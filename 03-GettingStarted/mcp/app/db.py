"""
Oracle connection pooling, read-only SQL guardrails, and query helpers.

Connection config priority (highest to lowest):
  1. ConnConfig passed directly to each function (per-call override)
  2. Environment variables: ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN

Pool sizing (env vars, applied globally):
  ORACLE_POOL_MIN, ORACLE_POOL_MAX, ORACLE_POOL_INCREMENT

Driver mode (env var, global — set once per process):
  ORACLE_DRIVER_MODE=thin|thick  (default: thin)
  ORACLE_CLIENT_LIB_DIR          (required for thick mode)
"""

from __future__ import annotations

import os
import re
from contextvars import ContextVar, Token
from dataclasses import dataclass, field
from typing import Any

import oracledb

# One pool per (user, dsn) pair, shared across callers with the same credentials.
_pools: dict[tuple[str, str], oracledb.ConnectionPool] = {}
_client_initialized = False

# Per-request default connection injected via HTTP headers (see OracleHeaderMiddleware).
# Falls back to env vars if not set.
_session_conn: ContextVar[ConnConfig | None] = ContextVar("_session_conn", default=None)


# ---------------------------------------------------------------------------
# Connection configuration
# ---------------------------------------------------------------------------

@dataclass
class ConnConfig:
    """Oracle connection parameters for a single caller."""
    user: str
    password: str
    dsn: str
    pool_min: int = field(default=1)
    pool_max: int = field(default=5)
    pool_increment: int = field(default=1)

    @classmethod
    def from_env(cls) -> "ConnConfig":
        """Build a ConnConfig from environment variables. Raises if any required var is missing."""
        user = os.environ.get("ORACLE_USER", "")
        password = os.environ.get("ORACLE_PASSWORD", "")
        dsn = os.environ.get("ORACLE_DSN", "")
        if not user or not password or not dsn:
            raise RuntimeError(
                "No connection provided and server has no default Oracle config. "
                "Pass connection={\"user\": ..., \"password\": ..., \"dsn\": ...} to the tool."
            )
        return cls(
            user=user,
            password=password,
            dsn=dsn,
            pool_min=_env_int("ORACLE_POOL_MIN", 1),
            pool_max=_env_int("ORACLE_POOL_MAX", 5),
            pool_increment=_env_int("ORACLE_POOL_INCREMENT", 1),
        )


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    return int(raw)


# ---------------------------------------------------------------------------
# Driver / pool management
# ---------------------------------------------------------------------------

def _init_oracle_client_if_needed() -> None:
    global _client_initialized
    if _client_initialized:
        return

    mode = os.environ.get("ORACLE_DRIVER_MODE", "thin").strip().lower()
    if mode not in ("thin", "thick"):
        raise RuntimeError("ORACLE_DRIVER_MODE must be either 'thin' or 'thick'.")

    if mode == "thick":
        lib_dir = os.environ.get("ORACLE_CLIENT_LIB_DIR", "").strip()
        if not lib_dir:
            raise RuntimeError(
                "ORACLE_CLIENT_LIB_DIR is required when ORACLE_DRIVER_MODE=thick."
            )
        oracledb.init_oracle_client(lib_dir=lib_dir)

    _client_initialized = True


def get_pool(cfg: ConnConfig) -> oracledb.ConnectionPool:
    """Return (creating if needed) a pool for this (user, dsn) pair."""
    _init_oracle_client_if_needed()

    key = (cfg.user.upper(), cfg.dsn)
    if key in _pools:
        return _pools[key]

    pool = oracledb.create_pool(
        user=cfg.user,
        password=cfg.password,
        dsn=cfg.dsn,
        min=cfg.pool_min,
        max=cfg.pool_max,
        increment=cfg.pool_increment,
    )
    _pools[key] = pool
    return pool


def set_session_conn(cfg: ConnConfig | None) -> Token:
    """Store a per-request default connection (called by OracleHeaderMiddleware)."""
    return _session_conn.set(cfg)


def reset_session_conn(token: Token) -> None:
    """Restore the previous context value after the request completes."""
    _session_conn.reset(token)


def _resolve_cfg(cfg: ConnConfig | None) -> ConnConfig:
    """Return the provided config, the per-request session config, or fall back to env vars.

    Priority (highest → lowest):
      1. `connection` dict passed explicitly to the tool call
      2. Credentials injected via HTTP headers (X-Oracle-User / -Password / -DSN)
      3. ORACLE_USER / ORACLE_PASSWORD / ORACLE_DSN environment variables
    """
    if cfg is not None:
        return cfg
    session_cfg = _session_conn.get()
    if session_cfg is not None:
        return session_cfg
    return ConnConfig.from_env()


def close_all_pools() -> None:
    """Close every open connection pool (called at process exit)."""
    for key in list(_pools):
        try:
            _pools.pop(key).close()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# SQL validation
# ---------------------------------------------------------------------------

def _remove_sql_comments(sql: str) -> str:
    s = re.sub(r"/\*.*?\*/", "", sql, flags=re.DOTALL)
    lines = []
    for line in s.splitlines():
        if "--" in line:
            line = line.split("--", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def validate_select_only_sql(sql: str) -> str:
    cleaned = _remove_sql_comments(sql).strip()
    if not cleaned:
        raise ValueError("SQL is empty.")

    parts = [p.strip() for p in cleaned.split(";")]
    non_empty = [p for p in parts if p]
    if len(non_empty) > 1:
        raise ValueError("Only a single SQL statement is allowed (no multiple statements).")

    stmt = non_empty[0] if non_empty else ""
    upper = stmt.upper()

    if re.search(r"\bFOR\s+UPDATE\b", upper):
        raise ValueError("FOR UPDATE is not allowed.")
    if re.search(r"\b(INSERT|UPDATE|DELETE|MERGE|TRUNCATE|DROP|ALTER|CREATE|GRANT|REVOKE)\b", upper):
        raise ValueError("Only SELECT queries are allowed.")

    first_word = re.match(r"^\s*(\w+)", stmt, re.IGNORECASE)
    if not first_word:
        raise ValueError("Could not parse SQL statement.")
    if first_word.group(1).upper() not in ("SELECT", "WITH"):
        raise ValueError("Only SELECT (or WITH ... SELECT) statements are allowed.")

    return stmt


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def _rows_to_jsonable(rows: list[Any], cursor: oracledb.Cursor) -> list[dict[str, Any]]:
    columns = [d[0] for d in (cursor.description or [])]
    out: list[dict[str, Any]] = []
    for row in rows:
        item: dict[str, Any] = {}
        for i, col in enumerate(columns):
            val = row[i]
            if isinstance(val, (bytes, bytearray)):
                item[col] = val.hex() if len(val) > 64 else f"<bytes len={len(val)}>"
            else:
                item[col] = val
        out.append(item)
    return out


def run_select_impl(
    sql: str,
    binds: dict[str, Any] | None = None,
    max_rows: int = 100,
    cfg: ConnConfig | None = None,
) -> dict[str, Any]:
    stmt = validate_select_only_sql(sql)
    if max_rows < 1:
        raise ValueError("max_rows must be at least 1.")

    pool = get_pool(_resolve_cfg(cfg))
    binds = binds or {}

    with pool.acquire() as conn:
        with conn.cursor() as cursor:
            cursor.execute(stmt, binds)
            rows = cursor.fetchmany(max_rows + 1)
            truncated = len(rows) > max_rows
            if truncated:
                rows = rows[:max_rows]
            return {
                "columns": [d[0] for d in (cursor.description or [])],
                "rows": _rows_to_jsonable(rows, cursor),
                "row_count": len(rows),
                "truncated": truncated,
            }


def list_tables_impl(owner: str | None = None, cfg: ConnConfig | None = None) -> dict[str, Any]:
    pool = get_pool(_resolve_cfg(cfg))
    with pool.acquire() as conn:
        with conn.cursor() as cursor:
            if owner:
                cursor.execute(
                    """
                    SELECT owner, table_name
                    FROM all_tables
                    WHERE owner = :owner
                    ORDER BY owner, table_name
                    """,
                    {"owner": owner.upper()},
                )
            else:
                cursor.execute(
                    """
                    SELECT USER AS owner, table_name
                    FROM user_tables
                    ORDER BY table_name
                    """
                )
            rows = cursor.fetchall()
            cols = [d[0] for d in (cursor.description or [])]
            return {
                "columns": cols,
                "rows": _rows_to_jsonable(rows, cursor),
                "row_count": len(rows),
            }


def describe_table_impl(
    table_name: str,
    owner: str | None = None,
    cfg: ConnConfig | None = None,
) -> dict[str, Any]:
    if not table_name or not table_name.strip():
        raise ValueError("table_name is required.")

    tname = table_name.strip().upper()
    pool = get_pool(_resolve_cfg(cfg))

    with pool.acquire() as conn:
        with conn.cursor() as cursor:
            if owner:
                cursor.execute(
                    """
                    SELECT column_id, column_name, data_type, nullable,
                           data_length, data_precision, data_scale
                    FROM all_tab_columns
                    WHERE owner = :owner AND table_name = :table_name
                    ORDER BY column_id
                    """,
                    {"owner": owner.upper(), "table_name": tname},
                )
            else:
                cursor.execute(
                    """
                    SELECT column_id, column_name, data_type, nullable,
                           data_length, data_precision, data_scale
                    FROM user_tab_columns
                    WHERE table_name = :table_name
                    ORDER BY column_id
                    """,
                    {"table_name": tname},
                )
            rows = cursor.fetchall()
            cols = [d[0] for d in (cursor.description or [])]
            return {
                "columns": cols,
                "rows": _rows_to_jsonable(rows, cursor),
                "row_count": len(rows),
            }

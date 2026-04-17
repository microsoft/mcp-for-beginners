"""
Oracle connection pooling, read-only SQL guardrails, and query helpers.

Configuration via environment variables:
  ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN (required for live DB)
  ORACLE_POOL_MIN, ORACLE_POOL_MAX, ORACLE_POOL_INCREMENT (optional)
  ORACLE_DRIVER_MODE=thin|thick (optional, default: thin)
  ORACLE_CLIENT_LIB_DIR=/path/to/instantclient (required for thick mode)
"""

from __future__ import annotations

import os
import re
from typing import Any

import oracledb

_pool: oracledb.ConnectionPool | None = None
_client_initialized = False


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    return int(raw)


def _init_oracle_client_if_needed() -> None:
    """
    Initialize python-oracledb client mode once.

    - thin mode (default): no client libraries required
    - thick mode: requires ORACLE_CLIENT_LIB_DIR (Instant Client path)
    """
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


def get_pool() -> oracledb.ConnectionPool:
    """Create (once) and return the Oracle connection pool."""
    global _pool
    if _pool is not None:
        return _pool

    _init_oracle_client_if_needed()

    user = os.environ.get("ORACLE_USER")
    password = os.environ.get("ORACLE_PASSWORD")
    dsn = os.environ.get("ORACLE_DSN")
    if not user or not password or not dsn:
        raise RuntimeError(
            "Missing Oracle configuration. Set ORACLE_USER, ORACLE_PASSWORD, and ORACLE_DSN."
        )

    _pool = oracledb.create_pool(
        user=user,
        password=password,
        dsn=dsn,
        min=_env_int("ORACLE_POOL_MIN", 1),
        max=_env_int("ORACLE_POOL_MAX", 5),
        increment=_env_int("ORACLE_POOL_INCREMENT", 1),
    )
    return _pool


def close_pool() -> None:
    """Close the pool if it was opened."""
    global _pool
    if _pool is not None:
        try:
            _pool.close()
        finally:
            _pool = None


def _remove_sql_comments(sql: str) -> str:
    """Strip -- line and /* */ block comments (best-effort)."""
    s = sql
    # Block comments
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.DOTALL)
    # Line comments
    lines = []
    for line in s.splitlines():
        if "--" in line:
            line = line.split("--", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def validate_select_only_sql(sql: str) -> str:
    """
    Ensure SQL is a single read-only SELECT (or WITH ... SELECT) statement.

    Returns the single statement to execute (trimmed).
    Raises ValueError with a user-facing message if not allowed.
    """
    cleaned = _remove_sql_comments(sql).strip()
    if not cleaned:
        raise ValueError("SQL is empty.")

    parts = [p.strip() for p in cleaned.split(";")]
    non_empty = [p for p in parts if p]
    if len(non_empty) > 1:
        raise ValueError("Only a single SQL statement is allowed (no multiple statements).")

    stmt = non_empty[0] if non_empty else ""

    # Disallow obvious write / lock patterns in standalone SQL
    upper = stmt.upper()
    if re.search(r"\bFOR\s+UPDATE\b", upper):
        raise ValueError("FOR UPDATE is not allowed.")
    if re.search(r"\b(INSERT|UPDATE|DELETE|MERGE|TRUNCATE|DROP|ALTER|CREATE|GRANT|REVOKE)\b", upper):
        raise ValueError("Only SELECT queries are allowed.")

    first_word = re.match(r"^\s*(\w+)", stmt, re.IGNORECASE)
    if not first_word:
        raise ValueError("Could not parse SQL statement.")
    fw = first_word.group(1).upper()
    if fw not in ("SELECT", "WITH"):
        raise ValueError("Only SELECT (or WITH ... SELECT) statements are allowed.")

    return stmt


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
) -> dict[str, Any]:
    """Execute a validated SELECT and return structured rows."""
    stmt = validate_select_only_sql(sql)
    if max_rows < 1:
        raise ValueError("max_rows must be at least 1.")

    pool = get_pool()
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


def list_tables_impl(owner: str | None = None) -> dict[str, Any]:
    """List tables visible to the session (user tables, or ALL_TABLES for a schema)."""
    pool = get_pool()
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


def describe_table_impl(table_name: str, owner: str | None = None) -> dict[str, Any]:
    """Describe columns for a table (USER or ALL)."""
    if not table_name or not table_name.strip():
        raise ValueError("table_name is required.")

    tname = table_name.strip().upper()
    pool = get_pool()

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

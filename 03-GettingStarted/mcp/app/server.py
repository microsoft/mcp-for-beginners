"""
MCP server exposing read-only Oracle database tools + Knowledge Central search.

Transport:
  stdio (default, local dev):  python server.py
  HTTP (K8s / shared):         MCP_TRANSPORT=streamable-http python server.py

Database connection — three ways to supply credentials (highest → lowest priority):

  1. Per-call `connection` dict in the tool call:
       {"user": "alice", "password": "s3cr3t", "dsn": "host:1521/svc"}

  2. HTTP headers (recommended for the shared K8s deployment — set once in
     claude_desktop_config.json via mcp-remote --header flags):
       X-Oracle-User: alice
       X-Oracle-Password: s3cr3t
       X-Oracle-DSN: host:1521/svc

  3. Environment variables (useful for local dev):
       ORACLE_USER / ORACLE_PASSWORD / ORACLE_DSN

Team claude_desktop_config.json example:
  {
    "mcpServers": {
      "aria-oracle-kb": {
        "command": "npx",
        "args": [
          "mcp-remote", "http://<server-host>/mcp",
          "--header", "x-oracle-user:team_user",
          "--header", "x-oracle-password:team_pass",
          "--header", "x-oracle-dsn:host:1521/svc"
        ]
      }
    }
  }

Inspector: npx @modelcontextprotocol/inspector python server.py
"""

from __future__ import annotations

import atexit
import os
import traceback

from mcp.server.fastmcp import FastMCP

from db import (
    ConnConfig,
    close_all_pools,
    describe_table_impl,
    list_tables_impl,
    reset_session_conn,
    run_select_impl,
    set_session_conn,
)
from kb import DEFAULT_BASE_URL, fetch_kb_page, search_kb


# ---------------------------------------------------------------------------
# ASGI middleware — injects Oracle credentials from HTTP headers so each team
# only needs to configure their claude_desktop_config.json once.
# Uses a pure ASGI approach (no Starlette BaseHTTPMiddleware) so it is safe
# for streaming / chunked responses.
# ---------------------------------------------------------------------------

class OracleHeaderMiddleware:
    """Read X-Oracle-User / X-Oracle-Password / X-Oracle-DSN headers and set
    them as the per-request default connection via a context variable."""

    def __init__(self, app: object) -> None:
        self.app = app

    async def __call__(self, scope: dict, receive: object, send: object) -> None:
        if scope["type"] in ("http", "websocket"):
            headers = {k.lower(): v for k, v in scope.get("headers", [])}
            user = headers.get(b"x-oracle-user", b"").decode("utf-8", errors="ignore").strip()
            password = headers.get(b"x-oracle-password", b"").decode("utf-8", errors="ignore").strip()
            dsn = headers.get(b"x-oracle-dsn", b"").decode("utf-8", errors="ignore").strip()
            if user and password and dsn:
                token = set_session_conn(ConnConfig(user=user, password=password, dsn=dsn))
                try:
                    await self.app(scope, receive, send)
                finally:
                    reset_session_conn(token)
                return
        await self.app(scope, receive, send)

mcp = FastMCP(
    "KnowledgeCentralAndOracleMCP",
    host=os.environ.get("MCP_HOST", "0.0.0.0"),
    port=int(os.environ.get("MCP_PORT", "8000")),
)


def _tool_error(exc: BaseException) -> dict:
    out: dict = {"error": str(exc), "type": type(exc).__name__}
    if os.environ.get("ORACLE_MCP_DEBUG"):
        out["traceback"] = traceback.format_exc()
    return out


def _parse_conn(connection: dict | None) -> ConnConfig | None:
    """Convert the raw dict from a tool call into a ConnConfig, or None to use env vars."""
    if not connection:
        return None
    try:
        return ConnConfig(**connection)
    except TypeError as e:
        raise ValueError(
            f"Invalid connection dict: {e}. "
            "Expected keys: user, password, dsn (and optionally pool_min, pool_max, pool_increment)."
        ) from e


@mcp.tool()
def list_tables(
    owner: str | None = None,
    connection: dict | None = None,
) -> dict:
    """
    List Oracle tables.

    - `owner`: schema name to list (omit for the connected user's own tables).
    - `connection`: optional dict with keys `user`, `password`, `dsn` to connect
      to your own database instead of the server default.
    """
    try:
        return list_tables_impl(owner, cfg=_parse_conn(connection))
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def describe_table(
    table_name: str,
    owner: str | None = None,
    connection: dict | None = None,
) -> dict:
    """
    Describe columns for an Oracle table.

    - `connection`: optional dict with keys `user`, `password`, `dsn`.
    """
    try:
        return describe_table_impl(table_name, owner, cfg=_parse_conn(connection))
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def run_select(
    sql: str,
    binds: dict | None = None,
    max_rows: int = 100,
    connection: dict | None = None,
) -> dict:
    """
    Run a single read-only SELECT (or WITH ... SELECT) against Oracle.

    - `binds`: optional named bind variables, e.g. `{"status": "ACTIVE"}`.
    - `max_rows`: row cap (default 100).
    - `connection`: optional dict with keys `user`, `password`, `dsn`.
    """
    try:
        return run_select_impl(sql, binds=binds, max_rows=max_rows, cfg=_parse_conn(connection))
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def kb_fetch(url: str = DEFAULT_BASE_URL, max_chars: int = 12000) -> dict:
    """Fetch and parse one Knowledge Central page into text and links."""
    try:
        return fetch_kb_page(url=url, max_chars=max_chars)
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def kb_search(
    query: str,
    base_url: str = DEFAULT_BASE_URL,
    max_pages: int = 12,
    max_results: int = 5,
) -> dict:
    """Search Knowledge Central by crawling a limited set of public pages."""
    try:
        return search_kb(
            query=query,
            base_url=base_url,
            max_pages=max_pages,
            max_results=max_results,
        )
    except Exception as e:
        return _tool_error(e)


atexit.register(close_all_pools)

if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8000"))

    if transport == "streamable-http":
        import uvicorn
        # Wrap the FastMCP ASGI app with our header-injection middleware so
        # every team can supply their own Oracle credentials without touching
        # the shared server config.
        asgi_app = OracleHeaderMiddleware(mcp.streamable_http_app())
        uvicorn.run(asgi_app, host=host, port=port, log_level="info")
    else:
        mcp.run()

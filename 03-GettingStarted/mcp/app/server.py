"""
MCP server exposing read-only Oracle database tools (stdio transport).

Run: python server.py
Inspector: npx @modelcontextprotocol/inspector python server.py
"""

from __future__ import annotations

import atexit
import os
import traceback

from mcp.server.fastmcp import FastMCP

from db import (
    close_pool,
    describe_table_impl,
    list_tables_impl,
    run_select_impl,
)
from kb import DEFAULT_BASE_URL, fetch_kb_page, search_kb

mcp = FastMCP("KnowledgeCentralAndOracleMCP")


def _tool_error(exc: BaseException) -> dict:
    out: dict = {"error": str(exc), "type": type(exc).__name__}
    if os.environ.get("ORACLE_MCP_DEBUG"):
        out["traceback"] = traceback.format_exc()
    return out


@mcp.tool()
def list_tables(owner: str | None = None) -> dict:
    """List tables: current user's tables, or all tables in a schema (owner)."""
    try:
        return list_tables_impl(owner)
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def describe_table(table_name: str, owner: str | None = None) -> dict:
    """Describe columns for a table (user tables if owner omitted, else ALL_TAB_COLUMNS)."""
    try:
        return describe_table_impl(table_name, owner)
    except Exception as e:
        return _tool_error(e)


@mcp.tool()
def run_select(sql: str, binds: dict | None = None, max_rows: int = 100) -> dict:
    """Run a single read-only SELECT (or WITH ... SELECT). Optional bind dict and row cap."""
    try:
        return run_select_impl(sql, binds=binds, max_rows=max_rows)
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

# Clean up pool on exit
atexit.register(close_pool)

if __name__ == "__main__":
    mcp.run()

"""Unit tests for SQL validation and DB helpers (mocked pool)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import db as db_mod
from db import (
    ConnConfig,
    describe_table_impl,
    list_tables_impl,
    run_select_impl,
    validate_select_only_sql,
)

_FAKE_CFG = ConnConfig(user="u", password="p", dsn="host:1521/svc")


def test_validate_accepts_simple_select():
    s = validate_select_only_sql("SELECT 1 FROM dual")
    assert "SELECT" in s.upper()


def test_validate_accepts_with_cte():
    s = validate_select_only_sql(
        "WITH t AS (SELECT 1 AS x FROM dual) SELECT x FROM t"
    )
    assert s.upper().startswith("WITH")


def test_validate_rejects_insert():
    with pytest.raises(ValueError, match="Only SELECT"):
        validate_select_only_sql("INSERT INTO t VALUES (1)")


def test_validate_rejects_multiple_statements():
    with pytest.raises(ValueError, match="single"):
        validate_select_only_sql("SELECT 1 FROM dual; SELECT 2 FROM dual")


def test_validate_rejects_for_update():
    with pytest.raises(ValueError, match="FOR UPDATE"):
        validate_select_only_sql("SELECT * FROM t FOR UPDATE")


def test_validate_rejects_empty():
    with pytest.raises(ValueError):
        validate_select_only_sql("   ")


def _mock_pool_for_select(rows, columns):
    """Build a fake pool that returns one connection/cursor with fetchmany behavior."""
    pool = MagicMock()
    conn_cm = MagicMock()
    pool.acquire.return_value = conn_cm
    conn = MagicMock()
    conn_cm.__enter__.return_value = conn
    conn_cm.__exit__.return_value = None

    cur_cm = MagicMock()
    conn.cursor.return_value = cur_cm
    cursor = MagicMock()
    cur_cm.__enter__.return_value = cursor
    cur_cm.__exit__.return_value = None

    cursor.description = [(c,) for c in columns]
    cursor.fetchmany.return_value = rows
    return pool


@patch.object(db_mod, "get_pool")
def test_run_select_impl_returns_rows(mock_get_pool):
    mock_get_pool.return_value = _mock_pool_for_select(
        [(1, "hello")],
        ["ID", "MSG"],
    )
    out = run_select_impl("SELECT id, msg FROM t WHERE id = :id", {"id": 1}, max_rows=10, cfg=_FAKE_CFG)
    assert out["row_count"] == 1
    assert out["truncated"] is False
    assert out["columns"] == ["ID", "MSG"]
    assert out["rows"] == [{"ID": 1, "MSG": "hello"}]


@patch.object(db_mod, "get_pool")
def test_run_select_impl_truncates(mock_get_pool):
    rows = [(i,) for i in range(5)]
    mock_get_pool.return_value = _mock_pool_for_select(rows, ["N"])
    out = run_select_impl("SELECT n FROM t", max_rows=3, cfg=_FAKE_CFG)
    assert out["truncated"] is True
    assert out["row_count"] == 3
    assert len(out["rows"]) == 3


@patch.object(db_mod, "get_pool")
def test_list_tables_impl_user(mock_get_pool):
    pool = MagicMock()
    mock_get_pool.return_value = pool
    conn_cm = MagicMock()
    pool.acquire.return_value = conn_cm
    conn = MagicMock()
    conn_cm.__enter__.return_value = conn
    conn_cm.__exit__.return_value = None
    cur_cm = MagicMock()
    conn.cursor.return_value = cur_cm
    cursor = MagicMock()
    cur_cm.__enter__.return_value = cursor
    cur_cm.__exit__.return_value = None
    cursor.description = [("OWNER",), ("TABLE_NAME",)]
    cursor.fetchall.return_value = [("SCOTT", "EMP")]

    out = list_tables_impl(None, cfg=_FAKE_CFG)
    assert out["row_count"] == 1
    assert out["rows"][0]["TABLE_NAME"] == "EMP"


@patch.object(db_mod, "get_pool")
def test_describe_table_impl(mock_get_pool):
    pool = MagicMock()
    mock_get_pool.return_value = pool
    conn_cm = MagicMock()
    pool.acquire.return_value = conn_cm
    conn = MagicMock()
    conn_cm.__enter__.return_value = conn
    conn_cm.__exit__.return_value = None
    cur_cm = MagicMock()
    conn.cursor.return_value = cur_cm
    cursor = MagicMock()
    cur_cm.__enter__.return_value = cursor
    cur_cm.__exit__.return_value = None
    cursor.description = [("COLUMN_NAME",), ("DATA_TYPE",)]
    cursor.fetchall.return_value = [("ID", "NUMBER")]

    out = describe_table_impl("EMP", None, cfg=_FAKE_CFG)
    assert out["row_count"] == 1
    assert out["rows"][0]["COLUMN_NAME"] == "ID"


def test_server_tools_import():
    import server  # noqa: F401 — ensures package imports

    assert server.mcp.name == "KnowledgeCentralAndOracleMCP"

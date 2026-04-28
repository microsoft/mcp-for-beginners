"""
Live Oracle tests — run only when ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN are set.

Example:
  export ORACLE_USER=...
  export ORACLE_PASSWORD=...
  export ORACLE_DSN=host:1521/service
  pytest tests/test_integration_oracle.py -q
"""

from __future__ import annotations

import os

import pytest

from db import close_all_pools, describe_table_impl, list_tables_impl, run_select_impl


def _oracle_configured() -> bool:
    return bool(
        os.environ.get("ORACLE_USER")
        and os.environ.get("ORACLE_PASSWORD")
        and os.environ.get("ORACLE_DSN")
    )


pytestmark = pytest.mark.skipif(
    not _oracle_configured(),
    reason="Set ORACLE_USER, ORACLE_PASSWORD, ORACLE_DSN for integration tests.",
)


@pytest.fixture(autouse=True)
def reset_pool():
    """Ensure no stale pool between integration tests."""
    close_all_pools()
    yield
    close_all_pools()


def test_list_tables_smoke():
    out = list_tables_impl(None)
    assert "columns" in out and "rows" in out
    assert isinstance(out["rows"], list)


def test_run_select_dual():
    out = run_select_impl("SELECT 1 AS one FROM dual", max_rows=10)
    assert out["row_count"] >= 1
    row = out["rows"][0]
    val = row.get("ONE") or row.get("one")
    assert val is not None
    assert int(val) == 1


def test_describe_user_table_if_any():
    tables = list_tables_impl(None)
    if tables["row_count"] == 0:
        pytest.skip("No user tables to describe")
    first = tables["rows"][0]
    tname = first.get("TABLE_NAME") or first.get("table_name")
    assert tname
    desc = describe_table_impl(str(tname), None)
    assert desc["row_count"] >= 1

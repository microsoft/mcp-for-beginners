# Aria Knowledge + Oracle Database MCP Tool (sample)

Public Aria Knowledge Central tools plus read-only Oracle tools exposed through [Model Context Protocol](https://modelcontextprotocol.io/) (Python + FastMCP).

## Tools

| Tool | Purpose |
|------|---------|
| `list_tables` | Tables in your schema (`owner` omitted) or in a given schema (`owner`). |
| `describe_table` | Column metadata for a table (user tables or `owner` + table). |
| `run_select` | Single **SELECT** / **WITH … SELECT** only, optional binds, row cap. |
| `kb_fetch` | Fetch one KB page (`https://knowledge.ariasystems.net/` by default) and return title/text/links. |
| `kb_search` | Crawl a limited number of KB pages and return ranked lexical matches for a query. |

Non-SELECT SQL (DML/DDL), multiple statements, and `FOR UPDATE` are rejected.

## Setup

```bash
cd 03-GettingStarted/mcp/dbs
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Environment variables

**Required** to run tools against a real database:

| Variable | Description |
|----------|----------------|
| `ORACLE_USER` | Database user |
| `ORACLE_PASSWORD` | Password |
| `ORACLE_DSN` | e.g. `host:1521/service_name` or Easy Connect string |

**Optional** pool tuning:

| Variable | Default |
|----------|---------|
| `ORACLE_POOL_MIN` | `1` |
| `ORACLE_POOL_MAX` | `5` |
| `ORACLE_POOL_INCREMENT` | `1` |

**Optional** debugging:

| Variable | Effect |
|----------|--------|
| `ORACLE_MCP_DEBUG` | If set, tool error responses include a Python traceback |

The pool is created lazily on the first tool call that needs the database.

### Knowledge base behavior

- KB tools use public pages from `https://knowledge.ariasystems.net/` (no auth).
- `kb_search` uses bounded crawling (`max_pages`) for predictable runtime.
- Search is lexical ranking (term overlap), designed for deterministic tool behavior.

### Driver mode (thin vs thick)

By default, `python-oracledb` runs in **thin** mode.
If your DB requires Native Network Encryption (NNE), use **thick** mode:

| Variable | Value |
|----------|-------|
| `ORACLE_DRIVER_MODE` | `thick` |
| `ORACLE_CLIENT_LIB_DIR` | Absolute path to Oracle Instant Client directory |

Example:

```bash
export ORACLE_DRIVER_MODE=thick
export ORACLE_CLIENT_LIB_DIR=/opt/oracle/instantclient_23_3
```

If thick mode is enabled without `ORACLE_CLIENT_LIB_DIR`, server tools will return a clear configuration error.

### Download Oracle Instant Client

Official Oracle downloads:

- Main downloads page: [https://www.oracle.com/database/technologies/instant-client/downloads.html](https://www.oracle.com/database/technologies/instant-client/downloads.html)
- macOS Intel (x86_64): [https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html](https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html)
- macOS Apple Silicon (ARM64): [https://www.oracle.com/database/technologies/instant-client/macos-arm64-downloads.html](https://www.oracle.com/database/technologies/instant-client/macos-arm64-downloads.html)

## Run the server (stdio)

```bash
python server.py
```

## Example tool calls

- Find release notes in KB:
  - `kb_search(query="Aria Billing Release 70", max_pages=12, max_results=5)`
- Read one KB page:
  - `kb_fetch(url="https://knowledge.ariasystems.net/")`
- Query DB for matching account data:
  - `run_select(sql="SELECT account_no, status FROM accounts WHERE status = :s", binds={"s":"ACTIVE"})`

## Test with MCP Inspector

From this directory:

```bash
npx @modelcontextprotocol/inspector python server.py
```

## Tests

**Unit tests** (mocked Oracle — no DB required):

```bash
pytest tests/test_server.py -q
pytest tests/test_kb.py -q
```

**All tests** (integration tests skip unless Oracle env vars are set):

```bash
pytest tests/ -q
```

**Live Oracle integration tests** (set credentials first):

```bash
export ORACLE_USER=your_user
export ORACLE_PASSWORD=your_password
export ORACLE_DSN=host:1521/your_service
export ORACLE_DRIVER_MODE=thick
export ORACLE_CLIENT_LIB_DIR=/opt/oracle/instantclient_23_3

pytest tests/test_integration_oracle.py -q
```

## Files

- `server.py` — FastMCP server and tool entrypoints
- `db.py` — Pool management, SQL validation, and query helpers
- `tests/test_server.py` — Unit tests
- `tests/test_integration_oracle.py` — Optional live DB smoke tests

# MCP Calculator Server (Python)



A simple Model Context Protocol (MCP) server implementation in Python that provides basic calculator functionality.


## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install the MCP Python SDK directly:

```bash
pip install mcp>=1.18.0
```

## Usage

### Running the Server

The server is designed to be used by MCP clients (like Claude Desktop). To start the server:

```bash
python mcp_calculator_server.py
```

**Note**: When run directly in a terminal, you'll see JSON-RPC validation errors. This is normal behavior - the server is waiting for properly formatted MCP client messages.

### Testing the Functions

To test that the calculator functions work correctly:

```bash
python test_calculator.py
```

## Troubleshooting

### Import Errors

If you see `ModuleNotFoundError: No module named 'mcp'`, install the MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC Errors When Running Directly

Errors like "Invalid JSON: EOF while parsing a value" when running the server directly are expected. The server needs MCP client messages, not direct terminal input.
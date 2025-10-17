# MCP Calculator Server (Python)# Sample



A simple Model Context Protocol (MCP) server implementation in Python that provides basic calculator functionality.This is a Python sample for an MCP Server



## 🔧 Fixed IssuesHere's what the calculator portion looks like:



This calculator server has been updated to work with the current MCP Python SDK:```python

@mcp.tool()

- ✅ **Fixed import errors**: Updated to use `from mcp.server.fastmcp import FastMCP`def add(a: float, b: float) -> float:

- ✅ **Removed deprecated transport imports**: No longer uses `mcp.server.transports.stdio`    """Add two numbers together and return the result."""

- ✅ **Updated server initialization**: Uses `FastMCP("Calculator MCP Server")` without version parameter    return a + b

- ✅ **Modern server startup**: Uses `mcp.run()` instead of `asyncio.run(serve_stdio(mcp))`

@mcp.tool()

## Featuresdef subtract(a: float, b: float) -> float:

    """Subtract b from a and return the result."""

This server provides four calculator tools:    return a - b



```python@mcp.tool()

@mcp.tool()def multiply(a: float, b: float) -> float:

def add(a: float, b: float) -> float:    """Multiply two numbers together and return the result."""

    """Add two numbers together and return the result."""    return a * b

    return a + b

@mcp.tool()

@mcp.tool()def divide(a: float, b: float) -> float:

def subtract(a: float, b: float) -> float:    """

    """Subtract b from a and return the result."""    Divide a by b and return the result.

    return a - b    

    Raises:

@mcp.tool()        ValueError: If b is zero

def multiply(a: float, b: float) -> float:    """

    """Multiply two numbers together and return the result."""    if b == 0:

    return a * b        raise ValueError("Cannot divide by zero")

    return a / b

@mcp.tool()```

def divide(a: float, b: float) -> float:

    """## Install

    Divide a by b and return the result.

    Run the following command:

    Raises:

        ValueError: If b is zero```bash

    """pip install mcp

    if b == 0:```

        raise ValueError("Cannot divide by zero")

    return a / b## Run

```

```bash

## Installationpython mcp_calculator_server.py

```
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
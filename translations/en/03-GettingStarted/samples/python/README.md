# MCP Calculator Server (Python)

A simple implementation of a Model Context Protocol (MCP) server in Python that offers basic calculator functionality.

## Installation

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Or install the MCP Python SDK directly:

```bash
pip install mcp>=1.18.0
```

## Usage

### Running the Server

The server is intended for use with MCP clients (such as Claude Desktop). To start the server:

```bash
python mcp_calculator_server.py
```

**Note**: If you run the server directly in a terminal, you may encounter JSON-RPC validation errors. This is normal behavior—the server is waiting for properly formatted messages from an MCP client.

### Testing the Functions

To verify that the calculator functions are working correctly:

```bash
python test_calculator.py
```

## Troubleshooting

### Import Errors

If you encounter `ModuleNotFoundError: No module named 'mcp'`, install the MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC Errors When Running Directly

Errors like "Invalid JSON: EOF while parsing a value" when running the server directly are expected. The server is designed to process messages from MCP clients, not direct input from the terminal.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
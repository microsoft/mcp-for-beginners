# MCP Calculator Server (Python)



Na simple Model Context Protocol (MCP) server wey dem do for Python wey fit do basic calculator work.


## Installation

Make sure say you install wetin you need:

```bash
pip install -r requirements.txt
```

Or make you install MCP Python SDK direct:

```bash
pip install mcp>=1.18.0
```

## Usage

### How to Run the Server

Dis server na for MCP clients (like Claude Desktop) to use. To start am:

```bash
python mcp_calculator_server.py
```

**Note**: If you run am direct for terminal, you go see JSON-RPC validation errors. No worry, na normal - the server dey wait for MCP client messages wey dey well formatted.

### How to Test the Functions

To check say the calculator functions dey work well:

```bash
python test_calculator.py
```

## Troubleshooting

### Import Errors

If you see `ModuleNotFoundError: No module named 'mcp'`, make sure say you don install MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC Errors When Running Directly

Errors like "Invalid JSON: EOF while parsing a value" when you run the server direct na normal. The server dey need MCP client messages, e no dey work with direct terminal input.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey accurate well. Di original dokyument for di language wey dem take write am first na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Calculator Server (Python)



Simple Model Context Protocol (MCP) server wey dem implement for Python wey dey provide basic calculator functionality.


## Installation

Install di required dependencies:

```bash
pip install -r requirements.txt
```

Or install di MCP Python SDK direct:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Usage

### Running di Server

Di server dey made so dat MCP clients (like Claude Desktop) go fit use am. To start di server:

```bash
python mcp_calculator_server.py
```

**Note**: If you run am direct for terminal, you go see JSON-RPC validation errors. Dis na normal behaviour - di server dey wait for properly formatted MCP client messages.

### Testing di Functions

To test sey di calculator functions dey work correct:

```bash
python test_calculator.py
```

## Troubleshooting

### Import Errors

If you see `ModuleNotFoundError: No module named 'mcp'`, install di MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC Errors When You Run Am Direct

Errors like "Invalid JSON: EOF while parsing a value" wen you run di server direct na normal tin. Di server need MCP client messages, no be direct terminal input.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
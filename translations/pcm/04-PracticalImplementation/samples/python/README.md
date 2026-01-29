# Model Context Protocol (MCP) Python Implementation

Dis repository get Python implementation of di Model Context Protocol (MCP), wey dey show how to create server and client application wey go dey communicate wit MCP standard.

## Overview

Di MCP implementation get two main parts:

1. **MCP Server (`server.py`)** - Na server wey dey provide:
   - **Tools**: Functions wey person fit call from far place
   - **Resources**: Data wey person fit collect
   - **Prompts**: Templates wey dey help generate prompts for language models

2. **MCP Client (`client.py`)** - Na client application wey dey connect to di server and use di features

## Features

Dis implementation dey show some important MCP features:

### Tools
- `completion` - E dey generate text completions from AI models (na simulation)
- `add` - Na simple calculator wey dey add two numbers

### Resources
- `models://` - E dey return information about di AI models wey dey available
- `greeting://{name}` - E dey return personalized greeting for di name wey you give am

### Prompts
- `review_code` - E dey generate prompt for reviewing code

## Installation

To use dis MCP implementation, install di packages wey you need:

```powershell
pip install mcp-server mcp-client
```

## Running di Server and Client

### How to Start di Server

Run di server for one terminal window:

```powershell
python server.py
```

You fit also run di server for development mode wit di MCP CLI:

```powershell
mcp dev server.py
```

Or install am for Claude Desktop (if e dey available):

```powershell
mcp install server.py
```

### How to Run di Client

Run di client for another terminal window:

```powershell
python client.py
```

Dis one go connect to di server and show all di features wey dey available.

### How di Client Work

Di client (`client.py`) dey show all di MCP features:

```powershell
python client.py
```

Dis one go connect to di server and use all di features like tools, resources, and prompts. Di output go show:

1. Result for calculator tool (5 + 7 = 12)
2. Response from completion tool for "Wetin be di meaning of life?"
3. List of di AI models wey dey available
4. Personalized greeting for "MCP Explorer"
5. Code review prompt template

## Implementation Details

Di server dey use `FastMCP` API, wey dey provide high-level way to define MCP services. Dis na example of how tools dey defined:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Di client dey use MCP client library to connect and call di server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Learn More

To sabi more about MCP, visit: https://modelcontextprotocol.io/

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
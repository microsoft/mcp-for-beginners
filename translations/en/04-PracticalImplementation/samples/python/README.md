# Model Context Protocol (MCP) Python Implementation

This repository contains a Python implementation of the Model Context Protocol (MCP), showing how to build both a server and client application that communicate using the MCP standard.

## Overview

The MCP implementation includes two main parts:

1. **MCP Server (`server.py`)** - A server that provides:
   - **Tools**: Functions that can be called remotely
   - **Resources**: Data that can be accessed
   - **Prompts**: Templates for generating prompts for language models

2. **MCP Client (`client.py`)** - A client application that connects to the server and uses its features

## Features

This implementation showcases several key MCP features:

### Tools
- `completion` - Generates text completions from AI models (simulated)
- `add` - Simple calculator that adds two numbers

### Resources
- `models://` - Returns information about available AI models
- `greeting://{name}` - Returns a personalized greeting for a given name

### Prompts
- `review_code` - Generates a prompt for reviewing code

## Installation

To use this MCP implementation, install the required packages:

```powershell
pip install mcp-server mcp-client
```

## Running the Server and Client

### Starting the Server

Run the server in one terminal window:

```powershell
python server.py
```

The server can also be run in development mode using the MCP CLI:

```powershell
mcp dev server.py
```

Or installed in Claude Desktop (if available):

```powershell
mcp install server.py
```

### Running the Client

Run the client in another terminal window:

```powershell
python client.py
```

This will connect to the server and demonstrate all available features.

### Client Usage

The client (`client.py`) demonstrates all the MCP capabilities:

```powershell
python client.py
```

This will connect to the server and test all features including tools, resources, and prompts. The output will show:

1. Calculator tool result (5 + 7 = 12)
2. Completion tool response to "What is the meaning of life?"
3. List of available AI models
4. Personalized greeting for "MCP Explorer"
5. Code review prompt template

## Implementation Details

The server is built using the `FastMCP` API, which offers high-level abstractions for defining MCP services. Here's a simplified example of how tools are defined:

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

The client uses the MCP client library to connect to and call the server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Learn More

For more information about MCP, visit: https://modelcontextprotocol.io/

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
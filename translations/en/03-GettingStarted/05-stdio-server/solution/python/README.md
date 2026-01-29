# MCP stdio Server - Python Solution

> **⚠️ Important**: This solution has been updated to use the **stdio transport** as recommended by MCP Specification 2025-06-18. The original SSE transport has been deprecated.

## Overview

This Python solution demonstrates how to build an MCP server using the current stdio transport. The stdio transport is simpler, more secure, and provides better performance than the deprecated SSE approach.

## Prerequisites

- Python 3.8 or later
- It is recommended to install `uv` for package management. See [instructions](https://docs.astral.sh/uv/#highlights)

## Setup Instructions

### Step 1: Create a virtual environment

```bash
python -m venv venv
```

### Step 2: Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install the dependencies

```bash
pip install mcp
```

## Running the Server

The stdio server operates differently from the old SSE server. Instead of starting a web server, it communicates through stdin/stdout:

```bash
python server.py
```

**Important**: The server will appear to hang - this is normal! It's waiting for JSON-RPC messages from stdin.

## Testing the Server

### Method 1: Using the MCP Inspector (Recommended)

```bash
npx @modelcontextprotocol/inspector python server.py
```

This will:
1. Launch your server as a subprocess
2. Open a web interface for testing
3. Allow you to test all server tools interactively

### Method 2: Direct JSON-RPC testing

You can also test by sending JSON-RPC messages directly:

1. Start the server: `python server.py`
2. Send a JSON-RPC message (example):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. The server will respond with available tools

### Available Tools

The server provides these tools:

- **add(a, b)**: Add two numbers together
- **multiply(a, b)**: Multiply two numbers together  
- **get_greeting(name)**: Generate a personalized greeting
- **get_server_info()**: Get information about the server

### Testing with Claude Desktop

To use this server with Claude Desktop, add this configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Key Differences from SSE

**stdio transport (Current):**
- ✅ Simpler setup - no web server needed
- ✅ Better security - no HTTP endpoints
- ✅ Subprocess-based communication
- ✅ JSON-RPC over stdin/stdout
- ✅ Better performance

**SSE transport (Deprecated):**
- ❌ Required HTTP server setup
- ❌ Needed web framework (Starlette/FastAPI)
- ❌ More complex routing and session management
- ❌ Additional security considerations
- ❌ Now deprecated in MCP 2025-06-18

## Debugging Tips

- Use `stderr` for logging (never `stdout`)
- Test with the Inspector for visual debugging
- Ensure all JSON messages are newline-delimited
- Check that the server starts without errors

This solution follows the current MCP specification and demonstrates best practices for stdio transport implementation.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the definitive source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
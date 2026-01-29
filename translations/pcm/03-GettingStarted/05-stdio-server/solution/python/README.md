# MCP stdio Server - Python Solution

> **⚠️ Important**: Dis solution don update to use **stdio transport** as MCP Specification 2025-06-18 recommend. Di old SSE transport don comot.

## Overview

Dis Python solution dey show how you fit build MCP server wey dey use di current stdio transport. Di stdio transport simple pass, e secure well-well, and e dey perform better pass di old SSE method.

## Prerequisites

- Python 3.8 or higher
- E good make you install `uv` for package management, check [instructions](https://docs.astral.sh/uv/#highlights)

## Setup Instructions

### Step 1: Create virtual environment

```bash
python -m venv venv
```

### Step 2: Activate di virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install di dependencies

```bash
pip install mcp
```

## Running di Server

Di stdio server dey run different from di old SSE server. Instead of starting web server, e dey communicate through stdin/stdout:

```bash
python server.py
```

**Important**: Di server go look like say e don hang - e normal! E dey wait for JSON-RPC messages from stdin.

## Testing di Server

### Method 1: Use MCP Inspector (Recommended)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Dis one go:
1. Start your server as subprocess
2. Open web interface for testing
3. Allow you test all server tools interactively

### Method 2: Direct JSON-RPC testing

You fit test am by sending JSON-RPC messages directly:

1. Start di server: `python server.py`
2. Send JSON-RPC message (example):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Di server go reply with di tools wey dey available

### Available Tools

Di server get dis tools:

- **add(a, b)**: Add two numbers together
- **multiply(a, b)**: Multiply two numbers together  
- **get_greeting(name)**: Create personalized greeting
- **get_server_info()**: Get info about di server

### Testing with Claude Desktop

To use dis server with Claude Desktop, add dis configuration to your `claude_desktop_config.json`:

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
- ✅ Setup dey easy - no need web server
- ✅ Better security - no HTTP endpoints
- ✅ Subprocess-based communication
- ✅ JSON-RPC dey use stdin/stdout
- ✅ Better performance

**SSE transport (Deprecated):**
- ❌ E need HTTP server setup
- ❌ E need web framework (Starlette/FastAPI)
- ❌ Routing and session management dey more complex
- ❌ E get extra security wahala
- ❌ MCP 2025-06-18 don comot am

## Debugging Tips

- Use `stderr` for logging (no use `stdout`)
- Test with Inspector for visual debugging
- Make sure all JSON messages dey newline-delimited
- Check say di server start without errors

Dis solution dey follow di current MCP specification and e dey show best practices for stdio transport implementation.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for di native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
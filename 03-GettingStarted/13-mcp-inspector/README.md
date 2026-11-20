# Debugging with MCP Inspector

> [!NOTE]
> Commands using `--sse` and URLs ending in `/sse` test the legacy HTTP+SSE
> transport. For a new MCP `2026-07-28` server, use an Inspector version that
> supports Streamable HTTP and select that transport instead.

The **MCP Inspector** is an essential debugging tool that lets you interactively test and troubleshoot your MCP servers without needing a full AI host application. Think of it as "Postman for MCP" - it provides a visual interface to send requests, view responses, and understand how your server behaves.

## Why Use MCP Inspector?

When building MCP servers, you'll often encounter these challenges:

- **"Is my server even running?"** - Inspector shows connection status
- **"Are my tools registered correctly?"** - Inspector lists all available tools
- **"What's the response format?"** - Inspector displays full JSON responses
- **"Why isn't this tool working?"** - Inspector shows detailed error messages

## Prerequisites

- Node.js 18+ installed
- npm (comes with Node.js)
- An MCP server to test (see [Module 3.1 - First Server](../01-first-server/README.md))

## Installation

### Option 1: Run with npx (Recommended for Quick Testing)

```bash
npx @modelcontextprotocol/inspector
```

### Option 2: Install Globally

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Option 3: Add to Your Project

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Add to `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Connecting to Your Server

### stdio Servers (Local Process)

For servers that communicate via standard input/output:

The Inspector starts your server with only a minimal environment (such as `HOME` and `PATH`), so variables you set in your shell, for example `OPENAI_API_KEY=xxx npx ...`, don't reach the server. Pass them with `-e` instead:

```bash
# Python server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js server
npx @modelcontextprotocol/inspector node ./build/index.js

# With environment variables for the server (-e KEY=VALUE, repeatable)
npx @modelcontextprotocol/inspector -e OPENAI_API_KEY=xxx python server.py
```

### SSE/HTTP Servers (Network)

For servers running as HTTP services:

1. Start your server first:
   ```bash
   python server.py  # Server running on http://localhost:8080
   ```

2. Launch Inspector and connect:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector Interface Overview

When Inspector launches, you'll see a web interface (typically at `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Testing Tools

### Listing Available Tools

1. Click the **Tools** tab
2. Inspector automatically calls `tools/list`
3. You'll see all registered tools with:
   - Tool name
   - Description
   - Input schema (parameters)

### Invoking a Tool

1. Select a tool from the list
2. Fill in the required parameters in the form
3. Click **Run Tool**
4. View the response in the results panel

**Example: Testing a calculator tool**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Debugging Tool Errors

When a tool fails, Inspector shows:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Common error codes:
| Code | Meaning |
|------|---------|
| -32700 | Parse error (invalid JSON) |
| -32600 | Invalid request |
| -32601 | Method not found |
| -32602 | Invalid params |
| -32603 | Internal error |

---

## Testing Resources

### Listing Resources

1. Click the **Resources** tab
2. Inspector calls `resources/list`
3. You'll see:
   - Resource URIs
   - Names and descriptions
   - MIME types

### Reading a Resource

1. Select a resource
2. Click **Read Resource**
3. View the content returned

**Example output:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Testing Prompts

### Listing Prompts

1. Click the **Prompts** tab
2. Inspector calls `prompts/list`
3. View available prompt templates

### Getting a Prompt

1. Select a prompt
2. Fill in any required arguments
3. Click **Get Prompt**
4. See the rendered prompt messages

---

## Message Log Analysis

The message log shows all MCP protocol messages. The transcript below is from a
legacy `2025-11-25` server and includes the removed `initialize` handshake. A
`2026-07-28` server uses self-contained request metadata and `server/discover`
instead.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### What to Look For

- **Request/Response pairs**: Each `→` should have a matching `←`
- **Error messages**: Look for `"error"` in responses
- **Timing**: Large gaps might indicate performance issues
- **Protocol version**: Ensure server and client agree on version

---

## VS Code Integration

You can run Inspector directly from VS Code:

### Using launch.json

Add to `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274/?MCP_INSPECTOR_API_TOKEN=local-dev-token",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Using Tasks

Add to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "options": {
        "env": {
          "MCP_INSPECTOR_API_TOKEN": "local-dev-token",
          "MCP_AUTO_OPEN_ENABLED": "false"
        }
      },
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "is up and running"
        }
      }
    }
  ]
}
```

The task sets a fixed `MCP_INSPECTOR_API_TOKEN` so the browser launch configuration can open the Inspector UI (port 6274 by default) with the matching token, and turns off the Inspector's own browser window. `endsPattern` matches the "MCP Inspector Web is up and running" line the Inspector prints when it's ready. Use a fixed token only on your local machine.

---

## Common Debugging Scenarios

### Scenario 1: Server Won't Connect

**Symptoms:** Inspector shows "Disconnected" or hangs on "Connecting..."

**Checklist:**
1. ✅ Is the server command correct?
2. ✅ Are all dependencies installed?
3. ✅ Is the server path absolute or relative to current directory?
4. ✅ Are required environment variables set?

**Debug steps:**
```bash
# Test server manually first
python -c "import your_server_module; print('OK')"

# Check for import errors
python -m your_server_module 2>&1 | head -20

# Verify MCP SDK is installed
pip show mcp
```

### Scenario 2: Tools Not Appearing

**Symptoms:** Tools tab shows empty list

**Possible causes:**
1. Tools not registered during server initialization
2. Server crashed after startup
3. `tools/list` handler returning empty array

**Debug steps:**
1. Check message log for `tools/list` response
2. Add logging to your tool registration code
3. Verify `@mcp.tool()` decorators are present (Python)

### Scenario 3: Tool Returns Error

**Symptoms:** Tool call returns error response

**Debug approach:**
1. Read the error message carefully
2. Check parameter types match schema
3. Add try/catch with detailed error messages
4. Check server logs for stack traces

**Example improved error handling:**

```python
from mcp.server.mcpserver.exceptions import ToolError

@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tool logic here
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        # ToolError is returned to the client as a tool result with is_error=True,
        # so the LLM can see the message and react to it
        raise ToolError(f"Invalid parameter: {e}")
    except Exception as e:
        raise ToolError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Resource Content Empty

**Symptoms:** Resource returns but content is empty or null

**Checklist:**
1. ✅ File path or URI is correct
2. ✅ Server has permission to read the resource
3. ✅ Resource content is being returned correctly

---

## Advanced Inspector Features

### Custom Headers (HTTP and SSE)

```bash
# Web UI, preconfigured for an SSE server
npx @modelcontextprotocol/inspector \
  --transport sse \
  --server-url http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"

# CLI mode against a Streamable HTTP server
npx @modelcontextprotocol/inspector --cli http://localhost:8080/mcp \
  --transport http \
  --header "Authorization: Bearer your-token" \
  --method tools/list
```

### Stack Traces for Inspector Errors

```bash
MCP_DEBUG=1 npx @modelcontextprotocol/inspector python server.py
```

`MCP_DEBUG` (or `DEBUG`) makes the Inspector print full stack traces when it fails. To see what your server is doing, look at its stderr output, which the Inspector shows in the web UI, and the messages in the history panel.

### Recording Sessions

Inspector can export message logs for later analysis:
1. Click **Export Log** in the message panel
2. Save the JSON file
3. Share with team members for debugging

---

## Best Practices

1. **Test early and often** - Use Inspector during development, not just when things break
2. **Start simple** - Test basic connectivity before complex tool calls
3. **Check the schema** - Many errors come from parameter type mismatches
4. **Read error messages** - MCP errors are usually descriptive
5. **Keep Inspector open** - It helps catch issues as you develop

---

## What's Next

You've completed Module 3: Getting Started! Continue your learning:

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## Additional Resources

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

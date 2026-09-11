# Debugging wit MCP Inspector

> [!NOTE]
> Command wey dey use `--sse` an URLs wey end for `/sse` dey test di old HTTP+SSE
> transport. For new MCP `2026-07-28` server, make you use Inspector version wey
> support Streamable HTTP an choose dat transport instead.

Di **MCP Inspector** na important debugging tool wey make you fit test an troubleshoot yo MCP servers without to get full AI host application. Think am like "Postman for MCP" - e dey provide visual interface to send requests, see responses, an understand how yo server dey behave.

## Why Use MCP Inspector?

When you dey build MCP servers, you go often meet dis kain wahala dem:

- **"My server even dey run?"** - Inspector go show connection status
- **"My tools dem register correct?"** - Inspector go list all tools wey dey
- **"Wetin be di response format?"** - Inspector go show full JSON responses
- **"Why dis tool no dey work?"** - Inspector go show detailed error messages

## Prerequisites

- Node.js 18+ don install
- npm (e dey come wit Node.js)
- One MCP server wey you fit test (see [Module 3.1 - First Server](../01-first-server/README.md))

## Installation

### Option 1: Run wit npx (Beta Quick Testing)

```bash
npx @modelcontextprotocol/inspector
```

### Option 2: Install Globally

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Option 3: Add to Yo Project

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

## Connecting to Yo Server

### stdio Servers (Local Process)

For servers wey dey communicate via standard input/output:

```bash
# Python server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js server
npx @modelcontextprotocol/inspector node ./build/index.js

# Wit environment variables dem
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP Servers (Network)

For servers wey dey run as HTTP services:

1. Start yo server first:
   ```bash
   python server.py  # Server dey run for http://localhost:8080
   ```

2. Launch Inspector an connect:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector Interface Overview

When Inspector open, you go see web interface (typically for `http://localhost:5173`):

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

1. Click di **Tools** tab
2. Inspector go automatically call `tools/list`
3. You go see all registered tools wit:
   - Tool name
   - Description
   - Input schema (parameters)

### Invoking a Tool

1. Select one tool from di list
2. Fill di required parameters for di form
3. Click **Run Tool**
4. See di response for di results panel

**Example: Testing one calculator tool**

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

When tool fail, Inspector go show:

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
| -32601 | Method no find |
| -32602 | Invalid params |
| -32603 | Internal error |

---

## Testing Resources

### Listing Resources

1. Click di **Resources** tab
2. Inspector go call `resources/list`
3. You go see:
   - Resource URIs
   - Names and descriptions
   - MIME types

### Reading one Resource

1. Select one resource
2. Click **Read Resource**
3. See di content wey dem return

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

1. Click di **Prompts** tab
2. Inspector go call `prompts/list`
3. View available prompt templates

### Getting one Prompt

1. Select one prompt
2. Fill any argument wey dem require
3. Click **Get Prompt**
4. See di rendered prompt messages

---

## Message Log Analysis

Di message log dey show all MCP protocol messages. Di transcript below na from one
legacy `2025-11-25` server an e include di removed `initialize` handshake. One
`2026-07-28` server dey use self-contained request metadata an `server/discover`
instead.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Wetin to Look Out For

- **Request/Response pairs**: Each `→` suppose get matching `←`
- **Error messages**: Look out for `"error"` inside responses
- **Timing**: Big gaps fit mean say performance get problem
- **Protocol version**: Make sure server an client dem agree on version

---

## VS Code Integration

You fit run Inspector direct from VS Code:

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
      "url": "http://localhost:5173",
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
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Common Debugging Scenarios

### Scenario 1: Server No Go Connect

**Symptoms:** Inspector dey show "Disconnected" or e hang for "Connecting..."

**Checklist:**
1. ✅ Server command correct?
2. ✅ All dependencies don install?
3. ✅ Server path na absolute or relative to current directory?
4. ✅ All required environment variables set?

**Debug steps:**
```bash
# Test di server manuli fɔs
python -c "import your_server_module; print('OK')"

# Check fɔ import erɔs
python -m your_server_module 2>&1 | head -20

# Make sure say MCP SDK dey installed
pip show mcp
```

### Scenario 2: Tools No Dey Show

**Symptoms:** Tools tab dey empty

**Possible causes:**
1. Tools no register during server initialization
2. Server crash after e start
3. `tools/list` handler dey return empty array

**Debug steps:**
1. Check message log for `tools/list` response
2. Add logging to your tool registration code
3. Check say `@mcp.tool()` decorators dey (Python)

### Scenario 3: Tool Dey Return Error

**Symptoms:** Tool call dey return error response

**Debug approach:**
1. Read error message well well
2. Check parameter types match the schema
3. Add try/catch wit detailed error messages
4. Check server logs for stack traces

**Example better error handling:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tool logic deh here
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenario 4: Resource Content Empty

**Symptoms:** Resource return, but content empty or null

**Checklist:**
1. ✅ File path or URI correct
2. ✅ Server get permission to read resource
3. ✅ Resource content dey return the right way

---

## Advanced Inspector Features

### Custom Headers (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Verbose Logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Recording Sessions

Inspector fit export message logs make you analyze later:
1. Click **Export Log** for the message panel
2. Save di JSON file
3. Share am wit your team mates for debugging

---

## Best Practices

1. **Test early and often** - Use Inspector as you dey develop, no wait till wahala show
2. **Start simple** - Test basic connectivity before you try complex tool calls
3. **Check di schema** - Many errors dey come from wrong parameter types
4. **Read error messages** - MCP errors dey usually explain wetin happen
5. **Keep Inspector open** - E go help you catch wahala quick quick as you dey work

---

## Wetin Next

You don finish Module 3: Getting Started! Continue to dey learn:

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## Additional Resources

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Server wit stdio Transport

> **⚠️ Important Update**: As of MCP Specification 2025-06-18, di standalone SSE (Server-Sent Events) transport don **deprecated** and dem don replace am wit "Streamable HTTP" transport. Di current MCP specification dey define two main transport mechanisms:
> 1. **stdio** - Standard input/output (wey dem recommend for local servers)
> 2. **Streamable HTTP** - For remote servers wey fit use SSE inside
>
> Dis lesson don update to focus on di **stdio transport**, wey be di recommended way for most MCP server implementations.

Di stdio transport dey allow MCP servers to dey communicate wit clients through standard input and output streams. Na di most common and recommended transport mechanism for di current MCP specification, e dey provide simple and efficient way to build MCP servers wey fit easily work wit different client applications.

## Overview

Dis lesson go show how to build and use MCP Servers wit di stdio transport.

## Learning Objectives

By di end of dis lesson, you go fit:

- Build MCP Server wit di stdio transport.
- Debug MCP Server wit di Inspector.
- Use MCP Server wit Visual Studio Code.
- Understand di current MCP transport mechanisms and why stdio dey recommended.

## stdio Transport - How e Work

Di stdio transport na one of di two supported transport types for di current MCP specification (2025-06-18). Dis na how e dey work:

- **Simple Communication**: Di server dey read JSON-RPC messages from standard input (`stdin`) and dey send messages to standard output (`stdout`).
- **Process-based**: Di client dey launch di MCP server as subprocess.
- **Message Format**: Messages na individual JSON-RPC requests, notifications, or responses, wey newline dey separate.
- **Logging**: Di server FIT write UTF-8 strings to standard error (`stderr`) for logging.

### Key Requirements:
- Messages MUST dey separate by newline and MUST NOT get newline inside dem
- Di server MUST NOT write anything to `stdout` wey no be valid MCP message
- Di client MUST NOT write anything to di server `stdin` wey no be valid MCP message

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

For di code wey dey above:

- We dey import di `Server` class and `StdioServerTransport` from di MCP SDK
- We dey create server instance wit basic configuration and capabilities

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

For di code wey dey above:

- We dey create server instance wit di MCP SDK
- We dey define tools wit decorators
- We dey use di stdio_server context manager to handle di transport

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Di main difference from SSE na say stdio servers:

- No need web server setup or HTTP endpoints
- Di client dey launch server as subprocess
- Communication dey happen through stdin/stdout streams
- E dey simple to implement and debug

## Exercise: How to Create stdio Server

To create di server, we need to remember two things:

- We need web server to expose endpoints for connection and messages.

## Lab: How to Create Simple MCP stdio Server

For dis lab, we go create simple MCP server wit di recommended stdio transport. Di server go expose tools wey clients fit call wit di standard Model Context Protocol.

### Prerequisites

- Python 3.8 or later
- MCP Python SDK: `pip install mcp`
- Basic understanding of async programming

Make we start to create our first MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Di Key Difference from di Deprecated SSE Approach

**Stdio Transport (Current Standard):**
- Simple subprocess model - client dey launch server as child process
- Communication dey happen via stdin/stdout wit JSON-RPC messages
- No need HTTP server setup
- Better performance and security
- E dey easy to debug and develop

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- E need HTTP server wit SSE endpoints
- E dey more complex to setup wit web server infrastructure
- E get extra security wahala for HTTP endpoints
- Dem don replace am wit Streamable HTTP for web-based scenarios

### How to Create Server wit stdio Transport

To create stdio server, we need to:

1. **Import di required libraries** - We need MCP server components and stdio transport
2. **Create server instance** - Define di server wit di capabilities
3. **Define tools** - Add di functionality wey we wan expose
4. **Set up di transport** - Configure stdio communication
5. **Run di server** - Start di server and handle messages

Make we build am step by step:

### Step 1: Create Basic stdio Server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Step 2: Add More Tools

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Step 3: Run di Server

Save di code as `server.py` and run am for command line:

```bash
python server.py
```

Di server go start and e go dey wait for input from stdin. E dey communicate wit JSON-RPC messages over di stdio transport.

### Step 4: Test wit di Inspector

You fit test di server wit MCP Inspector:

1. Install di Inspector: `npx @modelcontextprotocol/inspector`
2. Run di Inspector and point am to di server
3. Test di tools wey you don create

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugging Your stdio Server

### How to Use MCP Inspector

Di MCP Inspector na better tool for debugging and testing MCP servers. Dis na how to use am wit your stdio server:

1. **Install di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test di server**: Di Inspector dey provide web interface wey you fit use to:
   - See di server capabilities
   - Test tools wit different parameters
   - Monitor JSON-RPC messages
   - Debug connection wahala

### How to Use VS Code

You fit debug MCP server directly for VS Code:

1. Create launch configuration for `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Put breakpoints for di server code
3. Run di debugger and test wit di Inspector

### Common Debugging Tips

- Use `stderr` for logging - no write anything to `stdout` as e dey reserved for MCP messages
- Make sure all JSON-RPC messages dey separate by newline
- Test wit simple tools first before you add complex functionality
- Use di Inspector to confirm message formats

## How to Use Your stdio Server for VS Code

After you don build MCP stdio server, you fit connect am wit VS Code to use am wit Claude or other MCP-compatible clients.

### Configuration

1. **Create MCP configuration file** for `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Restart Claude**: Close and open Claude again to load di new server configuration.

3. **Test di connection**: Start conversation wit Claude and try use di server tools:
   - "Fit you greet me wit di greeting tool?"
   - "Calculate di sum of 15 and 27"
   - "Wetin be di server info?"

### TypeScript stdio Server Example

Dis na complete TypeScript example for reference:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio Server Example

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Summary

For dis updated lesson, you don learn how to:

- Build MCP servers wit di current **stdio transport** (recommended way)
- Understand why SSE transport don deprecated for stdio and Streamable HTTP
- Create tools wey MCP clients fit call
- Debug di server wit MCP Inspector
- Connect di stdio server wit VS Code and Claude

Di stdio transport dey provide simple, secure, and better performance way to build MCP servers compared to di deprecated SSE approach. Na di recommended transport for most MCP server implementations as of di 2025-06-18 specification.

### .NET

1. Make we create some tools first, for dis we go create file *Tools.cs* wit di following content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: Test Your stdio Server

Now wey you don build stdio server, make we test am to make sure e dey work well.

### Prerequisites

1. Make sure you don install MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code suppose dey saved (e.g., as `server.py`)

### Test wit di Inspector

1. **Start di Inspector wit your server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open di web interface**: Di Inspector go open browser window wey go show di server capabilities.

3. **Test di tools**: 
   - Try di `get_greeting` tool wit different names
   - Test di `calculate_sum` tool wit different numbers
   - Call di `get_server_info` tool to see server metadata

4. **Monitor di communication**: Di Inspector go show di JSON-RPC messages wey dey pass between client and server.

### Wetin You Suppose See

If di server start well, you suppose see:
- Server capabilities for di Inspector
- Tools wey dey available for testing
- JSON-RPC messages wey dey pass well
- Tool responses wey dey show for di interface

### Common Issues and Solutions

**Server no start:**
- Check say all dependencies don install: `pip install mcp`
- Confirm Python syntax and indentation
- Look for error messages for console

**Tools no dey show:**
- Make sure `@server.tool()` decorators dey there
- Confirm say tool functions dey defined before `main()`
- Check say server dey configured well

**Connection wahala:**
- Make sure server dey use stdio transport well
- Confirm say no other processes dey disturb
- Check di Inspector command syntax

## Assignment

Try build your server wit more capabilities. Check [dis page](https://api.chucknorris.io/) to, for example, add tool wey dey call API. You go decide how di server go be. Enjoy am :)

## Solution

[Solution](./solution/README.md) Dis na possible solution wit working code.

## Key Takeaways

Di key takeaways from dis chapter na di following:

- Di stdio transport na di recommended way for local MCP servers.
- Stdio transport dey allow smooth communication between MCP servers and clients wit standard input and output streams.
- You fit use both Inspector and Visual Studio Code to use stdio servers directly, wey go make debugging and integration easy.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wetin Next

## Next Steps

Now wey you don learn how to build MCP servers wit di stdio transport, you fit check more advanced topics:

- **Next**: [HTTP Streaming wit MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about di other supported transport mechanism for remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Add security for your MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Deploy your servers for production use

## Additional Resources

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Official specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK references for all languages
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from di community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
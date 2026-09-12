# MCP Server wit stdio Transport

> **⚠️ Important Update**: As MCP Specification 2025-06-18 don come, di standalone SSE (Server-Sent Events) transport don **deprecated** and dem don change am to "Streamable HTTP" transport. Di current MCP specification get two main transport mechanism:
> 1. **stdio** - Standard input/output (wey dem recommend for local servers)
> 2. **Streamable HTTP** - For remote servers wey fit use SSE insaid
>
> Dis lesson don update to focus on di **stdio transport**, wey be di recommended way for most MCP server builds.

Di stdio transport dey allow MCP servers to dey talk to clients through standard input and output streams. Na di most common and recommended transport mechanism for di current MCP specification, e dey provide simple and efficient way to build MCP servers wey fit join well with plenty client applications.

## Overview

Dis lesson go teach how to build and use MCP Servers wit di stdio transport.

## Learning Objectives

By di time you finish dis lesson, you go fit:

- Build MCP Server wit di stdio transport.
- Debug MCP Server wit Inspector.
- Use MCP Server wit Visual Studio Code.
- Understand di current MCP transport and why dem recommend stdio.


## stdio Transport - How e Dey Work

Di stdio transport na one of di two standard transports inside MCP Specification
`2026-07-28`. Na so e dey work:

- **Simple Communication**: Di server dey read JSON-RPC messages from standard input (`stdin`) and e dey send messages go standard output (`stdout`).
- **Process-based**: Di client dey launch di MCP server as subprocess.
- **Message Format**: Messages na individual JSON-RPC requests, notifications, or responses, wey dem separate by newlines.
- **Logging**: Di server fit write UTF-8 strings go standard error (`stderr`) for logging purpose.

### Key Requirements:
- Messages MUST be separated by newlines and MUST NOT carry inside newlines
- Di server MUST NOT write anything for `stdout` wey no be valid MCP message
- Di client MUST NOT write anything go di server `stdin` wey no be valid MCP message

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

For di code wey come before:

- We dey import di `Server` class and `StdioServerTransport` from di MCP SDK
- We create server instance with simple configuration and capabilities
- We create `StdioServerTransport` instance and connect di server to am, to allow communication through stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Make server instance
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

For di code wey come before:

- Create server instance using MCP SDK
- Define tools with decorators
- Use stdio_server context manager to handle di transport

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Di main difference from SSE na say stdio servers:

- No need any web server or HTTP endpoints
- Dem dey launch as subprocess by di client
- Dem dey communicate through stdin/stdout streams
- Dem get simpler implementation and easier to debug

## Exercise: How to create stdio Server

To create our server, two things we need to remember:

- We need to use web server to expose endpoints for connection and messages.
## Lab: Creating simple MCP stdio server

For dis lab, we go create simple MCP server using di advised stdio transport. Dis server go expose tools wey clients fit call using di Model Context Protocol.

### Prerequisites

- Python 3.8 or recent pass
- MCP Python SDK: `pip install mcp`
- Basic sabi async programming

Make we start to create our first MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Set wetin go dey record log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Make the server
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
    # Use stdio way to carry message
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Key difference from di deprecated SSE approach

**Stdio Transport (Current Standard):**
- Simple subprocess model - client fit launch server as child process
- Communication through stdin/stdout wit JSON-RPC messages
- No need setup HTTP server
- Better performance and safety
- Easy to debug and develop

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- Dem need HTTP server wit SSE endpoints
- Complex setup with web server infrastructure
- Additional safety concerns for HTTP endpoints
- E don change to Streamable HTTP for web-based scenarios

### How to create server wit stdio transport

To create our stdio server, we need to:

1. **Import di required libraries** - We need MCP server components and stdio transport
2. **Create server instance** - Define server wit capabilities
3. **Define tools** - Add functionality we want to expose
4. **Set up di transport** - Configure stdio communication
5. **Run di server** - Start server and handle messages

Make we build am step by step:

### Step 1: Create basic stdio server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Make the server
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

### Step 2: Add more tools

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

### Step 3: Run di server

Save di code as `server.py` and run am from command line:

```bash
python server.py
```

Di server go start and wait for input from stdin. E dey communicate using JSON-RPC messages over stdio transport.

### Step 4: Test wit Inspector

You fit test your server wit MCP Inspector:

1. Install Inspector: `npx @modelcontextprotocol/inspector`
2. Run Inspector and point am to your server
3. Test di tools wey you build

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug your stdio server

### How to use MCP Inspector

MCP Inspector na good tool for debugging and testing MCP servers. Na how you fit use am for your stdio server:

1. **Install Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test your server**: Inspector get web interface wey you fit:
   - See server capabilities
   - Test tools wit different parameters
   - Monitor JSON-RPC messages
   - Debug connection wahala

### Use VS Code

You fit also debug your MCP server straight for VS Code:

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

2. Set breakpoints for your server code
3. Run debugger and test wit Inspector

### Common debugging tips

- Use `stderr` for logging - no write for `stdout` as na only MCP messages go there
- Make sure all JSON-RPC messages get newline separation
- Test wit simple tools first before adding complex ones
- Use Inspector to check message formats

## How to use your stdio server inside VS Code

After you build your MCP stdio server, you fit join am with VS Code to use wit Claude or other MCP-compatible clients.

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

3. **Test connection**: Start talk with Claude and try your server tools:
   - "Fit greet me wit di greeting tool?"
   - "Mak una calculate 15 plus 27"
   - "Wetin be di server info?"

### TypeScript stdio server example

Here be complete TypeScript example for reference:

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

// Add tools for work
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

### .NET stdio server example

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Summary

For dis updated lesson, you don learn how to:

- Build MCP servers using di current **stdio transport** (wey dem recommend)
- Understand why dem stop to use SSE transport and prefer stdio and Streamable HTTP
- Create tools wey MCP clients fit call
- Debug your server using MCP Inspector
- Join your stdio server with VS Code and Claude

Di stdio transport na simpler, safer, and better way to build MCP servers compared to di old SSE way. Na di recommended transport for most MCP servers since 2025-06-18 specification.


### .NET

1. Make we first create some tools, for dis one we go create file *Tools.cs* wit dis content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: How to test your stdio server

Now wey you don build your stdio server, make we test am well to ensure say e dey work fine.

### Prerequisites

1. Make sure say you don install MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code suppose dey saved (e.g., as `server.py`)

### Testing wit Inspector

1. **Start Inspector wit your server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open web interface**: Inspector go open browser to show your server capabilities.

3. **Test tools**: 
   - Try `get_greeting` tool wit different names
   - Test `calculate_sum` tool wit different numbers
   - Call `get_server_info` tool make you see server details

4. **Monitor communication**: Inspector go show di JSON-RPC messages wey dey waka between client and server.

### Wetin you suppose see

When your server start well, you go see:
- Server capabilities wey Inspector list
- Tools wey client fit take test
- Successful JSON-RPC message exchange
- Tool responses wey go show for interface

### Common issues and how to solve dem

**Server no fit start:**
- Check all dependencies install: `pip install mcp`
- Check Python syntax and indentation
- Look out for any error messages for console

**Tools no dey show:**
- Make sure `@server.tool()` decorators dey there
- Check say tool functions dey defined before `main()`
- Verify say server dey properly set

**Connection wahala:**
- Make sure server dey use stdio transport correct
- Check say no other processes dey interfere
- Verify Inspector command syntax

## Assignment

Try build your server wit more capabilities. See [this page](https://api.chucknorris.io/) for example to add tool wey go call API. Na you suppose decide how your server go be. Make you enjoy :)
## Solution

[Solution](./solution/README.md) Here be one possible solution wit working code.

## Key Takeaways

Di key points from dis chapter na:

- Di stdio transport na di recommended mechanism for local MCP servers.
- Stdio transport dey allow smooth communication between MCP servers and clients through standard input and output streams.
- You fit use both Inspector and Visual Studio Code to consume stdio servers directly, making debugging and integration easy.

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

Now wey you don learn how to build MCP servers wit stdio transport, you fit explore more advanced topics:

- **Next**: [HTTP Streaming wit MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about di other transport mechanism for remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Implement security for your MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Deploy your servers for production

## Additional Resources

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Current specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK reference for all languages
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
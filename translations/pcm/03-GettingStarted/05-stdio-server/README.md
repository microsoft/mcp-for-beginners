# MCP Server wit stdio Transport

> **⚠️ Important Update**: As of MCP Specification 2025-06-18, di standalone SSE (Server-Sent Events) transport don **deprecated** and dem don change am to "Streamable HTTP" transport. Di current MCP specification dey define two main transport mechanisms:
> 1. **stdio** - Standard input/output (wey dem recommend for local servers)
> 2. **Streamable HTTP** - For remote servers wey fit use SSE inside
>
> Dis lesson don update to focus on di **stdio transport**, wey na di recommended way for most MCP server implementations.

Di stdio transport dey allow MCP servers to communicate wit clients thru standard input and output streams. Na di most common and recommended transport mechanism in di current MCP specification, e dey provide one simple and efficient way to build MCP servers wey fit integrate easily wit different client applications.

## Overview

Dis lesson go cover how to build and use MCP Servers wit di stdio transport.

## Learning Objectives

By di end of dis lesson, you go fit:

- Build MCP Server wit di stdio transport.
- Debug MCP Server wit di Inspector.
- Use MCP Server wit Visual Studio Code.
- Understand di current MCP transport mechanisms and why dem recommend stdio.

## stdio Transport - How e Dey Work

Di stdio transport na one of di two supported transport types for di current MCP specification (2025-06-18). Dis na how e dey work:

- **Simple Communication**: Di server dey read JSON-RPC messages from standard input (`stdin`) and send messages to standard output (`stdout`).
- **Process-based**: Di client dey launch di MCP server as subprocess.
- **Message Format**: Messages na separate JSON-RPC requests, notifications, or responses, dem dey separated by newlines.
- **Logging**: Di server fit write UTF-8 strings to standard error (`stderr`) for logging.

### Key Requirements:
- Messages MUST dey separated by newlines and NO embedded newlines inside dem
- Di server MUST NO write anything to `stdout` wey no be valid MCP message
- Di client MUST NO write anything to di server `stdin` wey no be valid MCP message

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

For di code wey dey up:

- We import di `Server` class and `StdioServerTransport` from MCP SDK
- We create server instance wit basic configuration and capabilities
- We create one `StdioServerTransport` instance and connect di server to am, to enable communication thru stdin/stdout

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

For di code wey dey up:

- We create server instance using MCP SDK
- We define tools using decorators
- We use di stdio_server context manager to handle di transport

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

Main difference wey de between SSE and stdio servers be say:

- No need set up web server or HTTP endpoints for stdio
- Dem launch stdio servers as subprocess by di client
- Dem communicate thru stdin/stdout streams
- E simpler to implement and debug

## Exercise: How to Create stdio Server

To create di server, we need to remember two tins:

- We need use web server to expose endpoints for connection and messages.
## Lab: Build simple MCP stdio server

For dis lab, we go build simple MCP server using di recommended stdio transport. Dis server go expose tools wey clients fit call using di standard Model Context Protocol.

### Prerequisites

- Python 3.8 or later
- MCP Python SDK: `pip install mcp`
- Basic knowledge of async programming

Make we start to build our first MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Set up how we go dey log tins
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

## Main difference from di deprecated SSE way

**Stdio Transport (Current Standard):**
- Simple subprocess model - client go launch server as child process
- Communication via stdin/stdout wit JSON-RPC messages
- No need to set up HTTP server
- Better security and performance
- Easier to debug and build

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- Need HTTP server wit SSE endpoints
- More complex setup with web server infrastructure
- Additional security considerations for HTTP endpoints
- Dem don replace am wit Streamable HTTP for web-based cases

### How to build server wit stdio transport

To create our stdio server, we go:

1. **Import di needed libraries** - We need MCP server components and stdio transport
2. **Create server instance** - Define di server wit di capabilities
3. **Define tools** - Add di functions we want make available
4. **Set up di transport** - Configure stdio communication
5. **Run di server** - Start server and handle messages

Make we build am step by step:

### Step 1: Create simple stdio server

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

### Step 4: Test wit di Inspector

You fit test your server using di MCP Inspector:

1. Install di Inspector: `npx @modelcontextprotocol/inspector`
2. Run di Inspector and point am to your server
3. Test di tools wey you build

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug your stdio server

### Using di MCP Inspector

Di MCP Inspector na beta tool for debugging and testing MCP servers. Dis na how to use am wit your stdio server:

1. **Install di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test your server**: Di Inspector get web interface where you fit:
   - View server capabilities
   - Test tools wit different parameters
   - Monitor JSON-RPC messages
   - Debug connection wahala

### Using VS Code

You fit also debug your MCP server directly inside VS Code:

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
3. Run debugger and test wit di Inspector

### Common debugging tips

- Use `stderr` for logging - no write anything for `stdout` as e reserve for MCP messages
- Make sure all JSON-RPC messages dey newline-delimited
- Test wit simple tools first before you add complex functionalities
- Use Inspector to verify message format

## How to use your stdio server in VS Code

Once you don build MCP stdio server, you fit integrate am with VS Code to use am wit Claude or other MCP-compatible clients.

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

2. **Restart Claude**: Close and open Claude again to load new server settings.

3. **Test connection**: Start conversation wit Claude and try use your server's tools:
   - "Fit greet me usin di greeting tool?"
   - "Calculate di sum of 15 and 27"
   - "Wetin be di server info?"

### TypeScript stdio server example

Here na complete TypeScript example for reference:

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

- Build MCP servers using current **stdio transport** (wey dem recommend)
- Understand why dem deprecated SSE transport for stdio and Streamable HTTP
- Create tools wey MCP clients fit call
- Debug your server using MCP Inspector
- Integrate your stdio server wit VS Code and Claude

Di stdio transport na simpler, more secure, and better performance way to build MCP servers compared to di SSE way wey dem don stop to use. E be di recommended transport for most MCP server implementations as per 2025-06-18 specification.


### .NET

1. Make we create some tools first, for dat one, we go create file *Tools.cs* wit dis content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: Test your stdio server

Now wey you don build your stdio server, make we test am to make sure e dey work well.

### Prerequisites

1. Make sure sey you don install MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code suppose dey saved (like `server.py`)

### How to test with Inspector

1. **Start Inspector with your server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open di web interface**: Di Inspector go open browser to show your server capabilities.

3. **Test your tools**: 
   - Try di `get_greeting` tool wit different names
   - Test `calculate_sum` tool wit plenty numbers
   - Call `get_server_info` tool to see server metadata

4. **Monitor di communication**: Inspector go show JSON-RPC messages wey dey pass between client and server.

### Wetin you suppose see

When your server start correct, you go see:
- Server capabilities for inside Inspector
- Tools wey you fit test
- Successful JSON-RPC message exchange
- Tool responses wey show for interface

### Common problems and how to fix

**Server no start:**
- Check sey all dependencies don install: `pip install mcp`
- Verify Python syntax and indentation
- Look for error messages for console

**Tools no dey appear:**
- Make sure `@server.tool()` decorators dey
- Confirm tools functions dey defined before `main()`
- Check sey server get proper config

**Connection problems:**
- Confirm sey server dey use stdio transport correct
- Check sey no other process dey interfere
- Verify Inspector command syntax

## Assignment

Try build your server wit more capabilities. Check [dis page](https://api.chucknorris.io/) to, for example, add tool wey dey call API. You fit decide how your server go be. Enjoy am :)
## Solution

[Solution](./solution/README.md) Here na possible solution wit working code.

## Key Takeaways

Di main points from dis chapter be:

- Di stdio transport na di recommended way to run local MCP servers.
- Stdio transport fit connect MCP servers and clients smooth using standard input/output streams.
- You fit use Inspector and Visual Studio Code to consume stdio servers directly, wey make debugging and integration easier.

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

Now wey you don learn how to build MCP servers wit stdio transport, you fit explore advanced topics:

- **Next**: [HTTP Streaming wit MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about di other transport for remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Implement security for your MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - How to deploy servers for production use

## Additional Resources

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Official specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK references for all programming languages
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make am accurate, abeg sabi say automated translation fit get errors or wahala. Di original dokument for im own language na di correct source. For important tins, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
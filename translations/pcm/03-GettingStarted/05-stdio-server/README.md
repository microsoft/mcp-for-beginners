# MCP Server wit stdio Transport

> **⚠️ Important Update**: As of MCP Specification 2025-06-18, di standalone SSE (Server-Sent Events) transport don **deprecated** and dem don replace am wit "Streamable HTTP" transport. Di current MCP specification get two main transport mechanism dem:
> 1. **stdio** - Standard input/output (wey dem recommend for local servers)
> 2. **Streamable HTTP** - For remote servers wey fit use SSE inside
>
> Dis lesson don update to focus on di **stdio transport**, wey be di recommended way for most MCP server implementation dem.

Di stdio transport dey allow MCP servers to tok wit clients through standard input and output streams. Na di most common and recommended transport mechanism for di current MCP specification, e dey provide simple and efficient way to build MCP servers wey fit easily blend with different client applications.

## Overview

Dis lesson go show how to build and use MCP Servers wit di stdio transport.

## Wetin You Go Learn

By di time you finish dis lesson, you go fit:

- Build MCP Server wit di stdio transport.
- Debug MCP Server wit di Inspector.
- Use MCP Server wit Visual Studio Code.
- Understand di current MCP transport mechanism dem and why dem recommend stdio.

## stdio Transport - How E Dey Work

Di stdio transport na one of two transport types wey dem support for di current MCP specification (2025-06-18). Dis na how e dey work:

- **Simple Communication**: Di server dey read JSON-RPC messages from standard input (`stdin`) and e dey send messages go standard output (`stdout`).
- **Process-based**: Di client dey start di MCP server as subprocess.
- **Message Format**: Messages na individual JSON-RPC requests, notifications, or responses, wey dem separate wit newlines.
- **Logging**: Di server fit write UTF-8 strings go standard error (`stderr`) for logging tinz.

### Key Requirements:
- Messages MUST dey separated by newlines and dem NO suppose get embedded newlines inside
- Di server MUST NO write anything for `stdout` wey no be valid MCP message
- Di client MUST NO write anything go di server `stdin` wey no be valid MCP message

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

For di code way pass:

- We import di `Server` class and `StdioServerTransport` from di MCP SDK
- We create server instance wit basic configuration and capabilities

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

For di code way pass:

- We create server instance using di MCP SDK
- We define tools using decorators
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Di major difference wey dey between SSE and stdio servers be say:

- Dem no need to setup web server or HTTP endpoints
- Client na im dey launch am as subprocess
- Dem dey communicate through stdin/stdout streams
- E simple to implement and debug

## Exercise: Create stdio Server

To create our server, we need to remember two tins:

- We need to use web server to show endpoints for connection and messages.

## Lab: Create simple MCP stdio server

For dis lab, we go create simple MCP server wey dey use di recommended stdio transport. Dis server go show tools wey clients fit call using di standard Model Context Protocol.

### Wetin you suppose get before you start

- Python 3.8 or later
- MCP Python SDK: `pip install mcp`
- Basic knowledge of async programming

Make we start by creating our first MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Set up logging
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

## Key difference from di deprecated SSE way

**Stdio Transport (Current Standard):**
- Simple subprocess model - client dey launch server as child process
- Communication dey happen via stdin/stdout wit JSON-RPC messages
- No need to setup HTTP server
- Better performance and security
- E easy to debug and develop

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- E need HTTP server wey get SSE endpoints
- Setup more complex wit web server infrastructure
- Extra security considerations for HTTP endpoints
- Dem don replace am wit Streamable HTTP for web-based cases

### How to create server wit stdio transport

To create our stdio server, we go:

1. **Import di libraries wey we need** - We need MCP server components and stdio transport
2. **Create server instance** - Define di server wit im capabilities
3. **Define tools** - Add di functionality we want make e expose
4. **Setup di transport** - Configure stdio communication
5. **Run di server** - Start di server and handle messages

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

# Make di server
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

Di server go start and e go wait for input from stdin. E dey communicate using JSON-RPC messages over di stdio transport.

### Step 4: Test wit Inspector

You fit test your server wit MCP Inspector:

1. Install Inspector: `npx @modelcontextprotocol/inspector`
2. Run Inspector and point am to your server
3. Test di tools wey you don create

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## How to debug your stdio server

### Using MCP Inspector

Di MCP Inspector na beta tool to debug and test MCP servers. Na so you fit use am wit your stdio server:

1. **Install di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test your server**: Di Inspector get web interface wey you fit:
   - See server capabilities
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
3. Run debugger and test with Inspector

### Common debugging tips

- Use `stderr` for logging - no ever write anything for `stdout` because na reserved space for MCP messages
- Make sure all JSON-RPC messages dey newline-delimited
- Test wit simple tools first before you add complex functionality
- Use Inspector to check message formats

## How to consume your stdio server inside VS Code

Once you don build your MCP stdio server, you fit join am wit VS Code make e work wit Claude or other MCP-compatible clients.

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

3. **Test di connection**: Start talk wit Claude and try use your server tools:
   - "You fit greet me using di greeting tool?"
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

// Add tool dem
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
- Understand why dem deprecated SSE transport and use stdio and Streamable HTTP instead
- Create tools wey MCP clients fit call
- Debug your server using MCP Inspector
- Join your stdio server with VS Code and Claude

Di stdio transport na simpler, more secure, and better performing way to build MCP servers compared to di deprecated SSE way. Na di recommended transport for most MCP server implementations as of 2025-06-18 specification.

### .NET

1. Make we create some tools first, for dis we go create file *Tools.cs* wit dis tin dem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: Test your stdio server

Now wey you don build your stdio server, make we test am to confirm say e dey work well.

### Wetin you need before you start

1. Make sure say you don install MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code suppose dey saved (like `server.py`)

### Testing wit Inspector

1. **Start Inspector wit your server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open di web interface**: Di Inspector go open browser window wey go show your server capabilities.

3. **Test di tools**: 
   - Try `get_greeting` tool wit different names
   - Test `calculate_sum` tool wit different numbers
   - Call `get_server_info` tool make you see server metadata

4. **Watch di communication**: Di Inspector dey show JSON-RPC messages wey dey happen between client and server.

### Wetin you go see

When your server start well, you go see:
- Server capabilities listed for Inspector
- Tools wey you fit test
- Successful JSON-RPC message exchange
- Tool responses wey show for di interface

### Common wahala and how to solve

**Server no go start:**
- Check if all dependencies dem install: `pip install mcp`
- Check your Python syntax and indentation
- Look for error messages for console

**Tools no dey appear:**
- Make sure `@server.tool()` decorators dey
- Check say tool functions dey defined before `main()`
- Verify say server setup correct

**Connection wahala:**
- Make sure server dey use stdio transport well
- Check if any other process no dey interfere
- Verify Inspector command syntax

## Assignment

Try build your server wit more capabilities. See [dis page](https://api.chucknorris.io/) to, for example, add tool wey dey call API. Na you sabi how your server suppose be. Enjoy :)

## Solution

[Solution](./solution/README.md) Here na one possible solution wey get working code.

## Key Takeaways

Key takeaways from dis chapter na:

- Di stdio transport na di recommended mechanism for local MCP servers.
- Stdio transport dey allow smooth communication between MCP servers and clients with standard input and output streams.
- You fit use both Inspector and Visual Studio Code to consume stdio servers directly, wey dey make debugging and integration easy.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wetin Follow Next

## Next Steps

Now wey you don learn how to build MCP servers wit stdio transport, you fit explore advanced topics:

- **Next**: [HTTP Streaming wit MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about di other supported transport for remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Implement security for your MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - How to deploy your servers for production

## Additional Resources

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Official specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK references for all languages
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from di community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) wey translate am. Even though we dey try make am correct, abeg sabi say automated translation fit get some errors or mistakes. Di original document wey dey the main language na di correct one wey you suppose trust. If na serious information, e better make human professional translate am. We no go responsible if you no understand well or if you misinterpret anything wey come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
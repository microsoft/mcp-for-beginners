# MCP Server wit stdio Transport

> **⚠️ Important Update**: As of MCP Specification 2025-06-18, the standalone SSE (Server-Sent Events) transport don been **deprecated** an don replace am wit "Streamable HTTP" transport. Di current MCP specification dey define two primary transport mechanisms:
> 1. **stdio** - Standard input/output (wey dem recommend for local servers)
> 2. **Streamable HTTP** - For remote servers wey fit use SSE internally
>
> This lesson don update to focus on the **stdio transport**, wey na di recommended approach for most MCP server implementations.

Di stdio transport make MCP servers fit communicate wit clients through standard input an output streams. Na di most common an recommended transport mechanism for di current MCP specification, e dey provide simple an efficient way to build MCP servers wey fit easily integrate wit different client applications.

## Overview

Dis lesson dey cover how to build an consume MCP Servers using di stdio transport.

## Wetin You Go Learn

By di end of dis lesson, you go fit:

- Build an MCP Server using di stdio transport.
- Debug an MCP Server using di Inspector.
- Consume an MCP Server using Visual Studio Code.
- Understand di current MCP transport mechanisms an why stdio dey recommended.


## stdio Transport - How e dey Work

Di stdio transport na one of di two standard transports in MCP Specification
`2026-07-28`. Na so e dey work:

- **Simple Communication**: Di server dey read JSON-RPC messages from standard input (`stdin`) and dey send messages to standard output (`stdout`).
- **Process-based**: Di client go launch di MCP server as a subprocess.
- **Message Format**: Messages na individual JSON-RPC requests, notifications, or responses, dem delimited by newlines.
- **Logging**: Di server MAY write UTF-8 strings to standard error (`stderr`) for logging purposes.

### Key Requirements:
- Messages MUST be delimited by newlines and MUST NOT contain embedded newlines
- The server MUST NOT write anything to `stdout` wey no be a valid MCP message
- The client MUST NOT write anything to the server's `stdin` wey no be a valid MCP message

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

For di code wey pass:

- We import di `Server` class an `StdioServerTransport` from di MCP SDK
- We create a server instance wit basic configuration an capabilities
- We create a `StdioServerTransport` instance an connect di server to am, enabling communication over stdin/stdout

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

For di code wey pass we:

- Create a server instance using di MCP SDK
- Define tools using decorators
- Use di stdio_server context manager to handle di transport

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

Di key difference from SSE na say stdio servers:

- No need web server setup or HTTP endpoints
- Dem dey launch as subprocesses by di client
- Dem dey communicate through stdin/stdout streams
- Dem easier to implement an debug

## Exercise: Creating a stdio Server

To create our server, make we remember two tins:

- We need use a web server to expose endpoints for connection and messages.
## Lab: Creating a simple MCP stdio server

For dis lab, we go create simple MCP server using di recommended stdio transport. Dis server go expose tools wey clients fit call using di standard Model Context Protocol.

### Prerequisites

- Python 3.8 or later
- MCP Python SDK: `pip install mcp`
- Basic understanding of async programming

Make we start by creating our first MCP stdio server:

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

## Key differences from di deprecated SSE approach

**Stdio Transport (Current Standard):**
- Simple subprocess model - client go launch server as child process
- Communication via stdin/stdout using JSON-RPC messages
- No HTTP server setup required
- Better performance and security
- Easier debugging and development

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- Require HTTP server with SSE endpoints
- More complex setup with web server infrastructure
- Additional security considerations for HTTP endpoints
- Now replaced by Streamable HTTP for web-based scenarios

### Creating a server with stdio transport

To create our stdio server, we go need to:

1. **Import the required libraries** - We need di MCP server components and stdio transport
2. **Create a server instance** - Define di server wit im capabilities
3. **Define tools** - Add di functionality we wan expose
4. **Set up the transport** - Configure stdio communication
5. **Run the server** - Start di server an handle messages

Make we build dis step by step:

### Step 1: Create a basic stdio server

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

### Step 3: Running the server

Save di code as `server.py` an run am from di command line:

```bash
python server.py
```

Di server go start an wait for input from stdin. E dey communicate using JSON-RPC messages over di stdio transport.

### Step 4: Testing wit di Inspector

You fit test your server using di MCP Inspector:

1. Install di Inspector: `npx @modelcontextprotocol/inspector`
2. Run di Inspector an point am to your server
3. Test di tools wey you don create

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugging your stdio server

### Using di MCP Inspector

MCP Inspector na valuable tool for debugging an testing MCP servers. Na so you go take use am wit your stdio server:

1. **Install di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run di Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test your server**: Di Inspector dey provide web interface wey you fit:
   - See server capabilities
   - Test tools wit different parameters
   - Monitor JSON-RPC messages
   - Debug connection issues

### Using VS Code

You fit also debug your MCP server directly for VS Code:

1. Create a launch configuration in `.vscode/launch.json`:
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

2. Set breakpoints in your server code
3. Run di debugger an test wit di Inspector

### Common debugging tips

- Use `stderr` for logging - never write to `stdout` as e dey reserved for MCP messages
- Make sure all JSON-RPC messages dey newline-delimited
- Test wit simple tools first before you add complex functionality
- Use di Inspector to verify message formats

## How to use your stdio server in VS Code

Once you don build your MCP stdio server, you fit integrate am wit VS Code to use am wit Claude or other MCP-compatible clients.

### Configuration

1. **Create an MCP configuration file** at `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Restart Claude**: Close an open Claude again to load di new server configuration.

3. **Test the connection**: Start conversation wit Claude an try use your server's tools:
   - "Fit you greet me using di greeting tool?"
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

For dis updated lesson, you learn how to:

- Build MCP servers using di current **stdio transport** (recommended approach)
- Understand why SSE transport don been deprecated in favor of stdio an Streamable HTTP
- Create tools wey MCP clients fit call
- Debug your server using di MCP Inspector
- Integrate your stdio server wit VS Code an Claude

Di stdio transport dey provide simpler, more secure, an more performant way to build MCP servers compared to di deprecated SSE approach. Na di recommended transport for most MCP server implementations as of di 2025-06-18 specification.


### .NET

1. Make we create some tools first; for this we go create file *Tools.cs* wit di following content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: Testing your stdio server

Now wey you don build your stdio server, make we test am to make sure say e dey work correct.

### Prerequisites

1. Make sure say you get di MCP Inspector installed:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code suppose don save (e.g., as `server.py`)

### Testing with di Inspector

1. **Start di Inspector with your server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open di web interface**: Di Inspector go open browser window wey go show your server's capabilities.

3. **Test di tools**: 
   - Try di `get_greeting` tool wit different names
   - Test di `calculate_sum` tool wit various numbers
   - Call di `get_server_info` tool to see server metadata

4. **Monitor di communication**: Di Inspector dey show JSON-RPC messages wey dey exchange between client an server.

### Wetin you suppose see

When your server start correct, you go see:
- Server capabilities listed in di Inspector
- Tools wey available for testing
- Successful JSON-RPC message exchanges
- Tool responses wey go display in di interface

### Common issues and solutions

**Server no go start:**
- Check say all dependencies don install: `pip install mcp`
- Verify Python syntax an indentation
- Check for error messages for di console

**Tools no dey appear:**
- Make sure `@server.tool()` decorators dey present
- Check say tool functions dem define before `main()`
- Verify say di server don properly configure

**Connection issues:**
- Make sure say di server dey use stdio transport correct
- Check say no oda processes dey interfere
- Verify di Inspector command syntax

## Assignment

Try build your server wit more capabilities. See [this page](https://api.chucknorris.io/) to, for example, add a tool wey go call an API. Na you go decide how di server suppose be. Enjoy :)
## Solution

[Solution](./solution/README.md) Here na one possible solution wey get working code.

## Key Takeaways

Di main takeaways from dis chapter na di following:

- Di stdio transport na di recommended mechanism for local MCP servers.
- Stdio transport allow seamless communication between MCP servers an clients using standard input an output streams.
- You fit use both Inspector an Visual Studio Code to consume stdio servers directly, wey dey make debugging an integration straightforward.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wetin Next

## Next Steps

Now wey you don learn how to build MCP servers wit di stdio transport, you fit explore more advanced topics:

- **Next**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about di oda supported transport mechanism for remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Implement security for your MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Deploy your servers for production use

## Additional Resources

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Current specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK references for all languages
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
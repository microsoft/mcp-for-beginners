# MCP Server with stdio Transport

> **⚠️ Important Update**: As of the MCP Specification 2025-06-18, the standalone SSE (Server-Sent Events) transport has been **deprecated** and replaced by the "Streamable HTTP" transport. The current MCP specification defines two primary transport mechanisms:
> 1. **stdio** - Standard input/output (recommended for local servers)
> 2. **Streamable HTTP** - For remote servers that may use SSE internally
>
> This lesson has been updated to focus on the **stdio transport**, which is the recommended approach for most MCP server implementations.

The stdio transport enables MCP servers to communicate with clients through standard input and output streams. It is the most commonly used and recommended transport mechanism in the current MCP specification, offering a simple and efficient way to build MCP servers that can be easily integrated with various client applications.

## Overview

This lesson explains how to build and use MCP Servers with the stdio transport.

## Learning Objectives

By the end of this lesson, you will be able to:

- Build an MCP Server using the stdio transport.
- Debug an MCP Server using the Inspector.
- Use an MCP Server with Visual Studio Code.
- Understand the current MCP transport mechanisms and why stdio is recommended.

## stdio Transport - How it Works

The stdio transport is one of the two supported transport types in the current MCP specification (2025-06-18). Here's how it works:

- **Simple Communication**: The server reads JSON-RPC messages from standard input (`stdin`) and sends messages to standard output (`stdout`).
- **Process-based**: The client starts the MCP server as a subprocess.
- **Message Format**: Messages are individual JSON-RPC requests, notifications, or responses, separated by newlines.
- **Logging**: The server MAY write UTF-8 strings to standard error (`stderr`) for logging purposes.

### Key Requirements:
- Messages MUST be separated by newlines and MUST NOT contain embedded newlines.
- The server MUST NOT write anything to `stdout` that is not a valid MCP message.
- The client MUST NOT write anything to the server's `stdin` that is not a valid MCP message.

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

In the code above:

- The `Server` class and `StdioServerTransport` are imported from the MCP SDK.
- A server instance is created with basic configuration and capabilities.

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

In the code above:

- A server instance is created using the MCP SDK.
- Tools are defined using decorators.
- The `stdio_server` context manager is used to handle the transport.

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

The main differences from SSE are:

- Stdio servers do not require web server setup or HTTP endpoints.
- They are launched as subprocesses by the client.
- Communication happens through stdin/stdout streams.
- They are simpler to implement and debug.

## Exercise: Creating a stdio Server

To create our server, we need to keep two things in mind:

- We need to use a web server to expose endpoints for connection and messages.

## Lab: Creating a Simple MCP stdio Server

In this lab, we'll create a simple MCP server using the recommended stdio transport. This server will expose tools that clients can call using the standard Model Context Protocol.

### Prerequisites

- Python 3.8 or later
- MCP Python SDK: `pip install mcp`
- Basic understanding of asynchronous programming

Let's start by creating our first MCP stdio server:

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

## Key Differences from the Deprecated SSE Approach

**Stdio Transport (Current Standard):**
- Simple subprocess model - the client launches the server as a child process.
- Communication via stdin/stdout using JSON-RPC messages.
- No HTTP server setup required.
- Better performance and security.
- Easier debugging and development.

**SSE Transport (Deprecated as of MCP 2025-06-18):**
- Required an HTTP server with SSE endpoints.
- More complex setup with web server infrastructure.
- Additional security considerations for HTTP endpoints.
- Now replaced by Streamable HTTP for web-based scenarios.

### Creating a Server with stdio Transport

To create our stdio server, we need to:

1. **Import the required libraries** - MCP server components and stdio transport.
2. **Create a server instance** - Define the server with its capabilities.
3. **Define tools** - Add the functionality we want to expose.
4. **Set up the transport** - Configure stdio communication.
5. **Run the server** - Start the server and handle messages.

Let's build this step by step:

### Step 1: Create a Basic stdio Server

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

### Step 3: Running the Server

Save the code as `server.py` and run it from the command line:

```bash
python server.py
```

The server will start and wait for input from stdin. It communicates using JSON-RPC messages over the stdio transport.

### Step 4: Testing with the Inspector

You can test your server using the MCP Inspector:

1. Install the Inspector: `npx @modelcontextprotocol/inspector`
2. Run the Inspector and point it to your server.
3. Test the tools you've created.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debugging Your stdio Server

### Using the MCP Inspector

The MCP Inspector is a valuable tool for debugging and testing MCP servers. Here's how to use it with your stdio server:

1. **Install the Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Run the Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test Your Server**: The Inspector provides a web interface where you can:
   - View server capabilities.
   - Test tools with different parameters.
   - Monitor JSON-RPC messages.
   - Debug connection issues.

### Using VS Code

You can also debug your MCP server directly in VS Code:

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

2. Set breakpoints in your server code.
3. Run the debugger and test with the Inspector.

### Common Debugging Tips

- Use `stderr` for logging - never write to `stdout` as it's reserved for MCP messages.
- Ensure all JSON-RPC messages are newline-delimited.
- Test with simple tools first before adding complex functionality.
- Use the Inspector to verify message formats.

## Consuming Your stdio Server in VS Code

Once you've built your MCP stdio server, you can integrate it with VS Code to use it with Claude or other MCP-compatible clients.

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

2. **Restart Claude**: Close and reopen Claude to load the new server configuration.

3. **Test the Connection**: Start a conversation with Claude and try using your server's tools:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27."
   - "What's the server info?"

### TypeScript stdio Server Example

Here's a complete TypeScript example for reference:

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

In this updated lesson, you learned how to:

- Build MCP servers using the current **stdio transport** (recommended approach).
- Understand why SSE transport was deprecated in favor of stdio and Streamable HTTP.
- Create tools that can be called by MCP clients.
- Debug your server using the MCP Inspector.
- Integrate your stdio server with VS Code and Claude.

The stdio transport provides a simpler, more secure, and more performant way to build MCP servers compared to the deprecated SSE approach. It's the recommended transport for most MCP server implementations as of the 2025-06-18 specification.

### .NET

1. Let's create some tools first. For this, we will create a file *Tools.cs* with the following content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercise: Testing Your stdio Server

Now that you've built your stdio server, let's test it to make sure it works correctly.

### Prerequisites

1. Ensure you have the MCP Inspector installed:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Your server code should be saved (e.g., as `server.py`).

### Testing with the Inspector

1. **Start the Inspector with Your Server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open the Web Interface**: The Inspector will open a browser window showing your server's capabilities.

3. **Test the Tools**: 
   - Try the `get_greeting` tool with different names.
   - Test the `calculate_sum` tool with various numbers.
   - Call the `get_server_info` tool to see server metadata.

4. **Monitor the Communication**: The Inspector shows the JSON-RPC messages being exchanged between client and server.

### What You Should See

When your server starts correctly, you should see:
- Server capabilities listed in the Inspector.
- Tools available for testing.
- Successful JSON-RPC message exchanges.
- Tool responses displayed in the interface.

### Common Issues and Solutions

**Server Won't Start:**
- Check that all dependencies are installed: `pip install mcp`.
- Verify Python syntax and indentation.
- Look for error messages in the console.

**Tools Not Appearing:**
- Ensure `@server.tool()` decorators are present.
- Check that tool functions are defined before `main()`.
- Verify the server is properly configured.

**Connection Issues:**
- Make sure the server is using stdio transport correctly.
- Check that no other processes are interfering.
- Verify the Inspector command syntax.

## Assignment

Try building out your server with more capabilities. See [this page](https://api.chucknorris.io/) to, for example, add a tool that calls an API. You decide what the server should look like. Have fun :)

## Solution

[Solution](./solution/README.md) Here's a possible solution with working code.

## Key Takeaways

The key takeaways from this chapter are:

- The stdio transport is the recommended mechanism for local MCP servers.
- Stdio transport allows seamless communication between MCP servers and clients using standard input and output streams.
- You can use both Inspector and Visual Studio Code to consume stdio servers directly, making debugging and integration straightforward.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## What's Next

## Next Steps

Now that you've learned how to build MCP servers with the stdio transport, you can explore more advanced topics:

- **Next**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Learn about the other supported transport mechanism for remote servers.
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Implement security in your MCP servers.
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Deploy your servers for production use.

## Additional Resources

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Official specification.
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - SDK references for all languages.
- [Community Examples](../../06-CommunityContributions/README.md) - More server examples from the community.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
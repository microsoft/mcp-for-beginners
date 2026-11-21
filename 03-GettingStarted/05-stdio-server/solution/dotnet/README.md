# MCP stdio Server - .NET Solution

> **⚠️ Important**: This solution has been updated to use the **stdio transport** as recommended by MCP Specification 2025-06-18. The original SSE transport has been deprecated.

## Overview

This .NET solution demonstrates how to build an MCP server using the current stdio transport. The stdio transport is simpler, more secure, and provides better performance than the deprecated SSE approach.

## Prerequisites

- .NET 10.0 SDK or later
- Basic understanding of .NET dependency injection

## Setup Instructions

### Step 1: Restore dependencies

```bash
dotnet restore
```

### Step 2: Build the project

```bash
dotnet build
```

## Running the Server

The stdio server runs differently than the old HTTP-based server. Instead of starting a web server, it communicates through stdin/stdout:

```bash
dotnet run
```

**Important**: The server will appear to hang - this is normal! It's waiting for JSON-RPC messages from stdin.

## Testing the Server

### Method 1: Using the MCP Inspector (Recommended)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

This will:
1. Launch your server as a subprocess
2. Open a web interface for testing
3. Allow you to test all server tools interactively

### Method 2: Direct command line testing

You can also test by launching the Inspector directly:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Available Tools

The server provides these tools:

- **add_numbers(a, b)**: Add two numbers together
- **multiply_numbers(a, b)**: Multiply two numbers together
- **get_greeting(name)**: Generate a personalized greeting
- **get_server_info()**: Get information about the server

The C# methods are called `AddNumbers`, `MultiplyNumbers`, and so on; the MCP C# SDK publishes them in snake_case, so use these names when you call the tools.

### Testing with Claude Desktop

To use this server with Claude Desktop, add this configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "/absolute/path/to/server.csproj"]
    }
  }
}
```

Use an absolute path, because Claude Desktop doesn't start the server from this folder.

## Project Structure

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Key Differences from HTTP/SSE

**stdio transport (Current):**
- ✅ Simpler setup - no web server needed
- ✅ Better security - no HTTP endpoints
- ✅ Uses `Host.CreateApplicationBuilder()` instead of `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` instead of `WithHttpTransport()`
- ✅ Console application instead of web application
- ✅ Better performance

**HTTP/SSE transport (Deprecated):**
- ❌ Required ASP.NET Core web server
- ❌ Needed `app.MapMcp()` routing setup
- ❌ More complex configuration and dependencies
- ❌ Additional security considerations
- ❌ Now deprecated in MCP 2025-06-18

## Development Features

- **Dependency Injection**: Full DI support for services and logging
- **Structured Logging**: Proper logging to stderr using `ILogger<T>`
- **Tool Attributes**: Clean tool definition using `[McpServerTool]` attributes
- **Async Support**: All tools support async operations
- **Error Handling**: Graceful error handling and logging

## Development Tips

- Use `ILogger` for logging (never write to stdout directly)
- Build with `dotnet build` before testing
- Test with the Inspector for visual debugging
- All logging goes to stderr: `Program.cs` sets `LogToStandardErrorThreshold = LogLevel.Trace` on the console logger, whose default target is stdout
- The server handles graceful shutdown signals

This solution follows the current MCP specification and demonstrates best practices for stdio transport implementation using .NET.
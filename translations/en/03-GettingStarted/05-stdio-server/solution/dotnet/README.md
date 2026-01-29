# MCP stdio Server - .NET Solution

> **⚠️ Important**: This solution has been updated to use the **stdio transport** as recommended by MCP Specification 2025-06-18. The original SSE transport has been deprecated.

## Overview

This .NET solution showcases how to create an MCP server using the latest stdio transport. The stdio transport is easier to use, more secure, and offers better performance compared to the outdated SSE method.

## Prerequisites

- .NET 9.0 SDK or newer
- Basic knowledge of .NET dependency injection

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

The stdio server operates differently from the previous HTTP-based server. Instead of starting a web server, it communicates via stdin/stdout:

```bash
dotnet run
```

**Important**: The server may seem unresponsive—this is expected! It is waiting for JSON-RPC messages through stdin.

## Testing the Server

### Method 1: Using the MCP Inspector (Recommended)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

This will:
1. Start your server as a subprocess
2. Open a web interface for testing
3. Enable interactive testing of all server tools

### Method 2: Direct command line testing

You can also test by running the Inspector directly:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Available Tools

The server provides the following tools:

- **AddNumbers(a, b)**: Adds two numbers
- **MultiplyNumbers(a, b)**: Multiplies two numbers  
- **GetGreeting(name)**: Creates a personalized greeting
- **GetServerInfo()**: Retrieves server information

### Testing with Claude Desktop

To use this server with Claude Desktop, include this configuration in your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

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
- ✅ Easier setup—no web server required
- ✅ Enhanced security—no HTTP endpoints
- ✅ Uses `Host.CreateApplicationBuilder()` instead of `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` replaces `WithHttpTransport()`
- ✅ Console application instead of web application
- ✅ Improved performance

**HTTP/SSE transport (Deprecated):**
- ❌ Required an ASP.NET Core web server
- ❌ Needed `app.MapMcp()` routing configuration
- ❌ More complex setup and dependencies
- ❌ Additional security concerns
- ❌ Deprecated as of MCP 2025-06-18

## Development Features

- **Dependency Injection**: Comprehensive DI support for services and logging
- **Structured Logging**: Proper logging to stderr using `ILogger<T>`
- **Tool Attributes**: Simplified tool definition with `[McpServerTool]` attributes
- **Async Support**: All tools support asynchronous operations
- **Error Handling**: Robust error handling and logging

## Development Tips

- Use `ILogger` for logging (avoid writing directly to stdout)
- Build the project with `dotnet build` before testing
- Test using the Inspector for visual debugging
- All logs are automatically directed to stderr
- The server gracefully handles shutdown signals

This solution adheres to the latest MCP specification and demonstrates best practices for implementing stdio transport in .NET.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
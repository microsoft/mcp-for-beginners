# MCP stdio Server - .NET Solution

> **⚠️ Important**: Dis solution don update to dey use **stdio transport** as MCP Specification 2025-06-18 recommend. Di original SSE transport don comot.

## Overview

Dis .NET solution dey show how you fit build MCP server wey dey use di current stdio transport. Di stdio transport simple pass, e secure well-well, and e dey perform better pass di old SSE method wey dem don comot.

## Prerequisites

- .NET 9.0 SDK or later
- Basic sabi of .NET dependency injection

## Setup Instructions

### Step 1: Restore dependencies

```bash
dotnet restore
```

### Step 2: Build di project

```bash
dotnet build
```

## Running di Server

Di stdio server dey run different from di old HTTP-based server. Instead of to start web server, e dey communicate through stdin/stdout:

```bash
dotnet run
```

**Important**: Di server go look like say e don hang - no worry! E dey wait for JSON-RPC messages from stdin.

## Testing di Server

### Method 1: Use MCP Inspector (Recommended)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dis one go:
1. Start your server as subprocess
2. Open web interface for testing
3. Allow you test all di server tools interactively

### Method 2: Direct command line testing

You fit test am by launching di Inspector directly:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Available Tools

Di server get dis tools:

- **AddNumbers(a, b)**: Add two numbers together
- **MultiplyNumbers(a, b)**: Multiply two numbers together  
- **GetGreeting(name)**: Create personalized greeting
- **GetServerInfo()**: Show info about di server

### Testing with Claude Desktop

To use dis server with Claude Desktop, add dis configuration to your `claude_desktop_config.json`:

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
- ✅ E easy to setup - no need web server
- ✅ Better security - no HTTP endpoints
- ✅ E dey use `Host.CreateApplicationBuilder()` instead of `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` instead of `WithHttpTransport()`
- ✅ Console application instead of web application
- ✅ Better performance

**HTTP/SSE transport (Deprecated):**
- ❌ E need ASP.NET Core web server
- ❌ E need `app.MapMcp()` routing setup
- ❌ E complex for configuration and dependencies
- ❌ E get extra security wahala
- ❌ MCP 2025-06-18 don comot am

## Development Features

- **Dependency Injection**: Full DI support for services and logging
- **Structured Logging**: Proper logging to stderr using `ILogger<T>`
- **Tool Attributes**: Clean tool definition with `[McpServerTool]` attributes
- **Async Support**: All tools dey support async operations
- **Error Handling**: E dey handle errors well and dey log am

## Development Tips

- Use `ILogger` for logging (no write directly to stdout)
- Build am with `dotnet build` before you test
- Test am with di Inspector for visual debugging
- All logging dey go stderr automatically
- Di server dey handle shutdown signals well

Dis solution dey follow di current MCP specification and e dey show di best way to implement stdio transport with .NET.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong way wey person go take understand di transleshion wey dis dokyument get.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP stdio Server - TypeScript Solution

> **⚠️ Important**: This solution has been updated to use the **stdio transport** as recommended by MCP Specification 2025-06-18. The original SSE transport has been deprecated.

## Overview

This TypeScript solution demonstrates how to build an MCP server using the current stdio transport. The stdio transport is simpler, more secure, and provides better performance than the deprecated SSE approach.

## Prerequisites

- Node.js 18+ or later
- npm or yarn package manager

## Setup Instructions

### Step 1: Install the dependencies

```bash
npm install
```

### Step 2: Build the project

```bash
npm run build
```

## Running the Server

The stdio server runs differently than the old SSE server. Instead of starting a web server, it communicates through stdin/stdout:

```bash
npm start
```

**Important**: The server will appear to hang - this is normal! It's waiting for JSON-RPC messages from stdin.

## Testing the Server

### Method 1: Using the MCP Inspector (Recommended)

```bash
npm run inspector
```

This will:
1. Launch your server as a subprocess
2. Open a web interface for testing
3. Allow you to test all server tools interactively

### Method 2: Direct command line testing

You can also test by launching the Inspector directly:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Available Tools

The server provides these tools:

- **add(a, b)**: Add two numbers together
- **multiply(a, b)**: Multiply two numbers together  
- **get_greeting(name)**: Generate a personalized greeting
- **get_server_info()**: Get information about the server

### Testing with Claude Desktop

To use this server with Claude Desktop, add this configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Project Structure

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Key Differences from SSE

**stdio transport (Current):**
- ✅ Simpler setup - no HTTP server needed
- ✅ Better security - no HTTP endpoints
- ✅ Subprocess-based communication
- ✅ JSON-RPC over stdin/stdout
- ✅ Better performance

**SSE transport (Deprecated):**
- ❌ Required Express server setup
- ❌ Needed complex routing and session management
- ❌ More dependencies (Express, HTTP handling)
- ❌ Additional security considerations
- ❌ Now deprecated in MCP 2025-06-18

## Development Tips

- Use `console.error()` for logging (never `console.log()` as it writes to stdout)
- Build with `npm run build` before testing
- Test with the Inspector for visual debugging
- Ensure all JSON messages are properly formatted
- The server automatically handles graceful shutdown on SIGINT/SIGTERM

This solution follows the current MCP specification and demonstrates best practices for stdio transport implementation using TypeScript.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
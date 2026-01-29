# MCP stdio Server - TypeScript Solution

> **⚠️ Important**: Dis solution don update to dey use **stdio transport** as MCP Specification 2025-06-18 recommend. Di original SSE transport don dey deprecated.

## Overview

Dis TypeScript solution dey show how to build MCP server wey dey use di current stdio transport. Di stdio transport simple pass, e secure well-well, and e dey perform better pass di old SSE method wey dem don stop.

## Prerequisites

- Node.js 18+ or later
- npm or yarn package manager

## Setup Instructions

### Step 1: Install di dependencies

```bash
npm install
```

### Step 2: Build di project

```bash
npm run build
```

## How to Run di Server

Di stdio server dey run different from di old SSE server. Instead of to start web server, e dey communicate through stdin/stdout:

```bash
npm start
```

**Important**: Di server go look like say e don hang - no worry! E dey wait for JSON-RPC messages from stdin.

## How to Test di Server

### Method 1: Use MCP Inspector (Recommended)

```bash
npm run inspector
```

Dis one go:
1. Start your server as subprocess
2. Open web interface for testing
3. Allow you test all di server tools interactively

### Method 2: Test directly for command line

You fit test am by launching di Inspector directly:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Tools wey dey Available

Di server dey provide dis tools:

- **add(a, b)**: Add two numbers together
- **multiply(a, b)**: Multiply two numbers together  
- **get_greeting(name)**: Create personalized greeting
- **get_server_info()**: Get info about di server

### Test am with Claude Desktop

To use dis server with Claude Desktop, add dis configuration for your `claude_desktop_config.json`:

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

## Di Key Difference from SSE

**stdio transport (Current):**
- ✅ Setup dey simple - no need HTTP server
- ✅ Security better - no HTTP endpoints
- ✅ Communication dey subprocess-based
- ✅ JSON-RPC dey use stdin/stdout
- ✅ Performance dey better

**SSE transport (Deprecated):**
- ❌ E need Express server setup
- ❌ E need complex routing and session management
- ❌ E get more dependencies (Express, HTTP handling)
- ❌ E get extra security wahala
- ❌ MCP don stop am since 2025-06-18

## Development Tips

- Use `console.error()` for logging (no use `console.log()` because e dey write to stdout)
- Build am with `npm run build` before you test
- Test am with di Inspector for visual debugging
- Make sure say all JSON messages dey well formatted
- Di server dey handle shutdown well-well automatically if SIGINT/SIGTERM happen

Dis solution dey follow di current MCP specification and e dey show di best way to implement stdio transport with TypeScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for di language wey dem take write am first na di one wey you go take as di correct one. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
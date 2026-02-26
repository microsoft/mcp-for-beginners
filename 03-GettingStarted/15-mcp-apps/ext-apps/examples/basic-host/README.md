# Example: Basic Host

A reference implementation showing how to build an MCP host application that connects to MCP servers and renders tool UIs in a secure sandbox.

This basic host can also be used to test MCP Apps during local development.

## Key Files

- [`index.html`](index.html) / [`src/index.tsx`](src/index.tsx) - React UI host with tool selection, parameter input, and iframe management
- [`sandbox.html`](sandbox.html) / [`src/sandbox.ts`](src/sandbox.ts) - Outer iframe proxy with security validation and bidirectional message relay
- [`src/implementation.ts`](src/implementation.ts) - Core logic: server connection, tool calling, and AppBridge setup

## Getting Started

```bash
npm install
npm run start
# Open http://localhost:8080
```

By default, the host application will try to connect to an MCP server at `http://localhost:3001/mcp`. You can configure this behavior by setting the `SERVERS` environment variable with a JSON array of server URLs:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

This example uses a double-iframe sandbox pattern for secure UI isolation:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Why two iframes?**

- The outer iframe runs on a separate origin (port 8081) preventing direct access to the host
- The inner iframe receives HTML via `srcdoc` and is restricted by sandbox attributes
- Messages flow through the outer iframe which validates and relays them bidirectionally

This architecture ensures that even if tool UI code is malicious, it cannot access the host application's DOM, cookies, or JavaScript context.

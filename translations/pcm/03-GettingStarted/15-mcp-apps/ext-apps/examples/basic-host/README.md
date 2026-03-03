# Example: Basic Host

A reference implementation wey dey show how to build MCP host application wey connect to MCP servers and dey render tool UIs inside secure sandbox.

Dis basic host fit also use to test MCP Apps during local development.

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host wey get tool selection, parameter input, and iframe management
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Outer iframe proxy wey get security validation and bidirectional message relay
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Core logic: server connection, tool calling, and AppBridge setup

## Getting Started

```bash
npm install
npm run start
# Open http://localhost:8080
```

By default, the host application go try connect to MCP server for `http://localhost:3001/mcp`. You fit configure dis behavior by setting the `SERVERS` environment variable with JSON array of server URLs:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Dis example dey use double-iframe sandbox pattern make E secure UI isolation:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Why two iframes?**

- The outer iframe dey run for separate origin (port 8081) wey dey prevent direct access to the host
- The inner iframe dey receive HTML via `srcdoc` and e dey restricted by sandbox attributes
- Messages dey flow through the outer iframe wey go validate and relay dem bidirectionally

Dis architecture dey make sure say even if tool UI code dey wicked, e no fit access the host application's DOM, cookies, or JavaScript context.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make everything correct, abeg sabi say automated translation fit get some mistakes or no too clear. Di original document wey e dey for im correct language na di main tin to trust. If na important information, better make person wey sabi human translation do am. We no go responsible if person missunderstand or misinterpret anything wey come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP stdio Server Solutions

> **⚠️ Important**: Dis solutions don update to use **stdio transport** as MCP Specification 2025-06-18 recommend. Di original SSE (Server-Sent Events) transport don dey deprecated.

Dis na di complete solutions wey you fit use build MCP servers wit di stdio transport for each runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Complete stdio server implementation
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio server wey dey use asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio server wey dey use dependency injection

Each solution dey show:
- How to setup stdio transport
- How to define server tools
- Di correct way to handle JSON-RPC messages
- How to connect MCP clients like Claude

All di solutions dey follow di current MCP specification and dey use di recommended stdio transport for better performance and security.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
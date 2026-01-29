# Complete MCP Client Examples

Dis folder get complete, working example of MCP clients for different programming languages. Each client dey show all di functionality wey dey described for di main README.md tutorial.

## Available Clients

### 1. Java Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) wey dey use HTTP
- **Target Server**: `http://localhost:8080`
- **Features**:
  - Connection setup and ping
  - Tool listing
  - Calculator operations (add, subtract, multiply, divide, help)
  - Error handling and result extraction

**How to run am:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local .NET MCP server wey dey run via dotnet run
- **Features**:
  - Automatic server startup via stdio transport
  - Tool and resource listing
  - Calculator operations
  - JSON result parsing
  - Comprehensive error handling

**How to run am:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local Node.js MCP server
- **Features**:
  - Full MCP protocol support
  - Tool, resource, and prompt operations
  - Calculator operations
  - Resource reading and prompt execution
  - Strong error handling

**How to run am:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Transport**: Stdio (Standard Input/Output)  
- **Target Server**: Local Python MCP server
- **Features**:
  - Async/await pattern for operations
  - Tool and resource discovery
  - Calculator operations testing
  - Resource content reading
  - Class-based organization

**How to run am:**

```bash
python client_example_python.py
```

## Common Features Across All Clients

Each client implementation dey show:

1. **Connection Management**
   - How to connect MCP server
   - How to handle connection errors
   - Proper cleanup and resource management

2. **Server Discovery**
   - How to list available tools
   - How to list available resources (if e dey supported)
   - How to list available prompts (if e dey supported)

3. **Tool Invocation**
   - Basic calculator operations (add, subtract, multiply, divide)
   - Help command for server information
   - Proper argument passing and result handling

4. **Error Handling**
   - Connection errors
   - Tool execution errors
   - Graceful failure and user feedback

5. **Result Processing**
   - How to extract text content from responses
   - How to format output make e dey easy to read
   - How to handle different response formats

## Prerequisites

Before you go run these clients, make sure say you get:

1. **Di MCP server wey dey run** (from `../01-first-server/`)
2. **Di required dependencies wey don install** for di language wey you choose
3. **Correct network connection** (for HTTP-based transports)

## Key Differences Between Implementations

| Language   | Transport | Server Startup | Async Model | Key Libraries       |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | External       | Sync        | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatic      | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatic      | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatic      | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatic      | Async/Await | Rust MCP SDK, Tokio |

## Next Steps

After you don check these client examples:

1. **Change di clients** to add new features or operations
2. **Create your own server** and test am with these clients
3. **Try different transports** (SSE vs. Stdio)
4. **Build more complex application** wey go use MCP functionality

## Troubleshooting

### Common Issues

1. **Connection refused**: Make sure say di MCP server dey run for di correct port/path
2. **Module not found**: Install di required MCP SDK for di language wey you dey use
3. **Permission denied**: Check file permissions for stdio transport
4. **Tool not found**: Confirm say di server get di tools wey you dey expect

### Debug Tips

1. **Enable verbose logging** for your MCP SDK
2. **Check server logs** for error messages
3. **Confirm tool names and signatures** dey match between client and server
4. **Test with MCP Inspector** first to make sure say di server dey work well

## Related Documentation

- [Main Client Tutorial](./README.md)
- [MCP Server Examples](../../../../03-GettingStarted/01-first-server)
- [MCP with LLM Integration](../../../../03-GettingStarted/03-llm-client)
- [Official MCP Documentation](https://modelcontextprotocol.io/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make di transle-shon correct, abeg make you sabi say AI transle-shon fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Complete MCP Client Examples

This directory contains complete, working examples of MCP clients in different programming languages. Each client demonstrates the full functionality described in the main README.md tutorial.

## Available Clients

### 1. Java Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) over HTTP
- **Target Server**: `http://localhost:8080`
- **Features**:
  - Connection establishment and ping
  - Tool listing
  - Calculator operations (add, subtract, multiply, divide, help)
  - Error handling and result extraction

**To run:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local .NET MCP server via dotnet run
- **Features**:
  - Automatic server startup via stdio transport
  - Tool and resource listing
  - Calculator operations
  - JSON result parsing
  - Comprehensive error handling

**To run:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: The TypeScript server from `01-first-server/solution/typescript`
- **Features**:
  - Tool listing and the `add` tool
  - Resource template listing and reading `greeting://World`
  - Prompt listing and the `review-code` prompt
  - Closes the connection so the process exits

**To run:** the client uses the MCP SDK and starts the server with `node build/index.js`, so run it from the first-server TypeScript project:

```bash
cd ../01-first-server/solution/typescript
npm install
cp ../../../02-client/client_example_typescript.ts src/
npm run build
node build/client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Transport**: Stdio (Standard Input/Output)  
- **Target Server**: The Python server from `01-first-server/solution/python`
- **Features**:
  - Async/await pattern for operations
  - Tool discovery and the `add` and `subtract` tools
  - Resource template listing and reading `greeting://World`
  - Class-based organization

**To run:** from this directory, in a virtual environment with the MCP Python SDK installed (see `01-first-server/solution/python/README.md`):

```bash
pip install "mcp[cli]>=2.3.0,<3"
python client_example_python.py
```

## Common Features Across All Clients

Each client implementation demonstrates:

1. **Connection Management**
   - Establishing connection to MCP server
   - Handling connection errors
   - Proper cleanup and resource management

2. **Server Discovery**
   - Listing available tools
   - Listing available resources (where supported)
   - Listing available prompts (where supported)

3. **Tool Invocation**
   - Basic calculator operations (add, subtract, multiply, divide)
   - Help command for server information
   - Proper argument passing and result handling

4. **Error Handling**
   - Connection errors
   - Tool execution errors
   - Graceful failure and user feedback

5. **Result Processing**
   - Extracting text content from responses
   - Formatting output for readability
   - Handling different response formats

## Prerequisites

Before running these clients, ensure you have:

1. **The corresponding MCP server running** (from `../01-first-server/`)
2. **Required dependencies installed** for your chosen language
3. **Proper network connectivity** (for HTTP-based transports)

## Key Differences Between Implementations

| Language   | Transport | Server Startup | Async Model | Key Libraries       |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | External       | Sync        | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatic      | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatic      | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatic      | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatic      | Async/Await | Rust MCP SDK, Tokio |

## Next Steps

After exploring these client examples:

1. **Modify the clients** to add new features or operations
2. **Create your own server** and test it with these clients
3. **Experiment with different transports** (SSE vs. Stdio)
4. **Build a more complex application** that integrates MCP functionality

## Troubleshooting

### Common Issues

1. **Connection refused**: Ensure the MCP server is running on the expected port/path
2. **Module not found**: Install the required MCP SDK for your language
3. **Permission denied**: Check file permissions for stdio transport
4. **Tool not found**: Verify the server implements the expected tools

### Debug Tips

1. **Enable verbose logging** in your MCP SDK
2. **Check server logs** for error messages
3. **Verify tool names and signatures** match between client and server
4. **Test with MCP Inspector** first to validate server functionality

## Related Documentation

- [Main Client Tutorial](./README.md)
- [MCP Server Examples](../01-first-server/)
- [MCP with LLM Integration](../03-llm-client/)
- [Official MCP Documentation](https://modelcontextprotocol.io/)

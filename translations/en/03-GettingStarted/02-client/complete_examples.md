# Complete MCP Client Examples

This directory contains fully functional examples of MCP clients in various programming languages. Each client showcases the complete functionality described in the main README.md tutorial.

## Available Clients

### 1. Java Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) over HTTP
- **Target Server**: `http://localhost:8080`
- **Features**:
  - Establishing a connection and sending a ping
  - Listing tools
  - Performing calculator operations (add, subtract, multiply, divide, help)
  - Handling errors and extracting results

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
  - Automatically starting the server using stdio transport
  - Listing tools and resources
  - Performing calculator operations
  - Parsing JSON results
  - Comprehensive error handling

**To run:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local Node.js MCP server
- **Features**:
  - Full support for the MCP protocol
  - Operations with tools, resources, and prompts
  - Performing calculator operations
  - Reading resources and executing prompts
  - Robust error handling

**To run:**

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
  - Using async/await for operations
  - Discovering tools and resources
  - Testing calculator operations
  - Reading resource content
  - Organized with a class-based structure

**To run:**

```bash
python client_example_python.py
```

## Common Features Across All Clients

Each client implementation demonstrates:

1. **Connection Management**
   - Establishing a connection to the MCP server
   - Handling connection errors
   - Proper cleanup and resource management

2. **Server Discovery**
   - Listing available tools
   - Listing available resources (if supported)
   - Listing available prompts (if supported)

3. **Tool Invocation**
   - Performing basic calculator operations (add, subtract, multiply, divide)
   - Using the help command to get server information
   - Passing arguments correctly and handling results

4. **Error Handling**
   - Managing connection errors
   - Handling tool execution errors
   - Failing gracefully and providing user feedback

5. **Result Processing**
   - Extracting text content from responses
   - Formatting output for better readability
   - Managing different response formats

## Prerequisites

Before running these clients, make sure you have:

1. **The corresponding MCP server running** (from `../01-first-server/`)
2. **Installed the required dependencies** for your chosen programming language
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

1. **Customize the clients** to add new features or operations
2. **Develop your own server** and test it with these clients
3. **Experiment with different transports** (SSE vs. Stdio)
4. **Build a more advanced application** that integrates MCP functionality

## Troubleshooting

### Common Issues

1. **Connection refused**: Ensure the MCP server is running on the expected port/path
2. **Module not found**: Install the required MCP SDK for your programming language
3. **Permission denied**: Check file permissions for stdio transport
4. **Tool not found**: Verify that the server implements the expected tools

### Debug Tips

1. **Enable verbose logging** in your MCP SDK
2. **Check server logs** for error messages
3. **Verify tool names and signatures** match between the client and server
4. **Test with MCP Inspector** first to validate server functionality

## Related Documentation

- [Main Client Tutorial](./README.md)
- [MCP Server Examples](../../../../03-GettingStarted/01-first-server)
- [MCP with LLM Integration](../../../../03-GettingStarted/03-llm-client)
- [Official MCP Documentation](https://modelcontextprotocol.io/)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
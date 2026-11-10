## Testing and Debugging

Before you begin testing your MCP server, it's important to understand the available tools and best practices for debugging. Effective testing ensures your server behaves as expected and helps you quickly identify and resolve issues. The following section outlines recommended approaches for validating your MCP implementation.

## Overview

This lesson covers how to select the right testing approach and the most effective testing tool.

## Learning Objectives

By the end of this lesson, you will be able to:

- Describe various approaches for testing.
- Use different tools to effectively test your code.


## Testing MCP Servers

MCP provides tools to help you test and debug your servers:

- **MCP Inspector**: A command line tool that can be run both as a CLI tool and as a visual tool.
- **Manual testing**: You can use a tool like curl to run web requests, but any tool capable of running HTTP will do.
- **Unit testing**: It's possible to use your preferred testing framework to test the features of both server and client.

### Using MCP Inspector

We've described the usage of this tool in previous lessons but let's talk about it a bit at high level. It's a tool built in Node.js and you can use it by calling the `npx` executable which will download and install the tool itself temporarily and will clean itself up once it's done running your request.

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) helps you:

- **Discover Server Capabilities**: Automatically detect available resources, tools, and prompts
- **Test Tool Execution**: Try different parameters and see responses in real-time
- **View Server Metadata**: Examine server info, schemas, and configurations

A typical run of the tool looks like so:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

The above command starts an MCP and its visual interface and launches a local web interface in your browser. You can expect to see a dashboard displaying your registered MCP servers, their available tools, resources, and prompts. The interface allows you to interactively test tool execution, inspect server metadata, and view real-time responses, making it easier to validate and debug your MCP server implementations.

Here's what it can look like: ![Inspector](../01-first-server/assets/connect.png)

You can also run this tool in CLI mode in which case you add `--cli` attribute. Here's an example of running the tool in "CLI" mode which lists all the tools on the server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

Apart from running the inspector tool to test server capabilities, another similar approach is to run a client capable of using HTTP like for example curl.

An MCP server that uses the Streamable HTTP transport has a single endpoint (often `/mcp`) that accepts JSON-RPC messages in POST requests. There are no separate REST routes per tool. A client must first initialize a session, then it can list and call tools. Here's the exchange with curl, using the Python server from [06-http-streaming](../06-http-streaming/solution/python/) (`python server.py mcp`, listening on `http://localhost:8000/mcp`):

```bash
# 1. Initialize; the response header Mcp-Session-Id identifies your session
curl -i http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"curl","version":"1.0"}}}'

# 2. Copy the Mcp-Session-Id value from the response headers
SESSION_ID="<value of the Mcp-Session-Id header>"

# 3. Tell the server initialization is complete (returns 202 Accepted)
curl http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -H "MCP-Protocol-Version: 2025-11-25" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'

# 4. List the tools
curl http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -H "MCP-Protocol-Version: 2025-11-25" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'

# 5. Call a tool
curl http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -H "MCP-Protocol-Version: 2025-11-25" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"process_files","arguments":{"message":"hello"}}}'
```

The server answers as a Server-Sent Events stream (`event: message` / `data: {...}`). For the tool call you first see the progress notifications (`notifications/message`) and then the result:

```text
event: message
data: {"jsonrpc":"2.0","method":"notifications/message","params":{"level":"info","data":"Processing file_1.txt (1/3)..."}}

...

event: message
data: {"jsonrpc":"2.0","id":3,"result":{"content":[{"text":"Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello","type":"text"}],"isError":false}}
```

Stateless servers, such as the .NET server in 06-http-streaming, don't return an `Mcp-Session-Id`; send the requests without that header. Use the approach that fits you best. CLI tools in general tend to be faster to use and lend themselves to be scripted which can be useful in a CI/CD environment.

### Unit Testing

Create unit tests for your tools and resources to ensure they work as expected. Here's some example testing code.

```python
import pytest

from mcp.client import Client
from mcp.server.mcpserver import MCPServer

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: MCPServer doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

    server = MCPServer("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    # Client(server) connects to the server in memory, no network or subprocess needed
    async with Client(server) as client:
        # Test without cursor parameter (omitted)
        result1 = await client.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client.list_tools(cursor="")
        assert len(result4.tools) == 2
```

The preceding code does the following:

- Leverages pytest framework which lets you create tests as functions and use assert statements.
- Creates an MCP Server with two different tools.
- Uses `assert` statement to check that certain conditions are fulfilled.

Have a look at the [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Given the above file, you can test your own server to ensure capabilities are created as they should.

All major SDKs have similar testing sections so you can adjust to your chosen runtime.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../samples/csharp/)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../samples/python/) 

## Additional Resources

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## What's Next

- Next: [Deployment](../09-deployment/README.md)

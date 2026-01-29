## Testing and Debugging

Before you go start to test your MCP server, e good make you sabi di tools wey dey and di best way to debug am. Beta testing go make sure say your server dey work as e suppose and e go help you quick quick find and fix wahala. Di next section go show di recommended way to check your MCP implementation.

## Overview

Dis lesson go teach you how to choose di correct testing method and di best testing tool.

## Learning Objectives

By di end of dis lesson, you go fit:

- Talk about different ways to test.
- Use different tools to test your code well well.

## Testing MCP Servers

MCP get tools wey go help you test and debug your servers:

- **MCP Inspector**: Na command line tool wey fit run as CLI tool or as visual tool.
- **Manual testing**: You fit use tool like curl to send web requests, but any tool wey fit run HTTP go work.
- **Unit testing**: You fit use your favorite testing framework to test di features of di server and client.

### Using MCP Inspector

We don talk about how to use dis tool for di lessons wey don pass, but make we yarn small about am for high level. Na tool wey dem build with Node.js and you fit use am by calling di `npx` executable wey go download and install di tool for small time and go clean amself after e finish run your request.

Di [MCP Inspector](https://github.com/modelcontextprotocol/inspector) dey help you:

- **Discover Server Capabilities**: E go detect di resources, tools, and prompts wey dey available automatically.
- **Test Tool Execution**: You fit try different parameters and see di response as e dey happen.
- **View Server Metadata**: Check di server info, schemas, and configurations.

Di normal way to run di tool be like dis:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Di command wey dey up go start MCP and e visual interface, then e go open local web interface for your browser. You go see dashboard wey dey show di MCP servers wey you don register, di tools, resources, and prompts wey dey available. Di interface go allow you test di tools interactively, check server metadata, and see di response as e dey happen, e go make am easy to validate and debug your MCP server implementation.

E fit look like dis: ![Inspector](../../../../translated_images/pcm/connect.141db0b2bd05f096.webp)

You fit also run dis tool for CLI mode if you add `--cli` attribute. Example of how to run di tool for "CLI" mode wey go list all di tools for di server be like dis:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

Apart from using di inspector tool to test server capabilities, another way wey resemble am na to use client wey fit use HTTP like curl.

With curl, you fit test MCP servers directly with HTTP requests:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

As you see for di curl example wey dey up, you go use POST request to call tool with payload wey get di tool name and di parameters. Use di method wey work for you pass. CLI tools dey fast to use and e dey easy to script, wey fit help for CI/CD environment.

### Unit Testing

Create unit tests for your tools and resources to make sure say dem dey work as e suppose. Example testing code dey here:

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Di code wey dey up dey do di following:

- E dey use pytest framework wey allow you create tests as functions and use assert statements.
- E dey create MCP Server wey get two different tools.
- E dey use `assert` statement to check say some conditions dey correct.

Check di [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

With di file wey dey up, you fit test your own server to make sure say di capabilities dey work as e suppose.

All di major SDKs get similar testing sections so you fit adjust am to di runtime wey you choose.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## What's Next

- Next: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make professional human transle-shon dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
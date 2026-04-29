## Testing and Debugging

Bifo you begin test your MCP server, e important to sabi di available tools and di best way for debugging. Effective testing dey make sure say your server dey work as e suppose and e go help you find and solve wahala quick quick. Di section wey follow go talk about better way dem for check say your MCP waka correct.

## Overview

Dis lesson go show how to choose better testing way and di best testing tool.

## Learning Objectives

By di end of dis lesson, you go fit:

- Talk about different testing way dem.
- Use different tools test your code well well.


## Testing MCP Servers

MCP get tools wey fit help you test and debug your servers:

- **MCP Inspector**: Na command line tool wey you fit run as CLI tool and also as visual tool.
- **Manual testing**: You fit use tool like curl run web requests, but any tool wey fit run HTTP go do.
- **Unit testing**: You fit use your preferred testing framework test features of both server and client.

### Using MCP Inspector

We don talk how to use dis tool for previous lessons but make we talk small about am for high level. Na tool wey dem build for Node.js and you fit run am by calling di `npx` executable wey go download and install di tool temporary and e go clear itself after e finish run your request.

Di [MCP Inspector](https://github.com/modelcontextprotocol/inspector) dey help you:

- **Discover Server Capabilities**: Automatically find available resources, tools, and prompts
- **Test Tool Execution**: Try different parameters and see responses as dem dey happen
- **View Server Metadata**: Check server info, schemas, and configurations

Typical run of di tool be like this:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Di command wey pass start MCP and hin visual interface and e go launch local web interface for your browser. You go see dashboard wey dey show your registered MCP servers, di tools, resources, and prompts wey dem get. Di interface allow you test tools for real time, check server metadata, and view real-time responses so e go easy to validate and debug your MCP server.

Dis be how e fit look: ![Inspector](../../../../translated_images/pcm/connect.141db0b2bd05f096.webp)

You fit run dis tool for CLI mode too by adding `--cli` like dis. Here na example of running di tool for "CLI" mode wey go list all tools for di server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

Besides running inspector tool to test server capability, another way be to run client wey fit use HTTP like curl for example.

With curl, you fit test MCP servers directly using HTTP requests:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Run wan tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

From di curl example above, you dey send POST request to run tool with payload wey get di tool name and hin parameters. Use di way wey suit you best. CLI tools normally quick to use and dem fit be scripted which fit help well for CI/CD environment.

### Unit Testing

Make unit tests for your tools and resources to make sure dem dey work as dem suppose. Here na example testing code.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark di whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create some test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (dem no put am)
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

Di code wey pass do dis:

- Use pytest framework wey allow you create tests as functions and use assert statements.
- Create MCP Server with two different tools.
- Use `assert` statement check say certain condition dem meet.

See di [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

With di file wey pass, you fit test your own server to make sure capabilities dem dey created as e suppose be.

All major SDKs get similar testing sections so you fit adjust am to your runtime.

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
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you sabi say automated translation fit get mistake or no correct. Di original dokument for im own language na di oga for correct info. If na serious info, e good make profesonal human translate am. We no go fit carry any blame if person misunderstand or miss-interpret tins wey come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
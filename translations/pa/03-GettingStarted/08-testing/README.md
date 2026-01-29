## ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ

ਆਪਣਾ MCP ਸਰਵਰ ਟੈਸਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਉਪਲਬਧ ਟੂਲਾਂ ਅਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕਿਆਂ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਤੁਹਾਡਾ ਸਰਵਰ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪਛਾਣਨ ਅਤੇ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਭਾਗ ਤੁਹਾਡੇ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕੇ ਦਰਸਾਉਂਦਾ ਹੈ।

## ਓਵਰਵਿਊ

ਇਸ ਪਾਠ ਵਿੱਚ ਸਹੀ ਟੈਸਟਿੰਗ ਤਰੀਕੇ ਦੀ ਚੋਣ ਅਤੇ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਟੂਲ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੱਤੀ ਗਈ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਟੈਸਟਿੰਗ ਲਈ ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਦਾ ਵਰਣਨ ਕਰਨ ਲਈ।
- ਆਪਣੇ ਕੋਡ ਨੂੰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਟੈਸਟ ਕਰਨ ਲਈ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ।

## MCP ਸਰਵਰਾਂ ਦੀ ਟੈਸਟਿੰਗ

MCP ਤੁਹਾਡੇ ਸਰਵਰਾਂ ਦੀ ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ ਟੂਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

- **MCP Inspector**: ਇੱਕ ਕਮਾਂਡ ਲਾਈਨ ਟੂਲ ਜੋ CLI ਟੂਲ ਅਤੇ ਵਿਜ਼ੂਅਲ ਟੂਲ ਦੋਹਾਂ ਵਜੋਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- **ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ**: ਤੁਸੀਂ curl ਵਰਗਾ ਟੂਲ ਵਰਤ ਕੇ ਵੈੱਬ ਰਿਕਵੇਸਟ ਚਲਾ ਸਕਦੇ ਹੋ, ਪਰ ਕੋਈ ਵੀ HTTP ਚਲਾਉਣ ਵਾਲਾ ਟੂਲ ਇਸ ਲਈ ਕਾਫ਼ੀ ਹੈ।
- **ਯੂਨਿਟ ਟੈਸਟਿੰਗ**: ਤੁਸੀਂ ਆਪਣੇ ਮਨਪਸੰਦ ਟੈਸਟਿੰਗ ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਦੋਹਾਂ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ।

### MCP Inspector ਦੀ ਵਰਤੋਂ

ਅਸੀਂ ਇਸ ਟੂਲ ਦੀ ਵਰਤੋਂ ਪਿਛਲੇ ਪਾਠਾਂ ਵਿੱਚ ਵੇਖੀ ਹੈ ਪਰ ਆਓ ਇਸ ਬਾਰੇ ਥੋੜ੍ਹਾ ਜਿਹਾ ਉੱਚ ਸਤਰ 'ਤੇ ਗੱਲ ਕਰੀਏ। ਇਹ Node.js ਵਿੱਚ ਬਣਾਇਆ ਗਿਆ ਟੂਲ ਹੈ ਅਤੇ ਤੁਸੀਂ ਇਸਨੂੰ `npx` ਐਗਜ਼ਿਕਿਊਟੇਬਲ ਕਾਲ ਕਰਕੇ ਵਰਤ ਸਕਦੇ ਹੋ, ਜੋ ਟੂਲ ਨੂੰ ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਡਾਊਨਲੋਡ ਅਤੇ ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਰਿਕਵੇਸਟ ਦੇ ਚੱਲਣ ਤੋਂ ਬਾਅਦ ਆਪਣੇ ਆਪ ਸਾਫ਼ ਕਰ ਲੈਂਦਾ ਹੈ।

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ਤੁਹਾਡੀ ਮਦਦ ਕਰਦਾ ਹੈ:

- **ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਦੀ ਖੋਜ**: ਉਪਲਬਧ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰਾਂਪਟਸ ਨੂੰ ਆਪਣੇ ਆਪ ਪਛਾਣੋ
- **ਟੂਲ ਚਲਾਉਣ ਦੀ ਜਾਂਚ**: ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਜਵਾਬ ਵੇਖੋ
- **ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਵੇਖੋ**: ਸਰਵਰ ਜਾਣਕਾਰੀ, ਸਕੀਮਾਂ ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

ਇਸ ਟੂਲ ਦੀ ਆਮ ਚਾਲ ਇਸ ਤਰ੍ਹਾਂ ਹੁੰਦੀ ਹੈ:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

ਉਪਰ ਦਿੱਤਾ ਕਮਾਂਡ ਇੱਕ MCP ਅਤੇ ਇਸਦਾ ਵਿਜ਼ੂਅਲ ਇੰਟਰਫੇਸ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਇੱਕ ਲੋਕਲ ਵੈੱਬ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹਦਾ ਹੈ। ਤੁਸੀਂ ਆਪਣੇ ਰਜਿਸਟਰਡ MCP ਸਰਵਰਾਂ, ਉਨ੍ਹਾਂ ਦੇ ਉਪਲਬਧ ਟੂਲਾਂ, ਸਰੋਤਾਂ ਅਤੇ ਪ੍ਰਾਂਪਟਸ ਦਾ ਡੈਸ਼ਬੋਰਡ ਵੇਖ ਸਕਦੇ ਹੋ। ਇਹ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਇੰਟਰਐਕਟਿਵ ਤਰੀਕੇ ਨਾਲ ਟੂਲ ਚਲਾਉਣ ਦੀ ਜਾਂਚ ਕਰਨ, ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਦੀ ਜਾਂਚ ਕਰਨ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਜਵਾਬ ਵੇਖਣ ਦੀ ਆਸਾਨੀ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਹਾਡੇ MCP ਸਰਵਰ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਦੀ ਸਹੀ ਜਾਂਚ ਅਤੇ ਡੀਬੱਗਿੰਗ ਹੋ ਸਕਦੀ ਹੈ।

ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖ ਸਕਦਾ ਹੈ: ![Inspector](../../../../translated_images/pa/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

ਤੁਸੀਂ ਇਸ ਟੂਲ ਨੂੰ CLI ਮੋਡ ਵਿੱਚ ਵੀ ਚਲਾ ਸਕਦੇ ਹੋ ਜਿਸ ਲਈ `--cli` ਐਟ੍ਰਿਬਿਊਟ ਜੋੜਨਾ ਪੈਂਦਾ ਹੈ। ਹੇਠਾਂ CLI ਮੋਡ ਵਿੱਚ ਟੂਲ ਚਲਾਉਣ ਦਾ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ ਜੋ ਸਰਵਰ ਉੱਤੇ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ

ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਜਾਂਚ ਲਈ inspector ਟੂਲ ਚਲਾਉਣ ਤੋਂ ਇਲਾਵਾ, ਇੱਕ ਹੋਰ ਸਮਾਨ ਤਰੀਕਾ ਹੈ HTTP ਚਲਾਉਣ ਵਾਲੇ ਕਲਾਇੰਟ ਨੂੰ ਚਲਾਉਣਾ, ਜਿਵੇਂ ਕਿ curl।

curl ਨਾਲ, ਤੁਸੀਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਸਿੱਧਾ HTTP ਰਿਕਵੇਸਟਾਂ ਰਾਹੀਂ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

ਜਿਵੇਂ ਕਿ curl ਦੀ ਉਪਰੋਕਤ ਵਰਤੋਂ ਤੋਂ ਪਤਾ ਲੱਗਦਾ ਹੈ, ਤੁਸੀਂ ਇੱਕ POST ਰਿਕਵੇਸਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਜਿਸ ਵਿੱਚ ਟੂਲ ਦਾ ਨਾਮ ਅਤੇ ਉਸਦੇ ਪੈਰਾਮੀਟਰਾਂ ਵਾਲਾ ਪੇਲੋਡ ਹੁੰਦਾ ਹੈ। ਉਹ ਤਰੀਕਾ ਵਰਤੋ ਜੋ ਤੁਹਾਡੇ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਹੋਵੇ। CLI ਟੂਲ ਆਮ ਤੌਰ 'ਤੇ ਤੇਜ਼ ਹੁੰਦੇ ਹਨ ਅਤੇ ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ ਅਨੁਕੂਲ ਹੁੰਦੇ ਹਨ, ਜੋ CI/CD ਵਾਤਾਵਰਣ ਵਿੱਚ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ।

### ਯੂਨਿਟ ਟੈਸਟਿੰਗ

ਆਪਣੇ ਟੂਲਾਂ ਅਤੇ ਸਰੋਤਾਂ ਲਈ ਯੂਨਿਟ ਟੈਸਟ ਬਣਾਓ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਉਹ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦੇ ਹਨ। ਹੇਠਾਂ ਕੁਝ ਉਦਾਹਰਨ ਟੈਸਟਿੰਗ ਕੋਡ ਦਿੱਤਾ ਗਿਆ ਹੈ।

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

ਉਪਰੋਕਤ ਕੋਡ ਇਹ ਕਰਦਾ ਹੈ:

- pytest ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਫੰਕਸ਼ਨਾਂ ਵਜੋਂ ਟੈਸਟ ਬਣਾਉਣ ਅਤੇ assert ਬਿਆਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- ਦੋ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲ ਇੱਕ MCP ਸਰਵਰ ਬਣਾਉਂਦਾ ਹੈ।
- ਕੁਝ ਸ਼ਰਤਾਂ ਪੂਰੀਆਂ ਹੋਣ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ `assert` ਬਿਆਨ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

[ਪੂਰਾ ਫਾਇਲ ਇੱਥੇ ਵੇਖੋ](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

ਉਪਰੋਕਤ ਫਾਇਲ ਦੇ ਆਧਾਰ 'ਤੇ, ਤੁਸੀਂ ਆਪਣੇ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਸਮਰੱਥਾਵਾਂ ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਬਣਾਈਆਂ ਗਈਆਂ ਹਨ।

ਸਾਰੇ ਮੁੱਖ SDKs ਵਿੱਚ ਸਮਾਨ ਟੈਸਟਿੰਗ ਭਾਗ ਹੁੰਦੇ ਹਨ ਤਾਂ ਤੁਸੀਂ ਆਪਣੇ ਚੁਣੇ ਹੋਏ ਰਨਟਾਈਮ ਅਨੁਸਾਰ ਅਨੁਕੂਲਿਤ ਕਰ ਸਕਦੇ ਹੋ।

## ਨਮੂਨੇ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## ਵਾਧੂ ਸਰੋਤ

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [Deployment](../09-deployment/README.md)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
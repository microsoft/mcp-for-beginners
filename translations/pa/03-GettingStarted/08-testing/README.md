## Testing and Debugging

ਤੁਹਾਡੇ MCP ਸਰਵਰ ਦੀ ਜਾਂਚ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਡੀਬੱਗਿੰਗ ਲਈ ਉਪਲਬਧ ਟੂਲਾਂ ਅਤੇ ਸਰਵੋਤਮ ਅਭਿਆਸਾਂ ਨੂੰ ਸਮਝਣਾ ਜ਼ਰੂਰੀ ਹੈ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਇਹ ਯਕੀਨੀ ਬਣਾਂਦੀ ਹੈ ਕਿ ਤੁਹਾਡਾ ਸਰਵਰ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਮਸਲਿਆਂ ਨੂੰ ਜਲਦੀ ਪਛਾਣਣ ਅਤੇ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਭਾਗ ਤੁਹਾਡੇ MCP ਇੰਪਲੀਮੇਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਲਈ ਸਿਫਾਰਸ਼ੀਅਤ ਤਰੀਕਿਆਂ ਨੂੰ ਦਰਸਾਂਦਾ ਹੈ।

## Overview

ਇਹ ਪਾਠ ਸਹੀ ਟੈਸਟਿੰਗ ਅਭਿਗਮ ਨੂੰ ਚੁਣਨ ਅਤੇ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਟੂਲ ਦੇ ਬਾਰੇ ਕਵਰ ਕਰਦਾ ਹੈ।

## Learning Objectives

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਟੈਸਟਿੰਗ ਲਈ ਵੱਖ-ਵੱਖ ਅਭਿਗਮਾਂ ਦਾ ਵਰਣਨ ਕਰੋ।
- ਆਪਣਾ ਕੋਡ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕੇ ਨਾਲ ਜਾਂਚਣ ਲਈ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।

## Testing MCP Servers

MCP ਤੁਹਾਡੇ ਸਰਵਰਾਂ ਦੀ ਜਾਂਚ ਅਤੇ ਡੀਬੱਗਿੰਗ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਨ ਲਈ ਟੂਲਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

- **MCP Inspector**: ਇੱਕ ਕਮਾਂਡ ਲਾਈਨ ਟੂਲ ਜੋ CLI ਟੂਲ ਵਜੋਂ ਅਤੇ ਵਿਜ਼ੂਅਲ ਟੂਲ ਵਜੋਂ ਦੋਹਾਂ ਤਰ੍ਹਾਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- **ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ**: ਤੁਸੀਂ curl ਵਰਗੇ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੈੱਬ ਰਿਕਵੇਸਟ ਚਲਾ ਸਕਦੇ ਹੋ, ਪਰ ਕੋਈ ਵੀ ਟੂਲ ਜੋ HTTP ਚਲਾ ਸਕਦਾ ਹੈ, ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।
- **ਯੂਨਿਟ ਟੈਸਟਿੰਗ**: ਤੁਸੀਂ ਆਪਣੀ ਪਸੰਦ ਦਾ ਟੈਸਟਿੰਗ ਫਰੇਮਵਰਕ ਵਰਤ ਕੇ ਸਰਵਰ ਅਤੇ ਕਲਾਈਟ ਦੇ ਫੀਚਰਾਂ ਦੀ ਟੈਸਟਿੰਗ ਕਰ ਸਕਦੇ ਹੋ।

### Using MCP Inspector

ਅਸੀਂ ਪਿਛਲੇ ਪਾਠਾਂ ਵਿੱਚ ਇਸ ਟੂਲ ਦੇ ਉਪਯੋਗ ਬਾਰੇ ਵਿਆਖਿਆ ਕੀਤੀ ਹੈ ਪਰ ਆਓ ਇਸ ਬਾਰੇ ਕੁਝ ਉੱਚ-ਸਤਹ ਤੇ ਗੱਲ ਕਰੀਏ। ਇਹ Node.js ਵਿੱਚ ਬਣਿਆ ਟੂਲ ਹੈ ਅਤੇ ਤੁਸੀਂ ਇਹ `npx` ਐਗਜ਼ਕਿਊਟੇਬਲ ਨੂੰ ਕਾਲ ਕਰਕੇ ਵਰਤ ਸਕਦੇ ਹੋ ਜੋ ਟੂਲ ਨੂੰ ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਡਾਊਨਲੋਡ ਅਤੇ ਇੰਸਟਾਲ ਕਰੇਗਾ ਅਤੇ ਤੁਹਾਡੀ ਰਿਕਵੇਸਟ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ ਆਪਣੇ ਆਪ ਸਾਫ਼ ਕਰ ਲੇਗਾ।

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ਤੁਹਾਡੀ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ:

- **ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਖੋਜੋ**: ਉਪਲਬਧ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰੌਂਪਟਸ ਨੂੰ ਆਪਣੇ ਆਪ ਖੋਜੋ
- **ਟੂਲ ਚਲਾਉਣ ਦੀ ਜਾਂਚ ਕਰੋ**: ਵੱਖ-ਵੱਖ ਪੈਰੇਮੀਟਰ ਅਜ਼ਮਾਓ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਜਵਾਬ ਵੇਖੋ
- **ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਵੇਖੋ**: ਸਰਵਰ ਜਾਣਕਾਰੀ, ਸਕੀਮਾਵਾਂ ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

ਇਹ ਟੂਲ ਚਲਾਉਣ ਦਾ ਇੱਕ ਮਿਸਾਲੀ ਤਰੀਕਾ ਇਉਂ ਹੈ:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

ਉਪਰ ਦਿੱਤਾ ਕਮਾਂਡ MCP ਅਤੇ ਇਸ ਦੀ ਵਿਜ਼ੂਅਲ ਇੰਟਰਫੇਸ ਦੀ ਸ਼ੁਰੂਆਤ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਇੱਕ ਲੋਕਲ ਵੈੱਬ ਇੰਟਰਫੇਸ ਖੋਲਦਾ ਹੈ। ਤੁਸੀਂ ਆਪਣੀ ਰਜਿਸਟਰਡ MCP ਸਰਵਰਾਂ, ਉਨ੍ਹਾਂ ਦੇ ਉਪਲਬਧ ਟੂਲਾਂ, ਸਰੋਤਾਂ ਅਤੇ ਪ੍ਰੌਂਪਟਸ ਵਾਲਾ ਡੈਸ਼ਬੋਰਡ ਵੇਖ ਸਕਦੇ ਹੋ। ਇਹ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਟੂਲ ਚਲਾਉਣ ਦੀ ਇੰਟਰੈਕਟਿਵ ਜਾਂਚ ਕਰਨ, ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਦੀ ਜਾਂਚ ਕਰਨ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਜਵਾਬ ਵੇਖਣ ਦੀ ਆਸਾਨੀ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਹਾਡੇ MCP ਸਰਵਰ ਇੰਪਲੀਮੇਂਟੇਸ਼ਨਾਂ ਦੀ ਪੁਸ਼ਟੀ ਅਤੇ ਡੀਬੱਗਿੰਗ ਸਹੁਲਤਮੰਦ ਹੁੰਦੀ ਹੈ।

ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਦਾ ਹੈ: ![Inspector](../../../../translated_images/pa/connect.141db0b2bd05f096.webp)

ਤੁਸੀਂ ਇਸ ਟੂਲ ਨੂੰ CLI ਮੋਡ ਵਿੱਚ ਵੀ ਚਲਾ ਸਕਦੇ ਹੋ ਜਿਸ ਲਈ ਤੁਸੀਂ `--cli` ਐਟ੍ਰਿਬਿਊਟ ਜੋੜਦੇ ਹੋ। ਹੇਠਾਂ ਦਿੱਤਾ ਉਦਾਹਰਨ "CLI" ਮੋਡ ਵਿੱਚ ਟੂਲ ਚਲਾਉਣ ਦਾ ਹੈ ਜੋ ਸਰਵਰ 'ਤੇ ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਲਿਸਟ ਕਰਦਾ ਹੈ:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਦੀ ਜਾਂਚ ਲਈ ਇੰਸਪੈਕਟਰ ਟੂਲ ਚਲਾਉਣ ਦੇ ਇਲਾਵਾ, ਇੱਕ ਹੋਰ ਸਮਾਨ ਤਰੀਕਾ ਹੈ HTTP ਵਰਤ ਸਕਣ ਵਾਲਾ ਕਲਾਇੰਟ ਚਲਾਉਣਾ, ਉਦਾਹਰਨ ਵਜੋਂ curl।

curl ਨਾਲ ਤੁਸੀਂ MCP ਸਰਵਰਾਂ ਦੀ ਸਿੱਧੀ HTTP ਬੇਨਤੀ ਨਾਲ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ:

```bash
# ਉਦਾਹਰਨ: ਟੈਸਟ ਸਰਵਰ ਮੈਟਾ ਡੇਟਾ
curl http://localhost:3000/v1/metadata

# ਉਦਾਹਰਨ: ਇੱਕ ਟੂਲ ਨੂੰ ਚਲਾਓ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

ਉਪਰ ਦਿੱਤਾ curl ਦੇ ਉਪਯੋਗ ਤੋਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਇੱਕ POST ਬੇਨਤੀ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਜਿਸ ਵਿੱਚ ਟੂਲ ਦਾ ਨਾਮ ਅਤੇ ਇਸਦੇ ਪੈਰੇਮੀਟਰ ਹੋਂਦੇ ਹਨ। ਉਹ ਤਰੀਕਾ ਵਰਤੋ ਜੋ ਤੁਹਾਡੇ ਲਈ ਸਭ ਤੋਂ ਢੁਕਵਾਂ ਬੈਠਦਾ ਹੋਵੇ। CLI ਟੂਲ ਆਮ ਤੌਰ 'ਤੇ ਤੇਜ਼ ਹੁੰਦੇ ਹਨ ਅਤੇ ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ ਸਹੂਲਤਮੰਦ ਹੁੰਦੇ ਹਨ, ਜਿਹੜਾ ਕਿ CI/CD ਵਾਤਾਵਰਨ ਵਿੱਚ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ।

### Unit Testing

ਆਪਣੇ ਟੂਲਾਂ ਅਤੇ ਸਰੋਤਾਂ ਲਈ ਯੂਨਿਟ ਟੈਸਟ ਬਣਾਓ ਤਾਂ ਜੋ ਇਹ ਸੁਨਿਸ਼ਚਿਤ ਕੀਤਾ ਜਾ ਸਕੇ ਕਿ ਉਹ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰ ਰਹੇ ਹਨ। ਹੇਠਾਂ ਕੁਝ ਉਦਾਹਰਣ ਟੈਸਟਿੰਗ ਕੋਡ ਦਿੱਤਾ ਗਿਆ ਹੈ।

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# ਪੂਰੇ ਮੋਡੀਊਲ ਨੂੰ ਅਸਿੰਕ ਟੈਸਟਾਂ ਲਈ ਨਿਸ਼ਾਨਿਤ ਕਰੋ
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # ਕੁਝ ਟੈਸਟ ਟੂਲ ਬਣਾਓ
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # ਕੌਰਸਰ ਪੈਰਾਮੀਟਰ ਦੇ ਬਿਨਾਂ ਟੈਸਟ ਕਰੋ (ਛੱਡ ਦਿੱਤਾ ਗਿਆ)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # ਕੌਰਸਰ=None ਨਾਲ ਟੈਸਟ ਕਰੋ
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # ਕੌਰਸਰ ਦੇ ਤੌਰ 'ਤੇ ਸਟਰਿੰਗ ਨਾਲ ਟੈਸਟ ਕਰੋ
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # ਖਾਲੀ ਸਟਰਿੰਗ ਕੌਰਸਰ ਨਾਲ ਟੈਸਟ ਕਰੋ
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

ਉੱਪਰ ਦਿੱਤਾ ਕੋਡ ਹੇਠ ਲਿਖਿਆ ਕੰਮ ਕਰਦਾ ਹੈ:

- pytest ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਫੰਕਸ਼ਨ ਵਜੋਂ ਟੈਸਟ ਬਣਾਉਣ ਅਤੇ assert ਬਿਆਨ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- ਦੋ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲ ਇੱਕ MCP ਸਰਵਰ ਬਣਾਉਂਦਾ ਹੈ।
- ਕੁਝ ਸ਼ਰਤਾਂ ਪੂਰੀਆਂ ਹੋਣ ਦੀ ਜਾਂਚ ਲਈ `assert` ਬਿਆਨ ਵਰਤਦਾ ਹੈ।

[ਪੂਰਾ ਫਾਈਲ ਇੱਥੇ ਵੇਖੋ](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

ਉਪਰ ਦਿੱਤੇ ਫਾਈਲ ਦੇ ਆਧਾਰ 'ਤੇ, ਤੁਸੀਂ ਆਪਣੇ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਸਮਰਥਾਵਾਂ ਜਿਵੇਂ ਬਣਾਈਆਂ ਗਈਆਂ ਹਨ, ਉਹ ਸਹੀ ਹਨ।

ਸਭ ਮੁੱਖ SDKs ਵਿੱਚ ਸਮਾਨ ਟੈਸਟਿੰਗ ਹਿੱਸੇ ਹੁੰਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਤੁਸੀਂ ਆਪਣੇ ਚੁਣੇ ਹੋਏ ਰਨ ਟਾਈਮ ਅਨੁਸਾਰ ਬਦਲ ਸਕਦੇ ਹੋ।

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
**ਇਨਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰੱਥਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਵਿਸ਼ੇਸ਼ਜ્ઞ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਉਤਪੰਨ ਕੋਈ ਸਮਝਦਾਰੀ ਦੇ ਭ੍ਰਮ ਜਾਂ ਗਲਤ ਅਰਥਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
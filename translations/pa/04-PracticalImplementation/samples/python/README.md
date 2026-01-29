# Model Context Protocol (MCP) Python Implementation

ਇਹ ਰਿਪੋਜ਼ਿਟਰੀ Model Context Protocol (MCP) ਦੀ Python ਵਿੱਚ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਹੈ, ਜੋ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ ਇੱਕ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ ਜੋ MCP ਸਟੈਂਡਰਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਗੱਲਬਾਤ ਕਰਦੇ ਹਨ।

## ਓਵਰਵਿਊ

MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਵਿੱਚ ਦੋ ਮੁੱਖ ਹਿੱਸੇ ਹਨ:

1. **MCP Server (`server.py`)** - ਇੱਕ ਸਰਵਰ ਜੋ ਇਹ ਚੀਜ਼ਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:
   - **Tools**: ਫੰਕਸ਼ਨ ਜੋ ਦੂਰੇ ਤੋਂ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ
   - **Resources**: ਡਾਟਾ ਜੋ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ
   - **Prompts**: ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ ਪ੍ਰੰਪਟ ਬਣਾਉਣ ਦੇ ਟੈਂਪਲੇਟ

2. **MCP Client (`client.py`)** - ਇੱਕ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ ਇਸ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ

## ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

ਇਹ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਕੁਝ ਮੁੱਖ MCP ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਂਦੀ ਹੈ:

### Tools
- `completion` - AI ਮਾਡਲਾਂ ਤੋਂ ਟੈਕਸਟ ਪੂਰਾ ਕਰਦਾ ਹੈ (ਨਕਲੀ)
- `add` - ਸਧਾਰਣ ਕੈਲਕੁਲੇਟਰ ਜੋ ਦੋ ਨੰਬਰ ਜੋੜਦਾ ਹੈ

### Resources
- `models://` - ਉਪਲਬਧ AI ਮਾਡਲਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ
- `greeting://{name}` - ਦਿੱਤੇ ਗਏ ਨਾਮ ਲਈ ਵਿਅਕਤੀਗਤ ਸਲਾਮਤੀਆਂ ਦਿੰਦਾ ਹੈ

### Prompts
- `review_code` - ਕੋਡ ਸਮੀਖਿਆ ਲਈ ਪ੍ਰੰਪਟ ਬਣਾਉਂਦਾ ਹੈ

## ਇੰਸਟਾਲੇਸ਼ਨ

ਇਸ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਨੂੰ ਵਰਤਣ ਲਈ, ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ:

```powershell
pip install mcp-server mcp-client
```

## ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਚਲਾਉਣਾ

### ਸਰਵਰ ਸ਼ੁਰੂ ਕਰਨਾ

ਇੱਕ ਟਰਮੀਨਲ ਵਿੰਡੋ ਵਿੱਚ ਸਰਵਰ ਚਲਾਓ:

```powershell
python server.py
```

ਸਰਵਰ ਨੂੰ ਵਿਕਾਸ ਮੋਡ ਵਿੱਚ MCP CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੀ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ:

```powershell
mcp dev server.py
```

ਜਾਂ Claude Desktop ਵਿੱਚ ਇੰਸਟਾਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ (ਜੇ ਉਪਲਬਧ ਹੋਵੇ):

```powershell
mcp install server.py
```

### ਕਲਾਇੰਟ ਚਲਾਉਣਾ

ਦੂਜੇ ਟਰਮੀਨਲ ਵਿੰਡੋ ਵਿੱਚ ਕਲਾਇੰਟ ਚਲਾਓ:

```powershell
python client.py
```

ਇਹ ਸਰਵਰ ਨਾਲ ਜੁੜੇਗਾ ਅਤੇ ਸਾਰੀਆਂ ਉਪਲਬਧ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਏਗਾ।

### ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ

ਕਲਾਇੰਟ (`client.py`) ਸਾਰੀਆਂ MCP ਸਮਰੱਥਾਵਾਂ ਦਿਖਾਉਂਦਾ ਹੈ:

```powershell
python client.py
```

ਇਹ ਸਰਵਰ ਨਾਲ ਜੁੜੇਗਾ ਅਤੇ ਸਾਰੇ ਟੂਲ, ਰਿਸੋਰਸ ਅਤੇ ਪ੍ਰੰਪਟ ਸਮੇਤ ਸਾਰੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰੇਗਾ। ਨਤੀਜਾ ਇਹ ਹੋਵੇਗਾ:

1. ਕੈਲਕੁਲੇਟਰ ਟੂਲ ਦਾ ਨਤੀਜਾ (5 + 7 = 12)
2. "What is the meaning of life?" ਲਈ completion ਟੂਲ ਦਾ ਜਵਾਬ
3. ਉਪਲਬਧ AI ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ
4. "MCP Explorer" ਲਈ ਵਿਅਕਤੀਗਤ ਸਲਾਮ
5. ਕੋਡ ਸਮੀਖਿਆ ਲਈ ਪ੍ਰੰਪਟ ਟੈਂਪਲੇਟ

## ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਵੇਰਵੇ

ਸਰਵਰ `FastMCP` API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਜੋ MCP ਸੇਵਾਵਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਉੱਚ-ਸਤਰ ਦੇ ਅਬਸਟ੍ਰੈਕਸ਼ਨ ਦਿੰਦਾ ਹੈ। ਇੱਥੇ ਇੱਕ ਸਧਾਰਣ ਉਦਾਹਰਨ ਹੈ ਕਿ ਕਿਵੇਂ ਟੂਲ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾਂਦੇ ਹਨ:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

ਕਲਾਇੰਟ MCP ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਅਤੇ ਕਾਲ ਕਰਦਾ ਹੈ:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ

MCP ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਵੇਖੋ: https://modelcontextprotocol.io/

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
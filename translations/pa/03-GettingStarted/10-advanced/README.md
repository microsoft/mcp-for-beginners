# ਐਡਵਾਂਸਡ ਸਰਵਰ ਸੇਵਾ

MCP SDK ਵਿੱਚ ਦੋ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਸਰਵਰ ਖੁੱਲ੍ਹੇ ਹਨ, ਤੁਹਾਡਾ ਆਮ ਸਰਵਰ ਅਤੇ ਲੋ-ਲੇਵਲ ਸਰਵਰ। ਆਮ ਤੌਰ 'ਤੇ, ਤੁਸੀਂ ਆਮ ਸਰਵਰ ਦਾ ਇਸਤੇਮਾਲ ਫੀਚਰ ਜੋੜਨ ਲਈ ਕਰਦੇ ਹੋ। ਪਰ ਕੁਝ ਹਾਲਤਾਂ ਵਿੱਚ, ਤੁਸੀਂ ਲੋ-ਲੇਵਲ ਸਰਵਰ 'ਤੇ ਨਿਰਭਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜਿਵੇਂ ਕਿ:

- ਬਿਹਤਰ ਵਾਸ਼ਤਾ. ਦੋਹਾਂ ਆਮ ਸਰਵਰ ਅਤੇ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਇੱਕ ਸਾਫ ਵਾਸ਼ਤਾ ਬਣਾਉਣਾ ਸੰਭਵ ਹੈ ਪਰ ਕਿਹਾ ਜਾ ਸਕਦਾ ਹੈ ਕਿ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਇਹ ਥੋੜ੍ਹਾ ਜਿਹਾ ਆਸਾਨ ਹੈ।
- ਫੀਚਰ ਦੀ ਉਪਲਬਧਤਾ. ਕੁਝ ਐਡਵਾਂਸਡ ਫੀਚਰ ਸਿਰਫ਼ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਦੇ ਨਾਲ ਹੀ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਤੁਹਾਨੂੰ ਅੱਗੇ ਦੇ ਅਧਿਆਇਆਂ ਵਿੱਚ ਇਹ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਸੈਪਲਿੰਗ ਅਤੇ ਇਲਿਸਿਟੇਸ਼ਨ ਜੋੜਦੇ ਹਾਂ।

## ਆਮ ਸਰਵਰ ਅਤੇ ਲੋ-ਲੇਵਲ ਸਰਵਰ

ਇਹ ਹੈ ਕਿ ਆਮ ਸਰਵਰ ਨਾਲ MCP ਸਰਵਰ ਬਣਾਉਣਾ ਕਿਵੇਂ ਹੁੰਦਾ ਹੈ

**Python**

```python
mcp = FastMCP("Demo")

# ਇਕ ਜੋੜਣ ਵਾਲਾ ਸੰਦ ਸ਼ਾਮਲ ਕਰੋ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

**TypeScript**

```typescript
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// ਇੱਕ ਜੋੜ ਔਜ਼ਾਰ ਸ਼ਾਮਲ ਕਰੋ
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);
```

ਮਹੱਤਵਪੂਰਨ ਗੱਲ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਹਰ ਇੱਕ ਟੂਲ, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ ਜਿਸ ਨੂੰ ਤੁਸੀਂ ਸਰਵਰ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਨੂੰ ਖੁਦ ਵਧਾਉਂਦੇ ਹੋ। ਇਸ ਵਿੱਚ ਕੋਈ ਗਲਤ ਨਹੀਂ।

### ਲੋ-ਲੇਵਲ ਸਰਵਰ ਵਿਧੀ

ਪਰ ਜਦੋਂ ਤੁਸੀਂ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਵਿਧੀ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਸੋਚਣਾ ਪੈਂਦਾ ਹੈ। ਹਰੇਕ ਟੂਲ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਹਰ ਇੱਕ ਫੀਚਰ ਕਿਸਮ (ਟੂਲਜ਼, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ) ਲਈ ਦੋ ਹੈਂਡਲਰ ਬਣਾਉਂਦੇ ਹੋ। ਉਦਾਹਰਨ ਤੌਰ ਤੇ ਟੂਲਜ਼ ਲਈ ਕੇਵਲ ਦੋ ਫੰਕਸ਼ਨ ਹੁੰਦੇ ਹਨ:

- ਸਾਰੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ। ਇੱਕ ਫੰਕਸ਼ਨ ਸਾਰੇ ਟੂਲਜ਼ ਦੀ ਲਿਸਟ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੁੰਦਾ ਹੈ।
- ਸਾਰੇ ਟੂਲਜ਼ ਨੂੰ ਕਾਲ ਕਰਨਾ ਸੰਭਾਲਣਾ। ਇੱਥੇ ਵੀ, ਕੇਵਲ ਇੱਕ ਫੰਕਸ਼ਨ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੁੰਦਾ ਹੈ।

ਇਹ ਘੱਟ ਕੰਮ ਲੱਗਦਾ ਹੈ, ਹੈ ਨਾ? ਇਸ ਲਈ ਟੂਲ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਜਗ੍ਹਾ, ਮੈਨੂੰ ਸਿਰਫ਼ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਜਦੋਂ ਮੈਂ ਸਾਰੇ ਟੂਲਜ਼ ਦੀ ਲਿਸਟ ਬਣਾਉਂਦਾ ਹਾਂ, ਟੂਲ ਸੂਚੀ ਵਿੱਚ ਹੁੰਦਾ ਹੈ ਅਤੇ ਜਦੋਂ ਟੂਲ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਆਉਂਦੀ ਹੈ ਤਾਂ ਇਹ ਕਾਲ ਵੀ ਹੁੰਦੀ ਹੈ।

ਚਲੋ ਹੁਣ ਇਸ ਕੋਡ ਨੂੰ ਵੇਖੀਏ ਕਿ ਹੁਣ ਇਹ ਕਿਵੇਂ ਦਿਖਦਾ ਹੈ:

**Python**

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "number to add"}, 
                    "b": {"type": "number", "description": "number to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ਰਜਿਸਟਰਡ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "number to add"}, 
                "b": {"type": "number", "description": "number to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

ਇਥੇ ਸਾਡੇ ਕੋਲ ਇੱਕ ਫੰਕਸ਼ਨ ਹੈ ਜੋ ਫੀਚਰਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਟੂਲਜ਼ ਲਿਸਟ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਵਿੱਚ ਹੁਣ `name`, `description` ਅਤੇ `inputSchema` ਵਰਗੇ ਖੇਤਰ ਹੁੰਦੇ ਹਨ ਜੋ ਵਾਪਸੀ ਦੇ ਕਿਸਮ ਨਾਲ ਮਿਲਦੇ ਹਨ। ਇਹ ਸਾਡੀਆਂ ਟੂਲਜ਼ ਅਤੇ ਫੀਚਰ ਪਰਿਭਾਸ਼ਾ অন্য ਸਥਾਨ ਤੇ ਰੱਖਣ ਜਾਂਦਾ ਹੈ। ਹੁਣ ਅਸੀਂ ਆਪਣੇ ਸਾਰੇ ਟੂਲਜ਼ ਨੂੰ ਇੱਕ ਟੂਲਜ਼ ਫੋਲਡਰ ਵਿੱਚ ਬਣਾ ਸਕਦੇ ਹਾਂ, ਤੇ ਸਾਰੀਆਂ ਫੀਚਰਾਂ ਲਈ ਵੀ ਇਹੀ, ਤਾਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਏਸ ਤਰ੍ਹਾਂ ਸੁਧਰ ਜਾਵੇਗਾ:

```text
app
--| tools
----| add
----| substract
--| resources
----| products
----| schemas
--| prompts
----| product-description
```

ਇਹ ਬਹੁਤ ਵਧੀਆ ਹੈ, ਸਾਡੀ ਵਾਸ਼ਤਾ ਬਹੁਤ ਸੰਭਾਲੀ ਜਾ ਸਕਦੀ ਹੈ।

ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਕੀ ਸੋਚ ਹੈ, ਕੀ ਇਹੋ ਜਿਹਾ ਹੈ, ਇਕ ਹੈਂਡਲਰ ਜੋ ਕਿਸੇ ਭੀ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ? ਹਾਂ, ਬਿਲਕੁਲ, ਇਹ ਰਹੇ ਕੋਡ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇੱਕ ਸ਼ਬਦਕੋਸ਼ ਹੈ ਜਿਸ ਵਿੱਚ ਟੂਲ ਦੇ ਨਾਮ ਕੁੰਜੀਆਂ ਵਜੋਂ ਹਨ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

**TypeScript**

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if(!tool) {
        return {
            error: {
                code: "tool_not_found",
                message: `Tool ${name} not found.`
            }
       };
    }
    
    // args: request.params.arguments
    // TODO ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ਜਿਵੇਂ ਤੁਸੀਂ ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਤੋਂ ਵੇਖ ਸਕਦੇ ਹੋ, ਸਾਨੂੰ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਕਿਹੜੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨਾ ਹੈ ਤੇ ਕਿਸ ਆਰਗੁਮੈਂਟ ਨਾਲ ਇਹ ਕੰਮ ਕਰਨਾ ਹੈ, ਇਹ ਪਾਰਸ ਕਰਨਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਫਿਰ ਕਾਲ ਕਰਨੀ ਪੈਂਦੀ ਹੈ।

## ਵੈਰੀਫਿਕੇਸ਼ਨ ਨਾਲ ਵਿਧੀ ਦਾ ਸੁਧਾਰ

ਹੁਣ ਤੱਕ ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਟੂਲਜ਼, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਸ਼ਾਮਿਲ ਕਰਨ ਲਈ ਕੀਤੇ ਸਾਰੇ ਰਜਿਸਟਰੇਸ਼ਨਜ਼ ਨੂੰ ਇਹ ਦੋ ਹੈਂਡਲਰ ਪ੍ਰਤੀ ਫੀਚਰ ਕਿਸਮ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਹੋਰ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ? ਅਸੀਂ ਕੁਝ ਪ੍ਰਮਾਣਿਕਤਾ (ਵੈਰੀਫਿਕੇਸ਼ਨ) ਜੋੜਨੀ ਚਾਹੀਦੀ ਹੈ ਤਾਂ ਕਿ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਟੂਲ ਸਹੀ ਆਰਗੁਮੈਂਟਸ ਦੇ ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਹਰ ਰਨਟਾਈਮ ਇਸਦਾ ਆਪਣਾ ਹੱਲ ਹੁੰਦਾ ਹੈ, ਉਦਾਹਰਨ ਵਜੋਂ Python ਵਿੱਚ Pydantic ਵਰਗੀ ਅਤੇ TypeScript ਵਿੱਚ Zod ਵਰਗੀ ਵਰਤੋਂ ਹੁੰਦੀ ਹੈ। ਵਿਚਾਰ ਹੈ ਕਿ ਅਸੀਂ ਇਹ ਕਰੀਏ:

- ਇੱਕ ਫੀਚਰ (ਟੂਲ, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ) ਬਣਾਉਣ ਦੀ ਲੋਜਿਕ ਉਸਦੇ ਸਮਰਪਿਤ ਫੋਲਡਰ ਵਿੱਚ ਸਥਿਤ ਕਰਨ।
- ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ ਗੁਣਵੱਤਾ ਲਈ ਜਾਂਚਣ ਦਾ ਢੰਗ ਜੋ ਕਿ ਉਦਾਹਰਨ ਵਜੋਂ ਕਾਲ ਟੂਲ ਵਾਲੀ ਬੇਨਤੀ ਹੋ ਸਕਦੀ ਹੈ।

### ਫੀਚਰ ਬਣਾਉਣਾ

ਫੀਚਰ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਉਸ ਫੀਚਰ ਲਈ ਇੱਕ ਫਾਇਲ ਬਣਾਉਣੀ ਪਵੇਗੀ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਨਾਉਣਾ ਹੋਵੇਗਾ ਕਿ ਉਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਖੇਤਰ ਹਨ। ਟੂਲਜ਼, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਵਿੱਚ ਫਰਕ ਕੁਝ ਖੇਤਰਾਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।

**Python**

```python
# schema.py
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float

# add.py

from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ਪਾਈਡੈਂਟਿਕ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁਟ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ਪਾਈਡੈਂਟਿਕ ਸ਼ਾਮਲ ਕਰੋ, ਤਾਂ ਜੋ ਅਸੀਂ ਇਕ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ args ਦੀ ਪੁਸ਼ਟੀ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਅਸੀਂ ਇਹ ਕਰਦੇ ਹਾਂ:

- Pydantic ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਸਕੀਮਾ ਬਣਾਉਂਦੇ ਹਾਂ `AddInputModel` ਜਿਸ ਵਿੱਚ ਖੇਤਰ ਹਨ `a` ਅਤੇ `b` ਫਾਇਲ *schema.py* ਵਿੱਚ।
- ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ `AddInputModel` ਕਿਸਮ ਦਾ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਜੇ ਕੋਈ ਗਲਤ ਪੈਰਾਮੀਟਰ ਹੋਏ ਤਾਂ ਇਹ ਸਿਸਟਮ ਠੱਪ ਹੋ ਜਾਵੇਗਾ:

   ```python
   # add.py
    try:
        # Pydantic ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁਟ ਨੂੰ ਬਰੌਜ਼ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ਤੁਸੀਂ ਇਹ ਪਾਰਸਿੰਗ ਲੋਜਿਕ ਟੂਲ ਕਾਲ ਦੇ ਵਿੱਚ ਜਾਂ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਦੇ ਵੀ ਆਪਣੇ ਚੋਣ ਮੁਤਾਬਕ ਰੱਖ ਸਕਦੇ ਹੋ।

**TypeScript**

```typescript
// ਸਰਵਰ.ਟੀਐਸ
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { params: { name } } = request;
    let tool = tools.find(t => t.name === name);
    if (!tool) {
       return {
        error: {
            code: "tool_not_found",
            message: `Tool ${name} not found.`
        }
       };
    }
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);

       // @ts-ignore
       const result = await tool.callback(input);

       return {
          content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
      };
    } catch (error) {
       return {
          error: {
             code: "invalid_arguments",
             message: `Invalid arguments for tool ${name}: ${error instanceof Error ? error.message : String(error)}`
          }
    };
   }

});

// ਸਕੀਮਾ.ਟੀਐਸ
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// ਜੋੜੋ.ਟੀਐਸ
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

- ਸਾਰੇ ਟੂਲ ਕਾਲਾਂ ਦਾ ਹੈਂਡਲਰ ਜਿਸਦਾ ਕੰਮ ਹੈ ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ ਟੂਲ ਦੀ ਪਰਿਭਾਸ਼ਿਤ ਸਕੀਮਾ ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ਜੇ ਇਹ ਸਫਲ ਹੋ ਜਾਵੇ, ਤਾਂ ਅਸੀਂ ਅਸਲ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const result = await tool.callback(input);
    ```

ਜਿਵੇਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, ਇਹ ਵਿਧੀ ਇੱਕ ਬਹੁਤ ਵਧੀਆ ਵਾਸ਼ਤਾ ਬਣਾਉਂਦੀ ਹੈ ਕਿਉਂਕਿ ਹਰ ਚੀਜ਼ ਆਪਣੀ ਜਗ੍ਹਾ 'ਤੇ ਹੁੰਦੀ ਹੈ। *server.ts* ਇਕ ਬਹੁਤ ਛੋਟੀ ਫਾਇਲ ਹੈ ਜੋ ਸਿਰਫ ਰਿਕਵੇਸਟ ਹੈਂਡਲਰਜ਼ ਨੂੰ ਜੋੜਦੀ ਹੈ ਅਤੇ ਹਰ ਫੀਚਰ ਆਪਣੇ ਫੋਲਡਰ ਵਿੱਚ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ tools/, resources/ ਜਾਂ prompts/।

ਵਧੀਆ, ਆਓ ਅਗਲਾ ਕਦਮ ਬਣਾਈਏ।

## ਅਭਿਆਸ: ਲੋ-ਲੇਵਲ ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਕਰਾਂਗੇ:

1. ਲੋ-ਲੇਵਲ ਸਰਵਰ ਬਣਾਉਣਾ ਜੋ ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਅਤੇ ਕਾਲਿੰਗ ਦਾ ਹੈਂਡਲ ਕਰੇ।
2. ਇੱਕ ਐਸੀ ਵਾਸ਼ਤਾ ਲਾਗੂ ਕਰਨੀ ਜੋ ਤੁਸੀਂ ਅੱਗੇ ਵਧਾ ਸਕਦੇ ਹੋ।
3. ਪ੍ਰਮਾਣਿਕਤਾ ਜੋੜਨੀ ਤਾਂ ਕਿ ਤੁਹਾਡੇ ਟੂਲ ਕਾਲ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਪਰਖੇ ਜਾ ਸਕਣ।

### -1- ਵਾਸ਼ਤਾ ਬਣਾਉਣਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਉਹ ਵਾਸ਼ਤਾ ਜੋ ਅਸੀਂ_scale ਕਰ ਸਕੀਏ ਜਿਵੇਂ ਅਸੀਂ ਹੋਰ ਫੀਚਰ ਜੋੜੀਏ, ਇਹ ਹੈ:

**Python**

```text
server.py
--| tools
----| __init__.py
----| add.py
----| schema.py
client.py
```

**TypeScript**

```text
server.ts
--| tools
----| add.ts
----| schema.ts
client.ts
```

ਹੁਣ ਅਸੀਂ ਇੱਕ ਐਸਾ ਵਾਸ਼ਤਾ ਸੈੱਟ ਕੀਤਾ ਹੈ ਜੋ ਅਸੀਂ ਆਸਾਨੀ ਨਾਲ ਟੂਲਜ਼ ਨੂੰ tools ਫੋਲਡਰ ਵਿੱਚ ਜੋੜ ਸਕੀਏ। ресурсы ਅਤੇ prompts ਲਈ ਵੀ ਤੁਸੀਂ ਸਬ-ਡਾਇਰੈਕਟਰੀਜ ਬਣਾ ਸਕਦੇ ਹੋ।

### -2- ਟੂਲ ਬਣਾਉਣਾ

ਚਲੋ ਦੇਖੀਏ ਟੂਲ ਬਣਾਉਣਾ ਕਿਵੇਂ ਹੁੰਦਾ ਹੈ। ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਆਪਣੇ *tool* ਸਬਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਜਿਵੇਂ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ਪਾਈਡੈਂਟਿਕ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਦੀ ਵੈਧਤਾ ਦੀ ਜਾਂਚ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ਪਾਈਡੈਂਟਿਕ ਜੋੜੋ, ਤਾਂ ਜੋ ਅਸੀਂ ਇੱਕ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ ਆਰਗੂਮੈਂਟਾਂ ਦੀ ਵੈਧਤਾ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਅਸੀਂ ਦੇਖਦੇ ਹਾਂ ਕਿ ਕਿਵੇਂ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਇੰਪੁੱਟ ਸਕੀਮਾ Pydantic ਨਾਲ ਡਿਫਾਈਨ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇੱਕ ਹੈਂਡਲਰ ਬਣਾਉਂਦੇ ਹਾਂ ਜੋ ਟੂਲ ਕਾਲ ਹੋਣ 'ਤੇ ਚਲਾਇਆ ਜਾਵੇਗਾ। ਆਖ਼ਰੀ ਵਿੱਚ ਅਸੀਂ `tool_add` ਨੂੰ ਐਕਸਪੋਰਟ ਕਰਦੇ ਹਾਂ ਜੋ ਇਹ ਸਾਰੀਆਂ ਪ੍ਰਾਪਰਟੀਜ਼ ਨੂੰ ਰੱਖਦਾ ਹੈ।

ਇਸਦੇ ਨਾਲ *schema.py* ਵੀ ਹੈ ਜੋ ਟੂਲ ਦੀ ਇੰਪੁੱਟ ਸਕੀਮਾ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ਸਾਡੇ ਕੋਲ *__init__.py* ਭੀ ਭਰਨੀ ਪੈਂਦੀ ਹੈ ਤਾਂ ਜੋ tools ਡਾਇਰੈਕਟਰੀ ਮੋਡੀਊਲ ਵਜੋਂ ਮੰਨੀ ਜਾਵੇ। ਇਸਦੇ ਨਾਲ-ਨਾਲ ਅਸੀਂ ਇਸਦੇ ਮੋਡੀਊਲਾਂ ਨੂੰ ਐਕਸਪੋਰਟ ਕਰਦੇ ਹਾਂ ਜਿਵੇਂ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ਜਿਵੇਂ-ਜਿਵੇਂ ਅਸੀਂ ਹੋਰ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰਦੇ ਹਾਂ, ਅਸੀਂ ਇਸ ਫਾਇਲ ਵਿੱਚ ਵੀ ਹੁਣੇ ਕਰਦੇ ਰਹਾਂਗੇ।

**TypeScript**

```typescript
import { Tool } from "./tool.js";
import { MathInputSchema } from "./schema.js";
import { zodToJsonSchema } from "zod-to-json-schema";

export default {
    name: "add",
    rawSchema: MathInputSchema,
    inputSchema: zodToJsonSchema(MathInputSchema),
    callback: async ({ a, b }) => {
        return {
            content: [{ type: "text", text: String(a + b) }]
        };
    }
} as Tool;
```

ਇੱਥੇ ਅਸੀਂ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿਸਦੀ ਸਮੱਗਰੀ ਹੈ:

- name, ਇਹ ਟੂਲ ਦਾ ਨਾਮ ਹੈ।  
- rawSchema, ਇਹ Zod ਸਕੀਮਾ ਹੈ ਜੋ ਆਉਣ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰੇਗਾ।  
- inputSchema, ਇਹ handler ਵੱਲੋਂ ਵਰਤੀ ਜਾਣ ਵਾਲੀ ਸਕੀਮਾ ਹੈ।  
- callback, ਇਹ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ।  

ਇੱਥੇ `Tool` ਵੀ ਹੈ ਜੋ ਇਸ ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਐਸੀ ਕਿਸਮ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੋ MCP ਸਰਵਰ ਹੈਂਡਲਰ ਸਮਝਦਾ ਹੈ, ਅਤੇ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ਅਤੇ *schema.ts* ਹੈ ਜਿੱਥੇ ਅਸੀਂ ਹਰ ਟੂਲ ਦੀ ਇੰਪੁੱਟ ਸਕੀਮਾਵਾਂ ਸਟੋਰ ਕਰਦੇ ਹਾਂ, ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਹੁੰਦੀ ਹੈ, ਹੁਣ ਸਿਰਫ ਇੱਕ ਸਕੀਮਾ ਹੈ ਪਰ ਜਿਵੇਂ ਜਿਹੇ ਅਸੀਂ ਹੋਰ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ, ਅਸੀਂ ਹੋਰ ਐਂਟਰੀਆਂ ਜੋੜਾਂਗੇ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ਵਧੀਆ, ਆਓ ਹੁਣ ਅਸੀਂ ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਸੰਭਾਲਦੇ ਹਾਂ।

### -3- ਟੂਲ ਲਿਸਟਿੰਗ ਸੰਭਾਲਣਾ

ਹੁਣ, ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਸੰਭਾਲਣ ਲਈ, ਸਾਨੂੰ ਆਪਣੇ ਸਰਵਰ ਫਾਇਲ ਵਿੱਚ ਇੱਕ ਰਿਕਵੇਸਟ ਹੈਂਡਲਰ ਸੈੱਟ ਕਰਨਾ ਪਵੇਗਾ:

**Python**

```python
# ਕੋਡ ਸਾਰ ਸੰਭਾਲ ਲਈ ਛੱਡ ਦਿੱਤਾ ਗਿਆ
from tools import tools

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tool_list = []
    print(tools)

    for tool in tools.values():
        tool_list.append(
            types.Tool(
                name=tool["name"],
                description=tool["description"],
                inputSchema=pydantic_to_json(tool["input_schema"]),
            )
        )
    return tool_list
```

ਇੱਥੇ ਅਸੀਂ `@server.list_tools` ਡੈਕੋਰੇਟਰ ਅਤੇ `handle_list_tools` ਫੰਕਸ਼ਨ ਵਧਾਉਂਦੇ ਹਾਂ। ਇਸ ਵਿੱਚ ਸਾਡੇ ਕੋਲ ਇੱਕ ਟੂਲਜ਼ ਦੀ ਲਿਸਟ ਤਿਆਰ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। ਹਰ ਟੂਲ ਦਾ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ inputSchema ਹੋਣਾ ਜਰੂਰੀ ਹੈ।  

**TypeScript**

ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਲਈ, ਸਰਵਰ ਤੇ `setRequestHandler` ਕਾਲ ਕਰਨੀ ਪੈਂਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਉਹ ਸਕੀਮਾ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ ਜੋ ਅਸੀਂ ਕਰ ਰਹੇ ਹਾਂ, ਇਸ ਮਾਮਲੇ ਵਿੱਚ `ListToolsRequestSchema`।

```typescript
// ਇੰਡੈਕਸ.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// ਸਰਵਰ.ts
// ਸੰਖੇਪ ਲਈ ਕੋਡ ਛੱਡਿਆ ਗਿਆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ਦਰਜ ਕੀਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
  return {
    tools: tools
  };
});
```

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਦਾ ਹਿੱਸਾ ਸਹੀ ਕਰ ਲਿਆ, ਚਲੋ ਦੂਜੇ ਹਿੱਸੇ ਦੀ ਵੱਲ ਚੱਲੀਏ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਟੂਲ ਕਾਲ ਕਰਦੇ ਹਾਂ।

### -4- ਟੂਲ ਕਾਲ ਸੰਭਾਲਣਾ

ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਇੱਕ ਹੋਰ ਰਿਕਵੇਸਟ ਹੈਂਡਲਰ ਬਣਾਉਣਾ ਪਵੇਗਾ ਜੋ ਉਨ੍ਹਾਂ ਬੇਨਤੀਆਂ ਨੂੰ ਸੰਭਾਲੇ ਜਿਸ ਵਿੱਚ ਫੀਚਰ ਕਿਹੜਾ ਕਾਲ ਕਰਨਾ ਹੈ ਤੇ ਉਸਦੇ ਆਰਗੁਮੈਂਟ ਕੀ ਹਨ, ਇਹ ਦਿੱਤਾ ਹੋਵੇ।

**Python**

ਆਓ `@server.call_tool` ਡੈਕੋਰੇਟਰ ਵਰਤੀਏ ਅਤੇ ਇਸਨੂੰ `handle_call_tool` ਫੰਕਸ਼ਨ ਨਾਲ ਇੰਪਲੀਮੈਂਟ ਕਰੀਏ। ਇਸ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਸਾਨੂੰ ਟੂਲ ਦਾ ਨਾਮ, ਉਸਦੇ ਆਰਗੁਮੈਂਟ ਪਾਰਸ ਕਰਨੇ ਨੇ ਅਤੇ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਆਰਗੁਮੈਂਟਸ ਟੂਲ ਲਈ ਸਹੀ ਹਨ। ਅਸੀਂ ਇਹ ਜਾਂ ਤਾਂ ਇਸ ਫੰਕਸ਼ਨ ਦੇ ਅੰਦਰ ਜਾਂ ਅਸਲ ਟੂਲ ਵਿੱਚ ਗਰੰਟੀ ਕਰ ਸਕਦੇ ਹਾਂ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜਿਸ ਵਿਚ ਟੂਲ ਦੇ ਨਾਮ ਕੁੰਜੀਆਂ ਵਜੋਂ ਹਨ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ਇਥੇ ਕੀ ਹੁੰਦਾ ਹੈ:

- ਸਾਡਾ ਟੂਲ ਨਾਮ ਪਹਿਲਾਂ ਹੀ ਇੰਪੁੱਟ ਪੈਰਾਮੀਟਰ `name` ਦੇ ਰੂਪ ਵਿੱਚ ਮੌਜੂਦ ਹੈ, ਜਿਸ ਤਰ੍ਹਾਂ ਸਾਡੇ ਆਰਗੁਮੈਂਟ `arguments` ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਹਨ।

- ਟੂਲ ਨੂੰ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਆਰਗੁਮੈਂਟ ਦੀ ਪ੍ਰਮਾਣਿਕਤਾ `handler` ਪ੍ਰਾਪਰਟੀ ਵਿੱਚ ਹੁੰਦੀ ਹੈ ਜੋ ਕਿ ਇੱਕ ਫੰਕਸ਼ਨ ਹੈ, ਜੇ ਇਹ ਨਾਕਾਮ ਹੋਵੇ ਤਾਂ ਇਹ ਐਕਸਪਸ਼ਨ ਉਠਾਏਗਾ।

ਹੁਣ ਸਾਡੇ ਕੋਲ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਅਤੇ ਕਾਲ ਕਰਨ ਦੀ ਪੂਰੀ ਸਮਝ ਹੈ।

ਪੂਰਾ ਉਦਾਹਰਨ ਦੇਖੋ [ਇੱਥੇ](./code/README.md)

## ਐਸਾਈਨਮੈਂਟ

ਜੋ ਕੋਡ ਤੁਹਾਨੂੰ ਦਿੱਤਾ ਗਿਆ ਹੈ ਉਸਨੂੰ ਵਧਾਉਂਦੇ ਹੋਏ ਕਈ ਟੂਲਜ਼, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਸ਼ਾਮਿਲ ਕਰੋ ਅਤੇ ਵੇਖੋ ਕਿ ਤੁਸੀਂ ਸਿਰਫ tools ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਫਾਇਲਾਂ ਸ਼ਾਮਿਲ ਕਰ ਰਹੇ ਹੋ, ਹੋਰ ਕਿੱਥੇ ਨਹੀਂ।

*ਕੋਈ ਹੱਲ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ*

## ਸੰਖੇਪ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਵੇਖਿਆ ਕਿ ਲੋ-ਲੇਵਲ ਸਰਵਰ ਵਿਧੀ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ ਅਤੇ ਕਿਵੇਂ ਇਹ ਸਾਨੂੰ ਇੱਕ ਸੁੰਦਰ ਵਾਸ਼ਤਾ ਤਿਆਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ ਜਿਸ ਤੇ ਅਸੀਂ ਮੈਂਟੇਨ ਕਰ ਸਕੀਏ। ਅਸੀਂ ਪ੍ਰਮਾਣਿਕਤਾ ਬਾਰੇ ਵੀ ਵਿਚਾਰ ਕੀਤਾ ਅਤੇ ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਕਿਵੇਂ ਪ੍ਰਮਾਣਿਕਤਾ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨਾਲ ਕੰਮ ਕਰਕੇ ਇੰਪੁੱਟ ਵੈਰੀਫਾਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [ਸਿਮਪਲ ਆਥੈਂਟੀਕੇਸ਼ਨ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡਿਸਕਲੇਮਰ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਵਰਣ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
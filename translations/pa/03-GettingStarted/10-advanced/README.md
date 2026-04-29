# ਅਡਵਾਂਸਡ ਸਰਵਰ ਵਰਤੋਂ

MCP SDK ਵਿੱਚ ਦੋ ਵੱਖ-ਵੱਖ ਤਰ੍ਹਾਂ ਦੇ ਸਰਵਰ ਦਰਸਾਏ ਗਏ ਹਨ, ਤੁਹਾਡਾ ਨਾਰਮਲ ਸਰਵਰ ਅਤੇ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ। ਆਮ ਤੌਰ 'ਤੇ, ਤੁਸੀਂ ਇਸ ਵਿੱਚ ਫੀਚਰ ਜੋੜਨ ਲਈ ਰੈਗੂਲਰ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ। ਤਾਂ ਵੀ ਕੁਝ ਕੇਸਾਂ ਵਿੱਚ, ਤੁਸੀਂ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ 'ਤੇ ਨਿਰਭਰ ਕਰਨਾ ਚਾਹੋਗੇ ਜਿਵੇਂ ਕਿ:

- ਬਿਹਤਰ ਆਰਕੀਟੈਕਚਰ। ਦੋਹਾਂ ਰੈਗੂਲਰ ਸਰਵਰ ਅਤੇ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਸਾਫ-ਸੁਥਰੀ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣਾ ਸੰਭਵ ਹੈ ਪਰ ਇਹ ਦਲੀਲ ਦਿੱਤੀ ਜਾ ਸਕਦੀ ਹੈ ਕਿ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਇਹ ਥੋੜ੍ਹਾ ਜਿਆਦਾ ਆਸਾਨ ਹੈ।
- ਫੀਚਰ ਉਪਲਬਧਤਾ। ਕੁਝ ਅੱਗੇ ਵਧੇ ਫੀਚਰ ਸਿਰਫ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਨਾਲ ਹੀ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਤੁਸੀਂ ਇਸਨੂੰ ਆਉਣ ਵਾਲੇ ਅਧਿਆਇਆਂ ਵਿੱਚ ਦੇਖੋਗੇ ਜਦੋਂ ਅਸੀਂ ਸੈਂਪਲਿੰਗ ਅਤੇ ਇਲਿਸਿਟੇਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ।

## ਰੈਗੂਲਰ ਸਰਵਰ vs ਲੋਅ-ਲੇਵਲ ਸਰਵਰ

ਇਹਾਂ MCP ਸਰਵਰ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ ਰੈਗੂਲਰ ਸਰਵਰ ਨਾਲ ਹੈ

**Python**

```python
mcp = FastMCP("Demo")

# ਇੱਕ ਜੋੜਨ ਦਾ ਸੰਦ ਸ਼ਾਮਲ ਕਰੋ
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

// ਇੱਕ ਜੋੜਨ ਵਾਲਾ ਯੰਤਰ ਸ਼ਾਮਲ ਕਰੋ
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

ਮੁੜ ਮਕਸਦ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਵਿਸ਼ੇਸ਼ ਤੌਰ 'ਤੇ ਹਰ ਇੱਕ ਟੂਲ, ਰਿਸੋਰਸ ਜਾਂ ਪ੍ਰੋਂਪਟ ਜੋ ਤੁਸੀਂ ਸਰਵਰ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਜੋੜਦੇ ਹੋ। ਇਸ ਵਿੱਚ ਕੋਈ ਗਲਤ ਨਹੀਂ ਹੈ।  

### ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਦਾ ਤਰੀਕਾ

ਪਰ ਜਦੋਂ ਤੁਸੀਂ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਤਰੀਕੇ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ ਇਹ ਕੁਝ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਸੋਚਣਾ ਪੈਂਦਾ ਹੈ। ਹਰ ਇੱਕ ਟੂਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਫੀਚਰ ਦੀ ਕਿਸਮ (ਟੂਲਜ਼, ਰਿਸੋਰਸਜ਼ ਜਾਂ ਪ੍ਰੋਂਪਟਸ) ਲਈ ਦੋ ਹੈਂਡਲਰ ਬਣਾਉਂਦੇ ਹੋ। ਉਦਾਹਰਨ ਵੱਜੋਂ ਟੂਲਜ਼ ਲਈ ਕੇਵਲ ਦੋ ਫੰਕਸ਼ਨ ਹੁੰਦੇ ਹਨ:

- ਸਾਰੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀਬੱਧ ਕਰਨਾ। ਇੱਕ ਫੰਕਸ਼ਨ ਸਾਰੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਦੇਣ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੁੰਦਾ ਹੈ।
- ਸਾਰੇ ਟੂਲਜ਼ ਨੂੰ ਕਾਲ ਕਰਨ ਨੂੰ ਸੰਭਾਲਣਾ। ਇੱਥੇ ਵੀ ਇੱਕੋ ਫੰਕਸ਼ਨ ਯੂਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

ਇਹ ਉਮੀਦ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਕਿ ਇਸ ਨਾਲ ਕੰਮ ਘੱਟ ਹੋ ਜਾਵੇਗਾ, ਸਹੀ? ਇਸ ਲਈ ਟੂਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਮੈਨੂੰ ਸਿਰਫ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਜਦੋਂ ਮੈਂ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਦਿੰਦਾ ਹਾਂ ਤਾਂ ਟੂਲ ਸੂਚੀ ਵਿੱਚ ਹੋਵੇ ਅਤੇ ਜਦੋਂ ਕਿ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਹੁੰਦੀ ਹੈ ਤਾਂ ਇਸਨੂੰ ਕਾਲ ਕੀਤਾ ਜਾਵੇ।

ਆਓ ਹੁਣ ਦੇਖੀਏ ਕਿ ਕੋਡ ਹੁਣ ਕਿਵੇਂ ਦੇਖਦਾ ਹੈ:

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
  // ਦਰਜ ਕੀਤੇ ਗਏ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
  return {
    tools: [{
        name: "add",
        description: "Add two numbers",
        inputSchema: {
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

ਇੱਥੇ ਸਾਨੂੰ ਇੱਕ ਐਸਾ ਫੰਕਸ਼ਨ ਮਿਲਦਾ ਹੈ ਜੋ ਫੀਚਰਜ਼ ਦੀ ਸੂਚੀ ਦਿੰਦਾ ਹੈ। ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਹੁਣ `name`, `description` ਅਤੇ `inputSchema` ਵਰਗੇ ਫੀਲਡਾਂ ਰੱਖਦੀ ਹੈ ਜੋ ਰਿਟਰਨ ਟਾਈਪ ਨੂੰ ਪੂਰਾ ਕਰਦੀ ਹੈ। ਇਸ ਨਾਲ ਸਾਡੀਆਂ ਟੂਲਜ਼ ਅਤੇ ਫੀਚਰ ਡਿਫਿਨੀਸ਼ਨ ਕਿਸੇ ਹੋਰ ਥਾਂ ਰੱਖਣ ਦੀ ਆਜ਼ਾਦੀ ਮਿਲਦੀ ਹੈ। ਅਸੀਂ ਹੁਣ ਸਾਰੇ ਟੂਲਜ਼ ਨੂੰ ਇੱਕ ਟੂਲਜ਼ ਫੋਲਡਰ ਵਿੱਚ ਬਣਾਉਣਾ ਹੈ ਅਤੇ ਉਹੀ ਗੱਲ ਤੁਹਾਡੇ ਸਾਰੇ ਫੀਚਰਜ਼ ਲਈ ਲਾਗੂ ਹੁੰਦੀ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਅਚਾਨਕ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਖਦਾ ਹੈ:

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

ਵਧੀਆ, ਸਾਡੀ ਆਰਕੀਟੈਕਚਰ ਕਾਫੀ ਸਾਫ਼-ਸੁਥਰੀ ਬਣ ਸਕਦੀ ਹੈ।

ਟੂਲ ਕਾਲ ਕਰਨ ਦਾ ਕੰਮ ਕਿਵੇਂ ਹੁੰਦਾ ਹੈ, ਕੀ ਇਹੀ ਵਿਚਾਰ ਹੈ ਕਿ ਇੱਕ ਹੈਂਡਲਰ ਹੈ ਜੋ ਕਿਸੇ ਵੀ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੇ? ਹਾਂ, ਬ bilkul, ਇਹ ਕੋਡ ਹੈ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਟੂਲ ਨਾਂ ਕੁੰਜੀਆਂ ਵਜੋਂ ਹਨ
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
    
    // ਦਲੀਲਾਂ: request.params.arguments
    // TODO ਸੰਦ ਨੂੰ ਕਾਲ ਕਰੋ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ਜਿਵੇਂ ਤੁਸੀਂ ਉੱਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਦੇਖ ਸਕਦੇ ਹੋ, ਸਾਨੂੰ ਇਹ ਜਾਣਨਾ ਪੈਂਦਾ ਹੈ ਕਿ ਕਿਹੜਾ ਟੂਲ ਕਾਲ ਕਰਨਾ ਹੈ, ਕਿਸ ਆਰਗੁਮੈਂਟ ਨਾਲ, ਫਿਰ ਸਾਨੂੰ ਟੂਲ ਕੋਲ ਕਾਲ ਕਰਨੀ ਹੁੰਦੀ ਹੈ।

## ਵੈਰੀਫਿਕੇਸ਼ਨ ਨਾਲ ਤਰੀਕੇ ਦੀ ਸੁਧਾਰ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਹੈ ਕਿ ਟੂਲਜ਼, ਰਿਸੋਰਸਜ਼ ਅਤੇ ਪ੍ਰੋਂਪਟਸ ਜੋੜਨ ਲਈ ਤੁਹਾਡੇ ਸਾਰੇ ਰਜਿਸਟਰੇਸ਼ਨ ਨੂੰ ਕਿਸ ਤਰ੍ਹਾਂ ਦੋ ਹੈਂਡਲਰਜ਼ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਅੱਗੇ ਹੋਰ ਕੀ ਜਰੂਰੀ ਹੈ? ਸਾਨੂੰ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਗਾਉਣੀ ਚਾਹੀਦੀ ਹੈ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣ ਸਕੇ ਕਿ ਟੂਲ ਨੂੰ ਸਹੀ ਆਰਗੁਮੈਂਟਜ਼ ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਹਰ ਰਨਟਾਈਮ ਲਈ ਇਸਦਾ ਆਪਣਾ ਹੱਲ ਹੁੰਦਾ ਹੈ, ਉਦਾਹਰਨ ਲਈ Python Pydantic ਵਰਤਦਾ ਹੈ ਅਤੇ TypeScript Zod। ਇਸ ਦੀ ਵਿਚਾਰਧਾਰਾ ਇਹ ਹੈ:

- ਇੱਕ ਫੀਚਰ (ਟੂਲ, ਰਿਸੋਰਸ ਜਾਂ ਪ੍ਰੋਂਪਟ) ਬਣਾਉਣ ਲਈ ਲੋਜਿਕ ਉਸਦੇ ਸਮਰਪਿਤ ਫੋਲਡਰ ਵਿੱਚ ਰੱਖੋ।
- ਜਿਵੇਂ ਕਿ ਟੂਲ ਕਾਲ ਕਰਨ ਵਾਲੀ ਅਰਜ਼ੀ ਨੂੰ ਵੈਧਾ ਕਰਨਾ।

### ਇਕ ਫੀਚਰ ਬਣਾਉਣ ਲਈ

ਇੱਕ ਫੀਚਰ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਉਸ ਫੀਚਰ ਲਈ ਇੱਕ ਫਾਈਲ ਬਣਾਉਣੀ ਪਏਗੀ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਏਗਾ ਕਿ ਇਸ ਵਿੱਚ ਲਾਜ਼ਮੀ ਫੀਲਡ ਹਨ। ਜਿਹੜੇ ਟੂਲਜ਼, ਰਿਸੋਰਸਜ਼ ਅਤੇ ਪ੍ਰੋਂਪਟਸ ਵਿੱਚ ਕੁਝ ਫਰਕ ਹੁੰਦੇ ਹਨ।

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
        # Pydantic ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਦੀ ਵੈਰੀਫਿਕੇਸ਼ਨ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ਸ਼ਾਮਲ ਕਰੋ, ਤਾਂ ਜੋ ਅਸੀਂ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ args ਨੂੰ ਵੈਲੀਡੇਟ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਅਸੀਂ ਕੀ ਕਰਦੇ ਹਾਂ:

- Pydantic ਦੀ ਵਰਤੋਂ ਕਰਕੇ `AddInputModel` ਨਾਂ ਦਾ ਸਕੀਮਾ ਬਣਾਇਆ ਜਿਸ ਵਿੱਚ ਫੀਲਡਾਂ `a` ਅਤੇ `b` ਹਨ ਜੋ *schema.py* ਫਾਈਲ ਵਿੱਚ ਹੈ।
- ਆ ਰਹੀ ਅਰਜ਼ੀ ਨੂੰ ਟਾਈਪ `AddInputModel` ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼, ਜੇਕਰ ਪੈਰਮੀਟਰਾਂ ਵਿੱਚ ਅਸੁਮਤਲ ਹੈ ਤਾਂ ਇਹ ਕਰੈਸ਼ ਕਰ ਜਾਵੇਗਾ:

   ```python
   # add.py
    try:
        # ਇਨਪੁੱਟ ਦਾ ਮਾਡਲ ਪਾੜਾਂ ਵਲੋਂ ਜਾਂਚ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ਤੁਸੀਂ ਇਹ ਪਾਰਸਿੰਗ ਲੌਜਿਕ ਟੂਲ ਕਾਲ ਵਿੱਚ ਖੁਦ ਜਾਂ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਵਿੱਚ ਰੱਖ ਸਕਦੇ ਹੋ।

**TypeScript**

```typescript
// ਸਰਵਰ.ts
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

// ਸਕੀਮਾ.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// ਜੋੜੋ.ts
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

- ਸਾਰੇ ਟੂਲ ਕਾਲਾਂ ਵਾਲੇ ਹੈਂਡਲਰ ਵਿੱਚ, ਅਸੀਂ ਆ ਰਹੀ ਅਰਜ਼ੀ ਨੂੰ ਟੂਲ ਦੇ ਪਰਿਭਾਸ਼ਿਤ ਸਕੀਮਾ ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ਜੇਕਰ ਇਹ ਸਫਲ ਹੋ ਜਾਂਦਾ ਹੈ ਤਾਂ ਅਸਲ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const result = await tool.callback(input);
    ```

ਜਿਵੇਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, ਇਹ ਤਰੀਕਾ ਇੱਕ ਵਧੀਆ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਂਦਾ ਹੈ ਕਿਉਂਕਿ ਹਰ ਚੀਜ਼ ਆਪਣੀ ਥਾਂ ਤੇ ਹੈ, *server.ts* ਇੱਕ ਬਹੁਤ ਛੋਟੀ ਫਾਈਲ ਹੈ ਜੋ ਸਿਰਫ ਰਿਕਵੈਸਟ ਹੈਂਡਲਰਜ਼ ਨੂੰ ਜੋੜਦਾ ਹੈ ਅਤੇ ਹਰ ਫੀਚਰ ਆਪਣੇ-ਆਪਣੇ ਫੋਲਡਰ ਵਿੱਚ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ ਟੂਲਜ਼/, ਰਿਸੋਰਸਜ਼/ ਜਾਂ /prompts।

ਵਧੀਆ, ਆਓ ਇਸ ਨੂੰ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਬਣਾਈਏ।

## ਅਭਿਆਸ: ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਕਰਾਂਗੇ:

1. ਇੱਕ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਬਣਾਉਣਾ ਜੋ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਅਤੇ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੋਵੇ।
1. ਇੱਕ ਐਸਾ ਆਰਕੀਟੈਕਚਰ ਲਾਗੂ ਕਰਨਾ ਜਿਸ ਉੱਤੇ ਤੁਸੀਂ ਅੱਗੇ ਵਧ ਸਕੋ।
1. ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਵੈਰੀਫਿਕੇਸ਼ਨ ਜੋੜੋ ਕਿ ਟੂਲ ਕਾਲਾਂ ਦਾ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਤਸਦੀਕ ਕੀਤਾ ਗਿਆ ਹੈ।

### -1- ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਸਾਨੂੰ ਇੱਕ ਐਸਾ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣਾ ਹੈ ਜੋ ਜਿਵੇਂ ਜਿਵੇਂ ਫੀਚਰ ਵਧਦੇ ਹਨ ਉਹ ਸਧਾਰਨ ਰਹੇ, ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਖਦਾ ਹੈ:

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

ਹੁਣ ਅਸੀਂ ਇੱਕ ਐਸਾ ਆਰਕੀਟੈਕਚਰ ਸੈੱਟਅਪ ਕੀਤਾ ਹੈ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਅਸੀਂ ਆਸਾਨੀ ਨਾਲ ਟੂਲਜ਼ ਫੋਲਡਰ ਵਿੱਚ ਨਵੇਂ ਟੂਲ ਸ਼ਾਮਲ ਕਰ ਸਕੀਏ। ਤੁਹਾਨੂੰ resources ਅਤੇ prompts ਲਈ ਸਬਡਾਇਰੈਕਟਰੀ ਬਣਾਉਣ ਲਈ ਇਸ ਪੈਟਰਨ ਨੂੰ ਅਨੁਸਰਨਾ ਚਾਹੀਦਾ ਹੈ।

### -2- ਟੂਲ ਬਣਾਉਣਾ

ਆਓ ਵੇਖੀਏ ਟੂਲ ਬਣਾਉਣਾ ਕਿਵੇਂ ਹੁੰਦਾ ਹੈ। ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਉਸਦੇ *tool* ਸਬਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਬਣਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿਵੇਂ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ਪਾਈਡੈਂਟਿਕ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਨੂੰ ਵੈਧ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # ਟੂਡੂ: ਪਾਈਡੈਂਟਿਕ ਸ਼ਾਮਲ ਕਰੋ, ਤਾਂ ਜੋ ਅਸੀਂ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ ਆਰਗੂੰ ਨੂੰ ਵੈਧ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਅਸੀਂ ਵੇਖਦੇ ਹਾਂ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾ Pydantic ਨਾਲ ਡਿਫਾਈਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਹੈਂਡਲਰ ਜਿਸਨੂੰ ਟੂਲ ਕਾਲ ਕਰਨ ਉੱਤੇ ਵਜਾਇਆ ਜਾਂਦਾ ਹੈ। ਆਖਰੀ ਵਿੱਚ, ਅਸੀਂ `tool_add` ਨੂੰ ਐਕਸਪੋਰਟ ਕਰਦੇ ਹਾਂ ਜੋ ਇਹ ਸਾਰੇ ਗੁਣ ਰੱਖਦਾ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ।

ਇਸਦੇ ਨਾਲ *schema.py* ਵੀ ਹੈ ਜੋ ਟੂਲ ਲਈ ਇਨਪੁਟ ਸਕੀਮਾ ਡਿਫਾਈਨ ਕਰਦਾ ਹੈ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ਸਾਨੂੰ *__init__.py* ਫਾਈਲ ਨੂੰ ਭਰਨਾ ਵੀ ਪਏਗਾ ਤਾਂ ਜੋ ਟੂਲਜ਼ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਮਾਡਿਊਲ ਵਜੋਂ ਮੰਨਿਆ ਜਾਵੇ। ਸਾਥ ਹੀ, ਸਾਨੂੰ ਮਾਡਿਊਲਜ਼ ਨੂੰ ਐਕਸਪੋਰਟ ਕਰਨਾ ਪਏਗਾ ਇੰਝ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ਜਿਵੇਂ ਜਿਵੇਂ ਅਸੀਂ ਹੋਰ ਟੂਲਜ਼ ਸ਼ਾਮਲ ਕਰਾਂਗੇ, ਅਸੀਂ ਇਸ ਫਾਈਲ ਵਿੱਚ ਵੀ ਵਰਧੀ ਕਰ ਸਕਦੇ ਹਾਂ।

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

ਇੱਥੇ ਅਸੀਂ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਸਮੱਗਰੀ ਹਨ:

- name, ਟੂਲ ਦਾ ਨਾਮ।
- rawSchema, ਇਹ Zod ਸਕੀਮਾ ਹੈ, ਜੋ ਟੂਲ ਕਾਲਾਂ ਦੀ ਵੈਲੀਡੇਸ਼ਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ।
- inputSchema, ਇਹ ਹੈਂਡਲਰ ਦੁਆਰਾ ਵਰਤਿਆ ਜਾਵੇਗਾ।
- callback, ਜੋ ਟੂਲ ਨੂੰ ਸੰਦੂਰ ਕਰਦਾ ਹੈ।

ਫਿਰ `Tool` ਹੈ ਜੋ ਇਸ ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਉਸ ਟਾਈਪ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੋ mcp ਸਰਵਰ ਹੈਂਡਲਰ ਸਵੀਕਾਰ ਕਰਦਾ ਹੈ ਅਤੇ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ਅਤੇ *schema.ts* ਹੈ ਜਿੱਥੇ ਅਸੀਂ ਹਰ ਟੂਲ ਲਈ ਇਨਪੁਟ ਸਕੀਮਾ ਰੱਖਦੇ ਹਾਂ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਖਦਾ ਹੈ, ਹੁਣ ਤੱਕ ਇੱਕ ਸਕੀਮਾ ਹੈ ਪਰ ਜਿਵੇਂ ਜਿਵੇਂ ਅਸੀਂ ਹੋਰ ਟੂਲ ਸ਼ਾਮਲ ਕਰਾਂਗੇ, ਹੋਰ ਐਂਟਰੀਜ਼ ਵੀ ਕਰੋਗੇ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ਵਧੀਆ, ਆਓ ਹੁਣ ਸਾਡੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਬਣਾਉਣ 'ਤੇ ਕੰਮ ਕਰੀਏ।

### -3- ਟੂਲ ਲਿਸਟਿੰਗ ਦਾ ਹੈਂਡਲਿੰਗ

ਅਗਲਾ ਕਦਮ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਨੂੰ ਹੈਂਡਲ ਕਰਨ ਲਈ ਇੱਕ ਰਿਕਵੈਸਟ ਹੈਂਡਲਰ ਬਣਾਉਣਾ ਹੈ। ਇਹ ਤਾਂ ਤੁਹਾਡੇ ਸਰਵਰ ਫਾਈਲ ਵਿੱਚ ਇਹਨਾਂ ਚੀਜ਼ਾਂ ਨੂੰ ਜੋੜੋ:

**Python**

```python
# ਸਾਰ ਸੰਖੇਪ ਲਈ ਕੋਡ ਹਟਾਇਆ ਗਿਆ ਹੈ
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

ਇੱਥੇ ਅਸੀਂ ਡੈਕੋਰੇਟਰ `@server.list_tools` ਜੋੜਦੇ ਹਾਂ ਅਤੇ ਇਸ ਨੂੰ ਲਾਗੂ ਕਰਦੇ ਹਾਂ `handle_list_tools` ਫੰਕਸ਼ਨ ਨਾਲ। ਇਸ ਵਿੱਚ ਅਸੀਂ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਤਿਆਰ ਕਰਦੇ ਹਾਂ। ਧਿਆਨ ਰਹੇ ਕਿ ਹਰ ਟੂਲ ਨੂੰ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ inputSchema ਦੀ ਲੋੜ ਹੈ।   

**TypeScript**

ਟੂਲ ਲਿਸਟਿੰਗ ਲਈ ਬੇਨਤੀ ਹੈਂਡਲਰ ਸੈੱਟ ਕਰਨ ਲਈ ਸਾਨੂੰ ਸਰਵਰ ਉੱਤੇ `setRequestHandler` ਕਾਲ ਕਰਨੀ ਹੈ ਜਿਸਦੀ ਸਕੀਮਾ ਉਸ ਕਾਮ ਲਈ ਮੇਲ ਖਾਂਦੀ ਹੋਵੇ, ਇਸ ਮਾਮਲੇ ਵਿੱਚ `ListToolsRequestSchema`।

```typescript
// index.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// server.ts
// ਸਖਤੀ ਲਈ ਕੋਡ ਛੱਡ ਦਿਤਾ ਗਿਆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ਦਰਜ ਔਜ਼ਾਰਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
  return {
    tools: tools
  };
});
```

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਦਾ ਹਿੱਸਾ ਹੱਲ ਕਰ ਲਿਆ ਹੈ, ਆਓ ਅਗਲੇ ਕਦਮ ਦੇਖੀਏ ਕਿ ਟੂਲ ਕਿਵੇਂ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

### -4- ਟੂਲ ਕਾਲ ਨੂੰ ਸੰਭਾਲਣਾ

ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਦੂਜਾ ਰਿਕਵੈਸਟ ਹੈਂਡਲਰ ਸੈੱਟਅਪ ਕਰਨਾ ਪਵੇਗਾ, ਜੋ ਕਿ ਇਹ ਜਾਣਦਾ ਹੋਵੇ ਕਿ ਕਿਹੜਾ ਫੀਚਰ ਕਾਲ ਕਰਨਾ ਹੈ ਅਤੇ ਕਿਸ ਆਰਗੁਮੈਂਟ ਨਾਲ।

**Python**

ਆਓ ਡੈਕੋਰੇਟਰ `@server.call_tool` ਵਰਤਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ `handle_call_tool` ਨਾਲ ਅਮਲ ਕਰੀਏ। ਇਸ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਸਾਨੂੰ ਟੂਲ ਦਾ ਨਾਮ, ਇਸਦਾ ਆਰਗੁਮੈਂਟ ਪਾਰਸ ਕਰਨਾ ਹੈ ਅਤੇ ਇਹ ਸੁਨਿਸ਼ਚਿਤ ਕਰਨਾ ਹੈ ਕਿ ਆਰਗੁਮੈਂਟ ਟੂਲ ਲਈ ਵੈਧ ਹਨ। ਅਸੀਂ ਇਹ ਜਾਂ ਤਾਂ ਇੱਥੇ ਹੀ ਕਰ ਸਕਦੇ ਹਾਂ ਜਾਂ ਅਸਲ ਟੂਲ ਵਿੱਚ ਅੱਗੇ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਟੂਲਾਂ ਦੇ ਨਾਮ ਕੀਜ਼ ਵਜੋਂ ਹਨ
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

ਇੱਥੇ ਕੀ ਹੁੰਦਾ ਹੈ:

- ਸਾਡਾ ਟੂਲ ਨਾਮ ਪਹਿਲਾਂ ਹੀ `name` ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਵਜੋਂ ਮੌਜੂਦ ਹੈ, ਅਤੇ ਸਾਡੇ ਆਰਗੁਮੈਂਟ `arguments` ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਹਨ।

- ਟੂਲ ਨੂੰ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਆਰਗੁਮੈਂਟ ਦੀ ਵੈਧਤਾ `handler` ਗੁਣ ਵਿੱਚ ਹੁੰਦੀ ਹੈ ਜੋ ਇੱਕ ਫੰਕਸ਼ਨ ਵੱਲ ਵਿੱਖਰਾ ਹੈ, ਜੇ ਇਹ ਫੇਲ ਹੁੰਦਾ ਹੈ ਤਾਂ ਇਹ ਇਕ ਸਨਮੀਤੀ ਉੱਠਾਏਗਾ। 

ਹੁਣ ਸਾਡੇ ਕੋਲ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਨਾਲ ਟੂਲਜ਼ ਦੀ ਲਿਸਟਿੰਗ ਅਤੇ ਕਾਲਿੰਗ ਦੀ ਪੂਰੀ ਸਮਝ ਹੈ।

ਇਸਦੀ [ਪੂਰੀ ਉਦਾਹਰਣ](./code/README.md) ਦੇਖੋ ਇੱਥੇ

## ਅਸਾਈਨਮੈਂਟ

ਤੁਹਾਨੂੰ ਦਿੱਤਾ ਗਿਆ ਕੋਡ ਵਿੱਚ ਕਈ ਟੂਲਜ਼, ਰਿਸੋਰਸਜ਼ ਅਤੇ ਪ੍ਰੋਂਪਟ ਸ਼ਾਮਲ ਕਰੋ ਅਤੇ ਵੇਖੋ ਕਿ ਤੁਸੀਂ ਸਿਰਫ਼ ਟੂਲਜ਼ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਫਾਈਲਾਂ ਜੋੜਨ ਦੀ ਲੋੜ ਕਿਵੇਂ ਮਹਿਸੂਸ ਕਰਦੇ ਹੋ ਅਤੇ ਹੋਰ ਕਿਤੇ ਨਹੀਂ।

*ਕੋਈ ਸਮਾਧਾਨ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ*

## ਸੰਖੇਪ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਿਆ ਕਿ ਲੋਅ-ਲੇਵਲ ਸਰਵਰ ਤਰੀਕਾ ਕਿਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਇਹ ਸਾਨੂੰ ਇੱਕ ਵਧੀਆ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣ ਵਿੱਚ ਕਿਵੇਂ ਮਦਦ ਕਰਦਾ ਹੈ ਜਿਸ ਤੇ ਅਸੀਂ ਅੱਗੇ ਵਧ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਵੈਰੀਫਿਕੇਸ਼ਨ ਤੇ ਵੀ ਵਿਚਾਰ ਕੀਤਾ ਅਤੇ ਤੁਹਾਨੂੰ ਵਿਖਾਇਆ ਗਿਆ ਕਿ ਕਿਵੇਂ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਾਇਬ੍ਰੇਰੀਆਂ ਜਿਵੇਂ Pydantic ਅਤੇ Zod ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁਟ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ ਸਕੀਮਾ ਬਣਾਉਣੇ।

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [ਸਰਲ ਪ੍ਰਮਾਣੀਕਰਨ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਪ੍ਰਯਾਸ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸੂਚਿਤ ਜਾਣਕਾਰੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਵેદਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫ਼ਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਵਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
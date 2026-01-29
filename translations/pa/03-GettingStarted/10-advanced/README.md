# ਉੱਚ-ਸਤ੍ਹਾ ਸਰਵਰ ਦੀ ਵਰਤੋਂ

MCP SDK ਵਿੱਚ ਦੋ ਤਰ੍ਹਾਂ ਦੇ ਸਰਵਰ ਹਨ: ਆਮ ਸਰਵਰ ਅਤੇ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ। ਆਮ ਤੌਰ 'ਤੇ, ਤੁਸੀਂ ਆਮ ਸਰਵਰ ਨੂੰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹੋ। ਪਰ ਕੁਝ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ 'ਤੇ ਨਿਰਭਰ ਕਰਨਾ ਪਵੇਗਾ, ਜਿਵੇਂ:

- ਬਿਹਤਰ ਆਰਕੀਟੈਕਚਰ। ਆਮ ਸਰਵਰ ਅਤੇ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਦੋਵਾਂ ਨਾਲ ਸਾਫ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣਾ ਸੰਭਵ ਹੈ, ਪਰ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਨਾਲ ਇਹ ਥੋੜਾ ਆਸਾਨ ਹੋ ਸਕਦਾ ਹੈ।
- ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਉਪਲਬਧਤਾ। ਕੁਝ ਉੱਚ-ਸਤ੍ਹਾ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸਿਰਫ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਨਾਲ ਹੀ ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਤੁਸੀਂ ਇਸ ਬਾਰੇ ਅਗਲੇ ਅਧਿਆਇ ਵਿੱਚ ਦੇਖੋਗੇ ਜਦੋਂ ਅਸੀਂ ਸੈਂਪਲਿੰਗ ਅਤੇ ਇਲਿਸਿਟੇਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ।

## ਆਮ ਸਰਵਰ ਵਿਰੁੱਧ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ

ਇਹ ਹੈ ਕਿ MCP Server ਨੂੰ ਆਮ ਸਰਵਰ ਨਾਲ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ:

**Python**

```python
mcp = FastMCP("Demo")

# Add an addition tool
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

// Add an addition tool
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

ਇਸ ਵਿੱਚ ਗੱਲ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਹਰ ਟੂਲ, ਰਿਸੋਰਸ ਜਾਂ ਪ੍ਰੋਮਪਟ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦੇ ਹੋ ਜੋ ਤੁਸੀਂ ਸਰਵਰ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਵਿੱਚ ਕੋਈ ਗਲਤ ਨਹੀਂ ਹੈ।

### ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਪਹੁੰਚ

ਹਾਲਾਂਕਿ, ਜਦੋਂ ਤੁਸੀਂ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਪਹੁੰਚ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਵੱਖਰੇ ਤਰੀਕੇ ਨਾਲ ਸੋਚਣਾ ਪਵੇਗਾ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਹਰ ਟੂਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਹਰ ਵਿਸ਼ੇਸ਼ਤਾ ਪ੍ਰਕਾਰ (ਟੂਲ, ਰਿਸੋਰਸ ਜਾਂ ਪ੍ਰੋਮਪਟ) ਲਈ ਦੋ ਹੈਂਡਲਰ ਬਣਾਉਂਦੇ ਹੋ। ਉਦਾਹਰਨ ਲਈ, ਟੂਲਾਂ ਲਈ ਸਿਰਫ ਦੋ ਫੰਕਸ਼ਨ ਹੁੰਦੇ ਹਨ:

- ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ। ਇੱਕ ਫੰਕਸ਼ਨ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਦੇ ਯਤਨ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੁੰਦਾ ਹੈ।
- ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦਾ ਹੈਂਡਲ। ਇੱਥੇ ਵੀ, ਸਿਰਫ ਇੱਕ ਫੰਕਸ਼ਨ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੇ ਯਤਨ ਨੂੰ ਹੈਂਡਲ ਕਰਦਾ ਹੈ।

ਇਹ ਸੁਣਨ ਵਿੱਚ ਘੱਟ ਕੰਮ ਜਾਪਦਾ ਹੈ, ਹੈ ਨਾ? ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਟੂਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਮੈਨੂੰ ਸਿਰਫ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਟੂਲ ਸੂਚੀ ਵਿੱਚ ਹੈ ਜਦੋਂ ਮੈਂ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਂਦਾ ਹਾਂ ਅਤੇ ਇਹ ਕਾਲ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਆਉਂਦੀ ਹੈ।

ਆਓ ਹੁਣ ਕੋਡ ਦੇਖੀਏ ਕਿ ਇਹ ਕਿਵੇਂ ਦਿਖਦਾ ਹੈ:

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
                    "a": {"type": "number", "description": "nubmer to add"}, 
                    "b": {"type": "number", "description": "nubmer to add"}
                },
                "required": ["query"],
            },
        )
    ]
```

**TypeScript**

```typescript
server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: [{
        name="add",
        description="Add two numbers",
        inputSchema={
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "nubmer to add"}, 
                "b": {"type": "number", "description": "nubmer to add"}
            },
            "required": ["query"],
        }
    }]
  };
});
```

ਇੱਥੇ ਹੁਣ ਸਾਡੇ ਕੋਲ ਇੱਕ ਫੰਕਸ਼ਨ ਹੈ ਜੋ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰਦਾ ਹੈ। ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਵਿੱਚ ਹੁਣ `name`, `description` ਅਤੇ `inputSchema` ਵਰਗੇ ਫੀਲਡ ਹਨ ਜੋ ਵਾਪਸੀ ਦੇ ਪ੍ਰਕਾਰ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ। ਇਸ ਨਾਲ ਸਾਨੂੰ ਆਪਣੇ ਟੂਲਾਂ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾ ਦੀ ਪਰਿਭਾਸ਼ਾ ਕਿਤੇ ਹੋਰ ਰੱਖਣ ਦੀ ਸਹੂਲਤ ਮਿਲਦੀ ਹੈ। ਹੁਣ ਅਸੀਂ ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਇੱਕ ਟੂਲ ਫੋਲਡਰ ਵਿੱਚ ਬਣਾਉਣ ਦੇ ਯੋਗ ਹਾਂ ਅਤੇ ਇਹੀ ਗੱਲ ਤੁਹਾਡੇ ਸਾਰੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਈ ਵੀ ਹੈ। ਇਸ ਤਰ੍ਹਾਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਇਸ ਤਰ੍ਹਾਂ ਸੰਗਠਿਤ ਹੋ ਸਕਦਾ ਹੈ:

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

ਇਹ ਵਧੀਆ ਹੈ, ਸਾਡਾ ਆਰਕੀਟੈਕਚਰ ਕਾਫ਼ੀ ਸਾਫ਼ ਦਿਖ ਸਕਦਾ ਹੈ।

ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਬਾਰੇ ਕੀ? ਕੀ ਇਹ ਵੀ ਉਹੀ ਵਿਚਾਰ ਹੈ, ਇੱਕ ਹੈਂਡਲਰ ਜੋ ਕਿਸੇ ਵੀ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੇ? ਹਾਂ, ਬਿਲਕੁਲ, ਇਸ ਲਈ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
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
    // TODO call the tool, 

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ਜਿਵੇਂ ਤੁਸੀਂ ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਦੇਖ ਸਕਦੇ ਹੋ, ਸਾਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਟੂਲ ਅਤੇ ਕਿਹੜੇ ਆਰਗੂਮੈਂਟ ਦੀ ਲੋੜ ਹੈ, ਇਹ ਪਾਰਸ ਕਰਨਾ ਪਵੇਗਾ, ਅਤੇ ਫਿਰ ਸਾਨੂੰ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਣੀ ਪਵੇਗੀ।

## ਪਹੁੰਚ ਵਿੱਚ ਸੁਧਾਰ: ਵੈਲੀਡੇਸ਼ਨ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਟੂਲ, ਰਿਸੋਰਸ ਅਤੇ ਪ੍ਰੋਮਪਟ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਸਾਰੇ ਰਜਿਸਟਰੇਸ਼ਨ ਨੂੰ ਹਰ ਵਿਸ਼ੇਸ਼ਤਾ ਪ੍ਰਕਾਰ ਲਈ ਦੋ ਹੈਂਡਲਰ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਹੁਣ ਅਸੀਂ ਕੀ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ? ਖੈਰ, ਸਾਨੂੰ ਕੁਝ ਤਰ੍ਹਾਂ ਦੀ ਵੈਲੀਡੇਸ਼ਨ ਸ਼ਾਮਲ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਟੂਲ ਸਹੀ ਆਰਗੂਮੈਂਟ ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਹਰ ਰਨਟਾਈਮ ਦਾ ਇਸ ਲਈ ਆਪਣਾ ਹੱਲ ਹੁੰਦਾ ਹੈ, ਉਦਾਹਰਨ ਲਈ Python Pydantic ਵਰਤਦਾ ਹੈ ਅਤੇ TypeScript Zod ਵਰਤਦਾ ਹੈ। ਵਿਚਾਰ ਇਹ ਹੈ ਕਿ ਅਸੀਂ ਇਹ ਕਰਦੇ ਹਾਂ:

- ਵਿਸ਼ੇਸ਼ਤਾ (ਟੂਲ, ਰਿਸੋਰਸ ਜਾਂ ਪ੍ਰੋਮਪਟ) ਬਣਾਉਣ ਦੀ ਲਾਜ਼ਮੀ ਲਾਜ਼ਿਕ ਨੂੰ ਇਸਦੇ ਸਮਰਪਿਤ ਫੋਲਡਰ ਵਿੱਚ ਲਿਜਾਇਆ ਜਾਵੇ।
- ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ ਵੈਲੀਡੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਉਦਾਹਰਨ ਲਈ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰਦੀ ਹੈ।

### ਵਿਸ਼ੇਸ਼ਤਾ ਬਣਾਉਣਾ

ਵਿਸ਼ੇਸ਼ਤਾ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਉਸ ਵਿਸ਼ੇਸ਼ਤਾ ਲਈ ਇੱਕ ਫਾਈਲ ਬਣਾਉਣੀ ਪਵੇਗੀ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਵੇਗਾ ਕਿ ਉਸ ਵਿਸ਼ੇਸ਼ਤਾ ਦੇ ਲਾਜ਼ਮੀ ਫੀਲਡ ਹਨ। ਇਹ ਫੀਲਡ ਟੂਲ, ਰਿਸੋਰਸ ਅਤੇ ਪ੍ਰੋਮਪਟ ਵਿੱਚ ਥੋੜੇ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ।

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
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਅਸੀਂ ਇਹ ਕਰਦੇ ਹਾਂ:

- Pydantic `AddInputModel` ਦੀ ਵਰਤੋਂ ਕਰਕੇ *schema.py* ਫਾਈਲ ਵਿੱਚ `a` ਅਤੇ `b` ਫੀਲਡ ਨਾਲ ਇੱਕ ਸਕੀਮਾ ਬਣਾਉਣਾ।
- ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ `AddInputModel` ਦੇ ਪ੍ਰਕਾਰ ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨਾ। ਜੇ ਪੈਰਾਮੀਟਰ ਵਿੱਚ ਮਿਸਮੈਚ ਹੋਵੇ ਤਾਂ ਇਹ ਕਰੈਸ਼ ਕਰੇਗਾ:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ ਕਿ ਇਹ ਪਾਰਸਿੰਗ ਲਾਜ਼ਿਕ ਟੂਲ ਕਾਲ ਵਿੱਚ ਰੱਖਣੀ ਹੈ ਜਾਂ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਵਿੱਚ।

**TypeScript**

```typescript
// server.ts
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

// schema.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// add.ts
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

- ਟੂਲ ਕਾਲਾਂ ਨਾਲ ਨਜਿੱਠਣ ਵਾਲੇ ਹੈਂਡਲਰ ਵਿੱਚ, ਅਸੀਂ ਹੁਣ ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ ਟੂਲ ਦੇ ਪਰਿਭਾਸ਼ਿਤ ਸਕੀਮਾ ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ਜੇ ਇਹ ਕੰਮ ਕਰਦਾ ਹੈ ਤਾਂ ਅਸੀਂ ਅਸਲ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਰੱਖਦੇ ਹਾਂ:

    ```typescript
    const result = await tool.callback(input);
    ```

ਜਿਵੇਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ, ਇਹ ਪਹੁੰਚ ਇੱਕ ਵਧੀਆ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਂਦੀ ਹੈ ਕਿਉਂਕਿ ਹਰ ਚੀਜ਼ ਦਾ ਆਪਣਾ ਸਥਾਨ ਹੁੰਦਾ ਹੈ। *server.ts* ਇੱਕ ਬਹੁਤ ਹੀ ਛੋਟੀ ਫਾਈਲ ਹੈ ਜੋ ਸਿਰਫ ਬੇਨਤੀ ਹੈਂਡਲਰ ਨੂੰ ਵਾਇਰ ਕਰਦੀ ਹੈ ਅਤੇ ਹਰ ਵਿਸ਼ੇਸ਼ਤਾ ਆਪਣੇ ਸਬੰਧਤ ਫੋਲਡਰ ਵਿੱਚ ਹੈ ਜਿਵੇਂ tools/, resources/ ਜਾਂ /prompts।

ਵਧੀਆ, ਆਓ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਇਸ ਨੂੰ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ।

## ਅਭਿਆਸ: ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਕਰਾਂਗੇ:

1. ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਵਾਲੇ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਬਣਾਉਣਾ।
1. ਇੱਕ ਆਰਕੀਟੈਕਚਰ ਲਾਗੂ ਕਰਨਾ ਜਿਸ 'ਤੇ ਤੁਸੀਂ ਬਣਾਉਣ ਕਰ ਸਕਦੇ ਹੋ।
1. ਵੈਲੀਡੇਸ਼ਨ ਸ਼ਾਮਲ ਕਰਨਾ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਟੂਲ ਕਾਲਾਂ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਵੈਲੀਡੇਟ ਕੀਤੀਆਂ ਜਾ ਸਕਣ।

### -1- ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਸਾਨੂੰ ਇੱਕ ਆਰਕੀਟੈਕਚਰ ਦਾ ਪਤਾ ਲਗਾਉਣਾ ਹੈ ਜੋ ਸਾਨੂੰ ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸ਼ਾਮਲ ਕਰਨ ਦੇ ਨਾਲ ਸਕੇਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

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

ਹੁਣ ਸਾਡੇ ਕੋਲ ਇੱਕ ਆਰਕੀਟੈਕਚਰ ਹੈ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਅਸੀਂ ਟੂਲ ਫੋਲਡਰ ਵਿੱਚ ਨਵੇਂ ਟੂਲ ਆਸਾਨੀ ਨਾਲ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਰਿਸੋਰਸ ਅਤੇ ਪ੍ਰੋਮਪਟ ਲਈ ਸਬਡਾਇਰੈਕਟਰੀ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਇਸ ਨੂੰ ਅਨੁਸਰਣ ਕਰਨ ਲਈ ਸੁਤੰਤਰ ਰਹੋ।

### -2- ਟੂਲ ਬਣਾਉਣਾ

ਆਓ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਟੂਲ ਬਣਾਉਣ ਦੇਖੀਏ। ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਇਸਨੂੰ ਇਸਦੇ *tool* ਸਬਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇਸ ਤਰ੍ਹਾਂ ਬਣਾਉਣਾ ਪਵੇਗਾ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: add Pydantic, so we can create an AddInputModel and validate args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਅਸੀਂ ਵੇਖਦੇ ਹਾਂ ਕਿ ਅਸੀਂ name, description, Pydantic ਦੀ ਵਰਤੋਂ ਕਰਕੇ input schema ਅਤੇ ਇੱਕ ਹੈਂਡਲਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ ਜੋ ਇਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ 'ਤੇ ਚਲਾਇਆ ਜਾਵੇਗਾ। ਆਖਿਰਕਾਰ, ਅਸੀਂ `tool_add` ਨੂੰ expose ਕਰਦੇ ਹਾਂ ਜੋ ਇਹ ਸਾਰੇ ਗੁਣਾਂ ਰੱਖਦਾ ਹੈ।

ਇਸਦੇ ਨਾਲ *schema.py* ਵੀ ਹੈ ਜੋ ਸਾਡੇ ਟੂਲ ਦੁਆਰਾ ਵਰਤੇ ਜਾਣ ਵਾਲੇ input schema ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ਸਾਨੂੰ *__init__.py* ਨੂੰ ਵੀ ਪੂਰਾ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਟੂਲ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਮੌਡਿਊਲ ਵਜੋਂ ਮੰਨਿਆ ਜਾਵੇ। ਇਸਦੇ ਨਾਲ, ਸਾਨੂੰ ਇਸ ਵਿੱਚ ਮੌਜੂਦ ਮੌਡਿਊਲਾਂ ਨੂੰ expose ਕਰਨਾ ਪਵੇਗਾ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ਜਦੋਂ ਅਸੀਂ ਹੋਰ ਟੂਲ ਸ਼ਾਮਲ ਕਰਦੇ ਹਾਂ, ਤਾਂ ਅਸੀਂ ਇਸ ਫਾਈਲ ਵਿੱਚ ਹੋਰ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹਾਂ।

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

ਇੱਥੇ ਅਸੀਂ ਗੁਣਾਂ ਦੀ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਬਣਾਉਂਦੇ ਹਾਂ:

- name, ਇਹ ਟੂਲ ਦਾ ਨਾਮ ਹੈ।
- rawSchema, ਇਹ Zod schema ਹੈ, ਇਹ ਆਉਣ ਵਾਲੀ ਬੇਨਤੀ ਨੂੰ ਵੈਲੀਡੇਟ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ।
- inputSchema, ਇਹ schema ਹੈ ਜੋ ਹੈਂਡਲਰ ਦੁਆਰਾ ਵਰਤੀ ਜਾਵੇਗੀ।
- callback, ਇਹ ਟੂਲ ਨੂੰ invoke ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ।

ਇਸਦੇ ਨਾਲ `Tool` ਹੈ ਜੋ ਇਸ ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਇੱਕ ਪ੍ਰਕਾਰ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜਿਸਨੂੰ mcp server ਹੈਂਡਲਰ ਸਵੀਕਾਰ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ਇਸਦੇ ਨਾਲ *schema.ts* ਹੈ ਜਿੱਥੇ ਅਸੀਂ ਹਰ ਟੂਲ ਲਈ input schemas ਸਟੋਰ ਕਰਦੇ ਹਾਂ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇਸ ਸਮੇਂ ਸਿਰਫ ਇੱਕ schema ਹੈ ਪਰ ਜਿਵੇਂ ਅਸੀਂ ਹੋਰ ਟੂਲ ਸ਼ਾਮਲ ਕਰਦੇ ਹਾਂ, ਅਸੀਂ ਹੋਰ ਐਂਟਰੀ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹਾਂ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ਵਧੀਆ, ਆਓ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਸਾਡੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਨੂੰ ਹੈਂਡਲ ਕਰੀਏ।

### -3- ਟੂਲ ਸੂਚੀ ਬਣਾਉਣ ਨੂੰ ਹੈਂਡਲ ਕਰਨਾ

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਸਾਡੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਇਸ ਲਈ ਇੱਕ ਬੇਨਤੀ ਹੈਂਡਲਰ ਸੈਟਅਪ ਕਰਨਾ ਪਵੇਗਾ। ਇਹ ਹੈ ਜੋ ਸਾਨੂੰ ਆਪਣੇ ਸਰਵਰ ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਪਵੇਗਾ:

**Python**

```python
# code omitted for brevity
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

ਇੱਥੇ ਅਸੀਂ `@server.list_tools` ਡੈਕੋਰੇਟਰ ਸ਼ਾਮਲ ਕਰਦੇ ਹਾਂ ਅਤੇ `handle_list_tools` ਫੰਕਸ਼ਨ ਲਾਗੂ ਕਰਦੇ ਹਾਂ। ਇਸ ਵਿੱਚ, ਸਾਨੂੰ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਪੈਦਾ ਕਰਨੀ ਪਵੇਗੀ। ਧਿਆਨ ਦਿਓ ਕਿ ਹਰ ਟੂਲ ਵਿੱਚ name, description ਅਤੇ inputSchema ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

**TypeScript**

ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਲਈ ਬੇਨਤੀ ਹੈਂਡਲਰ ਸੈਟਅਪ ਕਰਨ ਲਈ, ਸਾਨੂੰ `setRequestHandler` ਨੂੰ schema ਨਾਲ ਕਾਲ ਕਰਨਾ ਪਵੇਗਾ ਜੋ ਅਸੀਂ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ, ਇਸ ਮਾਮਲੇ ਵਿੱਚ `ListToolsRequestSchema`।

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
// code omitted for brevity
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Return the list of registered tools
  return {
    tools: tools
  };
});
```

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਦਾ ਹੱਲ ਕਰ ਲਿਆ ਹੈ। ਆਓ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੇਖੀਏ।

### -4- ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਨੂੰ ਹੈਂਡਲ ਕਰਨਾ

ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਇੱਕ ਹੋਰ ਬੇਨਤੀ ਹੈਂਡਲਰ ਸੈਟਅਪ ਕਰਨਾ ਪਵੇਗਾ, ਇਸ ਵਾਰ ਇਸ ਬੇਨਤੀ ਨਾਲ ਨਜਿੱਠਣ ਲਈ ਜੋ ਦੱਸਦੀ ਹੈ ਕਿ ਕਿਹੜੀ ਵਿਸ਼ੇਸ਼ਤਾ ਕਾਲ ਕਰਨੀ ਹੈ ਅਤੇ ਕਿਹੜੇ ਆਰਗੂਮੈਂਟ ਨਾਲ।

**Python**

ਆਓ `@server.call_tool` ਡੈਕੋਰੇਟਰ ਵਰਤਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ `handle_call_tool` ਫੰਕਸ਼ਨ ਨਾਲ ਲਾਗੂ ਕਰਦੇ ਹਾਂ। ਇਸ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਸਾਨੂੰ ਟੂਲ ਦਾ ਨਾਮ, ਇਸਦੇ ਆਰਗੂਮੈਂਟ ਨੂੰ ਪਾਰਸ ਕਰਨਾ ਪਵੇਗਾ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਵੇਗਾ ਕਿ ਆਰਗੂਮੈਂਟ ਸਹੀ ਹਨ। ਅਸੀਂ ਇਹ ਵੈਲੀਡੇਸ਼ਨ ਇਸ ਫੰਕਸ਼ਨ ਵਿੱਚ ਜਾਂ ਟੂਲ ਵਿੱਚ ਕਰ ਸਕਦੇ ਹਾਂ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is a dictionary with tool names as keys
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # invoke the tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ਇੱਥੇ ਕੀ ਹੁੰਦਾ ਹੈ:

- ਸਾਡੇ ਟੂਲ ਦਾ ਨਾਮ ਪਹਿਲਾਂ ਹੀ input ਪੈਰਾਮੀਟਰ `name` ਦੇ ਰੂਪ ਵਿੱਚ ਮੌਜੂਦ ਹੈ, ਜੋ ਸਾਡੇ arguments dictionary ਲਈ ਸੱਚ ਹੈ।

- ਟੂਲ ਨੂੰ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। arguments ਦੀ ਵੈਲੀਡੇਸ਼ਨ `handler` ਗੁਣ ਵਿੱਚ ਹੁੰਦੀ ਹੈ ਜੋ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਪੋਇੰਟ ਕਰਦਾ ਹੈ। ਜੇ ਇਹ ਫੇਲ ਹੁੰਦਾ ਹੈ ਤਾਂ ਇਹ exception ਉਠਾਏਗਾ।

ਇੱਥੇ, ਹੁਣ ਸਾਨੂੰ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਅਤੇ ਕਾਲ ਕਰਨ ਦੀ ਪੂਰੀ ਸਮਝ ਹੈ।

[ਪੂਰਾ ਉਦਾਹਰਨ](./code/README.md) ਇੱਥੇ ਵੇਖੋ

## ਅਸਾਈਨਮੈਂਟ

ਤੁਹਾਨੂੰ ਦਿੱਤੇ ਗਏ ਕੋਡ ਨੂੰ ਕਈ ਟੂਲਾਂ, ਰਿਸੋਰਸ ਅਤੇ ਪ੍ਰੋਮਪਟ ਨਾਲ ਵਧਾਓ ਅਤੇ ਇਸ ਬਾਰੇ ਵਿਚਾਰ ਕਰੋ ਕਿ ਤੁਸੀਂ ਸਿਰਫ ਟੂਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਲੋੜ ਮਹਿਸੂ ਕਰਦੇ ਹੋ ਅਤੇ ਕਿਤੇ ਹੋਰ ਨਹੀਂ।

*ਕੋਈ ਹੱਲ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ*

## ਸਾਰ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਿਆ ਕਿ ਨੀਵੀਂ-ਸਤ੍ਹਾ ਸਰਵਰ ਪਹੁੰਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ ਅਤੇ ਇਹ ਸਾਨੂੰ ਇੱਕ ਵਧੀਆ ਆਰਕੀਟੈਕਚਰ ਬਣਾਉਣ ਵਿੱਚ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ ਜਿਸ 'ਤੇ ਅਸੀਂ ਬਣਾਉਣ ਕਰ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਵੈਲੀਡੇਸ਼ਨ ਬਾਰੇ ਵੀ ਚ

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
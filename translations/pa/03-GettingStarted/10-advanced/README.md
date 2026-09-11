# ਉੱਨਤ ਸਰਵਰ ਉਪਯੋਗ

MCP SDK ਵਿੱਚ ਦੋ ਵੱਖ-ਵੱਖ ਕਿਸਮ ਦੇ ਸਰਵਰ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਗਏ ਹਨ, ਤੁਹਾਡਾ ਸਧਾਰਣ ਸਰਵਰ ਅਤੇ ਲੋ-ਲੈਵਲ ਸਰਵਰ। ਆਮ ਤੌਰ 'ਤੇ, ਤੁਸੀਂ ਆਮ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਫੀਚਰ ਸ਼ਾਮਿਲ ਕਰਨ ਲਈ ਕਰਦੇ ਹੋ। ਪਰ ਕੁਝ ਹਾਲਤਾਂ ਵਿੱਚ, ਤੁਸੀਂ ਲੋ-ਲੈਵਲ ਸਰਵਰ 'ਤੇ ਨਿਰਭਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜਿਵੇਂ:

- ਬਿਹਤਰ ਸੰਰਚਨਾ। ਸਾਫ਼ ਸੰਰਚਨਾ ਬਣਾਉਣਾ ਸੰਭਵ ਹੈ ਦੋਹਾਂ ਆਮ ਸਰਵਰ ਅਤੇ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਨਾਲ ਪਰ ਇਹ ਕਿਹਾ ਜਾ ਸਕਦਾ ਹੈ ਕਿ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਨਾਲ ਇਹ ਥੋੜ੍ਹਾ ਅਸਾਨ ਹੁੰਦਾ ਹੈ।
- ਫੀਚਰ ਉਪਲਬਧਤਾ। ਕੁਝ ਉੱਨਤ ਫੀਚਰ ਸਿਰਫ਼ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਨਾਲ ਹੀ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।
    ਬਾਅਦ ਦੇ ਅਧਿਆਇ ਵਿੱਚ Elicitation ਅਤੇ ਲੇਗੇਸੀ Sampling
    ਫੀਚਰ ਲੱਭੇ ਜਾਣਗੇ, ਜੋ MCP `2026-07-28` ਵਿੱਚ ਡੀਪ੍ਰੀਕੇਟ ਕੀਤਾ ਗਿਆ ਹੈ।

## ਆਮ ਸਰਵਰ ਵਿਰੁੱਧ ਲੋ-ਲੈਵਲ ਸਰਵਰ

ਆਮ ਸਰਵਰ ਨਾਲ MCP ਸਰਵਰ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ

**Python**

```python
mcp = FastMCP("Demo")

# ਇੱਕ ਜੋੜ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
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

// ਇੱਕ ਜੋੜਣ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
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

ਮਕਸਦ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਜੋ ਕੋਈ ਵੀ ਟੂਲ, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ ਸਰਵਰ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਉਹ ਜੁਆਰਾ ਦਿਓ। ਇਸ ਵਿੱਚ ਕੋਈ ਗੜਬੜ ਨਹੀਂ।  

### ਲੋ-ਲੈਵਲ ਸਰਵਰ ਪਹੁੰਚ

ਪਰ ਜਦੋਂ ਤੁਸੀਂ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਪਹੁੰਚ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਇਸ ਬਾਰੇ ਵੱਖਰੇ ਤਰੀਕੇ ਨਾਲ ਸੋਚਣਾ ਪੈਂਦਾ ਹੈ। ਹਰ ਟੂਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਹਰ ਫੀਚਰ ਕਿਸਮ (ਟੂਲ, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ) ਲਈ ਦੋ ਹੈਂਡਲਰ ਬਨਾਉਂਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ ਟੂਲ ਲਈ ਸਿਰਫ਼ ਦੋ ਫੰਕਸ਼ਨ ਹਨ:

- ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਲਿਸਟ ਬਣਾਉਣਾ। ਇੱਕ ਫੰਕਸ਼ਨ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਲਿਸਟ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ਾਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ।
- ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਨੂੰ ਸੰਭਾਲਣਾ। ਇੱਥੇ ਵੀ, ਸਿਰਫ਼ ਇੱਕ ਫੰਕਸ਼ਨ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ।

ਇਹ ਕੰਮ ਘਟੋ ਘੱਟ ਲੱਗਦਾ ਹੈ, ਨਾ? ਇਸ ਲਈ ਟੂਲ ਰਜਿਸਟਰ ਕਰਨ ਦੀ ਬਜਾਏ, ਮੈਨੂੰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਜਦੋਂ ਮੈਂ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਲਿਸਟ ਕਰਾਂ ਤਾਂ ਇਹ ਟੂਲ ਲਿਸਟ ਵਿੱਚ ਹੋਵੇ ਅਤੇ ਜਦੋਂ ਟੂਲ ਕਾਲ ਕੀਤੇ ਜਾਣ ਦੀ ਬੇਨਤੀ ਆਉਂਦੀ ਹੈ ਤਾਂ ਇਸਨੂੰ ਕਾਲ ਕੀਤਾ ਜਾਵੇ। 

ਆਓ ਵੇਖੀਏ ਹੁਣ ਕੋਡ ਕਿਵੇਂ ਦਿਖਾਈ ਦੇਂਦਾ ਹੈ:

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
  // ਦਰਜ ਕੀਤੇ ਗਏ ਸਾਜ਼ੋ-ਸਾਮਾਨ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
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

ਹੁਣ ਸਾਡੇ ਕੋਲ ਇਕ ਫੰਕਸ਼ਨ ਹੈ ਜੋ ਫੀਚਰਾਂ ਦੀ ਲਿਸਟ ਰਿਟਰਨ ਕਰਦਾ ਹੈ। ਟੂਲਾਂ ਦੀ ਲਿਸਟ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਵਿੱਚ ਹੁਣ `name`, `description` ਅਤੇ `inputSchema` ਵਰਗੇ ਖੇਤਰ ਹਨ ਜੋ ਰਿਟਰਨ ਟਾਈਪ ਦੇ ਅਨੁਕੂਲ ਹਨ। ਇਹ ਸਾਡੇ ਟੂਲਾਂ ਅਤੇ ਫੀਚਰ ਪਰਿਭਾਸ਼ਾ ਨੂੰ ਹੋਰ ਜਗ੍ਹਾ ਬਣਾਉਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। ਸਾਨੂੰ ਹੁਣ ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਇੱਕ ਟੂਲ ਫੋਲਡਰ ਵਿੱਚ ਬਣਾਉਣ ਦੀ ਸੁਵਿਧਾ ਹੈ ਅਤੇ ਸਾਰੇ ਫੀਚਰਾਂ ਲਈ ਵੀ, ਤਾਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਅਚਾਨਕ ਇਸ ਤਰ੍ਹਾਂ ਸੰਵੱਧਿਤ ਹੋ ਸਕਦਾ ਹੈ:

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

ਇਹ ਵਧੀਆ ਹੈ, ਸਾਡੀ ਸੰਰਚਨਾ ਕਾਫ਼ੀ ਸਾਫ਼ ਸੁਥਰੀ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ।

ਟੂਲ ਕਾਲ ਕਰਨ ਬਾਰੇ ਕੀ, ਕੀ ਇਹ ਓਹੀ ਵਿਚਾਰ ਹੈ, ਇੱਕ ਹੈਂਡਲਰ ਜੋ ਕਿਸੇ ਵੀ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੇ? ਹਾਂ, ਬਿਲਕੁਲ, ਇਹ ਰਿਹਾ ਉਸਦਾ ਕੋਡ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇੱਕ ਸ਼ਬਦਕੋਸ਼ ਹੈ ਜਿਸ ਵਿੱਚ ਟੂਲ ਨਾਂ ਕੁੰਜੀਆਂ ਵਜੋਂ ਹਨ
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
    // TODO ਸੰਦ ਨੂੰ ਕਾਲ ਕਰੋ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ਉੱਪਰ ਦਿੱਤੇ ਕੋਡ ਤੋਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਸਾਨੂੰ ਕਾਲ ਕਰਨ ਵਾਲਾ ਟੂਲ ਅਤੇ ਉਸਦੇ ਆਗਮਨ ਦਲੀਲਾਂ ਨੂੰ ਪਾਰਸ ਕਰਨਾ ਪੈਂਦਾ ਹੈ, ਫਿਰ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨਾ ਹੁੰਦਾ ਹੈ।

## ਜਾਂਚ ਨਾਲ ਤਰੀਕੇ ਵਿੱਚ ਸੁਧਾਰ

ਇੱਥੇ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਕਿਵੇਂ ਤੁਸੀਂ ਟੂਲ, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਸ਼ਾਮਿਲ ਕਰਨ ਲਈ ਦਿੱਤੇ ਗਏ ਸਾਰੇ ਰਜਿਸਟਰੇਸ਼ਨ ਦੋ ਹੈਂਡਲਰਾਂ ਨਾਲ ਬਦਲ ਸਕਦੇ ਹੋ। ਹੁਣ ਹੋਰ ਕੀ ਕਰਨ ਦੀ ਲੋੜ ਹੈ? ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ ਅਸੀਂ ਕਿਸੇ ਤਰ੍ਹਾਂ ਦੀ ਜਾਂਚ ਸ਼ਾਮਿਲ ਕਰੀਏ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਟੂਲ ਨੂੰ ਸਹੀ ਦਲੀਲਾਂ ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ। ਹਰ ਰਨਟਾਈਮ ਦਾ ਇਸ ਲਈ ਆਪਣਾ ਹੱਲ ਹੈ, ਉਦਾਹਰਨ ਵਜੋਂ Python 'ਚ Pydantic ਅਤੇ TypeScript 'ਚ Zod ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਸੋਚ ਇਹ ਹੈ ਕਿ ਅਸੀਂ ਹੇਠ ਲਿਖਿਆ ਕਰੀਏ:

- ਫੀਚਰ (ਟੂਲ, ਸਰੋਤ ਜਾਂ ਪ੍ਰੰਪਟ) ਬਣਾਉਣ ਲਈ ਲਾਜ਼ਮੀ ਤਰੀਕਾ ਉਸਦੇ ਨਿਰਧਾਰਤ ਫੋਲਡਰ ਵਿੱਚ ਲੈ ਜਾਵੇ।
- ਇੱਕ ਤਰੀਕਾ ਜੋ ਆ ਵਿੱਚ ਆਉਂਦੇ ਕਾਲ ਦੀ ਜਾਂਚ ਕਰੇ, ਉਦਾਹਰਨ ਵਜੋਂ ਟੂਲ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ।

### ਫੀਚਰ ਬਣਾਓ

ਇੱਕ ਫੀਚਰ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਉਸ ਫੀਚਰ ਲਈ ਇੱਕ ਫਾਇਲ ਬਣਾਉਣੀ ਪਵੇਗੀ ਅਤੇ ਯਕੀਨ ਕਰਨਾ ਪਵੇਗਾ ਕਿ ਉਸ ਵਿੱਚ ਲਾਜ਼ਮੀ ਖੇਤਰ ਸ਼ਾਮਿਲ ਹਨ, ਜੋ工具, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਵਿਚ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ।

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
        # Pydantic ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਦੀ ਤਸਦੀਕ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ਸ਼ਾਮਲ ਕਰੋ, ਤਾਂ ਜੋ ਅਸੀਂ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ args ਦੀ ਤਸਦੀਕ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਅਸੀਂ ਹੇਠ ਲਿਖਿਆ ਕਰਦੇ ਹਾਂ:

- Pydantic `AddInputModel` ਵਰਤ ਕੇ schema ਬਣਾਉਣਾ ਜਿਸ ਵਿੱਚ ਖੇਤਰ `a` ਅਤੇ `b` ਹਨ ਜੋ ਫਾਇਲ *schema.py* ਵਿੱਚ ਹਨ।
- ਆਉਂਦੇ ਦਲੀਲਾਂ ਨੂੰ `AddInputModel` ਦੇ ਤੌਰ ਤੇ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼, ਜੇ ਪੈਰਾਮੀਟਰਾਂ ਵਿੱਚ ਗਲਤੀ ਹੋਵੇ ਤਾਂ ਇਹ ਟੁੱਟ ਜਾਵੇਗਾ:

   ```python
   # add.py
    try:
        # Pydantic ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਨੂੰ ਵੈਰੀਫਾਈ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ਤੁਸੀਂ ਇਹਨਾਂ ਪਾਰਸਿੰਗ ਲਾਜਿਕ ਨੂੰ ਟੂਲ ਕਾਲ ਵਿੱਚ ਜਾਂ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਵਿੱਚ ਰੱਖ ਸਕਦੇ ਹੋ।

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

- ਸਾਰੇ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲਣ ਵਾਲੇ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਆਉਂਦੇ ਬੇਨਤੀ ਨੂੰ ਟੂਲ ਦੇ ਨਿਰਧਾਰਤ schema ਵਿੱਚ ਪਾਰਸ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼: 

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ਜੇ ਇਹ ਸਫਲ ਹੁੰਦਾ ਹੈ ਤਦ ਅਸੀਂ ਅਸਲ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const result = await tool.callback(input);
    ```

ਇਸ ਤਰੀਕੇ ਨਾਲ ਇੱਕ ਸ਼ਾਨਦਾਰ ਸੰਰਚਨਾ ਬਣਦੀ ਹੈ ਕਿਉਂਕਿ ਹਰ ਚੀਜ਼ ਆਪਣੇ ਸਥਾਨ 'ਤੇ ਹੁੰਦੀ ਹੈ, *server.ts* ਬਹੁਤ ਛੋਟਾ ਫਾਇਲ ਹੈ ਜੋ ਸਿਰਫ ਬੇਨਤੀ ਹੈਂਡਲਰ ਲਾਈਨ ਕਰਦਾ ਹੈ ਅਤੇ ਹਰ ਫੀਚਰ ਆਪਣੇ-ਆਪਣੇ ਫੋਲਡਰ ਵਿੱਚ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ tools/, resources/ ਜਾਂ /prompts.

ਵਧੀਆ, ਅਗਲੇ ਹਿੱਸੇ ਨੂੰ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ। 

## ਵਰਕਆਉਟ: ਲੋ-ਲੈਵਲ ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਵਰਕਆਉਟ ਵਿੱਚ ਅਸੀਂ ਹੇਠ ਲਿਖਿਆ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ:

1. ਇੱਕ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਬਣਾਉਣਾ ਜੋ ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਅਤੇ ਟੂਲ ਕਾਲਿੰਗ ਨੂੰ ਸੰਭਾਲੇ।
1. ਇੱਕ ਐਸਾ ਸੰਰਚਨਾ ਲਾਗੂ ਕਰਨੀ ਜੋ ਤੁਸੀਂ ਅਗਲੇ ਸਮੇਂ ਤੇ ਅਧਾਰਿਤ ਕਰ ਸਕੋ।
1. ਜਾਂਚ ਸ਼ਾਮਿਲ ਕਰਨੀ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਟੂਲ ਕਾਲ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਬਹੁਤਰੀਨ ਪੱਕੜੇ ਜਾਣ।

### -1- ਇੱਕ ਸੰਰਚਨਾ ਬਣਾਉਣਾ

ਸਭ ਤੋਂ ਪਹਿਲਾ ਕੁਝ ਅਜਿਹੀ ਸੰਰਚਨਾ ਦੀ ਲੋੜ ਹੈ ਜੋ ਸਾਡੇ ਫੀਚਰ ਵਧਣ ਦੁਆਰਾ ਪੈਮਾਨਾ ਬਧਾਉਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰੇ, ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ:

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

ਹੁਣ ਅਸੀਂ ਇੱਥੇ ਐਸੀ ਸੰਰਚਨਾ ਬਣਾਈ ਹੈ ਜੋ ਅਸਾਨੀ ਨਾਲ ਨਵੇਂ ਟੂਲਾਂ ਨੂੰ tools ਫੋਲਡਰ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰ ਸਕੇ। ਤੁਸੀਂ resources ਅਤੇ prompts ਲਈ ਵੀ ਸਬਡਾਇਰੈਕਟਰੀਜ਼ ਸ਼ਾਮਿਲ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ।

### -2- ਟੂਲ ਬਣਾਉਣਾ

ਆਓ ਵੇਖੀਏ ਕਿ ਟੂਲ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। ਪਹਿਲਾਂ, ਇਹ ਆਪਣੇ *tool* ਸਬਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਬਣਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ ਤਰ੍ਹਾਂ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ਪਾਈਡੈਂਟਿਕ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁਟ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ਪਾਈਡੈਂਟਿਕ ਸ਼ਾਮਲ ਕਰੋ, ਤਾਂ ਜੋ ਅਸੀਂ ਇੱਕ AddInputModel ਬਣਾ ਸਕੀਏ ਅਤੇ args ਦੀ ਪੁਸ਼ਟੀ ਕਰ ਸਕੀਏ

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ਇੱਥੇ ਅਸੀਂ ਵੇਖਦੇ ਹਾਂ ਕਿ ਕਿਵੇਂ ਅਸੀਂ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁੱਟ ਸਕੀਮਾ ਨੂੰ Pydantic ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇੱਕ ਹੈਂਡਲਰ ਜੋ ਇਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦਿਆਂ ਚਲਾਇਆ ਜਾਵੇਗਾ। ਆਖਰੀ ਵਿੱਚ, ਅਸੀਂ `tool_add` ਨਾਂ ਦਾ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਪ੍ਰਗਟ ਕਰਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਇਹ ਸਾਰੇ ਗੁਣ ਹਨ।

ਇੱਥੇ *schema.py* ਵੀ ਹੈ ਜੋ ਸਾਡੇ ਟੂਲ ਲਈ ਇਨਪੁੱਟ ਸਕੀਮਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ਸਾਨੂੰ *__init__.py* ਨੂੰ ਭੀ ਪੂਰਾ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ tools ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਮੋਡੀਊਲ ਵਜੋਂ ਮੰਨਿਆ ਜਾਵੇ। ਨਾਲ ਹੀ, ਅਸੀਂ ਇਸ ਵਿੱਚ ਮੌਜੂਦ ਮਾਡਿਊਲ ਵੀ ਬਾਹਰ ਪ੍ਰਗਟ ਕਰਦੇ ਹਾਂ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ਜਿੱਥੇ ਜਿੱਥੇ ਨਵੇਂ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰਨੇ ਹੋਣ, ਅਸੀਂ ਇਸ ਫਾਇਲ ਵਿੱਚ ਵੀ ਬਰਕਰਾਰ ਰੱਖਾਂਗੇ।

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

ਇੱਥੇ ਅਸੀਂ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਇਹ ਗੁਣ ਹਨ:

- name, ਇਹ ਟੂਲ ਦਾ ਨਾਮ ਹੈ।
- rawSchema, ਇਹ Zod ਸਕੀਮਾ ਹੈ ਜੋ ਇਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਵਾਲੀਆਂ ਆਉਂਦੀਆਂ ਬੇਨਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰੇਗਾ।
- inputSchema, ਇਹ ਹੈਂਡਲਰ ਵੱਲੋਂ ਵਰਤਿਆ ਜਾਵੇਗਾ।
- callback, ਇਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

ਇੱਥੇ `Tool` ਵੀ ਹੈ ਜੋ ਇਸ ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਇੱਕ ਕਿਸਮ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੋ mcp ਸਰਵਰ ਹੈਂਡਲਰ ਸਵੀਕਾਰ ਕਰ ਸਕਦਾ ਹੈ, ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ਅਤੇ ਇਹ *schema.ts* ਹੈ ਜਿੱਥੇ ਅਸੀਂ ਹਰ ਟੂਲ ਲਈ ਇਨਪੁੱਟ ਸਕੀਮਾਂ ਸੰਗ੍ਰਹਿਤ ਕਰਦੇ ਹਾਂ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ, ਹੁਣ ਸਿਰਫ ਇੱਕ ਸਕੀਮਾ ਹੈ ਪਰ ਜਿਵੇਂ ਜਿਵੇਂ ਅਸੀਂ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰਨਾਂਗੇ, ਹੋਰ ਐਂਟਰੀਆਂ ਵੀ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਆਪਣੇ ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਸੰਭਾਲਣਾ ਸ਼ੁਰੂ ਕਰੀਏ।

### -3- ਟੂਲ ਲਿਸਟਿੰਗ ਨੂੰ ਸੰਭਾਲਣਾ

ਅਗਲੇ, ਟੂਲ ਲਿਸਟਿੰਗ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਸੇਵਾ ਲਈ ਇੱਕ ਬੇਨਤੀ ਹੈਂਡਲਰ ਸੈੱਟ ਅਪ ਕਰਨਾ ਹੈ। ਇਹ ਸਾਡੇ ਸਰਵਰ ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕੀਤਾ ਜਾਵੇਗਾ:

**Python**

```python
# ਸਾਰ ਲਈ ਕੋਡ ਛੱਡਿਆ ਗਿਆ
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

ਇੱਥੇ, ਅਸੀਂ `@server.list_tools` ਡਿਕਰੇਟਰ ਅਤੇ ਇਸਨੂੰ ਲਾਗੂ ਕਰਨ ਵਾਲੀ ਫੰਕਸ਼ਨ `handle_list_tools` ਸ਼ਾਮਿਲ ਕਰਦੇ ਹਾਂ। ਇਸ ਵਿੱਚ ਸਾਨੂੰ ਟੂਲਾਂ ਦੀ ਇੱਕ ਲਿਸਟ ਤਿਆਰ ਕਰਨੀ ਹੈ। ਧਿਆਨ ਦਿਓ ਕਿ ਹਰ ਟੂਲ ਵਿੱਚ ਨਾਮ, ਵਰਣਨ ਅਤੇ inputSchema ਹੋਣਾ ਜ਼ਰੂਰੀ ਹੈ।   

**TypeScript**

ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਦੇ ਬੇਨਤੀ ਹੈਂਡਲਰ ਨੂੰ ਸੈੱਟ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਸਰਵਰ ਤੇ `setRequestHandler` ਕਾਲ ਕਰਨਾ ਹੈ ਜਿਸਦਾ schema ਉਸ ਕੰਮ ਲਈ ਫਿੱਟ ਬੈਠਦਾ ਹੈ, ਇੱਥੇ `ListToolsRequestSchema` ਹੈ। 

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
// ਸੰਖੇਪ ਲਈ ਕੋਡ ਛੱਡ ਦਿੱਤਾ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ਦਰਜ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੋ
  return {
    tools: tools
  };
});
```

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਦਾ ਹਿੱਸਾ ਸੰਜੋ ਲਿਆ ਹੈ, ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਟੂਲ ਕਾਲ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ।

### -4- ਟੂਲ ਕਾਲ ਕਰਨ ਨੂੰ ਸੰਭਾਲਣਾ

ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਇਕ ਹੋਰ ਬੇਨਤੀ ਹੈਂਡਲਰ ਬਣਾਉਣਾ ਪਏਗਾ, ਜੋ ਇਸ ਵਾਰੀ ਉਹ ਬੇਨਤੀ ਸੰਭਾਲੇ ਜੋ ਮੁਕੱਦਮਾ ਕਰੇ ਕਿਹੜਾ ਫੀਚਰ ਕਾਲ ਕਰਨਾ ਹੈ ਅਤੇ ਕਿਹੜੀਆਂ ਦਲੀਲਾਂ ਨਾਲ।

**Python**

ਆਓ ਡਿਕਰੇਟਰ `@server.call_tool` ਵਰਤ ਕੇ ਇੱਕ ਫੰਕਸ਼ਨ ਜਿਵੇਂ `handle_call_tool` ਲਿਖੀਏ। ਇਸ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਸਾਨੂੰ ਟੂਲ ਦਾ ਨਾਮ, ਇਸਦਾ ਆਰਗੂਮੈਂਟ ਕੱਢਣਾ ਹੈ ਅਤੇ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਦਲੀਲਾਂ ਇਸ ਟੂਲ ਲਈ ਸਹੀ ਹਨ। ਅਸੀਂ ਦਲੀਲਾਂ ਦੀ ਜਾਂਚ ਇਸੇ ਫੰਕਸ਼ਨ ਵਿੱਚ ਕਰ ਸਕਦੇ ਹਾਂ ਜਾਂ ਅਸਲ ਟੂਲ ਵਿੱਚ downstream ਕਰ ਸਕਦੇ ਹਾਂ।

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ਇੱਕ ਸ਼ਬਦਕੋਸ਼ ਹੈ ਜਿਸ ਵਿੱਚ ਸੰਦਾਂ ਦੇ ਨਾਮ ਕੁੰਜੀਆਂ ਵਜੋਂ ਹਨ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ਸੰਦ ਨੂੰ ਬੁਲਾਓ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ਇੱਥੇ ਚੀਜ਼ਾਂ ਕਿਵੇਂ ਚਲਦੀਆਂ ਹਨ:

- ਸਾਡਾ ਟੂਲ ਨਾਮ ਪਹਿਲਾਂ ਹੀ ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ `name` ਦੇ ਤੌਰ ਤੇ ਮੌਜੂਦ ਹੈ ਅਤੇ ਸਾਡੀਆਂ ਦਲੀਲਾਂ `arguments` ਡਿਕਸ਼ਨਰੀ ਦੇ ਤੌਰ ਤੇ ਹਨ।

- ਟੂਲ ਨੂੰ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ਨਾਲ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਦਲੀਲਾਂ ਦੀ ਜਾਂਚ ਹੈਂਡਲਰ ਗੁਣ ਵਿੱਚ ਹੁੰਦੀ ਹੈ ਜੋ ਫੰਕਸ਼ਨ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ, ਜੇ ਇਹ ਫੇਲ ਹੁੰਦਾ ਹੈ ਤਾਂ ਇੰਸੈਪਸ਼ਨ ਉਠਾਇਆ ਜਾਂਦਾ ਹੈ।

ਹਾਂ, ਹੁਣ ਅਸੀਂ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਨਾਲ ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਅਤੇ ਕਾਲ ਕਰਨ ਦੀ ਪੂਰੀ ਸਮਝ ਪ੍ਰਾਪਤ ਕਰ ਲਈ ਹੈ।

[ਇੱਥੇ ਪੂਰਾ ਉਦਾਹਰਨ](./code/README.md) ਵੇਖੋ

## ਅਸਾਈਨਮੈਂਟ

ਤੁਸੀਂ ਦਿੱਤੇ ਗਏ ਕੋਡ ਵਿੱਚ ਕਈ ਟੂਲ, ਸਰੋਤ ਅਤੇ ਪ੍ਰੰਪਟ ਸ਼ਾਮਿਲ ਕਰੋ ਅਤੇ ਦੇਖੋ ਕਿ ਤੁਹਾਨੂੰ ਕੇਵਲ tools ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਫਾਇਲਾਂ ਸ਼ਾਮਿਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਅਤੇ ਹੋਰ ਕਿੱਥੇ ਨਹੀਂ।

*ਕੋਈ ਹੱਲ ਨਹੀਂ ਦਿੱਤਾ ਗਿਆ ਹੈ*

## ਸਾਰ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਿਆ ਕਿ ਲੋ-ਲੈਵਲ ਸਰਵਰ ਪਹੁੰਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ ਅਤੇ ਇਹ ਕਿਵੇਂ ਸਾਡੇ ਲਈ ਇੱਕ ਸੁੰਦਰ ਸੰਰਚਨਾ ਬਣਾਉਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੀ ਹੈ ਜਿਸ 'ਤੇ ਅਸੀਂ ਅੱਗੇ ਬਣਾ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਜਾਂਚ ਬਾਰੇ ਵੀ ਚਰਚਾ ਕੀਤੀ ਅਤੇ ਤੁਹਾਨੂੰ ਦਿਖਾਇਆ ਗਿਆ ਕਿ ਜਾਂਚ ਲਈ ਕਿਵੇਂ ਸਚੇਤਨ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਨਾਲ ਕੰਮ ਕਰਨਾ ਹੈ।

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [ਸਧਾਰਣ ਪ੍ਰਮਾਣੀਕਰਨ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
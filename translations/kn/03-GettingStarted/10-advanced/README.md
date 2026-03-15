# ಅಧುನಿಕ ಸರ್ವರ್ ಬಳಕೆ

MCP SDK ಯಲ್ಲಿ ಎರಡು ವಿಭಿನ್ನ ವಿಧದ ಸರ್ವರ್‌ಗಳು ಬಹಿರಂಗಪಡಿಸಲಾಗಿದೆ, ನಿಮ್ಮ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು లో-ಲೆವೆಲ್ ಸರ್ವರ್. ಸಾಮಾನ್ಯವಾಗಿ, ನೀವು ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಅನ್ನು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಬಳಸುತ್ತೀರಿ. ಕೆಲ ಸಂದರ್ಭಗಳಲ್ಲಿ, ನೀವು లో-ಲೆವೆಲ್ ಸರ್ವರ್ ಮೇಲೆ ಅವಲಂಬಿಸಬೇಕಾಗುತ್ತದೆ, ಉದಾಹರಣೆಗೆ:

- ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪ. ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು లో-ಲೆವೆಲ್ ಸರ್ವರ್ ಎರಡರೊಂದಿಗೆ ಸ್ವಚ್ಛ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸೃಷ್ಟಿಸುವುದಕ್ಕೆ ಸಾಧ್ಯವಿದ್ದು, ಆದರೆ ಇದು ಸ್ವಲ್ಪ ಸುಲಭ ಎಂದು ವಾದಿಸಬಹುದು.
- ವೈಶಿಷ್ಟ್ಯ ಲಭ್ಯತೆ. ಕೆಲವು ಉನ್ನತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕೇವಲ లో-ಲೆವೆಲ್ ಸರ್ವರ್ ಮೂಲಕ ಮಾತ್ರ ಬಳಸಬಹುದು. ನಾವು ನಂತರದ ಅಧ್ಯಾಯಗಳಲ್ಲಿ ಸಾಂಪ್ರದಾಯಿಕ ಮತ್ತು ಎಲಿಸಿಟೇಶನ್ ಸೇರಿಸುವಾಗ ಇದನ್ನು ನೋಡುತ್ತೇವೆ.

## ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು లో-ಲೆವೆಲ್ ಸರ್ವರ್

ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ರಚನೆ ಹೀಗೆಯಿದೆ:

**Python**

```python
mcp = FastMCP("Demo")

# ಒಂದು ಸೇರ್ಪಡೆ ಸಾಧನವನ್ನು ಸೇರಿಸಿ
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

// ಒಂದು ಸೇರಿಸುವ ಸಾಧನವನ್ನು ಸೇರಿಸಿ
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

ನೀವು ಸ್ಪಷ್ಟವಾಗಿ ಸರ್ವರ್‌ಗೆ ಬೇಕಾದ ಪ್ರತಿಯೊಂದು ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಸೂತ್ರವನ್ನು ಸೇರಿಸುತ್ತೀರಿ. ಇದರಲ್ಲಿ ಯಾವದೂ ತಪ್ಪಿಲ್ಲ.

### లో-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ

ಆದರೆ, ನೀವು లో-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನವನ್ನು ಬಳಸುವಾಗ ಬೇರೆಯಾಗಿ ಯೋಚಿಸಬೇಕಾಗುತ್ತದೆ. ಪ್ರತಿಯೊಂದು ಸಾಧನವನ್ನು ನೋಂದಾಯಿಸುವ ಬದಲು, ನೀವು ವೈಶಿಷ್ಟ್ಯ ಪ್ರಕಾರಕ್ಕೆ (ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಅಥವಾ ಸೂತ್ರಗಳು) ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ರಚಿಸುತ್ತೀರಿ. ಉದಾಹರಣೆಗೆ, ಸಾಧನಗಳಿಗೆ ಕೆಳಗಿನ ಎರಡು ಕಾರ್ಯಗಳು ಇರುತ್ತವೆ:

- ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು. ಒಂದು ಕಾರ್ಯವು ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತಿದ್ದರೆ.
- ಎಲ್ಲಾ ಸಾಧನಗಳ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು. ಇಲ್ಲಿ ಕೂಡ, ಕೊಲುವ ಕೆಲಸಕ್ಕೆ ಒಂದೇ ಕಾರ್ಯ ಹೊಣೆಗಾರ.

ಇದು ಕಡಿಮೆ ಕೆಲಸವಾಗಬಹುದು ಎಂದು ತೋರುತ್ತದೆ ಅಲ್ಲವೇ? ಆದ್ದರಿಂದ ಸಾಧನವನ್ನು ನೋಂದಾಯಿಸುವ ಬದಲು, ನಾನು ಸಾಧನವೂ ಎಲ್ಲಾ ಸಾಧನಗಳು ಪಟ್ಟಿ ಮಾಡಿದಾಗ ಪಟ್ಟಿ ಮಾಡಲ್ಪಟ್ಟಿರಬೇಕು ಮತ್ತು ಯಾವುದಾದರು ಸಾಧನವನ್ನು ಕರೆಯಲು ವಿನಂತಿ ಬಂದಾಗ ಅದು ಕರೆಯಲ್ಪಡುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳುತ್ತೇನೆ.

ನೋಡೋಣ ಈಗ ಈ ಕೋಡ್ ಹೇಗಿದೆ:

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
  // ನೋಂದಾಯಿಸಲಾಗಿದೆ ಉಪಕರಣಗಳ പട്ടಿಕೆಯನ್ನು ಮರಳಿಸಿ
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

ಇಲ್ಲಿ ಈಗ ವೈಶಿಷ್ಟ್ಯಗಳ ಪಟ್ಟಿ ನೀಡುವ ಕಾರ್ಯವಿದೆ. ಸಾಧನಗಳ ಪಟ್ಟಿಯ ಪ್ರತಿಯೊಂದು ನಮೂದಿಗೆ `name`, `description` ಮತ್ತು `inputSchema` ಎಂಬ ಕ್ಷೇತ್ರಗಳಿವೆ, ಇದರಿಂದ ನಾವು ಸಾಧನ ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ವ್ಯಾಖ್ಯಾನಗಳನ್ನು ಬೇರೆಡೆ ಇಡಬಹುದು. ನಾವು ಈಗ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿರಿಸಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಎಲ್ಲ ವೈಶಿಷ್ಟ್ಯಗಳಿಗೆ ಸಹ ಹಾಗೆ ಮಾಡಬಹುದು, ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಹೀಗೆ ಸಂಘಟಿತವಾಗಬಹುದು:

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

ಚೆನ್ನಾಗಿದೆ, ನಮ್ಮ ವಾಸ್ತುಶಿಲ್ಪ ಸ್ವಚ್ಛವಾಗಿ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತದೆ.

ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡುವದಾದರೆ ಹೇಗೆ, ಅದೇ ಕಲ್ಪನೆ ಅಲ್ಲವೇ, ಯಾವುದಾದರೂ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡುವ ಒಂದು ಹ್ಯಾಂಡ್ಲರ್? ಹೌದು, ಖಚಿತವಾಗಿ, ಅದಕ್ಕಾಗಿ ಕೆಳಗಿನ ಕೋಡ್ ಇದೆ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಟೂಲ್ ಹೆಸರುಗಳನ್ನು ಕೀಗಳಾಗಿ ಬಳಸಿಕೊಂಡು ರೂಪಿಸಿದ ನಿಘಂಟು.
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
    // TODO ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ಮೇಲಿನ ಕೋಡ್‌ನಿಂದ ನೀವು ನೋಡಬಹುದಾದಂತೆ, ನಾವು ಕರೆಯಬೇಕಾದ ಸಾಧನವನ್ನು ಯಾವ ತರ್ಕದೊಂದಿಗೆ ಕರೆಯಬೇಕೋ ವಿವರಿಸಿ ಅದು ಕರೆ ಮಾಡಲು ಮುಂದೆ ಹೋಗಬೇಕು.

## ಮಾನ್ಯತೆ ಮೂಲಕ ವಿಧಾನವನ್ನು ಸುಧಾರಣೆ

ಇದುವರೆಗೆ ನೀವು ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಸೂತ್ರಗಳನ್ನು ಸೇರಿಸುವ ನಿಮ್ಮ ಎಲ್ಲಾ ನೋಂದಣಿಗಳನ್ನು ಈ ಎರಡು ಹ್ಯಾಂಡ್ಲರ್ ಗಳು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯದ ಪ್ರಕಾರ ಬದಲಿ ಮಾಡಬಹುದೆಂದು ನೋಡಿದ್ದೀರಿ. ಇನ್ನೇನು ಮಾಡಬೇಕಿದೆ? ನಾವು ಸಾಧನ ಸರಿಯಾದ ತರ್ಕದೊಂದಿಗೆ ಕರೆ ಮಾಡುತ್ತಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸುವ ಮಾನ್ಯತೆ ಸೇರಿಸಬೇಕು. ಪ್ರತಿಯೊಂದುruntime ಇದಕ್ಕೆ ತಮ್ಮದೇ ಪರಿಹಾರವಿದೆ, ಉದಾಹರಣೆಗೆ Python Pydantic ಬಳಕೆಮಾಡುತ್ತದೆ ಮತ್ತು TypeScript Zod ಬಳಸುತ್ತದೆ. ತತ್ವವೇನೆಂದರೆ:

- ವೈಶಿಷ್ಟ್ಯ (ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಸೂತ್ರ) ಸೃಷ್ಟಿಸುವ ತರ್ಕವನ್ನು ಅದರ ಸಮರ್ಪಿತ ಫೋಲ್ಡರ್‌ಗೆ ವರ್ಗಾಯಿಸಿ.
- ಉದಾಹರಣೆಗೆ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡುವ ವಿನಂತಿಯನ್ನು ಮಾನ್ಯತೆ ಮಾಡಿಸಲು ವಿಧಾನ ಸೇರಿಸಿ.

### ವೈಶಿಷ್ಟ್ಯವನ್ನು ರಚಿಸುವುದು

ವೈಶಿಷ್ಟ್ಯವನ್ನು ರಚಿಸುವುದಕ್ಕೆ ಅವಶ್ಯಕ ಕ್ಷೇತ್ರಗಳೊಂದಿಗೆ ಒಂದು ಫೈಲ್ ರಚಿಸಬೇಕು. ಯಾವ ಕ್ಷೇತ್ರಗಳು ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಸೂತ್ರಗಳಲ್ಲಿ ಭಿನ್ನತೆ ಇದೆ.

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
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಪರಿಶೀಲಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಅನ್ನು ಸೇರಿಸಿ, ಆದ್ದರಿಂದ ನಾವು AddInputModel ರಚಿಸಬಹುದು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ಇಲ್ಲಿ ನಾವು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತೇವೆ ಎಂಬುದು ಇಂತಿದೆ:

- Pydantic ಬಳಸಿ `AddInputModel` ಎಂಬ ಸ್ಕೀಮಾ ಅನ್ನು `a` ಮತ್ತು `b` ಕ್ಷೇತ್ರಗಳೊಂದಿಗೆ *schema.py* ಫೈಲ್‌ನಲ್ಲಿ ರಚಿಸಿ.
- ನಮೂದಿಸಿದ ವಿನಂತಿಯನ್ನು `AddInputModel` ಗೆ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸಿ, ಪ್ಯಾರಾಮೀಟರ್ಗಳಲ್ಲಿ ಭಿನ್ನತೆ ಇದ್ದರೆ ಅಪಘಾತ ಉಂಟಾಗುತ್ತದೆ:

   ```python
   # add.py
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಪರಿಶೀಲಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ಈ ಪಾರ್ಸಿಂಗ್ ತರ್ಕವನ್ನು ಸಾಧನ ಕರೆಯುವಲ್ಲಿ ಅಥವಾ ಹ್ಯಾಂಡ್ಲರ್ ಕಾರ್ಯದಲ್ಲಿ ಇರಿಸಬಹುದು.

**TypeScript**

```typescript
// ಸರ್ವರ್.ts
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

       // @ts-ಅಗ್ನೋರ್
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

// ಸ್ಕೀಮಾ.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// ಸೇರಿಸು.ts
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

- ಎಲ್ಲಾ ಸಾಧನ ಗಳ ಕರೆಗಳನ್ನು ನಿಭಾಯಿಸುವ ಹ್ಯಾಂಡ್ಲರ್‌ನಲ್ಲಿ, ನಾವು ಈಗಿನ ವಿನಂತಿಯನ್ನು ಸಾಧನ ವ್ಯಾಖ್ಯಾನಿತ ಸ್ಕೀಮಾಗೆ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ಸರಿ ಆಗಿದ್ದರೆ ನಾವು ಆ ಸದನವನ್ನೇ ಕರೆ ಮಾಡುತ್ತೇವೆ:

    ```typescript
    const result = await tool.callback(input);
    ```

ನೀವು ನೋಡಬಹುದಾದಂತೆ, ಈ ವಿಧಾನವು ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಪ್ರತಿಯೊಂದು ಎಲ್ಲಿದೆಂದು ಇದೆ, *server.ts* ಅತ್ಯಂತ ಸಣ್ಣ ಫೈಲ್ ಆಗಿದ್ದು ಕೇವಲ ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಗಳು ಸಂಪರ್ಕ ಮಾಡುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಯೊಂದು ವೈಶಿಷ್ಟ್ಯ ತನ್ನ-ತನ್ನ ಫೋಲ್ಡರ್ ನಲ್ಲಿ ಇರುತ್ತದೆ: tools/, resources/ ಅಥವಾ prompts/.

ಚೆನ್ನಾಗಿದೆ, ಅದನ್ನು ಮುಂದುವರೆಯೋಣ.

## ವ್ಯಾಯಾಮ: ಲೋ ಲೆವೆಲ್ ಸರ್ವರ್ ರಚನೆ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ನಾವು:

1. ಉಪಕರಣಗಳ ಪಟ್ಟಿ ಮತ್ತು ಕರೆಯುವಿಕೆಯನ್ನು ನಿಭಾಯಿಸುವ ಲೋ ಲೆವೆಲ್ ಸರ್ವರ್ ರಚನೆ.
2. ನಿರ್ಮಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.
3. ಸಾಧನಗಳ ಕರೆಯಲು ಮಾನ್ಯತೆ ಸೇರಿಸಿ.

### -1- ವಾಸ್ತುಶಿಲ್ಪ ರಚನೆ

ನಾವು ನಿಭಾಯಿಸುವ ಮೊದಲ ವಿಷಯವು ಹೆಚ್ಚಿನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಸಹಾಯ ಮಾಡುವ ವಾಸ್ತುಶಿಲ್ಪ.

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

ನಾವು ಈಗ tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಸುಲಭವಾಗಿ ಹೊಸ ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪ ಸಿದ್ಧಪಡಿಸಿದ್ದೇವೆ. resources ಮತ್ತು prompts ಗೆ ಉಪಮಾಹಿತಿಗಳನ್ನು ಸೇರಿಸಲು ಈ ಮಾರ್ಗವನ್ನು ಅನುಸರಿಸಬಹುದು.

### -2- ಉಪಕರಣ ರಚನೆ

ಮುಂದೆ ಉಪಕರಣ ರಚಿಸುವುದು ಹೇಗಿದೆ ನೋಡೋಣ. ಮೊದಲಿಗೆ ಇದು ತನ್ನ *tool* ಉಪವಿಭಾಗದಲ್ಲಿ ರಚಿಸಬೇಕಾಗುತ್ತದೆ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಅನ್ನು ಸೇರಿಸಿ, ಹೀಗಾಗಿ ನಾವು AddInputModel ರಚಿಸಿ ಆರ್ಗ್ಸ್‌ಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ಇಲ್ಲಿ ನಾವು Pydantic ಬಳಸಿ ಹೆಸರು, ವಿವರಣೆ, ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ ಮತ್ತು ಈ ಸಾಧನ ಕರೆ ಮಾಡಲಾದಾಗ invoke ಆಗುವ ಹ್ಯಾಂಡ್ಲರ್ ಇದೆ. ಕೊನೆಗೆ, ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಹೊಂದಿರುವ `tool_add` ಡಿಕ್ಷನರಿಯನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತೇವೆ.

ಮತ್ತು *schema.py* ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾ ವ್ಯಾಖ್ಯಾನ ಮಾಡಲು ಉಪಯೋಗಿಸುತ್ತಿದೆ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ಅನ್ನು ಬಿಡದೇ ಪರಿಪೂರ್ಣ ಮಾಡಬೇಕು; ಇದು tools ಡಿರೆಕ್ಟರಿಯನ್ನು ಮಾಯೋಜ್ಯುತ ಆಗಿಸುವಂತೆ ಮಾಡುತ್ತದೆ. ಜೊತೆಗೆ ಈ ಫೈಲ್ ಮೂಲಕ ಒಳಗಿನ ಎಲ್ಲಾ ಮಾಯೋಜ್ಯುಲ್ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸಬೇಕು:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ಹೆಚ್ಚು ಸಾಧನಗಳನ್ನು ಸೇರಿಸುವಾಗ ಈ ಫೈಲ್ ವಿಸ್ತಾರ ಸಾಧ್ಯ.

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

ಇಲ್ಲಿ ನಾವು ಗುಣಲಕ್ಷಣಗಳ ಡಿಕ್ಷನರಿ ರಚಿಸುತ್ತೇವೆ:

- name: ಸಾಧನದ ಹೆಸರು.
- rawSchema: Zod ಸ್ಕೀಮಾ, ಇದನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಈ ಸಾಧನ ಕರೆಯುವ ವಿನಂತಿಗಳ ಮಾನ್ಯತೆಗೆ ಬಳಸಲಾಗುತ್ತದೆ.
- inputSchema: ಈ ಸ್ಕೀಮಾವನ್ನು ಹ್ಯಾಂಡ್ಲರ್ ಬಳಸುತ್ತದೆ.
- callback: ಇದನ್ನು ಸಾಧನ invoke ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ.

`Tool` ಕೂಡ ಇರುತ್ತದೆ, ಇದು ಡಿಕ್ಷನರಿಯನ್ನು mcp ಸರ್ವರ್ ಹ್ಯಾಂಡ್ಲರ್ ಸ್ವೀಕರಿಸುವ ಪ್ರಕಾರಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ಮತ್ತು *schema.ts* ಇದರಲ್ಲಿ ಪ್ರತಿ ಉಪಕರಣದ ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾಗಳು ಇರುತ್ತವೆ, ಈಗಿಗೆ ಒಂದೇ ಸ್ಕೀಮಾ ಇದೆ ಆದರೆ ಹೆಚ್ಚಿಸಿದಂತೆ ಹೆಚ್ಚಿಸಿರಿ:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ಚೆನ್ನಾಗಿದೆ, ಈಗ ಉಪಕರಣಗಳ ಪಟ್ಟಿ ನಿಭಾಯಿಸಲು ಮುಂದಾಗೋಣ.

### -3- ಉಪಕರಣ ಪಟ್ಟಿ ನಿಭಾಯಿಸುವುದು

ಉಪಕರಣಗಳ ಪಟ್ಟಿ ನಿಭಾಯಿಸಲು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಸಿದ್ಧಪಡಿಸುವುದು, ಇದರ ಕೋಡ್ ಸರ್ವರ್ ಫೈಲ್‌ಗೆ ಸೇರಿಸಬೇಕು:

**Python**

```python
# ಸಂಕ್ಷಿಪ್ತತೆಗೆ ಕೋಡ್ ಹೊರತುಪಡಿಸಲಾಗಿದೆ
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

ಇಲ್ಲಿ ನಾವು `@server.list_tools` ಡೆಕಾರೇಟರ್ ಮತ್ತು ಅದನ್ನು ನಿಭಾಯಿಸುವ `handle_list_tools` ಕ್ರಿಯೆಯನ್ನು ಸೇರಿಸುತ್ತೇವೆ. ನಂತರ ಸಾಧನಗಳ ಪಟ್ಟಿ ಸೃಷ್ಟಿಸಬೇಕು. ಪ್ರತಿ ಸಾಧನಕ್ಕೆ ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾ ಇರಬೇಕು ಎಂದು ಗಮನಿಸಿ. 

**TypeScript**

ವಿನಂತಿಯ ಹ್ಯಾಂಡ್ಲರ್ ಸಿದ್ಧಪಡಿಸಲು, ಸರ್ವರ್‌ನಲ್ಲಿ `setRequestHandler` ಕರೆ ಮಾಡಬೇಕು, ಇದಕ್ಕೆ ಬರುವ ಸ್ಕೀಮಾದೊಂದಿಗೆ - ಇಲ್ಲಿ `ListToolsRequestSchema`.

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
// ಸರಳತೆಗೆ ಕೋಡ್ ಒತ್ತಿಮಾಡಲಾಗಿದೆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ನೋಂದಾಯಿತ ಸಲಕರಣೆಗಳ ಪಟ್ಟಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
  return {
    tools: tools
  };
});
```

ಚೆನ್ನಾಗಿದೆ, ಈಗ ಉಪಕರಣಗಳ ಪಟ್ಟಿಯ ಸಮಸ್ಯೆ ಪರಿಹರಿಸಿದೆ, ನೋಡೋಣ ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡುವುದನ್ನು.

### -4- upkaraṇa ಕರೆಯುವಿಕೆ ನಿಭಾಯಿಸುವದು

ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಲು ಇನ್ನೊಂದು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಸಿದ್ಧಪಡಿಸಬೇಕಾಗುತ್ತದೆ, ಇದು ಯಾವ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಕರೆಯುವುದು ಮತ್ತು ಯಾವ ಪರಿಮಾಣಗಳೊಂದಿಗೆ ಎನ್ನುವ ವಿನಂತಿಯನ್ನು ನಿಭಾಯಿಸುತ್ತದೆ.

**Python**

`@server.call_tool` ಡೆಕಾರೇಟರ್ ಬಳಸಿ, `handle_call_tool` ಎಂಬ ಕಾರ್ಯವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸೋಣ. ಈ ಕಾರ್ಯದಲ್ಲಿ ಸಾಧನದ ಹೆಸರು ಮತ್ತು ಅದರ ಪರಿಮಾಣಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಬೇಕು ಮತ್ತು ಪರಿಮಾಣಗಳು ಸರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು. ಈ ಮಾನ್ಯತೆಯನ್ನು ಈ ಕಾರ್ಯದಲ್ಲಿ ಅಥವಾ ನಿಜವಾದ ಸಾಧನದಲ್ಲಿಯೂ ಮಾಡಬಹುದು.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಅನ್ನು ಉಪಕರಣಗಳ ಹೆಸರುಗಳನ್ನು ಕೀಲಿಗಳಾಗಿ ಹೊಂದಿರುವ ಡಿಕ್ಷನರಿ ಆಗಿದೆ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ಇದಾವಂತೆ ನಡೆಯುತ್ತದೆ:

- ಸಾಧನದ ಹೆಸರು ಈಗಲೇ ಇನ್‌ಪುಟ್ ಪ್ಯಾರೆಮೀಟರ್ `name` ಆಗಿದೆ, ಮತ್ತು `arguments` ಡಿಕ್ಷನರಿಯಲ್ಲಿ ಪರಿಮಾಣಗಳೂ ಇದ್ದವು.

- ಸಾಧನವನ್ನು `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ನಲ್ಲಿ ಕರೆ ಮಾಡಲಾಗಿದೆ. ಪರಿಮಾಣಗಳ ಮಾನ್ಯತೆ `handler` ಗುಣಲಕ್ಷಣದಲ್ಲಿ ಕಾರ್ಯವಾಗುತ್ತದೆ, ಅದು ತಪ್ಪು ನೀಡಿದರೆ ಸ_EXCEPTION ಉಂಟಾಗುತ್ತದೆ.

ಇಷ್ಟು, ನಾವು ಲೋ ಲೆವೆಲ್ ಸರ್ವರ್ ಬಳಸಿ ಉಪಕರಣಗಳ ಪಟ್ಟಿಸುವಿಕೆ ಮತ್ತು ಕರೆ ಮಾಡುವುದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇವೆ.

ಪೂರ್ಣ ಉದಾಹರಣೆ ನೋಡಿ: [full example](./code/README.md)

## ಕಾರ್ಯ

ನೀವು ಪಡೆದಿರುವ ಕೋಡ್ ಅನ್ನು ಹಲವು ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸೂತ್ರಗಳಿಂದ ವಿಸ್ತರಿಸಿ, ನೀವು ಗಮನಿಸುವಿರಿ, ನಿಮಗೆ ಕೇವಲ tools ಡೈರಕ್ಟರಿಯಲ್ಲಿ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸುವಷ್ಟೇ ಅಗತ್ಯ, ಮತ್ತಾವುದೇ ಸ್ಥಳದಲ್ಲಿ ಅಲ್ಲ.

*ಯಾವುದೇ ಪರಿಹಾರ ನೀಡಲಾಗಿಲ್ಲ*

## ಸಾರಾಂಶ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ಲೋ ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ ಹೇಗೆ ಚಲಿಸುತ್ತದೆ ಮತ್ತು ಅದು ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸಲು ಹೇಗೆ ಸಹಾಯಕ ಎಂಬುದನ್ನು ನೋಡಿ. ನಾವು ಮಾನ್ಯತೆಯನ್ನು ಚರ್ಚಿಸಿ, ಇನ್‌ಪುಟ್ ಮಾನ್ಯತೆಗೆ ಸ್ಕೀಮಾಗಳು ರಚಿಸುವುದಕ್ಕೆ ಮಾನ್ಯತೆ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಹೇಗೆ ಬಳಸಬೇಕು ಎಂಬುದನ್ನು ತಿಳಿದುಕೊಂಡಿದ್ದೇವೆ.

## ಮುಂದೇನು

- ಮುಂದಿನ ಅಧ್ಯಾಯ: [ಸರಳ ಪ್ರಮಾಣೀಕರಣ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಪರಾಹ್ನ**:  
ಈ ನುಡಿಮಾತು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಭಾಷಾಂತರ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಭಾಷಾಂತರಿಸಲು ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿರಿ. ಮೂಲ ದಾಖಲೆ ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಅಧಿಕೃತ ಸ್ರೋತವನ್ನಾಗಿ ಪರಿಗಣಿಸಲಾಗಬೇಕು. ಮಹತ್ವಪೂರ್ಣ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅಸಮಂಜಸ್ಯತೆಗಳು ಅಥವಾ ತಪ್ಪುಬುದ್ದಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
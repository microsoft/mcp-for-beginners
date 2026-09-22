# ಪ್ರಗತಿಶೀಲ ಸರ್ವರ್ ಬಳಕೆ

MCP SDK ಯಲ್ಲಿ ಎರಡು ವಿಭಿನ್ನ ರೀತಿಯ ಸರ್ವರ್‌ಗಳು ಬಾಹ್ಯಗುಮೆಯಾಗಿವೆ, ನಿಮ್ಮ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್. ಸಾಮಾನ್ಯವಾಗಿ, ನೀವು ಲಕ್ಷಣಗಳನ್ನು ಸೇರಿಸಲು ನಿಯಮಿತ ಸರ್ವರ್ ಅನ್ನು ಬಳಸುತ್ತೀರಿ. ಆದರೆ ಕೆಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ, ನೀವು ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ಮೇಲೆ ನಂಬಿಕೆ ಇಡಬೇಕು, ಉದಾಹರಣೆಗೆ:

- ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪ. ನಿಯಮಿತ ಸರ್ವರ್ ಮತ್ತು ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ಎರಡನ್ನೂ ಬಳಸಿಕೊಂಡು ಶುದ್ಧ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸೃಷ್ಟಿಸುವುದು ಸಾಧ್ಯ, ಆದರೆ ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ಬಳಸಿದಾಗ ಇದು ಸ್ವಲ್ಪ ಸುಲಭವಾಗಬಹುದು ಎಂದು ವಿವಾದಿಸಬಹುದು.
- ಲಕ್ಷಣ ಲಭ್ಯತೆ. ಕೆಲವು ಪ್ರಗತಿಶೀಲ ಲಕ್ಷಣಗಳನ್ನು ಮಾತ್ರ ಕೆಳ-ಮಟ್ಟದ ಸರ್ವರ್‌ನಲ್ಲಿ ಬಳಸಬಹುದು.
    ನಂತರದ ಅಧ್ಯಾಯಗಳಲ್ಲಿ Elicitation ಮತ್ತು ಪೈಪ್ಲೈನ್ Sampling
    ಲಕ್ಷಣವನ್ನು ಕೂಡ ವಿವರಿಸಲಾಗಿದ್ದು, ಇದು MCP `2026-07-28` ನಲ್ಲಿ ಹಳೆಯದಾಗಿ ಪರಿಗಣಿಸಲಾಗಿದೆ.

## ನಿಯಮಿತ ಸರ್ವರ್ ವಿರುದ್ಧ ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್

ನಿಯಮಿತ ಸರ್ವರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ರಚನೆ ಹೇಗಿರುತ್ತದೆ ಹೀಗಿದೆ

**Python**

```python
mcp = FastMCP("Demo")

# ಒಂದು ಸೇರ್ಪಡೆ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
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

// ಸೇರಿಸುವ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
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

ಅರ್ಥವೆನಂದ್ರೆ ನೀವು ಸರ್ವರ್ ಹೊಂದಿರಬೇಕಾದ ಪ್ರತಿಯೊಂದು ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಸೇರಿಸುತ್ತೀರಿ. ಇದರಲ್ಲಿ ಏನೂ ತಪ್ಪಿಲ್ಲ.  

### ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ವಿಧಾನ

ಆದಾಗ್ಯೂ, ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ಪದ್ದತಿಯನ್ನು ಬಳಸಿದಾಗ ನೀವು ವಿಭಿನ್ನ ರೀತಿಯಲ್ಲಿ ಯೋಚಿಸಬೇಕು. ಪ್ರತಿ ಲಕ್ಷಣ ಪ್ರಕಾರಕ್ಕೆ ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸಬೇಕು (sadhana, ಸಂಪನ್ಮೂಲಗಳು ಅಥವಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳು). ಉದಾಹರಣೆಗೆ, ಸಾಧನಗಳಿಗೆ ಕೇವಲ ಎರಡು ಕಾರ್ಯಗಳು ಇರುತ್ತವೆ ಹೀಗಾಗಿ:

- ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು. ಒಂದು ಕಾರ್ಯವು ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು ಹೊಣೆ ಹೊತ್ತಿರುತ್ತದೆ.
- ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವದು. ಇಲ್ಲಿ ಸಹ ಸರ್ವಕಾಲಿಕ ಕಾರ್ಯವೊಂದೇ ಸಾಧನಕ್ಕೆ ಕರೆಗಳನ್ನು ಸಂಸ್ಕರಿಸುತ್ತದೆ.

ಇದು ಕಡಿಮೆ ಕೆಲಸವೆಂದು ತೋರುತ್ತದೆ ಹೌದಾ? ಆದ್ದರಿಂದ ಒಂದು ಸಾಧನವನ್ನು ನೊಂದಾಯಿಸುವ ಬದಲು, ನಾನು ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವಾಗ ಸಾಧನ ಪಟ್ಟಿ ಇಲ್ಲಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು ಮತ್ತು ಸಾಧನವನ್ನು ಕರೆಮಾಡುವ ವಿನಂತಿ ಬಂದಾಗ ಅದನ್ನು ಕರೆಮಾಡಬೇಕು. 

ಈಗ ನೋಡೋಣ ಈ ಕೋಡ್ ಈಗ ಹೇಗಿದೆ:

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
  // ನೋಂದಾಯಿಸಲಾದ ಉಪಕರಣಗಳ ಪಟ್ಟಿ ನೀಡಿರಿ
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

ಇಲ್ಲಿ ನಾವು ಈಗ ಕಾರ್ಯಗಳನ್ನು ಹಿಂತಿರುಗಿಸುವ ಕಾರ್ಯವೊಂದನ್ನು ಹೊಂದಿದ್ದೇವೆ. ಸಾಧನಗಳ ಪಟ್ಟಿಯು ಈಗ `name`, `description` ಮತ್ತು `inputSchema` ಎಂಬ ಕ್ಷೇತ್ರಗಳನ್ನು ಹೊಂದಿದೆ. ಇದು ಪ್ರತ್ಯೇಕವಾಗಿ ಸಾಧನಗಳು ಮತ್ತು ಲಕ್ಷಣ ವ್ಯಾಖ್ಯಾನವನ್ನು ಬೇರೆಯಡೆ ಇಡುವುದಕ್ಕೆ ಅವಕಾಶ ಕೊಡುತ್ತದೆ. ಈಗ ನಾವು ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ರಚಿಸಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಎಲ್ಲ ಲಕ್ಷಣಗಳಿಗೂ ಕೂಡ ಇದನ್ನು ಅನ್ವಯಿಸಬಹುದು. ಆದ್ದರಿಂದ ನಿಮ್ಮ ಯೋಜನೆ ಹೀಗೆಸಿದ್ಧವಾಗಬಹುದು:

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

ಇದು ಉತ್ತಮ, ನಮ್ಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸ್ವಚ್ಛವಾಗಿ ರೂಪಿಸಬಹುದು.

ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವುದರ ಬಗ್ಗೆ, ಇದು ಒಂದೇ ಧಾರಾಳನೆ ಹೌದಾ, ಒಂದು ಹ್ಯಾಂಡ್ಲರ್ ಎಲ್ಲ ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುತ್ತದೆ? ಹೌದು, ನಿಖರವಾಗಿ, ಇದಕ್ಕಾಗಿ ಕೋಡ್ ಹೀಗಿದೆ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಕೀಲಿಗಳು ಯಂತ್ರೋಪಕರಣಗಳ ಹೆಸರുകൾ ಇರುವ ನಿಘಂಟುವಾಗಿದೆ
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

ಮೇಲಿನ ಕೋಡ್ ನೋಡಿದರೆ, ನಾವು ಕರೆಮಾಡುವ ಸಾಧನವನ್ನು ಮತ್ತು ಅದರ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಅಗತ್ಯವಿದೆ ಮತ್ತು ನಂತರ ಸಾಧನವನ್ನು ಕರೆಮಾಡುವ ಪ್ರಕ್ರಿಯೆಗೆ ಮುಂದುವರೆಯಬೇಕು.

## ಪರಿಶೀಲನೆ ಮೂಲಕ ವಿಧಾನ ವೃದ್ಧಿ

ಇಷ್ಟು ದೂರ ನೀವು ನೋಡಿದಂತೆ ಸಾಧನಗಳನ್ನು, ಸಂಪನ್ಮೂಲಗಳನ್ನು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸೇರಿಸುವ ನೊಂದಾಯಿಸುವಿಕೆಗಳನ್ನು ಪ್ರತಿಯೊಂದು ಲಕ್ಷಣ ಪ್ರಕಾರಕ್ಕೆ ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳಿಂದ ಬದಲಾಯಿಸಬಹುದು. ನಾವು ಇನ್ನೇನು ಮಾಡಬೇಕು? ಸರಿಯಾದ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಸಾಧನವನ್ನು ಕರೆಯಲಾಗುತ್ತಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಲು ವ suatuಪಶೀಲನೆ ಒಂದನ್ನು ಸೇರಿಸಬೇಕು. ಪ್ರತಿ ರನ್‌ಟೈಮ್ ತಮ್ಮದೇ ರೀತಿಯ ಪರಿಹಾರವನ್ನು ಹೊಂದಿವೆ, ಉದಾಹರಣೆಗೆ Python Pydantic ಅನ್ನು ಮತ್ತು TypeScript Zod ಅನ್ನು ಬಳಸುತ್ತದೆ. ನಮ್ಮ ಯೋಚನೆ ಹೀಗಿದೆ:

- ವೈಶಿಷ್ಟ್ಯ ( ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್ ) ರಚಿಸುವ ಲಾಜಿಕ್ ಅನ್ನು ಅದರ ಸಮರ್ಪಿತ ಫೋಲ್ಡರ್‌ಗೆ ಸರಿಸಿ.
- ಉದಾಹರಣೆಗೆ ಸಾಧನವನ್ನು ಕರೆಯಲು ಕೇಳುವ ಯಾವುದೇ ನಿರ್ಗಮಿಸುವ ವಿನಂತಿಯನ್ನು ಪರಿಶೀಲಿಸಲು ವಿಧಾನ ಸೇರಿಸಿ.

### ವೈಶಿಷ್ಟ್ಯ ರಚಿಸಿ

ವೈಶಿಷ್ಟ್ಯವನ್ನು ರಚಿಸಲು, ನಾವು ಆ ವೈಶಿಷ್ಟ್ಯದ ಫೈಲ್ ಸೃಷ್ಟಿಸಬೇಕು ಮತ್ತು ಅದರಲ್ಲಿ ಆ ವೈಶಿಷ್ಟ್ಯಕ್ಕೆ ಬೇಕಾದ ಆವಶ್ಯಕ ಕ್ಷೇತ್ರಗಳನ್ನು ಕಾಣಿಸಬೇಕು. ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳಲ್ಲಿ ಕೆಲವು ಕ್ಷೇತ್ರಗಳ ಭಿನ್ನತೆ ಇದೆ.

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
        # ಪೈಡ್ಯಾಂಟಿಕ್ ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್ಪುಟ್ ಅನ್ನು ಪರಿಶೀಲಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # ಟುಡೂ: ಪೈಡ್ಯಾಂಟಿಕ್ ಸೇರಿಸು, ಆದ್ದರಿಂದ ನಾವು AddInputModel ರಚಿಸಿ ಮತ್ತು ಆರ್ಗ್ಸ್ ಅನ್ನು ಪರಿಶೀಲಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ಇಲ್ಲಿ ನಾವು ಹೀಗೆ ಮಾಡುತ್ತೇವೆ:

- Pydantic `AddInputModel` ಬಳಸಿ `a` ಮತ್ತು `b` ಕ್ಷೇತ್ರಗಳನ್ನು ಹೊಂದಿರುವ ಪಠ್ಯ ರೂಪ ರಚಿಸಿ *schema.py* ಫೈಲ್‌ನಲ್ಲಿ.
- ಬರುವ ವಿನಂತಿಯನ್ನು `AddInputModel` ರೀತಿಗೆ ವಿಶ್ಲೇಷಿಸಲು ಪ್ರಯತ್ನಿಸಿ, ಪರಿಮಾಣಗಳಲ್ಲಿ ಸೇರಿದಾಗಲ್ಲಿ ಇದು ದೋಷ ಉಂಟುಮಾಡುತ್ತದೆ:

   ```python
   # add.py
    try:
        # ಪ್ಯಾಡ್ಯಾಂಟಿಕ್ ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಇನ್‌ಪುಟ್ ಮಾನ್ಯತೆ ಮಾಡು
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ನೀವು ಈ ವಿಷಯದ ವಿಶ್ಲೇಷಣಾ ಲಾಜಿಕ್ ಅನ್ನು ಸಾಧನದ ಕರೆ ಅಥವಾ ಹ್ಯಾಂಡ್ಲರ್ ಕಾರ್ಯದಲ್ಲಿ ಇರಿಸಬಹುದು.

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

       // @ts-ಅನುವೂತಿಸಿ
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

// ಸ್ಕೆಮಾ.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// ಸೇರಿಸಿ.ts
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

- ಎಲ್ಲಾ ಸಾಧನ ಕರೆಗಳನ್ನು ನಿಭಾಯಿಸುವ ಹ್ಯಾಂಡ್ಲರ್‌ನಲ್ಲಿ, ಬರುವ ವಿನಂತಿಯು ಸಾಧನ ವ್ಯಾಖ್ಯಾನಿಸುವ ಪಠ್ಯ ರೂಪಕ್ಕೆ ಪರಿಗಣಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ಅದು ಕಾರ್ಯಗತವಾಗಿದ್ದರೆ ನಿಜವಾದ ಸಾಧನವನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ:

    ```typescript
    const result = await tool.callback(input);
    ```

ನೋಡಿದಂತೆ, ಈ ವಿಧಾನವು ಅದ್ಭುತ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಎಲ್ಲವನ್ನೂ ತನ್ನ ತನ್ನ ಸ್ಥಳದಲ್ಲಿ ಇಡುತ್ತದೆ, *server.ts* ಒಂದು ಚಿಕ್ಕ ಫೈಲ್ ಮಾತ್ರವಾಗಿದೆ ಇದು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಮಾತ್ರ ಸಂಪರ್ಕಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯವು ತಕ್ಕ ತಕ್ಕ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಇರುತ್ತದೆ ಉದಾಹರಣೆಗೆ tools/, resources/ ಅಥವಾ /prompts.

ಅದ್ಭುತ, ಮುಂದುವರೆದು ಇದನ್ನು ನಿರ್ಮಿಸೋಣ.

## ವ್ಯಾಯಾಮ: ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ರಚನೆ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ನಾವು ಹೀಗೆ ಮಾಡುತ್ತೇವೆ:

1. ಸಾಧನಗಳ ಪಟ್ಟಿ ಮಾಡುವುದು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡುವುದನ್ನು ನಿಭಾಯಿಸುವ ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ರಚಿಸಿ.
1. ನೀವು ಉಪಯೋಗಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.
1. ನಿಮ್ಮ ಸಾಧನಗಳ ಕರೆಗಳನ್ನು ಸರಿಯಾಗಿ ಪರಿಶೀಲಿಸಲು ವ ಸೂಪಶೀಲನೆಯನ್ನು ಸೇರಿಸಿ.

### -1- ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸು

ನಾವು ಮಾರುಕಟ್ಟೆಯನ್ನು ಪಿಗಿಸಲಾಗುವುದು ಎಂದರೆ, ಹೆಚ್ಚುವರಿ ಲಕ್ಷಣಗಳನ್ನು ಸೇರಿಸಿದಂತೆ ವಿಸ್ತಾರಗೊಳ್ಳುವ ವಾಸ್ತುಶಿಲ್ಪ ಇದಾಗಿದೆ, ಹೀಗಿದೆ:

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

ಈಗ ನಾವು ಒಂದು ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಹೊಂದಿದ್ದೇವೆ ಇದು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಹೊಸ ಸಾಧನಗಳನ್ನು ಸುಲಭವಾಗಿ ಸೇರಿಸಲು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ. resource ಮತ್ತು prompt ಉಪಡೈರೆಕ್ಟರಿಗಳನ್ನು ಸೇರಿಸಲು ನೀವು ಇದನ್ನು ಅನುಸರಿಸಬಹುದು.

### -2- ಸಾಧನವನ್ನು ರಚಿಸುವುದು

ಮುಂದಿಗೆ ನೋಡೋಣ ಸಾಧನವನ್ನು ರಚಿಸುವುದು ಹೇಗಿದೆ. ಮೊದಲಿಗೆ, ಅದು ತನ್ನ *tool* ಉಪಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ರಚಿಸಬೇಕು ಹೀಗೆ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # ಪೈಡ್ಯಾಂಟಿಕ್ ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಮಾನ್ಯತೆ ನೀಡಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ಪೈಡ್ಯಾಂಟಿಕ್ ಅನ್ನು ಸೇರಿಸಿ, ಆದ್ದರಿಂದ ನಾವು AddInputModel ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಆರ್ಗ್ಸ್ ಅನ್ನು ಮಾನ್ಯತೆಗೊಳಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ಇಲ್ಲಿ ನಾವು ಹೆಸರನ್ನು, ವಿವರಣೆಯನ್ನು ಮತ್ತು ಪೈಡ್ಯಾಂಟಿಕ್ ಉಪಯೋಗಿಸಿ ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತೇವೆ ಮತ್ತು ಈ ಸಾಧನ ಕರೆ ಮಾಡಿದಾಗ invoked ಆಗುವ ಹ್ಯಾಂಡ್ಲರ್ ಇರುತ್ತದೆ. ಕೊನೆಯಲ್ಲಿ, `tool_add` ಎಂಬ ಡಿಕ್ಷನರಿ ಹೊಂದಿದ್ದು ಇದರಲ್ಲಿ ಈ ಎಲ್ಲಾ ಗುಣ ಲಕ್ಷಣಗಳಿವೆ.

ಜೊತೆಗೆ *schema.py* ಇದೆ ಇದು ಸಾಧನದ ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾ ವಿವರಿಸುವುದಕ್ಕೆ ಬಳಸಿಕೊಳ್ಳಲಾಗುತ್ತದೆ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ಅನ್ನು ಕೂಡ ತುಂಬಿಸುವ ಅಗತ್ಯವಿದೆ ಯಾಕೆಂದರೆ tools ಡೈರೆಕ್ಟರಿಯನ್ನು ಒಂದು ಮాడ್ಯೂಲ್ ಆಗಿ ಪರಿಗಣಿಸಲು. ಜೊತೆಗೆ ಅದರಲ್ಲಿ ಇರುವ ಮಾರುಕಟ್ಟೆಗಳಿಗನುಗುಣವಾಗಿ ಹೊರತಗೆಯಬೇಕು:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ನಾವು ಈ ಫೈಲಿಗೆ ಹೊಸ ಸಾಧನಗಳನ್ನು ಸೇರಿಸಬಹುದು.

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

- ಹೆಸರು, ಇದು ಸಾಧನದ ಹೆಸರು.
- rawSchema, ಇದು Zod ಸ್ಕೀಮಾ, ಇದು ಸಾಧನವನ್ನು ಕರೆಯಲು ಬರುವ ವಿನಂತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.
- inputSchema, ಈ ಸ್ಕೀಮಾ ಹ್ಯಾಂಡ್ಲರ್ ಬಳಕೆಗಾಗಿ.
- callback, ಇದು ಸಾಧನವನ್ನು invoke ಮಾಡಲು ಬಳಕೆಯಾಗುತ್ತದೆ.

`Tool` ಕೂಡ ಇದೆ ಇದು ಈ ಡಿಕ್ಷನರಿಯನ್ನು mcp ಸರ್ವರ್ ಹ್ಯಾಂಡ್ಲರ್ ಅಂಗೀಕರಿಸುವ ರೀತಿಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ ಹಾಗೆ ಇದೆ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ಮತ್ತು *schema.ts* ಇದೆ ಇಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಸಾಧನಕ್ಕೆ ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾಗಳನ್ನು ಸಂಗ್ರಹಿಸುತ್ತೇವೆ, ಈಗಾಗಲೇ ಒಂದು ಸ್ಕೀಮಾ ಇದೆ ಆದರೆ ನವ ಸಾಧನಗಳನ್ನು ಸೇರಿಸಿದ್ದಂತೆ entries ಹೆಚ್ಚಿಸಬಹುದು:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ಅದ್ಭುತ, ಈಗ ನಾವು ಸಾಧನ ಪಟ್ಟಿ ಮಾಡುವುದನ್ನು ನಿಭಾಯಿಸೋಣ.

### -3- ಸಾಧನ ಪಟ್ಟಿ ನಿಭಾಯಿಸಿ

ನಂತರ, ಸಾಧನವನ್ನು ಪಟ್ಟಿ ಮಾಡಲು ನಾವು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ನಿಯೋಜಿಸಬೇಕು. ಅದನ್ನೂ ನಮ್ಮ ಸರ್ವರ್ ಫೈಲ್‌ಗೆ ಸೇರಿಸಬೇಕು:

**Python**

```python
# ಸಂಕ್ಷಿಪ್ತಕ್ಕೆ ಕೋಡ್ ಆಳವಟ್ಟಿ ಮಾಡಲಾಗಿದೆ
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

ಇಲ್ಲಿ, ನಾವು `@server.list_tools` ಡೆಕೊರೇಟರ್ ಸೇರಿಸಿ `handle_list_tools` ಕಾರ್ಯ ನಿರ್ವಹಿಸುತ್ತೇವೆ. ಇದರಲ್ಲಿ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ತಯಾರಿಸಲು ಅಗತ್ಯವಿದೆ. ಪ್ರತಿಯೊಂದು ಸಾಧನದ ಹೆಸರ, ವಿವರಣೆ ಮತ್ತು inputSchema ಇರಬೇಕು.   

**TypeScript**

ಸಾಧನ ಪಟ್ಟಿ ಮಾಡುವ ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಸೃಜಿಸಲು, ನಾವು ಸರ್ವರ್‌ನಲ್ಲಿ `setRequestHandler` ಕರೆದಿಟ್ಟು schema ವನ್ನು `ListToolsRequestSchema` ಎಂದರೆ ನಿಗದಿಪಡಿಸಲು ಬೇಕು. 

```typescript
// ಇನ್ದೆಕ್ಸ.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// ಸರ್ವರ್.ts
// ಸಂಕ್ಷಿಪ್ತವಾಗಿ ಕೋಡ್ ಬಿಡಲಾಗಿದೆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ನೋಂದಾಯಿಸಲಾದ ಟೂಲ್ಸ್ ಪಟ್ಟಿಯನ್ನು ಹಂಚಿಸಿ
  return {
    tools: tools
  };
});
```

ಅದ್ಭುತ, ಈಗ ಸಾಧನ ಪಟ್ಟಿ ಮಾಡುವ ಭಾಗವನ್ನು ಊಕಾದೊಡನೆ ನಡೆಸಿದೆವು, ಈಗ ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡುವುದೇನು ಹೇಗಿದ್ದು ನೋಡೋಣ.

### -4- ಸಾಧನವನ್ನು ಕರೆ ಮಾಡುವುದನ್ನು ನಿಭಾಯಿಸಿ

ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಲು ಮತ್ತೊಂದು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಬೇಕು, ಇದರಲ್ಲಿ ಬರೋ ವಿನಂತಿಯು ಯಾವ ಸ_feature_ ಅನ್ನು ಕರೆಮಾಡಬೇಕು ಮತ್ತು ಯಾವ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಎಂಬುದು ಸೂಚಿಸಲಾಗಿದೆ.

**Python**

ನಾವು `@server.call_tool` ಡೆಕೊರೇಟರ್ ಬಳಸಿ `handle_call_tool` ಎಂಬ ಕಾರ್ಯ ತಯಾರಿಸೋಣ. ಆ ಕಾರ್ಯದಲ್ಲಿ ನಾವು ಸಾಧನದ ಹೆಸರನ್ನು, ಆರ್ಗ್ಯುಮೆಂಟ್ ಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಆರ್ಮ್ಯುಮೆಂಟ್‌ಗಳು ಸರಳವಾಗಿವೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು. ಆರ್ಮ್ಯುಮೆಂಟ್‌ಗಳ ಪರಿಶೀಲನೆ ಈ ಕಾರ್ಯದಲ್ಲೇ ಅಥವಾ ನಿಜವಾದ ಸಾಧನದ ಒಳಗೆ ಕೂಡ ನಡೆಯಬಹುದು.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಸಲಕರಣೆ ಹೆಸರುಗಳನ್ನು ಕೀಲಿಗಳಾಗಿಳ್ಳ ಸಾರಣಿ
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ಸಲಕರಣೆಯನ್ನು ಕರೆಮಾಡಿ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ಇದರಿಂದ ನಡೆಯುವದು:

- ನಮ್ಮ ಸಾಧನ ಹೆಸರಿನ ಇನ್‌ಪುಟ್ ಪರಿಮಾಣ `name` ಇರುತ್ತದೆ ಮತ್ತು ಆರ್ಮ್ಯುಮೆಂಟ್‌ಗಳ `arguments` ಡಿಕ್ಷನರಿಯ ರೂಪದಲ್ಲಿ ಇರುತ್ತದೆ.

- `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ಅನುಷ್ಠಾನದಿಂದ ಸಾಧನ ಕರೆ ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಕಾರ್ಯದಲ್ಲಿ ಆರ್ಮ್ಯುಮೆಂಟ್‌ಗಳ ಪರಿಶೀಲನೆ ಸದ್ಯದಲ್ಲೇ (handler ಗುಣಲಕ್ಷಣದಲ್ಲಿ) ನಡೆಯುತ್ತದೆ, ದೋಷ ಬಂದರೆ ಹೊರಗಿನ ತೊಂದರೆ ಉಂಟಾಗುತ್ತದೆ.

ಇಂತಿ, ನಾವು ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ಬಳಸಿ ಸಾಧನಗಳ ಪಟ್ಟಿ ಮತ್ತು ಕರೆ ಮಾಡುವುದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇವೆ.

ಪೂರ್ಣ ಉದಾಹರಣೆಯನ್ನು [ಇಲ್ಲಿ](./code/README.md) ನೋಡಿ

## ನಿಯೋಜನೆ

ನಿಮಗೆ ನೀಡಲಾದ ಕೋಡ್ ಅನ್ನು ಹಲವು ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಸೇರಿಸಿ ವಿಸ್ತರಿಸಿ ಮತ್ತು ಗಮನಿಸಿ ನೀವು tools ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಮಾತ್ರ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸಬೇಕು ಮತ್ತು ಇನ್ಯಾವುದೂ ಬೇಡ.

*ಯಾವುದೂ ಪರಿಹಾರ ನೀಡಲಾಗಿಲ್ಲ*

## ಸಾರಾಂಶ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ ನಾವು ಕಡಿಮೆ-ಪದರದ ಸರ್ವರ್ ವಿಧಾನ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಅದರಿಂದ ನಾವು ಹೇಗೆ ಒಳ್ಳೆಯ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರೂಪಿಸಬಹುದು ಎಂದು ನೋಡಿದ್ದೇವೆ. ಪರಿಶೀಲನೆಯ ಬಗ್ಗೆ ಚರ್ಚೆ ಮಾಡಿದೆವು ಮತ್ತು ಪರಿಚಯಿಸಲ್ಪಟ್ಟಿದ್ದೇವೆ ಹೇಗೆ ಪರಿಶೀಲನಾ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಇನ್‌ಪುಟ್ ಪರಿಶೀಲನೆಯಿಗಾಗಿ ಸ್ಕೀಮಾ ಸೃಷ್ಟಿಸಲು.

## ಮುಂದೇನು

- ಮುಂದಿನದು: [ಸರಳ ಪ್ರಮಾಣೀಕರಣೆ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
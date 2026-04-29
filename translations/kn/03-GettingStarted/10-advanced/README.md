# ಉನ್ನತ ಸರ್ವರ್ ಬಳಕೆ

MCP SDK ಯಲ್ಲಿ ಎರಡು ವಿಭಿನ್ನ ಪ್ರಕಾರದ ಸರ್ವರ್‌ಗಳು ಲಭ್ಯವಿವೆ, ನಿಮ್ಮ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್. ಸಾಮಾನ್ಯವಾಗಿ, ನೀವು ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಬಳಸಿ ಅದಕ್ಕೆ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸುತ್ತೀರಿ. ಆದರೆ ಕೆಲ ಸಂದರ್ಭಗಳಲ್ಲಿ, ನೀವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಮೇಲೆ ಅವಲಂಬಿಸಬೇಕಾಗುತ್ತದೆ ಉದಾಹರಣೆಗೆ:

- ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪ. ಎರಡೂ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಬಳಸಿ ಶುದ್ಧ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸೃಷ್ಟಿಸುವುದು ಸಾಧ್ಯವಾಗುತ್ತದೆ ಆದರೆ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಜೊತೆಗೆ ಸ್ವಲ್ಪ ಸುಲಭ ಎಂದು ವಾದಿಸಬಹುದು.
- ವೈಶಿಷ್ಟ್ಯ ಲಭ್ಯತೆ. ಕೆಲವು ಉನ್ನತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕೇವಲ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಬಳಸಿ ಮಾತ್ರ ಬಳಸಬಹುದು. ನಾವು ನಂತರದ ಅಧ್ಯಾಯಗಳಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮತ್ತು ಎಲಿಸಿಟೇಶನ್ ಸೇರಿಸುವಾಗ ನೀವು ಇದನ್ನು ನೋಡಬಹುದು.

## ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್

ಇಲ್ಲಿ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ಅನ್ನು ರಚಿಸುವುದು ಹೀಗಿದೆ

**Python**

```python
mcp = FastMCP("Demo")

# ಸೇರಿಸುವ ಸಲಕರಣೆ ಸೇರಿಸಿ
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

// ಒಂದು ಸೇರ್ಸು ಸಾಧನವನ್ನು ಸೇರಿಸಿ
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

ಮುಖ್ಯಾಂಶವೇನೆಂದರೆ ನೀವು ಸರ್ವರ್‌ಗೆ ಬೇಕಾಗುವ ಪ್ರತಿ ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಸೇರಿಸುತ್ತೀರಿ. ಅದರಲ್ಲಿ ಯಾರಾದರೂ ತಪ್ಪಿಲ್ಲ.  

### ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ

ಆದರೆ, ನೀವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ ಬಳಸುವಾಗ ನೀವು ಭಿನ್ನವಾಗಿ ಯೋಚಿಸಬೇಕಾಗುತ್ತದೆ. ಪ್ರತಿ ಸಾಧನವನ್ನು ಪಂಜೀಕರಿಸುವ ಬದಲು, ನೀವು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯ ಪ್ರಕಾರಕ್ಕೆ (ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಅಥವಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳು) ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ರಚಿಸಬೇಕು. ಉದಾಹರಣೆಗೆ ಸಾಧನಗಳಿಗೆ ಹೀಗೆ ಎರಡು ಕಾರ್ಯಗಳು ಇರುತ್ತವೆ:

- ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು. ಒಂದು ಕಾರ್ಯ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು ಜವಾಬ್ದಾರಿಯಾಗಿ ಇರುತ್ತದೆ.
- ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವುದನ್ನು ನಿರ್ವಹಿಸುವುದು. ಇಲ್ಲಿ ಕೂಡ, ಒಂದು ಕಾರ್ಯ ಮಾತ್ರ ಒಂದು ಸಾಧನವನ್ನು ಕರೆಮಾಡುವ ಕೋರಿಕೆಯನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡುತ್ತದೆ

ಇದು ಕಡಿಮೆ ಕೆಲಸವಾಗಬಹುದು ಎನ್ನಿಸುವುದು ಸಾದ್ಯವಿದೆ ಅಲ್ಲವೇ? ಹೀಗಾಗಿ ಸಾಧನವನ್ನು ಪಂಜೀಕರಿಸುವ ಬದಲು, ನಾನು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವಾಗ ಸಾಧನ ಪಟ್ಟಿ ಆಗಿರಬೇಕು ಮತ್ತು ಸಾಧನವನ್ನು ಕರೆಮಾಡಬೇಕಾದಾಗ ಅದು ಕರೆಮಾಡಲ್ಪಡಬೇಕು ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು. 

ನೋಡಿ, ಈಗ ಕೋಡ್ ಹೇಗೆ ಕಾಣಿಸುತ್ತದೆ:

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
  // ನೋಂದಾಯಿಸಲಾದ ಉಪಕರಣಗಳ ಪಟ್ಟಿ ಹಿಂತಿರುಗಿಸಿ
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

ಇಲ್ಲಿ ನಾವು ವೈಶಿಷ್ಟ್ಯಗಳ ಪಟ್ಟಿ ನೀಡುವ ಒಂದು ಕಾರ್ಯವನ್ನು ಹೊಂದಿದ್ದೇವೆ. ಸಾಧನಗಳ ಪಟ್ಟಿಯ ಪ್ರತಿ ಎಂಟ್ರಿಯಲ್ಲಿ `name`, `description`, ಮತ್ತು `inputSchema` ಎಂಬ ಕ್ಷೇತ್ರಗಳು ಇವೆ, ಇದು ರಿಟರ್ನ್ ಪ್ರಕಾರಕ್ಕೆ ಅನುಗುಣವಾಗಿದೆ. ಇದರಿಂದ ನಮ್ಮ ಸಾಧನಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ವ್ಯಾಖ್ಯಾನವನ್ನು ಬೇರೆಲ್ಲೆ ಇರಿಸಬಹುದು. ಈಗ ನಾವು ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ರಚಿಸಬಹುದು ಮತ್ತು ಅದೇ ಬಗೆನೆ દરેક ವೈಶಿಷ್ಟ್ಯಗಳಿಗೆ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಈ ರೀತಿ ವ್ಯವಸ್ಥಿತವಾಗಬಹುದು:

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

ಅದ್ಭುತ, ನಮ್ಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ತುಂಬಾ ಶುದ್ಧವಾಗಿಸುವಂತೆ ಮಾಡಬಹುದು.

ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವುದು ಹೇಗೆ, ಅದೇ գաղափಾರವೇ, ಒಂದು ಹ್ಯಾಂಡ್ಲರ್ ಎಲ್ಲ ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡಲು ಬಳಸುವುದು? ಹೌದು, ಖಚಿತವಾಗಿ, ಇದಕ್ಕೆ ಕೋಡ್ ಇಲ್ಲಿದೆ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಅನ್ನೋದು ಸಾಧನಗಳ ಹೆಸರನ್ನು ಕೀಲಿಗಳಾಗಿ ಹೊಂದಿರುವ ನಿಘಂಟು ಆಗಿದೆ
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
    // TODO ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

ಮೇಲಿನ ಕೋಡ್ ನೋಡಿದರೆ, ನಾವು ಕರೆಮಾಡಬೇಕಾದ ಸಾಧನವನ್ನು ಮತ್ತು ಅದಕ್ಕೆ ಯಾವುದೇ ಆರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳಿರಬಹುದೋ ಅವುಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಬೇಕು ಮತ್ತು ನಂತರ ಸಾಧನವನ್ನು ಕರೆಮಾಡಬೇಕು.

## ಮಾನ್ಯತೆ ಸಹಿತ ವಿಧಾನ ಸುಧಾರಣೆ

ಇಲ್ಲಿಯವರೆಗೆ, ನಿಮ್ಮ ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಸೇರಿಸುವ ಎಲ್ಲಾ ನೋಂದಣಿಗಳನ್ನು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯ ಪ್ರಕಾರಕ್ಕೆ ಈ ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳ ಮೂಲಕ ಬದಲಿ ಮಾಡಬಹುದು. ಇನ್ನೇನು ಮಾಡಬೇಕಾಗಿದೆ? ನಾವು ಸಾಧನವನ್ನು ಸರಿಯಾದ ಆರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಕರೆಮಾಡಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಲು ಒಂದು ವಿಧದ ಮಾನ್ಯತೆ ಸೇರಿಸಬೇಕು. ಪ್ರತಿ ರನ್‌ಟೈಮ್ ತನ್ನದೇ ಪರಿಹಾರವನ್ನು ಹೊಂದಿದೆ, ಉದಾಹರಣೆಗೆ Python ನಲ್ಲಿ Pydantic ಅನ್ನು ಮತ್ತು TypeScript ನಲ್ಲಿ Zod ಬಳಸಲಾಗುತ್ತದೆ. අදೇಶವೆಂದರೆ:

- ವೈಶಿಷ್ಟ್ಯ (ಸಾಧನ, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್) ರಚನೆಗೆ ಸಂಬಂಧಿಸಿದ ತರ್ಕವನ್ನು ಅದರ ನಿರ್ದಿಷ್ಟ ಫೋಲ್ಡರ್‌ಗೆ ಸ್ಥಳಾಂತರಿಸುವುದು.
- ಉದಾಹರಣೆಗೆ ಸಾಧನವನ್ನು ಕರೆಮಾಡುವಂತೆ ಕೇಳುವ ಇನಕಮಿಂಗ್ ಕೋರಿಕೆಯನ್ನು ಮಾನ್ಯ ಮಾಡುವುದು.

### ವೈಶಿಷ್ಟ್ಯ ಸೃಷ್ಟಿ

ವೈಶಿಷ್ಟ್ಯವನ್ನು ರಚಿಸಲು, ಆ ವೈಶಿಷ್ಟ್ಯದ ಫೈಲ್ ರಚಿಸಿ ಅದರ ಅಗತ್ಯವಿರುವ ಕ್ಷೇತ್ರಗಳಿವೆ ಎಂದು ಖಚಿತಪಡಿಸಬೇಕು. ಯಾವ ಕ್ಷೇತ್ರಗಳು ಸಧನ, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳಲ್ಲಿ ವಿಭಿನ್ನವಾಗಿರುತ್ತವೆ.

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
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್ಪುಟ್ ಮಾನ್ಯೀಕರಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಸೇರಿಸಿ, ώστε ನಾವು AddInputModel ನಿರ್ಮಿಸಿ ಆರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳನ್ನು ಮಾನ್ಯೀಕರಿಸಬಹುದು

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

- *schema.py* ಫೈಲ್‌ನಲ್ಲಿ `a` ಮತ್ತು `b` ಕ್ಷೇತ್ರಗಳೊಂದಿಗೆ Pydantic `AddInputModel` ಬಳಸಿ ಸ್ಕೀಮಾವನ್ನು ರಚಿಸುವುದು.
- ಇನಕಮಿಂಗ್ ಕೋರಿಕೆಯನ್ನು `AddInputModel` ಪ್ರಕಾರ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುವುದು, ಇದರಲ್ಲಿ ಪರಿಮಾಣಗಳ ಬಗ್ಗೆ ಅಸಮ್ಮತಿ ಇದ್ದರೆ ಇದು ಕ್ರ್ಯಾಶ್ ಆಗುತ್ತದೆ:

   ```python
   # add.py
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ನೀವು ಈ ಪಾರ್ಸಿಂಗ್ ತರ್ಕವನ್ನು ಸಾಧನ ಕರೆಗೂಡಿನಲ್ಲಿ ಅಥವಾ ಹ್ಯಾಂಡ್ಲರ್ ಕಾರ್ಯದಲ್ಲಿ ಇರಿಸಬಹುದು.

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

// ಸ್ಕೀಮಾ.ts
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

- ಎಲ್ಲಾ ಸಾಧನ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಹ್ಯಾಂಡ್ಲರ್‌ನಲ್ಲಿ, ಇನಕಮಿಂಗ್ ಕೋರಿಕೆಯನ್ನು ಸಾಧನದ ನಿರ್ದಿಷ್ಟ ಸ್ಕೀಮಾಗೆ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ಅದು ಕಾರ್ಯಕ್ಷಮವಾಗಿದ್ದರೆ ನಾವು ನಿಜವಾದ ಸಾಧನವನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ:

    ```typescript
    const result = await tool.callback(input);
    ```

ನೀವು ನೋಡಬಹುದು, ಈ ವಿಧಾನ ಒಂದು ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಪ್ರತಿಯೊಂದು ವಿಷಯಕ್ಕೂ ಅದರ ಸ್ವತಂತ್ರ ಸ್ಥಳವಿದೆ, *server.ts* ಒಂದು ಬಹಳ ಸಣ್ಣ ಫೈಲ್ ಆಗಿದ್ದು ಕೇವಲ ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಸಂಪರ್ಕಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯವು ತನ್ನ ಸೂಕ್ತ ಫೋಲ್ಡರ್‌ಗಳಲ್ಲಿ ಇರುತ್ತದೆ ಉದಾ: tools/, resources/ ಅಥವಾ prompts/.

ಉತ್ತಮ, ಈಗ ಈಗಿನಿಂದ ನಿರ್ಮಿಸಲು ಪ್ರಯತ್ನಿಸೋಣ.

## ಅಭ್ಯಾಸ: ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ರಚನೆ

ಈ ಅಭ್ಯಾಸದಲ್ಲಿ, ನಾವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡುತ್ತೇವೆ:

1. ಸಾಧನಗಳ ಪಟ್ಟಿ ಮಾಡುವುದು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ನಿರ್ಮಿಸುವುದು.
2. ನೀವು ಸುಗಮವಾಗಿ ನಿರ್ಮಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.
3. ನಿಮ್ಮ ಸಾಧನ ಕರೆಗಳು ಸರಿಯಾಗಿ ಮಾನ್ಯಕರಿಸಲ್ಪಟ್ಟಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಲು ಮಾನ್ಯತೆ ಸೇರಿಸುವುದು.

### -1- ವಾಸ್ತುಶಿಲ್ಪ ರಚನೆ

ಮೊದಲ ವಿಷಯವೆಂದರೆ, ನಾವು ಹೆಚ್ಚು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸುವಾಗ ನಮಗೆ ಸಹಾಯಕವಾಗುವ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಆಧರಿಸಬೇಕು, ಹೀಗಿದೆ ಅದು:

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

ಈಗ ನಾವು ಒಂದು ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಕೊಂಡೊಯ್ದಿದ್ದೇವೆ, ಇದು ಸಾಧನಗಳನ್ನು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಸುಲಭವಾಗಿ ಸೇರಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ. resources ಮತ್ತು prompts ಗೆ ಉಪಡೈರೆಕ್ಟರಿಗಳನ್ನು ಸೇರಿಸಲು ಇದನ್ನು ಅನುಸರಿಸಬಹುದು.

### -2- ಸಾಧನ ರಚನೆ

ಮುಂದೆ ಸಾಧನವನ್ನು ರಚಿಸುವುದು ಹೇಗೆ ನೋಡೋಣ. ಮೊದಲು, ಅದು ತನ್ನ *tool* ಉಪಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ರಚಿಸಬೇಕು ಹೀಗೆಯೆ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್ಪುಟ್ ಪರಿಶೀಲಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಅನ್ನು ಸೇರಿಸು, ώστε ನಾವು AddInputModel ರಚಿಸಿ ಆರ್ಗ್ಸ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ನೀವು ಇಲ್ಲಿ ನೋಡುತ್ತಿರುವುದು નામ, ವರ್ಣನೆ, ಮತ್ತು Pydantic ಬಳಸಿ input schema ಅನ್ನು ಹೇಗೆ ವ್ಯಾಖ್ಯಾನಿಸುವುದು ಮತ್ತು ಈ ಸಾಧನವನ್ನು ಕರೆಮಾಡುವಾಗ ಹ್ಯಾಂಡ್ಲರ್ ಹೇಗೆ ಕರೆಮಾಡುತ್ತದೆ ಎಂದು.

ಕೊನೆಗೆ, ಈ ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಹೊರುವ ಡಿಕ್ಷನರಿ ಆದ `tool_add` ಅನ್ನು ಹೊರಗೊಳ್ಳಿಸಲಾಗುತ್ತದೆ.

*schema.py* ಫೈಲ್ ಕೂಡ ಇದಕ್ಕೆ ಇನಪುಟ್ ಸ್ಕೀಮಾ ವ್ಯಾಖ್ಯಾನಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ಫೈಲ್ ಅನ್ನು ತುಂಬಿಸಬೇಕಾಗುತ್ತದೆ ताकि tools ಡೈರೆಕ್ಟರಿ ಒಂದು ಮೊಡಿಯುಲ್ ಆಗಿ ವ್ಯವಹರಿಸಬೇಕು. ಜೊತೆಗೆ ಮಡ್ಯೂಲ್ ಗಳನ್ನು ಹೀಗೆ ಹೊರಗೆ ಹೊರಡಿಸಬೇಕು:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ನಾವು ಹೆಚ್ಚು ಸಾಧನಗಳನ್ನು ಸೇರಿಸುವಂತೆ ಈ ಫೈಲ್ ಅನ್ನು ಮುಂದುವರೆಸಬಹುದು.

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

- name, ಇದು ಸಾಧನದ ಹೆಸರು.
- rawSchema, ಇದು Zod ಸ್ಕೀಮಾ, ಇದು ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಬೇಕಾದ ಇನಕಮಿಂಗ್ ಕೋರಿಕೆಯನ್ನು ಮಾನ್ಯಗೊಳಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.
- inputSchema, ಈ ಸ್ಕೀಮವನ್ನು ಹ್ಯಾಂಡ್ಲರ್ ಬಳಸುತ್ತದೆ.
- callback, ಇದು ಸಾಧನವನ್ನು ಕರೆಮಾಡಲು ಉಪಯುಕ್ತವಾಗಿದೆ.

`Tool` ಕೂಡ ಇದೆ, ಇದು ಈ ಡಿಕ್ಷನರಿಯನ್ನು mcp ಸರ್ವರ್ ಹ್ಯಾಂಡ್ಲರ್ ಸ್ವೀಕರಿಸುವ ಪ್ರಕಾರಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ, ಹೀಗೆ ಕಾಣುತ್ತದೆ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ಮತ್ತು *schema.ts* ಇಲ್ಲಿ ನಾವು ಪ್ರತಿ ಸಾಧನಕ್ಕಾಗಿ ಇನಪುಟ್ ಸ್ಕೀಮಾಗಳನ್ನು ಇಡುತ್ತೇವೆ, ಪ್ರಸ್ತುತ ಒಂದೇ ಸ್ಕೀಮಾ ಇದೆ ಆದರೆ ನಾವು ಸಾಧನಗಳನ್ನು ಸೇರಿಸುವಾಗ entries ಹೆಚ್ಚಿಸಬಹುದು:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ಉತ್ತಮ, ಈಗ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ನಿರ್ವಹಿಸುವುದಕ್ಕೆ ಮುಂದಾಗೋಣ.

### -3- ಸಾಧನ ಪಟ್ಟಿ ನಿರ್ವಹಣೆ

ಮುಂದೆ ನಾವು ಸಾಧನ ಪಟ್ಟಿ ನಿರ್ವಹಿಸಲು ಕೋರಿಕೆ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಸಿದ್ಧಪಡಿಸಬೇಕು. ಅದಕ್ಕಾಗಿ ನಮ್ಮ ಸರ್ವರ್ ಫೈಲ್‌ಗೆ ಈ ಕೆಳಗಿನುದನ್ನು ಸೇರಿಸಬೇಕು:

**Python**

```python
# ಸರಳಿಕರಣಕ್ಕಾಗಿ ಕೋಡ್ ಅನ್ನು ತೆಗೆದುಹಾಕಲಾಗಿದೆ
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

ಇಲ್ಲಿ ನಾವು `@server.list_tools` ಡೆಕೋರೇಟರ್ ಅನ್ನು ಸೇರಿಸಿ `handle_list_tools` ಕಾರ್ಯವನ್ನು ಅನುಷ್ಟಿಸುತ್ತೇವೆ. ಇದರೊಳಗೆ ನಾವು ಸಾಧನಗಳ ಪಟ್ಟಿ ಸೃಷ್ಟಿಸಬೇಕು. ಪ್ರತಿ ಸಾಧನ ಹೇಗೆ ಕೂಡಲೇ ಒಂದು ಹೆಸರು, ವರ್ಣನೆ ಮತ್ತು inputSchema ಇರಬೇಕು.

**TypeScript**

ಸಾಧನ ಪಟ್ಟಿ ಮಾಡಲು ಬೇಕಾದ ಕೋರಿಕೆಗೆ ಹ್ಯಾಂಡ್ಲರ್ ಸಿದ್ಧಪಡಿಸಲು, ನಾವು ಸರ್ವರ್‌ನಲ್ಲಿ `setRequestHandler` ಅನ್ನು `ListToolsRequestSchema` ಸ್ಕೀಮಾರೊಂದಿಗೆ ಕರೆಯುತ್ತೇವೆ. 

```typescript
// ಸೂಚ್ಯಂಕ.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// ಸರ್ವರ್.ts
// ಸಂಕ್ಷಿಪ್ತತೆಗಾಗಿ ಕೋಡ್ ಮರೆಮಾಡಲಾಗಿದೆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ನೋಂದಾಯಿಸಿದ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
  return {
    tools: tools
  };
});
```

ಉತ್ತಮ, ಈಗ ನಾವು ಸಾಧನ ಪಟ್ಟಿ ಮಾಡಲು ಬಿಡಿದೇವೆ, ಮುಂದೆ ಸಾಧನಗಳನ್ನು ಹೇಗೆ ಕರೆ ಮಾಡಬಹುದು ಅಂತ ನೋಡೋಣ.

### -4- ಸಾಧನ ಕರೆ ನಿರ್ವಹಣೆ

ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಲು, ಮತ್ತೊಂದು ಕೋರಿಕೆ ಹ್ಯಾಂಡ್ಲರ್ ಸಿದ್ಧಪಡಿಸಬೇಕು, ಇದು ಎಂಥ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಕರೆಮಾಡಬೇಕೆಂದು ಸೂಚಿಸುವ ಹಾಗೂ ಆರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳೊಡನೆ ಕೋರಿಕೆಯ ನಿರ್ವಹಣೆಗೆ ಕೇಂದ್ರೀಕೃತವಾದುದು.

**Python**

`@server.call_tool` ಡೆಕೋರೇಟರ್ ಬಳಸಿ `handle_call_tool` ಎಂಬ ಕಾರ್ಯವನ್ನು ಅನುಷ್ಟಿಸೋಣ. ಆ ಕಾರ್ಯದೊಳಗೆ ಸಾಧನದ ಹೆಸರು, ಅದರ ಪರಿಮಾಣಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಲು ಮತ್ತು ಆ ಪರಿಮಾಣಗಳು ಪ್ರಮಾಣಪತ್ರಗಳಾಗಿವೆ ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸಬೇಕು. ನಾವು ಈ ಮಾನ್ಯತೆ ಕಾರ್ಯದಲ್ಲಿ ಅಥವಾ ಸಾಧನದ ತುದಿಯಲ್ಲಿ ಕೂಡಾ ಮಾಡಿ ಇರಬಹುದು.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಸಾಧನಗಳ ಹೆಸರುಗಳನ್ನು ಕೀಲಿಗಳಾಗಿ ಹೊಂದಿರುವ ನಿಘಂಟು
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ನೀವು ತಿಳಿಯಿರಿ:

- ನಮ್ಮ ಸಾಧನ ಹೆಸರು ಇನಪುಟ್ ಮೌಲ್ಯ `name` ಆಗಿದೆ ಮತ್ತು `arguments` ಡಿಕ್ಷನರಿಯಲ್ಲಿ ಇರುವ ನಮ್ಮ ವಿವರಣೆಗಳಿಗಾಗಿ.

- ಸಾಧನವನ್ನು `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ಎಂದು ಕರೆ ಮಾಡುತ್ತದೆ. ಪರಿಮಾಣಗಳ ಮಾನ್ಯತೆ `handler` ಗುಣಲಕ್ಷಣದಲ್ಲಿ ಆಗುತ್ತದೆ, ಇದು ಕಾರ್ಯಕ್ಕೆ ಸೂಚಿಸುತ್ತದೆಯೆ, ಅದು ವಿಫಲವಾದರೆ ತಪ್ಪು ಎದ್ದು ಬರುತ್ತದೆ.

ಈಗ ನಾವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಉದಾಹರಣೆಯಾಗಿ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋದು ಮತ್ತು ಕರೆ ಮಾಡೋದು ಸಂಪೂರ್ಣವಾಗಿ ತಿಳಿಯಿತು.

ಪೂರ್ಣ ಉದಾಹರಣೆಯನ್ನು ಇಲ್ಲಿ ನೋಡಿ [full example](./code/README.md)

## ಹಸ್ತಾಂತರ

ನೀವು ಪಡೆದ ಕೋಡನ್ನು ಹೆಚ್ಚು ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ವಿಸ್ತರಿಸಿ ಮತ್ತು ನೀವು ಗಮನಿಸಬೇಕಾದದ್ದು tools ಡೈರೆಕ್ಟರಿಯಲ್ಲೇ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸುವುದಾದರೆ ಇತರ ಕಡೆ ಅಲ್ಲ ಎಂಬುದಾಗಿದೆ. 

*ಯಾವುದೇ ಪರಿಹಾರ ನೀಡಲಾಗಿಲ್ಲ*

## ಸಂಕಷ್ಟ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನವು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಅದರಿಂದ ನಾವು ಹೇಗೆ ಶುದ್ಧ ವಾಸ್ತುಶಿಲ್ಪ ರಚಿಸಬಹುದು ಅಂತ ನೋಡಿದೆವು. ನಾವು ಮಾನ್ಯತೆ ವಿಷಯವನ್ನೂ ಚರ್ಚಿಸಿಕೊಂಡಿದ್ದೇವೆ ಮತ್ತು ಮಾನ್ಯತೆ ಗ್ರಂಥಾಲಯಗಳೊಂದಿಗೆ ಇನಪುಟ್ ಮಾನ್ಯತೆಗಾಗಿ ಸ್ಕೀಮಾಗಳನ್ನು ರಚಿಸುವ ರೀತಿಯನ್ನು ತೋರಿಸಲಾಗಿದೆ.

## ಮುಂದಿನದ್ದು ಏನು

- ಮುಂದಿನದು: [ಸರಳ ದೃಢೀಕರಣ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಜ್ಯತೆ**:
ಈ փաստಾವಳಿ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲು ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳಿರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಪಠ್ಯದ ಮೂಲ ಭಾಷೆಯ ದಾಖಲೆಯನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸಿಕೊಂಡು ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಧಾರಣೆಗಳು ಅಥವಾ ದುರ್ಭಾಷ್ಯಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
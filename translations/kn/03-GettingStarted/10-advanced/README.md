<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1de8367745088b9fcd4746ea4cc5a161",
  "translation_date": "2025-12-11T12:46:08+00:00",
  "source_file": "03-GettingStarted/10-advanced/README.md",
  "language_code": "kn"
}
-->
# ಅಡ್ವಾನ್ಸ್ಡ್ ಸರ್ವರ್ ಬಳಕೆ

MCP SDK ನಲ್ಲಿ ಎರಡು ವಿಭಿನ್ನ ರೀತಿಯ ಸರ್ವರ್‌ಗಳು ಇವೆ, ನಿಮ್ಮ ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್. ಸಾಮಾನ್ಯವಾಗಿ, ನೀವು ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಅನ್ನು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಬಳಸುತ್ತೀರಿ. ಆದರೆ ಕೆಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ, ನೀವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಮೇಲೆ ಅವಲಂಬಿಸಬೇಕಾಗುತ್ತದೆ, ಉದಾಹರಣೆಗೆ:

- ಉತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪ. ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಎರಡನ್ನೂ ಬಳಸಿಕೊಂಡು ಸ್ವಚ್ಛ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸುವುದು ಸಾಧ್ಯ, ಆದರೆ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಬಳಕೆ ಸ್ವಲ್ಪ ಸುಲಭ ಎಂದು ವಾದಿಸಬಹುದು.
- ವೈಶಿಷ್ಟ್ಯ ಲಭ್ಯತೆ. ಕೆಲವು ಅಡ್ವಾನ್ಸ್ಡ್ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕೇವಲ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಮೂಲಕ ಮಾತ್ರ ಬಳಸಬಹುದು. ನಾವು ನಂತರದ ಅಧ್ಯಾಯಗಳಲ್ಲಿ ಸ್ಯಾಂಪ್ಲಿಂಗ್ ಮತ್ತು ಎಲಿಸಿಟೇಶನ್ ಸೇರಿಸುವಾಗ ಇದನ್ನು ನೋಡುತ್ತೀರಿ.

## ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಮತ್ತು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್

ಸಾಮಾನ್ಯ ಸರ್ವರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ರಚನೆ ಹೇಗಿರುತ್ತದೆ ಎಂಬುದನ್ನು ಇಲ್ಲಿ ನೋಡಬಹುದು

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

// ಒಂದು ಸೇರ್ಪಡೆ ಸಾಧನವನ್ನು ಸೇರಿಸಿ
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

ಮುಖ್ಯ ಅರ್ಥವೆಂದರೆ ನೀವು ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರತಿ ಟೂಲ್, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಸರ್ವರ್‌ಗೆ ಸೇರಿಸುತ್ತೀರಿ. ಇದರಲ್ಲಿ ಯಾವುದೇ ತಪ್ಪಿಲ್ಲ.

### ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ

ಆದರೆ, ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನವನ್ನು ಬಳಸುವಾಗ ನೀವು ವಿಭಿನ್ನವಾಗಿ ಯೋಚಿಸಬೇಕಾಗುತ್ತದೆ, ಅಂದರೆ ಪ್ರತಿ ಟೂಲ್ ಅನ್ನು ನೋಂದಾಯಿಸುವ ಬದಲು, ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯ ಪ್ರಕಾರಕ್ಕೆ (ಟೂಲ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಅಥವಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳು) ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ರಚಿಸುತ್ತೀರಿ. ಉದಾಹರಣೆಗೆ, ಟೂಲ್‌ಗಳಿಗೆ ಎರಡು ಫಂಕ್ಷನ್‌ಗಳು ಇರುತ್ತವೆ:

- ಎಲ್ಲಾ ಟೂಲ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು. ಒಂದು ಫಂಕ್ಷನ್ ಎಲ್ಲಾ ಟೂಲ್ ಪಟ್ಟಿ ಮಾಡುವ ಪ್ರಯತ್ನಗಳಿಗೆ ಹೊಣೆಗಾರ.
- ಎಲ್ಲಾ ಟೂಲ್‌ಗಳನ್ನು ಕರೆ ಮಾಡುವ ಹ್ಯಾಂಡ್ಲರ್. ಇಲ್ಲಿ ಕೂಡ, ಒಂದು ಫಂಕ್ಷನ್ ಮಾತ್ರ ಟೂಲ್ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

ಇದು ಕಡಿಮೆ ಕೆಲಸದಂತೆ ಕಾಣುತ್ತದೆಯೇ? ಆದ್ದರಿಂದ ಟೂಲ್ ನೋಂದಾಯಿಸುವ ಬದಲು, ನಾನು ಎಲ್ಲಾ ಟೂಲ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವಾಗ ಟೂಲ್ ಪಟ್ಟಿ ಆಗಿರಬೇಕು ಮತ್ತು ಟೂಲ್ ಕರೆ ಮಾಡಲು ಬಂದಾಗ ಅದನ್ನು ಕರೆ ಮಾಡಬೇಕು ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು.

ಈಗ ಕೋಡ್ ಹೇಗಿದೆ ನೋಡೋಣ:

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
  // ನೋಂದಾಯಿಸಿದ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
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

ಇಲ್ಲಿ ನಾವು ವೈಶಿಷ್ಟ್ಯಗಳ ಪಟ್ಟಿ ನೀಡುವ ಫಂಕ್ಷನ್ ಹೊಂದಿದ್ದೇವೆ. ಟೂಲ್ ಪಟ್ಟಿ ಪ್ರತಿ ಎಂಟ್ರಿಯಲ್ಲಿ `name`, `description` ಮತ್ತು `inputSchema` ಎಂಬ ಕ್ಷೇತ್ರಗಳಿವೆ, ಇದು ರಿಟರ್ನ್ ಟೈಪ್‌ಗೆ ಅನುಗುಣವಾಗಿದೆ. ಇದರಿಂದ ನಾವು ನಮ್ಮ ಟೂಲ್‌ಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ವ್ಯಾಖ್ಯಾನವನ್ನು ಬೇರೆಡೆ ಇಡಬಹುದು. ಈಗ ನಾವು ಎಲ್ಲಾ ಟೂಲ್‌ಗಳನ್ನು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ರಚಿಸಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಎಲ್ಲಾ ವೈಶಿಷ್ಟ್ಯಗಳಿಗೂ ಇದೇ ರೀತಿ ಮಾಡಬಹುದು, ಆದ್ದರಿಂದ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಹೀಗೆ ಸಂಘಟಿತವಾಗಬಹುದು:

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

ಅದು ಅದ್ಭುತ, ನಮ್ಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಸ್ವಚ್ಛವಾಗಿ ಮಾಡಬಹುದು.

ಟೂಲ್‌ಗಳನ್ನು ಕರೆ ಮಾಡುವುದೇನು, ಅದೇ ಕಲ್ಪನೆ ಅಲ್ಲವೇ, ಒಂದು ಹ್ಯಾಂಡ್ಲರ್ ಎಲ್ಲ ಟೂಲ್‌ಗಳನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ, ಯಾವ ಟೂಲ್ ಆಗಿರಲಿ? ಹೌದು, ನಿಖರವಾಗಿ, ಇದರ ಕೋಡ್ ಇಲ್ಲಿದೆ:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಉಪಕರಣಗಳ ಹೆಸರನ್ನು ಕೀಲಿಗಳಾಗಿ ಹೊಂದಿರುವ ನಿಘಂಟು ಆಗಿದೆ
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

ಮೇಲಿನ ಕೋಡ್‌ನಿಂದ ನೀವು ನೋಡಬಹುದು, ನಾವು ಕರೆ ಮಾಡಬೇಕಾದ ಟೂಲ್ ಮತ್ತು ಅದರ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ, ನಂತರ ಟೂಲ್ ಅನ್ನು ಕರೆ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

## ಮಾನ್ಯತೆ (Validation) ಮೂಲಕ ವಿಧಾನವನ್ನು ಸುಧಾರಿಸುವುದು

ಇದುವರೆಗೆ, ನೀವು ಟೂಲ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸೇರಿಸುವ ಎಲ್ಲಾ ನೋಂದಣಿಗಳನ್ನು ಈ ಎರಡು ಹ್ಯಾಂಡ್ಲರ್‌ಗಳಿಂದ ಬದಲಾಯಿಸಬಹುದು ಎಂದು ನೋಡಿದ್ದೀರಿ. ಇನ್ನೇನು ಮಾಡಬೇಕಾಗುತ್ತದೆ? ನಾವು ಟೂಲ್ ಸರಿಯಾದ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಕರೆ ಮಾಡಲಾಗುತ್ತಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಲು ಕೆಲವು ರೀತಿಯ ಮಾನ್ಯತೆ ಸೇರಿಸಬೇಕು. ಪ್ರತಿ ರನ್‌ಟೈಮ್ ಇದಕ್ಕೆ ತನ್ನದೇ ಪರಿಹಾರವನ್ನು ಹೊಂದಿದೆ, ಉದಾಹರಣೆಗೆ Python ನಲ್ಲಿ Pydantic ಮತ್ತು TypeScript ನಲ್ಲಿ Zod ಬಳಸಲಾಗುತ್ತದೆ. ಕಲ್ಪನೆ ಹೀಗಿದೆ:

- ವೈಶಿಷ್ಟ್ಯ (ಟೂಲ್, ಸಂಪನ್ಮೂಲ ಅಥವಾ ಪ್ರಾಂಪ್ಟ್) ರಚಿಸುವ ಲಾಜಿಕ್ ಅನ್ನು ಅದರ ಸಮರ್ಪಿತ ಫೋಲ್ಡರ್‌ಗೆ ಸ್ಥಳಾಂತರಿಸುವುದು.
- ಉದಾಹರಣೆಗೆ ಟೂಲ್ ಕರೆ ಮಾಡಲು ಬರುವ ವಿನಂತಿಯನ್ನು ಮಾನ್ಯತೆ ಮಾಡುವುದು.

### ವೈಶಿಷ್ಟ್ಯ ರಚನೆ

ವೈಶಿಷ್ಟ್ಯವನ್ನು ರಚಿಸಲು, ನಾವು ಆ ವೈಶಿಷ್ಟ್ಯಕ್ಕೆ ಫೈಲ್ ರಚಿಸಿ ಅದರ ಅಗತ್ಯ ಕ್ಷೇತ್ರಗಳನ್ನು ಹೊಂದಿರಬೇಕು. ಟೂಲ್, ಸಂಪನ್ಮೂಲ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳ ನಡುವೆ ಕೆಲವು ಕ್ಷೇತ್ರಗಳು ಭಿನ್ನವಾಗಿರುತ್ತವೆ.

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
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಅನ್ನು ಸೇರಿಸಿ, ಆದ್ದರಿಂದ ನಾವು AddInputModel ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಆರ್ಗ್‌ಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಬಹುದು

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

- Pydantic `AddInputModel` ಬಳಸಿ schema ರಚಿಸುವುದು, `a` ಮತ್ತು `b` ಕ್ಷೇತ್ರಗಳೊಂದಿಗೆ *schema.py* ಫೈಲ್‌ನಲ್ಲಿ.
- ಬರುವ ವಿನಂತಿಯನ್ನು `AddInputModel` ಪ್ರಕಾರ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುವುದು, ಪ್ಯಾರಾಮೀಟರ್‌ಗಳಲ್ಲಿ ಭಿನ್ನತೆ ಇದ್ದರೆ ಇದು ಕ್ರ್ಯಾಶ್ ಆಗುತ್ತದೆ:

   ```python
   # add.py
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ನೀವು ಈ ಪಾರ್ಸಿಂಗ್ ಲಾಜಿಕ್ ಅನ್ನು ಟೂಲ್ ಕರೆ ಫಂಕ್ಷನ್‌ನಲ್ಲಿ ಅಥವಾ ಹ್ಯಾಂಡ್ಲರ್ ಫಂಕ್ಷನ್‌ನಲ್ಲಿ ಇರಿಸಬಹುದು.

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

- ಎಲ್ಲಾ ಟೂಲ್ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಹ್ಯಾಂಡ್ಲರ್‌ನಲ್ಲಿ, ನಾವು ಈಗ ಬರುವ ವಿನಂತಿಯನ್ನು ಟೂಲ್‌ನ ವ್ಯಾಖ್ಯಾನಿತ schema ಗೆ ಪಾರ್ಸ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ಅದು ಯಶಸ್ವಿಯಾಗಿದ್ರೆ ನಾವು ನಿಜವಾದ ಟೂಲ್ ಅನ್ನು ಕರೆ ಮಾಡುತ್ತೇವೆ:

    ```typescript
    const result = await tool.callback(input);
    ```

ನೀವು ನೋಡಬಹುದು, ಈ ವಿಧಾನವು ಅತ್ಯುತ್ತಮ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಪ್ರತಿಯೊಂದು ವಸ್ತುವಿಗೂ ತನ್ನ ಸ್ಥಳವಿದೆ, *server.ts* ಒಂದು ತುಂಬಾ ಸಣ್ಣ ಫೈಲ್ ಆಗಿದ್ದು ಕೇವಲ ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳನ್ನು ಸಂಪರ್ಕಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿ ವೈಶಿಷ್ಟ್ಯವು ತನ್ನ ಸಂಬಂಧಿತ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಇರುತ್ತದೆ, ಉದಾ: tools/, resources/ ಅಥವಾ /prompts.

ಅದ್ಭುತ, ಮುಂದಿನ ಹಂತವನ್ನು ನಿರ್ಮಿಸೋಣ.

## ಅಭ್ಯಾಸ: ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ರಚನೆ

ಈ ಅಭ್ಯಾಸದಲ್ಲಿ, ನಾವು ಹೀಗೆ ಮಾಡುತ್ತೇವೆ:

1. ಟೂಲ್ ಪಟ್ಟಿ ಮಾಡುವುದು ಮತ್ತು ಟೂಲ್ ಕರೆ ಮಾಡುವುದನ್ನು ನಿರ್ವಹಿಸುವ ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ರಚಿಸುವುದು.
2. ನೀವು ನಿರ್ಮಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು.
3. ನಿಮ್ಮ ಟೂಲ್ ಕರೆಗಳು ಸರಿಯಾಗಿ ಮಾನ್ಯತೆಗೊಳ್ಳುವಂತೆ ಮಾನ್ಯತೆ ಸೇರಿಸುವುದು.

### -1- ವಾಸ್ತುಶಿಲ್ಪ ರಚನೆ

ಮೊದಲನೆಯದಾಗಿ ನಾವು ಗಮನಿಸಬೇಕಾದದ್ದು, ನಾವು ಹೆಚ್ಚು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸುವಂತೆ ಸ್ಕೇಲ್ ಮಾಡಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪ, ಇದು ಹೀಗೆ ಕಾಣುತ್ತದೆ:

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

ಈಗ ನಾವು tools ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಹೊಸ ಟೂಲ್‌ಗಳನ್ನು ಸುಲಭವಾಗಿ ಸೇರಿಸಬಹುದಾದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಹೊಂದಿದ್ದೇವೆ. ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಗೆ ಉಪಡೈರೆಕ್ಟರಿಗಳನ್ನು ಸೇರಿಸಲು ಇದನ್ನು ಅನುಸರಿಸಬಹುದು.

### -2- ಟೂಲ್ ರಚನೆ

ಮುಂದೆ, ಟೂಲ್ ರಚನೆ ಹೇಗಿರುತ್ತದೆ ನೋಡೋಣ. ಮೊದಲು, ಅದು ತನ್ನ *tool* ಉಪಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ರಚಿಸಬೇಕು ಹೀಗೆ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic ಮಾದರಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಪುಟ್ ಅನ್ನು ಮಾನ್ಯಗೊಳಿಸಿ
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ಅನ್ನು ಸೇರಿಸಿ, ಆದ್ದರಿಂದ ನಾವು AddInputModel ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಆರ್ಗ್‌ಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸಬಹುದು

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ಇಲ್ಲಿ ನಾವು ಹೆಸರನ್ನು, ವಿವರಣೆಯನ್ನು, Pydantic ಬಳಸಿ ಇನ್‌ಪುಟ್ schema ಅನ್ನು ಮತ್ತು ಈ ಟೂಲ್ ಕರೆ ಮಾಡಲಾಗುವಾಗ ಕರೆಮಾಡುವ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ. ಕೊನೆಗೆ, `tool_add` ಎಂಬ ಡಿಕ್ಷನರಿ ಮೂಲಕ ಈ ಎಲ್ಲಾ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಹೊರತರುತ್ತೇವೆ.

*schema.py* ಕೂಡ ಇದೆ, ಇದು ನಮ್ಮ ಟೂಲ್ ಬಳಕೆ ಮಾಡುವ ಇನ್‌ಪುಟ್ schema ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

ನಾವು *__init__.py* ಫೈಲ್ ಅನ್ನು ಕೂಡ ತುಂಬಬೇಕು, ಇದರಿಂದ tools ಡೈರೆಕ್ಟರಿ ಒಂದು ಮೋಡ್ಯೂಲ್ ಆಗಿ ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ. ಜೊತೆಗೆ, ಅದರ ಒಳಗಿನ ಮೋಡ್ಯೂಲ್‌ಗಳನ್ನು ಹೀಗೆ ಹೊರತರುವ ಅಗತ್ಯವಿದೆ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ನಾವು ಹೆಚ್ಚು ಟೂಲ್‌ಗಳನ್ನು ಸೇರಿಸುವಂತೆ ಈ ಫೈಲ್ ಅನ್ನು ವಿಸ್ತರಿಸಬಹುದು.

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

- name, ಇದು ಟೂಲ್ ಹೆಸರು.
- rawSchema, ಇದು Zod schema, ಇದು ಟೂಲ್ ಕರೆ ಮಾಡಲು ಬರುವ ವಿನಂತಿಗಳನ್ನು ಮಾನ್ಯತೆ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ.
- inputSchema, ಈ schema ಅನ್ನು ಹ್ಯಾಂಡ್ಲರ್ ಬಳಸುತ್ತದೆ.
- callback, ಇದು ಟೂಲ್ ಅನ್ನು invoke ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ.

`Tool` ಕೂಡ ಇದೆ, ಇದು ಈ ಡಿಕ್ಷನರಿಯನ್ನು mcp ಸರ್ವರ್ ಹ್ಯಾಂಡ್ಲರ್ ಸ್ವೀಕರಿಸುವ ಟೈಪ್‌ಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ, ಇದು ಹೀಗೆ ಕಾಣುತ್ತದೆ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

ಮತ್ತು *schema.ts* ಇದೆ, ಇಲ್ಲಿ ಪ್ರತಿ ಟೂಲ್‌ಗೆ ಇನ್‌ಪುಟ್ schemaಗಳನ್ನು ಸಂಗ್ರಹಿಸುತ್ತೇವೆ, ಪ್ರಸ್ತುತ ಒಂದೇ schema ಇದೆ ಆದರೆ ನಾವು ಹೆಚ್ಚು ಟೂಲ್‌ಗಳನ್ನು ಸೇರಿಸುವಂತೆ entries ಹೆಚ್ಚಿಸಬಹುದು:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

ಅದ್ಭುತ, ಈಗ ನಮ್ಮ ಟೂಲ್ ಪಟ್ಟಿ ನಿರ್ವಹಣೆಗೆ ಮುಂದಾಗೋಣ.

### -3- ಟೂಲ್ ಪಟ್ಟಿ ನಿರ್ವಹಣೆ

ಮುಂದೆ, ಟೂಲ್ ಪಟ್ಟಿ ನಿರ್ವಹಿಸಲು, ನಾವು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಸರ್ವರ್ ಫೈಲ್‌ಗೆ ಸೇರಿಸಬೇಕು:

**Python**

```python
# ಸಂಕ್ಷಿಪ್ತತೆಗೆ ಕೋಡ್ ತೆಗೆದುಹಾಕಲಾಗಿದೆ
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

ಇಲ್ಲಿ ನಾವು `@server.list_tools` ಡೆಕೊರೇಟರ್ ಮತ್ತು `handle_list_tools` ಫಂಕ್ಷನ್ ಅನ್ನು ಸೇರಿಸುತ್ತೇವೆ. ನಂತರ, ಟೂಲ್ ಪಟ್ಟಿ ರಚಿಸಬೇಕು. ಪ್ರತಿ ಟೂಲ್‌ಗೆ name, description ಮತ್ತು inputSchema ಇರಬೇಕು ಎಂದು ಗಮನಿಸಿ.

**TypeScript**

ಟೂಲ್ ಪಟ್ಟಿ ಮಾಡಲು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಸರ್ವರ್‌ನಲ್ಲಿ `setRequestHandler` ಮೂಲಕ `ListToolsRequestSchema` ಗೆ ಹೊಂದುವಂತೆ ಸೆಟ್ ಮಾಡಬೇಕು.

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
// ಸಂಕ್ಷಿಪ್ತತೆಗೆ ಕೋಡ್ ತೆಗೆದುಹಾಕಲಾಗಿದೆ
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // ನೋಂದಾಯಿಸಿದ ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ಹಿಂತಿರುಗಿಸಿ
  return {
    tools: tools
  };
});
```

ಅದ್ಭುತ, ಈಗ ನಾವು ಟೂಲ್ ಪಟ್ಟಿ ಭಾಗವನ್ನು ಪರಿಹರಿಸಿದ್ದೇವೆ, ಮುಂದಿನದಾಗಿ ಟೂಲ್‌ಗಳನ್ನು ಹೇಗೆ ಕರೆ ಮಾಡಬಹುದು ನೋಡೋಣ.

### -4- ಟೂಲ್ ಕರೆ ನಿರ್ವಹಣೆ

ಟೂಲ್ ಅನ್ನು ಕರೆ ಮಾಡಲು, ಇನ್ನೊಂದು ವಿನಂತಿ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಸೆಟ್ ಮಾಡಬೇಕು, ಇದು ಯಾವ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಯಾವ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಕರೆ ಮಾಡಬೇಕೆಂದು ನಿರ್ಧರಿಸುತ್ತದೆ.

**Python**

`@server.call_tool` ಡೆಕೊರೇಟರ್ ಬಳಸಿ `handle_call_tool` ಫಂಕ್ಷನ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸೋಣ. ಈ ಫಂಕ್ಷನ್‌ನಲ್ಲಿ, ಟೂಲ್ ಹೆಸರು, ಅದರ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ, ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಸರಿಯಾಗಿವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು. ನೀವು ಈ ಮಾನ್ಯತೆಯನ್ನು ಈ ಫಂಕ್ಷನ್‌ನಲ್ಲಿ ಅಥವಾ ನಿಜವಾದ ಟೂಲ್‌ನಲ್ಲಿ ಮಾಡಬಹುದು.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ಎಂಬುದು ಉಪಕರಣದ ಹೆಸರುಗಳನ್ನು ಕೀಲಿಗಳಾಗಿ ಹೊಂದಿರುವ ನಿಘಂಟು
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

ಇಲ್ಲಿ ನಡೆಯುವವು:

- ನಮ್ಮ ಟೂಲ್ ಹೆಸರು ಈಗಾಗಲೇ `name` ಇನ್‌ಪುಟ್ ಪ್ಯಾರಾಮೀಟರ್ ಆಗಿದೆ ಮತ್ತು `arguments` ಡಿಕ್ಷನರಿಯಲ್ಲಿ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಇವೆ.

- ಟೂಲ್ ಅನ್ನು `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ಮೂಲಕ ಕರೆ ಮಾಡಲಾಗುತ್ತದೆ. ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳ ಮಾನ್ಯತೆ `handler` ಗುಣಲಕ್ಷಣದಲ್ಲಿ ನಡೆಯುತ್ತದೆ, ಇದು ಫಂಕ್ಷನ್‌ಗೆ ಸೂಚಿಸುತ್ತದೆ, ವಿಫಲವಾದರೆ exception ಎಬ್ಬುತ್ತದೆ.

ಇದೀಗ, ನಾವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ಬಳಸಿ ಟೂಲ್ ಪಟ್ಟಿ ಮತ್ತು ಕರೆ ಮಾಡುವುದನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇವೆ.

[ಪೂರ್ಣ ಉದಾಹರಣೆ](./code/README.md) ಇಲ್ಲಿ ನೋಡಿ

## ಹುದ್ದೆ

ನೀವು ಪಡೆದಿರುವ ಕೋಡ್‌ಗೆ ಹಲವು ಟೂಲ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ವಿಸ್ತರಿಸಿ ಮತ್ತು ನೀವು ಗಮನಿಸುವಂತೆ tools ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಮಾತ್ರ ಫೈಲ್‌ಗಳನ್ನು ಸೇರಿಸುವ ಅಗತ್ಯವಿದೆ ಮತ್ತು ಬೇರೆಡೆ ಇಲ್ಲ ಎಂದು ಪರಿಗಣಿಸಿ.

*ಯಾವುದೇ ಪರಿಹಾರ ನೀಡಲಾಗಿಲ್ಲ*

## ಸಾರಾಂಶ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಲೋ-ಲೆವೆಲ್ ಸರ್ವರ್ ವಿಧಾನ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಅದರಿಂದ ನಾವು ಸುಂದರ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ರಚಿಸಬಹುದು ಎಂದು ನೋಡಿದೆವು. ನಾವು ಮಾನ್ಯತೆಯ ಬಗ್ಗೆ ಚರ್ಚಿಸಿ, ಇನ್‌ಪುಟ್ ಮಾನ್ಯತೆಗಾಗಿ schema ರಚಿಸಲು validation ಲೈಬ್ರರಿಗಳನ್ನು ಹೇಗೆ ಬಳಸುವುದು ಎಂದು ತೋರಿಸಲಾಗಿದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1de8367745088b9fcd4746ea4cc5a161",
  "translation_date": "2025-12-11T12:43:59+00:00",
  "source_file": "03-GettingStarted/10-advanced/README.md",
  "language_code": "ml"
}
-->
# ആഡ്വാൻസ്ഡ് സർവർ ഉപയോഗം

MCP SDK-യിൽ രണ്ട് വ്യത്യസ്ത തരത്തിലുള്ള സർവറുകൾ ഉണ്ട്, നിങ്ങളുടെ സാധാരണ സർവർയും ലോ-ലെവൽ സർവർയും. സാധാരണയായി, നിങ്ങൾ സാധാരണ സർവർ ഉപയോഗിച്ച് അതിൽ ഫീച്ചറുകൾ ചേർക്കും. ചില സാഹചര്യങ്ങളിൽ, നിങ്ങൾ ലോ-ലെവൽ സർവറിനെ ആശ്രയിക്കണം, ഉദാഹരണത്തിന്:

- മെച്ചപ്പെട്ട ആർക്കിടെക്ചർ. സാധാരണ സർവർക്കും ലോ-ലെവൽ സർവർക്കും ഉപയോഗിച്ച് ഒരു ക്ലീൻ ആർക്കിടെക്ചർ സൃഷ്ടിക്കാം, പക്ഷേ ലോ-ലെവൽ സർവറുമായി ഇത് കുറച്ച് എളുപ്പമാണ് എന്ന് വാദിക്കാം.
- ഫീച്ചർ ലഭ്യത. ചില ആഡ്വാൻസ്ഡ് ഫീച്ചറുകൾ ലോ-ലെവൽ സർവറുമായി മാത്രമേ ഉപയോഗിക്കാനാകൂ. സാമ്പ്ലിംഗ്, എലിസിറ്റേഷൻ എന്നിവ ചേർക്കുമ്പോൾ ഇത് പിന്നീട് കാണാം.

## സാധാരണ സർവർ vs ലോ-ലെവൽ സർവർ

സാധാരണ സർവറുമായി MCP Server സൃഷ്ടിക്കുന്നത് ഇങ്ങനെ കാണാം

**Python**

```python
mcp = FastMCP("Demo")

# ഒരു കൂട്ടിച്ചേർക്കൽ ഉപകരണം ചേർക്കുക
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

// ഒരു കൂട്ടിച്ചേർക്കൽ ഉപകരണം ചേർക്കുക
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

അർത്ഥം, നിങ്ങൾ സർവറിന് വേണ്ട എല്ലാ ടൂൾസ്, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ വ്യക്തമായി ചേർക്കുന്നു. ഇതിൽ തെറ്റ് ഒന്നുമില്ല.

### ലോ-ലെവൽ സർവർ സമീപനം

എങ്കിലും, ലോ-ലെവൽ സർവർ സമീപനം ഉപയോഗിക്കുമ്പോൾ നിങ്ങൾ വ്യത്യസ്തമായി ചിന്തിക്കണം, അതായത് ഓരോ ഫീച്ചർ തരം (ടൂൾസ്, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ) വേണ്ടി രണ്ട് ഹാൻഡ്ലറുകൾ സൃഷ്ടിക്കണം. ഉദാഹരണത്തിന് ടൂൾസ് രണ്ട് ഫംഗ്ഷനുകൾ മാത്രമേ ഉണ്ടാകൂ:

- എല്ലാ ടൂളുകളും ലിസ്റ്റ് ചെയ്യുക. ഒരു ഫംഗ്ഷൻ എല്ലാ ടൂൾ ലിസ്റ്റിംഗ് ശ്രമങ്ങൾ കൈകാര്യം ചെയ്യും.
- എല്ലാ ടൂൾ കോളുകളും കൈകാര്യം ചെയ്യുക. ഇവിടെ ഒരു ഫംഗ്ഷൻ മാത്രമേ ടൂൾ കോളുകൾ കൈകാര്യം ചെയ്യൂ.

ഇത് കുറച്ച് കുറവ് ജോലി പോലെ തോന്നുന്നില്ലേ? അതായത് ടൂൾ രജിസ്റ്റർ ചെയ്യുന്നതിന് പകരം, ഞാൻ ടൂൾസ് ലിസ്റ്റ് ചെയ്യുമ്പോൾ ടൂൾ ലിസ്റ്റിൽ ഉണ്ടെന്ന് ഉറപ്പാക്കണം, ടൂൾ കോളിന് ഒരു അഭ്യർത്ഥന വന്നാൽ അത് വിളിക്കണം.

ഇപ്പോൾ കോഡ് എങ്ങനെ കാണപ്പെടുന്നു നോക്കാം:

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
  // രജിസ്റ്റർ ചെയ്ത ടൂളുകളുടെ പട്ടിക തിരികെ നൽകുക
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

ഇവിടെ ഫീച്ചറുകളുടെ ലിസ്റ്റ് റിട്ടേൺ ചെയ്യുന്ന ഒരു ഫംഗ്ഷൻ ഉണ്ട്. ടൂൾസ് ലിസ്റ്റിലെ ഓരോ എൻട്രിക്കും `name`, `description`, `inputSchema` പോലുള്ള ഫീൽഡുകൾ ഉണ്ട്, ഇത് റിട്ടേൺ ടൈപ്പിനോട് പൊരുത്തപ്പെടാൻ. ഇതിലൂടെ ടൂൾസ്, ഫീച്ചർ നിർവചനങ്ങൾ വേറെ സ്ഥലത്ത് സൂക്ഷിക്കാം. ഇനി എല്ലാ ടൂൾസും tools ഫോൾഡറിൽ സൃഷ്ടിക്കാം, അതുപോലെ എല്ലാ ഫീച്ചറുകളും, അതിനാൽ നിങ്ങളുടെ പ്രോജക്ട് ഇങ്ങനെ ക്രമീകരിക്കാം:

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

അത്ഭുതം, നമ്മുടെ ആർക്കിടെക്ചർ വളരെ ക്ലീൻ ആയി കാണാൻ കഴിയും.

ടൂൾ കോളിംഗ് എങ്ങനെയാകും, അതേ ആശയമാണോ, ഒരു ഹാൻഡ്ലർ ഏതൊരു ടൂളും വിളിക്കാനായി? അതെ, കൃത്യമായി, ഇതാ അതിന്റെ കോഡ്:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools എന്നത് ടൂൾ നാമങ്ങൾ കീകളായി ഉള്ള ഒരു നിഘണ്ടുവാണ്
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
    // TODO ടൂൾ വിളിക്കുക,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

മുകളിൽ കാണുന്ന കോഡിൽ നിന്ന്, ടൂൾ ഏത് ആണെന്ന്, ഏത് arguments-ഉം ഉപയോഗിച്ച് വിളിക്കണമെന്ന് പാഴ്സുചെയ്യണം, പിന്നെ ടൂൾ വിളിക്കണം.

## വാലിഡേഷൻ ഉപയോഗിച്ച് സമീപനം മെച്ചപ്പെടുത്തൽ

ഇതുവരെ, ടൂൾസ്, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ ചേർക്കുന്നതിനുള്ള എല്ലാ രജിസ്ട്രേഷനുകളും ഓരോ ഫീച്ചർ തരം വേണ്ടി രണ്ട് ഹാൻഡ്ലറുകൾ ഉപയോഗിച്ച് മാറ്റാമെന്ന് കണ്ടു. ഇനി എന്ത് ചെയ്യണം? ടൂൾ ശരിയായ arguments-ഉം ഉപയോഗിച്ച് വിളിക്കപ്പെടുന്നുണ്ടെന്ന് ഉറപ്പാക്കാൻ വാലിഡേഷൻ ചേർക്കണം. ഓരോ റൺടൈമിനും ഇതിന് സ്വന്തം പരിഹാരമുണ്ട്, ഉദാഹരണത്തിന് Python Pydantic ഉപയോഗിക്കുന്നു, TypeScript Zod ഉപയോഗിക്കുന്നു. ആശയം:

- ഫീച്ചർ (ടൂൾ, റിസോഴ്‌സ്, പ്രോംപ്റ്റ്) സൃഷ്ടിക്കുന്ന ലജിക് അതിന്റെ സമർപ്പിത ഫോൾഡറിൽ മാറ്റുക.
- ഒരു അഭ്യർത്ഥന വാലിഡേറ്റ് ചെയ്യാനുള്ള മാർഗം ചേർക്കുക, ഉദാഹരണത്തിന് ടൂൾ കോളിന്.

### ഫീച്ചർ സൃഷ്ടിക്കുക

ഫീച്ചർ സൃഷ്ടിക്കാൻ, ആ ഫീച്ചറിനായി ഒരു ഫയൽ സൃഷ്ടിച്ച് അതിൽ ആ ഫീച്ചറിന് ആവശ്യമായ നിർബന്ധിത ഫീൽഡുകൾ ഉണ്ടെന്ന് ഉറപ്പാക്കണം. ടൂൾസ്, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ തമ്മിൽ ഫീൽഡുകൾ കുറച്ച് വ്യത്യസ്തമാണ്.

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
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, അതിലൂടെ നാം AddInputModel സൃഷ്ടിച്ച് args സാധുത പരിശോധിക്കാം

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ഇവിടെ കാണാം:

- Pydantic ഉപയോഗിച്ച് `AddInputModel` എന്ന സ്കീമ സൃഷ്ടിക്കുന്നു, ഫീൽഡുകൾ `a` , `b` *schema.py* ഫയലിൽ.
- വരുന്ന അഭ്യർത്ഥന `AddInputModel` ടൈപ്പിൽ പാഴ്സുചെയ്യാൻ ശ്രമിക്കുന്നു, പാരാമീറ്ററുകളിൽ പൊരുത്തക്കേട് ഉണ്ടെങ്കിൽ ക്രാഷ് ചെയ്യും:

   ```python
   # add.py
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ഈ പാഴ്സിംഗ് ലജിക് ടൂൾ കോളിൽ തന്നെ ഇടാമോ, ഹാൻഡ്ലർ ഫംഗ്ഷനിൽ ഇടാമോ നിങ്ങൾ തിരഞ്ഞെടുക്കാം.

**TypeScript**

```typescript
// സെർവർ.ts
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

       // @ts-അഗ്നേയം
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

// സ്കീമ.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// ചേർക്കുക.ts
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

- എല്ലാ ടൂൾ കോളുകളും കൈകാര്യം ചെയ്യുന്ന ഹാൻഡ്ലറിൽ, വരുന്ന അഭ്യർത്ഥന ടൂളിന്റെ നിർവചിച്ച സ്കീമയിലേക്ക് പാഴ്സുചെയ്യാൻ ശ്രമിക്കുന്നു:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ഇത് ശരിയെങ്കിൽ, യഥാർത്ഥ ടൂൾ കോളിലേക്ക് പോകുന്നു:

    ```typescript
    const result = await tool.callback(input);
    ```

ഈ സമീപനം മികച്ച ആർക്കിടെക്ചർ സൃഷ്ടിക്കുന്നു, *server.ts* വളരെ ചെറിയ ഫയലാണ്, അത് അഭ്യർത്ഥന ഹാൻഡ്ലറുകൾ മാത്രം വയർ ചെയ്യുന്നു, ഓരോ ഫീച്ചറും അവരുടെ ഫോൾഡറുകളിൽ ആണ്, ഉദാ: tools/, resources/, prompts/.

നല്ലത്, ഇനി ഇത് നിർമ്മിക്കാൻ ശ്രമിക്കാം.

## അഭ്യാസം: ലോ-ലെവൽ സർവർ സൃഷ്ടിക്കൽ

ഈ അഭ്യാസത്തിൽ, നാം ചെയ്യുന്നത്:

1. ടൂൾസ് ലിസ്റ്റിംഗ്, ടൂൾ കോളിംഗ് കൈകാര്യം ചെയ്യുന്ന ലോ-ലെവൽ സർവർ സൃഷ്ടിക്കുക.
2. നിങ്ങൾക്ക് വികസിപ്പിക്കാൻ കഴിയുന്ന ഒരു ആർക്കിടെക്ചർ നടപ്പിലാക്കുക.
3. ടൂൾ കോളുകൾ ശരിയായി വാലിഡേറ്റ് ചെയ്യപ്പെടുന്നുണ്ടെന്ന് ഉറപ്പാക്കാൻ വാലിഡേഷൻ ചേർക്കുക.

### -1- ആർക്കിടെക്ചർ സൃഷ്ടിക്കുക

ആദ്യം പരിഗണിക്കേണ്ടത്, കൂടുതൽ ഫീച്ചറുകൾ ചേർക്കുമ്പോൾ സ്കെയിൽ ചെയ്യാൻ സഹായിക്കുന്ന ഒരു ആർക്കിടെക്ചർ ആണ്, ഇങ്ങനെ കാണാം:

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

ഇപ്പോൾ tools ഫോൾഡറിൽ പുതിയ ടൂൾസ് എളുപ്പത്തിൽ ചേർക്കാൻ കഴിയുന്ന ആർക്കിടെക്ചർ സജ്ജമാക്കി. resources, prompts എന്നിവയ്ക്കും സബ്ഡയറക്ടറികൾ ചേർക്കാം.

### -2- ടൂൾ സൃഷ്ടിക്കുക

ടൂൾ സൃഷ്ടിക്കുന്നത് എങ്ങനെ കാണാം. ആദ്യം, അത് *tool* സബ്ഡയറക്ടറിയിൽ സൃഷ്ടിക്കണം:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, അതിലൂടെ നാം AddInputModel സൃഷ്ടിച്ച് args സാധുത പരിശോധിക്കാം

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ഇവിടെ നാം കാണുന്നത്, ടൂൾയുടെ പേര്, വിവരണം, Pydantic ഉപയോഗിച്ചുള്ള ഇൻപുട്ട് സ്കീമ, ടൂൾ വിളിക്കുമ്പോൾ പ്രവർത്തിക്കുന്ന ഹാൻഡ്ലർ എന്നിവ നിർവചിക്കുന്നു. അവസാനം `tool_add` എന്ന ഡിക്ഷണറി എല്ലാ പ്രോപ്പർട്ടികളും ഉൾക്കൊള്ളുന്നു.

*schema.py* ഫയലും ഉണ്ട്, ടൂളിന്റെ ഇൻപുട്ട് സ്കീമ നിർവചിക്കാൻ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ഫയൽ പൂരിപ്പിച്ച് tools ഡയറക്ടറി ഒരു മോഡ്യൂളായി പരിഗണിക്കണം. അതിനുള്ള കോഡ്:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

പുതിയ ടൂൾസ് ചേർക്കുമ്പോൾ ഈ ഫയൽ അപ്ഡേറ്റ് ചെയ്യാം.

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

ഇവിടെ ഒരു ഡിക്ഷണറി സൃഷ്ടിക്കുന്നു, പ്രോപ്പർട്ടികൾ:

- name: ടൂളിന്റെ പേര്.
- rawSchema: Zod സ്കീമ, ടൂൾ കോളിന് വരുന്ന അഭ്യർത്ഥന വാലിഡേറ്റ് ചെയ്യാൻ.
- inputSchema: ഹാൻഡ്ലർ ഉപയോഗിക്കുന്ന സ്കീമ.
- callback: ടൂൾ വിളിക്കാൻ ഉപയോഗിക്കുന്നു.

`Tool` എന്നത് ഈ ഡിക്ഷണറി MCP സർവർ ഹാൻഡ്ലർ സ്വീകരിക്കുന്ന ടൈപ്പിലേക്ക് മാറ്റാൻ ഉപയോഗിക്കുന്നു, ഇങ്ങനെ കാണാം:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* ഫയലിൽ ഓരോ ടൂളിനും ഇൻപുട്ട് സ്കീമ സൂക്ഷിക്കുന്നു, ഇപ്പോൾ ഒരു സ്കീമ മാത്രമേ ഉള്ളൂ, ടൂൾസ് കൂട്ടുമ്പോൾ കൂടുതൽ ചേർക്കാം:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

നല്ലത്, ഇനി ടൂൾസ് ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യാം.

### -3- ടൂൾ ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യുക

ടൂൾസ് ലിസ്റ്റ് ചെയ്യാൻ അഭ്യർത്ഥന ഹാൻഡ്ലർ സജ്ജമാക്കണം. സർവർ ഫയലിൽ ചേർക്കേണ്ടത്:

**Python**

```python
# ലഘൂകരണത്തിനായി കോഡ് ഒഴിവാക്കി
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

`@server.list_tools` ഡെക്കറേറ്റർ ചേർത്ത് `handle_list_tools` ഫംഗ്ഷൻ നടപ്പിലാക്കുന്നു. ടൂൾസ് ലിസ്റ്റ് നൽകണം, ഓരോ ടൂളിനും name, description, inputSchema വേണം.

**TypeScript**

ടൂൾസ് ലിസ്റ്റിംഗ് അഭ്യർത്ഥന ഹാൻഡ്ലർ സജ്ജമാക്കാൻ, സർവറിൽ `setRequestHandler` വിളിച്ച് `ListToolsRequestSchema` ഉപയോഗിക്കുന്നു:

```typescript
// ഇൻഡക്സ്.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// സെർവർ.ts
// ലഘൂകരിക്കാൻ കോഡ് ഒഴിവാക്കി
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // രജിസ്റ്റർ ചെയ്ത ടൂളുകളുടെ പട്ടിക തിരികെ നൽകുക
  return {
    tools: tools
  };
});
```

നല്ലത്, ടൂൾസ് ലിസ്റ്റിംഗ് പരിഹരിച്ചു, ഇനി ടൂൾ കോളിംഗ് എങ്ങനെ ചെയ്യാമെന്ന് നോക്കാം.

### -4- ടൂൾ കോളിംഗ് കൈകാര്യം ചെയ്യുക

ടൂൾ കോളിംഗ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാൻ മറ്റൊരു ഹാൻഡ്ലർ സജ്ജമാക്കണം, ഏത് ഫീച്ചർ വിളിക്കണം, ഏത് arguments-ഉം ഉപയോഗിക്കണം എന്നത് നിർദ്ദേശിക്കുന്ന അഭ്യർത്ഥന.

**Python**

`@server.call_tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് `handle_call_tool` ഫംഗ്ഷൻ നടപ്പിലാക്കാം. ഈ ഫംഗ്ഷനിൽ ടൂൾ നാമം, arguments പാഴ്സ് ചെയ്ത് അവ ശരിയാണെന്ന് ഉറപ്പാക്കണം. വാലിഡേഷൻ ഈ ഫംഗ്ഷനിൽ അല്ലെങ്കിൽ ടൂളിൽ തന്നെ ചെയ്യാം.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools എന്നത് ടൂൾ നാമങ്ങൾ കീകളായി ഉള്ള ഒരു നിഘണ്ടുവാണ്
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ടൂൾ പ്രവർത്തിപ്പിക്കുക
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

ഇവിടെ സംഭവിക്കുന്നത്:

- ടൂൾ നാമം `name` എന്ന ഇൻപുട്ട് പാരാമീറ്ററായി ലഭ്യമാണ്, arguments `arguments` ഡിക്ഷണറിയിൽ.
- ടൂൾ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ഉപയോഗിച്ച് വിളിക്കുന്നു. arguments വാലിഡേഷൻ `handler` ഫംഗ്ഷനിൽ നടക്കും, പരാജയപ്പെട്ടാൽ എക്സെപ്ഷൻ ഉയരും.

ഇപ്പോൾ ലോ-ലെവൽ സർവർ ഉപയോഗിച്ച് ടൂൾസ് ലിസ്റ്റ് ചെയ്യാനും കോളിംഗ് ചെയ്യാനും പൂർണ്ണമായ ധാരണ ലഭിച്ചു.

[പൂർണ്ണ ഉദാഹരണം](./code/README.md) കാണുക

## അസൈൻമെന്റ്

നൽകിയ കോഡിൽ കൂടുതൽ ടൂൾസ്, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ ചേർക്കുക, tools ഡയറക്ടറിയിൽ മാത്രമേ ഫയലുകൾ ചേർക്കേണ്ടതുണ്ടെന്ന് ശ്രദ്ധിക്കുക.

*പരിഹാരം നൽകിയിട്ടില്ല*

## സംഗ്രഹം

ഈ അധ്യായത്തിൽ, ലോ-ലെവൽ സർവർ സമീപനം എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന്, അത് എങ്ങനെ നല്ല ആർക്കിടെക്ചർ സൃഷ്ടിക്കാൻ സഹായിക്കുന്നുവെന്ന് കണ്ടു. വാലിഡേഷൻ ചർച്ച ചെയ്തു, ഇൻപുട്ട് വാലിഡേഷനായി സ്കീമകൾ സൃഷ്ടിക്കാൻ വാലിഡേഷൻ ലൈബ്രറികൾ ഉപയോഗിക്കുന്നത് കാണിച്ചു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
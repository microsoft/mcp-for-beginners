# അഭിമുഖ്യ സെർവർ ഉപയോഗം

MCP SDK യിൽ രണ്ട് വ്യത്യസ്ത തരത്തിലുള്ള സെർവർകൾ ഉണ്ട്, നിങ്ങളുടെ സാധാരണ സെർവർയും ലോ-ലവൽ സെർവർയും. സാധാരണയായി, നിങ്ങൾ അതിൽ ഫീച്ചറുകൾ ചേർക്കാൻ സാധാരണ സെർവർ ഉപയോഗിക്കും. എന്നാൽ ചില സന്ദർഭങ്ങളിൽ, നിങ്ങൾ ലോ-ലവൽ സെർവറിനെ ആശ്രയിക്കണമെന്ന് ആഗ്രഹിക്കുന്നു, ഉദാഹരണത്തിന്:

- മികച്ച ആർക്കിടെക്ചർ. സാധാരണ സെർവർയും ലോ-ലവൽ സെർവറുമുള്ള ശുദ്ധമായ ആർക്കിടെക്ചർ സൃഷ്ടിക്കൽ സാധ്യമാണ്, പക്ഷേ ലോ-ലവൽ സെർവറിനൊപ്പം ഇത് കൂടുതൽ എളുപ്പമാണെന്ന് വാദിക്കാമെന്നാണ്.
- ഫീച്ചർ ലഭ്യത. ചില അഭിമുഖ്യ ഫീച്ചറുകൾ മാത്രമേ ലോ-ലവൽ സെർവറുമായി മാത്രമേ ഉപയോഗിക്കാനാകൂ. സാമ്പ്ലിംഗ്, elicitation എന്നിവ ചേർക്കുമ്പോൾ ഇതു അഗ്‌വ്യാപകമായി കാണാം.

## സാധാരണ സെർവർ vs ലോ-ലവൽ സെർവർ

സാധാരണ സെർവറോടെ MCP സെർവർ സൃഷ്ടിക്കുന്നത് ഇതാണ്:

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

// ഒരു കൂട്ടിയടിയിലേക്കുള്ള ഉപകരണം ചേർക്കുക
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

മുശായിക്. നിങ്ങൾ സെർവർക്ക് വേണമെന്നെങ്കിൽ ഓരോ ടൂൾ, റിസോഴ്‌സ്, പ്രോംപ്റ്റ് എന്നിവ വ്യക്തമായി ചേർക്കുന്നു. അതിൽ പിഴവ് ഒന്നുമില്ല.

### ലോ-ലവൽ സെർവർ സമീപനം

എന്നാൽ, ലോ-ലവൽ സെർവർ ഉപയോഗിക്കുമ്പോൾ, നിങ്ങൾ മറ്റൊരു രീതിയിൽ ആലോചിക്കണം. ഓരോ ടൂൾ അല്ലെങ്കിൽ റിസോഴ്‌സ്, പ്രോംപ്റ്റ് തരത്തിനും (ഫീച്ചർ ടൈപ്പ്) രണ്ട് ഹാൻഡ്ലർമാർ മാത്രം സൃഷ്ടിക്കുന്നു. ഉദാഹരണത്തിന്, ടൂളുകൾക്ക് രണ്ട് ഫംഗ്ഷനുകളുണ്ട്:

- എല്ലാ ടൂളുകളുടെയും പട്ടിക തയ്യാറാക്കൽ. എല്ലാ ടൂൾ ലിസ്റ്റിംഗ് ശ്രമങ്ങൾക്കായി ഒരു ഫംഗ്ഷൻ ഉത്തരവാദിയാണ്.
- എല്ലാ ടൂൾ കാളുകളും കൈകാര്യം ചെയ്യൽ. ഓരോ ടൂൾ വിളിക്കാനുള്ള ഒരു ഫംഗ്ഷൻ മാത്രം.

കുറഞ്ഞ ജോലി പോലെയാണ് ഇത് തോന്നേണ്ടതല്ലേ? അതായത് ടൂൾ രജിസ്റ്റർ ചെയ്യുന്നത് പകരം, ടൂൾ ലിസ്റ്റ് ചെയ്യുമ്പോൾ ടൂൾ ഉള്ളതായി ഉറപ്പാക്കുക, ടൂൾ വിളിക്കേണ്ടപ്പോൾ അതിനെ വിളിക്കുക എന്നതാണ്.

ഇപ്പോൾ കോംഡ് ഇങ്ങനെ കാണാം:

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
  // രജിസ്റ്റര്‍ ചെയ്ത ടൂളുകളുടെ പട്ടിക തിരിച്ചയയ്ക്കുക
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

ഇവിടെ ഒരു ഫംഗ്ഷൻ ഫീച്ചറുകളുടെ ലിസ്റ്റ് തിരികെ നൽകുന്നു. ടൂൾ ലിസ്റ്റിലെ ഓരോ എൻട്രിക്കും `name`, `description`, `inputSchema` പോലുള്ള ഫീൽഡുകൾ ഉണ്ട്, ഇത് തിരിച്ചറിവ് ടൈപ്പിനനുസരിച്ച് ആണ്. ഇതോടെ ഞങ്ങൾ ടൂളുകളും ഫീച്ചർ നിർവ്വചനവും മറ്റൊരിടത്തും വെയ്ക്കാം. ടൂളുകൾ tools ഫോൾഡറിലാക്കാം, ആ കവിതയെപ്പോലെ നിങ്ങളുടെ പ്രോജക്റ്റ് ഈ രൂപത്തിൽ ക്രമീകരിക്കാം:

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

അതായിരിക്കും, ആർക്കിടെക്ചർ വളരെ ശുദ്ധമായേക്കാം.

ടൂൾ വിളിക്കുന്നത് എങ്ങനെയാണോ? ഒരേ ഹാൻഡ്ലറിനു പുറമെ, ഏതൊരു ടൂളും വിളിക്കാൻ അനുയോജ്യമാണോ? അതല്ലേ. ഇതാ അതിന്റെ കോഡ്:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # toolsയുടെ കീകൾ ടൂൾ നാമങ്ങളാണ് എന്ന ഒരു നിഘണ്ടു ആണ്
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
    // TODO ഉപകരണം വിളിക്കുക,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

മുൻപ് കണ്ടതിനുനുസരിച്ച്, ടൂൾ, അതിന്റെ_ARGUMENTS വകിട്ടു കിട്ടണം, ൽ കളിക്കാൻ തുടങ്ങണം.

## സമയോചിത പരിശോധനയുമായി സമീപനം മെച്ചപ്പെടുത്തൽ

ഇപ്പോഴുവരെ നിങ്ങൾ കണ്ടത് ടൂൾ, റിസോഴ്‌സ്, പ്രോംപ്റ്റ് രജിസ്‌ട്രേഷനുകൾ ഇവ രണ്ടാമൂഴം ഹാൻഡ്ലർമാർക്കൊപ്പം മാറ്റുകയായിരുന്നു. ഇനി എന്ത് വേണം? ടൂൾ ശരിയായ_ARGUMENTS-ഉം കൂടി വിളിക്കപ്പെടുന്നതെന്ന് ഉറപ്പാക്കാൻ ഏതെങ്കിലും പരിശോധന ചേർക്കണം. ഓരോ റൺടൈമിനും വ്യത്യസ്ത പരിഹാരമുണ്ട്, ഉദാഹരണത്തിന് Python Pydantic ഉപയോഗിക്കുന്നു, TypeScript Zod. ആശയം:

- ഫീച്ചർ(ടൂൾ, റിസോഴ്‌സ്, പ്രോംപ്റ്റ്) സൃഷ്ടിക്കൽ ലജിക്ക് പ്രത്യേക ഫോൾഡറിലേക്ക് മാറ്റുക.
- ടൂളിൽ വിളിക്കൽ പോലുള്ള ഇൻകമിംഗ് റിക്വസ്റ്റ് പരിശോധിക്കാൻ മാർഗം ചേർക്കുക.

### ഫീച്ചർ സൃഷ്ടിക്കുക

ഫീച്ചർ സൃഷ്ടിക്കാൻ ആ ഫീച്ചറിനായി ഫയൽ സൃഷ്ടിക്കണം, അതിൽ ഫീച്ചറിനെ ആവശ്യമായ നിർബന്ധമായ ഫീൽഡുകൾ ചേർക്കണം. ടൂൾസ്, റിസോഴ്‌സസ്, പ്രോംപ്റ്റ്സിൽ ഫീൽഡ് വ്യത്യാസമുണ്ട്.

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
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുവാക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, അതിലൂടെ AddInputModel സൃഷ്ടിച്ച് ആർഗ്യുമെന്റുകൾ സാധുവാക്കാം

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

നിങ്ങൾ കാണുന്നത്:

- Pydantic ഉപയോഗിച്ച് `AddInputModel` സ്‌കീമ സൃഷ്ടിക്കൽ `a` and `b` ഫീൽഡുകളോടെ *schema.py* ൽ.
- ഇൻകമിംഗ് റിക്വസ്റ്റ് `AddInputModel` ടൈപ്പിലേക്കു പാഴ്സുചെയ്യുക, പരാമീറ്ററുകൾ പൊരുത്തപ്പെടുത്താത്ത പക്ഷം ക്രാഷ് ഉണ്ടാകും:

   ```python
   # add.py
    try:
        # പൈഡാന്റിക് മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധൂകരിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

പാഴ്സിംഗ് ലോജിക്ക് ടൂൾ വിളിക്കലിൽ അല്ലെങ്കിൽ ഹാൻഡ്ലർ ഫംഗ്ഷനിൽ വയ്ക്കാം.

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

       // @ts-അഗ്നി
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

- എല്ലാ ടൂൾ വിളികളും കൈകാര്യം ചെയ്യുന്ന ഹാൻഡ്ലറിൽ, ഇൻകമിംഗ് റിക്വസ്റ്റ് ടൂളിന്റെ നിർവ്വചിച്ച സ്‌കീമയിലേക്കു പാഴ്സ് ചെയ്യാൻ ശ്രമിക്കുന്നു:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

  ഇത് വിജയിച്ചാൽ ടൂൾ യഥാർഥത്തിൽ വിളിക്കുകയാണ്:

    ```typescript
    const result = await tool.callback(input);
    ```

ഈ സമീപനം മികച്ച ആർക്കിടെക്ചർ സൃഷ്ടിക്കുന്നു, എല്ലായിടത്തും തനിക്ക് വേണ്ടതുണ്ട്, *server.ts* വളരെ ചെറുതും, ഒപ്പം പ്രോജക്റ്റിലെ ഓരോ ഫീച്ചറുകളും ബന്ധപ്പെട്ട ഫോൾഡറുകളിലായി ഒതുക്കം.

നല്ലത്, അടുത്തതായി ഇത് നിർമ്മിക്കാം.

## വ്യായാമം: ലോ-ലവൽ സെർവർ സൃഷ്ടിക്കൽ

ഈ വ്യായാമത്തിൽ:

1. ടൂൾ ലിസ്റ്റിംഗ്, ടൂൾ വിളി കൈകാര്യം ചെയ്യുന്ന ലോ-ലവൽ സെർവർ ഒരുക്കുക.
2. വികസിപ്പിക്കാൻ കഴിയുന്ന ആർക്കിടെക്ചർ നടപ്പിലാക്കുക.
3. ടൂൾ വിളികൾ ശരിയായി പരിശോധന ചെയ്യുന്നു എന്നതുകാണിച്ച് സാധ്യമായ പരിശോധന ചേർക്കുക.

### -1- ആർക്കിടെക്ചർ സൃഷ്ടി

ആദ്യം ഒരു ആർക്കിടെക്ചർ സൃഷ്ടിക്കാം, കൂടുതല് ഫീച്ചറുകൾ ചേർക്കുമ്പോൾ ഇത് സഹായിക്കും, ഇതാ രൂപം:

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

ഇപ്പോൾ tools ഫോൾഡറിൽ എളുപ്പത്തിൽ പുതിയ ടൂളുകൾ ചേർക്കാം. നിങ്ങളുടെ ആവശ്യപ്രകാരം resources, prompts എന്നിവക്ക് ഉപഡയറക്ടറികൾ ഈ മത്തെ തുടരാം.

### -2- ടൂൾ സൃഷ്ടിക്കൽ

ടൂൾ സൃഷ്ടിക്കുന്നത് ഇങ്ങനെ കാണാം. ആദ്യം, അത് ടൂൾ സബ് ഡയറക്ടറിയിൽ സൃഷ്ടിക്കണം:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധന നടത്തുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, ώστε നാം AddInputModel നിർമ്മിച്ച് args സാധുത പരിശോധിക്കാം

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

നിങ്ങൾ കാണുന്നത് ടൂൾ നാമം, വിവരണം, ഇൻപുട്ട് സ്കീമ Pydantic ഉപയോഗിച്ച് നിർവ്വചിക്കുകയാണെന്നും, ടൂളിന്റെ ഹാൻഡ്ലർ നിർവ്വചിച്ചിരിക്കുന്നതുമാണ്. `tool_add` എന്ന ഡിക്ഷനറി മുഖേന ഇവ പുറംവകയിൽ എത്തിക്കുന്നു.

*schema.py* ഇൻപുട്ട് സ്‌കീമ നിർവ്വചിക്കുന്നു:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ടൂളുകൾ മോഡ്യൂളായി പരിഗണിക്കപ്പെടാൻ സ്വാധീനിക്കുന്നു, മെയിൻ ഫയൽ മോഡ്യൂളുകൾ പുറത്ത് കൊണ്ടുവരുന്നു:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ഇത് തുടരും കൊടുക്കുന്ന ടൂളുകൾക്കനുസരിച്ച്.

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

ടൂൾ സൃഷ്ടിക്കുന്നത്:

- name: ടൂളിന്റെ പേര്.
- rawSchema: Zod സ്‌കീമ, ഇൻകമിംഗ് ടൂൾ വിളികളെ സാധൂകരിക്കാൻ.
- inputSchema: ഹാൻഡ്ലറിനായി ഉപയോഗിക്കുന്ന സ്‌കീമ.
- callback: ടൂൾ പ്രവർത്തിപ്പിക്കാൻ.

`Tool` എന്നത് ഈ ഡിക്ഷനറി ടൈപ്പിലാക്കുന്നു, സെർവർ ഹാൻഡ്ലർക്ക് അനുവദ്യമായ ടൈപ്പ്:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* ഫയലിൽ ഓരോ ടൂളിനും ഇൻപുട്ട് സ്കീമകൾ സൂക്ഷിക്കുന്നു, ഇപ്പോൾ ഒരു സ്കീമ മാത്രമേ ഉണ്ടാകൂ, പുതിയ ടൂളുകൾ ചേർക്കുമ്പോൾ എൻട്രികൾ കൂട്ടാം:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

നല്ലത്, ഇനി ടൂൾ ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യാം.

### -3- ടൂൾ ലിസ്റ്റിംഗ് കൈകാര്യം

ടൂൾ ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യാൻ ഈ ഹാൻഡ്ലർ സെർവർ ഫയലിൽ ചേർക്കണം:

**Python**

```python
# സംക്ഷിപ്തമായതിനാൽ കോഡ് ഒഴിവാക്കിയിരിക്കുന്നു
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

`@server.list_tools` ഡെക്കറേറ്ററും `handle_list_tools` ഫംഗ്ഷനും ചേര്‍ത്തിട്ടുണ്ട്. ടൂൾ പಟ್ಟಿ സൃഷ്ടിക്കണം, ഓരോ ടൂളും name, description, inputSchema എന്നതു വേണം.

**TypeScript**

ടൂൾ ലിസ്റ്റിംഗിനായി സെർവറിൽ `setRequestHandler` ഉപയോഗിച്ച് schema ആയി `ListToolsRequestSchema` നല്കണം:

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
// സംക്ഷിപ്തമായി കോഡ് ഒഴിവാക്കിയിരിക്കുന്നു
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // രജിസ്റ്റർ ചെയ്ത ഉപകരണങ്ങളുടെ പട്ടിക തിരിച്ചു നൽകുക
  return {
    tools: tools
  };
});
```

ഇപ്പോൾ ടൂൾ ലിസ്റ്റിംഗ് ഭാഗം തീർന്നു. ഇനി ടൂൾ വിളിക്കൽ എങ്ങനെ ചെയ്യാമെന്ന് നോക്കാം.

### -4- ടൂൾ വിളിക്കൽ കൈകാര്യം

ടൂൾ വിളിക്കാൻ മറ്റൊരു ഹാൻഡ്ലർ ഒരുക്കണം. ഇത് ഏത് ഫീച്ചറിനെ വിളിക്കണമെന്ന് നിർദ്ദേശിക്കുന്ന റിക്വസ്റ്റ് കൈകാര്യം ചെയ്യും, അർഗ്യുമെന്റുകളും പരിശോധിക്കണം.

**Python**

`@server.call_tool` ഡെക്കറേറ്റർ ഉപയോഗിച്ച് `handle_call_tool` ഫംഗ്ഷൻ സൃഷ്ടിക്കുക. ഇതിൽ ടൂൾ നാമം, അർഗ്യുമെന്റുകൾ പാഴ്സ് ചെയ്ത് അവ ശരിയാണെന്ന് ഉറപ്പാക്കണം. പരിശോധനം ഈ ഫംഗ്ഷനിലോ ടീമിലോ ചെയ്യും.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools തിരെഞ്ഞെടുത്ത ഉപകരണങ്ങളുടെ പേരുകൾ കീകളാവുന്ന ഒരു നിഘണ്ടുവാണ്
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # ഉപകരണം പ്രവർത്തിപ്പിക്കുക
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

സംഗതികൾ:

- ടൂൾ നാമം `name` ഇൻപുട്ട് പാരാമീറ്ററായി ഇതിനകം ഉണ്ട്, അർഗ്യുമെന്റുകൾ `arguments` ഡിക്ഷണറിയിൽ.
- ടൂൾ `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` ആയി വിളിക്കുന്നു. അർഗ്യുമെന്റുകളുടെ പരിശോധന `handler` ഫംഗ്ഷനിൽ നടക്കുന്നു, പരാജയം ഉണ്ടെങ്കിൽ Exception ഉയരും.

ഇപ്പോൾ, ലോ-ലവൽ സെർവർ ഉപയോഗിച്ചുള്ള ടൂൾ ലിസ്റ്റിംഗ്, വിളിക്കൽ പൂർണമായി മനസ്സിലായി.

[പ്രധാന ഉദാഹരണം](./code/README.md) കാണുക

## അസൈൻമെന്റ്

നൽകിയ കോഡിൽ നിങ്ങൾ പുതിയ ടൂൾസ്, റിസോഴ്‌സസ്, പ്രോംപ്റ്റ് ചേർത്ത് നോക്കുക. നിങ്ങൾ കാണും, tools ഡയറക്ടറിയിൽ ഫയലുകൾ മാത്രം ചേർക്കണം, മറ്റെവിടെയും വേണ്ട.

*പരിഹാരമില്ല*

## സംഗ്രഹം

ഈ അധ്യായത്തിൽ, ലോ-ലവൽ സെർവർ സമീപനം എങ്ങനെ പ്രവർത്തിക്കുന്നുവെന്ന്, അതിലൂടെ ഒരു നല്ല ആർക്കിടെക്ചർ സൃഷ്ടിക്കാമെന്നും കണ്ടു. പരിശോധനയും, ഇൻപുട്ട് സ്കീമ നിർമ്മാണത്തിനു validation ലൈബ്രറികൾ ഉപയോഗിക്കുന്നതും പഠിച്ചു.

## അടുത്തത്

- അടുത്തത്: [സിമ്പിൾ അടെന്റിക്കേഷൻ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസ്വീകാരം**:  
ഈ രേഖ AI അനuvadana സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമ ചെയ്തതാണ്. നാം കൃത്യത നേടാൻ ശ്രമിച്ചിരുന്നുവെങ്കിലും, യാന്ത്രികതർജ്ജമകളിൽ പിശകുകൾ അല്ലെങ്കിൽ വ്യത്യാസങ്ങൾ ഉണ്ടാകുന്നത് സ്വാഭാവികമാണ്. യഥാർത്ഥ രേഖ മാനദണ്ഡമായ ഭാഷയിൽ ഉള്ളതായിരിക്കണം മിക്കവാറും വിശ്വസനീയമായ ഉറവിടം. നിർണ്ണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യൻ്റെ തർജ്ജമ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ തർജ്ജമ ഉപയോഗിക്കുന്നത് മൂലം ഉണ്ടാകുന്ന ഏതൊരു തെറ്റുവ്യാഖ്യാനങ്ങൾക്കും അല്ലെങ്കിൽ തെറ്റിദ്ധാരണകൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
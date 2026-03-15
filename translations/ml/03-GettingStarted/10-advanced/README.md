# ശ്രദ്ധേയമായ സര്‍വര്‍ ഉപയോഗനം

MCP SDK-യില്‍ രണ്ട് വ്യത്യസ്തതം ഉള്ള സര്‍വറുകള്‍ നല്‍കുന്നു, സാധാരണ സര്‍വറും ലോ-ലെവല്‍ സര്‍വറും. സാധാരണ, പുതിയ ഫീച്ചറുകള്‍ ചേര്‍ക്കാന്‍ സാധാരണ സര്‍വര്‍ ഉപയോഗിക്കും. ചില പ്രത്യേക സാഹചര്യങ്ങളില്‍ however, ലോ-ലെവല്‍ സര്‍വറിനെ ആശ്രയിക്കേണ്ടിവരും ഉദാഹരണത്തിന്:

- മെച്ചപ്പെട്ട ആർക്കിടെക്ചർ. സാധാരണ സര്‍വറും ലോ-ലെവല്‍ സര്‍വറും ഒരുമിച്ച് ഒരു ശുദ്ധമായ ആർക്കിടെക്ചർ സൃഷ്ടിക്കാം, പക്ഷേ ലോ-ലെവല്‍ സര്‍വറിനൊപ്പം അത് കുറച്ച് എളുപ്പമാക്കാം എന്ന വാദം ഉണ്ട്.
- ഫീച്ചർ ലഭ്യത. ചില ഉയർന്ന നിലവാരത്തിലുള്ള ഫീച്ചറുകൾ മാത്രം ലോ-ലെവല്‍ സര്‍വറിനൊപ്പം ഉപയോഗിക്കാം. ഇത് Sampling ഉം Elicitation ഉം ചേര്‍ക്കുമ്പോള്‍ പിന്നീട് കണ്ടു പോകാം.

## സാധാരണ സര്‍വര്‍ vs ലോ-ലെവല്‍ സര്‍വര്‍

സാധാരണ സര്‍വറുപയോഗിച്ച് MCP സര്‍വര്‍ സൃഷ്ടിക്കുന്നത് ഇങ്ങനെ കാണാം

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

// ഒരു കൂട്ടിച്ചേർക്കൽ ടൂൾ ചേർക്കുക
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

അര്‍ഥം, നിങ്ങള്‍ സര്‍വറിന്റെ വേണ്ടിയുള്ള ഓരോ ടൂൾ, റിസോഴ്‌സ്, പ്രാംപ്്റ്റ് എന്നിവയ്ക്കും വ്യക്തമായായി ചേർക്കുന്നു. ഇതില്‍ പിഴവുള്ളത് ഒന്നും ഇല്ല.  

### ലോ-ലെവല്‍ സര്‍വര്‍ രീതിവഴി

പക്ഷേ, ലോ-ലെവല്‍ സര്‍വര്‍ രീതിവഴി ഉപയോഗിച്ചാല്‍ വേറുതായി ചിന്തിക്കേണ്ടിവരും. ഓരോ ടൂൾ രജിസ്റ്റർ ചെയ്യുന്നതിനുപകരം, ഓരോ ഫീച്ചര്‍ തരത്തിനും (tools, resources, prompts) രണ്ട് ഹാന്‍‌ഡിലറുകൾ സൃഷ്ടിയ്ക്കുകയും ചെയ്യണം. ഉദാഹരണത്തിന് ടൂളുകൾക്ക് രണ്ടു ഫംഗ്ഷനുകൾ മാത്രമേ ഉള്ളൂ, ഇങ്ങനെ:

- എല്ലാ ടൂളുകളും ലിസ്റ്റ് ചെയ്യല്‍. ഒരു ഫംഗ്ഷന്‍ എല്ലാ ടൂൾ ലിസ്റ്റിങ് ശ്രമങ്ങൾക്ക് ഉത്തരവാദിയാകും.
- എല്ലാ ടൂളുകളും വിളിക്കാനുള്ള ഹാന്‍‌ഡിലിംഗ്. ഇവിടെ ഒറ്റ ഫംഗ്ഷന്‍ തന്നെ ടൂൾ വിളിക്കലുകള്‍ കൈകാര്യം ചെയ്യും.

ഇത് കുറച്ച് കുറവ് ജോലി പോലെ തോന്നുന്നില്ലേ? അതായത് ടൂൾ രജിസ്റ്റർ ചെയ്യാതെ, ടൂൾ ലിസ്റ്റുള്ളപ്പോൾ അത് ലിസ്റ്റിലും, ന്റെട്കോൾ വരുന്നപ്പോൾ വിളിക്കും ഉറപ്പാക്കുക മാത്രം.

ഇപ്പോള്‍ കോഡ് എങ്ങനെയാണ് എന്നു നോക്കാം:

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
  // രജിസ്റ്റർ ചെയ്ത ടൂളുകളുടെ പട്ടിക മടക്കുക
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

ഇവിടെ ഒരു ഫംഗ്ഷന്‍ ഫീച്ചറുകളുടെ ലിസ്റ്റ് തിരികെ നൽകുന്നു. tools ലിസ്റ്റിലെ ഓരോ എൻട്രിക്കും `name`, `description`, `inputSchema` പോലുള്ള ഫീൽഡുകൾ ഉണ്ട്, റിട്ടേൺ ടൈപ്പിന് അനുസൃതമായി. ഇതുവഴി, ടൂളുകളും ഫീച്ചർ ഡെഫിനിഷൻ മറ്റൊരിടത്തും വെക്കാം. ഇനി tools ഫോൾഡറിൽ എല്ലാ ടൂളുകളും സൃഷ്ടിയ്ക്കാം, അതുപോലെ തന്നെയാണ് നിങ്ങളുടെ എല്ലാ ഫീച്ചറുകൾക്കും; പണിയടി ഈപദ്ധതി അങ്ങനെ ക്രമീകരിക്കാം:

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

അതെ, നമ്മുടെ ആർക്കിടെക്ചർ വളരെ ശുദ്ധവും നല്ലതുമായിരിക്കും.

ടൂളുകൾക്ക് കോൾ ചെയ്യുന്നതെന്ത് ആകും, ഒറ്റ ഹാന്‍‌ഡിലറാണോ എല്ലാ ടൂളുകളും വിളിക്കാനുള്ളത്? അതേ, കൃത്യമായും, ഇതാ അതിന്റെ കോഡ്:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools എന്നത് ടൂളുകളുടെ പേരുകളാണ് കീകൾ ഉള്ള ഒരു നിഘണ്ടു
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

മുകളിൽ നിന്നും കാണാം, വിളിക്കേണ്ട ടൂൾ, ഏതൊക്കെ arguments എന്നിവ പാഴ്സ് ചെയ്ത്, ടൂൾ വിളിക്കേണ്ടതുണ്ട്.

## സാധുത മെച്ചപ്പെടുത്തല്‍

ഇവരെക്കുറിച്ചും ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രാംപ്്റ്റുകൾ എന്നിവ ചേർക്കുന്ന എല്ലാ രജിസ്ട്രേഷനുകളും ഈ രണ്ട് ഹാന്‍‌ഡിലർ പാര്ട്ട് ഒന്നിനുപകരം ഉപയോഗിക്കാം എന്നത് കാണിച്ചു. ഇനി വേറെ എന്താണ് ചെയ്യേണ്ടത്? ടൂൾ ശരിയായ arguments ഉപയോഗിച്ച് വിളിക്കപ്പെട്ടിട്ടുണ്ടെന്ന് സംശയം ഒഴിവാക്കാൻ സാധുത വരുത്തണം. ഓരോ റൺടൈമിനും ഇതിന് തനതു പരിഹാരമുണ്ട്. ഉദാ. Python-ല്‍ Pydantic ഉപയോഗിക്കുന്നു, TypeScript-ല്‍ Zod. ആശയം:

- ഒരു ഫീച്ചർ (tool, resource or prompt) സൃഷ്ടിക്കുന്നതിന് ലോഗിക് അത് നിര്‍ദിഷ്‌ട ഫോൾഡറിൽ മാറ്റുക.
- ടൂൾ വിളിക്കാൻ വരുന്ന request ശരിയായ തരം ആണെന്ന് സാധുവാക്കേണ്ട വഴിയുണ്ടാക്കുക.

### ഒരു ഫീച്ചർ സൃഷ്ടിക്കുക

ഒരു ഫീച്ചർ സൃഷ്ടിക്കേണ്ടത് അതിന് ഒരു ഫയല്‍ ഉണ്ടാക്കി അതിലെ നിര്‍ബന്ധമായ ഫീൽഡുകൾ ചേർക്കുക ആണ്. ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രാംപ്്റ്റുകൾ എന്നിവയ്ക്കിടയിൽ ഫീൽഡുകൾ വ്യത്യസ്തമാണ്.

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
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് പരിശോദിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, അതിലൂടെ നാം ഒരു AddInputModel സൃഷ്ടിച്ചു ആർക്കുകൾ പരിശോദിക്കാം

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

- Pydantic ഉപയോഗിച്ച് `AddInputModel` എന്ന സ്കീമ സൃഷ്ടിക്കുന്നു, ഫീൽഡുകൾ `a` and `b` ആണ്, *schema.py* ഫയലിൽ.
- വരുന്ന request `AddInputModel` ആയിരിക്കും എന്ന് parse ചെയ്യാൻ ശ്രമിക്കുന്നു, parameters ഒക്കെ പൊരുത്തപ്പെടാതെയുള്ളാലും ഇത് ക്രാഷ് ചെയ്യും:

   ```python
   # add.py
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് പുതുക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ഈ parsing ലോഗിക് ടൂൾ കോൾ തന്നെ അല്ലെങ്കിൽ ഹാന്‍‌ഡിലർ ഫംഗ്ഷനിൽ വെക്കാം.

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

- എല്ലാ ടൂൾ കോൾ കൈകാര്യം ചെയ്യുന്ന ഹാന്‍‌ഡിലറിൽ, വരുന്ന request ടൂൾ നിർദ്ദിഷ്‌ട സ്കീമയിൽ പാഴ്സ് ചെയ്യാൻ ശ്രമിക്കുന്നു:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ഇത് വിജയിച്ചാൽ ടൂൾ കോൾ ചെയ്യും:

    ```typescript
    const result = await tool.callback(input);
    ```

ഈ രീതിയിലൂടെ നല്ല നീരീക്ഷണമുള്ള ആർക്കിടെക്ചർ ഉണ്ടാകുന്നു, *server.ts* വളരെ ചെറിയ ഫയൽ ആണ്, വെറും req handlers വയറിങ്ങ് മാത്രം ചെയ്യുന്നു. ഓരോ ഫീച്ചറും തങ്ങളുടേതായ ഫോൾഡറിൽ (tools/, resources/, prompts/) ആണ്.

നല്ലതു, ഇനി ഇത് കെട്ടിപ്പടുക്കാം.

## പരിചയം: ലോ-ലെവല്‍ സർവര്‍ സൃഷ്ടിക്കല്‍

ഇവിടെ ചെയ്യേണ്ടത്:

1. tools ലിസ്റ്റ് ചെയ്യുന്നതും tools വിളിയ്ക്കുന്നതുമായ ലോ-ലെവല്‍ സര്‍വര്‍ സൃഷ്ടിക്കുക.
1. കെട്ടിടാശയം സ്ഥാപിക്കുക.
1. നിങ്ങളുടെ ടൂൾ കോൾ ശരിയായി സാധുക്കളായി സാധുവാക്കാൻ സാധുത ചേര്‍ക്കുക.

### -1- ഒരു കെട്ടിടാശയം സൃഷ്ടിക്കുക

ആദ്യമായി പരിഹരിക്കുക എന്ന് നോക്കുന്നത് വളരെയധികം ഫീച്ചറുകള്‍ ചേർക്കുമ്പോള്‍ സ്കെയിലുചെയ്യാന്‍ സഹായിക്കുന്ന ഒരു ആർക്കിടെക്ചർ ആണ്, ഇങ്ങനെ കാണാം:

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

ഇനി tools ഫോള്‍ഡറിൽ ടൂളുകൾ എളുപ്പം ചേർത്തെടുക്കാം. ആവശ്യം തോന്നിയാല്‍ resources, prompts എന്നിവയ്ക്കും സബ് ഡയറക്ടറികൾ ഈപോലെ കൂട്ടാം.

### -2- ഒരു ടൂൾ സൃഷ്ടിക്കുക

ടൂൾ സൃഷ്ടിക്കല്‍ ഇങ്ങനെ കാണാം. ആദ്യം അത് *tool* സബ് ഡയറക്ടറിയിലായിരിക്കണം:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, അതിലൂടെ ഞങ്ങൾക്കായി ഒരു AddInputModel സൃഷ്ടിക്കാനും args സാധുത പരിശോധന നടത്താനും കഴിയും

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ഇവിടെ കാണുന്നതെന്തെന്നാല്‍ નામം, വിവരണം, input schema Pydantic ഉപയോഗിച്ച് നിർവ്വചിക്കുന്നു, ടൂൾ വിളിക്കുമ്പോള്‍ പ്രവർത്തിക്കുന്ന ഹാന്‍‌ഡിലർ ഉണ്ട്. ഒടുവിൽ, `tool_add` എന്ന dict ആക്യുന്നു, എല്ലാ പ്രോപ്പർട്ടികളും ഇവിടെ ചേർന്നിരിക്കുന്നു.

*schema.py* എന്ന ഫയലും ഉണ്ട് ടൂളിന് ഉപയോഗിക്കുന്ന input schema നിർവ്വചിക്കാൻ:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

*__init__.py* ഉള്ളടക്കം പൂരിപ്പിക്കണം tools ഡയറക്ടറി ഒരു മോഡ്യൂൾ ആക്കാൻ. കൂടാതെ അതിലെ മാഡ്യൂളുകളും പുറത്താക്കണം ഇങ്ങനെ:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

ഇനിയും ടൂളുകൾ കൂട്ടിച്ചേർക്കുമ്പോൾ ഈ ഫയൽ അപ്ഡേറ്റ് ചെയ്യാം.

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

ഇവിടെ dict സൃഷ്ടിക്കുന്നു:

- name, ടൂൾയുടെ പേര്.
- rawSchema, Zod സ്കീമ, വരുന്ന ടൂൾ കോൾ request-നെ സാധുവാക്കാൻ ഉപയോഗിക്കും.
- inputSchema, ഹാന്‍‌ഡിലർ ഉപയോഗിക്കുന്നു്.
- callback, ടൂൾ പ്രവർത്തിപ്പിക്കാൻ.

`Tool` എന്നത് ഈ dict ടൈപ്പിലേക്ക് മാറ്റുന്നു MPL server ഹാന്‍‌ഡിലർ ഉപയോഗിക്കാവുന്ന വിധത്തിൽ:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* ഫയൽ ഉണ്ട്, ഓരോ ടൂളിന്റെയും input schemas സൂക്ഷിക്കുന്നു ഇങ്ങനെ, ഇപ്പോള്‍ ഒരു(schema മാത്രം ഉണ്ട്, കൂട്ടുമ്പോൾ കൂടുതലുണ്ട്):

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

നല്ലതു, ഇനി tools ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യാം.

### -3- tools ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യുക

tools ലിസ്റ്റ് ചെയ്യാനുള്ള request handler സജ്ജമാക്കണം. സർവർ ഫയലിൽ ചേർക്കേണ്ടത് ഇതാണ്:

**Python**

```python
# ലഘുക്കിപ്പിന് കോഡ് ഉളളിലപ്പെടുത്തി
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

`@server.list_tools` ഡികോറേറ്റർ ചേർക്കുന്നു, ഫംഗ്ഷന് `handle_list_tools` ആണ്. ഇവിടെ tools ലിസ്റ്റ് തയ്യാറാക്കണം. tools ഓരോന്നിനും name, description, inputSchema വേണം.   

**TypeScript**

tools ലിസ്റ്റ് ചെയ്യാനുള്ള request handler സജ്ജമാക്കാൻ, `setRequestHandler` സർവറിന് വിളിക്കണം, അതിനായി `ListToolsRequestSchema` ഉപയോഗിക്കുന്നു:

```typescript
// ഇൻഡക്സ്.ts
import addTool from "./add.js";
import subtractTool from "./subtract.js";
import {server} from "../server.js";
import { Tool } from "./tool.js";

export let tools: Array<Tool> = [];
tools.push(addTool);
tools.push(subtractTool);

// സേര്‍വര്.ts
// ലഘുചിത്രത്തിന് കോഡ് ഒഴിവാക്കിയിരിക്കുന്നു
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // രജിസ്റ്റർ ചെയ്ത ഉപകരണങ്ങളുടെ പട്ടിക തിരികെ നൽകുക
  return {
    tools: tools
  };
});
```

നല്ലത്, tools ലിസ്റ്റിങ്ങ് പൂർത്തിയാക്കി, ഇനി ടൂളുകൾ വിളിക്കാൻ നോക്കാം.

### -4- ടൂൾ വിളിക്കൽ കൈകാര്യം ചെയ്യുക

ടൂൾ വിളിക്കാനുള്ള request handler വേണം, ഏത് ഫീച്ചർ വിളിക്കണമെന്ന്, എന്ത് arguments എന്നിവ കൈകാര്യം ചെയ്യണം.

**Python**

`@server.call_tool` ഡികോറേറ്റർ ഉപയോഗിച്ച്, `handle_call_tool` ഫംഗ്ഷന് നിർമ്മിക്കുക. ടൂൾ നാമം, arguments പാഴ്സ് ചെയ്ത്, arguments ശരിയ്ക്കാണെന്ന് ഉറപ്പാക്കേണ്ടത് ഈ ഫംഗ്ഷനിലാണ്. arguments ഈ ഫംഗ്ഷനിലോ ടൂളിന് ആവശ്യമുള്ള അടിസ്ഥാനത്തിലോ സാധുവാക്കാം.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools എന്നത് ടൂൾ നാമങ്ങളെ കീകൾ ആയി അടങ്ങിയ ഒരു ഡിക്ഷണറിയാണ്
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

- ടൂൾ നാമം `name` പാരാമീറ്ററിലുണ്ട്, arguments `arguments` dictionary ആയിരിക്കും.

- ടൂൾ കോൾ ചെയ്യുന്നുണ്ട് `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. arguments സാധുത `handler` ഫംഗ്ഷനിൽ പരിശോധിക്കും, പരാജയം ഉണ്ടെങ്കില്‍ exception ഉയരും. 

ഇങ്ങനെ tools ലിസ്റ്റിംഗ്, calling എന്നിവ ലോ-ലെവല്‍ സര്‍വറുമായി എങ്ങനെ ചെയ്യാമെന്ന് പൂര്‍ണ്ണമായും മനസ്സിലായി.

[പൂർണ്ണ ഉദാഹരണം](./code/README.md) കാണുക

## അസൈന്‌മെന്റ്

നൽകിയിരിക്കുന്ന കോഡിൽ tools, resources, prompts കൂട്ടിച്ചേർക്കുക, ഒരുമിച്ച് ശ്രദ്ധിക്കണം tools ഡയറക്ടറിയിൽ മാത്രമെ ഫയലുകൾ കൂട്ടിച്ചേർക്കേണ്ടതുള്ളൂ എന്ന്.

*എന്തു പരിഹാരവും നൽകിയിട്ടില്ല*

## സംക്ഷേപം

ഈ അധ്യായത്തിൽ ലോ-ലെവല്‍ സർവര്‍ ഏങ്ങനെ പ്രവർത്തിക്കുമെന്ന്, നല്ല ആർക്കിടെക്ചർ എങ്ങിനെ ഉണ്ടാക്കാം എന്ന് കാണിച്ചു. സാധുത കുറിച്ച് സംസാരിക്കുകയും, വിവിധ സാധുത ലൈബ്രറികൾ ഉപയോഗിച്ച് input validation സ്കീമകൾ എങ്ങനെ സൃഷ്ടിക്കുന്നു എന്നു പഠിപ്പിച്ചു.

## അടുത്തത്

- അടുത്തത്: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**മാപ്പ്**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ തികച്ചും കൃത്യതയ്ക്കായി ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ അപ്രൂ ബന്ധങ്ങൾ ഉണ്ടായേക്കാമെന്ന് ദയവായി മനസിലാക്കുക. അതിനാൽ, യഥാർത്ഥ ഭാഷയിലുള്ള ഡോക്യുമെന്റ് പ്രാധാന്യമുള്ള സ്രോതസ്സായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനുഷിക വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനത്തെ അടിസ്ഥാനമാക്കിയുള്ള യാതൊരു തെറ്റിദ്ധാരണകൾക്കും ഞങ്ങൾ ഉത്തരവാദിത്വം വഹിക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# പുരോഗമിച്ച സെർവർ ഉപയോഗം

MCP SDK-യിൽ രണ്ട് വ്യത്യസ്ത തരത്തിലുള്ള സെർവർകൾ ഉണ്ട്, നിങ്ങളുടെ സാധാരണ സെർവർയും ലോ ലെവൽ സെർവർയും. സാധാരണയായി, നിങ്ങൾ സാധാരണ സെർവർ ഉപയോഗിച്ച് അതിനെ ഫീച്ചറുകൾ ചേർക്കാൻ ഉപയോഗിക്കും. ചില സാഹചര്യങ്ങളിൽ, നിങ്ങൾ ലോ ലെവൽ സെർവർ ആശ്രയിക്കണമെന്ന് ആഗ്രഹിക്കുന്നതാണ്, ഉദാ:

- മെച്ചപ്പെട്ട ആർക്കിടെക്ചർ. സാധാരണ സെർവർയും ലോ ലെവൽ സെർവർയും ഉപയോഗിച്ച് സുചിത റിതിയിൽ ആർക്കിടെക്ചർ സൃഷ്ടിക്കാൻ സാധിക്കാം, പക്ഷേ ലോ ലെവൽ സെർവറോടെ ഇത് കുറച്ചു എളുപ്പമാണ് എന്ന് പറയാനാകും.
- ഫീച്ചർ ലഭ്യത. ചില പുരോഗമിച്ച ഫീച്ചറുകൾ മാത്രമേ ലോ ലെവൽ സെർവറോടുകൂടി ഉപയോഗിക്കാനാകൂ.
    പിന്നീട് അദ്ധ്യായങ്ങളിൽ Elicitation-ഉം legacy Sampling
    ഫീച്ചറും ഉൾപ്പെടുത്തുന്നു, ഇത് MCP `2026-07-28`-ൽ ഒഴിവാക്കി.

## സാധാരണ സെർവറും ലോ ലെവൽ സെർവറും തമ്മിലുള്ള വ്യത്യാസം

സാധാരണ സെർവറിനൊപ്പം MCP സെർവർ സൃഷ്ടിക്കുന്നതിന്റെ രൂപം ഇതുപോലെ ആണ്

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

ലക്ഷ്യം ഏത് ടൂൾ, വിഭവം, പ്രോംപ്റ്റ് സെർവറിന് ലഭ്യമാക്കണമെന്ന് വ്യക്തമായി ചേർക്കുകയാണ്. അതിൽ എന്തെങ്കിലും തെറ്റ് ഇല്ല.  

### ലോ ലെവൽ സെർവർ സമീപനം

എന്നാൽ ലോ ലെവൽ സെർവർ സമീപനം ഉപയോഗിക്കുമ്പോൾ, ഇത് വ്യത്യസ്തമായി ചിന്തിക്കണം. ഓരോ ഫീച്ചർ തരം (ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾ)ക്ക് രണ്ട് ഹാൻഡ്ലറുകൾ സൃഷ്ടിക്കണം. ഉദാഹരണത്തിന് ടൂളുകൾക്ക് രണ്ടു ഫംഗ്ഷനുകൾ മാത്രമാണുള്ളത്:

- എല്ലാ ടൂളുകളും ലിസ്റ്റ് ചെയ്യുക. ഒരു ഫംഗ്ഷൻ ടൂളുകൾ ലിസ്റ്റ് ചെയ്യാനുള്ള എല്ലാ ശ്രമങ്ങൾക്കും ഉത്തരവാദിയാണ്.
- എല്ലാ ടൂൾ വിളികളും കൈകാര്യം ചെയ്യുക. ഇവിടെ കൂടി ഒരു ഫംഗ്ഷൻ മാത്രം ടൂൾ വിളികൾ കൈകാര്യം ചെയ്യുന്നു.

ഇത് കുറവ് ജോലി ആകാമെന്ന് തോന്നുന്നില്ലേ? അതായത് ഒരു ടൂൾ രജിസ്റ്റർ ചെയ്യുന്നതിന് പകരം, ഞാൻ ഓരോ ടൂളും ലിസ്റ്റിൽ ഉണ്ടെന്നത് ഉറപ്പാക്കണം, കൂടാതെ ടൂൾ വിളിക്കാൻ ആവശ്യപ്പെട്ടാൽ അത് വിളിക്കണം.

ഇപ്പോൾ കോഡ് ഇങ്ങനെ കാണാം:

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
  // റജിസ്റ്റർ ചെയ്തിട്ടുള്ള ടൂളുകളുടെ ലിസ്റ്റ് മടക്കി നൽകുക
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

ഇവിടെ ഓരോ ഫീച്ചറിന്റെ ഒരു ലിസ്റ്റ് റിട്ടേൺ ചെയ്യുന്ന ഫംഗ്ഷൻ ഉണ്ട്. ടൂളുകളുടെ ലിസ്റ്റിലുള്ള ഓരോ എൻട്രിക്കും `name`, `description`, `inputSchema` പോലുള്ള ഫീൽഡുകൾ ഉണ്ടാകണം റിട്ടേൺ തരം പാലിക്കാൻ. ഇത് ടൂളുകളും ഫീച്ചർ നിർവചനങ്ങളും വേറിടാൻ സഹായിക്കുന്നു. നമ്മുടെ എല്ലാ ടൂളുകളും tools ഫോൾഡറിൽ സൃഷ്ടിക്കാം, അതുപോലെ തന്നെ എല്ലാ ഫീച്ചറുകളും; പ്രോജക്ട് ഇങ്ങനെ ക്രമീകരിക്കാം:

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

അതിനോട് അനുയോജ്യമായി നമ്മുടെ ആർക്കിടെക്ചർ കൂടി സുചിതമായി കാണാം.

ടൂളുകൾ വിളിക്കുന്നത് എങ്ങനെ? ഐഡിയ ഒരേപോലെ തന്നേ, ഒരു ഹാൻഡ്ലർ ഏതൊരു ടൂളും വിളിക്കുന്നത് കൈകാര്യം ചെയ്യുമോ? അതെ, ഇവിടെ അത് നടത്താനുള്ള കോഡ്:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ഒരു നിഘണ്ടുവാണ്, അതിൽ ടൂൾ നെയിമുകൾ കീ എന്ന നിലയിൽ ഉണ്ട്
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

മുകളിൽ നൽകിയ കോഡിൽ നിന്നും കാണാനാകും, ടൂൾ ഏതാണ് വിളിക്കേണ്ടതെന്ന്, ആർക്ക് എന്ത് ഉൾക്കൊള്ളണമെന്നും പാഴ്സ്ചെയ്യണം, പിന്നെ ടൂൾ വിളിക്കാനാണ് മുന്നോട്ട് പോവേണ്ടത്.

## സ്ഥിരീകരണത്തോടെ സമീപനം മെച്ചപ്പെടുത്തൽ

ഇതുവരെയായി, ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾ ചേർക്കുന്ന എല്ലാ രജിസ്ട്രേഷനുകളും ഓരോ ഫീച്ചർ തരംപ്രകാരമുള്ള രണ്ട് ഹാൻഡ്ലറുകൾ കൊണ്ട് മാറ്റാം. ഇപ്പോൾ എന്ത് ചെയ്യണം? ടൂൾ വിളിക്കുമ്പോൾ ശരിയായ ആർഗ്യുമെന്റുകൾ ഉപയോഗിക്കപ്പെടുന്നതെന്ന് ഉറപ്പാക്കാൻ ഏതെങ്കിലും സ്വഭാവത്തിലുള്ള സ്ഥിരീകരണം ചേർക്കണം. ഓരോ റൺടൈമിനും ഈ രംഗത്ത് തങ്ങളുടെ പരിഹാരങ്ങളുണ്ട്, ഉദാഹരണത്തിന് Python Pydantic ഉപയോഗിക്കുന്നു, TypeScript Zod ഉപയോഗിക്കുന്നു. ആശയം താഴെപറയുന്നത് പോലെ ആണ്:

- ഒരു ഫീച്ചർ (ടൂൾ, വിഭവം, പ്രോംപ്റ്റ്) സൃഷ്ടിക്കുന്ന ലോഗിക് അതിന്റെ സമർപ്പിത ഫോൾഡറിൽ മാറ്റുക.
- ഒരു ഇൻകമിംഗ് അഭ്യർത്ഥനക്ക്, ഉദാഹരണത്തിന് ടൂൾ വിളിക്കാനായി ആവശ്യപ്പെടുമ്പോൾ, അതിനെ ശരിവെക്കാൻ വഴി ചേർക്കുക.

### ഒരു ഫീച്ചർ സൃഷ്ടിക്കൂ

ഒരു ഫീച്ചർ സൃഷ്ടിക്കാൻ, ആ ഫീച്ചറിനായി ഒരു ഫയൽ സൃഷ്ടിച്ച് അതിനുള്ള നിർബന്ധമായ ഫീൽഡുകൾ ചേർക്കണം. ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾക്കിടയിൽ ഫീൽഡുകൾ കുറച്ചു വ്യത്യാസം ഉണ്ടാകാം.

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
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് പരിശോധന നടത്തുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, ώστε നാം ഒരു AddInputModel സൃഷ്ടിച്ച് арг്സ് പരിശോധന നടത്താൻ കഴിയും

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

താഴെ പറയുന്നതുപോലെ ചെയ്യുന്നതാണ് കാണുന്നത്:

- Pydantic ഉപയോഗിച്ച് `AddInputModel` എന്ന സ്കീമ സൃഷ്ടിക്കുക, *schema.py* ഫയലിൽ ഫീൽഡുകൾ `a` , `b` എന്നിവ ചേർക്കുക.
- ഇൻകമിംഗ് അഭ്യർത്ഥനം `AddInputModel` തരത്തിൽ പാഴ്സ്ചെയ്യാൻ ശ്രമിക്കുക, പാരാമീറ്ററുകളിൽ പൊരുത്തക്കേട് ഉണ്ടെങ്കിൽ ഇത് ക്രാഷ് ചെയ്യും:

   ```python
   # add.py
    try:
        # പൈഡാന്റിക് മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുത പരിശോധിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

ഈ പാഴ്സിംഗ് ലോഗിക് ടൂൾ കോളിൽ തന്നെ വച്ചുപോവുകയോ ഹാൻഡ്ലർ ഫംഗ്ഷനിലോ വയ്ക്കാം.

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

       // @ts-അഗ്നൈഗ്നോർ
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

- ടൂൾ വിളികളെ കൈകാര്യം ചെയ്യുന്ന ഹാൻഡ്ലറിൽ, ഇൻകമിംഗ് അഭ്യർത്ഥനം ടൂളിന്റെ സ്കീമയിലേക്ക് പാഴ്സ് ചെയ്യാൻ ശ്രമിക്കുന്നു:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ഇത് സഫലമായാൽ πραγματικό ടൂൾ കോളിലേക്ക് മുന്നോട്ട് പോവുന്നു:

    ```typescript
    const result = await tool.callback(input);
    ```

കാണുന്നതുപോലെ, ഈ സമീപനം മികച്ച ആർക്കിടെക്ചർ സൃഷ്ടിക്കുന്നു. *server.ts* വളരെ ചെറിയ ഫയലാണ്, വെറും ഹാൻഡ്ലറുകൾ ഘടിപ്പിക്കുന്നു, ഓരോ ഫീച്ചറും അവരുടെ അതേ ഫോൾഡറിൽ ആണ്; tools/, resources/, അല്ലെങ്കിൽ prompts/.

നന്നെ, ഇനി ഇത് നമുക്ക് നിർമ്മിക്കാം.

## അഭ്യാസം: ലോ ലെവൽ സെർവർ സൃഷ്ടിക്കൽ

ഈ അഭ്യാസത്തിൽ നാം നൽകാനുള്ളത്:

1. ടൂളുകളുടെ ലിസ്റ്റിംഗ്, ടൂൾ കോളിംഗ് കൈകാര്യം ചെയ്യുന്ന ലോ ലെവൽ സെർവർ സൃഷ്ടിക്കുക.
1. നിങ്ങൾ വളർത്താൻ കഴിയുന്ന ആർക്കിടെക്ചർ നടപ്പിലാക്കുക.
1. ടൂൾ കോളുകൾ ശരിയായ രീതിയിൽ സ്ഥിരീകരിക്കപ്പെടുന്നുവെന്ന് ഉറപ്പാക്കാൻ സ്ഥിരീകരണം ചേർക്കുക.

### -1- ഒരു ആർക്കിടെക്ചർ സൃഷ്ടിക്കുക

കൂടുതൽ ഫീച്ചറുകൾ ചേർക്കുമ്പോൾ എങ്ങനെ സ്കെയിൽ ചെയ്യാമെന്ന് സഹായിക്കുന്ന ഒരു ആർക്കിടെക്ചർ പരിഗണിക്കാം, ഇങ്ങനെ കാണാം:

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

ഇപ്പോൾ tools ഫോൾഡറിൽ പുതിയ ടൂളുകൾ ചേർക്കാൻ എളുപ്പമുള്ള ഒരു ആർക്കിടെക്ചർ ഒരുക്കിയിട്ടുണ്ട്. resources, prompts എന്നിവയ്ക്കായി സബ്ഡയറക്ടറികൾ നിർമിക്കാൻ അനുമതിയുണ്ട്.

### -2- ഒരു ടൂൾ സൃഷ്ടിക്കൽ

ടൂൾ സൃഷ്ടിക്കലിന്റെ പ്രത്യക്ഷം കാണാം. ആദ്യം അത് *tool* സബ്‌ഡയറക്ടറിയിൽ സൃഷ്ടിക്കണം, ഇങ്ങനെ:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Pydantic മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് സാധുതാപരിപ്പിക്കുക
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic ചേർക്കുക, ώστε μπορούμε να δημιουργήσουμε ένα AddInputModel και να επικυρώσουμε τα args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ഇവിടെ നാം βλέക്കുന്നത് പോലെ, നാം Pydantic ഉപയോഗിച്ച് name, description, input schema നിർവചിക്കുന്നു, ടൂൾ വിളിക്കുമ്പോൾ വിളിക്കാവുന്ന ഹാൻഡ്ലറും. അവസാനത്തിലും `tool_add` എന്ന ഡിക്ഷണറി എല്ലാ പ്രോപ്പർട്ടികളും കൈവശം വയ്ക്കുന്നു.

ഒരു *schema.py* ഫയൽ കൂടി ഉണ്ട്, ടൂളിന്റെ ഇൻപുട്ട് സ്കീമ നിർവചിക്കാൻ.

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

tools ഡയറക്ടറി ഒരു മോഡ്യൂളായി പരിഗണിക്കാൻ *__init__.py* പൂരിപ്പിക്കണം. കൂടാതെ ഇൻപുട്ട് മോഡ്യൂളുകൾ ഇവിടുകൾ വഴി പുറത്തെടുക്കണം:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

പുതിയ ടൂളുകൾ കൂട്ടിച്ചേർക്കുമ്പോൾ ഈ ഫയൽ അപ്‌ഡേറ്റ് ചെയ്യുക.

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

ഇവിടെ നാം ഒരു ഡിക്ഷണറി സൃഷ്ടിക്കുന്നു, ഇതിൽ പ്രോപ്പർട്ടികൾ ഉൾപ്പെടുന്നു:

- name, ടൂളിന്റെ പേര്.
- rawSchema, Zod സ്കീമ, ടൂൾ വിളിക്കുന്ന ഇൻകമിംഗ് അഭ്യർത്ഥനകളെ സ്ഥിരീകരിക്കാൻ ഉപയോഗിക്കുന്നു.
- inputSchema, ഹാൻഡ്ലർ ഉപയോഗിക്കുന്ന സ്കീമ.
- callback, ടൂൾ പ്രവർത്തിപ്പിക്കാൻ ഉപയോഗിക്കുന്നു.

`Tool` ടൈപ്പ് ഉപയോഗിച്ച് ഡിക്ഷണറി ഒരു ടൈപ്പായി പരിവർത്തനം ചെയ്യുന്നു, ഇത് MCP സെർവർ ഹാൻഡ്ലർ സ്വീകരിക്കും:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

*schema.ts* ഫയലിൽ ഓരോ ടൂളിനും ഇൻപുട്ട് സ്കീമ സൂക്ഷിക്കുന്നു, ഇപ്പോൾ ഒറ്റ സ്കീമ മാത്രമാണ് ഉണ്ടെങ്കിലും പുതിയ ടൂളുകൾ ചേർക്കുമ്പോൾ കൂടുതൽ ചേർക്കാം:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

നന്നായി, ഇനി നമുക്ക് ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുന്നത് കൈകാര്യം ചെയ്യാം.

### -3- ടൂൾ ലിസ്റ്റിംഗ് കൈകാര്യം ചെയ്യുക

ടൂളുകൾ ലിസ്റ്റ് ചെയ്യാൻ ഒരു അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാനുള്ള ഹാൻഡ്ലർ സജ്ജീകരിക്കണം. സെർവർ ഫയലിൽ ചേർക്കേണ്ടത് ഇങ്ങനെ:

**Python**

```python
# ചുരുക്കത്തിന് കോഡ് ഒഴിവാക്കിയിരിക്കുന്നു
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

ഇവിടെ `@server.list_tools` ഡികോറേറ്റർ ചേർക്കുന്നു, `handle_list_tools` എന്ന ഫംഗ്ഷൻ നടപ്പാക്കുന്നു. ഈ ഫംഗ്ഷൻ ടൂളുകളുടെ ലിസ്റ്റ് സൃഷ്ടിക്കണം. ഓരോ ടൂളിനും name, description, inputSchema ഉണ്ടായിരിക്കണം.   

**TypeScript**

ടൂളുകൾ ലിസ്റ്റ് ചെയ്യാൻ അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാൻ സെർവറിൽ `setRequestHandler` ഉപയോഗിച്ച് കാണിച്ചിരിക്കുന്നു, ഇതിന് `ListToolsRequestSchema` ഉപയോഗിക്കാം.

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
// ലഘുവാക്കലിനായി കോഡ് ഒഴിവാക്കി
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // രജിസ്റ്റർ ചെയ്ത ടൂളുകളുടെ പട്ടിക മടക്കുക
  return {
    tools: tools
  };
});
```

നൻവഴി ടൂളുകൾ ലിസ്റ്റിംഗ് എന്ന ഭാഗം തീർന്നു, ഇനി ടൂളുകൾ വിളിക്കുന്ന സന്ദർഭം കാണാം.

### -4- ടൂൾ വിളിക്കുന്നതിനുപരി

ടൂൾ വിളിക്കാനായി മറ്റു ഒരു അഭ്യർത്ഥന ഹാൻഡ്ലർ സജ്ജീകരിക്കണം, ഇത് ഏത് ഫീച്ചർ വിളിക്കണമെന്ന്, ഏത് ആർഗുമെന്റുകളോടുകൂടി എന്നെല്ലാം കൈകാര്യം ചെയ്യണം.

**Python**

`@server.call_tool` ഡികോറേറ്റർ ഉപയോഗിച്ച് `handle_call_tool` എന്നു ഫംഗ്ഷൻ നടപ്പാക്കാം. അതിൽ ടൂൾ നാമം, ആർഗുമെന്റുകൾ പാഴ്സുചെയ്യണം, അവ ശരിയായവയാണെന്ന് ഉറപ്പാക്കണം. ഇത് ഈ ഫംഗ്ഷനിൽ വെയ്ക്കാമോ, അല്ലെങ്കിൽ യഥാർത്ഥ ടൂളിൽ വെയ്ക്കാമോ.

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
        # ടൂൾ അഭിമുഖീകരിക്കുക
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

ഇവ നടക്കുന്നത് ഇങ്ങനെ:

- ടൂൾ നാമം `name` എന്ന ഇൻപുട്ട് പാരാമീറ്ററിൽ ഇതിനകം ഉണ്ടെന്നാണ്.

- ടൂൾ വിളിക്കപ്പെടുന്നത് `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` വഴി ആണ്. പാരാമീറ്ററുകളുടെ സ്ഥിരീകരണം ഹാൻഡ്ലർ ഫംഗ്ഷനിലാണ് നടക്കുന്നത്, പരാജയം ഉണ്ടെങ്കിൽ ഒഴിവാക്കൽ.Throw ചെയ്യും.

ഇങ്ങനെ, ലോ ലെവൽ സെർവർ ഉപയോഗിച്ച് ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുകയും വിളിക്കയും ചെയ്യുന്നത് പൂർണ്ണമായി മനസ്സിലായി.

[സമ്പൂർണ്ണ ഉദാഹരണം](./code/README.md) ഇവിടെയാണ് കാണുക

## അസൈൻമെന്റ്സ്

നിങ്ങൾ ലഭിച്ച കോഡ് വിപുലീകരിച്ച് കൂടുതൽ ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾ ചേർക്കുക, tools ഡയറക്ടറിയിൽ മാത്രമാണ് ഫയലുകൾ ചേർക്കേണ്ടത് എന്നതിനെ കുറിച്ച് നിരൂപിക്കുക.

*വിഭവം നൽകിയിട്ടില്ല*

## സംക്ഷേപം

ഈ അദ്ധ്യായത്തിൽ, ലോ ലെവൽ സെർവർ സമീപനം എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്നതും, അത് ഉപയോഗിച്ച് നന്നായി ഒരു ആർക്കിടെക്ചർ നിർമ്മിക്കാനുള്ള സഹായവും, സ്ഥിരീകരണവും ചർച്ച ചെയ്തു. ഇൻപുട്ട് സ്ഥിരീകരണത്തിനായി ഉപയോഗിക്കുന്ന ലൈബ്രറികൾ ഉപയോഗിച്ച് സ്കീമ നിർമ്മിക്കുന്ന രീതി കാണിച്ചു.

## അടുത്തതായി എന്ത്

- അടുത്തത്: [സിംപിൾ ഓതന്റിക്കേഷൻ](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
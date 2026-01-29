# Advanced server usage

May dalawang uri ng server na ipinapakita sa MCP SDK: ang normal na server at ang low-level server. Karaniwan, ginagamit mo ang regular na server upang magdagdag ng mga tampok dito. Gayunpaman, sa ilang mga kaso, mas mainam na umasa sa low-level server tulad ng:

- Mas maayos na arkitektura. Posibleng lumikha ng malinis na arkitektura gamit ang parehong regular na server at low-level server, ngunit maaaring mas madali ito sa low-level server.
- Availability ng mga tampok. Ang ilang mga advanced na tampok ay magagamit lamang sa low-level server. Makikita mo ito sa mga susunod na kabanata habang nagdadagdag tayo ng sampling at elicitation.

## Regular server vs low-level server

Ganito ang hitsura ng paglikha ng MCP Server gamit ang regular na server:

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

Ang punto dito ay malinaw mong idinadagdag ang bawat tool, resource, o prompt na nais mong magkaroon ang server. Walang masama dito.

### Low-level server approach

Gayunpaman, kapag ginamit mo ang low-level server approach, kailangan mong mag-isip nang iba. Sa halip na irehistro ang bawat tool, gagawa ka ng dalawang handler para sa bawat uri ng tampok (tools, resources, o prompts). Halimbawa, para sa tools, mayroon lamang dalawang function tulad nito:

- Paglista ng lahat ng tools. Isang function ang responsable para sa lahat ng pagtatangka na maglista ng tools.
- Pag-handle ng pagtawag sa lahat ng tools. Dito rin, mayroon lamang isang function na humahawak sa mga tawag sa isang tool.

Mukhang mas kaunting trabaho, di ba? Sa halip na irehistro ang isang tool, kailangan ko lang tiyakin na ang tool ay nakalista kapag naglista ako ng lahat ng tools at tinatawag ito kapag may papasok na request upang tawagin ang tool.

Tingnan natin kung paano ngayon ang hitsura ng code:

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

Dito, mayroon na tayong function na nagbabalik ng listahan ng mga tampok. Ang bawat entry sa tools list ay may mga field tulad ng `name`, `description`, at `inputSchema` upang sumunod sa return type. Pinapayagan tayo nitong ilagay ang ating mga tool at feature definition sa ibang lugar. Maaari na nating likhain ang lahat ng ating tools sa isang tools folder, at ganoon din para sa lahat ng iyong mga tampok, kaya ang iyong proyekto ay maaaring maayos na nakaayos tulad nito:

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

Maganda, ang ating arkitektura ay maaaring gawing malinis.

Paano naman ang pagtawag sa tools, pareho ba ang ideya, isang handler para tumawag sa isang tool, alinman sa tool? Oo, eksakto, narito ang code para doon:

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

Tulad ng nakikita mo sa code sa itaas, kailangan nating i-parse ang tool na tatawagin, at kung anong mga argumento ang gagamitin, at pagkatapos ay magpatuloy sa pagtawag sa tool.

## Pagpapabuti ng approach gamit ang validation

Sa ngayon, nakita mo kung paano ang lahat ng iyong mga rehistrasyon upang magdagdag ng tools, resources, at prompts ay maaaring mapalitan ng dalawang handler bawat uri ng tampok. Ano pa ang kailangan nating gawin? Dapat tayong magdagdag ng isang uri ng validation upang matiyak na ang tool ay tinatawag gamit ang tamang mga argumento. Ang bawat runtime ay may sariling solusyon para dito, halimbawa, ang Python ay gumagamit ng Pydantic at ang TypeScript ay gumagamit ng Zod. Ang ideya ay gawin ang mga sumusunod:

- Ilipat ang lohika para sa paglikha ng isang tampok (tool, resource, o prompt) sa dedikadong folder nito.
- Magdagdag ng paraan upang i-validate ang papasok na request na humihiling, halimbawa, tumawag sa isang tool.

### Gumawa ng isang tampok

Upang lumikha ng isang tampok, kailangan nating gumawa ng file para sa tampok na iyon at tiyakin na mayroon itong mga mandatoryong field na kinakailangan ng tampok na iyon. Ang mga field ay bahagyang nagkakaiba sa pagitan ng tools, resources, at prompts.

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

Dito makikita mo kung paano natin ginagawa ang mga sumusunod:

- Gumawa ng schema gamit ang Pydantic `AddInputModel` na may mga field na `a` at `b` sa file *schema.py*.
- Subukang i-parse ang papasok na request upang maging uri ng `AddInputModel`, kung may hindi pagkakatugma sa mga parameter, ito ay magka-crash:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Maaari mong piliin kung ilalagay ang parsing logic na ito sa mismong tool call o sa handler function.

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

- Sa handler na humahawak sa lahat ng tool calls, sinusubukan nating i-parse ang papasok na request sa schema na tinukoy ng tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kung gumagana iyon, magpapatuloy tayo sa pagtawag sa aktwal na tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Tulad ng nakikita mo, ang approach na ito ay lumilikha ng mahusay na arkitektura dahil ang lahat ay may lugar, ang *server.ts* ay isang napakaliit na file na nag-wire up lamang ng mga request handler, at ang bawat tampok ay nasa kani-kanilang folder, i.e., tools/, resources/, o /prompts.

Magaling, subukan nating buuin ito sa susunod.

## Exercise: Paglikha ng low-level server

Sa exercise na ito, gagawin natin ang mga sumusunod:

1. Gumawa ng low-level server na humahawak sa paglista ng tools at pagtawag sa tools.
1. Magpatupad ng arkitektura na maaari mong pagbuuin.
1. Magdagdag ng validation upang matiyak na ang iyong tool calls ay maayos na na-validate.

### -1- Gumawa ng arkitektura

Ang unang bagay na kailangan nating tugunan ay ang arkitektura na tumutulong sa atin na mag-scale habang nagdadagdag tayo ng mas maraming tampok. Ganito ang hitsura nito:

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

Ngayon, mayroon na tayong setup ng arkitektura na tinitiyak na madali tayong makakapagdagdag ng mga bagong tool sa isang tools folder. Malaya kang sundin ito upang magdagdag ng mga subdirectory para sa resources at prompts.

### -2- Gumawa ng tool

Tingnan natin kung paano ang paggawa ng tool. Una, kailangang likhain ito sa subdirectory ng *tool* tulad nito:

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

Makikita natin dito kung paano natin tinutukoy ang name, description, isang input schema gamit ang Pydantic, at isang handler na tatawagin kapag ang tool na ito ay tinawag. Sa huli, inilalantad natin ang `tool_add` na isang dictionary na naglalaman ng lahat ng mga property na ito.

Mayroon ding *schema.py* na ginagamit upang tukuyin ang input schema na ginagamit ng ating tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kailangan din nating punan ang *__init__.py* upang matiyak na ang tools directory ay itinuturing bilang isang module. Bukod pa rito, kailangan nating ilantad ang mga module sa loob nito tulad nito:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Maaari tayong magpatuloy sa pagdaragdag sa file na ito habang nagdadagdag tayo ng mas maraming tools.

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

Dito, gumagawa tayo ng dictionary na binubuo ng mga property:

- name, ito ang pangalan ng tool.
- rawSchema, ito ang Zod schema, gagamitin ito upang i-validate ang papasok na request upang tawagin ang tool na ito.
- inputSchema, ang schema na ito ay gagamitin ng handler.
- callback, ginagamit ito upang tawagin ang tool.

Mayroon ding `Tool` na ginagamit upang i-convert ang dictionary na ito sa isang uri na maaaring tanggapin ng mcp server handler, at ganito ang hitsura nito:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

At mayroon ding *schema.ts* kung saan iniimbak natin ang input schemas para sa bawat tool na ganito ang hitsura na may isang schema lamang sa kasalukuyan, ngunit habang nagdadagdag tayo ng tools, maaari tayong magdagdag ng mas maraming entry:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Magaling, magpatuloy tayo sa pag-handle ng paglista ng ating mga tools.

### -3- Handle tool listing

Susunod, upang i-handle ang paglista ng ating mga tools, kailangan nating mag-set up ng request handler para dito. Narito ang kailangan nating idagdag sa ating server file:

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

Dito, idinagdag natin ang decorator na `@server.list_tools` at ang implementing function na `handle_list_tools`. Sa huli, kailangan nating gumawa ng listahan ng tools. Pansinin kung paano ang bawat tool ay kailangang magkaroon ng name, description, at inputSchema.

**TypeScript**

Upang mag-set up ng request handler para sa paglista ng tools, kailangan nating tawagin ang `setRequestHandler` sa server gamit ang schema na angkop sa ating ginagawa, sa kasong ito `ListToolsRequestSchema`.

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

Magaling, ngayon nasolusyonan na natin ang bahagi ng paglista ng tools, tingnan natin kung paano natin tatawagin ang tools sa susunod.

### -4- Handle calling a tool

Upang tumawag sa isang tool, kailangan nating mag-set up ng isa pang request handler, sa pagkakataong ito nakatuon sa pag-handle ng request na tumutukoy kung aling tampok ang tatawagin at kung anong mga argumento ang gagamitin.

**Python**

Gamitin natin ang decorator na `@server.call_tool` at ipatupad ito gamit ang isang function tulad ng `handle_call_tool`. Sa loob ng function na iyon, kailangan nating i-parse ang pangalan ng tool, ang mga argumento nito, at tiyakin na ang mga argumento ay wasto para sa tool na pinag-uusapan. Maaari nating i-validate ang mga argumento sa function na ito o sa downstream sa aktwal na tool.

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

Narito ang nangyayari:

- Ang pangalan ng ating tool ay naroroon na bilang input parameter na `name`, na totoo rin para sa ating mga argumento sa anyo ng `arguments` dictionary.

- Ang tool ay tinatawag gamit ang `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Ang validation ng mga argumento ay nangyayari sa `handler` property na tumutukoy sa isang function, kung nabigo iyon, magtataas ito ng exception.

Diyan, mayroon na tayong buong pag-unawa sa paglista at pagtawag sa tools gamit ang low-level server.

Tingnan ang [buong halimbawa](./code/README.md) dito.

## Assignment

Palawakin ang code na ibinigay sa iyo gamit ang ilang tools, resources, at prompt, at pag-isipan kung paano mo napapansin na kailangan mo lamang magdagdag ng mga file sa tools directory at wala nang iba.

*Walang solusyon na ibinigay*

## Summary

Sa kabanatang ito, nakita natin kung paano gumagana ang low-level server approach at kung paano ito makakatulong sa atin na lumikha ng maayos na arkitektura na maaari nating patuloy na pagbuuin. Tinalakay din natin ang validation, at ipinakita sa iyo kung paano gumamit ng validation libraries upang lumikha ng schemas para sa input validation.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
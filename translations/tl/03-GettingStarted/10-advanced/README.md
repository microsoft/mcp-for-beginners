# Advanced na paggamit ng server

Mayroong dalawang magkaibang uri ng mga server na ipinapakita sa MCP SDK, ang iyong normal na server at ang low-level na server. Karaniwan, gagamitin mo ang regular na server upang magdagdag ng mga tampok dito. Ngunit sa ilang mga kaso, nais mong umasa sa low-level na server tulad ng:

- Mas magandang arkitektura. Posibleng gumawa ng malinis na arkitektura gamit parehong regular na server at low-level na server ngunit maaaring masasabing mas madali ito sa low-level na server.
- Availability ng mga tampok. Ang ilang mga advanced na tampok ay maaari lamang magamit gamit ang
    low-level na server. Tatalakayin sa mga susunod na kabanata ang Elicitation at ang legacy Sampling
    na tampok, na hindi na ginagamit sa MCP `2026-07-28`.

## Regular na server kumpara sa low-level na server

Ganito ang itsura ng paglikha ng isang MCP Server gamit ang regular na server

**Python**

```python
mcp = FastMCP("Demo")

# Magdagdag ng kasangkapan para sa karagdagan
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

// Magdagdag ng kasangkapang pantambal
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

Ang punto ay sadyang ina-ad ang bawat tool, resource o prompt na gusto mong magkaroon ang server. Wala namang mali doon.  

### Diskarte ng low-level na server

Gayunman, kapag ginamit mo ang diskarte ng low-level na server kailangan mong pag-isipan ito nang iba. Sa halip na irehistro ang bawat tool, gagawa ka ng dalawang handler bawat uri ng tampok (mga tool, resources o prompts). Kaya halimbawa ang mga tool ay may dalawang function lang tulad nito:

- Pag-lista ng lahat ng mga tool. Isang function ang responsable sa lahat ng pagtatangkang maglista ng mga tool.
- Paghawak ng pagtawag sa lahat ng mga tool. Dito rin, isang function lang ang humahawak sa mga pagtawag sa isang tool

Mukhang mas konti ang trabaho di ba? Kaya sa halip na irehistro ang isang tool, kailangan ko lang siguraduhin na nakalista ang tool kapag nililista ko ang lahat ng mga tool at tinatawag ito kapag may dumating na kahilingan na tawagan ang tool. 

Tingnan natin kung ano na ang itsura ng code ngayon:

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
  // Ibalik ang listahan ng mga rehistradong kasangkapan
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

Dito ay mayroon tayong function na nagbabalik ng listahan ng mga tampok. Bawat entry sa listahan ng tools ay may mga field tulad ng `name`, `description` at `inputSchema` upang sumunod sa return type. Pinapayagan tayo nitong ilagay ang ating mga tools at depinisyon ng tampok sa iba pang lugar. Maaari na nating gawin lahat ng ating tools sa isang tools folder at ganoon din para sa lahat ng iyong mga tampok kaya biglang magiging maayos ang iyong proyekto tulad nito:

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

Ayos na ayos, maaaring gawing malinis ang ating arkitektura.

Paano naman ang pagtawag ng mga tool, pareho lang ba ang ideya, isang handler para tawagin ang isang tool, alinmang tool? Oo, eksakto, ito ang code para doon:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # ang tools ay isang diksyunaryo na may mga pangalan ng tools bilang mga susi
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
    // TODO tawagan ang tool,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Makikita mo sa nasa itaas na code na kailangan nating i-parse ang tool na tatawagin, at kung ano ang mga argumento, at pagkatapos ay kailangan nating ituloy ang pagtawag sa tool.

## Pagpapabuti ng diskarte gamit ang validation

Sa ngayon, nakita mo kung paano pinalitan ng dalawang handler bawat uri ng tampok ang lahat ng iyong mga rehistrasyon para magdagdag ng tools, resources at prompts. Ano pa ang kailangan nating gawin? Dapat tayong magdagdag ng ilang uri ng validation upang matiyak na tinatawag ang tool gamit ang tamang mga argumento. May sarili-sariling solusyon ang bawat runtime para dito, halimbawa ang Python ay gumagamit ng Pydantic at ang TypeScript ay gumagamit ng Zod. Ang ideya ay gawin ang mga sumusunod:

- Ilipat ang lohika para gumawa ng isang tampok (tool, resource o prompt) sa dedikadong folder nito.
- Magdagdag ng paraan para ma-validate ang isang papasok na request na humihiling halimbawa ng pagtawag sa isang tool.

### Gumawa ng isang tampok

Para gumawa ng isang tampok, kailangang gumawa ng isang file para sa tampok na iyon at siguraduhing mayroon itong mga mandatory na field na kinakailangan ng tampok na iyon. Ang mga field ay bahagyang nagkakaiba sa pagitan ng mga tool, resources at prompts.

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
        # I-validate ang input gamit ang Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: idagdag ang Pydantic, para makagawa tayo ng AddInputModel at ma-validate ang mga args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

dito makikita kung paano natin ginagawa ang mga sumusunod:

- Gumawa ng isang schema gamit ang Pydantic `AddInputModel` na may mga field na `a` at `b` sa file na *schema.py*.
- Subukang i-parse ang papasok na request upang maging uri na `AddInputModel`, kung may mismatch sa mga parametro, magka-crash ito:

   ```python
   # add.py
    try:
        # Suriin ang input gamit ang Pydantic na modelo
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Maaari mong piliin kung ilalagay ang lohika ng parsing na ito sa mismong pagtawag ng tool o sa handler function.

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

- Sa handler na humahawak sa lahat ng tawag sa tool, sinusubukan nating i-parse ang papasok na request sa schema na itinakda ng tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kung magtagumpay ito saka natin itutuloy ang pagtawag sa mismong tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Makikita mo na ang diskarteng ito ay lumilikha ng magandang arkitektura dahil lahat ay may kanya-kanyang lugar, ang *server.ts* ay isang napakaliit na file na nag-uugnay lang ng mga request handlers at bawat tampok ay nasa kani-kanilang folder gaya ng tools/, resources/ o /prompts.

Ayos, subukan nating buuin ito sunod. 

## Ehersisyo: Paglikha ng low-level na server

Sa ehersisyong ito, gagawin natin ang mga sumusunod:

1. Gumawa ng low-level na server na humahawak sa paglista ng mga tool at pagtawag ng mga tool.
1. Ipatupad ang isang arkitektura na maaari mong dagdagan pa.
1. Magdagdag ng validation upang matiyak na ang iyong mga tawag sa tool ay tama ang pag-validate.

### -1- Gumawa ng isang arkitektura

Ang unang bagay na kailangan nating pagtuunan ay ang isang arkitektura na tumutulong sa ating mag-scale habang dadami ang mga tampok na idaragdag natin, ganito ang hitsura nito:

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

Ngayon ay nakasetup na tayo ng arkitektura na nagsisigurong madali tayong makakagdagdag ng bagong mga tool sa isang tools folder. Malaya kang sundan ito upang magdagdag ng mga subdirectory para sa mga resources at prompts.

### -2- Paglikha ng isang tool

Tingnan natin kung paano ang paggawa ng isang tool. Una, kailangan itong malikha sa *tool* subdirectory nito gaya nito:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # I-validate ang input gamit ang Pydantic na modelo
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: magdagdag ng Pydantic, para makagawa tayo ng AddInputModel at ma-validate ang mga args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Nakikita natin dito kung paano natin idinedefine ang pangalan, deskripsyon, at input schema gamit ang Pydantic at isang handler na tatawagin kapag tumawag ang tool na ito. Panghuli, inilalantad natin ang `tool_add` na isang diksyunaryo na may lahat ng mga property na ito.

Meron ding *schema.py* na ginagamit para idefine ang input schema na ginagamit ng ating tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kailangan din nating punan ang *__init__.py* upang matiyak na ang tools directory ay itinuturing bilang isang module. Bukod dito, kailangan nating ilantad ang mga module sa loob nito tulad nito:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Maaari nating patuloy na dagdagan ang file na ito habang nadaragdagan ang mga tool.

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

Dito gumawa tayo ng isang diksyunaryo na binubuo ng mga properties:

- name, ito ang pangalan ng tool.
- rawSchema, ito ang Zod schema, gagamitin ito para i-validate ang mga papasok na request na tumatawag sa tool na ito.
- inputSchema, gagamitin ng handler ang schema na ito.
- callback, ito ay ginagamit para tawagin ang tool.

Mayroon ding `Tool` na ginagamit para i-convert ang diksyunaryo na ito sa isang type na matatanggap ng mcp server handler at ganito ang itsura:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

At meron ding *schema.ts* kung saan natin iniimbak ang mga input schema para sa bawat tool na ganito ang itsura, sa ngayon ay may isang schema lang pero habang nadadagdagan ang mga tools, maaari tayong magdagdag ng mas maraming entries:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Ayos, magpatuloy tayo sa paghawak ng paglist ng ating mga tool.

### -3- Hawakan ang paglist ng tool

Susunod, upang hawakan ang paglist ng mga tool, kailangan nating mag-setup ng request handler para dito. Ganito ang kailangang idagdag sa ating server file:

**Python**

```python
# inalis ang code para sa kasimplehan
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

Dito, idinadagdag natin ang decorator na `@server.list_tools` at ang function na nagpapatupad nito na `handle_list_tools`. Sa function na ito, kailangan nating gumawa ng isang listahan ng mga tool. Pansinin na bawat tool ay kailangang magkaroon ng pangalan, deskripsyon at inputSchema.   

**TypeScript**

Para mag-setup ng request handler para sa paglist ng tool, kailangan nating tawagin ang `setRequestHandler` sa server na may schema na akma sa ginagawa natin, sa kasong ito `ListToolsRequestSchema`. 

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
// code na inalis para sa ikinababawas ng haba
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Ibalik ang listahan ng nakarehistrong mga tool
  return {
    tools: tools
  };
});
```

Ayos, ngayon ay naresolba na natin ang bahaging paglist ng mga tool, tingnan naman natin kung paano natin tatawagin ang mga tool.

### -4- Hawakan ang pagtawag ng isang tool

Para tawagan ang isang tool, kailangan nating mag-setup ng isa pang request handler, na nakatuon sa paghawak ng request na tumutukoy kung aling tampok ang tatawagin at kung ano ang mga argumento.

**Python**

Gamitin natin ang decorator na `@server.call_tool` at ipatupad ito ng isang function tulad ng `handle_call_tool`. Sa function na ito, kailangan nating i-parse ang pangalan ng tool, ang mga argumento nito at tiyakin na tama ang mga argumento para sa tool na iyon. Maaaring i-validate natin ang mga argumento dito o sa mismong tool.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # ang tools ay isang diksyunaryo na may mga pangalan ng tool bilang mga susi
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # tawagin ang tool
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ganito ang nangyayari:

- Ang pangalan ng tool ay nasa input parameter na `name` na tumutugma rin para sa mga argumento sa anyo ng `arguments` dictionary.

- Ang tool ay tinatawag gamit ang `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Ang validation ng mga argumento ay nangyayari sa `handler` property na tumutukoy sa isang function, kung mabigo ito magta-throw ng exception.

Ayan, ngayon ay may buong pagkakaintindi na tayo sa paglist at pagtawag ng mga tool gamit ang low-level na server.

Tingnan ang [buong halimbawa](./code/README.md) dito

## Takdang Aralin

Palawakin ang code na ibinigay sa iyo ng ilang mga tool, resources at prompt at pag-isipan kung paano mo mapapansin na kailangan mo lang magdagdag ng mga file sa tools directory at wala nang ibang lugar. 

*Walang ibinigay na solusyon*

## Buod

Sa kabanatang ito, nakita natin kung paano gumagana ang diskarte ng low-level na server at paano nito matutulungan tayong lumikha ng maayos na arkitektura na maaari nating ipagpatuloy na buuin. Tinalakay din natin ang validation at ipinakita kung paano gumamit ng mga validation library upang gumawa ng mga schema para sa input validation.

## Ano ang Susunod

- Susunod: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
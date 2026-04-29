# Advanced na paggamit ng server

Mayroong dalawang uri ng server na ipinapakita sa MCP SDK, ang iyong normal na server at ang low-level na server. Karaniwan, gagamitin mo ang regular na server upang magdagdag ng mga tampok dito. Sa ilang mga kaso, gusto mong umasa sa low-level na server tulad ng:

- Mas mabuting arkitektura. Posible na gumawa ng malinis na arkitektura gamit ang parehong regular na server at isang low-level na server ngunit maaaring masabi na mas madali ito sa low-level na server.
- Availability ng tampok. Ang ilang mga advanced na tampok ay maaari lamang gamitin sa isang low-level na server. Makikita mo ito sa mga susunod na kabanata habang nagdadagdag tayo ng sampling at elicitation.

## Regular na server vs low-level na server

Ganito ang hitsura ng paglikha ng isang MCP Server gamit ang regular na server

**Python**

```python
mcp = FastMCP("Demo")

# Magdagdag ng kasangkapang pangdagdag
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

// Magdagdag ng isang karagdagang kasangkapan
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

Ang punto dito ay nagdadagdag ka nang tahasan ng bawat tool, resource o prompt na gusto mong mayroon ang server. Wala namang mali doon.

### Paraan ng low-level na server

Gayunpaman, kapag ginamit mo ang low-level na server na paraan, kailangan mong mag-isip nang iba. Sa halip na irehistro ang bawat tool, lumikha ka ng dalawang handler bawat uri ng tampok (tools, resources o prompts). Halimbawa, ang mga tools ay may dalawang function lamang tulad nito:

- Paglilista ng lahat ng tools. Isang function ang magiging responsable para sa lahat ng pagtatangka na ilista ang mga tools.
- Pag-handle ng pagtawag sa lahat ng tools. Dito rin, isa lang ang function na humahandle ng pagtawag sa isang tool.

Parang mas konti ang trabaho di ba? Kaya imbes na irehistro ang isang tool, siguraduhin ko lang na nakalista ang tool kapag nililista ko ang lahat ng tools at tinatawag ito kapag may papasok na request para tawagan ang tool.

Tingnan natin kung paano ngayon ang itsura ng code:

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

Dito ay meron na tayong function na nagbabalik ng listahan ng mga tampok. Bawat entry sa listahan ng tools ay may mga field tulad ng `name`, `description` at `inputSchema` upang sumunod sa return type. Pinapayagan tayo nitong ilagay ang ating mga tools at definisyon ng tampok sa ibang lugar. Maaari na nating likhain ang lahat ng mga tool sa isang tools folder at pareho rin para sa lahat ng features kaya ang iyong proyekto ay maaaring maging organisado nang ganito:

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

Maganda ito, ang ating arkitektura ay maaaring gawing malinis.

Paano naman ang pagtawag sa mga tools, pareho lang ba ang ideya, isang handler lang para tawagan ang isang tool, kahit anong tool? Oo, tama, ganito ang code para doon:

**Python**

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
    
    // args: mga argumento ng request.params
    // TODO tawagan ang tool,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Makikita mo sa code sa itaas, kailangan nating i-parse kung aling tool ang tatawagin, at kung ano ang mga arguments, saka tayo tatawag ng tool.

## Pagpapahusay ng paraan gamit ang validation

Hanggang ngayon, nakita mo kung paano ang lahat ng iyong mga rehistrasyon para magdagdag ng tools, resources at prompts ay maaaring palitan ng dalawang handlers bawat uri ng tampok. Ano pa ang kailangan nating gawin? Dapat tayong magdagdag ng validation para masigurong ang tool ay tatawagin gamit ang tamang mga argumento. Bawat runtime ay may sarili nitong solusyon para dito, halimbawa ginagamit ng Python ang Pydantic at TypeScript ang Zod. Ang ideya ay ganito:

- Ilipat ang lohika sa paglikha ng isang tampok (tool, resource o prompt) sa dedikadong folder nito.
- Magdagdag ng paraan upang i-validate ang papasok na request na humihiling halimbawa na tawagan ang isang tool.

### Gumawa ng tampok

Para gumawa ng tampok, kailangan nating gumawa ng file para sa tampok na iyon at siguraduhing mayroon ito ng mga mandatory na fields na kailangan ng tampok na iyon. Ang mga field ay bahagyang nagkakaiba sa mga tools, resources at prompts.

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
        # Patunayan ang input gamit ang Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: idagdag ang Pydantic, upang makagawa tayo ng AddInputModel at mapatunayan ang mga argumento

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

- Gumawa ng schema gamit ang Pydantic `AddInputModel` na may mga field na `a` at `b` sa file na *schema.py*.
- Subukan i-parse ang papasok na request bilang uri ng `AddInputModel`, kung may mismatch sa mga parameters dito ay magka-crash:

   ```python
   # add.py
    try:
        # I-validate ang input gamit ang Pydantic na modelo
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Maaari mong piliin kung ilalagay mo ang parsing logic sa tool call mismo o sa handler function.

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

- Sa handler na humahawak sa lahat ng tool calls, sinusubukan na nating i-parse ang papasok na request sa schema na itinakda ng tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kung gumana ito, saka tayo tatawag sa aktwal na tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Makikita mo na ang pamamaraang ito ay lumilikha ng magandang arkitektura dahil lahat ay may tamang lugar, ang *server.ts* ay isang napakaliit na file na nagwiring lang ng mga request handlers at bawat tampok ay nasa kani-kanilang folder tulad ng tools/, resources/ o prompts/.

Maganda, subukan nating buuin ito ngayon.

## Ehersisyo: Paglikha ng low-level na server

Sa ehersisyong ito, gagawin natin ang mga sumusunod:

1. Gumawa ng low-level na server na humahandle ng pag-lista ng tools at pagtawag sa tools.
1. Mag-implementa ng arkitektura na maaari mong pagbasehan.
1. Magdagdag ng validation para masigurong tama ang mga pagtawag sa tool.

### -1- Gumawa ng arkitektura

Ang unang dapat nating ayusin ay arkitektura na tutulong sa pag-scale habang nagdadagdag tayo ng mas maraming tampok, ganito ang itsura nito:

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

Ngayon ay naayos na natin ang arkitektura na nagbibigay-daan para madali tayong makapagdagdag ng mga bagong tools sa isang tools folder. Malaya kang sumunod dito para magdagdag ng mga subdirectories para sa resources at prompts.

### -2- Paglikha ng tool

Tingnan natin kung paano ang paggawa ng tool. Una, kailangang likhain ito sa ilalim ng *tool* subdirectory ganito:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Suriin ang input gamit ang modelo ng Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: magdagdag ng Pydantic, upang makagawa tayo ng AddInputModel at masuri ang args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Makikita dito kung paano natin dinefine ang pangalan, deskripsyon, at input schema gamit ang Pydantic at isang handler na tatawagin kapag tinawag ang tool na ito. Sa huli, inilalabas natin ang `tool_add` na isang diksyunaryo na naglalaman ng mga properties na ito.

Mayroon ding *schema.py* na ginagamit para idefine ang input schema na ginagamit ng ating tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kailangan din nating lagyan ng laman ang *__init__.py* para siguraduhing ang tools directory ay tinatrato bilang isang module. Dagdag pa, kailangang ilabas ang mga modules sa loob nito ganito:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Maaari tayong magdagdag pa dito habang nadadagdagan ang mga tools.

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

Dito tayo ay gumagawa ng diksyunaryo na naglalaman ng mga properties:

- name, ito ang pangalan ng tool.
- rawSchema, ito ang Zod schema, gagamitin ito upang i-validate ang mga papasok na request para tawagin ang tool.
- inputSchema, gagamitin ng handler ang schema na ito.
- callback, ito ang ginagamit para tawagin ang tool.

Mayroon ding `Tool` na ginagamit para gawing type ang diksyunaryong ito na matatanggap ng mcp server handler, ganito ang itsura:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

At may *schema.ts* kung saan natin inilalagay ang mga input schemas para sa bawat tool na ganito ang itsura na isa pang schema lang sa ngayon pero habang nadadagdagan ang mga tools pwede kayong magdagdag ng mas maraming entry:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Maganda, magpatuloy tayo sa paghandle ng pag-lista ng mga tools.

### -3- Pag-handle ng pag-lista ng tools

Sunod, para sa paghandle ng paglist ng mga tools, kailangan nating gumawa ng request handler para dito. Ito ang kailangang idagdag sa server file:

**Python**

```python
# inalis ang code para sa ikinabibining
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

Dito, idinadagdag natin ang decorator na `@server.list_tools` at ang function na `handle_list_tools` na nagpapatupad nito. Sa huli, kailangang makagawa tayo ng listahan ng tools. Pansinin kung paano kailangang mayroon ang bawat tool ng name, description at inputSchema.

**TypeScript**

Para ma-set up ang request handler para sa pag-lista ng tools, kailangan nating tawagan ang `setRequestHandler` sa server na may schema na akma sa layunin, sa kasong ito `ListToolsRequestSchema`.

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
// code na tinanggal para sa pagpapaikli
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Ibalik ang listahan ng mga nakarehistrong kagamitan
  return {
    tools: tools
  };
});
```

Maganda, nasolusyonan na natin ang bahagi ng pag-lista ng tools, tignan natin kung paano tayo maaaring tumawag sa tools.

### -4- Pag-handle ng pagtawag sa tool

Para tawagan ang tool, kailangan natin gumawa ng isa pang request handler, sa pagkakataong ito ay nakatutok sa pagtanggap ng request na nagsasaad kung anong tampok ang tatawagin at ano ang mga argumento.

**Python**

Gamitin natin ang decorator na `@server.call_tool` at ipatupad ito gamit ang function na tulad ng `handle_call_tool`. Sa loob ng function na iyon, kailangang i-parse natin ang pangalan ng tool, ang argument nito at siguraduhing tama ang mga argumento para sa tool na iyon. Pwede nating i-validate ang mga argumento dito o sa mismong tool.

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

Ganito nangyayari:

- Ang pangalan ng tool ay nandito na bilang input parameter na `name` at totoo rin ito para sa mga argumento sa anyo ng diksyunaryong `arguments`.

- Tinatawag ang tool gamit ang `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Ang validation ng mga argumento ay nangyayari sa `handler` property na tumutukoy sa isang function, kapag nabigo ito ay magtataas ng exception.

Ayan, ngayon ay may buong pag-unawa na tayo sa pag-lista at pagtawag sa mga tools gamit ang low-level na server.

Tingnan ang [buong halimbawa](./code/README.md) dito

## Assignment

Palawakin ang code na ibinigay sa iyo gamit ang ilang tools, resources at prompt at pagnilayan kung paano mo mapapansin na kailangan mo lang magdagdag ng mga file sa tools directory at wala nang ibang bahagi.

*Walang ibinigay na solusyon*

## Buod

Sa kabanatang ito, nakita natin kung paano gumagana ang low-level na server na paraan at paano ito makakatulong sa paglikha ng magandang arkitektura na maaari nating ipagpatuloy na buuin. Tinalakay din natin ang validation at ipinakita kung paano gamitin ang mga validation libraries upang gumawa ng mga schemas para sa input validation.

## Ano ang Susunod

- Susunod: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang aming pinagsisikapan ang katumpakan, mangyaring tandaan na maaaring may mga pagkakamali o hindi pagkakatugma ang mga awtomatikong salin. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na pangunahing sanggunian. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagutan sa anumang hindi pagkakaunawaan o maling interpretasyon na magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
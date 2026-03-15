# Advanced server usage

May dalawang magkakaibang uri ng server na ipinapakita sa MCP SDK, ang iyong normal na server at ang low-level server. Karaniwan, gagamitin mo ang regular na server para magdagdag ng mga feature dito. Sa ilang mga kaso, gusto mong umasa sa low-level server gaya ng:

- Mas magandang arkitektura. Posibleng gumawa ng malinis na arkitektura gamit ang parehong regular na server at low-level server pero maaaring sabihin na mas madali ito sa low-level server.
- Availability ng feature. Ang ilang advanced na feature ay maaari lamang gamitin sa low-level server. Makikita mo ito sa mga susunod na kabanata habang nagdadagdag tayo ng sampling at elicitation.

## Regular server vs low-level server

Ganito ang hitsura ng paglikha ng isang MCP Server gamit ang regular na server

**Python**

```python
mcp = FastMCP("Demo")

# Magdagdag ng isang kasangkapang pandagdag
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

// Magdagdag ng isang kasangkapang pantambal
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

Ang punto ay ikaw ay hayagang nagdaragdag ng bawat tool, resource o prompt na gusto mong magkaroon ang server. Walang masama doon.

### Low-level server approach

Gayunpaman, kapag ginamit mo ang low-level server na pamamaraan, kailangan mong mag-isip nang iba. Sa halip na magrehistro ng bawat tool, lumikha ka ng dalawang handler bawat uri ng feature (tools, resources o prompts). Halimbawa, ang tools ay may dalawang function lang tulad nito:

- Paglista ng lahat ng tools. Ang isang function ang magiging responsable sa lahat ng pagtatangka na maglista ng tools.
- Pamahalaan ang pagtawag ng lahat ng tools. Dito rin, iisang function lang ang humahawak ng pagtawag sa tool.

Mukhang mas kaunting trabaho, hindi ba? Sa halip na magrehistro ng tool, kailangan ko lang siguraduhin na naka-lista ang tool kapag nililista ko ang lahat ng tools at na tinatawag ito kapag may darating na request na tumawag ng tool.

Tingnan natin kung paano ang hitsura ng code ngayon:

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
  // Ibalik ang listahan ng mga nakarehistrong kasangkapan
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

Dito mayroon na tayong function na nagbabalik ng listahan ng mga feature. Bawat entry sa tools listahan ay may mga field tulad ng `name`, `description` at `inputSchema` para sumunod sa return type. Pinapahintulutan tayo nito na ilagay ang ating mga tool at feature na definisyon sa ibang lugar. Maaari na nating likhain lahat ng ating tools sa isang tools folder at ganoon din sa lahat ng mga feature kaya ang iyong proyekto ay biglang magiging organisado ng ganito:

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

Ang ganda, maaaring maging malinis ang ating arkitektura.

Paano naman ang pagtawag ng mga tools, pareho lang ba ang ideya, isang handler lang na tumawag sa isang tool, sinumang tool? Oo, tama iyan, narito ang code para doon:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # ang tools ay isang diksyonaryo na may mga pangalan ng kagamitan bilang mga susi
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
    // TODO tawagan ang kasangkapan,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Tulad ng nakikita mo mula sa code sa itaas, kailangan nating i-parse kung anong tool ang tatawagin, at kung ano ang mga argumento, at pagkatapos ay kailangan nating ipagpatuloy ang pagtawag sa tool.

## Pagpapabuti ng pamamaraan gamit ang validation

Sa ngayon, nakita mo kung paano ang lahat ng iyong mga rehistrasyon para magdagdag ng tools, resources at prompts ay maaaring mapalitan ng dalawang handler bawat uri ng feature. Ano pa ba ang kailangan nating gawin? Dapat tayong magdagdag ng ilang anyo ng validation upang matiyak na ang tool ay tinatawag na may tamang mga argumento. Bawat runtime ay may kanya-kanyang solusyon para dito, halimbawa ginagamit ng Python ang Pydantic at TypeScript ang Zod. Ang ideya ay gawin natin ang sumusunod:

- Ilipat ang lohika para sa paglikha ng feature (tool, resource o prompt) sa kanya-kanyang nakalaang folder.
- Magdagdag ng paraan upang ma-validate ang papasok na request na, halimbawa, tumawag ng tool.

### Lumikha ng isang feature

Para lumikha ng isang feature, kailangan nating gumawa ng file para sa feature na iyon at siguraduhin na mayroon itong mga mandatory na field na kailangan ng feature na iyon. Ang mga field ay bahagyang nagkakaiba sa pagitan ng tools, resources at prompts.

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
        # Beripikahin ang input gamit ang Pydantic na modelo
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: idagdag ang Pydantic, upang makagawa tayo ng AddInputModel at ma-validate ang mga args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Dito makikita mo kung paano natin ginagawa ang sumusunod:

- Gumawa ng schema gamit ang Pydantic `AddInputModel` na may mga field na `a` at `b` sa file na *schema.py*.
- Subukang i-parse ang papasok na request upang maging uri ng `AddInputModel`, kung may mismatch sa mga parameter ay matatalo ito:

   ```python
   # add.py
    try:
        # Patunayan ang input gamit ang Pydantic na modelo
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Maaari mong piliin kung ilalagay ang lohika ng parsing na ito sa mismong tool call o sa handler function.

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

- Sa handler na humahawak sa lahat ng pagtawag sa tool, sinusubukan nating i-parse ang papasok na request sa schema na idinefine ng tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kung gumana ito, magpapatuloy tayo sa pagtawag ng aktwal na tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Tulad ng nakikita mo, ang pamamaraang ito ay lumilikha ng magandang arkitektura dahil bawat bagay ay may sariling lugar, ang *server.ts* ay isang napakaliit na file na nag-uugnay lang sa mga request handlers at bawat feature ay nasa kani-kaniyang folder gaya ng tools/, resources/ o /prompts.

Maganda, subukan nating buuin ito ngayon.

## Exercise: Paglikha ng low-level server

Sa pagsasanay na ito, gagawin natin ang mga sumusunod:

1. Gumawa ng low-level server na humahawak sa paglista ng tools at pagtawag ng mga tools.
2. Magpatupad ng arkitektura na madaling mapalawig.
3. Magdagdag ng validation upang matiyak na wastong na-validate ang pagtawag sa tool.

### -1- Gumawa ng arkitektura

Ang unang bagay na kailangan nating tugunan ay isang arkitektura na tumutulong sa atin mag-scale habang nagdadagdag tayo ng mas maraming feature, ganito ang hitsura:

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

Ngayon ay na-set up na natin ang arkitektura na nagtitiyak na madali tayong makakapagdagdag ng mga bagong tools sa tools folder. Malayang sundan ito upang magdagdag ng mga subdirectory para sa resources at prompts.

### -2- Paglikha ng tool

Tingnan natin kung paano ang paggawa ng tool. Una, kailangang likhain ito sa kanyang *tool* na subdirectory tulad nito:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # I-validate ang input gamit ang Pydantic model
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

Makikita dito kung paano natin dinefine ang pangalan, deskripsyon, at input schema gamit ang Pydantic at isang handler na tatawagin kapag tinawag ang tool na ito. Sa huli, inilalabas natin ang `tool_add` na isang dictionary na naglalaman ng mga property na ito.

Meron ding *schema.py* na ginagamit upang idefine ang input schema na ginagamit ng ating tool:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Kailangan din nating lagyan ng laman ang *__init__.py* upang matiyak na ang tools directory ay itinuturing bilang isang module. Bukod doon, kailangan nating ilabas ang mga module na nasa loob nito ng ganito:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Maaari nating patuloy na dagdagan ang file na ito habang nadaragdagan ang ating mga tools.

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

Dito gumawa tayo ng dictionary na binubuo ng mga property:

- name, ito ang pangalan ng tool.
- rawSchema, ito ang Zod schema, gagamitin ito para i-validate ang mga papasok na request para tawagin ang tool.
- inputSchema, gagamitin ito ng handler.
- callback, ito ang ginagamit para tawagin ang tool.

Meron ding `Tool` na ginagamit para i-convert ang dictionary na ito sa isang type na matatanggap ng mcp server handler at ganito ang itsura:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

At may *schema.ts* kung saan inilalagay natin ang input schemas para sa bawat tool na ganito ang itsura at kasalukuyang may isang schema lamang pero habang nagdadagdag tayo ng tools maaari tayong magdagdag ng iba pang entry:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Maganda, magpapatuloy tayo sa paghawak ng paglista ng ating mga tool.

### -3- Hawakan ang paglista ng tool

Susunod, upang hawakan ang paglista ng ating mga tool, kailangan nating mag-set up ng request handler para dito. Ito ang kailangan nating idagdag sa ating server file:

**Python**

```python
# inalis ang code para sa pagpapaikli
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

Dito, idinagdag natin ang decorator na `@server.list_tools` at ang function na nag-iimplementa na `handle_list_tools`. Sa huli, kailangan nating gumawa ng listahan ng mga tools. Pansinin na bawat tool ay kailangang may pangalan, deskripsyon at inputSchema.

**TypeScript**

Para mag-set up ng request handler para sa paglista ng tools, kailangan nating tawagin ang `setRequestHandler` sa server gamit ang schema na akma sa gusto nating gawin, sa kasong ito ay `ListToolsRequestSchema`.

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
// code na nilaktawan para sa ikinababawas ng haba
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Ibalik ang listahan ng mga nakarehistrong kasangkapan
  return {
    tools: tools
  };
});
```

Maganda, ngayon ay nasolusyunan na natin ang bahagi ng paglista ng tools, tingnan natin kung paano naman tayo tatawag ng mga tools.

### -4- Hawakan ang pagtawag ng tool

Para tumawag ng tool, kailangan nating mag-set up ng isa pang request handler, ngayon ay nakatuon ito sa paghawak ng request na nagsasaad kung anong feature ang tatawagin at kung anong mga argumento.

**Python**

Gamitin natin ang decorator na `@server.call_tool` at ipatupad ito sa isang function na tulad ng `handle_call_tool`. Sa loob ng function na iyon, kailangan nating i-parse ang pangalan ng tool, ang mga argumento nito at tiyakin na valid ang mga argumento para sa tool na iyon. Maaari nating i-validate ang mga argumento dito o sa mismong tool.

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

Ito ang nangyayari:

- Ang pangalan ng tool ay nandiyan na bilang input parameter na `name` at ang mga argumento ay nasa anyo ng `arguments` dictionary.

- Ang tool ay tinatawag gamit ang `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Ang validation ng mga argumento ay nagaganap sa `handler` property na tumutukoy sa isang function, kung pumalya ito ay magpa-raise ng exception.

Ayan, mayroon na tayong buong pag-unawa sa paglista at pagtawag ng tools gamit ang low-level server.

Tingnan ang [buong halimbawa](./code/README.md) dito

## Assignment

Palawakin ang code na ibinigay sa iyo gamit ang ilang tools, resources at prompt at pagnilayan kung paano mo napapansin na kailangan mo lang magdagdag ng mga file sa tools directory at sa ibang parte wala nang kailangang idagdag.

*Walang ibinigay na solusyon*

## Buod

Sa kabanatang ito, nakita natin kung paano gumagana ang low-level server approach at kung paano nito matutulungan tayong makagawa ng magandang arkitektura na maaari nating dagdagan. Tinalakay din natin ang validation at ipinakita kung paano gamitin ang mga validation library upang gumawa ng mga schema para sa input validation.

## Anong Susunod

- Susunod: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kaming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring bilang pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang pagsasalin ng isang propesyonal na tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
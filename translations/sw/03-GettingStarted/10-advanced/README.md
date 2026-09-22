# Matumizi ya juu ya seva

Kuna aina mbili tofauti za seva zilizotolewa katika MCP SDK, seva yako ya kawaida na seva ya ngazi ya chini. Kawaida, ungetumia seva ya kawaida kuongeza vipengele kwake. Hata hivyo, katika baadhi ya kesi, unataka kutegemea seva ya ngazi ya chini kama vile:

- Miundo bora. Inawezekana kuunda usanifu safi na seva ya kawaida na seva ya ngazi ya chini lakini kuna hoja kwamba ni rahisi kidogo na seva ya ngazi ya chini.
- Upatikanaji wa kipengele. Vipengele vingine vya juu vinaweza kutumika tu na
    seva ya ngazi ya chini. Sura za baadaye huzungumzia Elicitation na kipengele cha diwaridhifa cha Sampling,
    ambacho kimefutwa matumizi kwenye MCP `2026-07-28`.

## Seva ya kawaida dhidi ya seva ya ngazi ya chini

Hivi ndivyo muundo wa kuunda Seva ya MCP unavyoonekana na seva ya kawaida

**Python**

```python
mcp = FastMCP("Demo")

# Ongeza chombo cha kuongeza
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

// Ongeza chombo cha kuongeza
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

Madhumuni ni kwamba unaongeza kila chombo, rasilimali au maelekezo unayotaka seva iwe nayo waziwazi. Hakuna tatizo na hilo.  

### Njia ya seva ya ngazi ya chini

Hata hivyo, unapotumia njia ya seva ya ngazi ya chini unahitaji kufikiri tofauti. Badala ya kusajili kila chombo, unaunda washughulikiaji wawili kwa kila aina ya kipengele (vifaa, rasilimali au maelekezo). Kwa mfano, vifaa vina kazi mbili tu kama ifuatavyo:

- Orodhesha vifaa vyote. Kazi moja itakuwa na jukumu la kuorodhesha vifaa vyote.
- shughulikia kuitwa kwa vifaa vyote. Pia hapa kuna kazi moja tu inayoshughulikia simu ya chombo

Hii inaonekana kama kazi kidogo, sivyo? Kwa hivyo badala ya kusajili chombo, nahitaji tu kuhakikisha chombo kiko kwenye orodha ninapoorodhesha vifaa vyote na kinapoitwa pale panapokuja ombi la kuitwa chombo. 

Tazama jinsi msimbo unavyoonekana sasa:

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
  // Rudisha orodha ya zana zilizojisajili
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

Hapa sasa tuna kazi inayorejea orodha ya vipengele. Kila kipengele kwenye orodha ya vifaa sasa kina sehemu kama `name`, `description` na `inputSchema` kufuatilia aina inayorejea. Hii inatuwezesha kuweka vifaa vyetu na ufafanuzi wa vipengele mahali pengine. Sasa tunaweza kuunda vifaa vyote kwenye folda ya vifaa na vivyo hivyo kwa vipengele vyako vyote ili mradi wako upangwa kama ifuatavyo:

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

Hiyo ni nzuri, usanifu wetu unaweza kuonekana safi sana.

Kuhusu kuitwa kwa vifaa, je, ni wazo lile lile, msimamizi mmoja kwa kuitwa kwa chombo chochote? Ndiyo, haswa, hapa kuna msimbo wa hilo:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # zana ni kamusi iliyo na majina ya zana kama funguo
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
    
    // hoja: request.params.arguments
    // TODO piga chombo hicho,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kama unavyoona kutoka kwa msimbo huu wa juu, tunahitaji kuchambua chombo kitakachoitwa, na kwa hoja gani, kisha tunaendelea kuitwa kwa chombo.

## Kuboresha njia kwa uthibitishaji

Hadi sasa, umeona jinsi usajili wako wote wa kuongeza vifaa, rasilimali na maelekezo unavyoweza kubadilishwa na washughulikiaji hawa wawili kwa kila aina ya kipengele. Je, ni nini kingine tunachohitaji kufanya? Kweli, tunapaswa kuongeza aina fulani ya uthibitishaji kuhakikisha kuwa chombo kinaitwa kwa hoja sahihi. Kila runtime ina suluhisho lake kwa hili, kwa mfano Python inatumia Pydantic na TypeScript inatumia Zod. Wazo ni kufanya yafuatayo:

- Hamisha mantiki ya kuunda kipengele (chombo, rasilimali au maelekezo) kwenye folda yake maalum.
- Ongeza njia ya kuthibitisha ombi linalokuja, kwa mfano kuuliza kuitwa kwa chombo.

### Unda kipengele

Kuunda kipengele, tutahitaji kuunda faili kwa ajili ya kipengele hicho na kuhakikisha kina sehemu muhimu zinazohitajika kwa kipengele hicho. Sehemu hizi zinatofautiana kidogo kati ya vifaa, rasilimali na maelekezo.

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
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ongeza Pydantic, ili tuweze kuunda AddInputModel na kuthibitisha hujambo

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

hapa unaona jinsi tunavyofanya yafuatayo:

- Unda skimu kwa kutumia Pydantic `AddInputModel` yenye sehemu `a` na `b` kwenye faili *schema.py*.
- Jaribu kuchambua ombi linalokuja liwe la aina `AddInputModel`, kama kuna mabadiliko kwenye vigezo hii itasababisha kutokwenda sawa:

   ```python
   # add.py
    try:
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Unaweza kuchagua kuweka mantiki hii ya uchambuzi moja kwa moja katika simu ya chombo au kwenye kazi ya mshughulikiaji.

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

       // @ts-sahau
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

// ongeza.ts
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

- Katika mshughulikiaji anayeangalia simu zote za chombo, sasa tunajaribu kuchambua ombi linaloingia kwa njia ya skimu iliyofafanuliwa na chombo:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kama hili linafanikiwa basi tunaendelea kuitwa kwa chombo halisi:

    ```typescript
    const result = await tool.callback(input);
    ```

Kama unavyoona, njia hii huunda usanifu mzuri huku kila kitu kikiwa na mahali pake, faili *server.ts* ni ndogo sana inayounganisha washughulikiaji wa maombi na kila kipengele kiko kwenye folda yake inayofaa yaani tools/, resources/ au /prompts.

Nzuri, hebu jaribu kuijenga hii ifuatayo. 

## Mazoezi: Kuunda seva ya ngazi ya chini

Katika zoezi hili, tutafanya yafuatayo:

1. Unda seva ya ngazi ya chini inayoshughulikia orodha ya vifaa na kuitwa kwa vifaa.
1. Tekeleza usanifu unaoweza kujengea juu.
1. Ongeza uthibitishaji kuhakikisha simu za chombo ni sahihi.

### -1- Unda usanifu

Kitu cha kwanza tunachohitaji kushughulikia ni usanifu unaotusaidia kupanua tunapoongeza vipengele zaidi, hii ndivyo inavyoonekana:

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

Sasa tumetengeneza usanifu unaohakikisha tunaweza kuongeza vifaa vipya kwa urahisi kwenye folda ya vifaa. Haliwezi kufuata hii kuongeza vitengo kwa ajili ya rasilimali na maelekezo.

### -2- Kuunda chombo

Hebu tuone jinsi kuunda chombo kunavyoonekana ifuatayo. Kwanza, kinapaswa kuundwa katika folda yake ndogo ya *tool* kama ifuatavyo:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ongeza Pydantic, ili tuweze kuunda AddInputModel na kuthibitisha hoja

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Kinachoonekana hapa ni jinsi tunavyofafanua jina, maelezo, na skimu ya ingizo kwa kutumia Pydantic pamoja na mshughulikiaji atakayeitwa mara chombo hiki kitapigiwa simu. Mwishowe, tunaonyesha `tool_add` ambayo ni kamusi inayoshikilia sifa hizi zote.

Pia kuna *schema.py* inayotumika kufafanua skimu ya ingizo inayotumiwa na chombo chetu:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tunahitaji pia kujaza faili *__init__.py* kuhakikisha folda ya vifaa inatambuliwa kama moduli. Zaidi ya hayo, tunahitaji kuonyesha moduli zilizo ndani kama ifuatavyo:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tunaweza kuendelea kuongeza kwenye faili hii tunapoendelea kuongeza vifaa.

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

Hapa tunaunda kamusi yenye sifa zifuatazo:

- name, hii ni jina la chombo.
- rawSchema, hii ni skimu ya Zod, itatumiwa kuthibitisha maombi yanayoingia ya kuitwa chombo hiki.
- inputSchema, skimu hii itatumika na mshughulikiaji.
- callback, hii hutumiwa kuita chombo.

Pia kuna `Tool` inayotumika kubadilisha kamusi hii kuwa aina ambayo mshughulikiaji wa seva ya mcp anaweza kupokea na inavyoonekana kama ifuatavyo:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Na kuna *schema.ts* ambapo tunahifadhi skimu za ingizo kwa kila chombo ambapo kwa sasa kuna skimu moja tu lakini tunapoendelea kuingiza vifaa tunaweza kuongeza zaidi:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nzuri, twende tukashughulikie orodha ya vifaa ifuatayo.

### -3- Shughulikia orodha ya chombo

Ifuatayo, kushughulikia orodha ya vifaa vyetu, tunahitaji kuweka mshughulikiaji wa maombi kwa hili. Hapa ni kile tunachohitaji kuongeza kwenye faili ya seva:

**Python**

```python
# msimbo umefupishwa kwa ufupi
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

Hapa, tunaongeza kipambanuzi `@server.list_tools` na kazi ya kutekeleza `handle_list_tools`. Katika hii, tunapaswa kuzalisha orodha ya vifaa. Angalia jinsi kila chombo kinahitaji kuwa na jina, maelezo na inputSchema.   

**TypeScript**

Kuhakikisha mshughulikiaji wa maombi kwa orodha ya vifaa, tunahitaji kuita `setRequestHandler` kwenye seva na skimu inayoendana na kile tunachotaka kufanya, katika kesi hii `ListToolsRequestSchema`. 

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
// msimbo umeachwa kwa ufupi
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Rudisha orodha ya zana zilizosajiliwa
  return {
    tools: tools
  };
});
```

Nzuri, sasa tumesuluhisha sehemu ya orodha ya vifaa, hebu tazame jinsi tunavyoweza kuitwa kwa vifaa ifuatayo.

### -4- Shughulikia kuitwa kwa chombo

Kuitwa kwa chombo, tunahitaji kuweka mshughulikiaji mwingine wa maombi, wakati huu ukilenga kushughulikia ombi linalobainisha ni kipengele gani kuita na kwa hoja gani.

**Python**

Tumia kipambanuzi `@server.call_tool` na utekeleze kwa kazi kama `handle_call_tool`. Ndani ya kazi hiyo, tunahitaji kuchambua jina la chombo, hoja zake na kuhakikisha kuwa hoja hizo ni sahihi kwa chombo husika. Tunaweza kuthibitisha hoja hizi ndani ya kazi hii au baadaye katika chombo halisi.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # zana ni kamusi yenye majina ya zana kama funguo
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # itumie zana
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Hivi ndivyo inavyofanyika:

- Jina letu la chombo tayari liko kama parameter ya ingizo `name` ambayo ni kweli kwa hoja zetu katika kamusi ya `arguments`.

- Chombo kinaitwa kwa `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Uthibitishaji wa hoja hufanyika katika sifa ya `handler` ambayo inaonyesha kazi, kama itashindwa itatoa kosa. 

Hapo, sasa tumeelewa kabisa jinsi ya kuorodhesha na kuitwa kwa vifaa kwa kutumia seva ya ngazi ya chini.

Angalia [mfano kamili](./code/README.md) hapa

## Kazi ya nyumbani

Panua msimbo uliotolewa kwa idadi ya vifaa, rasilimali na maelekezo na tafakari jinsi unavyogundua kuwa unahitaji kuongeza tu faili katika folda ya vifaa na si mahali pengine. 

*Hakuna suluhisho lililotolewa*

## Muhtasari

Katika sura hii, tuliangalia jinsi njia ya seva ya ngazi ya chini ilivyofanya kazi na jinsi inavyoweza kutusaidia kuunda usanifu mzuri tunaoweza kuendelea kujenga juu yake. Pia tulijadili uthibitishaji na ulionyeshwa jinsi ya kutumia maktaba za uthibitishaji kuunda skimu za uthibitishaji wa ingizo.

## Nini Kifuatayo

- Ifuatayo: [Uthibitishaji Rahisi](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Matumizi ya juu ya seva

Kuna aina mbili tofauti za seva zilizowekwa katika MCP SDK, seva yako ya kawaida na seva ya ngazi ya chini. Kawaida, utatumia seva ya kawaida kuongeza vipengele ndani yake. Lakini kwa baadhi ya kesi, unaweza kutegemea seva ya ngazi ya chini kama vile:

- Miundo bora. Inawezekana kuunda usanifu safi kwa seva ya kawaida na seva ya ngazi ya chini lakini kuna hoja kwamba ni rahisi zaidi kidogo kwa seva ya ngazi ya chini.
- Upatikanaji wa vipengele. Baadhi ya vipengele vya juu vinaweza kutumika tu na seva ya ngazi ya chini. Hii utaiona katika sura zinazofuata tunapoongeza sampuli na kuchochea.

## Seva ya kawaida dhidi ya seva ya ngazi ya chini

Huu ndio muonekano wa kuunda MCP Server kwa seva ya kawaida

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

Dharura ni kwamba unaongeza kwa makusudi kila zana, rasilimali au onyo unayotaka seva iwe nayo. Hakuna kosa lolote katika hilo.

### Njia ya seva ya ngazi ya chini

Hata hivyo, unapotumia njia ya seva ya ngazi ya chini unahitaji kuifikiria tofauti. Badala ya kusajili kila zana, unaunda handlers mbili kwa kila aina ya kipengele (zana, rasilimali au onyo). Kwa mfano, zana zina kazi mbili tu kama ifuatavyo:

- Orodhesha zana zote. Kazi moja inahusika na majaribio yote ya kuorodhesha zana.
- Kushughulikia kuita zana zote. Hapa pia, kuna kazi moja tu inayoshughulikia miito kwa zana.

Hii inaonekana kama kazi ndogo, sivyo? Badala ya kusajili zana, ninahitaji tu kuhakikisha zana inaorodheshwa ninapoorodhesha zana zote na inaitwa pale pa ombi la kuwaita zana linapokuja.

Tuchukulie muonekano wa sasa wa msimbo:

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
  // Rejesha orodha ya zana zilizoorodheshwa
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

Hapa sasa tuna kazi inayorejesha orodha ya vipengele. Kila kipengele katika orodha za zana sasa kina nyanja kama `name`, `description` na `inputSchema` ili kufuata aina ya kurudisha. Hii inatuwezesha kuweka zana na ufafanuzi wa kipengele mahali pengine. Sasa tunaweza kuunda zana zetu zote katika folda ya zana na vivyo hivyo kwa vipengele vyote ili mradi wako uwe umepangwa kama ifuatavyo:

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

Hiyo ni nzuri, usanifu wetu unaweza kuonekana safi kabisa.

Je, juu ya kuwaita zana, ni ile wazo hilo hilo then, handler moja kwa kuitwa zana, zana yoyote? Ndiyo, kabisa, hapa ni msimbo wa hilo:

**Python**

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
    // TODO piga simu zana,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kama unavyoona kutoka msimbo juu, tunahitaji kuchambua zana ya kuitwa, na kwa hoja zipi, na kisha tuendelee kuitwa kwa zana hiyo.

## Kuboresha njia hii kwa uthibitishaji

Mpaka sasa, umeona jinsi usajili wako wote wa kuongeza zana, rasilimali na onyo unavyoweza kubadilishwa na handlers hizi mbili kwa kila aina ya kipengele. Tunachohitaji kingine ni nini? Naam, tunapaswa kuongeza aina fulani ya uthibitishaji kuhakikisha kuwa zana inaitwa kwa hoja sahihi. Kila runtime ina suluhisho lao kwa hili, kwa mfano Python inatumia Pydantic na TypeScript inatumia Zod. Wazo ni kwamba tunafanya yafuatayo:

- Hamisha mantiki ya kuunda kipengele (zana, rasilimali au onyo) kwenda kwenye folda yake maalum.
- Ongeza njia ya kuthibitisha ombi linalokuja la kwa mfano kuitwa kwa zana.

### Kuunda kipengele

Ili kuunda kipengele, tutahitaji kuunda faili kwa kipengele hicho na kuhakikisha kina nyanja muhimu zinazotakiwa kwa kipengele hicho. Nyanja ambazo hutofautiana kidogo kati ya zana, rasilimali na onyo.

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

    # TODO:ongeza Pydantic, ili tuweze kuunda AddInputModel na kuthibitisha hoja

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

hapa unaweza kuona tunafanya yafuatayo:

- Kuunda schema kutumia Pydantic `AddInputModel` na nyanja `a` na `b` katika faili *schema.py*.
- Jaribu kuchambua ombi linalokuja kuwa aina ya `AddInputModel`, ikiwa kuna tofauti katika vigezo hii itasukuma kosa:

   ```python
   # add.py
    try:
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Unaweza kuchagua kuweka mantiki hii ya kuchambua ndani ya wito wa zana yenyewe au katika kazi ya handler.

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

- Katika handler inayoshughulikia miito yote ya zana, sasa tunajaribu kuchambua ombi linalokuja ndani ya schema iliyotangazwa na zana:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ikiwa hiyo itafanya kazi basi tutaendelea kuitwa kwa zana halisi:

    ```typescript
    const result = await tool.callback(input);
    ```

Kama unavyoona, njia hii inaunda usanifu mzuri kwani kila kitu kina mahali pake, *server.ts* ni faili ndogo sana inayounganisha handlers za maombi na kila kipengele kiko katika folda zake zinazohusika yaani tools/, resources/ au /prompts.

Nzuri, tujaribu kuunda hii ipitayo.

## Zoef: Kuunda seva ya ngazi ya chini

Katika zoezi hili, tutafanya yafuatayo:

1. Kuunda seva ya ngazi ya chini inayoshughulikia orodha ya zana na miito ya zana.
1. Kutekeleza usanifu unaoweza kujengwa juu yake.
1. Ongeza uthibitishaji kuhakikisha miito yako ya zana inathibitishwa ipasavyo.

### -1- Kuunda usanifu

Kitu cha kwanza tunachopaswa kushughulikia ni usanifu ambao unatupa uwezo wa kupanua sehemu zaidi tunapoongeza vipengele, huu ndio muonekano wake:

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

Sasa tumeanzisha usanifu unaohakikisha tunaweza kuongeza zana mpya kwa urahisi ndani ya folda ya tools. Ruhusu kufuatilia hii kuongeza folda ndogo kwa resources na prompts.

### -2- Kuunda zana

Tuchukulie muonekano wa kuunda zana. Kwanza, inapaswa kuundwa katika folda yake ndogo ya *tool* kama ifuatavyo:

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

Tunachoona hapa ni jinsi tunavyofafanua jina, maelezo, na schema ya kuingiza kwa kutumia Pydantic na handler ambayo itaitwa mara zana hii itakapotumiwa. Mwishowe, tunafichua `tool_add` ambayo ni kamusi inayoashiria mali zote hizi.

Pia kuna *schema.py* inayotumika kufafanua schema ya kuingiza inayotumika na zana yetu:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Pia tunahitaji kujaza *__init__.py* ili kuhakikisha folda ya tools inachukuliwa kama moduli. Zaidi, tunahitaji kufichua moduli ndani yake kama ifuatavyo:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tunaweza kuendelea kuongeza kwenye faili hili tunapoingiza zana zaidi.

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

Hapa tunaunda kamusi inayojumuisha mali:

- name, hii ni jina la zana.
- rawSchema, hii ni schema ya Zod, itatumika kuthibitisha maombi yanayoingia ya kuitwa kwa zana hii.
- inputSchema, schema hii itatumika na handler.
- callback, hii inatumika kuita zana.

Pia kuna `Tool` inayotumika kubadilisha kamusi hii kuwa aina inayokubalika na handler wa seva ya mcp na inaonekana kama ifuatavyo:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Na kuna *schema.ts* ambapo tunahifadhi schemas za kuingiza kwa kila zana ambazo zinaonekana hivi na kama sasa schema moja tu lakini tunapoongeza zana tunaweza kuongeza ingizo zaidi:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nzuri, tuchukulie sasa kushughulikia orodha ya zana zetu.

### -3- Shughulikia orodha ya zana

Ili kushughulikia orodha ya zana zetu, tunahitaji kuweka handler wa ombi la hilo. Hapa ni kile tunachotakiwa kuongeza katika faili ya seva:

**Python**

```python
# msimbo umefutwa kwa ufupi
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

Hapa, tunaongeza dekoreta `@server.list_tools` na kazi inayotekeleza `handle_list_tools`. Katika hii, tunapaswa kutoa orodha ya zana. Kumbuka kila zana inapaswa kuwa na jina, maelezo na inputSchema.

**TypeScript**

Ili kuweka handler wa ombi kwa ajili ya kuorodhesha zana, tunahitaji kuita `setRequestHandler` kwenye seva na schema inayolingana na tunachojaribu kufanya, katika kesi hii `ListToolsRequestSchema`.

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
// msimbo umeondolewa kwa ufupi
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Rudisha orodha ya zana zilizosajiliwa
  return {
    tools: tools
  };
});
```

Nzuri, sasa tumesuluhisha sehemu ya kuorodhesha zana, tuchukulie jinsi tunavyoweza kuita zana zetu.

### -4- Shughulikia kuitwa kwa zana

Ili kuita zana, tunahitaji kuweka handler mwingine wa ombi, wakati huu ukilenga kushughulikia ombi linalobainisha kipengele cha kuitwa na na hoja zipi.

**Python**

Tutatumia dekoreta `@server.call_tool` na kuitekeleza na kazi kama `handle_call_tool`. Ndani ya kazi hii, tunapaswa kuchambua jina la zana, hoja zake na kuhakikisha hoja ni sahihi kwa zana husika. Tunaweza kuthibitisha hoja ndani ya kazi hii au baadaye katika zana yenyewe.

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

Hapa ni kinachoendelea:

- Jina la zana limekwisha kuwepo kama parameter ya kuingiza `name` ambayo pia ni kweli kwa hoja zetu katika kamusi ya `arguments`.

- Zana inaitwa na `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Uthibitishaji wa hoja unafanyika katika mali ya `handler` inayong'atia kazi, ikiwa itashindwa itatoa kosa.

Hapo, sasa tuna uelewa kamili wa kuorodhesha na kuitwa kwa zana kwa kutumia seva ya ngazi ya chini.

Tazama [mfano kamili](./code/README.md) hapa

## Mradi

Panua msimbo uliotolewa kwa idadi ya zana, rasilimali na onyo na fikiria jinsi unavyogundua kuwa unahitaji tu kuongeza faili ndani ya folda ya tools na mahali pengine siyo.

*Hakuna suluhisho lililotolewa*

## Muhtasari

Katika sura hii, tuliiona jinsi njia ya seva ya ngazi ya chini ilivyofanya kazi na jinsi inavyotusaidia kuunda usanifu mzuri tunaweza kuendelea kuujenga. Pia tulijadili uthibitishaji na ulipewa jinsi ya kufanya kazi na maktaba za uthibitishaji kuunda schemas kwa uthibitishaji wa kuingiza.

## Ijayo ni nini

- Ifuatayo: [Uthibitishaji Rahisi](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kumbusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri kwa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upotovu wa maana. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa za muhimu sana, tafsiri ya kitaalamu kwa binadamu inapendekezwa. Hatubeba dhima kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Matumizi ya seva ya juu

Kuna aina mbili tofauti za seva zilizowekwa katika MCP SDK, seva yako ya kawaida na seva ya chini-kiwango. Kawaida, ungetumia seva ya kawaida kuongeza vipengele kwake. Hata hivyo kwa baadhi ya matukio, unataka kutegemea seva ya chini-kiwango kama vile:

- Miundombinu bora. Inawezekana kuunda miundombinu safi kwa seva ya kawaida pamoja na seva ya chini-kiwango lakini inaweza kudaiwa kuwa ni rahisi kidogo kwa seva ya chini-kiwango.
- Upatikanaji wa kipengele. Baadhi ya vipengele vya hali ya juu vinaweza kutumika tu kwa seva ya chini-kiwango. Hii utaiona katika sura za baadaye tunapoongeza sampuli na elicitation.

## Seva ya kawaida dhidi ya seva ya chini-kiwango

Hivi ndivyo uundaji wa MCP Server unavyoonekana na seva ya kawaida

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

Madhumuni ni kwamba unaongeza kila chombo, rasilimali au prompt unayotaka seva iwe nayo kwa uwazi. Hakuna kosa lolote kuhusu hilo.  

### Njia ya seva ya chini-kiwango

Hata hivyo, unapotumia njia ya seva ya chini-kiwango unahitaji kufikiria tofauti. Badala ya kusajili kila chombo, badala yake unaunda handlers mbili kwa kila aina ya kipengele (vifaa, rasilimali au prompts). Kwa mfano vifaa vinaweza kuwa na kazi mbili tu kama ifuatavyo:

- Orodhesha vifaa vyote. Kazi moja itahusiana na majaribio yote ya kuorodhesha vifaa.
- utunzaji wa kuita vifaa vyote. Hapa pia, kuna kazi moja tu inayosimamia maombi ya kuita chombo

Hiyo inaonekana kama kazi kidogo, sivyo? Kwa hivyo badala ya kusajili chombo, ninahitaji tu kuhakikisha chombo kimeorodheshwa ninapoorodhesha vifaa vyote na kinapoitwa linapokuwapo ombi la kuwaita chombo.

Tuchunguze sasa jinsi msimbo unavyoonekana:

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
  // Rudisha orodha ya zana zilizosajiliwa
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

Hapa sasa tuna kazi inayorejesha orodha ya vipengele. Kila kipengele kwenye orodha ya vifaa sasa kina nyanja kama `name`, `description` na `inputSchema` kufuata aina ya kurudisha. Hii inatuwezesha kuweka vifaa vyetu na ufafanuzi wa kipengele mahali pengine. Sasa tunaweza kuunda vifaa vyote kwenye folda ya vifaa na vivyo hivyo kwa vipengele vyako wote ili mradi wako ungepangwa kwa namna ifuatayo:

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

Hiyo ni nzuri, miundombinu yetu inaweza kuonekana safi kabisa.

Je, kuhusu kuitwa kwa vifaa, je ni wazo lile lile basi, handler moja ya kuitwa kwa chombo chochote? Ndiyo, hasa, hii hapa ni msimbo wa hilo:

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
    // TODO piga simu kwa chombo,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kama unavyoona kutoka msimbo hapo juu, tunahitaji kuchambua chombo cha kuitwa, na na hoja zipi, kisha tunaendelea kuitwa kwa chombo hicho.

## Kuboresha njia kwa uthibitishaji

Hadi sasa, umeona jinsi usajili wako wote wa kuongeza vifaa, rasilimali na prompts unaweza kubadilishwa na handlers hizi mbili kwa kila aina ya kipengele. Je, tunahitaji kufanya nini zaidi? Naam, tunapaswa kuongeza aina fulani ya uthibitishaji ili kuhakikisha chombo kinaitwa na hoja sahihi. Kila runtime ina suluhisho lake kwa hili, kwa mfano Python hutumia Pydantic na TypeScript hutumia Zod. Mawazo ni yafuatayo:

- Hamisha mantiki ya kuunda kipengele (chombo, rasilimali au prompt) kwenda folda yake maalum.
- Ongeza njia ya kuthibitisha ombi linalokuja likiomba kwa mfano kuitwa kwa chombo.

### Unda kipengele

Ili kuunda kipengele, tutahitaji kuunda faili ya kipengele hicho na kuhakikisha ina nyanja za lazima zinazotakiwa kutoka kwa kipengele hicho. Nyanja hizi hutofautiana kidogo kati ya vifaa, rasilimali na prompts.

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

    # TODO: ongeza Pydantic, ili tuweze kuunda AddInputModel na kuthibitisha hujazo

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

hapa unaweza kuona jinsi tunavyofanya yafuatayo:

- Unda schema kutumia Pydantic `AddInputModel` na nyanja `a` na `b` kwenye faili *schema.py*.
- Jaribu kuchambua ombi linalokuja liwe la aina `AddInputModel`, ikiwa kuna tofauti ya hoja hii itasababisha makosa:

   ```python
   # add.py
    try:
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Unaweza kuchagua kuweka mantiki hii ya kuchambua katika mwito wa chombo yenyewe au katika kazi ya handler.

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

- Kwenye handler inayoshughulikia miito yote ya chombo, sasa tunajaribu kuchambua ombi linalokuja kuwa kwa schema iliyoainishwa ya chombo:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kama hiyo itafanya kazi basi tunaendelea kuitwa kwa chombo halisi:

    ```typescript
    const result = await tool.callback(input);
    ```

Kama unavyoona, njia hii huunda miundombinu nzuri kwa sababu kila kitu kina mahali pake, *server.ts* ni faili ndogo inayowasha tu handlers wa maombi na kila kipengele kipo kwenye folda yake ya muktadha yaani tools/, resources/ au /prompts.

Nzuri, hebu tujaribu kuunda hii ifuatayo.

## Mazoezi: Kuunda seva ya chini-kiwango

Katika zoezi hili, tutafanya yafuatayo:

1. Unda seva ya chini-kiwango inayoshughulikia orodha ya vifaa na miito ya vifaa.
2. Tekeleza miundombinu unaweza kuijenga juu yake.
3. Ongeza uthibitishaji kuhakikisha miito yako ya chombo inathibitishwa ipasavyo.

### -1- Unda miundombinu

Kitu cha kwanza tunachohitaji kushughulikia ni miundombinu inayotusaidia kupanua tunapoongeza vipengele zaidi, hii ndiyo hiyo:

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

Sasa tumeanzisha miundombinu inayohakikisha tunaweza kuongeza vifaa vipya kwa urahisi kwenye folda ya vifaa. Hisia huru kufuata hili kuongeza saraka ndogo kwa rasilimali na prompts.

### -2- Kuunda chombo

Tuchukue jinsi chombo kinavyoundwa. Kwanza, kinatakiwa kuundwa kwenye saraka yake ndogo ya *tool* kama ifuatavyo:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Thibitisha ingizo kwa kutumia mfano wa Pydantic
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: ongeza Pydantic, ili tuweze kuunda AddInputModel na kuthibitisha argumeenti

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tunavyoona hapa ni jinsi tunavyofafanua jina, maelezo, na input schema kutumia Pydantic na handler atakayetimizwa mara chombo hiki kitapigiwa simu. Mwishowe, tunaonyesha `tool_add` ambayo ni kamusi inayoshikilia mali hizi zote.

Pia kuna *schema.py* inayotumika kufafanua input schema inayotumika na chombo chetu:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Pia tunahitaji kujaza *__init__.py* kuhakikisha saraka ya vifaa inatambuliwa kama moduli. Zaidi ya hayo, tunahitaji kuonesha moduli zilizo ndani yake kama ifuatavyo:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tunaweza kuendelea kuongeza kwenye faili hii tunapoongeza vifaa zaidi.

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

Hapa tunaunda kamusi yenye mali:

- name, hili ni jina la chombo.
- rawSchema, hii ni schema ya Zod, itatumiwa kuthibitisha maombi yanayoingia ya kuita chombo hiki.
- inputSchema, schema hii itatumika na handler.
- callback, hii hutumika kupiga simu chombo.

Pia kuna `Tool` inayotumiwa kubadilisha kamusi hii kuwa aina ambayo handler wa seva ya mcp anaweza kubali na inavyoonekana kama ifuatavyo:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Na kuna *schema.ts* ambapo tunahifadhi schemas za ingizo kwa kila chombo kama ifuatavyo na schema moja tu kwa sasa lakini tunapoongeza vifaa tunaweza kuongeza maingizo zaidi:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nzuri, tuendelee sasa kushughulikia orodha ya vifaa vyetu.

### -3- Shughulikia orodha ya chombo

Ifuatayo, kushughulikia orodha ya vifaa vyetu, tunahitaji kuweka handler ya maombi kwa ajili ya hilo. Hii hapa tunazotakiwa kuongeza kwenye faili yetu ya seva:

**Python**

```python
# msimbo umefafanuliwa kwa ufupi
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

Hapa, tunongeza dekoreta `@server.list_tools` na kazi inayotekeleza `handle_list_tools`. Katika hii ya mwisho, tunahitaji kutoa orodha ya vifaa. Angalia kama kila chombo kinapasa kuwa na jina, maelezo na inputSchema.

**TypeScript**

Ili kuweka handler wa ombi la kuorodhesha vifaa, tunahitaji kuita `setRequestHandler` kwenye seva na schema inayofaa kwa kile tunachojaribu kufanya, katika kesi hii `ListToolsRequestSchema`. 

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

Nzuri, sasa tumetatua sehemu ya orodha ya vifaa, tuchunguze jinsi tunavyoweza kuitisha vifaa ifuatayo.

### -4- Shughulikia kuitwa kwa chombo

Kuita chombo, tunahitaji kuweka handler mwingine wa maombi, wakati huu ukizingatia kushughulikia ombi linaloelezea ni kipengele gani kaitawekwa na kwa hoja zipi.

**Python**

Tumtumia dekoreta `@server.call_tool` na kutekeleza kwa kazi kama `handle_call_tool`. Ndani ya kazi hiyo, tunahitaji kuchambua jina la chombo, hoja zake na kuhakikisha hoja hizo zina sahihi kwa chombo kinachotazamiwa. Tunaweza kuthibitisha hoja ndani ya kazi hii au baadaye ndani ya chombo halisi.

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
        # itumie zana hiyo
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Hivi ndivyo inavyotendeka:

- Jina la chombo yetu tayari liko kama parameter ya input `name` ambayo ni kweli kwa hoja zetu katika kamusi ya `arguments`.

- Chombo kinaitwa kwa `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Uthibitishaji wa hoja hutokea katika mali ya `handler` ambayo inaonyesha kazi, kama ikishindikana itatoa ubaguzi.

Sasa, tunaelewa kikamilifu kuorodhesha na kuitisha vifaa kwa kutumia seva ya chini-kiwango.

Tazama [mfano kamili](./code/README.md) hapa

## Kazi ya nyumbani

Panua msimbo uliotolewa kwa vifaa kadhaa, rasilimali na prompt na angalia jinsi unavyoona kwamba unahitaji tu kuongeza faili katika saraka ya vifaa na si mahali pengine.

*Hakuna suluhisho lililotolewa*

## Muhtasari

Katika sura hii, tumeona jinsi njia ya seva ya chini-kiwango ilivyofanya kazi na jinsi inavyoweza kutusaidia kuunda miundombinu nzuri tunaweza kuendelea kujenga juu yake. Pia tulijadili uthibitishaji na ulionyeshwa jinsi ya kufanya kazi na maktaba za uthibitishaji kuunda schemas za uthibitisho wa ingizo.

## Nini kinakuja baadaye

- Ifuatayo: [Uthibitishaji Rahisi](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Maelezo ya kuacha majukumu**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri zilizotengenezwa kwa automatiska zinaweza kuwa na makosa au upotoshaji. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu na binadamu inapendekezwa. Hatuna dhamana kwa kutokuelewana au kutoeleweka kwa makusudi kunakotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
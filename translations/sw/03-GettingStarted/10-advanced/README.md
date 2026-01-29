# Matumizi ya Juu ya Seva

Kuna aina mbili za seva zinazotolewa katika MCP SDK, seva ya kawaida na seva ya kiwango cha chini. Kwa kawaida, ungetumia seva ya kawaida kuongeza vipengele. Hata hivyo, kuna baadhi ya hali ambapo unahitaji kutegemea seva ya kiwango cha chini, kama:

- Muundo bora. Inawezekana kuunda muundo safi kwa kutumia seva ya kawaida na seva ya kiwango cha chini, lakini inaweza kusemwa kuwa ni rahisi kidogo na seva ya kiwango cha chini.
- Upatikanaji wa vipengele. Baadhi ya vipengele vya hali ya juu vinaweza kutumika tu na seva ya kiwango cha chini. Utaona hili katika sura zijazo tunapoongeza sampuli na uchochezi.

## Seva ya Kawaida vs Seva ya Kiwango cha Chini

Hivi ndivyo uundaji wa MCP Server unavyoonekana kwa kutumia seva ya kawaida:

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

Hoja ni kwamba unaongeza wazi kila zana, rasilimali au maelezo unayotaka seva iwe nayo. Hakuna tatizo na hilo.

### Njia ya Seva ya Kiwango cha Chini

Hata hivyo, unapochagua kutumia njia ya seva ya kiwango cha chini, unahitaji kufikiria kwa njia tofauti, yaani badala ya kusajili kila zana, unaunda wahandaji wawili kwa kila aina ya kipengele (zana, rasilimali au maelezo). Kwa mfano, kwa zana, unakuwa na kazi mbili tu kama ifuatavyo:

- Orodhesha zana zote. Kazi moja itakuwa na jukumu la majaribio yote ya kuorodhesha zana.
- Kushughulikia miito ya zana zote. Hapa pia, kuna kazi moja tu inayoshughulikia miito ya zana.

Hilo linaonekana kama kazi ndogo, sivyo? Badala ya kusajili zana, ninahitaji tu kuhakikisha zana imeorodheshwa wakati ninapoorodhesha zana zote na kwamba inaitwa wakati kuna ombi linaloingia la kuitumia zana.

Hebu tuangalie jinsi msimbo unavyoonekana sasa:

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

Hapa tuna kazi inayorejesha orodha ya vipengele. Kila kipengele katika orodha ya zana sasa kina sehemu kama `name`, `description` na `inputSchema` ili kufuata aina ya kurudi. Hii inatuwezesha kuweka zana zetu na ufafanuzi wa vipengele mahali pengine. Tunaweza sasa kuunda zana zetu zote katika folda ya zana na vivyo hivyo kwa vipengele vyote, hivyo mradi wetu unaweza kupangwa kama ifuatavyo:

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

Hilo ni zuri, muundo wetu unaweza kufanywa kuwa safi kabisa.

Vipi kuhusu kuitumia zana, je, ni wazo lile lile, mhusika mmoja wa kuitumia zana yoyote? Ndio, hasa, hapa kuna msimbo wa hilo:

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

Kama unavyoona kutoka kwa msimbo hapo juu, tunahitaji kuchambua zana ya kuitumia, na kwa hoja gani, kisha tunahitaji kuendelea kuitumia zana.

## Kuboresha Njia kwa Uthibitishaji

Hadi sasa, umeona jinsi usajili wako wote wa kuongeza zana, rasilimali na maelezo unaweza kubadilishwa na wahandaji hawa wawili kwa kila aina ya kipengele. Je, tunahitaji kufanya nini kingine? Naam, tunapaswa kuongeza aina fulani ya uthibitishaji ili kuhakikisha kuwa zana inaitwa na hoja sahihi. Kila mazingira ya utekelezaji yana suluhisho lake kwa hili, kwa mfano Python hutumia Pydantic na TypeScript hutumia Zod. Wazo ni kwamba tunafanya yafuatayo:

- Hamisha mantiki ya kuunda kipengele (zana, rasilimali au maelezo) kwenye folda yake maalum.
- Ongeza njia ya kuthibitisha ombi linaloingia linaloomba, kwa mfano, kuitumia zana.

### Kuunda Kipengele

Ili kuunda kipengele, tutahitaji kuunda faili kwa kipengele hicho na kuhakikisha kina sehemu za lazima zinazohitajika kwa kipengele hicho. Sehemu zinazohitajika zinatofautiana kidogo kati ya zana, rasilimali na maelezo.

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

Hapa unaweza kuona jinsi tunavyofanya yafuatayo:

- Unda schema kwa kutumia Pydantic `AddInputModel` na sehemu `a` na `b` katika faili *schema.py*.
- Jaribu kuchambua ombi linaloingia kuwa la aina `AddInputModel`, ikiwa kuna kutofautiana katika vigezo hili litashindwa:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Unaweza kuchagua kuweka mantiki hii ya uchambuzi katika mwito wa zana yenyewe au katika kazi ya mhusika.

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

- Katika mhusika anayeshughulikia miito yote ya zana, sasa tunajaribu kuchambua ombi linaloingia kuwa schema iliyofafanuliwa ya zana:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ikiwa hilo linafanikiwa basi tunaendelea kuitumia zana halisi:

    ```typescript
    const result = await tool.callback(input);
    ```

Kama unavyoona, njia hii inaunda muundo mzuri kwani kila kitu kina nafasi yake, *server.ts* ni faili ndogo sana inayounganisha wahandaji wa maombi na kila kipengele kiko katika folda zake husika, yaani tools/, resources/ au /prompts.

Zuri, hebu tujaribu kujenga hili sasa.

## Zoezi: Kuunda Seva ya Kiwango cha Chini

Katika zoezi hili, tutafanya yafuatayo:

1. Unda seva ya kiwango cha chini inayoshughulikia kuorodhesha zana na kuitumia zana.
1. Tekeleza muundo unaoweza kujengwa juu yake.
1. Ongeza uthibitishaji ili kuhakikisha miito ya zana zako inathibitishwa ipasavyo.

### -1- Unda Muundo

Jambo la kwanza tunalohitaji kushughulikia ni muundo unaotusaidia kupanuka tunapoongeza vipengele zaidi, hivi ndivyo unavyoonekana:

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

Sasa tumeweka muundo unaohakikisha tunaweza kuongeza zana mpya kwa urahisi katika folda ya zana. Jisikie huru kufuata hili ili kuongeza folda ndogo kwa rasilimali na maelezo.

### -2- Kuunda Zana

Hebu tuone jinsi kuunda zana kunavyoonekana. Kwanza, inahitaji kuundwa katika folda ndogo ya *tool* kama ifuatavyo:

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

Tunachokiona hapa ni jinsi tunavyofafanua jina, maelezo, schema ya pembejeo kwa kutumia Pydantic na mhusika atakayeitwa mara zana hii inapotumiwa. Mwisho, tunatoa `tool_add` ambayo ni kamusi inayoshikilia mali hizi zote.

Pia kuna *schema.py* inayotumika kufafanua schema ya pembejeo inayotumiwa na zana yetu:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Tunahitaji pia kujaza *__init__.py* ili kuhakikisha folda ya zana inachukuliwa kama moduli. Zaidi ya hayo, tunahitaji kutoa moduli ndani yake kama ifuatavyo:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Tunaweza kuendelea kuongeza faili hii tunapoongeza zana zaidi.

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

- name, hili ni jina la zana.
- rawSchema, hili ni schema ya Zod, itatumika kuthibitisha maombi yanayoingia ya kuitumia zana hii.
- inputSchema, schema hii itatumika na mhusika.
- callback, hii inatumika kuitumia zana.

Pia kuna `Tool` inayotumika kubadilisha kamusi hii kuwa aina ambayo mhusika wa seva ya MCP anaweza kukubali, na inaonekana kama ifuatavyo:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Na kuna *schema.ts* ambapo tunahifadhi schema za pembejeo kwa kila zana, inavyoonekana kama ifuatavyo ikiwa na schema moja tu kwa sasa lakini tunapoongeza zana tunaweza kuongeza maingizo zaidi:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Zuri, hebu tuendelee kushughulikia kuorodhesha zana zetu.

### -3- Kushughulikia Kuorodhesha Zana

Kisha, ili kushughulikia kuorodhesha zana zetu, tunahitaji kuweka mhusika wa ombi kwa hilo. Hivi ndivyo tunavyohitaji kuongeza kwenye faili ya seva yetu:

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

Hapa tunaongeza kivinjari `@server.list_tools` na kazi inayotekeleza `handle_list_tools`. Katika kazi ya mwisho, tunahitaji kutoa orodha ya zana. Angalia jinsi kila zana inavyohitaji kuwa na jina, maelezo na inputSchema.

**TypeScript**

Ili kuweka mhusika wa ombi kwa kuorodhesha zana, tunahitaji kuita `setRequestHandler` kwenye seva na schema inayofaa kile tunachojaribu kufanya, katika kesi hii `ListToolsRequestSchema`.

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

Zuri, sasa tumeshughulikia kipande cha kuorodhesha zana, hebu tuangalie jinsi tunavyoweza kuitumia zana.

### -4- Kushughulikia Kuitumia Zana

Ili kuitumia zana, tunahitaji kuweka mhusika mwingine wa ombi, wakati huu ukilenga kushughulikia ombi linaloeleza kipengele cha kuitumia na hoja gani.

**Python**

Hebu tutumie kivinjari `@server.call_tool` na tukitekeleze kwa kazi kama `handle_call_tool`. Ndani ya kazi hiyo, tunahitaji kuchambua jina la zana, hoja zake na kuhakikisha hoja hizo ni sahihi kwa zana husika. Tunaweza kuthibitisha hoja katika kazi hii au chini katika zana halisi.

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

Hivi ndivyo kinachotokea:

- Jina la zana yetu tayari lipo kama parameter ya pembejeo `name` ambayo ni kweli kwa hoja zetu katika mfumo wa kamusi ya `arguments`.

- Zana inaitwa na `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Uthibitishaji wa hoja hufanyika katika mali ya `handler` ambayo inaelekeza kwenye kazi, ikiwa hilo litashindwa litatoa hitilafu.

Hapo, sasa tunaelewa kikamilifu jinsi ya kuorodhesha na kuitumia zana kwa kutumia seva ya kiwango cha chini.

Tazama [mfano kamili](./code/README.md) hapa.

## Kazi

Panua msimbo uliyopewa kwa zana kadhaa, rasilimali na maelezo na tafakari jinsi unavyogundua kuwa unahitaji tu kuongeza faili katika folda ya zana na si mahali pengine.

*Hakuna suluhisho lililotolewa*

## Muhtasari

Katika sura hii, tumeona jinsi njia ya seva ya kiwango cha chini inavyofanya kazi na jinsi hiyo inaweza kutusaidia kuunda muundo mzuri tunaoweza kuendelea kujenga juu yake. Pia tulijadili uthibitishaji na ulionyeshwa jinsi ya kufanya kazi na maktaba za uthibitishaji kuunda schema za uthibitishaji wa pembejeo.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
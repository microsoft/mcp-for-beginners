# Fejlett szerver használat

Az MCP SDK-ban két különféle szervert érhetsz el: a normál szervert és az alacsony szintű szervert. Általában a normál szervert használod a funkciók hozzáadásához. Bizonyos esetekben azonban az alacsony szintű szerverre kell támaszkodnod, például:

- Jobb architektúra. Lehetséges tiszta architektúrát létrehozni mind a normál, mind az alacsony szintű szerverrel, de elmondható, hogy egy kicsit könnyebb az alacsony szintű szerverrel.
- Funkció elérhetőség. Néhány fejlett funkció csak alacsony szintű szerverrel használható. Ezt a későbbi fejezetekben fogod látni, amikor mintavételezést és kérdezést adunk hozzá.

## Normál szerver vs alacsony szintű szerver

Így néz ki egy MCP szerver létrehozása normál szerverrel

**Python**

```python
mcp = FastMCP("Demo")

# Adj hozzá egy összeadási eszközt
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

// Adj hozzá egy összeadási eszközt
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

A lényeg, hogy explicit módon adod hozzá az egyes eszközöket, erőforrásokat vagy promptokat, amelyeket a szervernek tartalmaznia kell. Ebben nincs semmi rossz.

### Alacsony szintű szerver megközelítés

Azonban ha alacsony szintű szerver megközelítést alkalmazol, másképp kell gondolkodnod. Az egyes eszközök regisztrálása helyett inkább típusonként (eszközök, erőforrások vagy promptok) két kezelőt hozol létre. Például az eszközöknek akkor csak két funkciójuk van:

- Az összes eszköz listázása. Egy funkció felel az összes eszközlista kérésekért.
- Az összes eszköz hívásának kezelése. Itt is csak egy funkció kezeli az adott eszköz hívásait.

Ez potenciálisan kevesebb munkának hangzik, ugye? Tehát eszköz regisztrálása helyett csak biztosítanom kell, hogy az eszköz szerepeljen az eszközök listájában, és hogy meghívják, amikor egy eszköz meghívására érkezik kérés.

Nézzük meg, hogy így hogyan néz ki a kód:

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
  // Adja vissza a regisztrált eszközök listáját
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

Itt most van egy függvényünk, amely visszaad egy funkciólistát. Az eszközök listájának minden eleme most olyan mezőket tartalmaz, mint a `name`, `description` és `inputSchema`, hogy megfeleljen a visszatérési típusnak. Ez lehetővé teszi, hogy az eszközeinket és a funkciódefiníciókat máshol helyezzük el. Most már az összes eszközünket egy tools mappában létrehozhatjuk, és ugyanez vonatkozik minden funkcióra, így a projekted hirtelen így szerveződhet:

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

Ez nagyszerű, az architektúránk egészen tisztának tűnhet.

Mi a helyzet az eszközök hívásával, ugyanaz az ötlet, egy kezelő, ami hívja az eszközt, bármelyik legyen is az? Igen, pontosan, itt van a kód ehhez:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # a tools egy szótár, amelyben az eszközök nevei a kulcsok
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
    // TODO hívd meg az eszközt,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Ahogy a fenti kódból látható, ki kell elemeznünk, hogy melyik eszközt hívjuk meg és milyen argumentumokkal, majd folytatnunk kell az eszköz meghívásával.

## A megközelítés javítása validációval

Eddig azt láttad, hogyan váltható le az összes eszköz-, erőforrás- és promptregisztráció ezekre a típusonként két kezelőre. Mit érdemes még tenni? Például hozzá kell adnunk valamilyen ellenőrzést, hogy biztosítsuk az eszköz helyes argumentumokkal történő meghívását. Minden futtatókörnyezet megoldása eltérő, például Pythonban Pydanticot használunk, TypeScriptben pedig Zodot. A cél az, hogy a következőt tegyük:

- A funkció (eszköz, erőforrás vagy prompt) létrehozásához szükséges logikát a neki dedikált mappába helyezzük.
- Hozzunk létre egy módot az érkező kérés validálására, például amikor eszközt hívunk meg.

### Funkció létrehozása

Egy funkció létrehozásához létre kell hoznunk egy fájlt a funkció számára, és biztosítani kell, hogy meglegyenek a kötelező mezők, amelyek az adott funkcióhoz szükségesek. Ezek a mezők eszközönként, erőforrásonként és promptként kicsit eltérnek.

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
        # Érvényesítsük a bemenetet Pydantic modell segítségével
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adjuk hozzá a Pydantic-et, hogy létrehozhassunk egy AddInputModel-t és érvényesíthessük az argumentumokat

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Itt azt látod, hogy a következőket tesszük:

- Létrehozunk egy sémát Pydantic `AddInputModel` segítségével a *schema.py* fájlban, amely `a` és `b` mezőkkel rendelkezik.
- Megpróbáljuk az érkező kérést beparse-olni `AddInputModel` típusúnak, ha paraméter eltérés van, az le fog állítani minket:

   ```python
   # add.py
    try:
        # Érvényesítse a bemenetet Pydantic modell segítségével
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Dönthetsz, hogy ezt az elemző logikát magában az eszközhívásban vagy a kezelő függvényben helyezed el.

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

- Az összes eszköz hívását kezelő kezelőben most megpróbáljuk beparse-olni az érkező kérést az eszköz által definiált sémára:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Ha ez sikeres, akkor folytatjuk az eszköz tényleges meghívásával:

    ```typescript
    const result = await tool.callback(input);
    ```

Ahogy látható, ez a megközelítés remek architektúrát hoz létre, mert mindennek megvan a helye: a *server.ts* egy nagyon kis fájl, amely csak összekapcsolja a kéréskezelőket, és minden funkció a saját mappájában van, azaz tools/, resources/ vagy prompts/.

Nagyszerű, próbáljuk ezt megépíteni legközelebb.

## Gyakorlat: Alacsony szintű szerver létrehozása

Ebben a gyakorlatban a következőket fogjuk csinálni:

1. Létrehozunk egy alacsony szintű szervert, amely kezeli az eszközök listázását és hívását.
1. Megvalósítunk egy olyan architektúrát, amelyre építhetünk.
1. Hozzáadunk validációt, hogy az eszközhívások megfelelően legyenek ellenőrizve.

### -1- Architektúra létrehozása

Az első, amit meg kell oldanunk, egy olyan architektúra, amely segít a skálázásban, ahogy több funkciót adunk hozzá. Így néz ki:

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

Most beállítottunk egy olyan architektúrát, amely biztosítja, hogy könnyen adhassunk hozzá új eszközöket a tools mappában. Nyugodtan kövesd ezt, hogy erőforrások és promptok számára is alkönyvtárakat adj hozzá.

### -2- Eszköz létrehozása

Nézzük meg, hogyan néz ki egy eszköz létrehozása. Először is létre kell hoznunk az eszközt az *tool* alkönyvtárban így:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Értékeld ki a bemenetet Pydantic modellel
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adjuk hozzá a Pydanticet, hogy létrehozhassunk egy AddInputModelt és érvényesíthessük az argumentumokat

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Itt azt láthatjuk, hogyan definiáljuk a nevet, leírást és a bemeneti sémát Pydantic segítségével, valamint egy kezelőt, amely majd meghíváskor fut le. Végül közzétesszük a `tool_add` változót, ami egy szótár, amely tartalmazza ezeket a tulajdonságokat.

Van egy *schema.py* is, amely definiálja az eszközhöz használt bemeneti sémát:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Továbbá fel kell töltenünk a *__init__.py* fájlt, hogy a tools könyvtár modulként legyen kezelve. Emellett itt tesszük elérhetővé a benne lévő modulokat is:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ehhez az állományhoz továbbra is hozzáadhatsz, ahogy további eszközöket adsz hozzá.

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

Itt egy szótárt hozunk létre a következő tulajdonságokkal:

- name, az eszköz neve.
- rawSchema, ez a Zod séma, amelyet a bejövő eszközhívó kérések érvényesítésére használunk.
- inputSchema, ezt a sémát fogja használni a kezelő.
- callback, ez az eszköz meghívására szolgál.

Van továbbá egy `Tool` típus is, amely ezt a szótárt egy típussá alakítja, amelyet az mcp szerver kezelője elfogad, ez így néz ki:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Létezik még a *schema.ts* fájl is, amely az eszközök bemeneti sémáit tárolja. Jelenleg egy sémát tartalmaz, de ahogy több eszközt adunk hozzá, itt is bővülhetünk:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nagyszerű, haladjunk tovább az eszközök listázásának kezelésére.

### -3- Az eszközlista kezelése

Most az eszközök listázásának kezeléséhez be kell állítanunk egy kérés kezelőt. Ezt kell hozzáadni a szerver fájlhoz:

**Python**

```python
# a kód rövidítve
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

Itt hozzáadjuk a `@server.list_tools` dekorátort és az implementáló `handle_list_tools` függvényt. Ez utóbbiban egy eszközlista létrehozására van szükség. Figyeld meg, hogy minden eszköznek tartalmaznia kell nevét, leírását és inputSchema-ját.

**TypeScript**

Az eszközök listázását kezelő kérés kezelő beállításához a szerveren a `setRequestHandler`-t kell hívni a megfelelő sémával, jelen esetben a `ListToolsRequestSchema`-val.

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
// A kód rövidítve
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // A regisztrált eszközök listájának visszaadása
  return {
    tools: tools
  };
});
```

Nagyszerű, most megoldottuk az eszközök listázását, nézzük meg, hogyan hívhatnánk meg eszközöket.

### -4- Eszköz hívásának kezelése

Az eszközök hívásához újabb kérés kezelőt kell felállítanunk, most olyat, amely az érkező kérésből kibogozza, hogy melyik funkciót kell hívni és milyen argumentumokkal.

**Python**

Használjuk a `@server.call_tool` dekorátort és implementáljuk a `handle_call_tool` függvényben. Ebben ki kell parsolnunk az eszköz nevét, argumentumait és ellenőriznünk kell, hogy az argumentumok érvényesek-e az adott eszközhöz. Ez az ellenőrzés történhet itt vagy lenn az eszközben.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # a tools egy szótár, amelyben az eszközök nevei a kulcsok
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # hívja meg az eszközt
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ez történik:

- Az eszköz neve már jelen van `name` bemeneti paraméterként, az argumentumok pedig `arguments` szótárként vannak megadva.

- Az eszköz meghívása így történik: `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Az argumentumok validálása a `handler` tulajdonságban történik, amely egy függvényre mutat; ha az érvénytelen, kivételt dob.

Most már teljes képet kaptunk az eszközök listázásáról és meghívásáról alacsony szintű szerver használatával.

A [teljes példát](./code/README.md) itt találod

## Feladat

Bővítsd a megkapott kódot számos eszközzel, erőforrással és prompttal, majd gondolkodj el azon, hogy észreveszed, hogy csak a tools könyvtárba kell fájlokat hozzáadnod, máshova nem.

*Nincs megoldás mellékelve*

## Összefoglaló

Ebben a fejezetben megnéztük, hogyan működik az alacsony szintű szerver megközelítés, és hogyan segít egy jó architektúra kialakításában, amelyre tovább építhetünk. Beszéltünk a validációról is, és megmutattuk, hogyan dolgozhatsz validációs könyvtárakkal, hogy sémákat hozz létre a bemeneti adatok ellenőrzésére.

## Mi jön ezután

- Következő: [Egyszerű hitelesítés](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. A dokumentum eredeti nyelvű változata tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
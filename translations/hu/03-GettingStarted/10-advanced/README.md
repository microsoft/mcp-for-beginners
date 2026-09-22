# Haladó szerverhasználat

Az MCP SDK-ban kétféle szerver érhető el, a normál szerver és az alacsony szintű szerver. Általában a normál szervert használjuk, hogy funkciókat adjunk hozzá. Bizonyos esetekben viszont inkább az alacsony szintű szerverre szeretnénk támaszkodni, például:

- Jobb architektúra. Lehetséges tiszta architektúrát létrehozni mind a normál, mind az alacsony szintű szerverrel, de vitatható, hogy az alacsony szintű szerverrel ez kicsit egyszerűbb.
- Funkcióelérhetőség. Néhány fejlett funkció csak alacsony szintű szerverrel használható,
    például a későbbi fejezetekben tárgyalt Elicitation és a régi Sampling
    funkció, amely az MCP `2026-07-28` verzióban elavult.

## Normál szerver vs alacsony szintű szerver

Íme, így néz ki egy MCP Szerver létrehozása a normál szerverrel

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

A lényeg az, hogy kifejezetten hozzáadod az összes eszközt, erőforrást vagy promptot, amit a szervernek tudnia kell. Ebben nincs semmi rossz.  

### Alacsony szintű szerver megközelítés

Azonban, amikor az alacsony szintű szerver megközelítést használod, másként kell rá gondolni. Ahelyett, hogy minden eszközt regisztrálnánk, inkább két kezelőt hozunk létre funkciótípusonként (eszközök, erőforrások vagy promptok). Például az eszközök esetén akkor csak két függvény van:

- Az összes eszköz felsorolása. Egy függvény felel minden eszközök listázási próbálkozásért.
- Az eszközök meghívásának kezelése. Itt is csak egy függvény kezeli az eszköz meghívásokat.

Ez potenciálisan kevesebb munkának tűnik, igaz? Szóval eszköz regisztrálás helyett csak biztosítanunk kell, hogy az eszköz szerepeljen az eszközök listájában és hogy hívás esetén meghívásra kerüljön.

Nézzük akkor, hogyan néz ki most a kód:

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
  // Visszaadja a regisztrált eszközök listáját
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

Itt most van egy függvényünk, ami visszaad egy funkciók listáját. Az eszközök listájának minden bejegyzése most olyan mezőkkel rendelkezik, mint `name`, `description` és `inputSchema`, hogy megfeleljen a visszatérési típusnak. Ez lehetővé teszi, hogy az eszközöket és funkciódefiníciókat máshol tartsuk. Most már létrehozhatjuk az összes eszközünket egy tools mappában, és ugyanez érvényes az összes funkcióra is, így a projekted hirtelen így nézhet ki:

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

Ez nagyszerű, az architektúránk elég tisztának nézhet ki.

Mi van az eszközök meghívásával, ugyanaz az elv, egy kezelő az összes eszköz meghívására? Igen, pontosan, itt van a hozzá tartozó kód:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # a tools egy szótár, amelyben az eszköznevek a kulcsok
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
    
    // argumentumok: request.params.arguments
    // FELADAT: hívja meg az eszközt,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Ahogy a fenti kódból látható, ki kell értékelnünk, melyik eszközt kell meghívni, milyen argumentumokkal, majd meg kell hívnunk az adott eszközt.

## A megközelítés javítása validálással

Eddig láttad, hogyan helyettesíthetők az összes eszköz, erőforrás és prompt regisztrációi ezekkel a két kezelővel funkciótípusonként. Mit kell még tennünk? Nos, valamilyen validálást kell hozzáadnunk, hogy biztosítsuk, hogy az eszközök helyesen legyenek meghívva helyes argumentumokkal. Minden futtatókörnyezetnek megvan a maga megoldása erre, például a Python Pydantic-et, a TypeScript pedig Zod-ot használ. A koncepció a következő:

- Áthelyezzük a funkció (eszköz, erőforrás vagy prompt) létrehozásának logikáját az adott dedikált mappájába.
- Hozzáadunk egy módot az bejövő kérés validálására, például eszköz meghívásra.

### Funkció létrehozása

Funkció létrehozásához létre kell hoznunk egy fájlt az adott funkcióhoz, és biztosítani kell, hogy az tartalmazza a kötelező mezőket. Ezek a mezők kicsit eltérnek eszközök, erőforrások és promptok esetén.

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
        # Érvényesítse a bemenetet Pydantic modell segítségével
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: adjuk hozzá a Pydantic-et, hogy létrehozhassunk egy AddInputModelt és érvényesíthessük az argumentumokat

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Itt látható, hogy a következőket csináljuk:

- Létrehozunk egy sémát Pydantic `AddInputModel` néven, mezőkkel `a` és `b` a *schema.py* fájlban.
- Megpróbáljuk kiértékelni a bejövő kérést `AddInputModel` típusúra, ha nem egyeznek az argumentumok, a program hibát dob:

   ```python
   # add.py
    try:
        # A bemenet ellenőrzése Pydantic modell használatával
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Döntheted el, hogy ezt az kiértékelési logikát az eszköz hívásánál vagy a kezelő függvényben helyezed el.

**TypeScript**

```typescript
// szerver.ts
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

// séma.ts
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });

// hozzáad.ts
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

- Az összes eszköz hívását kezelő handlerben most megpróbáljuk kiértékelni a bejövő kérést az eszköz által definiált séma szerint:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ha ez sikerül, folytatjuk az adott eszköz meghívásával:

    ```typescript
    const result = await tool.callback(input);
    ```

Ahogy látható, ez a megközelítés nagyszerű architektúrát eredményez, mivel mindennek megvan a helye; a *server.ts* egy nagyon kis méretű fájl, amely csak az összekötő kéréskezelőket tartalmazza, és minden funkció a saját mappájában van, azaz tools/, resources/ vagy prompts/.

Nagyszerű, nézzük meg, hogyan építhetjük ezt fel.

## Gyakorlat: Alacsony szintű szerver létrehozása

Ebben a gyakorlatban a következőket fogjuk tenni:

1. Létrehozunk egy alacsony szintű szervert, amely kezeli az eszközök listázását és meghívását.
1. Megvalósítunk egy architektúrát, amelyre építkezhetünk.
1. Validálást adunk hozzá, hogy biztos legyen, hogy eszköz hívásaink megfelelően vannak ellenőrizve.

### -1- Architektúra létrehozása

Az első dolog, amit meg kell oldanunk, egy olyan architektúra, amely segít skálázódni, ahogy több funkciót adunk hozzá, így néz ki:

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

Most létrehoztunk egy architektúrát, amely biztosítja, hogy könnyen hozzáadhatunk új eszközöket a tools mappába. Nyugodtan kövesd ezt az erőforrások és promptok mappáinak al-mappákkal való bővítéséhez is.

### -2- Eszköz létrehozása

Nézzük meg, hogyan néz ki egy eszköz létrehozása. Először ki kell hoznunk a *tool* alkönyvtárban így:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Érvényesítse a bemenetet Pydantic model segítségével
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

Itt látható, hogyan definiáljuk a nevet, a leírást és a bemeneti sémát Pydantic segítségével, valamint egy kezelőt, amely meghíváskor fut le. Végül kitetjük a `tool_add`-ot, amely egy szótár, ami ezeket a tulajdonságokat tartalmazza.

Van még egy *schema.py* is, amely a toolunk bemeneti sémáját definiálja:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Ki kell töltenünk az *__init__.py* fájlt is, hogy biztosítsuk, hogy a tools könyvtár modulnak számítson. Emellett ezen belül kitenni is kell a modulokat így:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ebben a fájlban folyamatosan bővíthetjük az eszközök számával.

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

Itt egy szótárat hozunk létre, amely tartalmazza a tulajdonságokat:

- name, ez az eszköz neve.
- rawSchema, ez a Zod séma, amelyet a bejövő eszköz hívások ellenőrzésére használunk.
- inputSchema, ezt a sémát használja a kezelő.
- callback, ezzel hívjuk meg az eszközt.

Van egy `Tool` típus is, amivel ezt a szótárat olyan típussá konvertáljuk, amit az mcp szerver kezelője elfogad, így néz ki:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Van egy *schema.ts* fájlunk, ahol az egyes eszközök bemeneti sémáit tároljuk, így néz ki egy séma egyelőre csak egy eszközhöz, de ahogy több eszközt adunk hozzá, bővíthetjük:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nagyszerű, folytassuk az eszközlista kezelésével.

### -3- Eszközök listázásának kezelése

Az eszközök listájának kezeléséhez be kell állítanunk egy kéréskezelőt. Ezt kell hozzáadnunk a szerver fájlhoz:

**Python**

```python
# a kód a terjedelem miatt el lett hagyva
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

Itt hozzáadjuk a `@server.list_tools` dekorátort és az implementáló függvényt `handle_list_tools` néven. Ebben egy eszközlista létrehozása szükséges. Figyeld meg, hogy minden eszköznek legyen neve, leírása és inputSchema-ja.   

**TypeScript**

Az eszközök listázásához a szerveren be kell állítanunk a `setRequestHandler`-t egy olyan sémával, ami illeszkedik a tevékenységhez, jelen esetben `ListToolsRequestSchema`.

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
// a kód rövidítve
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Visszaadja a regisztrált eszközök listáját
  return {
    tools: tools
  };
});
```

Nagyszerű, megoldottuk az eszközök listázását, nézzük meg, hogy hogyan hívhatjuk meg őket.

### -4- Eszköz meghívásának kezelése

Egy másik kéréskezelőt kell beállítanunk az eszköz meghívásához, amely kezeli a kérés azon paramétereit, hogy melyik funkciót hívjuk meg, és milyen argumentumokkal.

**Python**

Használjuk a `@server.call_tool` dekorátort és implementáljuk egy `handle_call_tool` nevű függvénnyel. Ebben a függvényben ki kell olvasnunk az eszköz nevét és annak argumentumait, és ellenőriznünk kell, hogy az argumentumok érvényesek-e az adott eszközhöz. Az argumentumokat itt vagy az eszközben magában lehet validálni.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # a tools egy szótár, amiben az eszközök nevei a kulcsok
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # az eszköz meghívása
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Ez történik itt:

- Az eszköz neve már megvan az input paraméterként `name`-ként, és az argumentumok szintén a `arguments` szótárban vannak.

- Az eszköz meghívása `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` módon történik. Az argumentumok validálása a `handler` tulajdonságban lévő függvényben történik, ha sikertelen, kivételt dob.

Így most teljesen értjük, hogyan működik az eszközök listázása és meghívása alacsony szintű szerverrel.

Lásd a [teljes példát](./code/README.md) itt

## Feladat

Bővítsd a megadott kódot több eszközzel, erőforrással és prompttal, és gondolkodj el rajta, hogyan kell csak fájlokat hozzáadnod a tools könyvtárban, máshol nem.

*Megoldás nincs megadva*

## Összefoglalás

Ebben a fejezetben megismertük az alacsony szintű szerver megközelítését, és hogy ez hogyan segít egy jól szervezett architektúra létrehozásában, amelyre tovább építhetünk. Megbeszéltük a validálást, és bemutattuk, hogyan dolgozhatsz validáló könyvtárakkal input sémák létrehozásához.

## Mi következik

- Következő: [Egyszerű hitelesítés](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
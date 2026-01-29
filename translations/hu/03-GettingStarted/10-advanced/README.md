# Haladó szerverhasználat

Az MCP SDK kétféle szervert kínál: a normál szervert és az alacsony szintű szervert. Általában a normál szervert használjuk funkciók hozzáadására. Bizonyos esetekben azonban az alacsony szintű szerverre van szükség, például:

- Jobb architektúra. Bár tiszta architektúrát lehet létrehozni mind a normál, mind az alacsony szintű szerverrel, vitatható, hogy az alacsony szintű szerverrel ez valamivel egyszerűbb.
- Funkcióelérhetőség. Néhány fejlett funkció csak alacsony szintű szerverrel érhető el. Ezt későbbi fejezetekben fogjuk látni, amikor mintavételezést és adatgyűjtést adunk hozzá.

## Normál szerver vs alacsony szintű szerver

Így néz ki egy MCP szerver létrehozása normál szerverrel:

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

A lényeg az, hogy kifejezetten hozzáadjuk azokat az eszközöket, erőforrásokat vagy promptokat, amelyeket a szervernek tartalmaznia kell. Ezzel semmi probléma nincs.  

### Alacsony szintű szerver megközelítés

Az alacsony szintű szerver használatakor azonban másképp kell gondolkodni. Ahelyett, hogy minden eszközt regisztrálnánk, két kezelőt hozunk létre funkciótípusonként (eszközök, erőforrások vagy promptok). Például az eszközök esetében csak két funkció van:

- Az összes eszköz listázása. Egy funkció felelős az összes eszköz listázási kísérletéért.
- Az összes eszköz hívásának kezelése. Itt is csak egy funkció kezeli az eszközök hívásait.

Ez kevesebb munkának tűnik, igaz? Tehát ahelyett, hogy regisztrálnék egy eszközt, csak arról kell gondoskodnom, hogy az eszköz szerepeljen a listában, amikor az összes eszközt listázom, és hogy hívható legyen, amikor bejövő kérés érkezik az eszköz hívására.

Nézzük meg, hogyan néz ki most a kód:

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

Itt most van egy funkciónk, amely visszaadja a funkciók listáját. Az eszközök listájának minden bejegyzése olyan mezőket tartalmaz, mint `name`, `description` és `inputSchema`, hogy megfeleljen a visszatérési típusnak. Ez lehetővé teszi, hogy az eszközöket és a funkciódefiníciókat máshol helyezzük el. Most már létrehozhatjuk az összes eszközt egy eszközök mappában, és ugyanez vonatkozik az összes funkcióra, így a projekt hirtelen így szervezhető:

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

Ez nagyszerű, az architektúránk elég tiszta lehet.

Mi a helyzet az eszközök hívásával? Ugyanaz az ötlet, egy kezelő az eszköz hívására, bármelyik eszközre? Igen, pontosan, itt van a kód erre:

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

Ahogy a fenti kódból látható, ki kell elemezni, hogy melyik eszközt kell hívni, milyen argumentumokkal, majd folytatni kell az eszköz hívását.

## A megközelítés javítása validációval

Eddig láttuk, hogyan lehet az eszközök, erőforrások és promptok hozzáadását helyettesíteni ezekkel a két kezelővel funkciótípusonként. Mi mást kell még tennünk? Nos, valamilyen validációt kell hozzáadnunk, hogy biztosítsuk, hogy az eszközt megfelelő argumentumokkal hívják meg. Minden futtatókörnyezetnek megvan a saját megoldása erre, például Pythonban a Pydantic, TypeScriptben pedig a Zod. Az ötlet a következő:

- A funkció (eszköz, erőforrás vagy prompt) létrehozásának logikáját áthelyezzük a dedikált mappájába.
- Hozzáadunk egy módot a bejövő kérés validálására, amely például egy eszköz hívását kéri.

### Funkció létrehozása

Egy funkció létrehozásához létre kell hoznunk egy fájlt az adott funkcióhoz, és gondoskodnunk kell arról, hogy tartalmazza az adott funkció kötelező mezőit. Ezek a mezők eszközök, erőforrások és promptok esetében kissé eltérnek.

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

Itt látható, hogyan tesszük a következőket:

- Létrehozunk egy sémát a Pydantic `AddInputModel` segítségével, amely mezőket tartalmaz, például `a` és `b` a *schema.py* fájlban.
- Megpróbáljuk a bejövő kérést `AddInputModel` típusúvá alakítani, ha a paraméterek nem egyeznek, akkor ez hibát okoz:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Eldönthetjük, hogy ezt az elemzési logikát magában az eszköz hívásában vagy a kezelő funkcióban helyezzük el.

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

- Az összes eszköz hívásával foglalkozó kezelőben megpróbáljuk a bejövő kérést az eszköz által definiált sémára alakítani:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ha ez sikerül, akkor folytatjuk az eszköz tényleges hívását:

    ```typescript
    const result = await tool.callback(input);
    ```

Ahogy látható, ez a megközelítés nagyszerű architektúrát hoz létre, mivel minden a helyén van, a *server.ts* egy nagyon kicsi fájl, amely csak a kéréskezelőket kapcsolja össze, és minden funkció a saját mappájában van, például tools/, resources/ vagy /prompts.

Nagyszerű, próbáljuk meg ezt felépíteni.

## Gyakorlat: Alacsony szintű szerver létrehozása

Ebben a gyakorlatban a következőket fogjuk tenni:

1. Hozzunk létre egy alacsony szintű szervert, amely kezeli az eszközök listázását és hívását.
1. Valósítsunk meg egy architektúrát, amelyre építhetünk.
1. Adjunk hozzá validációt, hogy biztosítsuk az eszköz hívások megfelelő validálását.

### -1- Architektúra létrehozása

Először egy olyan architektúrát kell létrehoznunk, amely segít a skálázásban, ahogy több funkciót adunk hozzá. Így néz ki:

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

Most már van egy architektúránk, amely biztosítja, hogy könnyen hozzáadhassunk új eszközöket egy eszközök mappában. Nyugodtan kövesse ezt, hogy alkönyvtárakat adjon hozzá erőforrásokhoz és promptokhoz.

### -2- Eszköz létrehozása

Nézzük meg, hogyan néz ki egy eszköz létrehozása. Először az eszközt a *tool* alkönyvtárban kell létrehozni, így:

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

Itt látható, hogyan definiáljuk a nevet, leírást, egy bemeneti sémát a Pydantic segítségével, és egy kezelőt, amelyet akkor hívunk meg, amikor ezt az eszközt hívják. Végül kiteszünk egy `tool_add` nevű szótárat, amely tartalmazza ezeket a tulajdonságokat.

Van egy *schema.py* fájl is, amelyet az eszköz által használt bemeneti séma definiálására használunk:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Ezenkívül ki kell töltenünk a *__init__.py* fájlt, hogy biztosítsuk, hogy az eszközök könyvtár modulként legyen kezelve. Továbbá ki kell tennünk a benne lévő modulokat, így:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ezt a fájlt folyamatosan bővíthetjük, ahogy új eszközöket adunk hozzá.

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

Itt egy szótárat hozunk létre, amely a következő tulajdonságokat tartalmazza:

- name, ez az eszköz neve.
- rawSchema, ez a Zod séma, amelyet a bejövő kérések validálására használunk.
- inputSchema, ezt a sémát a kezelő használja.
- callback, ezt az eszköz meghívására használjuk.

Van egy `Tool`, amelyet arra használunk, hogy ezt a szótárat olyan típusra alakítsuk, amelyet az MCP szerver kezelője elfogad, és így néz ki:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Van egy *schema.ts* fájl is, ahol az egyes eszközök bemeneti sémáit tároljuk. Jelenleg csak egy séma van benne, de ahogy új eszközöket adunk hozzá, több bejegyzést is hozzáadhatunk:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nagyszerű, folytassuk az eszközök listázásának kezelésével.

### -3- Eszközök listázásának kezelése

Az eszközök listázásának kezeléséhez be kell állítanunk egy kéréskezelőt erre. Íme, mit kell hozzáadnunk a szerver fájlhoz:

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

Itt hozzáadjuk a `@server.list_tools` dekorátort és az implementáló `handle_list_tools` funkciót. Az utóbbiban elő kell állítanunk az eszközök listáját. Figyeljük meg, hogy minden eszköznek rendelkeznie kell névvel, leírással és inputSchema-val.   

**TypeScript**

Az eszközök listázására szolgáló kéréskezelő beállításához a szerveren a `setRequestHandler` függvényt kell hívnunk egy olyan sémával, amely megfelel annak, amit próbálunk tenni, ebben az esetben a `ListToolsRequestSchema`-val.

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

Nagyszerű, most megoldottuk az eszközök listázásának problémáját, nézzük meg, hogyan lehet eszközöket hívni.

### -4- Eszköz hívásának kezelése

Egy eszköz hívásához egy másik kéréskezelőt kell beállítanunk, amely ezúttal arra összpontosít, hogy kezelje a kérésben megadott funkciót és annak argumentumait.

**Python**

Használjuk a `@server.call_tool` dekorátort, és valósítsuk meg egy olyan funkcióval, mint a `handle_call_tool`. Ebben a funkcióban ki kell elemeznünk az eszköz nevét, annak argumentumait, és biztosítanunk kell, hogy az argumentumok érvényesek legyenek az adott eszköz számára. Az argumentumokat vagy ebben a funkcióban, vagy az eszközben validálhatjuk.

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

Itt történik a következő:

- Az eszköz neve már jelen van bemeneti paraméterként `name`, ami igaz az argumentumokra is az `arguments` szótár formájában.

- Az eszközt a `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` segítségével hívjuk meg. Az argumentumok validálása a `handler` tulajdonságban történik, amely egy funkcióra mutat, ha ez nem sikerül, kivételt dob. 

Most már teljes megértésünk van az eszközök listázásáról és hívásáról alacsony szintű szerver használatával.

Lásd a [teljes példát](./code/README.md) itt.

## Feladat

Egészítse ki a kapott kódot több eszközzel, erőforrással és prompttal, és gondolja át, hogyan veszi észre, hogy csak az eszközök könyvtárában kell fájlokat hozzáadnia, máshol nem. 

*Nincs megoldás megadva*

## Összefoglalás

Ebben a fejezetben láttuk, hogyan működik az alacsony szintű szerver megközelítés, és hogyan segíthet ez egy jól felépíthető architektúra létrehozásában. Megbeszéltük a validációt is, és bemutattuk, hogyan lehet validációs könyvtárakkal dolgozni bemeneti validációs sémák létrehozásához.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
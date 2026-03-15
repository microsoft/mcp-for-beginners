# Fejlett szerverhasználat

Az MCP SDK két különböző típusú szervert tartalmaz, a normál szervert és az alacsony szintű szervert. Normál esetben a normál szervert használod, hogy funkciókat adj hozzá. Bizonyos esetekben azonban az alacsony szintű szerverre támaszkodnál, például:

- Jobb architektúra. Lehet tiszta architektúrát létrehozni mind a normál, mind az alacsony szintű szerverrel, de elmondható, hogy az alacsony szintű szerverrel ez némileg könnyebb.
- Funkció elérhetősége. Egyes fejlett funkciókat csak az alacsony szintű szerverrel lehet használni. Ez későbbi fejezetekben is látható lesz, amikor mintavételt és kiváltást adunk hozzá.

## Normál szerver vs alacsony szintű szerver

Így néz ki az MCP szerver létrehozása a normál szerverrel

**Python**

```python
mcp = FastMCP("Demo")

# Adjon hozzá egy összeadási eszközt
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

// Adj hozzá egy összeadó eszközt
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

A lényeg, hogy explicit módon hozzáadsz minden eszközt, erőforrást vagy promptot, amivel a szervernek rendelkeznie kell. Ebben nincs semmi hiba.

### Alacsony szintű szerver megközelítés

Azonban, amikor az alacsony szintű szerver megközelítést használod, másképp kell gondolkodnod. Ahelyett, hogy minden eszközt regisztrálnál, inkább két kezelőt hozol létre minden funkció típushoz (eszközök, erőforrások vagy promptok). Például az eszközöknél így csak két funkció van:

- Az összes eszköz listázása. Egy funkciónak kell kezelnie minden eszközlistázási próbálkozást.
- Az eszközök hívásának kezelése. Itt is csak egy funkció kezel minden eszköz hívást.

Ez potenciálisan kevesebb munkának tűnik, igaz? Tehát ahelyett, hogy regisztrálok egy eszközt, csak biztosítanom kell, hogy az eszköz benne legyen az eszközök listájában és hogy hívás esetén az el legyen indítva.

Nézzük meg hogyan néz ki a kód most:

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

Itt most van egy funkciónk, ami visszaadja az elérhető funkciók listáját. Az eszközök listájának minden elemében most vannak olyan mezők, mint a `name`, `description`, és `inputSchema`, hogy megfeleljenek a visszatérési típusnak. Ez lehetővé teszi, hogy az eszközeinket és funkció definícióinkat máshol tartsuk. Most már létrehozhatod az összes eszközt egy tools mappában, és ugyanez vonatkozik minden funkcióra, így a projekted hirtelen így nézhet ki:

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

Ez nagyszerű, az architektúránk elég tisztának tűnhet.

Akkor az eszközök hívásánál is ugyanaz az ötlet, egy kezelő hív minden eszközt? Igen, pontosan, itt a kód erre:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # a tools egy szótár, ahol az eszköznevek a kulcsok
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
    // TODO hívja meg az eszközt,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Ahogy a fenti kódból látható, ki kell szednünk, melyik eszközt hívjuk, milyen argumentumokkal, majd ezt követően meghívjuk az eszközt.

## Megközelítés fejlesztése validációval

Eddig láttad, hogyan válthatod le az összes regisztrációdat eszközök, erőforrások és promptok hozzáadásához ezekre a két kezelőre minden funkció típusra. Mit kell még tennünk? Nos, valamilyen validációt kell hozzáadnunk, hogy biztosítsuk, hogy az eszközt a megfelelő argumentumokkal hívják meg. Minden futtatókörnyezet saját megoldást használ erre, például a Python a Pydantic-et, a TypeScript pedig a Zod-ot. A koncepció a következő:

- Az adott funkció (eszköz, erőforrás vagy prompt) létrehozásának logikáját áthelyezni a dedikált mappájába.
- Hozzáadni egy módot a bejövő kérés validálására, amely például egy eszköz meghívását kéri.

### Funkció létrehozása

Funkció létrehozásához szükséges egy fájlt készíteni az adott funkcióhoz, és biztosítani, hogy a kötelező mezőket tartalmazza, amelyek kissé eltérnek az eszközök, erőforrások és promptok esetében.

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
        # A bemenet érvényesítése Pydantic modellel
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

Itt látható, hogyan csináljuk a következőt:

- Létrehozunk egy séma típust Pydantic `AddInputModel` néven, amely mezőket `a` és `b` tartalmaz, a *schema.py* fájlban.
- Megpróbáljuk beolvasni a bejövő kérést `AddInputModel` típusként, ha az argumentumok nem egyeznek, akkor a folyamat leáll:

   ```python
   # add.py
    try:
        # Érvényesítse a bemenetet Pydantic modell segítségével
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Dönthetsz, hogy ezt az elemző logikát magában az eszköz hívásában vagy a kezelő funkcióban helyezed el.

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

- Az összes eszköz hívását kezelő funkciónál most megpróbáljuk a bejövő kérést a megfelelő eszköz által definiált sémára parse-olni:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ha ez sikerül, akkor folytatjuk az eszköz tényleges meghívását:

    ```typescript
    const result = await tool.callback(input);
    ```

Ahogy látható, ez a megközelítés nagyszerű architektúrát hoz létre, mert mindennek megvan a helye, a *server.ts* egy nagyon kicsi fájl, amely csak összeköti a kérés kezelőket, és minden funkció a maga mappájában van, azaz tools/, resources/ vagy prompts/ mappákban.

Nagyszerű, próbáljuk meg ezt legközelebb megépíteni.

## Gyakorlat: Alacsony szintű szerver létrehozása

Ebben a gyakorlatban a következőket fogjuk tenni:

1. Létrehozunk egy alacsony szintű szervert, amely kezeli az eszközök listázását és meghívását.
1. Megvalósítunk egy olyan architektúrát, amelyre építhetsz.
1. Hozzáadunk validációt, hogy biztosítsuk az eszköz hívások helyes validálását.

### -1- Architektúra létrehozása

Az első dolog, amit meg kell oldanunk, egy olyan architektúra létrehozása, amely lehetővé teszi a bővítést további funkciókkal. Így néz ki:

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

Most beállítottunk egy olyan architektúrát, amely biztosítja, hogy könnyen hozzáadhass új eszközöket a tools mappában. Nyugodtan kövesd ezt, hogy al-mappákat hozz létre az erőforrások és promptok számára.

### -2- Eszköz létrehozása

Nézzük meg, hogyan néz ki egy eszköz létrehozása. Elsőként az eszközt a saját *tool* almappájában kell létrehozni így:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Érvényesítse a bemenetet Pydantic modellel
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

Itt látható, hogyan definiáljuk a nevet, leírást és a bemeneti sémát a Pydantic segítségével, valamint egy kezelőt, ami akkor hívódik meg, amikor az eszközt meghívják. Végül kiteszünk egy `tool_add` nevű szótárat, amely tartalmazza ezeket a tulajdonságokat.

Van még a *schema.py* fájl, amely definiálja az eszköz által használt bemeneti sémát:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Meg kell töltenünk a *__init__.py* fájlt is, hogy a tools könyvtár modulnak számítson. Ezen túlmenően meg kell osztanunk a benne lévő modulokat így:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Ehhez a fájlhoz hozzáadhatunk újabb eszközöket, ahogy szükséges.

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

Itt létrehozunk egy szótárt, amely a következő tulajdonságokat tartalmazza:

- name, az eszköz neve.
- rawSchema, ez a Zod séma, amely használatban lesz a bejövő kérések validálására, amelyek ezt az eszközt hívják.
- inputSchema, ezt a sémát a kezelő használja.
- callback, ez az eszköz meghívására szolgál.

Van egy `Tool` is, amely ezt a szótárt átalakítja egy olyan típussá, amelyet az mcp szerver kezelő elfogad, és így néz ki:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Van még egy *schema.ts* fájl, ahol minden eszköz beviteli sémáját tároljuk, jelenleg csak egy sémával, de ahogy további eszközöket adunk hozzá, több bejegyzést is elhelyezhetünk:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Nagyszerű, folytassuk az eszközök listázásának kezelésével.

### -3- Eszközlista kezelése

Az eszközök listázásának kezeléséhez kérés kezelőt kell beállítanunk. Íme, mit kell hozzáadnunk a szerver fájlunkhoz:

**Python**

```python
# a kód egyszerűsítve
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

Itt hozzáadjuk a `@server.list_tools` dekorátort és a megvalósító `handle_list_tools` függvényt. Ebben előállítunk egy eszközök listáját. Figyeld meg, hogy minden eszköznek van `name`, `description` és `inputSchema` mezője.

**TypeScript**

Az eszközök listázását kezelő kéréskezelő beállításához a szerveren hívni kell a `setRequestHandler` metódust, amelynek egy sémát adunk meg, ami illik a feladathoz, jelen esetben a `ListToolsRequestSchema`-t.

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

Nagyszerű, most megoldottuk az eszközök listázását, nézzük meg, hogyan hívhatjuk meg az eszközöket.

### -4- Eszköz meghívás kezelése

Az eszköz meghívásához egy újabb kéréskezelőt kell beállítanunk, amely olyan kéréseket kezel, amelyek megadják, melyik funkciót (eszközt) kell hívni és milyen argumentumokkal.

**Python**

Használjuk a `@server.call_tool` dekorátort, és valósítsuk meg egy függvénnyel, például `handle_call_tool`-lal. Ebben a függvényben ki kell olvasnunk az eszköz nevét, az argumentumait, és ellenőriznünk kell, hogy az argumentumok érvényesek-e az adott eszköz számára. Ez a validáció történhet itt vagy később, magában az eszközben is.

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

Itt történik:

- Az eszköz neve már az input paraméter `name` formájában van, az argumentumok pedig a `arguments` szótárban.
- Az eszköz meghívása `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` formában történik. Az argumentumok validációja a `handler` tulajdonságban történik, amely egy függvényt hív meg; ha ez nem sikerül, kivételt dob.

Ennyi, most már teljes képet kaptunk arról, hogyan lehet listázni és meghívni az eszközöket egy alacsony szintű szerverrel.

Lásd a [teljes példát](./code/README.md) itt

## Feladat

Bővítsd a kapott kódot több eszközzel, erőforrással és prompttal, és gondold át, hogy mennyire csak a tools könyvtárba kell új fájlokat hozzáadnod, máshova nem.

*Megoldás nincs megadva*

## Összefoglaló

Ebben a fejezetben megnéztük, hogyan működik az alacsony szintű szerver megközelítés, és hogyan segíthet egy tiszta architektúra kialakításában, amelyre építhetünk tovább. Megbeszéltük a validációt, és bemutattuk, hogyan használhatók validációs könyvtárak sémák létrehozására a bemenetek validálásához.

## Mi következik

- Következő: [Egyszerű hitelesítés](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális, emberi fordítás igénybevétele javasolt. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
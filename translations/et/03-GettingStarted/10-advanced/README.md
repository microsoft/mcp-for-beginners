# Täiustatud serveri kasutamine

MCP SDK-s on kaks erinevat tüüpi servereid: tavaline server ja madala taseme server. Tavaliselt kasutatakse tavalist serverit funktsioonide lisamiseks. Kuid mõnel juhul võib olla kasulik tugineda madala taseme serverile, näiteks:

- Parem arhitektuur. Kuigi puhta arhitektuuri loomine on võimalik nii tavalise kui ka madala taseme serveriga, võib väita, et madala taseme serveriga on see veidi lihtsam.
- Funktsioonide kättesaadavus. Mõned täiustatud funktsioonid on saadaval ainult madala taseme serveriga. Näete seda hilisemates peatükkides, kui lisame proovivõtmise ja küsimuste esitamise.

## Tavaline server vs madala taseme server

Siin on näide MCP serveri loomisest tavalise serveriga:

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

Põhimõte on see, et lisate selgesõnaliselt iga tööriista, ressursi või küsimuse, mida soovite serveris kasutada. See on täiesti okei.

### Madala taseme serveri lähenemine

Kui kasutate madala taseme serveri lähenemist, peate mõtlema veidi teisiti. Selle asemel, et registreerida iga tööriist, loote iga funktsiooni tüübi (tööriistad, ressursid või küsimused) jaoks kaks käsitlejat. Näiteks tööriistade puhul on ainult kaks funktsiooni:

- Kõigi tööriistade loetlemine. Üks funktsioon vastutab kõigi tööriistade loetlemise katsete eest.
- Kõigi tööriistade kasutamise käsitlemine. Siin on samuti ainult üks funktsioon, mis käsitleb tööriista kasutamise taotlusi.

See kõlab nagu vähem tööd, eks? Selle asemel, et registreerida tööriist, pean lihtsalt tagama, et tööriist oleks loetletud, kui loetletakse kõik tööriistad, ja et seda kutsutakse, kui saabub taotlus tööriista kasutamiseks.

Vaatame, kuidas kood nüüd välja näeb:

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

Siin on meil funktsioon, mis tagastab funktsioonide loendi. Iga kirje tööriistade loendis sisaldab välju nagu `name`, `description` ja `inputSchema`, et vastata tagastustüübile. See võimaldab meil paigutada oma tööriistad ja funktsioonide määratlused mujale. Nüüd saame luua kõik oma tööriistad eraldi kausta ja sama kehtib ka kõigi funktsioonide kohta, nii et projekt võib olla organiseeritud järgmiselt:

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

See on suurepärane, meie arhitektuur võib olla üsna puhas.

Aga tööriistade kasutamine, kas see on sama idee – üks käsitleja tööriista kasutamiseks, ükskõik millist tööriista? Jah, täpselt, siin on selle koodi näide:

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

Nagu ülaltoodud koodist näha, peame välja selgitama, millist tööriista kasutada ja milliste argumentidega, ning seejärel jätkama tööriista kasutamist.

## Lähenemise täiustamine valideerimisega

Siiani olete näinud, kuidas kõik tööriistade, ressursside ja küsimuste lisamise registreerimised saab asendada nende kahe käsitlejaga iga funktsiooni tüübi jaoks. Mida veel peaksime tegema? Peaksime lisama mingi valideerimise, et tagada tööriista kasutamine õige argumentidega. Igal käitusajal on oma lahendus selleks, näiteks Python kasutab Pydanticut ja TypeScript Zodi. Idee on järgmine:

- Viia funktsiooni (tööriista, ressursi või küsimuse) loomise loogika selle pühendatud kausta.
- Lisada viis sissetuleva taotluse valideerimiseks, näiteks tööriista kasutamise taotluse puhul.

### Funktsiooni loomine

Funktsiooni loomiseks peame looma selle funktsiooni jaoks faili ja tagama, et see sisaldab kohustuslikke välju, mis on vajalikud selle funktsiooni jaoks. Kohustuslikud väljad erinevad tööriistade, ressursside ja küsimuste puhul.

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

Siin näete, kuidas me teeme järgmist:

- Loome skeemi, kasutades Pydanticut `AddInputModel` väljadega `a` ja `b` failis *schema.py*.
- Püüame sissetulevat taotlust parsida tüübiks `AddInputModel`. Kui parameetrites on lahknevus, siis see ebaõnnestub:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Saate valida, kas panna see parsimisloogika tööriista kasutamise funktsiooni või käsitleja funktsiooni.

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

- Käsitlejas, mis tegeleb kõigi tööriistade kasutamisega, püüame parsida sissetulevat taotlust tööriista määratletud skeemiks:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Kui see õnnestub, siis jätkame tööriista tegeliku kasutamisega:

    ```typescript
    const result = await tool.callback(input);
    ```

Nagu näete, loob see lähenemine suurepärase arhitektuuri, kus kõik on omal kohal. *server.ts* on väga väike fail, mis ainult ühendab taotluste käsitlejad, ja iga funktsioon on oma vastavas kaustas, näiteks tools/, resources/ või prompts/.

Suurepärane, proovime seda nüüd ehitada.

## Harjutus: Madala taseme serveri loomine

Selles harjutuses teeme järgmist:

1. Loome madala taseme serveri, mis käsitleb tööriistade loetlemist ja kasutamist.
1. Rakendame arhitektuuri, millele saab ehitada.
1. Lisame valideerimise, et tagada tööriista kasutamise korrektne valideerimine.

### -1- Arhitektuuri loomine

Esimene asi, mida peame lahendama, on arhitektuur, mis aitab meil skaleerida, kui lisame rohkem funktsioone. Siin on, kuidas see välja näeb:

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

Nüüd oleme loonud arhitektuuri, mis tagab, et saame hõlpsasti lisada uusi tööriistu eraldi kausta. Võite järgida seda, et lisada alamkatalooge ressursside ja küsimuste jaoks.

### -2- Tööriista loomine

Vaatame, kuidas tööriista loomine välja näeb. Esiteks tuleb see luua oma *tool* alamkataloogis, näiteks:

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

Siin näeme, kuidas määratleme nime, kirjelduse, sisendskeemi, kasutades Pydanticut, ja käsitleja, mida kutsutakse, kui seda tööriista kasutatakse. Lõpuks ekspordime `tool_add`, mis on sõnastik, mis sisaldab kõiki neid omadusi.

Samuti on olemas *schema.py*, mida kasutatakse tööriista sisendskeemi määratlemiseks:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Peame täitma ka *__init__.py*, et tagada tööriistade kataloogi käsitlemine moodulina. Lisaks peame ekspordima selles olevad moodulid järgmiselt:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Saame seda faili täiendada, kui lisame rohkem tööriistu.

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

Siin loome sõnastiku, mis koosneb omadustest:

- name, see on tööriista nimi.
- rawSchema, see on Zodi skeem, mida kasutatakse sissetulevate taotluste valideerimiseks.
- inputSchema, seda skeemi kasutab käsitleja.
- callback, seda kasutatakse tööriista kutsumiseks.

Samuti on olemas `Tool`, mida kasutatakse selle sõnastiku teisendamiseks tüübiks, mida MCP serveri käsitleja saab aktsepteerida, ja see näeb välja järgmiselt:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja on olemas *schema.ts*, kuhu salvestame iga tööriista sisendskeemid. Praegu on seal ainult üks skeem, kuid tööriistade lisamisel saame lisada rohkem kirjeid:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Suurepärane, liigume edasi tööriistade loetlemise käsitlemise juurde.

### -3- Tööriistade loetlemise käsitlemine

Järgmiseks, et käsitleda tööriistade loetlemist, peame seadistama taotluste käsitleja selleks. Siin on, mida peame lisama oma serveri faili:

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

Siin lisame dekoratsiooni `@server.list_tools` ja rakendame funktsiooni `handle_list_tools`. Viimases peame koostama tööriistade loendi. Pange tähele, et igal tööriistal peab olema nimi, kirjeldus ja sisendskeem.

**TypeScript**

Tööriistade loetlemise taotluste käsitleja seadistamiseks peame kutsuma `setRequestHandler` serveris skeemiga, mis sobib sellega, mida üritame teha, antud juhul `ListToolsRequestSchema`.

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

Suurepärane, nüüd oleme lahendanud tööriistade loetlemise osa, vaatame, kuidas tööriistu kasutada.

### -4- Tööriista kasutamise käsitlemine

Tööriista kasutamiseks peame seadistama teise taotluste käsitleja, mis keskendub taotlusele, mis määrab, millist funktsiooni kasutada ja milliste argumentidega.

**Python**

Kasutame dekoratsiooni `@server.call_tool` ja rakendame seda funktsiooniga nagu `handle_call_tool`. Selles funktsioonis peame välja selgitama tööriista nime, selle argumendid ja tagama, et argumendid sobivad konkreetse tööriistaga. Argumentide valideerimise saame teha kas selles funktsioonis või tööriista sees.

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

Siin toimub järgmist:

- Tööriista nimi on juba olemas sisendparameetrina `name`, mis kehtib ka argumentide kohta `arguments` sõnastikus.

- Tööriista kutsutakse `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentide valideerimine toimub `handler` omaduses, mis osutab funktsioonile. Kui see ebaõnnestub, visatakse erand.

Nüüd on meil täielik arusaam tööriistade loetlemisest ja kasutamisest madala taseme serveri abil.

Vaata [täielikku näidet](./code/README.md) siit.

## Ülesanne

Laienda antud koodi mitmete tööriistade, ressursside ja küsimustega ning mõtle, kuidas märkad, et pead lisama faile ainult tööriistade kataloogi ja mitte mujale.

*Lahendust ei anta*

## Kokkuvõte

Selles peatükis nägime, kuidas madala taseme serveri lähenemine töötab ja kuidas see aitab meil luua kena arhitektuuri, millele saab edasi ehitada. Arutasime ka valideerimist ja nägime, kuidas kasutada valideerimisraamatukogusid sisendskeemide loomiseks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
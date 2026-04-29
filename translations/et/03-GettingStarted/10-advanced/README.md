# Täiustatud serveri kasutamine

MCP SDK-s on kaks erinevat tüüpi servereid, sinu tavaline server ja madala taseme server. Tavaliselt kasutad sa tavapärast serverit, et sellele funktsioone lisada. Mõnel juhul aga soovid toetuda madala taseme serverile, näiteks:

- Parem arhitektuur. On võimalik luua puhas arhitektuur nii tavapärase kui ka madala taseme serveriga, kuid võib väita, et see on veidi lihtsam madala taseme serveriga.
- Funktsioonide kättesaadavus. Mõned täiustatud funktsioonid on kasutatavad ainult madala taseme serveri puhul. Seda näed hilisemas peatükis, kui lisame proovimist ja esiletoomist.

## Tavaline server vs madala taseme server

Näide MCP serveri loomisest tavapärase serveriga:

**Python**

```python
mcp = FastMCP("Demo")

# Lisa liitumise tööriist
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

// Lisa liitmistööriist
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

Oluline on see, et sa lisad selgesõnaliselt iga tööriista, ressursi või päringu, mida soovid serveris kasutada. Pole selles midagi halba.

### Madala taseme serveri lähenemine

Kui kasutad madala taseme serveri lähenemist, pead mõtlema veidi teisiti. Selle asemel, et registreerida iga tööriist, loote iga funktsioonitüübi (tööriistad, ressursid või päringud) jaoks kaks töötlejat. Näiteks tööriistade puhul on ainult kaks funktsiooni:

- Kõikide tööriistade loetlemine. Üks funktsioon vastutab kõikide tööriistade loetlemise katsete eest.
- Kõigi tööriistade kutsumine. Samuti on siin ainult üks funktsioon, mis tegeleb tööriista kutsumisega.

See kõlab nagu potentsiaalselt vähem tööd, eks? Nii et selle asemel, et tööriista registreerida, pean lihtsalt veenduma, et tööriist oleks loetelus, kui loetlen kõik tööriistad, ja et see kutsutaks, kui tuleb tööriista kutsumise päring.

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
  // Tagasta registreeritud tööriistade nimekiri
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

Nüüd on meil funktsioon, mis tagastab funktsioonide loendi. Igas tööriistade loendi kirjes on nagu `name`, `description` ja `inputSchema` väljad, et vastata tagastustüübile. See võimaldab meil panna tööriistade ja funktsioonide definitsioonid mujale. Saame nüüd kõik tööriistad luua kaustas tools ja sama kehtib kõigi sinu funktsioonide kohta, nii et sinu projekt võib olla korraldatud järgnevalt:

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

See on suurepärane, meie arhitektuur saab olla päris puhas.

Aga kuidas on tööriistade kutsumisega, kas siis on sama idee, üks töötleja tööriista kutsumiseks, ükskõik millist tööriista? Jah, täpselt nii, siin on selle kood:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tööriistad on sõnastik, kus võtmeteks on tööriistade nimed
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
    // TODO kutsu tööriist välja,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Nagu ülalolevast koodist näha, peame välja lugema, millist tööriista kutsuda ja milliste argumentidega, seejärel jätkame tööriista kutsumisega.

## Lähenemise parandamine valideerimisega

Nii kaugele oleme näinud, kuidas kõik tööriistadele, ressurssidele ja päringutele registreerimine saab asendada nende kahe töötlejaga iga funktsioonitüübi kohta. Mida veel peaksime tegema? Peame lisama mingit sorti valideerimise, et veenduda, et tööriist kutsutakse õige argumentidega. Igal runtime'il on oma lahendus selleks, näiteks Python kasutab Pydanticut ja TypeScript Zod'i. Idee on järgmine:

- Viia funktsiooni (tööriist, ressurss või päring) loomise loogika selle pühendatud kausta.
- Lisada võimalus valideerida sissetulev päring, mis näiteks palub tööriista kutsuda.

### Loo funktsioon

Funktsiooni loomiseks peame looma selle funktsiooni jaoks faili ja veenduma, et seal on nõutud kohustuslikud väljad. Millised väljad on erinevad tööriistade, ressursside ja päringute vahel.

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
        # Kontrolli sisendit, kasutades Pydantic mudelit
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisa Pydantic, et saaksime luua AddInputModeli ja valideerida argumendid

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Siin näed, kuidas me teeme järgnevat:

- Loome skeemi kasutades Pydanticut `AddInputModel` väljadega `a` ja `b` failis *schema.py*.
- Üritame sissetuleva päringu parsida tüübiks `AddInputModel`. Kui parameetrites on lahknevus, tekib viga:

   ```python
   # add.py
    try:
        # Sisendi valideerimine Pydantic mudeli abil
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Sa võid otsustada, kas panna see parseri loogika tööriista kutsesse või töötleja funktsiooni.

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

- Töötlejas, mis tegeleb kõigi tööriistade kutsumisega, proovime nüüd parsida sissetuleva päringu tööriista määratud skeemiks:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Kui see õnnestub, jätkame tööriista tegeliku kutsumisega:

    ```typescript
    const result = await tool.callback(input);
    ```

Nagu näha, loob see lähenemine suurepärase arhitektuuri, sest kõigil asjadel on oma koht ning *server.ts* on väga väike fail, mis ühendab vaid päringutöötlejad ja iga funktsioon on oma kaustas ehk tools/, resources/ või /prompts.

Suurepärane, proovime seda järgmine ehitada.

## Harjutus: Madala taseme serveri loomine

Selles harjutuses teeme järgmist:

1. Loome madala taseme serveri, mis haldab tööriistade loetlemist ja kutsumist.
2. Rakendame arhitektuuri, millele saab edasi ehitada.
3. Lisame valideerimise tagamaks, et sinu tööriistakutsed on korrektselt valideeritud.

### -1- Loo arhitektuur

Esimene asi, millele peame lahenduse leidma, on arhitektuur, mis aitab meil skaleerida, kui lisame rohkem funktsioone, see näeb välja nii:

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

Nüüd oleme seadistanud arhitektuuri, mis tagab, et saame lihtsalt lisada uusi tööriistu kausta tools. Võid vabalt järgida seda ka subkaustade lisamiseks ressursside ja päringute jaoks.

### -2- Tööriista loomine

Vaatame, kuidas tööriista loomine välja näeb. Esiteks peab see olema loodud selles *tool* alamkaustas selliselt:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Sisendi valideerimine Pydantic mudeli abil
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisa Pydantic, et saaksime luua AddInputModeli ja valideerida argumendid

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Siin näeme, kuidas määrame nime, kirjelduse ja sisendi skeemi, kasutades Pydanticut, ning töötlejat, mis kutsutakse välja tööriista kasutamisel. Lõpuks ekspordime `tool_add`, mis on sõnastik, mis hoiab kõiki neid omadusi.

On ka *schema.py*, mida kasutatakse tööriista sisendi skeemi määratlemiseks:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Peame täiendama ka *__init__.py*, et tagada, et tools kaust käitutakse moodulina. Lisaks peame ekspordima selle sees olevad moodulid selliselt:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Sellesse faili saame lisada uusi mooduleid, kui lisame rohkem tööriistu.

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

Siin loome omadussõnastiku, mis koosneb järgmistest omadustest:

- name, see on tööriista nimi.
- rawSchema, see on Zod skeem, seda kasutatakse sissetulevate tööriistakutsete valideerimiseks.
- inputSchema, seda skeemi kasutab töötleja.
- callback, see kutsutakse tööriista käivitamiseks.

On ka `Tool`, mis teisendab selle sõnastiku tüübiks, mida mcp serveri töötleja aktsepteerib, ja see näeb välja nii:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Samuti on olemas *schema.ts*, kus hoiame iga tööriista sisendi skeeme, mis praegu näeb välja nii, kus on ainult üks skeem, kuid tööriistu lisades saame lisada rohkem kirjeid:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Suurepärane, liigume edasi tööriistade loetlemise käsitlemise juurde.

### -3- Tööriistade loetlemise töötlemine

Järgmine samm on tööriistade loetlemise töötleja seadistamine. Siin on see, mida peame serveri faili lisama:

**Python**

```python
# kood on lühiduse huvides välja jäetud
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

Siin lisame dekoratsiooni `@server.list_tools` ja rakendame funktsiooni `handle_list_tools`. Viimasel peame genereerima tööriistade nimekirja. Pange tähele, et iga tööriist peab sisaldama nime, kirjeldust ja inputSchema'd.

**TypeScript**

Tööriistade loetlemise päringu töötleja seadistamiseks peame serveris kutsuma `setRequestHandler` sobiva skeemiga, antud juhul `ListToolsRequestSchema`.

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
// kood on lühendamiseks välja jäetud
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Tagasta registreeritud tööriistade nimekiri
  return {
    tools: tools
  };
});
```

Suurepärane, nüüd on tööriistade loetlemise osa lahendatud. Vaatame, kuidas saaks järgmisena tööriistu kutsuda.

### -4- Tööriista kutsumise töötlemine

Tööriista kutsumiseks vajame teist päringu töötlejat, mis tegeleb päringuga, mis määrab, millist funktsiooni kutsuda ja milliste argumentidega.

**Python**

Kasutame dekoratsiooni `@server.call_tool` ja rakendame selle funktsiooniga, näiteks `handle_call_tool`. Selles funktsioonis saame välja lugeda tööriista nime, argumendid ja veenduda, et argumendid on selle tööriista jaoks kehtivad. Argumentide valideerimist saab teha kas siin või päringu tegelikus tööriistas.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tööriistad on sõnastik, kus võtmeteks on tööriistade nimed
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # käivita tööriist
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Toimub järgnev:

- Meie tööriista nimi on juba sisendparameetrina `name` ja argumendid on sõnastikus `arguments`.

- Tööriista kutsumine toimub läbi `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentide valideerimine toimub `handler` omaduses, mis on funktsioon, ning veateate korral visatakse erind.

Nüüd on meil täielik arusaam tööriistade loetlemisest ja kutsumisest madala taseme serveri abil.

Vaata [täielikku näidet](./code/README.md)

## Ülesanne

Laienda antud koodi mitme tööriista, ressursi ja päringuga ning mõtiskle, kuidas märkad, et pead ainult tööriistade kaustas faile lisama ja mujale mitte.

*Mingit lahendust ei anta*

## Kokkuvõte

Selles peatükis nägime, kuidas madala taseme serveri lähenemine töötab ja kuidas see aitab meil luua kena arhitektuuri, millele saame edasi ehitada. Samuti arutasime valideerimist ja sulle näidati, kuidas töötada valideerimisteekidega, et luua skeeme sisendi valideerimiseks.

## Mis järgmisena

- Järgmine: [Lihtne autentimine](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun pange tähele, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
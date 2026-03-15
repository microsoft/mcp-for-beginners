# Täiustatud serveri kasutamine

MCP SDK-s on avalikult kasutatavad kaks erinevat tüüpi serverit, teie tavaline server ja madala taseme server. Tavaliselt kasutate funktsioonide lisamiseks tavalist serverit. Mõnel juhul aga soovite tugineda madala taseme serverile, näiteks:

- Parem arhitektuur. On võimalik luua puhas arhitektuur nii tavalise kui madala taseme serveriga, kuid võib väita, et madala taseme serveriga on see natuke lihtsam.
- Funktsioonide kättesaadavus. Mõnda täiustatud funktsiooni saab kasutada ainult madala taseme serveriga. Seda näete hiljem peatükkides, kui lisame proovivõtu ja elikitsiooni.

## Tavaline server vs madala taseme server

Siin on, kuidas MCP serveri loomine välja näeb tavalise serveri puhul

**Python**

```python
mcp = FastMCP("Demo")

# Lisa liitmismeeristik
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

// Lisa liitmiste tööriist
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

Põhjus on selles, et te lisate selgesõnaliselt iga tööriista, ressursi või küsimuse, mida soovite, et serveril oleks. Sellega pole midagi valesti.  

### Madala taseme serveri lähenemine

Kui aga kasutate madala taseme serveri lähenemist, peate mõtlema teisiti. Selle asemel, et registreerida iga tööriist, loote iga funktsioonitüübi (tööriistad, ressursid või küsitlused) jaoks kaks töötlejat. Nii et näiteks tööriistadel on ainult kaks funktsiooni:

- Kõigi tööriistade loetelu kuvamine. Üks funktsioon vastutab kõigi katsete eest tööriistu loetleda.
- Kõigi tööriistade kutsumise käsitlemine. Siin on samuti ainult üks funktsioon, mis tegeleb tööriista väljakutsetega.

See kõlab nagu vähem tööd, eks? Selle asemel, et registreerida tööriist, pean lihtsalt veenduma, et tööriist oleks loetletud kõigi tööriistade loetlemisel ja et seda kutsutaks, kui tuleb päring tööriista kutsumiseks.

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
  // Tagastage registreeritud tööriistade nimekiri
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

Siin on meil nüüd funktsioon, mis tagastab funktsioonide nimekirja. Iga tööriista nimekirja kirje sisaldab nüüd välju nagu `name`, `description` ja `inputSchema`, mis vastavad tagastustüübile. See võimaldab meil paigutada oma tööriistad ja funktsioonide definitsioonid mujale. Saame nüüd luua kõik oma tööriistad kaustas tools ning sama kehtib kõigi teie funktsioonide kohta, nii et teie projekt võib olla organiseeritud näiteks nii:

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

Kuidas on tööriistade kutsumisega, kas see on siis sama mõte, üks töötleja tööriista kutsumiseks, ükskõik millise tööriista puhul? Jah, just nii, siin on selle jaoks kood:

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
    // TODO kutsuda tööriist,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Nagu ülalolevast koodist näha, peame välja võtma, millist tööriista kutsutakse ja milliste argumentidega, ning seejärel peame tööriista kutsumisega jätkama.

## Lähenemise parendamine valideerimisega

Siiani nägite, kuidas kõik teie registreeringud tööriistade, ressursside ja küsimuste lisamiseks saab asendada nende kahe töötlejaga iga funktsioonitüübi kohta. Mida veel teha? Tuleb lisada mingi vorm valideerimist, et tagada tööriista kutsumine õige argumentidega. Igal käituskeskkonnal on selle jaoks oma lahendus, näiteks Python kasutab Pydanticut ja TypeScript Zod-i. Idee on järgmine:

- Liigutada funktsiooni (tööriist, ressurss või küsitlus) loomise loogika omaette kausta.
- Lisada viis valideerida sissetulev päring, mis näiteks küsib tööriista kutsumist.

### Funktsiooni loomine

Funktsiooni loomiseks peame looma selle funktsiooni jaoks faili ja tagama, et see sisaldab selle funktsiooni jaoks vajalikke kohustuslikke välju. Millised väljad erinevad veidi tööriistade, ressursside ja küsitluste vahel.

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
        # Kontrolli sisendit Pydantic mudeli abil
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

Siin näete, kuidas me teeme järgmist:

- Loome skeemi Pydanticu `AddInputModel` abil, millel on väljad `a` ja `b`, failis *schema.py*.
- Püüame sissetuleva päringu teisendada tüübiks `AddInputModel`, kui parameetrid ei klapi, siis see põhjustab vea:

   ```python
   # add.py
    try:
        # Sisendi valideerimine Pydantic mudeli abil
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Võite valida, kas panna see parsimise loogika tööriista kutse enda sisse või töötleja funktsiooni.

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

- Kõikide tööriistade kutsetega tegelevas töötlejas püüame nüüd sissetuleva päringu teisendada tööriista määratletud skeemiks:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kui see õnnestub, jätkame tööriista tegeliku kutsumisega:

    ```typescript
    const result = await tool.callback(input);
    ```

Nagu näha, loob see lähenemine suurepärase arhitektuuri, kuna kõigil on oma koht, *server.ts* on väga väike fail, mis ainult ühendab päringute töötlejad ja iga funktsioon on oma kaustas, nt tools/, resources/ või /prompts.

Suurepärane, proovime seda järgmine kord ehitada. 

## Harjutus: Madala taseme serveri loomine

Selles harjutuses teeme järgmist:

1. Loome madalat taset serveri, mis haldab tööriistade loetelu ja tööriistade kutsumist.
1. Teostame arhitektuuri, millele saab edasi ehitada.
1. Lisame valideerimise, et tagada tööriista kutsed on korrektselt valideeritud.

### -1- Arhitektuuri loomine

Esimene asi, millega tegeleme, on arhitektuur, mis aitab meil skaleerida, kui lisame rohkem funktsioone, siin on, kuidas see välja näeb:

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

Nüüd oleme seadistanud arhitektuuri, mis tagab, et saame hõlpsasti lisada uusi tööriistu kausta tools. Võite lisada ka alamkaustad ressurssidele ja küsitlustele.

### -2- Tööriista loomine

Vaatame, kuidas tööriista loomine järgmisena välja näeb. Esiteks peab tööriist olema loodud oma *tool* alamkaustas selliselt:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Kontrolli sisendit, kasutades Pydantic mudelit
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lisa Pydantic, et saaksime luua AddInputModel ja valideerida argumendid

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Siin näeme, kuidas defineerime nime, kirjelduse ja sisendi skeemi Pydanticu abil ning töötlejat, mis kutsutakse tööriista kasutamisel. Lõpuks ekspordime `tool_add`, mis on sõnastik kõigi nende omadustega.

Samuti on olemas *schema.py*, mida kasutatakse meie tööriista sisendi skeemi defineerimiseks:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Peame täitma ka *__init__.py*, et tööriistade kataloogi käsitletaks moodulina. Lisaks peame ekspordima selles moodulis olevad moodulid, näiteks nii:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Selles faili saame lisada juurde, kui lisame rohkem tööriistu.

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

Siin loome sõnastiku, mis sisaldab omadusi:

- name, tööriista nimi.
- rawSchema, see on Zod skeem, mida kasutatakse sissetulevate tööriistakutsete valideerimiseks.
- inputSchema, seda skeemi kasutab töötleja.
- callback, mida kasutatakse tööriista kutsumiseks.

Samuti on olemas `Tool`, mida kasutatakse selle sõnastiku teisendamiseks tüübiks, mida mcp serveri töötleja saab aktsepteerida, see näeb välja selline:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja on olemas *schema.ts*, kuhu salvestame iga tööriista sisendi skeemid, juhuslikult on seal praegu ainult üks skeem, kuid tööriistu lisades võime lisada ka rohkem kirjeid:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Suurepärane, jätkame järgmise sammuga: haldame tööriistade loetelu.

### -3- Tööriistade loetelu haldamine

Järgmine samm on seadistada päringut töötleja, mis haldab tööriistade nimekirja päringuid. Siin on, mida serveri faili lisada:

**Python**

```python
# kood on lühendatud
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

Siin lisame dekoratsiooni `@server.list_tools` ja rakendame funktsiooni `handle_list_tools`. Viimases peame tootma tööriistade nimekirja. Pange tähele, et iga tööriist vajab nime, kirjeldust ja inputSchema-d.

**TypeScript**

Tööriistade loendamise päringut töötlejaks seadistamiseks kutsume serveril `setRequestHandler`, kasutades sobivat skeemi, antud juhul `ListToolsRequestSchema`.

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
// Kood on lühendatud
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Tagasta registreeritud tööriistade nimekiri
  return {
    tools: tools
  };
});
```

Suurepärane, nüüd oleme lahendanud tööriistade loetelu osa, vaatame järgmisena, kuidas saaks tööriistu kutsuda.

### -4- Tööriista kutsumise haldamine

Tööriista kutsumiseks peame seadistama teise päringut töötleja, mis tegeleb päringutega, milles on määratud, millist funktsiooni kutsutakse ja milliste argumentidega.

**Python**

Kasutame dekoratsiooni `@server.call_tool` ja rakendame selle funktsiooniga `handle_call_tool`. Selle funktsiooni sees peame välja võtma tööriista nime, argumendid ja tagama, et argumendid on valiidid tööriista jaoks. Võime argumente valideerida kas selles funktsioonis või hiljem tööriistas endas.

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
        # kutsu tööriista esile
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Siin läheb järgmist:

- Meie tööriista nimi on juba sisendparameetri `name` kujul ja argumendid sõnastiku `arguments` kujul.

- Tööriist kutsutakse `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` abil. Argumentide valideerimine toimub `handler` atribuudi funktsioonis, kui see ebaõnnestub, visatakse erand.

Nüüd on meil täielik arusaam tööriistade loendamisest ja kutsumisest madala taseme serveri abil.

Vaata [täielik näide](./code/README.md) siit

## Kodutöö

Laienda antud koodi mitme tööriista, ressursi ja küsitlusega ning peegelduge, kuidas märkate, et peate lisama faile ainult tools kausta ja mitte kuskile mujale.

*Lahendust ei anta*

## Kokkuvõte

Selles peatükis nägime, kuidas madala taseme serveri lähenemine töötab ja kuidas see aitab meil luua kena arhitektuuri, millele saab järjest juurde ehitada. Arutasime ka valideerimist ja teile näidati, kuidas kasutada valideerimisteeke, et luua sisendi valideerimise skeeme.

## Mis järgmiseks

- Järgmine: [Lihtne autentimine](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüdleme täpsuse poole, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutusele võtta professionaalne inimtõlge. Me ei vastuta selle tõlke kasutamisest tingitud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
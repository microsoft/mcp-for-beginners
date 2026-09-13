# Täiustatud serveri kasutamine

MCP SDK-s on kaks erinevat serveritüüpi, normaalsed serverid ja madala tasemega serverid. Tavaliselt kasutate tavalist serverit selle võimaluste laiendamiseks. Mõnel juhul aga soovite tugineda madala tasemega serverile, näiteks:

- Parem arhitektuur. On võimalik luua puhas arhitektuur nii tavalise serveri kui madala taseme serveriga, kuid väidetavalt on see natuke lihtsam madala taseme serveriga.
- Funktsioonide kättesaadavus. Mõnda täiustatud funktsiooni saab kasutada ainult madala taseme serveriga.
    Hilisemates peatükkides käsitletakse Elicitationi ja vananenud Sampling
    funktsiooni, mida MCP `2026-07-28` enam ei toetata.

## Tavaline server vs madala taseme server

Siin on, kuidas MCP serveri loomine välja näeb tavalise serveri puhul

**Python**

```python
mcp = FastMCP("Demo")

# Lisa lisamise tööriist
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

// Lisa liitmise tööriist
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

Peamine mõte on see, et peate selgesõnaliselt lisama iga tööriista, ressursi või käsku, mis soovite serverile lisada. Sellega pole midagi valesti.

### Madala taseme serveri lähenemine

Madala taseme serveri kasutamisel tuleb sellele teistmoodi mõelda. Selle asemel, et registreerida iga tööriist eraldi, loote iga funktsioonitüübi (tööriistad, ressursid või käsud) jaoks kaks töötlejat. Näiteks on tööriistadel siis ainult kaks funktsiooni:

- Kõigi tööriistade loetelu koostamine. Üks funktsioon vastutab kõigi tööriistade loetlemise katsete eest.
- Kõigi tööriiskutsete töötlemine. Siin on samuti ainult üks funktsioon, mis haldab tööriistakõnesid.

Tundub, et see võib olla vähem tööd, eks? Niisiis, selle asemel, et registreerida tööriist, pean ma lihtsalt veenduma, et tööriista loetletakse, kui ma loetlen kõik tööriistad, ja et seda kutsutakse, kui toimub tööriista kutsumise päring.

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

Nüüd on meil funktsioon, mis tagastab funktsioonide loendi. Igal tööriistal on nüüd väljad nagu `name`, `description` ja `inputSchema`, et vastata tagastustüübile. See võimaldab meil tööriistade ja funktsioonide määratluse paigutada mujale. Saame kõik oma tööriistad paigutada tööriistade kausta ning sama kehtib kõigi teie funktsioonide kohta, nii et projekt võib järsku olla organiseeritud nii:

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

See on suurepärane, meie arhitektuur võib välja näha väga puhas.

Kuidas on tööriistade kutsumisega, kas see on sama mõte, üks töötleja tööriista kutsumiseks, ükskõik millise tööriista puhul? Jah, täpselt, siin on kood selle jaoks:

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
    // TEE KORRAL tööriista kutsumine,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Nagu näete ülaltoodud koodist, peame tööstuse kutsumiseks ja argumentide eraldamiseks analüüsima ning seejärel kutse tegemiseks tööriista edasi kutsuma.

## Lähenemise parandamine valideerimisega

Seni olete näinud, kuidas kõik teie registreerimised tööriistade, ressursside ja käskude lisamiseks saab asendada nende kahe töötlejaga iga funktsioonitüübi kohta. Mida veel peame tegema? Peaksime lisama mingisuguse valideerimise, et veenduda, et tööriist kutsutakse õige argumendiga. Iga käitusaeg kasutab selleks oma lahendust, näiteks Python kasutab Pydanticut ja TypeScript Zod'i. Mõte on see:

- Viia funktsiooni loomise loogika (tööriist, ressurss või käsk) oma pühendatud kausta.
- Lisada viis valideerida saabuvat päringut, mis küsib näiteks tööriista kutsumist.

### Funktsiooni loomine

Funktsiooni loomiseks peame selle funktsiooni jaoks looma faili ja veenduma, et selles on funktsioonile vajalikud kohustuslikud väljad. Väljad erinevad tööriistadel, ressurssidel ja käskudel natuke.

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

    # TODO: lisa Pydantic, et saaksime luua AddInputModeli ja valideerida argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

siin näete, kuidas me teeme järgmist:

- Luuakse skeem Pydanticuga `AddInputModel` koos väljadega `a` ja `b` failis *schema.py*.
- Püüab sisenevat päringut analüüsida kui tüüpi `AddInputModel`; kui parameetrid ei ühti, siis programm kunagi kokku jookseb:

   ```python
   # add.py
    try:
        # Sisendi valideerimine Pydantic mudeli abil
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Võite valida, kas panna see analüüsiloogika tööriista kutsesse või töötleja funktsiooni.

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

- Tööriistakõnede töötlejas proovitakse nüüd sisenev päring tõlgendada tööriista määratletud skeemi järgi:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    kui see õnnestub, jätkatakse tegeliku tööriista kutsumisega:

    ```typescript
    const result = await tool.callback(input);
    ```

Nagu näete, loob see lähenemine suurepärase arhitektuuri, sest kõigil on oma koht; *server.ts* on väga väike fail, mis seob ainult päringutöötlejad kokku ning iga funktsioon on oma vastavas kaustas, nt tools/, resources/ või /prompts.

Väga hea, proovime nüüd selle üles ehitada.

## Harjutus: Madala taseme serveri loomine

Selles harjutuses teeme järgmist:

1. Loome madala taseme serveri, mis tegeleb tööriistade loetlemise ja kutsumisega.
1. Rakendame arhitektuuri, millele saate edasi ehitada.
1. Lisame valideerimise, et teie tööriistakutsed oleksid korrektselt valideeritud.

### -1- Arhitektuuri loomine

Esimene asi, mida peame lahendama, on arhitektuur, mis aitab meil suures mahus funktsioone lisada; see näeb välja selline:

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

Nüüd oleme loonud arhitektuuri, mis tagab, et saame hõlpsalt lisada uusi tööriistu tööriistade kausta. Võite sama teha ka ressursside ja käskude jaoks alamkaustadena.

### -2- Tööriista loomine

Vaatame, kuidas tööriista loomine välja näeb. Esiteks tuleb see luua oma *tool* alamkausta nii:

**Python**

```python
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

Siin näeme, kuidas määratleme nime, kirjelduse ja sisendskeemi Pydanticuga ning töötleja, mis käivitatakse tööriista kutsumisel. Lõpuks ekspordime `tool_add`, mis on sõnastik kõigi nende omadustega.

Samuti on olemas *schema.py*, mida kasutatakse meie tööriista sisendskeemi määramiseks:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Peame täiendavalt täitma *__init__.py*, et tööriistade kaust oleks moodulina käsitletud. Lisaks peame moodulid ekspordima nii:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Võime sellesse faili lisada juurde, kui lisame uusi tööriistu.

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
- rawSchema, see on Zod skeem, mida kasutatakse tööriista kutsumise päringute valideerimiseks.
- inputSchema, selle skeemiga töötab töötleja.
- callback, seda kasutatakse tööriista käivitamiseks.

Samuti on olemas tüüp `Tool`, mis teisendab selle sõnastiku tüüpi, mida mcp serveri töötleja saab vastu võtta, ja see näeb välja nii:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ja on olemas *schema.ts*, kuhu salvestame iga tööriista sisendskeemid, praegu on ainult üks skeem, kuid tööriistu lisades saab lisada rohkem:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Suurepärane, liigume edasi tööriistade listimise töötlejale.

### -3- Tööriistade loendi töötlemine

Järgmiseks peame loonudgi päringu töötleja tööriistade loetlemiseks. See, mida peame lisama serveri failile:

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

Siin lisame dekoratsiooni `@server.list_tools` ja funktsiooni `handle_list_tools`. Viimases peame tagastama tööriistade nimekirja. Pane tähele, et igal tööriistal peab olema nimi, kirjeldus ja inputSchema.

**TypeScript**

Tööriistade loendamise päringu töötleja seadistamiseks kutsume serveril `setRequestHandler` sobiva skeemiga, antud juhul `ListToolsRequestSchema`.

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

Väga hea, nüüd on tööriistade listimise osa lahendatud, vaatame, kuidas võiks tööriistu kutsuda.

### -4- Tööriista kutsumise töötlemine

Tööriista kutsumiseks peame seadistama teise päringu töötleja, mis tegeleb päringuga, mis näitab, millist funktsiooni kutsuda ja milliste argumentidega.

**Python**

Kasutame dekoratsiooni `@server.call_tool` ja rakendame selle funktsiooniga nagu `handle_call_tool`. Selle funktsiooni sees peame välja analüüsima tööriista nime, selle argumendid ning veenduma, et argumendid on antud tööriista jaoks õiged. Võime argumendid valideerida selles funktsioonis või hiljem tegelikus tööriistas.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools on sõnastik, kus tööriistade nimed on võtmeteks
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # kutsu tööriist välja
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Siin toimub järgnev:

- Meie tööriista nimi on juba olemas sisendiparameetrina `name` ja see kehtib ka argumentide kohta sõnastikus `arguments`.

- Tööriist kutsutakse `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` abil. Argumentide valideerimine toimub `handler` omaduses, mis on funktsioon; kui see ebaõnnestub, visatakse erind.

Nüüd oleme täielikult aru saanud, kuidas tööriistu loetleda ja kutsuda madala taseme serveri abil.

Vaata [täielikku näidet](./code/README.md) siit

## Kodune ülesanne

Laienda antud koodi mitme tööriista, ressursi ja käsuga ning pane tähele, kuidas tuleb faile lisada ainult tööriistade kataloogi ega kusagile mujale.

*Lahendust ei anta*

## Kokkuvõte

Selles peatükis nägime, kuidas madala taseme serveri lähenemine töötab ja kuidas see aitab luua kena arhitektuuri, millele saame edasi ehitada. Rääkisime ka valideerimisest ning näidati teile, kuidas töötada valideerimisteekidega skeemide loomiseks sisendite kontrollimiseks.

## Mis järgmiseks

- Järgmine: [Lihtne autentimine](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
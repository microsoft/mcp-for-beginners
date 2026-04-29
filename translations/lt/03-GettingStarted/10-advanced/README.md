# Išplėstinis serverio naudojimas

MCP SDK yra du skirtingi serverių tipai: jūsų įprastas serveris ir žemo lygio serveris. Paprastai naudotumėte įprastą serverį funkcijoms pridėti. Tačiau kai kuriais atvejais norite pasikliauti žemo lygio serveriu, pavyzdžiui:

- Geresnė architektūra. Galima sukurti švarią architektūrą tiek su įprastu, tiek su žemo lygio serveriu, tačiau galima teigti, kad tai šiek tiek lengviau padaryti su žemo lygio serveriu.
- Funkcijų prieinamumas. Kai kurios pažangios funkcijos galima naudoti tik su žemo lygio serveriu. Tai pamatysite vėlesniuose skyriuose, kai pridėsime imtį ir iškvietimą.

## Įprastas serveris vs žemo lygio serveris

Štai kaip atrodo MCP serverio kūrimas su įprastu serveriu

**Python**

```python
mcp = FastMCP("Demo")

# Pridėti papildymo įrankį
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

// Pridėti papildymo įrankį
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

Pagrindas yra tai, kad jūs aiškiai pridedate kiekvieną įrankį, išteklių ar užklausą, kurių norite, kad serveris turėtų. Čia nėra nieko blogo.

### Žemo lygio serverio požiūris

Tačiau naudodami žemo lygio serverio požiūrį turite galvoti kitaip. Vietoje kiekvieno įrankio registravimo, vietoje to sukuriate po du apdorotojus kiekvienam funkcijos tipui (įrankiai, ištekliai ar užklausos). Pvz., įrankiai turi tik dvi funkcijas:

- Visų įrankių sąrašo pateikimas. Viena funkcija atsako už visas bandymų pateikti įrankių sąrašą užklausas.
- Aptarnauja įrankių iškvietimą. Čia taip pat yra viena funkcija, apdorojanti įrankio iškvietimą.

Skamba, kaip mažiau darbo teisingai? Vietoje kad registruočiau įrankį, man tiesiog reikia užtikrinti, kad įrankis būtų įtrauktas į įrankių sąrašą ir kad jis būtų iškviečiamas atvykus užklausai iškviesti įrankį.

Pažiūrėkime, kaip dabar atrodo kodas:

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
  // Grąžinti registruotų įrankių sąrašą
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

Čia turime funkciją, kuri grąžina funkcijų sąrašą. Kiekvienas įrankių sąrašo įrašas dabar turi laukus, pavyzdžiui, `name`, `description` ir `inputSchema`, kad atitiktų grąžinimo tipą. Tai leidžia įrankius ir funkcijų apibrėžimą laikyti kitur. Dabar galime visus įrankius sukurti *tools* kataloge, tas pats galioja ir visoms jūsų funkcijoms, todėl jūsų projektas gali būti organizuotas taip:

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

Puiku, mūsų architektūrą galima padaryti labai švarią.

O kaip dėl įrankių iškvietimo, ar tai tas pats principas, viena apdorotojo funkcija iškviečia bet kurį įrankį? Taip, tiksliai, štai kodas tam:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kur raktažodžiai yra įrankių pavadinimai
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
    // TODO iškviesti įrankį,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kaip matote iš aukščiau pateikto kodo, turime išanalizuoti, kurį įrankį iškviesti ir su kokiais argumentais, tada tęsti įrankio iškvietimą.

## Požiūrio gerinimas su validacija

Iki šiol matėte, kaip visi jūsų įrankių, išteklių ir užklausų registravimai gali būti pakeisti šiomis dviem apdorojančiomis funkcijomis kiekvienam funkcijos tipui. Ką dar turime padaryti? Turėtume pridėti tam tikrą validaciją, kad įrankis būtų iškviečiamas su tinkamais argumentais. Kiekviena vykdymo aplinka turi savo sprendimus — pavyzdžiui, Python naudoja Pydantic, o TypeScript Zod. Idėja tokia:

- Perkelti funkcijos kūrimo (įrankio, ištekliaus ar užklausos) logiką į skiriamą katalogą.
- Pridėti būdą validuoti atėjusias užklausas, pavyzdžiui, kai norima iškviesti įrankį.

### Funkcijos kūrimas

Norint sukurti funkciją, reikia sukurti tą funkciją reprezentuojantį failą ir užtikrinti, kad jame būtų privalomi tos funkcijos laukai. Šie laukai šiek tiek skiriasi įrankiams, ištekliams ir užklausoms.

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
        # Patikrinkite įvestį naudodami Pydantic modelį
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridėti Pydantic, kad galėtume sukurti AddInputModel ir patikrinti argumentus

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Čia matome kaip atliekame:

- Sukuriame Pydantic `AddInputModel` schemą su laukais `a` ir `b` faile *schema.py*.
- Bandoma analizuoti atėjusią užklausą, kad ji būtų `AddInputModel` tipo, jei parametrai nesutampa, tai sugrius:

   ```python
   # add.py
    try:
        # Patikrinkite įvestį naudodami Pydantic modelį
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Galite pasirinkti, ar tą analizavimo logiką dėti į patį įrankio iškvietimą, ar į apdorojančią funkciją.

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

- Apdorojant visas įrankių iškvietimo užklausas, bandoma analizuoti atėjusią užklausą pagal įrankio apibrėžtą schemą:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jei tai pavyksta, tęsiame faktinį įrankio iškvietimą:

    ```typescript
    const result = await tool.callback(input);
    ```

Kaip matote, ši koncepcija sukuria puikią architektūrą, nes viskas yra savo vietoje, *server.ts* yra labai mažas failas, kuris tik sujungia užklausų apdorojimo funkcijas, o kiekviena funkcija yra savo kataloge, t. y. tools/, resources/ arba /prompts.

Puiku, pabandykime tai sukurti toliau.

## Užduotis: Sukurti žemo lygio serverį

Šios užduoties metu atliksime:

1. Sukursime žemo lygio serverį, kuris apdoros įrankių sąrašą ir jų iškvietimą.
1. Įgyvendinsime architektūrą, kuria galėsite plėsti.
1. Pridėsime validaciją, kad užtikrintume teisingą įrankių iškvietimų tikrinimą.

### -1- Sukurti architektūrą

Pirmas dalykas, kurį turime spręsti — architektūra, kuri padės mums augti pridedant funkcijas, štai kaip ji atrodo:

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

Dabar sukūrėme architektūrą, kuri užtikrina, jog galime lengvai pridėti naujus įrankius *tools* kataloge. Galite taip pat pridėti paveiksliukus ištekliams ir užklausoms.

### -2- Įrankio kūrimas

Pažiūrėkime, kaip atrodo įrankio kūrimas. Pirmiausia jis turi būti sukurtas savo *tool* pakatalogyje, pavyzdžiui:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Patvirtinti įvestį naudojant Pydantic modelį
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: pridėti Pydantic, kad galėtume sukurti AddInputModel ir patikrinti argumentus

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Čia matome, kaip apibrėžiame pavadinimą, aprašymą ir įvesties schemą naudojant Pydantic ir apdorojimo funkciją, kuri bus kviečiama iškvietus įrankį. Galų gale eksportuojame `tool_add`, kuris yra žodynas, turintis šias savybes.

Taip pat yra *schema.py*, kuri apibrėžia įvesčių schemą mūsų įrankiui:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Reikia užpildyti ir *__init__.py*, kad *tools* katalogas būtų laikomas moduliu. Be to, reikia eksportuoti modulius taip:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Galime tęsti šį failą, kai pridėsime daugiau įrankių.

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

Čia sukuriame žodyną, kuriame yra:

- name — tai įrankio pavadinimas.
- rawSchema — Zod schema, naudojama validuoti įrankio iškvietimo užklausoms.
- inputSchema — schema, naudojama apdorojančioje funkcijoje.
- callback — funkcija, kuri iškviečia įrankį.

Yra taip pat `Tool` tipas, kuris paverčia šį žodyną į tipą, kurį gali priimti mcp serverio apdorotojas, atrodo taip:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Taip pat yra *schema.ts*, kur saugomos įvesties schemos kiekvienam įrankiui, dabar su vienu schema, bet pridėjus daugiau įrankių, išaugs įrašų skaičius:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Puiku, dabar imkimės apdoroti įrankių sąrašą.

### -3- Įrankių sąrašo tvarkymas

Norint apdoroti įrankių sąrašą, reikia nustatyti užklausų apdorojimo funkciją. Štai ką reikia pridėti prie serverio failo:

**Python**

```python
# kodas sutrumpintas dėl glaustumo
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

Pridedame dekoratorių `@server.list_tools` ir apdorojančią funkciją `handle_list_tools`. Joje reikia pateikti įrankių sąrašą. Atkreipkite dėmesį, kad kiekvienas įrankis turi turėti laukus name, description ir inputSchema.

**TypeScript**

Kad nustatytume užklausų apdorojimo funkciją įrankių sąrašui, kviečiame `setRequestHandler` ant serverio su schema, atitinkančia mūsų veiksmą, šiuo atveju `ListToolsRequestSchema`.

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
// kodas sutrumpintas
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Grąžinkite registruotų įrankių sąrašą
  return {
    tools: tools
  };
});
```

Puiku, išsprendėme įrankių sąrašo dalį, pažvelkime, kaip galėtume iškviesti įrankius.

### -4- Įrankio iškvietimo tvarkymas

Norint iškviesti įrankį, reikia sukurti dar vieną užklausų apdorojimo funkciją, kuri apdoros užklausą, kurioje bus nurodyta, kurią funkciją iškviesti ir su kokiais argumentais.

**Python**

Naudosime dekoratorių `@server.call_tool` ir apdorojimą įgyvendinsime funkcija pavadinimu `handle_call_tool`. Joje turime išanalizuoti įrankio pavadinimą, argumentus ir patikrinti, ar argumentai tinkami tam įrankiui. Galima validuoti argumentus čia arba jau pačiame įrankyje.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kurio raktai yra įrankių pavadinimai
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # iškvieskite įrankį
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Štai ką darome:

- Įrankio pavadinimas jau yra įėjimo parametre `name`, o argumentai pateikti `arguments` žodyne.

- Įrankis iškviečiamas `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentų validavimas vyksta pačioje `handler` funkcijoje, jei jis nepavyksta, bus išmesta klaida.

Štai pilnas supratimas apie įrankių sąrašą ir iškvietimą naudojant žemo lygio serverį.

Visa [pilna pavyzdžių galerija](./code/README.md) čia

## Užduotis

Išplėskite pateiktą kodą pridėdami keletą įrankių, išteklių ir užklausų ir apmąstykite, kaip stebite, jog reikia kurti failus tik *tools* kataloge, o niekur kitur.

*Nėra pateikto sprendimo*

## Santrauka

Šiame skyriuje matėme, kaip veikia žemo lygio serverio požiūris ir kaip jis gali padėti sukurti tvarkingą architektūrą tolesniam plėtojimui. Taip pat aptarėme validaciją ir kaip naudoti validavimo bibliotekas, kad sukurtume įvesties validacijos schemas.

## Kas toliau

- Toliau: [Paprastas autentifikavimas](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas pagrindiniu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingą interpretavimą, kilusius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
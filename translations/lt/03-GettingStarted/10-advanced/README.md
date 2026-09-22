# Išplėstinis serverio naudojimas

MCP SDK yra dvi skirtingos serverių rūšys – įprastasis serveris ir žemo lygio serveris. Paprastai naudojate įprastą serverį, kad pridėtumėte funkcijas. Tačiau kai kuriais atvejais norėsite pasikliauti žemo lygio serveriu, pavyzdžiui:

- Geresnė architektūra. Įmanoma sukurti švarią architektūrą tiek su įprastiniu, tiek su žemo lygio serveriu, tačiau galima teigti, kad tai truputį lengviau su žemo lygio serveriu.
- Funkcionalumo prieinamumas. Kai kurios pažangios funkcijos gali būti naudojamos tik su
    žemo lygio serveriu. Vėlesniuose skyriuose aptariama Elicitation ir senstelėjusi Sampling
    funkcija, kuri MCP `2026-07-28` yra nebenaudojama.

## Įprastinis serveris vs žemo lygio serveris

Štai kaip atrodo MCP Serverio kūrimas naudojant įprastinį serverį

**Python**

```python
mcp = FastMCP("Demo")

# Pridėti pridedamą įrankį
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

// Pridėti pridėjimo įrankį
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

Pagrindinė idėja yra ta, kad jūs aiškiai pridedate kiekvieną įrankį, išteklių ar užklausą, kurią norite turėti serveryje. Tai visiškai normalu.  

### Žemo lygio serverio metodas

Tačiau naudodami žemo lygio serverio metodą turite galvoti kitaip. Vietoje to, kad registruotumėte kiekvieną įrankį, jūs kuriate du valdiklius kiekvienam funkcijų tipui (įrankiai, ištekliai ar užklausos). Pavyzdžiui, įrankiams lieka tik dvi funkcijos:

- Išvardinti visus įrankius. Viena funkcija atsakinga už visus įrankių išvardinimus.
- tvarkyti įrankio kvietimus. Čia taip pat yra tik viena funkcija, apdorojanti įrankio kvietimus.

Skamba kaip potencialiai mažiau darbo, tiesa? Taigi, vietoje to, kad registruočiau įrankį, man tiesiog reikia įsitikinti, kad įrankis yra išvardintas, kai išvardinu visus įrankius, ir kad jį kviečiu, kai ateina užklausa įrankiui iškviesti. 

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
  // Grąžina registruotų įrankių sąrašą
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

Dabar turime funkciją, kuri grąžina funkcijų sąrašą. Kiekvienas įrašas įrankių sąraše dabar turi laukus kaip `name`, `description` ir `inputSchema`, kad atitiktų grąžinimo tipą. Tai leidžia įrankių ir funkcijų apibrėžimus laikyti kitur. Galime sukurti visus įrankius įrankių kataloge ir taip pat padaryti taip su visomis funkcijomis, todėl projektas gali būti organizuotas taip:

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

Puiku, mūsų architektūra gali būti gana švari.

O kaip su įrankių kvietimu, ar tai ta pati idėja – vienas valdiklis kviečia bet kurį įrankį? Taip, tiksliai, štai kodas tam:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kurio raktažodžiai yra įrankių pavadinimai
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

Kaip matote iš aukščiau pateikto kodo, turime išanalizuoti, kurį įrankį kviečiame ir su kokiais argumentais, o tada tęsti įrankio kvietimą.

## Metodas tobulinant validaciją

Iki šiol matėte, kaip visas registracijas pridedant įrankius, išteklius ir užklausas galima pakeisti šiomis dviem valdiklių funkcijomis kiekvienam funkcijų tipui. Ką dar reikia padaryti? Turėtume pridėti tam tikrą validaciją, kad įrankis būtų kviečiamas su tinkamais argumentais. Kiekviena vykdymo aplinka tai sprendžia savaip, pavyzdžiui Python naudoja Pydantic, o TypeScript – Zod. Idėja tokia:

- Perkelti logiką, kuri sukuria funkciją (įrankį, išteklių ar užklausą) į jos dedikuotą katalogą.
- Pridėti būdą tikrinti įeinančią užklausą, prašančią, pavyzdžiui, įrankio kvietimo.

### Kurti funkciją

Kad sukurtume funkciją, mums reikės sukurti failą tai funkcijai ir įsitikinti, kad ji turi privalomus laukus, kurie reikalaujami tą funkciją apibrėžiančių. Laukai truputį skiriasi tarp įrankių, išteklių ir užklausų.

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

čia matote, kaip atliekame:

- Sukuriame schemą naudodami Pydantic `AddInputModel` su laukais `a` ir `b` faile *schema.py*.
- Bandome išanalizuoti įeinančią užklausą kaip `AddInputModel` tipą, jei parametrai nesutampa, tai baigsis klaida:

   ```python
   # add.py
    try:
        # Patikrinkite įvestį naudodami Pydantic modelį
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Galite pasirinkti, ar šią analizės logiką įdėti į įrankio kvietimo funkciją, ar į valdiklio funkciją.

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

- Valdiklyje, tvarkančiame visus įrankių kvietimus, dabar bandoma įeinančią užklausą išanalizuoti pagal įrankio apibrėžtą schemą:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jei tai pavyksta, tęsiame įrankio kvietimą:

    ```typescript
    const result = await tool.callback(input);
    ```

Kaip matote, šis požiūris sukuria puikią architektūrą, nes viskas yra savo vietoje, *server.ts* yra labai mažas failas, kuris tik prijungia užklausų valdiklius, o kiekviena funkcija yra savo aplanke – įrankiai, ištekliai ar užklausos.

Puiku, pabandykime dabar tai sukurti.

## Praktinė užduotis: žemo lygio serverio kūrimas

Šioje užduotyje mes atliksime:

1. Sukursime žemo lygio serverį, kuris valdo įrankių išvardinimą ir kvietimą.
1. Įgyvendinsime architektūrą, ant kurios galėsite toliau kurti.
1. Pridėsime validaciją, kad įrankių kvietimai būtų teisingai tikrinami.

### -1- Sukurkite architektūrą

Pirmiausia turime susitvarkyti architektūrą, kuri padėtų mums išplėsti projektą pridedant daugiau funkcijų. Štai kaip tai atrodo:

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

Dabar turime architektūrą, kuri leidžia lengvai pridėti naujus įrankius į tools katalogą. Galite laisvai pridėti poskirsnius resources ir prompts.

### -2- Įrankio kūrimas

Pažiūrėkime, kaip atrodo įrankio kūrimas. Pirmiausia, jis turi būti sukurtas savo *tool* poskirtyje taip:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Patvirtinkite įvestį naudodami Pydantic modelį
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

Čia matome, kaip apibrėžiame pavadinimą, aprašymą ir įvesties schemą naudodami Pydantic bei valdiklį, kuris bus kviečiamas įrankiui iškvietus. Galiausiai eksponuojame `tool_add`, kuris yra žodynas su šiomis savybėmis.

Taip pat yra *schema.py*, kuriame apibrėžiame įvesties schemą, naudojamą mūsų įrankio:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Taip pat reikia užpildyti *__init__.py*, kad tools katalogas būtų laikomas moduliu. Taip pat reikia eksponuoti jo modulius taip:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Galime toliau pildyti šį failą pridėdami daugiau įrankių.

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

Čia kuriame žodyną su savybėmis:

- name – tai įrankio pavadinimas.
- rawSchema – tai Zod schema, kuri bus naudojama naujoms užklausoms tikrinti kviečiant šį įrankį.
- inputSchema – ši schema bus naudojama valdiklyje.
- callback – naudojama įrankiui iškviesti.

Taip pat yra `Tool` tipas, skirtas paversti šį žodyną į tipą, kurį MCP serverio valdiklis priims, kuris atrodo taip:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Dar yra *schema.ts*, kuriame laikome įrankio įvesties schemas, dabar viena schema, bet pridėjus daugiau įrankių tokių įrašų bus daugiau:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Puiku, dabar pereikime prie mūsų įrankių sąrašo valdymo.

### -3- Įrankių sąrašo valdymas

Toliau, norint valdyti įrankių sąrašą, reikia nustatyti užklausų valdiklį. Štai ką būtina pridėti į mūsų serverio failą:

**Python**

```python
# kodas dėl trumpumo praleistas
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

Čia pridedame dekoratorių `@server.list_tools` ir įgyvendiname funkciją `handle_list_tools`. Pastarojoje reikia sukurti įrankių sąrašą. Atkreipkite dėmesį, kad kiekvienas įrankis turi turėti name, description ir inputSchema.   

**TypeScript**

Norint nustatyti užklausų valdiklį įrankių išvardinimui, serveryje kviečiame `setRequestHandler` su schema, atitinkančia mūsų tikslą, šiuo atveju `ListToolsRequestSchema`. 

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
  // Grąžinti registruotų įrankių sąrašą
  return {
    tools: tools
  };
});
```

Puiku, dabar, kai išsprendėme įrankių išvardinimą, pažiūrėkime, kaip galima kvietinėti įrankius.

### -4- Įrankio kvietimo valdymas

Norint kvieti įrankį, reikia nustatyti dar vieną užklausų valdiklį, kuris apdorotų užklausą, nurodančią, kurią funkciją kviečiame ir su kokiais argumentais.

**Python**

Naudosime dekoratorių `@server.call_tool` ir įgyvendinsime jį funkcija `handle_call_tool`. Joje turime išanalizuoti įrankio pavadinimą, argumentą ir užtikrinti, kad argumentai yra galiojantys atitinkamam įrankiui. Validaciją galime atlikti čia arba vėlesniame įrankio kvietime.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kuriame įrankių pavadinimai yra kaip raktažodžiai
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

Štai kaip tai veikia:

- Mūsų įrankio pavadinimas jau yra įvesties parametre `name`, o argumentai yra `arguments` žodyne.

- Įrankis kviečiamas kaip `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentų validacija vyksta `handler` ypatybėje – ji nurodo funkciją, jei validacija nepavyksta, bus išmesta klaida.

Taigi, dabar turime pilną supratimą apie įrankių išvardinimą ir kvietimą naudojant žemo lygio serverį.

Žr. [pilną pavyzdį](./code/README.md)

## Užduotis

Išplėskite gautą kodą pridėdami keletą įrankių, išteklių ir užklausų ir pastebėkite, kad jums reikia pridėti failus tik į tools katalogą ir niekur kitur.

*Sprendimas nepateiktas*

## Santrauka

Šiame skyriuje pamatėme, kaip veikia žemo lygio serverio metodas ir kaip jis leidžia sukurti tvarkingą architektūrą, kurią galima toliau plėsti. Taip pat aptarėme validaciją ir parodyta, kaip naudoti validacijos bibliotekas kuriant įvesties schemas.

## Kas toliau

- Toliau: [Paprasta autentifikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
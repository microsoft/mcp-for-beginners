# Išplėstinis serverio naudojimas

MCP SDK yra du skirtingi serverių tipai – jūsų įprastas serveris ir žemo lygio serveris. Paprastai naudotumėte įprastą serverį, kad jam pridėtumėte funkcijų. Tačiau tam tikrais atvejais norėsite pasikliauti žemo lygio serveriu, pavyzdžiui:

- Geresnė architektūra. Galima sukurti švarią architektūrą naudojant tiek įprastą, tiek žemo lygio serverį, bet galima teigti, kad žemo lygio serverio naudojimas šiek tiek lengvesnis.
- Funkcijų prieinamumas. Kai kurios pažangios funkcijos gali būti naudojamos tik su žemo lygio serveriu. Tai pamatysite vėlesniuose skyriuose pridėdami imtį ir išgavimą.

## Įprastas serveris prieš žemo lygio serverį

Štai kaip atrodo MCP serverio kūrimas naudojant įprastą serverį

**Python**

```python
mcp = FastMCP("Demo")

# Pridėti sudėjimo įrankį
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

Esminis dalykas yra tas, kad jūs aiškiai pridedate kiekvieną įrankį, išteklių ar užklausą, kurią norite, kad serveris turėtų. Tai nėra blogai.

### Žemo lygio serverio požiūris

Tačiau naudojant žemo lygio serverio požiūrį reikia mąstyti kitaip. Vietoj kiekvieno įrankio registravimo, jūs sukuriate du valdiklius kiekvienam funkcijų tipui (įrankiams, ištekliams arba užklausoms). Pavyzdžiui, įrankiai turi tik dvi funkcijas:

- Visų įrankių sąrašo pateikimas. Viena funkcija atsakinga už visus užklausimus pateikti įrankių sąrašą.
- Įrankių kvietimo valdymas. Čia taip pat tik viena funkcija valdo kvietimus į įrankį.

Skamba kaip mažiau darbo, tiesa? Taigi, vietoj įrankio registravimo, tiesiog reikia užtikrinti, kad įrankis būtų įtrauktas į įrankių sąrašą ir būtų iškviečiamas gavus atitinkamą kvietimą.

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

Čia turime funkciją, kuri grąžina funkcijų sąrašą. Kiekviename įrankių sąrašo įraše dabar yra laukai, tokie kaip `name`, `description` ir `inputSchema`, atitinkantys grąžinimo tipą. Tai leidžia įrankius ir funkcijų aprašymus talpinti kitur. Dabar galime sukurti visus įrankius įrankių aplanke, taip pat ir visos kitos funkcijos galės būti savo atitinkamuose aplankuose, tad jūsų projektas gali būti organizuotas tokia struktūra:

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

Puiku, mūsų architektūra gali būti labai švari.

O kaip su įrankių kvietimu, ar tai ta pati idėja – vienas valdiklis kviečia įrankį, bet kurį įrankį? Taip, tiksliai, čia kodas šiai daliai:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kuriame raktai yra įrankių pavadinimai
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
    // ATLIKTI iškviesti įrankį,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kaip matote iš aukščiau esančio kodo, turime išskaidyti, kurį įrankį kviečiame, su kokiais argumentais, tada tęsti įrankio iškvietimą.

## Požiūrio tobulinimas su validacija

Iki šiol matėte, kaip visus registravimus – įrankių, išteklių ir užklausų – galima pakeisti šiais dviem valdikliais kiekvienam funkcijų tipui. Ką dar turime padaryti? Reikia pridėti validaciją, kad užtikrintume, jog įrankis kviečiamas su tinkamais argumentais. Kiekviena vykdymo aplinka turi savo sprendimą, pavyzdžiui, Python naudoja Pydantic, o TypeScript – Zod. Idėja yra tokia:

- Perkelti funkcijų (įrankių, išteklių ar užklausų) kūrimo logiką į atskirą aplanką.
- Pridėti galimybę patikrinti gaunamą užklausą, pvz., tikrinant įrankio iškvietimą.

### Sukurti funkciją

Norint sukurti funkciją, turime sukurti failą šiai funkcijai ir įsitikinti, kad jame yra privalomi to funkcijos laukai. Šie laukai šiek tiek skiriasi tarp įrankių, išteklių ir užklausų.

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
        # Patikrinti įvestį naudojant Pydantic modelį
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

Čia matote, kaip atliekame šiuos veiksmus:

- Sukuriame schemą naudodami Pydantic `AddInputModel` su laukais `a` ir `b` faile *schema.py*.
- Bandoma išanalizuoti gaunamą užklausą kaip `AddInputModel` tipą; jei parametrai neatitinka, kils klaida:

   ```python
   # add.py
    try:
        # Patvirtinkite įvestį naudodami Pydantic modelį
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Galite pasirinkti, ar šią analizės logiką dėti tiesiai į įrankio kvietimą, ar į valdiklio funkciją.

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

- Valdiklyje, kuris apdoroja visus įrankių kvietimus, dabar bandoma išanalizuoti gaunamą užklausą pagal įrankio aprašytą schemą:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jeigu tai sėkminga, tęsime pats įrankio kvietimas:

    ```typescript
    const result = await tool.callback(input);
    ```

Kaip matote, šis požiūris sukuria puikią architektūrą, nes viskas yra savo vietoje: *server.ts* yra labai mažas failas, kuris tik suriša užklausų valdiklius, o kiekviena funkcija yra savo atskirame aplanke, pvz., tools/, resources/ arba /prompts.

Puiku, pabandykime tai sukurti dabar.

## Užduotis: Žemo lygio serverio kūrimas

Šioje užduotyje darysime šiuos dalykus:

1. Sukursime žemo lygio serverį, kuris tvarkys įrankių sąrašo pateikimą ir įrankių kvietimą.
1. Įgyvendinsime architektūrą, kurią galėsite plėsti.
1. Pridėsime validaciją, kad įrankių kvietimai būtų teisingai tikrinami.

### -1- Sukurti architektūrą

Pirmiausia reikia paruošti architektūrą, kuri padės mums augti, kai pridėsime daugiau funkcijų. Štai kaip ji atrodo:

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

Dabar turime architektūrą, kuri užtikrina, kad galėsime lengvai pridėti naujus įrankius į tools aplanką. Galite papildomai sukurti subaplankus ištekliams ir užklausoms.

### -2- Įrankio kūrimas

Pažiūrėkime, kaip atrodo įrankio kūrimas. Pirmiausia jis turi būti sukurtas savo *tool* aplanke taip:

**Python**

```python
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

Čia matome, kaip apibrėžiame pavadinimą, aprašymą ir įvesties schemą naudodami Pydantic bei valdiklį, kuris bus kviečiamas įrankiui iškviesti. Galiausiai viešiname `tool_add`, kuris yra žodynas su visomis šiomis savybėmis.

Taip pat yra *schema.py*, kuriame apibrėžiama įvesties schema, naudojama mūsų įrankyje:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Taip pat turime užpildyti *__init__.py*, kad įrankių katalogas būtų laikomas moduliu. Papildomai reikia viešinti modulius, kaip čia:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Galime šį failą pildyti, kai pridedame daugiau įrankių.

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

Čia kuriame žodyną, sudarytą iš savybių:

- name – įrankio pavadinimas.
- rawSchema – Zod schema, skirta tikrinti gaunamas užklausas įrankiui iškviesti.
- inputSchema – schema, kurią naudoja valdiklis.
- callback – funkcija, kuri kviečia įrankį.

Taip pat yra `Tool` tipas, kuris paverčia šį žodyną į tipą, kurį priima MCP serverio valdiklis, taip:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ir yra *schema.ts*, kur kaupiame įvesties schemas kiekvienam įrankiui, kuri šiuo metu atrodo taip ir turi tik vieną schemą, bet kai pridedame įrankių, pridedame daugiau įrašų:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Puiku, dabar pereikime prie mūsų įrankių sąrašo pateikimo tvarkymo.

### -3- Tvarkyti įrankių sąrašo pateikimą

Toliau reikia sukurti užklausų valdiklį, kuris pateiks įrankių sąrašą. Štai ką reikia pridėti į serverio failą:

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

Čia pridedame dekoratorių `@server.list_tools` ir įgyvendinamą funkciją `handle_list_tools`. Joje reikia sukurti įrankių sąrašą. Kiekvienas įrankis turi turėti pavadinimą, aprašymą ir inputSchema.

**TypeScript**

Norėdami nustatyti užklausų valdiklį įrankių sąrašui, kviečiame `setRequestHandler` serveryje su schema, atitinkančia mūsų tikslą, šiuo atveju `ListToolsRequestSchema`.

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
// Kodo dalis pateikta sutrumpintai
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Grąžina užregistruotų įrankių sąrašą
  return {
    tools: tools
  };
});
```

Puiku, dabar jau išsprendėme įrankių sąrašo pateikimą, pažiūrėkime, kaip galėtume kvieti įrankius.

### -4- Tvarkyti įrankio kvietimą

Norėdami iškviesti įrankį, turime nustatyti kitą užklausų valdiklį, kuris tvarkys užklausas su informacija, kurį funkcionalumą kviečiame ir su kokiais argumentais.

**Python**

Naudosime dekoratorių `@server.call_tool` ir įgyvendinsime funkciją, pvz., `handle_call_tool`. Šioje funkcijoje reikia išanalizuoti įrankio pavadinimą, argumentus ir užtikrinti, kad argumentai atitiktų įrankio reikalavimus. Galime validuoti argumentus čia arba pačiame įrankyje.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools yra žodynas, kuriame kaip raktai naudojami įrankių pavadinimai
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

Čia vyksta:

- Įrankio pavadinimas gaunamas per įvesties parametrą `name`, o argumentai kaip žodynas `arguments`.

- Įrankis kviečiamas su `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentų validacija vyksta funkcinėje `handler` savybėje, kuri rodo į funkciją, o klaida iškeliama, jei validacija nepavyksta.

Taigi, dabar pilnai suprantame, kaip naudoti žemo lygio serverį įrankių sąrašo pateikimui ir kvietimams.

Žr. [pilną pavyzdį](./code/README.md) čia

## Užduotis

Išplėskite pateiktą kodą pridėdami keletą įrankių, išteklių ir užklausų ir įvertinkite, kaip pastebite, kad tereikia pridėti failus tik į tools katalogą ir niekur kitur.

*Nėra pateikto sprendimo*

## Santrauka

Šiame skyriuje pamatėme, kaip veikia žemo lygio serverio požiūris ir kaip jis gali padėti sukurti patogią architektūrą, ant kurios galima augti. Taip pat aptarėme validaciją ir buvo parodyta, kaip naudotis validavimo bibliotekomis kuriant įvesties validacijos schemas.

## Kas toliau

- Toliau: [Paprastas autentifikavimas](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai, rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus interpretavimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
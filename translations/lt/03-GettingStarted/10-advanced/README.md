# Išplėstinis serverio naudojimas

MCP SDK pateikia du skirtingus serverių tipus: įprastą serverį ir žemo lygio serverį. Paprastai naudojate įprastą serverį, kad pridėtumėte funkcijų. Tačiau kai kuriais atvejais verta pasikliauti žemo lygio serveriu, pavyzdžiui:

- Geresnė architektūra. Nors švarią architektūrą galima sukurti tiek naudojant įprastą, tiek žemo lygio serverį, galima teigti, kad su žemo lygio serveriu tai padaryti šiek tiek lengviau.
- Funkcijų prieinamumas. Kai kurios pažangios funkcijos gali būti naudojamos tik su žemo lygio serveriu. Tai pamatysite vėlesniuose skyriuose, kai pridėsime mėginių ėmimą ir elicitaciją.

## Įprastas serveris vs žemo lygio serveris

Štai kaip atrodo MCP serverio kūrimas naudojant įprastą serverį:

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

Esmė ta, kad aiškiai pridedate kiekvieną įrankį, resursą ar užklausą, kurią norite turėti serveryje. Tai visiškai normalu.

### Žemo lygio serverio metodas

Tačiau naudojant žemo lygio serverio metodą reikia galvoti kitaip. Vietoj to, kad registruotumėte kiekvieną įrankį, jūs sukuriate du tvarkytuvus kiekvienam funkcijų tipui (įrankiai, resursai ar užklausos). Pavyzdžiui, įrankiams yra tik dvi funkcijos:

- Visų įrankių sąrašas. Viena funkcija atsakinga už visus bandymus pateikti įrankių sąrašą.
- Visų įrankių iškvietimas. Čia taip pat yra tik viena funkcija, tvarkanti įrankio iškvietimus.

Skamba kaip mažiau darbo, tiesa? Vietoj to, kad registruotumėte įrankį, jums tereikia užtikrinti, kad įrankis būtų įtrauktas į sąrašą, kai pateikiamas visų įrankių sąrašas, ir kad jis būtų iškviečiamas, kai gaunamas prašymas iškviesti įrankį.

Pažvelkime, kaip dabar atrodo kodas:

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

Čia turime funkciją, kuri grąžina funkcijų sąrašą. Kiekvienas įrašas įrankių sąraše dabar turi laukus, tokius kaip `name`, `description` ir `inputSchema`, kad atitiktų grąžinimo tipą. Tai leidžia mums perkelti įrankių ir funkcijų apibrėžimą kitur. Dabar galime sukurti visus savo įrankius atskirame įrankių aplanke, o tas pats galioja visoms funkcijoms, todėl projektas gali būti organizuotas taip:

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

Puiku, mūsų architektūra gali atrodyti gana švari.

O kaip dėl įrankių iškvietimo? Ar tai ta pati idėja – vienas tvarkytuvas, skirtas bet kokiam įrankiui iškviesti? Taip, būtent, štai kodas:

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

Kaip matote iš aukščiau pateikto kodo, reikia išanalizuoti, kurį įrankį iškviesti ir su kokiais argumentais, o tada tęsti įrankio iškvietimą.

## Požiūrio tobulinimas su validacija

Iki šiol matėte, kaip visus registracijos veiksmus, skirtus įrankiams, resursams ir užklausoms pridėti, galima pakeisti šiais dviem tvarkytuvais kiekvienam funkcijų tipui. Ką dar reikia padaryti? Na, turėtume pridėti tam tikrą validaciją, kad užtikrintume, jog įrankis iškviečiamas su tinkamais argumentais. Kiekviena vykdymo aplinka turi savo sprendimą, pavyzdžiui, Python naudoja Pydantic, o TypeScript – Zod. Idėja yra tokia:

- Perkelti logiką, skirtą funkcijai (įrankiui, resursui ar užklausai) sukurti, į jai skirtą aplanką.
- Pridėti būdą patikrinti gaunamą prašymą, pavyzdžiui, iškviesti įrankį.

### Funkcijos kūrimas

Norėdami sukurti funkciją, turėsime sukurti failą tai funkcijai ir užtikrinti, kad jame būtų privalomi laukai, reikalingi tai funkcijai. Kokie laukai reikalingi, šiek tiek skiriasi tarp įrankių, resursų ir užklausų.

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

Čia matote, kaip mes darome:

- Sukuriame schemą naudodami Pydantic `AddInputModel` su laukais `a` ir `b` faile *schema.py*.
- Bandome analizuoti gaunamą prašymą, kad jis atitiktų `AddInputModel` tipą. Jei parametrai nesutampa, tai sukels klaidą:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Galite pasirinkti, ar šią analizės logiką įdėti į patį įrankio iškvietimą, ar į tvarkytuvo funkciją.

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

- Tvarkytuve, kuris tvarko visus įrankių iškvietimus, bandome analizuoti gaunamą prašymą pagal įrankio apibrėžtą schemą:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    jei tai veikia, tęsiame faktinio įrankio iškvietimą:

    ```typescript
    const result = await tool.callback(input);
    ```

Kaip matote, šis požiūris sukuria puikią architektūrą, kurioje viskas turi savo vietą, *server.ts* yra labai mažas failas, kuris tik sujungia prašymų tvarkytuvus, o kiekviena funkcija yra savo atitinkamame aplanke, pvz., tools/, resources/ arba /prompts.

Puiku, pabandykime tai sukurti.

## Pratimai: žemo lygio serverio kūrimas

Šiame pratime atliksime šiuos veiksmus:

1. Sukursime žemo lygio serverį, kuris tvarkys įrankių sąrašą ir jų iškvietimą.
1. Įgyvendinsime architektūrą, kurią galėsite plėsti.
1. Pridėsime validaciją, kad užtikrintume, jog įrankių iškvietimai yra tinkamai patikrinti.

### -1- Architektūros kūrimas

Pirmiausia turime sukurti architektūrą, kuri padėtų mums plėstis, kai pridėsime daugiau funkcijų. Štai kaip tai atrodo:

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

Dabar turime architektūrą, kuri užtikrina, kad galime lengvai pridėti naujus įrankius į įrankių aplanką. Galite laisvai pridėti subkatalogus resursams ir užklausoms.

### -2- Įrankio kūrimas

Pažiūrėkime, kaip atrodo įrankio kūrimas. Pirmiausia jis turi būti sukurtas savo *tool* subkataloge, pavyzdžiui:

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

Čia matome, kaip apibrėžiame pavadinimą, aprašymą, įvesties schemą naudodami Pydantic ir tvarkytuvą, kuris bus iškviečiamas, kai šis įrankis bus naudojamas. Galiausiai, mes eksponuojame `tool_add`, kuris yra žodynas, turintis visas šias savybes.

Taip pat yra *schema.py*, kuris naudojamas apibrėžti įvesties schemą, naudojamą mūsų įrankyje:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Taip pat turime užpildyti *__init__.py*, kad užtikrintume, jog įrankių katalogas būtų traktuojamas kaip modulis. Be to, turime eksponuoti modulius jame, pavyzdžiui:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Galime tęsti šio failo pildymą, kai pridėsime daugiau įrankių.

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

Čia sukuriame žodyną, sudarytą iš savybių:

- name – tai įrankio pavadinimas.
- rawSchema – tai Zod schema, ji bus naudojama patikrinti gaunamus prašymus iškviesti šį įrankį.
- inputSchema – ši schema bus naudojama tvarkytuve.
- callback – tai naudojama įrankio iškvietimui.

Taip pat yra `Tool`, kuris naudojamas konvertuoti šį žodyną į tipą, kurį MCP serverio tvarkytuvas gali priimti, ir jis atrodo taip:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Ir yra *schema.ts*, kur saugome įvesties schemas kiekvienam įrankiui, kuris atrodo taip, šiuo metu turint tik vieną schemą, bet pridėdami įrankius galime pridėti daugiau įrašų:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Puiku, pereikime prie įrankių sąrašo tvarkymo.

### -3- Įrankių sąrašo tvarkymas

Norėdami tvarkyti įrankių sąrašą, turime nustatyti prašymo tvarkytuvą. Štai ką reikia pridėti prie mūsų serverio failo:

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

Čia pridedame dekoratorių `@server.list_tools` ir įgyvendiname funkciją `handle_list_tools`. Pastarojoje turime pateikti įrankių sąrašą. Atkreipkite dėmesį, kad kiekvienas įrankis turi turėti pavadinimą, aprašymą ir inputSchema.

**TypeScript**

Norėdami nustatyti prašymo tvarkytuvą įrankių sąrašui, turime iškviesti `setRequestHandler` serveryje su schema, atitinkančia tai, ką bandome padaryti, šiuo atveju `ListToolsRequestSchema`.

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

Puiku, dabar išsprendėme įrankių sąrašo dalį, pažiūrėkime, kaip galėtume iškviesti įrankius.

### -4- Įrankio iškvietimo tvarkymas

Norėdami iškviesti įrankį, turime nustatyti kitą prašymo tvarkytuvą, šį kartą skirtą prašymui, nurodančiam, kurią funkciją iškviesti ir su kokiais argumentais.

**Python**

Naudokime dekoratorių `@server.call_tool` ir įgyvendinkime jį funkcijoje, pavyzdžiui, `handle_call_tool`. Šioje funkcijoje turime išanalizuoti įrankio pavadinimą, jo argumentus ir užtikrinti, kad argumentai būtų tinkami tam įrankiui. Galime patikrinti argumentus šioje funkcijoje arba toliau pačiame įrankyje.

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

Štai kas vyksta:

- Mūsų įrankio pavadinimas jau yra kaip įvesties parametras `name`, tas pats pasakytina apie argumentus, pateiktus kaip `arguments` žodynas.

- Įrankis iškviečiamas su `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Argumentų validacija vyksta `handler` savybėje, kuri nurodo funkciją. Jei tai nepavyksta, bus iškelta išimtis.

Štai, dabar turime pilną supratimą apie įrankių sąrašą ir jų iškvietimą naudojant žemo lygio serverį.

Žiūrėkite [pilną pavyzdį](./code/README.md) čia.

## Užduotis

Papildykite jums pateiktą kodą keliais įrankiais, resursais ir užklausomis ir apmąstykite, kaip pastebite, kad jums tereikia pridėti failus į įrankių katalogą ir niekur kitur.

*Sprendimas nepateiktas*

## Santrauka

Šiame skyriuje aptarėme, kaip veikia žemo lygio serverio metodas ir kaip jis gali padėti sukurti gražią architektūrą, kurią galima toliau plėsti. Taip pat aptarėme validaciją ir jums buvo parodyta, kaip dirbti su validacijos bibliotekomis, kad sukurtumėte schemas įvesties validacijai.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
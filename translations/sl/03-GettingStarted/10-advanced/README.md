# Napredna uporaba strežnika

V MCP SDK sta na voljo dva različna tipa strežnikov: običajni strežnik in strežnik na nizki ravni. Običajno uporabljate običajni strežnik za dodajanje funkcionalnosti. V nekaterih primerih pa se boste morda želeli zanašati na strežnik na nizki ravni, na primer:

- Boljša arhitektura. Možno je ustvariti čisto arhitekturo tako z običajnim kot s strežnikom na nizki ravni, vendar bi lahko trdili, da je to nekoliko lažje s strežnikom na nizki ravni.
- Razpoložljivost funkcij. Nekatere napredne funkcije so na voljo samo s strežnikom na nizki ravni. To boste videli v kasnejših poglavjih, ko bomo dodajali vzorčenje in pridobivanje podatkov.

## Običajni strežnik vs strežnik na nizki ravni

Tako izgleda ustvarjanje MCP strežnika z običajnim strežnikom:

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

Ključno je, da eksplicitno dodate vsako orodje, vir ali poziv, ki ga želite imeti na strežniku. Nič narobe s tem.

### Pristop strežnika na nizki ravni

Ko pa uporabljate pristop strežnika na nizki ravni, morate razmišljati drugače, in sicer namesto registracije vsakega orodja ustvarite dva obdelovalca za vsak tip funkcije (orodja, viri ali pozivi). Na primer, za orodja obstajata samo dve funkciji, kot sledi:

- Seznam vseh orodij. Ena funkcija je odgovorna za vse poskuse seznamov orodij.
- Obdelava klicev vseh orodij. Tudi tukaj obstaja samo ena funkcija, ki obravnava klice orodja.

To se sliši kot potencialno manj dela, kajne? Namesto registracije orodja moram samo zagotoviti, da je orodje navedeno, ko navajam vsa orodja, in da se pokliče, ko pride zahteva za klic orodja.

Poglejmo, kako zdaj izgleda koda:

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

Tukaj imamo funkcijo, ki vrne seznam funkcij. Vsak vnos v seznamu orodij zdaj vsebuje polja, kot so `name`, `description` in `inputSchema`, da ustreza vrsti vrnitve. To nam omogoča, da naša orodja in definicije funkcij postavimo drugam. Zdaj lahko ustvarimo vsa naša orodja v mapi orodij, enako pa velja za vse vaše funkcije, tako da je vaš projekt nenadoma organiziran takole:

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

Odlično, naša arhitektura je lahko videti precej čista.

Kaj pa klicanje orodij, je potem ista ideja, en obdelovalec za klic orodja, ne glede na to, katero orodje? Da, točno tako, tukaj je koda za to:

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

Kot lahko vidite iz zgornje kode, moramo razčleniti orodje za klicanje in s katerimi argumenti, nato pa nadaljevati s klicanjem orodja.

## Izboljšanje pristopa z validacijo

Do sedaj ste videli, kako lahko vse vaše registracije za dodajanje orodij, virov in pozivov nadomestite s tema dvema obdelovalcema na tip funkcije. Kaj še moramo storiti? No, dodati bi morali neko obliko validacije, da zagotovimo, da je orodje poklicano s pravimi argumenti. Vsako okolje ima svojo rešitev za to, na primer Python uporablja Pydantic, TypeScript pa Zod. Ideja je, da naredimo naslednje:

- Premaknemo logiko za ustvarjanje funkcije (orodja, vira ali poziva) v njeno namensko mapo.
- Dodamo način za validacijo dohodne zahteve, ki na primer zahteva klic orodja.

### Ustvarjanje funkcije

Za ustvarjanje funkcije moramo ustvariti datoteko za to funkcijo in zagotoviti, da ima obvezna polja, ki jih zahteva ta funkcija. Katera polja se razlikujejo med orodji, viri in pozivi.

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

Tukaj lahko vidite, kako naredimo naslednje:

- Ustvarimo shemo z uporabo Pydantic `AddInputModel` s polji `a` in `b` v datoteki *schema.py*.
- Poskusimo razčleniti dohodno zahtevo, da je tipa `AddInputModel`, če pride do neskladja v parametrih, bo to povzročilo napako:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Lahko se odločite, ali želite to logiko razčlenjevanja postaviti v sam klic orodja ali v funkcijo obdelovalca.

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

- V obdelovalcu, ki obravnava vse klice orodij, zdaj poskušamo razčleniti dohodno zahtevo v shemo, ki jo je določilo orodje:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    če to deluje, nadaljujemo s klicanjem dejanskega orodja:

    ```typescript
    const result = await tool.callback(input);
    ```

Kot lahko vidite, ta pristop ustvarja odlično arhitekturo, saj ima vse svoje mesto, *server.ts* je zelo majhna datoteka, ki samo povezuje obdelovalce zahtev, vsaka funkcija pa je v svoji ustrezni mapi, tj. tools/, resources/ ali /prompts.

Odlično, poskusimo to zgraditi naslednjič.

## Vaja: Ustvarjanje strežnika na nizki ravni

V tej vaji bomo naredili naslednje:

1. Ustvarili strežnik na nizki ravni, ki obravnava seznam orodij in klicanje orodij.
1. Implementirali arhitekturo, na kateri lahko gradite.
1. Dodali validacijo, da zagotovimo, da so vaši klici orodij pravilno validirani.

### -1- Ustvarjanje arhitekture

Prva stvar, ki jo moramo obravnavati, je arhitektura, ki nam pomaga pri skaliranju, ko dodajamo več funkcij. Tukaj je, kako izgleda:

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

Zdaj imamo arhitekturo, ki zagotavlja, da lahko zlahka dodajamo nova orodja v mapo orodij. Po želji lahko sledite temu, da dodate podmape za vire in pozive.

### -2- Ustvarjanje orodja

Poglejmo, kako izgleda ustvarjanje orodja. Najprej ga je treba ustvariti v njegovi podmapi *tool*, kot sledi:

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

Tukaj vidimo, kako definiramo ime, opis, vhodno shemo z uporabo Pydantic in obdelovalca, ki bo poklican, ko bo to orodje uporabljeno. Na koncu izpostavimo `tool_add`, ki je slovar, ki vsebuje vse te lastnosti.

Obstaja tudi *schema.py*, ki se uporablja za definiranje vhodne sheme, ki jo uporablja naše orodje:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Prav tako moramo napolniti *__init__.py*, da zagotovimo, da se mapa orodij obravnava kot modul. Poleg tega moramo izpostaviti module znotraj nje, kot sledi:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

To datoteko lahko še naprej dopolnjujemo, ko dodajamo več orodij.

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

Tukaj ustvarimo slovar, ki vsebuje lastnosti:

- name, to je ime orodja.
- rawSchema, to je Zod shema, ki se bo uporabljala za validacijo dohodnih zahtev za klic tega orodja.
- inputSchema, to shemo bo uporabljal obdelovalec.
- callback, to se uporablja za klicanje orodja.

Obstaja tudi `Tool`, ki se uporablja za pretvorbo tega slovarja v tip, ki ga lahko sprejme obdelovalec strežnika MCP, in izgleda takole:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

In obstaja *schema.ts*, kjer shranjujemo vhodne sheme za vsako orodje, ki trenutno izgleda tako z eno samo shemo, vendar lahko dodajamo več vnosov, ko dodajamo orodja:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Odlično, nadaljujmo z obravnavo seznama naših orodij.

### -3- Obravnava seznama orodij

Naslednje, za obravnavo seznama naših orodij, moramo nastaviti obdelovalec zahtev za to. Tukaj je, kaj moramo dodati v našo datoteko strežnika:

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

Tukaj dodamo dekorator `@server.list_tools` in implementacijsko funkcijo `handle_list_tools`. V slednji moramo ustvariti seznam orodij. Opazite, kako mora imeti vsako orodje ime, opis in inputSchema.

**TypeScript**

Za nastavitev obdelovalca zahtev za seznam orodij moramo poklicati `setRequestHandler` na strežniku s shemo, ki ustreza temu, kar poskušamo narediti, v tem primeru `ListToolsRequestSchema`.

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

Odlično, zdaj smo rešili del seznama orodij, poglejmo, kako bi lahko naslednje klicali orodja.

### -4- Obravnava klicanja orodja

Za klicanje orodja moramo nastaviti še en obdelovalec zahtev, tokrat osredotočen na obravnavo zahteve, ki določa, katero funkcijo poklicati in s katerimi argumenti.

**Python**

Uporabimo dekorator `@server.call_tool` in ga implementirajmo s funkcijo, kot je `handle_call_tool`. Znotraj te funkcije moramo razčleniti ime orodja, njegove argumente in zagotoviti, da so argumenti veljavni za zadevno orodje. Argumente lahko validiramo bodisi v tej funkciji bodisi v nadaljevanju v dejanskem orodju.

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

Tukaj se dogaja naslednje:

- Ime našega orodja je že prisotno kot vhodni parameter `name`, kar velja tudi za naše argumente v obliki slovarja `arguments`.

- Orodje se pokliče z `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumentov se zgodi v lastnosti `handler`, ki kaže na funkcijo, če to ne uspe, bo sprožila izjemo.

Tako, zdaj imamo popolno razumevanje seznama in klicanja orodij z uporabo strežnika na nizki ravni.

Celoten primer si oglejte [tukaj](./code/README.md).

## Naloga

Razširite kodo, ki ste jo prejeli, z več orodji, viri in pozivi ter razmislite, kako opazite, da morate dodajati datoteke samo v mapo orodij in nikjer drugje.

*Rešitev ni podana*

## Povzetek

V tem poglavju smo videli, kako deluje pristop strežnika na nizki ravni in kako nam lahko pomaga ustvariti lepo arhitekturo, na kateri lahko še naprej gradimo. Prav tako smo razpravljali o validaciji in pokazali smo vam, kako delati z validacijskimi knjižnicami za ustvarjanje shem za validacijo vhodnih podatkov.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
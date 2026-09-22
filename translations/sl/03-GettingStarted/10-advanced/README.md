# Napredna uporaba strežnika

V SDK MCP so na voljo dva različna tipa strežnikov, vaš običajni strežnik in nizkonivojski strežnik. Običajno bi uporabili običajni strežnik za dodajanje funkcij. V nekaterih primerih pa boste želeli uporabiti nizkonivojski strežnik, kot so:

- Boljša arhitektura. Možno je ustvariti čisto arhitekturo z obema, običajnim in nizkonivojskim strežnikom, vendar se lahko argumentira, da je to nekoliko lažje z nizkonivojskim strežnikom.
- Razpoložljivost funkcij. Nekatere napredne funkcije je mogoče uporabiti samo z
    nizkonivojskim strežnikom. Kasnejša poglavja pokrivajo Elicitation in legacy Sampling
    funkcijo, ki je v MCP `2026-07-28` odsvetovana.

## Običajni strežnik vs nizkonivojski strežnik

Tako izgleda ustvarjanje MCP strežnika z običajnim strežnikom

**Python**

```python
mcp = FastMCP("Demo")

# Dodajte orodje za seštevanje
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

// Dodajte orodje za seštevanje
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

Namen je, da izrecno dodate vsak pripomoček, vir ali poziv, ki ga želite, da ga strežnik ima. Ni s tem nič narobe.  

### Pristop nizkonivojskega strežnika

Ko pa uporabite pristop nizkonivojskega strežnika, morate o tem razmišljati drugače. Namesto da registrirate vsak pripomoček, ustvarite dva upravljavca na tip funkcije (pripomočki, viri ali pozivi). Torej na primer pripomočki imajo samo dve funkciji tako:

- Seznam vseh pripomočkov. Ena funkcija bi bila odgovorna za vse poskuse za seznam pripomočkov.
- upravljanje klicev pripomočkov. Tukaj je tudi samo ena funkcija, ki upravlja klice pripomočka.

Zveni kot manj dela, kajne? Namesto registracije pripomočka moram samo zagotoviti, da je pripomoček naveden, ko seznamujem vse pripomočke in da je klican, ko prispe zahteva za klic pripomočka. 

Poglejmo, kako koda zdaj izgleda:

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
  // Vrni seznam registriranih orodij
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

Zdaj imamo funkcijo, ki vrne seznam funkcij. Vsak vnos na seznamu pripomočkov ima polja kot so `name`, `description` in `inputSchema`, da ustreza tipu vrnitve. To omogoča, da naše pripomočke in definicijo funkcij postavimo drugam. Vse naše pripomočke lahko sedaj ustvarimo v mapi tools, enako velja za vse vaše funkcije, tako da je vaš projekt lahko zlahka organiziran tako:

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

To je super, naša arhitektura je lahko precej čista.

Kaj pa klicanje pripomočkov, enaka ideja, en upravljalec za klic pripomočka, ne glede na katero? Da, točno tako, tukaj je koda za to:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovar z imeni orodij kot ključi
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
    // TODO pokliči orodje,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kot lahko vidite iz zgornje kode, moramo razčleniti, kateri pripomoček poklicati in s kakšnimi argumenti, nato pa nadaljevati s klicem pripomočka.

## Izboljšanje pristopa z validacijo

Do zdaj ste videli, kako lahko vse vaše registracije za dodajanje pripomočkov, virov in pozivov nadomestite s tema dvema upravljalcema na tip funkcije. Kaj še moramo storiti? Dodati moramo neko obliko validacije, da zagotovimo, da je pripomoček poklican z ustreznimi argumenti. Vsak runtime ima svojo rešitev, na primer Python uporablja Pydantic, TypeScript pa Zod. Ideja je, da naredimo naslednje:

- Premaknemo logiko za ustvarjanje funkcije (pripomoček, vir ali poziv) v namensko mapo.
- Dodamo način za validacijo vhodnih zahtev, ki na primer prosijo za klic pripomočka.

### Ustvarjanje funkcije

Za ustvarjanje funkcije moramo ustvariti datoteko za to funkcijo in zagotoviti, da ima obvezna polja, ki jih ta funkcija potrebuje. Katera polja se razlikujejo med pripomočki, viri in pozivi.

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
        # Preveri vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, da lahko ustvarimo AddInputModel in preverimo argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

tukaj lahko vidite, kako naredimo naslednje:

- Ustvarimo shemo z uporabo Pydantic `AddInputModel` s polji `a` in `b` v datoteki *schema.py*.
- Poskušamo razčleniti vhodno zahtevo kot tip `AddInputModel`, če obstaja neujemanje parametrov, bo to povzročilo napako:

   ```python
   # add.py
    try:
        # Preverite vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Lahko se odločite, ali to logiko razčlenjevanja postavite v klic pripomočka ali v funkcijo upravljalca.

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

- V upravljalcu, ki obravnava vse klice pripomočkov, poskušamo zdaj razčleniti vhodno zahtevo v definirano shemo pripomočka:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    če to uspe, nadaljujemo s klicem dejanskega pripomočka:

    ```typescript
    const result = await tool.callback(input);
    ```

Kot vidite, ta pristop ustvarja odlično arhitekturo, saj ima vse svoje mesto, datoteka *server.ts* je zelo majhna in samo poveže upravljalce zahtev, vsaka funkcija pa je v svoji mapi, npr. tools/, resources/ ali /prompts.

Super, poskusimo to zdaj sestaviti. 

## Vaja: Ustvarjanje nizkonivojskega strežnika

V tej vaji bomo naredili naslednje:

1. Ustvarili nizkonivojski strežnik, ki upravlja seznam pripomočkov in klice pripomočkov.
1. Implementirali arhitekturo, na kateri lahko gradite.
1. Dodali validacijo, da zagotovimo pravilno preverjanje klicev pripomočkov.

### -1- Ustvarimo arhitekturo

Prva stvar, ki jo moramo urediti, je arhitektura, ki nam pomaga skalirati, ko dodajamo več funkcij, tako izgleda:

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

Zdaj smo postavili arhitekturo, ki zagotavlja, da lahko enostavno dodajamo nove pripomočke v mapo tools. Prosto dodajte tudi podmape za vire in pozive.

### -2- Ustvarjanje pripomočka

Poglejmo, kako izgleda ustvarjanje pripomočka. Najprej ga je treba ustvariti v njegovi podmapi *tool* tako:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Preveri vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, da lahko ustvarimo AddInputModel in preverimo argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tukaj vidimo, kako definiramo ime, opis in vhodno shemo z uporabo Pydantic in upravljalca, ki se bo poklical, ko se bo pripomoček klical. Nazadnje izpostavimo `tool_add`, ki je slovar z vsemi temi lastnostmi.

Obstaja tudi *schema.py*, ki se uporablja za definiranje vhodne sheme, ki jo uporablja naš pripomoček:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Prav tako moramo napolniti *__init__.py*, da zagotovimo, da se mapa tools obravnava kot modul. Poleg tega moramo izpostaviti module znotraj kot sledi:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

V to datoteko lahko še naprej dodajamo nove pripomočke.

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

- name, to je ime pripomočka.
- rawSchema, to je Zod shema, uporabi se za validacijo dohodnih zahtev za klic tega pripomočka.
- inputSchema, ta shema se uporablja v upravljalcu.
- callback, to se uporablja za klic pripomočka.

Obstaja tudi `Tool`, ki se uporablja za pretvorbo tega slovarja v tip, ki ga lahko sprejme mcp strežniški upravljalec in izgleda tako:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

In obstaja *schema.ts*, kjer hranimo vhodne sheme za vsak pripomoček, ki izgleda tako, trenutno samo s eno shemo, a ko dodajamo pripomočke, lahko dodamo več vnosov:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, nadaljujmo z upravljanjem seznama pripomočkov.

### -3- Upravljanje seznama pripomočkov

Nato, za upravljanje seznama pripomočkov, moramo nastaviti upravljalec zahtev za to. Tukaj je, kaj moramo dodati v našo strežniško datoteko:

**Python**

```python
# koda izpuščena zaradi jedrnatosti
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

Tukaj dodamo dekorator `@server.list_tools` in implementiramo funkcijo `handle_list_tools`. V slednji moramo ustvariti seznam pripomočkov. Opazite, da mora vsak pripomoček imeti ime, opis in inputSchema.   

**TypeScript**

Za nastavitev upravljalca zahtev za seznam pripomočkov, moramo poklicati `setRequestHandler` na strežniku s shemo, ki ustreza temu, kar želimo narediti, v tem primeru `ListToolsRequestSchema`. 

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
// koda je zaradi preglednosti izpuščena
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrni seznam registriranih orodij
  return {
    tools: tools
  };
});
```

Super, zdaj smo rešili del seznama pripomočkov, poglejmo, kako bi lahko naslednje klicali pripomočke.

### -4- Upravljanje klica pripomočka

Za klic pripomočka moramo nastaviti še en upravljalec zahtev, tokrat osredotočen na zahteve, ki določajo, katero funkcijo poklicati in s kakšnimi argumenti.

**Python**

Uporabimo dekorator `@server.call_tool` in ga implementiramo z funkcijo, kot je `handle_call_tool`. V tej funkciji moramo razčleniti ime pripomočka, njegove argumente in zagotoviti, da so argumenti veljavni za zadevni pripomoček. Argumente lahko validiramo bodisi v tej funkciji bodisi kasneje v dejanskem pripomočku.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je slovar z orodji kot ključi
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # pokliči orodje
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Tako to poteka:

- Naše ime pripomočka je že prisotno kot vhodni parameter `name`, kar velja tudi za argumente v obliki slovarja `arguments`.

- Pripomoček se kliče z `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumentov se zgodi v lastnosti `handler`, ki kaže na funkcijo, če to ne uspe, bo sprožila izjemo. 

Tako zdaj imamo popolno razumevanje seznama in klicev pripomočkov z nizkonivojskim strežnikom.

Oglejte si [popoln primer](./code/README.md) tukaj

## Naloga

Razširite dano kodo z več pripomočki, viri in pozivi in razmislite, kako opazite, da morate dodajati le datoteke v mapo tools in nikjer drugje. 

*Rešitev ni na voljo*

## Povzetek

V tem poglavju smo videli, kako deluje pristop nizkonivojskega strežnika in kako nam to lahko pomaga ustvariti lepo arhitekturo, na kateri lahko še naprej gradimo. Prav tako smo razpravljali o validaciji in vam prikazali, kako delati z knjižnicami za validacijo za ustvarjanje shem za validacijo vhodov.

## Kaj sledi

- Naslednje: [Preprosta avtentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Napredno upravljanje s strežnikom

V MCP SDK so na voljo dva različna tipa strežnikov, vaš običajni strežnik in nizkonivojski strežnik. Običajno bi za dodajanje funkcij uporabili običajni strežnik. V nekaterih primerih pa želite uporabiti nizkonivojski strežnik, na primer:

- Boljša arhitektura. Možno je ustvariti čisto arhitekturo z obema, običajnim in nizkonivojskim strežnikom, a lahko se trdi, da je to nekoliko lažje z nizkonivojskim strežnikom.
- Razpoložljivost funkcij. Nekatere napredne funkcije so na voljo samo z nizkonivojskim strežnikom. To boste videli v kasnejših poglavjih, ko bomo dodajali vzorčenje in vzbujanje.

## Običajni strežnik proti nizkonivojskemu strežniku

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

Pomembno je, da izrecno dodate vsak pripomoček, vir ali poziv, ki ga želite, da jih strežnik ima. V tem ni nič narobe.  

### Pristop nizkonivojskega strežnika

Ko pa uporabite pristop nizkonivojskega strežnika, morate razmišljati drugače. Namesto da registrirate vsak pripomoček, ustvarite dva obdelovalca za vsako vrsto funkcije (pripomočki, viri ali pozivi). Na primer, pripomočki imajo samo dve funkciji:

- Izpis vseh pripomočkov. Ena funkcija je odgovorna za vse poskuse izpisa pripomočkov.
- Obdelava klicev vseh pripomočkov. Tudi tukaj obstaja samo ena funkcija, ki obdeluje klice na pripomoček.

Zveni kot manj dela, kajne? Namesto da registriram pripomoček, moram samo zagotoviti, da je pripomoček na seznamu, ko navajam vse pripomočke, in da je poklican, ko pride zahteva za klic pripomočka. 

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

Tukaj imamo funkcijo, ki vrne seznam funkcij. Vsak vnos na seznamu pripomočkov ima polja, kot so `name`, `description` in `inputSchema`, da ustreza tipu vrnitve. To nam omogoča, da definicijo pripomočkov in funkcij hranimo kjerkoli drugje. Zdaj lahko vse naše pripomočke ustvarimo v mapi tools, enako velja za vse vaše funkcije, tako da je vaš projekt lahko organiziran takole:

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

Odlično, naša arhitektura je lahko precej čista.

Kaj pa klic pripomočkov, je to ista ideja, en obdelovalec za klic pripomočka, katerega koli pripomočka? Da, točno tako, tukaj je koda za to:

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
    // TODO pokličite orodje,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kot vidite v zgornji kodi, moramo razbrati, kateri pripomoček je treba poklicati in s katerimi argumenti, potem pa naprej klicati pripomoček.

## Izboljšava pristopa z validacijo

Do sedaj ste videli, kako lahko vse registracije za dodajanje pripomočkov, virov in pozivov nadomestite s tema dvema obdelovalcema za vsako vrsto funkcije. Kaj še moramo narediti? Dodati bi morali neko obliko validacije, da zagotovimo, da se pripomoček kliče z pravimi argumenti. Vsako okolje ima svojo rešitev za to, na primer Python uporablja Pydantic, TypeScript pa Zod. Ideja je, da naredimo naslednje:

- Premaknemo logiko za ustvarjanje funkcije (pripomoček, vir ali poziv) v njeno namensko mapo.
- Dodamo način za validacijo prihajajoče zahteve, na primer za klic pripomočka.

### Ustvarite funkcijo

Za ustvarjanje funkcije bomo morali ustvariti datoteko za to funkcijo in zagotoviti, da ima obvezna polja, ki jih zahteva funkcija. Katera polja so zahtevana, se nekoliko razlikujejo med pripomočki, viri in pozivi.

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
        # Preveri vhod z uporabo modela Pydantic
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

Tukaj je prikazano, kako naredimo naslednje:

- Ustvarimo shemo z uporabo Pydantic `AddInputModel` s polji `a` in `b` v datoteki *schema.py*.
- Poskusimo razčleniti prihajajočo zahtevo kot tip `AddInputModel`, če parametri ne ustrezajo, bo to povzročilo napako:

   ```python
   # add.py
    try:
        # Preveri vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Lahko se odločite, ali to logiko razčlenjevanja postavite v sam klic pripomočka ali v funkcijo obdelovalca.

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

- V obdelovalcu, ki upravlja klice vseh pripomočkov, zdaj poskušamo razčleniti prihajajočo zahtevo v shemo pripomočka:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    če to uspe, nadaljujemo s klicem pripomočka:

    ```typescript
    const result = await tool.callback(input);
    ```

Kot vidite, ta pristop ustvarja odlično arhitekturo, saj ima vse svoje mesto, *server.ts* je zelo majhna datoteka, ki poveže samo obdelovalce zahtev, vsaka funkcija pa je v svoji mapi, na primer tools/, resources/ ali prompts/.

Odlično, poskusimo to naslednje zgraditi.

## Vaja: Ustvarjanje nizkonivojskega strežnika

V tej vaji bomo naredili naslednje:

1. Ustvarili nizkonivojski strežnik, ki upravlja izpis pripomočkov in klic pripomočkov.
1. Implementirali arhitekturo, na katero lahko gradite.
1. Dodali validacijo, da zagotovimo pravilno validacijo klicev pripomočkov.

### -1- Ustvarite arhitekturo

Prvi korak je arhitektura, ki nam pomaga pri skaliranju z dodajanjem več funkcij, tako izgleda:

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

Zdaj smo vzpostavili arhitekturo, ki zagotavlja, da lahko preprosto dodajamo nove pripomočke v mapo tools. Čutite se prosto, da dodate podmape za vire in pozive.

### -2- Ustvarjanje pripomočka

Poglejmo, kako zgleda ustvarjanje pripomočka. Najprej mora biti ustvarjen v svoji podmapi *tool* takole:

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

Tukaj vidimo, kako definiramo ime, opis in vhodno shemo z uporabo Pydantic, ter obdelovalec, ki se bo poklical, ko je ta pripomoček klican. Nazadnje izpostavimo `tool_add`, slovar, ki vsebuje vse te lastnosti.

Obstaja tudi *schema.py*, ki definira vhodno shemo, ki jo uporablja naš pripomoček:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Prav tako moramo napolniti *__init__.py*, da zagotovimo, da je mapa tools obravnavana kot modul. Poleg tega moramo izpostaviti module znotraj nje takole:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

V to datoteko lahko nadaljujemo z dodajanjem, ko dodajamo še več pripomočkov.

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

- name, ime pripomočka.
- rawSchema, to je Zod shema, ki bo uporabljena za validacijo prihajajočih zahtev za klic pripomočka.
- inputSchema, ta shema se uporablja v obdelovalcu.
- callback, to se uporabi za klic pripomočka.

Obstaja tudi `Tool`, ki se uporabi za pretvorbo tega slovarja v tip, ki ga lahko sprejme MCP strežniški obdelovalec, in izgleda takole:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

In je *schema.ts*, kjer hranimo vhodne sheme za vsak pripomoček, ki izgleda takole z enim samim shemom trenutno, a ko dodajamo pripomočke, lahko dodamo več vnosov:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Odlično, nadaljujmo z obdelavo izpisa naših pripomočkov.

### -3- Obdelava izpisa pripomočkov

Nato moramo za izpis pripomočkov nastaviti obdelovalca zahtev. Tukaj je, kaj moramo dodati v našo datoteko strežnika:

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

Tukaj dodamo dekorator `@server.list_tools` in implementacijsko funkcijo `handle_list_tools`. V slednji moramo ustvariti seznam pripomočkov. Opazite, da mora imeti vsak pripomoček ime, opis in inputSchema.   

**TypeScript**

Za nastavitev obdelovalca zahteve za izpis pripomočkov moramo na strežniku poklicati `setRequestHandler` s shemo, ki ustreza temu, kar poskušamo narediti, v tem primeru `ListToolsRequestSchema`. 

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
// Koda izpuščena zaradi jedrnatosti
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrni seznam registriranih orodij
  return {
    tools: tools
  };
});
```

Odlično, zdaj imamo rešeno nalogo izpisa pripomočkov, poglejmo, kako lahko kličemo pripomočke.

### -4- Obdelava klica pripomočka

Za klic pripomočka moramo nastaviti še enega obdelovalca zahtev, tokrat osredotočenega na upravljanje zahteve, ki določa, katero funkcijo klicati in s katerimi argumenti.

**Python**

Uporabimo dekorator `@server.call_tool` in ga implementiramo s funkcijo, kot je `handle_call_tool`. V tej funkciji moramo razčleniti ime pripomočka, njegove argumente in zagotoviti, da so argumenti veljavni za ta pripomoček. Arguments lahko validiramo tukaj ali kasneje v pripomočku.

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
        # pokliči orodje
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Tukaj se zgodi:

- Ime našega pripomočka je že prisotno kot vhodni parameter `name`, prav tako kot argumenti v obliki slovarja `arguments`.

- Pripomoček se kliče z `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumentov se izvede v lastnosti `handler`, ki kaže na funkcijo, če tej spodleti, bo sprožila izjemo. 

Tako zdaj imamo popolno razumevanje izpisa in klica pripomočkov z nizkonivojskim strežnikom.

Oglejte si [celoten primer](./code/README.md) tukaj

## Naloga

Razširite kodo, ki ste jo prejeli, z več pripomočki, viri in pozivi ter razmislite, kako opazite, da morate datoteke dodajati samo v mapo tools in nikjer drugje.

*Rešitev ni podana*

## Povzetek

V tem poglavju smo videli, kako deluje pristop nizkonivojskega strežnika in kako nam lahko pomaga ustvariti lepo arhitekturo, na kateri lahko gradimo. Pogovorili smo se tudi o validaciji in prikazali, kako delati z knjižnicami za validacijo za ustvarjanje shem vhodnih podatkov.

## Kaj sledi

- Naprej: [Preprosta avtentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatski prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v matičnem jeziku naj velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
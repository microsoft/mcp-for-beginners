# Napredna uporaba strežnika

V MCP SDK sta na voljo dva različna tipa strežnikov, vaš običajni strežnik in nizkonivojski strežnik. Običajno uporabite običajni strežnik, da mu dodate funkcionalnosti. V nekaterih primerih pa želite zanašati na nizkonivojski strežnik, na primer:

- Boljša arhitektura. Možno je ustvariti čisto arhitekturo z obema, tako običajnim kot nizkonivojskim strežnikom, vendar se lahko trdi, da je nekoliko lažje z nizkonivojskim strežnikom.
- Razpoložljivost funkcij. Nekatere napredne funkcije lahko uporabljate samo z nizkonivojskim strežnikom. To boste videli v kasnejših poglavjih, ko bomo dodajali vzorčenje in izzivanje.

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

// Dodaj orodje za seštevanje
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

Poanta je, da izrecno dodate vsako orodje, vir ali poziv, ki ga želite imeti na strežniku. Ni nič narobe s tem.

### Pristop nizkonivojskega strežnika

Ko pa uporabite pristop nizkonivojskega strežnika, morate razmišljati drugače. Namesto, da registrirate vsako orodje, namesto tega ustvarite dve funkciji za vsako vrsto funkcije (orodja, viri ali pozivi). Na primer, orodja imajo samo dve funkciji, in sicer:

- Seznam vseh orodij. Ena funkcija je odgovorna za vse poskuse seznama orodij.
- Obdelava klicev vseh orodij. Tudi tukaj obstaja samo ena funkcija, ki obdeluje klice orodja.

Zveni kot potencialno manj dela, kajne? Torej namesto registracije orodja moram samo poskrbeti, da je orodje na seznamu, ko naštejem vsa orodja, in da se pokliče, ko pride zahteva za klic orodja.

Oglejmo si zdaj, kako koda izgleda:

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

Tukaj imamo funkcijo, ki vrne seznam funkcij. Vsak vnos na seznamu orodij ima zdaj polja, kot so `name`, `description` in `inputSchema`, da ustreza tipu vračanja. To nam omogoča, da orodja in definicijo funkcije postavimo kam drugam. Sedaj lahko ustvarimo vsa orodja v mapi tools in enako velja za vse vaše funkcije, tako da je vaš projekt lahko organiziran na tak način:

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

To je super, naša arhitektura je lahko zelo čista.

Kaj pa klic orodij, ali je to isto, ena funkcija za klic orodja, katerokoli orodje? Da, natanko tako, tukaj je koda za to:

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

Kot vidite iz zgornje kode, moramo razčleniti, katero orodje klicati in s kakšnimi argumenti, nato moramo nadaljevati s klicanjem orodja.

## Izboljšanje pristopa z validacijo

Do zdaj ste videli, kako lahko vse vaše registracije za dodajanje orodij, virov in pozivov nadomestite s temi dvema funkcijama na vsako vrsto funkcije. Kaj še moramo storiti? No, morali bi dodati neko obliko validacije, da zagotovimo, da je orodje klicano s pravimi argumenti. Vsako okolje za izvajanje ima svojo rešitev za to, na primer Python uporablja Pydantic, TypeScript pa Zod. Ideja je, da naredimo naslednje:

- Premaknemo logiko za ustvarjanje funkcije (orodje, vir ali poziv) v svojo namensko mapo.
- Dodamo način za validacijo dohodne zahteve, ki na primer zahteva klic orodja.

### Ustvarjanje funkcije

Za ustvarjanje funkcije bomo morali ustvariti datoteko za to funkcijo in poskrbeti, da vsebuje obvezna polja, ki jih zahteva ta funkcija. Ta polja nekoliko razlikujejo med orodji, viri in pozivi.

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
        # Preveri vnos z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, da bomo lahko ustvarili AddInputModel in preverili argumente

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

- Ustvarimo shemo s Pydantic `AddInputModel` s polji `a` in `b` v datoteki *schema.py*.
- Poskusimo razčleniti dohodno zahtevo, da bo tipa `AddInputModel`, če parametri niso skladni, se bo to sesulo:

   ```python
   # add.py
    try:
        # Preveri vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Lahko izberete, ali to logiko razčlenjevanja postavite v sam klic orodja ali v funkcijo obdelovalca.

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

- V obdelovalcu, ki upravlja vse klice orodij, zdaj poskušamo razčleniti dohodno zahtevo v definirano shemo orodja:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    če to deluje, potem nadaljujemo s klicem dejanskega orodja:

    ```typescript
    const result = await tool.callback(input);
    ```

Kot vidite, ta pristop ustvarja odlično arhitekturo, saj ima vse svoj prostor, *server.ts* je zelo majhna datoteka, ki samo povezuje obdelovalce zahtev in vsaka funkcija je v svoji mapi, npr. tools/, resources/ ali /prompts.

Super, poskusimo to naslednje zgraditi.

## Vaja: Ustvarjanje nizkonivojskega strežnika

V tej vaji bomo naredili naslednje:

1. Ustvarili nizkonivojski strežnik, ki upravlja seznam orodij in klice orodij.
1. Implementirali arhitekturo, na kateri lahko gradite.
1. Dodali validacijo, da zagotovimo pravilno validacijo vaših klicev orodij.

### -1- Ustvarjanje arhitekture

Prva stvar, na katero moramo paziti, je arhitektura, ki nam pomaga razširiti se, ko dodajamo več funkcij, tako izgleda:

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

Zdaj smo pripravili arhitekturo, ki zagotavlja, da lahko v mapi tools enostavno dodajamo nova orodja. Prosto sledite temu pristopu za dodajanje podmap za vire in pozive.

### -2- Ustvarjanje orodja

Poglejmo, kako izgleda ustvarjanje orodja. Najprej mora biti ustvarjeno v svoji podmapi *tool* na tak način:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Preveri vhod z uporabo Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, da bomo lahko ustvarili AddInputModel in preverili argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Tukaj vidimo, kako definiramo ime, opis in vhodno shemo z uporabo Pydantic in obdelovalec, ki bo poklican, ko bo orodje klicano. Nazadnje izpostavimo `tool_add`, ki je slovar z vsemi temi lastnostmi.

Obstaja tudi *schema.py*, ki definira vhodno shemo, ki jo uporablja naše orodje:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Prav tako moramo zapolniti *__init__.py*, da zagotovimo, da se mapa tools obravnava kot modul. Poleg tega moramo izpostaviti module v njej tako:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

To datoteko lahko nadaljujemo dopolnjevati, ko dodajamo več orodij.

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
- rawSchema, to je Zod shema, ki se uporablja za validacijo dohodnih zahtev za klic tega orodja.
- inputSchema, ta shema se uporablja v obdelovalcu.
- callback, uporablja se za klic orodja.

Obstaja tudi `Tool`, ki se uporablja za pretvorbo tega slovarja v tip, ki ga lahko sprejme obdelovalec MCP strežnika, in izgleda takole:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

In obstaja *schema.ts*, kjer hranimo vhode za vsako orodje, ki trenutno vsebuje samo eno shemo, a ko dodajamo orodja, lahko dodamo več vnosov:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, nadaljujmo z obdelavo seznama naših orodij.

### -3- Obdelava seznama orodij

Nato, da upravljamo seznam orodij, moramo ustvariti obdelovalca zahtev za to. Tukaj je, kar moramo dodati v našo datoteko strežnika:

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

Tukaj dodamo dekorator `@server.list_tools` in implementiramo funkcijo `handle_list_tools`. V slednji moramo ustvariti seznam orodij. Opazite, da mora imeti vsako orodje ime, opis in vhodno shemo.

**TypeScript**

Za nastavitev obdelovalca zahtev za seznanjanje orodij moramo na strežniku poklicati `setRequestHandler` s shemo, ki ustreza temu, kar želimo narediti, v tem primeru `ListToolsRequestSchema`.

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
// koda izpuščena zaradi jedrnatosti
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrni seznam registriranih orodij
  return {
    tools: tools
  };
});
```

Super, zdaj smo rešili kos seznama orodij, poglejmo, kako lahko kličemo orodja.

### -4- Obdelava klica orodja

Za klic orodja moramo nastaviti še enega obdelovalca zahtev, tokrat z osredotočenostjo na obdelavo zahteve, ki določa, katero funkcijo klicati in s kakšnimi argumenti.

**Python**

Uporabimo dekorator `@server.call_tool` in ga implementiramo z funkcijo, kot je `handle_call_tool`. V tej funkciji moramo razčleniti ime orodja, njegove argumente in zagotoviti, da so argumenti veljavni za zadevno orodje. Argumente lahko validiramo bodisi v tej funkciji ali kasneje v dejanskem orodju.

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
        # sproži orodje
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Tukaj se zgodi naslednje:

- Ime našega orodja je že prisotno kot vhodni parameter `name`, podobno pa velja tudi za naše argumente v obliki slovarja `arguments`.

- Orodje je klicano z `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumentov poteka v lastnosti `handler`, ki kaže na funkcijo; če ne uspe, bo sprožila izjemo.

Torej zdaj imamo popolno razumevanje seznanjanja in klicanja orodij z uporabo nizkonivojskega strežnika.

Oglejte si [celoten primer](./code/README.md) tukaj

## Naloga

Razširite kodo, ki ste jo dobili, z več orodji, viri in pozivi ter razmislite, kako ugotovite, da morate dodajati datoteke samo v mapo tools in nikjer drugje.

*Rešitev ni podana*

## Povzetek

V tem poglavju smo videli, kako deluje pristop nizkonivojskega strežnika in kako nam lahko pomaga ustvariti lepo arhitekturo, na kateri lahko še naprej gradimo. Prav tako smo obravnavali validacijo in prikazali, kako delati s knjižnicami za validacijo za ustvarjanje shem za validacijo vhodov.

## Kaj sledi

- Naslednje: [Preprosta avtentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
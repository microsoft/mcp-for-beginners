# Napredno korištenje poslužitelja

Postoje dvije različite vrste poslužitelja izložene u MCP SDK, vaš uobičajeni poslužitelj i niskorazinski poslužitelj. Obično biste koristili uobičajeni poslužitelj za dodavanje značajki. Međutim, za neke slučajeve želite se osloniti na niskorazinski poslužitelj, kao što su:

- Bolja arhitektura. Moguće je stvoriti čistu arhitekturu i s uobičajenim i s niskorazinskim poslužiteljem, ali može se tvrditi da je nešto lakše s niskorazinskim poslužiteljem.
- Dostupnost značajki. Neke napredne značajke mogu se koristiti samo s
    niskorazinskim poslužiteljem. Kasniji poglavlja pokrivaju Elicitation i zastarjelu Sampling
    značajku, koja je zastarjela u MCP `2026-07-28`.

## Uobičajeni poslužitelj vs niskorazinski poslužitelj

Ovako izgleda stvaranje MCP poslužitelja s uobičajenim poslužiteljem

**Python**

```python
mcp = FastMCP("Demo")

# Dodajte alat za zbrajanje
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

// Dodajte alat za zbrajanje
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

Poanta je da eksplicitno dodajete svaki alat, resurs ili prompt koji želite da poslužitelj ima. Nema ništa loše u tome.  

### Pristup niskorazinskog poslužitelja

Međutim, kada koristite pristup niskorazinskog poslužitelja, morate razmišljati drugačije. Umjesto registracije svakog alata, stvarate po dva handlera za svaki tip značajke (alat, resurs ili prompt). Na primjer, alati tada imaju samo dvije funkcije ovako:

- Popisivanje svih alata. Jedna funkcija bila bi odgovorna za sve pokušaje popisivanja alata.
- Obrada poziva svih alata. Ovdje također postoji samo jedna funkcija koja obrađuje pozive na alat.

Zvuči kao potencijalno manje posla, zar ne? Dakle, umjesto registracije alata, samo se moram pobrinuti da je alat na popisu kad izlistam sve alate i da se pozove kad postoji dolazni zahtjev za poziv alata.

Pogledajmo kako sada izgleda kod:

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
  // Vrati popis registriranih alata
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

Ovdje sada imamo funkciju koja vraća popis značajki. Svaki unos u popisu alata sada ima polja kao što su `name`, `description` i `inputSchema` prema tipu povratne vrijednosti. To nam omogućuje da alate i definiciju značajki smjestimo drugdje. Sada možemo sve alate staviti u mapu tools i isto vrijedi za sve vaše značajke tako da vaš projekt može biti organiziran ovako:

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

To je sjajno, naša arhitektura može izgledati prilično čisto.

A što je s pozivanjem alata, je li to ista ideja, jedan handler za pozivanje bilo kojeg alata? Da, upravo tako, evo koda za to:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je rječnik s imenima alata kao ključevima
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
    // TODO pozvati alat,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Kao što vidite iz gornjeg koda, trebamo parsirati koji alat pozvati i s kojim argumentima, a zatim nastaviti s pozivanjem alata.

## Poboljšanje pristupa s validacijom

Dosad ste vidjeli kako se sve vaše registracije za dodavanje alata, resursa i prompta mogu zamijeniti ovim dvama upravljačkim funkcijama po tipu značajke. Što još trebamo napraviti? Pa, trebali bismo dodati neku vrstu validacije da budemo sigurni da se alat poziva s pravim argumentima. Svaki runtime ima svoje rješenje za to, na primjer, Python koristi Pydantic, a TypeScript koristi Zod. Ideja je da napravimo sljedeće:

- Premjestimo logiku za stvaranje značajke (alat, resurs ili prompt) u njegovu namjensku mapu.
- Dodamo način za validaciju dolaznog zahtjeva za primjer poziva alata.

### Stvaranje značajke

Za stvaranje značajke, trebamo stvoriti datoteku za tu značajku i osigurati da ona ima obavezna polja potrebna za tu značajku. Koja polja se razlikuju za alate, resurse i promptove.

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
        # Validirajte unos pomoću Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodati Pydantic, tako da možemo stvoriti AddInputModel i validirati argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

ovdje možete vidjeti kako radimo sljedeće:

- Stvaramo shemu koristeći Pydantic `AddInputModel` s poljima `a` i `b` u datoteci *schema.py*.
- Pokušavamo parsirati dolazni zahtjev kao tip `AddInputModel`, ako postoji neslaganje u parametrima doći će do pada:

   ```python
   # add.py
    try:
        # Validirajte unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Možete odabrati hoćete li ovu logiku parsiranja staviti u sam poziv alata ili u handler funkciju.

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

- U handleru koji obrađuje sve pozive alata, sada pokušavamo parsirati dolazni zahtjev u definiranu shemu alata:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ako to uspije, nastavljamo s pozivom stvarnog alata:

    ```typescript
    const result = await tool.callback(input);
    ```

Kao što vidite, ovaj pristup stvara sjajnu arhitekturu jer sve ima svoje mjesto, *server.ts* je vrlo mala datoteka koja samo povezuje zahtjeve i svaki je feature u svom direktoriju, npr. tools/, resources/ ili prompts/.

Odlično, pokušajmo to sljedeće izgraditi.

## Vježba: Kreiranje niskorazinskog poslužitelja

U ovoj vježbi napravit ćemo sljedeće:

1. Kreirati niskorazinski poslužitelj koji obrađuje listanje alata i njihov poziv.
1. Implementirati arhitekturu na kojoj možete graditi.
1. Dodati validaciju kako bi osigurali ispravnu validaciju poziva vaših alata.

### -1- Kreiranje arhitekture

Prvo što trebamo riješiti je arhitektura koja nam pomaže skalirati dok dodajemo nove značajke, ovako to izgleda:

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

Sada smo postavili arhitekturu koja osigurava da lako možemo dodavati nove alate u mapu tools. Slobodno slijedite ovaj primjer da biste dodali poddirektorije za resurse i prometive.

### -2- Kreiranje alata

Pogledajmo sada kako izgleda kreiranje alata. Prvo, alat mora biti stvoren u svom *tool* poddirektoriju ovako:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validiraj unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, tako da možemo napraviti AddInputModel i validirati argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ovdje vidimo kako definiramo ime, opis i input shemu koristeći Pydantic i handler koji će se pozvati kad se ovaj alat koristi. Na kraju izlažemo `tool_add` koji je rječnik koji sadrži sva ta svojstva.

Tu je i *schema.py* koji se koristi za definiranje input sheme alata:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Također trebamo popuniti *__init__.py* kako bismo osigurali da se direktorij tools tretira kao modul. Dodatno, treba izložiti module unutar njega ovako:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Nastavljamo dodavati u ovu datoteku kako dodajemo nove alate.

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

Ovdje stvaramo rječnik koji se sastoji od svojstava:

- name, ovo je ime alata.
- rawSchema, ovo je Zod shema, koristi se za validaciju dolaznih zahtjeva za poziv ovog alata.
- inputSchema, ovu shemu koristi handler.
- callback, ovo se koristi za pozivanje alata.

Također je tu `Tool` koji se koristi za pretvaranje ovog rječnika u tip koji mcp server handler može prihvatiti, izgleda ovako:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

I tu je *schema.ts* gdje pohranjujemo input sheme za svaki alat, trenutno je samo jedna shema, ali kako dodajemo alate možemo dodavati nove unose:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Odlično, idemo sada na rukovanje popisom alata.

### -3- Rukovanje popisom alata

Sljedeće, za rukovanje popisom alata, trebamo postaviti handler za taj zahtjev. Evo što trebamo dodati u našu datoteku servera:

**Python**

```python
# kod izostavljen radi sažetosti
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

Ovdje dodajemo dekorator `@server.list_tools` i funkciju koja ga implementira `handle_list_tools`. Unutar te funkcije treba izraditi popis alata. Primijetite da svaki alat treba imati ime, opis i inputSchema.   

**TypeScript**

Za postavljanje handlera zahtjeva za popis alata, trebamo pozvati `setRequestHandler` na serveru sa shemom koja odgovara onome što radimo, u ovom slučaju `ListToolsRequestSchema`. 

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
// kod izostavljen zbog sažetosti
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vraća popis registriranih alata
  return {
    tools: tools
  };
});
```

Odlično, sada smo riješili dio s popisom alata, pogledajmo kako ćemo pozivati alate.

### -4- Rukovanje pozivom alata

Za pozivanje alata, trebamo postaviti drugi handler zahtjeva, ovaj put fokusiran na obradu zahtjeva koji specificira koju značajku pozvati i s kojim argumentima.

**Python**

Koristit ćemo dekorator `@server.call_tool` i implementirati ga funkcijom poput `handle_call_tool`. Unutar te funkcije trebamo parsirati ime alata, njegove argumente i osigurati da su argumenti valjani za taj alat. Argumente možemo validirati u ovoj funkciji ili niže u samom alatu.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je rječnik s imenima alata kao ključevima
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # pozovi alat
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Evo što se događa:

- Ime našeg alata je već dostupno kao ulazni parametar `name`, a argumenti su u obliku rječnika `arguments`.

- Alat se poziva s `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumenata se događa u svojstvu `handler` koje pokazuje na funkciju, ako ne uspije, baca iznimku.

Tako, sada imamo potpuno razumijevanje popisivanja i pozivanja alata koristeći niskorazinski poslužitelj.

Pogledajte [cijeli primjer](./code/README.md) ovdje

## Zadatak

Proširite kod koji ste dobili s više alata, resursa i prompta i razmislite o tome kako primjećujete da trebate samo dodavati datoteke u direktoriju tools i nigdje drugo.

*Nema dane riješenja*

## Sažetak

U ovom poglavlju vidjeli smo kako funkcionira pristup niskorazinskog poslužitelja i kako nam to može pomoći stvoriti lijepu arhitekturu na koju možemo nastaviti graditi. Također smo raspravljali o validaciji i pokazano vam je kako raditi s knjižnicama za validaciju za stvaranje shema za validaciju unosa.

## Što slijedi

- Sljedeće: [Jednostavna autentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
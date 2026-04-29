# Napredno korištenje servera

U MCP SDK-u postoje dvije različite vrste servera: vaš uobičajeni server i niskorazinski server. Obično biste koristili obični server za dodavanje funkcionalnosti. Međutim, u nekim slučajevima želite se osloniti na niskorazinski server, kao što su:

- Bolja arhitektura. Moguće je napraviti čistu arhitekturu i s običnim i s niskorazinskim serverom, ali može se tvrditi da je to nešto lakše s niskorazinskim serverom.
- Dostupnost funkcionalnosti. Neke napredne funkcije mogu se koristiti samo s niskorazinskim serverom. To ćete vidjeti u kasnijim poglavljima kada dodajemo uzorkovanje i ispitivanje.

## Obični server vs niskorazinski server

Evo kako izgleda kreiranje MCP Servera s običnim serverom

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

Poanta je da eksplicitno dodajete svaki alat, resurs ili prompt koji želite da server ima. Nema ništa loše u tome.  

### Pristup niskorazinskog servera

Međutim, kad koristite pristup niskorazinskog servera, morate razmišljati drugačije. Umjesto registracije svakog alata, umjesto toga stvarate dva rukovatelja po vrsti značajke (alat, resurs ili prompt). Tako, na primjer, alati imaju samo dvije funkcije poput ovih:

- Popisivanje svih alata. Jedna funkcija je zadužena za sve pokušaje popisivanja alata.
- rukovanje pozivanjem svih alata. Ovdje također postoji samo jedna funkcija koja rukuje pozivima na alat.

To zvuči kao potencijalno manje posla, zar ne? Dakle, umjesto da registriram alat, samo moram osigurati da je alat naveden kad popisujem sve alate i da se pozove kad postoji dolazni zahtjev za pozivanje alata. 

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

Ovdje sada imamo funkciju koja vraća popis značajki. Svaki unos u popisu alata sada ima polja poput `name`, `description` i `inputSchema` kako bi se pridržavao tipa povratka. To nam omogućava da definiramo alate i značajke negdje drugdje. Sada možemo stvoriti sve naše alate u mapi tools, i isto vrijedi za sve vaše značajke, tako da vaš projekt može biti organiziran ovako:

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

Što s pozivanjem alata, je li to ista ideja, jedan rukovatelj za pozivanje bilo kojeg alata? Da, upravo tako, evo koda za to:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools je rječnik koji ima nazive alata kao ključeve
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

Kao što vidite iz gornjeg koda, moramo parsirati koji alat pozvati i s kojim argumentima, a zatim nastaviti s pozivanjem alata.

## Poboljšanje pristupa validacijom

Do sada ste vidjeli kako se sve vaše registracije za dodavanje alata, resursa i promptova mogu zamijeniti ovim dvama rukovateljima po vrsti značajke. Što još trebamo napraviti? Pa, trebali bismo dodati neku vrstu validacije kako bismo osigurali da se alat poziva s ispravnim argumentima. Svako runtime okruženje ima svoje rješenje za to, na primjer Python koristi Pydantic, a TypeScript koristi Zod. Ideja je da napravimo sljedeće:

- Premjestimo logiku stvaranja značajke (alata, resursa ili prompta) u njegovu namjensku mapu.
- Dodamo način validacije dolaznog zahtjeva, primjerice za pozivanje alata.

### Kreirati značajku

Da bismo stvorili značajku, morat ćemo napraviti datoteku za tu značajku i osigurati da ima obavezna polja koja se zahtijevaju za tu značajku. Koja polja se razlikuju između alata, resursa i promptova.

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
        # Validirajte unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodajte Pydantic kako bismo mogli kreirati AddInputModel i validirati argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ovdje možete vidjeti kako radimo sljedeće:

- Stvaramo shemu koristeći Pydantic `AddInputModel` s poljima `a` i `b` u datoteci *schema.py*.
- Pokušavamo parsirati dolazni zahtjev kao tip `AddInputModel`, ako postoji nepodudaranje parametara, to će se srušiti:

   ```python
   # add.py
    try:
        # Validirajte unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Možete odabrati hoćete li ovu parsiranu logiku staviti unutar samog poziva alata ili u rukovateljsku funkciju.

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

- U rukovatelju koji obrađuje sve pozive alata, sada pokušavamo parsirati dolazni zahtjev u definiranu shemu alata:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ako to uspije, nastavljamo s pozivanjem stvarnog alata:

    ```typescript
    const result = await tool.callback(input);
    ```

Kao što vidite, ovaj pristup stvara odličnu arhitekturu jer sve ima svoje mjesto, *server.ts* je vrlo mala datoteka koja samo povezuje rukovatelje zahtjeva, a svaka značajka je u svojoj mapi, tj. tools/, resources/ ili /prompts.

Odlično, pokušajmo to izgraditi sljedeće. 

## Vježba: Kreiranje niskorazinskog servera

U ovoj vježbi napravit ćemo sljedeće:

1. Kreirati niskorazinski server koji upravlja popisivanjem alata i pozivanjem alata.
1. Implementirati arhitekturu na kojoj možete graditi.
1. Dodati validaciju kako biste osigurali pravilnu validaciju poziva vaših alata.

### -1- Kreirajte arhitekturu

Prvo što trebamo napraviti jest arhitektura koja nam pomaže skalirati kako dodajemo više značajki, evo kako to izgleda:

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

Sada smo postavili arhitekturu koja osigurava da lako možemo dodavati nove alate u mapu tools. Slobodno pratite ovo da dodate poddirektorije za resurse i promptove.

### -2- Kreiranje alata

Pogledajmo kako izgleda stvaranje alata. Prvo, mora biti kreiran u svojoj *tool* poddirektoriju ovako:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validiraj unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, kako bismo mogli napraviti AddInputModel i validirati argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ovdje vidimo kako definiramo ime, opis i ulaznu shemu koristeći Pydantic i rukovatelja koji će se pozvati kad se ovaj alat pozove. Na kraju, izlažemo `tool_add` što je rječnik koji sadrži sve ove vrijednosti.

Također postoji *schema.py* koja se koristi za definiranje ulazne sheme koju koristi naš alat:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Također trebamo napuniti *__init__.py* kako bismo osigurali da se direktorij tools tretira kao modul. Dodatno, trebamo izložiti module unutar nje na sljedeći način:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Možemo nastaviti dodavati u ovu datoteku dok dodajemo više alata.

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

Ovdje kreiramo rječnik koji sadrži svojstva:

- name, to je ime alata.
- rawSchema, to je Zod shema, koristi se za validaciju dolaznih zahtjeva za pozivanje ovog alata.
- inputSchema, ovu shemu koristi rukovatelj.
- callback, koristi se za pozivanje alata.

Postoji i `Tool` koji služi za pretvorbu ovog rječnika u tip koji MCP server rukovatelj može prihvatiti i izgleda ovako:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

I tu je *schema.ts* gdje spremamo ulazne sheme za svaki alat koji trenutno izgleda ovako, s jednom shemom, ali kako dodajemo alate možemo dodavati više unosa:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Odlično, prijeđimo na rukovanje popisivanjem naših alata.

### -3- Rukovanje popisivanjem alata

Sljedeće, da bismo upravljali popisivanjem naših alata, trebamo postaviti rukovatelja zahtjeva za to. Evo što trebamo dodati u naš server fajl:

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

Ovdje dodajemo dekorator `@server.list_tools` i implementacijsku funkciju `handle_list_tools`. U potonjoj moramo proizvesti popis alata. Primijetite kako svaki alat mora imati ime, opis i inputSchema.   

**TypeScript**

Za postavljanje rukovatelja zahtjeva za popisivanje alata, trebamo pozvati `setRequestHandler` na serveru s shemom koja odgovara onome što pokušavamo napraviti, u ovom slučaju `ListToolsRequestSchema`. 

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
// kod izostavljen radi sažetosti
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrati popis registriranih alata
  return {
    tools: tools
  };
});
```

Sjajno, sada smo riješili dio s popisivanjem alata, pogledajmo kako bismo mogli pozivati alate sljedeće.

### -4- Rukovanje pozivanjem alata

Za pozivanje alata, moramo postaviti još jednog rukovatelja zahtjeva, ovaj put fokusiranog na obradu zahtjeva koji specificira koju značajku pozvati i s kojim argumentima.

**Python**

Koristit ćemo dekorator `@server.call_tool` i implementirati ga funkcijom poput `handle_call_tool`. Unutar te funkcije trebamo parsirati ime alata, njegove argumente i osigurati da su argumenti valjani za dotični alat. Argumente možemo validirati ili u ovoj funkciji ili kasnije u samom alatu.

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
        # pozvati alat
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Evo što se događa:

- Ime našeg alata već je prisutno kao ulazni parametar `name` što vrijedi i za naše argumente u obliku rječnika `arguments`.

- Alat se poziva s `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumenata događa se u svojstvu `handler` koje pokazuje na funkciju, ako to ne uspije, podiže se iznimka.

Eto, sada imamo potpuno razumijevanje popisivanja i pozivanja alata koristeći niskorazinski server.

Pogledajte [puni primjer](./code/README.md) ovdje

## Zadatak

Proširite dani kod s nizom alata, resursa i prompta i razmislite kako primjećujete da morate samo dodavati datoteke u direktorij tools i nigdje drugdje. 

*Nije dana rješenja*

## Sažetak

U ovom poglavlju vidjeli smo kako rade pristupi niskorazinskog servera i kako to može pomoći da stvorimo lijepu arhitekturu na kojoj možemo neprestano graditi. Također smo razgovarali o validaciji i pokazano vam je kako raditi s bibliotekama za validaciju za kreiranje shema za ulaznu validaciju.

## Što slijedi

- Sljedeće: [Jednostavna autentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku smatra se autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
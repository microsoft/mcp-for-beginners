# Napredno korištenje servera

U MCP SDK postoje dva različita tipa servera, vaš normalni server i low-level server. Obično koristite regularni server za dodavanje značajki. Međutim, u nekim slučajevima želite koristiti low-level server, kao na primjer:

- Bolja arhitektura. Moguće je kreirati čistu arhitekturu s regularnim serverom i low-level serverom, ali može se tvrditi da je to malo lakše s low-level serverom.
- Dostupnost značajki. Neke napredne značajke mogu se koristiti samo s low-level serverom. To ćete vidjeti u kasnijim poglavljima kada dodajemo uzorkovanje i prikupljanje.

## Regularni server vs low-level server

Evo kako izgleda kreiranje MCP servera s regularnim serverom

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

Poanta je da eksplicitno dodajete svaki alat, resurs ili upit koji želite da server ima. Nema ništa loše u tome.

### Pristup low-level servera

Međutim, kada koristite pristup low-level servera morate razmišljati drugačije. Umjesto da registrirate svaki alat, kreirate dvije funkcije po tipu značajke (alati, resursi ili upiti). Na primjer, za alate postoje samo dvije funkcije:

- Nabrajanje svih alata. Jedna funkcija će biti odgovorna za sve pokušaje nabrajanja alata.
- Obrada poziva svih alata. Ovdje također postoji samo jedna funkcija koja obrađuje pozive na alat.

To zvuči kao manje posla, zar ne? Umjesto registracije alata, samo trebam osigurati da je alat naveden kada nabrajam sve alate i da se pozove kada stigne zahtjev za poziv alata.

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

Ovdje sada imamo funkciju koja vraća popis značajki. Svaki unos u popisu alata sada ima polja poput `name`, `description` i `inputSchema` da udovolji tipu povratne vrijednosti. To nam omogućuje da alate i definicije značajki držimo negdje drugdje. Sada možemo kreirati sve naše alate u mapi tools i isto vrijedi za sve vaše značajke pa vaš projekt može biti organiziran ovako:

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

Odlično, naša arhitektura može biti vrlo čista.

Što je s pozivanjem alata, je li ideja ista, jedan handler za pozivanje bilo kojeg alata? Da, upravo tako, evo koda za to:

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

Kao što vidite iz gornjeg koda, moramo parsirati koji alat treba pozvati i s kojim argumentima, a zatim nastaviti s pozivanjem alata.

## Poboljšanje pristupa s validacijom

Do sada ste vidjeli kako se sve vaše registracije za dodavanje alata, resursa i upita mogu zamijeniti s dvije funkcije po tipu značajke. Što još trebamo napraviti? Trebali bismo dodati neku vrstu validacije da osiguramo da se alat poziva s ispravnim argumentima. Svako runtime okruženje ima svoje rješenje za to, na primjer Python koristi Pydantic, a TypeScript koristi Zod. Ideja je da napravimo sljedeće:

- Premjestimo logiku za kreiranje značajke (alatat, resurs ili upit) u njenu namjensku mapu.
- Dodamo način da se validira dolazni zahtjev za poziv alata.

### Kreiranje značajke

Za kreiranje značajke trebamo napraviti datoteku za tu značajku i osigurati da ima obavezna polja koja ta značajka zahtijeva. Koja se polja razlikuju između alata, resursa i upita.

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
        # Provjeri unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, tako da možemo kreirati AddInputModel i provjeriti argumenate

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

- Kreiramo shemu koristeći Pydantic `AddInputModel` s poljima `a` i `b` u datoteci *schema.py*.
- Pokušavamo parsirati dolazni zahtjev da bude tipa `AddInputModel`, ako postoji nesklad u parametrima, to će se srušiti:

   ```python
   # add.py
    try:
        # Validirajte unos korištenjem Pydantic modela
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Možete odlučiti hoćete li ovu logiku parsiranja staviti u sam poziv alata ili u handler funkciju.

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

- U handleru koji obrađuje sve pozive alata sada pokušavamo parsirati dolazni zahtjev u definiranu shemu alata:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    ako to uspije, nastavljamo s pozivanjem samog alata:

    ```typescript
    const result = await tool.callback(input);
    ```

Kao što vidite, ovaj pristup kreira izvrsnu arhitekturu jer sve ima svoje mjesto, *server.ts* je vrlo mala datoteka koja samo povezuje request handlere, a svaka značajka je u svojoj mapi, npr. tools/, resources/ ili prompts/.

Super, pokušajmo to sada izgraditi.

## Vježba: Kreiranje low-level servera

U ovoj vježbi učinit ćemo sljedeće:

1. Kreirati low-level server za rukovanje nabrajanjem alata i pozivanjem alata.
1. Implementirati arhitekturu na kojoj možete graditi.
1. Dodati validaciju da osigurate da su vaši pozivi alata ispravno validirani.

### -1- Kreirati arhitekturu

Prvo što trebamo riješiti je arhitektura koja nam pomaže da skaliramo dok dodajemo više značajki, evo kako to izgleda:

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

Sada smo postavili arhitekturu koja osigurava da lako možemo dodavati nove alate u mapu tools. Slobodno napravite poddirektorije za resources i prompts.

### -2- Kreiranje alata

Pogledajmo kako izgleda kreiranje alata. Prvo, mora biti stvoren u poddirektoriju *tool* ovako:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validiraj unos koristeći Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: dodaj Pydantic, tako da možemo kreirati AddInputModel i validirati argumente

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Ovdje vidimo kako definiramo ime, opis i ulaznu shemu koristeći Pydantic i handler koji će se pozvati kada se alat pozove. Na kraju izlažemo `tool_add` koji je rječnik koji drži sve ove stvari.

Postoji i *schema.py* koji definira ulaznu shemu koju alat koristi:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Također moramo popuniti *__init__.py* kako bi direktorij tools bio tretiran kao modul. Osim toga, moramo izložiti module unutar njega ovako:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Možemo nastaviti dodavati u ovu datoteku kako dodajemo više alata.

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

Ovdje kreiramo rječnik sastavljen od svojstava:

- name, ime alata.
- rawSchema, to je Zod shema koja se koristi za validaciju dolaznih zahtjeva poziva alata.
- inputSchema, ova shema se koristi u handleru.
- callback, ovo se koristi za pozivanje alata.

Postoji i `Tool` koji pretvara ovaj rječnik u tip koji mcp server handler može prihvatiti i izgleda ovako:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Također postoji *schema.ts* gdje pohranjujemo ulazne sheme za svaki alat koji izgleda ovako, trenutno samo sa jednom shemom, ali kako dodajemo alate može biti više unosa:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, nastavimo s rukovanjem nabrajanjem naših alata.

### -3- Rukovanje nabrajanjem alata

Sljedeće, za rukovanje nabrajanjem alata, trebamo postaviti request handler za to. Evo što trebamo dodati u naš server file:

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

Ovdje dodajemo dekorator `@server.list_tools` i implementiramo funkciju `handle_list_tools`. U njoj trebamo proizvesti listu alata. Obratite pažnju da svaki alat treba imati name, description i inputSchema.

**TypeScript**

Da bismo postavili request handler za nabrajanje alata, trebamo pozvati `setRequestHandler` na serveru sa shemom koja odgovara onome što radimo, u ovom slučaju `ListToolsRequestSchema`.

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
// kod izostavljen zbog sažetka
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Vrati popis registriranih alata
  return {
    tools: tools
  };
});
```

Odlično, sada smo riješili dio za nabrajanje alata, pogledajmo kako možemo pozivati alate.

### -4- Rukovanje pozivanjem alata

Za pozivanje alata, trebamo postaviti još jedan request handler, ovaj put fokusiran na zahtjev koji specificira koju značajku pozvati i s kojim argumentima.

**Python**

Upotrijebimo dekorator `@server.call_tool` i implementirajmo ga funkcijom poput `handle_call_tool`. U toj funkciji trebamo parsirati ime alata, njegove argumente i osigurati da su argumenti valjani za dotični alat. Validaciju argumenata možemo napraviti u ovoj funkciji ili dublje u samom alatu.

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

- Ime našeg alata već je prisutno kao ulazni parametar `name` što vrijedi i za argumente u rječniku `arguments`.

- Alat se poziva s `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumenata događa se u `handler` svojstvu koje pokazuje na funkciju, a ako ne uspije bit će podignut izuzetak.

Eto, sada imamo potpuno razumijevanje nabrajanja i pozivanja alata koristeći low-level server.

Pogledajte [cijeli primjer](./code/README.md) ovdje

## Zadatak

Proširite dobiveni kod s nekoliko alata, resursa i upita i razmislite kako primjećujete da samo trebate dodavati datoteke u mapu tools i nigdje drugo.

*Rješenje nije dano*

## Sažetak

U ovom poglavlju vidjeli smo kako funkcionira pristup low-level servera i kako nam to pomaže stvoriti lijepu arhitekturu na kojoj možemo dalje graditi. Također smo razgovarali o validaciji i pokazano vam je kako raditi s bibliotekama za validaciju da kreirate sheme za ulaznu validaciju.

## Što slijedi

- Sljedeće: [Jednostavna autentikacija](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja proizašla iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
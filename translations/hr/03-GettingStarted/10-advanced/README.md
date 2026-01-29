# Napredno korištenje servera

Postoje dvije različite vrste servera koje MCP SDK nudi: vaš uobičajeni server i server niske razine. Obično koristite uobičajeni server za dodavanje značajki. Međutim, u nekim slučajevima možda ćete se osloniti na server niske razine, primjerice:

- Bolja arhitektura. Moguće je stvoriti čistu arhitekturu s oba tipa servera, ali može se reći da je to malo lakše s serverom niske razine.
- Dostupnost značajki. Neke napredne značajke mogu se koristiti samo s serverom niske razine. Vidjet ćete to u kasnijim poglavljima dok dodajemo uzorkovanje i prikupljanje podataka.

## Uobičajeni server vs server niske razine

Evo kako izgleda kreiranje MCP servera s uobičajenim serverom:

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

Poanta je da eksplicitno dodajete svaki alat, resurs ili upit koji želite da server ima. Ništa loše u tome.

### Pristup serveru niske razine

Međutim, kada koristite pristup serveru niske razine, morate razmišljati drugačije, naime umjesto registriranja svakog alata, kreirate dva handlera po vrsti značajke (alati, resursi ili upiti). Na primjer, za alate postoje samo dvije funkcije, ovako:

- Popis svih alata. Jedna funkcija odgovara za sve pokušaje popisivanja alata.
- Obrada poziva svih alata. Ovdje također postoji samo jedna funkcija koja obrađuje pozive alatima.

Zvuči kao potencijalno manje posla, zar ne? Umjesto registriranja alata, samo trebam osigurati da je alat naveden kada popisujem sve alate i da se poziva kada postoji dolazni zahtjev za poziv alata.

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

Ovdje sada imamo funkciju koja vraća popis značajki. Svaki unos u popisu alata sada ima polja poput `name`, `description` i `inputSchema` kako bi se pridržavao tipa povratne vrijednosti. Ovo nam omogućuje da naše alate i definicije značajki smjestimo drugdje. Sada možemo kreirati sve naše alate u mapi alata, a isto vrijedi i za sve vaše značajke, pa vaš projekt odjednom može biti organiziran ovako:

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

Odlično, naša arhitektura može izgledati prilično čisto.

Što je s pozivanjem alata, je li to ista ideja, jedan handler za poziv alata, bilo kojeg alata? Da, točno, evo koda za to:

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

Kao što možete vidjeti iz gornjeg koda, trebamo izdvojiti alat koji se poziva, s kojim argumentima, a zatim nastaviti s pozivanjem alata.

## Poboljšanje pristupa validacijom

Do sada ste vidjeli kako se sve vaše registracije za dodavanje alata, resursa i upita mogu zamijeniti s ova dva handlera po vrsti značajke. Što još trebamo učiniti? Pa, trebali bismo dodati neki oblik validacije kako bismo osigurali da se alat poziva s ispravnim argumentima. Svako runtime okruženje ima svoje rješenje za ovo, na primjer Python koristi Pydantic, a TypeScript koristi Zod. Ideja je da učinimo sljedeće:

- Premjestimo logiku za kreiranje značajke (alata, resursa ili upita) u njezinu namjensku mapu.
- Dodamo način za validaciju dolaznog zahtjeva koji, na primjer, traži poziv alata.

### Kreiranje značajke

Za kreiranje značajke, trebamo kreirati datoteku za tu značajku i osigurati da ima obavezna polja potrebna za tu značajku. Koja polja se razlikuju između alata, resursa i upita.

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

Ovdje možete vidjeti kako radimo sljedeće:

- Kreiramo shemu koristeći Pydantic `AddInputModel` s poljima `a` i `b` u datoteci *schema.py*.
- Pokušavamo parsirati dolazni zahtjev da bude tipa `AddInputModel`, ako postoji nesklad u parametrima, ovo će se srušiti:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Možete odabrati hoćete li ovu logiku parsiranja staviti u sam poziv alata ili u funkciju handlera.

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

Kao što možete vidjeti, ovaj pristup stvara odličnu arhitekturu jer sve ima svoje mjesto, *server.ts* je vrlo mala datoteka koja samo povezuje request handlere, a svaka značajka je u svojoj odgovarajućoj mapi, tj. tools/, resources/ ili prompts/.

Odlično, pokušajmo ovo izgraditi sljedeće.

## Vježba: Kreiranje servera niske razine

U ovoj vježbi ćemo učiniti sljedeće:

1. Kreirati server niske razine koji obrađuje popisivanje alata i pozivanje alata.
1. Implementirati arhitekturu na kojoj možete graditi.
1. Dodati validaciju kako bismo osigurali da su pozivi vašim alatima ispravno validirani.

### -1- Kreiranje arhitekture

Prvo što trebamo riješiti je arhitektura koja nam pomaže skalirati kako dodajemo više značajki, evo kako to izgleda:

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

Sada smo postavili arhitekturu koja osigurava da lako možemo dodavati nove alate u mapu alata. Slobodno slijedite ovo kako biste dodali poddirektorije za resurse i upite.

### -2- Kreiranje alata

Pogledajmo kako izgleda kreiranje alata. Prvo, alat treba biti kreiran u svom poddirektoriju *tool* ovako:

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

Ovdje vidimo kako definiramo ime, opis, ulaznu shemu koristeći Pydantic i handler koji će biti pozvan kada se ovaj alat poziva. Na kraju, izlažemo `tool_add`, koji je rječnik koji sadrži sva ova svojstva.

Tu je i *schema.py* koji se koristi za definiranje ulazne sheme koju koristi naš alat:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Također trebamo popuniti *__init__.py* kako bismo osigurali da se direktorij alata tretira kao modul. Osim toga, trebamo izložiti module unutar njega ovako:

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

Ovdje kreiramo rječnik koji se sastoji od svojstava:

- name, ovo je ime alata.
- rawSchema, ovo je Zod shema, koristit će se za validaciju dolaznih zahtjeva za poziv ovog alata.
- inputSchema, ova shema će se koristiti od strane handlera.
- callback, koristi se za pozivanje alata.

Tu je i `Tool` koji se koristi za pretvaranje ovog rječnika u tip koji MCP server handler može prihvatiti, a izgleda ovako:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Tu je i *schema.ts* gdje pohranjujemo ulazne sheme za svaki alat, a izgleda ovako s samo jednom shemom trenutno, ali kako dodajemo alate, možemo dodati više unosa:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Odlično, nastavimo s obradom popisivanja naših alata.

### -3- Obrada popisivanja alata

Sljedeće, za obradu popisivanja alata, trebamo postaviti request handler za to. Evo što trebamo dodati u našu datoteku servera:

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

Ovdje dodajemo dekorator `@server.list_tools` i implementiramo funkciju `handle_list_tools`. U potonjoj, trebamo proizvesti popis alata. Primijetite kako svaki alat treba imati ime, opis i inputSchema.

**TypeScript**

Za postavljanje request handlera za popisivanje alata, trebamo pozvati `setRequestHandler` na serveru sa shemom koja odgovara onome što pokušavamo učiniti, u ovom slučaju `ListToolsRequestSchema`.

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

Odlično, sada smo riješili dio popisivanja alata, pogledajmo kako bismo mogli pozivati alate sljedeće.

### -4- Obrada poziva alata

Za pozivanje alata, trebamo postaviti još jedan request handler, ovaj put fokusiran na obradu zahtjeva koji specificira koju značajku pozvati i s kojim argumentima.

**Python**

Koristimo dekorator `@server.call_tool` i implementiramo ga s funkcijom poput `handle_call_tool`. Unutar te funkcije, trebamo izdvojiti ime alata, njegove argumente i osigurati da su argumenti valjani za dotični alat. Možemo validirati argumente u ovoj funkciji ili dalje u stvarnom alatu.

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

Evo što se događa:

- Ime našeg alata već je prisutno kao ulazni parametar `name`, što vrijedi i za naše argumente u obliku rječnika `arguments`.

- Alat se poziva s `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Validacija argumenata događa se u svojstvu `handler`, koje pokazuje na funkciju, ako to ne uspije, podići će se iznimka.

Eto, sada imamo potpuno razumijevanje popisivanja i pozivanja alata koristeći server niske razine.

Pogledajte [cijeli primjer](./code/README.md) ovdje.

## Zadatak

Proširite kod koji ste dobili s nekoliko alata, resursa i upita te razmislite o tome kako primjećujete da trebate dodavati datoteke samo u direktorij alata i nigdje drugdje.

*Rješenje nije dano*

## Sažetak

U ovom poglavlju vidjeli smo kako funkcionira pristup serveru niske razine i kako nam to može pomoći u stvaranju lijepe arhitekture na kojoj možemo nastaviti graditi. Također smo raspravljali o validaciji i pokazano vam je kako raditi s bibliotekama za validaciju kako biste kreirali sheme za validaciju ulaznih podataka.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
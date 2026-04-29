# Avansert serverbruk

Det finnes to forskjellige typer servere eksponert i MCP SDK, din vanlige server og den lavnivå serveren. Normalt ville du brukt den vanlige serveren for å legge til funksjoner. For noen tilfeller ønsker du likevel å stole på lavnivå serveren, slik som:

- Bedre arkitektur. Det er mulig å lage en ren arkitektur med både den vanlige serveren og en lavnivå server, men det kan argumenteres for at det er litt enklere med en lavnivå server.
- Funksjonstilgjengelighet. Noen avanserte funksjoner kan bare brukes med en lavnivå server. Du vil se dette i senere kapitler når vi legger til sampling og elicitation.

## Vanlig server vs lavnivå server

Slik ser opprettelsen av en MCP Server ut med den vanlige serveren

**Python**

```python
mcp = FastMCP("Demo")

# Legg til et tillegg verktøy
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

// Legg til et tilleggsværktøy
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

Poenget er at du eksplisitt legger til hvert verktøy, ressurs eller prompt som du vil serveren skal ha. Det er ingenting galt med det.  

### Lavnivå server-tilnærming

Men når du bruker lavnivå server-tilnærmingen må du tenke annerledes. I stedet for å registrere hvert verktøy, lager du i stedet to behandlere per funksjonstype (verktøy, ressurser eller prompts). Så for eksempel verktøy har da bare to funksjoner slik:

- Liste opp alle verktøy. En funksjon er ansvarlig for alle forsøk på å liste verktøy.
- håndtere å kalle alle verktøy. Her er det også bare én funksjon som håndterer kall til et verktøy.

Det høres ut som potensielt mindre arbeid, ikke sant? Så i stedet for å registrere et verktøy, trenger jeg bare å sørge for at verktøyet vises når jeg lister alle verktøy og at det kalles når det kommer en forespørsel om å kalle et verktøy. 

La oss se på hvordan koden nå ser ut:

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
  // Returner listen over registrerte verktøy
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

Her har vi nå en funksjon som returnerer en liste med funksjoner. Hver oppføring i verktøyslisten har nå felt som `name`, `description` og `inputSchema` for å samsvare med returtypen. Dette gjør at vi kan legge verktøyene og funksjonsdefinisjonen et annet sted. Vi kan nå lage alle våre verktøy i en verktøymappe, og det samme gjelder for alle funksjonene dine, slik at prosjektet ditt plutselig kan organiseres slik:

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

Det er flott, arkitekturen vår kan gjøres ganske ryddig.

Hva med å kalle verktøy, er det samme idéen da, én håndterer for å kalle et verktøy, uansett hvilket verktøy? Ja, akkurat, her er koden for det:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools er et ordbok med verktøynavn som nøkler
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
    // TODO kall verktøyet,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Som du kan se fra koden ovenfor må vi tolke ut hvilket verktøy som skal kalles, og med hvilke argumenter, og så må vi gå videre for å kalle verktøyet.

## Forbedre tilnærmingen med validering

Så langt har du sett hvordan alle dine registreringer for å legge til verktøy, ressurser og prompts kan erstattes med disse to behandlerne per funksjonstype. Hva mer må vi gjøre? Vel, vi bør legge til en form for validering for å sikre at verktøyet kalles med riktige argumenter. Hver runtime har sin egen løsning for dette, for eksempel bruker Python Pydantic og TypeScript bruker Zod. Ideen er at vi gjør følgende:

- Flytte logikken for å lage en funksjon (verktøy, ressurs eller prompt) til sin dedikerte mappe.
- Legge til en måte å validere en innkommende forespørsel som for eksempel ber om å kalle et verktøy.

### Lage en funksjon

For å lage en funksjon må vi lage en fil for den funksjonen og sørge for at den har obligatoriske felt som kreves av den funksjonen. Hvilke felt som kreves varierer litt mellom verktøy, ressurser og prompts.

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
        # Valider input ved bruk av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: legg til Pydantic, slik at vi kan lage en AddInputModel og validere argumenter

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

her kan du se hvordan vi gjør følgende:

- Lager et skjema ved å bruke Pydantic `AddInputModel` med feltene `a` og `b` i filen *schema.py*.
- Prøver å tolke den innkommende forespørselen som typen `AddInputModel`, hvis det er en mismatch i parametere krasjer dette:

   ```python
   # add.py
    try:
        # Valider inndata ved bruk av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan velge om du vil legge denne tolkingslogikken i selve verktøykallet eller i håndteringsfunksjonen.

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

- I håndteringen som tar seg av alle verktøykall, prøver vi nå å tolke innkommende forespørsel inn i verktøyets definerte skjema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    hvis det fungerer, går vi videre til å kalle selve verktøyet:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du ser skaper denne tilnærmingen en flott arkitektur siden alt har sin plass, *server.ts* er en veldig liten fil som bare kobler opp forespørselsbehandlerne og hver funksjon ligger i sin respektive mappe, f.eks. tools/, resources/ eller /prompts.

Flott, la oss prøve å bygge dette nå. 

## Øvelse: Lage en lavnivå server

I denne øvelsen gjør vi følgende:

1. Lage en lavnivå server som håndterer listing av verktøy og kalling av verktøy.
1. Implementere en arkitektur du kan bygge videre på.
1. Legge til validering for å sikre at verktøykallene dine blir riktig validert.

### -1- Lage en arkitektur

Det første vi må ta tak i er en arkitektur som hjelper oss å skalere etter hvert som vi legger til flere funksjoner, slik ser den ut:

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

Nå har vi satt opp en arkitektur som sikrer at vi enkelt kan legge til nye verktøy i en tools-mappe. Føl deg fri til å følge dette for å legge til undermapper for ressurser og prompts.

### -2- Lage et verktøy

La oss se hvordan det ser ut å lage et verktøy. Først må det lages i sin *tool*-undermappe slik:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valider input ved hjelp av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: legg til Pydantic, slik at vi kan opprette en AddInputModel og validere args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Det vi ser her er hvordan vi definerer navn, beskrivelse og inputskjema med Pydantic og en håndterer som kalles når dette verktøyet blir kalt. Til slutt eksponerer vi `tool_add` som er en ordbok som inneholder alle disse egenskapene.

Det finnes også *schema.py* som brukes til å definere inntaksskjemaet for verktøyet vårt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi må også fylle ut *__init__.py* for å sikre at tools-mappen behandles som et modul. I tillegg må vi eksponere modulene inni den slik:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Vi kan fortsette å legge til i denne filen etter hvert som vi legger til flere verktøy.

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

Her lager vi en ordbok bestående av egenskapene:

- name, dette er navnet på verktøyet.
- rawSchema, dette er Zod-skjemaet som brukes til å validere innkommende forespørsler om å kalle dette verktøyet.
- inputSchema, dette skjemaet brukes av håndtereren.
- callback, dette brukes til å påkalle verktøyet.

Det finnes også `Tool` som brukes til å konvertere denne ordboken til en type som mcp-serverhåndtereren kan akseptere, og det ser slik ut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og det finnes *schema.ts* hvor vi lagrer inntaksskjemaene for hvert verktøy som ser slik ut med bare ett skjema her nå, men etter hvert som vi legger til verktøy kan vi legge til flere oppføringer:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Flott, la oss gå videre til å håndtere listing av verktøy nå.

### -3- Håndtere opplisting av verktøy

Neste steg, for å håndtere opplisting av verktøy, må vi sette opp en forespørselsbehandler for det. Her er hva vi må legge til i serverfilen:

**Python**

```python
# kode utelatt for korthet
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

Her legger vi til dekoratoren `@server.list_tools` og implementasjonsfunksjonen `handle_list_tools`. I sistnevnte må vi produsere en liste av verktøy. Legg merke til at hvert verktøy må ha et navn, en beskrivelse og inputSchema.   

**TypeScript**

For å sette opp forespørselsbehandleren for å liste verktøy, må vi kalle `setRequestHandler` på serveren med et skjema som passer det vi prøver å gjøre, i dette tilfellet `ListToolsRequestSchema`. 

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
// kode utelatt for korthet
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returner listen over registrerte verktøy
  return {
    tools: tools
  };
});
```

Flott, nå har vi løst den biten med å liste verktøy, la oss se på hvordan vi kan kalle verktøy deretter.

### -4- Håndtere å kalle et verktøy

For å kalle et verktøy må vi sette opp en annen forespørselsbehandler, denne gangen fokusert på å håndtere en forespørsel som spesifiserer hvilken funksjon som skal kalles og med hvilke argumenter.

**Python**

La oss bruke dekoratoren `@server.call_tool` og implementere den med en funksjon som `handle_call_tool`. Inne i denne funksjonen må vi tolke ut verktøyets navn, argumenter og sikre at argumentene er gyldige for det aktuelle verktøyet. Vi kan enten validere argumentene i denne funksjonen eller videre ned i det faktiske verktøyet.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # verktøy er et ordbok med verktøynavn som nøkler
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # kall verktøyet
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Slik foregår det:

- Verktøynavnet vårt finnes allerede som input-parameter `name`, som også er sant for argumentene våre i form av `arguments` ordboken.

- Verktøyet kalles med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen av argumentene skjer i `handler`-egenskapen som peker til en funksjon, hvis det feiler kastes en unntak. 

Der, nå har vi full forståelse av opplisting og kalling av verktøy ved bruk av en lavnivå server.

Se det [fullstendige eksempelet](./code/README.md) her

## Oppgave

Utvid koden du har fått med en rekke verktøy, ressurser og prompt og reflekter over hvordan du bare trenger å legge til filer i tools-mappen og ingen andre steder. 

*Ingen løsning gitt*

## Oppsummering

I dette kapitlet så vi hvordan lavnivå server-tilnærmingen fungerte og hvordan det kan hjelpe oss å lage en fin arkitektur vi kan bygge videre på. Vi diskuterte også validering, og du ble vist hvordan du kan jobbe med valideringsbiblioteker for å lage skjemaer til innholdsvalidering.

## Hva er neste

- Neste: [Simple Authentication](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets morsmål bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Avansert serverbruk

Det finnes to forskjellige typer servere tilgjengelige i MCP SDK, din vanlige server og lavnivå-serveren. Normalt ville du brukt den vanlige serveren for å legge til funksjoner. I noen tilfeller vil du derimot benytte lavnivå-serveren, slik som for:

- Bedre arkitektur. Det er mulig å lage en ryddig arkitektur med både den vanlige serveren og en lavnivå-server, men det kan argumenteres for at det er litt enklere med en lavnivå-server.
- Funksjonsmuligheter. Noen avanserte funksjoner kan kun brukes med en lavnivå-server. Dette vil du se i senere kapitler når vi legger til sampling og elicitation.

## Vanlig server vs lavnivå-server

Slik ser opprettelsen av en MCP-server ut med den vanlige serveren

**Python**

```python
mcp = FastMCP("Demo")

# Legg til et tilleggverktøy
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

// Legg til et tillegg verktøy
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

Poenget er at du eksplisitt legger til hvert verktøy, ressurs eller prompt som du ønsker at serveren skal ha. Det er ingenting galt med det.  

### Lavnivå-server tilnærming

Når du bruker lavnivå-server tilnærmingen må du tenke annerledes. Istedenfor å registrere hvert verktøy, lager du to håndterere per funksjonstype (verktøy, ressurser eller prompts). For eksempel har verktøy bare to funksjoner som følger:

- Liste opp alle verktøy. En funksjon vil ha ansvar for alle forsøk på å liste verktøy.
- Håndtere kall til alle verktøy. Også her er det kun én funksjon som håndterer kall til et verktøy.

Det høres ut som potensielt mindre arbeid, ikke sant? Så i stedet for å registrere et verktøy, må jeg bare sørge for at verktøyet listes opp når jeg lister alle verktøy og at det kalles når det kommer en innkommende forespørsel om å kalle et verktøy.

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

Her har vi nå en funksjon som returnerer en liste funksjoner. Hver post i verktøyslisten har felter som `name`, `description` og `inputSchema` for å tilfredsstille returtypen. Dette gjør at vi kan plassere våre verktøy og funksjonsdefinisjon andre steder. Vi kan nå opprette alle verktøyene våre i en verktøysmappe, og det samme gjelder alle funksjonene slik at prosjektet ditt plutselig kan organiseres slik:

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

Hva med å kalle verktøy, er det samme idéen, én håndterer for å kalle et verktøy, uansett hvilket? Ja, akkurat, her er koden for det:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # verktøy er en ordbok med verktøynavn som nøkler
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

Som du kan se fra koden ovenfor, må vi parse ut hvilket verktøy som skal kalles, og med hvilke argumenter, og så må vi gå videre med å kalle verktøyet.

## Forbedre tilnærmingen med validering

Så langt har du sett hvordan alle registreringer for å legge til verktøy, ressurser og prompts kan erstattes med disse to håndtererne per funksjonstype. Hva mer må vi gjøre? Vel, vi bør legge til en form for validering for å sikre at verktøyet kalles med riktige argumenter. Hver runtime har sin egen løsning på dette, for eksempel bruker Python Pydantic og TypeScript bruker Zod. Ideen er at vi gjør følgende:

- Flytte logikken for å lage en funksjon (verktøy, ressurs eller prompt) til sin dedikerte mappe.
- Legge til en måte å validere en innkommende forespørsel som for eksempel ber om å kalle et verktøy.

### Opprett en funksjon

For å opprette en funksjon må vi lage en fil for den funksjonen og sørge for at den har de obligatoriske feltene som kreves for den funksjonen. Hvilke felt som kreves varierer litt mellom verktøy, ressurser og prompts.

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

    # TODO: legg til Pydantic, så vi kan lage en AddInputModel og validere argumenter

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Her kan du se hvordan vi gjør følgende:

- Opprette et skjema med Pydantic `AddInputModel` med feltene `a` og `b` i filen *schema.py*.
- Forsøke å parse den innkommende forespørselen til typen `AddInputModel`, hvis det er avvik i parametrene vil dette krasje:

   ```python
   # add.py
    try:
        # Valider input ved bruk av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan selv velge om du vil legge denne parse-logikken i selve verktøykallet eller i håndtererfunksjonen.

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

- I håndtereren som håndterer alle kall til verktøy, prøver vi nå å parse den innkommende forespørselen til verktøyets definerte skjema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Hvis det fungerer, går vi videre til å kalle selve verktøyet:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se skaper denne tilnærmingen en flott arkitektur ettersom alt har sin plass, *server.ts* er en veldig liten fil som bare kopler opp forespørselshåndterere, og hver funksjon ligger i sin respektive mappe, det vil si tools/, resources/, eller /prompts/.

Flott, la oss prøve å bygge dette neste.

## Øvelse: Opprette en lavnivå-server

I denne øvelsen skal vi gjøre følgende:

1. Lage en lavnivå-server som håndterer listing av verktøy og kall til verktøy.
1. Implementere en arkitektur du kan bygge videre på.
1. Legge til validering for å sikre at dine verktøykall valideres riktig.

### -1- Lag en arkitektur

Det første vi må adressere er en arkitektur som hjelper oss å skalere når vi legger til flere funksjoner, slik ser den ut:

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

Nå har vi satt opp en arkitektur som gjør at vi enkelt kan legge til nye verktøy i en tools-mappe. Føl deg fri til å følge denne for å legge til undermapper for ressurser og prompts.

### -2- Lage et verktøy

La oss se hvordan det ser ut å lage et verktøy. Først må det opprettes i sin *tool*-undermappe slik:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valider input ved å bruke Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: legg til Pydantic, så vi kan lage en AddInputModel og validere argumenter

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Det vi ser her er hvordan vi definerer navn, beskrivelse, og input-skjema ved bruk av Pydantic, samt en håndterer som blir kalt når dette verktøyet blir kalt. Til slutt eksponerer vi `tool_add` som er en ordbok som holder alle disse egenskapene.

Det finnes også *schema.py* som brukes for å definere input-skjemaet som brukes av verktøyet vårt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi må også fylle ut *__init__.py* for å sikre at tools-mappen behandles som en modul. I tillegg må vi eksponere modulene inni den slik:

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

Her lager vi et objekt bestående av følgende egenskaper:

- name, dette er navnet på verktøyet.
- rawSchema, dette er Zod-skjemaet, det vil brukes for å validere innkommende forespørsler for å kalle dette verktøyet.
- inputSchema, dette skjemaet vil brukes av håndtereren.
- callback, dette brukes for å kalle verktøyet.

Det finnes også `Tool` som brukes for å konvertere dette objektet til en type MCP-server håndterer kan akseptere og det ser slik ut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og det finnes *schema.ts* hvor vi lagrer input-skjemaene for hvert verktøy, som ser slik ut med kun ett skjema foreløpig, men etter hvert som vi legger til verktøy kan vi legge til flere oppføringer:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Flott, la oss gå videre til å håndtere listing av verktøy nå.

### -3- Håndtere listing av verktøy

Neste trinn, for å håndtere listing av verktøy, må vi sette opp en forespørselsbehandler for det. Slik ser det ut å legge det til i server-filen:

**Python**

```python
# kode utelatt for kortfattethet
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

Her legger vi til dekoratøren `@server.list_tools` og implementerende funksjon `handle_list_tools`. I sistnevnte må vi produsere en liste av verktøy. Legg merke til at hvert verktøy må ha navn, beskrivelse og inputSchema.   

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

Flott, nå har vi løst delen med å liste verktøy, la oss se på hvordan vi kan kalle verktøy neste.

### -4- Håndtere kall til et verktøy

For å kalle et verktøy må vi sette opp en ny forespørselsbehandler, denne gangen fokusert på å håndtere en forespørsel som spesifiserer hvilken funksjon som skal kalles og med hvilke argumenter.

**Python**

La oss bruke dekoratøren `@server.call_tool` og implementere den med en funksjon som `handle_call_tool`. Inni den funksjonen må vi parse ut verktøy-navnet, dets argumenter, og sørge for at argumentene er gyldige for det aktuelle verktøyet. Vi kan validere argumentene enten i denne funksjonen eller videre ned i det faktiske verktøyet.

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

Slik fungerer det:

- Verktøy-navnet vårt er allerede tilgjengelig som input-parameteren `name` som også gjelder argumentene i form av `arguments`-ordboken.

- Verktøyet kalles med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen av argumentene skjer i `handler`-egenskapen som peker til en funksjon; hvis det feiler vil det kaste et unntak.

Der har du det, nå har vi en full forståelse av listing og kall til verktøy ved å bruke en lavnivå-server.

Se det [fullstendige eksempelet](./code/README.md) her

## Oppgave

Utvid koden du har fått med en rekke verktøy, ressurser og prompts og reflekter over hvordan du merker at du bare trenger å legge til filer i tools-katalogen og ingen andre steder.

*Ingen løsning levert*

## Oppsummering

I dette kapitlet så vi hvordan lavnivå-server tilnærmingen fungerte og hvordan det kan hjelpe oss å lage en fin arkitektur vi kan fortsette å bygge på. Vi diskuterte også validering, og du ble vist hvordan du kan jobbe med valideringsbiblioteker for å lage skjemaer for inputvalidering.

## Hva er neste

- Neste: [Enkel autentisering](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
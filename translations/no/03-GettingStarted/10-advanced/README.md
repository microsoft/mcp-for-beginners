# Avansert bruk av server

Det finnes to forskjellige typer servere som eksponeres i MCP SDK: den vanlige serveren og lavnivåserveren. Vanligvis bruker du den vanlige serveren for å legge til funksjoner. I noen tilfeller kan det imidlertid være nødvendig å bruke lavnivåserveren, for eksempel:

- Bedre arkitektur. Det er mulig å lage en ren arkitektur med både den vanlige serveren og lavnivåserveren, men det kan argumenteres for at det er litt enklere med lavnivåserveren.
- Funksjonalitet. Noen avanserte funksjoner kan kun brukes med lavnivåserveren. Du vil se dette i senere kapitler når vi legger til sampling og elicitering.

## Vanlig server vs lavnivåserver

Slik ser opprettelsen av en MCP-server ut med den vanlige serveren:

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

Poenget her er at du eksplisitt legger til hvert verktøy, ressurs eller prompt som du vil at serveren skal ha. Det er ingenting galt med det.  

### Tilnærming med lavnivåserver

Når du bruker lavnivåserveren, må du tenke litt annerledes. I stedet for å registrere hvert verktøy, oppretter du to håndteringsfunksjoner per funksjonstype (verktøy, ressurser eller prompts). For eksempel for verktøy, har du kun to funksjoner som ser slik ut:

- Liste alle verktøy. Én funksjon er ansvarlig for alle forsøk på å liste verktøy.
- Håndtere kall til alle verktøy. Her er det også kun én funksjon som håndterer kall til et verktøy.

Det høres ut som potensielt mindre arbeid, ikke sant? I stedet for å registrere et verktøy, trenger jeg bare å sørge for at verktøyet er oppført når jeg lister alle verktøy, og at det blir kalt når det kommer en forespørsel om å bruke et verktøy.

La oss se hvordan koden ser ut nå:

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

Her har vi nå en funksjon som returnerer en liste over funksjoner. Hver oppføring i verktøyslisten har nå felt som `name`, `description` og `inputSchema` for å følge returtypen. Dette gjør det mulig å plassere definisjonen av verktøy og funksjoner andre steder. Vi kan nå opprette alle verktøyene våre i en verktøysmappe, og det samme gjelder for alle funksjonene dine, slik at prosjektet plutselig kan organiseres slik:

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

Hva med å kalle verktøy, er det samme idé, én håndteringsfunksjon for å kalle et verktøy, uansett hvilket verktøy? Ja, akkurat, her er koden for det:

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

Som du kan se fra koden ovenfor, må vi analysere hvilket verktøy som skal kalles, med hvilke argumenter, og deretter fortsette med å kalle verktøyet.

## Forbedre tilnærmingen med validering

Så langt har du sett hvordan alle registreringene for å legge til verktøy, ressurser og prompts kan erstattes med disse to håndteringsfunksjonene per funksjonstype. Hva annet må vi gjøre? Vel, vi bør legge til en form for validering for å sikre at verktøyet blir kalt med riktige argumenter. Hvert runtime-miljø har sin egen løsning for dette, for eksempel bruker Python Pydantic og TypeScript bruker Zod. Ideen er at vi gjør følgende:

- Flytt logikken for å opprette en funksjon (verktøy, ressurs eller prompt) til sin dedikerte mappe.
- Legg til en måte å validere en innkommende forespørsel som ber om for eksempel å kalle et verktøy.

### Opprette en funksjon

For å opprette en funksjon, må vi opprette en fil for den funksjonen og sørge for at den har de obligatoriske feltene som kreves for den funksjonen. Hvilke felt som kreves, varierer litt mellom verktøy, ressurser og prompts.

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

Her kan du se hvordan vi gjør følgende:

- Opprett et skjema ved hjelp av Pydantic `AddInputModel` med feltene `a` og `b` i filen *schema.py*.
- Forsøk å analysere den innkommende forespørselen til å være av typen `AddInputModel`. Hvis det er en mismatch i parametere, vil dette krasje:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan velge om du vil plassere denne analyse-logikken i selve verktøykallet eller i håndteringsfunksjonen.

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

- I håndteringsfunksjonen som håndterer alle verktøykall, prøver vi nå å analysere den innkommende forespørselen til verktøyets definerte skjema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Hvis det fungerer, fortsetter vi med å kalle det faktiske verktøyet:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se, skaper denne tilnærmingen en flott arkitektur der alt har sin plass. *server.ts* er en veldig liten fil som kun kobler opp forespørselshåndterere, og hver funksjon ligger i sine respektive mapper, dvs. tools/, resources/ eller prompts/.

Flott, la oss prøve å bygge dette neste.

## Øvelse: Opprette en lavnivåserver

I denne øvelsen skal vi gjøre følgende:

1. Opprette en lavnivåserver som håndterer listing av verktøy og kall til verktøy.
1. Implementere en arkitektur du kan bygge videre på.
1. Legge til validering for å sikre at verktøykallene dine blir korrekt validert.

### -1- Opprette en arkitektur

Det første vi må adressere er en arkitektur som hjelper oss å skalere etter hvert som vi legger til flere funksjoner. Slik ser det ut:

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

Nå har vi satt opp en arkitektur som sikrer at vi enkelt kan legge til nye verktøy i en verktøysmappe. Følg gjerne dette for å legge til undermapper for ressurser og prompts.

### -2- Opprette et verktøy

La oss se hvordan det ser ut å opprette et verktøy. Først må det opprettes i sin *tool*-undermappe slik:

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

Her ser vi hvordan vi definerer navn, beskrivelse, et input-skjema ved hjelp av Pydantic og en håndteringsfunksjon som vil bli kalt når dette verktøyet brukes. Til slutt eksponerer vi `tool_add`, som er en ordbok som inneholder alle disse egenskapene.

Det finnes også *schema.py*, som brukes til å definere input-skjemaet som brukes av verktøyet vårt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi må også fylle ut *__init__.py* for å sikre at verktøysmappen behandles som et modul. I tillegg må vi eksponere modulene innenfor den slik:

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

Her oppretter vi en ordbok som består av egenskaper:

- name, dette er navnet på verktøyet.
- rawSchema, dette er Zod-skjemaet, som vil bli brukt til å validere innkommende forespørsler for å kalle dette verktøyet.
- inputSchema, dette skjemaet vil bli brukt av håndteringsfunksjonen.
- callback, dette brukes til å kalle verktøyet.

Det finnes også `Tool`, som brukes til å konvertere denne ordboken til en type som MCP-serverhåndtereren kan akseptere, og det ser slik ut:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og det finnes *schema.ts*, der vi lagrer input-skjemaene for hvert verktøy. Det ser slik ut med kun ett skjema for øyeblikket, men etter hvert som vi legger til verktøy, kan vi legge til flere oppføringer:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Flott, la oss gå videre til å håndtere listing av verktøy.

### -3- Håndtere listing av verktøy

For å håndtere listing av verktøy, må vi sette opp en forespørselshåndterer for det. Her er hva vi må legge til i serverfilen:

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

Her legger vi til dekoratoren `@server.list_tools` og implementeringsfunksjonen `handle_list_tools`. I sistnevnte må vi produsere en liste over verktøy. Legg merke til hvordan hvert verktøy må ha et navn, en beskrivelse og et inputSchema.   

**TypeScript**

For å sette opp forespørselshåndtereren for listing av verktøy, må vi kalle `setRequestHandler` på serveren med et skjema som passer til det vi prøver å gjøre, i dette tilfellet `ListToolsRequestSchema`. 

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

Flott, nå har vi løst delen med listing av verktøy. La oss se på hvordan vi kan kalle verktøy neste.

### -4- Håndtere kall til et verktøy

For å kalle et verktøy, må vi sette opp en annen forespørselshåndterer, denne gangen fokusert på å håndtere en forespørsel som spesifiserer hvilken funksjon som skal kalles og med hvilke argumenter.

**Python**

La oss bruke dekoratoren `@server.call_tool` og implementere den med en funksjon som `handle_call_tool`. Innenfor den funksjonen må vi analysere verktøynavnet, dets argumenter og sikre at argumentene er gyldige for det aktuelle verktøyet. Vi kan enten validere argumentene i denne funksjonen eller nedstrøms i det faktiske verktøyet.

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

Her er hva som skjer:

- Verktøynavnet vårt er allerede tilgjengelig som inputparameteren `name`, og det samme gjelder argumentene i form av ordboken `arguments`.

- Verktøyet kalles med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen av argumentene skjer i `handler`-egenskapen, som peker til en funksjon. Hvis det mislykkes, vil det kaste en unntak.

Der, nå har vi en full forståelse av hvordan man lister og kaller verktøy ved hjelp av en lavnivåserver.

Se [fullt eksempel](./code/README.md) her.

## Oppgave

Utvid koden du har fått med flere verktøy, ressurser og prompts, og reflekter over hvordan du merker at du kun trenger å legge til filer i verktøysmappen og ingen andre steder. 

*Ingen løsning gitt*

## Oppsummering

I dette kapittelet så vi hvordan tilnærmingen med lavnivåserver fungerer, og hvordan det kan hjelpe oss med å lage en ryddig arkitektur vi kan bygge videre på. Vi diskuterte også validering, og du ble vist hvordan du kan bruke valideringsbiblioteker til å opprette skjemaer for inputvalidering.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
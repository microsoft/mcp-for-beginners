# Avanceret serverbrug

Der er to forskellige typer servere eksponeret i MCP SDK'en, din normale server og den lavniveau-server. Normalt ville du bruge den almindelige server til at tilføje funktioner til den. I nogle tilfælde vil du dog gerne stole på lavniveau-serveren, såsom:

- Bedre arkitektur. Det er muligt at skabe en ren arkitektur med både den almindelige server og en lavniveau-server, men det kan argumenteres for, at det er lidt lettere med en lavniveau-server.
- Funktionstilgængelighed. Nogle avancerede funktioner kan kun bruges med en
    lavniveau-server. Senere kapitler dækker Elicitation og den ældre Sampling
    funktion, som er forældet i MCP `2026-07-28`.

## Almindelig server vs lavniveau-server

Her er, hvordan oprettelsen af en MCP-server ser ud med den almindelige server

**Python**

```python
mcp = FastMCP("Demo")

# Tilføj et additionsværktøj
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

// Tilføj et additionsværktøj
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

Pointen er, at du eksplicittilføjer hvert værktøj, ressource eller prompt, som du vil have serveren til at have. Der er ikke noget galt med det.  

### Lavniveau-server tilgang

Men når du bruger lavniveau-server tilgangen, skal du tænke anderledes. I stedet for at registrere hvert værktøj, opretter du to håndteringsfunktioner pr. funktionstype (værktøjer, ressourcer eller prompts). For eksempel har værktøjer så kun to funktioner, sådan her:

- Liste over alle værktøjer. Én funktion ville være ansvarlig for alle forsøg på at liste værktøjer.
- Håndtere kald til alle værktøjer. Her er der også kun én funktion, der håndterer kald til et værktøj.

Det lyder som potentielt mindre arbejde, ikke? Så i stedet for at registrere et værktøj, skal jeg bare sikre mig, at værktøjet listes, når jeg lister alle værktøjer, og at det kaldes, når der kommer en forespørgsel om at kalde et værktøj. 

Lad os se på, hvordan koden nu ser ud:

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
  // Returner listen over registrerede værktøjer
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

Her har vi nu en funktion, der returnerer en liste over funktioner. Hver post i værktøjslisten har nu felter som `name`, `description` og `inputSchema` for at opfylde returtypen. Dette gør det muligt for os at placere vores værktøjer og funktionsdefinition et andet sted. Vi kan nu oprette alle vores værktøjer i en mappe tools, og det samme gælder for alle dine funktioner, så dit projekt pludselig kan organiseres sådan her:

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

Det er godt, vores arkitektur kan gøres ganske ren.

Hvad med at kalde værktøjer, er det den samme idé, én håndtering til at kalde et værktøj, hvilket som helst værktøj? Ja, præcis, her er koden til det:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools er et ordbog med værktøjsnavne som nøgler
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
    // TODO kald værktøjet,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Som du kan se i ovenstående kode, skal vi parse det værktøj ud, der skal kaldes, og med hvilke argumenter, og derefter skal vi fortsætte med at kalde værktøjet.

## Forbedring af tilgangen med validering

Indtil nu har du set, hvordan alle dine registreringer til at tilføje værktøjer, ressourcer og prompts kan erstattes med disse to håndteringsfunktioner pr. funktionstype. Hvad mere skal vi gøre? Jo, vi bør tilføje en form for validering for at sikre, at værktøjet kaldes med de rigtige argumenter. Hver runtime har deres egen løsning til dette, for eksempel bruger Python Pydantic og TypeScript bruger Zod. Ideen er, at vi gør følgende:

- Flytte logikken for at oprette en funktion (værktøj, ressource eller prompt) til dens dedikerede mappe.
- Tilføje en måde at validere en indkommende forespørgsel, der for eksempel anmoder om at kalde et værktøj.

### Opret en funktion

For at oprette en funktion skal vi oprette en fil for denne funktion og sikre, at den har de obligatoriske felter, som kræves af den pågældende funktionstype. Hvilke felter der kræves varierer lidt mellem værktøjer, ressourcer og prompts.

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
        # Valider input ved hjælp af Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tilføj Pydantic, så vi kan oprette en AddInputModel og validere argumenter

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

her kan du se, hvordan vi gør følgende:

- Opretter et schema ved hjælp af Pydantic `AddInputModel` med felterne `a` og `b` i filen *schema.py*.
- Forsøger at parse den indkommende forespørgsel som typen `AddInputModel`, hvis der er uoverensstemmelse i parametrene, vil dette fejle:

   ```python
   # add.py
    try:
        # Valider input ved hjælp af Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan vælge, om du vil have denne parselogik i selve værktøjskaldet eller i håndteringsfunktionen.

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

- I håndteringen, der beskæftiger sig med alle værktøjskald, forsøger vi nu at parse den indkommende forespørgsel til det definerede schema for værktøjet:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    hvis det virker, fortsætter vi med at kalde det faktiske værktøj:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se, skaber denne tilgang en god arkitektur, da alt har sin plads. *server.ts* er en meget lille fil, som kun forbinder forespørgsels-håndtererne, og hver funktion ligger i deres respektive mapper, dvs. tools/, resources/ eller prompts/.

Fantastisk, lad os prøve at bygge dette næste.

## Øvelse: Opret en lavniveau-server

I denne øvelse vil vi gøre følgende:

1. Oprette en lavniveau-server, der håndterer opremsning og kald af værktøjer.
1. Implementere en arkitektur, du kan bygge videre på.
1. Tilføje validering for at sikre, at dine værktøjskald valideres korrekt.

### -1- Opret en arkitektur

Det første, vi skal tage fat på, er en arkitektur, der hjælper os med at skalere, efterhånden som vi tilføjer flere funktioner, sådan her ser det ud:

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

Nu har vi sat en arkitektur op, som sikrer, at vi nemt kan tilføje nye værktøjer i en mappe tools. Føl dig fri til at følge denne for at tilføje undermapper for resources og prompts.

### -2- Opret et værktøj

Lad os se på, hvordan man opretter et værktøj næste gang. Først skal det oprettes i sin *tool* undermappe sådan her:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valider input ved hjælp af Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tilføj Pydantic, så vi kan oprette en AddInputModel og validere argumenter

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Det, vi ser her, er hvordan vi definerer navn, beskrivelse og inputschema ved hjælp af Pydantic og en håndteringsfunktion, der bliver kaldt, når dette værktøj bliver kaldt. Til sidst eksponerer vi `tool_add`, som er en ordbog, der indeholder alle disse egenskaber.

Der er også *schema.py*, som bruges til at definere inputschemat, der bruges af vores værktøj:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi skal også udfylde *__init__.py* for at sikre, at værktøjsmappen behandles som et modul. Derudover skal vi eksponere modulerne inden for den sådan her:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Vi kan fortsætte med at tilføje til denne fil, når vi tilføjer flere værktøjer.

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

Her opretter vi en ordbog bestående af egenskaber:

- name, det er navnet på værktøjet.
- rawSchema, dette er Zod-schemaet, det vil blive brugt til at validere indkommende kald til dette værktøj.
- inputSchema, dette schema vil blive brugt af håndteringsfunktionen.
- callback, dette bruges til at påkalde værktøjet.

Der er også `Tool`, som bruges til at konvertere denne ordbog til en type, som mcp's serverhåndtering kan acceptere, og det ser sådan ud:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og der er *schema.ts*, hvor vi gemmer inputschemata for hvert værktøj, som ser sådan ud med kun ét schema for nu, men efterhånden som vi tilføjer værktøjer, kan vi tilføje flere:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Fantastisk, lad os fortsætte med at håndtere opremsningen af vores værktøjer næste gang.

### -3- Håndter værktøjsopremsning

Dernæst, for at håndtere opremsning af vores værktøjer, skal vi oprette en forespørgsels-håndtering til det. Her er, hvad vi skal tilføje til vores serverfil:

**Python**

```python
# kode udeladt for korthed
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

Her tilføjer vi dekorationen `@server.list_tools` og implementeringsfunktionen `handle_list_tools`. I sidstnævnte skal vi producere en liste over værktøjer. Bemærk, at hvert værktøj skal have et navn, en beskrivelse og et inputSchema.   

**TypeScript**

For at oprette forespørgsels-håndteringen til at liste værktøjer, skal vi kalde `setRequestHandler` på serveren med et schema, der passer til det, vi forsøger at gøre, i dette tilfælde `ListToolsRequestSchema`. 

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
// kode udeladt for korthed
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returner listen over registrerede værktøjer
  return {
    tools: tools
  };
});
```

Fantastisk, nu har vi løst delen med at liste værktøjer, lad os se på, hvordan vi kunne kalde værktøjer næste gang.

### -4- Håndter kald af værktøj

For at kalde et værktøj, skal vi sætte en anden forespørgsels-håndtering op, denne gang fokuseret på at behandle en forespørgsel, der specificerer, hvilken funktion der skal kaldes og med hvilke argumenter.

**Python**

Lad os bruge dekorationen `@server.call_tool` og implementere det med en funktion som `handle_call_tool`. Inde i den funktion skal vi parse værktøjets navn, dets argument og sikre, at argumenterne er gyldige for det pågældende værktøj. Vi kan enten validere argumenterne i denne funktion eller downstream i det faktiske værktøj.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools er en ordbog med værktøjsnavne som nøgler
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # påkald værktøjet
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Her er, hvad der sker:

- Vores værktøjsnavn er allerede givet som inputparameteren `name`, hvilket også gælder for vores argumenter i form af ordbogen `arguments`.

- Værktøjet kaldes med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen af argumenterne sker i `handler`-egenskaben, som peger på en funktion, hvis det fejler, vil den rejse en undtagelse.

Der, nu har vi en fuld forståelse af at liste og kalde værktøjer ved brug af en lavniveau-server.

Se det [fulde eksempel](./code/README.md) her

## Opgave

Udvid den kode, du har fået, med en række værktøjer, ressourcer og prompts og reflekter over, hvordan du bemærker, at du kun behøver at tilføje filer i tools-mappen og ikke andetsteds. 

*Ingen løsning givet*

## Resumé

I dette kapitel så vi, hvordan lavniveau-server tilgangen fungerede, og hvordan det kan hjælpe os med at skabe en pæn arkitektur, som vi kan blive ved med at bygge videre på. Vi diskuterede også validering, og du blev vist, hvordan du arbejder med valideringsbiblioteker til at skabe schemas for inputvalidering.

## Hvad kommer nu

- Næste: [Simpel autentifikation](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
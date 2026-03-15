# Avanceret server brug

Der findes to forskellige typer servere i MCP SDK, din normale server og den lavniveau server. Normalt vil du bruge den almindelige server til at tilføje funktioner til den. I nogle tilfælde ønsker du dog at stole på den lavniveau server, for eksempel:

- Bedre arkitektur. Det er muligt at skabe en ren arkitektur både med den almindelige server og en lavniveau server, men det kan argumenteres for, at det er lidt nemmere med en lavniveau server.
- Funktionsmuligheder. Nogle avancerede funktioner kan kun bruges med en lavniveau server. Du vil se dette i senere kapitler, når vi tilføjer sampling og elicitation.

## Almindelig server vs lavniveau server

Sådan ser oprettelsen af en MCP Server ud med den almindelige server

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

Pointen er, at du eksplicit tilføjer hvert værktøj, ressource eller prompt, som du ønsker, at serveren skal have. Der er intet galt med det.

### Lavniveau server tilgang

Når du bruger lavniveau server tilgangen, skal du tænke anderledes. I stedet for at registrere hvert værktøj, opretter du to handlere pr. funktionstype (værktøjer, ressourcer eller prompts). For eksempel har værktøjer kun to funktioner som sådan:

- Liste over alle værktøjer. En funktion vil være ansvarlig for alle forsøg på at liste værktøjer.
- Håndtere kald til alle værktøjer. Her er der også kun én funktion, der håndterer kald til et værktøj.

Det lyder som muligvis mindre arbejde, ikke? Så i stedet for at registrere et værktøj, skal jeg bare sørge for, at værktøjet er opført, når jeg lister alle værktøjer, og at det bliver kaldt, når der er en indkommende anmodning om at kalde et værktøj.

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

Her har vi nu en funktion, der returnerer en liste over funktioner. Hvert element i værktøjslisten har nu felter som `name`, `description` og `inputSchema` for at overholde tilbagevendende typen. Dette gør os i stand til at placere vores værktøjer og funktionsdefinition andetsteds. Vi kan nu oprette alle vores værktøjer i en tools-mappe, og det samme gælder for alle dine funktioner, så dit projekt pludselig kan organiseres sådan:

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

Hvad med at kalde værktøjer, er det samme idé, så en håndterer til at kalde et værktøj, uanset hvilket værktøj? Ja, præcis, her er koden til det:

**Python**

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
    
    // args: request.params.argumenter
    // TODO kald værktøjet,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Som det ses fra koden ovenfor, skal vi parse hvilket værktøj der skal kaldes, og med hvilke argumenter, og så skal vi forsætte med at kalde værktøjet.

## Forbedre tilgangen med validering

Indtil nu har du set, hvordan alle dine registreringer til at tilføje værktøjer, ressourcer og prompts kan erstattes med disse to handlere pr. funktionstype. Hvad mere skal vi gøre? Vi bør tilføje en form for validering for at sikre, at værktøjet kaldes med de rigtige argumenter. Hver runtime har deres egen løsning til dette, for eksempel bruger Python Pydantic og TypeScript bruger Zod. Ideen er, at vi gør følgende:

- Flyt logikken for at oprette en funktion (værktøj, ressource eller prompt) til dens dedikerede mappe.
- Tilføj en måde at validere en indkommende anmodning, som f.eks. at kalde et værktøj.

### Opret en funktion

For at oprette en funktion skal vi oprette en fil for den funktion og sikre, at den har de obligatoriske felter, som kræves for den funktionstype. Hvilke felter der kræves, varierer lidt mellem værktøjer, ressourcer og prompts.

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

    # TODO: tilføj Pydantic, så vi kan oprette en AddInputModel og validere arguments

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Her kan du se, hvordan vi gør følgende:

- Opretter et schema ved hjælp af Pydantic `AddInputModel` med felterne `a` og `b` i filen *schema.py*.
- Forsøger at parse den indkommende anmodning til typen `AddInputModel`, hvis der er uoverensstemmelse i parametrene, vil dette crashe:

   ```python
   # add.py
    try:
        # Valider input ved hjælp af Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan vælge, om du vil placere denne parse-logik i selve værktøjskaldet eller i handler funktionen.

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

- I handleren, der håndterer alle kald til værktøjer, prøver vi nu at parse den indkommende anmodning ind i værktøjets definerede schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    hvis det lykkes, fortsætter vi med at kalde det faktiske værktøj:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se, skaber denne tilgang en god arkitektur, da alt har sin plads. *server.ts* er en meget lille fil, der kun forbinder request handlers, og hver funktion ligger i deres respektive mappe, dvs. tools/, resources/ eller /prompts.

Fint, lad os prøve at bygge dette næste.

## Øvelse: Opret en lavniveau server

I denne øvelse skal vi gøre følgende:

1. Oprette en lavniveau server, der håndterer listing af værktøjer og kald af værktøjer.
2. Implementere en arkitektur, du kan bygge videre på.
3. Tilføje validering for at sikre, at dine værktøjskald valideres korrekt.

### -1- Opret en arkitektur

Det første, vi skal tage fat på, er en arkitektur, der hjælper os med at skalere, efterhånden som vi tilføjer flere funktioner, sådan ser det ud:

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

Nu har vi sat en arkitektur op, som sikrer, at vi let kan tilføje nye værktøjer i en tools-mappe. Du kan frit følge denne for at tilføje undermapper til resources og prompts.

### -2- Opret et værktøj

Lad os se på, hvordan det ser ud at oprette et værktøj. Først skal det oprettes i sin *tool* undermappe sådan her:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valider input ved hjælp af Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: tilføj Pydantic, så vi kan oprette en AddInputModel og validere args

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Her ser vi, hvordan vi definerer navn, beskrivelse og input-schema ved hjælp af Pydantic samt en handler, der vil blive kaldt, når dette værktøj bliver brugt. Til sidst eksponerer vi `tool_add`, som er et dictionary, der indeholder alle disse egenskaber.

Der er også *schema.py*, som bruges til at definere input-schemaet, der anvendes af vores værktøj:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi skal også udfylde *__init__.py* for at sikre, at tools-mappen behandles som et modul. Derudover skal vi eksponere modulerne indeni sådan her:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Vi kan blive ved med at tilføje til denne fil, efterhånden som vi tilføjer flere værktøjer.

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

Her opretter vi et dictionary bestående af egenskaber:

- name, det er navnet på værktøjet.
- rawSchema, det er Zod-schemaet, som bruges til at validere indkommende anmodninger om at kalde dette værktøj.
- inputSchema, dette schema bruges af handleren.
- callback, det bruges til at påkalde værktøjet.

Der er også `Tool`, som bruges til at konvertere dette dictionary til en type, som MCP server handler kan acceptere og det ser sådan ud:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og der er *schema.ts*, hvor vi gemmer input-schemaer for hvert værktøj, som ser sådan ud, i øjeblikket med kun et schema, men når vi tilføjer værktøjer, kan vi tilføje flere poster:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Fantastisk, lad os nu fortsætte med at håndtere listingen af vores værktøjer.

### -3- Håndter listing af værktøjer

Næste skridt er at oprette en request handler til listing af værktøjer. Det skal vi tilføje til vores server fil sådan her:

**Python**

```python
# kode udeladt for overskuelighed
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

Her tilføjer vi dekoratoren `@server.list_tools` og den implementerende funktion `handle_list_tools`. I sidstnævnte skal vi producere en liste over værktøjer. Bemærk, at hvert værktøj skal have et navn, beskrivelse og inputSchema.

**TypeScript**

For at oprette request handler til listing af værktøjer, skal vi kalde `setRequestHandler` på serveren med et schema, der passer til det, vi forsøger at gøre, i dette tilfælde `ListToolsRequestSchema`.

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
// kode udeladt for overskuelighed
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returner listen over registrerede værktøjer
  return {
    tools: tools
  };
});
```

Super, nu har vi løst delen med at liste værktøjer, lad os se på, hvordan vi kan kalde værktøjer næste.

### -4- Håndter kald af værktøj

For at kalde et værktøj skal vi oprette en anden request handler, denne gang fokuseret på at håndtere en anmodning, der specificerer, hvilken funktion der skal kaldes, og med hvilke argumenter.

**Python**

Lad os bruge dekoratoren `@server.call_tool` og implementere den med en funktion som `handle_call_tool`. Inden i denne funktion skal vi udtrække værktøjets navn, argumenter og sikre, at argumenterne er gyldige for det pågældende værktøj. Vi kan enten validere argumenterne i denne funktion eller i det egentlige værktøj downstream.

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
        # kald værktøjet
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Her sker følgende:

- Værktøjets navn er allerede til stede som inputparameteren `name`, og vores argumenter er i form af `arguments` dictionary.

- Værktøjet kaldes med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen af argumenterne sker i `handler`-egenskaben, som peger på en funktion; hvis det fejler, vil det kaste en undtagelse.

Således har vi nu fuld forståelse af listing og kald af værktøjer ved brug af en lavniveau server.

Se det [fulde eksempel](./code/README.md) her

## Opgave

Udvid den kode, du har fået, med flere værktøjer, ressourcer og prompts og reflekter over, hvordan du kun behøver at tilføje filer i tools-kataloget og ikke andre steder.

*Ingen løsning givet*

## Resumé

I dette kapitel så vi, hvordan lavniveau server tilgangen fungerer, og hvordan det kan hjælpe os med at skabe en fin arkitektur, vi kan fortsætte med at bygge på. Vi diskuterede også validering, og du blev vist, hvordan man arbejder med valideringsbiblioteker til at skabe schemas til input-validering.

## Hvad er næste

- Næste: [Simpel Autentificering](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget skal betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, som måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Avanceret serverbrug

Der er to forskellige typer servere, der eksponeres i MCP SDK: din normale server og lavniveau-serveren. Normalt bruger du den almindelige server til at tilføje funktioner. I nogle tilfælde kan det dog være nødvendigt at bruge lavniveau-serveren, for eksempel:

- Bedre arkitektur. Det er muligt at skabe en ren arkitektur med både den almindelige server og lavniveau-serveren, men det kan argumenteres, at det er en smule lettere med lavniveau-serveren.
- Funktionalitet. Nogle avancerede funktioner kan kun bruges med lavniveau-serveren. Du vil se dette i senere kapitler, når vi tilføjer sampling og elicitering.

## Almindelig server vs lavniveau-server

Her er, hvordan oprettelsen af en MCP-server ser ud med den almindelige server:

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

Pointen er, at du eksplicit tilføjer hvert værktøj, ressource eller prompt, som du ønsker, at serveren skal have. Der er ikke noget galt med det.

### Lavniveau-server tilgang

Men når du bruger lavniveau-servertilgangen, skal du tænke anderledes, nemlig at i stedet for at registrere hvert værktøj, opretter du to håndteringsfunktioner pr. funktionstype (værktøjer, ressourcer eller prompts). For eksempel for værktøjer har du kun to funktioner som følger:

- Liste over alle værktøjer. Én funktion er ansvarlig for alle forsøg på at liste værktøjer.
- Håndtere kald til alle værktøjer. Her er der også kun én funktion, der håndterer kald til et værktøj.

Det lyder som potentielt mindre arbejde, ikke? Så i stedet for at registrere et værktøj, skal jeg bare sikre mig, at værktøjet er opført, når jeg lister alle værktøjer, og at det bliver kaldt, når der er en indgående anmodning om at kalde et værktøj.

Lad os se, hvordan koden nu ser ud:

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

Her har vi nu en funktion, der returnerer en liste over funktioner. Hver post i værktøjslisten har nu felter som `name`, `description` og `inputSchema` for at overholde returtypen. Dette gør det muligt for os at placere vores værktøjer og funktionsdefinitioner et andet sted. Vi kan nu oprette alle vores værktøjer i en værktøjsmappe, og det samme gælder for alle dine funktioner, så dit projekt pludselig kan organiseres sådan her:

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

Det er fantastisk, vores arkitektur kan gøres ret ren.

Hvad med at kalde værktøjer, er det samme idé, én håndteringsfunktion til at kalde et værktøj, uanset hvilket værktøj? Ja, præcis, her er koden for det:

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

Som du kan se fra ovenstående kode, skal vi udtrække det værktøj, der skal kaldes, og med hvilke argumenter, og derefter fortsætte med at kalde værktøjet.

## Forbedring af tilgangen med validering

Indtil videre har du set, hvordan alle dine registreringer for at tilføje værktøjer, ressourcer og prompts kan erstattes med disse to håndteringsfunktioner pr. funktionstype. Hvad skal vi ellers gøre? Vi bør tilføje en form for validering for at sikre, at værktøjet kaldes med de rigtige argumenter. Hver runtime har sin egen løsning til dette, for eksempel bruger Python Pydantic, og TypeScript bruger Zod. Ideen er, at vi gør følgende:

- Flyt logikken for at oprette en funktion (værktøj, ressource eller prompt) til dens dedikerede mappe.
- Tilføj en måde at validere en indgående anmodning, der for eksempel beder om at kalde et værktøj.

### Opret en funktion

For at oprette en funktion skal vi oprette en fil til den funktion og sikre, at den har de obligatoriske felter, der kræves for den funktion. Hvilke felter varierer lidt mellem værktøjer, ressourcer og prompts.

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

Her kan du se, hvordan vi gør følgende:

- Opretter et schema ved hjælp af Pydantic `AddInputModel` med felterne `a` og `b` i filen *schema.py*.
- Forsøger at parse den indgående anmodning til at være af typen `AddInputModel`. Hvis der er en mismatch i parametre, vil dette fejle:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan vælge, om du vil placere denne parsing-logik i selve værktøjskaldet eller i håndteringsfunktionen.

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

- I håndteringsfunktionen, der håndterer alle værktøjskald, forsøger vi nu at parse den indgående anmodning til værktøjets definerede schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Hvis det lykkes, fortsætter vi med at kalde det faktiske værktøj:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se, skaber denne tilgang en god arkitektur, da alt har sin plads. Filen *server.ts* er en meget lille fil, der kun forbinder anmodningshåndteringsfunktionerne, og hver funktion er i deres respektive mappe, dvs. tools/, resources/ eller prompts/.

Fantastisk, lad os prøve at bygge dette næste.

## Øvelse: Opret en lavniveau-server

I denne øvelse vil vi gøre følgende:

1. Opret en lavniveau-server, der håndterer liste over værktøjer og kald af værktøjer.
1. Implementer en arkitektur, du kan bygge videre på.
1. Tilføj validering for at sikre, at dine værktøjskald er korrekt valideret.

### -1- Opret en arkitektur

Det første, vi skal adressere, er en arkitektur, der hjælper os med at skalere, når vi tilføjer flere funktioner. Her er, hvordan det ser ud:

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

Nu har vi oprettet en arkitektur, der sikrer, at vi nemt kan tilføje nye værktøjer i en værktøjsmappe. Føl dig fri til at følge dette for at tilføje undermapper til ressourcer og prompts.

### -2- Opret et værktøj

Lad os se, hvordan oprettelsen af et værktøj ser ud næste. Først skal det oprettes i sin *tool*-undermappe som følger:

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

Her ser vi, hvordan vi definerer navn, beskrivelse, et inputschema ved hjælp af Pydantic og en håndteringsfunktion, der vil blive kaldt, når dette værktøj bliver kaldt. Til sidst eksponerer vi `tool_add`, som er en dictionary, der indeholder alle disse egenskaber.

Der er også *schema.py*, der bruges til at definere inputschemaet, der bruges af vores værktøj:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi skal også udfylde *__init__.py* for at sikre, at værktøjsmappen behandles som et modul. Derudover skal vi eksponere modulerne inden for det som følger:

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

Her opretter vi en dictionary bestående af egenskaber:

- name, dette er navnet på værktøjet.
- rawSchema, dette er Zod-schemaet, det vil blive brugt til at validere indgående anmodninger om at kalde dette værktøj.
- inputSchema, dette schema vil blive brugt af håndteringsfunktionen.
- callback, dette bruges til at kalde værktøjet.

Der er også `Tool`, der bruges til at konvertere denne dictionary til en type, som MCP-serverhåndteringen kan acceptere, og det ser sådan ud:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Og der er *schema.ts*, hvor vi gemmer inputschemas for hvert værktøj, der ser sådan ud med kun ét schema i øjeblikket, men efterhånden som vi tilføjer værktøjer, kan vi tilføje flere poster:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Fantastisk, lad os gå videre til at håndtere listen over vores værktøjer næste.

### -3- Håndter liste over værktøjer

For at håndtere listen over værktøjer skal vi oprette en anmodningshåndteringsfunktion for det. Her er, hvad vi skal tilføje til vores serverfil:

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

Her tilføjer vi dekoratoren `@server.list_tools` og den implementerende funktion `handle_list_tools`. I sidstnævnte skal vi producere en liste over værktøjer. Bemærk, hvordan hvert værktøj skal have et navn, en beskrivelse og et inputSchema.

**TypeScript**

For at oprette anmodningshåndteringsfunktionen for liste over værktøjer skal vi kalde `setRequestHandler` på serveren med et schema, der passer til det, vi forsøger at gøre, i dette tilfælde `ListToolsRequestSchema`.

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

Fantastisk, nu har vi løst delen med at liste værktøjer. Lad os se på, hvordan vi kan kalde værktøjer næste.

### -4- Håndter kald af et værktøj

For at kalde et værktøj skal vi oprette en anden anmodningshåndteringsfunktion, denne gang fokuseret på at håndtere en anmodning, der angiver, hvilken funktion der skal kaldes, og med hvilke argumenter.

**Python**

Lad os bruge dekoratoren `@server.call_tool` og implementere den med en funktion som `handle_call_tool`. Inden for den funktion skal vi udtrække værktøjets navn, dets argumenter og sikre, at argumenterne er gyldige for det pågældende værktøj. Vi kan enten validere argumenterne i denne funktion eller længere nede i det faktiske værktøj.

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

Her er, hvad der sker:

- Værktøjets navn er allerede tilgængeligt som inputparameteren `name`, hvilket også gælder for vores argumenter i form af dictionaryen `arguments`.

- Værktøjet kaldes med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen af argumenterne sker i egenskaben `handler`, som peger på en funktion. Hvis det fejler, vil det rejse en undtagelse.

Der, nu har vi en fuld forståelse af liste og kald af værktøjer ved hjælp af en lavniveau-server.

Se [det fulde eksempel](./code/README.md) her.

## Opgave

Udvid den kode, du har fået, med en række værktøjer, ressourcer og prompts, og reflekter over, hvordan du bemærker, at du kun behøver at tilføje filer i værktøjsmappen og ingen andre steder.

*Ingen løsning givet*

## Opsummering

I dette kapitel så vi, hvordan lavniveau-servertilgangen fungerede, og hvordan den kan hjælpe os med at skabe en god arkitektur, vi kan bygge videre på. Vi diskuterede også validering, og du blev vist, hvordan du arbejder med valideringsbiblioteker for at oprette schemas til inputvalidering.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
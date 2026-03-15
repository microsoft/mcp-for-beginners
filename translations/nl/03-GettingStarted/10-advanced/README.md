# Geavanceerd servergebruik

Er zijn twee verschillende types servers beschikbaar in de MCP SDK, je normale server en de low-level server. Normaal gesproken zou je de reguliere server gebruiken om functies toe te voegen. In sommige gevallen wil je echter vertrouwen op de low-level server, bijvoorbeeld bij:

- Betere architectuur. Het is mogelijk om een schone architectuur te creëren met zowel de reguliere server als een low-level server, maar er kan gesteld worden dat het iets gemakkelijker is met een low-level server.
- Beschikbaarheid van functies. Sommige geavanceerde functies kunnen alleen worden gebruikt met een low-level server. Je zult dit later in hoofdstukken zien bij het toevoegen van sampling en elicitation.

## Reguliere server versus low-level server

Zo ziet het aanmaken van een MCP Server eruit met de reguliere server

**Python**

```python
mcp = FastMCP("Demo")

# Voeg een optellingstool toe
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

// Voeg een toevoegingshulpmiddel toe
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

Het punt is dat je expliciet elke tool, resource of prompt toevoegt die je wilt dat de server heeft. Daar is niets mis mee.

### Low-level server aanpak

Wanneer je echter de low-level server aanpak gebruikt, moet je er anders over denken. In plaats van elke tool te registreren, maak je twee handlers per functietype (tools, resources of prompts). Dus bijvoorbeeld tools hebben dan slechts twee functies zoals:

- Alle tools opsommen. Eén functie is verantwoordelijk voor alle pogingen om tools op te sommen.
- Het afhandelen van aanroepen van alle tools. Ook hier is er slechts één functie die aanroepen naar een tool afhandelt.

Dat klinkt als mogelijk minder werk toch? Dus in plaats van een tool te registreren, hoef ik alleen te zorgen dat de tool wordt vermeld wanneer ik alle tools opvraag en dat hij wordt aangeroepen wanneer er een binnenkomend verzoek is om een tool aan te roepen.

Laten we eens kijken hoe de code er nu uitziet:

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
  // Geef de lijst met geregistreerde tools terug
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

Hier hebben we nu een functie die een lijst met functies teruggeeft. Elke invoer in de lijst met tools bevat nu velden zoals `name`, `description` en `inputSchema` om te voldoen aan het gegevenstype. Dit stelt ons in staat om onze tools en functiedefinities elders te plaatsen. We kunnen nu al onze tools creëren in een tools-map en hetzelfde geldt voor alle functies, zodat je project er plotseling zo georganiseerd uit kan zien:

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

Dat is geweldig, onze architectuur kan dus best netjes worden gemaakt.

En het aanroepen van tools, is dat dan hetzelfde idee; één handler om een tool aan te roepen, welke tool dan ook? Ja, precies, hier is de code daarvoor:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is een woordenboek met toolnamen als sleutels
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
    // TODO roep het hulpmiddel aan,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Zoals je in bovenstaande code ziet, moeten we de aan te roepen tool en de bijbehorende argumenten parsen, en vervolgens moeten we doorgaan met het aanroepen van de tool.

## De aanpak verbeteren met validatie

Tot nu toe heb je gezien hoe al je registraties om tools, resources en prompts toe te voegen kunnen worden vervangen door deze twee handlers per functietype. Wat moeten we nog meer doen? Wel, we zouden een vorm van validatie moeten toevoegen om te zorgen dat de tool wordt aangeroepen met de juiste argumenten. Elke runtime heeft hiervoor zijn eigen oplossing, bijvoorbeeld Python gebruikt Pydantic en TypeScript gebruikt Zod. Het idee is dat we het volgende doen:

- Verplaats de logica voor het maken van een functie (tool, resource of prompt) naar de daarvoor bestemde map.
- Voeg een manier toe om een binnenkomend verzoek te valideren dat bijvoorbeeld vraagt om een tool aan te roepen.

### Een functie maken

Om een functie te maken, moeten we een bestand voor die functie aanmaken en zorgen dat het de verplichte velden bevat die vereist zijn voor die functie. Welke velden dat zijn, verschilt enigszins tussen tools, resources en prompts.

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
        # Valideer invoer met behulp van Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: voeg Pydantic toe, zodat we een AddInputModel kunnen maken en args kunnen valideren

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Hier zie je hoe we het volgende doen:

- Een schema maken met Pydantic `AddInputModel` met velden `a` en `b` in het bestand *schema.py*.
- Proberen het binnenkomende verzoek te parsen naar het type `AddInputModel`; als er een mismatch is in parameters, zal dit crashen:

   ```python
   # add.py
    try:
        # Valideer invoer met behulp van Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Je kunt kiezen of je deze parseerlogica in de tool-aanroep zelf zet of in de handlerfunctie.

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

- In de handler die alle tool-aanroepen afhandelt, proberen we nu het binnenkomende verzoek te parsen naar het gedefinieerde schema van de tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Als dat lukt, gaan we over tot het aanroepen van de daadwerkelijke tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Zoals je kunt zien, zorgt deze aanpak voor een fijne architectuur omdat alles zijn plek heeft, het *server.ts* bestand heel klein is en alleen de request handlers aan elkaar koppelt en elke functie zich in de respectievelijke map bevindt, zoals tools/, resources/ of /prompts.

Geweldig, laten we dit als volgende proberen te bouwen.

## Oefening: Een low-level server maken

In deze oefening gaan we het volgende doen:

1. Een low-level server maken die het opsommen van tools en het aanroepen van tools afhandelt.
1. Een architectuur implementeren waarop je kunt voortbouwen.
1. Validatie toevoegen om te zorgen dat je tool-aanroepen correct worden gevalideerd.

### -1- Een architectuur creëren

Het eerste wat we moeten doen is een architectuur opzetten die ons helpt te schalen naarmate we meer functies toevoegen, zo ziet dat eruit:

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

We hebben nu een architectuur opgezet waarmee we gemakkelijk nieuwe tools in een tools-map kunnen toevoegen. Voel je vrij om ook submappen voor resources en prompts toe te voegen.

### -2- Een tool maken

Laten we eens bekijken hoe het maken van een tool eruitziet. Eerst moet deze worden gemaakt in de submap *tool* zoals dit:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valideer invoer met behulp van Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: voeg Pydantic toe, zodat we een AddInputModel kunnen maken en args kunnen valideren

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Wat we hier zien is hoe we naam, beschrijving en input-schema definiëren met Pydantic en een handler die wordt aangeroepen wanneer deze tool wordt gebruikt. Tenslotte exposen we `tool_add`, een dictionary die al deze eigenschappen bevat.

Er is ook *schema.py* dat gebruikt wordt om het input-schema van onze tool te definiëren:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We moeten ook *__init__.py* vullen zodat de tools-map als een module wordt behandeld. Daarnaast moeten we de modules daarin beschikbaar maken zoals dit:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We kunnen dit bestand blijven uitbreiden naarmate we meer tools toevoegen.

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

Hier maken we een dictionary bestaande uit eigenschappen:

- name, dit is de naam van de tool.
- rawSchema, dit is het Zod-schema, het wordt gebruikt om binnenkomende verzoeken om deze tool aan te roepen te valideren.
- inputSchema, dit schema wordt door de handler gebruikt.
- callback, dit wordt gebruikt om de tool aan te roepen.

Er is ook `Tool` dat deze dictionary omzet in een type dat de mcp server handler kan accepteren, en dat ziet er als volgt uit:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

En er is *schema.ts* waar we de input-schema's voor elke tool opslaan, dit ziet er zo uit met nog maar één schema, maar als we tools toevoegen kunnen we er meer toevoegen:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Geweldig, laten we nu verder gaan met het afhandelen van het opsommen van onze tools.

### -3- Tools opsommen afhandelen

Om het opsommen van tools af te handelen moeten we een request handler instellen. Dit voegen we toe aan ons serverbestand:

**Python**

```python
# code weggelaten voor de beknoptheid
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

Hier voegen we de decorator `@server.list_tools` toe en implementeren we de functie `handle_list_tools`. In die functie produceren we een lijst met tools. Let op dat elke tool een naam, beschrijving en inputSchema moet hebben.

**TypeScript**

Om de request handler voor tools opsommen in te stellen, roepen we `setRequestHandler` aan op de server met een schema dat past bij wat we willen doen, in dit geval `ListToolsRequestSchema`.

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
// code weggelaten voor beknoptheid
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Geef de lijst met geregistreerde tools terug
  return {
    tools: tools
  };
});
```

Geweldig, we hebben nu het onderdeel tools opsommen opgelost, laten we nu kijken hoe we tools kunnen aanroepen.

### -4- Een tool aanroepen afhandelen

Om een tool aan te roepen, moeten we een andere request handler instellen, deze keer gericht op het afhandelen van een verzoek waarin wordt gespecificeerd welke functie aangeroepen moet worden en met welke argumenten.

**Python**

Laten we de decorator `@server.call_tool` gebruiken en dit implementeren met een functie zoals `handle_call_tool`. In die functie moeten we de toolnaam en de argumenten parsen en zorgen dat de argumenten geldig zijn voor de betreffende tool. We kunnen de argumenten validatie in deze functie doen of downstream in de daadwerkelijke tool.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is een woordenboek met toolnamen als sleutels
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # voer de tool uit
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ] 
```

Dit is wat er gebeurt:

- Onze toolnaam is al aanwezig als inputparameter `name` en de argumenten zijn in de vorm van de `arguments` dictionary.

- De tool wordt aangeroepen met `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. De validatie van de argumenten gebeurt in de `handler` eigenschap die wijst naar een functie; als dat faalt wordt er een exception gegooid.

Zo, nu hebben we een volledig begrip van het opsommen en aanroepen van tools met een low-level server.

Zie het [volledige voorbeeld](./code/README.md) hier

## Opdracht

Breid de gegeven code uit met een aantal tools, resources en prompt en reflecteer hoe je merkt dat je alleen bestanden in de tools-directory hoeft toe te voegen en nergens anders.

*Geen oplossing gegeven*

## Samenvatting

In dit hoofdstuk zagen we hoe de low-level server aanpak werkt en hoe dat ons helpt een mooie architectuur te creëren waarop we kunnen voortbouwen. We hebben ook validatie besproken en je hebt gezien hoe je met validatiebibliotheken schemas kunt maken voor inputvalidatie.

## Wat volgt

- Volgend: [Eenvoudige Authenticatie](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, kan het voorkomen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden bevatten. Het oorspronkelijke document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor belangrijke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of foutieve interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
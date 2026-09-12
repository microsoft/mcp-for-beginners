# Geavanceerd servergebruik

Er zijn twee verschillende soorten servers beschikbaar in de MCP SDK, je normale server en de laag-niveau server. Normaal gesproken gebruik je de reguliere server om er functies aan toe te voegen. In sommige gevallen wil je echter vertrouwen op de laag-niveau server, zoals:

- Betere architectuur. Het is mogelijk om een nette architectuur te maken met zowel de reguliere server als een laag-niveau server, maar het kan worden betoogd dat het iets gemakkelijker is met een laag-niveau server.
- Beschikbaarheid van functies. Sommige geavanceerde functies kunnen alleen worden gebruikt met een
    laag-niveau server. Latere hoofdstukken behandelen Elicitation en de legacy Sampling
    functie, die is afgekeurd in MCP `2026-07-28`.

## Reguliere server vs laag-niveau server

Zo ziet het maken van een MCP Server eruit met de reguliere server

**Python**

```python
mcp = FastMCP("Demo")

# Voeg een toevoegingshulpmiddel toe
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

// Voeg een optellingstool toe
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

Het punt is dat je expliciet elk hulpmiddel, bron of prompt toevoegt dat je wilt dat de server heeft. Daar is niets mis mee.  

### Laag-niveau server benadering

Echter, wanneer je de laag-niveau server benadering gebruikt, moet je er anders over denken. In plaats van elk hulpmiddel te registreren, maak je twee handlers per functietype (tools, resources of prompts). Dus bijvoorbeeld tools hebben dan maar twee functies zoals:

- Lijst van alle tools opvragen. Eén functie is verantwoordelijk voor alle pogingen om tools op te sommen.
- Aanroepen van alle tools afhandelen. Ook hier is er maar één functie die oproepen naar een tool afhandelt.

Dat klinkt als mogelijk minder werk toch? Dus in plaats van een tool te registreren, hoef ik alleen maar te zorgen dat de tool wordt weergegeven wanneer ik alle tools opsom, en dat het wordt aangeroepen wanneer er een binnenkomend verzoek is om een tool aan te roepen. 

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
  // Retourneer de lijst van geregistreerde hulpmiddelen
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

Hier hebben we nu een functie die een lijst van functies teruggeeft. Elke invoer in de lijst van tools heeft nu velden zoals `name`, `description` en `inputSchema` om te voldoen aan het retourtype. Dit stelt ons in staat om onze tools en functiedefinities elders te plaatsen. We kunnen nu al onze tools in een tools map aanmaken en hetzelfde geldt voor al je functies, zodat je project er plotseling zo georganiseerd uitziet:

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

Dat is geweldig, onze architectuur kan er behoorlijk netjes uitzien.

En het aanroepen van tools, is dat dan hetzelfde idee, één handler om een tool aan te roepen, welke tool dan ook? Ja, precies, hier is de code daarvoor:

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
    // TODO bel het hulpmiddel,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Zoals je kunt zien aan de bovenstaande code, moeten we de tool om aan te roepen ontleden, en met welke argumenten, en dan moeten we doorgaan met het aanroepen van de tool.

## Verbetering van de benadering met validatie

Tot nu toe heb je gezien hoe al je registraties om tools, resources en prompts toe te voegen kunnen worden vervangen door deze twee handlers per functietype. Wat moeten we nog meer doen? Nou, we moeten een vorm van validatie toevoegen om ervoor te zorgen dat de tool wordt aangeroepen met de juiste argumenten. Elke runtime heeft hier zijn eigen oplossing voor, bijvoorbeeld Python gebruikt Pydantic en TypeScript gebruikt Zod. Het idee is dat we het volgende doen:

- Verplaats de logica voor het maken van een functie (tool, resource of prompt) naar zijn toegewijde map.
- Voeg een manier toe om een binnenkomend verzoek te valideren dat bijvoorbeeld vraagt om een tool aan te roepen.

### Maak een functie aan

Om een functie aan te maken, moeten we een bestand voor die functie maken en ervoor zorgen dat het de verplichte velden heeft die vereist zijn voor die functie. Welke velden verschillen enigszins tussen tools, resources en prompts.

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

    # TODO: voeg Pydantic toe, zodat we een AddInputModel kunnen maken en argumenten kunnen valideren

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

- Maak een schema met Pydantic `AddInputModel` met velden `a` en `b` in bestand *schema.py*.
- Probeer het binnenkomende verzoek te ontleden als type `AddInputModel`, als er een mismatch is in parameters zal dit crashen:

   ```python
   # add.py
    try:
        # Valideer invoer met behulp van Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Je kunt kiezen of je deze ontledingslogica in de toolaanroep zelf plaatst of in de handlerfunctie.

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

- In de handler die alle tooloproepen afhandelt, proberen we het binnenkomende verzoek te ontleden tot het schema dat door de tool is gedefinieerd:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    als dat werkt dan gaan we door met het aanroepen van de daadwerkelijke tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Zoals je kunt zien, creëert deze benadering een prachtige architectuur omdat alles zijn plaats heeft, het *server.ts* is een heel klein bestand dat alleen de verzoek handlers aan elkaar knoopt en elke functie bevindt zich in hun respectievelijke map zoals tools/, resources/ of /prompts.

Geweldig, laten we dit nu proberen te bouwen. 

## Oefening: Een laag-niveau server maken

In deze oefening doen we het volgende:

1. Maak een laag-niveau server die het opsommen van tools en het aanroepen van tools afhandelt.
1. Implementeer een architectuur waarop je kunt voortbouwen.
1. Voeg validatie toe om ervoor te zorgen dat je tool aanroepen correct worden gevalideerd.

### -1- Maak een architectuur

Het eerste wat we moeten aanpakken is een architectuur die ons helpt opschalen als we meer functies toevoegen, zo ziet dat eruit:

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

Nu hebben we een architectuur opgezet die ervoor zorgt dat we gemakkelijk nieuwe tools kunnen toevoegen in een tools map. Voel je vrij om dit te volgen om submappen toe te voegen voor resources en prompts.

### -2- Een tool maken

Laten we eens kijken hoe het maken van een tool er uitziet. Eerst moet het in zijn *tool* subdirectory worden aangemaakt zoals volgt:

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

Wat we hier zien is hoe we naam, beschrijving en input schema definiëren met Pydantic en een handler die wordt aangeroepen zodra deze tool wordt aangeroepen. Ten slotte exposeren we `tool_add` wat een dictionary is die al deze eigenschappen bevat.

Er is ook *schema.py* die wordt gebruikt om het input schema te definiëren dat door onze tool wordt gebruikt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We moeten ook *__init__.py* vullen om ervoor te zorgen dat de tools directory als module wordt behandeld. Daarnaast moeten we de modules binnenin zoals volgt exposeren:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We kunnen blijven toevoegen aan dit bestand naarmate we meer tools toevoegen.

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

- name, dit is de naam van het hulpmiddel.
- rawSchema, dit is het Zod-schema, het zal worden gebruikt om inkomende verzoeken om deze tool aan te roepen te valideren.
- inputSchema, dit schema zal worden gebruikt door de handler.
- callback, dit wordt gebruikt om de tool aan te roepen.

Er is ook `Tool` die wordt gebruikt om deze dictionary om te zetten in een type dat de mcp server handler kan accepteren en het ziet er zo uit:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

En er is *schema.ts* waar we de inputschema's voor elke tool opslaan die er zo uitziet met momenteel maar één schema, maar naarmate we tools toevoegen kunnen we meer invoeren:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Geweldig, laten we verder gaan met het afhandelen van het opsommen van onze tools.

### -3- Tools opsommen afhandelen

Vervolgens moeten we een request handler opzetten om onze tools op te sommen. Hier is wat we moeten toevoegen aan ons serverbestand:

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

Hier voegen we de decorator `@server.list_tools` toe en de implementerende functie `handle_list_tools`. In deze laatste moeten we een lijst van tools produceren. Let op dat elke tool een naam, beschrijving en inputSchema moet hebben.   

**TypeScript**

Om de request handler op te zetten om tools op te sommen, moeten we `setRequestHandler` op de server aanroepen met een schema passend bij wat we proberen te doen, in dit geval `ListToolsRequestSchema`. 

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
// code weggelaten ter beknoptheid
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Geef de lijst met geregistreerde tools terug
  return {
    tools: tools
  };
});
```

Geweldig, nu we het stuk van het opsommen van tools hebben opgelost, laten we eens kijken hoe we tools kunnen aanroepen.

### -4- Een tool aanroepen afhandelen

Om een tool aan te roepen moeten we een andere request handler opzetten, deze keer gericht op het afhandelen van een verzoek dat specificeert welke functie moet worden aangeroepen en met welke argumenten.

**Python**

Laten we de decorator `@server.call_tool` gebruiken en deze implementeren met een functie als `handle_call_tool`. Binnen die functie moeten we de naam van de tool, de argumenten eruit halen en ervoor zorgen dat de argumenten geldig zijn voor de betreffende tool. We kunnen de argumenten valideren in deze functie of verderop in de daadwerkelijke tool.

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
        # roep de tool aan
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Dit gebeurt er:

- Onze toolnaam is al aanwezig als inputparameter `name` wat ook geldt voor onze argumenten in de vorm van de `arguments` dictionary.

- De tool wordt aangeroepen met `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. De validatie van de argumenten gebeurt in de `handler` property die naar een functie wijst, als dat faalt wordt er een uitzondering opgegooid. 

Zo, nu hebben we een volledig begrip van het opsommen en aanroepen van tools met een laag-niveau server.

Zie het [volledige voorbeeld](./code/README.md) hier

## Opdracht

Breid de code die je gegeven is uit met een aantal tools, resources en prompts en reflecteer op hoe je opvalt dat je alleen bestanden hoeft toe te voegen in de tools directory en nergens anders. 

*Geen oplossing gegeven*

## Samenvatting

In dit hoofdstuk hebben we gezien hoe de laag-niveau server benadering werkt en hoe dat ons kan helpen een mooie architectuur te creëren waarop we kunnen blijven bouwen. We hebben ook validatie besproken en je is getoond hoe je kunt werken met validatiebibliotheken om schema's te maken voor inputvalidatie.

## Wat Nu

- Volgende: [Eenvoudige authenticatie](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
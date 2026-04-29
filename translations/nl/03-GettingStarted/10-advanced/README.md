# Geavanceerd servergebruik

Er zijn twee verschillende soorten servers beschikbaar in de MCP SDK, je normale server en de laag-niveau server. Normaal gebruik je de reguliere server om er functies aan toe te voegen. Voor sommige gevallen wil je echter vertrouwen op de laag-niveau server, zoals:

- Betere architectuur. Het is mogelijk om een schone architectuur te creëren met zowel de reguliere server als een laag-niveau server, maar het valt te betogen dat het iets eenvoudiger is met een laag-niveau server.
- Beschikbaarheid van functies. Sommige geavanceerde functies kunnen alleen worden gebruikt met een laag-niveau server. Je zult dit in latere hoofdstukken zien wanneer we sampling en elicitation toevoegen.

## Reguliere server vs laag-niveau server

Zo ziet het creëren van een MCP Server eruit met de reguliere server

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

### Laag-niveau server benadering

Echter, als je de laag-niveau server benadering gebruikt, moet je er anders over denken. In plaats van elke tool te registreren, maak je twee handlers per functie-type (tools, resources of prompts). Bijvoorbeeld tools hebben dan slechts twee functies zoals:

- Alle tools op een lijst zetten. Eén functie is verantwoordelijk voor alle pogingen om tools te tonen.
- Oproepen van alle tools afhandelen. Hier is er ook maar één functie die oproepen naar een tool afhandelt.

Dat klinkt als mogelijk minder werk toch? Dus in plaats van een tool te registreren, hoef ik alleen ervoor te zorgen dat de tool wordt weergegeven als ik alle tools opvraag en dat die wordt aangeroepen bij een binnenkomend verzoek om een tool aan te roepen.

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
  // Retourneer de lijst van geregistreerde gereedschappen
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

Hier hebben we nu een functie die een lijst met functies teruggeeft. Elk item in de toolslijst heeft nu velden als `name`, `description` en `inputSchema` om te voldoen aan het return-type. Dit stelt ons in staat onze tools en functie-definities elders te plaatsen. We kunnen nu al onze tools maken in een tools map en hetzelfde geldt voor alle functies, zodat je project er ineens zo uit kan zien:

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

Dat is geweldig, onze architectuur kan er best schoon uitzien.

Wat betreft het aanroepen van tools, is het dan hetzelfde idee, één handler om een tool aan te roepen, welke tool dan ook? Ja, precies, hier is de code daarvoor:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools is een woordenboek met gereedschapsnamen als sleutels
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

Zoals je kunt zien aan bovenstaande code, moeten we de op te roepen tool en de argumenten uitlezen, en dan moeten we overgaan tot het aanroepen van de tool.

## Verbetering van de benadering met validatie

Tot nu toe heb je gezien hoe je alle registraties om tools, resources en prompts toe te voegen kunt vervangen door deze twee handlers per functie-type. Wat moeten we nog meer doen? Nou, we moeten wat validatie toevoegen om ervoor te zorgen dat de tool wordt aangeroepen met de juiste argumenten. Elke runtime heeft haar eigen oplossing hiervoor, bijvoorbeeld Python gebruikt Pydantic en TypeScript gebruikt Zod. Het idee is dat we het volgende doen:

- Verplaats de logica voor het maken van een functie (tool, resource of prompt) naar de daarvoor bestemde map.
- Voeg een manier toe om een binnenkomend verzoek te valideren dat bijvoorbeeld vraagt om een tool aan te roepen.

### Maak een functie aan

Om een functie te maken, moeten we een bestand aanmaken voor die functie en ervoor zorgen dat het de verplichte velden bevat die nodig zijn voor die functie. Welke velden dat zijn verschilt een beetje tussen tools, resources en prompts.

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

- Een schema creëren met Pydantic `AddInputModel` met velden `a` en `b` in het bestand *schema.py*.
- Proberen de binnenkomende aanvraag te parsen naar het type `AddInputModel`, als er een mismatch is in parameters zal dit crashen:

   ```python
   # add.py
    try:
        # Valideer invoer met behulp van het Pydantic-model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Je kunt kiezen of je deze parse-logica in de tool-aanroep zelf plaatst of in de handler-functie.

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

- In de handler die alle tool-aanroepen afhandelt, proberen we nu de binnenkomende aanvraag te parsen naar het opgegeven schema van de tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    als dat lukt, gaan we over tot het aanroepen van de daadwerkelijke tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Zoals je ziet creëert deze benadering een geweldige architectuur omdat alles zijn plek heeft, de *server.ts* is een heel klein bestand dat alleen de request handlers aan elkaar knoopt en elke functie staat in zijn eigen map, dus tools/, resources/ of /prompts.

Geweldig, laten we dit nu proberen te bouwen.

## Oefening: Het maken van een laag-niveau server

In deze oefening gaan we het volgende doen:

1. Maak een laag-niveau server die het tonen van tools en het aanroepen van tools afhandelt.
1. Implementeer een architectuur waarop je verder kunt bouwen.
1. Voeg validatie toe om ervoor te zorgen dat je tool-aanroepen goed worden gevalideerd.

### -1- Maak een architectuur

Het eerste wat we moeten aanpakken is een architectuur die ons helpt schalen naarmate we meer functies toevoegen, zo ziet dat eruit:

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

### -2- Maak een tool aan

Laten we eens zien hoe het maken van een tool eruitziet. Eerst moet deze worden aangemaakt in zijn *tool* submap zoals hier:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Valideer invoer met behulp van het Pydantic-model
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

Wat we hier zien is hoe we naam, beschrijving en input-schema definiëren met Pydantic en een handler die wordt aangeroepen zodra deze tool wordt aangeroepen. Tot slot exposen we `tool_add`, wat een dictionary is die al deze eigenschappen bevat.

Daarnaast is er *schema.py* dat wordt gebruikt om het inputschema te definiëren dat onze tool gebruikt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We moeten ook *__init__.py* vullen om ervoor te zorgen dat de tools directory als een module wordt gezien. Bovendien moeten we de modules daarin ook exposen zoals hier:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We kunnen dit bestand blijven aanvullen naarmate we meer tools toevoegen.

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

Hier maken we een dictionary aan bestaande uit eigenschappen:

- name, dit is de naam van de tool.
- rawSchema, dit is het Zod schema, het wordt gebruikt om binnenkomende verzoeken die deze tool willen aanroepen te valideren.
- inputSchema, dit schema wordt door de handler gebruikt.
- callback, dit wordt gebruikt om de tool aan te roepen.

Er is ook `Tool` dat wordt gebruikt om deze dictionary om te zetten in een type dat de MCP server handler kan accepteren en het ziet er zo uit:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

En er is *schema.ts* waar we de inputschema's opslaan voor elke tool die er zo uitzien met voorlopig maar één schema, maar naarmate we meer tools toevoegen kunnen we meer invoeren:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Geweldig, laten we nu doorgaan met het afhandelen van het tonen van onze tools.

### -3- Afhandelen van tool lijst

Om de lijst van tools af te handelen, moeten we een request handler opzetten. Dit is wat we aan ons serverbestand moeten toevoegen:

**Python**

```python
# code weggelaten ter beknoptheid
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

Hier voegen we de decorator `@server.list_tools` toe en de bijbehorende functie `handle_list_tools`. In die functie moeten we een lijst met tools produceren. Let erop dat elke tool een naam, beschrijving en inputSchema moet hebben.

**TypeScript**

Om de request handler voor het tonen van tools op te zetten, moeten we `setRequestHandler` aanroepen op de server met een schema passend bij wat we willen doen, in dit geval `ListToolsRequestSchema`.

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

Geweldig, nu hebben we het stukje over tools tonen opgelost, laten we kijken hoe we tools kunnen aanroepen.

### -4- Afhandelen van het aanroepen van een tool

Om een tool aan te roepen, moeten we nog een request handler opzetten, deze keer gericht op een verzoek dat specificeert welke functie we willen aanroepen en met welke argumenten.

**Python**

Laten we de decorator `@server.call_tool` gebruiken en deze implementeren met een functie zoals `handle_call_tool`. In die functie moeten we de naam van de tool, zijn argumenten eruit halen en ervoor zorgen dat de argumenten geldig zijn voor de betreffende tool. We kunnen de validatie van argumenten in deze functie doen of later in de daadwerkelijke tool.

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

- Onze toolnaam is al aanwezig als de invoerparameter `name` die ook geldt voor onze argumenten in de vorm van de dictionary `arguments`.

- De tool wordt aangeroepen met `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. De validatie van de argumenten gebeurt in de `handler` eigenschap die verwijst naar een functie, als dat mislukt wordt er een uitzondering opgeworpen.

Daar heb je het, nu hebben we een volledig begrip van het tonen en aanroepen van tools via een laag-niveau server.

Zie het [volledige voorbeeld](./code/README.md) hier

## Opdracht

Breid de code die je hebt gekregen uit met een aantal tools, resources en prompts en merk op dat je alleen bestanden in de tools directory hoeft toe te voegen en nergens anders.

*Geen oplossing gegeven*

## Samenvatting

In dit hoofdstuk hebben we gezien hoe de laag-niveau server-benadering werkt en hoe dat ons kan helpen een mooie architectuur te creëren waarop we kunnen voortbouwen. We hebben ook validatie besproken en je hebt gezien hoe je met validatiebibliotheken kunt werken om schema's te maken voor invoervalidatie.

## Wat is het volgende

- Volgende: [Eenvoudige authenticatie](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
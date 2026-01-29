# Geavanceerd servergebruik

Er zijn twee verschillende soorten servers beschikbaar in de MCP SDK: je normale server en de low-level server. Normaal gesproken gebruik je de reguliere server om functies toe te voegen. In sommige gevallen wil je echter vertrouwen op de low-level server, bijvoorbeeld:

- Betere architectuur. Het is mogelijk om een schone architectuur te creëren met zowel de reguliere server als een low-level server, maar het kan worden gesteld dat dit iets eenvoudiger is met een low-level server.
- Beschikbaarheid van functies. Sommige geavanceerde functies kunnen alleen worden gebruikt met een low-level server. Dit zul je later in de hoofdstukken zien wanneer we sampling en elicitation toevoegen.

## Reguliere server vs low-level server

Hier is hoe het maken van een MCP Server eruitziet met de reguliere server:

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

Het punt is dat je expliciet elke tool, resource of prompt toevoegt die je wilt dat de server heeft. Daar is niets mis mee.  

### Low-level server aanpak

Wanneer je echter de low-level server aanpak gebruikt, moet je anders denken. In plaats van elke tool te registreren, maak je twee handlers per functietype (tools, resources of prompts). Dus bijvoorbeeld voor tools heb je slechts twee functies zoals:

- Alle tools opsommen. Eén functie is verantwoordelijk voor alle pogingen om tools op te sommen.
- Het afhandelen van het aanroepen van alle tools. Ook hier is er slechts één functie die oproepen naar een tool afhandelt.

Dat klinkt als mogelijk minder werk, toch? Dus in plaats van een tool te registreren, hoef ik alleen maar ervoor te zorgen dat de tool wordt vermeld wanneer ik alle tools opsom en dat deze wordt aangeroepen wanneer er een inkomend verzoek is om een tool aan te roepen.

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

Hier hebben we nu een functie die een lijst met functies retourneert. Elk item in de tools-lijst heeft nu velden zoals `name`, `description` en `inputSchema` om te voldoen aan het retourtype. Dit stelt ons in staat om onze tools en functiedefinitie elders te plaatsen. We kunnen nu al onze tools in een tools-map maken, en hetzelfde geldt voor al je functies, zodat je project er ineens georganiseerd uitziet zoals:

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

Dat is geweldig, onze architectuur kan er behoorlijk schoon uitzien.

Hoe zit het met het aanroepen van tools? Is het dan hetzelfde idee, één handler om een tool aan te roepen, welke tool dan ook? Ja, precies, hier is de code daarvoor:

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

Zoals je kunt zien in de bovenstaande code, moeten we de tool die moet worden aangeroepen en met welke argumenten uit elkaar halen, en vervolgens moeten we doorgaan met het aanroepen van de tool.

## De aanpak verbeteren met validatie

Tot nu toe heb je gezien hoe al je registraties om tools, resources en prompts toe te voegen kunnen worden vervangen door deze twee handlers per functietype. Wat moeten we verder doen? Wel, we zouden een vorm van validatie moeten toevoegen om ervoor te zorgen dat de tool wordt aangeroepen met de juiste argumenten. Elke runtime heeft zijn eigen oplossing hiervoor, bijvoorbeeld Python gebruikt Pydantic en TypeScript gebruikt Zod. Het idee is dat we het volgende doen:

- Verplaats de logica voor het maken van een functie (tool, resource of prompt) naar de daarvoor bestemde map.
- Voeg een manier toe om een inkomend verzoek te valideren dat bijvoorbeeld vraagt om een tool aan te roepen.

### Een functie maken

Om een functie te maken, moeten we een bestand voor die functie maken en ervoor zorgen dat het de verplichte velden bevat die vereist zijn voor die functie. Welke velden verschillen enigszins tussen tools, resources en prompts.

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

Hier zie je hoe we het volgende doen:

- Maak een schema met behulp van Pydantic `AddInputModel` met velden `a` en `b` in het bestand *schema.py*.
- Probeer het inkomende verzoek te parseren naar het type `AddInputModel`. Als er een mismatch is in parameters, zal dit crashen:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Je kunt ervoor kiezen om deze parseringslogica in de tool zelf te plaatsen of in de handlerfunctie.

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

- In de handler die alle tool-oproepen afhandelt, proberen we nu het inkomende verzoek te parseren naar het gedefinieerde schema van de tool:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Als dat werkt, gaan we verder met het aanroepen van de daadwerkelijke tool:

    ```typescript
    const result = await tool.callback(input);
    ```

Zoals je kunt zien, creëert deze aanpak een geweldige architectuur, omdat alles zijn plaats heeft. Het *server.ts*-bestand is een zeer klein bestand dat alleen de request handlers koppelt, en elke functie bevindt zich in de respectieve map, zoals tools/, resources/ of /prompts.

Geweldig, laten we proberen dit nu te bouwen.

## Oefening: Een low-level server maken

In deze oefening gaan we het volgende doen:

1. Een low-level server maken die het opsommen van tools en het aanroepen van tools afhandelt.
1. Een architectuur implementeren waarop je kunt voortbouwen.
1. Validatie toevoegen om ervoor te zorgen dat je tool-oproepen correct worden gevalideerd.

### -1- Een architectuur maken

Het eerste dat we moeten aanpakken, is een architectuur die ons helpt schalen terwijl we meer functies toevoegen. Hier is hoe het eruitziet:

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

Nu hebben we een architectuur opgezet die ervoor zorgt dat we gemakkelijk nieuwe tools kunnen toevoegen in een tools-map. Voel je vrij om dit te volgen en submappen toe te voegen voor resources en prompts.

### -2- Een tool maken

Laten we eens kijken hoe het maken van een tool eruitziet. Eerst moet deze worden gemaakt in de *tool*-submap zoals:

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

Wat we hier zien, is hoe we de naam, beschrijving, een inputschema met behulp van Pydantic definiëren en een handler die wordt aangeroepen zodra deze tool wordt aangeroepen. Ten slotte stellen we `tool_add` beschikbaar, wat een dictionary is die al deze eigenschappen bevat.

Er is ook *schema.py* dat wordt gebruikt om het inputschema te definiëren dat door onze tool wordt gebruikt:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

We moeten ook *__init__.py* vullen om ervoor te zorgen dat de tools-map wordt behandeld als een module. Bovendien moeten we de modules binnenin beschikbaar maken zoals:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

We kunnen dit bestand blijven aanvullen terwijl we meer tools toevoegen.

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
- rawSchema, dit is het Zod-schema, dat zal worden gebruikt om inkomende verzoeken te valideren om deze tool aan te roepen.
- inputSchema, dit schema zal worden gebruikt door de handler.
- callback, dit wordt gebruikt om de tool aan te roepen.

Er is ook `Tool` dat wordt gebruikt om deze dictionary om te zetten in een type dat de MCP server handler kan accepteren, en het ziet er zo uit:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

En er is *schema.ts* waar we de inputschemas voor elke tool opslaan. Het ziet er zo uit met slechts één schema op dit moment, maar naarmate we tools toevoegen, kunnen we meer items toevoegen:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Geweldig, laten we doorgaan met het afhandelen van het opsommen van onze tools.

### -3- Tools opsommen

Om het opsommen van tools af te handelen, moeten we een request handler hiervoor instellen. Hier is wat we moeten toevoegen aan ons serverbestand:

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

Hier voegen we de decorator `@server.list_tools` toe en de implementatiefunctie `handle_list_tools`. In de laatste moeten we een lijst met tools produceren. Merk op dat elke tool een naam, beschrijving en inputSchema moet hebben.   

**TypeScript**

Om de request handler in te stellen voor het opsommen van tools, moeten we `setRequestHandler` aanroepen op de server met een schema dat past bij wat we proberen te doen, in dit geval `ListToolsRequestSchema`. 

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

Geweldig, nu hebben we het stuk van het opsommen van tools opgelost. Laten we eens kijken hoe we tools kunnen aanroepen.

### -4- Een tool aanroepen

Om een tool aan te roepen, moeten we een andere request handler instellen, deze keer gericht op het afhandelen van een verzoek dat specificeert welke functie moet worden aangeroepen en met welke argumenten.

**Python**

Laten we de decorator `@server.call_tool` gebruiken en deze implementeren met een functie zoals `handle_call_tool`. Binnen die functie moeten we de toolnaam, de argumenten en ervoor zorgen dat de argumenten geldig zijn voor de betreffende tool. We kunnen de argumenten valideren in deze functie of downstream in de daadwerkelijke tool.

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

Hier is wat er gebeurt:

- Onze toolnaam is al aanwezig als de inputparameter `name`, wat ook geldt voor onze argumenten in de vorm van de `arguments` dictionary.

- De tool wordt aangeroepen met `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. De validatie van de argumenten gebeurt in de `handler`-eigenschap die naar een functie wijst. Als dat faalt, zal het een uitzondering veroorzaken. 

Daarmee hebben we nu een volledig begrip van het opsommen en aanroepen van tools met behulp van een low-level server.

Zie het [volledige voorbeeld](./code/README.md) hier.

## Opdracht

Breid de code die je hebt gekregen uit met een aantal tools, resources en prompts en reflecteer op hoe je merkt dat je alleen bestanden hoeft toe te voegen in de tools-map en nergens anders. 

*Geen oplossing gegeven*

## Samenvatting

In dit hoofdstuk hebben we gezien hoe de low-level server aanpak werkt en hoe dat ons kan helpen een mooie architectuur te creëren waarop we kunnen blijven bouwen. We hebben ook validatie besproken en je hebt gezien hoe je met validatiebibliotheken kunt werken om schemas te maken voor inputvalidatie.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
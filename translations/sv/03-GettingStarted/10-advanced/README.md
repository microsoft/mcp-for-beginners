# Avancerad serveranvändning

Det finns två olika typer av servrar som exponeras i MCP SDK: din vanliga server och låg-nivå servern. Normalt sett använder du den vanliga servern för att lägga till funktioner. I vissa fall kan det dock vara bättre att använda låg-nivå servern, exempelvis:

- Bättre arkitektur. Det är möjligt att skapa en ren arkitektur med både den vanliga servern och låg-nivå servern, men det kan argumenteras att det är något enklare med låg-nivå servern.
- Funktionstillgänglighet. Vissa avancerade funktioner kan endast användas med låg-nivå servern. Du kommer att se detta i senare kapitel när vi lägger till sampling och elicitering.

## Vanlig server vs låg-nivå server

Så här ser skapandet av en MCP-server ut med den vanliga servern:

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

Poängen är att du explicit lägger till varje verktyg, resurs eller prompt som du vill att servern ska ha. Det är inget fel med det.  

### Låg-nivå servermetod

När du använder låg-nivå servermetoden behöver du tänka annorlunda, nämligen att istället för att registrera varje verktyg skapar du två hanterare per funktionstyp (verktyg, resurser eller prompts). Så för exempelvis verktyg har du bara två funktioner som ser ut så här:

- Lista alla verktyg. En funktion ansvarar för alla försök att lista verktyg.
- Hantera anrop till alla verktyg. Här finns också bara en funktion som hanterar anrop till ett verktyg.

Det låter som potentiellt mindre arbete, eller hur? Istället för att registrera ett verktyg behöver jag bara se till att verktyget listas när jag listar alla verktyg och att det anropas när det finns en inkommande begäran att anropa ett verktyg.

Låt oss titta på hur koden ser ut nu:

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

Här har vi nu en funktion som returnerar en lista med funktioner. Varje post i verktygslistan har nu fält som `name`, `description` och `inputSchema` för att följa returtypen. Detta gör det möjligt att placera våra verktyg och funktionsdefinitioner någon annanstans. Vi kan nu skapa alla våra verktyg i en verktygsmapp och samma sak gäller för alla dina funktioner, så ditt projekt kan plötsligt organiseras så här:

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

Det är fantastiskt, vår arkitektur kan göras ganska ren.

Hur är det med att anropa verktyg, är det samma idé då, en hanterare för att anropa ett verktyg, vilket som helst? Ja, precis, här är koden för det:

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

Som du kan se från koden ovan behöver vi analysera vilket verktyg som ska anropas och med vilka argument, och sedan fortsätta med att anropa verktyget.

## Förbättra metoden med validering

Hittills har du sett hur alla dina registreringar för att lägga till verktyg, resurser och prompts kan ersättas med dessa två hanterare per funktionstyp. Vad mer behöver vi göra? Jo, vi bör lägga till någon form av validering för att säkerställa att verktyget anropas med rätt argument. Varje runtime har sin egen lösning för detta, till exempel använder Python Pydantic och TypeScript använder Zod. Idén är att vi gör följande:

- Flytta logiken för att skapa en funktion (verktyg, resurs eller prompt) till dess dedikerade mapp.
- Lägg till ett sätt att validera en inkommande begäran som exempelvis ber om att anropa ett verktyg.

### Skapa en funktion

För att skapa en funktion behöver vi skapa en fil för den funktionen och se till att den har de obligatoriska fälten som krävs för den funktionen. Vilka fält som krävs skiljer sig något mellan verktyg, resurser och prompts.

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

Här kan du se hur vi gör följande:

- Skapar ett schema med Pydantic `AddInputModel` med fälten `a` och `b` i filen *schema.py*.
- Försöker analysera den inkommande begäran till att vara av typen `AddInputModel`. Om det finns en mismatch i parametrar kommer detta att krascha:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan välja om du vill placera denna analyslogik i själva verktygsanropet eller i hanterarfunktionen.

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

- I hanteraren som hanterar alla verktygsanrop försöker vi nu analysera den inkommande begäran till verktygets definierade schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Om det fungerar fortsätter vi med att anropa det faktiska verktyget:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se skapar denna metod en fantastisk arkitektur där allt har sin plats. *server.ts* är en mycket liten fil som bara kopplar ihop begäranhanterare, och varje funktion finns i sina respektive mappar, dvs tools/, resources/ eller /prompts.

Bra, låt oss försöka bygga detta nästa gång.

## Övning: Skapa en låg-nivå server

I denna övning kommer vi att göra följande:

1. Skapa en låg-nivå server som hanterar listning av verktyg och anrop av verktyg.
1. Implementera en arkitektur som du kan bygga vidare på.
1. Lägg till validering för att säkerställa att dina verktygsanrop valideras korrekt.

### -1- Skapa en arkitektur

Det första vi behöver adressera är en arkitektur som hjälper oss att skala när vi lägger till fler funktioner. Så här ser det ut:

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

Nu har vi satt upp en arkitektur som säkerställer att vi enkelt kan lägga till nya verktyg i en verktygsmapp. Du kan följa detta för att lägga till undermappar för resurser och prompts.

### -2- Skapa ett verktyg

Låt oss se hur det ser ut att skapa ett verktyg. Först måste det skapas i sin *tool*-undermapp så här:

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

Här ser vi hur vi definierar namn, beskrivning, ett inmatningsschema med Pydantic och en hanterare som kommer att anropas när detta verktyg används. Slutligen exponerar vi `tool_add`, som är en ordbok som innehåller alla dessa egenskaper.

Det finns också *schema.py* som används för att definiera inmatningsschemat som används av vårt verktyg:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi behöver också fylla i *__init__.py* för att säkerställa att verktygsmappen behandlas som en modul. Dessutom behöver vi exponera modulerna inom den så här:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Vi kan fortsätta att lägga till i denna fil när vi lägger till fler verktyg.

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

Här skapar vi en ordbok som består av egenskaper:

- name, detta är namnet på verktyget.
- rawSchema, detta är Zod-schemat, det kommer att användas för att validera inkommande begäranden att anropa detta verktyg.
- inputSchema, detta schema kommer att användas av hanteraren.
- callback, detta används för att anropa verktyget.

Det finns också `Tool` som används för att konvertera denna ordbok till en typ som MCP-serverhanteraren kan acceptera, och det ser ut så här:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Och det finns *schema.ts* där vi lagrar inmatningsscheman för varje verktyg, som ser ut så här med endast ett schema för närvarande, men när vi lägger till verktyg kan vi lägga till fler poster:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bra, låt oss gå vidare till att hantera listning av våra verktyg nästa gång.

### -3- Hantera verktygslistning

För att hantera listning av verktyg behöver vi ställa in en begäranhanterare för det. Här är vad vi behöver lägga till i vår serverfil:

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

Här lägger vi till dekorationen `@server.list_tools` och den implementerande funktionen `handle_list_tools`. I den senare behöver vi producera en lista med verktyg. Observera hur varje verktyg behöver ha ett namn, en beskrivning och ett inputSchema.   

**TypeScript**

För att ställa in begäranhanteraren för att lista verktyg behöver vi anropa `setRequestHandler` på servern med ett schema som passar det vi försöker göra, i detta fall `ListToolsRequestSchema`. 

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

Bra, nu har vi löst biten med att lista verktyg, låt oss titta på hur vi kan anropa verktyg nästa gång.

### -4- Hantera anrop av ett verktyg

För att anropa ett verktyg behöver vi ställa in en annan begäranhanterare, denna gång fokuserad på att hantera en begäran som specificerar vilken funktion som ska anropas och med vilka argument.

**Python**

Låt oss använda dekorationen `@server.call_tool` och implementera den med en funktion som `handle_call_tool`. Inom den funktionen behöver vi analysera verktygsnamnet, dess argument och säkerställa att argumenten är giltiga för det aktuella verktyget. Vi kan antingen validera argumenten i denna funktion eller längre ner i det faktiska verktyget.

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

Här är vad som händer:

- Vårt verktygsnamn finns redan som inmatningsparameter `name`, vilket också gäller för våra argument i form av ordboken `arguments`.

- Verktyget anropas med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen av argumenten sker i egenskapen `handler`, som pekar på en funktion. Om det misslyckas kommer det att generera ett undantag. 

Där, nu har vi en full förståelse för att lista och anropa verktyg med en låg-nivå server.

Se [hela exemplet](./code/README.md) här.

## Uppgift

Utöka koden du har fått med ett antal verktyg, resurser och prompts och reflektera över hur du märker att du bara behöver lägga till filer i verktygsmappen och ingen annanstans. 

*Ingen lösning ges*

## Sammanfattning

I detta kapitel såg vi hur låg-nivå servermetoden fungerar och hur den kan hjälpa oss att skapa en trevlig arkitektur som vi kan fortsätta bygga på. Vi diskuterade också validering och du fick se hur man arbetar med valideringsbibliotek för att skapa scheman för inmatningsvalidering.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
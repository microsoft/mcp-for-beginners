# Avancerad serveranvändning

Det finns två olika typer av servrar exponerade i MCP SDK, din vanliga server och den låg-nivå servern. Normalt använder du den vanliga servern för att lägga till funktioner. I vissa fall vill du dock förlita dig på låg-nivå servern, till exempel:

- Bättre arkitektur. Det är möjligt att skapa en ren arkitektur med både den vanliga servern och en låg-nivå server, men det kan hävdas att det är lite enklare med en låg-nivå server.
- Funktionstillgänglighet. Vissa avancerade funktioner kan endast användas med en låg-nivå server. Detta kommer du att se i senare kapitel när vi lägger till sampling och elicitation.

## Vanlig server vs låg-nivå server

Så här ser skapandet av en MCP Server ut med den vanliga servern

**Python**

```python
mcp = FastMCP("Demo")

# Lägg till ett tilläggsverktyg
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

// Lägg till ett additionsverktyg
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

Poängen är att du explicit lägger till varje verktyg, resurs eller prompt som du vill att servern ska ha. Inget fel med det.  

### Låg-nivå servermetodik

Men när du använder låg-nivå servermetodiken måste du tänka annorlunda. Istället för att registrera varje verktyg skapar du istället två hanterare per funktionstyp (verktyg, resurser eller prompts). Så till exempel har verktyg då bara två funktioner som följer:

- Lista alla verktyg. En funktion ansvarar för alla försök att lista verktyg.
- Hantera anrop till alla verktyg. Även här finns bara en funktion som hanterar anrop till ett verktyg.

Det låter som potentiellt mindre arbete va? Så istället för att registrera ett verktyg behöver jag bara se till att verktyget listas när jag listar alla verktyg och att det anropas när det finns en inkommande förfrågan för att anropa ett verktyg. 

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
  // Returnera listan över registrerade verktyg
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

Här har vi nu en funktion som returnerar en lista av funktioner. Varje post i verktygslistan har nu fält som `name`, `description` och `inputSchema` för att följa returtypen. Detta möjliggör att vi kan lägga våra verktyg och funktionsdefinition någon annanstans. Vi kan nu skapa alla våra verktyg i en tools-mapp och samma gäller för alla dina funktioner så ditt projekt plötsligt kan organiseras så här:

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

Det är toppen, vår arkitektur kan göras ganska ren.

Hur är det med anrop till verktyg, är det samma idé då, en hanterare för att anropa ett verktyg, vilket verktyg som helst? Ja, precis, här är koden för det:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools är en ordbok med verktygsnamn som nycklar
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
    // TODO anropa verktyget,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Som du kan se i koden ovan behöver vi plocka ut vilket verktyg som anropas och med vilka argument, sedan behöver vi fortsätta med att anropa verktyget.

## Förbättra metodiken med validering

Hittills har du sett hur alla dina registreringar för att lägga till verktyg, resurser och prompts kan ersättas med dessa två hanterare per funktionstyp. Vad mer behöver vi göra? Jo, vi borde lägga till någon form av validering för att säkerställa att verktyget anropas med rätt argument. Varje runtime har sin egen lösning för detta, till exempel använder Python Pydantic och TypeScript använder Zod. Idén är att vi gör följande:

- Flytta logiken för att skapa en funktion (verktyg, resurs eller prompt) till dess dedikerade mapp.
- Lägg till ett sätt att validera en inkommande förfrågan som till exempel ber om att anropa ett verktyg.

### Skapa en funktion

För att skapa en funktion behöver vi skapa en fil för den funktionen och se till att den har de obligatoriska fälten som krävs för den funktionen. Vilka fält som behövs skiljer sig lite mellan verktyg, resurser och prompts.

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
        # Validera indata med hjälp av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lägg till Pydantic, så att vi kan skapa en AddInputModel och validera argumenten

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

här kan du se hur vi gör följande:

- Skapar ett schema med Pydantic `AddInputModel` med fälten `a` och `b` i filen *schema.py*.
- Försöker tolka den inkommande förfrågan som typen `AddInputModel`, om det finns en mismatch i parametrar kraschar detta:

   ```python
   # add.py
    try:
        # Validera indata med Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kan välja om du vill lägga denna tolkningslogik i själva verktygsanropet eller i hanteringsfunktionen.

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

- I hanteraren som hanterar alla verktygsanrop, försöker vi nu tolka den inkommande förfrågan till verktygets definierade schema:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    om det fungerar fortsätter vi med att anropa det faktiska verktyget:

    ```typescript
    const result = await tool.callback(input);
    ```

Som du kan se skapar denna metodik en bra arkitektur där allt har sin plats, *server.ts* är en mycket liten fil som bara kopplar ihop förfrågningshanterarna och varje funktion finns i sin respektive mapp, dvs tools/, resources/ eller /prompts.

Toppen, låt oss försöka bygga detta nu. 

## Övning: Skapa en låg-nivå server

I denna övning ska vi göra följande:

1. Skapa en låg-nivå server som hanterar listning av verktyg och anrop av verktyg.
1. Implementera en arkitektur som du kan bygga vidare på.
1. Lägg till validering för att säkerställa att dina verktygsanrop valideras korrekt.

### -1- Skapa en arkitektur

Det första vi behöver ta tag i är en arkitektur som hjälper oss att skala när vi lägger till fler funktioner. Så här ser den ut:

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

Nu har vi satt upp en arkitektur som säkerställer att vi enkelt kan lägga till nya verktyg i en tools-mapp. Känn dig fri att följa detta för att lägga till undermappar för resurser och prompts.

### -2- Skapa ett verktyg

Låt oss se hur det ser ut att skapa ett verktyg. Först måste det skapas i sin *tool*-undermapp så här:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Validera indata med hjälp av Pydantic-modell
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: lägg till Pydantic, så att vi kan skapa en AddInputModel och validera argumenten

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Det vi ser här är hur vi definierar namn, beskrivning och inschema med Pydantic och en hanterare som kommer att anropas när detta verktyg kallas. Slutligen exponerar vi `tool_add` som är en ordbok som innehåller alla dessa egenskaper.

Det finns också *schema.py* som används för att definiera inschemas som våra verktyg använder:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Vi behöver också fylla i *__init__.py* för att säkerställa att verktygsmappen behandlas som en modul. Dessutom behöver vi exponera modulerna i den så här:

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

Här skapar vi en ordbok bestående av egenskaper:

- name, det här är verktygets namn.
- rawSchema, detta är Zod-schemat som används för att validera inkommande anrop för att kalla detta verktyg.
- inputSchema, detta schema används av hanteraren.
- callback, används för att anropa verktyget.

Det finns också `Tool` som används för att konvertera denna ordbok till en typ som mcp-serverhanteraren kan acceptera och den ser ut så här:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Och det finns *schema.ts* där vi lagrar input-scheman för varje verktyg som ser ut så här med endast ett schema för tillfället men när vi lägger till verktyg kan vi lägga till fler poster:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Bra, låt oss gå vidare till att hantera listningen av våra verktyg.

### -3- Hantera listning av verktyg

Nästa steg för att hantera listning av våra verktyg är att sätta upp en förfrågningshanterare för det. Så här lägger vi till det i vår serverfil:

**Python**

```python
# kod utelämnad för korthet
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

Här lägger vi till dekoratorn `@server.list_tools` och den implementerande funktionen `handle_list_tools`. I den senare behöver vi producera en lista på verktyg. Notera hur varje verktyg måste ha ett namn, en beskrivning och inputSchema.   

**TypeScript**

För att sätta upp förfrågningshanteraren för att lista verktyg behöver vi anropa `setRequestHandler` på servern med ett schema som passar det vi försöker göra, i detta fall `ListToolsRequestSchema`. 

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
// kod utelämnad för korthet
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Returnera listan över registrerade verktyg
  return {
    tools: tools
  };
});
```

Toppen, nu har vi löst biten med att lista verktyg, låt oss se hur vi sedan skulle kunna anropa verktyg.

### -4- Hantera anrop till ett verktyg

För att anropa ett verktyg behöver vi sätta upp en annan förfrågningshanterare, denna gång fokuserad på att hantera en förfrågan som specificerar vilken funktion som ska anropas och med vilka argument.

**Python**

Låt oss använda dekoratorn `@server.call_tool` och implementera den med en funktion som `handle_call_tool`. Inuti den funktionen behöver vi plocka ut verktygets namn, dess argument och säkerställa att argumenten är giltiga för det aktuella verktyget. Vi kan antingen validera argumenten i denna funktion eller längre ner i det faktiska verktyget.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools är en ordbok med verktygsnamn som nycklar
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # anropa verktyget
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Så här går det till:

- Vårt verktygsnamn finns redan som inparameter `name` vilket gäller för våra argument i form av `arguments` ordboken.

- Verktyget anropas med `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)`. Valideringen av argumenten sker i egenskapen `handler` som pekar på en funktion, om det misslyckas kommer ett undantag att kastas. 

Där, nu har vi en full förståelse för att lista och anropa verktyg med en låg-nivå server.

Se [fullständigt exempel](./code/README.md) här

## Uppgift

Utöka den kod du fått med ett antal verktyg, resurser och promptar och reflektera över hur du märker att du endast behöver lägga till filer i tools-katalogen och ingen annanstans. 

*Ingen lösning ges*

## Sammanfattning

I detta kapitel såg vi hur låg-nivå servermetodiken fungerade och hur den kan hjälpa oss skapa en fin arkitektur att bygga vidare på. Vi diskuterade också validering och du visades hur du arbetar med valideringsbibliotek för att skapa scheman för inputvalidering.

## Vad som komma skall

- Nästa: [Enkel autentisering](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
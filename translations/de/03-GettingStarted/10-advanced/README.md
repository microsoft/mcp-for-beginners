# Erweiterte Servernutzung

Im MCP SDK gibt es zwei verschiedene Arten von Servern: den normalen Server und den Low-Level-Server. Normalerweise verwendet man den regulären Server, um Funktionen hinzuzufügen. In einigen Fällen ist es jedoch sinnvoll, auf den Low-Level-Server zurückzugreifen, beispielsweise:

- **Bessere Architektur**: Es ist möglich, sowohl mit dem regulären Server als auch mit dem Low-Level-Server eine saubere Architektur zu erstellen. Es lässt sich jedoch argumentieren, dass dies mit dem Low-Level-Server etwas einfacher ist.
- **Verfügbarkeit von Funktionen**: Einige erweiterte Funktionen können nur mit einem Low-Level-Server genutzt werden. Dies wird in späteren Kapiteln deutlich, wenn wir Sampling und Elicitation hinzufügen.

## Regulärer Server vs. Low-Level-Server

So sieht die Erstellung eines MCP-Servers mit dem regulären Server aus:

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

Der Punkt ist, dass man explizit jedes Tool, jede Ressource oder jeden Prompt hinzufügt, die der Server haben soll. Daran ist nichts auszusetzen.

### Ansatz des Low-Level-Servers

Wenn man jedoch den Low-Level-Server-Ansatz verwendet, muss man anders denken. Statt jedes Tool zu registrieren, erstellt man zwei Handler pro Funktionstyp (Tools, Ressourcen oder Prompts). Für Tools gibt es beispielsweise nur zwei Funktionen:

- **Auflistung aller Tools**: Eine Funktion ist für alle Versuche zuständig, Tools aufzulisten.
- **Aufruf aller Tools**: Hier gibt es ebenfalls nur eine Funktion, die den Aufruf eines Tools verarbeitet.

Das klingt nach potenziell weniger Arbeit, oder? Statt ein Tool zu registrieren, muss man lediglich sicherstellen, dass das Tool bei der Auflistung aller Tools aufgeführt wird und dass es aufgerufen wird, wenn eine Anfrage zum Aufruf eines Tools eingeht.

Schauen wir uns an, wie der Code jetzt aussieht:

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

Hier haben wir nun eine Funktion, die eine Liste von Funktionen zurückgibt. Jedes Element in der Tool-Liste hat Felder wie `name`, `description` und `inputSchema`, um dem Rückgabetyp zu entsprechen. Dadurch können wir unsere Tools und Funktionsdefinitionen an anderer Stelle platzieren. Wir können jetzt alle unsere Tools in einem Tools-Ordner erstellen, und dasselbe gilt für alle Funktionen, sodass unser Projekt plötzlich so organisiert werden kann:

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

Das ist großartig, unsere Architektur kann sehr sauber gestaltet werden.

Wie sieht es mit dem Aufruf von Tools aus? Ist es dann dieselbe Idee, ein Handler für den Aufruf eines Tools, egal welches Tool? Ja, genau, hier ist der Code dafür:

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

Wie man im obigen Code sehen kann, müssen wir das Tool, das aufgerufen werden soll, und die Argumente dafür herausfiltern und dann mit dem Aufruf des Tools fortfahren.

## Verbesserung des Ansatzes durch Validierung

Bisher haben Sie gesehen, wie alle Registrierungen zum Hinzufügen von Tools, Ressourcen und Prompts durch diese zwei Handler pro Funktionstyp ersetzt werden können. Was müssen wir noch tun? Nun, wir sollten eine Form der Validierung hinzufügen, um sicherzustellen, dass das Tool mit den richtigen Argumenten aufgerufen wird. Jede Laufzeitumgebung hat ihre eigene Lösung dafür, beispielsweise verwendet Python Pydantic und TypeScript Zod. Die Idee ist, Folgendes zu tun:

- Die Logik zur Erstellung einer Funktion (Tool, Ressource oder Prompt) in ihren dedizierten Ordner verschieben.
- Eine Möglichkeit hinzufügen, eine eingehende Anfrage zu validieren, die beispielsweise den Aufruf eines Tools anfordert.

### Erstellung einer Funktion

Um eine Funktion zu erstellen, müssen wir eine Datei für diese Funktion erstellen und sicherstellen, dass sie die obligatorischen Felder enthält, die für diese Funktion erforderlich sind. Welche Felder erforderlich sind, unterscheidet sich etwas zwischen Tools, Ressourcen und Prompts.

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

Hier sehen Sie, wie wir Folgendes tun:

- Ein Schema mit Pydantic `AddInputModel` mit den Feldern `a` und `b` in der Datei *schema.py* erstellen.
- Den Versuch unternehmen, die eingehende Anfrage in den Typ `AddInputModel` zu parsen. Wenn die Parameter nicht übereinstimmen, wird dies abstürzen:

   ```python
   # add.py
    try:
        # Validate input using Pydantic model
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Sie können wählen, ob Sie diese Parsing-Logik direkt im Tool-Aufruf oder in der Handler-Funktion platzieren möchten.

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

- Im Handler, der alle Tool-Aufrufe verarbeitet, versuchen wir nun, die eingehende Anfrage in das definierte Schema des Tools zu parsen:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Wenn das funktioniert, fahren wir mit dem eigentlichen Tool-Aufruf fort:

    ```typescript
    const result = await tool.callback(input);
    ```

Wie Sie sehen, schafft dieser Ansatz eine großartige Architektur, da alles seinen Platz hat. Die Datei *server.ts* ist sehr klein und dient nur dazu, die Request-Handler zu verbinden, und jede Funktion befindet sich in ihrem jeweiligen Ordner, z. B. tools/, resources/ oder prompts/.

Super, lassen Sie uns das als Nächstes aufbauen.

## Übung: Erstellung eines Low-Level-Servers

In dieser Übung werden wir Folgendes tun:

1. Einen Low-Level-Server erstellen, der die Auflistung von Tools und den Aufruf von Tools verarbeitet.
1. Eine Architektur implementieren, auf der Sie aufbauen können.
1. Validierung hinzufügen, um sicherzustellen, dass Ihre Tool-Aufrufe ordnungsgemäß validiert werden.

### -1- Erstellung einer Architektur

Das Erste, was wir angehen müssen, ist eine Architektur, die uns beim Skalieren hilft, wenn wir weitere Funktionen hinzufügen. So sieht sie aus:

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

Jetzt haben wir eine Architektur eingerichtet, die sicherstellt, dass wir problemlos neue Tools in einem Tools-Ordner hinzufügen können. Sie können diese Struktur gerne erweitern, um Unterverzeichnisse für Ressourcen und Prompts hinzuzufügen.

### -2- Erstellung eines Tools

Schauen wir uns als Nächstes an, wie die Erstellung eines Tools aussieht. Zunächst muss es in seinem *tool*-Unterverzeichnis erstellt werden, wie folgt:

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

Hier sehen wir, wie wir Name, Beschreibung, ein Eingabe-Schema mit Pydantic und einen Handler definieren, der aufgerufen wird, sobald dieses Tool aufgerufen wird. Schließlich stellen wir `tool_add` bereit, ein Dictionary, das all diese Eigenschaften enthält.

Es gibt auch *schema.py*, das verwendet wird, um das Eingabe-Schema zu definieren, das von unserem Tool verwendet wird:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Wir müssen auch *__init__.py* ausfüllen, um sicherzustellen, dass das Tools-Verzeichnis als Modul behandelt wird. Außerdem müssen wir die Module darin wie folgt bereitstellen:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Wir können diese Datei erweitern, wenn wir weitere Tools hinzufügen.

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

Hier erstellen wir ein Dictionary, das aus folgenden Eigenschaften besteht:

- **name**: Der Name des Tools.
- **rawSchema**: Das Zod-Schema, das verwendet wird, um eingehende Anfragen zur Nutzung dieses Tools zu validieren.
- **inputSchema**: Dieses Schema wird vom Handler verwendet.
- **callback**: Wird verwendet, um das Tool aufzurufen.

Es gibt auch `Tool`, das verwendet wird, um dieses Dictionary in einen Typ zu konvertieren, den der MCP-Server-Handler akzeptieren kann. Es sieht wie folgt aus:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Und es gibt *schema.ts*, wo wir die Eingabe-Schemas für jedes Tool speichern. Es sieht wie folgt aus, mit nur einem Schema derzeit, aber wir können weitere Einträge hinzufügen, wenn wir Tools hinzufügen:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, fahren wir mit der Verarbeitung der Auflistung unserer Tools fort.

### -3- Verarbeitung der Tool-Auflistung

Um die Auflistung unserer Tools zu verarbeiten, müssen wir einen Request-Handler dafür einrichten. Hier ist, was wir zu unserer Server-Datei hinzufügen müssen:

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

Hier fügen wir den Dekorator `@server.list_tools` und die Implementierungsfunktion `handle_list_tools` hinzu. In letzterer müssen wir eine Liste von Tools erstellen. Beachten Sie, dass jedes Tool einen Namen, eine Beschreibung und ein Eingabe-Schema haben muss.

**TypeScript**

Um den Request-Handler für die Auflistung von Tools einzurichten, müssen wir `setRequestHandler` auf dem Server mit einem Schema aufrufen, das zu dem passt, was wir tun möchten, in diesem Fall `ListToolsRequestSchema`.

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

Super, jetzt haben wir das Stück der Tool-Auflistung gelöst. Schauen wir uns als Nächstes an, wie wir Tools aufrufen könnten.

### -4- Verarbeitung des Tool-Aufrufs

Um ein Tool aufzurufen, müssen wir einen weiteren Request-Handler einrichten, der sich darauf konzentriert, eine Anfrage zu verarbeiten, die angibt, welche Funktion aufgerufen werden soll und mit welchen Argumenten.

**Python**

Verwenden wir den Dekorator `@server.call_tool` und implementieren ihn mit einer Funktion wie `handle_call_tool`. Innerhalb dieser Funktion müssen wir den Tool-Namen und seine Argumente herausfiltern und sicherstellen, dass die Argumente für das betreffende Tool gültig sind. Wir können die Argumente entweder in dieser Funktion oder weiter unten im eigentlichen Tool validieren.

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

Hier passiert Folgendes:

- Der Tool-Name ist bereits als Eingabeparameter `name` vorhanden, was auch für die Argumente in Form des `arguments`-Dictionaries gilt.

- Das Tool wird mit `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` aufgerufen. Die Validierung der Argumente erfolgt in der `handler`-Eigenschaft, die auf eine Funktion verweist. Wenn dies fehlschlägt, wird eine Ausnahme ausgelöst.

Damit haben wir nun ein vollständiges Verständnis davon, wie Tools mit einem Low-Level-Server aufgelistet und aufgerufen werden.

Siehe das [vollständige Beispiel](./code/README.md) hier.

## Aufgabe

Erweitern Sie den gegebenen Code um eine Reihe von Tools, Ressourcen und Prompts und reflektieren Sie darüber, wie Sie feststellen, dass Sie nur Dateien im Tools-Verzeichnis hinzufügen müssen und nirgendwo anders.

*Keine Lösung angegeben*

## Zusammenfassung

In diesem Kapitel haben wir gesehen, wie der Low-Level-Server-Ansatz funktioniert und wie er uns helfen kann, eine schöne Architektur zu erstellen, auf der wir weiter aufbauen können. Wir haben auch über Validierung gesprochen und Ihnen gezeigt, wie Sie mit Validierungsbibliotheken arbeiten können, um Schemas für die Eingabevalidierung zu erstellen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
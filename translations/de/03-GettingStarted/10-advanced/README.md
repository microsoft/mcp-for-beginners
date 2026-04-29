# Erweiterte Servernutzung

Im MCP SDK gibt es zwei verschiedene Arten von Servern: Ihren normalen Server und den Low-Level-Server. Normalerweise verwenden Sie den regulären Server, um Funktionen hinzuzufügen. In einigen Fällen möchten Sie jedoch auf den Low-Level-Server zurückgreifen, z. B.:

- Bessere Architektur. Es ist möglich, mit sowohl dem regulären Server als auch einem Low-Level-Server eine saubere Architektur zu erstellen, aber es kann argumentiert werden, dass es mit einem Low-Level-Server etwas einfacher ist.
- Verfügbare Funktionen. Einige erweiterte Funktionen können nur mit einem Low-Level-Server verwendet werden. Dies sehen Sie in späteren Kapiteln, wenn wir Sampling und Elicitation hinzufügen.

## Regulärer Server vs. Low-Level-Server

So sieht die Erstellung eines MCP-Servers mit dem regulären Server aus

**Python**

```python
mcp = FastMCP("Demo")

# Fügen Sie ein Additionstool hinzu
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

// Füge ein Additionstool hinzu
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

Der Punkt ist, dass Sie explizit jedes Tool, jede Ressource oder jeden Prompt hinzufügen, den der Server haben soll. Daran ist nichts auszusetzen.

### Low-Level-Server-Ansatz

Beim Low-Level-Server-Ansatz müssen Sie jedoch anders denken. Anstatt jedes Tool zu registrieren, erstellen Sie stattdessen zwei Handler pro Funktionstyp (Tools, Ressourcen oder Prompts). Zum Beispiel haben Tools dann nur zwei Funktionen wie folgt:

- Auflisten aller Tools. Eine Funktion wäre für alle Versuche zuständig, Tools aufzulisten.
- Alle Tool-Aufrufe behandeln. Auch hier gibt es nur eine Funktion, die Aufrufe an ein Tool handhabt.

Das klingt nach potenziell weniger Arbeit, oder? Anstatt ein Tool zu registrieren, müssen Sie nur sicherstellen, dass das Tool aufgelistet wird, wenn Sie alle Tools auflisten, und dass es aufgerufen wird, wenn eine eingehende Anfrage vorliegt, ein Tool aufzurufen.

Sehen wir uns an, wie der Code jetzt aussieht:

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
  // Gibt die Liste der registrierten Werkzeuge zurück
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

Hier haben wir jetzt eine Funktion, die eine Liste von Funktionen zurückgibt. Jeder Eintrag in der Tools-Liste hat jetzt Felder wie `name`, `description` und `inputSchema`, um dem Rückgabetyp zu entsprechen. Das ermöglicht es uns, unsere Tools und Funktionsdefinitionen woanders zu platzieren. Wir können jetzt alle Tools in einem Tools-Ordner erstellen, und das Gleiche gilt für alle Ihre Funktionen, sodass Ihr Projekt plötzlich wie folgt organisiert sein kann:

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

Das ist großartig, unsere Architektur kann dadurch sehr sauber gestaltet werden.

Und wie sieht es mit dem Aufrufen von Tools aus? Ist das dann dieselbe Idee, ein Handler zum Aufrufen eines Tools, egal welches? Ja, genau, hier ist der Code dafür:

**Python**

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ist ein Wörterbuch mit Werkzeugnamen als Schlüsseln
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
    // TODO rufe das Werkzeug auf,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Wie Sie am obigen Code sehen können, müssen wir das aufzurufende Tool und die übergebenen Argumente herausparsen und dann das Tool aufrufen.

## Verbesserung des Ansatzes mit Validierung

Bisher haben Sie gesehen, wie alle Registrierungen zur Hinzufügung von Tools, Ressourcen und Prompts durch diese zwei Handler pro Funktionstyp ersetzt werden können. Was müssen wir noch tun? Wir sollten eine Form der Validierung hinzufügen, um sicherzustellen, dass das Tool mit den richtigen Argumenten aufgerufen wird. Jede Laufzeitumgebung hat hier ihre eigene Lösung, zum Beispiel nutzt Python Pydantic und TypeScript verwendet Zod. Die Idee ist folgende:

- Die Logik zur Erstellung einer Funktion (Tool, Ressource oder Prompt) in ihren jeweiligen Ordner verschieben.
- Eine Möglichkeit hinzufügen, eine eingehende Anfrage beispielsweise für den Aufruf eines Tools zu validieren.

### Eine Funktion erstellen

Um eine Funktion zu erstellen, müssen wir eine Datei für diese Funktion anlegen und sicherstellen, dass sie die Pflichtfelder enthält, die für diese Funktion erforderlich sind. Welche Felder sich unterscheiden, hängt von Tools, Ressourcen und Prompts ab.

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
        # Eingaben mithilfe des Pydantic-Modells validieren
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic hinzufügen, damit wir ein AddInputModel erstellen und args validieren können

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Hier sehen Sie, wie Folgendes umgesetzt wird:

- Erstellung eines Schemas mit Pydantic `AddInputModel` mit den Feldern `a` und `b` in der Datei *schema.py*.
- Versuch, die eingehende Anfrage als Typ `AddInputModel` zu parsen; gibt es eine Parameterabweichung, schlägt dies fehl:

   ```python
   # add.py
    try:
        # Eingabe mit Pydantic-Modell validieren
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Sie können selbst entscheiden, ob Sie diese Parsing-Logik im eigentlichen Tool-Aufruf oder im Handler implementieren.

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

// hinzufügen.ts
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

- Im Handler, der alle Toolaufrufe bearbeitet, versuchen wir nun, die eingehende Anfrage in das definierte Schema des Tools zu parsen:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Wenn das funktioniert, fahren wir mit dem eigentlichen Tool-Aufruf fort:

    ```typescript
    const result = await tool.callback(input);
    ```

Wie Sie sehen, schafft dieser Ansatz eine großartige Architektur, da alles seinen Platz hat. Die *server.ts* ist eine sehr kleine Datei, die nur die Request-Handler verdrahtet und jede Funktion sich im jeweiligen Ordner befindet, also tools/, resources/ oder prompts/.

Super, lassen Sie uns als Nächstes versuchen, das zu bauen.

## Übung: Erstellen eines Low-Level-Servers

In dieser Übung machen wir Folgendes:

1. Einen Low-Level-Server erstellen, der das Auflisten und Aufrufen von Tools behandelt.
1. Eine Architektur implementieren, auf der Sie aufbauen können.
1. Validierung hinzufügen, die sicherstellt, dass Ihre Toolaufrufe korrekt validiert werden.

### -1- Eine Architektur erstellen

Das erste, was wir brauchen, ist eine Architektur, die uns beim Skalieren hilft, wenn wir mehr Funktionen hinzufügen. So sieht sie aus:

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

Jetzt haben wir eine Architektur eingerichtet, die es uns ermöglicht, einfach neue Tools in einem Tools-Ordner hinzuzufügen. Sie können gerne diesem Muster folgen, um Unterverzeichnisse für Ressourcen und Prompts hinzuzufügen.

### -2- Ein Tool erstellen

Sehen wir uns als Nächstes an, wie das Erstellen eines Tools aussieht. Es muss zuerst in seinem *tool*-Unterverzeichnis erstellt werden, so:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Eingaben mit Pydantic-Modell validieren
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")

    # TODO: Pydantic hinzufügen, damit wir ein AddInputModel erstellen und Argumente validieren können

    """Handler function for the add tool."""
    return float(input_model.a) + float(input_model.b)

tool_add = {
    "name": "add",
    "description": "Adds two numbers",
    "input_schema": AddInputModel,
    "handler": add_handler 
}
```

Hier sehen wir, wie Name, Beschreibung und Eingabeschema mit Pydantic definiert werden und ein Handler, der aufgerufen wird, sobald dieses Tool ausgeführt wird. Zum Schluss wird `tool_add` exponiert, ein Dictionary mit all diesen Eigenschaften.

Es gibt auch *schema.py*, das das Eingabeschema definiert, das von unserem Tool verwendet wird:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Wir müssen auch *__init__.py* befüllen, damit das Verzeichnis tools als Modul behandelt wird. Zusätzlich müssen wir die darin enthaltenen Module wie folgt exponieren:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Wir können diese Datei nach Bedarf erweitern, wenn wir weitere Tools hinzufügen.

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

Hier erstellen wir ein Objekt mit folgenden Eigenschaften:

- name: der Name des Tools.
- rawSchema: das Zod-Schema, das zur Validierung eingehender Anfragen zum Aufruf dieses Tools verwendet wird.
- inputSchema: dieses Schema wird von dem Handler genutzt.
- callback: wird verwendet, um das Tool aufzurufen.

Es gibt außerdem `Tool`, das dieses Objekt in einen Typ konvertiert, den der MCP-Server-Handler akzeptieren kann, und sieht so aus:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Und es gibt *schema.ts*, wo wir die Eingabeschemas für jedes Tool speichern, so wie hier mit momentan nur einem Schema, aber wir können für weitere Tools weitere Einträge hinzufügen:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, als Nächstes kümmern wir uns um das Listen unserer Tools.

### -3- Tool-Auflistung behandeln

Um das Auflisten von Tools zu behandeln, müssen wir einen Request-Handler dafür einrichten. Folgendes fügen wir unserer Server-Datei hinzu:

**Python**

```python
# Code aus Platzgründen weggelassen
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

Hier fügen wir den Dekorator `@server.list_tools` und die implementierende Funktion `handle_list_tools` hinzu. In letzterer müssen wir eine Liste von Tools erzeugen. Beachten Sie, dass jedes Tool einen Namen, eine Beschreibung und ein Eingabeschema haben muss.

**TypeScript**

Um den Request-Handler für die Toolauflistung einzurichten, rufen wir `setRequestHandler` auf dem Server mit einem Schema auf, das zu unserem Vorhaben passt, in diesem Fall `ListToolsRequestSchema`.

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
// Code aus Platzgründen weggelassen
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Gibt die Liste der registrierten Werkzeuge zurück
  return {
    tools: tools
  };
});
```

Prima, nun haben wir das Auflisten der Tools gelöst, schauen wir uns als Nächstes an, wie das Aufrufen von Tools funktioniert.

### -4- Einen Tool-Aufruf behandeln

Um ein Tool aufzurufen, müssen wir einen weiteren Request-Handler einrichten, der sich mit Anfragen befasst, die angeben, welche Funktion mit welchen Argumenten aufgerufen werden soll.

**Python**

Verwenden wir den Dekorator `@server.call_tool` und implementieren ihn mit einer Funktion wie `handle_call_tool`. Innerhalb dieser Funktion müssen wir den Namen des Tools und seine Argumente herausparsen und sicherstellen, dass die Argumente für das betreffende Tool gültig sind. Die Validierung der Argumente kann entweder hier oder weiter unten im tatsächlichen Tool erfolgen.

```python
@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, str] | None
) -> list[types.TextContent]:
    
    # tools ist ein Wörterbuch mit Werkzeugnamen als Schlüssel
    if name not in tools.tools:
        raise ValueError(f"Unknown tool: {name}")
    
    tool = tools.tools[name]

    result = "default"
    try:
        # das Werkzeug aufrufen
        result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)
    except Exception as e:
        raise ValueError(f"Error calling tool {name}: {str(e)}")

    return [
        types.TextContent(type="text", text=str(result))
    ]
```

Folgendes passiert:

- Unser Toolname liegt bereits als Eingabeparameter `name` vor, ebenso unsere Argumente in Form des Dictionaries `arguments`.

- Das Tool wird mit `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` aufgerufen. Die Validierung der Argumente passiert in der `handler`-Eigenschaft, die auf eine Funktion zeigt; schlägt sie fehl, wird eine Ausnahme ausgelöst.

Damit haben wir nun ein vollständiges Verständnis davon, wie man Tools mit einem Low-Level-Server auflistet und aufruft.

Siehe das [vollständige Beispiel](./code/README.md) hier

## Aufgabe

Erweitern Sie den Ihnen gegebenen Code um eine Anzahl von Tools, Ressourcen und Prompts und reflektieren Sie, wie Sie feststellen, dass Sie nur Dateien im Tools-Verzeichnis hinzufügen müssen und sonst nirgendwo.

*Keine Lösung angegeben*

## Zusammenfassung

In diesem Kapitel haben wir gesehen, wie der Low-Level-Server-Ansatz funktioniert und wie er uns hilft, eine schöne Architektur zu erstellen, auf der wir weiter aufbauen können. Wir haben außerdem Validierung besprochen und gezeigt bekommen, wie man mit Validierungsbibliotheken arbeitet, um Schemas für die Eingabevalidierung zu erstellen.

## Was kommt als Nächstes

- Nächstes Kapitel: [Einfache Authentifizierung](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle anzusehen. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
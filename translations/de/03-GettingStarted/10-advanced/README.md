# Erweiterte Server-Nutzung

Im MCP SDK gibt es zwei verschiedene Arten von Servern: Ihren normalen Server und den Low-Level-Server. Normalerweise würden Sie den regulären Server verwenden, um Funktionen hinzuzufügen. In manchen Fällen möchte man jedoch auf den Low-Level-Server zurückgreifen, beispielsweise:

- Bessere Architektur. Es ist möglich, eine saubere Architektur mit sowohl dem regulären Server als auch einem Low-Level-Server zu schaffen, aber es kann argumentiert werden, dass es mit einem Low-Level-Server etwas einfacher ist.
- Verfügbarkeit von Funktionen. Einige erweiterte Funktionen können nur mit einem
    Low-Level-Server verwendet werden. Spätere Kapitel behandeln Elicitation und die veraltete Sampling-Funktion,
    die in MCP `2026-07-28` veraltet ist.

## Regulärer Server vs. Low-Level-Server

So sieht die Erstellung eines MCP-Servers mit dem regulären Server aus

**Python**

```python
mcp = FastMCP("Demo")

# Fügen Sie ein Additionswerkzeug hinzu
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

// Fügen Sie ein Additionstool hinzu
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

Das Wesentliche ist, dass Sie explizit jedes Werkzeug, jede Ressource oder Eingabeaufforderung hinzufügen, die der Server haben soll. Daran ist nichts auszusetzen.  

### Low-Level-Server-Ansatz

Wenn Sie jedoch den Low-Level-Server-Ansatz verwenden, müssen Sie anders denken. Statt jedes Werkzeug zu registrieren, erstellen Sie stattdessen zwei Handler pro Funktionstyp (Werkzeuge, Ressourcen oder Eingabeaufforderungen). Zum Beispiel haben Werkzeuge dann nur zwei Funktionen:

- Auflisten aller Werkzeuge. Eine Funktion wäre für alle Versuche zuständig, Werkzeuge aufzulisten.
- Aufrufen aller Werkzeuge. Hier gibt es ebenfalls nur eine Funktion, die Aufrufe an ein Werkzeug behandelt.

Das klingt nach potentiell weniger Arbeit, oder? Statt ein Werkzeug zu registrieren, muss ich nur sicherstellen, dass das Werkzeug aufgelistet wird, wenn ich alle Werkzeuge aufliste, und dass es aufgerufen wird, wenn eine Anfrage zum Aufruf eines Werkzeugs eingegangen ist. 

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

Hier haben wir jetzt eine Funktion, die eine Liste von Features zurückgibt. Jeder Eintrag in der Werkzeugliste hat nun Felder wie `name`, `description` und `inputSchema`, um dem Rückgabetyp zu entsprechen. Das ermöglicht es uns, unsere Werkzeuge und Feature-Definitionen an anderer Stelle zu speichern. Wir können jetzt alle Werkzeuge in einem tools-Ordner erstellen, und das Gleiche gilt für alle Ihre Features, sodass Ihr Projekt plötzlich so organisiert sein kann:

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

Das ist großartig, unsere Architektur kann recht sauber gestaltet werden.

Und wie ist das mit dem Aufrufen von Werkzeugen, ist es dann dieselbe Idee, ein Handler, um ein Werkzeug aufzurufen, egal welches? Ja, genau, hier ist der Code dafür:

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
    
    // args: request.params.argumente
    // TODO rufe das Werkzeug auf,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Wie Sie im obigen Code sehen, müssen wir das aufzurufende Werkzeug und dessen Argumente herausfiltern und dann das Werkzeug aufrufen.

## Verbesserung des Ansatzes mit Validierung

Bisher haben Sie gesehen, wie all Ihre Registrierungen zum Hinzufügen von Werkzeugen, Ressourcen und Eingabeaufforderungen durch diese zwei Handler pro Funktionstyp ersetzt werden können. Was müssen wir sonst noch tun? Nun, wir sollten eine Art Validierung hinzufügen, um sicherzustellen, dass das Werkzeug mit den richtigen Argumenten aufgerufen wird. Jede Laufzeitumgebung hat dafür ihre eigene Lösung, zum Beispiel verwendet Python Pydantic und TypeScript Zod. Die Idee ist, Folgendes zu tun:

- Die Logik zur Erstellung eines Features (Werkzeug, Ressource oder Eingabeaufforderung) in seinen eigenen Ordner verschieben.
- Eine Möglichkeit hinzufügen, eine eingehende Anfrage zu validieren, z.B. zum Aufrufen eines Werkzeugs.

### Ein Feature erstellen

Um ein Feature zu erstellen, müssen wir eine Datei für dieses Feature anlegen und sicherstellen, dass es die erforderlichen Felder hat. Die Felder unterscheiden sich etwas zwischen Werkzeugen, Ressourcen und Eingabeaufforderungen.

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
        # Eingabe mit Pydantic-Modell validieren
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

Hier sehen Sie, wie wir Folgendes tun:

- Ein Schema mit Pydantic `AddInputModel` erstellen mit den Feldern `a` und `b` in der Datei *schema.py*.
- Versuchen, die eingehende Anfrage als `AddInputModel` zu parsen; bei Parameterabweichungen stürzt dies ab:

   ```python
   # add.py
    try:
        # Eingaben mit Pydantic-Modell validieren
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Sie können entscheiden, ob Sie diese Parsing-Logik im Werkzeugaufruf selbst oder in der Handler-Funktion platzieren.

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

- Im Handler für alle Werkzeugaufrufe versuchen wir nun, die eingehende Anfrage in das definierte Schema des Werkzeugs zu parsen:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Wenn das klappt, rufen wir das eigentliche Werkzeug auf:

    ```typescript
    const result = await tool.callback(input);
    ```

Wie Sie sehen, schafft dieser Ansatz eine großartige Architektur, da alles seinen Platz hat. Die *server.ts* ist eine sehr kleine Datei, die nur die Anforderungs-Handler verbindet, und jedes Feature befindet sich im jeweiligen Ordner, also tools/, resources/ oder prompts/.

Super, versuchen wir nun, das aufzubauen.

## Übung: Einen Low-Level-Server erstellen

In dieser Übung machen wir Folgendes:

1. Einen Low-Level-Server erstellen, der das Auflisten und Aufrufen von Werkzeugen behandelt.
1. Eine Architektur implementieren, auf der Sie aufbauen können.
1. Validierung hinzufügen, um sicherzustellen, dass Ihre Werkzeugaufrufe richtig validiert werden.

### -1- Eine Architektur erstellen

Das Erste, was wir angehen müssen, ist eine Architektur, die uns hilft, zu skalieren, während wir mehr Features hinzufügen. So sieht sie aus:

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

Nun haben wir eine Architektur eingerichtet, die es uns erlaubt, einfach neue Werkzeuge im tools-Ordner hinzuzufügen. Sie können gerne auch Unterverzeichnisse für resources und prompts anlegen.

### -2- Ein Werkzeug erstellen

Schauen wir uns an, wie man ein Werkzeug erstellt. Zuerst muss es im Unterverzeichnis *tool* so angelegt werden:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Eingaben mit dem Pydantic-Modell validieren
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

Hier sehen wir, wie wir Name, Beschreibung und Eingabeschema mit Pydantic definieren und einen Handler, der aufgerufen wird, wenn dieses Werkzeug benutzt wird. Schließlich exponieren wir `tool_add`, ein Dictionary, das all diese Eigenschaften enthält.

Es gibt auch *schema.py*, das benutzt wird, um das Eingabeschema für unser Werkzeug zu definieren:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Wir müssen auch *__init__.py* befüllen, damit das tools-Verzeichnis als Modul behandelt wird. Außerdem müssen wir die darin enthaltenen Module so exponieren:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Wir können diese Datei weiter ausbauen, wenn wir mehr Werkzeuge hinzufügen.

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

Hier erstellen wir ein Dictionary mit folgenden Eigenschaften:

- name: der Name des Werkzeugs.
- rawSchema: das ist das Zod-Schema, es wird verwendet, um Anfragen zum Aufrufen dieses Werkzeugs zu validieren.
- inputSchema: dieses Schema wird vom Handler verwendet.
- callback: das wird verwendet, um das Werkzeug aufzurufen.

Es gibt auch `Tool`, das dieses Dictionary in einen Typ umwandelt, den der MCP-Server-Handler akzeptieren kann, und es sieht so aus:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Und es gibt *schema.ts*, wo wir die Eingabeschemata für jedes Werkzeug speichern, wie hier gezeigt – derzeit nur mit einem Schema, aber mit weiteren Werkzeugen können weitere Einträge hinzugefügt werden:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, fahren wir fort mit dem Handhaben des Auflistens unserer Werkzeuge.

### -3- Werkzeug-Auflistung behandeln

Als nächstes brauchen wir einen Request-Handler, der das Auflisten unserer Werkzeuge bedient. Folgendes fügen wir zu unserer Server-Datei hinzu:

**Python**

```python
# Code aus Gründen der Kürze weggelassen
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

Hier fügen wir den Decorator `@server.list_tools` sowie die implementierende Funktion `handle_list_tools` hinzu. In letzterer müssen wir eine Liste von Werkzeugen erzeugen. Beachten Sie, dass jedes Werkzeug einen Namen, eine Beschreibung und ein inputSchema haben muss.   

**TypeScript**

Um den Request-Handler für das Auflisten von Werkzeugen einzurichten, müssen wir `setRequestHandler` auf dem Server mit einem passenden Schema, in diesem Fall `ListToolsRequestSchema`, aufrufen. 

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
// Code aus Gründen der Kürze ausgelassen
import { tools } from './tools/index.js';

server.setRequestHandler(ListToolsRequestSchema, async (request) => {
  // Gibt die Liste der registrierten Werkzeuge zurück
  return {
    tools: tools
  };
});
```

Prima, jetzt ist das Thema Auflisten von Werkzeugen gelöst, schauen wir uns an, wie wir Werkzeuge aufrufen können.

### -4- Werkzeugaufruf behandeln

Um ein Werkzeug aufzurufen, müssen wir einen weiteren Request-Handler einrichten, diesmal speziell für Anfragen, die angeben, welches Feature mit welchen Argumenten aufzurufen ist.

**Python**

Verwenden wir den Decorator `@server.call_tool` und implementieren ihn mit einer Funktion wie `handle_call_tool`. Innerhalb dieser Funktion müssen wir den Werkzeugnamen und seine Argumente parsen und sicherstellen, dass die Argumente für das jeweilige Werkzeug gültig sind. Die Validierung der Argumente kann entweder hier oder in dem tatsächlichen Werkzeug stattfinden.

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

So funktioniert es:

- Unser Werkzeugname ist bereits als Eingabeparameter `name` vorhanden, und unsere Argumente liegen als `arguments`-Dictionary vor.

- Das Werkzeug wird mit `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` aufgerufen. Die Validierung der Argumente erfolgt in der `handler`-Eigenschaft, die auf eine Funktion zeigt; falls das fehlschlägt, wird eine Ausnahme ausgelöst.

Damit haben wir nun ein vollständiges Verständnis, wie man Werkzeuge mit einem Low-Level-Server auflistet und aufruft.

Siehe das [vollständige Beispiel](./code/README.md) hier

## Aufgabe

Erweitern Sie den vorliegenden Code um eine Reihe von Werkzeugen, Ressourcen und Eingabeaufforderungen und reflektieren Sie dabei, wie Sie feststellen, dass Sie nur Dateien im tools-Verzeichnis hinzufügen müssen und sonst nirgends.

*Keine Lösung gegeben*

## Zusammenfassung

In diesem Kapitel haben wir gesehen, wie der Low-Level-Server-Ansatz funktioniert und wie dieser uns helfen kann, eine schöne Architektur zu schaffen, die wir weiter ausbauen können. Wir haben auch die Validierung besprochen und Ihnen gezeigt, wie Sie Validierungsbibliotheken zur Erstellung von Schemas für die Eingabevalidierung verwenden können.

## Was kommt als Nächstes

- Nächstes: [Einfache Authentifizierung](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
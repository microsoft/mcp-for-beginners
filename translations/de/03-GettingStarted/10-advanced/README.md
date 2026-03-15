# Erweiterte Server-Nutzung

Im MCP SDK gibt es zwei verschiedene Arten von Servern: den normalen Server und den Low-Level-Server. Normalerweise verwendet man den regulären Server, um Funktionen hinzuzufügen. In manchen Fällen möchte man jedoch auf den Low-Level-Server zurückgreifen, z.B.:

- Bessere Architektur. Es ist möglich, mit sowohl dem regulären Server als auch einem Low-Level-Server eine saubere Architektur zu erstellen, aber es kann argumentiert werden, dass es mit einem Low-Level-Server etwas einfacher ist.
- Verfügbarkeit von Funktionen. Einige erweiterte Funktionen können nur mit einem Low-Level-Server genutzt werden. Dies wird in späteren Kapiteln beim Hinzufügen von Sampling und Elicitation deutlich.

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

// Fügen Sie ein Additionswerkzeug hinzu
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

Der Punkt ist, dass man explizit jedes Tool, jede Ressource oder jeden Prompt hinzufügen muss, den der Server haben soll. Daran ist nichts falsch.

### Low-Level-Server-Ansatz

Beim Low-Level-Server-Ansatz muss man aber anders denken. Statt jedes Tool zu registrieren, erstellt man stattdessen zwei Handler pro Feature-Typ (Tools, Ressourcen oder Prompts). Zum Beispiel haben Tools dann nur zwei Funktionen wie folgt:

- Alle Tools auflisten. Eine Funktion ist für alle Versuche verantwortlich, Tools aufzulisten.
- Aufrufe aller Tools behandeln. Hier gibt es ebenfalls nur eine Funktion, die die Aufrufe eines Tools handhabt.

Das klingt nach potenziell weniger Arbeit, oder? Statt also ein Tool zu registrieren, muss ich nur sicherstellen, dass das Tool beim Auflisten aller Tools auftaucht und aufgerufen wird, wenn eine Anfrage zum Aufruf eines Tools eintrifft.

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

Hier haben wir jetzt eine Funktion, die eine Liste von Features zurückgibt. Jeder Eintrag in der Tool-Liste hat jetzt Felder wie `name`, `description` und `inputSchema`, um dem Rückgabetyp zu entsprechen. Das ermöglicht es uns, unsere Tools und Feature-Definitionen an anderer Stelle unterzubringen. Wir können nun alle unsere Tools in einem Tools-Ordner erstellen, genauso wie alle Features, sodass dein Projekt plötzlich so organisiert aussehen kann:

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

Und wie sieht es mit dem Aufruf von Tools aus? Ist es die gleiche Idee, also ein Handler, der jedes Tool aufruft? Ja, genau, hier ist der Code dafür:

**Python**

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
    // TODO Rufen Sie das Werkzeug auf,

    return {
       content: [{ type: "text", text: `Tool ${name} called with arguments: ${JSON.stringify(input)}, result: ${JSON.stringify(result)}` }]
    };
});
```

Aus dem obigen Code ist ersichtlich, dass wir das Tool, das aufgerufen werden soll, bestimmen und mit welchen Argumenten, und anschließend das Tool aufrufen müssen.

## Verbesserung des Ansatzes mit Validierung

Bisher hast du gesehen, wie alle Registrierungen zum Hinzufügen von Tools, Ressourcen und Prompts mit diesen zwei Handlern pro Feature-Typ ersetzt werden können. Was müssen wir sonst noch tun? Nun, wir sollten eine Form der Validierung hinzufügen, um sicherzustellen, dass das Tool mit den richtigen Argumenten aufgerufen wird. Jede Laufzeit hat dafür ihre eigene Lösung, z.B. verwendet Python Pydantic und TypeScript Zod. Die Idee ist folgende:

- Die Logik zur Erstellung eines Features (Tool, Ressource oder Prompt) in seinen eigenen Ordner verschieben.
- Eine Möglichkeit hinzufügen, eingehende Anfragen zu validieren, z.B. beim Aufruf eines Tools.

### Ein Feature erstellen

Um ein Feature zu erstellen, müssen wir eine Datei für dieses Feature anlegen und sicherstellen, dass sie die obligatorischen Felder enthält, die für dieses Feature erforderlich sind. Welche Felder das genau sind, unterscheidet sich leicht zwischen Tools, Ressourcen und Prompts.

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

Hier siehst du, wie wir Folgendes tun:

- Ein Schema mit Pydantic `AddInputModel` mit den Feldern `a` und `b` in der Datei *schema.py* erstellen.
- Versuchen, die eingehende Anfrage zu parsen, sodass sie vom Typ `AddInputModel` ist; bei Parameterabweichungen wird das scheitern:

   ```python
   # add.py
    try:
        # Eingabe mit Pydantic-Modell validieren
        input_model = AddInputModel(**args)
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")
   ```

Du kannst entscheiden, ob du diese Parsing-Logik im Tool-Aufruf selbst oder im Handler implementierst.

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

- Im Handler, der alle Tool-Aufrufe behandelt, versuchen wir nun, die eingehende Anfrage in das durch das Tool definierte Schema zu parsen:

    ```typescript
    const Schema = tool.rawSchema;

    try {
       const input = Schema.parse(request.params.arguments);
    ```

    Wenn das funktioniert, fahren wir mit dem tatsächlichen Aufruf des Tools fort:

    ```typescript
    const result = await tool.callback(input);
    ```

Wie man sieht, schafft dieser Ansatz eine großartige Architektur, da alles seinen Platz hat: *server.ts* ist eine sehr kleine Datei, die nur die Request-Handler verbindet, und jedes Feature befindet sich im jeweiligen Ordner, z.B. tools/, resources/ oder prompts/.

Super, lass uns das als Nächstes bauen.

## Übung: Erstellen eines Low-Level-Servers

In dieser Übung werden wir Folgendes tun:

1. Einen Low-Level-Server erstellen, der Tool-Listen und Tool-Aufrufe handhabt.
1. Eine Architektur implementieren, auf der du aufbauen kannst.
1. Validierung hinzufügen, um sicherzustellen, dass Tool-Aufrufe korrekt validiert werden.

### -1- Architektur erstellen

Als Erstes brauchen wir eine Architektur, die uns beim Skalieren hilft, wenn wir mehr Features hinzufügen. So sieht sie aus:

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

Jetzt haben wir eine Architektur eingerichtet, die es uns ermöglicht, einfach neue Tools in einem Tools-Ordner hinzuzufügen. Folge gerne diesem Beispiel, um weitere Unterverzeichnisse für Ressourcen und Prompts anzulegen.

### -2- Ein Tool erstellen

Schauen wir uns als Nächstes an, wie man ein Tool erstellt. Es muss zuerst im *tool*-Unterordner wie folgt erstellt werden:

**Python**

```python
from .schema import AddInputModel

async def add_handler(args) -> float:
    try:
        # Eingaben mit einem Pydantic-Modell validieren
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

Hier sehen wir, wie wir mit Pydantic den Namen, die Beschreibung und das Input-Schema definieren und einen Handler, der aufgerufen wird, wenn dieses Tool verwendet wird. Schließlich exponieren wir `tool_add`, ein Dictionary, das all diese Eigenschaften enthält.

Außerdem gibt es *schema.py*, das das Input-Schema für unser Tool definiert:

```python
from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float
```

Wir müssen auch *__init__.py* befüllen, damit das Tools-Verzeichnis als Modul behandelt wird. Zusätzlich müssen wir die Module darin so exponieren:

```python
from .add import tool_add

tools = {
  tool_add["name"] : tool_add
}
```

Wir können diese Datei weiterhin erweitern, wenn wir weitere Tools hinzufügen.

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

Hier erstellen wir ein Dictionary mit den Eigenschaften:

- name, das ist der Name des Tools.
- rawSchema, das ist das Zod-Schema, welches verwendet wird, um eingehende Anfragen zum Aufruf dieses Tools zu validieren.
- inputSchema, dieses Schema wird vom Handler verwendet.
- callback, das wird genutzt, um das Tool aufzurufen.

Außerdem gibt es `Tool`, das dieses Dictionary in einen Typ umwandelt, den der MCP-Server-Handler akzeptieren kann und das so aussieht:

```typescript
import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: z.ZodTypeAny;
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}
```

Und es gibt *schema.ts*, wo wir die Input-Schemas für jedes Tool speichern. Aktuell nur mit einem Schema, aber wenn wir mehr Tools hinzufügen, können wir weitere Einträge ergänzen:

```typescript
import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });
```

Super, als Nächstes kümmern wir uns um das Auflisten unserer Tools.

### -3- Tool-Auflistung behandeln

Als Nächstes müssen wir einen Request-Handler für das Auflisten unserer Tools einrichten. Folgendes fügen wir zur Server-Datei hinzu:

**Python**

```python
# Code aus Platzgründen ausgelassen
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

Hier fügen wir den Dekorator `@server.list_tools` und die Implementierung `handle_list_tools` hinzu. In letzterem müssen wir eine Liste von Tools erzeugen. Beachte, dass jedes Tool einen Namen, eine Beschreibung und ein InputSchema haben muss.

**TypeScript**

Um den Request-Handler für das Auflisten von Tools einzurichten, müssen wir `setRequestHandler` auf dem Server mit einem passenden Schema aufrufen, in diesem Fall `ListToolsRequestSchema`.

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

Super, jetzt haben wir das Auflisten von Tools gelöst, lass uns ansehen, wie Tool-Aufrufe aussehen können.

### -4- Tool-Aufruf behandeln

Um ein Tool aufzurufen, müssen wir einen weiteren Request-Handler einrichten, der sich darauf fokussiert, zu behandeln, welches Feature mit welchen Argumenten aufgerufen werden soll.

**Python**

Nutzen wir den Dekorator `@server.call_tool` und implementieren ihn mit einer Funktion wie `handle_call_tool`. In dieser Funktion müssen wir den Tool-Namen und seine Argumente parsen und sicherstellen, dass die Argumente für das entsprechende Tool gültig sind. Die Argumentvalidierung kann entweder in dieser Funktion oder später im eigentlichen Tool erfolgen.

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

Folgendes passiert hier:

- Unser Tool-Name ist als Eingabeparameter `name` bereits vorhanden, ebenso unsere Argumente als `arguments`-Dictionary.

- Das Tool wird mit `result = await tool["handler"](../../../../03-GettingStarted/10-advanced/arguments)` aufgerufen. Die Validierung der Argumente erfolgt in der `handler`-Eigenschaft, die auf eine Funktion zeigt; wenn das fehlschlägt, wird eine Ausnahme ausgelöst.

So, jetzt haben wir ein vollständiges Verständnis für das Auflisten und Aufrufen von Tools mittels eines Low-Level-Servers.

Siehe das [vollständige Beispiel](./code/README.md) hier

## Aufgabe

Erweitere den dir gegebenen Code um eine Reihe von Tools, Ressourcen und Prompts und reflektiere dabei, wie du nur noch Dateien im Tools-Verzeichnis hinzufügen musst und sonst nirgendwo.

*Keine Lösung vorgegeben*

## Zusammenfassung

In diesem Kapitel haben wir gesehen, wie der Low-Level-Server-Ansatz funktioniert und wie er uns hilft, eine schöne Architektur aufzubauen, auf der man weiter aufbauen kann. Wir haben zudem über Validierung gesprochen und dir gezeigt, wie du mit Validierungsbibliotheken Schemas zur Input-Validierung erstellst.

## Was kommt als Nächstes

- Nächstes Thema: [Einfache Authentifizierung](../11-simple-auth/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
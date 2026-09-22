# MCP-Server mit stdio-Transport

> **⚠️ Wichtige Aktualisierung**: Ab MCP-Spezifikation 2025-06-18 wurde der eigenständige SSE (Server-Sent Events)-Transport **veraltet** und durch den "Streamable HTTP"-Transport ersetzt. Die aktuelle MCP-Spezifikation definiert zwei primäre Transportmechanismen:
> 1. **stdio** - Standard-Ein-/Ausgabe (empfohlen für lokale Server)
> 2. **Streamable HTTP** - Für entfernte Server, die intern SSE verwenden können
>
> Diese Lektion wurde aktualisiert, um sich auf den **stdio-Transport** zu konzentrieren, der die empfohlene Methode für die meisten MCP-Serverimplementierungen ist.

Der stdio-Transport ermöglicht es MCP-Servern, über Standard-Ein- und Ausgabeströme mit Clients zu kommunizieren. Dies ist der am häufigsten verwendete und empfohlene Transportmechanismus in der aktuellen MCP-Spezifikation und bietet eine einfache und effiziente Möglichkeit, MCP-Server zu erstellen, die leicht in verschiedene Client-Anwendungen integriert werden können.

## Überblick

Diese Lektion behandelt, wie man MCP-Server mit dem stdio-Transport erstellt und konsumiert.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server mit dem stdio-Transport zu erstellen.
- Einen MCP-Server mit dem Inspector zu debuggen.
- Einen MCP-Server mit Visual Studio Code zu konsumieren.
- Die aktuellen MCP-Transportmechanismen zu verstehen und warum stdio empfohlen wird.


## stdio-Transport – Funktionsweise

Der stdio-Transport ist einer der zwei Standardtransports in der MCP-Spezifikation
`2026-07-28`. So funktioniert er:

- **Einfache Kommunikation**: Der Server liest JSON-RPC-Nachrichten von der Standardeingabe (`stdin`) und sendet Nachrichten an die Standardausgabe (`stdout`).
- **Prozessbasiert**: Der Client startet den MCP-Server als Unterprozess.
- **Nachrichtenformat**: Nachrichten sind einzelne JSON-RPC-Anfragen, -Benachrichtigungen oder -Antworten, durch Zeilenumbrüche getrennt.
- **Protokollierung**: Der Server KANN UTF-8-Zeichenketten zur Protokollierung an die Standardfehlerausgabe (`stderr`) schreiben.

### Wichtige Anforderungen:
- Nachrichten MÜSSEN durch Zeilenumbrüche getrennt sein und DÜRFEN keine eingebetteten Zeilenumbrüche enthalten
- Der Server DARF NICHT etwas an `stdout` schreiben, das keine gültige MCP-Nachricht ist
- Der Client DARF NICHT etwas an die `stdin` des Servers schreiben, das keine gültige MCP-Nachricht ist

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Im vorangegangenen Code:

- Importieren wir die `Server`-Klasse und `StdioServerTransport` aus dem MCP SDK
- Erstellen eine Server-Instanz mit grundlegender Konfiguration und Fähigkeiten
- Erstellen eine `StdioServerTransport`-Instanz und verbinden den Server damit, um Kommunikation über stdin/stdout zu ermöglichen

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Serverinstanz erstellen
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Im vorangegangenen Code:

- Erstellen wir eine Serverinstanz mit dem MCP SDK
- Definieren Tools mit Dekoratoren
- Verwenden den Kontextmanager stdio_server zur Handhabung des Transports

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Der Hauptunterschied zu SSE ist, dass stdio-Server:

- Kein Setup eines Webservers oder HTTP-Endpunkte benötigen
- Als Unterprozesse vom Client gestartet werden
- Über stdin/stdout-Kommunizieren
- Einfacher zu implementieren und zu debuggen sind

## Übung: Einen stdio-Server erstellen

Um unseren Server zu erstellen, müssen wir zwei Dinge beachten:

- Wir müssen einen Webserver verwenden, um Endpunkte für Verbindung und Nachrichten bereitzustellen.
## Labor: Einen einfachen MCP-stdio-Server erstellen

In diesem Labor erstellen wir einen einfachen MCP-Server mit dem empfohlenen stdio-Transport. Dieser Server stellt Werkzeuge bereit, die Clients mithilfe des Standard Model Context Protocol aufrufen können.

### Voraussetzungen

- Python 3.8 oder neuer
- MCP Python SDK: `pip install mcp`
- Grundkenntnisse in asynchroner Programmierung

Beginnen wir damit, unseren ersten MCP-stdio-Server zu erstellen:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Protokollierung konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Den Server erstellen
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # stdio-Transport verwenden
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Wichtige Unterschiede zur veralteten SSE-Methode

**Stdio-Transport (aktuelle Norm):**
- Einfaches Unterprozessmodell - Client startet den Server als Kindprozess
- Kommunikation über stdin/stdout mit JSON-RPC-Nachrichten
- Kein HTTP-Server-Setup erforderlich
- Bessere Leistung und Sicherheit
- Einfacheres Debugging und Entwicklung

**SSE-Transport (seit MCP 2025-06-18 veraltet):**
- Erforderlicher HTTP-Server mit SSE-Endpunkten
- Komplexere Einrichtung mit Webserver-Infrastruktur
- Zusätzliche Sicherheitsaspekte für HTTP-Endpunkte
- Wird jetzt durch Streamable HTTP für webbasierte Szenarien ersetzt

### Einen Server mit stdio-Transport erstellen

Um unseren stdio-Server zu erstellen, müssen wir:

1. **Die benötigten Bibliotheken importieren** - Wir brauchen die MCP-Serverkomponenten und den stdio-Transport
2. **Eine Serverinstanz erstellen** - Definieren Sie den Server mit seinen Fähigkeiten
3. **Tools definieren** - Fügen Sie die Funktionalität hinzu, die Sie bereitstellen möchten
4. **Den Transport einrichten** - Konfigurieren Sie die stdio-Kommunikation
5. **Den Server ausführen** - Starten Sie den Server und bearbeiten Sie Nachrichten

Bauen wir das Schritt für Schritt auf:

### Schritt 1: Einen einfachen stdio-Server erstellen

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Protokollierung konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Den Server erstellen
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Schritt 2: Weitere Tools hinzufügen

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Schritt 3: Den Server starten

Speichern Sie den Code als `server.py` und führen Sie ihn über die Kommandozeile aus:

```bash
python server.py
```

Der Server startet und wartet auf Eingaben von stdin. Er kommuniziert über JSON-RPC-Nachrichten über den stdio-Transport.

### Schritt 4: Testen mit dem Inspector

Sie können Ihren Server mit dem MCP Inspector testen:

1. Installieren Sie den Inspector: `npx @modelcontextprotocol/inspector`
2. Starten Sie den Inspector und verbinden ihn mit Ihrem Server
3. Testen Sie die erstellten Tools

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugging Ihres stdio-Servers

### Verwendung des MCP Inspectors

Der MCP Inspector ist ein wertvolles Werkzeug zum Debuggen und Testen von MCP-Servern. So verwenden Sie ihn mit Ihrem stdio-Server:

1. **Installieren Sie den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Starten Sie den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testen Sie Ihren Server**: Der Inspector bietet eine Weboberfläche, in der Sie:
   - Serverfähigkeiten anzeigen können
   - Tools mit verschiedenen Parametern testen können
   - JSON-RPC-Nachrichten überwachen können
   - Verbindungsprobleme debuggen können

### Verwendung von VS Code

Sie können Ihren MCP-Server auch direkt in VS Code debuggen:

1. Erstellen Sie eine Startkonfiguration in `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Setzen Sie Breakpoints im Servercode
3. Starten Sie den Debugger und testen Sie mit dem Inspector

### Häufige Debugging-Tipps

- Verwenden Sie `stderr` zum Protokollieren – schreiben Sie niemals an `stdout`, da es für MCP-Nachrichten reserviert ist
- Stellen Sie sicher, dass alle JSON-RPC-Nachrichten zeilenweise getrennt sind
- Testen Sie zunächst mit einfachen Tools, bevor Sie komplexe Funktionalität hinzufügen
- Verwenden Sie den Inspector, um Nachrichtenformate zu überprüfen

## Ihren stdio-Server in VS Code konsumieren

Sobald Sie Ihren MCP-stdio-Server gebaut haben, können Sie ihn in VS Code integrieren, um ihn mit Claude oder anderen MCP-kompatiblen Clients zu verwenden.

### Konfiguration

1. **Erstellen Sie eine MCP-Konfigurationsdatei** unter `%APPDATA%\Claude\claude_desktop_config.json` (Windows) oder `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Starten Sie Claude neu**: Schließen und öffnen Sie Claude, damit die neue Serverkonfiguration geladen wird.

3. **Testen Sie die Verbindung**: Starten Sie ein Gespräch mit Claude und versuchen Sie, die Tools Ihres Servers zu verwenden:
   - „Kannst du mich mit dem Begrüßungstool begrüßen?“
   - „Berechne die Summe von 15 und 27“
   - „Wie lauten die Serverinformationen?“

### Beispiel für einen TypeScript-stdio-Server

Hier ist ein vollständiges TypeScript-Beispiel als Referenz:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Werkzeuge hinzufügen
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET-stdio-Server-Beispiel

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Zusammenfassung

In dieser aktualisierten Lektion haben Sie gelernt:

- MCP-Server mit dem aktuellen **stdio-Transport** zu bauen (empfohlene Methode)
- Warum der SSE-Transport zugunsten von stdio und Streamable HTTP veraltet wurde
- Tools zu erstellen, die von MCP-Clients aufgerufen werden können
- Ihren Server mit dem MCP Inspector zu debuggen
- Ihren stdio-Server mit VS Code und Claude zu integrieren

Der stdio-Transport bietet eine einfachere, sicherere und leistungsfähigere Möglichkeit, MCP-Server zu erstellen, im Vergleich zum veralteten SSE-Ansatz. Er ist der empfohlene Transport für die meisten MCP-Serverimplementierungen ab der Spezifikation 2025-06-18.


### .NET

1. Erstellen wir zunächst einige Tools, dafür erstellen wir eine Datei *Tools.cs* mit folgendem Inhalt:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Übung: Ihren stdio-Server testen

Nachdem Sie Ihren stdio-Server erstellt haben, testen wir ihn, um sicherzugehen, dass er korrekt funktioniert.

### Voraussetzungen

1. Stellen Sie sicher, dass der MCP Inspector installiert ist:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ihr Servercode sollte gespeichert sein (z.B. als `server.py`)

### Testen mit dem Inspector

1. **Starten Sie den Inspector mit Ihrem Server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öffnen Sie die Weboberfläche**: Der Inspector öffnet ein Browserfenster, in dem Sie die Fähigkeiten Ihres Servers sehen.

3. **Testen Sie die Tools**: 
   - Probieren Sie das Tool `get_greeting` mit verschiedenen Namen aus
   - Testen Sie das Tool `calculate_sum` mit verschiedenen Zahlen
   - Rufen Sie das Tool `get_server_info` auf, um Server-Metadaten zu sehen

4. **Überwachen Sie die Kommunikation**: Der Inspector zeigt die JSON-RPC-Nachrichten, die zwischen Client und Server ausgetauscht werden.

### Was Sie sehen sollten

Wenn Ihr Server richtig gestartet ist, sollten Sie sehen:
- Serverfähigkeiten, die im Inspector aufgelistet sind
- Tools, die zum Testen verfügbar sind
- Erfolgreiche JSON-RPC-Nachrichten-Austausche
- Tool-Antworten, die in der Oberfläche angezeigt werden

### Häufig auftretende Probleme und Lösungen

**Server startet nicht:**
- Prüfen Sie, ob alle Abhängigkeiten installiert sind: `pip install mcp`
- Überprüfen Sie Python-Syntax und Einrückungen
- Suchen Sie nach Fehlermeldungen in der Konsole

**Tools werden nicht angezeigt:**
- Stellen Sie sicher, dass `@server.tool()`-Dekoratoren vorhanden sind
- Prüfen Sie, ob die Tool-Funktionen vor `main()` definiert sind
- Vergewissern Sie sich, dass der Server richtig konfiguriert ist

**Verbindungsprobleme:**
- Stellen Sie sicher, dass der Server den stdio-Transport korrekt verwendet
- Prüfen Sie, ob keine anderen Prozesse stören
- Überprüfen Sie die Syntax des Inspector-Kommandos

## Aufgabe

Versuchen Sie, Ihren Server mit mehr Fähigkeiten auszubauen. Siehe [diese Seite](https://api.chucknorris.io/), um zum Beispiel ein Tool hinzuzufügen, das eine API aufruft. Sie entscheiden, wie der Server aussehen soll. Viel Spaß :)
## Lösung

[Lösung](./solution/README.md) Hier ist eine mögliche Lösung mit funktionsfähigem Code.

## Wichtigste Erkenntnisse

Die wichtigsten Erkenntnisse dieses Kapitels sind:

- Der stdio-Transport ist der empfohlene Mechanismus für lokale MCP-Server.
- Der stdio-Transport ermöglicht nahtlose Kommunikation zwischen MCP-Servern und Clients über Standard-Ein- und Ausgabeströme.
- Sie können sowohl Inspector als auch Visual Studio Code verwenden, um stdio-Server direkt zu konsumieren, was Debugging und Integration erleichtert.

## Beispiele

- [Java-Rechner](../samples/java/calculator/README.md)
- [.Net-Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-Rechner](../samples/javascript/README.md)
- [TypeScript-Rechner](../samples/typescript/README.md)
- [Python-Rechner](../../../../03-GettingStarted/samples/python)

## Zusätzliche Ressourcen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Was kommt als Nächstes

## Nächste Schritte

Nachdem Sie gelernt haben, wie man MCP-Server mit dem stdio-Transport erstellt, können Sie sich fortgeschrittenen Themen zuwenden:

- **Weiter**: [HTTP-Streaming mit MCP (Streamable HTTP)](../06-http-streaming/README.md) - Lernen Sie den anderen unterstützten Transportmechanismus für entfernte Server kennen
- **Fortgeschritten**: [MCP Sicherheitsbest Practices](../../02-Security/README.md) - Implementieren Sie Sicherheit in Ihren MCP-Servern
- **Produktion**: [Bereitstellungsstrategien](../09-deployment/README.md) - Setzen Sie Ihre Server produktiv ein

## Zusätzliche Ressourcen

- [MCP-Spezifikation 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Aktuelle Spezifikation
- [MCP SDK Dokumentation](https://github.com/modelcontextprotocol/sdk) - SDK-Referenzen für alle Sprachen
- [Community-Beispiele](../../06-CommunityContributions/README.md) - Weitere Serverbeispiele aus der Community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
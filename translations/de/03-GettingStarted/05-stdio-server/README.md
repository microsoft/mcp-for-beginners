# MCP-Server mit stdio-Transport

> **⚠️ Wichtige Aktualisierung**: Ab der MCP-Spezifikation vom 18.06.2025 wurde der eigenständige SSE-Transport (Server-Sent Events) **veraltet** und durch den "Streamable HTTP"-Transport ersetzt. Die aktuelle MCP-Spezifikation definiert zwei primäre Transportmechanismen:
> 1. **stdio** - Standard-Eingabe/Ausgabe (empfohlen für lokale Server)
> 2. **Streamable HTTP** - Für Remote-Server, die intern SSE verwenden können
>
> Diese Lektion wurde aktualisiert, um sich auf den **stdio-Transport** zu konzentrieren, der für die meisten MCP-Server-Implementierungen empfohlen wird.

Der stdio-Transport ermöglicht MCP-Servern die Kommunikation mit Clients über Standard-Eingabe- und -Ausgabeströme. Dies ist der am häufigsten verwendete und empfohlene Transportmechanismus in der aktuellen MCP-Spezifikation und bietet eine einfache und effiziente Möglichkeit, MCP-Server zu erstellen, die leicht in verschiedene Client-Anwendungen integriert werden können.

## Überblick

Diese Lektion behandelt, wie MCP-Server mit dem stdio-Transport erstellt und genutzt werden können.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen MCP-Server mit dem stdio-Transport zu erstellen.
- Einen MCP-Server mit dem Inspector zu debuggen.
- Einen MCP-Server mit Visual Studio Code zu nutzen.
- Die aktuellen MCP-Transportmechanismen zu verstehen und zu wissen, warum stdio empfohlen wird.

## stdio-Transport – Funktionsweise

Der stdio-Transport ist einer von zwei unterstützten Transporttypen in der aktuellen MCP-Spezifikation (18.06.2025). So funktioniert er:

- **Einfache Kommunikation**: Der Server liest JSON-RPC-Nachrichten aus der Standard-Eingabe (`stdin`) und sendet Nachrichten an die Standard-Ausgabe (`stdout`).
- **Prozessbasiert**: Der Client startet den MCP-Server als Unterprozess.
- **Nachrichtenformat**: Nachrichten sind einzelne JSON-RPC-Anfragen, Benachrichtigungen oder Antworten, die durch Zeilenumbrüche getrennt sind.
- **Protokollierung**: Der Server KANN UTF-8-Zeichenfolgen zur Standard-Fehlerausgabe (`stderr`) schreiben, um Protokolle zu erstellen.

### Wichtige Anforderungen:
- Nachrichten MÜSSEN durch Zeilenumbrüche getrennt sein und DÜRFEN KEINE eingebetteten Zeilenumbrüche enthalten.
- Der Server DARF NICHTS an `stdout` schreiben, das keine gültige MCP-Nachricht ist.
- Der Client DARF NICHTS an die `stdin` des Servers schreiben, das keine gültige MCP-Nachricht ist.

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
```

Im obigen Code:

- Wir importieren die `Server`-Klasse und `StdioServerTransport` aus dem MCP-SDK.
- Wir erstellen eine Server-Instanz mit grundlegender Konfiguration und Fähigkeiten.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

Im obigen Code:

- Wir erstellen eine Server-Instanz mit dem MCP-SDK.
- Wir definieren Tools mithilfe von Dekoratoren.
- Wir verwenden den `stdio_server`-Kontextmanager, um den Transport zu verwalten.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Der Hauptunterschied zu SSE besteht darin, dass stdio-Server:

- Keine Einrichtung eines Webservers oder HTTP-Endpunkts erfordern.
- Als Unterprozesse vom Client gestartet werden.
- Über stdin/stdout-Ströme kommunizieren.
- Einfacher zu implementieren und zu debuggen sind.

## Übung: Erstellen eines stdio-Servers

Um unseren Server zu erstellen, müssen wir zwei Dinge beachten:

- Wir müssen einen Webserver verwenden, um Endpunkte für Verbindungen und Nachrichten bereitzustellen.

## Lab: Erstellen eines einfachen MCP-stdio-Servers

In diesem Lab erstellen wir einen einfachen MCP-Server mit dem empfohlenen stdio-Transport. Dieser Server wird Tools bereitstellen, die Clients mithilfe des Standard-Model Context Protocol aufrufen können.

### Voraussetzungen

- Python 3.8 oder höher
- MCP Python SDK: `pip install mcp`
- Grundlegendes Verständnis von asynchroner Programmierung

Beginnen wir mit der Erstellung unseres ersten MCP-stdio-Servers:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Hauptunterschiede zur veralteten SSE-Methode

**Stdio-Transport (aktueller Standard):**
- Einfaches Unterprozessmodell – Client startet Server als Kindprozess.
- Kommunikation über stdin/stdout mit JSON-RPC-Nachrichten.
- Keine Einrichtung eines HTTP-Servers erforderlich.
- Bessere Leistung und Sicherheit.
- Einfacheres Debugging und Entwicklung.

**SSE-Transport (veraltet ab MCP 18.06.2025):**
- Erforderte HTTP-Server mit SSE-Endpunkten.
- Komplexere Einrichtung mit Webserver-Infrastruktur.
- Zusätzliche Sicherheitsüberlegungen für HTTP-Endpunkte.
- Jetzt durch Streamable HTTP für webbasierte Szenarien ersetzt.

### Erstellen eines Servers mit stdio-Transport

Um unseren stdio-Server zu erstellen, müssen wir:

1. **Benötigte Bibliotheken importieren** – Wir benötigen die MCP-Server-Komponenten und den stdio-Transport.
2. **Server-Instanz erstellen** – Den Server mit seinen Fähigkeiten definieren.
3. **Tools definieren** – Die Funktionalität hinzufügen, die wir bereitstellen möchten.
4. **Transport einrichten** – stdio-Kommunikation konfigurieren.
5. **Server starten** – Den Server starten und Nachrichten verarbeiten.

Lassen Sie uns dies Schritt für Schritt umsetzen:

### Schritt 1: Erstellen eines einfachen stdio-Servers

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### Schritt 3: Server ausführen

Speichern Sie den Code als `server.py` und führen Sie ihn über die Kommandozeile aus:

```bash
python server.py
```

Der Server wird gestartet und wartet auf Eingaben über stdin. Er kommuniziert über JSON-RPC-Nachrichten über den stdio-Transport.

### Schritt 4: Testen mit dem Inspector

Sie können Ihren Server mit dem MCP Inspector testen:

1. Installieren Sie den Inspector: `npx @modelcontextprotocol/inspector`
2. Starten Sie den Inspector und verbinden Sie ihn mit Ihrem Server.
3. Testen Sie die Tools, die Sie erstellt haben.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debugging Ihres stdio-Servers

### Verwendung des MCP Inspectors

Der MCP Inspector ist ein wertvolles Tool zum Debuggen und Testen von MCP-Servern. So verwenden Sie ihn mit Ihrem stdio-Server:

1. **Inspector installieren**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector starten**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Server testen**: Der Inspector bietet eine Weboberfläche, in der Sie:
   - Serverfähigkeiten anzeigen.
   - Tools mit verschiedenen Parametern testen.
   - JSON-RPC-Nachrichten überwachen.
   - Verbindungsprobleme debuggen.

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

2. Setzen Sie Haltepunkte in Ihrem Servercode.
3. Führen Sie den Debugger aus und testen Sie mit dem Inspector.

### Allgemeine Debugging-Tipps

- Verwenden Sie `stderr` für Protokollierung – schreiben Sie niemals in `stdout`, da dies für MCP-Nachrichten reserviert ist.
- Stellen Sie sicher, dass alle JSON-RPC-Nachrichten durch Zeilenumbrüche getrennt sind.
- Testen Sie zuerst mit einfachen Tools, bevor Sie komplexe Funktionalität hinzufügen.
- Verwenden Sie den Inspector, um Nachrichtenformate zu überprüfen.

## Nutzung Ihres stdio-Servers in VS Code

Sobald Sie Ihren MCP-stdio-Server erstellt haben, können Sie ihn in VS Code integrieren, um ihn mit Claude oder anderen MCP-kompatiblen Clients zu verwenden.

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

2. **Claude neu starten**: Schließen und öffnen Sie Claude erneut, um die neue Serverkonfiguration zu laden.

3. **Verbindung testen**: Starten Sie ein Gespräch mit Claude und testen Sie die Tools Ihres Servers:
   - "Kannst du mich mit dem Begrüßungstool begrüßen?"
   - "Berechne die Summe von 15 und 27."
   - "Was sind die Serverinformationen?"

### TypeScript-Beispiel für stdio-Server

Hier ist ein vollständiges TypeScript-Beispiel zur Referenz:

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

// Add tools
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

### .NET-Beispiel für stdio-Server

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Zusammenfassung

In dieser aktualisierten Lektion haben Sie gelernt:

- MCP-Server mit dem aktuellen **stdio-Transport** (empfohlener Ansatz) zu erstellen.
- Verstanden, warum der SSE-Transport zugunsten von stdio und Streamable HTTP veraltet ist.
- Tools zu erstellen, die von MCP-Clients aufgerufen werden können.
- Ihren Server mit dem MCP Inspector zu debuggen.
- Ihren stdio-Server mit VS Code und Claude zu integrieren.

Der stdio-Transport bietet eine einfachere, sicherere und leistungsfähigere Möglichkeit, MCP-Server im Vergleich zur veralteten SSE-Methode zu erstellen. Er ist der empfohlene Transport für die meisten MCP-Server-Implementierungen gemäß der Spezifikation vom 18.06.2025.

### .NET

1. Lassen Sie uns zunächst einige Tools erstellen. Dazu erstellen wir eine Datei *Tools.cs* mit folgendem Inhalt:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Übung: Testen Ihres stdio-Servers

Nachdem Sie Ihren stdio-Server erstellt haben, testen Sie ihn, um sicherzustellen, dass er korrekt funktioniert.

### Voraussetzungen

1. Stellen Sie sicher, dass der MCP Inspector installiert ist:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ihr Servercode sollte gespeichert sein (z. B. als `server.py`).

### Testen mit dem Inspector

1. **Starten Sie den Inspector mit Ihrem Server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Weboberfläche öffnen**: Der Inspector öffnet ein Browserfenster, das die Fähigkeiten Ihres Servers anzeigt.

3. **Tools testen**: 
   - Testen Sie das `get_greeting`-Tool mit verschiedenen Namen.
   - Testen Sie das `calculate_sum`-Tool mit verschiedenen Zahlen.
   - Rufen Sie das `get_server_info`-Tool auf, um Server-Metadaten anzuzeigen.

4. **Kommunikation überwachen**: Der Inspector zeigt die JSON-RPC-Nachrichten, die zwischen Client und Server ausgetauscht werden.

### Was Sie sehen sollten

Wenn Ihr Server korrekt startet, sollten Sie Folgendes sehen:
- Serverfähigkeiten im Inspector aufgelistet.
- Tools, die zum Testen verfügbar sind.
- Erfolgreiche JSON-RPC-Nachrichtenaustausche.
- Tool-Antworten, die in der Oberfläche angezeigt werden.

### Häufige Probleme und Lösungen

**Server startet nicht:**
- Überprüfen Sie, ob alle Abhängigkeiten installiert sind: `pip install mcp`.
- Verifizieren Sie die Python-Syntax und Einrückungen.
- Suchen Sie nach Fehlermeldungen in der Konsole.

**Tools erscheinen nicht:**
- Stellen Sie sicher, dass `@server.tool()`-Dekoratoren vorhanden sind.
- Überprüfen Sie, ob Tool-Funktionen vor `main()` definiert sind.
- Vergewissern Sie sich, dass der Server korrekt konfiguriert ist.

**Verbindungsprobleme:**
- Stellen Sie sicher, dass der Server den stdio-Transport korrekt verwendet.
- Überprüfen Sie, ob keine anderen Prozesse stören.
- Verifizieren Sie die Syntax des Inspector-Befehls.

## Aufgabe

Versuchen Sie, Ihren Server mit weiteren Funktionen auszustatten. Sehen Sie sich [diese Seite](https://api.chucknorris.io/) an, um beispielsweise ein Tool hinzuzufügen, das eine API aufruft. Sie entscheiden, wie der Server aussehen soll. Viel Spaß :)

## Lösung

[Solution](./solution/README.md) Hier ist eine mögliche Lösung mit funktionierendem Code.

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Der stdio-Transport ist der empfohlene Mechanismus für lokale MCP-Server.
- Der stdio-Transport ermöglicht nahtlose Kommunikation zwischen MCP-Servern und Clients über Standard-Eingabe- und -Ausgabeströme.
- Sie können sowohl den Inspector als auch Visual Studio Code verwenden, um stdio-Server direkt zu nutzen, was Debugging und Integration erleichtert.

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

Nachdem Sie gelernt haben, wie MCP-Server mit dem stdio-Transport erstellt werden, können Sie sich mit fortgeschrittenen Themen beschäftigen:

- **Weiter**: [HTTP-Streaming mit MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lernen Sie den anderen unterstützten Transportmechanismus für Remote-Server kennen.
- **Fortgeschritten**: [MCP-Sicherheitsbest Practices](../../02-Security/README.md) – Implementieren Sie Sicherheit in Ihren MCP-Servern.
- **Produktion**: [Bereitstellungsstrategien](../09-deployment/README.md) – Stellen Sie Ihre Server für den Produktionseinsatz bereit.

## Zusätzliche Ressourcen

- [MCP-Spezifikation 18.06.2025](https://spec.modelcontextprotocol.io/specification/) – Offizielle Spezifikation.
- [MCP-SDK-Dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-Referenzen für alle Sprachen.
- [Community-Beispiele](../../06-CommunityContributions/README.md) – Weitere Server-Beispiele aus der Community.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
# MCP-Server mit stdio-Transport

> **⚠️ Wichtige Aktualisierung**: Ab der MCP-Spezifikation 2025-06-18 wurde der eigenständige SSE (Server-Sent Events) Transport **veraltet** und durch den "Streamable HTTP" Transport ersetzt. Die aktuelle MCP-Spezifikation definiert zwei primäre Transportmechanismen:
> 1. **stdio** – Standard Eingabe/Ausgabe (empfohlen für lokale Server)
> 2. **Streamable HTTP** – Für entfernte Server, die intern SSE verwenden können
>
> Diese Lektion wurde aktualisiert, um sich auf den **stdio-Transport** zu konzentrieren, der der empfohlene Ansatz für die meisten MCP-Serverimplementierungen ist.

Der stdio-Transport ermöglicht MCP-Servern die Kommunikation mit Clients über Standard-Eingabe- und Ausgabeströme. Dies ist der am häufigsten verwendete und empfohlene Transportmechanismus in der aktuellen MCP-Spezifikation und bietet eine einfache und effiziente Möglichkeit, MCP-Server zu erstellen, die leicht in verschiedene Client-Anwendungen integriert werden können.

## Überblick

Diese Lektion behandelt, wie man MCP-Server mit dem stdio-Transport erstellt und verwendet.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Einen MCP-Server mit dem stdio-Transport zu erstellen.
- Einen MCP-Server mit dem Inspector zu debuggen.
- Einen MCP-Server mit Visual Studio Code zu verwenden.
- Die aktuellen MCP-Transportmechanismen zu verstehen und warum stdio empfohlen wird.

## stdio Transport – Funktionsweise

Der stdio-Transport ist einer von zwei unterstützten Transporttypen in der aktuellen MCP-Spezifikation (2025-06-18). So funktioniert er:

- **Einfache Kommunikation**: Der Server liest JSON-RPC-Nachrichten von der Standardeingabe (`stdin`) und sendet Nachrichten an die Standardausgabe (`stdout`).
- **Prozessbasiert**: Der Client startet den MCP-Server als Unterprozess.
- **Nachrichtenformat**: Nachrichten sind einzelne JSON-RPC-Anfragen, Benachrichtigungen oder Antworten, die durch Zeilenumbrüche getrennt sind.
- **Logging**: Der Server KANN UTF-8-Zeichenfolgen zur Standardfehlerausgabe (`stderr`) für Logging-Zwecke schreiben.

### Wichtige Anforderungen:
- Nachrichten MÜSSEN durch Zeilenumbrüche getrennt sein und DÜRFEN keine eingebetteten Zeilenumbrüche enthalten
- Der Server DARF nichts zu `stdout` schreiben, das keine gültige MCP-Nachricht ist
- Der Client DARF nichts in die `stdin` des Servers schreiben, das keine gültige MCP-Nachricht ist

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

Im obigen Code:

- Importieren wir die Klasse `Server` und `StdioServerTransport` aus dem MCP SDK
- Erstellen wir eine Serverinstanz mit Basis-Konfiguration und Fähigkeiten
- Erstellen wir eine Instanz von `StdioServerTransport` und verbinden den Server damit, um Kommunikation über stdin/stdout zu ermöglichen

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

Im obigen Code:

- Erstellen wir eine Serverinstanz mit dem MCP SDK
- Definieren wir Werkzeuge mit Dekoratoren
- Verwenden wir den Kontextmanager `stdio_server`, um den Transport zu handhaben

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

Der wesentliche Unterschied zu SSE ist, dass stdio-Server:

- Keine Webserver-Konfiguration oder HTTP-Endpunkte benötigen
- Als Unterprozesse vom Client gestartet werden
- Über stdin/stdout kommunizieren
- Einfacher zu implementieren und zu debuggen sind

## Übung: Einen stdio-Server erstellen

Um unseren Server zu erstellen, müssen wir zwei Dinge beachten:

- Wir müssen einen Webserver verwenden, um Endpunkte für Verbindung und Nachrichten bereitzustellen.

## Labor: Einen einfachen MCP-stdio-Server erstellen

In diesem Labor erstellen wir einen einfachen MCP-Server mit dem empfohlenen stdio-Transport. Dieser Server stellt Werkzeuge bereit, die Clients mit dem standardmäßigen Model Context Protocol aufrufen können.

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

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server erstellen
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


## Wichtige Unterschiede zum veralteten SSE-Ansatz

**Stdio Transport (aktueller Standard):**

- Einfaches Unterprozessmodell – Client startet Server als Kindprozess
- Kommunikation über stdin/stdout mit JSON-RPC-Nachrichten
- Kein Einrichten eines HTTP-Servers erforderlich
- Bessere Leistung und Sicherheit
- Einfacheres Debugging und Entwicklung

**SSE Transport (ab MCP 2025-06-18 veraltet):**

- Erforderte HTTP-Server mit SSE-Endpunkten
- Komplexere Einrichtung mit Webserver-Infrastruktur
- Zusätzliche Sicherheitsaspekte für HTTP-Endpunkte
- Jetzt ersetzt durch Streamable HTTP für webbasierte Szenarien

### Einen Server mit stdio-Transport erstellen

Um unseren stdio-Server zu erstellen, müssen wir:

1. **Die benötigten Bibliotheken importieren** – Wir benötigen die MCP Server-Komponenten und den stdio-Transport
2. **Eine Serverinstanz erstellen** – Definiere den Server mit seinen Fähigkeiten
3. **Werkzeuge definieren** – Füge die Funktionalität hinzu, die wir bereitstellen möchten
4. **Den Transport einrichten** – Konfiguriere die stdio-Kommunikation
5. **Den Server starten** – Starte den Server und handle Nachrichten

Lasst uns das Schritt für Schritt aufbauen:

### Schritt 1: Einen einfachen stdio-Server erstellen

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Protokollierung konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Erstellen Sie den Server
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

### Schritt 2: Weitere Werkzeuge hinzufügen

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

### Schritt 3: Den Server ausführen

Speichere den Code als `server.py` und starte ihn über die Kommandozeile:

```bash
python server.py
```

Der Server startet und wartet auf Eingaben von stdin. Die Kommunikation erfolgt über JSON-RPC-Nachrichten über den stdio-Transport.

### Schritt 4: Testen mit dem Inspector

Du kannst deinen Server mit dem MCP Inspector testen:

1. Installiere den Inspector: `npx @modelcontextprotocol/inspector`
2. Starte den Inspector und richte ihn auf deinen Server aus
3. Teste die von dir erstellten Werkzeuge

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Debuggen deines stdio-Servers

### Verwendung des MCP Inspectors

Der MCP Inspector ist ein wertvolles Tool zum Debuggen und Testen von MCP-Servern. So kannst du ihn mit deinem stdio-Server verwenden:

1. **Installiere den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Starte den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Teste deinen Server**: Der Inspector bietet eine Weboberfläche, in der du:
   - Server-Fähigkeiten einsehen kannst
   - Werkzeuge mit verschiedenen Parametern testen kannst
   - JSON-RPC-Nachrichten überwachen kannst
   - Verbindungsprobleme debuggen kannst

### Verwendung von VS Code

Du kannst deinen MCP-Server auch direkt in VS Code debuggen:

1. Erstelle eine Startkonfiguration in `.vscode/launch.json`:
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

2. Setze Haltepunkte in deinem Servercode
3. Starte den Debugger und teste mit dem Inspector

### Häufige Debugging-Tipps

- Verwende `stderr` zum Logging – schreibe niemals in `stdout`, da dieser für MCP-Nachrichten reserviert ist
- Stelle sicher, dass alle JSON-RPC-Nachrichten zeilenweise getrennt sind
- Teste zunächst mit einfachen Werkzeugen, bevor du komplexe Funktionen hinzufügst
- Nutze den Inspector, um Nachrichtenformate zu überprüfen

## Verwendung deines stdio-Servers in VS Code

Nachdem du deinen MCP-stdio-Server gebaut hast, kannst du ihn in VS Code integrieren, um ihn mit Claude oder anderen MCP-kompatiblen Clients zu verwenden.

### Konfiguration

1. **Erstelle eine MCP-Konfigurationsdatei** unter `%APPDATA%\Claude\claude_desktop_config.json` (Windows) oder `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Starte Claude neu**: Schliesse und öffne Claude erneut, damit die neue Serverkonfiguration geladen wird.

3. **Teste die Verbindung**: Beginne ein Gespräch mit Claude und probiere die Werkzeuge deines Servers aus:
   - „Kannst du mich mit dem Begrüßungswerkzeug begrüßen?“
   - „Berechne die Summe von 15 und 27.“
   - „Was sind die Serverinformationen?“

### Beispiel für einen TypeScript-stdio-Server

Hier ein vollständiges TypeScript-Beispiel zum Nachschlagen:

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

### Beispiel für einen .NET-stdio-Server

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

In dieser aktualisierten Lektion hast du gelernt:

- MCP-Server mit dem aktuellen **stdio-Transport** (empfohlener Ansatz) zu bauen
- Warum der SSE-Transport zugunsten von stdio und Streamable HTTP veraltet ist
- Werkzeuge zu erstellen, die von MCP-Clients aufgerufen werden können
- Deinen Server mit dem MCP Inspector zu debuggen
- Deinen stdio-Server in VS Code und Claude zu integrieren

Der stdio-Transport bietet eine einfachere, sicherere und leistungsfähigere Möglichkeit, MCP-Server im Vergleich zum veralteten SSE-Ansatz zu erstellen. Er ist der empfohlene Transport für die meisten MCP-Serverimplementierungen gemäß der Spezifikation vom 2025-06-18.

### .NET

1. Erstellen wir zunächst einige Werkzeuge, dazu legen wir eine Datei *Tools.cs* mit folgendem Inhalt an:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## Übung: Deinen stdio-Server testen

Nachdem du deinen stdio-Server erstellt hast, wollen wir ihn testen, um sicherzugehen, dass er korrekt funktioniert.

### Voraussetzungen

1. Stelle sicher, dass du den MCP Inspector installiert hast:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Dein Servercode sollte gespeichert sein (z. B. als `server.py`)

### Testen mit dem Inspector

1. **Starte den Inspector mit deinem Server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öffne die Weboberfläche**: Der Inspector öffnet ein Browserfenster, das die Fähigkeiten deines Servers anzeigt.

3. **Teste die Werkzeuge**:
   - Probiere das Werkzeug `get_greeting` mit verschiedenen Namen aus
   - Teste das Werkzeug `calculate_sum` mit verschiedenen Zahlen
   - Rufe das Werkzeug `get_server_info` auf, um Server-Metadaten anzusehen

4. **Überwache die Kommunikation**: Der Inspector zeigt die zwischen Client und Server ausgetauschten JSON-RPC-Nachrichten an.

### Was du sehen solltest

Wenn dein Server korrekt startet, solltest du folgendes sehen:
- Im Inspector aufgelistete Server-Fähigkeiten
- Verfügbare Werkzeuge zum Testen
- Erfolgreich ausgetauschte JSON-RPC-Nachrichten
- Angezeigte Werkzeugantworten in der Oberfläche

### Häufige Probleme und Lösungen

**Server startet nicht:**
- Prüfe, ob alle Abhängigkeiten installiert sind: `pip install mcp`
- Überprüfe Python-Syntax und Einrückungen
- Suche nach Fehlermeldungen in der Konsole

**Werkzeuge werden nicht angezeigt:**
- Stelle sicher, dass `@server.tool()`-Dekoratoren vorhanden sind
- Prüfe, dass Werkzeugfunktionen vor `main()` definiert sind
- Verifiziere, dass der Server korrekt konfiguriert ist

**Verbindungsprobleme:**
- Stelle sicher, dass der Server den stdio-Transport korrekt verwendet
- Prüfe, ob keine anderen Prozesse stören
- Überprüfe die Syntax des Inspector-Kommandos

## Aufgabe

Versuche, deinen Server mit mehr Fähigkeiten auszubauen. Siehe [diese Seite](https://api.chucknorris.io/), um beispielsweise ein Werkzeug hinzuzufügen, das eine API aufruft. Du entscheidest, wie der Server aussehen soll. Viel Spaß :)

## Lösung

[Solution](./solution/README.md) Hier ist eine mögliche Lösung mit funktionierendem Code.

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Der stdio-Transport ist der empfohlene Mechanismus für lokale MCP-Server.
- Der stdio-Transport ermöglicht nahtlose Kommunikation zwischen MCP-Servern und Clients mittels Standard Ein- und Ausgabe.
- Du kannst sowohl Inspector als auch Visual Studio Code verwenden, um stdio-Server direkt zu konsumieren, was Debugging und Integration vereinfacht.

## Beispiele

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Zusätzliche Ressourcen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Was kommt als Nächstes

## Nächste Schritte

Nachdem du gelernt hast, wie man MCP-Server mit dem stdio-Transport baut, kannst du fortgeschrittenere Themen erkunden:

- **Als nächstes**: [HTTP Streaming mit MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lerne den anderen unterstützten Transportmechanismus für entfernte Server kennen
- **Fortgeschritten**: [MCP Security Best Practices](../../02-Security/README.md) – Implementiere Sicherheit in deinen MCP-Servern
- **Produktiv**: [Deployment-Strategien](../09-deployment/README.md) – Setze deine Server produktiv ein

## Zusätzliche Ressourcen

- [MCP Spezifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Offizielle Spezifikation
- [MCP SDK Dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-Referenzen für alle Sprachen
- [Community-Beispiele](../../06-CommunityContributions/README.md) – Weitere Server-Beispiele aus der Community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP-Server mit stdio-Transport

> **⚠️ Wichtige Aktualisierung**: Ab MCP-Spezifikation 2025-06-18 wurde der eigenständige SSE (Server-Sent Events)-Transport **veraltet** und durch den "Streamable HTTP"-Transport ersetzt. Die aktuelle MCP-Spezifikation definiert zwei Haupttransportmechanismen:
> 1. **stdio** – Standard-Eingabe/Ausgabe (empfohlen für lokale Server)
> 2. **Streamable HTTP** – Für entfernte Server, die intern SSE verwenden können
>
> Diese Lektion wurde aktualisiert und konzentriert sich auf den **stdio-Transport**, der die empfohlene Methode für die meisten MCP-Serverimplementierungen ist.

Der stdio-Transport ermöglicht es MCP-Servern, mit Clients über Standard-Eingabe- und Ausgabeströme zu kommunizieren. Dies ist der am häufigsten verwendete und empfohlene Transportmechanismus in der aktuellen MCP-Spezifikation und bietet eine einfache und effiziente Möglichkeit, MCP-Server zu erstellen, die sich leicht in verschiedene Client-Anwendungen integrieren lassen.

## Überblick

Diese Lektion behandelt, wie man MCP-Server mit dem stdio-Transport erstellt und nutzt.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Einen MCP-Server mit dem stdio-Transport zu erstellen.
- Einen MCP-Server mit dem Inspector zu debuggen.
- Einen MCP-Server mit Visual Studio Code zu nutzen.
- Die aktuellen MCP-Transportmechanismen zu verstehen und warum stdio empfohlen wird.

## stdio Transport – Funktionsweise

Der stdio-Transport ist einer von zwei unterstützten Transporttypen in der aktuellen MCP-Spezifikation (2025-06-18). So funktioniert er:

- **Einfache Kommunikation**: Der Server liest JSON-RPC-Nachrichten von der Standard-Eingabe (`stdin`) und sendet Nachrichten an die Standard-Ausgabe (`stdout`).
- **Prozessbasiert**: Der Client startet den MCP-Server als Unterprozess.
- **Nachrichtenformat**: Nachrichten sind einzelne JSON-RPC-Anfragen, Benachrichtigungen oder Antworten, die durch Zeilenumbrüche getrennt sind.
- **Protokollierung**: Der Server KANN UTF-8-Zeichenketten zur Standard-Fehlerausgabe (`stderr`) für Protokollierungszwecke schreiben.

### Wichtige Anforderungen:
- Nachrichten MÜSSEN durch Zeilenumbrüche begrenzt sein und DÜRFEN keine eingebetteten Zeilenumbrüche enthalten
- Der Server DARF nichts in `stdout` schreiben, das keine gültige MCP-Nachricht ist
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
```

Im vorigen Code:

- Importieren wir die Klasse `Server` und `StdioServerTransport` aus dem MCP SDK
- Erstellen eine Serverinstanz mit grundlegender Konfiguration und Funktionen

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

Im vorigen Code:

- Erstellen wir eine Serverinstanz mit dem MCP SDK
- Definieren Tools mit Dekoratoren
- Verwenden den Kontextmanager stdio_server, um den Transport zu handhaben

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

- Keine Einrichtung eines Webservers oder HTTP-Endpunkte benötigen
- Vom Client als Unterprozesse gestartet werden
- Über stdin/stdout Streams kommunizieren
- Einfacher zu implementieren und zu debuggen sind

## Übung: Einen stdio-Server erstellen

Um unseren Server zu erstellen, müssen wir zwei Dinge beachten:

- Wir müssen einen Webserver verwenden, um Endpunkte für Verbindung und Nachrichten bereitzustellen.

## Labor: Einen einfachen MCP stdio-Server erstellen

In diesem Labor erstellen wir einen einfachen MCP-Server mit dem empfohlenen stdio-Transport. Dieser Server stellt Tools bereit, die Clients über das Standard Model Context Protocol aufrufen können.

### Voraussetzungen

- Python 3.8 oder neuer
- MCP Python SDK: `pip install mcp`
- Grundlegendes Verständnis von asynchroner Programmierung

Beginnen wir damit, unseren ersten MCP stdio-Server zu erstellen:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Logging konfigurieren
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

## Hauptunterschiede zum veralteten SSE-Ansatz

**Stdio-Transport (aktueller Standard):**
- Einfaches Unterprozessmodell – der Client startet den Server als Kindprozess
- Kommunikation über stdin/stdout mit JSON-RPC-Nachrichten
- Keine Einrichtung eines HTTP-Servers erforderlich
- Bessere Leistung und Sicherheit
- Einfacheres Debugging und Entwicklung

**SSE-Transport (veraltet ab MCP 2025-06-18):**
- Erfordert HTTP-Server mit SSE-Endpunkten
- Komplexere Einrichtung mit Webserver-Infrastruktur
- Zusätzliche Sicherheitsaspekte für HTTP-Endpunkte
- Wurde durch Streamable HTTP für webbasierte Szenarien ersetzt

### Einen Server mit stdio-Transport erstellen

Um unseren stdio-Server zu erstellen, müssen wir:

1. **Die benötigten Bibliotheken importieren** – Wir benötigen die MCP-Serverkomponenten und den stdio-Transport
2. **Eine Serverinstanz erstellen** – Den Server mit seinen Funktionen definieren
3. **Tools definieren** – Funktionalitäten hinzufügen, die wir bereitstellen wollen
4. **Den Transport einrichten** – stdio-Kommunikation konfigurieren
5. **Den Server starten** – Den Server starten und Nachrichten bearbeiten

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

### Schritt 3: Server starten

Speichere den Code als `server.py` und starte ihn über die Kommandozeile:

```bash
python server.py
```

Der Server startet und wartet auf Eingaben von stdin. Er kommuniziert über JSON-RPC-Nachrichten via stdio-Transport.

### Schritt 4: Mit dem Inspector testen

Du kannst deinen Server mit dem MCP Inspector testen:

1. Installiere den Inspector: `npx @modelcontextprotocol/inspector`
2. Starte den Inspector und verbinde ihn mit deinem Server
3. Teste die erstellten Tools

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Deinen stdio-Server debuggen

### Verwendung des MCP Inspectors

Der MCP Inspector ist ein wertvolles Werkzeug zum Debuggen und Testen von MCP-Servern. So verwendest du ihn mit deinem stdio-Server:

1. **Installiere den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Starte den Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Teste deinen Server**: Der Inspector stellt eine Weboberfläche bereit, in der du:
   - Serverfunktionen einsehen kannst
   - Tools mit verschiedenen Parametern testen kannst
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

2. Setze Breakpoints in deinem Servercode
3. Starte den Debugger und teste mit dem Inspector

### Häufige Debugging-Tipps

- Nutze `stderr` für Protokollierung – schreibe niemals in `stdout`, da es für MCP-Nachrichten reserviert ist
- Stelle sicher, dass alle JSON-RPC-Nachrichten durch Zeilenumbrüche getrennt sind
- Teste zuerst mit einfachen Tools, bevor du komplexe Funktionalitäten hinzufügst
- Verwende den Inspector zur Überprüfung des Nachrichtenformats

## Deinen stdio-Server in VS Code verwenden

Nachdem du deinen MCP stdio-Server erstellt hast, kannst du ihn in VS Code integrieren, um ihn mit Claude oder anderen MCP-kompatiblen Clients zu nutzen.

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

2. **Starte Claude neu**: Schliesse und öffne Claude, um die neue Serverkonfiguration zu laden.

3. **Teste die Verbindung**: Starte ein Gespräch mit Claude und probiere die Tools deines Servers aus:
   - "Kannst du mich mit dem Begrüßungstool begrüßen?"
   - "Berechne die Summe von 15 und 27"
   - "Wie lauten die Serverinformationen?"

### TypeScript stdio-Server-Beispiel

Hier ein vollständiges TypeScript-Beispiel zur Referenz:

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

### .NET stdio-Server-Beispiel

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

- MCP-Server mit dem aktuellen **stdio-Transport** zu erstellen (empfohlener Ansatz)
- Warum der SSE-Transport zugunsten von stdio und Streamable HTTP veraltet ist
- Tools zu erstellen, die von MCP-Clients aufgerufen werden können
- Deinen Server mit dem MCP Inspector zu debuggen
- Deinen stdio-Server mit VS Code und Claude zu integrieren

Der stdio-Transport bietet eine einfachere, sicherere und leistungsfähigere Möglichkeit, MCP-Server zu erstellen als der veraltete SSE-Ansatz. Er ist der empfohlene Transport für die meisten MCP-Serverimplementierungen gemäß der Spezifikation vom 2025-06-18.

### .NET

1. Erstellen wir zunächst einige Tools, dazu legen wir eine Datei *Tools.cs* mit folgendem Inhalt an:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Übung: Deinen stdio-Server testen

Nachdem du deinen stdio-Server erstellt hast, testen wir ihn, um sicherzustellen, dass er korrekt funktioniert.

### Voraussetzungen

1. Stelle sicher, dass der MCP Inspector installiert ist:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Dein Server-Code sollte gespeichert sein (z.B. als `server.py`)

### Testen mit dem Inspector

1. **Starte den Inspector mit deinem Server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öffne die Weboberfläche**: Der Inspector öffnet ein Browserfenster, das die Serverfähigkeiten anzeigt.

3. **Teste die Tools**:
   - Probiere das Tool `get_greeting` mit verschiedenen Namen aus
   - Teste das Tool `calculate_sum` mit verschiedenen Zahlen
   - Rufe das Tool `get_server_info` auf, um Server-Metadaten zu sehen

4. **Überwache die Kommunikation**: Der Inspector zeigt die JSON-RPC-Nachrichten, die zwischen Client und Server ausgetauscht werden.

### Was du sehen solltest

Wenn dein Server korrekt startet, solltest du Folgendes sehen:
- Serverfunktionen im Inspector aufgelistet
- Tools für Tests verfügbar
- Erfolgreiche JSON-RPC-Nachrichtenaustausche
- Tool-Antworten werden in der Oberfläche angezeigt

### Häufige Probleme und Lösungen

**Server startet nicht:**
- Prüfe, ob alle Abhängigkeiten installiert sind: `pip install mcp`
- Überprüfe Python-Syntax und Einrückungen
- Achte auf Fehlermeldungen in der Konsole

**Tools erscheinen nicht:**
- Stelle sicher, dass `@server.tool()` Dekoratoren vorhanden sind
- Überprüfe, ob Tool-Funktionen vor `main()` definiert sind
- Verifiziere, dass der Server korrekt konfiguriert ist

**Verbindungsprobleme:**
- Stelle sicher, dass der Server stdio-Transport korrekt verwendet
- Prüfe, ob keine anderen Prozesse stören
- Überprüfe die Inspector-Befehlsyntax

## Aufgabe

Versuche, deinen Server mit mehr Funktionen auszustatten. Sieh dir [diese Seite](https://api.chucknorris.io/) an, um z.B. ein Tool hinzuzufügen, das eine API aufruft. Du entscheidest, wie dein Server aussehen soll. Viel Spaß :)

## Lösung

[Solution](./solution/README.md) Hier ist eine mögliche Lösung mit funktionierendem Code.

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse aus diesem Kapitel sind:

- Der stdio-Transport ist der empfohlene Mechanismus für lokale MCP-Server.
- Der stdio-Transport ermöglicht nahtlose Kommunikation zwischen MCP-Servern und Clients über Standard-Ein- und Ausgabeströme.
- Du kannst sowohl Inspector als auch Visual Studio Code nutzen, um stdio-Server direkt zu konsumieren, was Debugging und Integration vereinfacht.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)

## Zusätzliche Ressourcen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Was kommt als Nächstes

## Nächste Schritte

Nachdem du gelernt hast, wie man MCP-Server mit dem stdio-Transport erstellt, kannst du dich fortgeschrittenen Themen widmen:

- **Als Nächstes**: [HTTP-Streaming mit MCP (Streamable HTTP)](../06-http-streaming/README.md) – Erfahre mehr über den anderen unterstützten Transportmechanismus für entfernte Server
- **Fortgeschritten**: [MCP-Sicherheitsbest Practices](../../02-Security/README.md) – Sicherheit in deinen MCP-Servern implementieren
- **Produktion**: [Bereitstellungsstrategien](../09-deployment/README.md) – Server produktiv einsetzen

## Zusätzliche Ressourcen

- [MCP-Spezifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Offizielle Spezifikation
- [MCP SDK-Dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-Referenzen für alle Sprachen
- [Community-Beispiele](../../06-CommunityContributions/README.md) – Weitere Serverbeispiele aus der Community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
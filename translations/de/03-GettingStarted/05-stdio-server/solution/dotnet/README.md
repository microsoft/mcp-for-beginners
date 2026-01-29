# MCP stdio Server - .NET-Lösung

> **⚠️ Wichtig**: Diese Lösung wurde aktualisiert, um den **stdio-Transport** gemäß der MCP-Spezifikation vom 18.06.2025 zu verwenden. Der ursprüngliche SSE-Transport wurde veraltet.

## Überblick

Diese .NET-Lösung zeigt, wie man einen MCP-Server mit dem aktuellen stdio-Transport erstellt. Der stdio-Transport ist einfacher, sicherer und bietet eine bessere Leistung als der veraltete SSE-Ansatz.

## Voraussetzungen

- .NET 9.0 SDK oder höher
- Grundlegendes Verständnis von .NET Dependency Injection

## Installationsanleitung

### Schritt 1: Abhängigkeiten wiederherstellen

```bash
dotnet restore
```

### Schritt 2: Projekt bauen

```bash
dotnet build
```

## Server starten

Der stdio-Server funktioniert anders als der alte HTTP-basierte Server. Anstatt einen Webserver zu starten, kommuniziert er über stdin/stdout:

```bash
dotnet run
```

**Wichtig**: Der Server scheint zu hängen – das ist normal! Er wartet auf JSON-RPC-Nachrichten über stdin.

## Server testen

### Methode 1: Mit dem MCP Inspector (empfohlen)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dies wird:
1. Ihren Server als Unterprozess starten
2. Eine Weboberfläche zum Testen öffnen
3. Ihnen ermöglichen, alle Server-Tools interaktiv zu testen

### Methode 2: Direkter Test über die Kommandozeile

Sie können auch testen, indem Sie den Inspector direkt starten:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Verfügbare Tools

Der Server stellt folgende Tools bereit:

- **AddNumbers(a, b)**: Zwei Zahlen addieren
- **MultiplyNumbers(a, b)**: Zwei Zahlen multiplizieren  
- **GetGreeting(name)**: Eine personalisierte Begrüßung generieren
- **GetServerInfo()**: Informationen über den Server abrufen

### Testen mit Claude Desktop

Um diesen Server mit Claude Desktop zu verwenden, fügen Sie diese Konfiguration zu Ihrer `claude_desktop_config.json` hinzu:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Projektstruktur

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Wichtige Unterschiede zu HTTP/SSE

**stdio-Transport (aktuell):**
- ✅ Einfachere Einrichtung – kein Webserver erforderlich
- ✅ Bessere Sicherheit – keine HTTP-Endpunkte
- ✅ Verwendet `Host.CreateApplicationBuilder()` statt `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` statt `WithHttpTransport()`
- ✅ Konsolenanwendung statt Webanwendung
- ✅ Bessere Leistung

**HTTP/SSE-Transport (veraltet):**
- ❌ Erforderte ASP.NET Core-Webserver
- ❌ Benötigte `app.MapMcp()`-Routing-Einrichtung
- ❌ Komplexere Konfiguration und Abhängigkeiten
- ❌ Zusätzliche Sicherheitsüberlegungen
- ❌ Seit MCP 18.06.2025 veraltet

## Entwicklungsfunktionen

- **Dependency Injection**: Vollständige DI-Unterstützung für Services und Logging
- **Strukturiertes Logging**: Korrektes Logging auf stderr mit `ILogger<T>`
- **Tool-Attribute**: Saubere Tool-Definition mit `[McpServerTool]`-Attributen
- **Async-Unterstützung**: Alle Tools unterstützen asynchrone Operationen
- **Fehlerbehandlung**: Elegante Fehlerbehandlung und Logging

## Entwicklungstipps

- Verwenden Sie `ILogger` für Logging (schreiben Sie niemals direkt auf stdout)
- Bauen Sie mit `dotnet build`, bevor Sie testen
- Testen Sie mit dem Inspector für visuelles Debugging
- Alle Logs werden automatisch auf stderr ausgegeben
- Der Server verarbeitet Shutdown-Signale elegant

Diese Lösung folgt der aktuellen MCP-Spezifikation und zeigt Best Practices für die Implementierung des stdio-Transports mit .NET.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
# MCP stdio Server - TypeScript-Lösung

> **⚠️ Wichtig**: Diese Lösung wurde aktualisiert, um den **stdio-Transport** gemäß der MCP-Spezifikation vom 18.06.2025 zu verwenden. Der ursprüngliche SSE-Transport wurde veraltet.

## Überblick

Diese TypeScript-Lösung zeigt, wie man einen MCP-Server mit dem aktuellen stdio-Transport erstellt. Der stdio-Transport ist einfacher, sicherer und bietet eine bessere Leistung als der veraltete SSE-Ansatz.

## Voraussetzungen

- Node.js 18+ oder höher
- npm- oder yarn-Paketmanager

## Installationsanleitung

### Schritt 1: Abhängigkeiten installieren

```bash
npm install
```

### Schritt 2: Projekt bauen

```bash
npm run build
```

## Server starten

Der stdio-Server funktioniert anders als der alte SSE-Server. Anstatt einen Webserver zu starten, kommuniziert er über stdin/stdout:

```bash
npm start
```

**Wichtig**: Der Server scheint zu hängen – das ist normal! Er wartet auf JSON-RPC-Nachrichten über stdin.

## Server testen

### Methode 1: Mit dem MCP Inspector (Empfohlen)

```bash
npm run inspector
```

Dies wird:
1. Ihren Server als Unterprozess starten
2. Eine Weboberfläche zum Testen öffnen
3. Ihnen ermöglichen, alle Server-Tools interaktiv zu testen

### Methode 2: Direkter Test über die Kommandozeile

Sie können auch testen, indem Sie den Inspector direkt starten:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Verfügbare Tools

Der Server stellt folgende Tools bereit:

- **add(a, b)**: Zwei Zahlen addieren
- **multiply(a, b)**: Zwei Zahlen multiplizieren  
- **get_greeting(name)**: Eine personalisierte Begrüßung generieren
- **get_server_info()**: Informationen über den Server abrufen

### Testen mit Claude Desktop

Um diesen Server mit Claude Desktop zu verwenden, fügen Sie diese Konfiguration zu Ihrer `claude_desktop_config.json` hinzu:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Projektstruktur

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Wichtige Unterschiede zu SSE

**stdio-Transport (Aktuell):**
- ✅ Einfachere Einrichtung – kein HTTP-Server erforderlich
- ✅ Bessere Sicherheit – keine HTTP-Endpunkte
- ✅ Kommunikation über Unterprozesse
- ✅ JSON-RPC über stdin/stdout
- ✅ Höhere Leistung

**SSE-Transport (Veraltet):**
- ❌ Erforderte Einrichtung eines Express-Servers
- ❌ Benötigte komplexes Routing und Sitzungsmanagement
- ❌ Mehr Abhängigkeiten (Express, HTTP-Verarbeitung)
- ❌ Zusätzliche Sicherheitsüberlegungen
- ❌ Seit MCP 18.06.2025 veraltet

## Entwicklungstipps

- Verwenden Sie `console.error()` für Logging (niemals `console.log()`, da es in stdout schreibt)
- Bauen Sie das Projekt mit `npm run build`, bevor Sie testen
- Testen Sie mit dem Inspector für visuelles Debugging
- Stellen Sie sicher, dass alle JSON-Nachrichten korrekt formatiert sind
- Der Server führt bei SIGINT/SIGTERM automatisch einen sauberen Shutdown durch

Diese Lösung folgt der aktuellen MCP-Spezifikation und zeigt Best Practices für die Implementierung des stdio-Transports mit TypeScript.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
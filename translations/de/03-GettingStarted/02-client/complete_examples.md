# Vollständige MCP-Client-Beispiele

Dieses Verzeichnis enthält vollständige, funktionierende Beispiele für MCP-Clients in verschiedenen Programmiersprachen. Jeder Client demonstriert die gesamte Funktionalität, die im Haupttutorial README.md beschrieben wird.

## Verfügbare Clients

### 1. Java-Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) über HTTP
- **Zielserver**: `http://localhost:8080`
- **Funktionen**:
  - Verbindungsaufbau und Ping
  - Auflistung von Tools
  - Rechneroperationen (addieren, subtrahieren, multiplizieren, dividieren, Hilfe)
  - Fehlerbehandlung und Ergebnisauswertung

**Ausführen:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C#-Client (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Ein-/Ausgabe)
- **Zielserver**: Lokaler .NET MCP-Server über dotnet run
- **Funktionen**:
  - Automatischer Serverstart über Stdio-Transport
  - Auflistung von Tools und Ressourcen
  - Rechneroperationen
  - JSON-Ergebnisanalyse
  - Umfassende Fehlerbehandlung

**Ausführen:**

```bash
dotnet run
```

### 3. TypeScript-Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Ein-/Ausgabe)
- **Zielserver**: Lokaler Node.js MCP-Server
- **Funktionen**:
  - Vollständige Unterstützung des MCP-Protokolls
  - Tool-, Ressourcen- und Prompt-Operationen
  - Rechneroperationen
  - Lesen von Ressourcen und Ausführung von Prompts
  - Robuste Fehlerbehandlung

**Ausführen:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python-Client (`client_example_python.py`)

- **Transport**: Stdio (Standard Ein-/Ausgabe)  
- **Zielserver**: Lokaler Python MCP-Server
- **Funktionen**:
  - Async/await-Muster für Operationen
  - Entdeckung von Tools und Ressourcen
  - Testen von Rechneroperationen
  - Lesen von Ressourceninhalten
  - Klassenbasierte Organisation

**Ausführen:**

```bash
python client_example_python.py
```

## Gemeinsame Funktionen aller Clients

Jede Client-Implementierung demonstriert:

1. **Verbindungsmanagement**
   - Aufbau der Verbindung zum MCP-Server
   - Behandlung von Verbindungsfehlern
   - Ordnungsgemäße Bereinigung und Ressourcenmanagement

2. **Server-Erkennung**
   - Auflistung verfügbarer Tools
   - Auflistung verfügbarer Ressourcen (falls unterstützt)
   - Auflistung verfügbarer Prompts (falls unterstützt)

3. **Tool-Aufrufe**
   - Grundlegende Rechneroperationen (addieren, subtrahieren, multiplizieren, dividieren)
   - Hilfe-Befehl für Serverinformationen
   - Ordnungsgemäße Argumentübergabe und Ergebnisverarbeitung

4. **Fehlerbehandlung**
   - Verbindungsfehler
   - Fehler bei der Tool-Ausführung
   - Gnadenvolles Scheitern und Benutzerfeedback

5. **Ergebnisverarbeitung**
   - Extrahieren von Textinhalten aus Antworten
   - Formatierung der Ausgabe für bessere Lesbarkeit
   - Umgang mit verschiedenen Antwortformaten

## Voraussetzungen

Bevor Sie diese Clients ausführen, stellen Sie sicher, dass:

1. **Der entsprechende MCP-Server läuft** (aus `../01-first-server/`)
2. **Die erforderlichen Abhängigkeiten installiert sind** für die gewählte Sprache
3. **Eine ordnungsgemäße Netzwerkverbindung besteht** (für HTTP-basierte Transports)

## Wichtige Unterschiede zwischen den Implementierungen

| Sprache    | Transport | Server-Start   | Async-Modell | Wichtige Bibliotheken |
|------------|-----------|----------------|--------------|------------------------|
| Java       | SSE/HTTP  | Extern         | Sync         | WebFlux, MCP SDK      |
| C#         | Stdio     | Automatisch    | Async/Await  | .NET MCP SDK          |
| TypeScript | Stdio     | Automatisch    | Async/Await  | Node MCP SDK          |
| Python     | Stdio     | Automatisch    | AsyncIO      | Python MCP SDK        |
| Rust       | Stdio     | Automatisch    | Async/Await  | Rust MCP SDK, Tokio   |

## Nächste Schritte

Nachdem Sie diese Client-Beispiele erkundet haben:

1. **Modifizieren Sie die Clients**, um neue Funktionen oder Operationen hinzuzufügen
2. **Erstellen Sie Ihren eigenen Server** und testen Sie ihn mit diesen Clients
3. **Experimentieren Sie mit verschiedenen Transports** (SSE vs. Stdio)
4. **Entwickeln Sie eine komplexere Anwendung**, die MCP-Funktionalität integriert

## Fehlerbehebung

### Häufige Probleme

1. **Verbindung verweigert**: Stellen Sie sicher, dass der MCP-Server auf dem erwarteten Port/Pfad läuft
2. **Modul nicht gefunden**: Installieren Sie das erforderliche MCP SDK für Ihre Sprache
3. **Zugriff verweigert**: Überprüfen Sie die Dateiberechtigungen für den Stdio-Transport
4. **Tool nicht gefunden**: Vergewissern Sie sich, dass der Server die erwarteten Tools implementiert

### Debug-Tipps

1. **Aktivieren Sie ausführliches Logging** in Ihrem MCP SDK
2. **Überprüfen Sie die Server-Logs** auf Fehlermeldungen
3. **Verifizieren Sie Tool-Namen und Signaturen**, die zwischen Client und Server übereinstimmen
4. **Testen Sie zuerst mit MCP Inspector**, um die Serverfunktionalität zu validieren

## Verwandte Dokumentation

- [Haupt-Client-Tutorial](./README.md)
- [MCP-Server-Beispiele](../../../../03-GettingStarted/01-first-server)
- [MCP mit LLM-Integration](../../../../03-GettingStarted/03-llm-client)
- [Offizielle MCP-Dokumentation](https://modelcontextprotocol.io/)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
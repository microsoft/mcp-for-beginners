# Debuggen mit MCP Inspector

> [!NOTE]
> Befehle mit `--sse` und URLs, die auf `/sse` enden, testen den Legacy HTTP+SSE
> Transport. Für einen neuen MCP `2026-07-28` Server verwenden Sie eine Inspector-Version, die
> Streamable HTTP unterstützt und wählen stattdessen diesen Transport.

Der **MCP Inspector** ist ein unverzichtbares Debugging-Tool, mit dem Sie Ihre MCP-Server interaktiv testen und Fehler beheben können, ohne eine vollständige KI-Host-Anwendung zu benötigen. Man kann ihn als „Postman für MCP“ betrachten – er bietet eine visuelle Oberfläche zum Senden von Anfragen, Anzeigen von Antworten und Verstehen des Serververhaltens.

## Warum MCP Inspector verwenden?

Beim Erstellen von MCP-Servern begegnen Ihnen häufig folgende Herausforderungen:

- **„Läuft mein Server überhaupt?“** - Inspector zeigt den Verbindungsstatus an
- **„Sind meine Tools korrekt registriert?“** - Inspector listet alle verfügbaren Tools auf
- **„Wie ist das Antwortformat?“** - Inspector zeigt vollständige JSON-Antworten an
- **„Warum funktioniert dieses Tool nicht?“** - Inspector zeigt detaillierte Fehlermeldungen an

## Voraussetzungen

- Node.js 18+ installiert
- npm (wird mit Node.js geliefert)
- Ein MCP-Server zum Testen (siehe [Modul 3.1 – Erster Server](../01-first-server/README.md))

## Installation

### Option 1: Mit npx ausführen (Empfohlen für schnelles Testen)

```bash
npx @modelcontextprotocol/inspector
```

### Option 2: Global installieren

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Option 3: Zum Projekt hinzufügen

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Zum `package.json` hinzufügen:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Verbindung zu Ihrem Server herstellen

### stdio Server (lokaler Prozess)

Für Server, die über Standard-Ein-/Ausgabe kommunizieren:

```bash
# Python-Server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js-Server
npx @modelcontextprotocol/inspector node ./build/index.js

# Mit Umgebungsvariablen
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP Server (Netzwerk)

Für als HTTP-Dienste laufende Server:

1. Starten Sie zuerst Ihren Server:
   ```bash
   python server.py  # Server läuft unter http://localhost:8080
   ```

2. Starten Sie Inspector und verbinden Sie sich:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Übersicht der Inspector-Benutzeroberfläche

Wenn Inspector startet, sehen Sie eine Web-Oberfläche (typischerweise unter `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Testen von Tools

### Verfügbare Tools auflisten

1. Klicken Sie auf den Tab **Tools**
2. Inspector ruft automatisch `tools/list` auf
3. Sie sehen alle registrierten Tools mit:
   - Toolname
   - Beschreibung
   - Eingabeschema (Parameter)

### Ein Tool aufrufen

1. Wählen Sie ein Tool aus der Liste
2. Füllen Sie die erforderlichen Parameter im Formular aus
3. Klicken Sie auf **Tool ausführen**
4. Sehen Sie sich die Antwort im Ergebnisbereich an

**Beispiel: Ein Kalkulator-Tool testen**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Tool-Fehler debuggen

Wenn ein Tool fehlschlägt, zeigt Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Häufige Fehlercodes:
| Code | Bedeutung |
|------|------------|
| -32700 | Parse-Fehler (ungültiges JSON) |
| -32600 | Ungültige Anfrage |
| -32601 | Methode nicht gefunden |
| -32602 | Ungültige Parameter |
| -32603 | Interner Fehler |

---

## Ressourcen testen

### Ressourcen auflisten

1. Klicken Sie auf den Tab **Resources**
2. Inspector ruft `resources/list` auf
3. Sie sehen:
   - Ressourcen-URIs
   - Namen und Beschreibungen
   - MIME-Typen

### Eine Ressource lesen

1. Wählen Sie eine Ressource aus
2. Klicken Sie auf **Ressource lesen**
3. Sehen Sie sich den zurückgegebenen Inhalt an

**Beispielausgabe:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Prompts testen

### Prompts auflisten

1. Klicken Sie auf den Tab **Prompts**
2. Inspector ruft `prompts/list` auf
3. Verfügbare Prompt-Vorlagen anzeigen

### Einen Prompt abrufen

1. Wählen Sie einen Prompt aus
2. Füllen Sie alle erforderlichen Argumente aus
3. Klicken Sie auf **Prompt abrufen**
4. Sehen Sie die gerenderten Prompt-Nachrichten

---

## Nachrichtenprotokoll-Analyse

Das Nachrichtenprotokoll zeigt alle MCP-Protokollnachrichten. Die folgende Transkription stammt von einem
Legacy-`2025-11-25` Server und beinhaltet den entfernten `initialize`-Handshake. Ein
`2026-07-28` Server verwendet selbstenthaltene Anfrage-Metadaten und `server/discover`
stattdessen.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Worauf achten

- **Anfrage-/Antwort-Paare**: Jede `→` sollte ein passendes `←` haben
- **Fehlermeldungen**: Achten Sie auf `"error"` in Antworten
- **Zeitliche Abstände**: Große Pausen können auf Leistungsprobleme hindeuten
- **Protokollversion**: Stellen Sie sicher, dass Server und Client dieselbe Version verwenden

---

## VS Code Integration

Sie können Inspector direkt aus VS Code ausführen:

### Verwendung von launch.json

Fügen Sie `.vscode/launch.json` hinzu:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Verwendung von Tasks

Fügen Sie `.vscode/tasks.json` hinzu:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Häufige Debugging-Szenarien

### Szenario 1: Server verbindet nicht

**Symptome:** Inspector zeigt „Getrennt“ oder hängt bei „Verbindung wird hergestellt...“

**Checkliste:**
1. ✅ Ist der Server-Befehl korrekt?
2. ✅ Sind alle Abhängigkeiten installiert?
3. ✅ Ist der Serverpfad absolut oder relativ zum aktuellen Verzeichnis?
4. ✅ Sind die erforderlichen Umgebungsvariablen gesetzt?

**Debug-Schritte:**
```bash
# Testen Sie den Server zuerst manuell
python -c "import your_server_module; print('OK')"

# Auf Importfehler prüfen
python -m your_server_module 2>&1 | head -20

# Überprüfen Sie, ob das MCP SDK installiert ist
pip show mcp
```

### Szenario 2: Tools erscheinen nicht

**Symptome:** Tools-Tab zeigt leere Liste

**Mögliche Ursachen:**
1. Tools wurden bei Serverinitialisierung nicht registriert
2. Server ist nach dem Start abgestürzt
3. `tools/list` Handler liefert leeres Array zurück

**Debug-Schritte:**
1. Überprüfen Sie das Nachrichtenprotokoll auf `tools/list` Antwort
2. Fügen Sie Logging zu Ihrem Tool-Registrierungscode hinzu
3. Vergewissern Sie sich, dass `@mcp.tool()` Dekoratoren vorhanden sind (Python)

### Szenario 3: Tool gibt Fehler zurück

**Symptome:** Tool-Aufruf gibt Fehlerantwort zurück

**Debug-Ansatz:**
1. Lesen Sie die Fehlermeldung sorgfältig
2. Überprüfen Sie, ob die Parametertypen dem Schema entsprechen
3. Fügen Sie try/catch mit detaillierten Fehlermeldungen hinzu
4. Überprüfen Sie Server-Logs auf Stacktraces

**Beispiel für verbesserte Fehlerbehandlung:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Werkzeuglogik hier
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Szenario 4: Ressourcendaten sind leer

**Symptome:** Ressource wird zurückgegeben, aber Inhalt ist leer oder null

**Checkliste:**
1. ✅ Datei- oder URI-Pfad ist korrekt
2. ✅ Server hat Leseberechtigung für die Ressource
3. ✅ Ressourcendaten werden korrekt zurückgegeben

---

## Erweiterte Inspector-Funktionen

### Benutzerdefinierte Header (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Ausführliches Logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Sitzungen aufzeichnen

Inspector kann Nachrichtenprotokolle für spätere Analysen exportieren:
1. Klicken Sie im Nachrichtenbereich auf **Protokoll exportieren**
2. Speichern Sie die JSON-Datei
3. Teilen Sie sie mit Teammitgliedern zum Debuggen

---

## Best Practices

1. **Früh und oft testen** – Verwenden Sie Inspector während der Entwicklung, nicht nur wenn Probleme auftreten
2. **Einfach anfangen** – Testen Sie zuerst die Basisverbindung, bevor Sie komplexe Tool-Aufrufe testen
3. **Schema überprüfen** – Viele Fehler entstehen durch Parameter-Typen, die nicht übereinstimmen
4. **Fehlermeldungen lesen** – MCP-Fehler sind meist aussagekräftig
5. **Inspector offen halten** – Er hilft, Probleme während der Entwicklung zu erkennen

---

## Wie geht es weiter

Sie haben Modul 3: Erste Schritte abgeschlossen! Setzen Sie Ihr Lernen fort:

- [Modul 4: Praktische Umsetzung](../../04-PracticalImplementation/README.md)

---

## Zusätzliche Ressourcen

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Spezifikation – Protokollnachrichten](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Spezifikation](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
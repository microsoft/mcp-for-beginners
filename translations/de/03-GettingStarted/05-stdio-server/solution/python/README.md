# MCP stdio Server - Python-Lösung

> **⚠️ Wichtig**: Diese Lösung wurde aktualisiert, um den **stdio-Transport** gemäß der MCP-Spezifikation vom 18.06.2025 zu verwenden. Der ursprüngliche SSE-Transport wurde veraltet.

## Überblick

Diese Python-Lösung zeigt, wie man einen MCP-Server mit dem aktuellen stdio-Transport erstellt. Der stdio-Transport ist einfacher, sicherer und bietet eine bessere Leistung als der veraltete SSE-Ansatz.

## Voraussetzungen

- Python 3.8 oder höher
- Es wird empfohlen, `uv` für das Paketmanagement zu installieren. Siehe [Anleitung](https://docs.astral.sh/uv/#highlights)

## Installationsanleitung

### Schritt 1: Erstellen Sie eine virtuelle Umgebung

```bash
python -m venv venv
```

### Schritt 2: Aktivieren Sie die virtuelle Umgebung

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Schritt 3: Installieren Sie die Abhängigkeiten

```bash
pip install mcp
```

## Server starten

Der stdio-Server funktioniert anders als der alte SSE-Server. Anstatt einen Webserver zu starten, kommuniziert er über stdin/stdout:

```bash
python server.py
```

**Wichtig**: Der Server scheint zu hängen – das ist normal! Er wartet auf JSON-RPC-Nachrichten über stdin.

## Server testen

### Methode 1: Mit dem MCP Inspector (Empfohlen)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Dies wird:
1. Ihren Server als Unterprozess starten
2. Eine Weboberfläche zum Testen öffnen
3. Ihnen ermöglichen, alle Server-Tools interaktiv zu testen

### Methode 2: Direkte JSON-RPC-Tests

Sie können auch testen, indem Sie JSON-RPC-Nachrichten direkt senden:

1. Starten Sie den Server: `python server.py`
2. Senden Sie eine JSON-RPC-Nachricht (Beispiel):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Der Server antwortet mit verfügbaren Tools

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
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Wichtige Unterschiede zu SSE

**stdio-Transport (Aktuell):**
- ✅ Einfachere Einrichtung – kein Webserver erforderlich
- ✅ Bessere Sicherheit – keine HTTP-Endpunkte
- ✅ Kommunikation über Unterprozesse
- ✅ JSON-RPC über stdin/stdout
- ✅ Höhere Leistung

**SSE-Transport (Veraltet):**
- ❌ Erforderte Einrichtung eines HTTP-Servers
- ❌ Benötigte ein Web-Framework (Starlette/FastAPI)
- ❌ Komplexeres Routing und Sitzungsmanagement
- ❌ Zusätzliche Sicherheitsüberlegungen
- ❌ Seit MCP 2025-06-18 veraltet

## Tipps zur Fehlerbehebung

- Verwenden Sie `stderr` für das Logging (niemals `stdout`)
- Testen Sie mit dem Inspector für visuelles Debugging
- Stellen Sie sicher, dass alle JSON-Nachrichten zeilenweise getrennt sind
- Überprüfen Sie, ob der Server fehlerfrei startet

Diese Lösung folgt der aktuellen MCP-Spezifikation und zeigt Best Practices für die Implementierung des stdio-Transports.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
# Beispiel ausführen

Dieses Beispiel startet einen MCP-Server mit einer Middleware, die überprüft, ob ein gültiger Authorization-Header vorhanden ist.

## Abhängigkeiten installieren

```bash
pip install "mcp[cli]" 
```

## Server starten

```bash
python server.py
```

Starte den Client in einem anderen Terminal

```bash
python client.py
```

Du solltest ein Ergebnis sehen, das ähnlich aussieht wie:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Das bedeutet, dass die übermittelte Berechtigung akzeptiert wurde.

Versuche, die Berechtigung in `client.py` auf "secret-token2" zu ändern. Dann solltest du diesen Text als Teil der Antwort sehen:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Das bedeutet, dass du authentifiziert wurdest (du hattest eine Berechtigung), aber sie war ungültig.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
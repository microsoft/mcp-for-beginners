# Beispiel ausführen

## Umgebung erstellen

```sh
python -m venv venv
source ./venv/bin/activate
```

## Abhängigkeiten installieren

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Token generieren

Sie müssen einen Token generieren, den der Client verwendet, um mit dem Server zu kommunizieren.

Aufruf:

```sh
python util.py
```

## Code ausführen

Führen Sie den Code aus mit:

```sh
python server.py
```

In einem separaten Terminal geben Sie ein:

```sh
python client.py
```

Im Server-Terminal sollten Sie etwas Ähnliches sehen wie:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Im Client-Fenster sollten Sie einen Text sehen, der ähnlich aussieht wie:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Das bedeutet, dass alles funktioniert.

### Ändern Sie die Informationen, um einen Fehler zu provozieren

Suchen Sie diesen Code in *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Ändern Sie ihn so, dass er "User.Write" sagt. Ihr aktueller Token hat nicht diese Berechtigungsstufe, daher sollten Sie, wenn Sie den Server neu starten und versuchen, den Client erneut auszuführen, einen Fehler ähnlich dem folgenden im Server-Terminal sehen:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Sie können entweder Ihren Server-Code zurückändern oder einen neuen Token generieren, der diesen zusätzlichen Bereich enthält – ganz wie Sie möchten.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
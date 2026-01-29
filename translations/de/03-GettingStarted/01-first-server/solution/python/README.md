# Ausführen dieses Beispiels

Es wird empfohlen, `uv` zu installieren, aber es ist nicht zwingend erforderlich. Siehe [Anleitung](https://docs.astral.sh/uv/#highlights).

## -0- Erstellen Sie eine virtuelle Umgebung

```bash
python -m venv venv
```

## -1- Aktivieren Sie die virtuelle Umgebung

```bash
venv\Scripts\activate
```

## -2- Installieren Sie die Abhängigkeiten

```bash
pip install "mcp[cli]"
```

## -3- Führen Sie das Beispiel aus

```bash
mcp run server.py
```

## -4- Testen Sie das Beispiel

Während der Server in einem Terminal läuft, öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus:

```bash
mcp dev server.py
```

Dies sollte einen Webserver mit einer visuellen Oberfläche starten, die es Ihnen ermöglicht, das Beispiel zu testen.

Sobald der Server verbunden ist:

- Versuchen Sie, Werkzeuge aufzulisten und führen Sie `add` aus, mit den Argumenten 2 und 4. Sie sollten 6 als Ergebnis sehen.

- Gehen Sie zu Ressourcen und Ressourcenvorlage und rufen Sie `get_greeting` auf. Geben Sie einen Namen ein, und Sie sollten eine Begrüßung mit dem eingegebenen Namen sehen.

### Testen im CLI-Modus

Der von Ihnen gestartete Inspector ist tatsächlich eine Node.js-Anwendung, und `mcp dev` ist ein Wrapper dafür.

Sie können ihn direkt im CLI-Modus starten, indem Sie den folgenden Befehl ausführen:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Dies wird alle verfügbaren Werkzeuge auf dem Server auflisten. Sie sollten die folgende Ausgabe sehen:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Um ein Werkzeug aufzurufen, geben Sie Folgendes ein:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Sie sollten die folgende Ausgabe sehen:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Es ist in der Regel viel schneller, den Inspector im CLI-Modus auszuführen als im Browser.
> Lesen Sie mehr über den Inspector [hier](https://github.com/modelcontextprotocol/inspector).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
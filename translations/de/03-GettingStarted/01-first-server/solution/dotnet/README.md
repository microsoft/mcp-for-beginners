# Ausführen dieses Beispiels

## -1- Installieren Sie die Abhängigkeiten

```bash
dotnet restore
```

## -3- Beispiel ausführen

```bash
dotnet run
```

## -4- Beispiel testen

Mit dem Server, der in einem Terminal läuft, öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dies sollte einen Webserver mit einer visuellen Oberfläche starten, die es Ihnen ermöglicht, das Beispiel zu testen.

Sobald der Server verbunden ist:

- Versuchen Sie, Werkzeuge aufzulisten und führen Sie `add` aus, mit den Argumenten 2 und 4. Sie sollten 6 als Ergebnis sehen.
- Gehen Sie zu Ressourcen und Ressourcenvorlage und rufen Sie "greeting" auf. Geben Sie einen Namen ein, und Sie sollten eine Begrüßung mit dem von Ihnen angegebenen Namen sehen.

### Testen im CLI-Modus

Sie können es direkt im CLI-Modus starten, indem Sie den folgenden Befehl ausführen:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Dies wird alle verfügbaren Werkzeuge im Server auflisten. Sie sollten die folgende Ausgabe sehen:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Um ein Werkzeug aufzurufen, geben Sie Folgendes ein:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Sie sollten die folgende Ausgabe sehen:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Es ist normalerweise viel schneller, den Inspector im CLI-Modus auszuführen als im Browser.
> Lesen Sie mehr über den Inspector [hier](https://github.com/modelcontextprotocol/inspector).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
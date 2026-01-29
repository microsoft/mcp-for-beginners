# Ausführen dieses Beispiels

Es wird empfohlen, `uv` zu installieren, aber es ist nicht zwingend erforderlich. Siehe [Anleitung](https://docs.astral.sh/uv/#highlights).

## -1- Abhängigkeiten installieren

```bash
npm install
```

## -3- Beispiel ausführen

```bash
npm run build
```

## -4- Beispiel testen

Während der Server in einem Terminal läuft, öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus:

```bash
npm run inspector
```

Dies sollte einen Webserver mit einer visuellen Oberfläche starten, die es Ihnen ermöglicht, das Beispiel zu testen.

Sobald der Server verbunden ist:

- Versuchen Sie, Werkzeuge aufzulisten und führen Sie `add` aus, mit den Argumenten 2 und 4. Sie sollten 6 als Ergebnis sehen.
- Gehen Sie zu Ressourcen und Ressourcenvorlagen und rufen Sie "greeting" auf. Geben Sie einen Namen ein, und Sie sollten eine Begrüßung mit dem von Ihnen angegebenen Namen sehen.

### Testen im CLI-Modus

Der von Ihnen gestartete Inspector ist tatsächlich eine Node.js-Anwendung, und `mcp dev` ist ein Wrapper dafür.

Sie können ihn direkt im CLI-Modus starten, indem Sie den folgenden Befehl ausführen:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Dies wird alle im Server verfügbaren Werkzeuge auflisten. Sie sollten die folgende Ausgabe sehen:

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
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> Es ist normalerweise viel schneller, den Inspector im CLI-Modus auszuführen als im Browser.
> Lesen Sie mehr über den Inspector [hier](https://github.com/modelcontextprotocol/inspector).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
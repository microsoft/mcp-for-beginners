# Ausführen des Beispiels

Hier gehen wir davon aus, dass Sie bereits einen funktionierenden Servercode haben. Bitte suchen Sie einen Server aus einem der vorherigen Kapitel.

## Einrichten von mcp.json

Hier ist eine Datei, die Sie als Referenz verwenden, [mcp.json](../../../../../03-GettingStarted/04-vscode/solution/mcp.json).

Ändern Sie den Server-Eintrag nach Bedarf, um den absoluten Pfad zu Ihrem Server einschließlich des vollständigen Befehls zum Ausführen anzugeben.

In der oben genannten Beispieldatei sieht der Server-Eintrag wie folgt aus:

<details>
<summary>node.js</summary>
```json
"hello-mcp": {
    "command": "node",
    "args": [
        "build/index.js"
    ]
}
```
</details>

<details>
<summary>.NET</summary>

Möglicherweise müssen Sie das Root-Verzeichnis des GitHub-Repositories angeben, das mit dem Befehl `git rev-parse --show-toplevel` ermittelt werden kann.

```jsonc
{
  "inputs": [
    {
      "type": "promptString",
      "id": "repository-root",
      "description": "The absolute path to the repository root"
    }
  ],
  "servers": {
    "calculator-mcp-dotnet": {
      "type": "stdio",
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "${input:repository-root}/03-GettingStarted/02-client/solution/server/server.csproj"
      ]
    }
  }
}
```

</details>

Dies entspricht dem Ausführen eines Befehls wie: `node build/index.js`.

- Ändern Sie diesen Server-Eintrag so, dass er dem Speicherort Ihrer Serverdatei entspricht oder dem, was zum Starten Ihres Servers je nach gewählter Laufzeitumgebung und Serverstandort erforderlich ist.

## Verwenden Sie die Funktionen auf dem Server

- Klicken Sie auf das `play`-Symbol, sobald Sie *mcp.json* zum Ordner *./vscode* hinzugefügt haben,

    Beobachten Sie, wie sich das Symbol für die Werkzeuge ändert, um die Anzahl der verfügbaren Werkzeuge zu erhöhen. Das Werkzeug-Symbol befindet sich direkt über dem Chat-Feld in GitHub Copilot.

## Führen Sie ein Werkzeug aus

- Geben Sie eine Eingabeaufforderung in Ihr Chatfenster ein, die der Beschreibung Ihres Werkzeugs entspricht. Zum Beispiel, um das Werkzeug `add` auszulösen, geben Sie etwas wie "add 3 to 20" ein.

    Sie sollten ein Werkzeug über dem Chat-Textfeld angezeigt bekommen, das Ihnen anzeigt, dass Sie das Werkzeug zur Ausführung auswählen können, wie in dieser Darstellung:

    ![VS Code zeigt an, dass es ein Werkzeug ausführen möchte](../../../../../translated_images/de/vscode-agent.d5a0e0b897331060.webp)

    Die Auswahl des Werkzeugs sollte ein numerisches Ergebnis anzeigen mit dem Wert "23", wenn Ihre Eingabeaufforderung wie oben beschrieben war.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
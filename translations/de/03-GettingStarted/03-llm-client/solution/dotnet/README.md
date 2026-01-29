# Dieses Beispiel ausführen

> [!NOTE]
> Dieses Beispiel geht davon aus, dass du eine GitHub Codespaces-Instanz verwendest. Wenn du es lokal ausführen möchtest, musst du ein persönliches Zugriffstoken (PAT) auf GitHub einrichten.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## Bibliotheken installieren

```sh
dotnet restore
```

Sollte die folgenden Bibliotheken installieren: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Ausführen

```sh 
dotnet run
```

Du solltest eine Ausgabe ähnlich der folgenden sehen:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Ein Großteil der Ausgabe dient nur der Fehlerbehebung, aber wichtig ist, dass du Werkzeuge vom MCP Server auflistest, diese in LLM-Werkzeuge umwandelst und am Ende eine MCP-Client-Antwort „Sum 6“ erhältst.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
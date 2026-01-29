# Ausführen dieses Beispiels

Dieses Beispiel erfordert, dass ein LLM auf dem Client läuft. Das LLM benötigt, dass du entweder dies in Codespaces ausführst oder ein persönliches Zugriffstoken in GitHub einrichtest, damit es funktioniert.

## -1- Installiere die Abhängigkeiten

```bash
npm install
```

## -3- Starte den Server

```bash
npm run build
```

## -4- Starte den Client

```sh
npm run client
```

Du solltest ein Ergebnis ähnlich dem Folgenden sehen:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
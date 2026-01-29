# Beispiel ausführen

## Abhängigkeiten installieren

```sh
npm install
```

## Build

```sh
npm run build
```

## Tokens generieren

```sh
npm run generate
```

Dies erstellt einen Token in einer Datei *.env*. Der Client wird diesen Token aus der Datei lesen.

## Code ausführen

Starte den Server mit:

```sh
npm start
```

Führe den Client in einem separaten Terminal aus mit:

```sh
npm run client
```

Im Terminal des Servers solltest du eine Ausgabe sehen, die ähnlich aussieht wie:

```text
User exists
User has required scopes
Middleware executed
```

und im Terminal des Clients solltest du eine Ausgabe sehen, die ähnlich aussieht wie:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Änderungen vornehmen

Lass uns sicherstellen, dass wir die Scopes verstehen. Öffne die Datei *server.ts* und finde diesen Code:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Das bedeutet, dass der übergebene Token "User.Read" enthalten muss. Ändern wir das zu "User.Write". Führe nun `npm run build` aus und starte den Server neu mit `npm start`. Du solltest jetzt sehen, dass die Authentifizierung fehlschlägt, da wir diesen Scope nicht haben (wir haben User.Read und Admin.Write):

Der Client zeigt jetzt an:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

und im Terminal des Servers kannst du sehen, dass es sagt:

```text
User exists
```

und dass es nicht über diesen Punkt hinausgeht.

Entweder füge diesen Scope "User.Write" hinzu, führe `npm run generate` aus und starte den Client erneut, ODER ändere den Servercode zurück.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
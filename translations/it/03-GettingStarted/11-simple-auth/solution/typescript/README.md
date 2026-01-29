# Esegui esempio

## Installa dipendenze

```sh
npm install
```

## Compila

```sh
npm run build
```

## Genera token

```sh
npm run generate
```

Questo crea un token in un file *.env*. Il client leggerà da questo file.

## Esegui il codice

Avvia il server con:

```sh
npm start
```

Esegui il client, in un terminale separato, con:

```sh
npm run client
```

Nel terminale del server, dovresti vedere un output simile a:

```text
User exists
User has required scopes
Middleware executed
```

e nel terminale del client, dovresti vedere un output simile a:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Modificare le cose

Assicuriamoci di comprendere gli ambiti. Trova il file *server.ts* e questo codice:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Questo indica che il token passato deve avere "User.Read". Cambiamolo in "User.Write". Ora esegui `npm run build` e riavvia il server con `npm start`. Dovresti ora vedere che l'autenticazione fallisce poiché non abbiamo questo ambito (abbiamo User.Read e Admin.Write):

Il client ora dice

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

e puoi vedere nel terminale del server che dice:

```text
User exists
```

e che non va oltre questo punto.

Puoi aggiungere questo ambito "User.Write", eseguire `npm run generate` e rieseguire il client OPPURE modificare nuovamente il codice del server.

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
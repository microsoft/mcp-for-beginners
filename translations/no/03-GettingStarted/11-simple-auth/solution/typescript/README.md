# Kjør eksempel

## Installer avhengigheter

```sh
npm install
```

## Bygg

```sh
npm run build
```

## Generer tokens

```sh
npm run generate
```

Dette oppretter en token i en fil som heter *.env*. Klienten vil lese fra denne filen.

## Kjør kode

Start serveren med:

```sh
npm start
```

Kjør klienten i et separat terminalvindu med:

```sh
npm run client
```

I serverens terminal bør du se en utdata som ligner på:

```text
User exists
User has required scopes
Middleware executed
```

og i klientens terminal bør du se en utdata som ligner på:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Endre ting

La oss sørge for at vi forstår omfangene. Finn filen *server.ts* og denne koden:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Dette sier at den sendte tokenen må ha "User.Read". La oss endre det til "User.Write". Kjør nå `npm run build` og start serveren på nytt med `npm start`. Du bør nå se at autentiseringen feiler fordi vi ikke har dette omfanget (vi har User.Read og Admin.Write):

Klienten sier nå

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

og du kan se i serverens terminal at den sier:

```text
User exists
```

og at den ikke går videre fra dette punktet.

Enten legg til dette omfanget "User.Write", kjør `npm run generate` og kjør klienten på nytt ELLER endre serverkoden tilbake.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
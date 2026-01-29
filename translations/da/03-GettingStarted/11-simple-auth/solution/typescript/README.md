# Kør eksempel

## Installer afhængigheder

```sh
npm install
```

## Byg

```sh
npm run build
```

## Generer tokens

```sh
npm run generate
```

Dette opretter en token i en fil *.env*. Klienten vil læse fra denne fil.

## Kør kode

Start serveren med:

```sh
npm start
```

Kør klienten i en separat terminal med:

```sh
npm run client
```

I serverens terminal bør du se en output, der ligner:

```text
User exists
User has required scopes
Middleware executed
```

og fra klientens terminal bør du se en output, der ligner:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Ændringer

Lad os sikre, at vi forstår scopes. Find filen *server.ts* og denne kode:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Dette angiver, at den overførte token skal have "User.Read". Lad os ændre det til "User.Write". Kør nu `npm run build` og genstart serveren med `npm start`. Du bør nu se, at godkendelsen fejler, da vi ikke har dette scope (vi har User.Read og Admin.Write):

Klienten siger nu

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

og du kan se i serverens terminal, at den siger:

```text
User exists
```

og at den ikke går videre herfra.

Enten tilføj dette scope "User.Write" og kør `npm run generate` og kør klienten igen, ELLER ændr serverkoden tilbage.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
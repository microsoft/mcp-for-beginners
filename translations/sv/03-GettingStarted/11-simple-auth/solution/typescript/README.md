# Kör exempel

## Installera beroenden

```sh
npm install
```

## Bygg

```sh
npm run build
```

## Generera tokens

```sh
npm run generate
```

Detta skapar en token i en fil *.env*. Klienten kommer att läsa från denna fil.

## Kör kod

Starta servern med:

```sh
npm start
```

Kör klienten i en separat terminal med:

```sh
npm run client
```

I serverns terminal bör du se en output som liknar:

```text
User exists
User has required scopes
Middleware executed
```

och från klientens terminal bör du se en output som liknar:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Ändra saker

Låt oss säkerställa att vi förstår scopes. Hitta filen *server.ts* och denna kod:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Detta säger att den skickade tokenen behöver ha "User.Read", låt oss ändra det till "User.Write". Kör nu `npm run build` och starta om servern med `npm start`. Du bör nu se att autentiseringen misslyckas eftersom vi inte har detta scope (vi har User.Read och Admin.Write):

Klienten säger nu

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

och du kan se i serverns terminal att den säger:

```text
User exists
```

och att den inte går vidare från denna punkt.

Antingen lägg till detta scope "User.Write" och kör `npm run generate` och kör om klienten ELLER ändra tillbaka serverkoden.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
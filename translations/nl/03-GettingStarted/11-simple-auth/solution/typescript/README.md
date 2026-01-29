# Voorbeeld uitvoeren

## Installeer afhankelijkheden

```sh
npm install
```

## Bouwen

```sh
npm run build
```

## Tokens genereren

```sh
npm run generate
```

Dit maakt een token aan in een bestand *.env*. De client zal dit bestand uitlezen.

## Code uitvoeren

Start de server met:

```sh
npm start
```

Start de client in een aparte terminal met:

```sh
npm run client
```

In de terminal van de server zou je een output moeten zien die lijkt op:

```text
User exists
User has required scopes
Middleware executed
```

en in de terminal van de client zou je een output moeten zien die lijkt op:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Dingen aanpassen

Laten we ervoor zorgen dat we de scopes begrijpen. Zoek het bestand *server.ts* en deze code:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Dit geeft aan dat het doorgegeven token "User.Read" moet bevatten. Laten we dat veranderen naar "User.Write". Voer nu `npm run build` uit en herstart de server met `npm start`. Je zou nu moeten zien dat de authenticatie faalt omdat we deze scope niet hebben (we hebben User.Read en Admin.Write):

De client geeft nu het volgende aan:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

en in de terminal van de server kun je zien dat het aangeeft:

```text
User exists
```

en dat het niet verder gaat vanaf dit punt.

Voeg deze scope "User.Write" toe en voer `npm run generate` uit en start de client opnieuw OF verander de servercode terug.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
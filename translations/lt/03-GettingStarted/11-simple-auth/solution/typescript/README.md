# Paleiskite pavyzdį

## Įdiekite priklausomybes

```sh
npm install
```

## Sukurkite

```sh
npm run build
```

## Sukurkite žetonus

```sh
npm run generate
```

Tai sukuria žetoną faile *.env*. Klientas skaitys iš šio failo.

## Paleiskite kodą

Paleiskite serverį su:

```sh
npm start
```

Paleiskite klientą atskirame terminale su:

```sh
npm run client
```

Serverio terminale turėtumėte matyti išvestį, panašią į:

```text
User exists
User has required scopes
Middleware executed
```

o kliento terminale turėtumėte matyti išvestį, panašią į:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Keiskime dalykus

Įsitikinkime, kad suprantame sritis. Suraskite failą *server.ts* ir šį kodą:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Tai nurodo, kad perduodamas žetonas turi turėti "User.Read". Pakeiskime tai į "User.Write". Dabar paleiskite `npm run build` ir iš naujo paleiskite serverį su `npm start`. Dabar turėtumėte matyti, kad autentifikacija nepavyksta, nes neturime šios srities (turime User.Read ir Admin.Write):

Dabar klientas sako

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ir serverio terminale galite matyti, kad jis sako:

```text
User exists
```

ir kad jis neperžengia šio taško.

Galite arba pridėti šią sritį "User.Write", paleisti `npm run generate` ir iš naujo paleisti klientą, ARBA grąžinti serverio kodą į ankstesnę būseną.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
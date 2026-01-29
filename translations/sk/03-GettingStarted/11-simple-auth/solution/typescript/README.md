# Spustenie ukážky

## Inštalácia závislostí

```sh
npm install
```

## Zostavenie

```sh
npm run build
```

## Generovanie tokenov

```sh
npm run generate
```

Týmto sa vytvorí token v súbore *.env*. Klient bude čítať z tohto súboru.

## Spustenie kódu

Spustite server pomocou:

```sh
npm start
```

Spustite klienta v samostatnom termináli pomocou:

```sh
npm run client
```

V termináli servera by ste mali vidieť výstup podobný:

```text
User exists
User has required scopes
Middleware executed
```

a v termináli klienta by ste mali vidieť výstup podobný:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Zmeny

Poďme sa uistiť, že rozumieme rozsahom. Nájdite súbor *server.ts* a tento kód:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Toto hovorí, že odovzdaný token musí mať "User.Read". Zmeňme to na "User.Write". Teraz spustite `npm run build` a reštartujte server pomocou `npm start`. Teraz by ste mali vidieť, že autentifikácia zlyhala, pretože nemáme tento rozsah (máme User.Read a Admin.Write):

Klient teraz hovorí

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

a v termináli servera môžete vidieť, že hovorí:

```text
User exists
```

a že sa nedostane ďalej.

Buď pridajte tento rozsah "User.Write" a spustite `npm run generate` a znovu spustite klienta, ALEBO zmeňte kód servera späť.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
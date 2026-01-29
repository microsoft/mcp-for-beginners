# Spuštění ukázky

## Instalace závislostí

```sh
npm install
```

## Sestavení

```sh
npm run build
```

## Generování tokenů

```sh
npm run generate
```

Tím se vytvoří token v souboru *.env*. Klient bude číst z tohoto souboru.

## Spuštění kódu

Spusťte server pomocí:

```sh
npm start
```

Spusťte klienta v samostatném terminálu pomocí:

```sh
npm run client
```

V terminálu serveru byste měli vidět výstup podobný:

```text
User exists
User has required scopes
Middleware executed
```

a v terminálu klienta byste měli vidět výstup podobný:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Změna nastavení

Pojďme se ujistit, že rozumíme rozsahům. Najděte soubor *server.ts* a tento kód:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Toto říká, že předaný token musí mít "User.Read". Změňme to na "User.Write". Nyní spusťte `npm run build` a restartujte server pomocí `npm start`. Nyní byste měli vidět, že ověření selhalo, protože nemáme tento rozsah (máme User.Read a Admin.Write):

Klient nyní říká

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

a v terminálu serveru můžete vidět, že říká:

```text
User exists
```

a že se nedostane dál.

Buď přidejte tento rozsah "User.Write" a spusťte `npm run generate` a znovu spusťte klienta, NEBO změňte kód serveru zpět.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
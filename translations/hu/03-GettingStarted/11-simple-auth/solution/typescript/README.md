# Példa futtatása

## Függőségek telepítése

```sh
npm install
```

## Build

```sh
npm run build
```

## Tokenek generálása

```sh
npm run generate
```

Ez létrehoz egy tokent egy *.env* fájlban. Az ügyfél ebből a fájlból fog olvasni.

## Kód futtatása

Indítsd el a szervert ezzel:

```sh
npm start
```

Futtasd az ügyfelet egy külön terminálban ezzel:

```sh
npm run client
```

A szerver termináljában hasonló kimenetet kell látnod:

```text
User exists
User has required scopes
Middleware executed
```

és az ügyfél termináljában hasonló kimenetet kell látnod:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Módosítások

Győződjünk meg arról, hogy értjük a jogosultságokat. Keresd meg a *server.ts* fájlt és ezt a kódot:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Ez azt mondja, hogy a megadott tokennek "User.Read" jogosultsággal kell rendelkeznie. Változtassuk ezt "User.Write"-ra. Most futtasd a `npm run build` parancsot, és indítsd újra a szervert `npm start`. Most azt kell látnod, hogy az autentikáció sikertelen, mivel nincs ilyen jogosultságunk (csak User.Read és Admin.Write van):

Az ügyfél most ezt mondja:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

és láthatod a szerver termináljában, hogy ezt mondja:

```text
User exists
```

és nem halad tovább ezen a ponton.

Vagy add hozzá ezt a jogosultságot: "User.Write", futtasd a `npm run generate` parancsot, és futtasd újra az ügyfelet, VAGY állítsd vissza a szerver kódját.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
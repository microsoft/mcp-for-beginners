# Pokreni primjer

## Instaliraj ovisnosti

```sh
npm install
```

## Izgradi

```sh
npm run build
```

## Generiraj tokene

```sh
npm run generate
```

Ovo stvara token u datoteci *.env*. Klijent će čitati iz ove datoteke.

## Pokreni kod

Pokreni server s:

```sh
npm start
```

Pokreni klijent u zasebnom terminalu s:

```sh
npm run client
```

U terminalu servera trebali biste vidjeti izlaz sličan:

```text
User exists
User has required scopes
Middleware executed
```

a u terminalu klijenta trebali biste vidjeti izlaz sličan:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Promjena stvari

Provjerimo da razumijemo opsege. Pronađite datoteku *server.ts* i ovaj kod:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Ovo kaže da proslijeđeni token mora imati "User.Read", promijenimo to u "User.Write". Sada pokrenite `npm run build` i ponovno pokrenite server s `npm start`. Sada biste trebali vidjeti da autentifikacija ne uspijeva jer nemamo taj opseg (imamo User.Read i Admin.Write):

Klijent sada kaže

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

a u terminalu servera možete vidjeti da kaže:

```text
User exists
```

i da ne ide dalje od ove točke.

Ili dodajte ovaj opseg "User.Write" i pokrenite `npm run generate` te ponovno pokrenite klijent, ILI vratite kod servera na prethodno stanje.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
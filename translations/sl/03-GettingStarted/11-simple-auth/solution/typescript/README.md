# Zagon vzorca

## Namestitev odvisnosti

```sh
npm install
```

## Gradnja

```sh
npm run build
```

## Generiranje žetonov

```sh
npm run generate
```

To ustvari žeton v datoteki *.env*. Odjemalec bo prebral iz te datoteke.

## Zagon kode

Zaženite strežnik z:

```sh
npm start
```

Zaženite odjemalca v ločenem terminalu z:

```sh
npm run client
```

V terminalu strežnika bi morali videti izpis, podoben temu:

```text
User exists
User has required scopes
Middleware executed
```

in v terminalu odjemalca bi morali videti izpis, podoben temu:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Spreminjanje stvari

Poskrbimo, da razumemo obseg. Poiščite datoteko *server.ts* in ta del kode:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

To pomeni, da mora posredovani žeton imeti "User.Read". Spremenimo to v "User.Write". Zdaj zaženite `npm run build` in ponovno zaženite strežnik z `npm start`. Zdaj bi morali videti, da avtentikacija ne uspe, saj nimamo tega obsega (imamo User.Read in Admin.Write):

Odjemalec zdaj pravi

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

in v terminalu strežnika lahko vidite, da pravi:

```text
User exists
```

in da ne gre naprej od te točke.

Dodajte ta obseg "User.Write" in zaženite `npm run generate` ter ponovno zaženite odjemalca ALI spremenite kodo strežnika nazaj.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
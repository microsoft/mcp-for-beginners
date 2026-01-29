# Käivita näidis

## Paigalda sõltuvused

```sh
npm install
```

## Ehita

```sh
npm run build
```

## Loo tokenid

```sh
npm run generate
```

See loob tokeni faili *.env*. Klient loeb sellest failist.

## Käivita kood

Käivita server:

```sh
npm start
```

Käivita klient eraldi terminalis:

```sh
npm run client
```

Serveri terminalis peaksid nägema väljundit, mis on sarnane:

```text
User exists
User has required scopes
Middleware executed
```

ja kliendi terminalis peaksid nägema väljundit, mis on sarnane:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Muudatuste tegemine

Veendume, et mõistame ulatusi. Leia fail *server.ts* ja järgmine kood:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

See ütleb, et edastatud tokenil peab olema "User.Read". Muudame selle "User.Write"-ks. Nüüd käivita `npm run build` ja taaskäivita server `npm start`. Nüüd peaksid nägema, et autentimine ebaõnnestub, kuna meil pole seda ulatust (meil on User.Read ja Admin.Write):

Klient ütleb nüüd

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ja serveri terminalis näed, et see ütleb:

```text
User exists
```

ja et see ei lähe sellest punktist edasi.

Lisa kas ulatus "User.Write" ja käivita `npm run generate` ning käivita klient uuesti VÕI muuda serveri kood tagasi.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
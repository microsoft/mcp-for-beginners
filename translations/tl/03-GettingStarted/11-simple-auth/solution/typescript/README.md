# Patakbuhin ang halimbawa

## I-install ang mga kinakailangan

```sh
npm install
```

## Bumuo

```sh
npm run build
```

## Gumawa ng mga token

```sh
npm run generate
```

Ito ay lilikha ng token sa isang file na *.env*. Babasahin ng client ang file na ito.

## Patakbuhin ang code

Simulan ang server gamit ang:

```sh
npm start
```

Patakbuhin ang client, sa isang hiwalay na terminal gamit ang:

```sh
npm run client
```

Sa terminal ng server, dapat mong makita ang output na katulad ng:

```text
User exists
User has required scopes
Middleware executed
```

at sa terminal ng client, dapat mong makita ang output na katulad ng:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Pagbabago ng mga bagay

Tiyakin natin na nauunawaan ang mga scope. Hanapin ang file na *server.ts* at ang code na ito:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Sinasabi nito na ang ipinasa na token ay kailangang magkaroon ng "User.Read", baguhin natin ito sa "User.Write". Ngayon patakbuhin ang `npm run build` at i-restart ang server gamit ang `npm start`. Dapat mong makita na nabigo ang authentication dahil wala tayong scope na ito (meron tayong User.Read at Admin.Write):

Ang client ngayon ay nagsasabi ng

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

at makikita mo sa terminal ng server na sinasabi nito:

```text
User exists
```

at hindi ito lumalampas sa puntong ito.

Maaaring idagdag ang scope na "User.Write" at patakbuhin ang `npm run generate` at muling patakbuhin ang client O ibalik ang code ng server sa dati.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
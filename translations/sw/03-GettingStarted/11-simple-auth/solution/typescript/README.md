# Endesha mfano

## Sakinisha utegemezi

```sh
npm install
```

## Jenga

```sh
npm run build
```

## Tengeneza tokeni

```sh
npm run generate
```

Hii inatengeneza tokeni kwenye faili *.env*. Mteja atasoma kutoka faili hii.

## Endesha msimbo

Anzisha seva kwa:

```sh
npm start
```

Endesha mteja, kwenye terminal tofauti kwa:

```sh
npm run client
```

Kwenye terminal ya seva, unapaswa kuona matokeo yanayofanana na:

```text
User exists
User has required scopes
Middleware executed
```

na kutoka kwenye terminal ya mteja, unapaswa kuona matokeo yanayofanana na:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Kubadilisha mambo

Hebu tuhakikishe tunaelewa mawanda. Tafuta faili *server.ts* na msimbo huu:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Hii inasema tokeni iliyopitishwa inahitaji kuwa na "User.Read", hebu tubadilishe hiyo kuwa "User.Write". Sasa endesha `npm run build` na anzisha tena seva kwa `npm start`. Sasa unapaswa kuona uthibitisho ukishindwa kwa sababu hatuna mawanda haya (tunayo User.Read na Admin.Write):

Mteja sasa unasema

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

na unaweza kuona kwenye terminal ya seva kwamba inasema:

```text
User exists
```

na kwamba haifiki hatua inayofuata.

Ama ongeza mawanda haya "User.Write" na endesha `npm run generate` na endesha tena mteja AU badilisha msimbo wa seva kurudi kama ulivyokuwa.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
# Suorita esimerkki

## Asenna riippuvuudet

```sh
npm install
```

## Käännä

```sh
npm run build
```

## Luo tokenit

```sh
npm run generate
```

Tämä luo tokenin tiedostoon *.env*. Asiakas lukee tämän tiedoston.

## Suorita koodi

Käynnistä palvelin komennolla:

```sh
npm start
```

Suorita asiakas erillisessä terminaalissa komennolla:

```sh
npm run client
```

Palvelimen terminaalissa pitäisi näkyä jotain tämän kaltaista:

```text
User exists
User has required scopes
Middleware executed
```

ja asiakasterminaalissa pitäisi näkyä jotain tämän kaltaista:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Muutosten tekeminen

Varmistetaan, että ymmärrämme käyttöoikeudet. Etsi tiedosto *server.ts* ja tämä koodi:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Tämä tarkoittaa, että välitetyn tokenin täytyy sisältää "User.Read". Muutetaan tämä "User.Write"-muotoon. Suorita nyt `npm run build` ja käynnistä palvelin uudelleen komennolla `npm start`. Nyt pitäisi näkyä, että autentikointi epäonnistuu, koska meillä ei ole tätä käyttöoikeutta (meillä on User.Read ja Admin.Write):

Asiakas näyttää nyt

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ja palvelimen terminaalissa näkyy:

```text
User exists
```

eikä se etene tästä pisteestä.

Lisää joko tämä käyttöoikeus "User.Write" ja suorita `npm run generate` ja käynnistä asiakas uudelleen TAI muuta palvelimen koodi takaisin.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
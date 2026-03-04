# Esimerkki: Peruspalvelin

Viitemalli, joka näyttää, miten rakennetaan MCP-palvelinsovellus, joka yhdistää MCP-palvelimiin ja renderöi työkalujen käyttöliittymät turvallisessa hiekkalaatikossa.

Tätä peruspalvelinta voi myös käyttää MCP-sovellusten testaamiseen paikallisessa kehityksessä.

## Tärkeimmät tiedostot

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React-käyttöliittymäpalvelin työkalun valinnalle, parametrien syötölle ja iframe-hallinnalle
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Ulkoinen iframe-välityspalvelin turvallisuustarkistuksilla ja kaksisuuntaisella viestien välityksellä
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Ydinlogiikka: palvelinyhteys, työkalun kutsuminen ja AppBridge-asetukset

## Aloittaminen

```bash
npm install
npm run start
# Avaa http://localhost:8080
```
  
Oletuksena palvelinsovellus yrittää yhdistää MCP-palvelimeen osoitteessa `http://localhost:3001/mcp`. Voit muokata tätä käytöstä asettamalla `SERVERS`-ympäristömuuttujan, jonka arvona on JSON-taulukko palvelinten URL-osoitteista:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```
  
## Arkkitehtuuri

Tässä esimerkissä käytetään kaksikerroksista iframe-hiekkalaatikkomallia käyttöliittymän turvalliseen eristämiseen:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```
  
**Miksi kaksi iframea?**

- Ulompi iframe toimii eri alkuperässä (portti 8081), mikä estää suoran pääsyn palvelimeen
- Sisempi iframe vastaanottaa HTML-koodin `srcdoc`-attribuutin kautta ja on rajoitettu hiekkalaatikko-ominaisuuksilla
- Viestit kulkevat ulomman iframen kautta, joka validoi ne ja välittää eteen- ja taaksepäin

Tämä arkkitehtuuri takaa, että vaikka työkalun käyttöliittymän koodi olisi haitallinen, se ei pääse käsiksi palvelinsovelluksen DOM:iin, evästeisiin tai JavaScript-kontekstiin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on ensisijainen lähde. Tärkeissä tiedoissa suositellaan ammattimaisen ihmiskääntäjän käyttämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
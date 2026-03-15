## Testaus ja virheenkorjaus

Ennen kuin aloitat MCP-palvelimesi testaamisen, on tärkeää ymmärtää käytettävissä olevat työkalut ja parhaat käytännöt virheenkorjaukseen. Tehokas testaus varmistaa, että palvelimesi toimii odotetusti ja auttaa sinua nopeasti tunnistamaan ja ratkaisemaan ongelmat. Seuraavassa osiossa käsitellään suositeltuja lähestymistapoja MCP-toteutuksesi validoimiseksi.

## Yleiskatsaus

Tässä oppitunnissa käydään läpi, kuinka valita oikea testauslähestymistapa ja tehokkain testausväline.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Kuvailla erilaisia testauslähestymistapoja.
- Käyttää erilaisia työkaluja koodisi tehokkaaseen testaamiseen.

## MCP-palvelimien testaus

MCP tarjoaa työkaluja, jotka auttavat sinua testaamaan ja virheenkorjaamaan palvelimiasi:

- **MCP Inspector**: Komentorivityökalu, jota voidaan käyttää sekä CLI-työkaluna että visuaalisena työkaluna.
- **Manuaalinen testaus**: Voit käyttää esimerkiksi curl-työkalua suorittaaksesi verkkopyyntöjä, mutta mikä tahansa HTTP-pyynnöt osaava työkalu käy.
- **Yksikkötestaus**: Voit käyttää suosimaasi testauskehystä testataksesi niin palvelimen kuin asiakkaan toimintoja.

### MCP Inspectorin käyttö

Olemme kuvanneet tämän työkalun käyttöä aiemmissa oppitunneissa, mutta käsitellään sitä hieman yleisellä tasolla. Se on Node.js:ssä rakennettu työkalu, jota voit käyttää kutsumalla `npx`-suoritustiedostoa, joka lataa ja asentaa työkalun tilapäisesti ja siivoaa asennuksen suorituksen jälkeen.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) auttaa sinua:

- **Löytämään palvelimen kyvykkyydet**: Havaitsemaan automaattisesti käytettävissä olevat resurssit, työkalut ja kehotteet
- **Testaamaan työkalujen suorittamista**: Kokeilemaan erilaisia parametreja ja näkemään vastaukset reaaliajassa
- **Tarkastelemaan palvelimen metatietoja**: Tutkimaan palvelintietoja, skeemoja ja konfiguraatioita

Tyypillinen työkalun suoritus näyttää tältä:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Yllä oleva komento käynnistää MCP:n ja sen visuaalisen käyttöliittymän ja avaa paikallisen verkkokäyttöliittymän selaimessasi. Näet kojelaudan, jossa on rekisteröityjä MCP-palvelimiasi, niiden käytettävissä olevat työkalut, resurssit ja kehotteet. Käyttöliittymä mahdollistaa työkalujen suorituksen vuorovaikutteisen testaamisen, palvelimen metatietojen tarkastelun ja reaaliaikaisen vastausten seuraamisen, mikä helpottaa MCP-palvelintoteutustesi validoimista ja virheenkorjausta.

Näin se voi näyttää: ![Inspector](../../../../translated_images/fi/connect.141db0b2bd05f096.webp)

Voit myös käyttää tätä työkalua CLI-tilassa, johon lisäät `--cli`-attribuutin. Tässä esimerkki työkalun ajamisesta "CLI"-tilassa, joka listaa kaikki palvelimen työkalut:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuaalinen testaus

Tarkastelun lisäksi MCP Inspector -työkalun käytölle palvelimen kykyjen testaamiseksi toinen samankaltainen lähestymistapa on suorittaa HTTP-pyyntöjä osaava asiakas, kuten curl.

Curlilla voit testata MCP-palvelimia suoraan HTTP-pyyntöjen avulla:

```bash
# Esimerkki: Testipalvelimen metatiedot
curl http://localhost:3000/v1/metadata

# Esimerkki: Työkalun suorittaminen
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kuten yllä curlin käytöstä näet, käytät POST-pyyntöä työkalun kutsumiseen työkalun nimen ja parametrien sisältävän tietoruudun avulla. Käytä sinulle parhaiten sopivaa lähestymistapaa. Komentorivityökalut ovat yleensä nopeampia käyttää ja soveltuvat skriptaamiseen, mikä voi olla hyödyllistä CI/CD-ympäristössä.

### Yksikkötestaus

Luo yksikkötestejä työkaluillesi ja resursseillesi varmistaaksesi, että ne toimivat odotetusti. Tässä esimerkki testauskoodista.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Merkitse koko moduuli asynkronisia testejä varten
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Luo pari testityökalua
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Testaa ilman cursor-parametria (ohitettu)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testaa cursor=None:lla
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testaa cursor merkkijonona
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testaa tyhjällä merkkijonon cursorilla
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Edellinen koodi tekee seuraavaa:

- Hyödyntää pytest-kehystä, jonka avulla voit luoda testejä funktioina ja käyttää assert-lauseita.
- Luo MCP-palvelimen, jossa on kaksi erilaista työkalua.
- Käyttää `assert`-lausetta tarkistamaan, että tietyt ehdot täyttyvät.

Tutustu [täydelliseen tiedostoon täällä](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Edellä olevan tiedoston avulla voit testata omaa palvelintasi varmistaaksesi, että kyvykkyydet luodaan suunnitellusti.

Kaikilla suurimmilla SDK:illa on samanlaisia testausosioita, joten voit mukautua valitsemaasi ajonaikaiseen ympäristöön.

## Esimerkit

- [Java-laskin](../samples/java/calculator/README.md)
- [.Net-laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](../samples/javascript/README.md)
- [TypeScript-laskin](../samples/typescript/README.md)
- [Python-laskin](../../../../03-GettingStarted/samples/python)

## Lisäresurssit

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Mitä seuraavaksi

- Seuraava: [Julkaisu](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
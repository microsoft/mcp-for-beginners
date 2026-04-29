## Testaus ja virheenkorjaus

Ennen kuin aloitat MCP-palvelimesi testaamisen, on tärkeää ymmärtää käytettävissä olevat työkalut ja parhaat käytännöt virheenkorjaukseen. Tehokas testaus varmistaa, että palvelimesi toimii odotetusti ja auttaa sinua tunnistamaan ja ratkaisemaan ongelmat nopeasti. Seuraavassa osiossa esitellään suositeltuja lähestymistapoja MCP-toteutuksesi validoimiseksi.

## Yleiskatsaus

Tämä oppitunti käsittelee oikean testausmenetelmän valintaa ja tehokkaimman testausvälineen käyttämistä.

## Oppimistavoitteet

Tämän oppitunnin lopuksi osaat:

- Kuvata erilaisia testausmenetelmiä.
- Käyttää erilaisia työkaluja koodisi tehokkaaseen testaamiseen.

## MCP-palvelinten testaus

MCP tarjoaa työkaluja, jotka auttavat sinua testaamaan ja virheenkorjaamaan palvelimiasi:

- **MCP Inspector**: Komentorivityökalu, jota voi käyttää sekä CLI-työkaluna että visuaalisena työkaluna.
- **Manuaalinen testaus**: Voit käyttää esimerkiksi curl-työkalua verkkopyyntöjen tekemiseen, mutta mikä tahansa HTTP:n tukema työkalu käy.
- **Yksikkötestaus**: Voit käyttää suosimaasi testauskehystä testataksesi sekä palvelimen että asiakkaan toimintoja.

### MCP Inspectorin käyttö

Olemme kuvanneet tämän työkalun käyttöä aikaisemmissa oppitunneissa, mutta käydään siitä nyt lyhyesti yleisellä tasolla. Se on Node.js:llä rakennettu työkalu, jota voit käyttää kutsumalla `npx`-suoritustiedostoa. Tämä lataa ja asentaa työkalun väliaikaisesti ja siivoaa sen pois, kun pyyntösi on suoritettu.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) auttaa sinua:

- **Palvelimen kyvykkyyksien havaitsemisessa**: Tunnistamaan automaattisesti käytettävissä olevat resurssit, työkalut ja kehotteet
- **Työkalun suorituksen testaamisessa**: Kokeilemaan erilaisia parametreja ja näkemään vastaukset reaaliajassa
- **Palvelimen metadataan tutustumisessa**: Tarkastelemaan palvelimen tietoja, skeemoja ja asetuksia

Tyypillinen työkalun ajaminen näyttää tältä:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Yllä oleva komento käynnistää MCP:n ja sen visuaalisen käyttöliittymän sekä avaa paikallisen web-käyttöliittymän selaimessasi. Näet kojelaudan, joka näyttää rekisteröidyt MCP-palvelimesi, niiden käytettävissä olevat työkalut, resurssit ja kehotteet. Käyttöliittymän avulla voit testata työkalun suorittamista interaktiivisesti, tarkastella palvelimen metadataa ja nähdä vastaukset reaaliajassa, mikä helpottaa MCP-palvelintoteutuksiesi validointia ja virheenkorjausta.

Tältä se voi näyttää: ![Inspector](../../../../translated_images/fi/connect.141db0b2bd05f096.webp)

Voit myös ajaa tämän työkalun CLI-tilassa lisäämällä `--cli`-parametrin. Tässä esimerkki työkalun ajamisesta "CLI"-tilassa, joka listaa kaikki palvelimen työkalut:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manuaalinen testaus

Inspector-työkalun lisäksi palvelimen kyvykkyyksien testaamiseen on toinen samanlainen lähestymistapa, jossa käytetään HTTP:tä tukevia asiakkaita, kuten curl.

Curlilla voit testata MCP-palvelimia suoraan HTTP-pyynnöillä:

```bash
# Esimerkki: Testipalvelimen metatiedot
curl http://localhost:3000/v1/metadata

# Esimerkki: Työkalun suorittaminen
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Kuten yllä olevasta curl-esimerkistä näkyy, käytät POST-pyyntöä kutsuaksesi työkalua, jonka kuormana on työkalun nimi ja sen parametrit. Käytä sitä lähestymistapaa, joka parhaiten sopii sinulle. CLI-työkalut ovat yleisesti nopeampia käyttää ja ne soveltuvat helposti skriptattaviksi, mikä voi olla hyödyllistä CI/CD-ympäristössä.

### Yksikkötestaus

Luo yksikkötestejä työkaluillesi ja resursseillesi varmistaaksesi, että ne toimivat odotetusti. Tässä esimerkki testauskoodista.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Merkitse koko moduuli asynkronisille testeille
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
        # Testaa ilman kursoriparametriä (ohitetaan)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Testaa kursorin ollessa None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Testaa kursorin ollessa merkkijono
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Testaa tyhjällä merkkijonokursorilla
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Edellinen koodi tekee seuraavaa:

- Käyttää pytest-kehystä, joka mahdollistaa testien luomisen funktioina ja assert-lauseiden käytön.
- Luo MCP-palvelimen, jossa on kaksi eri työkalua.
- Käyttää `assert`-lausetta tarkistaakseen, että tietyt ehdot täyttyvät.

Katso koko tiedosto täältä: [täysi tiedosto](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Yllä olevan tiedoston avulla voit testata omaa palvelintasi varmistaaksesi, että kyvykkyydet luodaan oikein.

Kaikissa merkittävissä SDK:issa on vastaavia testiosioita, joten voit mukautua haluamaasi ajonaikaiseen ympäristöön.

## Esimerkit

- [Java Laskin](../samples/java/calculator/README.md)
- [.Net Laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Laskin](../samples/javascript/README.md)
- [TypeScript Laskin](../samples/typescript/README.md)
- [Python Laskin](../../../../03-GettingStarted/samples/python)

## Lisäresurssit

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Mitä seuraavaksi

- Seuraava: [Julkaisu](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on katsottava auktoritatiiviseksi lähteeksi. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ota vastuuta mahdollisista väärinymmärryksistä tai virhetulkintojen aiheutumisesta tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
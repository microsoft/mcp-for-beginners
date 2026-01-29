# Model Context Protocol (MCP) Python -toteutus

Tämä repositorio sisältää Python-toteutuksen Model Context Protocolille (MCP), joka näyttää, miten luodaan sekä palvelin- että asiakasohjelma, jotka kommunikoivat MCP-standardin mukaisesti.

## Yleiskatsaus

MCP-toteutus koostuu kahdesta pääosasta:

1. **MCP Server (`server.py`)** – Palvelin, joka tarjoaa:
   - **Tools**: Etäkäytettävät funktiot
   - **Resources**: Haettavat tiedot
   - **Prompts**: Mallipohjat kielimallien kehotteiden luomiseen

2. **MCP Client (`client.py`)** – Asiakasohjelma, joka yhdistyy palvelimeen ja käyttää sen ominaisuuksia

## Ominaisuudet

Tämä toteutus esittelee useita keskeisiä MCP-ominaisuuksia:

### Tools
- `completion` – Tekstinkorjausten generointi tekoälymalleilta (simuloitu)
- `add` – Yksinkertainen laskin, joka laskee kahden luvun summan

### Resources
- `models://` – Palauttaa tietoa saatavilla olevista tekoälymalleista
- `greeting://{name}` – Palauttaa henkilökohtaisen tervehdyksen annetulle nimelle

### Prompts
- `review_code` – Luo kehotteen koodin tarkistukseen

## Asennus

Käyttääksesi tätä MCP-toteutusta, asenna tarvittavat paketit:

```powershell
pip install mcp-server mcp-client
```

## Palvelimen ja asiakkaan käynnistäminen

### Palvelimen käynnistäminen

Aja palvelin yhdessä terminaali-ikkunassa:

```powershell
python server.py
```

Palvelin voidaan myös käynnistää kehitystilassa MCP CLI:n avulla:

```powershell
mcp dev server.py
```

Tai asentaa Claude Desktopiin (jos saatavilla):

```powershell
mcp install server.py
```

### Asiakkaan käynnistäminen

Aja asiakas toisessa terminaali-ikkunassa:

```powershell
python client.py
```

Tämä yhdistää palvelimeen ja esittelee kaikki käytettävissä olevat ominaisuudet.

### Asiakkaan käyttö

Asiakas (`client.py`) näyttää kaikki MCP:n toiminnot:

```powershell
python client.py
```

Tämä yhdistää palvelimeen ja käyttää kaikkia ominaisuuksia, mukaan lukien työkalut, resurssit ja kehotteet. Tuloste näyttää:

1. Laskintyökalun tuloksen (5 + 7 = 12)
2. Completion-työkalun vastauksen kysymykseen "What is the meaning of life?"
3. Luettelon saatavilla olevista tekoälymalleista
4. Henkilökohtaisen tervehdyksen "MCP Explorer" -nimelle
5. Koodin tarkistuksen kehotemallin

## Toteutuksen yksityiskohdat

Palvelin on toteutettu `FastMCP`-API:n avulla, joka tarjoaa korkean tason abstraktioita MCP-palveluiden määrittelyyn. Tässä yksinkertaistettu esimerkki työkalujen määrittelystä:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Asiakas käyttää MCP-asiakas kirjastoa yhdistääkseen palvelimeen ja kutsuakseen sitä:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Lisätietoja

Lisätietoja MCP:stä löytyy osoitteesta: https://modelcontextprotocol.io/

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
# Oppitunti: Web-hakumCP-palvelimen rakentaminen

Tässä luvussa näytetään, miten rakennetaan käytännön AI-agentti, joka yhdistyy ulkoisiin API-rajapintoihin, käsittelee erilaisia tietotyyppejä, hallitsee virheitä ja ohjaa useita työkaluja – kaikki tuotantovalmiissa muodossa. Näet:

- **Yhdistäminen ulkoisiin API-rajapintoihin, jotka vaativat todennuksen**
- **Erilaisten tietotyyppien käsittely useista päätepisteistä**
- **Vankka virheenkäsittely ja lokitusstrategiat**
- **Monityökalujen orkestrointi yhdessä palvelimessa**

Lopuksi sinulla on käytännön kokemusta malleista ja parhaista käytännöistä, jotka ovat olennaisia kehittyneissä AI- ja LLM-pohjaisissa sovelluksissa.

## Johdanto

Tässä oppitunnissa opit rakentamaan kehittyneen MCP-palvelimen ja -asiakkaan, joka laajentaa LLM:n kykyjä reaaliaikaisella verkkodatan haulla SerpAPI:n avulla. Tämä on tärkeä taito dynaamisten AI-agenttien kehittämiseen, jotka pystyvät hakemaan ajantasaista tietoa verkosta.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Integroimaan ulkoisia API-rajapintoja (kuten SerpAPI) turvallisesti MCP-palvelimeen
- Toteuttamaan useita työkaluja web-, uutis-, tuotehakuun ja kysymys-vastaus-toimintoihin
- Jäsentämään ja muotoilemaan rakenteellista dataa LLM:n käyttöön sopivaksi
- Käsittelemään virheitä ja hallitsemaan API-kutsujen rajoituksia tehokkaasti
- Rakentamaan ja testaamaan sekä automatisoituja että interaktiivisia MCP-asiakkaita

## Web-hakumCP-palvelin

Tässä osiossa esitellään Web Search MCP Serverin arkkitehtuuri ja ominaisuudet. Näet, miten FastMCP ja SerpAPI toimivat yhdessä laajentaen LLM:n kykyjä reaaliaikaisella verkkodatalla.

### Yleiskatsaus

Tämä toteutus sisältää neljä työkalua, jotka demonstroivat MCP:n kykyä käsitellä monipuolisia, ulkoisiin API-rajapintoihin perustuvia tehtäviä turvallisesti ja tehokkaasti:

- **general_search**: Laaja verkkohaku
- **news_search**: Viimeaikaiset uutisotsikot
- **product_search**: Verkkokaupan tiedot
- **qna**: Kysymys-vastaus-pätkät

### Ominaisuudet
- **Koodiesimerkit**: Sisältää kielikohtaisia koodilohkoja Pythonille (ja helposti laajennettavissa muihin kieliin) selkeyden vuoksi

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Ennen kuin ajat asiakasta, on hyödyllistä ymmärtää, mitä palvelin tekee. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) -tiedosto toteuttaa MCP-palvelimen, joka tarjoaa työkaluja web-, uutis-, tuotehakuun ja kysymys-vastaus-toimintoihin SerpAPI:n integroinnin kautta. Se käsittelee saapuvat pyynnöt, hallitsee API-kutsut, jäsentää vastaukset ja palauttaa rakenteelliset tulokset asiakkaalle.

Voit tutustua koko toteutukseen tiedostossa [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Tässä on lyhyt esimerkki siitä, miten palvelin määrittelee ja rekisteröi työkalun:

### Python-palvelin

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Ulkoisen API:n integrointi**: Näyttää, miten API-avaimia ja ulkoisia pyyntöjä käsitellään turvallisesti
- **Rakenteellisen datan jäsentäminen**: Kuvaa, miten API-vastaukset muunnetaan LLM:lle sopiviksi muodoiksi
- **Virheenkäsittely**: Vankka virheenkäsittely asianmukaisella lokituksella
- **Interaktiivinen asiakas**: Sisältää sekä automatisoidut testit että interaktiivisen tilan testausta varten
- **Kontekstinhallinta**: Hyödyntää MCP Contextia lokitukseen ja pyyntöjen seurantaan

## Esivaatimukset

Ennen aloittamista varmista, että ympäristösi on oikein asetettu seuraavien ohjeiden mukaisesti. Tämä varmistaa, että kaikki riippuvuudet on asennettu ja API-avaimesi on konfiguroitu oikein sujuvaa kehitystä ja testausta varten.

- Python 3.8 tai uudempi
- SerpAPI API-avain (Rekisteröidy osoitteessa [SerpAPI](https://serpapi.com/) – ilmainen taso saatavilla)

## Asennus

Aloittaaksesi seuraa näitä ohjeita ympäristösi pystyttämiseksi:

1. Asenna riippuvuudet käyttämällä uv:tä (suositeltu) tai pip:iä:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Luo projektin juureen `.env`-tiedosto, johon lisäät SerpAPI-avaimesi:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Käyttö

Web Search MCP Server on keskeinen komponentti, joka tarjoaa työkaluja web-, uutis-, tuotehakuun ja kysymys-vastaus-toimintoihin SerpAPI:n integroinnin kautta. Se käsittelee saapuvat pyynnöt, hallitsee API-kutsut, jäsentää vastaukset ja palauttaa rakenteelliset tulokset asiakkaalle.

Voit tutustua koko toteutukseen tiedostossa [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Palvelimen käynnistäminen

Käynnistääksesi MCP-palvelimen, käytä seuraavaa komentoa:

```bash
python server.py
```

Palvelin toimii stdio-pohjaisena MCP-palvelimena, johon asiakas voi yhdistää suoraan.

### Asiakastilat

Asiakas (`client.py`) tukee kahta tilaa MCP-palvelimen kanssa kommunikointiin:

- **Normaali tila**: Suorittaa automatisoituja testejä, jotka käyttävät kaikkia työkaluja ja tarkistavat niiden vastaukset. Tämä on kätevä tapa nopeasti varmistaa, että palvelin ja työkalut toimivat odotetusti.
- **Interaktiivinen tila**: Käynnistää valikkopohjaisen käyttöliittymän, jossa voit manuaalisesti valita ja kutsua työkaluja, syöttää omia kyselyjä ja nähdä tulokset reaaliajassa. Tämä on ihanteellinen tapa tutkia palvelimen ominaisuuksia ja kokeilla erilaisia syötteitä.

Voit tutustua koko toteutukseen tiedostossa [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Asiakkaan käynnistäminen

Suorittaaksesi automatisoidut testit (käynnistää palvelimen automaattisesti):

```bash
python client.py
```

Tai aja interaktiivisessa tilassa:

```bash
python client.py --interactive
```

### Testaus eri menetelmillä

Työkaluja voi testata ja käyttää monin eri tavoin tarpeidesi ja työnkulkujesi mukaan.

#### Oman testiskriptin kirjoittaminen MCP Python SDK:lla
Voit myös rakentaa omia testiskriptejä MCP Python SDK:n avulla:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Tässä yhteydessä "testiskripti" tarkoittaa omaa Python-ohjelmaa, jonka kirjoitat MCP-palvelimen asiakkaaksi. Sen sijaan, että kyseessä olisi virallinen yksikkötesti, tämä skripti antaa sinun ohjelmallisesti yhdistää palvelimeen, kutsua mitä tahansa sen työkaluista haluamillasi parametreilla ja tarkastella tuloksia. Tämä lähestymistapa on hyödyllinen:

- Prototyyppien ja kokeilujen tekemiseen työkalukutsuilla
- Palvelimen vastausten validointiin eri syötteillä
- Toistuvien työkalukutsujen automatisointiin
- Omien työnkulkujen tai integraatioiden rakentamiseen MCP-palvelimen päälle

Voit käyttää testiskriptejä nopeasti kokeillaksesi uusia kyselyjä, virheiden selvittämiseen tai jopa lähtökohtana kehittyneemmälle automaatiolle. Alla on esimerkki MCP Python SDK:n käytöstä tällaisen skriptin luomiseen:

## Työkalujen kuvaukset

Voit käyttää palvelimen tarjoamia työkaluja erilaisiin haku- ja kyselytarkoituksiin. Jokainen työkalu on kuvattu alla parametreineen ja esimerkkikäytöineen.

Tässä osiossa kerrotaan yksityiskohtaisesti jokaisesta käytettävissä olevasta työkalusta ja niiden parametreista.

### general_search

Suorittaa yleisen verkkohakukyselyn ja palauttaa muotoillut tulokset.

**Työkalun kutsuminen:**

Voit kutsua `general_search`-työkalua omasta skriptistäsi MCP Python SDK:n avulla tai interaktiivisesti Inspectorin tai interaktiivisen asiakastilan kautta. Tässä esimerkki SDK:n käytöstä:

# [Python-esimerkki](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Vaihtoehtoisesti interaktiivisessa tilassa valitse valikosta `general_search` ja syötä kysely, kun sitä pyydetään.

**Parametrit:**
- `query` (merkkijono): Hakukysely

**Esimerkkipyyntö:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Hakee viimeisimpiä uutisartikkeleita kyselyyn liittyen.

**Työkalun kutsuminen:**

Voit kutsua `news_search`-työkalua omasta skriptistäsi MCP Python SDK:n avulla tai interaktiivisesti Inspectorin tai interaktiivisen asiakastilan kautta. Tässä esimerkki SDK:n käytöstä:

# [Python-esimerkki](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Vaihtoehtoisesti interaktiivisessa tilassa valitse valikosta `news_search` ja syötä kysely, kun sitä pyydetään.

**Parametrit:**
- `query` (merkkijono): Hakukysely

**Esimerkkipyyntö:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Hakee tuotteita, jotka vastaavat kyselyä.

**Työkalun kutsuminen:**

Voit kutsua `product_search`-työkalua omasta skriptistäsi MCP Python SDK:n avulla tai interaktiivisesti Inspectorin tai interaktiivisen asiakastilan kautta. Tässä esimerkki SDK:n käytöstä:

# [Python-esimerkki](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Vaihtoehtoisesti interaktiivisessa tilassa valitse valikosta `product_search` ja syötä kysely, kun sitä pyydetään.

**Parametrit:**
- `query` (merkkijono): Tuotehakukysely

**Esimerkkipyyntö:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Hakee suoria vastauksia kysymyksiin hakukoneista.

**Työkalun kutsuminen:**

Voit kutsua `qna`-työkalua omasta skriptistäsi MCP Python SDK:n avulla tai interaktiivisesti Inspectorin tai interaktiivisen asiakastilan kautta. Tässä esimerkki SDK:n käytöstä:

# [Python-esimerkki](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Vaihtoehtoisesti interaktiivisessa tilassa valitse valikosta `qna` ja syötä kysymys, kun sitä pyydetään.

**Parametrit:**
- `question` (merkkijono): Kysymys, johon etsitään vastausta

**Esimerkkipyyntö:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Koodin yksityiskohdat

Tässä osiossa on koodiesimerkkejä ja viitteitä palvelimen ja asiakkaan toteutuksista.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Katso täydelliset toteutustiedot tiedostoista [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ja [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Tämän oppitunnin edistyneet käsitteet

Ennen rakentamisen aloittamista tässä on joitakin tärkeitä edistyneitä käsitteitä, jotka esiintyvät läpi luvun. Niiden ymmärtäminen auttaa sinua pysymään mukana, vaikka ne olisivat sinulle uusia:

- **Monityökalujen orkestrointi**: Tämä tarkoittaa useiden erilaisten työkalujen (kuten web-haku, uutishaku, tuotehaku ja kysymys-vastaus) ajamista yhdessä MCP-palvelimessa. Se mahdollistaa palvelimesi käsittelevän monenlaisia tehtäviä, ei vain yhtä.
- **API-kutsujen rajoitusten hallinta**: Monet ulkoiset API:t (kuten SerpAPI) rajoittavat, kuinka monta pyyntöä voit tehdä tietyn ajan sisällä. Hyvä koodi tarkistaa nämä rajat ja käsittelee ne sujuvasti, jotta sovelluksesi ei kaadu, jos raja ylittyy.
- **Rakenteellisen datan jäsentäminen**: API-vastaukset ovat usein monimutkaisia ja sisäkkäisiä. Tämä käsite tarkoittaa näiden vastausten muuntamista siisteiksi, helposti käytettäviksi muodoiksi, jotka sopivat LLM:lle tai muille ohjelmille.
- **Virheiden palautuminen**: Joskus tapahtuu virheitä – esimerkiksi verkko pettää tai API ei palauta odotettua. Virheiden palautuminen tarkoittaa, että koodisi pystyy käsittelemään nämä ongelmat ja antamaan hyödyllistä palautetta sen sijaan, että kaatuisi.
- **Parametrien validointi**: Tämä tarkoittaa, että kaikki työkalujen syötteet tarkistetaan oikeiksi ja turvallisiksi käyttää. Se sisältää oletusarvojen asettamisen ja tyyppien varmistamisen, mikä auttaa estämään virheitä ja sekaannuksia.

Tämä osio auttaa sinua diagnosoimaan ja ratkaisemaan yleisiä ongelmia, joita saatat kohdata työskennellessäsi Web Search MCP Serverin kanssa. Jos kohtaat virheitä tai odottamatonta käyttäytymistä, tämä vianmääritysohje tarjoaa ratkaisuja yleisimpiin ongelmiin. Tutustu näihin vinkkeihin ennen lisäavun hakemista – ne usein ratkaisevat ongelmat nopeasti.

## Vianmääritys

Työskennellessäsi Web Search MCP Serverin kanssa saatat toisinaan kohdata ongelmia – tämä on normaalia ulkoisten API:en ja uusien työkalujen kanssa työskennellessä. Tämä osio tarjoaa käytännön ratkaisuja yleisimpiin ongelmiin, jotta pääset nopeasti takaisin raiteille. Jos kohtaat virheen, aloita tästä: alla olevat vinkit käsittelevät yleisimpiä käyttäjien kohtaamia ongelmia ja voivat usein ratkaista ongelmasi ilman lisäapua.

### Yleiset ongelmat

Alla on joitakin yleisimpiä ongelmia, joita käyttäjät kohtaavat, selkeine selityksineen ja ratkaisuohjeineen:

1. **SERPAPI_KEY puuttuu .env-tiedostosta**
   - Jos näet virheen `SERPAPI_KEY environment variable not found`, se tarkoittaa, että sovelluksesi ei löydä SerpAPI-avainta. Korjataksesi tämän, luo projektin juureen `.env`-tiedosto (jos sitä ei vielä ole) ja lisää rivi `SERPAPI_KEY=oma_serpapi_avaimesi`. Muista korvata `oma_serpapi_avaimesi` oikealla avaimellasi SerpAPI:n sivustolta.

2. **Moduulia ei löydy -virheet**
   - Virheet kuten `ModuleNotFoundError: No module named 'httpx'` tarkoittavat, että tarvittava Python-kirjasto puuttuu. Tämä tapahtuu yleensä, jos et ole asentanut kaikkia riippuvuuksia. Korjaa tämä ajamalla terminaalissa `pip install -r requirements.txt`, jolloin kaikki projektin tarvitsemat paketit asennetaan.

3. **Yhteysongelmat**
   - Jos saat virheen kuten `Error during client execution`, se tarkoittaa usein, että asiakas ei pysty yhdistämään palvelimeen tai palvelin ei ole käynnissä odotetusti. Tarkista, että sekä asiakas että palvelin ovat yhteensopivia versioita ja että `server.py` on olemassa ja käynnissä oikeassa hakemistossa. Palvelimen ja asiakkaan uudelleenkäynnistys voi myös auttaa.

4. **SerpAPI-virheet**
   - Virhe `Search API returned error status: 401` tarkoittaa, että SerpAPI-avaimesi puuttuu, on virheellinen tai vanhentunut. Mene SerpAPI-hallintapaneeliisi, varmista avain ja päivitä tarvittaessa `.env`-tiedosto. Jos avain on oikein mutta virhe jatkuu, tarkista, onko ilmainen käyttöoikeutesi loppunut.

### Debug-tila

Oletuksena sovellus kirjaa vain tärkeimmät tiedot. Jos haluat nähdä enemmän yksityiskohtia tapahtumista (esim. vaikeiden ongelmien diagnosointiin), voit ottaa DEBUG-tilan käyttöön. Tämä näyttää paljon enemmän tietoa jokaisesta sovelluksen suorittamasta vaiheesta.

**Esimerkki: Normaali tulostus**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Esimerkki: DEBUG-tulostus**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Huomaa, että DEBUG-
DEBUG-tilan aktivoimiseksi aseta lokitustaso DEBUG-arvoksi `client.py`- tai `server.py`-tiedoston alkuun:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Mitä seuraavaksi

- [5.10 Reaaliaikainen suoratoisto](../mcp-realtimestreaming/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
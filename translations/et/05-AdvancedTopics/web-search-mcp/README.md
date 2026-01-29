# Õppetund: Veebipõhise otsingu MCP serveri loomine

Selles peatükis näidatakse, kuidas luua päriselu AI-agent, mis integreerub väliste API-dega, käsitleb erinevaid andmetüüpe, haldab vigu ja koordineerib mitut tööriista – kõik tootmisvalmis formaadis. Saate teada:

- **Integratsioon väliste API-dega, mis nõuavad autentimist**
- **Erinevate andmetüüpide käsitlemine mitmest lõpp-punktist**
- **Tõhusad veahaldus- ja logimisstrateegiad**
- **Mitme tööriista koordineerimine ühes serveris**

Õppetunni lõpuks omandate praktilisi kogemusi mustrite ja parimate tavadega, mis on hädavajalikud arenenud AI ja LLM-põhiste rakenduste jaoks.

## Sissejuhatus

Selles õppetunnis õpite, kuidas luua täiustatud MCP serverit ja klienti, mis laiendavad LLM-i võimekust reaalajas veebialaste andmetega, kasutades SerpAPI-d. See on oluline oskus dünaamiliste AI-agentide arendamiseks, mis pääsevad ligi ajakohasele teabele veebist.

## Õppe-eesmärgid

Õppetunni lõpuks oskate:

- Turvaliselt integreerida väliseid API-sid (nagu SerpAPI) MCP serverisse
- Rakendada mitut tööriista veebis, uudistes, toodete otsingus ja küsimuste-vastuste jaoks
- Parsida ja vormindada struktureeritud andmeid LLM-i tarbimiseks
- Tõhusalt hallata vigu ja API päringute limiite
- Luua ja testida nii automatiseeritud kui ka interaktiivseid MCP kliente

## Veebipõhine otsingu MCP server

Selles osas tutvustatakse Veebipõhise otsingu MCP serveri arhitektuuri ja funktsioone. Näete, kuidas FastMCP ja SerpAPI koos töötavad, et laiendada LLM-i võimekust reaalajas veebialaste andmetega.

### Ülevaade

See rakendus sisaldab nelja tööriista, mis demonstreerivad MCP võimet turvaliselt ja tõhusalt käsitleda mitmekesiseid, väliste API-dega seotud ülesandeid:

- **general_search**: Üldiste veebitulemuste jaoks
- **news_search**: Viimaste pealkirjade jaoks
- **product_search**: E-kaubanduse andmete jaoks
- **qna**: Küsimuste ja vastuste fragmentide jaoks

### Funktsioonid
- **Koodinäited**: Sisaldab keelespetsiifilisi koodiblokke Pythonis (ja hõlpsasti laiendatav teistele keeltele), kasutades koodipivoteid selguse huvides

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

Enne kliendi käivitamist on kasulik mõista, mida server teeb. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) fail rakendab MCP serveri, mis pakub tööriistu veebis, uudistes, toodete otsingus ja küsimuste-vastuste jaoks, integreerudes SerpAPI-ga. See käsitleb sissetulevaid päringuid, haldab API-kõnesid, parsib vastuseid ja tagastab struktureeritud tulemused kliendile.

Täielikku rakendust saate vaadata failis [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Siin on lühike näide, kuidas server määratleb ja registreerib tööriista:

### Python Server

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

- **Välise API integratsioon**: Näitab API võtmete ja väliste päringute turvalist käsitlemist
- **Struktureeritud andmete parsimine**: Näitab, kuidas API vastuseid LLM-sõbralikeks formaatideks muuta
- **Veahaldus**: Tõhus veahaldus koos sobiva logimisega
- **Interaktiivne klient**: Sisaldab nii automatiseeritud teste kui ka interaktiivset režiimi testimiseks
- **Konteksti haldamine**: Kasutab MCP konteksti logimiseks ja päringute jälgimiseks

## Eeltingimused

Enne alustamist veenduge, et teie keskkond on korralikult seadistatud, järgides neid samme. See tagab, et kõik sõltuvused on installitud ja teie API võtmed on õigesti konfigureeritud sujuvaks arendamiseks ja testimiseks.

- Python 3.8 või uuem
- SerpAPI API võti (registreeruge [SerpAPI](https://serpapi.com/) - saadaval tasuta pakett)

## Paigaldamine

Alustamiseks järgige neid samme, et oma keskkond seadistada:

1. Installige sõltuvused, kasutades uv (soovitatav) või pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Looge projekti juurkausta `.env` fail oma SerpAPI võtmega:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Kasutamine

Veebipõhine otsingu MCP server on põhikomponent, mis pakub tööriistu veebis, uudistes, toodete otsingus ja küsimuste-vastuste jaoks, integreerudes SerpAPI-ga. See käsitleb sissetulevaid päringuid, haldab API-kõnesid, parsib vastuseid ja tagastab struktureeritud tulemused kliendile.

Täielikku rakendust saate vaadata failis [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Serveri käivitamine

MCP serveri käivitamiseks kasutage järgmist käsku:

```bash
python server.py
```

Server töötab stdio-põhise MCP serverina, millega klient saab otse ühendust võtta.

### Kliendi režiimid

Klient (`client.py`) toetab kahte režiimi MCP serveriga suhtlemiseks:

- **Tavaline režiim**: Käitab automatiseeritud teste, mis kasutavad kõiki tööriistu ja kontrollivad nende vastuseid. See on kasulik serveri ja tööriistade kiireks kontrollimiseks.
- **Interaktiivne režiim**: Käivitab menüüpõhise liidese, kus saate käsitsi valida ja kasutada tööriistu, sisestada kohandatud päringuid ja näha tulemusi reaalajas. See sobib serveri võimaluste uurimiseks ja erinevate sisendite katsetamiseks.

Täielikku rakendust saate vaadata failis [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Kliendi käivitamine

Automatiseeritud testide käivitamiseks (see käivitab automaatselt serveri):

```bash
python client.py
```

Või käivitage interaktiivses režiimis:

```bash
python client.py --interactive
```

### Testimine erinevate meetoditega

Serveri pakutavate tööriistade testimiseks ja nendega suhtlemiseks on mitu võimalust, sõltuvalt teie vajadustest ja töövoost.

#### Kohandatud testskriptide kirjutamine MCP Python SDK-ga
Samuti saate luua oma testskripte, kasutades MCP Python SDK-d:

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

Selles kontekstis tähendab "testskript" kohandatud Python-programmi, mille kirjutate MCP serveri kliendina. Selle asemel, et olla formaalne üksustest, võimaldab see skript teil programmiliselt serveriga ühendust võtta, kutsuda selle tööriistu valitud parameetritega ja uurida tulemusi. See lähenemine on kasulik:
- Tööriistakõnede prototüüpimiseks ja katsetamiseks
- Serveri vastuste valideerimiseks erinevatele sisenditele
- Korduvate tööriistakõnede automatiseerimiseks
- Oma töövoogude või integratsioonide loomiseks MCP serveri peale

Testskripte saate kasutada uute päringute kiireks proovimiseks, tööriistade käitumise silumiseks või isegi lähtepunktina keerukamaks automatiseerimiseks. Allpool on näide, kuidas kasutada MCP Python SDK-d sellise skripti loomiseks:

## Tööriistade kirjeldused

Serveri pakutavaid tööriistu saate kasutada erinevat tüüpi otsingute ja päringute tegemiseks. Iga tööriista kirjeldus on allpool koos selle parameetrite ja näidiskasutusega.

Selles osas on üksikasjad iga saadaoleva tööriista ja nende parameetrite kohta.

### general_search

Teostab üldise veebipõhise otsingu ja tagastab vormindatud tulemused.

**Kuidas seda tööriista kasutada:**

Saate kutsuda `general_search` oma skriptist, kasutades MCP Python SDK-d, või interaktiivselt, kasutades Inspectorit või interaktiivset kliendirežiimi. Siin on koodinäide SDK kasutamisest:

# [Python Näide](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatiivselt valige interaktiivses režiimis menüüst `general_search` ja sisestage oma päring, kui seda küsitakse.

**Parameetrid:**
- `query` (string): Otsingupäring

**Näidis päring:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Otsib hiljutisi uudisteartikleid, mis on seotud päringuga.

**Kuidas seda tööriista kasutada:**

Saate kutsuda `news_search` oma skriptist, kasutades MCP Python SDK-d, või interaktiivselt, kasutades Inspectorit või interaktiivset kliendirežiimi. Siin on koodinäide SDK kasutamisest:

# [Python Näide](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatiivselt valige interaktiivses režiimis menüüst `news_search` ja sisestage oma päring, kui seda küsitakse.

**Parameetrid:**
- `query` (string): Otsingupäring

**Näidis päring:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Otsib tooteid, mis vastavad päringule.

**Kuidas seda tööriista kasutada:**

Saate kutsuda `product_search` oma skriptist, kasutades MCP Python SDK-d, või interaktiivselt, kasutades Inspectorit või interaktiivset kliendirežiimi. Siin on koodinäide SDK kasutamisest:

# [Python Näide](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatiivselt valige interaktiivses režiimis menüüst `product_search` ja sisestage oma päring, kui seda küsitakse.

**Parameetrid:**
- `query` (string): Toote otsingupäring

**Näidis päring:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Saab otsingumootoritelt otseseid vastuseid küsimustele.

**Kuidas seda tööriista kasutada:**

Saate kutsuda `qna` oma skriptist, kasutades MCP Python SDK-d, või interaktiivselt, kasutades Inspectorit või interaktiivset kliendirežiimi. Siin on koodinäide SDK kasutamisest:

# [Python Näide](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatiivselt valige interaktiivses režiimis menüüst `qna` ja sisestage oma küsimus, kui seda küsitakse.

**Parameetrid:**
- `question` (string): Küsimus, millele vastust otsitakse

**Näidis päring:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Koodi üksikasjad

Selles osas on koodinäited ja viited serveri ja kliendi rakendustele.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Vaadake [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ja [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) täielikke rakenduse üksikasju.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Täiustatud kontseptsioonid selles õppetunnis

Enne alustamist on siin mõned olulised täiustatud kontseptsioonid, mis ilmuvad kogu selle peatüki jooksul. Nende mõistmine aitab teil kaasa minna, isegi kui olete nendega uus:

- **Mitme tööriista koordineerimine**: See tähendab mitme erineva tööriista (nagu veebipõhine otsing, uudiste otsing, toodete otsing ja küsimuste-vastuste) käivitamist ühe MCP serveri sees. See võimaldab serveril käsitleda mitmesuguseid ülesandeid, mitte ainult ühte.
- **API päringute limiidi haldamine**: Paljud välised API-d (nagu SerpAPI) piiravad, kui palju päringuid saate teatud aja jooksul teha. Hea kood kontrollib neid limiite ja käsitleb neid sujuvalt, et teie rakendus ei katkeks, kui limiit saavutatakse.
- **Struktureeritud andmete parsimine**: API vastused on sageli keerulised ja pesastatud. See kontseptsioon seisneb nende vastuste muutmises puhtaks, hõlpsasti kasutatavaks formaadiks, mis on sõbralik LLM-idele või teistele programmidele.
- **Veataaste**: Mõnikord lähevad asjad valesti – võib-olla võrguühendus katkeb või API ei tagasta oodatut. Veataaste tähendab, et teie kood suudab neid probleeme käsitleda ja siiski kasulikku tagasisidet anda, selle asemel et kokku kukkuda.
- **Parameetrite valideerimine**: See seisneb selles, et kõik tööriistade sisendid kontrollitakse ja tehakse kindlaks, et need on õiged ja turvalised. See hõlmab vaikeväärtuste seadmist ja tüüpide kontrollimist, mis aitab vältida vigu ja segadust.

See osa aitab teil diagnoosida ja lahendada levinud probleeme, millega võite Veebipõhise otsingu MCP serveriga töötades kokku puutuda. Kui teil tekib vigu või ootamatut käitumist, pakub see tõrkeotsingu osa lahendusi kõige tavalisematele probleemidele. Vaadake neid näpunäiteid enne täiendava abi otsimist – need lahendavad sageli probleemid kiiresti.

## Tõrkeotsing

Veebipõhise otsingu MCP serveriga töötades võite aeg-ajalt probleeme kohata – see on normaalne, kui arendate väliste API-de ja uute tööriistadega. Selles osas on praktilised lahendused kõige tavalisematele probleemidele, et saaksite kiiresti edasi liikuda. Kui kohtate viga, alustage siit: allpool olevad näpunäited käsitlevad probleeme, millega enamik kasutajaid kokku puutub, ja võivad sageli teie probleemi lahendada ilma lisatoeta.

### Levinud probleemid

Allpool on mõned kõige sagedasemad probleemid, millega kasutajad kokku puutuvad, koos selgete selgituste ja lahendamise sammudega:

1. **Puuduv SERPAPI_KEY `.env` failis**
   - Kui näete viga `SERPAPI_KEY environment variable not found`, tähendab see, et teie rakendus ei leia SerpAPI-le juurdepääsuks vajalikku API võtit. Selle parandamiseks looge oma projekti juurkausta fail nimega `.env` (kui seda veel pole) ja lisage rida nagu `SERPAPI_KEY=your_serpapi_key_here`. Veenduge, et asendate `your_serpapi_key_here` oma tegeliku võtmega SerpAPI veebisaidilt.

2. **Moodulite puudumise vead**
   - Vead nagu `ModuleNotFoundError: No module named 'httpx'` viitavad sellele, et vajalik Python-pakett puudub. See juhtub tavaliselt siis, kui te pole kõiki sõltuvusi installinud. Selle lahendamiseks käivitage oma terminalis `pip install -r requirements.txt`, et installida kõik, mida teie projekt vajab.

3. **Ühenduse probleemid**
   - Kui saate vea nagu `Error during client execution`, tähendab see sageli, et klient ei saa serveriga ühendust või server ei tööta oodatult. Kontrollige, kas nii klient kui ka server on ühilduvad versioonid, ja kas `server.py` on õiges kataloogis olemas ja töötab. Serveri ja kliendi taaskäivitamine võib samuti aidata.

4. **SerpAPI vead**
   - Kui näete `Search API returned error status: 401`, tähendab see, et teie SerpAPI võti puudub, on vale või aegunud. Minge oma SerpAPI juhtpaneelile, kontrollige oma võtit ja värskendage vajadusel oma `.env` faili. Kui teie võti on õige, kuid näete endiselt seda viga, kontrollige, kas teie tasuta pakett on limiidi ületanud.

### Debug-režiim

Vaikimisi logib rakendus ainult olulist teavet. Kui soovite näha rohkem üksikasju selle kohta, mis toimub (näiteks keeruliste probleemide diagnoosimiseks), saate lubada DEBUG-režiimi. See näitab teile palju rohkem iga sammu kohta, mida rakendus teeb.

**Näide: Tavaline väljund**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Näide: DEBUG-väljund**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Pange tähele, kuidas DEBUG-režiim sisaldab lisaridu HTTP-päringute, vastuste ja muude sisemiste üksikasjade kohta. See võib olla väga kasulik tõrkeotsinguks.
DEBUG-režiimi lubamiseks seadke logimise tase `client.py` või `server.py` faili alguses väärtusele DEBUG:

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

## Mis edasi 

- [5.10 Reaalajas voogedastus](../mcp-realtimestreaming/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
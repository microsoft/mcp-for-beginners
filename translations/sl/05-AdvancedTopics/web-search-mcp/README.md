# Lekcija: Gradnja MCP strežnika za spletno iskanje

Ta poglavje prikazuje, kako zgraditi resničnega AI agenta, ki se povezuje z zunanjimi API-ji, obdeluje različne vrste podatkov, upravlja napake in usklajuje več orodij — vse v produkcijsko pripravljenem formatu. Videli boste:

- **Integracija z zunanjimi API-ji, ki zahtevajo avtentikacijo**
- **Obdelava različnih vrst podatkov iz več končnih točk**
- **Robustno upravljanje napak in strategije beleženja**
- **Usklajevanje več orodij v enem strežniku**

Na koncu boste pridobili praktične izkušnje s vzorci in najboljšimi praksami, ki so ključne za napredne AI in aplikacije, ki temeljijo na LLM.

## Uvod

V tej lekciji se boste naučili, kako zgraditi napredni MCP strežnik in odjemalca, ki razširjata zmogljivosti LLM z uporabo podatkov iz spleta v realnem času preko SerpAPI. To je ključna veščina za razvoj dinamičnih AI agentov, ki lahko dostopajo do ažurnih informacij iz spleta.

## Cilji učenja

Na koncu te lekcije boste znali:

- Varnostno integrirati zunanje API-je (kot je SerpAPI) v MCP strežnik
- Implementirati več orodij za spletno, novičarsko, produktno iskanje in vprašanja-odgovore
- Razčleniti in oblikovati strukturirane podatke za uporabo v LLM
- Učinkovito upravljati napake in omejitve hitrosti API-ja
- Zgraditi in testirati tako avtomatizirane kot interaktivne MCP odjemalce

## MCP strežnik za spletno iskanje

Ta razdelek predstavlja arhitekturo in funkcionalnosti MCP strežnika za spletno iskanje. Videli boste, kako FastMCP in SerpAPI skupaj razširjata zmogljivosti LLM z uporabo podatkov iz spleta v realnem času.

### Pregled

Ta implementacija vključuje štiri orodja, ki prikazujejo sposobnost MCP za varno in učinkovito upravljanje različnih nalog, ki temeljijo na zunanjih API-jih:

- **general_search**: Za široke spletne rezultate
- **news_search**: Za najnovejše naslove novic
- **product_search**: Za podatke o e-trgovanju
- **qna**: Za izseke vprašanj in odgovorov

### Funkcionalnosti
- **Primeri kode**: Vključuje jezikovno specifične kode za Python (in enostavno razširljive na druge jezike) z uporabo kodnih blokov za jasnost

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

Pred zagonom odjemalca je koristno razumeti, kaj strežnik počne. Datoteka [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementira MCP strežnik, ki izpostavlja orodja za spletno, novičarsko, produktno iskanje in vprašanja-odgovore z integracijo SerpAPI. Obdeluje dohodne zahteve, upravlja klice API-ja, razčlenjuje odgovore in vrača strukturirane rezultate odjemalcu.

Celotno implementacijo si lahko ogledate v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Tukaj je kratek primer, kako strežnik definira in registrira orodje:

### Python strežnik

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

- **Integracija zunanjih API-jev**: Prikazuje varno upravljanje API ključev in zunanjih zahtevkov
- **Razčlenjevanje strukturiranih podatkov**: Prikazuje, kako pretvoriti odgovore API-ja v formate, prijazne LLM
- **Upravljanje napak**: Robustno upravljanje napak z ustreznim beleženjem
- **Interaktivni odjemalec**: Vključuje tako avtomatizirane teste kot interaktivni način za testiranje
- **Upravljanje konteksta**: Izrablja MCP Context za beleženje in sledenje zahtevam

## Predpogoji

Preden začnete, poskrbite, da je vaše okolje pravilno nastavljeno z naslednjimi koraki. Tako boste zagotovili, da so vse odvisnosti nameščene in da so vaši API ključi pravilno konfigurirani za nemoten razvoj in testiranje.

- Python 3.8 ali novejši
- SerpAPI API ključ (registrirajte se na [SerpAPI](https://serpapi.com/) - na voljo brezplačni paket)

## Namestitev

Za začetek sledite tem korakom za nastavitev okolja:

1. Namestite odvisnosti z uporabo uv (priporočeno) ali pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Ustvarite datoteko `.env` v korenu projekta z vašim SerpAPI ključem:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Uporaba

MCP strežnik za spletno iskanje je osrednja komponenta, ki izpostavlja orodja za spletno, novičarsko, produktno iskanje in vprašanja-odgovore z integracijo SerpAPI. Obdeluje dohodne zahteve, upravlja klice API-ja, razčlenjuje odgovore in vrača strukturirane rezultate odjemalcu.

Celotno implementacijo si lahko ogledate v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Zagon strežnika

Za zagon MCP strežnika uporabite naslednji ukaz:

```bash
python server.py
```

Strežnik bo tekel kot MCP strežnik, ki temelji na stdio, in se mu bo odjemalec lahko neposredno povezal.

### Načini odjemalca

Odjemalec (`client.py`) podpira dva načina za interakcijo z MCP strežnikom:

- **Normalni način**: Izvede avtomatizirane teste, ki preizkusijo vsa orodja in preverijo njihove odgovore. To je uporabno za hitro preverjanje, ali strežnik in orodja delujejo kot pričakovano.
- **Interaktivni način**: Zažene meni, kjer lahko ročno izbirate in kličete orodja, vnašate lastne poizvedbe in v realnem času vidite rezultate. Idealno za raziskovanje zmogljivosti strežnika in eksperimentiranje z različnimi vnosi.

Celotno implementacijo si lahko ogledate v [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Zagon odjemalca

Za zagon avtomatiziranih testov (to bo samodejno zagnalo tudi strežnik):

```bash
python client.py
```

Ali za zagon v interaktivnem načinu:

```bash
python client.py --interactive
```

### Testiranje z različnimi metodami

Obstaja več načinov za testiranje in interakcijo z orodji, ki jih strežnik ponuja, odvisno od vaših potreb in delovnega toka.

#### Pisanje lastnih testnih skript z MCP Python SDK
Lahko tudi ustvarite svoje testne skripte z uporabo MCP Python SDK:

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

V tem kontekstu "testna skripta" pomeni lasten Python program, ki ga napišete kot odjemalca za MCP strežnik. Namesto formalnega enotnega testa vam ta skripta omogoča, da se programsko povežete s strežnikom, pokličete katerokoli orodje z izbranimi parametri in pregledate rezultate. Ta pristop je uporaben za:
- Prototipiranje in eksperimentiranje z orodji
- Preverjanje, kako strežnik odgovarja na različne vnose
- Avtomatizacijo ponavljajočih se klicev orodij
- Gradnjo lastnih delovnih tokov ali integracij na vrhu MCP strežnika

Testne skripte lahko uporabite za hitro preizkušanje novih poizvedb, odpravljanje napak v orodjih ali kot izhodišče za bolj napredno avtomatizacijo. Spodaj je primer, kako uporabiti MCP Python SDK za ustvarjanje takšne skripte:

## Opisi orodij

Za izvajanje različnih vrst iskanj in poizvedb lahko uporabite naslednja orodja, ki jih ponuja strežnik. Vsako orodje je opisano spodaj skupaj z njegovimi parametri in primeri uporabe.

Ta razdelek podaja podrobnosti o vsakem razpoložljivem orodju in njihovih parametrih.

### general_search

Izvede splošno spletno iskanje in vrne oblikovane rezultate.

**Kako poklicati to orodje:**

`general_search` lahko pokličete iz lastne skripte z uporabo MCP Python SDK ali interaktivno preko Inspectorja ali interaktivnega načina odjemalca. Tukaj je primer kode z uporabo SDK:

# [Python primer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, v interaktivnem načinu izberite `general_search` iz menija in vnesite poizvedbo, ko boste pozvani.

**Parametri:**
- `query` (niz): Iskalna poizvedba

**Primer zahteve:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Išče najnovejše novice, povezane s poizvedbo.

**Kako poklicati to orodje:**

`news_search` lahko pokličete iz lastne skripte z uporabo MCP Python SDK ali interaktivno preko Inspectorja ali interaktivnega načina odjemalca. Tukaj je primer kode z uporabo SDK:

# [Python primer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, v interaktivnem načinu izberite `news_search` iz menija in vnesite poizvedbo, ko boste pozvani.

**Parametri:**
- `query` (niz): Iskalna poizvedba

**Primer zahteve:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Išče izdelke, ki ustrezajo poizvedbi.

**Kako poklicati to orodje:**

`product_search` lahko pokličete iz lastne skripte z uporabo MCP Python SDK ali interaktivno preko Inspectorja ali interaktivnega načina odjemalca. Tukaj je primer kode z uporabo SDK:

# [Python primer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, v interaktivnem načinu izberite `product_search` iz menija in vnesite poizvedbo, ko boste pozvani.

**Parametri:**
- `query` (niz): Poizvedba za iskanje izdelkov

**Primer zahteve:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Pridobi neposredne odgovore na vprašanja iz iskalnikov.

**Kako poklicati to orodje:**

`qna` lahko pokličete iz lastne skripte z uporabo MCP Python SDK ali interaktivno preko Inspectorja ali interaktivnega načina odjemalca. Tukaj je primer kode z uporabo SDK:

# [Python primer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, v interaktivnem načinu izberite `qna` iz menija in vnesite vprašanje, ko boste pozvani.

**Parametri:**
- `question` (niz): Vprašanje, na katerega želite najti odgovor

**Primer zahteve:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Podrobnosti kode

Ta razdelek vsebuje odlomke kode in reference za implementacije strežnika in odjemalca.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Celotne podrobnosti implementacije si oglejte v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Napredni koncepti v tej lekciji

Preden začnete z gradnjo, so tukaj nekateri pomembni napredni koncepti, ki se bodo pojavljali skozi celotno poglavje. Razumevanje teh vam bo pomagalo slediti, tudi če ste z njimi novi:

- **Usklajevanje več orodij**: To pomeni, da v enem MCP strežniku teče več različnih orodij (kot so spletno iskanje, novičarsko iskanje, produktno iskanje in vprašanja-odgovori). To omogoča, da strežnik obvladuje različne naloge, ne le eno.
- **Upravljanje omejitev hitrosti API-ja**: Veliko zunanjih API-jev (kot je SerpAPI) omejuje, koliko zahtevkov lahko naredite v določenem času. Dobra koda preverja te omejitve in jih obravnava na eleganten način, da aplikacija ne crkne, če doseže omejitev.
- **Razčlenjevanje strukturiranih podatkov**: Odgovori API-jev so pogosto kompleksni in gnezdeni. Ta koncept pomeni pretvorbo teh odgovorov v čiste, enostavne formate, ki so prijazni LLM ali drugim programom.
- **Obnova po napaki**: Včasih gre kaj narobe — morda omrežje odpove ali API ne vrne pričakovanih podatkov. Obnova po napaki pomeni, da vaša koda zna te težave obravnavati in še vedno nuditi uporabne povratne informacije, namesto da bi se zrušila.
- **Preverjanje parametrov**: Gre za preverjanje, da so vsi vnosi v vaša orodja pravilni in varni za uporabo. Vključuje nastavljanje privzetih vrednosti in preverjanje tipov, kar pomaga preprečiti napake in zmedo.

Ta razdelek vam bo pomagal diagnosticirati in rešiti pogoste težave, na katere lahko naletite pri delu z MCP strežnikom za spletno iskanje. Če naletite na napake ali nepričakovano vedenje, ta razdelek za odpravljanje težav ponuja rešitve za najpogostejše težave. Preden poiščete dodatno pomoč, preglejte te nasvete — pogosto hitro odpravijo težave.

## Odpravljanje težav

Pri delu z MCP strežnikom za spletno iskanje se lahko občasno pojavijo težave — to je običajno pri razvoju z zunanjimi API-ji in novimi orodji. Ta razdelek ponuja praktične rešitve za najpogostejše težave, da se lahko hitro vrnete na pravo pot. Če naletite na napako, začnite tukaj: spodnji nasveti obravnavajo težave, s katerimi se največ uporabnikov srečuje, in pogosto rešijo vaš problem brez dodatne pomoči.

### Pogoste težave

Spodaj so nekatere najpogostejše težave, s katerimi se uporabniki srečujejo, skupaj z jasnimi razlagami in koraki za rešitev:

1. **Manjka SERPAPI_KEY v datoteki .env**
   - Če vidite napako `SERPAPI_KEY environment variable not found`, to pomeni, da vaša aplikacija ne najde API ključa, potrebnega za dostop do SerpAPI. Za rešitev ustvarite datoteko `.env` v korenu projekta (če še ne obstaja) in dodajte vrstico, kot je `SERPAPI_KEY=your_serpapi_key_here`. Poskrbite, da boste `your_serpapi_key_here` zamenjali z dejanskim ključem s spletne strani SerpAPI.

2. **Napake "Module not found"**
   - Napake, kot je `ModuleNotFoundError: No module named 'httpx'`, kažejo, da manjka potrebna Python knjižnica. To se običajno zgodi, če niste namestili vseh odvisnosti. Za rešitev zaženite `pip install -r requirements.txt` v terminalu, da namestite vse, kar projekt potrebuje.

3. **Težave s povezavo**
   - Če dobite napako, kot je `Error during client execution`, to pogosto pomeni, da se odjemalec ne more povezati s strežnikom ali strežnik ne teče kot pričakovano. Preverite, da sta odjemalec in strežnik združljivi različici in da je `server.py` prisoten ter teče v pravilni mapi. Ponovni zagon strežnika in odjemalca lahko prav tako pomaga.

4. **Napake SerpAPI**
   - Napaka `Search API returned error status: 401` pomeni, da vaš SerpAPI ključ manjka, je napačen ali je potekel. Obiščite svojo nadzorno ploščo SerpAPI, preverite ključ in po potrebi posodobite datoteko `.env`. Če je ključ pravilen, a napaka še vedno obstaja, preverite, ali vam je potekel brezplačni paket.

### Način za odpravljanje napak (Debug)

Privzeto aplikacija beleži le pomembne informacije. Če želite videti več podrobnosti o dogajanju (na primer za diagnosticiranje težav), lahko omogočite način DEBUG. Ta način vam bo prikazal veliko več o vsakem koraku, ki ga aplikacija izvaja.

**Primer: običajen izpis**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Primer: izpis v načinu DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Opazite, da način DEBUG vključuje dodatne vrstice o HTTP zahtevah, odgovorih in drugih notranjih podrobnostih. To je lahko zelo koristno pri odpravljanju težav.
Za omogočanje načina DEBUG nastavite raven beleženja na DEBUG na vrhu vaše datoteke `client.py` ali `server.py`:

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

## Kaj sledi

- [5.10 Pretakanje v realnem času](../mcp-realtimestreaming/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
# Lekcija: Izgradnja MCP servera za web pretraživanje

Ovo poglavlje pokazuje kako izgraditi stvarnog AI agenta koji se integrira s vanjskim API-jima, obrađuje različite vrste podataka, upravlja pogreškama i koordinira više alata — sve u produkcijski spremnom obliku. Vidjet ćete:

- **Integraciju s vanjskim API-jima koji zahtijevaju autentifikaciju**
- **Rukovanje različitim vrstama podataka s više krajnjih točaka**
- **Robusne strategije za upravljanje pogreškama i zapisivanje**
- **Orkestraciju više alata unutar jednog servera**

Na kraju ćete imati praktično iskustvo s obrascima i najboljim praksama koje su ključne za napredne AI i LLM aplikacije.

## Uvod

U ovoj lekciji naučit ćete kako izgraditi napredni MCP server i klijenta koji proširuju mogućnosti LLM-a s podacima s weba u stvarnom vremenu koristeći SerpAPI. Ovo je ključna vještina za razvoj dinamičnih AI agenata koji mogu pristupiti najnovijim informacijama s interneta.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Sigurno integrirati vanjske API-je (poput SerpAPI) u MCP server
- Implementirati više alata za pretraživanje weba, vijesti, proizvoda i Q&A
- Parsirati i formatirati strukturirane podatke za potrebe LLM-a
- Učinkovito upravljati pogreškama i ograničenjima API-ja
- Izgraditi i testirati automatizirane i interaktivne MCP klijente

## MCP server za web pretraživanje

Ovaj dio uvodi arhitekturu i značajke MCP servera za web pretraživanje. Vidjet ćete kako se FastMCP i SerpAPI koriste zajedno za proširenje LLM mogućnosti s podacima s weba u stvarnom vremenu.

### Pregled

Ova implementacija sadrži četiri alata koji pokazuju MCP-ovu sposobnost sigurnog i učinkovitog upravljanja raznolikim zadacima vođenim vanjskim API-jima:

- **general_search**: Za široke rezultate pretraživanja weba
- **news_search**: Za najnovije vijesti
- **product_search**: Za podatke o proizvodima iz e-trgovine
- **qna**: Za isječke pitanja i odgovora

### Značajke
- **Primjeri koda**: Uključuje jezično specifične blokove koda za Python (i lako proširivo na druge jezike) koristeći code pivote radi jasnoće

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

Prije pokretanja klijenta, korisno je razumjeti što server radi. Datoteka [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementira MCP server, izlažući alate za pretraživanje weba, vijesti, proizvoda i Q&A integracijom sa SerpAPI-jem. Server obrađuje dolazne zahtjeve, upravlja API pozivima, parsira odgovore i vraća strukturirane rezultate klijentu.

Puni kod možete pregledati u [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Evo kratkog primjera kako server definira i registrira alat:

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

- **Integracija vanjskog API-ja**: Pokazuje sigurno upravljanje API ključevima i vanjskim zahtjevima
- **Parsiranje strukturiranih podataka**: Prikazuje kako transformirati API odgovore u formate pogodne za LLM
- **Upravljanje pogreškama**: Robusno upravljanje pogreškama s odgovarajućim zapisivanjem
- **Interaktivni klijent**: Uključuje automatizirane testove i interaktivni način rada za testiranje
- **Upravljanje kontekstom**: Koristi MCP Context za zapisivanje i praćenje zahtjeva

## Preduvjeti

Prije nego što započnete, provjerite je li vaše okruženje pravilno postavljeno slijedeći ove korake. To će osigurati da su sve ovisnosti instalirane i da su vaši API ključevi ispravno konfigurirani za nesmetan razvoj i testiranje.

- Python 3.8 ili noviji
- SerpAPI API ključ (registrirajte se na [SerpAPI](https://serpapi.com/) - dostupna je besplatna razina)

## Instalacija

Za početak, slijedite ove korake za postavljanje okruženja:

1. Instalirajte ovisnosti koristeći uv (preporučeno) ili pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Kreirajte `.env` datoteku u korijenu projekta s vašim SerpAPI ključem:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Korištenje

MCP server za web pretraživanje je glavna komponenta koja izlaže alate za pretraživanje weba, vijesti, proizvoda i Q&A integracijom sa SerpAPI-jem. Server obrađuje dolazne zahtjeve, upravlja API pozivima, parsira odgovore i vraća strukturirane rezultate klijentu.

Puni kod možete pregledati u [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Pokretanje servera

Za pokretanje MCP servera koristite sljedeću naredbu:

```bash
python server.py
```

Server će raditi kao MCP server baziran na stdio-u kojem se klijent može izravno povezati.

### Načini rada klijenta

Klijent (`client.py`) podržava dva načina rada za interakciju s MCP serverom:

- **Normalni način**: Pokreće automatizirane testove koji koriste sve alate i provjeravaju njihove odgovore. Korisno za brzo provjeravanje ispravnosti servera i alata.
- **Interaktivni način**: Pokreće izbornik u kojem možete ručno birati i pozivati alate, unositi vlastite upite i vidjeti rezultate u stvarnom vremenu. Idealno za istraživanje mogućnosti servera i eksperimentiranje s različitim unosima.

Puni kod možete pregledati u [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Pokretanje klijenta

Za pokretanje automatiziranih testova (ovo će automatski pokrenuti server):

```bash
python client.py
```

Ili pokrenite u interaktivnom načinu:

```bash
python client.py --interactive
```

### Testiranje različitim metodama

Postoji nekoliko načina za testiranje i interakciju s alatima koje server pruža, ovisno o vašim potrebama i radnom tijeku.

#### Pisanje vlastitih test skripti s MCP Python SDK-om
Također možete izraditi vlastite test skripte koristeći MCP Python SDK:

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

U ovom kontekstu, "test skripta" znači prilagođeni Python program koji pišete da djeluje kao klijent MCP servera. Umjesto formalnog jedinicnog testa, ova skripta vam omogućuje programsku vezu sa serverom, pozivanje bilo kojeg od njegovih alata s parametrima koje odaberete i pregled rezultata. Ovaj pristup je koristan za:
- Prototipiranje i eksperimentiranje s pozivima alata
- Provjeru kako server reagira na različite unose
- Automatizaciju ponovljenih poziva alata
- Izgradnju vlastitih radnih tokova ili integracija na vrhu MCP servera

Test skripte možete koristiti za brzo isprobavanje novih upita, otklanjanje pogrešaka u ponašanju alata ili kao polaznu točku za napredniju automatizaciju. Ispod je primjer kako koristiti MCP Python SDK za izradu takve skripte:

## Opisi alata

Možete koristiti sljedeće alate koje server pruža za izvođenje različitih vrsta pretraživanja i upita. Svaki alat je opisan s parametrima i primjerom korištenja.

Ovaj dio daje detalje o svakom dostupnom alatu i njihovim parametrima.

### general_search

Izvodi opće pretraživanje weba i vraća formatirane rezultate.

**Kako pozvati ovaj alat:**

`general_search` možete pozvati iz vlastite skripte koristeći MCP Python SDK ili interaktivno koristeći Inspector ili interaktivni način rada klijenta. Evo primjera koda koristeći SDK:

# [Python primjer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, u interaktivnom načinu odaberite `general_search` iz izbornika i unesite upit kada se to zatraži.

**Parametri:**
- `query` (string): Upit za pretraživanje

**Primjer zahtjeva:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Pretražuje najnovije vijesti povezane s upitom.

**Kako pozvati ovaj alat:**

`news_search` možete pozvati iz vlastite skripte koristeći MCP Python SDK ili interaktivno koristeći Inspector ili interaktivni način rada klijenta. Evo primjera koda koristeći SDK:

# [Python primjer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, u interaktivnom načinu odaberite `news_search` iz izbornika i unesite upit kada se to zatraži.

**Parametri:**
- `query` (string): Upit za pretraživanje

**Primjer zahtjeva:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Pretražuje proizvode koji odgovaraju upitu.

**Kako pozvati ovaj alat:**

`product_search` možete pozvati iz vlastite skripte koristeći MCP Python SDK ili interaktivno koristeći Inspector ili interaktivni način rada klijenta. Evo primjera koda koristeći SDK:

# [Python primjer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, u interaktivnom načinu odaberite `product_search` iz izbornika i unesite upit kada se to zatraži.

**Parametri:**
- `query` (string): Upit za pretraživanje proizvoda

**Primjer zahtjeva:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Daje izravne odgovore na pitanja iz tražilica.

**Kako pozvati ovaj alat:**

`qna` možete pozvati iz vlastite skripte koristeći MCP Python SDK ili interaktivno koristeći Inspector ili interaktivni način rada klijenta. Evo primjera koda koristeći SDK:

# [Python primjer](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativno, u interaktivnom načinu odaberite `qna` iz izbornika i unesite pitanje kada se to zatraži.

**Parametri:**
- `question` (string): Pitanje na koje tražite odgovor

**Primjer zahtjeva:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalji koda

Ovaj dio pruža isječke koda i reference za implementacije servera i klijenta.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Pogledajte [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) i [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) za potpune detalje implementacije.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Napredni koncepti u ovoj lekciji

Prije nego što počnete graditi, evo nekoliko važnih naprednih koncepata koji će se pojavljivati kroz ovo poglavlje. Razumijevanje ovih pomoći će vam da lakše pratite, čak i ako su vam novi:

- **Orkestracija više alata**: To znači pokretanje nekoliko različitih alata (poput web pretraživanja, pretraživanja vijesti, pretraživanja proizvoda i Q&A) unutar jednog MCP servera. Omogućuje vašem serveru da obrađuje razne zadatke, ne samo jedan.
- **Upravljanje ograničenjima API-ja**: Mnogi vanjski API-ji (poput SerpAPI) ograničavaju koliko zahtjeva možete poslati u određenom vremenu. Dobar kod provjerava ta ograničenja i lijepo ih obrađuje, tako da vaša aplikacija ne padne ako dosegnete limit.
- **Parsiranje strukturiranih podataka**: Odgovori API-ja često su složeni i ugniježđeni. Ovaj koncept se odnosi na pretvaranje tih odgovora u čiste, lako upotrebljive formate koji su pogodni za LLM ili druge programe.
- **Oporavak od pogrešaka**: Ponekad stvari krenu po zlu — možda mreža zakaže ili API ne vrati ono što očekujete. Oporavak od pogrešaka znači da vaš kod može upravljati tim problemima i i dalje pružiti korisne povratne informacije, umjesto da se sruši.
- **Validacija parametara**: Radi se o provjeri da su svi ulazi u vaše alate ispravni i sigurni za korištenje. Uključuje postavljanje zadane vrijednosti i provjeru tipova, što pomaže u sprječavanju grešaka i zabune.

Ovaj dio pomoći će vam dijagnosticirati i riješiti uobičajene probleme na koje možete naići dok radite s MCP serverom za web pretraživanje. Ako naiđete na pogreške ili neočekivano ponašanje, ovaj odjeljak za rješavanje problema nudi rješenja za najčešće probleme. Pregledajte ove savjete prije traženja dodatne pomoći — često brzo riješe problem.

## Rješavanje problema

Prilikom rada s MCP serverom za web pretraživanje, povremeno se mogu pojaviti problemi — to je normalno pri razvoju s vanjskim API-jima i novim alatima. Ovaj odjeljak nudi praktična rješenja za najčešće probleme, kako biste se brzo vratili na pravi put. Ako naiđete na pogrešku, započnite ovdje: savjeti u nastavku rješavaju probleme s kojima se većina korisnika susreće i često mogu riješiti vaš problem bez dodatne pomoći.

### Česti problemi

Ispod su neki od najčešćih problema na koje korisnici nailaze, zajedno s jasnim objašnjenjima i koracima za njihovo rješavanje:

1. **Nedostaje SERPAPI_KEY u .env datoteci**
   - Ako vidite pogrešku `SERPAPI_KEY environment variable not found`, to znači da vaša aplikacija ne može pronaći API ključ potreban za pristup SerpAPI-ju. Da biste to popravili, kreirajte datoteku `.env` u korijenu projekta (ako već ne postoji) i dodajte redak poput `SERPAPI_KEY=your_serpapi_key_here`. Obavezno zamijenite `your_serpapi_key_here` stvarnim ključem s SerpAPI web stranice.

2. **Pogreške "Module not found"**
   - Pogreške poput `ModuleNotFoundError: No module named 'httpx'` znače da nedostaje potrebni Python paket. To se obično događa ako niste instalirali sve ovisnosti. Da biste to riješili, pokrenite `pip install -r requirements.txt` u terminalu da instalirate sve što vaš projekt treba.

3. **Problemi s povezivanjem**
   - Ako dobijete pogrešku poput `Error during client execution`, često to znači da se klijent ne može povezati sa serverom ili server ne radi kako se očekuje. Provjerite jesu li klijent i server kompatibilne verzije i da je `server.py` prisutan i pokrenut u ispravnom direktoriju. Ponovno pokretanje servera i klijenta također može pomoći.

4. **Pogreške SerpAPI-ja**
   - Poruka `Search API returned error status: 401` znači da vaš SerpAPI ključ nedostaje, nije ispravan ili je istekao. Posjetite svoj SerpAPI nadzorni panel, provjerite ključ i po potrebi ažurirajte `.env` datoteku. Ako je ključ ispravan, ali i dalje vidite ovu pogrešku, provjerite jeste li potrošili kvotu besplatne razine.

### Debug način rada

Po defaultu, aplikacija zapisuje samo važne informacije. Ako želite vidjeti više detalja o tome što se događa (npr. za dijagnosticiranje složenih problema), možete uključiti DEBUG način rada. To će vam pokazati puno više o svakom koraku koji aplikacija poduzima.

**Primjer: Normalni ispis**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Primjer: DEBUG ispis**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Primijetite kako DEBUG način uključuje dodatne retke o HTTP zahtjevima, odgovorima i drugim internim detaljima. Ovo može biti vrlo korisno za rješavanje problema.
Za uključivanje DEBUG moda, postavite razinu zapisivanja na DEBUG na vrhu vašeg `client.py` ili `server.py`:

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

## Što slijedi

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
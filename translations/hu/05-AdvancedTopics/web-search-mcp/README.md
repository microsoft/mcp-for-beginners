# Lecke: Webes kereső MCP szerver építése

Ez a fejezet bemutatja, hogyan építhetünk valós AI ügynököt, amely külső API-kkal integrálódik, különféle adatokat kezel, hibákat kezel, és több eszközt koordinál – mindezt éles környezetbe alkalmas formában. Megismerheted:

- **Hitelesítést igénylő külső API-k integrálása**
- **Különböző adat típusok kezelése több végpontról**
- **Robosztus hibakezelési és naplózási stratégiák**
- **Több eszköz egy szerveren belüli összehangolása**

A végére gyakorlati tapasztalatot szerzel olyan mintákkal és bevált gyakorlatokkal, amelyek elengedhetetlenek fejlett AI és LLM-alapú alkalmazásokhoz.

## Bevezetés

Ebben a leckében megtanulod, hogyan építs egy fejlett MCP szervert és klienst, amely valós idejű webes adatokkal bővíti az LLM képességeit a SerpAPI segítségével. Ez kulcsfontosságú készség dinamikus AI ügynökök fejlesztéséhez, amelyek naprakész információkat tudnak lekérni a webről.

## Tanulási célok

A lecke végére képes leszel:

- Biztonságosan integrálni külső API-kat (például SerpAPI) egy MCP szerverbe
- Több eszközt megvalósítani webes, hírek, termékkeresés és kérdés-válasz funkciókra
- Strukturált adatokat feldolgozni és formázni LLM-fogyasztásra
- Hatékonyan kezelni hibákat és API-korlátozásokat
- Automatikus és interaktív MCP klienseket építeni és tesztelni

## Webes kereső MCP szerver

Ebben a részben bemutatjuk a Webes kereső MCP szerver architektúráját és funkcióit. Meglátod, hogyan használható együtt a FastMCP és a SerpAPI, hogy valós idejű webes adatokkal bővítsék az LLM képességeit.

### Áttekintés

Ez a megvalósítás négy eszközt tartalmaz, amelyek bemutatják az MCP képességét különféle, külső API-k által vezérelt feladatok biztonságos és hatékony kezelésére:

- **general_search**: Általános webes kereséshez
- **news_search**: Legfrissebb hírekhez
- **product_search**: E-kereskedelmi adatokhoz
- **qna**: Kérdés-válasz részletekhez

### Funkciók
- **Kódpéldák**: Nyelvspecifikus kódrészletek Pythonhoz (és könnyen bővíthető más nyelvekre), kód pivotokkal az átláthatóságért

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

A kliens futtatása előtt hasznos megérteni, mit csinál a szerver. A [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) fájl valósítja meg az MCP szervert, amely eszközöket tesz elérhetővé webes, hírek, termékkeresés és kérdés-válasz funkciókra a SerpAPI integrációján keresztül. Kezeli a bejövő kéréseket, API hívásokat menedzsel, válaszokat elemzi, és strukturált eredményeket ad vissza a kliensnek.

A teljes megvalósítást megtekintheted a [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) fájlban.

Íme egy rövid példa arra, hogyan definiál és regisztrál egy eszközt a szerver:

### Python szerver

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

- **Külső API integráció**: Biztonságos API kulcs kezelés és külső kérések bemutatása
- **Strukturált adat feldolgozás**: API válaszok átalakítása LLM-barát formátumra
- **Hibakezelés**: Robosztus hibakezelés megfelelő naplózással
- **Interaktív kliens**: Automatikus tesztek és interaktív mód a teszteléshez
- **Kontekstus kezelés**: MCP Context használata naplózáshoz és kéréskövetéshez

## Előfeltételek

Mielőtt elkezdenéd, győződj meg róla, hogy a környezeted megfelelően be van állítva az alábbi lépések követésével. Ez biztosítja, hogy minden függőség telepítve legyen, és az API kulcsaid helyesen legyenek konfigurálva a zökkenőmentes fejlesztéshez és teszteléshez.

- Python 3.8 vagy újabb
- SerpAPI API kulcs (Regisztrálj a [SerpAPI](https://serpapi.com/) oldalon – ingyenes csomag elérhető)

## Telepítés

A környezet beállításához kövesd az alábbi lépéseket:

1. Telepítsd a függőségeket uv-vel (ajánlott) vagy pip-pel:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Hozz létre egy `.env` fájlt a projekt gyökerében a SerpAPI kulcsoddal:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Használat

A Webes kereső MCP szerver az a központi komponens, amely eszközöket tesz elérhetővé webes, hírek, termékkeresés és kérdés-válasz funkciókra a SerpAPI integrációján keresztül. Kezeli a bejövő kéréseket, API hívásokat menedzsel, válaszokat elemzi, és strukturált eredményeket ad vissza a kliensnek.

A teljes megvalósítást megtekintheted a [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) fájlban.

### A szerver indítása

Az MCP szerver indításához használd a következő parancsot:

```bash
python server.py
```

A szerver stdio-alapú MCP szerverként fut, amelyhez a kliens közvetlenül csatlakozhat.

### Kliens módok

A kliens (`client.py`) két módot támogat az MCP szerverrel való interakcióhoz:

- **Normál mód**: Automatikus teszteket futtat, amelyek az összes eszközt kipróbálják és ellenőrzik a válaszokat. Ez gyors ellenőrzésre alkalmas, hogy a szerver és az eszközök megfelelően működnek-e.
- **Interaktív mód**: Menüvezérelt felületet indít, ahol manuálisan választhatsz eszközt, adhatsz meg egyéni lekérdezéseket, és valós időben láthatod az eredményeket. Ez ideális a szerver képességeinek felfedezéséhez és különböző bemenetek kipróbálásához.

A teljes megvalósítást megtekintheted a [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) fájlban.

### A kliens futtatása

Az automatikus tesztek futtatásához (ez automatikusan elindítja a szervert is):

```bash
python client.py
```

Vagy indítsd interaktív módban:

```bash
python client.py --interactive
```

### Tesztelés különböző módszerekkel

Számos módon tesztelheted és használhatod az eszközöket, attól függően, mire van szükséged és milyen a munkafolyamatod.

#### Egyedi teszt szkriptek írása az MCP Python SDK-val
Saját teszt szkripteket is készíthetsz az MCP Python SDK használatával:

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

Ebben az esetben a "teszt szkript" egy egyedi Python programot jelent, amelyet kliensként írsz az MCP szerverhez. Nem formális egységteszt, hanem egy olyan szkript, amely programozottan csatlakozik a szerverhez, meghívja bármelyik eszközt a választott paraméterekkel, és megvizsgálja az eredményeket. Ez hasznos:

- Eszközhívások prototípusához és kísérletezéshez
- A szerver válaszainak validálásához különböző bemenetekre
- Ismétlődő eszközhívások automatizálásához
- Saját munkafolyamatok vagy integrációk építéséhez az MCP szerverre építve

Teszt szkriptekkel gyorsan kipróbálhatsz új lekérdezéseket, hibakereshetsz, vagy akár fejlettebb automatizálás kiindulópontjaként is használhatod. Az alábbi példa bemutatja, hogyan használhatod az MCP Python SDK-t egy ilyen szkript létrehozásához:

## Eszközök leírása

A szerver által biztosított eszközöket különböző keresések és lekérdezések végrehajtására használhatod. Az egyes eszközöket az alábbiakban ismertetjük paramétereikkel és példákkal.

Ez a rész részletezi az elérhető eszközöket és azok paramétereit.

### general_search

Általános webes keresést végez és formázott eredményeket ad vissza.

**Hogyan hívd meg ezt az eszközt:**

A `general_search` eszközt meghívhatod saját szkriptedből az MCP Python SDK-val, vagy interaktívan az Inspectorral vagy az interaktív kliens módban. Íme egy kód példa az SDK használatával:

# [Python példa](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatívaként interaktív módban válaszd a `general_search` opciót a menüből, és írd be a lekérdezést, amikor kéri.

**Paraméterek:**
- `query` (string): A keresési lekérdezés

**Példa kérés:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Legfrissebb hírek keresése egy adott lekérdezéshez kapcsolódóan.

**Hogyan hívd meg ezt az eszközt:**

A `news_search` eszközt meghívhatod saját szkriptedből az MCP Python SDK-val, vagy interaktívan az Inspectorral vagy az interaktív kliens módban. Íme egy kód példa az SDK használatával:

# [Python példa](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatívaként interaktív módban válaszd a `news_search` opciót a menüből, és írd be a lekérdezést, amikor kéri.

**Paraméterek:**
- `query` (string): A keresési lekérdezés

**Példa kérés:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Termékek keresése a lekérdezés alapján.

**Hogyan hívd meg ezt az eszközt:**

A `product_search` eszközt meghívhatod saját szkriptedből az MCP Python SDK-val, vagy interaktívan az Inspectorral vagy az interaktív kliens módban. Íme egy kód példa az SDK használatával:

# [Python példa](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatívaként interaktív módban válaszd a `product_search` opciót a menüből, és írd be a lekérdezést, amikor kéri.

**Paraméterek:**
- `query` (string): A termékkeresési lekérdezés

**Példa kérés:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Közvetlen válaszokat ad kérdésekre keresőmotorokból.

**Hogyan hívd meg ezt az eszközt:**

A `qna` eszközt meghívhatod saját szkriptedből az MCP Python SDK-val, vagy interaktívan az Inspectorral vagy az interaktív kliens módban. Íme egy kód példa az SDK használatával:

# [Python példa](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternatívaként interaktív módban válaszd a `qna` opciót a menüből, és írd be a kérdésed, amikor kéri.

**Paraméterek:**
- `question` (string): A kérdés, amire választ keresel

**Példa kérés:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Kód részletek

Ez a rész kódrészleteket és hivatkozásokat tartalmaz a szerver és kliens megvalósításához.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

A teljes megvalósításhoz lásd a [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) és [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) fájlokat.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Fejlett fogalmak ebben a leckében

Mielőtt elkezdenéd az építést, itt van néhány fontos fejlett fogalom, amelyek végigkísérik ezt a fejezetet. Ezek megértése segít követni az anyagot, még ha újak is számodra:

- **Több eszköz összehangolása**: Ez azt jelenti, hogy egy MCP szerveren belül több különböző eszközt futtatsz (például webes keresés, hírek keresése, termékkeresés és kérdés-válasz). Ez lehetővé teszi, hogy a szerver sokféle feladatot kezeljen, ne csak egyet.
- **API-korlátozások kezelése**: Sok külső API (például SerpAPI) korlátozza, hogy mennyi kérést tehetsz egy adott idő alatt. A jó kód ellenőrzi ezeket a korlátokat és megfelelően kezeli őket, hogy az alkalmazás ne omoljon össze, ha eléri a limitet.
- **Strukturált adat feldolgozás**: Az API válaszok gyakran összetettek és beágyazottak. Ez a fogalom arról szól, hogyan alakítsuk át ezeket a válaszokat tiszta, könnyen használható formátumokká, amelyek barátságosak az LLM-ek vagy más programok számára.
- **Hibahelyreállítás**: Néha hibák lépnek fel – például hálózati probléma vagy az API nem a várt választ adja. A hibahelyreállítás azt jelenti, hogy a kód kezeli ezeket a problémákat, és hasznos visszajelzést ad, ahelyett, hogy összeomlana.
- **Paraméter ellenőrzés**: Ez arról szól, hogy minden bemenetet az eszközeidhez helyesen és biztonságosan ellenőrzünk. Ide tartozik az alapértelmezett értékek beállítása és a típusok helyességének biztosítása, ami segít megelőzni hibákat és félreértéseket.

Ez a rész segít diagnosztizálni és megoldani a Webes kereső MCP szerverrel kapcsolatos gyakori problémákat. Ha hibába ütközöl vagy váratlan viselkedést tapasztalsz, ez a hibakeresési rész megoldásokat kínál a leggyakoribb problémákra. Nézd át ezeket a tippeket, mielőtt további segítséget kérnél – gyakran gyorsan megoldják a gondokat.

## Hibakeresés

A Webes kereső MCP szerver használata közben időnként problémákba ütközhetsz – ez normális, amikor külső API-kkal és új eszközökkel dolgozol. Ez a rész gyakorlati megoldásokat kínál a leggyakoribb problémákra, hogy gyorsan visszatérhess a munkához. Ha hibát tapasztalsz, innen érdemes kezdeni: az alábbi tippek a legtöbb felhasználó által tapasztalt problémákat fedik le, és gyakran megoldják a gondokat további segítség nélkül.

### Gyakori problémák

Az alábbiakban a leggyakoribb problémák és azok egyértelmű magyarázatai, valamint megoldási lépései találhatók:

1. **Hiányzó SERPAPI_KEY a .env fájlban**
   - Ha a `SERPAPI_KEY environment variable not found` hiba jelenik meg, az azt jelenti, hogy az alkalmazás nem találja a SerpAPI eléréséhez szükséges API kulcsot. Javításhoz hozz létre egy `.env` fájlt a projekt gyökerében (ha még nincs), és adj hozzá egy sort így: `SERPAPI_KEY=your_serpapi_key_here`. Cseréld ki a `your_serpapi_key_here` részt a SerpAPI weboldalán kapott valódi kulcsodra.

2. **Modul nem található hibák**
   - Olyan hibák, mint `ModuleNotFoundError: No module named 'httpx'` azt jelzik, hogy egy szükséges Python csomag hiányzik. Ez általában akkor fordul elő, ha nem telepítetted az összes függőséget. Megoldáshoz futtasd a `pip install -r requirements.txt` parancsot a terminálban, hogy
A DEBUG mód engedélyezéséhez állítsd a naplózási szintet DEBUG-ra a `client.py` vagy `server.py` fájl elején:

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

## Mi következik

- [5.10 Valós idejű adatfolyam](../mcp-realtimestreaming/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
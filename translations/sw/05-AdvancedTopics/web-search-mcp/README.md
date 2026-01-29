# Somo: Kujenga Server ya Utafutaji wa Mtandao ya MCP

Sura hii inaonyesha jinsi ya kujenga wakala halisi wa AI anayejumuisha API za nje, kushughulikia aina mbalimbali za data, kusimamia makosa, na kuendesha zana nyingi—yote haya kwa muundo unaotumika katika uzalishaji. Utaona:

- **Ushirikiano na API za nje zinazohitaji uthibitishaji**
- **Kushughulikia aina mbalimbali za data kutoka vyanzo vingi**
- **Mikakati thabiti ya kushughulikia makosa na kurekodi matukio**
- **Uendeshaji wa zana nyingi katika server moja**

Mwisho wa somo, utakuwa na uzoefu wa vitendo na mifumo bora muhimu kwa programu za AI na LLM zilizoendelea.

## Utangulizi

Katika somo hili, utajifunza jinsi ya kujenga server na mteja wa MCP wa hali ya juu unaoongeza uwezo wa LLM kwa data za mtandao za wakati halisi kwa kutumia SerpAPI. Hii ni ujuzi muhimu kwa kuunda mawakala wa AI wenye uwezo wa kupata taarifa za hivi punde kutoka mtandao.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuunganisha API za nje (kama SerpAPI) kwa usalama katika server ya MCP
- Kutekeleza zana nyingi za utafutaji wa mtandao, habari, bidhaa, na maswali-jawabu
- Kuchambua na kuandaa data iliyopangwa kwa matumizi ya LLM
- Kushughulikia makosa na kusimamia viwango vya maombi ya API kwa ufanisi
- Kujenga na kujaribu wateja wa MCP wa moja kwa moja na wa mwingiliano

## Server ya Utafutaji wa Mtandao ya MCP

Sehemu hii inaelezea usanifu na sifa za Server ya Utafutaji wa Mtandao ya MCP. Utaona jinsi FastMCP na SerpAPI vinavyotumika pamoja kuongeza uwezo wa LLM kwa data za mtandao za wakati halisi.

### Muhtasari

Utekelezaji huu una zana nne zinazothibitisha uwezo wa MCP kushughulikia kazi mbalimbali zinazotegemea API za nje kwa usalama na ufanisi:

- **general_search**: Kwa matokeo ya jumla ya mtandao
- **news_search**: Kwa vichwa vya habari vya hivi karibuni
- **product_search**: Kwa data za biashara mtandao
- **qna**: Kwa vipande vya maswali na majibu

### Sifa
- **Mifano ya Msimbo**: Inajumuisha sehemu za msimbo maalum kwa lugha ya Python (na rahisi kupanuliwa kwa lugha nyingine) kwa kutumia pivoti za msimbo kwa uwazi

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

Kabla ya kuendesha mteja, ni muhimu kuelewa kazi za server. Faili la [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) lina utekelezaji wa server ya MCP, likitoa zana za utafutaji wa mtandao, habari, bidhaa, na maswali-jawabu kwa kuunganishwa na SerpAPI. Linashughulikia maombi yanayoingia, kusimamia simu za API, kuchambua majibu, na kurudisha matokeo yaliyopangwa kwa mteja.

Unaweza kupitia utekelezaji kamili katika [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Hapa kuna mfano mfupi wa jinsi server inavyofafanua na kusajili zana:

### Server ya Python

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

- **Ushirikiano wa API za Nje**: Inaonyesha jinsi ya kushughulikia kwa usalama funguo za API na maombi ya nje
- **Uchambuzi wa Data Iliyo Pangiliwa**: Inaonyesha jinsi ya kubadilisha majibu ya API kuwa muundo unaofaa kwa LLM
- **Kushughulikia Makosa**: Kushughulikia makosa kwa nguvu pamoja na kurekodi matukio ipasavyo
- **Mteja wa Mwingiliano**: Inajumuisha majaribio ya moja kwa moja na hali ya mwingiliano kwa majaribio
- **Usimamizi wa Muktadha**: Inatumia MCP Context kwa ajili ya kurekodi na kufuatilia maombi

## Mahitaji ya Awali

Kabla ya kuanza, hakikisha mazingira yako yamewekwa ipasavyo kwa kufuata hatua hizi. Hii itahakikisha kuwa utegemezi wote umewekwa na funguo zako za API zimepangwa kwa usahihi kwa maendeleo na majaribio bila matatizo.

- Python 3.8 au zaidi
- Funguo ya API ya SerpAPI (Jisajili kwenye [SerpAPI](https://serpapi.com/) - kiwango cha bure kinapatikana)

## Usanidi

Ili kuanza, fuata hatua hizi kuweka mazingira yako:

1. Sakinisha utegemezi kwa kutumia uv (inapendekezwa) au pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Tengeneza faili `.env` kwenye mzizi wa mradi na funguo yako ya SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Matumizi

Server ya Utafutaji wa Mtandao ya MCP ni sehemu kuu inayotoa zana za utafutaji wa mtandao, habari, bidhaa, na maswali-jawabu kwa kuunganishwa na SerpAPI. Inashughulikia maombi yanayoingia, kusimamia simu za API, kuchambua majibu, na kurudisha matokeo yaliyopangwa kwa mteja.

Unaweza kupitia utekelezaji kamili katika [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Kuendesha Server

Kuanzisha server ya MCP, tumia amri ifuatayo:

```bash
python server.py
```

Server itaendesha kama server ya MCP inayotumia stdio ambayo mteja anaweza kuunganishwa moja kwa moja.

### Hali za Mteja

Mteja (`client.py`) una hali mbili za kuingiliana na server ya MCP:

- **Hali ya kawaida**: Inaendesha majaribio ya moja kwa moja yanayojaribu zana zote na kuthibitisha majibu yao. Hii ni muhimu kwa kuangalia haraka kama server na zana zinafanya kazi kama inavyotarajiwa.
- **Hali ya mwingiliano**: Inaanzisha kiolesura cha menyu ambapo unaweza kuchagua na kuitisha zana kwa mikono, kuingiza maswali maalum, na kuona matokeo kwa wakati halisi. Hii ni bora kwa kuchunguza uwezo wa server na kujaribu pembejeo tofauti.

Unaweza kupitia utekelezaji kamili katika [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Kuendesha Mteja

Kuendesha majaribio ya moja kwa moja (hii itaanzisha server moja kwa moja):

```bash
python client.py
```

Au endesha katika hali ya mwingiliano:

```bash
python client.py --interactive
```

### Kupima kwa Njia Mbali Mbali

Kuna njia kadhaa za kupima na kuingiliana na zana zinazotolewa na server, kulingana na mahitaji na mtiririko wako wa kazi.

#### Kuandika Skripti Maalum za Majaribio kwa kutumia MCP Python SDK
Pia unaweza kujenga skripti zako za majaribio kwa kutumia MCP Python SDK:

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

Katika muktadha huu, "skripti ya majaribio" inamaanisha programu maalum ya Python unayoandika ili itumike kama mteja wa server ya MCP. Badala ya kuwa jaribio rasmi la kitengo, skripti hii inakuwezesha kuunganishwa na server kwa njia ya programu, kuitisha zana yoyote na vigezo unavyotaka, na kuchunguza matokeo. Njia hii ni muhimu kwa:
- Kuunda na kujaribu kuitisha zana
- Kuhakiki jinsi server inavyotenda kwa pembejeo tofauti
- Kuendesha kwa urahisi kuitisha zana mara kwa mara
- Kujenga mtiririko wako wa kazi au ushirikiano juu ya server ya MCP

Unaweza kutumia skripti za majaribio kujaribu maswali mapya haraka, kutatua tabia za zana, au hata kama msingi wa otomatiki zaidi. Hapa chini ni mfano wa jinsi ya kutumia MCP Python SDK kuunda skripti kama hiyo:

## Maelezo ya Zana

Unaweza kutumia zana zifuatazo zinazotolewa na server kufanya aina tofauti za utafutaji na maswali. Kila zana imeelezewa hapa chini pamoja na vigezo na mfano wa matumizi.

Sehemu hii inatoa maelezo kuhusu kila zana inayopatikana na vigezo vyake.

### general_search

Hufanya utafutaji wa jumla wa mtandao na kurudisha matokeo yaliyopangwa.

**Jinsi ya kuitisha zana hii:**

Unaweza kuitisha `general_search` kutoka kwenye skripti yako kwa kutumia MCP Python SDK, au kwa njia ya mwingiliano kwa kutumia Inspector au hali ya mteja wa mwingiliano. Hapa kuna mfano wa msimbo ukitumia SDK:

# [Mfano wa Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Vinginevyo, katika hali ya mwingiliano, chagua `general_search` kutoka kwenye menyu na ingiza swali lako unapoulizwa.

**Vigezo:**
- `query` (kamba): Swali la utafutaji

**Mfano wa Ombi:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Hufanya utafutaji wa makala za habari za hivi karibuni zinazohusiana na swali.

**Jinsi ya kuitisha zana hii:**

Unaweza kuitisha `news_search` kutoka kwenye skripti yako kwa kutumia MCP Python SDK, au kwa njia ya mwingiliano kwa kutumia Inspector au hali ya mteja wa mwingiliano. Hapa kuna mfano wa msimbo ukitumia SDK:

# [Mfano wa Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Vinginevyo, katika hali ya mwingiliano, chagua `news_search` kutoka kwenye menyu na ingiza swali lako unapoulizwa.

**Vigezo:**
- `query` (kamba): Swali la utafutaji

**Mfano wa Ombi:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Hufanya utafutaji wa bidhaa zinazolingana na swali.

**Jinsi ya kuitisha zana hii:**

Unaweza kuitisha `product_search` kutoka kwenye skripti yako kwa kutumia MCP Python SDK, au kwa njia ya mwingiliano kwa kutumia Inspector au hali ya mteja wa mwingiliano. Hapa kuna mfano wa msimbo ukitumia SDK:

# [Mfano wa Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Vinginevyo, katika hali ya mwingiliano, chagua `product_search` kutoka kwenye menyu na ingiza swali lako unapoulizwa.

**Vigezo:**
- `query` (kamba): Swali la utafutaji wa bidhaa

**Mfano wa Ombi:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Hupata majibu ya moja kwa moja kwa maswali kutoka kwa injini za utafutaji.

**Jinsi ya kuitisha zana hii:**

Unaweza kuitisha `qna` kutoka kwenye skripti yako kwa kutumia MCP Python SDK, au kwa njia ya mwingiliano kwa kutumia Inspector au hali ya mteja wa mwingiliano. Hapa kuna mfano wa msimbo ukitumia SDK:

# [Mfano wa Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Vinginevyo, katika hali ya mwingiliano, chagua `qna` kutoka kwenye menyu na ingiza swali lako unapoulizwa.

**Vigezo:**
- `question` (kamba): Swali unalotaka kupata jibu

**Mfano wa Ombi:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Maelezo ya Msimbo

Sehemu hii inatoa vipande vya msimbo na marejeleo kwa utekelezaji wa server na mteja.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Tazama [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) na [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) kwa maelezo kamili ya utekelezaji.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Dhana za Juu Katika Somo Hili

Kabla ya kuanza kujenga, hapa kuna dhana muhimu za juu zitakazojitokeza katika sura hii. Kuelewa hizi kutakusaidia kufuatilia kwa urahisi, hata kama ni mara yako ya kwanza:

- **Uendeshaji wa Zana Nyingi**: Hii inamaanisha kuendesha zana tofauti kadhaa (kama utafutaji wa mtandao, habari, bidhaa, na maswali-jawabu) ndani ya server moja ya MCP. Inaruhusu server yako kushughulikia kazi mbalimbali, siyo moja tu.
- **Kushughulikia Viwango vya Maombi ya API**: API nyingi za nje (kama SerpAPI) zinaweka kikomo cha maombi unayoweza kutuma kwa muda fulani. Msimbo mzuri huangalia vikwazo hivi na kushughulikia kwa busara, ili programu yako isivunjike ukipita kikomo.
- **Uchambuzi wa Data Iliyo Pangiliwa**: Majibu ya API mara nyingi ni magumu na yamepangwa kwa kina. Dhana hii ni kuhusu kubadilisha majibu hayo kuwa muundo safi, rahisi kutumia unaofaa kwa LLM au programu nyingine.
- **Urejeshaji wa Makosa**: Wakati mwingine mambo hayendi sawa—labda mtandao unashindwa, au API hairejee kile unachotarajia. Urejeshaji wa makosa unamaanisha msimbo wako unaweza kushughulikia matatizo haya na bado kutoa mrejesho mzuri, badala ya kuanguka.
- **Uhakiki wa Vigezo**: Hii ni kuhusu kuhakikisha pembejeo zote kwa zana zako ni sahihi na salama kutumia. Inajumuisha kuweka thamani za msingi na kuhakikisha aina za data ni sahihi, ambayo husaidia kuzuia hitilafu na mkanganyiko.

Sehemu hii itakusaidia kugundua na kutatua matatizo ya kawaida unayoweza kukutana nayo unapotumia Server ya Utafutaji wa Mtandao ya MCP. Ukikumbana na makosa au tabia zisizotarajiwa, sehemu hii ya utatuzi itatoa suluhisho la matatizo yanayojirudia mara nyingi. Pitia vidokezo hivi kabla ya kutafuta msaada zaidi—mara nyingi hutatua matatizo haraka.

## Utatuzi wa Matatizo

Unapofanya kazi na Server ya Utafutaji wa Mtandao ya MCP, mara nyingine unaweza kukutana na matatizo—hii ni kawaida wakati wa kuendeleza kwa kutumia API za nje na zana mpya. Sehemu hii inatoa suluhisho za vitendo kwa matatizo yanayojirudia mara nyingi, ili urudi kwenye kazi haraka. Ukikumbana na kosa, anza hapa: vidokezo hapa chini vinashughulikia matatizo yanayokumba watumiaji wengi na mara nyingi vinaweza kutatua tatizo lako bila msaada wa ziada.

### Matatizo ya Kawaida

Hapa chini ni baadhi ya matatizo yanayojirudia mara nyingi watumiaji wanayokumbana nayo, pamoja na maelezo wazi na hatua za kuyatatua:

1. **Kosa la kukosa SERPAPI_KEY katika faili `.env`**
   - Ikiwa unaona kosa `SERPAPI_KEY environment variable not found`, inamaanisha programu yako haipati funguo ya API inayohitajika kufikia SerpAPI. Ili kutatua, tengeneza faili liitwalo `.env` kwenye mzizi wa mradi (ikiwa halipo) na ongeza mstari kama `SERPAPI_KEY=funguo_yako_ya_serpapi_hapa`. Hakikisha unabadilisha `funguo_yako_ya_serpapi_hapa` na funguo halisi kutoka tovuti ya SerpAPI.

2. **Makosa ya moduli isiyopatikana**
   - Makosa kama `ModuleNotFoundError: No module named 'httpx'` yanaonyesha kuwa kifurushi cha Python kinachohitajika hakijasakinishwa. Hii kawaida hutokea kama hujasakinisha utegemezi wote. Ili kutatua, endesha `pip install -r requirements.txt` kwenye terminal yako kusakinisha kila kitu mradi unahitaji.

3. **Matatizo ya muunganisho**
   - Ikiwa unapata kosa kama `Error during client execution`, mara nyingi inamaanisha mteja hawezi kuunganishwa na server, au server haifanyi kazi kama inavyotarajiwa. Hakikisha mteja na server ni matoleo yanayolingana, na `server.py` ipo na inaendesha kwenye saraka sahihi. Kuanza upya server na mteja pia kunaweza kusaidia.

4. **Makosa ya SerpAPI**
   - Kuona `Search API returned error status: 401` kunamaanisha funguo yako ya SerpAPI haipo, si sahihi, au imeisha muda wake. Nenda kwenye dashibodi ya SerpAPI, hakiki funguo yako, na sasisha faili `.env` ikiwa inahitajika. Ikiwa funguo yako ni sahihi lakini bado unapata kosa hili, angalia kama kiwango chako cha bure kimeisha.

### Hali ya Ufuatiliaji (Debug Mode)

Kwa kawaida, programu huandika tu taarifa muhimu. Ikiwa unataka kuona maelezo zaidi kuhusu kinachoendelea (kwa mfano, kutatua matatizo magumu), unaweza kuwasha hali ya DEBUG. Hii itaonyesha maelezo mengi zaidi kuhusu kila hatua programu inayoichukua.

**Mfano: Matokeo ya Kawaida**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Mfano: Matokeo ya DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Angalia jinsi hali ya DEBUG inajumuisha mistari ya ziada kuhusu maombi ya HTTP, majibu, na maelezo mengine ya ndani. Hii inaweza kusaidia sana katika utatuzi wa matatizo.
Ili kuwezesha hali ya DEBUG, weka kiwango cha uandishi wa kumbukumbu kuwa DEBUG juu ya faili yako ya `client.py` au `server.py`:

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

## Nini kinachofuata

- [5.10 Uenezaji wa Muda Halisi](../mcp-realtimestreaming/README.md)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
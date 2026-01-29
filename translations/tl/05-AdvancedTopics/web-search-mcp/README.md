# Lesson: Paggawa ng Web Search MCP Server

Ipinapakita sa kabanatang ito kung paano bumuo ng isang totoong AI agent na nakakabit sa mga external API, humahawak ng iba't ibang uri ng data, nagma-manage ng mga error, at nag-oorganisa ng maraming tools—lahat sa isang production-ready na format. Makikita mo dito:

- **Pagsasama ng mga external API na nangangailangan ng authentication**
- **Pag-handle ng iba't ibang uri ng data mula sa maraming endpoints**
- **Matibay na paghawak ng error at mga estratehiya sa pag-log**
- **Pag-oorganisa ng maraming tools sa iisang server**

Sa pagtatapos, magkakaroon ka ng praktikal na karanasan sa mga pattern at best practices na mahalaga para sa mga advanced na AI at LLM-powered na aplikasyon.

## Panimula

Sa araling ito, matututuhan mo kung paano bumuo ng advanced na MCP server at client na nagpapalawak ng kakayahan ng LLM gamit ang real-time na web data gamit ang SerpAPI. Isang mahalagang kasanayan ito para makagawa ng dynamic na AI agents na nakakakuha ng pinakabagong impormasyon mula sa web.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Isama nang ligtas ang mga external API (tulad ng SerpAPI) sa isang MCP server
- Magpatupad ng maraming tools para sa web, balita, paghahanap ng produkto, at Q&A
- I-parse at i-format ang structured data para sa paggamit ng LLM
- Mag-handle ng mga error at epektibong pamahalaan ang API rate limits
- Bumuo at mag-test ng parehong automated at interactive MCP clients

## Web Search MCP Server

Ipinapakilala sa seksyong ito ang arkitektura at mga tampok ng Web Search MCP Server. Makikita mo kung paano ginagamit ang FastMCP at SerpAPI nang sabay upang palawakin ang kakayahan ng LLM gamit ang real-time na web data.

### Pangkalahatang-ideya

Ang implementasyong ito ay may apat na tools na nagpapakita ng kakayahan ng MCP na ligtas at mahusay na humawak ng iba't ibang gawain na pinapagana ng external API:

- **general_search**: Para sa malawakang resulta sa web
- **news_search**: Para sa mga pinakabagong balita
- **product_search**: Para sa datos ng e-commerce
- **qna**: Para sa mga tanong at sagot

### Mga Tampok
- **Mga Halimbawa ng Code**: May mga language-specific na code blocks para sa Python (at madaling mapalawak sa ibang mga wika) gamit ang code pivots para sa kalinawan

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

Bago patakbuhin ang client, makakatulong na maintindihan kung ano ang ginagawa ng server. Ang file na [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ay nag-iimplementa ng MCP server, na naglalantad ng mga tools para sa web, balita, paghahanap ng produkto, at Q&A sa pamamagitan ng pagsasama sa SerpAPI. Pinoproseso nito ang mga papasok na request, pinamamahalaan ang mga API call, ini-parse ang mga tugon, at ibinabalik ang mga nakaayos na resulta sa client.

Maaari mong suriin ang buong implementasyon sa [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Narito ang isang maikling halimbawa kung paano dine-define at nirehistro ng server ang isang tool:

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

- **Pagsasama ng External API**: Ipinapakita ang ligtas na paghawak ng mga API key at mga external na request
- **Pag-parse ng Structured Data**: Ipinapakita kung paano gawing LLM-friendly ang mga tugon mula sa API
- **Pag-handle ng Error**: Matibay na paghawak ng error na may angkop na pag-log
- **Interactive Client**: Kasama ang parehong automated tests at interactive mode para sa pagsusuri
- **Pamamahala ng Konteksto**: Ginagamit ang MCP Context para sa pag-log at pagsubaybay ng mga request

## Mga Kinakailangan

Bago ka magsimula, siguraduhing maayos ang pagkaka-setup ng iyong environment sa pamamagitan ng pagsunod sa mga hakbang na ito. Titiyakin nito na naka-install ang lahat ng dependencies at tama ang pagkaka-configure ng iyong mga API key para sa maayos na development at testing.

- Python 3.8 o mas mataas pa
- SerpAPI API Key (Mag-sign up sa [SerpAPI](https://serpapi.com/) - may libreng tier)

## Pag-install

Para makapagsimula, sundin ang mga hakbang na ito para i-setup ang iyong environment:

1. I-install ang mga dependencies gamit ang uv (inirerekomenda) o pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Gumawa ng `.env` file sa root ng proyekto na may iyong SerpAPI key:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Paggamit

Ang Web Search MCP Server ang pangunahing bahagi na naglalantad ng mga tools para sa web, balita, paghahanap ng produkto, at Q&A sa pamamagitan ng pagsasama sa SerpAPI. Pinoproseso nito ang mga papasok na request, pinamamahalaan ang mga API call, ini-parse ang mga tugon, at ibinabalik ang mga nakaayos na resulta sa client.

Maaari mong suriin ang buong implementasyon sa [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Pagpapatakbo ng Server

Para simulan ang MCP server, gamitin ang sumusunod na utos:

```bash
python server.py
```

Tatakbo ang server bilang stdio-based MCP server na direktang makakonekta ang client.

### Mga Mode ng Client

Sinusuportahan ng client (`client.py`) ang dalawang mode para makipag-ugnayan sa MCP server:

- **Normal mode**: Pinapatakbo ang automated tests na sinusubok ang lahat ng tools at sinusuri ang kanilang mga tugon. Kapaki-pakinabang ito para mabilisang pag-check kung gumagana nang maayos ang server at mga tools.
- **Interactive mode**: Nagsisimula ng menu-driven na interface kung saan maaari mong piliin at tawagan ang mga tools nang manu-mano, maglagay ng custom na query, at makita ang mga resulta nang real time. Mainam ito para tuklasin ang kakayahan ng server at mag-eksperimento sa iba't ibang input.

Maaari mong suriin ang buong implementasyon sa [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Pagpapatakbo ng Client

Para patakbuhin ang automated tests (awtomatikong sisimulan ang server):

```bash
python client.py
```

O patakbuhin sa interactive mode:

```bash
python client.py --interactive
```

### Pagsusuri gamit ang Iba't Ibang Paraan

May ilang paraan para subukan at makipag-ugnayan sa mga tools na ibinibigay ng server, depende sa iyong pangangailangan at workflow.

#### Pagsusulat ng Custom Test Scripts gamit ang MCP Python SDK
Maaari ka ring gumawa ng sarili mong test scripts gamit ang MCP Python SDK:

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

Sa kontekstong ito, ang "test script" ay tumutukoy sa custom na Python program na sinusulat mo upang kumilos bilang client para sa MCP server. Sa halip na isang pormal na unit test, pinapayagan ka nitong programmatically kumonekta sa server, tawagan ang alinmang tool nito gamit ang mga parameter na pipiliin mo, at suriin ang mga resulta. Kapaki-pakinabang ito para sa:
- Prototyping at pag-eksperimento sa mga tawag sa tool
- Pag-validate kung paano tumutugon ang server sa iba't ibang input
- Pag-automate ng paulit-ulit na pagtawag sa mga tool
- Paggawa ng sarili mong workflows o integrasyon sa ibabaw ng MCP server

Maaari mong gamitin ang mga test script para mabilis na subukan ang mga bagong query, i-debug ang pag-uugali ng tool, o bilang panimulang punto para sa mas advanced na automation. Narito ang isang halimbawa kung paano gamitin ang MCP Python SDK para gumawa ng ganitong script:

## Mga Paglalarawan ng Tool

Maaari mong gamitin ang mga sumusunod na tools na ibinibigay ng server upang magsagawa ng iba't ibang uri ng paghahanap at query. Bawat tool ay inilalarawan sa ibaba kasama ang mga parameter at halimbawa ng paggamit.

Ang seksyong ito ay nagbibigay ng detalye tungkol sa bawat available na tool at ang kanilang mga parameter.

### general_search

Nagsasagawa ng pangkalahatang paghahanap sa web at nagbabalik ng naka-format na mga resulta.

**Paano tawagan ang tool na ito:**

Maaari mong tawagan ang `general_search` mula sa sarili mong script gamit ang MCP Python SDK, o interaktibo gamit ang Inspector o ang interactive client mode. Narito ang isang halimbawa ng code gamit ang SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

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

Bilang alternatibo, sa interactive mode, piliin ang `general_search` mula sa menu at ilagay ang iyong query kapag na-prompt.

**Mga Parameter:**
- `query` (string): Ang query para sa paghahanap

**Halimbawa ng Request:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Naghahanap ng mga pinakabagong artikulo ng balita na may kaugnayan sa isang query.

**Paano tawagan ang tool na ito:**

Maaari mong tawagan ang `news_search` mula sa sarili mong script gamit ang MCP Python SDK, o interaktibo gamit ang Inspector o ang interactive client mode. Narito ang isang halimbawa ng code gamit ang SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

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

Bilang alternatibo, sa interactive mode, piliin ang `news_search` mula sa menu at ilagay ang iyong query kapag na-prompt.

**Mga Parameter:**
- `query` (string): Ang query para sa paghahanap

**Halimbawa ng Request:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Naghahanap ng mga produkto na tumutugma sa isang query.

**Paano tawagan ang tool na ito:**

Maaari mong tawagan ang `product_search` mula sa sarili mong script gamit ang MCP Python SDK, o interaktibo gamit ang Inspector o ang interactive client mode. Narito ang isang halimbawa ng code gamit ang SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

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

Bilang alternatibo, sa interactive mode, piliin ang `product_search` mula sa menu at ilagay ang iyong query kapag na-prompt.

**Mga Parameter:**
- `query` (string): Ang query para sa paghahanap ng produkto

**Halimbawa ng Request:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Kumuha ng direktang sagot sa mga tanong mula sa mga search engine.

**Paano tawagan ang tool na ito:**

Maaari mong tawagan ang `qna` mula sa sarili mong script gamit ang MCP Python SDK, o interaktibo gamit ang Inspector o ang interactive client mode. Narito ang isang halimbawa ng code gamit ang SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

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

Bilang alternatibo, sa interactive mode, piliin ang `qna` mula sa menu at ilagay ang iyong tanong kapag na-prompt.

**Mga Parameter:**
- `question` (string): Ang tanong na nais hanapan ng sagot

**Halimbawa ng Request:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Mga Detalye ng Code

Nagbibigay ang seksyong ito ng mga snippet ng code at mga sanggunian para sa implementasyon ng server at client.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Tingnan ang [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) at [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) para sa buong detalye ng implementasyon.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Mga Advanced na Konsepto sa Araling Ito

Bago ka magsimulang bumuo, narito ang ilang mahahalagang advanced na konsepto na lalabas sa buong kabanatang ito. Ang pag-unawa sa mga ito ay makakatulong sa iyong pagsunod, kahit na bago ka pa lamang sa mga ito:

- **Pag-oorganisa ng Maramihang Tools**: Ibig sabihin nito ay pagpapatakbo ng iba't ibang tools (tulad ng web search, news search, product search, at Q&A) sa iisang MCP server. Pinapayagan nito ang iyong server na humawak ng iba't ibang gawain, hindi lang isa.
- **Pag-handle ng API Rate Limit**: Maraming external API (tulad ng SerpAPI) ang nililimitahan kung ilang request ang maaari mong gawin sa isang takdang oras. Ang magandang code ay sinusuri ang mga limitasyong ito at maayos na hinaharap ang mga ito, para hindi masira ang iyong app kapag naabot ang limit.
- **Pag-parse ng Structured Data**: Madalas na komplikado at nested ang mga tugon mula sa API. Ang konseptong ito ay tungkol sa pag-convert ng mga tugon na iyon sa malinis at madaling gamitin na mga format na friendly sa LLM o iba pang programa.
- **Pag-recover mula sa Error**: Minsan may mga problema—maaaring pumalya ang network, o hindi ibinalik ng API ang inaasahan mo. Ang pag-recover mula sa error ay nangangahulugang kaya ng iyong code na harapin ang mga problemang ito at magbigay pa rin ng kapaki-pakinabang na feedback, sa halip na mag-crash.
- **Pag-validate ng Parameter**: Ito ay tungkol sa pagsuri na tama at ligtas gamitin ang lahat ng input sa iyong mga tools. Kasama dito ang pagtatakda ng default na mga halaga at pagtiyak na tama ang mga uri, na tumutulong maiwasan ang mga bug at kalituhan.

Ang seksyong ito ay tutulong sa iyo na matukoy at maresolba ang mga karaniwang isyu na maaaring maranasan habang nagtatrabaho sa Web Search MCP Server. Kung makaranas ka ng mga error o hindi inaasahang pag-uugali habang ginagamit ang Web Search MCP Server, nagbibigay ang seksyong ito ng mga solusyon sa mga pinakakaraniwang problema. Suriin muna ang mga tip na ito bago humingi ng karagdagang tulong—madalas ay mabilis nitong naaayos ang mga problema.

## Pag-troubleshoot

Kapag nagtatrabaho sa Web Search MCP Server, paminsan-minsan ay maaaring makaranas ka ng mga isyu—normal ito kapag nagde-develop gamit ang mga external API at bagong tools. Nagbibigay ang seksyong ito ng praktikal na mga solusyon sa mga pinakakaraniwang problema, para mabilis kang makabalik sa tamang landas. Kung makakita ka ng error, simulan dito: tinutugunan ng mga tip sa ibaba ang mga isyung madalas maranasan ng mga user at madalas ay naayos ang problema nang hindi na kailangan ng dagdag na tulong.

### Mga Karaniwang Isyu

Narito ang ilan sa mga madalas na problema na nararanasan ng mga user, kasama ang malinaw na paliwanag at mga hakbang para ayusin ang mga ito:

1. **Walang SERPAPI_KEY sa .env file**
   - Kung makita mo ang error na `SERPAPI_KEY environment variable not found`, ibig sabihin ay hindi makita ng iyong aplikasyon ang API key na kailangan para ma-access ang SerpAPI. Para ayusin ito, gumawa ng file na pinangalanang `.env` sa root ng iyong proyekto (kung wala pa) at idagdag ang linyang `SERPAPI_KEY=your_serpapi_key_here`. Siguraduhing palitan ang `your_serpapi_key_here` ng iyong totoong key mula sa SerpAPI website.

2. **Mga error na Module not found**
   - Ang mga error tulad ng `ModuleNotFoundError: No module named 'httpx'` ay nagpapahiwatig na may kulang na Python package. Karaniwan itong nangyayari kapag hindi mo pa na-install ang lahat ng dependencies. Para ayusin ito, patakbuhin ang `pip install -r requirements.txt` sa iyong terminal para ma-install ang lahat ng kailangan ng proyekto.

3. **Mga isyu sa koneksyon**
   - Kung makakita ka ng error na tulad ng `Error during client execution`, madalas ibig sabihin nito ay hindi makakonekta ang client sa server, o hindi tumatakbo nang maayos ang server. Siguraduhing compatible ang bersyon ng client at server, at nandun at tumatakbo ang `server.py` sa tamang direktoryo. Ang pag-restart ng parehong server at client ay makakatulong din.

4. **Mga error mula sa SerpAPI**
   - Ang error na `Search API returned error status: 401` ay nangangahulugan na nawawala, mali, o expired ang iyong SerpAPI key. Pumunta sa iyong SerpAPI dashboard, i-verify ang iyong key, at i-update ang iyong `.env` file kung kinakailangan. Kung tama ang iyong key pero patuloy pa rin ang error, tingnan kung naubos na ang quota ng iyong libreng tier.

### Debug Mode

Sa default, naglo-log lang ang app ng mga importanteng impormasyon. Kung gusto mong makita ang mas detalyadong impormasyon tungkol sa mga nangyayari (halimbawa, para mag-diagnose ng mahihirap na isyu), maaari mong i-enable ang DEBUG mode. Ipapakita nito ang mas maraming detalye sa bawat hakbang na ginagawa ng app.

**Halimbawa: Normal Output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Halimbawa: DEBUG Output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Mapapansin na ang DEBUG mode ay may dagdag na mga linya tungkol sa HTTP requests, responses, at iba pang internal na detalye. Napakabisa nito para sa pag-troubleshoot.
Upang paganahin ang DEBUG mode, itakda ang antas ng logging sa DEBUG sa itaas ng iyong `client.py` o `server.py`:

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

## Ano ang susunod

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
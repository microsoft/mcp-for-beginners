# Лекција: Изградња Web Search MCP сервера

Овај поглавље показује како направити реалног AI агента који се интегрише са спољним API-јима, рукује различитим типовима података, управља грешкама и оркестрира више алата — све у продукцијском формату. Видећете:

- **Интеграцију са спољним API-јима који захтевају аутентификацију**
- **Руковање различитим типовима података са више крајњих тачака**
- **Робусне стратегије за управљање грешкама и логовање**
- **Оркестрацију више алата у једном серверу**

На крају ћете имати практично искуство са шаблонима и најбољим праксама које су кључне за напредне AI и LLM апликације.

## Увод

У овој лекцији научићете како да направите напредни MCP сервер и клијента који проширују могућности LLM-а коришћењем података са веба у реалном времену преко SerpAPI. Ово је важна вештина за развој динамичних AI агената који могу приступити ажурираним информацијама са интернета.

## Циљеви учења

На крају ове лекције моћи ћете да:

- Безбедно интегришете спољне API-је (као што је SerpAPI) у MCP сервер
- Имплементирате више алата за претрагу веба, вести, производа и питања и одговора
- Парсирате и форматирате структуриране податке за коришћење у LLM-у
- Ефикасно управљате грешкама и ограничењима броја позива API-ја
- Креирате и тестирате аутоматизоване и интерактивне MCP клијенте

## Web Search MCP сервер

Овај одељак представља архитектуру и функције Web Search MCP сервера. Видећете како се FastMCP и SerpAPI користе за проширење могућности LLM-а са подацима са веба у реалном времену.

### Преглед

Ова имплементација садржи четири алата који показују способност MCP-а да безбедно и ефикасно рукује разноликим задацима заснованим на спољним API-јима:

- **general_search**: За опште резултате претраге веба
- **news_search**: За најновије наслове вести
- **product_search**: За податке из е-трговине
- **qna**: За исечке питања и одговора

### Карактеристике
- **Примери кода**: Укључује језички специфичне блокове кода за Python (и лако прошириве на друге језике) користећи code pivots ради јасноће

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

Пре покретања клијента, корисно је разумети шта сервер ради. Фајл [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) имплементира MCP сервер, излажући алате за претрагу веба, вести, производа и Q&A интеграцијом са SerpAPI-јем. Он обрађује долазне захтеве, управља позивима API-ја, парсира одговоре и враћа структуриране резултате клијенту.

Пуну имплементацију можете погледати у [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Ево кратког примера како сервер дефинише и региструје алат:

### Python сервер

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

- **Интеграција спољних API-ја**: Приказује безбедно руковање API кључевима и спољним захтевима
- **Парсирање структурираних података**: Приказује како се одговори API-ја трансформишу у формате пријатељске за LLM
- **Управљање грешкама**: Робусно руковање грешкама уз одговарајуће логовање
- **Интерактивни клијент**: Укључује аутоматизоване тестове и интерактивни режим за тестирање
- **Управљање контекстом**: Користи MCP Context за логовање и праћење захтева

## Предуслови

Пре него што почнете, уверите се да је ваше окружење правилно подешено пратећи ове кораке. Ово ће осигурати да су све зависности инсталиране и да су ваши API кључеви исправно конфигурисани за беспрекорни развој и тестирање.

- Python 3.8 или новији
- SerpAPI API кључ (Региструјте се на [SerpAPI](https://serpapi.com/) - доступан бесплатни ниво)

## Инсталација

Да бисте почели, пратите ове кораке за подешавање окружења:

1. Инсталирајте зависности користећи uv (препоручено) или pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Креирајте `.env` фајл у корену пројекта са вашим SerpAPI кључем:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Коришћење

Web Search MCP сервер је основни део који излаже алате за претрагу веба, вести, производа и Q&A интеграцијом са SerpAPI-јем. Он обрађује долазне захтеве, управља позивима API-ја, парсира одговоре и враћа структуриране резултате клијенту.

Пуну имплементацију можете погледати у [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Покретање сервера

За покретање MCP сервера користите следећу команду:

```bash
python server.py
```

Сервер ће радити као stdio-базирани MCP сервер на који се клијент може директно повезати.

### Режими клијента

Клијент (`client.py`) подржава два режима за интеракцију са MCP сервером:

- **Нормални режим**: Покреће аутоматизоване тестове који проверавају све алате и њихове одговоре. Ово је корисно за брзу проверу да ли сервер и алати раде како се очекује.
- **Интерактивни режим**: Покреће менијски интерфејс у коме можете ручно одабрати и позвати алате, унети прилагођене упите и видети резултате у реалном времену. Ово је идеално за истраживање могућности сервера и експериментисање са различитим уносима.

Пуну имплементацију можете погледати у [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Покретање клијента

За покретање аутоматизованих тестова (ово ће аутоматски покренути сервер):

```bash
python client.py
```

Или покрените у интерактивном режиму:

```bash
python client.py --interactive
```

### Тестирање различитим методама

Постоји неколико начина да тестирате и интерагујете са алатима које сервер пружа, у зависности од ваших потреба и радног тока.

#### Писање прилагођених тест скрипти са MCP Python SDK-ом
Такође можете направити своје тест скрипте користећи MCP Python SDK:

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

У овом контексту, „тест скрипта“ значи прилагођени Python програм који пишете да би деловао као клијент MCP сервера. Уместо формалног јединичног теста, ова скрипта вам омогућава да програмски повежете сервер, позовете било који од његових алата са параметрима по вашем избору и прегледате резултате. Овај приступ је користан за:
- Прототиповање и експериментисање са позивима алата
- Валидацију како сервер реагује на различите уносе
- Аутоматизацију поновљених позива алата
- Креирање сопствених радних токова или интеграција на врху MCP сервера

Можете користити тест скрипте да брзо испробате нове упите, дебагујете понашање алата или чак као полазну основу за напреднију аутоматизацију. Испод је пример како користити MCP Python SDK за креирање такве скрипте:

## Опис алата

Можете користити следеће алате које пружа сервер за извођење различитих врста претрага и упита. Сваки алат је описан са својим параметрима и примером коришћења.

Овај одељак пружа детаље о сваком доступном алату и њиховим параметрима.

### general_search

Изводи општу претрагу веба и враћа форматиране резултате.

**Како позвати овај алат:**

Можете позвати `general_search` из своје скрипте користећи MCP Python SDK, или интерактивно преко Inspector-а или интерактивног режима клијента. Ево примера кода користећи SDK:

# [Python пример](../../../../05-AdvancedTopics/web-search-mcp)

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

Алтернативно, у интерактивном режиму изаберите `general_search` из менија и унесите свој упит када се затражи.

**Параметри:**
- `query` (string): Упит за претрагу

**Пример захтева:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Претражује најновије вести везане за упит.

**Како позвати овај алат:**

Можете позвати `news_search` из своје скрипте користећи MCP Python SDK, или интерактивно преко Inspector-а или интерактивног режима клијента. Ево примера кода користећи SDK:

# [Python пример](../../../../05-AdvancedTopics/web-search-mcp)

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

Алтернативно, у интерактивном режиму изаберите `news_search` из менија и унесите свој упит када се затражи.

**Параметри:**
- `query` (string): Упит за претрагу

**Пример захтева:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Претражује производе који одговарају упиту.

**Како позвати овај алат:**

Можете позвати `product_search` из своје скрипте користећи MCP Python SDK, или интерактивно преко Inspector-а или интерактивног режима клијента. Ево примера кода користећи SDK:

# [Python пример](../../../../05-AdvancedTopics/web-search-mcp)

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

Алтернативно, у интерактивном режиму изаберите `product_search` из менија и унесите свој упит када се затражи.

**Параметри:**
- `query` (string): Упит за претрагу производа

**Пример захтева:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Добија директне одговоре на питања са претраживача.

**Како позвати овај алат:**

Можете позвати `qna` из своје скрипте користећи MCP Python SDK, или интерактивно преко Inspector-а или интерактивног режима клијента. Ево примера кода користећи SDK:

# [Python пример](../../../../05-AdvancedTopics/web-search-mcp)

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

Алтернативно, у интерактивном режиму изаберите `qna` из менија и унесите своје питање када се затражи.

**Параметри:**
- `question` (string): Питање за које тражите одговор

**Пример захтева:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Детаљи кода

Овај одељак пружа исечке кода и референце за имплементације сервера и клијента.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Погледајте [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) и [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) за детаљне имплементације.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Напредни концепти у овој лекцији

Пре него што почнете са изградњом, ево неколико важних напредних концепата који ће се појавити кроз цело поглавље. Разумевање ових ће вам помоћи да пратите материјал, чак и ако су вам нови:

- **Оркестрација више алата**: Ово значи покретање више различитих алата (као што су претрага веба, претрага вести, претрага производа и Q&A) у оквиру једног MCP сервера. Омогућава вашем серверу да обрађује разне задатке, не само један.
- **Управљање ограничењима броја позива API-ја**: Многи спољни API-ји (као SerpAPI) ограничавају колико захтева можете послати у одређеном временском периоду. Добар код проверава ова ограничења и лепо их обрађује, тако да ваша апликација неће отказати ако достигнете лимит.
- **Парсирање структурираних података**: Одговори API-ја су често сложени и унутрашње структуре. Овај концепт се односи на претварање тих одговора у чисте, лако употребљиве формате који су пријатељски за LLM или друге програме.
- **Опоравак од грешака**: Понекад нешто пође по злу — можда мрежа не ради, или API не врати оно што очекујете. Опоравак од грешака значи да ваш код може да се носи са тим проблемима и да и даље пружи корисне повратне информације, уместо да се сруши.
- **Валидација параметара**: Ово значи проверу да ли су сви уноси у ваше алате исправни и безбедни за коришћење. Укључује подешавање подразумеваних вредности и проверу типова, што помаже у спречавању грешака и конфузије.

Овај одељак ће вам помоћи да дијагностикујете и решите уобичајене проблеме на које можете наићи док радите са Web Search MCP сервером. Ако наиђете на грешке или неочекивано понашање, овај одељак за решавање проблема пружа решења за најчешће проблеме. Прегледајте ове савете пре него што тражите додатну помоћ — често брзо решавају проблеме.

## Решавање проблема

Када радите са Web Search MCP сервером, повремено можете наићи на проблеме — то је нормално приликом развоја са спољним API-јима и новим алатима. Овај одељак пружа практична решења за најчешће проблеме, како бисте брзо наставили рад. Ако наиђете на грешку, почните овде: савети испод покривају проблеме са којима се већина корисника сусреће и често могу решити ваш проблем без додатне помоћи.

### Чести проблеми

Испод су неки од најчешћих проблема са којима се корисници сусрећу, заједно са јасним објашњењима и корацима за решавање:

1. **Недостаје SERPAPI_KEY у .env фајлу**
   - Ако видите грешку `SERPAPI_KEY environment variable not found`, то значи да ваша апликација не може да пронађе API кључ потребан за приступ SerpAPI-ју. Да бисте то решили, креирајте фајл `.env` у корену пројекта (ако већ не постоји) и додајте линију као што је `SERPAPI_KEY=your_serpapi_key_here`. Обавезно замените `your_serpapi_key_here` стварним кључем са SerpAPI сајта.

2. **Грешке типа Module not found**
   - Грешке као што је `ModuleNotFoundError: No module named 'httpx'` указују да недостаје потребан Python пакет. Ово се обично дешава ако нисте инсталирали све зависности. Да бисте решили, покрените `pip install -r requirements.txt` у вашем терминалу да инсталирате све што пројекат захтева.

3. **Проблеми са конекцијом**
   - Ако добијете грешку као што је `Error during client execution`, често то значи да клијент не може да се повеже са сервером или сервер не ради како треба. Проверите да ли су клијент и сервер компатибилне верзије и да ли је `server.py` прис
Да бисте омогућили DEBUG режим, подесите ниво логовања на DEBUG на врху вашег `client.py` или `server.py`:

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

## Шта следи

- [5.10 Реално време стриминг](../mcp-realtimestreaming/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
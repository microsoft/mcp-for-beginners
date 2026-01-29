# Lekce: Vytvoření Web Search MCP Serveru

Tato kapitola ukazuje, jak postavit reálného AI agenta, který se integruje s externími API, zpracovává různé typy dat, zvládá chyby a orchestruje více nástrojů – to vše v produkčním formátu. Uvidíte:

- **Integraci s externími API vyžadujícími autentizaci**
- **Zpracování různorodých dat z více zdrojů**
- **Robustní zpracování chyb a strategie logování**
- **Orchestrace více nástrojů v jednom serveru**

Na konci budete mít praktické zkušenosti s postupy a osvědčenými metodami, které jsou nezbytné pro pokročilé AI a aplikace využívající LLM.

## Úvod

V této lekci se naučíte, jak postavit pokročilý MCP server a klienta, kteří rozšiřují schopnosti LLM o data z webu v reálném čase pomocí SerpAPI. To je klíčová dovednost pro vývoj dynamických AI agentů, kteří mají přístup k aktuálním informacím z internetu.

## Cíle učení

Na konci této lekce budete schopni:

- Bezpečně integrovat externí API (např. SerpAPI) do MCP serveru
- Implementovat více nástrojů pro vyhledávání na webu, zpráv, produktů a Q&A
- Parsovat a formátovat strukturovaná data pro potřeby LLM
- Efektivně zvládat chyby a řídit limity API
- Vytvářet a testovat jak automatizované, tak interaktivní MCP klienty

## Web Search MCP Server

Tato část představuje architekturu a funkce Web Search MCP Serveru. Ukáže se, jak FastMCP a SerpAPI společně rozšiřují schopnosti LLM o data z webu v reálném čase.

### Přehled

Tato implementace obsahuje čtyři nástroje, které demonstrují schopnost MCP bezpečně a efektivně zpracovávat různé úkoly řízené externími API:

- **general_search**: Pro široké výsledky z webu
- **news_search**: Pro aktuální zprávy
- **product_search**: Pro data z e-commerce
- **qna**: Pro otázky a odpovědi

### Funkce
- **Ukázky kódu**: Obsahuje jazykově specifické bloky kódu pro Python (a snadno rozšiřitelné do dalších jazyků) s využitím code pivots pro přehlednost

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

Než spustíte klienta, je užitečné pochopit, co server dělá. Soubor [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementuje MCP server, který zpřístupňuje nástroje pro vyhledávání na webu, zpráv, produktů a Q&A integrací se SerpAPI. Zpracovává příchozí požadavky, spravuje volání API, parsuje odpovědi a vrací strukturované výsledky klientovi.

Celou implementaci si můžete prohlédnout v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Zde je krátký příklad, jak server definuje a registruje nástroj:

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

- **Integrace externího API**: Ukazuje bezpečné zacházení s API klíči a externími požadavky
- **Parsování strukturovaných dat**: Ukazuje, jak převést odpovědi API do formátů vhodných pro LLM
- **Zpracování chyb**: Robustní zpracování chyb s odpovídajícím logováním
- **Interaktivní klient**: Obsahuje jak automatizované testy, tak interaktivní režim pro testování
- **Správa kontextu**: Využívá MCP Context pro logování a sledování požadavků

## Požadavky

Než začnete, ujistěte se, že máte správně nastavené prostředí podle těchto kroků. To zajistí, že všechny závislosti jsou nainstalovány a vaše API klíče jsou správně nakonfigurovány pro bezproblémový vývoj a testování.

- Python 3.8 nebo novější
- SerpAPI API klíč (Zaregistrujte se na [SerpAPI](https://serpapi.com/) – dostupný je i bezplatný tarif)

## Instalace

Pro začátek postupujte podle těchto kroků k nastavení prostředí:

1. Nainstalujte závislosti pomocí uv (doporučeno) nebo pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Vytvořte soubor `.env` v kořenovém adresáři projektu a vložte do něj svůj SerpAPI klíč:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Použití

Web Search MCP Server je hlavní komponenta, která zpřístupňuje nástroje pro vyhledávání na webu, zpráv, produktů a Q&A integrací se SerpAPI. Zpracovává příchozí požadavky, spravuje volání API, parsuje odpovědi a vrací strukturované výsledky klientovi.

Celou implementaci si můžete prohlédnout v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Spuštění serveru

Pro spuštění MCP serveru použijte následující příkaz:

```bash
python server.py
```

Server poběží jako MCP server založený na stdio, ke kterému se klient může přímo připojit.

### Režimy klienta

Klient (`client.py`) podporuje dva režimy pro interakci s MCP serverem:

- **Normální režim**: Spouští automatizované testy, které vyzkouší všechny nástroje a ověří jejich odpovědi. Je to užitečné pro rychlé ověření, že server a nástroje fungují správně.
- **Interaktivní režim**: Spustí menu, kde můžete ručně vybírat a volat nástroje, zadávat vlastní dotazy a sledovat výsledky v reálném čase. Ideální pro prozkoumání možností serveru a experimentování s různými vstupy.

Celou implementaci si můžete prohlédnout v [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Spuštění klienta

Pro spuštění automatizovaných testů (tím se automaticky spustí i server):

```bash
python client.py
```

Nebo spusťte interaktivní režim:

```bash
python client.py --interactive
```

### Testování různými způsoby

Existuje několik způsobů, jak testovat a pracovat s nástroji poskytovanými serverem, podle vašich potřeb a pracovního postupu.

#### Vytváření vlastních testovacích skriptů s MCP Python SDK
Můžete také vytvořit vlastní testovací skripty pomocí MCP Python SDK:

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

V tomto kontextu „testovací skript“ znamená vlastní Python program, který napíšete jako klient pro MCP server. Místo formálního unit testu vám tento skript umožní programově se připojit k serveru, volat jakýkoli z jeho nástrojů s vámi zvolenými parametry a prohlížet si výsledky. Tento přístup je užitečný pro:
- Prototypování a experimentování s voláním nástrojů
- Ověření, jak server reaguje na různé vstupy
- Automatizaci opakovaných volání nástrojů
- Vytváření vlastních pracovních postupů nebo integrací nad MCP serverem

Testovací skripty můžete použít k rychlému vyzkoušení nových dotazů, ladění chování nástrojů nebo jako výchozí bod pro pokročilejší automatizaci. Níže je příklad, jak použít MCP Python SDK k vytvoření takového skriptu:

## Popisy nástrojů

Následující nástroje poskytované serverem můžete použít k provádění různých typů vyhledávání a dotazů. Každý nástroj je popsán níže spolu s parametry a příklady použití.

Tato část obsahuje podrobnosti o jednotlivých dostupných nástrojích a jejich parametrech.

### general_search

Provádí obecné vyhledávání na webu a vrací formátované výsledky.

**Jak tento nástroj volat:**

Nástroj `general_search` můžete volat ze svého vlastního skriptu pomocí MCP Python SDK, nebo interaktivně pomocí Inspektora či interaktivního režimu klienta. Zde je příklad kódu s využitím SDK:

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

Alternativně v interaktivním režimu vyberte `general_search` z menu a zadejte dotaz, když budete vyzváni.

**Parametry:**
- `query` (string): Vyhledávací dotaz

**Příklad požadavku:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Vyhledává aktuální zprávy související s dotazem.

**Jak tento nástroj volat:**

Nástroj `news_search` můžete volat ze svého vlastního skriptu pomocí MCP Python SDK, nebo interaktivně pomocí Inspektora či interaktivního režimu klienta. Zde je příklad kódu s využitím SDK:

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

Alternativně v interaktivním režimu vyberte `news_search` z menu a zadejte dotaz, když budete vyzváni.

**Parametry:**
- `query` (string): Vyhledávací dotaz

**Příklad požadavku:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Vyhledává produkty odpovídající dotazu.

**Jak tento nástroj volat:**

Nástroj `product_search` můžete volat ze svého vlastního skriptu pomocí MCP Python SDK, nebo interaktivně pomocí Inspektora či interaktivního režimu klienta. Zde je příklad kódu s využitím SDK:

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

Alternativně v interaktivním režimu vyberte `product_search` z menu a zadejte dotaz, když budete vyzváni.

**Parametry:**
- `query` (string): Vyhledávací dotaz na produkt

**Příklad požadavku:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Získává přímé odpovědi na otázky z vyhledávačů.

**Jak tento nástroj volat:**

Nástroj `qna` můžete volat ze svého vlastního skriptu pomocí MCP Python SDK, nebo interaktivně pomocí Inspektora či interaktivního režimu klienta. Zde je příklad kódu s využitím SDK:

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

Alternativně v interaktivním režimu vyberte `qna` z menu a zadejte otázku, když budete vyzváni.

**Parametry:**
- `question` (string): Otázka, na kterou chcete najít odpověď

**Příklad požadavku:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Podrobnosti kódu

Tato část obsahuje úryvky kódu a odkazy na implementace serveru a klienta.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Podrobnosti celé implementace najdete v [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) a [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Pokročilé koncepty v této lekci

Než začnete stavět, zde jsou některé důležité pokročilé koncepty, které se v této kapitole objeví. Jejich pochopení vám pomůže lépe sledovat obsah, i když s nimi nejste zatím obeznámeni:

- **Orchestrace více nástrojů**: Znamená to provozovat několik různých nástrojů (např. webové vyhledávání, zprávy, vyhledávání produktů a Q&A) v jednom MCP serveru. Umožňuje to serveru zvládat různé úkoly, ne jen jeden.
- **Řízení limitů API**: Mnoho externích API (např. SerpAPI) omezuje počet požadavků za určitý čas. Kvalitní kód tyto limity kontroluje a elegantně je řeší, aby aplikace nepřestala fungovat při dosažení limitu.
- **Parsování strukturovaných dat**: Odpovědi API jsou často složité a vnořené. Tento koncept znamená převést tyto odpovědi do čistých, snadno použitelných formátů vhodných pro LLM nebo jiné programy.
- **Obnova po chybách**: Někdy se něco pokazí – třeba selže síť nebo API nevrátí očekávaná data. Obnova po chybách znamená, že váš kód tyto problémy zvládne a stále poskytne užitečnou zpětnou vazbu místo pádu aplikace.
- **Validace parametrů**: Znamená kontrolu, že všechny vstupy do vašich nástrojů jsou správné a bezpečné k použití. Zahrnuje nastavení výchozích hodnot a ověření typů, což pomáhá předcházet chybám a nedorozuměním.

Tato část vám pomůže diagnostikovat a vyřešit běžné problémy, na které můžete při práci s Web Search MCP Serverem narazit. Pokud se setkáte s chybami nebo neočekávaným chováním, tato sekce nabízí řešení nejčastějších potíží. Projděte si tyto tipy dříve, než budete hledat další pomoc – často problém rychle vyřeší.

## Řešení problémů

Při práci s Web Search MCP Serverem se občas mohou vyskytnout potíže – to je běžné při vývoji s externími API a novými nástroji. Tato sekce nabízí praktická řešení nejčastějších problémů, abyste se mohli rychle vrátit k práci. Pokud narazíte na chybu, začněte zde: níže uvedené tipy řeší problémy, se kterými se většina uživatelů setkává, a často vyřeší váš problém bez nutnosti další pomoci.

### Běžné problémy

Níže jsou uvedeny některé z nejčastějších problémů, se kterými se uživatelé setkávají, spolu s jasnými vysvětleními a kroky k jejich vyřešení:

1. **Chybějící SERPAPI_KEY v souboru .env**
   - Pokud se zobrazí chyba `SERPAPI_KEY environment variable not found`, znamená to, že aplikace nemůže najít API klíč potřebný pro přístup k SerpAPI. Pro opravu vytvořte v kořenovém adresáři projektu soubor `.env` (pokud ještě neexistuje) a přidejte řádek `SERPAPI_KEY=your_serpapi_key_here`. Nezapomeňte nahradit `your_serpapi_key_here` vaším skutečným klíčem ze SerpAPI.

2. **Chyby typu Module not found**
   - Chyby jako `ModuleNotFoundError: No module named 'httpx'` znamenají, že chybí požadovaný Python balíček. Obvykle se to stane, pokud jste nenainstalovali všechny závislosti. Pro vyřešení spusťte v terminálu `pip install -r requirements.txt`, aby se nainstalovalo vše potřebné.

3. **Problémy s připojením**
   - Pokud se objeví chyba jako `Error during client execution`, často to znamená, že klient se nemůže připojit k serveru nebo server neběží podle očekávání. Zkontrolujte, zda jsou klient i server kompatibilní verze a zda je soubor `server.py` ve správném adresáři a běží. Restartování serveru i klienta může také pomoci.

4. **Chyby SerpAPI**
   - Pokud vidíte `Search API returned error status: 401`, znamená to, že váš SerpAPI klíč chybí, je nesprávný nebo vypršel. Přejděte do svého SerpAPI dashboardu, ověřte klíč a případně aktualizujte soubor `.env`. Pokud je klíč správný, ale chyba přetrvává, zkontrolujte, zda vám nevypršel bezplatný tarif.

### Režim ladění (Debug Mode)

Ve výchozím nastavení aplikace loguje pouze důležité informace. Pokud chcete vidět více detailů o tom, co se děje (například pro diagnostiku složitých problémů), můžete zapnout režim DEBUG. Ten zobrazí mnohem více informací o každém kroku, který aplikace provádí.

**Příklad: Normální výstup**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Příklad: Výstup v režimu DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Všimněte si, že režim DEBUG obsahuje další řádky o HTTP požadavcích, odpovědích a dalších interních detailech. To může být velmi užitečné při řešení problémů.
Chcete-li povolit režim DEBUG, nastavte úroveň logování na DEBUG v horní části vašeho `client.py` nebo `server.py`:

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

## Co dál

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
# Lektion: Bygga en Web Search MCP-server

Det här kapitlet visar hur man bygger en verklig AI-agent som integreras med externa API:er, hanterar olika datatyper, hanterar fel och orkestrerar flera verktyg – allt i ett produktionsklart format. Du kommer att se:

- **Integration med externa API:er som kräver autentisering**
- **Hantering av olika datatyper från flera slutpunkter**
- **Robust felhantering och loggningsstrategier**
- **Orkestrering av flera verktyg i en enda server**

I slutet kommer du ha praktisk erfarenhet av mönster och bästa praxis som är avgörande för avancerade AI- och LLM-drivna applikationer.

## Introduktion

I den här lektionen lär du dig hur man bygger en avancerad MCP-server och klient som utökar LLM-funktionalitet med realtidsdata från webben via SerpAPI. Detta är en viktig färdighet för att utveckla dynamiska AI-agenter som kan hämta uppdaterad information från webben.

## Lärandemål

I slutet av lektionen ska du kunna:

- Integrera externa API:er (som SerpAPI) säkert i en MCP-server
- Implementera flera verktyg för webbsökning, nyheter, produktsökning och Q&A
- Tolka och formatera strukturerad data för LLM-användning
- Hantera fel och API-begränsningar effektivt
- Bygga och testa både automatiserade och interaktiva MCP-klienter

## Web Search MCP-server

Den här sektionen introducerar arkitekturen och funktionerna i Web Search MCP-servern. Du får se hur FastMCP och SerpAPI används tillsammans för att utöka LLM-funktionalitet med realtidsdata från webben.

### Översikt

Denna implementation innehåller fyra verktyg som visar MCP:s förmåga att hantera olika, externa API-drivna uppgifter på ett säkert och effektivt sätt:

- **general_search**: För breda webbresultat
- **news_search**: För senaste nyhetsrubriker
- **product_search**: För e-handelsdata
- **qna**: För frågor och svar

### Funktioner
- **Kodexempel**: Inkluderar språksspecifika kodblock för Python (och enkelt utbyggbart till andra språk) med kodpivoter för tydlighet

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

Innan du kör klienten är det bra att förstå vad servern gör. Filen [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementerar MCP-servern och exponerar verktyg för webbsökning, nyheter, produktsökning och Q&A genom integration med SerpAPI. Den hanterar inkommande förfrågningar, sköter API-anrop, tolkar svar och returnerar strukturerade resultat till klienten.

Du kan granska hela implementationen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Här är ett kort exempel på hur servern definierar och registrerar ett verktyg:

### Python-server

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

- **Integration med externa API:er**: Visar säker hantering av API-nycklar och externa anrop
- **Tolkning av strukturerad data**: Visar hur API-svar omvandlas till LLM-vänliga format
- **Felhantering**: Robust felhantering med lämplig loggning
- **Interaktiv klient**: Inkluderar både automatiserade tester och ett interaktivt läge för testning
- **Kontexthantering**: Använder MCP Context för loggning och spårning av förfrågningar

## Förutsättningar

Innan du börjar, se till att din miljö är korrekt uppsatt genom att följa dessa steg. Detta säkerställer att alla beroenden är installerade och att dina API-nycklar är korrekt konfigurerade för smidig utveckling och testning.

- Python 3.8 eller högre
- SerpAPI API-nyckel (Registrera dig på [SerpAPI](https://serpapi.com/) – gratisnivå finns)

## Installation

För att komma igång, följ dessa steg för att ställa in din miljö:

1. Installera beroenden med uv (rekommenderas) eller pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Skapa en `.env`-fil i projektets rotmapp med din SerpAPI-nyckel:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Användning

Web Search MCP-servern är kärnkomponenten som exponerar verktyg för webbsökning, nyheter, produktsökning och Q&A genom integration med SerpAPI. Den hanterar inkommande förfrågningar, sköter API-anrop, tolkar svar och returnerar strukturerade resultat till klienten.

Du kan granska hela implementationen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Starta servern

För att starta MCP-servern, använd följande kommando:

```bash
python server.py
```

Servern körs som en stdio-baserad MCP-server som klienten kan ansluta till direkt.

### Klientlägen

Klienten (`client.py`) stödjer två lägen för interaktion med MCP-servern:

- **Normalläge**: Kör automatiserade tester som använder alla verktyg och verifierar deras svar. Detta är användbart för att snabbt kontrollera att servern och verktygen fungerar som förväntat.
- **Interaktivt läge**: Startar ett menybaserat gränssnitt där du manuellt kan välja och anropa verktyg, skriva egna frågor och se resultat i realtid. Perfekt för att utforska serverns funktioner och experimentera med olika indata.

Du kan granska hela implementationen i [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Köra klienten

För att köra de automatiserade testerna (detta startar automatiskt servern):

```bash
python client.py
```

Eller kör i interaktivt läge:

```bash
python client.py --interactive
```

### Testa med olika metoder

Det finns flera sätt att testa och interagera med verktygen som servern tillhandahåller, beroende på dina behov och arbetsflöde.

#### Skriva egna testskript med MCP Python SDK
Du kan också bygga egna testskript med MCP Python SDK:

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

I detta sammanhang betyder "testskript" ett eget Python-program som du skriver för att agera som klient mot MCP-servern. Istället för att vara ett formellt enhetstest låter detta skript dig programmatisk ansluta till servern, anropa valfritt verktyg med valfria parametrar och inspektera resultaten. Detta är användbart för:
- Prototypning och experiment med verktygsanrop
- Validering av serverns svar på olika indata
- Automatisering av upprepade verktygsanrop
- Bygga egna arbetsflöden eller integrationer ovanpå MCP-servern

Du kan använda testskript för att snabbt prova nya frågor, felsöka verktygsbeteende eller som utgångspunkt för mer avancerad automation. Nedan är ett exempel på hur du använder MCP Python SDK för att skapa ett sådant skript:

## Verktygsbeskrivningar

Du kan använda följande verktyg som servern tillhandahåller för att utföra olika typer av sökningar och frågor. Varje verktyg beskrivs nedan med dess parametrar och exempel på användning.

Den här sektionen ger detaljer om varje tillgängligt verktyg och deras parametrar.

### general_search

Utför en generell webbsökning och returnerar formaterade resultat.

**Så här anropar du verktyget:**

Du kan anropa `general_search` från ditt eget skript med MCP Python SDK, eller interaktivt via Inspector eller det interaktiva klientläget. Här är ett kodexempel med SDK:

# [Python-exempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktivt läge, välj `general_search` från menyn och skriv in din fråga när du blir ombedd.

**Parametrar:**
- `query` (sträng): Sökfrågan

**Exempel på förfrågan:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Söker efter senaste nyhetsartiklar relaterade till en fråga.

**Så här anropar du verktyget:**

Du kan anropa `news_search` från ditt eget skript med MCP Python SDK, eller interaktivt via Inspector eller det interaktiva klientläget. Här är ett kodexempel med SDK:

# [Python-exempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktivt läge, välj `news_search` från menyn och skriv in din fråga när du blir ombedd.

**Parametrar:**
- `query` (sträng): Sökfrågan

**Exempel på förfrågan:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Söker efter produkter som matchar en fråga.

**Så här anropar du verktyget:**

Du kan anropa `product_search` från ditt eget skript med MCP Python SDK, eller interaktivt via Inspector eller det interaktiva klientläget. Här är ett kodexempel med SDK:

# [Python-exempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktivt läge, välj `product_search` från menyn och skriv in din fråga när du blir ombedd.

**Parametrar:**
- `query` (sträng): Produktsökfrågan

**Exempel på förfrågan:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Hämtar direkta svar på frågor från sökmotorer.

**Så här anropar du verktyget:**

Du kan anropa `qna` från ditt eget skript med MCP Python SDK, eller interaktivt via Inspector eller det interaktiva klientläget. Här är ett kodexempel med SDK:

# [Python-exempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktivt läge, välj `qna` från menyn och skriv in din fråga när du blir ombedd.

**Parametrar:**
- `question` (sträng): Frågan du vill ha svar på

**Exempel på förfrågan:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Koddetaljer

Den här sektionen innehåller kodexempel och referenser för server- och klientimplementationerna.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Se [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) och [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) för fullständiga implementationsdetaljer.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Avancerade koncept i denna lektion

Innan du börjar bygga, här är några viktiga avancerade koncept som dyker upp genom hela kapitlet. Att förstå dessa hjälper dig att följa med, även om du är ny på dem:

- **Orkestrering av flera verktyg**: Detta innebär att flera olika verktyg (som webbsökning, nyhetssökning, produktsökning och Q&A) körs inom en enda MCP-server. Det gör att din server kan hantera en mängd olika uppgifter, inte bara en.
- **Hantering av API-begränsningar**: Många externa API:er (som SerpAPI) begränsar hur många förfrågningar du kan göra under en viss tid. Bra kod kontrollerar dessa begränsningar och hanterar dem smidigt, så att din app inte kraschar om du når en gräns.
- **Tolkning av strukturerad data**: API-svar är ofta komplexa och nästlade. Detta koncept handlar om att omvandla dessa svar till rena, lättanvända format som är vänliga för LLM eller andra program.
- **Felåterhämtning**: Ibland går saker fel – kanske nätverket fallerar eller API:et returnerar oväntade svar. Felåterhämtning betyder att din kod kan hantera dessa problem och ändå ge användbar feedback istället för att krascha.
- **Parameterkontroll**: Detta handlar om att kontrollera att alla indata till dina verktyg är korrekta och säkra att använda. Det inkluderar att sätta standardvärden och säkerställa rätt datatyper, vilket hjälper till att förebygga buggar och förvirring.

Den här sektionen hjälper dig att diagnostisera och lösa vanliga problem du kan stöta på när du arbetar med Web Search MCP-servern. Om du stöter på fel eller oväntat beteende när du arbetar med Web Search MCP-servern, ger denna felsökningssektion lösningar på de vanligaste problemen. Läs igenom dessa tips innan du söker vidare hjälp – de löser ofta problem snabbt.

## Felsökning

När du arbetar med Web Search MCP-servern kan du ibland stöta på problem – det är normalt när man utvecklar med externa API:er och nya verktyg. Den här sektionen ger praktiska lösningar på de vanligaste problemen så att du snabbt kan komma tillbaka på rätt spår. Om du får ett fel, börja här: tipsen nedan tar upp de problem som flest användare stöter på och kan ofta lösa ditt problem utan extra hjälp.

### Vanliga problem

Nedan listas några av de vanligaste problemen användare stöter på, tillsammans med tydliga förklaringar och steg för att lösa dem:

1. **Saknad SERPAPI_KEY i .env-filen**
   - Om du ser felet `SERPAPI_KEY environment variable not found` betyder det att din applikation inte hittar API-nyckeln som behövs för att komma åt SerpAPI. För att fixa detta, skapa en fil som heter `.env` i projektets rotmapp (om den inte redan finns) och lägg till en rad som `SERPAPI_KEY=din_serpapi_nyckel_här`. Se till att byta ut `din_serpapi_nyckel_här` mot din faktiska nyckel från SerpAPI-webbplatsen.

2. **Modul inte hittad-fel**
   - Fel som `ModuleNotFoundError: No module named 'httpx'` indikerar att ett nödvändigt Python-paket saknas. Detta händer oftast om du inte har installerat alla beroenden. För att lösa detta, kör `pip install -r requirements.txt` i din terminal för att installera allt som projektet behöver.

3. **Anslutningsproblem**
   - Om du får ett fel som `Error during client execution` betyder det ofta att klienten inte kan ansluta till servern, eller att servern inte körs som förväntat. Dubbelkolla att både klient och server är kompatibla versioner, och att `server.py` finns och körs i rätt katalog. Att starta om både server och klient kan också hjälpa.

4. **SerpAPI-fel**
   - Om du ser `Search API returned error status: 401` betyder det att din SerpAPI-nyckel saknas, är felaktig eller har gått ut. Gå till din SerpAPI-dashboard, verifiera din nyckel och uppdatera din `.env`-fil vid behov. Om nyckeln är korrekt men du fortfarande får detta fel, kontrollera om din gratisnivå har slut på kvot.

### Debug-läge

Som standard loggar appen bara viktig information. Om du vill se mer detaljer om vad som händer (till exempel för att diagnostisera svåra problem) kan du aktivera DEBUG-läget. Detta visar mycket mer om varje steg appen tar.

**Exempel: Normal utdata**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Exempel: DEBUG-utdata**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Notera hur DEBUG-läget inkluderar extra rader om HTTP-förfrågningar, svar och andra interna detaljer. Detta kan vara mycket hjälpsamt vid felsökning.
För att aktivera DEBUG-läge, ställ in loggningsnivån till DEBUG högst upp i din `client.py` eller `server.py`:

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

## Vad händer härnäst

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
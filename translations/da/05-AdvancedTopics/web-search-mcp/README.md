# Lektion: Bygning af en Web Search MCP Server

Dette kapitel viser, hvordan man bygger en AI-agent til den virkelige verden, der integrerer med eksterne API'er, håndterer forskellige datatyper, styrer fejl og orkestrerer flere værktøjer – alt sammen i et produktionsklart format. Du vil se:

- **Integration med eksterne API'er, der kræver autentificering**
- **Håndtering af forskellige datatyper fra flere endpoints**
- **Robust fejlhåndtering og logningsstrategier**
- **Multi-værktøjs orkestrering i en enkelt server**

Ved slutningen vil du have praktisk erfaring med mønstre og bedste praksis, som er essentielle for avancerede AI- og LLM-drevne applikationer.

## Introduktion

I denne lektion lærer du at bygge en avanceret MCP-server og klient, der udvider LLM-funktionalitet med realtidsdata fra nettet ved hjælp af SerpAPI. Dette er en vigtig færdighed til at udvikle dynamiske AI-agenter, der kan tilgå opdateret information fra nettet.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Integrere eksterne API'er (som SerpAPI) sikkert i en MCP-server
- Implementere flere værktøjer til web-, nyheds-, produkt-søgning og Q&A
- Parse og formatere strukturerede data til LLM-forbrug
- Håndtere fejl og styre API-ratebegrænsninger effektivt
- Bygge og teste både automatiserede og interaktive MCP-klienter

## Web Search MCP Server

Denne sektion introducerer arkitekturen og funktionerne i Web Search MCP Server. Du vil se, hvordan FastMCP og SerpAPI bruges sammen til at udvide LLM-funktionalitet med realtidsdata fra nettet.

### Oversigt

Denne implementering indeholder fire værktøjer, der demonstrerer MCP’s evne til sikkert og effektivt at håndtere forskellige, eksterne API-drevne opgaver:

- **general_search**: Til brede webresultater
- **news_search**: Til de seneste overskrifter
- **product_search**: Til e-handelsdata
- **qna**: Til spørgsmål-og-svar uddrag

### Funktioner
- **Kodeeksempler**: Indeholder sprog-specifikke kodeblokke for Python (og let udvidelige til andre sprog) ved brug af kodepivoter for klarhed

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

Før du kører klienten, er det nyttigt at forstå, hvad serveren gør. Filen [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementerer MCP-serveren, som eksponerer værktøjer til web-, nyheds-, produkt-søgning og Q&A ved at integrere med SerpAPI. Den håndterer indkommende forespørgsler, styrer API-kald, parser svar og returnerer strukturerede resultater til klienten.

Du kan gennemgå hele implementeringen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Her er et kort eksempel på, hvordan serveren definerer og registrerer et værktøj:

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

- **Integration med eksterne API'er**: Viser sikker håndtering af API-nøgler og eksterne forespørgsler
- **Parsing af strukturerede data**: Viser, hvordan API-svar omdannes til LLM-venlige formater
- **Fejlhåndtering**: Robust fejlhåndtering med passende logning
- **Interaktiv klient**: Indeholder både automatiserede tests og en interaktiv tilstand til testning
- **Context Management**: Udnytter MCP Context til logning og sporing af forespørgsler

## Forudsætninger

Før du går i gang, skal du sikre, at dit miljø er sat korrekt op ved at følge disse trin. Det sikrer, at alle afhængigheder er installeret, og at dine API-nøgler er konfigureret korrekt for problemfri udvikling og test.

- Python 3.8 eller nyere
- SerpAPI API-nøgle (Tilmeld dig på [SerpAPI](https://serpapi.com/) – gratis niveau tilgængeligt)

## Installation

For at komme i gang, følg disse trin for at sætte dit miljø op:

1. Installer afhængigheder ved hjælp af uv (anbefalet) eller pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Opret en `.env`-fil i projektets rodmappe med din SerpAPI-nøgle:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Brug

Web Search MCP Server er den centrale komponent, der eksponerer værktøjer til web-, nyheds-, produkt-søgning og Q&A ved at integrere med SerpAPI. Den håndterer indkommende forespørgsler, styrer API-kald, parser svar og returnerer strukturerede resultater til klienten.

Du kan gennemgå hele implementeringen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Kørsel af serveren

For at starte MCP-serveren, brug følgende kommando:

```bash
python server.py
```

Serveren kører som en stdio-baseret MCP-server, som klienten kan forbinde til direkte.

### Klienttilstande

Klienten (`client.py`) understøtter to tilstande til interaktion med MCP-serveren:

- **Normal tilstand**: Kører automatiserede tests, der afprøver alle værktøjer og verificerer deres svar. Dette er nyttigt til hurtigt at tjekke, at serveren og værktøjerne fungerer som forventet.
- **Interaktiv tilstand**: Starter en menu-baseret grænseflade, hvor du manuelt kan vælge og kalde værktøjer, indtaste brugerdefinerede forespørgsler og se resultater i realtid. Dette er ideelt til at udforske serverens funktioner og eksperimentere med forskellige input.

Du kan gennemgå hele implementeringen i [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Kørsel af klienten

For at køre de automatiserede tests (dette starter automatisk serveren):

```bash
python client.py
```

Eller kør i interaktiv tilstand:

```bash
python client.py --interactive
```

### Test med forskellige metoder

Der er flere måder at teste og interagere med de værktøjer, som serveren tilbyder, afhængigt af dine behov og arbejdsgang.

#### Skriv brugerdefinerede test-scripts med MCP Python SDK
Du kan også bygge dine egne test-scripts ved hjælp af MCP Python SDK:

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

I denne sammenhæng betyder et "test-script" et brugerdefineret Python-program, du skriver for at fungere som klient til MCP-serveren. I stedet for at være en formel enhedstest, giver dette script dig mulighed for programmæssigt at forbinde til serveren, kalde et hvilket som helst af dens værktøjer med valgte parametre og inspicere resultaterne. Denne tilgang er nyttig til:
- Prototyping og eksperimentering med værktøjskald
- Validering af, hvordan serveren reagerer på forskellige input
- Automatisering af gentagne værktøjskald
- Opbygning af egne arbejdsgange eller integrationer oven på MCP-serveren

Du kan bruge test-scripts til hurtigt at prøve nye forespørgsler, fejlfinde værktøjsadfærd eller endda som udgangspunkt for mere avanceret automatisering. Nedenfor er et eksempel på, hvordan du bruger MCP Python SDK til at oprette et sådant script:

## Værktøjsbeskrivelser

Du kan bruge følgende værktøjer, som serveren stiller til rådighed, til at udføre forskellige typer søgninger og forespørgsler. Hvert værktøj er beskrevet nedenfor med dets parametre og eksempel på brug.

Denne sektion giver detaljer om hvert tilgængeligt værktøj og deres parametre.

### general_search

Udfører en generel websøgning og returnerer formaterede resultater.

**Sådan kalder du dette værktøj:**

Du kan kalde `general_search` fra dit eget script ved hjælp af MCP Python SDK, eller interaktivt via Inspector eller den interaktive klienttilstand. Her er et kodeeksempel med SDK:

# [Python Eksempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktiv tilstand, vælg `general_search` fra menuen og indtast din forespørgsel, når du bliver bedt om det.

**Parametre:**
- `query` (string): Søgeforespørgslen

**Eksempel på forespørgsel:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Søger efter nylige nyhedsartikler relateret til en forespørgsel.

**Sådan kalder du dette værktøj:**

Du kan kalde `news_search` fra dit eget script ved hjælp af MCP Python SDK, eller interaktivt via Inspector eller den interaktive klienttilstand. Her er et kodeeksempel med SDK:

# [Python Eksempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktiv tilstand, vælg `news_search` fra menuen og indtast din forespørgsel, når du bliver bedt om det.

**Parametre:**
- `query` (string): Søgeforespørgslen

**Eksempel på forespørgsel:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Søger efter produkter, der matcher en forespørgsel.

**Sådan kalder du dette værktøj:**

Du kan kalde `product_search` fra dit eget script ved hjælp af MCP Python SDK, eller interaktivt via Inspector eller den interaktive klienttilstand. Her er et kodeeksempel med SDK:

# [Python Eksempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktiv tilstand, vælg `product_search` fra menuen og indtast din forespørgsel, når du bliver bedt om det.

**Parametre:**
- `query` (string): Produkt-søgeforespørgslen

**Eksempel på forespørgsel:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Henter direkte svar på spørgsmål fra søgemaskiner.

**Sådan kalder du dette værktøj:**

Du kan kalde `qna` fra dit eget script ved hjælp af MCP Python SDK, eller interaktivt via Inspector eller den interaktive klienttilstand. Her er et kodeeksempel med SDK:

# [Python Eksempel](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativt, i interaktiv tilstand, vælg `qna` fra menuen og indtast dit spørgsmål, når du bliver bedt om det.

**Parametre:**
- `question` (string): Spørgsmålet, der skal findes svar på

**Eksempel på forespørgsel:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Kodedetaljer

Denne sektion indeholder kodeudsnit og referencer til server- og klientimplementeringerne.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Se [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) og [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) for fulde implementeringsdetaljer.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Avancerede Koncepter i Denne Lektion

Før du begynder at bygge, er her nogle vigtige avancerede koncepter, der vil optræde gennem hele kapitlet. At forstå disse vil hjælpe dig med at følge med, selv hvis du er ny til dem:

- **Multi-værktøjs orkestrering**: Det betyder at køre flere forskellige værktøjer (som web-søgning, nyhedssøgning, produkt-søgning og Q&A) inden for en enkelt MCP-server. Det giver din server mulighed for at håndtere en række opgaver, ikke kun én.
- **Håndtering af API-ratebegrænsninger**: Mange eksterne API'er (som SerpAPI) begrænser, hvor mange forespørgsler du kan lave inden for en given tid. God kode tjekker for disse begrænsninger og håndterer dem elegant, så din app ikke bryder sammen, hvis du rammer en grænse.
- **Parsing af strukturerede data**: API-svar er ofte komplekse og indlejrede. Dette koncept handler om at omdanne disse svar til rene, let anvendelige formater, der er venlige for LLM’er eller andre programmer.
- **Fejlgenopretning**: Nogle gange går ting galt – måske fejler netværket, eller API’en returnerer ikke det forventede. Fejlgenopretning betyder, at din kode kan håndtere disse problemer og stadig give brugbar feedback i stedet for at crashe.
- **Parameter-validering**: Det handler om at sikre, at alle input til dine værktøjer er korrekte og sikre at bruge. Det inkluderer at sætte standardværdier og sikre, at typerne er rigtige, hvilket hjælper med at forhindre fejl og forvirring.

Denne sektion hjælper dig med at diagnosticere og løse almindelige problemer, du kan støde på, mens du arbejder med Web Search MCP Server. Hvis du oplever fejl eller uventet adfærd, giver denne fejlsøgningssektion løsninger på de mest almindelige problemer. Gennemgå disse tips, før du søger yderligere hjælp – de løser ofte problemer hurtigt.

## Fejlsøgning

Når du arbejder med Web Search MCP Server, kan du af og til støde på problemer – det er normalt, når man udvikler med eksterne API’er og nye værktøjer. Denne sektion giver praktiske løsninger på de mest almindelige problemer, så du hurtigt kan komme videre. Hvis du støder på en fejl, start her: tipsene nedenfor adresserer de problemer, som de fleste brugere møder, og kan ofte løse dit problem uden ekstra hjælp.

### Almindelige problemer

Nedenfor er nogle af de hyppigste problemer, brugere støder på, sammen med klare forklaringer og trin til at løse dem:

1. **Manglende SERPAPI_KEY i .env-filen**
   - Hvis du ser fejlen `SERPAPI_KEY environment variable not found`, betyder det, at din applikation ikke kan finde API-nøglen, der er nødvendig for at tilgå SerpAPI. For at løse dette, opret en fil med navnet `.env` i din projektmappe (hvis den ikke allerede findes) og tilføj en linje som `SERPAPI_KEY=din_serpapi_nøgle_her`. Sørg for at erstatte `din_serpapi_nøgle_her` med din faktiske nøgle fra SerpAPI-websitet.

2. **Modul ikke fundet fejl**
   - Fejl som `ModuleNotFoundError: No module named 'httpx'` indikerer, at et nødvendigt Python-pakke mangler. Dette sker typisk, hvis du ikke har installeret alle afhængigheder. For at løse dette, kør `pip install -r requirements.txt` i din terminal for at installere alt, hvad dit projekt behøver.

3. **Forbindelsesproblemer**
   - Hvis du får en fejl som `Error during client execution`, betyder det ofte, at klienten ikke kan forbinde til serveren, eller at serveren ikke kører som forventet. Dobbelttjek, at både klient og server er kompatible versioner, og at `server.py` findes og kører i den korrekte mappe. Genstart både server og klient kan også hjælpe.

4. **SerpAPI fejl**
   - Hvis du ser `Search API returned error status: 401`, betyder det, at din SerpAPI-nøgle mangler, er forkert eller udløbet. Gå til dit SerpAPI-dashboard, bekræft din nøgle, og opdater din `.env`-fil om nødvendigt. Hvis din nøgle er korrekt, men du stadig ser denne fejl, tjek om din gratis kvote er opbrugt.

### Debug-tilstand

Som standard logger appen kun vigtig information. Hvis du vil se flere detaljer om, hvad der sker (for eksempel for at diagnosticere vanskelige problemer), kan du aktivere DEBUG-tilstand. Det vil vise dig meget mere om hvert trin, appen tager.

**Eksempel: Normal output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Eksempel: DEBUG output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Bemærk, hvordan DEBUG-tilstand inkluderer ekstra linjer om HTTP-forespørgsler, svar og andre interne detaljer. Dette kan være meget hjælpsomt til fejlsøgning.
For at aktivere DEBUG-tilstand skal du sætte logningsniveauet til DEBUG øverst i din `client.py` eller `server.py`:

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

## Hvad er det næste

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
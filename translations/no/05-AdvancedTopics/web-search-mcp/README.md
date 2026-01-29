# Lekse: Bygge en Web Search MCP Server

Dette kapitlet viser hvordan du bygger en ekte AI-agent som integreres med eksterne API-er, håndterer ulike datatyper, styrer feil og orkestrerer flere verktøy – alt i et produksjonsklart format. Du vil se:

- **Integrasjon med eksterne API-er som krever autentisering**
- **Håndtering av ulike datatyper fra flere endepunkter**
- **Robust feilhåndtering og loggstrategier**
- **Orkestrering av flere verktøy i én enkelt server**

Mot slutten vil du ha praktisk erfaring med mønstre og beste praksis som er essensielle for avanserte AI- og LLM-drevne applikasjoner.

## Introduksjon

I denne leksen lærer du hvordan du bygger en avansert MCP-server og klient som utvider LLM-funksjonalitet med sanntidsdata fra nettet ved hjelp av SerpAPI. Dette er en viktig ferdighet for å utvikle dynamiske AI-agenter som kan hente oppdatert informasjon fra nettet.

## Læringsmål

Etter denne leksen skal du kunne:

- Integrere eksterne API-er (som SerpAPI) sikkert i en MCP-server
- Implementere flere verktøy for web-, nyhets-, produkt-søk og Q&A
- Tolke og formatere strukturert data for LLM-bruk
- Håndtere feil og styre API-ratebegrensninger effektivt
- Bygge og teste både automatiserte og interaktive MCP-klienter

## Web Search MCP Server

Denne delen introduserer arkitekturen og funksjonene til Web Search MCP Server. Du vil se hvordan FastMCP og SerpAPI brukes sammen for å utvide LLM-funksjonalitet med sanntidsdata fra nettet.

### Oversikt

Denne implementasjonen har fire verktøy som viser MCPs evne til å håndtere ulike, eksterne API-drevne oppgaver på en sikker og effektiv måte:

- **general_search**: For brede webresultater
- **news_search**: For ferske nyhetssaker
- **product_search**: For e-handelsdata
- **qna**: For spørsmål-og-svar utdrag

### Funksjoner
- **Kodeeksempler**: Inkluderer språkspesifikke kodeblokker for Python (og lett utvidbart til andre språk) med kodepivoter for klarhet

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

Før du kjører klienten, er det nyttig å forstå hva serveren gjør. Filen [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementerer MCP-serveren, som eksponerer verktøy for web-, nyhets-, produkt-søk og Q&A ved å integrere med SerpAPI. Den håndterer innkommende forespørsler, styrer API-kall, tolker svar og returnerer strukturerte resultater til klienten.

Du kan se hele implementasjonen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Her er et kort eksempel på hvordan serveren definerer og registrerer et verktøy:

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

- **Integrasjon med eksternt API**: Viser sikker håndtering av API-nøkler og eksterne forespørsler
- **Tolkning av strukturert data**: Viser hvordan API-svar omformes til LLM-vennlige formater
- **Feilhåndtering**: Robust feilhåndtering med passende logging
- **Interaktiv klient**: Inkluderer både automatiserte tester og en interaktiv modus for testing
- **Kontekststyring**: Utnytter MCP Context for logging og sporing av forespørsler

## Forutsetninger

Før du begynner, sørg for at miljøet ditt er riktig satt opp ved å følge disse stegene. Dette sikrer at alle avhengigheter er installert og at API-nøklene dine er konfigurert korrekt for sømløs utvikling og testing.

- Python 3.8 eller nyere
- SerpAPI API-nøkkel (Registrer deg på [SerpAPI](https://serpapi.com/) – gratis nivå tilgjengelig)

## Installasjon

For å komme i gang, følg disse stegene for å sette opp miljøet ditt:

1. Installer avhengigheter med uv (anbefalt) eller pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Lag en `.env`-fil i prosjektets rotmappe med din SerpAPI-nøkkel:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Bruk

Web Search MCP Server er kjernen som eksponerer verktøy for web-, nyhets-, produkt-søk og Q&A ved å integrere med SerpAPI. Den håndterer innkommende forespørsler, styrer API-kall, tolker svar og returnerer strukturerte resultater til klienten.

Du kan se hele implementasjonen i [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Kjøre serveren

For å starte MCP-serveren, bruk følgende kommando:

```bash
python server.py
```

Serveren vil kjøre som en stdio-basert MCP-server som klienten kan koble til direkte.

### Klientmoduser

Klienten (`client.py`) støtter to moduser for å samhandle med MCP-serveren:

- **Normal modus**: Kjører automatiserte tester som bruker alle verktøyene og verifiserer svarene deres. Dette er nyttig for raskt å sjekke at serveren og verktøyene fungerer som forventet.
- **Interaktiv modus**: Starter et menybasert grensesnitt hvor du manuelt kan velge og kalle verktøy, skrive inn egne spørringer og se resultater i sanntid. Dette er ideelt for å utforske serverens funksjoner og eksperimentere med ulike input.

Du kan se hele implementasjonen i [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Kjøre klienten

For å kjøre de automatiserte testene (dette starter automatisk serveren):

```bash
python client.py
```

Eller kjør i interaktiv modus:

```bash
python client.py --interactive
```

### Testing med ulike metoder

Det finnes flere måter å teste og samhandle med verktøyene som serveren tilbyr, avhengig av dine behov og arbeidsflyt.

#### Skrive egne testskript med MCP Python SDK
Du kan også lage egne testskript ved å bruke MCP Python SDK:

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

I denne sammenhengen betyr et "testskript" et egendefinert Python-program du skriver for å fungere som klient mot MCP-serveren. I stedet for å være en formell enhetstest, lar dette skriptet deg programmere tilkobling til serveren, kalle hvilket som helst verktøy med valgte parametere, og inspisere resultatene. Denne tilnærmingen er nyttig for:
- Prototyping og eksperimentering med verktøysamtaler
- Validere hvordan serveren svarer på ulike input
- Automatisere gjentatte verktøy-kall
- Bygge egne arbeidsflyter eller integrasjoner på toppen av MCP-serveren

Du kan bruke testskript for raskt å prøve ut nye spørringer, feilsøke verktøysoppførsel, eller som utgangspunkt for mer avansert automatisering. Nedenfor er et eksempel på hvordan du bruker MCP Python SDK for å lage et slikt skript:

## Verktøybeskrivelser

Du kan bruke følgende verktøy som serveren tilbyr for å utføre ulike typer søk og spørringer. Hvert verktøy er beskrevet med parametere og eksempel på bruk.

Denne delen gir detaljer om hvert tilgjengelig verktøy og deres parametere.

### general_search

Utfører et generelt web-søk og returnerer formaterte resultater.

**Hvordan kalle dette verktøyet:**

Du kan kalle `general_search` fra ditt eget skript ved hjelp av MCP Python SDK, eller interaktivt via Inspector eller den interaktive klientmodusen. Her er et kodeeksempel med SDK:

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

Alternativt, i interaktiv modus, velg `general_search` fra menyen og skriv inn søket ditt når du blir bedt om det.

**Parametere:**
- `query` (string): Søkeord eller setning

**Eksempel på forespørsel:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Søker etter ferske nyhetsartikler relatert til en spørring.

**Hvordan kalle dette verktøyet:**

Du kan kalle `news_search` fra ditt eget skript ved hjelp av MCP Python SDK, eller interaktivt via Inspector eller den interaktive klientmodusen. Her er et kodeeksempel med SDK:

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

Alternativt, i interaktiv modus, velg `news_search` fra menyen og skriv inn søket ditt når du blir bedt om det.

**Parametere:**
- `query` (string): Søkeord eller setning

**Eksempel på forespørsel:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Søker etter produkter som matcher en spørring.

**Hvordan kalle dette verktøyet:**

Du kan kalle `product_search` fra ditt eget skript ved hjelp av MCP Python SDK, eller interaktivt via Inspector eller den interaktive klientmodusen. Her er et kodeeksempel med SDK:

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

Alternativt, i interaktiv modus, velg `product_search` fra menyen og skriv inn søket ditt når du blir bedt om det.

**Parametere:**
- `query` (string): Produktsøk-spørring

**Eksempel på forespørsel:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Henter direkte svar på spørsmål fra søkemotorer.

**Hvordan kalle dette verktøyet:**

Du kan kalle `qna` fra ditt eget skript ved hjelp av MCP Python SDK, eller interaktivt via Inspector eller den interaktive klientmodusen. Her er et kodeeksempel med SDK:

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

Alternativt, i interaktiv modus, velg `qna` fra menyen og skriv inn spørsmålet ditt når du blir bedt om det.

**Parametere:**
- `question` (string): Spørsmålet du vil ha svar på

**Eksempel på forespørsel:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Kodedetaljer

Denne delen gir kodeutdrag og referanser for server- og klientimplementasjonene.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Se [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) og [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) for fullstendige implementasjonsdetaljer.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Avanserte konsepter i denne leksen

Før du begynner å bygge, her er noen viktige avanserte konsepter som vil dukke opp gjennom hele kapitlet. Å forstå disse vil hjelpe deg å følge med, selv om du er ny på dem:

- **Orkestrering av flere verktøy**: Dette betyr å kjøre flere forskjellige verktøy (som web-søk, nyhetssøk, produktsøk og Q&A) innenfor én enkelt MCP-server. Det gjør at serveren kan håndtere en rekke oppgaver, ikke bare én.
- **Håndtering av API-ratebegrensninger**: Mange eksterne API-er (som SerpAPI) begrenser hvor mange forespørsler du kan sende i en gitt tidsperiode. God kode sjekker for disse begrensningene og håndterer dem på en smidig måte, slik at appen ikke krasjer hvis du når grensen.
- **Tolkning av strukturert data**: API-svar er ofte komplekse og nestede. Dette konseptet handler om å gjøre disse svarene om til rene, lettbrukte formater som er vennlige for LLM-er eller andre programmer.
- **Feilgjenoppretting**: Noen ganger går ting galt – kanskje nettverket feiler, eller API-et returnerer ikke det du forventer. Feilgjenoppretting betyr at koden din kan håndtere disse problemene og fortsatt gi nyttig tilbakemelding, i stedet for å krasje.
- **Validering av parametere**: Dette handler om å sjekke at alle input til verktøyene dine er korrekte og trygge å bruke. Det inkluderer å sette standardverdier og sikre at typene er riktige, noe som hjelper til å unngå feil og forvirring.

Denne delen vil hjelpe deg å diagnostisere og løse vanlige problemer du kan møte mens du jobber med Web Search MCP Server. Hvis du støter på feil eller uventet oppførsel, gir denne feilsøkingsdelen løsninger på de vanligste problemene. Gå gjennom disse tipsene før du søker videre hjelp – de løser ofte problemer raskt.

## Feilsøking

Når du jobber med Web Search MCP Server, kan du av og til støte på problemer – dette er normalt når du utvikler med eksterne API-er og nye verktøy. Denne delen gir praktiske løsninger på de vanligste problemene, slik at du raskt kan komme tilbake på sporet. Hvis du får en feil, start her: tipsene nedenfor tar for seg problemene de fleste brukere møter og kan ofte løse problemet uten ekstra hjelp.

### Vanlige problemer

Nedenfor er noen av de mest vanlige problemene brukere møter, med klare forklaringer og steg for å løse dem:

1. **Manglende SERPAPI_KEY i .env-filen**
   - Hvis du ser feilen `SERPAPI_KEY environment variable not found`, betyr det at applikasjonen ikke finner API-nøkkelen som trengs for å få tilgang til SerpAPI. For å fikse dette, lag en fil kalt `.env` i prosjektets rotmappe (hvis den ikke allerede finnes) og legg til en linje som `SERPAPI_KEY=din_serpapi_nøkkel_her`. Husk å bytte ut `din_serpapi_nøkkel_her` med din faktiske nøkkel fra SerpAPI-nettsiden.

2. **Modul ikke funnet-feil**
   - Feil som `ModuleNotFoundError: No module named 'httpx'` indikerer at en nødvendig Python-pakke mangler. Dette skjer vanligvis hvis du ikke har installert alle avhengigheter. For å løse dette, kjør `pip install -r requirements.txt` i terminalen for å installere alt prosjektet trenger.

3. **Tilkoblingsproblemer**
   - Hvis du får en feil som `Error during client execution`, betyr det ofte at klienten ikke klarer å koble til serveren, eller at serveren ikke kjører som forventet. Dobbeltsjekk at både klient og server er kompatible versjoner, og at `server.py` finnes og kjører i riktig mappe. Å starte både server og klient på nytt kan også hjelpe.

4. **SerpAPI-feil**
   - Feilen `Search API returned error status: 401` betyr at SerpAPI-nøkkelen din mangler, er feil eller utløpt. Gå til SerpAPI-dashbordet ditt, verifiser nøkkelen, og oppdater `.env`-filen om nødvendig. Hvis nøkkelen er korrekt, men du fortsatt får denne feilen, sjekk om gratisnivået ditt har brukt opp kvoten.

### Debug-modus

Som standard logger appen kun viktig informasjon. Hvis du vil se flere detaljer om hva som skjer (for eksempel for å feilsøke vanskelige problemer), kan du aktivere DEBUG-modus. Dette vil vise mye mer om hvert steg appen tar.

**Eksempel: Normal utdata**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Eksempel: DEBUG-utdata**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Legg merke til hvordan DEBUG-modus inkluderer ekstra linjer om HTTP-forespørsler, svar og andre interne detaljer. Dette kan være svært nyttig for feilsøking.
For å aktivere DEBUG-modus, sett loggnivået til DEBUG øverst i `client.py` eller `server.py`:

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

## Hva skjer videre

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
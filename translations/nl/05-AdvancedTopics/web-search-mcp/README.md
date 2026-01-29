# Les: Een Web Search MCP Server Bouwen

Dit hoofdstuk laat zien hoe je een realistische AI-agent bouwt die integreert met externe API's, verschillende datatypes verwerkt, fouten afhandelt en meerdere tools orkestreert—alles in een productieklare opzet. Je leert:

- **Integratie met externe API's die authenticatie vereisen**
- **Omgaan met diverse datatypes van meerdere eindpunten**
- **Robuuste foutafhandeling en logstrategieën**
- **Multi-tool orkestratie in één server**

Aan het einde heb je praktische ervaring met patronen en best practices die essentieel zijn voor geavanceerde AI- en LLM-gestuurde toepassingen.

## Introductie

In deze les leer je hoe je een geavanceerde MCP-server en client bouwt die LLM-mogelijkheden uitbreidt met realtime webdata via SerpAPI. Dit is een cruciale vaardigheid voor het ontwikkelen van dynamische AI-agenten die toegang hebben tot actuele informatie van het web.

## Leerdoelen

Aan het einde van deze les kun je:

- Externe API's (zoals SerpAPI) veilig integreren in een MCP-server
- Meerdere tools implementeren voor web-, nieuws-, productzoekopdrachten en Q&A
- Gestructureerde data parsen en formatteren voor LLM-gebruik
- Fouten afhandelen en API-rate limits effectief beheren
- Zowel geautomatiseerde als interactieve MCP-clients bouwen en testen

## Web Search MCP Server

In dit gedeelte wordt de architectuur en functionaliteit van de Web Search MCP Server geïntroduceerd. Je ziet hoe FastMCP en SerpAPI samen worden gebruikt om LLM-mogelijkheden uit te breiden met realtime webdata.

### Overzicht

Deze implementatie bevat vier tools die laten zien hoe MCP diverse, externe API-gedreven taken veilig en efficiënt kan afhandelen:

- **general_search**: Voor brede webresultaten
- **news_search**: Voor recente nieuwsberichten
- **product_search**: Voor e-commerce data
- **qna**: Voor vraag-en-antwoordfragmenten

### Kenmerken
- **Codevoorbeelden**: Bevat taalspecifieke codeblokken voor Python (en eenvoudig uitbreidbaar naar andere talen) met codepivots voor duidelijkheid

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

Voordat je de client start, is het handig om te begrijpen wat de server doet. Het bestand [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementeert de MCP-server en biedt tools voor web-, nieuws-, productzoekopdrachten en Q&A door integratie met SerpAPI. Het verwerkt binnenkomende verzoeken, beheert API-aanroepen, parseert antwoorden en retourneert gestructureerde resultaten aan de client.

Je kunt de volledige implementatie bekijken in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Hier is een kort voorbeeld van hoe de server een tool definieert en registreert:

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

- **Integratie met externe API's**: Laat zien hoe API-sleutels en externe verzoeken veilig worden afgehandeld
- **Gestructureerde data parsing**: Toont hoe API-antwoorden worden omgezet naar LLM-vriendelijke formaten
- **Foutafhandeling**: Robuuste foutafhandeling met passende logging
- **Interactieve client**: Bevat zowel geautomatiseerde tests als een interactieve modus voor testen
- **Contextbeheer**: Maakt gebruik van MCP Context voor logging en het volgen van verzoeken

## Vereisten

Voordat je begint, zorg dat je omgeving correct is ingesteld door deze stappen te volgen. Dit zorgt ervoor dat alle afhankelijkheden zijn geïnstalleerd en je API-sleutels correct zijn geconfigureerd voor een soepele ontwikkeling en testing.

- Python 3.8 of hoger
- SerpAPI API-sleutel (Meld je aan op [SerpAPI](https://serpapi.com/) - gratis tier beschikbaar)

## Installatie

Volg deze stappen om je omgeving op te zetten:

1. Installeer afhankelijkheden met uv (aanbevolen) of pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Maak een `.env`-bestand aan in de projectroot met je SerpAPI-sleutel:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Gebruik

De Web Search MCP Server is het kernonderdeel dat tools aanbiedt voor web-, nieuws-, productzoekopdrachten en Q&A door integratie met SerpAPI. Het verwerkt binnenkomende verzoeken, beheert API-aanroepen, parseert antwoorden en retourneert gestructureerde resultaten aan de client.

Je kunt de volledige implementatie bekijken in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Server starten

Om de MCP-server te starten, gebruik je het volgende commando:

```bash
python server.py
```

De server draait dan als een stdio-gebaseerde MCP-server waar de client direct verbinding mee kan maken.

### Client-modi

De client (`client.py`) ondersteunt twee modi om met de MCP-server te communiceren:

- **Normale modus**: Voert geautomatiseerde tests uit die alle tools aanroepen en hun antwoorden verifiëren. Dit is handig om snel te controleren of de server en tools naar behoren werken.
- **Interactieve modus**: Start een menu-gestuurde interface waarin je handmatig tools kunt selecteren en aanroepen, eigen zoekopdrachten kunt invoeren en resultaten realtime kunt bekijken. Ideaal om de mogelijkheden van de server te verkennen en te experimenteren met verschillende invoer.

Je kunt de volledige implementatie bekijken in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Client draaien

Om de geautomatiseerde tests uit te voeren (dit start automatisch de server):

```bash
python client.py
```

Of start in interactieve modus:

```bash
python client.py --interactive
```

### Testen met verschillende methoden

Er zijn meerdere manieren om de tools van de server te testen en ermee te werken, afhankelijk van je behoeften en workflow.

#### Eigen test-scripts schrijven met de MCP Python SDK
Je kunt ook je eigen test-scripts bouwen met de MCP Python SDK:

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

In deze context betekent een "test-script" een eigen Python-programma dat je schrijft om als client voor de MCP-server te fungeren. In plaats van een formele unittest, laat dit script je programmatisch verbinding maken met de server, een van de tools aanroepen met parameters naar keuze en de resultaten inspecteren. Deze aanpak is handig voor:
- Prototypen en experimenteren met tool-aanroepen
- Valideren hoe de server reageert op verschillende invoer
- Automatiseren van herhaalde tool-aanroepen
- Eigen workflows of integraties bouwen bovenop de MCP-server

Je kunt test-scripts gebruiken om snel nieuwe zoekopdrachten uit te proberen, toolgedrag te debuggen of als startpunt voor geavanceerdere automatisering. Hieronder een voorbeeld van hoe je de MCP Python SDK gebruikt om zo’n script te maken:

## Toolbeschrijvingen

Je kunt de volgende tools gebruiken die de server aanbiedt om verschillende soorten zoekopdrachten en queries uit te voeren. Elke tool wordt hieronder beschreven met zijn parameters en voorbeeldgebruik.

Deze sectie geeft details over elke beschikbare tool en hun parameters.

### general_search

Voert een algemene webzoekopdracht uit en retourneert geformatteerde resultaten.

**Hoe deze tool aan te roepen:**

Je kunt `general_search` aanroepen vanuit je eigen script met de MCP Python SDK, of interactief via de Inspector of de interactieve clientmodus. Hier is een codevoorbeeld met de SDK:

# [Python Voorbeeld](../../../../05-AdvancedTopics/web-search-mcp)

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

Of in interactieve modus, selecteer `general_search` in het menu en voer je zoekopdracht in wanneer daarom gevraagd wordt.

**Parameters:**
- `query` (string): De zoekopdracht

**Voorbeeldverzoek:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Zoekt naar recente nieuwsartikelen gerelateerd aan een zoekopdracht.

**Hoe deze tool aan te roepen:**

Je kunt `news_search` aanroepen vanuit je eigen script met de MCP Python SDK, of interactief via de Inspector of de interactieve clientmodus. Hier is een codevoorbeeld met de SDK:

# [Python Voorbeeld](../../../../05-AdvancedTopics/web-search-mcp)

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

Of in interactieve modus, selecteer `news_search` in het menu en voer je zoekopdracht in wanneer daarom gevraagd wordt.

**Parameters:**
- `query` (string): De zoekopdracht

**Voorbeeldverzoek:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Zoekt naar producten die overeenkomen met een zoekopdracht.

**Hoe deze tool aan te roepen:**

Je kunt `product_search` aanroepen vanuit je eigen script met de MCP Python SDK, of interactief via de Inspector of de interactieve clientmodus. Hier is een codevoorbeeld met de SDK:

# [Python Voorbeeld](../../../../05-AdvancedTopics/web-search-mcp)

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

Of in interactieve modus, selecteer `product_search` in het menu en voer je zoekopdracht in wanneer daarom gevraagd wordt.

**Parameters:**
- `query` (string): De productzoekopdracht

**Voorbeeldverzoek:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Geeft directe antwoorden op vragen van zoekmachines.

**Hoe deze tool aan te roepen:**

Je kunt `qna` aanroepen vanuit je eigen script met de MCP Python SDK, of interactief via de Inspector of de interactieve clientmodus. Hier is een codevoorbeeld met de SDK:

# [Python Voorbeeld](../../../../05-AdvancedTopics/web-search-mcp)

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

Of in interactieve modus, selecteer `qna` in het menu en voer je vraag in wanneer daarom gevraagd wordt.

**Parameters:**
- `question` (string): De vraag waarvoor je een antwoord zoekt

**Voorbeeldverzoek:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Code Details

Deze sectie bevat codefragmenten en verwijzingen voor de server- en clientimplementaties.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Zie [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) en [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) voor volledige implementatiedetails.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Geavanceerde Concepten in Deze Les

Voordat je begint met bouwen, zijn hier enkele belangrijke geavanceerde concepten die door dit hoofdstuk heen terugkomen. Ze begrijpen helpt je om beter te volgen, ook als ze nieuw voor je zijn:

- **Multi-tool Orkestratie**: Dit betekent dat je meerdere verschillende tools (zoals websearch, nieuwssearch, productsearch en Q&A) binnen één MCP-server draait. Zo kan je server verschillende taken aan, niet slechts één.
- **API Rate Limit Afhandeling**: Veel externe API's (zoals SerpAPI) beperken hoeveel verzoeken je in een bepaalde tijd mag doen. Goede code controleert deze limieten en gaat er netjes mee om, zodat je app niet crasht als je de limiet bereikt.
- **Gestructureerde Data Parsing**: API-antwoorden zijn vaak complex en genest. Dit concept gaat over het omzetten van die antwoorden naar schone, makkelijk te gebruiken formaten die vriendelijk zijn voor LLM's of andere programma's.
- **Foutherstel**: Soms gaat er iets mis—bijvoorbeeld een netwerkfout of een onverwacht API-antwoord. Foutherstel betekent dat je code deze problemen kan opvangen en toch nuttige feedback geeft, in plaats van te crashen.
- **Parameter Validatie**: Dit gaat over het controleren of alle invoer voor je tools correct en veilig is. Inclusief het instellen van standaardwaarden en het controleren van types, wat helpt bugs en verwarring te voorkomen.

Deze sectie helpt je om veelvoorkomende problemen te herkennen en op te lossen die je kunt tegenkomen bij het werken met de Web Search MCP Server. Als je fouten of onverwacht gedrag ervaart, biedt deze troubleshooting-sectie oplossingen voor de meest voorkomende issues. Bekijk deze tips eerst—ze lossen vaak problemen snel op.

## Problemen Oplossen

Bij het werken met de Web Search MCP Server kun je af en toe problemen tegenkomen—dat is normaal bij het ontwikkelen met externe API's en nieuwe tools. Deze sectie geeft praktische oplossingen voor de meest voorkomende problemen, zodat je snel weer verder kunt. Als je een fout tegenkomt, begin hier: de onderstaande tips behandelen de issues die de meeste gebruikers ervaren en kunnen vaak je probleem oplossen zonder extra hulp.

### Veelvoorkomende Problemen

Hieronder staan enkele van de meest voorkomende problemen met duidelijke uitleg en stappen om ze op te lossen:

1. **Ontbrekende SERPAPI_KEY in .env-bestand**
   - Als je de foutmelding `SERPAPI_KEY environment variable not found` ziet, betekent dit dat je applicatie de API-sleutel voor SerpAPI niet kan vinden. Maak een bestand `.env` aan in je projectroot (als dat nog niet bestaat) en voeg een regel toe zoals `SERPAPI_KEY=je_serpapi_sleutel_hier`. Vervang `je_serpapi_sleutel_hier` door je echte sleutel van de SerpAPI-website.

2. **Module niet gevonden fouten**
   - Fouten zoals `ModuleNotFoundError: No module named 'httpx'` geven aan dat een benodigde Python-package ontbreekt. Dit gebeurt meestal als je niet alle dependencies hebt geïnstalleerd. Los dit op door in je terminal `pip install -r requirements.txt` te draaien om alles te installeren wat je project nodig heeft.

3. **Verbindingsproblemen**
   - Als je een fout krijgt zoals `Error during client execution`, betekent dit vaak dat de client geen verbinding kan maken met de server, of dat de server niet draait zoals verwacht. Controleer of zowel client als server compatibele versies zijn en dat `server.py` aanwezig is en draait in de juiste map. Het herstarten van zowel server als client kan ook helpen.

4. **SerpAPI-fouten**
   - De melding `Search API returned error status: 401` betekent dat je SerpAPI-sleutel ontbreekt, onjuist is of verlopen. Ga naar je SerpAPI-dashboard, controleer je sleutel en werk je `.env`-bestand bij indien nodig. Als je sleutel correct is maar je ziet deze fout nog steeds, controleer dan of je gratis tier niet is opgebruikt.

### Debug-modus

Standaard logt de app alleen belangrijke informatie. Wil je meer details zien over wat er gebeurt (bijvoorbeeld om lastige problemen te diagnosticeren), dan kun je de DEBUG-modus inschakelen. Hiermee zie je veel meer over elke stap die de app neemt.

**Voorbeeld: Normale output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Voorbeeld: DEBUG-output**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Let op hoe de DEBUG-modus extra regels toont over HTTP-verzoeken, antwoorden en andere interne details. Dit is erg handig bij het oplossen van problemen.
Om de DEBUG-modus in te schakelen, stel je het logniveau in op DEBUG bovenaan je `client.py` of `server.py`:

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

## Wat volgt

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
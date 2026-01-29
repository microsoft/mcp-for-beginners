# Model Context Protocol (MCP) Python-implementatie

Deze repository bevat een Python-implementatie van het Model Context Protocol (MCP), waarin wordt getoond hoe je zowel een server- als een clientapplicatie kunt maken die communiceren via de MCP-standaard.

## Overzicht

De MCP-implementatie bestaat uit twee hoofdcomponenten:

1. **MCP Server (`server.py`)** - Een server die het volgende aanbiedt:
   - **Tools**: Functies die op afstand kunnen worden aangeroepen
   - **Resources**: Gegevens die opgevraagd kunnen worden
   - **Prompts**: Sjablonen voor het genereren van prompts voor taalmodellen

2. **MCP Client (`client.py`)** - Een clientapplicatie die verbinding maakt met de server en gebruikmaakt van de aangeboden functionaliteiten

## Functionaliteiten

Deze implementatie laat verschillende belangrijke MCP-functionaliteiten zien:

### Tools
- `completion` - Genereert tekstafwerkingen van AI-modellen (gesimuleerd)
- `add` - Eenvoudige rekenmachine die twee getallen optelt

### Resources
- `models://` - Geeft informatie over beschikbare AI-modellen
- `greeting://{name}` - Geeft een gepersonaliseerde begroeting voor een opgegeven naam

### Prompts
- `review_code` - Genereert een prompt voor het beoordelen van code

## Installatie

Om deze MCP-implementatie te gebruiken, installeer je de benodigde pakketten:

```powershell
pip install mcp-server mcp-client
```

## Server en Client starten

### Server starten

Start de server in een terminalvenster:

```powershell
python server.py
```

De server kan ook in ontwikkelmodus worden gestart met de MCP CLI:

```powershell
mcp dev server.py
```

Of geïnstalleerd worden in Claude Desktop (indien beschikbaar):

```powershell
mcp install server.py
```

### Client starten

Start de client in een ander terminalvenster:

```powershell
python client.py
```

Dit maakt verbinding met de server en demonstreert alle beschikbare functionaliteiten.

### Client gebruik

De client (`client.py`) laat alle MCP-mogelijkheden zien:

```powershell
python client.py
```

Dit maakt verbinding met de server en gebruikt alle functies, inclusief tools, resources en prompts. De output toont:

1. Resultaat van de rekenmachine-tool (5 + 7 = 12)
2. Reactie van de completion-tool op "What is the meaning of life?"
3. Lijst van beschikbare AI-modellen
4. Gepersonaliseerde begroeting voor "MCP Explorer"
5. Prompt-sjabloon voor code review

## Implementatiedetails

De server is geïmplementeerd met de `FastMCP` API, die hoog-niveau abstracties biedt voor het definiëren van MCP-diensten. Hier is een vereenvoudigd voorbeeld van hoe tools worden gedefinieerd:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

De client gebruikt de MCP clientbibliotheek om verbinding te maken met en aanroepen te doen naar de server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Meer informatie

Voor meer informatie over MCP, bezoek: https://modelcontextprotocol.io/

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
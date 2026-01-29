# Model Context Protocol (MCP) Python-implementation

Det här arkivet innehåller en Python-implementation av Model Context Protocol (MCP) som visar hur man skapar både en server- och klientapplikation som kommunicerar med MCP-standarden.

## Översikt

MCP-implementationen består av två huvudkomponenter:

1. **MCP Server (`server.py`)** – En server som exponerar:
   - **Verktyg**: Funktioner som kan anropas på distans
   - **Resurser**: Data som kan hämtas
   - **Prompter**: Mallar för att generera prompts för språkmodeller

2. **MCP Klient (`client.py`)** – En klientapplikation som ansluter till servern och använder dess funktioner

## Funktioner

Denna implementation visar flera viktiga MCP-funktioner:

### Verktyg
- `completion` – Genererar textkompletteringar från AI-modeller (simulerat)
- `add` – Enkel kalkylator som adderar två tal

### Resurser
- `models://` – Returnerar information om tillgängliga AI-modeller
- `greeting://{name}` – Returnerar en personlig hälsning för ett givet namn

### Prompter
- `review_code` – Genererar en prompt för kodgranskning

## Installation

För att använda denna MCP-implementation, installera de nödvändiga paketen:

```powershell
pip install mcp-server mcp-client
```

## Köra Server och Klient

### Starta Servern

Kör servern i ett terminalfönster:

```powershell
python server.py
```

Servern kan också köras i utvecklingsläge med MCP CLI:

```powershell
mcp dev server.py
```

Eller installeras i Claude Desktop (om tillgängligt):

```powershell
mcp install server.py
```

### Köra Klienten

Kör klienten i ett annat terminalfönster:

```powershell
python client.py
```

Detta ansluter till servern och demonstrerar alla tillgängliga funktioner.

### Användning av Klienten

Klienten (`client.py`) visar alla MCP-funktioner:

```powershell
python client.py
```

Detta ansluter till servern och testar alla funktioner inklusive verktyg, resurser och prompter. Utdata visar:

1. Resultat från kalkylatorverktyget (5 + 7 = 12)
2. Svar från completion-verktyget på "What is the meaning of life?"
3. Lista över tillgängliga AI-modeller
4. Personlig hälsning till "MCP Explorer"
5. Promptmall för kodgranskning

## Implementationsdetaljer

Servern är implementerad med `FastMCP` API:et, som erbjuder högre abstraktioner för att definiera MCP-tjänster. Här är ett förenklat exempel på hur verktyg definieras:

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

Klienten använder MCP-klientbiblioteket för att ansluta till och anropa servern:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Läs mer

För mer information om MCP, besök: https://modelcontextprotocol.io/

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
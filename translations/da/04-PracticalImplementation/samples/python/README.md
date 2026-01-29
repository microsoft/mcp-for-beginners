# Model Context Protocol (MCP) Python-implementering

Dette repository indeholder en Python-implementering af Model Context Protocol (MCP), som viser, hvordan man opretter både en server- og en klientapplikation, der kommunikerer ved hjælp af MCP-standarden.

## Oversigt

MCP-implementeringen består af to hovedkomponenter:

1. **MCP Server (`server.py`)** - En server, der eksponerer:
   - **Værktøjer**: Funktioner, der kan kaldes eksternt
   - **Ressourcer**: Data, der kan hentes
   - **Prompter**: Skabeloner til at generere prompts til sprogmodeller

2. **MCP Klient (`client.py`)** - En klientapplikation, der forbinder til serveren og bruger dens funktioner

## Funktioner

Denne implementering demonstrerer flere centrale MCP-funktioner:

### Værktøjer
- `completion` - Genererer tekstfuldførelser fra AI-modeller (simuleret)
- `add` - Enkel lommeregner, der lægger to tal sammen

### Ressourcer
- `models://` - Returnerer information om tilgængelige AI-modeller
- `greeting://{name}` - Returnerer en personlig hilsen til et givent navn

### Prompter
- `review_code` - Genererer en prompt til kodegennemgang

## Installation

For at bruge denne MCP-implementering, installer de nødvendige pakker:

```powershell
pip install mcp-server mcp-client
```

## Kørsel af Server og Klient

### Start af Server

Kør serveren i et terminalvindue:

```powershell
python server.py
```

Serveren kan også køres i udviklingstilstand ved hjælp af MCP CLI:

```powershell
mcp dev server.py
```

Eller installeres i Claude Desktop (hvis tilgængelig):

```powershell
mcp install server.py
```

### Kørsel af Klient

Kør klienten i et andet terminalvindue:

```powershell
python client.py
```

Dette vil forbinde til serveren og demonstrere alle tilgængelige funktioner.

### Klientbrug

Klienten (`client.py`) demonstrerer alle MCP-funktionaliteter:

```powershell
python client.py
```

Dette vil forbinde til serveren og afprøve alle funktioner, inklusive værktøjer, ressourcer og prompter. Outputtet vil vise:

1. Resultat fra lommeregner-værktøjet (5 + 7 = 12)
2. Svar fra completion-værktøjet på "What is the meaning of life?"
3. Liste over tilgængelige AI-modeller
4. Personlig hilsen til "MCP Explorer"
5. Skabelon til kodegennemgangsprompt

## Implementeringsdetaljer

Serveren er implementeret ved hjælp af `FastMCP` API’en, som tilbyder højniveau-abstraktioner til at definere MCP-tjenester. Her er et forenklet eksempel på, hvordan værktøjer defineres:

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

Klienten bruger MCP-klientbiblioteket til at forbinde til og kalde serveren:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Lær Mere

For mere information om MCP, besøg: https://modelcontextprotocol.io/

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
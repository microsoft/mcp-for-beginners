# Model Context Protocol (MCP) Python-implementasjon

Dette depotet inneholder en Python-implementasjon av Model Context Protocol (MCP), som viser hvordan man kan lage både en server- og klientapplikasjon som kommuniserer ved hjelp av MCP-standarden.

## Oversikt

MCP-implementasjonen består av to hovedkomponenter:

1. **MCP Server (`server.py`)** – En server som eksponerer:
   - **Verktøy**: Funksjoner som kan kalles eksternt
   - **Ressurser**: Data som kan hentes
   - **Prompter**: Maler for å generere prompter til språkmodeller

2. **MCP Klient (`client.py`)** – En klientapplikasjon som kobler til serveren og bruker dens funksjoner

## Funksjoner

Denne implementasjonen demonstrerer flere viktige MCP-funksjoner:

### Verktøy
- `completion` – Genererer tekstfullføringer fra AI-modeller (simulert)
- `add` – Enkel kalkulator som legger sammen to tall

### Ressurser
- `models://` – Returnerer informasjon om tilgjengelige AI-modeller
- `greeting://{name}` – Returnerer en personlig hilsen til et gitt navn

### Prompter
- `review_code` – Genererer en prompt for kodegjennomgang

## Installasjon

For å bruke denne MCP-implementasjonen, installer de nødvendige pakkene:

```powershell
pip install mcp-server mcp-client
```

## Kjøre Server og Klient

### Starte Serveren

Kjør serveren i et terminalvindu:

```powershell
python server.py
```

Serveren kan også kjøres i utviklingsmodus ved hjelp av MCP CLI:

```powershell
mcp dev server.py
```

Eller installeres i Claude Desktop (hvis tilgjengelig):

```powershell
mcp install server.py
```

### Kjøre Klienten

Kjør klienten i et annet terminalvindu:

```powershell
python client.py
```

Dette vil koble til serveren og demonstrere alle tilgjengelige funksjoner.

### Bruk av Klient

Klienten (`client.py`) demonstrerer alle MCP-funksjonaliteter:

```powershell
python client.py
```

Dette vil koble til serveren og teste alle funksjoner, inkludert verktøy, ressurser og prompter. Resultatet vil vise:

1. Kalkulatorverktøyets resultat (5 + 7 = 12)
2. Svar fra completion-verktøyet på "What is the meaning of life?"
3. Liste over tilgjengelige AI-modeller
4. Personlig hilsen til "MCP Explorer"
5. Mal for kodegjennomgangsprompt

## Implementasjonsdetaljer

Serveren er implementert ved hjelp av `FastMCP` API, som gir høynivåabstraksjoner for å definere MCP-tjenester. Her er et forenklet eksempel på hvordan verktøy defineres:

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

Klienten bruker MCP-klientbiblioteket for å koble til og kalle serveren:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Lær mer

For mer informasjon om MCP, besøk: https://modelcontextprotocol.io/

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
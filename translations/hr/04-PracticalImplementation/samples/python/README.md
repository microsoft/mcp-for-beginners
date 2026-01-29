# Model Context Protocol (MCP) Python implementacija

Ovaj repozitorij sadrži Python implementaciju Model Context Protocol (MCP), koja pokazuje kako kreirati i serversku i klijentsku aplikaciju koje komuniciraju koristeći MCP standard.

## Pregled

MCP implementacija sastoji se od dva glavna dijela:

1. **MCP Server (`server.py`)** - Server koji izlaže:
   - **Alate**: Funkcije koje se mogu pozivati na daljinu
   - **Resurse**: Podatke koji se mogu dohvatiti
   - **Promptove**: Predloške za generiranje promptova za jezične modele

2. **MCP Klijent (`client.py`)** - Klijentska aplikacija koja se povezuje na server i koristi njegove funkcionalnosti

## Značajke

Ova implementacija demonstrira nekoliko ključnih MCP značajki:

### Alati
- `completion` - Generira tekstualne dovršetke iz AI modela (simulirano)
- `add` - Jednostavan kalkulator koji zbraja dva broja

### Resursi
- `models://` - Vraća informacije o dostupnim AI modelima
- `greeting://{name}` - Vraća personaliziranu pozdravnu poruku za zadano ime

### Promptovi
- `review_code` - Generira prompt za pregled koda

## Instalacija

Za korištenje ove MCP implementacije, instalirajte potrebne pakete:

```powershell
pip install mcp-server mcp-client
```

## Pokretanje servera i klijenta

### Pokretanje servera

Pokrenite server u jednom terminalu:

```powershell
python server.py
```

Server se može pokrenuti i u razvojnom načinu rada koristeći MCP CLI:

```powershell
mcp dev server.py
```

Ili instalirati u Claude Desktop (ako je dostupan):

```powershell
mcp install server.py
```

### Pokretanje klijenta

Pokrenite klijenta u drugom terminalu:

```powershell
python client.py
```

Ovo će se povezati na server i demonstrirati sve dostupne značajke.

### Korištenje klijenta

Klijent (`client.py`) demonstrira sve MCP mogućnosti:

```powershell
python client.py
```

Ovo će se povezati na server i isprobati sve značajke uključujući alate, resurse i promptove. Izlaz će prikazati:

1. Rezultat kalkulatora (5 + 7 = 12)
2. Odgovor alata za dovršetak na pitanje "What is the meaning of life?"
3. Popis dostupnih AI modela
4. Personalizirani pozdrav za "MCP Explorer"
5. Predložak prompta za pregled koda

## Detalji implementacije

Server je implementiran koristeći `FastMCP` API, koji pruža visoke apstrakcije za definiranje MCP servisa. Evo pojednostavljenog primjera kako se definiraju alati:

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

Klijent koristi MCP klijentsku biblioteku za povezivanje i pozivanje servera:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Saznajte više

Za više informacija o MCP-u, posjetite: https://modelcontextprotocol.io/

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
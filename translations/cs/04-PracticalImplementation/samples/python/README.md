# Model Context Protocol (MCP) Python Implementace

Tento repozitář obsahuje Python implementaci Model Context Protocolu (MCP), která ukazuje, jak vytvořit serverovou i klientskou aplikaci komunikující pomocí standardu MCP.

## Přehled

Implementace MCP se skládá ze dvou hlavních částí:

1. **MCP Server (`server.py`)** – Server, který zpřístupňuje:
   - **Nástroje**: Funkce, které lze volat vzdáleně
   - **Zdroje**: Data, která lze získat
   - **Výzvy**: Šablony pro generování výzev pro jazykové modely

2. **MCP Klient (`client.py`)** – Klientská aplikace, která se připojuje k serveru a využívá jeho funkce

## Funkce

Tato implementace demonstruje několik klíčových funkcí MCP:

### Nástroje
- `completion` – Generuje textová dokončení z AI modelů (simulováno)
- `add` – Jednoduchá kalkulačka, která sčítá dvě čísla

### Zdroje
- `models://` – Vrací informace o dostupných AI modelech
- `greeting://{name}` – Vrací personalizovaný pozdrav pro zadané jméno

### Výzvy
- `review_code` – Generuje výzvu pro kontrolu kódu

## Instalace

Pro použití této MCP implementace nainstalujte požadované balíčky:

```powershell
pip install mcp-server mcp-client
```

## Spuštění serveru a klienta

### Spuštění serveru

Spusťte server v jednom terminálovém okně:

```powershell
python server.py
```

Server lze také spustit v režimu vývoje pomocí MCP CLI:

```powershell
mcp dev server.py
```

Nebo jej nainstalovat do Claude Desktop (pokud je k dispozici):

```powershell
mcp install server.py
```

### Spuštění klienta

Spusťte klienta v jiném terminálovém okně:

```powershell
python client.py
```

Tím se připojíte k serveru a vyzkoušíte všechny dostupné funkce.

### Použití klienta

Klient (`client.py`) demonstruje všechny schopnosti MCP:

```powershell
python client.py
```

Tím se připojíte k serveru a vyzkoušíte všechny funkce včetně nástrojů, zdrojů a výzev. Výstup zobrazí:

1. Výsledek kalkulačky (5 + 7 = 12)
2. Odpověď nástroje completion na otázku „Jaký je smysl života?“
3. Seznam dostupných AI modelů
4. Personalizovaný pozdrav pro „MCP Explorer“
5. Šablonu výzvy pro kontrolu kódu

## Detaily implementace

Server je implementován pomocí API `FastMCP`, které poskytuje vysoce úrovňové abstrakce pro definování MCP služeb. Zde je zjednodušený příklad definice nástrojů:

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

Klient používá MCP klientskou knihovnu pro připojení a volání serveru:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Další informace

Pro více informací o MCP navštivte: https://modelcontextprotocol.io/

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
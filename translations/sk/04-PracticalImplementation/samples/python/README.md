# Model Context Protocol (MCP) Python implementácia

Tento repozitár obsahuje Python implementáciu Model Context Protocol (MCP), ktorá ukazuje, ako vytvoriť serverovú aj klientsku aplikáciu komunikujúcu pomocou štandardu MCP.

## Prehľad

Implementácia MCP pozostáva z dvoch hlavných častí:

1. **MCP Server (`server.py`)** – Server, ktorý poskytuje:
   - **Nástroje**: Funkcie, ktoré je možné volať na diaľku
   - **Zdroje**: Dáta, ktoré je možné získať
   - **Výzvy (Prompts)**: Šablóny na generovanie výziev pre jazykové modely

2. **MCP Klient (`client.py`)** – Klientská aplikácia, ktorá sa pripája k serveru a využíva jeho funkcie

## Funkcie

Táto implementácia demonštruje niekoľko kľúčových vlastností MCP:

### Nástroje
- `completion` – Generuje textové dokončenia z AI modelov (simulované)
- `add` – Jednoduchá kalkulačka, ktorá sčíta dve čísla

### Zdroje
- `models://` – Vracia informácie o dostupných AI modeloch
- `greeting://{name}` – Vracia personalizované pozdravy pre zadané meno

### Výzvy (Prompts)
- `review_code` – Generuje výzvu na kontrolu kódu

## Inštalácia

Na použitie tejto MCP implementácie nainštalujte potrebné balíky:

```powershell
pip install mcp-server mcp-client
```

## Spustenie servera a klienta

### Spustenie servera

Server spustite v jednom terminálovom okne:

```powershell
python server.py
```

Server je možné spustiť aj v režime vývoja pomocou MCP CLI:

```powershell
mcp dev server.py
```

Alebo ho nainštalovať do Claude Desktop (ak je dostupný):

```powershell
mcp install server.py
```

### Spustenie klienta

Klienta spustite v inom terminálovom okne:

```powershell
python client.py
```

Tým sa klient pripojí k serveru a predvedie všetky dostupné funkcie.

### Použitie klienta

Klient (`client.py`) demonštruje všetky schopnosti MCP:

```powershell
python client.py
```

Tým sa klient pripojí k serveru a využije všetky funkcie vrátane nástrojov, zdrojov a výziev. Výstup zobrazí:

1. Výsledok kalkulačky (5 + 7 = 12)
2. Odpoveď nástroja completion na otázku „What is the meaning of life?“
3. Zoznam dostupných AI modelov
4. Personalizovaný pozdrav pre „MCP Explorer“
5. Šablónu výzvy na kontrolu kódu

## Detaily implementácie

Server je implementovaný pomocou API `FastMCP`, ktoré poskytuje vysokú úroveň abstrakcie pre definovanie MCP služieb. Tu je zjednodušený príklad definície nástrojov:

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

Klient používa MCP klientskú knižnicu na pripojenie a volanie servera:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Viac informácií

Pre viac informácií o MCP navštívte: https://modelcontextprotocol.io/

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
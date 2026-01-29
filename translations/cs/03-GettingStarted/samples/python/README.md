# MCP Kalkulační Server (Python)

Jednoduchá implementace serveru Model Context Protocol (MCP) v Pythonu, která poskytuje základní funkce kalkulačky.

## Instalace

Nainstalujte potřebné závislosti:

```bash
pip install -r requirements.txt
```

Nebo přímo nainstalujte MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Použití

### Spuštění serveru

Server je navržen tak, aby ho používali MCP klienti (například Claude Desktop). Pro spuštění serveru:

```bash
python mcp_calculator_server.py
```

**Poznámka**: Při přímém spuštění v terminálu uvidíte chyby validace JSON-RPC. To je normální chování - server čeká na správně formátované zprávy od MCP klienta.

### Testování funkcí

Pro otestování, zda funkce kalkulačky fungují správně:

```bash
python test_calculator.py
```

## Řešení problémů

### Chyby při importu

Pokud se zobrazí `ModuleNotFoundError: No module named 'mcp'`, nainstalujte MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Chyby JSON-RPC při přímém spuštění

Chyby jako "Invalid JSON: EOF while parsing a value" při přímém spuštění serveru jsou očekávané. Server potřebuje zprávy od MCP klienta, nikoli přímý vstup z terminálu.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
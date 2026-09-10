# MCP Calculator Server (Python)



Jednoduchá implementace Model Context Protocol (MCP) serveru v Pythonu, která poskytuje základní funkcionalitu kalkulačky.


## Instalace

Nainstalujte požadované závislosti:

```bash
pip install -r requirements.txt
```

Nebo nainstalujte MCP Python SDK přímo:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Použití

### Spuštění serveru

Server je navržen tak, aby jej používali MCP klienti (jako Claude Desktop). Pro spuštění serveru:

```bash
python mcp_calculator_server.py
```

**Poznámka**: Při přímém spuštění v terminálu uvidíte chyby validace JSON-RPC. Toto je normální chování – server čeká na správně formátované zprávy od MCP klientů.

### Testování funkcí

Pro otestování, že funkce kalkulačky fungují správně:

```bash
python test_calculator.py
```

## Řešení problémů

### Chyby importu

Pokud se vám zobrazí `ModuleNotFoundError: No module named 'mcp'`, nainstalujte MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Chyby JSON-RPC při přímém spuštění

Chyby jako "Invalid JSON: EOF while parsing a value" při přímém spuštění serveru jsou očekávané. Server potřebuje zprávy od MCP klientů, nikoli přímý vstup z terminálu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
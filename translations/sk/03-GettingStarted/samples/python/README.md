# MCP Kalkulačka Server (Python)

Jednoduchá implementácia servera Model Context Protocol (MCP) v Pythone, ktorá poskytuje základnú funkcionalitu kalkulačky.

## Inštalácia

Nainštalujte potrebné závislosti:

```bash
pip install -r requirements.txt
```

Alebo nainštalujte priamo MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Použitie

### Spustenie servera

Server je navrhnutý na použitie klientmi MCP (napríklad Claude Desktop). Na spustenie servera:

```bash
python mcp_calculator_server.py
```

**Poznámka**: Pri priamom spustení v termináli uvidíte chyby validácie JSON-RPC. Toto je normálne správanie - server čaká na správne formátované správy od MCP klienta.

### Testovanie funkcií

Na otestovanie, či funkcie kalkulačky fungujú správne:

```bash
python test_calculator.py
```

## Riešenie problémov

### Chyby pri importe

Ak sa zobrazí `ModuleNotFoundError: No module named 'mcp'`, nainštalujte MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Chyby JSON-RPC pri priamom spustení

Chyby ako "Invalid JSON: EOF while parsing a value" pri priamom spustení servera sú očakávané. Server potrebuje správy od MCP klienta, nie priamy vstup z terminálu.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
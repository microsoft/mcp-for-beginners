# MCP Kalkulačný Server (Python)



Jednoduchá implementácia Model Context Protocol (MCP) servera v Pythone, ktorý poskytuje základnú kalkulačnú funkcionalitu.


## Inštalácia

Nainštalujte potrebné závislosti:

```bash
pip install -r requirements.txt
```

Alebo nainštalujte MCP Python SDK priamo:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Použitie

### Spustenie Servera

Server je navrhnutý na použitie MCP klientmi (ako Claude Desktop). Na spustenie servera:

```bash
python mcp_calculator_server.py
```

**Poznámka**: Pri spustení priamo v termináli uvidíte chyby overenia JSON-RPC. Toto je normálne správanie - server čaká na správne naformátované správy od MCP klientov.

### Testovanie Funkcií

Ak chcete otestovať, či kalkulačné funkcie fungujú správne:

```bash
python test_calculator.py
```

## Riešenie Problémov

### Chyby Importu

Ak sa objaví `ModuleNotFoundError: No module named 'mcp'`, nainštalujte MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Chyby JSON-RPC Pri Priamo Spustení

Očakávajú sa chyby ako „Invalid JSON: EOF while parsing a value“ pri priamom spustení servera. Server potrebuje správy od MCP klienta, nie priame vstupy z terminálu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
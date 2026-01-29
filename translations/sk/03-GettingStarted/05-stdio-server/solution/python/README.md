# MCP stdio Server - Python Riešenie

> **⚠️ Dôležité**: Toto riešenie bolo aktualizované na používanie **stdio transportu** podľa odporúčaní MCP špecifikácie z 2025-06-18. Pôvodný SSE transport bol vyradený.

## Prehľad

Toto Python riešenie demonštruje, ako vytvoriť MCP server pomocou aktuálneho stdio transportu. Stdio transport je jednoduchší, bezpečnejší a poskytuje lepší výkon ako zastaraný SSE prístup.

## Predpoklady

- Python 3.8 alebo novší
- Odporúča sa nainštalovať `uv` na správu balíkov, pozrite si [inštrukcie](https://docs.astral.sh/uv/#highlights)

## Inštrukcie na nastavenie

### Krok 1: Vytvorte virtuálne prostredie

```bash
python -m venv venv
```

### Krok 2: Aktivujte virtuálne prostredie

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Krok 3: Nainštalujte závislosti

```bash
pip install mcp
```

## Spustenie servera

Stdio server funguje inak ako starý SSE server. Namiesto spustenia webového servera komunikuje cez stdin/stdout:

```bash
python server.py
```

**Dôležité**: Server sa môže zdať, že zamrzol - to je normálne! Čaká na JSON-RPC správy zo stdin.

## Testovanie servera

### Metóda 1: Použitie MCP Inspector (Odporúčané)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Toto:
1. Spustí váš server ako podproces
2. Otvorí webové rozhranie na testovanie
3. Umožní vám interaktívne testovať všetky nástroje servera

### Metóda 2: Priame testovanie JSON-RPC

Môžete tiež testovať posielaním JSON-RPC správ priamo:

1. Spustite server: `python server.py`
2. Pošlite JSON-RPC správu (príklad):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server odpovie dostupnými nástrojmi

### Dostupné nástroje

Server poskytuje tieto nástroje:

- **add(a, b)**: Sčíta dve čísla
- **multiply(a, b)**: Vynásobí dve čísla  
- **get_greeting(name)**: Vytvorí personalizovaný pozdrav
- **get_server_info()**: Poskytne informácie o serveri

### Testovanie s Claude Desktop

Ak chcete použiť tento server s Claude Desktop, pridajte túto konfiguráciu do vášho `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Kľúčové rozdiely oproti SSE

**stdio transport (Aktuálny):**
- ✅ Jednoduchšie nastavenie - nie je potrebný webový server
- ✅ Lepšia bezpečnosť - žiadne HTTP endpointy
- ✅ Komunikácia založená na podprocesoch
- ✅ JSON-RPC cez stdin/stdout
- ✅ Lepší výkon

**SSE transport (Zastaraný):**
- ❌ Vyžadoval nastavenie HTTP servera
- ❌ Potreboval webový framework (Starlette/FastAPI)
- ❌ Zložitejšie smerovanie a správa relácií
- ❌ Dodatočné bezpečnostné úvahy
- ❌ Teraz vyradený v MCP 2025-06-18

## Tipy na ladenie

- Používajte `stderr` na logovanie (nikdy `stdout`)
- Testujte s Inspectorom na vizuálne ladenie
- Uistite sa, že všetky JSON správy sú oddelené novým riadkom
- Skontrolujte, či server štartuje bez chýb

Toto riešenie nasleduje aktuálnu MCP špecifikáciu a demonštruje najlepšie praktiky pre implementáciu stdio transportu.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
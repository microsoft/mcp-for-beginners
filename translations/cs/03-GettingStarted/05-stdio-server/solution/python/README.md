# MCP stdio Server - Python řešení

> **⚠️ Důležité**: Toto řešení bylo aktualizováno tak, aby používalo **stdio transport**, jak je doporučeno v MCP Specifikaci 2025-06-18. Původní SSE transport byl zrušen.

## Přehled

Toto Python řešení ukazuje, jak vytvořit MCP server pomocí aktuálního stdio transportu. Stdio transport je jednodušší, bezpečnější a poskytuje lepší výkon než zastaralý přístup SSE.

## Předpoklady

- Python 3.8 nebo novější
- Doporučuje se nainstalovat `uv` pro správu balíčků, viz [instrukce](https://docs.astral.sh/uv/#highlights)

## Pokyny k nastavení

### Krok 1: Vytvořte virtuální prostředí

```bash
python -m venv venv
```

### Krok 2: Aktivujte virtuální prostředí

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Krok 3: Nainstalujte závislosti

```bash
pip install mcp
```

## Spuštění serveru

Stdio server funguje jinak než starý SSE server. Namísto spuštění webového serveru komunikuje přes stdin/stdout:

```bash
python server.py
```

**Důležité**: Server se může zdát, že "zamrzl" - to je normální! Čeká na JSON-RPC zprávy ze stdin.

## Testování serveru

### Metoda 1: Použití MCP Inspector (doporučeno)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Tímto:
1. Spustíte server jako podproces
2. Otevřete webové rozhraní pro testování
3. Umožníte interaktivní testování všech nástrojů serveru

### Metoda 2: Přímé testování JSON-RPC

Můžete také testovat zasíláním JSON-RPC zpráv přímo:

1. Spusťte server: `python server.py`
2. Odešlete JSON-RPC zprávu (příklad):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server odpoví dostupnými nástroji

### Dostupné nástroje

Server poskytuje tyto nástroje:

- **add(a, b)**: Sečte dvě čísla
- **multiply(a, b)**: Vynásobí dvě čísla  
- **get_greeting(name)**: Vytvoří personalizovaný pozdrav
- **get_server_info()**: Získá informace o serveru

### Testování s Claude Desktop

Pro použití tohoto serveru s Claude Desktop přidejte tuto konfiguraci do svého `claude_desktop_config.json`:

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

## Klíčové rozdíly oproti SSE

**stdio transport (aktuální):**
- ✅ Jednodušší nastavení - není potřeba webový server
- ✅ Lepší bezpečnost - žádné HTTP endpointy
- ✅ Komunikace založená na podprocesech
- ✅ JSON-RPC přes stdin/stdout
- ✅ Lepší výkon

**SSE transport (zastaralý):**
- ❌ Vyžadoval nastavení HTTP serveru
- ❌ Potřeboval webový framework (Starlette/FastAPI)
- ❌ Složitější směrování a správa relací
- ❌ Další bezpečnostní úvahy
- ❌ Nyní zrušen v MCP 2025-06-18

## Tipy pro ladění

- Používejte `stderr` pro logování (nikdy `stdout`)
- Testujte pomocí Inspectoru pro vizuální ladění
- Ujistěte se, že všechny JSON zprávy jsou odděleny novým řádkem
- Zkontrolujte, zda server startuje bez chyb

Toto řešení odpovídá aktuální MCP specifikaci a ukazuje nejlepší postupy pro implementaci stdio transportu.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
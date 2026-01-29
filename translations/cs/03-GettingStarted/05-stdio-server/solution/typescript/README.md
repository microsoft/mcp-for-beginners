# MCP stdio Server - TypeScript Řešení

> **⚠️ Důležité**: Toto řešení bylo aktualizováno na použití **stdio transportu**, jak je doporučeno ve specifikaci MCP 2025-06-18. Původní SSE transport byl zrušen.

## Přehled

Toto TypeScript řešení ukazuje, jak vytvořit MCP server pomocí aktuálního stdio transportu. Stdio transport je jednodušší, bezpečnější a poskytuje lepší výkon než zastaralý přístup SSE.

## Předpoklady

- Node.js 18+ nebo novější
- Správce balíčků npm nebo yarn

## Pokyny k nastavení

### Krok 1: Instalace závislostí

```bash
npm install
```

### Krok 2: Sestavení projektu

```bash
npm run build
```

## Spuštění serveru

Stdio server funguje jinak než starý SSE server. Místo spuštění webového serveru komunikuje přes stdin/stdout:

```bash
npm start
```

**Důležité**: Server se může zdát, že "zamrzl" - to je normální! Čeká na JSON-RPC zprávy ze stdin.

## Testování serveru

### Metoda 1: Použití MCP Inspectoru (doporučeno)

```bash
npm run inspector
```

Tímto:
1. Spustíte server jako podproces
2. Otevřete webové rozhraní pro testování
3. Umožníte interaktivní testování všech nástrojů serveru

### Metoda 2: Přímé testování z příkazové řádky

Můžete také testovat spuštěním Inspectoru přímo:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Dostupné nástroje

Server poskytuje tyto nástroje:

- **add(a, b)**: Sečte dvě čísla
- **multiply(a, b)**: Vynásobí dvě čísla  
- **get_greeting(name)**: Vytvoří personalizovaný pozdrav
- **get_server_info()**: Získá informace o serveru

### Testování s Claude Desktop

Pro použití tohoto serveru s Claude Desktop přidejte tuto konfiguraci do souboru `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Struktura projektu

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Klíčové rozdíly oproti SSE

**stdio transport (aktuální):**
- ✅ Jednodušší nastavení - není potřeba HTTP server
- ✅ Lepší zabezpečení - žádné HTTP endpointy
- ✅ Komunikace založená na podprocesech
- ✅ JSON-RPC přes stdin/stdout
- ✅ Lepší výkon

**SSE transport (zastaralý):**
- ❌ Vyžadoval nastavení Express serveru
- ❌ Potřeboval složité směrování a správu relací
- ❌ Více závislostí (Express, HTTP zpracování)
- ❌ Další bezpečnostní úvahy
- ❌ Nyní zrušen ve specifikaci MCP 2025-06-18

## Tipy pro vývoj

- Používejte `console.error()` pro logování (nikdy `console.log()`, protože zapisuje do stdout)
- Před testováním sestavte pomocí `npm run build`
- Testujte pomocí Inspectoru pro vizuální ladění
- Ujistěte se, že všechny JSON zprávy jsou správně formátované
- Server automaticky zpracovává plynulé ukončení při SIGINT/SIGTERM

Toto řešení odpovídá aktuální specifikaci MCP a ukazuje osvědčené postupy pro implementaci stdio transportu pomocí TypeScriptu.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
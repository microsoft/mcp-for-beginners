# MCP stdio Server - TypeScript Riešenie

> **⚠️ Dôležité**: Toto riešenie bolo aktualizované na používanie **stdio transportu** podľa odporúčaní MCP Špecifikácie 2025-06-18. Pôvodný SSE transport bol vyradený.

## Prehľad

Toto TypeScript riešenie demonštruje, ako vytvoriť MCP server pomocou aktuálneho stdio transportu. Stdio transport je jednoduchší, bezpečnejší a poskytuje lepší výkon ako zastaraný prístup SSE.

## Predpoklady

- Node.js 18+ alebo novší
- Správca balíkov npm alebo yarn

## Inštrukcie na nastavenie

### Krok 1: Nainštalujte závislosti

```bash
npm install
```

### Krok 2: Zostavte projekt

```bash
npm run build
```

## Spustenie servera

Stdio server funguje inak ako starý SSE server. Namiesto spustenia webového servera komunikuje cez stdin/stdout:

```bash
npm start
```

**Dôležité**: Server sa môže zdať, že "zamrzol" - to je normálne! Čaká na JSON-RPC správy zo stdin.

## Testovanie servera

### Metóda 1: Použitie MCP Inspector (Odporúčané)

```bash
npm run inspector
```

Toto:
1. Spustí váš server ako podproces
2. Otvorí webové rozhranie na testovanie
3. Umožní vám interaktívne testovať všetky nástroje servera

### Metóda 2: Priame testovanie cez príkazový riadok

Môžete tiež testovať spustením Inspector priamo:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Dostupné nástroje

Server poskytuje tieto nástroje:

- **add(a, b)**: Sčíta dve čísla
- **multiply(a, b)**: Vynásobí dve čísla  
- **get_greeting(name)**: Vytvorí personalizovaný pozdrav
- **get_server_info()**: Získa informácie o serveri

### Testovanie s Claude Desktop

Ak chcete použiť tento server s Claude Desktop, pridajte túto konfiguráciu do vášho `claude_desktop_config.json`:

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

## Štruktúra projektu

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Kľúčové rozdiely oproti SSE

**stdio transport (Aktuálny):**
- ✅ Jednoduchšie nastavenie - nie je potrebný HTTP server
- ✅ Lepšia bezpečnosť - žiadne HTTP endpointy
- ✅ Komunikácia založená na podprocesoch
- ✅ JSON-RPC cez stdin/stdout
- ✅ Lepší výkon

**SSE transport (Zastaraný):**
- ❌ Vyžadoval nastavenie Express servera
- ❌ Potreboval zložité smerovanie a správu relácií
- ❌ Viac závislostí (Express, HTTP spracovanie)
- ❌ Dodatočné bezpečnostné úvahy
- ❌ Teraz vyradený v MCP 2025-06-18

## Tipy na vývoj

- Používajte `console.error()` na logovanie (nikdy `console.log()`, pretože zapisuje do stdout)
- Pred testovaním zostavte projekt pomocou `npm run build`
- Testujte s Inspector pre vizuálne ladenie
- Uistite sa, že všetky JSON správy sú správne naformátované
- Server automaticky spracováva plynulé ukončenie pri SIGINT/SIGTERM

Toto riešenie nasleduje aktuálnu MCP špecifikáciu a demonštruje najlepšie postupy pre implementáciu stdio transportu pomocou TypeScript.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
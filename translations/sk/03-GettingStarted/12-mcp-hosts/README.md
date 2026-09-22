# Nastavenie populárnych MCP host klientov

> [!NOTE]
> Konfigurácie hostiteľov, ktoré smerujú na `/sse`, sú staršie príklady HTTP+SSE pre
> MCP `2025-11-25`. Pre MCP `2026-07-28` vyberte Streamable HTTP v hostiteľoch, ktorí
> to podporujú, a použite koncový bod nakonfigurovaný serverom.

Tento sprievodca pokrýva, ako nastaviť a používať MCP servery s populárnymi AI hostiteľskými aplikáciami. Každý hostiteľ má svoj vlastný spôsob konfigurácie, ale po nastavení všetci komunikujú so servermi MCP pomocou štandardizovaného protokolu.

## Čo je MCP Host?

**MCP Host** je AI aplikácia, ktorá sa môže pripojiť k MCP serverom, aby rozšírila svoje schopnosti. Predstavte si to ako "front end", s ktorým používatelia interagujú, zatiaľ čo MCP servery poskytujú "back end" nástroje a dáta.

```mermaid
flowchart LR
    User[👤 Používateľ] --> Host[🖥️ MCP Hostiteľ]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populárni hostitelia"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Predpoklady

- MCP server, ku ktorému sa chcete pripojiť (pozri [Module 3.1 - First Server](../01-first-server/README.md))
- Hostiteľská aplikácia nainštalovaná vo vašom systéme
- Základná znalosť konfiguračných súborov JSON

---

## 1. Claude Desktop

**Claude Desktop** je oficiálna desktopová aplikácia Anthropic, ktorá natívne podporuje MCP.

### Inštalácia

1. Stiahnite Claude Desktop z [claude.ai/download](https://claude.ai/download)
2. Nainštalujte a prihláste sa pomocou účtu Anthropic

### Konfigurácia

Claude Desktop používa JSON konfiguračný súbor na definovanie MCP serverov.

**Umiestnenie konfiguračného súboru:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Príklad konfigurácie:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Možnosti konfigurácie

| Pole | Popis | Príklad |
|-------|-------------|---------|
| `command` | Spustiteľný súbor, ktorý sa spustí | `"python"`, `"node"`, `"npx"` |
| `args` | Argumenty príkazového riadku | `["-m", "my_server"]` |
| `env` | Premenné prostredia | `{"API_KEY": "xxx"}` |
| `cwd` | Pracovný adresár | `"/path/to/server"` |

### Testovanie vášho nastavenia

1. Uložte konfiguračný súbor
2. Úplne reštartujte Claude Desktop (ukončite a znovu otvorte)
3. Otvorte novú konverzáciu
4. Vyhľadajte ikonu 🔌 indikujúcu pripojené servery
5. Vyskúšajte požiadať Claude, aby použil jeden z vašich nástrojov

### Riešenie problémov s Claude Desktop

**Server sa nezobrazuje:**
- Skontrolujte syntax konfiguračného súboru pomocou JSON validátora
- Uistite sa, že cesta ku príkazu je správna
- Skontrolujte logy Claude Desktop: Pomoc → Zobraziť logy

**Server havaruje pri spustení:**
- Najprv otestujte server manuálne v termináli
- Skontrolujte správne nastavenie premenných prostredia
- Uistite sa, že všetky závislosti sú nainštalované

---

## 2. VS Code s GitHub Copilot

VS Code podporuje MCP prostredníctvom rozšírení GitHub Copilot Chat.

### Predpoklady

1. Nainštalovaný VS Code verzie 1.99+
2. Nainštalované rozšírenie GitHub Copilot
3. Nainštalované rozšírenie GitHub Copilot Chat

### Konfigurácia

VS Code používa `.vscode/mcp.json` vo vašom pracovnom priestore alebo v používateľských nastaveniach.

**Konfigurácia pracovného priestoru** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Používateľské nastavenia** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Použitie MCP vo VS Code

1. Otvorte panel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Napíšte `@` pre zobrazenie dostupných MCP nástrojov
3. Použite prirodzený jazyk na vyvolanie nástrojov: "Vypočítaj 25 * 48 pomocou kalkulačky"

### Riešenie problémov vo VS Code

**MCP servery sa nerešpektujú:**
- Skontrolujte panel Výstup → "MCP" pre chybové logy
- Znovu načítajte okno: Ctrl+Shift+P → "Developer: Reload Window"
- Overte, že server beží samostatne na začiatku

---

## 3. Cursor

**Cursor** je AI-prvá editor kódu s natívnou podporou MCP.

### Inštalácia

1. Stiahnite Cursor z [cursor.sh](https://cursor.sh)
2. Nainštalujte a prihláste sa

### Konfigurácia

Cursor používa podobný formát konfigurácie ako Claude Desktop.

**Umiestnenie konfiguračného súboru:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Príklad konfigurácie:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Použitie MCP v Cursor

1. Otvorte AI chat Cursor (Ctrl+L / Cmd+L)
2. MCP nástroje sa automaticky zobrazia v návrhoch
3. Požiadajte AI o vykonávanie úloh pomocou pripojených serverov

---

## 4. Cline (terminálový)

**Cline** je terminálový MCP klient, ideálny pre prácu cez príkazový riadok.

### Inštalácia

```bash
npm install -g @anthropic/cline
```

### Konfigurácia

Cline používa premenné prostredia a argumenty príkazového riadku.

**Použitie premenných prostredia:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Použitie argumentov príkazového riadku:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfiguračný súbor** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Používanie Cline

```bash
# Spustiť interaktívnu reláciu
cline

# Jediný dotaz s MCP
cline "Calculate the square root of 144 using the calculator"

# Zoznam dostupných nástrojov
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** je ďalší editor kódu poháňaný AI s podporou MCP.

### Inštalácia

1. Stiahnite Windsurf z [codeium.com/windsurf](https://codeium.com/windsurf)
2. Nainštalujte a vytvorte si účet

### Konfigurácia

Konfigurácia Windsurf sa spravuje cez rozhranie nastavení:

1. Otvorte Nastavenia (Ctrl+, / Cmd+,)
2. Vyhľadajte "MCP"
3. Kliknite na "Edit in settings.json"

**Príklad konfigurácie:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Porovnanie typov transportov

Rôzni hostitelia podporujú rôzne mechanizmy prenosu:

| Hostiteľ | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (štandardný vstup/výstup): Najvhodnejšie pre lokálne servery spustené hostiteľom
**SSE/HTTP**: Najvhodnejšie pre vzdialené servery alebo servery zdieľané viacerými klientmi

---

## Bežné riešenie problémov

### Server sa nespustí

1. **Najprv otestujte server manuálne:**
   ```bash
   # Pre Python
   python -m your_server_module
   
   # Pre Node.js
   node /path/to/server/index.js
   ```

2. **Skontrolujte cestu ku príkazu:**
   - Používajte, ak je možné, absolútne cesty
   - Uistite sa, že spustiteľný súbor je vo vašom PATH

3. **Overte závislosti:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server sa pripojí, ale nástroje nefungujú

1. **Skontrolujte logy servera** - Väčšina hostiteľov umožňuje zapisovanie logov
2. **Overte registráciu nástrojov** - Použite MCP Inspector na testovanie
3. **Skontrolujte oprávnenia** - Niektoré nástroje potrebujú prístup k súborom alebo sieti

### Premenné prostredia sa neprenášajú

- Niektorí hostitelia sanitizujú premenné prostredia
- Výslovne používajte pole `env` v konfigurácii
- Nepoužívajte citlivé údaje v konfiguračných súboroch (používajte správu tajomstiev)

---

## Najlepšie bezpečnostné praktiky

1. **Nikdy neukladajte API kľúče** v konfiguračných súboroch
2. **Používajte premenné prostredia** pre citlivé údaje
3. **Obmedzte oprávnenia servera** len na to, čo je potrebné
4. **Preverte kód servera** pred udelením prístupu do vášho systému
5. **Používajte zoznamy povolených** pre prístup k súborovému systému a sieti

---

## Čo ďalej

- [3.13 - Ladenie s MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Vytvorte svoj prvý MCP server](../01-first-server/README.md)
- [Modul 5 - Pokročilé témy](../../05-AdvancedTopics/README.md)

---

## Ďalšie zdroje

- [Dokumentácia MCP Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Rozšírenie](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Špecifikácia MCP - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Oficiálny register MCP serverov](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
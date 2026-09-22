# Nastavení populárních klientů MCP hostitelů

> [!NOTE]
> Konfigurace hostitelů, které ukazují na `/sse`, jsou příklady staršího HTTP+SSE protokolu pro
> MCP `2025-11-25`. Pro MCP `2026-07-28` zvolte Streamable HTTP v hostitelích, kteří
> jej podporují, a použijte koncový bod nastavený serverem.

Tento průvodce popisuje, jak nakonfigurovat a používat MCP servery s oblíbenými AI hostitelskými aplikacemi. Každý hostitel má svůj vlastní přístup ke konfiguraci, ale jakmile je nastaven, všechny komunikují se servery MCP pomocí standardizovaného protokolu.

## Co je MCP Hostitel?

**MCP Hostitel** je AI aplikace, která se může připojit k MCP serverům, aby rozšířila své možnosti. Dá se chápat jako „front-end“, se kterým uživatelé komunikují, zatímco MCP servery poskytují „back-end“ nástroje a data.

```mermaid
flowchart LR
    User[👤 Uživatel] --> Host[🖥️ MCP Hostitel]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populární hostitelé"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Předpoklady

- MCP server, ke kterému se připojit (viz [Modul 3.1 - První server](../01-first-server/README.md))
- Hostitelská aplikace nainstalovaná ve vašem systému
- Základní seznámení se s JSON konfiguračními soubory

---

## 1. Claude Desktop

**Claude Desktop** je oficiální desktopová aplikace Anthropic, která nativně podporuje MCP.

### Instalace

1. Stáhněte Claude Desktop z [claude.ai/download](https://claude.ai/download)
2. Nainstalujte a přihlaste se pomocí svého účtu Anthropic

### Konfigurace

Claude Desktop používá JSON konfigurační soubor k definování MCP serverů.

**Umístění konfiguračního souboru:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Příklad konfigurace:**

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

### Konfigurační možnosti

| Pole | Popis | Příklad |
|-------|-------------|---------|
| `command` | Spustitelný soubor k provedení | `"python"`, `"node"`, `"npx"` |
| `args` | Argumenty příkazového řádku | `["-m", "my_server"]` |
| `env` | Proměnné prostředí | `{"API_KEY": "xxx"}` |
| `cwd` | Pracovní adresář | `"/path/to/server"` |

### Testování Nastavení

1. Uložte konfigurační soubor
2. Kompletně restartujte Claude Desktop (ukončete a znovu otevřete)
3. Otevřete nový rozhovor
4. Sledujte ikonu 🔌, která značí připojené servery
5. Zkuste požádat Claude o použití jednoho z vašich nástrojů

### Řešení problémů s Claude Desktop

**Server se nezobrazuje:**
- Zkontrolujte syntax konfiguračního souboru pomocí JSON validátoru
- Ujistěte se, že cesta ke spuštěnému souboru je správná
- Zkontrolujte záznamy Claude Desktop: Nápověda → Zobrazit záznamy

**Server padá při spuštění:**
- Nejprve otestujte server ručně v terminálu
- Zkontrolujte správné nastavení proměnných prostředí
- Ujistěte se, že jsou všechny závislosti nainstalované

---

## 2. VS Code s GitHub Copilot

VS Code podporuje MCP prostřednictvím rozšíření GitHub Copilot Chat.

### Předpoklady

1. Nainstalován VS Code verze 1.99+
2. Nainstalováno rozšíření GitHub Copilot
3. Nainstalováno rozšíření GitHub Copilot Chat

### Konfigurace

VS Code používá `.vscode/mcp.json` ve vašem pracovním prostoru nebo v uživatelských nastaveních.

**Konfigurace pracovního prostoru** (`.vscode/mcp.json`):

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

**Uživatelská nastavení** (`settings.json`):

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

### Použití MCP ve VS Code

1. Otevřete panel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Zadejte `@` pro zobrazení dostupných MCP nástrojů
3. Použijte přirozený jazyk pro vyvolání nástrojů: "Vypočítej 25 * 48 pomocí kalkulačky"

### Řešení problémů ve VS Code

**MCP servery se nenačítají:**
- Zkontrolujte panel Výstup → "MCP" pro chybové záznamy
- Znovu načtěte okno: Ctrl+Shift+P → "Developer: Reload Window"
- Nejprve ověřte, že server běží samostatně

---

## 3. Cursor

**Cursor** je editor kódu s prioritou AI s vestavěnou podporou MCP.

### Instalace

1. Stáhněte Cursor z [cursor.sh](https://cursor.sh)
2. Nainstalujte a přihlaste se

### Konfigurace

Cursor používá podobný formát konfigurace jako Claude Desktop.

**Umístění konfiguračního souboru:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Příklad konfigurace:**

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

### Použití MCP v Cursor

1. Otevřete AI chat Cursoru (Ctrl+L / Cmd+L)
2. MCP nástroje se automaticky objeví v návrzích
3. Požádejte AI, aby vykonala úkoly pomocí připojených serverů

---

## 4. Cline (terminálový klient)

**Cline** je MCP klient založený na terminálu, ideální pro pracovní postupy v příkazové řádce.

### Instalace

```bash
npm install -g @anthropic/cline
```

### Konfigurace

Cline používá proměnné prostředí a argumenty příkazového řádku.

**Použití proměnných prostředí:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Použití argumentů příkazového řádku:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurační soubor** (`~/.clinerc`):

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

### Použití Cline

```bash
# Spusťte interaktivní relaci
cline

# Jediný dotaz s MCP
cline "Calculate the square root of 144 using the calculator"

# Vypsat dostupné nástroje
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** je další AI poháněný editor kódu s podporou MCP.

### Instalace

1. Stáhněte Windsurf z [codeium.com/windsurf](https://codeium.com/windsurf)
2. Nainstalujte a vytvořte si účet

### Konfigurace

Konfigurace Windsurfu se řídí přes uživatelské rozhraní nastavení:

1. Otevřete Nastavení (Ctrl+, / Cmd+,)
2. Vyhledejte „MCP“
3. Klikněte na „Upravit v settings.json“

**Příklad konfigurace:**

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

## Porovnání typů transportu

Různí hostitelé podporují různé přenosové mechanismy:

| Hostitel | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standardní vstup/výstup): Nejvhodnější pro lokální servery spuštěné hostitelem
**SSE/HTTP**: Nejvhodnější pro vzdálené servery nebo servery sdílené mezi více klienty

---

## Běžné řešení problémů

### Server se nespustí

1. **Nejprve otestujte server ručně:**
   ```bash
   # Pro Python
   python -m your_server_module
   
   # Pro Node.js
   node /path/to/server/index.js
   ```

2. **Zkontrolujte cestu ke spuštěnému souboru:**
   - Používejte absolutní cesty, kdykoliv je to možné
   - Ujistěte se, že je spustitelný soubor v PATH

3. **Ověřte závislosti:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server se připojí, ale nástroje nefungují

1. **Zkontrolujte záznamy serveru** - Většina hostitelů má možnosti logování
2. **Ověřte registraci nástrojů** - Použijte MCP Inspector k testování
3. **Zkontrolujte oprávnění** - Některé nástroje potřebují přístup k souborům/síti

### Proměnné prostředí nejsou předány

- Některé hostitele sanitizují proměnné prostředí
- Explicitně použijte pole `env` v konfiguraci
- Vyhněte se citlivým datům v konfiguračních souborech (použijte správu tajemství)

---

## Bezpečnostní osvědčené postupy

1. **Nikdy necommitujte API klíče** do konfiguračních souborů
2. **Používejte proměnné prostředí** pro citlivá data
3. **Omezte oprávnění serveru** pouze na nezbytné
4. **Prověřte kód serveru** před poskytnutím přístupu k vašemu systému
5. **Používejte allowlisty** pro přístup k souborovému systému a síti

---

## Co dál

- [3.13 - Ladění s MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Vytvořte svůj první MCP server](../01-first-server/README.md)
- [Modul 5 - Pokročilé témata](../../05-AdvancedTopics/README.md)

---

## Další zdroje

- [Dokumentace Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP rozšíření](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Specifikace MCP - Transporty](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Oficiální registr MCP serverů](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
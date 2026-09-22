# Konfigurera Populära MCP Host-klienter

> [!NOTE]
> Konfigurationer för host som pekar på `/sse` är äldre HTTP+SSE-exempel för
> MCP `2025-11-25`. För MCP `2026-07-28`, välj Streamable HTTP i hosts som
> stödjer det och använd den endpoint som konfigurerats av servern.

Denna guide täcker hur man konfigurerar och använder MCP-servrar med populära AI host-applikationer. Varje host har sitt eget konfigurationssätt, men när de väl är inställda kommunicerar alla med MCP-servrar via det standardiserade protokollet.

## Vad är en MCP Host?

En **MCP Host** är en AI-applikation som kan ansluta till MCP-servrar för att utöka sina möjligheter. Tänk på det som en "front end" som användare interagerar med, medan MCP-servrar tillhandahåller "back end" verktyg och data.

```mermaid
flowchart LR
    User[👤 Användare] --> Host[🖥️ MCP Värd]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populära Värdar"
        H1[Claude Skrivbord]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Förutsättningar

- En MCP-server att ansluta till (se [Modul 3.1 - Första Servern](../01-first-server/README.md))
- Host-applikationen installerad på ditt system
- Grundläggande kännedom om JSON-konfigurationsfiler

---

## 1. Claude Desktop

**Claude Desktop** är Anthropics officiella desktopapplikation som inbyggt stöder MCP.

### Installation

1. Ladda ner Claude Desktop från [claude.ai/download](https://claude.ai/download)
2. Installera och logga in med ditt Anthropic-konto

### Konfiguration

Claude Desktop använder en JSON-konfigurationsfil för att definiera MCP-servrar.

**Plats för konfigurationsfil:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Exempel på konfiguration:**

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

### Konfigurationsalternativ

| Fält | Beskrivning | Exempel |
|-------|-------------|---------|
| `command` | Körbar fil att köra | `"python"`, `"node"`, `"npx"` |
| `args` | Kommandoradsargument | `["-m", "my_server"]` |
| `env` | Miljövariabler | `{"API_KEY": "xxx"}` |
| `cwd` | Arbetskatalog | `"/path/to/server"` |

### Testa din installation

1. Spara konfigurationsfilen
2. Starta om Claude Desktop helt (avsluta och öppna igen)
3. Öppna en ny konversation
4. Leta efter ikonen 🔌 som visar anslutna servrar
5. Prova att be Claude använda ett av dina verktyg

### Felsökning av Claude Desktop

**Server dyker inte upp:**
- Kontrollera syntaxen i konfigurationsfilen med en JSON-validator
- Säkerställ att kommandovägen är korrekt
- Kontrollera Claude Desktop-loggar: Hjälp → Visa Loggar

**Server kraschar vid start:**
- Testa din server manuellt i terminalen först
- Kontrollera att miljövariabler är korrekt inställda
- Säkerställ att alla beroenden är installerade

---

## 2. VS Code med GitHub Copilot

VS Code stöder MCP via GitHub Copilot Chat-tillägg.

### Förutsättningar

1. VS Code 1.99+ installerad
2. GitHub Copilot-tillägget installerat
3. GitHub Copilot Chat-tillägget installerat

### Konfiguration

VS Code använder `.vscode/mcp.json` i ditt arbetsyta- eller användarinställningar.

**Arbetsyte-konfiguration** (`.vscode/mcp.json`):

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

**Användarinställningar** (`settings.json`):

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

### Använda MCP i VS Code

1. Öppna Copilot Chat-panelen (Ctrl+Shift+I / Cmd+Shift+I)
2. Skriv `@` för att se tillgängliga MCP-verktyg
3. Använd naturligt språk för att anropa verktyg: "Beräkna 25 * 48 med kalkylatorn"

### Felsökning av VS Code

**MCP-servrar laddas inte:**
- Kontrollera Output-panelen → "MCP" för felmeddelanden
- Ladda om fönstret: Ctrl+Shift+P → "Utvecklare: Ladda om fönster"
- Verifiera att servern körs fristående först

---

## 3. Cursor

**Cursor** är en AI-fokuserad kodredigerare med inbyggt MCP-stöd.

### Installation

1. Ladda ner Cursor från [cursor.sh](https://cursor.sh)
2. Installera och logga in

### Konfiguration

Cursor använder ett liknande konfigurationsformat som Claude Desktop.

**Plats för konfigurationsfil:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Exempel på konfiguration:**

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

### Använda MCP i Cursor

1. Öppna Cursors AI-chatt (Ctrl+L / Cmd+L)
2. MCP-verktyg visas automatiskt i förslagen
3. Be AI:n utföra uppgifter med anslutna servrar

---

## 4. Cline (Terminalbaserad)

**Cline** är en terminalbaserad MCP-klient, idealisk för kommandoradsarbetsflöden.

### Installation

```bash
npm install -g @anthropic/cline
```

### Konfiguration

Cline använder miljövariabler och kommandoradsargument.

**Använda miljövariabler:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Använda kommandoradsargument:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfigurationsfil** (`~/.clinerc`):

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

### Använda Cline

```bash
# Starta en interaktiv session
cline

# Enskild förfrågan med MCP
cline "Calculate the square root of 144 using the calculator"

# Lista tillgängliga verktyg
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** är en annan AI-driven kodredigerare med MCP-stöd.

### Installation

1. Ladda ner Windsurf från [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installera och skapa ett konto

### Konfiguration

Windsurf-konfiguration hanteras via inställningsgränssnittet:

1. Öppna Inställningar (Ctrl+, / Cmd+,)
2. Sök efter "MCP"
3. Klicka på "Redigera i settings.json"

**Exempel på konfiguration:**

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

## Jämförelse av Transporttyper

Olika hosts stöder olika transportmekanismer:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Bäst för lokala servrar som startas av hosten
**SSE/HTTP**: Bäst för fjärrservrar eller servrar delade mellan flera klienter

---

## Vanliga Felsökningssteg

### Servern startar inte

1. **Testa servern manuellt först:**
   ```bash
   # För Python
   python -m your_server_module
   
   # För Node.js
   node /path/to/server/index.js
   ```

2. **Kontrollera kommandovägen:**
   - Använd absoluta sökvägar när möjligt
   - Säkerställ att programmet finns i din PATH

3. **Verifiera beroenden:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Servern ansluter men verktyg fungerar inte

1. **Kontrollera serverloggar** - De flesta hosts har loggalternativ
2. **Verifiera verktygsregistrering** - Använd MCP Inspector för testning
3. **Kontrollera behörigheter** - Vissa verktyg behöver fil-/nätverksåtkomst

### Miljövariabler vidarebefordras inte

- Vissa hosts sanerar miljövariabler
- Använd `env`-konfigurationsfältet uttryckligen
- Undvik känsliga data i konfigurationsfiler (använd hemlighetshantering)

---

## Säkerhetsbästa Praxis

1. **Lägg aldrig upp API-nycklar** i konfigurationsfiler
2. **Använd miljövariabler** för känsliga uppgifter
3. **Begränsa serverbehörigheter** till endast det som behövs
4. **Granska serverkoden** innan du ger systemåtkomst
5. **Använd tillåtelselistor** för filsystem- och nätverksåtkomst

---

## Vad händer härnäst

- [3.13 - Felsökning med MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Skapa din första MCP-server](../01-first-server/README.md)
- [Modul 5 - Avancerade Ämnen](../../05-AdvancedTopics/README.md)

---

## Ytterligare Resurser

- [Claude Desktop MCP Dokumentation](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Tillägg](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specifikation - Transporter](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Officiell MCP Serverregister](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
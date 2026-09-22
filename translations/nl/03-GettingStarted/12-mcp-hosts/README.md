# Populaire MCP Host Clients Instellen

> [!NOTE]
> Hostconfiguraties die verwijzen naar `/sse` zijn legacy HTTP+SSE-voorbeelden voor
> MCP `2025-11-25`. Voor MCP `2026-07-28` selecteer Streamable HTTP in hosts die
> dit ondersteunen en gebruik de door de server geconfigureerde endpoint.

Deze gids behandelt hoe je MCP-servers configureert en gebruikt met populaire AI-host applicaties. Elke host heeft zijn eigen configuratiebenadering, maar eenmaal ingesteld communiceren ze allemaal met MCP-servers via het gestandaardiseerde protocol.

## Wat is een MCP Host?

Een **MCP Host** is een AI-toepassing die verbinding kan maken met MCP-servers om zijn mogelijkheden uit te breiden. Zie het als de "frontend" waarmee gebruikers omgaan, terwijl MCP-servers de "backend" gereedschappen en data leveren.

```mermaid
flowchart LR
    User[👤 Gebruiker] --> Host[🖥️ MCP Host]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populaire Hosts"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Vereisten

- Een MCP-server om verbinding mee te maken (zie [Module 3.1 - Eerste Server](../01-first-server/README.md))
- De hostapplicatie geïnstalleerd op jouw systeem
- Basiskennis van JSON-configuratiebestanden

---

## 1. Claude Desktop

**Claude Desktop** is de officiële desktopapplicatie van Anthropic die native MCP ondersteunt.

### Installatie

1. Download Claude Desktop van [claude.ai/download](https://claude.ai/download)
2. Installeer en meld je aan met je Anthropic-account

### Configuratie

Claude Desktop gebruikt een JSON-configuratiebestand om MCP-servers te definiëren.

**Locatie configuratiebestand:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Voorbeeldconfiguratie:**

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

### Configuratieopties

| Veld | Beschrijving | Voorbeeld |
|-------|-------------|---------|
| `command` | De uit te voeren executable | `"python"`, `"node"`, `"npx"` |
| `args` | Commandoregelargumenten | `["-m", "my_server"]` |
| `env` | Omgevingsvariabelen | `{"API_KEY": "xxx"}` |
| `cwd` | Werkmap | `"/path/to/server"` |

### Testen van je opzet

1. Sla het configuratiebestand op
2. Herstart Claude Desktop volledig (afsluiten en opnieuw openen)
3. Open een nieuw gesprek
4. Zoek naar het 🔌-icoontje dat verbonden servers aangeeft
5. Probeer Claude te vragen een van je tools te gebruiken

### Problemen oplossen met Claude Desktop

**Server verschijnt niet:**
- Controleer de syntaxis van het configuratiebestand met een JSON-validator
- Zorg dat het pad naar het commando correct is
- Controleer Claude Desktop logs: Help → Logs tonen

**Server crasht bij opstarten:**
- Test je server eerst handmatig in de terminal
- Controleer of omgevingsvariabelen juist zijn ingesteld
- Zorg dat alle afhankelijkheden zijn geïnstalleerd

---

## 2. VS Code met GitHub Copilot

VS Code ondersteunt MCP via de GitHub Copilot Chat-extensies.

### Vereisten

1. VS Code 1.99+ geïnstalleerd
2. GitHub Copilot-extensie geïnstalleerd
3. GitHub Copilot Chat-extensie geïnstalleerd

### Configuratie

VS Code gebruikt `.vscode/mcp.json` in je werkruimte of gebruikersinstellingen.

**Werkruimte configuratie** (`.vscode/mcp.json`):

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

**Gebruikersinstellingen** (`settings.json`):

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

### MCP gebruiken in VS Code

1. Open het Copilot Chat-paneel (Ctrl+Shift+I / Cmd+Shift+I)
2. Typ `@` om beschikbare MCP-tools te zien
3. Gebruik natuurlijke taal om tools op te roepen: "Bereken 25 * 48 met de rekenmachine"

### Problemen oplossen met VS Code

**MCP servers laden niet:**
- Controleer het Output-paneel → "MCP" op foutlogs
- Herlaad het venster: Ctrl+Shift+P → "Developer: Reload Window"
- Verifieer dat de server zelfstandig draait

---

## 3. Cursor

**Cursor** is een AI-gerichte code-editor met ingebouwde MCP-ondersteuning.

### Installatie

1. Download Cursor van [cursor.sh](https://cursor.sh)
2. Installeer en meld je aan

### Configuratie

Cursor gebruikt een vergelijkbaar configuratieformaat als Claude Desktop.

**Locatie configuratiebestand:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Voorbeeldconfiguratie:**

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

### MCP gebruiken in Cursor

1. Open Cursor's AI-chat (Ctrl+L / Cmd+L)
2. MCP-tools verschijnen automatisch in suggesties
3. Vraag de AI om taken uit te voeren met verbonden servers

---

## 4. Cline (Terminal-gebaseerd)

**Cline** is een terminal-gebaseerde MCP-client, ideaal voor commandoregelwerkstromen.

### Installatie

```bash
npm install -g @anthropic/cline
```

### Configuratie

Cline gebruikt omgevingsvariabelen en commandoregelargumenten.

**Gebruik van omgevingsvariabelen:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Gebruik van commandoregelargumenten:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Configuratiebestand** (`~/.clinerc`):

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

### Cline gebruiken

```bash
# Start een interactieve sessie
cline

# Enkele query met MCP
cline "Calculate the square root of 144 using the calculator"

# Beschikbare tools weergeven
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** is nog een AI-gebaseerde code-editor met MCP-ondersteuning.

### Installatie

1. Download Windsurf van [codeium.com/windsurf](https://codeium.com/windsurf)
2. Installeer en maak een account aan

### Configuratie

Windsurf-configuratie wordt beheerd via de instellingen-UI:

1. Open Instellingen (Ctrl+, / Cmd+,)
2. Zoek naar "MCP"
3. Klik op "Bewerken in settings.json"

**Voorbeeldconfiguratie:**

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

## Vergelijking van Transporttypen

Verschillende hosts ondersteunen verschillende transportmechanismen:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standaardinvoer/-uitvoer): Het beste voor lokale servers gestart door de host
**SSE/HTTP**: Het beste voor externe servers of servers gedeeld tussen meerdere clients

---

## Veelvoorkomende Problemen Oplossen

### Server start niet op

1. **Test de server eerst handmatig:**
   ```bash
   # Voor Python
   python -m your_server_module
   
   # Voor Node.js
   node /path/to/server/index.js
   ```

2. **Controleer het pad van het commando:**
   - Gebruik indien mogelijk absolute paden
   - Zorg dat de executable in je PATH staat

3. **Verifieer afhankelijkheden:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server maakt verbinding maar tools werken niet

1. **Controleer serverlogs** - De meeste hosts hebben loggingopties
2. **Verifieer tool-registratie** - Gebruik MCP Inspector om te testen
3. **Controleer permissies** - Sommige tools hebben bestand-/netwerktoegang nodig

### Omgevingsvariabelen worden niet doorgegeven

- Sommige hosts filteren omgevingsvariabelen
- Gebruik expliciet het `env` configuratieveld
- Vermijd gevoelige data in configuratiebestanden (gebruik geheimebeheer)

---

## Beveiligingsrichtlijnen

1. **Commit NOOIT API-sleutels** naar configuratiebestanden
2. **Gebruik omgevingsvariabelen** voor gevoelige data
3. **Beperk serverpermissies** tot alleen wat nodig is
4. **Bekijk servercode** voordat je toegang geeft tot je systeem
5. **Gebruik allowlists** voor bestandssysteem- en netwerktoegang

---

## Wat Nu?

- [3.13 - Debuggen met MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Maak je eerste MCP-server](../01-first-server/README.md)
- [Module 5 - Gevorderde Onderwerpen](../../05-AdvancedTopics/README.md)

---

## Meer Bronnen

- [Claude Desktop MCP Documentatie](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Extensie](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specificatie - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Officiële MCP Servers Registratie](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
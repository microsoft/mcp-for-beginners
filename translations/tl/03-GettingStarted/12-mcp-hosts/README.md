# Pag-set Up ng Mga Sikat na MCP Host Clients

> [!NOTE]
> Ang mga configuration ng host na tumutukoy sa `/sse` ay mga legacy HTTP+SSE na halimbawa para sa
> MCP `2025-11-25`. Para sa MCP `2026-07-28`, piliin ang Streamable HTTP sa mga host na
> sumusuporta rito at gamitin ang endpoint na naka-configure ng server.

Saklaw ng gabay na ito kung paano i-configure at gamitin ang mga MCP server gamit ang mga sikat na AI host application. Bawat host ay may kanya-kanyang paraan ng pag-configure, ngunit kapag na-set up na, lahat sila ay nakikipag-ugnayan sa mga MCP server gamit ang standardisadong protocol.

## Ano ang MCP Host?

Ang **MCP Host** ay isang AI application na maaaring kumonekta sa mga MCP server upang mapalawak ang mga kakayahan nito. Isipin ito bilang "front end" na ginagamit ng mga user, habang ang mga MCP server ang nagbibigay ng "back end" na mga tools at data.

```mermaid
flowchart LR
    User[👤 Gumagamit] --> Host[🖥️ Host ng MCP]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Sikat na Mga Host"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Mga Kinakailangan

- Isang MCP server na pagkukunan ng koneksyon (tingnan ang [Module 3.1 - First Server](../01-first-server/README.md))
- Ang host application na naka-install sa iyong system
- Pangunahing kaalaman sa mga JSON configuration file

---

## 1. Claude Desktop

Ang **Claude Desktop** ay ang opisyal na desktop application ng Anthropic na may native support para sa MCP.

### Pag-install

1. I-download ang Claude Desktop mula sa [claude.ai/download](https://claude.ai/download)
2. I-install at mag-sign in gamit ang iyong Anthropic account

### Pag-configure

Ang Claude Desktop ay gumagamit ng JSON configuration file para tukuyin ang mga MCP server.

**Lokasyon ng configuration file:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Halimbawa ng configuration:**

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

### Mga Opsyon sa Configuration

| Field | Paglalarawan | Halimbawa |
|-------|-------------|---------|
| `command` | Ang executable na patatakbuhin | `"python"`, `"node"`, `"npx"` |
| `args` | Mga argumento sa command line | `["-m", "my_server"]` |
| `env` | Mga environment variable | `{"API_KEY": "xxx"}` |
| `cwd` | Working directory | `"/path/to/server"` |

### Pagsubok sa Iyong Setup

1. I-save ang configuration file
2. Ganap na i-restart ang Claude Desktop (isara at buksan muli)
3. Magbukas ng bagong pag-uusap
4. Hanapin ang icon na 🔌 na nagpapahiwatig na nakakonekta ang mga server
5. Subukang utusan si Claude na gumamit ng isa sa iyong mga tool

### Pag-troubleshoot ng Claude Desktop

**Hindi lumalabas ang server:**
- Suriin ang syntax ng configuration file gamit ang JSON validator
- Tiyaking tama ang command path
- Suriin ang mga logs ng Claude Desktop: Help → Show Logs

**Nag-crash ang server sa startup:**
- Subukang patakbuhin manu-mano ang server sa terminal muna
- Siguraduhing tama ang setting ng mga environment variable
- Tiyaking na-install ang lahat ng pangangailangang dependencies

---

## 2. VS Code gamit ang GitHub Copilot

Sinusuportahan ng VS Code ang MCP sa pamamagitan ng mga GitHub Copilot Chat extension.

### Mga Kinakailangan

1. Nakainstall ang VS Code 1.99+
2. Nakainstall ang GitHub Copilot extension
3. Nakainstall ang GitHub Copilot Chat extension

### Pag-configure

Ginagamit ng VS Code ang `.vscode/mcp.json` sa iyong workspace o user settings.

**Workspace configuration** (`.vscode/mcp.json`):

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

**User settings** (`settings.json`):

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

### Paggamit ng MCP sa VS Code

1. Buksan ang Copilot Chat panel (Ctrl+Shift+I / Cmd+Shift+I)
2. I-type ang `@` para makita ang mga available na MCP tool
3. Gamitin ang natural na wika para tawagin ang mga tool: "Calculate 25 * 48 using the calculator"

### Pag-troubleshoot ng VS Code

**Hindi naglo-load ang mga MCP server:**
- Suriin ang Output panel → "MCP" para sa mga log ng error
- I-reload ang window: Ctrl+Shift+P → "Developer: Reload Window"
- Siguraduhing tumatakbo muna nang standalone ang server

---

## 3. Cursor

Ang **Cursor** ay isang AI-first na code editor na may built-in na suporta para sa MCP.

### Pag-install

1. I-download ang Cursor mula sa [cursor.sh](https://cursor.sh)
2. I-install at mag-sign in

### Pag-configure

Gumagamit ang Cursor ng katulad na format ng configuration gaya ng Claude Desktop.

**Lokasyon ng configuration file:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Halimbawa ng configuration:**

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

### Paggamit ng MCP sa Cursor

1. Buksan ang AI chat ng Cursor (Ctrl+L / Cmd+L)
2. Awtomatikong lalabas ang mga MCP tool sa mga suhestiyon
3. Utusan ang AI na magsagawa ng mga gawain gamit ang nakakonektang mga server

---

## 4. Cline (Batay sa Terminal)

Ang **Cline** ay terminal-based na MCP client, na mainam para sa mga command-line na workflows.

### Pag-install

```bash
npm install -g @anthropic/cline
```

### Pag-configure

Gumagamit ang Cline ng environment variables at command-line arguments.

**Paggamit ng environment variables:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Paggamit ng command-line arguments:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Configuration file** (`~/.clinerc`):

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

### Paggamit ng Cline

```bash
# Simulan ang isang interaktibong sesyon
cline

# Isang tanong gamit ang MCP
cline "Calculate the square root of 144 using the calculator"

# Ilan sa mga magagamit na kasangkapan
cline --list-tools
```

---

## 5. Windsurf

Ang **Windsurf** ay isa pang AI-powered code editor na may suporta para sa MCP.

### Pag-install

1. I-download ang Windsurf mula sa [codeium.com/windsurf](https://codeium.com/windsurf)
2. I-install at gumawa ng account

### Pag-configure

Pinangangasiwaan ang configuration ng Windsurf sa pamamagitan ng settings UI:

1. Buksan ang Settings (Ctrl+, / Cmd+,)
2. Hanapin ang "MCP"
3. I-click ang "Edit in settings.json"

**Halimbawa ng configuration:**

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

## Paghahambing ng Mga Uri ng Transport

Iba't ibang host ay sumusuporta sa iba't ibang mekanismo ng transport:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Pinakamainam para sa mga lokal na server na sinimulan ng host
**SSE/HTTP**: Pinakamainam para sa mga remote server o mga server na ibinabahagi sa maraming client

---

## Karaniwang Pag-troubleshoot

### Hindi nagsisimula ang server

1. **Subukan muna manu-mano ang server:**
   ```bash
   # Para sa Python
   python -m your_server_module
   
   # Para sa Node.js
   node /path/to/server/index.js
   ```

2. **Suriin ang command path:**
   - Gumamit ng absolute paths kung maaari
   - Siguraduhing nasa PATH ang executable

3. **Siguraduhin ang mga dependencies:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Kumokonekta ang server pero hindi gumagana ang mga tool

1. **Suriin ang mga log ng server** - Karamihan sa mga host ay may opsyon para sa logging
2. **Siguraduhin ang rehistrasyon ng tool** - Gamitin ang MCP Inspector para subukan
3. **Suriin ang mga permiso** - May ilang tool na nangangailangan ng access sa file/network

### Hindi naipapasa ang environment variables

- May ilang host na nagsasala ng environment variables
- Gamitin nang tahasan ang field na `env` sa configuration
- Iwasan ang paggamit ng sensitibong data sa config files (gumamit ng secrets management)

---

## Mga Pinakamahusay na Kasanayan sa Seguridad

1. **Huwag kailanman i-commit ang mga API key** sa configuration files
2. **Gamitin ang environment variables** para sa sensitibong data
3. **Limitahan ang mga permiso ng server** sa mga kinakailangan lamang
4. **Suriin ang code ng server** bago bigyan ng access sa iyong system
5. **Gumamit ng allowlists** para sa access sa file system at network

---

## Ano ang Susunod

- [3.13 - Debugging gamit ang MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Gumawa ng iyong unang MCP server](../01-first-server/README.md)
- [Module 5 - Mga Advanced na Paksa](../../05-AdvancedTopics/README.md)

---

## Karagdagang Mga Mapagkukunan

- [Dokumentasyon ng Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specification - Mga Transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Opisyal na Registry ng MCP Servers](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
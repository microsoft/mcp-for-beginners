# Populaarsete MCP hosti klientide seadistamine

> [!NOTE]
> Hostide konfiguratsioonid, mis suunavad `/sse`-le, on MCP `2025-11-25` jaoks vananenud HTTP+SSE näited. MCP `2026-07-28` puhul vali hostides, mis seda toetavad, Streamable HTTP ja kasuta serveri poolt konfigureeritud lõpp-punkti.
> 
> 

See juhend käsitleb, kuidas seadistada ja kasutada MCP servereid populaarsete AI hostirakendustega. Iga hostil on oma konfiguratsiooniviis, kuid pärast seadistamist suhtlevad nad kõik MCP serveritega standardiseeritud protokolli abil.

## Mis on MCP Host?

**MCP Host** on AI-rakendus, mis suudab ühendada MCP serveritega, et laiendada oma võimekust. Mõtle sellele kui "esiküljele", millega kasutajad suhtlevad, samal ajal kui MCP serverid pakuvad "tagapõhja" tööriistu ja andmeid.

```mermaid
flowchart LR
    User[👤 Kasutaja] --> Host[🖥️ MCP Host]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Populaarsed hostid"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Eeltingimused

- MCP server, millega ühendada (vt [Moodul 3.1 - Esimene server](../01-first-server/README.md))
- Hostirakendus installitud sinu süsteemis
- Baasteadmised JSON konfiguratsioonifailidest

---

## 1. Claude Desktop

**Claude Desktop** on Anthropicu ametlik lauaarvuti rakendus, mis toetab MCP-d loomupäraselt.

### Paigaldus

1. Laadi alla Claude Desktop aadressilt [claude.ai/download](https://claude.ai/download)
2. Paigalda ja logi sisse oma Anthropicu kontoga

### Konfiguratsioon

Claude Desktop kasutab MCP serverite määratlemiseks JSON konfiguratsioonifaili.

**Konfiguratsioonifaili asukoht:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Näidis konfiguratsioon:**

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

### Konfiguratsiooni valikud

| Väli | Kirjeldus | Näide |
|-------|-------------|---------|
| `command` | Käivitatav programm | `"python"`, `"node"`, `"npx"` |
| `args` | Käsklusrida argumendid | `["-m", "my_server"]` |
| `env` | Keskkonnamuutujad | `{"API_KEY": "xxx"}` |
| `cwd` | Töötamiskataloog | `"/path/to/server"` |

### Seadistuse testimine

1. Salvesta konfiguratsioonifail
2. Taaskäivita Claude Desktop täielikult (välju ja ava uuesti)
3. Ava uus vestlus
4. Otsi ikooni 🔌, mis näitab ühendatud servereid
5. Proovi paluda Claude'il kasutada mõnda su tööriista

### Claude Desktopi tõrkeotsing

**Server ei ilmu:**
- Kontrolli konfiguratsioonifaili sünaksit JSON valideerijaga
- Veendu, et käskluse tee on õige
- Kontrolli Claude Desktopi logisid: Abi → Näita logisid

**Server jookseb käivitamisel kokku:**
- Proovi serverit esmalt terminalis käsitsi käivitada
- Kontrolli, et keskkonnamuutujad on õigesti määratud
- Veendu, et kõik sõltuvused on paigaldatud

---

## 2. VS Code GitHub Copilotiga

VS Code toetab MCP-d GitHub Copilot Chat laienduste kaudu.

### Eeltingimused

1. Paigaldatud VS Code versioon 1.99+
2. Paigaldatud GitHub Copilot laiendus
3. Paigaldatud GitHub Copilot Chat laiendus

### Konfiguratsioon

VS Code kasutab tööruumi või kasutaja seadetes faili `.vscode/mcp.json`.

**Tööruumi konfiguratsioon** (`.vscode/mcp.json`):

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

**Kasutaja sätted** (`settings.json`):

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

### MCP kasutamine VS Code'is

1. Ava Copilot Chati paneel (Ctrl+Shift+I / Cmd+Shift+I)
2. Kirjuta `@`, et näha saadaolevaid MCP tööriistu
3. Kasuta loomulikku keelt tööriistade kutsumiseks: "Arvuta kalkulaatoriga 25 * 48"

### VS Code tõrkeotsing

**MCP serverid ei laadi:**
- Kontrolli väljundi paneelis → "MCP" vealogisid
- Laadi aken uuesti: Ctrl+Shift+P → "Arendaja: Laadi aken uuesti"
- Veendu, et server töötab esmalt iseseisvalt

---

## 3. Cursor

**Cursor** on AI-keskne koodiredaktor, millel on sisseehitatud MCP tugi.

### Paigaldus

1. Laadi alla Cursor aadressilt [cursor.sh](https://cursor.sh)
2. Paigalda ja logi sisse

### Konfiguratsioon

Cursor kasutab sarnast konfiguratsiooniformaati nagu Claude Desktop.

**Konfiguratsioonifaili asukoht:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Näidis konfiguratsioon:**

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

### MCP kasutamine Cursoris

1. Ava Cursor AI vestlus (Ctrl+L / Cmd+L)
2. MCP tööriistad ilmuvad automaatselt soovitustes
3. Palu AI-l toiminguid sooritada ühendatud serverite abil

---

## 4. Cline (terminalipõhine)

**Cline** on terminalipõhine MCP klient, sobilik käsurea töövoogude jaoks.

### Paigaldus

```bash
npm install -g @anthropic/cline
```

### Konfiguratsioon

Cline kasutab keskkonnamuutujaid ja käsurea argumente.

**Keskkonnamuutujate kasutamine:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Käsurea argumentide kasutamine:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Konfiguratsioonifail** (`~/.clinerc`):

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

### Cline kasutamine

```bash
# Alusta interaktiivset sessiooni
cline

# Üksik päring MCP-ga
cline "Calculate the square root of 144 using the calculator"

# Loetle kasutatavad tööriistad
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** on veel üks MCP toetusega AI-kodeerimisredaktor.

### Paigaldus

1. Laadi alla Windsurf aadressilt [codeium.com/windsurf](https://codeium.com/windsurf)
2. Paigalda ja loo konto

### Konfiguratsioon

Windsurf’i konfiguratsiooni haldatakse sätete liidese kaudu:

1. Ava Seaded (Ctrl+, / Cmd+,)
2. Otsi "MCP"
3. Klõpsa "Muuda settings.json'is"

**Näidis konfiguratsioon:**

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

## Transporttüüpide võrdlus

Erinevad hostid toetavad erinevaid transpordimehhanisme:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard sisend/väljund): Parim kohalikeks serveriteks, mis käivituvad hosti poolt
**SSE/HTTP**: Parim kaugarvutis asuvate serverite või mitme kliendi vahel jagatud serverite jaoks

---

## Levinud tõrkeotsingu juhised

### Server ei käivitu

1. **Testi serverit esmalt käsitsi:**
   ```bash
   # Pythoniks
   python -m your_server_module
   
   # Node.js jaoks
   node /path/to/server/index.js
   ```

2. **Kontrolli käsku:**
   - Kasuta võimalusel absoluutseid teid
   - Veendu, et käivitatav fail on PATH-s

3. **Kontrolli sõltuvusi:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server on ühendatud, kuid tööriistad ei toimi

1. **Kontrolli serveri logisid** - Enamikel hostidel on logimisvõimalused
2. **Kontrolli tööriistade registreerimist** - Kasuta MCP Inspectorit testimiseks
3. **Kontrolli õigusi** - Mõned tööriistad vajavad faili-/võrgu ligipääsu

### Keskkonnamuutujad ei lähe läbi

- Mõned hostid puhastavad keskkonnamuutujaid
- Kasuta `env` konfiguratsioonivälja selgelt
- Väldi tundliku info panemist konfiguratsioonifailidesse (kasuta salajate haldust)

---

## Turvalisuse parimad tavad

1. **Ära kunagi kirjuta API võtmeid konfiguratsioonifailidesse**
2. **Kasuta tundlike andmete jaoks keskkonnamuutujaid**
3. **Piira serveri õigusi ainult vajalikuni**
4. **Loe serveri koodi enne süsteemi ligipääsu andmist läbi**
5. **Kasuta lubade nimekirju failisüsteemi ja võrgu ligipääsuks**

---

## Mis järgmiseks

- [3.13 - Pahade asjade otsimine MCP Inspectoriga](../13-mcp-inspector/README.md)
- [3.1 - Loo oma esimene MCP server](../01-first-server/README.md)
- [Moodul 5 - Täiustatud teemad](../../05-AdvancedTopics/README.md)

---

## Lisamaterjalid

- [Claude Desktop MCP dokumentatsioon](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP laiendus](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP spetsifikatsioon - Transpordid](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Ametlik MCP serverite registratuur](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
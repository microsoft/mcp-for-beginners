# Kuweka Watumiaji Wenyeji Maarufu wa MCP

> [!NOTE]
> Mipangilio ya mwenyeji inayolenga `/sse` ni mifano ya zamani ya HTTP+SSE kwa
> MCP `2025-11-25`. Kwa MCP `2026-07-28`, chagua Streamable HTTP kwenye wenyeji ambao
> wanaunga mkono na tumia mwisho wa huduma uliowekwa na seva.

Mwongozo huu unahusu jinsi ya kusanidi na kutumia seva za MCP na programu maarufu za mwenyeji wa AI. Kila mwenyeji ana njia yake ya usanidi, lakini baada ya kusanidiwa, wote huwasiliana na seva za MCP kwa kutumia itifaki iliyosanifishwa.

## Nini MCP Mwenza?

**MCP Mwenza** ni programu ya AI inayoweza kuungana na seva za MCP ili kuongeza uwezo wake. Fikiria kama ni "sehemu ya mbele" ambayo watumiaji huingiliana nayo, wakati seva za MCP zinatoa "sehemu ya nyuma" ya zana na data.

```mermaid
flowchart LR
    User[👤 Mtumiaji] --> Host[🖥️ Mwanzilishi MCP]
    Host --> S1[Seva MCP A]
    Host --> S2[Seva MCP B]
    Host --> S3[Seva MCP C]
    
    subgraph "Waenyeji Maarufu"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Masharti ya Awali

- Seva ya MCP ya kuungana nayo (angalia [Seva ya Kwanza 3.1](../01-first-server/README.md))
- Programu ya mwenyeji imewekwa kwenye mfumo wako
- Uzoefu wa msingi na faili za usanidi za JSON

---

## 1. Claude Desktop

**Claude Desktop** ni programu rasmi ya Anthropic ya desktop inayounga mkono MCP asili.

### Usanidi

1. Pakua Claude Desktop kutoka [claude.ai/download](https://claude.ai/download)
2. Sakinisha na ingia na akaunti yako ya Anthropic

### Usanidi

Claude Desktop hutumia faili la usanidi la JSON kufafanua seva za MCP.

**Mahali pa faili la usanidi:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Mfano wa usanidi:**

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

### Chaguzi za Usanidi

| Sehemu | Maelezo | Mfano |
|-------|-------------|---------|
| `command` | Inatekelezwa kukimbia | `"python"`, `"node"`, `"npx"` |
| `args` | Hoja za mstari wa amri | `["-m", "my_server"]` |
| `env` | Mabadiliko ya mazingira | `{"API_KEY": "xxx"}` |
| `cwd` | Saraka ya kazi | `"/path/to/server"` |

### Kupima Usanidi Wako

1. Hifadhi faili la usanidi
2. Anzisha tena Claude Desktop kabisa (toka na ufungue upya)
3. Fungua mazungumzo mapya
4. Tafuta ikoni ya 🔌 inayoonyesha seva zilizounganishwa
5. Jaribu kumuuliza Claude atumie mojawapo ya zana zako

### Kukatatua Matatizo ya Claude Desktop

**Seva haionekani:**
- Angalia muundo wa faili la usanidi kutumia mtathmini wa JSON
- Hakikisha njia ya amri ni sahihi
- Angalia kumbukumbu za Claude Desktop: Msaada → Onyesha Kumbukumbu

**Seva inakufa wakati wa kuanzisha:**
- Jaribu seva yako kwa mkono kwanza kwenye terminal
- Angalia mabadiliko ya mazingira yamewekwa vizuri
- Hakikisha utegemezi wote umewekwa

---

## 2. VS Code na GitHub Copilot

VS Code inaunga mkono MCP kupitia nyongeza za GitHub Copilot Chat.

### Masharti ya Awali

1. VS Code 1.99+ imewekwa
2. Nyongeza ya GitHub Copilot imewekwa
3. Nyongeza ya GitHub Copilot Chat imewekwa

### Usanidi

VS Code hutumia `.vscode/mcp.json` katika eneo lako la kazi au mipangilio ya mtumiaji.

**Usanidi wa eneo la kazi** (`.vscode/mcp.json`):

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

**Mipangilio ya mtumiaji** (`settings.json`):

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

### Kutumia MCP katika VS Code

1. Fungua jopo la Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Andika `@` kuona zana za MCP zinazoonekana
3. Tumia lugha ya asili kuitisha zana: "Hesabu 25 * 48 ukitumia kalkuleta"

### Kukatatua Matatizo ya VS Code

**Seva za MCP hazipaki:**
- Angalia jopo la Output → "MCP" kwa kumbukumbu za makosa
- Reload window: Ctrl+Shift+P → "Developer: Reload Window"
- Hakikisha seva inafanya kazi peke yake kwanza

---

## 3. Cursor

**Cursor** ni mhariri wa nambari ya AI wenye msaada wa MCP uliojengewa ndani.

### Usanidi

1. Pakua Cursor kutoka [cursor.sh](https://cursor.sh)
2. Sakinisha na ingia

### Usanidi

Cursor hutumia muundo wa usanidi kama ule wa Claude Desktop.

**Mahali pa faili la usanidi:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Mfano wa usanidi:**

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

### Kutumia MCP katika Cursor

1. Fungua mazungumzo ya AI ya Cursor (Ctrl+L / Cmd+L)
2. Zana za MCP zinaonekana moja kwa moja katika mapendekezo
3. Muulize AI kufanya kazi ukitumia seva zilizounganishwa

---

## 4. Cline (Kwenye Terminal)

**Cline** ni mteja wa MCP anayeendeshwa kwenye terminal, bora kwa kazi za mstari wa amri.

### Usanidi

```bash
npm install -g @anthropic/cline
```

### Usanidi

Cline hutumia mabadiliko ya mazingira na hoja za mstari wa amri.

**Kutumia mabadiliko ya mazingira:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Kutumia hoja za mstari wa amri:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Faili la usanidi** (`~/.clinerc`):

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

### Kutumia Cline

```bash
# Anza kikao cha mwingiliano
cline

# Utafutaji mmoja na MCP
cline "Calculate the square root of 144 using the calculator"

# Orodhesha zana zinazopatikana
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** ni mhariri mwingine wa nambari wa AI wenye msaada wa MCP.

### Usanidi

1. Pakua Windsurf kutoka [codeium.com/windsurf](https://codeium.com/windsurf)
2. Sakinisha na tengeneza akaunti

### Usanidi

Usanidi wa Windsurf unaendeshwa kupitia UI ya mipangilio:

1. Fungua Mipangilio (Ctrl+, / Cmd+,)
2. Tafuta "MCP"
3. Bonyeza "Hariri katika settings.json"

**Mfano wa usanidi:**

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

## Ulinganisho wa Aina za Usafirishaji

Wenyeji tofauti wanaunga mkono mbinu tofauti za usafirishaji:

| Mwenyeji | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (ingizo/saizi ya kawaida): Bora kwa seva za ndani zinazozinduliwa na mwenyeji
**SSE/HTTP**: Bora kwa seva za mbali au seva zinazoendelea kwa wateja wengi

---

## Kukatatua Matatizo ya Kawaida

### Seva haitaanza

1. **Jaribu seva kwa mkono kwanza:**
   ```bash
   # Kwa Python
   python -m your_server_module
   
   # Kwa Node.js
   node /path/to/server/index.js
   ```

2. **Angalia njia ya amri:**
   - Tumia njia za uhakika pale inavyowezekana
   - Hakikisha lengo lina PATH yako

3. **Thibitisha utegemezi:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Seva inakubali lakini zana hazifanyi kazi

1. **Angalia kumbukumbu za seva** - Wenyeji wengi wana chaguzi za kumbukumbu
2. **Hakikisha usajili wa zana** - Tumia MCP Inspector kujaribu
3. **Angalia vibali** - Zana baadhi zinahitaji ruhusa za faili/mtandao

### Mabadiliko ya mazingira hayapasmwishiwa

- Wenyeji wengine hurekebisha mabadiliko ya mazingira
- Tumia sehemu ya usanidi ya `env` waziwazi
- Epuka data nyeti katika faili za usanidi (tumia usimamizi wa siri)

---

## Mazoea Bora ya Usalama

1. **Usiweka funguo za API** katika faili za usanidi
2. **Tumia mabadiliko ya mazingira** kwa data nyeti
3. **Punguza ruhusa za seva** kwa kile kinachohitajika tu
4. **Pitia msimbo wa seva** kabla ya kutoa upatikanaji kwa mfumo wako
5. **Tumia orodha ya kuruhusu** kwa upatikanaji wa mfumo wa faili na mtandao

---

## Nini Kifuatacho

- [3.13 - Ufafanuzi kwa MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Tengeneza seva yako ya kwanza ya MCP](../01-first-server/README.md)
- [Somo 5 - Mada za Juu](../../05-AdvancedTopics/README.md)

---

## Rasilimali Zaidi

- [Nyaraka za Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Nyongeza ya VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Mafunzo ya MCP - Usafirishaji](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Sajili Rasmi ya Seva za MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
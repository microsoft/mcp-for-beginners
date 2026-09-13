# ការកំណត់រចនាសម្ព័ន្ធអតិថិជនម៉ាស៊ីនផ្ដល់មាស៊ីន MCP ដែលមានប្រជាប្រិយភាព

> [!NOTE]
> ការកំណត់រចនាសម្ព័ន្ធម៉ាស៊ីនផ្ដល់ដែលបញ្ជូនទៅ `/sse` គឺជាឧទាហរណ៍ HTTP+SSE ដើមសម្រាប់
> MCP `2025-11-25`។ សម្រាប់ MCP `2026-07-28` ចូរជ្រើស Streamable HTTP នៅក្នុងម៉ាស៊ីនផ្ដល់ដែល
> គាំទ្រ និងប្រើចំណុចចប់ដែលបានកំណត់ដោយម៉ាស៊ីនមេ។

មគ្គុទេសក៍នេះពិពណ៌នាអំពីវិធីការកំណត់រចនាសម្ព័ន្ធ និងប្រើម៉ាស៊ីនមេ MCP ជាមួយកម្មវិធីម៉ាស៊ីនផ្ដល់ AI ប្រជាប្រិយភាព។ ម៉ាស៊ីនផ្ដល់មួយៗមានវិធីកំណត់រចនាសម្ព័ន្ធផ្ទាល់ខ្លួន ប៉ុន្តែក្រោយពីបានតំឡើងរួច គេនឹងទំនាក់ទំនងជាមួយម៉ាស៊ីនមេ MCP តាមប្រព័ន្ធស្តង់ដារ។

## ម៉ាស៊ីនផ្ដល់ MCP ជាអ្វី?

**ម៉ាស៊ីនផ្ដល់ MCP** គឺជាកម្មវិធី AI ដែលអាចតភ្ជាប់ទៅម៉ាស៊ីនមេ MCP ដើម្បីពង្រីកសមត្ថភាពរបស់វា។ គិតវាដូចជា "មុខម្ខាង" ដែលអ្នកប្រើប្រាស់កាន់កាប់ អំឡុងពេលម៉ាស៊ីនមេ MCP ផ្ដល់ឧបករណ៍ និងទិន្នន័យ "ខាងក្រោយ"។

```mermaid
flowchart LR
    User[👤 អ្នកប្រើ] --> Host[🖥️ ម៉ាស៊ីនបម្រើ MCP]
    Host --> S1[ម៉ាស៊ីនបម្រើ MCP A]
    Host --> S2[ម៉ាស៊ីនបម្រើ MCP B]
    Host --> S3[ម៉ាស៊ីនបម្រើ MCP C]
    
    subgraph "ម៉ាស៊ីនបម្រើពេញនិយម"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## អ្វីដែលត្រូវមានជាមុន

- ម៉ាស៊ីនមេ MCP មួយសម្រាប់តភ្ជាប់ទៅ (មើល [Module 3.1 - First Server](../01-first-server/README.md))
- កម្មវិធីម៉ាស៊ីនផ្ដល់ត្រូវបានដំឡើងលើប្រព័ន្ធរបស់អ្នក
- មានចំណេះដឹងមូលដ្ឋានអំពីឯកសារconfig JSON

---

## 1. Claude Desktop

**Claude Desktop** គឺជាកម្មវិធីម៉ាស៊ីនផ្ដល់ផ្លូវការរបស់ Anthropic ដែលគាំទ្រ MCP របស់ខ្លួនដោយដើម។

### ការដំឡើង

1. ទាញClaude Desktop ពី [claude.ai/download](https://claude.ai/download)
2. ដំឡើង និងចូលដោយគណនីAnthropic របស់អ្នក

### ការកំណត់រចនាសម្ព័ន្ធ

Claude Desktop ប្រើឯកសារកំណត់រចនាសម្ព័ន្ធ JSON ដើម្បីកំណត់ម៉ាស៊ីនមេ MCP។

**ទីតាំងឯកសារកំណត់រចនាសម្ព័ន្ធ ៖**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**ឧទាហរណ៍កំណត់រចនាសម្ព័ន្ធ:**

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

### ជម្រើសកំណត់រចនាសម្ព័ន្ធ

| Field | ពណ៌នា | ឧទាហរណ៍ |
|-------|-------------|---------|
| `command` | កម្មវិធីហៅបញ្ចេញ | `"python"`, `"node"`, `"npx"` |
| `args` | អាគុយម៉ង់បន្ទាត់ពាក្យបញ្ជា | `["-m", "my_server"]` |
| `env` | អថេរសេវាស្ថាន | `{"API_KEY": "xxx"}` |
| `cwd` |ថតការងារ | `"/path/to/server"` |

### សាកល្បងការតំឡើងរបស់អ្នក

1. សូមរក្សាទុកឯកសារកំណត់រចនាសម្ព័ន្ធ
2. ចាប់ផ្ដើមClaude Desktop ជាថ្មីទាំងស្រុង (បិទហើយបើកឡើងវិញ)
3. បើកការសន្ទនាថ្មីមួយ
4. រកសញ្ញា 🔌 សម្រាប់បង្ហាញម៉ាស៊ីនមេដែលបានភ្ជាប់
5. សាកល្បងសួរឱ្យClaude ប្រើឧបករណ៍មួយឬច្រើនរបស់អ្នក

### ដោះស្រាយបញ្ហាClaude Desktop

**ម៉ាស៊ីនមេមិនបង្ហាញ:**
- ពិនិត្យវាយនភាពឯកសារកំណត់រចនាសម្ព័ន្ធជាមួយមេធាវី JSON
- ប្រាកដថាតំបន់នៅកម្មវិធីត្រូវតែត្រឹមត្រូវ
- ពិនិត្យកំណត់ហេតុClaude Desktop: Help → Show Logs

**ម៉ាស៊ីនមេស្ទូចខ្ទាស់ពេលចាប់ផ្ដើម:**
- សាកល្បងម៉ាស៊ីនមេរបស់អ្នកជាមុនសិនតាម terminal
- ពិនិត្យអថេរសេវាស្ថានបានកំណត់ត្រឹមត្រូវ
- ប្រាកដថាមានការដំឡើងគ្រប់ថ្នាក់ដ dependencia

---

## 2. VS Code ជាមួយ GitHub Copilot

VS Code គាំទ្រ MCP តាមរយៈបន្ថែម GitHub Copilot Chat។

### អ្វីដែលត្រូវមានជាមុន

1. VS Code 1.99+ ត្រូវបានដំឡើង
2. បន្ថែម GitHub Copilot ត្រូវបានដំឡើង
3. បន្ថែម GitHub Copilot Chat ត្រូវបានដំឡើង

### ការកំណត់រចនាសម្ព័ន្ធ

VS Code ប្រើ `.vscode/mcp.json` នៅក្នុងកន្លែងការងាររបស់អ្នកឬការកំណត់អ្នកប្រើប្រាស់។

**កំណត់រចនាសម្ព័ន្ធកន្លែងការងារ** (`.vscode/mcp.json`):

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

**កំណត់រចនាសម្ព័ន្ធអ្នកប្រើប្រាស់** (`settings.json`):

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

### ការប្រើ MCP នៅក្នុង VS Code

1. បើកផ្ទាំង Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. វាយ `@` ដើម្បីមើលឧបករណ៍ MCP មានស្រាប់
3. ប្រើភាសាធម្មជាតិដើម្បីហៅឧបករណ៍: "Calculate 25 * 48 using the calculator"

### ដោះស្រាយបញ្ហា VS Code

**ម៉ាស៊ីនមេ MCP មិនដំណើរការ:**
- ពិនិត្យផ្ទាំង Output → "MCP" សម្រាប់កំណត់ហេតុកំហុស
- โหลดវីនដូឡើងវិញ: Ctrl+Shift+P → "Developer: Reload Window"
- ប្រាកដថាម៉ាស៊ីនមេដំណើរការដាច់ដោយឡែកជាមុន

---

## 3. Cursor

**Cursor** គឺជាអ្នកកែសម្រួលកូដដែលផ្តោតលើ AI ជាចម្បង មានការគាំទ្រ MCP ក្នុងខ្លួន។

### ការដំឡើង

1. ទាញ Cursor ពី [cursor.sh](https://cursor.sh)
2. ដំឡើង និងចូល

### ការកំណត់រចនាសម្ព័ន្ធ

Cursor ប្រើទ្រង់ទ្រាយកំណត់រចនាសម្ព័ន្ធស្រដៀងនឹង Claude Desktop។

**ទីតាំងឯកសារកំណត់រចនាសម្ព័ន្ធ:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**ឧទាហរណ៍កំណត់រចនាសម្ព័ន្ធ:**

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

### ការប្រើ MCP នៅក្នុង Cursor

1. បើកការសន្ទនា AI របស់ Cursor (Ctrl+L / Cmd+L)
2. ឧបករណ៍ MCP បង្ហាញដោយស្វ័យប្រវត្តិក្នុងការផ្តល់យោបល់
3. សុំអោយ AI ធ្វើកិច្ចការប្រើម៉ាស៊ីនមេដែលបានភ្ជាប់

---

## 4. Cline (ផ្អែកលើ Terminal)

**Cline** គឺជាអតិថិជន MCP ផ្អែកលើ terminal ដែលសមស្របសម្រាប់ដំណើរការបន្ទាត់ពាក្យបញ្ជា។

### ការដំឡើង

```bash
npm install -g @anthropic/cline
```

### ការកំណត់រចនាសម្ព័ន្ធ

Cline ប្រើអថេរសេវាស្ថាន និងអាគុយម៉ង់បន្ទាត់ពាក្យបញ្ជា។

**ការប្រើអថេរសេវាស្ថាន:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**ការប្រើអាគុយម៉ង់បន្ទាត់ពាក្យបញ្ជា:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**ឯកសារកំណត់រចនាសម្ព័ន្ធ** (`~/.clinerc`):

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

### ការប្រើ Cline

```bash
# ចាប់ផ្តើមសម័យអន្តរកម្ម
cline

# សំណួរតែមួយជាមួយ MCP
cline "Calculate the square root of 144 using the calculator"

# បញ្ជីឧបករណ៍ដែលមានស្រាប់
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** គឺជាអ្នកកែសម្រួលកូដដែលមានថាមពលពី AI មួយទៀតដែលមានការគាំទ្រ MCP។

### ការដំឡើង

1. ទាញ Windsurf ពី [codeium.com/windsurf](https://codeium.com/windsurf)
2. ដំឡើង និងបង្កើតគណនី

### ការកំណត់រចនាសម្ព័ន្ធ

ការកំណត់រចនាសម្ព័ន្ធ Windsurf ត្រូវបានគ្រប់គ្រងតាមអេឡិាយណ៍ UI៖

1. បើក Settings (Ctrl+, / Cmd+,)
2. ស្វែងរក "MCP"
3. ចុច "Edit in settings.json"

**ឧទាហរណ៍កំណត់រចនាសម្ព័ន្ធ:**

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

## ការប្រៀបធៀបប្រភេទដឹកជញ្ជូន

ម៉ាស៊ីនផ្ដល់ផ្សេងគ្នាគាំទ្រមុខងារដឹកជញ្ជូនផ្សេងៗគ្នា៖

| ម៉ាស៊ីនផ្ដល់ | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (បញ្ចូល/បញ្ចេញស្តង់ដារ): ល្អបំផុតសម្រាប់ម៉ាស៊ីនមេក្នុងកន្លែងដែលបានចាប់ផ្ដើមដោយម៉ាស៊ីនផ្ដល់
**SSE/HTTP**: ល្អបំផុតសម្រាប់ម៉ាស៊ីនមេពីចម្ងាយឬម៉ាស៊ីនមេដែលបានចែករំលែករវាងអតិថិជនច្រើន

---

## ការដោះស្រាយបញ្ហាទូទៅ

### ម៉ាស៊ីនមេមិនចាប់ផ្ដើមកំណត់

1. **សាកល្បងម៉ាស៊ីនមេខ្លួនឯងជាមុន:**
   ```bash
   # សម្រាប់ Python
   python -m your_server_module
   
   # សម្រាប់ Node.js
   node /path/to/server/index.js
   ```

2. **ពិនិត្យផ្លូវ command:**
   - ប្រើផ្លូវលំអិតបើអាចធ្វើទៅបាន
   - ប្រាកដថាកម្មវិធីដំណើរការនៅក្នុង PATH របស់អ្នក

3. **បញ្ជាក់ការទាមទារ:**
   ```bash
   # ពីថុន
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### ម៉ាស៊ីនមេតភ្ជាប់បាន ប៉ុន្តែឧបករណ៍មិនដំណើរការ

1. **ពិនិត្យកំណត់ហេតុម៉ាស៊ីនមេ** - ម៉ាស៊ីនផ្ដល់ភាគច្រើនមានជម្រើសកំណត់ហេតុ
2. **បញ្ជាក់ការចុះបញ្ជីឧបករណ៍** - ប្រើ MCP Inspector ដើម្បីសាកល្បង
3. **ពិនិត្យសិទ្ធិ** - ឧបករណ៍ខ្លះត្រូវការចូលប្រើឯកសារ/បណ្តាញ

### អថេរសេវាស្ថានមិនត្រូវបានផ្ទេរ

- ម៉ាស៊ីនផ្ដល់ខ្លះសម្អាតអថេរសេវាស្ថាន
- ប្រើ ប្រ_FIELD `env` ក្នុងកំណត់រចនាសម្ព័ន្ធយ៉ាងច្បាស់
- កុំប្រើទិន្នន័យដែលងាយរងគ្រោះក្នុងឯកសារកំណត់រចនាសម្ព័ន្ធ (ប្រើគ្រប់គ្រងអាថ៌កំបាំង)

---

## ប្រយ័ត្នសុវត្ថិភាពល្អបំផុត

1. **កុំដាក់កូនសោ API នៅក្នុងឯកសារកំណត់រចនាសម្ព័ន្ធ**
2. **ប្រើអថេរសេវាស្ថានសម្រាប់ទិន្នន័យងាយរងគ្រោះ**
3. **ដាក់កំណត់សិទ្ធិម៉ាស៊ីនមែសម្រាប់តែដែលត្រូវការ**
4. **ពិនិត្យកូដម៉ាស៊ីនមេ មុនផ្តល់សិទ្ធិចូលប្រព័ន្ធ**
5. **ប្រើបញ្ជីអនុញ្ញាតសម្រាប់ចូលប្រើប្រព័ន្ធឯកសារ និងបណ្តាញ**

---

## តើតើបន្ទាប់?

- [3.13 - ការត្រួតពិនិត្យជាមួយ MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - បង្កើតម៉ាស៊ីនមេ MCP ដំបូងរបស់អ្នក](../01-first-server/README.md)
- [Module 5 - ប្រធានបទកម្រិតខ្ពស់](../../05-AdvancedTopics/README.md)

---

## ឯកសារបន្ថែម

- [ឯកសារព័ត៌មាន MCP នៃ Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [បន្ថែម MCP សម្រាប់ VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [លក្ខណៈគម្រូ MCP - ប្រភេទដឹកជញ្ជូន](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [ប្រតិបត្តិការម៉ាស៊ីនមេ MCP ផ្លូវការជាតិ](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
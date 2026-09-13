# လူကြိုက်များသော MCP ဟုတ်စ်ကလိုင်များ စက်ဆောက်ခြင်း

> [!NOTE]
> `/sse` ကိုညွှန်ပြသော ဟုတ်စ် ကွန်ဖစ်မြားသည် MCP `2025-11-25` အတွက် အတိတ် HTTP+SSE နမူနာများဖြစ်သည်။
> MCP `2026-07-28` အတွက်၊ ထောက်ခံသော ဟုတ်စ်များတွင် Streamable HTTP ကို ရွေးချယ်ပြီး ဆာဗာမှ သတ်မှတ်ထားသော endpoint ကို အသုံးပြုပါ။


ဟုတ်စ်တိုင်းမှာ ကိုယ်ပိုင် ကွန်ဖစ်ပြုလုပ်နည်းရှိသော်လည်း တပ်ဆင်ပြီးနောက် များစွာသော MCP ဆာဗာများနှင့် စံပြောစနစ်ဖြင့် ဆက်သွယ်စကားပြောကြသည်။

## MCP ဟုတ်စ် ဆိုတာဘာလဲ?

**MCP ဟုတ်စ်** ဆိုသည်မှာ ၎င်း၏ စွမ်းဆောင်နိုင်မှုများကို တိုးချဲ့ရန် MCP ဆာဗာများနှင့် ချိတ်ဆက်နိုင်သော AI အပလီကေးရှင်းတစ်ခုဖြစ်သည်။ ၎င်းကို အသုံးပြုသူများနှင့် ပြန်လည်ဆက်ဆံသည့် "ရှေ့ဖက်" ဟု သတ်မှတ်နိုင်ပြီး MCP ဆာဗာများသည် "နောက်ဖက်" ကိရိယာများနှင့် ဒေတာများကို ပံ့ပိုးပေးသည်။

```mermaid
flowchart LR
    User[👤 အသုံးပြုသူ] --> Host[🖥️ MCP မှင်ဆာ]
    Host --> S1[MCP ဆာဗာ A]
    Host --> S2[MCP ဆာဗာ B]
    Host --> S3[MCP ဆာဗာ C]
    
    subgraph "လူကြိုက်များသော မှင်ဆာများ"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## မတိုင်မီလိုအပ်ချက်များ

- ချိတ်ဆက်ရန် MCP ဆာဗာတစ်ခု (ကြည့်ပါ [Module 3.1 - ပထမဆုံး ဆာဗာ](../01-first-server/README.md))
- သင့်စနစ်တွင် ထည့်သွင်းထားသည့် ဟုတ်စ်အပလီကေးရှင်း
- JSON ကွန်ဖစ်ဖိုင်များအတွက် အခြေခံသိရှိမှု

---

## 1. Claude Desktop

**Claude Desktop** သည် Anthropic ၏ တရားဝင် မီးနံပန်းအက်ပ်ဖြစ်ပြီး MCP ကို သဘာဝပေါ်မူတည်ပြီး ထောက်ခံသည်။

### တပ်ဆင်ခြင်း

1. Claude Desktop ကို [claude.ai/download](https://claude.ai/download) မှ ဒေါင်းလုပ်လုပ်ပါ
2. ထည့်သွင်းပြီး သင်၏ Anthropic အကောင့်ဖြင့် ချိတ်ဆက်ဝင်ပါ

### ကွန်ဖစ်ပြုလုပ်ခြင်း

Claude Desktop သည် MCP ဆာဗာများကို သတ်မှတ်ရန် JSON ကွန်ဖစ်ဖိုင်ကို အသုံးပြုသည်။

**ကွန်ဖစ်ဖိုင်တည်နေရာ:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**နမူနာကွန်ဖစ်:**

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

### ကွန်ဖစ်ရွေးချယ်စရာများ

| စာရင်း | ဖော်ပြချက် | နမူနာ |
|-------|-------------|---------|
| `command` | လုပ်ဆောင်မည့် အရာ | `"python"`, `"node"`, `"npx"` |
| `args` | ကွန်မန္များ စာကြောင်းတန်းများ | `["-m", "my_server"]` |
| `env` | ပတ်ဝန်းကျင် အရင်းအမြစ်များ | `{"API_KEY": "xxx"}` |
| `cwd` | လုပ်ငန်းတိုက် ဒစ်ရေးပါတရီ | `"/path/to/server"` |

### သင့်စက်တင်ကို စမ်းသပ်ခြင်း

1. ကွန်ဖစ်ဖိုင်ကို သိမ်းဆည်းပါ
2. Claude Desktop ကို ပြန်စတင်ပါ (ပိတ်ပြီး ထပ်ဖွင့်ပါ)
3. စကားပြောသစ်တစ်ခု ဖွင့်ပါ
4. ဆာဗာများချိတ်ဆက်ပြီးသည်ကို ဖော်ပြသော 🔌 ရုပ်သံကို ကြည့်ပါ
5. Claude ကို သင့်ကိရိယာများကို အသုံးပြုရန် မေးမြန်းကြည့်ပါ

### Claude Desktop ပြဿနာဖြေရှင်းခြင်း

**ဆာဗာမပေါ်ပါက:**
- JSON တရားဝင်စနစ်ဖြင့် ကွန်ဖစ်ဖိုင် ဖော်မြူးမှု စစ်ဆေးပါ
- command လမ်းကြောင်းမှန်ကန်မှုစစ်ဆေးပါ
- Claude Desktop မှတ်တမ်းတွေကို စစ်ဆေးပါ: Help → Show Logs

**ဆာဗာ စတင်ချိန်တွင် ကျရှုံးမှု:**
- သင့်ဆာဗာကို Terminal မှာ သေချာစွာ စမ်းသပ်ပါ
- ပတ်ဝန်းကျင်အပြောင်းအလဲများကို မှန်ကန်စွာ သတ်မှတ်ထားမှု စစ်ဆေးပါ
- မိတ်ဆက်ထားသော မပါဝင်မှုများအားလုံး အတည်ပြုပါ

---

## 2. VS Code နှင့် GitHub Copilot

VS Code သည် GitHub Copilot Chat ဖြစ်သည် extension များမှတဆင့် MCP ကို ထောက်ခံသည်။

### မတိုင်မီလိုအပ်ချက်များ

1. VS Code 1.99+ ထည့်သွင်းထားခြင်း
2. GitHub Copilot extension ထည့်သွင်းထားခြင်း
3. GitHub Copilot Chat extension ထည့်သွင်းထားခြင်း

### ကွန်ဖစ်ပြုလုပ်ခြင်း

VS Codeသည် `.vscode/mcp.json` ကို သင်၏ အလုပ်လုပ်နေရာ (workspace) သို့မဟုတ် အသုံးပြုသူ စက်တင်များတွင် အသုံးပြုသည်။

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

### VS Code တွင် MCP အသုံးပြုခြင်း

1. Copilot Chat panel ကို ဖွင့်ပါ (Ctrl+Shift+I / Cmd+Shift+I)
2. အသုံးပြုနိုင်သည့် MCP ကိရိယာများကို ကြည့်ရန် `@` ကိုရိုက်ထည့်ပါ
3. သဘာဝဘာသာစကားဖြင့် ကိရိယာများ ပို့စ်ပေးပါ - "Calculate 25 * 48 using the calculator"

### VS Code ပြဿနာဖြေရှင်းခြင်း

**MCP ဆာဗာများ မပေါ်ပါက:**
- Output panel → "MCP" တွင် error logs များစစ်ဆေးပါ
- ပြန်လည်ဖွင့်ရန်: Ctrl+Shift+P → "Developer: Reload Window"
- ဆာဗာ standalone အဖြစ် စမ်းသပ်ပါ

---

## 3. Cursor

**Cursor** သည် MCP ထောက်ခံမှု ပါဝင်သည့် AI အလေးတင် ကုဒ်တည်းဖြတ်ရန်အပ်ဖြစ်သည်။

### တပ်ဆင်ခြင်း

1. Cursor ကို [cursor.sh](https://cursor.sh) မှ ဒေါင်းလုပ်လုပ်ပါ
2. ထည့်သွင်းပြီး အကောင့်ဝင်ပါ

### ကွန်ဖစ်ပြုလုပ်ခြင်း

Cursor သည် Claude Desktop နှင့် ဆင်တူသော ကွန်ဖစ်ဖိုင် ပုံစံကို အသုံးပြုသည်။

**ကွန်ဖစ်ဖိုင်တည်နေရာ:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**နမူနာကွန်ဖစ်:**

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

### Cursor တွင် MCP အသုံးပြုခြင်း

1. Cursor ၏ AI စကားပြော (Ctrl+L / Cmd+L) ကို ဖွင့်ပါ
2. MCP ကိရိယာများကို အကြံပြုချက်များ၌ အလိုအလျောက် ပြသသည်
3. ချိတ်ဆက်ထားသည့် ဆာဗာများကို အသုံးပြု၍ AI ကို လုပ်ငန်းများ တိုက်တွန်းပါ

---

## 4. Cline (Terminal မူရင်း)

**Cline** သည် terminal အခြေပြု MCP ကလိုင်ဖြစ်ပြီး command-line အလုပ်လုပ်သော လုပ်ငန်းများအတွက် ကိုက်ညီသည်။

### တပ်ဆင်ခြင်း

```bash
npm install -g @anthropic/cline
```

### ကွန်ဖစ်ပြုလုပ်ခြင်း

Cline သည် ပတ်ဝန်းကျင် အရင်းအမြစ်များနှင့် command-line အတည်ပြုချက်များကို အသုံးပြုသည်။

**ပတ်ဝန်းကျင် အရင်းအမြစ်များ အသုံးပြုခြင်း:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**command-line အတည်ပြုချက်များ အသုံးပြုခြင်း:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**ကွန်ဖစ်ဖိုင်** (`~/.clinerc`):

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

### Cline အသုံးပြုခြင်း

```bash
# အပြန်အလှန်အလုပ်လုပ်ရန်အစပြုပါ
cline

# MCP ဖြင့် တစ်ခုတည်းသော မေးခွန်း
cline "Calculate the square root of 144 using the calculator"

# အသုံးပြုနိုင်သည့်ကိရိယာများကို ပေါင်းစုပါ
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** သည် MCP ထောက်ခံမှု ပါဝင်သည့် AI စွမ်းဆောင်ရည်ပြည့်သော ကုဒ်တည်းဖြတ်ရန်အပ်ဖြစ်သည်။

### တပ်ဆင်ခြင်း

1. Windsurf ကို [codeium.com/windsurf](https://codeium.com/windsurf) မှ ဒေါင်းလုပ်လုပ်ပါ
2. ထည့်သွင်းပြီး အကောင့်ဖန်တီးပါ

### ကွန်ဖစ်ပြုလုပ်ခြင်း

Windsurf ကွန်ဖစ်ပြုလုပ်မှုကို settings UI မှ တာဝန်ယူထားသည်။

1. Settings ကို ဖွင့်ပါ (Ctrl+, / Cmd+,)
2. "MCP" ကို ရှာဖွေပါ
3. "Edit in settings.json" ကို နှိပ်ပါ

**နမူနာကွန်ဖစ်:**

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

## သယ်ယူပို့ဆောင်မှု ပုံစံများနှိုင်းယှဉ်

ဟုတ်စ်များပေါ်မူတည်၍ သယ်ယူပို့ဆောင်မှု မော်ဒယ်အမျိုးမျိုးအထောက်အပံ့ရှိသည်။

| ဟုတ်စ် | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (မူဝါဒ အွတ်မြေး/ထွက်): ဟုတ်စ်မှ စတင်သော ဒေသတွင်းဆာဗာများအတွက် သင့်လျော်သည်
**SSE/HTTP**: ဝေးလံသော ဆာဗာများ သို့မဟုတ် စနစ်တကျ မျှဝေသော ဆာဗာများအတွက် အကောင်းဆုံးဖြစ်သည်

---

## ပုံမှန် ပြဿနာဖြေရှင်းနည်းများ

### ဆာဗာ မစတင်နိုင်ခြင်း

1. **ဆာဗာကို အရင်ဆုံး လက်တွင် စမ်းသပ်ပါ:**
   ```bash
   # Python အတွက်
   python -m your_server_module
   
   # Node.js အတွက်
   node /path/to/server/index.js
   ```

2. **command လမ်းကြောင်း စစ်ဆေးပါ:**

   - အပြည့်အစုံဖြစ်သော လမ်းကြောင်းများကို သုံးပါ
   - အကောင်အထည်ဖော်နိုင်သော ဖိုင်သည် သင့် PATH တွင်တည်ရှိခြင်းကို အာမခံပါ

3. **မူလအရာများကို အတည်ပြုပါ:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### ဆာဗာသည် ချိတ်ဆက်သော်လည်း ကိရိယာများ မအလုပ်ဖြစ်ခြင်း

1. **ဆာဗာမှတ်တမ်းများကို စစ်ဆေးပါ** - အများဆုံး ဟော့တ်များတွင် မှတ်တမ်း options ရှိသည်
2. **ကိရိယာ မှတ်ပုံတင်ခြင်းကို အတည်ပြုပါ** - MCP Inspector ကို သုံးပြီး စမ်းသပ်ပါ
3. **ခွင့်ပြုချက်များကို စစ်ဆေးပါ** - ကိရိယာတချို့တွင် ဖိုင်/ကွန်ရက် အတတ်နိုင်မှုလိုအပ်သည်

### ပတ်ဝန်းကျင် မလုပ်បានသော ဒေတာများ မပို့ပေးခြင်း

- အချို့ ဟော့တ်များသည် ပတ်ဝန်းကျင် ဒေတာများကို သန့်စင်ကြသည်
- `env` ဖော်ပြချက်ကွက်ကို အထူးအသုံးပြုပါ
- အရေးကြီးသော ဒေတာများကို ဖိုင်တွင် ထည့်ထည့်မှာ မဟုတ်ပါနှင့် (secrets management ကို အသုံးပြုပါ)

---

## လုံခြုံရေး အကောင်းဆုံးကျင့်သုံးမှုများ

1. **API key များကို configuration ဖိုင်များတွင် ဘယ်တော့မှ commit မပြုလုပ်ပါနှင့်**
2. **အရေးကြီးသော ဒေတာများအတွက် environment variable များကို အသုံးပြုပါ**
3. **ဆာဗာ ခြင့်ပြုချက်များကို လိုအပ်သမျှသာ မိန့်ပါ**
4. **သင့်စနစ်အပေါ် ချိတ်ဆက်ခွင့်မတွဲမီ ဆာဗာကုဒ်ကို ပြန်လည်သုံးသပ်ပါ**
5. **ဖိုင်စနစ်နှင့် ကွန်ရက် ခွင့်ပြုချက်များအတွက် allowlists ကို သုံးပါ**

---

## နောက်ဆက်တွဲ အကြောင်းအရာများ

- [3.13 - MCP Inspector ဖြင့် ပြဿနာဖြေရှင်းခြင်း](../13-mcp-inspector/README.md)
- [3.1 - သင့် ပထမဆုံး MCP ဆာဗာ ကို ဖန်တီးခြင်း](../01-first-server/README.md)
- [Module 5 - အဆင့်မြင့် ခေါင်းစဉ်များ](../../05-AdvancedTopics/README.md)

---

## ထပ်ဆောင်း အရင်းအမြစ်များ

- [Claude Desktop MCP စာတမ်းများ](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specification - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [တရားဝင် MCP ဆာဗာ စာရင်း](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
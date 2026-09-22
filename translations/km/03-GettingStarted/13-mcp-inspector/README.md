# ការដោះស្រាយបញ្ហា​ជាមួយ MCP Inspector

> [!NOTE]
> ពាក្យបញ្ជាដោយប្រើ `--sse` និង URL ដែលបញ្ចប់ដោយ `/sse` ផ្ទៀងផ្ទាត់ការដឹកជញ្ជូន HTTP+SSE ចាស់។
> សម្រាប់ម៉ាស៊ីនមេ MCP ម៉ូដែលថ្មី `2026-07-28` សូមប្រើ Inspector ដែល
> គាំទ្រការដឹកជញ្ជូន Streamable HTTP ហើយជ្រើសរើសការដឹកជញ្ជូននោះវិញ។

**MCP Inspector** គឺជាឧបករណ៍សំខាន់សម្រាប់ដោះស្រាយបញ្ហាដែលអនុញ្ញាតឱ្យអ្នកសាកល្បង និងជួសជុលម៉ាស៊ីនមេ MCP របស់អ្នកដោយអន្តរកម្ម ដោយមិនចាំបាច់មានកម្មវិធី AI រួមបញ្ចូលទាំងមូល។ គិតថាវាជា "Postman សម្រាប់ MCP" - វាបង្ហាញផ្ទាំងផ្លូវក្រោមដើម្បីផ្ញើសំណើ មើលចម្លើយ និងយល់ពីរបៀបដែលម៉ាស៊ីនមេទើបផ្ទុះ។

## ហេតុផលដែលត្រូវប្រើ MCP Inspector?

នៅពេលដែលសាងសង់ម៉ាស៊ីនមេ MCP អ្នកអាចប្រឈមមុខនឹងបញ្ហាទាំងនេះ:

- **"ម៉ាស៊ីនមេរបស់ខ្ញុំដំណើរការទេ?"** - Inspector បង្ហាញស្ថានភាពការតភ្ជាប់
- **"ឧបករណ៍របស់ខ្ញុំត្រូវបានចុះបញ្ជីត្រឹមត្រូវទេ?"** - Inspector បង្ហាញបញ្ជីឧបករណ៍ទាំងអស់
- **"ទ្រង់ទ្រាយចម្លើយជាអ្វី?"** - Inspector បង្ហាញចម្លើយ JSON ពេញលេញ
- **"ហេតុអ្វីបានជា​ឧបករណ៍នេះមិនដំណើរការទេ?"** - Inspector បង្ហាញសារបង្ហាញកំហុសលម្អិត

## លក្ខខណ្ឌមុន

- Node.js 18+ ត្រូវបានដំឡើង
- npm (ភ្ជាប់មកជាមួយ Node.js)
- ម៉ាស៊ីនមេ MCP សម្រាប់ធ្វើតេស្ត (មើល [Module 3.1 - First Server](../01-first-server/README.md))

## ការដំឡើង

### ជម្រើសទី១៖ រត់ជាមួយ npx (ណែនាំសម្រាប់ការធ្វើតេស្តលឿន)

```bash
npx @modelcontextprotocol/inspector
```

### ជម្រើសទី២៖ ដំឡើងជាសកល

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### ជម្រើសទី៣៖ បញ្ចូលទៅក្នុងគម្រោងរបស់អ្នក

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

បញ្ចូលទៅក្នុង `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## ការតភ្ជាប់ទៅម៉ាស៊ីនមេរបស់អ្នក

### ម៉ាស៊ីនមេ stdio (ដំណើរការប្រព័ន្ធក្នុងស្រុក)

សម្រាប់ម៉ាស៊ីនមេដែលផ្សព្វផ្សាយតាមបញ្ចូល/បញ្ចេញស្តង់ដារ៖

```bash
# រដ្ឋបាល Python
npx @modelcontextprotocol/inspector python -m your_server_module

# រដ្ឋបាល Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# ជាមួយអថេរបរិស្ថាន
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### ម៉ាស៊ីនមេ SSE/HTTP (បណ្ដាញ)

សម្រាប់ម៉ាស៊ីនមេដែលដំណើរការជាសេវាកម្ម HTTP៖

1. ចាប់ផ្តើមម៉ាស៊ីនមេខាងមុន៖
   ```bash
   python server.py  # ប្រព័ន្ធផ្សព្វផ្សាយដំណើរការនៅលើ http://localhost:8080
   ```

2. បើក Inspector ហើយតភ្ជាប់៖
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## ទិដ្ឋភាពផ្ទៃមុខ Inspector

នៅពេលដែល Inspector បើក អ្នកនឹងមើលឃើញផ្ទៃមុខបណ្ដាញ (ជាទូទៅនៅ `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ការធ្វើតេស្តឧបករណ៍

### បញ្ជីឧបករណ៍ដែលអាចប្រើបាន

1. ចុចផ្ទាំង **Tools**
2. Inspector ដំណើរការការហៅ `tools/list`
3. អ្នកនឹងឃើញឧបករណ៍ទាំងអស់ដែលបានចុះបញ្ជីជាមួយ:
   - ឈ្មោះឧបករណ៍
   - សេចក្ដីពិពណ៌នា
   - លំនាំបញ្ចូល (ប៉ារ៉ាម៉ែត្រ)

### ការហៅឧបករណ៍មួយ

1. ជ្រើសរើសឧបករណ៍ពីបញ្ជី
2. បំពេញប៉ារ៉ាម៉ែត្រដែលត្រូវការនៅក្នុងទម្រង់
3. ចុច **Run Tool**
4. មើលចម្លើយនៅក្នុងផ្ទាំងលទ្ធផល

**ឧទាហរណ៍៖ ការធ្វើតេស្តឧបករណ៍គណនាគ្រាប់**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### ការដោះស្រាយកំហុសឧបករណ៍

នៅពេលឧបករណ៍បរាជ័យ Inspector បង្ហាញ:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

កូដកំហុសទូទៅ៖
| កូដ | គោលបំណង |
|------|---------|
| -32700 | កំហុសបកប្រែ (JSON មិនត្រឹមត្រូវ) |
| -32600 | សំណើមិនត្រឹមត្រូវ |
| -32601 | វិធីសាស្រ្តគ្មានទេ |
| -32602 | ប៉ារ៉ាម៉ែត្រ​មិនត្រឹមត្រូវ |
| -32603 | កំហុសខាងក្នុង |

---

## ការធ្វើតេស្តធនធាន

### បញ្ជីធនធាន

1. ចុចផ្ទាំង **Resources**
2. Inspector ហៅ `resources/list`
3. អ្នកនឹងឃើញ:
   - URL ធនធាន
   - ឈ្មោះ និងសេចក្ដីពិពណ៌នា
   - ប្រភេទ MIME

### ការអានធនធាន


1. ជ្រើសរើសធនធានមួយ
2. ចុច **អានធនធាន**
3. មើលខ្លឹមសារដែលត្រូវបានត្រឡប់មកវិញ

**លទ្ធផលឧទាហរណ៍៖**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## ការធ្វើតេស្តការជំរុញ

### ការចុះបញ្ជីការជំរុញ

1. ចុចផ្ទាំង **ការជំរុញ**
2. អ្នកត្រួតពិនិត្យហៅ `prompts/list`
3. មើលប្លង់ការជំរុញដែលមានស្រាប់

### ការទទួលបានការជំរុញ

1. ជ្រើសរើសការជំរុញមួយ
2. បំពេញបំណុលដែលត្រូវការ
3. ចុច **ទទួលបានការជំរុញ**
4. មើលសារជំរុញដែលបានបង្ហាញ

---

## ការវិភាគកំណត់ហេតុសារជូន

កំណត់ហេតុសារជូនបង្ហាញសារប្រព័ន្ធ MCP ទាំងអស់។ កំណត់ហេតុនេះគឺមកពីម៉ាស៊ីនមេ `2025-11-25` ហើយរួមបញ្ចូលការចុះហត្ថលេខា `initialize` ដែលត្រូវបានដកចេញ។ ម៉ាស៊ីនមេនៅ `2026-07-28` ប្រើពត៌មានសំណើដែលមាននៅក្នុងខ្លួនឯង និង `server/discover` ជំនួស។
legacy `2025-11-25` server and includes the removed `initialize` handshake. A
`2026-07-28` server uses self-contained request metadata and `server/discover`
instead.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### អ្វីដែលគួរតែសង្កេត

- **គូសំណើ/ចំលოგ**: រាល់ `→` ត្រូវមាន `←` តំរៀប
- **សារ​កំហុស**: ស្វែងរក `"error"` ក្នុងចំលុងការឆ្លើយតប
- **ពេលវេលា**: ចន្លោះធំអាចបង្ហាញពីបញ្ហាប្រសិទ្ធភាព
- **ជំនាន់ប្រព័ន្ធ**: ប្រាកដថាម៉ាស៊ីនមេ និងអតិថិជនយល់ព្រមនៅលើជំនាន់

---

## ការបញ្ជូល VS Code

អ្នកអាចរត់ Inspector ត្រង់ពី VS Code បាន:

### ការប្រើ launch.json

បន្ថែមទៅ `.vscode/launch.json`៖

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### ការប្រើ Tasks

បន្ថែមទៅ `.vscode/tasks.json`៖

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## សេណារីយៗជួសជុលកំហុសទូទៅ

### សេណារីយ៍ 1: ម៉ាស៊ីនមេមិនភ្ជាប់បាន

**រោគសញ្ញា:** Inspector បង្ហាញ "បានដំរុញចេញ" ឬតំណក់នៅលើ "កំពុងភ្ជាប់..."

**បញ្ជីត្រួតពិនិត្យ:**
1. ✅ តើពាក្យបញ្ជាម៉ាស៊ីនមេច្បាស់លាស់ឬ?
2. ✅ តើហ្វាយរាយការណ៍ទាំងអស់ត្រូវបានតំឡើងហើយឬ?
3. ✅ តើផ្លូវម៉ាស៊ីនមេជាគន្លងពេញលេញ ឬទាក់ទាញទៅកាន់ថតបច្ចុប្បន្ន?
4. ✅ តើអថេរ​បរិស្ថាន​ដែលតម្រូវបានកំណត់ហើយឬ?

**ជំហានដោះស្រាយបញ្ហា:**
```bash
# សាកល្បងម៉ាស៊ីនមេដោយ​ដៃជាមុន
python -c "import your_server_module; print('OK')"

# ពិនិត្យមើលការបញ្ចូលកំហុស
python -m your_server_module 2>&1 | head -20

# ផ្ទៀងផ្ទាត់ថា MCP SDK ត្រូវបានដំឡើងហើយ
pip show mcp
```

### សេណារីយ៍ 2: ឧបករណ៍មិនបង្ហាញ

**រោគសញ្ញា:** ផ្ទាំងឧបករណ៍បង្ហាញបញ្ជីទំនេរ

**ហេតុផលអាចកើតមាន៖**
1. ឧបករណ៍មិនបានចុះបញ្ជីនៅពេលចាប់ផ្ដើមម៉ាស៊ីនមេ
2. ម៉ាស៊ីនមេចេញផ្សាយបន្ទាប់ពីចាប់ផ្តើម
3. អ្នកដំណើរការ `tools/list` បង្គាប់ត្រីមាសទទេ

**ជំហានដោះស្រាយបញ្ហា:**
1. ពិនិត្យកំណត់ហេតុសារជូនសម្រាប់ចំលើយ `tools/list`
2. បន្ថែមការចុះបញ្ជីកូដចុះបញ្ជីឧបករណ៍របស់អ្នក
3. ផ្ទៀងផ្ទាត់ថា មាន `@mcp.tool()` ការតុបតែង (Python)

### សេណារីយ៍ 3: ឧបករណ៍ឆ្លើយតបកំហុស

**រោគសញ្ញា:** ការហៅឧបករណ៍ឆ្លើយតបកំហុស

**វិធីសាស្រ្តដោះស្រាយបញ្ហា:**
1. អានសារកំហុសយ៉ាងច្បាស់លាស់
2. ពិនិត្យប្រភេទប៉ារ៉ាម៉ែត្រត្រូវទៅនឹងស្គីម៉ា
3. បន្ថែមសារកំហុសលម្អិតដើម្បីសាកល្បង/ចាប់កំហុស
4. ពិនិត្យកន្លែងបញ្ជូលកំណត់ហេតុម៉ាស៊ីនសម្រាប់តាមដាន

**ឧទាហរណ៍ទ្រង់ទ្រាយកែសម្រួលកំហុស:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # គន្លងហេតុការណ៍ឧបករណ៍នៅទីនេះ
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### សេណារីយ៍ 4: ខ្លឹមសារធនធានទទេ

**រោគសញ្ញា:** ធនធានត្រឡប់មកវិញប៉ុន្តខ្លឹមសារទទេ ឬ null

**បញ្ជីត្រួតពិនិត្យ:**
1. ✅ ផ្លូវឯកសារ ឬ URI ត្រឹមត្រូវ
2. ✅ ម៉ាស៊ីនមេមានសិទ្ធិអានធនធាន។
3. ✅ ខ្លឹមសារធនធានត្រូវបានត្រឡប់យ៉ាងត្រឹមត្រូវ

---

## លក្ខណៈពិសេស Inspector ទាញមុខ

### ក្បាលផ្ទាល់ខ្លួន (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### ការចុះបញ្ជីពិពណ៌នាយ៉ាងលម្អិត

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### ការថតសម័យសន្ដិសុខ

Inspector អាចនាំចេញកំណត់ហេតុសារជូនសម្រាប់វិភាគនៅពេលក្រោយ៖
1. ចុច **នាំចេញកំណត់ហេតុ** នៅផ្នែកសារ
2. រក្សាទុកឯកសារ JSON
3. ចែករំលែកជាមួយសមាជិកក្រុមសម្រាប់ការជួសជុលកំហុស

---


## ចំណេះដឹងល្អបំផុត

1. **សាកល្បងមុននិងជារៀងរាល់ដង** - ប្រើកម្មវិធី Inspector ក្នុងការអភិវឌ្ឍ សិនមុន​មិនមែនពេលអ្វីៗខូចទេ
2. **ចាប់ផ្តើមពីងាយស្រួល** - សាកល្បងការតភ្ជាប់មូលដ្ឋានមុនការហៅឧបករណ៍ស្មុគស្មាញ
3. **ពិនិត្យ schema** - បញ្ហាច្រើនមកពីការមិនត្រូវគ្នានៃប្រភេទប៉ារ៉ាម៉ែត្រ
4. **អានសារ​បញ្ហា** - កំហុស MCP ជាធម្មតាមានការពណ៌នាលម្អិត
5. **រក្សា Inspector បើក** - វាជួយចាប់កំហុសនៅពេលអ្នកអភិវឌ្ឍ

---

## អ្វីទៅជាបន្ទាប់?

អ្នកបានបញ្ចប់ Module 3: Getting Started! បន្តការសិក្សារបស់អ្នក:

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## ឯកសារបន្ថែម

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# ការបញ្ចូលពីរបៀប Debugging នៅជាមួយ MCP Inspector

**MCP Inspector** គឺជាឧបករណ៍ debugging ដែលមានសារៈសំខាន់ ដែលអនុញ្ញាតឱ្យអ្នកធ្វើតេស្ត និងដោះស្រាយបញ្ហាជាមួយម៉ាស៊ីនមេ MCP របស់អ្នកដោយផ្ទាល់ដោយមិនចាំបាច់មានកម្មវិធី​រៀបចំ AI ពេញលេញណា។ គិតថាវា​ជា "Postman សម្រាប់ MCP" - វា​ផ្ដល់មុខងារជាផ្ទាំងមើលឃើញ​ដើម្បីផ្ញើការស្នើសំម្ដី ទស្សនាលទ្ធផល និងយល់ពីរបៀបដែលម៉ាស៊ែរបស់អ្នកធ្វើការ។

## ហេតុអ្វីបានជា​ប្រើ MCP Inspector?

ពេលដែលកំពុងបង្កើតម៉ាស៊ែរម៉ាស៊ីន MCP អ្នកអាចជួបប្រទះបញ្ហាទាំងនេះ៖

- **"ម៉ាស៊ីនមេរបស់ខ្ញុំកំពុងដំណើរការឬទេ?"** - Inspector បង្ហាញស្ថានភាពចុះតភ្ជាប់
- **"ឧបករណ៍របស់ខ្ញុំទាំងអស់ត្រូវបានចុះបញ្ជីត្រឹមត្រូវហើយទេ?"** - Inspector បង្ហាញបញ្ជីឧបករណ៍ទាំងអស់
- **"ទ្រង់ទ្រាយចម្លើយមានរបៀបណា?"** - Inspector បង្ហាញចម្លើយ JSON ពេញលេញ
- **"ហេតុអ្វីឧបករណ៍នេះមិនដំណើរការទេ?"** - Inspector បង្ហាញសារ​កំហុស​លម្អិត

## ទាមទារ​តម្រូវការ​​

- Node.js 18+ ត្រូវបានដំឡើង
- npm (បានមកជាមួយ Node.js)
- ម៉ាស៊ីនមេ MCP សម្រាប់ធ្វើតេស្ត (មើល [Module 3.1 - First Server](../01-first-server/README.md))

## វិធីដំឡើង

### ជម្រើសទី 1៖ ប្រើ npx (ផ្ដល់អនុសាសន៍សម្រាប់តេស្តលឿន)

```bash
npx @modelcontextprotocol/inspector
```

### ជម្រើសទី 2៖ ដំឡើងជាសកល

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### ជម្រើសទី 3៖ បញ្ចូលទៅគម្រោងរបស់អ្នក

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

បន្ថែមទៅកាន់ `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## ការតភ្ជាប់ទៅម៉ាស៊ីនមេរបស់អ្នក

### ម៉ាស៊ីនមេ stdio (ដំណើរការប្រតិបត្តិការ ក្នុងតំបន់)

សម្រាប់ម៉ាស៊ីនមេដែលធ្វើការទំនាក់ទំនងតាម​បញ្ចូល/បញ្ចាំងស្តង់ដារ:

```bash
# ម៉ាស៊ីនម៉ាស៊ីន Python
npx @modelcontextprotocol/inspector python -m your_server_module

# ម៉ាស៊ីន Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# ជាមួយអថេរបរិស្ថាន
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### ម៉ាស៊ីនមេ SSE/HTTP (បណ្ដាញ)

សម្រាប់ម៉ាស៊ីនមេដំណើរការជាសេវា HTTP:

1. ចាប់ផ្តើមម៉ាស៊ីនមេរបស់អ្នកជាមុនសិន៖
   ```bash
   python server.py  # ម៉ាស៊ីនមេដំណើរការនៅលើ http://localhost:8080
   ```

2. បើក Inspector ហើយភ្ជាប់៖
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## ទិដ្ឋភាពមុខងារ Inspector

ពេល Inspector ចាប់ផ្តើម អ្នកនឹងឃើញផ្ទាំងគេហទំព័រ (ភាគច្រើននៅ `http://localhost:5173`):

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

## ការតេស្តឧបករណ៍

### បញ្ជីឧបករណ៍ដែលមានប្រើ

1. ចុចផ្ទាំង **Tools**
2. Inspector បង្ហាញការហៅ `tools/list` ជាអូតូម៉ាទិច
3. អ្នកនឹងឃើញឧបករណ៍ទាំងអស់ដែលបានចុះបញ្ជីដោយ​មាន៖
   - ឈ្មោះឧបករណ៍
   - ការពិពណ៌នា
   - គំរូបញ្ចូល (ប៉ារ៉ាម៉ែត្រ)

### ការហៅឧបករណ៍

1. ជ្រើសឧបករណ៍ពីបញ្ជី
2. បញ្ចូលប៉ារ៉ាម៉ែត្រចាំបាច់នៅក្នុងទម្រង់
3. ចុច **Run Tool**
4. មើលចម្លើយនៅផ្ទាំងលទ្ធផល

**ឧទាហរណ៍៖ ការធ្វើតេស្តឧបករណ៍គណនាយន្ត**

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

### ដោះស្រាយកំហុសឧបករណ៍

ពេលឧបករណ៍បរាជ័យ Inspector នឹងបង្ហាញ៖

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
| កូដ | អត្ថន័យ |
|------|---------|
| -32700 | ពន្យល់បានមិនត្រឹមត្រូវ (JSON មិនត្រឹម) |
| -32600 | សំណើមិនត្រឹមត្រូវ |
| -32601 | មិនមានវិធីសាស្រ្ត |
| -32602 | ប៉ារ៉ាម៉ែត្រមិនត្រឹមត្រូវ |
| -32603 | កំហុសផ្នែកក្នុង |

---

## ការតេស្តធនធាន

### បញ្ជីធនធាន

1. ចុចផ្ទាំង **Resources**
2. Inspector ហៅ `resources/list`
3. អ្នកនឹងឃើញ៖
   - URI ធនធាន
   - ឈ្មោះ និងការពិពណ៌នា
   - ប្រភេទ MIME

### ការអានធនធាន

1. ជ្រើសធនធាន
2. ចុច **Read Resource**
3. មើលខ្លឹមសារដែលត្រូវបានផ្តល់វិញ

**ឧទាហរណ៍លទ្ធផល៖**

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

## ការតេស្តសារ​សម្គាល់

### បញ្ជីសារ​សម្គាល់

1. ចុចផ្ទាំង **Prompts**
2. Inspector ហៅ `prompts/list`
3. មើលគំរូសារ​សម្គាល់ដែលមានជ្រើស

### ទទួលបានសារ​សម្គាល់

1. ជ្រើសសារ​សម្គាល់
2. បញ្ចូលអាគុយម៉ង់ដែលត្រូវការ
3. ចុច **Get Prompt**
4. មើលសារ​សម្គាល់ដែលបានបង្ហាញ

---

## វិភាគកំណត់ហេតុសារ

កំណត់ហេតុនេះបង្ហាញសារ MCP សកលទាំងអស់៖

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### អ្វីដែលត្រូវមើល

- **គូសំណើ/ចម្លើយ**: ឲ្យចំណាំថា `→` មួយទៀតត្រូវមាន `←` ត្រូវគ្នា
- **សារ​កំហុស**: ស្វែងរក `"error"` នៅក្នុងចម្លើយ
- **ពេលវេលា**: កន្លែងរំកិលធំអាចបង្ហាញបញ្ហាការងារ
- **កំណត់ Protocol**: ប្រាកដថាម៉ាស៊ីនមេ និងអ្នកប្រើព្រមព្រៀងលើកំណែ

---

## ការរួមបញ្ចូល VS Code

អ្នកអាចដំណើរការ Inspector ពីផ្ទាល់ក្នុង VS Code:

### ប្រើ launch.json

បញ្ចូលទៅ `.vscode/launch.json`៖

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

### ប្រើការងារ (Tasks)

បញ្ចូលទៅ `.vscode/tasks.json`៖

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

## ស្ថានភាព debugging ទូទៅ

### ស្ថានភាពទី 1៖ ម៉ាស៊ីនមេទាក់ទងមិនបាន

**រោគសញ្ញា:** Inspector បង្ហាញ "Disconnected" ឬចាប់តភ្ជាប់ "Connecting..." ហើយអត់ចេញ

**បញ្ជីត្រួតពិនិត្យ៖**
1. ✅ ពិនិត្យមើលសន្ទស្សន៍បញ្ជាម៉ាស៊ីនមេត្រឹមត្រូវទេ
2. ✅ ពិនិត្យមើលថា dependencies ទាំងអស់បានដំឡើងហើយ
3. ✅ គន្លងទៅម៉ាស៊ីនមេជាកន្លែងត្រឹមត្រូវ ឬ​ស្ថិត​នៅ​ក្នុង​ថត​បច្ចុប្បន្ន​ទេ
4. ✅ បរិស្ថានដែលត្រូវបានកំណត់បានត្រឹមត្រូវ

**ជំហាន_debug:**
```bash
# សាកល្បងម៉ាស៊ីនបម្រើដោយដៃដំបូង
python -c "import your_server_module; print('OK')"

# ពិនិត្យមើលមានកំហុសនាំចូលឬអត់
python -m your_server_module 2>&1 | head -20

# ធ្វើការត្រួតពិនិត្យថា MCP SDK ត្រូវបានដំឡើងរួចហើយ
pip show mcp
```

### ស្ថានភាពទី 2៖ ឧបករណ៍មិនបង្ហាញ

**រោគសញ្ញា:** ផ្ទាំង Tools បង្ហាញបញ្ជីទទេ

**ហេតុអាចមាន៖**
1. ឧបករណ៍មិនបានចុះបញ្ជីពេលចាប់ផ្តើមម៉ាស៊ីនមេ
2. ម៉ាស៊ីនមេរងរវល់បរាជ័យបន្ទាប់ពីចាប់ផ្តើម
3. អ្នកដំណើរការនៃ `tools/list` បង្ហាញបញ្ជីទទេ

**ជំហាន_debug:**
1. ពិនិត្យកំណត់ហេតុសារសម្រាប់ចម្លើយ `tools/list`
2. បន្ថែមសារ​បរិច្ឆេទ​ក្នុង​កូដ​ចុះបញ្ជីឧបករណ៍របស់អ្នក
3. ពិនិត្យថា `@mcp.tool()` ត្រូវបានដាក់ចូល (សម្រាប់ Python)

### ស្ថានភាពទី 3៖ ឧបករណ៍បង្ហាញកំហុស

**រោគសញ្ញា:** ការហៅឧបករណ៍បង្ហាញចម្លើយកំហុស

**វិធីសាស្ត្រដោះស្រាយ៖**
1. អានសារកំហុសយ៉ាងម៉ត់ចត់
2. ត្រួតពិនិត្យប្រភេទប៉ារ៉ាម៉ែត្រឱ្យត្រូវគ្នានឹងគំរូ
3. បន្ថែមកូដ try/catch សម្រាប់សារកំហុសលម្អិត
4. ពិនិត្យកំណត់ហេតុម៉ាស៊ីនមេទៅកាន់កំណត់ហេតុវាយថ្មើរលំអិត

**ឧទាហរណ៍៖ ការកែលម្អការដោះស្រាយកំហុស៖**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # យោបល់​ឧបករណ៍​នៅទីនេះ
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### ស្ថានភាពទី 4៖ ខ្លឹមសារធនធានទទេ

**រោគសញ្ញា:** មាតិកាធនធានចេញមក ប៉ុន្តែមិនមានខ្លឹមសារ ឬ null

**បញ្ជីត្រួតពិនិត្យ៖**
1. ✅ ត្រួតពិនិត្យគន្លងឯកសារ ឫ URI ត្រឹមត្រូវ
2. ✅ ម៉ាស៊ីនមេមានសិទិ្ធអានធនធាន
3. ✅ មាតិកាធនធានត្រូវបានផ្តល់ត្រឹមត្រូវ

---

## លក្ខណៈពិសេស Inspector ឆ្នៃប្រាក់

### ចំណងជើងប្ដូរ (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### កំណត់ហេតុបង្ហាញលម្អិត

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### កំណត់សម័យកំណត់ហេតុ

Inspector អាចបញ្ចេញកំណត់ហេតុសារទៅឲ្យអ្នកវិភាគក្រោយ៖
1. ចុច **Export Log** នៅផ្ទាំងសារ
2. រក្សាទុកឯកសារ JSON
3. ចែករំលែកជាមួយសមាជិកក្រុមសម្រាប់ការដោះស្រាយកំហុស

---

## ផ្នែកហាត់ប្រាណល្អបំផុត

1. **ធ្វើតេស្តមុននឹងច្រើន** - ប្រើ Inspector ក្នុងដំណើរការអភិវឌ្ឍ មិនមែនតែពេលមានបញ្ហា
2. **ចាប់ផ្តើមដោយសាមញ្ញ** - ពិនិត្យការតភ្ជាប់មូលដ្ឋាន មុនហៅឧបករណ៍ស្មុគស្មាញ
3. **ពិនិត្យគំរូ** - កំហុសភាគច្រើនចេញពីប្រភេទប៉ារ៉ាម៉ែត្រមិនត្រឹមត្រូវ
4. **អានសារ​កំហុស** - កំហុស MCP ភាគច្រើនមានការពន្យល់លម្អិត
5. **រក្សា Inspector ឲ្យបើក** - វាជួយរកឃើញបញ្ហាពេលអ្នកបង្កើត

---

## តើបន្ទាប់មានអ្វី?

អ្នកបានបញ្ចប់ Module 3: Getting Started! សូមបន្តរៀនកម្រិតបន្ទាប់៖

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## ធនធានបន្ថែម

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើស្មាតហ្វូនបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងឲ្យបានភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងរបៀបនេះអាចមានកំហុសឬការមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមិត្តរបស់វាគួរត្រូវបានចាត់ទុកថាជាដើមទាំងស្រុង។ សម្រាប់ព័ត៌មានសំខាន់ៗ អនុសាសន៍ឲ្យប្រើការបកប្រែដោយមនុស្សជំនាញផ្នែកវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
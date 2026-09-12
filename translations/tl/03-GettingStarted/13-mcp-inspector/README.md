# Pag-debug gamit ang MCP Inspector

> [!NOTE]
> Ang mga utos na gumagamit ng `--sse` at mga URL na nagtatapos sa `/sse` ay sumusubok sa legacy HTTP+SSE
> transport. Para sa bagong MCP `2026-07-28` server, gamitin ang isang bersyon ng Inspector na
> sumusuporta sa Streamable HTTP at piliin ang transport na iyon sa halip.

Ang **MCP Inspector** ay isang mahalagang kasangkapan sa pag-debug na nagpapahintulot sa iyo na subukan at ayusin ang iyong mga MCP server nang interaktibo nang hindi kinakailangang magkaroon ng buong AI host application. Isipin ito bilang "Postman para sa MCP" - nagbibigay ito ng isang biswal na interface upang magpadala ng mga kahilingan, tingnan ang mga tugon, at maunawaan kung paano kumikilos ang iyong server.

## Bakit Gamitin ang MCP Inspector?

Kapag bumubuo ng mga MCP server, madalas mong mararanasan ang mga hamong ito:

- **"Tumutakba ba ang aking server?"** - Ipinapakita ng Inspector ang katayuan ng koneksyon
- **"Tama ba ang pagrehistro ng aking mga tool?"** - Ipinapakita ng Inspector ang lahat ng magagamit na mga tool
- **"Ano ang format ng tugon?"** - Ipinapakita ng Inspector ang buong mga tugon sa JSON
- **"Bakit hindi gumagana ang tool na ito?"** - Ipinapakita ng Inspector ang detalyadong mga mensahe ng error

## Mga Kinakailangan

- Nakainstall na Node.js 18+
- npm (kasama sa Node.js)
- Isang MCP server para subukan (tingnan ang [Module 3.1 - First Server](../01-first-server/README.md))

## Pag-install

### Opsyon 1: Patakbuhin gamit ang npx (Inirerekomenda para sa Mabilisang Pagsubok)

```bash
npx @modelcontextprotocol/inspector
```

### Opsyon 2: I-install Nang Global

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opsyon 3: Idagdag sa Iyong Proyekto

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Idagdag sa `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Pagkonekta sa Iyong Server

### stdio Servers (Lokal na Proseso)

Para sa mga server na nakikipagkomunika sa pamamagitan ng standard input/output:

```bash
# Server ng Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Server ng Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Gamit ang mga environment variable
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP Servers (Network)

Para sa mga server na tumatakbo bilang mga serbisyo ng HTTP:

1. Simulan muna ang iyong server:
   ```bash
   python server.py  # Server na tumatakbo sa http://localhost:8080
   ```

2. Ilunsad ang Inspector at kumonekta:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Pangkalahatang Tanaw ng Interface ng Inspector

Kapag inilunsad ang Inspector, makikita mo ang isang web interface (karaniwang nasa `http://localhost:5173`):

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

## Pagsubok ng mga Tool

### Paglisting ng Magagamit na Mga Tool

1. I-click ang tab na **Tools**
2. Awtomatikong tatawagin ng Inspector ang `tools/list`
3. Makikita mo ang lahat ng nakarehistrong tool na may:
   - Pangalan ng Tool
   - Paglalarawan
   - Input schema (mga parameter)

### Pagtawag sa isang Tool

1. Piliin ang isang tool mula sa listahan
2. Punan ang kinakailangang mga parameter sa form
3. I-click ang **Run Tool**
4. Tingnan ang tugon sa panel ng mga resulta

**Halimbawa: Pagsubok ng isang calculator tool**

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

### Pag-debug ng mga Error sa Tool

Kapag nabigo ang isang tool, ipinapakita ng Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Mga karaniwang code ng error:
| Code | Kahulugan |
|------|---------|
| -32700 | Parse error (hindi wastong JSON) |
| -32600 | Hindi wastong kahilingan |
| -32601 | Hindi nakita ang pamamaraan |
| -32602 | Hindi wastong mga parameter |
| -32603 | Panloob na error |

---

## Pagsubok ng Mga Mapagkukunan

### Paglisting ng Mga Mapagkukunan

1. I-click ang tab na **Resources**
2. Tatawagin ng Inspector ang `resources/list`
3. Makikita mo:
   - Mga URI ng Resource
   - Mga pangalan at paglalarawan
   - Mga MIME type

### Pagbasa ng isang Resource

1. Piliin ang isang resource
2. I-click ang **Read Resource**
3. Tingnan ang ibinalik na nilalaman

**Halimbawa ng output:**

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

## Pagsubok ng Mga Prompt

### Paglisting ng Mga Prompt

1. I-click ang tab na **Prompts**
2. Tatawagin ng Inspector ang `prompts/list`
3. Tingnan ang mga magagamit na template ng prompt

### Pagkuha ng Prompt

1. Piliin ang isang prompt
2. Punan ang anumang kinakailangang mga argumento
3. I-click ang **Get Prompt**
4. Tingnan ang na-render na mga mensahe ng prompt

---

## Pagsusuri ng Log ng Mensahe

Ipinapakita ng log ng mensahe ang lahat ng MCP protocol messages. Ang transcript sa ibaba ay mula sa
legacy `2025-11-25` server at kasama ang tinanggal na handshake na `initialize`. Ang isang
`2026-07-28` server ay gumagamit ng self-contained request metadata at `server/discover`
bilang kapalit.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Ano ang Titignan

- **Mga pares ng Request/Response**: Bawat `→` ay dapat may katumbas na `←`
- **Mga mensahe ng error**: Hanapin ang `"error"` sa mga tugon
- **Timing**: Malalaking agwat ay maaaring magpahiwatig ng mga isyu sa performance
- **Bersyon ng protocol**: Siguraduhin na nagkakasundo ang server at client sa bersyon

---

## Integrasyon sa VS Code

Maaari mong patakbuhin ang Inspector nang direkta mula sa VS Code:

### Paggamit ng launch.json

Idagdag sa `.vscode/launch.json`:

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

### Paggamit ng Mga Task

Idagdag sa `.vscode/tasks.json`:

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

## Karaniwang Mga Senaryo sa Pag-debug

### Senaryo 1: Hindi Kumokonekta ang Server

**Sintomas:** Ipinapakita ng Inspector ang "Disconnected" o naipit sa "Connecting..."

**Checklist:**
1. ✅ Tama ba ang utos ng server?
2. ✅ Nakainstall ba lahat ng dependencies?
3. ✅ Ang path ba ng server ay absolute o relative sa kasalukuyang direktoryo?
4. ✅ Nakaset ba ang mga kinakailangang environment variables?

**Mga hakbang sa pag-debug:**
```bash
# Manu-manong subukan muna ang server
python -c "import your_server_module; print('OK')"

# Suriin ang mga error sa pag-import
python -m your_server_module 2>&1 | head -20

# Tiyaking naka-install ang MCP SDK
pip show mcp
```

### Senaryo 2: Hindi Lumalabas ang Mga Tool

**Sintomas:** Walang laman ang listahan sa tab na Tools

**Mga posibleng dahilan:**
1. Hindi narehistro ang mga tool sa panahon ng initialization ng server
2. Nag-crash ang server pagkatapos ng startup
3. Ang `tools/list` handler ay nagbabalik ng walang laman na array

**Mga hakbang sa pag-debug:**
1. Suriin ang message log para sa tugon ng `tools/list`
2. Magdagdag ng logging sa iyong code para sa pagrehistro ng tool
3. Tiyaking naroroon ang `@mcp.tool()` decorators (Python)

### Senaryo 3: Nagbibigay ng Error ang Tool

**Sintomas:** Nagbabalik ang tawag sa tool ng tugon na may error

**Pamamaraan sa pag-debug:**
1. Basahin nang maigi ang mensahe ng error
2. Suriin kung nagtutugma ang mga uri ng parameter sa schema
3. Magdagdag ng try/catch na may detalyadong mga mensahe ng error
4. Suriin ang mga log ng server para sa stack traces

**Halimbawa ng pinahusay na paghawak ng error:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Lohika ng kasangkapan dito
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Senaryo 4: Walang Nilalaman ang Resource

**Sintomas:** Nagbabalik ang resource ngunit walang laman o null ang nilalaman

**Checklist:**
1. ✅ Tama ang path ng file o URI
2. ✅ May permiso ang server na basahin ang resource
3. ✅ Tama ang pagbalik ng nilalaman ng resource

---

## Mga Advanced na Tampok ng Inspector

### Custom na Mga Header (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Verbose Logging

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Pagre-record ng mga Session

Maaaring mag-export ang Inspector ng mga message log para sa susunod na pagsusuri:
1. I-click ang **Export Log** sa message panel
2. I-save ang JSON file
3. Ibahagi ito sa mga kasamahan para sa pag-debug

---

## Mga Pinakamahusay na Gawi

1. **Subukan ng maaga at madalas** - Gamitin ang Inspector habang nagde-develop, hindi lang kapag may sira
2. **Magsimula sa simple** - Subukan ang pangunahing koneksyon bago ang komplikadong mga tawag sa tool
3. **Suriin ang schema** - Maraming error ang nagmumula sa hindi pagtutugmang uri ng parameter
4. **Basahin ang mga mensahe ng error** - Karaniwan ay deskriptibo ang mga MCP error
5. **Panatilihing bukas ang Inspector** - Nakakatulong ito sa pag-amo ng mga isyu habang nagde-develop

---

## Ano ang Susunod

Natapos mo na ang Module 3: Pagsisimula! Ipagpatuloy ang iyong pag-aaral:

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## Karagdagang Mga Mapagkukunan

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
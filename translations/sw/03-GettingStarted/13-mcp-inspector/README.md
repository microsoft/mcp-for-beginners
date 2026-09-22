# Kurekebisha Hitilafu kwa MCP Inspector

> [!NOTE]
> Amri zinazotumia `--sse` na URL zinazomalizika kwa `/sse` hujaribu usafirishaji wa zamani wa HTTP+SSE.
> Kwa seva mpya ya MCP `2026-07-28`, tumia toleo la Inspector linalounga mkono HTTP Inayoweza Kutiririka na chagua usafirishaji huo badala yake.


**MCP Inspector** ni chombo muhimu cha kurekebisha hitilafu kinachokuwezesha kupima na kutatua matatizo ya seva zako za MCP kwa maingiliano bila hitaji la programu kamili ya mwenyeji AI. Fikiria kama "Postman kwa MCP" - kinatoa interface ya kuona kutuma maombi, kuona majibu, na kuelewa jinsi seva yako inavyotenda.

## Kwa Nini Utumie MCP Inspector?

Unapojenga seva za MCP, mara nyingi utakutana na changamoto hizi:

- **"Je, seva yangu inaendelea kufanya kazi?"** - Inspector inaonyesha hali ya muunganisho
- **"Je, zana zangu zimesajiliwa ipasavyo?"** - Inspector inaorodhesha zana zote zinazopatikana
- **"Ni muundo gani wa majibu?"** - Inspector inaonyesha majibu kamili ya JSON
- **"Kwanini chombo hiki hakifanyi kazi?"** - Inspector inaonyesha ujumbe wa makosa kwa undani

## Masharti

- Node.js 18+ imewekwa
- npm (huambatana na Node.js)
- Seva ya MCP ya kupima (angalia [Module 3.1 - Seva ya Kwanza](../01-first-server/README.md))

## Ufungaji

### Chaguo 1: Endesha kwa npx (Inapendekezwa kwa Upimaji wa Haraka)

```bash
npx @modelcontextprotocol/inspector
```

### Chaguo 2: Sakinisha Kwanza

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Chaguo 3: Ongeza Kwenye Mradi Wako

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Ongeza kwenye `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Kuunganisha na Seva Yako

### seva za stdio (Mchakato wa Ndani)

Kwa seva zinazowasiliana kupitia ingizo/totizo la kawaida:

```bash
# Seva ya Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Seva ya Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Kwa kutumia mabadiliko ya mazingira
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### seva za SSE/HTTP (Mtandao)

Kwa seva zinazofanya kazi kama huduma za HTTP:

1. Anzisha seva yako kwanza:
   ```bash
   python server.py  # Seva inafanya kazi kwenye http://localhost:8080
   ```

2. Anzisha Inspector na uungane:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Muhtasari wa Interface ya Inspector

Unapoanzisha Inspector, utaona interface ya wavuti (kwa kawaida kwenye `http://localhost:5173`):

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

## Kupima Zana

### Orodhesha Zana Zilizopo

1. Bonyeza kichupo cha **Zana**
2. Inspector huita moja kwa moja `tools/list`
3. Utaona zana zote zilizosajiliwa pamoja na:
   - Jina la chombo
   - Maelezo
   - Mfumo wa ingizo (vigezo)

### Kupiga Chombo

1. Chagua chombo kutoka kwenye orodha
2. Jaza vigezo vinavyohitajika kwenye fomu
3. Bonyeza **Endesha Chombo**
4. Angalia jibu kwenye paneli ya matokeo

**Mfano: Kupima chombo cha kalikuleta**

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

### Kurekebisha Makosa ya Zana

Ukishindwa, Inspector inaonyesha:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Msimbo wa makosa wa kawaida:
| Msimbo | Maana |
|------|---------|
| -32700 | Hitilafu ya tafsiri (JSON batili) |
| -32600 | Ombi batili |
| -32601 | Njia haipatikani |
| -32602 | Vigezo batili |
| -32603 | Hitilafu ya ndani |

---

## Kupima Rasilimali

### Orodhesha Rasilimali

1. Bonyeza kichupo cha **Rasilimali**
2. Inspector huita `resources/list`
3. Utaona:
   - URI za rasilimali
   - Majina na maelezo
   - Aina za MIME

### Kusoma Rasilimali

1. Chagua rasilimali
2. Bonyeza **Soma Rasilimali**
3. Angalia yaliyorejeshwa

**Matokeo ya mfano:**

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

## Kupima Maelekezo

### Orodhesha Maelekezo

1. Bonyeza kichupo cha **Maelekezo**
2. Inspector huita `prompts/list`
3. Angalia templeti za maelekezo zinazopatikana

### Kupata Maelekezo

1. Chagua maelekezo
2. Jaza vilivyoombwa vigezo
3. Bonyeza **Pata Maelekezo**
4. Ona ujumbe wa maelekezo yaliyotolewa

---

## Uchambuzi wa Rekodi za Ujumbe

Rekodi ya ujumbe inaonyesha ujumbe wote wa itifaki ya MCP. Mwisho wa mazungumzo hapo chini unatoka kwa
seva ya zamani ya `2025-11-25` na inaonyesha utambulisho wa 'initialize' uliotolewa. Seva ya
`2026-07-28` hutumia metadata ya maombi yenyewe na badala yake hutumia `server/discover`.


```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Kile Kinachopaswa Kutazamiwa

- **Jozi za Ombi/Majibu**: Kila `→` inapaswa kuwa na inayoambatana na `←`
- **Ujumbe wa makosa**: Tafuta `"error"` katika majibu
- **Muda**: Mapengo makubwa yanaweza kuashiria matatizo ya utendaji
- **Toleo la itifaki**: Hakikisha seva na mteja wanakubaliana juu ya toleo

---

## Kuunganishwa na VS Code

Unaweza kuendesha Inspector moja kwa moja kutoka VS Code:

### Kutumia launch.json

Ongeza kwenye `.vscode/launch.json`:

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

### Kutumia Tasks

Ongeza kwenye `.vscode/tasks.json`:

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

## Matukio ya Kawaida ya Kurekebisha Hitilafu

### Tukio 1: Seva Haikuunganishi

**Dalili:** Inspector inaonyesha "Imevunjika" au inashikilia kwenye "Inaunganishwa..."

**Orodha ya Kukagua:**
1. ✅ Je, amri ya seva ni sahihi?
2. ✅ Je, utegemezi wote umewekwa?
3. ✅ Njia ya seva ni kamili au ni jamaa na saraka ya sasa?
4. ✅ Je, mabadiliko ya mazingira yanayohitajika yamewekwa?

**Hatua za kurekebisha:**
```bash
# Jaribu seva kwa mkono kwanza
python -c "import your_server_module; print('OK')"

# Angalia kwa makosa ya kuingiza
python -m your_server_module 2>&1 | head -20

# Thibitisha MCP SDK imewekwa
pip show mcp
```

### Tukio 2: Zana Hazionekani

**Dalili:** Kichupo cha zana kinaonyesha orodha tupu

**Sababu zinazowezekana:**
1. Zana hazijasajiliwa wakati wa kuanzishwa kwa seva
2. Seva iliharibika baada ya kuanzishwa
3. Msimamizi wa `tools/list` anarudisha safu tupu

**Hatua za kurekebisha:**
1. Kagua rekodi ya ujumbe kwa jibu la `tools/list`
2. Ongeza kurekodi katika msajili wa zana zako
3. Thibitisha kuwa maandiko ya `@mcp.tool()` yapo (Python)

### Tukio 3: Chombo Kinarejesha Hitilafu

**Dalili:** Kuitwa kwa chombo kurudisha jibu la hitilafu

**Mbinu ya kurekebisha:**
1. Soma ujumbe wa makosa kwa makini
2. Angalia aina za vigezo zililingana na mfumo
3. Ongeza jaribu/shika na ujumbe wa makosa ya kina
4. Kagua rekodi za seva kwa taarifa za mfululizo wa makosa

**Mfano wa kuboresha utunzaji wa makosa:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Mantiki ya chombo hapa
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Tukio 4: Yaliyomo ya Rasilimali YEmpty

**Dalili:** Rasilimali inarudisha lakini yaliyomo ni tupu au ni sifuri

**Orodha ya Kukagua:**
1. ✅ Njia ya faili au URI ni sahihi
2. ✅ Seva ina ruhusa ya kusoma rasilimali
3. ✅ Maudhui ya rasilimali yanarudishwa ipasavyo

---

## Vipengele vya Juu vya Inspector

### Vichwa Maalum (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Uandikishaji wa kina (Verbose Logging)

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Kurekodi Vikao

Inspector inaweza kutoa rekodi za ujumbe kwa uchambuzi wa baadaye:
1. Bonyeza **Export Log** kwenye paneli ya ujumbe
2. Hifadhi faili la JSON
3. Shiriki na wanateam kwa ajili ya kurekebisha hitilafu

---


## Mazoezi Bora

1. **Jaribu mapema na mara kwa mara** - Tumia Inspector wakati wa maendeleo, si tu wakati vitu vinavunjika
2. **Anza kwa urahisi** - Jaribu muunganisho wa msingi kabla ya simu za zana ngumu
3. **Angalia schema** - Makosa mengi hutokea kutokana na kutofanana kwa aina za vigezo
4. **Soma ujumbe wa makosa** - Makosa ya MCP kawaida ni ya kueleweka
5. **Weka Inspector wazi** - Husaidia kugundua matatizo unapoendelea kuendeleza

---

## Nini Kifuatacho

Umeumaliza Moduli 3: Kuanzisha! Endelea na mafunzo yako:

- [Moduli 4: Utekelezaji wa Kivitendo](../../04-PracticalImplementation/README.md)

---

## Rasilimali Zaidi

- [Hazina ya MCP Inspector GitHub](https://github.com/modelcontextprotocol/inspector)
- [Ufafanuzi wa MCP - Ujumbe za Itifaki](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Ufafanuzi wa JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
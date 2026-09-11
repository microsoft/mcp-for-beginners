# Silumine MCP Inspectoriga

> [!NOTE]
> Käsklused, mis kasutavad `--sse` ja URL-id, mis lõpevad `/sse`, testivad pärandatud HTTP+SSE
> transporti. Uue MCP `2026-07-28` serveri puhul kasutage Inspector'i versiooni, mis
> toetab voogedastatavat HTTP-d ja valige selle asemel see transpordimeetod.

**MCP Inspector** on oluline silumistöökalu, mis võimaldab teil interaktiivselt testida ja veadiagnostikat teha oma MCP serveritel ilma täismahus AI hosti rakendust vajamata. Võrrelge seda kui „Postman MCP jaoks“ — see pakub visuaalset liidest päringute saatmiseks, vastuste vaatamiseks ja serveri käitumise mõistmiseks.

## Miks kasutada MCP Inspectorit?

MCP serverite loomisel puutute sageli kokku järgmiste väljakutsetega:

- **„Kas minu server üldse töötab?“** – Inspector kuvab ühenduse oleku
- **„Kas minu tööriistad on õigesti registreeritud?“** – Inspector loetleb kõik saadaval olevad tööriistad
- **„Mis on vastuse formaat?“** – Inspector näitab täielikke JSON-vastuseid
- **„Miks see tööriist ei tööta?“** – Inspector kuvab detailseid veateateid

## Eeldused

- Paigaldatud Node.js versioon 18 või uuem
- npm (tuleb koos Node.js-ga)
- Testimiseks MCP server (vt [Moodul 3.1 – Esimene server](../01-first-server/README.md))

## Paigaldus

### Valik 1: Käivita npx-iga (Soovitatav kiireks testimiseks)

```bash
npx @modelcontextprotocol/inspector
```

### Valik 2: Globaalne paigaldus

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Valik 3: Lisa oma projekti

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Lisa `package.json` faili:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Ühendamine oma serveriga

### stdio serverid (kohalik protsess)

Serverite puhul, mis suhtlevad standardse sisendi/väljundi kaudu:

```bash
# Python server
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js server
npx @modelcontextprotocol/inspector node ./build/index.js

# Keskkonnamuutujatega
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP serverid (võrk)

Serverite puhul, mis töötavad HTTP teenustena:

1. Käivitage esmalt oma server:
   ```bash
   python server.py  # Server töötab aadressil http://localhost:8080
   ```

2. Käivitage Inspector ja ühendage:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspectori liidese ülevaade

Inspector käivitamisel näete veebiliidest (tavaliselt aadressil `http://localhost:5173`):

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

## Tööriistade testimine

### Saadaval olevate tööriistade loetelu

1. Klõpsake **Tools** vahekaarti
2. Inspector kutsub automaatselt `tools/list`
3. Näete kõiki registreeritud tööriistu koos:
   - Tööriista nimedega
   - Kirjeldustega
   - Sissepääsu skeemiga (parameetrid)

### Tööriista kutsumine

1. Valige tööriist nimekirjast
2. Täitke vormis nõutud parameetrid
3. Klõpsake **Run Tool**
4. Vaadake vastust tulemuste paneelis

**Näide: Kalkulaatori tööriista testimine**

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

### Tööriista vigade silumine

Kui tööriist ebaõnnestub, kuvab Inspector:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Levinumad veakoodid:
| Kood | Tähendus |
|------|---------|
| -32700 | Parsimisviga (kehtetu JSON) |
| -32600 | Vigane päring |
| -32601 | Meetodit ei leitud |
| -32602 | Vigased parameetrid |
| -32603 | Sisemine tõrge |

---

## Ressursside testimine

### Ressursside loetelu

1. Klõpsake **Resources** vahekaarti
2. Inspector kutsub `resources/list`
3. Näete:
   - Ressursside URI-sid
   - Nimesid ja kirjeldusi
   - MIME tüüpe

### Ressursi lugemine

1. Valige ressurss
2. Klõpsake **Read Resource**
3. Vaadake tagastatud sisu

**Näite väljund:**

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

## Promptide testimine

### Promptide loetelu

1. Klõpsake **Prompts** vahekaarti
2. Inspector kutsub `prompts/list`
3. Vaadake saadaolevaid promptimalle

### Prompti hankimine

1. Valige prompt
2. Täitke vajadusel nõutud argumendid
3. Klõpsake **Get Prompt**
4. Vaadake renderdatud promptisõnumeid

---

## Sõnumilogide analüüs

Sõnumilogis kuvatakse kõik MCP protokollisõnumid. Allolev vestlus pärineb
pärandatud `2025-11-25` serverist ja sisaldab eemaldatud `initialize` käepigistust. 
`2026-07-28` server kasutab iseseisvat päringu metaandmeid ning `server/discover` kõnet
selle asemel.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Mida jälgida

- **Päringu/vastuse paarid**: Iga `→` peaks omama vastavat `←`
- **Veateated**: Otsige vastustest sõna `"error"`
- **Ajastus**: Suured pausid võivad viidata jõudlusprobleemidele
- **Protokolli versioon**: Veenduge, et server ja klient on versioonis ühel meelel

---

## VS Code integratsioon

Võite Inspectori käivitada otse VS Code'st:

### launch.json kasutamine

Lisage `.vscode/launch.json`:

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

### Tasks kasutamine

Lisage `.vscode/tasks.json`:

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

## Levinumad silumissituatsioonid

### Situatsioon 1: Server ei ühendu

**Sümptomid:** Inspector kuvab "Disconnected" või jääb seisma "Connecting..." peal

**Kontrollnimekiri:**
1. ✅ Kas serveri käsk on õige?
2. ✅ Kas kõik sõltuvused on paigaldatud?
3. ✅ Kas serveri rada on absoluutne või suhteline jooksvale kataloogile?
4. ✅ Kas vajalikud keskkonnamuutujad on seatud?

**Silumissammud:**
```bash
# Testi serverit esmalt käsitsi
python -c "import your_server_module; print('OK')"

# Kontrolli importimise vigu
python -m your_server_module 2>&1 | head -20

# Kinnita, et MCP SDK on paigaldatud
pip show mcp
```

### Situatsioon 2: Tööriistad ei ilmu

**Sümptomid:** Tööriistade vahekaart kuvab tühja nimekirja

**Võimalikud põhjused:**
1. Tööriistu ei registreeritud serveri käivitamisel
2. Server kukkus pärast käivitamist kokku
3. `tools/list` käsitsemisfunktsioon tagastab tühja massiivi

**Silumissammud:**
1. Kontrollige sõnumilogist `tools/list` vastust
2. Lisage oma tööriista registreerimiskoodi logimine
3. Veenduge, et `@mcp.tool()` dekoratsioonid on olemas (Python)

### Situatsioon 3: Tööriist tagastab vea

**Sümptomid:** Tööriista kutsumine tagastab veavastuse

**Silumisviis:**
1. Lugege veateadet hoolikalt
2. Kontrollige, et parameetritüüp vastab skeemile
3. Lisage katse/bloki lõks üksikasjalike veateadetega
4. Kontrollige serveri logisid peenekohtade leidmiseks

**Näide parendatud veakäsitlusest:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tööriista loogika siin
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Situatsioon 4: Ressursi sisu tühi

**Sümptomid:** Ressurss tagastab, kuid sisu on tühi või null

**Kontrollnimekiri:**
1. ✅ Failitee või URI on õige
2. ✅ Serveril on õigus ressurssi lugeda
3. ✅ Ressursi sisu tagastatakse korrektselt

---

## Täiustatud Inspectori omadused

### Kohandatud päised (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Üksikasjalik logimine

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Sessioonide salvestamine

Inspector võimaldab eksportida sõnumiloge hilisemaks analüüsiks:
1. Klõpsake sõnumipaneelil **Export Log**
2. Salvestage JSON-fail
3. Jagage meeskonnaliikmetega vigade analüüsimiseks

---

## Parimad praktikad

1. **Testige vara ja tihti** – Kasutage Inspectorit arenduse käigus, mitte ainult vigade ilmnemisel
2. **Alustage lihtsast** – Testige esmalt põhikonnektiivsust enne keerukate tööriistade kutsumist
3. **Kontrollige skeemi** – Paljud vead tulenevad parameetritüüpide mittevastavusest
4. **Lugege veateateid** – MCP vead on enamasti kirjeldavad
5. **Hoidke Inspector avatud** – See aitab vigasid varakult märgata arengu ajal

---

## Mis järgmiseks

Olete lõpetanud Mooduli 3: Alustamine! Jätkake õppimist:

- [Moodul 4: Praktiline rakendamine](../../04-PracticalImplementation/README.md)

---

## Täiendavad ressursid

- [MCP Inspectori GitHub hoidla](https://github.com/modelcontextprotocol/inspector)
- [MCP spetsifikatsioon – protokollisõnumid](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 spetsifikatsioon](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
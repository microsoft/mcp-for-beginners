# Derinimas su MCP Inspector

> [!NOTE]
> Komandos naudojant `--sse` ir URL, kurie baigiasi `/sse`, tikrina senąjį HTTP+SSE
> transportą. Naujam MCP `2026-07-28` serveriui naudokite Inspector versiją, kuri
> palaiko Streamable HTTP, ir pasirinkite tą transportą.

**MCP Inspector** yra svarbi derinimo priemonė, leidžianti interaktyviai testuoti ir spręsti problemas savo MCP serveriuose be pilnos AI host aplikacijos poreikio. Galvokite apie tai kaip „Postman MCP“ – jis suteikia vizualią sąsają užklausoms siųsti, atsakymams peržiūrėti ir suprasti, kaip veikia jūsų serveris.

## Kodėl naudoti MCP Inspector?

Kuriant MCP serverius, dažnai susiduriate su šiais iššūkiais:

- **„Ar mano serveris išvis veikia?“** – Inspector rodo prisijungimo būseną
- **„Ar mano įrankiai teisingai užregistruoti?“** – Inspector pateikia visų įrankių sąrašą
- **„Koks atsakymo formatas?“** – Inspector rodo pilnus JSON atsakymus
- **„Kodėl šis įrankis neveikia?“** – Inspector parodo išsamius klaidų pranešimus

## Reikalavimai

- Įdiegta Node.js 18 ar naujesnė versija
- npm (įeina į Node.js paketą)
- MCP serveris testavimui (žr. [3.1 modulis – Pirmasis serveris](../01-first-server/README.md))

## Įdiegimas

### Parinktis 1: Paleisti su npx (Rekomenduojama greitam testavimui)

```bash
npx @modelcontextprotocol/inspector
```

### Parinktis 2: Įdiegti globaliai

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Parinktis 3: Įtraukti į savo projektą

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Pridėkite į `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Prisijungimas prie jūsų serverio

### stdio serveriai (vietinis procesas)

Serveriams, kurie komunikuoja per standartinę įvestį/išvestį:

```bash
# Python serveris
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js serveris
npx @modelcontextprotocol/inspector node ./build/index.js

# Su aplinkos kintamaisiais
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP serveriai (tinklas)

Serveriams, veikiančiam kaip HTTP paslaugos:

1. Pirmiausia paleiskite savo serverį:
   ```bash
   python server.py  # Serveris veikia adresu http://localhost:8080
   ```

2. Paleiskite Inspector ir prisijunkite:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector sąsajos apžvalga

Paleidus Inspector, matysite žiniatinklio sąsają (dažniausiai adresu `http://localhost:5173`):

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

## Įrankių testavimas

### Pasiekiamų įrankių sąrašas

1. Spustelėkite skirtuką **Tools**
2. Inspector automatiškai iškviečia `tools/list`
3. Matysite visus užregistruotus įrankius su:
   - Įrankio pavadinimu
   - Aprašymu
   - Įvesties schema (parametrais)

### Įrankio kvietimas

1. Pasirinkite įrankį iš sąrašo
2. Užpildykite reikalingus parametrus formoje
3. Spustelėkite **Run Tool**
4. Žiūrėkite atsakymą rezultatų skydelyje

**Pavyzdys: skaičiuoklio įrankio testavimas**

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

### Įrankių klaidų derinimas

Kai įrankis sugenda, Inspector rodo:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Dažniausios klaidų kodų reikšmės:
| Kodas | Reikšmė |
|------|----------|
| -32700 | Analizės klaida (neteisingas JSON) |
| -32600 | Neteisinga užklausa |
| -32601 | Metodas nerastas |
| -32602 | Neteisingi parametrai |
| -32603 | Vidinė klaida |

---

## Išteklių testavimas

### Išteklių sąrašo peržiūra

1. Spustelėkite skirtuką **Resources**
2. Inspector iškviečia `resources/list`
3. Matysite:
   - Išteklių URI
   - Pavadinimus ir aprašymus
   - MIME tipus

### Išteklių skaitymas

1. Pasirinkite išteklių
2. Spustelėkite **Read Resource**
3. Peržiūrėkite grąžinamą turinį

**Pavyzdinis išvesties pavyzdys:**

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

## Prompts testavimas

### Prompts sąrašo peržiūra

1. Spustelėkite skirtuką **Prompts**
2. Inspector iškviečia `prompts/list`
3. Peržiūrėkite prieinamus promptų šablonus

### Gauti promptą

1. Pasirinkite promptą
2. Užpildykite visus būtinus argumentus
3. Spustelėkite **Get Prompt**
4. Peržiūrėkite sugeneruotus promptų pranešimus

---

## Pranešimų žurnalo analizė

Pranešimų žurnalas rodo visas MCP protokolo žinutes. Žemiau pateikiama transkripcija iš
seno `2025-11-25` serverio, įskaitant pašalintą `initialize` rankos paspaudimą. Naujas
`2026-07-28` serveris naudoja savarankiškus užklausos metaduomenis ir vietoj to
`server/discover`.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Į ką atkreipti dėmesį

- **Užklausos/atsakymai porose**: Kiekvienam `→` turi atitikti `←`
- **Klaidų pranešimai**: Ieškokite `"error"` atsakymuose
- **Laiko intervalai**: Didelės pauzės gali rodyti veikimo problemas
- **Protokolo versija**: Įsitikinkite, kad serveris ir klientas sutaria versiją

---

## VS Code integracija

Inspector galite tiesiogiai paleisti iš VS Code:

### Naudojant launch.json

Pridėkite į `.vscode/launch.json`:

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

### Naudojant Tasks

Pridėkite į `.vscode/tasks.json`:

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

## Įprastos derinimo situacijos

### Situacija 1: Serveris neprisijungia

**Simptomai:** Inspector rodo „Disconnected“ arba užstringa prie „Connecting...“

**Kontrolinis sąrašas:**
1. ✅ Ar teisinga serverio komanda?
2. ✅ Ar įdiegtos visos priklausomybės?
3. ✅ Ar serverio kelias yra absoliutus ar santykinis esamai direktorijai?
4. ✅ Ar nustatyti reikalingi aplinkos kintamieji?

**Derinimo žingsniai:**
```bash
# Išbandykite serverį rankiniu būdu pirmiausia
python -c "import your_server_module; print('OK')"

# Patikrinkite, ar nėra importavimo klaidų
python -m your_server_module 2>&1 | head -20

# Patvirtinkite, kad MCP SDK yra įdiegtas
pip show mcp
```

### Situacija 2: Įrankiai nepasiekiami

**Simptomai:** Tools skirtuke rodomas tuščias sąrašas

**Galimos priežastys:**
1. Įrankiai neužregistruoti serverio inicializavimo metu
2. Serveris sugriuvo po paleidimo
3. `tools/list` tvarkyklė grąžina tuščią masyvą

**Derinimo žingsniai:**
1. Patikrinkite žinutės žurnalą dėl `tools/list` atsakymo
2. Įjunkite žurnalavimą įrankių registravimo kode
3. Patikrinkite, ar yra `@mcp.tool()` dekoratoriai (Python)

### Situacija 3: Įrankis grąžina klaidą

**Simptomai:** Įrankio kvietimas grąžina klaidos atsakymą

**Derinimo būdas:**
1. Atidžiai perskaitykite klaidos pranešimą
2. Patikrinkite, ar parametro tipai atitinka schemą
3. Pridėkite try/catch blokus su išsamesniais klaidų pranešimais
4. Patikrinkite serverio žurnalus dėl klaidų sekų

**Pavyzdys kaip patobulinti klaidų valdymą:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Įrankio logika čia
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Situacija 4: Išteklių turinys tuščias

**Simptomai:** Išteklius grąžinamas, bet turinys tuščias arba null

**Kontrolinis sąrašas:**
1. ✅ Ar failo kelias arba URI yra teisingas
2. ✅ Ar serveris turi leidimą skaityti išteklių
3. ✅ Ar ištekliaus turinys teisingai grąžinamas

---

## Išplėstiniai Inspector funkcionalumai

### Pasirinktini antraštiniai duomenys (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Detalus žurnalavimas

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Sesijų įrašymas

Inspector gali eksportuoti žinučių žurnalus vėlesnei analizei:
1. Spustelėkite **Export Log** pranešimų skydelyje
2. Išsaugokite JSON failą
3. Pasidalinkite su komandos nariais derinimui

---


## Geriausios praktikos

1. **Testuokite anksti ir dažnai** - Naudokite Inspector kūrimo metu, ne tik kai kažkas sugenda
2. **Pradėkite nuo paprasto** - Išbandykite pagrindinį ryšį prieš sudėtingus įrankių kvietimus
3. **Patikrinkite schemą** - Daug klaidų kyla dėl parametrų tipų neatitikimų
4. **Skaitykite klaidų pranešimus** - MCP klaidos paprastai yra aprašomos
5. **Laikykite Inspector atidarytą** - Tai padeda pastebėti problemas vystymosi metu

---

## Kas toliau

Baigėte 3 modulį: Pradžia! Tęskite mokymąsi:

- [4 modulis: Praktinė įgyvendinimas](../../04-PracticalImplementation/README.md)

---

## Papildomi ištekliai

- [MCP Inspector GitHub saugykla](https://github.com/modelcontextprotocol/inspector)
- [MCP specifikacija - protokolo žinutės](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 specifikacija](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
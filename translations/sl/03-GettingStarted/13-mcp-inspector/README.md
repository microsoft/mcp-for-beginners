# Odpravljanje napak z MCP Inspector

> [!NOTE]
> Ukazi z uporabo `--sse` in URL-ji, ki se končajo z `/sse`, testirajo zastareli HTTP+SSE
> transport. Za nov MCP strežnik `2026-07-28` uporabite različico Inspectorja, ki
> podpira Streamable HTTP in izberite ta transport.

**MCP Inspector** je bistveno orodje za odpravljanje napak, ki vam omogoča interaktivno testiranje in odpravljanje težav z vašimi MCP strežniki brez potrebe po celotni AI gostiteljski aplikaciji. Lahko si ga predstavljate kot "Postman za MCP" - nudi vizualni vmesnik za pošiljanje zahtevkov, ogled odgovorov in razumevanje delovanja vašega strežnika.

## Zakaj uporabljati MCP Inspector?

Pri ustvarjanju MCP strežnikov se pogosto srečate s temi izzivi:

- **"Ali moj strežnik sploh deluje?"** - Inspector prikazuje stanje povezave
- **"So moji tooli pravilno registrirani?"** - Inspector navaja vse razpoložljive toole
- **"Kakšen je format odgovora?"** - Inspector prikazuje celoten JSON odgovor
- **"Zakaj ta tool ne deluje?"** - Inspector prikazuje podrobna sporočila o napakah

## Predpogoji

- Nameščen Node.js 18+
- npm (prisoten z Node.js)
- MCP strežnik za testiranje (glej [Modul 3.1 - Prvi strežnik](../01-first-server/README.md))

## Namestitev

### Možnost 1: Zagon z npx (Priporočeno za hitro testiranje)

```bash
npx @modelcontextprotocol/inspector
```

### Možnost 2: Globalna namestitev

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Možnost 3: Dodaj v svoj projekt

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Dodaj v `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Povezava na vaš strežnik

### stdio strežniki (lokalni proces)

Za strežnike, ki komunicirajo preko standardnega vhoda/izhoda:

```bash
# Python strežnik
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js strežnik
npx @modelcontextprotocol/inspector node ./build/index.js

# Z okoljskimi spremenljivkami
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP strežniki (omrežni)

Za strežnike, ki delujejo kot HTTP storitve:

1. Najprej zaženite svoj strežnik:
   ```bash
   python server.py  # Strežnik teče na http://localhost:8080
   ```

2. Zaženite Inspector in se povežite:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Pregled vmesnika Inspectorja

Ko zaženete Inspector, videli boste spletni vmesnik (navadno na `http://localhost:5173`):

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

## Testiranje toolov

### Prikaz razpoložljivih toolov

1. Kliknite na zavihek **Tools**
2. Inspector samodejno kliče `tools/list`
3. Videli boste vse registrirane toole z:
   - Imenom toola
   - Opisom
   - Vhodno shemo (parametre)

### Klic toola

1. Izberite tool s seznama
2. Izpolnite zahtevane parametre v obrazcu
3. Kliknite **Run Tool**
4. Oglejte si odgovor v panelu rezultatov

**Primer: Testiranje orodja kalkulator**

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

### Odpravljanje napak toolov

Ko tool odpove, Inspector prikaže:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Pogoste kode napak:
| Koda | Pomen |
|------|---------|
| -32700 | Napaka pri parsiranju (neveljaven JSON) |
| -32600 | Neveljavna zahteva |
| -32601 | Metoda ni najdena |
| -32602 | Neveljavni parametri |
| -32603 | Notranja napaka |

---

## Testiranje virov

### Prikaz virov

1. Kliknite na zavihek **Resources**
2. Inspector kliče `resources/list`
3. Videli boste:
   - URI-je virov
   - Imena in opise
   - MIME tipe

### Branje vira

1. Izberite vir
2. Kliknite **Read Resource**
3. Oglejte si vrnjeno vsebino

**Primer izpisa:**

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

## Testiranje pozivov

### Prikaz pozivov

1. Kliknite na zavihek **Prompts**
2. Inspector kliče `prompts/list`
3. Oglejte si razpoložljive predloge pozivov

### Pridobitev poziva

1. Izberite poziv
2. Izpolnite potrebne argumente
3. Kliknite **Get Prompt**
4. Oglejte si prikazane sporočila poziva

---

## Analiza dnevnika sporočil

Dnevnik sporočil prikazuje vsa sporočila MCP protokola. Spodnji prepis je iz
zastarelega strežnika `2025-11-25`, ki vključuje odstranjen rokovalni `initialize`. Strežnik
`2026-07-28` uporablja samostojno metapodatke zahtev in `server/discover`
namesto tega.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Na kaj paziti

- **Povratne pare zahteva/odgovor**: Vsak `→` naj ima ustrezen `←`
- **Sporočila o napakah**: Iščite `"error"` v odgovorih
- **Časovne zamike**: Veliki premori lahko nakazujejo težave s performansom
- **Različica protokola**: Preverite, da se strežnik in odjemalec strinjata glede različice

---

## Integracija z VS Code

Inspector lahko zaženete neposredno iz VS Code:

### Uporaba launch.json

Dodajte v `.vscode/launch.json`:

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

### Uporaba Tasks

Dodajte v `.vscode/tasks.json`:

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

## Pogosti primeri odpravljanja napak

### Primer 1: Strežnik se ne poveže

**Simptomi:** Inspector prikazuje "Disconnected" ali se zatakne pri "Connecting..."

**Kontrolni seznam:**
1. ✅ Je ukaz za strežnik pravilen?
2. ✅ So vsi odvisni moduli nameščeni?
3. ✅ Je pot do strežnika absolutna ali relativna glede na trenutno mapo?
4. ✅ So nastavljene potrebne okoljske spremenljivke?

**Koraki za odpravljanje:**
```bash
# Najprej ročno preizkusite strežnik
python -c "import your_server_module; print('OK')"

# Preverite napake pri uvozu
python -m your_server_module 2>&1 | head -20

# Preverite, ali je MCP SDK nameščen
pip show mcp
```

### Primer 2: Tooli se ne prikazujejo

**Simptomi:** Zavihek Tools prikazuje prazen seznam

**Možni vzroki:**
1. Tooli niso bili registrirani med inicializacijo strežnika
2. Strežnik se je sesul po zagonu
3. Obdelovalec `tools/list` vrača prazno tabelo

**Koraki za odpravljanje:**
1. Preverite dnevnik sporočil za odgovor `tools/list`
2. Dodajte beleženje v kodo za registracijo toolov
3. Preverite, ali so prisotni dekoratorji `@mcp.tool()` (Python)

### Primer 3: Tool vrne napako

**Simptomi:** Klic toola vrne napako v odgovoru

**Pristop k odpravljanju:**
1. Natančno preberite sporočilo o napaki
2. Preverite, da tipi parametrov ustrezajo shemi
3. Dodajte try/catch z detaljnimi sporočili o napakah
4. Preverite strežniške dnevnike za sledove skladov

**Primer izboljšanega ravnanja z napakami:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Tukaj je logika orodja
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Primer 4: Vsebina vira je prazna

**Simptomi:** Vir vrne, a vsebina je prazna ali ničelna

**Kontrolni seznam:**
1. ✅ Pot do datoteke ali URI je pravilen
2. ✅ Strežnik ima pravice za branje vira
3. ✅ Vsebina vira je pravilno vrnjena

---

## Napredne funkcije Inspectorja

### Prilagojeni glavi (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Podrobno beleženje

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Snemanje sej

Inspector lahko izvozi dnevnike sporočil za poznejšo analizo:
1. Kliknite **Export Log** v panelu sporočil
2. Shrani JSON datoteko
3. Delite s člani ekipe za odpravljanje napak

---

## Najboljše prakse

1. **Testirajte zgodaj in pogosto** - Uporabljajte Inspector med razvojem, ne samo, ko se kaj pokvari
2. **Začnite preprosto** - Preverite osnovno povezljivost pred kompleksnimi klici toolov
3. **Preverite shemo** - Veliko napak izvira iz neujemanja tipov parametrov
4. **Beri sporočila o napakah** - Napake MCP so navadno opisne
5. **Imejte Inspector odprt** - Pomaga ujeti težave med razvojem

---

## Kaj sledi

Zaključili ste Modul 3: Začetek! Nadaljujte z učenjem:

- [Modul 4: Praktična implementacija](../../04-PracticalImplementation/README.md)

---

## Dodatni viri

- [Repositorij MCP Inspector na GitHubu](https://github.com/modelcontextprotocol/inspector)
- [Specifikacija MCP - Protokolna sporočila](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 specifikacija](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
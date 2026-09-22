# Otklanjanje pogrešaka s MCP Inspektorom

> [!NOTE]
> Naredbe koje koriste `--sse` i URL-ovi koji završavaju na `/sse` testiraju naslijeđeni HTTP+SSE
> transport. Za novi MCP `2026-07-28` poslužitelj, koristite verziju Inspektora koja
> podržava Streamable HTTP i odaberite taj transport umjesto toga.

**MCP Inspektor** je nezaobilazan alat za otklanjanje pogrešaka koji vam omogućuje interaktivno testiranje i rješavanje problema vaših MCP poslužitelja bez potrebe za punom AI aplikacijom hosta. Zamislite ga kao "Postman za MCP" - pruža vizualno sučelje za slanje zahtjeva, pregled odgovora i razumijevanje ponašanja vašeg poslužitelja.

## Zašto koristiti MCP Inspektor?

Kada gradite MCP poslužitelje, često ćete naići na ove izazove:

- **"Radi li uopće moj poslužitelj?"** - Inspektor prikazuje status veze
- **"Jesu li moji alati pravilno registrirani?"** - Inspektor prikazuje sve dostupne alate
- **"Koji je format odgovora?"** - Inspektor prikazuje cijele JSON odgovore
- **"Zašto ovaj alat ne radi?"** - Inspektor prikazuje detaljne poruke o pogreškama

## Preduvjeti

- Node.js 18+ instaliran
- npm (dolazi s Node.js-om)
- MCP poslužitelj za testiranje (vidi [Modul 3.1 - Prvi poslužitelj](../01-first-server/README.md))

## Instalacija

### Opcija 1: Pokreni s npx (Preporučeno za brzo testiranje)

```bash
npx @modelcontextprotocol/inspector
```

### Opcija 2: Instaliraj globalno

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opcija 3: Dodaj u svoj projekt

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Dodaj u `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Povezivanje s vašim poslužiteljem

### stdio Poslužitelji (lokalni proces)

Za poslužitelje koji komuniciraju putem standardnog ulaza/izlaza:

```bash
# Python poslužitelj
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js poslužitelj
npx @modelcontextprotocol/inspector node ./build/index.js

# S varijablama okoline
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP poslužitelji (mrežni)

Za poslužitelje koji rade kao HTTP servisi:

1. Prvo pokrenite svoj poslužitelj:
   ```bash
   python server.py  # Poslužitelj radi na http://localhost:8080
   ```

2. Pokrenite Inspektor i povežite se:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Pregled sučelja Inspektora

Kada se Inspektor pokrene, vidjet ćete web sučelje (obično na `http://localhost:5173`):

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

## Testiranje alata

### Popis dostupnih alata

1. Kliknite karticu **Tools** (Alati)
2. Inspektor automatski poziva `tools/list`
3. Vidjet ćete sve registrirane alate s:
   - Naziv alata
   - Opis
   - Ulazna shema (parametri)

### Pozivanje alata

1. Odaberite alat s popisa
2. Ispunite potrebne parametre u obrascu
3. Kliknite **Run Tool** (Pokreni alat)
4. Pogledajte odgovor u panelu rezultata

**Primjer: Testiranje kalkulatora**

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

### Otklanjanje pogrešaka alata

Kad alat ne uspije, Inspektor prikazuje:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Uobičajeni kodovi pogrešaka:
| Kod | Značenje |
|------|---------|
| -32700 | Pogreška parsimiranja (neispravan JSON) |
| -32600 | Nevažeći zahtjev |
| -32601 | Metoda nije pronađena |
| -32602 | Nevažeći parametri |
| -32603 | Interna pogreška |

---

## Testiranje resursa

### Popis resursa

1. Kliknite karticu **Resources** (Resursi)
2. Inspektor poziva `resources/list`
3. Vidjet ćete:
   - URI-jeve resursa
   - Nazive i opise
   - MIME tipove

### Čitanje resursa

1. Odaberite resurs
2. Kliknite **Read Resource** (Pročitaj resurs)
3. Pogledajte vraćeni sadržaj

**Primjer izlaza:**

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

## Testiranje promptova

### Popis promptova

1. Kliknite karticu **Prompts** (Promptovi)
2. Inspektor poziva `prompts/list`
3. Pregledajte dostupne predloške promptova

### Dohvaćanje prompta

1. Odaberite prompt
2. Ispunite potrebne argumente
3. Kliknite **Get Prompt** (Dohvati prompt)
4. Pogledajte prikazane poruke prompta

---

## Analiza dnevnika poruka

Dnevnik poruka prikazuje sve MCP protokol poruke. Donji transkript je s
naslijeđenog `2025-11-25` poslužitelja i uključuje uklonjeni `initialize` handshake. 
`2026-07-28` poslužitelj koristi samostalne metapodatke zahtjeva i `server/discover`
umjesto toga.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Na što obratiti pažnju

- **Parovi zahtjev/odgovor**: Svaki `→` treba imati odgovarajući `←`
- **Poruke o pogrešci**: Potražite `"error"` u odgovorima
- **Vrijeme**: Veliki razmaci mogu ukazivati na probleme s izvedbom
- **Verzija protokola**: Provjerite slažu li se verzije poslužitelja i klijenta

---

## Integracija s VS Code-om

Inspektor možete pokrenuti izravno iz VS Code-a:

### Korištenje launch.json

Dodajte u `.vscode/launch.json`:

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

### Korištenje zadataka (Tasks)

Dodajte u `.vscode/tasks.json`:

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

## Uobičajeni scenariji otklanjanja pogrešaka

### Scenarij 1: Poslužitelj se ne povezuje

**Simptomi:** Inspektor pokazuje "Disconnected" ili se zaglavi na "Connecting..."

**Popis za provjeru:**
1. ✅ Je li naredba za poslužitelj ispravna?
2. ✅ Jesu li sve ovisnosti instalirane?
3. ✅ Je li put do poslužitelja apsolutan ili relativan u odnosu na trenutni direktorij?
4. ✅ Jesu li potrebne varijable okoline postavljene?

**Koraci za otklanjanje pogrešaka:**
```bash
# Prvo ručno testirajte poslužitelj
python -c "import your_server_module; print('OK')"

# Provjerite ima li pogrešaka pri uvozu
python -m your_server_module 2>&1 | head -20

# Provjerite je li MCP SDK instaliran
pip show mcp
```

### Scenarij 2: Alati se ne prikazuju

**Simptomi:** Kartica Alati prikazuje prazan popis

**Mogući uzroci:**
1. Alati nisu registrirani tijekom inicijalizacije poslužitelja
2. Poslužitelj se srušio nakon pokretanja
3. `tools/list` handler vraća prazni niz

**Koraci za otklanjanje pogrešaka:**
1. Provjerite dnevnik poruka za odgovor `tools/list`
2. Dodajte zapisivanje u kod registracije alata
3. Provjerite jesu li prisutni `@mcp.tool()` dekoratori (Python)

### Scenarij 3: Alat vraća pogrešku

**Simptomi:** Poziv alata vraća odgovor s pogreškom

**Pristup otklanjanju:**
1. Pažljivo pročitajte poruku o pogrešci
2. Provjerite slažu li se tipovi parametara s shemom
3. Dodajte try/catch s detaljnim porukama o pogrešci
4. Provjerite zapisnike poslužitelja za stack trace

**Primjer poboljšanog rukovanja pogreškama:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Logika alata ovdje
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Scenarij 4: Sadržaj resursa je prazan

**Simptomi:** Resurs se vraća, ali sadržaj je prazan ili null

**Popis za provjeru:**
1. ✅ Put do datoteke ili URI je točan
2. ✅ Poslužitelj ima dozvolu za čitanje resursa
3. ✅ Sadržaj resursa se pravilno vraća

---

## Napredne značajke Inspektora

### Prilagođeni zaglavlja (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Detaljno zapisivanje (verbose logging)

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Snimanje sesija

Inspektor može izvesti dnevnike poruka za kasniju analizu:
1. Kliknite **Export Log** u panelu poruka
2. Spremite JSON datoteku
3. Podijelite s članovima tima za otklanjanje pogrešaka

---

## Najbolje prakse

1. **Testirajte rano i često** - Koristite Inspektor tijekom razvoja, ne samo kad stvari zakažu
2. **Počnite jednostavno** - Testirajte osnovnu povezanost prije složenih poziva alata
3. **Provjerite shemu** - Mnoge pogreške dolaze od neslaganja tipova parametara
4. **Čitajte poruke o pogrešci** - MCP pogreške su obično opisne
5. **Držite Inspektor otvorenim** - Pomaže uhvatiti probleme tijekom razvoja

---

## Što je sljedeće

Završili ste Modul 3: Početak! Nastavite s učenjem:

- [Modul 4: Praktična implementacija](../../04-PracticalImplementation/README.md)

---

## Dodatni resursi

- [MCP Inspector GitHub repozitorij](https://github.com/modelcontextprotocol/inspector)
- [MCP specifikacija - protokol poruke](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 specifikacija](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
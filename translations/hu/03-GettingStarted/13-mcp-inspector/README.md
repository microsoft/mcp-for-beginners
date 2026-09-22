# Hibakeresés MCP Inspektorral

> [!NOTE]
> A `--sse` használatával és `/sse` végződésű URL-ekkel végzett parancsok a régi HTTP+SSE
> átvitelt tesztelik. Új, `2026-07-28` MCP szerverhez olyan Inspektor verziót használj,
> amely támogatja a Streamable HTTP-t, és válaszd azt az átvitelt.

A **MCP Inspektor** egy alapvető hibakereső eszköz, amely lehetővé teszi, hogy interaktívan teszteld és hibakeresd az MCP szervereidet teljes AI host alkalmazás nélkül. Gondolj rá úgy, mint egy „Postman az MCP-hez” - vizuális felületet ad, amellyel kéréseket küldhetsz, válaszokat nézhetsz meg, és megértheted, hogyan viselkedik a szervered.

## Miért használd az MCP Inspektort?

MCP szerverek építése közben gyakran találkozol ezekkel a kihívásokkal:

- **„Egyáltalán fut a szerverem?”** - Az Inspektor mutatja a kapcsolat állapotát
- **„Helyesen vannak regisztrálva az eszközeim?”** - Az Inspektor listázza az összes elérhető eszközt
- **„Milyen a válasz formátuma?”** - Az Inspektor megjeleníti a teljes JSON válaszokat
- **„Miért nem működik ez az eszköz?”** - Az Inspektor részletes hibaüzeneteket mutat

## Előfeltételek

- Telepített Node.js 18+ verzió
- npm (a Node.js-sel együtt érkezik)
- Tesztelendő MCP szerver (lásd [3.1. Modul - Első szerver](../01-first-server/README.md))

## Telepítés

### 1. lehetőség: futtatás npx-szel (Gyors teszteléshez ajánlott)

```bash
npx @modelcontextprotocol/inspector
```

### 2. lehetőség: Globális telepítés

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### 3. lehetőség: Projektbe való beillesztés

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Add hozzá a `package.json`-hoz:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Kapcsolódás a szerveredhez

### stdio szerverek (helyi folyamat)

Azoknál a szervereknél, amelyek szabványos bemeneten/kimeneten kommunikálnak:

```bash
# Python szerver
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js szerver
npx @modelcontextprotocol/inspector node ./build/index.js

# Környezeti változókkal
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP szerverek (hálózati)

Azoknál a szervereknél, amelyek HTTP szolgáltatásként futnak:

1. Először indítsd el a szervered:
   ```bash
   python server.py  # Szerver fut a http://localhost:8080 címen
   ```

2. Indítsd el az Inspektort és csatlakozz:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspektor felület áttekintése

Amikor az Inspektor elindul, egy webes felületet fogsz látni (általában a `http://localhost:5173` címen):

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

## Eszközök tesztelése

### Elérhető eszközök listázása

1. Kattints a **Tools** fülre
2. Az Inspektor automatikusan meghívja a `tools/list` parancsot
3. Megjelenik az összes regisztrált eszköz:
   - Eszköz neve
   - Leírás
   - Bemeneti séma (paraméterek)

### Egy eszköz meghívása

1. Válassz ki egy eszközt a listából
2. Töltsd ki a szükséges paramétereket az űrlapon
3. Kattints a **Run Tool** gombra
4. Nézd meg a választ az eredmény panelen

**Példa: Számológép eszköz tesztelése**

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

### Hibák hibakeresése eszközöknél

Ha egy eszköz hibát jelez, az Inspektor megmutatja:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Gyakori hibakódok:
| Kód | Jelentése |
|------|---------|
| -32700 | Elemzési hiba (érvénytelen JSON) |
| -32600 | Érvénytelen kérés |
| -32601 | Metódus nem található |
| -32602 | Érvénytelen paraméterek |
| -32603 | Belső hiba |

---

## Erőforrások tesztelése

### Erőforrások listázása

1. Kattints a **Resources** fülre
2. Az Inspektor meghívja a `resources/list` parancsot
3. Megjelenik:
   - Erőforrás URI-k
   - Nevek és leírások
   - MIME típusok

### Erőforrás olvasása

1. Válassz ki egy erőforrást
2. Kattints a **Read Resource** gombra
3. Nézd meg a visszakapott tartalmat

**Kimenet példa:**

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

## Promptok tesztelése

### Promptok listázása

1. Kattints a **Prompts** fülre
2. Az Inspektor meghívja a `prompts/list` parancsot
3. Nézd meg a rendelkezésre álló prompt sablonokat

### Prompt lekérése

1. Válassz ki egy promptot
2. Töltsd ki a szükséges argumentumokat
3. Kattints a **Get Prompt** gombra
4. Nézd meg a megjelenített prompt üzeneteket

---

## Üzenetnapló elemzés

Az üzenetnapló az összes MCP protokoll üzenetet mutatja. Az alábbi átírás egy
régi, `2025-11-25` szervertől származik és tartalmazza az eltávolított `initialize` kézfogást. Egy
`2026-07-28` szerver önálló kérés metaadatokat és a `server/discover`
metódust használ helyette.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### Mire figyelj

- **Kérés/válasz párok**: Minden `→` után kell lennie egy `←`-nek
- **Hibaüzenetek**: Figyeld a válaszokban a `"error"` üzeneteket
- **Időzítés**: Nagy időközök teljesítményproblémákra utalhatnak
- **Protokoll verzió**: Győződj meg róla, hogy a szerver és kliens ugyanazt a verziót használja

---

## VS Code integráció

Az Inspektort közvetlenül VS Code-ból is futtathatod:

### launch.json használata

Add hozzá a `.vscode/launch.json` fájlhoz:

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

### Taskok használata

Add hozzá a `.vscode/tasks.json` fájlhoz:

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

## Gyakori hibakeresési helyzetek

### Helyzet 1: Nem csatlakozik a szerver

**Tünetek:** Az Inspektor „Disconnected” üzenetet mutat vagy „Connecting...” állapotban ragad

**Ellenőrző lista:**
1. ✅ A szerver parancs helyes?
2. ✅ Minden függőség telepítve van?
3. ✅ A szerver útvonala abszolút vagy az aktuális könyvtárhoz viszonyított?
4. ✅ A szükséges környezeti változók be vannak állítva?

**Hibakeresési lépések:**
```bash
# Először kézzel teszteld a szervert
python -c "import your_server_module; print('OK')"

# Ellenőrizd az importálási hibákat
python -m your_server_module 2>&1 | head -20

# Győződj meg róla, hogy az MCP SDK telepítve van
pip show mcp
```

### Helyzet 2: Eszközök nem jelennek meg

**Tünetek:** Az Eszközök fül üres listát mutat

**Lehetséges okok:**
1. Az eszközök nincsenek regisztrálva a szerver inicializálásakor
2. A szerver összeomlott az indítás után
3. A `tools/list` kezelő üres tömböt ad vissza

**Hibakeresési lépések:**
1. Ellenőrizd az üzenetnaplót a `tools/list` válaszért
2. Adj hozzá naplózást az eszközregisztrációs kódodhoz
3. Ellenőrizd, hogy a `@mcp.tool()` dekorátorok jelen vannak-e (Python esetén)

### Helyzet 3: Eszköz hibát ad vissza

**Tünetek:** Az eszköz hívása hibás választ ad vissza

**Hibakeresési megközelítés:**
1. Olvasd el figyelmesen a hibaüzenetet
2. Ellenőrizd, hogy a paraméter típusok megfelelnek-e a sémának
3. Adj hozzá try/catch blokkot részletes hibaüzenetekkel
4. Nézd át a szerver naplókat stack trace-ek után kutatva

**Példa javított hibakezelésre:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Az eszköz logikája itt
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Helyzet 4: Az erőforrás tartalma üres

**Tünetek:** Az erőforrás válaszol, de a tartalom üres vagy null

**Ellenőrző lista:**
1. ✅ A fájl útvonala vagy URI helyes
2. ✅ A szervernek van jogosultsága az erőforrás olvasásához
3. ✅ Az erőforrás tartalma helyesen kerül visszaadásra

---

## Fejlett Inspektor funkciók

### Egyéni fejléc (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Részletes naplózás

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Munkamenetek rögzítése

Az Inspektor képes üzenetnaplókat exportálni későbbi elemzésre:
1. Kattints a **Export Log** gombra az üzenet panelen
2. Mentsd el a JSON fájlt
3. Oszd meg a csapattagokkal a hibakereséshez

---

## Legjobb gyakorlatok

1. **Tesztelj korán és gyakran** - Használd az Inspektort a fejlesztés során, ne csak hibák esetén
2. **Kezdd egyszerűen** - Először az alapvető kapcsolatot teszteld, mielőtt bonyolult eszközhívásokat végzel
3. **Ellenőrizd a sémát** - Sok hiba a paramétertípusok eltéréséből ered
4. **Olvasd el a hibaüzeneteket** - Az MCP hibái általában leíróak
5. **Tartsd nyitva az Inspektort** - Segít észrevenni a problémákat fejlesztés közben

---

## Mi a következő lépés?

Befejezted a 3. modult: Bevezetés! Folytasd a tanulást:

- [4. Modul: Gyakorlati megvalósítás](../../04-PracticalImplementation/README.md)

---

## További források

- [MCP Inspektor GitHub tárhely](https://github.com/modelcontextprotocol/inspector)
- [MCP Specifikáció - Protokoll üzenetek](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 specifikáció](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
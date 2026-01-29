# MCP stdio Server - Python Megoldás

> **⚠️ Fontos**: Ez a megoldás frissítve lett, hogy a **stdio transport**-ot használja, ahogyan azt az MCP 2025-06-18-as specifikációja ajánlja. Az eredeti SSE transport elavulttá vált.

## Áttekintés

Ez a Python megoldás bemutatja, hogyan lehet MCP szervert építeni a jelenlegi stdio transport használatával. A stdio transport egyszerűbb, biztonságosabb, és jobb teljesítményt nyújt, mint a már elavult SSE megközelítés.

## Előfeltételek

- Python 3.8 vagy újabb
- Ajánlott telepíteni az `uv` csomagkezelőt, lásd [útmutató](https://docs.astral.sh/uv/#highlights)

## Telepítési Útmutató

### 1. lépés: Hozz létre egy virtuális környezetet

```bash
python -m venv venv
```

### 2. lépés: Aktiváld a virtuális környezetet

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. lépés: Telepítsd a függőségeket

```bash
pip install mcp
```

## A szerver futtatása

A stdio szerver eltérően működik a régi SSE szervertől. Webszerver indítása helyett stdin/stdout-on keresztül kommunikál:

```bash
python server.py
```

**Fontos**: A szerver úgy tűnhet, mintha lefagyott volna - ez normális! A stdin-en keresztül érkező JSON-RPC üzenetekre vár.

## A szerver tesztelése

### 1. Módszer: MCP Inspector használata (Ajánlott)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Ez a következőket teszi:
1. Alfolyamatként elindítja a szervert
2. Megnyit egy webes felületet a teszteléshez
3. Lehetővé teszi az összes szervereszköz interaktív tesztelését

### 2. Módszer: Közvetlen JSON-RPC tesztelés

Közvetlenül is tesztelheted JSON-RPC üzenetek küldésével:

1. Indítsd el a szervert: `python server.py`
2. Küldj egy JSON-RPC üzenetet (példa):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. A szerver válaszol az elérhető eszközökkel

### Elérhető Eszközök

A szerver a következő eszközöket biztosítja:

- **add(a, b)**: Két szám összeadása
- **multiply(a, b)**: Két szám szorzása  
- **get_greeting(name)**: Személyre szabott üdvözlés generálása
- **get_server_info()**: Információk lekérése a szerverről

### Tesztelés Claude Desktop-pal

Ha ezt a szervert Claude Desktop-pal szeretnéd használni, add hozzá ezt a konfigurációt a `claude_desktop_config.json` fájlhoz:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Főbb Különbségek az SSE-hez képest

**stdio transport (Jelenlegi):**
- ✅ Egyszerűbb beállítás - nincs szükség webszerverre
- ✅ Jobb biztonság - nincsenek HTTP végpontok
- ✅ Alfolyamat-alapú kommunikáció
- ✅ JSON-RPC stdin/stdout-on keresztül
- ✅ Jobb teljesítmény

**SSE transport (Elavult):**
- ❌ Webszerver beállítása szükséges
- ❌ Webes keretrendszer (Starlette/FastAPI) szükséges
- ❌ Bonyolultabb útvonal- és munkamenetkezelés
- ❌ További biztonsági megfontolások
- ❌ Az MCP 2025-06-18-ban elavulttá vált

## Hibakeresési Tippek

- Használj `stderr`-t a naplózáshoz (soha ne `stdout`-ot)
- Tesztelj az Inspectorral a vizuális hibakereséshez
- Győződj meg róla, hogy minden JSON üzenet új sorral van elválasztva
- Ellenőrizd, hogy a szerver hibák nélkül indul-e

Ez a megoldás követi a jelenlegi MCP specifikációt, és bemutatja a stdio transport implementációjának legjobb gyakorlatait.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
# MCP stdio Server - TypeScript Megoldás

> **⚠️ Fontos**: Ez a megoldás frissítve lett, hogy a **stdio transport**-ot használja, ahogyan azt az MCP Specifikáció 2025-06-18 ajánlja. Az eredeti SSE transport elavult.

## Áttekintés

Ez a TypeScript megoldás bemutatja, hogyan lehet MCP szervert építeni a jelenlegi stdio transport használatával. A stdio transport egyszerűbb, biztonságosabb, és jobb teljesítményt nyújt, mint a korábban használt SSE megközelítés.

## Előfeltételek

- Node.js 18+ vagy újabb
- npm vagy yarn csomagkezelő

## Telepítési útmutató

### 1. lépés: Függőségek telepítése

```bash
npm install
```

### 2. lépés: Projekt felépítése

```bash
npm run build
```

## A szerver futtatása

A stdio szerver másképp működik, mint a régi SSE szerver. Webszerver indítása helyett stdin/stdout-on keresztül kommunikál:

```bash
npm start
```

**Fontos**: A szerver látszólag lefagy - ez normális! JSON-RPC üzenetekre vár stdin-en keresztül.

## A szerver tesztelése

### 1. módszer: MCP Inspector használata (Ajánlott)

```bash
npm run inspector
```

Ez a következőket teszi:
1. A szervert alfolyamatként indítja
2. Megnyit egy webes felületet teszteléshez
3. Lehetővé teszi az összes szerver eszköz interaktív tesztelését

### 2. módszer: Közvetlen parancssori tesztelés

A teszteléshez az Inspectort közvetlenül is elindíthatod:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Elérhető eszközök

A szerver az alábbi eszközöket biztosítja:

- **add(a, b)**: Két szám összeadása
- **multiply(a, b)**: Két szám szorzása  
- **get_greeting(name)**: Személyre szabott üdvözlés generálása
- **get_server_info()**: Információk lekérése a szerverről

### Tesztelés Claude Desktop segítségével

Ha ezt a szervert Claude Desktop-pal szeretnéd használni, add hozzá ezt a konfigurációt a `claude_desktop_config.json` fájlhoz:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Projekt struktúrája

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Fő különbségek az SSE-hez képest

**stdio transport (Jelenlegi):**
- ✅ Egyszerűbb beállítás - nincs szükség HTTP szerverre
- ✅ Jobb biztonság - nincs HTTP végpont
- ✅ Alfolyamat-alapú kommunikáció
- ✅ JSON-RPC stdin/stdout-on keresztül
- ✅ Jobb teljesítmény

**SSE transport (Elavult):**
- ❌ Express szerver beállítását igényelte
- ❌ Bonyolult útvonal- és munkamenet-kezelést igényelt
- ❌ Több függőség (Express, HTTP kezelés)
- ❌ További biztonsági megfontolások
- ❌ Az MCP 2025-06-18 szerint elavult

## Fejlesztési tippek

- Használj `console.error()`-t naplózáshoz (soha ne `console.log()`-ot, mivel az stdout-ra ír)
- Tesztelés előtt építsd fel a projektet `npm run build` paranccsal
- Tesztelj az Inspectorral vizuális hibakereséshez
- Győződj meg róla, hogy minden JSON üzenet megfelelően van formázva
- A szerver automatikusan kezeli a zökkenőmentes leállítást SIGINT/SIGTERM esetén

Ez a megoldás követi a jelenlegi MCP specifikációt, és bemutatja a stdio transport TypeScript alapú implementációjának legjobb gyakorlatait.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
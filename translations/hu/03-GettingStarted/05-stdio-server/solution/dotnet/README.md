# MCP stdio Szerver - .NET Megoldás

> **⚠️ Fontos**: Ez a megoldás frissítve lett, hogy a **stdio transzportot** használja, ahogy azt az MCP Specifikáció 2025-06-18 ajánlja. Az eredeti SSE transzport elavult.

## Áttekintés

Ez a .NET megoldás bemutatja, hogyan lehet MCP szervert építeni a jelenlegi stdio transzport használatával. A stdio transzport egyszerűbb, biztonságosabb, és jobb teljesítményt nyújt, mint a már elavult SSE megközelítés.

## Előfeltételek

- .NET 9.0 SDK vagy újabb
- Alapvető ismeretek a .NET függőséginjektálásról

## Telepítési Útmutató

### 1. lépés: Függőségek visszaállítása

```bash
dotnet restore
```

### 2. lépés: A projekt felépítése

```bash
dotnet build
```

## A szerver futtatása

A stdio szerver másképp működik, mint a régi HTTP-alapú szerver. Webszerver indítása helyett stdin/stdout-on keresztül kommunikál:

```bash
dotnet run
```

**Fontos**: A szerver úgy tűnhet, mintha lefagyna - ez normális! JSON-RPC üzenetekre vár stdin-en keresztül.

## A szerver tesztelése

### 1. módszer: MCP Inspector használata (Ajánlott)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ez a következőket teszi:
1. Alfolyamatként indítja el a szervert
2. Megnyit egy webes felületet a teszteléshez
3. Lehetővé teszi az összes szervereszköz interaktív tesztelését

### 2. módszer: Közvetlen parancssori tesztelés

A teszteléshez közvetlenül is elindíthatja az Inspectort:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Elérhető Eszközök

A szerver a következő eszközöket biztosítja:

- **AddNumbers(a, b)**: Két szám összeadása
- **MultiplyNumbers(a, b)**: Két szám szorzása  
- **GetGreeting(name)**: Személyre szabott üdvözlés generálása
- **GetServerInfo()**: Információk lekérése a szerverről

### Tesztelés Claude Desktop-pal

A szerver használatához Claude Desktop-pal adja hozzá ezt a konfigurációt a `claude_desktop_config.json` fájlhoz:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Projektstruktúra

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Fő Különbségek a HTTP/SSE-hez képest

**stdio transzport (Jelenlegi):**
- ✅ Egyszerűbb beállítás - nincs szükség webszerverre
- ✅ Jobb biztonság - nincsenek HTTP végpontok
- ✅ `Host.CreateApplicationBuilder()` használata `WebApplication.CreateBuilder()` helyett
- ✅ `WithStdioTransport()` használata `WithHttpTransport()` helyett
- ✅ Konzolalkalmazás webszerver helyett
- ✅ Jobb teljesítmény

**HTTP/SSE transzport (Elavult):**
- ❌ ASP.NET Core webszerver szükséges
- ❌ `app.MapMcp()` útvonalbeállítás szükséges
- ❌ Bonyolultabb konfiguráció és függőségek
- ❌ További biztonsági megfontolások
- ❌ Az MCP 2025-06-18 szerint elavult

## Fejlesztési Funkciók

- **Függőséginjektálás**: Teljes DI támogatás szolgáltatásokhoz és naplózáshoz
- **Strukturált Naplózás**: Helyes naplózás stderr-re `ILogger<T>` használatával
- **Eszköz Attribútumok**: Tiszta eszközdefiníció `[McpServerTool]` attribútumokkal
- **Aszinkron Támogatás**: Minden eszköz támogatja az aszinkron műveleteket
- **Hibakezelés**: Kifinomult hibakezelés és naplózás

## Fejlesztési Tippek

- Használja az `ILogger`-t naplózáshoz (soha ne írjon közvetlenül stdout-ra)
- Építse a projektet `dotnet build` paranccsal tesztelés előtt
- Teszteljen az Inspectorral vizuális hibakereséshez
- Minden naplózás automatikusan stderr-re kerül
- A szerver kezeli a leállítási jeleket

Ez a megoldás követi a jelenlegi MCP specifikációt, és bemutatja a stdio transzport implementálásának legjobb gyakorlatait .NET környezetben.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
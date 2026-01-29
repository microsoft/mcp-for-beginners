# Teljes MCP kliens példák

Ez a könyvtár teljes, működő MCP kliens példákat tartalmaz különböző programozási nyelveken. Minden kliens bemutatja a fő README.md oktatóanyagban leírt teljes funkcionalitást.

## Elérhető kliensek

### 1. Java kliens (`client_example_java.java`)

- **Átvitel**: SSE (Server-Sent Events) HTTP-n keresztül
- **Cél szerver**: `http://localhost:8080`
- **Funkciók**:
  - Kapcsolat létrehozása és pingelés
  - Eszközök listázása
  - Kalkulátor műveletek (összeadás, kivonás, szorzás, osztás, súgó)
  - Hibakezelés és eredmény kinyerés

**Futtatáshoz:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# kliens (`client_example_csharp.cs`)

- **Átvitel**: Stdio (Standard Input/Output)
- **Cél szerver**: Helyi .NET MCP szerver dotnet run segítségével
- **Funkciók**:
  - Automatikus szerverindítás stdio átvitel segítségével
  - Eszközök és erőforrások listázása
  - Kalkulátor műveletek
  - JSON eredmény feldolgozás
  - Átfogó hibakezelés

**Futtatáshoz:**

```bash
dotnet run
```

### 3. TypeScript kliens (`client_example_typescript.ts`)

- **Átvitel**: Stdio (Standard Input/Output)
- **Cél szerver**: Helyi Node.js MCP szerver
- **Funkciók**:
  - Teljes MCP protokoll támogatás
  - Eszközök, erőforrások és prompt műveletek
  - Kalkulátor műveletek
  - Erőforrás olvasás és prompt végrehajtás
  - Robusztus hibakezelés

**Futtatáshoz:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python kliens (`client_example_python.py`)

- **Átvitel**: Stdio (Standard Input/Output)  
- **Cél szerver**: Helyi Python MCP szerver
- **Funkciók**:
  - Async/await minta a műveletekhez
  - Eszközök és erőforrások felfedezése
  - Kalkulátor műveletek tesztelése
  - Erőforrás tartalom olvasása
  - Osztály-alapú szervezés

**Futtatáshoz:**

```bash
python client_example_python.py
```

## Közös funkciók minden kliensben

Minden kliens implementáció bemutatja:

1. **Kapcsolatkezelés**
   - Kapcsolat létrehozása az MCP szerverrel
   - Kapcsolati hibák kezelése
   - Megfelelő takarítás és erőforrás-kezelés

2. **Szerver felfedezése**
   - Elérhető eszközök listázása
   - Elérhető erőforrások listázása (ha támogatott)
   - Elérhető promptok listázása (ha támogatott)

3. **Eszközök meghívása**
   - Alapvető kalkulátor műveletek (összeadás, kivonás, szorzás, osztás)
   - Súgó parancs a szerver információkhoz
   - Megfelelő argumentumok átadása és eredmények kezelése

4. **Hibakezelés**
   - Kapcsolati hibák
   - Eszköz végrehajtási hibák
   - Kíméletes hiba és felhasználói visszajelzés

5. **Eredmény feldolgozás**
   - Szöveges tartalom kinyerése a válaszokból
   - Kimenet formázása olvashatóság érdekében
   - Különböző válaszformátumok kezelése

## Előfeltételek

A kliensek futtatása előtt győződj meg arról, hogy:

1. **A megfelelő MCP szerver fut** (a `../01-first-server/` könyvtárból)
2. **A szükséges függőségek telepítve vannak** a választott nyelvhez
3. **Megfelelő hálózati kapcsolat** van (HTTP-alapú átvitelekhez)

## Fő különbségek az implementációk között

| Nyelv      | Átvitel   | Szerver indítás | Async modell | Kulcs könyvtárak       |
|------------|-----------|-----------------|--------------|------------------------|
| Java       | SSE/HTTP  | Külső           | Szinkron     | WebFlux, MCP SDK       |
| C#         | Stdio     | Automatikus     | Async/Await  | .NET MCP SDK           |
| TypeScript | Stdio     | Automatikus     | Async/Await  | Node MCP SDK           |
| Python     | Stdio     | Automatikus     | AsyncIO      | Python MCP SDK         |
| Rust       | Stdio     | Automatikus     | Async/Await  | Rust MCP SDK, Tokio    |

## Következő lépések

Miután felfedezted ezeket a kliens példákat:

1. **Módosítsd a klienseket**, hogy új funkciókat vagy műveleteket adj hozzá
2. **Hozz létre saját szervert**, és teszteld ezeket a kliensekkel
3. **Kísérletezz különböző átvitelekkel** (SSE vs. Stdio)
4. **Építs egy összetettebb alkalmazást**, amely integrálja az MCP funkcionalitást

## Hibakeresés

### Gyakori problémák

1. **Kapcsolat megtagadva**: Győződj meg arról, hogy az MCP szerver a várt porton/útvonalon fut
2. **Modul nem található**: Telepítsd a szükséges MCP SDK-t a nyelvedhez
3. **Hozzáférés megtagadva**: Ellenőrizd a fájlengedélyeket stdio átvitelhez
4. **Eszköz nem található**: Ellenőrizd, hogy a szerver implementálja-e a várt eszközöket

### Hibakeresési tippek

1. **Kapcsold be a részletes naplózást** az MCP SDK-ban
2. **Ellenőrizd a szerver naplóit** hibaüzenetekért
3. **Győződj meg arról, hogy az eszköznevek és aláírások** egyeznek a kliens és szerver között
4. **Teszteld MCP Inspectorral** először a szerver funkcionalitásának validálásához

## Kapcsolódó dokumentáció

- [Fő kliens oktatóanyag](./README.md)
- [MCP szerver példák](../../../../03-GettingStarted/01-first-server)
- [MCP LLM integrációval](../../../../03-GettingStarted/03-llm-client)
- [Hivatalos MCP dokumentáció](https://modelcontextprotocol.io/)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
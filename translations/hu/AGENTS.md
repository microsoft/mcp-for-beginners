# AGENTS.md

## Projektáttekintés

**MCP kezdőknek** egy nyílt forráskódú oktatási tananyag, amely az AI modellek és kliensalkalmazások közötti interakciók szabványos keretrendszerének, a Model Context Protocol (MCP) megismerésére szolgál. Ez a tároló átfogó tanulási anyagokat kínál gyakorlati kódpéldákkal több programozási nyelven.

### Kulcstechnológiák

- **Programozási nyelvek**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Keretrendszerek és SDK-k**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Adatbázisok**: PostgreSQL pgvector kiterjesztéssel
- **Felhőplatformok**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build eszközök**: npm, Maven, pip, Cargo
- **Dokumentáció**: Markdown automatikus többnyelvű fordítással (48+ nyelv)

### Architektúra

- **11 alapmodul (00-11)**: Lépésről lépésre haladó tanulási útvonal az alapoktól a haladó témákig
- **Gyakorlati laborok**: Gyakorlati feladatok teljes megoldási kóddal több nyelven
- **Mintaprojektek**: Működő MCP szerver és kliens implementációk
- **Fordítási rendszer**: Automatikus GitHub Actions munkafolyamat többnyelvű támogatáshoz
- **Képállományok**: Központosított képkönyvtár fordított verziókkal

## Beállítási parancsok

Ez egy dokumentációra fókuszáló tároló. A legtöbb beállítás az egyes mintaprojektekben és laborokban történik.

### Tároló beállítása

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Mintaprojektek használata

A mintaprojektek helye:
- `03-GettingStarted/samples/` - Nyelvspecifikus példák
- `03-GettingStarted/01-first-server/solution/` - Első szerver implementációk
- `03-GettingStarted/02-client/solution/` - Kliens implementációk
- `11-MCPServerHandsOnLabs/` - Átfogó adatbázis-integrációs laborok

Minden mintaprojekt saját beállítási útmutatót tartalmaz:

#### TypeScript/JavaScript projektek
```bash
cd <project-directory>
npm install
npm start
```

#### Python projektek
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java projektek
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Fejlesztési munkafolyamat

### Dokumentáció felépítése

- **00-11 modulok**: Alaptananyag tartalom sorrendben
- **translations/**: Nyelvspecifikus verziók (automatikusan generált, ne szerkeszd közvetlenül)
- **translated_images/**: Lokalizált képek verziói (automatikusan generált)
- **images/**: Forrásképek és diagramok

### Dokumentáció módosítása

1. Csak az angol markdown fájlokat szerkeszd a gyökérmodul könyvtárakban (00-11)
2. Ha szükséges, frissítsd a képeket az `images/` könyvtárban
3. A co-op-translator GitHub Action automatikusan generálja a fordításokat
4. A fordítások a fő ágra történő push után újra generálódnak

### Fordítások kezelése

- **Automatikus fordítás**: GitHub Actions munkafolyamat kezeli az összes fordítást
- **NE szerkeszd kézzel** a `translations/` könyvtár fájljait
- A fordítási metaadatok minden fordított fájlba be vannak ágyazva
- Támogatott nyelvek: 48+ nyelv, beleértve az arabot, kínait, franciát, németet, hindit, japánt, koreait, portugált, oroszt, spanyolt és sok más nyelvet

## Tesztelési útmutató

### Dokumentáció validálása

Mivel ez elsősorban egy dokumentációs tároló, a tesztelés az alábbiakra összpontosít:

1. **Linkek validálása**: Ellenőrizd, hogy minden belső hivatkozás működik
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Kódminták validálása**: Teszteld, hogy a kódpéldák lefordulnak/futnak
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown lintelés**: Ellenőrizd a formázási konzisztenciát
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Mintaprojektek tesztelése

Minden nyelvspecifikus minta saját tesztelési megközelítést tartalmaz:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Kódstílus irányelvek

### Dokumentáció stílusa

- Használj világos, kezdőbarát nyelvezetet
- Tartalmazz kódpéldákat több nyelven, ahol alkalmazható
- Kövesd a markdown legjobb gyakorlatokat:
  - Használj ATX-stílusú fejléceket (`#` szintaxis)
  - Használj kerített kódblokkokat nyelvazonosítókkal
  - Tartalmazz leíró alt szöveget a képekhez
  - Tartsd ésszerűen a sorhosszokat (nincs szigorú korlát, de légy ésszerű)

### Kódminta stílusa

#### TypeScript/JavaScript
- Használj ES modulokat (`import`/`export`)
- Kövesd a TypeScript szigorú mód konvencióit
- Tartalmazz típusannotációkat
- Célozd meg az ES2022-t

#### Python
- Kövesd a PEP 8 stílusirányelveket
- Használj típusjelzéseket, ahol megfelelő
- Tartalmazz docstringeket a függvényekhez és osztályokhoz
- Használj modern Python funkciókat (3.8+)

#### Java
- Kövesd a Spring Boot konvenciókat
- Használj Java 21 funkciókat
- Kövesd a szabványos Maven projektstruktúrát
- Tartalmazz Javadoc kommenteket

### Fájlok szervezése

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build és telepítés

### Dokumentáció telepítése

A tároló GitHub Pages vagy hasonló rendszert használ a dokumentáció hosztolására (ha alkalmazható). A fő ágra történő változtatások kiváltják:

1. Fordítási munkafolyamat (`.github/workflows/co-op-translator.yml`)
2. Az összes angol markdown fájl automatikus fordítása
3. Képek lokalizálása szükség szerint

### Nincs szükség build folyamatra

Ez a tároló elsősorban markdown dokumentációt tartalmaz. Nincs szükség fordítási vagy build lépésre az alaptananyag tartalomhoz.

### Mintaprojektek telepítése

Az egyes mintaprojektek saját telepítési útmutatóval rendelkezhetnek:
- Lásd `03-GettingStarted/09-deployment/` az MCP szerver telepítési útmutatójához
- Azure Container Apps telepítési példák a `11-MCPServerHandsOnLabs/` könyvtárban

## Hozzájárulási irányelvek

### Pull Request folyamat

1. **Fork és klónozás**: Forkold a tárolót és klónozd a forkot helyben
2. **Ág létrehozása**: Használj leíró ágneveket (pl. `fix/typo-module-3`, `add/python-example`)
3. **Változtatások végrehajtása**: Csak az angol markdown fájlokat szerkeszd (ne fordításokat)
4. **Teszteld helyben**: Ellenőrizd, hogy a markdown helyesen jelenik meg
5. **PR beküldése**: Használj egyértelmű PR címeket és leírásokat
6. **CLA**: Írd alá a Microsoft Contributor License Agreement-et, amikor erre felszólítanak

### PR cím formátuma

Használj egyértelmű, leíró címeket:
- `[Module XX] Rövid leírás` modul-specifikus változtatásokhoz
- `[Samples] Leírás` mintakód változtatásokhoz
- `[Docs] Leírás` általános dokumentációs frissítésekhez

### Mit lehet hozzájárulni

- Hibajavítások a dokumentációban vagy kódmintákban
- Új kódpéldák további nyelveken
- Pontosítások és fejlesztések a meglévő tartalomban
- Új esettanulmányok vagy gyakorlati példák
- Hibajelentések homályos vagy helytelen tartalomról

### Mit NE tegyél

- Ne szerkeszd közvetlenül a `translations/` könyvtár fájljait
- Ne szerkeszd a `translated_images/` könyvtárat
- Ne adj hozzá nagy bináris fájlokat megbeszélés nélkül
- Ne változtasd meg a fordítási munkafolyamat fájlokat koordináció nélkül

## További megjegyzések

### Tároló karbantartása

- **Változásnapló**: Minden jelentős változás dokumentálva van a `changelog.md` fájlban
- **Tanulmányi útmutató**: Használd a `study_guide.md` fájlt a tananyag navigációs áttekintéséhez
- **Hibajelentés sablonok**: Használd a GitHub hibajelentés sablonokat hibajelentésekhez és funkciókérésekhez
- **Magatartási kódex**: Minden hozzájárulónak követnie kell a Microsoft Open Source Code of Conduct-ot

### Tanulási útvonal

Kövesd a modulokat sorrendben (00-11) az optimális tanulás érdekében:
1. **00-02**: Alapok (Bevezetés, Alapfogalmak, Biztonság)
2. **03**: Kezdés gyakorlati megvalósítással
3. **04-05**: Gyakorlati megvalósítás és haladó témák
4. **06-10**: Közösség, legjobb gyakorlatok és valós alkalmazások
5. **11**: Átfogó adatbázis-integrációs laborok (13 egymást követő labor)

### Támogatási források

- **Dokumentáció**: https://modelcontextprotocol.io/
- **Specifikáció**: https://spec.modelcontextprotocol.io/
- **Közösség**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord szerver
- **Kapcsolódó kurzusok**: Lásd README.md további Microsoft tanulási útvonalakért

### Gyakori problémák megoldása

**K: Miért bukik el a PR fordítási ellenőrzése?**  
V: Ellenőrizd, hogy csak az angol markdown fájlokat szerkesztetted a gyökérmodul könyvtárakban, nem a fordított verziókat.

**K: Hogyan adhatok hozzá új nyelvet?**  
V: A nyelvi támogatást a co-op-translator munkafolyamat kezeli. Nyiss egy hibajelentést az új nyelvek hozzáadásának megbeszéléséhez.

**K: Miért nem működnek a kódminták?**  
V: Ellenőrizd, hogy követted-e a konkrét minta README-jében található beállítási útmutatót. Ellenőrizd, hogy a megfelelő verziójú függőségek telepítve vannak-e.

**K: Miért nem jelennek meg a képek?**  
V: Ellenőrizd, hogy a képek elérési útjai relatívak és előre perjelezettek. A képeknek az `images/` könyvtárban vagy a `translated_images/` lokalizált verziókban kell lenniük.

### Teljesítmény szempontok

- A fordítási munkafolyamat több percet is igénybe vehet
- Nagy képeket optimalizálni kell a commit előtt
- Tartsd az egyes markdown fájlokat fókuszáltan és ésszerű méretűen
- Használj relatív hivatkozásokat a jobb hordozhatóság érdekében

### Projektirányítás

Ez a projekt a Microsoft nyílt forráskódú gyakorlatát követi:
- MIT licenc a kódhoz és dokumentációhoz
- Microsoft Open Source Code of Conduct
- CLA szükséges a hozzájárulásokhoz
- Biztonsági problémák: Kövesd a SECURITY.md irányelveket
- Támogatás: Lásd SUPPORT.md a segítségnyújtási forrásokért

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
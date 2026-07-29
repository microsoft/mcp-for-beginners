# AGENTS.md

## Projekt áttekintése

**MCP kezdőknek** egy nyílt forráskódú oktatási tananyag a Model Context Protocol (MCP) elsajátításához – egy szabványosított keretrendszer az AI modellek és ügyfélalkalmazások közötti interakciókhoz. Ez a tárhely átfogó tananyagot és gyakorlati kódpéldákat kínál több programozási nyelven.

### Kulcs technológiák

- **Programozási nyelvek**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Keretrendszerek és SDK-k**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Adatbázisok**: PostgreSQL pgvector kiterjesztéssel
- **Felhőplatformok**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build eszközök**: npm, Maven, pip, Cargo
- **Dokumentáció**: Markdown automatizált többnyelvű fordítással (48+ nyelv)

### Architektúra

- **11 fő modul (00-11)**: Szisztematikus tanulási út az alapoktól a haladó témákig
- **Gyakorlati laborgyakorlatok**: Gyakorlati feladatok komplett megoldási kóddal több nyelven
- **Minta projektek**: Működő MCP szerver és kliens implementációk
- **Fordítási rendszer**: Automatizált GitHub Actions munkafolyamat többnyelvű támogatáshoz
- **Kép állományok**: Központi képtár helyi fordított változatokkal

## Beállító parancsok

Ez egy dokumentációközpontú tárhely. A legtöbb beállítás az egyes mintaprojektekben és laborgyakorlatokban történik.

### A tárhely beállítása

```bash
# Klónozd a tárolót
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Minta projektekkel való munka

A minta projektek helye:
- `03-GettingStarted/samples/` - Nyelvspecifikus példák
- `03-GettingStarted/01-first-server/solution/` - Első szerver implementációk
- `03-GettingStarted/02-client/solution/` - Kliens implementációk
- `11-MCPServerHandsOnLabs/` - Átfogó adatbázis integrációs laborgyakorlatok

Minden minta projekt saját beállítási utasításokat tartalmaz:

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
# vagy
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

### MCP 7-28 készültség

#### Tárhely készültségi ellenőrző lista

- [x] **Új közreműködők számára egyértelműség**: Ez a fájl meghatározza a tárhely célját,
  struktúráját, hozzájárulási szabályokat és minta beállítási útvonalakat.
- [x] **Pontos build/test/lint parancsok**:
  - Tárhely dokumentáció lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Tárhely dokumentáció linkminta ellenőrzés:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript minta validáció:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python minta validáció:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java minta validáció:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Egy realisztikus munkafolyamat, ami MCP eszközzé válhat**:
  `validate_curriculum_change`
- [x] **Bemenetek/kimenetek explicit megadása** (lásd lentebb a specifikációt).
- [x] **Engedélyek és hibamódok dokumentálva** (lásd lentebb a specifikációt).
- [x] **CI tesztelhetőség explicit** (determinista parancsok, explicit kilépési kódok,
  és gépileg olvasható kimenetek).

#### Jelölt MCP eszköz munkafolyamat: `validate_curriculum_change`

##### Cél

Ellenőrizni a tananyag dokumentáció változásokat és a példakód egészségi állapotát
a beolvadás előtt.

##### Bemenetek

- `changed_paths: string[]` (kötelező) - a PR-ban változott relatív elérési utak.
- `run_docs_lint: boolean` (alapértelmezett `true`)
- `run_links_audit: boolean` (alapértelmezett `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (alapértelmezett mind `false`)

##### Kimenetek

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Engedélyek

- Csak munkakönyvtár fájlok olvasása és eszköz által generált állományok írása (pl. lint
  jelentések, teszt logok); nem ír a `translations/` vagy
  `translated_images/` könyvtárakba.
- Helyi shell parancsok futtatása.
- Hálózati hozzáférés csak opcionálisan, a csomaghelyreállításhoz (`npm ci`,
  `python -m pip install`, `mvn` függőség feloldás).
- Nincs jogosultság push-olásra, merge-re vagy módosításra a `translations/` vagy
  `translated_images/` könyvtárakban.

##### Hibamódok

- `E_NO_INPUT_PATHS`: `changed_paths` üres.
- `E_INVALID_PATH`: bemeneti elérési út kilép a tárhely gyökérből.
- `E_LINT_FAILED`: markdown lint nem nulla kilépési kóddal állt le.
- `E_LINK_AUDIT_FAILED`: link ellenőrző parancs nem nulla kilépési kóddal állt le.
- `E_SAMPLE_TEST_FAILED`: minta teszt/build nem nulla kilépési kóddal állt le.
- `E_TIMEOUT`: a parancs túllépte a beállított időkorlátot.

##### Ajánlott CI szerződés

Az ellenőrzés automatizálásához állíts be egy CI feladatot, amely:

- Aktiválódik olyan pull requestek esetén, amelyek `*.md` fájlokat, példakódokat vagy ezt a fájlt érintik.
- A fent megadott pontos parancsokat futtatja.
- Megőrzi a logokat műtárgyaként.
- A feladat hibás lesz nem nulla kilépési kód esetén.

#### Ha MCP szervert szállítasz erről a tárhelyről

- [ ] Olvasd át az MCP 7-28 váznaptárat:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Teszteld a szervered az SDK bétáival:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Távolítsd el a munkamenet és kézfogás feltételezéseket; kezelj minden kérést
  önálló egységként:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Küldj `Mcp-Method` és `Mcp-Name` fejléceket nyers HTTP kérésekhez:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Vizsgáld át a kemény kódolt hibakódokat (`missing resource` áthelyezve `-32002`-ről `-32602`-re).
- [ ] Jelöld és tervezd a migrációt elavult gyökerek, mintavételezés és
  naplózás esetén:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrálj az experimentális `2025-11-25` Tasks API-ról:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Tekintsd át az OAuth és OpenID Connect jogosultságokat:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentációs struktúra

- **Modulok 00-11**: Alap tananyag sorrendben
- **translations/**: Nyelvspecifikus változatok (automatikusan generált, ne szerkeszd közvetlenül)
- **translated_images/**: Lokalizált képek (automatikusan generált)
- **images/**: Forrás képek és ábrák

### Dokumentációs változtatások végrehajtása

1. Csak az angol nyelvű markdown fájlokat szerkeszd a gyökér modul könyvtárakban (00-11)
2. Szükség esetén frissítsd a `images/` könyvtár képeit
3. A co-op-translator GitHub Action automatikusan generálja a fordításokat
4. A fordítások újragenerálódnak a main ágra történő push után

### Fordítások kezelése

- **Automatizált fordítás**: A GitHub Actions munkafolyamat kezeli az összes fordítást
- **NE szerkeszd kézzel** a `translations/` könyvtár fájljait
- A fordítás metaadata minden fordított fájlban beágyazott
- Támogatott nyelvek: több mint 48 nyelv, köztük arab, kínai, francia, német, hindi, japán, koreai, portugál, orosz, spanyol és sok más

## Tesztelési utasítások

### Dokumentáció ellenőrzés

Mivel főleg dokumentációs tárhelyről van szó, a tesztelés fókusza:

1. **Linkminta ellenőrzés**: A Markdown linkek listázása áttekintésre

   ```bash
   # Markdown linkek felsorolása (mintázatellenőrzés)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kódminta validáció**: A kód példák fordítása/futtatása

   ```bash
   # Navigáljon egy adott mintához, és futtassa le a tesztjeit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown lintelés**: Formázási konzisztencia ellenőrzése

   ```bash
   # Használja a markdownlint-et, ha szükséges
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Minta projekt tesztelés

Minden nyelvspecifikus mintaprojekt saját tesztelési megközelítést alkalmaz:

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

### Dokumentációs stílus

- Használj tiszta, kezdőbarát nyelvezetet
- Több nyelven adj kód példákat, ahol releváns
- Kövesd a markdown legjobb gyakorlatokat:
  - Használj ATX stílusú címsorokat (`#` szintaxis)
  - Használj dettós kódrészleteket nyelvjelzővel
  - Adj képekhez leíró alt szöveget
  - Tartsd észszerűen a sorhosszt (nincs szigorú határ, de légy józan)

### Kódminta stílus

#### TypeScript/JavaScript
- Használj ES modulokat (`import`/`export`)
- Kövesd a TypeScript szigorú mód konvencióit
- Adj típus annotációkat
- Cél verzió: ES2022

#### Python
- Kövesd a PEP 8 stílus irányelveket
- Használj típus jelöléseket, ahol szükséges
- Adj docstringeket függvényekhez és osztályokhoz
- Használj modern Python funkciókat (3.8+)

#### Java
- Kövesd a Spring Boot konvenciókat
- Használj Java 21 funkciókat
- Kövesd a standard Maven projekt struktúrát
- Adj Javadoc kommenteket

### Fájlszervezés

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

### Dokumentáció telepítés

A tárhely GitHub Pages vagy hasonló szolgáltatást használ dokumentáció hostingra (ha alkalmazható). A main ágra történő változtatás:

1. Elindítja a fordítási munkafolyamatot (`.github/workflows/co-op-translator.yml`)
2. Automatikusan lefordít minden angol markdown fájlt
3. Szükség esetén képek lokalizálása

### Build folyamat nem szükséges

Ez a tárhely elsősorban markdown dokumentációt tartalmaz. Az alap tananyagot nem kell lefordítani vagy buildelni.

### Minta projekt telepítés

Az egyes mintaprojektek saját telepítési utasításokat tartalmazhatnak:
- Lásd a `03-GettingStarted/09-deployment/` MCP szerver telepítési útmutatóját
- Azure Container Apps telepítési példák a `11-MCPServerHandsOnLabs/` könyvtárban

## Hozzájárulási irányelvek

### Pull Request folyamat

1. **Fork és klónozás**: Forkold a tárhelyet, majd klónozd a sajátodat helyileg
2. **Ág létrehozása**: Használj leíró ág neveket (pl. `fix/typo-module-3`, `add/python-example`)
3. **Változtatások**: Csak az angol nyelvű markdown fájlokat szerkeszd (nem a fordításokat)
4. **Helyi tesztelés**: Ellenőrizd, hogy a markdown helyesen jelenik meg
5. **PR beküldése**: Használj egyértelmű címet és leírást a PR-hoz
6. **CLA**: Írd alá a Microsoft Contributor License Agreement-et, ha felszólítanak

### PR cím formátuma

Használj tiszta, leíró címeket:
- `[Module XX] Rövid leírás` modul-specifikus változtatásokhoz
- `[Samples] Leírás` kódpélda változtatásokhoz
- `[Docs] Leírás` általános dokumentáció frissítésekhez

### Mit járulj hozzá

- Hibajavítások a dokumentációban vagy kódpéldákban
- Új kód példák további nyelveken
- Tisztázások és fejlesztések a meglévő tartalmakban
- Új esettanulmányok vagy gyakorlati példák
- Hibajelentések nem tiszta vagy hibás tartalomra

### Mit NE csinálj

- Ne szerkeszd közvetlenül a `translations/` könyvtár fájljait
- Ne szerkeszd a `translated_images/` könyvtárat
- Ne adj hozzá nagy bináris fájlokat egyeztetés nélkül
- Ne változtasd a fordítási munkafolyamat fájlokat koordináció nélkül

## További megjegyzések

### Tárhely karbantartás

- **Változásnapló**: Minden jelentős változás dokumentálva van a `changelog.md`-ben
- **Tanulmányi útmutató**: Használd a `study_guide.md`-t a tananyag áttekintéséhez
- **Hibajegyből sablonok**: Használj GitHub hibajegy sablonokat hibajelentéshez és funkciókéréshez
- **Magatartási kódex**: Minden közreműködőnek követnie kell a Microsoft Open Source Magatartási kódexét

### Tanulási útvonal

Kövesd a modulokat sorrendben (00-11) a optimális tanulásért:
1. **00-02**: Alapok (Bevezetés, Alapfogalmak, Biztonság)
2. **03**: Első lépések gyakorlati megvalósítással
3. **04-05**: Gyakorlati megvalósítás és haladó témák
4. **06-10**: Közösség, legjobb gyakorlatok és valós alkalmazások
5. **11**: Átfogó adatbázis integrációs laborgyakorlatok (13 egymást követő laborgyakorlat)

### Támogatási erőforrások

- **Dokumentáció**: https://modelcontextprotocol.io/
- **Specifikáció**: https://spec.modelcontextprotocol.io/
- **Közösség**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord szerver
- **Kapcsolódó tanfolyamok**: Lásd README.md a további Microsoft tanulási útvonalakért

### Gyakori hibaelhárítás

**K: A PR-om elbukik a fordítási ellenőrzésen**
V: Győződj meg róla, hogy csak az angol nyelvű markdown fájlokat szerkesztetted a gyökér modul könyvtárakban, nem a lefordított verziókat.

**K: Hogyan adhatok hozzá új nyelvet?**
V: A nyelvi támogatást a co-op-translator munkafolyamat kezeli. Nyiss egy hibajegyet az új nyelvek hozzáadásának megbeszéléséhez.

**K: A kód példák nem működnek**

V: Győződjön meg róla, hogy követte a konkrét minta README fájljában található beállítási útmutatót. Ellenőrizze, hogy a megfelelő verziójú függőségek vannak telepítve.

**K: A képek nem jelennek meg**
V: Ellenőrizze, hogy a képútvonalak relatívak és perjeleket használnak. A képeknek az `images/` könyvtárban kell lenniük, vagy a lokalizált verzióknál a `translated_images/` mappában.

### Teljesítmény szempontok

- A fordítási munkafolyamat több percig is eltarthat
- Nagy képeket érdemes optimalizálni a commit előtt
- Tartsa az egyes markdown fájlokat fókuszáltnak és ésszerű méretűnek
- Használjon relatív hivatkozásokat a jobb hordozhatóság érdekében

### Projekt irányítás

Ez a projekt a Microsoft nyílt forráskódú gyakorlatainak megfelelően működik:
- MIT licenc a kódra és dokumentációra
- Microsoft Open Source Code of Conduct
- CLA kötelező hozzájárulások esetén
- Biztonsági problémák: Kövesse a SECURITY.md irányelveit
- Támogatás: Lásd a SUPPORT.md fájlt segélyforrásokért

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
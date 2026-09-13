# AGENTS.md

## Projekt áttekintése

**MCP kezdőknek** egy nyílt forráskódú oktatási tananyag a Model Context Protocol (MCP) - az AI modellek és kliens alkalmazások közötti interakciók szabványosított keretrendszere - elsajátításához. Ez a tároló átfogó tananyagot biztosít gyakorlati kódpéldákkal több programozási nyelven.

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
- **Dokumentáció**: Markdown automatikus többnyelvű fordítással (48+ nyelv)

### Architektúra

- **11 Magmodul (00-11)**: Folyamatos tanulási útvonal az alapoktól a haladó témákig
- **Gyakorlati laborok**: Kódolási gyakorlatok több nyelvű teljes megoldással
- **Minta projektek**: Működő MCP szerver és kliens megvalósítások
- **Fordító rendszer**: Automatikus GitHub Actions munkafolyamat több nyelv támogatására
- **Képi erőforrások**: Központosított képek mappa fordított verziókkal

## Telepítési parancsok

Ez egy dokumentáció-központú tároló. A legtöbb telepítés az egyes minta projektekben és laborokban történik.

### Tároló beállítása

```bash
# Klónozd a tárolót
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Minta projektek kezelése

A minta projektek helye:
- `03-GettingStarted/samples/` - Nyelvspecifikus példák
- `03-GettingStarted/01-first-server/solution/` - Első szerver megvalósítások
- `03-GettingStarted/02-client/solution/` - Kliens megvalósítások
- `11-MCPServerHandsOnLabs/` - Átfogó adatbázis integrációs laborok

Minden minta projekthez saját telepítési útmutató tartozik:

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

#### Tároló készültségi ellenőrző lista

- [x] **Új közreműködők számára világos**: Ez a fájl határozza meg a tároló célját,
  szerkezetét, hozzájárulási szabályokat, és a minta telepítési útvonalakat.
- [x] **Build/test/lint parancsok pontos kapcsolókkal**:
  - Tároló dokumentáció lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Tároló dokumentáció linkminta audit:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript minta validálás:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python minta validálás:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java minta validálás:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Egy valós munkafolyamat ami MCP eszközzé válhat**:
  `validate_curriculum_change`
- [x] **Bemenetek/kimenetek egyértelműek** (lásd alább a specifikációt).
- [x] **Engedélyek és hibamódok dokumentáltak** (lásd alább a specifikációt).
- [x] **CI tesztelhetőség egyértelmű** (determinista parancsok, egyértelmű
  kilépési kódok, géppel olvasható kimenetek).

#### Jelölt MCP eszköz munkafolyamat: `validate_curriculum_change`

##### Cél

Validálni a tananyagdokumentáció változásait és reprezentatív minta kódok
egészségét összeolvadás előtt.

##### Bemenetek

- `changed_paths: string[]` (kötelező) - az PR által módosított relatív útvonalak.
- `run_docs_lint: boolean` (alapértelmezett `true`)
- `run_links_audit: boolean` (alapértelmezett `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (alapértelmezett minden `false`)

##### Kimenetek

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Engedélyek

- Csak a munkaterület fájljainak olvasása és az eszköz által generált eredmények (pl. lint
  jelentések, teszt naplók) írása; semmilyen írás a `translations/` vagy
  `translated_images/` mappákba.
- Helyi shell parancsok végrehajtása.
- Opcionális hálózati hozzáférés csak csomag-helyreállításhoz (`npm ci`,
  `python -m pip install`, `mvn` függőség feloldás).
- Nincs jogosultság `translations/` vagy
  `translated_images/` módosításához, pusholásához vagy összeolvasztásához.

##### Hibamódok

- `E_NO_INPUT_PATHS`: `changed_paths` üres.
- `E_INVALID_PATH`: bemeneti útvonal kilép a tároló gyökeréből.
- `E_LINT_FAILED`: markdown lint nem nulla kilépési kóddal kilép.
- `E_LINK_AUDIT_FAILED`: link audit parancs nem nulla kilépési kóddal kilép.
- `E_SAMPLE_TEST_FAILED`: minta teszt/build nem nulla kilépési kóddal kilép.
- `E_TIMEOUT`: parancs túllépte a beállított időkorlátot.

##### Ajánlott CI szerződés

Az érvényesítés automatizálásához állíts be egy CI feladatot, amely:

- Felhúzás kérésekre (pull request), amelyek érintik a `*.md`, minta kódokat vagy ezt a fájlt.
- Futtatja a fent felsorolt pontos parancsokat.
- Ment naplókat eredményként.
- Hibára fut bármely nem nulla kilépési kód esetén.

#### Ha MCP szervert szállítasz innen a tárolóból

- [ ] Olvasd el a végleges MCP `2026-07-28` változásjegyzéket:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Ellenőrizd, hogy a kiválasztott SDK kiadás támogatja-e az MCP `2026-07-28` verziót:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Távolítsd el a munkamenet- és kézfogás feltételezéseket; minden kérés legyen
  önálló egység:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Küldd el a `Mcp-Method` és `Mcp-Name` fejlécet az alap HTTP kérésekhez:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Vizsgáld felül a keménykódolt hibakódokat (`missing resource` áthelyezve a `-32002`-ről `-32602`-re).

- [ ] Áthelyezni a megszűnt Roots, Sampling, Logging és Dynamic Client
  regisztrációt:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Áttérés az experimentális `2025-11-25` Tasks API-ról:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Felülvizsgálni az OAuth és OpenID Connect engedélyezést a megerősítéshez:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentációs struktúra

- **00-11 modulok**: Alap tananyag tartalma sorrendben
- **translations/**: Nyelvspecifikus verziók (automatikusan generált, ne szerkessze közvetlenül)
- **translated_images/**: Lokalizált képek verziói (automatikusan generált)
- **images/**: Forrás képek és diagramok

### Dokumentációs változtatások végrehajtása

1. Csak az angol markdown fájlokat szerkessze a gyökér modul könyvtárakban (00-11)
2. Szükség esetén frissítse a képeket az `images/` könyvtárban
3. A co-op-translator GitHub Action automatikusan generálja a fordításokat
4. A fordítás újragenerálódik, amikor a fő ágra push-olnak

### Fordítások kezelése

- **Automatizált fordítás**: A GitHub Actions folyamat kezeli az összes fordítást
- Ne szerkessze kézzel a `translations/` könyvtár fájljait
- A fordítási metaadatok minden fordított fájlban beágyazva vannak
- Támogatott nyelvek: 48+ nyelv, beleértve az arabot, kínait, franciát, németet, hindit, japánt, koreait, portugált, oroszt, spanyolt és még sok mást

## Tesztelési útmutató

### Dokumentáció érvényesítése

Mivel elsősorban dokumentációs tárhelyről van szó, a tesztelés az alábbiakra összpontosít:

1. **Link mintázat ellenőrzése**: Markdown linkek listázása átnézéshez

   ```bash
   # Markdown linkek listázása (mintavizsgálat)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kód példa validálás**: Ellenőrizze, hogy a kód példák fordíthatók/futtathatók

   ```bash
   # Navigáljon egy adott mintához, és futtassa annak tesztjeit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Formázási következetesség ellenőrzése

   ```bash
   # Használd a markdownlint-et, ha szükséges
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Mintaprojekt tesztelése

Minden nyelvspecifikus mintához saját tesztelési megközelítés tartozik:

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

## Kód stílus irányelvek

### Dokumentáció stílusa

- Használjon világos, kezdőknek szóló nyelvezetet
- Tartalmazzon kód példákat több nyelven, ahol alkalmazható
- Kövesse a markdown legjobb gyakorlatait:
  - Használjon ATX stílusú címeket (`#` szintaxis)
  - Használjon keretes kódblokkokat nyelvazonosítókkal
  - Tartalmazzon képleíró alt szöveget a képekhez
  - Tartsa mértékkel a sorhosszakat (nincs kemény korlát, de legyen értelmes)

### Kód példa stílusa

#### TypeScript/JavaScript
- Használjon ES modulokat (`import`/`export`)
- Kövesse a TypeScript szigorú mód konvencióit
- Tartalmazzon típus annotációkat
- Célzott ES2022

#### Python
- Kövesse a PEP 8 stílusirányelveket
- Használjon típusjelöléseket ahol megfelelő
- Tartalmazzon docstringeket függvényekhez és osztályokhoz
- Használjon modern Python funkciókat (3.8+)

#### Java
- Kövesse a Spring Boot konvenciókat
- Használjon Java 21 funkciókat
- Kövesse a szabványos Maven projekt szerkezetet
- Tartalmazzon Javadoc kommenteket

### Fájl szervezés

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

A tárhely GitHub Pages vagy hasonlót használ dokumentáció hosztolására (ha alkalmazható). A főág változásai kiváltják:

1. Fordítási folyamat (`.github/workflows/co-op-translator.yml`)
2. Minden angol markdown fájl automatikus fordítása

3. Kép lokalizálása szükség szerint

### Nincs szükség build folyamatra

Ez a tároló elsősorban markdown dokumentációt tartalmaz. A fő tananyag tartalmának nem szükséges fordítási vagy build lépés.

### Minta projekt telepítése

Egyéni minta projektekhez lehetnek telepítési utasítások:
- Lásd a `03-GettingStarted/09-deployment/` mappát az MCP szerver telepítési útmutatóért
- Azure Container Apps telepítési példák a `11-MCPServerHandsOnLabs/` mappában

## Hozzájárulási irányelvek

### Pull Request folyamat

1. **Fork és klónozás**: Forkold a tárolót, majd klónozd helyileg a forkodat
2. **Ág létrehozása**: Használj leíró ágneveket (például `fix/typo-module-3`, `add/python-example`)
3. **Változtatások**: Szerkeszd csak az angol nyelvű markdown fájlokat (ne a fordításokat)
4. **Tesztelés helyben**: Ellenőrizd, hogy a markdown helyesen jelenik meg
5. **PR beküldése**: Használj világos PR címet és leírást
6. **CLA**: Írd alá a Microsoft Hozzájárulói Licenc Megállapodást, amikor erre kérnek

### PR cím formátum

Használj egyértelmű, leíró címeket:
- `[Module XX] Rövid leírás` modul-specifikus változtatásokhoz
- `[Samples] Leírás` mintakód változtatásokhoz
- `[Docs] Leírás` általános dokumentációs frissítésekhez

### Mihez járulhatsz hozzá

- Hibajavítások dokumentációban vagy kódmintákban
- Új kódpéldák további nyelveken
- Megerősítések és fejlesztések a meglévő tartalomban
- Új esettanulmányok vagy gyakorlati példák
- Probléma jelentések homályos vagy hibás tartalomról

### Mit ne tegyél

- Ne szerkeszd közvetlenül a `translations/` könyvtár fájljait
- Ne szerkeszd a `translated_images/` könyvtárat
- Ne adj hozzá nagy bináris fájlokat megbeszélés nélkül
- Ne változtass a fordítási munkafolyamat fájlokon előzetes egyeztetés nélkül

## További megjegyzések

### Tároló karbantartás

- **Változásnapló**: Minden jelentős változás dokumentálva van a `changelog.md` fájlban
- **Tanulmányi útmutató**: Használd a `study_guide.md`-t a tananyag áttekintő navigációjához
- **Probléma sablonok**: Használd a GitHub problémasablonjait hibajelentésekhez és funkciókéréshez
- **Magatartási kódex**: Minden közreműködőnek be kell tartania a Microsoft Nyílt Forráskód Magatartási Kódexet

### Tanulási útvonal

A modulokat sorrendben (00-11) kövesd az optimális tanulás érdekében:
1. **00-02**: Alapok (Bevezetés, Alapfogalmak, Biztonság)
2. **03**: Kezdő lépések gyakorlati megvalósítással
3. **04-05**: Gyakorlati megvalósítás és haladó témák
4. **06-10**: Közösség, bevált gyakorlatok és valós alkalmazások
5. **11**: Átfogó adatbázis integrációs laborok (13 egymás utáni labor)

### Támogatási erőforrások

- **Dokumentáció**: https://modelcontextprotocol.io/
- **Specifikáció**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Közösség**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord szerver
- **Kapcsolódó tanfolyamok**: Lásd a README.md fájlt más Microsoft tanulási útvonalakért

### Gyakori hibakeresés

**K: A PR-em elbukik a fordítási ellenőrzésen**
V: Győződj meg arról, hogy csak az angol nyelvű markdown fájlokat szerkesztetted a gyökér modul könyvtárakban, nem a fordításokat.

**K: Hogyan adhatok hozzá új nyelvet?**
V: A nyelvi támogatás a co-op-translator munkafolyamat révén van kezelve. Nyiss egy issue-t az új nyelvek hozzáadása érdekében.

**K: A kódpéldák nem működnek**

A: Győződj meg róla, hogy követted a telepítési utasításokat az adott példa README fájljában. Ellenőrizd, hogy a megfelelő verziójú függőségek telepítve vannak.


**K: A képek nem jelennek meg** 

A: Ellenőrizze, hogy a képek elérési útjai relatívak és előre mutató perjeleket használnak. A képeknek az `images/` könyvtárban vagy a lokalizált verziók esetén a `translated_images/` könyvtárban kell lenniük.

### Teljesítmény szempontok

- A fordítási munkafolyamat több percig is eltarthat
- A nagy méretű képeket optimalizálni kell elkötelezés előtt
- Tartsa a markdown fájlokat fókuszáltan és ésszerű méretűen
- Használjon relatív hivatkozásokat a jobb hordozhatóság érdekében

### Projektirányítás

Ez a projekt a Microsoft nyílt forráskódú gyakorlatait követi:
- MIT licenc a kódra és dokumentációra
- Microsoft nyílt forráskódú magatartási kódex
- CLA szükséges a hozzájárulásokhoz
- Biztonsági problémák: Kövesse a SECURITY.md útmutatásait
- Támogatás: Kérjen segítséget a SUPPORT.md-ben található forrásokból

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
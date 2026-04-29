# Változásnapló: MCP kezdőknek tananyag

Ez a dokumentum a Model Context Protocol (MCP) kezdőknek szóló tananyagában történt minden jelentős változás nyilvántartására szolgál. A változások fordított időrendi sorrendben vannak dokumentálva (a legújabb változások elöl).

## 2026. április 11.

### Új lecke, dokumentációs javítások és függőségfrissítések

#### Új tananyagtartalom hozzáadva

**05-ös modul – Haladó témák**
- **5.17. lecke: Ellenséges többügynökös érvelés MCP-vel** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Új átfogó útmutató az ellenséges vitázó mintáról többügynökös rendszerekben
  - Mermaid architektúra diagram: két ügynök → közös MCP szerver → vita átirat → bíró → ítélet
  - Közös MCP eszközszerver (`web_search` + `run_python`) Pythonban és TypeScriptben megvalósítva
  - Ellentétes rendszerutasítások (MELLETT / ELLEN / Bíró) explicit eszközhasználati követelményekkel
  - Vita rendező Pythonban, TypeScriptben és C#-ban, köröket kezelve és érveket irányítva
  - MCP `ClientSession` bekötése a rendező részére a valódi eszközhívásokhoz
  - Használati eset tábla (hallucináció detektálás, fenyegetésmodellezés, API tervezési áttekintés, tényellenőrzés, technológia választás)
  - Biztonsági megfontolások: sandbox környezet, eszközhívás érvényesítés, ráta korlátozás, audit naplózás
  - Strukturált gyakorlat három gyakorlati szcenárióval (kódáttekintés, architektúra döntés, tartalom moderálás)

#### Dokumentációs javítások

**03-as modul – Kezdés**
- **05-stdio-server/README.md**: Javított hiányos TypeScript stdio szerver példa — hozzáadva hiányzó transzport példányosítás (`new StdioServerTransport()`) és `server.connect(transport)` hívás, hogy egyezzen a szakaszon belüli Python és .NET példákkal
- **14-sampling/README.md**: Elírás javítva — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Tananyagfrissítések

**Fő README.md**
- Hozzáadva 5.17-es tétel (Ellenséges többügynökös érvelés MCP-vel) a tananyagtáblázathoz közvetlen linken az új leckéhez

**05-AdvancedTopics/README.md**
- Hozzáadva 5.17-es lecke sor a leckék táblázatához

**study_guide.md**
- Hozzáadva az Ellenséges többügynökös érvelés téma az elmetérképhez és a Haladó témák szöveges leírásához

#### Kód- és biztonsági javítások

**05-ös modul – Ellenséges ügynökök (`mcp-adversarial-agents`)**
- **Biztonsági javítás – parancs injekció**: A TypeScript `run_python` eszközben az `execSync` shell interpolációját `execFile` + `promisify` váltotta fel, kiküszöbölve a parancs injekciós felületet (a LLM vezérelt kód már literális argv elemként kerül át shell bevonás nélkül)
- **MCP eszköz hurok bekötés**: A Python vita rendező frissítve, hogy `AsyncAnthropic` klienst használjon (blokkoló szinkron `Anthropic` helyett), élő `ClientSession`-t adjon át közvetlenül minden ügynök körének, minden körben lekérdezze az eszköz definíciókat `session.list_tools()`-szal, és a `tool_use` blokkokat hurokban küldje `session.call_tool()` segítségével, amíg a modell végső szöveges választ nem ad

#### Függőségfrissítések

- A `hono` verziója 4.12.12-re emelve több csomagban (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- A `@hono/node-server` 1.19.11-ről 1.19.13-ra frissítve TypeScript csomagokban
- A `cryptography` 46.0.5-ről 46.0.7-re frissítve Python csomagokban (10-StreamliningAIWorkflows laborok 3 és 4)
- A `lodash` 4.17.23-ról 4.18.1-re emelve a 10-StreamliningAIWorkflows inspectorban

#### Fordítások

- 48+ nyelv fordításai szinkronizálva a legfrissebb forrásváltozásokkal (i18n frissítés)

---

## 2026. február 5.

### Tároló-szintű érvényesítés és navigáció fejlesztések

#### Új tananyagtartalom hozzáadva

**03-as modul – Kezdés**
- **12-mcp-hosts/README.md**: Új átfogó útmutató az MCP hostok beállításához
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigurációs példák
  - JSON konfigurációs sablonok minden fő hosthoz
  - Transzport típusok összehasonlító táblázata (stdio, SSE/HTTP, WebSocket)
  - Gyakori kapcsolódási problémák hibakeresése
  - Host konfiguráció biztonsági ajánlások

- **13-mcp-inspector/README.md**: Új hibakeresési útmutató az MCP Inspectorhoz
  - Telepítési módok (npx, globális npm, forrásból)
  - Kapcsolódás stdio és HTTP/SSE-n keresztül
  - Tesztelő eszközök, források és prompt folyamatok
  - VS Code integráció az MCP Inspectorral
  - Gyakori hibakeresési esetek és megoldások

**04-es modul – Gyakorlati megvalósítás**
- **pagination/README.md**: Új lapozási megvalósítási útmutató
  - Cursor-alapú lapozási minták Pythonban, TypeScriptben, Javaban
  - Kliensoldali lapozás kezelése
  - Cursor tervezési stratégiák (áttetsző vs. strukturált)
  - Teljesítményoptimalizálási ajánlások

**05-ös modul – Haladó témák**
- **mcp-protocol-features/README.md**: Új protokoll funkciók mélyreható bemutatása
  - Előrehaladási értesítések megvalósítása
  - Kérés törlési minták
  - Erőforrás sablonok URI mintákkal
  - Szerver életciklus kezelése
  - Naplózási szint vezérlés
  - Hibakezelési minták JSON-RPC kódokkal

#### Navigációs javítások (24+ fájl frissítve)

**Fő modul README-k**
 Most linkelnek mind az első leckéhez, mind a következő modulhoz

**02-Security kiegészítő fájlok**
- Minden 5 kiegészítő biztonsági dokumentum tartalmaz "Mi következik" navigációt:

**09-CaseStudy fájlok**
- Minden esettanulmány fájl most már egymás utáni navigációval rendelkezik:

**10-StreamliningAI laborok**
Hozzáadva "Mi következik" szekció a 10-es modul áttekintőhöz és a 11-es modulhoz

#### Kód- és tartalmi javítások

**SDK és függőségfrissítések**
Üres openai verzió javítva `^4.95.0`-ra
SDK frissítve `^1.8.0`-ról `>=1.26.0`-ra
mcp verziószámok frissítve `>=1.26.0`-ra

**Kód javítások**
Érvénytelen modell `gpt-4o-mini` javítva `gpt-4.1-mini`-re

**Tartalmi javítások**
Törött link javítva `READMEmd` → `README.md`, tananyag fejléc javítva `Module 1-3` → `Module 0-3`, kis-/nagybetű érzékeny elérési út javítva
Tönkrement 5-ös eset tanulmány duplikált tartalma eltávolítva

**Kezdő iránymutatás javítások**
Megfelelő bevezető, tanulási célok és előfeltételek hozzáadva kezdőknek

#### Tananyagfrissítések

**Fő README.md**
- Hozzáadva 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Lapozás), 5.16 (Protokoll funkciók) bejegyzések a tananyagtáblázathoz

**Modul README-k**
Hozzáadva a 12-es és 13-as leckék a leckelistához
Hozzáadva Gyakorlati útmutatók szekció a lapozás linkkel
Hozzáadva 5.15 (Egyéni transzport) és 5.16 (Protokoll funkciók) leckék

**study_guide.md**
- Frissítve az elmetérkép minden új témával: MCP Hosts beállítás, MCP Inspector, Lapozási stratégiák, Protokoll funkciók mélyreható ismertetése

## 2026. január 28.

### MCP 2025-11-25 specifikáció megfelelőség átvizsgálás

#### Alapfogalmak fejlesztése (01-CoreConcepts/)
- **Új kliens primitív – Roots**: Átfogó dokumentáció hozzáadva a Roots kliens primitívről, amely lehetővé teszi a szerverek számára a fájlrendszer határok és hozzáférési jogosultságok megértését
- **Eszköz annotációk**: Dokumentáció a viselkedés annotációkról (`readOnlyHint`, `destructiveHint`) a jobb eszköz végrehajtási döntésekhez
- **Eszköz hívás mintavételnél**: A Sampling dokumentáció frissítve a `tools` és `toolChoice` paraméterekkel, modellezett eszköz hívás támogatására mintavétel közben
- **URL mód felhívás**: Dokumentáció URL alapú behívásról a szerver által indított külső web interakciókhoz
- **Feladatok (kísérleti)**: Új rész hozzáadva a kísérleti feladat funkciókról, tartós végrehajtási csomagolókról és késleltetett eredmény lekérésről
- **Ikon támogatás**: Megjegyzés, hogy eszközök, erőforrások, erőforrás sablonok és promptok most már tartalmazhatnak ikonokat mint kiegészítő metaadatokat

#### Dokumentáció frissítések
- **README.md**: MCP Specifikáció 2025-11-25 verzió hivatkozás és dátumalapú verziózás magyarázat hozzáadva
- **study_guide.md**: Tananyag térkép frissítve a Feladatok és Eszköz annotációk részekkel az Alapfogalmakban; dokumentum időbélyeg frissítve

#### Specifikáció megfelelőség ellenőrzés
- **Protokoll verzió**: Ellenőrizve, hogy minden dokumentáció a legfrissebb MCP Specifikáció 2025-11-25-öt hivatkozza
- **Architektúra összehangolás**: Megerősítve a két rétegű architektúra (Adatréteg + Transzport réteg) dokumentáció pontossága
- **Primitívek dokumentálása**: Érvényesítve a szerver és kliens primitíveket (Erőforrások, Promptok, Eszközök, Sampling, Elicitation, Logging, Roots)
- **Transzport mechanizmusok**: Ellenőrizve STDIO és Streamable HTTP transzport dokumentáció pontossága
- **Biztonsági útmutatások**: Megerősítve, hogy összehangolt a jelenlegi MCP Biztonsági Legjobb Gyakorlatok dokumentációval

#### Fő MCP 2025-11-25 funkciók dokumentálva
- **OpenID Connect felfedezés**: Hitelesítő szerver felfedezése OIDC-n keresztül
- **OAuth kliens azonosító metaadat dokumentumok**: Ajánlott kliens regisztrációs mechanizmus
- **JSON Schema 2020-12**: MCP sémadefiníciók alapértelmezett dialektusa
- **SDK rétegzés rendszere**: SDK funkció támogatás és karbantartás formális követelményei
- **Irányítási szerkezet**: MCP irányításban formális munkacsoportok és érdeklődési csoportok

### Biztonsági dokumentáció jelentős frissítés (02-Security/)

#### MCP Biztonsági Csúcstalálkozó Workshop (Sherpa) integráció
- **Új gyakorlati képzési forrás**: Átfogó integráció hozzáadva a [MCP Biztonsági Csúcstalálkozó Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) dokumentációkhoz
- **Expedíciós útvonal lefedettség**: Dokumentálva a teljes tábortól táborig tartó haladás az Alaptábortól a Csúcsig
- **OWASP összehangolás**: Minden biztonsági útmutatás most már az OWASP MCP Azure Biztonsági Útmutató kockázataira mutat

#### OWASP MCP Top 10 integráció
- **Új rész**: OWASP MCP Top 10 biztonsági kockázatok táblája Azure mérséklésekkel a fő Biztonsági README-ben
- **Kockázat-alapú dokumentáció**: Frissítve a `mcp-security-controls-2025.md` az OWASP MCP kockázati hivatkozásokkal minden biztonsági területhez
- **Referencia architektúra**: Hivatkozás az OWASP MCP Azure Biztonsági Útmutató referencia architektúrájára és megvalósítási mintáira

#### Frissített biztonsági fájlok
- **README.md**: Sherpa Workshop áttekintés, expedíciós útvonal táblázat, OWASP MCP Top 10 kockázatok összefoglaló és gyakorlati képzési szekció hozzáadva
- **mcp-security-controls-2025.md**: Fejléc frissítve 2026 februárra, OWASP kockázati hivatkozások (MCP01-MCP08) hozzáadva, specifikáció verzió inkonzisztencia javítva
- **mcp-security-best-practices-2025.md**: Sherpa és OWASP forrás szekció hozzáadva, időbélyeg frissítve
- **mcp-best-practices.md**: Gyakorlati képzési szekció Sherpa és OWASP linkekkel
- **azure-content-safety-implementation.md**: OWASP MCP06 referencia, Sherpa Tábor 3 összehangolás, és további erőforrások szekció hozzáadva

#### Új forrás linkek hozzáadva
- [MCP Biztonsági Csúcstalálkozó Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Biztonsági Útmutató](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Egyéni OWASP MCP kockázati oldalak (MCP01-MCP10)

### Tananyagszintű MCP Specifikáció 2025-11-25 összhang

#### 03-as modul – Kezdés
- **SDK dokumentáció**: Go SDK hozzáadva a hivatalos SDK listához; minden SDK hivatkozás frissítve az MCP Specifikáció 2025-11-25 szerint
- **Transzport tisztázás**: STDIO és HTTP Streaming transzport leírások explicit protokoll hivatkozással frissítve

#### 04-es modul – Gyakorlati megvalósítás
- **SDK frissítések**: Go SDK hozzáadása; SDK lista frissítve a specifikáció verzió hivatkozással
- **Engedélyezési specifikáció**: MCP Engedélyezési specifikáció linkje frissítve a jelenlegi 2025-11-25 verzióra

#### 05-ös modul – Haladó témák
- **Új funkciók**: Megjegyzés a MCP Specifikáció 2025-11-25 új funkcióiról (Feladatok, Eszköz annotációk, URL mód felhívás, Roots)
- **Biztonsági források**: OWASP MCP Top 10 és Sherpa workshop linkek hozzáadva a további hivatkozásokhoz

#### 06-os modul – Közösségi hozzájárulások
- **SDK lista**: Swift és Rust SDK-k hozzáadva; specifikáció link frissítve 2025-11-25 verzióra
- **Specifikáció hivatkozás**: MCP Specifikáció link frissítve közvetlen specifikáció URL-re

#### 07-es modul – Korai alkalmazási tapasztalatok
- **Erőforrás frissítések**: MCP Specifikáció 2025-11-25 link és OWASP MCP Top 10 hozzáadva a további forrásokhoz

#### 08-as modul – Legjobb gyakorlatok
- **Specifikáció verzió**: MCP Specifikáció hivatkozás frissítve 2025-11-25 verzióra
- **Biztonsági források**: OWASP MCP Top 10 és Sherpa workshop hozzáadva a további hivatkozásokhoz

#### 10-es modul – AI munkafolyamatok hatékonyságának növelése
- **Jelvény frissítés**: MCP verzió jelvény SDK verzióról (1.9.3) a specifikáció verzióra (2025-11-25) változott
- **Erőforrás linkek**: MCP Specifikáció link frissítve; OWASP MCP Top 10 hozzáadva

#### 11-es modul – MCP szerver gyakorlati laborok
- **Specifikáció hivatkozás**: MCP Specifikáció link frissítve 2025-11-25 verzióra
- **Biztonsági források**: OWASP MCP Top 10 hozzáadva hivatalos forrásként

## 2025. december 18.
### Biztonsági Dokumentáció Frissítés – MCP Specifikáció 2025-11-25

#### MCP Biztonsági Legjobb Gyakorlatok (02-Security/mcp-best-practices.md) – Specifikáció Verzió Frissítés
- **Protokoll Verzió Frissítés**: Frissítve a legújabb MCP Specifikáció 2025-11-25 (2025. november 25-én kiadva) hivatkozására
  - Az összes specifikáció verzió hivatkozás frissítve 2025-06-18-ról 2025-11-25-re
  - A dokumentum dátum hivatkozások frissítve 2025. augusztus 18-ról 2025. december 18-ra
  - Ellenőrizve, hogy az összes specifikáció URL a jelenlegi dokumentációra mutat
- **Tartalom Ellenőrzés**: Átfogó validálás a biztonsági legjobb gyakorlatokkal a legújabb szabványok alapján
  - **Microsoft Biztonsági Megoldások**: Ellenőrizve a jelenlegi terminológia és hivatkozások a Prompt Shields (korábban „Jailbreak veszély felismerés”), Azure Content Safety, Microsoft Entra ID és Azure Key Vault esetén
  - **OAuth 2.1 Biztonság**: Megerősítve a legújabb OAuth biztonsági legjobb gyakorlatokkal való összhang
  - **OWASP Szabványok**: Ellenőrizve, hogy az OWASP Top 10 LLM-ekhez kapcsolódó hivatkozások naprakészek
  - **Azure Szolgáltatások**: Ellenőrizve az összes Microsoft Azure dokumentációs link és legjobb gyakorlat
- **Szabványoknak Való Megfelelés**: Minden hivatkozott biztonsági szabvány megerősítve, hogy aktuális
  - NIST AI Kockázatkezelési Keretrendszer
  - ISO 27001:2022
  - OAuth 2.1 Biztonsági Legjobb Gyakorlatok
  - Azure biztonsági és megfelelőségi keretrendszerek
- **Implementációs Források**: Ellenőrizve minden implementációs útmutató és erőforrás hivatkozás
  - Azure API Management hitelesítési minták
  - Microsoft Entra ID integrációs útmutatók
  - Azure Key Vault titkok kezelése
  - DevSecOps pipeline-ok és megfigyelési megoldások

### Dokumentáció Minőségbiztosítás
- **Specifikáció Megfelelés**: Biztosítva, hogy minden kötelező MCP biztonsági követelmény (MUST/MUST NOT) összhangban legyen a legújabb specifikációval
- **Források Aktualitása**: Ellenőrizve az összes külső link a Microsoft dokumentációhoz, biztonsági szabványokhoz és implementációs útmutatókhoz
- **Legjobb Gyakorlatok Lefedettsége**: Megerősítve az átfogó lefedettség az autentikáció, autorizáció, AI-specifikus fenyegetések, ellátási lánc biztonság és vállalati minták terén

## 2025. október 6.

### Kezdő Szakasz Kibővítése – Haladó Szerver Használat & Egyszerű Hitelesítés

#### Haladó Szerver Használat (03-GettingStarted/10-advanced)
- **Új Fejezet Hozzáadva**: Átfogó útmutató a haladó MCP szerver használathoz, beleértve a szokásos és az alacsony szintű szerverarchitektúrákat.
  - **Szokásos vs. Alacsony Szintű Szerver**: Részletes összehasonlítás és kódpéldák Python és TypeScript nyelven mindkét megközelítéshez.
  - **Handler-Alapú Tervezés**: Magyarázat a handler-alapú eszköz/erőforrás/prompt kezeléssel a skálázható, rugalmas szervermegvalósításokhoz.
  - **Gyakorlati Minták**: Valós helyzetek, ahol az alacsony szintű szerverminták előnyösek haladó funkciók és architektúrák esetén.

#### Egyszerű Hitelesítés (03-GettingStarted/11-simple-auth)
- **Új Fejezet Hozzáadva**: Lépésről lépésre útmutató az egyszerű hitelesítés megvalósításához MCP szervereken.
  - **Auth Fogalmak**: Egyértelmű magyarázat a hitelesítés és autorizáció között, valamint a hitelesítő adatok kezeléséről.
  - **Alap Hitelesítés Megvalósítása**: Middleware alapú hitelesítési minták Python (Starlette) és TypeScript (Express) nyelven, kódmintákkal.
  - **Fejlődés Haladó Biztonság Felé**: Útmutatás az egyszerű hitelesítésből indulva az OAuth 2.1 és RBAC felé, hivatkozásokkal a haladó biztonsági modulokra.

Ezek a kiegészítések gyakorlati, kézzelfogható útmutatást nyújtanak a robusztusabb, biztonságosabb és rugalmasabb MCP szerver megvalósítások építéséhez, hidat képezve az alapfogalmak és a haladó gyártásbeli minták között.

## 2025. szeptember 29.

### MCP Szerver Adatbázis Integráció Laborok – Átfogó Gyakorlati Tanulási Út

#### 11-MCPServerHandsOnLabs – Új Teljes Adatbázis Integrációs Tananyag
- **Teljes 13 Laborból Álló Tanulási Útvonal**: Átfogó gyakorlati tananyag hozzáadva termeléskész MCP szerverek építéséhez PostgreSQL adatbázis-integrációval
  - **Valós Alkalmazás**: Zava Retail elemzési eset használatával, vállalati szintű mintákkal
  - **Strukturált Tanulási Folyamat**:
    - **Laborok 00-03: Alapok** – Bevezetés, Alap Architektúra, Biztonság és Többbérlős környezet, Környezet beállítása
    - **Laborok 04-06: MCP Szerver Építése** – Adatbázis tervezés & séma, MCP szerver megvalósítás, eszköz fejlesztés  
    - **Laborok 07-09: Haladó Funkciók** – Szemantikus keresés integráció, tesztelés & hibakeresés, VS Code integráció
    - **Laborok 10-12: Termelés & Legjobb Gyakorlatok** – Kiadási stratégiák, megfigyelés & megfigyelhetőség, legjobb gyakorlatok & optimalizáció
  - **Vállalati Technológiák**: FastMCP keretrendszer, PostgreSQL pgvector-ral, Azure OpenAI beágyazások, Azure Container Apps, Application Insights
  - **Haladó Funkciók**: Sor szintű biztonság (RLS), szemantikus keresés, többbérlős adat-hozzáférés, vektor beágyazások, valós idejű megfigyelés

#### Terminológia Standardizálás – Modulról Laborra Átállás
- **Átfogó Dokumentáció Frissítés**: Rendszeresen frissítve minden README fájl az 11-MCPServerHandsOnLabs könyvtárban, hogy "Labor" terminológiát használjon modul helyett
  - **Szakasz Fejlécek**: Az összes 13 laborban a „Mit fed le ez a modul” kifejezés „Mit fed le ez a labor” formára cserélve
  - **Tartalom Leírás**: „Ez a modul biztosít…” helyett „Ez a labor biztosít…” a teljes dokumentációban
  - **Tanulási Célok**: „A modul végére…” módosítva „A labor végére…”
  - **Navigációs Hivatkozások**: Az összes „Modul XX:” hivatkozás átváltva „Labor XX:” formára kereszthivatkozásokban és navigációban
  - **Befejezési Követés**: „A modul befejezése után…” helyett „A labor befejezése után…”
  - **Műszaki Hivatkozások Megőrzése**: Python modul hivatkozások változatlanok maradtak konfigurációs fájlokban (pl. `"module": "mcp_server.main"`)

#### Tanulmányi Útmutató Fejlesztése (study_guide.md)
- **Vizualizált Tananyag Térkép**: Új „11. Adatbázis Integrációs Laborok” szakasz hozzáadva, átfogó labor struktúra vizualizációval
- **Tárolóstruktúra**: Tíz helyett tizenegy fő szakasz, részletes 11-MCPServerHandsOnLabs leírással
- **Tanulási Útvonal Útmutató**: Navigációs utasítások bővítve a 00-11 szakaszok feldolgozására
- **Technológiai Lefedettség**: FastMCP, PostgreSQL, Azure szolgáltatások integráció részletezése
- **Tanulási Eredmények**: Kiemelve a termeléskész szerver fejlesztést, adatbázis integrációs mintákat és vállalati biztonságot

#### Fő README Struktúra Fejlesztése
- **Labor-alapú Terminológia**: Az 11-MCPServerHandsOnLabs fő README.md fájl modulos megnevezése laborra váltva egységesen
- **Tanulási Útvonal Szervezés**: Világos haladás az alapfogalmakon át a haladó implementációig és termelési kiadásig
- **Valós Világra Fókuszálás**: Gyakorlati, kézzel fogható tanulás hangsúlyozva, vállalati mintákkal és technológiákkal

### Dokumentáció Minőség- és Következetesség Javítások
- **Gyakorlati Tanulás Hangsúlyozása**: Egész dokumentáción át erősített gyakorlati, labor-alapú megközelítés
- **Vállalati Mintákra Fókusz**: Kiemelve termelésképes megvalósításokat és vállalati biztonsági szempontokat
- **Technológiai Integráció**: Átfogó lefedettség a modern Azure szolgáltatásokról és AI integrációs mintákról
- **Tanulási Folyamat**: Világos, strukturált útvonal az alapfogalmaktól a termelési kiadásig

## 2025. szeptember 26.

### Esettanulmányok Fejlesztése – GitHub MCP Registry Integráció

#### Esettanulmányok (09-CaseStudy/) – Ökoszisztéma Fejlesztési Fókusz
- **README.md**: Jelentős bővítés átfogó GitHub MCP Registry esettanulmánnyal
  - **GitHub MCP Registry Esettanulmány**: Új átfogó esettanulmány a GitHub MCP Registry 2025 szeptemberi indulásáról
    - **Probléma Elemzés**: Részletes vizsgálat a széttagolt MCP szerver felfedezés és telepítés kihívásairól
    - **Megoldási Architektúra**: GitHub központosított regisztrációs megközelítése egykattintásos VS Code telepítéssel
    - **Üzleti Hatás**: Mérhető javulás a fejlesztői onboarding és termelékenység terén
    - **Stratégiai Érték**: Moduláris ügynök telepítés és eszközök közötti interoperabilitás fókuszban
    - **Ökoszisztéma Fejlődés**: Alapvető platformként pozicionálás az ügynöki integrációkhoz
  - **Esettanulmány Struktúra Fejlesztés**: Az összes hét esettanulmány frissítve következetes formázással és részletes leírással
    - Azure AI Utazási Ügynökök: Többügynökös szervezés hangsúlyozása
    - Azure DevOps Integráció: Munkafolyamat automatizálás fókusz
    - Valós Idejű Dokumentum Lekérés: Python konzol kliens megvalósítás
    - Interaktív Tanulási Terv Generátor: Chainlit beszélgetős webalkalmazás
    - In-Szerkesztő Dokumentáció: VS Code és GitHub Copilot integráció
    - Azure API Management: Vállalati API integrációs minták
    - GitHub MCP Registry: Ökoszisztéma fejlesztés és közösségi platform
  - **Átfogó Záró Rész**: Átírt összegzés szakasz kiemelve a hét esettanulmányt, mely számos MCP megvalósítási dimenziót lefed
    - Vállalati Integráció, Többügynökös Szervezés, Fejlesztői Termelékenység
    - Ökoszisztéma Fejlesztés, Oktatási Alkalmazások kategorizációja
    - Bővített betekintések az architekturális mintákba, implementációs stratégiákba és legjobb gyakorlatokba
    - Hangsúly az MCP mint érett, termeléskész protokoll

#### Tanulmányi Útmutató Frissítések (study_guide.md)
- **Vizualizált Tananyag Térkép**: Frissítve a gondolattérkép, hogy tartalmazza a GitHub MCP Registry-t az Esettanulmányok szekcióban
- **Esettanulmányok Leírása**: Bővítve általános leírásokról részletes bontásra hét átfogó esettanulmányra
- **Tároló Struktúra**: A 10-es szakasz frissítve, hogy tükrözze az átfogó esettanulmány lefedettséget részletes megvalósításokkal
- **Változásnapló Integráció**: Hozzáadva 2025. szeptember 26-i bejegyzés a GitHub MCP Registry hozzáadásáról és esettanulmány fejlesztésekről
- **Dátum Frissítések**: Lábléc időbélyeg frissítve a legfrissebb módosításra (2025. szeptember 26.)

### Dokumentáció Minőség Javítások
- **Következetesség Fejlesztése**: Egységes esettanulmány formázás és szerkezet a hét példa között
- **Átfogó Lefedettség**: Esettanulmányok lefedik a vállalati, fejlesztői termelékenységi és ökoszisztéma fejlesztési forgatókönyveket
- **Stratégiai Pozicionálás**: Kiemelt hangsúly az MCP alapvető platformként való szerepére az ügynöki rendszerek telepítésében
- **Forrás Integráció**: Bővített további erőforrások GitHub MCP Registry linkkel

## 2025. szeptember 15.

### Haladó Témakörök Kibővítése – Egyedi Transzportok & Kontextus Mérnökség

#### MCP Egyedi Transzportok (05-AdvancedTopics/mcp-transport/) – Új Haladó Implementációs Útmutató
- **README.md**: Teljes implementációs útmutató egyedi MCP transzport mechanizmusokra
  - **Azure Event Grid Transzport**: Átfogó szerver nélküli eseményvezérelt transzport megvalósítás
    - C#, TypeScript és Python példák Azure Functions integrációval
    - Eseményvezérelt architektúra minták skálázható MCP megoldásokhoz
    - Webhook fogadók és push-alapú üzenetkezelés
  - **Azure Event Hubs Transzport**: Nagy átviteli sebességű streaming transzport megvalósítás
    - Valós idejű streaming képességek alacsony késleltetésű forgatókönyvekhez
    - Partícionálási stratégiák és checkpoint kezelése
    - Üzenet csoportosítás és teljesítmény optimalizálás
  - **Vállalati Integrációs Minták**: Termeléskész architekturális példák
    - Elosztott MCP feldolgozás több Azure Functions között
    - Hibrid transzport architektúrák több transzport típus kombinációjával
    - Üzenet tartósság, megbízhatóság és hiba kezelés stratégiák
  - **Biztonság & Megfigyelés**: Azure Key Vault integráció és megfigyelő minták
    - Kezelt identitás autentikáció és legkisebb jogosultság elv
    - Application Insights telemetria és teljesítmény monitorozás
    - áramkör megszakítók és hibabiztossági minták
  - **Tesztelési Keretrendszerek**: Átfogó tesztelési stratégiák egyedi transzportokhoz
    - Egység tesztelés teszt dupla és mock keretrendszerekkel
    - Integrációs tesztelés Azure Test Containers használatával
    - Teljesítmény- és terheléses tesztelési szempontok

#### Kontextus Mérnökség (05-AdvancedTopics/mcp-contextengineering/) – Feltörekvő AI Diszciplína
- **README.md**: Átfogó bemutató a kontextus mérnökség mint feltörekvő terület
  - **Alapelvek**: Teljes körű kontextus megosztás, cselekvési döntések tudatossága és kontextus ablak kezelés
  - **MCP Protokoll Összhang**: Hogyan kezeli az MCP a kontextus mérnökségi kihívásokat
    - Kontextus ablak korlátok és progresszív betöltési stratégiák
    - Relevancia meghatározás és dinamikus kontextus lekérés
    - Többmodalitású kontextus kezelés és biztonsági szempontok
  - **Implementációs Megközelítések**: Egyszálú vs. többügynök architektúrák
    - Kontextus darabolás és priorizálási technikák
    - Progresszív kontextus betöltés és tömörítési stratégiák
    - Rétegezett kontextus megközelítések és lekérés optimalizáció
  - **Mérési Keretrendszer**: Feltörekvő metrikák a kontextus hatékonyság mérésére
    - Bemeneti hatékonyság, teljesítmény, minőség és felhasználói élmény szempontok
    - Kísérleti megközelítések a kontextus optimalizációra
    - Hibaanalízis és fejlesztési módszertanok

#### Tananyag Navigáció Frissítések (README.md)
- **Fejlesztett Modul Struktúra**: A tananyag táblázat frissítve a új haladó témákkal
  - Kontextus Mérnökség (5.14) és Egyedi Transzport (5.15) hozzáadva
  - Következetes formázás és navigációs hivatkozások minden modulon át
  - Leírások frissítve a jelenlegi tartalomkörnek megfelelően

### Könyvtár Struktúra Fejlesztések
- **Névváltoztatás Egységesítése**: „mcp transport” átnevezve „mcp-transport” a más haladó témakörök könyvtáraihoz igazítva
- **Tartalom Rendszerezés**: Minden 05-AdvancedTopics könyvtár most egységes névformátumot követ (mcp-[téma])

### Dokumentáció Minőség Javítások
- **MCP Specifikáció Összhang**: Minden új tartalom a jelenlegi MCP Specifikáció 2025-06-18-ra hivatkozik
- **Többnyelvű Példák**: Átfogó kódpéldák C#, TypeScript és Python nyelven
- **Vállalati Fókusz**: Termeléskész minták és Azure felhő integráció az egész dokumentációban
- **Vizualizált Dokumentáció**: Mermaid diagramok az architektúra és folyamatábrázolásra

## 2025. augusztus 18.

### Dokumentáció Átfogó Frissítés – MCP 2025-06-18 Szabványok

#### MCP Biztonsági Legjobb Gyakorlatok (02-Security/) – Teljes Korszerűsítés
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Teljes átírás az MCP specifikáció 2025-06-18 szerinti összhangban  
  - **Kötelező követelmények**: Hivatalos specifikációból származó egyértelmű KELL / NEM KELL követelmények hozzáadva, jól látható vizuális jelzésekkel  
  - **12 alapvető biztonsági gyakorlat**: Átszerkesztve a 15 tételes listából átfogó biztonsági területekké  
    - Token biztonság és hitelesítés külső identitásszolgáltató integrációval  
    - Munkamenet-kezelés és szállításbiztonság kriptográfiai követelményekkel  
    - Mesterséges intelligenciára specializált fenyegetések elleni védelem Microsoft Prompt Shields integrációval  
    - Hozzáférés-vezérlés és jogosultságok a legkisebb privilégium elvével  
    - Tartalombiztonság és megfigyelés Azure Content Safety integrációval  
    - Ellátási lánc biztonsága átfogó komponensellenőrzéssel  
    - OAuth biztonság és Confused Deputy támadások elleni védelem PKCE implementációval  
    - Eseménykezelés és helyreállítás automatizált képességekkel  
    - Megfelelőség és irányítás szabályozói összhangban  
    - Fejlett biztonsági vezérlők nulladik bizalom architektúrával  
    - Microsoft biztonsági ökoszisztéma integráció átfogó megoldásokkal  
    - Folyamatos biztonsági fejlődés adaptív gyakorlatokkal  
  - **Microsoft biztonsági megoldások**: Fejlettebb integrációs útmutató Prompt Shields, Azure Content Safety, Entra ID és GitHub Advanced Security-hez  
  - **Megvalósítási erőforrások**: Átfogó erőforrás hivatkozások kategorizálva Hivatalos MCP dokumentáció, Microsoft biztonsági megoldások, biztonsági szabványok és implementációs útmutatók szerint  

#### Fejlett biztonsági vezérlők (02-Security/) – Vállalati megvalósítás  
- **MCP-SECURITY-CONTROLS-2025.md**: Teljes átalakítás vállalati szintű biztonsági keretrendszerrel  
  - **9 átfogó biztonsági terület**: Bővítve alapvezérlőkről részletes vállalati keretrendszerre  
    - Fejlett hitelesítés és engedélyezés Microsoft Entra ID integrációval  
    - Token biztonság és anti-passthrough vezérlők átfogó validálással  
    - Munkamenet biztonsági vezérlők eltérítési védelemmel  
    - Mesterséges intelligenciára specializált biztonsági vezérlők prompt injekció és eszközmérgezés elleni védelemmel  
    - Confused Deputy támadás elleni védelem OAuth proxy biztonsággal  
    - Eszközvégrehajtás biztonság sandboxinggal és izolációval  
    - Ellátási lánc biztonsági vezérlők függőségellenőrzéssel  
    - Megfigyelési és észlelési vezérlők SIEM integrációval  
    - Eseménykezelés és helyreállítás automatizált képességekkel  
  - **Megvalósítási példák**: Részletes YAML konfigurációs blokkokkal és kódpéldákkal kiegészítve  
  - **Microsoft megoldás integráció**: Átfogó leírás Azure biztonsági szolgáltatásokról, GitHub Advanced Security-ről és vállalati identitáskezelésről  

#### Fejlett témák biztonság (05-AdvancedTopics/mcp-security/) – Termelésre kész megvalósítás  
- **README.md**: Teljes átírás vállalati biztonsági megvalósításra  
  - **Aktuális specifikáció szerinti összhang**: Frissítve MCP specifikáció 2025-06-18 szerint, kötelező biztonsági követelményekkel  
  - **Fejlett hitelesítés**: Microsoft Entra ID integráció átfogó .NET és Java Spring Security példákkal  
  - **AI biztonsági integráció**: Microsoft Prompt Shields és Azure Content Safety implementálás részletes Python példákkal  
  - **Fejlett fenyegetéscsökkentés**: Átfogó megvalósítási példák  
    - Confused Deputy elleni védelem PKCE-vel és felhasználói hozzájárulás validálással  
    - Token passthrough megelőzés audience validálással és biztonságos token kezeléssel  
    - Munkamenet eltérítés elleni védelem kriptográfiai kötés és viselkedéselemzéssel  
  - **Vállalati biztonsági integráció**: Azure Application Insights megfigyelés, fenyegetésészlelési folyamatok és ellátási lánc biztonság  
  - **Megvalósítási ellenőrzőlista**: Egyértelmű kötelező és ajánlott biztonsági vezérlők Microsoft biztonsági ökoszisztéma előnyeivel  

### Dokumentáció minősége és szabványokhoz igazítás  
- **Specifikáció hivatkozások**: Minden hivatkozás frissítve az aktuális MCP specifikáció 2025-06-18 szerint  
- **Microsoft biztonsági ökoszisztéma**: Integrációs útmutatás bővítve minden biztonsági dokumentációban  
- **Gyakorlati megvalósítás**: Részletes kódpéldák .NET, Java és Python nyelveken, vállalati mintákkal  
- **Erőforrások rendszerezése**: Hivatalos dokumentációk, biztonsági szabványok, kutatás, Microsoft megoldások és megvalósítási útmutatók kategorizálása  
- **Vizuális jelzések**: Egyértelmű megkülönböztetés kötelező követelmények és ajánlott gyakorlatok között  

#### Alapfogalmak (01-CoreConcepts/) – Teljes modernizáció  
- **Protokoll verzió frissítés**: Hivatkozás a jelenlegi MCP specifikációra 2025-06-18, dátumalapú verzió formátummal (ÉÉÉÉ-HH-NN)  
- **Architektúra finomítás**: Részletesebb leírás Hostokról, kliensekről és szerverekről a jelenlegi MCP architektúra minták szerint  
  - Hostok most világosan definiáltak mint mesterséges intelligencia alkalmazások, amelyek több MCP kliens kapcsolatot koordinálnak  
  - Kliens leírás mint protokollkapcsolók, amelyek egy-egy szerverrel tartanak kapcsolatot  
  - Szerverek fejlesztve lokális és távoli telepítési forgatókönyvekkel  
- **Primitivek átszervezése**: Teljes áttekintés szerver és kliens primítvek terén  
  - Szerver primítvek: Erőforrások (adatforrások), Promptok (sablonok), Eszközök (végrehajtható funkciók) részletes magyarázattal és példákkal  
  - Kliens primítvek: Mintavétel (LLM befejezések), Kiváltás (felhasználói bemenet), Naplózás (hibakeresés/megfigyelés)  
  - Frissítve az aktuális discovery (`*/list`), lekérés (`*/get`) és végrehajtás (`*/call`) módszermintákkal  
- **Protokoll architektúra**: Két szintű architektúra modell bevezetése  
  - Adatréteg: JSON-RPC 2.0 alapú életciklus-kezeléssel és primitivekkel  
  - Szállítási réteg: STDIO (helyi) és streamelhető HTTP SSE-vel (távoli) szállítási mechanizmusok  
- **Biztonsági keretrendszer**: Átfogó biztonsági elvek, beleértve az explicite felhasználói hozzájárulást, adatvédelmet, eszközvégrehajtás biztonságát és szállítási réteg védelmét  
- **Kommunikációs minták**: Frissített protokoll üzenetek az inicializáció, felfedezés, végrehajtás és értesítés folyamatainak megjelenítésére  
- **Kódpéldák**: Többnyelvű példák (.NET, Java, Python, JavaScript) frissítve az aktuális MCP SDK mintáknak megfelelően  

#### Biztonság (02-Security/) – Átfogó biztonsági átalakítás  
- **Szabványoknak való megfelelés**: Teljes összhang az MCP specifikáció 2025-06-18 biztonsági követelményeivel  
- **Hitelesítés fejlődése**: Dokumentált evolúció egyedi OAuth szerverektől külső identitásszolgáltató delegációig (Microsoft Entra ID)  
- **Mesterséges intelligenciára specifikus fenyegetés-elemzés**: Fejlettebb lefedettség a modern MI támadási vektorokkal  
  - Részletes prompt injekciós támadás forgatókönyvek valós példákkal  
  - Eszközmérgezési mechanizmusok és "rug pull" támadási minták  
  - Kontextusablak mérgezés és modellezési zavarkeltő támadások  
- **Microsoft MI biztonsági megoldások**: Átfogó ismertetése a Microsoft biztonsági ökoszisztémájának  
  - AI Prompt Shields fejlett detektálással, kiemelésekkel és elválasztótechnikákkal  
  - Azure Content Safety integrációs minták  
  - GitHub Advanced Security az ellátási lánc védelméhez  
- **Fejlett fenyegetéscsökkentő vezérlők**: Részletesen  
  - Munkamenet eltérítési támadások MCP specifikus mintákkal, kriptográfiai munkamenet azonosító követelménnyel  
  - Confused Deputy problémák MCP proxy környezetben explitit hozzájárulási követelményekkel  
  - Token passthrough sebezhetőségek kötelező validálási vezérlőkkel  
- **Ellátási lánc biztonság**: Kibővített MI ellátási lánc lefedettség alapmodellekkel, embedding szolgáltatásokkal, kontextus szolgáltatókkal és harmadik fél API-kkal  
- **Alapbiztonság**: Fejlesztett vállalati biztonsági minták integrációja, beleértve a nulladik bizalom architektúrát és Microsoft biztonsági ökoszisztémát  
- **Erőforrás rendszerezés**: Átfogó hivatkozások kategorizálva típusaik szerint (Hivatalos dokumentációk, szabványok, kutatás, Microsoft megoldások, megvalósítási útmutatók)  

### Dokumentáció minőségi fejlesztések  
- **Strukturált tanulási célok**: Fejlesztett, specifikus, cselekvésre ösztönző tanulási eredmények  
- **Kereszt-hivatkozások**: Hivatkozások összekapcsolva kapcsolódó biztonsági és alapfogalmi témákkal  
- **Aktuális információk**: Minden dátum és specifikáció link frissítve jelenlegi szabványokra  
- **Megvalósítási útmutatások**: Részletes, végrehajtható iránymutatások mindkét szakaszban  

## 2025. július 16.

### README és navigáció fejlesztések  
- Teljesen áttervezett tananyag navigáció a README.md-ben  
- `<details>` tagek helyett táblázatalapú, jobban hozzáférhető formátum  
- Alternatív elrendezési opciók létrehozása új "alternative_layouts" mappában  
- Kártya-alapú, lapozós és összehúzható navigációs példák hozzáadása  
- Tárolószerkezet szakasz frissítése minden legújabb fájllal  
- "Hogyan használjuk ezt a tananyagot" rész fejlesztése egyértelmű javaslatokkal  
- MCP specifikáció linkek frissítve helyes URL-ekre  
- Kontextus-mérnökség szakasz (5.14) hozzáadása a tananyagszerkezethez  

### Tanulási útmutató frissítések  
- Teljes útmutató felülvizsgálat igazítva az aktuális tárolószerkezethez  
- Új szakaszok hozzáadva MCP kliensek és eszközök, valamint népszerű MCP szerverek témában  
- Vizualizált tananyagtérkép pontos frissítése minden témával  
- Fejlett témák leírásainak bővítése minden speciális területre  
- Esettanulmány szakasz aktualizálása valós példákkal  
- Ez a részletes változásnapló hozzáadva  

### Közösségi hozzájárulások (06-CommunityContributions/)  
- Részletes információ MCP szerverekről képgeneráláshoz  
- Átfogó szakasz Claude használatáról VSCode-ban  
- Cline terminál kliens telepítési és használati útmutatója  
- MCP kliens szakasz frissítése minden népszerű klienssel  
- Hozzájárulási példák pontosabb kódmintákkal kiegészítve  

### Fejlett témák (05-AdvancedTopics/)  
- Minden speciális témaköri mappa szervezése egységes névhasználattal  
- Kontextus-mérnökségi anyagok és példák hozzáadása  
- Foundry agent integrációs dokumentáció  
- Entra ID biztonsági integráció dokumentáció bővítése  

## 2025. június 11.

### Első létrehozás  
- MCP for Beginners tananyag első verziójának kiadása  
- Minden 10 fő szakasz alapstruktúrájának létrehozása  
- Vizualizált tananyagtérkép megvalósítása a navigációhoz  
- Kezdeti mintaprojektek hozzáadása több programozási nyelven  

### Kezdő lépések (03-GettingStarted/)  
- Első szerver megvalósítási példák létrehozása  
- Kliens fejlesztési iránymutatások hozzáadva  
- LLM kliens integrációs útmutató mellékelve  
- VS Code integráció dokumentációja  
- Server-Sent Events (SSE) szerver példák implementálva  

### Alapfogalmak (01-CoreConcepts/)  
- Részletes magyarázat a kliens-szerver architektúráról  
- Dokumentáció a kulcsfontosságú protokoll komponensekről  
- Üzenetküldési minták az MCP-ben dokumentálva  

## 2025. május 23.

### Tárolószerkezet  
- Alap mappa struktúra létrehozva a tárban  
- README fájlok létrehozása minden fő szakaszban  
- Fordítási infrastruktúra beállítása  
- Képi anyagok és diagramok hozzáadása  

### Dokumentáció  
- Kezdeti README.md létrehozva tananyag áttekintéssel  
- CODE_OF_CONDUCT.md és SECURITY.md dokumentumok hozzáadva  
- SUPPORT.md beállítása segítségkéréshez  
- Előzetes tanulási útmutató struktúra megalkotva  

## 2025. április 15.

### Tervezés és keretrendszer  
- MCP for Beginners tananyag kezdeti tervezése  
- Tanulási célok és célközönség meghatározása  
- A tananyag 10 szakaszos felépítésének vázlata  
- Fogalmi keretrendszer kidolgozása példákhoz és esettanulmányokhoz  
- Kezdeti prototípus példák készítése kulcsfogalmakhoz

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült fordítás. Bár igyekszünk pontosak lenni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum annak anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakember által végzett emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
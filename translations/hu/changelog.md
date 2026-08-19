# Változásnapló: MCP kezdőknek tananyag

Ez a dokumentum a Model Context Protocol (MCP) kezdőknek tananyagban történt minden jelentős változás nyilvántartására szolgál. A változásokat fordított időrendi sorrendben dokumentáljuk (a legújabb változások vannak elöl).

## 2026. július 29.

### Új 08-as modulhoz társított anyag: Megbízhatósági mellékműveletek és biztonságos újrapróbálkozások

Hozzáadtunk egy gyártósemleges társítható leckét az MCP eszközökhöz, amelyek valós
hatásokat hoznak létre, összhangban a végleges `2026-07-28` szabványtervvel.

- **Új**: A [megbízhatósági mellékműveletek társított leckéje][reliability-sidecar]
  egy támogató jegyes történetet, két Mermaid diagramot és egy újrapróbálkozási döntési
  folyamatot használ a stabil működés kulcsainak, atomikus duplikált elfogadásnak,
  harmonizációnak, bizonyítékoknak és a Feladatok kiterjesztési határának magyarázatára.
- **Új**: Egy standard könyvtári Python és SQLite hibabeinjektálási gyakorlat
  különálló műveleti és jegytárolókat használ annak bemutatására, hogy egy válasz elveszik,
  miután egy külső hatás elköteleződik. Hat determinisztikus teszt fedi le a naiv
  duplikációt, védett újraindítási helyreállítást, terhelésütközéseket, gyorsítótárazott eredményeket,
  aktív követeléseket és párhuzamos duplikált elfogadást.
- **Frissítve**: A 08-as modul most már csatolja a társított leckét, azonosítja a
  végleges `2026-07-28` állapotmentes kérés modellt, elkülöníti az OpenTelemetry
  megfigyelhetőségét a már elavult MCP naplózási funkciótól, és példaként korlátozza az
  általános újrapróbálkozást csak olvasási műveletekre.
- **Opcionális**: A lecke a hordozható fogalmakat egy címkézett közösségi implementációhoz
  köti anélkül, hogy a hosztolt szolgáltatás vagy hálózati hívás az
  gyakorlati feladat részévé válna.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026. július 2.

### Új lecke: A 2026-07-28 MCP szabványterv kiadásra jelölt változata

Hozzáadtunk lefedettséget a közelgő `2026-07-28` MCP szabványterv kiadásra jelölt változatához (bejelentve 2026. május 21-én; végleges kiadás ütemezve 2026. július 28-ra), összefoglalva az [hivatalos bejelentő blogposztból](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). A tananyag alapja továbbra is az **MCP szabvány 2025-11-25**, amíg az új verzió megjelenik, így ez előretekintő útmutatóként szolgál, nem pedig a meglévő leckék átírásaként.

- **Új**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — egy teljes lecke az állapotmentes protokoll magjáról (az `initialize` kézfogás és az `Mcp-Session-Id` eltávolítása), az új `Mcp-Method`/`Mcp-Name` útválasztó fejlécekről, `ttlMs`/`cacheScope` gyorsítótárazási metaadatokról, W3C Trace Context-ről a `_meta` alatt, a formális Kiterjesztés keretrendszerről (MCP alkalmazások és az új Feladatok kiterjesztés), hat jogosultságmegerősítő SEP-ről, a Gyökerek/Mintavétel/Naplózás elavulásáról, és az eszköz séma teljes JSON Schema 2020-12-re való áttéréséről.
- **Frissítve** előretekintő hivatkozásokkal, amelyek az új leckéhez kapcsolódnak:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokoll verzió megjegyzés, Mintavétel/Gyökerek/Naplózás/Feladatok szakaszok, és "Mi következik"
  - [02-Security/README.md](./02-Security/README.md): jogosultság megerősítés hivatkozás
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): állapotmentes szállítási hivatkozás
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): mintavétel elavulás hivatkozás
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): naplózás elavulás és Feladatok kiterjesztési hivatkozás
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): állapotmentes/munkamenet útválasztási hivatkozás
  - [README.md](./README.md): Az előretekintés megjegyzése a szabvány szakaszban és egy új `1.1` bejegyzés a tananyag modul táblázatban
  - [study_guide.md](./study_guide.md): előretekintő pont a Core Concepts áttekintés alatt és dátumozott kiegészítő megjegyzés
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): hivatkozás az `mcp-session-id` szállítási térképre az állapotmentes kérés modell előtti résznél
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): modul áttekintés a Gyökér kontextusok/Mintavételek elavulásáról és a Feladatok kiterjesztésről
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): jogosultság megerősítés hivatkozás

## 2026. június 24.

### Új lecke: MCP használata a Copilot alkalmazásban

- [Eszközökkel kapcsolatos rész](./12-tooling/README.md) Hozzáadott eszköz rész.
- [MCP a Copilot alkalmazásban](./12-tooling/01-copilot-app/README.md)

## 2026. június 16.

### MCP szabvány összhang és minta érvényesítés

Érvényesítettük a tananyagot a jelenlegi **MCP szabvány 2025-11-25** és a legújabb hivatalos SDK-k szerint, majd korrigáltuk a maradék elavult szabvány hivatkozásokat és megerősítettük, hogy a fő minták még mindig épülnek és futnak.

#### Szabvány verzió korrekciók (2025-06-18 / 2025-03-26 → 2025-11-25)

Frissítettük az angol tartalmat, ahol még azt állította, hogy egy korábbi szabvány revízió a *jelenlegi/legfrissebb* szabvány, és átirányítottuk a linkeket a kanonikus `modelcontextprotocol.io` szabvány útvonalakra:
- **05-AdvancedTopics/mcp-security/README.md**: Frissítettük a "Jelenlegi szabvány" bannert, bevezetőt, a biztonsági alapelvek fejléceit, kötelező követelményeket, Microsoft Entra ID szakaszt, Hivatkozások és Források linkjeit, valamint a záró biztonsági értesítést (8 hivatkozás) a 2025-11-25-re
- **05-AdvancedTopics/mcp-transport/README.md**: Frissítettük a További erőforrások szabvány linket és a "Jelenlegi szabvány" bannert a 2025-11-25-re
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Kicseréltük az elavult `2025-03-26` biztonsági és megbízhatósági linket a jelenlegi 2025-11-25 biztonsági legjobb gyakorlat oldalra
- **03-GettingStarted/14-sampling/README.md**: Frissítettük a hivatalos mintavételi dokumentum linkjét a 2025-11-25-re
- **03-GettingStarted/05-stdio-server/README.md**: Frissítettük a jelen időben lévő "jelenlegi MCP szabvány" hivatkozást és a További erőforrások szabvány linket a 2025-11-25-re (a történelmi SSE-elavulási megjegyzések változatlanok a pontosság miatt)

#### Minták érvényesítése a jelenlegi SDK-kon

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` megoldotta a `@modelcontextprotocol/sdk@1.29.0` csomagot; `tsc --noEmit` sikeresen lefutott típushibák nélkül — a meglévő `McpServer`/`StdioServerTransport` API-k érvényesek maradnak
- **Python (03-GettingStarted/01-first-server/solution/python)**: Ellenőriztük izolált `.venv` környezetben a `mcp[cli]` (1.27.2) csomaggal; `py_compile` sikeres volt és a `FastMCP.list_tools()` helyesen visszaadta a `add` és `subtract` eszközöket
- Megerősítettük, hogy minden minta `@modelcontextprotocol/sdk` verzióköre (`>=1.26.0` / `^1.26.0` / `^1.27.0`) zökkenőmentesen megoldódik a jelenlegi `1.29.0` verzióra törő API változások nélkül

#### Függőség verzió felzárkóztatás (lezárva verziórések)

Frissítettük az elavult SDK veremeket, hogy minden minta kövesse a jelenlegi MCP kiadást, megfelelve a teljes adattár szabványának:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Frissítettük a `@modelcontextprotocol/sdk` verzióját `^1.8.0`-ról `>=1.26.0`-ra, továbbá frissítettük az elavult `"updated for MCP 2025-06-18"` csomag leírást `"aligned with MCP Specification 2025-11-25"`-re
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** és **lab4/code/github_mcp_server/pyproject.toml**: Frissítettük az pontos pin `mcp==1.23.0`-ról `mcp>=1.26.0`-ra; mindkét `uv.lock` fájlt újrageneráltuk (`uv lock`), így a lock fájlok most a jelenlegi `mcp 1.27.2` verzióra oldódnak és szinkronban maradnak a manifestekkel

#### Tananyag hiányelemzés — legújabb szabvány funkciók lefedése

Ellenőriztük, hogy a tananyag már lefedi az összes MCP 2025-11-25-ben bevezetett/bővített primitívet, így nincs tartalmi hiány:
- **Mintavétel**: Lecke 03-GettingStarted/14-sampling és 05-AdvancedTopics/mcp-sampling
- **Elicitation (beléértve URL módot is)**: Dokumentálva az 01-CoreConcepts és 05-AdvancedTopics/mcp-protocol-features tananyagokban
- **Gyökerek**: Dokumentálva a 00-Introduction, 01-CoreConcepts, és 05-AdvancedTopics/mcp-root-contexts tananyagokban
- **Feladatok (kísérleti, hosszú lefutású műveletek)**: Dokumentálva az 01-CoreConcepts és 05-AdvancedTopics/mcp-protocol-features tananyagokban
- **Eszköz annotációk** (`readOnlyHint` / `destructiveHint`): Dokumentálva az 01-CoreConcepts és 05-AdvancedTopics/mcp-protocol-features tananyagokban

### Biztonsági megerősítés és függőség sérülékenységek javítása

Teljes biztonsági átvilágítást végeztünk minden függőségi manifesten és minta forráskódon, majd javítottuk az összes jelentett npm figyelmeztetést és egy kód szintű problémát. A javítások után az `npm audit` minden áttekintett könyvtárban **0 sérülékenységet** jelent.

#### npm függőség sérülékenységek (áttételes) — Javítva

Átvizsgáltuk az összes 15 beadott `package-lock.json` fájlt. A sérülékenységek az MCP Inspector fejlesztő eszköz, az OpenAI kliens és az MCP SDK által behúzott áttételes függőségekhez kötöttek; mind most megoldott anélkül, hogy a minták megsérülnének:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** és **lab3/code/weather_mcp/inspector**: Frissítettük a `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), amely megszüntette a bundle-ölt `ajv`, `brace-expansion`, `diff`, `path-to-regexp` és `ws` figyelmeztetéseket. Hozzáadtunk egy npm `overrides` bejegyzést a javított `shell-quote@1.8.4` kikényszerítésére az utolsó kritikus figyelmeztetés eltávolításához, amelyet a `concurrently` vitt; mindkét lock fájlt újrageneráltuk (most 0 sérülékenység)
- **03-GettingStarted/samples/typescript**: `npm audit fix` javította az áttételes `qs` (közepes) csomagot egy javított kiadásra
- **03-GettingStarted/samples/javascript**: `npm audit fix` javította az áttételes `hono` (közepes) csomagot egy javított kiadásra
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` javította az áttételes `form-data` (magas) csomagot egy javított kiadásra
- **03-GettingStarted/11-simple-auth/solution/typescript**: Elkészítettük a hiányzó `package-lock.json` fájlt, így a projekt reprodukálható és auditálható (0 sérülékenység)

#### Kód szintű biztonsági javítás (OWASP A03: Injekció)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Eltávolítottuk a `shell=True` beállítást az `open_in_vscode` eszközből. A korábbi `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` lehetővé tette, hogy a shell metakarakterek egy mappanévben a `cmd.exe` által értelmezve legyenek (parancs befecskendezési vektor). Most közvetlenül a feloldott `Code.exe`-t indítja el a mappával argumentumként — shell nélkül — ami funkcionálisan ekvivalens és biztonságos

#### Python függőség audit

- Átvizsgáltunk minden Python követelmény halmazt `pip-audit` segítségével. A `05-AdvancedTopics` és `03-GettingStarted/samples/python` nem jelzett ismert sérülékenységet (az ő `mcp` / `httpx` / `pydantic` / `python-dotenv` verziótartományaik a jelenlegi javított kiadásokra mutatnak)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: A `pip-audit` jelezte a áttételes függőség **`werkzeug` 3.1.1** esetén három `safe_join` Windows eszköznév DoS figyelmeztetést — `CVE-2025-66221`, `CVE-2026-21860`, és `CVE-2026-27199` (mind javítva 3.1.6-ban). Megadtunk egy explicit biztonsági tűrést `werkzeug>=3.1.6` hogy a javított kiadás megoldódjon; ellenőriztük, hogy a feltétel zökkenőmentesen megoldódik a `chainlit` / `mcp` / `semantic-kernel` veremmel

### Terméknév újra márkázás

Frissítettük az összes tananyagtartalmat, hogy tükrözze a Microsoft termék újra márkázását:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Frissítettük a Discord közösségi linket

- **AGENTS.md**: Frissített Discord szerver hivatkozás
- **README.md**: Frissített technológiai ökoszisztéma hivatkozások
- **study_guide.md**: Frissített esettanulmány hivatkozások
- **05-AdvancedTopics/README.md**: Frissített 5.13 modul cím és leírás
- **05-AdvancedTopics/mcp-integration/README.md**: Frissített szakaszfejléc és leírás
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Teljes modul cím és tartalom frissítés
- **05-AdvancedTopics/mcp-security-entra/README.md**: Frissített kereszthivatkozás link
- **07-LessonsfromEarlyAdoption/README.md**: Frissített esettanulmány hivatkozások
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Frissített 9. szakasz fejléc, jelvények és képességek
- **08-BestPractices/README.md**: Frissített Discord közösségi link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Frissített Discord csatorna hivatkozás
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Frissített modell telepítési hivatkozás
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Frissített AI Szolgáltatások táblázat
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Frissített erőforrás hivatkozások

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension a VS Code-hoz
- **README.md**: Frissített fő tananyag hivatkozások
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Frissített modul cím, áttekintés és minden modul fejlécek
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Frissített cím, tanulási célok, beállítási utasítások és erőforrások
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Frissített cím, tanulási célok, MCP host táblázat és kereszthivatkozások
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Frissített cím, jelvények, előfeltételek és erőforrások
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Frissített Agent Builder hivatkozások és visszajelzési link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Frissített előfeltételek és bővítmény hivatkozások

---

## 2026. április 11.

### Új lecke, dokumentációs javítások és függőségfrissítések

#### Új tananyag tartalom hozzáadva

**05-ös Modul - Haladó témák**
- **5.17 lecke: Ellenfél multi-agent érvelés MCP-vel** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Új átfogó útmutató a többügynökös rendszerek ellenfél vitatkozási mintájáról
  - Mermaid architektúra diagram: két ügynök → megosztott MCP szerver → vita átirat → bíró → ítélet
  - Megosztott MCP eszközszerver (`web_search` + `run_python`) Python és TypeScript-ben megvalósítva
  - Ellenfél rendszer promptok (TÁMOGAT / ELLEN / Bíró) explicit eszközhasználati követelményekkel
  - Vita irányító Pythonban, TypeScriptben és C#-ban, amely köröket kezel és érvényeket irányít
  - MCP `ClientSession` bekötés az irányító számára valódi eszközhívásokhoz
  - Használati eset táblázat (hallucináció érzékelés, fenyegetés modellezés, API tervezés felülvizsgálat, tényszerű ellenőrzés, technológia választás)
  - Biztonsági megfontolások: sandbox végrehajtás, eszközhívás validáció, ráta korlátozás, audit naplózás
  - Strukturált gyakorlat három gyakorlati szcenárióval (kód felülvizsgálat, architektúra döntés, tartalom moderálás)

#### Dokumentációs javítások

**03-as Modul - Kezdés**
- **05-stdio-server/README.md**: Javított hiányos TypeScript stdio szerver példa — hozzátéve hiányzó szállítási példányosítás (`new StdioServerTransport()`) és `server.connect(transport)` hívás hogy egyezzen a Python és .NET példákkal az adott szakaszban
- **14-sampling/README.md**: Hibajavítás — javított `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Tananyag frissítések

**Fő README.md**
- Hozzáadva 5.17 (Ellenfél multi-agent érvelés MCP-vel) bejegyzés a tananyag táblázathoz közvetlen linkkel az új leckéhez

**05-AdvancedTopics/README.md**
- Hozzáadva 5.17 lecke sor a leckék táblázathoz

**study_guide.md**
- Hozzáadva ellenfél multi-agent érvelés téma az Advanced Topics szócsoport térképéhez és kifejtő leíráshoz

#### Kód- és biztonsági javítások

**05-ös Modul - Ellenfélügynökök (`mcp-adversarial-agents`)**
- **Biztonsági javítás — parancsbevitel injekció**: A TypeScript `run_python` eszközben az `execSync` shell interpoláció helyett `execFile` + `promisify` alkalmazása, ezzel megszüntetve a parancsbevitel injekciós felületét (a LLM által vezérelt kód most literal argv elemként kerül átadásra shell közreműködés nélkül)
- **MCP eszköz ciklus bekötés**: Frissítve a Python vita irányító, hogy használja az `AsyncAnthropic` klienst (a blokkoló szinkron `Anthropic` helyett), élő `ClientSession`-t közvetlenül továbbadva minden ügynök körnek, az eszköz definíciókat minden körben a `session.list_tools()` hívással lekéri, és a `tool_use` blokkokat a `session.call_tool()` ciklussal indítja, amíg a modell végleges szöveges választ nem ad

#### Függőségfrissítések

- A `hono` verzióját 4.12.12-re emelték több csomagban (03-Kezdők, 04-Gyakorlati megvalósítás, 10-Mesterségesintelligencia munkafolyamat optimalizálása)
- `@hono/node-server` frissítve 1.19.11-ről 1.19.13-ra a TypeScript csomagokban
- `cryptography` frissítve 46.0.5-ről 46.0.7-re Python csomagokban (10-Mesterségesintelligencia munkafolyamat laborok 3 és 4)
- `lodash` frissítve 4.17.23-ról 4.18.1-re a 10-Mesterségesintelligencia munkafolyamat felügyelőjében

#### Fordítások

- Szinkronizált fordítások több mint 48 nyelven a legfrissebb forrás változásokkal (i18n frissítés)

---

## 2026. február 5.

### Tárolón átívelő érvényesítés és navigációs fejlesztések

#### Új tananyag tartalom hozzáadva

**03-as Modul - Kezdés**
- **12-mcp-hosts/README.md**: Új átfogó útmutató MCP hostok beállításához
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigurációs példák
  - JSON konfigurációs sablonok minden főbb hosthoz
  - Szállítási típusok összehasonlító táblázata (stdio, SSE/HTTP, WebSocket)
  - Gyakori kapcsolódási hibák hibaelhárítása
  - Biztonsági legjobb gyakorlatok a host konfigurációnál

- **13-mcp-inspector/README.md**: Új hibakeresési útmutató az MCP Inspectorhoz
  - Telepítési módok (npx, globális npm, forrásból)
  - Kapcsolódás stdio és HTTP/SSE protokollokon keresztül
  - Teszt eszközök, erőforrások és prompt munkafolyamatok
  - VS Code integráció az MCP Inspectorral
  - Gyakori hibakeresési szcenáriók megoldásokkal

**04-es Modul - Gyakorlati megvalósítás**
- **pagination/README.md**: Új lapozási megvalósítási útmutató
  - Python, TypeScript, Java kurzor alapú lapozási minták
  - Ügyféloldali lapozás kezelése
  - Kurzordizájn stratégiák (átlátszatlan vs. strukturált)
  - Teljesítmény optimalizálási ajánlások

**05-ös Modul - Haladó témák**
- **mcp-protocol-features/README.md**: Új protokoll funkciók részletes bemutatása
  - Folyamatjelentések megvalósítása
  - Lekérés megszakítási minták
  - Erőforrás sablonok URI mintákkal
  - Szerver életciklus kezelése
  - Naplózási szint vezérlés
  - Hibakezelési minták JSON-RPC kódokkal

#### Navigációs javítások (24+ fájl frissítve)

**Fő modul README fájlok**
 Most linkek mind az első leckére, mind a következő modulra

**02-Security al-fájlok**
- Mind az 5 kiegészítő biztonsági dokumentum most "Mi jön ezután" navigációval rendelkezik:

**09-CaseStudy fájlok**
- Minden esettanulmány fájl most szekvenciális navigációval rendelkezik:

**10-StreamliningAI laborok**
Hozzáadva "Mi jön ezután" szakasz a 10-es modul áttekintéséhez és a 11-es modulhoz

#### Kód- és tartalom javítások

**SDK és függőség frissítések**
Javított üres openai verzió `^4.95.0`-ra
SDK frissítve `^1.8.0`-ról `>=1.26.0`-ra
MCP verzió pinyek frissítve `>=1.26.0`-ra

**Kód javítások**
Javítva hibás modell `gpt-4o-mini` → `gpt-4.1-mini`

**Tartalom javítások**
Javítva törött link `READMEmd` → `README.md`, javított tananyag fejléce `Module 1-3` → `Module 0-3`, javított kis- és nagybetű érzékeny útvonal
Eltávolítva sérült ismétlődő Case Study 5 tartalom

**Kezdő útmutató fejlesztések**
Hozzáadva megfelelő bevezető, tanulási célok és előfeltételek kezdők számára

#### Tananyag frissítések

**Fő README.md**
- Hozzáadva bejegyzések 3.12 (MCP Hostok), 3.13 (MCP Inspector), 4.1 (Lapozás), 5.16 (Protokoll funkciók) a tananyag táblázathoz

**Modul README-k**
Hozzáadva 12-es és 13-as lecke a lecke listához
Hozzáadva Gyakorlati Útmutatók szekció lapozási linkkel
Hozzáadva leckék 5.15 (Egyedi Szállítás) és 5.16 (Protokoll funkciók)

**study_guide.md**
- Frissítve az elmetérkép az új témákkal: MCP Hostok beállítása, MCP Inspector, Lapozási stratégiák, Protokoll funkciók részletes bemutatása

## 2026. január 28.

### MCP Specifikáció 2025-11-25 megfelelőségi áttekintés

#### Alapfogalmak fejlesztése (01-CoreConcepts/)
- **Új kliens primitív - Gyökerek**: Átfogó dokumentáció hozzáadva a Roots kliens primitívhez, amely lehetővé teszi a szerverek számára a fájlrendszer határai és hozzáférési engedélyek megértését
- **Eszköz annotációk**: Dokumentáció eszköz viselkedési annotációkról (`readOnlyHint`, `destructiveHint`) jobb eszköz végrehajtási döntésekhez
- **Eszköz hívás a mintavételezésben**: A mintavételezési dokumentáció frissítve paraméterekkel `tools` és `toolChoice` a modell által vezérelt eszköz meghívásokhoz mintavételezési kérések során
- **URL mód előidézés**: Dokumentáció hozzáadva URL-alapú előidézésről a szerver által indított külső webes interakciókhoz
- **Feladatok (kísérleti)**: Új szakasz dokumentálva a kísérleti Feladatok funkcióról tartós végrehajtási burkolók és késleltetett eredmény lekérés céljából
- **Ikon támogatás**: Megjegyezve, hogy az eszközök, erőforrások, erőforrás sablonok és promptok mostantól ikonokat is tartalmazhatnak kiegészítő metaadatként

#### Dokumentációs frissítések
- **README.md**: Hozzáadva MCP Specifikáció 2025-11-25 verzió hivatkozás és dátumalapú verziókezelés magyarázata
- **study_guide.md**: Frissítve a tananyag térkép, hogy tartalmazza a Feladatokat és Eszköz annotációkat az Alapfogalmak szekcióban; dokumentum időbélyeg frissítés

#### Specifikáció megfelelőség ellenőrzés
- **Protokoll verzió**: Ellenőrizve az összes dokumentáció a jelenlegi MCP Specifikáció 2025-11-25 alapján
- **Architektúra megfelelés**: Megerősítve a két rétegű architektúra (Adat réteg + Szállítás réteg) dokumentáció pontosságát
- **Primitívek dokumentációja**: Érvényesítve szerver primitívek (Erőforrások, Promptok, Eszközök) és kliens primitívek (Mintavételezés, Előidézés, Naplózás, Gyökerek)
- **Szállítási mechanizmusok**: Ellenőrizve STDIO és Streamable HTTP szállítás dokumentáció pontossága
- **Biztonsági iránymutatás**: Megerősítve a jelenlegi MCP Biztonsági Legjobb Gyakorlat dokumentációval való összhang

#### Fő MCP 2025-11-25 funkciók dokumentálva
- **OpenID Connect felfedezés**: OIDC-n keresztüli hitelesítési szerver felfedezés
- **OAuth kliens azonosító metaadat dokumentumok**: Ajánlott kliens regisztrációs mechanizmus
- **JSON Schema 2020-12**: Alapértelmezett dialektus az MCP sémadefinícióknál
- **SDK rétegző rendszer**: Formalizált követelmények az SDK funkció támogatás és karbantartáshoz
- **Kormányzati struktúra**: Formalizált Munkacsoportok és Érdekkörök az MCP irányításban

### Jelentős biztonsági dokumentáció frissítés (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integráció
- **Új gyakorlati képzési erőforrás**: Átfogó integráció hozzáadva a [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)-val a teljes biztonsági dokumentációban
- **Expedíciós útvonal lefedettség**: Dokumentálva a teljes tábortól-táborig haladás az Alaptábortól a Csúcsig
- **OWASP kompatibilitás**: A teljes biztonsági iránymutatás mostantól megfelel az OWASP MCP Azure Security Guide kockázatoknak

#### OWASP MCP Top 10 integráció
- **Új szakasz**: Hozzáadva OWASP MCP Top 10 biztonsági kockázatok táblázata Azure enyhítésekkel a fő Biztonsági README-hez
- **Kockázatalapú dokumentáció**: Frissítve az mcp-security-controls-2025.md az OWASP MCP kockázat hivatkozásokkal minden biztonsági területhez
- **Referencia architektúra**: Linkelve az OWASP MCP Azure Security Guide referencia architektúrájához és megvalósítási mintákhoz

#### Frissített biztonsági fájlok
- **README.md**: Hozzáadva Sherpa Workshop áttekintés, expedíciós útvonal táblázat, OWASP MCP Top 10 kockázatok összefoglalása és gyakorlati képzési szekció
- **mcp-security-controls-2025.md**: Frissített fejléc február 2026-ra, hozzáadva OWASP kockázat hivatkozások (MCP01-MCP08), javított specifikáció verzió inkonzisztencia
- **mcp-security-best-practices-2025.md**: Hozzáadva Sherpa és OWASP erőforrás szekció, frissített időbélyeg
- **mcp-best-practices.md**: Hozzáadva gyakorlati képzési szekció Sherpa és OWASP linkekkel
- **azure-content-safety-implementation.md**: Hozzáadva OWASP MCP06 hivatkozás, Sherpa Camp 3 összhang, és további erőforrások szekciója

#### Új erőforrás linkek hozzáadva
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Biztonsági Útmutató](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Egyéni OWASP MCP kockázati oldalak (MCP01-MCP10)

### Tanterv-szintű MCP specifikáció 2025-11-25 összehangolás

#### Modul 03 - Kezdő lépések
- **SDK dokumentáció**: Hozzáadva a Go SDK a hivatalos SDK listához; minden SDK hivatkozás frissítve az MCP specifikáció 2025-11-25 szerinti összehangolásra
- **Szállítási tisztázás**: Frissítve a STDIO és HTTP Streaming szállítási leírások explicit specifikációs hivatkozásokkal

#### Modul 04 - Gyakorlati megvalósítás
- **SDK frissítések**: Hozzáadva a Go SDK; SDK lista frissítve a specifikáció verzió hivatkozással
- **Engedélyezési specifikáció**: MCP engedélyezési specifikáció link frissítve a jelenlegi 2025-11-25 verzióra

#### Modul 05 - Haladó témák
- **Új funkciók**: Hozzáadva megjegyzés az új MCP Specifikáció 2025-11-25 funkciókról (Feladatok, Eszköz annotációk, URL mód előhívás, Gyökerek)
- **Biztonsági források**: Hozzáadva OWASP MCP Top 10 és Sherpa műhely linkek további hivatkozásokként

#### Modul 06 - Közösségi hozzájárulások
- **SDK lista**: Hozzáadva Swift és Rust SDK-k; specifikáció link frissítve 2025-11-25 verzióra
- **Specifikációs hivatkozás**: MCP Specifikáció link frissítve közvetlen specifikációs URL-re

#### Modul 07 - Tanulságok korai bevezetésből
- **Erőforrás frissítések**: Hozzáadva MCP Specifikáció 2025-11-25 link és OWASP MCP Top 10 további forrásokhoz

#### Modul 08 - Legjobb gyakorlatok
- **Specifikáció verzió**: MCP Specifikáció hivatkozás frissítve 2025-11-25 verzióra
- **Biztonsági források**: Hozzáadva OWASP MCP Top 10 és Sherpa műhely további hivatkozásokhoz

#### Modul 10 - AI munkafolyamatok egyszerűsítése
- **Jelvény frissítés**: MCP verzió jelvény módosítása SDK verzióról (1.9.3) a specifikáció verzióra (2025-11-25)
- **Erőforrás linkek**: MCP Specifikáció link frissítve; hozzáadva OWASP MCP Top 10

#### Modul 11 - MCP szerver gyakorlati laborok
- **Specifikáció hivatkozás**: MCP Specifikáció link frissítve 2025-11-25 verzióra
- **Biztonsági források**: OWASP MCP Top 10 hozzáadva hivatalos forrásként

## 2025. december 18.

### Biztonsági dokumentáció frissítés - MCP Specifikáció 2025-11-25

#### MCP Biztonsági legjobb gyakorlatok (02-Security/mcp-best-practices.md) - Specifikációs verzió frissítés
- **Protokoll verzió frissítés**: Frissítve a legújabb MCP Specifikáció 2025-11-25 hivatkozására (kiadva 2025. november 25.)
  - Minden specifikáció verzió hivatkozás frissítve 2025-06-18-ról 2025-11-25-re
  - Dátum hivatkozások frissítve 2025. augusztus 18-ról 2025. december 18-ra
  - Ellenőrizve, hogy minden specifikáció URL a legfrissebb dokumentációra mutat
- **Tartalom validálás**: Átfogó validálás a biztonsági legjobb gyakorlatoknak a legfrissebb szabványokkal való egyezésére
  - **Microsoft biztonsági megoldások**: Ellenőrizve aktuális terminológia és linkek a Prompt Shields (korábban „Jailbreak kockázat észlelés”), Azure Content Safety, Microsoft Entra ID és Azure Key Vault esetén
  - **OAuth 2.1 biztonság**: Megerősítve az összehangolás a legújabb OAuth biztonsági legjobb gyakorlatokkal
  - **OWASP szabványok**: Érvényesítve, hogy az OWASP Top 10 LLM-ek esetében naprakész
  - **Azure szolgáltatások**: Ellenőrizve minden Microsoft Azure dokumentációs link és legjobb gyakorlat
- **Szabványok összhangja**: Minden hivatkozott biztonsági szabvány megerősítve aktuálisnak
  - NIST AI Kockázatkezelési Keretrendszer
  - ISO 27001:2022
  - OAuth 2.1 Biztonsági Legjobb Gyakorlatok
  - Azure biztonsági és megfelelőségi keretrendszerek
- **Megvalósítási erőforrások**: Ellenőrizve minden megvalósítási útmutató link és erőforrás
  - Azure API Management hitelesítési minták
  - Microsoft Entra ID integrációs útmutatók
  - Azure Key Vault titkok kezelése
  - DevSecOps pipeline-ok és megfigyelési megoldások

### Dokumentáció minőségbiztosítás
- **Specifikációnak való megfelelés**: Biztosítva, hogy minden kötelező MCP biztonsági követelmény (MUST/MUST NOT) megfelel a legfrissebb specifikációnak
- **Erőforrás frissesség**: Ellenőrizve minden külső hivatkozás Microsoft dokumentációra, biztonsági szabványokra és megvalósítási útmutatókra
- **Legjobb gyakorlatok lefedettsége**: Megerősítve a teljes körű lefedettség hitelesítés, engedélyezés, AI-specifikus fenyegetések, ellátási lánc biztonság és vállalati minták esetén

## 2025. október 6.

### Kezdő szekció bővítés – Haladó szerverhasználat és egyszerű hitelesítés

#### Haladó szerverhasználat (03-GettingStarted/10-advanced)
- **Új fejezet hozzáadva**: Átfogó útmutató a haladó MCP szerverhasználathoz, beleértve a normál és alacsony szintű szerverarchitektúrákat.
  - **Normál vs. alacsony szintű szerver**: Részletes összehasonlítás és kódpéldák Pythonban és TypeScriptben mindkét megközelítéshez.
  - **Handler-alapú tervezés**: Magyarázat a handler-alapú eszköz/erőforrás/prompt kezelésről a skálázható, rugalmas szerver megvalósításokhoz.
  - **Gyakorlati minták**: Valós példák arra, amikor az alacsony szintű szerverminták előnyösek haladó funkciókhoz és architektúrához.

#### Egyszerű hitelesítés (03-GettingStarted/11-simple-auth)
- **Új fejezet hozzáadva**: Lépésről lépésre útmutató az egyszerű hitelesítés megvalósításához MCP szerverekben.
  - **Hitelesítési fogalmak**: Világos magyarázat a hitelesítés és engedélyezés, valamint az adatok kezelése között.
  - **Alap hitelesítés megvalósítása**: Middleware-alapú hitelesítési minták Pythonban (Starlette) és TypeScriptben (Express), kódpéldákkal.
  - **Haladó biztonság felé haladás**: Útmutatás az egyszerű hitelesítésről indulva az OAuth 2.1 és RBAC felé, hivatkozásokkal haladó biztonsági modulokra.

Ezek a kiegészítések gyakorlati, kézzelfogható útmutatást nyújtanak a robusztusabb, biztonságosabb és rugalmasabb MCP szerver megvalósítások építéséhez, összekötve az alapvető fogalmakat a haladó gyártási mintákkal.

## 2025. szeptember 29.

### MCP Szerver adatbázis integrációs laborok – Átfogó gyakorlati tanulási út

#### 11-MCPServerHandsOnLabs - Új, teljes adatbázis integrációs tanterv
- **Teljes 13-laboros tanulási út**: Átfogó gyakorlati tanterv hozzáadva gyártásra készen MCP szerverek építéséhez PostgreSQL adatbázis integrációval
  - **Valós megvalósítás**: Zava Retail elemzési esettanulmány vállalati szintű mintákkal
  - **Strukturált tanulási előrehaladás**:
    - **Labok 00-03: Alapok** – Bevezetés, alap architektúra, biztonság & többbérlős működés, környezet beállítása
    - **Labok 04-06: MCP szerver építése** – Adatbázis tervezés & séma, MCP szerver implementáció, eszközfejlesztés
    - **Labok 07-09: Haladó funkciók** – Szemantikus keresés integráció, tesztelés & hibakeresés, VS Code integráció
    - **Labok 10-12: Gyártás & legjobb gyakorlatok** – Telepítési stratégiák, megfigyelés & monitorozás, optimalizálás & legjobb gyakorlatok
  - **Vállalati technológiák**: FastMCP keretrendszer, PostgreSQL pgvectorrel, Azure OpenAI beágyazások, Azure Container Apps, Application Insights
  - **Haladó funkciók**: Soronkénti biztonság (RLS), szemantikus keresés, többbérlős adat-hozzáférés, vektorbeli beágyazások, valós idejű megfigyelés

#### Terminológia standardizálás - Modulról laborra átalakítás
- **Átfogó dokumentáció frissítés**: Minden README fájl szisztematikusan frissítve az 11-MCPServerHandsOnLabs-ban, hogy "Lab" terminológiát használjon "Modul" helyett
  - **Szekciócímek**: "Mit fed le ez a modul" frissítve "Mit fed le ez a labor" mind a 13 labban
  - **Tartalom leírása**: "Ez a modul biztosítja..." módosítva "Ez a labor biztosítja..."-ra az összes dokumentumban
  - **Tanulási célok**: "A modul végére..." frissítve "A labor végére..."
  - **Navigációs hivatkozások**: Minden "Modul XX:" hivatkozás "Labor XX:"-ra váltva kereszthivatkozásokban és navigációban
  - **Teljesítménykövetés**: "A modul befejezése után..." módosítva "A labor befejezése után..."
  - **Megőrzött technikai hivatkozások**: Python modul hivatkozások megőrizve konfigurációs fájlokban (pl. `"module": "mcp_server.main"`)

#### Tanulmányi útmutató fejlesztése (study_guide.md)
- **Vizualizált tantervtérkép**: Új "11. Adatbázis integrációs laborok" szekció hozzáadva átfogó labor struktúra vizualizációval
- **Tároló struktúra**: Frissítve tíz fő szekcióról tizenegyre, részletes leírással az 11-MCPServerHandsOnLabs-ról
- **Tanulási útmutatás**: Navigációs utasítások bővítve a 00-11 szekciókat lefedve
- **Technológiai lefedettség**: Hozzáadva FastMCP, PostgreSQL és Azure szolgáltatások integrációs részletek
- **Tanulási eredmények**: Kiemelve a gyártásra kész szerverfejlesztést, adatbázisintegrációs mintákat és vállalati biztonságot

#### Fő README struktúra fejlesztése
- **Labor-alapú terminológia**: Az 11-MCPServerHandsOnLabs fő README.md-je frissítve, hogy egységesen használja a "Labor" struktúrát
- **Tanulási út szervezése**: Egyértelmű előrehaladás az alapvető fogalmaktól a haladó megvalósításon át a gyártási telepítésig
- **Valós fókusz**: Gyakorlati, kézzelfogható tanulás hangsúlyozása vállalati szintű mintákkal és technológiákkal

### Dokumentáció minőség és következetesség javítása
- **Gyakorlati tanulás hangsúlyozása**: Az egész dokumentációban megerősítve a gyakorlati, labor-alapú megközelítés
- **Vállalati minták fókusz**: Kiemelve a gyártásra kész implementációkat és a vállalati biztonsági megfontolásokat
- **Technológiai integráció**: Átfogó lefedettség a modern Azure szolgáltatások és AI integrációs minták esetén
- **Tanulási előrehaladás**: Egyértelmű, strukturált út az alapvető fogalmaktól a gyártási telepítésig

## 2025. szeptember 26.

### Esettanulmányok bővítése - GitHub MCP Registry integráció

#### Esettanulmányok (09-CaseStudy/) - Ökoszisztéma fejlesztési fókusz
- **README.md**: Jelentős bővítés átfogó GitHub MCP Registry esettanulmánnyal
  - **GitHub MCP Registry esettanulmány**: Új átfogó esettanulmány a GitHub MCP Registry elindításáról 2025 szeptemberében
    - **Probléma elemzés**: Részletes vizsgálat a fragmentált MCP szerver felfedezésről és telepítési kihívásokról
    - **Megoldás architektúra**: GitHub központosított regiszter megközelítés egykattintásos VS Code telepítéssel
    - **Üzleti hatás**: Mérhető javulások a fejlesztői onboardingban és termelékenységben
    - **Stratégiai érték**: Moduláris agent telepítésre és eszközök közötti interoperabilitásra fókuszálva
    - **Ökoszisztéma fejlesztés**: Alapvető platformként pozícionálva az agent rendszerek integrációjához
  - **Fejlesztett esettanulmány struktúra**: Minden hét esettanulmány frissítve egységes formázással és átfogó leírással
    - Azure AI utazási ügynökök: Többagentű koordináció hangsúlyozása
    - Azure DevOps integráció: Munkafolyamat automatizálás fókusz
    - Valós idejű dokumentum lekérés: Python konzolos kliens implementáció
    - Interaktív tanulmányterv generátor: Chainlit konverzációs webalkalmazás
    - Szerkesztői dokumentáció: VS Code és GitHub Copilot integráció
    - Azure API Management: Vállalati API integrációs minták
    - GitHub MCP Registry: Ökoszisztéma fejlesztés és közösségi platform
  - **Átfogó összefoglaló**: Átírt összefoglaló rész, amely kiemeli a hét esettanulmányt több MCP megvalósítási dimenzióban
    - Vállalati integráció, Többagentű koordináció, Fejlesztői termelékenység
    - Ökoszisztéma fejlesztés, Oktatási alkalmazások kategorizálás
    - Fejlesztett betekintések architekturális mintákba, megvalósítási stratégiákba és legjobb gyakorlatokba
    - Kiemelve az MCP-t, mint érett, gyártásra kész protokollt

#### Tanulmányi útmutató frissítések (study_guide.md)
- **Vizualizált tantervtérkép**: Frissítve a gondolattérkép, hogy tartalmazza a GitHub MCP Registry-t az Esettanulmányok szekcióban
- **Esettanulmányok leírása**: Fejlesztve az általános leírásokból részletes bontásra hét átfogó esettanulmányról
- **Tároló szerkezet**: Frissítve a 10. szekció a részletes esettanulmány lefedettséggel és konkrét megvalósítási részletekkel
- **Changelog integráció**: Hozzáadva a 2025. szeptember 26-i bejegyzés, amely dokumentálja a GitHub MCP Registry hozzáadását és az esettanulmány fejlesztéseket
- **Dátum frissítések**: Lábléc időbélyeg frissítve a legújabb verzióra (2025. szeptember 26.)

### Dokumentáció minőség javítása
- **Következetesség fejlesztése**: Esettanulmány formázás és szerkezet egységesítve mind a hét példánál
- **Átfogó lefedettség**: Esettanulmányok kiterjednek üzleti, fejlesztői termelékenységi és ökoszisztéma fejlesztési forgatókönyvekre
- **Stratégiai pozicionálás**: Fókuszálás fejlesztve az MCP-re, mint alap platform az agent rendszerek telepítéséhez
- **Erőforrás integráció**: További erőforrások frissítve a GitHub MCP Registry linkjével

## 2025. szeptember 15.

### Haladó témák bővítése - Egyedi szállítások és kontextus mérnökség

#### MCP egyedi szállítások (05-AdvancedTopics/mcp-transport/) - Új haladó megvalósítási útmutató
- **README.md**: Teljeskörű útmutató az egyedi MCP szállítási mechanizmusokhoz
  - **Azure Event Grid szállítás**: Átfogó szerver nélküli eseményvezérelt szállítási megvalósítás
    - C#, TypeScript és Python példák Azure Functions integrációval
    - Eseményvezérelt architektúra minták skálázható MCP megoldásokhoz
    - Webhook fogadók és push-alapú üzenetkezelés
  - **Azure Event Hubs szállítás**: Nagy áteresztőképességű streaming szállítás megvalósítása
    - Valós idejű streaming képességek alacsony késleltetésű forgatókönyvekhez
    - Particionálási stratégiák és ellenőrzőpont kezelés
    - Üzenet kötegzés és teljesítményoptimalizálás
  - **Vállalati integrációs minták**: Gyártásra kész architekturális példák
    - Elosztott MCP feldolgozás több Azure Functions között
    - Hibrid szállítási architektúrák több szállítási típus kombinálásával
    - Üzenet tartósság, megbízhatóság és hibakezelési stratégiák
  - **Biztonság és megfigyelés**: Azure Key Vault integráció és megfigyelhetőségi minták
    - Kezelt identitás hitelesítés és legkisebb jogosultság hozzáférés
    - Application Insights telemetria és teljesítmény monitorozás
    - Áramkör megszakítók és hibátűrési minták
  - **Tesztelési keretrendszerek**: Átfogó tesztelési stratégiák egyedi szállításokhoz
    - Egység tesztelés teszt double-ökkel és mocking keretrendszerekkel
    - Integrációs tesztelés Azure Test Containers használatával
    - Teljesítmény és terheléses tesztelési megfontolások

#### Kontextus mérnökség (05-AdvancedTopics/mcp-contextengineering/) - Felemelkedő AI terület
- **README.md**: Átfogó feltárása a kontextus mérnökségnek, mint felemelkedő szakterület
  - **Alapelvek**: Teljes kontextus megosztás, akció döntéshozatali tudatosság, és kontextus ablak kezelése

  - **MCP protokollal való összehangolás**: Hogyan kezeli az MCP tervezése a kontextusmenedzsment kihívásait
    - Kontextusablak korlátok és progresszív betöltési stratégiák
    - Relevancia meghatározása és dinamikus kontextus lekérdezés
    - Többmodalitású kontextuskezelés és biztonsági szempontok
  - **Megvalósítási megközelítések**: Egyszálú vs. többügynökös architektúrák
    - Kontextusrészek darabolási és prioritási technikái
    - Progresszív kontextusbetöltés és tömörítési stratégiák
    - Rétegezett kontextusmegközelítések és lekérdezés optimalizálás
  - **Mérés keretrendszere**: Feltörekvő metrikák a kontextus hatékonyságának értékelésére
    - Bemeneti hatékonyság, teljesítmény, minőség és felhasználói élmény szempontjai
    - Kísérleti megközelítések a kontextus optimalizálására
    - Hibaanalízis és fejlesztési módszertanok

#### Tananyag navigáció frissítések (README.md)
- **Fokozott modulstruktúra**: Frissített tananyagtábla új, haladó témákkal bővítve
  - Hozzáadva Context Engineering (5.14) és Custom Transport (5.15) bejegyzések
  - Egységes formázás és navigációs linkek minden modulban
  - Frissített leírások, hogy tükrözzék a jelenlegi tartalomkört

### Könyvtárszerkezet fejlesztések
- **Elnevezési szabványosítás**: Az "mcp transport" átnevezése "mcp-transport"-ra, hogy megfeleljen a többi haladó témakönyvtárnak
- **Tartalom szervezés**: Minden 05-AdvancedTopics mappa mostantól egységes elnevezési mintát követ (mcp-[téma])

### Dokumentáció minőség fejlesztések
- **MCP specifikáció összehangolás**: Minden új tartalom hivatkozik a 2025-06-18-as MCP specifikációra
- **Többnyelvű példák**: Átfogó kódpéldák C#, TypeScript és Python nyelven
- **Vállalati fókusz**: Gyártásra kész minták és Azure felhő integráció mindenütt
- **Vizualizációs dokumentáció**: Mermaid diagramok az architektúra és folyamatelemzés megjelenítésére

## 2025. augusztus 18.

### Dokumentáció átfogó frissítés – MCP 2025-06-18 standardok

#### MCP biztonsági legjobb gyakorlatok (02-Security/) - Teljes modernizáció
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Teljes átírás a 2025-06-18-as MCP specifikációhoz igazítva
  - **Kötelező követelmények**: Hozzáadott kifejezett KELL / NEM KELL követelmények a hivatalos specifikációból, egyértelmű vizuális jelölőkkel
  - **12 alapvető biztonsági gyakorlat**: Újratervezve a 15 elemből átfogó biztonsági területekké
    - Token biztonság és hitelesítés külső identitásszolgáltatóval való integrációval
    - Munkamenet-kezelés és szállítási biztonság kriptográfiai követelményekkel
    - AI-specifikus fenyegetésvédelem Microsoft Prompt Shields integrációval
    - Hozzáférés-vezérlés és jogosultságok a legkisebb jogosultság elve szerint
    - Tartalombiztonság és felügyelet Azure Content Safety integrációval
    - Ellátási lánc biztonság átfogó komponensellenőrzéssel
    - OAuth biztonság és Confused Deputy megelőzés PKCE implementációval
    - Eseménykezelés és helyreállítás automatizált képességekkel
    - Megfelelőség és irányítás szabályozási összhangban
    - Fejlett biztonsági ellenőrzések zero trust architektúrával
    - Microsoft biztonsági ökoszisztéma integráció átfogó megoldásokkal
    - Folyamatos biztonsági fejlődés adaptív gyakorlatokkal
  - **Microsoft biztonsági megoldások**: Fejlesztett integrációs útmutatás Prompt Shields, Azure Content Safety, Entra ID és GitHub Advanced Security számára
  - **Megvalósítási erőforrások**: Kategorizált átfogó hivatkozások a Hivatalos MCP dokumentáció, Microsoft biztonsági megoldások, biztonsági szabványok és megvalósítási útmutatók szerint

#### Haladó biztonsági ellenőrzések (02-Security/) - Vállalati megvalósítás
- **MCP-SECURITY-CONTROLS-2025.md**: Teljes felülvizsgálat vállalati szintű biztonsági keretrendszerrel
  - **9 átfogó biztonsági terület**: Bővítve az alapvető ellenőrzésekből részletes vállalati keretbe
    - Fejlett hitelesítés és autorizáció Microsoft Entra ID integrációval
    - Token biztonság és átadásgátló ellenőrzések átfogó validációval
    - Munkamenet biztonsági ellenőrzések eltérítés megelőzéssel
    - AI-specifikus biztonsági ellenőrzések prompt injekció és eszközvegyítés elleni védelemmel
    - Confused Deputy támadás megelőzés OAuth proxy biztonsággal
    - Eszköz végrehajtás biztonság homokozóval és izolációval
    - Ellátási lánc biztonsági ellenőrzések függőségellenőrzéssel
    - Felügyelet és észlelési ellenőrzések SIEM integrációval
    - Eseménykezelés és helyreállítás automatizáltan
  - **Megvalósítási példák**: Részletes YAML konfigurációs blokkok és kódpéldák hozzáadva
  - **Microsoft megoldások integrációja**: Átfogó lefedettség Azure biztonsági szolgáltatásokkal, GitHub Advanced Security-vel és vállalati identitáskezeléssel

#### Haladó témák biztonság (05-AdvancedTopics/mcp-security/) - Gyártásra kész megvalósítás
- **README.md**: Teljes átírás vállalati biztonsági megvalósításról
  - **Aktuális specifikáció szerinti**: Frissítve MCP Specification 2025-06-18-ra kötelező biztonsági követelményekkel
  - **Fokozott hitelesítés**: Microsoft Entra ID integráció részletes .NET és Java Spring Security példákkal
  - **AI biztonsági integráció**: Microsoft Prompt Shields és Azure Content Safety megvalósítás részletes Python példákkal
  - **Haladó fenyegetéscsillapítás**: Átfogó megvalósítási példák a
    - Confused Deputy támadás megelőzésére PKCE-vel és felhasználói hozzájárulás validációval
    - Token átengedés megelőzése közönségvalidációval és biztonságos tokenkezeléssel
    - Munkamenet eltérítés megelőzés kriptográfiai kötésekkel és viselkedési elemzéssel
  - **Vállalati biztonsági integráció**: Azure Application Insights monitorozás, fenyegetésészlelő csatornák és ellátási lánc biztonság
  - **Megvalósítási ellenőrző lista**: Egyértelmű kötelező és ajánlott biztonsági ellenőrzések, Microsoft biztonsági ökoszisztéma előnyökkel

### Dokumentáció minőség és szabvány összehangolás
- **Specifikáció hivatkozások**: Frissítve minden hivatkozás az aktuális MCP Specification 2025-06-18-ra
- **Microsoft biztonsági ökoszisztéma**: Fejlett integrációs útmutatás minden biztonsági dokumentációban
- **Gyakorlati megvalósítás**: Részletes kódpéldák hozzáadva .NET, Java és Python nyelveken vállalati mintákkal
- **Erőforrás-szervezés**: Átfogó kategorizálás hivatalos dokumentáció, biztonsági szabványok és megvalósítási útmutatók szerint
- **Vizuális jelölések**: Egyértelmű jelölés kötelező követelmények és ajánlott gyakorlatok között


#### Alapfogalmak (01-CoreConcepts/) - Teljes modernizáció
- **Protokoll verzió frissítés**: Aktuális MCP Specification 2025-06-18-ra hivatkozik, dátumalapú verziózással (ÉÉÉÉ-HH-NN formátum)
- **Architektúra finomítás**: Hosts, Clients és Servers leírásainak fejlesztése az aktuális MCP architektúrális minták tükrében
  - A Hostok most már egyértelműen AI alkalmazásokként meghatározva, amelyek több MCP kliens kapcsolatot koordinálnak
  - Kliensek protokollkapcsolóként, amelyek egy az egyhez szerverkapcsolatokat tartanak fenn
  - Szerverek fejlesztve helyi és távoli telepítési forgatókönyvekkel
- **Primitívek átalakítása**: Teljes átdolgozás szerver és kliens primitívekkel
  - Szerver primitívek: Erőforrások (adatforrások), Kérések (sablonok), Eszközök (futtatható funkciók) részletes magyarázatokkal és példákkal
  - Kliens primitívek: Mintavételezés (LLM kiegészítések), Kiváltás (felhasználói input), Naplózás (hibakeresés/felügyelet)
  - Frissítve aktuális felfedezési (`*/list`), lekérdezési (`*/get`) és végrehajtási (`*/call`) módszerminták szerint
- **Protokoll architektúra**: Két rétegű architektúra modell bevezetése
  - Adatréteg: JSON-RPC 2.0 alap, életciklus-kezeléssel és primitívekkel
  - Szállítási réteg: STDIO (helyi) és streamelhető HTTP SSE-vel (távoli) szállítási mechanizmusok
- **Biztonsági keretrendszer**: Átfogó biztonsági alapelvek, beleértve a kifejezett felhasználói hozzájárulást, adatok védelmét, eszközvégrehajtás biztonságát és szállítási réteg biztonságot
- **Kommunikációs minták**: Frissített protokoll üzenetek inicializálási, felfedezési, végrehajtási és értesítési folyamatokat mutatnak
- **Kódpéldák**: Felfrissített többnyelvű példák (.NET, Java, Python, JavaScript) az aktuális MCP SDK minták szerint

#### Biztonság (02-Security/) - Teljes biztonsági áttekintés  
- **Szabványok összehangolása**: Teljes összhang az MCP Specification 2025-06-18 biztonsági követelményeivel
- **Hitelesítés fejlődése**: Dokumentált evolúció egyedi OAuth szerverektől külső identitásszolgáltató delegálásáig (Microsoft Entra ID)
- **AI-specifikus fenyegetéselemzés**: Kiterjesztett lefedettség a modern AI támadási vektorokra
  - Részletes prompt injekciós támadás forgatókönyvek valós példákkal
  - Eszközvegyítés mechanizmusok és "rug pull" támadási minták
  - Kontextusablak vegyítése és modell összezavarás támadások
- **Microsoft AI biztonsági megoldások**: Átfogó Microsoft biztonsági ökoszisztéma lefedettség
  - AI Prompt Shields fejlett észlelési, kiemelési és elválasztó technikákkal
  - Azure Content Safety integrációs minták
  - GitHub Advanced Security az ellátási lánc védelemhez
- **Haladó fenyegetéscsillapítás**: Részletes biztonsági ellenőrzések a
  - Munkamenet eltérítés MCP specifikus támadási forgatókönyvekkel és kriptográfiai session ID követelményekkel
  - Confused deputy problémák MCP proxy forgatókönyvekben egyértelmű hozzájárulás követelményekkel
  - Token átengedési sérülékenységek kötelező validációs ellenőrzésekkel
- **Ellátási lánc biztonság**: Bővített AI ellátási lánc lefedettség alapmodellek, beágyazási szolgáltatások, kontextus szolgáltatók és harmadik fél API-k szintjén
- **Alapbiztonság**: Fejlesztett integráció vállalati biztonsági mintákba, beleértve a zero trust architektúrát és Microsoft biztonsági ökoszisztémát
- **Erőforrás szervezés**: Átfogó kategorizált erőforrás hivatkozások típus szerint (Hivatalos Docs, Szabványok, Kutatás, Microsoft megoldások, megvalósítási útmutatók)

### Dokumentáció minőség javítások
- **Strukturált tanulási célok**: Fejlesztett tanulási célok konkrét, cselekvő eredményekkel
- **Kereszthivatkozások**: Hozzáadott linkek kapcsolódó biztonsági és alapfogalmi témák között
- **Aktuális információk**: Frissített minden dátum hivatkozást és specifikációs linket az aktuális szabványokra
- **Megvalósítási útmutatás**: Hozzáadott specifikus, cselekvő megvalósítási iránymutatások mindkét szekcióban

## 2025. július 16.

### README és navigáció fejlesztések
- Teljesen újraterveztük a tananyag navigációt a README.md-ben
- `<details>` tagek helyett hozzáférhetőbb táblázatos formátumot alkalmaztunk
- Alternatív elrendezési opciókat hoztunk létre az új "alternative_layouts" mappában
- Hozzáadott kártyás, fülös és harmonikaszerű navigációs példák
- Frissítettük a tárhely struktúra szekciót a legfrissebb fájlokkal
- Fokozottuk a "Hogyan használd ezt a tananyagot" részt világos ajánlásokkal
- Frissítettük az MCP specifikációs linkeket a helyes URL-ekre
- Hozzáadtuk a Context Engineering szekciót (5.14) a tananyagszerkezethez

### Tanulmányi útmutató frissítések
- Teljesen felülvizsgáltuk a tanulmányi útmutatót a jelenlegi tárhelystruktúrához igazítva
- Hozzáadott új szekciókat MCP kliensek és eszközök, illetve népszerű MCP szerverek számára
- Frissítettük a vizuális tananyagtérképet, hogy pontosan tükrözze az összes témát
- Fokozottuk a haladó témák leírását, hogy lefedje az összes speciális területet
- Frissítettük az esettanulmány szekciót a tényleges példák tükrében
- Hozzáadtuk ezt az átfogó változásnaplót

### Közösségi hozzájárulások (06-CommunityContributions/)
- Részletes információk hozzáadva MCP szerverekről képgeneráláshoz
- Átfogó szekció Claude használatáról VSCode-ban
- Hozzáadott Cline terminál kliens beállítási és használati útmutatót
- Frissített MCP kliens szekciót az összes népszerű klienssel
- Fejlesztettük a hozzájárulási példákat pontosabb kódmintákkal

### Haladó témák (05-AdvancedTopics/)
- Szerveztük az összes speciális témakönyvtárat egységes elnevezési szabvánnyal
- Hozzáadtuk a kontextus mérnöki anyagokat és példákat
- Hozzáadott Foundry agent integrációs dokumentációt
- Fokozottuk Entra ID biztonsági integrációs dokumentációt

## 2025. június 11.

### Kezdeti létrehozás
- Kiadva az MCP kezdőknek tananyag első verziója
- Létrehozva az összes 10 fő szekció alapstruktúrája
- Megvalósítva a vizuális tananyagtérkép a navigációhoz
- Hozzáadott kezdeti mintaprojektek több programozási nyelven

### Első lépések (03-GettingStarted/)
- Létrehozva az első szerver megvalósítási példák
- Hozzáadva kliens fejlesztési útmutatás
- Beillesztve LLM kliens integrációs utasítások
- Hozzáadott VS Code integrációs dokumentáció
- Megvalósítva Server-Sent Events (SSE) szerver példák

### Alapfogalmak (01-CoreConcepts/)
- Hozzáadott részletes magyarázat kliens-szerver architektúráról
- Létrehozva dokumentáció kulcs protokoll komponensekről
- Dokumentálva az MCP üzenetküldési minták

## 2025. május 23.

### Tárhely struktúra
- Inicializálva a tárhely alap mappastruktúrával
- Létrehozva README fájlok minden fő szekcióhoz
- Beállítva fordítási infrastruktúra
- Hozzáadva képi anyagok és diagramok

### Dokumentáció
- Létrehozva kezdeti README.md tananyag áttekintéssel
- Hozzáadva CODE_OF_CONDUCT.md és SECURITY.md
- Beállítva SUPPORT.md segítségkéréshez
- Létrehozva előzetes tanulmányi útmutató szerkezet

## 2025. április 15.

### Tervezés és keretrendszer
- Kezdeti tervezés az MCP kezdőknek tananyaghoz
- Meghatározva tanulási célok és célközönség
- Vázolva a tananyag 10 szekciós szerkezete
- Kidolgozva szemléleti keretrendszer példákhoz és esettanulmányokhoz
- Létrehozva kezdeti prototípus példák kulcsfogalmakhoz

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Muutuste logi: MCP algajatele kursus

See dokument on Model Context Protocoli (MCP) algajate kursuse kõigi oluliste muudatuste arvestus. Muudatused on dokumenteeritud pööratud kronoloogilises järjekorras (uusimad muudatused esimesena).

## 2. juuli 2026

### Uus õppetund: 2026-07-28 MCP spetsifikatsiooni vabastusversioon

Lisatud järgmise `2026-07-28` MCP spetsifikatsiooni vabastusversiooni katvus (teatatud 21. mail 2026; lõplik väljalase planeeritud 28. juuliks 2026), kokkuvõtlikult [ametliku teadaande blogipostitusest](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Kursuse alus jääb alles **MCP Spetsifikatsioon 2025-11-25** kuni uue versiooni väljalaskmiseni, seega on see esitatud tulevikku vaatava juhisena, mitte olemasolevate õppetundide ümberkirjutusena.

- **Uus**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — täispikk õppetund, mis käsitleb olekuta protokolli tuuma (kaotades `initialize` käepigistuse ja `Mcp-Session-Id`), uusi `Mcp-Method`/`Mcp-Name` marsruuteerimis päiseid, `ttlMs`/`cacheScope` vahemällu salvestamise metaandmeid, W3C Trace Context `_meta`-s, ametlikku Laienduste raamistikku (MCP rakendused ja uus Tasks laiendus), kuut autoriseerimise tugevdamise SEPid, Rootsi/Sampling/Loggingu kasutuse lõpetamist ning täielikku liikumist JSON Schema 2020-12 tööriistade skeemide jaoks.
- **Uuendatud** edasivaatavad hüüdlaused uue õppetundi viitamiseks:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolli versiooni märkus, Sampling/Roots/Logging/Tasks jaotised ning "Mis järgmiseks"
  - [02-Security/README.md](./02-Security/README.md): autoriseerimise tugevdamise märkused
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): olekuta transpordi viide
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Samplingu kasutuse lõpetamise viide
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Loggingu kasutuse lõpetamise ning Tasks laienduse viide
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): olekuta / seansi marsruudi viide
  - [README.md](./README.md): "Tuleviku väljavaated" märkus spetsifikatsiooni osas ning uus `1.1` kirje kursuse moodulite tabelis
  - [study_guide.md](./study_guide.md): tulevikku vaatav punkt põhikontseptsioonide ülevaates ning kuupäevaga lisamärkus
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): viide `mcp-session-id` transpordikaardile enne olekuta päringumudelit
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): mooduli ülevaade Root Contexts/Sampling kasutuse lõpetamise ning Tasks laienduse kohta
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autoriseerimise tugevdamise viide

## 24. juuni 2026

### Uus õppetund: MCP kasutamine Copilot rakenduses

- [Tööriistade jaotis](./12-tooling/README.md) Lisatud tööriistade jaotis.
- [MCP Copilot rakenduses](./12-tooling/01-copilot-app/README.md)

## 16. juuni 2026

### MCP Spetsifikatsiooni kooskõlastamine ja näidiste valideerimine

Valideeriti kursus vastavalt kehtivale **MCP Spetsifikatsioon 2025-11-25** ja viimastele ametlikele SDK-dele, seejärel parandati allesjäänud aegunud spetsifikatsiooni viited ning kinnitati, et põhinäidised ehituvad ja töötavad endiselt korrektselt.

#### Spetsifikatsiooni versiooni parandused (2025-06-18 / 2025-03-26 → 2025-11-25)

Uuendatud ingliskeelne sisu, kus see väitis veel vanema spetsifikatsiooni kehtivat standardit, ning parandas lingid kanonilistele `modelcontextprotocol.io` spetsifikatsiooni teedele:
- **05-AdvancedTopics/mcp-security/README.md**: Uuendatud "Praegune standard" bänner, sissejuhatus, põhiturvapõhimõtete pealkiri, kohustuslike nõuete sektsioon, Microsoft Entra ID jaotised, Viited & Ressursid ning turvateade (8 viidet) versioonile 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Uuendatud täiendavate ressursside spetsifikatsiooni link ja "Praegune standard" bänner versioonile 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Asendatud aegunud `2025-03-26` turbe- ja usalduslink kehtiva 2025-11-25 turbe parimate praktikatega leheküljega
- **03-GettingStarted/14-sampling/README.md**: Uuendatud ametlik proovivõtu dokumendid link 2025-11-25-le
- **03-GettingStarted/05-stdio-server/README.md**: Uuendatud oleviku vormis „praegune MCP spetsifikatsioon“ viide ja täiendavate ressursside spetsifikatsiooni link 2025-11-25-le (ajaloolised SSE kasutuse lõpetamise märkused jäeti täpsuse huvides alles)

#### Näidiste valideerimine kehtivate SDK-dega

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` lahendas `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` läbis ilma tüübivigadeta — olemasolevad `McpServer`/`StdioServerTransport` API-d on endiselt kehtivad
- **Python (03-GettingStarted/01-first-server/solution/python)**: valideeritud isoleeritud `.venv`-keskkonnas koos `mcp[cli]` (1.27.2); `py_compile` õnnestus ja `FastMCP.list_tools()` tagastas õigesti tööriistad `add` ja `subtract`
- Kinnitatud, et kõik näidiste `@modelcontextprotocol/sdk` versiooni vahemikud (`>=1.26.0` / `^1.26.0` / `^1.27.0`) lahenevad korrektselt versioonile `1.29.0` ilma murdvaid API muudatusi tegemata

#### Sõltuvuste versiooninäitude joondamine (versioonide lünkade sulgemine)

Värskendatud aegunud SDK versiooninäiteid, nii et iga näide järgib praegust MCP väljaannet vastavalt kogu repositooriumi konventsioonile:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: tõstetud `@modelcontextprotocol/sdk` versioon `^1.8.0` → `>=1.26.0` ja uuendatud aegunud kirjeldus `"updated for MCP 2025-06-18"` uuele `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ja **lab4/code/github_mcp_server/pyproject.toml**: täpsed versiooninäidud `mcp==1.23.0` tõstetud → `mcp>=1.26.0`; mõlemas taastatud `uv.lock` failid (`uv lock`), et lukustust failid lahendaksid praeguse `mcp 1.27.2` ja püsiksid sünkroonis manifestidega

#### Kursuse sisulünkade analüüs — viimaste spetsifikatsiooni funktsioonide kaetavus

Kinnitatud, et kursus katab juba kõiki MCP 2025-11-25 lisatud või laiendatud primitiive, puuduvad sisulüngad:
- **Sampling**: Õppetund 03-GettingStarted/14-sampling koos 05-AdvancedTopics/mcp-sampling-ga
- **Info pärimine (kaasa arvatud URL režiim)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumenteeritud 00-Introduction, 01-CoreConcepts ja 05-AdvancedTopics/mcp-root-contexts
- **Tasks (katse- ja pikaajalised toimingud)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Tööriistade annotatsioonid** (`readOnlyHint` / `destructiveHint`): Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features

### Turvalisuse tugevdamine ja sõltuvuste haavatavuste parandamine

Tehtud täielik turvakontroll iga sõltuvuse manifesti ja näidiskoodi suhtes, seejärel parandatud kõik teatatud npm hoiatused ja üks kooditaseme turvaauk. Pärast parandusi aruandlus `npm audit` näitab iga auditeeritud kataloogi kohta **0 haavatavust**.

#### npm sõltuvuste haavatavused (transitiivsed) — parandatud

Auditeeritud kõik 15 kinnitatud `package-lock.json` faili. Haavatavused leiti ainult transitiivsetes sõltuvustes, mis tõi sisse MCP Inspector arendustööriist, OpenAI klient ja MCP SDK; kõik on nüüd lahendatud murdmatult näidistele:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ja **lab3/code/weather_mcp/inspector**: tõstetud `@modelcontextprotocol/inspector` versioonid (`0.16.6` / `0.14.1` → `0.22.0`), mis lahendasid kaasatud `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ja `ws` turvahoiatused. Lisatud npm `overrides` kirje, mis sunnib parandatud `shell-quote@1.8.4` kasutamist ülejäänud kriitilise hoiatuse kõrvaldamiseks `concurrently` pakendilt; mõlema lukustust failid on uuesti genereeritud (praegu 0 haavatavust).
- **03-GettingStarted/samples/typescript**: `npm audit fix` uuendas transitiivset `qs` (keskmine haavatavus) parandatud versioonile
- **03-GettingStarted/samples/javascript**: `npm audit fix` uuendas transitiivset `hono` (keskmine haavatavus) parandatud versioonile
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` uuendas transitiivset `form-data` (kõrge haavatavus) parandatud versioonile
- **03-GettingStarted/11-simple-auth/solution/typescript**: genereeritud puuduv `package-lock.json` fail, et projekti saaks korraga taastoota ja auditeerida (0 haavatavust)

#### Kooditaseme turvaparandus (OWASP A03: süstimine)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: eemaldatud `shell=True` `open_in_vscode` tööriistast. Varem `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` lubas shell-metakaraktereid kaustatee osana tõlgendada `cmd.exe`-s (käskude süstimise vektor). Nüüd käivitab ta otse lahendatud `Code.exe` koos kaustateega argumendina — ilma shellita — mis on funktsionaalselt ekvivalentne ja ohutu.

#### Pythoni sõltuvuste audit

- Auditeeritud kõik Python nõuete kokkupaketid `pip-audit` abil. Kataloogid `05-AdvancedTopics` ja `03-GettingStarted/samples/python` ei leidnud **pole teadaolevaid haavatavusi** (nende `mcp` / `httpx` / `pydantic` / `python-dotenv` versioonivahemikud lahenevad praegustele parandatud versioonidele)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` leidis transitiivse sõltuvuse **`werkzeug` 3.1.1** koos kolme `safe_join` Windowsi seadmenime DoS hoiatusega — `CVE-2025-66221`, `CVE-2026-21860` ja `CVE-2026-27199` (kõik parandatud versioonis 3.1.6). Lisatud turvalisuse lukustus `werkzeug>=3.1.6`, et lahendada parandus; kinnitatud, et piirang lahendub puhtalt koos `chainlit` / `mcp` / `semantic-kernel` virnaga

### Toote nime ümbernimetamine

Uuendatud kogu kursuse sisu Microsofti toote ümberbrändimise kajastamiseks:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: uuendatud Discordi kogukonna link
- **AGENTS.md**: uuendatud Discordi serveri viide
- **README.md**: uuendatud tehnoloogia ökosüsteemi viited
- **study_guide.md**: uuendatud juhtumiuuringu viited
- **05-AdvancedTopics/README.md**: uuendatud mooduli 5.13 pealkiri ja kirjeldus
- **05-AdvancedTopics/mcp-integration/README.md**: uuendatud jaotise päis ja kirjeldus
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: täielik mooduli pealkirja ja sisu uuendus
- **05-AdvancedTopics/mcp-security-entra/README.md**: uuendatud ristviide link
- **07-LessonsfromEarlyAdoption/README.md**: uuendatud juhtumiuuringu viited
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: uuendatud jaotise 9 päis, märgised ja võimalused
- **08-BestPractices/README.md**: uuendatud Discordi kogukonna link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: uuendatud Discordi kanali viide
- **09-CaseStudy/docs-mcp/solution/python/README.md**: uuendatud mudeli juurutamise viide
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: uuendatud AI teenuste tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: uuendatud ressursiviited

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Uuendatud peamise õppekava viited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Uuendatud mooduli pealkiri, ülevaade ja kõik mooduli päised
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Uuendatud pealkiri, õpieesmärgid, seadistamisjuhised ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Uuendatud pealkiri, õpieesmärgid, MCP hostide tabel ja ristviited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Uuendatud pealkiri, märgised, eeldused ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Uuendatud Agent Builder viited ja tagasiside link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Uuendatud eeldused ja laienduste viited

---

## 11. aprill 2026

### Uus õppetund, dokumentatsiooni parandused ja sõltuvuste uuendused

#### Lisatud uus õppekava sisu

**Moodul 05 - Täiustatud teemad**
- **Õppetund 5.17: Konkurentsivõimeline mitmeagentne arutelu MCP-ga** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uus põhjalik juhend mitmeagendi süsteemide konkurentsivõimelise arutelu mustri kohta
  - Mermaid arhitektuuri diagramm: kaks agenti → ühine MCP server → arutelu transkriptsioon → kohtunik → otsus
  - Ühine MCP tööriistade server (`web_search` + `run_python`) realiseeritud Pythonis ja TypeScriptis
  - Vastandlikud süsteemi käsud (POOLDUSEKS / VASTU / Kohtunik) koos selgete tööriistakasutusnõuetega
  - Arutelu korraldaja Pythonis, TypeScriptis ja C#-s, kes haldab voorusid ja juhib argumente
  - MCP `ClientSession` ühendused korraldajale reaalsete tööriistakutsete tegemiseks
  - Kasutusskeemid (hallutsinatsioonide tuvastamine, ohumudelid, API disaini ülevaade, faktide kontroll, tehnoloogia valik)
  - Turvakaalutlused: liivakasti-töötlus, tööriistakutsete valideerimine, päringute piiramise mehhanismid, auditilogimine
  - Struktureeritud harjutus kolme praktilise stsenaariumiga (koodi ülevaade, arhitektuuri otsus, sisuhalduse moderatsioon)

#### Dokumentatsiooni parandused

**Moodul 03 - Algus**
- **05-stdio-server/README.md**: Parandatud puudulik TypeScript stdio serveri näide — lisatud puuduv transpordi loomine (`new StdioServerTransport()`) ja `server.connect(transport)` kõne, et vastata Python ja .NET näidetele sama sektsiooni sees
- **14-sampling/README.md**: Parandatud trükkviga — "Sampling is an davanced features" muutus "Sampling is an advanced feature"

#### Õppekava uuendused

**Peamine README.md**
- Lisatud kirje 5.17 (Konkurentsivõimeline mitmeagentne arutelu MCP-ga) õppekava tabelisse koos otselingiga uude õppetundi

**05-AdvancedTopics/README.md**
- Lisatud Õppetund 5.17 rida õppetundide tabelisse

**study_guide.md**
- Lisatud Konkurentsivõimeline mitmeagentne arutelu teema mõttekaardile ja prose-kirjeldusele Täiustatud Tõemade osas

#### Koodi ja turvalisuse parandused

**Moodul 05 - Konkurentsivõimelised Agendid (`mcp-adversarial-agents`)**
- **Turvaparandus — käsu süstimine**: Asendatud TypeScripti `run_python` tööriistas `execSync` shell-interpolatsioon `execFile + promisify`-ga; käsukommandid nüüd edastatud argumendina ilma shelli vahenduseta, kõrvaldades käsu süstimise riski (LLM juhitud kood läbib nüüd täpselt argv elemendina)
- **MCP tööriistade tsükli ühendus**: Uuendatud Pythonis arutelu korraldaja kasutama `AsyncAnthropic` klienti (asendades blokeeriva sünkroonse `Anthropic`), edastama aktiivse `ClientSession` igale agentide voorule, hankima tööriistade definitsioonid iga vooru alguses `session.list_tools()` kaudu ning käivitama `tool_use` bloke läbi `session.call_tool()` tsüklis, kuni mudel annab lõpliku teksti vastuse

#### Sõltuvuste uuendused

- Uuendatud `hono` versiooniks 4.12.12 mitmes paketis (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uuendatud `@hono/node-server` TypeScript pakettides versioonile 1.19.13 (varem 1.19.11)
- Uuendatud Python pakettides (10-StreamliningAIWorkflows laborid 3 ja 4) `cryptography` versioon 46.0.7 peale (varem 46.0.5)
- Uuendatud `lodash` 10-StreamliningAIWorkflows inspektris versiooniks 4.18.1 (varem 4.17.23)

#### Tõlked

- Sünkroniseeritud tõlked 48+ keelde viimaste lähtefailide muudatustega (i18n uuendus)

---

## 5. veebruar 2026

### Üldine repositooriumi valideerimine ja navigeerimise parandused

#### Lisatud uus õppekava sisu

**Moodul 03 - Algus**
- **12-mcp-hosts/README.md**: Uus põhjalik juhend MCP hostide seadistamiseks
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfiguratsiooninäited
  - Kõigi peamiste hostide JSON konfiguratsioonimallid
  - Transpordi tüüpide võrdlustabel (stdio, SSE/HTTP, WebSocket)
  - Levinumate ühendusvigade lahendamine
  - Turvalisuse parimad praktikad hosti seadistamiseks

- **13-mcp-inspector/README.md**: Uus silumisjuhend MCP Inspectorile
  - Paigaldusmeetodid (npx, npm globaalselt, lähtekoodist)
  - Ühendamine serveritega stdio ja HTTP/SSE kaudu
  - Tööriistade, ressursside ja promptide testimise töövood
  - VS Code integratsioon MCP Inspectoriga
  - Levinumad silumisstsenaariumid lahendustega

**Moodul 04 - Praktiline rakendamine**
- **pagination/README.md**: Uus lehekülje jaotamise rakendamise juhend
  - Põhineb kursoril lehekülgede jaotamine Pythonis, TypeScriptis, Javas
  - Kliendipoolse lehekülgede haldus
  - Kursori kujunduse strateegiad (suletud vs struktureeritud)
  - Tulemuslikkuse optimeerimise soovitused

**Moodul 05 - Täiustatud teemad**
- **mcp-protocol-features/README.md**: Uus protokolli funktsioonide põhjalik ülevaade
  - Edenemise teavituste rakendamine
  - Päringu tühistamise mustrid
  - Ressursside mallid URI mustritega
  - Serveri elutsükli haldus
  - Logimise tasemete juhtimine
  - Vigade käsitlemise mustrid JSON-RPC koodidega

#### Navigeerimise parandused (24+ faili uuendatud)

**Peamised mooduli READMEd**
 Nüüd lingivad nii esimesele õppetunnile KUI ka järgnevasse moodulisse

**02-Security alamfailid**
- Kõigil 5 lisa turvalisusdokumendil on nüüd "Mis edasi" navigeerimine:

**09-Kasustamise uurimistöö failid**
- Kõigil kasustamise uurimistöö failidel on nüüd järjestikune navigeerimine:

**10-StreamliningAI Laborid**
 Lisatud Mis edasi sektsioon mooduli 10 ülevaatesse ja mooduli 11

#### Koodi ja sisu parandused

**SDK ja sõltuvuste uuendused**
Parandatud tühje openai versiooni märgistused `^4.95.0`
Uuendatud SDK versioon `^1.8.0` pealt `>=1.26.0`
Uuendatud mcp versiooni nõuded `>=1.26.0`

**Koodi parandused**
Parandatud valesti kirjutatud mudel `gpt-4o-mini` → `gpt-4.1-mini`

**Sisu parandused**
Parandatud katkine link `READMEmd` → `README.md`, parandatud õppekava päis `Module 1-3` → `Module 0-3`, parandatud suur-täht-sõltuv tee
Eemaldatud rikutud duplikaat Kasustamise uurimistöö 5 sisu

**Algajate juhendamise täiustused**
Lisatud korralik sissejuhatus, õpieesmärgid ja eeldused algajatele

#### Õppekava uuendused

**Peamine README.md**
- Lisatud kirjed 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Lehekülgede jagamine), 5.16 (Protokolli funktsioonid) õppekava tabelisse

**Mooduli READMEd**
Lisatud õppetunnid 12 ja 13 õppetundide nimekirja
Lisatud praktiliste juhendite sektsioon koos lehekülgede jagamise lingiga
Lisatud õppetunnid 5.15 (Kohandatud transpordi tüüp) ja 5.16 (Protokolli funktsioonid)

**study_guide.md**
- Uuendatud mõttekaart kõigi uute teemadega: MCP hostide seadistamine, MCP inspector, lehekülgede jagamise strateegiad, protokolli funktsioonide põhjalik käsitlus

## 28. jaanuar 2026

### MCP spetsifikatsiooni 2025-11-25 vastavuse ülevaatus

#### Põhikonseptsioonide täiustamine (01-CoreConcepts/)
- **Uus kliendi põhitüüp - Roots**: Lisatud põhjalik dokumentatsioon Roots kliendi põhitüübi kohta, mis võimaldab serveritel mõista failisüsteemi piiranguid ja ligipääsu õigusi
- **Tööriistade annotatsioonid**: Lisatud dokumentatsioon tööriistade käitumise annotatsioonide (`readOnlyHint`, `destructiveHint`) kohta paremate täitmiskäitumise otsuste tegemiseks
- **Tööriistakutsed proovimise ajal**: Uuendatud Sampling dokumentatsiooni, lisades parameetrid `tools` ja `toolChoice`, mis võimaldavad mudelil juhitud tööriistakutsed proovide päringute ajal
- **URL-režiimi ergutamine**: Lisatud dokumentatsioon URL-põhise ergutamise kohta serveripoolselt algatatud väliste veebitegevuste jaoks
- **Ülesanded (katsetusfaas)**: Lisatud uus jaotis, mis kirjeldab katsetusfaasis olevat ülesannete funktsiooni kestvate täitmiste katte ja tulemite hilise pärimise jaoks
- **Ikonite tugi**: Märgitud, et tööriistad, ressursid, ressursimallid ja promtid võivad nüüd sisaldada ikoone täiendava metaandmete tasandina

#### Dokumentatsiooni uuendused
- **README.md**: Lisatud MCP spetsifikatsiooni 2025-11-25 versiooniviide ja kuupõhine versioonihaldus
- **study_guide.md**: Uuendatud õppekava kaart, lisades Ülesanded ja Tööriistade annotatsioonid põhikonseptsioonide ossa; uuendatud dokumendi ajatemplit

#### Spetsifikatsiooni vastavuse kontroll
- **Protokolli versioon**: Kontrollitud, et kogu dokumentatsioon viitab ajakohasele MCP spetsifikatsioonile 2025-11-25
- **Arhitektuuri joondus**: Kinnitatud kahekihiline arhitektuur (Andmekiht + Transpordikiht) dokumentatsiooni õigsus
- **Põhitüübid dokumentatsioon**: Kinnitused serveripoolsed põhitüübid (Resources, Prompts, Tools) ja kliendipoolsed põhitüübid (Sampling, Elicitation, Logging, Roots)
- **Transpordimehhanismid**: Kontrollitud STDIO ja streamitava HTTP transpordi dokumentatsiooni vastavus
- **Turvajuhised**: Kinnitatud nõuete vastavus seni kehtivatele MCP turvalisuse parimatele tavadele

#### Peamised MCP 2025-11-25 funktsioonid dokumenteeritud
- **OpenID Connect leitavus**: Autentimiserverite leidmine läbi OIDC
- **OAuth kliendi ID metaandmed**: Soovitatud kliendi registreerimise mehhanismid
- **JSON skeem 2020-12**: MCP skeemide vaike-dialekt
- **SDK kihisüsteem**: Formaliseeritud SDK funktsioonide toetuse ja hoolduse nõuded
- **Juhtimismudel**: MCP juhtimisgruppide ja huvigruppide formeerimine

### Turvalisuse dokumentatsiooni põhitäiendused (02-Security/)

#### MCP turvalisuse tippkohtumise (Sherpa) töötoa integratsioon
- **Uus praktiline koolitusressurss**: Lisatud põhjalik integratsioon [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kogu turvadokumentatsiooni ulatuses
- **Ekspeditsiooni marsruut**: Dokumenteeritud täielik marsruut baaslaagrist tippu
- **OWASP joondus**: Kõik turvajuhtnöörid vastavad OWASP MCP Azure turvajuhendi riskidele

#### OWASP MCP Top 10 integreerimine
- **Uus sektsioon**: Lisatud OWASP MCP Top 10 turvariskide tabel Azure leevendustega põhiturvalisuse README-sse
- **Riskipõhine dokumentatsioon**: Uuendatud mcp-security-controls-2025.md OWASP MCP riskiviidetega iga turvavaldkonna kohta
- **Võrdlusarhitektuur**: Sidumine OWASP MCP Azure turvajuhendi võrdlusarhitektuuri ja rakendusmustritega

#### Uuendatud turvafailid
- **README.md**: Lisatud Sherpa töötoa ülevaade, ekspeditsioonimarsruudi tabel, OWASP MCP Top 10 riskide kokkuvõte ja praktilise koolituse sektsioon
- **mcp-security-controls-2025.md**: Uuendatud päis veebruar 2026, lisatud OWASP riskiviited (MCP01-MCP08), parandatud spetsifikatsiooni versioonide ebajärjekindlus
- **mcp-security-best-practices-2025.md**: Lisatud Sherpa ja OWASP ressursside sektsioon, ajatempli uuendus
- **mcp-best-practices.md**: Lisatud praktilise koolituse sektsioon Sherpa ja OWASP linkidega
- **azure-content-safety-implementation.md**: Lisatud OWASP MCP06 viide, Sherpa Camp 3 joondamine ja täiendav ressursside jaotis

#### Lisatud uued ressursiviited
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure turvajuhend](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuaalsed OWASP MCP riskilehed (MCP01-MCP10)

### Õppekava MCP spetsifikatsiooni 2025-11-25 kooskõlastus

#### Moodul 03 - Algus
- **SDK dokumentatsioon**: Lisatud Go SDK ametliku SDK nimekirja; uuendatud kõik SDK viited MCP spetsifikatsiooni 2025-11-25 versiooni järgi
- **Transpordi täpsustused**: Uuendatud STDIO ja HTTP streaming transpordi kirjeldused koos otseste spetsifikatsiooni viidetega

#### Moodul 04 - Praktiline rakendamine
- **SDK uuendused**: Lisatud Go SDK ja uuendatud SDK nimekiri MCP spetsifikatsiooni versiooniga
- **Autendusspetsifikatsioon**: Uuendatud MCP Authorization spetsifikatsiooni link 2025-11-25 versioonile

#### Moodul 05 - Täiustatud teemad
- **Uued funktsioonid**: Lisatud märkus MCP spetsifikatsiooni 2025-11-25 uutest funktsioonidest (Ülesanded, Tööriistade annotatsioonid, URL režiimi ergutamine, Roots)
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid täiendavatesse viidetesse

#### Moodul 06 - Kogukonnapanused
- **SDK nimekiri**: Lisatud Swift ja Rust SDKd; uuendatud spetsifikatsiooni link 2025-11-25 versioonile

#### Moodul 07 - Esialgsed kogemused
- **Ressursside värskendused**: Lisatud MCP spetsifikatsiooni 2025-11-25 link ja OWASP MCP Top 10 täiendavate ressurssidena

#### Moodul 08 - Parimad tavad
- **Spetsifikatsiooni versioon**: Uuendatud MCP spetsifikatsiooni viide versioonile 2025-11-25
- **Turbe ressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötuba täiendavatesse viidetes

#### Moodul 10 - AI töövoogude lihtsustamine
- **Sildi uuendus**: MCP versiooni silt muudetud SDK versioonilt (1.9.3) spetsifikatsiooni versioonile (2025-11-25)
- **Ressursside lingid**: Uuendatud MCP spetsifikatsiooni link; lisatud OWASP MCP Top 10

#### Moodul 11 - MCP serveri praktilised laborid
- **Spetsifikatsiooni viide**: Uuendatud MCP spetsifikatsiooni link versioonile 2025-11-25
- **Turbe ressursid**: Lisatud OWASP MCP Top 10 ametlikesse ressurssidesse

## 18. detsember 2025

### Turbedokumentatsiooni värskendus - MCP spetsifikatsioon 2025-11-25

#### MCP turbe parimad tavad (02-Security/mcp-best-practices.md) - spetsifikatsiooni versiooni uuendus
- **Protokolli versiooni uuendus**: Uuendatud viide uusimale MCP spetsifikatsioonile 2025-11-25 (avalikustatud 25. november 2025)
  - Uuendatud kõik spetsifikatsiooni versiooni viited 2025-06-18 asemel 2025-11-25
  - Uuendatud dokumendikuupäevad augusti 18, 2025 asemel detsember 18, 2025
  - Kontrollitud, et kõik spetsifikatsiooni URL-id osutavad kehtivale dokumentatsioonile
- **Sisu valideerimine**: Põhjalik turbe parimate tavade valideerimine uusimate standarditega
  - **Microsofti turbelahendused**: Kinnitatud kehtivad terminid ja lingid Prompt Shieldsi (varem "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID ja Azure Key Vault kohta
  - **OAuth 2.1 turbepraktikad**: Kinnitused kooskõlast sobivate OAuth turbestandarditega
  - **OWASP standardid**: OWASP Top 10 LLM-de kohta viidete ajakohasus
  - **Azure teenused**: Kõik Microsoft Azure dokumentatsiooni lingid ja parimad tavad on valideeritud
- **Standardite kooskõla**: Kõik viidatud turbestandardid on ajakohased
  - NIST AI riskijuhtimise raamistik
  - ISO 27001:2022
  - OAuth 2.1 turbe parimad tavad
  - Azure turbe- ja nõuetele vastavuse raamistikud
- **Rakendusressursid**: Kõik rakendamise juhendid ja ressursid on valideeritud
  - Azure API Management autentimismustrid
  - Microsoft Entra ID integratsioonijuhendid
  - Azure Key Vault saladuste haldamine
  - DevSecOps torujuhtmed ja jälgimislahendused

### Dokumentatsiooni kvaliteedi tagamine
- **Spetsifikatsioonile vastavus**: Kindlustatud, et kõik kohustuslikud MCP turbenõuded (PEAB/JÄÄB ÄRA) vastavad uusimale spetsifikatsioonile
- **Ressursside ajakohasus**: Kontrollitud kõik välimised lingid Microsofti dokumentatsiooni, turbestandardite ja rakendusjuhendite poole
- **Parimate tavade katvus**: Kinnitatud autentimise, autoriseerimise, AI-spetsiifiliste ohtude, tarneahela turbe ja ettevõtte mustrite täielik hõlmatus

## 6. oktoober 2025

### Sissejuhatuse sektsiooni laiendus – Täiustatud serveri kasutamine ja lihtne autentimine

#### Täiustatud serveri kasutamine (03-GettingStarted/10-advanced)
- **Uus peatükk lisatud**: Esitatud põhjalik juhend täiustatud MCP serveri kasutamiseks, hõlmates nii tavapäraseid kui madala taseme serveri arhitektuure.
  - **Tavapärane vs madala taseme server**: Üksikasjalik võrdlus ja kodeerimisnäited Pythonis ja TypeScriptis mõlemate lähenemiste kohta.
  - **Handler-põhine disain**: Tööriistade/ressursside/promptide haldamise selgitus handlerite kaudu skaleeritavate ja paindlike serverirakenduste jaoks.
  - **Praktilised mustrid**: Reaalse elu stsenaariumid, kus madala taseme serveri mustrid pakuvad eeliseid täiustatud funktsioonide ja arhitektuuri puhul.

#### Lihtne autentimine (03-GettingStarted/11-simple-auth)
- **Uus peatükk lisatud**: Samm-sammuline juhend lihtsa autentimise rakendamiseks MCP serverites.
  - **Autendi mõisted**: Selge selgitus autentimise ja autoriseerimise erinevustest ning volituste käitlemisest.
  - **Põhilise autentimise rakendus**: Middleware-põhised autentimismustrid Pythonis (Starlette) ja TypeScriptis (Express) koos koodinäidetega.
  - **Üleminek täiendatud turbele**: Juhised lihtsast autentimisest alustamiseks ja liikumiseks OAuth 2.1 ning RBAC suunas koos viidetega täiustatud turbemoodulitele.

Need lisandused pakuvad praktilist ja käed-küljes juhendit tugevamate, turvalisemate ja paindlikumate MCP serveri rakenduste loomiseks, ühendades põhikontseptsioonid täiustatud tootmismustritega.

## 29. september 2025

### MCP serveri andmebaasi integratsiooni laborid – põhjalik praktiline õppeprogramm

#### 11-MCPServerHandsOnLabs – uus täielik andmebaasi integreerimise õppekava
- **Täielik 13-labori õppeprogramm**: Lisatud põhjalik praktiline õppekava tootmisküpsete MCP serverite ehitamiseks PostgreSQL andmebaasi integratsiooniga
  - **Reaalse elu rakendus**: Zava Retail analüüsi juhtum demonstreerib ettevõttetaseme mustreid
  - **Struktureeritud õppeprotsess**:
    - **Laborid 00-03: Alused** – Sissejuhatus, põhiarhitektuur, turve ja mitmekasutajalisus, keskkonna seadistamine
    - **Laborid 04-06: MCP serveri ehitus** – Andmebaasi disain ja skeem, MCP serveri rakendus, tööriista arendus
    - **Laborid 07-09: Täiustatud funktsioonid** – Semantiline otsing, testimine ja silumine, VS Code integratsioon
    - **Laborid 10-12: Tootmine ja parimad tavad** – Paigaldusstrateegiad, jälgimine ja nähtavus, parimad tavad ja optimeerimine
  - **Ettevõtte tehnoloogiad**: FastMCP raamistik, PostgreSQL koos pgvectoriga, Azure OpenAI manused, Azure Container Apps, Application Insights
  - **Täiustatud funktsioonid**: Ridade taseme turve (RLS), semantiline otsing, mitmekasutajate andmete juurdepääs, vektormanused, reaalajas jälgimine

#### Terminoloogia standardiseerimine – moodulite ümbernimetamine laboriteks
- **Dokumentatsiooni põhjalik uuendus**: Süstemaatiliselt uuendatud kõik README failid 11-MCPServerHandsOnLabs kataloogis kasutama "Labor" termini "Mooduli" asemel
  - **Sektsioonide pealkirjad**: Uuendatud "What This Module Covers" → "What This Lab Covers" kõigis 13 laboris
  - **Sisu kirjeldus**: Muudetud "This module provides..." → "This lab provides..." kogu dokumentatsioonis
  - **Õpieesmärgid**: Uuendatud "By the end of this module..." → "By the end of this lab..."
  - **Navigatsioonilingid**: Kõik "Module XX:" viited muudetud "Lab XX:" formaati ristviidetes ja navigeerimisel
  - **Valmimise jälgimine**: Uuendatud "After completing this module..." → "After completing this lab..."
  - **Tehniliste viidete säilitamine**: Säilitatud Python moodulite viited konfiguratsioonifailides (nt `"module": "mcp_server.main"`)

#### Õppejuhendi täiustamine (study_guide.md)
- **Visuaalne õppekava kaart**: Lisatud uus jaotis "11. Andmebaasi integratsiooni laborid" koos põhjaliku laboristruktuuri visualiseeringuga
- **Repositsiooni struktuur**: Uuendatud kümnest üheteistkümneks põhiosaks, lisades detailse kirjelduse 11-MCPServerHandsOnLabs kohta
- **Õppeteekonna juhendid**: Täiendatud navigeerimisjuhiseid kaetavate sektsioonide 00-11 osas
- **Tehnoloogia hõlmatus**: Lisatud FastMCP, PostgreSQL ja Azure teenuste integratsiooni üksikasjad
- **Õpitulemused**: Rõhutatud tootmisküpsete serverite arendamist, andmebaasi integreerimise mustreid ja ettevõtte turbe aspekte

#### Põhijuhendi struktuuri täiustamine
- **Laboripõhine terminoloogia**: Uuendatud peamine README.md fail 11-MCPServerHandsOnLabs kataloogis, kasutades järjekindlalt laboristruktuuri
- **Õppeteekonna korraldus**: Selge areng alates põhikontseptsioonidest kuni täiustatud rakenduse ja tootmisseadistamiseni
- **Reaalse elu fookus**: Rõhuasetusega praktilisele, käed-küljes õppimisele ettevõtte tasemel mustrite ja tehnoloogiatega

### Dokumentatsiooni kvaliteedi ja järjepidevuse täiustused
- **Praktilise õppe rõhutamine**: Süvendatud laboripõhist lähenemist kogu dokumentatsioonis
- **Ettevõtte mustrite fookus**: Toodetud valmis lahendused ja ettevõtte turvalisus on esile tõstetud
- **Tehnoloogia integratsioon**: Kaetud kaasaegsed Azure teenused ja AI integratsiooni mustrid põhjalikult
- **Õppeteekonna areng**: Selge ja struktureeritud tee alates algtasemest kuni tootmisseadistamiseni

## 26. september 2025

### Juhtumiuuringute täiustamine – GitHub MCP registri integratsioon

#### Juhtumiuuringud (09-CaseStudy/) – ökosüsteemi arengu fookus
- **README.md**: Suur laiendus põhjaliku GitHub MCP registri juhtumiuuringuga
  - **GitHub MCP registri juhtumiuuring**: Uus põhjalik juhtumiuuring, mis analüüsib GitHub MCP registri lansseerimist 2025. aasta septembris
    - **Probleemi analüüs**: Üksikasjalik selgitus killustunud MCP serveri avastamise ja juurutamise väljakutsetest
    - **Lahenduse arhitektuur**: GitHubi tsentraliseeritud registri lähenemine ühe klõpsuga VS Code installatsiooniga
    - **Äriline mõju**: Mõõdetavad paranemised arendajate sisseelamisel ja tootlikkuses
    - **Strateegiline väärtus**: Modulaarsed agentide juurutamise ja tööriistadevahelise koostalitluse rõhutamine
    - **Ökosüsteemi areng**: Positsioneerimine aluseks agentide integreerimise platvormina
  - **Täiendatud juhtumiuuringute struktuur**: Kõik seitse juhtumiuuringut uuendatud ühtse vormingu ja põhjalike kirjeldustega
    - Azure AI reisibürood: mitme agendi orkestreerimise rõhk
    - Azure DevOps integratsioon: töövoo automatiseerimise fookus
    - Reaalaegne dokumentide taasesitus: Python konsoolikliendi rakendus
    - Interaktiivne õppeplaani generaator: Chainlit vestlev veebirakendus
    - Toimetaja sees dokumentatsioon: VS Code ja GitHub Copiloti integreerimine
    - Azure API Management: ettevõtte API integratsiooni mustrid
    - GitHub MCP registri: ökosüsteemi arenduse ja kogukonnaplatvormi fookus
  - **Kokkuvõte**: Ümberkirjutatud lõik, mis tõstab esile seitset juhtumiuuringut kattes erinevaid MCP rakendusvaldkondi
    - Ettevõtte integratsioon, mitme agendi orkestreerimine, arendaja tootlikkus
    - Ökosüsteemi arendus, hariduslikud rakendused
    - Täiustatud vaated arhitektuurimustritele, rakendusstrateegiatele ja parimatele tavadele
    - Rõhk MCP-le kui küpselt, tootmisküpselt protokollilt

#### Õppejuhendi uuendused (study_guide.md)
- **Visuaalne õppekava kaart**: Uuendatud mõttekaart lisades GitHub MCP registri juhtumiuuringute sektsiooni
- **Juhtumiuuringute kirjeldus**: Täiustatud üldistest kirjeldustest detailseks seitse põhjalikku juhtumiuuringut sisaldavaks jaotuseks
- **Repositsiooni struktuur**: Täiendatud sektsioon 10 peegeldamaks juhtumiuuringute laiahaardelisust ja üksikasju
- **Muudatuste ajalugu**: Lisatud 26. septembri 2025 sissekanne kajastamaks GitHub MCP registri lisamist ja juhtumiuuringute täiendusi
- **Kuupäevade uuendus**: Jaluse ajatempli värskendus viimasele versioonile (26. september 2025)

### Dokumentatsiooni kvaliteedi täiustused
- **Järjepidevuse parandamine**: Ühtlustatud juhtumiuuringute vorming ja struktuur kõigi seitse näite puhul
- **Põhjalikkus**: Juhtumiuuringud hõlmavad nüüd ettevõtte, arendaja tootlikkuse ja ökosüsteemi arenduse stsenaariumeid
- **Strateegiline positsioneerimine**: Tähelepanu MCP-le kui agentide süsteemide juurutamise alussambale
- **Ressursside integreerimine**: Täiendavate ressurssidena lisatud GitHub MCP registri lingid

## 15. september 2025

### Täiustatud teemade laiendus – kohandatud transpordid & konteksti inseneriteadus

#### MCP kohandatud transpordid (05-AdvancedTopics/mcp-transport/) – uus täiustatud rakendamise juhend
- **README.md**: Täielik juhend kohandatud MCP transpordimehhanismide rakendamiseks
  - **Azure Event Grid transpordikasutus**: Põhjalik serverivaba sündmuspõhine transpordi rakendus
    - C#, TypeScript ja Python näited koos Azure Functions integratsiooniga
    - Sündmustel põhinevad arhitektuurimustrid skaleeritavate MCP lahenduste jaoks
    - Veebikonksu (webhook) vastuvõtjad ja sõnumite edastamise kontroll
  - **Azure Event Hubs transpordikasutus**: Kõrge läbilaskevõimega voogedastuse transpordi rakendus
    - Reaalaegsed voogedastuse võimalused madala latentsusega stsenaariumides
    - Partitsioneerimise strateegiad ja kontrollpunktide haldus
    - Sõnumite grupeerimine ja jõudluse optimeerimine
  - **Ettevõtte integratsioonimustrid**: Tootmisküpsed arhitektuurinäited
    - Hajutatud MCP töötlemine mitme Azure Functioni vahel
    - Hübriidtranspordi arhitektuurid, kombineerides mitut transpordiliiki
    - Sõnumite vastupidavus, usaldusväärsus ja veakäsitluse strateegiad
  - **Turve ja monitooring**: Azure Key Vault integratsioon ja jälgimismustrid
    - Juhtimisidentiteedi autentimine ja least privilege ligipääs
    - Application Insights telemeetria ja jõudluse jälgimine
    - Lülitid (circuit breakers) ja riketele tolerantsemise mustrid
  - **Testimisraamistikud**: Põhjalikud testistrateegiad kohandatud transpordi jaoks
    - Ühiktestimine testtopside ja mockimise raamistikega
    - Integratsioonitestimine Azure Test Containers abil
    - Jõudluse ja koormustestimise kaalutlused

#### Konteksti inseneriteadus (05-AdvancedTopics/mcp-contextengineering/) – tekkiv AI valdkond
- **README.md**: Põhjalik ülevaade konteksti inseneriteadusest kui uue distsipliini sünnust
  - **Põhiprintsiibid**: Täielik konteksti jagamine, tegevuse otsustamise teadlikkus ja konteksti akna haldus
  - **MCP protokolli kooskõla**: Kuidas MCP disain lahendab konteksti inseneriteaduse väljakutseid
    - Konteksti akna piirangud ja progressiivse laadimise strateegiad
    - Asjakohasuse määramine ja dünaamiline konteksti pärimine
    - Mitmemodaalne konteksti käsitlemine ja turvaküsimused
  - **Rakendamisviisid**: Ühe keermega vs mitme agendi arhitektuurid
    - Konteksti lõikamine ja prioriseerimise tehnikad
    - Progressiivne konteksti laadimine ja tihendamise strateegiad
    - Kihiline konteksti lähenemine ja päringu optimeerimine
  - **Mõõtmise raamistik**: Tekkinud mõõdikud konteksti tõhususe hindamiseks
    - Sisendi efektiivsus, jõudlus, kvaliteet ja kasutajakogemus
    - Eksperimentaalsed lähenemised konteksti optimeerimiseks
    - Riketuvastus ja täiustuste metoodikad

#### Õppekava navigeerimise uuendused (README.md)
- **Täiendatud moodulistruktuur**: Uuendatud õppekava tabel, lisades uued täiustatud teemad
  - Lisatud Konteksti inseneriteadus (5.14) ja Kohandatud transpordid (5.15)
  - Järjekindel vormindus ja navigeerimislingid kõigi moodulite vahel
  - Uuendatud kirjeldused peegeldades praegust sisukogumit

### Kausta struktuuri täiustused
- **Nimede standardiseerimine**: Muudetud "mcp transport" nimeks "mcp-transport" koos teiste täiustatud teemade kaustadega kooskõlas
- **Sisu organiseerimine**: Kõik 05-AdvancedTopics kaustad järgivad nüüd ühtlast nimevormingut (mcp-[teema])

### Dokumentatsiooni kvaliteedi täiustused
- **MCP spetsifikatsiooni kooskõla**: Kõik uued sisud viitavad kehtivale MCP spetsifikatsioonile 2025-06-18
- **Mitmekeelsed näited**: Põhjalikud koodinäited C#, TypeScriptis ja Pythonis
- **Ettevõtte Keskendumine**: Tootmiseks valmis mustrid ja Azure pilve integratsioon kogu ulatuses
- **Visuaalne Dokumentatsioon**: Mermaid diagrammid arhitektuuri ja voogude visualiseerimiseks

## 18. august 2025

### Dokumentatsiooni Kattuv Uuendus - MCP 2025-06-18 Standardid

#### MCP Turbe Parimad Tavad (02-Security/) - Täielik Moderniseerimine
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täielik ümbersõnastus vastavalt MCP Spetsifikatsioonile 2025-06-18
  - **Kohustuslikud Nõuded**: Lisatud selged PEAJA/PEAJA MITTE nõuded ametliku spetsifikatsiooni järgi, koos selgete visuaalsete märkidega
  - **12 Põhiturbpraktiikat**: Struktureeritud tagasi 15-punktisest nimekirjast põhjalikeks turbaladeks
    - Tokeni Turvalisus & Autentimine, koos välist identiteedipakkuja integratsiooniga
    - Sessioonihaldus & Ülekande Turvalisus koos krüptograafiliste nõuetega
    - AI-spetsiifiline Ohtude Kaitse Microsoft Prompt Shieldsi integratsiooniga
    - Juurdepääsukontroll & Load koos minimaalsete õiguste põhimõttega
    - Sisu Turvalisus & Jälgimine Azure Content Safety integratsiooniga
    - Tarneahela Turvalisus põhjaliku komponentide kontrolliga
    - OAuth Turvalisus & Segadusseajamise Tõrje PKCE rakendusega
    - Intsidendis Vastus & Taastumine automatiseeritud võimekustega
    - Vastavus & Juhitavus regulatiivse joondumisega
    - Täiustatud Turvakontrollid nullusaldus arhitektuuriga
    - Microsoft Turbeökosüsteemi Integratsioon põhjalike lahendustega
    - Jätkuv Turbarände Evolutsioon kohanemise praktikatega
  - **Microsoft Turvalahendused**: Paranenud juhised Prompt Shieldsi, Azure Content Safety, Entra ID ja GitHub Advanced Security integreerimiseks
  - **Rakenduse Ressursid**: Kategooriate kaupa täielik ressursilinkide kogumik ametliku MCP dokumentatsiooni, Microsoft turvalahenduste, turbestandardite ja rakendusjuhendite alusel

#### Täiustatud Turvakontrollid (02-Security/) - Ettevõtte Rakendus
- **MCP-SECURITY-CONTROLS-2025.md**: Täielik uuendus ettevõtte tasemel turbiraamistiku jaoks
  - **9 Põhjalikku Turbaladade Kategooriat**: Laiendatud lihtsatest kontrollidest detailse ettevõtte raamistiku suunas
    - Täiustatud Autentimine & Autoriseerimine Microsoft Entra ID integratsiooniga
    - Tokeni Turvalisus & Anti-Passthrough Kontrollid põhjaliku valideerimisega
    - Sessiooniturbe Kontrollid ülevõtmise vältimiseks
    - AI-spetsiifilised Turbekontrollid prompt-injektsiooni ja tööriistamürgituse tõrjeks
    - Segadusseajamise Ründaja Tõrje OAuth-proxy turvalisusega
    - Tööriistade Käivitamise Turvalisus liivakasti ja isoleerimisega
    - Tarneahela Turbekontrollid sõltuvuste valideerimisega
    - Jälgimis- ja Tuvastamiskontrollid SIEM integratsiooniga
    - Intsidendile Vastus & Taastumine automatiseeritud võimekustega
  - **Rakendusnäited**: Lisatud detailset YAML konfiguratsiooni plokid ja koodinäited
  - **Microsoft Lahenduste Integratsioon**: Ulatuslik Azure turvateenuste, GitHub Advanced Security ja ettevõtte identiteedihalduse katvus

#### Täiustatud Turvateemad (05-AdvancedTopics/mcp-security/) - Tootmiseks valmis rakendus
- **README.md**: Täielik ümbersõnastus ettevõtte turvakasutuseks
  - **Praeguse Spetsifikatsiooni Joondus**: Uuendatud MCP Spetsifikatsiooniga 2025-06-18 ning kohustuslike turbenõuetega
  - **Täiustatud Autentimine**: Microsoft Entra ID integratsioon koos põhjalike .NET ja Java Spring Security näidetega
  - **AI Turbe Integratsioon**: Microsoft Prompt Shields & Azure Content Safety rakendus koos detailsete Python näidetega
  - **Edasijõudnud Ohtude Lõpetamine**: Põhjalikud rakendusnäited
    - Segadusseajamise Rünnete Tõrje PKCE ja kasutaja nõusoleku valideerimisega
    - Tokeni Passthrough Tõrje publikumi valideerimise ning turvalise tokeni haldusega
    - Sessioonivarguse Tõrje krüptograafiliste sidumiste ja käitumusliku analüüsiga
  - **Ettevõtte Turbe Integreerimine**: Azure Application Insights jälgimine, ohutuvastusvood ja tarneahela turvalisus
  - **Rakenduse Kontrollnimekiri**: Selgelt eristatud kohustuslikud ja soovitatud turvakontrollid Microsofti turbeökosüsteemi kasudega

### Dokumentatsiooni Kvaliteedi ja Standardite Joondamine
- **Spetsifikatsiooniviited**: Uuendatud kõik viited kehtivale MCP Spetsifikatsioonile 2025-06-18
- **Microsoft Turbeökosüsteem**: Paranenud kogu turbedokumentatsioonis integratsiooni juhised
- **Praktiline Rakendus**: Lisatud detailseid koodinäiteid .NET, Java ja Python keeltes koos ettevõtte mustritega
- **Ressursside Organiseerimine**: Põhjalik ametliku dokumentatsiooni, turbestandardite ja rakendusjuhendite kategooriline korraldus
- **Visuaalsed Näitajad**: Selged märgistused kohustuslike nõuete ja soovitatud tavade vahel

#### Põhikonseptsioonid (01-CoreConcepts/) - Täielik Moderniseerimine
- **Protokolli Versiooni Uuendus**: Uuendatud praeguse MCP Spetsifikatsiooni 2025-06-18 viidete järgi kuupäevapõhise versiooniga (AAAA-KK-PP formaat)
- **Arhitektuuri Täpsustus**: Parandatud Hosts, Clientide ja Serverite kirjeldused vastavalt MCP arhitektuurimustritele
  - Hosts nüüd selgelt defineeritud kui AI rakendused, mis koordineerivad mitut MCP kliendiühendust
  - Clientid kirjeldatud protokolli ühendajatena, hoides ühesuunalisi seoseid serveritega
  - Serverid täiustatud lokaalsete ja kaugjuhtimise juurutamise stsenaariumidega
- **Primitiivide Ümberkorraldus**: Täielik ülevaade serveri ja kliendi primitiividest
  - Serveri primitiivid: Ressursid (andmeallikad), Promptid (mallid), Tööriistad (täidetavad funktsioonid) koos detailsete seletuste ja näidetega
  - Kliendi primitiivid: Proovivõtt (LLM tulemused), Käitumist tekitav sisend, Logimine (silumine/jälgimine)
  - Uuendatud vastavalt praegustele avastamise (`*/list`), päringu (`*/get`) ja täitmise (`*/call`) meetodimustritele
- **Protokolli Arhitektuur**: Sissejuhatus kahetasandilisse arhitektuurimudelisse
  - Andmekiht: JSON-RPC 2.0 alus koos elutsükli halduse ja primitiividega
  - Ülekandekiht: STDIO (kohalik) ja Streamable HTTP koos SSE-ga (kaugreis)
- **Turberaamistik**: Põhjalikud turvapõhimõtted, mis sisaldavad selget kasutajanõusolekut, andmekaitset, tööriistade turvalisust ja ülekandekihtide turvalisust
- **Kommunikatsioonimustrid**: Uuendatud protokollisõnumid, mis katavad initsialiseerimist, avastamist, täitmist ja teavitamist
- **Koodinäited**: Uuendatud mitmekeelsete näidetega (.NET, Java, Python, JavaScript), peegeldamaks praeguseid MCP SDK mustreid

#### Turve (02-Security/) - Põhjalik Turbe Ümberehitamine  
- **Standardite Joondus**: Täielik viimine vastavusse MCP Spetsifikatsiooni 2025-06-18 turbenõuetega
- **Autentimise Evolutsioon**: Dokumenteeritud areng kohandatud OAuth serveritelt välist identiteedipakkujateni (Microsoft Entra ID)
- **AI-spetsiifiline Ohtude Analüüs**: Paranenud katvus tänapäevastele AI ründetüüpidele
  - Detailne prompt-injektsiooni rünnete stsenaarium koos reaalsete näidetega
  - Tööriistamürgituse mehhanismid ja "rug pull" ründemustrid
  - Kontekstiaknaramid ja mudelite segadusseajamise rünnakud
- **Microsoft AI Turvalahendused**: Täielik katvus Microsofti turbeökosüsteemist
  - AI Prompt Shieldsid täiustatud tuvastamise, esiletõstmise ja delimiteerimistehnikatega
  - Azure Content Safety integratsioonimustrid
  - GitHub Advanced Security tarneahela kaitseks
- **Edasijõudnud Ohtude Lõpetamine**: Põhjalikud turvakontrollid
  - Sessioonivargused MCP-spetsiifiliste rünnete ja krüptograafiliste sessioonide ID nõuetega
  - Segadusseajamise probleemid MCP proxy stsenaariumites koos selgete nõusolekute nõuetega
  - Tokeni passthrough haavatavused kohustusliku valideerimisega
- **Tarneahela Turvalisus**: Laiendatud AI tarneahela katvus, sealhulgas alusmudelid, embeddings teenused, konteksti pakkujad ja kolmanda osapoole API-d
- **Alusrakenduse Turvalisus**: Paranenud integratsioon ettevõtte turbemustritega, kaasa arvatud nullusaldus arhitektuur ja Microsofti turbeökosüsteem
- **Ressursside Korraldus**: Kategooriline täielike ressursside linkide kogumik tüübi järgi (Ametlikud Dokumendid, Standardid, Uuringud, Microsoft Lahendused, Rakendusjuhendid)

### Dokumentatsiooni Kvaliteedi Parandused
- **Struktureeritud Õppe Eesmärgid**: Paranenud kindlad, teostatavad tulemused
- **Ristviited**: Lisatud lingid seotud turbe- ja põhikontseptsiooni teemade vahel
- **Uuendatud Info**: Kõik kuupäevad ja spetsifikatsiooni lingid uuendatud vastavalt kehtivatele standarditele
- **Rakendusjuhised**: Lisatud spetsiifilised ja teostatavad juhised mõlemas jaotises

## 16. juuli 2025

### README ja Navigatsiooni Parandused
- Kurrikulum navigatsioon täielikult ümber kujundatud README.md-s
- Asendatud `<details>` sildid ligipääsetavama tabelipõhise vorminguga
- Loodud alternatiivsed paigutuse valikud uues "alternative_layouts" kaustas
- Lisatud kaardipõhist, sakkide stiilis ning akordionstiilis navigatsiooni näited
- Uuendatud hoidla struktuuri sektsioon hõlmamaks kõiki uusimaid faile
- Parandatud "Kuidas seda kurrikulumit kasutada" selgete soovitustega
- Uuendatud MCP spetsifikatsiooni lingid õigete URL-idega
- Lisatud Konteksti Inseneri jaotis (5.14) kurrikulu struktuuri

### Õppejuhendi Uuendused
- Õppejuhend täielikult läbi vaadatud ja joondatud kehtiva hoidla struktuuriga
- Lisatud uued jaotised MCP Klientide ja Tööriistade ning Populaarsete MCP Serverite kohta
- Uuendatud Visuaalne Kurrikulum Kaart kõigi teemade täpseks kuvamiseks
- Parandatud Täiustatud Teemade kirjeldusi kõigi spetsialiseeritud alade hulgas
- Uuendatud Juhtumiuuringute jaotis tegelike näidetega
- Lisatud see põhjalik muudatuste logi

### Kogukonna Panused (06-CommunityContributions/)
- Lisatud põhjalik info MCP serverite kohta pildigeneratsiooni jaoks
- Lisatud põhjalik jaotis Claude kasutamisest VSCode’is
- Lisatud Cline terminalikliendi seadistus ja kasutusjuhised
- Uuendatud MCP kliendi jaotis kõigi populaarsete klientide variantidega
- Parandatud panusnäited täpsemate koodinäidetega

### Täiustatud Teemad (05-AdvancedTopics/)
- Kõik spetsialiseeritud teemakaustad organiseeritud järjepidevate nimetustega
- Lisatud konteksti insenerimise materjalid ja näited
- Lisatud Foundry agendi integratsiooni dokumentatsioon
- Parandatud Entra ID turbeintegreerimise dokumentatsioon

## 11. juuni 2025

### Algne Loomine
- Avaldatud MCP Algajatele kurrikulu esimene versioon
- Loodud baasstruktuur kõigi 10 põhiajava jaoks
- Rakendatud Visuaalne Kurrikulum Kaart navigatsiooniks
- Lisatud esialgsed näidisprojektid mitmes programmeerimiskeeles

### Alustamine (03-GettingStarted/)
- Loodud esimesed serveri rakendusnäited
- Lisatud kliendi arenduse juhend
- Kaasatud LLM kliendi integratsiooni juhised
- Lisatud VS Code integratsiooni dokumentatsioon
- Rakendatud Server-Sent Events (SSE) serverinäited

### Põhikonseptsioonid (01-CoreConcepts/)
- Lisatud põhjalik kliendi-serveri arhitektuuri selgitus
- Loodud dokumentatsioon võtmeprotokolli komponentidest
- Dokumenteeritud sõnumimustrid MCP-s

## 23. mai 2025

### Hoidla Struktuur
- Algatatud hoidla baasfailide struktuur
- Loodud README failid iga suurema jaotise jaoks
- Seatud üles tõlkeinfrastruktuur
- Lisatud pildid ja diagrammid

### Dokumentatsioon
- Loodud esialgne README.md koos kurrikulu ülevaatega
- Lisatud CODE_OF_CONDUCT.md ja SECURITY.md
- Seatud SUPPORT.md abi saamise juhistega
- Loodud esialgne õppejuhendi struktuur

## 15. aprill 2025

### Planeerimine ja Raamistiku Loomine
- MCP Algajatele kurrikulu algplaneerimine
- Määratletud õpieesmärgid ja sihtrühm
- Kirjeldatud 10-jaotise struktuur kurrikulule
- Arendatud kontseptuaalne raamistik näidete ja juhtumiuuringute jaoks
- Loodud esialgsed prototüüpnäited võtmekontseptsioonidest

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
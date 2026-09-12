# Muudatuste logi: MCP algajate õppekava

See dokument toimib kõigi Model Context Protocol (MCP) algajate õppekavas tehtud oluliste muudatuste registrina. Muudatused on dokumenteeritud pöördses kronoloogilises järjekorras (kõige uuemad muudatused ees).

## 9. september 2026

### MCP 2026-07-28 lõpliku spetsifikatsiooni joondamine

Uuendatud ingliskeelne õppekava release-kandidaadi ja `2025-11-25`
baasjoonist lõpliku MCP `2026-07-28` spetsifikatsiooni vastu.

- **Uuendatud**: Praeguse versiooni viited, spetsifikatsiooni lingid, staaditud
  päringu juhised, `server/discover`, voogedastatavad HTTP päised ja ülesannete
  laienduselu tsükkel 38 ingliskeelses dokumentatsioonifailis.
- **Parandatud**: Elicitation kasutab nüüd `elicitation/create`, Sampling kasutab
  `sampling/createMessage` ning `InputRequiredResult.resultType` kasutab
  `"input_required"`.
- **Asendatud**: Ebatäpne Root Context vestlusstaadi õppetund asendatud
  protokollile vastava Roots õppetunniga, mis katab infoteadlikke failisüsteemi vihjeid,
  praegust mitmekordse ringkäigu voogu, turvapiire ja migratsioonivõimalusi.
- **Selgitatud**: Roots, Sampling, Logging ja Dynamic Client Registration on
  `2026-07-28` versioonis aegunud, koos soovitatud asenduste ja varaseima
  eemaldamise kuupäevaga dokumenteeritud.
- **Sildistatud**: Näited, mis sõltuvad endiselt MCP `2025-11-25`, HTTP+SSE,
  initsialiseerimiskäteviisidest või protokollisessioonidest, hoitakse pärandühilduvuse
  näidetena, mitte mitteakutsetava rakendusena.
- **Turvajuhised**: Uuendatud eraldiseisvad turva juhendid kasutama
  päringu-põhist autoriseerimist ja selgeid rakenduse oleku käsitlejaid eemaldatud
  protokollisessiooni ID-de asemel. Kliendi ID metaandmedokumentid on nüüd
  eelistatud registreerimise tee, DCR dokumenteeritud kui ainult ühilduvus.
- **Tugimaterjalid**: Uuendatud õpi juhend, kaastöötajate kontrollnimekiri,
  Publora juhtumiuuring ja APIM juhtumiuuring. APIM läbivaade soovitab nüüd
  oma voogedastatavat HTTP `/mcp` lõpp-punkti asemel aegunud `/sse`.
- **Kanonilised lingid**: Asendatud lõpetatud ja mustandi spetsifikatsiooni URL-id
  ingliskeelse lähte Markdowni versioonitud `2026-07-28` linkidega,
  säilitades aga nähtavad lingid pärandi versioonidele seal, kus näide on
  vanema tööriistaga lukustatud.
- **Stabiilsed failinimed**: Nimeti lõplik spetsifikatsiooni juhend ja kaks turvajuhendit
  ümber, eemaldades release-kandidaadi ja aastasildi ning uuendades kõiki
  ingliskeelseid hüperlinke nende stabiilsete radade järjekorda.
- **Uus autoriseerimisnäide**: Lisatud testitud
  [TypeScript MCP `2026-07-28` ressursiserver](./02-Security/samples/cimd-dcr-auth/README.md),
  mis võrdleb eelistatud Kliendi ID Metaandmedokumente aegunud dünaamilise
  kliendi registreerimise varukoopiaga. Näide sisaldab RFC 9728 avastust,
  JWKS valideerimist, tööriistadeüleseid õigusi, tosinat testi ja Auth0 seadistusjuhendit.
- **Tõlkeulatus**: Muudetud on ainult ingliskeelsed lähtefailid; genereeritud






Lisatud tarnijast sõltumatu kaaslase õppetund MCP tööriistadele, mis loovad reaalse maailma


- **Uus**: [Usaldusväärsuse abikomponendi kaaslase õppetund][reliability-sidecar]
  kasutab ühte tugipileti lugu, kahte Mermaid diagrammi ja korduskatses
  otsustuslõiku sujuvaks toimimise võti, aatomiline dubleerimississepääs,
  kokkusobitamine, tõendid ja ülesannete laienduse piirid selgitamiseks.
- **Uus**: Standardteegipõhine Python ja SQLite rike-söödu harjutus kasutab
  eraldi töötluse ja piletite andmehoidlaid, et demonstreerida vastust, mis kaob
  pärast välist efekti sooritamist. Kuus deterministlikku testi katavad naiivset
  dubleerimist, kaitstud taaskäivituse taaste, koormuse konflikte, vahemällu pandud tulemusi,
  aktiivseid nõudeid ja samaaegset dubleerimississepääsu.
- **Uuendatud**: Moodul 08 lingib nüüd kaaslase õppetundi, määratleb
  lõpliku `2026-07-28` staatilse päringu mudeli, eristab OpenTelemetry
  jälgitavust aegunud MCP logimisfunktsioonist ning piirab oma üldist
  korduskatsenäidet ainult lugemisoperatsioonide jaoks.
- **Valikuline**: Õppetund seob oma kaasaskantavad kontseptsioonid ühe märgistatud
  kogukonna rakendusega ilma, et hostitud teenus või võrguühendus oleks osa










- **Uus**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — täismahus õppetund, mis käsitleb staatilist protokolli tuuma (algse `initialize` käepigistuse ning `Mcp-Session-Id` eemaldamine), uusi `Mcp-Method`/`Mcp-Name` marsruutingupäiseid, `ttlMs`/`cacheScope` vahemällu salvestamise metaandmeid, W3C Trace Context `_meta` sees, formaalset laiendusraamistikku (MCP rakendused ja uus Ülesannete laiendus), kuut volituste tugevdamise SEP-i, Roots/Sampling/Logging aegumist ja üleminekut täielikule JSON Schema 2020-12 tööriistade skeemidele.
- **Uuendatud** tulevikku suunatud viidetega, mis ühendavad uue õppetunniga:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolli versiooni märkus, Sampling/Roots/Logging/Tasks sektsioonid ja "Mis järgmiseks"
  - [02-Security/README.md](./02-Security/README.md): volituste tugevdamise juhis
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): staatilise transpordi juhis
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling aegumise juhis

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): seisundivaba/seansi-reisituse välja toomine
  - [README.md](./README.md): "Vaatame ette" märkus spetsifikatsiooni sektsioonis ja uus `1.1` kirje õppekava moodulitabelis
  - [study_guide.md](./study_guide.md): edasipilgav punkt Tuumikkontseptsioonide ülevaates ja dateeritud lisa märkus
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): välja toomine `mcp-session-id` transpordikaardilt enne seisundivaba päringu mudelit
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): mooduli ülevaate välja toomine Root Contexts/Sampling aegumiste ja Tasks laienduse kohta
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autoriseerimise tugevdamise välja toomine

## 24. juuni 2026

### Uus õppetund: MCP kasutamine Copiloti rakenduses

- [Tööriistade sektsioon](./12-tooling/README.md) Lisatud tööriistade sektsioon.
- [MCP Copiloti rakenduses](./12-tooling/01-copilot-app/README.md)

## 16. juuni 2026

### MCP spetsifikatsiooni joondamine & näidise valideerimine

Valideeriti õppekava vastavalt kehtivale **MCP Spetsifikatsioonile 2025-11-25** ja viimastele ametlikele SDK-dele, seejärel parandati kõik aegunud spetsifikatsiooni viited ning kinnitati, et tuumiknäidised ikkagi ehituvad ja töötavad.

#### Spetsifikatsiooni versiooniparandused (2025-06-18 / 2025-03-26 → 2025-11-25)

Uuendatud ingliskeelset sisu seal, kus see väitis veel vanema spetsifikatsioonimuudatuse olevat *kehtiv/viimane* standard ning suunatud lingid uuesti kanonilistele `modelcontextprotocol.io` spetsifikatsiooni radadele:
- **05-AdvancedTopics/mcp-security/README.md**: Uuendatud "Kehtiv standard" bänner, sissejuhatus, tuumik turvapõhimõtete pealkiri, kohustuslike nõuete pealkiri, Microsoft Entra ID sektsioon, Viited & Ressursid lingid ning lõplik turvateade (8 viidet) versioonile 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Uuendatud Lisavahendite spetsifikatsiooni link ja "Kehtiv standard" bänner versioonile 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Asendatud aegunud `2025-03-26` turvalisuse-ja-usaldusväärsuse link praeguse 2025-11-25 turvalisuse parimate tavade lehega
- **03-GettingStarted/14-sampling/README.md**: Uuendatud ametlik proovitöö dokumentide link versioonile 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Uuendatud oleviku "kehtiv MCP spetsifikatsioon" viide ja Lisavahendite spetsifikatsiooni link versioonile 2025-11-25 (ajaloolised SSE aegumise märkused jäid täpsuseks alles)

#### Näidise valideerimine kehtivate SDK-dega

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` lahendas `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` möödus ilma tüübivigadeta — olemasolevad `McpServer`/`StdioServerTransport` API-d jäid kehtima
- **Python (03-GettingStarted/01-first-server/solution/python)**: Valideeritud isoleeritud `.venv` keskkonnas `mcp[cli]` (1.27.2); `py_compile` õnnestus ja `FastMCP.list_tools()` tagastas korrektselt tööriistad `add` ja `subtract`
- Kinnitatud, et kõik näidises kasutatud `@modelcontextprotocol/sdk` versioonivahemikud (`>=1.26.0` / `^1.26.0` / `^1.27.0`) lahenevad puhtalt praegusele `1.29.0` versioonile ilma API murdmiseta

#### Sõltuvuste täpsustamine (versioonivahede sulgemine)

Tõstetud aegunud SDK versioonid nii, et iga näidis jälgib kehtivat MCP versiooni, vastavalt kogu repositooriumi konventsioonile:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Tõstetud `@modelcontextprotocol/sdk` `^1.8.0` → `>=1.26.0` ja uuendatud aegunud `"updated for MCP 2025-06-18"` paketi kirjeldus versioonile `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ja **lab4/code/github_mcp_server/pyproject.toml**: Tõstetud täpne versioonipiirang `mcp==1.23.0` → `mcp>=1.26.0`; uuesti genereeritud mõlemad `uv.lock` failid (`uv lock`), nii et lukustusfailid lahenevad praegusele `mcp 1.27.2` versioonile ning püsivad manifestidega sünkroonis

#### Õppekava lünkade analüüs — uusima spetsifikatsiooni funktsioonide kaetus

Kinnitatud, et õppekava hõlmab juba kõiki põhielemente, mis MCP 2025-11-25 toob või laiendab, seega sisulünki pole jäänud:
- **Proovi võtmine**: Õppetund 03-GettingStarted/14-sampling ning 05-AdvancedTopics/mcp-sampling
- **Andmete kogumine (sh URL režiim)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Juured**: Dokumenteeritud 00-Introduction, 01-CoreConcepts ja 05-AdvancedTopics/mcp-root-contexts
- **Ülesanded (katseversioon, pikaajalised toimingud)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Tööriista märkused** (`readOnlyHint` / `destructiveHint`): Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features

### Turvalisuse tugevdamine ja sõltuvuste haavatavuste parandamine

Läbiviidud täielik turvastaatus kõigi sõltuvuste manifestid ja näidise lähtekoodi kohta, seejärel lahendatud kõik npm-i hoiatuste teated ning üks koodi tasandi leidmine. Pärast parandusi annab `npm audit` aru iga kontrollitud kataloogi kohta **0 haavatavust**.

#### npm sõltuvuste haavatavused (kaudsed) — Parandatud

Kontrollitud kõiki 15 kaustas salvestatud `package-lock.json` faili. Haavatavused piirdusid kaudsete sõltuvustega, mis toodi MCP Inspector arendusriista, OpenAI kliendi ning MCP SDK kaudu; kõik on nüüd lahendatud ilma näidiste purunemiseta:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ja **lab3/code/weather_mcp/inspector**: Uuendatud `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), mis kustutas kaasatud `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ja `ws` hoiatused. Lisatud npm `overrides` kirje, mis sunnib parendatud `shell-quote@1.8.4` kasutamist, et likvideerida `concurrently` poolt kantud ülejäänud kriitiline hoiatus; mõlema lukufaili ümberregeneratsioon (nüüd 0 haavatavust)
- **03-GettingStarted/samples/typescript**: `npm audit fix` uuendas transitiivset `qs` (keskmine) parandatud versioonini
- **03-GettingStarted/samples/javascript**: `npm audit fix` uuendas transitiivset `hono` (keskmine) parandatud versioonini
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` uuendas transitiivset `form-data` (kõrge) parandatud versioonini
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genereeritud puuduolev `package-lock.json`, nii et projekt on reprodutseeritav ja auditeeritav (0 haavatavust)

#### Kooditaseme turvaparandus (OWASP A03: Süstimine)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Eemaldatud `shell=True` `open_in_vscode` tööriistast. Varem `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` lubas kausta tee sees shell-metamärke tõlgendada `cmd.exe` poolt (käskude süstimise vektor). Nüüd käivitab otse lahendatud `Code.exe` kaustaga argumendina — ilma shellita — mis on funktsionaalselt samaväärne ja turvaline

#### Python'i sõltuvuste audit

- Auditeeritud iga Python'i nõuete komplekt `pip-audit` abil. `05-AdvancedTopics` ja `03-GettingStarted/samples/python` ei leidnud **tuntud haavatavusi** (nende `mcp` / `httpx` / `pydantic` / `python-dotenv` vahemikud lahenduvad praegustesse parandatud väljaannetesse)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` tuvastas transitiivse sõltuvuse **`werkzeug` 3.1.1** kolme `safe_join` Windowsi seadmenime DoS hoiatusena — `CVE-2025-66221`, `CVE-2026-21860` ja `CVE-2026-27199` (kõik parandatud versioonis 3.1.6). Lisatud konkreetne turvapin `werkzeug>=3.1.6`, et lahendatakse parandatud väljaanne; kontrollitud, et tingimus lahendub puhtalt `chainlit` / `mcp` / `semantic-kernel` staki puhul

### Toote nime ümberbrändimine

Uuendatud kogu õppesisu vastamaks Microsofti toote ümberbrändimisele:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Uuendatud Discordi kogukonna link
- **AGENTS.md**: Uuendatud Discordi serveri viide
- **README.md**: Uuendatud tehnoloogia ökosüsteemi viited
- **study_guide.md**: Uuendatud juhtumiuuringu viited
- **05-AdvancedTopics/README.md**: Uuendatud mooduli 5.13 pealkiri ja kirjeldus
- **05-AdvancedTopics/mcp-integration/README.md**: Uuendatud sektsiooni päis ja kirjeldus
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Täielik mooduli pealkirja ja sisu uuendus
- **05-AdvancedTopics/mcp-security-entra/README.md**: Uuendatud ristviite link
- **07-LessonsfromEarlyAdoption/README.md**: Uuendatud juhtumiuuringu viited
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Uuendatud jaotise 9 päis, märgised ja võimed
- **08-BestPractices/README.md**: Uuendatud Discordi kogukonna link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Uuendatud Discordi kanali viide
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Uuendatud mudeli juurutuse viide
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Uuendatud AI teenuste tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Uuendatud ressursside viited

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Uuendatud põhilise õppekava viited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Uuendatud mooduli pealkiri, ülevaade ja kõik mooduli päised
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Uuendatud pealkiri, õpieesmärgid, seadistusjuhised ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Uuendatud pealkiri, õpieesmärgid, MCP hostide tabel ja ristviited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Uuendatud pealkiri, märgised, eeltingimused ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Uuendatud Agent Builder'i viited ja tagasiside link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Uuendatud eeltingimused ja laienduste viited

---

## 11. aprill 2026

### Uus õppetund, dokumentatsiooni parandused ja sõltuvuste uuendused

#### Lisatud uus õppekava sisu

**Moodul 05 - Täiendavad teemad**
- **Õppetund 5.17: Konfliktne mitme agendi põhjendamine MCP-ga** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uus põhjalik juhend konflikti-debati mustrist mitme agendi süsteemide jaoks
  - Mermaidi arhitektuuri diagramm: kaks agenti → jagatud MCP server → debati transkriptsioon → kohtunik → lahendus
  - Jagatud MCP tööriista server (`web_search` + `run_python`) teostatud Pythonis ja TypeScriptis
  - Vastuolulised süsteemi kehtestused (FOR / AGAINST / Judge) koos selgete tööriistakasutuse nõuetega
  - Debati orkestreerija Pythonis, TypeScriptis ja C#-s, haldades voorusid ja argumentide marsruutimist
  - MCP `ClientSession` ühendamine orkestreerijale päristööriistakõnede jaoks
  - Kasutusjuhtumite tabel (hallutsinatsioonide tuvastamine, ohumudelite koostamine, API disaini ülevaade, faktide kontroll, tehnika valik)
  - Turvaküsimused: liivakastis käitamine, tööriistakõnede valideerimine, kiiruse piiramine, auditeerimise logimine
  - Struktureeritud harjutus kolme praktilise stsenaariumiga (koodi ülevaade, arhitektuuri otsus, sisumajandus)

#### Dokumentatsiooni parandused

**Moodul 03 - Algus**
- **05-stdio-server/README.md**: Parandas mittetäieliku TypeScript stdio serveri näite — lisati puuduolev transpordinietamine (`new StdioServerTransport()`) ja `server.connect(transport)` kõne, et vastata Python ja .NET näidetele samas jaotises
- **14-sampling/README.md**: Parandas trükivea — parandatud `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Õppekava uuendused

**Põhijuhend README.md**
- Lisatud sissekanne 5.17 (Konfliktne mitme agendi põhjendamine MCP-ga) õppekava tabelisse koos otselinkiga uuele õppetunnile

**05-AdvancedTopics/README.md**
- Lisatud õppetunni 5.17 rida õppetundide tabelisse

**study_guide.md**
- Lisatud Konfliktse mitme agendi põhjendamise teema mõttekaardile ja täiendavate teemade tekstikirjeldusse

#### Koodi ja turvaparandused

**Moodul 05 - Konflikt-agendid (`mcp-adversarial-agents`)**
- **Turvaparandus — käsu süstimine**: Asendatud `execSync` shell-interpolatsioon `execFile` + `promisify` abil TypeScripti `run_python` tööriistas, eemaldades käsu süstimise pinnase (LLM juhitud kood edastatakse nüüd kirjaliku argv elemendina ilma shelli osaluseta)
- **MCP tööriistade tsükli juhtimine**: Uuendatud Python'i debati orkestreerija kasutama `AsyncAnthropic` klienti (asendades blokeeriva süntroonse `Anthropic`), edastama igale agendi voorule otse live `ClientSession`, pärima tööriistade definitsioone iga vooru jaoks `session.list_tools()` kaudu ja saatma `tool_use` plokke `session.call_tool()` tsüklis kuni mudel genereerib lõpliku tekstvastuse

#### Sõltuvuste uuendused

- Uuendatud `hono` versiooniks 4.12.12 mitmetes pakkides (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uuendatud `@hono/node-server` 1.19.11 → 1.19.13 TypeScripti pakkides
- Uuendatud `cryptography` 46.0.5 → 46.0.7 Python'i pakkides (10-StreamliningAIWorkflows laboris 3 ja 4)
- Uuendatud `lodash` 4.17.23 → 4.18.1 10-StreamliningAIWorkflows inspektoris

#### Tõlked

- Sünkroniseeritud tõlked 48+ keelde viimaste lähte muudatustega (i18n uuendus)

---

## 5. veebruar 2026

### Terve repositooriumi valideerimise ja navigeerimise täiustused

#### Lisatud uus õppekava sisu

**Moodul 03 - Algus**
- **12-mcp-hosts/README.md**: Uus põhjalik juhend MCP hostide seadistamiseks
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfiguratsiooni näited
  - JSON konfiguratsioonimallid kõigi peamiste hostide jaoks
  - Transporditüüpide võrdlustabel (stdio, SSE/HTTP, WebSocket)
  - Levinud ühendusprobleemide tõrkeotsing
  - Parimad turvatavad hostide konfiguratsioonis

- **13-mcp-inspector/README.md**: Uus MCP Inspektori tõrkeotsingu juhend
  - Paigaldamisviisid (npx, npm global, lähtekoodist)
  - Ühendamine serveritega stdio ja HTTP/SSE kaudu
  - Testitööriistad, ressursid ja promptide töövood
  - VS Code integreerimine MCP Inspektoriga
  - Levinud tõrkeotsingu stsenaariumid koos lahendustega

**Moodul 04 - Praktiline rakendus**
- **pagination/README.md**: Uus lehekülgede lõikamise teostamise juhend
  - Kursoripõhised lehekülgede lõikamise mustrid Pythonis, TypeScriptis, Javas
  - Kliendipoolse lehekülgede haldamine
  - Kursoridisaini strateegiad (suletud vs struktureeritud)
  - Jõudluse optimeerimise soovitused

**Moodul 05 - Täiendavad teemad**
- **mcp-protocol-features/README.md**: Uus põhjalik protokolli funktsioonide ülevaade
  - Edusammuteate teostus
  - Päringu katkestamise mustrid
  - Ressursimallid URI mustritega
  - Serveri elutsükli haldus
  - Logimise taseme juhtimine
  - Vea haldamise mustrid JSON-RPC koodidega

#### Navigeerimise parandused (uuendatud 24+ faili)

**Põhimooduli README.d**
 Nüüd lingid nii esimesele õppetunnile KUI järgnevale moodulile

**02-Security alamfailid**
- Kõik 5 täiendavat turvadokumenti on nüüd "Mis järgmiseks" navigeerimisega varustatud:

**09-CaseStudy failid**
- Kõik juhtumiuuringu failid on nüüd järjestikuse navigeerimisega varustatud:

**10-StreamliningAI laboris**
Lisatud Mis järgmiseks sektsioon Moodulisse 10 ülevaates ja Moodulisse 11

#### Koodi ja sisu parandused

**SDK ja sõltuvuste uuendused**
Parandatud tühi openai versiooniks `^4.95.0`
Uuendatud SDK versiooniks `>=1.26.0` (varasemalt `^1.8.0`)
Uuendatud mcp versioonipinnid `>=1.26.0`

**Koodi parandused**
Parandatud vale mudel `gpt-4o-mini` → `gpt-4.1-mini`

**Sisu parandused**
Parandatud purunenud link `READMEmd` → `README.md`, parandatud õppekava päis `Module 1-3` → `Module 0-3`, parandatud suurustundlik teekond
Eemaldatud rikutud duplikaat Case Study 5 sisu

**Algajate juhendamise parandused**
Lisatud korrektne sissejuhatus, õpieesmärgid ja eeltingimused algajatele

#### Õppekava uuendused

**Põhijuhend README.md**
- Lisatud sissekanded 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Lehekülgede lõikamine), 5.16 (Protokolli funktsioonid) õppekava tabelisse

**Moodulite README.d**
Lisatud õppetunnid 12 ja 13 õppetundide nimekirja
Lisatud Praktilised juhendid jaotis lehekülgede lõikamise lingiga
Lisatud õppetunnid 5.15 (Kohandatud Transport) ja 5.16 (Protokolli funktsioonid)

**study_guide.md**
- Uuendatud mõttekaart kõigi uute teemadega: MCP Hosts seadistus, MCP Inspector, lehekülgede lõikamise strateegiad, protokolli funktsioonide põhjalik ülevaade

## 28. jaanuar 2026

### MCP spetsifikatsiooni 2025-11-25 vastavuse ülevaade

#### Põhikontseptsioonide täiustamine (01-CoreConcepts/)
- **Uus kliendi primitiiv - Roots**: Lisatud põhjalik dokumentatsioon Roots kliendi primitiivi kohta, võimaldades serveritel mõista failisüsteemi piire ja juurdepääsuõigusi
- **Tööriistade märgendid**: Lisatud dokumentatsioon tööriistade käitumismärkmete kohta (`readOnlyHint`, `destructiveHint`), et parandada tööriistade täitmise otsuseid
- **Tööriistade kutsumine proovivõtmisel**: Uuendatud proovivõtmise dokumentatsiooni, lisades `tools` ja `toolChoice` parameetrid mudelipõhiseks tööriistakutsumiseks proovivõtmise päringute käigus
- **URL režiimi tuvastamine**: Lisatud dokumentatsioon URL-põhise tuvastamise kohta serveri algatatud väliste veebiside toimingute jaoks
- **Ülesanded (eksperimentaalne)**: Lisatud uus jaotis, mis dokumenteerib eksperimentaalset Ülesannete funktsiooni kestvate täitmispakendite ja tulemuste edasi lükitud hankimise jaoks

- **Ikonide tugi**: Märgitud, et tööriistad, ressursid, ressursside mallid ja üleskutsed võivad nüüd sisaldada ikoone täiendava metainformatsioonina

#### Dokumentatsiooni uuendused
- **README.md**: Lisatud MCP spetsifikatsiooni 2025-11-25 versiooni viide ja kuupõhine versiooni selgitus
- **study_guide.md**: Uuendatud õppekava kaart, lisades ülesanded ja tööriistade annotatsioonid põhikontseptsioonide sektsiooni; uuendatud dokumendi kuupäev

#### Spetsifikatsiooni vastavuse kontroll
- **Protokolli versioon**: Kinnitatud, et kogu dokumentatsioon viitab kehtivale MCP spetsifikatsioonile 2025-11-25
- **Arhitektuuri joondus**: Kinnitatud kahekihilise arhitektuuri (andmekiht + transpordikiht) dokumentatsiooni täpsus
- **Primitiivide dokumentatsioon**: Kontrollitud serveri primitiive (ressursid, üleskutsed, tööriistad) ja kliendi primitiive (valim, andmete kogumine, logimine, juured)
- **Transpordimehhanismid**: Kinnitatud STDIO ja voogedastatava HTTP transpordi dokumentatsiooni täpsus
- **Turvalisuse juhised**: Kinnitatud vastavus kehtivatele MCP turvalisuse headele praktikatele

#### Olulised MCP 2025-11-25 omadused dokumenteeritud
- **OpenID Connect avastus**: Autentimisserveri avastus OIDC kaudu
- **OAuth kliendi ID metaandmete dokumendid**: Soovitatud kliendi registreerimise mehhanism
- **JSON skeem 2020-12**: MCP skeemide määratluste vaike dialekt
- **SDK kihistamissüsteem**: Formaliseeritud nõuded SDK funktsioonide toetuseks ja hoolduseks
- **Juhtimisstruktuur**: Formaliseeritud MCP juhtimisvõrgustikud ja huvigruppide struktuur

### Turvalisuse dokumentatsiooni põhiuuendus (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integreerimine
- **Uus praktiline koolitusressurss**: Lisatud ulatuslik integratsioon [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kogu turvalisuse dokumentatsiooni ulatuses
- **Ekspeditsiooni marsruudi kajastus**: Dokumenteeritud täielik laager-laager üleminek baaskomandopunktist tippu
- **OWASP-iga joondus**: Kõik turvalisuse juhised nüüd kooskõlas OWASP MCP Azure Security Guide riskidega

#### OWASP MCP Top 10 integreerimine
- **Uus sektsioon**: Lisatud OWASP MCP Top 10 turvariskide tabel Azure leevendustega peamise turvalisuse README-sse
- **Riskipõhine dokumentatsioon**: Uuendatud mcp-security-controls-2025.md koos OWASP MCP riskiviidetega igas turvavaldkonnas
- **Viidearhitektuur**: Linkitud OWASP MCP Azure Security Guide viidearhitektuuri ja rakendusmustritele

#### Uuendatud turvafailid
- **README.md**: Lisatud Sherpa töötoa ülevaade, ekspeditsiooni marsruudi tabel, OWASP MCP Top 10 riskide kokkuvõte ja praktilise koolituse sektsioon
- **mcp-security-controls-2025.md**: Uuendatud päis veebruariks 2026, lisatud OWASP riskiviited (MCP01-MCP08), parandatud spetsifikatsiooni versiooni vastuolu
- **mcp-security-best-practices-2025.md**: Lisatud Sherpa ja OWASP ressursside sektsioon, uuendatud ajatemplit
- **mcp-best-practices.md**: Lisatud praktilise koolituse sektsioon Sherpa ja OWASP linkidega
- **azure-content-safety-implementation.md**: Lisatud OWASP MCP06 viide, Sherpa Camp 3 joondus ja täiendavate ressursside sektsioon

#### Uued ressursside lingid lisatud
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuaalsed OWASP MCP riskilehed (MCP01-MCP10)

### Õppekava ulatuslik MCP spetsifikatsiooni 2025-11-25 joondus

#### Moodul 03 - Algus
- **SDK dokumentatsioon**: Lisatud Go SDK ametliku SDK nimekirja; uuendatud kõik SDK viited MCP spetsifikatsioonile 2025-11-25 vastavalt
- **Transpordi täpsustus**: Uuendatud STDIO ja HTTP voogedastuse transpordi kirjeldused koos otseste spetsifikatsiooni viidetega

#### Moodul 04 - Praktiline rakendus
- **SDK uuendused**: Lisatud Go SDK; uuendatud SDK nimekiri koos spetsifikatsiooni versiooni viitega
- **Autentimise spetsifikatsioon**: Uuendatud MCP autentimise spetsifikatsiooni link kehtivale 2025-11-25 versioonile

#### Moodul 05 - Täiustatud teemad
- **Uued omadused**: Lisatud märkus MCP spetsifikatsiooni 2025-11-25 uutest omadustest (Ülesanded, Tööriistade annotatsioonid, URL-režiimi andmeküsitlused, Juured)
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid täiendavatele viidetele

#### Moodul 06 - Kogukonna panused
- **SDK nimekiri**: Lisatud Swift ja Rust SDKd; uuendatud spetsifikatsiooni link 2025-11-25
- **Spetsifikatsiooni viide**: Uuendatud MCP spetsifikatsiooni link otse spetsifikatsiooni URL-ile

#### Moodul 07 - Varased praktikad
- **Ressursside uuendused**: Lisatud MCP spetsifikatsiooni 2025-11-25 link ja OWASP MCP Top 10 täiendavatesse ressurssidesse

#### Moodul 08 - Head praktikad
- **Spetsifikatsiooni versioon**: Uuendatud MCP spetsifikatsiooni viide 2025-11-25
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötuba täiendavates viidetes

#### Moodul 10 - AI töövoogude sujuvamaks muutmine
- **Märgistuse uuendus**: Muudetud MCP versiooni märk SDK versioonilt (1.9.3) spetsifikatsiooni versioonile (2025-11-25)
- **Ressursside lingid**: Uuendatud MCP spetsifikatsiooni link; lisatud OWASP MCP Top 10

#### Moodul 11 - MCP serveri praktilised töötoad
- **Spetsifikatsiooni viide**: Uuendatud MCP spetsifikatsiooni link 2025-11-25 versioonile
- **Turvaressursid**: Lisatud OWASP MCP Top 10 ametlike ressursside hulka

## 18. detsember 2025

### Turvalisuse dokumentatsiooni uuendus - MCP spetsifikatsioon 2025-11-25

#### MCP turvalisuse head praktikad (02-Security/mcp-best-practices.md) - spetsifikatsiooni versiooni uuendus
- **Protokolli versiooni uuendus**: Uuendatud viide uusimale MCP spetsifikatsioonile 2025-11-25 (välja antud 25. november 2025)
  - Uuendatud kõik spetsifikatsiooni versiooni viited 2025-06-18 -> 2025-11-25
  - Uuendatud dokumendi kuupäeva viited 18. august 2025 -> 18. detsember 2025
  - Kontrollitud, et kõik spetsifikatsiooni URLid viitavad kehtivale dokumentatsioonile
- **Sisu valideerimine**: Ulatuslik turvalisuse headade praktikate vastavuse kontroll viimaste standarditega
  - **Microsofti turvalahendused**: Kinnitatud tänapäevane terminoloogia ja lingid Prompt Shieldile (varem "vanglakaristuste riskide tuvastamine"), Azure Content Safety, Microsoft Entra ID ja Azure Key Vaulti kohta
  - **OAuth 2.1 turvalisus**: Kinnitatud vastavus uusimatele OAuth turvapraktikatele
  - **OWASP standardid**: Kontrollitud, et OWASP Top 10 LLMide kohta viited on ajakohased
  - **Azure teenused**: Kontrollitud kõik Microsoft Azure dokumentatsiooni lingid ja head praktikad
- **Standardite joondus**: Kõik viidatud turvastandardid kinnitatud ajakohasteks
  - NIST AI riskijuhtimise raamistik
  - ISO 27001:2022
  - OAuth 2.1 turvalisuse head praktikad
  - Azure turbe- ja vastavusraamistikud
- **Rakendamisjuhised**: Kinnitatud kõik rakendusjuhiste lingid ja ressursid
  - Azure API haldamise autentimismustrid
  - Microsoft Entra ID integreerimisjuhendid
  - Azure Key Vaulti salajaste andmete haldus
  - DevSecOps torujuhtmed ja jälgimislahendused

### Dokumentatsiooni kvaliteedi tagamine
- **Spetsifikatsiooni nõuete järgimine**: Kinnitatud, et kõik kohustuslikud MCP turvanõuded (PEAB/PEAB MITTE) vastavad uusimale spetsifikatsioonile
- **Ressursside ajakohasus**: Kontrollitud kõik välised lingid Microsofti dokumentatsioonile, turvastandarditele ja rakendusjuhistele
- **Heade praktikate ulatus**: Kinnitatud põhjalik katvus autentimise, autoriseerimise, AI spetsiifiliste ohtude, tarneahela turvalisuse ja ettevõtte mustrite osas

## 6. oktoober 2025

### Algusosa laiendus – Täiustatud serveri kasutus ja lihtne autentimine

#### Täiustatud serveri kasutus (03-GettingStarted/10-advanced)
- **Uus peatükk lisatud**: Esitatud põhjalik juhend täiustatud MCP serveri kasutusele, hõlmates nii regulaarset kui madala taseme serveri arhitektuuri.
  - **Regulaarne vs madala taseme server**: Detailne võrdlus ning koodinäited Pythonis ja TypeScriptis mõlema lähenemise kohta.
  - **Handler-põhine disain**: Selgitus vahendipõhisest tööriistade/ressursside/üleskutsete haldamisest skaleeritavate ja paindlike serverirakenduste jaoks.
  - **Praktilised mustrid**: Reaalsed stsenaariumid, kus madala taseme serverimustrid on kasulikud täiustatud funktsioonide ja arhitektuuri jaoks.

#### Lihtne autentimine (03-GettingStarted/11-simple-auth)
- **Uus peatükk lisatud**: Samm-sammuline juhend lihtsa autentimise rakendamiseks MCP serverites.
  - **Autentimise kontseptsioonid**: Selge selgitus autentimise ja autoriseerimise erinevustest ning tõendite käsitlemisest.
  - **Lihtsa autentimise rakendamine**: Vahevara-põhised autentimismustrid Pythonis (Starlette) ja TypeScriptis (Express), koodinäidetega.
  - **Arene turvalisuse suunas**: Juhised, kuidas alustada lihtsa autentimisega ja liikuda edasi OAuth 2.1 ja RBAC juurde, viidates täiustatud turvamoodulitele.

Need täiendused pakuvad praktilist käed-külge juhendit tugevamate, turvalisemate ja paindlikumate MCP serveri rakenduste loomiseks, ühendades põhikontseptsioonid täiustatud tootmispraktikatega.

## 29. september 2025

### MCP serveri andmebaasi integreerimise töötoad - põhjalik praktiline õppekava

#### 11-MCPServerHandsOnLabs - uus täismahus andmebaasi integreerimise õppekava
- **Täielik 13 töötoa õppekava**: Lisatud ulatuslik praktiline õppekava tootmisvalmis MCP serverite loomiseks PostgreSQL andmebaasi integratsiooniga
  - **Reaalmaailma rakendus**: Zava Retail analüütika kasutusjuht, näidates ettevõtte tasemel mustreid
  - **Struktureeritud õppeprotsess**:
    - **Töötoad 00-03: Alused** - Sissejuhatus, põhiarhitektuur, turvalisus ja mitmiküüriline funktsionaalsus, keskkonna seadistamine
    - **Töötoad 04-06: MCP serveri ehitamine** - Andmebaasi disain ja skeem, MCP serveri rakendamine, tööriistade arendus  
    - **Töötoad 07-09: Täiustatud funktsioonid** - Semantiline otsing, testimine ja silumine, VS Code integratsioon
    - **Töötoad 10-12: Tootmine ja head praktikad** - Juhtimise strateegiad, monitooring ja jälgitavus, head praktikad ja optimeerimine
  - **Ettevõtte tehnoloogiad**: FastMCP raamistik, PostgreSQL koos pgvectoriga, Azure OpenAI embeddid, Azure Container Apps, Application Insights
  - **Täiustatud omadused**: Rea taseme turvalisus (RLS), semantiline otsing, mitme kliendi andmete ligipääs, vektori embeddid, reaalajas monitooring

#### Terminoloogia standardiseerimine - mooduli töötoaks muutmine
- **Põhjalik dokumentatsiooni uuendus**: Süsteemne kõigi README failide uuendus 11-MCPServerHandsOnLabs kataloogis, kasutades "Töötuba" terminoloogiat "Mooduli" asemel
  - **Sektsioonide pealkirjad**: Muudetud "Mis see moodul katab" kõigis 13 töökohas "Mis see töötuba katab"
  - **Sisu kirjeldus**: Muudetud "See moodul pakub..." vormingust "See töötuba pakub..." üle kogu dokumentatsioonis
  - **Õpieesmärgid**: Muudetud "Selle mooduli lõpuks..." vormingust "Selle töötoa lõpuks..." 
  - **Navigatsioonilingid**: Kõik "Moodul XX:" viited muudetud "Töötuba XX:"-ks ristviidetes ja navigeerimisel
  - **Lõpetamise jälgimine**: Muudetud "Pärast selle mooduli lõpetamist..." vormingust "Pärast selle töötoa lõpetamist..."
  - **Tehnilised viited säilitatud**: Säilitatud Python mooduliviited konfiguratsioonifailides (nt `"module": "mcp_server.main"`)

#### Õppematerjali täiustamine (study_guide.md)
- **Visuaalne õppekava kaart**: Lisatud uus sektsioon "11. Andmebaasintegreerimise töötoad" koos põhjaliku töötoa struktuuri visualiseerimisega
- **Kataloogi struktuur**: Uuendatud kümnest üheteistkümneks põhiosaks koos detailselt 11-MCPServerHandsOnLabs kirjeldusega
- **Õpimarsruudi juhendamine**: Täiustatud navigeerimisjuhised hõlmates sektsioone 00-11
- **Tehnoloogiate katvus**: Lisatud FastMCP, PostgreSQL, Azure teenuste integratsiooni detailid
- **Õpitulemused**: Tõstetud esile tootmisvalmis serveri arendus, andmebaasi integratsiooni mustrid ja ettevõttesektori turvalisus

#### Peamise README struktuuri täiustamine
- **Töötuba-põhine terminoloogia**: Uuendatud põhi README.md 11-MCPServerHandsOnLabs kaustas järjekindlalt kasutama "Töötuba" struktuuri
- **Õpimarsruudi korraldus**: Selge areng alates põhikontseptsioonidest kuni täiustatud rakenduste ja tootmise juurutamiseni
- **Reaalmaailma fookus**: Rõhutatud praktilist, käed-külge õppe lähenemist ettevõtte tasemel mustrite ja tehnoloogiatega

### Dokumentatsiooni kvaliteedi ja järjepidevuse parandused
- **Praktilise õppe rõhutamine**: Kinnitatud praktiline, töötubade-põhine lähenemine kogu dokumentatsioonis
- **Ettevõtte mustrite fookus**: Tõstetud esile tootmisvalmis rakendused ja ettevõtte turvapõhimõtted
- **Tehnoloogia integratsioon**: Ulatuslik kaetus kaasaegsetest Azure teenustest ja AI integreerimise mustritest
- **Õppimise areng**: Selge, struktureeritud tee põhikontseptsioonidest tootmisjuurutuseni

## 26. september 2025

### Juhtumiuuringute täiustamine - GitHub MCP registri integreerimine

#### Juhtumiuuringud (09-CaseStudy/) - ökosüsteemi arendamise fookus
- **README.md**: Suur laiendus ulatusliku GitHub MCP registri juhtumiuuringuga
  - **GitHub MCP registri juhtumiuuring**: Uus põhjalik juhtumiuuring, uurides GitHub MCP registri käivitust 2025. aasta septembris
    - **Probleemi analüüs**: Detailne läbivaatus killustatud MCP serveri avastamise ja juurutamise väljakutsetest
    - **Lahenduse arhitektuur**: GitHubi tsentraliseeritud registri lahendus koos ühe-klõpsuga VS Code installiga
    - **Äriline mõju**: Mõõdetavad parendused arendajate käibele ja tootlikkuses
    - **Strateegiline väärtus**: Fookus modulaarsele agendi juurutusele ja tööriistadevahelisele koostalitlusvõimele
    - **Ökosüsteemi areng**: Positsioneerimine alustalaks agentuursel integratsioonil
  - **Täiendatud juhtumiuuringute struktuur**: Kõigi seitsme juhtumiuuringu värskendamine ühetaolise vormingu ja ulatuslike kirjeldustega
    - Azure AI reisisekretärid: Mitme agendi orkestreerimise rõhuasetus
    - Azure DevOpsi integratsioon: Töövoo automatiseerimise fookus
    - Reaalajas dokumentatsiooni tuvastus: Python konsoolikliendi rakendus
    - Interaktiivne õppekava generaator: Chainlit vestlev veebirakendus

    - Toimetaja sees olev dokumentatsioon: VS Code ja GitHub Copilot integratsioon
    - Azure API haldus: Ettevõtte API integratsioonimustrid
    - GitHub MCP register: Ökosüsteemi arendus ja kogukonna platvorm
  - **Ülevaatlik kokkuvõte**: ümber kirjutatud kokkuvõtte osa, kus on välja toodud seitse juhtumiuuringut, mis hõlmavad MCP rakendamise mitmeid dimensioone
    - Ettevõtte integreerimine, mitmeagendi orkestreerimine, arendaja tootlikkus
    - Ökosüsteemi arendus, hariduslike rakenduste kategoriseerimine
    - Täiustatud ülevaated arhitektuurimustritest, rakendusstrateegiatest ja parimatest tavade näidetest
    - Rõhk MCP-l kui küpsel, tootmiskõlblikul protokollil

#### Õppejuhendi uuendused (study_guide.md)
- **Visuaalne õppekava kaart**: uuendatud mõttekaart, et lisada GitHub MCP register juhtumiuuringute sektsiooni
- **Juhtumiuuringute kirjeldus**: parendatud üldistest kirjetest detailseks seitse ulatusliku juhtumiuuringu jaotuseks
- **Arhiivi struktuur**: uuendatud 10. sektsioon, mis kajastab ulatuslikku juhtumiuuringute katvust spetsiifiliste rakenduste detailidega
- **Muudatuste logi integreerimine**: lisatud 26. septembri 2025 sissekanne, dokumenteerides GitHub MCP registri lisamise ja juhtumiuuringute täiustused
- **Kuupäeva uuendused**: jaluses uuendatud viimase versiooni kuupäev (26. september 2025)

### Dokumentatsiooni kvaliteedi parendused
- **Järjepidevuse parandamine**: ühetaoline juhtumiuuringute vorming ja struktuur kõigi seitsme näite puhul
- **Ülevaatlik katvus**: juhtumiuuringud hõlmavad nüüd ettevõtte, arendaja tootlikkuse ja ökosüsteemi arenduse stsenaariume
- **Strateegiline positsioneerimine**: rõhuasetuse tugevdamine MCP-l kui agentide süsteemi paigaldamise alusplatvormil
- **Ressursside integreerimine**: täiendatud lisavahendite jaotist GitHub MCP registri lingiga

## 15. september 2025

### Täiendatud teemade laiendus – Kohandatud transpordid ja konteksti inseneriteadus

#### MCP kohandatud transpordid (05-AdvancedTopics/mcp-transport/) – uus täiustatud rakendusjuhend
- **README.md**: täielik juhend kohandatud MCP transpordimehhanismide rakendamiseks
  - **Azure Event Gridi transport**: ulatuslik serverivaba sündmuspõhine transpordirakendus
    - näited C#, TypeScripti ja Pythoni keeles Azure Functions integratsiooniga
    - sündmuspõhised arhitektuurimustrid skaleeritavate MCP lahenduste jaoks
    - webhook vastuvõtjad ja sõnumite push-tüüpi töötlemine
  - **Azure Event Hubsi transport**: suure läbilaskevõimega voogedastus transpordi rakendus
    - reaalajas voogedastus madala latentsusega stsenaariumite jaoks
    - partitsioneerimisstrateegiad ja punktide haldus
    - sõnumite partiide töötlemine ja jõudluse optimeerimine
  - **Ettevõtte integratsioonimustrid**: tootmiskõlblikud arhitektuuri näited
    - hajutatud MCP töötlemine mitme Azure Functioni vahel
    - hübriidtranspordi arhitektuurid, mis kombineerivad mitut transporditüüpi
    - sõnumite vastupidavuse, usaldusväärsuse ja veakäsitluse strateegiad
  - **Turvalisus ja jälgimine**: Azure Key Vault integratsioon ja jälgitavuse mustrid
    - hallatava identiteedi autentimine ja minimaalsete õiguste põhimõte
    - Application Insights telemeetria ja jõudluse jälgimine
    - kaitselülitid ja tõrketaluvuse mustrid
  - **Testimisraamistikud**: kõikehõlmavad testimisstrateegiad kohandatud transpordite jaoks
    - üksuse testimine testtopiste ja mokkimisraamistikega
    - integratsioonitestimine Azure Test Containersiga
    - jõudluse ja koormustestimise kaalutlused

#### Konteksti inseneriteadus (05-AdvancedTopics/mcp-contextengineering/) – tekkiv AI eriala
- **README.md**: põhjalik uurimus konteksti inseneriteadusest kui tekkivast valdkonnast
  - **Põhiprintsiibid**: täielik konteksti jagamine, tegevuseotsuste teadlikkus ja konteksti akna haldus
  - **MCP protokolli kooskõlastamine**: kuidas MCP disain lahendab konteksti inseneriteaduse väljakutseid
    - konteksti akna piirangud ja progressiivse laadimise strateegiad
    - asjakohasuse määramine ja dünaamiline konteksti hankimine
    - multimodaalne konteksti käsitlemine ja turvaküsimused
  - **Rakendamise lähenemised**: ühesuunalised vs mitmeagendi arhitektuurid
    - kontekstitükkide jaotamine ja prioriseerimise tehnikad
    - progressiivne konteksti laadimine ja pakkimise strateegiad
    - kihilised konteksti lähenemised ja hankimise optimeerimine
  - **Mõõtmise raamistik**: tekkivad mõõdikud konteksti tõhususe hindamiseks
    - sisendite efektiivsus, jõudlus, kvaliteet ja kasutajakogemuse kaalutlused
    - eksperimentaalsed lähenemised konteksti optimeerimiseks
    - rikete analüüs ja parendusmeetodid

#### Õppekava navigeerimise uuendused (README.md)
- **Täiustatud moodulistruktuur**: uuendatud õppekava tabel, et hõlmata uusi täiustatud teemasid
  - lisatud Konteksti inseneriteadus (5.14) ja kohandatud transport (5.15)
  - järjepidev vormindus ja navigeerimislingid kõigi moodulite vahel
  - uuendatud kirjeldused, et kajastada praegust sisukattvust

### Kaustastruktuuri parandused
- **Nimede standardiseerimine**: ümber nimetatud "mcp transport" kujule "mcp-transport" kooskõlas teiste täiustatud teemade kaustadega
- **Sisu organiseerimine**: kõik 05-AdvancedTopics kaustad järgnevad nüüd ühtsele nimetamismustrile (mcp-[teema])

### Dokumentatsiooni kvaliteedi täiendused
- **MCP spetsifikatsiooni kooskõlastamine**: kogu uus sisu viitab MCP spetsifikatsioonile 2025-06-18
- **Mitmekeelsed näited**: põhjalikud koodinäited C#, TypeScripti ja Pythoni keeles
- **Ettevõtte fookus**: tootmiskõlblikud mustrid ja Azure pilve integratsioon kõigis osades
- **Visuaalne dokumentatsioon**: Mermaid diagrammid arhitektuuri ja voo visualiseerimiseks

## 18. august 2025

### Dokumentatsiooni põhjalik uuendus – MCP 2025-06-18 standardid

#### MCP turvalisuse parimad praktikad (02-Security/) – täielik moderniseerimine
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: täielik ümberkirjutus kooskõlas MCP spetsifikatsiooniga 2025-06-18
  - **Kohustuslikud nõuded**: lisatud selged PEAB/PEAB MITTE nõuded ametlikust spetsifikatsioonist koos visuaalsete indikaatoritega
  - **12 põhiturvalisuse praktikat**: ümber struktuuritud 15-kohalisest loendist laiaulatuslikeks turva valdkondadeks
    - Tokeni turvalisus ja autentimine välishalduri integratsiooniga
    - Sessiooni haldus ja transpordi turvalisus krüptograafiliste nõuetega
    - Tehisintellekti spetsiifiline ohu kaitse Microsoft Prompt Shieldi integratsiooniga
    - Juurdepääsukontroll ja õigused minimaalsete privileegidega
    - Sisu turvalisus ja jälgimine Azure Content Safety integratsiooniga
    - Tarneahela turvalisus põhjaliku komponentide kontrolliga
    - OAuth turvalisus ja Confused Deputy rünnakute ennetamine PKCE rakendusega
    - Intsidendihaldus ja taastumine automatiseeritud võimalustega
    - Nõuetele vastavus ja juhtimine regulatiivse kooskõlastusega
    - Täiustatud turvakontrollid nullusaldus arhitektuuri alusel
    - Microsofti turvaökosüsteemi integratsioon laiaulatuslike lahendustega
    - Turvalisuse pidev areng adaptatiivsete praktikatega
  - **Microsofti turvalahendused**: parendatud integreerimisjuhendid Prompt Shieldsi, Azure Content Safety, Entra ID ja GitHub Advanced Security jaoks
  - **Rakendamise ressursid**: kategooriastatud allikad ametliku MCP dokumentatsiooni, Microsofti turvalahenduste, turvastandardite ja rakendusjuhiste kaupa

#### Täiustatud turvakontrollid (02-Security/) – ettevõtte rakendus
- **MCP-SECURITY-CONTROLS-2025.md**: täielik ülevaatus ettevõtte tasemel turvasüsteemiga
  - **9 laiaulatuslikku turvavaldkonda**: põhikontrollidest täpse ettevõtte raamistiku juurde
    - Täiustatud autentimine ja autoriseerimine Microsoft Entra ID integratsiooniga
    - Tokeni turvalisus ja pass-through kontrollid põhjaliku valideerimisega
    - Sessiooni turvalisuse kontrollid kaaperdamise ennetamiseks
    - AI spetsiifilised turvakontrollid prompt-injectioni ja tööriista mürgituse ennetamiseks
    - Confused Deputy rünnakute ennetamine OAuth-proxy turvalisusega
    - Tööriistade täitmise turvalisus sandboxi ja isoleerimisega
    - Tarneahela turvakontrollid sõltuvuste kontrolliga
    - Jälgimise ja avastamise kontrollid SIEM integratsiooniga
    - Intsidendi reageerimine ja taastumine automatiseeritud võimalustega
  - **Rakenduse näited**: lisatud detailseid YAML konfiguratsiooniblokke ja koodinäiteid
  - **Microsofti lahenduste integreerimine**: ulatuslik ülevaade Azure turvateenustest, GitHub Advanced Securityst ja ettevõtte identiteedihaldusest

#### Täiustatud teemade turvalisus (05-AdvancedTopics/mcp-security/) – tootmiskõlblik rakendus
- **README.md**: täielik ümberkirjutus ettevõtte turvalisuse rakenduseks
  - **Praegune spetsifikatsiooni kooskõlas**: uuendatud MCP spetsifikatsioonile 2025-06-18 koos kohustuslike turvanõuetega
  - **Täiustatud autentimine**: Microsoft Entra ID integratsioon koos põhjalike .NET ja Java Spring Security näidetega
  - **AI turva integratsioon**: Microsoft Prompt Shieldsi ja Azure Content Safety rakendamine detailsete Python näidetega
  - **Täiustatud ohu leevendamine**: põhjalikud rakendamise näited
    - Confused Deputy rünnaku ennetamine PKCE ja kasutaja nõusoleku valideerimisega
    - Tokeni läbimise ennetamine audientsi valideerimise ja turvalise tokeni haldusega
    - Sessiooni kaaperdamise ennetamine krüptograafilise sidumise ja käitumisanalüüsiga
  - **Ettevõtte turvaintegreerimine**: Azure Application Insights jälgimine, ohu tuvastamise töövood ja tarneahela turvalisus
  - **Rakenduse kontrollnimekiri**: selge jaotus kohustuslike ja soovitatavate turvakontrollide vahel koos Microsofti turvaökosüsteemi eelistustega

### Dokumentatsiooni kvaliteet ja standardite kooskõlastamine
- **Spetsifikatsiooni viited**: uuendatud kõik viited praegusele MCP spetsifikatsioonile 2025-06-18
- **Microsofti turvaökosüsteem**: täiustatud integreerimisjuhendid kogu turvadokumentatsioonis
- **Praktiline rakendamine**: lisatud detailseid koodinäiteid .NET, Java ja Python keeles koos ettevõtte mustritega
- **Ressursside korraldus**: ametlike dokumentide, turvastandardite ja rakendusjuhiste põhjalik kategooriajaotus
- **Visuaalsed indikaatorid**: kohustuslike nõuete ja soovitatavate tavade selge märgistamine


#### Põhikontseptsioonid (01-CoreConcepts/) – täielik moderniseerimine
- **Protokolli versiooni uuendus**: värskendatud viide MCP spetsifikatsioonile 2025-06-18 kuupõhise versiooniga (AAAA-KK-PP formaat)
- **Arhitektuuri täpsustus**: täiustatud Hosts, Clients ja Servers kirjeldused, peegeldades MCP praeguseid arhitektuurimustreid
  - Hosts defineeritud selgelt kui AI rakendused, mis koordineerivad mitut MCP kliendiühendust
  - Clients kirjelduse, kui protokolli ühendajad, kes hoiavad ühe-ühe vastu serveri suhteid
  - Servers täiustatud kohaliku ja kaugpaigalduse stsenaariumitega
- **Primitiivide ümberkorraldus**: täielik ülevaatus serveri ja kliendi primitiividest
  - Serveri primitiivid: ressursid (andmeallikad), juhised (mallid), tööriistad (käidavad funktsioonid) koos põhjalike selgituste ja näidetega
  - Kliendi primitiivid: proovivõtt (LLM täitmised), väljatoomine (kasutaja sisend), logimine (silumine/jälgimine)
  - Värskendatud praeguste avastamise (`*/list`), hankimise (`*/get`) ja täitmise (`*/call`) meetodimustritega
- **Protokolli arhitektuur**: esitatud kahekihiline arhitektuuri mudel
  - Andmekiht: JSON-RPC 2.0 alus koos elutsükli halduse ja primitiividega
  - Transpordikiht: STDIO (kohalik) ja voogestatav HTTP koos SSE-ga (kaugtranspordimehhanismid)
- **Turvasüsteem**: ulatuslikud turvapõhimõtted koos selge kasutaja nõusoleku, andmekaitse, tööriista täitmise ohutuse ja transpordikihi turvalisusega
- **Suhtlemismustrid**: protokolli sõnumite uuendamine, kajastades initsialiseerimist, avastamist, täitmist ja teavitamise vooge
- **Koodinäited**: värskendatud mitmekeelsetes näidetes (.NET, Java, Python, JavaScript) praeguseid MCP SDK mustreid

#### Turvalisus (02-Security/) – põhjalik turvauuendus  
- **Standardite kooskõlastamine**: täpne vastavus MCP spetsifikatsiooni 2025-06-18 turvanõuetele
- **Autentimise areng**: dokumenteeritud areng kohandatud OAuth serveritest välistuveni (Microsoft Entra ID)
- **AI-spetsiifiline ohuanalüüs**: täiustatud kaasaegsete AI rünnakute vektorite käsitlus
  - üksikasjalikud prompt injection rünnakute stsenaariumid reaalse elu näidetega
  - tööriistade mürgitamise mehhanismid ja "rug pull" rünnakud
  - konteksti akna mürgitamine ja mudeli segadusseajamise rünnakud
- **Microsofti AI turvalahendused**: põhjalik ülevaade Microsofti turvaökosüsteemist
  - AI Prompt Shieldsid koos täiustatud avastamise, rõhutamise ja piiritlemistehnikatega
  - Azure Content Safety integratsioonimustrid
  - GitHub Advanced Security tarneahela kaitseks
- **Täiustatud ohu leevendamine**: üksikasjalikud turvakontrollid
  - Sessiooni kaaperdamine MCP-spetsiifiliste stsenaariumitega ja krüptograafiliste sessioonitunnuste nõuetega
  - Confused Deputy probleemid MCP proxy stsenaariumites koos selgete nõusoleku nõuetega
  - Tokeni läbipääsu haavatavused kohustusliku valideerimisega
- **Tarneahela turvalisus**: laiendatud AI tarneahela katvus, sh alusmudelid, embedded teenused, konteksti pakkujad ja kolmandate osapoolte API-d
- **Aluse turvalisus**: täiustatud ettevõtte turvamustrite integratsioon nullusaldus arhitektuuri ja Microsofti turvaökosüsteemiga
- **Ressursside korraldus**: põhjalik kategooriate jaotus ametlike dokumentide, standardite, uurimiste, Microsofti lahenduste ja rakendusjuhiste kaupa

### Dokumentatsiooni kvaliteedi parendused
- **Struktureeritud õpieesmärgid**: täiustatud õpieesmärgid spetsiifiliste, teostatavate tulemuste jaoks 
- **Ristviited**: lisatud lingid seotud turva- ja põhikontseptsiooni teemade vahel
- **Praegune info**: uuendatud kõik kuupäevaviited ja spetsifikatsiooni lingid vastavalt praegustele standarditele
- **Rakendamisjuhendid**: lisatud spetsiifilisi, teostatavaid rakendamisjuhiseid mõlemas sektsioonis

## 16. juuli 2025

### README ja navigeerimise täiustused
- Tõeliselt ümber kujundatud õppekava navigeerimine README.md failis
- Asendatud `<details>` sildid ligipääsetavama tabelipõhise vorminguga
- Loodud alternatiivsed paigutuse valikud uues “alternative_layouts” kaustas
- Lisatud kaartide, vahekaartide ja akordionstiili navigeerimise näited
- Uuendatud arhiivi struktuuriosa, et hõlmata kõiki uusimaid faile
- Täiustatud sektsioon “Kuidas seda õppekava kasutada” selgete soovitustega
- Uuendatud MCP spetsifikatsiooni lingid, et osutada õigetele URL-idele
- Lisatud Konteksti inseneriteaduse sektsioon (5.14) õppekava struktuuri

### Õppejuhendi uuendused
- Täielikult üle vaadatud õppejuhend, et olla kooskõlas praeguse arhiivi struktuuriga
- Lisatud uued sektsioonid MCP klientide ja tööriistade ning populaarsete MCP serverite kohta
- Uuendatud visuaalne õppekava kaart, et täpselt kajastada kõiki teemasid
- Täiustatud Advanced Topics kirjeldused, hõlmates kõiki spetsialiseeritud valdkondi
- Uuendatud juhtumiuuringute osa, et kajastada tegelikke näiteid
- Lisatud see põhjalik muudatuste logi

### Kogukonna panused (06-CommunityContributions/)
- Lisatud põhjalik info MCP serverite kohta pildigeneratsiooni jaoks
- Lisatud ulatuslik sektsioon Claude kasutamise kohta VSCode'is
- Lisatud Cline terminali kliendi seadistuse ja kasutusjuhised
- Uuendatud MCP kliendi sektsioon, et hõlmata kõiki populaarseid kliendi valikuid
- Täiustatud panuse näited täpsemate koodinäidetega

### Täiustatud teemad (05-AdvancedTopics/)
- Kõik spetsialiseeritud teema kaustad organiseeritud järjepideva nimetamisega
- Lisatud konteksti inseneriteaduse materjalid ja näited
- Lisatud Foundry agendi integratsiooni dokumentatsioon
- Täiustatud Entra ID turvalisuse integratsiooni dokumentatsioon

## 11. juuni 2025

### Esialgne loomine
- Avaldatud esimene versioon MCP for Beginners õppekavast

- Loodud põhiline struktuur kõigile 10 põhiosale
- Rakendatud Visuaalne õppekava kaart navigeerimiseks
- Lisatud esialgsed näidistooted mitmes programmeerimiskeeles

### Alustamine (03-GettingStarted/)
- Loodud esimesed serveri rakenduse näited
- Lisatud juhised kliendi arendamiseks
- Kaasatud LLM kliendi integratsiooni juhised
- Lisatud VS Code integratsiooni dokumentatsioon
- Rakendatud Server-Sent Events (SSE) serveri näited

### Põhikontseptsioonid (01-CoreConcepts/)
- Lisatud põhjalik selgitus kliendi-serveri arhitektuurist
- Loodud dokumentatsioon peamiste protokolli komponentide kohta
- Dokumenteeritud sõnumivahetusmustrid MCP-s

## 23. mai 2025

### Repositooriumi struktuur
- Algatatud repositoorium põhilise kaustastruktuuriga
- Loodud README failid iga suurema osa jaoks
- Seadistatud tõlkeinfrastruktuur
- Lisatud pildifailid ja diagrammid

### Dokumentatsioon
- Loodud esialgne README.md õppekava ülevaatega
- Lisatud CODE_OF_CONDUCT.md ja SECURITY.md
- Seadistatud SUPPORT.md abi saamise juhistega
- Loodud eelluure juhendi struktuur

## 15. aprill 2025

### Planeerimine ja raamistik
- Esialgne planeerimine MCP algajate õppekavale
- Määratletud õpieesmärgid ja sihtgrupp
- Koostatud õppekava 10 osa struktuur
- Arendatud kontseptuaalne raamistik näidete ja juhtumianalüüside jaoks
- Loodud esialgsed prototüüpnäited oluliste kontseptsioonide kohta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
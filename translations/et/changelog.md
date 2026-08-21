# Muudatuste logi: MCP algajate õppekava

See dokument toimib kõigi Model Context Protocol (MCP) algajate õppekavas tehtud oluliste muudatuste kirjelduseks. Muudatused on dokumenteeritud pööratud kronoloogilises järjekorras (kõige uuemad muudatused eespool).

## 29. juuli 2026

### Uus moodul 08 kaaslane: Usaldusväärsuse kõrvalprogrammid ja turvalised taaskatsed

Lisatud tarnijast sõltumatu kaasatundmuse tund MCP tööriistadele, mis loovad reaalmaailma
efekte, vastavuses lõpliku `2026-07-28` spetsifikatsiooniga.

- **Uus**: [usaldusväärsuse kõrvalprogrammi kaasõppetund][reliability-sidecar]
  kasutab ühte tugipileti lugu, kahte Mermaid diagrammi ja taaskatse otsustamise
  voogu, et selgitada stabiilse toimimise võtmeid, aatomilist duplikaatide vastuvõttu,
  kokkulepet, tõendeid ja Tasks laienduse piire.
- **Uus**: Standardraamatukogu Python ja SQLite veasisestamise harjutus
  kasutab eraldi toimingute ja piletite andmekogusid, et demonstreerida vastuse kaotust
  pärast välise efekti kinnitamist. Kuus deterministlikku testi hõlmavad naiivset
  dubleerimist, kaitstud taaskäivituse taastumist, koormuse konflikte, vahemällu salvestatud tulemusi,
  aktiivseid nõudeid ja samaaegset dubleerimise vastuvõttu.
- **Uuendatud**: Moodul 08 ühendab nüüd kaasõppetunni lingi, määratleb
  lõpliku `2026-07-28` olekutaotluse mudeli, eristab OpenTelemetry jälgitavust
  MCP logimisfunktsioonist ja piirab oma
  üldist taaskatse näidet ainult lugemisoperatsioonidele.
- **Valikuline**: Õppetund seob oma kaasaskantavad kontseptsioonid ühe märgistatud kogukonna
  teostusega ilma, et majutatud teenus või võrguühendus oleks osa
  harjutusest.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. juuli 2026

### Uus õppetund: MCP spetsifikatsiooni vabastamise kandidaat 2026-07-28

Lisatud ülevaade eelseisvast `2026-07-28` MCP spetsifikatsiooni vabastamise kandidaadist (teatatud 21. mail 2026; lõplik vabastamine kavandatud 28. juuliks 2026), kokkuvõtlikult [ametlikust teatise blogipostitusest](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Õppekava alus jääb alles **MCP spetsifikatsioon 2025-11-25** kuni uue versiooni väljalaskmiseni, seega esitatakse see kui tulevikku vaatavat juhist, mitte olemasolevate õppetundide ümberkirjutust.

- **Uus**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — terve õppetund, mis käsitleb olekutut protokolli tuuma (algusest `initialize` käepigistuse ja `Mcp-Session-Id` eemaldamine), uusi `Mcp-Method`/`Mcp-Name` marsruutimispäiseid, `ttlMs`/`cacheScope` vahemällu salvestamise metaandmeid, W3C jälje konteksti `_meta` sees, ametlikku laienduste raamistikku (MCP rakendused ja uus Tasks laiendus), kuut autoriseerimise tugevdamise SEP-i, Roots/Sampling/Logging kasutuse lõpetamist ja üleminekut täielikule JSON Schema 2020-12 tööriistade skeemidele.
- **Uuendatud** tulevikku vaatavate viidetega, mis lingivad uuele õppetundile:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolli versiooni märkus, Sampling/Roots/Logging/Tasks osad ja "Mis järgmiseks"
  - [02-Security/README.md](./02-Security/README.md): autoriseerimise tugevdamise märkus
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): olekuta transpordi märkus
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling lõpetamise märkus
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging lõpetamise ja Tasks laienduse märkus
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): olekuta/session-marsruutimise märkus
  - [README.md](./README.md): "Tulevikku vaatamine" märkus spetsifikatsiooni sektsioonis ja uus `1.1` kirje õppekava moodulite tabelis
  - [study_guide.md](./study_guide.md): tulevikku vaatav punkt Core Concepts ülevaates ja dateeritud lisamärkus
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): märkus `mcp-session-id` transpordimapi kohta enne olekutaotluse mudelit
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): mooduli ülevaate märkus Root Contexts/Sampling lõpetamiste ja Tasks laienduse kohta
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autoriseerimise tugevdamise märkus

## 24. juuni 2026

### Uus õppetund: MCP kasutamine Copiloti rakenduses

- [Tööriistade sektsioon](./12-tooling/README.md) Lisatud tööriistade sektsioon.
- [MCP Copiloti rakenduses](./12-tooling/01-copilot-app/README.md)

## 16. juuni 2026

### MCP spetsifikatsiooni joondamine ja näidiste valideerimine

Valideeriti õppekava vastavust kehtivale **MCP spetsifikatsioonile 2025-11-25** ja uusimatele ametlikele SDK-dele, seejärel parandati ülejäänud aegunud spetsifikatsiooni viited ning kinnitati, et põhinäited ehituvad ja jooksevad endiselt.

#### Spetsifikatsiooni versiooni parandused (2025-06-18 / 2025-03-26 → 2025-11-25)

Uuendatud ingliskeelne sisu, kus endiselt väideti, et vanem spetsifikatsiooni revisjon oli *praegune/viimane* standard, ning suunatud lingid kanonilistele `modelcontextprotocol.io` spetsifikatsiooni radadele:
- **05-AdvancedTopics/mcp-security/README.md**: Uuendatud "Praegune standard" bännerit, sissejuhatust, tuumaturbefilosoofia pealkirja, kohustuslike nõuete pealkirja, Microsoft Entra ID jaotist, Viiteid ja Ressursse linke ning lõplikku turvahoiatust (8 viidet) 2025-11-25 kuupäevaks
- **05-AdvancedTopics/mcp-transport/README.md**: Uuendatud Lisaressursside spetsifikatsiooni linki ja "Praegune standard" bännerit 2025-11-25 kuupäevani
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Asendatud aegunud `2025-03-26` turbe-ja-usalduslink praeguse 2025-11-25 turbe parimate tavade lehega
- **03-GettingStarted/14-sampling/README.md**: Uuendatud ametlikust proovi võtmise dokumentatsioonist link 2025-11-25 kuupäevaga

- **03-GettingStarted/05-stdio-server/README.md**: Uuendatud olevikuvormis „praeguse MCP spetsifikatsiooni“ viide ja täiendavate ressursside spetsifikatsiooni link kuupäevale 2025-11-25 (ajaloolised SSE-deprekatsiooni märkused jäid täpsuse huvides muutmata)

#### Näidised kehtivuse kontroll praeguste SDK-de vastu

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` lahendas `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` läbis tüübiveadeta — olemasolevad `McpServer`/`StdioServerTransport` API-d jäävad kehtima
- **Python (03-GettingStarted/01-first-server/solution/python)**: Kontrollitud isoleeritud `.venv` keskkonnas `mcp[cli]` (1.27.2) abil; `py_compile` läbis ja `FastMCP.list_tools()` tagastas korrektselt `add` ja `subtract` tööriistad
- Kinnitatud, et kõigi näidiste `@modelcontextprotocol/sdk` versioonivahemikud (`>=1.26.0` / `^1.26.0` / `^1.27.0`) lahenevad korrektselt praegusele `1.29.0` versioonile ilma katkestavate API muutusteta

#### Sõltuvuste versioonipinnide joondamine (versioonilünkade lõpetamine)

Värskendatud aegunud SDK pinnid nii, et iga näidis jälgib praegust MCP väljaannet, järgides kogu mõisa konventsiooni:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Uuendatud `@modelcontextprotocol/sdk` versioonilt `^1.8.0` → `>=1.26.0` ning aegunud pakendi kirjeldus "uuendatud MCP 2025-06-18 jaoks" uuendatud "joondunud MCP spetsifikatsiooniga 2025-11-25"
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ja **lab4/code/github_mcp_server/pyproject.toml**: Täpsete kinnituste `mcp==1.23.0` → `mcp>=1.26.0` tõstmine; mõlema `uv.lock` faili uuesti genereerimine (`uv lock`), nii, et lockfailid lahenduksid praegusele `mcp 1.27.2` versioonile ning püsiksid manuaalidega sünkroonis

#### Õppekava lünkade analüüs — uusima spetsifikatsiooni funktsioonide katvus

Kontrollitud, et õppekava hõlmab juba kõiki MCP 2025-11-25 tutvustatud / laiendatud primitiive, seega pole sisulisi puudujääke:
- **Võtmine (Sampling)**: Õppetund 03-GettingStarted/14-sampling pluss 05-AdvancedTopics/mcp-sampling
- **Elicitation (sh URL-režiim)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Juurkontekstid (Roots)**: Dokumenteeritud 00-Introduction, 01-CoreConcepts ja 05-AdvancedTopics/mcp-root-contexts
- **Ülesanded (eksperimentaalne, pikaajalised toimingud)**: Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features
- **Tööriista annotatsioonid** (`readOnlyHint` / `destructiveHint`): Dokumenteeritud 01-CoreConcepts ja 05-AdvancedTopics/mcp-protocol-features

### Turvalisuse tugevdamine & sõltuvuste haavatavuste parandamine

Läbitud täielik turvapassinõue iga sõltuvuse manifesti ja näidiste lähtekoodi kohta, seejärel parandatud kõik teatatud npm hoiatused ja üks kooditasandi probleem. Pärast parandusi näitab `npm audit` raporteeritud seirekaustades **0 haavatavust**.

#### npm sõltuvuste haavatavused (kaudsed) — Parandatud

Kontrolliti kõiki 15 kohusetäitnud `package-lock.json` faili. Haavatavused piirdusid kaudsete sõltuvustega, mida tõmbas MCP Inspector dev tööriist, OpenAI klient ja MCP SDK; kõik on nüüd lahendatud ilma näidiseid katkestamata:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ja **lab3/code/weather_mcp/inspector**: Uuendatud `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), mis eemaldab kaasatud `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ja `ws` hoiatused. Lisatud npm `overrides` kirje, mis sunnib parandatud `shell-quote@1.8.4` kasutamist, et elimineerida kogu kriitiline hoiatus, mida edastas `concurrently`; mõlema lockfaili uuesti genereerimine (nüüd 0 haavatavust)
- **03-GettingStarted/samples/typescript**: `npm audit fix` uuendas kaudse `qs` (kõrge) parandatud versioonile
- **03-GettingStarted/samples/javascript**: `npm audit fix` uuendas kaudse `hono` (keskmine) parandatud versioonile
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` uuendas kaudse `form-data` (kõrge) parandatud versioonile
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genereeritud puuduva `package-lock.json`, et projekt oleks reprodutseeritav ja auditeeritav (0 haavatavust)

#### Kooditasandi turvaparandus (OWASP A03: süstimine)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Eemaldatud `shell=True` `open_in_vscode` tööriistast. Varasem `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` lubas käsukesta metamärgid kaustatee sees `cmd.exe` poolt tõlgendamiseks (käsusüstimise vektor). Nüüd käivitatakse lahendatud `Code.exe` otse kausta argumendiga — ilma kestas — mis on funktsionaalselt ekvivalentne ning ohutu

#### Python sõltuvuste audit

- Auditeeritud iga Python'i nõuete komplekt `pip-audit` abil. `05-AdvancedTopics` ja `03-GettingStarted/samples/python` teatavad **mitte ühestki tuntud haavatavusest** (nende `mcp` / `httpx` / `pydantic` / `python-dotenv` vahemikud lahenevad praegustele parandatud versioonidele)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` tuvastas kaudse sõltuvuse **`werkzeug` 3.1.1** kohta kolm `safe_join` Windowsi seadmenime DoS hoiatusi — `CVE-2025-66221`, `CVE-2026-21860` ja `CVE-2026-27199` (kõik parandatud versioonis 3.1.6). Lisatud otsene turvalisuse pin `werkzeug>=3.1.6`, et parandatud versioon lahenduks korrektselt; kinnitatud, et piirang laheneb puhtalt `chainlit` / `mcp` / `semantic-kernel` virna kontekstis

### Tootenime ümberbrändimine

Uuendatud kogu õppekava sisu, et kajastada Microsofti tootenime ümberbrändimist:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Uuendatud Discordi kogukonna link

- **AGENTS.md**: Uuendatud Discordi serveri viide
- **README.md**: Uuendatud tehnoloogilise ökosüsteemi viited
- **study_guide.md**: Uuendatud juhtumiuuringute viited
- **05-AdvancedTopics/README.md**: Uuendatud Mooduli 5.13 pealkiri ja kirjeldus
- **05-AdvancedTopics/mcp-integration/README.md**: Uuendatud sektsiooni päis ja kirjeldus
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Täielik mooduli pealkirja ja sisu uuendus
- **05-AdvancedTopics/mcp-security-entra/README.md**: Uuendatud ristviitamise link
- **07-LessonsfromEarlyAdoption/README.md**: Uuendatud juhtumiuuringute viited
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Uuendatud jaotise 9 päis, märgised ja võimalused
- **08-BestPractices/README.md**: Uuendatud Discordi kogukonna link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Uuendatud Discordi kanali viide
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Uuendatud mudeli juurutamise viide
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Uuendatud AI teenuste tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Uuendatud ressursside viited

#### AI tööriistakomplekt / AITK → Microsoft Foundry tööriistakomplekti laiendus VS Code’ile
- **README.md**: Uuendatud põhikursuse viited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Uuendatud mooduli pealkiri, ülevaade ja kõik mooduli päised
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Uuendatud pealkiri, õpieesmärgid, seadistamise juhised ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Uuendatud pealkiri, õpieesmärgid, MCP hostide tabel ja ristviited
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Uuendatud pealkiri, märgised, eeltingimused ja ressursid
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Uuendatud Agent Builderi viited ja tagasiside link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Uuendatud eeltingimused ja laienduse viited

---

## 11. aprill 2026

### Uus õppetund, dokumentatsiooni parandused ja sõltuvuste uuendused

#### Lisatud uus kursuse sisu

**Moodul 05 - Täiustatud teemad**
- **Õppetund 5.17: Vihkiv mitmeagendiline mõtlemine MCP abil** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Uus põhjalik juhend, mis käsitleb mitme-agendi süsteemide vastuolulise vaidluse mustrit
  - Mermaid arhitektuuri diagramm: kaks agenti → ühine MCP server → vaidluse transkriptsioon → kohtunik → otsus
  - Ühiskasutatav MCP tööriistaserver (`web_search` + `run_python`) realiseeritud Pythonis ja TypeScriptis
  - Vastandlikud süsteemi käsklused (FOR / AGAINST / Judge) koos selgete tööriistakasutuse nõuetega
  - Vaidluse korraldaja Pythonis, TypeScriptis ja C# keeles, haldab voorusid ja argumentide suunamist
  - MCP `ClientSession` ühendamine korraldajale päris tööriistakõnede jaoks
  - Kasutusjuhtude tabel (hallutsinatsiooni tuvastamine, ohumudelite loomine, API disaini ülevaade, faktide kontroll, tehnoloogia valik)
  - Turvaküsimused: liivakastis täitmine, tööriistakõnede valideerimine, kvoodi piiramine, auditeerimine
  - Struktureeritud harjutus kolme praktilise stsenaariumiga (koodi ülevaade, arhitektuuri otsus, sisumoderatsioon)

#### Dokumentatsiooni parandused

**Moodul 03 - Algus**
- **05-stdio-server/README.md**: Parandatud mittetäielik TypeScript stdio serveri näide — lisatud puuduva transpordi loomisekutse (`new StdioServerTransport()`) ja `server.connect(transport)` kõne vastavuseks Python ja .NET näidistega samas jaotises
- **14-sampling/README.md**: Parandatud kirjavea — parandatud "Sampling is an davanced features" → "Sampling is an advanced feature"

#### Kursuse uuendused

**Põhi README.md**
- Lisatud 5.17 (Vihkiv mitme-agendi mõtlemine MCP abil) kande kursuse tabelisse koos otselinkiga uuele õppetunnile

**05-AdvancedTopics/README.md**
- Lisatud õppetund 5.17 rida õppetundide tabelisse

**study_guide.md**
- Lisatud Vihkiva mitme-agendi mõtlemise teema mõttekaardile ja täiendatud kirjeldus Täiustatud teemades

#### Koodi ja turvalisuse parandused

**Moodul 05 - Vihkivad agendid (`mcp-adversarial-agents`)**
- **Turvaparandus — käsu süstimine**: Asendatud `execSync` kestainterpolatsioon `execFile` + `promisify` kombinatsiooniga TypeScripti `run_python` tööriistas, likvideerides käsu süstimise pinna (LLM-i juhitud kood edastatakse nüüd kirjeldavalt argv elemendina ilma kestataustata)
- **MCP tööriistasilmuse ühendamine**: Uuendatud Python debate-orgide kasutama `AsyncAnthropic` klienti (asendab blokeeriva sünkroonse `Anthropic`), edastab live `ClientSession` otseselt igale agendi voorule, hangib tööriistade definitsioonid `session.list_tools()` kaudu igas voorus ja edastab `tool_use` plokid `session.call_tool()` abil lõputeksti vastuse saamiseni

#### Sõltuvuste uuendused

- Tõstetud `hono` versiooniks 4.12.12 mitmes paketis (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Tõstetud `@hono/node-server` versioon 1.19.11 → 1.19.13 TypeScripti pakettides
- Tõstetud `cryptography` versioon 46.0.5 → 46.0.7 Python pakettides (10-StreamliningAIWorkflows laborid 3 ja 4)
- Tõstetud `lodash` versioon 4.17.23 → 4.18.1 10-StreamliningAIWorkflows inspector

#### Tõlked

- Sünkroniseeritud tõlked 48+ keeles viimaste lähte muudatustega (i18n uuendus)

---

## 5. veebruar 2026

### Kogu hoidla valideerimine ja navigeerimise parandused

#### Lisatud uus kursuse sisu

**Moodul 03 - Algus**
- **12-mcp-hosts/README.md**: Uus põhjalik juhend MCP hostide seadistamiseks
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfiguratsiooni näited
  - JSON konfiguratsiooni mallid kõigi peamiste hostide jaoks
  - Transporditüüpide võrdlustabel (stdio, SSE/HTTP, WebSocket)
  - Levinumate ühendusprobleemide tõrkeotsing
  - Hostide konfiguratsiooni turvalisuse parimad tavad

- **13-mcp-inspector/README.md**: Uus silumise juhend MCP Inspectorile
  - Paigaldusmeetodid (npx, globaalne npm, lähtekoodist)
  - Ühendamine serveritega stdio ja HTTP/SSE kaudu
  - Testimise tööriistad, ressursid ja käskluste töövoogude juhised
  - VS Code integratsioon MCP Inspectoriga
  - Levinumad silumise stsenaariumid koos lahendustega

**Moodul 04 - Praktiline rakendamine**
- **pagination/README.md**: Uus leheküljestamise rakendamisjuhend
  - Kursori põhised leheküljestamise mustrid Pythonis, TypeScriptis, Javas
  - Kliendipoolse leheküljestamise haldus
  - Kursori disaini strateegiad (opaakne vs struktureeritud)
  - Jõudluse optimeerimise soovitused

**Moodul 05 - Täiustatud teemad**
- **mcp-protocol-features/README.md**: Uus protokolli funktsioonide põhjalik ülevaade
  - Edusammude teatamise rakendus
  - Päringu tühistamise mustrid
  - Ressursi mallid URI mustritega
  - Serveri elutsükli haldus
  - Logitaseme kontroll
  - Veahaldusmeetodid JSON-RPC koodidega

#### Navigeerimise parandused (24+ faili uuendatud)

**Peamiste moodulite README-d**
 Nüüd lingib nii esimesele õppetunnile KUI ka järgnevale moodulile

**02-Security alamfailid**
- Kõigil 5 täiendaval turvakäsiraamatul on nüüd "Mis järgmiseks" navigeerimine:

**09-CaseStudy failid**
- Kõigil juhtumiuuringute failidel on nüüd järjestikune navigeerimine:

**10-StreamliningAI laboris**
Lisatud “Mis järgmiseks” jaotis Moodulite 10 ülevaatesse ja Mooduli 11-le

#### Koodi ja sisu parandused

**SDK ja sõltuvuste uuendused**
Parandatud tühi openai versioon `^4.95.0`-ks
SDK uuendatud versioonile `>=1.26.0` varasemalt `^1.8.0`
MCP versiooni lukustused uuendatud `>=1.26.0`

**Koodi parandused**
Parandatud vale mudel `gpt-4o-mini` → `gpt-4.1-mini`

**Sisupärandused**
Parandatud katkine link `READMEmd` → `README.md`, parandas kursuse päise `Moodul 1-3` → `Moodul 0-3`, parandatud tõstutundlik tee
Eemaldatud rikutud duplikaat juhtumiuuringu 5 sisu

**Algajate juhendamise täiustused**
Lisatud korralik sissejuhatus, õpieesmärgid ja eeltingimused algajatele

#### Kursuse uuendused

**Põhi README.md**
- Lisatud kanded 3.12 (MCP hostid), 3.13 (MCP Inspector), 4.1 (Leheküljestamine), 5.16 (Protokolli funktsioonid) kursuse tabelisse

**Mooduli README-d**
Lisatud õppetunnid 12 ja 13 õppetundide nimekirja
Lisatud Praktiliste juhendite jaotis koos leheküljestamise lingiga
Lisatud õppetunnid 5.15 (Kohandatud transport) ja 5.16 (Protokolli funktsioonid)

**study_guide.md**
- Uuendatud mõttekaart kõigi uute teemadega: MCP hostide seadistus, MCP Inspector, leheküljestamise strateegiad, protokolli funktsioonide põhjalik ülevaade

## 28. jaanuar 2026

### MCP spetsifikatsiooni 2025-11-25 vastavuse ülevaatus

#### Tuumikkontseptsioonide täiustamine (01-CoreConcepts/)
- **Uus kliendi primitiiv - Roots**: Lisatud põhjalik dokumentatsioon Roots kliendi primitiivi kohta, mis võimaldab serveritel mõista failisüsteemi piire ja juurdepääsuõigusi
- **Tööriista annotatsioonid**: Lisatud dokumentatsioon tööriista käitumise annotatsioonidest (`readOnlyHint`, `destructiveHint`) paremate tööriistate täitmise otsuste jaoks
- **Tööriistakõned valikus**: Uuendatud Sampling dokumentatsiooni, lisades `tools` ja `toolChoice` parameetrid mudelipõhiste tööriistakõnede tegemiseks proovivõtu päringute ajal
- **URL režiimi paljastamine**: Lisatud dokumentatsioon URL-põhise paljastamise kohta serveripoolsete väliste veebisuhtluste algatamiseks
- **Ülesanded (eksperimentaalne)**: Lisatud uus jaotis ülesannete kohta, mis dokumenteerib katsetuslikku funktsiooni vastupidavate täitmiskihistuste ja tulemust tagastamise edasilükkamiseks
- **Ikonide tugi**: Märgitud, et tööriistad, ressursid, ressursimallid ja kutseviidad võivad nüüd sisaldada ikoone lisametabina

#### Dokumentatsiooni uuendused
- **README.md**: Lisatud MCP spetsifikatsiooni 2025-11-25 versiooni viide ja kuupõhine versioonihaldus selgitus
- **study_guide.md**: Uuendatud kursuse kaart, lisades Ülesanded ja Tööriista annotatsioonid Tuumikontseptsioonide sektsiooni; uuendatud dokumendi kuupäev

#### Spetsifikatsiooni vastavuse kinnitamine
- **Protokolli versioon**: Kontrollitud, et kogu dokumentatsioon viitab aktuaalsele MCP spetsifikatsioonile 2025-11-25
- **Arhitektuuri kokkusobivus**: Kinnitatud kahekihiline arhitektuur (andmekiht + transpordikiht) dokumentatsiooni täpsus
- **Primitiivide dokumenteerimine**: Kontollitud serveripoolsete primitiivide (ressursid, kutsed, tööriistad) ja kliendipoolsete primitiivide (Sampling, Elicitation, Logging, Roots) dokumentatsiooni täpsus
- **Transpordimehhanismid**: Kinnitatud STDIO ja Streamable HTTP transpordi dokumentatsiooni täpsus
- **Turvajuhtnöörid**: Kinnitatud vastavus hetke MCP turvalisuse parimate tavade dokumentatsioonile

#### Olulised MCP 2025-11-25 funktsioonid dokumenteeritud
- **OpenID Connect avastamine**: Autentimisserveri avastamine OIDC kaudu
- **OAuth kliendi ID metaandmete dokumendid**: Soovitatud kliendi registreerimise mehhanism
- **JSON skeem 2020-12**: MCP skeemide põhikeel
- **SDK astmeliistude süsteem**: Formaliseeritud nõuded SDK funktsioonide toetusele ja hooldusele
- **Haldusstruktuur**: Formaliseeritud töörühmad ja huvirühmad MCP halduses

### Turvadokumentatsiooni suur uuendus (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integreerimine
- **Uus praktiline koolitusressurss**: Lisatud põhjalik integratsioon [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) kõigis turbudokumentides
- **Ekspeditsiooni marsruudid**: Dokumenteeritud kogu laagrilt laagrile liikumine Aluslaagrist Haripunkti
- **OWASP vastavus**: Kõik turvajuhtnöörid nüüd kooskõlas OWASP MCP Azure turvajuhendite riskidega

#### OWASP MCP Top 10 integreerimine
- **Uus sektsioon**: Lisatud OWASP MCP Top 10 turvariskide tabel Azure leevendustega peamise Security README-sse
- **Riskipõhine dokumentatsioon**: Uuendatud mcp-security-controls-2025.md koos OWASP MCP riskiviidetega igas turvadomeenis
- **Võrdlusarhitektuur**: Lingitud OWASP MCP Azure turvajuhendi võrdlusarhitektuuri ja rakendusmustritega

#### Uuendatud turbefailid
- **README.md**: Lisatud Sherpa koolituse ülevaade, ekspeditsiooni marsruuditabel, OWASP MCP Top 10 riskide kokkuvõte ja praktilise koolituse jaotis
- **mcp-security-controls-2025.md**: Uuendatud päis veebruar 2026, lisatud OWASP riskiviited (MCP01-MCP08), parandatud spetsifikatsiooni versiooni vastuolu
- **mcp-security-best-practices-2025.md**: Lisatud Sherpa ja OWASP ressursside jaotis, uuendatud kuupäev
- **mcp-best-practices.md**: Lisatud praktilise koolituse jaotis Sherpa ja OWASP linkidega
- **azure-content-safety-implementation.md**: Lisatud OWASP MCP06 viide, Sherpa laager 3 kooskõlastus ja täiendavate ressursside jaotis

#### Lisatud uued ressursside lingid
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure turvajuht](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Üksikisiku OWASP MCP riskilehed (MCP01-MCP10)

### Õppekavaülene MCP Spetsifikatsiooni 2025-11-25 joondamine

#### Moodul 03 - Alustamine
- **SDK dokumentatsioon**: Lisatud Go SDK ametlikku SDK nimekirja; uuendatud kõik SDK viited MCP Spetsifikatsioonile 2025-11-25 vastavaks
- **Ülekande täpsustus**: Uuendatud STDIO ja HTTP voogedastuse transpordi kirjeldusega, kus on eksplicitse spetsifikatsiooni viited

#### Moodul 04 - Praktiline rakendamine
- **SDK uuendused**: Lisatud Go SDK; uuendatud SDK nimekiri spetsifikatsiooni versiooni viitega
- **Autoriseerimise spetsifikatsioon**: Uuendatud MCP autoriseerimise spetsifikatsiooni link uuele 2025-11-25 versioonile

#### Moodul 05 - Täiustatud teemad
- **Uued funktsioonid**: Lisatud märkus MCP Spetsifikatsiooni 2025-11-25 uute funktsioonide kohta (ülesanded, tööriistade annotatsioonid, URL režii tuvastamine, juured)
- **Turberessursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid täiendavatesse viidetesse

#### Moodul 06 - Ühiskonna panused
- **SDK nimekiri**: Lisatud Swift ja Rust SDKd; uuendatud spetsifikatsiooni link 2025-11-25
- **Spetsifikatsiooni viide**: Uuendatud MCP Spetsifikatsiooni link otsesele spetsifikatsiooni URLile

#### Moodul 07 - Õppetunnid varajastest kasutuselevõttudest
- **Ressursside uuendused**: Lisatud MCP Spetsifikatsioon 2025-11-25 lingid ja OWASP MCP Top 10 täiendavatesse ressurssidesse

#### Moodul 08 - Parimad praktikad
- **Spetsifikatsiooni versioon**: Uuendatud MCP Spetsifikatsiooni viide 2025-11-25 versioonile
- **Turberessursid**: Lisatud OWASP MCP Top 10 ja Sherpa töötoa lingid täiendavatesse viidetesse

#### Moodul 10 - AI töövoogude sujuvamaks muutmine
- **Märgisuuendus**: Vahetatud MCP versiooni märgis SDK versioonilt (1.9.3) spetsifikatsiooni versioonile (2025-11-25)
- **Ressursside lingid**: Uuendatud MCP Spetsifikatsiooni link; lisatud OWASP MCP Top 10

#### Moodul 11 - MCP serveri praktilised laborisessioonid
- **Spetsifikatsiooni viide**: Uuendatud MCP Spetsifikatsiooni link 2025-11-25 versioonile
- **Turberessursid**: Lisatud OWASP MCP Top 10 ametlikesse ressurssidesse

## 18. detsember 2025

### Turbedokumentatsiooni uuendus - MCP Spetsifikatsioon 2025-11-25

#### MCP Turbe parimad praktikad (02-Security/mcp-best-practices.md) - Spetsifikatsiooni versiooni uuendus
- **Protokolli versiooni uuendus**: Uuendatud viide uusimale MCP Spetsifikatsioonile 2025-11-25 (vabastatud 25. novembril 2025)
  - Uuendatud kõik spetsifikatsiooni versiooni viited 2025-06-18 asemel 2025-11-25
  - Uuendatud dokumendi kuupäevad augustist 18, 2025 detsembrisse 18, 2025
  - Kontrollitud, et kõik spetsifikatsiooni URLid osutaksid kehtivale dokumentatsioonile
- **Sisu valideerimine**: Ulatuslik turbe parimate tavade valideerimine viimaste standardite vastu
  - **Microsofti turbeslahendused**: Kinnitatud terminoloogia ja lingid Prompt Shields (varem "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID ja Azure Key Vault kohta
  - **OAuth 2.1 turve**: Kinnitatud uusimate OAuth turbetavade järgimine
  - **OWASP standardid**: Valideeritud, et OWASP Top 10 LLMide puhul on ajakohane
  - **Azure teenused**: Kontrollitud kõik Microsoft Azure dokumentatsiooni lingid ja parimad praktikad
- **Standardite joondamine**: Kõik viidatud turbestandardid on ajakohased
  - NIST AI Riskide juhtimise raamistik
  - ISO 27001:2022
  - OAuth 2.1 turbe parimad tavad
  - Azure turbe ja vastavuse raamistikud
- **Rakendamise ressursid**: Kinnitatud kõik rakendamisjuhendite lingid ja ressursid
  - Azure API haldamise autentimismustrid
  - Microsoft Entra ID integratsiooni juhendid
  - Azure Key Vault saladuste haldamine
  - DevSecOps torujuhtmed ja monitooringulahendused

### Dokumentatsiooni kvaliteedi tagamine
- **Spetsifikatsiooni nõuete järgimine**: Tagatud kõikide MCP turbenõuete (PEAB/PEAB MITTE) vastavus uusimale spetsifikatsioonile
- **Ressursside ajakohasus**: Kontrollitud kõik välised lingid Microsofti dokumentatsioonile, turbestandarditele ja rakendamisjuhenditele
- **Parimate tavade ulatus**: Kinnitatud autentimise, autoriseerimise, AI-spetsiifiliste ohtude, tarneahela turbe ja ettevõttesiseste mustrite kõikehõlmav käsitlemine

## 6. oktoober 2025

### Alustamise sektsiooni laiendus – Täiustatud serverikasutus ja lihtne autentimine

#### Täiustatud serverikasutus (03-GettingStarted/10-advanced)
- **Lisatud uus peatükk**: Tutvustati ulatuslikku juhendit täiustatud MCP serveri kasutamiseks, hõlmates nii tavapärast kui ka madala taseme serveri arhitektuuri.
  - **Tavalise versus madala taseme server**: Üksikasjalik võrdlus ja koodinäited Pythonis ja TypeScriptis mõlemal lähenemisel.
  - **Handleripõhine disain**: Selgitus tööriistade, ressursside ja promptide haldamiseks handleripõhiselt, et toetada skaleeritavaid ja paindlikke serverilahendusi.
  - **Praktilised mustrid**: Reaalmaailma stsenaariumid, kus madala taseme serverimustrid aitavad täiustatud funktsioone ja arhitektuuri.

#### Lihtne autentimine (03-GettingStarted/11-simple-auth)
- **Lisatud uus peatükk**: Samm-sammuline juhend lihtsa autentimise rakendamiseks MCP serverites.
  - **Autentimise kontseptsioonid**: Selged selgitused autentimise ja autoriseerimise ning mandaadihalduse vahel.
  - **Põhjauth rakendus**: Vahevara-põhised autentimismustrid Pythonis (Starlette) ja TypeScriptis (Express), koos koodinäidetega.
  - **Edasiminek täiustatud turbe suunas**: Juhised lihtsast autentimisest alustamiseks ja edasi liikumiseks OAuth 2.1 ja RBAC juurde, koos viidetega täiustatud turbemoodulitele.

Need täiendused pakuvad praktilist ja käed-külge juhendit tugevamate, turvalisemate ja paindlikumate MCP serverilahenduste ehitamiseks, ühendades põhikontseptsioonid täiustatud tootmismustritega.

## 29. september 2025

### MCP serveri andmebaasi integratsiooni laborisessioonid - Ulatuslik praktiline õppeprogramm

#### 11-MCPServerHandsOnLabs - uus täielik andmebaasi integratsiooni õppekava
- **Täielik 13-laboriline õppekava**: Lisatud ulatuslik praktika MCP tootmistasemel serverite ehitamiseks PostgreSQL andmebaasi integratsiooniga
  - **Reaalmaailma rakendus**: Zava Retail analüütiline kasutusjuhtum, mis demonstreerib ettevõtte standardeid
  - **Struktureeritud õppimise progresioon**:
    - **Laborid 00-03: Alused** - Sissejuhatus, põhiehituse arhitektuur, turve & mitme üürnikuga tugi, keskkonna seadistamine
    - **Laborid 04-06: MCP serveri arendus** - Andmebaasi disain & skeem, MCP serveri rakendus, tööriistade arendamine  
    - **Laborid 07-09: Täiustatud funktsioonid** - Semantiline otsing, testimine ja silumine, VS Code integratsioon
    - **Laborid 10-12: Tootmine ja parimad praktikad** - Juhtimise strateegiad, monitooring & jälgitavus, parimad praktikad & optimeerimine
  - **Ettevõtte tehnoloogiad**: FastMCP raamistik, PostgreSQL koos pgvectoriga, Azure OpenAI sisaldised, Azure Container Apps, Application Insights
  - **Täiustatud funktsioonid**: Ridade tasemel turve (RLS), semantiline otsing, mitme üürniku andmete ligipääs, vektorimplantaatide kasutus, reaalajas monitooring

#### Terminoloogia standardiseerimine - Moodulist laborisse üleminek
- **Ulatuslik dokumentatsiooni uuendus**: Süsteemne kõigi README failide uuendus 11-MCPServerHandsOnLabs kataloogis, kasutades terminoloogiat "Labor" "Mooduli" asemel
  - **Sektsioonide päised**: Uuendatud kõigis 13 laboris jaotist "Mida see moodul hõlmab" kujule "Mida see labor hõlmab"
  - **Sisukirjeldus**: Muudetud "See moodul pakub..." kujule "See labor pakub..." dokumentatsioonis
  - **Õpieesmärgid**: Uuendatud "Selle mooduli lõpus..." kujule "Selle labori lõpus..."
  - **Navigatsioonilingid**: Kõik "Moodul XX:" viited muudetud "Labor XX:" viideteks ristviidetes ja navigeerimisel
  - **Lõpetamise jälgimine**: Uuendatud "Pärast selle mooduli lõpetamist..." kujule "Pärast selle labori lõpetamist..."
  - **Tehnilised viited säilitatud**: Säilitatud Python mooduliviited konfiguratsioonifailides (näiteks `"module": "mcp_server.main"`)

#### Õpigrupeeringu täiustamine (study_guide.md)
- **Visuaalne õppekava kaart**: Lisatud uus sektsioon "11. Andmebaasi integratsiooni laborisessioonid" koos ulatusliku laboristruktuuri visualiseerimisega
- **Repositooriumi struktuur**: Uuendatud kümnest üheteistkümneks põhiosas, lisades põhjaliku 11-MCPServerHandsOnLabs kirjelduse
- **Õppeteejuhend**: Täiustatud navigeerimisjuhised, hõlmates sektsioone 00-11
- **Tehnoloogiate käsitlus**: Lisatud FastMCP, PostgreSQL, Azure teenuste integratsiooni üksikasjad
- **Õpitulemused**: Rõhutatud tootmisvalmis serveri arendamist, andmebaasi integratsioonimustreid ja ettevõtte turvalisust

#### Peamise README struktuuri täiustamine
- **Laboripõhine terminoloogia**: Uuendatud 11-MCPServerHandsOnLabs peamist README.md faili järjepidevalt kasutama "Labor" struktuuri
- **Õppeteekonna organiseerimine**: Selge progresioon alustavate kontseptsioonide, täiustatud rakendamise ja tootmisvalmiks juurutamise vahel
- **Reaalmaailma fookus**: Rõhutatud praktilist, käed-külge õppimist ettevõtte standardite ja tehnoloogiatega

### Dokumentatsiooni kvaliteedi ja ühtsuse täiustused
- **Praktiliste õppemomentide rõhutamine**: Tugevdatud käed-külge, laboripõhine lähenemine kogu dokumentatsioonis
- **Ettevõttemustrid**: Esile toodud täisväärtuslikud tootmisvalmid rakendused ja ettevõtte turbe kaalutlused
- **Tehnoloogiate integratsioon**: Kaasaegsete Azure teenuste ja AI integratsioonimustrite ulatuslik käsitlus
- **Õppeteekonna progressioon**: Selge, struktureeritud tee alustavate kontseptsioonide juurest tootmisvalmis juurutamiseni

## 26. september 2025

### Juhtumiuuringute täiustamine - GitHub MCP registri integratsioon

#### Juhtumiuuringud (09-CaseStudy/) - Ökosüsteemi arendusfookus
- **README.md**: Oluline laiendus ulatuslike GitHub MCP registri juhtumiuuringutega
  - **GitHub MCP registri juhtumiuuring**: Uus põhjalik juhtumiuuring, mis uurib GitHub MCP registri lansseerimist septembris 2025
    - **Probleemi analüüs**: Üksikasjalik fragmentide MCP serverite leidmise ja juurutamise väljakutsetest
    - **Lahenduse arhitektuur**: GitHubi keskne registri lähenemine koos ühe klõpsuga VS Code paigaldusega
    - **Äriline mõju**: Mõõdetavad parendused arendaja käivitamisel ja tootlikkuses
    - **Strateegiline väärtus**: Fookus modulaarsele agendi juurutamisele ja tööriistadevahelisele koostalitlusele
    - **Ökosüsteemi arendamine**: Positsioneerimine agentipõhise süsteemi alussektorina
  - **Täiustatud juhtumiuuringu struktuur**: Uuendatud kõik seitse juhtumiuuringut järjepideva vormingu ja põhjalike kirjeldustega
    - Azure AI reisibürood: Mitmeagendi orkestreerimise rõhuasetus
    - Azure DevOps integratsioon: Töövoo automatiseerimise keskendumine
    - Reaalajas dokumentide päring: Python konsooliklient
    - Interaktiivne õppeplaani generaator: Chainlit vestluspõhine veebirakendus
    - Redaktori sees dokumentatsioon: VS Code ja GitHub Copilot integratsioon
    - Azure API haldamine: Ettevõtte API integratsiooni mustrid
    - GitHub MCP registri: Ökosüsteemi arendus ja kogukonna platvorm
  - **Ulatuslik järeldus**: Ümberkirjutatud kokkuvõtte peatükk, mis rõhutab seitset erinevat juhtumiuuringut, hõlmates mitmeid MCP rakendamismõõtmeid
    - Ettevõtte integratsioon, mitmeagendi orkestreerimine, arendaja tootlikkus
    - Ökosüsteemi arendus, hariduslike rakenduste kategoriseerimine
    - Täiustatud teadmised arhitektuurimustritest, rakendusstrateegiatest ja parimatest praktikatest
    - Rõhuasetus MCP-le kui küpsele, tootmisvalmiks protokollile

#### Õpigruppi juhendi uuendused (study_guide.md)
- **Visuaalne õppekava kaart**: Uuendatud mõttekart gramm GitHub MCP registri lisamiseks juhtumiuuringute sektsiooni
- **Juhtumiuuringute kirjeldus**: Täiustatud üldistest kirjeldustest üksikasjalikuks ülevaateks seitsmel põhjalikul juhtumiuuringul
- **Repositooriumi struktuur**: Uuendatud 10. sektsioon hõlmama põhjalikku juhtumiuuringute käsitlust koos konkreetsete rakenduse detailidega
- **Muudatuste logi integreerimine**: Lisatud 26. septembri 2025 sissekanne, mis dokumenteerib GitHub MCP registri lisamist ja juhtumiuuringute täiustusi
- **Kuupäeva uuendused**: Uuendatud jaluse ajatempli peegeldamaks viimast versiooni (26. september 2025)

### Dokumentatsiooni kvaliteedi parandused
- **Järjepidevuse täiustamine**: Standardiseeritud juhtumiuuringute vormindus ja struktuur kõigis seitsmes näites
- **Ulatuslik käsitlus**: Juhtumiuuringud hõlmavad nüüd ettevõtte, arendaja tootlikkuse ja ökosüsteemi arendusstsenaariume
- **Strateegiline positsioneerimine**: Täiustatud fookus MCP-le agentipõhise süsteemide rakendamise fundamentaalse platvormina
- **Ressursside integreerimine**: Täiendatud täiendavad ressursid lisades GitHub MCP registri lingi

## 15. september 2025

### Täiustatud teemade laiendus - Kohandatud transpordid ja konteksti inseneritöö

#### MCP kohandatud transpordid (05-AdvancedTopics/mcp-transport/) - uus täiustatud rakendamise juhend
- **README.md**: Täielik rakendamisjuhend kohandatud MCP transpordimehhanismide kohta
  - **Azure Event Grid transport**: Ulatuslik serverivaba sündmustel põhineva transpordi rakendus
    - Näited C#, TypeScript ja Python keelega Azure Functions integratsiooniga
    - Sündmustel põhineva arhitektuuri mustrid skaleeritavate MCP lahenduste jaoks
    - Webhook vastuvõtjad ja push-sõnumi käsitlemine
  - **Azure Event Hubs transport**: Suure läbilaskevõimega voogedastuse transpordi rakendus
    - Reaalajas voogedastuse võimalused madala latentsusega stsenaariumites
    - Partitsioneerimise strateegiad ja kontrollpunktide haldus
    - Sõnumite virnastamine ja jõudluse optimeerimine
  - **Ettevõtte integratsioonimustrid**: Tootmisvalmis arhitektuurinäited
    - Hajutatud MCP töötlemine mitmes Azure Functions funktsioonis
    - Hübriidtranspordi arhitektuurid, mis ühendavad mitut transporditüüpi
    - Sõnumi vastupidavus, usaldusväärsus ja veakäsitluse strateegiad
  - **Turve ja monitooring**: Azure Key Vault integratsioon ja jälgitavuse mustrid
    - Hallatud identiteedi autentimine ja minimaalsete õiguste ligipääs
    - Application Insights telemeetria ja jõudluse jälgimine
    - Kaitseseadmed ja vigursallivuse mustrid
  - **Testimisraamistikud**: Ulatuslikud testimisstrateegiad kohandatud transpordide jaoks
    - Ühiktestimine testtopeltide ja simulatsiooniraamistikega
    - Integratsioonitestimine Azure Test Containersiga
    - Jõudluse ja koormuse testimise kaalutlused

#### Konteksti inseneritöö (05-AdvancedTopics/mcp-contextengineering/) - Kujunev tehisintellekti distsipliin
- **README.md**: Läbivaatus konteksti inseneritööst kui kujunevast valdkonnast
  - **Põhiprintsiibid**: Täielik konteksti jagamine, tegevusotsuste teadlikkus ja konteksti akna haldus

  - **MCP protokolli vastavus**: Kuidas MCP disain lahendab kontekstitöötluse väljakutseid
    - Kontekstiakna piirangud ja progressiivsed laadimisstrateegiad
    - Asjakohasuse määramine ja dünaamiline konteksti hankimine
    - Mitme modaalne konteksti töötlemine ja turvalisuse kaalutlused
  - **Rakendusviisid**: Üheteljelised vs. mitmeagendi arhitektuurid
    - Kontekstitükkide tegemise ja prioriseerimise tehnikad
    - Progressiivne konteksti laadimine ja tihendamisstrateegiad
    - Kihilised kontekstilähenemised ja hankimise optimeerimine
  - **Mõõtmise raamistik**: Uued mõõdikud konteksti tõhususe hindamiseks
    - Sisendi efektiivsus, jõudlus, kvaliteet ja kasutajakogemus
    - Katsemeetodid konteksti optimeerimiseks
    - Rikkefailide analüüs ja täiustamismetoodikad

#### Õppekava navigeerimise uuendused (README.md)
- **Täpsem mooduli struktuur**: Uuendatud õppekava tabel lisamaks uusi edasijõudnute teemasid
  - Lisatud kontekstitöötlus (5.14) ja kohandatud transport (5.15) kirjed
  - Ühtlane vormindus ja navigeerimislingid kõikides moodulites
  - Uuendatud kirjeldused vastavaks praegusele sisule

### Kaustastruktuuri täiustused
- **Nimede standardiseerimine**: "mcp transport" ümber nimetatud "mcp-transport" järjepidevuse huvides teiste täiustatud teemade kaustadega
- **Sisu organiseerimine**: Kõik 05-AdvancedTopics kaustad järgivad nüüd ühtset nimetamismustrit (mcp-[teema])

### Dokumentatsiooni kvaliteedi parandused
- **MCP spetsifikatsiooni vastavus**: Kõik uus sisu viitab praegusele MCP spetsifikatsioonile 2025-06-18
- **Mitmekeelsed näited**: Ulatuslikud koodinäited C#, TypeScript ja Python keeles
- **Ettevõttesisene fookus**: Tootmiseks valmis mustrid ja Azure pilve integratsioon kogu materjalis
- **Visuaalne dokumentatsioon**: Mermaid skeemid arhitektuuri ja voogude visualiseerimiseks

## 18. august 2025

### Dokumentatsiooni põhjalik uuendus - MCP 2025-06-18 standardid

#### MCP turvalisuse parimad tavad (02-Security/) - Täielik moderniseerimine
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Täielik ümberkirjutus vastavuses MCP spetsifikatsiooniga 2025-06-18
  - **Kohustuslikud nõuded**: Lisatud selged PEAB/PEAB MITTE nõuded ametlikust spetsifikatsioonist koos visuaalsete indikaatoritega
  - **12 põhilist turvapraktilist juhendit**: Muudetud 15-punktilisest loendist ulatuslikeks turva valdkondadeks
    - Märgistamise turvalisus ja autentimine väliste identiteedipakkujate integratsiooniga
    - Sessioonihaldus ja transpordi turvalisus krüptograafiliste nõuetega
    - AI-spetsiifiline ohutuse kaitse Microsoft Prompt Shieldsi integratsiooniga
    - Juhtimis- ja õiguste haldus vähemalt privileegide põhimõttega
    - Sisu turvalisus ja järelevalve Azure Content Safety integratsiooniga
    - Tarneahela turvalisus ulatuslike komponendi kontrollidega
    - OAuth turvalisus ja Confused Deputy rünnete ennetus PKCEga
    - Intsidendi reageerimine ja taastumine automatiseeritud võimekusega
    - Vastavus ja valitsemine regulatiivse nõuetega
    - Täiustatud turvakontrollid null usalduse arhitektuuriga
    - Microsoft turvaökosüsteemi integratsioon ulatuslike lahendustega
    - Pidev turvaarenemine kohanemisvõimeliste praktikutega
  - **Microsofti turvalahendused**: Täiustatud integratsiooni juhised Prompt Shieldsi, Azure Content Safety, Entra ID ja GitHub Advanced Security jaoks
  - **Rakendusressursid**: Kategooriatena esitatud ulatuslikud ressursilingid ametliku MCP dokumentatsiooni, Microsofti turvalahenduste, turvastandardite ja rakendusjuhiste kaupa

#### Täiustatud turvakontrollid (02-Security/) - Ettevõttesisene rakendus
- **MCP-SECURITY-CONTROLS-2025.md**: Täielik ülevaatus ettevõtte tasemel turvaraamistikuga
  - **9 ulatuslikku turvavaldkonda**: Põhikontrollidest ümber töötatud üksikasjalikuks ettevõtte raamistiku
    - Täiustatud autentimine ja volitamine Microsoft Entra ID integratsiooniga
    - Märgistamise turvalisus ja läbipääsu kontrollid ulatusliku valideerimisega
    - Sessiooni turvakontrollid ülevõtmise ennetamiseks
    - AI spetsiifilised turvakontrollid õpetuste süstimise ja tööriista mürgitamise ennetusega
    - Confused Deputy rünnete ennetus OAuth proxy turvameetmetega
    - Tööriistade täitmise turvalisus liivakasti ja isolatsiooni kasutades
    - Tarneahela turvakontrollid sõltuvuste kontrolliga
    - Jälgimis- ja avastamiskontrollid SIEM integratsiooniga
    - Intsidendi reageerimine ja taastumine automatiseeritud võimestusega
  - **Rakendusnäited**: Lisatud üksikasjalikud YAML konfiguratsiooni plokid ja koodinäited
  - **Microsofti lahenduste integratsioon**: Ulatuslik käsitlus Azure turvateenuste, GitHub Advanced Security ja ettevõtte identiteedihaldusega

#### Täiustatud teemade turvalisus (05-AdvancedTopics/mcp-security/) - Tootmiseks valmis rakendus
- **README.md**: Täielik ümberkirjutus ettevõtte turvarakendamiseks
  - **Praegune spetsifikatsiooni vastavus**: Uuendatud MCP spetsifikatsiooniga 2025-06-18 ning kohustuslike turvanõuetega
  - **Täiustatud autentimine**: Microsoft Entra ID integreerimine ulatuslike .NET ja Java Spring Security näidetega
  - **AI turvaintegratsioon**: Microsoft Prompt Shields ja Azure Content Safety rakendus üksikasjalike Python näidetega
  - **Täiustatud ohtude leevendamine**: Ulatuslikud rakendusnäited
    - Confused Deputy rünnete ennetamine PKCE ja kasutaja nõusoleku valideerimisega
    - Märgistuse läbipääsu ennetamine publiku valideerimise ja turvalise märgistusjuhtimisega
    - Sessiooni ülevõtmise ennetus krüptograafilise sidumise ja käitumusanalüüsiga
  - **Ettevõtte turvaintegratsioon**: Azure Application Insights jälgimine, ohtude tuvastamise torustikud ja tarneahela turvalisus
  - **Rakendusnimekiri**: Selged kohustuslikud vs soovitatavad turvakontrollid koos Microsofti turvaökosüsteemi eelistega

### Dokumentatsiooni kvaliteet ja standardite vastavus
- **Spetsifikatsiooniviited**: Uuendatud kõik viited praegusele MCP spetsifikatsioonile 2025-06-18
- **Microsofti turvaökosüsteem**: Paranenud integratsioonijuhised kogu turvadokumentatsioonis
- **Praktilised rakendused**: Lisatud üksikasjalikud koodinäited .NET, Java ja Python keeles koos ettevõttesiseste mustritega
- **Ressursside organiseerimine**: Ulatuslik ametliku dokumentatsiooni, turvastandardite ja rakendusjuhiste kategooriajaotus
- **Visuaalsed indikaatorid**: Selge märgistus kohustuslike nõuete ja soovitatud praktikate vahel


#### Põhikontseptsioonid (01-CoreConcepts/) - Täielik moderniseerimine
- **Protokolli versiooni uuendus**: Uuendatud viide praegusele MCP spetsifikatsioonile 2025-06-18 koos kuupõhise versiooninumbriga (AAAA-KK-PP vorming)
- **Arhitektuuri täpsustamine**: Parandatud kirjeldused Hostidest, klientidest ja serveritest MCP arhitektuuri mustrite järgi
  - Hostid nüüd selgelt määratletud kui AI rakendused, mis koordineerivad mitut MCP kliendiühendust
  - Kliendid kirjeldatud protokolli ühendajatena, säilitades ühe-ühele serveri seosed
  - Serverid täiustatud lokaalse vs kaugjuhtimise paigaldusstsenaariumitega
- **Primitiivide ümberkorraldus**: Serveri ja kliendi primitiivide täielik ülevaatus
  - Serveri primitiivid: Ressursid (andmeallikad), Päringud (mallid), Tööriistad (täidetavad funktsioonid) koos üksikasjalike selgituste ja näidetega
  - Kliendi primitiivid: Valimine (LLM vastused), Päring (kasutaja sisend), Logimine (silumine/jälgimine)
  - Uuendatud praeguste avastamise (`*/list`), hankimise (`*/get`) ja täitmise (`*/call`) metodoloogiate mustritega
- **Protokolli arhitektuur**: Esitatud kahekihiline arhitektuuri mudel
  - Andmekiht: JSON-RPC 2.0 alus koos elutsükli halduse ja primitiividega
  - Transpordikiht: STDIO (kohalik) ja streamitav HTTP koos SSE (kaug-) transpordimehhanismidega
- **Turvarest**: Ulatuslikud turvapõhimõtted, sh kasutaja selge nõusolek, andmekaitse, tööriistade täitmise turvalisus ja transpordikihi turvalisus
- **Kommunikatsioonimustrid**: Uuendatud protokollisõnumid, mis näitavad initsialiseerimist, avastamist, täitmist ja teavitusi
- **Koodinäited**: Värskendatud mitmekeelsed näited (.NET, Java, Python, JavaScript) vastavalt praegustele MCP SDK mustritele

#### Turvalisus (02-Security/) - Ulatuslik turvapõhikorrastus  
- **Standardite vastavus**: Täielik kooskõla MCP spetsifikatsiooni 2025-06-18 turvanõuetega
- **Autentimise areng**: Dokumenteeritud areng kohandatud OAuth serveritest väliste identiteedipakkujate delegeerimiseni (Microsoft Entra ID)
- **AI spetsiifiline ohtude analüüs**: Paranenud kajastus tänapäevastele AI rünnakute vektoritele
  - Üksikasjalikud õpetuste süstimise ründe stsenaariumid reaalse maailma näidetega
  - Tööriistamürgituse mehhanismid ja "rug pull" ründemustrid
  - Konteksti akna mürgitus ja mudeli segaduse rünnakud
- **Microsoft AI turvarahastused**: Ulatuslik ülevaade Microsofti turvaökosüsteemist
  - AI Prompt Shieldsid koos täiustatud tuvastuse, esiletõstmise ja eraldusmeetoditega
  - Azure Content Safety integratsiooni mustrid
  - GitHub Advanced Security tarneahela kaitseks
- **Täiustatud ohtude leevendus**: Üksikasjalikud turvakontrollid
  - Sessiooni ülevõtmine MCP-spetsiifiliste ründe stsenaariumitega ja krüptograafiliste sessiooni ID nõuetega
  - Confused Deputy probleemid MCP proksi stsenaariumites koos selgete nõusoleku nõuetega
  - Märgistuse läbipääsu haavatavused kohustuslike valideerimiskontrollidega
- **Tarneahela turvalisus**: Laiendatud AI tarneahela käsitlus kaasates baasmodelle, manustusteenuseid, kontekstipakkujaid ja kolmanda osapoole API-sid
- **Põhi turvalisus**: Täiustatud integratsioon ettevõtte turvamustritega, sh null usalduse arhitektuur ja Microsofti turvaökosüsteem
- **Ressursside organiseerimine**: Kategooriatena esitatud ulatuslikud ressursilingid tüübi kaupa (ametlik dokumentatsioon, standardid, uurimused, Microsofti lahendused, rakendusjuhendid)

### Dokumentatsiooni kvaliteedi parandused
- **Struktureeritud õpieesmärgid**: Täiustatud õpieesmärgid spetsiifiliste ja teostatavate tulemustega 
- **Vastastikused viited**: Lisatud lingid seotud turva ja põhimõistete teemade vahel
- **Ajakohane info**: Uuendatud kõik kuupäeva viited ja spetsifikatsiooni lingid praeguste standardite järgi
- **Rakendusjuhised**: Lisatud spetsiifilised ja teostatavad rakendusjuhised mõlemas osas

## 16. juuli 2025

### README ja navigeerimise täiustused
- Täielikult ümber kujundatud õppekava navigeerimine README.md-s
- Asendatud `<details>` sildid ligipääsetavama tabelipõhise vorminguga
- Loodud alternatiivsed paigutusvalikud uues "alternative_layouts" kaustas
- Lisatud kaartidel põhinevad, tabulaarsed ja akordionstiilis navigeerimisnäited
- Uuendatud hoidla struktuur jaotises, et hõlmata kõiki viimaseid faile
- Täiustatud "Kuidas seda õppekava kasutada" jaotis selgete soovitustega
- Uuendatud MCP spetsifikatsiooni lingid õigetesse URL-idesse
- Lisatud kontekstitöötluse jaotis (5.14) õppekava struktuuri

### Õppekava juhendi uuendused
- Täielikult uuendatud õppekavajuhend vastavaks praegusele hoidla struktuurile
- Lisatud uued jaotised MCP klientide ja tööriistade ning populaarsete MCP serverite jaoks
- Uuendatud visuaalne õppekava kaart kõigi teemade täpseks kajastamiseks
- Täiustatud Advanced Topics kirjeldusi kõigi spetsialiseeritud valdkondade katmiseks
- Uuendatud juhtumiuuringute jaotis, et kajastada tegelikke näiteid
- Lisatud see põhjalik muudatuste logi

### Kogukonna panused (06-CommunityContributions/)
- Lisatud üksikasjalik info MCP serverite kohta piltide genereerimiseks
- Lisatud ulatuslik jaotis Claude kasutamisest VSCode-is
- Lisatud Cline terminalikliendi seadistamise ja kasutusjuhendid
- Uuendatud MCP kliendi jaotis, mis sisaldab kõiki populaarseid kliendivalikuid
- Täiustatud panuse näited täpsemate koodinäidetega

### Täiustatud teemad (05-AdvancedTopics/)
- Korraldatud kõik spetsialiseeritud teema kaustad ühtse nimetamisega
- Lisatud kontekstitöötluse materjalid ja näited
- Lisatud Foundry agendi integratsiooni dokumentatsioon
- Täiustatud Entra ID turvaintegratsiooni dokumentatsioon

## 11. juuni 2025

### Esmane loomine
- Välja lastud MCP algajate õppekava esimene versioon
- Loodud põhistruktuur kõigi 10 põhijaotise jaoks
- Rakendatud Visuaalne õppekava kaart navigeerimiseks
- Lisatud esialgsed prooviprojektid mitmes programmeerimiskeeles

### Alustamine (03-GettingStarted/)
- Loodud esimesed serveri rakendusnäited
- Lisatud kliendi arendusjuhend
- Kaasas LLM kliendi integratsiooni juhised
- Lisatud VS Code integratsiooni dokumentatsioon
- Rakendatud Server-Sent Events (SSE) serveri näited

### Põhikonseptsioonid (01-CoreConcepts/)
- Lisatud kliendi-serveri arhitektuuri üksikasjalik selgitus
- Loodud dokumentatsioon võtmeprotokolli komponentide kohta
- Dokumenteeritud sõnumimustrid MCP-s

## 23. mai 2025

### Hoidla struktuur
- Initsialiseeritud hoidla baaskaustastruktuuriga
- Loodud README-failid iga suurema jaotise tarbeks
- Seadistatud tõlke infrastruktuur
- Lisatud pildid ja skeemid

### Dokumentatsioon
- Loodud esialgne README.md õppekava ülevaatega
- Lisatud CODE_OF_CONDUCT.md ja SECURITY.md failid
- Seadistatud SUPPORT.md abi saamise juhistega
- Loodud esmane õppekava struktuur

## 15. aprill 2025

### Planeerimine ja raamistik
- Esmane planeerimine MCP for Beginners õppekavaks
- Määratletud õpieesmärgid ja sihtrühm
- Kirjeldatud õppekava 10 jaotise struktuur
- Töötatud välja kontseptuaalne raamistik näidete ja juhtumiuuringute jaoks
- Loodud esialgsed prototüübi näited võtmekontseptsioonide kohta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
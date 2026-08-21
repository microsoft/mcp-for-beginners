# Pokyčių žurnalas: MCP pradedantiesiems kursas

Šis dokumentas tarnauja kaip įrašas apie visus svarbius pakeitimus, atliktus Modelio konteksto protokolo (MCP) pradedantiesiems kurse. Pakeitimai dokumentuojami atvirkštine chronologine tvarka (naujausi pakeitimai pirmi).

## 2026 m. liepos 29 d.

### Naujas 08 modulio palydovas: Patikimumo papildiniai ir saugūs bandymai iš naujo

Pridėta tiekėjų neutrali palydovinė pamoka MCP įrankiams, kurie sukuria realaus pasaulio
poveikius, suderinta su galutine `2026-07-28` specifikacija.

- **Naujas**: [patikimumo papildinė pamoka][reliability-sidecar]
  naudoja vieną palaikymo bilieto istoriją, du Mermaid diagramas ir bandymo iš naujo
  sprendimų srautą, kad paaiškintų stabilios veiklos raktus, atominį dubliavimo
  priėmimą, suderinimą, įrodymus ir užduočių plėtinių ribą.
- **Naujas**: Standartinės bibliotekos Python ir SQLite gedimų injekcijos pratimas
  naudoja atskiras operacijų ir bilietų saugyklas, kad parodytų atsakymo praradimą
  po išorinio poveikio įsipareigojimo. Šeši deterministiniai testai apima naivų
  dubliavimą, apsaugotą paleidimo atkūrimą, informacijos konfliktus, talpyklos rezultatus,
  aktyvius reikalavimus ir vienalaikį dubliavimo priėmimą.
- **Atnaujinta**: 08 modulis dabar susieja palydovinę pamoką, identifikuoja
  galutinį `2026-07-28` bevaldišką užklausos modelį, atskiria OpenTelemetry
  stebėjimą nuo pasenusių MCP žurnalų funkcijų ir riboja savo
  bendrinį bandymą iš naujo skaitymo operacijoms.
- **Pasirinktinai**: Pamoka susieja savo nešiojamus konceptus su vienu žymimu bendruomenės
  įgyvendinimu, neįtraukdama talpinamos paslaugos ar tinklo užklausos į
  pratimą.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026 m. liepos 2 d.

### Nauja pamoka: 2026-07-28 MCP specifikacijos leidimo kandidatas

Pridėtas būsimam `2026-07-28` MCP specifikacijos leidimo kandidatui skirtas turinys (paskelbta 2026 m. gegužės 21 d.; galutinis leidimas suplanuotas 2026 m. liepos 28 d.), apibendrinta iš [oficialaus pranešimo tinklaraščio įrašo](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Kurso pagrindas išlieka **MCP specifikacija 2025-11-25**, kol nebus išleista nauja versija, todėl tai pateikiama kaip įžvalga į ateitį, o ne esamų pamokų perrašymas.

- **Naujas**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) – visa pamoka, skirta bevaldiško protokolo branduoliui (inicijavimo rankos spaudimo ir `Mcp-Session-Id` pašalinimas), naujiems `Mcp-Method`/`Mcp-Name` maršruto antraštėms, `ttlMs`/`cacheScope` talpyklos metaduomenims, W3C Trace Context `_meta`, oficialiai Išplėtimo sistemai (MCP programėlėms ir naujam Užduočių praplečiamumui), šešioms autorizacijos stiprinimo SEP, Roots/Sampling/Logging nebenaudojimui ir pereinam į pilną JSON Schema 2020-12 įrankių schemas.
- **Atnaujinta** su ateities nuorodomis, susiejančiomis su nauja pamoka:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolo versijos pastaba, Sampling/Roots/Logging/Tasks skyriai ir "Kas toliau"

  - [02-Security/README.md](./02-Security/README.md): autorizacijos stiprinimo įspėjimas
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): bevalstės transporto įspėjimas
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Imties ėmimo nutraukimo įspėjimas
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Žurnalų fiksavimo nutraukimas ir Uždaviniai plėtinio įspėjimas
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): bevalstės/sesijos maršruto įspėjimas
  - [README.md](./README.md): skyriuje „Žvelgiant į priekį“ pažymėtas pranešimas ir nauja `1.1` įrašas mokymų modulių lentelėje
  - [study_guide.md](./study_guide.md): pažymėtas į ateitį orientuotas šaškių taškas pagrindinių sąvokų apžvalgoje ir datuotas priedas
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): įspėjimas apie `mcp-session-id` transporto žemėlapį prieš bevalstės užklausų modelį
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): modulio apžvalgos įspėjimas apie Pagrindinius kontekstus/Imties ėmimą nutraukimus ir Uždavinių plėtinį
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorizacijos stiprinimo įspėjimas

## 2026 m. birželio 24 d.

### Nauja pamoka: MCP naudojimas Copilot programėlėje

- [Įrankių skyrius](./12-tooling/README.md) Pridėtas įrankių skyrius.
- [MCP Copilot programėlėje](./12-tooling/01-copilot-app/README.md)

## 2026 m. birželio 16 d.

### MCP specifikacijos suderinimas ir pavyzdžių patikra

Patikrintas mokymų turinys pagal dabartinę **MCP specifikaciją 2025-11-25** ir naujausias oficialias SDK versijas, pataisyti likę pasenusioje specifikacijoje nurodyti elementai bei patvirtinta, kad pagrindiniai pavyzdžiai vis dar veikia.

#### Specifikacijos versijos pataisymai (2025-06-18 / 2025-03-26 → 2025-11-25)

Atnaujintas anglų kalbos turinys, kuriame dar buvo teigiama, kad senesnė specifikacijos versija yra *dabartinė/atestuota* standartas, ir nuorodos nukreiptos į kanoninį `modelcontextprotocol.io` specifiakcijos kelią:
- **05-AdvancedTopics/mcp-security/README.md**: atnaujintas „Dabartinio standarto“ baneris, įvadas, pagrindiniai saugumo principų antraštė, privalomų reikalavimų antraštė, Microsoft Entra ID skyrius, Nuorodos ir ištekliai, bei uždarantis saugumo pranešimas (8 nuorodos) į 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: atnaujinta Papildomų išteklių nuoroda į specifikaciją ir „Dabartinio standarto“ baneris į 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: pakeista pasenusi `2025-03-26` saugumo-ir-patikimumo nuoroda į dabartinę 2025-11-25 saugumo geriausios praktikos svetainę

- **03-GettingStarted/14-sampling/README.md**: Atnaujinta oficiali imties paėmimo dokumentacijos nuoroda į 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Atnaujinta esamo laiko „dabartinės MCP specifikacijos“ nuoroda ir Papildomų išteklių specifikacijos nuoroda į 2025-11-25 (istorinės SSE palaikymo nutraukimo pastabos paliktos tikslumui išlaikyti)

#### Pavyzdžių validavimas su dabartiniais SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` išsprendė `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` praėjo be tipo klaidų — esami `McpServer`/`StdioServerTransport` API lieka galiojantys
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validuota izoliuotoje `.venv` aplinkoje su `mcp[cli]` (1.27.2); `py_compile` praėjo ir `FastMCP.list_tools()` teisingai grąžino `add` ir `subtract` įrankius
- Patvirtinta, kad visos pavyzdžių `@modelcontextprotocol/sdk` versijos ribos (`>=1.26.0` / `^1.26.0` / `^1.27.0`) be problemų išsprendžiamos į dabartinę `1.29.0` versiją be API sutrikdymų

#### Priklausomybių užfiksavimo suderinamumas (versijų tarpų uždarymas)

Pakeltas pasenęs SDK versijos užfiksavimas, todėl kiekvienas pavyzdys atitinka dabartinį MCP leidimą, pagal bendrą repozitorijos praktiką:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Pakeltas `@modelcontextprotocol/sdk` nuo `^1.8.0` iki `>=1.26.0` ir atnaujintas pasenęs paketo aprašas iš `"updated for MCP 2025-06-18"` į `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ir **lab4/code/github_mcp_server/pyproject.toml**: Pakeltas tikslus užfiksavimas `mcp==1.23.0` į `mcp>=1.26.0`; vėl sugeneruoti abu `uv.lock` failai (`uv lock`), kad užrakinimo failai atitiktų dabartinę `mcp 1.27.2` versiją ir būtų suderinti su manifestais

#### Sąlygų trūkumo analizė – naujausių specifikacijų funkcijų aprėptis

Patikrinta, kad mokymo programa jau apima visas MCP 2025-11-25 įvestas/plečiamas funkcijas, tad turinys komplektuotas:
- **Atrankos (Sampling)**: Pamoka 03-GettingStarted/14-sampling ir 05-AdvancedTopics/mcp-sampling
- **Inicijavimas (įskaitant URL režimą)**: Dokumentuota 01-CoreConcepts ir 05-AdvancedTopics/mcp-protocol-features
- **Šaknys**: Dokumentuota 00-Introduction, 01-CoreConcepts, ir 05-AdvancedTopics/mcp-root-contexts
- **Užduotys (eksperimentinės, ilgai vykstančios operacijos)**: Dokumentuota 01-CoreConcepts ir 05-AdvancedTopics/mcp-protocol-features
- **Įrankių anotacijos** (`readOnlyHint` / `destructiveHint`): Dokumentuota 01-CoreConcepts ir 05-AdvancedTopics/mcp-protocol-features

### Saugumo stiprinimas ir priklausomybių pažeidžiamumo šalinimas

Vykdyta pilna saugumo patikra visų priklausomybių manifestuose ir pavyzdžių šaltinio kode, vėliau pašalintos visos praneštos npm įspėjimų klaidos ir viena kodo lygmens problema. Po pataisymų `npm audit` rodo **0 pažeidžiamumų** visuose tikrintuose kataloguose.

#### npm priklausomybių pažeidžiamumai (perkelti) — Ištaisyta

Patikrinti visi 15 įtrauktų `package-lock.json` failų. Pažeidžiamumai buvo riboti prie perkeliamų priklausomybių, kuriuos įtraukdavo MCP Inspector kūrimo įrankis, OpenAI klientas ir MCP SDK; visi dabar išspręsti nepažeidžiant pavyzdžių:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ir **lab3/code/weather_mcp/inspector**: Pakeltas `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), kuris pašalino įtrauktą `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ir `ws` įspėjimų problemas. Pridėtas npm `overrides` įrašas, priverčiantis pataisytą `shell-quote@1.8.4` pašalinti likusią kritinę įspėjimą, kurią sukėlė `concurrently`; abu užrakinimo failai pergeneruoti (dabar 0 pažeidžiamumų)
- **03-GettingStarted/samples/typescript**: `npm audit fix` atnaujino perkeliamą `qs` (vidutinis) į pataisytą versiją
- **03-GettingStarted/samples/javascript**: `npm audit fix` atnaujino perkeliamą `hono` (vidutinis) į pataisytą versiją
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` atnaujino perkeliamą `form-data` (didelis) į pataisytą versiją
- **03-GettingStarted/11-simple-auth/solution/typescript**: Sugeneruotas trūkstamas `package-lock.json`, kad projektas būtų atkuriamas ir tikrinamas (0 pažeidžiamumų)

#### Kodo lygmens saugumo pataisa (OWASP A03: Įvedimo injekcija)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Pašalintas `shell=True` iš `open_in_vscode` įrankio. Ankstesnis `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` leido apdoroti aplanko kelią per shell metatezes simbolius komandoje (`cmd.exe`), kas galėjo sukelti komandos injekcijos puolimą. Dabar tiesiogiai paleidžiamas „Code.exe“ su aplanku kaip argumentu — jokio shell — funkcionaliai ekvivalentu ir saugu

#### Python priklausomybių tikrinimas

- Patikrintos visos Python reikalavimų rinkinio priklausomybės su `pip-audit`. `05-AdvancedTopics` ir `03-GettingStarted/samples/python` pranešė **neaptikta žinomų pažeidžiamumų** (jų `mcp` / `httpx` / `pydantic` / `python-dotenv` versijų ribos išsprendžiamos į dabartines pataisytas versijas)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` aptiko perkeliamą priklausomybę **`werkzeug` 3.1.1** su trimis `safe_join` Windows įrenginio pavadinimo DoS įspėjimais — `CVE-2025-66221`, `CVE-2026-21860` ir `CVE-2026-27199` (visi pataisyti 3.1.6 versijoje). Pridėtas aiškus saugumo užfiksavimas `werkzeug>=3.1.6`, kad išspręstų pataisytą versiją; patikrinta, kad apribojimas tvarkingai išsprendžiamas kartu su `chainlit` / `mcp` / `semantic-kernel` paketu

### Produkto pavadinimo perkėlimas (rebrandingas)

Atnaujintas visas mokymo turinys, atitinkantis Microsoft produkto pavadinimo pakeitimus:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Atnaujinta Discord bendruomenės nuoroda

- **AGENTS.md**: Atnaujinta Discord serverio nuoroda
- **README.md**: Atnaujintos technologijų ekosistemos nuorodos
- **study_guide.md**: Atnaujintos atvejo studijos nuorodos
- **05-AdvancedTopics/README.md**: Atnaujintas 5.13 modulio pavadinimas ir aprašymas
- **05-AdvancedTopics/mcp-integration/README.md**: Atnaujinta skyriaus antraštė ir aprašymas
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Pilnas modulio pavadinimo ir turinio atnaujinimas
- **05-AdvancedTopics/mcp-security-entra/README.md**: Atnaujinta kryžminės nuorodos saitas
- **07-LessonsfromEarlyAdoption/README.md**: Atnaujintos atvejo studijos nuorodos
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Atnaujinta 9 skyriaus antraštė, ženkleliai ir galimybės
- **08-BestPractices/README.md**: Atnaujinta Discord bendruomenės nuoroda
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Atnaujinta Discord kanalo nuoroda
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Atnaujinta modelio diegimo nuoroda
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Atnaujinta AI paslaugų lentelė
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Atnaujintos išteklių nuorodos

#### AI rinkinys / AITK → Microsoft Foundry Toolkit papildinys VS Code
- **README.md**: Atnaujintos pagrindinės mokymosi medžiagos nuorodos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Atnaujintas modulio pavadinimas, apžvalga ir visi modulio antraštės elementai
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Atnaujintas pavadinimas, mokymosi tikslai, parengimo instrukcijos ir ištekliai
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Atnaujintas pavadinimas, mokymosi tikslai, MCP šeimininkų lentelė ir kryžminės nuorodos
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Atnaujintas pavadinimas, ženkleliai, išankstiniai reikalavimai ir ištekliai
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Atnaujintos Agentų kūrėjo nuorodos ir atsiliepimų saitas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Atnaujinti išankstiniai reikalavimai ir papildymo nuorodos

---

## 2026 m. balandžio 11 d.

### Nauja pamoka, dokumentacijos pataisymai ir priklausomybių atnaujinimai

#### Pridėta naujo mokymosi turinio

**Modulis 05 - Išplėstiniai dalykai**
- **Pamoka 5.17: Konkurencinis kelių agentų samprotavimas su MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Naujas išsamus vadovas apie konkurencinės diskusijos modelį kelių agentų sistemoms
  - Mermaid architektūros diagrama: du agentai → bendras MCP serveris → diskusijos transkriptas → teisėjas → verdiktas
  - Bendras MCP įrankių serveris (`web_search` + `run_python`), įgyvendintas Python ir TypeScript kalbomis
  - Priešingi sistemos raginimai (FOR / AGAINST / Teisėjas) su aiškiais įrankių naudojimo reikalavimais
  - Diskusijų organizatorius Python, TypeScript ir C# kalbomis, valdantis raundus ir argumentų maršrutizavimą
  - MCP `ClientSession` prijungimas organizatoriui tikram įrankių kvietimui
  - Panaudojimo scenarijų lentelė (halucinacijų aptikimas, grėsmių modeliavimas, API dizaino peržiūra, faktų patikra, technologijų parinkimas)
  - Saugumo aspektai: izoliuotas vykdymas, įrankių kvietimų patvirtinimas, kvotų ribojimas, audito žurnalo vedimas
  - Struktūruota užduotis su trimis praktinėmis situacijomis (kodo peržiūra, architektūros sprendimas, turinio moderavimas)

#### Dokumentacijos pataisymai

**Modulis 03 - Pradžia**
- **05-stdio-server/README.md**: Ištaisyta neišsami TypeScript stdio serverio pavyzdžio klaida — pridėta trūkstama transporto instancija (`new StdioServerTransport()`) ir `server.connect(transport)` kvietimas, kad atitiktų Python ir .NET pavyzdžius tame pačiame skyriuje
- **14-sampling/README.md**: Pataisyta rašybos klaida — pakeista `"Sampling is an davanced features"` į `"Sampling is an advanced feature"`

#### Mokymo plano atnaujinimai

**Pagrindinis README.md**
- Pridėtas įrašas 5.17 (Konkurencinis kelių agentų samprotavimas su MCP) mokymo plano lentelėje su tiesiogine nuoroda į naują pamoką

**05-AdvancedTopics/README.md**
- Pridėtas 5.17 pamokos eilutė prie pamokų lentelės

**study_guide.md**
- Pridėta Konkurencinio kelių agentų samprotavimo tema prie proto žemėlapio ir prozos aprašymo apie Išplėstinius dalykus

#### Kodo ir saugumo pataisymai

**Modulis 05 - Konkurencingi agentai (`mcp-adversarial-agents`)**
- **Saugumo taisymas — komandų injekcija**: Pakeista `execSync` “shell” interpolacija į `execFile` + `promisify` TypeScript `run_python` įrankyje, pašalinant komandų injekcijos paviršių (dabar LLM valdomas kodas perduodamas kaip tiesioginis argv elementas be shell įsikišimo)
- **MCP įrankių ciklo sujungimas**: Atnaujintas Python diskusijų organizatorius naudoti `AsyncAnthropic` klientą (pakeitė blokuojantį sinchroninį `Anthropic`), perduoti tiesioginį „ClientSession“ kiekvienam agento ratui, gauti įrankių apibrėžimus per `session.list_tools()` kiekvieną kartą ir siųsti `tool_use` blokus per `session.call_tool()` cikle, kol modelis sugeneruoja galutinį teksto atsakymą

#### Priklausomybių atnaujinimai

- Pakeltas `hono` iki 4.12.12 daugelyje paketų (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Pakeltas `@hono/node-server` nuo 1.19.11 iki 1.19.13 TypeScript paketuose
- Pakelta `cryptography` nuo 46.0.5 iki 46.0.7 Python paketuose (10-StreamliningAIWorkflows laboratorijose 3 ir 4)
- Pakeltas `lodash` nuo 4.17.23 iki 4.18.1 10-StreamliningAIWorkflows inspektoriuje

#### Vertimai

- Sinchronizuoti vertimai į daugiau nei 48 kalbas su naujausiais šaltinio pakeitimais (i18n atnaujinimas)

---

## 2026 m. vasario 5 d.

### Saugyklos validacijos ir navigacijos patobulinimai

#### Pridėta naujo mokymosi turinio

**Modulis 03 - Pradžia**
- **12-mcp-hosts/README.md**: Naujas išsamus vadovas MCP šeimininkų nustatymui
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigūracijos pavyzdžiai
  - JSON konfigūracijos šablonai visiems pagrindiniams šeimininkams
  - Transporto tipų palyginimo lentelė (stdio, SSE/HTTP, WebSocket)
  - Dažniausiai pasitaikančių prisijungimo problemų sprendimas
  - Saugaus šeimininkų konfigūravimo geriausios praktikos

- **13-mcp-inspector/README.md**: Naujas MCP inspektoriaus derinimo vadovas
  - Įdiegimo būdai (npx, npm global, iš šaltinio)
  - Prisijungimas prie serverių per stdio ir HTTP/SSE
  - Įrankių, išteklių ir raginimų darbo eiga testavimas
  - VS Code integracija su MCP inspektoriumi
  - Dažniausios derinimo situacijos su sprendimais

**Modulis 04 - Praktinė įgyvendinimas**
- **pagination/README.md**: Naujas puslapiavimo įgyvendinimo vadovas
  - Sužymėtas puslapiavimas Python, TypeScript, Java kalbomis
  - Kliento pusės puslapiavimo tvarkymas
  - Sužymėtojo dizaino strategijos (nepermatomas prieš struktūruotą)
  - Veiklos optimizavimo rekomendacijos

**Modulis 05 - Išplėstiniai dalykai**
- **mcp-protocol-features/README.md**: Naujas protokolo funkcijų gilinimasis
  - Progreso pranešimų įgyvendinimas
  - Užklausų atšaukimo modeliai
  - Ištekliai šablonai su URI šablonais
  - Serverio gyvavimo ciklo valdymas
  - Žurnalo lygio kontrolė
  - Klaidų apdorojimo modeliai su JSON-RPC kodais

#### Navigacijos pataisymai (atnaujinta daugiau nei 24 failai)

**Pagrindinių modulių README failai**
 Dabar nuorodos į pirmą pamoką IR kitą modulį

**02-Security pagalbiniai failai**
- Visi 5 papildomi saugumo dokumentai dabar turi „Kas toliau“ navigaciją:

**09-CaseStudy failai**
- Visi atvejo studijų failai dabar turi sekamą navigaciją:

**10-StreamliningAI laboratorijos**
Pridėta „Kas toliau“ skyrius Modulio 10 apžvalgoje ir Modulyje 11

#### Kodo ir turinio pataisymai

**SDK ir priklausomybių atnaujinimai**
Ištaisyta tuščia openai versija į `^4.95.0`
Atnaujintas SDK nuo `^1.8.0` iki `>=1.26.0`
Atnaujinti mcp versijų ribojimai iki `>=1.26.0`

**Kodo pataisymai**
Ištaisyta neteisinga modelio „gpt-4o-mini“ į „gpt-4.1-mini“

**Turinio pataisymai**
Ištaisyta sugedusi nuoroda `READMEmd` → `README.md`, pataisytas mokymo plano antraštės „Module 1-3“ į „Module 0-3“, pataisytas rašybos jautrus kelias
Pašalintas sugadintas pasikartojantis 5-os atvejo studijos turinys

**Pradedančiųjų gairių patobulinimai**
Pridėta tinkama įžanga, mokymosi tikslai ir išankstiniai reikalavimai pradedantiesiems

#### Mokymosi plano atnaujinimai

**Pagrindinis README.md**
- Pridėti įrašai 3.12 (MCP šeimininkai), 3.13 (MCP inspektorius), 4.1 (puslapiavimas), 5.16 (protokolo funkcijos) mokymo plano lentelėje

**Modulių README failai**
Pridėtos 12 ir 13 pamokos į pamokų sąrašą
Pridėta praktinių vadovų skiltis su puslapiavimo nuoroda
Pridėtos pamokos 5.15 (Pasirinktinis transportas) ir 5.16 (protokolo funkcijos)

**study_guide.md**
- Atnaujintas proto žemėlapis su visomis naujomis temomis: MCP šeimininkų nustatymas, MCP inspektorius, puslapiavimo strategijos, gilus protokolo funkcijų apžvalga

## 2026 m. sausio 28 d.

### MCP specifikacijos 2025-11-25 atitikties peržiūra

#### Pagrindinių koncepcijų patobulinimas (01-CoreConcepts/)
- **Naujas kliento pradinys – Roots**: Pridėta išsami dokumentacija apie Roots kliento pradinį objektą, leidžiantiems serveriams suprasti failų sistemos ribas ir prieigos teises
- **Įrankių anotacijos**: Pridėta dokumentacija apie įrankių elgsenos anotacijas (`readOnlyHint`, `destructiveHint`), geresniam įrankių vykdymo sprendimui
- **Įrankių kvietimas per Sampling**: Atnaujinta Sampling dokumentacija pridėjus `tools` ir `toolChoice` parametrus modelio valdomam įrankių kvietimui per Sampling užklausas
- **URL režimo generavimas**: Pridėta dokumentacija apie URL pagrindu inicijuotą iškvietimą serverio pradėtoms išorinėms žiniatinklio sąveikoms
- **Užduotys (eksperimentinė)**: Pridėtas naujas skyrius apie eksperimentinę Užduočių funkciją, skirtą patvariems vykdymo apvalkalams ir vėluotiniam rezultatų gavimui
- **Piktogramos palaikymas**: Pažymėta, kad įrankiai, ištekliai, išteklių šablonai ir raginimai dabar gali turėti piktogramas kaip papildomą metaduomenį

#### Dokumentacijos atnaujinimai
- **README.md**: Pridėta MCP specifikacijos 2025-11-25 versijos nuoroda ir datos pagrindu versijos valdymo paaiškinimas
- **study_guide.md**: Atnaujintas mokymo plano žemėlapis, įtraukiant Užduotis ir Įrankių anotacijas į Pagrindinių koncepcijų skyrių; atnaujintas dokumento laiko žymeklis

#### Specifikacijos atitikties patvirtinimas
- **Protokolo versija**: Patvirtinta, kad visa dokumentacija atitinka dabartinę MCP specifikaciją 2025-11-25
- **Architektūros suderinamumas**: Patvirtinta, kad dviejų sluoksnių architektūros (Duomenų sluoksnis + Transporto sluoksnis) dokumentacija yra tiksli
- **Pradinių objektų dokumentacija**: Patvirtinta serverio pradinių objektų (Ištekliai, Raginimai, Įrankiai) ir kliento pradinių objektų (Sampling, Elicitation, Logging, Roots) dokumentacija
- **Transporto mechanizmai**: Patvirtinta, kad STDIO ir Streamable HTTP transporto dokumentacija yra tiksli
- **Saugumo gairės**: Patvirtinta, kad atitinka dabartines MCP saugumo geriausias praktikas

#### Pagrindinės MCP 2025-11-25 funkcijos dokumentuotos
- **OpenID Connect atradimas**: Autentifikacijos serverio atradimas per OIDC
- **OAuth kliento ID metaduomenų dokumentai**: Rekomenduojamas kliento registracijos mechanizmas
- **JSON Schema 2020-12**: Numatytoji MCP schemų apibrėžimų kalba
- **SDK sluoksniavimo sistema**: Formalizuoti reikalavimai SDK funkcijų palaikymui ir priežiūrai
- **Valdymo struktūra**: Formalizuotos MCP valdymo darbo grupės ir interesų grupės

### Saugumo dokumentacijos didelis atnaujinimas (02-Security/)

#### MCP saugumo aukščiausio lygio sesijos (Sherpa) integracija
- **Naujas praktinis mokymo išteklius**: Pridėta išsami integracija su [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) visoje saugumo dokumentacijoje
- **Ekspedicijos maršruto aprašymas**: Dokumentuota pilna stovyklos nuo bazinės stovyklos iki viršūnės pažanga
- **OWASP atitikimas**: Visa saugumo informacija dabar susieta su OWASP MCP Azure Security Guide rizikomis

#### OWASP MCP Top 10 integracija
- **Naujas skyrius**: Pridėta OWASP MCP Top 10 saugumo rizikų lentelė su Azure sprendimais pagrindiniame Saugumo README faile
- **Rizikomis grįsta dokumentacija**: Atnaujintas mcp-security-controls-2025.md su OWASP MCP rizikų nuorodomis kiekvienam saugumo sričiai
- **Referencinė architektūra**: Nuoroda į OWASP MCP Azure Security Guide referencinę architektūrą ir įgyvendinimo modelius

#### Atnaujinti saugumo failai
- **README.md**: Pridėta Sherpa sesijos apžvalga, ekspedicijos maršruto lentelė, OWASP MCP Top 10 rizikų santrauka ir praktinių mokymų skyrius
- **mcp-security-controls-2025.md**: Atnaujinta antraštė vasariui 2026 m., pridėtos OWASP rizikų nuorodos (MCP01-MCP08), ištaisyta specifikacijos versijos neatitikimo klaida
- **mcp-security-best-practices-2025.md**: Pridėta Sherpa ir OWASP išteklių skiltis, atnaujintas laiko žymeklis
- **mcp-best-practices.md**: Pridėtas praktinių mokymų skyrius su Sherpa ir OWASP saitais
- **azure-content-safety-implementation.md**: Pridėtas OWASP MCP06 nuoroda, suderinimas su Sherpa 3 stovykla ir papildomi ištekliai

#### Pridėtos naujos išteklių nuorodos
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure saugumo vadovas](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individualūs OWASP MCP rizikos puslapiai (MCP01-MCP10)

### Mokymo programos MCP specifikacijos suderinimas 2025-11-25

#### Modulis 03 - Pradžia
- **SDK dokumentacija**: Įtrauktas Go SDK į oficialų SDK sąrašą; atnaujinti visi SDK nuorodos, suderinant su MCP specifikacija 2025-11-25
- **Transporto paaiškinimas**: Atnaujintos STDIO ir HTTP srautinio perdavimo aprašymai su aiškiomis nuorodomis į specifikaciją

#### Modulis 04 - Praktinė įgyvendinimo dalis
- **SDK atnaujinimai**: Įtrauktas Go SDK; atnaujintas SDK sąrašas su specifikacijos versijos nuoroda
- **Autorizacijos specifikacija**: Atnaujinta MCP autorizacijos specifikacijos nuoroda į dabartinę 2025-11-25 versiją

#### Modulis 05 - Pažangios temos
- **Naujos funkcijos**: Įrašyta pastaba apie naujas MCP specifikacijos 2025-11-25 funkcijas (Užduotys, Įrankių anotacijos, URL režimo išgavimas, Šaknys)
- **Saugumo ištekliai**: Pridėtos OWASP MCP Top 10 ir Sherpa dirbtuvės kaip papildomos nuorodos

#### Modulis 06 - Bendruomenės indėliai
- **SDK sąrašas**: Pridėti Swift ir Rust SDK; atnaujinta specifikacijos nuoroda į 2025-11-25
- **Specifikacijos nuoroda**: Atnaujinta MCP specifikacijos nuoroda į tiesioginę specifikacijos URL

#### Modulis 07 - Pamokos iš ankstyvosios diegimo praktikos
- **Išteklių atnaujinimai**: Pridėta MCP specifikacijos 2025-11-25 nuoroda ir OWASP MCP Top 10 kaip papildomi ištekliai

#### Modulis 08 - Geriausios praktikos
- **Specifikacijos versija**: Atnaujinta MCP specifikacijos nuoroda į 2025-11-25
- **Saugumo ištekliai**: Pridėta OWASP MCP Top 10 ir Sherpa dirbtuvės kaip papildomos nuorodos

#### Modulis 10 - AI darbo procesų supaprastinimas
- **Ženklo atnaujinimas**: Pakeistas MCP versijos ženkliukas nuo SDK versijos (1.9.3) į specifikacijos versiją (2025-11-25)
- **Išteklių nuorodos**: Atnaujinta MCP specifikacijos nuoroda; pridėta OWASP MCP Top 10

#### Modulis 11 - MCP serverio praktinės laboratorijos
- **Specifikacijos nuoroda**: Atnaujinta MCP specifikacijos nuoroda į 2025-11-25 versiją
- **Saugumo ištekliai**: Pridėta OWASP MCP Top 10 į oficialius išteklius

## 2025 m. gruodžio 18 d.

### Saugumo dokumentacijos atnaujinimas - MCP specifikacija 2025-11-25

#### MCP saugumo gerosios praktikos (02-Security/mcp-best-practices.md) - specifikacijos versijos atnaujinimas
- **Protokolo versijos atnaujinimas**: Atnaujinta nuoroda į naujausią MCP specifikaciją 2025-11-25 (išleista 2025 m. lapkričio 25 d.)
  - Visos specifikacijos versijos nuorodos atnaujintos nuo 2025-06-18 iki 2025-11-25
  - Dokumento datos nuorodos atnaujintos nuo 2025 m. rugpjūčio 18 d. iki 2025 m. gruodžio 18 d.
  - Patikrinta, kad visos specifikacijos URL nuorodos rodo į dabartinę dokumentaciją
- **Turinio patikra**: Išsami saugumo gerųjų praktikų patikra pagal naujausius standartus
  - **Microsoft saugumo sprendimai**: Patvirtinta dabartinė terminologija ir nuorodos į Prompt Shields (anksčiau "Jailbreak rizikos aptikimas"), Azure turinio saugą, Microsoft Entra ID ir Azure Key Vault
  - **OAuth 2.1 saugumas**: Patvirtintas suderinamumas su naujausiomis OAuth saugumo gerosiomis praktikomis
  - **OWASP standartai**: Patikrinta, kad OWASP Top 10 LLM nuorodos tebėra aktualios
  - **Azure paslaugos**: Patikrintos visos Microsoft Azure dokumentacijos nuorodos ir gerosios praktikos
- **Standartų atitikimas**: Patvirtinta, kad visi saugumo standartai yra dabartiniai
  - NIST AI rizikos valdymo sistema
  - ISO 27001:2022
  - OAuth 2.1 saugumo gerosios praktikos
  - Azure saugumo ir atitikties pagrindai
- **Įgyvendinimo ištekliai**: Patikrintos visos diegimo vadovų nuorodos ir ištekliai
  - Azure API valdymo autentifikacijos modeliai
  - Microsoft Entra ID integracijos vadovai
  - Azure Key Vault slaptųjų raktų valdymas
  - DevSecOps pipeline'ai ir stebėjimo sprendimai

### Dokumentacijos kokybės užtikrinimas
- **Specifikacijos atitikimas**: Užtikrinta, kad visi privalomi MCP saugumo reikalavimai (MUST/MUST NOT) atitinka naujausią specifikaciją
- **Išteklių aktualumas**: Patikrintos visos išorinės nuorodos į Microsoft dokumentaciją, saugumo standartus bei diegimo vadovus
- **Geriausios praktikos aprėptis**: Patvirtinta išsami autentifikacijos, autorizacijos, AI specifinių grėsmių, tiekimo grandinės saugumo ir įmonių modelių aprėptis

## 2025 m. spalio 6 d.

### Pradžios skyriaus išplėtimas – pažangus serverio naudojimas ir paprasta autentifikacija

#### Pažangus serverio naudojimas (03-GettingStarted/10-advanced)
- **Įtrauktas naujas skyrius**: Išsamus vadovas apie pažangų MCP serverio naudojimą, apimantis tiek standartinę, tiek žemo lygio serverio architektūrą.
  - **Standartinis vs žemo lygio serveris**: Išsamus palyginimas su pavyzdžiais Python ir TypeScript kalbomis abiem atvejais.
  - **Handlerių pagrindu sukurta dizaino schema**: Paaiškinimas apie įrankių/išteklių/ekranų valdymą, leidžiantį kurti lankstesnius, masteliuojamus serverio sprendimus.
  - **Praktiniai modeliai**: Realių scenarijų pavyzdžiai, kur žemo lygio serverio modeliai praverčia pažangioms funkcijoms ir architektūrai.

#### Paprasta autentifikacija (03-GettingStarted/11-simple-auth)
- **Įtrauktas naujas skyrius**: Žingsnis po žingsnio vadovas paprastos autentifikacijos įgyvendinimui MCP serveriuose.
  - **Autentifikacijos sąvokos**: Aiškus paaiškinimas apie autentifikaciją vs autorizaciją bei kredencialų valdymą.
  - **Paprastos autentifikacijos įgyvendinimas**: Middleware tipo autentifikacijos modeliai Python (Starlette) ir TypeScript (Express) kalbomis su kodo pavyzdžiais.
  - **Perėjimas prie pažangaus saugumo**: Nurodymai, kaip pradėti nuo paprastos autentifikacijos ir pažengti iki OAuth 2.1 bei RBAC su nuorodomis į pažangius saugumo modulius.

Šie papildymai suteikia praktinių, tiesioginės veiklos gairių kuriant stabilesnius, saugesnius ir lankstesnius MCP serverių sprendimus, jungiant pagrindines sąvokas su pažangiais gamybos modeliais.

## 2025 m. rugsėjo 29 d.

### MCP serverio duomenų bazės integracijos laboratorijos - išsamus praktinis mokymosi kelias

#### 11-MCPServerHandsOnLabs - nauja išsami duomenų bazės integracijos mokymo programa
- **Išsamus 13 laboratorijų mokymo kelias**: Pridėta pilna praktinė mokymo programa MCP serverių kūrimui su PostgreSQL duomenų bazės integracija
  - **Realaus pasaulio įgyvendinimas**: Zava Retail analizės atvejis, demonstruojantis įmonių lygio modelius
  - **Struktūrizuotas mokymosi progresas**:
    - **Laboratorijos 00-03: Pagrindai** – Įvadas, pagrindinė architektūra, saugumas ir daugelio nuomininkų palaikymas, aplinkos paruošimas
    - **Laboratorijos 04-06: MCP serverio kūrimas** – duomenų bazės dizainas ir schema, MCP serverio įgyvendinimas, įrankių plėtra
    - **Laboratorijos 07-09: Pažangios funkcijos** – semantinės paieškos integracija, testavimas ir derinimas, VS Code integracija
    - **Laboratorijos 10-12: Gamyba ir gerosios praktikos** – įdiegimo strategijos, stebėjimas ir stebėjimo sistema, gerosios praktikos ir optimizavimas
  - **Įmonių technologijos**: FastMCP karkasas, PostgreSQL su pgvector, Azure OpenAI embedingai, Azure Container Apps, Application Insights
  - **Pažangios funkcijos**: eilutės lygio saugumas (RLS), semantinė paieška, daugiapartinė duomenų prieiga, vektoriniai embedingai, realaus laiko stebėjimas

#### Terminologijos standartizavimas - modulio į laboratoriją konvertavimas
- **Išsamus dokumentacijos atnaujinimas**: Sistemingai atnaujinti visi README failai 11-MCPServerHandsOnLabs, naudojant terminą „Laboratorija“ vietoje „Modulis“
  - **Skyriaus antraštės**: Pakeista „What This Module Covers“ į „What This Lab Covers“ visose 13 laboratorijų
  - **Turinio aprašymas**: Pakeista „This module provides...“ į „This lab provides...“ visoje dokumentacijoje
  - **Mokymosi tikslai**: Pakeista „By the end of this module...“ į „By the end of this lab...“
  - **Navigacijos nuorodos**: Visos „Module XX:“ nuorodos pakeistos į „Lab XX:“ kryžminėse nuorodose ir navigacijoje
  - **Atlikimo sekimo atnaujinimai**: Pakeista „After completing this module...“ į „After completing this lab...“
  - **Išsaugotos techninės nuorodos**: Išlaikyti Python modulių pavadinimai konfigūracijos failuose (pvz., `"module": "mcp_server.main"`)

#### Studijų vadovo patobulinimai (study_guide.md)
- **Vizualinė mokymo programos schema**: Pridėtas naujas „11. Database Integration Labs“ skyrius su išsamiu laboratorijų struktūros vaizdavimu
- **Saugyklos struktūra**: Atnaujinta iš dešimties į vienuolika pagrindinių skyrių su išsamiu aprašymu 11-MCPServerHandsOnLabs
- **Mokymosi kelio gaires**: Patobulinti navigacijos nurodymai aprėpiant skyrius 00-11
- **Technologijų apžvalga**: Pridėti FastMCP, PostgreSQL, Azure paslaugų integracijos detalės
- **Mokymosi rezultatai**: Pabrėžtas gamybos lygiu veikiantys serverio kūrimo modeliai, duomenų bazės integracija ir įmonių sauga

#### Pagrindinio README struktūros patobulinimai
- **Laboratorijomis pagrįsta terminologija**: Pagrindinis README.md faile 11-MCPServerHandsOnLabs nuosekliai naudotas „Laboratorijos“ terminų žymėjimas
- **Mokymosi kelio organizavimas**: Aiškus progresas nuo pagrindinių sąvokų iki pažangos įgyvendinimo ir gamybinio diegimo
- **Realaus pasaulio fokusuotas**: Akcentas praktiniam, rankomis atliekamam mokymuisi naudojant įmonių lygio modelius ir technologijas

### Dokumentacijos kokybės ir nuoseklumo gerinimas
- **Praktinio mokymosi akcentas**: Stiprinamas praktinis, laboratorijomis pagrįstas požiūris visoje dokumentacijoje
- **Įmonių modelių fokusas**: Pabrėžti gamybos lygio įgyvendinimai ir įmonių saugumo svarstymai
- **Technologijų integracija**: Išsami modernių Azure paslaugų ir AI integracijos modelių aprėptis
- **Mokymosi progresas**: Aiškus, struktūrizuotas kelias nuo pagrindinių sąvokų iki gamybinio taikymo

## 2025 m. rugsėjo 26 d.

### Atvejų studijų plėtra - GitHub MCP registracijos integracija

#### Atvejų studijos (09-CaseStudy/) - ekosistemos vystymo fokusas
- **README.md**: Didelis išplėtimas su išsamiu GitHub MCP registracijos atvejo studija
  - **GitHub MCP registracijos atvejo studija**: Nauja išsami atvejo studija nagrinėjanti GitHub MCP registracijos paleidimą 2025 m. rugsėjį
    - **Problemos analizė**: Išsamus MCP serverių atradimo ir diegimo iššūkių nagrinėjimas
    - **Sprendimo architektūra**: GitHub centralizuoto registro metodas su vieno paspaudimo VS Code diegimu
    - **Verslo poveikis**: Matomi tobulėjimai programuotojų įvedimo ir produktyvumo srityse
    - **Strateginė vertė**: Modulinio agentų diegimo ir įrankių tarpusavio veikimo fokusas
    - **Ekosistemos vystymas**: Pozicionavimas kaip pagrindinė agentinių sistemų įdiegimo platforma
  - **Patobulinta atvejo studijų struktūra**: Visų septynių atvejo studijų atnaujinimas su nuoseklia forma ir išsamiu aprašymu
    - Azure AI kelionių agentai: daugiaagentų orkestravimo akcentas
    - Azure DevOps integracija: darbo srautų automatizavimo fokusas
    - Realaus laiko dokumentų gavimas: Python konsolės kliento įgyvendinimas
    - Interaktyvus mokymosi plano generatorius: Chainlit pokalbių interneto programa
    - Dokumentacija redaktoriuje: VS Code ir GitHub Copilot integracija
    - Azure API valdymas: įmonės API integracijos modeliai
    - GitHub MCP registracija: ekosistemos vystymas ir bendruomenės platforma
  - **Išsamūs išvados**: Perrašyta išvadų dalis, apimanti septynias atvejo studijas įvairiose MCP įgyvendinimo srityse
    - Įmonių integracija, daugiaagentų orkestravimas, programuotojų produktyvumas
    - Ekosistemos vystymas, švietimo programų klasifikacija
    - Pagerintos įžvalgos apie architektūrinius modelius, įgyvendinimo strategijas ir gerąją praktiką
    - Pabrėžtas MCP kaip brandus, gamybai tinkamas protokolas

#### Studijų vadovo atnaujinimai (study_guide.md)
- **Vizualinė mokymo programos schema**: Atnaujintas smegenų žemėlapis, įtraukiant GitHub MCP registraciją į atvejo studijų skyrių
- **Atvejo studijų aprašymas**: Išplėstas nuo bendrų aprašymų iki detalaus septynių išsamių atvejo studijų skaidymo
- **Saugyklos struktūra**: Atnaujintas skyrius 10, atspindintis išsamią atvejo studijų apimtį su konkrečiomis įgyvendinimo detalėmis
- **Pokyčių žurnalo integracija**: Pridėta 2025 m. rugsėjo 26 d. įrašo, dokumentuojančio GitHub MCP registracijos pridėjimą ir atvejo studijų patobulinimus
- **Datos atnaujinimai**: Atnaujintas puslapio apačios laiko žymeklis, atspindintis naujausią peržiūrą (2025 m. rugsėjo 26 d.)

### Dokumentacijos kokybės patobulinimai
- **Nuoseklumo gerinimas**: Standartizuotas atvejo studijų formatas ir struktūra visuose septyniuose pavyzdžiuose
- **Išsamus aprėpimas**: Atvejo studijos apima įmonių, programuotojų produktyvumo ir ekosistemos vystymo scenarijus
- **Strateginis pozicionavimas**: Patobulintas fokusas į MCP kaip pagrindinę agentinių sistemų diegimo platformą
- **Išteklių integracija**: Atnaujinti papildomi ištekliai, įtraukiant GitHub MCP registracijos nuorodą

## 2025 m. rugsėjo 15 d.

### Pažangių temų išplėtimas - individualūs transportai ir konteksto inžinerija

#### MCP individualūs transportai (05-AdvancedTopics/mcp-transport/) - naujas pažangus įgyvendinimo vadovas
- **README.md**: Pilnas natyralus MCP individualių transportų mechanizmų įgyvendinimo vadovas
  - **Azure Event Grid transportas**: Išsamus serverless įvykių pagrindu veikiantis transporto įgyvendinimas
    - Pavyzdžiai C#, TypeScript ir Python kalbomis su Azure Functions integracija
    - Įvykių valdomos architektūros modeliai mastelio MCP sprendimams
    - Webhook imtuvai ir žinučių transliavimas su push mechanizmu
  - **Azure Event Hubs transportas**: Didelio pralaidumo srautinio perdavimo įgyvendinimas
    - Realaus laiko srautai žemos delsos scenarijoms
    - Skirstymo strategijos ir kontrolinių taškų valdymas
    - Žinučių grupavimas ir našumo optimizavimas
  - **Įmonių integracijos modeliai**: Gamybai tinkami architektūriniai pavyzdžiai
    - Išskirtinė MCP apdorojimo paskirstymas keliuose Azure Functions
    - Hibridiniai transporto architektūros modeliai, jungiantys kelis transporto tipus
    - Žinučių patvarumo, patikimumo ir klaidų tvarkymo strategijos
  - **Saugumas ir stebėjimas**: Azure Key Vault integracija ir stebėjimo modeliai
    - Valdomo tapatumo autentifikavimas ir minimalus leidimų suteikimas
    - Application Insights telemetrija ir našumo stebėjimas
    - Grandinių pertraukikliai ir trikčių tolerancijos modeliai
  - **Testavimo karkasai**: Išsamios testavimo strategijos individualiems transportams
    - Vienetinis testavimas naudojant testinius dublius ir imituojančias sistemas
    - Integracijos testavimas su Azure Test Containers
    - Našumo ir apkrovos testavimo aspektai

#### Konteksto inžinerija (05-AdvancedTopics/mcp-contextengineering/) - nauja atsirandanti AI disciplina
- **README.md**: Išsamus konteksto inžinerijos kaip naujos srities tyrimas
  - **Pagrindiniai principai**: Viso konteksto dalijimasis, veiksmų sprendimų sąmoningumas ir konteksto lango valdymas

  - **MCP protokolo suderinamumas**: Kaip MCP dizainas sprendžia konteksto inžinerijos iššūkius
    - Konteksto lango apribojimai ir progresyvios įkėlimo strategijos
    - Reikšmingumo nustatymas ir dinaminis konteksto gavimas
    - Daugiakanalio konteksto valdymas ir saugumo svarstymai
  - **Įgyvendinimo būdai**: Viengubos gijos ir daugiaprieigos architektūros
    - Konteksto suskaidymo ir prioritetų nustatymo technikos
    - Progresyvus konteksto įkėlimas ir suspaudimo strategijos
    - Sluoksniuotos konteksto taikymo metodikos ir gavimo optimizavimas
  - **Matavimo sistema**: Nauji metrika konteksto efektyvumo vertinimui
    - Įvesties efektyvumas, našumas, kokybė ir vartotojo patirties aspektai
    - Eksperimentiniai konteksto optimizavimo metodai
    - Gedimų analizė ir tobulinimo metodologijos

#### Mokymo plano naršymo atnaujinimai (README.md)
- **Patobulinta modulių struktūra**: Atnaujinta mokymo plano lentelė įtraukiant naujas pažangias temas
  - Pridėti įrašai „Konteksto inžinerija“ (5.14) ir „Pasirinktinis perkėlimas“ (5.15)
  - Nuoseklus formatavimas ir naršymo nuorodos visuose moduliuose
  - Atnaujinti aprašymai, atitinkantys esamą turinio apimtį

### Katalogo struktūros patobulinimai
- **Pavadinimų standartizavimas**: Pervadintas „mcp transport“ į „mcp-transport“, kad atitiktų kitų pažangių temų aplankus
- **Turinio organizavimas**: Visi 05-AdvancedTopics aplankai dabar atitinka nuoseklų pavadinimų modelį (mcp-[tema])

### Dokumentacijos kokybės gerinimas
- **MCP specifikacijos atitikimas**: Visa nauja informacija nurodo dabartinę MCP specifikaciją 2025-06-18
- **Daugiakalbiai pavyzdžiai**: Išsamūs kodo pavyzdžiai C#, TypeScript ir Python kalbomis
- **Įmonių orientacija**: Gamybai paruošti šablonai ir Azure debesų integracija visur
- **Vizualinė dokumentacija**: Mermaid diagramos architektūros ir srauto vizualizacijai

## 2025 m. rugpjūčio 18 d.

### Išsamus dokumentacijos atnaujinimas – MCP 2025-06-18 standartai

#### MCP saugumo geriausios praktikos (02-Security/) – visiškas atnaujinimas
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Visiškai perrašyta, suderinta su MCP specifikacija 2025-06-18
  - **Privalomi reikalavimai**: Pridėti aiškūs MUST/MUST NOT reikalavimai iš oficialios specifikacijos su aiškiais vizualiniais ženklais
  - **12 pagrindinių saugumo praktikų**: Pertvarkyta iš 15 punktų sąrašo į išsamias saugumo sritis
    - Žetonų saugumas ir autentifikacija su išorinio identiteto tiekėjo integracija
    - Sesijų valdymas ir transporto saugumas su kriptografiniais reikalavimais
    - AI specifinė grėsmių apsauga su Microsoft Prompt Shields integracija
    - Prieigos kontrolė ir leidimai pagal mažiausio privilegijų principą
    - Turinys sauga ir stebėsena su Azure Content Safety integracija
    - Tiekimo grandinės saugumas su išsamia komponentų patikra
    - OAuth saugumas ir „Confused Deputy“ prevencija su PKCE įgyvendinimu
    - Incidentų valdymas ir atkūrimas su automatizuotomis funkcijomis
    - Atitiktis ir valdymas su reglamentine integracija
    - Pažangios saugumo priemonės su „zero trust“ architektūra
    - Microsoft saugumo ekosistemos integracija su visapusiškais sprendimais
    - Nuolatinis saugumo tobulėjimas su adaptuotomis praktikomis
  - **Microsoft saugumo sprendimai**: Patobulintos integravimo gairės Prompt Shields, Azure Content Safety, Entra ID ir GitHub Advanced Security
  - **Įgyvendinimo šaltiniai**: Kategorizuotos visapusiškos nuorodos pagal oficialią MCP dokumentaciją, Microsoft saugumo sprendimus, saugumo standartus ir įgyvendinimo vadovus

#### Pažangios saugumo priemonės (02-Security/) – verslo įgyvendinimas
- **MCP-SECURITY-CONTROLS-2025.md**: Visiškas pertvarkymas su verslo lygio saugumo sistema
  - **9 visapusiškos saugumo sritys**: Išplėsta nuo pagrindinių priemonių iki išsamios verslo sistemos
    - Pažangi autentifikacija ir autorizacija su Microsoft Entra ID integracija
    - Žetonų saugumas ir anti-praeinimo kontrolės su išsamia validacija
    - Sesijų saugumo priemonės su užgrobties prevencija
    - AI specifinės apsaugos priemonės nuo paklausų įdėjimo ir įrankių nuodus
    - Confused Deputy atakų prevencija su OAuth proxy saugumu
    - Įrankių vykdymo saugumas su izoliacija ir smėlio dėže
    - Tiekimo grandinės saugumo kontrolės su priklausomybių tikrinimu
    - Stebėsena ir aptikimo priemonės su SIEM integracija
    - Incidentų valdymas ir atkūrimas su automatizuotomis funkcijomis
  - **Įgyvendinimo pavyzdžiai**: Pridėti išsamūs YAML konfigūracijos blokai ir kodo pavyzdžiai
  - **Microsoft sprendimų integracija**: Visapusiškas Azure saugumo paslaugų, GitHub Advanced Security ir verslo identiteto valdymo aprėptis

#### Pažangios temos saugumas (05-AdvancedTopics/mcp-security/) – gamybai paruoštas įgyvendinimas
- **README.md**: Visiškai perrašyta verslo saugumo įgyvendinimui
  - **Dabartinė specifikacija**: Atnaujinta į MCP specifikaciją 2025-06-18 su privalomais saugumo reikalavimais
  - **Patobulinta autentifikacija**: Microsoft Entra ID integracija su išsamiais .NET ir Java Spring Security pavyzdžiais
  - **AI saugumo integracija**: Microsoft Prompt Shields ir Azure Content Safety įgyvendinimas su išsamiais Python pavyzdžiais
  - **Pažangi grėsmių šalinimo strategija**: Išsamūs įgyvendinimo pavyzdžiai
    - Confused Deputy atakų prevencija su PKCE ir vartotojo sutikimo validacija
    - Žetonų perleidimo prevencija su auditorijos validacija ir saugiu žetonų valdymu
    - Sesijų užgrobimo prevencija su kriptografiniu rišimu ir elgsenos analize
  - **Verslo saugumo integracija**: Azure Application Insights stebėjimas, grėsmių aptikimo dujotiekiai ir tiekimo grandinės saugumas
  - **Įgyvendinimo kontrolinis sąrašas**: Aiškūs privalomi ir rekomenduojami saugumo kontrolės su Microsoft saugumo ekosistemos privalumais

### Dokumentacijos kokybė ir standartų suderinamumas
- **Specifikacijų nuorodos**: Atnaujintos visos nuorodos į dabartinę MCP specifikaciją 2025-06-18
- **Microsoft saugumo ekosistema**: Pagerintos integravimo gairės visuose saugumo dokumentuose
- **Praktinis įgyvendinimas**: Pridėti išsamūs kodo pavyzdžiai .NET, Java ir Python su verslo šablonais
- **Ištekliai organizavimas**: Visapusiškas oficialios dokumentacijos, saugumo standartų ir įgyvendinimo vadovų kategorizavimas
- **Vizualiniai indikatoriai**: Aiškus privalomų reikalavimų ir rekomenduojamų praktikų žymėjimas


#### Pagrindinės koncepcijos (01-CoreConcepts/) – visiškas atnaujinimas
- **Protokolo versijos atnaujinimas**: Atnaujinta su nuoroda į dabartinę MCP specifikaciją 2025-06-18 su datos formatu (YYYY-MM-DD)
- **Architektūros tobulinimas**: Patobulinti topologijų, klientų ir serverių aprašymai, atitinkantys dabartinius MCP architektūros modelius
  - Tinkamai apibrėžti hostai kaip AI programos, koordinuojančios kelis MCP klientų ryšius
  - Klientai apibūdinami kaip protokolo jungtys, palaikančios vienas prie vieno serverio ryšius
  - Serveriai tobulinti su vietinio ir nuotolinio diegimo scenarijomis
- **Primitive pertvarkymas**: Visiškas serverių ir klientų primityvų perrašymas
  - Serverių primityvai: Resursai (duomenų šaltiniai), Užklausos (šablonai), Įrankiai (vykdomos funkcijos) su detaliomis paaiškinimų ir pavyzdžiais
  - Klientų primityvai: Atranka (LLM išbaigimai), Elicijavimas (vartotojo įvestis), Registravimas (debug/informacijos rinkimas)
  - Atnaujinti dabartiniai atradimo (`*/list`), gavimo (`*/get`) ir vykdymo (`*/call`) metodų modeliai
- **Protokolo architektūra**: Įvesta dviejų sluoksnių architektūros schema
  - Duomenų sluoksnis: JSON-RPC 2.0 pagrindas su gyvavimo ciklo valdymu ir primityvais
  - Transporto sluoksnis: STDIO (vietinis) ir Streamable HTTP su SSE (nuotolinis) transportavimo mechanizmai
- **Saugumo sistema**: Visapusiški saugumo principai, įskaitant aiškų vartotojo sutikimą, duomenų privatumą, įrankių vykdymo saugumą ir transporto sluoksnio apsaugą
- **Komunikacijos modeliai**: Atnaujinti protokolo pranešimai iniciavimo, atradimo, vykdymo ir pranešimų srautų parodymui
- **Kodo pavyzdžiai**: Atnaujinti daugakalbiai pavyzdžiai (.NET, Java, Python, JavaScript), atsižvelgiant į dabartinius MCP SDK modelius

#### Saugumas (02-Security/) – išsamus saugumo pertvarkymas  
- **Standartų suderinamumas**: Pilnas suderinamumas su MCP specifikacijos 2025-06-18 saugumo reikalavimais
- **Autentifikacijos evoliucija**: Dokumentuota pažanga nuo pasirinktinių OAuth serverių iki išorinio identiteto tiekėjo delegavimo (Microsoft Entra ID)
- **AI specifinės grėsmės analizė**: Apskrūplinta dabartinių AI atakų vektorių apimtis
  - Išsamios paklausų įdėjimo atakų scenarijos su realaus pasaulio pavyzdžiais
  - Įrankių apsinuodijimo mechanizmai ir „rug pull“ atakų modeliai
  - Konteksto lango užnuodijimas ir modelio painiojimų atakos
- **Microsoft AI saugumo sprendimai**: Visapusiškas Microsoft saugumo ekosistemos aprėptis
  - AI prompt apsauga su pažangia aptikimo, paryškinimo ir žymėjimo metodais
  - Azure Content Safety integracijos modeliai
  - GitHub Advanced Security tiekimo grandinės apsaugai
- **Pažangių grėsmių šalinimo priemonės**: Išsamios saugumo kontrolės skirtos
  - Sesijų užgrobimui MCP specifiniais atakų scenarijais ir kriptografiniais sesijos ID reikalavimais
  - „Confused Deputy“ problemos MCP proxy scenarijuose su aiškiais sutikimo reikalavimais
  - Žetonų perleidimo saugumo spragos su privaloma validacija
- **Tiekimo grandinės saugumas**: Išplėsta AI tiekimo grandinės aprėptis įskaitant pagrindinius modelius, įdiegimo paslaugas, konteksto tiekėjus ir trečiųjų šalių API
- **Pagrindinė sauga**: Patobulinta verslo saugumo šablonų integracija įskaitant „zero trust“ architektūrą ir Microsoft saugumo ekosistemą
- **Ištekliai organizavimas**: Kategorizuotos išsamios nuorodos pagal tipą (Oficiali dokumentacija, standartai, tyrimai, Microsoft sprendimai, įgyvendinimo vadovai)

### Dokumentacijos kokybės patobulinimai
- **Struktūruoti mokymosi tikslai**: Patobulinti mokymosi tikslai su konkrečiais, įgyvendinamais rezultatais
- **Kryžminės nuorodos**: Pridėtos nuorodos tarp susijusių saugumo ir pagrindinių koncepcijų temų
- **Dabartinė informacija**: Atnaujintos visos datos nuorodos ir specifikacijų saitai į dabartinius standartus
- **Įgyvendinimo gairės**: Pridėtos specifinės, įgyvendinamos gairės abiejose sekcijose

## 2025 m. liepos 16 d.

### README ir naršymo patobulinimai
- Visiškai pertvarkyta mokymo plano naršymo sistema README.md faile
- Pakeistas `<details>` žymes labiau prieinamais lentelės formatais
- Sukurtos alternatyvios išdėstymo parinktys naujame „alternative_layouts“ aplanke
- Pridėti kortelių, skirtukų ir akordeono stiliaus naršymo pavyzdžiai
- Atnaujinta saugyklos struktūros sekcija, apimanti visus naujausius failus
- Patobulinta „Kaip naudotis šiuo mokymo planu“ sekcija su aiškiomis rekomendacijomis
- Atnaujintos MCP specifikacijų nuorodos į teisingus URL
- Pridėta „Konteksto inžinerijos“ skiltis (5.14) į mokymo plano struktūrą

### Studijų vadovo atnaujinimai
- Visiškai pertvarkytas studijų vadovas, suderintas su dabartine saugyklos struktūra
- Pridėtos naujos skiltys MCP klientams ir įrankiams, bei populiariems MCP serveriams
- Atnaujinta vizualinė mokymo plano žemėlapis, tiksliai atspindinti visas temas
- Patobulinti pažangių temų aprašymai, apimantys visas specializuotas sritis
- Atnaujinta atvejų analizės skiltis atsižvelgiant į tikrus pavyzdžius
- Pridėtas šis išsamus pakeitimų žurnalas

### Bendruomenės indėliai (06-CommunityContributions/)
- Pridėta išsami informacija apie MCP serverius vaizdų generavimui
- Pridėta išsamus skirsnis apie Claude naudojimą VSCode aplinkoje
- Pridėta Cline terminalo kliento diegimo ir naudojimo instrukcijos
- Atnaujinta MCP klientų skiltis, apimanti visas populiarias klientų parinktis
- Patobulinti indėlių pavyzdžiai su tikslesniais kodo pavyzdžiais

### Pažangios Temos (05-AdvancedTopics/)
- Organizuoti visi specializuoti temų aplankai su nuosekliais pavadinimais
- Pridėta medžiaga ir pavyzdžiai konteksto inžinerijai
- Pridėta Foundry agento integracijos dokumentacija
- Patobulinta Entra ID saugumo integracijos dokumentacija

## 2025 m. birželio 11 d.

### Pradinis sukūrimas
- Išleista pirmoji MCP pradedančiųjų mokymo plano versija
- Sukurta pagrindinė struktūra visoms 10 pagrindinėms dalims
- Įgyvendintas vizualinis mokymo plano žemėlapis naršymui
- Pridėti pradinių pavyzdinių projektų keliomis programavimo kalbomis

### Pradžia (03-GettingStarted/)
- Sukurti pirmieji serverių įgyvendinimo pavyzdžiai
- Pridėtos kliento vystymo gairės
- Įtrauktas LLM kliento integravimo vadovas
- Pridėta VS Code integracijos dokumentacija
- Įgyvendinti Server-Sent Events (SSE) serverių pavyzdžiai

### Pagrindinės koncepcijos (01-CoreConcepts/)
- Pridėtas išsamus kliento-serverio architektūros paaiškinimas
- Sukurta dokumentacija apie pagrindines protokolo sudedamąsias dalis
- Dokumentuoti pranešimų modeliai MCP protokole

## 2025 m. gegužės 23 d.

### Saugyklos struktūra
- Inicijuota saugykla su pagrindine aplankų struktūra
- Sukurti README failai kiekvienai didžiausiai daliai
- Įdiegta vertimų infrastruktūra
- Pridėti paveikslėlių ištekliai ir diagramos

### Dokumentacija
- Sukurtas pirminis README.md su mokymo plano apžvalga
- Pridėti CODE_OF_CONDUCT.md ir SECURITY.md
- Nustatytas SUPPORT.md su pagalbos gavimo gairėmis
- Sukurta preliminari studijų vadovo struktūra

## 2025 m. balandžio 15 d.

### Planavimas ir sistema
- Pirminis MCP pradedančiųjų mokymo plano planavimas
- Apibrėžti mokymosi tikslai ir tikslinė auditorija
- Nustatyta 10 dalių mokymo plano struktūra
- Sukurta konceptuali sistema pavyzdžiams ir atvejų analizėms
- Sukurti pradinių pavyzdžių prototipai pagrindinėms koncepcijoms

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
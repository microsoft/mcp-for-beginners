# Ændringslog: MCP for Begyndere Pensum

Dette dokument tjener som en optegnelse over alle væsentlige ændringer foretaget i Model Context Protocol (MCP) for Begyndere pensum. Ændringer dokumenteres i omvendt kronologisk rækkefølge (nyeste ændringer først).

## 9. september 2026

### MCP 2026-07-28 Endelig Specifikationsjustering

Opdaterede det engelske pensum fra release-kandidat og `2025-11-25`
baseline-vejledning til den endelige MCP `2026-07-28` specifikation.

- **Opdateret**: Referencer til nuværende version, specifikationslinks, stateless
  anmodningsvejledning, `server/discover`, Streamable HTTP-headers og Tasks
  udvidelses livscyklus på tværs af 38 engelske dokumentationsfiler.
- **Korrigeret**: Elicitation bruger nu `elicitation/create`, Sampling bruger
  `sampling/createMessage`, og `InputRequiredResult.resultType` bruger
  `"input_required"`.
- **Udskiftet**: Den unøjagtige Root Context samtalestatus lektion med en
  protokol-korrekt Roots lektion, der dækker informationsfilsystem hints, den
  nuværende multi-round-trip flow, sikkerhedsgrænser og migrationsmuligheder.
- **Præciseret**: Roots, Sampling, Logging og Dynamic Client Registration er
  afskaffet i `2026-07-28`, med deres anbefalede erstatninger og tidligste
  fjernelsesdato dokumenteret.
- **Mærket**: Samples, der stadig er afhængige af MCP `2025-11-25`, HTTP+SSE,
  initialiserings-handshakes eller protokolsessioner, opretholdes som legacy
  kompatibilitetseksempler i stedet for at blive præsenteret som aktuelle implementeringer.
- **Sikkerhedsvejledning**: Opdaterede de selvstændige sikkerhedsguider til brug af
  autorisation pr. anmodning og eksplicitte application state handles i stedet for
  fjernede protokolsessions-ID'er. Client ID Metadata Dokumenter er nu den
  foretrukne registreringsvej, med DCR dokumenteret som kompatibilitets-only.
- **Støttemateriale**: Opdaterede studievejledning, bidragydercheckliste,
  Publora case study og APIM case study. APIM walkthrough anbefaler nu
  dets nuværende Streamable HTTP `/mcp` endpoint i stedet for afskaffede `/sse`.
- **Kanoniske links**: Udskiftede pensionerede og udkast til specifikations-URL'er i engelske
  kildemarkdown med versionerede `2026-07-28` links, samtidig med at eksplicitte
  links til legacy-versioner bevares, hvor et sample stadig er bundet til ældre værktøjer.
- **Stabile filnavne**: Omdøbte den endelige specifikationsguide og to sikkerhedsguider
  for at fjerne release-kandidat og årstals suffikser, og opdaterede derefter alle engelske
  hyperlinks til deres stabile stier.
- **Ny autorisationssample**: Tilføjede en testet
  [TypeScript MCP `2026-07-28` ressource-server](./02-Security/samples/cimd-dcr-auth/README.md)
  der sammenligner foretrukne Client ID Metadata Dokumenter med afskaffet Dynamic
  Client Registration fallback. Sample inkluderer RFC 9728 discovery, JWKS
  validering, per-værktøj scopes, tolv tests og en Auth0 setup walkthrough.
- **Oversættelsesomfang**: Kun engelske kildefiler blev redigeret; genererede
  oversættelser og oversatte billeder forbliver uændrede, da disse er autooversat.

## 29. juli 2026

### Ny Modul 08 Følgesvend: Reliability Sidecars og Sikker Genforsøg

Tilføjede en leverandør-neutral følgesvendlektion til MCP-værktøjer, der skaber reelle
effekter, tilpasset den endelige `2026-07-28` specifikation.

- **Ny**: [reliability sidecar følgesvend lektion][reliability-sidecar]
  bruger en support-ticket historie, to Mermaid diagrammer og en genforsøgsbeslutnings-
  flow for at forklare stabile operation keys, atomisk duplikatoptagelse,
  forsoning, beviser og Tasks udvidelsesgrænse.
- **Ny**: En standardbibliotek Python og SQLite failure-injection øvelse
  bruger separate operation og ticket lagre til at demonstrere et svar tabt
  efter en ekstern effekt er committet. Seks deterministiske tests dækker naive
  duplikationer, beskyttet genstart genopretning, payload konflikter, cachede resultater,
  aktive krav og samtidige duplikatoptagelser.
- **Opdateret**: Modul 08 linker nu til følgesvendlektion, identificerer den
  endelige `2026-07-28` stateless anmodningsmodel, skelner OpenTelemetry
  observability fra den afskaffede MCP logging funktion og begrænser sit
  generiske genforsøgs-eksempel til skrivebeskyttede operationer.
- **Valgfri**: Lektionen kortlægger sine bærbare koncepter til én tagget community
  implementering uden at gøre den hostede service eller et netværkskald til en del af
  øvelsen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. juli 2026

### Ny Lektion: MCP Specifikation Release Candidate 2026-07-28

Tilføjede dækning af den kommende `2026-07-28` MCP specifikation release kandidat (annonceret 21. maj 2026; endelig udgivelse planlagt til 28. juli 2026), opsummeret fra [officiel annonceringsblogindlæg](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Pensummets baseline forbliver **MCP Specifikation 2025-11-25** indtil den nye version udsendes, så dette præsenteres som fremadskuende vejledning og ikke en omskrivning af eksisterende lektioner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — en fuld lektion, der dækker den stateless protokolkerne (fjernelse af `initialize` handshake og `Mcp-Session-Id`), de nye `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` cache metadata, W3C Trace Context i `_meta`, det formelle Extensions framework (MCP Apps og den nye Tasks extension), seks autorisations-hærdende SEPs, afskaffelsen af Roots/Sampling/Logging, og overgangen til fuld JSON Schema 2020-12 for værktøjs-skemaer.
- **Opdateret** med fremadskuende henvisninger til den nye lektion:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolversionsnote, Sampling/Roots/Logging/Tasks sektioner, og "Hvad kommer næste"
  - [02-Security/README.md](./02-Security/README.md): autorisationshærdning henvisning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport henvisning
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling afskaffelses henvisning
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging afskaffelse og Tasks extension henvisning
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing henvisning
  - [README.md](./README.md): "Ser fremad" note i specifikationssektionen og en ny `1.1` indgang i pensummodultabellen
  - [study_guide.md](./study_guide.md): fremadskuende punkt under Core Concepts oversigt og en dateret tillægsmåde note
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): henvisning på `mcp-session-id` transportkort foran stateless anmodningsmodellen
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduloversigt henvisning på Root Contexts/Sampling afskaffelser og Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisationshærdning henvisning

## 24. juni 2026

### Ny Lektion: Brug af MCP i Copilot app

- [Tooling sektion](./12-tooling/README.md) Tilføjede tooling sektion.
- [MCP i Copilot app](./12-tooling/01-copilot-app/README.md)

## 16. juni 2026

### MCP Specifikationsjustering & Samplevalidering

Validerede pensum mod den nuværende **MCP Specifikation 2025-11-25** og de nyeste officielle SDK'er, derefter korrigerede de resterende forældede specifikationsreferencer og bekræftede, at kernesamples stadig bygges og kører.

#### Specifikationsversionskorrektioner (2025-06-18 / 2025-03-26 → 2025-11-25)

Opdaterede engelsk indhold, hvor det stadig påstod, at en ældre spec revision var den *nuværende/sidste* standard, og pegede links til de kanoniske `modelcontextprotocol.io` spec stier:
- **05-AdvancedTopics/mcp-security/README.md**: Opdaterede "Nuværende Standard" banner, introduktion, kerne sikkerhedsprincipper overskrift, obligatoriske krav overskrift, Microsoft Entra ID sektion, Referencer & Ressourcer links og afsluttende sikkerhedsmeddelelse (8 referencer) til 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Opdaterede den ekstra ressource specifikationslink og "Nuværende Standard" banner til 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Udskiftede det forældede `2025-03-26` sikkerheds- og tillidslink med den aktuelle 2025-11-25 sikkerhedspraksis side
- **03-GettingStarted/14-sampling/README.md**: Opdaterede det officielle sampling dokuments link til 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Opdaterede nutidens "nuværende MCP specifikation" reference og ekstra ressourcer specifikationslink til 2025-11-25 (historiske SSE-afskaffelsesnoter bevaret for nøjagtighed)

#### Samplevalidering mod nuværende SDK'er

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` løste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` bestod uden typefejl — eksisterende `McpServer`/`StdioServerTransport` API'er er stadig gyldige
- **Python (03-GettingStarted/01-first-server/solution/python)**: Valideret i isoleret `.venv` med `mcp[cli]` (1.27.2); `py_compile` bestod og `FastMCP.list_tools()` returnerede korrekt `add` og `subtract` værktøjerne
- Bekræftede, at alle sample `@modelcontextprotocol/sdk` versionsintervaller (`>=1.26.0` / `^1.26.0` / `^1.27.0`) løses rent til den nuværende `1.29.0` uden brud på API

#### Afhængigheds-pin-justering (lukker versionsgab)

Opdaterede forældede SDK pins, så hvert sample følger den aktuelle MCP-udgivelse, i overensstemmelse med repoets overordnede konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Opdaterede `@modelcontextprotocol/sdk` fra `^1.8.0` → `>=1.26.0` og opdaterede den forældede `"updated for MCP 2025-06-18"` pakke-beskrivelse til `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** og **lab4/code/github_mcp_server/pyproject.toml**: Opdaterede den præcise pin `mcp==1.23.0` → `mcp>=1.26.0`; regenererede begge `uv.lock` filer (`uv lock`), så lockfilerne løser til den nuværende `mcp 1.27.2` og forbliver synkroniserede med manifestene

#### Pensum Gap Analyse — Seneste Spec Funktionsdækning

Bekræftede, at pensum allerede dækker alle primitivt introducerede/udvidede i MCP 2025-11-25, så der ikke mangler indhold:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-tilstand)**: Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumenteret i 00-Introduction, 01-CoreConcepts og 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentelle, langvarige operationer)**: Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features

### Sikkerhedshærdning & Afhjælpning af Afhængighedssårbarheder

Kørte en fuld sikkerhedsgennemgang på tværs af alle afhængighedsmanifester og samplekildekode, og afhjælpede derefter alle rapporterede npm-advarsler og et kodniveau-fund. Efter afhjælpning rapporterer `npm audit` **0 sårbarheder** i hver revideret mappe.

#### npm Afhængighedssårbarheder (transitive) — Rettet

Reviderede alle 15 forpligtede `package-lock.json` filer. Sårbarheder var begrænset til transitive afhængigheder trukket ind af MCP Inspector udviklingsværktøj, OpenAI klienten og MCP SDK; alle er nu løst uden at bryde samples:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** og **lab3/code/weather_mcp/inspector**: Opgraderede `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), hvilket fjernede de bundtede advisories for `ajv`, `brace-expansion`, `diff`, `path-to-regexp` og `ws`. Tilføjet en npm `overrides` post, som tvinger den patched `shell-quote@1.8.4` for at eliminere den resterende kritiske advisory båret af `concurrently`; regenereret begge lockfiler (nu 0 sårbarheder)
- **03-GettingStarted/samples/typescript**: `npm audit fix` opdaterede den transitiv `qs` (moderat) til en patched version
- **03-GettingStarted/samples/javascript**: `npm audit fix` opdaterede den transitiv `hono` (moderat) til en patched version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` opdaterede den transitiv `form-data` (høj) til en patched version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genereret den manglende `package-lock.json`, så projektet er reproducerbart og auditerbart (0 sårbarheder)

#### Sikkerhedsrettelse på kode-niveau (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Fjernet `shell=True` fra `open_in_vscode` værktøjet. Den tidligere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillod shell metakarakterer i en mappesti at blive fortolket af `cmd.exe` (kommando-injektionsvektor). Den starter nu den resolvede `Code.exe` direkte med mappen som argument — uden shell — hvilket er funktionelt ækvivalent og sikkert

#### Python afhængighedsaudit

- Reviderede alle Python requirements sæt med `pip-audit`. `05-AdvancedTopics` og `03-GettingStarted/samples/python` rapporterede **ingen kendte sårbarheder** (deres `mcp` / `httpx` / `pydantic` / `python-dotenv` versioner peger på nuværende patched udgivelser)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` markerede den transitiv afhængighed **`werkzeug` 3.1.1** med tre `safe_join` Windows device-naam DoS advisories — `CVE-2025-66221`, `CVE-2026-21860` og `CVE-2026-27199` (alle rettet i 3.1.6). Tilføjet en eksplicit sikkerhedspinning `werkzeug>=3.1.6`, så patched udgivelsen bliver brugt; verificeret at betingelsen løser korrekt med `chainlit` / `mcp` / `semantic-kernel` stakken

### Produktnavn Genbranding

Opdateret alt undervisningsmateriale til at afspejle Microsofts produktgenbranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Opdateret Discord fællesskabslink
- **AGENTS.md**: Opdateret Discord server henvisning
- **README.md**: Opdateret teknologiøkosystem henvisninger
- **study_guide.md**: Opdateret case study henvisninger
- **05-AdvancedTopics/README.md**: Opdateret titel og beskrivelse for modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Opdateret sektion overskrift og beskrivelse
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Fuldt modul titel- og indholdsopdatering
- **05-AdvancedTopics/mcp-security-entra/README.md**: Opdateret kryds-reference link
- **07-LessonsfromEarlyAdoption/README.md**: Opdateret case study henvisninger
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Opdateret Sektion 9 overskrift, badges og funktioner
- **08-BestPractices/README.md**: Opdateret Discord fællesskabslink
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Opdateret Discord kanal henvisning
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Opdateret model deployment henvisning
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Opdateret AI Services tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Opdateret ressourcehenvisninger

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Opdateret hovedundervisningsreferencer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Opdateret modultitel, overblik og alle moduloverskrifter
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Opdateret titel, læringsmål, opsætningsinstruktioner og ressourcer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Opdateret titel, læringsmål, MCP hosts tabel og krydsreferencer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Opdateret titel, badges, forudsætninger og ressourcer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Opdateret Agent Builder referencer og feedback link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Opdateret forudsætninger og udvidelsesreferencer

---

## 11. april 2026

### Nyt modul, dokumentationsrettelser og afhængighedsopdateringer

#### Nyt kursusindhold tilføjet

**Modul 05 - Avancerede emner**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende guide om det adversarielle debatmønster for multi-agent systemer
  - Mermaid arkitekturskema: to agenter → delt MCP server → debattranskript → dommer → afgørelse
  - Delt MCP værktøjsserver (`web_search` + `run_python`) implementeret i Python og TypeScript
  - Modstridende systemprompter (FOR / IMOD / Dommer) med eksplicitte krav til værktøjsbrug
  - Debatorkestrator i Python, TypeScript og C# til at styre runder og rute argumenter
  - MCP `ClientSession` kobling til orkestratoren for reelle værktøjskald
  - Brugsscenarie tabel (hallucinationsdetektion, risikomodelering, API design review, faktatjek, teknisk valg)
  - Sikkerhedsovervejelser: sandboxet eksekvering, validering af værktøjskald, ratebegrænsning, revisionslogning
  - Struktureret øvelse med tre praktiske scenarier (kodegennemgang, arkitekturvalg, indholdsmoderering)

#### Dokumentationsrettelser

**Modul 03 - Kom godt i gang**
- **05-stdio-server/README.md**: Rettede ufuldstændigt TypeScript stdio-server eksempel — tilføjet manglende transport-initialisering (`new StdioServerTransport()`) og kald `server.connect(transport)` for at matche Python og .NET eksemplerne i samme sektion
- **14-sampling/README.md**: Rettede stavefejl — rettet `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kursusopdateringer

**Hoved README.md**
- Tilføjet post 5.17 (Adversarial Multi-Agent Reasoning with MCP) til kursustabel med direkte link til den nye lektion

**05-AdvancedTopics/README.md**
- Tilføjet lektion 5.17 række til lektionslisten

**study_guide.md**
- Tilføjet emnet Adversarial Multi-Agent Reasoning til mindmap og prose-beskrivelse af Avancerede emner

#### Kode- og sikkerhedsrettelser

**Modul 05 - Adversarielle agenter (`mcp-adversarial-agents`)**
- **Sikkerhedsrettelse — kommandoinjektion**: Udskiftede `execSync` shell interpolation med `execFile` + `promisify` i TypeScript `run_python` værktøjet, hvilket eliminerer kommandoinjektionsfladen (LLM-styret kode overføres nu som et litteralt argv-element uden indblanding af shell)
- **MCP værktøjsløkke kobling**: Opdaterede den Python-baserede debatorkestrator til at bruge `AsyncAnthropic` klient (udskiftede den blokerende sync `Anthropic`), indsende en live `ClientSession` direkte til hver agent-turn, hente værktøjsdefinitioner via `session.list_tools()` for hver turn, og udsende `tool_use` blokke via `session.call_tool()` i loop indtil modellen udsender et endeligt tekstsvar

#### Afhængighedsopdateringer

- Opgraderede `hono` til 4.12.12 i flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Opgraderede `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript pakker
- Opgraderede `cryptography` fra 46.0.5 til 46.0.7 i Python pakker (10-StreamliningAIWorkflows labs 3 og 4)
- Opgraderede `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Oversættelser

- Synkroniserede oversættelser til 48+ sprog med de seneste kildeændringer (i18n opdatering)

---

## 5. februar 2026

### Validering og navigationsforbedringer på tværs af repository

#### Nyt kursusindhold tilføjet

**Modul 03 - Kom godt i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide til opsætning af MCP hosts
  - Eksempler på konfigurationer for Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-konfigurationstemplater for alle større hosts
  - Sammenligningstabel for transporttyper (stdio, SSE/HTTP, WebSocket)
  - Problemløsning for almindelige forbindelsesfejl
  - Sikkerhedspraksis for host-konfiguration

- **13-mcp-inspector/README.md**: Ny fejlsøgningsguide til MCP Inspector
  - Installationsmetoder (npx, global npm, fra kildekode)
  - Forbindelse til servere via stdio og HTTP/SSE
  - Testværktøjer, ressourcer og prompt-workflows
  - VS Code integration med MCP Inspector
  - Almindelige fejlsøgningsscenarier med løsninger

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guide til pagineringimplementering
  - Cursor-baserede pagineringsmønstre i Python, TypeScript, Java
  - Klientside pagineringshåndtering
  - Cursor designstrategier (opaque vs. struktureret)
  - Anbefalinger til performanceoptimering

**Modul 05 - Avancerede emner**
- **mcp-protocol-features/README.md**: Ny dybdegående gennemgang af protokolfunktioner
  - Implementering af fremdriftsmeddelelser
  - Mønstre for anmodningsannullering
  - Ressourcetemplater med URI-mønstre
  - Serverlivscyklusstyring
  - Kontrol af logniveauer
  - Fejlhåndteringsmønstre med JSON-RPC koder

#### Navigationsrettelser (24+ filer opdaterede)

**Hovedmodul READMEs**
 Nu linker både til første lektion OG næste modul

**02-Security Underfiler**
- Alle 5 supplerende sikkerhedsdokumenter har nu "Hvad er næste?" navigation:

**09-CaseStudy Filer**
- Alle case study filer har nu sekventiel navigation:

**10-StreamliningAI Labs**
Tilføjet Hvad er næste? sektion til Modul 10 overblik og Modul 11

#### Kode- og indholdsrettelser

**SDK- og afhængighedsopdateringer**
Rettede tom openai-version til `^4.95.0`
Opdaterede SDK fra `^1.8.0` til `>=1.26.0`
Opdaterede mcp versionspins til `>=1.26.0`

**Kodefix**
Rettede ugyldig model `gpt-4o-mini` til `gpt-4.1-mini`

**Indholdsrettelser**
Rettede brudt link `READMEmd` → `README.md`, rettede kursushoved `Module 1-3` → `Module 0-3`, rettede case-sensitiv sti
Fjernede korrumperet dublet indhold af Case Study 5

**Forbedringer for begyndere**
Tilføjet korrekt introduktion, læringsmål og forudsætninger for begyndere

#### Kursusopdateringer

**Hoved README.md**
- Tilføjet poster 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) til kursustabel

**Modul READMEs**
Tilføjet lektioner 12 og 13 til lektionsliste
Tilføjet Praktiske guider sektion med pagineringslink
Tilføjet lektioner 5.15 (Custom Transport) og 5.16 (Protocol Features)

**study_guide.md**
- Opdateret mindmap med alle nye emner: MCP Hosts Opsætning, MCP Inspector, Pagineringsstrategier, Dybdegående Protokolfunktioner

## 28. jan 2026

### MCP Specifikation 2025-11-25 Overensstemmelsesgennemgang

#### Forbedring af kernekoncepter (01-CoreConcepts/)
- **Ny klientprimitiv - Roots**: Tilføjet omfattende dokumentation om Roots klientprimitiv, der gør det muligt for servere at forstå filsystemgrænser og adgangstilladelser
- **Værktøjsannotationer**: Tilføjet dokumentation om værktøjsadfærdsannotationer (`readOnlyHint`, `destructiveHint`) for bedre beslutningstagning ved værktøjsudførelse
- **Værktøjskald i sampling**: Opdateret samplingdokumentation til at inkludere `tools` og `toolChoice` parametre til modelstyrede værktøjskald under samplinganmodninger
- **URL Mode Elicitation**: Tilføjet dokumentation om URL-baseret elicitation for serverinitierede eksterne webinteraktioner
- **Tasks (Eksperimentelt)**: Tilføjet ny sektion, der dokumenterer den eksperimentelle Tasks-funktion til holdbare eksekverings-omslag og udsat resultatindhentning

- **Ikoner Understøttelse**: Bemærket at værktøjer, ressourcer, ressource-skabeloner og prompts nu kan inkludere ikoner som yderligere metadata

#### Dokumentationsopdateringer
- **README.md**: Tilføjet MCP Specifikation 2025-11-25 versionsreference og forklaring af datobaseret versionsstyring
- **study_guide.md**: Opdateret læseplan oversigt til at inkludere Opgaver og Værktøjsannotationer i Kernekoncepter sektionen; opdateret dokumentets tidsstempel

#### Overensstemmelsesverifikation af Specifikation
- **Protokolversion**: Bekræftet at al dokumentation refererer til den nuværende MCP Specifikation 2025-11-25
- **Arkitekturjustering**: Bekræftet nøjagtighed i dokumentationen af to-lags arkitektur (Datalag + Transportlag)
- **Primitiver Dokumentation**: Valideret serverprimitiver (Ressourcer, Prompts, Værktøjer) og klientprimitiver (Sampling, Fremkaldelse, Logning, Roots)
- **Transportmekanismer**: Bekræftet nøjagtighed af dokumentationen for STDIO og Streambar HTTP transport
- **Sikkerhedsanvisninger**: Bekræftet overensstemmelse med gældende MCP Sikkerhedspraksis dokumentation

#### Centrale MCP 2025-11-25 Funktioner Dokumenteret
- **OpenID Connect Discovery**: Auth server opdagelse gennem OIDC
- **OAuth Client ID Metadata Dokumenter**: Anbefalet klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skemadefinitioner
- **SDK Lagdelingssystem**: Formaliserede krav til SDK funktionalitetsunderstøttelse og vedligeholdelse
- **Governance Struktur**: Formaliserede arbejdsgrupper og interessegrupper i MCP styring

### Stor Sikkerhedsdokumentationsopdatering (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **Nyt Hands-On Træningsressource**: Tilføjet omfattende integration med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i hele sikkerhedsdokumentationen
- **Ekspedition Rute Dækning**: Dokumenteret hele camp-til-camp progressionen fra Base Camp til Summit
- **OWASP Justering**: Al sikkerhedsguidance map’er nu til OWASP MCP Azure Security Guide risici

#### OWASP MCP Top 10 Integration
- **Ny Sektion**: Tilføjet OWASP MCP Top 10 Sikkerhedsrisikotabel med Azure afbødninger til hovedsikkerheds-README
- **Risiko-Baseret Dokumentation**: Opdateret mcp-security-controls-2025.md med OWASP MCP risikoreferencer for hvert sikkerhedsområde
- **Reference Arkitektur**: Linket til OWASP MCP Azure Security Guide referencearkitektur og implementeringsmønstre

#### Opdaterede Sikkerhedsfiler
- **README.md**: Tilføjet Sherpa Workshop oversigt, ekspeditionsrutetabel, OWASP MCP Top 10 risikoresumé og hands-on træningssektion
- **mcp-security-controls-2025.md**: Opdateret header til februar 2026, tilføjet OWASP risikoreferencer (MCP01-MCP08), rettet versionsinkonsistens
- **mcp-security-best-practices-2025.md**: Tilføjet Sherpa og OWASP ressourcer sektion, opdateret tidsstempel
- **mcp-best-practices.md**: Tilføjet hands-on træningssektion med Sherpa og OWASP links
- **azure-content-safety-implementation.md**: Tilføjet OWASP MCP06 reference, Sherpa Camp 3 tilpasning, og yderligere ressourcer sektion

#### Nye Ressourcelinks Tilføjet
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Enkelte OWASP MCP risikosider (MCP01-MCP10)

### Læseplansomspændende MCP Specifikation 2025-11-25 Justering

#### Modul 03 - Kom Godt I Gang
- **SDK Dokumentation**: Tilføjet Go SDK til officielt SDK-overblik; opdateret alle SDK-referencer til at matche MCP Specifikation 2025-11-25
- **Transportafklaring**: Opdateret beskrivelser for STDIO og HTTP Streaming transport med eksplicitte specifikationsreferencer

#### Modul 04 - Praktisk Implementering
- **SDK Opdateringer**: Tilføjet Go SDK; opdateret SDK liste med specifikationsversionsreference
- **Autorisationsspecifikation**: Opdateret MCP Autorisationsspecifikation link til aktuelt 2025-11-25 version

#### Modul 05 - Avancerede Emner
- **Nye Funktioner**: Tilføjet note om nye MCP Specifikation 2025-11-25 funktioner (Opgaver, Værktøjsannotationer, URL Mode Fremkaldelse, Roots)
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop links til yderligere referencer

#### Modul 06 - Community Bidrag
- **SDK Liste**: Tilføjet Swift og Rust SDK’er; opdateret specifikationslink til 2025-11-25
- **Specifikationsreference**: Opdateret MCP Specifikation link til direkte specifikations-URL

#### Modul 07 - Erfaringer fra Tidlig Adoption
- **Ressource Opdateringer**: Tilføjet MCP Specifikation 2025-11-25 link og OWASP MCP Top 10 til yderligere ressourcer

#### Modul 08 - Bedste Praksis
- **Spec Versionsopdatering**: Opdateret MCP Specifikationsreference til 2025-11-25
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop til yderligere referencer

#### Modul 10 - Optimering af AI Arbejdsgange
- **Badge Opdatering**: Ændret MCP versionsbadge fra SDK version (1.9.3) til specifikationsversion (2025-11-25)
- **Ressourcelinks**: Opdateret MCP Specifikationslink; tilføjet OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Labs
- **Specifikationsreference**: Opdateret MCP Specifikationslink til 2025-11-25 version
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 til officielle ressourcer

## 18. december 2025

### Sikkerhedsdokumentationsopdatering - MCP Specifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specifikationsversionsopdatering
- **Protokolversionsopdatering**: Opdateret til at referere til nyeste MCP Specifikation 2025-11-25 (udgivet 25. november 2025)
 - Opdateret alle specifikationsversionsreferencer fra 2025-06-18 til 2025-11-25
 - Opdateret dokumentdato referencer fra 18. august 2025 til 18. december 2025
 - Bekræftet at alle specifikations-URL’er peger på aktuel dokumentation
- **Indholdsvalidering**: Omfattende validering af sikkerhedsbest practices mod de nyeste standarder
 - **Microsoft Security Solutions**: Bekræftet opdateret terminologi og links for Prompt Shields (tidligere "Jailbreak risikodetektion"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
 - **OAuth 2.1 Sikkerhed**: Bekræftet overensstemmelse med nyeste OAuth sikkerhedsbest practices
 - **OWASP Standarder**: Valideret at OWASP Top 10 for LLM’er referencer er aktuelle
 - **Azure Services**: Bekræftet alle Microsoft Azure dokumentationslinks og bedste praksis
- **Standardoverensstemmelse**: Alle refererede sikkerhedsstandarder bekræftet aktuelle
 - NIST AI Risk Management Framework
 - ISO 27001:2022
 - OAuth 2.1 Security Best Practices
 - Azure sikkerheds- og overholdelsesrammer
- **Implementeringsressourcer**: Valideret alle implementeringsguide-links og ressourcer
 - Azure API Management godkendelsesmønstre
 - Microsoft Entra ID integrationsvejledninger
 - Azure Key Vault hemmelighedshåndtering
 - DevSecOps pipelines og overvågningsløsninger

### Dokumentations Kvalitetssikring
- **Specifikationsoverensstemmelse**: Sikret at alle obligatoriske MCP sikkerhedskrav (MUST/MUST NOT) er i overensstemmelse med den nyeste specifikation
- **Ressourceaktualitet**: Bekræftet at alle eksterne links til Microsoft dokumentation, sikkerhedsstandarder og implementeringsguides er opdaterede
- **Dækning af Best Practices**: Bekræftet omfattende dækning af autentificering, autorisation, AI-specifikke trusler, forsyningskædesikkerhed og enterprise mønstre

## 6. oktober 2025

### Udvidelse af Kom Godt I Gang Sektion – Avanceret Serverbrug & Simpel Autentificering

#### Avanceret Serverbrug (03-GettingStarted/10-advanced)
- **Nyt Kapitel Tilføjet**: Introduceret en omfattende guide til avanceret MCP serverbrug, der dækker både regelmæssige og lavniveau serverarkitekturer.
 - **Regulær vs. Lavniveau Server**: Detaljeret sammenligning og kodeeksempler i Python og TypeScript for begge tilgange.
 - **Handler-baseret Design**: Forklaring af handler-baseret håndtering af værktøj/ressourcer/prompts til skalerbare, fleksible serverimplementeringer.
 - **Praktiske Mønstre**: Virkelighedsnære scenarier hvor lavniveau servermønstre er gavnlige for avancerede funktioner og arkitektur.

#### Simpel Autentificering (03-GettingStarted/11-simple-auth)
- **Nyt Kapitel Tilføjet**: Trin-for-trin vejledning i implementering af simpel autentificering i MCP servere.
 - **Auth Begreber**: Klar forklaring af autentificering vs. autorisation, og håndtering af legitimationsoplysninger.
 - **Grundlæggende Auth Implementering**: Middleware-baserede autentificeringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
 - **Fremgang til Avanceret Sikkerhed**: Vejledning i at starte med simpel auth og avancere til OAuth 2.1 og RBAC, med referencer til avancerede sikkerhedsmoduler.

Disse tilføjelser giver praktisk, hands-on vejledning til at bygge mere robuste, sikre og fleksible MCP serverimplementeringer, som bygger bro mellem grundlæggende koncepter og avancerede produktionsmønstre.

## 29. september 2025

### MCP Server Database Integration Labs - Omfattende Hands-On Læringsforløb

#### 11-MCPServerHandsOnLabs - Ny komplet databaseintegrationslæseplan
- **Komplet 13-Lab Læringsforløb**: Tilføjet omfattende hands-on læseplan til at bygge produktionsklare MCP servere med PostgreSQL databaseintegration
 - **Virkelighedsnær Implementering**: Zava Retail analytics brugssag, der demonstrerer enterprise-grade mønstre
 - **Struktureret Læringsprogression**:
   - **Labs 00-03: Grundlag** - Introduktion, kernearkitektur, sikkerhed & multi-tenancy, miljøopsætning
   - **Labs 04-06: Opbygning af MCP Server** - Databasedesign & skema, MCP Server implementering, værktøjsudvikling  
   - **Labs 07-09: Avancerede Funktioner** - Semantisk søgning integration, test & fejlfinding, VS Code integration
   - **Labs 10-12: Produktion & Bedste Praksis** - Udrulningsstrategier, overvågning & observabilitet, bedste praksis & optimering
 - **Enterprise Teknologier**: FastMCP framework, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
 - **Avancerede Funktioner**: Row Level Security (RLS), semantisk søgning, multi-tenant dataadgang, vektor-embeddings, realtidsmonitorering

#### Terminologistandardisering - Modul til Lab Konvertering
- **Omfattende Dokumentationsopdatering**: Systematisk opdateret alle README filer i 11-MCPServerHandsOnLabs til at bruge "Lab" terminologi i stedet for "Modul"
 - **Sektionstitler**: Opdateret "What This Module Covers" til "What This Lab Covers" i alle 13 labs
 - **Indholdsbeskrivelser**: Ændret "This module provides..." til "This lab provides..." i hele dokumentationen
 - **Læringsmål**: Opdateret "By the end of this module..." til "By the end of this lab..." 
 - **Navigationslinks**: Konverteret alle "Module XX:" referencer til "Lab XX:" i krydsreferencer og navigation
 - **Færdiggørelsessporing**: Opdateret "After completing this module..." til "After completing this lab..."
 - **Bevarede Tekniske Referencer**: Beholdt Python modulreferencer i konfigurationsfiler (f.eks. `"module": "mcp_server.main"`)

#### Studievejledning Forbedring (study_guide.md)
- **Visuelt Curriculum Kort**: Tilføjet ny sektion "11. Database Integration Labs" med omfattende visualisering af labstruktur
- **Repository Struktur**: Opdateret fra ti til elleve hovedsektioner med detaljeret beskrivelse af 11-MCPServerHandsOnLabs
- **Læringsvejledning**: Forbedrede navigationsinstruktioner der dækker sektioner 00-11
- **Teknologidækning**: Tilføjet FastMCP, PostgreSQL, Azure services integrationsdetaljer
- **Læringsresultater**: Fremhævet produktionsegnede serverudvikling, databaseintegrationsmønstre og enterprise-sikkerhed

#### Forbedring af Hoved-README Struktur
- **Lab-Baseret Terminologi**: Opdateret hoved README.md i 11-MCPServerHandsOnLabs til konsekvent at bruge "Lab" struktur
- **Læringsvej Organisationsstruktur**: Klar progression fra grundlæggende koncepter over avanceret implementering til produktionsudrulning
- **Virkelighedsfokus**: Fokus på praktisk, hands-on læring med enterprise-grade mønstre og teknologier

### Dokumentationskvalitet & Konsistensforbedringer
- **Hands-On Læringsfokus**: Understreget praktisk, lab-baseret tilgang i hele dokumentationen
- **Enterprise Mønsterfokus**: Fremhævet produktionsegnede implementeringer og enterprise sikkerhedsovervejelser
- **Teknologiintegration**: Omfattende dækning af moderne Azure services og AI integrationsmønstre
- **Læringsprogression**: Klar, struktureret vej fra grundlæggende koncepter til produktionsudrulning

## 26. september 2025

### Case Studies Forbedring - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Økosystemudviklingsfokus
- **README.md**: Stor udvidelse med omfattende GitHub MCP Registry case study
 - **GitHub MCP Registry Case Study**: Ny omfattende case study, der undersøger GitHubs lancering af MCP Registry i september 2025
   - **Problemanalyse**: Detaljeret undersøgelse af fragmenterede MCP server opdagelses- og implementeringsudfordringer
   - **Løsningsarkitektur**: GitHubs centraliserede registry-tilgang med one-click VS Code installation
   - **Forretningspåvirkning**: Målbare forbedringer i udvikler onboarding og produktivitet
   - **Strategisk Værdi**: Fokus på modulær agent-implementering og tværværktøjsinteroperabilitet
   - **Økosystemudvikling**: Positionering som grundlæggende platform for agentbaseret integration
 - **Forbedret Case Study Struktur**: Opdateret alle syv case studies med konsekvent formatering og omfattende beskrivelser
   - Azure AI Travel Agents: Fokus på multi-agent orkestrering
   - Azure DevOps Integration: Fokus på workflow-automatisering
   - Real-Time Dokumentationshentning: Implementering af Python konsolklient
   - Interaktiv Studieplansgenerator: Chainlit konversationsbaseret webapp

    - Dokumentation i editor: VS Code og GitHub Copilot integration
    - Azure API Management: Enterprise API integrationsmønstre
    - GitHub MCP Registry: Økosystemudvikling og fællesskabsplatform
  - **Omfattende Konklusion**: Omskrevet konklusionsafsnit der fremhæver syv case-studier på tværs af flere MCP implementeringsdimensioner
    - Enterprise Integration, Multi-Agent Orkestrering, Udviklerproduktivitet
    - Økosystemudvikling, Kategorisering af Uddannelsesapplikationer
    - Forbedrede indsigter i arkitektur mønstre, implementeringsstrategier og bedste praksis
    - Vægt på MCP som moden, produktionsklar protokol

#### Opdateringer af Studievejledning (study_guide.md)
- **Visuelt Kursuskort**: Opdateret mindmap til at inkludere GitHub MCP Registry i Case Studies sektionen
- **Case Studier Beskrivelser**: Forbedret fra generiske beskrivelser til detaljeret nedbrydning af syv omfattende case studier
- **Repositoriestruktur**: Opdateret sektion 10 for at afspejle omfattende case study dækning med specifikke implementeringsdetaljer
- **Changelog Integration**: Tilføjet 26. september 2025 post dokumenterende tilføjelse af GitHub MCP Registry og forbedringer i case studier
- **Datoopdateringer**: Opdateret fodertidsstempel til at afspejle seneste revision (26. september 2025)

### Forbedringer af Dokumentationskvalitet
- **Konsistensforbedring**: Standardiseret case study formatering og struktur på tværs af alle syv eksempler
- **Omfattende Dækning**: Case studier dækker nu enterprise, udviklerproduktivitet og økosystemudviklingsscenarier
- **Strategisk Positionering**: Forbedret fokus på MCP som grundlæggende platform for agentbaseret systemudrulning
- **Ressourceintegration**: Opdateret yderligere ressourcer til at inkludere link til GitHub MCP Registry

## 15. september 2025

### Udvidelse af Avancerede Emner - Tilpassede Transports og Context Engineering

#### MCP Tilpassede Transports (05-AdvancedTopics/mcp-transport/) - Ny Guide til Avanceret Implementering
- **README.md**: Fuldstændig implementeringsvejledning for tilpassede MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverløs event-drevet transportimplementering
    - C#, TypeScript og Python eksempler med Azure Functions integration
    - Event-drevne arkitekturmønstre for skalerbare MCP løsninger
    - Webhook modtagere og push-baseret beskedhåndtering
  - **Azure Event Hubs Transport**: Højgennemstrømnings streaming transportimplementering
    - Realtids streaming kapaciteter til lav-latens scenarier
    - Partitioneringsstrategier og checkpoint management
    - Meddelelses-batching og ydelsesoptimering
  - **Enterprise Integrationsmønstre**: Produktionsklare arkitektureksempler
    - Distribueret MCP behandling på tværs af flere Azure Functions
    - Hybrid transportarkitektur kombinerende flere transporttyper
    - Beskedudholdenhed, pålidelighed og fejlhåndteringsstrategier
  - **Sikkerhed & Monitorering**: Azure Key Vault integration og observation patterns
    - Managed identity autentificering og mindst privilegie adgang
    - Application Insights telemetri og ydelsesovervågning
    - Afbrydere og fejltolerance mønstre
  - **Test Frameworks**: Omfattende teststrategier for tilpassede transports
    - Unit testing med testdoubles og mocking frameworks
    - Integrationstest med Azure Test Containers
    - Ydelses- og belastningstest overvejelser

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI Disciplin
- **README.md**: Omfattende udforskning af context engineering som et fremvoksende felt
  - **Kerneprincipper**: Kompletdeling af kontekst, handlingsbeslutningsbevidsthed, kontekstvinduesstyring
  - **MCP Protokol Justering**: Hvordan MCP design adresserer context engineering udfordringer
    - Begrænsninger af kontekstvinduer og progressive loading strategier
    - Relevansbestemmelse og dynamisk kontekstindhentning
    - Multimodal kontekstbehandling og sikkerhedsovervejelser
  - **Implementeringstilgange**: Enkeltrådet vs. multi-agent arkitekturer
    - Kontekstchunking og prioriteringsteknikker
    - Progressiv kontekstindlæsning og komprimeringsstrategier
    - Lagdelt konteksttilgang og optimering af indhentning
  - **Målerammeværk**: Fremvoksende metrikker til evaluering af konsteksteffektivitet
    - Input effektivitet, ydelse, kvalitet og brugeroplevelsesovervejelser
    - Eksperimentelle tilgange til kontekstoptimering
    - Fejl-analyse og forbedringsmetodologier

#### Opdateringer til Curriculum Navigering (README.md)
- **Forbedret Modultstruktur**: Opdateret curriculum tabel til at inkludere nye avancerede emner
  - Tilføjet Context Engineering (5.14) og Custom Transport (5.15) poster
  - Konsistent formatering og navigationslinks på tværs af alle moduler
  - Opdaterede beskrivelser til at afspejle aktuelt indholdsomfang

### Forbedringer af Bibliotekstruktur
- **Navnestandardisering**: Omdøbt "mcp transport" til "mcp-transport" for konsistens med andre avancerede emne-mapper
- **Indholdsorganisering**: Alle 05-AdvancedTopics mapper følger nu konsekvent navngivningsmønster (mcp-[emne])

### Forbedringer af Dokumentationskvalitet
- **MCP Specifikationsjustering**: Alt nyt indhold henviser til gældende MCP Specification 2025-06-18
- **Fler-sprogede Eksempler**: Omfattende kodeeksempler i C#, TypeScript og Python
- **Enterprise Fokus**: Produktionsklare mønstre og Azure cloud integration overalt
- **Visuel Dokumentation**: Mermaid-diagrammer til arkitektur- og flowvisualisering

## 18. august 2025

### Omfattende Dokumentationsopdatering - MCP 2025-06-18 Standarder

#### MCP Sikkerhedsbedste Praksis (02-Security/) - Fuld Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fuld omskrivning i overensstemmelse med MCP Specification 2025-06-18
  - **Obligatoriske Krav**: Tilføjet eksplicitte SKAL/MÅ IKKE krav fra officiel specifikation med klare visuelle indikatorer
  - **12 Kerne Sikkerhedspraksisser**: Omstruktureret fra 15-punkts liste til omfattende sikkerhedsområder
    - Tokensikkerhed & Autentificering med ekstern identitetsudbyder integration
    - Session Management & Transport Security med kryptografiske krav
    - AI-Specifik Trusselsbeskyttelse med Microsoft Prompt Shields integration
    - Adgangskontrol & Tilladelser med mindst privilegie-princip
    - Indholdssikkerhed & Monitorering med Azure Content Safety integration
    - Supply Chain Security med omfattende komponentverifikation
    - OAuth Sikkerhed & Confused Deputy Forebyggelse med PKCE implementering
    - Incident Response & Recovery med automatiserede kapaciteter
    - Compliance & Governance med regulatorisk overensstemmelse
    - Avancerede Sikkerhedskontroller med zero trust arkitektur
    - Microsoft Sikkerhedsøkosystem Integration med omfattende løsninger
    - Kontinuerlig Sikkerhedsudvikling med adaptive praksisser
  - **Microsoft Security Solutions**: Forbedret integrationsvejledning for Prompt Shields, Azure Content Safety, Entra ID og GitHub Advanced Security
  - **Implementeringsressourcer**: Kategoriserede omfattende ressourcelinks efter Officiel MCP Dokumentation, Microsoft Security-løsninger, Sikkerhedsstandarder og Implementeringsvejledninger

#### Avancerede Sikkerhedskontroller (02-Security/) - Enterprise Implementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fuldstændig revision med enterprise-sikkerhedsarkitektur
  - **9 Omfattende Sikkerhedsområder**: Udvidet fra basis til detaljeret enterprise framework
    - Avanceret Autentificering & Autorisation med Microsoft Entra ID integration
    - Tokensikkerhed & Anti-Passthrough Kontroller med omfattende validering
    - Sessionssikkerhedskontroller med forhindring af overtagelse
    - AI-specifikke sikkerhedskontroller mod prompt-injektion og værktøjforgiftning
    - Confused Deputy Attack forebyggelse med OAuth proxy sikkerhed
    - Værktøjsudførselsikkerhed med sandboxing og isolering
    - Supply Chain Security kontroller med afhængighedsverifikation
    - Monitorerings- & Detektionskontroller med SIEM integration
    - Incident Response & Recovery med automatiserede evner
  - **Implementeringseksempler**: Tilføjet detaljerede YAML konfigurationsblokke og kodeeksempler
  - **Microsoft Solutions Integration**: Omfattende dækning af Azure sikkerhedstjenester, GitHub Advanced Security og enterprise identitetsstyring

#### Avancerede Emner Sikkerhed (05-AdvancedTopics/mcp-security/) - Produktionsklar Implementering
- **README.md**: Komplett omskrivning til enterprise sikkerhedsimplementering
  - **Aktuel Specifikationsjustering**: Opdateret til MCP Specification 2025-06-18 med obligatoriske sikkerhedskrav
  - **Forbedret Autentificering**: Microsoft Entra ID integration med omfattende .NET og Java Spring Security eksempler
  - **AI Sikkerhedsintegration**: Microsoft Prompt Shields og Azure Content Safety implementering med detaljerede Python eksempler
  - **Avanceret Trusselsstyring**: Omfattende implementeringseksempler for
    - Confused Deputy Attack forebyggelse med PKCE og bruger samtykkevalidering
    - Token Passthrough forebyggelse med målgruppe-validering og sikker tokenhåndtering
    - Session Overtagelsesforebyggelse med kryptografisk binding og adfærdsanalyse
  - **Enterprise Sikkerhedsintegration**: Azure Application Insights overvågning, trusselsdetektions-pipelines og supply chain sikkerhed
  - **Implementeringstjekliste**: Klar opdeling af obligatoriske vs. anbefalede sikkerhedskontroller med Microsoft sikkerhedsøkosystem fordele

### Dokumentationskvalitet & Standardjustering
- **Specifikationsreferencer**: Opdaterede alle referencer til gældende MCP Specification 2025-06-18
- **Microsoft Sikkerhedsøkosystem**: Forbedret integrationsvejledning i hele sikkerhedsdokumentationen
- **Praktisk Implementering**: Tilføjede detaljerede kodeeksempler i .NET, Java og Python med enterprise mønstre
- **Ressourceorganisering**: Omfattende kategorisering af officiel dokumentation, sikkerhedsstandarder og implementeringsvejledninger
- **Visuelle Indikatorer**: Klar afmærkning af obligatoriske krav vs. anbefalede praksisser


#### Kernekoncepter (01-CoreConcepts/) - Fuld Modernisering
- **Protokolversionsopdatering**: Opdateret til at referere MCP Specification 2025-06-18 med datobaseret versionsformat (ÅÅÅÅ-MM-DD)
- **Arkitekturforfining**: Forbedrede beskrivelser af Hosts, Clients og Servers for at afspejle aktuelle MCP arkitekturmodeller
  - Hosts nu tydeligt defineret som AI applikationer der koordinerer flere MCP klientforbindelser
  - Clients beskrevet som protokolforbindere der opretholder one-to-one server relationer
  - Servers forbedret med lokale vs. fjernudrulningsscenarier
- **Primitive Omstrukturering**: Fuldstændig revision af server- og klientprimitive
  - Server Primitives: Ressourcer (datakilder), Prompts (skabeloner), Værktøjer (eksekverbare funktioner) med detaljerede forklaringer og eksempler
  - Client Primitives: Sampling (LLM fuldførelser), Elicitation (brugerinput), Logging (debugging/monitorering)
  - Opdateret med aktuelle opdagelses (`*/list`), hentnings (`*/get`) og udførelses (`*/call`) metode-mønstre
- **Protokolarkitektur**: Introduceret to-lags arkitekturmodel
  - Data Lag: JSON-RPC 2.0 fundament med livscyklusstyring og primitive komponenter
  - Transport Lag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer
- **Sikkerhedsrammeværk**: Omfattende sikkerhedsprincipper inklusiv eksplicit bruger samtykke, databeskyttelse, værktøjseksekveringssikkerhed og sikkerhed i transportlaget
- **Kommunikationsmønstre**: Opdaterede protokolmeddelelser der viser initialisering, opdagelse, udførelse og notifikationsflows
- **Kodeeksempler**: Opfriskede flersprogede eksempler (.NET, Java, Python, JavaScript) for at afspejle aktuelle MCP SDK mønstre

#### Sikkerhed (02-Security/) - Omfattende Sikkerhedsrevision  
- **Standardtilpasning**: Fuld tilpasning til MCP Specification 2025-06-18 sikkerhedskrav
- **Autentificeringsevolution**: Dokumenteret evolution fra brugerdefinerede OAuth-servere til eksterne identitetsudbyderdelegering (Microsoft Entra ID)
- **AI-specifik trusselsanalyse**: Forbedret dækning af moderne AI angrebsvektorer
  - Detaljerede prompt-injektionsangrebsscenarier med virkelighedseksempler
  - Værktøjsforgiftning mekanismer og "rug pull" angrebsmønstre
  - Kontekstvinduesforgiftning og model forvirringsangreb
- **Microsoft AI Sikkerhedsløsninger**: Omfattende dækning af Microsoft sikkerhedsøkosystem
  - AI Prompt Shields med avanceret detektion, spotlighting og afgrænsningsteknikker
  - Azure Content Safety integrationsmønstre
  - GitHub Advanced Security til supply chain beskyttelse
- **Avanceret trusselsforebyggelse**: Detaljerede sikkerhedskontroller for
  - Session hijacking med MCP-specifikke angrebsscenarier og kryptografiske session-ID krav
  - Confused deputy problemer i MCP proxy scenarier med eksplicitte samtykkekrav
  - Token passthrough sårbarheder med obligatoriske valideringskontroller
- **Supply Chain Security**: Udvidet AI supply chain dækning inklusive foundation models, embeddings services, context providers og tredjeparts-API'er
- **Foundation Security**: Forbedret integration med enterprise sikkerhedsmønstre inklusiv zero trust arkitektur og Microsoft sikkerhedsøkosystem
- **Ressourceorganisering**: Kategoriserede omfattende ressourcelinks efter type (Officiel Docs, Standards, Forskningsartikler, Microsoft Løsninger, Implementeringsvejledninger)

### Forbedringer af Dokumentationskvalitet
- **Strukturerede Læringsmål**: Forbedrede læringsmål med specifikke, handlingsorienterede resultater 
- **Krydsreferencer**: Tilføjet links mellem relaterede sikkerheds- og kernekoncept emner
- **Aktuel Information**: Opdateret alle dato-referencer og specifikationslinks til gældende standarder
- **Implementeringsvejledning**: Tilføjet specifikke, handlingsanviste implementeringsretningslinjer gennem begge sektioner

## 16. juli 2025

### README og Navigationsforbedringer
- Fuldstændig redesignet curriculum navigation i README.md
- Erstattet `<details>` tags med mere tilgængeligt tabelbaseret format
- Oprettet alternative layoutmuligheder i ny "alternative_layouts" mappe
- Tilføjet kort-baserede, fanebaserede og accordion-stil navigationseksempler
- Opdateret repositoriestruktuafsnittet for at inkludere alle seneste filer
- Forbedret "How to Use This Curriculum" sektion med klare anbefalinger
- Opdateret MCP specifikationslinks til at pege på korrekte URLs
- Tilføjet Context Engineering sektion (5.14) til curriculum struktur

### Opdateringer til Studievejledning
- Fuldstændig revideret studievejledning for at tilpasse sig nuværende repositoriestruktur
- Tilføjet nye sektioner for MCP Clients og Tools, og Populære MCP Servers
- Opdateret det Visuelle Kursuskort for præcist at afspejle alle emner
- Forbedret beskrivelser af Avancerede Emner til at dække alle specialiserede områder
- Opdateret Case Studies sektion for at afspejle faktiske eksempler
- Tilføjet denne omfattende changelog

### Fællesskabsbidrag (06-CommunityContributions/)
- Tilføjet detaljeret information om MCP servers til billedgenerering
- Tilføjet omfattende sektion om brug af Claude i VSCode
- Tilføjet Cline terminal klient opsætning og brugsinstruktioner
- Opdateret MCP klient sektion til at inkludere alle populære klientmuligheder
- Forbedrede bidragseksempler med mere præcise kodeeksempler

### Avancerede Emner (05-AdvancedTopics/)
- Organiseret alle specialiserede emne-mapper med konsekvent navngivning
- Tilføjet context engineering materialer og eksempler
- Tilføjet Foundry agent integrationsdokumentation
- Forbedret Entra ID sikkerhedsintegrationsdokumentation

## 11. juni 2025

### Første Oprettelse
- Udgivet første version af MCP for Beginners curriculum

- Oprettet grundlæggende struktur for alle 10 hovedsektioner
- Implementeret Visuelt Kursuskort til navigation
- Tilføjet indledende prøveprojekter i flere programmeringssprog

### Kom godt i gang (03-GettingStarted/)
- Oprettet de første serverimplementeringseksempler
- Tilføjet vejledning til klientudvikling
- Inkluderet instruktioner til LLM-klientintegration
- Tilføjet dokumentation til VS Code-integration
- Implementeret Server-Sent Events (SSE) servereksempler

### Kernebegreber (01-CoreConcepts/)
- Tilføjet detaljeret forklaring af klient-server arkitektur
- Oprettet dokumentation om nøgleprotokolkomponenter
- Dokumenteret beskedmønstre i MCP

## 23. maj 2025

### Repositoriumstruktur
- Initialiseret repositorium med grundlæggende mappestruktur
- Oprettet README-filer for hver hovedsektion
- Sat oversættelsesinfrastruktur op
- Tilføjet billedeaktiver og diagrammer

### Dokumentation
- Oprettet indledende README.md med oversigt over curriculum
- Tilføjet CODE_OF_CONDUCT.md og SECURITY.md
- Sat SUPPORT.md op med vejledning til at få hjælp
- Oprettet foreløbig studieguide-struktur

## 15. april 2025

### Planlægning og Rammeværk
- Indledende planlægning for MCP for Begyndere-kursus
- Definerede læringsmål og målgruppe
- Skitseret 10-sektions struktur for curriculum
- Udviklet konceptuelt rammeværk for eksempler og casestudier
- Oprettet indledende prototypeeksempler for nøglebegreber

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
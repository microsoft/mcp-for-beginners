# Ændringslog: MCP for Beginners Curriculum

Dette dokument tjener som en registrering af alle væsentlige ændringer foretaget i Model Context Protocol (MCP) for Beginners curriculum. Ændringer dokumenteres i omvendt kronologisk rækkefølge (nyeste ændringer først).

## 29. juli 2026

### Nyt modul 08 følgesvend: Pålidelighedssidecars og sikre genforsøg

Tilføjet en leverandøruafhængig følgesvendlektion til MCP-værktøjer, der skaber virkelige effekter,
i overensstemmelse med den endelige `2026-07-28` specifikation.

- **Ny**: Følgesvendlektionen om [pålidelighedssidecars][reliability-sidecar]
  bruger én supportbillet-historie, to Mermaid-diagrammer og en genforsøgsbeslutnings-
  flow til at forklare stabile operationstaster, atomisk duplikatindgang,
  forsoning, beviser og Tasks-udvidelsesgrænsen.
- **Ny**: En standardbiblioteks Python- og SQLite-fejlindsprøjtningsøvelse
  bruger separate operation- og billetlager til at demonstrere et svar, der mistes
  efter at en ekstern effekt har gennemført. Seks deterministiske tests dækker naive
  duplikationer, beskyttet genstartgendannelse, payload-konflikter, cachede resultater,
  aktive krav og samtidige duplikatindgange.
- **Opdateret**: Modul 08 linker nu til følgesvendlektionen, identificerer den
  endelige `2026-07-28` statsløse forespørgselsmodel, skelner OpenTelemetry
  observerbarhed fra den forældede MCP-loggingfunktion og begrænser sit
  generiske genforsøgseksempel til skrivebeskyttede operationer.
- **Valgfri**: Lektionen kortlægger sine bærbare koncepter til én tagget
  community-implementering uden at gøre den hostede tjeneste eller netværkskald
  til en del af øvelsen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. juli 2026

### Ny lektion: 2026-07-28 MCP Specifikations Release Candidate

Tilføjet dækning af den kommende `2026-07-28` MCP specifikations-release candidate (annonceret 21. maj 2026; endelig udgivelse planlagt til 28. juli 2026), opsummeret fra det [officielle annonceringsblogindlæg](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Curriculumets baseline forbliver **MCP Specification 2025-11-25** indtil den nye version frigives, så dette præsenteres som fremadskuende vejledning frem for en omskrivning af eksisterende lektioner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — en fuld lektion der dækker den statsløse protokolkerne (fjernelse af `initialize` håndtryk og `Mcp-Session-Id`), de nye `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context i `_meta`, den formelle Extensions-ramme (MCP Apps og den nye Tasks-udvidelse), seks autorisationshærdende SEPer, udfasningen af Roots/Sampling/Logging, og overgangen til fuld JSON Schema 2020-12 for værktøjs-skemaer.
- **Opdateret** med fremadskuende henvisninger til den nye lektion:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokolversionsnote, Sampling/Roots/Logging/Tasks sektioner og "Hvad kommer herefter"
  - [02-Security/README.md](./02-Security/README.md): autorisationshærdningshenvisning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): statsløs transporthenvisning
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling-udfasede henvisning
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging-udfasede og Tasks-udvidelseshenvisning
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): statsløs/session-routing henvisning
  - [README.md](./README.md): "Ser fremad" note i specifikationsafsnittet og en ny `1.1` post i curriculummoduletabellen
  - [study_guide.md](./study_guide.md): fremadskuende punkt under Core Concepts oversigten og en dateret tillægspåmindelse
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): henvisning til `mcp-session-id` transportmappen forud for den statsløse forespørgselsmodel
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduloversigt med henvisning til Root Contexts/Sampling udfasninger og Tasks-udvidelsen
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisationshærdningshenvisning

## 24. juni 2026

### Ny lektion: Brug af MCP i Copilot app

- [Tooling sektion](./12-tooling/README.md) Tilføjet tooling-sektion.
- [MCP i Copilot app](./12-tooling/01-copilot-app/README.md)

## 16. juni 2026

### MCP Specifikationsjustering & Sample-validering

Validerede curriculum mod den aktuelle **MCP Specification 2025-11-25** og de nyeste officielle SDK'er, rettede derefter de resterende forældede reference til specifikationen og bekræftede, at kerneeksemplerne stadig kan bygges og køres.

#### Specifikationsversionsrettelser (2025-06-18 / 2025-03-26 → 2025-11-25)

Opdaterede det engelske indhold, hvor det stadig hævdede, at en ældre specifikationsrevision var den *nuværende/sidste* standard, og omdirigerede links til de kanoniske `modelcontextprotocol.io` specifikationsstier:
- **05-AdvancedTopics/mcp-security/README.md**: Opdaterede "Nuværende Standard"-banner, introduktion, kerne-sikkerhedsprincip-per overskrift, obligatoriske krav-overskrift, Microsoft Entra ID-sektion, Referencer & Ressourcer links og afsluttende sikkerhedsmeddelelse (8 referencer) til 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Opdaterede yderligere ressourcer specifikationslink og "Nuværende Standard"-banner til 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Udskiftede det forældede `2025-03-26` sikkerheds- og tillids-link med den aktuelle 2025-11-25 sikkerhedspraksis-side
- **03-GettingStarted/14-sampling/README.md**: Opdaterede officiel sampling-dokumentationslink til 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Opdaterede præsent tids "nuværende MCP specifikation" reference og yderligere ressourcer specifikationslink til 2025-11-25 (historiske SSE-udfasede noter bibeholdt for nøjagtighed)

#### Sample-validering mod aktuelle SDK'er

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` løste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` bestod uden typefejl — eksisterende `McpServer`/`StdioServerTransport` API'er forbliver gyldige
- **Python (03-GettingStarted/01-first-server/solution/python)**: Valideret i isoleret `.venv` med `mcp[cli]` (1.27.2); `py_compile` bestod og `FastMCP.list_tools()` returnerede korrekt `add` og `subtract` værktøjerne
- Bekræftet at alle sample `@modelcontextprotocol/sdk` versionsintervaller (`>=1.26.0` / `^1.26.0` / `^1.27.0`) løses rent til den aktuelle `1.29.0` uden brydende API-ændringer

#### Afstemning af afhængighedspins (lukker versionshuller)

Opdaterede forældede SDK pins, så hver sample følger den aktuelle MCP-udgivelse, i overensstemmelse med det overordnede repo-konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Opdaterede `@modelcontextprotocol/sdk` fra `^1.8.0` → `>=1.26.0` og opdaterede den forældede `"updated for MCP 2025-06-18"` pakkebeskrivelse til `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** og **lab4/code/github_mcp_server/pyproject.toml**: Opdaterede den præcise pin `mcp==1.23.0` → `mcp>=1.26.0`; genskabte begge `uv.lock` filer (`uv lock`) så lockfilerne løser til den aktuelle `mcp 1.27.2` og forbliver synkroniserede med manifestfilerne

#### Curriculum gap-analyse — Seneste specifikations feature-dækning

Bekræftet at curriculum allerede dækker alle primitive introduceret/udvidet i MCP 2025-11-25, så ingen indholdshuller er tilbage:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-tilstand)**: Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumenteret i 00-Introduction, 01-CoreConcepts og 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentelle, langvarige operationer)**: Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Dokumenteret i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features

### Sikkerhedshærdning & afhængighedssårbarhedsoprydning

Kørte en fuld sikkerhedsgennemgang af alle afhængighedsmanifest og eksempelkildekode, og udbedrede derefter alle rapporterede npm advisory'er og en kode-fund. Efter udbedring rapporterer `npm audit` **0 sårbarheder** i alle gennemgåede mapper.

#### npm afhængighedssårbarheder (transitive) — Rettet

Gjorde revision af alle 15 committede `package-lock.json` filer. Sårbarheder var begrænset til transitive afhængigheder hentet af MCP Inspector dev-værktøj, OpenAI-klienten og MCP SDK; alle er nu løst uden at bryde eksemplerne:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** og **lab3/code/weather_mcp/inspector**: Opdaterede `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), hvilket fjernede de inkluderede advisory'er for `ajv`, `brace-expansion`, `diff`, `path-to-regexp` og `ws`. Tilføjede en npm `overrides` post, der tvinger patched `shell-quote@1.8.4` for at eliminere den resterende kritiske advisory båret af `concurrently`; genskabte begge lockfiler (nu 0 sårbarheder)
- **03-GettingStarted/samples/typescript**: `npm audit fix` opdaterede transitive `qs` (moderat) til en patched udgivelse
- **03-GettingStarted/samples/javascript**: `npm audit fix` opdaterede transitive `hono` (moderat) til en patched udgivelse
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` opdaterede transitive `form-data` (høj) til en patched udgivelse
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genererede manglende `package-lock.json` så projektet er reproducerbart og auditabelt (0 sårbarheder)

#### Kode-niveau sikkerhedsrettelse (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Fjernet `shell=True` fra `open_in_vscode` værktøjet. Det tidligere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillod shell-metategn i en mappebane at blive tolket af `cmd.exe` (kommandoinjektionsvektor). Det starter nu resolved `Code.exe` direkte med mappen som argument — uden shell — hvilket funktionelt er det samme og sikkert

#### Python Afhængighedsrevisionskontrol

- Reviderede alle Python requirements sæt med `pip-audit`. `05-AdvancedTopics` og `03-GettingStarted/samples/python` rapporterede **ingen kendte sårbarheder** (deres `mcp` / `httpx` / `pydantic` / `python-dotenv` intervaller løser til aktuelle patched udgivelser)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flaggede den transitive afhængighed **`werkzeug` 3.1.1** med tre `safe_join` Windows enhedsnavn DoS advisory'er — `CVE-2025-66221`, `CVE-2026-21860`, og `CVE-2026-27199` (alle rettet i 3.1.6). Tilføjede en eksplicit sikkerhedspin `werkzeug>=3.1.6` så patched udgivelsen løses; bekræftede, at constraint løser rent med `chainlit` / `mcp` / `semantic-kernel` stacken

### Produktnavnumændring

Opdaterede alt indhold i curriculum for at afspejle Microsofts produktrebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Opdaterede Discord community link

- **AGENTER.md**: Opdateret Discord-server reference
- **README.md**: Opdateret referencer til teknologiekosystemet
- **study_guide.md**: Opdaterede referencer til case-studier
- **05-AdvancedTopics/README.md**: Opdateret titel og beskrivelse for modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Opdateret sektion overskrift og beskrivelse
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Fuld opdatering af modultitel og indhold
- **05-AdvancedTopics/mcp-security-entra/README.md**: Opdateret krydsreference link
- **07-LessonsfromEarlyAdoption/README.md**: Opdaterede referencer til case-studier
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Opdateret sektion 9 overskrift, badges og kapabiliteter
- **08-BestPractices/README.md**: Opdateret Discord community link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Opdateret Discord kanal reference
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Opdateret model-implementerings reference
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Opdateret AI Services tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Opdaterede ressourcereferencer

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Opdaterede hovedcurriculum referencer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Opdateret modultitel, oversigt og alle moduloverskrifter
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Opdateret titel, læringsmål, opsætningsinstruktioner og ressourcer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Opdateret titel, læringsmål, MCP hosts tabel og krydsreferencer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Opdateret titel, badges, forudsætninger og ressourcer
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Opdaterede Agent Builder referencer og feedback link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Opdaterede forudsætninger og extensions referencer

---

## 11. april 2026

### Ny lektion, dokumentationsrettelser og afhængighedsopdateringer

#### Nyt curriculumindhold tilføjet

**Modul 05 - Avancerede emner**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende guide, der dækker det modsatrettede diskussionsmønster for multi-agent systemer
  - Mermaid arkitekturdiagram: to agenter → delt MCP-server → diskussionstranskript → dommer → dom
  - Delt MCP-værktøjsserver (`web_search` + `run_python`) implementeret i Python og TypeScript
  - Modsatrettede system-prompter (FOR / IMOD / Dommer) med eksplicitte værktøjsbrugs-krav
  - Diskussionsorkestrator i Python, TypeScript og C#, der styrer runder og routing af argumenter
  - MCP `ClientSession` kobling for orkestratoren til reelle værktøjsopkald
  - Use-case tabel (hallucinationsregistrering, trusselsmodellering, API design review, faktatjek, teknologivalg)
  - Sikkerhedsovervejelser: sandboxed udførelse, værktøjsopkaldsvalidering, ratebegrænsning, revisionslogning
  - Struktureret øvelse med tre praktiske scenarier (kodegennemgang, arkitektur beslutning, indholdsmoderering)

#### Dokumentationsrettelser

**Modul 03 - Kom godt i gang**
- **05-stdio-server/README.md**: Rettet ufuldstændigt TypeScript stdio server eksempel — tilføjet manglende transport instansiering (`new StdioServerTransport()`) og `server.connect(transport)` opkald for at matche Python og .NET eksempler i samme sektion
- **14-sampling/README.md**: Rettet slåfejl — korrekt til `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculumopdateringer

**Hoved README.md**
- Tilføjet post 5.17 (Adversarial Multi-Agent Reasoning med MCP) til curriculum tabellen med direkte link til ny lektion

**05-AdvancedTopics/README.md**
- Tilføjet række for lektion 5.17 til lektionstabellen

**study_guide.md**
- Tilføjet Adversarial Multi-Agent Reasoning emne til mind-map og prosabeskrevne avancerede emner

#### Kode- og sikkerhedsrettelser

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sikkerhedsrettelse — kommandoinjektion**: Udskiftet `execSync` shell interpolation med `execFile` + `promisify` i TypeScript `run_python` værktøjet, hvilket eliminerer kommandoinjektionsoverfladen (LLM-kontrolleret kode sendes nu som et bogstaveligt argv element uden shell involvering)
- **MCP værktøjsloop kobling**: Opdateret Python debat orkestrator til brug af `AsyncAnthropic` klient (erstatter blokkerende sync `Anthropic`), sende live `ClientSession` direkte til hver agent tur, hente værktøjsdefinitioner via `session.list_tools()` hver tur og afsende `tool_use` blokke via `session.call_tool()` i loop indtil modellen udsender endelig tekstrespons

#### Afhængighedsopdateringer

- Opgraderet `hono` til 4.12.12 i flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Opgraderet `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript pakker
- Opgraderet `cryptography` fra 46.0.5 til 46.0.7 i Python pakker (10-StreamliningAIWorkflows labs 3 og 4)
- Opgraderet `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Oversættelser

- Synkroniserede oversættelser for 48+ sprog med de seneste kildeændringer (i18n opdatering)

---

## 5. februar 2026

### Repositorium-dækkende validering og navigationsforbedringer

#### Nyt curriculumindhold tilføjet

**Modul 03 - Kom i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide til opsætning af MCP hosts
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigurations-eksempler
  - JSON konfigurationsskabeloner for alle store hosts
  - Sammenligningstabel for transporttyper (stdio, SSE/HTTP, WebSocket)
  - Fejlfinding af almindelige forbindelsesproblemer
  - Sikkerhedspraksis for værtskonfiguration

- **13-mcp-inspector/README.md**: Ny fejlsøgningsguide til MCP Inspector
  - Installationsmetoder (npx, npm global, fra kilde)
  - Forbindelse til servere via stdio og HTTP/SSE
  - Testværktøjer, ressourcer og prompt workflows
  - VS Code integration med MCP Inspector
  - Almindelige fejlsøgningsscenarier med løsninger

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guide til implementering af paginering
  - Cursor-baserede pagineringmønstre i Python, TypeScript, Java
  - Klient-side håndtering af paginering
  - Cursor designstrategier (opak vs. struktureret)
  - Anbefalinger til ydeevneoptimering

**Modul 05 - Avancerede emner**
- **mcp-protocol-features/README.md**: Nyt dybdegående indblik i protokolfunktioner
  - Implementering af fremskridts-notifikationer
  - Annulleringsmønstre for anmodninger
  - Ressourceskabeloner med URI-mønstre
  - Serverlivscyklusstyring
  - Kontrol af logningsniveau
  - Fejlhåndteringsmønstre med JSON-RPC koder

#### Navigationsrettelser (24+ filer opdateret)

**Hovedmodul READMEs**
 Nu links til både første lektion OG næste modul

**02-Sikkerheds undermapper**
- Alle 5 supplerende sikkerhedsdokumenter har nu "What's Next" navigation:

**09-CaseStudy filer**
- Alle case-studiefiler har nu sekventiel navigation:

**10-StreamliningAI Labs**
Tilføjet What's Next sektion til Modul 10 oversigt og Modul 11

#### Kode- og indholdsrettelser

**SDK og afhængighedsopdateringer**
Rettet tom openai version til `^4.95.0`
Opdateret SDK fra `^1.8.0` til `>=1.26.0`
Opdateret mcp versionspins til `>=1.26.0`

**Kode rettelser**
Rettet ugyldig model `gpt-4o-mini` til `gpt-4.1-mini`

**Indholdsrettelser**
Rettet ødelagt link `READMEmd` → `README.md`, rettet curriculum header `Module 1-3` → `Module 0-3`, rettet case-sensitiv sti
Fjernet korrupt dublet af Case Study 5 indhold

**Begyndervejledning forbedringer**
Tilføjet ordentlig introduktion, læringsmål og forudsætninger for begyndere

#### Curriculumopdateringer

**Hoved README.md**
- Tilføjet poster 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) til curriculum tabel

**Modul README-filer**
Tilføjet lektioner 12 og 13 til lektionliste
Tilføjet Praktiske guider sektion med paginering link
Tilføjet lektioner 5.15 (Custom Transport) og 5.16 (Protocol Features)

**study_guide.md**
- Opdateret mindmap med alle nye emner: MCP Hosts Opsætning, MCP Inspector, Paginering Strategier, Dybt Indblik i Protokolfunktioner

## 28. jan 2026

### MCP Specifikation 2025-11-25 Overensstemmelsesgennemgang

#### Kernebegrebsforbedringer (01-CoreConcepts/)
- **Ny klient primitiv - Roots**: Tilføjet omfattende dokumentation om Roots klient-primitiven, der gør det muligt for servere at forstå filsystemgrænser og adgangstilladelser
- **Værktøjsannotationer**: Tilføjet dokumentation om værktøjsadfærdsannotationer (`readOnlyHint`, `destructiveHint`) for bedre beslutninger om værktøjsudførelse
- **Værktøjsopkald i Sampling**: Opdateret Sampling dokumentation til at inkludere `tools` og `toolChoice` parametre til modelstyret værktøjsopkald under sampling-forespørgsler
- **URL mode elicitation**: Tilføjet dokumentation om URL-baseret elicitation for server-initieret ekstern webinteraktion
- **Opgaver (Eksperimentelt)**: Tilføjet ny sektion, der dokumenterer den eksperimentelle Opgavefunktion for holdbare udførelsesomslag og udsat resultatindhentning
- **Ikonunderstøttelse**: Noteret at værktøjer, ressourcer, ressourceskabeloner og prompts nu kan inkludere ikoner som yderligere metadata

#### Dokumentationsopdateringer
- **README.md**: Tilføjet MCP Specifikation 2025-11-25 versionsreference og forklaring af versionsstyring baseret på dato
- **study_guide.md**: Opdateret curriculum-kort til at inkludere Opgaver og Værktøjsannotationer i Kernebegreber sektionen; opdateret dokument tidsstempel

#### Verifikation af specoverensstemmelse
- **Protokolversion**: Verificeret at al dokumentation refererer til den aktuelle MCP Specifikation 2025-11-25
- **Arkitekturtilpasning**: Bekræftet korrekt dokumentation af to-lags arkitektur (Data Layer + Transport Layer)
- **Primitiver dokumentation**: Valideret serverprimitiver (Ressourcer, Prompter, Værktøjer) og klientprimitiver (Sampling, Elicitation, Logging, Roots)
- **Transportmekanismer**: Verificeret STDIO og Streamable HTTP transport dokumentationsnøjagtighed
- **Sikkerhedsanvisninger**: Bekræftet overensstemmelse med aktuelle MCP Sikkerhedsbedste praksisser dokumentation

#### Vigtige MCP 2025-11-25 funktioner dokumenteret
- **OpenID Connect Discovery**: Auth-server opdagelse gennem OIDC
- **OAuth Client ID metadata dokumenter**: Anbefalet klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skemadefinitioner
- **SDK tiering system**: Formaliserede krav til SDK funktionalitetsstøtte og vedligeholdelse
- **Governance struktur**: Formaliserede arbejdsgrupper og interessegrupper i MCP governance

### Stor opdatering af sikkerhedsdokumentation (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integration
- **Nyt hands-on træningsressource**: Tilføjet omfattende integration med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i alle sikkerhedsdokumenter
- **Ekspeditionsrutedækning**: Dokumenteret fuld progression fra Base Camp til Summit
- **OWASP tilpasning**: Al sikkerhedsanvisning kortlagt til OWASP MCP Azure Security Guide risici

#### OWASP MCP Top 10 integration
- **Ny sektion**: Tilføjet OWASP MCP Top 10 sikkerhedsrisikotabel med Azure afbødningsmetoder til hovedsikkerheds-README
- **Risiko-baseret dokumentation**: Opdateret mcp-security-controls-2025.md med OWASP MCP risikoreferencer for hvert sikkerhedsområde
- **Referencearkitektur**: Linket til OWASP MCP Azure Security Guide referencearkitektur og implementeringsmønstre

#### Opdaterede sikkerhedsfiler
- **README.md**: Tilføjet Sherpa Workshop oversigt, ekspeditionsrutetabel, OWASP MCP Top 10 risikosammendrag og hands-on træningssektion
- **mcp-security-controls-2025.md**: Opdateret header til februar 2026, tilføjet OWASP risikoreferencer (MCP01-MCP08), rettet versionsinkonsistens i specifikation
- **mcp-security-best-practices-2025.md**: Tilføjet Sherpa og OWASP ressourcer sektion, opdateret tidsstempel
- **mcp-best-practices.md**: Tilføjet hands-on træningssektion med Sherpa og OWASP links
- **azure-content-safety-implementation.md**: Tilføjet OWASP MCP06 reference, Sherpa Camp 3 tilpasning og yderligere ressourcer sektion

#### Nye ressourcelinks tilføjet
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP risikosider (MCP01-MCP10)

### Curriculum-Bred MCP Specifikation 2025-11-25 Justering

#### Modul 03 - Kom godt i gang
- **SDK Dokumentation**: Tilføjet Go SDK til den officielle SDK-liste; opdateret alle SDK-referencer til at stemme overens med MCP Specifikation 2025-11-25
- **Transportafklaring**: Opdaterede STDIO og HTTP Streaming transportbeskrivelser med eksplicitte specifikationsreferencer

#### Modul 04 - Praktisk Implementering
- **SDK Opdateringer**: Tilføjet Go SDK; opdateret SDK-liste med versionsreference til specifikationen
- **Authorization Spec**: Opdateret MCP Authorization specifikationslink til gældende 2025-11-25 version

#### Modul 05 - Avancerede Emner
- **Nye Funktioner**: Tilføjet note om nye MCP Specifikation 2025-11-25 funktioner (Opgaver, Værktøjsannoteringer, URL Mode Elicitation, Rødder)
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop links til yderligere referencer

#### Modul 06 - Community Bidrag
- **SDK Liste**: Tilføjet Swift og Rust SDK'er; opdateret specifikationslink til 2025-11-25
- **Spec Reference**: Opdateret MCP Specifikation link til direkte specifikations-URL

#### Modul 07 - Læringer fra Tidlig Adoption
- **Ressourceopdateringer**: Tilføjet MCP Specifikation 2025-11-25 link og OWASP MCP Top 10 til yderligere ressourcer

#### Modul 08 - Best Practices
- **Spec Versions**: Opdateret MCP Specifikationsreference til 2025-11-25
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop til yderligere referencer

#### Modul 10 - Effektivisering af AI Workflows
- **Badge Opdatering**: Ændret MCP versionsbadge fra SDK version (1.9.3) til specifikationsversion (2025-11-25)
- **Ressourcelinks**: Opdateret MCP Specifikation link; tilføjet OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Labs
- **Spec Reference**: Opdateret MCP Specifikation link til 2025-11-25 version
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 til officielle ressourcer

## 18. december 2025

### Sikkerhedsdokumentationsopdatering - MCP Specifikation 2025-11-25

#### MCP Sikkerhed Best Practices (02-Security/mcp-best-practices.md) - Versionsopdatering af Specifikation
- **Protokolversionsopdatering**: Opdateret til at referere til seneste MCP Specifikation 2025-11-25 (udgivet 25. november 2025)
  - Opdaterede alle versionsreferencer fra 2025-06-18 til 2025-11-25
  - Opdaterede dokumentdatoer fra 18. august 2025 til 18. december 2025
  - Verificeret at alle specifikations-URL’er peger til nuværende dokumentation
- **Indholdsvalidering**: Omfattende validering af sikkerhedsbest practices imod nyeste standarder
  - **Microsoft Security Solutions**: Verificeret aktuel terminologi og links for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Sikkerhed**: Bekræftet overensstemmelse med nyeste OAuth sikkerhedsbest practices
  - **OWASP Standarder**: Valideret at OWASP Top 10 for LLM'er referencer er aktuelle
  - **Azure Services**: Verificeret alle Microsoft Azure dokumentationslinks og best practices
- **Standardoverensstemmelse**: Alle refererede sikkerhedsstandarder bekræftet aktuelle
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure sikkerheds- og compliance-rammer
- **Implementeringsressourcer**: Valideret alle guides og ressourcelinks til implementering
  - Azure API Management autentificeringsmønstre
  - Microsoft Entra ID integrationsguider
  - Azure Key Vault hemmelighedsstyring
  - DevSecOps pipelines og overvågningsløsninger

### Dokumentationskvalitetssikring
- **Specifikationsoverensstemmelse**: Sikret at alle obligatoriske MCP sikkerhedskrav (MUST/MUST NOT) stemmer overens med seneste specifikation
- **Ressourceaktualitet**: Verificeret alle eksterne links til Microsoft-dokumentation, sikkerhedsstandarder og implementeringsguider
- **Best Practices Dækning**: Bekræftet omfattende dækning af autentificering, autorisation, AI-specifikke trusler, forsyningskædesikkerhed og virksomhedsmønstre

## 6. oktober 2025

### Udvidelse af Kom godt i gang sektion – Avanceret Serverbrug & Simpel Autentificering

#### Avanceret Serverbrug (03-GettingStarted/10-advanced)
- **Nyt Kapitel Tilføjet**: Introduceret en omfattende guide til avanceret MCP serverbrug, der dækker både almindelig og lav-niveau serverarkitektur.
  - **Almindelig vs. Lav-niveau Server**: Detaljeret sammenligning og kodeeksempler i Python og TypeScript for begge tilgange.
  - **Handler-baseret Design**: Forklaring af handler-baseret værktøj/ressource/prompt styring for skalerbare, fleksible serverimplementeringer.
  - **Praktiske Mønstre**: Virkelige scenarier, hvor lav-niveau servermønstre er fordelagtige for avancerede funktioner og arkitektur.

#### Simpel Autentificering (03-GettingStarted/11-simple-auth)
- **Nyt Kapitel Tilføjet**: Trin-for-trin guide til implementering af simpel autentificering i MCP servere.
  - **Auth Begreber**: Klar forklaring af autentificering vs. autorisation, og håndtering af legitimationsoplysninger.
  - **Basic Auth Implementering**: Middleware-baserede autentificeringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
  - **Progression til Avanceret Sikkerhed**: Vejledning i at starte med simpel auth og avancere til OAuth 2.1 og RBAC, med henvisninger til avancerede sikkerhedsmoduler.

Disse tilføjelser giver praktisk, håndgribelig vejledning til at bygge mere robuste, sikre og fleksible MCP serverimplementeringer, der bygger bro mellem grundlæggende koncepter og avancerede produktionsmønstre.

## 29. september 2025

### MCP Server Database Integrations Labs – Omfattende Hands-On Læringssti

#### 11-MCPServerHandsOnLabs - Nyt komplet databaseintegrationspensum
- **Fuld 13-Lab læringssti**: Tilføjet omfattende hands-on pensum for at bygge produktionsklare MCP servere med PostgreSQL databaseintegration
  - **Virkelighedsnær Implementering**: Zava Retail analyseuse case, der demonstrerer virksomhedsklare mønstre
  - **Struktureret læring progression**:
    - **Labs 00-03: Fundament** - Introduktion, Kernearkitektur, Sikkerhed & Multitenancy, Miljøopsætning
    - **Labs 04-06: Opbygning af MCP Server** - Database Design & Schema, MCP Server Implementering, Værktøjsudvikling  
    - **Labs 07-09: Avancerede Funktioner** - Semantisk søgeintegration, Test & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Best Practices** - Implementeringsstrategier, Overvågning & Observabilitet, Best Practices & Optimering
  - **Enterprise Teknologier**: FastMCP framework, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avancerede Funktioner**: Row Level Security (RLS), semantisk søgning, multi-tenant dataadgang, vektorembeddings, realtidsmonitorering

#### Terminologistandardisering - Modul til Lab konvertering
- **Omfattende dokumentationsopdatering**: Systematisk opdateret alle README-filer i 11-MCPServerHandsOnLabs til at bruge "Lab" terminologi i stedet for "Modul"
  - **Sektionstitler**: Opdateret "What This Module Covers" til "What This Lab Covers" på tværs af alle 13 labs
  - **Indholdsbeskrivelse**: Ændret "This module provides..." til "This lab provides..." i hele dokumentationen
  - **Læringsmål**: Opdateret "By the end of this module..." til "By the end of this lab..."
  - **Navigation Links**: Konverteret alle "Module XX:" referencer til "Lab XX:" i krydsreferencer og navigation
  - **Færdiggørelsessporing**: Opdateret "After completing this module..." til "After completing this lab..."
  - **Bevarede tekniske referencer**: Opretholdt Python modulreferencer i konfigurationsfiler (f.eks. `"module": "mcp_server.main"`)

#### Studieguideforbedring (study_guide.md)
- **Visuelt Curriculum Kort**: Tilføjet nyt "11. Database Integration Labs" afsnit med omfattende visualisering af lab-struktur
- **Repository Struktur**: Opdateret fra ti til elleve hovedafsnit med detaljeret beskrivelse af 11-MCPServerHandsOnLabs
- **Læringsstivejledning**: Forbedret navigationsinstruktioner, der dækker sektioner 00-11
- **Teknologidækning**: Tilføjet FastMCP, PostgreSQL, Azure service integrationsdetaljer
- **Læringsresultater**: Fremhævet produktionklar serverudvikling, databaseintegrationsmønstre og virksomhedsikkerhed

#### Forbedring af hoved-README struktur
- **Lab-baseret terminologi**: Opdateret hoved-README.md i 11-MCPServerHandsOnLabs til konsekvent at bruge "Lab" struktur
- **Læringssti Organisering**: Klar progression fra grundlæggende koncepter gennem avanceret implementering til produktionsudrulning
- **Virkelighedsfokus**: Vægt på praktisk, hands-on læring med virksomhedsgrade mønstre og teknologier

### Dokumentationskvalitet & Konsistensforbedringer
- **Hands-On Læringsfokus**: Forstærket praktisk, labbaseret tilgang gennem dokumentationen
- **Enterprise Mønsterfokus**: Fremhævet produktionsklare implementeringer og virksomhedssikkerhedshensyn
- **Teknologiintegration**: Omfattende dækning af moderne Azure tjenester og AI integrationsmønstre
- **Læringsprogression**: Klar, struktureret sti fra grundlæggende koncepter til produktionsudrulning

## 26. september 2025

### Case Studier Forbedring - GitHub MCP Registry Integration

#### Case Studier (09-CaseStudy/) - Økosystem Udviklingsfokus
- **README.md**: Stor udvidelse med omfattende GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Ny omfattende case study, der undersøger GitHubs MCP Registry lancering i september 2025
    - **Problem Analyse**: Detaljeret gennemgang af fragmenterede MCP server opdagelses- og udrulningsudfordringer
    - **Løsningsarkitektur**: GitHubs centraliserede registry-tilgang med ét-klik VS Code installation
    - **Forretningsmæssig Impact**: Målbare forbedringer i udvikler onboarding og produktivitet
    - **Strategisk Værdi**: Fokus på modulær agentudrulning og tværværktøjs interoperabilitet
    - **Økosystem Udvikling**: Positionering som grundlæggende platform for agentintegration
  - **Forbedret Case Study Struktur**: Opdateret alle syv case studies med konsistent formatering og omfattende beskrivelser
    - Azure AI Travel Agents: Fokus på multi-agent orkestrering
    - Azure DevOps Integration: Workflow automatiseringsfokus
    - Realtids dokumenthentning: Python konsolklientimplementering
    - Interaktiv Studieplan Generator: Chainlit konversations-webapp
    - In-Editor Dokumentation: VS Code og GitHub Copilot integration
    - Azure API Management: Enterprise API integrationsmønstre
    - GitHub MCP Registry: Økosystemudvikling og community platform
  - **Omfattende Konklusion**: Omskrevet konklusionsafsnit, der fremhæver syv case studies, der spænder over flere MCP implementationsdimensioner
    - Enterprise Integration, Multi-Agent Orkestrering, Udviklerproduktivitet
    - Økosystem Udvikling, Uddannelsesapplikationer kategorisering
    - Forbedrede indsigter i arkitektur mønstre, implementeringsstrategier og best practices
    - Vægt på MCP som moden, produktionsklar protokol

#### Studieguideupdates (study_guide.md)
- **Visuelt Curriculum Kort**: Opdateret mindmap til at inkludere GitHub MCP Registry i Case Studies sektion
- **Case Study Beskrivelser**: Forbedret fra generiske beskrivelser til detaljeret gennemgang af syv omfattende case studies
- **Repository Struktur**: Opdateret sektion 10 til at afspejle omfattende case study dækning med specifikke implementeringsdetaljer
- **Changelog Integration**: Tilføjet 26. september 2025 post, der dokumenterer tilføjelsen af GitHub MCP Registry og case study forbedringer
- **Dato Opdateringer**: Opdateret fodertidspunkt til at afspejle seneste revision (26. september 2025)

### Dokumentationskvalitetsforbedringer
- **Konsistensforbedring**: Standardiseret case study formatering og struktur på tværs af alle syv eksempler
- **Omfattende Dækning**: Case studies spænder nu over virksomhed, udviklerproduktivitet og økosystemudviklingsscenarier
- **Strategisk Positionering**: Forbedret fokus på MCP som grundlæggende platform for agentbaseret systemudrulning
- **Ressourceintegration**: Opdateret yderligere ressourcer til at inkludere GitHub MCP Registry link

## 15. september 2025

### Udvidelse af Avancerede Emner - Egen Transports & Kontekst Engineering

#### MCP Egen Transports (05-AdvancedTopics/mcp-transport/) - Ny avanceret implementeringsguide
- **README.md**: Fuldstændig implementeringsguide for brugerdefinerede MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverless event-drevet transportimplementering
    - C#, TypeScript og Python eksempler med Azure Functions integration
    - Event-drevet arkitektur mønstre til skalerbare MCP løsninger
    - Webhook modtagere og push-baseret beskedhåndtering
  - **Azure Event Hubs Transport**: High-throughput streaming transportimplementering
    - Realtids streamingkapaciteter til lav-latens scenarier
    - Partitioneringsstrategier og checkpoint styring
    - Besked-samlings- og performanceoptimering
  - **Enterprise Integrationsmønstre**: Produktionsklare arkitektureksempler
    - Distribueret MCP behandling på tværs af flere Azure Functions
    - Hybrid transportarkitekturer, der kombinerer flere transporttyper
    - Beskedholdbarhed, pålidelighed og fejlhåndteringsstrategier
  - **Sikkerhed & Overvågning**: Azure Key Vault integration og observabilitetsmønstre
    - Managed identity autentificering og mindst privilegium adgang
    - Application Insights telemetri og performance overvågning
    - Circuit breakers og fejltolerance mønstre
  - **Test Frameworks**: Omfattende teststrategier for brugerdefinerede transports
    - Unit tests med testdoubles og mocking frameworks
    - Integrationstest med Azure Test Containers
    - Performance- og belastningstest overvejelser

#### Kontekst Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI disciplin
- **README.md**: Omfattende udforskning af kontekst engineering som et fremvoksende felt
  - **Kerneprincipper**: Fuld kontekstdeling, handlingsbeslutningsbevidsthed og kontekstvinduestyring

  - **MCP Protokoljustering**: Hvordan MCP-design adresserer udfordringer inden for kontekst-ingeniørarbejde  
    - Begrænsninger i kontekstvindue og progressive indlæsningsstrategier  
    - Relevansbestemmelse og dynamisk kontekstindhentning  
    - Multimodal konsteksthåndtering og sikkerhedsovervejelser  
  - **Implementeringsmetoder**: Enkelttrådet vs. multi-agent arkitekturer  
    - Kontekst-opdeling og prioriteringsteknikker  
    - Progressiv kontekstindlæsning og komprimeringsstrategier  
    - Lagdelt konteksttilgang og optimering af indhentning  
  - **Målerammeværk**: Fremvoksende metrikker til evaluering af konteksteffektivitet  
    - Inputeffektivitet, ydeevne, kvalitet og brugeroplevelses-overvejelser  
    - Eksperimentelle tilgange til kontekstoptimering  
    - Fejlanalyse og forbedringsmetodologier  

#### Opdateringer til pensumnavigation (README.md)  
- **Forbedret modulstruktur**: Opdateret pensumtabel med nye avancerede emner  
  - Tilføjet Context Engineering (5.14) og Custom Transport (5.15) poster  
  - Konsistent formatering og navigationslinks på tværs af alle moduler  
  - Opdaterede beskrivelser for at afspejle det aktuelle indholdsomfang  

### Forbedringer af mappe-struktur  
- **Navnestandardisering**: Omdøbte "mcp transport" til "mcp-transport" for konsistens med andre avancerede emne-mapper  
- **Indholdsorganisering**: Alle 05-AdvancedTopics mapper følger nu et ensartet navngivningsmønster (mcp-[emne])  

### Forbedringer i dokumentationskvalitet  
- **MCP specifikationsjustering**: Alt nyt indhold refererer til gældende MCP Specifikation 2025-06-18  
- **Eksempler på flere programmeringssprog**: Omfattende kodeeksempler i C#, TypeScript og Python  
- **Enterprise fokus**: Produktionsklare mønstre og Azure cloud-integration overalt  
- **Visuel dokumentation**: Mermaid-diagrammer til arkitektur- og flowvisualisering  

## 18. august 2025  

### Omfattende dokumentationsopdatering - MCP 2025-06-18 standarder  

#### MCP Sikkerhedspraksis (02-Security/) - Fuld modernisering  
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fuld omskrivning i overensstemmelse med MCP Specifikation 2025-06-18  
  - **Obligatoriske krav**: Tilføjet eksplicitte SKAL/IKKE SKAL krav fra officiel specifikation med tydelige visuelle markører  
  - **12 Kerne-sikkerhedspraksisser**: Omstruktureret fra 15-punkts liste til omfattende sikkerhedsdomaener  
    - Token-sikkerhed & godkendelse med ekstern identitetsudbyderintegration  
    - Sessionshåndtering & transportsikkerhed med kryptografiske krav  
    - AI-specifik trusselsbeskyttelse med Microsoft Prompt Shields-integration  
    - Adgangskontrol & tilladelser med princippet om mindst privilegium  
    - Indholdssikkerhed & overvågning med Azure Content Safety-integration  
    - Forsyningskædesikkerhed med omfattende komponentverifikation  
    - OAuth-sikkerhed & Confused Deputy-forebyggelse med PKCE-implementering  
    - Hændelsesrespons & genopretning med automatiserede kapabiliteter  
    - Overholdelse & governance med regulatorisk tilpasning  
    - Avancerede sikkerhedskontroller med zero trust-arkitektur  
    - Microsoft sikkerhedsøkoystem-integration med omfattende løsninger  
    - Kontinuerlig sikkerhedsevolution med adaptive praksisser  
  - **Microsoft sikkerhedsløsninger**: Forbedret integrationsvejledning til Prompt Shields, Azure Content Safety, Entra ID, og GitHub Advanced Security  
  - **Implementeringsressourcer**: Kategoriserede omfattende ressourcelinks efter Officiel MCP Dokumentation, Microsoft Sikkerhedsløsninger, Sikkerhedsstandarder og Implementeringsvejledninger  

#### Avancerede sikkerhedskontroller (02-Security/) - Enterprise implementering  
- **MCP-SECURITY-CONTROLS-2025.md**: Fuld overhaling med enterprise-kvalitets sikkerhedsrammeværk  
  - **9 omfattende sikkerhedsdomaener**: Udvidet fra grundlæggende kontroller til detaljeret enterprise-rammeværk  
    - Avanceret godkendelse & autorisation med Microsoft Entra ID integration  
    - Token-sikkerhed & anti-passthrough-kontroller med omfattende validering  
    - Sessionssikkerhedskontroller med hijacking-forebyggelse  
    - AI-specifikke sikkerhedskontroller med promptinjektions- og tool-forsvarsforanstaltninger  
    - Confused Deputy-angrebsforebyggelse med OAuth proxy-sikkerhed  
    - Tool-eksekveringssikkerhed med sandboxing og isolation  
    - Forsyningskæde-sikkerhedskontroller med afhængighedsverifikation  
    - Overvågnings- & detektionskontroller med SIEM-integration  
    - Hændelsesrespons & genopretning med automatiserede kapabiliteter  
  - **Implementeringseksempler**: Tilføjet detaljerede YAML-konfigurationsblokke og kodeeksempler  
  - **Microsoft-løsningsintegration**: Omfattende dækning af Azure sikkerhedstjenester, GitHub Advanced Security, og enterprise identitetsstyring  

#### Avancerede emner sikkerhed (05-AdvancedTopics/mcp-security/) - Produktionsklar implementering  
- **README.md**: Fuld omskrivning til enterprise sikkerhedsimplementering  
  - **Aktuel specifikationsjustering**: Opdateret til MCP Specifikation 2025-06-18 med obligatoriske sikkerhedskrav  
  - **Forbedret godkendelse**: Microsoft Entra ID-integration med omfattende .NET og Java Spring Security eksempler  
  - **AI sikkerhedsintegration**: Microsoft Prompt Shields og Azure Content Safety-implementering med detaljerede Python-eksempler  
  - **Avanceret trusselsafværgelse**: Omfattende implementeringseksempler for  
    - Confused Deputy-angrebsforebyggelse med PKCE og bruger samtykkevalidering  
    - Token Passthrough-forebyggelse med publikumsvalidering og sikker token-håndtering  
    - Session Hijacking-forebyggelse med kryptografisk binding og adfærdsanalyse  
  - **Enterprise sikkerhedsintegration**: Azure Application Insights overvågning, trusselsdetektionspipelines, og forsyningskædesikkerhed  
  - **Implementeringskontrolliste**: Klart adskilte obligatoriske vs. anbefalede sikkerhedskontroller med Microsoft sikkerhedsøkosystem-fordele  

### Dokumentationskvalitet & standardtilpasning  
- **Specifikationsreferencer**: Opdateret alle referencer til gældende MCP Specifikation 2025-06-18  
- **Microsoft sikkerhedsøkosystem**: Forbedret integrationsvejledning gennem hele sikkerhedsdokumentationen  
- **Praktisk implementering**: Tilføjet detaljerede kodeeksempler i .NET, Java og Python med enterprise mønstre  
- **Ressourceorganisering**: Omfattende kategorisering af officiel dokumentation, sikkerhedsstandarder og implementeringsvejledninger  
- **Visuelle indikatorer**: Klar markering af obligatoriske krav vs. anbefalede praksisser  


#### Kernekoncepter (01-CoreConcepts/) - Fuld modernisering  
- **Protokolversionsopdatering**: Opdateret til at referere til gældende MCP Specifikation 2025-06-18 med datobaseret versionsangivelse (ÅÅÅÅ-MM-DD format)  
- **Arkitekturforfining**: Forbedrede beskrivelser af Hosts, Klienter og Servere for at afspejle nuværende MCP arkitekturprincipper  
  - Hosts nu klart defineret som AI-applikationer, der koordinerer flere MCP klientforbindelser  
  - Klienter beskrevet som protokolforbindere, der opretholder en-til-en serverrelationer  
  - Servere forbedret med lokale vs. fjerndeploymentscenarier  
- **Primtivomstrukturering**: Fuld overhaling af server- og klientprimitive  
  - Serverprimitive: Ressourcer (datakilder), Prompter (skabeloner), Værktøjer (udførelsesfunktioner) med detaljerede forklaringer og eksempler  
  - Klientprimitive: Sampling (LLM fuldførelser), Elicitation (brugerinput), Logging (debugging/overvågning)  
  - Opdateret med aktuelle opdagelses- (`*/list`), indhentnings- (`*/get`), og udførelses- (`*/call`) mønstre  
- **Protokolarkitektur**: Introduceret to-lags arkitekturmodel  
  - Datalag: JSON-RPC 2.0 fundament med livscyklusstyring og primitive  
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer  
- **Sikkerhedsrammeværk**: Omfattende sikkerhedsprincipper inkl. eksplicit bruger-samtykke, databeskyttelse, værktøjseksekveringssikkerhed og transportsikkerhed  
- **Kommunikationsmønstre**: Opdaterede protokolbeskeder til at vise initialisering, opdagelse, udførelse og notifikationsflows  
- **Kodeeksempler**: Opfriskede flersprogede eksempler (.NET, Java, Python, JavaScript) for at afspejle nuværende MCP SDK-mønstre  

#### Sikkerhed (02-Security/) - Omfattende sikkerhedsomstrukturering  
- **Standardtilpasning**: Fuld overensstemmelse med MCP Specifikation 2025-06-18 sikkerhedskrav  
- **Godkendelsesevolution**: Dokumenteret udvikling fra brugerdefinerede OAuth-servere til ekstern identitetsudbyderdelegation (Microsoft Entra ID)  
- **AI-specifik trussel-analyse**: Forbedret dækning af moderne AI-angrebsmønstre  
  - Detaljerede promptinjektions-angrebsscenarier med virkelighedseksempler  
  - Tool-forgiftning mekanismer og "rug pull"-angrebsmønstre  
  - Korrumpering af kontekstvindue og modelleringsforvirringsangreb  
- **Microsoft AI sikkerhedsløsninger**: Omfattende dækning af Microsoft sikkerhedsøkosystem  
  - AI Prompt Shields med avanceret detektion, spotlighting og delimiter teknikker  
  - Azure Content Safety integrationsmønstre  
  - GitHub Advanced Security til forsyningskædebeskyttelse  
- **Avanceret trusselsafvænning**: Detaljerede sikkerhedskontroller for  
  - Sessionshijacking med MCP-specifikke angrebsscenarier og kryptografiske sessions-ID-krav  
  - Confused Deputy-problematikker i MCP proxy-scenarier med eksplicitte samtykkekrav  
  - Token passthrough-sårbarheder med obligatoriske valideringskontroller  
- **Forsyningskædesikkerhed**: Udvidet AI forsyningskædedækning inklusive foundation modeller, embeddings-services, kontekstleverandører og tredjeparts-API'er  
- **Foundation sikkerhed**: Forbedret integration med enterprise-sikkerhedspraksis inkl. zero trust arkitektur og Microsoft sikkerhedsøkosystem  
- **Ressourceorganisering**: Kategoriserede omfattende ressourcelinks efter type (Officielle docs, Standarder, Forskning, Microsoft-løsninger, Implementeringsvejledninger)  

### Forbedringer i dokumentationskvalitet  
- **Strukturerede læringsmål**: Forbedrede læringsmål med specifikke, handlingsrettede resultater  
- **Krydsreferencer**: Tilføjede links mellem relaterede sikkerheds- og kernekoncept-emner  
- **Aktuel information**: Opdaterede alle datasreferencer og specifikationslinks til gældende standarder  
- **Implementeringsvejledning**: Tilføjet specifikke, handlingsrettede implementeringsvejledninger på tværs af begge sektioner  

## 16. juli 2025  

### README og navigationsforbedringer  
- Fuldstændig redesignet pensumnavigation i README.md  
- Udskiftede `<details>` tags med mere tilgængeligt tabelbaseret format  
- Oprettede alternative layoutmuligheder i ny "alternative_layouts" mappe  
- Tilføjede kortbaserede, fanebaserede og accordion-stil navigationseksempler  
- Opdateret repositoriestruktur afsnit for at inkludere alle nyeste filer  
- Forbedret "How to Use This Curriculum" afsnit med klare anbefalinger  
- Opdaterede MCP specifikationslinks til korrekte URL'er  
- Tilføjede Context Engineering sektion (5.14) til pensumstruktur  

### Opdateringer til studievejledning  
- Fuldstændig revideret studievejledning for at tilpasse sig gældende repositorystruktur  
- Tilføjede nye sektioner for MCP Klienter og Værktøjer, samt Populære MCP Servere  
- Opdateret den visuelle pensumskort til nøjagtigt at afspejle alle emner  
- Forbedrede beskrivelser af Avancerede emner til at dække alle specialiserede områder  
- Opdateret Case Studies sektion for at reflektere faktiske eksempler  
- Tilføjede denne omfattende ændringslog  

### Fællesskabsbidrag (06-CommunityContributions/)  
- Tilføjede detaljerede oplysninger om MCP servere til billedgenerering  
- Tilføjede omfattende sektion om brug af Claude i VSCode  
- Tilføjede Cline terminalklient opsætnings- og brugsinstruktioner  
- Opdaterede MCP klientsektion til at inkludere alle populære klientmuligheder  
- Forbedrede bidragseksempler med mere præcise kodesamples  

### Avancerede emner (05-AdvancedTopics/)  
- Organiserede alle specialiserede emnemapper med ensartet navngivning  
- Tilføjede materialer og eksempler til kontekst-ingeniørarbejde  
- Tilføjede dokumentation for Foundry agent integration  
- Forbedrede dokumentationen for Entra ID sikkerhedsintegration  

## 11. juni 2025  

### Initial oprettelse  
- Udgav første version af MCP for Beginners pensum  
- Oprettede grundstruktur for alle 10 hovedsektioner  
- Implementerede visuelt pensumkort til navigation  
- Tilføjede indledende prøveprojekter i flere programmeringssprog  

### Kom godt i gang (03-GettingStarted/)  
- Oprettede første serverimplementeringseksempler  
- Tilføjede vejledning til klientudvikling  
- Inkluderede LLM klientintegrationsinstruktioner  
- Tilføjede dokumentation for VS Code integration  
- Implementerede Server-Sent Events (SSE) servereksempler  

### Kernekoncepter (01-CoreConcepts/)  
- Tilføjede detaljeret forklaring af klient-server arkitektur  
- Oprettede dokumentation om nøgleprotokolkomponenter  
- Dokumenterede beskedmønstre i MCP  

## 23. maj 2025  

### Repository-struktur  
- Initialiserede repository med grundlæggende mappestruktur  
- Oprettede README-filer for hver hovedsektion  
- Satte oversættelsesinfrastruktur op  
- Tilføjede billedmateriale og diagrammer  

### Dokumentation  
- Oprettede indledende README.md med oversigt over pensum  
- Tilføjede CODE_OF_CONDUCT.md og SECURITY.md  
- Satte SUPPORT.md op med vejledning til at få hjælp  
- Oprettede foreløbig studievejledningsstruktur  

## 15. april 2025  

### Planlægning og rammeværk  
- Indledende planlægning for MCP for Beginners pensum  
- Definerede læringsmål og målgruppe  
- Skitserede 10-sektions struktur for pensum  
- Udviklede konceptuelt rammeværk for eksempler og case-studier  
- Oprettede indledende prototypeeksempler for nøglekoncepter  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
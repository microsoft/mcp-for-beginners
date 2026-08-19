# Endringslogg: MCP for Nybegynnere Pensum

Dette dokumentet fungerer som en oversikt over alle vesentlige endringer gjort i Model Context Protocol (MCP) for Nybegynnere pensum. Endringene dokumenteres i omvendt kronologisk rekkefølge (nyeste endringer først).

## 29. juli 2026

### Ny modulkamerat 08: Pålitelige sidecars og sikre forsøk på nytt

Lagt til en leverandørnøytral kamerat-leksjon for MCP-verktøy som skaper virkelige
effekter, tilpasset den endelige `2026-07-28` spesifikasjonen.

- **Ny**: [kamerat-leksjonen for pålitelighetssidecar][reliability-sidecar]
  bruker én støtte-sak-historie, to Mermaid-diagrammer, og et beslutnings-
  flyt for gjenforsøk for å forklare stabile operasjonsnøkler, atomisk duplikat-
  opptak, forsoning, bevis, og grensen for Tasks-utvidelsen.
- **Ny**: En standardbibliotek Python og SQLite feilinjiseringsøvelse
  bruker separate operasjons- og saksbutikker for å demonstrere et svar som går tapt
  etter at en ekstern effekt har bekreftet. Seks deterministiske tester dekker naive
  duplikater, beskyttet gjenoppretting ved omstart, konflikt i nyttelast,
  bufrede resultater, aktive krav, og samtidig duplikatopptak.
- **Oppdatert**: Modul 08 kobler nå til kamerat-leksjonen, identifiserer
  den endelige `2026-07-28` stateless forespørselsmodellen, skiller OpenTelemetry
  observabilitet fra den utfasede MCP logging-funksjonen, og begrenser
  det generiske gjenforsøk-eksempelet til leseoperasjoner.
- **Valgfritt**: Leksjonen kartlegger sine portable konsepter til én merket fellesskaps-
  implementering uten å gjøre den hostede tjenesten eller et nettverkskall til
  del av øvelsen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. juli 2026

### Ny leksjon: 2026-07-28 MCP Spesifikasjons Release Candidate

Lagt til dekning av den kommende `2026-07-28` MCP spesifikasjons release candidate (annonsert 21. mai 2026; endelig utgivelse planlagt 28. juli 2026), oppsummert fra [den offisielle kunngjøringsbloggen](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Pensumets basis forblir **MCP Spesifikasjon 2025-11-25** til den nye versjonen lanseres, så dette presenteres som fremtidsrettet veiledning fremfor omskriving av eksisterende leksjoner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — en fullstendig leksjon som dekker den stateless protokollkjernen (fjerning av `initialize` håndtrykk og `Mcp-Session-Id`), de nye `Mcp-Method`/`Mcp-Name` rutingshodene, `ttlMs`/`cacheScope` cache-metadatainformasjon, W3C Trace Context i `_meta`, det formelle utvidelsesrammeverket (MCP Apps og den nye Tasks-utvidelsen), seks autorisasjonsharding SEPer, utfasing av Roots/Sampling/Logging, og overgangen til full JSON Schema 2020-12 for verktøy-skjemadefinisjoner.
- **Oppdatert** med fremtidsrettede henvisninger til ny leksjon:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollversjonsnotat, Sampling/Roots/Logging/Tasks seksjoner, og "Hva er neste"
  - [02-Security/README.md](./02-Security/README.md): autorisasjonsharding henvisning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport henvisning
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling utfasing henvisning
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging utfasing og Tasks-utvidelse henvisning
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-ruting henvisning
  - [README.md](./README.md): "Ser fremover" notat i spesifikasjonsseksjonen og en ny `1.1` oppføring i modultabellen
  - [study_guide.md](./study_guide.md): fremtidsrettet kulepunkt under Core Concepts oversikt og et datert tillegg
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): henvisning om `mcp-session-id` transportkart foran den stateless forespørselsmodellen
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduloversikt henvisning om utfasing av Root Contexts/Sampling og Tasks-utvidelsen
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisasjonsharding henvisning

## 24. juni 2026

### Ny leksjon: Bruke MCP i Copilot-app

- [Verktøyseksjon](./12-tooling/README.md) Lagt til verktøyseksjon.
- [MCP i Copilot-app](./12-tooling/01-copilot-app/README.md)

## 16. juni 2026

### MCP Spesifikasjonsjustering & Eksempelsvalidering

Validerte pensum mot gjeldende **MCP Spesifikasjon 2025-11-25** og de nyeste offisielle SDKene, korrigerte deretter gjenværende utdaterte spesifikasjonsreferanser, og bekreftet at kjerneeksemplene fortsatt bygger og kjører.

#### Spesifikasjonsversjonskorrigeringer (2025-06-18 / 2025-03-26 → 2025-11-25)

Oppdatert engelsk innhold der det fortsatt hevdet at en eldre spesifikasjonsrevisjon var *nåværende/siste* standard, og omdirigerte lenker til de kanoniske `modelcontextprotocol.io` spesifikasjonsbanene:
- **05-AdvancedTopics/mcp-security/README.md**: Oppdaterte "Nåværende Standard" banner, introduksjon, kjerneprinsipper for sikkerhet overskrift, obligatorisk krav-overskrift, Microsoft Entra ID seksjon, Referanser & Ressurser lenker, og avsluttende sikkerhetsmelding (8 referanser) til 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Oppdaterte Ytterligere Ressurser spesifikasjonslenke og "Nåværende Standard" banner til 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Erstatter den utdaterte `2025-03-26` sikkerhets-og-pålitelighets lenken med gjeldende 2025-11-25 beste praksis side for sikkerhet
- **03-GettingStarted/14-sampling/README.md**: Oppdaterte den offisielle sampling-dokumentasjonslenken til 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Oppdaterte nåværende tid referanse til "nåværende MCP spesifikasjon" og Ytterligere Ressurser spesifikasjonslenke til 2025-11-25 (historiske SSE-utfasingsnotater beholdt for nøyaktighet)

#### Eksempelsvalidering mot gjeldende SDKer

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` løste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` bestod uten typefeil — eksisterende `McpServer`/`StdioServerTransport` APIer forblir gyldige
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validert i et isolert `.venv` med `mcp[cli]` (1.27.2); `py_compile` bestod og `FastMCP.list_tools()` returnerte korrekt verktøyene `add` og `subtract`
- Bekreftet at alle eksempels `@modelcontextprotocol/sdk` versjonsområder (`>=1.26.0` / `^1.26.0` / `^1.27.0`) løser seg rent til nåværende `1.29.0` uten API-brytende endringer

#### Avhengighets-pin Justering (lukker versjonsgap)

Oppdatert utdaterte SDK pinner slik at hvert eksempel følger nåværende MCP-utgivelse, i samsvar med repoets konvensjon:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Oppgradert `@modelcontextprotocol/sdk` fra `^1.8.0` → `>=1.26.0` og oppdaterte den utdaterte `"oppdatert for MCP 2025-06-18"` pakkebeskrivelse til `"justert til MCP Spesifikasjon 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** og **lab4/code/github_mcp_server/pyproject.toml**: Oppgradert nøyaktig pin `mcp==1.23.0` → `mcp>=1.26.0`; regenererte begge `uv.lock` filene (`uv lock`) slik at lockfilene løser til nåværende `mcp 1.27.2` og holder seg synkronisert med manifestene

#### Pensum Gap-analyse — Siste Spesifikasjonsfunksjonsdekning

Verifisert at pensum allerede dekker alle primitive som er introdusert/utvidet i MCP 2025-11-25, så ingen innholdsgap gjenstår:
- **Sampling**: Leksjon 03-GettingStarted/14-sampling pluss 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-modus)**: Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentert i 00-Introduction, 01-CoreConcepts, og 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentell, langvarige operasjoner)**: Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Verktøyannotasjoner** (`readOnlyHint` / `destructiveHint`): Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features

### Sikkerhetsharding & Avhengighets-sårbarhetsutbedring

Kjørte en full sikkerhetsrunde over alle avhengighetsmanifest og eksempel-kildekode, deretter utbedret alle rapporterte npm rådgivninger og én kode-nivå funn. Etter utbedring rapporterer `npm audit` **0 sårbarheter** i alle auditert kataloger.

#### npm Avhengighetssårbarheter (transitive) — Fikset

Reviderte alle 15 innsendte `package-lock.json` filer. Sårbarheter var begrenset til transitive avhengigheter hentet av MCP Inspector dev-verktøy, OpenAI klienten, og MCP SDK; alle er nå løst uten å bryte eksemplene:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** og **lab3/code/weather_mcp/inspector**: Oppgradert `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), som fjernet de inkluderte `ajv`, `brace-expansion`, `diff`, `path-to-regexp` og `ws` rådgivningene. Lagt til en npm `overrides` oppføring som tvinger patched `shell-quote@1.8.4` for å eliminere den gjenværende kritiske rådgivningen båret av `concurrently`; regenerert begge lockfilene (nå 0 sårbarheter)
- **03-GettingStarted/samples/typescript**: `npm audit fix` oppdaterte den transitive `qs` (moderat) til en patched utgivelse
- **03-GettingStarted/samples/javascript**: `npm audit fix` oppdaterte den transitive `hono` (moderat) til en patched utgivelse
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` oppdaterte den transitive `form-data` (høy) til en patched utgivelse
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generert manglende `package-lock.json` for å gjøre prosjektet reproduserbart og auditert (0 sårbarheter)

#### Kode-nivå sikkerhetsfiksering (OWASP A03: Injeksjon)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Fjernet `shell=True` fra `open_in_vscode` verktøyet. Det tidligere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillot shell-metategn i en mappesti å tolkes av `cmd.exe` (kommando-injeksjonsvektor). Det starter nå den løste `Code.exe` direkte med mappen som argument — ingen shell — som er funksjonelt ekvivalent og trygt

#### Python Avhengighetsrevisjon

- Revidert alle Python kravsett med `pip-audit`. `05-AdvancedTopics` og `03-GettingStarted/samples/python` rapporterte **ingen kjente sårbarheter** (deres `mcp` / `httpx` / `pydantic` / `python-dotenv` områder løser til nåværende patched utgivelser)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` markerte den transitive avhengigheten **`werkzeug` 3.1.1** med tre `safe_join` Windows device-navn DoS rådgivninger — `CVE-2025-66221`, `CVE-2026-21860`, og `CVE-2026-27199` (alle fikset i 3.1.6). Lagt til eksplisitt sikkerhetspinning `werkzeug>=3.1.6` slik at patched utgivelsen løses; verifisert at begrensningen løser rent med `chainlit` / `mcp` / `semantic-kernel` stacken

### Produktnavn Rebranding

Oppdatert alt pensuminhold for å reflektere Microsofts produktrebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Oppdatert Discord-fellesskapslenke

- **AGENTS.md**: Oppdatert referanse til Discord-server
- **README.md**: Oppdaterte referanser til teknologiekosystemet
- **study_guide.md**: Oppdaterte case study-referanser
- **05-AdvancedTopics/README.md**: Oppdatert Modul 5.13 tittel og beskrivelse
- **05-AdvancedTopics/mcp-integration/README.md**: Oppdatert seksjonsoverskrift og beskrivelse
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Full modul tittel og innholdsoppdatering
- **05-AdvancedTopics/mcp-security-entra/README.md**: Oppdatert kryssreferanselenke
- **07-LessonsfromEarlyAdoption/README.md**: Oppdaterte case study-referanser
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Oppdatert Seksjon 9 overskrift, merker og kapasiteter
- **08-BestPractices/README.md**: Oppdatert Discord-fellesskapslenke
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Oppdatert Discord-kanalreferanse
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Oppdatert modellutrullingsreferanse
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Oppdatert AI Services-tabell
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Oppdaterte ressursreferanser

#### AI Toolkit / AITK → Microsoft Foundry Toolkit-utvidelse for VS Code
- **README.md**: Oppdaterte hovedpensumreferanser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Oppdatert modultittel, oversikt og alle moduloverskrifter
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Oppdatert tittel, læringsmål, oppsettinstruksjoner og ressurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Oppdatert tittel, læringsmål, MCP-verts tabell og kryssreferanser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Oppdatert tittel, merker, forutsetninger og ressurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Oppdaterte Agent Builder-referanser og tilbakemeldingslenke
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Oppdaterte forutsetninger og utvidelsesreferanser

---

## 11. april 2026

### Nytt undervisningstilbud, dokumentasjonsfikser og avhengighetsoppdateringer

#### Nytt pensuminnhold lagt til

**Modul 05 - Avanserte emner**
- **Leksjon 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende veiledning som dekker det adversariale debattmønsteret for multi-agent systemer
  - Mermaid arkitekturdiagram: to agenter → delt MCP-server → debatttranskripsjon → dommer → dom
  - Delt MCP verktøyserver (`web_search` + `run_python`) implementert i Python og TypeScript
  - Motstridende systemoppfordringer (FOR / IMOT / Dommer) med eksplisitte krav til verktøybruk
  - Debattorchestrator i Python, TypeScript, og C# som styrer runder og ruter argumenter
  - MCP `ClientSession`-wiring for orchestratoren til ekte verktøykall
  - Brukstilfelletabell (hallusinasjonsdeteksjon, trusselmodellering, API-designgjennomgang, faktasjekk, teknologivalg)
  - Sikkerhetshensyn: sandbokseksekvering, verktøykallvalidering, begrensning av hastighet, revisjonslogging
  - Strukturert øvelse med tre praktiske scenarier (kodegjennomgang, arkitekturbeslutning, innholdmoderering)

#### Dokumentasjonsfikser

**Modul 03 - Komme i gang**
- **05-stdio-server/README.md**: Rettet ufullstendig eksempel på TypeScript stdio-server — la til manglende transportinstansiering (`new StdioServerTransport()`) og `server.connect(transport)` kall for å matche Python- og .NET-eksemplene i samme seksjon
- **14-sampling/README.md**: Rettet skrivefeil — korrigert `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Pensumoppdateringer

**Hoved README.md**
- La til oppføring 5.17 (Adversarial Multi-Agent Reasoning med MCP) i pensumtabell med direkte lenke til ny leksjon

**05-AdvancedTopics/README.md**
- La til rad for Leksjon 5.17 i leksjonstabellen

**study_guide.md**
- La til Adversarial Multi-Agent Reasoning-emnet i tankekart og tekstbeskrivelse av Avanserte emner

#### Kode- og sikkerhetsfikser

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sikkerhetsfiks — kommandoinjeksjon**: Erstattet `execSync` shell-interpolasjon med `execFile` + `promisify` i TypeScript `run_python`-verktøyet, fjernet kommandoinjeksjonssårbarhet (LLM-kontrollert kode sendes nå som et litteralt argv-element uten shell-involvering)
- **MCP verktøysløyfe-wiring**: Oppdatert Python debate orchestrator til å bruke `AsyncAnthropic` klient (erstatter blokkerende sync `Anthropic`), sende en live `ClientSession` direkte til hver agents tur, hente verktøydefinisjoner via `session.list_tools()` hver tur, og sende `tool_use`-blokker via `session.call_tool()` i en løkke til modellen gir et endelig tekstsvar

#### Avhengighetsoppdateringer

- Oppgradert `hono` til 4.12.12 på tvers av flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Oppgradert `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript-pakker
- Oppgradert `cryptography` fra 46.0.5 til 46.0.7 i Python-pakker (10-StreamliningAIWorkflows lab 3 og 4)
- Oppgradert `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspektør

#### Oversettelser

- Synkroniserte oversettelser for 48+ språk med siste kildeendringer (i18n-oppdatering)

---

## 5. februar 2026

### Repositorie-omfattende validerings- og navigasjonsforbedringer

#### Nytt pensuminnhold lagt til

**Modul 03 - Komme i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide for oppsett av MCP-verter
  - Konfigurasjonseksempler for Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-konfigurasjonsmaler for alle større verter
  - Sammenligningstabell for transporttyper (stdio, SSE/HTTP, WebSocket)
  - Feilsøking av vanlige tilkoblingsproblemer
  - Sikkerhetsbeste praksis for vertskonfigurasjon

- **13-mcp-inspector/README.md**: Ny feilsøkingsguide for MCP Inspector
  - Installasjonsmetoder (npx, npm global, fra kilde)
  - Tilkobling til servere via stdio og HTTP/SSE
  - Testing av verktøy, ressurser og prompt-arbeidsflyter
  - VS Code-integrasjon med MCP Inspector
  - Vanlige feilsøkingsscenarioer med løsninger

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guide for implementering av paginering
  - Cursor-baserte pagineringsmønstre i Python, TypeScript, Java
  - Paginering behandlet på klientsiden
  - Cursor designstrategier (opakt vs strukturert)
  - Anbefalinger for ytelsesoptimalisering

**Modul 05 - Avanserte emner**
- **mcp-protocol-features/README.md**: Ny dybdedokumentasjon om protokollfunksjoner
  - Implementering av fremdriftsvarsler
  - Mønstre for avbestilling av forespørsler
  - Ressursmaler med URI-mønstre
  - Administrasjon av serverens livssyklus
  - Kontroll av loggnivåer
  - Feilhåndteringsmønstre med JSON-RPC-koder

#### Navigasjonsfikser (24+ filer oppdatert)

**Hovedmodul-README-er**
 Nå lenker til både første leksjon OG neste modul

**02-Security underfiler**
- Alle 5 ekstra sikkerhetsdokumenter har nå "Hva er neste" navigasjon:

**09-CaseStudy filer**
- Alle case-studiefiler har nå sekvensiell navigasjon:

**10-StreamliningAI Labs**
La til Hva er neste-seksjon i Modul 10 oversikt og Modul 11

#### Kode- og innholdsoppdateringer

**SDK- og avhengighetsoppdateringer**
Rettet tom openai-versjon til `^4.95.0`
Oppdatert SDK fra `^1.8.0` til `>=1.26.0`
Oppdatert MCP versjonspinner til `>=1.26.0`

**Kodefikser**
Rettet ugyldig modell `gpt-4o-mini` til `gpt-4.1-mini`

**Innholdsrettelser**
Rettet ødelagt lenke `READMEmd` → `README.md`, rettet pensumoverskrift `Module 1-3` → `Module 0-3`, rettet stifølsom bane
Fjernet korrupte duplikater av Case Study 5-innhold

**Begynnerveiledningsforbedringer**
La til korrekt introduksjon, læringsmål og forutsetninger for nybegynnere

#### Pensumoppdateringer

**Hoved README.md**
- La til oppføringer 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protokollfunksjoner) i pensumtabell

**Modul-README-er**
La til leksjonene 12 og 13 i leksjonsliste
La til Praktiske guider-seksjon med pagineringslenke
La til leksjonene 5.15 (Egendefinert transport) og 5.16 (Protokollfunksjoner)

**study_guide.md**
- Oppdatert tankekart med alle nye emner: MCP Hosts-oppsett, MCP Inspector, Pagineringstrategier, Protokollfunksjoner dybdeanalyse

## 28. jan 2026

### MCP Spesifikasjon 2025-11-25 Samsvarsrevisjon

#### Kjernetema-forbedring (01-CoreConcepts/)
- **Ny klientprimitiv - Roots**: La til omfattende dokumentasjon om Roots-klientprimitiven, som gjør at servere kan forstå filsystemsgrenser og tilgangstillatelser
- **Verktøyannotasjoner**: La til dokumentasjon om verktøys adferdsannotasjoner (`readOnlyHint`, `destructiveHint`) for bedre beslutninger om verktøykjøring
- **Verktøykall i Sampling**: Oppdatert Sampling-dokumentasjonen med `tools` og `toolChoice` parametere for modellstyrte verktøykall under sampling-forespørsler
- **URL-modus fremkalling**: La til dokumentasjon om URL-basert fremkalling for serverinitierte eksterne webinteraksjoner
- **Oppgaver (Eksperimentelle)**: La til ny seksjon som dokumenterer eksperimentelle Oppgaver-funksjonalitet for holdbare utførelsesinnpakninger og utsatt resultatinnhenting
- **Ikonstøtte**: Notert at verktøy, ressurser, ressursmaler og prompts nå kan inkludere ikoner som tilleggmetadata

#### Dokumentasjonsoppdateringer
- **README.md**: La til MCP Spesifikasjon 2025-11-25 versjonsreferanse og dato-basert versjonsstyring forklaring
- **study_guide.md**: Oppdatert pensumkart for å inkludere Oppgaver og Verktøyannotasjoner i Kjernetema-seksjonen; oppdatert dokumenttidspunkt

#### Samsvarsvurdering med spesifikasjon
- **Protokollversjon**: Verifisert at all dokumentasjon refererer til gjeldende MCP Spesifikasjon 2025-11-25
- **Arkitekturtilpasning**: Bekreftet nøyaktighet i dokumentasjon av to-lags arkitektur (Data Layer + Transport Layer)
- **Primitiver Dokumentasjon**: Validert serverprimitiver (Ressurser, Prompts, Verktøy) og klientprimitiver (Sampling, Fremkalling, Logging, Roots)
- **Transportmekanismer**: Verifisert nøyaktighet i stdio og Streamable HTTP-transport dokumentasjon
- **Sikkerhetsretningslinjer**: Bekreftet samsvar med gjeldende MCP Sikkerhetsbeste praksiser dokumentasjon

#### Viktige MCP 2025-11-25 funksjoner dokumentert
- **OpenID Connect Discovery**: Autentiseringsserver discovery via OIDC
- **OAuth Client ID Metadata Dokumenter**: Anbefalt klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skjemadefinisjoner
- **SDK Lagdelingssystem**: Formaliserte krav til SDK funksjonsstøtte og vedlikehold
- **Styringsstruktur**: Formaliserte arbeidsgrupper og interessegrupper i MCP-styring

### Stor oppdatering av sikkerhetsdokumentasjon (02-Security/)

#### MCP Security Summit Workshop (Sherpa) integrasjon
- **Nytt praktisk treningsressurs**: La til omfattende integrasjon med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all sikkerhetsdokumentasjon
- **Dekning av ekspedisjonsrute**: Dokumentert full progresjon leir-til-leir fra Base Camp til Summit
- **OWASP-tilpasning**: All sikkerhetsveiledning koblet til OWASP MCP Azure Security Guide-risikoer

#### OWASP MCP Topp 10 integrasjon
- **Ny seksjon**: La til OWASP MCP Topp 10 sikkerhetsrisikotabell med Azure avbøtninger i hoved Sikkerhets README
- **Risiko-basert dokumentasjon**: Oppdatert mcp-security-controls-2025.md med OWASP MCP risikoreferanser for hver sikkerhetsdomene
- **Referansearkitektur**: Lenket til OWASP MCP Azure Security Guide referansearkitektur og implementeringsmønstre

#### Oppdaterte sikkerhetsfiler
- **README.md**: La til Sherpa Workshop oversikt, ekspedisjonsrutetabell, OWASP MCP Topp 10 risikooppsummering og praktisk treningsseksjon
- **mcp-security-controls-2025.md**: Oppdatert overskrift til februar 2026, lagt til OWASP risikoreferanser (MCP01-MCP08), rettet inkonsekvent spesifikasjonsversjon
- **mcp-security-best-practices-2025.md**: La til Sherpa og OWASP ressurser seksjon, oppdatert tidsstempel
- **mcp-best-practices.md**: La til praktisk treningsseksjon med Sherpa og OWASP lenker
- **azure-content-safety-implementation.md**: La til OWASP MCP06-referanse, Sherpa Camp 3-tilpasning og tillegg av ressursseksjon

#### Nye ressurslenker lagt til
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP risikosider (MCP01-MCP10)

### Pensum-omfattende MCP-spesifikasjon 2025-11-25 justering

#### Modul 03 - Komme i gang
- **SDK-dokumentasjon**: Lagt til Go SDK til offisiell SDK-liste; oppdatert alle SDK-referanser for å samsvare med MCP-spesifikasjon 2025-11-25
- **Transportavklaring**: Oppdatert STDIO- og HTTP Streaming transportbeskrivelser med eksplisitte spesifikasjonsreferanser

#### Modul 04 - Praktisk implementering
- **SDK-oppdateringer**: Lagt til Go SDK; oppdatert SDK-liste med spesifikasjonsversjonsreferanse
- **Autorisasjonsspesifikasjon**: Oppdatert MCP autorisasjonsspesifikasjonslenke til gjeldende versjon 2025-11-25

#### Modul 05 - Avanserte emner
- **Nye funksjoner**: Lagt til notat om nye MCP-spesifikasjonsfunksjoner 2025-11-25 (Oppgaver, Verktøyannotasjoner, URL-modusinnhenting, Røtter)
- **Sikkerhetsressurser**: Lagt til OWASP MCP Top 10 og Sherpa verkstedslenker til tilleggskilder

#### Modul 06 - Fellesskapsbidrag
- **SDK-liste**: Lagt til Swift og Rust SDKer; oppdatert spesifikasjonslenke til 2025-11-25
- **Spesifikasjonsreferanse**: Oppdatert MCP Spesifikasjonslenke til direkte spesifikasjons-URL

#### Modul 07 - Erfaringer fra tidlig adopsjon
- **Ressursoppdateringer**: Lagt til MCP Spesifikasjon 2025-11-25-lenke og OWASP MCP Top 10 til tilleggskilder

#### Modul 08 - Beste praksis
- **Spesifikasjonsversjon**: Oppdatert MCP Spesifikasjonsreferanse til 2025-11-25
- **Sikkerhetsressurser**: Lagt til OWASP MCP Top 10 og Sherpa verksted til tilleggskilder

#### Modul 10 - Effektivisering av AI-arbeidsflyter
- **Merkesoppdatering**: Endret MCP-versjonsmerke fra SDK-versjon (1.9.3) til spesifikasjonsversjon (2025-11-25)
- **Ressurslenker**: Oppdatert MCP Spesifikasjonslenke; lagt til OWASP MCP Top 10

#### Modul 11 - Praktiske MCP-server-laboratorier
- **Spesifikasjonsreferanse**: Oppdatert MCP Spesifikasjonslenke til versjon 2025-11-25
- **Sikkerhetsressurser**: Lagt til OWASP MCP Top 10 i offisielle ressurser

## 18. desember 2025

### Oppdatering av sikkerhetsdokumentasjon - MCP spesifikasjon 2025-11-25

#### MCP Sikkerhets Beste Praksis (02-Security/mcp-best-practices.md) - Versjonsoppdatering spesifikasjon
- **Protokollversjonsoppdatering**: Oppdatert til å referere til siste MCP spesifikasjon 2025-11-25 (utgitt 25. november 2025)
  - Oppdatert alle spesifikasjonsversjonsreferanser fra 2025-06-18 til 2025-11-25
  - Oppdatert dokumentets datoreferanser fra 18. august 2025 til 18. desember 2025
  - Verifisert at alle spesifikasjons-URL-er peker til gjeldende dokumentasjon
- **Innholdsvalidering**: Omfattende validering av sikkerhetsbeste praksis mot de nyeste standardene
  - **Microsoft Sikkerhetsløsninger**: Verifisert nåværende terminologi og lenker for Prompt Shields (tidligere "Jailbreak risikooppdagelse"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Sikkerhet**: Bekreftet samsvar med nyeste OAuth sikkerhetsbeste praksis
  - **OWASP-standarder**: Validert OWASP Top 10 for LLMs-referanser opprettholdes aktuelle
  - **Azure-tjenester**: Verifisert alle Microsoft Azure dokumentasjonslenker og beste praksis
- **Standardjustering**: Alle refererte sikkerhetsstandarder bekreftet oppdaterte
  - NIST AI Risikostyringsrammeverk
  - ISO 27001:2022
  - OAuth 2.1 Sikkerhets beste praksis
  - Azure sikkerhets- og samsvarsrammeverk
- **Implementeringsressurser**: Verifisert alle implementeringsveiledningslenker og ressurser
  - Azure API Management autentiseringsmønstre
  - Microsoft Entra ID integrasjonsguider
  - Azure Key Vault hemmelighetshåndtering
  - DevSecOps pipelines og overvåkingsløsninger

### Dokumentasjons kvalitetskontroll
- **Spesifikasjonsoverholdelse**: Sikret at alle obligatoriske MCP sikkerhetskrav (MÅ/MÅ IKKE) samsvarer med siste spesifikasjon
- **Ressursaktualitet**: Verifisert alle eksterne lenker til Microsoft dokumentasjon, sikkerhetsstandarder og implementeringsguider
- **Dekning av beste praksis**: Bekreftet omfattende dekning av autentisering, autorisasjon, AI-spesifikke trusler, forsyningskjedesikkerhet og bedriftsmønstre

## 6. oktober 2025

### Utvidelse av Komme i gang-seksjon – Avansert serverbruk & Enkel autentisering

#### Avansert serverbruk (03-GettingStarted/10-advanced)
- **Nytt kapittel lagt til**: Introdusert en omfattende veiledning om avansert MCP serverbruk, som dekker både regulære og lavnivå serverarkitekturer.
  - **Regulær vs. lavnivå server**: Detaljert sammenligning og kodeeksempler i Python og TypeScript for begge tilnærmingene.
  - **Handler-basert design**: Forklaring om handler-basert verktøy/ressurs/prompt-administrasjon for skalerbare, fleksible serverimplementeringer.
  - **Praktiske mønstre**: Virkelige scenarier der lavnivå servermønstre er fordelaktige for avanserte funksjoner og arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapittel lagt til**: Trinnvis veiledning for implementering av enkel autentisering i MCP-servere.
  - **Autentiseringskonsepter**: Klar forklaring av autentisering vs. autorisasjon, og credential-håndtering.
  - **Grunnleggende autentisering**: Middleware-baserte autentiseringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
  - **Overgang til avansert sikkerhet**: Veiledning om å starte med enkel auth og videre til OAuth 2.1 og RBAC, med referanser til avanserte sikkerhetsmoduler.

Disse tilleggene gir praktisk, hands-on veiledning for å bygge mer robuste, sikre og fleksible MCP-serverimplementeringer, som brobygger grunnleggende konsepter med avanserte produksjonsmønstre.

## 29. september 2025

### MCP Server Databaseintegreringslaboratorier - Omfattende praktisk læringsløp

#### 11-MCPServerHandsOnLabs - Ny komplett databaseintegreringspensum
- **Fullstendig 13-lab læringsløp**: Lagt til omfattende praktisk pensum for bygging av produksjonsklare MCP-servere med PostgreSQL databaseintegrasjon
  - **Virkelig implementering**: Zava Retail analysebrukstilfelle som demonstrerer bedriftsnivå mønstre
  - **Strukturert læringsprogresjon**:
    - **Laboratorier 00-03: Grunnlag** - Introduksjon, kjernearkitektur, sikkerhet & multi-leietakertilpasning, miljøoppsett
    - **Laboratorier 04-06: Bygging av MCP-serveren** - Databasedesign & skjema, MCP serverimplementasjon, verktøyutvikling  
    - **Laboratorier 07-09: Avanserte funksjoner** - Semantisk søkintegrasjon, testing & feilsøking, VS Code-integrasjon
    - **Laboratorier 10-12: Produksjon & beste praksis** - Distribusjonsstrategier, overvåking & observabilitet, beste praksis & optimalisering
  - **Bedriftsteknologier**: FastMCP-rammeverk, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avanserte funksjoner**: Row Level Security (RLS), semantisk søk, flerleietaker datatilgang, vektor-embeddings, sanntidsovervåkning

#### Terminologistandardisering - Modul til lab-konvertering
- **Omfattende dokumentasjonsoppdatering**: Systematisk oppdatert alle README-filer i 11-MCPServerHandsOnLabs til å bruke "Lab"-terminologi i stedet for "Modul"
  - **Seksjonsoverskrifter**: Oppdatert "Hva denne modulen dekker" til "Hva dette laboratoriet dekker" i alle 13 laboratorier
  - **Innholdsbeskrivelse**: Endret "Denne modulen gir..." til "Dette laboratoriet gir..." gjennom all dokumentasjon
  - **Læringsmål**: Oppdatert "Ved slutten av denne modulen..." til "Ved slutten av dette laboratoriet..."
  - **Navigasjonslenker**: Konvertert alle "Modul XX:" referanser til "Lab XX:" i kryssreferanser og navigasjon
  - **Fremdriftssporing**: Oppdatert "Etter å ha fullført denne modulen..." til "Etter å ha fullført dette laboratoriet..."
  - **Bevarte tekniske referanser**: Opprettholdt Python modulreferanser i konfigurasjonsfiler (f.eks., `"module": "mcp_server.main"`)

#### Studieguideforbedring (study_guide.md)
- **Visuelt pensumkart**: Lagt til ny "11. Databaseintegreringslaboratorier" seksjon med omfattende visualisering av labstruktur
- **Depotstruktur**: Oppdatert fra ti til elleve hovedseksjoner med detaljert beskrivelse av 11-MCPServerHandsOnLabs
- **Læringsløpsveiledning**: Forbedret navigasjonsinstruksjoner for seksjoner 00-11
- **Teknologidekning**: Lagt til FastMCP, PostgreSQL, Azure tjenester integrasjonsdetaljer
- **Læringsutbytte**: Fremhevet produksjonsklar serverutvikling, databaseintegrasjonsmønstre og bedriftsikkerhet

#### Hoved README-strukturforbedring
- **Lab-basert terminologi**: Oppdatert hoved README.md i 11-MCPServerHandsOnLabs til konsekvent bruk av "Lab"-struktur
- **Organisering av læringsløp**: Klar progresjon fra grunnleggende konsepter gjennom avansert implementering til produksjonsdistribusjon
- **Virkelighetsfokus**: Vekt på praktisk, hands-on læring med bedriftsnivå mønstre og teknologier

### Dokumentasjonskvalitets- og konsistensforbedringer
- **Vekt på praktisk læring**: Forsterket praktisk, laboratoriebasert tilnærming gjennom dokumentasjonen
- **Fokus på bedriftmønstre**: Fremhevet produksjonsklare implementeringer og bedriftsikkerhetshensyn
- **Teknologiintegrasjon**: Omfattende dekning av moderne Azure-tjenester og AI-integrasjonsmønstre
- **Læringsprogresjon**: Klar, strukturert vei fra grunnleggende konsepter til produksjonsdistribusjon

## 26. september 2025

### Casestudier-forbedring - GitHub MCP Registry-integrasjon

#### Casestudier (09-CaseStudy/) - Fokus på økosystemutvikling
- **README.md**: Stor utvidelse med omfattende GitHub MCP Registry casestudie
  - **GitHub MCP Registry casestudie**: Ny omfattende casestudie som undersøker GitHubs MCP Registry lansering i september 2025
    - **Problemanalyse**: Detaljert undersøkelse av fragmenterte MCP server oppdagelses- og distribusjonsutfordringer
    - **Løsningsarkitektur**: GitHubs sentraliserte registertilnærming med ett-klikk VS Code installasjon
    - **Forretningspåvirkning**: Målbare forbedringer i utviklerombordingsprosess og produktivitet
    - **Strategisk verdi**: Fokus på modulær agentdistribusjon og tverrverktøy interoperabilitet
    - **Økosystemutvikling**: Posisjonering som grunnleggende plattform for agentisk integrasjon
  - **Forbedret casestudie-struktur**: Oppdatert alle syv casestudier med konsistent formatering og omfattende beskrivelser
    - Azure AI Reiseagenter: Vekt på fleragentorchestrering
    - Azure DevOps-integrasjon: Fokus på arbeidsflytautomatisering
    - Dokumentasjonsinnhenting i sanntid: Python konsollklientimplementasjon
    - Interaktiv studieplansgenerator: Chainlit samtale-webapp
    - Dokumentasjon i editor: VS Code og GitHub Copilot integrasjon
    - Azure API Management: Bedrifts-API integrasjonsmønstre
    - GitHub MCP Registry: Økosystemutvikling og samfunnsplattform
  - **Omfattende konklusjon**: Omskrevet konklusjonsseksjon som fremhever syv casestudier som spenner over flere MCP implementasjonsdimensjoner
    - Bedriftsintegrasjon, fleragentorchestrering, utviklerproduktivitet
    - Økosystemutvikling, utdanningsapplikasjonskategorisering
    - Forbedrede innsikter i arkitekturmønstre, implementeringsstrategier og beste praksis
    - Vekt på MCP som moden, produksjonsklar protokoll

#### Studieguideoppdateringer (study_guide.md)
- **Visuelt pensumkart**: Oppdatert tankekart for å inkludere GitHub MCP Registry i Casestudier-seksjonen
- **Casestudiebeskrivelser**: Forbedret fra generiske beskrivelser til detaljert oppdeling av syv omfattende casestudier
- **Depotstruktur**: Oppdatert seksjon 10 for å reflektere omfattende casestudiedekning med spesifikke implementeringsdetaljer
- **Endringslogg-integrasjon**: Lagt til oppføring for 26. september 2025 som dokumenterer GitHub MCP Registry tillegg og casestudieforbedringer
- **Datooppdateringer**: Oppdatert bunntekst tidsstempel for å reflektere nyeste revisjon (26. september 2025)

### Forbedringer i dokumentasjonskvalitet
- **Konsistensforbedring**: Standardisert casestudieformatering og struktur på tvers av alle sju eksempler
- **Omfattende dekning**: Casestudier dekker nå bedrifts-, utviklerproduktivitet- og økosystemutviklingsscenarier
- **Strategisk posisjonering**: Forsterket fokus på MCP som grunnleggende plattform for agentisk systemdistribusjon
- **Ressursintegrasjon**: Oppdatert tilleggskilder for å inkludere GitHub MCP Registry-lenke

## 15. september 2025

### Utvidelse av avanserte emner - Egendefinerte transporter & Konteksteknikk

#### MCP Egendefinerte transporter (05-AdvancedTopics/mcp-transport/) - Ny avansert implementeringsveiledning
- **README.md**: Komplett implementeringsveiledning for egendefinerte MCP transportmekanismer
  - **Azure Event Grid-transport**: Omfattende serverløs hendelsesdrevet transportimplementasjon
    - C#, TypeScript og Python eksempler med Azure Functions integrasjon
    - Hendelsesdrevne arkitekturmønstre for skalerbare MCP-løsninger
    - Webhook-mottakere og push-basert meldinghåndtering
  - **Azure Event Hubs-transport**: Høy gjennomstrømming streamingtransportimplementasjon
    - Sanntids streamingmuligheter for lav latens-scenarier
    - Partisjoneringsstrategier og sjekkpunktadministrasjon
    - Meldingbatching og ytelsesoptimalisering
  - **Bedriftsintegrasjonsmønstre**: Produksjonsklare arkitektoniske eksempler
    - Distribuert MCP behandling over flere Azure Functions
    - Hybrid transportarkitekturer som kombinerer flere transporttyper
    - Meldingens holdbarhet, pålitelighet og feilhåndteringsstrategier
  - **Sikkerhet & overvåking**: Azure Key Vault-integrasjon og observabilitétsmønstre
    - Administrert identitetsautentisering og minst privilegium-tilgang
    - Application Insights telemetri og ytelsesovervåking
    - Bruddautomater og feiltoleransemønstre
  - **Testingsrammeverk**: Omfattende teststrategier for egendefinerte transporter
    - Enhetstesting med testdoubler og mocking-rammeverk
    - Integrasjonstesting med Azure Test Containers
    - Ytelsestesting og belastningstestbetraktninger

#### Konteksteknikk (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI-disiplin
- **README.md**: Omfattende utforskning av konteksteknikk som et fremvoksende felt
  - **Kjerneprinsipper**: Komplett deling av kontekst, bevissthet om handlingsbeslutninger og kontekstvindu-administrasjon

  - **MCP-protokolltilpasning**: Hvordan MCP-design adresserer utfordringer innen kontekstengineering  
    - Begrensninger i kontekstvindu og progressive lastestrategier  
    - Relevansbestemmelse og dynamisk kontekstinnhenting  
    - Håndtering av multimodal kontekst og sikkerhetshensyn  
  - **Implementeringstilnærminger**: Enkelttrådet vs. multi-agent arkitekturer  
    - Kontekstbitering og prioriteringsteknikker  
    - Progressiv kontekstlasting og komprimeringsstrategier  
    - Lagdelte kontekstilnærminger og optimalisering av innhenting  
  - **Målerammeverk**: Fremvoksende metrikker for evaluering av konteksteffektivitet  
    - Inndataeffektivitet, ytelse, kvalitet, og brukeropplevelse  
    - Eksperimentelle tilnærminger til kontekstoptimalisering  
    - Feilanalyse og forbedringsmetodikker  

#### Oppdateringer i læreplannavigasjon (README.md)  
- **Forbedret modulstruktur**: Oppdatert læreplantabell for å inkludere nye avanserte emner  
  - Lagt til Context Engineering (5.14) og Custom Transport (5.15)  
  - Konsistent formatering og navigasjonslenker gjennom alle moduler  
  - Oppdaterte beskrivelser for å reflektere nåværende innholdsomfang  

### Forbedringer i katalogstruktur  
- **Navnestandardisering**: Omdøpt "mcp transport" til "mcp-transport" for konsistens med andre avanserte emnemapper  
- **Innholdsorganisering**: Alle 05-AdvancedTopics-mapper følger nå konsistent navngivingsmønster (mcp-[emne])  

### Kvalitetsforbedringer i dokumentasjon  
- **MCP-spesifikasjonstilpasning**: Alt nytt innhold refererer til nåværende MCP-spesifikasjon 2025-06-18  
- **Multi-språklige eksempler**: Omfattende kodeeksempler i C#, TypeScript og Python  
- **Enterprise-fokus**: Produksjonsklare mønstre og Azure-integrasjon gjennom hele dokumentasjonen  
- **Visuell dokumentasjon**: Mermaid-diagrammer for arkitektur- og flytvisualisering  

## 18. august 2025  

### Omfattende dokumentasjonsoppdatering - MCP 2025-06-18 standarder  

#### MCP sikkerhetsbeste praksiser (02-Security/) - Full modernisering  
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Full omskriving tilpasset MCP-spesifikasjon 2025-06-18  
  - **Obligatoriske krav**: Lagt til eksplisitte MÅ/IKKE MÅ-krav fra offisiell spesifikasjon med klare visuelle indikatorer  
  - **12 kjerne sikkerhetspraksiser**: Omstrukturert fra 15-punktsliste til omfattende sikkerhetsdomener  
    - Tokensikkerhet & autentisering med integrasjon av ekstern identitetsleverandør  
    - Sesjonshåndtering & transportsikkerhet med kryptografiske krav  
    - AI-spesifikk trusselbeskyttelse med Microsoft Prompt Shields integrasjon  
    - Tilgangskontroll & tillatelser med minst privilegium-prinsipp  
    - Innholdssikkerhet & overvåking med Azure Content Safety integrasjon  
    - Leverandørkjede-sikkerhet med grundig komponentverifisering  
    - OAuth-sikkerhet & Confused Deputy-beskyttelse med PKCE-implementering  
    - Hendelseshåndtering & gjenoppretting med automatiserte kapasiteter  
    - Samsvar & styring med regulatorisk tilpasning  
    - Avanserte sikkerhetskontroller med zero trust-arkitektur  
    - Microsoft sikkerhetsøkosystemintegrasjon med omfattende løsninger  
    - Kontinuerlig sikkerhetsevolusjon med adaptive praksiser  
  - **Microsoft sikkerhetsløsninger**: Forbedret integrasjonsveiledning for Prompt Shields, Azure Content Safety, Entra ID, og GitHub Advanced Security  
  - **Implementeringsressurser**: Kategoriserte omfattende ressurslenker etter Offisiell MCP-dokumentasjon, Microsoft-sikkerhetsløsninger, sikkerhetsstandarder og implementeringsveiledninger  

#### Avanserte sikkerhetskontroller (02-Security/) - Enterprise-implementering  
- **MCP-SECURITY-CONTROLS-2025.md**: Fullstendig overhaling med sikkerhetsrammeverk i enterprise-klasse  
  - **9 omfattende sikkerhetsdomener**: Utvidet fra grunnleggende kontroller til detaljert enterprise-rammeverk  
    - Avansert autentisering & autorisasjon med Microsoft Entra ID integrasjon  
    - Tokensikkerhet & anti-passthrough-kontroller med omfattende validering  
    - Sesjonsikkerhetskontroller med hijacking-beskyttelse  
    - AI-spesifikke sikkerhetskontroller med prompt-injeksjon og verktøyforgiftning-beskyttelse  
    - Confused Deputy-angrepsbeskyttelse med OAuth-proktorsikkerhet  
    - Verktøykjøringssikkerhet med sandkasse og isolasjon  
    - Leverandørkjede-sikkerhetskontroller med avhengighetsverifisering  
    - Overvåkings- og deteksjonskontroller med SIEM-integrasjon  
    - Hendelseshåndtering & gjenoppretting med automatiserte kapasiteter  
  - **Implementeringseksempler**: Lagt til detaljerte YAML-konfigurasjonsblokker og kodeeksempler  
  - **Microsoft-løsningsintegrasjon**: Omfattende dekning av Azure sikkerhetstjenester, GitHub Advanced Security og enterprise identitetsstyring  

#### Sikkerhet i avanserte emner (05-AdvancedTopics/mcp-security/) - Produksjonsklar implementering  
- **README.md**: Full omskriving for enterprise sikkerhetsimplementering  
  - **Nåværende spesifikasjonstilpasning**: Oppdatert til MCP-spesifikasjon 2025-06-18 med obligatoriske sikkerhetskrav  
  - **Forbedret autentisering**: Microsoft Entra ID integrasjon med omfattende .NET- og Java Spring Security-eksempler  
  - **AI-sikkerhetsintegrasjon**: Microsoft Prompt Shields og Azure Content Safety med detaljerte Python-eksempler  
  - **Avansert trusselmitigering**: Omfattende implementeringseksempler for  
    - Confused Deputy-angrepsbeskyttelse med PKCE og validering av brukersamtykke  
    - Token Passthrough-beskyttelse med publikumsvalidering og sikker tokenhåndtering  
    - Sesjonshijacking-beskyttelse med kryptografisk binding og atferdsanalyse  
  - **Enterprise sikkerhetsintegrasjon**: Azure Application Insights overvåking, trusseldeteksjonspipelines og leverandørkjede-sikkerhet  
  - **Implementeringssjekkliste**: Klare obligatoriske vs. anbefalte sikkerhetskontroller med fordeler fra Microsoft sikkerhetsøkosystem  

### Dokumentasjonskvalitet & standardtilpasning  
- **Spesifikasjonsreferanser**: Oppdaterte alle referanser til nåværende MCP-spesifikasjon 2025-06-18  
- **Microsoft sikkerhetsøkosystem**: Forbedret integrasjonsveiledning gjennom all sikkerhetsdokumentasjon  
- **Praktisk implementering**: Lagt til detaljerte kodeeksempler i .NET, Java og Python med enterprise-mønstre  
- **Ressursorganisering**: Omfattende kategorisering av offisiell dokumentasjon, sikkerhetsstandarder og implementeringsveiledninger  
- **Visuelle indikatorer**: Klar markering av obligatoriske krav vs. anbefalte praksiser  


#### Kjernebegreper (01-CoreConcepts/) - Full modernisering  
- **Protokollversjonsoppdatering**: Oppdatert for å referere til nåværende MCP-spesifikasjon 2025-06-18 med datobasert versjonering (ÅÅÅÅ-MM-DD format)  
- **Arkitekturforbedring**: Forbedrede beskrivelser av Hosts, Clients og Servers for å reflektere nåværende MCP-arkitekturmønstre  
  - Hosts er nå tydelig definert som AI-applikasjoner som koordinerer flere MCP-klientforbindelser  
  - Klienter beskrevet som protokollforbindelser som opprettholder en-til-en serverrelasjoner  
  - Servere forbedret med lokale vs. eksterne distribusjonsscenarier  
- **Primitive omstrukturering**: Fullstendig overhaling av server- og klientprimitiver  
  - Serverprimitiver: Ressurser (datakilder), Prompter (maler), Verktøy (eksekverbare funksjoner) med detaljerte forklaringer og eksempler  
  - Klientprimitiver: Sampling (LLM-svar), Elicitation (brukerinndata), Logging (feilsøking/overvåking)  
  - Oppdatert med nåværende oppdagelses- (`*/list`), innhentings- (`*/get`), og eksekverings- (`*/call`) metode-mønstre  
- **Protokollarkitektur**: Innført to-lags arkitekturmodell  
  - Datalag: JSON-RPC 2.0 fundament med livssyklushåndtering og primitivene  
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (ekstern) transportmekanismer  
- **Sikkerhetsrammeverk**: Omfattende sikkerhetsprinsipper inkludert eksplisitt brukersamtykke, datavern, verktøysikkerhet og transportsikkerhet  
- **Kommunikasjonsmønstre**: Oppdaterte protokollmeldinger for å vise initialisering, oppdagelse, eksekvering og varslingsflyter  
- **Kodeeksempler**: Oppfrisket flerspråklige eksempler (.NET, Java, Python, JavaScript) for å gjenspeile nåværende MCP SDK-mønstre  

#### Sikkerhet (02-Security/) - Omfattende sikkerhetsoverhaling  
- **Standardtilpasning**: Full tilpasning til MCP-spesifikasjon 2025-06-18 sikkerhetskrav  
- **Autentiseringsevolusjon**: Dokumentert utvikling fra egendefinerte OAuth-servere til ekstern identitetsleverandør-delegasjon (Microsoft Entra ID)  
- **AI-spesifikk trusselanalyse**: Forbedret dekning av moderne AI-angrepsvektorer  
  - Detaljerte prompt-injeksjonsangripscenarioer med reelle eksempler  
  - Verktøyforgiftingsmekanismer og "rug pull"-angrepsmønstre  
  - Kontekstvindu-forgiftning og modelleringsforvirringsangrep  
- **Microsoft AI-sikkerhetsløsninger**: Omfattende dekning av Microsofts sikkerhetsøkosystem  
  - AI Prompt Shields med avansert deteksjon, spotlighting og avgrensningsteknikker  
  - Azure Content Safety integrasjonsmønstre  
  - GitHub Advanced Security for leverandørkjede-beskyttelse  
- **Avansert trusselmitigering**: Detaljerte sikkerhetskontroller for  
  - Sesjonshijacking med MCP-spesifikke angrepsscenarier og kryptografiske sesjons-ID-krav  
  - Confused Deputy-problemer i MCP-proxy-scenarier med eksplisitte samtykkekrav  
  - Token passthrough-sårbarheter med obligatoriske valideringskontroller  
- **Leverandørkjede-sikkerhet**: Utvidet AI leverandørkjedeomfang inkludert fundamentmodeller, embeddingtjenester, kontekstleverandører og tredjeparts-APIer  
- **Foundationsikkerhet**: Forbedret integrasjon med enterprise-sikkerhetsmønstre inkludert zero trust-arkitektur og Microsoft sikkerhetsøkosystem  
- **Ressursorganisering**: Kategoriserte omfattende ressurslenker etter type (offisielle dokumenter, standarder, forskning, Microsoft-løsninger, implementeringsveiledninger)  

### Dokumentasjonskvalitetsforbedringer  
- **Strukturerte læringsmål**: Forbedret læringsmål med spesifikke, handlingsorienterte resultater  
- **Kryssreferanser**: Lagt til lenker mellom relaterte sikkerhets- og kjernebegreps-emner  
- **Aktuell informasjon**: Oppdaterte alle datoreferanser og spesifikasjonslenker til gjeldende standarder  
- **Implementeringsveiledning**: Lagt til spesifikke, handlingsorienterte implementeringsretningslinjer gjennom begge seksjoner  

## 16. juli 2025  

### README og navigasjonsforbedringer  
- Fullstendig redesignet læreplannavigasjon i README.md  
- Erstattet `<details>`-tagger med mer tilgjengelig tabellbasert format  
- Laget alternative layoutvalg i ny "alternative_layouts"-mappe  
- Lagt til kortbaserte, tab-baserte og akkordionstil navigasjonseksempler  
- Oppdatert seksjon for repositorie-struktur for å inkludere alle siste filer  
- Forbedret "Slik bruker du denne læreplanen"-seksjon med klare anbefalinger  
- Oppdatert MCP-spesifikasjonslenker til å peke til korrekte URLer  
- Lagt til Context Engineering seksjon (5.14) i læreplanstruktur  

### Studieveiledningsoppdateringer  
- Fullstendig revidert studieveiledning for å tilpasse nåværende repositorie-struktur  
- Lagt til nye seksjoner for MCP-klienter og verktøy, samt populære MCP-servere  
- Oppdatert Visual Curriculum Map for å nøyaktig reflektere alle emner  
- Forbedret beskrivelser av avanserte emner for å dekke alle spesialiserte områder  
- Oppdatert kasusstudieseksjon for å reflektere faktiske eksempler  
- Lagt til denne omfattende endringsloggen  

### Fellesskapsbidrag (06-CommunityContributions/)  
- Lagt til detaljert informasjon om MCP-servere for bildegenerering  
- Lagt til omfattende seksjon om bruk av Claude i VSCode  
- Lagt til Cline terminalklient-oppsett og brukerveiledning  
- Oppdatert MCP-klientseksjon for å inkludere alle populære klientvalg  
- Forbedret bidragseksempler med mer nøyaktige kodeeksempler  

### Avanserte emner (05-AdvancedTopics/)  
- Organisert alle spesialiserte emnemapper med konsistent navngivning  
- Lagt til materiale og eksempler for kontekstengineering  
- Lagt til Foundry-agentintegrasjonsdokumentasjon  
- Forbedret dokumentasjon for Entra ID-sikkerhetsintegrasjon  

## 11. juni 2025  

### Første opprettelse  
- Utgitt første versjon av MCP for Beginners læreplan  
- Opprettet grunnleggende struktur for alle 10 hovedseksjoner  
- Implementert Visual Curriculum Map for navigasjon  
- Lagt til innledende prøveprosjekter i flere programmeringsspråk  

### Komme i gang (03-GettingStarted/)  
- Opprettet første serverimplementeringseksempler  
- Lagt til veiledning for klientutvikling  
- Inkludert instruksjoner for LLM-klientintegrasjon  
- Lagt til VS Code integrasjonsdokumentasjon  
- Implementert Server-Sent Events (SSE) servereksempler  

### Kjernebegreper (01-CoreConcepts/)  
- Lagt til detaljert forklaring av klient-server-arkitektur  
- Opprettet dokumentasjon for sentrale protokollkomponenter  
- Dokumentert meldingsmønstre i MCP  

## 23. mai 2025  

### Repositorie-struktur  
- Initialisert repositoriet med grunnleggende mappestruktur  
- Opprettet README-filer for hver hovedseksjon  
- Satte opp oversettelsesinfrastruktur  
- Lagt til bildeassets og diagrammer  

### Dokumentasjon  
- Opprettet innledende README.md med oversikt over læreplan  
- Lagt til CODE_OF_CONDUCT.md og SECURITY.md  
- Satte opp SUPPORT.md med veiledning for å få hjelp  
- Opprettet foreløpig studieveiledningsstruktur  

## 15. april 2025  

### Planlegging og rammeverk  
- Innledende planlegging for MCP for Beginners læreplan  
- Definerte læringsmål og målgruppe  
- Skisset ut 10-seksjons struktur av læreplan  
- Utviklet konseptuelt rammeverk for eksempler og kasusstudier  
- Opprettet første prototype-eksempler for nøkkelbegreper  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
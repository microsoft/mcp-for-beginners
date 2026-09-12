# Endringslogg: MCP for Nybegynnere Pensum

Dette dokumentet fungerer som en oversikt over alle betydelige endringer gjort i Model Context Protocol (MCP) for Nybegynnere-pensumet. Endringene dokumenteres i omvendt kronologisk rekkefølge (nyeste endringer først).

## 9. september 2026

### MCP 2026-07-28 Endelig Spesifikasjonsjustering

Oppdaterte det engelske pensumet fra release-kandidat og `2025-11-25`
baselinje-veiledning til den endelige MCP `2026-07-28` spesifikasjonen.

- **Oppdatert**: Referanser til nåværende versjon, spesifikasjonslenker, stateless
  forespørselsveiledning, `server/discover`, Streamable HTTP-headere, og Tasks
  utvidelsens livsløp i 38 engelske dokumentasjonsfiler.
- **Korrigert**: Elicitation bruker nå `elicitation/create`, Sampling bruker
  `sampling/createMessage`, og `InputRequiredResult.resultType` bruker
  `"input_required"`.
- **Erstattet**: Den unøyaktige Root Context samtaletilstanden med en
  protokollnøyaktig Roots-leksjon som dekker informasjonsfilsystemhint, den
  nåværende fler-omgangs flyten, sikkerhetsgrenser og migrasjonsmuligheter.
- **Presisert**: Roots, Sampling, Logging og Dynamic Client Registration er
  avskrevet i `2026-07-28`, med anbefalte erstatninger og tidligste
  fjerningsdato dokumentert.
- **Merket**: Eksempler som fortsatt avhenger av MCP `2025-11-25`, HTTP+SSE,
  initialiseringshåndtrykk eller protokollsesjoner beholdes som eksempler på 
  eldre kompatibilitet istedenfor å presenteres som nåværende implementasjoner.
- **Sikkerhetsveiledning**: Oppdaterte de frittstående sikkerhetsveiledningene til å bruke
  per-forespørsel autorisasjon og eksplisitte applikasjonstilstandshåndtak i stedet for
  fjernede protokollsesjons-IDer. Client ID Metadata-dokumenter er nå
  den foretrukne registreringsveien, med DCR dokumentert som kun kompatibilitet.
- **Støttemateriale**: Oppdaterte studieguide, bidragsjekkliste,
  Publora case-studie, og APIM case-studie. APIM-gjennomgangen anbefaler nå
  sin nåværende Streamable HTTP `/mcp` endepunkt i stedet for avskrevne `/sse`.
- **Kanoniske lenker**: Erstattet pensjonerte og utkastspesifikasjons-URLer i engelske
  kilde-Markdown med versjonerte `2026-07-28` lenker, samtidig som eksplisitte
  lenker til eldre versjoner bevares der et eksempel fortsatt er låst til eldre verktøy.
- **Stabile filnavn**: Omdøpte den endelige spesifikasjonsguiden og to sikkerhets-
  guider for å fjerne release-kandidat og årstallsuffix, og oppdaterte deretter alle engelske
  hyperlenker til deres stabile stier.
- **Nytt autorisasjonseksempel**: Lagt til en testet
  [TypeScript MCP `2026-07-28` ressursserver](./02-Security/samples/cimd-dcr-auth/README.md)
  som sammenligner foretrukne Client ID Metadata-dokumenter med avskrevet Dynamic
  Client Registration fallback. Eksemplet inkluderer RFC 9728 discovery, JWKS
  validering, per-verktøy scopes, tolv tester, og en Auth0 oppsett gjenn...
- **Oversettelsesomfang**: Kun engelske kildefiler ble redigert; genererte
  oversettelser og oversatte bilder forblir uendret da disse er automatisk oversatt.

## 29. juli 2026

### Ny Modul 08 Følgesvenn: Reliabilitet Sidecars og Sikker Gjentakelse

Lagt til en leverandør-nøytral følgesvennleksjon for MCP-verktøy som skaper virkelige
effekter, tilpasset den endelige `2026-07-28` spesifikasjonen.

- **Ny**: [reliability sidecar følgesvennleksjon][reliability-sidecar]
  bruker én support-forespørsels historie, to Mermaid diagrammer, og en beslutnings-
  flyt for gjentakelse for å forklare stabile operasjonsnøkler, atomisk duplikat-
  opptak, forsoning, bevis og Tasks-utvidelsesgrense.
- **Ny**: En standardbibliotek Python og SQLite feil-injeksjonsøvelse
  bruker separate operasjons- og billettdatabaser for å demonstrere tapt respons
  etter at en ekstern effekt har blitt begått. Seks deterministiske tester dekker naiv
  duplisering, forsvarte restart-gjenopprettinger, lastkonflikter, bufrede resultater,
  aktive krav og samtidige duplikatopptak.
- **Oppdatert**: Modul 08 lenker nå følgesvennleksjonen, identifiserer den
  endelige `2026-07-28` stateless forespørselsmodellen, skiller OpenTelemetry
  observabilitet fra den avskrevne MCP logging-funksjonen, og begrenser sitt
  generiske gjentakelse-eksempel til bare leseoperasjoner.
- **Valgfri**: Leksjonen kartlegger sine bærbare konsepter til en tagget community-
  implementasjon uten å gjøre vertstjenesten eller et nettverkskall til del av
  øvelsen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2. juli 2026

### Ny Leksjon: MCP Spesifikasjonsutgivelse Kandidat 2026-07-28

Lagt til dekning av den kommende `2026-07-28` MCP spesifikasjonsutgivelse kandidat (kunngjort 21. mai 2026; endelig utgivelse planlagt 28. juli 2026), oppsummert fra den [offisielle kunngjøringsblogginnlegget](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Pensumets baselinje forblir **MCP Spesifikasjon 2025-11-25** til den nye versjonen leveres, så dette presenteres som fremtidsrettet veiledning snarere enn en omskriving av eksisterende leksjoner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — en fullstendig leksjon som dekker den stateless protokollkjernen (fjerning av `initialize` håndtrykket og `Mcp-Session-Id`), de nye `Mcp-Method`/`Mcp-Name` rutingsheaderne, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context i `_meta`, den formelle Utvidelsesrammeverket (MCP Apps og den nye Tasks-utvidelsen), seks autorisasjonsherdings-SEPer, avskrivning av Roots/Sampling/Logging, og overgangen til full JSON Schema 2020-12 for verktøy-skemaer.
- **Oppdatert** med fremtidsrettede påpekninger som lenker til den nye leksjonen:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollversjonsnotat, Sampling/Roots/Logging/Tasks seksjoner, og "Hva kommer videre"
  - [02-Security/README.md](./02-Security/README.md): autorisasjonsherdingspåpekning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport-påpekning
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling avskrivningspåpekning
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging avskrivning og Tasks-utvidelse påpekning
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing påpekning
  - [README.md](./README.md): "Ser fremover" notat i spesifikasjonsseksjonen og en ny `1.1` oppføring i pensummodultabellen
  - [study_guide.md](./study_guide.md): fremtidsrettet punkt under Core Concepts oversikten og et datert tillegg
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): påpekning om `mcp-session-id` transportkart foran stateless forespørselsmodell
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduloversiktspåpekning om Root Contexts/Sampling avskrivninger og Tasks-utvidelsen
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisasjonsherdingspåpekning

## 24. juni 2026

### Ny Leksjon: Bruke MCP i Copilot app

- [Verktøyseksjon](./12-tooling/README.md) Lagt til verktøyseksjon.
- [MCP i Copilot app](./12-tooling/01-copilot-app/README.md)

## 16. juni 2026

### MCP Spesifikasjonsjustering & Eksempelsvalidering

Validerte pensumet mot gjeldende **MCP Spesifikasjon 2025-11-25** og de nyeste offisielle SDKene, deretter korrigerte de gjenværende utdaterte spesifikasjonsreferansene og bekreftet at kjerneeksemplene fortsatt bygger og kjører.

#### Spesifikasjonsversjonskorreksjoner (2025-06-18 / 2025-03-26 → 2025-11-25)

Oppdaterte engelsk innhold der det fortsatt ble påstått at en eldre spesifikasjonsrevisjon var *nåværende/siste* standard, og pekte lenker til kanoniske `modelcontextprotocol.io` spesifikasjonsstier:
- **05-AdvancedTopics/mcp-security/README.md**: Oppdaterte banner "Current Standard", introduksjon, kjerne sikkerhetsprinsipper overskrift, obligatoriske krav overskrift, Microsoft Entra ID seksjon, Referanser & Ressurser lenker, samt avsluttende sikkerhetsvarsel (8 referanser) til 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Oppdaterte spesifikasjonslenken for Tilleggsressurser og "Current Standard" banner til 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Erstattet utdatert `2025-03-26` sikkerhets-og-tillit lenke med gjeldende 2025-11-25 sikkerhets beste praksis side
- **03-GettingStarted/14-sampling/README.md**: Oppdaterte offisielle sampling dokumentasjonslenke til 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Oppdaterte nåværende tidsform "nåværende MCP spesifikasjon" referanse og Tilleggsressurser spesifikasjonslenke til 2025-11-25 (historiske SSE-avskrivningsnotater beholdt for nøyaktighet)

#### Eksempelsvalidering mot nåværende SDKer

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` løste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` passerte uten typefeil — eksisterende `McpServer`/`StdioServerTransport` APIer forblir gyldige
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validert i isolert `.venv` med `mcp[cli]` (1.27.2); `py_compile` passerte og `FastMCP.list_tools()` returnerte korrekt `add` og `subtract` verktøy
- Bekreftet at alle eksempel `@modelcontextprotocol/sdk` versjonsintervaller (`>=1.26.0` / `^1.26.0` / `^1.27.0`) løses rent til nåværende `1.29.0` uten API-brudd

#### Avhengighets-pin Justering (lukking av versjonsgap)

Oppdatert utdaterte SDK pins slik at hvert eksempel følger nåværende MCP-utgivelse, i tråd med repo-omfattende konvensjon:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Oppdatert `@modelcontextprotocol/sdk` fra `^1.8.0` → `>=1.26.0` og oppdaterte utdaterte `"updated for MCP 2025-06-18"` pakkebeskrivelse til `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** og **lab4/code/github_mcp_server/pyproject.toml**: Oppdatert eksakt pin `mcp==1.23.0` → `mcp>=1.26.0`; genererte begge `uv.lock` filene på nytt (`uv lock`) slik at låsefilene løses til nåværende `mcp 1.27.2` og forblir synkroniserte med manifestene

#### Pensum Gap Analyse — Nyeste Spesifikasjonsfunksjon Dekning

Bekreftet at pensum allerede dekker alle primitive som er introdusert/utvidet i MCP 2025-11-25, så ingen innholdsgap gjenstår:
- **Sampling**: Leksjon 03-GettingStarted/14-sampling pluss 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-modus)**: Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumentert i 00-Introduction, 01-CoreConcepts, og 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimentelt, langvarige operasjoner)**: Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features
- **Verktøynotasjoner** (`readOnlyHint` / `destructiveHint`): Dokumentert i 01-CoreConcepts og 05-AdvancedTopics/mcp-protocol-features

### Sikkerhetsherding & Avhengighets-sårbarhetsutbedring

Kjørt en full sikkerhetssjekk over alle avhengighetsmanifester og eksempel kildekode, deretter utbedret alle rapporterte npm-advarsler og ett kode-nivå funn. Etter utbedring rapporterer `npm audit` **0 sårbarheter** i alle reviderte kataloger.

#### npm Dependency Vulnerabilities (transitive) — Fikset

Revidert alle 15 innleverte `package-lock.json` filer. Sårbarhetene var begrenset til transitive avhengigheter trukket inn av MCP Inspector utviklerverktøy, OpenAI klienten, og MCP SDK; alle er nå løst uten å bryte eksemplene:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** og **lab3/code/weather_mcp/inspector**: Oppdatert `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), som fjernet de inkluderte `ajv`, `brace-expansion`, `diff`, `path-to-regexp` og `ws` advisories. La til en npm `overrides`-oppføring som tvinger den oppdaterte `shell-quote@1.8.4` for å eliminere gjenværende kritisk advisory som bæres av `concurrently`; genererte begge lockfiles på nytt (nå 0 sårbarheter)
- **03-GettingStarted/samples/typescript**: `npm audit fix` oppdaterte den transitive `qs` (moderat) til en oppdatert versjon
- **03-GettingStarted/samples/javascript**: `npm audit fix` oppdaterte den transitive `hono` (moderat) til en oppdatert versjon
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` oppdaterte den transitive `form-data` (høy) til en oppdatert versjon
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genererte den manglende `package-lock.json` slik at prosjektet er reproduserbart og reviderbart (0 sårbarheter)

#### Sikkerhetsfikser på kode-nivå (OWASP A03: Injeksjon)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Fjernet `shell=True` fra `open_in_vscode` verktøyet. Tidligere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillot shell-metategn i en mappesti å bli tolket av `cmd.exe` (kommando-injeksjonsvektor). Nå starter den den løste `Code.exe` direkte med mappen som argument — ingen shell — noe som er funksjonelt ekvivalent og trygt

#### Python-avhengighetsrevisjon

- Reviderte alle Python kravsett med `pip-audit`. `05-AdvancedTopics` og `03-GettingStarted/samples/python` rapporterte **ingen kjente sårbarheter** (deres `mcp` / `httpx` / `pydantic` / `python-dotenv` intervaller løser til nåværende oppdaterte versjoner)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` markerte den transitive avhengigheten **`werkzeug` 3.1.1** med tre `safe_join` Windows-enhetsnavn DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, og `CVE-2026-27199` (alle fikset i 3.1.6). La til en eksplisitt sikkerhets-pin `werkzeug>=3.1.6` slik at oppdatert versjon blir løst; bekreftet at begrensningen løser rent med `chainlit` / `mcp` / `semantic-kernel` stakken

### Produktnavn Rebranding

Oppdaterte alt pensuminnhold for å gjenspeile Microsofts produktrebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Oppdaterte Discord-fellesskapslenke
- **AGENTS.md**: Oppdaterte Discord-serverreferanse
- **README.md**: Oppdaterte teknologi-økosystemreferanser
- **study_guide.md**: Oppdaterte case-studierreferanser
- **05-AdvancedTopics/README.md**: Oppdaterte Modul 5.13 tittel og beskrivelse
- **05-AdvancedTopics/mcp-integration/README.md**: Oppdaterte seksjonsoverskrift og beskrivelse
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Full modul tittel- og innholdsoppdatering
- **05-AdvancedTopics/mcp-security-entra/README.md**: Oppdaterte kryssreferanselenke
- **07-LessonsfromEarlyAdoption/README.md**: Oppdaterte case-studierreferanser
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Oppdaterte Seksjon 9 overskrift, merker og kapabiliteter
- **08-BestPractices/README.md**: Oppdaterte Discord-fellesskapslenke
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Oppdaterte Discord-kanalreferanse
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Oppdaterte modell-distribusjonsreferanse
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Oppdaterte AI-tjenestetabell
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Oppdaterte ressursreferanser

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Oppdaterte hovedpensumreferanser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Oppdaterte modultittel, oversikt og alle moduloverskrifter
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Oppdaterte tittel, læringsmål, oppsettinstruksjoner og ressurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Oppdaterte tittel, læringsmål, MCP verter tabell og kryssreferanser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Oppdaterte tittel, merker, forutsetninger og ressurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Oppdaterte Agent Builder referanser og tilbakemeldingslenke
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Oppdaterte forutsetninger og utvidelsesreferanser

---

## 11. april 2026

### Nytt kurs, dokumentasjonsfikser og avhengighetsoppdateringer

#### Nytt pensuminnhold lagt til

**Modul 05 - Avanserte emner**
- **Leksjon 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende guide som dekker det adversarielle debattmønsteret for multi-agent systemer
  - Mermaid arkitekturdiagram: to agenter → delt MCP server → debattutskrift → dommer → avgjørelse
  - Delt MCP verktøyserver (`web_search` + `run_python`) implementert i Python og TypeScript
  - Motstridende systemprompt (FOR / MOT / Dommer) med eksplisitte verktøy-bruks krav
  - Debatt-orkestrator i Python, TypeScript og C# som styrer runder og ruter argumenter
  - MCP `ClientSession` kobling for orkestratoren til faktiske verktøysamtaler
  - Brukstilfelle tabell (hallusinasjonsdeteksjon, trusselmodellering, API-design-gjennomgang, faktasjekk, teknologivalg)
  - Sikkerhetshensyn: sandkasse-kjøring, verktøybruk-validering, ratebegrensning, revisjonslogging
  - Strukturert øvelse med tre praktiske scenarier (kodegjennomgang, arkitekturavgjørelse, innholdsmotering)

#### Dokumentasjonsfikser

**Modul 03 - Komme i gang**
- **05-stdio-server/README.md**: Fikset ufullstendig TypeScript stdio-server eksempel — la til manglende transport-instansiering (`new StdioServerTransport()`) og `server.connect(transport)` kall for å matche Python og .NET eksemplene i samme seksjon
- **14-sampling/README.md**: Fikset skrivefeil — korrigert `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Pensumoppdateringer

**Hoved README.md**
- La til oppføring 5.17 (Adversarial Multi-Agent Reasoning med MCP) i pensumtabellen med direkte lenke til ny leksjon

**05-AdvancedTopics/README.md**
- La til rad for leksjon 5.17 i leksjonstabellen

**study_guide.md**
- La til Adversarial Multi-Agent Reasoning-tema i tankekart og beskrivelsen av Avanserte emner

#### Kode- og sikkerhetsfikser

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sikkerhetsfikser — kommandoinjeksjon**: Erstattet `execSync` shell-interpolasjon med `execFile` + `promisify` i TypeScript `run_python`-verktøyet, noe som eliminerer kommandoinjeksjonsflaten (LLM-kontrollert kode sendes nå som et bokstavelig argv-element uten shell involvering)
- **MCP verktøy-løkke kobling**: Oppdatert Python debatt-orkestrator til å bruke `AsyncAnthropic` klient (erstatter blokkert sync `Anthropic`), sender en live `ClientSession` direkte til hver agentrunde, henter verktøydefinisjoner via `session.list_tools()` hver runde, og sender `tool_use` blokker via `session.call_tool()` i en løkke til modellen produserer et endelig tekstsvar

#### Avhengighetsoppdateringer

- Oppdatert `hono` til 4.12.12 på tvers av flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Oppdatert `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript pakker
- Oppdatert `cryptography` fra 46.0.5 til 46.0.7 i Python pakker (10-StreamliningAIWorkflows lab 3 og 4)
- Oppdatert `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Oversettelser

- Synkronisert oversettelser for 48+ språk med siste kildeendringer (i18n oppdatering)

---

## 5. februar 2026

### Hele depotet validering og navigasjonsforbedringer

#### Nytt pensuminnhold lagt til

**Modul 03 - Komme i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide for oppsett av MCP verter
  - Eksempler på konfigurasjon for Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON konfigurasjonsmaler for alle hovedverter
  - Sammenligningstabell for transporttyper (stdio, SSE/HTTP, WebSocket)
  - Feilsøking av vanlige tilkoblingsproblemer
  - Sikkerhetsbest practices for vertkonfigurasjon

- **13-mcp-inspector/README.md**: Ny feilsøkingsguide for MCP Inspector
  - Installasjonsmetoder (npx, global npm, fra kilde)
  - Tilkobling til servere via stdio og HTTP/SSE
  - Testing av verktøy, ressurser og prompt-arbeidsflyter
  - VS Code integrasjon med MCP Inspector
  - Vanlige feilsøkingsscenarier med løsninger

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guide for implementering av paginering
  - Cursor-basert pagineri mønstre i Python, TypeScript, Java
  - Klient-side håndtering av paginering
  - Cursor designstrategier (ugjennomsiktig vs strukturert)
  - Anbefalinger for ytelsesoptimalisering

**Modul 05 - Avanserte emner**
- **mcp-protocol-features/README.md**: Ny dypdykk i protokollfunksjoner
  - Implementering av fremdriftsvarsler
  - Avbestillingsmønstre for forespørsler
  - Ressursmaler med URI-mønstre
  - Serverlivssyklusadministrasjon
  - Kontroll av loggnivåer
  - Feilhåndteringsmønstre med JSON-RPC koder

#### Navigasjonsfikser (24+ filer oppdatert)

**Hovedmodul README-filer**
 Nå lenker både til første leksjon OG neste modul

**02-Sikkerhets undersider**
- Alle 5 supplerende sikkerhetsdokumenter har nå "Hva er neste" navigasjon:

**09-CaseStudy filer**
- Alle case-studiefiler har nå sekvensiell navigasjon:

**10-StreamliningAI Labs**
La til Seksjonen Hva er neste i Modul 10 oversikten og Modul 11

#### Kode- og innholdsfikser

**SDK og avhengighetsoppdateringer**
Fikset tom versjon for openai til `^4.95.0`
Oppdaterte SDK fra `^1.8.0` til `>=1.26.0`
Oppdaterte mcp versjon pinner til `>=1.26.0`

**Kodefikser**
Fikset ugyldig modell `gpt-4o-mini` til `gpt-4.1-mini`

**Innholdsoppdateringer**
Fikset ødelagt lenke `READMEmd` → `README.md`, fikset pensumoverskrift `Module 1-3` → `Module 0-3`, fikset kasus-sensitiv sti
Fjernet korrumpert duplikat Innhold for Case Study 5

**Forbedringer for nybegynnere**
La til ordentlig introduksjon, læringsmål og forutsetninger for nybegynnere

#### Pensumoppdateringer

**Hoved README.md**
- La til oppføringer 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protokollfunksjoner) til pensumtabellen

**Modul README-filer**
La til leksjoner 12 og 13 til leksjonsliste
La til Praktiske guider-seksjon med paginering lenke
La til leksjoner 5.15 (Egendefinert transport) og 5.16 (Protokollfunksjoner)

**study_guide.md**
- Oppdaterte tankekartet med alle nye emner: MCP Hosts Oppsett, MCP Inspector, Paginering strategier, Dypdykk i protokollfunksjoner

## 28. januar 2026

### MCP-spesifikasjon 2025-11-25 samsvarsrevisjon

#### Forbedring av kjernebegreper (01-CoreConcepts/)
- **Ny klientprimitive - Roots**: Lagt til omfattende dokumentasjon om Roots klientprimitive som gjør det mulig for servere å forstå filsystemgrenser og tilgangstillatelser
- **Verktøyanmerkninger**: Lagt til dokumentasjon om adferdsanmerkninger til verktøy (`readOnlyHint`, `destructiveHint`) for bedre beslutninger ved kjøring av verktøy
- **Verktøykall under sampling**: Oppdatert sampling-dokumentasjon for å inkludere `tools` og `toolChoice` parametere for modellstyrt verktøykall under sampling-forespørsler
- **URL-modus uttrekk**: Lagt til dokumentasjon om URL-basert uttrekk for serverinitiert ekstern webinteraksjon
- **Oppgaver (Eksperimentelt)**: Lagt til ny seksjon som dokumenterer eksperimentelt oppgave-funksjon for holdbare utførelsesinnpakninger og utsatt resultatinnhenting

- **Ikoner Støtte**: Merket at verktøy, ressurser, maler for ressurser og prompt nå kan inkludere ikoner som tilleggmetadata

#### Oppdateringer i Dokumentasjon
- **README.md**: Lagt til MCP Spesifikasjon 2025-11-25 versjonsreferanse og forklaring på datobasert versjonering
- **study_guide.md**: Oppdatert læreplanoversikt til å inkludere Oppgaver og Verktøyannotasjoner i Seksjon for Kjernebegreper; oppdatert dokumenttidsstempel

#### Verifikasjon av Spesifikasjonskompatibilitet
- **Protokollversjon**: Verifisert at all dokumentasjon refererer til nåværende MCP Spesifikasjon 2025-11-25
- **Arkitekturjustering**: Bekreftet nøyaktighet i dokumentasjon av to-lags arkitektur (Datakjede + Transportlag)
- **Primitive Dokumentasjon**: Validert serverprimitive (Ressurser, Prompts, Verktøy) og klientprimitive (Sampling, Elicitering, Logging, Røtter)
- **Transportmekanismer**: Verifisert nøyaktighet i dokumentasjon for STDIO og Streambar HTTP transport
- **Sikkerhetsveiledning**: Bekreftet samsvar med nåværende MCP Security Best Practices dokumentasjon

#### Nøkkelfunksjoner i MCP 2025-11-25 Dokumentert
- **OpenID Connect Discovery**: Autentiseringsserveroppdagelse gjennom OIDC
- **OAuth Client ID Metadata Dokumenter**: Anbefalt klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skjema-definisjoner
- **SDK Tiersystem**: Formaliserte krav for SDK funksjonsstøtte og vedlikehold
- **Styringsstruktur**: Formaliserte Arbeidsgrupper og Interessegrupper i MCP styring

### Stor Oppdatering i Sikkerhetsdokumentasjon (02-Security/)

#### Integrasjon av MCP Security Summit Workshop (Sherpa)
- **Nytt Praktisk Treningsressurs**: Lagt til omfattende integrasjon med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all sikkerhetsdokumentasjon
- **Dekning av Ekspedisjonsrute**: Dokumentert komplett fremdrift fra Base Camp til Summit
- **OWASP Justering**: All sikkerhetsveiledning kartlegges nå til OWASP MCP Azure Security Guide risikoer

#### Integrasjon av OWASP MCP Topp 10
- **Ny Seksjon**: Lagt til tabell over OWASP MCP Topp 10 sikkerhetsrisikoer med Azure-mitigering i hoved Security README
- **Risikobasert Dokumentasjon**: Oppdatert mcp-security-controls-2025.md med OWASP MCP risikoreferanser for hvert sikkerhetsdomene
- **Referansearkitektur**: Lenket til OWASP MCP Azure Security Guide referansearkitektur og implementeringsmønstre

#### Oppdaterte Sikkerhetsfiler
- **README.md**: Lagt til Sherpa Workshop oversikt, ekspedisjonsrutetabell, OWASP MCP Topp 10 risksammendrag og praktisk treningsseksjon
- **mcp-security-controls-2025.md**: Oppdatert overskrift til februar 2026, lagt til OWASP risiko referanser (MCP01-MCP08), rettet uoverensstemmelse i spesifikasjonsversjon
- **mcp-security-best-practices-2025.md**: Lagt til Sherpa og OWASP ressursseksjon, oppdatert tidsstempel
- **mcp-best-practices.md**: Lagt til seksjon med praktisk trening med Sherpa og OWASP lenker
- **azure-content-safety-implementation.md**: Lagt til OWASP MCP06 referanse, Sherpa Camp 3 justering, og ekstra ressursseksjon

#### Nye Ressurslenker Lagt Til
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP risikosider (MCP01-MCP10)

### Læreplanomfattende MCP Spesifikasjon 2025-11-25 Justering

#### Modul 03 - Komme i Gang
- **SDK Dokumentasjon**: Lagt til Go SDK i offisiell SDK-liste; oppdatert alle SDK-referanser for å samsvare med MCP Spesifikasjon 2025-11-25
- **Transportforklaring**: Oppdaterte STDIO og HTTP Streaming transportbeskrivelser med eksplisitte spesifikasjonsreferanser

#### Modul 04 - Praktisk Implementering
- **SDK Oppdateringer**: Lagt til Go SDK; oppdatert SDK-listen med spesifikasjonsversjonsreferanse
- **Autorisering Spesifikasjon**: Oppdatert MCP Autorisasjon spesifikasjonslenke til gjeldende 2025-11-25 versjon

#### Modul 05 - Avanserte Emner
- **Nye Funksjoner**: Lagt til merknad om nye MCP Spesifikasjon 2025-11-25 funksjoner (Oppgaver, Verktøyannotasjoner, URL Mode Elicitering, Røtter)
- **Sikkerhetsressurser**: Lagt til OWASP MCP Topp 10 og Sherpa workshop lenker til tillegg referanser

#### Modul 06 - Fellesskapsbidrag
- **SDK Liste**: Lagt til Swift og Rust SDKer; oppdatert spesifikasjonslenke til 2025-11-25
- **Spesifikasjonsreferanse**: Oppdatert MCP Spesifikasjonslenke til direkte spesifikasjons-URL

#### Modul 07 - Erfaringer fra Tidlig Adopsjon
- **Ressursoppdateringer**: Lagt til MCP Spesifikasjon 2025-11-25 lenke og OWASP MCP Topp 10 til tilleggressurser

#### Modul 08 - Beste Praksis
- **Spesifikasjonsversjon**: Oppdatert MCP Spesifikasjonsreferanse til 2025-11-25
- **Sikkerhetsressurser**: Lagt til OWASP MCP Topp 10 og Sherpa workshop til tilleggreferanser

#### Modul 10 - Effektivisering av AI Arbeidsflyter
- **Badge Oppdatering**: Endret MCP versjonsmerke fra SDK versjon (1.9.3) til spesifikasjonsversjon (2025-11-25)
- **Ressurslenker**: Oppdatert MCP Spesifikasjonslenke; lagt til OWASP MCP Topp 10

#### Modul 11 - MCP Server Praktiske Labber
- **Spesifikasjonsreferanse**: Oppdatert MCP Spesifikasjonslenke til 2025-11-25 versjon
- **Sikkerhetsressurser**: Lagt til OWASP MCP Topp 10 i offisielle ressurser

## 18. desember 2025

### Oppdatering av Sikkerhetsdokumentasjon - MCP Spesifikasjon 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Oppdatering av Spesifikasjonsversjon
- **Oppdatering av Protokollversjon**: Oppdatert til å referere nyeste MCP Spesifikasjon 2025-11-25 (utgitt 25. november 2025)
  - Oppdatert alle spesifikasjonsversjonsreferanser fra 2025-06-18 til 2025-11-25
  - Oppdatert dokumentdatoreferanser fra 18. august 2025 til 18. desember 2025
  - Verifisert at alle spesifikasjons-URLer peker til nåværende dokumentasjon
- **Innholdsvalidering**: Omfattende validering av sikkerhetsbeste praksis mot siste standarder
  - **Microsoft Security Solutions**: Verifisert nåværende terminologi og lenker for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Sikkerhet**: Bekreftet samsvar med de siste OAuth sikkerhetsanbefalingene
  - **OWASP Standarder**: Validert at OWASP Top 10 for LLMs referanser er oppdaterte
  - **Azure-tjenester**: Verifisert alle Microsoft Azure dokumentasjonslenker og beste praksiser
- **Standarder Justering**: Alle refererte sikkerhetsstandarder er bekreftet oppdaterte
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure sikkerhets- og samsvarsrammeverk
- **Implementeringsressurser**: Validert alle lenker og ressurser for implementasjonsguider
  - Azure API Management autentiseringsmønstre
  - Microsoft Entra ID integrasjonsguider
  - Azure Key Vault hemmelighetshåndtering
  - DevSecOps pipelines og overvåkningsløsninger

### Kvalitetssikring av Dokumentasjon
- **Spesifikasjonskompatibilitet**: Sikret at alle obligatoriske MCP sikkerhetskrav (MÅ/MÅ IKKE) samsvarer med siste spesifikasjon
- **Aktualitet for Ressurser**: Verifisert alle eksterne lenker til Microsoft dokumentasjon, sikkerhetsstandarder og implementeringsguider
- **Dekning av Beste Praksis**: Bekreftet omfattende dekning av autentisering, autorisasjon, AI-spesifikke trusler, forsyningskjede-sikkerhet og bedriftsmønstre

## 6. oktober 2025

### Utvidelse av Komme i Gang Seksjon – Avansert Serverbruk & Enkel Autentisering

#### Avansert Serverbruk (03-GettingStarted/10-advanced)
- **Ny Kapittel Lagt Til**: Introdusert en omfattende guide til avansert MCP serverbruk, som dekker både vanlig og lavnivå serverarkitektur.
  - **Vanlig vs. Lavnivå Server**: Detaljert sammenligning og kodeeksempler i Python og TypeScript for begge tilnærminger.
  - **Handler-basert Design**: Forklaring av handler-basert verktøy/ressurs/prompt administrasjon for skalerbare, fleksible serverimplementasjoner.
  - **Praktiske Mønstre**: Virkelige scenarier hvor lavnivå servermønstre er gunstige for avanserte funksjoner og arkitektur.

#### Enkel Autentisering (03-GettingStarted/11-simple-auth)
- **Ny Kapittel Lagt Til**: Steg-for-steg guide for implementering av enkel autentisering i MCP servere.
  - **Autentiseringskonsepter**: Klar forklaring av autentisering vs. autorisasjon, og håndtering av påloggingsinformasjon.
  - **Grunnleggende Autentiseringsimplementering**: Middleware-baserte autentiseringsmønstre i Python (Starlette) og TypeScript (Express), med kodeeksempler.
  - **Fremgang til Avansert Sikkerhet**: Veiledning i å starte med enkel autentisering og utvikle til OAuth 2.1 og RBAC, med henvisninger til avanserte sikkerhetsmoduler.

Disse tilleggene gir praktisk, hands-on veiledning for å bygge mer robuste, sikre og fleksible MCP serverimplementasjoner, som bygger bro mellom grunnleggende konsepter og avanserte produksjonsmønstre.

## 29. september 2025

### MCP Server Database Integrasjonslabber - Omfattende Praktisk Læringssti

#### 11-MCPServerHandsOnLabs - Ny Komplett Database Integrasjonslæreplan
- **Fullstendig 13-Lab Læringssti**: Lagt til omfattende praktisk læreplan for utvikling av produksjonsklare MCP servere med PostgreSQL databaseintegrasjon
  - **Virkelighetsnær Implementering**: Zava Retail analyse-case som demonstrerer bedriftsnivåmønstre
  - **Strukturert Læringsprogresjon**:
    - **Labber 00-03: Grunnlag** - Introduksjon, Kjernearkitektur, Sikkerhet & Multi-leiing, Miljøoppsett
    - **Labber 04-06: Bygging av MCP Server** - Databasedesign & Skjema, MCP Server Implementering, Verktøyutvikling  
    - **Labber 07-09: Avanserte Funksjoner** - Semantisk Søkeinvolvering, Testing & Feilsøking, VS Code Integrering
    - **Labber 10-12: Produksjon & Beste Praksis** - Distribusjonsstrategier, Overvåking & Observabilitet, Beste Praksis & Optimalisering
  - **Bedriftsteknologier**: FastMCP rammeverk, PostgreSQL med pgvector, Azure OpenAI embeddinger, Azure Container Apps, Application Insights
  - **Avanserte Funksjoner**: Row Level Security (RLS), semantisk søk, flerleietakers datapåtkomst, vektor-embeddinger, sanntidsovervåking

#### Terminologistandardisering - Modul til Lab Konvertering
- **Omfattende Dokumentasjonsoppdatering**: Systematisk oppdatert alle README-filer i 11-MCPServerHandsOnLabs for å bruke "Lab" terminologi i stedet for "Modul"
  - **Seksjonsoverskrifter**: Oppdatert "What This Module Covers" til "What This Lab Covers" i alle 13 labber
  - **Innholdsbeskrivelse**: Endret "This module provides..." til "This lab provides..." gjennom dokumentasjonen
  - **Læringsmål**: Oppdatert "By the end of this module..." til "By the end of this lab..."
  - **Navigasjonslenker**: Konvertert alle "Module XX:" referanser til "Lab XX:" i kryssreferanser og navigasjon
  - **Fullføringssporing**: Oppdatert "After completing this module..." til "After completing this lab..."
  - **Bevarte Tekniske Referanser**: Opprettholdt Python modulreferanser i konfigurasjonsfiler (f.eks. `"module": "mcp_server.main"`)

#### Forbedring av Studieguide (study_guide.md)
- **Visuell Læreplansoversikt**: Lagt til ny seksjon "11. Database Integration Labs" med omfattende labsstrukturvisualisering
- **Repositorie-struktur**: Oppdatert fra ti til elleve hovedseksjoner med detaljert 11-MCPServerHandsOnLabs beskrivelse
- **Læringsstiveiledning**: Forbedret navigasjonsinstruksjoner som dekker seksjoner 00-11
- **Teknologidekning**: Lagt til detaljer om FastMCP, PostgreSQL, Azure tjenester integrering
- **Læringsutbytte**: Vektlagt produksjonsklar serverutvikling, databasedesignmønstre og bedriftsikkerhet

#### Hoved README Strukturoppgradering
- **Lab-basert Terminologi**: Oppdatert hoved README.md i 11-MCPServerHandsOnLabs til å konsekvent bruke "Lab" struktur
- **Organisering av Læringssti**: Klar progresjon fra grunnleggende konsepter gjennom avansert implementering til produksjonsdistribusjon
- **Virkelighetsfokus**: Vekt på praktisk, hands-on læring med bedriftsnivåmønstre og teknologier

### Forbedringer i Dokumentasjonskvalitet og Konsistens
- **Vekt på Praktisk Læring**: Forsterket praktisk, lab-basert tilnærming gjennom dokumentasjon
- **Fokus på Bedriftsmønstre**: Fremhevet produksjonsklare implementasjoner og sikkerhet for bedrifter
- **Teknologiintegrasjon**: Omfattende dekning av moderne Azure-tjenester og AI integrasjonsmønstre
- **Læringsprogresjon**: Klar, strukturert sti fra grunnleggende konsepter til produksjonsdistribusjon

## 26. september 2025

### Forbedring av Case Studier - GitHub MCP Registry Integrasjon

#### Case Studier (09-CaseStudy/) - Fokus på Økosystemutvikling
- **README.md**: Stor utvidelse med omfattende GitHub MCP Registry case studie
  - **GitHub MCP Registry Case Studie**: Ny omfattende case studie som undersøker GitHubs MCP Registry lansering i september 2025
    - **Problemanalyse**: Detaljert undersøkelse av fragmentert MCP serveroppdagelse og distribusjonsutfordringer
    - **Løsningsarkitektur**: GitHubs sentraliserte registertilnærming med ett-klikk VS Code installasjon
    - **Forretningspåvirkning**: Målbare forbedringer i utvikler onboarding og produktivitet
    - **Strategisk Verdi**: Fokus på modulær agentdistribusjon og tverrverktøy interoperabilitet
    - **Økosystemutvikling**: Posisjonert som grunnleggende plattform for agentisk integrasjon
  - **Forbedret Case Studie Struktur**: Oppdatert alle syv case studier med konsekvent formatering og omfattende beskrivelser
    - Azure AI Reiseagenter: Vekt på flere agenter orkestrering
    - Azure DevOps Integrasjon: Fokus på arbeidsflytautomatisering
    - Sanntids Dokumenthenting: Python konsollklient implementering
    - Interaktiv Studieplan Generator: Chainlit samtalewebapp

    - Dokumentasjon i editoren: VS Code og GitHub Copilot-integrasjon
    - Azure API Management: Enterprise API-integrasjonsmønstre
    - GitHub MCP Registry: Økosystemutvikling og fellesskapsplattform
  - **Omfattende konklusjon**: Omskrevet konklusjonsseksjon som fremhever syv casestudier som dekker flere MCP-implementeringsdimensjoner
    - Enterprise-integrasjon, multi-agent orkestrering, utviklerproduktivitet
    - Økosystemutvikling, kategorisering av utdanningsapplikasjoner
    - Forbedrede innsikter i arkitekturmodeller, implementeringsstrategier og beste praksis
    - Vekt på MCP som en moden, produksjonsklar protokoll

#### Oppdateringer i studieveiledning (study_guide.md)
- **Visuell læreplanoversikt**: Oppdatert tankekart for å inkludere GitHub MCP Registry i seksjonen Casestudier
- **Casestudier beskrivelse**: Forbedret fra generelle beskrivelser til detaljert oppdeling av syv omfattende casestudier
- **Repositorisstruktur**: Oppdatert seksjon 10 for å gjenspeile omfattende casestudiedekning med spesifikke implementeringsdetaljer
- **Endringslogg-integrasjon**: Lagt til oppføring for 26. september 2025 som dokumenterer tillegg av GitHub MCP Registry og forbedringer i casestudier
- **Datooppdateringer**: Oppdatert tidsstempel i bunntekst for å reflektere siste revisjon (26. september 2025)

### Forbedringer i dokumentasjonskvalitet
- **Konsistensforbedring**: Standardisert formatering og struktur i casestudier på tvers av alle syv eksempler
- **Omfattende dekning**: Casestudier dekker nå scenarioer innen enterprise, utviklerproduktivitet og økosystemutvikling
- **Strategisk posisjonering**: Økt fokus på MCP som grunnleggende plattform for agentbasert systemdistribusjon
- **Ressursintegrasjon**: Oppdaterte tilleggsmaterialer med lenke til GitHub MCP Registry

## 15. september 2025

### Utvidelse av avanserte emner - egendefinerte transportmetoder og kontekstteknikk

#### MCP egendefinerte transportmetoder (05-AdvancedTopics/mcp-transport/) - Ny avansert implementasjonsveiledning
- **README.md**: Fullstendig implementasjonsveiledning for egendefinerte MCP-transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverløs hendelsesdrevet transportimplementering
    - Eksempler i C#, TypeScript, og Python med integrasjon mot Azure Functions
    - Hendelsesdrevne arkitekturmønstre for skalerbare MCP-løsninger
    - Webhook-mottakere og push-basert meldingshåndtering
  - **Azure Event Hubs Transport**: Høytytende strømmingstransportimplementasjon
    - Sanntids strømmingsfunksjonalitet for lav-latens scenarier
    - Partisjoneringsstrategier og checkpoint-administrasjon
    - Meldingsbunting og ytelsesoptimalisering
  - **Enterprise Integrasjonsmønstre**: Produksjonsklare arkitektur-eksempler
    - Distribuert MCP-prosessering over flere Azure Functions
    - Hybrid transportarkitektur som kombinerer flere transporttyper
    - Meldingsbestandighet, pålitelighet og feilhåndteringsstrategier
  - **Sikkerhet og overvåkning**: Azure Key Vault-integrasjon og observasjonsmønstre
    - Autentisering med administrert identitet og minste privilegium tilgang
    - Application Insights-telemetri og ytelsesovervåkning
    - Vern mot feil og strømbrytermønstre
  - **Test-rammeverk**: Omfattende teststrategier for egendefinerte transportmetoder
    - Enhetstesting med testdoubler og mocking-rammeverk
    - Integrasjonstesting med Azure Test Containers
    - Ytelses- og belastningstesting vurderinger

#### Kontekstteknikk (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI-disiplin
- **README.md**: Omfattende utforskning av kontekstteknikk som et fremvoksende felt
  - **Kjerneprinsipper**: Fullstendig deling av kontekst, beslutningsbevissthet, og håndtering av kontekstvinduer
  - **MCP protokolltilpasning**: Hvordan MCP-design adresserer utfordringer innen kontekstteknikk
    - Begrensninger for kontekstvinduer og progressive lastestrategier
    - Relevansbestemmelse og dynamisk kontekstinnhenting
    - Multimodal konsteksthåndtering og sikkerhetshensyn
  - **Implementeringstilnærminger**: En-trådet vs. multi-agent arkitekturer
    - Kontekstdeling og prioriteringsteknikker
    - Progressiv kontekstlastning og komprimeringsstrategier
    - Lagvis konteksttilnærming og innhentingsoptimalisering
  - **Målerammeverk**: Fremvoksende målemetoder for evaluering av konsteksteffektivitet
    - Inndatteeffektivitet, ytelse, kvalitet og brukeropplevelse
    - Eksperimentelle tilnærminger til kontekstoptimalisering
    - Feilanalyse og forbedringsmetodologier

#### Oppdateringer i læreplan-navigasjon (README.md)
- **Forbedret modulstruktur**: Oppdatert tabell i læreplanen for å inkludere nye avanserte emner
  - Lagt til kontekstteknikk (5.14) og egendefinert transport (5.15)
  - Konsistent formatering og navigasjonslenker på tvers av alle moduler
  - Oppdaterte beskrivelser for å reflektere gjeldende innholdsomfang

### Forbedringer i katalogstruktur
- **Navnestandardisering**: Endret "mcp transport" til "mcp-transport" for konsistens med andre avanserte emnemapper
- **Innholdsorganisering**: Alle 05-AdvancedTopics-mapper følger nå konsistent navngivningsmønster (mcp-[tema])

### Forbedringer i dokumentasjonskvalitet
- **MCP-spesifikasjonstilpasning**: Alt nytt innhold refererer til gjeldende MCP-spesifikasjon 2025-06-18
- **Flerspråklige eksempler**: Omfattende kodeeksempler i C#, TypeScript, og Python
- **Enterprise-fokus**: Produksjonsklare mønstre og integrasjon med Azure Cloud gjennomgående
- **Visuell dokumentasjon**: Mermaid-diagrammer for arkitektur- og flytvisualisering

## 18. august 2025

### Omfattende dokumentasjonsoppdatering - MCP 2025-06-18 standarder

#### MCP sikkerhetsbeste praksis (02-Security/) - Full modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullstendig omskriving i samsvar med MCP-spesifikasjon 2025-06-18
  - **Obligatoriske krav**: Lagt til eksplisitte MUST/MUST NOT-krav fra offisiell spesifikasjon med tydelige visuelle indikatorer
  - **12 kjernepraksiser innen sikkerhet**: Restrukturert fra 15-punkts liste til omfattende sikkerhetsdomener
    - Token-sikkerhet og autentisering med ekstern identitetsleverandørintegrasjon
    - Sesjonshåndtering og transportsikkerhet med kryptografiske krav
    - AI-spesifikk trusselbeskyttelse med Microsoft Prompt Shields-integrasjon
    - Tilgangskontroll og tillatelser med prinsippet om minste privilegium
    - Innholdssikkerhet og overvåkning med Azure Content Safety-integrasjon
    - Sikkerhet i forsyningskjeden med omfattende komponentverifisering
    - OAuth-sikkerhet og forebygging av forvirret stedfortreder med PKCE-implementering
    - Hendelsesrespons og gjenoppretting med automatiserte kapasiteter
    - Overholdelse og styring med regulatorisk tilpasning
    - Avanserte sikkerhetskontroller med zero trust-arkitektur
    - Integrasjon i Microsoft sikkerhetsekosystem med omfattende løsninger
    - Kontinuerlig sikkerhetsevolusjon med adaptive praksiser
  - **Microsoft sikkerhetsløsninger**: Forbedret veiledning for integrasjon av Prompt Shields, Azure Content Safety, Entra ID, og GitHub Advanced Security
  - **Implementeringsressurser**: Kategoriserte omfattende ressurslenker etter Offisiell MCP-dokumentasjon, Microsoft sikkerhetsløsninger, sikkerhetsstandarder, og implementeringsveiledninger

#### Avanserte sikkerhetskontroller (02-Security/) - Enterprise-implementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fullstendig gjennomgang med sikkerhetsrammeverk i bedriftsklasse
  - **9 omfattende sikkerhetsdomener**: Utvidet fra grunnleggende kontroller til detaljert bedriftsrammeverk
    - Avansert autentisering og autorisasjon med Microsoft Entra ID-integrasjon
    - Token-sikkerhet og anti-passthrough-kontroller med omfattende validering
    - Sesjonssikkerhetskontroller med hijacking-forebygging
    - AI-spesifikke sikkerhetskontroller med forebygging av prompt-injeksjon og verktøygifting
    - Forebygging av forvirret stedfortreder-angrep med OAuth-proxysikkerhet
    - Verktøykjøringssikkerhet med sandboxing og isolasjon
    - Sikkerhetskontroller for forsyningskjeden med avhengighetsbekreftelse
    - Overvåkings- og deteksjonskontroller med SIEM-integrasjon
    - Hendelsesrespons og gjenoppretting med automatiserte kapasiteter
  - **Implementeringseksempler**: Lagt til detaljerte YAML-konfigurasjonsblokker og kodeeksempler
  - **Microsoft-løsningsintegrasjon**: Omfattende dekning av Azure sikkerhetstjenester, GitHub Advanced Security og bedriftsidentitetsadministrasjon

#### Sikkerhet i avanserte emner (05-AdvancedTopics/mcp-security/) - Produksjonsklar implementering
- **README.md**: Fullstendig omskriving for bedriftsimplementering av sikkerhet
  - **Gjeldende spesifikasjonstilpasning**: Oppdatert til MCP-spesifikasjon 2025-06-18 med obligatoriske sikkerhetskrav
  - **Forbedret autentisering**: Microsoft Entra ID-integrasjon med omfattende .NET og Java Spring Security-eksempler
  - **AI-sikkerhetsintegrasjon**: Microsoft Prompt Shields og Azure Content Safety-implementering med detaljerte Python-eksempler
  - **Avansert trusselmitigering**: Omfattende implementeringseksempler for
    - Forebygging av forvirret stedfortreder-angrep med PKCE og validering av bruker samtykke
    - Forebygging av token-passthrough med målgruppevalidering og sikker tokenhåndtering
    - Forhindring av sesjonshijacking med kryptografisk binding og atferdsanalyse
  - **Enterprise-sikkerhetsintegrasjon**: Azure Application Insights-overvåkning, trusseldeteksjonsrørledninger, og forsyningskjedesikkerhet
  - **Implementeringssjekkliste**: Tydelig skille mellom obligatoriske og anbefalte sikkerhetskontroller med fordeler fra Microsofts sikkerhetsekosystem

### Dokumentasjonskvalitet og standardtilpasning
- **Spesifikasjonsreferanser**: Oppdatert alle referanser til gjeldende MCP-spesifikasjon 2025-06-18
- **Microsoft sikkerhetsekosystem**: Forbedret integrasjonsveiledning i all sikkerhetsdokumentasjon
- **Praktisk implementering**: Lagt til detaljerte kodeeksempler i .NET, Java, og Python med bedriftsmønstre
- **Ressursorganisering**: Omfattende kategorisering av offisiell dokumentasjon, sikkerhetsstandarder og implementeringsveiledninger
- **Visuelle indikatorer**: Tydelig merking av obligatoriske krav vs. anbefalte praksiser


#### Kjernebegreper (01-CoreConcepts/) - Full modernisering
- **Protokollversjonsoppdatering**: Oppdatert til å referere til gjeldende MCP-spesifikasjon 2025-06-18 med datobasert versjonering (ÅÅÅÅ-MM-DD format)
- **Arkitekturrevisjon**: Forbedrede beskrivelser av Hosts, Clients og Servers for å reflektere gjeldende MCP-arkitekturmodeller
  - Hosts nå klart definert som AI-applikasjoner som koordinerer flere MCP-klienttilkoblinger
  - Clients beskrevet som protokollkoblere som opprettholder én-til-én serverrelasjoner
  - Servers forbedret med lokale vs. fjern distribusjonsscenarier
- **Primitive omstrukturering**: Full gjennomgang av server- og klientprimitive
  - Serverprimitiver: Ressurser (datakilder), Prompter (maler), Verktøy (utførbare funksjoner) med detaljerte forklaringer og eksempler
  - Klientprimitiver: Sampling (LLM fullføringer), Elicitation (brukerinndata), Logging (feilsøking/overvåkning)
  - Oppdatert med nåværende oppdagelses- (`*/list`), innhentings- (`*/get`), og utførelses- (`*/call`) metodemønstre
- **Protokollarkitektur**: Innført to-lags arkitekturmodell
  - Datalag: JSON-RPC 2.0 grunnlag med livssyklusstyring og primitiv
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer
- **Sikkerhetsrammeverk**: Omfattende sikkerhetsprinsipper inkludert eksplisitt brukersamtykke, datavern, sikker eksekvering av verktøy, og transportlagsikkerhet
- **Kommunikasjonsmønstre**: Oppdaterte protokollmeldinger for å vise initialisering, oppdagelse, utførelse og varslingsflyter
- **Kodeeksempler**: Oppfrisket flerspråklige eksempler (.NET, Java, Python, JavaScript) for å reflektere nåværende MCP SDK-mønstre

#### Sikkerhet (02-Security/) - Omfattende sikkerhetsgjennomgang  
- **Standardtilpasning**: Full samsvar med MCP-spesifikasjon 2025-06-18 sikkerhetskrav
- **Autentiseringsevolusjon**: Dokumentert utvikling fra egendefinerte OAuth-servere til ekstern identitetsleverandørdelegasjon (Microsoft Entra ID)
- **AI-spesifikk trusselanalyse**: Forbedret dekning av moderne AI-angrepstyper
  - Detaljerte scenarier for prompt-injeksjonsangrep med virkelighetseksempler
  - Mekanismer for verktøygifting og "rug pull"-angrepsmønstre
  - Kontekstvindusforgiftning og modellforvirringsangrep
- **Microsoft AI sikkerhetsløsninger**: Omfattende dekning av Microsoft sikkerhetsekosystem
  - AI Prompt Shields med avansert deteksjon, spotlighting og skilleteknikker
  - Azure Content Safety integrasjonsmønstre
  - GitHub Advanced Security for beskyttelse av forsyningskjede
- **Avansert trusselmitigering**: Detaljert sikkerhetskontroller for
  - Sesjonshijacking med MCP-spesifikke angrepsscenarioer og kryptografiske sesjons-ID-krav
  - Forvirret stedfortreder-problemer i MCP proxy-scenarier med eksplisitte samtykkekrav
  - Token passthrough-sårbarheter med obligatoriske valideringskontroller
- **Forsyningskjedesikkerhet**: Utvidet AI-forsyningskjededekning inkludert grunnmodell, embeddingtjenester, kontekstleverandører og tredjeparts-APIer
- **Grunnleggende sikkerhet**: Forbedret integrasjon med bedriftsikkerhetsmønstre inkludert zero trust-arkitektur og Microsoft sikkerhetsekosystem
- **Ressursorganisering**: Kategoriserte omfattende ressurslenker etter type (offisielle dokumenter, standarder, forskning, Microsoft-løsninger, implementeringsveiledninger)

### Forbedringer i dokumentasjonskvalitet
- **Strukturerte læringsmål**: Forbedret læringsmål med spesifikke, handlingsorienterte resultater
- **Kryssreferanser**: Lagt til lenker mellom relaterte sikkerhets- og kjernebegrepsemner
- **Aktuell informasjon**: Oppdatert alle datoreferanser og spesifikasjonslenker til gjeldende standarder
- **Implementeringsveiledning**: Lagt til spesifikke, handlingsrettede implementeringsretningslinjer gjennom begge seksjoner

## 16. juli 2025

### README og navigasjonsforbedringer
- Fullstendig redesignet læreplannavigasjon i README.md
- Erstattet `<details>`-tagger med mer tilgjengelig tabellbasert format
- Opprettet alternative layoutvalg i ny mappe "alternative_layouts"
- Lagt til kort-baserte, fane-stil, og harmonika-stil navigasjonseksempler
- Oppdatert seksjon for repositorisstruktur til å inkludere alle siste filer
- Forbedret "Hvordan bruke denne læreplanen" med tydelige anbefalinger
- Oppdatert MCP-spesifikasjonslenker til å peke til korrekte URLer
- Lagt til seksjon om kontekstteknikk (5.14) i kursstrukturen

### Oppdateringer i studieveiledning
- Fullstendig revidert studieveiledningen for å samsvare med nåværende repositorisstruktur
- Lagt til nye seksjoner for MCP-klienter og -verktøy, og populære MCP-servere
- Oppdatert Visuell Læreplanoversikt for å korrekt vise alle emner
- Forbedret beskrivelser av avanserte emner for å dekke alle spesialiserte områder
- Oppdatert seksjon Casestudier for å gjenspeile faktiske eksempler
- Lagt til denne omfattende endringsloggen

### Fellesskapsbidrag (06-CommunityContributions/)
- Lagt til detaljert informasjon om MCP-servere for bilde-generering
- Lagt til omfattende seksjon om bruk av Claude i VSCode
- Lagt til instruksjoner for oppsett og bruk av Cline terminalklient
- Oppdatert MCP-klientseksjon for å inkludere alle populære klientalternativer
- Forbedret bidragseksempler med mer nøyaktige kodeeksempler

### Avanserte emner (05-AdvancedTopics/)
- Organisert alle spesialiserte emnemapper med konsistent navngivning
- Lagt til materiell og eksempler for kontekstteknikk
- Lagt til dokumentasjon for Foundry agent-integrasjon
- Forbedret dokumentasjon for sikkerhetsintegrasjon med Entra ID

## 11. juni 2025

### Første utgivelse
- Utgitt første versjon av MCP for Beginners læreplan

- Opprettet grunnleggende struktur for alle 10 hovedseksjoner
- Implementerte Visuell Læreplankart for navigasjon
- La til innledende prøveprosjekter i flere programmeringsspråk

### Komme i gang (03-GettingStarted/)
- Opprettet første serverimplementeringseksempler
- La til veiledning for klientutvikling
- Inkluderte instruksjoner for LLM-klientintegrasjon
- La til dokumentasjon for VS Code-integrasjon
- Implementerte Server-Sent Events (SSE) servereksempler

### Kjernebegreper (01-CoreConcepts/)
- La til detaljert forklaring av klient-server-arkitektur
- Opprettet dokumentasjon om nøkkelkomponenter i protokollen
- Dokumenterte meldingsmønstre i MCP

## 23. mai 2025

### Repositoriumstruktur
- Initialiserte repositoriet med grunnleggende mappestruktur
- Opprettet README-filer for hver hovedseksjon
- Satte opp oversettelsesinfrastruktur
- La til bilde-ressurser og diagrammer

### Dokumentasjon
- Opprettet første README.md med oversikt over læreplanen
- La til CODE_OF_CONDUCT.md og SECURITY.md
- Satte opp SUPPORT.md med veiledning for å få hjelp
- Opprettet foreløpig studieveiledningsstruktur

## 15. april 2025

### Planlegging og rammeverk
- Innledende planlegging for MCP for Beginners læreplan
- Definerte læringsmål og målgruppe
- Skisset opp 10-delt struktur for læreplanen
- Utviklet konseptuelt rammeverk for eksempler og casestudier
- Opprettet første prototypeeksempler for nøkkelbegreper

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
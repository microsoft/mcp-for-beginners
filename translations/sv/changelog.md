# Ändringslogg: MCP för nybörjare läroplan

Detta dokument fungerar som en logg över alla betydande ändringar som gjorts i Model Context Protocol (MCP) för nybörjare läroplan. Ändringar dokumenteras i omvänd kronologisk ordning (nyaste ändringarna först).

## 29 juli 2026

### Ny modul 08 följeslagare: Pålitliga sidovagnar och säkra omförsök

Lagt till en leverantörsoberoende följelärdom för MCP-verktyg som skapar verklighetsbaserade
effekter, i linje med den slutliga `2026-07-28` specifikationen.

- **Ny**: [följeslagarlektions om pålitliga sidovagnar][reliability-sidecar]
  använder en supportärendeberättelse, två Mermaid-diagram och ett beslutsflöde för omförsök
  för att förklara stabila driftnycklar, atomär dubblettillåtelse,
  försoning, bevis och Tasks-förlängningsgränsen.
- **Ny**: En standardbiblioteksövning i Python och SQLite med felinjektion
  använder separata drift- och ärendebutiker för att demonstrera ett förlorat svar
  efter att en extern effekt har slutförts. Sex deterministiska tester täcker naiv
  duplicering, skyddad omstartsåterställning, payloadkonflikter, cachade resultat,
  aktiva krav och samtidig dubblettillåtelse.
- **Uppdaterad**: Modul 08 länkar nu följeslagarletionen, identifierar den
  slutgiltiga `2026-07-28` statslösa begäransmodellen, skiljer OpenTelemetry
  observerbarhet från den föråldrade MCP-loggningsfunktionen, och begränsar sitt
  generiska exempel på omförsök till skrivskyddade operationer.
- **Valfri**: Lektionen kartlägger sina portabla begrepp till en taggad community-
  implementation utan att göra den hostade tjänsten eller ett nätverksanrop till
  en del av övningen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juli 2026

### Ny lektion: MCP-specifikations releasekandidat 2026-07-28

Lagt till täckning av den kommande `2026-07-28` MCP-specifikations releasekandidat (meddelad 21 maj 2026; slutlig release planerad till 28 juli 2026), sammanfattad från [det officiella tillkännagivandeblogginlägget](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Läroplanens baslinje är fortfarande **MCP Specification 2025-11-25** tills den nya versionen släpps, så detta presenteras som framåtblickande vägledning snarare än en omskrivning av befintliga lektioner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — en full lektion som täcker kärnan i det statslösa protokollet (borttagning av `initialize` handskakningen och `Mcp-Session-Id`), de nya `Mcp-Method`/`Mcp-Name` routningshuvudena, `ttlMs`/`cacheScope` cachningsmetadata, W3C Trace Context i `_meta`, det formella Extensions-ramverket (MCP-appar och den nya Tasks-förlängningen), sex auktoriseringsförstärkande SEPs, avvecklingen av Roots/Sampling/Logging och övergången till fullständigt JSON Schema 2020-12 för verktygsscheman.
- **Uppdaterad** med framåtblickande anmärkningar och länkar till den nya lektionen:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollversionsnotis, sektioner för Sampling/Roots/Logging/Tasks samt "Vad kommer härnäst"
  - [02-Security/README.md](./02-Security/README.md): anmärkning om auktoriseringsförstärkning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): anmärkning om statslös transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): anmärkning om avveckling av Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): anmärkning om avveckling av Logging och Tasks-förlängningen
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): anmärkning om statslös/session-routning
  - [README.md](./README.md): "Ser fram emot" notis i specifikationsavsnittet och en ny `1.1` post i läroplansmodultabellen
  - [study_guide.md](./study_guide.md): framåtblickande punkt under Core Concepts-översikten och en daterad tilläggsnotis
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): anmärkning om `mcp-session-id` transportkarta inför den statslösa begäransmodellen
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): modulöversikt anmärkning om Root Contexts/Sampling-avvecklingar och Tasks-förlängningen
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): anmärkning om auktoriseringsförstärkning

## 24 juni 2026

### Ny lektion: Använda MCP i Copilot-app

- [Verktygsavsnitt](./12-tooling/README.md) Lagt till verktygsavsnitt.
- [MCP i Copilot-app](./12-tooling/01-copilot-app/README.md)

## 16 juni 2026

### MCP-specifikationsanpassning och exempelvalidering

Validerade läroplanen mot nuvarande **MCP Specification 2025-11-25** och de senaste officiella SDK:erna, korrigerade sedan kvarstående föråldrade specifikationsreferenser och bekräftade att huvudexemplen fortfarande kan byggas och köras.

#### Specifikationsversionskorrigeringar (2025-06-18 / 2025-03-26 → 2025-11-25)

Uppdaterade engelsk text där den fortfarande hävdade att en äldre spec-revision var *nuvarande/senaste* standard, och pekade om länkar till de kanoniska `modelcontextprotocol.io` spec-vägarna:
- **05-AdvancedTopics/mcp-security/README.md**: Uppdaterade "Current Standard"-banderollen, introduktionen, kärnsäkerhetsprinciprubriken, obligatoriska krav-rubriken, Microsoft Entra ID-sektionen, Referenser & Resurslänkarna samt avslutande säkerhetsnotis (8 referenser) till 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Uppdaterade länken till Ytterligare Resurser-specifikationen och "Current Standard"-banderollen till 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Ersatte den föråldrade `2025-03-26` länken till security-and-trust med den aktuella säkerhets-bästapraxis sidan för 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Uppdaterade den officiella samplingdokumentationslänken till 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Uppdaterade referensen till nutida "nuvarande MCP-specifikation" och länken till ytterligare resurser för specifikation till 2025-11-25 (historiska SSE-avvecklingsanteckningar lämnade intakta för noggrannhet)

#### Exempelvalidering mot aktuella SDK:er

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` löste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` klarade utan typfel — befintliga `McpServer`/`StdioServerTransport` API:er är fortfarande giltiga
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validerad i en isolerad `.venv` med `mcp[cli]` (1.27.2); `py_compile` gick igenom och `FastMCP.list_tools()` returnerade korrekt verktygen `add` och `subtract`
- Bekräftade att alla exempel `@modelcontextprotocol/sdk` versionsintervall (`>=1.26.0` / `^1.26.0` / `^1.27.0`) löses smidigt till nuvarande `1.29.0` utan brytande API-ändringar

#### Justering av beroendepinnar (stänger versionsgap)

Uppdaterade föråldrade SDK-pinnar så varje exempel följer nuvarande MCP-release, enligt repövergripande konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Uppdaterade `@modelcontextprotocol/sdk` från `^1.8.0` → `>=1.26.0` och ändrade den inaktuella paketbeskrivningen `"updated for MCP 2025-06-18"` till `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** och **lab4/code/github_mcp_server/pyproject.toml**: Uppdaterade exakt pin `mcp==1.23.0` → `mcp>=1.26.0`; regenererade båda `uv.lock`-filer (`uv lock`) så låsfilerna löses till aktuella `mcp 1.27.2` och är i synk med manifesten

#### Analys av kursluckor — Senaste specifikationsfunktionernas täckning

Bekräftat att kursinnehållet redan täcker alla primitiva som introducerats/utökats i MCP 2025-11-25, så inga innehållsluckor finns kvar:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-läge)**: Dokumenterat i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumenterat i 00-Introduction, 01-CoreConcepts och 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentella, långvariga operationer)**: Dokumenterat i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features
- **Verktygsanvisningar** (`readOnlyHint` / `destructiveHint`): Dokumenterat i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features

### Säkerhetsförstärkning & åtgärdande av beroendesårbarheter

Genomförde en full säkerhetsgenomgång av varje beroendemani-fest och exempelkälla, och åtgärdade alla rapporterade npm-anvisningar och en kodnivåfynd. Efter åtgärder visar `npm audit` **0 sårbarheter** i varje granskad katalog.

#### npm-beroendesårbarheter (transitiva) — Åtgärdade

Granskade alla 15 incheckade `package-lock.json`-filer. Sårbarheter begränsades till transitiva beroenden som drogs in av MCP Inspector-utvecklingsverktyget, OpenAI-klienten och MCP SDK; alla är nu lösta utan att exemplen bryts:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** och **lab3/code/weather_mcp/inspector**: Uppdaterade `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), vilket rensade bundlade `ajv`, `brace-expansion`, `diff`, `path-to-regexp` och `ws` anvisningar. Lade till en npm `overrides` post som tvingar fram patchade `shell-quote@1.8.4` för att eliminera kvarvarande kritiska anvisning från `concurrently`; regenererade båda låsfilerna (nu 0 sårbarheter)
- **03-GettingStarted/samples/typescript**: `npm audit fix` uppdaterade transitiva `qs` (måttlig) till en patchad version
- **03-GettingStarted/samples/javascript**: `npm audit fix` uppdaterade transitiva `hono` (måttlig) till en patchad version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` uppdaterade transitiva `form-data` (hög) till en patchad version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genererade den saknade `package-lock.json` så projektet är reproducerbart och granskningsbart (0 sårbarheter)

#### Kodnivåsäkerhetsfix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Tog bort `shell=True` från `open_in_vscode` verktyget. Tidigare `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillät shell-metatecken i en mappsökväg att tolkas av `cmd.exe` (kommandoinjektionsvektor). Det startar nu det upplösta `Code.exe` direkt med mappen som argument - utan shell - vilket är funktionellt ekvivalent och säkert

#### Pythonberoendegranskning

- Granskade varje Python-kravssats med `pip-audit`. `05-AdvancedTopics` och `03-GettingStarted/samples/python` rapporterade **inga kända sårbarheter** (deras `mcp` / `httpx` / `pydantic` / `python-dotenv` intervall löses till aktuella patchade versioner)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flaggade transitiva beroendet **`werkzeug` 3.1.1** med tre `safe_join` Windows-enhetsnamns DoS-anvisningar — `CVE-2025-66221`, `CVE-2026-21860` och `CVE-2026-27199` (alla fixade i 3.1.6). Lade till ett explicit säkerhetspinne `werkzeug>=3.1.6` så patched release löses; verifierade att restriktionen löses rent med `chainlit` / `mcp` / `semantic-kernel` stacken

### Produktnamns-omprofilering

Uppdaterade allt kursmaterial för att reflektera Microsofts produktomprofilering:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Uppdaterad Discord-community-länk

- **AGENTS.md**: Uppdaterad referens till Discord-servern
- **README.md**: Uppdaterade referenser till teknologiekosystemet
- **study_guide.md**: Uppdaterade referenser till fallstudier
- **05-AdvancedTopics/README.md**: Uppdaterad titel och beskrivning för modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Uppdaterad avsnittsrubrik och beskrivning
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Fullständig uppdatering av modultitel och innehåll
- **05-AdvancedTopics/mcp-security-entra/README.md**: Uppdaterad korsreferenslänk
- **07-LessonsfromEarlyAdoption/README.md**: Uppdaterade referenser till fallstudier
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Uppdaterad rubrik för avsnitt 9, badges och kapaciteter
- **08-BestPractices/README.md**: Uppdaterad länk till Discord-community
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Uppdaterad referens till Discord-kanal
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Uppdaterad referens för modellutplacering
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Uppdaterad tabell för AI-tjänster
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Uppdaterade resursreferenser

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension för VS Code
- **README.md**: Uppdaterade huvudreferenser i kursplanen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Uppdaterad modultitel, översikt och alla modulkategorier
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Uppdaterad titel, inlärningsmål, installationsinstruktioner och resurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Uppdaterad titel, inlärningsmål, tabell över MCP-värdar och korsreferenser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Uppdaterad titel, badges, förkunskapskrav och resurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Uppdaterade referenser för Agent Builder och länk för feedback
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Uppdaterade förkunskapskrav och extensionsreferenser

---

## 11 april 2026

### Ny lektion, dokumentationskorrigeringar och beroendeuppdateringar

#### Nytt kursinnehåll tillagt

**Modul 05 - Avancerade Ämnen**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattande guide som täcker den adversariella debattmodellen för multi-agent system
  - Mermaid arkitekturdiagram: två agenter → delad MCP-server → debatttranskript → domare → domslut
  - Delad MCP-verktygsserver (`web_search` + `run_python`) implementerad i Python och TypeScript
  - Motstående systemuppmaningar (FOR / AGAINST / Domare) med uttryckliga krav för verktygsanvändning
  - Debattregissör i Python, TypeScript och C# som hanterar rundor och dirigerar argument
  - MCP `ClientSession` koppling för regissören till riktiga verktygsanrop
  - Användartabell (hallucinationsdetektion, hotmodellering, API-designgranskning, faktakontroll, teknikval)
  - Säkerhetsöverväganden: sandlådemiljö för exekvering, validering av verktygsanrop, hastighetsbegränsning, revisionsloggning
  - Strukturerad övning med tre praktiska scenarier (kodgranskning, arkitekturval, innehållsmoderering)

#### Dokumentationskorrigeringar

**Modul 03 - Kom igång**
- **05-stdio-server/README.md**: Rättat ofullständigt exempel på TypeScript stdio-server — lade till saknad transportinitiering (`new StdioServerTransport()`) och `server.connect(transport)` anrop för att matcha Python- och .NET-exemplen i samma avsnitt
- **14-sampling/README.md**: Rättade skrivfel — korrigerat `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kursplanuppdateringar

**Huvudsaklig README.md**
- Lade till post 5.17 (Adversarial Multi-Agent Reasoning med MCP) i kursplantabellen med direktlänk till nya lektionen

**05-AdvancedTopics/README.md**
- Lade till rad för Lektion 5.17 i tabellen för lektioner

**study_guide.md**
- Lade till ämnet Adversarial Multi-Agent Reasoning i tankekartan och löpande beskrivning av Avancerade Ämnen

#### Kod- och säkerhetsfixar

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Säkerhetsfix — kommandoinjektion**: Ersatte `execSync` shell-interpolering med `execFile` + `promisify` i TypeScript-verktyget `run_python`, vilket eliminerar injektionsytan (LLM-styrd kod skickas nu som ett literalt argv-element utan shell-inblandning)
- **MCP verktygsslingskoppling**: Uppdaterade Python debattregissör att använda `AsyncAnthropic` klient (ersätter blockerande sync `Anthropic`), skickar en live `ClientSession` direkt till varje agenttur, hämtar verktygsdefinitioner via `session.list_tools()` varje tur, och skickar `tool_use` block via `session.call_tool()` i slinga tills modellen ger slutlig textrespons

#### Beroendeuppdateringar

- Uppgraderade `hono` till 4.12.12 i flera paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uppgraderade `@hono/node-server` från 1.19.11 till 1.19.13 i TypeScript-paket
- Uppgraderade `cryptography` från 46.0.5 till 46.0.7 i Python-paket (10-StreamliningAIWorkflows labbar 3 och 4)
- Uppgraderade `lodash` från 4.17.23 till 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Översättningar

- Synkroniserade översättningar för 48+ språk med senaste källändringar (i18n uppdatering)

---

## 5 februari 2026

### Förbättringar av validering och navigation för hela repositoryt

#### Nytt kursinnehåll tillagt

**Modul 03 - Kom igång**
- **12-mcp-hosts/README.md**: Ny omfattande guide för att sätta upp MCP-värdar
  - Exempel på konfiguration för Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-konfigurationmallar för alla större värdar
  - Jämförelsetabell över transporttyper (stdio, SSE/HTTP, WebSocket)
  - Felsökning av vanliga anslutningsproblem
  - Säkerhetsbästa praxis för värdkonfiguration

- **13-mcp-inspector/README.md**: Ny felsökningsguide för MCP Inspector
  - Installationsmetoder (npx, npm globalt, från källkod)
  - Anslutning till servrar via stdio och HTTP/SSE
  - Testningsverktyg, resurser och promptarbetsflöden
  - VS Code-integration med MCP Inspector
  - Vanliga felsökningsscenarier med lösningar

**Modul 04 - Praktisk Implementering**
- **pagination/README.md**: Ny guide för sidindelning
  - Cursor-baserade sidindelningsmönster i Python, TypeScript, Java
  - Hantering av sidindelning på klientsidan
  - Cursor-designstrategier (opförtunnade kontra strukturerade)
  - Rekommendationer för prestandaoptimering

**Modul 05 - Avancerade Ämnen**
- **mcp-protocol-features/README.md**: Ny djupdykning i protokollfunktioner
  - Implementering av framstegssignaler
  - Mönster för avbeställning av förfrågningar
  - Resursmallar med URI-mönster
  - Hantering av serverns livscykel
  - Kontroll av loggnivå
  - Felhanteringsmönster med JSON-RPC-koder

#### Navigationskorrigeringar (24+ filer uppdaterade)

**Huvudmodul-README-filer**
 Länkar nu till både första lektionen OCH nästa modul

**02-Säkerhetsunderfiler**
- Alla 5 kompletterande säkerhetsdokument har nu "Vad är nästa" navigation:

**09-CaseStudy-filer**
- Alla fallstudiefiler har nu sekventiell navigation:

**10-StreamliningAI-labbar**
Lade till sektionen "Vad är nästa" i Modul 10 översikt och Modul 11

#### Kod- och innehållskorrigeringar

**SDK- och beroendeuppdateringar**
Rättade tom openai-version till `^4.95.0`
Uppdaterade SDK från `^1.8.0` till `>=1.26.0`
Uppdaterade mcp versionspinnar till `>=1.26.0`

**Kodkorrigeringar**
Rättade ogiltig modell `gpt-4o-mini` till `gpt-4.1-mini`

**Innehållskorrigeringar**
Rättade trasig länk `READMEmd` → `README.md`, rättade kursplanrubrik `Module 1-3` → `Module 0-3`, rättade skiftlägeskänslig sökväg
Tog bort korrupt duplicerat innehåll i Case Study 5

**Förbättringar för nybörjarguide**
Lade till korrekt introduktion, inlärningsmål och förkunskapskrav för nybörjare

#### Kursplanuppdateringar

**Huvudsaklig README.md**
- Lade till poster 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) i kursplantabellen

**Modul-README-filer**
Lade till lektioner 12 och 13 i lektionslistan
Lade till avsnitt Praktiska guider med länkar för sidindelning
Lade till lektioner 5.15 (Anpassad Transport) och 5.16 (Protokollfunktioner)

**study_guide.md**
- Uppdaterade tankekartan med alla nya ämnen: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## 28 januari 2026

### Översyn av överensstämmelse med MCP-specifikation 2025-11-25

#### Förbättring av kärnkoncept (01-CoreConcepts/)
- **Ny klient-primitiv - Roots**: Lade till omfattande dokumentation om Roots klient-primitiv som gör det möjligt för servrar att förstå filsystemgränser och åtkomsträttigheter
- **Verktygsannoteringar**: Lade till dokumentation om beteendeannoteringar för verktyg (`readOnlyHint`, `destructiveHint`) för bättre beslut om verktygsexekvering
- **Verktygsanrop i Sampling**: Uppdaterade Sampling-dokumentationen för att inkludera parametrarna `tools` och `toolChoice` för modellstyrda verktygsanrop vid samplingförfrågningar
- **URL Mode Elicitation**: Lade till dokumentation om URL-baserad elicitation för serverinitierade externa webbinteraktioner
- **Tasks (Experimentellt)**: Lade till nytt avsnitt som dokumenterar den experimentella funktionaliteten Tasks för hållbara exekveringsomslag och fördröjd resultatåtervinning
- **Ikonsupport**: Nämnde att verktyg, resurser, resursmallar och prompts nu kan inkludera ikoner som ytterligare metadata

#### Dokumentationsuppdateringar
- **README.md**: Lade till referens till MCP-specifikation 2025-11-25 version och förklaring av versionshantering baserad på datum
- **study_guide.md**: Uppdaterade kursplanskartläggning för att inkludera Tasks och Tool Annotations i avsnittet för kärnkoncept; uppdaterad dokumentets tidsstämpel

#### Verifiering av specifikationsöverensstämmelse
- **Protokollversion**: Verifierade att all dokumentation refererar till nuvarande MCP-specifikation 2025-11-25
- **Arkitekturefterlevnad**: Bekräftade att dokumentationen av tvåskiktsarkitekturen (Data Layer + Transport Layer) är korrekt
- **Dokumentation av primitiva element**: Validerade serverprimitiver (Resurser, Prompts, Verktyg) och klientprimitiver (Sampling, Elicitation, Logging, Roots)
- **Transportmekanismer**: Verifierade korrekthet för STDIO och Streamable HTTP-transportdokumentation
- **Säkerhetsvägledning**: Bekräftade överensstämmelse med aktuell MCP säkerhetsbästa praxis-dokumentation

#### Nyckelfunktioner i MCP 2025-11-25 dokumenterade
- **OpenID Connect Discovery**: Autentiseringsserverupptäckt via OIDC
- **OAuth Client ID Metadata-dokument**: Rekommenderad klientregistreringsmekanism
- **JSON Schema 2020-12**: Standarddialekt för MCP schema-definitioner
- **SDK-tiering system**: Formaliserade krav för SDK-funktionsstöd och underhåll
- **Styrningsstruktur**: Formaliserade arbetsgrupper och intressegrupper i MCP-styrningen

### Större säkerhetsdokumentationsuppdatering (02-Säkerhet/)

#### Integrering av MCP Security Summit Workshop (Sherpa)
- **Nytt praktiskt träningsresurs**: Lade till omfattande integrering med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all säkerhetsdokumentation
- **Resväg för expeditionen**: Dokumentationen av den kompletta camp-till-camp-progressionen från Base Camp till Summit
- **OWASP-överensstämmelse**: All säkerhetsvägledning kopplad till OWASP MCP Azure Security Guide risker

#### Integrering av OWASP MCP Top 10
- **Nytt avsnitt**: Lade till tabell över OWASP MCP Top 10 säkerhetsrisker med Azure-mitigeringar i huvudsäkerhets-README
- **Riskbaserad dokumentation**: Uppdaterade mcp-security-controls-2025.md med OWASP MCP riskreferenser för varje säkerhetsdomän
- **Referensarkitektur**: Länkade till OWASP MCP Azure Security Guide referensarkitektur och implementeringsmönster

#### Uppdaterade säkerhetsfiler
- **README.md**: Lade till översikt för Sherpa-workshop, tabell över expeditonsrutt, sammanfattning av OWASP MCP Top 10-risker samt avsnitt för handgriplig träning
- **mcp-security-controls-2025.md**: Uppdaterad rubrik till februari 2026, lade till OWASP-riskreferenser (MCP01-MCP08), fixade versionsinkonsekvens i specifikation
- **mcp-security-best-practices-2025.md**: Lade till sektion med Sherpa och OWASP resurser, uppdaterad tidsstämpel
- **mcp-best-practices.md**: Lade till sektion för praktisk träning med länkar till Sherpa och OWASP
- **azure-content-safety-implementation.md**: Lade till referens för OWASP MCP06, anpassning till Sherpa Camp 3 samt sektion med ytterligare resurser

#### Nya resurslänkar tillagda
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuella OWASP MCP risk sidor (MCP01-MCP10)

### Läroplansomfattande MCP-specifikation 2025-11-25 Justering

#### Modul 03 - Komma igång
- **SDK Dokumentation**: Lagt till Go SDK i den officiella SDK-listan; uppdaterade alla SDK-referenser för att stämma överens med MCP-specifikation 2025-11-25
- **Transportförtydligande**: Uppdaterade STDIO- och HTTP-strömningstransportbeskrivningar med uttryckliga spec-referenser

#### Modul 04 - Praktisk Implementering
- **SDK-uppdateringar**: Lagt till Go SDK; uppdaterade SDK-listan med specifikationsversionsreferens
- **Auktoriseringsspecifikation**: Uppdaterade MCP Authorization-specifikationslänk till nuvarande version 2025-11-25

#### Modul 05 - Avancerade Ämnen
- **Nya Funktioner**: Lagt till notering om nya MCP-specifikation 2025-11-25 funktioner (Uppgifter, Verktygsannoteringar, URL-lägesfrågeställning, Rötter)
- **Säkerhetsresurser**: Lagt till OWASP MCP Top 10 och Sherpa workshop länkar till ytterligare referenser

#### Modul 06 - Communitybidrag
- **SDK-lista**: Lagt till Swift och Rust SDKs; uppdaterade specifikationslänk till 2025-11-25
- **Spec-referens**: Uppdaterade MCP-specifikationslänk till direkt specifikations-URL

#### Modul 07 - Lärdomar från tidig adoption
- **Resursuppdateringar**: Lagt till MCP-specifikation 2025-11-25 länk och OWASP MCP Top 10 till ytterligare resurser

#### Modul 08 - Bästa Praxis
- **Spec versionsuppdatering**: Uppdaterade MCP-specifikationsreferens till 2025-11-25
- **Säkerhetsresurser**: Lagt till OWASP MCP Top 10 och Sherpa workshop till ytterligare referenser

#### Modul 10 - Effektivisering av AI-arbetsflöden
- **Märkesuppdatering**: Ändrat MCP versionsmärke från SDK-version (1.9.3) till specifikationsversion (2025-11-25)
- **Resurslänkar**: Uppdaterade MCP-specifikationslänk; lade till OWASP MCP Top 10

#### Modul 11 - MCP Server Praktiska Laborationer
- **Spec-referens**: Uppdaterade MCP-specifikationslänk till version 2025-11-25
- **Säkerhetsresurser**: Lagt till OWASP MCP Top 10 till officiella resurser

## 18 december 2025

### Säkerhetsdokumentationsuppdatering - MCP Specifikation 2025-11-25

#### MCP Säkerhetsbästa praxis (02-Security/mcp-best-practices.md) - Specifikationsversionsuppdatering
- **Protokollversionsuppdatering**: Uppdaterade för att referera till senaste MCP-specifikation 2025-11-25 (släppt 25 november 2025)
  - Uppdaterade alla specifikationsversionsreferenser från 2025-06-18 till 2025-11-25
  - Uppdaterade dokumentdatumreferenser från 18 augusti 2025 till 18 december 2025
  - Verifierade att alla specifikations-URL:er pekar till aktuell dokumentation
- **Innehållsvalidering**: Omfattande validering av säkerhetsbästa praxis mot senaste standarder
  - **Microsoft Säkerhetslösningar**: Verifierade aktuell terminologi och länkar för Prompt Shields (tidigare "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, och Azure Key Vault
  - **OAuth 2.1 Säkerhet**: Bekräftade överensstämmelse med senaste OAuth säkerhetsbästa praxis
  - **OWASP-standarder**: Validerade att OWASP Top 10 för LLMs-referenserna är aktuella
  - **Azure Tjänster**: Verifierade alla Microsoft Azure-dokumentationslänkar och bästa praxis
- **Standardanpassning**: Alla refererade säkerhetsstandarder bekräftade som aktuella
  - NIST AI Riskhanteringsramverk
  - ISO 27001:2022
  - OAuth 2.1 säkerhetsbästa praxis
  - Azure säkerhets- och efterlevnadsramverk
- **Implementeringsresurser**: Verifierade alla implementeringsguide-länkar och resurser
  - Azure API Management autentiseringsmönster
  - Microsoft Entra ID integrationsguider
  - Azure Key Vault secrets-hantering
  - DevSecOps pipeline- och övervakningslösningar

### Dokumentationskvalitetssäkring
- **Specifikationsöverensstämmelse**: Säkerställde att alla obligatoriska MCP säkerhetskrav (MÅSTE/MÅSTE INTE) stämmer överens med senaste specifikationen
- **Aktualitet av resurser**: Verifierade alla externa länkar till Microsoft-dokumentation, säkerhetsstandarder och implementeringsguider
- **Täcker bästa praxis**: Bekräftade omfattande täckning av autentisering, auktorisering, AI-specifika hot, leveranskedjesäkerhet och företagsmönster

## 6 oktober 2025

### Utökning av Kom igång-sektionen – Avancerad serveranvändning & Enkel autentisering

#### Avancerad serveranvändning (03-GettingStarted/10-advanced)
- **Ny kapitel tillagd**: Introducerade en omfattande guide för avancerad MCP-serveranvändning, som täcker både reguljär och låg-nivå serverarkitektur.
  - **Reguljär vs. låg-nivå server**: Detaljerad jämförelse och kodexempel i Python och TypeScript för båda tillvägagångssätten.
  - **Handler-baserad design**: Förklaring av hanterarebaserad verktyg-/resurs-/prompt-hantering för skalbara, flexibla serverimplementationer.
  - **Praktiska mönster**: Verkliga scenarier där låg-nivå servermönster är fördelaktiga för avancerade funktioner och arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Ny kapitel tillagd**: Steg-för-steg-guide för att implementera enkel autentisering i MCP-servrar.
  - **Autentiseringskoncept**: Tydlig förklaring av autentisering vs. auktorisering, och hantering av inloggningsuppgifter.
  - **Grundläggande autentiseringsimplementering**: Middleware-baserade autentiseringsmönster i Python (Starlette) och TypeScript (Express), med kodexempel.
  - **Framsteg till avancerad säkerhet**: Vägledning för att börja med enkel autentisering och gå vidare till OAuth 2.1 och RBAC, med referenser till avancerade säkerhetsmoduler.

Dessa tillägg ger praktisk, handgriplig vägledning för att bygga mer robusta, säkra och flexibla MCP-serverimplementeringar, och förbinder grundläggande koncept med avancerade produktionsmönster.

## 29 september 2025

### MCP Server Databasintegrationslaborationer - Omfattande praktisk inlärningsväg

#### 11-MCPServerHandsOnLabs - Ny komplett läroplansserie för databasintegration
- **Fullständig 13-laborations läroväg**: Lagt till omfattande praktisk läroplan för att bygga produktionsfärdiga MCP-servrar med PostgreSQL databasintegration
  - **Verklig implementering**: Zava Retail analytics-användningsfall som demonstrerar företagsmönster
  - **Strukturerad inlärningsprogression**:
    - **Labbar 00-03: Grunder** - Introduktion, Kärnarkitektur, Säkerhet & Multi-Tenancy, Miljöinställning
    - **Labbar 04-06: Bygga MCP-server** - Databasdesign & Schema, MCP-serverimplementering, Verktygsutveckling  
    - **Labbar 07-09: Avancerade funktioner** - Semantisk sökintegration, Testning & felsökning, VS Code-integration
    - **Labbar 10-12: Produktion & bästa praxis** - Distribueringsstrategier, Övervakning & Observabilitet, Bästa praxis & optimering
  - **Företagsteknologier**: FastMCP-ramverk, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avancerade funktioner**: Radnivåsäkerhet (RLS), semantisk sökning, multi-tenant dataåtkomst, vektorinfodringar, realtidsövervakning

#### Terminologistandardisering - Modul till labb-konvertering
- **Omfattande dokumentationsuppdatering**: Systematiskt uppdaterat alla README-filer i 11-MCPServerHandsOnLabs för att använda "Lab" terminologi istället för "Modul"
  - **Sektionstitlar**: Uppdaterade "Vad denna modul täcker" till "Vad detta labb täcker" i alla 13 labbar
  - **Innehållsbeskrivning**: Ändrade "Denna modul tillhandahåller..." till "Detta labb tillhandahåller..." genom all dokumentation
  - **Lärandemål**: Uppdaterade "I slutet av denna modul..." till "I slutet av detta labb..." 
  - **Navigeringslänkar**: Omvandlade alla "Modul XX:" referenser till "Labb XX:" i korsreferenser och navigering
  - **Avslutningsspårning**: Uppdaterade "Efter att ha slutfört denna modul..." till "Efter att ha slutfört detta labb..."
  - **Bevarade tekniska referenser**: Behöll Python modulreferenser i konfigurationsfiler (t.ex. `"module": "mcp_server.main"`)

#### Förbättring av studievägledning (study_guide.md)
- **Visuell läroplansöversikt**: Lagt till ny sektion "11. Databasintegrationslabbar" med omfattande labbstrukturvisualisering
- **Förrådsstruktur**: Uppdaterad från tio till elva huvudsektioner med detaljerad beskrivning av 11-MCPServerHandsOnLabs
- **Vägledning av inlärningsväg**: Förbättrade navigationsinstruktioner som täcker sektioner 00-11
- **Teknologitäckning**: Lagt till FastMCP, PostgreSQL, Azure-tjänsters integrationsdetaljer
- **Läranderesultat**: Betonade produktionsfärdig serverutveckling, databasintegrationsmönster och företagsäkerhet

#### Förbättring av huvudsaklig README-struktur
- **Labb-baserad terminologi**: Uppdaterade huvud README.md i 11-MCPServerHandsOnLabs för att konsekvent använda "Labb"-struktur
- **Organisering av inlärningsväg**: Tydlig progression från grundläggande koncept via avancerad implementering till produktionsdistribution
- **Verklighetsfokus**: Betoning på praktisk, handgriplig inlärning med företagsmönster och teknologier

### Dokumentationskvalitet och konsekvensförbättringar
- **Praktisk inlärning i fokus**: Förstärkt praktisk, labb-baserad metod över hela dokumentationen
- **Fokus på företagsmönster**: Betoning på produktionsfärdiga implementationer och företagsäkerhetshänsyn
- **Teknologiintegration**: Omfattande täckning av moderna Azure-tjänster och AI-integrationsmönster
- **Inlärningsprogression**: Tydlig, strukturerad väg från grundläggande koncept till produktionsdistribution

## 26 september 2025

### Förbättring av fallstudier - GitHub MCP Registry-integration

#### Fallstudier (09-CaseStudy/) - Fokus på ekosystemutveckling
- **README.md**: Stor utökning med omfattande GitHub MCP Registry fallstudie
  - **GitHub MCP Registry Fallstudie**: Ny omfattande fallstudie som granskar GitHubs MCP Registry-lansering i september 2025
    - **Problemanalys**: Detaljerad granskning av fragmenterad MCP-serverupptäckt och distributionsutmaningar
    - **Lösningsarkitektur**: GitHubs centraliserade registertillvägagångssätt med en-klicks VS Code-installation
    - **Affärspåverkan**: Mätbara förbättringar i utvecklarintroduktion och produktivitet
    - **Strategiskt värde**: Fokus på modulär agentdistribution och interoperabilitet mellan verktyg
    - **Ekosystemutveckling**: Positionering som grundplattform för agentbaserad integration
  - **Förbättrad fallstudiestruktur**: Uppdaterade alla sju fallstudier med konsekvent formatering och omfattande beskrivningar
    - Azure AI Travel Agents: Betoning på multi-agent orkestrering
    - Azure DevOps-integration: Fokus på arbetsflödesautomatisering
    - Realtidsdokumenthämtning: Python-konsolkundimplementering
    - Interaktiv studieplangenerator: Chainlit konversationswebbapp
    - Dokumentation i redigeraren: VS Code och GitHub Copilot integration
    - Azure API Management: Företags-API-integrationsmönster
    - GitHub MCP Registry: Ekosystemutveckling och community-plattform
  - **Omfattande slutsats**: Omskriven slutsatssektion som lyfter fram sju fallstudier som täcker flera MCP-implementeringsdimensioner
    - Företagsintegration, Multi-agent orkestrering, Utvecklarproduktivitet
    - Ekosystemutveckling, Kategorisering av utbildningsapplikationer
    - Förbättrade insikter i arkitekturmönster, implementeringsstrategier och bästa praxis
    - Betoning på MCP som ett moget, produktionsfärdigt protokoll

#### Uppdateringar av studieguide (study_guide.md)
- **Visuell läroplansöversikt**: Uppdaterad mindmap för att inkludera GitHub MCP Registry i sektionen Fallstudier
- **Fallstudiebeskrivning**: Förbättrad från generiska beskrivningar till detaljerad genomgång av sju omfattande fallstudier
- **Förrådsstruktur**: Uppdaterad sektion 10 för att spegla omfattande fallstudietäckning med specifika implementeringsdetaljer
- **Ändringsloggsintegration**: Lagt till 26 september 2025-post som dokumenterar tillägg av GitHub MCP Registry och förbättringar av fallstudier
- **Datumuppdateringar**: Uppdaterad sidfots tidsstämpel för att återspegla senaste revisionen (26 september 2025)

### Kvalitetsförbättringar i dokumentation
- **Konsekvensförbättring**: Standardiserad formatering och struktur för fallstudier över alla sju exempel
- **Omfattande täckning**: Fallstudierna omfattar nu företags-, utvecklarproduktivitet- och ekosystemutvecklingsscenarier
- **Strategisk positionering**: Förstärkt fokus på MCP som grundläggande plattform för agentbaserad systemdistribution
- **Resursintegration**: Uppdaterade ytterligare resurser för att inkludera GitHub MCP Registry-länk

## 15 september 2025

### Utökning av avancerade ämnen - Anpassade transporter & Kontextteknik

#### MCP Anpassade transporter (05-AdvancedTopics/mcp-transport/) - Ny guide för avancerad implementation
- **README.md**: Komplett guide för implementering av anpassade MCP-transportsmekanismer
  - **Azure Event Grid Transport**: Omfattande serverlös händelsestyrd transportimplementering
    - Exempel i C#, TypeScript och Python med Azure Functions-integration
    - Händelsestyrda arkitekturmodeller för skalbara MCP-lösningar
    - Webhook-mottagare och push-baserad meddelandehantering
  - **Azure Event Hubs Transport**: Höghastighets strömningstransportimplementering
    - Realtidsströmning för låglatensscenarier
    - Partitioneringsstrategier och kontrollpunktshantering
    - Meddelandebatchning och prestandaoptimering
  - **Företagsintegrationsmönster**: Produktionsfärdiga arkitektur-exempel
    - Distribuerad MCP bearbetning över flera Azure Functions
    - Hybridtransportarkitektur som kombinerar flera transporttyper
    - Meddelandehållbarhet, tillförlitlighet och felhanteringsstrategier
  - **Säkerhet & övervakning**: Azure Key Vault-integration och observabilitetsmönster
    - Hanterad identitetsautentisering och principen om minsta privilegium
    - Application Insights telemetri och prestandaövervakning
    - Strömbrytare och felmotståndsmönster
  - **Testningsramverk**: Omfattande teststrategier för anpassade transporter
    - Enhetstester med testdubblar och mocking-ramverk
    - Integrationstester med Azure Test Containers
    - Prestanda- och belastningstestningsöverväganden

#### Kontextteknik (05-AdvancedTopics/mcp-contextengineering/) - Framväxande AI-disciplin
- **README.md**: Omfattande utforskning av kontextteknik som ett framväxande område
  - **Kärnprinciper**: Komplett samdelning av kontext, medvetenhet om åtgärdsbeslut och hantering av kontextfönster

  - **MCP-protokollanpassning**: Hur MCP-design hanterar utmaningar inom kontextteknik
    - Begränsningar i kontextfönster och progressiva inläsningsstrategier
    - Relevansbestämning och dynamisk kontextåtervinning
    - Multimodal kontexthantering och säkerhetsaspekter
  - **Implementeringsmetoder**: Entrådiga kontra multiagent-arkitekturer
    - Tekniker för kontextuppdelning och prioritering
    - Progressiv kontextinläsning och komprimeringsstrategier
    - Lager-på-lager-kontekstilvägagångssätt och optimering av återvinning
  - **Mätramverk**: Framväxande mätvärden för utvärdering av kontexteffektivitet
    - Ingångseffektivitet, prestanda, kvalitet och användarupplevelseöverväganden
    - Experimentella metoder för kontextoptimering
    - Felanalys och förbättringsmetoder

#### Uppdateringar i kursplanen (README.md)
- **Förbättrad modulstruktur**: Uppdaterad kursplanstabell för att inkludera nya avancerade ämnen
  - Tillagt Context Engineering (5.14) och Custom Transport (5.15)
  - Konsekvent formatering och navigeringslänkar i alla moduler
  - Uppdaterade beskrivningar för att spegla aktuellt innehållsomfång

### Förbättringar av katalogstruktur
- **Namnstandardisering**: "mcp transport" omdöpt till "mcp-transport" för att matcha andra avancerade ämnesmappar
- **Innehållsorganisation**: Alla 05-AdvancedTopics-mappar följer nu enhetligt namnmönster (mcp-[ämne])

### Förbättringar av dokumentationskvalitet
- **MCP-specifikationsanpassning**: Allt nytt innehåll refererar till aktuella MCP-specifikation 2025-06-18
- **Fler språkexempel**: Omfattande kodexempel i C#, TypeScript och Python
- **Företagsfokus**: Produktionsklara mönster och Azure-molnintegration överallt
- **Visuell dokumentation**: Mermaid-diagram för arkitektur och flödesvisualisering

## 18 augusti, 2025

### Omfattande dokumentationsuppdatering - MCP 2025-06-18 standarder

#### MCP-säkerhetsbästpraxis (02-Security/) - Fullständig modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Komplett omskrivning i linje med MCP-specifikation 2025-06-18
  - **Obligatoriska krav**: Tillagda uttryckliga SKA/INTE SKA-krav från officiell specifikation med tydliga visuella indikatorer
  - **12 kärnsäkerhetspraxis**: Omstrukturerad från 15-punktslista till omfattande säkerhetsdomäner
    - Tokensäkerhet & autentisering med integration för externa identitetsleverantörer
    - Sessionshantering & transportsäkerhet med kryptografiska krav
    - AI-specifikt hotsskydd med Microsoft Prompt Shields-integration
    - Åtkomstkontroll & behörigheter med principen om minsta privilegium
    - Innehållssäkerhet & övervakning med Azure Content Safety-integration
    - Leverantörskedjesäkerhet med omfattande komponentverifiering
    - OAuth-säkerhet & Confused Deputy-förebyggande med PKCE-implementering
    - Incidenthantering & återhämtning med automatiserade funktioner
    - Efterlevnad & styrning med regleringsanpassning
    - Avancerade säkerhetskontroller med zero trust-arkitektur
    - Microsofts säkerhetsekosystemintegration med omfattande lösningar
    - Kontinuerlig säkerhetsevolution med adaptiva metoder
  - **Microsoft säkerhetslösningar**: Förbättrad integrationsvägledning för Prompt Shields, Azure Content Safety, Entra ID och GitHub Advanced Security
  - **Implementeringsresurser**: Kategoriserade omfattande resurslänkar efter Officiell MCP-dokumentation, Microsoft säkerhetslösningar, säkerhetsstandarder och implementeringsguider

#### Avancerade säkerhetskontroller (02-Security/) - Företagsimplementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fullständig genomgång med säkerhetsramverk i företagsskala
  - **9 omfattande säkerhetsdomäner**: Utökad från grundläggande kontroller till detaljerat företagsramverk
    - Avancerad autentisering & auktorisering med Microsoft Entra ID-integration
    - Tokensäkerhet & anti-passthrough-kontroller med omfattande validering
    - Sessionssäkerhetskontroller med förebyggande av övertagande
    - AI-specifika säkerhetskontroller med skydd mot promptinjektion och verktygsförgiftning
    - Förebyggande av Confused Deputy-attacker med OAuth-proxy-säkerhet
    - Verktygsexekveringssäkerhet med sandboxing och isolering
    - Leverantörskedjesäkerhetskontroller med beroendeverifiering
    - Övervaknings- & detektionskontroller med SIEM-integration
    - Incidenthantering & återhämtning med automatiserade funktioner
  - **Implementeringsexempel**: Tillagda detaljerade YAML-konfigurationsblock och kodexempel
  - **Microsoft-lösningsintegration**: Omfattande täckning av Azure-säkerhetstjänster, GitHub Advanced Security och företagsidentitetshantering

#### Avancerade ämnens säkerhet (05-AdvancedTopics/mcp-security/) - Produktionsredo implementering
- **README.md**: Komplett omskrivning för företagsmässig säkerhetsimplementering
  - **Aktuell specifikationsanpassning**: Uppdaterad till MCP-specifikation 2025-06-18 med obligatoriska säkerhetskrav
  - **Förbättrad autentisering**: Microsoft Entra ID-integration med omfattande .NET- och Java Spring Security-exempel
  - **AI-säkerhetsintegration**: Microsoft Prompt Shields och Azure Content Safety-implementering med detaljerade Python-exempel
  - **Avancerad hotmitigering**: Omfattande implementeringsexempel för
    - Förebyggande av Confused Deputy-attacker med PKCE och användarsamtyckesvalidering
    - Förebyggande av token-passthrough med publikumsvalidering och säker tokenhantering
    - Förebyggande av sessionkapning med kryptografisk bindning och beteendeanalys
  - **Företagssäkerhetsintegration**: Azure Application Insights-övervakning, hotdetektionspipeline och leverantörskedjesäkerhet
  - **Implementeringschecklista**: Tydliga obligatoriska kontra rekommenderade säkerhetskontroller med Microsofts säkerhetsekosystemfördelar

### Dokumentationskvalitet & standardanpassning
- **Specifikationsreferenser**: Uppdaterade alla referenser till aktuella MCP-specifikation 2025-06-18
- **Microsofts säkerhetsekosystem**: Förbättrad integrationsvägledning i all säkerhetsdokumentation
- **Praktisk implementering**: Tillagda detaljerade kodexempel i .NET, Java och Python med företagspraxis
- **Resursorganisation**: Omfattande kategorisering av officiell dokumentation, säkerhetsstandarder och implementeringsguider
- **Visuella indikatorer**: Tydlig markering av obligatoriska krav kontra rekommenderade metoder


#### Kärnkoncept (01-CoreConcepts/) - Fullständig modernisering
- **Protokollversionsuppdatering**: Uppdaterad för att referera nuvarande MCP-specifikation 2025-06-18 med datum-baserad versionering (ÅÅÅÅ-MM-DD format)
- **Arkitekturförfining**: Förbättrade beskrivningar av värdar, klienter och servrar för att spegla aktuella MCP-arkitekturmönster
  - Värdar nu tydligt definierade som AI-applikationer som koordinerar flera MCP-klientanslutningar
  - Klienter beskrivna som protokollkopplingar som upprätthåller en-till-en-serverrelationer
  - Servrar förbättrade med lokala vs fjärrutplaceringsscenarier
- **Primitiv omstrukturering**: Total översyn av server- och klientprimitiver
  - Serverprimitiver: Resurser (datakällor), Prompter (mallar), Verktyg (exekverbara funktioner) med detaljerade förklaringar och exempel
  - Klientprimitiver: Sampling (LLM-svar), Elicitation (användarinmatning), Logging (felsökning/övervakning)
  - Uppdaterade med aktuella upptäckts- (`*/list`), återvinnings- (`*/get`) och exekverings- (`*/call`) metodmönster
- **Protokollarkitektur**: Introducerade tvålagersarkitekturmodell
  - Datalager: JSON-RPC 2.0-bas med livscykelhantering och primitiver
  - Transportlager: STDIO (lokalt) och strömningsbar HTTP med SSE (fjärr) transportmekanismer
- **Säkerhetsramverk**: Omfattande säkerhetsprinciper inklusive uttryckligt användarsamtycke, dataskydd, säker verktygsexekvering och transportsäkerhet
- **Kommunikationsmönster**: Uppdaterade protokollmeddelanden för att visa initiering, upptäckt, exekvering och notifieringsflöden
- **Kodexempel**: Uppdaterade flerspråkiga exempel (.NET, Java, Python, JavaScript) för att spegla aktuella MCP SDK-mönster

#### Säkerhet (02-Security/) - Omfattande säkerhetsgenomgång  
- **Standardanpassning**: Fullständig anpassning till MCP-specifikation 2025-06-18 säkerhetskrav
- **Autentiseringsevolution**: Dokumenterad utveckling från egna OAuth-servrar till delegation till externa identitetsleverantörer (Microsoft Entra ID)
- **AI-specifik hotanalys**: Förbättrad täckning av moderna AI-attackvektorer
  - Detaljerade promptinjektionsattackscenarier med verkliga exempel
  - Verktygsförgiftning och "rug pull"-attackmönster
  - Kontextfönsterförgiftning och modellförvirringsattacker
- **Microsoft AI-säkerhetslösningar**: Omfattande täckning av Microsofts säkerhetsekosystem
  - AI Prompt Shields med avancerad detektion, spotlight och avgränsartekniker
  - Azure Content Safety integrationsmönster
  - GitHub Advanced Security för leverantörskedjeskydd
- **Avancerad hotmitigering**: Detaljerade säkerhetskontroller för
  - Sessionskapning med MCP-specifika attackscenarier och kryptografiska sessions-ID-krav
  - Confused Deputy-problem i MCP-proxy-scenerier med uttryckliga samtyckeskrav
  - Token-passthrough-sårbarheter med obligatoriska valideringskontroller
- **Leverantörskedjesäkerhet**: Utökad AI-leverantörskedjetäckning inklusive grundmodeller, inbäddningstjänster, kontextleverantörer och tredjeparts-API:er
- **Grundsäkerhet**: Förbättrad integration med företagssäkerhetsmönster inklusive zero trust-arkitektur och Microsofts säkerhetsekosystem
- **Resursorganisation**: Kategoriserade omfattande resurslänkar efter typ (Officiella dokument, standarder, forskning, Microsoft-lösningar, implementeringsguider)

### Förbättringar av dokumentationskvalitet
- **Strukturerade lärandemål**: Förbättrade lärandemål med specifika, handlingsbara resultat 
- **Tvärreferenser**: Tillagda länkar mellan relaterade säkerhets- och kärnkonceptämnen
- **Aktuell information**: Uppdaterade alla datumreferenser och specifikationslänkar till gällande standarder
- **Implementeringsvägledning**: Tillagda specifika, handlingsbara implementeringsriktlinjer i båda sektionerna

## 16 juli, 2025

### README och navigeringsförbättringar
- Fullständigt omarbetad kursplannavigering i README.md
- Ersatte `<details>`-taggar med mer tillgängligt tabellformat
- Skapade alternativa layoutalternativ i ny mapp "alternative_layouts"
- Tillagda navigeringsexempel med kortbaserat, flikformat och dragspelsformat
- Uppdaterad sektion för repositorystrukturen för att inkludera alla senaste filer
- Förbättrad sektionen "Hur man använder denna kursplan" med tydliga rekommendationer
- Uppdaterade MCP-specifikationslänkar för att peka på korrekta URL:er
- Tillagd Context Engineering-sektion (5.14) till kursplanstrukturen

### Uppdateringar i studievägledning
- Fullständigt reviderad studievägledning för att stämma överens med aktuell repositorystruktur
- Tillagda nya sektioner för MCP-klienter och verktyg, samt populära MCP-servrar
- Uppdaterad visuell kursplanskarta för att korrekt spegla alla ämnen
- Förbättrade beskrivningar av avancerade ämnen för att täcka alla specialiserade områden
- Uppdaterad avsnitt för fallstudier för att spegla verkliga exempel
- Tillagt denna omfattande ändringslogg

### Gemenskapsbidrag (06-CommunityContributions/)
- Tillagt detaljerad information om MCP-servrar för bildgenerering
- Tillagd omfattande sektion om att använda Claude i VSCode
- Tillagg instruktioner för installation och användning av Cline terminalklient
- Uppdaterad MCP-klientsektion för att inkludera alla populära klientalternativ
- Förbättrade bidragsexempel med mer exakta kodexempel

### Avancerade ämnen (05-AdvancedTopics/)
- Organiserade alla specialämnesmappar med konsekvent namngivning
- Tillagda material och exempel för context engineering
- Tillagd Foundry agentintegrationsdokumentation
- Förbättrad dokumentation för Entra ID-säkerhetsintegration

## 11 juni, 2025

### Första skapandet
- Släppt första versionen av MCP för nybörjare-kursplan
- Skapade grundstruktur för alla 10 huvudsakliga sektioner
- Implementerade visuell kursplanskarta för navigering
- Tillagda initiala exempelprojekt i flera programmeringsspråk

### Komma igång (03-GettingStarted/)
- Skapade första serverimplementeringsexempel
- Tillagda riktlinjer för klientutveckling
- Inkluderade instruktioner för LLM-klientintegration
- Tillagda dokumentation för integration i VS Code
- Implementerade serverexempel med Server-Sent Events (SSE)

### Kärnkoncept (01-CoreConcepts/)
- Tillagda detaljerad beskrivning av klient-server-arkitektur
- Skapade dokumentation för nyckelkomponenter i protokollet
- Dokumenterade meddelandemönster i MCP

## 23 maj, 2025

### Repositorystruktur
- Initierade repository med grundläggande mappstruktur
- Skapade README-filer för varje större sektion
- Satt upp översättningsinfrastruktur
- Tillagda bildresurser och diagram

### Dokumentation
- Skapade initial README.md med kursplansöversikt
- Tillagda CODE_OF_CONDUCT.md och SECURITY.md
- Upprättade SUPPORT.md med vägledning för att få hjälp
- Skapade preliminär struktur för studievägledning

## 15 april, 2025

### Planering och ramverk
- Initial planering för MCP för nybörjare-kursplan
- Definierade lärandemål och målgrupp
- Skisserade kursplanens 10-sektionsstruktur
- Utvecklade konceptuellt ramverk för exempel och fallstudier
- Skapade initiala prototyp-exempel för nyckelkoncept

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Ändringslogg: MCP för nybörjare läroplan

Detta dokument tjänar som en registrering av alla betydande förändringar som gjorts i Model Context Protocol (MCP) för nybörjare läroplanen. Förändringar dokumenteras i omvänd kronologisk ordning (senaste förändringar först).

## 9 september 2026

### MCP 2026-07-28 slutgiltig specifikationsanpassning

Uppdaterade den engelska läroplanen från release-kandidat och `2025-11-25`
baslinjevägledning till den slutgiltiga MCP `2026-07-28` specifikationen.

- **Uppdaterat**: Referenser till aktuell version, specifikationslänkar, stateless
  förfrågningsvägledning, `server/discover`, Streamable HTTP headers och Tasks
  extension-livscykeln över 38 engelska dokumentationsfiler.
- **Korrigerat**: Elicitation använder nu `elicitation/create`, Sampling använder
  `sampling/createMessage`, och `InputRequiredResult.resultType` använder
  `"input_required"`.
- **Ersatt**: Den felaktiga lektionen om Root Context konversationsstatus med en
  protokollkorrekt Roots-lektion som täcker informativa filsystemstips, den
  aktuella multi-omgångsflödet, säkerhetsgränser och migreringsalternativ.
- **Klargjort**: Roots, Sampling, Logging och Dynamic Client Registration är
  föråldrade i `2026-07-28`, med deras rekommenderade ersättningar och tidigaste
  borttagningsdatum dokumenterade.
- **Märkt**: Exempel som fortfarande är beroende av MCP `2025-11-25`, HTTP+SSE,
  initialiseringshandshakes eller protokollsessions bevaras som legacy
  kompatibilitexempel snarare än att presenteras som aktuella implementeringar.
- **Säkerhetsvägledning**: Uppdaterade de fristående säkerhetsguiderna att använda
  per-förfrågan auktorisering och explicita applikationstillståndshandtag istället för
  borttagna protokollsessions-ID. Client ID Metadata Documents är nu den
  föredragna registreringsvägen, med DCR dokumenterat som kompatibilitet-endast.
- **Stödmaterial**: Uppdaterade studieguide, bidragschecklista,
  Publora fallstudie och APIM fallstudie. APIM-genomgången rekommenderar nu
  sin aktuella Streamable HTTP `/mcp` endpoint istället för den föråldrade `/sse`.
- **Kanoniska länkar**: Ersatte pensionerade och utkast till specifikations-URL:er i
  engelska käll-Markdown med versionerade `2026-07-28` länkar, samtidigt som explicita
  länkar till legacy-versioner bevaras där ett exempel fortfarande är låst till äldre verktyg.
- **Stabila filnamn**: Bytte namn på slutgiltig specifikationsguide och två säkerhets-
  guider för att ta bort release-kandidat och årsuffix, och uppdaterade sedan alla
  engelska hyperlänkar till deras stabila sökvägar.
- **Nytt auktoriseringsexempel**: Lade till en testad
  [TypeScript MCP `2026-07-28` resursserver](./02-Security/samples/cimd-dcr-auth/README.md)
  som jämför föredragna Client ID Metadata Documents med föråldrad Dynamic
  Client Registration fallback. Exemplet inkluderar RFC 9728 discovery, JWKS
  validering, verktygsspecifika scopes, tolv tester och en Auth0 installationsgenomgång.
- **Översättningsomfång**: Endast engelska källfiler redigerades; genererade
  översättningar och översatta bilder förblir oförändrade eftersom de är automatöversatta.

## 29 juli 2026

### Ny modul 08-kompanjon: Pålitlighetssidecars och säkra omförsök

Lade till en leverantörsneutral kompanjonlektion för MCP-verktyg som skapar verkliga
effekter, anpassad till den slutgiltiga `2026-07-28` specifikationen.

- **Ny**: [letionen om pålitlighetssidecar](../../reliability-sidecar)
  använder en supportärende-historia, två Mermaid-diagram och ett beslutflöde för omförsök
  för att förklara stabila operation-nycklar, atomisk dupliceringstillträde,
  försoning, bevis och Tasks extension-gräns.
- **Ny**: En standardbiblioteks Python- och SQLite-felförinjektionsövning
  använder separata operation- och ärendelager för att demonstrera ett svar som går förlorat
  efter att en extern effekt har genomförts. Sex deterministiska tester täcker naiv
  duplicering, skyddad återstartsåterhämtning, payload-konflikter, cachade resultat,
  aktiva anspråk och samtidigt dupliceringstillträde.
- **Uppdaterad**: Modul 08 länkar nu kompanjonlektionen, identifierar
  slutgiltiga `2026-07-28` stateless förfrågningsmodellen, skiljer OpenTelemetry
  observabilitet från den föråldrade MCP loggningsfunktionen och begränsar sitt
  generiska omförsöksexempel till skrivskyddade operationer.
- **Valfri**: Lektionen kartlägger sina portabla koncept till en märkt community-
  implementation utan att göra den hostade tjänsten eller en nätverksanrop del av
  övningen.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juli 2026

### Ny lektion: 2026-07-28 MCP specifikations release-kandidat

Lade till täckning av den kommande `2026-07-28` MCP specifikations release-kandidat (meddelad 21 maj 2026; slutgiltig release planerad till 28 juli 2026), sammanfattad från [det officiella tillkännagivandet](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Läroplanens baslinje förblir **MCP Specification 2025-11-25** tills den nya versionen levereras, så detta presenteras som framåtblickande vägledning snarare än en omskrivning av befintliga lektioner.

- **Ny**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — en fullständig lektion som täcker stateless protokollkärnan (borttagning av `initialize` handshake och `Mcp-Session-Id`), de nya `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` cachemetadata, W3C Trace Context i `_meta`, det formella Extensions-ramverket (MCP-appar och den nya Tasks-extensionen), sex auktoriseringshärdande SEPs, avvecklingen av Roots/Sampling/Logging och övergången till full JSON Schema 2020-12 för verktygsscheman.
- **Uppdaterad** med framåtblickande hänvisningar till den nya lektionen:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokollversionsnot, sampling/roots/logging/tasks avsnitt och "Vad händer härnäst"
  - [02-Security/README.md](./02-Security/README.md): auktoriseringshärdande hänvisning
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport hänvisning
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling avvecklingshänvisning
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging avveckling och Tasks extension hänvisning
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing hänvisning
  - [README.md](./README.md): "Ser framåt" notis i specifikationsdelen och en ny `1.1` post i läroplanens modultabell
  - [study_guide.md](./study_guide.md): framåtblickande punkt under Core Concepts översikten och en daterad tilläggsnotis
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): hänvisning till `mcp-session-id` transportkarta inför stateless förfrågningsmodell
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): modulöversikt med hänvisning till Root Contexts/Sampling avveckling och Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): auktoriseringshärdande hänvisning

## 24 juni 2026

### Ny lektion: Använda MCP i Copilot-app

- [Verktygsavsnitt](./12-tooling/README.md) Lade till verktygsavsnitt.
- [MCP i Copilot-app](./12-tooling/01-copilot-app/README.md)

## 16 juni 2026

### MCP specifikationsanpassning & exempelvalidering

Validerade läroplanen mot den aktuella **MCP Specification 2025-11-25** och de senaste officiella SDK:erna, korrigerade sedan återstående föråldrade specifikationsreferenser och bekräftade att kärnexemplen fortfarande kan byggas och köras.

#### Specifikationsversionskorrigeringar (2025-06-18 / 2025-03-26 → 2025-11-25)

Uppdaterade engelskt innehåll där det fortfarande påstods att en äldre specifikationsrevision var den *aktuella/senaste* standarden, och pekade om länkar till kanoniska `modelcontextprotocol.io` spec-sökvägar:
- **05-AdvancedTopics/mcp-security/README.md**: Uppdaterade "Current Standard"-banderoll, introduktion, kärnsäkerhetsprinciper rubrik, obligatoriska krav rubrik, Microsoft Entra ID-avsnitt, Referenser & Resurslänkar och avslutande säkerhetsnotis (8 referenser) till 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Uppdaterade länken för Ytterligare resurser och "Current Standard"-banderoll till 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Ersatte frånvarande `2025-03-26` säkerhets- och förtroendelänken med den aktuella 2025-11-25 sidan för säkerhetsbästa praxis
- **03-GettingStarted/14-sampling/README.md**: Uppdaterade officiella sampling-dokumentationslänken till 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Uppdaterade presensreferens till "nuvarande MCP-specifikation" och Ytterligare resurser-länk till 2025-11-25 (historiska SSE-avvecklingsnoteringar lämnades kvar för korrekthet)

#### Exempelvalidering mot aktuella SDK:er

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` löste `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` passerade utan typfel — befintliga `McpServer`/`StdioServerTransport` API:er förblir giltiga
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validerad i isolerad `.venv` med `mcp[cli]` (1.27.2); `py_compile` passerade och `FastMCP.list_tools()` returnerade korrekt `add` och `subtract` verktyg
- Bekräftade att alla exempel `@modelcontextprotocol/sdk` versionsspann (`>=1.26.0` / `^1.26.0` / `^1.27.0`) löser rent till nuvarande `1.29.0` utan brytande API-ändringar

#### Beroendestiftelsejustering (stänga versionsgap)

Uppgraderade föråldrade SDK-stiftelser så att varje exempel följer den aktuella MCP-releasen, i enlighet med repo-omfattande konvention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Uppgraderade `@modelcontextprotocol/sdk` från `^1.8.0` → `>=1.26.0` och uppdaterade den föråldrade `"updated for MCP 2025-06-18"` paketbeskrivningen till `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** och **lab4/code/github_mcp_server/pyproject.toml**: Uppgraderade exakt stake `mcp==1.23.0` → `mcp>=1.26.0`; återskapade båda `uv.lock` filerna (`uv lock`) så att lockfilerna löser till aktuella `mcp 1.27.2` och hålls synkroniserade med manifesten

#### Läroplansgapanalys — Senaste specifikationsfunktionsäckning

Verifierade att läroplanen redan täcker alla primitives som introducerats/utökats i MCP 2025-11-25, så inga innehållsgap återstår:
- **Sampling**: Lektion 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (inkl. URL-läge)**: Dokumenterad i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Dokumenterad i 00-Introduction, 01-CoreConcepts och 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimentella, långvariga operationer)**: Dokumenterad i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features
- **Verktygsannoteringar** (`readOnlyHint` / `destructiveHint`): Dokumenterad i 01-CoreConcepts och 05-AdvancedTopics/mcp-protocol-features

### Säkerhetshärdning & Beroendesårbarhetsåtgärder

Genomförde en full säkerhetsgranskning av alla beroendemanifest och källkoden för exemplen, och åtgärdade alla rapporterade npm-varningar samt en kodnivåfynd. Efter åtgärder rapporterar `npm audit` **0 sårbarheter** i varje granskad mapp.

#### npm beroendesårbarheter (transitiva) — Åtgärdade

Granskade alla 15 incheckade `package-lock.json` filer. Sårbarheter begränsades till transitiva beroenden dragna av MCP Inspector utvecklingsverktyget, OpenAI klienten och MCP SDK; alla är nu lösta utan att bryta exemplen:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** och **lab3/code/weather_mcp/inspector**: Uppgraderade `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), vilket löste de bundlade säkerhetsvarningarna för `ajv`, `brace-expansion`, `diff`, `path-to-regexp` och `ws`. Lade till en npm `overrides` post som tvingar fram den patchade `shell-quote@1.8.4` för att eliminera den kvarvarande kritiska varningen från `concurrently`; genererade om båda lockfilerna (nu 0 sårbarheter)
- **03-GettingStarted/samples/typescript**: `npm audit fix` uppdaterade den transitiva `qs` (medel) till en patchad version
- **03-GettingStarted/samples/javascript**: `npm audit fix` uppdaterade den transitiva `hono` (medel) till en patchad version
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` uppdaterade den transitiva `form-data` (hög) till en patchad version
- **03-GettingStarted/11-simple-auth/solution/typescript**: Genererade den saknade `package-lock.json` så att projektet är reproducerbart och granskbart (0 sårbarheter)

#### Säkerhetsfix på kodnivå (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Tog bort `shell=True` från verktyget `open_in_vscode`. Det tidigare `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` tillät shell-metakaraktärer i en mappsökväg att tolkas av `cmd.exe` (kommandoinjektionsvektor). Det startar nu den lösta `Code.exe` direkt med mappen som argument — utan shell — vilket är funktionellt ekvivalent och säkert

#### Revision av Python-beroenden

- Granskade varje Python requirements-set med `pip-audit`. `05-AdvancedTopics` och `03-GettingStarted/samples/python` rapporterade **inga kända sårbarheter** (deras `mcp` / `httpx` / `pydantic` / `python-dotenv` versioner pekar på aktuella patchade releaser)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flaggade det transitiva beroendet **`werkzeug` 3.1.1** med tre `safe_join` Windows device-name DoS-varningar — `CVE-2025-66221`, `CVE-2026-21860`, och `CVE-2026-27199` (alla fixade i 3.1.6). Lade till en explicit säkerhetsspärr `werkzeug>=3.1.6` så att den patchade releasen löses; verifierade att restriktionen löses korrekt med `chainlit` / `mcp` / `semantic-kernel` stacken

### Produktnamnsomprofilering

Uppdaterade allt kursinnehåll för att återspegla Microsofts produktomprofilering:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Uppdaterade Discord-communitylänk
- **AGENTS.md**: Uppdaterade Discord-serverreferens
- **README.md**: Uppdaterade referenser till teknikens ekosystem
- **study_guide.md**: Uppdaterade fallstudie-referenser
- **05-AdvancedTopics/README.md**: Uppdaterade titel och beskrivning för modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Uppdaterade avsnittsrubrik och beskrivning
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Full uppdatering av modultitel och innehåll
- **05-AdvancedTopics/mcp-security-entra/README.md**: Uppdaterade korsreferenslänk
- **07-LessonsfromEarlyAdoption/README.md**: Uppdaterade fallstudie-referenser
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Uppdaterade rubrik för avsnitt 9, märken och kapabiliteter
- **08-BestPractices/README.md**: Uppdaterade Discord-communitylänk
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Uppdaterade Discord-kanalreferens
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Uppdaterade referens till modellutplacering
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Uppdaterade AI Services-tabell
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Uppdaterade resurserreferenser

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Uppdaterade huvudsakliga kursreferenser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Uppdaterade modultitel, översikt och alla modulers rubriker
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Uppdaterade titel, lärandemål, installationsinstruktioner och resurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Uppdaterade titel, lärandemål, MCP-hosts tabell och korsreferenser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Uppdaterade titel, märken, förkunskaper och resurser
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Uppdaterade Agent Builder-referenser och feedbacklänk
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Uppdaterade förkunskaper och tilläggsreferenser

---

## 11 april, 2026

### Ny lektion, dokumentationsfixar och beroendeuppdateringar

#### Nytt kursinnehåll tillagt

**Modul 05 - Avancerade ämnen**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattande guide som täcker debattmönstret för multi-agent-system
  - Mermaid arkitekturdiagram: två agenter → delad MCP-server → debatttranskript → domare → domslut
  - Delad MCP verktygsserver (`web_search` + `run_python`) implementerad i Python och TypeScript
  - Motsatta system-promptar (FÖR / MOT / Domare) med explicita krav på verktygsanvändning
  - Debattorganisatör i Python, TypeScript och C# som hanterar rundor och dirigerar argument
  - MCP `ClientSession` kopplat till organisatören för verkliga verktygsanrop
  - Användarfallstabell (hallucinationsdetektion, hotmodellering, API-designgranskning, faktakontroll, tekniskt urval)
  - Säkerhetsöverväganden: sandboxad körning, validering av verktygsanrop, rate limiting, revisionsloggning
  - Strukturerad övning med tre praktiska scenarier (kodgranskning, arkitekturval, innehållsmoderering)

#### Dokumentationsfixar

**Modul 03 - Komma igång**
- **05-stdio-server/README.md**: Fixade ofullständigt TypeScript stdio-serverexempel — la till saknad transport-instandiering (`new StdioServerTransport()`) och anropet `server.connect(transport)` för att matcha Python och .NET-exemplen i samma avsnitt
- **14-sampling/README.md**: Fixade stavfel — rättade `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kursuppdateringar

**Huvud README.md**
- Lade till posten 5.17 (Adversarial Multi-Agent Reasoning med MCP) i kursöversiktstabellen med direktlänk till den nya lektionen

**05-AdvancedTopics/README.md**
- Lade till rad för Lektion 5.17 i lektionstabellen

**study_guide.md**
- Lade till ämnet Adversarial Multi-Agent Reasoning i tankekartan och textbeskrivningen av Avancerade Ämnen

#### Kod- och säkerhetsfixar

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Säkerhetsfix — kommandoinjektion**: Ersatte `execSync` shell-interpolering med `execFile` + `promisify` i TypeScript-verktyget `run_python`, vilket eliminerade kommandoinjektionsytan (LLM-styrd kod skickas nu som ett bokstavligt argv-element utan shell-inblandning)
- **MCP verktygsloppskoppling**: Uppdaterade Python-debattorganisatör att använda `AsyncAnthropic` klient (ersätter blockerande synkrona `Anthropic`), skicka en live `ClientSession` direkt till varje agents tur, hämta verktygsdefinitioner via `session.list_tools()` varje tur, och skicka `tool_use` block via `session.call_tool()` i en loop tills modellen sänder ett slutgiltigt textsvar

#### Beroendeuppdateringar

- Uppgraderade `hono` till 4.12.12 i flera paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uppgraderade `@hono/node-server` från 1.19.11 till 1.19.13 i TypeScript-paketen
- Uppgraderade `cryptography` från 46.0.5 till 46.0.7 i Python-paketen (10-StreamliningAIWorkflows labbar 3 och 4)
- Uppgraderade `lodash` från 4.17.23 till 4.18.1 i 10-StreamliningAIWorkflows inspektören

#### Översättningar

- Synkroniserade översättningar för 48+ språk med senaste källändringarna (i18n-uppdatering)

---

## 5 februari, 2026

### Validerings- och navigationsförbättringar för hela arkivet

#### Nytt kursinnehåll tillagt

**Modul 03 - Komma igång**
- **12-mcp-hosts/README.md**: Ny omfattande guide för att sätta upp MCP-hostar
  - Konfigurationsexempel för Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-konfigurationstillägg för alla större hosts
  - Jämförelsetabell för transporttyper (stdio, SSE/HTTP, WebSocket)
  - Felsökning av vanliga anslutningsproblem
  - Säkerhetsbästa praxis för hostkonfiguration

- **13-mcp-inspector/README.md**: Ny felsökningsguide för MCP Inspector
  - Installationsmetoder (npx, globalt npm, från källkod)
  - Anslutning till servrar via stdio och HTTP/SSE
  - Testverktyg, resurser och prompt-arbetsflöden
  - VS Code-integration med MCP Inspector
  - Vanliga felsökningsscenarier med lösningar

**Modul 04 - Praktisk implementering**
- **pagination/README.md**: Ny guide för pagineringsimplementering
  - Cursor-baserade pagineringsmönster i Python, TypeScript, Java
  - Klientsideshantering av paginering
  - Designstrategier för cursor (opak vs. strukturerad)
  - Prestandaoptimeringsrekommendationer

**Modul 05 - Avancerade ämnen**
- **mcp-protocol-features/README.md**: Ny djupdykning i protokollfunktioner
  - Implementering av framförandenotiser
  - Mönster för avbokningsförfrågningar
  - Resursmallar med URI-mönster
  - Hantering av serverns livscykel
  - Kontroll av loggnivåer
  - Felhanteringsmönster med JSON-RPC-koder

#### Navigationsfixar (24+ filer uppdaterade)

**Huvudmodulers README-filer**
 Nu länkar både till första lektionen OCH nästa modul

**02-Säkerhetsunderfiler**
- Alla 5 kompletterande säkerhetsdokument har nu "Vad händer härnäst?" navigering:

**09-CaseStudy Filer**
- Alla fallstudiefiler har nu sekventiell navigering:

**10-StreamliningAI Labs**
Lade till avsnittet Vad händer härnäst i Modul 10-översikten och Modul 11

#### Kod- och innehållsfixar

**SDK- och beroendeuppdateringar**
Fixade tom version av openai till `^4.95.0`
Uppdaterade SDK från `^1.8.0` till `>=1.26.0`
Uppdaterade MCP versionsspärrar till `>=1.26.0`

**Kodfixar**
Fixade ogiltig modell `gpt-4o-mini` till `gpt-4.1-mini`

**Innehållsfixar**
Fixade brutet länk `READMEmd` → `README.md`, korrigerade kursrubrik `Modul 1-3` → `Modul 0-3`, fixade skiftlägeskänslig sökväg
Tog bort korrupt duplicerat Case Study 5-innehåll

**Förbättringar i nybörjarguide**
Lade till ordentlig introduktion, lärandemål och förkunskaper för nybörjare

#### Kursuppdateringar

**Huvud README.md**
- Lade till posterna 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protokollfunktioner) till kursöversiktstabellen

**Modul-README-filer**
Lade till lektionerna 12 och 13 i lektionslistan
Lade till avsnittet Praktiska guider med pagineringslänk
Lade till lektionerna 5.15 (Custom Transport) och 5.16 (Protocol Features)

**study_guide.md**
- Uppdaterade tankekartan med alla nya ämnen: MCP Hosts Setup, MCP Inspector, Pagineringstrategier, Djupdykning i protokollfunktioner

## 28 januari, 2026

### Översyn av MCP-specifikationens efterlevnad 2025-11-25

#### Förbättring av kärnkoncept (01-CoreConcepts/)
- **Ny klientprimitive - Roots**: Lade till omfattande dokumentation om Roots-klientprimitiven som gör servrar medvetna om filsystemgränser och åtkomsträttigheter
- **Verktygsannoteringar**: Lade till dokumentation om verktygets beteendeannoteringar (`readOnlyHint`, `destructiveHint`) för bättre beslut vid verktygskörning
- **Verktygsanrop i sampling**: Uppdaterade samplingdokumentationen för att inkludera `tools` och `toolChoice` parametrar för modellstyrda verktygsanrop under samplingförfrågningar
- **URL Mode Elicitation**: Lade till dokumentation om URL-baserad elicitering för serverinitierade externa webinteraktioner
- **Uppgifter (experimentella)**: Lade till nytt avsnitt som dokumenterar den experimentella funktionen Uppgifter för hållbara exekveringsomslag och uppskjuten resultathämtning

- **Ikonstöd**: Noterade att verktyg, resurser, resursscheman och uppmaningar nu kan inkludera ikoner som ytterligare metadata

#### Uppdateringar i dokumentationen
- **README.md**: Lade till MCP-specifikation 2025-11-25 versionsreferens och förklaring av versionshantering baserad på datum
- **study_guide.md**: Uppdaterade läroplanskarta för att inkludera Uppgifter och Verktygsanteckningar i avsnittet Kärnkoncept; uppdaterade dokumentets tidsstämpel

#### Verifiering av specifikationsöverensstämmelse
- **Protokollversion**: Verifierade att all dokumentation refererar till nuvarande MCP-specifikation 2025-11-25
- **Arkitekturanpassning**: Bekräftade tvåskiktsarkitekturens (Data Layer + Transport Layer) dokumentationsnoggrannhet
- **Dokumentation av primitiva komponenter**: Validerade serverprimitiver (Resurser, Uppmaningar, Verktyg) och klientprimitiver (Sampling, Elicitation, Loggning, Roots)
- **Transportmekanismer**: Verifierade dokumentationsnoggrannhet för STDIO och Streamable HTTP-transport
- **Säkerhetsvägledning**: Bekräftade överensstämmelse med aktuella MCP Security Best Practices-dokument

#### Viktiga MCP 2025-11-25 Funktioner Dokumenterade
- **OpenID Connect Discovery**: Auth-serverupptäckt genom OIDC
- **OAuth Client ID Metadata Dokument**: Rekommenderad klientregistreringsmekanism
- **JSON Schema 2020-12**: Standarddialekt för MCP-schema-definitioner
- **SDK-Tieringssystem**: Formaliserade krav för SDK-funktionsstöd och underhåll
- **Styrningsstruktur**: Formaliserade Arbetsgrupper och Intressegrupper i MCP-styrning

### Större uppdatering av säkerhetsdokumentation (02-Security/)

#### Integration med MCP Security Summit Workshop (Sherpa)
- **Ny praktisk utbildningsresurs**: Lade till omfattande integration med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all säkerhetsdokumentation
- **Expeditionsrutt-täckning**: Dokumenterade hela progressionen från Basläger till Toppmöte
- **OWASP-anpassning**: All säkerhetsvägledning mappar nu till OWASP MCP Azure Security Guide-risker

#### Integration av OWASP MCP Top 10
- **Nytt avsnitt**: Lade till tabell för OWASP MCP Top 10 säkerhetsrisker med Azure-mitigeringar i huvud-Security README
- **Riskbaserad dokumentation**: Uppdaterade mcp-security-controls-2025.md med OWASP MCP-riskreferenser för varje säkerhetsdomän
- **Referensarkitektur**: Länkade till OWASP MCP Azure Security Guide referensarkitektur och implementeringsmönster

#### Uppdaterade säkerhetsfiler
- **README.md**: Lade till Sherpa Workshop-översikt, expeditionsrutt-tabell, sammanfattning av OWASP MCP Top 10 risker och sektion för praktisk utbildning
- **mcp-security-controls-2025.md**: Uppdaterade header till februari 2026, lade till OWASP-riskreferenser (MCP01-MCP08), rättade versionsinkonsistens
- **mcp-security-best-practices-2025.md**: Lade till Sherpa och OWASP-resurssektion, uppdaterade tidsstämpel
- **mcp-best-practices.md**: Lade till sektion för praktisk utbildning med Sherpa och OWASP-länkar
- **azure-content-safety-implementation.md**: Lade till OWASP MCP06-referens, Sherpa Camp 3-anpassning och ytterligare resurssektion

#### Nya resurslänkar tillagda
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuella OWASP MCP-risk-sidor (MCP01-MCP10)

### Läroplansomfattande MCP-specifikation 2025-11-25 anpassning

#### Modul 03 - Kom igång
- **SDK-dokumentation**: Lade till Go SDK i officiell SDK-lista; uppdaterade alla SDK-referenser för att följa MCP-specifikation 2025-11-25
- **Transportförtydligande**: Uppdaterade STDIO och HTTP Streaming transportbeskrivningar med explicita spec-referenser

#### Modul 04 - Praktisk implementering
- **SDK-uppdateringar**: Lade till Go SDK; uppdaterade SDK-lista med specifikationsversionsreferens
- **Authorization Spec**: Uppdaterade MCP Authorization-specifikationslänk till aktuell 2025-11-25 version

#### Modul 05 - Avancerade ämnen
- **Nya funktioner**: Lade till notering om nya MCP-specifikation 2025-11-25 funktioner (Uppgifter, Verktygsanteckningar, URL Mode Elicitation, Roots)
- **Säkerhetsresurser**: Lade till OWASP MCP Top 10 och Sherpa workshop-länkar till ytterligare referenser

#### Modul 06 - Communitybidrag
- **SDK-lista**: Lade till Swift och Rust SDKs; uppdaterade specifikationslänk till 2025-11-25
- **Spec-referens**: Uppdaterade MCP-specifikationslänk till direkt specifikations-URL

#### Modul 07 - Lärdomar från tidig adoption
- **Resursuppdateringar**: Lade till MCP-specifikation 2025-11-25-länk och OWASP MCP Top 10 till ytterligare resurser

#### Modul 08 - Bästa praxis
- **Specifikationsversion**: Uppdaterade MCP-specifikationsreferens till 2025-11-25
- **Säkerhetsresurser**: Lade till OWASP MCP Top 10 och Sherpa workshop i ytterligare referenser

#### Modul 10 - Effektivisering av AI-arbetsflöden
- **Badge-uppdatering**: Ändrade MCP versionsbadge från SDK-version (1.9.3) till specifikationsversion (2025-11-25)
- **Resurslänkar**: Uppdaterade MCP-specifikationslänk; lade till OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Labs
- **Spec-referens**: Uppdaterade MCP-specifikationslänk till 2025-11-25 version
- **Säkerhetsresurser**: Lade till OWASP MCP Top 10 till officiella resurser

## 18 december 2025

### Uppdatering av säkerhetsdokumentation - MCP-specifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Versionsuppdatering
- **Protokollversionsuppdatering**: Uppdaterade för att referera senaste MCP-specifikation 2025-11-25 (släppt 25 november 2025)
  - Uppdaterade alla referenser till specifikationsversion från 2025-06-18 till 2025-11-25
  - Uppdaterade dokumentdatumreferenser från 18 augusti 2025 till 18 december 2025
  - Verifierade att alla specifikations-URL:er pekar till aktuell dokumentation
- **Innehållsvalidering**: Omfattande validering av säkerhetsbästa praxis mot senaste standarder
  - **Microsoft Security Solutions**: Verifierade aktuell terminologi och länkar för Prompt Shields (tidigare ”Jailbreak risk detection”), Azure Content Safety, Microsoft Entra ID och Azure Key Vault
  - **OAuth 2.1 Security**: Bekräftade överensstämmelse med senaste OAuth-säkerhetsbästa praxis
  - **OWASP-standarder**: Validerade att OWASP Top 10 för LLMs-referenser är aktuella
  - **Azure-tjänster**: Verifierade alla Microsoft Azure-dokumentationslänkar och bästa praxis
- **Standardanpassning**: Alla refererade säkerhetsstandarder bekräftade aktuella
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure säkerhets- och regelefterlevnadsramverk
- **Implementeringsresurser**: Validerade alla implementeringsguide-länkar och resurser
  - Azure API Management autentiseringsmönster
  - Microsoft Entra ID integrationsguider
  - Azure Key Vault hemlighetshantering
  - DevSecOps pipelines och övervakningslösningar

### Dokumentationskvalitetssäkring
- **Specifikationsöverensstämmelse**: Säkerställde att alla obligatoriska MCP-säkerhetskrav (MÅSTE/FÅR INTE) överensstämmer med senaste specifikation
- **Resursvaluta**: Verifierade alla externa länkar till Microsoft-dokumentation, säkerhetsstandarder och implementeringsguider
- **Täckning av bästa praxis**: Bekräftade omfattande täckning av autentisering, auktorisation, AI-specifika hot, leveranskedjesäkerhet och företagsmönster

## 6 oktober 2025

### Utökning av Kom igång-avsnittet – Avancerad serveranvändning & Enkel autentisering

#### Avancerad serveranvändning (03-GettingStarted/10-advanced)
- **Nytt kapitel tillagt**: Introducerade en omfattande guide till avancerad MCP-serveranvändning, inklusive både vanliga och låg-nivå serverarkitekturer.
  - **Vanlig vs. Låg-nivå server**: Detaljerad jämförelse och kodexempel i Python och TypeScript för båda tillvägagångssätten.
  - **Handler-baserad design**: Förklaring av handler-baserad hantering av verktyg/resurser/uppmaningar för skalbara och flexibla serverimplementationer.
  - **Praktiska mönster**: Verkliga scenarier där låg-nivå servermönster är fördelaktiga för avancerade funktioner och arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapitel tillagt**: Steg-för-steg-guide för att implementera enkel autentisering i MCP-servrar.
  - **Auth-koncept**: Tydlig förklaring av autentisering vs. auktorisation och hantering av autentiseringsuppgifter.
  - **Grundläggande auth-implementering**: Middleware-baserade autentiseringsmönster i Python (Starlette) och TypeScript (Express) med kodexempel.
  - **Progression till avancerad säkerhet**: Vägledning för att börja med enkel auth och gå vidare till OAuth 2.1 och RBAC, med hänvisningar till avancerade säkerhetsmoduler.

Dessa tillägg ger praktisk, handgriplig vägledning för att bygga mer robusta, säkra och flexibla MCP-serverimplementationer, som knyter samman grundläggande koncept med avancerade produktionsmönster.

## 29 september 2025

### MCP Server Databasintegrationslaborationer - Omfattande praktisk inlärningsväg

#### 11-MCPServerHandsOnLabs - Ny komplett kursplan för databasintegration
- **Fullständig 13-laborations inlärningsväg**: Lade till en omfattande praktisk kursplan för att bygga produktionsklara MCP-servrar med PostgreSQL-databasintegration
  - **Verklig implementering**: Zava Retail-analysfall som demonstrerar företagsklassiga mönster
  - **Strukturerad inlärningsprogression**:
    - **Labbar 00-03: Grunder** - Introduktion, Kärnarkitektur, Säkerhet & Multi-Tenancy, Miljöuppsättning
    - **Labbar 04-06: Bygga MCP-servern** - Databasdesign & schema, MCP-serverimplementering, Verktygsutveckling  
    - **Labbar 07-09: Avancerade funktioner** - Semantisk sökintegration, Testning & felsökning, VS Code-integrering
    - **Labbar 10-12: Produktion & bästa praxis** - Distributionsstrategier, Övervakning & observabilitet, Bästa praxis & optimering
  - **Företagsteknologier**: FastMCP-ramverket, PostgreSQL med pgvector, Azure OpenAI-embeddingar, Azure Container Apps, Application Insights
  - **Avancerade funktioner**: Row Level Security (RLS), semantisk sökning, multi-tenant dataåtkomst, vektor-embeddingar, realtidsövervakning

#### Terminologistandardisering - Modul-till-Lab-omvandling
- **Omfattande dokumentationsuppdatering**: Systematiskt uppdaterat alla README-filer i 11-MCPServerHandsOnLabs för att använda "Lab"-terminologi istället för "Modul"
  - **Avsnittsrubriker**: Uppdaterade "Vad denna modul täcker" till "Vad denna labb täcker" i alla 13 labbar
  - **Innehållsbeskrivning**: Ändrat "Den här modulen tillhandahåller..." till "Den här labben tillhandahåller..." i hela dokumentationen
  - **Lärandemål**: Uppdaterade "I slutet av denna modul..." till "I slutet av denna labb..." 
  - **Navigeringslänkar**: Konverterade alla "Modul XX:"-referenser till "Labb XX:" i korsreferenser och navigation
  - **Slutfört spårning**: Uppdaterade "Efter att ha slutfört denna modul..." till "Efter att ha slutfört denna labb..."
  - **Bibehöll tekniska referenser**: Behöll Python-modulreferenser i konfigurationsfiler (t.ex. `"module": "mcp_server.main"`)

#### Förbättring av studieguiden (study_guide.md)
- **Visuell läroplanskarta**: Lade till nytt avsnitt "11. Databasintegrationslabbar" med omfattande visualisering av labbstrukturen
- **Repositorystruktur**: Uppdaterat från tio till elva huvudavsnitt med detaljerad beskrivning av 11-MCPServerHandsOnLabs
- **Navigeringsvägledning**: Förbättrade navigeringsinstruktioner för att täcka sektioner 00-11
- **Täckning av teknik**: Lade till FastMCP, PostgreSQL, Azure-tjänster integrationsdetaljer
- **Inlärningsresultat**: Betoning på produktionsklar serverutveckling, databasintegrationsmönster och företagsäkerhet

#### Förbättring av huvud-README-struktur
- **Labb-baserad terminologi**: Uppdaterade huvud-README.md i 11-MCPServerHandsOnLabs för konsekvent användning av "Labb"-struktur
- **Organisering av inlärningsväg**: Tydlig progression från grundläggande koncept till avancerad implementering och produktionsdistribuering
- **Verklighetsinriktning**: Betoning på praktiskt, handgripligt lärande med företagsklassiga mönster och teknologier

### Förbättringar av dokumentationskvalitet & konsekvens
- **Praktisk inlärning i fokus**: Förstärkt praktisk, labb-baserad metod i hela dokumentationen
- **Fokus på företagsmönster**: Framhävde produktionsklara implementationer och företagsäkerhetsaspekter
- **Teknikintegration**: Omfattande täckning av moderna Azure-tjänster och AI-integrationsmönster
- **Inlärningsprogression**: Tydlig, strukturerad väg från grundläggande koncept till produktionsdistribuering

## 26 september 2025

### Förbättring av fallstudier - GitHub MCP Registry-integration

#### Fallstudier (09-CaseStudy/) - Fokus på ekosystemutveckling
- **README.md**: Större utvidgning med omfattande fallstudie av GitHub MCP Registry
  - **GitHub MCP Registry fallstudie**: Ny omfattande fallstudie om GitHubs lansering av MCP Registry i september 2025
    - **Problemanalys**: Detaljerad granskning av fragmenterade MCP-serverupptäckts- och distributionsutmaningar
    - **Lösningsarkitektur**: GitHubs centraliserade registreringsmetod med en-klicks VS Code-installation
    - **Affärspåverkan**: Mätbara förbättringar i utvecklarintroduktion och produktivitet
    - **Strategiskt värde**: Fokus på modulär agentdistribution och tvärverktygsinteroperabilitet
    - **Ekosystemutveckling**: Positionering som grundplattform för agent-integration
  - **Förbättrad fallstudiestruktur**: Uppdaterade alla sju fallstudier med konsekvent formatering och omfattande beskrivningar
    - Azure AI Travel Agents: Fokus på orkestrering av flera agenter
    - Azure DevOps-integrering: Fokus på arbetsflödesautomation
    - Realtidsdokumentationstillgång: Python-konsolklientimplementering
    - Interaktiv studieplansgenerator: Chainlit konversationswebbapp

    - Dokumentation i redigeraren: VS Code och GitHub Copilot integration
    - Azure API Management: Företags-API integrationsmönster
    - GitHub MCP Registry: Ekosystemutveckling och communityplattform
  - **Omfattande slutsats**: Omskriven slutsatssektion som lyfter fram sju fallstudier som spänner över flera MCP-implementeringsdimensioner
    - Företagsintegration, Multi-Agent Orkestrering, Utvecklarproduktivitet
    - Ekosystemutveckling, kategorisering av utbildningsapplikationer
    - Förbättrade insikter i arkitekturmönster, implementeringsstrategier och bästa praxis
    - Betoning på MCP som ett moget, produktionsklart protokoll

#### Uppdateringar av studieguiden (study_guide.md)
- **Visuell läroplansöversikt**: Uppdaterad tankekarta för att inkludera GitHub MCP Registry i avsnittet om fallstudier
- **Beskrivning av fallstudier**: Förbättrad från generiska beskrivningar till detaljerad uppdelning av sju omfattande fallstudier
- **Repostruktur**: Uppdaterat avsnitt 10 för att återspegla omfattande fallstudiedäckning med specifika implementeringsdetaljer
- **Changelog-integration**: Lagt till inträde för 26 september 2025 som dokumenterar tillägg av GitHub MCP Registry och förbättringar av fallstudier
- **Datumen uppdaterade**: Uppdaterat datumstämpeln i sidfoten för att återspegla senaste revisionen (26 september 2025)

### Förbättringar av dokumentationskvalitet
- **Ökad konsekvens**: Standardiserad formatering och struktur för fallstudier över alla sju exempel
- **Omfattande täckning**: Fallstudier spänner nu över företags-, utvecklarproduktivitet- och ekosystemutvecklingsscenarier
- **Strategisk positionering**: Förbättrat fokus på MCP som grundläggande plattform för agent-baserad systemdistribution
- **Resursintegration**: Uppdaterat ytterligare resurser för att inkludera GitHub MCP Registry-länk

## 15 september 2025

### Utökning av avancerade ämnen - Anpassade transporter och kontextteknik

#### MCP Anpassade transporter (05-AdvancedTopics/mcp-transport/) - Ny Avancerad Implementeringsguide
- **README.md**: Komplett implementeringsguide för anpassade MCP-transportmekanismer
  - **Azure Event Grid Transport**: Omfattande serverlös händelsestyrd transportimplementation
    - Exempel i C#, TypeScript och Python med Azure Functions-integration
    - Händelsestyrda arkitekturmönster för skalbara MCP-lösningar
    - Webhook-mottagare och push-baserad meddelandehantering
  - **Azure Event Hubs Transport**: Högkapacitets streamingtransportimplementation
    - Realtids streamingkapacitet för låglatensscenarier
    - Partitionering och checkpoint-hanteringsstrategier
    - Meddelandebatchning och prestandaoptimering
  - **Företagsintegrationsmönster**: Produktionsklara arkitektoniska exempel
    - Distribuerad MCP-behandling över flera Azure Functions
    - Hybridtransportarkitekturer som kombinerar flera transporttyper
    - Meddelandets hållbarhet, tillförlitlighet och felhanteringsstrategier
  - **Säkerhet & Övervakning**: Azure Key Vault-integration och observabilitetspatterns
    - Autentisering med hanterad identitet och principen om minsta privilegium
    - Telemetri med Application Insights och prestandaövervakning
    - Kretsbrytare och felmotståndsmönster
  - **Testningsramverk**: Omfattande teststrategier för anpassade transporter
    - Enhetstestning med testdubbletter och mockningsramverk
    - Integrationstestning med Azure Test Containers
    - Överväganden vid prestanda- och lasttestning

#### Kontextteknik (05-AdvancedTopics/mcp-contextengineering/) - Framväxande AI-disciplin
- **README.md**: Omfattande utforskning av kontextteknik som framväxande område
  - **Kärnprinciper**: Fullständig kontextdelning, medvetenhet om handlingsbeslut och hantering av kontextfönster
  - **Anpassning till MCP-protokoll**: Hur MCP-designen adresserar kontextteknikutmaningar
    - Begränsningar för kontextfönster och progressiva laddningsstrategier
    - Relevansbestämning och dynamisk kontextåtervinning
    - Multimodal kontexthantering och säkerhetsaspekter
  - **Implementeringsmetoder**: Enkeltrådad vs. multi-agentarkitektur
    - Kontextuppdelning och prioriteringstekniker
    - Progressiv kontextladdning och komprimeringsstrategier
    - Lager-på-lager-kontekstmetoder och optimering av återvinning
  - **Mätningsramverk**: Framväxande mätetal för bedömning av kontexteffektivitet
    - Inmatningseffektivitet, prestanda, kvalitet och användarupplevelse
    - Experimentella metoder för kontextoptimering
    - Felanalys och förbättringsmetodiker

#### Uppdateringar för läroplansnavigering (README.md)
- **Förbättrad modulstruktur**: Uppdaterad läroplanstabell för att inkludera nya avancerade ämnen
  - Tillagt Context Engineering (5.14) och Custom Transport (5.15) poster
  - Konsekvent formatering och navigationslänkar över alla moduler
  - Uppdaterade beskrivningar för att återspegla nuvarande innehållsomfång

### Förbättringar av katalogstruktur
- **Namngivningsstandardisering**: Omdöpt "mcp transport" till "mcp-transport" för att vara konsekvent med andra avancerade ämnesmappar
- **Innehållsorganisation**: Alla 05-AdvancedTopics-mappar följer nu konsekvent namngivningsmönster (mcp-[ämne])

### Förbättringar av dokumentationskvalitet
- **Anpassning till MCP-specifikation**: Allt nytt innehåll refererar till nuvarande MCP Specification 2025-06-18
- **Exempel i flera språk**: Omfattande kodexempel i C#, TypeScript och Python
- **Företagsfokus**: Produktionsklara mönster och Azure molnintegration genomgående
- **Visuell dokumentation**: Mermaid-diagram för arkitektur- och flödesvisualisering

## 18 augusti 2025

### Omfattande dokumentationsuppdatering - MCP 2025-06-18-standarder

#### MCP Säkerhetsbästa praxis (02-Security/) - Komplett modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullständig omskrivning i linje med MCP Specification 2025-06-18
  - **Obligatoriska krav**: Tillägg av tydliga MÅSTE/MÅSTE INTE-krav från officiell specifikation med klara visuella indikatorer
  - **12 kärnsäkerhetspraxis**: Omstrukturerade från 15-punktslista till omfattande säkerhetsdomäner
    - Tokensäkerhet & autentisering med extern identitetsleverantörsintegration
    - Sessionshantering & transport­säkerhet med kryptografiska krav
    - AI-specifikt hot­skydd med Microsoft Prompt Shields-integration
    - Åtkomstkontroll & behörigheter med principen om minsta privilegium
    - Innehållssäkerhet & övervakning med Azure Content Safety-integration
    - Leveranskedjesäkerhet med omfattande komponentverifiering
    - OAuth-säkerhet & Confused Deputy-förebyggande med PKCE-implementering
    - Incidenthantering & återställning med automatiserade funktioner
    - Efterlevnad & styrning med regulatorisk anpassning
    - Avancerade säkerhetskontroller med zero trust-arkitektur
    - Microsofts säkerhetsekosystemsintegration med omfattande lösningar
    - Kontinuerlig säkerhetsevolution med adaptiva metoder
  - **Microsoft säkerhetslösningar**: Förbättrad integrationsvägledning för Prompt Shields, Azure Content Safety, Entra ID och GitHub Advanced Security
  - **Implementeringsresurser**: Kategoriserade omfattande resurslänkar efter officiell MCP-dokumentation, Microsoft säkerhetslösningar, säkerhetsstandarder och implementeringsguider

#### Avancerade säkerhetskontroller (02-Security/) - Företagsimplementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fullständig översyn med säkerhetsramverk för företag
  - **9 omfattande säkerhetsdomäner**: Utökade från grundläggande kontroller till detaljerat företagsramverk
    - Avancerad autentisering & auktorisering med Microsoft Entra ID-integration
    - Tokensäkerhet & anti-passthrough-kontroller med omfattande validering
    - Sessionssäkerhetskontroller med skydd mot kapning
    - AI-specifika säkerhetskontroller med skydd mot promptinjektion och verktygsförgiftning
    - Confused Deputy-attackförebyggande med OAuth-proxysäkerhet
    - Verktygsexekverings­säkerhet med sandlåda och isolering
    - Leveranskedjesäkerhetskontroller med beroendeverifiering
    - Övervaknings- & detektionskontroller med SIEM-integration
    - Incidenthantering & återställning med automatiserade funktioner
  - **Implementeringsexempel**: Lagt till detaljerade YAML-konfigurationsblock och kodexempel
  - **Microsoftlösningsintegration**: Omfattande täckning av Azure säkerhetstjänster, GitHub Advanced Security och företagsidentitetshantering

#### Säkerhet för avancerade ämnen (05-AdvancedTopics/mcp-security/) - Produktionsklar implementering
- **README.md**: Komplett omskrivning för företagsimplementering av säkerhet
  - **Aktuell specifikationsanpassning**: Uppdaterad till MCP Specification 2025-06-18 med obligatoriska säkerhetskrav
  - **Förbättrad autentisering**: Microsoft Entra ID-integration med omfattande .NET och Java Spring Security-exempel
  - **AI-säkerhetsintegration**: Microsoft Prompt Shields och Azure Content Safety-implementering med detaljerade Python-exempel
  - **Avancerad hotmotverkan**: Omfattande implementeringsexempel för
    - Confused Deputy-attackförebyggande med PKCE och validering av användarsamtycke
    - Token passthrough-förebyggande med publikumsvalidering och säker tokenhantering
    - Sessionskapningsförebyggande med kryptografisk bindning och beteendeanalys
  - **Företagssäkerhetsintegration**: Azure Application Insights-övervakning, hotdetekteringspipelines och leveranskedjesäkerhet
  - **Implementeringschecklista**: Tydlig uppdelning av obligatoriska kontra rekommenderade säkerhetskontroller med Microsofts säkerhetsekosystemfördelar

### Kvalitet och standardanpassning av dokumentation
- **Specifikationsreferenser**: Uppdaterade alla referenser till nuvarande MCP Specification 2025-06-18
- **Microsoft säkerhetsekosystem**: Förbättrad integrationsvägledning genom hela säkerhetsdokumentationen
- **Praktisk implementering**: Lagt till detaljerade kodexempel i .NET, Java och Python med företagsmönster
- **Resursorganisation**: Omfattande kategoriindelning av officiell dokumentation, säkerhetsstandarder och implementeringsguider
- **Visuella indikatorer**: Tydlig märkning av obligatoriska krav kontra rekommenderade metoder


#### Kärnkoncept (01-CoreConcepts/) - Komplett modernisering
- **Protokollversionsuppdatering**: Uppdaterad för att referera till nuvarande MCP Specification 2025-06-18 med datum-baserad versionering (ÅÅÅÅ-MM-DD-format)
- **Arkitekturförfining**: Förbättrade beskrivningar av Hosts, Clients och Servers för att återspegla aktuella MCP-arkitektur­mönster
  - Hosts definierade som AI-applikationer som koordinerar flera MCP-klientanslutningar
  - Clients beskrivna som protokollkopplingar med en-till-en-serverrelationer
  - Servers förbättrade med lokala vs. fjärrdriftsättningsscenarier
- **Primitive omstrukturering**: Fullständig översyn av server- och klientprimitiver
  - Serverprimitiver: Resurser (datakällor), Prompts (mallar), Verktyg (exekverbara funktioner) med detaljerade förklaringar och exempel
  - Klientprimitiver: Sampling (LLM-komplettering), Elicitation (användarinmatning), Loggning (felsökning/övervakning)
  - Uppdaterade med nuvarande metoder för upptäckt (`*/list`), hämtning (`*/get`) och exekvering (`*/call`)
- **Protokollarkitektur**: Infört tvålagerarkitekturmodell
  - Datalager: JSON-RPC 2.0-bas med livscykelhantering och primitiver
  - Transportlager: STDIO (lokal) och Streamable HTTP med SSE (fjärroptimera) transportmekanismer
- **Säkerhetsramverk**: Omfattande säkerhetsprinciper inklusive uttryckligt användarsamtycke, dataskydd, verktygssäkerhet och transportlagersäkerhet
- **Kommunikationsmönster**: Uppdaterade protokollmeddelanden för att visa initialisering, upptäckt, exekvering och notifieringsflöden
- **Kodexempel**: Uppdaterade fler-språks exempel (.NET, Java, Python, JavaScript) för att återspegla aktuella MCP SDK-mönster

#### Säkerhet (02-Security/) - Omfattande säkerhetsöversyn  
- **Standardanpassning**: Fullständig anpassning till MCP Specification 2025-06-18 säkerhetskrav
- **Autentiseringens utveckling**: Dokumenterad övergång från anpassade OAuth-servrar till delegat från extern identitetsleverantör (Microsoft Entra ID)
- **AI-specifik hotanalys**: Förbättrad täckning av moderna AI-attackvektorer
  - Detaljerade scenarier för promptinjektionsattacker med verkliga exempel
  - Verktygsförgiftning och "rug pull"-attackmönster
  - Kontextfönsterförgiftning och modell­förvirringsattacker
- **Microsoft AI-säkerhetslösningar**: Omfattande täckning av Microsofts säkerhetsekosystem
  - AI Prompt Shields med avancerad upptäckt, spotlighting och avgränsningstekniker
  - Azure Content Safety integrationsmönster
  - GitHub Advanced Security för leveranskedjeskydd
- **Avancerad hotmotverkan**: Detaljerade säkerhetskontroller för
  - Sessionskapning med MCP-specifika attackscenarier och krav på kryptografiskt sessions-ID
  - Confused Deputy-problem i MCP-proxy-scenarier med uttryckliga samtyckeskrav
  - Token passthrough-sårbarheter med obligatoriska valideringskontroller
- **Leveranskedjesäkerhet**: Utökad AI-leveranskedjetäckning inklusive grundmodeller, embeddings-tjänster, kontextleverantörer och tredjeparts-API:er
- **Grundläggande säkerhet**: Förbättrad integration med företags­ säkerhetsmönster inklusive zero trust-arkitektur och Microsofts säkerhetsekosystem
- **Resursorganisation**: Kategoriserade omfattande resurslänkar efter typ (Officiell Dokumentation, Standarder, Forskning, Microsoft Lösningar, Implementeringsguider)

### Förbättringar av dokumentationskvalitet
- **Strukturerade lärandemål**: Förbättrade lärandemål med specifika, handlingsbara resultat
- **Korsreferenser**: Lagt till länkar mellan relaterade säkerhets- och kärnkonceptämnen
- **Aktuell information**: Uppdaterade alla datumreferenser och specifikationslänkar till aktuella standarder
- **Implementeringsvägledning**: Lagt till specifika, handlingsbara implementeringsriktlinjer i båda sektionerna

## 16 juli 2025

### README och navigationsförbättringar
- Fullständigt omdesignad läroplansnavigering i README.md
- Ersatte `<details>`-taggar med mer tillgängligt tabellformat
- Skapade alternativa layoutalternativ i ny mapp "alternative_layouts"
- Lade till kortbaserade, flikade och dragspelsstil navigations-exempel
- Uppdaterade sektionen för repostruktur för att inkludera alla senaste filer
- Förbättrade sektionen "Hur man använder denna läroplan" med tydliga rekommendationer
- Uppdaterade MCP-specifikationslänkar för att peka på korrekta URL:er
- Lade till sektion för Context Engineering (5.14) i läroplansstrukturen

### Uppdateringar av studieguiden
- Fullständigt reviderad studieguiden för att anpassas till aktuella repostruktur
- Lagt till nya avsnitt för MCP-klienter och verktyg, samt populära MCP-servrar
- Uppdaterade visuella läroplansöversikt för att exakt återspegla alla ämnen
- Förbättrade beskrivningar av avancerade ämnen för att täcka alla specialiserade områden
- Uppdaterade fallstudieavsnitt för att återspegla verkliga exempel
- Lagt till detta omfattande changelog

### Communitybidrag (06-CommunityContributions/)
- Lagt till detaljerad information om MCP-servrar för bildgenerering
- Lagt till omfattande sektion om användning av Claude i VSCode
- Lagt till instruktioner för installation och användning av Cline terminalklient
- Uppdaterade MCP-klientsektion för att inkludera alla populära klientalternativ
- Förbättrade bidragsexempel med mer precisa kodexempel

### Avancerade ämnen (05-AdvancedTopics/)
- Organiserade alla specialiserade ämnesmappar med konsekvent namngivning
- Lagt till material och exempel för kontextteknik
- Lagt till dokumentation för Foundry agent-integration
- Förbättrade dokumentation för Entra ID-säkerhetsintegration

## 11 juni 2025

### Initial skapelse
- Släppt första versionen av MCP för nybörjare-läroplan

- Skapade grundstruktur för alla 10 huvudsektioner
- Implementerade Visuell Kursplan för navigering
- Lagt till initiala exempelprojekt i flera programmeringsspråk

### Komma Igång (03-GettingStarted/)
- Skapade första serverimplementeringsexempel
- Lagt till vägledning för klientutveckling
- Inkluderade instruktioner för LLM-klientintegration
- Lagt till dokumentation för VS Code-integration
- Implementerade Server-Sent Events (SSE) serverexempel

### Kärnkoncept (01-CoreConcepts/)
- Lagt till detaljerad förklaring av klient-server-arkitektur
- Skapade dokumentation om nyckelprotokollkomponenter
- Dokumenterade meddelandemönster i MCP

## 23 maj 2025

### Repositorystruktur
- Initierade repository med grundläggande mappstruktur
- Skapade README-filer för varje huvudsektion
- Satt upp översättningsinfrastruktur
- Lagt till bildresurser och diagram

### Dokumentation
- Skapade initial README.md med översikt av kursplanen
- Lagt till CODE_OF_CONDUCT.md och SECURITY.md
- Satt upp SUPPORT.md med vägledning för att få hjälp
- Skapade preliminär struktur för studieguide

## 15 april 2025

### Planering och Ramverk
- Initial planering för MCP för nybörjare-kursplan
- Definierade lärandemål och målgrupp
- Skisserade 10-sektions struktur för kursplanen
- Utvecklade konceptuellt ramverk för exempel och fallstudier
- Skapade initiala prototypexempel för nyckelkoncept

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
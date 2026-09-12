# Wijzigingslogboek: MCP voor Beginners Curriculum

Dit document dient als een overzicht van alle belangrijke wijzigingen die zijn aangebracht in het Model Context Protocol (MCP) voor Beginners curriculum. Wijzigingen worden achterstevoren chronologisch gedocumenteerd (nieuwste wijzigingen eerst).

## 9 september 2026

### MCP 2026-07-28 Definitieve Specificatie Afstemming

Bijgewerkt van de Engelse cursus van release-kandidaat en `2025-11-25`
basishandleiding naar de definitieve MCP `2026-07-28` specificatie.

- **Bijgewerkt**: Referenties naar de huidige versie, specificatielinks, stateless
  aanvraagrichtlijnen, `server/discover`, Streamable HTTP-headers en de levenscyclus
  van de Tasks extensie in 38 Engelse documentatiebestanden.
- **Gecorrigeerd**: Elicitation gebruikt nu `elicitation/create`, Sampling gebruikt
  `sampling/createMessage` en `InputRequiredResult.resultType` gebruikt
  `"input_required"`.
- **Vervangen**: De onnauwkeurige Root Context gesprekstoestand les door een
  protocol-accurate Roots les die informatieve bestandssysteem hints, de
  huidige multi-ronde-trip flow, beveiligingsgrenzen en migratie-opties behandelt.
- **Verduidelijkt**: Roots, Sampling, Logging en Dynamic Client Registration zijn
  verouderd in `2026-07-28`, met hun aanbevolen vervangingen en vroegste
  verwijderdatum gedocumenteerd.
- **Gemarkeerd**: Voorbeelden die nog afhankelijk zijn van MCP `2025-11-25`, HTTP+SSE,
  initialisatie-handshakes of protocolsessies blijven behouden als legacy
  compatibiliteit voorbeelden in plaats van gepresenteerd als huidige implementaties.
- **Beveiligingsrichtlijnen**: Bijgewerkt de op zichzelf staande beveiligingsgidsen om
  autorisatie per aanvraag te gebruiken en expliciete applicatiestatus-handles in plaats van
  verwijderde protocol-sessie-ID's. Client ID Metadata Documenten zijn nu
  het voorkeursregistratiepad, met DCR gedocumenteerd als alleen compatibiliteit.
- **Ondersteunend materiaal**: Bijgewerkt de studiegids, contribiteur checklist,
  Publora case study, en APIM case study. De APIM walkthrough beveelt nu
  de huidige Streamable HTTP `/mcp` endpoint aan in plaats van de verouderde `/sse`.
- **Canonieke links**: Verouderde en concept specificatie-URL's in Engelse
  bronnen in Markdown vervangen door versiegebonden `2026-07-28` links, terwijl expliciete
  links naar legacy versies behouden blijven waar een voorbeeld nog gekoppeld is aan oudere tooling.
- **Stabiele bestandsnamen**: De definitieve specificatiegids en twee beveiligings-
  gidsen hernoemd om release-kandidaat en jaartal achtervoegsels te verwijderen, waarna alle Engelse
  hyperlinks zijn bijgewerkt naar hun stabiele paden.
- **Nieuwe autorisatievoorbeeld**: Toegevoegd een geteste
  [TypeScript MCP `2026-07-28` resource server](./02-Security/samples/cimd-dcr-auth/README.md)
  die Client ID Metadata Documenten vergelijkt met de verouderde Dynamic
  Client Registration fallback. Het voorbeeld bevat RFC 9728 discovery, JWKS
  validatie, scopes per tool, twaalf tests en een Auth0 configuratieworkthrough.
- **Vertaalbereik**: Alleen Engelse bronbestanden zijn bewerkt; gegenereerde
  vertalingen en vertaalde afbeeldingen blijven ongewijzigd omdat deze automatisch worden vertaald.

## 29 juli 2026

### Nieuwe Module 08 Metgezel: Betrouwbaarheid Sidecars en Veilige Herhalingen

Toegevoegd een leverancier-neutrale metgezel les voor MCP-gereedschappen die realistische
effecten creëren, afgestemd op de definitieve `2026-07-28` specificatie.

- **Nieuw**: De [betrouwbaarheid sidecar metgezel les][reliability-sidecar]
  gebruikt een supportticket verhaal, twee Mermaid diagrammen en een beslis-
  stroom voor herhalingen om stabiele operatie-sleutels, atomaire dubbele toelating,
  reconciliatie, bewijs en de Tasks extensiegrens uit te leggen.
- **Nieuw**: Een standard-library Python en SQLite foutinjectie-oefening
  gebruikt aparte opslagplaatsen voor operaties en tickets om te demonstreren dat een
  antwoord verloren gaat nadat een extern effect commit. Zes deterministische tests behandelen naïeve
  duplicatie, beschermde herstart recovery, payload conflicten, gecachte resultaten,
  actieve claims en gelijktijdige dubbele toelating.
- **Bijgewerkt**: Module 08 linkt nu naar de metgezel les, identificeert het
  definitieve `2026-07-28` stateless verzoekmodel, onderscheidt OpenTelemetry
  observability van de verouderde MCP logging feature en beperkt zijn
  generieke retry voorbeeld tot read-only operaties.
- **Optioneel**: De les koppelt zijn draagbare concepten aan één getagde community
  implementatie zonder dat de gehoste dienst of een netwerkoproep deel uitmaakt van
  de oefening.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juli 2026

### Nieuwe les: De MCP Specificatie Release Candidate 2026-07-28

Toegevoegd de aankomende release candidate van de MCP specificatie `2026-07-28` (aangekondigd 21 mei 2026; definitieve release gepland 28 juli 2026), samengevat uit de [officiële aankondigingsblogpost](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). De basislijn van het curriculum blijft **MCP Specificatie 2025-11-25** totdat de nieuwe versie uitkomt, dus dit wordt gepresenteerd als vooruitziende richtlijnen in plaats van een herschrijving van bestaande lessen.

- **Nieuw**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — een volledige les die de stateless protocol kern behandelt (verwijdering van de `initialize` handshake en `Mcp-Session-Id`), de nieuwe `Mcp-Method`/`Mcp-Name` routeringsheaders, `ttlMs`/`cacheScope` cachemetadata, W3C Trace Context in `_meta`, het formele Extensies-framework (MCP Apps en de nieuwe Tasks extensie), zes autorisatie-versterkende SEPs, de veroudering van Roots/Sampling/Logging, en de overstap naar volledige JSON Schema 2020-12 voor tool schema’s.
- **Bijgewerkt** met vooruitziende verwijzingen naar de nieuwe les:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protocolversie notitie, Sampling/Roots/Logging/Tasks secties en "Wat komt hierna"
  - [02-Security/README.md](./02-Security/README.md): autorisatie versterking verwijzing
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport verwijzing
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling veroudering verwijzing
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging veroudering en Tasks extensie verwijzing
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routeringsverwijzing
  - [README.md](./README.md): "Vooruitkijken" notitie in de specificatiesectie en een nieuwe `1.1` vermelding in de curriculum module tabel
  - [study_guide.md](./study_guide.md): vooruitziende opsomming onder de Core Concepts overzicht en een gedateerde addendum notitie
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): verwijzing naar de `mcp-session-id` transportmap voorafgaand aan het stateless verzoekmodel
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduleoverzicht-verwijzing over Root Contexts/Sampling verouderingen en de Tasks extensie
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisatie versterking verwijzing

## 24 juni 2026

### Nieuwe les: Gebruik van MCP in Copilot app

- [Tooling sectie](./12-tooling/README.md) Toegevoegd tooling sectie.
- [MCP in Copilot app](./12-tooling/01-copilot-app/README.md)

## 16 juni 2026

### MCP Specificatie Afstemming & Voorbeeldvalidatie

Het curriculum gevalideerd tegen de huidige **MCP Specificatie 2025-11-25** en de nieuwste officiële SDK's, daarna de resterende verouderde specificatielinks gecorrigeerd en bevestigd dat de kernvoorbeelden nog steeds bouwen en draaien.

#### Specificatie Versie Correcties (2025-06-18 / 2025-03-26 → 2025-11-25)

Engelse inhoud bijgewerkt waar nog werd beweerd dat een oudere specificatieversie de *huidige/laatste* standaard was, en links herwezen naar de canonieke `modelcontextprotocol.io` specificatiepaden:
- **05-AdvancedTopics/mcp-security/README.md**: De "Huidige Standaard" banner, inleiding, kernbeveiligingsprincipes kop, verplichte eisen kop, Microsoft Entra ID sectie, Referenties & Bronnen links en afsluitende beveiligingsmededeling (8 referenties) bijgewerkt naar 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Link naar extra bronnen specificatie en "Huidige Standaard" banner bijgewerkt naar 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: De verouderde `2025-03-26` security-and-trust link vervangen door de huidige 2025-11-25 pagina voor beveiligingsbest practices
- **03-GettingStarted/14-sampling/README.md**: De officiële sampling docs link bijgewerkt naar 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: De huidige-tijd "huidige MCP specificatie" verwijzing en de link naar extra bronnen specificatie bijgewerkt naar 2025-11-25 (historische SSE-verouderingsnotities ongewijzigd voor nauwkeurigheid)

#### Voorbeeldvalidatie tegen huidige SDK's

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` installeerde `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` geslaagd zonder typefouten — bestaande `McpServer`/`StdioServerTransport` APIs blijven geldig
- **Python (03-GettingStarted/01-first-server/solution/python)**: Gevalideerd in een geïsoleerde `.venv` met `mcp[cli]` (1.27.2); `py_compile` geslaagd en `FastMCP.list_tools()` retourneerde correct de `add` en `subtract` tools
- Bevestigd dat alle voorbeelden met `@modelcontextprotocol/sdk` versiebereiken (`>=1.26.0` / `^1.26.0` / `^1.27.0`) schoon oplossen naar de huidige `1.29.0` zonder breuk in API wijzigingen

#### Dependency Pin Afstemming (versiekloof sluiting)

Verouderde SDK versies omhoog gebracht zodat elk voorbeeld de huidige MCP release volgt, overeenkomstig de repo-brede conventie:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` verhoogd van `^1.8.0` → `>=1.26.0` en de verouderde `"updated for MCP 2025-06-18"` pakketbeschrijving bijgewerkt naar `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** en **lab4/code/github_mcp_server/pyproject.toml**: Exacte pin `mcp==1.23.0` verhoogd naar `mcp>=1.26.0`; beide `uv.lock` bestanden opnieuw gegenereerd (`uv lock`) zodat de lockfiles resolven naar de huidige `mcp 1.27.2` en synchroniseren met de manifesten

#### Curriculum Gap Analyse — Laatste Specificatie Feature Dekking

Bevestigd dat het curriculum al alle primitieve elementen die geïntroduceerd/uitgebreid zijn in MCP 2025-11-25 behandelt, dus er zijn geen inhoudelijke hiaten:
- **Sampling**: Les 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. URL modus)**: Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Gedocumenteerd in 00-Introduction, 01-CoreConcepts, en 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimenteel, langlopende operaties)**: Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotaties** (`readOnlyHint` / `destructiveHint`): Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features

### Beveiligingsversterking & Behandeling van Dependency Kwetsbaarheden

Een volledige beveiligingscontrole uitgevoerd over elke dependency manifest en de voorbeeld broncode, daarna alle gemelde npm advisories en één code-niveau bevinding verholpen. Na correctie meldt `npm audit` **0 kwetsbaarheden** in elke gecontroleerde directory.

#### npm Dependency Kwetsbaarheden (transitief) — Verholpen

Alle 15 gecommitteerde `package-lock.json` bestanden gecontroleerd. Kwetsbaarheden waren beperkt tot transitieve dependencies die binnenkwamen via de MCP Inspector dev tool, de OpenAI client en de MCP SDK; al deze zijn nu opgelost zonder de voorbeelden te breken:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** en **lab3/code/weather_mcp/inspector**: Bijgewerkt `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), waarmee de gebundelde `ajv`, `brace-expansion`, `diff`, `path-to-regexp` en `ws` waarschuwingen zijn opgelost. Toegevoegd een npm `overrides` vermelding die de gepatchte `shell-quote@1.8.4` forceert om de resterende kritieke waarschuwing van `concurrently` te elimineren; beide lockfiles opnieuw gegenereerd (nu 0 kwetsbaarheden)
- **03-GettingStarted/samples/typescript**: `npm audit fix` heeft de transitieve `qs` (matig) bijgewerkt naar een gepatchte release
- **03-GettingStarted/samples/javascript**: `npm audit fix` heeft de transitieve `hono` (matig) bijgewerkt naar een gepatchte release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` heeft de transitieve `form-data` (hoog) bijgewerkt naar een gepatchte release
- **03-GettingStarted/11-simple-auth/solution/typescript**: De ontbrekende `package-lock.json` gegenereerd zodat het project reproduceerbaar en auditbaar is (0 kwetsbaarheden)

#### Beveiligingsfix op code-niveau (OWASP A03: Injectie)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `shell=True` verwijderd uit het `open_in_vscode` gereedschap. De eerdere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` liet shell-meta-tekens in een map pad toe om geïnterpreteerd te worden door `cmd.exe` (command-injectie vectortje). Nu start het direct de opgeloste `Code.exe` met de map als argument - geen shell - wat functioneel equivalent en veilig is

#### Python Afhankelijkheid Audit

- Iedere Python requirements set geaudit met `pip-audit`. `05-AdvancedTopics` en `03-GettingStarted/samples/python` meldden **geen bekende kwetsbaarheden** (hun `mcp` / `httpx` / `pydantic` / `python-dotenv` versies komen overeen met actuele gepatchte releases)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` gaf de transitieve afhankelijkheid **`werkzeug` 3.1.1** aan met drie `safe_join` Windows apparaatnaam DoS waarschuwingen — `CVE-2025-66221`, `CVE-2026-21860`, en `CVE-2026-27199` (alle drie opgelost in 3.1.6). Toegevoegd een expliciete beveiligingspin `werkzeug>=3.1.6` zodat de gepatchte release wordt gebruikt; geverifieerd dat de beperking schoon oplost met de `chainlit` / `mcp` / `semantic-kernel` stack

### Productnaam Rebranding

Alle curriculum inhoud bijgewerkt om de producthernoeming van Microsoft te weerspiegelen:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord community link bijgewerkt
- **AGENTS.md**: Discord server verwijzing bijgewerkt
- **README.md**: Technologie-ecosysteem verwijzingen bijgewerkt
- **study_guide.md**: Verwijzingen case study bijgewerkt
- **05-AdvancedTopics/README.md**: Titel en beschrijving Module 5.13 bijgewerkt
- **05-AdvancedTopics/mcp-integration/README.md**: Sectiekop en beschrijving bijgewerkt
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Volledige module titel en inhoud bijgewerkt
- **05-AdvancedTopics/mcp-security-entra/README.md**: Kruisverwijzing link bijgewerkt
- **07-LessonsfromEarlyAdoption/README.md**: Verwijzingen case study bijgewerkt
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Sectie 9 kop, badges en mogelijkheden bijgewerkt
- **08-BestPractices/README.md**: Discord community link bijgewerkt
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discord kanaal verwijzing bijgewerkt
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Verwijzing model deployment bijgewerkt
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI Services tabel bijgewerkt
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Ressourcenverwijzingen bijgewerkt

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension voor VS Code
- **README.md**: Hoofdcurriculum verwijzingen bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Moduletitel, overzicht en alle modulekoppen bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Titel, leerdoelen, setup instructies en bronnen bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Titel, leerdoelen, MCP hosts tabel en kruisverwijzingen bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Titel, badges, vereisten en bronnen bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Agent Builder verwijzingen en feedback link bijgewerkt
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Vereisten en extensieverwijzingen bijgewerkt

---

## 11 april 2026

### Nieuwe Les, Documentatiefixes en Afhankelijkheidsupdates

#### Nieuwe Curriculum Inhoud Toegevoegd

**Module 05 - Gevorderde Onderwerpen**
- **Les 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nieuwe uitgebreide gids over het adversarial debatpatroon voor multi-agent systemen
  - Mermaid architectuurdiagram: twee agenten → gedeelde MCP server → debat transcriptie → scheidsrechter → oordeel
  - Gedeelde MCP tool server (`web_search` + `run_python`) geïmplementeerd in Python en TypeScript
  - Tegenstrijdige systeem prompts (VOOR / TEGEN / Scheidsrechter) met expliciete tool gebruik vereisten
  - Debat orchestrator in Python, TypeScript en C# die rondes beheert en argumenten routeert
  - MCP `ClientSession` koppeling voor de orchestrator aan echte toolcalls
  - Gebruikstabel (hallucinatie detectie, dreigingsmodellering, API ontwerpreview, feitelijke verificatie, tech selectie)
  - Beveiligingsoverwegingen: sandboxed uitvoering, tool-call validatie, rate limiting, audit logging
  - Gestructureerde oefening met drie praktische scenario’s (code review, architectuurbeslissing, content moderatie)

#### Documentatiefixes

**Module 03 - Aan de Slag**
- **05-stdio-server/README.md**: Onvolledig TypeScript stdio server voorbeeld gefixt — ontbrekende transport instantie toegevoegd (`new StdioServerTransport()`) en `server.connect(transport)` aanroep om overeen te komen met de Python- en .NET voorbeelden in dezelfde sectie
- **14-sampling/README.md**: Typfout gecorrigeerd — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculum Updates

**Hoofd README.md**
- Invoeging 5.17 (Adversarial Multi-Agent Reasoning with MCP) toegevoegd aan de curriculum tabel met directe link naar de nieuwe les

**05-AdvancedTopics/README.md**
- Rij Les 5.17 toegevoegd aan de leslijst

**study_guide.md**
- Adversarial Multi-Agent Reasoning onderwerp toegevoegd aan mindmap en proza-beschrijving van Gevorderde Onderwerpen

#### Code- en beveiligingsfixes

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Beveiligingsfix — command injection**: `execSync` shell interpolatie vervangen door `execFile` + `promisify` in TypeScript `run_python` tool, waardoor het command-injectie oppervlak is geëlimineerd (LLM-gestuurde code wordt nu als literal argv element doorgegeven zonder shell-inmenging)
- **MCP tool loop koppeling**: Python debat orchestrator bijgewerkt om `AsyncAnthropic` client te gebruiken (vervanger voor blokkerende sync `Anthropic`), een live `ClientSession` direct aan elke agent beurt te geven, tooldefinities op te halen via `session.list_tools()` elke beurt, en `tool_use` blokken te dispatchen via `session.call_tool()` in een loop totdat het model een finale tekstrespons geeft

#### Afhankelijkheidsupdates

- `hono` geüpdatet naar 4.12.12 in meerdere pakketten (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- `@hono/node-server` geüpdatet van 1.19.11 naar 1.19.13 in TypeScript pakketten
- `cryptography` geüpdatet van 46.0.5 naar 46.0.7 in Python pakketten (10-StreamliningAIWorkflows labs 3 en 4)
- `lodash` geüpdatet van 4.17.23 naar 4.18.1 in 10-StreamliningAIWorkflows inspector

#### Vertalingen

- Vertalingen gesynchroniseerd voor 48+ talen met de nieuwste bronwijzigingen (i18n update)

---

## 5 februari 2026

### Repository-brede Validatie- en Navigatieverbeteringen

#### Nieuwe Curriculum Inhoud Toegevoegd

**Module 03 - Aan de Slag**
- **12-mcp-hosts/README.md**: Nieuwe uitgebreide gids voor het opzetten van MCP hosts
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf configuratievoorbeelden
  - JSON configuratiesjablonen voor alle belangrijke hosts
  - Transport types vergelijkingstabel (stdio, SSE/HTTP, WebSocket)
  - Problemen oplossen van veelvoorkomende verbindingsproblemen
  - Beveiligingsbest practices voor hostconfiguratie

- **13-mcp-inspector/README.md**: Nieuwe debugging gids voor MCP Inspector
  - Installatiemethoden (npx, npm globaal, vanuit bron)
  - Verbinden met servers via stdio en HTTP/SSE
  - Testgereedschappen, bronnen en promptworkflows
  - VS Code integratie met MCP Inspector
  - Veelvoorkomende debugscenario's met oplossingen

**Module 04 - Praktische Implementatie**
- **pagination/README.md**: Nieuwe paginatie implementatie gids
  - Cursor-gebaseerde paginatiepatronen in Python, TypeScript, Java
  - Client-side paginatie handling
  - Cursor ontwerp strategieën (ondoorzichtig vs gestructureerd)
  - Prestatie-optimalisatie aanbevelingen

**Module 05 - Gevorderde Onderwerpen**
- **mcp-protocol-features/README.md**: Nieuwe diepe duik in protocolfuncties
  - Implementatie van voortgangsmeldingen
  - Patroon voor request annulering
  - Resource sjablonen met URI patronen
  - Server levenscyclusbeheer
  - Logging niveau controle
  - Foutafhandelingspatronen met JSON-RPC codes

#### Navigatiefixes (24+ bestanden bijgewerkt)

**Hoofdmodule READMEs**
 Nu links naar zowel eerste les ALS volgende module

**02-Security Sub-bestanden**
- Alle 5 aanvullende beveiligingsdocumenten hebben nu "Wat Nu" navigatie:

**09-CaseStudy Bestanden**
- Alle case study bestanden hebben nu sequentiële navigatie:

**10-StreamliningAI Labs**
Toegevoegd "Wat Nu" sectie aan Module 10 overzicht en Module 11

#### Code- en Inhoudsfouten

**SDK en Afhankelijkheidsupdates**
Lege openai versie gefixt naar `^4.95.0`
SDK bijgewerkt van `^1.8.0` naar `>=1.26.0`
MCP versiepinnen bijgewerkt naar `>=1.26.0`

**Codefixes**
Ongeldig model `gpt-4o-mini` gefixt naar `gpt-4.1-mini`

**Inhoudsfouten**
Verbroke link `READMEmd` → `README.md` gefixt, curriculum kop `Module 1-3` → `Module 0-3` gecorrigeerd, hoofdlettergevoelige pad gefixt
Beschadigde dubbele Case Study 5 inhoud verwijderd

**Verbeteringen Beginnershandleiding**
Goede introductie, leerdoelen en vereisten toegevoegd voor beginners

#### Curriculum Updates

**Hoofd README.md**
- Invoer 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginatie), 5.16 (Protocol Features) toegevoegd aan curriculum tabel

**Module READMEs**
Lessen 12 en 13 toegevoegd aan leslijst
Praktische Gidsen sectie toegevoegd met paginatie link
Lessen 5.15 (Custom Transport) en 5.16 (Protocol Features) toegevoegd

**study_guide.md**
- Mindmap bijgewerkt met alle nieuwe onderwerpen: MCP Hosts Setup, MCP Inspector, Paginatie Strategieën, Deep Dive Protocol Functies

## 28 jan 2026

### MCP Specificatie 2025-11-25 Nalevingsbeoordeling

#### Core Concepten Verbetering (01-CoreConcepts/)
- **Nieuwe Client Primitief - Roots**: Uitgebreide documentatie toegevoegd over de Roots client primitief, waardoor servers filesystem grenzen en toegangsmachtigingen kunnen begrijpen
- **Tool Annotaties**: Documentatie toegevoegd over tool gedragsannotaties (`readOnlyHint`, `destructiveHint`) voor betere tooluitvoeringsbeslissingen
- **Tool Aanroepen in Sampling**: Sampling documentatie bijgewerkt met `tools` en `toolChoice` parameters voor modelgestuurde tooloproepen tijdens samplingverzoeken
- **URL Mode Elicitation**: Documentatie toegevoegd over URL-gebaseerde elicitation voor server-geïnitieerde externe webinteracties
- **Taken (Experimenteel)**: Nieuwe sectie toegevoegd die de experimentele Taken feature voor duurzame uitvoeringswikkels en uitgestelde resultaatopvraging documenteert

- **Iconenondersteuning**: Opgemerkt dat tools, bronnen, brontemplates en prompts nu iconen kunnen bevatten als aanvullende metadata

#### Documentatie-updates
- **README.md**: Toegevoegd MCP-specificatie versie 2025-11-25 en uitleg over versiebeheer op basis van datum
- **study_guide.md**: Bijgewerkte curriculumkaart om taken en toolannotaties op te nemen in de sectie Kernconcepten; bijgewerkte documenttijdstempel

#### Specificatie-nalevingsverificatie
- **Protocolversie**: Gecontroleerd dat alle documentatie verwijst naar de huidige MCP-specificatie 2025-11-25
- **Architectuurovereenkomst**: Bevestigde juiste documentatie van tweelaagse architectuur (Datalaag + Transportlaag)
- **Primitieven documentatie**: Bevestigde serverprimitieven (Brondsen, Prompts, Tools) en clientprimitieven (Sampling, Elicitation, Logging, Roots)
- **Transportmechanismen**: Gecontroleerd juiste documentatie van STDIO en Streamable HTTP transport
- **Beveiligingsrichtlijnen**: Bevestigde afstemming op huidige MCP Security Best Practices documentatie

#### Belangrijke MCP 2025-11-25 functies gedocumenteerd
- **OpenID Connect Discovery**: Auth server discovery via OIDC
- **OAuth Client ID metadata documenten**: Aanbevolen clientregistratiemechanisme
- **JSON Schema 2020-12**: Standaard dialect voor MCP schema-definities
- **SDK-niveausysteem**: Geformaliseerde vereisten voor SDK feature-ondersteuning en onderhoud
- **Governancestructuur**: Geformaliseerde werkgroepen en belangengroepen in MCP governance

### Grote update beveiligingsdocumentatie (02-Security/)

#### Integratie MCP Security Summit Workshop (Sherpa)
- **Nieuwe praktische trainingsbron**: Toegevoegd uitgebreide integratie met de [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in alle beveiligingsdocumentatie
- **Expeditieroutebeschrijving**: Gedocumenteerde volledige tocht van kamp tot kamp van Base Camp tot Summit
- **OWASP-afstemming**: Alle beveiligingsrichtlijnen zijn nu gekoppeld aan OWASP MCP Azure Security Guide risico’s

#### Integratie OWASP MCP Top 10
- **Nieuwe sectie**: Toegevoegd OWASP MCP Top 10 beveiligingsrisicotabel met Azure mitigaties aan hoofd README beveiliging
- **Risicogerichte documentatie**: mcp-security-controls-2025.md geactualiseerd met OWASP MCP risicoverwijzingen per beveiligingsdomein
- **Referentiearchitectuur**: Verwijzing naar OWASP MCP Azure Security Guide referentiearchitectuur en implementatiepatronen

#### Bijgewerkte beveiligingsbestanden
- **README.md**: Toegevoegd Sherpa Workshop overzicht, expeditieroutetabel, OWASP MCP Top 10 risicosamenvatting en sectie voor praktische training
- **mcp-security-controls-2025.md**: Header bijgewerkt naar februari 2026, OWASP risicoverwijzingen (MCP01-MCP08) toegevoegd, inconsistentie in spec-versie opgelost
- **mcp-security-best-practices-2025.md**: Toegevoegd Sherpa en OWASP resources sectie, bijgewerkte timestamp
- **mcp-best-practices.md**: Toegevoegd praktische trainingssectie met Sherpa en OWASP links
- **azure-content-safety-implementation.md**: Toegevoegd OWASP MCP06 verwijzing, Sherpa Camp 3 afstemming en extra resources sectie

#### Nieuwe resource links toegevoegd
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuele OWASP MCP risico pagina’s (MCP01-MCP10)

### Curriculum-brede MCP-specificatie 2025-11-25 afstemming

#### Module 03 - Aan de slag
- **SDK-documentatie**: Go SDK toegevoegd aan officiële SDK-lijst; alle SDK-verwijzingen bijgewerkt naar MCP-specificatie 2025-11-25
- **Transportverduidelijking**: Bijgewerkte beschrijvingen voor STDIO en HTTP Streaming transport met expliciete specificatieverwijzingen

#### Module 04 - Praktische implementatie
- **SDK-updates**: Go SDK toegevoegd; SDK-lijst bijgewerkt met specificatieversieverwijzing
- **Autorisatiespecificatie**: MCP autorisatie-specificatielink bijgewerkt naar huidige versie 2025-11-25

#### Module 05 - Geavanceerde onderwerpen
- **Nieuwe functies**: Opmerking toegevoegd over nieuwe MCP-specificatie 2025-11-25 functies (Taken, Toolannotaties, URL-modus elicitation, Roots)
- **Beveiligingsbronnen**: OWASP MCP Top 10 en Sherpa workshop links toegevoegd aan aanvullende referenties

#### Module 06 - Communitybijdragen
- **SDK-lijst**: Swift en Rust SDKs toegevoegd; specificatielink bijgewerkt naar 2025-11-25
- **Specificatieverwijzing**: MCP-specificatielink bijgewerkt naar directe specificatie-URL

#### Module 07 - Lessen van vroege adoptie
- **Bronupdates**: MCP-specificatie 2025-11-25 link en OWASP MCP Top 10 toegevoegd aan aanvullende resources

#### Module 08 - Best Practices
- **Spec-versie**: MCP-specificatieverwijzing bijgewerkt naar 2025-11-25
- **Beveiligingsbronnen**: OWASP MCP Top 10 en Sherpa workshop toegevoegd aan aanvullende referenties

#### Module 10 - AI-workflows stroomlijnen
- **Badge-update**: MCP-versiebadge gewijzigd van SDK-versie (1.9.3) naar specificatieversie (2025-11-25)
- **Bronlinks**: MCP-specificatielink bijgewerkt; OWASP MCP Top 10 toegevoegd

#### Module 11 - MCP Server hands-on labs
- **Specificatieverwijzing**: MCP-specificatielink bijgewerkt naar versie 2025-11-25
- **Beveiligingsbronnen**: OWASP MCP Top 10 toegevoegd aan officiële resources

## 18 december 2025

### Update beveiligingsdocumentatie - MCP-specificatie 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Update specificatieversie
- **Protocolversie-update**: Bijgewerkt om te verwijzen naar de nieuwste MCP-specificatie 2025-11-25 (uitgebracht 25 november 2025)
  - Alle specificatieversieverwijzingen bijgewerkt van 2025-06-18 naar 2025-11-25
  - Documentdatumverwijzingen bijgewerkt van 18 augustus 2025 naar 18 december 2025
  - Gecontroleerd dat alle specificatie-URL’s verwijzen naar actuele documentatie
- **Inhoudsvalidatie**: Uitgebreide validatie van beste beveiligingspraktijken tegen nieuwste standaarden
  - **Microsoft Security Solutions**: Controle op actuele terminologie en links voor Prompt Shields (voorheen "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID en Azure Key Vault
  - **OAuth 2.1 Security**: Bevestigde afstemming op de nieuwste OAuth-beveiligingsmaatregelen
  - **OWASP-standaarden**: Gevalideerde OWASP Top 10 voor LLMs verwijzingen blijven actueel
  - **Azure Services**: Alle Microsoft Azure documentatielinks en best practices gecontroleerd
- **Standaardafstemming**: Alle aangeroepen beveiligingsstandaarden bevestigd actueel
  - NIST AI Risicobeheer Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure beveiligings- en compliancekaders
- **Implementatieresources**: Alle implementatiehandleidinglinks en bronnen geverifieerd
  - Azure API Management authenticatiepatronen
  - Microsoft Entra ID integratiehandleidingen
  - Azure Key Vault secretsbeheer
  - DevSecOps-pijplijnen en monitoringoplossingen

### Documentatie kwaliteitsborging
- **Specificatienaleving**: Gecontroleerd dat alle verplichte MCP-beveiligingseisen (MOET/MAG NIET) overeenkomen met de nieuwste specificatie
- **Actualiteit resources**: Gecontroleerd op alle externe links naar Microsoft documentatie, beveiligingsstandaarden en implementatiehandleidingen
- **Beste Praktijken dekking**: Bevestigde uitgebreide dekking van authenticatie, autorisatie, AI-specifieke dreigingen, supply chain beveiliging en enterprise-patronen

## 6 oktober 2025

### Uitbreiding Aan de slag sectie – Geavanceerd servergebruik & eenvoudige authenticatie

#### Geavanceerd servergebruik (03-GettingStarted/10-advanced)
- **Nieuwe hoofdstuk toegevoegd**: Geïntroduceerde uitgebreide gids voor geavanceerd MCP servergebruik, inclusief reguliere en low-level serverarchitecturen.
  - **Reguliere versus low-level server**: Gedetailleerde vergelijking en codevoorbeelden in Python en TypeScript voor beide methoden.
  - **Handler-gebaseerd ontwerp**: Uitleg over handler-gebaseerd beheer van tools/bronnen/prompts voor schaalbare, flexibele serverimplementaties.
  - **Praktische patronen**: Realistische scenario’s waar low-level serverpatronen nuttig zijn voor geavanceerde functies en architectuur.

#### Eenvoudige authenticatie (03-GettingStarted/11-simple-auth)
- **Nieuw hoofdstuk toegevoegd**: Stapsgewijze handleiding voor het implementeren van eenvoudige authenticatie in MCP-servers.
  - **Authenticatieconcepten**: Duidelijke uitleg over authenticatie versus autorisatie en credentialbeheer.
  - **Basisauthenticatie-implementatie**: Middleware-gebaseerde authenticatiepatronen in Python (Starlette) en TypeScript (Express), met codevoorbeelden.
  - **Vooruitgang naar geavanceerde beveiliging**: Richtlijnen om te starten met eenvoudige authenticatie en door te groeien naar OAuth 2.1 en RBAC, met verwijzingen naar geavanceerde beveiligingsmodules.

Deze aanvullingen bieden praktische, hands-on richtlijnen voor het bouwen van robuustere, veiligere en flexibelere MCP-serverimplementaties, waarbij fundamentele concepten worden verbonden met geavanceerde productiepatronen.

## 29 september 2025

### MCP Server Database Integratie Labs - Uitgebreide hands-on leertraject

#### 11-MCPServerHandsOnLabs - Nieuwe volledige database-integratie curriculum
- **Volledige leertraject van 13 labs**: Toegevoegd uitgebreid hands-on curriculum voor productieklare MCP-servers met PostgreSQL database-integratie
  - **Praktijkvoorbeeld uit de echte wereld**: Zava Retail analytics use case die enterprise-grade patronen demonstreert
  - **Gestructureerde leerprogressie**:
    - **Labs 00-03: Fundamenten** - Introductie, kernarchitectuur, beveiliging & multi-tenancy, omgeving opzetten
    - **Labs 04-06: Bouw van de MCP-server** - Databas ontwerp & schema, MCP-serverimplementatie, toolontwikkeling  
    - **Labs 07-09: Geavanceerde functies** - Semantische zoekintegratie, testen & debuggen, VS Code-integratie
    - **Labs 10-12: Productie & beste praktijken** - Deploy- strategieën, monitoring & observeerbaarheid, best practices & optimalisatie
  - **Enterprise-technologieën**: FastMCP framework, PostgreSQL met pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Geavanceerde functies**: Row Level Security (RLS), semantische zoekopdrachten, multi-tenant data toegang, vector embeddings, real-time monitoring

#### Terminologiestandaardisatie - module-naar-lab conversie
- **Uitgebreide documentatie-update**: Systematisch alle README-bestanden in 11-MCPServerHandsOnLabs aangepast om "Lab" terminologie te gebruiken in plaats van "Module"
  - **Sectiekoppen**: "Wat deze module behandelt" gewijzigd in "Wat dit lab behandelt" in alle 13 labs
  - **Inhoudsbeschrijving**: "Deze module biedt..." gewijzigd naar "Dit lab biedt..." in de documentatie
  - **Leerdoelen**: "Aan het einde van deze module..." gewijzigd naar "Aan het einde van dit lab..." 
  - **Navigatielinks**: Alle verwijzingen “Module XX:” conversie naar “Lab XX:” in kruisverwijzingen en navigatie
  - **Volgtracking**: "Na afronding van deze module..." gewijzigd in "Na afronding van dit lab..."
  - **Technische verwijzingen behouden**: Python-moduleverwijzingen in configuratiebestanden behouden (bijv. `"module": "mcp_server.main"`)

#### Studiehandleiding verbeteringen (study_guide.md)
- **Visuele curriculumkaart**: Nieuwe sectie "11. Database Integration Labs" toegevoegd met uitgebreide visualisatie van labstructuur
- **Repositorystructuur**: Bijgewerkt van tien naar elf hoofddelen met gedetailleerde 11-MCPServerHandsOnLabs beschrijving
- **Leertraadbegeleiding**: Navigatie-instructies uitgebreid om secties 00-11 te omvatten
- **Technologie-overzicht**: FastMCP, PostgreSQL, Azure services integratiedetails toegevoegd
- **Leerresultaten**: Nadruk op productieklare serverontwikkeling, database-integratiepatronen en enterprise beveiliging

#### Verbeteringen hoofd-README-structuur
- **Lab-gebaseerde terminologie**: Hoofd-README.md in 11-MCPServerHandsOnLabs bijgewerkt voor consistente “Lab” structuur
- **Leertraagorganisatie**: Duidelijke progressie van fundamentele concepten via geavanceerde implementatie tot productiedeploy
- **Focus op praktijk**: Nadruk op praktische, hands-on leren met enterprise-grade patronen en technologieën

### Verbeteringen documentatiekwaliteit en consistentie
- **Hands-on leerbenadering**: Praktische, lab-gebaseerde aanpak in de hele documentatie versterkt
- **Focus enterprise patronen**: Nadruk op productieklare implementaties en enterprisebeveiliging
- **Technologie-integratie**: Uitgebreide dekking van moderne Azure-services en AI-integratiepatronen
- **Leerprogressie**: Duidelijk, gestructureerd pad van basisconcepten tot productiedeploy

## 26 september 2025

### Case studies verbetering - GitHub MCP Registry integratie

#### Case studies (09-CaseStudy/) - Focus op ecosysteemontwikkeling
- **README.md**: Grote uitbreiding met uitgebreide case study van GitHub MCP Registry
  - **GitHub MCP Registry case study**: Nieuwe uitgebreide case study over de lancering van GitHub’s MCP Registry in september 2025
    - **Probleemanalyse**: Gedetailleerde analyse van gefragmenteerde MCP-serverontdekking en deployment-uitdagingen
    - **Oplossingsarchitectuur**: GitHub’s gecentraliseerde registratiesysteem met one-click VS Code installatie
    - **Zakelijke impact**: Meetbare verbeteringen in onboarding en productiviteit van ontwikkelaars
    - **Strategische waarde**: Focus op modulaire agentdeployment en interoperabiliteit tussen tools
    - **Ecosysteemontwikkeling**: Positionering als fundamenteel platform voor agentische integratie
  - **Verbeterde case study structuur**: Alle zeven case studies bijgewerkt met consistente opmaak en uitgebreide beschrijvingen
    - Azure AI Travel Agents: Nadruk op multi-agent orkestratie
    - Azure DevOps integratie: Focus op workflowautomatisering
    - Real-time documentatieopvraging: Implementatie Python console client
    - Interactieve studieplangenerator: Chainlit conversational webapp

    - Documentatie in de editor: VS Code en GitHub Copilot integratie
    - Azure API Management: Enterprise API integratiepatronen
    - GitHub MCP Register: Ecosysteemontwikkeling en communityplatform
  - **Uitgebreide Conclusie**: Herschreven conclusie sectie met zeven casestudy's over meerdere MCP-implementatiedimensies
    - Enterprise Integratie, Multi-Agent Orkestratie, Ontwikkelaar Productiviteit
    - Ecosysteemontwikkeling, Educatieve Toepassingen categorisatie
    - Verhoogde inzichten in architectuurpatronen, implementatiestrategieën en best practices
    - Nadruk op MCP als volwassen, productieklaar protocol

#### Studiegids Updates (study_guide.md)
- **Visuele Curriculumkaart**: Bijgewerkte mindmap om GitHub MCP Register op te nemen in sectie Casestudy's
- **Casestudybeschrijvingen**: Verbeterd van algemene beschrijvingen naar gedetailleerde uitsplitsing van zeven uitgebreide casestudy's
- **Repositorystructuur**: Bijgewerkte sectie 10 om uitgebreide casestudydekking met specifieke implementatiedetails weer te geven
- **Changelog Integratie**: Toegevoegd item van 26 september 2025 waarin GitHub MCP Register toevoeging en casestudy verbeteringen worden gedocumenteerd
- **Datumupdates**: Bijgewerkt voettekst timestamp om laatste revisie weer te geven (26 september 2025)

### Verbeteringen Documentatiekwaliteit
- **Consistentieversterking**: Gestandaardiseerde casestudyopmaak en structuur in alle zeven voorbeelden
- **Uitgebreide Dekking**: Casestudy's bestrijken nu enterprise-, ontwikkelaar productiviteits- en ecosysteemontwikkelingsscenario’s
- **Strategische Positionering**: Verhoogde focus op MCP als fundamenteel platform voor agentische systeemimplementatie
- **Bronintegratie**: Bijgewerkte aanvullende bronnen om GitHub MCP Register link op te nemen

## 15 september 2025

### Uitbreiding Geavanceerde Onderwerpen - Aangepaste Transports & Context Engineering

#### MCP Aangepaste Transports (05-AdvancedTopics/mcp-transport/) - Nieuwe Geavanceerde Implementatiegids
- **README.md**: Complete implementatiehandleiding voor aangepaste MCP transportmechanismen
  - **Azure Event Grid Transport**: Uitgebreide serverloze event-driven transportimplementatie
    - C#, TypeScript en Python voorbeelden met Azure Functions integratie
    - Event-driven architectuurpatronen voor schaalbare MCP-oplossingen
    - Webhook ontvangers en push-gebaseerde berichtverwerking
  - **Azure Event Hubs Transport**: High-throughput streaming transportimplementatie
    - Real-time streamingmogelijkheden voor lage-latentie scenario's
    - Partitioneringsstrategieën en checkpointbeheer
    - Berichtenbatching en prestatieoptimalisatie
  - **Enterprise Integratiepatronen**: Productiegereed architectuurexamples
    - Gedistribueerde MCP-verwerking over meerdere Azure Functions
    - Hybride transportarchitecturen die meerdere transporttypes combineren
    - Berichtduurzaamheid, betrouwbaarheid en foutafhandelingsstrategieën
  - **Beveiliging & Monitoring**: Azure Key Vault integratie en observability patronen
    - Managed identity authenticatie en least privilege toegang
    - Application Insights telemetrie en prestatiemonitoring
    - Circuit breakers en fouttolerantiepatronen
  - **Testframeworks**: Uitgebreide teststrategieën voor aangepaste transports
    - Unit testen met test doubles en mocking frameworks
    - Integratietesten met Azure Test Containers
    - Prestatie- en load testing overwegingen

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Opkomende AI Discpline
- **README.md**: Uitgebreide verkenning van context engineering als een opkomend vakgebied
  - **Kernprincipes**: Volledige contextsdeling, actie-besluitbewustzijn en contextvensterbeheer
  - **MCP Protocolafstemming**: Hoe MCP ontwerp context engineering uitdagingen adresseert
    - Limieten van contextvensters en progressieve laadstrategieën
    - Relevantiebepaling en dynamische contextopvraging
    - Multi-modale contextverwerking en beveiligingsoverwegingen
  - **Implementatiebenaderingen**: Single-threaded vs. multi-agent architecturen
    - Technieken voor context chunking en prioritering
    - Progressieve contextlading en compressiestrategieën
    - Gelaagde contextbenaderingen en opvragoptimalisatie
  - **Meetframework**: Opkomende metrieken voor evaluatie van contexteffectiviteit
    - Overwegingen voor inputefficiëntie, prestaties, kwaliteit en gebruikerservaring
    - Experimentele benaderingen voor contextoptimalisatie
    - Faalkenanalyse en verbeteringsmethodologieën

#### Curriculum Navigatie Updates (README.md)
- **Verbeterde Modulstructuur**: Bijgewerkte curriculumtabel om nieuwe geavanceerde onderwerpen op te nemen
  - Toegevoegd Context Engineering (5.14) en Aangepaste Transport (5.15) items
  - Consistente opmaak en navigatielinks in alle modules
  - Bijgewerkte beschrijvingen om huidige inhoudsomvang te reflecteren

### Verbeteringen Mappenstructuur
- **Naamstandaardisatie**: "mcp transport" hernoemd naar "mcp-transport" voor consistentie met andere geavanceerde onderwerpmappen
- **Inhoudsorganisatie**: Alle 05-AdvancedTopics mappen volgen nu consistente naamgevingspatroon (mcp-[onderwerp])

### Verbeteringen Documentatiekwaliteit
- **MCP Specificatieafstemming**: Alle nieuwe inhoud verwijst naar actuele MCP Specificatie 2025-06-18
- **Multitalige Voorbeelden**: Uitgebreide codevoorbeelden in C#, TypeScript en Python
- **Enterprise Focus**: Productiegereed patronen en Azure cloudintegratie doorheen
- **Visuele Documentatie**: Mermaid diagrammen voor architectuur en flowvisualisatie

## 18 augustus 2025

### Uitgebreide Documentatie-update - MCP 2025-06-18 Normen

#### MCP Beveiligingsbest Practices (02-Security/) - Complete Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Volledige herschrijving afgestemd op MCP Specificatie 2025-06-18
  - **Verplichte Vereisten**: Toegevoegd expliciete MOET/MOET NIET vereisten uit officiële specificatie met duidelijke visuele indicatoren
  - **12 Kern Beveiligingspraktijken**: Hervormd van 15-item lijst naar uitgebreide beveiligingsdomeinen
    - Tokenbeveiliging & authenticatie met externe identity provider integratie
    - Sessiebeheer & transportbeveiliging met cryptografische vereisten
    - AI-specifieke dreigingsbescherming met Microsoft Prompt Shields integratie
    - Toegangscontrole & permissies met principe van minste privilege
    - Inhoudsveiligheid & monitoring met Azure Content Safety integratie
    - Supply Chain Security met uitgebreide componentverificatie
    - OAuth-beveiliging & Confused Deputy preventie met PKCE implementatie
    - Incidentrespons & herstel met geautomatiseerde mogelijkheden
    - Compliance & governance met naleving van regelgeving
    - Geavanceerde beveiligingscontroles met zero trust architectuur
    - Microsoft Beveiligingsecosysteemintegratie met uitgebreide oplossingen
    - Continu beveiligingsevolutie met adaptieve praktijken
  - **Microsoft Beveiligingsoplossingen**: Verbeterde integratierichtlijnen voor Prompt Shields, Azure Content Safety, Entra ID en GitHub Advanced Security
  - **Implementatieresources**: Geclassificeerde uitgebreide bronnensites per Officiële MCP-documentatie, Microsoft Beveiligingsoplossingen, Beveiligingsstandaarden en Implementatiehandleidingen

#### Geavanceerde Beveiligingscontroles (02-Security/) - Enterprise Implementatie
- **MCP-SECURITY-CONTROLS-2025.md**: Volledige herziening met enterprise-grade beveiligingsraamwerk
  - **9 Uitgebreide Beveiligingsdomeinen**: Uitgebreid van basale controles naar gedetailleerd enterprise raamwerk
    - Geavanceerde authenticatie & autorisatie met Microsoft Entra ID integratie
    - Token beveiliging & anti-passthrough controles met uitgebreide validatie
    - Sessiebeveiligingscontroles met kapingpreventie
    - AI-specifieke beveiligingscontroles met preventie van prompt injectie en tool vergiftiging
    - Confused Deputy aanvalpreventie met OAuth proxy beveiliging
    - Tool uitvoeringsbeveiliging met sandboxing en isolatie
    - Supply Chain beveiligingscontroles met afhankelijkheidsverificatie
    - Monitoring & detectiecontroles met SIEM-integratie
    - Incidentrespons & herstel met geautomatiseerde mogelijkheden
  - **Implementatievoorbeelden**: Toegevoegd gedetailleerde YAML-configuratieblokken en codevoorbeelden
  - **Microsoft Oplossingsintegratie**: Uitgebreide dekking van Azure beveiligingsservices, GitHub Advanced Security en enterprise identiteitsbeheer

#### Geavanceerde Onderwerpen Beveiliging (05-AdvancedTopics/mcp-security/) - Productieklare Implementatie
- **README.md**: Volledige herschrijving voor enterprise beveiligingsimplementatie
  - **Huidige Specificatieafstemming**: Bijgewerkt naar MCP Specificatie 2025-06-18 met verplichte beveiligingsvereisten
  - **Verbeterde authenticatie**: Microsoft Entra ID integratie met uitgebreide .NET en Java Spring Security voorbeelden
  - **AI beveiligingsintegratie**: Microsoft Prompt Shields en Azure Content Safety implementatie met gedetailleerde Python voorbeelden
  - **Geavanceerde bedreigingsmitigatie**: Uitgebreide implementatievoorbeelden voor
    - Confused Deputy aanvalpreventie met PKCE en gebruikersconsentvalidatie
    - Token Passthrough Preventie met audience validatie en veilige tokenbeheer
    - Tegen sessiekaping met cryptografische binding en gedragsanalyse
  - **Enterprise beveiligingsintegratie**: Azure Application Insights monitoring, dreigingsdetectiepijplijnen en supply chain beveiliging
  - **Implementatie-checklist**: Duidelijke verplichte versus aanbevolen beveiligingscontroles met voordelen van Microsoft beveiligingsecosysteem

### Documentatiekwaliteit & Normafstemming
- **Specificatieverwijzingen**: Alle verwijzingen bijgewerkt naar actuele MCP Specificatie 2025-06-18
- **Microsoft Beveiligingsecosysteem**: Verbeterde integratierichtlijnen door alle beveiligingsdocumentatie heen
- **Praktische implementatie**: Toegevoegd gedetailleerde codevoorbeelden in .NET, Java en Python met enterprise patronen
- **Bronorganisatie**: Uitgebreide categorisering van officiële documentatie, beveiligingsstandaarden en implementatiehandleidingen
- **Visuele indicatoren**: Duidelijke markering van verplichte vereisten versus aanbevolen praktijken


#### Kernconcepten (01-CoreConcepts/) - Volledige Modernisering
- **Protocolversie-update**: Bijgewerkt om te verwijzen naar actuele MCP Specificatie 2025-06-18 met datumgebaseerde versie (YYYY-MM-DD formaat)
- **Architectuurverfijning**: Verbeterde beschrijvingen van Hosts, Clients en Servers om huidige MCP architectuurpatronen te reflecteren
  - Hosts nu duidelijk gedefinieerd als AI-applicaties die meerdere MCP-clientverbindingen coördineren
  - Clients beschreven als protocolconnectoren die één-op-één serverrelaties onderhouden
  - Servers verbeterd met lokale versus externe implementatiescenario's
- **Primitief herstructurering**: Volledige herziening van server- en clientprimitieven
  - Serverprimitieven: Resources (gegevensbronnen), Prompts (sjablonen), Tools (uitvoerbare functies) met gedetailleerde uitleg en voorbeelden
  - Clientprimitieven: Sampling (LLM completions), Elicitation (gebruikersinput), Logging (debugging/monitoring)
  - Bijgewerkt met actuele discover (`*/list`), retrieval (`*/get`) en execution (`*/call`) methodpatronen
- **Protocolarchitectuur**: Geïntroduceerd tweelaags architectuurmodel
  - Datalayer: JSON-RPC 2.0 fundament met lifecycle management en primitieven
  - Transportlaag: STDIO (lokaal) en Streamable HTTP met SSE (remote) transportmechanismen
- **Beveiligingsraamwerk**: Uitgebreide beveiligingsprincipes inclusief expliciete gebruikersconsent, gegevensprivacybescherming, veilig draaien van tools en transportlaagnaar beveiliging
- **Communicatiepatronen**: Bijgewerkte protocolberichten om initialisatie, ontdekking, uitvoering en notificatie flows weer te geven
- **Codevoorbeelden**: Vernieuwde multitalige voorbeelden (.NET, Java, Python, JavaScript) om actuele MCP SDK-patronen te weerspiegelen

#### Beveiliging (02-Security/) - Uitgebreide Beveiligingsherziening  
- **Normafstemming**: Volledige afstemming op MCP Specificatie 2025-06-18 beveiligingseisen
- **Authenticatie Evolutie**: Gedocumenteerde evolutie van aangepaste OAuth-servers naar delegatie via externe identity provider (Microsoft Entra ID)
- **AI-specifieke dreigingsanalyse**: Versterkte dekking van moderne AI-aanvalsvectoren
  - Gedetailleerde promptinjectie aanvalscenario's met praktijkvoorbeelden
  - Mechanismen voor toolvergiftiging en "rug pull" aanvalpatronen
  - Contextvenstervergiftiging en modelverwarring aanvallen
- **Microsoft AI Beveiligingsoplossingen**: Uitgebreide dekking van Microsoft beveiligingsecosysteem
  - AI Prompt Shields met geavanceerde detectie, spotlighting en delimitertechnieken
  - Azure Content Safety integratiepatronen
  - GitHub Advanced Security voor bescherming van supply chain
- **Geavanceerde bedreigingsmitigatie**: Gedetailleerde beveiligingscontroles voor
  - Sessiekaping met MCP-specifieke aanvalscenario's en cryptografische sessie-ID vereisten
  - Confused deputy problemen in MCP proxyscenario's met expliciete consentvereisten
  - Token passthrough kwetsbaarheden met verplichte validatiecontroles
- **Supply Chain Security**: Uitgebreide AI supply chain dekking inclusief foundation modellen, embeddingdiensten, contextproviders en externe API's
- **Foundation Security**: Verbeterde integratie met enterprise beveiligingspatronen inclusief zero trust architectuur en Microsoft beveiligingsecosysteem
- **Bronorganisatie**: Geclassificeerde uitgebreide bronnensites per type (Officiële Docs, Standaarden, Onderzoek, Microsoft Oplossingen, Implementatiehandleidingen)

### Verbeteringen Documentatiekwaliteit
- **Gestructureerde Leerdoelen**: Verbeterde leerdoelen met specifieke, uitvoerbare resultaten 
- **Kruisverwijzingen**: Toegevoegd links tussen gerelateerde beveiligings- en kernconceptonderwerpen
- **Actuele informatie**: Alle datumverwijzingen en specificatielinks geüpdatet naar huidige standaarden
- **Implementatierichtlijnen**: Toegevoegd specifieke, uitvoerbare implementatierichtlijnen door beide secties heen

## 16 juli 2025

### README en Navigatieverbeteringen
- Volledig opnieuw ontworpen curriculum navigatie in README.md
- `<details>` tags vervangen door toegankelijker op tabel gebaseerde layout
- Alternatieve lay-outopties aangemaakt in nieuwe map "alternative_layouts"
- Toegevoegd kaartgebaseerde, tabstijl en accordeonstijl navigatievoorbeelden
- Bijgewerkte repositorystructuur sectie om alle nieuwste bestanden op te nemen
- Verbeterde sectie "Hoe dit curriculum te gebruiken" met duidelijke aanbevelingen
- Bijgewerkte MCP specificatielinks om naar correcte URL's te wijzen
- Toegevoegd Context Engineering sectie (5.14) aan curriculumstructuur

### Studiegids Updates
- Volledig herzien studiegids om aan te sluiten bij huidige repositorystructuur
- Toegevoegd nieuwe secties voor MCP Clients en Tools, en Populaire MCP Servers
- Bijgewerkte Visuele Curriculumkaart om alle onderwerpen accuraat te reflecteren
- Verbeterde beschrijvingen van Geavanceerde Onderwerpen om alle gespecialiseerde gebieden te dekken
- Bijgewerkte Casestudies sectie om daadwerkelijke voorbeelden te weerspiegelen
- Toegevoegd deze uitgebreide changelog

### Communitybijdragen (06-CommunityContributions/)
- Toegevoegde gedetailleerde informatie over MCP-servers voor beeldgeneratie
- Toegevoegde uitgebreide sectie over gebruik van Claude in VSCode
- Toegevoegde Cline terminal client setup en gebruiksinstructies
- Bijgewerkte MCP client sectie om alle populaire clientopties op te nemen
- Verbeterde bijdragevoorbeelden met accuratere codevoorbeelden

### Geavanceerde Onderwerpen (05-AdvancedTopics/)
- Georganiseerde alle gespecialiseerde onderwerpmappen met consistente naamgeving
- Toegevoegd context engineering materiaal en voorbeelden
- Toegevoegd Foundry agent integratiedocumentatie
- Verbeterde Entra ID beveiligingsintegratiedocumentatie

## 11 juni 2025

### Eerste Creatie
- Eerste versie uitgebracht van het MCP voor Beginners curriculum

- Basisstructuur gemaakt voor alle 10 hoofdsecties
- Visuele curriculumkaart geïmplementeerd voor navigatie
- Initiële voorbeeldprojecten toegevoegd in meerdere programmeertalen

### Aan de slag (03-GettingStarted/)
- Eerste serverimplementatievoorbeelden gemaakt
- Richtlijnen voor clientontwikkeling toegevoegd
- Instructies voor LLM-clientintegratie opgenomen
- Documentatie voor VS Code-integratie toegevoegd
- Server-Sent Events (SSE) servervoorbeelden geïmplementeerd

### Kernconcepten (01-CoreConcepts/)
- Gedetailleerde uitleg over client-serverarchitectuur toegevoegd
- Documentatie gemaakt over belangrijke protocolcomponenten
- Messagingpatronen in MCP gedocumenteerd

## 23 mei 2025

### Repositoriestructuur
- Repository geïnitieerd met basis mappenstructuur
- README-bestanden gemaakt voor elke hoofdsectie
- Vertaalinfrastructuur opgezet
- Beeldmateriaal en diagrammen toegevoegd

### Documentatie
- Initiële README.md met overzicht van het curriculum gemaakt
- CODE_OF_CONDUCT.md en SECURITY.md toegevoegd
- SUPPORT.md opgezet met richtlijnen voor hulp
- Voorlopige structuur studiehandleiding gemaakt

## 15 april 2025

### Planning en raamwerk
- Eerste planning voor MCP voor Beginners curriculum
- Leerdoelen en doelgroep vastgesteld
- Structuur van 10 secties van het curriculum geschetst
- Conceptueel raamwerk ontwikkeld voor voorbeelden en casestudy’s
- Eerste prototypevoorbeelden voor kernconcepten gemaakt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
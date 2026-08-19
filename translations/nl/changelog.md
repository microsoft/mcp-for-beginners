# Wijzigingslogboek: MCP voor Beginners Curriculum

Dit document dient als een overzicht van alle belangrijke wijzigingen die zijn aangebracht in het Model Context Protocol (MCP) voor Beginners curriculum. Wijzigingen worden in omgekeerde chronologische volgorde gedocumenteerd (nieuwste wijzigingen eerst).

## 29 juli 2026

### Nieuwe Module 08 Companion: Betrouwbaarheid Sidecars en Veilige Herhalingen

Toegevoegd een leverancier-neutrale begeleidende les voor MCP-tools die echte
effecten creëren, afgestemd op de definitieve specificatie van `2026-07-28`.

- **Nieuw**: De [betrouwbaarheid sidecar begeleidende les][reliability-sidecar]
  gebruikt één support-ticket verhaal, twee Mermaid diagrammen, en een retry-beslissings-
  stroom om stabiele bedieningssleutels, atomaire dubbele toelating,
  reconciliatie, bewijs, en de Tasks-uitbreidingsgrens uit te leggen.
- **Nieuw**: Een standaardbibliotheek Python en SQLite foutinjectie-oefening
  gebruikt gescheiden operatie- en ticketopslagplaatsen om een verloren antwoord 
  na een gecommitte externe effect te demonstreren. Zes deterministische tests
  omvatten naïeve duplicatie, beschermde herstartsituatie, payload conflicten,
  gecachte resultaten, actieve claims, en gelijktijdige dubbele toelating.
- **Bijgewerkt**: Module 08 linkt nu de begeleidende les, identificeert het
  definitieve `2026-07-28` stateless request model, onderscheidt OpenTelemetry
  observatie van de verouderde MCP logging-functie, en beperkt het
  generieke retry-voorbeeld tot alleen-lezen operaties.
- **Optioneel**: De les koppelt haar draagbare concepten aan één getagde community-
  implementatie zonder de gehoste service of een netwerkoproep te maken tot een
  onderdeel van de oefening.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 juli 2026

### Nieuwe Les: De 2026-07-28 MCP Specificatie Release Candidate

Toegevoegd dekking van de aankomende `2026-07-28` MCP specificatie release candidate (aangekondigd 21 mei 2026; definitieve release gepland op 28 juli 2026), samengevat uit de [officiële aankondigingsblog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). De basis van het curriculum blijft **MCP Specificatie 2025-11-25** tot de nieuwe versie wordt uitgebracht, dus dit wordt gepresenteerd als vooruitkijkende richtlijnen in plaats van een herschrijving van bestaande lessen.

- **Nieuw**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — een volledige les over de stateless protocol kern (verwijdering van de `initialize` handshake en `Mcp-Session-Id`), de nieuwe `Mcp-Method`/`Mcp-Name` routeringsheaders, `ttlMs`/`cacheScope` cache metadata, W3C Trace Context in `_meta`, het formele Extensions framework (MCP Apps en de nieuwe Tasks extensie), zes autorisatie-versterkende SEPs, het uitfaseren van Roots/Sampling/Logging, en de overstap naar volledige JSON Schema 2020-12 voor tool schema's.
- **Bijgewerkt** met vooruitkijkende verwijzingen naar de nieuwe les:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): notitie over protocolversie, secties Sampling/Roots/Logging/Tasks, en "Wat staat er te gebeuren"
  - [02-Security/README.md](./02-Security/README.md): autorisatie-versterking verwijzing
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport verwijzing
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling afbouw verwijzing
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging uitfasering en Tasks extensie verwijzing
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routeringsverwijzing
  - [README.md](./README.md): "Vooruitkijken" notitie in de specificatiesectie en een nieuwe `1.1` vermelding in de module tabel van het curriculum
  - [study_guide.md](./study_guide.md): vooruitkijkend punt onder de overzicht van Core Concepts en een gedateerde aanvullingsnotitie
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): verwijzing over de `mcp-session-id` transportmap voorafgaand aan het stateless request model
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): moduleoverzicht verwijzing naar Root Contexts/Sampling afbouw en de Tasks extensie
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): autorisatie-versterking verwijzing

## 24 juni 2026

### Nieuwe Les: MCP gebruiken in Copilot-app

- [Tooling sectie](./12-tooling/README.md) Toegevoegd tooling sectie.
- [MCP in Copilot-app](./12-tooling/01-copilot-app/README.md)

## 16 juni 2026

### MCP Specificatie Afstemming & Voorbeeld Validatie

Gevalideerd het curriculum tegen de huidige **MCP Specificatie 2025-11-25** en de nieuwste officiële SDK’s, daarna de resterende verouderde specificatieverwijzingen gecorrigeerd en bevestigd dat de kernvoorbeelden nog steeds bouwen en draaien.

#### Specificatie Versie Correcties (2025-06-18 / 2025-03-26 → 2025-11-25)

Bijgewerkte Engelse inhoud waar het nog beweerde dat een oudere specificatieversie de *huidige/laatste* standaard was, en links opnieuw gericht op de canonieke `modelcontextprotocol.io` specificatiepaden:
- **05-AdvancedTopics/mcp-security/README.md**: Bijgewerkt de banner "Huidige Standaard", introductie, kernbeveiligingsprincipes kop, verplichte vereisten kop, Microsoft Entra ID sectie, Referenties & Bronnen links, en afsluitende beveiligingswaarschuwing (8 referenties) naar 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Bijgewerkt de extra bronnen specificatielink en de "Huidige Standaard" banner naar 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Vervangen de verouderde `2025-03-26` beveiliging-en-vertrouwenslink door de huidige beveiligingspraktijkpagina van 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Bijgewerkt de officiële sampling-docs link naar 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Bijgewerkt de tegenwoordige "huidige MCP-specificatie" verwijzing en extra bronnen specificatielink naar 2025-11-25 (historische SSE-afbouwnotities intact gelaten voor nauwkeurigheid)

#### Voorbeeldvalidatie tegen Huidige SDK’s

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` loste `@modelcontextprotocol/sdk@1.29.0` op; `tsc --noEmit` geslaagd zonder typefouten — bestaande `McpServer`/`StdioServerTransport` API’s blijven geldig
- **Python (03-GettingStarted/01-first-server/solution/python)**: Gevalideerd in een geïsoleerde `.venv` met `mcp[cli]` (1.27.2); `py_compile` geslaagd en `FastMCP.list_tools()` gaf correct de `add` en `subtract` tools terug
- Bevestigd dat alle voorbeeld `@modelcontextprotocol/sdk` versiebereiken (`>=1.26.0` / `^1.26.0` / `^1.27.0`) schoon oplossen naar de huidige `1.29.0` zonder brekende API-wijzigingen

#### Afstemming Dependency Pin (versiekloven dichten)

Verhoogde verouderde SDK-pins zodat elke voorbeeld de huidige MCP-release volgt, vergelijkbaar met de repo-brede conventie:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Verhoogd `@modelcontextprotocol/sdk` van `^1.8.0` → `>=1.26.0` en bijgewerkt de verouderde `"updated for MCP 2025-06-18"` pakketomschrijving naar `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** en **lab4/code/github_mcp_server/pyproject.toml**: Verhoogd exacte pin `mcp==1.23.0` → `mcp>=1.26.0`; beide `uv.lock` bestanden opnieuw gegenereerd (`uv lock`) zodat de lockfiles oplossen naar de huidige `mcp 1.27.2` en synchroon blijven met de manifests

#### Analyse van Leerplankloof — Laatste Specificatiefunctie Dekking

Bevestigd dat het curriculum al alle primitieve elementen bevat die geïntroduceerd/uitgebreid zijn in MCP 2025-11-25, dus geen inhoudskloven blijven bestaan:
- **Sampling**: Les 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. URL-modus)**: Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Gedocumenteerd in 00-Introduction, 01-CoreConcepts, en 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimenteel, langlopende operaties)**: Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotaties** (`readOnlyHint` / `destructiveHint`): Gedocumenteerd in 01-CoreConcepts en 05-AdvancedTopics/mcp-protocol-features

### Beveiligingsversterking & Herstel van Afhankelijkheidskwetsbaarheden

Een volledige beveiligingscheck uitgevoerd over elk afhankelijkheidsmanifest en voorbeeldbroncode, vervolgens alle gerapporteerde npm-adviezen en één beveiligingsvondst op code-niveau opgelost. Na herstel meldt `npm audit` **0 kwetsbaarheden** in elk gecontroleerd map.

#### npm Dependency Kwetsbaarheden (transitief) — Opgelost

Alle 15 ingediende `package-lock.json` bestanden gecontroleerd. Kwetsbaarheden waren beperkt tot transitieve afhankelijkheden geïmporteerd door de MCP Inspector ontwikkelaarstool, de OpenAI client, en de MCP SDK; deze zijn nu allemaal opgelost zonder dat de voorbeelden breken:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** en **lab3/code/weather_mcp/inspector**: Verhoogd `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), wat de advisories voor de meegeleverde `ajv`, `brace-expansion`, `diff`, `path-to-regexp` en `ws` opruimde. Toegevoegd een npm `overrides` vermelding die de gepatchte `shell-quote@1.8.4` afdwingt om de resterende kritieke advisory van `concurrently` te elimineren; beide lockfiles opnieuw gegenereerd (nu 0 kwetsbaarheden)
- **03-GettingStarted/samples/typescript**: `npm audit fix` bijgewerkt de transitieve `qs` (matig) naar een gepatchte release
- **03-GettingStarted/samples/javascript**: `npm audit fix` bijgewerkt de transitieve `hono` (matig) naar een gepatchte release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` bijgewerkt de transitieve `form-data` (hoog) naar een gepatchte release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Gegeneerd het ontbrekende `package-lock.json` zodat het project reproduceerbaar en controleerbaar is (0 kwetsbaarheden)

#### Beveiligingsfix op Codniveau (OWASP A03: Injectie)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Verwijderd `shell=True` uit de `open_in_vscode` tool. De eerdere `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` stond shell-meta-tekens in een folderpad toe om geïnterpreteerd te worden door `cmd.exe` (command-injectie vector). Het start nu direct het opgeloste `Code.exe` met de folder als argument — geen shell — wat functioneel equivalent en veilig is

#### Python Dependency Audit

- Elke Python requirements-set gecontroleerd met `pip-audit`. `05-AdvancedTopics` en `03-GettingStarted/samples/python` meldden **geen bekende kwetsbaarheden** (hun `mcp` / `httpx` / `pydantic` / `python-dotenv` bereiken lossen op naar huidige gepatchte versies)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` wees op de transitieve afhankelijkheid **`werkzeug` 3.1.1** met drie `safe_join` Windows apparaatnaam DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, en `CVE-2026-27199` (alle opgelost in 3.1.6). Toegevoegd een expliciete beveiligingspin `werkzeug>=3.1.6` zodat de gepatchte release wordt opgelost; bevestigd dat de beperking schoon oplost met de `chainlit` / `mcp` / `semantic-kernel` stack

### Productnaam Herpositionering

Alle curriculuminhoud bijgewerkt om de productherpositionering van Microsoft weer te geven:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Bijgewerkte Discord communitylink

- **AGENTS.md**: Bijgewerkte Discord-serververwijzing
- **README.md**: Bijgewerkte verwijzingen naar technologisch ecosysteem
- **study_guide.md**: Bijgewerkte verwijzingen naar casestudy's
- **05-AdvancedTopics/README.md**: Bijgewerkte titel en beschrijving van Module 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Bijgewerkte sectiekop en beschrijving
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Volledige update van moduletitel en inhoud
- **05-AdvancedTopics/mcp-security-entra/README.md**: Bijgewerkte kruisverwijzingslink
- **07-LessonsfromEarlyAdoption/README.md**: Bijgewerkte verwijzingen naar casestudy's
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Bijgewerkte sectie 9 kop, badges en mogelijkheden
- **08-BestPractices/README.md**: Bijgewerkte Discord-communitylink
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Bijgewerkte verwijzing naar Discord-kanaal
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Bijgewerkte verwijzing naar modelimplementatie
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Bijgewerkte AI Services-tabel
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Bijgewerkte verwijzingen naar bronnen

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension voor VS Code
- **README.md**: Bijgewerkte hoofd curriculum verwijzingen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Bijgewerkte modultitel, overzicht en alle modulehoofdstukken
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Bijgewerkte titel, leerdoelen, installatie-instructies en bronnen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Bijgewerkte titel, leerdoelen, MCP-host-tabel en kruisverwijzingen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Bijgewerkte titel, badges, vereisten en bronnen
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Bijgewerkte Agent Builder-verwijzingen en feedbacklink
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Bijgewerkte vereisten en extensieverwijzingen

---

## 11 april 2026

### Nieuwe les, documentatiefouten opgelost en afhankelijkheidsupdates

#### Nieuwe curriculuminhoud toegevoegd

**Module 05 - Geavanceerde onderwerpen**
- **Les 5.17: Adversarial Multi-Agent Reasoning met MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nieuwe uitgebreide gids over het adversarial debatpatroon voor multi-agent-systemen
  - Mermaid architectuurdiagram: twee agenten → gedeelde MCP-server → debattranscript → rechter → oordeel
  - Gedeelde MCP tool-server (`web_search` + `run_python`) geïmplementeerd in Python en TypeScript
  - Tegenwerkende systeem prompts (VOOR / TEGEN / Rechter) met expliciete toolgebruikvereisten
  - Debatregisseur in Python, TypeScript en C# die rondes beheert en argumenten routeren
  - MCP `ClientSession`-koppeling voor de regisseur naar echte toolaanroepen
  - Use-case tabel (illusiedetectie, bedreigingsmodellering, API-ontwerpreview, feitelijke verificatie, technologische selectie)
  - Beveiligingsoverwegingen: sandboxed uitvoering, tool-aanroep validatie, rate limiting, audit logging
  - Gestructureerde oefening met drie praktische scenario's (code review, architectuurbeslissing, inhoudmoderatie)

#### Documentatiefouten opgelost

**Module 03 - Aan de slag**
- **05-stdio-server/README.md**: Verbeterd onvolledig TypeScript stdio-servervoorbeeld — toegevoegde ontbrekende transportinstantiering (`new StdioServerTransport()`) en `server.connect(transport)` oproep om overeen te komen met Python en .NET voorbeelden in dezelfde sectie
- **14-sampling/README.md**: Typfout gecorrigeerd — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculumupdates

**Hoofd README.md**
- Toegevoegd item 5.17 (Adversarial Multi-Agent Reasoning met MCP) aan de curriculumtabel met directe link naar de nieuwe les

**05-AdvancedTopics/README.md**
- Toegevoegd les 5.17 regel aan de lessentabel

**study_guide.md**
- Toegevoegd onderwerp Adversarial Multi-Agent Reasoning aan de mindmap en prozabeschrijving van Geavanceerde Onderwerpen

#### Code- en beveiligingsoplossingen

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Beveiligingsfix — commandoinjectie**: Vervangen van `execSync` shell interpolatie door `execFile` + `promisify` in het TypeScript `run_python`-tool, waardoor de commandoinjectie-oppervlakte wordt geëlimineerd (LLM-gestuurde code wordt nu als letterlijke argv-element doorgegeven zonder shell-betrokkenheid)
- **MCP tool loop koppeling**: Bijgewerkt Python debatregisseur om `AsyncAnthropic` client te gebruiken (ter vervanging van blokkerende sync `Anthropic`), een live `ClientSession` direct doorgeven aan elke agentbeurt, tooldefinities per beurt ophalen via `session.list_tools()`, en `tool_use`-blokken uitsturen via `session.call_tool()` in een lus totdat het model een finale tekstreactie genereert

#### Afhankelijkheidsupdates

- Hernoemd `hono` naar 4.12.12 in meerdere pakketten (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Hernoemd `@hono/node-server` van 1.19.11 naar 1.19.13 in TypeScript pakketten
- Hernoemd `cryptography` van 46.0.5 naar 46.0.7 in Python-pakketten (10-StreamliningAIWorkflows labs 3 en 4)
- Hernoemd `lodash` van 4.17.23 naar 4.18.1 in 10-StreamliningAIWorkflows inspector

#### Vertalingen

- Gesynchroniseerde vertalingen voor 48+ talen met de nieuwste bronwijzigingen (i18n-update)

---

## 5 februari 2026

### Repositorium-brede validatie en navigatieverbeteringen

#### Nieuwe curriculuminhoud toegevoegd

**Module 03 - Aan de slag**
- **12-mcp-hosts/README.md**: Nieuwe uitgebreide gids voor het instellen van MCP-hosts
  - Configuratievoorbeelden voor Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-configuratiesjablonen voor alle belangrijke hosts
  - Vergelijkingstabel van transporttypes (stdio, SSE/HTTP, WebSocket)
  - Veelvoorkomende verbindingsproblemen oplossen
  - Beveiligingsbest practices voor hostconfiguratie

- **13-mcp-inspector/README.md**: Nieuwe debugginggids voor MCP Inspector
  - Installatiemethoden (npx, npm globaal, uit bron)
  - Verbinden met servers via stdio en HTTP/SSE
  - Testtools, bronnen en promptworkflows
  - VS Code-integratie met MCP Inspector
  - Veelvoorkomende debugscenario's met oplossingen

**Module 04 - Praktische Implementatie**
- **pagination/README.md**: Nieuwe gids voor pagineringimplementatie
  - Cursor-gebaseerde pagineringspatronen in Python, TypeScript, Java
  - Client-side pagineringsafhandeling
  - Cursorontwerpstrategieën (opaque vs. gestructureerd)
  - Aanbevelingen voor prestatieoptimalisatie

**Module 05 - Geavanceerde onderwerpen**
- **mcp-protocol-features/README.md**: Nieuwe diepgaande uitleg van protocolkenmerken
  - Implementatie van voortgangsnotificaties
  - Patronen voor annulering van verzoeken
  - Bronsjablonen met URI-patronen
  - Server levenscyclusbeheer
  - Beheersing van logniveau
  - Foutafhandelingspatronen met JSON-RPC-codes

#### Navigatiefixes (24+ bestanden bijgewerkt)

**Hoofdmodule README's**
 Nu links naar zowel eerste les ALS volgende module

**02-Beveiliging subbestanden**
- Alle 5 aanvullende beveiligingsdocumenten hebben nu "Wat Nu" navigatie:

**09-CaseStudy-bestanden**
- Alle casestudy-bestanden hebben nu sequentiële navigatie:

**10-StreamliningAI Labs**
Toegevoegd sectie Wat Nu aan Module 10 overzicht en Module 11

#### Code- en inhoudsreparaties

**SDK- en afhankelijkheidsupdates**
Lege openai-versie aangepast naar `^4.95.0`
SDK bijgewerkt van `^1.8.0` naar `>=1.26.0`
MCP versie-pins bijgewerkt naar `>=1.26.0`

**Code fixes**
Ongeldig model `gpt-4o-mini` gecorrigeerd naar `gpt-4.1-mini`

**Inhoud fixes**
Gebroken link `READMEmd` → `README.md` gerepareerd, curriculumkop `Module 1-3` → `Module 0-3` aangepast, hoofdlettergevoelige pad gecorrigeerd
Gecorrumpeerde dubbele Case Study 5-inhoud verwijderd

**Verbeteringen voor beginners**
Juiste introductie, leerdoelen en vereisten voor beginners toegevoegd

#### Curriculumupdates

**Hoofd README.md**
- Toegevoegd items 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protocolkenmerken) aan curriculumtabel

**Module README's**
Toegevoegd lessen 12 en 13 aan leslijst
Toegevoegd sectie Praktische Gidsen met pagineringslink
Toegevoegd lessen 5.15 (Aangepast Transport) en 5.16 (Protocolkenmerken)

**study_guide.md**
- Mindmap bijgewerkt met alle nieuwe onderwerpen: MCP Hosts Setup, MCP Inspector, Pagineringstrategieën, Deep Dive in Protocolkenmerken

## 28 januari 2026

### MCP Specificatie 2025-11-25 Compliance Review

#### Verbetering kernconcepten (01-CoreConcepts/)
- **Nieuwe Client Primitive - Roots**: Uitgebreide documentatie toegevoegd over de Roots client primitive, waarmee servers bestandssysteemgrenzen en toegangsrechten kunnen begrijpen
- **Toolannotaties**: Documentatie toegevoegd over toolgedragsannotaties (`readOnlyHint`, `destructiveHint`) voor betere beslissingen bij uitvoering van tools
- **Toolaanroepen in Sampling**: Samplingdocumentatie geüpdatet om `tools` en `toolChoice` parameters op te nemen voor modelgestuurde toolaanroep tijdens sampling verzoeken
- **URL Mode Elicitation**: Documentatie toegevoegd over URL-gebaseerde elicitaties voor server-geïnitieerde externe webinteracties
- **Taken (Experimenteel)**: Nieuwe sectie toegevoegd die de experimentele Taken-functie documenteert voor duurzame uitvoeringsomslagen en uitgestelde resultaatretrieval
- **Pictogrammenondersteuning**: Opgemerkt dat tools, bronnen, bronsjablonen en prompts nu pictogrammen kunnen bevatten als aanvullende metadata

#### Documentatie-updates
- **README.md**: MCP Specificatie 2025-11-25 versie verwijzing en op datum gebaseerde versionering toegevoegd
- **study_guide.md**: Curriculumkaart bijgewerkt om Taken en Toolannotaties op te nemen in de kernconceptensectie; documenttijdstempel bijgewerkt

#### Specificatiecompliance verificatie
- **Protocolversie**: Gecontroleerd dat alle documentatie verwijst naar de actuele MCP Specificatie 2025-11-25
- **Architectuuraansluiting**: Bevestigd nauwkeurigheid van tweelaagse architectuur (Data Layer + Transport Layer) documentatie
- **Documentatie van primitieve functies**: Serverprimitieven (Bronnen, Prompts, Tools) en clientprimitieven (Sampling, Elicitation, Logging, Roots) gevalideerd
- **Transportmechanismen**: STDIO en Streamable HTTP transportdocumentatie geverifieerd
- **Beveiligingsrichtlijnen**: Bevestigde afstemming op huidige MCP Security Best Practices documentatie

#### Belangrijkste MCP 2025-11-25 functies gedocumenteerd
- **OpenID Connect Discovery**: Authenticatieserver discovery via OIDC
- **OAuth Client ID Metadata Documenten**: Aanbevolen clientregistratiemechanisme
- **JSON Schema 2020-12**: Standaarddialect voor MCP schema-definities
- **SDK Tiering-systeem**: Geformaliseerde vereisten voor SDK-functionaliteitsupport en onderhoud
- **Governancestructuur**: Geformaliseerde werkgroepen en interessegroepen in MCP-governance

### Grote update van beveiligingsdocumentatie (02-Security/)

#### Integratie MCP Security Summit Workshop (Sherpa)
- **Nieuwe hands-on trainingsbron**: Uitgebreide integratie toegevoegd met de [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) in alle beveiligingsdocumentatie
- **Route van expeditie gedocumenteerd**: Volledige progres van kamp tot kamp van Base Camp tot Summit beschreven
- **OWASP afstemming**: Alle beveiligingsrichtlijnen nu gemapt aan OWASP MCP Azure Security Guide risico's

#### OWASP MCP Top 10 integratie
- **Nieuwe sectie**: Toegevoegd OWASP MCP Top 10 beveiligingsrisicotabel met Azure-mitigaties aan hoofdbeveiligings-README
- **Risicogebaseerde documentatie**: Bijgewerkt mcp-security-controls-2025.md met OWASP MCP risicoverwijzingen voor elk beveiligingsdomein
- **Referentiearchitectuur**: Gelinked aan OWASP MCP Azure Security Guide referentiearchitectuur en implementatiepatronen

#### Bijgewerkte beveiligingsbestanden
- **README.md**: Overzicht Sherpa Workshop, expeditiesentabel, OWASP MCP Top 10 risicosamenvatting en sectie hands-on training toegevoegd
- **mcp-security-controls-2025.md**: Header bijgewerkt naar februari 2026, OWASP-risicoverwijzingen (MCP01-MCP08) toegevoegd, specificatieversie-inconsistentie opgelost
- **mcp-security-best-practices-2025.md**: Sectie Sherpa en OWASP bronnen toegevoegd, tijdstempel bijgewerkt
- **mcp-best-practices.md**: Hands-on trainingssectie toegevoegd met Sherpa- en OWASP-links
- **azure-content-safety-implementation.md**: OWASP MCP06 verwijzing toegevoegd, Sherpa Kamp 3 afstemming en sectie aanvullende bronnen toegevoegd

#### Nieuwe bronnenlinks toegevoegd
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuele OWASP MCP risicopagina's (MCP01-MCP10)

### Curriculum-brede MCP-specificatie 2025-11-25 Afstemming

#### Module 03 - Aan de slag
- **SDK Documentatie**: Toegevoegd Go SDK aan officiële SDK-lijst; alle SDK-verwijzingen bijgewerkt ter afstemming op MCP-specificatie 2025-11-25
- **Transportverduidelijking**: Bijgewerkte beschrijvingen van STDIO- en HTTP-streamingtransport met expliciete specificatieverwijzingen

#### Module 04 - Praktische Implementatie
- **SDK Updates**: Toegevoegd Go SDK; SDK-lijst bijgewerkt met specificatieversieversie
- **Autorisatie Specificatie**: Verwijzing naar MCP-autorisatiespecificatie bijgewerkt naar huidige versie 2025-11-25

#### Module 05 - Gevorderde Onderwerpen
- **Nieuwe Functies**: Opmerking toegevoegd over nieuwe MCP-specificatie 2025-11-25 functies (Taken, Toolannotaties, URL-modus Elicitatie, Wortels)
- **Beveiligingsbronnen**: Toegevoegd OWASP MCP Top 10 en Sherpa-workshop links aan aanvullende referenties

#### Module 06 - Gemeenschapsbijdragen
- **SDK-lijst**: Toegevoegd Swift en Rust SDK's; specificatieverwijzing bijgewerkt naar 2025-11-25
- **Specificatieverwijzing**: Verwijzing naar MCP-specificatie bijgewerkt naar directe specificatie-URL

#### Module 07 - Lessen van vroege adoptie
- **Bronupdates**: Toegevoegd MCP-specificatie 2025-11-25 link en OWASP MCP Top 10 aan aanvullende bronnen

#### Module 08 - Beste praktijken
- **Spec-versie**: MCP-specificatieverwijzing bijgewerkt naar 2025-11-25
- **Beveiligingsbronnen**: Toegevoegd OWASP MCP Top 10 en Sherpa-workshop aan aanvullende referenties

#### Module 10 - Stroomlijnen van AI-werkstromen
- **Badge Update**: MCP-versiebadge gewijzigd van SDK-versie (1.9.3) naar specificatieversie (2025-11-25)
- **Bronverwijzingen**: MCP-specificatielink bijgewerkt; toegevoegd OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec-verwijzing**: MCP-specificatie link bijgewerkt naar versie 2025-11-25
- **Beveiligingsbronnen**: Toegevoegd OWASP MCP Top 10 aan officiële bronnen

## 18 december 2025

### Beveiligingsdocumentatie-update - MCP-specificatie 2025-11-25

#### MCP Beveiligingsbeste praktijken (02-Security/mcp-best-practices.md) - Specificatieversie-update
- **Protocolversie-update**: Bijgewerkt naar verwijzing naar nieuwste MCP-specificatie 2025-11-25 (uitgebracht 25 november 2025)
  - Alle specificatieversieverwijzingen aangepast van 2025-06-18 naar 2025-11-25
  - Documentdatumverwijzingen bijgewerkt van 18 augustus 2025 naar 18 december 2025
  - Alle specificatie-URL's geverifieerd en wijzen naar actuele documentatie
- **Inhoudsvalidatie**: Uitgebreide validatie van beveiligingsbeste praktijken tegen nieuwste standaarden
  - **Microsoft Security Solutions**: Huidige terminologie en links gecontroleerd voor Prompt Shields (voorheen "Jailbreak risicodetectie"), Azure Content Safety, Microsoft Entra ID en Azure Key Vault
  - **OAuth 2.1 Beveiliging**: Bevestigde afstemming met nieuwste OAuth beveiligingspraktijken
  - **OWASP Standaarden**: Bevestigde dat verwijzingen naar OWASP Top 10 voor LLM's actueel blijven
  - **Azure Services**: Alle Microsoft Azure documentatielinks en beste praktijken geverifieerd
- **Standaardafstemming**: Alle vermelde beveiligingsnormen bevestigd actueel
  - NIST AI Risicobeheer Framework
  - ISO 27001:2022
  - OAuth 2.1 Beveiligingsbeste praktijken
  - Azure beveiligings- en compliance-frameworks
- **Implementatiebronnen**: Alle implementatiegidslinks en bronnen geverifieerd
  - Azure API Management authenticatiepatronen
  - Microsoft Entra ID integratiehandleidingen
  - Azure Key Vault geheimbeheer
  - DevSecOps pipelines en monitoring oplossingen

### Documentatie Kwaliteitsborging
- **Specificatieconformiteit**: Alle verplichte MCP beveiligingseisen (MOET/MAG NIET) afgestemd op laatste specificatie
- **Bronactualiteit**: Alle externe links naar Microsoft-documentatie, veiligheidsnormen en implementatiegidsen gecontroleerd
- **Beste praktijken dekking**: Volledige dekking bevestigd van authenticatie, autorisatie, AI-specifieke bedreigingen, supply chain-beveiliging en bedrijfsmodellen

## 6 oktober 2025

### Uitbreiding Getting Started-sectie – Geavanceerd servergebruik & eenvoudige authenticatie

#### Geavanceerd Servergebruik (03-GettingStarted/10-advanced)
- **Nieuw hoofdstuk toegevoegd**: Uitgebreide gids geïntroduceerd voor geavanceerd MCP servergebruik, met beide reguliere en low-level serverarchitecturen.
  - **Reguliere vs. Low-Level Server**: Gedetailleerde vergelijking en codevoorbeelden in Python en TypeScript voor beide benaderingen.
  - **Handler-gebaseerd ontwerp**: Uitleg van handler-gebaseerd beheer van tool/resource/prompt voor schaalbare, flexibele serverimplementaties.
  - **Praktische patronen**: Praktijkscenario's waarin low-level serverpatronen voordelig zijn voor geavanceerde functies en architectuur.

#### Eenvoudige Authenticatie (03-GettingStarted/11-simple-auth)
- **Nieuw hoofdstuk toegevoegd**: Stapsgewijze gids voor het implementeren van eenvoudige authenticatie in MCP-servers.
  - **Auth-concepten**: Duidelijke uitleg van authenticatie versus autorisatie, en het omgaan met referenties.
  - **Basis Auth-implementatie**: Middleware-gebaseerde authenticatiepatronen in Python (Starlette) en TypeScript (Express), met codevoorbeelden.
  - **Doorontwikkeling naar geavanceerde beveiliging**: Richtlijnen om te starten met eenvoudige auth en uit te breiden naar OAuth 2.1 en RBAC, met verwijzingen naar geavanceerde beveiligingsmodules.

Deze toevoegingen bieden praktische, hands-on begeleiding voor het bouwen van robuustere, veiligere en flexibelere MCP-serverimplementaties, die fundamentele concepten met geavanceerde productiepatronen verbinden.

## 29 september 2025

### MCP Server Database Integratie Labs - Uitgebreid Hands-On Leertraject

#### 11-MCPServerHandsOnLabs - Nieuwe Complete Database Integratie Curriculum
- **Volledige 13-Lab Leertraject**: Uitgebreid hands-on curriculum toegevoegd voor het bouwen van production-ready MCP-servers met PostgreSQL database-integratie
  - **Praktijkgevallen**: Zava Retail analytics use case die enterprise-grade patronen demonstreert
  - **Gestructureerde Leerprogressie**:
    - **Labs 00-03: Basis** - Introductie, Core Architectuur, Beveiliging & Multi-Tenancy, Omgevingssetup
    - **Labs 04-06: Het bouwen van de MCP-server** - Databasedesign & Schema, MCP Server Implementatie, Toolontwikkeling  
    - **Labs 07-09: Geavanceerde functies** - Semantische zoekintegratie, testen & debuggen, VS Code-integratie
    - **Labs 10-12: Productie & beste praktijken** - Deploymentsstrategieën, monitoring & observability, beste praktijken & optimalisatie
  - **Enterprise Technologieën**: FastMCP framework, PostgreSQL met pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Geavanceerde functies**: Row Level Security (RLS), semantische zoekfuncties, multi-tenant data toegang, vector embeddings, realtime monitoring

#### Terminologiestandaardisatie - Module naar Lab converteer
- **Uitgebreide documentatie-update**: Systematische update van alle README-bestanden in 11-MCPServerHandsOnLabs om "Lab" terminologie in plaats van "Module" te gebruiken
  - **Sectiekoppen**: "Wat deze module behandelt" gewijzigd in "Wat deze lab behandelt" voor alle 13 labs
  - **Inhoudsbeschrijving**: "Deze module biedt..." veranderd naar "Deze lab biedt..." door hele documentatie
  - **Leerdoelen**: "Aan het einde van deze module..." gewijzigd in "Aan het einde van deze lab..." 
  - **Navigatielinks**: Alle "Module XX:" verwijzingen aangepast naar "Lab XX:" in kruisverwijzingen en navigatie
  - **Voortgangsbewaking**: "Na het voltooien van deze module..." aangepast naar "Na het voltooien van deze lab..."
  - **Behouden technische verwijzingen**: Python moduleverwijzingen in configuratiebestanden behouden (bijv. `"module": "mcp_server.main"`)

#### Studiegids Verbetering (study_guide.md)
- **Visuele curriculumkaart**: Nieuwe sectie "11. Database Integratie Labs" toegevoegd met uitgebreide visualisatie van labstructuur
- **Repository structuur**: Geüpdatet van tien naar elf hoofdsecties met gedetailleerde beschrijving van 11-MCPServerHandsOnLabs
- **Leerwegindicaties**: Verbeterde navigatie-instructies voor secties 00-11
- **Technologie-dekking**: Toegevoegd FastMCP, PostgreSQL, Azure service-integratiedetails
- **Leeruitkomsten**: Benadrukt ontwikkeling van production-ready servers, database-integratiepatronen, en enterprise beveiliging

#### Hoofd README structuur verbetering
- **Lab-terminologie**: Hoofd README.md in 11-MCPServerHandsOnLabs geüpdatet voor consistente "Lab" structuur
- **Leerpadorganisatie**: Duidelijke progressie van basisconcepten via geavanceerde implementatie naar productie-implementatie
- **Praktijkgericht**: Focus op hands-on leren met enterprise-grade patronen en technologieën

### Documentatiekwaliteit & consistentieverbeteringen
- **Hands-on leerfocus**: Praktische, lab-gebaseerde aanpak versterkt door hele documentatie
- **Enterprisepatronen focus**: Klemtoon op production-ready implementaties en enterprise beveiligingsaspecten
- **Technologie-integratie**: Uitgebreide dekking van moderne Azure diensten en AI-integratiepatronen
- **Leerprogressie**: Helder, gestructureerd pad van basisconcepten tot productie-implementatie

## 26 september 2025

### Case Studies Uitbreiding - GitHub MCP Registry integratie

#### Case Studies (09-CaseStudy/) - Ecosysteemontwikkelingsfocus
- **README.md**: Grote uitbreiding met uitgebreide GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Nieuwe uitgebreide case study met analyse van GitHub's MCP Registry lancering in september 2025
    - **Probleemanalyse**: Gedetailleerde beoordeling van gefragmenteerde MCP-server discovery en deployment uitdagingen
    - **Oplossingsarchitectuur**: GitHub's gecentraliseerde registry aanpak met one-click VS Code installatie
    - **Zakelijke impact**: Meetbare verbeteringen in onboarding en productiviteit van ontwikkelaars
    - **Strategische waarde**: Focus op modulaire agent deployment en cross-tool interoperabiliteit
    - **Ecosysteemontwikkeling**: Positionering als fundamenteel platform voor agentische integratie
  - **Verbeterde case study structuur**: Alle zeven case studies geüpdatet met consistente opmaak en uitgebreide beschrijvingen
    - Azure AI Travel Agents: Klemtoon op multi-agent orkestratie
    - Azure DevOps Integratie: Focus op workflow-automatisering
    - Real-Time documentatie-inwinning: Python console client implementatie
    - Interactieve studieplangenerator: Chainlit conversational web app
    - In-Editor documentatie: VS Code en GitHub Copilot integratie
    - Azure API Management: Enterprise API-integratiepatronen
    - GitHub MCP Registry: Ecosysteemontwikkeling en community platform
  - **Uitgebreide conclusie**: Herschreven conclusie met nadruk op zeven case studies die meerdere MCP-implementatiedimensies beslaan
    - Enterprise-integratie, Multi-Agent Orkestratie, Ontwikkelaarsproductiviteit
    - Ecosysteemontwikkeling, Educatieve toepassingen categorisatie
    - Versterkte inzichten in architectuurpatronen, implementatiestrategieën en beste praktijken
    - Nadruk op MCP als volwassen, productie-klaar protocol

#### Studiegids-updates (study_guide.md)
- **Visuele curriculumkaart**: Mindmap bijgewerkt om GitHub MCP Registry op te nemen in Case Studies sectie
- **Case Studies Beschrijving**: Verbeterd van generieke beschrijvingen naar gedetailleerde analyse van zeven uitgebreide case studies
- **Repository structuur**: Sectie 10 bijgewerkt om uitgebreide case study-dekking met specifieke implementatiedetails weer te geven
- **Changelog integratie**: September 26, 2025 entry toegevoegd die GitHub MCP Registry toevoeging en case study uitbreidingen documenteert
- **Datumupdates**: Footer timestamp bijgewerkt naar laatste revisie (26 september 2025)

### Documentatie Kwaliteitsverbeteringen
- **Consistentieversterking**: Gestandaardiseerde case study-opmaak en structuur over alle zeven voorbeelden
- **Uitgebreide dekking**: Case studies beslaan nu enterprise, ontwikkelaarsproductiviteit en ecosysteemontwikkelingsscenario's
- **Strategische positionering**: Versterkte focus op MCP als fundamenteel platform voor agentische systeembediening
- **Bronintegratie**: Aanvullende bronnen bijgewerkt met link naar GitHub MCP Registry

## 15 september 2025

### Geavanceerde Onderwerpen Uitbreiding - Aangepaste Transports & Context Engineering

#### MCP Aangepaste Transports (05-AdvancedTopics/mcp-transport/) - Nieuwe Geavanceerde Implementatiegids
- **README.md**: Volledige implementatiegids voor aangepaste MCP transportmechanismen
  - **Azure Event Grid Transport**: Uitgebreide serverless event-driven transportimplementatie
    - Voorbeelden in C#, TypeScript en Python met Azure Functions integratie
    - Event-driven architectuurpatronen voor schaalbare MCP-oplossingen
    - Webhook-ontvangers en push-gebaseerde berichtafhandeling
  - **Azure Event Hubs Transport**: Hoge doorvoercapaciteit streamingtransportimplementatie
    - Real-time streamingmogelijkheden voor low-latency scenario's
    - Partitioneringsstrategieën en checkpointbeheer
    - Berichtensameling en prestatie-optimalisatie
  - **Enterprise Integratiepatronen**: Productieklaar architectuurvoorbeelden
    - Gedistribueerde MCP-verwerking over meerdere Azure Functions
    - Hybride transportarchitecturen die meerdere transporttypes combineren
    - Berichtduurzamer, betrouwbaarheid en foutafhandelingsstrategieën
  - **Beveiliging & Monitoring**: Azure Key Vault integratie en observability-patronen
    - Managed identity authenticatie en toegang met het minste privilege
    - Application Insights telemetrie en prestatiemonitoring
    - Circuit breakers en fouttolerantiepatronen
  - **Testframeworks**: Uitgebreide teststrategieën voor aangepaste transports
    - Unit testen met test-doubles en mocking frameworks
    - Integratietesten met Azure Test Containers
    - Prestatie- en belastingstestoverwegingen

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Opkomende AI-discipline
- **README.md**: Uitgebreide verkenning van context engineering als een opkomend vakgebied
  - **Kernprincipes**: Volledige contextdeling, bewustzijn van actiebeslissingen, en beheer van contextvensters

  - **MCP Protocoluitlijning**: Hoe MCP-ontwerp uitdagingen in contextengineering aanpakt
    - Beperkingen van contextvensters en progressieve laadstrategieën
    - Bepaling van relevantie en dynamische contextopvraging
    - Meerdere modaliteiten contextafhandeling en beveiligingsoverwegingen
  - **Implementatiebenaderingen**: Single-threaded versus multi-agent architecturen
    - Contextsegmentering en prioriteringstechnieken
    - Progressieve contextlading en compressiestrategieën
    - Gelaagde contextbenaderingen en optimalisatie van opvraging
  - **Meetkader**: Opkomende metrics voor evaluatie van contexteffectiviteit
    - Inputefficiëntie, prestaties, kwaliteit en gebruikservaringsoverwegingen
    - Experimentele benaderingen voor contextoptimalisatie
    - Falanalyse en verbeteringsmethodologieën

#### Updates Curriculumnavigatie (README.md)
- **Verbeterde Modulstructuur**: Bijgewerkte curriculumtabel met nieuwe geavanceerde onderwerpen
  - Toegevoegd Context Engineering (5.14) en Custom Transport (5.15) vermeldingen
  - Consistente opmaak en navigatielinks in alle modules
  - Bijgewerkte omschrijvingen om huidige inhoudsomvang weer te geven

### Verbeteringen Mappenstructuur
- **Naamstandaardisatie**: Hernoemd "mcp transport" naar "mcp-transport" voor consistentie met andere geavanceerde onderwerpenmappen
- **Inhoudsorganisatie**: Alle 05-AdvancedTopics mappen volgen nu een consistent naamgevingspatroon (mcp-[onderwerp])

### Verhoging Documentatiekwaliteit
- **MCP Specificatie-uitlijning**: Alle nieuwe inhoud verwijst naar actuele MCP Specificatie 2025-06-18
- **Meertalige Voorbeelden**: Uitgebreide codevoorbeelden in C#, TypeScript en Python
- **Enterprise Focus**: Productierijpe patronen en Azure cloudintegratie doorlopend
- **Visuele Documentatie**: Mermaid diagrammen voor architectuur- en stroomvisualisatie

## 18 augustus 2025

### Uitgebreide Documentatie-update - MCP 2025-06-18 Normen

#### MCP Beveiligingspraktijken (02-Security/) - Volledige Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Volledige herschrijving afgestemd op MCP Specificatie 2025-06-18
  - **Verplichte Vereisten**: Toevoeging van expliciete MOET/MOET NIET vereisten vanuit officiële specificatie met duidelijke visuele indicatoren
  - **12 Kernbeveiligingspraktijken**: Herschikt van lijst van 15 punten naar volledige beveiligingsdomeinen
    - Tokenbeveiliging & Authenticatie met integratie van externe identiteitsprovider
    - Sessiebeheer & Transportbeveiliging met cryptografische vereisten
    - AI-specifieke dreigingsbescherming met integratie van Microsoft Prompt Shields
    - Toegangscontrole & Machtigingen met principe van minste privilege
    - Inhoudsveiligheid & Monitoring met integratie van Azure Content Safety
    - Supply Chain Beveiliging met uitgebreide componentverificatie
    - OAuth-beveiliging & Confused Deputy Preventie met PKCE-implementatie
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden
    - Compliance & Governance met naleving van regelgeving
    - Geavanceerde Beveiligingscontroles met zero trust architectuur
    - Integratie Microsoft Beveiligingsecosysteem met uitgebreide oplossingen
    - Continue Beveiligingsevolutie met adaptieve praktijken
  - **Microsoft Beveiligingsoplossingen**: Verbeterde integratierichtlijnen voor Prompt Shields, Azure Content Safety, Entra ID en GitHub Advanced Security
  - **Implementatieresources**: Gecategoriseerde uitgebreide bronnelinks per officiële MCP documentatie, Microsoft beveiligingsoplossingen, beveiligingsstandaarden en implementatiehandleidingen

#### Geavanceerde Beveiligingscontroles (02-Security/) - Enterprise Implementatie
- **MCP-SECURITY-CONTROLS-2025.md**: Complete revisie met enterprise-grade beveiligingsframework
  - **9 Omvattende Beveiligingsdomeinen**: Uitgebreid van basiscontroles naar gedetailleerd enterprise-framework
    - Geavanceerde Authenticatie & Autorisatie met integratie Microsoft Entra ID
    - Tokenbeveiliging & Anti-Passthrough controles met uitgebreide validatie
    - Sessiebeveiligingscontroles met onderscheppingspreventie
    - AI-specifieke beveiligingscontroles met promptinjectie en toolvergiftigingspreventie
    - Confused Deputy aanvalpreventie met OAuth-proxy beveiliging
    - Tooluitvoeringsbeveiliging met sandboxing en isolatie
    - Supply Chain beveiligingscontroles met afhankelijkheidsverificatie
    - Monitoring & Detectiecontroles met SIEM-integratie
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden
  - **Implementatievoorbeelden**: Toegevoegd gedetailleerde YAML-configuratieblokken en codevoorbeelden
  - **Integratie Microsoft Oplossingen**: Uitgebreide dekking van Azure beveiligingsdiensten, GitHub Advanced Security en enterprise-identiteitsbeheer

#### Geavanceerde Onderwerpen Beveiliging (05-AdvancedTopics/mcp-security/) - Productierijpe Implementatie
- **README.md**: Volledige herschrijving voor enterprise beveiligingsimplementatie
  - **Actuele Specificatie-uitlijning**: Bijgewerkt naar MCP Specificatie 2025-06-18 met verplichte beveiligingseisen
  - **Verbeterde Authenticatie**: Integratie Microsoft Entra ID met uitgebreide .NET en Java Spring Security voorbeelden
  - **AI Beveiligingsintegratie**: Implementatie Microsoft Prompt Shields en Azure Content Safety met gedetailleerde Python voorbeelden
  - **Geavanceerde Dreigingsmitigatie**: Uitgebreide implementatievoorbeelden voor
    - Confused Deputy aanvalpreventie met PKCE en gebruikersconsentvalidatie
    - Token Passthrough Preventie met publiekvalidatie en veilige tokenbeheer
    - Sessie-onderscheppingspreventie met cryptografische binding en gedragsanalyse
  - **Enterprise Beveiligingsintegratie**: Azure Application Insights monitoring, dreigingsdetectiepijplijnen en supply chain beveiliging
  - **Implementatiechecklist**: Duidelijke verplichte versus aanbevolen beveiligingscontroles met Microsoft beveiligingsecosysteem voordelen

### Documentatiekwaliteit & Normuitlijning
- **Specificatieverwijzingen**: Bijgewerkte alle verwijzingen naar actuele MCP Specificatie 2025-06-18
- **Microsoft Beveiligingsecosysteem**: Verbeterde integratierichtlijnen door alle beveiligingsdocumentatie
- **Praktische Implementatie**: Toegevoegd gedetailleerde codevoorbeelden in .NET, Java en Python met enterprise patronen
- **Bronnenorganisatie**: Uitgebreide categorisering van officiële documentatie, beveiligingsstandaarden en implementatiehandleidingen
- **Visuele Indicatoren**: Duidelijke markering van verplichte vereisten versus aanbevolen praktijken


#### Kernconcepten (01-CoreConcepts/) - Volledige Modernisering
- **Protocolversie-update**: Bijgewerkt naar verwijzing actuele MCP Specificatie 2025-06-18 met datumgebaseerde versionering (YYYY-MM-DD-formaat)
- **Architectuurverfijning**: Verbeterde omschrijvingen van Hosts, Clients en Servers om huidige MCP architectuurpatronen weer te geven
  - Hosts nu duidelijk gedefinieerd als AI-toepassingen die meerdere MCP-clientverbindingen coördineren
  - Clients beschreven als protocolkoppelingen met een-op-een serverrelaties
  - Servers verbeterd met lokale versus remote deploymentscenario's
- **Primitieve Herstructurering**: Volledige revisie van server- en clientprimitieven
  - Serverprimitieven: Bronnen (datasources), Prompts (sjablonen), Hulpmiddelen (uitvoerbare functies) met gedetailleerde uitleg en voorbeelden
  - Clientprimitieven: Sampling (LLM-afrondingen), Elicitation (gebruikersinput), Logging (debugging/monitoring)
  - Bijgewerkt met huidige discovery (`*/list`), retrieval (`*/get`) en execution (`*/call`) methodepatronen
- **Protocolarchitectuur**: Geïntroduceerd tweelaags architectuurmodel
  - Datalayer: JSON-RPC 2.0 basis met levenscyclusbeheer en primitieven
  - Transportlaag: STDIO (lokaal) en Streamable HTTP met SSE (remote) transportmechanismen
- **Beveiligingskader**: Uitgebreide beveiligingsprincipes inclusief expliciete gebruikersconsent, databescherming, uitvoeringsveiligheid tools en transportlaagbeveiliging
- **Communicatiepatronen**: Bijgewerkte protocolberichten voor initialisatie, discovery, uitvoering en notificatie
- **Codevoorbeelden**: Vernieuwde meertalige voorbeelden (.NET, Java, Python, JavaScript) ter reflectie van huidige MCP SDK patronen

#### Beveiliging (02-Security/) - Omvattende Beveiligingsrevisie  
- **Normuitlijning**: Volledige afstemming op MCP Specificatie 2025-06-18 beveiligingseisen
- **Authenticatie-evolutie**: Gedocumenteerde evolutie van eigen OAuth-servers naar delegatie via externe identiteitsprovider (Microsoft Entra ID)
- **AI-specifieke Dreigingsanalyse**: Verbeterde dekking van moderne AI-aanvalsvectoren
  - Gedetailleerde promptinjectie-aanvalscenario's met praktijkvoorbeelden
  - Toolvergiftigingsmechanismen en "rug pull" aanvalspatronen
  - Contextvenstervergiftiging en modelverwarraanvallen
- **Microsoft AI Beveiligingsoplossingen**: Omvattende dekking Microsoft beveiligingsecosysteem
  - AI Prompt Shields met geavanceerde detectie, spotlighting en delimiter-technieken
  - Azure Content Safety integratiepatronen
  - GitHub Advanced Security voor supply chain bescherming
- **Geavanceerde Dreigingsmitigatie**: Gedetailleerde beveiligingscontroles voor
  - Sessiekaping met MCP-specifieke aanvalscenario's en cryptografische sessie-ID vereisten
  - Confused deputy problemen in MCP proxy scenario's met expliciete consentvereisten
  - Token passthrough kwetsbaarheden met verplichte validatiecontroles
- **Supply Chain Beveiliging**: Uitgebreide AI supply chain dekking inclusief foundation modellen, embeddings services, contextaanbieders en third-party API's
- **Foundation Beveiliging**: Verbeterde integratie met enterprise beveiligingspatronen inclusief zero trust architectuur en Microsoft beveiligingsecosysteem
- **Bronnenorganisatie**: Gecategoriseerde uitgebreide bronnelinks per type (Officiële Docs, Standaarden, Onderzoek, Microsoft Oplossingen, Implementatiehandleidingen)

### Verbeteringen Documentatiekwaliteit
- **Gestructureerde Leerdoelen**: Versterkte leerdoelen met specifieke, actiegerichte uitkomsten 
- **Kruisverwijzingen**: Toegevoegd links tussen gerelateerde beveiligings- en kernconceptonderwerpen
- **Actuele Informatie**: Alle datumverwijzingen en specificatielinks bijgewerkt naar actuele normen
- **Implementatierichtlijnen**: Toegevoegd specifieke, actiegerichte implementatierichtlijnen in beide secties

## 16 juli 2025

### README en Navigatieverbeteringen
- Het curriculumnavigatie in README.md volledig herontworpen
- `<details>` tags vervangen door toegankelijker tabelgebaseerd formaat
- Alternatieve lay-outopties toegevoegd in nieuwe map "alternative_layouts"
- Navigatievoorbeelden toegevoegd op basis van kaarten, tabbladen en accordeonstijlen
- Repositoriumstructuur sectie bijgewerkt met alle nieuwste bestanden
- Verbeterde "Hoe Gebruik Je Dit Curriculum" sectie met duidelijke aanbevelingen
- MCP specificatielinks bijgewerkt naar correcte URL's
- Context Engineering sectie (5.14) toegevoegd aan curriculumstructuur

### Updates Studiegids
- Studiegids volledig herzien om aan te sluiten bij huidige repositorystructuur
- Nieuwe secties toegevoegd voor MCP Clients en Tools, en Populaire MCP Servers
- Visueel curriculumkaart bijgewerkt om alle onderwerpen accuraat weer te geven
- Omschrijvingen Geavanceerde Onderwerpen verbeterd om alle gespecialiseerde gebieden te omvatten
- Casestudiesectie bijgewerkt met actuele voorbeelden
- Deze uitgebreide changelog toegevoegd

### Communitybijdragen (06-CommunityContributions/)
- Uitgebreide informatie toegevoegd over MCP-servers voor beeldgeneratie
- Omvattende sectie toegevoegd over gebruik van Claude in VSCode
- Instructies toegevoegd voor installatie en gebruik van Cline terminalclient
- MCP clientsectie bijgewerkt met alle populaire clientopties
- Bijdragervoorbeelden verbeterd met meer accurate codesamples

### Geavanceerde Onderwerpen (05-AdvancedTopics/)
- Alle gespecialiseerde onderwerpmappen georganiseerd met consistente naamgeving
- Context engineering materialen en voorbeelden toegevoegd
- Foundry agent integratiedocumentatie toegevoegd
- Verbeterde documentatie integratie Entra ID beveiliging

## 11 juni 2025

### Eerste Creatie
- Eerste versie van MCP voor Beginners curriculum uitgebracht
- Basisstructuur gemaakt voor alle 10 hoofdsecties
- Visuele curriculumkaart geïmplementeerd voor navigatie
- Eerste voorbeeldprojecten toegevoegd in meerdere programmeertalen

### Aan de Slag (03-GettingStarted/)
- Eerste serverimplementatievoorbeelden gemaakt
- Klantontwikkelingsrichtlijnen toegevoegd
- Integratie-instructies voor LLM-clients opgenomen
- Documentatie voor VS Code-integratie toegevoegd
- Server-Sent Events (SSE) servervoorbeelden geïmplementeerd

### Kernconcepten (01-CoreConcepts/)
- Gedetailleerde uitleg toegevoegd over client-server architectuur
- Documentatie gemaakt over kernprotocolcomponenten
- Messagingpatronen in MCP gedocumenteerd

## 23 mei 2025

### Repositoriumstructuur
- Repositorium geïnitieerd met basis mappenstructuur
- README-bestanden gemaakt voor elke hoofdsectie
- Vertaalinfrastructuur opgezet
- Beeldassets en diagrammen toegevoegd

### Documentatie
- Eerste README.md met curriculumoverzicht gemaakt
- CODE_OF_CONDUCT.md en SECURITY.md toegevoegd
- SUPPORT.md opgezet met richtlijnen voor hulp
- Voorlopige structuur studiegids opgesteld

## 15 april 2025

### Planning en Kader
- Initiële planning voor MCP voor Beginners curriculum
- Leerdoelen en doelgroep gedefinieerd
- Structuur van 10 secties van het curriculum geschetst
- Conceptueel kader ontwikkeld voor voorbeelden en casestudies
- Eerste prototypevoorbeelden gemaakt voor kernconcepten

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
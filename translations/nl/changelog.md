# Wijzigingslog: MCP voor Beginners Curriculum

Dit document dient als een verslag van alle belangrijke wijzigingen die zijn aangebracht aan het Model Context Protocol (MCP) voor Beginners curriculum. Wijzigingen worden vastgelegd in omgekeerde chronologische volgorde (nieuwste wijzigingen eerst).

## 11 april 2026

### Nieuwe Les, Documentatiefixes en Afhankelijkheidsupdates

#### Nieuwe Curriculum Inhoud Toegevoegd

**Module 05 - Geavanceerde Onderwerpen**  
- **Les 5.17: Adversarial Multi-Agent Redeneren met MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Nieuwe uitgebreide gids die het adversarial debatpatroon voor multi-agent systemen behandelt  
  - Mermaid architectuurdiagram: twee agenten → gedeelde MCP-server → debattranscript → rechter → oordeel  
  - Gedeelde MCP toolserver (`web_search` + `run_python`) geïmplementeerd in Python en TypeScript  
  - Tegengestelde systeem prompten (VOOR / TEGEN / Rechter) met expliciete tool-gebruikvereisten  
  - Debat orchestrator in Python, TypeScript en C# die rondes beheert en argumenten routeren  
  - MCP `ClientSession` koppeling voor de orchestrator naar echte tool-aanroepen  
  - Gebruiksgrafiektabel (hallucinatie detectie, bedreigingsmodellering, API-ontwerpbeoordeling, feitelijke verificatie, technologische selectie)  
  - Beveiligingsoverwegingen: sandbox uitvoering, validatie van tool-aanroepen, rate limiting, audit logging  
  - Gestructureerde oefening met drie praktische scenario's (code review, architectuurbeslissing, inhoudsmoderatie)  

#### Documentatiefixes

**Module 03 - Aan de Slag**  
- **05-stdio-server/README.md**: Ongeldig incompleet TypeScript stdio server voorbeeld gerepareerd — toegevoegd ontbrekende transportinstantiering (`new StdioServerTransport()`) en `server.connect(transport)` oproep om te stemmen met Python en .NET voorbeelden in dezelfde sectie  
- **14-sampling/README.md**: Typfout gerepareerd — gecorrigeerd `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`  

#### Curriculum Updates

**Hoofd README.md**  
- Invoer 5.17 (Adversarial Multi-Agent Redeneren met MCP) toegevoegd aan de curriculumlijst met directe link naar de nieuwe les  

**05-AdvancedTopics/README.md**  
- Rij voor Les 5.17 toegevoegd aan de lessen tabel  

**study_guide.md**  
- Onderwerp Adversarial Multi-Agent Redeneren toegevoegd aan de mindmap en prozabeschrijving van Geavanceerde Onderwerpen  

#### Code- en Beveiligingsfixes

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**  
- **Beveiligingsfix — command injection**: `execSync` shell interpolatie vervangen door `execFile` + `promisify` in de TypeScript `run_python` tool, waarmee het command injection oppervlak is geëlimineerd (LLM-gestuurde code wordt nu als letterlijk argv-element doorgegeven zonder shell betrokkenheid)  
- **MCP tool loop bekabeling**: Python debat orchestrator bijgewerkt naar gebruik van `AsyncAnthropic` client (ter vervanging van blokkerende synchroon `Anthropic`), live `ClientSession` direct doorgegeven aan elke agent beurt, tooldefinities opgehaald via `session.list_tools()` per beurt, en `tool_use` blokken verzonden via `session.call_tool()` in een lus totdat het model een finale tekstrespons afgeeft  

#### Afhankelijkheidsupdates

- `hono` verhoogd naar 4.12.12 in meerdere pakketten (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- `@hono/node-server` verhoogd van 1.19.11 naar 1.19.13 in TypeScript pakketten  
- `cryptography` verhoogd van 46.0.5 naar 46.0.7 in Python pakketten (10-StreamliningAIWorkflows labs 3 en 4)  
- `lodash` verhoogd van 4.17.23 naar 4.18.1 in 10-StreamliningAIWorkflows inspector  

#### Vertalingen

- Vertalingen voor 48+ talen gesynchroniseerd met de laatste bronwijzigingen (i18n update)  

---

## 5 februari 2026

### Repository-brede Validatie en Navigatieverbeteringen

#### Nieuwe Curriculum Inhoud Toegevoegd

**Module 03 - Aan de Slag**  
- **12-mcp-hosts/README.md**: Nieuwe uitgebreide handleiding voor het opzetten van MCP hosts  
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf configuratievoorbeelden  
  - JSON configuratiesjablonen voor alle grote hosts  
  - Transporttypen vergelijkingstabel (stdio, SSE/HTTP, WebSocket)  
  - Troubleshooting veelvoorkomende verbindingsproblemen  
  - Beveiligingsbest practices voor hostconfiguratie  

- **13-mcp-inspector/README.md**: Nieuwe debuggids voor MCP Inspector  
  - Installatiemethoden (npx, npm globaal, vanuit bron)  
  - Verbinden met servers via stdio en HTTP/SSE  
  - Testtools, resources en prompt-workflows  
  - VS Code integratie met MCP Inspector  
  - Veelvoorkomende debugscenario's met oplossingen  

**Module 04 - Praktische Implementatie**  
- **pagination/README.md**: Nieuwe paginering implementatiehandleiding  
  - Cursorgebaseerde paginering patronen in Python, TypeScript, Java  
  - Client-side pagineringsafhandeling  
  - Cursor ontwerpstrategieën (ondoorzichtig vs. gestructureerd)  
  - Prestatieoptimalisatie aanbevelingen  

**Module 05 - Geavanceerde Onderwerpen**  
- **mcp-protocol-features/README.md**: Nieuwe diepgaande gids over protocolfeatures  
  - Implementatie van voortgangsnotificaties  
  - Annuleringspatronen voor verzoeken  
  - Resource sjablonen met URI-patronen  
  - Serverlevenscyclusbeheer  
  - Logniveau besturing  
  - Foutafhandelingspatronen met JSON-RPC codes  

#### Navigatiefixes (24+ bestanden bijgewerkt)

**Hoofd Module README's**  
Nu links naar zowel eerste les ALS volgende module  

**02-Security Sub-bestanden**  
- Alle 5 aanvullende beveiligingsdocumenten hebben nu "Wat Nu" navigatie:  

**09-CaseStudy Bestanden**  
- Alle case study bestanden hebben nu opeenvolgende navigatie:  

**10-StreamliningAI Labs**  
"Wat Nu" sectie toegevoegd aan Module 10 overzicht en Module 11  

#### Code- en Contentfixes

**SDK en Afhankelijkheidsupdates**  
Lege openai versie aangepast naar `^4.95.0`  
SDK bijgewerkt van `^1.8.0` naar `>=1.26.0`  
mcp versie pins aangepast naar `>=1.26.0`  

**Codefixes**  
Ongeldig model `gpt-4o-mini` hersteld naar `gpt-4.1-mini`  

**Contentfixes**  
Verbroken link `READMEmd` → `README.md` gerepareerd, curriculumkop `Module 1-3` → `Module 0-3` gecorrigeerd, case-sensitive pad aangepast  
Dubbele corrupte Case Study 5 inhoud verwijderd  

**Verbeteringen voor Beginners**  
Introductie, leerdoelen en vereisten voor beginners toegevoegd  

#### Curriculum Updates

**Hoofd README.md**  
- Invoeren 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protocol Features) toegevoegd aan curriculumtabel  

**Module README's**  
- Lessen 12 en 13 toegevoegd aan lessenlijst  
- Praktische Gidsen sectie met pagineringslink toegevoegd  
- Lessen 5.15 (Custom Transport) en 5.16 (Protocol Features) toegevoegd  

**study_guide.md**  
- Mindmap bijgewerkt met alle nieuwe onderwerpen: MCP Hosts Setup, MCP Inspector, Paginering Strategieën, Protocol Features Deep Dive  

## 28 januari 2026

### MCP Specificatie 2025-11-25 Compliance Review

#### Kernconceptenverbetering (01-CoreConcepts/)  
- **Nieuwe Client Primitive - Roots**: Uitgebreide documentatie toegevoegd over de Roots client primitive, waarmee servers bestandssysteemgrenzen en toegangsrechten kunnen begrijpen  
- **Tool Annotaties**: Documentatie toegevoegd over tool gedragsannotaties (`readOnlyHint`, `destructiveHint`) voor betere uitvoering beslissingen  
- **Toolaanroepen in Sampling**: Sampling documentatie bijgewerkt met parameters `tools` en `toolChoice` voor modelgestuurde toolaanroepen tijdens sampling verzoeken  
- **URL-Mode Elicitation**: Documentatie toegevoegd over URL-gebaseerde elicitation voor server-geïnitieerde externe webinteracties  
- **Taken (Experimenteel)**: Nieuwe sectie toegevoegd die de experimentele Taken functie beschrijft voor duurzame uitvoeringswrappers en uitgestelde resultaatopvraging  
- **Iconen Ondersteuning**: Opmerking dat tools, resources, resourcesjablonen en prompten nu iconen als aanvullende metadata kunnen bevatten  

#### Documentatie-updates  
- **README.md**: MCP Specificatie 2025-11-25 versievermelding en op datum gebaseerde versiebeheer uitleg toegevoegd  
- **study_guide.md**: Curriculumkaart bijgewerkt met Taken en Tool Annotaties in de sectie Kernconcepten; documenttijdstempel aangepast  

#### Specificatie Compliance Verificatie  
- **Protocolversie**: Gecontroleerd dat alle documentatie verwijst naar MCP Specificatie 2025-11-25  
- **Architectuurafstemming**: Bevestigd nauwkeurigheid van twee-laags architectuur (Data Layer + Transport Layer) documentatie  
- **Primitives Documentatie**: Valide server primitives (Resources, Prompts, Tools) en client primitives (Sampling, Elicitation, Logging, Roots)  
- **Transportmechanismen**: Geverifieerde accuratesse van STDIO en Streamable HTTP transportdocumentatie  
- **Beveiligingsrichtlijnen**: Bevestigde afstemming met actuele MCP Security Best Practices documentatie  

#### Belangrijke MCP 2025-11-25 Kenmerken Gedocumenteerd  
- **OpenID Connect Discovery**: Auth server ontdekking via OIDC  
- **OAuth Client ID Metadata Documenten**: Aanbevolen client registratie mechanisme  
- **JSON Schema 2020-12**: Standaard dialect voor MCP schema definities  
- **SDK Tiering Systeem**: Geformaliseerde vereisten voor SDK feature ondersteuning en onderhoud  
- **Governance Structuur**: Geformaliseerde Werkgroepen en Interessegroepen in MCP governance  

### Grote Update van Beveiligingsdocumentatie (02-Security/)

#### Integratie MCP Security Summit Workshop (Sherpa)  
- **Nieuwe Hands-on Trainingsresource**: Uitgebreide integratie toegevoegd met de [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) door alle beveiligingsdocumentatie heen  
- **Expeditieroute Dekking**: Documentatie van het volledige kamp-tot-kamp verloop van Base Camp tot Summit  
- **OWASP Afstemming**: Alle beveiligingsrichtlijnen nu gemapt aan OWASP MCP Azure Security Guide risico’s  

#### Integratie OWASP MCP Top 10  
- **Nieuwe Sectie**: OWASP MCP Top 10 beveiligingsrisico’s tabel met Azure mitigaties toegevoegd aan hoofd Security README  
- **Risicogebaseerde Documentatie**: mcp-security-controls-2025.md bijgewerkt met OWASP MCP risicoverwijzingen per beveiligingsdomein  
- **Referentie Architectuur**: Gelinkt aan OWASP MCP Azure Security Guide referentiearchitectuur en implementatiepatronen  

#### Bijgewerkte Beveiligingsbestanden  
- **README.md**: Sherpa Workshop overzicht, expeditieroutetabel, OWASP MCP Top 10 risico-overzicht en hands-on trainingssectie toegevoegd  
- **mcp-security-controls-2025.md**: Koptekst bijgewerkt naar februari 2026, OWASP risicoverwijzingen (MCP01-MCP08) toegevoegd, spec versie inconsistentie gecorrigeerd  
- **mcp-security-best-practices-2025.md**: Sherpa en OWASP resources sectie toegevoegd, tijdstempel bijgewerkt  
- **mcp-best-practices.md**: Hands-on trainingssectie met Sherpa en OWASP links toegevoegd  
- **azure-content-safety-implementation.md**: OWASP MCP06 verwijzing, Sherpa Camp 3 afstemming en additionele bronnen sectie toegevoegd  

#### Nieuwe Resource Links Toegevoegd  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Individuele OWASP MCP risico pagina’s (MCP01-MCP10)  

### Curriculum-brede MCP Specificatie 2025-11-25 Afstemming

#### Module 03 - Aan de Slag  
- **SDK Documentatie**: Go SDK toegevoegd aan officiële SDK lijst; alle SDK verwijzingen bijgewerkt naar MCP Specificatie 2025-11-25  
- **Transportverduidelijking**: STDIO en HTTP Streaming transportbeschrijvingen geüpdatet met expliciete specificatieverwijzingen  

#### Module 04 - Praktische Implementatie  
- **SDK Updates**: Go SDK toegevoegd; SDK lijst bijgewerkt met specificatieversie verwijzing  
- **Autorisatiespecificatie**: MCP Autorisatiespecificatie link bijgewerkt naar actuele 2025-11-25 versie  

#### Module 05 - Geavanceerde Onderwerpen  
- **Nieuwe Features**: Opmerking toegevoegd over nieuwe MCP Specificatie 2025-11-25 features (Taken, Tool Annotaties, URL Mode Elicitation, Roots)  
- **Beveiligingsbronnen**: OWASP MCP Top 10 en Sherpa workshop links toegevoegd aan aanvullende referenties  

#### Module 06 - Community Bijdragen  
- **SDK Lijst**: Swift en Rust SDK’s toegevoegd; specificatielink bijgewerkt naar 2025-11-25  
- **Spec Verwijzing**: MCP Specificatie link bijgewerkt naar directe specificatie URL  

#### Module 07 - Lessen uit Vroege Adoptie  
- **Resource Updates**: MCP Specificatie 2025-11-25 link en OWASP MCP Top 10 toegevoegd aan aanvullende resources  

#### Module 08 - Best Practices  
- **Spec Versie**: MCP Specificatie verwijzing bijgewerkt naar 2025-11-25  
- **Beveiligingsbronnen**: OWASP MCP Top 10 en Sherpa workshop toegevoegd aan aanvullende referenties  

#### Module 10 - Streamlining AI Workflows  
- **Badge Update**: MCP versie badge gewijzigd van SDK versie (1.9.3) naar specificatieversie (2025-11-25)  
- **Resource Links**: MCP Specificatie link geüpdatet; OWASP MCP Top 10 toegevoegd  

#### Module 11 - MCP Server Hands-On Labs  
- **Spec Verwijzing**: MCP Specificatie link bijgewerkt naar versie 2025-11-25  
- **Beveiligingsbronnen**: OWASP MCP Top 10 toegevoegd aan officiële bronnen  

## 18 december 2025
### Beveiligingsdocumentatie Update - MCP Specificatie 2025-11-25

#### MCP Beveiligingsrichtlijnen (02-Security/mcp-best-practices.md) - Update Specificatieversie
- **Protocolversie Update**: Bijgewerkt naar verwijzing naar de nieuwste MCP Specificatie 2025-11-25 (uitgegeven op 25 november 2025)
  - Alle verwijzingen naar specificatieversies bijgewerkt van 2025-06-18 naar 2025-11-25
  - Documentdatum verwijzingen bijgewerkt van 18 augustus 2025 naar 18 december 2025
  - Alle specificatie-URL's gecontroleerd en wijzen naar de huidige documentatie
- **Inhoudsvalidatie**: Uitgebreide validatie van beveiligingsrichtlijnen volgens de nieuwste standaarden
  - **Microsoft Beveiligingsoplossingen**: Controle van huidige terminologie en links voor Prompt Shields (voorheen "Jailbreak risicodetectie"), Azure Content Safety, Microsoft Entra ID en Azure Key Vault
  - **OAuth 2.1 Beveiliging**: Bevestiging van afstemming met de nieuwste OAuth beveiligingsrichtlijnen
  - **OWASP Standaarden**: Validatie dat OWASP Top 10 voor LLMs verwijzingen actueel blijven
  - **Azure Diensten**: Controle van alle Microsoft Azure documentatielinks en best practices
- **Standaardenaansluiting**: Alle geraadpleegde beveiligingsstandaarden bevestigd actueel
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure beveiligings- en compliancekaders
- **Implementatieresources**: Gecontroleerde links en bronnen van implementatiehandleidingen
  - Azure API Management authenticatiepatronen
  - Microsoft Entra ID integratiehandleidingen
  - Azure Key Vault geheime beheer
  - DevSecOps pipelines en monitoringoplossingen

### Documentatie Kwaliteitsborging
- **Specificatie Naleving**: Gecontroleerd dat alle verplichte MCP beveiligingseisen (MUST/MUST NOT) overeenkomen met de nieuwste specificatie
- **Bronhargaheid**: Alle externe links naar Microsoft documentatie, beveiligingsstandaarden en implementatiehandleidingen geverifieerd
- **Best Practices Dekking**: Bevestigde volledige dekking van authenticatie, autorisatie, AI-specifieke bedreigingen, supply chain beveiliging en enterprise patronen

## 6 oktober 2025

### Uitbreiding Sectie Aan de Slag – Geavanceerd Servergebruik & Eenvoudige Authenticatie

#### Geavanceerd Servergebruik (03-GettingStarted/10-advanced)
- **Nieuw Hoofdstuk Toegevoegd**: Een uitgebreide handleiding geïntroduceerd voor geavanceerd MCP servergebruik, met zowel reguliere als laag-niveau serverarchitecturen.
  - **Reguliere versus Laag-niveau Server**: Gedetailleerde vergelijking en codevoorbeelden in Python en TypeScript voor beide benaderingen.
  - **Handler-Gebaseerd Ontwerp**: Uitleg over handler-gebaseerd beheer van tools/resources/prompts voor schaalbare, flexibele serverimplementaties.
  - **Praktische Patronen**: Scenario's uit de praktijk waarin laag-niveau serverpatronen nuttig zijn voor geavanceerde functies en architectuur.

#### Eenvoudige Authenticatie (03-GettingStarted/11-simple-auth)
- **Nieuw Hoofdstuk Toegevoegd**: Stapsgewijze handleiding voor het implementeren van eenvoudige authenticatie in MCP-servers.
  - **Authenticatieconcepten**: Duidelijke uitleg over authenticatie versus autorisatie, en credentialbeheer.
  - **Basisauthenticatie Implementatie**: Middleware-gebaseerde authenticatiepatronen in Python (Starlette) en TypeScript (Express) met codevoorbeelden.
  - **Overgang naar Geavanceerde Beveiliging**: Richtlijnen voor starten met eenvoudige authenticatie en doorgroeien naar OAuth 2.1 en RBAC, met verwijzingen naar geavanceerde beveiligingsmodules.

Deze toevoegingen bieden praktische, hands-on begeleiding voor het bouwen van robuustere, veiligere en flexibelere MCP-serverimplementaties, en vormen een brug tussen fundamentele concepten en geavanceerde productiekrachtpatronen.

## 29 september 2025

### MCP Server Database Integratie Labs - Uitgebreid Praktijkleertraject

#### 11-MCPServerHandsOnLabs - Nieuwe Volledige Database Integratie Curriculum
- **Volledig 13-Lab Leertraject**: Toegevoegd een uitgebreid praktijkcurriculum om productieklare MCP-servers te bouwen met PostgreSQL database-integratie
  - **Praktijkgerichte Implementatie**: Zava Retail analytics use case die enterprise-grade patronen demonstreert
  - **Gestructureerde Leerprogressie**:
    - **Labs 00-03: Fundamenten** - Introductie, Kernarchitectuur, Beveiliging & Multi-Tenancy, Omgevingsopzet
    - **Labs 04-06: MCP Server bouwen** - Databaseontwerp & Schema, MCP Server Implementatie, Toolontwikkeling  
    - **Labs 07-09: Geavanceerde Functies** - Semantische Zoekintegratie, Testen & Debuggen, VS Code Integratie
    - **Labs 10-12: Productie & Best Practices** - Deploymentsstrategieën, Monitoring & Observeerbaarheid, Best Practices & Optimalisatie
  - **Enterprise Technologieën**: FastMCP framework, PostgreSQL met pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Geavanceerde Functies**: Row Level Security (RLS), semantische zoekfuncties, multi-tenant data toegang, vector embeddings, realtime monitoring

#### Terminologiestandaardisatie - Omzetting Module naar Lab
- **Uitgebreide Documentatie Update**: Systematisch alle README-bestanden in 11-MCPServerHandsOnLabs bijgewerkt om "Lab" terminologie te gebruiken in plaats van "Module"
  - **Sectiekoppen**: "Wat deze module behandelt" bijgewerkt naar "Wat deze lab behandelt" in alle 13 labs
  - **Inhoudsbeschrijving**: "Deze module biedt..." gewijzigd in "Deze lab biedt..." door de hele documentatie
  - **Leerdoelen**: "Aan het einde van deze module..." gewijzigd naar "Aan het einde van deze lab..."
  - **Navigatielinks**: Alle "Module XX:" verwijzingen aangepast naar "Lab XX:" in kruisverwijzingen en navigatie
  - **Volgtracking**: "Na afronding van deze module..." aangepast naar "Na afronding van deze lab..."
  - **Technische Verwijzingen Behouden**: Python moduleverwijzingen in configuratiebestanden behouden (bv. `"module": "mcp_server.main"`)

#### Studiehandleiding Verbetering (study_guide.md)
- **Visuele Curriculumkaart**: Nieuwe sectie "11. Database Integratie Labs" toegevoegd met overzicht van labstructuur
- **Repository Structuur**: Bijgewerkt van tien naar elf hoofdsecties met gedetailleerde beschrijving van 11-MCPServerHandsOnLabs
- **Leertraject Richtlijnen**: Verbeterde navigatie-instructies voor secties 00-11
- **Technologie Dekking**: FastMCP, PostgreSQL, Azure services integratiedetails toegevoegd
- **Leerresultaten**: Benadrukking van productieklare serverontwikkeling, database-integratiepatronen en enterprise beveiliging

#### Hoofd README Structurele Verbetering
- **Lab-gebaseerde Terminologie**: Hoofd README.md in 11-MCPServerHandsOnLabs aangepast voor consequente "Lab" structuur
- **Leertraject Organisatie**: Heldere progressie van basisconcepten via geavanceerde implementatie naar productie-uitrol
- **Praktijkgerichte Focus**: Nadruk op hands-on leren met enterprise-grade patronen en technologieën

### Documentatie Kwaliteit & Consistentie Verbeteringen
- **Hands-On Leerbenadering**: Praktische, lab-gebaseerde aanpak versterkt door de hele documentatie
- **Enterprise Patronen Focus**: Nadruk op productieklare implementaties en enterprise beveiligingsoverwegingen
- **Technologie Integratie**: Uitgebreide dekking van moderne Azure diensten en AI-integratiepatronen
- **Leerprogressie**: Heldere, gestructureerde route van basisconcepten tot productiedistributie

## 26 september 2025

### Case Studies Verbetering - GitHub MCP Registry Integratie

#### Case Studies (09-CaseStudy/) - Ecosysteem Ontwikkelingsfocus
- **README.md**: Grote uitbreiding met uitgebreide GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Nieuwe uitgebreide case study over de lancering van GitHub’s MCP Registry in september 2025
    - **Probleemanalyse**: Gedetailleerde onderbouwing van gefragmenteerde MCP server ontdekking en deployment uitdagingen
    - **Oplossingsarchitectuur**: GitHub's gecentraliseerde registry benadering met één-klik VS Code installatie
    - **Zakelijke Impact**: Meetbare verbeteringen in onboarding en productiviteit van ontwikkelaars
    - **Strategische Waarde**: Focus op modulaire agent deployment en interoperabiliteit tussen tools
    - **Ecosysteemontwikkeling**: Positionering als fundamenteel platform voor agentgebaseerde integratie
  - **Verbeterde Case Study Structuur**: Alle zeven case studies bijgewerkt met consistente formattering en uitgebreide beschrijvingen
    - Azure AI Travel Agents: nadruk op multi-agent orchestratie
    - Azure DevOps Integratie: focus op workflowautomatisering
    - Real-Time Documentretrieval: Python console client implementatie
    - Interactieve Studieplanner Generator: Chainlit conversational webapp
    - In-Editor Documentatie: VS Code en GitHub Copilot integratie
    - Azure API Management: enterprise API integratiepatronen
    - GitHub MCP Registry: Ecosysteemontwikkeling en community platform
  - **Uitgebreide Conclusie**: Herschreven conclusie met nadruk op zeven case studies die meerdere MCP implementatiedimensies beslaan
    - Enterprise integratie, multi-agent orchestratie, ontwikkelaarproductiviteit,
    - Ecosysteemontwikkeling, educatieve toepassingen categorisatie
    - Uitgebreide inzichten in architectuurpatronen, implementatiestrategieën en best practices
    - Nadruk op MCP als volwassen, productieklare protocol

#### Studiehandleiding Updates (study_guide.md)
- **Visuele Curriculumkaart**: Mindmap bijgewerkt met GitHub MCP Registry in Case Studies sectie
- **Case Studies Beschrijving**: Van algemene beschrijvingen naar gedetailleerde uitsplitsing van zeven uitgebreide case studies
- **Repository Structuur**: Sectie 10 bijgewerkt voor volledige case study dekking met specifieke implementatiedetails
- **Changelog Integratie**: 26 september 2025 toegevoegd met documentatie van GitHub MCP Registry toevoeging en case study verbeteringen
- **Datumupdates**: Voettekst timestamp geactualiseerd naar nieuwste revisie (26 september 2025)

### Documentatie Kwaliteitsverbeteringen
- **Consistentieverbetering**: Gestandaardiseerde case study formatting en structuur over alle zeven voorbeelden
- **Omvattende Dekking**: Case studies omvatten nu enterprise-, ontwikkelaarproductiviteit- en ecosysteemontwikkelingsscenario’s
- **Strategische Positionering**: Verbeterde focus op MCP als fundamenteel platform voor agent-gebaseerde systeemdeployments
- **Resource Integratie**: Aanvullende bronnen bijgewerkt met GitHub MCP Registry link

## 15 september 2025

### Geavanceerde Onderwerpen Uitbreiding - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Nieuwe Geavanceerde Implementatiehandleiding
- **README.md**: Volledige implementatiehandleiding voor aangepaste MCP transportmechanismen
  - **Azure Event Grid Transport**: Uitgebreide serverless event-gedreven transportimplementatie
    - C#, TypeScript en Python voorbeelden met Azure Functions integratie
    - Event-gedreven architectuurpatronen voor schaalbare MCP oplossingen
    - Webhook ontvangers en push-based berichtafhandeling
  - **Azure Event Hubs Transport**: High-throughput streaming transportimplementatie
    - Real-time streamingcapabilities voor low-latency scenario's
    - Partitioneringsstrategieën en checkpoint management
    - Message batching en prestatie-optimalisatie
  - **Enterprise Integratiepatronen**: Productieklare architectuurexemplaren
    - Gedistribueerde MCP verwerking over meerdere Azure Functions
    - Hybride transportarchitecturen die meerdere transporttypes combineren
    - Berichtduurzaamheid, betrouwbaarheid en foutafhandelingsstrategieën
  - **Beveiliging & Monitoring**: Azure Key Vault integratie en observeerbaarheidspatronen
    - Managed identity authenticatie en least privilege toegang
    - Application Insights telemetrie en prestatiemonitoring
    - Circuit breakers en tolerantiepatronen voor fouten
  - **Testframeworks**: Omvattende teststrategieën voor custom transports
    - Unit testen met test doubles en mocking frameworks
    - Integratietesten met Azure Test Containers
    - Prestatie- en load testing overwegingen

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Ontstaan AI Discipline
- **README.md**: Uitgebreide verkenning van context engineering als opkomend vakgebied
  - **Kernprincipes**: Volledige contextdeling, actiebesluitbewustzijn en contextwindowbeheer
  - **MCP Protocol Afstemming**: Hoe MCP design context engineering uitdagingen adresseert
    - Beperkingen van context window en progressieve laadstrategieën
    - Relevantiebepaling en dynamische contextopvraging
    - Multi-modale contextverwerking en beveiligingsoverwegingen
  - **Implementatiebenaderingen**: Single-threaded versus multi-agent architecturen
    - Context chunking en prioriteringstechnieken
    - Progressief laden van context en compressiestrategieën
    - Gelaagde contextbenaderingen en retrievaloptimalisaties
  - **Meetkader**: Ontwikkelende meetmethoden voor contexteffectiviteit evaluatie
    - Input efficiëntie, prestatie, kwaliteit en gebruikerservaring
    - Experimentele methoden voor contextoptimalisatie
    - Faalanalyse en verbetermethodologieën

#### Curriculum Navigatie Updates (README.md)
- **Verbeterde Module Structuur**: Curriculummatrix bijgewerkt met nieuwe geavanceerde onderwerpen
  - Toevoeging van Context Engineering (5.14) en Custom Transport (5.15)
  - Consistente opmaak en navigatielinks door alle modules
  - Bijgewerkte beschrijvingen die huidige inhoudsomvang reflecteren

### Directory Structuur Verbeteringen
- **Naamgeving Standaardisatie**: "mcp transport" hernoemd naar "mcp-transport" voor consistentie met andere advanced topic mappen
- **Contentorganisatie**: Alle 05-AdvancedTopics mappen volgen nu consistente naamgevingspatroon (mcp-[onderwerp])

### Documentatie Kwaliteitsverbeteringen
- **MCP Specificatie Afstemming**: Alle nieuwe inhoud verwijst naar MCP Specificatie 2025-06-18
- **Meertalige Voorbeelden**: Uitgebreide codevoorbeelden in C#, TypeScript en Python
- **Enterprise Focus**: Productieklare patronen en Azure cloud integratie doorlopend
- **Visuele Documentatie**: Mermaid diagrammen voor architectuur- en flowvisualisatie

## 18 augustus 2025

### Uitgebreide Documentatie Update - MCP 2025-06-18 Standaarden

#### MCP Beveiligingsrichtlijnen (02-Security/) - Volledige Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Complete herschrijving afgestemd op MCP Specificatie 2025-06-18  
  - **Verplichte Vereisten**: Toegevoegd expliciete MOET/MOET NIET vereisten uit officiële specificatie met duidelijke visuele indicatoren  
  - **12 Kernbeveiligingspraktijken**: Herstructureerd van 15-items lijst naar uitgebreide beveiligingsdomeinen  
    - Tokenbeveiliging & Authenticatie met integratie van externe identiteitsprovider  
    - Sessiebeheer & Transportbeveiliging met cryptografische vereisten  
    - AI-Specifieke Dreigingsbeveiliging met Microsoft Prompt Shields integratie  
    - Toegangscontrole & Machtigingen met principe van minste privileges  
    - Inhoudsveiligheid & Monitoring met Azure Content Safety integratie  
    - Leveringsketenbeveiliging met uitgebreide componentverificatie  
    - OAuth-beveiliging & Confused Deputy Preventie met PKCE-implementatie  
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden  
    - Compliance & Governance met wettelijke afstemming  
    - Geavanceerde Beveiligingscontroles met zero trust architectuur  
    - Microsoft Beveiligingsecosysteem Integratie met uitgebreide oplossingen  
    - Continue Beveiligingsevolutie met adaptieve praktijken  
  - **Microsoft Beveiligingsoplossingen**: Verbeterde integratierichtlijnen voor Prompt Shields, Azure Content Safety, Entra ID, en GitHub Advanced Security  
  - **Implementatieresources**: Gecategoriseerde uitgebreide resource-links per Officiële MCP-documentatie, Microsoft Beveiligingsoplossingen, Beveiligingsstandaarden en Implementatiehandleidingen  

#### Geavanceerde Beveiligingscontroles (02-Security/) - Enterprise Implementatie  
- **MCP-SECURITY-CONTROLS-2025.md**: Complete herziening met beveiligingsframework op ondernemingsniveau  
  - **9 Uitgebreide Beveiligingsdomeinen**: Uitgebreid van basiscontroles naar gedetailleerd enterprise-framework  
    - Geavanceerde Authenticatie & Autorisatie met Microsoft Entra ID integratie  
    - Tokenbeveiliging & Anti-Passthrough Controles met uitgebreide validatie  
    - Sessiebeveiligingscontroles met hijackingpreventie  
    - AI-Specifieke Beveiligingscontroles met promptinjectie en toolvergiftigingspreventie  
    - Confused Deputy Attack Preventie met OAuth proxy-beveiliging  
    - Tool-uitvoeringsbeveiliging met sandboxing en isolatie  
    - Leveringsketenbeveiligingscontroles met afhankelijkheidsverificatie  
    - Monitoring- & Detectiecontroles met SIEM-integratie  
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden  
  - **Implementatievoorbeelden**: Toegevoegd gedetailleerde YAML-configuratieblokken en codevoorbeelden  
  - **Microsoft Oplossingenintegratie**: Uitgebreide dekking van Azure beveiligingsservices, GitHub Advanced Security, en enterprise identiteitsbeheer  

#### Geavanceerde Onderwerpen Beveiliging (05-AdvancedTopics/mcp-security/) - Productieklaar Implementatie  
- **README.md**: Complete herschrijving voor enterprise beveiligingsimplementatie  
  - **Afstemming op huidige specificatie**: Bijgewerkt naar MCP Specificatie 2025-06-18 met verplichte beveiligingseisen  
  - **Verbeterde authenticatie**: Microsoft Entra ID integratie met uitgebreide .NET en Java Spring Security voorbeelden  
  - **AI-beveiligingsintegratie**: Implementatie van Microsoft Prompt Shields en Azure Content Safety met gedetailleerde Python voorbeelden  
  - **Geavanceerde dreigingsmitigatie**: Uitgebreide implementatievoorbeelden voor  
    - Confused Deputy Attack Preventie met PKCE en gebruikersconsentvalidatie  
    - Token Passthrough Preventie met audience validatie en veilig tokenbeheer  
    - Sessie-hijackingpreventie met cryptografische binding en gedragsanalyse  
  - **Enterprise beveiligingsintegratie**: Azure Application Insights monitoring, dreigingsdetectiepijplijnen en leveringsketenbeveiliging  
  - **Implementatiecontrolelijst**: Duidelijke verplichte versus aanbevolen beveiligingscontroles met voordelen van Microsoft beveiligingsecosysteem  

### Documentatiekwaliteit & Standaardafstemming  
- **Specificatieverwijzingen**: Alle verwijzingen bijgewerkt naar actuele MCP Specificatie 2025-06-18  
- **Microsoft Beveiligingsecosysteem**: Verbeterde integratierichtlijnen door alle beveiligingsdocumentatie  
- **Praktische Implementatie**: Toegevoegd gedetailleerde codevoorbeelden in .NET, Java en Python met enterprise patronen  
- **Resourceorganisatie**: Uitgebreide categorisering van officiële documentatie, beveiligingsstandaarden en implementatiehandleidingen  
- **Visuele Indicatoren**: Duidelijke markering van verplichte vereisten versus aanbevolen praktijken  

#### Kernconcepten (01-CoreConcepts/) - Complete Modernisering  
- **Protocolversieupdate**: Geüpdatet naar verwijzing naar actuele MCP Specificatie 2025-06-18 met datumbased versiebeheer (YYYY-MM-DD formaat)  
- **Architectuurverbetering**: Verbeterde beschrijvingen van Hosts, Clients en Servers ten behoeve van actuele MCP architectuurpatronen  
  - Hosts nu duidelijk gedefinieerd als AI-applicaties die meerdere MCP clientverbindingen coördineren  
  - Clients beschreven als protocolkoppelingen die één-op-één serverrelaties onderhouden  
  - Servers uitgebreid met lokale versus remote implementatiescenario’s  
- **Primitiefherstructurering**: Complete herziening van server- en clientprimitieven  
  - Serverprimitieven: Resources (gegevensbronnen), Prompts (sjablonen), Tools (uitvoerbare functies) met gedetailleerde uitleg en voorbeelden  
  - Clientprimitieven: Sampling (LLM-afrondingen), Elicitation (gebruikersinvoer), Logging (debugging/monitoring)  
  - Geüpdatet met actuele discovery (`*/list`), retrieval (`*/get`) en uitvoering (`*/call`) methodepatronen  
- **Protocolarchitectuur**: Geïntroduceerd tweelaagsarchitectuurmodel  
  - Datalayer: JSON-RPC 2.0 basis met levenscyclusbeheer en primitieven  
  - Transportlayer: STDIO (lokaal) en Streamable HTTP met SSE (remote) transportmechanismen  
- **Beveiligingsframework**: Uitgebreide beveiligingsprincipes inclusief expliciete gebruikersconsent, dataprivacybescherming, tool-uitvoeringsveiligheid en transportlaagbeveiliging  
- **Communicatiepatronen**: Geüpdatete protocolberichten die initialisatie-, ontdekking-, uitvoering- en notificatiestromen tonen  
- **Codevoorbeelden**: Vernieuwde multi-taal voorbeelden (.NET, Java, Python, JavaScript) om MCP SDK-patronen te weerspiegelen  

#### Beveiliging (02-Security/) - Uitgebreide beveiligingsherziening  
- **Standaardafstemming**: Volledige afstemming op MCP Specificatie 2025-06-18 beveiligingseisen  
- **Authenticatie-evolutie**: Gedocumenteerde evolutie van aangepaste OAuth-servers naar externe identiteitsproviderdelegatie (Microsoft Entra ID)  
- **AI-Specifieke Dreigingsanalyse**: Uitgebreide dekking van moderne AI-aanvalsvectoren  
  - Gedetailleerde promptinjectie-aanvalsscenario’s met praktijkvoorbeelden  
  - Toolvergiftigingsmechanismen en “rug pull” aanvalspatronen  
  - Contextvenstervergiftiging en modelverwarringsaanvallen  
- **Microsoft AI Beveiligingsoplossingen**: Uitgebreide dekking van Microsoft beveiligingsecosysteem  
  - AI Prompt Shields met geavanceerde detectie, spotlighting en delimitertechnieken  
  - Azure Content Safety integratiepatronen  
  - GitHub Advanced Security voor leveringsketenbescherming  
- **Geavanceerde Dreigingsmitigatie**: Gedetailleerde beveiligingscontroles voor  
  - Sessie-hijacking met MCP-specifieke aanvalsscenario’s en cryptografische sessie-ID vereisten  
  - Confused deputy-problemen in MCP proxy-scenario’s met expliciete consentvereisten  
  - Token passthrough-kwetsbaarheden met verplichte validatiecontroles  
- **Leveringsketenbeveiliging**: Uitgebreide AI-leveringsketendekking inclusief foundation-modellen, embeddingsdiensten, contextproviders en API’s van derden  
- **Foundation Security**: Verbeterde integratie met enterprise beveiligingspatronen inclusief zero trust architectuur en Microsoft beveiligingsecosysteem  
- **Resourceorganisatie**: Gecategoriseerde uitgebreide resource-links per type (Officiële Docs, Standaarden, Onderzoek, Microsoft Oplossingen, Implementatiehandleidingen)  

### Documentatiekwaliteitsverbeteringen  
- **Gestructureerde Leerdoelen**: Verbeterde leerdoelen met specifieke, uitvoerbare resultaten  
- **Kruisverwijzingen**: Toegevoegd links tussen gerelateerde beveiligings- en kernconceptonderwerpen  
- **Actuele Informatie**: Alle datumverwijzingen en specificatielinks geüpdatet naar actuele standaarden  
- **Implementatierichtlijnen**: Toegevoegd specifieke, uitvoerbare implementatierichtlijnen door beide secties heen  

## 16 juli 2025  

### README en Navigatieverbeteringen  
- Volledig herontworpen curriculumnavigatie in README.md  
- Vervangen van `<details>` tags door toegankelijker tabelgebaseerd formaat  
- Gemaakt alternatieve lay-outopties in nieuwe map "alternative_layouts"  
- Toegevoegd kaartgebaseerde, tabbladstijl- en accordionstijl navigatievoorbeelden  
- Bijgewerkt sectie repositorystructuur met alle laatste bestanden  
- Verbeterde sectie "Hoe Gebruik Je Dit Curriculum" met duidelijke aanbevelingen  
- MCP specificatielinks bijgewerkt naar correcte URL’s  
- Toegevoegd Context Engineering sectie (5.14) aan curriculumsstructuur  

### Studiegidsupdates  
- Volledig herzien van studiegids om te aligneren met huidige repositorystructuur  
- Toegevoegd nieuwe secties voor MCP Clients en Tools, en Populaire MCP Servers  
- Bijgewerkt de Visuele Curriculumkaart om alle onderwerpen accuraat weer te geven  
- Verbeterde beschrijvingen van Geavanceerde Onderwerpen om alle gespecialiseerde gebieden te omvatten  
- Bijgewerkt sectie Case Studies om actuele voorbeelden weer te geven  
- Toegevoegd deze uitgebreide changelog  

### Community Bijdragen (06-CommunityContributions/)  
- Toegevoegd gedetailleerde informatie over MCP-servers voor beeldgeneratie  
- Toegevoegd uitgebreide sectie over het gebruik van Claude in VSCode  
- Toegevoegd Cline terminal client setup en gebruiksinstructies  
- Bijgewerkt MCP clientsectie met alle populaire clientopties  
- Verbeterde bijdragevoorbeelden met nauwkeurigere codesamples  

### Geavanceerde Onderwerpen (05-AdvancedTopics/)  
- Alle gespecialiseerde onderwerpmappen georganiseerd met consistente naamgeving  
- Toegevoegd context engineering materialen en voorbeelden  
- Toegevoegd Foundry agent integratiedocumentatie  
- Verbeterde integratiebeveiligingsdocumentatie voor Entra ID  

## 11 juni 2025  

### Initiële Creatie  
- Eerste versie van MCP voor Beginners curriculum uitgebracht  
- Basisstructuur voor alle 10 hoofdsecties gemaakt  
- Visuele Curriculumkaart voor navigatie geïmplementeerd  
- Initiële voorbeeldprojecten toegevoegd in meerdere programmeertalen  

### Aan de Slag (03-GettingStarted/)  
- Eerste serverimplementatievoorbeelden gemaakt  
- Clientontwikkelingsrichtlijnen toegevoegd  
- Instructies voor LLM-clientintegratie toegevoegd  
- Documentatie voor VS Code-integratie toegevoegd  
- Server-Sent Events (SSE) servervoorbeelden geïmplementeerd  

### Kernconcepten (01-CoreConcepts/)  
- Gedetailleerde uitleg van client-server architectuur toegevoegd  
- Documentatie over belangrijke protocolcomponenten gemaakt  
- Communicatiepatronen in MCP gedocumenteerd  

## 23 mei 2025  

### Repositorystructuur  
- Repository geïnitieerd met basisfolderstructuur  
- README-bestanden gemaakt voor elke hoofdsectie  
- Vertaalinfrastructuur opgezet  
- Beeldassets en diagrammen toegevoegd  

### Documentatie  
- Initiële README.md met curriculumoverzicht gemaakt  
- CODE_OF_CONDUCT.md en SECURITY.md toegevoegd  
- SUPPORT.md opgezet met richtlijnen voor hulp  
- Voorlopige studiegidsstructuur gemaakt  

## 15 april 2025  

### Planning en Framework  
- Initiële planning voor MCP voor Beginners curriculum  
- Leerdoelen en doelgroep gedefinieerd  
- 10-secties structuur van het curriculum geschetst  
- Conceptueel raamwerk voor voorbeelden en casestudy’s ontwikkeld  
- Initiële prototypevoorbeelden van kernconcepten gemaakt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
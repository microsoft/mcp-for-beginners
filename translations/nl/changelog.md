# Wijzigingslogboek: MCP voor Beginners Curriculum

Dit document dient als een overzicht van alle belangrijke wijzigingen die zijn aangebracht in het Model Context Protocol (MCP) voor Beginners curriculum. Wijzigingen worden gedocumenteerd in omgekeerde chronologische volgorde (nieuwste wijzigingen eerst).

## 18 december 2025

### Update Beveiligingsdocumentatie - MCP Specificatie 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Update Specificatieversie
- **Protocolversie Update**: Bijgewerkt om te verwijzen naar de nieuwste MCP Specificatie 2025-11-25 (uitgebracht op 25 november 2025)
  - Alle verwijzingen naar specificatieversies bijgewerkt van 2025-06-18 naar 2025-11-25
  - Documentdatumverwijzingen bijgewerkt van 18 augustus 2025 naar 18 december 2025
  - Gecontroleerd dat alle specificatie-URL's verwijzen naar de actuele documentatie
- **Inhoudsvalidatie**: Uitgebreide validatie van beveiligingsbest practices tegen de nieuwste standaarden
  - **Microsoft Security Solutions**: Gecontroleerd op actuele terminologie en links voor Prompt Shields (voorheen "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID en Azure Key Vault
  - **OAuth 2.1 Beveiliging**: Bevestigde afstemming met de nieuwste OAuth beveiligingsbest practices
  - **OWASP Standaarden**: Gevalideerd dat OWASP Top 10 voor LLMs verwijzingen actueel blijven
  - **Azure Services**: Gecontroleerd alle Microsoft Azure documentatielinks en best practices
- **Standaardafstemming**: Alle genoemde beveiligingsstandaarden bevestigd actueel
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure beveiligings- en compliancekaders
- **Implementatieressources**: Gevalideerd alle implementatiegidslinks en bronnen
  - Azure API Management authenticatiepatronen
  - Microsoft Entra ID integratiehandleidingen
  - Azure Key Vault geheimenbeheer
  - DevSecOps pipelines en monitoringoplossingen

### Kwaliteitsborging Documentatie
- **Specificatiecompliance**: Zeker gesteld dat alle verplichte MCP beveiligingseisen (MUST/MUST NOT) overeenkomen met de nieuwste specificatie
- **Bronnenactualiteit**: Gecontroleerd alle externe links naar Microsoft documentatie, beveiligingsstandaarden en implementatiegidsen
- **Best Practices Dekking**: Bevestigde uitgebreide dekking van authenticatie, autorisatie, AI-specifieke bedreigingen, supply chain beveiliging en enterprise patronen

## 6 oktober 2025

### Uitbreiding Sectie Aan de Slag – Geavanceerd Servergebruik & Eenvoudige Authenticatie

#### Geavanceerd Servergebruik (03-GettingStarted/10-advanced)
- **Nieuw Hoofdstuk Toegevoegd**: Invoering van een uitgebreide gids voor geavanceerd MCP servergebruik, met zowel reguliere als low-level serverarchitecturen.
  - **Reguliere vs. Low-Level Server**: Gedetailleerde vergelijking en codevoorbeelden in Python en TypeScript voor beide benaderingen.
  - **Handler-Based Ontwerp**: Uitleg over handler-gebaseerd beheer van tools/resources/prompts voor schaalbare, flexibele serverimplementaties.
  - **Praktische Patronen**: Praktijksituaties waarin low-level serverpatronen voordelig zijn voor geavanceerde functies en architectuur.

#### Eenvoudige Authenticatie (03-GettingStarted/11-simple-auth)
- **Nieuw Hoofdstuk Toegevoegd**: Stapsgewijze handleiding voor het implementeren van eenvoudige authenticatie in MCP-servers.
  - **Auth Concepten**: Duidelijke uitleg over authenticatie versus autorisatie, en credentialbeheer.
  - **Basis Auth Implementatie**: Middleware-gebaseerde authenticatiepatronen in Python (Starlette) en TypeScript (Express), met codevoorbeelden.
  - **Doorontwikkeling naar Geavanceerde Beveiliging**: Richtlijnen om te starten met eenvoudige auth en door te groeien naar OAuth 2.1 en RBAC, met verwijzingen naar geavanceerde beveiligingsmodules.

Deze toevoegingen bieden praktische, hands-on begeleiding voor het bouwen van robuustere, veiligere en flexibelere MCP-serverimplementaties, die fundamentele concepten verbinden met geavanceerde productiepatronen.

## 29 september 2025

### MCP Server Database Integratie Labs - Uitgebreid Hands-On Leertraject

#### 11-MCPServerHandsOnLabs - Nieuwe Complete Database Integratie Curriculum
- **Complete 13-Lab Leertraject**: Toegevoegd uitgebreid hands-on curriculum voor het bouwen van productieklare MCP-servers met PostgreSQL database-integratie
  - **Praktijkvoorbeeld**: Zava Retail analytics use case die enterprise-grade patronen demonstreert
  - **Gestructureerde Leerprogressie**:
    - **Labs 00-03: Fundamenten** - Introductie, Kernarchitectuur, Beveiliging & Multi-Tenancy, Omgevingssetup
    - **Labs 04-06: Bouwen van de MCP Server** - Databaseontwerp & Schema, MCP Server Implementatie, Toolontwikkeling  
    - **Labs 07-09: Geavanceerde Functies** - Semantische Zoekintegratie, Testen & Debuggen, VS Code Integratie
    - **Labs 10-12: Productie & Best Practices** - Deploymentsstrategieën, Monitoring & Observability, Best Practices & Optimalisatie
  - **Enterprise Technologieën**: FastMCP framework, PostgreSQL met pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Geavanceerde Functies**: Row Level Security (RLS), semantische zoekopdrachten, multi-tenant data toegang, vector embeddings, realtime monitoring

#### Terminologiestandaardisatie - Module naar Lab Conversie
- **Uitgebreide Documentatie-update**: Systematisch alle README-bestanden in 11-MCPServerHandsOnLabs bijgewerkt om "Lab" terminologie te gebruiken in plaats van "Module"
  - **Sectiekoppen**: "What This Module Covers" gewijzigd naar "What This Lab Covers" in alle 13 labs
  - **Inhoudsbeschrijving**: "This module provides..." veranderd in "This lab provides..." door de hele documentatie
  - **Leerdoelen**: "By the end of this module..." aangepast naar "By the end of this lab..."
  - **Navigatielinks**: Alle "Module XX:" verwijzingen omgezet naar "Lab XX:" in kruisverwijzingen en navigatie
  - **Volgtracking**: "After completing this module..." aangepast naar "After completing this lab..."
  - **Technische Verwijzingen Behouden**: Python moduleverwijzingen in configuratiebestanden behouden (bijv. `"module": "mcp_server.main"`)

#### Verbetering Studiegids (study_guide.md)
- **Visuele Curriculumkaart**: Nieuwe sectie "11. Database Integration Labs" toegevoegd met uitgebreide labstructuurvisualisatie
- **Repositorystructuur**: Bijgewerkt van tien naar elf hoofdsecties met gedetailleerde beschrijving van 11-MCPServerHandsOnLabs
- **Leertrajectinstructies**: Navigatie-instructies uitgebreid om secties 00-11 te omvatten
- **Technologiedekking**: Toegevoegd FastMCP, PostgreSQL, Azure services integratiedetails
- **Leerresultaten**: Benadrukt productieklare serverontwikkeling, database-integratiepatronen en enterprise beveiliging

#### Verbetering Hoofd README-structuur
- **Lab-gebaseerde Terminologie**: Hoofd README.md in 11-MCPServerHandsOnLabs bijgewerkt om consequent "Lab" structuur te gebruiken
- **Leertrajectorganisatie**: Duidelijke progressie van fundamentele concepten via geavanceerde implementatie naar productie-deployment
- **Praktijkgericht**: Focus op praktische, hands-on leerervaring met enterprise-grade patronen en technologieën

### Verbeteringen Documentatiekwaliteit & Consistentie
- **Hands-On Leerbenadering**: Praktische, lab-gebaseerde aanpak door de hele documentatie versterkt
- **Enterprise Patronen Focus**: Productieklare implementaties en enterprise beveiliging benadrukt
- **Technologie-integratie**: Uitgebreide dekking van moderne Azure services en AI-integratiepatronen
- **Leerprogressie**: Duidelijk, gestructureerd pad van basisconcepten tot productie-deployment

## 26 september 2025

### Verbetering Case Studies - GitHub MCP Registry Integratie

#### Case Studies (09-CaseStudy/) - Focus op Ecosysteemontwikkeling
- **README.md**: Grote uitbreiding met uitgebreide GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Nieuwe uitgebreide case study over de lancering van GitHub's MCP Registry in september 2025
    - **Probleemanalyse**: Gedetailleerde analyse van gefragmenteerde MCP server discovery en deployment uitdagingen
    - **Oplossingsarchitectuur**: GitHub's gecentraliseerde registry aanpak met one-click VS Code installatie
    - **Zakelijke Impact**: Meetbare verbeteringen in developer onboarding en productiviteit
    - **Strategische Waarde**: Focus op modulaire agent deployment en cross-tool interoperabiliteit
    - **Ecosysteemontwikkeling**: Positionering als fundamenteel platform voor agentische integratie
  - **Verbeterde Case Study Structuur**: Alle zeven case studies bijgewerkt met consistente opmaak en uitgebreide beschrijvingen
    - Azure AI Travel Agents: nadruk op multi-agent orkestratie
    - Azure DevOps Integratie: focus op workflow automatisering
    - Real-Time Document Retrieval: Python console client implementatie
    - Interactieve Studieplanner Generator: Chainlit conversational webapp
    - In-Editor Documentatie: VS Code en GitHub Copilot integratie
    - Azure API Management: enterprise API integratiepatronen
    - GitHub MCP Registry: ecosysteemontwikkeling en community platform
  - **Uitgebreide Conclusie**: Herschreven conclusie met nadruk op zeven case studies die meerdere MCP implementatiedimensies beslaan
    - Enterprise Integratie, Multi-Agent Orkestratie, Developer Productiviteit
    - Ecosysteemontwikkeling, Educatieve Toepassingen categorisering
    - Verdiepte inzichten in architectuurpatronen, implementatiestrategieën en best practices
    - Nadruk op MCP als volwassen, productieklare protocol

#### Updates Studiegids (study_guide.md)
- **Visuele Curriculumkaart**: Mindmap bijgewerkt om GitHub MCP Registry op te nemen in Case Studies sectie
- **Case Studies Beschrijving**: Verbeterd van generieke beschrijvingen naar gedetailleerde uitsplitsing van zeven uitgebreide case studies
- **Repositorystructuur**: Sectie 10 bijgewerkt om uitgebreide case study dekking met specifieke implementatiedetails weer te geven
- **Changelog Integratie**: Invoer van 26 september 2025 toegevoegd met documentatie van GitHub MCP Registry toevoeging en case study verbeteringen
- **Datumupdates**: Voettekst tijdstempel bijgewerkt naar laatste revisie (26 september 2025)

### Verbeteringen Documentatiekwaliteit
- **Consistentieverbetering**: Gestandaardiseerde case study opmaak en structuur over alle zeven voorbeelden
- **Uitgebreide Dekking**: Case studies bestrijken nu enterprise, developer productiviteit en ecosysteemontwikkelingsscenario's
- **Strategische Positionering**: Versterkte focus op MCP als fundamenteel platform voor agentische systeemdeployment
- **Bronintegratie**: Aanvullende bronnen bijgewerkt met GitHub MCP Registry link

## 15 september 2025

### Uitbreiding Geavanceerde Onderwerpen - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Nieuwe Geavanceerde Implementatiegids
- **README.md**: Volledige implementatiegids voor aangepaste MCP transportmechanismen
  - **Azure Event Grid Transport**: Uitgebreide serverless event-driven transportimplementatie
    - C#, TypeScript en Python voorbeelden met Azure Functions integratie
    - Event-driven architectuurpatronen voor schaalbare MCP-oplossingen
    - Webhook ontvangers en push-gebaseerde berichtverwerking
  - **Azure Event Hubs Transport**: High-throughput streaming transportimplementatie
    - Real-time streaming mogelijkheden voor low-latency scenario's
    - Partitioneringsstrategieën en checkpointbeheer
    - Berichtbatching en prestatieoptimalisatie
  - **Enterprise Integratiepatronen**: Productieklare architectuurexamples
    - Gedistribueerde MCP verwerking over meerdere Azure Functions
    - Hybride transportarchitecturen die meerdere transporttypes combineren
    - Berichtduurzaamheid, betrouwbaarheid en foutafhandelingsstrategieën
  - **Beveiliging & Monitoring**: Azure Key Vault integratie en observability patronen
    - Managed identity authenticatie en least privilege toegang
    - Application Insights telemetrie en prestatiemonitoring
    - Circuit breakers en fouttolerantiepatronen
  - **Testframeworks**: Uitgebreide teststrategieën voor custom transports
    - Unittesten met test doubles en mocking frameworks
    - Integratietesten met Azure Test Containers
    - Prestatie- en loadtesting overwegingen

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Opkomende AI Discipline
- **README.md**: Uitgebreide verkenning van context engineering als opkomend vakgebied
  - **Kernprincipes**: Volledige contextdeling, actie-besluitbewustzijn en context window management
  - **MCP Protocol Afstemming**: Hoe MCP ontwerp context engineering uitdagingen adresseert
    - Beperkingen van context windows en progressieve laadstrategieën
    - Relevantiebepaling en dynamische contextopvraging
    - Multi-modale contextverwerking en beveiligingsoverwegingen
  - **Implementatiebenaderingen**: Single-threaded versus multi-agent architecturen
    - Context chunking en prioriteringstechnieken
    - Progressieve contextlading en compressiestrategieën
    - Gelaagde contextbenaderingen en retrieval optimalisatie
  - **Meetkader**: Opkomende metrics voor evaluatie van contexteffectiviteit
    - Inputefficiëntie, prestaties, kwaliteit en gebruikerservaringsoverwegingen
    - Experimentele benaderingen voor contextoptimalisatie
    - Falanalyse en verbeteringsmethodologieën

#### Updates Curriculumnavigatie (README.md)
- **Verbeterde Modulstructuur**: Curriculumtabel bijgewerkt met nieuwe geavanceerde onderwerpen
  - Toegevoegd Context Engineering (5.14) en Custom Transport (5.15) vermeldingen
  - Consistente opmaak en navigatielinks over alle modules
  - Beschrijvingen bijgewerkt om huidige inhoudsomvang te weerspiegelen

### Verbeteringen Directorystructuur
- **Naamgevingsstandaardisatie**: "mcp transport" hernoemd naar "mcp-transport" voor consistentie met andere geavanceerde onderwerpmappen
- **Inhoudsorganisatie**: Alle 05-AdvancedTopics mappen volgen nu een consistent naamgevingspatroon (mcp-[topic])

### Verbeteringen Documentatiekwaliteit
- **MCP Specificatie Afstemming**: Alle nieuwe inhoud verwijst naar huidige MCP Specificatie 2025-06-18
- **Meertalige Voorbeelden**: Uitgebreide codevoorbeelden in C#, TypeScript en Python
- **Enterprise Focus**: Productieklare patronen en Azure cloud integratie doorlopend
- **Visuele Documentatie**: Mermaid diagrammen voor architectuur- en flowvisualisatie

## 18 augustus 2025

### Uitgebreide Documentatie-update - MCP 2025-06-18 Standaarden

#### MCP Security Best Practices (02-Security/) - Volledige Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Volledige herschrijving afgestemd op MCP Specificatie 2025-06-18
  - **Verplichte Vereisten**: Toegevoegd expliciete MOET/MOET NIET vereisten uit officiële specificatie met duidelijke visuele indicatoren
  - **12 Kernbeveiligingspraktijken**: Hervormd van 15-puntenlijst naar uitgebreide beveiligingsdomeinen
    - Tokenbeveiliging & Authenticatie met integratie van externe identiteitsprovider
    - Sessiebeheer & Transportbeveiliging met cryptografische vereisten
    - AI-specifieke Dreigingsbescherming met integratie van Microsoft Prompt Shields
    - Toegangscontrole & Machtigingen met principe van minste privilege
    - Inhoudsveiligheid & Monitoring met integratie van Azure Content Safety
    - Leveringsketenbeveiliging met uitgebreide componentverificatie
    - OAuth-beveiliging & Confused Deputy Preventie met PKCE-implementatie
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden
    - Naleving & Governance met afstemming op regelgeving
    - Geavanceerde Beveiligingscontroles met zero trust architectuur
    - Integratie van Microsoft Beveiligingsecosysteem met uitgebreide oplossingen
    - Continue Beveiligingsevolutie met adaptieve praktijken
  - **Microsoft Beveiligingsoplossingen**: Verbeterde integratierichtlijnen voor Prompt Shields, Azure Content Safety, Entra ID en GitHub Advanced Security
  - **Implementatieresources**: Gecategoriseerde uitgebreide resource-links per Officiële MCP Documentatie, Microsoft Beveiligingsoplossingen, Beveiligingsstandaarden en Implementatiehandleidingen

#### Geavanceerde Beveiligingscontroles (02-Security/) - Enterprise Implementatie
- **MCP-SECURITY-CONTROLS-2025.md**: Volledige herziening met enterprise-grade beveiligingsraamwerk
  - **9 Uitgebreide Beveiligingsdomeinen**: Uitgebreid van basiscontroles naar gedetailleerd enterprise-raamwerk
    - Geavanceerde Authenticatie & Autorisatie met Microsoft Entra ID integratie
    - Tokenbeveiliging & Anti-Passthrough Controles met uitgebreide validatie
    - Sessiebeveiligingscontroles met hijackingpreventie
    - AI-specifieke Beveiligingscontroles met preventie van promptinjectie en toolvergiftiging
    - Confused Deputy Aanvalspreventie met OAuth proxy beveiliging
    - Tooluitvoeringsbeveiliging met sandboxing en isolatie
    - Leveringsketenbeveiligingscontroles met afhankelijkheidsverificatie
    - Monitoring & Detectiecontroles met SIEM-integratie
    - Incidentrespons & Herstel met geautomatiseerde mogelijkheden
  - **Implementatievoorbeelden**: Toegevoegd gedetailleerde YAML-configuratieblokken en codevoorbeelden
  - **Integratie Microsoft Oplossingen**: Uitgebreide dekking van Azure beveiligingsdiensten, GitHub Advanced Security en enterprise identiteitsbeheer

#### Geavanceerde Onderwerpen Beveiliging (05-AdvancedTopics/mcp-security/) - Productieklaar Implementatie
- **README.md**: Volledige herschrijving voor enterprise beveiligingsimplementatie
  - **Huidige Specificatie Afstemming**: Bijgewerkt naar MCP Specificatie 2025-06-18 met verplichte beveiligingseisen
  - **Verbeterde Authenticatie**: Microsoft Entra ID integratie met uitgebreide .NET en Java Spring Security voorbeelden
  - **AI Beveiligingsintegratie**: Microsoft Prompt Shields en Azure Content Safety implementatie met gedetailleerde Python voorbeelden
  - **Geavanceerde Dreigingsmitigatie**: Uitgebreide implementatievoorbeelden voor
    - Confused Deputy Aanvalspreventie met PKCE en gebruikersconsentvalidatie
    - Token Passthrough Preventie met audience validatie en veilig tokenbeheer
    - Sessiekapingpreventie met cryptografische binding en gedragsanalyse
  - **Enterprise Beveiligingsintegratie**: Azure Application Insights monitoring, dreigingsdetectiepijplijnen en leveringsketenbeveiliging
  - **Implementatiechecklist**: Duidelijke verplichte versus aanbevolen beveiligingscontroles met voordelen van Microsoft beveiligingsecosysteem

### Documentatiekwaliteit & Standaardafstemming
- **Specificatieverwijzingen**: Alle verwijzingen bijgewerkt naar huidige MCP Specificatie 2025-06-18
- **Microsoft Beveiligingsecosysteem**: Verbeterde integratierichtlijnen door alle beveiligingsdocumentatie heen
- **Praktische Implementatie**: Toegevoegd gedetailleerde codevoorbeelden in .NET, Java en Python met enterprise patronen
- **Resourceorganisatie**: Uitgebreide categorisering van officiële documentatie, beveiligingsstandaarden en implementatiehandleidingen
- **Visuele Indicatoren**: Duidelijke markering van verplichte vereisten versus aanbevolen praktijken


#### Kernconcepten (01-CoreConcepts/) - Volledige Modernisering
- **Protocolversie Update**: Bijgewerkt naar verwijzing naar huidige MCP Specificatie 2025-06-18 met datumgebaseerde versie (YYYY-MM-DD formaat)
- **Architectuurverbetering**: Verbeterde beschrijvingen van Hosts, Clients en Servers om huidige MCP architectuurpatronen te weerspiegelen
  - Hosts nu duidelijk gedefinieerd als AI-toepassingen die meerdere MCP clientverbindingen coördineren
  - Clients beschreven als protocolconnectoren die één-op-één serverrelaties onderhouden
  - Servers verbeterd met lokale versus remote implementatiescenario’s
- **Primitieve Hervorming**: Volledige herziening van server- en clientprimitieven
  - Serverprimitieven: Resources (gegevensbronnen), Prompts (sjablonen), Tools (uitvoerbare functies) met gedetailleerde uitleg en voorbeelden
  - Clientprimitieven: Sampling (LLM-completions), Elicitation (gebruikersinvoer), Logging (debuggen/monitoring)
  - Bijgewerkt met huidige discovery (`*/list`), retrieval (`*/get`) en execution (`*/call`) methodenpatronen
- **Protocolarchitectuur**: Geïntroduceerd tweelaags architectuurmodel
  - Datalayer: JSON-RPC 2.0 basis met levenscyclusbeheer en primitieven
  - Transportlaag: STDIO (lokaal) en Streamable HTTP met SSE (remote) transportmechanismen
- **Beveiligingsraamwerk**: Uitgebreide beveiligingsprincipes inclusief expliciete gebruikersconsent, gegevensprivacybescherming, tooluitvoeringsveiligheid en transportlaagbeveiliging
- **Communicatiepatronen**: Bijgewerkte protocolberichten tonen initialisatie-, discovery-, uitvoering- en notificatiestromen
- **Codevoorbeelden**: Vernieuwde meertalige voorbeelden (.NET, Java, Python, JavaScript) om huidige MCP SDK-patronen te weerspiegelen

#### Beveiliging (02-Security/) - Uitgebreide Beveiligingsherziening  
- **Standaardafstemming**: Volledige afstemming op MCP Specificatie 2025-06-18 beveiligingseisen
- **Authenticatie-evolutie**: Gedocumenteerde evolutie van aangepaste OAuth-servers naar delegatie van externe identiteitsprovider (Microsoft Entra ID)
- **AI-specifieke Dreigingsanalyse**: Verbeterde dekking van moderne AI-aanvalsvectoren
  - Gedetailleerde promptinjectie-aanvalscenario’s met praktijkvoorbeelden
  - Toolvergiftigingsmechanismen en "rug pull" aanvalspatronen
  - Contextwindowvergiftiging en modelverwarringsaanvallen
- **Microsoft AI Beveiligingsoplossingen**: Uitgebreide dekking van Microsoft beveiligingsecosysteem
  - AI Prompt Shields met geavanceerde detectie, spotlighting en delimiter-technieken
  - Azure Content Safety integratiepatronen
  - GitHub Advanced Security voor leveringsketenbescherming
- **Geavanceerde Dreigingsmitigatie**: Gedetailleerde beveiligingscontroles voor
  - Sessiekaping met MCP-specifieke aanvalscenario’s en cryptografische sessie-ID vereisten
  - Confused deputy-problemen in MCP proxy-scenario’s met expliciete consentvereisten
  - Token passthrough-kwetsbaarheden met verplichte validatiecontroles
- **Leveringsketenbeveiliging**: Uitgebreide AI-leveringsketendekking inclusief foundation models, embeddingsdiensten, contextproviders en third-party API’s
- **Foundation Security**: Verbeterde integratie met enterprise beveiligingspatronen inclusief zero trust architectuur en Microsoft beveiligingsecosysteem
- **Resourceorganisatie**: Gecategoriseerde uitgebreide resource-links per type (Officiële Docs, Standaarden, Onderzoek, Microsoft Oplossingen, Implementatiehandleidingen)

### Verbeteringen Documentatiekwaliteit
- **Gestructureerde Leerdoelen**: Verbeterde leerdoelen met specifieke, uitvoerbare resultaten 
- **Kruisverwijzingen**: Toegevoegd links tussen gerelateerde beveiligings- en kernconceptonderwerpen
- **Actuele Informatie**: Alle datumverwijzingen en specificatielinks bijgewerkt naar huidige standaarden
- **Implementatierichtlijnen**: Toegevoegd specifieke, uitvoerbare implementatierichtlijnen door beide secties heen

## 16 juli 2025

### README en Navigatieverbeteringen
- Volledig herontworpen curriculumnavigatie in README.md
- Vervangen van `<details>` tags door toegankelijker tabelgebaseerd formaat
- Alternatieve lay-outopties gemaakt in nieuwe map "alternative_layouts"
- Toegevoegd kaartgebaseerde, tabstijl- en accordeonstijl navigatievoorbeelden
- Bijgewerkte repositorystructuursectie met alle nieuwste bestanden
- Verbeterde sectie "Hoe gebruik je dit curriculum" met duidelijke aanbevelingen
- MCP specificatielinks bijgewerkt naar correcte URL’s
- Toegevoegd Context Engineering sectie (5.14) aan curriculumstructuur

### Studiegidsupdates
- Volledig herzien van studiegids om aan te sluiten bij huidige repositorystructuur
- Nieuwe secties toegevoegd voor MCP Clients en Tools, en Populaire MCP Servers
- Visual Curriculum Map bijgewerkt om alle onderwerpen nauwkeurig weer te geven
- Verbeterde beschrijvingen van Geavanceerde Onderwerpen om alle gespecialiseerde gebieden te dekken
- Case Studies sectie bijgewerkt met actuele voorbeelden
- Toegevoegd deze uitgebreide changelog

### Communitybijdragen (06-CommunityContributions/)
- Gedetailleerde informatie toegevoegd over MCP-servers voor beeldgeneratie
- Uitgebreide sectie toegevoegd over het gebruik van Claude in VSCode
- Cline terminal client setup en gebruiksinstructies toegevoegd
- MCP clientsectie bijgewerkt met alle populaire clientopties
- Verbeterde bijdragevoorbeelden met nauwkeurigere codevoorbeelden

### Geavanceerde Onderwerpen (05-AdvancedTopics/)
- Alle gespecialiseerde onderwerpmappen georganiseerd met consistente naamgeving
- Context engineering materialen en voorbeelden toegevoegd
- Foundry agent integratiedocumentatie toegevoegd
- Verbeterde Entra ID beveiligingsintegratiedocumentatie

## 11 juni 2025

### Initiële Creatie
- Eerste versie van MCP voor Beginners curriculum uitgebracht
- Basisstructuur gemaakt voor alle 10 hoofdsecties
- Visual Curriculum Map geïmplementeerd voor navigatie
- Initiële voorbeeldprojecten toegevoegd in meerdere programmeertalen

### Aan de Slag (03-GettingStarted/)
- Eerste serverimplementatievoorbeelden gemaakt
- Richtlijnen voor clientontwikkeling toegevoegd
- Instructies voor LLM clientintegratie opgenomen
- Documentatie voor VS Code integratie toegevoegd
- Server-Sent Events (SSE) servervoorbeelden geïmplementeerd

### Kernconcepten (01-CoreConcepts/)
- Gedetailleerde uitleg van client-serverarchitectuur toegevoegd
- Documentatie over belangrijke protocolcomponenten gemaakt
- Messagingpatronen in MCP gedocumenteerd

## 23 mei 2025

### Repositorystructuur
- Repository geïnitieerd met basis mappenstructuur
- README-bestanden gemaakt voor elke hoofdsectie
- Vertaalinfrastructuur opgezet
- Afbeeldingsassets en diagrammen toegevoegd

### Documentatie
- Initiële README.md met curriculumoverzicht gemaakt
- CODE_OF_CONDUCT.md en SECURITY.md toegevoegd
- SUPPORT.md opgezet met richtlijnen voor hulp
- Voorlopige studiegidsstructuur gemaakt

## 15 april 2025

### Planning en Raamwerk
- Initiële planning voor MCP voor Beginners curriculum
- Leerdoelen en doelgroep gedefinieerd
- 10-sectiestructuur van het curriculum geschetst
- Conceptueel raamwerk ontwikkeld voor voorbeelden en casestudies
- Initiële prototypevoorbeelden voor kernconcepten gemaakt

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Changelog: MCP for Beginners Curriculum

Dette dokument fungerer som en oversigt over alle væsentlige ændringer foretaget i Model Context Protocol (MCP) for Beginners pensum. Ændringer dokumenteres i omvendt kronologisk rækkefølge (nyeste ændringer først).

## 18. december 2025

### Opdatering af sikkerhedsdokumentation - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Opdatering af specifikationsversion
- **Protokolversionsopdatering**: Opdateret til at referere til seneste MCP Specification 2025-11-25 (udgivet 25. november 2025)
  - Opdateret alle specifikationsversionshenvisninger fra 2025-06-18 til 2025-11-25
  - Opdateret dokumentdatoer fra 18. august 2025 til 18. december 2025
  - Verificeret at alle specifikations-URL'er peger på aktuel dokumentation
- **Indholdsvalidering**: Omfattende validering af sikkerhedspraksis i forhold til seneste standarder
  - **Microsoft Security Solutions**: Verificeret aktuelle termer og links for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Security**: Bekræftet overensstemmelse med seneste OAuth sikkerhedspraksis
  - **OWASP Standards**: Valideret at OWASP Top 10 for LLMs referencer er opdaterede
  - **Azure Services**: Verificeret alle Microsoft Azure dokumentationslinks og bedste praksis
- **Standardoverensstemmelse**: Alle refererede sikkerhedsstandarder bekræftet aktuelle
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure sikkerheds- og compliance-rammer
- **Implementeringsressourcer**: Valideret alle implementeringsvejledninger og ressourcelinks
  - Azure API Management autentificeringsmønstre
  - Microsoft Entra ID integrationsvejledninger
  - Azure Key Vault secrets management
  - DevSecOps pipelines og overvågningsløsninger

### Dokumentationskvalitetssikring
- **Specifikationsoverholdelse**: Sikret at alle obligatoriske MCP sikkerhedskrav (MUST/MUST NOT) stemmer overens med seneste specifikation
- **Ressourceaktualitet**: Verificeret alle eksterne links til Microsoft dokumentation, sikkerhedsstandarder og implementeringsvejledninger
- **Dækning af bedste praksis**: Bekræftet omfattende dækning af autentificering, autorisation, AI-specifikke trusler, supply chain sikkerhed og enterprise mønstre

## 6. oktober 2025

### Udvidelse af Getting Started-sektionen – Avanceret serverbrug & simpel autentificering

#### Avanceret serverbrug (03-GettingStarted/10-advanced)
- **Nyt kapitel tilføjet**: Introduceret en omfattende guide til avanceret MCP serverbrug, der dækker både almindelige og lavniveau serverarkitekturer.
  - **Almindelig vs. lavniveau server**: Detaljeret sammenligning og kodeeksempler i Python og TypeScript for begge tilgange.
  - **Handler-baseret design**: Forklaring af handler-baseret værktøj/ressource/prompt styring for skalerbare, fleksible serverimplementeringer.
  - **Praktiske mønstre**: Virkelige scenarier hvor lavniveau servermønstre er fordelagtige for avancerede funktioner og arkitektur.

#### Simpel autentificering (03-GettingStarted/11-simple-auth)
- **Nyt kapitel tilføjet**: Trin-for-trin guide til implementering af simpel autentificering i MCP servere.
  - **Auth-koncepter**: Klar forklaring af autentificering vs. autorisation og håndtering af legitimationsoplysninger.
  - **Grundlæggende auth-implementering**: Middleware-baserede autentificeringsmønstre i Python (Starlette) og TypeScript (Express) med kodeeksempler.
  - **Fremgang til avanceret sikkerhed**: Vejledning i at starte med simpel auth og avancere til OAuth 2.1 og RBAC med henvisninger til avancerede sikkerhedsmoduler.

Disse tilføjelser giver praktisk, hands-on vejledning til at bygge mere robuste, sikre og fleksible MCP serverimplementeringer, der forbinder grundlæggende koncepter med avancerede produktionsmønstre.

## 29. september 2025

### MCP Server Database Integration Labs - Omfattende hands-on læringssti

#### 11-MCPServerHandsOnLabs - Nyt komplet databaseintegrationspensum
- **Komplet 13-lab læringssti**: Tilføjet omfattende hands-on pensum til at bygge produktionsklare MCP servere med PostgreSQL databaseintegration
  - **Virkelighedsnær implementering**: Zava Retail analytics use case, der demonstrerer enterprise-grade mønstre
  - **Struktureret læringsprogression**:
    - **Labs 00-03: Fundamenter** - Introduktion, kernearkitektur, sikkerhed & multi-tenancy, miljøopsætning
    - **Labs 04-06: Byg MCP Serveren** - Database design & skema, MCP serverimplementering, værktøjsudvikling  
    - **Labs 07-09: Avancerede funktioner** - Semantisk søgeintegration, test & debugging, VS Code integration
    - **Labs 10-12: Produktion & bedste praksis** - Udrulningsstrategier, overvågning & observabilitet, bedste praksis & optimering
  - **Enterprise teknologier**: FastMCP framework, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avancerede funktioner**: Row Level Security (RLS), semantisk søgning, multi-tenant dataadgang, vektor-embeddings, realtidsmonitorering

#### Terminologistandardisering - Modul til lab konvertering
- **Omfattende dokumentationsopdatering**: Systematisk opdatering af alle README-filer i 11-MCPServerHandsOnLabs til at bruge "Lab" terminologi i stedet for "Module"
  - **Sektionstitler**: Opdateret "What This Module Covers" til "What This Lab Covers" i alle 13 labs
  - **Indholdsbeskrivelse**: Ændret "This module provides..." til "This lab provides..." i hele dokumentationen
  - **Læringsmål**: Opdateret "By the end of this module..." til "By the end of this lab..."
  - **Navigationslinks**: Konverteret alle "Module XX:" referencer til "Lab XX:" i krydsreferencer og navigation
  - **Færdiggørelsessporing**: Opdateret "After completing this module..." til "After completing this lab..."
  - **Bevarede tekniske referencer**: Opretholdt Python modulreferencer i konfigurationsfiler (f.eks. `"module": "mcp_server.main"`)

#### Forbedring af studieguide (study_guide.md)
- **Visuelt pensumkort**: Tilføjet ny sektion "11. Database Integration Labs" med omfattende visualisering af lab-struktur
- **Repositorystruktur**: Opdateret fra ti til elleve hovedsektioner med detaljeret beskrivelse af 11-MCPServerHandsOnLabs
- **Læringsstivejledning**: Forbedret navigationsinstruktioner til at dække sektioner 00-11
- **Teknologidækning**: Tilføjet detaljer om FastMCP, PostgreSQL, Azure services integration
- **Læringsresultater**: Fremhævet produktionklar serverudvikling, databaseintegrationsmønstre og enterprise sikkerhed

#### Forbedring af hoved-README struktur
- **Lab-baseret terminologi**: Opdateret hoved-README.md i 11-MCPServerHandsOnLabs til konsekvent at bruge "Lab" struktur
- **Læringssti organisation**: Klar progression fra grundlæggende koncepter gennem avanceret implementering til produktionsudrulning
- **Virkelighedsfokus**: Vægt på praktisk, hands-on læring med enterprise-grade mønstre og teknologier

### Dokumentationskvalitet & konsistensforbedringer
- **Hands-on læringsfokus**: Forstærket praktisk, lab-baseret tilgang i hele dokumentationen
- **Enterprise mønsterfokus**: Fremhævet produktionsklare implementeringer og enterprise sikkerhedsovervejelser
- **Teknologiintegration**: Omfattende dækning af moderne Azure services og AI integrationsmønstre
- **Læringsprogression**: Klar, struktureret sti fra grundlæggende koncepter til produktionsudrulning

## 26. september 2025

### Forbedring af case studies - GitHub MCP Registry integration

#### Case Studies (09-CaseStudy/) - Fokus på økosystemudvikling
- **README.md**: Stor udvidelse med omfattende GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Ny omfattende case study, der undersøger GitHubs MCP Registry lancering i september 2025
    - **Problemanalyse**: Detaljeret gennemgang af fragmenterede MCP server discovery og udrulningsudfordringer
    - **Løsningsarkitektur**: GitHubs centraliserede registry-tilgang med one-click VS Code installation
    - **Forretningsmæssig effekt**: Målbare forbedringer i udvikler onboarding og produktivitet
    - **Strategisk værdi**: Fokus på modulær agentudrulning og tværværktøjs interoperabilitet
    - **Økosystemudvikling**: Positionering som grundlæggende platform for agentisk integration
  - **Forbedret case study struktur**: Opdateret alle syv case studies med ensartet formatering og omfattende beskrivelser
    - Azure AI Travel Agents: Fokus på multi-agent orkestrering
    - Azure DevOps Integration: Fokus på workflow-automatisering
    - Real-Time Documentation Retrieval: Python konsolklient implementering
    - Interactive Study Plan Generator: Chainlit konversationsbaseret webapp
    - In-Editor Documentation: VS Code og GitHub Copilot integration
    - Azure API Management: Enterprise API integrationsmønstre
    - GitHub MCP Registry: Økosystemudvikling og community platform
  - **Omfattende konklusion**: Omskrevet konklusionsafsnit, der fremhæver syv case studies, der spænder over flere MCP implementeringsdimensioner
    - Enterprise integration, multi-agent orkestrering, udviklerproduktivitet
    - Økosystemudvikling, uddannelsesapplikationer kategorisering
    - Forbedrede indsigter i arkitektur mønstre, implementeringsstrategier og bedste praksis
    - Vægt på MCP som moden, produktionsklar protokol

#### Opdateringer til studieguide (study_guide.md)
- **Visuelt pensumkort**: Opdateret mindmap til at inkludere GitHub MCP Registry i Case Studies sektionen
- **Case studies beskrivelse**: Forbedret fra generiske beskrivelser til detaljeret opdeling af syv omfattende case studies
- **Repositorystruktur**: Opdateret sektion 10 til at afspejle omfattende case study dækning med specifikke implementeringsdetaljer
- **Changelog integration**: Tilføjet 26. september 2025 post, der dokumenterer tilføjelse af GitHub MCP Registry og case study forbedringer
- **Datoopdateringer**: Opdateret footer-tidsstempel til at afspejle seneste revision (26. september 2025)

### Forbedringer af dokumentationskvalitet
- **Konsistensforbedring**: Standardiseret case study formatering og struktur på tværs af alle syv eksempler
- **Omfattende dækning**: Case studies dækker nu enterprise, udviklerproduktivitet og økosystemudviklingsscenarier
- **Strategisk positionering**: Forbedret fokus på MCP som grundlæggende platform for agentiske systemudrulninger
- **Ressourceintegration**: Opdaterede yderligere ressourcer til at inkludere GitHub MCP Registry link

## 15. september 2025

### Udvidelse af avancerede emner - Custom transports & Context engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Ny avanceret implementeringsguide
- **README.md**: Fuld implementeringsguide til brugerdefinerede MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverless event-drevet transportimplementering
    - C#, TypeScript og Python eksempler med Azure Functions integration
    - Event-drevne arkitektur mønstre for skalerbare MCP løsninger
    - Webhook modtagere og push-baseret beskedhåndtering
  - **Azure Event Hubs Transport**: High-throughput streaming transportimplementering
    - Realtids streaming kapaciteter til lav-latens scenarier
    - Partitioneringsstrategier og checkpoint management
    - Besked-batching og performanceoptimering
  - **Enterprise integrationsmønstre**: Produktionsklare arkitektur-eksempler
    - Distribueret MCP behandling på tværs af flere Azure Functions
    - Hybrid transportarkitekturer, der kombinerer flere transporttyper
    - Beskedholdbarhed, pålidelighed og fejlhåndteringsstrategier
  - **Sikkerhed & overvågning**: Azure Key Vault integration og observabilitetsmønstre
    - Managed identity autentificering og mindst privilegeret adgang
    - Application Insights telemetri og performanceovervågning
    - Circuit breakers og fejltolerance mønstre
  - **Test frameworks**: Omfattende teststrategier for brugerdefinerede transports
    - Unit tests med testdoubles og mocking frameworks
    - Integrationstests med Azure Test Containers
    - Performance- og belastningstest overvejelser

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI disciplin
- **README.md**: Omfattende udforskning af context engineering som et fremvoksende felt
  - **Kerneprincipper**: Kompleks kontekstdeling, beslutningsbevidsthed og kontekstvinduesstyring
  - **MCP protokoltilpasning**: Hvordan MCP design adresserer context engineering udfordringer
    - Begrænsninger i kontekstvindue og progressive loading strategier
    - Relevansbestemmelse og dynamisk kontekstindhentning
    - Multimodal kontekstbehandling og sikkerhedsovervejelser
  - **Implementeringstilgange**: Single-threaded vs. multi-agent arkitekturer
    - Kontekstchunking og prioriteringsteknikker
    - Progressiv kontekstindlæsning og komprimeringsstrategier
    - Lagdelt konteksttilgang og retrieval optimering
  - **Målerammeværk**: Fremvoksende metrikker til evaluering af konteksteffektivitet
    - Inputeffektivitet, performance, kvalitet og brugeroplevelsesovervejelser
    - Eksperimentelle tilgange til kontekstoptimering
    - Fejlanalyse og forbedringsmetodologier

#### Opdateringer til pensumnavigation (README.md)
- **Forbedret modulstruktur**: Opdateret pensumtabel til at inkludere nye avancerede emner
  - Tilføjet Context Engineering (5.14) og Custom Transport (5.15) poster
  - Ensartet formatering og navigationslinks på tværs af alle moduler
  - Opdaterede beskrivelser til at afspejle aktuelt indholdsomfang

### Forbedringer af mappestruktur
- **Navnestandardisering**: Omdøbt "mcp transport" til "mcp-transport" for konsistens med andre avancerede emne-mapper
- **Indholdsorganisering**: Alle 05-AdvancedTopics mapper følger nu ensartet navngivningsmønster (mcp-[topic])

### Forbedringer af dokumentationskvalitet
- **MCP specifikationsoverensstemmelse**: Alt nyt indhold refererer til gældende MCP Specification 2025-06-18
- **Multisprogseksempler**: Omfattende kodeeksempler i C#, TypeScript og Python
- **Enterprise fokus**: Produktionsklare mønstre og Azure cloud integration gennemgående
- **Visuel dokumentation**: Mermaid diagrammer til arkitektur- og flowvisualisering

## 18. august 2025

### Omfattende dokumentationsopdatering - MCP 2025-06-18 standarder

#### MCP Security Best Practices (02-Security/) - Fuld modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fuld omskrivning i overensstemmelse med MCP Specification 2025-06-18
  - **Obligatoriske krav**: Tilføjet eksplicitte SKAL/IKKE SKAL-krav fra officiel specifikation med klare visuelle indikatorer
  - **12 kerne sikkerhedspraksisser**: Omstruktureret fra 15-punkts liste til omfattende sikkerhedsområder
    - Token-sikkerhed & autentificering med integration af ekstern identitetsudbyder
    - Sessionsstyring & transport-sikkerhed med kryptografiske krav
    - AI-specifik trusselsbeskyttelse med Microsoft Prompt Shields-integration
    - Adgangskontrol & tilladelser med princippet om mindst privilegium
    - Indholdssikkerhed & overvågning med Azure Content Safety-integration
    - Forsyningskædesikkerhed med omfattende komponentverifikation
    - OAuth-sikkerhed & Confused Deputy-forebyggelse med PKCE-implementering
    - Hændelsesrespons & genopretning med automatiserede kapabiliteter
    - Overholdelse & styring med regulatorisk tilpasning
    - Avancerede sikkerhedskontroller med zero trust-arkitektur
    - Microsoft sikkerhedsøkosystemintegration med omfattende løsninger
    - Kontinuerlig sikkerhedsudvikling med adaptive praksisser
  - **Microsoft sikkerhedsløsninger**: Forbedret integrationsvejledning for Prompt Shields, Azure Content Safety, Entra ID og GitHub Advanced Security
  - **Implementeringsressourcer**: Kategoriserede omfattende ressource-links efter Officiel MCP-dokumentation, Microsoft sikkerhedsløsninger, sikkerhedsstandarder og implementeringsvejledninger

#### Avancerede sikkerhedskontroller (02-Security/) - Enterprise-implementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fuldstændig revision med enterprise-grade sikkerhedsramme
  - **9 omfattende sikkerhedsområder**: Udvidet fra grundlæggende kontroller til detaljeret enterprise-ramme
    - Avanceret autentificering & autorisation med Microsoft Entra ID-integration
    - Token-sikkerhed & anti-passthrough-kontroller med omfattende validering
    - Sessionssikkerhedskontroller med forebyggelse af overtagelse
    - AI-specifikke sikkerhedskontroller med forebyggelse af prompt-injektion og værktøjsforgiftning
    - Confused Deputy-angrebsforebyggelse med OAuth-proxy-sikkerhed
    - Værktøjsudførelsessikkerhed med sandboxing og isolering
    - Forsyningskædesikkerhedskontroller med afhængighedsverifikation
    - Overvågnings- & detektionskontroller med SIEM-integration
    - Hændelsesrespons & genopretning med automatiserede kapabiliteter
  - **Implementeringseksempler**: Tilføjet detaljerede YAML-konfigurationsblokke og kodeeksempler
  - **Microsoft-løsningsintegration**: Omfattende dækning af Azure-sikkerhedstjenester, GitHub Advanced Security og enterprise identitetsstyring

#### Avancerede emner sikkerhed (05-AdvancedTopics/mcp-security/) - Produktionsklar implementering
- **README.md**: Fuldstændig omskrivning for enterprise-sikkerhedsimplementering
  - **Nuværende specifikationsjustering**: Opdateret til MCP Specification 2025-06-18 med obligatoriske sikkerhedskrav
  - **Forbedret autentificering**: Microsoft Entra ID-integration med omfattende .NET og Java Spring Security-eksempler
  - **AI-sikkerhedsintegration**: Microsoft Prompt Shields og Azure Content Safety-implementering med detaljerede Python-eksempler
  - **Avanceret trusselsafværgelse**: Omfattende implementeringseksempler for
    - Confused Deputy-angrebsforebyggelse med PKCE og bruger samtykkevalidering
    - Token-passthrough-forebyggelse med målgruppevalidering og sikker tokenhåndtering
    - Session-overtagelsesforebyggelse med kryptografisk binding og adfærdsanalyse
  - **Enterprise sikkerhedsintegration**: Azure Application Insights-overvågning, trusselsdetektionspipelines og forsyningskædesikkerhed
  - **Implementeringstjekliste**: Klare obligatoriske vs. anbefalede sikkerhedskontroller med Microsoft sikkerhedsøkosystemfordele

### Dokumentationskvalitet & standardtilpasning
- **Specifikationsreferencer**: Opdateret alle referencer til nuværende MCP Specification 2025-06-18
- **Microsoft sikkerhedsøkosystem**: Forbedret integrationsvejledning i hele sikkerhedsdokumentationen
- **Praktisk implementering**: Tilføjet detaljerede kodeeksempler i .NET, Java og Python med enterprise-mønstre
- **Ressourceorganisering**: Omfattende kategorisering af officiel dokumentation, sikkerhedsstandarder og implementeringsvejledninger
- **Visuelle indikatorer**: Klar markering af obligatoriske krav vs. anbefalede praksisser


#### Kernekoncepter (01-CoreConcepts/) - Fuld modernisering
- **Protokolversionsopdatering**: Opdateret til at referere til nuværende MCP Specification 2025-06-18 med datobaseret versionering (ÅÅÅÅ-MM-DD-format)
- **Arkitekturforfining**: Forbedrede beskrivelser af Hosts, Clients og Servers for at afspejle nuværende MCP-arkitekturpatterns
  - Hosts nu klart defineret som AI-applikationer, der koordinerer flere MCP-klientforbindelser
  - Clients beskrevet som protokolforbindere, der opretholder en-til-en serverrelationer
  - Servers forbedret med lokale vs. fjernudrulningsscenarier
- **Primitiv omstrukturering**: Fuldstændig revision af server- og klientprimitiver
  - Serverprimitiver: Ressourcer (datakilder), Prompter (skabeloner), Værktøjer (eksekverbare funktioner) med detaljerede forklaringer og eksempler
  - Klientprimitiver: Sampling (LLM-udførelser), Elicitation (brugerinput), Logging (debugging/overvågning)
  - Opdateret med nuværende opdagelses- (`*/list`), hentnings- (`*/get`) og eksekverings- (`*/call`) metodepatterns
- **Protokolarkitektur**: Introduceret to-lags arkitekturmodel
  - Datalag: JSON-RPC 2.0 fundament med livscyklusstyring og primitiv
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer
- **Sikkerhedsramme**: Omfattende sikkerhedsprincipper inklusive eksplicit bruger samtykke, databeskyttelse, værktøjsudførelsessikkerhed og transportlagsikkerhed
- **Kommunikationsmønstre**: Opdaterede protokolmeddelelser til at vise initialisering, opdagelse, eksekvering og notifikationsflows
- **Kodeeksempler**: Opfriskede flersprogede eksempler (.NET, Java, Python, JavaScript) for at afspejle nuværende MCP SDK-mønstre

#### Sikkerhed (02-Security/) - Omfattende sikkerhedsrevision  
- **Standardtilpasning**: Fuld tilpasning til MCP Specification 2025-06-18 sikkerhedskrav
- **Autentificeringsevolution**: Dokumenteret udvikling fra brugerdefinerede OAuth-servere til ekstern identitetsudbyderdelegering (Microsoft Entra ID)
- **AI-specifik trusselsanalyse**: Forbedret dækning af moderne AI-angrebsvektorer
  - Detaljerede prompt-injektionsangrebsscenarier med virkelighedsnære eksempler
  - Værktøjsforgiftning og "rug pull"-angrebsmønstre
  - Kontekstvinduesforgiftning og modelforvirringsangreb
- **Microsoft AI-sikkerhedsløsninger**: Omfattende dækning af Microsoft sikkerhedsøkosystem
  - AI Prompt Shields med avanceret detektion, spotlighting og delimiter-teknikker
  - Azure Content Safety integrationsmønstre
  - GitHub Advanced Security til forsyningskædebeskyttelse
- **Avanceret trusselsafværgelse**: Detaljerede sikkerhedskontroller for
  - Session-overtagelse med MCP-specifikke angrebsscenarier og kryptografiske session-ID-krav
  - Confused Deputy-problemer i MCP-proxy-scenarier med eksplicitte samtykkekrav
  - Token-passthrough-sårbarheder med obligatoriske valideringskontroller
- **Forsyningskædesikkerhed**: Udvidet AI-forsyningskædedækning inklusive foundation-modeller, embeddings-tjenester, kontekstudbydere og tredjeparts-API’er
- **Foundation-sikkerhed**: Forbedret integration med enterprise sikkerhedsmønstre inklusive zero trust-arkitektur og Microsoft sikkerhedsøkosystem
- **Ressourceorganisering**: Kategoriserede omfattende ressource-links efter type (Officielle docs, standarder, forskning, Microsoft-løsninger, implementeringsvejledninger)

### Forbedringer i dokumentationskvalitet
- **Strukturerede læringsmål**: Forbedrede læringsmål med specifikke, handlingsorienterede resultater
- **Krydsreferencer**: Tilføjet links mellem relaterede sikkerheds- og kernekonceptemner
- **Aktuel information**: Opdateret alle datoreferencer og specifikationslinks til gældende standarder
- **Implementeringsvejledning**: Tilføjet specifikke, handlingsorienterede implementeringsretningslinjer i begge sektioner

## 16. juli 2025

### README og navigationsforbedringer
- Fuldstændig redesignet læseplanens navigation i README.md
- Udskiftet `<details>`-tags med mere tilgængeligt tabelbaseret format
- Oprettet alternative layoutmuligheder i ny "alternative_layouts"-mappe
- Tilføjet kortbaserede, fanebaserede og akkordeon-stil navigations-eksempler
- Opdateret repository-strukturafsnit til at inkludere alle seneste filer
- Forbedret afsnittet "Sådan bruger du denne læseplan" med klare anbefalinger
- Opdateret MCP-specifikationslinks til at pege på korrekte URL’er
- Tilføjet afsnit om Context Engineering (5.14) til læseplansstrukturen

### Opdateringer til studieguide
- Fuldstændig revideret studieguide for at tilpasse til nuværende repository-struktur
- Tilføjet nye sektioner for MCP-klienter og værktøjer samt populære MCP-servere
- Opdateret det visuelle læseplanskort til nøjagtigt at afspejle alle emner
- Forbedret beskrivelser af avancerede emner for at dække alle specialiserede områder
- Opdateret casesektionen til at afspejle faktiske eksempler
- Tilføjet denne omfattende ændringslog

### Community-bidrag (06-CommunityContributions/)
- Tilføjet detaljeret information om MCP-servere til billedgenerering
- Tilføjet omfattende afsnit om brug af Claude i VSCode
- Tilføjet Cline terminalklient-opsætning og brugsinstruktioner
- Opdateret MCP-klientafsnit til at inkludere alle populære klientmuligheder
- Forbedret bidragseksempler med mere præcise kodeeksempler

### Avancerede emner (05-AdvancedTopics/)
- Organiseret alle specialiserede emnemapper med konsekvent navngivning
- Tilføjet materialer og eksempler om context engineering
- Tilføjet dokumentation for Foundry-agentintegration
- Forbedret Entra ID sikkerhedsintegrationsdokumentation

## 11. juni 2025

### Første udgivelse
- Udgivet første version af MCP for Beginners-læseplan
- Oprettet grundstruktur for alle 10 hovedsektioner
- Implementeret visuelt læseplanskort til navigation
- Tilføjet indledende prøveprojekter i flere programmeringssprog

### Kom godt i gang (03-GettingStarted/)
- Oprettet første serverimplementeringseksempler
- Tilføjet vejledning til klientudvikling
- Inkluderet instruktioner til LLM-klientintegration
- Tilføjet dokumentation for VS Code-integration
- Implementeret Server-Sent Events (SSE) servereksempler

### Kernekoncepter (01-CoreConcepts/)
- Tilføjet detaljeret forklaring af klient-server arkitektur
- Oprettet dokumentation om nøgleprotokolkomponenter
- Dokumenteret beskedmønstre i MCP

## 23. maj 2025

### Repository-struktur
- Initialiseret repository med grundlæggende mappestruktur
- Oprettet README-filer for hver hovedsektion
- Sat op oversættelsesinfrastruktur
- Tilføjet billedressourcer og diagrammer

### Dokumentation
- Oprettet indledende README.md med læseplansoversigt
- Tilføjet CODE_OF_CONDUCT.md og SECURITY.md
- Sat op SUPPORT.md med vejledning til hjælp
- Oprettet foreløbig studieguide-struktur

## 15. april 2025

### Planlægning og rammeværk
- Indledende planlægning for MCP for Beginners-læseplan
- Defineret læringsmål og målgruppe
- Skitseret 10-sektions struktur for læseplanen
- Udviklet konceptuelt rammeværk for eksempler og cases
- Oprettet indledende prototypeeksempler for nøglekoncepter

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
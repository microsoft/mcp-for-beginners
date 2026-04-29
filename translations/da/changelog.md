# Changelog: MCP for Beginners Curriculum

Dette dokument tjener som en oversigt over alle væsentlige ændringer foretaget i Model Context Protocol (MCP) for Beginners pensum. Ændringer dokumenteres i omvendt kronologisk rækkefølge (nyeste ændringer først).

## 11. april 2026

### Nyt lektion, dokumentationsrettelser og opdateringer af afhængigheder

#### Nyt pensumindhold tilføjet

**Modul 05 - Avancerede emner**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattende guide, der dækker det adversarielle debatmønster for multi-agent systemer
  - Mermaid arkitekturdiagram: to agenter → delt MCP-server → debattranskript → dommer → afgørelse
  - Delt MCP-værktøjsserver (`web_search` + `run_python`) implementeret i Python og TypeScript
  - Modstridende systemprompter (FOR / IMOD / Dommer) med eksplicitte krav til brug af værktøjer
  - Debate orchestrator i Python, TypeScript og C#, der håndterer runder og dirigerer argumenter
  - MCP `ClientSession` ledningsføring til orchestratoren for at kalde reelle værktøjer
  - Brugssammensat tabel (hallucinationdetektion, trusselsmodellering, API designgennemgang, faktakontrol, teknologivalg)
  - Sikkerhedsovervejelser: sandboxet eksekvering, validering af værktøjskald, ratebegrænsning, revisionslogning
  - Struktureret øvelse med tre praktiske scenarier (kodegennemgang, arkitekturafgørelse, indholdsmoderation)

#### Dokumentationsrettelser

**Modul 03 - Kom godt i gang**
- **05-stdio-server/README.md**: Rettet ufuldstændigt TypeScript stdio-server eksempel — tilføjet manglende instansiering af transport (`new StdioServerTransport()`) og `server.connect(transport)` kald for at matche Python- og .NET-eksemplerne i samme sektion
- **14-sampling/README.md**: Rettet slåfejl — rettet `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Opdateringer i pensum

**Hoved README.md**
- Tilføjet punkt 5.17 (Adversarial Multi-Agent Reasoning with MCP) til pensumtabel med direkte link til ny lektion

**05-AdvancedTopics/README.md**
- Tilføjet række for Lektion 5.17 til lektionstabellen

**study_guide.md**
- Tilføjet Adversarial Multi-Agent Reasoning emnet til mind-mappen og prosabeskrivelsen for Avancerede Emner

#### Kode- og sikkerhedsrettelser

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Sikkerhedsrettelse — kommandoinjektion**: Udskiftet `execSync` shell-interpolering med `execFile` + `promisify` i TypeScript `run_python` værktøjet, hvilket eliminerer overfladen for kommandoinjektion (LLM-styret kode sendes nu som et bogstaveligt argv-element uden shellindblanding)
- **MCP værktøj loop ledningsføring**: Opdateret Python debate orchestratoren til at bruge `AsyncAnthropic` klient (erstatter blokkerende sync `Anthropic`), sende en live `ClientSession` direkte til hver agent tur, hente værktøjsdefinitioner via `session.list_tools()` hver tur og udsende `tool_use` blokke via `session.call_tool()` i en løkke indtil modellen udsender et endeligt tekstsvar

#### Opdateringer af afhængigheder

- Opdateret `hono` til 4.12.12 på tværs af flere pakker (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Opdateret `@hono/node-server` fra 1.19.11 til 1.19.13 i TypeScript-pakker
- Opdateret `cryptography` fra 46.0.5 til 46.0.7 i Python-pakker (10-StreamliningAIWorkflows lab 3 og 4)
- Opdateret `lodash` fra 4.17.23 til 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Oversættelser

- Synkroniseret oversættelser for 48+ sprog med de seneste kildeændringer (i18n opdatering)

---

## 5. februar 2026

### Repo-dækkende validering og navigation forbedringer

#### Nyt pensumindhold tilføjet

**Modul 03 - Kom godt i gang**
- **12-mcp-hosts/README.md**: Ny omfattende guide til opsætning af MCP-værter
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf konfigurationseksempler
  - JSON konfigurationsskabeloner for alle større værter
  - Sammenligningstabel over transporttyper (stdio, SSE/HTTP, WebSocket)
  - Fejlfinding af almindelige forbindelsesproblemer
  - Sikkerhedspraksis for værtskonfiguration

- **13-mcp-inspector/README.md**: Ny debugging guide til MCP Inspector
  - Installationsmetoder (npx, npm global, fra kilde)
  - Forbindelse til servere via stdio og HTTP/SSE
  - Testværktøjer, ressourcer og prompt workflows
  - VS Code integration med MCP Inspector
  - Almindelige debugging scenarier med løsninger

**Modul 04 - Praktisk Implementation**
- **pagination/README.md**: Ny vejledning til implementering af pagination
  - Cursor-baserede pagination mønstre i Python, TypeScript, Java
  - Client-side pagination håndtering
  - Cursor designstrategier (opaque vs. struktureret)
  - Anbefalinger til ydeevneoptimering

**Modul 05 - Avancerede emner**
- **mcp-protocol-features/README.md**: Ny dybdegående gennemgang af protokolfunktioner
  - Implementering af fremdriftsnotifikationer
  - Mønstre for annullering af forespørgsler
  - Resurse-skabeloner med URI mønstre
  - Server livscyklus styring
  - Kontrol af logniveauer
  - Fejlhåndteringsmønstre med JSON-RPC koder

#### Navigation rettelser (24+ filer opdateret)

**Hovedmodul READMEs**
 Nu med links til både første lektion OG næste modul

**02-Security Underfiler**
- Alle 5 supplerende sikkerhedsdokumenter har nu "Hvad er næste" navigation:

**09-CaseStudy Filer**
- Alle case study filer har nu sekventiel navigation:

**10-StreamliningAI Labs**
Tilføjet 'Hvad er næste' sektion til Modul 10 oversigten og Modul 11

#### Kode- og indholdsrettelser

**SDK og afhængighedsopdateringer**
Fikset tom openai version til `^4.95.0`
Opdateret SDK fra `^1.8.0` til `>=1.26.0`
Opdateret mcp versionspins til `>=1.26.0`

**Kode rettelser**
Fikset ugyldig model `gpt-4o-mini` til `gpt-4.1-mini`

**Indholds rettelser**
Fikset ødelagt link `READMEmd` → `README.md`, rettet pensum header `Module 1-3` → `Module 0-3`, rettet case-sensitive sti
Fjernet korrumperet duplikat Case Study 5 indhold

**Begyndervejledning forbedringer**
Tilføjet ordentlig introduktion, læringsmål og forudsætninger for begyndere

#### Opdateringer i pensum

**Hoved README.md**
- Tilføjet punkter 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) til pensumtabel

**Modul READMEs**
Tilføjet lektioner 12 og 13 til lektionlisten
Tilføjet Praktiske guider sektion med pagination link
Tilføjet lektioner 5.15 (Custom Transport) og 5.16 (Protocol Features)

**study_guide.md**
- Opdateret mindmap med alle nye emner: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## 28. jan 2026

### MCP Specifikation 2025-11-25 Overensstemmelsesgennemgang

#### Kernen begreber forbedring (01-CoreConcepts/)
- **Ny klient-primitiv - Roots**: Tilføjet omfattende dokumentation om Roots klient-primitiv, som gør det muligt for servere at forstå filsystemgrænser og adgangstilladelser
- **Værktøjs-annoteringer**: Tilføjet dokumentation om annotationsadfærd for værktøjer (`readOnlyHint`, `destructiveHint`) for bedre beslutninger ved værktøjsudførelse
- **Værktøjskald i Sampling**: Opdateret Sampling dokumentationen til at inkludere `tools` og `toolChoice` parametre til modelstyret værktøjskald ved sampling forespørgsler
- **URL Mode Elicitation**: Tilføjet dokumentation om URL-baseret elicitation for server-initierede eksterne web-interaktioner
- **Tasks (Eksperimentel)**: Tilføjet ny sektion, der dokumenterer den eksperimentelle Tasks funktion til holdbare eksekverings-wrappere og udsat resultatindhentning
- **Icon Support**: Noteret at værktøjer, ressourcer, resurse-skabeloner og prompter nu kan inkludere ikoner som yderligere metadata

#### Dokumentationsopdateringer
- **README.md**: Tilføjet MCP Specifikation 2025-11-25 versionsreference og datering af versionsstyring
- **study_guide.md**: Opdateret pensumkort til at inkludere Tasks og Tool Annotations i Core Concepts sektionen; opdateret dokumentets tidsstempel

#### Overensstemmelsestjek af specifikation
- **Protokolversion**: Bekræftet at al dokumentation henviser til aktuel MCP Specifikation 2025-11-25
- **Arkitekturtilpasning**: Bekræftet at to-lags arkitektur (Data Layer + Transport Layer) er dokumenteret korrekt
- **Primitiver dokumentation**: Valideret serverprimitiver (Ressourcer, Prompter, Værktøjer) og klientprimitiver (Sampling, Elicitation, Logging, Roots)
- **Transportmekanismer**: Verificeret korrekt dokumentation af STDIO og Streamable HTTP transport
- **Sikkerhedsguides**: Bekræftet overensstemmelse med aktuelle MCP Security Best Practices dokumentation

#### Nøglefunktioner i MCP 2025-11-25 dokumenteret
- **OpenID Connect Discovery**: Auth server discovery via OIDC
- **OAuth Client ID Metadata Dokumenter**: Anbefalet klientregistreringsmekanisme
- **JSON Schema 2020-12**: Standard dialekt for MCP skemadefinitioner
- **SDK Tiering System**: Formaliserede krav til SDK funktionsstøtte og vedligeholdelse
- **Governance Struktur**: Formaliserede arbejdsgrupper og interessegrupper i MCP governance

### Stor opdatering af sikkerhedsdokumentation (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **Ny praktisk træningsressource**: Tilføjet omfattende integration med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i al sikkerhedsdokumentation
- **Ruteovervågning**: Dokumenteret fuld progression fra Base Camp til Summit
- **OWASP tilpasning**: Al sikkerhedsvejledning mappes nu til OWASP MCP Azure Security Guide risici

#### OWASP MCP Top 10 Integration
- **Ny sektion**: Tilføjet OWASP MCP Top 10 sikkerhedsrisikotabel med Azure-mitigationer til hovedsikkerheds README
- **Risiko-baseret dokumentation**: Opdateret mcp-security-controls-2025.md med OWASP MCP risikoreferencer for hvert sikkerhedsområde
- **Referencearkitektur**: Linket til OWASP MCP Azure Security Guide referencearkitektur og implementeringsmønstre

#### Opdaterede sikkerhedsfiler
- **README.md**: Tilføjet Sherpa Workshop oversigt, ekspeditionsrutetabel, OWASP MCP Top 10 risikosammendrag og praktisk træningssektion
- **mcp-security-controls-2025.md**: Opdateret header til februar 2026, tilføjet OWASP risikoreferencer (MCP01-MCP08), rettet versionsinkonsistens
- **mcp-security-best-practices-2025.md**: Tilføjet Sherpa og OWASP ressourcer sektion, opdateret tidsstempel
- **mcp-best-practices.md**: Tilføjet praktisk træningssektion med Sherpa og OWASP links
- **azure-content-safety-implementation.md**: Tilføjet OWASP MCP06 reference, Sherpa Camp 3 tilpasning og yderligere ressourcer sektion

#### Nye ressourcelinks tilføjet
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individuelle OWASP MCP risiko sider (MCP01-MCP10)

### Pensumdækkende MCP Specifikation 2025-11-25 Tilpasning

#### Modul 03 - Kom godt i gang
- **SDK dokumentation**: Tilføjet Go SDK til officiel SDK-liste; opdateret alle SDK referencer til at tilpasse MCP Specifikation 2025-11-25
- **Transportafklaring**: Opdateret beskrivelser af STDIO og HTTP streaming transport med eksplicitte spec reference

#### Modul 04 - Praktisk Implementation
- **SDK opdateringer**: Tilføjet Go SDK; opdateret SDK-liste med versionsreference til specifikationen
- **Autorisation Spec**: Opdateret MCP Authorization specifikationslink til gældende 2025-11-25 version

#### Modul 05 - Avancerede Emner
- **Nye funktioner**: Tilføjet note om nye MCP Specifikation 2025-11-25 funktioner (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop links til yderligere referencer

#### Modul 06 - Community Bidrag
- **SDK-liste**: Tilføjet Swift og Rust SDKs; opdateret specifikationslink til 2025-11-25
- **Spec reference**: Opdateret MCP Specifikationslink til direkte specifikations-URL

#### Modul 07 - Lessons from Early Adoption
- **Resource opdateringer**: Tilføjet MCP Specifikation 2025-11-25 link og OWASP MCP Top 10 til yderligere ressourcer

#### Modul 08 - Best Practices
- **Spec versions**: Opdateret MCP Specifikationsreference til 2025-11-25
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 og Sherpa workshop til yderligere referencer

#### Modul 10 - Streamlining AI Workflows
- **Badge opdatering**: Ændret MCP versionsbadge fra SDK version (1.9.3) til specifikationsversion (2025-11-25)
- **Ressourcelinks**: Opdateret MCP Specifikationslink; tilføjet OWASP MCP Top 10

#### Modul 11 - MCP Server Hands-On Labs
- **Spec reference**: Opdateret MCP Specifikationslink til 2025-11-25 version
- **Sikkerhedsressourcer**: Tilføjet OWASP MCP Top 10 til officielle ressourcer

## 18. december 2025
### Opdatering af Sikkerhedsdokumentation - MCP Specifikation 2025-11-25

#### MCP Sikkerhedsbedste Praksis (02-Security/mcp-best-practices.md) - Specifikationsversionsopdatering
- **Protokolversionsopdatering**: Opdateret til at referere den seneste MCP Specifikation 2025-11-25 (udgivet den 25. november 2025)
  - Opdaterede alle referencer til specifikationsversion fra 2025-06-18 til 2025-11-25
  - Opdaterede dokumentdato-referencer fra 18. august 2025 til 18. december 2025
  - Verificerede at alle specifikations-URL'er peger på den aktuelle dokumentation
- **Indholdsvalidering**: Omfattende validering af sikkerhedsbedste praksis i forhold til de nyeste standarder
  - **Microsoft Sikkerhedsløsninger**: Verificerede aktuelle terminologier og links for Prompt Shields (tidligere "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID og Azure Key Vault
  - **OAuth 2.1 Sikkerhed**: Bekræftet overensstemmelse med de nyeste OAuth sikkerhedsbedste praksis
  - **OWASP Standarder**: Validerede at OWASP Top 10 for LLMs-referencer forbliver aktuelle
  - **Azure Services**: Verificerede alle Microsoft Azure dokumentationslinks og bedste praksisser
- **Standardoverensstemmelse**: Alle refererede sikkerhedsstandarder bekræftet aktuelle
  - NIST AI Risikostyringsramme
  - ISO 27001:2022
  - OAuth 2.1 Sikkerhedsbedste Praksis
  - Azure sikkerheds- og compliance-rammer
- **Implementeringsressourcer**: Validerede alle links til implementeringsvejledninger og ressourcer
  - Azure API Management autentificeringsmønstre
  - Microsoft Entra ID integrationsvejledninger
  - Azure Key Vault hemmelighedshåndtering
  - DevSecOps pipelines og overvågningsløsninger

### Dokumentationskvalitetssikring
- **Specifikationsoverholdelse**: Sikrede at alle obligatoriske MCP sikkerhedskrav (SKAL/MÅ IKKE) stemmer overens med den seneste specifikation
- **Ressourceaktualitet**: Verificerede alle eksterne links til Microsoft dokumentation, sikkerhedsstandarder og implementeringsvejledninger
- **Dækning af bedste praksis**: Bekræftet omfattende dækning af autentifikation, autorisation, AI-specifikke trusler, sikkerhed i forsyningskæden og virksomhedsmønstre

## 6. oktober 2025

### Udvidelse af Kom Godt I Gang Sektion – Avanceret Serverbrug & Enkel Autentifikation

#### Avanceret Serverbrug (03-GettingStarted/10-advanced)
- **Nyt Kapitel Tilføjet**: Introducerede en omfattende guide til avanceret MCP serverbrug, der dækker både almindelige og lavniveau serverarkitekturer.
  - **Almindelig vs. Lavniveau Server**: Detaljeret sammenligning og kodeeksempler i Python og TypeScript for begge tilgange.
  - **Handler-baseret Design**: Forklaring af handler-baseret værktøj-/ressource-/promptstyring for skalerbare og fleksible serverimplementeringer.
  - **Praktiske Mønstre**: Virkelighedsnære scenarier hvor lavniveau servermønstre er gavnlige til avancerede funktioner og arkitektur.

#### Enkel Autentifikation (03-GettingStarted/11-simple-auth)
- **Nyt Kapitel Tilføjet**: Trin-for-trin vejledning til implementering af enkel autentifikation i MCP servere.
  - **Auth Begreber**: Klar forklaring af autentifikation vs. autorisation og håndtering af legitimationsoplysninger.
  - **Basic Auth Implementering**: Middleware-baserede autentifikationsmønstre i Python (Starlette) og TypeScript (Express) med kodeeksempler.
  - **Udvikling til Avanceret Sikkerhed**: Vejledning i start med enkel autentifikation og progression til OAuth 2.1 og RBAC, med henvisninger til avancerede sikkerhedsmoduler.

Disse tilføjelser giver praktisk, hands-on vejledning til at bygge mere robuste, sikre og fleksible MCP serverimplementeringer, som forbinder grundlæggende koncepter med avancerede produktionsmønstre.

## 29. september 2025

### MCP Server Databaseintegration Labs - Omfattende Praktisk Læringsvej

#### 11-MCPServerHandsOnLabs - Ny Fuldt Udviklet Databaseintegrationslæreplan
- **Komplet 13-Lab Læringsvej**: Tilføjet omfattende hands-on læreplan for opbygning af produktionsklare MCP servere med PostgreSQL databaseintegration
  - **Virkelighedsnær Implementering**: Zava Retail analytics use case demonstrerer virksomhedsmønstre
  - **Struktureret Læringsprogression**:
    - **Labs 00-03: Fundament** - Introduktion, Kernearkitektur, Sikkerhed & Multi-Tenancy, Miljøopsætning
    - **Labs 04-06: Opbygning af MCP Server** - Database Design & Skema, MCP Server Implementering, Værktøjsudvikling  
    - **Labs 07-09: Avancerede Funktioner** - Semantisk Søgning Integration, Test & Debugging, VS Code Integration
    - **Labs 10-12: Produktion & Bedste Praksis** - Implementeringsstrategier, Overvågning & Observabilitet, Bedste Praksis & Optimering
  - **Virksomhedsteknologier**: FastMCP framework, PostgreSQL med pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Avancerede Funktioner**: Row Level Security (RLS), semantisk søgning, multi-tenant dataadgang, vektorembeddings, realtids overvågning

#### Terminologistandardisering - Modul til Lab Konvertering
- **Omfattende Dokumentationsopdatering**: Systematisk opdateret alle README-filer i 11-MCPServerHandsOnLabs til at bruge "Lab"-terminologi i stedet for "Modul"
  - **Sektionoverskrifter**: Opdateret "What This Module Covers" til "What This Lab Covers" på tværs af alle 13 labs
  - **Indholdsbeskrivelser**: Ændret "This module provides..." til "This lab provides..." gennem hele dokumentationen
  - **Læringsmål**: Opdateret "By the end of this module..." til "By the end of this lab..."
  - **Navigation Links**: Konverteret alle "Module XX:" referencer til "Lab XX:" i krydsreferencer og navigation
  - **Færdiggørelsessporing**: Opdateret "After completing this module..." til "After completing this lab..."
  - **Tekniske Referencer Bevarede**: Opretholdt Python modulreferencer i konfigurationsfiler (fx. `"module": "mcp_server.main"`)

#### Studieguide Forbedring (study_guide.md)
- **Visuelt Læreplanskort**: Tilføjet ny sektion "11. Database Integration Labs" med omfattende visualisering af lab-strukturen
- **Repository Struktur**: Opdateret fra ti til elleve hovedsektioner med detaljeret beskrivelse af 11-MCPServerHandsOnLabs
- **Læringsvejledning**: Forbedrede navigationsinstruktioner til at dække sektioner 00-11
- **Teknologidækning**: Tilføjet FastMCP, PostgreSQL, Azure service integrationsdetaljer
- **Læringsresultater**: Fremhævet produktionsklar serverudvikling, databaseintegrationsmønstre og virksomhedsikkerhed

#### Hoved README Strukturforbedringer
- **Lab-Baseret Terminologi**: Opdateret hoved README.md i 11-MCPServerHandsOnLabs til konsekvent at bruge "Lab"-struktur
- **Læringsvejorganisation**: Klar progression fra grundlæggende koncepter til avanceret implementering og til produktion
- **Virkelighedsfokus**: Fokus på praktisk, hands-on læring med virksomhedsmønstre og teknologier

### Dokumentationskvalitet & Konsistensforbedringer
- **Hands-On Læringsfokus**: Styrket praktisk, lab-baseret tilgang i hele dokumentationen
- **Virksomhedsmønsterfokus**: Fremhævet produktionsklare implementeringer og virksomhedssikkerhedsovervejelser
- **Teknologiintegration**: Omfattende dækning af moderne Azure services og AI integrationsmønstre
- **Læringsprogression**: Klar, struktureret vej fra grundlæggende koncepter til produktionsimplementering

## 26. september 2025

### Case Studies Forbedring - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Fokus på Økosystemudvikling
- **README.md**: Stor udvidelse med omfattende GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Ny omfattende case study som undersøger GitHubs MCP Registry lancering i september 2025
    - **Problem Analyse**: Detaljeret undersøgelse af fragmenterede MCP server opdagelses- og implementeringsudfordringer
    - **Løsningsarkitektur**: GitHubs centraliserede registry tilgang med one-click VS Code installation
    - **Forretningsmæssig Indvirkning**: Målbare forbedringer i udvikler onboarding og produktivitet
    - **Strategisk Værdi**: Fokus på modulær agentudrulning og tværværktøjsinteroperabilitet
    - **Økosystemudvikling**: Positionering som fundamentalt platform for agentintegration
  - **Forbedret Case Study Struktur**: Opdaterede alle syv case studies med ensartet formatering og omfattende beskrivelser
    - Azure AI Rejseagenter: Fokus på multi-agent orkestrering
    - Azure DevOps Integration: Workflow automatiseringsfokus
    - Realtids Dokumenthentning: Python konsolklient implementation
    - Interaktiv Studieplansgenerator: Chainlit samtale web app
    - In-Editor Dokumentation: VS Code og GitHub Copilot integration
    - Azure API Management: Virksomheds API integrationsmønstre
    - GitHub MCP Registry: Økosystemudvikling og fællesskabsplatform
  - **Omfattende Konklusion**: Omskrevet konklusionssektion med fokus på syv case studies der spænder over flere MCP implementeringsdimensioner
    - Virksomhedsintegration, Multi-Agent Orkestrering, Udviklerproduktivitet
    - Økosystemudvikling, Uddannelsesmæssige Applikationer kategorisering
    - Forbedret indsigt i arkitektur, implementeringsstrategier og bedste praksis
    - Betoning af MCP som moden, produktionsklar protokol

#### Studieguide Opdateringer (study_guide.md)
- **Visuelt Læreplanskort**: Opdateret mindmap til inklusion af GitHub MCP Registry i Case Studies sektion
- **Case Study Beskrivelse**: Forbedret fra generiske beskrivelser til detaljeret gennemgang af syv omfattende case studies
- **Repository Struktur**: Opdateret sektion 10 for at afspejle omfattende case study dækning med specifikke implementeringsdetaljer
- **Ændringslog Integration**: Tilføjet post fra 26. september 2025 med dokumentation af GitHub MCP Registry tilføjelse og case study forbedringer
- **Dato Opdateringer**: Opdateret sidefodstidsstempling til at afspejle seneste revision (26. september 2025)

### Dokumentationskvalitetsforbedringer
- **Konsistensforbedring**: Standardiseret case study formatering og struktur på tværs af alle syv eksempler
- **Omfattende Dækning**: Case studies dækker nu virksomhed, udviklerproduktivitet og økosystemudviklingsscenarier
- **Strategisk Positionering**: Forbedret fokus på MCP som fundamentalt platform for agentbaseret systemsudrulning
- **Ressourceintegration**: Opdaterede yderligere ressourcer til at inkludere GitHub MCP Registry link

## 15. september 2025

### Udvidelse af Avancerede Emner - Tilpassede Transports & Kontekst Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Ny Avanceret Implementeringsguide
- **README.md**: Komplet implementeringsvejledning for tilpassede MCP transportmekanismer
  - **Azure Event Grid Transport**: Omfattende serverløs, hændelsesdrevet transportimplementering
    - C#, TypeScript og Python eksempler med Azure Functions integration
    - Hændelsesdrevne arkitektur-mønstre til skalerbare MCP løsninger
    - Webhook modtagere og push-baseret beskedhåndtering
  - **Azure Event Hubs Transport**: Højgennemløbs streaming-transportimplementering
    - Realtids streaming kapaciteter til lav-latens scenarier
    - Partitioneringsstrategier og checkpoint-styring
    - Beskedbunching og ydelsesoptimering
  - **Virksomhedsintegrationsmønstre**: Produktionsklare arkitektoniske eksempler
    - Distribueret MCP behandling på tværs af flere Azure Functions
    - Hybrid transportarkitekturer der kombinerer flere transporttyper
    - Beskedsikkerhed, pålidelighed og fejlhåndteringsstrategier
  - **Sikkerhed & Overvågning**: Azure Key Vault integration og observabilitetsmønstre
    - Managed identity autentifikation og mindst privilegeret adgang
    - Application Insights telemetri og ydelsesovervågning
    - Afbrydere og fejl-tolerance mønstre
  - **Test Frameworks**: Omfattende teststrategier til tilpassede transports
    - Unit tests med test doubles og mock frameworks
    - Integrations-tests med Azure Test Containers
    - Ydelses- og belastningstest overvejelser

#### Kontekst Engineering (05-AdvancedTopics/mcp-contextengineering/) - Fremvoksende AI Disciplin
- **README.md**: Omfattende udforskning af kontekst engineering som en fremvoksende disciplin
  - **Kerneprincipper**: Komplet kontekstdeling, handling beslutningsbevidsthed og kontekstvinduesstyring
  - **MCP Protokoltilpasning**: Hvordan MCP design tackler kontekst engineering udfordringer
    - Begrænsninger i kontekstvinduer og progressive indlæsningsstrategier
    - Relevansbestemmelse og dynamisk konteksthentning
    - Multimodal konstekstbehandling og sikkerhedsovervejelser
  - **Implementeringstilgange**: Single-threaded vs. multi-agent arkitekturer
    - Kontekstchunking og prioriteringsteknikker
    - Progressiv kontekstindlæsning og komprimeringsstrategier
    - Lagdelt konteksttilgange og hentningsoptimering
  - **Målerammeværk**: Fremvoksende metrikker til evaluering af konteksteffekt
    - Inputeffektivitet, ydelse, kvalitet og brugeroplevelsesovervejelser
    - Eksperimentelle tilgange til kontekstoptimering
    - Fejlanalyse og forbedringsmetoder

#### Curriculum Navigationsopdateringer (README.md)
- **Forbedret Modulstruktur**: Opdateret læreplantabel til at inkludere nye avancerede emner
  - Tilføjet Kontekst Engineering (5.14) og Custom Transport (5.15) poster
  - Ensartet formatering og navigationslinks på tværs af alle moduler
  - Opdaterede beskrivelser til at reflektere aktuelt indholdsomfang

### Mappestrukturforbedringer
- **Navngivningsstandardisering**: Omdøbte "mcp transport" til "mcp-transport" for overensstemmelse med andre avancerede emne-mapper
- **Indholdsorganisering**: Alle 05-AdvancedTopics mapper følger nu konsistent navngivningsmønster (mcp-[emne])

### Dokumentationskvalitetsforbedringer
- **MCP Specifikationsoverensstemmelse**: Alt nyt indhold refererer til nuværende MCP Specifikation 2025-06-18
- **Fler-sprogseksempler**: Omfattende kodeeksempler i C#, TypeScript og Python
- **Virksomhedsfokus**: Produktionsklare mønstre og integration med Azure cloud gennemgående
- **Visuel Dokumentation**: Mermaid-diagrammer til arkitektur- og flowvisualisering

## 18. august 2025

### Omfattende Dokumentationsopdatering - MCP 2025-06-18 Standarder

#### MCP Sikkerhedsbedste Praksis (02-Security/) - Fuld Modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fuldstændig omskrivning tilpasset MCP Specifikation 2025-06-18  
  - **Obligatoriske Krav**: Tilføjet eksplicitte SKAL/IKKE SKAL krav fra officiel specifikation med klare visuelle indikatorer  
  - **12 Kerne Sikkerhedspraksisser**: Omstruktureret fra 15-punkts liste til omfattende sikkerhedsområder  
    - Token Sikkerhed & Godkendelse med integration af ekstern identitetsudbyder  
    - Sessionsstyring & Transport Sikkerhed med kryptografiske krav  
    - AI-Specifik Trusselsbeskyttelse med Microsoft Prompt Shields integration  
    - Adgangskontrol & Rettigheder med princip om mindst rettighed  
    - Indholdssikkerhed & Overvågning med Azure Content Safety integration  
    - Forsyningskædesikkerhed med omfattende komponentverifikation  
    - OAuth Sikkerhed & Forvirret Stedfortræder Forebyggelse med PKCE-implementering  
    - Incident Response & Genopretning med automatiserede funktioner  
    - Overholdelse & Governance med regulatorisk tilpasning  
    - Avancerede Sikkerhedskontroller med zero trust arkitektur  
    - Microsoft Sikkerhedsøkosystem Integration med omfattende løsninger  
    - Kontinuerlig Sikkerhedsudvikling med adaptive praksisser  
  - **Microsoft Sikkerhedsløsninger**: Forbedret integrationsvejledning for Prompt Shields, Azure Content Safety, Entra ID og GitHub Advanced Security  
  - **Implementeringsressourcer**: Kategoriserede omfattende ressourcelinks efter Officiel MCP Dokumentation, Microsoft Sikkerhedsløsninger, Sikkerhedsstandarder og Implementeringsvejledninger  

#### Avancerede Sikkerhedskontroller (02-Security/) - Enterprise Implementering  
- **MCP-SECURITY-CONTROLS-2025.md**: Fuldstændig gennemgribende opdatering med enterprise-grade sikkerhedsramme  
  - **9 Omfattende Sikkerhedsområder**: Udvidet fra grundlæggende kontroller til detaljeret enterprise rammeværk  
    - Avanceret Godkendelse & Autorisation med Microsoft Entra ID integration  
    - Token Sikkerhed & Anti-Passthrough Kontroller med omfattende validering  
    - Sessionssikkerhedskontroller med afpresningsforebyggelse  
    - AI-Specifikke Sikkerhedskontroller med prompt injektions- og værktøjforgiftningsbeskyttelse  
    - Forvirret Stedfortræder Angrebsforebyggelse med OAuth proxy sikkerhed  
    - Værktøjsudførelsessikkerhed med sandboxing og isolation  
    - Forsyningskædesikkerhedskontroller med afhængighedsverifikation  
    - Overvågnings- & Detektionskontroller med SIEM-integration  
    - Incident Response & Genopretning med automatiserede funktioner  
  - **Implementeringseksempler**: Tilføjet detaljerede YAML-konfigurationsblokke og kodeeksempler  
  - **Microsoft Løsningsintegration**: Omfattende dækning af Azure sikkerhedstjenester, GitHub Advanced Security og enterprise identitetsadministration  

#### Avancerede Emner Security (05-AdvancedTopics/mcp-security/) - Produktionsklar Implementering  
- **README.md**: Fuldstændig omskrivning for enterprise sikkerhedsimplementering  
  - **Aktuel Specifikationsjustering**: Opdateret til MCP Specifikation 2025-06-18 med obligatoriske sikkerhedskrav  
  - **Forbedret Godkendelse**: Microsoft Entra ID integration med omfattende .NET og Java Spring Security eksempler  
  - **AI Sikkerhedsintegration**: Microsoft Prompt Shields og Azure Content Safety implementering med detaljerede Python-eksempler  
  - **Avanceret Trusselsafværgelse**: Omfattende implementeringseksempler for  
    - Forvirret Stedfortræder Angrebsforebyggelse med PKCE og bruger samtykkevalidering  
    - Token Passthrough Forebyggelse med målgruppevalidering og sikker tokenhåndtering  
    - Sessionskapring Forebyggelse med kryptografisk binding og adfærdsanalyse  
  - **Enterprise Sikkerhedsintegration**: Azure Application Insights overvågning, trusselsdetektionspipeline og forsyningskædesikkerhed  
  - **Implementeringstjekliste**: Klar opdeling af obligatoriske vs. anbefalede sikkerhedskontroller med Microsoft sikkerhedsøkosystemfordele  

### Dokumentationskvalitet & Standardtilpasning  
- **Specifikationshenvisninger**: Opdateret alle henvisninger til nuværende MCP Specifikation 2025-06-18  
- **Microsoft Sikkerhedsøkosystem**: Forbedret integrationsvejledning i hele sikkerhedsdokumentationen  
- **Praktisk Implementering**: Tilføjet detaljerede kodeeksempler i .NET, Java og Python med enterprise mønstre  
- **Ressourceorganisering**: Omfattende kategorisering af officiel dokumentation, sikkerhedsstandarder og implementeringsvejledninger  
- **Visuelle Indikatorer**: Klar markering af obligatoriske krav vs. anbefalede praksisser  

#### Kernekoncepter (01-CoreConcepts/) - Fuld Modernisering  
- **Protokolversionsopdatering**: Opdateret til at referere nuværende MCP Specifikation 2025-06-18 med datobaseret versionering (ÅÅÅÅ-MM-DD format)  
- **Arkitekturforfining**: Forbedrede beskrivelser af Hosts, Clients og Servers for at afspejle aktuelle MCP arkitekturpatterns  
  - Hosts nu klart defineret som AI-applikationer, der koordinerer flere MCP klientforbindelser  
  - Clients beskrevet som protokolconnectorer med one-to-one serverrelationer  
  - Servers forbedret med lokale vs. fjernudrulningsscenarier  
- **Primitive Omstrukturering**: Fuld gennemgang af server- og klientprimitiver  
  - Server Primitiver: Ressourcer (datakilder), Prompts (skabeloner), Værktøjer (udførbare funktioner) med detaljerede forklaringer og eksempler  
  - Klient Primitiver: Sampling (LLM afslutninger), Elicitation (brugerinput), Logging (debugging/overvågning)  
  - Opdateret med aktuelle opdagelses (`*/list`), hentning (`*/get`) og eksekverings (`*/call`) metodepatterns  
- **Protokolarkitektur**: Introduceret to-lags arkitekturmodel  
  - Datalag: JSON-RPC 2.0 fundament med livscyklusstyring og primitivlogik  
  - Transportlag: STDIO (lokal) og Streamable HTTP med SSE (fjern) transportmekanismer  
- **Sikkerhedsrammeværk**: Omfattende sikkerhedsprincipper inklusiv eksplicit bruger samtykke, databeskyttelse, værktøjsudførelsessikkerhed og transportlagsikkerhed  
- **Kommunikationsmønstre**: Opdaterede protokolbeskeder for at vise initialisering, opdagelse, udførelse og meddelelsesflows  
- **Kodeeksempler**: Opfriskede flersprogede eksempler (.NET, Java, Python, JavaScript) for at afspejle aktuelle MCP SDK mønstre  

#### Sikkerhed (02-Security/) - Omfattende Sikkerhedsgennemgang  
- **Standardtilpasning**: Fuld tilpasning til MCP Specifikation 2025-06-18 sikkerhedskrav  
- **Godkendelsesevolution**: Dokumenteret udvikling fra custom OAuth-servere til ekstern identitetsudbyderdelegation (Microsoft Entra ID)  
- **AI-Specifik Trusselsanalyse**: Forbedret dækning af moderne AI angrebsvektorer  
  - Detaljerede prompt injektionsangrebsscenarier med virkelighedsnære eksempler  
  - Værktøjforgiftning og “rug pull” angrebsmønstre  
  - Context window forgiftning og model forvirringsangreb  
- **Microsoft AI Sikkerhedsløsninger**: Omfattende dækning af Microsoft sikkerhedsøkosystem  
  - AI Prompt Shields med avanceret detektion, spotlighting og delimiter teknikker  
  - Azure Content Safety integrationsmønstre  
  - GitHub Advanced Security til forsyningskædebeskyttelse  
- **Avanceret Trusselsafværgelse**: Detaljerede sikkerhedskontroller for  
  - Sessionskapring med MCP-specifikke angrebsscenarier og kryptografiske session ID-krav  
  - Forvirret stedfortræderproblemer i MCP proxy-scenarier med eksplicitte samtykkekrav  
  - Token passthrough sårbarheder med obligatoriske valideringskontroller  
- **Forsyningskædesikkerhed**: Udvidet AI forsyningskædedækning inklusive foundation models, embeddings-tjenester, context providers og tredjeparts API’er  
- **Fondationssikkerhed**: Forbedret integration med enterprise sikkerhedsmønstre inkl. zero trust arkitektur og Microsoft sikkerhedsøkosystem  
- **Ressourceorganisering**: Kategoriserede omfattende ressourcelinks efter type (Officielle Docs, Standarder, Forskning, Microsoft Løsninger, Implementeringsvejledninger)  

### Dokumentationsforbedringer  
- **Strukturerede Læringsmål**: Forbedrede læringsmål med specifikke, handlingsrettede resultater  
- **Krydshenvisninger**: Tilføjet links mellem relaterede sikkerheds- og kernekoncept-emner  
- **Aktuel Information**: Opdateret alle dato- og specifikationshenvisninger til gældende standarder  
- **Implementeringsvejledning**: Tilføjet specifikke, handlingsorienterede implementeringsretningslinjer i begge sektioner  

## 16. juli 2025

### README og Navigation Forbedringer  
- Fuldstændig redesignet curriculum navigation i README.md  
- Udskiftet `<details>` tags med mere tilgængeligt tabelbaseret format  
- Oprettet alternative layoutmuligheder i ny "alternative_layouts" mappe  
- Tilføjet kortbaserede, fanebaserede og accordeon-stil navigationseksempler  
- Opdateret repositoriestruktursektion til at inkludere alle seneste filer  
- Forbedret afsnit om "Hvordan bruges dette curriculum" med klare anbefalinger  
- Opdateret MCP specifikationslinks til korrekte URL’er  
- Tilføjet Context Engineering sektion (5.14) til curriculumstruktur  

### Studieguide Opdateringer  
- Fuldstændig revideret studieguide for at tilpasse til nuværende repositoriestruktur  
- Tilføjet nye sektioner for MCP Clients og Tools, samt Populære MCP Servers  
- Opdateret Visual Curriculum Map til præcis at afspejle alle emner  
- Forbedret beskrivelser af avancerede emner for at dække alle specialiserede områder  
- Opdateret Case Studies sektion til at afspejle faktiske eksempler  
- Tilføjet denne omfattende changelog  

### Community Bidrag (06-CommunityContributions/)  
- Tilføjet detaljeret information om MCP servere til billedgenerering  
- Tilføjet omfattende sektion om brug af Claude i VSCode  
- Tilføjet Cline terminal-klient opsætning og brugervejledning  
- Opdateret MCP klient sektion til at inkludere alle populære klientmuligheder  
- Forbedret bidrageeksempler med mere præcise kodeeksempler  

### Avancerede Emner (05-AdvancedTopics/)  
- Organiseret alle specialiserede emnemapper med konsekvent navngivning  
- Tilføjet materialer og eksempler om context engineering  
- Tilføjet dokumentation for Foundry agent integration  
- Forbedret Entra ID sikkerhedsintegrationsdokumentation  

## 11. juni 2025

### Første Udgivelse  
- Udgav første version af MCP for Beginners curriculum  
- Oprettede grundstruktur for alle 10 hovedsektioner  
- Implementerede Visual Curriculum Map for navigation  
- Tilføjede indledende prøveprojekter i flere programmeringssprog  

### Kom Godt I Gang (03-GettingStarted/)  
- Oprettede første serverimplementeringseksempler  
- Tilføjede klientudviklingsvejledning  
- Inkluderede LLM klientintegrationsinstruktioner  
- Tilføjede VS Code integrationsdokumentation  
- Implementerede Server-Sent Events (SSE) servereksempler  

### Kernekoncepter (01-CoreConcepts/)  
- Tilføjede detaljeret forklaring af klient-server arkitektur  
- Oprettede dokumentation om nøgleprotokolkomponenter  
- Dokumenterede beskedmønstre i MCP  

## 23. maj 2025

### Repository Struktur  
- Initialiserede repository med grundlæggende mappestruktur  
- Oprettede README-filer for hver hovedsektion  
- Opsatte oversættelsesinfrastruktur  
- Tilføjede billedelementer og diagrammer  

### Dokumentation  
- Oprettede indledende README.md med curriculumoversigt  
- Tilføjede CODE_OF_CONDUCT.md og SECURITY.md  
- Opsatte SUPPORT.md med vejledning til hjælp  
- Oprettede foreløbig studieguide struktur  

## 15. april 2025

### Planlægning og Rammeværk  
- Første planlægning af MCP for Beginners curriculum  
- Definerede læringsmål og målgruppe  
- Skitserede 10-sektions struktur for curriculum  
- Udviklede konceptuelt rammeværk for eksempler og case studies  
- Oprettede indledende prototypeeksempler for nøglebegreber

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
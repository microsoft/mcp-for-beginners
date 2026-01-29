# Model Context Protocol (MCP) voor Beginners - Studiegids

Deze studiegids biedt een overzicht van de structuur en inhoud van de repository voor het curriculum "Model Context Protocol (MCP) voor Beginners". Gebruik deze gids om de repository efficiënt te navigeren en optimaal gebruik te maken van de beschikbare bronnen.

## Overzicht van de Repository

Het Model Context Protocol (MCP) is een gestandaardiseerd raamwerk voor interacties tussen AI-modellen en clienttoepassingen. Oorspronkelijk ontwikkeld door Anthropic, wordt MCP nu onderhouden door de bredere MCP-community via de officiële GitHub-organisatie. Deze repository biedt een uitgebreid curriculum met praktische codevoorbeelden in C#, Java, JavaScript, Python en TypeScript, ontworpen voor AI-ontwikkelaars, systeemarchitecten en software-engineers.

## Visuele Curriculumkaart

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Structuur van de Repository

De repository is georganiseerd in elf hoofdsecties, elk gericht op verschillende aspecten van MCP:

1. **Introductie (00-Introduction/)**
   - Overzicht van het Model Context Protocol
   - Waarom standaardisatie belangrijk is in AI-pijplijnen
   - Praktische toepassingen en voordelen

2. **Kernconcepten (01-CoreConcepts/)**
   - Client-serverarchitectuur
   - Belangrijke protocolcomponenten
   - Messagingpatronen in MCP

3. **Beveiliging (02-Security/)**
   - Beveiligingsrisico's in MCP-gebaseerde systemen
   - Best practices voor het beveiligen van implementaties
   - Authenticatie- en autorisatiestrategieën
   - **Uitgebreide Beveiligingsdocumentatie**:
     - MCP Security Best Practices 2025
     - Azure Content Safety Implementation Guide
     - MCP Security Controls and Techniques
     - MCP Best Practices Quick Reference
   - **Belangrijke Beveiligingsthema's**:
     - Prompt injection en tool poisoning-aanvallen
     - Sessiekaping en confused deputy-problemen
     - Token passthrough-kwetsbaarheden
     - Overmatige machtigingen en toegangscontrole
     - Beveiliging van de toeleveringsketen voor AI-componenten
     - Microsoft Prompt Shields-integratie

4. **Aan de slag (03-GettingStarted/)**
   - Omgevingsinstellingen en configuratie
   - Basis MCP-servers en -clients maken
   - Integratie met bestaande toepassingen
   - Inclusief secties voor:
     - Eerste serverimplementatie
     - Clientontwikkeling
     - LLM-clientintegratie
     - VS Code-integratie
     - Server-Sent Events (SSE) server
     - Geavanceerd servergebruik
     - HTTP-streaming
     - AI Toolkit-integratie
     - Teststrategieën
     - Implementatierichtlijnen

5. **Praktische Implementatie (04-PracticalImplementation/)**
   - Gebruik van SDK's in verschillende programmeertalen
   - Debugging-, test- en validatietechnieken
   - Herbruikbare prompttemplates en workflows maken
   - Voorbeeldprojecten met implementatievoorbeelden

6. **Geavanceerde Onderwerpen (05-AdvancedTopics/)**
   - Context engineering technieken
   - Foundry agent-integratie
   - Multi-modale AI-workflows
   - OAuth2-authenticatiedemo's
   - Real-time zoekmogelijkheden
   - Real-time streaming
   - Root contexts implementatie
   - Routeringsstrategieën
   - Samplingtechnieken
   - Schaalmethoden
   - Beveiligingsoverwegingen
   - Entra ID-beveiligingsintegratie
   - Webzoekintegratie

7. **Communitybijdragen (06-CommunityContributions/)**
   - Hoe code en documentatie bij te dragen
   - Samenwerken via GitHub
   - Communitygedreven verbeteringen en feedback
   - Gebruik van verschillende MCP-clients (Claude Desktop, Cline, VSCode)
   - Werken met populaire MCP-servers, inclusief beeldgeneratie

8. **Lessen uit Vroege Adoptie (07-LessonsfromEarlyAdoption/)**
   - Implementaties en succesverhalen uit de praktijk
   - MCP-gebaseerde oplossingen bouwen en implementeren
   - Trends en toekomstige roadmap
   - **Microsoft MCP Servers Guide**: Uitgebreide gids voor 10 productieklare Microsoft MCP-servers, waaronder:
     - Microsoft Learn Docs MCP Server
     - Azure MCP Server (15+ gespecialiseerde connectors)
     - GitHub MCP Server
     - Azure DevOps MCP Server
     - MarkItDown MCP Server
     - SQL Server MCP Server
     - Playwright MCP Server
     - Dev Box MCP Server
     - Azure AI Foundry MCP Server
     - Microsoft 365 Agents Toolkit MCP Server

9. **Best Practices (08-BestPractices/)**
   - Prestatieoptimalisatie
   - Ontwerpen van fouttolerante MCP-systemen
   - Test- en veerkrachtstrategieën

10. **Case Studies (09-CaseStudy/)**
    - **Zeven uitgebreide case studies** die de veelzijdigheid van MCP demonstreren in diverse scenario's:
    - **Azure AI Travel Agents**: Multi-agent orkestratie met Azure OpenAI en AI Search
    - **Azure DevOps Integratie**: Workflowprocessen automatiseren met YouTube-data-updates
    - **Real-Time Documentatieophaling**: Python-consoleclient met HTTP-streaming
    - **Interactieve Studieplan Generator**: Chainlit-webapp met conversatie-AI
    - **In-Editor Documentatie**: VS Code-integratie met GitHub Copilot-workflows
    - **Azure API Management**: Enterprise API-integratie met MCP-servercreatie
    - **GitHub MCP Registry**: Ecosysteemontwikkeling en agentische integratieplatform
    - Implementatievoorbeelden variërend van enterprise-integratie, ontwikkelaarsproductiviteit tot ecosysteemontwikkeling

11. **Hands-on Workshop (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Uitgebreide hands-on workshop die MCP combineert met AI Toolkit
    - Intelligente toepassingen bouwen die AI-modellen verbinden met echte tools
    - Praktische modules die de basis, aangepaste serverontwikkeling en productie-implementatiestrategieën behandelen
    - **Labstructuur**:
      - Lab 1: MCP Server Fundamentals
      - Lab 2: Geavanceerde MCP Server Ontwikkeling
      - Lab 3: AI Toolkit Integratie
      - Lab 4: Productie-implementatie en Schaling
    - Lab-gebaseerde leerbenadering met stapsgewijze instructies

12. **MCP Server Database Integratie Labs (11-MCPServerHandsOnLabs/)**
    - **Uitgebreid 13-lab leerpad** voor het bouwen van productieklare MCP-servers met PostgreSQL-integratie
    - **Praktische retailanalyse-implementatie** met de Zava Retail use case
    - **Enterprise-grade patronen** inclusief Row Level Security (RLS), semantisch zoeken en multi-tenant data toegang
    - **Volledige Labstructuur**:
      - **Labs 00-03: Basis** - Introductie, Architectuur, Beveiliging, Omgevingsinstelling
      - **Labs 04-06: MCP Server Bouwen** - Databaseontwerp, MCP Server Implementatie, Toolontwikkeling
      - **Labs 07-09: Geavanceerde Functies** - Semantisch Zoeken, Testen & Debuggen, VS Code Integratie
      - **Labs 10-12: Productie & Best Practices** - Implementatie, Monitoring, Optimalisatie
    - **Technologieën Gedekt**: FastMCP framework, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Leerresultaten**: Productieklare MCP-servers, database-integratiepatronen, AI-gestuurde analyses, enterprise-beveiliging

## Aanvullende Bronnen

De repository bevat ondersteunende bronnen:

- **Afbeeldingenmap**: Bevat diagrammen en illustraties die door het curriculum worden gebruikt
- **Vertalingen**: Meertalige ondersteuning met geautomatiseerde vertalingen van documentatie
- **Officiële MCP Bronnen**:
  - [MCP Documentatie](https://modelcontextprotocol.io/)
  - [MCP Specificatie](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub Repository](https://github.com/modelcontextprotocol)

## Hoe deze Repository te Gebruiken

1. **Sequentieel Leren**: Volg de hoofdstukken in volgorde (00 tot 11) voor een gestructureerde leerervaring.
2. **Taal-specifieke Focus**: Als je geïnteresseerd bent in een specifieke programmeertaal, verken de voorbeeldmappen voor implementaties in jouw voorkeurstaal.
3. **Praktische Implementatie**: Begin met de sectie "Aan de slag" om je omgeving in te stellen en je eerste MCP-server en -client te maken.
4. **Geavanceerde Verkenning**: Zodra je vertrouwd bent met de basis, duik in de geavanceerde onderwerpen om je kennis uit te breiden.
5. **Community Betrokkenheid**: Word lid van de MCP-community via GitHub-discussies en Discord-kanalen om in contact te komen met experts en mede-ontwikkelaars.

## MCP Clients en Tools

Het curriculum behandelt verschillende MCP-clients en tools:

1. **Officiële Clients**:
   - Visual Studio Code 
   - MCP in Visual Studio Code
   - Claude Desktop
   - Claude in VSCode 
   - Claude API

2. **Community Clients**:
   - Cline (terminal-gebaseerd)
   - Cursor (code-editor)
   - ChatMCP
   - Windsurf

3. **MCP Beheertools**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Populaire MCP Servers

De repository introduceert verschillende MCP-servers, waaronder:

1. **Officiële Microsoft MCP Servers**:
   - Microsoft Learn Docs MCP Server
   - Azure MCP Server (15+ gespecialiseerde connectors)
   - GitHub MCP Server
   - Azure DevOps MCP Server
   - MarkItDown MCP Server
   - SQL Server MCP Server
   - Playwright MCP Server
   - Dev Box MCP Server
   - Azure AI Foundry MCP Server
   - Microsoft 365 Agents Toolkit MCP Server

2. **Officiële Referentie Servers**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Beeldgeneratie**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Ontwikkelingstools**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Gespecialiseerde Servers**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Bijdragen

Deze repository verwelkomt bijdragen van de community. Zie de sectie Communitybijdragen voor richtlijnen over hoe je effectief kunt bijdragen aan het MCP-ecosysteem.

----

*Deze studiegids is bijgewerkt op 6 oktober 2025 en biedt een overzicht van de repository zoals die op die datum was. De inhoud van de repository kan na deze datum worden bijgewerkt.*

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
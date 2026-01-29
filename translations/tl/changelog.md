# Changelog: MCP para sa Mga Nagsisimula na Kurikulum

Ang dokumentong ito ay nagsisilbing talaan ng lahat ng mahahalagang pagbabago na ginawa sa Model Context Protocol (MCP) para sa kurikulum ng mga nagsisimula. Ang mga pagbabago ay naitala sa reverse chronological order (pinakabago muna).

## Disyembre 18, 2025

### Update sa Dokumentasyon ng Seguridad - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Update ng Bersyon ng Specification
- **Update ng Bersyon ng Protocol**: In-update upang i-refer ang pinakabagong MCP Specification 2025-11-25 (nilabas noong Nobyembre 25, 2025)
  - In-update ang lahat ng reference sa bersyon ng specification mula 2025-06-18 hanggang 2025-11-25
  - In-update ang mga petsa ng dokumento mula Agosto 18, 2025 hanggang Disyembre 18, 2025
  - Natiyak na lahat ng URL ng specification ay tumutukoy sa kasalukuyang dokumentasyon
- **Pag-validate ng Nilalaman**: Komprehensibong pag-validate ng mga best practices sa seguridad laban sa pinakabagong mga pamantayan
  - **Microsoft Security Solutions**: Natiyak ang kasalukuyang terminolohiya at mga link para sa Prompt Shields (dating "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, at Azure Key Vault
  - **OAuth 2.1 Security**: Nakumpirma ang pagsunod sa pinakabagong OAuth security best practices
  - **OWASP Standards**: Natiyak na ang mga reference sa OWASP Top 10 para sa LLMs ay nananatiling kasalukuyan
  - **Azure Services**: Natiyak ang lahat ng Microsoft Azure documentation links at best practices
- **Pagsunod sa Pamantayan**: Lahat ng tinukoy na security standards ay kumpirmadong kasalukuyan
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security at compliance frameworks
- **Mga Resources para sa Implementasyon**: Natiyak ang lahat ng mga link at resources para sa implementation guide
  - Azure API Management authentication patterns
  - Microsoft Entra ID integration guides
  - Azure Key Vault secrets management
  - DevSecOps pipelines at monitoring solutions

### Quality Assurance ng Dokumentasyon
- **Pagsunod sa Specification**: Tiniyak na lahat ng mandatory MCP security requirements (MUST/MUST NOT) ay naka-align sa pinakabagong specification
- **Kasalukuyang Resources**: Natiyak ang lahat ng external links sa Microsoft documentation, security standards, at implementation guides
- **Saklaw ng Best Practices**: Nakumpirma ang komprehensibong saklaw ng authentication, authorization, AI-specific threats, supply chain security, at enterprise patterns

## Oktubre 6, 2025

### Pagpapalawak ng Seksyon ng Pagsisimula – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **Bagong Kabanata**: Inilunsad ang komprehensibong gabay sa advanced MCP server usage, na sumasaklaw sa parehong regular at low-level server architectures.
  - **Regular vs. Low-Level Server**: Detalyadong paghahambing at mga halimbawa ng code sa Python at TypeScript para sa parehong pamamaraan.
  - **Handler-Based Design**: Paliwanag ng handler-based tool/resource/prompt management para sa scalable, flexible na server implementations.
  - **Praktikal na Mga Pattern**: Mga totoong senaryo kung saan kapaki-pakinabang ang low-level server patterns para sa advanced features at architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **Bagong Kabanata**: Step-by-step na gabay sa pagpapatupad ng simple authentication sa MCP servers.
  - **Mga Konsepto ng Auth**: Malinaw na paliwanag ng authentication vs. authorization, at paghawak ng credentials.
  - **Basic Auth Implementation**: Middleware-based authentication patterns sa Python (Starlette) at TypeScript (Express), na may mga halimbawa ng code.
  - **Pag-usad sa Advanced Security**: Gabay sa pagsisimula sa simple auth at pag-advance sa OAuth 2.1 at RBAC, na may mga reference sa advanced security modules.

Ang mga dagdag na ito ay nagbibigay ng praktikal, hands-on na gabay para sa pagbuo ng mas matibay, ligtas, at flexible na MCP server implementations, na nag-uugnay ng mga pundamental na konsepto sa mga advanced na production patterns.

## Setyembre 29, 2025

### MCP Server Database Integration Labs - Komprehensibong Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - Bagong Kumpletong Database Integration Curriculum
- **Kumpletong 13-Lab Learning Path**: Idinagdag ang komprehensibong hands-on curriculum para sa pagbuo ng production-ready MCP servers na may PostgreSQL database integration
  - **Totoong Implementasyon**: Zava Retail analytics use case na nagpapakita ng enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Panimula, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL na may pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Komprehensibong Update ng Dokumentasyon**: Sistematikong in-update ang lahat ng README files sa 11-MCPServerHandsOnLabs upang gamitin ang terminong "Lab" sa halip na "Module"
  - **Mga Header ng Seksyon**: In-update ang "What This Module Covers" sa "What This Lab Covers" sa lahat ng 13 labs
  - **Paglalarawan ng Nilalaman**: Pinalitan ang "This module provides..." ng "This lab provides..." sa buong dokumentasyon
  - **Mga Layunin sa Pagkatuto**: In-update ang "By the end of this module..." sa "By the end of this lab..."
  - **Mga Link sa Navigasyon**: Pinalitan ang lahat ng "Module XX:" references sa "Lab XX:" sa cross-references at navigasyon
  - **Pagsubaybay sa Pagtatapos**: In-update ang "After completing this module..." sa "After completing this lab..."
  - **Napanatili ang Mga Teknikal na Reference**: Pinanatili ang mga Python module references sa configuration files (hal., `"module": "mcp_server.main"`)

#### Pagpapahusay ng Study Guide (study_guide.md)
- **Visual Curriculum Map**: Idinagdag ang bagong seksyon na "11. Database Integration Labs" na may komprehensibong visualisasyon ng istruktura ng lab
- **Istruktura ng Repository**: In-update mula sampu hanggang labing-isang pangunahing seksyon na may detalyadong paglalarawan ng 11-MCPServerHandsOnLabs
- **Gabayan sa Learning Path**: Pinahusay ang mga tagubilin sa navigasyon upang saklawin ang mga seksyon 00-11
- **Saklaw ng Teknolohiya**: Idinagdag ang FastMCP, PostgreSQL, at detalye ng Azure services integration
- **Mga Resulta ng Pagkatuto**: Binigyang-diin ang production-ready server development, database integration patterns, at enterprise security

#### Pagpapahusay ng Pangunahing README Structure
- **Terminolohiyang Batay sa Lab**: In-update ang pangunahing README.md sa 11-MCPServerHandsOnLabs upang palaging gamitin ang "Lab" na istruktura
- **Organisasyon ng Learning Path**: Malinaw na pag-usad mula sa pundamental na mga konsepto hanggang sa advanced na implementasyon at production deployment
- **Pokus sa Totoong Mundo**: Binibigyang-diin ang praktikal, hands-on na pagkatuto gamit ang enterprise-grade patterns at teknolohiya

### Pagpapahusay ng Kalidad at Konsistensi ng Dokumentasyon
- **Pokus sa Hands-On Learning**: Pinatibay ang praktikal, lab-based na pamamaraan sa buong dokumentasyon
- **Pokus sa Enterprise Patterns**: Binanggit ang production-ready implementations at mga konsiderasyon sa enterprise security
- **Integrasyon ng Teknolohiya**: Komprehensibong saklaw ng modernong Azure services at AI integration patterns
- **Pag-usad ng Pagkatuto**: Malinaw, istrukturadong landas mula sa mga pangunahing konsepto hanggang sa production deployment

## Setyembre 26, 2025

### Pagpapahusay ng Case Studies - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Pokus sa Pag-unlad ng Ecosystem
- **README.md**: Malawakang pagpapalawak na may komprehensibong GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Bagong komprehensibong case study na sinusuri ang paglulunsad ng GitHub MCP Registry noong Setyembre 2025
    - **Pagsusuri ng Problema**: Detalyadong pagsusuri ng fragmented MCP server discovery at deployment challenges
    - **Arkitektura ng Solusyon**: Centralized registry approach ng GitHub na may one-click VS Code installation
    - **Epekto sa Negosyo**: Nasusukat na pagpapabuti sa developer onboarding at productivity
    - **Halaga sa Estratehiya**: Pokus sa modular agent deployment at cross-tool interoperability
    - **Pag-unlad ng Ecosystem**: Posisyon bilang pundamental na platform para sa agentic integration
  - **Pinahusay na Istruktura ng Case Study**: In-update ang lahat ng pitong case studies na may pare-parehong format at komprehensibong paglalarawan
    - Azure AI Travel Agents: Pokus sa multi-agent orchestration
    - Azure DevOps Integration: Pokus sa workflow automation
    - Real-Time Documentation Retrieval: Implementasyon ng Python console client
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code at GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Pag-unlad ng ecosystem at community platform
  - **Komprehensibong Konklusyon**: Muling isinulat na seksyon ng konklusyon na nagha-highlight ng pitong case studies na sumasaklaw sa maraming dimensyon ng MCP implementation
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications na kategorya
    - Pinahusay na mga insight sa architectural patterns, implementation strategies, at best practices
    - Binibigyang-diin ang MCP bilang mature, production-ready protocol

#### Mga Update sa Study Guide (study_guide.md)
- **Visual Curriculum Map**: In-update ang mindmap upang isama ang GitHub MCP Registry sa Case Studies section
- **Paglalarawan ng Case Studies**: Pinahusay mula sa generic na mga paglalarawan patungo sa detalyadong breakdown ng pitong komprehensibong case studies
- **Istruktura ng Repository**: In-update ang seksyon 10 upang ipakita ang komprehensibong saklaw ng case study na may partikular na detalye ng implementasyon
- **Integrasyon ng Changelog**: Idinagdag ang entry ng Setyembre 26, 2025 na nagdodokumento ng pagdagdag ng GitHub MCP Registry at pagpapahusay ng case studies
- **Pag-update ng Petsa**: In-update ang footer timestamp upang ipakita ang pinakabagong rebisyon (Setyembre 26, 2025)

### Pagpapahusay ng Kalidad ng Dokumentasyon
- **Pagpapahusay ng Konsistensi**: Standardisadong format at istruktura ng case study sa lahat ng pitong halimbawa
- **Komprehensibong Saklaw**: Ang mga case studies ay sumasaklaw na ngayon sa enterprise, developer productivity, at ecosystem development scenarios
- **Estratehikong Posisyon**: Pinahusay na pokus sa MCP bilang pundamental na platform para sa deployment ng agentic system
- **Integrasyon ng Resources**: In-update ang karagdagang mga resources upang isama ang link ng GitHub MCP Registry

## Setyembre 15, 2025

### Pagpapalawak ng Advanced Topics - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Bagong Advanced Implementation Guide
- **README.md**: Kumpletong gabay sa implementasyon para sa custom MCP transport mechanisms
  - **Azure Event Grid Transport**: Komprehensibong serverless event-driven transport implementation
    - Mga halimbawa sa C#, TypeScript, at Python na may Azure Functions integration
    - Mga pattern ng event-driven architecture para sa scalable MCP solutions
    - Webhook receivers at push-based message handling
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation
    - Real-time streaming capabilities para sa low-latency scenarios
    - Mga partitioning strategy at checkpoint management
    - Message batching at performance optimization
  - **Enterprise Integration Patterns**: Production-ready architectural examples
    - Distributed MCP processing sa maraming Azure Functions
    - Hybrid transport architectures na pinagsasama ang iba't ibang uri ng transport
    - Mga strategy para sa message durability, reliability, at error handling
  - **Seguridad at Monitoring**: Azure Key Vault integration at observability patterns
    - Managed identity authentication at least privilege access
    - Application Insights telemetry at performance monitoring
    - Circuit breakers at fault tolerance patterns
  - **Testing Frameworks**: Komprehensibong testing strategies para sa custom transports
    - Unit testing gamit ang test doubles at mocking frameworks
    - Integration testing gamit ang Azure Test Containers
    - Mga konsiderasyon sa performance at load testing

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Lumalabas na Disiplina sa AI
- **README.md**: Komprehensibong eksplorasyon ng context engineering bilang lumalabas na larangan
  - **Pangunahing Prinsipyo**: Kumpletong pagbabahagi ng context, awareness sa action decision, at pamamahala ng context window
  - **Pagsunod sa MCP Protocol**: Paano tinutugunan ng disenyo ng MCP ang mga hamon sa context engineering
    - Mga limitasyon ng context window at progressive loading strategies
    - Pagtukoy ng relevance at dynamic context retrieval
    - Multi-modal context handling at mga konsiderasyon sa seguridad
  - **Mga Paraan ng Implementasyon**: Single-threaded vs. multi-agent architectures
    - Context chunking at prioritization techniques
    - Progressive context loading at compression strategies
    - Layered context approaches at retrieval optimization
  - **Measurement Framework**: Lumalabas na mga metrics para sa pagsusuri ng bisa ng context
    - Input efficiency, performance, quality, at user experience considerations
    - Mga experimental na pamamaraan sa context optimization
    - Failure analysis at mga metodolohiya para sa pagpapabuti

#### Mga Update sa Navigation ng Kurikulum (README.md)
- **Pinahusay na Istruktura ng Module**: In-update ang curriculum table upang isama ang mga bagong advanced topics
  - Idinagdag ang Context Engineering (5.14) at Custom Transport (5.15) na mga entry
  - Pare-parehong format at mga link sa navigasyon sa lahat ng modules
  - In-update ang mga paglalarawan upang ipakita ang kasalukuyang saklaw ng nilalaman

### Pagpapahusay ng Istruktura ng Direktoryo
- **Standardisasyon ng Pangalan**: Pinalitan ang "mcp transport" ng "mcp-transport" para sa konsistensi sa ibang advanced topic folders
- **Organisasyon ng Nilalaman**: Lahat ng 05-AdvancedTopics folders ay sumusunod na sa pare-parehong naming pattern (mcp-[topic])

### Pagpapahusay ng Kalidad ng Dokumentasyon
- **Pagsunod sa MCP Specification**: Lahat ng bagong nilalaman ay nagre-refer sa kasalukuyang MCP Specification 2025-06-18
- **Mga Halimbawa sa Maramihang Wika**: Komprehensibong mga halimbawa ng code sa C#, TypeScript, at Python
- **Pokus sa Enterprise**: Production-ready patterns at Azure cloud integration sa buong dokumentasyon
- **Visual na Dokumentasyon**: Mermaid diagrams para sa arkitektura at flow visualization

## Agosto 18, 2025

### Komprehensibong Update ng Dokumentasyon - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Kumpletong Modernisasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kumpletong muling pagsulat na naka-align sa MCP Specification 2025-06-18
  - **Mga Mandatoryong Kinakailangan**: Idinagdag ang tahasang MUST/MUST NOT na mga kinakailangan mula sa opisyal na espesipikasyon na may malinaw na mga visual na palatandaan
  - **12 Pangunahing Praktis sa Seguridad**: Muling inayos mula sa 15-item na listahan patungo sa komprehensibong mga domain ng seguridad
    - Seguridad ng Token at Pagpapatunay gamit ang integrasyon ng panlabas na tagapagbigay ng pagkakakilanlan
    - Pamamahala ng Session at Seguridad sa Transportasyon na may mga kinakailangang kriptograpiko
    - AI-Specific Threat Protection na may integrasyon ng Microsoft Prompt Shields
    - Kontrol sa Access at Mga Pahintulot gamit ang prinsipyo ng pinakamababang pribilehiyo
    - Kaligtasan ng Nilalaman at Pagsubaybay gamit ang integrasyon ng Azure Content Safety
    - Seguridad ng Supply Chain na may komprehensibong beripikasyon ng mga bahagi
    - Seguridad ng OAuth at Pag-iwas sa Confused Deputy gamit ang implementasyon ng PKCE
    - Pagtugon sa Insidente at Pagbawi na may mga awtomatikong kakayahan
    - Pagsunod at Pamamahala na may pagsunod sa regulasyon
    - Mga Advanced na Kontrol sa Seguridad gamit ang zero trust architecture
    - Integrasyon ng Microsoft Security Ecosystem na may komprehensibong mga solusyon
    - Patuloy na Ebolusyon ng Seguridad gamit ang mga adaptive na praktis
  - **Mga Solusyon sa Seguridad ng Microsoft**: Pinahusay na gabay sa integrasyon para sa Prompt Shields, Azure Content Safety, Entra ID, at GitHub Advanced Security
  - **Mga Mapagkukunan sa Implementasyon**: Inuri ang komprehensibong mga link ng mapagkukunan ayon sa Opisyal na Dokumentasyon ng MCP, Mga Solusyon sa Seguridad ng Microsoft, Mga Pamantayan sa Seguridad, at Mga Gabay sa Implementasyon

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Kumpletong pagbabago gamit ang enterprise-grade na balangkas ng seguridad
  - **9 Komprehensibong Domain ng Seguridad**: Pinalawak mula sa mga pangunahing kontrol patungo sa detalyadong balangkas ng enterprise
    - Advanced Authentication at Authorization na may integrasyon ng Microsoft Entra ID
    - Seguridad ng Token at Anti-Passthrough Controls na may komprehensibong beripikasyon
    - Mga Kontrol sa Seguridad ng Session na may pag-iwas sa pag-hijack
    - AI-Specific Security Controls na may pag-iwas sa prompt injection at tool poisoning
    - Pag-iwas sa Confused Deputy Attack gamit ang seguridad ng OAuth proxy
    - Seguridad sa Pagpapatakbo ng Tool gamit ang sandboxing at isolation
    - Mga Kontrol sa Seguridad ng Supply Chain na may beripikasyon ng dependency
    - Mga Kontrol sa Pagsubaybay at Pag-detect na may integrasyon ng SIEM
    - Pagtugon sa Insidente at Pagbawi na may mga awtomatikong kakayahan
  - **Mga Halimbawa ng Implementasyon**: Idinagdag ang detalyadong mga YAML configuration block at mga halimbawa ng code
  - **Integrasyon ng Microsoft Solutions**: Komprehensibong saklaw ng mga serbisyo sa seguridad ng Azure, GitHub Advanced Security, at pamamahala ng pagkakakilanlan ng enterprise

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Kumpletong muling pagsulat para sa enterprise security implementation
  - **Kasulukuyang Pagsunod sa Espesipikasyon**: Na-update sa MCP Specification 2025-06-18 na may mga mandatoryong kinakailangan sa seguridad
  - **Pinahusay na Authentication**: Integrasyon ng Microsoft Entra ID na may komprehensibong mga halimbawa sa .NET at Java Spring Security
  - **Integrasyon ng AI Security**: Implementasyon ng Microsoft Prompt Shields at Azure Content Safety na may detalyadong mga halimbawa sa Python
  - **Advanced Threat Mitigation**: Komprehensibong mga halimbawa ng implementasyon para sa
    - Pag-iwas sa Confused Deputy Attack gamit ang PKCE at beripikasyon ng pahintulot ng user
    - Pag-iwas sa Token Passthrough gamit ang beripikasyon ng audience at secure na pamamahala ng token
    - Pag-iwas sa Session Hijacking gamit ang cryptographic binding at behavioral analysis
  - **Integrasyon ng Enterprise Security**: Pagsubaybay gamit ang Azure Application Insights, mga pipeline ng pagtuklas ng banta, at seguridad ng supply chain
  - **Checklist ng Implementasyon**: Malinaw na mga mandatoryo laban sa inirerekomendang mga kontrol sa seguridad na may mga benepisyo ng Microsoft security ecosystem

### Kalidad ng Dokumentasyon at Pagsunod sa Pamantayan
- **Mga Sanggunian sa Espesipikasyon**: Na-update ang lahat ng sanggunian sa kasalukuyang MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Pinahusay na gabay sa integrasyon sa buong dokumentasyon ng seguridad
- **Praktikal na Implementasyon**: Idinagdag ang detalyadong mga halimbawa ng code sa .NET, Java, at Python na may mga pattern ng enterprise
- **Organisasyon ng Mapagkukunan**: Komprehensibong pag-uuri ng opisyal na dokumentasyon, mga pamantayan sa seguridad, at mga gabay sa implementasyon
- **Mga Visual na Palatandaan**: Malinaw na pagmamarka ng mga mandatoryong kinakailangan laban sa mga inirerekomendang praktis


#### Core Concepts (01-CoreConcepts/) - Kumpletong Modernisasyon
- **Pag-update ng Bersyon ng Protocol**: Na-update upang tukuyin ang kasalukuyang MCP Specification 2025-06-18 na may petsa bilang bersyon (format na YYYY-MM-DD)
- **Pagpino ng Arkitektura**: Pinahusay na mga paglalarawan ng Hosts, Clients, at Servers upang ipakita ang kasalukuyang mga pattern ng arkitektura ng MCP
  - Ang mga Hosts ay malinaw na tinukoy bilang mga AI application na nag-uugnay ng maraming koneksyon ng MCP client
  - Ang mga Clients ay inilalarawan bilang mga protocol connector na nagpapanatili ng one-to-one na relasyon sa server
  - Ang mga Servers ay pinahusay na may mga lokal laban sa remote na mga senaryo ng deployment
- **Muling Pag-aayos ng Primitive**: Kumpletong pagbabago ng mga primitive ng server at client
  - Mga Primitive ng Server: Mga Resources (pinagmumulan ng data), Prompts (mga template), Tools (mga executable na function) na may detalyadong paliwanag at mga halimbawa
  - Mga Primitive ng Client: Sampling (LLM completions), Elicitation (input ng user), Logging (debugging/pagsubaybay)
  - Na-update gamit ang kasalukuyang mga pattern ng discovery (`*/list`), retrieval (`*/get`), at execution (`*/call`)
- **Arkitektura ng Protocol**: Ipinakilala ang dalawang-layer na modelo ng arkitektura
  - Data Layer: JSON-RPC 2.0 na pundasyon na may lifecycle management at mga primitive
  - Transport Layer: STDIO (lokal) at Streamable HTTP na may SSE (remote) na mga mekanismo ng transportasyon
- **Balangkas ng Seguridad**: Komprehensibong mga prinsipyo ng seguridad kabilang ang tahasang pahintulot ng user, proteksyon sa privacy ng data, kaligtasan sa pagpapatakbo ng tool, at seguridad sa transport layer
- **Mga Pattern ng Komunikasyon**: Na-update ang mga mensahe ng protocol upang ipakita ang initialization, discovery, execution, at notification flows
- **Mga Halimbawa ng Code**: Na-refresh ang mga halimbawa sa maraming wika (.NET, Java, Python, JavaScript) upang ipakita ang kasalukuyang mga pattern ng MCP SDK

#### Security (02-Security/) - Komprehensibong Pagbabago sa Seguridad  
- **Pagsunod sa Pamantayan**: Buong pagsunod sa mga kinakailangan sa seguridad ng MCP Specification 2025-06-18
- **Ebolusyon ng Authentication**: Naidokumento ang ebolusyon mula sa custom OAuth servers patungo sa delegasyon ng panlabas na tagapagbigay ng pagkakakilanlan (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Pinahusay na saklaw ng mga modernong AI attack vector
  - Detalyadong mga senaryo ng prompt injection attack na may mga totoong halimbawa
  - Mga mekanismo ng tool poisoning at mga pattern ng "rug pull" attack
  - Pagkalason ng context window at mga pag-atake sa kalituhan ng modelo
- **Mga Solusyon sa Seguridad ng Microsoft AI**: Komprehensibong saklaw ng Microsoft security ecosystem
  - AI Prompt Shields na may advanced detection, spotlighting, at delimiter techniques
  - Mga pattern ng integrasyon ng Azure Content Safety
  - GitHub Advanced Security para sa proteksyon ng supply chain
- **Advanced Threat Mitigation**: Detalyadong mga kontrol sa seguridad para sa
  - Session hijacking na may mga senaryo ng pag-atake na partikular sa MCP at mga kinakailangan sa cryptographic session ID
  - Mga problema sa confused deputy sa mga senaryo ng MCP proxy na may tahasang mga kinakailangan sa pahintulot
  - Mga kahinaan sa token passthrough na may mga mandatoryong kontrol sa beripikasyon
- **Seguridad ng Supply Chain**: Pinalawak na saklaw ng AI supply chain kabilang ang mga foundation model, embedding services, context providers, at third-party APIs
- **Seguridad ng Foundation**: Pinahusay na integrasyon gamit ang mga pattern ng enterprise security kabilang ang zero trust architecture at Microsoft security ecosystem
- **Organisasyon ng Mapagkukunan**: Inuri ang komprehensibong mga link ng mapagkukunan ayon sa uri (Opisyal na Docs, Pamantayan, Pananaliksik, Mga Solusyon ng Microsoft, Mga Gabay sa Implementasyon)

### Mga Pagpapabuti sa Kalidad ng Dokumentasyon
- **Istrakturadong Mga Layunin sa Pagkatuto**: Pinahusay na mga layunin sa pagkatuto na may mga tiyak at magagawa na resulta
- **Cross-References**: Idinagdag ang mga link sa pagitan ng mga kaugnay na paksa sa seguridad at pangunahing konsepto
- **Kasalukuyang Impormasyon**: Na-update ang lahat ng mga petsa at mga link ng espesipikasyon sa kasalukuyang mga pamantayan
- **Gabay sa Implementasyon**: Idinagdag ang mga tiyak at magagawa na mga gabay sa implementasyon sa buong mga seksyon

## Hulyo 16, 2025

### README at Mga Pagpapabuti sa Navigasyon
- Ganap na muling idinisenyo ang curriculum navigation sa README.md
- Pinalitan ang mga `<details>` tag ng mas accessible na format na batay sa talahanayan
- Nilikha ang mga alternatibong layout na opsyon sa bagong folder na "alternative_layouts"
- Idinagdag ang mga halimbawa ng card-based, tabbed-style, at accordion-style na navigasyon
- Na-update ang seksyon ng istruktura ng repository upang isama ang lahat ng pinakabagong mga file
- Pinahusay ang seksyon na "How to Use This Curriculum" na may malinaw na mga rekomendasyon
- Na-update ang mga link ng MCP specification upang ituro sa tamang mga URL
- Idinagdag ang seksyon ng Context Engineering (5.14) sa istruktura ng curriculum

### Mga Update sa Study Guide
- Ganap na nirebisa ang study guide upang umayon sa kasalukuyang istruktura ng repository
- Idinagdag ang mga bagong seksyon para sa MCP Clients at Tools, at Popular MCP Servers
- Na-update ang Visual Curriculum Map upang tumpak na ipakita ang lahat ng mga paksa
- Pinahusay ang mga paglalarawan ng Advanced Topics upang saklawin ang lahat ng mga espesyal na lugar
- Na-update ang seksyon ng Case Studies upang ipakita ang mga aktwal na halimbawa
- Idinagdag ang komprehensibong changelog na ito

### Mga Kontribusyon ng Komunidad (06-CommunityContributions/)
- Idinagdag ang detalyadong impormasyon tungkol sa mga MCP server para sa pagbuo ng imahe
- Idinagdag ang komprehensibong seksyon sa paggamit ng Claude sa VSCode
- Idinagdag ang mga tagubilin sa pag-setup at paggamit ng Cline terminal client
- Na-update ang seksyon ng MCP client upang isama ang lahat ng mga popular na opsyon ng client
- Pinahusay ang mga halimbawa ng kontribusyon gamit ang mas tumpak na mga sample ng code

### Advanced Topics (05-AdvancedTopics/)
- Inayos ang lahat ng mga folder ng espesyal na paksa na may pare-parehong pagngalan
- Idinagdag ang mga materyales at halimbawa sa context engineering
- Idinagdag ang dokumentasyon ng integrasyon ng Foundry agent
- Pinahusay ang dokumentasyon ng integrasyon ng seguridad ng Entra ID

## Hunyo 11, 2025

### Paunang Paglikha
- Inilabas ang unang bersyon ng MCP for Beginners curriculum
- Nilikha ang pangunahing istruktura para sa lahat ng 10 pangunahing seksyon
- Ipinalaganap ang Visual Curriculum Map para sa navigasyon
- Idinagdag ang mga paunang sample na proyekto sa maraming programming language

### Pagsisimula (03-GettingStarted/)
- Nilikha ang mga unang halimbawa ng implementasyon ng server
- Idinagdag ang gabay sa pagbuo ng client
- Isinama ang mga tagubilin sa integrasyon ng LLM client
- Idinagdag ang dokumentasyon ng integrasyon sa VS Code
- Ipinalaganap ang mga halimbawa ng Server-Sent Events (SSE) server

### Core Concepts (01-CoreConcepts/)
- Idinagdag ang detalyadong paliwanag ng client-server architecture
- Nilikha ang dokumentasyon sa mga pangunahing bahagi ng protocol
- Naidokumento ang mga pattern ng messaging sa MCP

## Mayo 23, 2025

### Istruktura ng Repository
- Inisyalisa ang repository gamit ang pangunahing istruktura ng folder
- Nilikha ang mga README file para sa bawat pangunahing seksyon
- Naitatag ang imprastraktura para sa pagsasalin
- Idinagdag ang mga image asset at diagram

### Dokumentasyon
- Nilikha ang paunang README.md na may overview ng curriculum
- Idinagdag ang CODE_OF_CONDUCT.md at SECURITY.md
- Naitatag ang SUPPORT.md na may gabay para sa paghingi ng tulong
- Nilikha ang paunang istruktura ng study guide

## Abril 15, 2025

### Pagpaplano at Balangkas
- Paunang pagpaplano para sa MCP for Beginners curriculum
- Tinukoy ang mga layunin sa pagkatuto at target na madla
- Inilatag ang 10-seksyon na istruktura ng curriculum
- Bumuo ng konseptwal na balangkas para sa mga halimbawa at case study
- Nilikha ang paunang prototype na mga halimbawa para sa mga pangunahing konsepto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
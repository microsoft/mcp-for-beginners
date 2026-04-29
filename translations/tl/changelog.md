# Changelog: MCP para sa Curriculum ng mga Baguhan

Ang dokumentong ito ay nagsisilbing talaan ng lahat ng mahahalagang pagbabago na ginawa sa Model Context Protocol (MCP) para sa curriculum ng mga baguhan. Ang mga pagbabago ay naitala sa reverse chronological order (pinakabagong mga pagbabago muna).

## Abril 11, 2026

### Bagong Aralin, Pag-aayos ng Dokumentasyon, at Mga Update sa Dependency

#### Bagong Nilalaman ng Kurikulum na Idinagdag

**Module 05 - Mga Advanced na Paksa**
- **Aralin 5.17: Adversarial Multi-Agent Reasoning gamit ang MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Bagong komprehensibong gabay na sumasaklaw sa adversarial debate pattern para sa multi-agent systems
  - Mermaid architecture diagram: dalawang ahente → shared MCP server → debate transcript → hukom → hatol
  - Shared MCP tool server (`web_search` + `run_python`) na ipinatupad sa Python at TypeScript
  - Magkakasalungat na system prompts (FOR / AGAINST / Hukom) na may malinaw na mga kinakailangan sa paggamit ng tool
  - Debate orchestrator sa Python, TypeScript, at C# na namamahala sa mga rounds at pag-ruruta ng mga argumento
  - MCP `ClientSession` wiring para sa orchestrator sa mga totoong tawag sa tool
  - Talaan ng mga case use (pagtuklas ng hallucination, threat modeling, pagsusuri sa disenyo ng API, beripikasyon ng katotohanan, pagpili ng teknolohiya)
  - Mga konsiderasyon sa seguridad: sandboxed execution, pag-validate ng tawag sa tool, rate limiting, audit logging
  - Istrakturadong ehersisyo na may tatlong praktikal na senaryo (pagsusuri ng code, desisyon sa arkitektura, moderation ng nilalaman)

#### Pag-aayos ng Dokumentasyon

**Module 03 - Pagsisimula**
- **05-stdio-server/README.md**: Naayos ang hindi kumpletong halimbawa ng TypeScript stdio server — idinagdag ang nawawalang transport instantiation (`new StdioServerTransport()`) at `server.connect(transport)` call upang tumugma sa mga halimbawa ng Python at .NET sa parehong seksyon
- **14-sampling/README.md**: Naayos ang typo — itinama mula sa `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang entry 5.17 (Adversarial Multi-Agent Reasoning gamit ang MCP) sa talahanayan ng kurikulum na may direktang link sa bagong aralin

**05-AdvancedTopics/README.md**
- Idinagdag ang hanay ng Aralin 5.17 sa talahanayan ng mga aralin

**study_guide.md**
- Idinagdag ang paksa ng Adversarial Multi-Agent Reasoning sa mind-map at deskripsyon ng mga Advanced na Paksa

#### Pag-aayos ng Code at Seguridad

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Pag-aayos sa Seguridad — command injection**: Pinalitan ang `execSync` shell interpolation gamit ang `execFile` + `promisify` sa TypeScript na `run_python` tool, na nagtanggal ng vulnerabilidad sa command injection (ang code na kontrolado ng LLM ay ipinapasa bilang literal na argv element nang walang shell involvement)
- **MCP tool loop wiring**: In-update ang Python debate orchestrator upang gamitin ang `AsyncAnthropic` client (pinalitan ang blocking sync `Anthropic`), ipasa nang live ang `ClientSession` sa bawat turn ng ahente, kunin ang mga depinisyon ng tool gamit ang `session.list_tools()` sa bawat turn, at magpadala ng `tool_use` blocks gamit ang `session.call_tool()` sa loop hanggang sa maglabas ang modelo ng huling sagot sa teksto

#### Mga Update sa Dependency

- In-update ang `hono` sa bersyon 4.12.12 sa maraming packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- In-update ang `@hono/node-server` mula 1.19.11 hanggang 1.19.13 sa mga TypeScript packages
- In-update ang `cryptography` mula 46.0.5 hanggang 46.0.7 sa mga Python packages (10-StreamliningAIWorkflows labs 3 at 4)
- In-update ang `lodash` mula 4.17.23 hanggang 4.18.1 sa 10-StreamliningAIWorkflows inspector

#### Mga Pagsasalin

- Sinync ang mga pagsasalin para sa 48+ na mga wika gamit ang pinakabagong pagbabago sa source (i18n update)

---

## Pebrero 5, 2026

### Pangkalahatang Pag-validate ng Repository at Mga Pagpapabuti sa Navigation

#### Bagong Nilalaman ng Kurikulum na Idinagdag

**Module 03 - Pagsisimula**
- **12-mcp-hosts/README.md**: Bagong komprehensibong gabay para sa pag-setup ng MCP hosts
  - Mga halimbawa ng configuration para sa Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mga template ng JSON configuration para sa lahat ng pangunahing hosts
  - Talaan ng paghahambing ng mga uri ng transport (stdio, SSE/HTTP, WebSocket)
  - Mga tip sa pag-troubleshoot ng mga karaniwang isyu sa koneksyon
  - Mga pinakamahuhusay na kasanayan sa seguridad para sa configuration ng host

- **13-mcp-inspector/README.md**: Bagong gabay sa pag-debug para sa MCP Inspector
  - Mga paraan ng pag-install (npx, npm global, mula sa source)
  - Pagsasangkot sa mga server gamit ang stdio at HTTP/SSE
  - Mga workflow para sa testing tools, resources, at prompts
  - Integrasyon ng VS Code sa MCP Inspector
  - Mga common na isyu sa pag-debug na may mga solusyon

**Module 04 - Praktikal na Implementasyon**
- **pagination/README.md**: Bagong gabay sa implementasyon ng pagination
  - Mga pattern ng cursor-based pagination sa Python, TypeScript, Java
  - Pag-handle ng client-side pagination
  - Mga estratehiya sa disenyo ng cursor (opaque vs. structured)
  - Mga rekomendasyon para sa pag-optimize ng performance

**Module 05 - Mga Advanced na Paksa**
- **mcp-protocol-features/README.md**: Malalim na pagsisid sa mga bagong feature ng protocol
  - Implementasyon ng mga progress notifications
  - Mga pattern ng request cancellation
  - Mga resource templates na may mga URI pattern
  - Pamamahala sa lifecycle ng server
  - Kontrol sa antas ng logging
  - Mga pattern sa paghawak ng error gamit ang JSON-RPC codes

#### Pag-aayos ng Navigation (24+ na mga file na-update)

**Pangunahing Module READMEs**
 Ngayon ay may link sa parehong unang aralin AT susunod na module

**02-Security Sub-files**
- Lahat ng 5 kasamang dokumento sa seguridad ay may "What's Next" na navigation ngayon:

**09-CaseStudy Files**
- Lahat ng mga case study files ay may sunud-sunod na navigation ngayon:

**10-StreamliningAI Labs**
Idinagdag ang seksyon na What's Next sa Module 10 overview at Module 11

#### Mga Pag-aayos sa Code at Nilalaman

**SDK at Mga Update sa Dependency**
Naayos ang walang laman na openai version sa `^4.95.0`
In-update ang SDK mula `^1.8.0` hanggang `>=1.26.0`
In-update ang mcp version pins sa `>=1.26.0`

**Pag-aayos ng Code**
Naayos ang invalid na model `gpt-4o-mini` sa `gpt-4.1-mini`

**Pag-aayos ng Nilalaman**
Naayos ang sirang link `READMEmd` → `README.md`, naayos ang header ng kurikulum mula `Module 1-3` → `Module 0-3`, naayos ang case-sensitive na path
Tinanggal ang corrupt duplicate na Case Study 5 content

**Pagpapahusay sa Gabay para sa mga Baguhan**
Idinagdag ang wastong pambungad, mga layunin sa pagkatuto, at mga kinakailangang paunang kaalaman para sa mga baguhan

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang mga entry 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) sa talahanayan ng kurikulum

**Module READMEs**
Idinagdag ang mga aralin 12 at 13 sa listahan ng aralin
Idinagdag ang seksyon ng Practical Guides na may link para sa pagination
Idinagdag ang mga aralin 5.15 (Custom Transport) at 5.16 (Protocol Features)

**study_guide.md**
- Na-update ang mindmap na may lahat ng bagong paksa: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## Enero 28, 2026

### Pagsusuri sa Pagsunod sa MCP Specification 2025-11-25

#### Pagpapahusay sa Mga Pangunahing Konsepto (01-CoreConcepts/)
- **Bagong Client Primitive - Roots**: Idinagdag ang komprehensibong dokumentasyon sa Roots client primitive, na nagpapahintulot sa mga server na maunawaan ang mga hangganan ng filesystem at mga pahintulot sa pag-access
- **Annotasyon ng Mga Tool**: Idinagdag ang dokumentasyon sa tool behavioral annotations (`readOnlyHint`, `destructiveHint`) para sa mas mahusay na pagpapasya sa pagpapatupad ng tool
- **Pagtawag sa Tool sa Sampling**: In-update ang dokumentasyon ng Sampling upang isama ang `tools` at `toolChoice` na mga parameter para sa model-driven na pagtawag ng tool sa mga sampling request
- **URL Mode Elicitation**: Idinagdag ang dokumentasyon sa URL-based elicitation para sa mga panlabas na interaksyon ng server na sinimulan sa web
- **Mga Gawain (Eksperimental)**: Idinagdag ang bagong seksyon na nagdodokumento sa experimental Tasks na feature para sa matibay na execution wrappers at ipinagpalibang paghahanap ng resulta
- **Suporta sa Mga Icon**: Napansin na ang mga tool, resources, resource templates, at prompts ay maaari nang may kasamang mga icon bilang karagdagang metadata

#### Mga Update sa Dokumentasyon
- **README.md**: Idinagdag ang bersyon ng MCP Specification 2025-11-25 at paliwanag sa bersyon ayon sa petsa
- **study_guide.md**: In-update ang mapa ng kurikulum upang isama ang Tasks at Tool Annotations sa seksyon ng Core Concepts; in-update ang timestamp ng dokumento

#### Pagtiyak sa Pagsunod sa Specification
- **Bersyon ng Protocol**: Nakumpirma na lahat ng dokumentasyon ay tumutukoy sa kasalukuyang MCP Specification 2025-11-25
- **Pagkakahanay ng Arkitektura**: Nakumpirma ang katumpakan ng dokumentasyon para sa two-layer architecture (Data Layer + Transport Layer)
- **Dokumentasyon ng Primitives**: Napatunayan ang mga server primitives (Resources, Prompts, Tools) at client primitives (Sampling, Elicitation, Logging, Roots)
- **Mga Mekanismo ng Transport**: Nakumpirma ang katumpakan ng dokumentasyon para sa STDIO at Streamable HTTP transport
- **Mga Patnubay sa Seguridad**: Nakumpirma ang pagkakaayon sa kasalukuyang dokumentadong MCP Security Best Practices

#### Mga Pangunahing Feature ng MCP 2025-11-25 na Naidokumento
- **OpenID Connect Discovery**: Pagdiskubre ng auth server sa pamamagitan ng OIDC
- **OAuth Client ID Metadata Documents**: Inirekumendang mekanismo ng pagrerehistro ng client
- **JSON Schema 2020-12**: Default na dialect para sa MCP schema definitions
- **SDK Tiering System**: Pormal na mga kinakailangan para sa pagsuporta at maintenance ng mga feature ng SDK
- **Estruktura ng Pamamahala**: Pormal na Working Groups at Interest Groups sa pamamahala ng MCP

### Malawakang Pag-update sa Dokumentasyon ng Seguridad (02-Security/)

#### Integrasyon ng MCP Security Summit Workshop (Sherpa)
- **Bagong Hands-On Training Resource**: Idinagdag ang komprehensibong integrasyon sa [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) sa lahat ng dokumentasyon sa seguridad
- **Saklaw ng Ruta ng Ekspedisyon**: Na-dokumento ang buong progreso mula Base Camp hanggang Summit
- **Pagkakahanay sa OWASP**: Lahat ng patnubay sa seguridad ay ngayon naka-map sa OWASP MCP Azure Security Guide risks

#### Integrasyon ng OWASP MCP Top 10
- **Bagong Seksyon**: Idinagdag ang talahanayan ng OWASP MCP Top 10 Security Risks na may mga mitigasyon ng Azure sa pangunahing Security README
- **Dokumentasyon Batay sa Risk**: In-update ang mcp-security-controls-2025.md na may mga reference sa OWASP MCP risk para sa bawat security domain
- **Reference Architecture**: Nag-link sa OWASP MCP Azure Security Guide reference architecture at mga pattern ng implementasyon

#### Mga Na-update na Security Files
- **README.md**: Idinagdag ang Sherpa Workshop overview, talaan ng ruta ng ekspedisyon, buod ng OWASP MCP Top 10 risk, at seksyon ng hands-on training
- **mcp-security-controls-2025.md**: In-update ang header hanggang Pebrero 2026, idinagdag ang mga OWASP risk references (MCP01-MCP08), inayos ang inconsistency sa bersyon ng spec
- **mcp-security-best-practices-2025.md**: Idinagdag ang mga Sherpa at OWASP resources section, in-update ang timestamp
- **mcp-best-practices.md**: Idinagdag ang hands-on training section na may Sherpa at OWASP links
- **azure-content-safety-implementation.md**: Idinagdag ang OWASP MCP06 reference, Sherpa Camp 3 alignment, at karagdagang resources na seksyon

#### Mga Bagong Resource Link na Idinagdag
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Mga indibidwal na pahina ng OWASP MCP risk (MCP01-MCP10)

### Pangkalahatang Pagkakahanay ng MCP Specification 2025-11-25 sa Kurikulum

#### Module 03 - Pagsisimula
- **Dokumentasyon ng SDK**: Idinagdag ang Go SDK sa opisyal na listahan ng SDK; in-update lahat ng reference sa SDK upang tumugma sa MCP Specification 2025-11-25
- **Paglilinaw sa Transport**: In-update ang mga paglalarawan ng STDIO at HTTP Streaming transport na may malinaw na referensya sa spec

#### Module 04 - Praktikal na Implementasyon
- **Mga Update ng SDK**: Idinagdag ang Go SDK; in-update ang listahan ng SDK na may referensya sa bersyon ng spec
- **Spec ng Awtorisasyon**: In-update ang link ng MCP Authorization specification sa kasalukuyang bersyon 2025-11-25

#### Module 05 - Mga Advanced na Paksa
- **Mga Bagong Feature**: Idinagdag ang tala tungkol sa mga bagong feature ng MCP Specification 2025-11-25 (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Mga Resource sa Seguridad**: Idinagdag ang OWASP MCP Top 10 at Sherpa workshop links sa karagdagang mga sanggunian

#### Module 06 - Mga Ambag ng Komunidad
- **Listahan ng SDK**: Idinagdag ang Swift at Rust SDKs; in-update ang link ng spec sa 2025-11-25
- **Referensya ng Spec**: In-update ang MCP Specification link sa direktang URL ng spec

#### Module 07 - Mga Aralin mula sa Maagang Paggamit
- **Mga Update sa Resource**: Idinagdag ang MCP Specification 2025-11-25 link at OWASP MCP Top 10 sa karagdagang mga sanggunian

#### Module 08 - Mga Pinakamahusay na Kasanayan
- **Bersyon ng Spec**: In-update ang MCP Specification reference sa 2025-11-25
- **Mga Resource sa Seguridad**: Idinagdag ang OWASP MCP Top 10 at Sherpa workshop sa karagdagang mga sanggunian

#### Module 10 - Pag-streamline ng AI Workflows
- **Update sa Badge**: Binago ang MCP version badge mula sa bersyon ng SDK (1.9.3) patungo sa bersyon ng specification (2025-11-25)
- **Mga Link ng Resource**: In-update ang MCP Specification link; idinagdag ang OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Referensya ng Spec**: In-update ang MCP Specification link sa bersyon 2025-11-25
- **Mga Resource sa Seguridad**: Idinagdag ang OWASP MCP Top 10 sa opisyal na mga sanggunian

## Disyembre 18, 2025
### Update sa Dokumentasyon ng Seguridad - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Update ng Bersyon ng Specification
- **Update sa Bersyon ng Protokol**: In-update para tumukoy sa pinakabagong MCP Specification 2025-11-25 (inilabas noong Nobyembre 25, 2025)
  - In-update lahat ng reperensya ng bersyon ng specification mula 2025-06-18 hanggang 2025-11-25
  - In-update ang mga petsa sa dokumento mula Agosto 18, 2025 hanggang Disyembre 18, 2025
  - Kinikilalang lahat ng URL ng specification ay nakaturo sa kasalukuyang dokumentasyon
- **Pag-validate ng Nilalaman**: Komprehensibong pag-validate ng mga pinakamahusay na kasanayan sa seguridad laban sa pinakabagong standards
  - **Microsoft Security Solutions**: Kinikilalang kasalukuyang terminolohiya at mga link para sa Prompt Shields (na dating "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, at Azure Key Vault
  - **OAuth 2.1 Security**: Nakumpirma ang pagsunod sa pinakahuling pinakamahusay na kasanayan sa seguridad ng OAuth
  - **OWASP Standards**: Kinumpirma na ang mga reperensya sa OWASP Top 10 para sa LLMs ay nananatiling bago
  - **Azure Services**: Kinikilalang lahat ng link sa dokumentasyon ng Microsoft Azure at mga pinakamahusay na kasanayan
- **Pagsunod sa Standards**: Lahat ng sangguniang security standards ay napatunayang kasalukuyan
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Pinakamahusay na Kasanayan sa Seguridad ng OAuth 2.1
  - Mga balangkas sa seguridad at pagsunod sa Azure
- **Mga Resources sa Implementasyon**: Nakumpirma ang lahat ng mga link sa gabay sa implementasyon at mga resources
  - Mga pattern ng pagpapatunay sa Azure API Management
  - Mga gabay sa integrasyon ng Microsoft Entra ID
  - Pamamahala ng mga lihim sa Azure Key Vault
  - DevSecOps pipeline at mga solusyong pang-monitor

### Pagsiguro ng Kalidad ng Dokumentasyon
- **Pagsunod sa Specification**: Tiniyak na lahat ng kinakailangang MCP security requirements (MUST/MUST NOT) ay naka-align sa pinakabago ng specification
- **Pagkakaroon ng Sariwang Resources**: Nakumpirma lahat ng panlabas na link sa dokumentasyong Microsoft, security standards, at mga gabay sa implementasyon
- **Saklaw ng Pinakamahusay na Kasanayan**: Nakumpirma ang komprehensibong saklaw ng pagpapatunay, awtorisasyon, mga AI-specific na banta, seguridad sa supply chain, at mga pattern ng enterprise

## Oktubre 6, 2025

### Paglawak ng Seksyon ng Simula – Advanced na Paggamit ng Server at Simpleng Pagpapatunay

#### Advanced na Paggamit ng Server (03-GettingStarted/10-advanced)
- **Bagong Kabanata**: Inilunsad ang komprehensibong gabay sa advanced na paggamit ng MCP server, na sumasaklaw sa regular at low-level na mga arkitektura ng server.
  - **Regular vs. Low-Level na Server**: Detalyadong paghahambing at mga halimbawa ng kodigo sa Python at TypeScript para sa parehong pamamaraan.
  - **Disenyong Nakabatay sa Handler**: Paliwanag sa handler-based na pamamahala ng tool/resource/prompt para sa scalable at flexible na implementasyon ng server.
  - **Mga Praktikal na Pattern**: Mga sitwasyong totoong buhay kung saan kapaki-pakinabang ang mga low-level server pattern para sa mga advanced na tampok at arkitektura.

#### Simpleng Pagpapatunay (03-GettingStarted/11-simple-auth)
- **Bagong Kabanata**: Hakbang-hakbang na gabay sa pagpapatupad ng simpleng pagpapatunay sa mga MCP server.
  - **Konsepto ng Auth**: Malinaw na paliwanag ng pagpapatunay laban sa awtorisasyon, at pamamahala ng kredensyal.
  - **Pangunahing Implementasyon ng Auth**: Middleware-based na authentication pattern sa Python (Starlette) at TypeScript (Express), kasama ang mga halimbawa ng kodigo.
  - **Pag-usbong sa Advanced na Seguridad**: Gabay sa pagsisimula sa simpleng auth at pag-angat sa OAuth 2.1 at RBAC, may kasamang sanggunian sa mga advanced na security module.

Ang mga dagdag na ito ay nagbibigay ng praktikal na patnubay para sa pagbuo ng mas matatag, ligtas, at flexible na mga implementasyon ng MCP server, na nag-uugnay sa mga pundamental na konsepto sa mga advanced na pattern sa produksyon.

## Setyembre 29, 2025

### MCP Server Database Integration Labs - Komprehensibong Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - Bagong Kumpletong Kurikulum sa Database Integration
- **Kumpletong 13-Lab Learning Path**: Idinagdag ang komprehensibong hands-on na kurikulum para sa pagbuo ng production-ready MCP servers na may PostgreSQL database integration
  - **Implementasyon sa Totoong Mundo**: Use case ng Zava Retail analytics na nagpapakita ng mga pattern ng enterprise-grade
  - **Istraktura ng Pagkatuto**:
    - **Labs 00-03: Mga Pundasyon** - Panimula, Core Architecture, Seguridad at Multi-Tenancy, Pagsasaayos ng Kapaligiran
    - **Labs 04-06: Pagbuo ng MCP Server** - Disenyo at Schema ng Database, Implementasyon ng MCP Server, Pagbuo ng Tool
    - **Labs 07-09: Mga Advanced na Tampok** - Semantic Search Integration, Pagsubok at Debugging, VS Code Integration
    - **Labs 10-12: Produksyon at Pinakamahusay na Kasanayan** - Mga Diskarte sa Deployment, Monitoring & Observability, Pinakamahusay na Kasanayan at Optimization
  - **Mga Teknolohiyang Pang-Enterprise**: FastMCP framework, PostgreSQL kasama ng pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Mga Advanced na Tampok**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time na pagmamanman

#### Standardisasyon ng Terminolohiya - Pagbabago mula sa Module tungo sa Lab
- **Komprehensibong Update ng Dokumentasyon**: Sistematikong in-update ang lahat ng README files sa 11-MCPServerHandsOnLabs upang gamitin ang terminong "Lab" sa halip na "Module"
  - **Mga Header ng Seksyon**: In-update ang "What This Module Covers" sa "What This Lab Covers" sa lahat ng 13 lab
  - **Paglalarawan ng Nilalaman**: Pinalitan ang "This module provides..." ng "This lab provides..." sa buong dokumentasyon
  - **Mga Layunin sa Pagkatuto**: In-update ang "By the end of this module..." sa "By the end of this lab..."
  - **Mga Link sa Navigasyon**: Pinalitan ang lahat ng "Module XX:" na reperensya sa "Lab XX:" sa mga cross-reference at navigasyon
  - **Pagsubaybay sa Pagtatapos**: In-update ang "After completing this module..." sa "After completing this lab..."
  - **Napanatiling Teknikal na Reperensya**: Pinanatili ang mga reperensyang Python module sa mga configuration files (hal. `"module": "mcp_server.main"`)

#### Pagpapahusay ng Study Guide (study_guide.md)
- **Visual Curriculum Map**: Idinagdag ang bagong seksyon na "11. Database Integration Labs" na may komprehensibong paglalantad ng istruktura ng lab
- **Istraktura ng Repository**: In-update mula sa sampu tungo sa labing-isang pangunahing mga seksyon na may detalyadong paglalarawan ng 11-MCPServerHandsOnLabs
- **Patnubay sa Learning Path**: Pinahusay na mga tagubilin sa navigasyon upang saklawin ang mga seksyon 00-11
- **Saklaw ng Teknolohiya**: Idinagdag ang FastMCP, PostgreSQL, detalye ng integrasyon ng Azure services
- **Mga Resulta sa Pagkatuto**: Binigyang-diin ang pag-develop ng production-ready server, pattern sa integrasyon ng database, at seguridad ng enterprise

#### Pagpapahusay ng Istruktura ng Pangunahing README
- **Terminolohiyang Nakabatay sa Lab**: In-update ang pangunahing README.md sa 11-MCPServerHandsOnLabs upang gamitin nang tuloy-tuloy ang istruktura ng "Lab"
- **Organisasyon ng Learning Path**: Malinaw na pag-usad mula sa pundasyong mga konsepto hanggang sa advanced na implementasyon at deployment sa produksyon
- **Pokus sa Totoong Mundo**: Bigyang-diin ang praktikal, hands-on na pagkatuto gamit ang mga enterprise-grade pattern at teknolohiya

### Pagpapabuti ng Kalidad at Konsistensi ng Dokumentasyon
- **Pagtutok sa Hands-On Learning**: Pinalakas ang praktikal na, lab-based na lapit sa buong dokumentasyon
- **Pokus sa Enterprise Patterns**: Binibigyang-diin ang production-ready na mga implementasyon at mga konsiderasyon sa seguridad ng enterprise
- **Integrasyon ng Teknolohiya**: Komprehensibong saklaw ng modernong Azure services at AI integration patterns
- **Pag-usad sa Pagkatuto**: Malinaw, istraktured na landas mula sa mga pangunahing konsepto hanggang sa deployment sa produksyon

## Setyembre 26, 2025

### Pagpapahusay ng Mga Case Study - Integrasyon ng GitHub MCP Registry

#### Mga Case Study (09-CaseStudy/) - Pokus sa Pag-unlad ng Ecosystem
- **README.md**: Malaking pagpapalawak na may komprehensibong GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: Bagong komprehensibong case study na sinusuri ang paglulunsad ng GitHub MCP Registry noong Setyembre 2025
    - **Pagsusuri sa Problema**: Detalyadong pagsusuri ng mga fragmented na MCP server discovery at mga hamon sa deployment
    - **Arkitektura ng Solusyon**: Sentralisadong registry approach ng GitHub na may one-click VS Code installation
    - **Epekto sa Negosyo**: Nasusukat na pagbuti sa onboarding ng developer at produktibidad
    - **Pangunahing Halaga**: Pokus sa modular agent deployment at interoperability ng mga cross-tool
    - **Pag-unlad ng Ecosystem**: Posisyon bilang pundasyong platform para sa agentic integration
  - **Pinahusay na Istruktura ng Case Study**: In-update ang lahat ng pitong case studies na may pare-parehong pormat at komprehensibong paglalarawan
    - Azure AI Travel Agents: Pokus sa multi-agent orchestration
    - Azure DevOps Integration: Pokus sa awtomasyon ng workflow
    - Real-Time Documentation Retrieval: Implementasyon ng Python console client
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code at GitHub Copilot integration
    - Azure API Management: Mga pattern ng enterprise API integration
    - GitHub MCP Registry: Pag-unlad ng ecosystem at community platform
  - **Komprehensibong Konklusyon**: Muling isinulat na seksyon ng konklusyon na binibigyang-diin ang pitong case studies na sumasaklaw sa maraming dimensyon ng MCP implementasyon
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Pag-unlad ng Ecosystem, Kategorya ng Mga Aplikasyong Edukasyonal
    - Pinahusay na mga pananaw sa mga architectural pattern, mga estratehiya sa implementasyon, at pinakamahusay na kasanayan
    - Pagbibigay-diin sa MCP bilang mature at production-ready na protocol

#### Mga Update sa Study Guide (study_guide.md)
- **Visual Curriculum Map**: In-update ang mindmap upang isama ang GitHub MCP Registry sa seksyon ng Mga Case Study
- **Paglalarawan ng Mga Case Study**: Pinahusay mula sa mga generic na paglalarawan tungo sa detalyadong breakdown ng pitong komprehensibong case study
- **Istruktura ng Repository**: In-update ang seksyon 10 upang ipakita ang komprehensibong coverage ng case study na may tiyak na detalye sa implementasyon
- **Integrasyon ng Changelog**: Idinagdag ang entry noong Setyembre 26, 2025 na dokumentado ang pagdaragdag ng GitHub MCP Registry at mga pagpapahusay ng case study
- **Mga Update sa Petsa**: In-update ang footer timestamp upang ipakita ang pinakabagong rebisyon (Setyembre 26, 2025)

### Pagpapabuti ng Kalidad ng Dokumentasyon
- **Pagpapahusay ng Konsistensi**: Standardisadong pormat at istruktura ng case study sa lahat ng pitong halimbawa
- **Komprehensibong Saklaw**: Ang mga case study ay sumasaklaw na sa enterprise, produktibidad ng developer, at pag-unlad ng ecosystem na mga scenario
- **Strategic na Posisyon**: Pinalakas na pokus sa MCP bilang pundasyong platform para sa deployment ng mga agentic system
- **Integrasyon ng Resources**: Updated ang dagdag na mga resources upang isama ang link sa GitHub MCP Registry

## Setyembre 15, 2025

### Paglawak ng Mga Advanced na Paksa - Custom Transports at Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Bagong Gabay sa Advanced na Implementasyon
- **README.md**: Kumpletong gabay sa implementasyon para sa mga custom MCP transport mechanism
  - **Azure Event Grid Transport**: Komprehensibong serverless event-driven transport implementation
    - Mga halimbawa sa C#, TypeScript, at Python na may Azure Functions integration
    - Mga arkitektura na event-driven para sa scalable MCP solutions
    - Mga webhook receiver at push-based message handling
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation
    - Real-time streaming na kapasidad para sa low-latency na mga senaryo
    - Mga estratehiya sa partitioning at checkpoint management
    - Mga batch ng mensahe at pag-optimize ng performance
  - **Enterprise Integration Patterns**: Mga production-ready na halimbawa ng arkitektura
    - Distributed MCP processing sa maraming Azure Functions
    - Hybrid transport architectures na pinagsasama ang iba't ibang transport types
    - Mga estratehiya sa durability, reliability, at error handling ng mensahe
  - **Seguridad at Monitoring**: Integrasyon ng Azure Key Vault at mga pattern ng observability
    - Managed identity authentication at pinakamababang pribilehiyong access
    - Application Insights telemetry at performance monitoring
    - Circuit breakers at mga pattern ng fault tolerance
  - **Mga Framework sa Pagsusuri**: Komprehensibong mga estratehiya sa pagsusuri para sa custom transports
    - Unit testing gamit ang test doubles at mocking frameworks
    - Integration testing gamit ang Azure Test Containers
    - Mga konsiderasyon sa performance at load testing

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Lumalabas na Disiplina sa AI
- **README.md**: Komprehensibong pagtalakay sa context engineering bilang bagong lumilitaw na larangan
  - **Pangunahing Prinsipyo**: Kumpletong pagbabahagi ng konteksto, kamalayan sa paggawa ng desisyon, at pamamahala ng context window
  - **Pagsunod sa MCP Protocol**: Paano tinutugunan ng disenyo ng MCP ang mga hamon ng context engineering
    - Mga limitasyon sa context window at progresibong loading strategies
    - Pagtukoy sa kaugnayan at dynamic na retrieval ng konteksto
    - Multi-modal na paghawak ng konteksto at mga konsiderasyon sa seguridad
  - **Mga Paraan ng Implementasyon**: Single-threaded kumpara sa multi-agent na arkitektura
    - Teknik sa pag-chunk at pagtatakda ng prayoridad ng konteksto
    - Progresibong pag-load at compression strategies ng konteksto
    - Layered context approaches at pag-optimize ng retrieval
  - **Measurement Framework**: Mga bagong sukatan para sa ebalwasyon ng bisa ng konteksto
    - Input efficiency, performance, kalidad, at mga konsiderasyon sa karanasan ng gumagamit
    - Mga eksperimento sa pag-optimize ng konteksto
    - Pagsusuri ng pagkabigo at mga metodolohiya para sa pagpapabuti

#### Update sa Navigasyon ng Kurikulum (README.md)
- **Pinahusay na Istruktura ng Module**: In-update ang talahanayan ng kurikulum upang isama ang mga bagong advanced topics
  - Idinagdag ang Context Engineering (5.14) at Custom Transport (5.15)
  - Pare-parehong pormat at mga link sa navigasyon sa lahat ng module
  - In-update ang mga paglalarawan upang ipakita ang kasalukuyang saklaw ng nilalaman

### Pagpapahusay sa Istruktura ng Direktoryo
- **Standardisasyon ng Pangalan**: Pinalitan ang "mcp transport" sa "mcp-transport" para sa pagkakapareho ng ibang folder ng advanced na paksa
- **Organisasyon ng Nilalaman**: Lahat ng 05-AdvancedTopics folder ay sumusunod na sa pare-parehong pattern ng pangalan (mcp-[topic])

### Pagpapaayos ng Kalidad ng Dokumentasyon
- **Pagsunod sa MCP Specification**: Lahat ng bagong nilalaman ay tumutukoy sa kasalukuyang MCP Specification 2025-06-18
- **Halimbawa sa Maramihang Wika**: Komprehensibong mga halimbawa ng kodigo sa C#, TypeScript, at Python
- **Pokus sa Enterprise**: Mga pattern na handa na sa produksyon at integrasyon ng Azure cloud sa buong dokumentasyon
- **Visual na Dokumentasyon**: Mermaid diagrams para sa arkitektura at pag-visualize ng daloy

## Agosto 18, 2025

### Komprehensibong Update ng Dokumentasyon - Mga Pamantayan ng MCP 2025-06-18

#### MCP Security Best Practices (02-Security/) - Kumpletong Modernisasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Ganap na muling pagsulat na naka-align sa MCP Specification 2025-06-18
  - **Mandatory Requirements**: Idinagdag ang tahasang MUST/MUST NOT na mga kinakailangan mula sa opisyal na espesipikasyon na may malinaw na visual na mga indikasyon
  - **12 Core Security Practices**: Naayos muli mula sa 15-item na listahan patungo sa komprehensibong mga domain ng seguridad
    - Token Security & Authentication na may integrasyon ng external na tagapagbigay ng pagkakakilanlan
    - Session Management & Transport Security na may mga kinakailangan sa kriptograpiya
    - AI-Specific Threat Protection na may integrasyon ng Microsoft Prompt Shields
    - Access Control & Permissions na may prinsipyo ng least privilege
    - Content Safety & Monitoring na may integrasyon ng Azure Content Safety
    - Supply Chain Security na may komprehensibong pagpapatunay ng mga bahagi
    - OAuth Security & Confused Deputy Prevention na may implementasyon ng PKCE
    - Incident Response & Recovery na may mga automated na kakayahan
    - Compliance & Governance na may pagsunod sa mga regulasyon
    - Advanced Security Controls na may zero trust na arkitektura
    - Microsoft Security Ecosystem Integration na may komprehensibong mga solusyon
    - Continuous Security Evolution na may mga adaptive na kasanayan
  - **Microsoft Security Solutions**: Pinahusay na gabay sa integrasyon para sa Prompt Shields, Azure Content Safety, Entra ID, at GitHub Advanced Security
  - **Implementation Resources**: Naikategorya ang komprehensibong mga link sa mga sanggunian ayon sa Opisyal na Dokumentasyon ng MCP, Microsoft Security Solutions, Mga Pamantayan sa Seguridad, at Mga Gabay sa Pagpapatupad

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Ganap na pagbabago gamit ang enterprise-grade na security framework
  - **9 Comprehensive Security Domains**: Pinalawak mula sa mga pangunahing kontrol patungo sa detalyadong enterprise framework
    - Advanced Authentication & Authorization na may integrasyon ng Microsoft Entra ID
    - Token Security & Anti-Passthrough Controls na may komprehensibong pagpapatunay
    - Session Security Controls na may pag-iwas sa hijacking
    - AI-Specific Security Controls na may pag-iwas sa prompt injection at tool poisoning
    - Confused Deputy Attack Prevention na may OAuth proxy security
    - Tool Execution Security na may sandboxing at isolation
    - Supply Chain Security Controls na may dependency verification
    - Monitoring & Detection Controls na may SIEM integration
    - Incident Response & Recovery na may mga automated na kakayahan
  - **Implementation Examples**: Idinagdag ang detalyadong mga YAML configuration blocks at mga halimbawa ng code
  - **Microsoft Solutions Integration**: Komprehensibong saklaw ng Azure security services, GitHub Advanced Security, at enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Ganap na muling pagsulat para sa enterprise security implementation
  - **Current Specification Alignment**: Na-update ayon sa MCP Specification 2025-06-18 na may mandatory security requirements
  - **Enhanced Authentication**: Integrasyon ng Microsoft Entra ID na may komprehensibong mga halimbawa gamit ang .NET at Java Spring Security
  - **AI Security Integration**: Implementasyon ng Microsoft Prompt Shields at Azure Content Safety na may detalyadong mga halimbawa sa Python
  - **Advanced Threat Mitigation**: Komprehensibong mga halimbawa ng implementasyon para sa
    - Confused Deputy Attack Prevention na may PKCE at pagsuri ng user consent
    - Token Passthrough Prevention na may audience validation at secure token management
    - Session Hijacking Prevention na may cryptographic binding at behavioral analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, at supply chain security
  - **Implementation Checklist**: Malinaw na paghihiwalay ng mandatory kumpara sa recommended security controls na may mga benepisyo ng Microsoft security ecosystem

### Dokumentasyon Kalidad at Pag-align sa Mga Pamantayan
- **Specification References**: Na-update lahat ng mga sanggunian sa kasalukuyang MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Pinahusay ang gabay sa integrasyon sa buong dokumentasyong pangseguridad
- **Praktikal na Pagpapatupad**: Idinagdag ang detalyadong mga halimbawa ng code gamit ang .NET, Java, at Python na may mga pattern sa enterprise
- **Organisasyon ng Resources**: Komprehensibong pagkategorya ng opisyal na dokumentasyon, mga pamantayan sa seguridad, at mga gabay sa pagpapatupad
- **Visual Indicators**: Malinaw na pagmamarka ng mandatory requirements laban sa recommended practices


#### Core Concepts (01-CoreConcepts/) - Ganap na Modernisasyon
- **Protocol Version Update**: Na-update upang tumukoy sa kasalukuyang MCP Specification 2025-06-18 gamit ang petsa-based na versioning (YYYY-MM-DD format)
- **Architecture Refinement**: Pinahusay na mga paglalarawan ng Hosts, Clients, at Servers upang ipakita ang kasalukuyang MCP architecture patterns
  - Ang mga Hosts ay malinaw nang tinukoy bilang mga AI application na nagko-coordinate ng maraming MCP client connections
  - Ang Clients ay inilalarawan bilang mga protocol connectors na nagpapanatili ng one-to-one na relasyon sa server
  - Ang Servers ay pinahusay na may lokal at remote deployment scenarios
- **Primitive Restructuring**: Ganap na pagbabago ng mga server at client primitives
  - Server Primitives: Mga Resources (pinagmumulan ng data), Prompts (mga template), Tools (gumaganang mga function) na may detalyadong paliwanag at mga halimbawa
  - Client Primitives: Sampling (LLM completions), Elicitation (input mula sa user), Logging (debugging/monitoring)
  - Na-update gamit ang kasalukuyang discovery (`*/list`), retrieval (`*/get`), at execution (`*/call`) na mga method pattern
- **Protocol Architecture**: Ipinakilala ang dalawang-layer na architectural model
  - Data Layer: JSON-RPC 2.0 na pundasyon na may lifecycle management at mga primitives
  - Transport Layer: STDIO (lokal) at Streamable HTTP na may SSE (remote) na mga mekanismo ng transportasyon
- **Security Framework**: Komprehensibong mga prinsipyo ng seguridad kabilang ang tahasang user consent, proteksyon sa privacy ng data, kaligtasan sa tool execution, at security sa transport layer
- **Communication Patterns**: Na-update ang mga protocol messages upang ipakita ang initialization, discovery, execution, at notification flows
- **Code Examples**: Na-refresh ang mga multi-language na halimbawa (.NET, Java, Python, JavaScript) upang ipakita ang kasalukuyang MCP SDK patterns

#### Security (02-Security/) - Komprehensibong Pagbabago sa Seguridad  
- **Standards Alignment**: Kumpletong pagsunod sa MCP Specification 2025-06-18 na mga kinakailangan sa seguridad
- **Authentication Evolution**: Dinokumento ang ebolusyon mula sa custom OAuth servers patungo sa external identity provider delegation (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Pinahusay ang saklaw ng mga modernong AI attack vectors
  - Detalyadong mga senaryo ng prompt injection attack na may mga totoong halimbawa
  - Mga mekanismo ng tool poisoning at mga pattern ng "rug pull" attack
  - Context window poisoning at model confusion attacks
- **Microsoft AI Security Solutions**: Komprehensibong saklaw ng Microsoft security ecosystem
  - AI Prompt Shields na may advanced detection, spotlighting, at delimiter techniques
  - Mga pattern ng integrasyon ng Azure Content Safety
  - GitHub Advanced Security para sa proteksyon ng supply chain
- **Advanced Threat Mitigation**: Detalyadong mga kontrol sa seguridad para sa
  - Session hijacking na may mga MCP-specific na senaryo at mga kinakailangan sa cryptographic session ID
  - Mga problema ng confused deputy sa mga MCP proxy scenario na may tahasang mga kinakailangan sa consent
  - Token passthrough vulnerabilities na may mandatory validation controls
- **Supply Chain Security**: Pinalawak na saklaw ng AI supply chain kasama ang foundation models, embeddings services, context providers, at third-party APIs
- **Foundation Security**: Pinahusay na integrasyon sa mga pattern ng enterprise security kabilang ang zero trust architecture at Microsoft security ecosystem
- **Resource Organization**: Inakategorya ang komprehensibong mga link sa mga resources ayon sa uri (Opisyal na Docs, Mga Pamantayan, Pananaliksik, Microsoft Solutions, Mga Gabay sa Pagpapatupad)

### Pagpapabuti sa Kalidad ng Dokumentasyon
- **Structured Learning Objectives**: Pinahusay na mga layunin sa pagkatuto na may spesipiko at actionable na mga resulta 
- **Cross-References**: Idinagdag ang mga link sa pagitan ng magkaugnay na mga paksa sa seguridad at core concepts
- **Current Information**: Na-update ang lahat ng petsa at mga sanggunian sa espesipikasyon upang tumugma sa kasalukuyang mga pamantayan
- **Implementation Guidance**: Nagdagdag ng spesipiko at actionable na mga gabay sa pagpapatupad sa buong mga seksyon

## Hulyo 16, 2025

### README at Mga Pagpapabuti sa Navigation
- Ganap na niredisenyo ang curriculum navigation sa README.md
- Pinalitan ang mga `<details>` tags ng mas accessible na table-based na format
- Nilikha ang alternatibong mga layout na opsyon sa bagong folder na "alternative_layouts"
- Idinagdag ang mga halimbawa ng card-based, tabbed-style, at accordion-style na navigation
- Na-update ang seksyon ng istruktura ng repositoryo upang isama ang lahat ng pinakabagong mga file
- Pinahusay ang seksyong "How to Use This Curriculum" na may malinaw na mga rekomendasyon
- Na-update ang mga MCP specification links upang tumuro sa tamang mga URL
- Idinagdag ang seksyong Context Engineering (5.14) sa istruktura ng kurikulum

### Mga Pag-update sa Study Guide
- Ganap na nirebisa ang study guide upang tumugma sa kasalukuyang istruktura ng repositoryo
- Idinagdag ang mga bagong seksyon para sa MCP Clients at Tools, at Mga Popular na MCP Servers
- Na-update ang Visual Curriculum Map upang tumpak na ipakita lahat ng paksa
- Pinahusay ang mga paglalarawan ng Advanced Topics upang masakop lahat ng espesyal na larangan
- Na-update ang seksyon ng Case Studies upang ipakita ang mga aktwal na halimbawa
- Idinagdag ang komprehensibong changelog na ito

### Mga Ambag ng Komunidad (06-CommunityContributions/)
- Idinagdag ang detalyadong impormasyon tungkol sa mga MCP server para sa image generation
- Idinagdag ang komprehensibong seksyon sa paggamit ng Claude sa VSCode
- Idinagdag ang setup at mga tagubilin sa paggamit ng Cline terminal client
- Na-update ang MCP client na seksyon upang isama ang lahat ng popular na client options
- Pinahusay ang mga halimbawa ng kontribusyon gamit ang mas tumpak na mga sample ng code

### Advanced Topics (05-AdvancedTopics/)
- Inorganisa ang lahat ng mga espesyal na folder ng paksa na may magkakatugmang mga pangalan
- Idinagdag ang mga materyales at mga halimbawa sa context engineering
- Idinagdag ang dokumentasyon ng integrasyon ng Foundry agent
- Pinahusay ang dokumentasyon ng seguridad ng integrasyon ng Entra ID

## Hunyo 11, 2025

### Unang Paglikha
- Inilabas ang unang bersyon ng MCP for Beginners curriculum
- Nilikha ang pangunahing istruktura para sa lahat ng 10 pangunahing seksyon
- Ipinaunlad ang Visual Curriculum Map para sa navigation
- Idinagdag ang mga unang sample projects sa iba't ibang programming languages

### Pagsisimula (03-GettingStarted/)
- Nilikha ang unang mga halimbawa ng implementasyon ng server
- Idinagdag ang gabay sa pagbuo ng client
- Isinama ang mga tagubilin sa integrasyon ng LLM client
- Idinagdag ang dokumentasyon nila sa VS Code integration
- Ipinaunlad ang mga halimbawa ng server gamit ang Server-Sent Events (SSE)

### Core Concepts (01-CoreConcepts/)
- Idinagdag ang detalyadong paliwanag ng client-server architecture
- Nilikha ang dokumentasyon sa mga pangunahing bahagi ng protocol
- Dinokumento ang mga messaging patterns sa MCP

## Mayo 23, 2025

### Istruktura ng Repositoryo
- Inilunsad ang repositoryo gamit ang pangunahing istruktura ng folder
- Nilikha ang mga README files para sa bawat pangunahing seksyon
- Naitatag ang imprastraktura para sa pagsasalin
- Idinagdag ang mga image assets at mga diagram

### Dokumentasyon
- Nilikha ang paunang README.md na may overview ng kurikulum
- Idinagdag ang CODE_OF_CONDUCT.md at SECURITY.md
- Naitatag ang SUPPORT.md na may mga gabay para sa paghingi ng tulong
- Nilikha ang paunang istruktura ng study guide

## Abril 15, 2025

### Pagpaplano at Balangkas
- Unang pagpaplano para sa MCP for Beginners curriculum
- Tinukoy ang mga layunin sa pagkatuto at target na audience
- Inilatag ang 10-seksiyon na istruktura ng kurikulum
- Ipinaunlad ang conceptual framework para sa mga halimbawa at case studies
- Nilikha ang unang mga prototype na halimbawa para sa mga pangunahing konsepto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang automated na pagsasalin ay maaaring maglaman ng mga error o pagkakamali. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
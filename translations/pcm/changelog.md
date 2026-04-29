# Changelog: MCP for Beginners Curriculum

Dis dokument na record for all di important changes wey dem make for di Model Context Protocol (MCP) for Beginners curriculum. Changes dey recorded for reverse chronological order (newest changes first).

## April 11, 2026

### New Lesson, Documentation Fixes, and Dependency Updates

#### New Curriculum Content Added

**Module 05 - Advanced Topics**
- **Lesson 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): New complete guide wey de explain di adversarial debate pattern for multi-agent systems
  - Mermaid architecture diagram: two agents → shared MCP server → debate transcript → judge → verdict
  - Shared MCP tool server (`web_search` + `run_python`) implement for Python and TypeScript
  - Opposing system prompts (FOR / AGAINST / Judge) with clear tool-use requirements
  - Debate orchestrator inside Python, TypeScript, and C# wey dey manage rounds and direct arguments
  - MCP `ClientSession` wiring for di orchestrator to real tool calls
  - Use-case table (hallucination detection, threat modeling, API design review, factual verification, tech selection)
  - Security considerations: sandboxed execution, tool-call validation, rate limiting, audit logging
  - Structured exercise with three practical scenarios (code review, architecture decision, content moderation)

#### Documentation Fixes

**Module 03 - Getting Started**
- **05-stdio-server/README.md**: Fix incomplete TypeScript stdio server example — add missing transport instantiation (`new StdioServerTransport()`) and `server.connect(transport)` call to match di Python and .NET examples for di same section
- **14-sampling/README.md**: Fix typo — correct `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculum Updates

**Main README.md**
- Add entry 5.17 (Adversarial Multi-Agent Reasoning with MCP) to di curriculum table wit direct link to di new lesson

**05-AdvancedTopics/README.md**
- Add Lesson 5.17 row to di lessons table

**study_guide.md**
- Add Adversarial Multi-Agent Reasoning topic to di mind-map and prose description of Advanced Topics

#### Code and Security Fixes

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Security fix — command injection**: Replace `execSync` shell interpolation wit `execFile` + `promisify` for di TypeScript `run_python` tool, wey stop command injection problem (LLM-controlled code now dey passed as literal argv element wit no shell involvement)
- **MCP tool loop wiring**: Update di Python debate orchestrator to use `AsyncAnthropic` client (replace blocking sync `Anthropic`), pass live `ClientSession` directly to each agent turn, fetch tool definitions with `session.list_tools()` each turn, and dispatch `tool_use` blocks wit `session.call_tool()` in loop until model give final text response

#### Dependency Updates

- Bump `hono` to 4.12.12 for plenti packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Bump `@hono/node-server` from 1.19.11 to 1.19.13 for TypeScript packages
- Bump `cryptography` from 46.0.5 to 46.0.7 for Python packages (10-StreamliningAIWorkflows labs 3 and 4)
- Bump `lodash` from 4.17.23 to 4.18.1 for 10-StreamliningAIWorkflows inspector

#### Translations

- Synced translations for 48+ languages wit di latest source changes (i18n update)

---

## February 5, 2026

### Repository-Wide Validation and Navigation Improvements

#### New Curriculum Content Added

**Module 03 - Getting Started**
- **12-mcp-hosts/README.md**: New detailed guide for setting up MCP hosts
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf configuration examples
  - JSON configuration templates for all main hosts
  - Transport types comparison table (stdio, SSE/HTTP, WebSocket)
  - Troubleshooting common connection problems
  - Security best practices for host configuration

- **13-mcp-inspector/README.md**: New debugging guide for MCP Inspector
  - Installation methods (npx, npm global, from source)
  - Connecting to servers via stdio and HTTP/SSE
  - Testing tools, resources, and prompts workflows
  - VS Code integration with MCP Inspector
  - Common debugging scenarios with solutions

**Module 04 - Practical Implementation**
- **pagination/README.md**: New pagination implementation guide
  - Cursor-based pagination patterns in Python, TypeScript, Java
  - Client-side pagination handling
  - Cursor design strategies (opaque vs. structured)
  - Performance optimization recommendations

**Module 05 - Advanced Topics**
- **mcp-protocol-features/README.md**: New protocol features detailed explanation
  - Progress notifications implementation
  - Request cancellation patterns
  - Resource templates with URI patterns
  - Server lifecycle management
  - Logging level control
  - Error handling patterns with JSON-RPC codes

#### Navigation Fixes (24+ files updated)

**Main Module READMEs**
 Now link to both first lesson AND next module

**02-Security Sub-files**
- All 5 supplementary security documents now get "What's Next" navigation:

**09-CaseStudy Files**
- All case study files now get sequential navigation:

**10-StreamliningAI Labs**
Add What's Next section to Module 10 overview and Module 11

#### Code and Content Fixes

**SDK and Dependency Updates**
Fix empty openai version to `^4.95.0`
Update SDK from `^1.8.0` to `>=1.26.0`
Update mcp version pins to `>=1.26.0`

**Code Fixes**
Fix invalid model `gpt-4o-mini` to `gpt-4.1-mini`

**Content Fixes**
Fix broken link `READMEmd` → `README.md`, fix curriculum header `Module 1-3` → `Module 0-3`, fix case-sensitive path
Remove corrupted duplicate Case Study 5 content

**Beginner Guidance Improvements**
Add proper introduction, learning objectives, and prerequisites for beginners

#### Curriculum Updates

**Main README.md**
- Add entries 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) to curriculum table

**Module READMEs**
Add lessons 12 and 13 to lesson list
Add Practical Guides section wit pagination link
Add lessons 5.15 (Custom Transport) and 5.16 (Protocol Features)

**study_guide.md**
- Update mindmap wit all new topics: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## Jan 28, 2026

### MCP Specification 2025-11-25 Compliance Review

#### Core Concepts Enhancement (01-CoreConcepts/)
- **New Client Primitive - Roots**: Add complete documentation on di Roots client primitive, wey dey enable servers to understand filesystem boundaries and access permissions
- **Tool Annotations**: Add documentation on tool behavioral annotations (`readOnlyHint`, `destructiveHint`) for beta tool execution decisions
- **Tool Calling in Sampling**: Update Sampling documentation to include `tools` and `toolChoice` parameters for model-driven tool invoke during sampling requests
- **URL Mode Elicitation**: Add documentation on URL-based elicitation for server-initiated external web interactions
- **Tasks (Experimental)**: Add new section documenting di experimental Tasks feature for durable execution wrappers and deferred result retrieval
- **Icons Support**: Note say tools, resources, resource templates, and prompts fit now include icons as extra metadata

#### Documentation Updates
- **README.md**: Add MCP Specification 2025-11-25 version reference and date-based versioning explanation
- **study_guide.md**: Update curriculum map to include Tasks and Tool Annotations in Core Concepts section; update document timestamp

#### Specification Compliance Verification
- **Protocol Version**: Confirm say all documentation reference current MCP Specification 2025-11-25
- **Architecture Alignment**: Confirm say two-layer architecture (Data Layer + Transport Layer) documentation dey accurate
- **Primitives Documentation**: Validate server primitives (Resources, Prompts, Tools) and client primitives (Sampling, Elicitation, Logging, Roots)
- **Transport Mechanisms**: Confirm STDIO and Streamable HTTP transport documentation accuracy
- **Security Guidance**: Confirm alignment wit current MCP Security Best Practices documentation

#### Key MCP 2025-11-25 Features Documented
- **OpenID Connect Discovery**: Auth server discovery through OIDC
- **OAuth Client ID Metadata Documents**: Recommend client registration mechanism
- **JSON Schema 2020-12**: Default dialect for MCP schema definitions
- **SDK Tiering System**: Formalize requirements for SDK feature support and maintenance
- **Governance Structure**: Formalize Working Groups and Interest Groups inside MCP governance

### Security Documentation Major Update (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **New Hands-On Training Resource**: Add complete integration wit di [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) throughout all security documentation
- **Expedition Route Coverage**: Document di complete camp-to-camp progression from Base Camp to Summit
- **OWASP Alignment**: All security guidance now dey mapped to OWASP MCP Azure Security Guide risks

#### OWASP MCP Top 10 Integration
- **New Section**: Add OWASP MCP Top 10 Security Risks table wit Azure mitigations to main Security README
- **Risk-Based Documentation**: Update mcp-security-controls-2025.md wit OWASP MCP risk references for each security domain
- **Reference Architecture**: Link to OWASP MCP Azure Security Guide reference architecture and implementation patterns

#### Updated Security Files
- **README.md**: Add Sherpa Workshop overview, expedition route table, OWASP MCP Top 10 risks summary, and hands-on training section
- **mcp-security-controls-2025.md**: Update header to February 2026, add OWASP risk references (MCP01-MCP08), fix spec version inconsistency
- **mcp-security-best-practices-2025.md**: Add Sherpa and OWASP resources section, update timestamp
- **mcp-best-practices.md**: Add hands-on training section wit Sherpa and OWASP links
- **azure-content-safety-implementation.md**: Add OWASP MCP06 reference, Sherpa Camp 3 alignment, and additional resources section

#### New Resource Links Added
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individual OWASP MCP risk pages (MCP01-MCP10)

### Curriculum-Wide MCP Specification 2025-11-25 Alignment

#### Module 03 - Getting Started
- **SDK Documentation**: Add Go SDK to official SDK list; update all SDK references to match MCP Specification 2025-11-25
- **Transport Clarification**: Update STDIO and HTTP Streaming transport descriptions wit explicit spec references

#### Module 04 - Practical Implementation
- **SDK Updates**: Add Go SDK; update SDK list with specification version reference
- **Authorization Spec**: Update MCP Authorization specification link to current 2025-11-25 version

#### Module 05 - Advanced Topics
- **New Features**: Add note about new MCP Specification 2025-11-25 features (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Security Resources**: Add OWASP MCP Top 10 and Sherpa workshop links to additional references

#### Module 06 - Community Contributions
- **SDK List**: Add Swift and Rust SDKs; update specification link to 2025-11-25
- **Spec Reference**: Update MCP Specification link to direct specification URL

#### Module 07 - Lessons from Early Adoption
- **Resource Updates**: Add MCP Specification 2025-11-25 link and OWASP MCP Top 10 to additional resources

#### Module 08 - Best Practices
- **Spec Version**: Update MCP Specification reference to 2025-11-25
- **Security Resources**: Add OWASP MCP Top 10 and Sherpa workshop to additional references

#### Module 10 - Streamlining AI Workflows
- **Badge Update**: Change MCP version badge from SDK version (1.9.3) to specification version (2025-11-25)
- **Resource Links**: Update MCP Specification link; add OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec Reference**: Update MCP Specification link to 2025-11-25 version
- **Security Resources**: Add OWASP MCP Top 10 to official resources

## December 18, 2025
### Security Documentation Update - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specification Version Update
- **Protocol Version Update**: Update make reference to di latest MCP Specification 2025-11-25 (wey dem release November 25, 2025)
  - Update all specification version reference dem from 2025-06-18 to 2025-11-25
  - Update document date reference dem from August 18, 2025 to December 18, 2025
  - Confirm say all specification URLs dem dey point to current documentation
- **Content Validation**: Proper validation of security best practices against up-to-date standards
  - **Microsoft Security Solutions**: Confirm say current terminology and links for Prompt Shields (wey dem dey call "Jailbreak risk detection" before), Azure Content Safety, Microsoft Entra ID, and Azure Key Vault correct
  - **OAuth 2.1 Security**: Confirm say e align with latest OAuth security best practices
  - **OWASP Standards**: Confirm say OWASP Top 10 for LLMs references still dey current
  - **Azure Services**: Confirm say all Microsoft Azure documentation links and best practices correct
- **Standards Alignment**: All referenced security standards confirm say dem current
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security and compliance frameworks
- **Implementation Resources**: Confirm say all implementation guide links and resources dey valid
  - Azure API Management authentication patterns
  - Microsoft Entra ID integration guides
  - Azure Key Vault secrets management
  - DevSecOps pipelines and monitoring solutions

### Documentation Quality Assurance
- **Specification Compliance**: Make sure all required MCP security requirements (MUST/MUST NOT) align with latest specification
- **Resource Currency**: Confirm say all external links to Microsoft documentation, security standards, and implementation guides correct
- **Best Practices Coverage**: Confirm say dem cover all authentication, authorization, AI-specific threats, supply chain security, and enterprise patterns well well

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: Introduce comprehensive guide to advanced MCP server usage, wey cover regular and low-level server architectures
  - **Regular vs. Low-Level Server**: Detail comparison and code examples for Python and TypeScript for both ways
  - **Handler-Based Design**: Explanation about handler-based tool/resource/prompt management for scalable, flexible server implementations
  - **Practical Patterns**: Real-world examples wey low-level server patterns dey help with advanced features and architecture

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide to implement simple authentication for MCP servers
  - **Auth Concepts**: Clear explanation on authentication versus authorization, plus how to handle credential dem
  - **Basic Auth Implementation**: Middleware-based authentication patterns for Python (Starlette) and TypeScript (Express), plus code samples
  - **Progression to Advanced Security**: Guide on how to start from simple auth go advance like OAuth 2.1 and RBAC, with references to advanced security modules

These additions dey provide practical, hand-on guidance for building more robust, secure, and flexible MCP server implementations, plus them link foundational concepts with advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: Add comprehensive hands-on curriculum for building production-ready MCP servers with PostgreSQL database integration
  - **Real-World Implementation**: Zava Retail analytics example show enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: Systematic update of all README files for 11-MCPServerHandsOnLabs to use "Lab" term instead of "Module"
  - **Section Headers**: Change "What This Module Covers" to "What This Lab Covers" for all 13 labs
  - **Content Description**: Change "This module provides..." to "This lab provides..." throughout all documents
  - **Learning Objectives**: Change "By the end of this module..." to "By the end of this lab..."
  - **Navigation Links**: Change all "Module XX:" references to "Lab XX:" for cross-references and navigation
  - **Completion Tracking**: Change "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: Keep Python module references unchanged inside configuration files (like `"module": "mcp_server.main"`)

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Add new "11. Database Integration Labs" section with full lab structure visualization
- **Repository Structure**: Change from ten to eleven main sections with detailed 11-MCPServerHandsOnLabs explanation
- **Learning Path Guidance**: Improve navigation instructions to cover sections 00-11
- **Technology Coverage**: Add FastMCP, PostgreSQL, Azure services integration info
- **Learning Outcomes**: Highlight production-ready server development, database integration patterns, and enterprise security

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Update main README.md in 11-MCPServerHandsOnLabs to consistently use "Lab" structure
- **Learning Path Organization**: Clear progression from foundation concepts through advanced implementation to production deployment
- **Real-World Focus**: Highlight practical, hands-on learning with enterprise-grade patterns and technologies

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: Stress practical, lab-based approach everywhere for documentation
- **Enterprise Patterns Focus**: Emphasize production-ready implementations and enterprise security considerations
- **Technology Integration**: Cover modern Azure services and AI integration patterns fully
- **Learning Progression**: Clear, structured path from basic concepts to production deployment

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Major expansion with big GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: New strong case study to show GitHub MCP Registry launch for September 2025
    - **Problem Analysis**: Detailed look at how fragmented MCP server discovery and deployment get wahala
    - **Solution Architecture**: GitHub centralized registry way with one-click VS Code installation
    - **Business Impact**: Clear improvement for developer onboarding and productivity
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability
    - **Ecosystem Development**: Show am as foundational platform for agentic integration
  - **Enhanced Case Study Structure**: Update all seven case studies with consistent style and full descriptions
    - Azure AI Travel Agents: Multi-agent orchestration emphasis
    - Azure DevOps Integration: Workflow automation focus
    - Real-Time Documentation Retrieval: Python console client implementation
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code and GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Ecosystem development and community platform
  - **Comprehensive Conclusion**: Rewrite conclusion section highlight all seven case studies covering different MCP implementation dimensions
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications categorization
    - Better insight about architectural patterns, implementation ways, and best practices
    - Highlight MCP as mature, production-ready protocol

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Update mindmap with GitHub MCP Registry in Case Studies section
- **Case Studies Description**: Improve from general stories to detailed breakdown of seven strong case studies
- **Repository Structure**: Update section 10 to show full case study coverage and implementation details
- **Changelog Integration**: Add September 26, 2025 entry for GitHub MCP Registry addition and case study improvements
- **Date Updates**: Update footer timestamp to show latest revision (September 26, 2025)

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardize case study formatting and structure for all seven examples
- **Comprehensive Coverage**: Case studies now cover enterprise, developer productivity, and ecosystem development well
- **Strategic Positioning**: Highlight focus on MCP as foundational platform for agentic system deployment
- **Resource Integration**: Update more resources to add GitHub MCP Registry link

## September 15, 2025

### Advanced Topics Expansion - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - New Advanced Implementation Guide
- **README.md**: Complete guide for custom MCP transport mechanisms
  - **Azure Event Grid Transport**: Full serverless event-driven transport implementation
    - Examples in C#, TypeScript, and Python with Azure Functions integration
    - Event-driven architecture patterns for scalable MCP solutions
    - Webhook receivers and push-based message handling
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation
    - Real-time streaming for low-latency scenarios
    - Partitioning strategies and checkpointing management
    - Message batching and optimization for better performance
  - **Enterprise Integration Patterns**: Production-ready architecture examples
    - Distributed MCP processing across many Azure Functions
    - Hybrid transport architectures combining different transport types
    - Message durability, reliability, and error handling patterns
  - **Security & Monitoring**: Azure Key Vault integration and observability patterns
    - Managed identity authentication and least privilege access
    - Application Insights telemetry and performance monitoring
    - Circuit breakers and fault tolerance architectures
  - **Testing Frameworks**: Complete testing strategies for custom transports
    - Unit test with test doubles and mocks
    - Integration testing with Azure Test Containers
    - Performance and load testing considerations

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Emerging AI Discipline
- **README.md**: Deep look at context engineering as new field
  - **Core Principles**: Complete context sharing, action decision awareness, and managing context windows
  - **MCP Protocol Alignment**: How MCP design address context engineering challenges
    - Context window limits and progressive loading methods
    - Relevance determination and dynamic context retrieval
    - Handling multi-modal context and security considerations
  - **Implementation Approaches**: Single-threaded versus multi-agent architectures
    - Context chunking and prioritization techniques
    - Progressive context loading and compression methods
    - Layered context methods and retrieval optimization
  - **Measurement Framework**: New metrics for context effectiveness evaluation
    - Input efficiency, performance, quality, and user experience considerations
    - Experimental ways for context optimization
    - Failure analysis and improvement methods

#### Curriculum Navigation Updates (README.md)
- **Enhanced Module Structure**: Update curriculum table to add new advanced topics
  - Add Context Engineering (5.14) and Custom Transport (5.15) entries
  - Consistent formatting and navigation links for all modules
  - Update descriptions to reflect current content scope

### Directory Structure Improvements
- **Naming Standardization**: Rename "mcp transport" folder to "mcp-transport" to match other advanced topic folders
- **Content Organization**: All 05-AdvancedTopics folders now dey follow same naming pattern (mcp-[topic])

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content refer to current MCP Specification 2025-06-18
- **Multi-Language Examples**: Many code examples in C#, TypeScript, and Python
- **Enterprise Focus**: Production-ready patterns and Azure cloud integration throughout
- **Visual Documentation**: Mermaid diagrams for architecture and flow visualization

## August 18, 2025

### Documentation Comprehensive Update - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Complete Modernization
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Complete rewrite wey align with MCP Specification 2025-06-18
  - **Mandatory Requirements**: Add explicit MUST/MUST NOT requirements from official specification with clear visual indicators
  - **12 Core Security Practices**: Restructure from 15-item list to comprehensive security domains
    - Token Security & Authentication with external identity provider integration
    - Session Management & Transport Security with cryptographic requirements
    - AI-Specific Threat Protection with Microsoft Prompt Shields integration
    - Access Control & Permissions with principle of least privilege
    - Content Safety & Monitoring with Azure Content Safety integration
    - Supply Chain Security with comprehensive component verification
    - OAuth Security & Confused Deputy Prevention with PKCE implementation
    - Incident Response & Recovery with automated capabilities
    - Compliance & Governance with regulatory alignment
    - Advanced Security Controls with zero trust architecture
    - Microsoft Security Ecosystem Integration with comprehensive solutions
    - Continuous Security Evolution with adaptive practices
  - **Microsoft Security Solutions**: Enhanced integration guidance for Prompt Shields, Azure Content Safety, Entra ID, and GitHub Advanced Security
  - **Implementation Resources**: Categorized comprehensive resource links by Official MCP Documentation, Microsoft Security Solutions, Security Standards, and Implementation Guides

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Complete overhaul wit enterprise-grade security framework
  - **9 Comprehensive Security Domains**: Expand from basic controls to detailed enterprise framework
    - Advanced Authentication & Authorization with Microsoft Entra ID integration
    - Token Security & Anti-Passthrough Controls with comprehensive validation
    - Session Security Controls with hijacking prevention
    - AI-Specific Security Controls with prompt injection and tool poisoning prevention
    - Confused Deputy Attack Prevention with OAuth proxy security
    - Tool Execution Security with sandboxing and isolation
    - Supply Chain Security Controls with dependency verification
    - Monitoring & Detection Controls with SIEM integration
    - Incident Response & Recovery with automated capabilities
  - **Implementation Examples**: Add detailed YAML configuration blocks and code examples
  - **Microsoft Solutions Integration**: Comprehensive coverage of Azure security services, GitHub Advanced Security, and enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Complete rewrite for enterprise security implementation
  - **Current Specification Alignment**: Update to MCP Specification 2025-06-18 wit mandatory security requirements
  - **Enhanced Authentication**: Microsoft Entra ID integration wit comprehensive .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety implementation wit detailed Python examples
  - **Advanced Threat Mitigation**: Comprehensive implementation examples for
    - Confused Deputy Attack Prevention wit PKCE and user consent validation
    - Token Passthrough Prevention wit audience validation and secure token management
    - Session Hijacking Prevention wit cryptographic binding and behavioral analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, and supply chain security
  - **Implementation Checklist**: Clear mandatory vs. recommended security controls wit Microsoft security ecosystem benefits

### Documentation Quality & Standards Alignment
- **Specification References**: Update all references to current MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Enhanced integration guidance throughout all security documentation
- **Practical Implementation**: Add detailed code examples in .NET, Java, and Python wit enterprise patterns
- **Resource Organization**: Comprehensive categorization of official documentation, security standards, and implementation guides
- **Visual Indicators**: Clear marking of mandatory requirements vs. recommended practices


#### Core Concepts (01-CoreConcepts/) - Complete Modernization
- **Protocol Version Update**: Update to reference current MCP Specification 2025-06-18 wit date-based versioning (YYYY-MM-DD format)
- **Architecture Refinement**: Enhanced descriptions of Hosts, Clients, and Servers to reflect current MCP architecture patterns
  - Hosts now clearly defined as AI applications coordinating multiple MCP client connections
  - Clients described as protocol connectors maintaining one-to-one server relationships
  - Servers enhanced wit local vs. remote deployment scenarios
- **Primitive Restructuring**: Complete overhaul of server and client primitives
  - Server Primitives: Resources (data sources), Prompts (templates), Tools (executable functions) wit detailed explanations and examples
  - Client Primitives: Sampling (LLM completions), Elicitation (user input), Logging (debugging/monitoring)
  - Update wit current discovery (`*/list`), retrieval (`*/get`), and execution (`*/call`) method patterns
- **Protocol Architecture**: Introduce two-layer architecture model
  - Data Layer: JSON-RPC 2.0 foundation wit lifecycle management and primitives
  - Transport Layer: STDIO (local) and Streamable HTTP wit SSE (remote) transport mechanisms
- **Security Framework**: Comprehensive security principles including explicit user consent, data privacy protection, tool execution safety, and transport layer security
- **Communication Patterns**: Update protocol messages to show initialization, discovery, execution, and notification flows
- **Code Examples**: Refresh multi-language examples (.NET, Java, Python, JavaScript) to reflect current MCP SDK patterns

#### Security (02-Security/) - Comprehensive Security Overhaul  
- **Standards Alignment**: Full alignment wit MCP Specification 2025-06-18 security requirements
- **Authentication Evolution**: Document evolution from custom OAuth servers to external identity provider delegation (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Enhanced coverage of modern AI attack vectors
  - Detailed prompt injection attack scenarios wit real-world examples
  - Tool poisoning mechanisms and "rug pull" attack patterns
  - Context window poisoning and model confusion attacks
- **Microsoft AI Security Solutions**: Comprehensive coverage of Microsoft security ecosystem
  - AI Prompt Shields wit advanced detection, spotlighting, and delimiter techniques
  - Azure Content Safety integration patterns
  - GitHub Advanced Security for supply chain protection
- **Advanced Threat Mitigation**: Detailed security controls for
  - Session hijacking wit MCP-specific attack scenarios and cryptographic session ID requirements
  - Confused deputy problems in MCP proxy scenarios wit explicit consent requirements
  - Token passthrough vulnerabilities wit mandatory validation controls
- **Supply Chain Security**: Expanded AI supply chain coverage including foundation models, embeddings services, context providers, and third-party APIs
- **Foundation Security**: Enhanced integration wit enterprise security patterns including zero trust architecture and Microsoft security ecosystem
- **Resource Organization**: Categorized comprehensive resource links by type (Official Docs, Standards, Research, Microsoft Solutions, Implementation Guides)

### Documentation Quality Improvements
- **Structured Learning Objectives**: Enhanced learning objectives wit specific, actionable outcomes 
- **Cross-References**: Add links between related security and core concept topics
- **Current Information**: Update all date references and specification links to current standards
- **Implementation Guidance**: Add specific, actionable implementation guidelines throughout both sections

## July 16, 2025

### README and Navigation Improvements
- Completely redesign curriculum navigation in README.md
- Replace `<details>` tags wit more accessible table-based format
- Create alternative layout options in new "alternative_layouts" folder
- Add card-based, tabbed-style, and accordion-style navigation examples
- Update repository structure section to include all latest files
- Enhance "How to Use This Curriculum" section wit clear recommendations
- Update MCP specification links to point to correct URLs
- Add Context Engineering section (5.14) to curriculum structure

### Study Guide Updates
- Completely revise study guide to align wit current repository structure
- Add new sections for MCP Clients and Tools, and Popular MCP Servers
- Update Visual Curriculum Map to accurately reflect all topics
- Enhance descriptions of Advanced Topics to cover all specialized areas
- Update Case Studies section to reflect actual examples
- Add this comprehensive changelog

### Community Contributions (06-CommunityContributions/)
- Add detailed information about MCP servers for image generation
- Add comprehensive section on using Claude in VSCode
- Add Cline terminal client setup and usage instructions
- Update MCP client section to include all popular client options
- Enhance contribution examples wit more accurate code samples

### Advanced Topics (05-AdvancedTopics/)
- Organize all specialized topic folders wit consistent naming
- Add context engineering materials and examples
- Add Foundry agent integration documentation
- Enhance Entra ID security integration documentation

## June 11, 2025

### Initial Creation
- Release first version of MCP for Beginners curriculum
- Create basic structure for all 10 main sections
- Implement Visual Curriculum Map for navigation
- Add initial sample projects in multiple programming languages

### Getting Started (03-GettingStarted/)
- Create first server implementation examples
- Add client development guidance
- Include LLM client integration instructions
- Add VS Code integration documentation
- Implement Server-Sent Events (SSE) server examples

### Core Concepts (01-CoreConcepts/)
- Add detailed explanation of client-server architecture
- Create documentation on key protocol components
- Document messaging patterns in MCP

## May 23, 2025

### Repository Structure
- Initialize repository with basic folder structure
- Create README files for each major section
- Set up translation infrastructure
- Add image assets and diagrams

### Documentation
- Create initial README.md wit curriculum overview
- Add CODE_OF_CONDUCT.md and SECURITY.md
- Set up SUPPORT.md wit guidance for getting help
- Create preliminary study guide structure

## April 15, 2025

### Planning and Framework
- Initial planning for MCP for Beginners curriculum
- Define learning objectives and target audience
- Outline 10-section structure of curriculum
- Develop conceptual framework for examples and case studies
- Create initial prototype examples for key concepts

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg make you sabi say automated translations fit get errors or mistakes. Di original document wey dey im correct language na di real correct source. For important info, na professional human translation dey recommended. We no go take responsibility for any misunderstanding or wrong interpretation wey fit happen from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
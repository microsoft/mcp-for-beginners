# Changelog: MCP for Beginners Curriculum

Dis dokument na record of all di important changes wey dem make for di Model Context Protocol (MCP) for Beginners curriculum. Changes dem dey documented for reverse chronological order (newest changes first).

## December 18, 2025

### Security Documentation Update - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specification Version Update
- **Protocol Version Update**: Updated to reference latest MCP Specification 2025-11-25 (wey dem release November 25, 2025)
  - Updated all specification version references from 2025-06-18 to 2025-11-25
  - Updated document date references from August 18, 2025 to December 18, 2025
  - Verified all specification URLs dey point to current documentation
- **Content Validation**: Comprehensive validation of security best practices against latest standards
  - **Microsoft Security Solutions**: Verified current terminology and links for Prompt Shields (wey before dem dey call am "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, and Azure Key Vault
  - **OAuth 2.1 Security**: Confirmed say e align with latest OAuth security best practices
  - **OWASP Standards**: Validated OWASP Top 10 for LLMs references still dey current
  - **Azure Services**: Verified all Microsoft Azure documentation links and best practices
- **Standards Alignment**: All referenced security standards confirmed say dem dey current
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security and compliance frameworks
- **Implementation Resources**: Validated all implementation guide links and resources
  - Azure API Management authentication patterns
  - Microsoft Entra ID integration guides
  - Azure Key Vault secrets management
  - DevSecOps pipelines and monitoring solutions

### Documentation Quality Assurance
- **Specification Compliance**: Make sure say all mandatory MCP security requirements (MUST/MUST NOT) dey align with latest specification
- **Resource Currency**: Verified all external links to Microsoft documentation, security standards, and implementation guides
- **Best Practices Coverage**: Confirm say e cover well well authentication, authorization, AI-specific threats, supply chain security, and enterprise patterns

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: Introduce comprehensive guide to advanced MCP server usage, wey cover both regular and low-level server architectures.
  - **Regular vs. Low-Level Server**: Detailed comparison and code examples for Python and TypeScript for both ways.
  - **Handler-Based Design**: Explanation of handler-based tool/resource/prompt management for scalable, flexible server implementations.
  - **Practical Patterns**: Real-world scenarios wey low-level server patterns dey useful for advanced features and architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide to implement simple authentication for MCP servers.
  - **Auth Concepts**: Clear explanation of authentication vs. authorization, and how to handle credentials.
  - **Basic Auth Implementation**: Middleware-based authentication patterns for Python (Starlette) and TypeScript (Express), with code samples.
  - **Progression to Advanced Security**: Guidance on how to start with simple auth and move go OAuth 2.1 and RBAC, with references to advanced security modules.

These additions dey provide practical, hands-on guidance to build more strong, secure, and flexible MCP server implementations, wey go connect foundational concepts with advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: Add comprehensive hands-on curriculum to build production-ready MCP servers with PostgreSQL database integration
  - **Real-World Implementation**: Zava Retail analytics use case wey show enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: Systematically update all README files for 11-MCPServerHandsOnLabs to use "Lab" terminology instead of "Module"
  - **Section Headers**: Update "What This Module Covers" to "What This Lab Covers" for all 13 labs
  - **Content Description**: Change "This module provides..." to "This lab provides..." everywhere
  - **Learning Objectives**: Update "By the end of this module..." to "By the end of this lab..." 
  - **Navigation Links**: Convert all "Module XX:" references to "Lab XX:" for cross-references and navigation
  - **Completion Tracking**: Update "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: Keep Python module references in configuration files (e.g., `"module": "mcp_server.main"`)

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Add new "11. Database Integration Labs" section with full lab structure visualization
- **Repository Structure**: Update from ten to eleven main sections with detailed 11-MCPServerHandsOnLabs description
- **Learning Path Guidance**: Improve navigation instructions to cover sections 00-11
- **Technology Coverage**: Add FastMCP, PostgreSQL, Azure services integration details
- **Learning Outcomes**: Emphasize production-ready server development, database integration patterns, and enterprise security

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Update main README.md in 11-MCPServerHandsOnLabs to consistently use "Lab" structure
- **Learning Path Organization**: Clear progression from foundational concepts through advanced implementation to production deployment
- **Real-World Focus**: Emphasize practical, hands-on learning with enterprise-grade patterns and technologies

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: Reinforce practical, lab-based approach throughout documentation
- **Enterprise Patterns Focus**: Highlight production-ready implementations and enterprise security considerations
- **Technology Integration**: Comprehensive coverage of modern Azure services and AI integration patterns
- **Learning Progression**: Clear, structured path from basic concepts to production deployment

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Major expansion with comprehensive GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: New comprehensive case study wey examine GitHub's MCP Registry launch for September 2025
    - **Problem Analysis**: Detailed look at fragmented MCP server discovery and deployment wahala
    - **Solution Architecture**: GitHub's centralized registry approach with one-click VS Code installation
    - **Business Impact**: Measurable improvements for developer onboarding and productivity
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability
    - **Ecosystem Development**: Position as foundational platform for agentic integration
  - **Enhanced Case Study Structure**: Update all seven case studies with consistent formatting and full descriptions
    - Azure AI Travel Agents: Multi-agent orchestration emphasis
    - Azure DevOps Integration: Workflow automation focus
    - Real-Time Documentation Retrieval: Python console client implementation
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code and GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Ecosystem development and community platform
  - **Comprehensive Conclusion**: Rewrite conclusion section to highlight seven case studies wey cover multiple MCP implementation dimensions
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications categorization
    - Enhanced insights into architectural patterns, implementation strategies, and best practices
    - Emphasis on MCP as mature, production-ready protocol

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Update mindmap to include GitHub MCP Registry for Case Studies section
- **Case Studies Description**: Improve from generic descriptions to detailed breakdown of seven comprehensive case studies
- **Repository Structure**: Update section 10 to reflect full case study coverage with specific implementation details
- **Changelog Integration**: Add September 26, 2025 entry wey document GitHub MCP Registry addition and case study enhancements
- **Date Updates**: Update footer timestamp to reflect latest revision (September 26, 2025)

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardize case study formatting and structure across all seven examples
- **Comprehensive Coverage**: Case studies now cover enterprise, developer productivity, and ecosystem development scenarios
- **Strategic Positioning**: Enhance focus on MCP as foundational platform for agentic system deployment
- **Resource Integration**: Update additional resources to include GitHub MCP Registry link

## September 15, 2025

### Advanced Topics Expansion - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - New Advanced Implementation Guide
- **README.md**: Complete implementation guide for custom MCP transport mechanisms
  - **Azure Event Grid Transport**: Comprehensive serverless event-driven transport implementation
    - C#, TypeScript, and Python examples with Azure Functions integration
    - Event-driven architecture patterns for scalable MCP solutions
    - Webhook receivers and push-based message handling
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation
    - Real-time streaming capabilities for low-latency scenarios
    - Partitioning strategies and checkpoint management
    - Message batching and performance optimization
  - **Enterprise Integration Patterns**: Production-ready architectural examples
    - Distributed MCP processing across multiple Azure Functions
    - Hybrid transport architectures combining multiple transport types
    - Message durability, reliability, and error handling strategies
  - **Security & Monitoring**: Azure Key Vault integration and observability patterns
    - Managed identity authentication and least privilege access
    - Application Insights telemetry and performance monitoring
    - Circuit breakers and fault tolerance patterns
  - **Testing Frameworks**: Comprehensive testing strategies for custom transports
    - Unit testing with test doubles and mocking frameworks
    - Integration testing with Azure Test Containers
    - Performance and load testing considerations

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Emerging AI Discipline
- **README.md**: Comprehensive exploration of context engineering as an emerging field
  - **Core Principles**: Complete context sharing, action decision awareness, and context window management
  - **MCP Protocol Alignment**: How MCP design dey address context engineering challenges
    - Context window limitations and progressive loading strategies
    - Relevance determination and dynamic context retrieval
    - Multi-modal context handling and security considerations
  - **Implementation Approaches**: Single-threaded vs. multi-agent architectures
    - Context chunking and prioritization techniques
    - Progressive context loading and compression strategies
    - Layered context approaches and retrieval optimization
  - **Measurement Framework**: Emerging metrics for context effectiveness evaluation
    - Input efficiency, performance, quality, and user experience considerations
    - Experimental approaches to context optimization
    - Failure analysis and improvement methodologies

#### Curriculum Navigation Updates (README.md)
- **Enhanced Module Structure**: Update curriculum table to include new advanced topics
  - Add Context Engineering (5.14) and Custom Transport (5.15) entries
  - Consistent formatting and navigation links across all modules
  - Update descriptions to reflect current content scope

### Directory Structure Improvements
- **Naming Standardization**: Rename "mcp transport" to "mcp-transport" for consistency with other advanced topic folders
- **Content Organization**: All 05-AdvancedTopics folders now follow consistent naming pattern (mcp-[topic])

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content reference current MCP Specification 2025-06-18
- **Multi-Language Examples**: Comprehensive code examples for C#, TypeScript, and Python
- **Enterprise Focus**: Production-ready patterns and Azure cloud integration throughout
- **Visual Documentation**: Mermaid diagrams for architecture and flow visualization

## August 18, 2025

### Documentation Comprehensive Update - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Complete Modernization
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Complete rewrite wey align with MCP Specification 2025-06-18
  - **Mandatory Requirements**: Add explicit MUST/MUST NOT requirements from official specification wit clear visual indicators
  - **12 Core Security Practices**: Restructure from 15-item list to comprehensive security domains
    - Token Security & Authentication wit external identity provider integration
    - Session Management & Transport Security wit cryptographic requirements
    - AI-Specific Threat Protection wit Microsoft Prompt Shields integration
    - Access Control & Permissions wit principle of least privilege
    - Content Safety & Monitoring wit Azure Content Safety integration
    - Supply Chain Security wit comprehensive component verification
    - OAuth Security & Confused Deputy Prevention wit PKCE implementation
    - Incident Response & Recovery wit automated capabilities
    - Compliance & Governance wit regulatory alignment
    - Advanced Security Controls wit zero trust architecture
    - Microsoft Security Ecosystem Integration wit comprehensive solutions
    - Continuous Security Evolution wit adaptive practices
  - **Microsoft Security Solutions**: Enhanced integration guidance for Prompt Shields, Azure Content Safety, Entra ID, and GitHub Advanced Security
  - **Implementation Resources**: Categorized comprehensive resource links by Official MCP Documentation, Microsoft Security Solutions, Security Standards, and Implementation Guides

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Complete overhaul wit enterprise-grade security framework
  - **9 Comprehensive Security Domains**: Expanded from basic controls to detailed enterprise framework
    - Advanced Authentication & Authorization wit Microsoft Entra ID integration
    - Token Security & Anti-Passthrough Controls wit comprehensive validation
    - Session Security Controls wit hijacking prevention
    - AI-Specific Security Controls wit prompt injection and tool poisoning prevention
    - Confused Deputy Attack Prevention wit OAuth proxy security
    - Tool Execution Security wit sandboxing and isolation
    - Supply Chain Security Controls wit dependency verification
    - Monitoring & Detection Controls wit SIEM integration
    - Incident Response & Recovery wit automated capabilities
  - **Implementation Examples**: Added detailed YAML configuration blocks and code examples
  - **Microsoft Solutions Integration**: Comprehensive coverage of Azure security services, GitHub Advanced Security, and enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Complete rewrite for enterprise security implementation
  - **Current Specification Alignment**: Updated to MCP Specification 2025-06-18 wit mandatory security requirements
  - **Enhanced Authentication**: Microsoft Entra ID integration wit comprehensive .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety implementation wit detailed Python examples
  - **Advanced Threat Mitigation**: Comprehensive implementation examples for
    - Confused Deputy Attack Prevention wit PKCE and user consent validation
    - Token Passthrough Prevention wit audience validation and secure token management
    - Session Hijacking Prevention wit cryptographic binding and behavioral analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, and supply chain security
  - **Implementation Checklist**: Clear mandatory vs. recommended security controls wit Microsoft security ecosystem benefits

### Documentation Quality & Standards Alignment
- **Specification References**: Updated all references to current MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Enhanced integration guidance throughout all security documentation
- **Practical Implementation**: Added detailed code examples in .NET, Java, and Python wit enterprise patterns
- **Resource Organization**: Comprehensive categorization of official documentation, security standards, and implementation guides
- **Visual Indicators**: Clear marking of mandatory requirements vs. recommended practices


#### Core Concepts (01-CoreConcepts/) - Complete Modernization
- **Protocol Version Update**: Updated to reference current MCP Specification 2025-06-18 wit date-based versioning (YYYY-MM-DD format)
- **Architecture Refinement**: Enhanced descriptions of Hosts, Clients, and Servers to reflect current MCP architecture patterns
  - Hosts now clearly defined as AI applications coordinating multiple MCP client connections
  - Clients described as protocol connectors maintaining one-to-one server relationships
  - Servers enhanced wit local vs. remote deployment scenarios
- **Primitive Restructuring**: Complete overhaul of server and client primitives
  - Server Primitives: Resources (data sources), Prompts (templates), Tools (executable functions) wit detailed explanations and examples
  - Client Primitives: Sampling (LLM completions), Elicitation (user input), Logging (debugging/monitoring)
  - Updated wit current discovery (`*/list`), retrieval (`*/get`), and execution (`*/call`) method patterns
- **Protocol Architecture**: Introduced two-layer architecture model
  - Data Layer: JSON-RPC 2.0 foundation wit lifecycle management and primitives
  - Transport Layer: STDIO (local) and Streamable HTTP wit SSE (remote) transport mechanisms
- **Security Framework**: Comprehensive security principles including explicit user consent, data privacy protection, tool execution safety, and transport layer security
- **Communication Patterns**: Updated protocol messages to show initialization, discovery, execution, and notification flows
- **Code Examples**: Refreshed multi-language examples (.NET, Java, Python, JavaScript) to reflect current MCP SDK patterns

#### Security (02-Security/) - Comprehensive Security Overhaul  
- **Standards Alignment**: Full alignment wit MCP Specification 2025-06-18 security requirements
- **Authentication Evolution**: Documented evolution from custom OAuth servers to external identity provider delegation (Microsoft Entra ID)
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
- **Cross-References**: Added links between related security and core concept topics
- **Current Information**: Updated all date references and specification links to current standards
- **Implementation Guidance**: Added specific, actionable implementation guidelines throughout both sections

## July 16, 2025

### README and Navigation Improvements
- Completely redesigned di curriculum navigation in README.md
- Replaced `<details>` tags wit more accessible table-based format
- Created alternative layout options in new "alternative_layouts" folder
- Added card-based, tabbed-style, and accordion-style navigation examples
- Updated repository structure section to include all latest files
- Enhanced "How to Use This Curriculum" section wit clear recommendations
- Updated MCP specification links to point to correct URLs
- Added Context Engineering section (5.14) to di curriculum structure

### Study Guide Updates
- Completely revised di study guide to align wit current repository structure
- Added new sections for MCP Clients and Tools, and Popular MCP Servers
- Updated di Visual Curriculum Map to accurately reflect all topics
- Enhanced descriptions of Advanced Topics to cover all specialized areas
- Updated Case Studies section to reflect actual examples
- Added dis comprehensive changelog

### Community Contributions (06-CommunityContributions/)
- Added detailed information about MCP servers for image generation
- Added comprehensive section on using Claude in VSCode
- Added Cline terminal client setup and usage instructions
- Updated MCP client section to include all popular client options
- Enhanced contribution examples wit more accurate code samples

### Advanced Topics (05-AdvancedTopics/)
- Organized all specialized topic folders wit consistent naming
- Added context engineering materials and examples
- Added Foundry agent integration documentation
- Enhanced Entra ID security integration documentation

## June 11, 2025

### Initial Creation
- Released first version of di MCP for Beginners curriculum
- Created basic structure for all 10 main sections
- Implemented Visual Curriculum Map for navigation
- Added initial sample projects in multiple programming languages

### Getting Started (03-GettingStarted/)
- Created first server implementation examples
- Added client development guidance
- Included LLM client integration instructions
- Added VS Code integration documentation
- Implemented Server-Sent Events (SSE) server examples

### Core Concepts (01-CoreConcepts/)
- Added detailed explanation of client-server architecture
- Created documentation on key protocol components
- Documented messaging patterns in MCP

## May 23, 2025

### Repository Structure
- Initialized di repository wit basic folder structure
- Created README files for each major section
- Set up translation infrastructure
- Added image assets and diagrams

### Documentation
- Created initial README.md wit curriculum overview
- Added CODE_OF_CONDUCT.md and SECURITY.md
- Set up SUPPORT.md wit guidance for getting help
- Created preliminary study guide structure

## April 15, 2025

### Planning and Framework
- Initial planning for MCP for Beginners curriculum
- Defined learning objectives and target audience
- Outlined 10-section structure of di curriculum
- Developed conceptual framework for examples and case studies
- Created initial prototype examples for key concepts

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some errors or wahala. Di original document wey dey im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
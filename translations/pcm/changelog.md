<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "beaeca2ae0ec007783e6310a3b63291f",
  "translation_date": "2025-11-18T18:46:20+00:00",
  "source_file": "changelog.md",
  "language_code": "pcm"
}
-->
# Changelog: MCP for Beginners Curriculum

Dis file na record of all di big changes wey dem don make for di Model Context Protocol (MCP) for Beginners curriculum. Di changes dey arranged from di newest go di oldest.

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: We don add one full guide wey go teach how to use MCP server for advanced level, e cover regular and low-level server architecture.
  - **Regular vs. Low-Level Server**: We explain di difference and show code example for Python and TypeScript for di two methods.
  - **Handler-Based Design**: We explain how handler-based tool/resource/prompt management fit help make server implementation scalable and flexible.
  - **Practical Patterns**: Real-life example wey show how low-level server pattern fit help for advanced features and architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide wey dey show how to do simple authentication for MCP servers.
  - **Auth Concepts**: We explain authentication vs. authorization, and how to handle credentials.
  - **Basic Auth Implementation**: Middleware-based authentication pattern for Python (Starlette) and TypeScript (Express), with code samples.
  - **Progression to Advanced Security**: How to start with simple auth and move to OAuth 2.1 and RBAC, with reference to advanced security modules.

Dis new chapters go help people learn how to build MCP servers wey strong, secure, and flexible, and e go connect di basic concepts to advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: We don add one full hands-on curriculum wey go teach how to build MCP servers wey ready for production with PostgreSQL database integration.
  - **Real-World Implementation**: Zava Retail analytics use case wey show enterprise-grade patterns.
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup.
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development.  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration.
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization.
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights.
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring.

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: We don update all README files for 11-MCPServerHandsOnLabs to use "Lab" instead of "Module."
  - **Section Headers**: Change "What This Module Covers" to "What This Lab Covers" for all 13 labs.
  - **Content Description**: Change "This module provides..." to "This lab provides..." for di documentation.
  - **Learning Objectives**: Change "By the end of this module..." to "By the end of this lab..."
  - **Navigation Links**: Change all "Module XX:" references to "Lab XX:" for cross-references and navigation.
  - **Completion Tracking**: Change "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: We no touch Python module references for configuration files (e.g., `"module": "mcp_server.main"`).

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Add new "11. Database Integration Labs" section with full lab structure visualization.
- **Repository Structure**: Update from ten to eleven main sections with detailed description for 11-MCPServerHandsOnLabs.
- **Learning Path Guidance**: Improve navigation instructions to cover sections 00-11.
- **Technology Coverage**: Add FastMCP, PostgreSQL, Azure services integration details.
- **Learning Outcomes**: Focus on production-ready server development, database integration patterns, and enterprise security.

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Update main README.md for 11-MCPServerHandsOnLabs to use "Lab" structure.
- **Learning Path Organization**: Clear progression from basic concepts to advanced implementation to production deployment.
- **Real-World Focus**: Emphasis on practical, hands-on learning with enterprise-grade patterns and technologies.

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: We dey focus on practical, lab-based approach for di documentation.
- **Enterprise Patterns Focus**: Highlight production-ready implementations and enterprise security considerations.
- **Technology Integration**: Full coverage of modern Azure services and AI integration patterns.
- **Learning Progression**: Clear, structured path from basic concepts to production deployment.

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Big expansion with full GitHub MCP Registry case study.
  - **GitHub MCP Registry Case Study**: New case study wey dey look GitHub's MCP Registry launch for September 2025.
    - **Problem Analysis**: Detailed look at di fragmented MCP server discovery and deployment challenges.
    - **Solution Architecture**: GitHub's centralized registry approach with one-click VS Code installation.
    - **Business Impact**: Improvements for developer onboarding and productivity.
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability.
    - **Ecosystem Development**: Positioning as foundational platform for agentic integration.
  - **Enhanced Case Study Structure**: Update all seven case studies with consistent formatting and full descriptions.
    - Azure AI Travel Agents: Multi-agent orchestration emphasis.
    - Azure DevOps Integration: Workflow automation focus.
    - Real-Time Documentation Retrieval: Python console client implementation.
    - Interactive Study Plan Generator: Chainlit conversational web app.
    - In-Editor Documentation: VS Code and GitHub Copilot integration.
    - Azure API Management: Enterprise API integration patterns.
    - GitHub MCP Registry: Ecosystem development and community platform.
  - **Comprehensive Conclusion**: Rewrite conclusion section to highlight seven case studies wey dey cover different MCP implementation dimensions.
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity.
    - Ecosystem Development, Educational Applications categorization.
    - Better insights into architectural patterns, implementation strategies, and best practices.
    - Focus on MCP as mature, production-ready protocol.

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Update mindmap to include GitHub MCP Registry for Case Studies section.
- **Case Studies Description**: Change from generic descriptions to detailed breakdown of seven full case studies.
- **Repository Structure**: Update section 10 to reflect full case study coverage with specific implementation details.
- **Changelog Integration**: Add September 26, 2025 entry wey document GitHub MCP Registry addition and case study improvements.
- **Date Updates**: Update footer timestamp to show latest revision (September 26, 2025).

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardize case study formatting and structure for all seven examples.
- **Comprehensive Coverage**: Case studies now dey cover enterprise, developer productivity, and ecosystem development scenarios.
- **Strategic Positioning**: Better focus on MCP as foundational platform for agentic system deployment.
- **Resource Integration**: Update extra resources to include GitHub MCP Registry link.

## September 15, 2025

### Advanced Topics Expansion - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - New Advanced Implementation Guide
- **README.md**: Full implementation guide for custom MCP transport mechanisms.
  - **Azure Event Grid Transport**: Full serverless event-driven transport implementation.
    - C#, TypeScript, and Python examples with Azure Functions integration.
    - Event-driven architecture patterns for scalable MCP solutions.
    - Webhook receivers and push-based message handling.
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation.
    - Real-time streaming capabilities for low-latency scenarios.
    - Partitioning strategies and checkpoint management.
    - Message batching and performance optimization.
  - **Enterprise Integration Patterns**: Production-ready architectural examples.
    - Distributed MCP processing across multiple Azure Functions.
    - Hybrid transport architectures combining multiple transport types.
    - Message durability, reliability, and error handling strategies.
  - **Security & Monitoring**: Azure Key Vault integration and observability patterns.
    - Managed identity authentication and least privilege access.
    - Application Insights telemetry and performance monitoring.
    - Circuit breakers and fault tolerance patterns.
  - **Testing Frameworks**: Full testing strategies for custom transports.
    - Unit testing with test doubles and mocking frameworks.
    - Integration testing with Azure Test Containers.
    - Performance and load testing considerations.

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Emerging AI Discipline
- **README.md**: Full exploration of context engineering as one new field.
  - **Core Principles**: Complete context sharing, action decision awareness, and context window management.
  - **MCP Protocol Alignment**: How MCP design dey address context engineering challenges.
    - Context window limitations and progressive loading strategies.
    - Relevance determination and dynamic context retrieval.
    - Multi-modal context handling and security considerations.
  - **Implementation Approaches**: Single-threaded vs. multi-agent architectures.
    - Context chunking and prioritization techniques.
    - Progressive context loading and compression strategies.
    - Layered context approaches and retrieval optimization.
  - **Measurement Framework**: New metrics for context effectiveness evaluation.
    - Input efficiency, performance, quality, and user experience considerations.
    - Experimental approaches to context optimization.
    - Failure analysis and improvement methodologies.

#### Curriculum Navigation Updates (README.md)
- **Enhanced Module Structure**: Update curriculum table to include new advanced topics.
  - Add Context Engineering (5.14) and Custom Transport (5.15) entries.
  - Consistent formatting and navigation links for all modules.
  - Update descriptions to reflect current content scope.

### Directory Structure Improvements
- **Naming Standardization**: Rename "mcp transport" to "mcp-transport" to match other advanced topic folders.
- **Content Organization**: All 05-AdvancedTopics folders now dey follow consistent naming pattern (mcp-[topic]).

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content dey reference current MCP Specification 2025-06-18.
- **Multi-Language Examples**: Full code examples for C#, TypeScript, and Python.
- **Enterprise Focus**: Production-ready patterns and Azure cloud integration dey everywhere.
- **Visual Documentation**: Mermaid diagrams for architecture and flow visualization.

## August 18, 2025

### Documentation Comprehensive Update - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Complete Modernization
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Full rewrite wey align with MCP Specification 2025-06-18.
  - **Mandatory Requirements**: Add clear MUST/MUST NOT requirements from official specification with visual indicators.
  - **12 Core Security Practices**: Restructure from 15-item list to full security domains.
    - Token Security & Authentication with external identity provider integration.
    - Session Management & Transport Security with cryptographic requirements.
    - AI-Specific Threat Protection with Microsoft Prompt Shields integration.
    - Access Control & Permissions with principle of least privilege.
    - Content Safety & Monitoring with Azure Content Safety integration.
    - Supply Chain Security with full component verification.
    - OAuth Security & Confused Deputy Prevention with PKCE implementation.
    - Incident Response & Recovery with automated capabilities.
    - Compliance & Governance with regulatory alignment.
    - Advanced Security Controls with zero trust architecture.
    - Microsoft Security Ecosystem Integration with full solutions.
    - Continuous Security Evolution with adaptive practices.
  - **Microsoft Security Solutions**: Better integration guidance for Prompt Shields, Azure Content Safety, Entra ID, and GitHub Advanced Security.
  - **Implementation Resources**: Categorize full resource links by Official MCP Documentation, Microsoft Security Solutions, Security Standards, and Implementation Guides.

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Full overhaul with enterprise-grade security framework.
  - **9 Comprehensive Security Domains**: Expand from basic controls to detailed enterprise framework.
    - Advanced Authentication & Authorization with Microsoft Entra ID integration.
    - Token Security & Anti-Passthrough Controls with full validation.
    - Session Security Controls with hijacking prevention.
    - AI-Specific Security Controls with prompt injection and tool poisoning prevention.
    - Confused Deputy Attack Prevention with OAuth proxy security.
    - Tool Execution Security with sandboxing and isolation.
    - Supply Chain Security Controls with dependency verification.
    - Monitoring & Detection Controls with SIEM integration.
    - Incident Response & Recovery with automated capabilities.
  - **Implementation Examples**: Add detailed YAML configuration blocks and code examples.
  - **Microsoft Solutions Integration**: Full coverage of Azure security services, GitHub Advanced Security, and enterprise identity management.
#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Rewrite am well for enterprise security setup
  - **Current Specification Alignment**: Update am to MCP Specification 2025-06-18 wey get mandatory security requirements
  - **Enhanced Authentication**: Microsoft Entra ID integration wey get full .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety setup wey get detailed Python examples
  - **Advanced Threat Mitigation**: Full implementation examples for
    - Confused Deputy Attack Prevention wey use PKCE and user consent validation
    - Token Passthrough Prevention wey use audience validation and secure token management
    - Session Hijacking Prevention wey use cryptographic binding and behavioral analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, and supply chain security
  - **Implementation Checklist**: Clear list of wetin be mandatory vs. recommended security controls wey dey show Microsoft security ecosystem benefits

### Documentation Quality & Standards Alignment
- **Specification References**: Update all references to current MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Add better integration guidance for all security documentation
- **Practical Implementation**: Add detailed code examples for .NET, Java, and Python wey follow enterprise patterns
- **Resource Organization**: Arrange official documentation, security standards, and implementation guides well
- **Visual Indicators**: Mark wetin be mandatory requirements vs. recommended practices clearly

#### Core Concepts (01-CoreConcepts/) - Complete Modernization
- **Protocol Version Update**: Update am to reference current MCP Specification 2025-06-18 wey dey use date-based versioning (YYYY-MM-DD format)
- **Architecture Refinement**: Make descriptions of Hosts, Clients, and Servers better to match current MCP architecture patterns
  - Hosts now dey defined as AI applications wey dey coordinate multiple MCP client connections
  - Clients dey described as protocol connectors wey dey maintain one-to-one server relationships
  - Servers dey enhanced with local vs. remote deployment scenarios
- **Primitive Restructuring**: Change server and client primitives completely
  - Server Primitives: Resources (data sources), Prompts (templates), Tools (executable functions) wey get detailed explanations and examples
  - Client Primitives: Sampling (LLM completions), Elicitation (user input), Logging (debugging/monitoring)
  - Update am with current discovery (`*/list`), retrieval (`*/get`), and execution (`*/call`) method patterns
- **Protocol Architecture**: Add two-layer architecture model
  - Data Layer: JSON-RPC 2.0 foundation wey get lifecycle management and primitives
  - Transport Layer: STDIO (local) and Streamable HTTP with SSE (remote) transport mechanisms
- **Security Framework**: Add full security principles wey include explicit user consent, data privacy protection, tool execution safety, and transport layer security
- **Communication Patterns**: Update protocol messages to show initialization, discovery, execution, and notification flows
- **Code Examples**: Refresh multi-language examples (.NET, Java, Python, JavaScript) to match current MCP SDK patterns

#### Security (02-Security/) - Comprehensive Security Overhaul  
- **Standards Alignment**: Full alignment with MCP Specification 2025-06-18 security requirements
- **Authentication Evolution**: Document how e don move from custom OAuth servers to external identity provider delegation (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Add better coverage of modern AI attack vectors
  - Detailed prompt injection attack scenarios wey get real-world examples
  - Tool poisoning mechanisms and "rug pull" attack patterns
  - Context window poisoning and model confusion attacks
- **Microsoft AI Security Solutions**: Full coverage of Microsoft security ecosystem
  - AI Prompt Shields wey get advanced detection, spotlighting, and delimiter techniques
  - Azure Content Safety integration patterns
  - GitHub Advanced Security for supply chain protection
- **Advanced Threat Mitigation**: Detailed security controls for
  - Session hijacking wey get MCP-specific attack scenarios and cryptographic session ID requirements
  - Confused deputy problems in MCP proxy scenarios wey need explicit consent requirements
  - Token passthrough vulnerabilities wey need mandatory validation controls
- **Supply Chain Security**: Expand AI supply chain coverage wey include foundation models, embeddings services, context providers, and third-party APIs
- **Foundation Security**: Add better integration with enterprise security patterns wey include zero trust architecture and Microsoft security ecosystem
- **Resource Organization**: Arrange resource links well by type (Official Docs, Standards, Research, Microsoft Solutions, Implementation Guides)

### Documentation Quality Improvements
- **Structured Learning Objectives**: Add better learning objectives wey get specific, actionable outcomes 
- **Cross-References**: Add links between related security and core concept topics
- **Current Information**: Update all date references and specification links to current standards
- **Implementation Guidance**: Add specific, actionable implementation guidelines for both sections

## July 16, 2025

### README and Navigation Improvements
- Redesign the curriculum navigation for README.md
- Replace `<details>` tags with table-based format wey dey more accessible
- Create alternative layout options for new "alternative_layouts" folder
- Add card-based, tabbed-style, and accordion-style navigation examples
- Update repository structure section to include all latest files
- Make "How to Use This Curriculum" section better with clear recommendations
- Update MCP specification links to point to correct URLs
- Add Context Engineering section (5.14) to the curriculum structure

### Study Guide Updates
- Revise the study guide well to match current repository structure
- Add new sections for MCP Clients and Tools, and Popular MCP Servers
- Update the Visual Curriculum Map to show all topics well
- Make descriptions of Advanced Topics better to cover all specialized areas
- Update Case Studies section to show real examples
- Add this full changelog

### Community Contributions (06-CommunityContributions/)
- Add detailed information about MCP servers for image generation
- Add full section on how to use Claude in VSCode
- Add Cline terminal client setup and usage instructions
- Update MCP client section to include all popular client options
- Make contribution examples better with more accurate code samples

### Advanced Topics (05-AdvancedTopics/)
- Arrange all specialized topic folders with consistent naming
- Add context engineering materials and examples
- Add Foundry agent integration documentation
- Make Entra ID security integration documentation better

## June 11, 2025

### Initial Creation
- Release first version of the MCP for Beginners curriculum
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
- Initialize the repository with basic folder structure
- Create README files for each major section
- Set up translation infrastructure
- Add image assets and diagrams

### Documentation
- Create initial README.md with curriculum overview
- Add CODE_OF_CONDUCT.md and SECURITY.md
- Set up SUPPORT.md with guidance for getting help
- Create preliminary study guide structure

## April 15, 2025

### Planning and Framework
- Start planning for MCP for Beginners curriculum
- Define learning objectives and target audience
- Outline 10-section structure of the curriculum
- Develop conceptual framework for examples and case studies
- Create initial prototype examples for key concepts

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say transleshion wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
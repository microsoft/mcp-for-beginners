# Changelog: MCP for Beginners Curriculum

This document serves as a record of all significant changes made to the Model Context Protocol (MCP) for Beginners curriculum. Changes are documented in reverse chronological order (newest changes first).

## July 29th, 2026

### New Module 08 Companion: Reliability Sidecars and Safe Retries

Added a vendor-neutral companion lesson for MCP tools that create real-world
effects, aligned with the final `2026-07-28` specification.

- **New**: The [reliability sidecar companion lesson][reliability-sidecar]
  uses one support-ticket story, two Mermaid diagrams, and a retry decision
  flow to explain stable operation keys, atomic duplicate admission,
  reconciliation, evidence, and the Tasks extension boundary.
- **New**: A standard-library Python and SQLite failure-injection exercise
  uses separate operation and ticket stores to demonstrate a response lost
  after an external effect commits. Six deterministic tests cover naive
  duplication, guarded restart recovery, payload conflicts, cached results,
  active claims, and concurrent duplicate admission.
- **Updated**: Module 08 now links the companion lesson, identifies the
  final `2026-07-28` stateless request model, distinguishes OpenTelemetry
  observability from the deprecated MCP logging feature, and limits its
  generic retry example to read-only operations.
- **Optional**: The lesson maps its portable concepts to one tagged community
  implementation without making the hosted service or a network call part of
  the exercise.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## July 2nd, 2026

### New Lesson: The 2026-07-28 MCP Specification Release Candidate

Added coverage of the upcoming `2026-07-28` MCP specification release candidate (announced May 21, 2026; final release scheduled July 28, 2026), summarized from the [official announcement blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). The curriculum's baseline remains **MCP Specification 2025-11-25** until the new version ships, so this is presented as forward-looking guidance rather than a rewrite of existing lessons.

- **New**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — a full lesson covering the stateless protocol core (removal of the `initialize` handshake and `Mcp-Session-Id`), the new `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context in `_meta`, the formal Extensions framework (MCP Apps and the new Tasks extension), six authorization-hardening SEPs, the deprecation of Roots/Sampling/Logging, and the move to full JSON Schema 2020-12 for tool schemas.
- **Updated** with forward-looking callouts linking to the new lesson:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protocol version note, Sampling/Roots/Logging/Tasks sections, and "What's next"
  - [02-Security/README.md](./02-Security/README.md): authorization hardening callout
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport callout
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling deprecation callout
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging deprecation and Tasks extension callout
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing callout
  - [README.md](./README.md): "Looking ahead" note in the specification section and a new `1.1` entry in the curriculum module table
  - [study_guide.md](./study_guide.md): forward-looking bullet under the Core Concepts overview and a dated addendum note
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): callout on the `mcp-session-id` transport map ahead of the stateless request model
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): module overview callout on Root Contexts/Sampling deprecations and the Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): authorization hardening callout

## June 24th, 2026

### New Lesson: Using MCP in Copilot app

- [Tooling section](./12-tooling/README.md) Added tooling section.
- [MCP in Copilot app](./12-tooling/01-copilot-app/README.md)

## June 16, 2026

### MCP Specification Alignment & Sample Validation

Validated the curriculum against the current **MCP Specification 2025-11-25** and the latest official SDKs, then corrected the remaining stale specification references and confirmed the core samples still build and run.

#### Specification Version Corrections (2025-06-18 / 2025-03-26 → 2025-11-25)

Updated English content where it still claimed an older spec revision was the *current/latest* standard, and repointed links to the canonical `modelcontextprotocol.io` spec paths:
- **05-AdvancedTopics/mcp-security/README.md**: Updated the "Current Standard" banner, introduction, core security principles heading, mandatory requirements heading, Microsoft Entra ID section, References & Resources links, and closing security notice (8 references) to 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Updated the Additional Resources spec link and the "Current Standard" banner to 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Replaced the outdated `2025-03-26` security-and-trust link with the current 2025-11-25 security best practices page
- **03-GettingStarted/14-sampling/README.md**: Updated the official sampling docs link to 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Updated the present-tense "current MCP specification" reference and the Additional Resources spec link to 2025-11-25 (historical SSE-deprecation notes left intact for accuracy)

#### Sample Validation Against Current SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolved `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` passed with no type errors — existing `McpServer`/`StdioServerTransport` APIs remain valid
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validated in an isolated `.venv` with `mcp[cli]` (1.27.2); `py_compile` passed and `FastMCP.list_tools()` correctly returned the `add` and `subtract` tools
- Confirmed all sample `@modelcontextprotocol/sdk` version ranges (`>=1.26.0` / `^1.26.0` / `^1.27.0`) resolve cleanly to the current `1.29.0` with no breaking API changes

#### Dependency Pin Alignment (closing version gaps)

Bumped outdated SDK pins so every sample tracks the current MCP release, matching the repo-wide convention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Bumped `@modelcontextprotocol/sdk` from `^1.8.0` → `>=1.26.0` and updated the stale `"updated for MCP 2025-06-18"` package description to `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** and **lab4/code/github_mcp_server/pyproject.toml**: Bumped the exact pin `mcp==1.23.0` → `mcp>=1.26.0`; regenerated both `uv.lock` files (`uv lock`) so the lockfiles resolve to the current `mcp 1.27.2` and stay in sync with the manifests

#### Curriculum Gap Analysis — Latest Spec Feature Coverage

Verified the curriculum already covers all primitives introduced/expanded in MCP 2025-11-25, so no content gaps remain:
- **Sampling**: Lesson 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. URL mode)**: Documented in 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documented in 00-Introduction, 01-CoreConcepts, and 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimental, long-running operations)**: Documented in 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Documented in 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features

### Security Hardening & Dependency Vulnerability Remediation

Ran a full security pass across every dependency manifest and the sample source code, then remediated all reported npm advisories and one code-level finding. After remediation, `npm audit` reports **0 vulnerabilities** in every audited directory.

#### npm Dependency Vulnerabilities (transitive) — Fixed

Audited all 15 committed `package-lock.json` files. Vulnerabilities were limited to transitive dependencies pulled in by the MCP Inspector dev tool, the OpenAI client, and the MCP SDK; all are now resolved without breaking the samples:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** and **lab3/code/weather_mcp/inspector**: Bumped `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), which cleared the bundled `ajv`, `brace-expansion`, `diff`, `path-to-regexp` and `ws` advisories. Added an npm `overrides` entry forcing the patched `shell-quote@1.8.4` to eliminate the remaining critical advisory carried by `concurrently`; regenerated both lockfiles (now 0 vulnerabilities)
- **03-GettingStarted/samples/typescript**: `npm audit fix` updated the transitive `qs` (moderate) to a patched release
- **03-GettingStarted/samples/javascript**: `npm audit fix` updated the transitive `hono` (moderate) to a patched release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` updated the transitive `form-data` (high) to a patched release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generated the missing `package-lock.json` so the project is reproducible and auditable (0 vulnerabilities)

#### Code-Level Security Fix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Removed `shell=True` from the `open_in_vscode` tool. The previous `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` allowed shell metacharacters in a folder path to be interpreted by `cmd.exe` (command-injection vector). It now launches the resolved `Code.exe` directly with the folder as an argument — no shell — which is functionally equivalent and safe

#### Python Dependency Audit

- Audited every Python requirements set with `pip-audit`. `05-AdvancedTopics` and `03-GettingStarted/samples/python` reported **no known vulnerabilities** (their `mcp` / `httpx` / `pydantic` / `python-dotenv` ranges resolve to current patched releases)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flagged the transitive dependency **`werkzeug` 3.1.1** with three `safe_join` Windows device-name DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, and `CVE-2026-27199` (all fixed in 3.1.6). Added an explicit security pin `werkzeug>=3.1.6` so the patched release is resolved; verified the constraint resolves cleanly with the `chainlit` / `mcp` / `semantic-kernel` stack

### Product Name Rebranding

Updated all curriculum content to reflect Microsoft's product rebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Updated Discord community link
- **AGENTS.md**: Updated Discord server reference
- **README.md**: Updated technology ecosystem references
- **study_guide.md**: Updated case study references
- **05-AdvancedTopics/README.md**: Updated Module 5.13 title and description
- **05-AdvancedTopics/mcp-integration/README.md**: Updated section header and description
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Full module title and content update
- **05-AdvancedTopics/mcp-security-entra/README.md**: Updated cross-reference link
- **07-LessonsfromEarlyAdoption/README.md**: Updated case study references
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Updated Section 9 header, badges, and capabilities
- **08-BestPractices/README.md**: Updated Discord community link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Updated Discord channel reference
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Updated model deployment reference
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Updated AI Services table
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Updated resource references

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Updated main curriculum references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Updated module title, overview, and all module headers
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Updated title, learning objectives, setup instructions, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Updated title, learning objectives, MCP hosts table, and cross-references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Updated title, badges, prerequisites, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Updated Agent Builder references and feedback link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Updated prerequisites and extension references

---

## April 11, 2026

### New Lesson, Documentation Fixes, and Dependency Updates

#### New Curriculum Content Added

**Module 05 - Advanced Topics**
- **Lesson 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): New comprehensive guide covering the adversarial debate pattern for multi-agent systems
  - Mermaid architecture diagram: two agents → shared MCP server → debate transcript → judge → verdict
  - Shared MCP tool server (`web_search` + `run_python`) implemented in Python and TypeScript
  - Opposing system prompts (FOR / AGAINST / Judge) with explicit tool-use requirements
  - Debate orchestrator in Python, TypeScript, and C# managing rounds and routing arguments
  - MCP `ClientSession` wiring for the orchestrator to real tool calls
  - Use-case table (hallucination detection, threat modeling, API design review, factual verification, tech selection)
  - Security considerations: sandboxed execution, tool-call validation, rate limiting, audit logging
  - Structured exercise with three practical scenarios (code review, architecture decision, content moderation)

#### Documentation Fixes

**Module 03 - Getting Started**
- **05-stdio-server/README.md**: Fixed incomplete TypeScript stdio server example — added missing transport instantiation (`new StdioServerTransport()`) and `server.connect(transport)` call to match the Python and .NET examples in the same section
- **14-sampling/README.md**: Fixed typo — corrected `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculum Updates

**Main README.md**
- Added entry 5.17 (Adversarial Multi-Agent Reasoning with MCP) to the curriculum table with a direct link to the new lesson

**05-AdvancedTopics/README.md**
- Added Lesson 5.17 row to the lessons table

**study_guide.md**
- Added Adversarial Multi-Agent Reasoning topic to the mind-map and prose description of Advanced Topics

#### Code and Security Fixes

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Security fix — command injection**: Replaced `execSync` shell interpolation with `execFile` + `promisify` in the TypeScript `run_python` tool, eliminating the command injection surface (LLM-controlled code is now passed as a literal argv element with no shell involvement)
- **MCP tool loop wiring**: Updated the Python debate orchestrator to use `AsyncAnthropic` client (replacing blocking sync `Anthropic`), pass a live `ClientSession` directly to each agent turn, fetch tool definitions via `session.list_tools()` each turn, and dispatch `tool_use` blocks via `session.call_tool()` in a loop until the model emits a final text response

#### Dependency Updates

- Bumped `hono` to 4.12.12 across multiple packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Bumped `@hono/node-server` from 1.19.11 to 1.19.13 in TypeScript packages
- Bumped `cryptography` from 46.0.5 to 46.0.7 in Python packages (10-StreamliningAIWorkflows labs 3 and 4)
- Bumped `lodash` from 4.17.23 to 4.18.1 in 10-StreamliningAIWorkflows inspector

#### Translations

- Synced translations for 48+ languages with the latest source changes (i18n update)

---

## February 5, 2026

### Repository-Wide Validation and Navigation Improvements

#### New Curriculum Content Added

**Module 03 - Getting Started**
- **12-mcp-hosts/README.md**: New comprehensive guide for setting up MCP hosts
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf configuration examples
  - JSON configuration templates for all major hosts
  - Transport types comparison table (stdio, SSE/HTTP, WebSocket)
  - Troubleshooting common connection issues
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
- **mcp-protocol-features/README.md**: New protocol features deep dive
  - Progress notifications implementation
  - Request cancellation patterns
  - Resource templates with URI patterns
  - Server lifecycle management
  - Logging level control
  - Error handling patterns with JSON-RPC codes

#### Navigation Fixes (24+ files updated)

**Main Module READMEs**
 Now links to both first lesson AND next module

**02-Security Sub-files**
- All 5 supplementary security documents now have "What's Next" navigation:

**09-CaseStudy Files**
- All case study files now have sequential navigation:

**10-StreamliningAI Labs**
Added What's Next section to Module 10 overview and Module 11

#### Code and Content Fixes

**SDK and Dependency Updates**
Fixed empty openai version to `^4.95.0`
Updated SDK from `^1.8.0` to `>=1.26.0`
Updated mcp version pins to `>=1.26.0`

**Code Fixes**
Fixed invalid model `gpt-4o-mini` to `gpt-4.1-mini`

**Content Fixes**
Fixed broken link `READMEmd` → `README.md`, fixed curriculum header `Module 1-3` → `Module 0-3`, fixed case-sensitive path
Removed corrupted duplicate Case Study 5 content

**Beginner Guidance Improvements**
Added proper introduction, learning objectives, and prerequisites for beginners

#### Curriculum Updates

**Main README.md**
- Added entries 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) to curriculum table

**Module READMEs**
Added lessons 12 and 13 to lesson list
Added Practical Guides section with pagination link
Added lessons 5.15 (Custom Transport) and 5.16 (Protocol Features)

**study_guide.md**
- Updated mindmap with all new topics: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## Jan 28, 2026

### MCP Specification 2025-11-25 Compliance Review

#### Core Concepts Enhancement (01-CoreConcepts/)
- **New Client Primitive - Roots**: Added comprehensive documentation on the Roots client primitive, enabling servers to understand filesystem boundaries and access permissions
- **Tool Annotations**: Added documentation on tool behavioral annotations (`readOnlyHint`, `destructiveHint`) for better tool execution decisions
- **Tool Calling in Sampling**: Updated Sampling documentation to include `tools` and `toolChoice` parameters for model-driven tool invocation during sampling requests
- **URL Mode Elicitation**: Added documentation on URL-based elicitation for server-initiated external web interactions
- **Tasks (Experimental)**: Added new section documenting the experimental Tasks feature for durable execution wrappers and deferred result retrieval
- **Icons Support**: Noted that tools, resources, resource templates, and prompts can now include icons as additional metadata

#### Documentation Updates
- **README.md**: Added MCP Specification 2025-11-25 version reference and date-based versioning explanation
- **study_guide.md**: Updated curriculum map to include Tasks and Tool Annotations in Core Concepts section; updated document timestamp

#### Specification Compliance Verification
- **Protocol Version**: Verified all documentation references current MCP Specification 2025-11-25
- **Architecture Alignment**: Confirmed two-layer architecture (Data Layer + Transport Layer) documentation accuracy
- **Primitives Documentation**: Validated server primitives (Resources, Prompts, Tools) and client primitives (Sampling, Elicitation, Logging, Roots)
- **Transport Mechanisms**: Verified STDIO and Streamable HTTP transport documentation accuracy
- **Security Guidance**: Confirmed alignment with current MCP Security Best Practices documentation

#### Key MCP 2025-11-25 Features Documented
- **OpenID Connect Discovery**: Auth server discovery through OIDC
- **OAuth Client ID Metadata Documents**: Recommended client registration mechanism
- **JSON Schema 2020-12**: Default dialect for MCP schema definitions
- **SDK Tiering System**: Formalized requirements for SDK feature support and maintenance
- **Governance Structure**: Formalized Working Groups and Interest Groups in MCP governance

### Security Documentation Major Update (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **New Hands-On Training Resource**: Added comprehensive integration with the [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) throughout all security documentation
- **Expedition Route Coverage**: Documented the complete camp-to-camp progression from Base Camp to Summit
- **OWASP Alignment**: All security guidance now maps to OWASP MCP Azure Security Guide risks

#### OWASP MCP Top 10 Integration
- **New Section**: Added OWASP MCP Top 10 Security Risks table with Azure mitigations to main Security README
- **Risk-Based Documentation**: Updated mcp-security-controls-2025.md with OWASP MCP risk references for each security domain
- **Reference Architecture**: Linked to OWASP MCP Azure Security Guide reference architecture and implementation patterns

#### Updated Security Files
- **README.md**: Added Sherpa Workshop overview, expedition route table, OWASP MCP Top 10 risks summary, and hands-on training section
- **mcp-security-controls-2025.md**: Updated header to February 2026, added OWASP risk references (MCP01-MCP08), fixed spec version inconsistency
- **mcp-security-best-practices-2025.md**: Added Sherpa and OWASP resources section, updated timestamp
- **mcp-best-practices.md**: Added hands-on training section with Sherpa and OWASP links
- **azure-content-safety-implementation.md**: Added OWASP MCP06 reference, Sherpa Camp 3 alignment, and additional resources section

#### New Resource Links Added
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individual OWASP MCP risk pages (MCP01-MCP10)

### Curriculum-Wide MCP Specification 2025-11-25 Alignment

#### Module 03 - Getting Started
- **SDK Documentation**: Added Go SDK to official SDK list; updated all SDK references to align with MCP Specification 2025-11-25
- **Transport Clarification**: Updated STDIO and HTTP Streaming transport descriptions with explicit spec references

#### Module 04 - Practical Implementation
- **SDK Updates**: Added Go SDK; updated SDK list with specification version reference
- **Authorization Spec**: Updated MCP Authorization specification link to current 2025-11-25 version

#### Module 05 - Advanced Topics
- **New Features**: Added note about new MCP Specification 2025-11-25 features (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Security Resources**: Added OWASP MCP Top 10 and Sherpa workshop links to additional references

#### Module 06 - Community Contributions
- **SDK List**: Added Swift and Rust SDKs; updated specification link to 2025-11-25
- **Spec Reference**: Updated MCP Specification link to direct specification URL

#### Module 07 - Lessons from Early Adoption
- **Resource Updates**: Added MCP Specification 2025-11-25 link and OWASP MCP Top 10 to additional resources

#### Module 08 - Best Practices
- **Spec Version**: Updated MCP Specification reference to 2025-11-25
- **Security Resources**: Added OWASP MCP Top 10 and Sherpa workshop to additional references

#### Module 10 - Streamlining AI Workflows
- **Badge Update**: Changed MCP version badge from SDK version (1.9.3) to specification version (2025-11-25)
- **Resource Links**: Updated MCP Specification link; added OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec Reference**: Updated MCP Specification link to 2025-11-25 version
- **Security Resources**: Added OWASP MCP Top 10 to official resources

## December 18, 2025

### Security Documentation Update - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specification Version Update
- **Protocol Version Update**: Updated to reference latest MCP Specification 2025-11-25 (released November 25, 2025)
  - Updated all specification version references from 2025-06-18 to 2025-11-25
  - Updated document date references from August 18, 2025 to December 18, 2025
  - Verified all specification URLs point to current documentation
- **Content Validation**: Comprehensive validation of security best practices against latest standards
  - **Microsoft Security Solutions**: Verified current terminology and links for Prompt Shields (previously "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, and Azure Key Vault
  - **OAuth 2.1 Security**: Confirmed alignment with latest OAuth security best practices
  - **OWASP Standards**: Validated OWASP Top 10 for LLMs references remain current
  - **Azure Services**: Verified all Microsoft Azure documentation links and best practices
- **Standards Alignment**: All referenced security standards confirmed current
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
- **Specification Compliance**: Ensured all mandatory MCP security requirements (MUST/MUST NOT) align with latest specification
- **Resource Currency**: Verified all external links to Microsoft documentation, security standards, and implementation guides
- **Best Practices Coverage**: Confirmed comprehensive coverage of authentication, authorization, AI-specific threats, supply chain security, and enterprise patterns

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: Introduced a comprehensive guide to advanced MCP server usage, covering both regular and low-level server architectures.
  - **Regular vs. Low-Level Server**: Detailed comparison and code examples in Python and TypeScript for both approaches.
  - **Handler-Based Design**: Explanation of handler-based tool/resource/prompt management for scalable, flexible server implementations.
  - **Practical Patterns**: Real-world scenarios where low-level server patterns are beneficial for advanced features and architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide to implementing simple authentication in MCP servers.
  - **Auth Concepts**: Clear explanation of authentication vs. authorization, and credential handling.
  - **Basic Auth Implementation**: Middleware-based authentication patterns in Python (Starlette) and TypeScript (Express), with code samples.
  - **Progression to Advanced Security**: Guidance on starting with simple auth and advancing to OAuth 2.1 and RBAC, with references to advanced security modules.

These additions provide practical, hands-on guidance for building more robust, secure, and flexible MCP server implementations, bridging foundational concepts with advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: Added comprehensive hands-on curriculum for building production-ready MCP servers with PostgreSQL database integration
  - **Real-World Implementation**: Zava Retail analytics use case demonstrating enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: Systematically updated all README files in 11-MCPServerHandsOnLabs to use "Lab" terminology instead of "Module"
  - **Section Headers**: Updated "What This Module Covers" to "What This Lab Covers" across all 13 labs
  - **Content Description**: Changed "This module provides..." to "This lab provides..." throughout documentation
  - **Learning Objectives**: Updated "By the end of this module..." to "By the end of this lab..." 
  - **Navigation Links**: Converted all "Module XX:" references to "Lab XX:" in cross-references and navigation
  - **Completion Tracking**: Updated "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: Maintained Python module references in configuration files (e.g., `"module": "mcp_server.main"`)

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Added new "11. Database Integration Labs" section with comprehensive lab structure visualization
- **Repository Structure**: Updated from ten to eleven main sections with detailed 11-MCPServerHandsOnLabs description
- **Learning Path Guidance**: Enhanced navigation instructions to cover sections 00-11
- **Technology Coverage**: Added FastMCP, PostgreSQL, Azure services integration details
- **Learning Outcomes**: Emphasized production-ready server development, database integration patterns, and enterprise security

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Updated main README.md in 11-MCPServerHandsOnLabs to consistently use "Lab" structure
- **Learning Path Organization**: Clear progression from foundational concepts through advanced implementation to production deployment
- **Real-World Focus**: Emphasis on practical, hands-on learning with enterprise-grade patterns and technologies

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: Reinforced practical, lab-based approach throughout documentation
- **Enterprise Patterns Focus**: Highlighted production-ready implementations and enterprise security considerations
- **Technology Integration**: Comprehensive coverage of modern Azure services and AI integration patterns
- **Learning Progression**: Clear, structured path from basic concepts to production deployment

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Major expansion with comprehensive GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: New comprehensive case study examining GitHub's MCP Registry launch in September 2025
    - **Problem Analysis**: Detailed examination of fragmented MCP server discovery and deployment challenges
    - **Solution Architecture**: GitHub's centralized registry approach with one-click VS Code installation
    - **Business Impact**: Measurable improvements in developer onboarding and productivity
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability
    - **Ecosystem Development**: Positioning as foundational platform for agentic integration
  - **Enhanced Case Study Structure**: Updated all seven case studies with consistent formatting and comprehensive descriptions
    - Azure AI Travel Agents: Multi-agent orchestration emphasis
    - Azure DevOps Integration: Workflow automation focus
    - Real-Time Documentation Retrieval: Python console client implementation
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code and GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Ecosystem development and community platform
  - **Comprehensive Conclusion**: Rewritten conclusion section highlighting seven case studies spanning multiple MCP implementation dimensions
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications categorization
    - Enhanced insights into architectural patterns, implementation strategies, and best practices
    - Emphasis on MCP as mature, production-ready protocol

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Updated mindmap to include GitHub MCP Registry in Case Studies section
- **Case Studies Description**: Enhanced from generic descriptions to detailed breakdown of seven comprehensive case studies
- **Repository Structure**: Updated section 10 to reflect comprehensive case study coverage with specific implementation details
- **Changelog Integration**: Added September 26, 2025 entry documenting GitHub MCP Registry addition and case study enhancements
- **Date Updates**: Updated footer timestamp to reflect latest revision (September 26, 2025)

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardized case study formatting and structure across all seven examples
- **Comprehensive Coverage**: Case studies now span enterprise, developer productivity, and ecosystem development scenarios
- **Strategic Positioning**: Enhanced focus on MCP as foundational platform for agentic system deployment
- **Resource Integration**: Updated additional resources to include GitHub MCP Registry link

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
  - **MCP Protocol Alignment**: How MCP design addresses context engineering challenges
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
- **Enhanced Module Structure**: Updated curriculum table to include new advanced topics
  - Added Context Engineering (5.14) and Custom Transport (5.15) entries
  - Consistent formatting and navigation links across all modules
  - Updated descriptions to reflect current content scope

### Directory Structure Improvements
- **Naming Standardization**: Renamed "mcp transport" to "mcp-transport" for consistency with other advanced topic folders
- **Content Organization**: All 05-AdvancedTopics folders now follow consistent naming pattern (mcp-[topic])

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content references current MCP Specification 2025-06-18
- **Multi-Language Examples**: Comprehensive code examples in C#, TypeScript, and Python
- **Enterprise Focus**: Production-ready patterns and Azure cloud integration throughout
- **Visual Documentation**: Mermaid diagrams for architecture and flow visualization

## August 18, 2025

### Documentation Comprehensive Update - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Complete Modernization
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Complete rewrite aligned with MCP Specification 2025-06-18
  - **Mandatory Requirements**: Added explicit MUST/MUST NOT requirements from official specification with clear visual indicators
  - **12 Core Security Practices**: Restructured from 15-item list to comprehensive security domains
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
- **MCP-SECURITY-CONTROLS-2025.md**: Complete overhaul with enterprise-grade security framework
  - **9 Comprehensive Security Domains**: Expanded from basic controls to detailed enterprise framework
    - Advanced Authentication & Authorization with Microsoft Entra ID integration
    - Token Security & Anti-Passthrough Controls with comprehensive validation
    - Session Security Controls with hijacking prevention
    - AI-Specific Security Controls with prompt injection and tool poisoning prevention
    - Confused Deputy Attack Prevention with OAuth proxy security
    - Tool Execution Security with sandboxing and isolation
    - Supply Chain Security Controls with dependency verification
    - Monitoring & Detection Controls with SIEM integration
    - Incident Response & Recovery with automated capabilities
  - **Implementation Examples**: Added detailed YAML configuration blocks and code examples
  - **Microsoft Solutions Integration**: Comprehensive coverage of Azure security services, GitHub Advanced Security, and enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Complete rewrite for enterprise security implementation
  - **Current Specification Alignment**: Updated to MCP Specification 2025-06-18 with mandatory security requirements
  - **Enhanced Authentication**: Microsoft Entra ID integration with comprehensive .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety implementation with detailed Python examples
  - **Advanced Threat Mitigation**: Comprehensive implementation examples for
    - Confused Deputy Attack Prevention with PKCE and user consent validation
    - Token Passthrough Prevention with audience validation and secure token management
    - Session Hijacking Prevention with cryptographic binding and behavioral analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, and supply chain security
  - **Implementation Checklist**: Clear mandatory vs. recommended security controls with Microsoft security ecosystem benefits

### Documentation Quality & Standards Alignment
- **Specification References**: Updated all references to current MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Enhanced integration guidance throughout all security documentation
- **Practical Implementation**: Added detailed code examples in .NET, Java, and Python with enterprise patterns
- **Resource Organization**: Comprehensive categorization of official documentation, security standards, and implementation guides
- **Visual Indicators**: Clear marking of mandatory requirements vs. recommended practices


#### Core Concepts (01-CoreConcepts/) - Complete Modernization
- **Protocol Version Update**: Updated to reference current MCP Specification 2025-06-18 with date-based versioning (YYYY-MM-DD format)
- **Architecture Refinement**: Enhanced descriptions of Hosts, Clients, and Servers to reflect current MCP architecture patterns
  - Hosts now clearly defined as AI applications coordinating multiple MCP client connections
  - Clients described as protocol connectors maintaining one-to-one server relationships
  - Servers enhanced with local vs. remote deployment scenarios
- **Primitive Restructuring**: Complete overhaul of server and client primitives
  - Server Primitives: Resources (data sources), Prompts (templates), Tools (executable functions) with detailed explanations and examples
  - Client Primitives: Sampling (LLM completions), Elicitation (user input), Logging (debugging/monitoring)
  - Updated with current discovery (`*/list`), retrieval (`*/get`), and execution (`*/call`) method patterns
- **Protocol Architecture**: Introduced two-layer architecture model
  - Data Layer: JSON-RPC 2.0 foundation with lifecycle management and primitives
  - Transport Layer: STDIO (local) and Streamable HTTP with SSE (remote) transport mechanisms
- **Security Framework**: Comprehensive security principles including explicit user consent, data privacy protection, tool execution safety, and transport layer security
- **Communication Patterns**: Updated protocol messages to show initialization, discovery, execution, and notification flows
- **Code Examples**: Refreshed multi-language examples (.NET, Java, Python, JavaScript) to reflect current MCP SDK patterns

#### Security (02-Security/) - Comprehensive Security Overhaul  
- **Standards Alignment**: Full alignment with MCP Specification 2025-06-18 security requirements
- **Authentication Evolution**: Documented evolution from custom OAuth servers to external identity provider delegation (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Enhanced coverage of modern AI attack vectors
  - Detailed prompt injection attack scenarios with real-world examples
  - Tool poisoning mechanisms and "rug pull" attack patterns
  - Context window poisoning and model confusion attacks
- **Microsoft AI Security Solutions**: Comprehensive coverage of Microsoft security ecosystem
  - AI Prompt Shields with advanced detection, spotlighting, and delimiter techniques
  - Azure Content Safety integration patterns
  - GitHub Advanced Security for supply chain protection
- **Advanced Threat Mitigation**: Detailed security controls for
  - Session hijacking with MCP-specific attack scenarios and cryptographic session ID requirements
  - Confused deputy problems in MCP proxy scenarios with explicit consent requirements
  - Token passthrough vulnerabilities with mandatory validation controls
- **Supply Chain Security**: Expanded AI supply chain coverage including foundation models, embeddings services, context providers, and third-party APIs
- **Foundation Security**: Enhanced integration with enterprise security patterns including zero trust architecture and Microsoft security ecosystem
- **Resource Organization**: Categorized comprehensive resource links by type (Official Docs, Standards, Research, Microsoft Solutions, Implementation Guides)

### Documentation Quality Improvements
- **Structured Learning Objectives**: Enhanced learning objectives with specific, actionable outcomes 
- **Cross-References**: Added links between related security and core concept topics
- **Current Information**: Updated all date references and specification links to current standards
- **Implementation Guidance**: Added specific, actionable implementation guidelines throughout both sections

## July 16, 2025

### README and Navigation Improvements
- Completely redesigned the curriculum navigation in README.md
- Replaced `<details>` tags with more accessible table-based format
- Created alternative layout options in new "alternative_layouts" folder
- Added card-based, tabbed-style, and accordion-style navigation examples
- Updated repository structure section to include all latest files
- Enhanced "How to Use This Curriculum" section with clear recommendations
- Updated MCP specification links to point to correct URLs
- Added Context Engineering section (5.14) to the curriculum structure

### Study Guide Updates
- Completely revised the study guide to align with current repository structure
- Added new sections for MCP Clients and Tools, and Popular MCP Servers
- Updated the Visual Curriculum Map to accurately reflect all topics
- Enhanced descriptions of Advanced Topics to cover all specialized areas
- Updated Case Studies section to reflect actual examples
- Added this comprehensive changelog

### Community Contributions (06-CommunityContributions/)
- Added detailed information about MCP servers for image generation
- Added comprehensive section on using Claude in VSCode
- Added Cline terminal client setup and usage instructions
- Updated MCP client section to include all popular client options
- Enhanced contribution examples with more accurate code samples

### Advanced Topics (05-AdvancedTopics/)
- Organized all specialized topic folders with consistent naming
- Added context engineering materials and examples
- Added Foundry agent integration documentation
- Enhanced Entra ID security integration documentation

## June 11, 2025

### Initial Creation
- Released first version of the MCP for Beginners curriculum
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
- Initialized the repository with basic folder structure
- Created README files for each major section
- Set up translation infrastructure
- Added image assets and diagrams

### Documentation
- Created initial README.md with curriculum overview
- Added CODE_OF_CONDUCT.md and SECURITY.md
- Set up SUPPORT.md with guidance for getting help
- Created preliminary study guide structure

## April 15, 2025

### Planning and Framework
- Initial planning for MCP for Beginners curriculum
- Defined learning objectives and target audience
- Outlined 10-section structure of the curriculum
- Developed conceptual framework for examples and case studies
- Created initial prototype examples for key concepts

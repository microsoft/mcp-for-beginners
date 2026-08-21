# Changelog: MCP for Beginners Curriculum

Dis dokument na record of all important changes wey dem don make to Model Context Protocol (MCP) for Beginners curriculum. Dem dey document changes for reverse chronological order (newest changes first).

## July 29th, 2026

### New Module 08 Companion: Reliability Sidecars and Safe Retries

Add one vendor-neutral companion lesson for MCP tools wey dey create real-world
effects, wey align with the final `2026-07-28` specification.

- **New**: The [reliability sidecar companion lesson][reliability-sidecar]
  dey use one support-ticket story, two Mermaid diagrams, and one retry decision
  flow to explain stable operation keys, atomic duplicate admission,
  reconciliation, evidence, and the Tasks extension boundary.
- **New**: One standard-library Python and SQLite failure-injection exercise
  dey use separate operation and ticket stores to show how response fit lost
  after external effect commit. Six deterministic tests cover naive
  duplication, guarded restart recovery, payload conflicts, cached results,
  active claims, and concurrent duplicate admission.
- **Updated**: Module 08 now link the companion lesson, identify the
  final `2026-07-28` stateless request model, differentiate OpenTelemetry
  observability from the deprecated MCP logging feature, and limit its
  generic retry example to read-only operations.
- **Optional**: The lesson map its portable concepts to one tagged community
  implementation without making the hosted service or network call part of
  the exercise.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## July 2nd, 2026

### New Lesson: The 2026-07-28 MCP Specification Release Candidate

Added coverage of the upcoming `2026-07-28` MCP specification release candidate (wey dem announce May 21, 2026; final release scheduled July 28, 2026), summarized from the [official announcement blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). The curriculum baseline still remain **MCP Specification 2025-11-25** until the new version launch, so dis one na forward-looking guidance instead of rewrite for existing lessons.

- **New**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — complete lesson wey cover stateless protocol core (wey dem comot the `initialize` handshake and `Mcp-Session-Id`), the new `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context for `_meta`, the formal Extensions framework (MCP Apps and new Tasks extension), six authorization-hardening SEPs, the deprecation of Roots/Sampling/Logging, and the move go full JSON Schema 2020-12 for tool schemas.
- **Updated** with forward-looking callouts wey link to new lesson:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protocol version note, Sampling/Roots/Logging/Tasks sections, and "What's next"
  - [02-Security/README.md](./02-Security/README.md): authorization hardening callout
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport callout
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling deprecation callout
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging deprecation and Tasks extension callout
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing callout
  - [README.md](./README.md): "Looking ahead" note for the specification section and new `1.1` entry for curriculum module table
  - [study_guide.md](./study_guide.md): forward-looking bullet under Core Concepts overview and dated addendum note
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): callout on the `mcp-session-id` transport map ahead of stateless request model
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): module overview callout on Root Contexts/Sampling deprecations and Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): authorization hardening callout

## June 24th, 2026

### New Lesson: Using MCP in Copilot app

- [Tooling section](./12-tooling/README.md) Added tooling section.
- [MCP in Copilot app](./12-tooling/01-copilot-app/README.md)

## June 16, 2026

### MCP Specification Alignment & Sample Validation

We don validate the curriculum with the current **MCP Specification 2025-11-25** and the latest official SDKs, then we correct the remaining stale specification references and confirm say the core samples still fit build and run.

#### Specification Version Corrections (2025-06-18 / 2025-03-26 → 2025-11-25)

We update English content where e still dey talk say older spec revision na *current/latest* standard, and redirect links go the canonical `modelcontextprotocol.io` spec paths:
- **05-AdvancedTopics/mcp-security/README.md**: Update the "Current Standard" banner, introduction, core security principles heading, mandatory requirements heading, Microsoft Entra ID section, References & Resources links, and closing security notice (8 references) to 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Update the Additional Resources spec link and the "Current Standard" banner to 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Replace the outdated `2025-03-26` security-and-trust link with the current 2025-11-25 security best practices page
- **03-GettingStarted/14-sampling/README.md**: Update the official sampling docs link to 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Update the present-tense "current MCP specification" reference and the Additional Resources spec link to 2025-11-25 (historical SSE-deprecation notes stay intact for accuracy)

#### Sample Validation Against Current SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolve `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` pass with no type errors — existing `McpServer`/`StdioServerTransport` APIs still valid
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validate for isolated `.venv` with `mcp[cli]` (1.27.2); `py_compile` pass and `FastMCP.list_tools()` return correct `add` and `subtract` tools
- Confirm say all sample `@modelcontextprotocol/sdk` version ranges (`>=1.26.0` / `^1.26.0` / `^1.27.0`) resolve cleanly to current `1.29.0` with no breaking API changes

#### Dependency Pin Alignment (to close version gaps)

We bump outdated SDK pins so every sample dey track current MCP release, match the repo-wide convention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Bump `@modelcontextprotocol/sdk` from `^1.8.0` to `>=1.26.0` and update the stale `"updated for MCP 2025-06-18"` package description to `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** and **lab4/code/github_mcp_server/pyproject.toml**: Bump exact pin `mcp==1.23.0` to `mcp>=1.26.0`; regenerate both `uv.lock` files (`uv lock`) so the lockfiles resolve to current `mcp 1.27.2` and stay in sync with manifests

#### Curriculum Gap Analysis — Latest Spec Feature Coverage

We verify the curriculum already cover all primitives wey MCP 2025-11-25 introduce or expand, so no content gaps remain:
- **Sampling**: Lesson 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (including URL mode)**: Documented for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documented for 00-Introduction, 01-CoreConcepts, and 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimental, long-running operations)**: Documented for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Documented for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features

### Security Hardening & Dependency Vulnerability Remediation

We run full security pass across every dependency manifest and sample source code, then fix all reported npm advisories and one code-level finding. After fix, `npm audit` dey report **0 vulnerabilities** for every audited directory.

#### npm Dependency Vulnerabilities (transitive) — Fixed

We audit all 15 committed `package-lock.json` files. Vulnerabilities limited to transitive dependencies wey MCP Inspector dev tool, OpenAI client, and MCP SDK bring, all now fix without breaking samples:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** and **lab3/code/weather_mcp/inspector**: Bump `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` to `0.22.0`), wey clear bundled `ajv`, `brace-expansion`, `diff`, `path-to-regexp`, and `ws` advisories. Add npm `overrides` entry wey force patched `shell-quote@1.8.4` to fix remaining critical advisory carried by `concurrently`; regenerate both lockfiles (now 0 vulnerabilities)
- **03-GettingStarted/samples/typescript**: `npm audit fix` update transitive `qs` (moderate) to patched release
- **03-GettingStarted/samples/javascript**: `npm audit fix` update transitive `hono` (moderate) to patched release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` update transitive `form-data` (high) to patched release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generate missing `package-lock.json` so project fit reproduce and audit (0 vulnerabilities)

#### Code-Level Security Fix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Remove `shell=True` from `open_in_vscode` tool. Previous `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` allow shell metacharacters for folder path to be interpreted by `cmd.exe` (command-injection vector). E now dey launch resolved `Code.exe` directly with folder as argument — no shell — which functionally na same and safe

#### Python Dependency Audit

- Audit every Python requirements set with `pip-audit`. `05-AdvancedTopics` and `03-GettingStarted/samples/python` report **no known vulnerabilities** (their `mcp` / `httpx` / `pydantic` / `python-dotenv` ranges resolve to current patched releases)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flag the transitive dependency **`werkzeug` 3.1.1** with three `safe_join` Windows device-name DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, and `CVE-2026-27199` (all fix for 3.1.6). Add explicit security pin `werkzeug>=3.1.6` so patched release resolve; verify constraint resolve cleanly with `chainlit` / `mcp` / `semantic-kernel` stack

### Product Name Rebranding

Update all curriculum content to reflect Microsoft's product rebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Update Discord community link

- **AGENTS.md**: Updet Discord server reference
- **README.md**: Updet technology ecosystem references
- **study_guide.md**: Updet case study references
- **05-AdvancedTopics/README.md**: Updet Module 5.13 title and description
- **05-AdvancedTopics/mcp-integration/README.md**: Updet section header and description
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Full module title and content update
- **05-AdvancedTopics/mcp-security-entra/README.md**: Updet cross-reference link
- **07-LessonsfromEarlyAdoption/README.md**: Updet case study references
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Updet Section 9 header, badges, and capabilities
- **08-BestPractices/README.md**: Updet Discord community link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Updet Discord channel reference
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Updet model deployment reference
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Updet AI Services table
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Updet resource references

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Updet main curriculum references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Updet module title, overview, and all module headers
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Updet title, learning objectives, setup instructions, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Updet title, learning objectives, MCP hosts table, and cross-references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Updet title, badges, prerequisites, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Updet Agent Builder references and feedback link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Updet prerequisites and extension references

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
- All 5 supplementary security documents now get "What's Next" navigation:

**09-CaseStudy Files**
- All case study files now get sequential navigation:

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
- Updet mindmap with all new topics: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## Jan 28, 2026

### MCP Specification 2025-11-25 Compliance Review

#### Core Concepts Enhancement (01-CoreConcepts/)
- **New Client Primitive - Roots**: Added comprehensive documentation on the Roots client primitive, enabling servers to understand filesystem boundaries and access permissions
- **Tool Annotations**: Added documentation on tool behavioral annotations (`readOnlyHint`, `destructiveHint`) for better tool execution decisions
- **Tool Calling in Sampling**: Updet Sampling documentation to include `tools` and `toolChoice` parameters for model-driven tool invocation during sampling requests
- **URL Mode Elicitation**: Added documentation on URL-based elicitation for server-initiated external web interactions
- **Tasks (Experimental)**: Added new section documenting the experimental Tasks feature for durable execution wrappers and deferred result retrieval
- **Icons Support**: Noted sey tools, resources, resource templates, and prompts fit now include icons as additional metadata

#### Documentation Updates
- **README.md**: Added MCP Specification 2025-11-25 version reference and date-based versioning explanation
- **study_guide.md**: Updet curriculum map to include Tasks and Tool Annotations in Core Concepts section; updet document timestamp

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
- **OWASP Alignment**: All security guidance now dey map to OWASP MCP Azure Security Guide risks

#### OWASP MCP Top 10 Integration
- **New Section**: Added OWASP MCP Top 10 Security Risks table with Azure mitigations to main Security README
- **Risk-Based Documentation**: Updet mcp-security-controls-2025.md with OWASP MCP risk references for each security domain
- **Reference Architecture**: Linked to OWASP MCP Azure Security Guide reference architecture and implementation patterns

#### Updated Security Files
- **README.md**: Added Sherpa Workshop overview, expedition route table, OWASP MCP Top 10 risks summary, and hands-on training section
- **mcp-security-controls-2025.md**: Updet header to February 2026, added OWASP risk references (MCP01-MCP08), fixed spec version inconsistency
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

  - **MCP Protocol Alignment**: How MCP design take handle context engineering wahala dem
    - Context window limit dem and progressive loading waya dem
    - How to sabi relevance plus dynamic context wey dem fit find
    - How dem dey handle multi-modal context plus security matter dem
  - **Implementation Approaches**: Single-threaded against multi-agent architecture dem
    - How dem dey chunk context and how dem dey put for priority
    - Progressive context loading plus how to compress am
    - Layered context method and how to make retrieval better
  - **Measurement Framework**: New metrics wey dem dey use check context effectiveness
    - Input efficiency, performance, quality, plus user experience matter dem
    - Experimental way of how to make context better
    - How to check failure and ways to improve am

#### Curriculum Navigation Updates (README.md)
- **Enhanced Module Structure**: Updated curriculum table to add new advanced topics
  - Added Context Engineering (5.14) and Custom Transport (5.15) entries
  - Consistent formatting plus navigation links for all modules
  - Updated descriptions to show current content scope

### Directory Structure Improvements
- **Naming Standardization**: Change "mcp transport" to "mcp-transport" make e consistent wit other advanced topic folders
- **Content Organization**: All 05-AdvancedTopics folders now get consistent naming pattern (mcp-[topic])

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content make e follow current MCP Specification 2025-06-18
- **Multi-Language Examples**: Complete code examples for C#, TypeScript, and Python
- **Enterprise Focus**: Patterns wey ready for production plus Azure cloud integration everywhere
- **Visual Documentation**: Mermaid diagrams for architecture plus flow pictures

## August 18, 2025

### Documentation Comprehensive Update - MCP 2025-06-18 Standards

#### MCP Security Best Practices (02-Security/) - Complete Modernization
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Rewrite complete to match MCP Specification 2025-06-18
  - **Mandatory Requirements**: Add clear MUST/MUST NOT requirements from official specification with sharp visual signs
  - **12 Core Security Practices**: Change am from 15-item list to full security areas
    - Token Security & Authentication with external identity provider join
    - Session Management & Transport Security wit cryptographic requirement dem
    - AI-Specific Threat Protection wit Microsoft Prompt Shields join
    - Access Control & Permissions wit principle say make person get only wetin e need
    - Content Safety & Monitoring wit Azure Content Safety join
    - Supply Chain Security wit thorough component checking
    - OAuth Security & Confused Deputy Prevention wit PKCE way dem use
    - Incident Response & Recovery wit automated things
    - Compliance & Governance wit how e suppose for regulations
    - Advanced Security Controls wit zero trust structure
    - Microsoft Security Ecosystem Integration wit all solution dem
    - Continuous Security Evolution wit flexible methods
  - **Microsoft Security Solutions**: Better integration guide for Prompt Shields, Azure Content Safety, Entra ID, and GitHub Advanced Security
  - **Implementation Resources**: Sort comprehensive resource links by Official MCP Documentation, Microsoft Security Solutions, Security Standards, and Implementation Guides

#### Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Total overhaul wit enterprise-level security framework
  - **9 Comprehensive Security Domains**: Expand from basic controls to detailed enterprise framework
    - Advanced Authentication & Authorization wit Microsoft Entra ID join
    - Token Security & Anti-Passthrough Controls wit thorough checking
    - Session Security Controls wit how to stop hijacking
    - AI-Specific Security Controls wit prompt injection and tool poisoning prevent
    - Confused Deputy Attack Prevention wit OAuth proxy security
    - Tool Execution Security wit sandboxing and separation
    - Supply Chain Security Controls wit dependency checking
    - Monitoring & Detection Controls wit SIEM integration
    - Incident Response & Recovery wit automated capabilities
  - **Implementation Examples**: Add detailed YAML configuration blocks and code examples
  - **Microsoft Solutions Integration**: Full coverage of Azure security services, GitHub Advanced Security, and enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Rewrite complete for enterprise security implementation
  - **Current Specification Alignment**: Update to MCP Specification 2025-06-18 with mandatory security requests
  - **Enhanced Authentication**: Microsoft Entra ID join wit full .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety implementation wit detailed Python examples
  - **Advanced Threat Mitigation**: Full implementation examples for
    - Confused Deputy Attack Prevention wit PKCE and user consent check
    - Token Passthrough Prevention wit audience check and safe token management
    - Session Hijacking Prevention wit cryptographic binding and behavior analysis
  - **Enterprise Security Integration**: Azure Application Insights monitoring, threat detection pipelines, and supply chain security
  - **Implementation Checklist**: Clear mandatory against recommended security controls wit Microsoft security ecosystem benefits

### Documentation Quality & Standards Alignment
- **Specification References**: Update all references to current MCP Specification 2025-06-18
- **Microsoft Security Ecosystem**: Better integration guides everywhere for security docs
- **Practical Implementation**: Add full code examples for .NET, Java, and Python with enterprise patterns
- **Resource Organization**: Complete sorting of official docs, security standards, and implementation guides
- **Visual Indicators**: Clear marking for mandatory and recommended practices


#### Core Concepts (01-CoreConcepts/) - Complete Modernization
- **Protocol Version Update**: Update to follow current MCP Specification 2025-06-18 wit date-based version (YYYY-MM-DD format)
- **Architecture Refinement**: Better description for Hosts, Clients, and Servers to show current MCP architecture patterns
  - Hosts now clearly be AI apps wey dey coordinate many MCP client connections
  - Clients na protocol connectors wey keep one-to-one server relationship
  - Servers dey improved wit local or remote wahala dem
- **Primitive Restructuring**: Total overhaul for server and client primitives
  - Server Primitives: Resources (data sources), Prompts (templates), Tools (executable functions) wit full explanation and examples
  - Client Primitives: Sampling (LLM completions), Elicitation (user input), Logging (debugging/monitoring)
  - Update wit current discovery (`*/list`), retrieval (`*/get`), and execution (`*/call`) method patterns
- **Protocol Architecture**: Introduce two-layer architecture model
  - Data Layer: JSON-RPC 2.0 foundation wit lifecycle management and primitives
  - Transport Layer: STDIO (local) and Streamable HTTP with SSE (remote) transport mechanisms
- **Security Framework**: Full security principles including explicit user consent, data privacy protection, tool execution safety, and transport layer security
- **Communication Patterns**: Update protocol messages to show initialization, discovery, execution, and notification flows
- **Code Examples**: Refresh multi-language examples (.NET, Java, Python, JavaScript) to show current MCP SDK patterns

#### Security (02-Security/) - Complete Security Overhaul  
- **Standards Alignment**: Full alignment wit MCP Specification 2025-06-18 security requirements
- **Authentication Evolution**: Document how e evolve from custom OAuth servers to external identity provider delegation (Microsoft Entra ID)
- **AI-Specific Threat Analysis**: Better coverage of current AI attack styles
  - Detailed prompt injection attack scenarios wit real-life examples
  - Tool poisoning methods and "rug pull" attack ways
  - Context window poisoning and model confusion attacks
- **Microsoft AI Security Solutions**: Full coverage of Microsoft security ecosystem
  - AI Prompt Shields wit advanced detection, highlighting, and delimiter ways
  - Azure Content Safety integration ways
  - GitHub Advanced Security for supply chain protection
- **Advanced Threat Mitigation**: Detailed security controls for
  - Session hijacking wit MCP-specific attack examples and cryptographic session ID requirements
  - Confused deputy wahala for MCP proxy cases wit clear consent requirements
  - Token passthrough weaknesses wit mandatory validation controls
- **Supply Chain Security**: Expand AI supply chain coverage including foundation models, embeddings services, context providers, and third-party APIs
- **Foundation Security**: Better integration wit enterprise security patterns including zero trust architecture and Microsoft security ecosystem
- **Resource Organization**: Categorize complete resource links by type (Official Docs, Standards, Research, Microsoft Solutions, Implementation Guides)

### Documentation Quality Improvements
- **Structured Learning Objectives**: Better learning objectives wit specific, actionable results 
- **Cross-References**: Add links between related security and core concept topics
- **Current Information**: Update all date and spec links to current standards
- **Implementation Guidance**: Add specific, actionable implementation tips everywhere for both sections

## July 16, 2025

### README and Navigation Improvements
- Completely redesign the curriculum navigation for README.md
- Change `<details>` tags to more easy table-based format
- Make alternative layout options for new "alternative_layouts" folder
- Add card-based, tabbed-style, and accordion-style navigation examples
- Update repository structure section to cover all latest files
- Better "How to Use This Curriculum" section wit clear recommendations
- Update MCP specification links to point to correct URLs
- Add Context Engineering section (5.14) for curriculum structure

### Study Guide Updates
- Completely change study guide to match current repository structure
- Add new sections for MCP Clients and Tools, and Popular MCP Servers
- Update Visual Curriculum Map to accurately show all topics
- Better descriptions of Advanced Topics to cover all special areas
- Update Case Studies section to show real examples
- Add this full changelog

### Community Contributions (06-CommunityContributions/)
- Add detailed info about MCP servers for image generation
- Add full section on how to use Claude in VSCode
- Add Cline terminal client setup and how to use am
- Update MCP client section to include popular client options
- Better contribution examples wit more correct code samples

### Advanced Topics (05-AdvancedTopics/)
- Organize all specialized topic folders wit consistent naming
- Add context engineering materials and examples
- Add Foundry agent integration docs
- Better Entra ID security integration docs

## June 11, 2025

### Initial Creation
- Release first version of MCP for Beginners curriculum
- Make basic structure for all 10 main sections
- Implement Visual Curriculum Map for navigation
- Add initial sample projects for many programming languages

### Getting Started (03-GettingStarted/)
- Make first server implementation examples
- Add client development direction
- Include LLM client integration instructions
- Add VS Code integration docs
- Implement Server-Sent Events (SSE) server examples

### Core Concepts (01-CoreConcepts/)
- Add full explanation of client-server architecture
- Make docs on key protocol parts
- Document messaging styles in MCP

## May 23, 2025

### Repository Structure
- Start the repository with basic folder structure
- Make README files for each big section
- Setup translation system
- Add image files and diagrams

### Documentation
- Make first README.md wit curriculum overview
- Add CODE_OF_CONDUCT.md and SECURITY.md
- Setup SUPPORT.md wit advice for getting help
- Make initial study guide structure

## April 15, 2025

### Planning and Framework
- Initial planning for MCP for Beginners curriculum
- Define learning goals and target audience
- Outline 10-section structure of curriculum
- Develop conceptual framework for examples and case studies
- Make initial prototype examples for key concepts

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
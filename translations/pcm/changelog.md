# Changelog: MCP for Beginners Curriculum

Dis dokument na record of all di important changes wey dem make for di Model Context Protocol (MCP) for Beginners curriculum. Dem dey write di changes for back-to-front order (di newest changes first).

## September 9th, 2026

### MCP 2026-07-28 Final Specification Alignment

Update di English curriculum from release-candidate and `2025-11-25`
baseline guide go di final MCP `2026-07-28` specification.

- **Updated**: Current-version references, specification links, stateless
  request guide, `server/discover`, Streamable HTTP headers, and di Tasks
  extension lifecycle across 38 English documentation files.
- **Corrected**: Elicitation now dey use `elicitation/create`, Sampling dey use
  `sampling/createMessage`, and `InputRequiredResult.resultType` dey use
  `"input_required"`.
- **Replaced**: Di wrong Root Context conversation-state lesson with
  protocol-accurate Roots lesson wey dey cover informational filesystem hints, di
  current multi-round-trip flow, security boundaries, and migration options.
- **Clarified**: Roots, Sampling, Logging, and Dynamic Client Registration don become
  deprecated for `2026-07-28`, wit their recommended replacements and earliest
  removal date wey dem document.
- **Labeled**: Samples wey still depend on MCP `2025-11-25`, HTTP+SSE,
  initialization handshakes, or protocol sessions dey remain as legacy
  compatibility examples no be current implementations.
- **Security guide**: Update standalone security guides to dey use
  per-request authorization and explicit application state handles instead of
  removed protocol session IDs. Client ID Metadata Documents na now
  di preferred registration path, wit DCR documented as compatibility-only.
- **Supporting material**: Update di study guide, contributor checklist,
  Publora case study, and APIM case study. Di APIM walkthrough now recommend
  its current Streamable HTTP `/mcp` endpoint instead of deprecated `/sse`.
- **Canonical links**: Replace retired and draft specification URLs for English
  source Markdown wit versioned `2026-07-28` links, but keep explicit
  links to legacy versions where sample still dey pinned to older tooling.
- **Stable filenames**: Rename di final specification guide and two security
  guides to remove release-candidate and year suffixes, then update all English
  hyperlinks to their stable paths.
- **New authorization sample**: Add one tested
  [TypeScript MCP `2026-07-28` resource server](./02-Security/samples/cimd-dcr-auth/README.md)
  wey compare preferred Client ID Metadata Documents wit deprecated Dynamic
  Client Registration fallback. Di sample get RFC 9728 discovery, JWKS
  validation, per-tool scopes, twelve tests, and Auth0 setup walkthrough.
- **Translation scope**: Only English source files dey edited; generated
  translations and translated images no change as dem be auto-translated.

## July 29th, 2026

### New Module 08 Companion: Reliability Sidecars and Safe Retries

Add one vendor-neutral companion lesson for MCP tools wey dey create real-world
effects, aligned wit di final `2026-07-28` specification.

- **New**: Di [reliability sidecar companion lesson][reliability-sidecar]
  dey use one support-ticket story, two Mermaid diagrams, and retry decision
  flow to explain stable operation keys, atomic duplicate admission,
  reconciliation, evidence, and Tasks extension boundary.
- **New**: Standard-library Python and SQLite failure-injection exercise
  dey use separate operation and ticket stores to show response wey lost
  after external effect commit. Six deterministic tests cover naive
  duplication, guarded restart recovery, payload conflicts, cached results,
  active claims, and concurrent duplicate admission.
- **Updated**: Module 08 now link di companion lesson, identify di
  final `2026-07-28` stateless request model, separate OpenTelemetry
  observability from deprecated MCP logging feature, and limit e generic
  retry example to read-only operations.
- **Optional**: Di lesson map di portable concepts to one tagged community
  implementation without make di hosted service or network call part of
  di exercise.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## July 2nd, 2026

### New Lesson: Di 2026-07-28 MCP Specification Release Candidate

Add coverage of di coming `2026-07-28` MCP specification release candidate (wey dem announce May 21, 2026; final release scheduled July 28, 2026), wey dem summarize from di [official announcement blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Di curriculum baseline still **MCP Specification 2025-11-25** until new version ready, so na forward-looking guide e be, no be rewrite of old lessons.

- **New**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — full lesson wey cover di stateless protocol core (remove `initialize` handshake and `Mcp-Session-Id`), new `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context for `_meta`, di formal Extensions framework (MCP Apps and new Tasks extension), six authorization-hardening SEPs, di deprecation of Roots/Sampling/Logging, and move to full JSON Schema 2020-12 for tool schemas.
- **Updated** wit forward-looking callouts linking to di new lesson:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protocol version note, Sampling/Roots/Logging/Tasks sections, and "Wetin dey next"
  - [02-Security/README.md](./02-Security/README.md): authorization hardening callout
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport callout
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling deprecation callout
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging deprecation and Tasks extension callout
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing callout
  - [README.md](./README.md): "Look ahead" note for di specification section and new `1.1` entry for curriculum module table
  - [study_guide.md](./study_guide.md): forward-looking bullet under Core Concepts overview and dated addendum note
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): callout on `mcp-session-id` transport map before stateless request model
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): module overview callout on Root Contexts/Sampling deprecations and Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): authorization hardening callout

## June 24th, 2026

### New Lesson: How to Use MCP for Copilot app

- [Tooling section](./12-tooling/README.md) Add tooling section.
- [MCP for Copilot app](./12-tooling/01-copilot-app/README.md)

## June 16, 2026

### MCP Specification Alignment & Sample Validation

Check the curriculum against current **MCP Specification 2025-11-25** and latest official SDKs, then correct all remaining old specification references and confirm say core samples still build and run.

#### Specification Version Corrections (2025-06-18 / 2025-03-26 → 2025-11-25)

Update English content where e still talk say older spec revision na *current/latest* standard, and repoint links to di official `modelcontextprotocol.io` spec paths:
- **05-AdvancedTopics/mcp-security/README.md**: Update "Current Standard" banner, introduction, core security principles heading, mandatory requirements heading, Microsoft Entra ID section, References & Resources links, and closing security notice (8 references) to 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Update Additional Resources spec link and "Current Standard" banner to 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Replace outdated `2025-03-26` security-and-trust link with current 2025-11-25 security best practices page
- **03-GettingStarted/14-sampling/README.md**: Update official sampling docs link to 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Update present-tense "current MCP specification" reference and Additional Resources spec link to 2025-11-25 (historical SSE-deprecation notes still dey for accuracy)

#### Sample Validation Against Current SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` resolved `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` pass wit no type errors — existing `McpServer`/`StdioServerTransport` APIs still valid
- **Python (03-GettingStarted/01-first-server/solution/python)**: Verify for isolated `.venv` wit `mcp[cli]` (1.27.2); `py_compile` pass and `FastMCP.list_tools()` correctly return `add` and `subtract` tools
- Confirm say all sample `@modelcontextprotocol/sdk` version ranges (`>=1.26.0` / `^1.26.0` / `^1.27.0`) resolve cleanly to current `1.29.0` wit no breaking API changes

#### Dependency Pin Alignment (close version gaps)

Update outdated SDK pins so every sample dey track di current MCP release, to match di repo-wide convention:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Bump `@modelcontextprotocol/sdk` from `^1.8.0` → `>=1.26.0` and update stale `"updated for MCP 2025-06-18"` package description to `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** and **lab4/code/github_mcp_server/pyproject.toml**: Bump exact pin `mcp==1.23.0` → `mcp>=1.26.0`; regenerate both `uv.lock` files (`uv lock`) so lockfiles resolve to current `mcp 1.27.2` and stay in sync wit manifests

#### Curriculum Gap Analysis — Latest Spec Feature Coverage

Check say di curriculum dey cover all di primitives wey MCP 2025-11-25 introduce or expand, so no content gaps remain:
- **Sampling**: Lesson 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (including URL mode)**: Document for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Document for 00-Introduction, 01-CoreConcepts, and 05-AdvancedTopics/mcp-root-contexts
- **Tasks (experimental, long-running operations)**: Document for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Document for 01-CoreConcepts and 05-AdvancedTopics/mcp-protocol-features

### Security Hardening & Dependency Vulnerability Fix

Run full security check for every dependency manifest and sample source code, then fix all reported npm advisories and one code-level finding. After fix, `npm audit` show **0 vulnerabilities** for every audited directory.

#### npm Dependency Vulnerabilities (transitive) — Fixed

Audit all 15 committed `package-lock.json` files. Vulnerabilities dey limited to transitive dependencies wey MCP Inspector dev tool, OpenAI client, and MCP SDK pull; all na resolve now wit no breaking for di samples:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** and **lab3/code/weather_mcp/inspector**: Im update `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), wey clear di bundled `ajv`, `brace-expansion`, `diff`, `path-to-regexp` and `ws` advisories dem. Add one npm `overrides` entry wey force di patched `shell-quote@1.8.4` make e comot di remaining critical advisory wey `concurrently` carry; regenerate both lockfiles (now 0 vulnerabilities)
- **03-GettingStarted/samples/typescript**: `npm audit fix` update di transitive `qs` (moderate) go patched release
- **03-GettingStarted/samples/javascript**: `npm audit fix` update di transitive `hono` (moderate) go patched release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` update di transitive `form-data` (high) go patched release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generate di missing `package-lock.json` so di project fit dey reproducible and auditable (0 vulnerabilities)

#### Code-Level Security Fix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Remove `shell=True` from di `open_in_vscode` tool. Di old `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` allow shell metacharacters for inside folder path to dey interpreted by `cmd.exe` (command-injection vector). Now e dey launch di resolved `Code.exe` directly with di folder as argument — no shell — wey be the same thing and safe

#### Python Dependency Audit

- Audited every Python requirements set with `pip-audit`. `05-AdvancedTopics` and `03-GettingStarted/samples/python` no report any **vulnerabilities** (dem `mcp` / `httpx` / `pydantic` / `python-dotenv` ranges dey resolve to current patched releases)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` flash one transitive dependency **`werkzeug` 3.1.1** with three `safe_join` Windows device-name DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, and `CVE-2026-27199` (all dem fix for 3.1.6). Add one explicit security pin `werkzeug>=3.1.6` so di patched release fit resolve well; confirm say di constraint resolve cleanly with di `chainlit` / `mcp` / `semantic-kernel` stack

### Product Name Rebranding

Update all curriculum content make e show Microsoft's product rebranding:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Update Discord community link
- **AGENTS.md**: Update Discord server reference
- **README.md**: Update technology ecosystem references
- **study_guide.md**: Update case study references
- **05-AdvancedTopics/README.md**: Update Module 5.13 title and description
- **05-AdvancedTopics/mcp-integration/README.md**: Update section header and description
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Update full module title and content
- **05-AdvancedTopics/mcp-security-entra/README.md**: Update cross-reference link
- **07-LessonsfromEarlyAdoption/README.md**: Update case study references
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Update Section 9 header, badges, and capabilities
- **08-BestPractices/README.md**: Update Discord community link
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Update Discord channel reference
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Update model deployment reference
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Update AI Services table
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Update resource references

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Update main curriculum references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Update module title, overview, and all module headers
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Update title, learning objectives, setup instructions, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Update title, learning objectives, MCP hosts table, and cross-references
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Update title, badges, prerequisites, and resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Update Agent Builder references and feedback link
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Update prerequisites and extension references

---

## April 11, 2026

### New Lesson, Documentation Fixes, and Dependency Updates

#### New Curriculum Content Added

**Module 05 - Advanced Topics**
- **Lesson 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): New complete guide wey cover di adversarial debate pattern for multi-agent systems
  - Mermaid architecture diagram: two agents → shared MCP server → debate transcript → judge → verdict
  - Shared MCP tool server (`web_search` + `run_python`) implement for Python and TypeScript
  - Opposing system prompts (FOR / AGAINST / Judge) wit clear tool-use requirements
  - Debate orchestrator for Python, TypeScript, and C# wey dey manage rounds and route arguments
  - MCP `ClientSession` wiring for di orchestrator go real tool calls
  - Use-case table (hallucination detection, threat modeling, API design review, factual verification, tech selection)
  - Security considerations: sandboxed execution, tool-call validation, rate limiting, audit logging
  - Structured exercise wit three practical scenarios (code review, architecture decision, content moderation)

#### Documentation Fixes

**Module 03 - Getting Started**
- **05-stdio-server/README.md**: Fix incomplete TypeScript stdio server example — add missing transport instantiation (`new StdioServerTransport()`) and `server.connect(transport)` call to match Python and .NET examples for di same section
- **14-sampling/README.md**: Fix typo — correct `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Curriculum Updates

**Main README.md**
- Add entry 5.17 (Adversarial Multi-Agent Reasoning with MCP) to curriculum table wit direct link to new lesson

**05-AdvancedTopics/README.md**
- Add Lesson 5.17 row to lessons table

**study_guide.md**
- Add Adversarial Multi-Agent Reasoning topic to mind-map and prose description of Advanced Topics

#### Code and Security Fixes

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Security fix — command injection**: Replace `execSync` shell interpolation wit `execFile` + `promisify` in TypeScript `run_python` tool, make command injection surface comot (LLM-controlled code now dey pass as literal argv element wit no shell involvement)
- **MCP tool loop wiring**: Update Python debate orchestrator to use `AsyncAnthropic` client (replace blocking sync `Anthropic`), pass live `ClientSession` direct to each agent turn, fetch tool definitions via `session.list_tools()` every turn, and dispatch `tool_use` blocks via `session.call_tool()` inside loop til model emit final text response

#### Dependency Updates

- Bump `hono` to 4.12.12 for plenty packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Bump `@hono/node-server` from 1.19.11 to 1.19.13 for TypeScript packages
- Bump `cryptography` from 46.0.5 to 46.0.7 for Python packages (10-StreamliningAIWorkflows labs 3 and 4)
- Bump `lodash` from 4.17.23 to 4.18.1 for 10-StreamliningAIWorkflows inspector

#### Translations

- Sync translations for 48+ languages wit latest source changes (i18n update)

---

## February 5, 2026

### Repository-Wide Validation and Navigation Improvements

#### New Curriculum Content Added

**Module 03 - Getting Started**
- **12-mcp-hosts/README.md**: New full guide for setup MCP hosts
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf configuration examples
  - JSON configuration templates for all main hosts
  - Transport types comparison table (stdio, SSE/HTTP, WebSocket)
  - Troubleshooting common connection wahala
  - Security best practices for host configuration

- **13-mcp-inspector/README.md**: New debugging guide for MCP Inspector
  - Installation ways (npx, npm global, from source)
  - Connect to servers via stdio and HTTP/SSE
  - Test tools, resources, and prompts workflows
  - VS Code integration with MCP Inspector
  - Common debugging scenarios with solutions

**Module 04 - Practical Implementation**
- **pagination/README.md**: New pagination implementation guide
  - Cursor-based pagination patterns for Python, TypeScript, Java
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
  - Error handling patterns wit JSON-RPC codes

#### Navigation Fixes (24+ files updated)

**Main Module READMEs**
 Now links to first lesson AND next module

**02-Security Sub-files**
- All 5 supplementary security documents don get "What's Next" navigation:

**09-CaseStudy Files**
- All case study files don get sequential navigation:

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
- **New Client Primitive - Roots**: Add complete documentation on di Roots client primitive, wey make servers fit understand filesystem boundaries and access permissions
- **Tool Annotations**: Add documentation on tool behavioral annotations (`readOnlyHint`, `destructiveHint`) for better tool execution decisions
- **Tool Calling in Sampling**: Update Sampling documentation to include `tools` and `toolChoice` parameters for model-driven tool invocation during sampling requests
- **URL Mode Elicitation**: Add documentation on URL-based elicitation for server-initiated external web interactions
- **Tasks (Experimental)**: Add new section documenting di experimental Tasks feature for durable execution wrappers and deferred result retrieval

- **Icons Support**: We don notice say tools, resources, resource templates, and prompts fit now get icons as extra metadata

#### Documentation Updates
- **README.md**: We add MCP Specification 2025-11-25 version reference and date-based versioning explanation
- **study_guide.md**: We update curriculum map to add Tasks and Tool Annotations for Core Concepts section; update document timestamp

#### Specification Compliance Verification
- **Protocol Version**: We check say all documentation dey follow MCP Specification 2025-11-25
- **Architecture Alignment**: We confirm say two-layer architecture (Data Layer + Transport Layer) documentation correct
- **Primitives Documentation**: We validate server primitives (Resources, Prompts, Tools) and client primitives (Sampling, Elicitation, Logging, Roots)
- **Transport Mechanisms**: We verify STDIO and Streamable HTTP transport documentation dey correct
- **Security Guidance**: We confirm say e align with current MCP Security Best Practices documentation

#### Key MCP 2025-11-25 Features Documented
- **OpenID Connect Discovery**: Auth server discovery through OIDC
- **OAuth Client ID Metadata Documents**: Dem recommend client registration mechanism
- **JSON Schema 2020-12**: Na default dialect for MCP schema definitions
- **SDK Tiering System**: We formalize requirements for SDK feature support and maintenance
- **Governance Structure**: We formalize Working Groups and Interest Groups for MCP governance

### Security Documentation Major Update (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **New Hands-On Training Resource**: We add comprehensive integration with [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) for all security documentation
- **Expedition Route Coverage**: We document the full camp-to-camp progression from Base Camp to Summit
- **OWASP Alignment**: All security guidance now match OWASP MCP Azure Security Guide risks

#### OWASP MCP Top 10 Integration
- **New Section**: We add OWASP MCP Top 10 Security Risks table plus Azure mitigations to main Security README
- **Risk-Based Documentation**: We update mcp-security-controls-2025.md with OWASP MCP risk references for each security domain
- **Reference Architecture**: We link to OWASP MCP Azure Security Guide reference architecture and implementation patterns

#### Updated Security Files
- **README.md**: We add Sherpa Workshop overview, expedition route table, OWASP MCP Top 10 risks summary, and hands-on training section
- **mcp-security-controls-2025.md**: We update header to February 2026, add OWASP risk references (MCP01-MCP08), fix spec version inconsistency
- **mcp-security-best-practices-2025.md**: We add Sherpa and OWASP resources section, update timestamp
- **mcp-best-practices.md**: We add hands-on training section with Sherpa and OWASP links
- **azure-content-safety-implementation.md**: We add OWASP MCP06 reference, Sherpa Camp 3 alignment, plus extra resources section

#### New Resource Links Added
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individual OWASP MCP risk pages (MCP01-MCP10)

### Curriculum-Wide MCP Specification 2025-11-25 Alignment

#### Module 03 - Getting Started
- **SDK Documentation**: We add Go SDK to official SDK list; update all SDK references to fit MCP Specification 2025-11-25
- **Transport Clarification**: We update STDIO and HTTP Streaming transport descriptions with clear spec references

#### Module 04 - Practical Implementation
- **SDK Updates**: Add Go SDK; update SDK list with specification version reference
- **Authorization Spec**: Update MCP Authorization specification link to current 2025-11-25 version

#### Module 05 - Advanced Topics
- **New Features**: We add note about new MCP Specification 2025-11-25 features (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Security Resources**: Add OWASP MCP Top 10 and Sherpa workshop links to extra references

#### Module 06 - Community Contributions
- **SDK List**: Add Swift and Rust SDKs; update specification link to 2025-11-25
- **Spec Reference**: Update MCP Specification link to direct specification URL

#### Module 07 - Lessons from Early Adoption
- **Resource Updates**: Add MCP Specification 2025-11-25 link and OWASP MCP Top 10 to extra resources

#### Module 08 - Best Practices
- **Spec Version**: Update MCP Specification reference to 2025-11-25
- **Security Resources**: Add OWASP MCP Top 10 and Sherpa workshop to extra references

#### Module 10 - Streamlining AI Workflows
- **Badge Update**: Change MCP version badge from SDK version (1.9.3) to specification version (2025-11-25)
- **Resource Links**: Update MCP Specification link; add OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec Reference**: Update MCP Specification link to 2025-11-25 version
- **Security Resources**: Add OWASP MCP Top 10 to official resources

## December 18, 2025

### Security Documentation Update - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specification Version Update
- **Protocol Version Update**: Update to reference latest MCP Specification 2025-11-25 (we release am November 25, 2025)
  - Update all specification version references from 2025-06-18 to 2025-11-25
  - Update document date references from August 18, 2025 to December 18, 2025
  - Confirm all specification URLs dey point to current documentation
- **Content Validation**: We do thorough validation of security best practices based on the latest standards
  - **Microsoft Security Solutions**: Validate current terminology and links for Prompt Shields (before na "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, and Azure Key Vault
  - **OAuth 2.1 Security**: Confirm alignment with latest OAuth security best practices
  - **OWASP Standards**: Validate OWASP Top 10 for LLMs references still dey current
  - **Azure Services**: Verify all Microsoft Azure documentation links and best practices
- **Standards Alignment**: All referenced security standards confirm say dem dey current
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security and compliance frameworks
- **Implementation Resources**: Verify all implementation guide links and resources
  - Azure API Management authentication patterns
  - Microsoft Entra ID integration guides
  - Azure Key Vault secrets management
  - DevSecOps pipelines and monitoring solutions

### Documentation Quality Assurance
- **Specification Compliance**: Make sure say all mandatory MCP security requirements (MUST/MUST NOT) align with latest specification
- **Resource Currency**: Confirm all external links to Microsoft documentation, security standards, and implementation guides dey current
- **Best Practices Coverage**: Confirm comprehensive coverage of authentication, authorization, AI-specific threats, supply chain security, and enterprise patterns

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: We introduce comprehensive guide to advanced MCP server usage, covering both normal and low-level server architectures.
  - **Regular vs. Low-Level Server**: Detailed comparison and code examples for Python and TypeScript for both ways.
  - **Handler-Based Design**: Explanation of handler-based tool/resource/prompt management for scalable, flexible server implementations.
  - **Practical Patterns**: Real-world examples where low-level server patterns dey useful for advanced features and architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide to implement simple authentication for MCP servers.
  - **Auth Concepts**: Clear explanation of authentication vs. authorization, and credential handling.
  - **Basic Auth Implementation**: Middleware-based authentication patterns for Python (Starlette) and TypeScript (Express), plus code samples.
  - **Progression to Advanced Security**: Guidance for start with simple auth and move on to OAuth 2.1 and RBAC, with references to advanced security modules.

These additions provide practical, hands-on guidance for building stronger, secure, and flexible MCP server implementations, bridging foundational concepts with advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: Add comprehensive hands-on curriculum for build production-ready MCP servers with PostgreSQL database integration
  - **Real-World Implementation**: Zava Retail analytics use case wey show enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: Systematically update all README files in 11-MCPServerHandsOnLabs to change "Module" to "Lab"
  - **Section Headers**: Change "What This Module Covers" to "What This Lab Covers" for all 13 labs
  - **Content Description**: Change "This module provides..." to "This lab provides..." everywhere
  - **Learning Objectives**: Change "By the end of this module..." to "By the end of this lab..."
  - **Navigation Links**: Change all "Module XX:" mentions to "Lab XX:" for cross-references and navigation
  - **Completion Tracking**: Change "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: Keep Python module references for config files (e.g., `"module": "mcp_server.main"`)

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Add new "11. Database Integration Labs" section with full lab structure visualization
- **Repository Structure**: Update from ten to eleven main sections with full 11-MCPServerHandsOnLabs description
- **Learning Path Guidance**: Improve navigation instructions to cover sections 00-11
- **Technology Coverage**: Add FastMCP, PostgreSQL, Azure services integration details
- **Learning Outcomes**: Emphasize production-ready server development, database integration patterns, and enterprise security

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Update main README.md in 11-MCPServerHandsOnLabs to use "Lab" structure everywhere
- **Learning Path Organization**: Clear progression from foundation concepts through advanced implementation to production deployment
- **Real-World Focus**: Focus on practical, hands-on learning with enterprise-grade patterns and tech

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: Reinforce practical, lab-based approach throughout documentation
- **Enterprise Patterns Focus**: Highlight production-ready implementations and enterprise security considerations
- **Technology Integration**: Cover modern Azure services and AI integration patterns well
- **Learning Progression**: Clear, structured path from basic concepts to production deployment

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Major expansion with full GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: New full case study wey look GitHub MCP Registry launch for September 2025
    - **Problem Analysis**: Detailed look at fragmented MCP server discovery and deployment wahala
    - **Solution Architecture**: GitHub centralized registry approach with one-click VS Code install
    - **Business Impact**: Measurable improvements for developer onboarding and productivity
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability
    - **Ecosystem Development**: Position as solid platform for agentic integration
  - **Enhanced Case Study Structure**: Update all seven case studies with consistent form and full descriptions
    - Azure AI Travel Agents: Multi-agent orchestration focus
    - Azure DevOps Integration: Workflow automation focus
    - Real-Time Documentation Retrieval: Python console client implementation
    - Interactive Study Plan Generator: Chainlit conversational web app

    - In-Editor Documentation: VS Code na GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Ecosystem development na community platform
  - **Comprehensive Conclusion**: Rewritten conclusion section wey dey highlight seven case studies wey cover multiple MCP implementation dimensions
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications categorization
    - Enhanced insights into architectural patterns, implementation strategies, and best practices
    - Emphasis on MCP as mature, production-ready protocol

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Updated mindmap to include GitHub MCP Registry for Case Studies section
- **Case Studies Description**: Enhanced from generic descriptions to detailed breakdown of seven comprehensive case studies
- **Repository Structure**: Updated section 10 to show comprehensive case study coverage with specific implementation details
- **Changelog Integration**: Added September 26, 2025 entry wey talk about GitHub MCP Registry addition and case study improvements
- **Date Updates**: Updated footer timestamp to show latest revision (September 26, 2025)

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardized case study formatting and structure across all seven examples
- **Comprehensive Coverage**: Case studies now cover enterprise, developer productivity, and ecosystem development scenarios
- **Strategic Positioning**: Enhanced focus on MCP as foundational platform for agentic system deployment
- **Resource Integration**: Updated additional resources to include GitHub MCP Registry link

## September 15, 2025

### Advanced Topics Expansion - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - New Advanced Implementation Guide
- **README.md**: Complete implementation guide for custom MCP transport mechanisms
  - **Azure Event Grid Transport**: Complete serverless event-driven transport implementation
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
  - **MCP Protocol Alignment**: How MCP design dey solve context engineering challenges
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
- **Content Organization**: All 05-AdvancedTopics folders now dey follow consistent naming pattern (mcp-[topic])

### Documentation Quality Enhancements
- **MCP Specification Alignment**: All new content dey reference current MCP Specification 2025-06-18
- **Multi-Language Examples**: Complete code examples for C#, TypeScript, and Python
- **Enterprise Focus**: Production-ready patterns and Azure cloud integration everywhere
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
- **MCP-SECURITY-CONTROLS-2025.md**: Total overhaul with enterprise-grade security framework
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
  - **Microsoft Solutions Integration**: Complete coverage of Azure security services, GitHub Advanced Security, and enterprise identity management

#### Advanced Topics Security (05-AdvancedTopics/mcp-security/) - Production-Ready Implementation
- **README.md**: Complete rewrite for enterprise security implementation
  - **Current Specification Alignment**: Updated to MCP Specification 2025-06-18 with mandatory security requirements
  - **Enhanced Authentication**: Microsoft Entra ID integration with complete .NET and Java Spring Security examples
  - **AI Security Integration**: Microsoft Prompt Shields and Azure Content Safety implementation with detailed Python examples
  - **Advanced Threat Mitigation**: Complete implementation examples for
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
  - Hosts now clearly defined as AI applications wey dey coordinate multiple MCP client connections
  - Clients described as protocol connectors wey dey maintain one-to-one server relationships
  - Servers enhanced with local vs. remote deployment scenarios
- **Primitive Restructuring**: Total overhaul of server and client primitives
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
- **Microsoft AI Security Solutions**: Complete coverage of Microsoft security ecosystem
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
- Added comprehensive section on how to use Claude for VSCode
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

- Bin create beta structure for all di 10 main sections
- Bin implement Visual Curriculum Map for navigation
- Bin add first sample projects for different programming languages

### Getting Started (03-GettingStarted/)
- Bin create first server implementation examples
- Bin add client development guidance
- Bin include LLM client integration instructions
- Bin add VS Code integration documentation
- Bin implement Server-Sent Events (SSE) server examples

### Core Concepts (01-CoreConcepts/)
- Bin add detailed explanation of client-server architecture
- Bin create documentation on key protocol components
- Bin document messaging patterns for MCP

## May 23, 2025

### Repository Structure
- Bin initialize di repository with basic folder structure
- Bin create README files for each major section
- Bin set up translation infrastructure
- Bin add image assets and diagrams

### Documentation
- Bin create initial README.md with curriculum overview
- Bin add CODE_OF_CONDUCT.md and SECURITY.md
- Bin set up SUPPORT.md with guidance for how to get help
- Bin create preliminary study guide structure

## April 15, 2025

### Planning and Framework
- Bin make initial plans for MCP for Beginners curriculum
- Bin define learning objectives and target audience
- Bin outline 10-section structure for the curriculum
- Bin develop conceptual framework for examples and case studies
- Bin create initial prototype examples for key concepts

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
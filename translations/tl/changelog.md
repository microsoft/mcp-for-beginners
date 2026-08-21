# Changelog: MCP para sa Mga Nagsisimula Kursong Pangkurikulum

Ang dokumentong ito ay nagsisilbing talaan ng lahat ng mahahalagang pagbabago na ginawa sa Model Context Protocol (MCP) para sa mga nagsisimula na kurikulum. Ang mga pagbabago ay idinadokumento sa reverse chronological order (pinakabago ang mga pagbabago una).

## Hulyo 29, 2026

### Bagong Module 08 Kasamang Aralin: Mga Reliability Sidecars at Ligtas na Retry

Idinagdag ang isang vendor-neutral na kasamang aralin para sa mga MCP tool na lumilikha ng mga totoong epekto sa mundo,
alinsunod sa panghuling `2026-07-28` na espesipikasyon.

- **Bago**: Ang [reliability sidecar companion lesson][reliability-sidecar]
  ay gumagamit ng isang kuwento ng support-ticket, dalawang Mermaid diagram, at isang flow ng retry decision
  upang ipaliwanag ang mga stable operation keys, atomic duplicate admission,
  reconciliation, ebidensya, at ang Tasks extension boundary.
- **Bago**: Isang standard-library Python at SQLite failure-injection exercise
  na gumagamit ng hiwalay na operation at ticket stores upang ipakita ang isang nawalang tugon
  pagkatapos mag-commit ang isang external effect. Anim na deterministic na mga pagsubok ang sumasaklaw sa naive
  duplication, guarded restart recovery, payload conflicts, cached results,
  active claims, at concurrent duplicate admission.
- **Nai-update**: Ngayon ay nagli-link ang Module 08 sa kasamang aralin, tinutukoy ang
  panghuling `2026-07-28` na stateless request model, pinag-iiba ang OpenTelemetry
  observability mula sa deprecated na MCP logging feature, at nililimitahan ang
  generic retry example nito sa read-only operations.
- **Opsyonal**: Ini-map ng aralin ang mga portable concepts nito sa isang naka-tag na community
  implementation nang hindi isinasali ang hosted service o isang network call bilang bahagi ng
  ng exercise.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## Hulyo 2, 2026

### Bagong Aralin: Ang 2026-07-28 MCP Specification Release Candidate

Idinagdag ang saklaw ng nalalapit na `2026-07-28` MCP specification release candidate (inaanunsyo noong Mayo 21, 2026; naka-iskedyul ang final release sa Hulyo 28, 2026), na pinaikling mula sa [opisyal na anunsyo sa blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Ang baseline ng kurikulum ay nanatiling **MCP Specification 2025-11-25** hanggang sa lumabas ang bagong bersyon, kaya ito ay inilalahad bilang patunguhang gabay at hindi muling pagsusulat ng umiiral na mga aralin.

- **Bago**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — isang buong aralin na sumasaklaw sa stateless protocol core (pag-alis ng `initialize` handshake at `Mcp-Session-Id`), ang mga bagong `Mcp-Method`/`Mcp-Name` na routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context sa `_meta`, ang pormal na Extensions framework (MCP Apps at ang bagong Tasks extension), anim na authorization-hardening SEPs, ang pag-deprecate ng Roots/Sampling/Logging, at ang paglilipat sa buong JSON Schema 2020-12 para sa mga tool schemas.
- **Nai-update** na may mga patunguhang link sa bagong aralin:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): tala ng bersyon ng protocol, mga seksyon ng Sampling/Roots/Logging/Tasks, at "Ano ang susunod"
  - [02-Security/README.md](./02-Security/README.md): callout sa authorization hardening
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): callout sa stateless transport
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): callout sa Sampling deprecation
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): callout sa Logging deprecation at Tasks extension
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): callout sa stateless/session-routing
  - [README.md](./README.md): tala ng "Tumingin sa hinaharap" sa seksyon ng espesipikasyon at isang bagong `1.1` entry sa talahanayan ng kurikulum module
  - [study_guide.md](./study_guide.md): forward-looking bullet sa ilalim ng Core Concepts overview at isang dated na addendum na tala
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): callout sa `mcp-session-id` transport map bago ang stateless request model
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): module overview callout sa Root Contexts/Sampling deprecations at Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): callout sa authorization hardening

## Hunyo 24, 2026

### Bagong Aralin: Paggamit ng MCP sa Copilot app

- [Seksyon ng Tooling](./12-tooling/README.md) Idinagdag na seksyon ng tooling.
- [MCP sa Copilot app](./12-tooling/01-copilot-app/README.md)

## Hunyo 16, 2026

### Pag-align sa MCP Specification at Sample Validation

Pinatunayan ang kurikulum laban sa kasalukuyang **MCP Specification 2025-11-25** at ang pinakabagong opisyal na SDK, at inayos ang natitirang mga lumang espesipikasyon na tinutukoy at kinumpirma na ang mga core sample ay patuloy na nagbuo at tumatakbo.

#### Mga Pagwawasto sa Bersyon ng Espesipikasyon (2025-06-18 / 2025-03-26 → 2025-11-25)

In-update ang English na nilalaman kung saan sinabing ang mas lumang bersyon ng spec ay ang *kasalukuyan/pinakabago* na pamantayan, at inilipat ang mga link sa canonical na mga path ng espesipikasyon sa `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: In-update ang banner na "Current Standard", panimula, pamagat ng mga pangunahing prinsipyo sa seguridad, pamagat ng mga kinakailangang mandatoryo, seksyon ng Microsoft Entra ID, mga link ng References & Resources, at pangwakas na paalala sa seguridad (8 mga reference) sa 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: In-update ang link sa Additional Resources na espesipikasyon at ang banner na "Current Standard" sa 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Pinalitan ang luma at outdated na `2025-03-26` na security-and-trust link ng kasalukuyang 2025-11-25 security best practices page
- **03-GettingStarted/14-sampling/README.md**: In-update ang opisyal na link ng sampling docs sa 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: In-update ang kasalukuyang "current MCP specification" reference sa kasalukuyang panahon at ang Additional Resources spec link sa 2025-11-25 (iniwan ang mga historical SSE-deprecation notes para sa katumpakan)

#### Pagpapatunay ng Sample Laban sa Kasalukuyang SDK

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` ay nag-resolve sa `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` ay pumasa nang walang error sa type — nananatiling valid ang umiiral na `McpServer`/`StdioServerTransport` APIs
- **Python (03-GettingStarted/01-first-server/solution/python)**: Pinatunayan sa isang isolated na `.venv` gamit ang `mcp[cli]` (1.27.2); `py_compile` pumasa at ang `FastMCP.list_tools()` ay tama ang pagbabalik ng `add` at `subtract` na mga tool
- Nakumpirma na ang lahat ng sample na `@modelcontextprotocol/sdk` version ranges (`>=1.26.0` / `^1.26.0` / `^1.27.0`) ay nag-resolve ng malinis sa kasalukuyang `1.29.0` nang walang breaking API changes

#### Pag-align sa Dependency Pin (pagsasara ng version gaps)

Itinaas ang mga luma at hindi updated na SDK pins upang masubaybayan ng bawat sample ang kasalukuyang MCP release, na sumusunod sa toàn repo-wide na konbensiyon:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Itinaas ang `@modelcontextprotocol/sdk` mula `^1.8.0` → `>=1.26.0` at in-update ang lumang `"updated for MCP 2025-06-18"` na paglalarawan ng package sa `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** at **lab4/code/github_mcp_server/pyproject.toml**: Itinaas ang eksaktong pin `mcp==1.23.0` → `mcp>=1.26.0`; muling nilikha parehas `uv.lock` na mga file (`uv lock`) upang ang mga lockfile ay nag-resolve sa kasalukuyang `mcp 1.27.2` at manatiling naka-sync sa mga manifest

#### Pagsusuri ng Kurikulum Gap — Pinakabagong Saklaw ng Tampok ng Spec

Nakumpirma na saklaw na ng kurikulum ang lahat ng mga primitives na ipinakilala/pinalawak sa MCP 2025-11-25, kaya walang natitirang agwat sa nilalaman:
- **Sampling**: Aralin 03-GettingStarted/14-sampling kasama ang 05-AdvancedTopics/mcp-sampling
- **Elicitation (kabilang ang URL mode)**: Naka-dokumento sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Naka-dokumento sa 00-Introduction, 01-CoreConcepts, at 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimental, mga pangmatagalang operasyon)**: Naka-dokumento sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Naka-dokumento sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features

### Pagpapalakas ng Seguridad at Pag-ayos ng Vulnerability sa Dependency

Nagsagawa ng buong security pass sa bawat dependency manifest at sa sample source code, pagkatapos ay inayos ang lahat ng naulat na npm advisories at isang code-level na natuklasan. Pagkatapos ng pag-aayos, nag-ulat ang `npm audit` ng **0 vulnerabilities** sa bawat audited directory.

#### Mga Vulnerabilidad ng npm Dependency (transitive) — Naayos

Sinuri ang lahat ng 15 na committed na `package-lock.json` na mga file. Ang mga vulnerabilidad ay limitado sa mga transitive dependencies na ibinunot ng MCP Inspector dev tool, OpenAI client, at MCP SDK; lahat ay naayos na ngayon nang hindi sinisira ang mga sample:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** at **lab3/code/weather_mcp/inspector**: Itinaas ang `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), na naglinis ng bundled `ajv`, `brace-expansion`, `diff`, `path-to-regexp` at `ws` na mga advisory. Nagdagdag ng npm `overrides` entry na pinipilit ang patched na `shell-quote@1.8.4` upang alisin ang natitirang critical advisory na dala ng `concurrently`; muling nilikha ang parehong lockfiles (ngayon 0 vulnerabilidad)
- **03-GettingStarted/samples/typescript**: `npm audit fix` in-update ang transitive `qs` (moderate) sa patched release
- **03-GettingStarted/samples/javascript**: `npm audit fix` in-update ang transitive `hono` (moderate) sa patched release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` in-update ang transitive `form-data` (high) sa patched release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Nilikha ang nawawalang `package-lock.json` kaya ang proyekto ay reproducible at auditable (0 vulnerabilities)

#### Code-Level Security Fix (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Tinanggal ang `shell=True` mula sa `open_in_vscode` tool. Ang dati na `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` ay nagpapahintulot ng shell metacharacters sa folder path na ma-interpret ng `cmd.exe` (command-injection vector). Ngayon ay direktang inilulunsad ang resolved na `Code.exe` gamit ang folder bilang argumento — walang shell — na pantay na gumagana at ligtas

#### Python Dependency Audit

- Sinuri ang bawat set ng Python requirements gamit ang `pip-audit`. Nag-ulat ang `05-AdvancedTopics` at `03-GettingStarted/samples/python` ng **walang kilalang vulnerabilidad** (ang kanilang `mcp` / `httpx` / `pydantic` / `python-dotenv` ranges ay nag-resolve sa mga kasalukuyang na-patch na mga release)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: Nag-flag ang `pip-audit` sa transitive dependency na **`werkzeug` 3.1.1** na may tatlong `safe_join` Windows device-name DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, at `CVE-2026-27199` (lahat ay naayos sa 3.1.6). Nagdagdag ng explicit security pin `werkzeug>=3.1.6` upang ma-resolve ang patched release; kinumpirma na malinis ang pag-resolve ng constraint gamit ang `chainlit` / `mcp` / `semantic-kernel` stack

### Pagbabago ng Pangalan ng Produkto

In-update ang lahat ng nilalaman ng kurikulum upang ipakita ang rebranding ng produkto ng Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: In-update ang link ng Discord community

- **AGENTS.md**: Na-update ang sanggunian sa Discord server
- **README.md**: Na-update ang mga sanggunian sa teknolohiyang ekosistema
- **study_guide.md**: Na-update ang mga sanggunian sa case study
- **05-AdvancedTopics/README.md**: Na-update ang pamagat at paglalarawan ng Module 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Na-update ang header ng seksyon at paglalarawan
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Buong pamagat ng module at pag-update ng nilalaman
- **05-AdvancedTopics/mcp-security-entra/README.md**: Na-update ang cross-reference link
- **07-LessonsfromEarlyAdoption/README.md**: Na-update ang mga sanggunian sa case study
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Na-update ang Section 9 header, mga badge, at mga kakayahan
- **08-BestPractices/README.md**: Na-update ang link ng Discord community
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Na-update ang sanggunian sa Discord channel
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Na-update ang sanggunian sa pag-deploy ng modelo
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Na-update ang talahanayan ng AI Services
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Na-update ang mga sanggunian sa resources

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension para sa VS Code
- **README.md**: Na-update ang mga pangunahing sanggunian ng kurikulum
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Na-update ang pamagat ng module, pangkalahatang-ideya, at lahat ng mga header ng module
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Na-update ang pamagat, mga layunin sa pagkatuto, mga instruksiyon sa pagsasaayos, at mga resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Na-update ang pamagat, mga layunin sa pagkatuto, talahanayan ng MCP hosts, at mga cross-reference
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Na-update ang pamagat, mga badge, mga kinakailangan, at mga resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Na-update ang mga sanggunian sa Agent Builder at link ng feedback
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Na-update ang mga kinakailangan at mga sanggunian sa extension

---

## Abril 11, 2026

### Bagong Aralin, Mga Pag-aayos sa Dokumentasyon, at Mga Update sa Dependency

#### Idinagdag na Bagong Nilalaman ng Kurikulum

**Module 05 - Mga Advanced na Paksa**
- **Lesson 5.17: Adversarial Multi-Agent Reasoning gamit ang MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Bagong komprehensibong gabay na sumasaklaw sa adversarial debate pattern para sa mga multi-agent systems
  - Diagram ng arkitektura sa mermaid: dalawang agent → shared MCP server → debate transcript → hurado → hatol
  - Shared MCP tool server (`web_search` + `run_python`) na ipinatupad sa Python at TypeScript
  - Mga opposing na system prompt (FOR / AGAINST / Judge) na may malinaw na mga pangangailangan sa paggamit ng tool
  - Debate orchestrator sa Python, TypeScript, at C# na nagpapatakbo ng mga round at nag-ruruta ng mga argumento
  - MCP `ClientSession` wiring para sa orchestrator sa mga totoong tawag sa tool
  - Talahanayan ng use-case (deteksyon ng halusinasyon, pagmomodelo ng banta, pagsusuri ng disenyo ng API, pag-verify ng mga katotohanan, pagpili ng teknolohiya)
  - Mga konsiderasyon sa seguridad: sandboxed na pagpapatupad, pagpapatunay ng tawag sa tool, rate limiting, audit logging
  - Estrukturadong pagsasanay na may tatlong praktikal na senaryo (review ng code, desisyon sa arkitektura, moderasyon ng nilalaman)

#### Mga Pag-aayos sa Dokumentasyon

**Module 03 - Pagsisimula**
- **05-stdio-server/README.md**: Naayos ang hindi kumpletong halimbawa ng TypeScript stdio server — idinagdag ang nawawalang paglikha ng transport (`new StdioServerTransport()`) at tawag na `server.connect(transport)` upang tumugma sa mga halimbawa sa Python at .NET sa parehong seksyon
- **14-sampling/README.md**: Naayos ang typographical error — itinama ang `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang entry 5.17 (Adversarial Multi-Agent Reasoning with MCP) sa talahanayan ng kurikulum na may direktang link sa bagong aralin

**05-AdvancedTopics/README.md**
- Idinagdag ang Lesson 5.17 na hilera sa talahanayan ng mga aralin

**study_guide.md**
- Idinagdag ang paksang Adversarial Multi-Agent Reasoning sa mind-map at paglalarawan sa teksto ng Mga Advanced na Paksa

#### Pag-aayos ng Code at Seguridad

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Pag-aayos sa Seguridad — command injection**: Pinalitan ang `execSync` shell interpolation ng `execFile` + `promisify` sa TypeScript `run_python` tool, tinanggal ang command injection surface (ang LLM-controlled na code ay ipinapasa bilang literal na argv element nang walang shell involvement)
- **MCP tool loop wiring**: In-update ang Python debate orchestrator sa paggamit ng `AsyncAnthropic` client (pinalitan ang blocking sync `Anthropic`), ipinapasa ang live na `ClientSession` direkta sa bawat turn ng agent, kinukuha ang tool definitions gamit ang `session.list_tools()` sa bawat turn, at ipinapadala ang mga `tool_use` block gamit ang `session.call_tool()` sa loop hanggang maglabas ang modelo ng panghuling text response

#### Mga Update sa Dependency

- In-update ang `hono` sa 4.12.12 sa maraming packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- In-update ang `@hono/node-server` mula 1.19.11 hanggang 1.19.13 sa mga TypeScript packages
- In-update ang `cryptography` mula 46.0.5 hanggang 46.0.7 sa mga Python packages (10-StreamliningAIWorkflows labs 3 at 4)
- In-update ang `lodash` mula 4.17.23 hanggang 4.18.1 sa 10-StreamliningAIWorkflows inspector

#### Mga Pagsasalin

- Pinagsabay ang mga pagsasalin para sa 48+ na mga wika gamit ang pinakabagong mga pagbabago sa source (i18n update)

---

## Pebrero 5, 2026

### Pangkalahatang Pagpapatunay at Pagpapahusay sa Navigasyon ng Repository

#### Idinagdag na Bagong Nilalaman ng Kurikulum

**Module 03 - Pagsisimula**
- **12-mcp-hosts/README.md**: Bagong komprehensibong gabay para sa pagsasaayos ng MCP hosts
  - Mga halimbawa ng configuration para sa Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mga template ng JSON configuration para sa lahat ng pangunahing hosts
  - Talahanayan ng paghahambing ng mga uri ng transport (stdio, SSE/HTTP, WebSocket)
  - Pag-aayos sa mga karaniwang problema sa koneksyon
  - Pinakamahusay na mga gawi sa seguridad para sa pagsasaayos ng host

- **13-mcp-inspector/README.md**: Bagong gabay sa debugging para sa MCP Inspector
  - Mga paraan ng pag-install (npx, npm global, mula sa source)
  - Pagkonekta sa mga server gamit ang stdio at HTTP/SSE
  - Mga workflow para sa mga test tool, resources, at mga prompt
  - Integrasyon ng VS Code kasama ang MCP Inspector
  - Mga karaniwang senaryo ng debugging at mga solusyon

**Module 04 - Praktikal na Implementasyon**
- **pagination/README.md**: Bagong gabay sa implementasyon ng pagination
  - Mga pattern ng cursor-based pagination sa Python, TypeScript, Java
  - Pag-handle ng client-side pagination
  - Mga diskarte sa disenyo ng cursor (opaque vs. structured)
  - Mga rekomendasyon para sa pag-optimize ng performance

**Module 05 - Mga Advanced na Paksa**
- **mcp-protocol-features/README.md**: Bagong malalim na pagtalakay sa mga tampok ng protocol
  - Implementasyon ng mga notipikasyon ng progreso
  - Mga pattern ng kanselasyon ng kahilingan
  - Mga template ng resource na may mga pattern ng URI
  - Pamamahala ng lifecycle ng server
  - Kontrol ng antas ng logging
  - Mga pattern ng paghawak ng error gamit ang mga JSON-RPC code

#### Mga Pag-aayos sa Navigasyon (24+ na mga file ang na-update)

**Pangunahing Mga README ng Module**
 Ngayon ay may mga link sa parehong unang aralin AT susunod na module

**Mga Sub-file ng 02-Security**
- Lahat ng 5 supplement na dokumento sa seguridad ay may "Ano ang Susunod" na navigasyon:

**Mga File ng 09-CaseStudy**
- Lahat ng case study files ay may magkakasunod na navigasyon:

**10-StreamliningAI Labs**
Idinagdag ang seksyong Ano ang Susunod sa pangkalahatang-ideya ng Module 10 at Module 11

#### Mga Pag-aayos sa Code at Nilalaman

**SDK at Mga Update sa Dependency**
Naayos ang walang laman na bersyon ng openai sa `^4.95.0`
In-update ang SDK mula sa `^1.8.0` hanggang `>=1.26.0`
In-update ang mga ipinatong bersyon ng mcp sa `>=1.26.0`

**Mga Pag-aayos sa Code**
Naayos ang invalid na modelo `gpt-4o-mini` sa `gpt-4.1-mini`

**Mga Pag-aayos sa Nilalaman**
Naayos ang sirang link `READMEmd` → `README.md`, naayos ang header ng kurikulum `Module 1-3` → `Module 0-3`, naayos ang case-sensitive na path
Tinanggal ang korap na duplicated na nilalaman ng Case Study 5

**Pagsasaayos sa Patnubay para sa Mga Baguhan**
Idinagdag ang tamang pagpapakilala, mga layunin sa pagkatuto, at mga kinakailangan para sa mga baguhan

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang mga entry 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) sa talahanayan ng kurikulum

**Mga README ng Module**
Idinagdag ang mga aralin 12 at 13 sa listahan ng mga aralin
Idinagdag ang seksyon ng Praktikal na Mga Gabay na may link sa pagination
Idinagdag ang mga aralin 5.15 (Custom Transport) at 5.16 (Protocol Features)

**study_guide.md**
- Na-update ang mindmap na may lahat ng bagong paksa: MCP Hosts Setup, MCP Inspector, Mga Diskarte sa Pagination, Malalim na Pagtalakay sa Mga Tampok ng Protocol

## Enero 28, 2026

### MCP Specification 2025-11-25 Pagsusuri sa Pagsunod

#### Pagpapahusay ng Mga Pangunahing Konsepto (01-CoreConcepts/)
- **Bagong Primitive ng Kliyente - Roots**: Idinagdag ang komprehensibong dokumentasyon tungkol sa Roots client primitive, na nagpapahintulot sa mga server na maunawaan ang mga hangganan ng filesystem at mga permiso sa pag-access
- **Mga Anotasyon sa Tool**: Idinagdag ang dokumentasyon tungkol sa mga anotasyon sa pag-uugali ng tool (`readOnlyHint`, `destructiveHint`) para sa mas mahusay na mga desisyon sa pagtakbo ng tool
- **Pagtawag sa Tool sa Sampling**: Na-update ang dokumentasyon ng Sampling upang isama ang mga parameter na `tools` at `toolChoice` para sa model-driven na pagtawag sa tool sa mga kahilingan sa sampling
- **URL Mode Elicitation**: Idinagdag ang dokumentasyon tungkol sa URL-based elicitation para sa server-initiated external web interactions
- **Mga Tasks (Eksperimento)**: Idinagdag ang bagong seksyon na nagdodokumento sa eksperimento ng Tasks feature para sa durable execution wrappers at deferred result retrieval
- **Suporta sa Mga Icon**: Tinala na ang mga tool, resources, mga template ng resource, at mga prompt ay maaari nang maglaman ng mga icon bilang dagdag na metadata

#### Mga Update sa Dokumentasyon
- **README.md**: Idinagdag ang sanggunian sa bersyon ng MCP Specification 2025-11-25 at paliwanag sa versioning batay sa petsa
- **study_guide.md**: Na-update ang curriculum map upang isama ang Tasks at Tool Annotations sa seksyon ng Core Concepts; na-update ang timestamp ng dokumento

#### Pagpapatunay ng Pagsunod sa Specification
- **Bersyon ng Protocol**: Tiniyak ang lahat ng dokumentasyon na sumasalamin sa kasalukuyang MCP Specification 2025-11-25
- **Pagkakatugma ng Arkitektura**: Kinumpirma ang dokumentasyon ng dalawang-layer na arkitektura (Data Layer + Transport Layer)
- **Dokumentasyon ng Mga Primitive**: Napatunayan ang server primitives (Resources, Prompts, Tools) at client primitives (Sampling, Elicitation, Logging, Roots)
- **Mga Mekanismo sa Transport**: Napatunayan ang katumpakan ng dokumentasyon para sa STDIO at Streamable HTTP transport
- **Patnubay sa Seguridad**: Kinumpirma ang pagkakatugma sa kasalukuyang MCP Security Best Practices na dokumentasyon

#### Mga Pangunahing Tampok ng MCP 2025-11-25 na Naidokumento
- **OpenID Connect Discovery**: Pagdiskubre ng auth server sa pamamagitan ng OIDC
- **OAuth Client ID Metadata Documents**: Inirerekomendang mekanismo ng pagpaparehistro ng kliyente
- **JSON Schema 2020-12**: Default na diyalekto para sa mga MCP schema definition
- **SDK Tiering System**: Pormal na ipinahayag ang mga kinakailangan para sa suporta at pagpapanatili ng mga tampok ng SDK
- **Istruktura ng Pamamahala**: Pormal na ipinahayag ang mga Working Group at Interest Group sa pamamahala ng MCP

### Malaking Update sa Dokumentasyon ng Seguridad (02-Security/)

#### Integrasyon ng MCP Security Summit Workshop (Sherpa)
- **Bagong Hands-On Training Resource**: Idinagdag ang komprehensibong integrasyon sa [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) sa buong dokumentasyon ng seguridad
- **Saklaw ng Ruta ng Expedition**: Naidokumento ang kumpletong progreso mula Base Camp hanggang sa Summit
- **Pagkakatugma sa OWASP**: Lahat ng patnubay sa seguridad ay naka-mapa ngayon sa mga panganib ng OWASP MCP Azure Security Guide

#### Integrasyon ng OWASP MCP Top 10
- **Bagong Seksyon**: Idinagdag ang talahanayan ng OWASP MCP Top 10 Security Risks na may mga mitigasyon sa Azure sa pangunahing Security README
- **Dokumentasyon na Batay sa Panganib**: Na-update ang mcp-security-controls-2025.md kasama ang mga sanggunian sa panganib ng OWASP MCP para sa bawat domain ng seguridad
- **Reference Architecture**: Nakalink sa OWASP MCP Azure Security Guide reference architecture at mga pattern ng implementasyon

#### Na-update na Mga File sa Seguridad
- **README.md**: Idinagdag ang Sherpa Workshop overview, talahanayan ng ruta ng expedition, buod ng panganib ng OWASP MCP Top 10, at seksyon para sa hands-on training
- **mcp-security-controls-2025.md**: Na-update ang header hanggang Pebrero 2026, idinagdag ang mga sanggunian sa panganib ng OWASP (MCP01-MCP08), naayos ang hindi pagkakatugma sa bersyon ng spec
- **mcp-security-best-practices-2025.md**: Idinagdag ang seksyon ng mga resources ng Sherpa at OWASP, na-update ang timestamp
- **mcp-best-practices.md**: Idinagdag ang seksyon para sa hands-on training na may mga link sa Sherpa at OWASP
- **azure-content-safety-implementation.md**: Idinagdag ang sanggunian sa OWASP MCP06, pagkakatugma sa Sherpa Camp 3, at karagdagang seksyon ng mga resources

#### Idinagdag na Mga Link sa Resource
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Indibidwal na mga pahina ng panganib ng OWASP MCP (MCP01-MCP10)

### Pangkalahatang Pag-ayon sa MCP Specification ng Kurikulum 2025-11-25

#### Module 03 - Pagsisimula
- **SDK Documentation**: Idinagdag ang Go SDK sa opisyal na listahan ng SDK; in-update ang lahat ng mga sanggunian ng SDK upang umayon sa MCP Specification 2025-11-25
- **Transport Clarification**: In-update ang mga paglalarawan ng STDIO at HTTP Streaming transport na may mga tiyak na sanggunian sa spec

#### Module 04 - Praktikal na Implementasyon
- **SDK Updates**: Idinagdag ang Go SDK; in-update ang listahan ng SDK kasama ang sanggunian sa bersyon ng specification
- **Authorization Spec**: In-update ang MCP Authorization specification link sa kasalukuyang bersyon ng 2025-11-25

#### Module 05 - Mga Advanced na Paksa
- **New Features**: Idinagdag ang tala tungkol sa mga bagong feature ng MCP Specification 2025-11-25 (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Security Resources**: Idinagdag ang OWASP MCP Top 10 at Sherpa workshop na mga link sa karagdagang mga reperensiya

#### Module 06 - Mga Kontribusyon ng Komunidad
- **SDK List**: Idinagdag ang Swift at Rust SDKs; in-update ang sanggunian ng specification sa 2025-11-25
- **Spec Reference**: In-update ang MCP Specification link sa direktang URL ng specification

#### Module 07 - Mga Aral mula sa Maagang Pagtanggap
- **Resource Updates**: Idinagdag ang MCP Specification 2025-11-25 na link at OWASP MCP Top 10 sa mga karagdagang mapagkukunan

#### Module 08 - Mga Pinakamahusay na Praktis
- **Spec Version**: In-update ang MCP Specification reference sa 2025-11-25
- **Security Resources**: Idinagdag ang OWASP MCP Top 10 at Sherpa workshop sa mga karagdagang reperensiya

#### Module 10 - Pagpapadali ng mga AI Workflow
- **Badge Update**: Binago ang MCP version badge mula sa SDK version (1.9.3) sa specification version (2025-11-25)
- **Resource Links**: In-update ang MCP Specification link; idinagdag ang OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec Reference**: In-update ang MCP Specification link sa bersyon ng 2025-11-25
- **Security Resources**: Idinagdag ang OWASP MCP Top 10 sa opisyal na mga mapagkukunan

## Disyembre 18, 2025

### Update ng Dokumentasyon sa Seguridad - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Pag-update ng Bersyon ng Specification
- **Protocol Version Update**: In-update upang ituro ang pinakabagong MCP Specification 2025-11-25 (ipinakilala noong Nobyembre 25, 2025)
  - In-update ang lahat ng bersyon ng sanggunian ng specification mula 2025-06-18 hanggang 2025-11-25
  - In-update ang mga sanggunian ng petsa ng dokumento mula Agosto 18, 2025 hanggang Disyembre 18, 2025
  - Na-verify na lahat ng mga URL ng specification ay tumuturo sa kasalukuyang dokumentasyon
- **Content Validation**: Komprehensibong beripikasyon ng mga pinakamahusay na praktis sa seguridad laban sa pinakabagong mga pamantayan
  - **Microsoft Security Solutions**: Na-verify ang kasalukuyang termino at mga link para sa Prompt Shields (dating "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, at Azure Key Vault
  - **OAuth 2.1 Security**: Nakumpirma ang pagsunod sa pinakahuling OAuth security best practices
  - **OWASP Standards**: Na-validate na ang OWASP Top 10 para sa LLMs ay nananatiling napapanahon
  - **Azure Services**: Na-verify ang lahat ng mga link sa dokumentasyon ng Microsoft Azure at pinakamahusay na mga praktis
- **Standards Alignment**: Lahat ng mga tinutukoy na pamantayan sa seguridad ay nakumpirma na napapanahon
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security at compliance frameworks
- **Implementation Resources**: Na-validate ang lahat ng mga link at mapagkukunan ng gabay para sa implementasyon
  - Azure API Management authentication patterns
  - Mga gabay sa integrasyon ng Microsoft Entra ID
  - Pamamahala ng sikreto gamit ang Azure Key Vault
  - DevSecOps pipelines at mga solusyon sa pagmamanman

### Pagsisiguro sa Kalidad ng Dokumentasyon
- **Specification Compliance**: Tiniyak na lahat ng kailangan sa MCP security (MUST/MUST NOT) ay umaayon sa pinakabagong specification
- **Resource Currency**: Na-verify ang lahat ng panlabas na link sa dokumentasyon ng Microsoft, mga pamantayan sa seguridad, at mga gabay sa implementasyon
- **Best Practices Coverage**: Nakumpirma ang malawakang saklaw ng authentication, authorization, mga banta na partikular sa AI, seguridad ng supply chain, at mga pattern sa enterprise

## Oktubre 6, 2025

### Pagpapalawak ng Seksyon ng Pagsisimula – Advanced Server Usage at Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **Bagong Kabanata Idinagdag**: Inilunsad ang komprehensibong gabay sa advanced na paggamit ng MCP server, na sumasaklaw sa regular at low-level na mga arkitektura ng server.
  - **Regular vs. Low-Level Server**: Detalyadong paghahambing at mga halimbawa ng code sa Python at TypeScript para sa parehong mga pamamaraan.
  - **Handler-Based Design**: Paliwanag ng handler-based na pamamahala ng tool/resource/prompt para sa scalable at flexible na mga implementasyon ng server.
  - **Praktikal na mga Pattern**: Mga totoong sitwasyon kung saan kapaki-pakinabang ang mga low-level na pattern ng server para sa advanced na mga feature at arkitektura.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **Bagong Kabanata Idinagdag**: Hakbang-hakbang na gabay sa pagpapatupad ng simpleng authentication sa mga MCP server.
  - **Mga Konsepto ng Auth**: Malinaw na paliwanag ng authentication kumpara sa authorization, at pamamahala ng mga kredensyal.
  - **Pangunahing Implementasyon ng Auth**: Middleware-based na mga authentication pattern sa Python (Starlette) at TypeScript (Express), kasama ang mga sample na code.
  - **Pag-unlad patungo sa Advanced Security**: Gabay sa pagsisimula sa simple auth at pag-usad patungo sa OAuth 2.1 at RBAC, na may mga reperensiya sa mga advanced na module ng seguridad.

Ang mga karagdagang ito ay nagbibigay ng praktikal at aktwal na gabay sa paggawa ng mas matatag, ligtas, at flexible na mga implementasyon ng MCP server, na pinag-uugnay ang mga pundamental na konsepto sa mga advanced na pattern sa produksyon.

## Setyembre 29, 2025

### MCP Server Database Integration Labs - Komprehensibong Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - Bagong Kompletong Kurrikulum ng Database Integration
- **Kompletong 13-Lab Learning Path**: Idinagdag ang komprehensibong hands-on na kurikulum para sa paggawa ng production-ready MCP servers na may PostgreSQL database integration
  - **Tunay na Implementasyon**: Zava Retail analytics use case na nagpapakita ng mga pattern para sa antas ng enterprise
  - **Structured Learning Progression**:
    - **Labs 00-03: Mga Pundasyon** - Panimula, Core Architecture, Seguridad at Multi-Tenancy, Pagsasaayos ng Kapaligiran
    - **Labs 04-06: Pagtatatag ng MCP Server** - Disenyo ng Database at Schema, Implementasyon ng MCP Server, Pagpapaunlad ng Tool  
    - **Labs 07-09: Mga Advanced na Tampok** - Semantic Search Integration, Pagsusuri at Pagde-debug, VS Code Integration
    - **Labs 10-12: Produksyon at Pinakamahusay na Praktis** - Mga Estratehiya ng Deployment, Pagmamanman at Observability, Pinakamahusay na Praktis at Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL gamit ang pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Mga Advanced na Tampok**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Pag-convert ng Module sa Lab
- **Komprehensibong Pag-update ng Dokumentasyon**: Sistematikong in-update ang lahat ng README files sa 11-MCPServerHandsOnLabs upang gamitin ang terminong "Lab" sa halip na "Module"
  - **Mga Header ng Seksyon**: In-update ang "What This Module Covers" sa "What This Lab Covers" sa lahat ng 13 labs
  - **Paglalarawan ng Nilalaman**: Pinalitan ang "This module provides..." ng "This lab provides..." sa buong dokumentasyon
  - **Mga Layunin sa Pag-aaral**: In-update ang "By the end of this module..." sa "By the end of this lab..."
  - **Mga Link sa Navigasyon**: Kinonvert ang lahat ng "Module XX:" references sa "Lab XX:" sa mga cross-references at navigasyon
  - **Pagsubaybay sa Pagtatapos**: In-update ang "After completing this module..." sa "After completing this lab..."
  - **Napanatili ang Teknikal na Reperensiya**: Pinanatili ang mga reperensiya ng module ng Python sa mga configuration file (hal., `"module": "mcp_server.main"`)

#### Pagpapahusay ng Study Guide (study_guide.md)
- **Visual Curriculum Map**: Idinagdag ang bagong seksyong "11. Database Integration Labs" na may komprehensibong visualisasyon ng estruktura ng lab
- **Estruktura ng Repositoryo**: In-update mula sampu hanggang labing-isang pangunahing seksyon na may detalyadong paglalarawan ng 11-MCPServerHandsOnLabs
- **Gabayan sa Learning Path**: Pinahusay ang mga tagubilin sa navigasyon para sa mga seksyon 00-11
- **Saklaw ng Teknolohiya**: Idinagdag ang mga detalye ng FastMCP, PostgreSQL, at integrasyon ng mga serbisyo ng Azure
- **Mga Kinalabasan ng Pag-aaral**: Binigyang-diin ang produksyon-ready na pagbuo ng server, mga pattern ng database integration, at seguridad ng enterprise

#### Pagpapahusay ng Main README Estruktura
- **Terminolohiya batay sa Lab**: In-update ang pangunahing README.md sa 11-MCPServerHandsOnLabs upang palagianang gamitin ang "Lab" na estruktura
- **Organisasyon ng Learning Path**: Malinaw na progreso mula pundamental na mga konsepto hanggang sa advanced na implementasyon at deployment sa produksyon
- **Tumutok sa Tunay na Mundo**: Binigyang-diin ang praktikal na hands-on na pag-aaral gamit ang mga pattern at teknolohiya ng antas ng enterprise

### Mga Pagpapahusay sa Kalidad at Konsistensi ng Dokumentasyon
- **Pagtutok sa Hands-On Learning**: Pinagtibay ang praktikal na lab-based na pamamaraan sa buong dokumentasyon
- **Tumutok sa Mga Pattern ng Enterprise**: Binanggit ang mga produksyon-ready na implementasyon at mga konsiderasyon sa seguridad ng enterprise
- **Integrasyon ng Teknolohiya**: Komprehensibong saklaw ng modernong mga serbisyo ng Azure at mga pattern ng AI integration
- **Pag-unlad sa Pag-aaral**: Malinaw at estrukturadong landas mula sa mga pangunahing konsepto hanggang sa deployment sa produksyon

## Setyembre 26, 2025

### Pagpapahusay ng Case Studies - Integrasyon ng GitHub MCP Registry

#### Case Studies (09-CaseStudy/) - Pagtuon sa Pag-unlad ng Ecosystem
- **README.md**: Malawakang pagpapalawak na may komprehensibong case study ng GitHub MCP Registry
  - **GitHub MCP Registry Case Study**: Bagong komprehensibong case study na sinusuri ang paglulunsad ng GitHub MCP Registry noong Setyembre 2025
    - **Pagsusuri ng Problema**: Detalyadong pagsusuri ng pira-pirasong MCP server discovery at mga hamon sa deployment
    - **Arkitektura ng Solusyon**: Centralized registry approach ng GitHub na may one-click VS Code installation
    - **Epekto sa Negosyo**: Masusukat na pagpapabuti sa onboarding at produktibidad ng mga developer
    - **Estratehikong Halaga**: Pagtuon sa modular na deployment ng agent at interoperability sa pagitan ng mga tool
    - **Pag-unlad ng Ecosystem**: Posisyon bilang pundasyong platform para sa agentic integration
  - **Pinahusay na Estruktura ng Case Study**: In-update ang lahat ng pitong case study sa pare-parehong pormat at komprehensibong mga paglalarawan
    - Azure AI Travel Agents: Pagtuon sa multi-agent orchestration
    - Azure DevOps Integration: Pagtuon sa workflow automation
    - Real-Time Documentation Retrieval: Implementasyon ng python console client
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: Integrasyon ng VS Code at GitHub Copilot
    - Azure API Management: Mga pattern ng enterprise API integration
    - GitHub MCP Registry: Pag-unlad ng ecosystem at platform ng komunidad
  - **Komprehensibong Konklusyon**: Mulit-ulit na sinulat na seksyon ng konklusyon na tumatalakay sa pitong case study na sumasaklaw sa maraming dimensyon ng MCP implementasyon
    - Enterprise Integration, Multi-Agent Orchestration, Produktibidad ng Developer
    - Pag-unlad ng Ecosystem, Kategorya ng Mga Aplikasyon sa Edukasyon
    - Pinahusay na mga insight sa mga pattern ng arkitektura, mga estratehiya ng implementasyon, at mga pinakamahusay na praktis
    - Pagtuon sa MCP bilang mature at production-ready na protocol

#### Mga Update sa Study Guide (study_guide.md)
- **Visual Curriculum Map**: In-update ang mindmap upang isama ang GitHub MCP Registry sa seksyon ng Case Studies
- **Paglalarawan ng Case Studies**: Pinaganda mula sa pangkalahatang paglalarawan hanggang sa detalyadong breakdown ng pitong komprehensibong case studies
- **Estruktura ng Repositoryo**: In-update ang seksyon 10 upang ipakita ang komprehensibong saklaw ng case study na may mga tiyak na detalye sa implementasyon
- **Changelog Integration**: Idinagdag ang tala ng Setyembre 26, 2025 na nagdodokumento ng pagdagdag ng GitHub MCP Registry at pagpapahusay ng case studies
- **Mga Update sa Petsa**: In-update ang footer timestamp upang ipakita ang pinakabagong rebisyon (Setyembre 26, 2025)

### Mga Pagpapahusay sa Kalidad ng Dokumentasyon
- **Pagpapahusay ng Konsistensi**: Standardisadong pormat at estruktura ng case study sa lahat ng pitong halimbawa
- **Komprehensibong Saklaw**: Ang mga case study ay sumasaklaw na ngayon sa mga eksena ng enterprise, produktibidad ng developer, at pag-unlad ng ecosystem
- **Estrategikong Posisyon**: Pinahusay ang pagtutok sa MCP bilang pundasyong platform para sa deployment ng mga agentic system
- **Integrasyon ng Reperensiya**: In-update ang mga karagdagang reperensiya upang isama ang link sa GitHub MCP Registry

## Setyembre 15, 2025

### Pagpapalawak ng Mga Advanced na Paksa - Custom Transports at Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Bagong Gabay sa Advanced na Implementasyon
- **README.md**: Kompletong gabay sa implementasyon para sa mga custom na mekanismo ng transport ng MCP
  - **Azure Event Grid Transport**: Komprehensibong implementasyon ng serverless na event-driven transport
    - Mga halimbawa sa C#, TypeScript, at Python na may integrasyon ng Azure Functions
    - Mga pattern ng event-driven architecture para sa scalable na mga solusyon ng MCP
    - Mga tumatanggap ng webhook at push-based na paghawak ng mensahe
  - **Azure Event Hubs Transport**: Mataas na throughput na streaming transport implementation
    - Real-time streaming na kakayahan para sa mga senaryo na may mababang latency
    - Mga estratehiya sa pag-partition at pamamahala ng checkpoint
    - Pagsasama-sama ng mga mensahe at pag-optimize ng performance
  - **Enterprise Integration Patterns**: Mga halimbawa ng arkitekturang handa para sa produksyon
    - Distributed na pagproseso ng MCP gamit ang maramihang Azure Functions
    - Hybrid na arkitektura ng transport na pinagsasama ang maramihang uri ng transport
    - Mga estratehiya para sa tibay ng mensahe, pagiging maaasahan, at paghawak ng error
  - **Security & Monitoring**: Integrasyon ng Azure Key Vault at mga pattern ng observability
    - Managed identity authentication at access na may pinakamababang pribilehiyo
    - Telemetriya sa Application Insights at pagmamanman ng performance
    - Mga circuit breakers at pattern ng fault tolerance
  - **Testing Frameworks**: Komprehensibong mga estratehiya sa pagsusuri para sa mga custom transport
    - Unit testing gamit ang test doubles at mocking frameworks
    - Integration testing gamit ang Azure Test Containers
    - Mga pagsasaalang-alang sa performance at load testing

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Lumilitaw na Disiplina ng AI
- **README.md**: Komprehensibong pagsisiyasat sa context engineering bilang umuusbong na larangan
  - **Pangunahing Prinsipyo**: Kumpletong pagbabahagi ng konteksto, kamalayan sa pagpapasya ng aksyon, at pamamahala ng context window

  - **Pag-align sa MCP Protocol**: Paano tinutugunan ng disenyo ng MCP ang mga hamon sa context engineering
    - Mga limitasyon sa context window at mga estratehiya sa progressive loading
    - Pagtukoy ng kaugnayan at dynamic na retrieval ng context
    - Paghawak ng multi-modal context at mga konsiderasyon sa seguridad
  - **Mga Pamamaraan sa Implementasyon**: Single-threaded kumpara sa multi-agent na arkitektura
    - Mga teknik sa pagchunk at pag-prioritize ng context
    - Progressive context loading at mga estratehiya sa compression
    - Mga layered na pamamaraan sa context at optimisasyon sa retrieval
  - **Balangkas sa Pagsusukat**: Mga umuusbong na metriko para sa ebalwasyon ng bisa ng context
    - Mga konsiderasyon sa input efficiency, performance, kalidad, at karanasan ng gumagamit
    - Mga eksperimento sa mga pamamaraan ng optimisasyon ng context
    - Pagsusuri sa pagkabigo at mga metodolohiya sa pagpapabuti

#### Mga Pag-update sa Pag-navigate ng Kurikulum (README.md)
- **Pinalawak na Estruktura ng Module**: Na-update na talahanayan ng kurikulum upang isama ang mga bagong advanced na paksa
  - Idinagdag ang Context Engineering (5.14) at Custom Transport (5.15) na mga entry
  - Konsistenteng pag-format at mga link sa pag-navigate sa lahat ng module
  - Na-update na mga paglalarawan upang ipakita ang kasalukuyang saklaw ng nilalaman

### Mga Pagbuti sa Estruktura ng Direktoryo
- **Standardisasyon ng Pangalan**: Pinalitan ang "mcp transport" ng "mcp-transport" para sa pagkakaugnay sa ibang mga folder ng mga advanced na paksa
- **Organisasyon ng Nilalaman**: Lahat ng 05-AdvancedTopics na mga folder ay sumusunod na sa konsistenteng pattern ng pangalan (mcp-[topic])

### Mga Pagpapahusay sa Kalidad ng Dokumentasyon
- **Pag-align sa MCP Specification**: Lahat ng bagong nilalaman ay tumutukoy sa kasalukuyang MCP Specification 2025-06-18
- **Mga Halimbawa sa Maraming Wika**: Komprehensibong mga code example sa C#, TypeScript, at Python
- **Pokus sa Enterprise**: Mga pattern na handa sa produksyon at integrasyon sa Azure cloud sa kabuuan
- **Visual na Dokumentasyon**: Mga diagram ng Mermaid para sa arkitektura at pagsasalarawan ng daloy

## Agosto 18, 2025

### Komprehensibong Pag-update ng Dokumentasyon - Mga Pamantayan ng MCP 2025-06-18

#### Pinakamahusay na Praktis sa Seguridad ng MCP (02-Security/) - Kumpletong Modernisasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Kumpletong muling pagsulat na naka-align sa MCP Specification 2025-06-18
  - **Mga Mandatoryong Kailangan**: Idinagdag ang malinaw na MUST/MUST NOT mga kinakailangan mula sa opisyal na espesipikasyon na may malinaw na visual na indikasyon
  - **12 Pangunahing Praktis sa Seguridad**: Muling inayos mula sa 15-item na listahan patungo sa komprehensibong mga domain ng seguridad
    - Seguridad sa Token at Pagpapatunay ng pagkakakilanlan na may integrasyon ng external na identity provider
    - Pamamahala ng Session at Seguridad ng Transport na may mga kinakailangan sa cryptographic
    - Proteksyon sa AI-Specific Threat na may integrasyon ng Microsoft Prompt Shields
    - Kontrol sa Access at mga Pahintulot na may prinsipyo ng pinakamababang pribilehiyo
    - Kaligtasan ng Nilalaman at Pagsubaybay na may integrasyon ng Azure Content Safety
    - Seguridad sa Supply Chain na may komprehensibong beripikasyon ng mga bahagi
    - Seguridad sa OAuth at Pag-iwas sa Confused Deputy na may implementasyon ng PKCE
    - Pagtugon sa Insidente at Pag-recover na may mga automated na kakayahan
    - Pagsunod at Pamamahala na may pag-align sa regulasyon
    - Mga Advanced na Kontrol sa Seguridad na may zero trust na arkitektura
    - Integrasyon sa Ecosystem ng Seguridad ng Microsoft na may komprehensibong mga solusyon
    - Patuloy na Pag-unlad sa Seguridad na may mga adaptive na praktis
  - **Mga Solusyon sa Seguridad ng Microsoft**: Pinahusay na gabay sa integrasyon para sa Prompt Shields, Azure Content Safety, Entra ID, at GitHub Advanced Security
  - **Mga Mapagkukunan sa Implementasyon**: Naka-kategorya ang komprehensibong mga link ng mapagkukunan ayon sa Opisyal na Dokumentasyon ng MCP, Mga Solusyon sa Seguridad ng Microsoft, Mga Pamantayan sa Seguridad, at Mga Gabay sa Implementasyon

#### Mga Advanced na Kontrol sa Seguridad (02-Security/) - Enterprise na Implementasyon
- **MCP-SECURITY-CONTROLS-2025.md**: Kumpletong pagbago gamit ang enterprise-grade na balangkas sa seguridad
  - **9 Komprehensibong Domain ng Seguridad**: Pinalawak mula sa mga pangunahing kontrol patungo sa detalyadong balangkas para sa enterprise
    - Advanced na Pagpapatunay at Awtorisasyon na may integrasyon ng Microsoft Entra ID
    - Seguridad sa Token at Anti-Passthrough na mga kontrol na may komprehensibong beripikasyon
    - Mga kontrol sa seguridad ng session na may pag-iwas sa pag-hijack
    - AI-Specific na mga kontrol sa seguridad na may pag-iwas sa prompt injection at pang-aalipusta ng tool
    - Pag-iwas sa Confused Deputy Attack na may seguridad sa OAuth proxy
    - Seguridad sa Pagpapatakbo ng Tool na may sandboxing at isolation
    - Mga kontrol sa seguridad ng Supply Chain na may beripikasyon ng dependency
    - Mga kontrol sa Pagsubaybay at Pagtuklas na may integrasyon ng SIEM
    - Pagtugon sa Insidente at Pag-recover na may mga automated na kakayahan
  - **Mga Halimbawa sa Implementasyon**: Idinagdag ang detalyadong mga YAML configuration block at mga halimbawa ng code
  - **Integrasyon ng Microsoft Solutions**: Komprehensibong saklaw ng Azure security services, GitHub Advanced Security, at enterprise identity management

#### Seguridad sa Mga Advanced na Paksa (05-AdvancedTopics/mcp-security/) - Handang Implementasyon para sa Produksyon
- **README.md**: Kumpletong muling pagsulat para sa enterprise security implementation
  - **Pag-align sa Kasalukuyang Espesipikasyon**: Na-update sa MCP Specification 2025-06-18 na may mga mandatoryong kinakailangan sa seguridad
  - **Pinahusay na Pagpapatunay**: Integrasyon ng Microsoft Entra ID na may komprehensibong mga halimbawa sa .NET at Java Spring Security
  - **Integrasyon sa AI Security**: Implementasyon ng Microsoft Prompt Shields at Azure Content Safety na may detalyadong halimbawa sa Python
  - **Advanced na Pagtatanggol sa Banta**: Komprehensibong mga halimbawa ng implementasyon para sa
    - Pag-iwas sa Confused Deputy Attack gamit ang PKCE at beripikasyon ng pahintulot ng gumagamit
    - Pag-iwas sa Token Passthrough gamit ang beripikasyon ng audience at ligtas na pamamahala ng token
    - Pag-iwas sa Session Hijacking gamit ang cryptographic binding at pagsusuri ng gawi
  - **Integrasyon sa Seguridad ng Enterprise**: Pagsubaybay gamit ang Azure Application Insights, mga pipeline ng pagtuklas ng banta, at seguridad ng supply chain
  - **Checklist sa Implementasyon**: Malinaw na pagkakaiba ng mga mandatoryo vs. inirerekomendang kontrol sa seguridad na may mga benepisyo mula sa ecosystem ng seguridad ng Microsoft

### Kalidad ng Dokumentasyon at Pag-align sa Pamantayan
- **Mga Sanggunian sa Espesipikasyon**: Na-update lahat ng mga sanggunian sa kasalukuyang MCP Specification 2025-06-18
- **Ecosystem ng Seguridad ng Microsoft**: Pinahusay ang gabay sa integrasyon sa kabuuan ng lahat ng dokumentasyon sa seguridad
- **Praktikal na Implementasyon**: Idinagdag ang detalyadong mga halimbawa ng code sa .NET, Java, at Python na may mga pattern para sa enterprise
- **Organisasyon ng Mga Mapagkukunan**: Komprehensibong pag-uuri ng opisyal na dokumentasyon, mga pamantayan sa seguridad, at gabay sa implementasyon
- **Visual na mga Indikador**: Malinaw na pagkaka-mark ng mga mandatoryong kinakailangan kumpara sa mga inirerekomendang praktis


#### Mga Pangunahing Konsepto (01-CoreConcepts/) - Kumpletong Modernisasyon
- **Pag-update ng Bersyon ng Protocol**: Na-update upang tumukoy sa kasalukuyang MCP Specification 2025-06-18 na may petsa-based na bersyon (YYYY-MM-DD format)
- **Pagpapahusay sa Arkitektura**: Pinahusay na paglalarawan ng Hosts, Clients, at Servers upang ipakita ang kasalukuyang mga pattern ng arkitektura ng MCP
  - Ang mga Hosts ay malinaw na tinukoy bilang mga AI application na nakikipag-coordinate ng maraming MCP client connections
  - Ang mga Clients ay inilalarawan bilang mga protocol connector na nagpapanatili ng one-to-one na ugnayan sa server
  - Ang mga Servers ay pinalawak ang mga senaryo ng lokal kumpara sa remote na deployment
- **Pagbabago sa Mga Primitive**: Kumpletong overhaul ng mga server at client primitives
  - Mga Server Primitives: Mga Resources (mga pinagkukunan ng data), Prompts (mga template), Tools (mga executable na function) na may detalyadong paliwanag at mga halimbawa
  - Mga Client Primitives: Sampling (mga LLM completion), Elicitation (input ng gumagamit), Logging (debugging/pagsubaybay)
  - Na-update gamit ang kasalukuyang mga discovery (`*/list`), retrieval (`*/get`), at execution (`*/call`) na mga pattern ng metodo
- **Arkitektura ng Protocol**: Ipinakilala ang modelo ng dalawang-layer na arkitektura
  - Data Layer: Foundation ng JSON-RPC 2.0 na may lifecycle management at mga primitive
  - Transport Layer: STDIO (lokal) at Streamable HTTP na may SSE (remote) na mga mekanismo ng transport
- **Balangkas sa Seguridad**: Komprehensibong mga prinsipyo sa seguridad kasama ang maliwanag na pahintulot ng gumagamit, proteksyon sa privacy ng data, kaligtasan sa pagpapatakbo ng tool, at seguridad ng transport layer
- **Mga Pattern sa Komunikasyon**: Na-update ang mga mensahe ng protocol upang ipakita ang mga daloy ng initialization, discovery, execution, at notification
- **Mga Halimbawa ng Code**: Na-refresh ang mga halimbawa sa maraming wika (.NET, Java, Python, JavaScript) upang ipakita ang kasalukuyang mga pattern ng MCP SDK

#### Seguridad (02-Security/) - Komprehensibong Pagbabago sa Seguridad  
- **Pag-align sa Pamantayan**: Buong pag-align sa mga kinakailangan sa seguridad ng MCP Specification 2025-06-18
- **Ebolusyon ng Pagpapatunay**: Naidokumento ang ebolusyon mula sa custom OAuth servers patungo sa delegasyon ng external identity provider (Microsoft Entra ID)
- **AI-Specific na Pagsusuri sa Banta**: Pinalawak na saklaw ng mga modernong vector ng atake sa AI
  - Detalyadong mga senaryo ng pag-atake sa prompt injection na may mga totoong halimbawa
  - Mga mekanismo ng tool poisoning at mga pattern ng "rug pull" attack
  - Pag-aalipusta sa context window at mga atake sa pagkalito ng modelo
- **Mga Solusyon sa Seguridad ng Microsoft AI**: Komprehensibong saklaw ng ecosystem ng seguridad ng Microsoft
  - AI Prompt Shields na may advanced detection, spotlighting, at mga teknik sa delimiter
  - Mga pattern ng integrasyon ng Azure Content Safety
  - GitHub Advanced Security para sa proteksyon ng supply chain
- **Advanced na Pagtatanggol sa Banta**: Detalyadong mga kontrol sa seguridad para sa
  - Pag-hijack ng session na may mga partikular na senaryo ng atake sa MCP at mga kinakailangan sa cryptographic session ID
  - Mga problema ng Confused deputy sa mga senaryo ng MCP proxy na may malinaw na mga kinakailangan sa pahintulot
  - Mga kahinaan sa token passthrough na may mandatoryong mga kontrol sa validation
- **Seguridad sa Supply Chain**: Pinalawak na saklaw ng AI supply chain kabilang ang mga foundation model, embedding services, context providers, at third-party API
- **Seguridad sa Foundation**: Pinahusay na integrasyon sa mga pattern ng enterprise security kabilang ang zero trust architecture at ecosystem ng seguridad ng Microsoft
- **Organisasyon ng Mapagkukunan**: Naka-kategorya ang komprehensibong mga link ng mapagkukunan ayon sa uri (Opisyal na Docs, Mga Pamantayan, Pananaliksik, Mga Solusyon ng Microsoft, Mga Gabay sa Implementasyon)

### Mga Pagpapahusay sa Kalidad ng Dokumentasyon
- **Istrakturang Mga Layunin sa Pagkatuto**: Pinahusay na mga layunin sa pagkatuto na may espesipiko at implementableng mga resulta 
- **Mga Cross-Reference**: Idinagdag ang mga link sa pagitan ng mga kaugnay na paksa sa seguridad at pangunahing konsepto
- **Kasalukuyang Impormasyon**: Na-update lahat ng mga sanggunian sa petsa at mga link ng espesipikasyon sa mga kasalukuyang pamantayan
- **Gabay sa Implementasyon**: Idinagdag ang mga espesipikong, implementableng mga gabay sa implementasyon sa parehong mga seksyon

## Hulyo 16, 2025

### Mga Pagpapahusay sa README at Pag-navigate
- Lubos na niredisenyo ang pag-navigate ng kurikulum sa README.md
- Pinalitan ang mga tag na `<details>` ng mas madaling gamitin na table-based na format
- Nilikha ang mga alternatibong opsyon sa layout sa bagong folder na "alternative_layouts"
- Idinagdag ang mga halimbawa ng card-based, tabbed-style, at accordion-style na pag-navigate
- Na-update ang seksyon ng repository structure upang isama ang lahat ng pinakabagong mga file
- Pinahusay ang seksyon ng "Paano Gamitin ang Kurikulum" na may malinaw na mga rekomendasyon
- Na-update ang mga link ng espesipikasyon ng MCP upang ituro sa tamang mga URL
- Idinagdag ang seksyon ng Context Engineering (5.14) sa estruktura ng kurikulum

### Mga Pag-update sa Gabay sa Pag-aaral
- Lubos na nirebisa ang gabay sa pag-aaral upang tumugma sa kasalukuyang estruktura ng repository
- Idinagdag ang mga bagong seksyon para sa MCP Clients at Tools, at Popular na MCP Servers
- Na-update ang Visual Curriculum Map upang tumpak na ipakita ang lahat ng mga paksa
- Pinahusay ang mga paglalarawan ng Mga Advanced na Paksa upang masaklaw ang lahat ng mga espesyalisadong larangan
- Na-update ang seksyon ng Case Studies upang ipakita ang mga aktwal na halimbawa
- Idinagdag ang komprehensibong changelog na ito

### Mga Ambag ng Komunidad (06-CommunityContributions/)
- Idinagdag ang detalyadong impormasyon tungkol sa mga MCP server para sa image generation
- Idinagdag ang komprehensibong seksyon sa paggamit ng Claude sa VSCode
- Idinagdag ang setup at mga tagubilin sa paggamit ng Cline terminal client
- Na-update ang seksyon ng MCP client upang isama ang lahat ng mga popular na client option
- Pinahusay ang mga halimbawa sa kontribusyon gamit ang mas tumpak na mga sample ng code

### Mga Advanced na Paksa (05-AdvancedTopics/)
- Inayos ang lahat ng mga specialized topic folder na may konsistenteng pangalan
- Idinagdag ang mga materyales at halimbawa sa context engineering
- Idinagdag ang dokumentasyon sa integrasyon ng Foundry agent
- Pinahusay ang dokumentasyon sa integrasyon ng seguridad ng Entra ID

## Hunyo 11, 2025

### Paunang Paggawa
- Inilabas ang unang bersyon ng MCP for Beginners na kurikulum
- Nilikhang batayang estruktura para sa lahat ng 10 pangunahing seksyon
- Ipinasok ang Visual Curriculum Map para sa pag-navigate
- Idinagdag ang paunang sample projects sa maraming programming languages

### Pagsisimula (03-GettingStarted/)
- Nilikhang unang mga halimbawa ng implementasyon ng server
- Idinagdag ang gabay sa pagbuo ng client
- Isinama ang mga tagubilin sa integrasyon ng LLM client
- Idinagdag ang dokumentasyon sa integrasyon ng VS Code
- Ipinasok ang mga halimbawa ng Server-Sent Events (SSE) na server

### Mga Pangunahing Konsepto (01-CoreConcepts/)
- Idinagdag ang detalyadong paliwanag ng client-server architecture
- Nilikhang dokumentasyon tungkol sa mga pangunahing bahagi ng protocol
- Nadukumento ang mga pattern ng messaging sa MCP

## Mayo 23, 2025

### Estruktura ng Repositoryo
- Inilunsad ang repositoryo gamit ang batayang estruktura ng folder
- Nilikhang README files para sa bawat pangunahing seksyon
- Inilunsad ang imprastraktura sa pagsasalin
- Idinagdag ang mga larawang asset at diagram

### Dokumentasyon
- Nilikhang paunang README.md na may pangkalahatang-ideya ng kurikulum
- Idinagdag ang CODE_OF_CONDUCT.md at SECURITY.md
- Inilunsad ang SUPPORT.md na may gabay para sa paghingi ng tulong
- Nilikhang paunang estruktura ng gabay sa pag-aaral

## Abril 15, 2025

### Pagpaplano at Balangkas
- Paunang pagpaplano para sa MCP for Beginners na kurikulum
- Tinukoy ang mga layunin sa pagkatuto at target na tagapakinig
- Inilarawan ang estruktura ng 10-seksyon ng kurikulum
- Bumuo ng konseptuwal na balangkas para sa mga halimbawa at case studies
- Nilikhang mga paunang prototype na halimbawa para sa mga pangunahing konsepto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Changelog: MCP para sa mga Nagsisimula na Kurikulum

Ang dokumentong ito ay nagsisilbing talaan ng lahat ng mahahalagang pagbabago na ginawa sa Model Context Protocol (MCP) para sa mga Nagsisimula na kurikulum. Ang mga pagbabago ay idinokumento sa reverse chronological order (pinakabago muna).

## Setyembre 9, 2026

### MCP 2026-07-28 Panghuling Pagkakaayos ng Espesipikasyon

In-update ang English na kurikulum mula sa release-candidate at `2025-11-25`
baseline guidance papunta sa panghuling MCP `2026-07-28` na espesipikasyon.

- **In-update**: Mga sanggunian sa kasalukuyang bersyon, mga link ng espesipikasyon, gabay para sa stateless
  na kahilingan, `server/discover`, Streamable HTTP headers, at ang lifecycle ng Tasks
  extension sa loob ng 38 English na dokumento.
- **Naayos**: Ngayon ay gumagamit ang Elicitation ng `elicitation/create`, ang Sampling ay gumagamit ng
  `sampling/createMessage`, at ang `InputRequiredResult.resultType` ay gumagamit ng
  `"input_required"`.
- **Pinalitan**: Ang hindi tumpak na leksyon tungkol sa Root Context conversation-state ay pinalitan ng
  leksyong protocol-accurate tungkol sa Roots na sumasaklaw sa mga impormal na filesystem hints, ang
  kasalukuyang multi-round-trip na daloy, mga security boundaries, at mga opsyon sa migration.
- **Nilinaw**: Ang Roots, Sampling, Logging, at Dynamic Client Registration ay
  deprecated sa `2026-07-28`, kasama ang kanilang mga inirekomendang kapalit at ang pinakamahalagang
  petsa ng pagtanggal ay idinokumento.
- **Naka-label**: Ang mga sample na umaasa pa rin sa MCP `2025-11-25`, HTTP+SSE,
  mga handshake sa pag-initialize, o mga protocol session ay nanatili bilang mga legacy
  compatibility na halimbawa kaysa ipakita bilang kasalukuyang mga implementasyon.
- **Gabay sa seguridad**: In-update ang mga standalone na gabay sa seguridad upang gumamit ng
  per-request na awtorisasyon at malinaw na mga application state handle sa halip na
  mga tinanggal na protocol session ID. Ang Client ID Metadata Documents ay ngayon ang
  inirerekomendang daan ng pagpaparehistro, kasama ang DCR na idinokumento bilang compatibility-only.
- **Suportadong materyal**: In-update ang study guide, contributor checklist,
  Publora case study, at APIM case study. Ang APIM walkthrough ay inirerekomenda na ngayon
  ang kasalukuyang Streamable HTTP `/mcp` endpoint nito sa halip na deprecated na `/sse`.
- **Canonical na link**: Pinalitan ang mga na-retire at draft na URL ng espesipikasyon sa English
  source Markdown ng mga versioned `2026-07-28` na link, habang pinananatili ang mga
  malinaw na link sa mga legacy na bersyon kung saan ang sample ay naka-pin pa rin sa mas lumang tooling.
- **Matatag na mga filename**: Pinalitan ang pangalan ng panghuling gabay ng espesipikasyon at dalawang gabay sa seguridad
  upang alisin ang release-candidate at year suffix, pagkatapos ay in-update ang lahat ng English
  hyperlink sa kanilang matatag na mga landas.
- **Bagong sample ng awtorisasyon**: Nagdagdag ng isang nasubok na
  [TypeScript MCP `2026-07-28` resource server](./02-Security/samples/cimd-dcr-auth/README.md)
  na naghahambing ng inirerekomendang Client ID Metadata Documents sa deprecated na fallback ng Dynamic
  Client Registration. Kasama sa sample ang RFC 9728 discovery, JWKS
  validation, per-tool scopes, labingdalawang pagsubok, at isang walkthrough ng setup ng Auth0.
- **Saklaw ng pagsasalin**: Tanging ang mga English source file lamang ang na-edit; ang mga
  nabuo na pagsasalin at mga isinaling larawan ay nananatiling hindi nagbabago dahil awtomatikong isinalin.

## Hulyo 29, 2026

### Bagong Module 08 Companion: Reliability Sidecars at Mga Ligtas na Retry

Nagdagdag ng vendor-neutral na companion lesson para sa mga MCP tool na lumilikha ng mga totoong epekto sa mundo,
naka-align sa panghuling `2026-07-28` na espesipikasyon.


- **Bago**: Ang [araling katuwang na reliability sidecar][reliability-sidecar]
  ay gumagamit ng isang istorya ng support-ticket, dalawang diagram ng Mermaid, at isang retry decision
  flow upang ipaliwanag ang mga susi sa matatag na operasyon, atomic duplicate admission,
  reconciliation, ebidensya, at ang Tasks extension boundary.
- **Bago**: Isang exercise sa pag-inject ng pagkabigo gamit ang standard-library Python at SQLite
  na gumagamit ng hiwalay na operation at ticket stores upang ipakita ang response na nawala
  pagkatapos makumpleto ang isang external effect. Anim na deterministikong pagsubok ang sumasaklaw sa naive
  duplication, guarded restart recovery, payload conflicts, cached results,
  active claims, at concurrent duplicate admission.
- **Na-update**: Ang Module 08 ay ngayon naka-link sa araling katuwang, tinutukoy ang
  panghuling `2026-07-28` na stateless request model, pinag-iiba ang OpenTelemetry
  observability mula sa deprecated MCP logging feature, at nililimitahan ang
  generic retry example nito sa mga read-only na operasyon.
- **Opsyonal**: Iminapa ng aralin ang mga portable na konsepto nito sa isang tagged na implementasyon ng komunidad
  nang hindi ginagawa ang hosted service o isang network call bilang bahagi ng
  ehersisyo.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## Hulyo 2, 2026

### Bagong Aralin: Ang 2026-07-28 MCP Specification Release Candidate

Idinagdag ang saklaw ng paparating na `2026-07-28` MCP specification release candidate (inaanunsyo noong Mayo 21, 2026; nakatakdang ilabas ang pinal noong Hulyo 28, 2026), na binuo mula sa [opisyal na anunsyo sa blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Nanatiling **MCP Specification 2025-11-25** ang baseline ng kurikulum hanggang sa maipadala ang bagong bersyon, kaya ito ay ipinapakita bilang patnubay na nakatingin sa hinaharap sa halip na muling pagsulat ng mga umiiral na aralin.

- **Bago**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — isang buong aralin na sumasaklaw sa stateless protocol core (pag-alis ng `initialize` handshake at `Mcp-Session-Id`), ang bagong `Mcp-Method`/`Mcp-Name` routing headers, `ttlMs`/`cacheScope` caching metadata, W3C Trace Context sa `_meta`, ang pormal na Extensions framework (MCP Apps at ang bagong Tasks extension), anim na authorization-hardening SEPs, ang pag-deprecate ng Roots/Sampling/Logging, at ang paglipat sa buong JSON Schema 2020-12 para sa mga tool schema.
- **Na-update** na may mga paunang pasulyap na tawag na naka-link sa bagong aralin:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): tala sa bersyon ng protocol, mga seksyon ng Sampling/Roots/Logging/Tasks, at "Ano ang susunod"
  - [02-Security/README.md](./02-Security/README.md): authorization hardening callout
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless transport callout
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling deprecation callout

  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Pag-log ng pag-uubos at paalala ng extension ng Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session-routing callout
  - [README.md](./README.md): tala na "Tumingin sa Hinaharap" sa seksyon ng espesipikasyon at isang bagong entry na `1.1` sa talahanayan ng kurikulum na module
  - [study_guide.md](./study_guide.md): pasulong na pagtingin sa bullet sa ilalim ng Core Concepts overview at isang may petsang addendum na tala
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): callout sa `mcp-session-id` transport map bago ang stateless na modelo ng kahilingan
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): module overview callout sa Root Contexts/Sampling deprecations at ang Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): authorization hardening callout

## Hunyo 24, 2026

### Bagong Aralin: Paggamit ng MCP sa Copilot app

- [Seksyon ng Tooling](./12-tooling/README.md) Idinagdag ang seksyon ng tooling.
- [MCP sa Copilot app](./12-tooling/01-copilot-app/README.md)

## Hunyo 16, 2026

### Pagkakatugma ng MCP Specification & Pagpapatunay ng Sample

Pinatunayan ang kurikulum laban sa kasalukuyang **MCP Specification 2025-11-25** at sa pinakabagong opisyal na SDKs, pagkatapos ay inayos ang mga natitirang lumang sanggunian sa espesipikasyon at kinumpirma na ang mga pangunahing sample ay patuloy na bumubuo at tumatakbo.

#### Pagwawasto ng Bersyon ng Espesipikasyon (2025-06-18 / 2025-03-26 → 2025-11-25)

In-update ang nilalaman sa Ingles kung saan ito ay nagsasabing ang mas lumang rebisyon ng spec ay ang *kasalukuyan/pinakabago* na pamantayan, at nireporma ang mga link sa canonical na mga landas ng `modelcontextprotocol.io` spec:
- **05-AdvancedTopics/mcp-security/README.md**: In-update ang "Kasalukuyang Pamantayan" na banner, panimula, mga heading ng pangunahing prinsipyo ng seguridad, mga heading ng mandatoryong mga kinakailangan, seksyon ng Microsoft Entra ID, mga link sa Mga Sanggunian at Mga Mapagkukunan, at para sa pagtatapos na paalala sa seguridad (8 na sanggunian) sa 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: In-update ang link sa Additional Resources spec at ang "Kasalukuyang Pamantayan" banner sa 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Pinalitan ang luma at lipas na `2025-03-26` security-and-trust na link ng kasalukuyang pahina ng pinakamahusay na praktis sa seguridad sa 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: In-update ang opisyal na sampling docs link sa 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: In-update ang kasalukuyang panahon na "kasalukuyang MCP specification" na sanggunian at ang Additional Resources spec link sa 2025-11-25 (iniwan ang mga makasaysayang tala sa SSE-deprecation para sa katumpakan)

#### Pagpapatunay ng Sample Laban sa Kasalukuyang SDKs

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` nagresolba ng `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` pumasa nang walang mga error sa uri — nananatiling wasto ang mga umiiral na `McpServer`/`StdioServerTransport` APIs
- **Python (03-GettingStarted/01-first-server/solution/python)**: Pinatunayan sa isang hiwalay na `.venv` gamit ang `mcp[cli]` (1.27.2); pumasa ang `py_compile` at ang `FastMCP.list_tools()` ay tamaang nagbalik ng `add` at `subtract` na mga tool
- Nakumpirma na ang lahat ng bersyon na range ng sample `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) ay malinis na nagre-resolba sa kasalukuyang `1.29.0` nang walang mga pagbabago sa API na sumisira

#### Pagkakatugma ng Dependency Pin (pagsasara ng mga agwat ng bersyon)

Inangat ang mga lumang SDK pins para bawat sample ay tumutugma sa kasalukuyang MCP release, ayon sa kasunduan sa buong repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Inangat ang `@modelcontextprotocol/sdk` mula `^1.8.0` → `>=1.26.0` at in-update ang lumang paglalarawan ng package na `"updated for MCP 2025-06-18"` sa `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** at **lab4/code/github_mcp_server/pyproject.toml**: Inangat ang eksaktong pin `mcp==1.23.0` → `mcp>=1.26.0`; niregenerada ang parehong `uv.lock` files (`uv lock`) kaya ang mga lockfiles ay nagre-resolba sa kasalukuyang `mcp 1.27.2` at nananatiling kaayon sa mga manifest

#### Pagsusuri ng Gap sa Kurikulum — Pinakabagong Saklaw ng Tampok ng Spec

Kinumpirma na ang kurikulum ay sumasaklaw na sa lahat ng primitives na ipinakilala/pinalawak sa MCP 2025-11-25, kaya walang mga puwang sa nilalaman:
- **Sampling**: Aralin 03-GettingStarted/14-sampling dagdag ang 05-AdvancedTopics/mcp-sampling
- **Elicitation (kasama ang URL mode)**: Naitala sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Naitala sa 00-Introduction, 01-CoreConcepts, at 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimental, mga mahahabang operasyon)**: Naitala sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Naitala sa 01-CoreConcepts at 05-AdvancedTopics/mcp-protocol-features

### Pagpapalakas ng Seguridad at Pag-ayos ng Mga Kahinaan sa Dependency

Nagsagawa ng kumpletong security pass sa bawat dependency manifest at sample source code, pagkatapos ay inayos ang lahat ng naulat na advisories ng npm at isang natuklasang code-level. Pagkatapos ng paglutas, ang `npm audit` ay nag-uulat ng **0 kahinaan** sa bawat audited na direktoryo.

#### Mga Kahinaan sa npm Dependency (transitive) — Naayos

Sinuri ang lahat ng 15 na naka-commit na `package-lock.json` files. Ang mga kahinaan ay limitado sa mga transitive dependencies na dinala ng MCP Inspector dev tool, OpenAI client, at MCP SDK; lahat ngayon ay naresolba nang hindi sinisira ang mga sample:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** at **lab3/code/weather_mcp/inspector**: In-update ang `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), na naglinis ng mga bundled na advisory para sa `ajv`, `brace-expansion`, `diff`, `path-to-regexp` at `ws`. Nagdagdag ng npm `overrides` na entry para pilitin ang patched na `shell-quote@1.8.4` upang alisin ang natitirang critical advisory mula sa `concurrently`; muling ginawa ang parehong lockfiles (ngayon 0 na kahinaan)
- **03-GettingStarted/samples/typescript**: `npm audit fix` in-update ang transitive na `qs` (moderate) sa patched na release
- **03-GettingStarted/samples/javascript**: `npm audit fix` in-update ang transitive na `hono` (moderate) sa patched na release
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` in-update ang transitive na `form-data` (high) sa patched na release
- **03-GettingStarted/11-simple-auth/solution/typescript**: Nalikha ang nawawalang `package-lock.json` upang maging reproducible at auditable ang proyekto (0 kahinaan)

#### Pag-ayos ng Seguridad sa Antas ng Code (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Tinanggal ang `shell=True` mula sa `open_in_vscode` na tool. Ang dating `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` ay nagpapahintulot sa shell metacharacters na nasa folder path na ma-interpret ng `cmd.exe` (vector ng command-injection). Ngayon ay direktang pinapalabas ang resolved na `Code.exe` na may kasamang folder bilang argumento — walang shell — na functionally katumbas at ligtas

#### Python Dependency Audit

- Sinuri ang bawat Python requirements gamit ang `pip-audit`. Ang `05-AdvancedTopics` at `03-GettingStarted/samples/python` ay nag-ulat ng **walang kilalang kahinaan** (ang kanilang `mcp` / `httpx` / `pydantic` / `python-dotenv` na mga range ay nagreresolba sa kasalukuyang mga patched na release)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: Ang `pip-audit` ay nag-flag sa transitive na dependency na **`werkzeug` 3.1.1** na may tatlong `safe_join` Windows device-name DoS advisories — `CVE-2025-66221`, `CVE-2026-21860`, at `CVE-2026-27199` (lahat ay naayos sa 3.1.6). Nagdagdag ng espesipikong security pin `werkzeug>=3.1.6` para ma-resolve ang patched release; pinatunayan na malinis ang constraint sa `chainlit` / `mcp` / `semantic-kernel` stack

### Pagbabago ng Pangalan ng Produkto

In-update ang lahat ng nilalaman ng kurikulum upang ipakita ang rebranding ng produkto ng Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: In-update ang link ng Discord community
- **AGENTS.md**: In-update ang reference sa Discord server
- **README.md**: In-update ang mga reference sa technology ecosystem
- **study_guide.md**: In-update ang mga reference sa case study
- **05-AdvancedTopics/README.md**: In-update ang pamagat at deskripsyon ng Module 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: In-update ang header ng seksyon at deskripsyon
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Buong pag-update ng pamagat ng module at nilalaman
- **05-AdvancedTopics/mcp-security-entra/README.md**: In-update ang cross-reference link
- **07-LessonsfromEarlyAdoption/README.md**: In-update ang mga reference sa case study
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: In-update ang header ng Seksyon 9, mga badge, at mga kakayahan
- **08-BestPractices/README.md**: In-update ang link ng Discord community
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: In-update ang reference sa Discord channel
- **09-CaseStudy/docs-mcp/solution/python/README.md**: In-update ang reference sa deployment ng modelo
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: In-update ang table ng AI Services
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: In-update ang mga reference sa resources

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension para sa VS Code
- **README.md**: In-update ang mga pangunahing reference ng kurikulum
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: In-update ang pamagat ng module, pangkalahatang-ideya, at lahat ng mga header ng module
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: In-update ang pamagat, mga layunin ng pagkatuto, mga tagubilin sa setup, at mga resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: In-update ang pamagat, mga layunin ng pagkatuto, tabel ng MCP hosts, at mga cross-reference
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: In-update ang pamagat, mga badge, mga prerequisites, at mga resources
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: In-update ang mga reference sa Agent Builder at link ng feedback
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: In-update ang mga prerequisites at mga reference sa extension

---

## Abril 11, 2026

### Bagong Aralin, Pag-ayos ng Dokumentasyon, at Mga Update sa Dependency

#### Idinagdag na Bagong Nilalaman ng Kurikulum

**Module 05 - Mga Advanced na Paksa**
- **Lesson 5.17: Adversarial Multi-Agent Reasoning with MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Bagong komprehensibong gabay tungkol sa adversarial debate pattern para sa multi-agent systems
  - Mermaid architecture diagram: dalawang agents → shared MCP server → debate transcript → judge → verdict
  - Shared MCP tool server (`web_search` + `run_python`) na ipinatupad sa Python at TypeScript
  - Mga pang-ibang panig na prompts ng system (FOR / AGAINST / Judge) na may explicit tool-use requirements
  - Debate orchestrator sa Python, TypeScript, at C# na nagpapatakbo ng mga rounds at nagro-route ng mga argumento
  - MCP `ClientSession` wiring para sa orchestrator sa totoong tawag ng tool
  - Tabel ng use-case (hallucination detection, threat modeling, API design review, factual verification, tech selection)
  - Mga konsiderasyon sa seguridad: sandboxed execution, tool-call validation, rate limiting, audit logging
  - Structured na exercise na may tatlong praktikal na scenario (code review, decision sa arkitektura, content moderation)

#### Pag-ayos ng Dokumentasyon

**Module 03 - Getting Started**
- **05-stdio-server/README.md**: Naayos ang hindi kumpletong halimbawa ng TypeScript stdio server — idinagdag ang nawawalang transport instantiation (`new StdioServerTransport()`) at `server.connect(transport)` na tawag upang tumugma sa mga exemplo sa Python at .NET sa parehong seksyon
- **14-sampling/README.md**: Naayos ang typographical error — inayos mula sa `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang entry 5.17 (Adversarial Multi-Agent Reasoning with MCP) sa tabel ng kurikulum na may direktang link sa bagong aralin

**05-AdvancedTopics/README.md**
- Idinagdag ang Lesson 5.17 sa talaan ng lessons

**study_guide.md**
- Idinagdag ang Adversarial Multi-Agent Reasoning bilang paksa sa mind-map at prose na paglalarawan ng Advanced Topics

#### Pag-ayos ng Code at Seguridad

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Pag-ayos sa seguridad — command injection**: Pinalitan ang `execSync` shell interpolation ng `execFile` + `promisify` sa TypeScript `run_python` na tool, na inaalis ang command injection surface (ang code na kontrolado ng LLM ay ipinapasa ngayon bilang literal argv element nang walang shell involvement)
- **MCP tool loop wiring**: In-update ang Python debate orchestrator upang gamitin ang `AsyncAnthropic` client (pinalitan ang blocking sync `Anthropic`), ipasa nang live ang `ClientSession` direkta sa bawat turn ng agent, kunin ang mga tool definitions gamit ang `session.list_tools()` bawat turn, at magpadala ng `tool_use` blocks gamit ang `session.call_tool()` sa isang loop hanggang maglabas ang modelo ng final na text response

#### Mga Update sa Dependency

- In-update ang `hono` sa 4.12.12 sa maraming packages (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- In-update ang `@hono/node-server` mula 1.19.11 hanggang 1.19.13 sa mga TypeScript packages
- In-update ang `cryptography` mula 46.0.5 hanggang 46.0.7 sa mga Python packages (10-StreamliningAIWorkflows labs 3 at 4)
- In-update ang `lodash` mula 4.17.23 hanggang 4.18.1 sa 10-StreamliningAIWorkflows inspector

#### Mga Pagsasalin

- Sinync ang mga pagsasalin para sa 48+ na wika gamit ang pinakabagong mga pagbabago sa source (i18n update)

---

## Pebrero 5, 2026

### Mga Pagpapabuti sa Validasyon at Navagasyon sa Buong Repository

#### Idinagdag na Bagong Nilalaman ng Kurikulum

**Module 03 - Getting Started**
- **12-mcp-hosts/README.md**: Bagong komprehensibong gabay sa pagsasaayos ng MCP hosts
  - Mga halimbawa sa pag-configure ng Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Mga template sa JSON configuration para sa lahat ng pangunahing hosts
  - Tabel ng paghahambing ng mga uri ng transport (stdio, SSE/HTTP, WebSocket)
  - Pag-aayos ng mga karaniwang problema sa koneksyon
  - Pinakamahusay na kasanayan sa seguridad para sa pag-setup ng host

- **13-mcp-inspector/README.md**: Bagong gabay sa debugging para sa MCP Inspector
  - Mga paraan ng pag-install (npx, npm global, mula sa source)
  - Pagkonekta sa mga server gamit ang stdio at HTTP/SSE
  - Pagsubok ng tools, resources, at workflows ng prompts
  - Integrasyon ng VS Code sa MCP Inspector
  - Mga karaniwang senaryo ng debugging na may mga solusyon

**Module 04 - Practical Implementation**
- **pagination/README.md**: Bagong gabay sa implementasyon ng pagination
  - Mga pattern ng cursor-based pagination sa Python, TypeScript, Java
  - Pag-handle ng pagination sa client side
  - Mga diskarte sa disenyo ng cursor (opaque laban sa structured)
  - Mga rekomendasyon para sa performance optimization

**Module 05 - Advanced Topics**
- **mcp-protocol-features/README.md**: Bagong malalim na pagtalakay ng mga bagong protocol features
  - Implementasyon ng progress notifications
  - Mga pattern sa pag-cancel ng request
  - Mga template ng resource na may mga pattern ng URI
  - Pamamahala ng lifecycle ng server
  - Kontrol ng logging level
  - Mga pattern sa paghawak ng error gamit ang JSON-RPC codes

#### Mga Pag-aayos sa Navagasyon (24+ files ang in-update)

**Pangunahing Mga Module na README**
 Ngayon ay may mga link sa parehong unang aralin AT susunod na module

**02-Security na Sub-files**
- Lahat ng 5 na mga security na dokumento ay ngayon may "Ano ang Susunod" na navagasyon:

**09-CaseStudy Files**
- Lahat ng mga case study files ay may sunud-sunod na navagasyon:

**10-StreamliningAI Labs**
Idinagdag ang Seksiyon na Ano ang Susunod sa pangkalahatan ng Module 10 at Module 11

#### Pag-ayos ng Code at Nilalaman

**SDK at Mga Update sa Dependency**
Inayos ang walang laman na bersyon ng openai sa `^4.95.0`
In-update ang SDK mula `^1.8.0` hanggang `>=1.26.0`
In-update ang mga version pin ng mcp sa `>=1.26.0`

**Pag-ayos ng Code**
Inayos ang maling modelo `gpt-4o-mini` sa `gpt-4.1-mini`

**Pag-aayos ng Nilalaman**
Inayos ang sira na link `READMEmd` → `README.md`, inayos ang header ng kurikulum mula `Module 1-3` → `Module 0-3`, inayos ang case-sensitive path
Tinanggal ang nasirang duplicate na nilalaman ng Case Study 5

**Pagpapabuti sa Gabay para sa mga Baguhan**
Idinagdag ang tamang panimula, mga layunin ng pagkatuto, at mga prerequisites para sa baguhan

#### Mga Update sa Kurikulum

**Pangunahing README.md**
- Idinagdag ang mga entries 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) sa tabel ng kurikulum

**Mga README ng Module**
Idinagdag ang mga lessons 12 at 13 sa listahan ng lessons
Idinagdag ang Seksiyon ng Practical Guides na may link sa pagination
Idinagdag ang mga lessons 5.15 (Custom Transport) at 5.16 (Protocol Features)

**study_guide.md**
- In-update ang mindmap kasama ang lahat ng bagong paksa: MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive

## Enero 28, 2026

### Repasuhin ang Pagsunod sa MCP Specification 2025-11-25

#### Pagpapahusay ng Core Concepts (01-CoreConcepts/)
- **Bagong Client Primitive - Roots**: Nagdagdag ng komprehensibong dokumentasyon tungkol sa Roots client primitive, na nagpapahintulot sa mga server na maintindihan ang mga hangganan ng filesystem at mga permiso sa pag-access
- **Mga Anotasyon sa Tool**: Nagdagdag ng dokumentasyon tungkol sa mga anotasyong pang-behavior ng tool (`readOnlyHint`, `destructiveHint`) para sa mas mahusay na mga desisyon sa pagpapatupad ng tool
- **Pagtawag ng Tool sa Sampling**: In-update ang dokumentasyon ng Sampling upang isama ang mga parameter na `tools` at `toolChoice` para sa pinapatakbo ng modelo na pagtawag ng tool sa mga sampling request
- **URL Mode Elicitation**: Nagdagdag ng dokumentasyon hinggil sa URL-based elicitation para sa mga panlabas na interaksyon sa web na inisyatiba ng server
- **Mga Gawain (Eksperimento)**: Nagdagdag ng bagong seksiyon na nagdodokumento ng experimental Tasks feature para sa mga durable execution wrappers at deferred result retrieval

- **Suporta sa Mga Icon**: Napansin na ang mga tool, mapagkukunan, template ng mapagkukunan, at mga prompt ay maaari nang magsama ng mga icon bilang karagdagang metadata

#### Mga Pag-update sa Dokumentasyon
- **README.md**: Idinagdag ang sanggunian sa bersyon ng MCP Specification 2025-11-25 at paliwanag sa pag-version batay sa petsa
- **study_guide.md**: Na-update ang mapa ng kurikulum upang isama ang Mga Gawain at Annotasyon ng Tool sa seksyong Core Concepts; na-update ang timestamp ng dokumento

#### Pag-Verify ng Pagsunod sa Espesipikasyon
- **Bersyon ng Protokol**: Nakumpirma na lahat ng dokumentasyon ay tumutukoy sa kasalukuyang MCP Specification 2025-11-25
- **Pag-align ng Arkitektura**: Nakumpirma ang katumpakan ng dokumentasyon ng dalawang-layer na arkitektura (Data Layer + Transport Layer)
- **Dokumentasyon ng Mga Primitibo**: Na-validate ang mga primitive ng server (Resources, Prompts, Tools) at mga primitive ng kliyente (Sampling, Elicitation, Logging, Roots)
- **Mga Mekanismo ng Transportasyon**: Nakumpirma ang katumpakan ng dokumentasyon para sa STDIO at Streamable HTTP na transportasyon
- **Patnubay sa Seguridad**: Nakumpirma ang pag-align sa kasalukuyang MCP Security Best Practices na dokumentasyon

#### Mga Pangunahing Tampok ng MCP 2025-11-25 na Naitala
- **OpenID Connect Discovery**: Pagtuklas ng server ng awtentikasyon sa pamamagitan ng OIDC
- **Mga Dokumento ng Metadata ng OAuth Client ID**: Inirerekomendang mekanismo ng pagpaparehistro ng kliyente
- **JSON Schema 2020-12**: Default na dialekto para sa mga depinisyon ng MCP schema
- **SDK Tiering System**: Pormal na mga kinakailangan para sa suporta at pagpapanatili ng mga tampok ng SDK
- **Estruktura ng Pamamahala**: Pormal na mga Working Groups at Interest Groups sa pamamahala ng MCP

### Malaking Pag-update sa Dokumentasyon ng Seguridad (02-Security/)

#### Integrasyon ng MCP Security Summit Workshop (Sherpa)
- **Bagong Hands-On Training Resource**: Idinagdag ang komprehensibong integrasyon ng [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) sa lahat ng dokumentasyon ng seguridad
- **Saklaw ng Ruta ng Ekspedisyon**: Naitala ang kumpletong progreso mula Base Camp hanggang Summit ng kampo
- **Pag-align sa OWASP**: Lahat ng patnubay sa seguridad ay naka-map na ngayon sa mga panganib ng OWASP MCP Azure Security Guide

#### Integrasyon ng OWASP MCP Top 10
- **Bagong Seksyon**: Idinagdag ang talahanayan ng OWASP MCP Top 10 Security Risks na may mga mitigasyon ng Azure sa pangunahing Security README
- **Dokumentasyon Batay sa Panganib**: Na-update ang mcp-security-controls-2025.md gamit ang mga sanggunian sa panganib ng OWASP MCP para sa bawat domain ng seguridad
- **Reference Architecture**: Nakalink sa OWASP MCP Azure Security Guide reference architecture at mga pattern ng implementasyon

#### Na-update na mga File ng Seguridad
- **README.md**: Idinagdag ang Sherpa Workshop overview, talahanayan ng ruta ng ekspedisyon, buod ng OWASP MCP Top 10 risks, at seksyon sa hands-on training
- **mcp-security-controls-2025.md**: Na-update ang header sa Pebrero 2026, idinagdag ang mga sanggunian sa panganib ng OWASP (MCP01-MCP08), inayos ang hindi pagkakatugma ng bersyon ng spec
- **mcp-security-best-practices-2025.md**: Idinagdag ang seksyon ng Sherpa at OWASP resources, na-update ang timestamp
- **mcp-best-practices.md**: Idinagdag ang seksyon ng hands-on training kasama ang Sherpa at OWASP na mga link
- **azure-content-safety-implementation.md**: Idinagdag ang sanggunian sa OWASP MCP06, pag-align sa Sherpa Camp 3, at karagdagang seksyon ng mga mapagkukunan

#### Idinagdag na Bagong Mga Link sa Resource
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Mga Indibidwal na pahina ng panganib ng OWASP MCP (MCP01-MCP10)

### Pangkalahatang Kurikulum na Pag-align sa MCP Specification 2025-11-25

#### Module 03 - Pagsisimula
- **Dokumentasyon ng SDK**: Idinagdag ang Go SDK sa opisyal na listahan ng SDK; na-update ang lahat ng sanggunian sa SDK upang tumugma sa MCP Specification 2025-11-25
- **Paglilinaw sa Transportasyon**: Na-update ang mga paglalarawan ng STDIO at HTTP Streaming na transportasyon na may malinaw na sanggunian sa spec

#### Module 04 - Praktikal na Implementasyon
- **Mga Pag-update sa SDK**: Idinagdag ang Go SDK; na-update ang listahan ng SDK na may sanggunian sa bersyon ng espesipikasyon
- **Spec ng Awtorisasyon**: Na-update ang link ng MCP Authorization specification sa kasalukuyang bersyon na 2025-11-25

#### Module 05 - Mga Advanced na Paksa
- **Mga Bagong Tampok**: Idinagdag ang nota tungkol sa mga bagong tampok ng MCP Specification 2025-11-25 (Mga Gawain, Annotasyon ng Tool, URL Mode Elicitation, Roots)
- **Mga Mapagkukunan sa Seguridad**: Idinagdag ang OWASP MCP Top 10 at mga link sa Sherpa workshop sa mga karagdagang sanggunian

#### Module 06 - Mga Kontribusyon ng Komunidad
- **Listahan ng SDK**: Idinagdag ang Swift at Rust SDKs; na-update ang link ng espesipikasyon sa 2025-11-25
- **Sanggunian sa Spec**: Na-update ang link ng MCP Specification sa direktang URL ng espesipikasyon

#### Module 07 - Mga Aral mula sa Maagang Pagtanggap
- **Mga Pag-update ng Resource**: Idinagdag ang MCP Specification 2025-11-25 na link at OWASP MCP Top 10 sa mga karagdagang mapagkukunan

#### Module 08 - Mga Pinakamahusay na Praktis
- **Bersyon ng Spec**: Na-update ang sanggunian sa MCP Specification sa 2025-11-25
- **Mga Mapagkukunan sa Seguridad**: Idinagdag ang OWASP MCP Top 10 at Sherpa workshop sa mga karagdagang sanggunian

#### Module 10 - Pagpapadali ng Mga Workflow ng AI
- **Pag-update sa Badge**: Binago mula sa badge ng bersyon ng SDK (1.9.3) sa badge ng bersyon ng espesipikasyon (2025-11-25)
- **Mga Link ng Resource**: Na-update ang link ng MCP Specification; idinagdag ang OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Sanggunian sa Spec**: Na-update ang link ng MCP Specification sa bersyon 2025-11-25
- **Mga Mapagkukunan sa Seguridad**: Idinagdag ang OWASP MCP Top 10 sa opisyal na mga mapagkukunan

## Disyembre 18, 2025

### Pag-update ng Dokumentasyon ng Seguridad - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Pag-update ng Bersyon ng Espesipikasyon
- **Pag-update ng Bersyon ng Protokol**: Na-update upang tukuyin ang pinakabagong MCP Specification 2025-11-25 (inilabas Nobyembre 25, 2025)
  - Na-update lahat ng sanggunian sa bersyon ng espesipikasyon mula 2025-06-18 hanggang 2025-11-25
  - Na-update ang mga sanggunian sa petsa ng dokumento mula Agosto 18, 2025 hanggang Disyembre 18, 2025
  - Nakumpirma na lahat ng URL ng espesipikasyon ay tumutukoy sa kasalukuyang dokumentasyon
- **Pagpapatunay ng Nilalaman**: Komprehensibong pagsusuri ng mga pinakamahusay na praktis sa seguridad laban sa pinakabagong mga pamantayan
  - **Microsoft Security Solutions**: Nakumpirma ang kasalukuyang termino at mga link para sa Prompt Shields (dating "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, at Azure Key Vault
  - **Seguridad ng OAuth 2.1**: Nakumpirma ang pagsunod sa pinakabagong pinakamahusay na praktis sa seguridad ng OAuth
  - **Mga Pamantayan ng OWASP**: Na-validate ang mga sanggunian sa OWASP Top 10 para sa LLMs ay nananatiling kasalukuyan
  - **Mga Serbisyo ng Azure**: Nakumpirma ang lahat ng Microsoft Azure dokumentasyon na mga link at pinakamahusay na praktis
- **Pag-align sa Pamantayan**: Lahat ng tinukoy na pamantayang pang-seguridad ay nakumpirmang kasalukuyan
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Mga Pinakamahusay na Praktis sa Seguridad ng OAuth 2.1
  - Mga framework ng seguridad at pagsunod ng Azure
- **Mga Mapagkukunan sa Implementasyon**: Na-validate ang lahat ng mga link ng gabay sa implementasyon at mga mapagkukunan
  - Mga pattern ng awtentikasyon sa Azure API Management
  - Mga gabay sa integrasyon ng Microsoft Entra ID
  - Pamamahala ng mga lihim ng Azure Key Vault
  - Mga pipeline ng DevSecOps at mga solusyon sa pagmamanman

### Pagsisiguro ng Kalidad sa Dokumentasyon
- **Pagsunod sa Espesipikasyon**: Tiniyak na lahat ng obligadong MCP na mga kinakailangan sa seguridad (MUST/MUST NOT) ay tumutugma sa pinakabagong espesipikasyon
- **Kasalukuyang Mga Mapagkukunan**: Nakumpirma ang lahat ng panlabas na mga link sa Microsoft dokumentasyon, pamantayan sa seguridad, at mga gabay sa implementasyon
- **Saklaw ng Pinakamahusay na Praktis**: Nakumpirma ang komprehensibong saklaw ng awtentikasyon, awtorisasyon, mga partikular na banta sa AI, seguridad ng supply chain, at mga pattern ng enterprise

## Oktubre 6, 2025

### Pagpapalawak ng Seksyon ng Pagsisimula – Advanced na Paggamit ng Server & Simpleng Awthentikasyon

#### Advanced na Paggamit ng Server (03-GettingStarted/10-advanced)
- **Bagong Kabanata Idinagdag**: Nagpakilala ng komprehensibong gabay sa advanced na paggamit ng MCP server, na sumasaklaw sa parehong regular at low-level na arkitektura ng server.
  - **Regular vs. Low-Level Server**: Detalyadong paghahambing at mga halimbawa ng code sa Python at TypeScript para sa parehong mga paraan.
  - **Disenyong Batay sa Handler**: Paliwanag ng handler-based tool/resource/prompt management para sa scalable, flexible na implementasyon ng server.
  - **Mga Praktikal na Pattern**: Mga totoong senaryo kung saan kapaki-pakinabang ang low-level server patterns para sa mga advanced na tampok at arkitektura.

#### Simpleng Awthentikasyon (03-GettingStarted/11-simple-auth)
- **Bagong Kabanata Idinagdag**: Hakbang-hakbang na gabay sa pagpapatupad ng simpleng awthentikasyon sa mga MCP server.
  - **Mga Konsepto ng Awthentikasyon**: Malinaw na paliwanag ng awthentikasyon kontra awtorisasyon, at paghawak ng mga kredensyal.
  - **Basic Auth Implementation**: Mga pattern ng awthentikasyon na batay sa middleware sa Python (Starlette) at TypeScript (Express), kasama ang mga sample ng code.
  - **Pag-usad sa Advanced na Seguridad**: Patnubay sa pagsisimula sa simpleng awthentikasyon at pag-usad sa OAuth 2.1 at RBAC, na may mga sanggunian sa mga advanced na module ng seguridad.

Ang mga dagdag na ito ay nagbibigay ng praktikal, hands-on na patnubay para sa pagbuo ng mas matibay, ligtas, at flexible na mga implementasyon ng MCP server, na nag-uugnay ng mga pundasyong konsepto sa mga advanced na pattern sa produksyon.

## Setyembre 29, 2025

### MCP Server Database Integration Labs - Komprehensibong Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - Bagong Kumpletong Kurikulum ng Database Integration
- **Kumpletong 13-Lab na Learning Path**: Idinagdag ang komprehensibong hands-on na kurikulum para sa pagbuo ng production-ready MCP servers na may PostgreSQL database integration
  - **Implementasyong Totoong Mundo**: Zava Retail analytics use case na nagpapakita ng mga enterprise-grade na pattern
  - **Istrukturadong Progression ng Pag-aaral**:
    - **Labs 00-03: Panimula** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Pagbuo ng MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Mga Advanced na Tampok** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Produksyon at Pinakamahusay na Praktis** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL na may pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Mga Advanced na Tampok**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Standardisasyon ng Terminolohiya - Modyul sa Pag-convert ng Lab
- **Komprehensibong Pag-update ng Dokumentasyon**: Sistematikong na-update ang lahat ng README files sa 11-MCPServerHandsOnLabs upang gamitin ang terminolohiyang "Lab" sa halip na "Module"
  - **Mga Header ng Seksyon**: Na-update ang "What This Module Covers" sa "What This Lab Covers" sa lahat ng 13 labs
  - **Paglalarawan ng Nilalaman**: Pinalitan ang "This module provides..." ng "This lab provides..." sa buong dokumentasyon
  - **Mga Layunin sa Pagkatuto**: Na-update ang "By the end of this module..." sa "By the end of this lab..." 
  - **Mga Link sa Navigasyon**: Pinalitan ang lahat ng sanggunian na "Module XX:" sa "Lab XX:" sa mga cross-reference at navigasyon
  - **Pagsubaybay ng Pagkumpleto**: Na-update ang "After completing this module..." sa "After completing this lab..."
  - **Napanatiling Mga Teknikal na Sanggunian**: Pinanatili ang mga Python module references sa mga configuration file (hal., `"module": "mcp_server.main"`)

#### Pagpapahusay ng Study Guide (study_guide.md)
- **Biswal na Mapa ng Kurikulum**: Idinagdag ang bagong seksyon na "11. Database Integration Labs" na may komprehensibong biswal na istruktura ng lab
- **Istruktura ng Repository**: Na-update mula sa sampu hanggang labing-isang pangunahing seksyon na may detalyadong paglalarawan ng 11-MCPServerHandsOnLabs
- **Patnubay sa Learning Path**: Pinahusay ang mga tagubilin sa navigasyon upang saklawin ang mga seksyong 00-11
- **Saklaw ng Teknolohiya**: Idinagdag ang detalye ng integrasyon ng FastMCP, PostgreSQL, at mga serbisyo ng Azure
- **Mga Kinalabasan ng Pagkatuto**: Pinag-tuunan ng pansin ang pagbuo ng production-ready na server, mga pattern ng database integration, at enterprise security

#### Pagpapahusay sa Istruktura ng Pangunahing README
- **Terminolohiya Batay sa Lab**: Na-update ang pangunahing README.md sa 11-MCPServerHandsOnLabs upang gamitin nang pare-pareho ang istruktura ng "Lab"
- **Organisasyon ng Learning Path**: Malinaw na progreso mula sa mga pundasyong konsepto hanggang sa advanced na implementasyon at deployment sa produksyon
- **Pokus sa Totoong Mundo**: Pinagtibay ang praktikal, hands-on na pagkatuto gamit ang mga enterprise-grade na pattern at teknolohiya

### Pagbuti sa Kalidad at Konsistensi ng Dokumentasyon
- **Pagtuon sa Hands-On Learning**: Pinatibay ang praktikal, lab-based na pamamaraan sa buong dokumentasyon
- **Pokus sa Enterprise Patterns**: Binigyang-diin ang production-ready na mga implementasyon at mga konsiderasyong pang-seguridad sa enterprise
- **Integrasyon ng Teknolohiya**: Komprehensibong saklaw ng mga modernong serbisyo ng Azure at mga pattern ng integrasyon ng AI
- **Progresyon ng Pag-aaral**: Malinaw, istrukturadong landas mula sa mga pangunahing konsepto hanggang sa deployment sa produksyon

## Setyembre 26, 2025

### Pagpapahusay sa Mga Case Study - Integrasyon ng GitHub MCP Registry

#### Mga Case Study (09-CaseStudy/) - Pokus sa Pagpapaunlad ng Ecosystem
- **README.md**: Malaking pagpapalawak gamit ang komprehensibong case study ng GitHub MCP Registry
  - **GitHub MCP Registry Case Study**: Bagong komprehensibong pag-aaral ng kaso na sinusuri ang paglulunsad ng GitHub MCP Registry noong Setyembre 2025
    - **Pagsusuri ng Problema**: Detalyadong pagsusuri ng mga hamon sa fragmented MCP server discovery at deployment
    - **Arkitektura ng Solusyon**: Sentralisadong rehistro ng GitHub na may one-click na pag-install sa VS Code
    - **Epekto sa Negosyo**: Nasusukat na mga pagpapabuti sa onboarding at produktibidad ng developer
    - **Halaga ng Estratehiya**: Pokus sa modular na deployment ng ahente at interoperabilidad ng cross-tool
    - **Pag-unlad ng Ecosystem**: Posisyon bilang pundamental na plataporma para sa ahenteng integrasyon
  - **Pinahusay na Estruktura ng Case Study**: Na-update ang lahat ng pitong case study na may pare-parehong format at komprehensibong mga paglalarawan
    - Azure AI Travel Agents: Pokus sa multi-agent orchestration
    - Azure DevOps Integration: Pokus sa workflow automation
    - Real-Time Documentation Retrieval: Implementasyon ng Python console client
    - Interactive Study Plan Generator: Chainlit conversational web app

    - Dokumentasyon sa Loob ng Editor: Integrasyon ng VS Code at GitHub Copilot
    - Azure API Management: Mga pattern ng Enterprise API integration
    - GitHub MCP Registry: Pag-unlad ng ecosystem at platform ng komunidad
  - **Komprehensibong Konklusyon**: Muling naisulat na seksyon ng konklusyon na nagtatampok ng pitong case studies na sumasaklaw sa maraming dimensyon ng pagpapatupad ng MCP
    - Enterprise Integration, Multi-Agent Orchestration, Produktibidad ng Developer
    - Pag-unlad ng Ecosystem, Kategorisasyon ng Mga Aplikasyong Pang-edukasyon
    - Pinalalim na mga pananaw sa mga pattern ng arkitektura, mga estratehiya sa pagpapatupad, at mga pinakamahusay na kasanayan
    - Pagbibigay-diin sa MCP bilang mature, handa na para sa produksyon na protocol

#### Mga Update sa Gabay sa Pag-aaral (study_guide.md)
- **Mapa ng Visual Curriculum**: In-update ang mindmap upang isama ang GitHub MCP Registry sa seksyong Case Studies
- **Paglalarawan ng mga Case Studies**: Pinalawak mula sa mga pangkalahatang paglalarawan patungo sa detalyadong paghahati ng pitong komprehensibong case studies
- **Istruktura ng Repository**: In-update ang seksyon 10 upang ipakita ang komprehensibong saklaw ng case study na may mga partikular na detalye ng pagpapatupad
- **Integrasyon ng Changelog**: Idinagdag ang entry ng Setyembre 26, 2025 na nagdodokumento ng pagdaragdag ng GitHub MCP Registry at mga pagpapahusay ng case study
- **Mga Update sa Petsa**: In-update ang footer timestamp upang ipakita ang pinakabagong rebisyon (Setyembre 26, 2025)

### Mga Pagpapahusay sa Kalidad ng Dokumentasyon
- **Pagpapahusay ng Konsistensi**: Na-standardize ang pag-format at istruktura ng case study sa lahat ng pitong halimbawa
- **Komprehensibong Saklaw**: Ang mga case study ay sumasaklaw na ngayon sa mga sitwasyon ng enterprise, produktibidad ng developer, at pag-unlad ng ecosystem
- **Estratehikong Posisyon**: Pinalalim na pokus sa MCP bilang pundasyon na plataporma para sa pag-deploy ng agentic system
- **Integrasyon ng mga Resources**: In-update ang karagdagang mga resources upang isama ang link ng GitHub MCP Registry

## Setyembre 15, 2025

### Pagpapalawak ng Mga Advanced na Paksa - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Bagong Gabay sa Advanced Implementation
- **README.md**: Kumpletong gabay sa pagpapatupad para sa mga custom na mekanismo ng MCP transport
  - **Azure Event Grid Transport**: Komprehensibong implementasyon ng serverless na event-driven na transport
    - Mga halimbawa sa C#, TypeScript, at Python na may integrasyon ng Azure Functions
    - Mga pattern ng event-driven architecture para sa scalable na mga solusyon ng MCP
    - Mga receiver ng webhook at push-based na paghawak ng mensahe
  - **Azure Event Hubs Transport**: Implementasyon ng high-throughput streaming transport
    - Mga kakayahan para sa real-time streaming sa mga low-latency na senaryo
    - Mga estratehiya sa partitioning at pamamahala ng checkpoint
    - Pag-batch ng mensahe at pag-optimize ng performance
  - **Enterprise Integration Patterns**: Mga halimbawa ng arkitekturang handa na sa produksyon
    - Naipamahaging pagproseso ng MCP sa maraming Azure Functions
    - Hybrid na mga arkitekturang transport na pinagsasama ang iba't ibang uri ng transport
    - Katatagan ng mensahe, pagiging maaasahan, at mga estratehiya sa paghawak ng error
  - **Seguridad at Monitoring**: Azure Key Vault integration at mga pattern ng observability
    - Managed identity authentication at least privilege access
    - Application Insights telemetry at performance monitoring
    - Circuit breakers at mga pattern ng fault tolerance
  - **Testing Frameworks**: Komprehensibong mga estratehiya sa pagsusuri para sa mga custom transport
    - Unit testing gamit ang test doubles at mocking frameworks
    - Integration testing gamit ang Azure Test Containers
    - Mga konsiderasyon para sa performance at load testing

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Lumalagong Disiplina sa AI
- **README.md**: Komprehensibong eksplorasyon ng context engineering bilang isang lumalabang larangan
  - **Pangunahing Prinsipyo**: Kumpletong pagbabahagi ng konteksto, kamalayan sa desisyon ng aksyon, at pamamahala ng context window
  - **Pagkakatugma sa MCP Protocol**: Paano tinutugunan ng disenyo ng MCP ang mga hamon sa context engineering
    - Mga limitasyon ng context window at mga estratehiya ng progressive loading
    - Pagtukoy ng kaugnayan at dynamic na retrieval ng konteksto
    - Multi-modal na paghawak ng konteksto at mga konsiderasyon sa seguridad
  - **Mga Paraan sa Pagpapatupad**: Single-threaded kumpara sa multi-agent na mga arkitektura
    - Teknik sa pag-chunk at priyoritisasyon ng konteksto
    - Mga estratehiya ng progressive context loading at compression
    - Layered na mga pamamaraan ng konteksto at pag-optimize ng retrieval
  - **Framework ng Pagsusukat**: Mga lumalabas na metriko para sa ebalwasyon ng bisa ng konteksto
    - Kahusayan ng input, performance, kalidad, at mga konsiderasyon sa karanasan ng gumagamit
    - Mga eksperimental na paraan sa pag-optimize ng konteksto
    - Pagsusuri sa pagkabigo at mga metodolohiya sa pagpapabuti

#### Mga Update sa Navigation ng Kurikulum (README.md)
- **Pinahusay na Istruktura ng Module**: In-update ang talahanayan ng kurikulum upang isama ang mga bagong advanced na paksa
  - Idinagdag ang Context Engineering (5.14) at Custom Transport (5.15)
  - Konsistent na pag-format at mga link sa navigation sa lahat ng mga module
  - In-update ang mga paglalarawan upang ipakita ang kasalukuyang saklaw ng nilalaman

### Mga Pagpapabuti sa Istruktura ng Direktoryo
- **Standardisasyon ng Pangalan**: Pinalitan ang "mcp transport" ng "mcp-transport" upang maging konsistente sa iba pang mga folder ng advanced na paksa
- **Organisasyon ng Nilalaman**: Lahat ng 05-AdvancedTopics na mga folder ay ngayon sumusunod sa konsistent na pattern ng pangalan (mcp-[paksa])

### Mga Pagpapabuti sa Kalidad ng Dokumentasyon
- **Pagkakatugma sa MCP Specification**: Lahat ng bagong nilalaman ay sumasang-ayon sa kasalukuyang MCP Specification 2025-06-18
- **Mga Halimbawa sa Maramihang Wika**: Komprehensibong mga halimbawa ng code sa C#, TypeScript, at Python
- **Pokus sa Enterprise**: Mga pattern na handa na sa produksyon at integrasyon sa Azure cloud sa kabuuan
- **Visual na Dokumentasyon**: Mga diagram na Mermaid para sa arkitektura at visualisasyon ng daloy

## Agosto 18, 2025

### Komprehensibong Update sa Dokumentasyon - Mga Pamantayan ng MCP 2025-06-18

#### Pinakamahusay na Kasanayan sa Seguridad ng MCP (02-Security/) - Kumpletong Modernisasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Ganap na muling pagsulat na naaayon sa MCP Specification 2025-06-18
  - **Mga Mandatoring Pangangailangan**: Idinagdag ang tahasang MUST/MUST NOT na mga kinakailangan mula sa opisyal na espesipikasyon na may malinaw na mga visual indicator
  - **12 Pangunahing Kasanayan sa Seguridad**: Muling inistruktura mula sa 15-item list patungo sa komprehensibong mga domain ng seguridad
    - Seguridad ng Token at Pag-authenticate na may integrasyon ng external identity provider
    - Pamamahala ng Session at Seguridad ng Transport na may mga pangangailangang kriptograpiko
    - AI-Specific Threat Protection na may integrasyon ng Microsoft Prompt Shields
    - Kontrol ng Access at Mga Pahintulot na may prinsipyo ng least privilege
    - Kaligtasan ng Nilalaman at Monitoring na may integrasyon ng Azure Content Safety
    - Seguridad ng Supply Chain na may komprehensibong pag-verify ng mga bahagi
    - Seguridad ng OAuth at Pag-iwas sa Confused Deputy na may implementasyon ng PKCE
    - Pagtugon sa Insidente at Pag-recover na may mga automated na kakayahan
    - Pagsunod at Pamamahala na may pagsunod sa regulasyon
    - Mga Advanced Security Controls na may zero trust architecture
    - Integrasyon sa Microsoft Security Ecosystem na may komprehensibong mga solusyon
    - Patuloy na Ebolusyon ng Seguridad na may adaptive na mga kasanayan
  - **Mga Solusyon sa Seguridad ng Microsoft**: Pinahusay na gabay sa integrasyon para sa Prompt Shields, Azure Content Safety, Entra ID, at GitHub Advanced Security
  - **Mga Resources sa Pagpapatupad**: Inuri ang mga komprehensibong link ng resource ayon sa Official MCP Documentation, Mga Solusyon sa Seguridad ng Microsoft, Mga Pamantayan sa Seguridad, at Mga Gabay sa Pagpapatupad

#### Mga Advanced Security Controls (02-Security/) - Enterprise Implementation
- **MCP-SECURITY-CONTROLS-2025.md**: Kumpletong overhaul gamit ang enterprise-grade na security framework
  - **9 Komprehensibong Domain ng Seguridad**: Pinalawak mula sa mga basic controls tungo sa detalyadong enterprise framework
    - Advanced Authentication at Authorization na may integrasyon ng Microsoft Entra ID
    - Seguridad ng Token at Anti-Passthrough Controls na may komprehensibong beripikasyon
    - Mga Control sa Session Security na may pag-iwas sa hijacking
    - Mga AI-Specific Security Controls na may pag-iwas sa prompt injection at tool poisoning
    - Pag-iwas sa Confused Deputy Attack gamit ang seguridad ng OAuth proxy
    - Seguridad sa Pagpapatupad ng Tool gamit ang sandboxing at isolation
    - Mga Control sa Seguridad ng Supply Chain na may pag-verify ng dependencies
    - Mga Control sa Monitoring at Detection na may integrasyon ng SIEM
    - Pagtugon sa Insidente at Pag-recover na may mga automated na kakayahan
  - **Mga Halimbawa sa Pagpapatupad**: Idinagdag ang detalyadong mga YAML configuration blocks at mga halimbawa ng code
  - **Integrasyon ng Mga Solusyon ng Microsoft**: Komprehensibong coverage ng Azure security services, GitHub Advanced Security, at enterprise identity management

#### Seguridad sa Mga Advanced na Paksa (05-AdvancedTopics/mcp-security/) - Handang-handa para sa Produksyon na Pagpapatupad
- **README.md**: Kumpletong muling pagsulat para sa enterprise security implementation
  - **Pagkakatugma sa Kasalukuyang Espesipikasyon**: In-update ayon sa MCP Specification 2025-06-18 na may mga mandatoring kinakailangan sa seguridad
  - **Pinahusay na Pag-authenticate**: Integrasyon ng Microsoft Entra ID na may komprehensibong .NET at Java Spring Security na mga halimbawa
  - **Integrasyon ng AI Security**: Implementasyon ng Microsoft Prompt Shields at Azure Content Safety na may detalyadong mga halimbawa sa Python
  - **Advanced Threat Mitigation**: Komprehensibong mga halimbawa ng pagpapatupad para sa
    - Pag-iwas sa Confused Deputy Attack gamit ang PKCE at pagsuri sa pahintulot ng user
    - Pag-iwas sa Token Passthrough gamit ang audience validation at secure token management
    - Pag-iwas sa Session Hijacking gamit ang cryptographic binding at behavioral analysis
  - **Integrasyon sa Enterprise Security**: Azure Application Insights monitoring, mga pipeline ng pagtuklas ng banta, at seguridad ng supply chain
  - **Checklist sa Pagpapatupad**: Malinaw na mga mandatoring vs. inirerekomendang mga kontrol sa seguridad na may mga benepisyo sa Microsoft security ecosystem

### Kalidad ng Dokumentasyon at Pagkakatugma sa Pamantayan
- **Mga Sanggunian ng Espesipikasyon**: In-update ang lahat ng sanggunian sa kasalukuyang MCP Specification 2025-06-18
- **Ecosystem ng Seguridad ng Microsoft**: Pinahusay na gabay sa integrasyon sa lahat ng dokumentasyon sa seguridad
- **Praktikal na Pagpapatupad**: Idinagdag ang detalyadong mga halimbawa ng code sa .NET, Java, at Python na may mga pattern ng enterprise
- **Organisasyon ng Resource**: Komprehensibong kategorizasyon ng opisyal na dokumentasyon, mga pamantayan sa seguridad, at mga gabay sa pagpapatupad
- **Mga Visual Indicator**: Malinaw na pagmamarka ng mga mandatoring kinakailangan kumpara sa mga inirerekomendang kasanayan


#### Pangunahing Konsepto (01-CoreConcepts/) - Kumpletong Modernisasyon
- **Pag-update ng Bersyon ng Protocol**: In-update upang tukuyin ang kasalukuyang MCP Specification 2025-06-18 na may petsa-batay na bersyon (format na YYYY-MM-DD)
- **Pagpino ng Arkitektura**: Pinalakas na mga paglalarawan ng Hosts, Clients, at Servers upang ipakita ang mga kasalukuyang pattern ng arkitektura ng MCP
  - Ang mga Hosts ay malinaw na tinukoy bilang mga AI application na nagko-coordinate ng maraming koneksyon ng MCP client
  - Ang mga Clients ay inilalarawan bilang mga protocol connector na nagpapanatili ng one-to-one na relasyon sa server
  - Ang mga Servers ay pinahusay na may mga senaryo ng deployment na lokal kumpara sa remote
- **Bagong Istruktura ng Primitives**: Kumpletong overhaul ng server at client primitives
  - Server Primitives: Mga Resources (pinagmumulan ng data), Prompts (mga template), Tools (mga executable functions) na may detalyadong paliwanag at mga halimbawa
  - Client Primitives: Sampling (LLM completions), Elicitation (pag-input ng user), Logging (debugging/monitoring)
  - In-update gamit ang kasalukuyang mga pamamaraan ng discovery (`*/list`), retrieval (`*/get`), at execution (`*/call`)
- **Arkitektura ng Protocol**: Inilunsad ang two-layer architecture model
  - Data Layer: JSON-RPC 2.0 na pundasyon na may lifecycle management at mga primitives
  - Transport Layer: STDIO (lokal) at Streamable HTTP na may SSE (remote) na mga mekanismo ng transport
- **Framework ng Seguridad**: Komprehensibong mga prinsipyo ng seguridad kabilang ang tahasang pahintulot ng user, proteksyon sa privacy ng data, kaligtasan sa pagpapatupad ng tool, at seguridad sa transport layer
- **Mga Pattern ng Komunikasyon**: In-update ang mga mensahe ng protocol upang ipakita ang initialization, discovery, execution, at notification flows
- **Mga Halimbawa ng Code**: Na-refresh ang mga multi-language na halimbawa (.NET, Java, Python, JavaScript) upang ipakita ang kasalukuyang mga pattern ng MCP SDK

#### Seguridad (02-Security/) - Kumpletong Overhaul ng Seguridad  
- **Pagkakatugma sa Pamantayan**: Ganap na pagkakatugma sa mga kinakailangan sa seguridad ng MCP Specification 2025-06-18
- **Ebolusyon ng Pag-authenticate**: Naidokumento ang pagbabago mula sa custom OAuth servers patungo sa external identity provider delegation (Microsoft Entra ID)
- **Pagsusuri ng AI-Specific Threat**: Pinahusay na saklaw ng mga modernong AI attack vectors
  - Detalyadong mga senaryo ng prompt injection attack na may mga totoong halimbawa
  - Mga mekanismo ng tool poisoning at mga pattern ng "rug pull" attack
  - Pagkalason ng context window at mga pag-atake sa pagkalito ng modelo
- **Mga Solusyon sa Seguridad ng Microsoft AI**: Komprehensibong saklaw ng Microsoft security ecosystem
  - AI Prompt Shields na may advanced na pagtuklas, spotlighting, at delimiter techniques
  - Mga pattern ng integrasyon ng Azure Content Safety
  - GitHub Advanced Security para sa proteksyon ng supply chain
- **Advanced Threat Mitigation**: Detalyadong mga kontrol sa seguridad para sa
  - Session hijacking na may mga senaryo ng pag-atake na espesipiko sa MCP at mga kinakailangan sa cryptographic session ID
  - Mga problema sa Confused Deputy sa mga MCP proxy scenario na may tahasang mga kinakailangan sa pahintulot
  - Mga kahinaan sa token passthrough na may mga mandatoring kontrol sa beripikasyon
- **Seguridad sa Supply Chain**: Pinalawak na saklaw ng AI supply chain kasama na ang foundation models, embeddings services, context providers, at third-party APIs
- **Seguridad ng Foundation**: Pinahusay na integrasyon gamit ang mga pattern ng seguridad sa enterprise kabilang ang zero trust architecture at Microsoft security ecosystem
- **Organisasyon ng mga Resource**: Inuri ang mga komprehensibong link ng resource ayon sa uri (Opisyal na Docs, Pamantayan, Pananaliksik, Microsoft Solutions, Gabay sa Pagpapatupad)

### Mga Pagpapahusay sa Kalidad ng Dokumentasyon
- **Mga Layunin sa Pagkatuto na Istruktura**: Pinahusay ang mga layunin sa pagkatuto na may mga partikular at aksyonableng resulta 
- **Cross-References**: Idinagdag ang mga link sa pagitan ng mga kaugnay na paksang seguridad at pangunahing konsepto
- **Kasalukuyang Impormasyon**: In-update lahat ng mga sanggunian ng petsa at mga link ng espesipikasyon sa kasalukuyang mga pamantayan 
- **Gabay sa Pagpapatupad**: Idinagdag ang partikular at aksyonableng mga alituntunin sa pagpapatupad sa buong parehong mga seksyon

## Hulyo 16, 2025

### Mga Pagpapahusay sa README at Navigation
- Ganap na muling dinisenyo ang navigation ng kurikulum sa README.md
- Pinalitan ang mga `<details>` tag ng mas madaling table-based na format
- Nilikha ang mga alternatibong layout options sa bagong folder na "alternative_layouts"
- Idinagdag ang mga halimbawa ng card-based, tabbed-style, at accordion-style navigation
- In-update ang seksyon ng istruktura ng repository upang isama ang lahat ng pinakabagong mga file
- Pinahusay ang seksyon na "Paano Gamitin ang Kurikulum" na may malinaw na mga rekomendasyon
- In-update ang mga link ng MCP specification upang ituro sa tamang mga URL
- Idinagdag ang seksyon ng Context Engineering (5.14) sa istruktura ng kurikulum

### Mga Update sa Gabay sa Pag-aaral
- Ganap na nirebisa ang gabay sa pag-aaral upang umayon sa kasalukuyang istruktura ng repository
- Idinagdag ang mga bagong seksyon para sa MCP Clients at Tools, at Mga Popular na MCP Servers
- In-update ang Visual Curriculum Map upang tumpak na ipakita lahat ng mga paksa
- Pinahusay ang mga paglalarawan ng Mga Advanced na Paksa upang masaklaw ang lahat ng mga espesyalisadong larangan
- In-update ang seksyon ng Case Studies upang ipakita ang aktuwal na mga halimbawa
- Idinagdag ang komprehensibong changelog na ito

### Mga Ambag ng Komunidad (06-CommunityContributions/)
- Idinagdag ang detalyadong impormasyon tungkol sa mga MCP server para sa paggawa ng imahe
- Idinagdag ang komprehensibong seksyon sa paggamit ng Claude sa VSCode
- Idinagdag ang mga tagubilin para sa pag-setup at paggamit ng Cline terminal client
- In-update ang seksyon ng MCP client upang isama ang lahat ng mga popular na opsyon sa client
- Pinahusay ang mga halimbawa ng kontribusyon na may mas tumpak na mga sample ng code

### Mga Advanced na Paksa (05-AdvancedTopics/)
- Inayos ang lahat ng mga espesyalisadong folder ng paksa na may konsistent na pag-pangalan
- Idinagdag ang mga materyales at mga halimbawa ng context engineering
- Idinagdag ang dokumentasyon ng integrasyon ng Foundry agent
- Pinahusay ang dokumentasyon ng integrasyon ng seguridad ng Entra ID

## Hunyo 11, 2025

### Paunang Paglikha
- Inilabas ang unang bersyon ng MCP for Beginners curriculum

- Nilikha ang pangunahing istruktura para sa lahat ng 10 pangunahing seksyon
- Ipinatupad ang Visual Curriculum Map para sa pag-navigate
- Nagdagdag ng mga paunang sample na proyekto sa iba't ibang programming languages

### Pagsisimula (03-GettingStarted/)
- Nilikha ang unang mga halimbawa ng server implementation
- Nagdagdag ng patnubay sa pag-develop ng kliyente
- Isinama ang mga tagubilin para sa LLM client integration
- Nagdagdag ng dokumentasyon para sa VS Code integration
- Ipinatupad ang mga halimbawa ng Server-Sent Events (SSE) server

### Mga Pangunahing Konsepto (01-CoreConcepts/)
- Nagdagdag ng detalyadong paliwanag tungkol sa client-server architecture
- Nilikha ang dokumentasyon sa mga pangunahing bahagi ng protocol
- Na dokumento ang mga messaging pattern sa MCP

## Mayo 23, 2025

### Istruktura ng Repository
- Inisyalisa ang repositoryo gamit ang pangunahing istruktura ng folder
- Nilikha ang mga README file para sa bawat malaking seksyon
- Naitakda ang imprastruktura ng pagsasalin
- Nagdagdag ng mga larawan at diagram

### Dokumentasyon
- Nilikha ang paunang README.md na may overview ng kurikulum
- Nagdagdag ng CODE_OF_CONDUCT.md at SECURITY.md
- Naitakda ang SUPPORT.md na may patnubay para sa pagkuha ng tulong
- Nilikha ang paunang istruktura ng gabay sa pag-aaral

## Abril 15, 2025

### Pagpaplano at Balangkas
- Paunang pagpaplano para sa MCP para sa mga Nagsisimula na kurikulum
- Tinukoy ang mga layunin sa pag-aaral at target na madla
- Inilatag ang 10-seksyong istruktura ng kurikulum
- Bumuo ng konseptwal na balangkas para sa mga halimbawa at case studies
- Nilikha ang paunang prototype na mga halimbawa para sa mga pangunahing konsepto

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
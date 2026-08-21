# Badiliko: MCP kwa Mtaala wa Waanzilishi

Hati hii inahudumu kama kumbukumbu ya mabadiliko yote muhimu yaliyofanywa katika mtaala wa Model Context Protocol (MCP) kwa Waanzilishi. Mabadiliko yameandikwa kwa mpangilio wa kinyume wa tarehe (mabadiliko mapya kwanza).

## Julai 29, 2026

### Msaidizi Mpya wa Moduli 08: Vijiko vya Uaminifu na Jaribio Salama la Kurudia

Iliongezwa somo la msaidizi huru kwa zana za MCP zinazozalisha athari halisi duniani,
zinazolingana na sifa ya mwisho ya `2026-07-28`.

- **Mpya**: [somu la msaidizi wa vijiko vya uaminifu][reliability-sidecar]
  linatumia hadithi moja ya tiketi ya msaada, michoro miwili ya Mermaid, na mtiririko wa maamuzi ya jaribio la kurudia
  kuelezea funguo za uendeshaji thabiti, kuingilia mara mbili kwa atomi,
  mrekebisho, ushahidi, na kikomo cha nyongeza za Kazi.
- **Mpya**: Mazoezi ya sindano ya hitilafu ya Python na SQLite ya maktaba ya kawaida
  yanatumia maghala tofauti ya operesheni na tiketi kuonyesha jibu lililopotea
  baada ya athari ya nje kukamilika. Majaribio sita ya zamani yanashughulikia marudio yasiyo na busara,
  urejesho wa kuanzisha salama, migongano ya mizigo, matokeo yaliyohifadhiwa,
  madai ya moja kwa moja, na kuingilia mara mbili kwa wakati mmoja.
- **Imeboreshwa**: Moduli 08 sasa inahusisha somo la msaidizi, hutambua
  mfano wa ombi la bila jimbo la mwisho `2026-07-28`, hutofautisha uangalizaji wa OpenTelemetry
  kutoka kwa kipengele kilichopitwa cha kurekodi cha MCP, na hupunguza
  mfano wa kurudia kwa ujumla kwa operesheni za kusoma tu.
- **Hiari**: Somo linaoanisha dhana zake rahisi kwa utekelezaji mmoja unaotambulishwa na jamii
  bila kufanya huduma iliyohudumiwa au wito wa mtandao kuwa sehemu ya
  zoezi.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## Julai 2, 2026

### Somo Jipya: Mgombea wa Kutolewa wa Sifa ya MCP ya 2026-07-28

Iliongeza mwanga juu ya mgombea wa sifa ya MCP ya kutolewa (iliyotangazwa Mei 21, 2026; utoaji wa mwisho umepangwa Julai 28, 2026), iliyo muhtasari kutoka kwa [chapisho rasmi la tangazo la blogi](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Msingi wa mtaala unabaki **MCP Specification 2025-11-25** hadi toleo jipya litakapotangazwa, hivyo hili linaletwa kama mwongozo wa mbele badala ya kuandika upya masomo yaliyopo.

- **Mpya**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — somo kamili linaloshughulikia msingi wa mkataba usio na jimbo (kuondoa salamu ya `initialize` na `Mcp-Session-Id`), vichwa vya maelekezo vipya vya `Mcp-Method`/`Mcp-Name`, metadata ya kuhifadhi `ttlMs`/`cacheScope`, Muktadha wa W3C Trace katika `_meta`, mfumo rasmi wa Nyongeza (MCP Apps na nyongeza mpya ya Kazi), SEP sita za kuimarisha vibali, kuachwa nyuma kwa Roots/Sampling/Logging, na kuhamia kwenye Mfumo Kamili wa JSON 2020-12 kwa schemas za zana.
- **Imeboreshwa** na viungo vinavyoelekeza somo jipya:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): maelezo ya toleo la mkataba, sehemu za Sampling/Roots/Logging/Tasks, na "Nini Kifuatavyo"
  - [02-Security/README.md](./02-Security/README.md): maelezo ya kuimarisha vibali
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): maelezo ya usafiri usio na jimbo
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): maelezo ya kuachwa nyuma kwa Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): maelezo ya kuachwa nyuma kwa Logging na nyongeza ya Kazi
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): maelezo ya usafiri/usambazaji wa kikao usio na jimbo
  - [README.md](./README.md): maelezo ya "Kuangalia mbele" katika sehemu ya sifa na kipengele kipya cha `1.1` katika jedwali la moduli ya mtaala
  - [study_guide.md](./study_guide.md): kipengele cha mbele chini ya muhtasari wa Dhana za Msingi na noti ya nyongeza iliyo na tarehe
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): maelezo juu ya ramani ya usafiri ya `mcp-session-id` kabla ya mfano wa ombi usio na jimbo
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): maelezo ya muhtasari wa moduli kuhusu kuachwa nyuma kwa Muktadha wa Mizuizi/Sampling na nyongeza ya Kazi
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): maelezo ya kuimarisha vibali

## Juni 24, 2026

### Somo Jipya: Kutumia MCP katika app ya Copilot

- [Sehemu ya Zana](./12-tooling/README.md) Iliongeza sehemu ya zana.
- [MCP katika app ya Copilot](./12-tooling/01-copilot-app/README.md)

## Juni 16, 2026

### Ulinganifu wa Sifa za MCP & Uthibitishaji wa Sampuli

Ulithibitisha mtaala dhidi ya **MCP Specification 2025-11-25** ya sasa na SDK rasmi za hivi karibuni, kisha kusahihisha marejeleo ya sifa zilizopitwa na kuhakikisha sampuli za msingi bado zinaweza kujengwa na kuendeshwa.

#### Marekebisho ya Toleo la Sifa (2025-06-18 / 2025-03-26 → 2025-11-25)

Iliboresha maudhui ya Kiingereza ambapo bado yalidai marekebisho ya sifa ya zamani kuwa *kiwango cha sasa/kibunifu*, na kuunganisha viungo kwenye njia za sifa za kipekee `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Imeboresha bango la "Kiwango cha Sasa", utangulizi, kichwa cha kanuni za msingi za usalama, kichwa cha mahitaji ya lazima, sehemu ya Microsoft Entra ID, viungo vya Marejeleo & Rasilimali, na tangazo la usalama la kufunga (marejeleo 8) hadi 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Imeboresha kiungo cha rasilimali ya ziada cha sifa na bango la "Kiwango cha Sasa" hadi 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Ilibadilisha kiungo cha zamani `2025-03-26` cha usalama-na-aminika kuwa ukurasa wa mbinu bora za usalama wa 2025-11-25
- **03-GettingStarted/14-sampling/README.md**: Imeboresha kiungo rasmi cha nyaraka za sampuli hadi 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Imesasisha rejea ya "malighafi ya MCP ya sasa" kwa wakati uliopo na kiungo cha rasilimali Zaidi za Maelezo kwa tarehe 2025-11-25 (maelezo ya kihistoria ya SSE-kuachwa yamehifadhiwa kwa usahihi)

#### Uthibitishaji wa Sampuli dhidi ya SDK za Sasa

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` ilisuluhisha `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` ilipita bila makosa ya aina — APIs zilizopo za `McpServer`/`StdioServerTransport` zinaendelea kuwa halali
- **Python (03-GettingStarted/01-first-server/solution/python)**: Imethibitishwa katika `.venv` waliyo peke yake na `mcp[cli]` (1.27.2); `py_compile` ilipita na `FastMCP.list_tools()` ilirudisha kwa usahihi zana za `add` na `subtract`
- Imethibitisha kuwa anuwai zote za toleo la sampuli `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) husuluhishwa vizuri hadi toleo la sasa `1.29.0` bila mabadiliko ya kuvunja API

#### Muafaka wa Pin wa Kutegemea (kufunga mapengo ya matoleo)

Iliinua pini za SDK zilizochakaa ili kila sampuli ifuatilie toleo la sasa la MCP, ikilingana na muktadha wa hifadhidata nzima:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Iliinua `@modelcontextprotocol/sdk` kutoka `^1.8.0` → `>=1.26.0` na kusasisha maelezo ya kifurushi yaliyochakaa `"updated for MCP 2025-06-18"` kuwa `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** na **lab4/code/github_mcp_server/pyproject.toml**: Iliinua pini sahihi `mcp==1.23.0` → `mcp>=1.26.0`; ikazalisha upya faili zote mbili za `uv.lock` (`uv lock`) ili lockfiles zizule toleo la sasa `mcp 1.27.2` na kuendelea kushikamana na maelezo

#### Uchambuzi wa Mapengo ya Mtaala — Ufungaji wa Kipengele cha Spec cha Hivi Karibuni

Imethibitisha kuwa mtaala tayari unafunika primitives zote zilizowasilishwa/kupanuliwa katika MCP 2025-11-25, hivyo hakuna mapengo ya maudhui yaliyobaki:
- **Sampling**: Somo 03-GettingStarted/14-sampling pamoja na 05-AdvancedTopics/mcp-sampling
- **Elicitation (yakiwemo mode ya URL)**: Imeandikwa katika 01-CoreConcepts na 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Imeandikwa katika 00-Introduction, 01-CoreConcepts, na 05-AdvancedTopics/mcp-root-contexts
- **Tasks (jaribio, operesheni za muda mrefu)**: Imeandikwa katika 01-CoreConcepts na 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Imeandikwa katika 01-CoreConcepts na 05-AdvancedTopics/mcp-protocol-features

### Kuimarisha Usalama & Uboreshaji wa Udhaifu wa Kutegemea

Ilifanya ukaguzi wa usalama kamili katika kila faili la kutegemea na msimbo wa chanzo wa sampuli, kisha ikarekebisha taarifa zote za tahadhari za npm zilizoripotiwa na hitilafu moja ya ngazi ya msimbo. Baada ya marekebisho, `npm audit` inaripoti **0 udhaifu** katika kila saraka iliyoangaliwa.

#### Udhaifu wa Kuwategemea wa npm (wasambazaji) — Imerekebishwa

Ilikagua faili zote 15 za `package-lock.json` zilizowekwa. Udhaifu ulikuwa kwa kutegemea wasambazaji waliotumika katika zana wa MCP Inspector ya maendeleo, kliente wa OpenAI, na MCP SDK; yote sasa yamesuluhishwa bila kuvunja sampuli:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** na **lab3/code/weather_mcp/inspector**: Iliinua `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), ambayo ilisuluhisha tahadhari zilizoambatanishwa za `ajv`, `brace-expansion`, `diff`, `path-to-regexp` na `ws`. Iliongeza kipengele cha `overrides` cha npm kilicholazimisha toleo lililorejeshwa la `shell-quote@1.8.4` kuondoa tahadhari muhimu iliyobaki iliyoletwa na `concurrently`; kufuatilia upya lockfiles zote mbili (sasa 0 udhaifu)
- **03-GettingStarted/samples/typescript**: `npm audit fix` ilisahihisha `qs` (katikati) katika wasambazaji zisizotegemea moja kwa moja
- **03-GettingStarted/samples/javascript**: `npm audit fix` ilisahihisha `hono` (katikati) katika wasambazaji zisizotegemea moja kwa moja
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` ilisahihisha `form-data` (juu) katika wasambazaji zisizotegemea moja kwa moja
- **03-GettingStarted/11-simple-auth/solution/typescript**: Ilizalisha `package-lock.json` iliyokosekana ili mradi uweze kutengenezwa upya na kuangaliwa (0 udhaifu)

#### Marekebisho ya Usalama ya Ngazi ya Msimbo (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Iliondoa `shell=True` kutoka kwa zana `open_in_vscode`. `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` iliyopita iliruhusu vigezo vya shell katika njia ya folda kufasiriwa na `cmd.exe` (njia ya kuingiza amri). Sasa inanzisha moja kwa moja `Code.exe` iliyotambuliwa na folda kama hoja — bila shell — ambayo ni sawa kivitendo na salama

#### Ukaguzi wa Kutegemea kwa Python

- Ilikagua kila seti ya mahitaji ya Python kwa kutumia `pip-audit`. `05-AdvancedTopics` na `03-GettingStarted/samples/python` ziliripoti **hakuna udhaifu unaojulikana** (anuwai zao `mcp` / `httpx` / `pydantic` / `python-dotenv` husuluhishwa hadi matoleo yaliyopachikwa ya sasa)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` ilibaini kutegemea zisizozidi moja kwa moja **`werkzeug` 3.1.1** na tahadhari tatu za DoS za jina la kifaa cha Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, na `CVE-2026-27199` (zote zilisahihishwa katika 3.1.6). Iliongeza pini ya usalama wazi `werkzeug>=3.1.6` ili toleo lililosahihishwa lisuluhishwe; imethibitisha sharti lina suluhishwa vizuri na stack ya `chainlit` / `mcp` / `semantic-kernel`

### Kubadilisha Jina la Bidhaa

Imesasisha maudhui yote ya mtaala kuakisi ubadilishaji wa jina la bidhaa la Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Iliunganisha jamii ya Discord imesasishwa

- **AGENTS.md**: Marejeo ya seva ya Discord yameboreshwa
- **README.md**: Marejeo ya mfumo wa teknolojia yameboreshwa
- **study_guide.md**: Marejeo ya masomo ya kesi yameboreshwa
- **05-AdvancedTopics/README.md**: Kichwa na maelezo ya Moduli 5.13 yameboreshwa
- **05-AdvancedTopics/mcp-integration/README.md**: Sehemu ya kichwa na maelezo yameboreshwa
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Kichwa kikamilifu cha moduli na maudhui yameboreshwa
- **05-AdvancedTopics/mcp-security-entra/README.md**: Kiungo cha rejea cha kuvuka kimeboreshwa
- **07-LessonsfromEarlyAdoption/README.md**: Marejeo ya masomo ya kesi yameboreshwa
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Kichwa cha Sehemu 9, bagesi, na uwezo vimeboreshwa
- **08-BestPractices/README.md**: Kiungo cha jumuiya ya Discord kimeboreshwa
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Rejea ya chaneli ya Discord imeboreshwa
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Rejea ya uanzishaji wa mfano imeboreshwa
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Jedwali la Huduma za AI limeboreshwa
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Marejeo ya rasilimali yameboreshwa

#### AI Toolkit / AITK → Ugani wa Zana za Microsoft Foundry kwa VS Code
- **README.md**: Marejeo makuu ya mtaala yameboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Kichwa cha moduli, muhtasari, na vichwa vyote vya moduli vimeboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Kichwa, malengo ya kujifunza, maagizo ya usanidi, na rasilimali vimeboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Kichwa, malengo ya kujifunza, jedwali la wenyeji wa MCP, na marejeo ya kuvuka vimeboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Kichwa, bagesi, masharti ya awali, na rasilimali vimeboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Marejeo ya Mjenzi wa Wakala na kiungo cha maoni yameboreshwa
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Masharti ya awali na marejeo ya ugani yameboreshwa

---

## Aprili 11, 2026

### Somo Jipya, Marekebisho ya Nyaraka, na Sasisho za Utegemezi

#### Maudhui Mapya ya Mtaala Yameongezwa

**Moduli 05 - Mada Zinazopendelea**
- **Somo 5.17: Mafanikio ya Wakala Wengi wa Kupaligana kwa kutumia MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Mwongozo mpya kamili unaofunika muundo wa mabishano ya wapinzani kwa mifumo ya mawakala wengi
  - Mchoro wa usanifu wa Mermaid: mawakala wawili → seva ya zana ya MCP ya pamoja → manukuu ya mabishano → hakimu → uamuzi
  - Seva ya zana ya MCP ya pamoja (`web_search` + `run_python`) imeandaliwa kwa Python na TypeScript
  - Maelekezo ya mifumo inayopingana (KWA / DHIDI YA / Hakimu) yenye mahitaji ya matumizi ya zana waziwazi
  - Msimamizi wa mabishano katika Python, TypeScript, na C# anayesimamia raundi na usambazaji wa hoja
  - Uunganishaji wa MCP `ClientSession` kwa msimamizi kwa simu halisi za zana
  - Jedwali la matumizi (ugundaji wa hali ya kufikirika, mfano wa tishio, marekebisho ya muundo wa API, uhakiki wa ukweli, uteuzi wa teknolojia)
  - Mambo ya usalama: utekelezaji wa sandboxed, uthibitishaji wa simu za zana, ukomo wa kiwango, ufuatiliaji wa kuri
  - Mazoezi yaliyo elekezwa na miundo mitatu ya vitendo (ukaguzi wa msimbo, uamuzi wa usanifu, ukaguzi wa maudhui)

#### Marekebisho ya Nyaraka

**Moduli 03 - Kuanza**
- **05-stdio-server/README.md**: Mfano wa seva ya stdio ya TypeScript uliokamilika umeboreshwa — umeongeza kuanzishwa kwa usafirishaji uliokosekana (`new StdioServerTransport()`) na simu ya `server.connect(transport)` ili kufanana na mifano ya Python na .NET katika sehemu hiyo hiyo
- **14-sampling/README.md**: Kosa la tahajia limec corrected — kutoka `"Sampling is an davanced features"` hadi `"Sampling is an advanced feature"`

#### Sasisho za Mtaala

**README.md Kuu**
- Kuingiza kipengele 5.17 (Mafanikio ya Wakala Wengi wa Kupaligana kwa kutumia MCP) kwenye jedwali la mtaala kwa kiungo moja kwa moja kwa somo jipya

**05-AdvancedTopics/README.md**
- Kuongeza mstari wa Somo 5.17 kwenye jedwali la masomo

**study_guide.md**
- Kuongeza mada ya Mafanikio ya Wakala Wengi wa Kupaligana katika ramani ya akili na maelezo ya maandishi ya Mada Zinazopendelea

#### Marekebisho ya Msimbo na Usalama

**Moduli 05 - Wakala Wapinzani (`mcp-adversarial-agents`)**
- **Marekebisho ya usalama — sindano ya amri**: Imebadilisha uingizaji wa `execSync` wa shell na `execFile` + `promisify` katika zana ya `run_python` ya TypeScript, kuondoa hatari ya sindano ya amri (sasa msimbo unaodhibitiwa na LLM hupitishwa kama kipengele cha argv kisicho cha shell)
- **Uunganishaji wa mzunguko wa zana za MCP**: Imesasisha msimamizi wa mabishano wa Python kutumia mteja wa `AsyncAnthropic` (kubadilisha `Anthropic` ya kufunga), kupitisha `ClientSession` hai moja kwa moja kwa kila zamu ya wakala, kupata maelezo ya zana kupitia `session.list_tools()` kila zamu, na kusambaza vifungu vya `tool_use` kupitia `session.call_tool()` kwa mzunguko hadi mfano utoe jibu la mwisho la maandishi

#### Sasisho za Utegemezi

- Kupanua toleo la `hono` hadi 4.12.12 katika vifurushi vingi (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Kupanua `@hono/node-server` kutoka 1.19.11 hadi 1.19.13 katika vifurushi vya TypeScript
- Kupanua `cryptography` kutoka 46.0.5 hadi 46.0.7 katika vifurushi vya Python (maabara 3 na 4 za 10-StreamliningAIWorkflows)
- Kupanua `lodash` kutoka 4.17.23 hadi 4.18.1 katika mtambuizaji wa 10-StreamliningAIWorkflows

#### Tafsiri

- Kumalizia tafsiri kwa lugha zaidi ya 48 kulingana na mabadiliko ya chanzo (sasisho la i18n)

---

## Februari 5, 2026

### Uthibitishaji na Maboresho ya Urambazaji katika Hifadhidata Yote

#### Maudhui Mapya ya Mtaala Yameongezwa

**Moduli 03 - Kuanza**
- **12-mcp-hosts/README.md**: Mwongozo mpya kamili wa usanidi wa wenyeji wa MCP
  - Mifano ya usanidi ya Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Sampuli za usanidi za JSON kwa wenyeji wakuu wote
  - Jedwali la kulinganisha aina za usafirishaji (stdio, SSE/HTTP, WebSocket)
  - Utatuzi wa matatizo ya kawaida ya muunganisho
  - Mbinu bora za usalama kwa usanidi wa mwenyeji

- **13-mcp-inspector/README.md**: Mwongozo mpya wa usahihishaji kwa MCP Inspector
  - Njia za usakinishaji (npx, npm global, kutoka chanzo)
  - Kuunganisha na seva kupitia stdio na HTTP/SSE
  - Vifaa vya majaribio, rasilimali, na mtiririko wa maelekezo
  - Uunganisho wa VS Code na MCP Inspector
  - Sehemu za kawaida za kusahihisha makosa na suluhisho

**Moduli 04 - Utekelezaji wa Kivitendo**
- **pagination/README.md**: Mwongozo mpya wa utekelezaji wa ukurasa
  - Mifumo ya ukurasa unaotumia cursor katika Python, TypeScript, Java
  - Usimamizi wa ukurasa upande wa mteja
  - Mikakati ya muundo wa cursor (isiyoonekana dhidi ya yenye muundo)
  - Mapendekezo ya uboreshaji wa utendaji

**Moduli 05 - Mada Zinazopendelea**
- **mcp-protocol-features/README.md**: Uchunguzi wa kina wa sifa za itifaki
  - Utekelezaji wa arifa za maendeleo
  - Mifumo ya kughairi ombi
  - Sampuli za rasilimali zenye mifumo ya URI
  - Usimamizi wa mzunguko wa maisha ya seva
  - Udhibiti wa viwango vya kuandika kumbukumbu
  - Mifumo ya kushughulikia makosa na nambari za JSON-RPC

#### Marekebisho ya Urambazaji (faili 24+ zimerudiwa)

**README Kuu za Moduli**
 Sasa zina kiungo kwa somo la kwanza NA moduli inayofuata

**Faili ndogo za Usalama 02**
- Hati zote 5 za ziada za usalama sasa zina urambazaji wa "Kitu Kifuatayo ni Nini":

**Faili za 09-CaseStudy**
- Faili zote za masomo ya kesi sasa zina urambazaji mfuatano:

**Maabara 10-StreamliningAI**
Imekuwa na sehemu ya Kitu Kifuatayo ni Nini kwenye muhtasari wa Moduli 10 na Moduli 11

#### Marekebisho ya Msimbo na Maudhui

**Sasisho la SDK na Utegemezi**
Toleo la wazi la openai limesahihishwa kuwa `^4.95.0`
SDK imesasishwa kutoka `^1.8.0` hadi `>=1.26.0`
Vigezo vya toleo la mcp vimesasishwa hadi `>=1.26.0`

**Marekebisho ya Msimbo**
Toleo lisilo halali la mfano `gpt-4o-mini` limesahihishwa kuwa `gpt-4.1-mini`

**Marekebisho ya Maudhui**
Kiungo kilichovunjika `READMEmd` → `README.md` kimesahihishwa, kichwa cha mtaala `Module 1-3` → `Module 0-3` kimesahihishwa, njia yenye mtazamo wa herufi imeboreshwa
Maudhui rudufu ya masomo ya kesi 5 yaliyoharibika yameondolewa

**Marekebisho ya Mwongozo kwa Mwanzo**
Maelezo sahihi, malengo ya kujifunza, na masharti ya awali kwa wanaoanza yameongezwa

#### Sasisho za Mtaala

**README.md Kuu**
- Kuingiza vipengele 3.12 (Wenyeji wa MCP), 3.13 (Mkaguzi wa MCP), 4.1 (Pagination), 5.16 (Sifa za Itifaki) kwenye jedwali la mtaala

**README za Moduli**
Masomo 12 na 13 yameongezwa kwenye orodha ya masomo
Sehemu ya Mwongozo wa Vitendo na kiungo cha pagination yameongezwa
Masomo 5.15 (Usafirishaji Maalum) na 5.16 (Sifa za Itifaki) yameongezwa

**study_guide.md**
- Ramani ya akili imesasishwa kwa mada zote mpya: Usanidi wa Wenyeji wa MCP, Mkaguzi wa MCP, Mikakati ya Pagination, Uchunguzi wa Kina wa Sifa za Itifaki

## Jan 28, 2026

### Ukaguzi wa Uzingatiaji wa Vipimo vya MCP 2025-11-25

#### Uboreshaji wa Dhana za Msingi (01-CoreConcepts/)
- **Kipengele Kipya cha Mteja - Roots**: Nyaraka kamili juu ya kipengele cha mteja wa Roots, kuwezesha seva kuelewa mipaka ya mfumo wa faili na ruhusa za upatikanaji
- **Maelezo ya Zana**: Nyaraka juu ya maelezo ya tabia za zana (`readOnlyHint`, `destructiveHint`) kwa maamuzi bora ya utekelezaji wa zana
- **Simu za Zana katika Uchimbaji**: Nyaraka ya Uchimbaji imeboreshwa kujumuisha vigezo `tools` na `toolChoice` kwa mwongozo wa matumizi ya zana wakati wa maombi ya uchimbaji
- **Njia ya Mode ya URL**: Nyaraka juu ya mjadala wa kuanzisha maingiliano ya wavuti ya nje unaoanzishwa na seva kwa kuzingatia URL
- **Mchakato wa Kazi (Jaribio)**: Sehemu mpya ya nyaraka ya kipengele cha Kazi za majaribio kwa vikavu vya utekelezaji na upokeaji wa matokeo yaliyochelewa
- **Msaada wa Ikoni**: Zana, rasilimali, sampuli za rasilimali, na maelekezo sasa zinaweza kujumuisha ikoni kama metadata ya ziada

#### Marekebisho ya Nyaraka
- **README.md**: Kuingiza kielezo cha toleo la MCP Specification 2025-11-25 na maelezo ya toleo kulingana na tarehe
- **study_guide.md**: Ramani ya mtaala imesasishwa kujumuisha Kazi na Maelezo ya Zana katika Sehemu ya Dhana za Msingi; tarehe ya nyaraka imesasishwa

#### Uhakiki wa Uzingatiaji wa Kipimo
- **Toleo la Itifaki**: Imethibitisha kuwa nyaraka zote zinarejelea MCP Specification 2025-11-25
- **Ulinganifu wa Usanifu**: Imethibitisha usahihi wa nyaraka wa usanifu wa safu mbili (Safu ya Data + Safu ya Usafirishaji)
- **Nyaraka za Kipengele Msingi**: Imethibitisha vipengele vya seva (Rasilimali, Maelekezo, Zana) na vipengele vya mteja (Uchimbaji, Mjadala, Kurekodi, Roots)
- **Mbinu za Usafirishaji**: Imethibitisha usahihi wa nyaraka wa usafirishaji wa STDIO na HTTP inayoweza kuchezwa kwa mtiririko
- **Miongozo ya Usalama**: Imethibitisha ulinganifu na miongozo ya hivi sasa ya Mazoezi Bora ya Usalama ya MCP

#### Sifa Muhimu za MCP 2025-11-25 Zimeandikwa
- **Ugunduzi wa OpenID Connect**: Ugunduzi wa seva ya uthibitishaji kupitia OIDC
- **Nyaraka za Metadata za Kitambulisho cha Mteja wa OAuth**: Inapendekeza mfumo wa usajili wa mteja
- **Msingi wa JSON 2020-12**: Lahaja ya chaguo-msingi kwa ufafanuzi wa schema za MCP
- **Mfumo wa Daraja la SDK**: Imethibitisha mahitaji rasmi ya usaidizi na matengenezo ya vipengele vya SDK
- **Muundo wa Utawala**: Vikundi vya Kazi na Vikundi vya Maslahi vimeformalishwa katika utawala wa MCP

### Sasisho Kuu la Nyaraka za Usalama (02-Security/)

#### Uunganisho wa Warsha ya Mkutano wa Usalama wa MCP (Sherpa)
- **Rasilimali Mpya ya Mafunzo Prakti**: Uunganisho kamili umeongezwa na [Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/) katika nyaraka zote za usalama
- **Mafunzo ya Njia ya Safari**: Imedocumenta mafanikio kamili ya safari kutoka Kambi ya Msingi hadi Mkutano Mkuu
- **Ulinganifu na OWASP**: Miongozo yote ya usalama sasa inaendana na hatari za Mwongozo wa Usalama wa MCP wa OWASP Azure

#### Uunganisho wa MCP wa Hatari 10 za Juu za OWASP
- **Sehemu Mpya**: Jedwali la Hatari 10 za Juu za Usalama za MCP za OWASP pamoja na hatua za usalama za Azure limeongezwa kwenye README kuu ya Usalama
- **Nyaraka za Hatari Za msingi**: mcp-security-controls-2025.md imesasishwa na rejea za hatari za OWASP MCP kwa kila eneo la usalama
- **Mchoro wa Marejeo**: Imeunganishwa na mchoro wa marejeo na mifano ya utekelezaji ya Mwongozo wa Usalama wa MCP wa OWASP Azure

#### Faili za Usalama Zimeboreshwa
- **README.md**: Muhtasari wa warsha ya Sherpa, jedwali la njia ya safari, muhtasari wa hatari za OWASP MCP Top 10, na sehemu ya mafunzo ya vitendo yameongezwa
- **mcp-security-controls-2025.md**: Kichwa kimesasishwa hadi Februari 2026, rejea za hatari za OWASP MCP (MCP01-MCP08) zimeongezwa, dosari ya toleo imerekebishwa
- **mcp-security-best-practices-2025.md**: Sehemu ya rasilimali ya Sherpa na OWASP imeongezwa, alama ya tarehe imesasishwa
- **mcp-best-practices.md**: Sehemu ya mafunzo ya vitendo na viungo vya Sherpa na OWASP vimeongezwa
- **azure-content-safety-implementation.md**: Rejea ya OWASP MCP06, muingiliano wa Kambi 3 ya Sherpa, na sehemu ya rasilimali za ziada vimeongezwa

#### Viungo Vipya vya Rasilimali Vimeongezwa
- [Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/)

- [MWONGOZO WA USALAMA WA OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Kurasa za mtu binafsi za hatari za OWASP MCP (MCP01-MCP10)

### Ulinganifu wa MCP wa Mtaala Kote 2025-11-25

#### Moduli 03 - Kuanzisha
- **Nyaraka za SDK**: Iliongeza Go SDK kwenye orodha rasmi ya SDK; ilisasisha marejeleo yote ya SDK kuendana na MCP Specification 2025-11-25
- **Ufafanuzi wa Usafirishaji**: Ilisasisha maelezo ya usafirishaji wa STDIO na HTTP Streaming kwa marejeleo ya wazi ya sifa

#### Moduli 04 - Utekelezaji wa Kivitendo
- **Marekebisho ya SDK**: Iliongeza Go SDK; ilisasisha orodha ya SDK na marejeleo ya toleo la sifa
- **Sifa ya Idhini**: Ilisasisha kiungo cha sifa cha Idhini ya MCP kwa toleo la sasa la 2025-11-25

#### Moduli 05 - Mada za Juu zaidi
- **Vipengele Vipya**: Iliongeza maelezo kuhusu vipengele vipya vya MCP Specification 2025-11-25 (Kazi, Maelezo ya Zana, Njia ya URL Mode Elicitation, Mizizi)
- **Rasilimali za Usalama**: Iliongeza kiungo cha OWASP MCP Top 10 na warsha ya Sherpa katika marejeleo ya ziada

#### Moduli 06 - Michango ya Jamii
- **Orodha ya SDK**: Iliongeza Swift na Rust SDKs; ilisasisha kiungo cha sifa hadi 2025-11-25
- **Marejeleo ya Sifa**: Ilisasisha kiungo cha MCP Specification kwa URL ya sifa moja kwa moja

#### Moduli 07 - Masomo kutoka kwa Utekelezaji wa Mapema
- **Marekebisho ya Rasilimali**: Iliongeza kiungo cha MCP Specification 2025-11-25 na OWASP MCP Top 10 katika rasilimali za ziada

#### Moduli 08 - Mbinu Bora
- **Toleo la Sifa**: Ilisasisha marejeleo ya MCP Specification hadi 2025-11-25
- **Rasilimali za Usalama**: Iliongeza OWASP MCP Top 10 na warsha ya Sherpa katika marejeleo ya ziada

#### Moduli 10 - Kurahisisha Mipango ya AI
- **Marekebisho ya Jabati**: Ilibadilisha jabati la toleo la MCP kutoka toleo la SDK (1.9.3) hadi toleo la sifa (2025-11-25)
- **Viungo vya Rasilimali**: Ilisasisha kiungo cha MCP Specification; iliongeza OWASP MCP Top 10

#### Moduli 11 - Mafunzo ya Mkono wa MCP Server
- **Marejeleo ya Sifa**: Ilisasisha kiungo cha MCP Specification hadi toleo la 2025-11-25
- **Rasilimali za Usalama**: Iliongeza OWASP MCP Top 10 katika rasilimali rasmi

## Desemba 18, 2025

### Sasisho la Nyaraka za Usalama - MCP Specification 2025-11-25

#### Mbinu Bora za Usalama za MCP (02-Security/mcp-best-practices.md) - Sasisho la Toelo la Sifa
- **Sasisho la Toelo la Itifaki**: Imesasisha kurejelea MCP Specification mpya ya 2025-11-25 (iliotolewa Novemba 25, 2025)
  - Imesasisha marejeleo yote ya toleo la sifa kutoka 2025-06-18 hadi 2025-11-25
  - Imesasisha marejeleo ya tarehe za hati kutoka Agosti 18, 2025 hadi Desemba 18, 2025
  - Imethibitisha kuwa URL zote za sifa zinamaanisha nyaraka za sasa
- **Uthibitishaji wa Maudhui**: Uthibitishaji wa kina wa mbinu bora za usalama dhidi ya viwango vipya
  - **Suluhisho za Usalama za Microsoft**: Imethibitisha istilahi na viungo vya sasa vya Prompt Shields (aliyepo awali kama "ugunduzi wa hatari za Jailbreak"), Azure Content Safety, Microsoft Entra ID, na Azure Key Vault
  - **Usalama wa OAuth 2.1**: Imetathmini ulinganifu na mbinu bora za usalama za OAuth za hivi karibuni
  - **Viwango vya OWASP**: Imethibitisha kuwa marejeleo ya OWASP Top 10 kwa LLMs bado ni ya sasa
  - **Huduma za Azure**: Imethibitisha viungo vyote vya nyaraka za Microsoft Azure na mbinu bora
- **Ulinganifu wa Viwango**: Viongozi wote wa viwango vya usalama waliothibitishwa kuwa wa sasa
  - Mfumo wa Usimamizi wa Hatari wa AI wa NIST
  - ISO 27001:2022
  - Mbinu Bora za Usalama za OAuth 2.1
  - Mifumo ya usalama na utekelezaji wa Azure
- **Rasilimali za Utekelezaji**: Imethibitisha viungo vyote vya miongozo ya utekelezaji na rasilimali
  - Mifumo ya uthibitishaji wa Azure API Management
  - Miongozo ya ushirikiano wa Microsoft Entra ID
  - Usimamizi wa siri za Azure Key Vault
  - Mifumo ya DevSecOps na ufumbuzi wa uangalizi

### Uhakikisho wa Ubora wa Nyaraka
- **Uzingatiaji wa Sifa**: Imethibitisha kwamba mahitaji yote muhimu ya usalama wa MCP (Lazima/Haitawezekana) yanaendana na sifa mpya
- **Uhalisia wa Rasilimali**: Imethibitisha viungo vyote vya nje kwa nyaraka za Microsoft, viwango vya usalama, na miongozo ya utekelezaji
- **Ujumuishaji wa Mbinu Bora**: Imethibitisha ufunikaji kamili wa uthibitishaji, idhini, vitisho maalum vya AI, usalama wa mnyororo wa usambazaji, na mifumo ya viwanda

## Oktoba 6, 2025

### Upanuzi wa Sehemu ya Kuanzisha – Matumizi ya Juu ya Server & Uthibitishaji Rahisi

#### Matumizi ya Juu ya Server (03-GettingStarted/10-advanced)
- **Sura Mpya Iliongezwa**: Iliwasilisha mwongozo kamili wa matumizi ya juu ya MCP server, ukijumuisha usanifu wa kawaida na wa kiwango cha chini.
  - **Server ya Kawaida dhidi ya ya Kiwango cha Chini**: Ulinganisho wa kina na mifano ya msimbo katika Python na TypeScript kwa njia zote mbili.
  - **Ubunifu wa Msimamizi**: Maelezo ya usimamizi wa zana/rasilimali/maelekezo kwa msingi wa msimamizi kwa utekelezaji wenye upanuzi na unyumbufu wa server.
  - **Mifumo ya Kivitendo**: Hali halisi ambapo aina za server za kiwango cha chini ni za manufaa kwa vipengele na usanifu wa hali ya juu.

#### Uthibitishaji Rahisi (03-GettingStarted/11-simple-auth)
- **Sura Mpya Iliongezwa**: Mwongozo wa hatua kwa hatua wa kutekeleza uthibitishaji rahisi katika server za MCP.
  - **Mafundisho ya Uthibitishaji**: Maelezo wazi ya tofauti kati ya uthibitishaji na idhini, na usimamizi wa sifa.
  - **Utekelezaji wa Msingi wa Uthibitishaji**: Aina za uthibitishaji zinazotumia middleware katika Python (Starlette) na TypeScript (Express), pamoja na mifano ya msimbo.
  - **Kuendelea kwa Usalama wa Juu**: Mwongozo wa kuanza na uthibitishaji rahisi na kuhamia OAuth 2.1 na RBAC, kwa marejeleo ya moduli za usalama wa hali ya juu.

Miongezano hii hutoa mwongozo wa vitendo, wa vitendo kwa ujenzi wa utekelezaji imara, salama, na yenye unyumbufu wa server za MCP, ikivuka dhana za msingi na mifumo ya hali ya juu ya uzalishaji.

## Septemba 29, 2025

### Mafunzo ya Mchanganyiko wa Hifadhidata ya MCP Server - Njia Kamili ya Kujifunza kwa Vitendo

#### 11-MCPServerHandsOnLabs - Mtaala Mpya wa Ushirikiano wa Hifadhidata
- **Njia Kamili ya Mafunzo ya Maabara 13**: Iliongeza mtaala kamili wa vitendo kwa ujenzi wa server za MCP zilizo tayari kwa uzalishaji zilizo na ujumuishaji wa hifadhidata ya PostgreSQL
  - **Utekelezaji wa Kivitendo**: Mfano wa uchambuzi wa Zava Retail unaonyesha mifumo ya daraja la viwanda
  - **Maendeleo ya Kujifunza Yaliyopangwa**:
    - **Maabara 00-03: Misingi** - Utangulizi, Usanifu wa Msingi, Usalama na Ukodishaji wa Wateja Wengi, Usanidi wa Mazingira
    - **Maabara 04-06: Ujenzi wa MCP Server** - Mchoro wa Hifadhidata & Schema, Utekelezaji wa MCP Server, Maendeleo ya Zana  
    - **Maabara 07-09: Vipengele vya Juu** - Ujumuishaji wa Utafutaji wa Kimiundo, Upimaji & Ukaguzi wa Makosa, Ujumuishaji wa VS Code
    - **Maabara 10-12: Uzalishaji & Mbinu Bora** - Mikakati ya Uenezaji, Uangalizi & Uwezo wa Kuona, Mbinu Bora & Uboreshaji
  - **Teknolojia za Viwanda**: Fremu ya FastMCP, PostgreSQL na pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Vipengele vya Juu**: Usalama wa Ngazi ya Safu (RLS), utafutaji wa kiuundo, upatikanaji wa data kwa wateja wengi, embeddings za vector, uangalizi wa wakati halisi

#### Upatanisho wa Istilahi - Ubadilishaji wa Moduli kuwa Maabara
- **Sasisho Kamili la Nyaraka**: Ilisasisha kwa nidaa yote mafaili ya README katika 11-MCPServerHandsOnLabs ili kutumia istilahi "Maabara" badala ya "Moduli"
  - **Vichwa vya Sehemu**: Ilisasisha "Kile Moduli Hiki Kinachojumuisha" kuwa "Kile Maabara Hii Inachojumuisha" katika maabara zote 13
  - **Maelezo ya Maudhui**: Imebadilisha "Moduli hii hutoa..." kuwa "Maabara hii hutoa..." katika nyaraka zote
  - **Malengo ya Kujifunza**: Ilisasisha "Mwisho wa moduli hii..." kuwa "Mwisho wa maabara hii..." 
  - **Viungo vya Kuongozwa**: Imebadilisha marejeleo yote ya "Moduli XX:" kuwa "Maabara XX:" katika marejeleo na urambazaji
  - **Ufuatiliaji wa Kukamilika**: Ilisasisha "Baada ya kumaliza moduli hii..." kuwa "Baada ya kumaliza maabara hii..."
  - **Marejeleo ya Kiufundi Yaliyohifadhiwa**: Imedumisha marejeleo ya moduli za Python ndani ya faili za usanidi (mfano, `"module": "mcp_server.main"`)

#### Uboreshaji wa Mwongozo wa Kujifunza (study_guide.md)
- **Ramani ya Mtaala ya Kuonekana**: Iliongeza sehemu mpya "11. Mafunzo ya Ujumuishaji wa Hifadhidata" yenye muonekano wa muundo wa maabara
- **Muundo wa Hifurushi**: Imesasisha kutoka sehemu kumi hadi kumi na moja zenye maelezo ya kina ya 11-MCPServerHandsOnLabs
- **Miongozo ya Njia ya Kujifunza**: Iliongeza maagizo ya urambazaji kuhusisha sehemu 00-11
- **Ujumuishaji wa Teknolojia**: Imeongeza maelezo ya FastMCP, PostgreSQL, na ujumuishaji wa huduma za Azure
- **Matokeo ya Kujifunza**: Imetoa msisitizo wa maendeleo ya server kwa ajili ya uzalishaji, mifumo ya ujumuishaji wa hifadhidata, na usalama wa viwanda

#### Uboreshaji wa Muundo Mkuu wa README
- **Istilahi Inayotegemea Maabara**: Imesasisha README.md kuu katika 11-MCPServerHandsOnLabs ili kutumia muundo wa "Maabara" kwa uthabiti
- **Mpangilio wa Njia ya Kujifunza**: Mchakato wazi kutoka kwa dhana za msingi hadi utekelezaji wa hali ya juu na uenezaji wa uzalishaji
- **Mwelekeo wa Kivitendo wa Dunia Halisi**: Msisitizo wa kujifunza kwa vitendo na mifumo na teknolojia za daraja la viwanda

### Maboresho ya Ubora na Ulinganisho wa Nyaraka
- **Msisitizo wa Kujifunza kwa Vitendo**: Imesisitiza njia ya vitendo inayotegemea maabara katika nyaraka zote
- **Mwelekeo wa Mifumo ya Viwanda**: Imesisitiza utekelezaji tayari wa uzalishaji na kuzingatia usalama wa viwanda
- **Ujumuishaji wa Teknolojia**: Ujumuishaji kamili wa huduma za kisasa za Azure na mifumo ya ujumuishaji wa AI
- **Maendeleo ya Njia ya Kujifunza**: Njia iliyo wazi na yenye muundo kuanzia dhana za msingi hadi uenezaji wa uzalishaji

## Septemba 26, 2025

### Uboreshaji wa Masomo - Ujumuishaji wa Usajili wa MCP wa GitHub

#### Masomo (09-CaseStudy/) - Mwelekeo wa Maendeleo ya Eko Syshemu
- **README.md**: Kupanua sana kwa somo kamili la usajili wa MCP wa GitHub
  - **Somo Kamili la Usajili wa MCP wa GitHub**: Somo jipya kamili linalochunguza uzinduzi wa Usajili wa MCP wa GitHub Septemba 2025
    - **Uchambuzi wa Tatizo**: Uchunguzi wa kina wa changamoto za kugundua na kueneza server za MCP zilizo na mgawanyiko
    - **Usanifu wa Suluhisho**: Njia ya usajili wa GitHub yenye usambazaji wa moja kwa mmoja wa usanidi wa VS Code
    - **Athari za Biashara**: Maboresho yanayopimika katika kuanzisha na ufanisi wa waendelezaji
    - **Thamani ya Kimkakati**: Msisitizo wa usambazaji wa wakala wa moduli na mwingiliano wa zana tofauti
    - **Maendeleo ya Eko Syshemu**: Kuweka kama jukwaa la msingi kwa ujumuishaji wa wakala
  - **Muundo wa Somo Lililosasishwa**: Imesasisha masomo saba yote na muundo thabiti na maelezo ya kina
    - Wakala wa Usafiri wa AI wa Azure: Msisitizo wa usimamizi wa wakala wengi
    - Ujumuishaji wa Azure DevOps: Msisitizo wa otomatiki za mchakato
    - Upataji wa Nyaraka kwa Muda Halisi: Utekelezaji wa mteja wa consola wa Python
    - Kizalishaji cha Mpango wa Kujifunza Anayotumia Mazungumzo: Programu ya wavuti ya Chainlit
    - Nyaraka Ndani ya Mhariri: Ujumuishaji wa VS Code na GitHub Copilot
    - Usimamizi wa API wa Azure: Mifano ya ujumuishaji wa API wa viwanda
    - Usajili wa MCP wa GitHub: Maendeleo ya jukwaa la eko syshemu na jamii
  - **Hitimisho Kamili**: Sehemu ya hitimisho imeandikwa upya ikielezea masomo saba yanayogusa vipengele vingi vya utekelezaji wa MCP
    - Ujumuishaji wa Viwanda, Usimamizi wa Wakala Wengi, Ufanisi wa Waendelezaji
    - Maendeleo ya Eko Syshemu, Kategorizing Matumizi ya Elimu
    - Uelewa wa kina wa mifano ya usanifu, mikakati ya utekelezaji, na mbinu bora
    - Msisitizo wa MCP kama itifaki imara, tayari kwa uzalishaji

#### Sasisho la Mwongozo wa Kujifunza (study_guide.md)
- **Ramani ya Mtaala ya Kuonekana**: Imesasisha ramani ya mawazo kujumuisha Usajili wa MCP wa GitHub katika sehemu ya Masomo
- **Maelezo ya Masomo**: Imboreshwa kutoka maelezo ya jumla hadi mgawanyo wa kina wa masomo saba kamili
- **Muundo wa Hifurushi**: Imesasisha sehemu ya 10 kuonyesha maelezo kamili ya masomo na maelezo ya utekelezaji maalum
- **Ujumuishaji wa Mabadiliko**: Iliongeza rekodi ya Septemba 26, 2025 inayoonyesha kuongeza Usajili wa MCP wa GitHub na maboresho ya masomo
- **Sasisho la Tarehe**: Imesasisha alama ya wakati ya mguu wa chini kuonyesha mapitio ya hivi karibuni (Septemba 26, 2025)

### Maboresho ya Ubora wa Nyaraka
- **Uboreshaji wa Ulinganisho**: Umekwisha weka kiwango cha muundo wa somo la kesi katika mifano saba yote
- **Ujumuishaji Kamili**: Masomo sasa yanahusu viwanda, ufanisi wa waendelezaji, na maendeleo ya eko syshemu
- **Mwelekeo wa Kimkakati**: Imesisitiza MCP kama msingi wa kusambaza mifumo ya wakala
- **Ujumuishaji wa Rasilimali**: Imesasisha rasilimali za ziada kuhusisha kiungo cha Usajili wa MCP wa GitHub

## Septemba 15, 2025

### Upanuzi wa Mada za Juu - Usafirishaji Maalum & Uhandisi wa Muktadha

#### Usafirishaji Maalum wa MCP (05-AdvancedTopics/mcp-transport/) - Mwongozo Mpya wa Utekelezaji wa Juu
- **README.md**: Mwongozo kamili wa utekelezaji wa njia maalum za usafirishaji wa MCP
  - **Usafirishaji wa Azure Event Grid**: Utekelezaji kamili wa usafirishaji usio na server ulioendeshwa kwa matukio
    - Mifano ya C#, TypeScript, na Python yenye ujumuishaji wa Azure Functions
    - Mifumo ya usanifu unaozingatia matukio kwa suluhisho za MCP zenye upanuzi
    - Kupokea webhook na usimamizi wa ujumbe unaotumwa
  - **Usafirishaji wa Azure Event Hubs**: Utekelezaji wa usafirishaji wa mtiririko wa kasi
    - Uwezo wa mtiririko wa wakati halisi kwa hali za ucheleweshaji mdogo
    - Mikakati ya kugawanya na usimamizi wa nukta za kuangalia
    - Kusanya ujumbe na uboreshaji wa utendaji
  - **Mifano ya Ujumuishaji wa Viwanda**: Mifano ya usanifu tayari kwa uzalishaji
    - Uendeshaji wake MCP unaogawanyika kati ya Azure Functions nyingi
    - Mifumo mchanganyiko ya usafirishaji inayochanganya aina mbalimbali za usafirishaji
    - Uendelevu wa ujumbe, uaminifu, na mikakati ya usimamizi wa makosa
  - **Usalama & Uangalizi**: Ujumuishaji wa Azure Key Vault na mifumo ya kuona
    - Uthibitishaji wa utambulisho uliodhibitiwa na upatikanaji wa idhini ya chini kabisa
    - Telemetri ya Application Insights na uangalizi wa utendaji
    - Vizuizi vya mzunguko na mifumo ya uvumilivu wa hitilafu
  - **Mifumo ya Upimaji**: Mikakati kamili ya upimaji kwa usafirishaji maalum
    - Upimaji wa vitengo kwa kutumia mawakala wa upimaji na mifumo ya kubuni upuuzi
    - Upimaji wa ujumuishaji na Azure Test Containers
    - Mambo ya kuzingatia kwa upimaji wa utendaji na mzigo

#### Uhandisi wa Muktadha (05-AdvancedTopics/mcp-contextengineering/) - Fani Inayoibukia ya AI
- **README.md**: Utafiti wa kina wa uhandisi wa muktadha kama fani inayokua
  - **Kanuni za Msingi**: Ushirikiano kamili wa muktadha, ufahamu wa maamuzi ya vitendo, na usimamizi wa dirisha la muktadha

  - **MCP Protocol Alignment**: Jinsi muundo wa MCP unavyoshughulikia changamoto za uhandisi wa muktadha
    - Vikwazo vya dirisha la muktadha na mikakati ya upakiaji wa hatua kwa hatua
    - Uamuzi wa umuhimu na upokeaji wa muktadha wa mienendo
    - Usimamizi wa muktadha wa modal nyingi na masuala ya usalama
  - **Mbinu za Utekelezaji**: Miundo ya mfululizo mmoja dhidi ya wa wakala wengi
    - Mbinu za kugawanya na kipaumbele cha sehemu za muktadha
    - Mikakati ya upakiaji wa hatua kwa hatua na usindishaji wa muktadha
    - Mbinu za tabaka za muktadha na uboreshaji wa upokeaji
  - **Mfumo wa Upimaji**: Vigezo vinavyojitokeza kwa tathmini ya ufanisi wa muktadha
    - Ufanisi wa pembejeo, utendaji, ubora, na masuala ya uzoefu wa mtumiaji
    - Mbinu za majaribio za uboreshaji wa muktadha
    - Uchambuzi wa kushindwa na mbinu za kuboresha

#### Sasisho za Mwelekeo wa Mtaala (README.md)
- **Muundo Uboreshwa wa Moduli**: Jedwali la mtaala lililosasishwa kuingiza mada mpya za juu
  - Iliongezwa Ingizo la Uhandisi wa Muktadha (5.14) na Usafirishaji Maalum (5.15)
  - Muundo thabiti na viungo vya urambazaji katika moduli zote
  - Maelezo yaliyosasishwa kuonyesha wigo wa sasa wa maudhui

### Maboresho ya Muundo wa Saraka
- **Kuweka Viwango vya Majina**: Kubadilisha jina la "mcp transport" kuwa "mcp-transport" ili ulingane na folda nyingine za mada za juu
- **Utaratibu wa Maudhui**: Folda zote 05-AdvancedTopics sasa zinaendana kwa mtindo wa majina (mcp-[mada])

### Maboresho ya Ubora wa Nyaraka
- **Ulinganifu wa Maelezo ya MCP**: Marejeo yote mapya yanarejelea Maelezo ya MCP ya sasa 2025-06-18
- **Mifano ya Lugha Nyingi**: Mifano kamili ya msimbo katika C#, TypeScript, na Python
- **Lengo la Biashara**: Mifumo tayari kwa uzalishaji na ushirikiano wa wingu la Azure kote
- **Nyaraka za Kivizualu**: Michoro ya Mermaid kwa usanifu na uonyesho wa mtiririko

## Agosti 18, 2025

### Sasisho Kamili la Nyaraka - Viwango vya MCP 2025-06-18

#### Mbinu Bora za Usalama wa MCP (02-Security/) - Uboreshaji Kamili
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Uandishi upya kamili uliolingana na Maelezo ya MCP 2025-06-18
  - **Mahitaji Lazima**: Iliongezwa mahitaji ya KUFANYA/HURU kando na viashiria vinavyoonekana wazi
  - **Mbinu 12 za Msingi za Usalama**: Ilipangwa upya kutoka orodha ya vitu 15 hadi nyanja kamili za usalama
    - Usalama wa Tokeni & Uthibitisho kwa ushirikiano wa mtoa utambulisho wa nje
    - Usimamizi wa Kikao & Usalama wa Usafirishaji na mahitaji ya usimbuaji
    - Ulinzi wa Vitisho Maalum kwa AI na ushirikiano wa Microsoft Prompt Shields
    - Udhibiti wa Upatikanaji & Ruhusa kwa kanuni ya ruhusa ya chini kabisa
    - Usalama wa Maudhui & Ufuatiliaji kwa ushirikiano wa Azure Content Safety
    - Usalama wa Mnyororo wa Ugavi kwa uhakikisho kamili wa vipengele
    - Usalama wa OAuth & Kuzuia Kutumika Vibaya kwa utekelezaji wa PKCE
    - Majibu ya Tukio & Urejeshwaji kwa uwezo wa kiotomatiki
    - Uzingatiaji & Usimamizi kwa ulinganifu wa kanuni
    - Udhibiti wa Usalama wa Juu na usanifu wa imani sifuri
    - Ushirikiano wa Mfumo wa Usalama wa Microsoft na suluhisho kamili
    - Mageuzi Endelevu ya Usalama kwa mbinu zinazobadilika
  - **Suluhisho za Usalama za Microsoft**: Mwongozo ulioboreshwa wa ushirikiano kwa Prompt Shields, Azure Content Safety, Entra ID, na GitHub Advanced Security
  - **Rasilimali za Utekelezaji**: Viungo vya rasilimali vya kina vilivyogawanywa kwa Nyaraka Rasmi za MCP, Suluhisho za Usalama za Microsoft, Viwango vya Usalama, na Mwongozo wa Utekelezaji

#### Udhibiti wa Usalama wa Juu (02-Security/) - Utekelezaji wa Biashara
- **MCP-SECURITY-CONTROLS-2025.md**: Marekebisho kamili na mfumo wa usalama wa ngazi ya biashara
  - **Nyanja 9 Kamili za Usalama**: Kupanuliwa kutoka kudhibiti rahisi hadi mfumo wa kina wa biashara
    - Uthibitishaji wa Juu & Ruhusa kwa ushirikiano wa Microsoft Entra ID
    - Usalama wa Tokeni & Udhibiti wa Kuingilia Usiojaliwa na uthibitishaji kamili
    - Udhibiti wa Usalama wa Vikao na kuzuia ndoa
    - Udhibiti wa Usalama wa AI Maalum kwa kuingiza maelekezo na kuzuia sumu ya zana
    - Kuzuia Shambulio la Msaidizi Aliyepoteza Hali kwa usalama wa wakala wa OAuth
    - Usalama wa Utekelezaji wa Zana kwa kujifunga na kutenganisha
    - Udhibiti wa Usalama wa Mnyororo wa Ugavi kwa uthibitisho wa utegemezi
    - Udhibiti wa Ufuatiliaji & Ugunduzi kwa ushirikiano wa SIEM
    - Majibu ya Tukio & Urejeshwaji kwa uwezo wa kiotomatiki
  - **Mifano ya Utekelezaji**: Iliongezwa sehemu za usanidi wa YAML kwa kina na mifano ya msimbo
  - **Ushirikiano wa Suluhisho za Microsoft**: Ufunuo kamili wa huduma za usalama za Azure, GitHub Advanced Security, na usimamizi wa utambulisho wa biashara

#### Usalama wa Mada za Juu (05-AdvancedTopics/mcp-security/) - Utekelezaji Tayari kwa Uzalishaji
- **README.md**: Uandishi upya kamili wa utekelezaji wa usalama wa biashara
  - **Ulinganifu wa Maelezo ya Sasa**: Imesasishwa na Maelezo ya MCP 2025-06-18 na mahitaji ya usalama ya lazima
  - **Uthibitishaji Uboreshwa**: Ushirikiano wa Microsoft Entra ID na mifano kamili ya .NET na Java Spring Security
  - **Ushirikiano wa Usalama wa AI**: Utekelezaji wa Microsoft Prompt Shields na Azure Content Safety na mifano ya kina ya Python
  - **Upunguzaji wa Vitisho vya Juu**: Mifano kamili ya utekelezaji wa
    - Kuzuia Shambulio la Msaidizi Aliyepoteza Hali kwa PKCE na uthibitishaji wa ridhaa ya mtumiaji
    - Kuzuia Kupitia Tokeni kwa uthibitishaji wa hadhira na usimamizi salama wa tokeni
    - Kuzuia Kukamatwa kwa Kikao kwa kushikamana kwa usimbaji na uchambuzi wa tabia
  - **Ushirikiano wa Usalama wa Biashara**: Ufuatiliaji wa Azure Application Insights, mistari ya kugundua vitisho, na usalama wa mnyororo wa ugavi
  - **Orodha ya Ukaguzi wa Utekelezaji**: Udhibiti wa usalama wa lazima dhidi ya uliopendekezwa na faida za mfumo wa usalama wa Microsoft

### Ubora wa Nyaraka & Ulinganifu wa Viwango
- **Marejeo ya Maelezo**: Yaliyosasishwa marejeo yote kwa Maelezo ya MCP 2025-06-18
- **Mfumo wa Usalama wa Microsoft**: Mwongozo wa ushirikiano ulioboreshwa katika nyaraka zote za usalama
- **Utekelezaji wa Kivitendo**: Iliongezwa mifano ya msimbo wa kina katika .NET, Java, na Python na mifumo ya biashara
- **Utaratibu wa Rasilimali**: Kategoriza kamili ya nyaraka rasmi, viwango vya usalama, na mwongozo wa utekelezaji
- **Viashiria vya Kivizualu**: Kuweka alama wazi za mahitaji ya lazima dhidi ya mbinu zinazopendekezwa


#### Misingi ya Msingi (01-CoreConcepts/) - Uboreshaji Kamili
- **Sasisho la Toleo la Itifaki**: Imesasishwa kurejelea Maelezo ya MCP ya sasa 2025-06-18 na utoleo wa tarehe (muundo wa YYYY-MM-DD)
- **Uboreshaji wa Usanifu**: Maelezo yaliyoimarishwa ya Wageni, Wateja, na Server ili kuonyesha mifumo ya sasa ya MCP
  - Wageni sasa wamefafanuliwa wazi kama programu za AI zinazoendeshana muunganisho wa wateja wengi wa MCP
  - Wateja wameelezewa kama waunganishaji wa itifaki wanaoshikilia uhusiano wa mmoja kwa mmoja na server
  - Server zimeboreshwa na matukio ya uanzishaji wa ndani vs. mbali
- **Urekebishaji wa Kimsingi**: Marekebisho kamili ya primitivi za server na wateja
  - Primitivi za Server: Rasilimali (vyanzo vya data), Maelekezo (templates), Zana (mifumo inayotekelezwa) na maelezo na mifano ya kina
  - Primitivi za Mteja: Sampuli (ukamilishaji wa LLM), Kuuliza (pembejeo za mtumiaji), Kuingiza rekodi (kufuatilia/kukagua)
  - Imesasishwa na mifano ya sasa ya kugundua (`*/list`), upokeaji (`*/get`), na utekelezaji (`*/call`)
- **Usanifu wa Itifaki**: Iliyotambulishwa mfano wa sani ya tabaka mbili
  - Tabaka la Data: Msingi wa JSON-RPC 2.0 na usimamizi wa mzunguko wa maisha na primitivi
  - Tabaka la Usafirishaji: STDIO (ndani) na HTTP ya Mtiririko na SSE (mbali) kama mbinu za usafirishaji
- **Mfumo wa Usalama**: Kanuni kamili za usalama zikiwemo ridhaa wazi ya mtumiaji, ulinzi wa faragha, usalama wa utekelezaji wa zana, na usalama wa tabaka la usafirishaji
- **Mifumo ya Mawasiliano**: Imesasisha ujumbe wa itifaki kuonyesha anza, ugunduzi, utekelezaji, na mtiririko wa taarifa
- **Mifano ya Msimbo**: Mifano ya lugha nyingi (.NET, Java, Python, JavaScript) imesafishwa kuonyesha mifumo ya sasa ya MCP SDK

#### Usalama (02-Security/) - Marekebisho Kamili ya Usalama  
- **Ulinganifu wa Viwango**: Ulinganifu kamili na mahitaji ya usalama ya Maelezo ya MCP 2025-06-18
- **Mageuzi ya Uthibitishaji**: Imethibitishwa mageuzi kutoka seva customize OAuth hadi usimamizi wa wakala mtoa utambulisho wa nje (Microsoft Entra ID)
- **Uchambuzi wa Vitisho Maalum kwa AI**: Ufunuo ulioboreshwa wa njia za kisasa za shambulio za AI
  - Matukio ya kina ya shambulio la kuingiza maelekezo na mifano halisi
  - Mbinu za sumu ya zana na mifano ya shambulio aina "rug pull"
  - Uchafuzi wa dirisha la muktadha na mashambulio ya mchanganyiko wa modeli
- **Suluhisho za Usalama za Microsoft AI**: Ufunika kamili wa mfumo wa usalama wa Microsoft
  - AI Prompt Shields zenye ujuzi wa ugunduzi wa hali ya juu, mwangaza, na mbinu za alama
  - Mifano ya ushirikiano wa Azure Content Safety
  - GitHub Advanced Security kwa ulinzi wa mnyororo wa ugavi
- **Upunguzaji wa Vitisho vya Juu**: Udhibiti wa usalama wa kina kwa
  - Kukamatwa kwa kikao kwa matukio ya shambulio maalum ya MCP na mahitaji ya kitambulisho cha kikao cha usimbuaji
  - Matatizo ya msaidizi aliyepoteza hali katika matukio ya wakala MCP na mahitaji ya ridhaa wazi
  - Uraibu wa kupitisha tokeni na udhibiti wa lazima wa uthibitisho
- **Usalama wa Mnyororo wa Ugavi**: Ufunuo wa kina wa mnyororo wa ugavi wa AI ikiwa ni pamoja na modeli za msingi, huduma za embeddings, watoa muktadha, na API za wahusika wengine
- **Usalama wa Msingi**: Ushirikiano ulioboreshwa na mifumo ya usalama ya biashara ikiwa ni pamoja na usanifu wa imani sifuri na mfumo wa usalama wa Microsoft
- **Utaratibu wa Rasilimali**: Viungo vya rasilimali vya kina vilivikogawanywa kwa aina (Nyaraka Rasmi, Viwango, Utafiti, Suluhisho za Microsoft, Mwongozo wa Utekelezaji)

### Maboresho ya Ubora wa Nyaraka
- **Malengo ya Kujifunza Yaliyopangwa**: Malengo ya kujifunza yaliyoimarishwa yenye matokeo mahususi na yanayotekelezeka
- **Marejeo ya Msalaba**: Viungo viliongezwa kati ya mada zinazohusiana za usalama na misingi ya msingi
- **Taarifa za Sasa**: Marejeo yote ya tarehe na viungo vya maelezo yalisasishwa kwa viwango vya sasa
- **Mwongozo wa Utekelezaji**: Mwongozo maalum na wa utekelezaji uliongezwa kote kwenye sehemu zote mbili

## Julai 16, 2025

### README na Maboresho ya Urambazaji
- Mwelekeo wa mtaala ulitengenezwa upya kabisa katika README.md
- Ilibadilishwa lebo za `<details>` na muundo unaotegemea jedwali rahisi kutumia
- Chaguzi mbadala za muundo ziliundwa katika folda mpya "alternative_layouts"
- Mifano ya urambazaji ya kadi, chaguzi za tabo, na mtindo wa accordion iliongezwa
- Sehemu ya muundo wa hifadhi imesasishwa kuingiza faili zote za hivi karibuni
- Sehemu ya "Jinsi ya Kutumia Mtaala Huu" iliboreshwa na mapendekezo wazi
- Viungo vya maelezo ya MCP vilisasishwa kwa kuonyesha URL sahihi
- Sehemu ya Uhandisi wa Muktadha (5.14) iliongezwa kwenye muundo wa mtaala

### Sasisho za Mwongozo wa Masomo
- Mwongozo wa masomo ulirekebishwa kabisa kulingana na muundo wa sasa wa hifadhi
- Sehemu mpya za Wateja wa MCP na Zana, na Server maarufu wa MCP ziliongezwa
- Ramani ya Mtaala wa Kivizualu ilisafishwa kuonyesha mada zote kwa usahihi
- Maelezo ya Mada za Juu yaliyoimarishwa kufunika maeneo yote maalum
- Sehemu ya Masomo ya Kesi ilisasaishwa kuonyesha mifano halisi
- Rekodi hii kamili ya mabadiliko iliongezwa

### Michango ya Jamii (06-CommunityContributions/)
- Maelezo ya kina kuhusu server za MCP za kizazi cha picha yaliyoongezwa
- Sehemu kamili juu ya matumizi ya Claude katika VSCode iliongezwa
- Maelekezo ya usanidi na matumizi ya mteja wa terminal wa Cline yaliyoongezwa
- Sehemu ya mteja wa MCP ilisasishwa kuwashirikisha chaguzi zote maarufu za mteja
- Mifano ya michango iliimarishwa kwa mifano sahihi ya msimbo

### Mada za Juu (05-AdvancedTopics/)
- Folda zote za mada maalum ziliandaliwa kwa majina thabiti
- Vifaa na mifano ya uhandisi wa muktadha viliongezwa
- Nyaraka za ushirikiano wa wakala wa Foundry ziliongezwa
- Maelezo ya ushirikiano wa usalama wa Entra ID yaliimarishwa

## Juni 11, 2025

### Uundaji wa Awali
- Toleo la kwanza la mtaala wa MCP kwa Waanzilishi lilitolewa
- Muundo wa msingi wa sehemu zote 10 kuu uliundwa
- Ramani ya Mtaala ya Kivizualu ilitekelezwa kwa urambazaji
- Miradi ya majaribio ya awali katika lugha mbalimbali za programu iliongezwa

### Kuanza (03-GettingStarted/)
- Mifano ya utekelezaji wa server wa kwanza ilitengenezwa
- Mwongozo wa maendeleo ya mteja uliongezwa
- Maelekezo ya ushirikiano wa mteja LLM yaliyojumuishwa
- Nyaraka za ushirikiano wa VS Code ziliongezwa
- Mifano ya Server-Sent Events (SSE) ilitekelezwa

### Misingi ya Msingi (01-CoreConcepts/)
- Maelezo ya kina ya usanifu wa mteja-server yaliyoongezwa
- Nyaraka kuhusu vipengele muhimu vya itifaki zilitengenezwa
- Mbinu za ujumbe katika MCP zilitangazwa

## Mei 23, 2025

### Muundo wa Hifadhi
- Hifadhi ilianzishwa na muundo wa kiufundi wa msingi
- Faili za README kwa kila sehemu kuu zilitengenezwa
- Miundombinu ya tafsiri ilianzishwa
- Vifaa vya picha na michoro viliongezwa

### Nyaraka
- README.md ya mwanzo na muhtasari wa mtaala ulitengenezwa
- CODE_OF_CONDUCT.md na SECURITY.md viliongezwa
- SUPPORT.md ilianzishwa kwa mwongozo wa kupata msaada
- Muundo wa mwongozo wa kwanza wa masomo ulitengenezwa

## Aprili 15, 2025

### Mipango na Mfumo
- Mipango ya awali ya mtaala wa MCP kwa Waanzilishi
- Malengo ya kujifunza na hadhira lengwa yaliwekwa wazi
- Muundo wa sehemu 10 wa mtaala ulielezewa
- Mfumo wa dhana kwa mifano na masomo ya kesi ulitengenezwa
- Mifano ya awali ya majaribio ya vipengele muhimu ilitengenezwa

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
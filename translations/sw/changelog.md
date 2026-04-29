# Mabadiliko: MCP kwa Mtaala wa Waanzilishi

Hati hii hutoa kumbukumbu ya mabadiliko yote muhimu yaliyofanywa kwenye mtaala wa Model Context Protocol (MCP) kwa Waanzilishi. Mabadiliko yameandikwa kwa mpangilio wa mfululizo wa kinyume wa wakati (mabadiliko mapya kwanza).

## Aprili 11, 2026

### Somo Jipya, Marekebisho ya Nyaraka, na Sasisho za Kutegemea

#### Yaliyoongezwa Maudhui ya Mtaala Mpya

**Moduli 05 - Mada za Juu**
- **Somo 5.17: Ufafanuzi wa Mawazo ya Wakala Wengi katika Ushindani na MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Mwongozo mpana mpya unaofunika mfano wa mijadala ya ushindani kwa mifumo ya wawakala wengi
  - Mchoro wa usanifu wa Mermaid: mawakala wawili → seva ya MCP iliyoshirikiwa → maandishi ya mjadala → hakimu → hukumu
  - Seva ya zana ya MCP iliyoshirikiwa (`web_search` + `run_python`) iliyoandikwa kwa Python na TypeScript
  - Maelekezo ya mfumo yanayopingana (KWA / DHIDI YA / Hakimu) na mahitaji ya wazi ya matumizi ya zana
  - Mkurugenzi wa mjadala katika Python, TypeScript, na C# akisimamia raundi na kupangilia hoja
  - Uunganishaji wa MCP `ClientSession` kwa mkurugenzi kwa miito halisi ya zana
  - Jedwali la matumizi (ugundaji wa hali ya kuota akilini, muundo wa tishio, ukaguzi wa muundo wa API, uhakiki wa ukweli, uteuzi wa teknolojia)
  - Mambo ya usalama: utekelezaji katika eneo la kujaribu, uthibitishaji wa miito ya zana, kupunguzwa kwa kasi, kumbukumbu za ukaguzi
  - Mazoezi yaliyojumuishwa yenye matukio matatu ya vitendo (uhakiki wa msimbo, uamuzi wa usanifu, udhibiti wa maudhui)

#### Marekebisho ya Nyaraka

**Moduli 03 - Anza Kutumia**
- **05-stdio-server/README.md**: Imerekebisha mfano usio kamili wa seva ya stdio ya TypeScript — iliongeza uanzishaji wa usafirishaji ulio fehlika (`new StdioServerTransport()`) na wito `server.connect(transport)` ili ulingane na mifano ya Python na .NET katika sehemu hiyo
- **14-sampling/README.md**: Imerekebisha makosa ya tahajia — imebadilisha `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Sasisho za Mtaala

**README.md Kuu**
- Imeongeza kipengele 5.17 (Ufafanuzi wa Mawazo ya Wakala Wengi katika Ushindani na MCP) kwenye jedwali la mtaala na kiungo cha moja kwa moja kwa somo jipya

**05-AdvancedTopics/README.md**
- Imeongeza safu ya Somo 5.17 kwenye jedwali la masomo

**study_guide.md**
- Imeongeza mada ya Ufafanuzi wa Mawazo ya Wakala Wengi katika Ushindani kwenye ramani ya mawazo na maelezo ya maandishi ya Mada za Juu

#### Marekebisho ya Msimbo na Usalama

**Moduli 05 - Wawakala Wanaopingana (`mcp-adversarial-agents`)**
- **Marekebisho ya Usalama — sindano ya amri**: Imebadilisha mchanganyiko wa `execSync` wa amri ya shell na `execFile` + `promisify` katika zana ya `run_python` ya TypeScript, kuondoa hatari ya sindano ya amri (msimbo unaodhibitiwa na LLM sasa hupitishwa kama kipengele halisi cha argv bila kushirikiana na shell)
- **Uunganishaji wa mzunguko wa zana ya MCP**: Imeboresha mkurugenzi wa mjadala wa Python kutumia mteja wa `AsyncAnthropic` (kubadilisha `Anthropic` ya kufunga), kupitisha `ClientSession` ya moja kwa moja kwa kila zamu ya wakala, kupata maelezo ya zana kupitia `session.list_tools()` kila zamu, na kusambaza vipengele vya `tool_use` kupitia `session.call_tool()` kwa mzunguko hadi mfano utoe jibu la mwisho la maandishi

#### Sasisho za Kutegemea

- Imeongeza toleo la `hono` hadi 4.12.12 katika vifurushi vingi (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Imeongeza `@hono/node-server` kutoka 1.19.11 hadi 1.19.13 katika vifurushi vya TypeScript
- Imeongeza `cryptography` kutoka 46.0.5 hadi 46.0.7 katika vifurushi vya Python (maabara ya 10-StreamliningAIWorkflows 3 na 4)
- Imeongeza `lodash` kutoka 4.17.23 hadi 4.18.1 katika msimamizi wa 10-StreamliningAIWorkflows

#### Tafsiri

- Imefanikiwa kusasisha tafsiri kwa lugha zaidi ya 48 kulingana na mabadiliko ya chanzo mapya (sasisho la i18n)

---

## Februari 5, 2026

### Uhakiki na Maboresho ya Uelekezaji Katika Ghavamano Yote la Hifadhi ya Maktaba

#### Yaliyoongezwa Maudhui ya Mtaala Mpya

**Moduli 03 - Anza Kutumia**
- **12-mcp-hosts/README.md**: Mwongozo mpya wa kina wa kuanzisha wamiliki wa MCP
  - Mifano ya usanidi wa Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Violezo vya usanidi vya JSON kwa wamiliki wote wakuu
  - Jedwali la kulinganisha aina za usafirishaji (stdio, SSE/HTTP, WebSocket)
  - Upangaji wa matatizo kwa hitilafu za kawaida za muunganisho
  - Mbinu bora za usalama kwa usanidi wa mwenyeji

- **13-mcp-inspector/README.md**: Mwongozo mpya wa utambuzi wa makosa kwa MCP Inspector
  - Njia za usakinishaji (npx, npm global, kutoka chanzo)
  - Kuunganisha kwa seva kupitia stdio na HTTP/SSE
  - Majaribio ya zana, rasilimali, na mitiririko ya maelekezo
  - Uunganisho wa VS Code na MCP Inspector
  - Matukio ya kawaida ya utambuzi wa makosa na suluhisho

**Moduli 04 - Utekelezaji wa Kivitendo**
- **pagination/README.md**: Mwongozo mpya wa utekelezaji wa ugawaji ukurasa
  - Mifumo ya ugawaji ukurasa inayotumia cursor katika Python, TypeScript, Java
  - Usimamizi wa ugawaji ukurasa upande wa mteja
  - Mikakati ya usanifu wa cursor (isiyo na mwangaza dhidi ya iliyo na muundo)
  - Mapendekezo ya kuboresha utendaji

**Moduli 05 - Mada za Juu**
- **mcp-protocol-features/README.md**: Ufafanuzi mpya wa kina wa sifa za itifaki
  - Utekelezaji wa taarifa za maendeleo
  - Mifumo ya kughairi ombi
  - Violezo vya rasilimali na mifumo ya URI
  - Usimamizi wa mzunguko wa maisha ya seva
  - Udhibiti wa viwango vya kumbukumbu
  - Mifumo ya kushughulikia makosa kwa kutumia nambari za JSON-RPC

#### Marekebisho ya Uelekezaji (faili 24+ zimesasishwa)

**README za Moduli Kuu**
 Sasa zina viungo kwa somo la kwanza NA moduli inayofuata

**02-Faili Ndogo za Usalama**
- Hati 5 zote za ziada za usalama sasa zina sehemu ya "Nini Kifuatacho" kwa uelekezaji:

**09-Faili za Uchunguzi wa Kesi**
- Faili zote za uchunguzi wa kesi sasa zina uelekezaji wa mfuatano:

**10-Maabara ya Streamlining AI**
Iliongeza sehemu ya Nini Kifuatacho kwenye muhtasari wa Moduli 10 na Moduli 11

#### Marekebisho ya Msimbo na Maudhui

**Sasisho za SDK na Kutegemea**
Imerekebisha toleo tupu la openai kuwa `^4.95.0`
Imesasisha SDK kutoka `^1.8.0` hadi `>=1.26.0`
Imesasisha alama za toleo la MCP kuwa `>=1.26.0`

**Marekebisho ya Msimbo**
Imerekebisha mfano batili wa `gpt-4o-mini` kuwa `gpt-4.1-mini`

**Marekebisho ya Maudhui**
Imerekebisha kiungo kilichovunjika `READMEmd` → `README.md`, kurekebisha kichwa cha mtaala kutoka `Module 1-3` → `Module 0-3`, na kurekebisha njia nyeti kwa herufi
Imeondoa nakala iliyoharibika ya maudhui ya Uchunguzi wa Kesi 5

**Maboresho ya Mwongozo kwa Waanzilishi**
Imeongeza utangulizi sahihi, malengo ya kujifunza, na stahiki za awali kwa waanzilishi

#### Sasisho za Mtaala

**README.md Kuu**
- Imeongeza kipengele 3.12 (Wamiliki wa MCP), 3.13 (MCP Inspector), 4.1 (Ugawaji Ukurasa), 5.16 (Sifa za Itifaki) kwenye jedwali la mtaala

**README za Moduli**
Ilimngeza masomo 12 na 13 kwenye orodha ya masomo
Ilimngeza sehemu ya Mwongozo wa Kivitendo na kiungo cha ugawaji ukurasa
Ilimngeza masomo 5.15 (Usafirishaji wa Kipekee) na 5.16 (Sifa za Itifaki)

**study_guide.md**
- Ilisasisha ramani ya mawazo na mada mpya zote: Usanidi wa Wamiliki wa MCP, MCP Inspector, Mikakati ya Ugawaji Ukurasa, Ufafanuzi wa Sifa za Itifaki

## Januali 28, 2026

### Ukaguzi wa Uzingatiaji wa Sifa za MCP Tarehe 2025-11-25

#### Uboreshaji wa Dhana za Msingi (01-CoreConcepts/)
- **Mteja Msingi Mpya - Mizizi**: Imeongeza nyaraka za kina kuhusu mteja msingi wa Mizizi, kuwezesha seva kuelewa mipaka ya mfumo wa faili na ruhusa za kufikia
- **Maandishi ya Zana**: Imeongeza nyaraka kuhusu maandishi ya tabia za zana (`readOnlyHint`, `destructiveHint`) kwa maamuzi bora ya utekelezaji wa zana
- **Mitoaji wa Zana katika Sampuli**: Imesasisha nyaraka za Sampuli kuwa jumuisha vigezo vya `tools` na `toolChoice` kwa miito ya zana inayoendeshwa na mfano wakati wa maombi ya sampuli
- **Uibua Hali ya URL**: Imeongeza nyaraka kuhusu uibua wa mtandao wa aina ya URL kwa mwingiliano wa wavuti unaoanzishwa na seva
- **Kazi (Jaribio)**: Imeongeza sehemu mpya inayofafanua sifa ya Kazi za majaribio kwa vifuniko vya utekelezaji endelevu na upokeaji wa matokeo yaliyochelewa
- **Msaada wa Ikoni**: Imenukuliwa kwamba zana, rasilimali, violezo vya rasilimali, na maelekezo sasa vinaweza kujumuisha ikoni kama metadata ya ziada

#### Sasisho za Nyaraka
- **README.md**: Imeongeza kumbukumbu ya toleo la MCP Specification 2025-11-25 na maelezo ya utoaji wa toleo kwa tarehe
- **study_guide.md**: Ilisasisha ramani ya mtaala kuingiza Kazi na Maandishi ya Zana katika sehemu ya Dhana za Msingi; ilisasisha alama ya tarehe ya hati

#### Uhakiki wa Uzingatiaji wa Sifa
- **Toleo la Itifaki**: Imethibitisha nyaraka zote zinarejelea MCP Specification 2025-11-25 ya sasa
- **Ulinganifu wa Usanifu**: Imethibitisha usahihi wa nyaraka wa usanifu wa tabaka mbili (Tabaka la Takwimu + Tabaka la Usafirishaji)
- **Nyaraka za Msingi**: Imethibitisha vigezo vya seva (Rasilimali, Maelekezo, Zana) na mteja (Sampuli, Uibua, Kumbukumbu, Mizizi)
- **Vifaa vya Usafirishaji**: Imethibitisha usahihi wa nyaraka za usafirishaji wa STDIO na HTTP inayoweza kuenezwa
- **Mwongozo wa Usalama**: Imethibitisha ulinganifu na nyaraka za sasa za Mazoezi Bora ya Usalama wa MCP

#### Sifa Muhimu za MCP 2025-11-25 Ziliandikwa
- **Ugunduzi wa OpenID Connect**: Ugunduzi wa seva ya uthibitishaji kupitia OIDC
- **Nyaraka za Metadata za Kitambulisho cha Mteja cha OAuth**: Mfumo uliopendekezwa wa usajili wa mteja
- **JSON Schema 2020-12**: Lahaja ya kimsingi kwa ufafanuzi wa schema za MCP
- **Mfumo wa Ngazi za SDK**: Mahitaji rasmi ya msaada na matengenezo ya sifa za SDK
- **Muundo wa Usimamizi**: Vikundi vya Kazi na Vikundi vya Maslahi vimeformalishwa katika usimamizi wa MCP

### Sasisho Kubwa la Nyaraka za Usalama (02-Security/)

#### Uunganishaji wa Warsha ya Mkutano wa Usalama wa MCP (Sherpa)
- **Rasilimali Mpya ya Mafunzo ya Vitendo**: Imeingiza kikamilifu rasilimali ya mafunzo ya vitendo ya [Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/) katika nyaraka zote za usalama
- **Mbali ya Njia ya Msafara**: Imeandikwa maendeleo kamili ya kampu kwa kampu kutoka Kampu ya Msingi hadi Kilele
- **Ulinganifu na OWASP**: Miongozo yote ya usalama sasa inalingana na hatari za Mwongozo wa Usalama wa MCP Azure wa OWASP

#### Uunganishaji wa Mwongozo wa OWASP MCP Top 10
- **Sehemu Mpya**: Imeongeza jedwali la hatari 10 za juu za usalama za OWASP MCP na mipango ya kupunguza hatari za Azure kwenye README kuu ya Usalama
- **Nyaraka Zenye Mwongozo wa Hatari**: Imeboresha mcp-security-controls-2025.md kwa marejeleo ya hatari za OWASP MCP kwa kila eneo la usalama
- **Muundo wa Marejeleo**: Imeunganishwa na usanifu wa marejeleo wa Mwongozo wa Usalama wa MCP Azure wa OWASP na mifano ya utekelezaji

#### Faili za Usalama Zilisasishwa
- **README.md**: Imeongeza muhtasari wa Warsha ya Sherpa, jedwali la njia ya msafara, muhtasari wa hatari 10 za juu za OWASP MCP, na sehemu ya mafunzo ya vitendo
- **mcp-security-controls-2025.md**: Imeboresha kichwa hadi Februari 2026, iliongeza marejeleo ya hatari za OWASP (MCP01-MCP08), ilirekebisha kutokubaliana kwa toleo la sifa
- **mcp-security-best-practices-2025.md**: Imeongeza sehemu za rasilimali za Sherpa na OWASP, ilisasisha alama ya tarehe
- **mcp-best-practices.md**: Imeongeza sehemu ya mafunzo ya vitendo na viungo vya Sherpa na OWASP
- **azure-content-safety-implementation.md**: Imeongeza marejeleo ya OWASP MCP06, ulinganifu na Kampu ya Sherpa 3, na sehemu za rasilimali za ziada

#### Viungo Vipya vya Rasilimali Vilivyoongezwa
- [Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/)
- [Mwongozo wa Usalama wa MCP Azure wa OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Kurasa za hatari binafsi za OWASP MCP (MCP01-MCP10)

### Ulinganifu wa MCP Specification 2025-11-25 katika Mtaala mzima

#### Moduli 03 - Anza Kutumia
- **Nyaraka za SDK**: Imeongeza Go SDK kwenye orodha rasmi ya SDK; ilisasisha marejeleo yote ya SDK kulingana na MCP Specification 2025-11-25
- **Kuelezea Usafirishaji**: Ilisasisha maelezo ya usafirishaji wa STDIO na HTTP Streaming pamoja na marejeleo ya wazi ya sifa

#### Moduli 04 - Utekelezaji wa Kivitendo
- **Sasisho za SDK**: Imeongeza Go SDK; ilisasisha orodha ya SDK na rejeleo la toleo la sifa
- **Sifa za Uidhinishaji**: Ilisasisha kiungo cha sifa za Uidhinishaji za MCP kwa toleo la sasa la 2025-11-25

#### Moduli 05 - Mada za Juu
- **Sifa Mpya**: Imeongeza noti kuhusu sifa mpya za MCP Specification 2025-11-25 (Kazi, Maandishi ya Zana, Uibua Hali ya URL, Mizizi)
- **Rasilimali za Usalama**: Imeongeza viungo vya OWASP MCP Top 10 na warsha ya Sherpa kama marejeleo ya ziada

#### Moduli 06 - Mchango wa Jumuiya
- **Orodha ya SDK**: Imeongeza Swift na Rust SDKs; ilisasisha kiungo cha sifa hadi 2025-11-25
- **Rejeleo la Sifa**: Ilisasisha kiungo cha MCP Specification hadi URL ya sifa ya moja kwa moja

#### Moduli 07 - Masomo kutoka kwa Utekelezaji wa Awali
- **Marekebisho ya Rasilimali**: Imeongeza kiungo cha MCP Specification 2025-11-25 na OWASP MCP Top 10 kama rasilimali za ziada

#### Moduli 08 - Mazoezi Bora
- **Toleo la Sifa**: Ilisasisha rejeleo la MCP Specification hadi 2025-11-25
- **Rasilimali za Usalama**: Imeongeza OWASP MCP Top 10 na warsha ya Sherpa kama marejeleo ya ziada

#### Moduli 10 - Kurahisisha Mtiririko wa AI
- **Sasisho la Bango**: Imebadilisha bango la toleo la MCP kutoka toleo la SDK (1.9.3) hadi toleo la sifa (2025-11-25)
- **Viungo vya Rasilimali**: Ilisasisha kiungo cha MCP Specification; iliongeza OWASP MCP Top 10

#### Moduli 11 - Maabara ya Mikono MCP Server
- **Rejeleo la Sifa**: Ilisasisha kiungo cha MCP Specification hadi toleo la 2025-11-25
- **Rasilimali za Usalama**: Imeongeza OWASP MCP Top 10 kama rasilimali rasmi

## Desemba 18, 2025
### Sasisho la Nyaraka za Usalama - Maelezo ya MCP 2025-11-25

#### Mbinu Bora za Usalama za MCP (02-Security/mcp-best-practices.md) - Sasisho la Toleo la Maelezo
- **Sasisho la Toleo la Itifaki**: Imesasishwa kurejelea Maelezo ya MCP ya mwisho 2025-11-25 (iliyotolewa Novemba 25, 2025)
  - Imesasisha marejeleo yote ya toleo la maelezo kutoka 2025-06-18 hadi 2025-11-25
  - Imesasisha tarehe za hati kutoka Agosti 18, 2025 hadi Desemba 18, 2025
  - Imethibitisha kuwa URL zote za maelezo zinaelekeza kwa nyaraka za sasa
- **Uhakiki wa Maudhui**: Uhakiki kamili wa mbinu bora za usalama dhidi ya viwango vya hivi karibuni
  - **Suluhisho za Usalama za Microsoft**: Imethibitisha istilahi za sasa na viungo kwa Prompt Shields (awali "utambuzi wa hatari ya uharibifu wa mfumo"), Azure Content Safety, Microsoft Entra ID, na Azure Key Vault
  - **Usalama wa OAuth 2.1**: Imethibitisha ulinganifu na mbinu bora za usalama za OAuth za hivi karibuni
  - **Viwango vya OWASP**: Imethibitisha viungo vya OWASP Top 10 kwa LLMs bado ni vya sasa
  - **Huduma za Azure**: Imethibitisha viungo vyote vya nyaraka za Microsoft Azure na mbinu bora
- **Ulinganifu wa Viwango**: Viwango vyote vya usalama vilivyorejelewa vimehakikiwa kuwa vya sasa
  - Mfumo wa Usimamizi wa Hatari wa NIA (NIST AI Risk Management Framework)
  - ISO 27001:2022
  - Mbinu Bora za Usalama za OAuth 2.1
  - Mifumo ya usalama na uendeshaji wa Azure
- **Rasilimali za Utekelezaji**: Imethibitisha viungo vyote vya mwongozo wa utekelezaji na rasilimali
  - Mifumo ya uthibitishaji wa Azure API Management
  - Mwongozo wa muunganisho wa Microsoft Entra ID
  - Usimamizi wa siri za Azure Key Vault
  - Mifumo ya mtiririko wa DevSecOps na suluhisho za ufuatiliaji

### Udhibitisho wa Ubora wa Nyaraka
- **Uzingatiaji wa Maelezo**: Imethibitisha mahitaji yote ya lazima ya usalama wa MCP (Lazima/Haipaswi) yanaendana na toleo la hivi karibuni
- **Sasa ya Rasilimali**: Imethibitisha viungo vyote vya nje kwa nyaraka za Microsoft, viwango vya usalama, na miongozo ya utekelezaji
- **Ujumuishaji wa Mbinu Bora**: Imethibitisha ufuniko kamili wa uthibitishaji, idhini, tishio maalum la AI, usalama wa mnyororo wa usambazaji, na mifumo ya biashara

## Oktoba 6, 2025

### Upanuzi wa Sehemu ya Kuanzia – Matumizi ya Seva ya Juu & Uthibitishaji Rahisi

#### Matumizi ya Seva ya Juu (03-GettingStarted/10-advanced)
- **Sura Mpya Imekuwa**: Imeanzisha mwongozo kamili wa matumizi ya juu ya seva ya MCP, ukijumuisha usanifu wa seva wa kawaida na wa ngazi ya chini.
  - **Seva ya Kawaida dhidi ya Ngazi ya Chini**: Ulinganisho wa kina na mifano ya msimbo katika Python na TypeScript kwa mbinu zote mbili.
  - **Ubunifu unaotegemea Mshughulikiaji**: Maelezo ya usimamizi wa zana/rasilimali/prompt unaotegemea mshughulikiaji kwa utekelezaji wa seva unaoweza kupanuka na wenye kubadilika.
  - **Mifumo ya Vitendo**: Mifano halisi ambapo mifumo ya seva ya ngazi ya chini ni ya manufaa kwa vipengele vya juu na usanifu.
  
#### Uthibitishaji Rahisi (03-GettingStarted/11-simple-auth)
- **Sura Mpya Imekuwa**: Mwongozo wa hatua kwa hatua wa kutekeleza uthibitishaji rahisi kwenye seva za MCP.
  - **Mafanikio ya Uthibitishaji**: Maelezo wazi ya uthibitishaji dhidi ya idhini, na usimamizi wa vyeti.
  - **Utekelezaji wa Auth Msingi**: Mifumo ya uthibitishaji inayotegemea middleware katika Python (Starlette) na TypeScript (Express), ikiwa na mifano ya msimbo.
  - **Maendeleo kwa Usalama wa Juu**: Mwongozo wa kuanzia na uthibitishaji rahisi na kuhamia kwa OAuth 2.1 na RBAC, pamoja na marejeleo ya moduli za usalama wa hali ya juu.

Nyongeza hizi zinatoa mwongozo wa vitendo wa kujenga utekelezaji imara zaidi, salama, na wenye kubadilika wa seva za MCP, zikivuka dhana za msingi hadi mifumo ya uzalishaji wa hali ya juu.

## Septemba 29, 2025

### Maabara za Muunganisho wa Hifadhidata za Seva ya MCP - Njia Kamili ya Kujifunza kwa Vitendo

#### 11-MCPServerHandsOnLabs - Kozi Kamili ya Muunganisho wa Hifadhidata
- **Njia Kamili ya Kujifunza Maabara 13**: Imeongezwa mtaala kamili wa maabara kwa kujenga seva za MCP tayari kwa uzalishaji zenye muunganisho wa hifadhidata ya PostgreSQL
  - **Utekelezaji wa Dunia Halisi**: Mfano wa matumizi wa Zava Retail analytics unaoonyesha mifumo ya kiwango cha biashara
  - **Muendelezo wa Kujifunza uliopangwa**:
    - **Maabara 00-03: Misingi** - Utangulizi, Usanifu wa Msingi, Usalama & Multi-Tenancy, Usaidizi wa Mazingira
    - **Maabara 04-06: Ujenzi wa Seva ya MCP** - Ubunifu wa Hifadhidata & Mchoro, Utekelezaji wa Seva ya MCP, Uendelezaji wa Zana  
    - **Maabara 07-09: Vipengele vya Juu** - Muunganisho wa Utafutaji wa Semantic, Upimaji & Ugunduzi Hitilafu, Muunganisho wa VS Code
    - **Maabara 10-12: Uzalishaji & Mbinu Bora** - Mikakati ya Ueneaji, Ufuatiliaji & Ubadili, Mbinu Bora & Uboreshaji
  - **Teknolojia za Kibiashara**: Fremu ya FastMCP, PostgreSQL na pgvector, embeddings za Azure OpenAI, Azure Container Apps, Application Insights
  - **Vipengele vya Juu**: Usalama wa Ngazi ya Safu (RLS), utafutaji wa semantic, upatikanaji wa data wa kwa pande nyingi, embeddings za vector, ufuatiliaji wa wakati halisi

#### Uboreshaji wa Istilahi - Ubadilishaji wa Moduli kuwa Maabara
- **Sasisho kamili la Nyaraka**: Imesasisha kwa mfumo wote faili za README katika 11-MCPServerHandsOnLabs kutumia istilahi "Lab" badala ya "Module"
  - **Vichwa vya Sehemu**: Imesahihisha "What This Module Covers" kuwa "What This Lab Covers" kwa maabara zote 13
  - **Maelezo ya Maudhui**: Imebadilisha "This module provides..." kuwa "This lab provides..." katika nyaraka zote
  - **Malengo ya Kujifunza**: Imesasisha "By the end of this module..." kuwa "By the end of this lab..."
  - **Viungo vya Urambazaji**: Imebadilisha marejeleo yote ya "Module XX:" kuwa "Lab XX:" katika marejeleo na urambazaji
  - **Ufuatiliaji wa Kukamilika**: Imesasisha "After completing this module..." kuwa "After completing this lab..."
  - **Marejeleo ya Kiufundi Yalihifadhiwa**: Imedumisha marejeleo ya moduli za Python katika faili za usanidi (mfano, `"module": "mcp_server.main"`)

#### Uboreshaji wa Mwongozo wa Kujifunza (study_guide.md)
- **Ramani ya Mtaala kwa Kuona**: Imeongezwa sehemu mpya "11. Database Integration Labs" yenye muhtasari wa muundo wa maabara
- **Muundo wa Hifadhi**: Imesasisha kutoka sehemu kumi hadi kumi na moja na maelezo ya kina ya 11-MCPServerHandsOnLabs
- **Mwongozo wa Njia ya Kujifunza**: Imboreshwa maagizo ya urambazaji kwa kugusa sehemu 00-11
- **Ujumuishaji wa Teknolojia**: Imeongeza maelezo ya FastMCP, PostgreSQL, na muunganisho wa huduma za Azure
- **Matokeo ya Kujifunza**: Imeangazia maendeleo ya seva tayari kwa uzalishaji, mifumo ya muunganisho wa hifadhidata, na usalama wa biashara

#### Uboreshaji wa Muundo wa README Mkuu
- **Istilahi ya Maabara**: Imesasisha README.md kuu katika 11-MCPServerHandsOnLabs kutumia muundo wa "Lab"
- **Mpangilio wa Njia ya Kujifunza**: Muendelezo wazi kutoka dhana za msingi hadi utekelezaji wa hali ya juu hadi ueneaji wa uzalishaji
- **Mkazo wa Dunia Halisi**: Uangalifu kwa kujifunza kwa vitendo na mifumo ya kiwango cha biashara na teknolojia

### Uboreshaji wa Ubora na Ulinganifu wa Nyaraka
- **Mkazo wa Kujifunza kwa Vitendo**: Imesisitiza njia ya maabara tayari kwa vitendo katika nyaraka zote
- **Mkazo wa Mifumo ya Biashara**: Imangazia utekelezaji tayari kwa uzalishaji na mkazo wa usalama wa biashara
- **Ujumuishaji wa Teknolojia**: Ufuniko kamili wa huduma za kisasa za Azure na mifumo ya muunganisho wa AI
- **Muendelezo wa Kujifunza**: Njia wazi iliyo na muundo kutoka dhana za msingi hadi ueneaji wa uzalishaji

## Septemba 26, 2025

### Uboreshaji wa Masomo ya Kesi - Muunganisho wa GitHub MCP Registry

#### Masomo ya Kesi (09-CaseStudy/) - Mkazo wa Maendeleo ya Eko-sistimu
- **README.md**: Upanuzi mkubwa na somo la kesi kamili la GitHub MCP Registry
  - **Somo la Kesi la GitHub MCP Registry**: Somo jipya la kina linalochunguza uzinduzi wa GitHub MCP Registry mwezi Septemba 2025
    - **Uchambuzi wa Tatizo**: Uchambuzi wa kina wa changamoto za kugundua na kueneza seva za MCP zilizogawanyika
    - **Usanifu wa Suluhisho**: Njia ya usajili wa GitHub yenye usambazaji wa usakinishaji wa bonyeza moja wa VS Code
    - **Athari za Kibiashara**: Maboresho yanayopimika katika kuajiri na uzalishaji wa watengenezaji programu
    - **Thamani ya Mikakati**: Mkazo juu ya usambazaji wa mawakala wa moduli na udhibiti wa zana mbalimbali
    - **Maendeleo ya Eko-sistimu**: Kushikilia kama jukwaa la msingi kwa muunganisho wa mifumo ya mawakala
  - **Muundo Ulioboreshwa wa Somo la Kesi**: Imesasisha masomo yote saba ya kesi kwa mtindo thabiti na maelezo kamili
    - Wakala wa Usafiri wa Azure AI: Mkazo wa usimamizi wa mawakala wengi
    - Muunganisho wa Azure DevOps: Mkazo wa otomatiki ya mchakato
    - Upataji wa Nyaraka kwa Wakati Halisi: Utekelezaji wa mteja wa console wa Python
    - Mtengenezaji wa Mpango wa Masomo wa Mchezo wa Mazungumzo: Web-app ya Chainlit
    - Nyaraka Katika Mhariri: Muunganisho wa VS Code na GitHub Copilot
    - Usimamizi wa Azure API: Mifumo ya muunganisho wa API za biashara
    - GitHub MCP Registry: Maendeleo ya eko-sistimu na jukwaa la jamii
  - **Hitimisho Kamili**: Sehemu ya hitimisho iliyoandikwa upya ikionyesha masomo saba ya kesi yanayochukua nyanja nyingi za utekelezaji wa MCP
    - Muunganisho wa Biashara, Usimamizi wa Mawakala Wengi, Uzalishaji wa Watengenezaji
    - Maendeleo ya Eko-sistimu, Kategorisasi ya Maombi ya Elimu
    - Maarifa yameboreshwa kuhusu mifumo ya usanifu, mikakati ya utekelezaji, na mbinu bora
    - Mkazo juu ya MCP kama itifaki imara, tayari kwa uzalishaji

#### Sasisho za Mwongozo wa Kujifunza (study_guide.md)
- **Ramani ya Mtaala kwa Kuona**: Imesasishwa ramani ya mawazo kujumuisha GitHub MCP Registry katika sehemu ya Masomo ya Kesi
- **Maelezo ya Masomo ya Kesi**: Imeboreshwa kutoka maelezo ya jumla hadi mgawanyo wa kina wa masomo saba ya kesi kamili
- **Muundo wa Hifadhi**: Imesasisha sehemu ya 10 kuonyesha ufuniko wa kina wa masomo ya kesi yenye maelezo maalum ya utekelezaji
- **Jumlisha ya Mabadiliko**: Imeongeza kipengele cha Septemba 26, 2025 kinachoelezea ongezeko la GitHub MCP Registry na maboresho ya masomo ya kesi
- **Sasisho la Tarehe**: Imesasisha alama ya muda kwenye mguu wa ukurasa kuonyesha toleo la hivi karibuni (Septemba 26, 2025)

### Uboreshaji wa Ubora wa Nyaraka
- **Ulinganifu wa Muundo**: Imesawazisha mtindo wa masomo ya kesi na muundo katika mifano yote saba
- **Ufuniko Kamili**: Masomo ya kesi sasa yanashughulikia biashara, uzalishaji wa watengenezaji, na mazingira ya maendeleo
- **Msimamo wa Mikakati**: Mkazo ulioboreshwa juu ya MCP kama jukwaa la msingi kwa usambazaji wa mifumo ya mawakala
- **Ujumuishaji wa Rasilimali**: Imesasisha rasilimali za ziada kuhusisha kiungo cha GitHub MCP Registry

## Septemba 15, 2025

### Upanuzi wa Mada za Juu - Usafirishaji Maalum & Ufundi wa Muktadha

#### Usafirishaji Maalum wa MCP (05-AdvancedTopics/mcp-transport/) - Mwongozo Mpya wa Utekelezaji wa Juu
- **README.md**: Mwongozo kamili wa utekelezaji wa mitambo ya usafirishaji maalum ya MCP
  - **Usafirishaji wa Azure Event Grid**: Utekelezaji kamili wa usafirishaji usio na seva unaotegemea matukio
    - Mifano ya C#, TypeScript, na Python na muunganisho wa Azure Functions
    - Miundo ya usanifu inayoendeshwa na tukio kwa suluhisho za MCP zinazoweza kupanuka
    - Wapokeaji wa webhook na usindikaji wa ujumbe unaotegemea msukumo
  - **Usafirishaji wa Azure Event Hubs**: Utekelezaji wa usafirishaji wa mtiririko wa kasi kubwa
    - Uwezo wa mtiririko wa wakati halisi kwa matukio ya ucheleweshaji mdogo
    - Mikakati ya kugawanya sehemu na usimamizi wa alama za ukaguzi
    - Ukusanyaji wa ujumbe na uboreshaji wa utendaji
  - **Mifumo ya Muunganisho wa Biashara**: Mifano ya usanifu tayari kwa uzalishaji
    - Usindikaji wa MCP ulioambatanishwa kwenye Azure Functions nyingi
    - Mifumo ya usafirishaji mseto inayochanganya aina mbalimbali za usafirishaji
    - Mikakati ya uimara wa ujumbe, uaminifu, na usimamizi wa makosa
  - **Usalama & Ufuatiliaji**: Muunganisho wa Azure Key Vault na mifumo ya ufuatiliaji
    - Uthibitishaji wa utambulisho uliodhibitiwa na upatikanaji wa haki duni zaidi
    - Telemetri ya Application Insights na ufuatiliaji wa utendaji
    - Mifumo ya kuzima mzunguko na uvumilivu wa hitilafu
  - **Mifumo ya Upimaji**: Mikakati kamili ya upimaji kwa usafirishaji maalum
    - Upimaji wa vipande kwa vipande na mifumo ya kuiga udanganyifu
    - Upimaji wa muunganisho na Azure Test Containers
    - Mawazo kuhusu upimaji wa utendaji na mzigo

#### Ufundi wa Muktadha (05-AdvancedTopics/mcp-contextengineering/) - Fani Inayojitokeza ya AI
- **README.md**: Uchunguzi kamili wa ufundi wa muktadha kama fani inayojitokeza
  - **Misingi Muhimu**: Kushirikiana kamili kwa muktadha, ufahamu wa maamuzi ya vitendo, na usimamizi wa dirisha la muktadha
  - **Ulinganifu na Itifaki ya MCP**: Jinsi usanifu wa MCP unavyoshughulikia changamoto za ufundi wa muktadha
    - Vizingiti vya dirisha la muktadha na mikakati ya mzigo inayoendelea
    - Ufafanuzi wa umuhimu na upataji wa muktadha unaobadilika
    - Usimamizi wa muktadha wa aina nyingi na kuzingatia usalama
  - **Mbinu za Utekelezaji**: Usanifu wa mstari mmoja dhidi ya mawakala wengi
    - Mbinu za kugawanya na kuweka kipaumbele vipande vya muktadha
    - Mikakati ya mzigo inayoendelea na usimbaji
    - Mbinu za muktadha zilizo na tabaka na uboreshaji wa upataji
  - **Mfumo wa Upimaji**: Vipimo vinavyojitokeza kwa tathmini ya ufanisi wa muktadha
    - Ufanisi wa ingizo, utendaji, ubora, na uzoefu wa mtumiaji
    - Mbinu za majaribio za uboreshaji wa muktadha
    - Uchambuzi wa kushindwa na mbinu za kuboresha

#### Sasisho za Urambazaji wa Mtaala (README.md)
- **Muundo Uboreshwa wa Moduli**: Imesasisha jedwali la mtaala kujumuisha mada mpya za juu
  - Imeongezwa Ingizo la Ufundi wa Muktadha (5.14) na Usafirishaji Maalum (5.15)
  - Muundo wa mtindo thabiti na viungo vya urambazaji kwa moduli zote
  - Maelezo yaliyosasishwa kuakisi maudhui ya sasa

### Uboreshaji wa Muundo wa Saraka
- **Ulinganifu wa Majina**: Imebadilisha jina "mcp transport" kuwa "mcp-transport" ili kulingana na folda nyingine za mada za juu
- **Mpangilio wa Maudhui**: Folda zote za 05-AdvancedTopics sasa zina mtindo thabiti wa majina (mcp-[mada])

### Uboreshaji wa Ubora wa Nyaraka
- **Ulinganifu wa Maelezo ya MCP**: Maudhui yote mapya yanarejelea MCP Specification 2025-06-18 ya sasa
- **Mifano ya Lugha Nyingi**: Mifano kamili ya msimbo katika C#, TypeScript, na Python
- **Mkazo wa Biashara**: Mifumo tayari kwa uzalishaji na ujumuishaji wa wingu la Azure kote
- **Nyaraka za Kitoo**: Michoro ya Mermaid kwa usanifu na utafutaji mtiririko

## Agosti 18, 2025

### Sasisho Kamili la Nyaraka - Viwango vya MCP 2025-06-18

#### Mbinu Bora za Usalama za MCP (02-Security/) - Uboreshaji Kamili wa Kisasa
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Uandishi upya kamili unaoendana na Maelezo ya MCP 2025-06-18  
  - **Mahitaji Yasiyoweza Kuepukika**: Iliyoongezwa mahitaji ya KUHITAJIKA/KUPELEKWA KUTO kutoka maelezo rasmi na viashirio vya wazi vya kuona  
  - **Mazingira 12 Muhimu ya Usalama**: Imeundwa upya kutoka orodha ya vitu 15 hadi maeneo kamili ya usalama  
    - Usalama wa Tokeni & Uthibitishaji na ushirikiano wa mtoaji wa utambulisho wa nje  
    - Usimamizi wa Kikao & Usalama wa Usafirishaji na mahitaji ya kriptografia  
    - Ulinzi wa Vitisho Maalum vya AI na ushirikiano wa Microsoft Prompt Shields  
    - Udhibiti wa Ufikiaji & Ruhusa kwa kanuni ya idhini ndogo kabisa  
    - Usalama wa Maudhui & Ufuatiliaji na ushirikiano wa Azure Content Safety  
    - Usalama wa Mnyororo wa Ugavi na uthibitishaji kamili wa vipengele  
    - Usalama wa OAuth & Kuzuia Msaliti Mchanganyiko na utekelezaji wa PKCE  
    - Majibu ya Tukio & Urejesho na uwezo wa kiotomatiki  
    - Uzingatiaji & Utawala unaoendana na kanuni za mamlaka  
    - Udhibiti wa Usalama wa Juu na usanifu wa kuaminiana sifuri  
    - Ushirikiano wa Mfumo wa Usalama wa Microsoft na suluhisho kamili  
    - Mabadiliko Endelevu ya Usalama na mbinu zinazobadilika  
  - **Suluhisho za Usalama za Microsoft**: Mwongozo ulioboreshwa wa ushirikiano kwa Prompt Shields, Azure Content Safety, Entra ID, na GitHub Advanced Security  
  - **Rasilimali za Utekelezaji**: Kuweka makundi ya viungo vya rasilimali kamili kwa Nyaraka Rasmi za MCP, Suluhisho za Usalama za Microsoft, Viwango vya Usalama, na Mwongozo wa Utekelezaji  

#### Udhibiti wa Usalama wa Juu (02-Security/) - Utekelezaji wa Biashara  
- **MCP-SECURITY-CONTROLS-2025.md**: Marekebisho kamili na mfumo wa usalama wa kiwango cha biashara  
  - **Maeneo 9 Kamili ya Usalama**: Kuongezwa kutoka udhibiti wa msingi hadi mfumo wa biashara uliofafanuliwa  
    - Uthibitishaji na Uidhinishaji wa Juu na ushirikiano wa Microsoft Entra ID  
    - Usalama wa Tokeni & Udhibiti wa Kuzuia Kupitisha na uthibitisho wa kina  
    - Udhibiti wa Usalama wa Kikao na kuzuia utekaji  
    - Udhibiti wa Usalama Maalum wa AI na kuzuia sindano za maelekezo na sumu ya zana  
    - Kuzuia Shambulio la Msaliti Mchanganyiko na usalama wa wakala wa OAuth  
    - Usalama wa Utekelezaji wa Zana kwa kutumia kufungiwa kwa sanduku na kutengwa  
    - Udhibiti wa Usalama wa Mnyororo wa Ugavi na uthibitishaji wa utegemezi  
    - Udhibiti wa Ufuatiliaji & Utambuzi na ushirikiano wa SIEM  
    - Majibu ya Tukio & Urejesho na uwezo wa kiotomatiki  
  - **Mifano ya Utekelezaji**: Kuongeza vitumika vya usanidi wa YAML na mifano ya msimbo  
  - **Ushirikiano wa Suluhisho za Microsoft**: Makini ya huduma za usalama za Azure, GitHub Advanced Security, na usimamizi wa utambulisho wa biashara  

#### Mada za Juu za Usalama (05-AdvancedTopics/mcp-security/) - Utekelezaji Tayari kwa Uzalishaji  
- **README.md**: Uandishi upya kamili wa utekelezaji wa usalama wa biashara  
  - **Ulinganifu wa Maelezo ya Sasa**: Imesasishwa kwa MCP Specification 2025-06-18 kwa mahitaji ya usalama yanayohitajika  
  - **Uthibitishaji Ulioboreshwa**: Ushirikiano wa Microsoft Entra ID na mifano kamili ya .NET na Java Spring Security  
  - **Ushirikiano wa Usalama wa AI**: Microsoft Prompt Shields na utekelezaji wa Azure Content Safety na mifano ya kina ya Python  
  - **Uzuiaji wa Vitisho vya Juu**: Mifano kamili ya utekelezaji kwa  
    - Kuzuia Shambulio la Msaliti Mchanganyiko kwa PKCE na uthibitishaji wa idhini ya mtumiaji  
    - Kuzuia Kupitisha Tokeni kwa uthibitishaji wa hadhira na usimamizi wa tokeni salama  
    - Kuzuia Utekaji wa Kikao kwa binging ya kriptografia na uchambuzi wa tabia  
  - **Ushirikiano wa Usalama wa Biashara**: Ufuatiliaji wa Azure Application Insights, mifumo ya kugundua vitisho, na usalama wa mnyororo wa ugavi  
  - **Orodha ya Udhibiti wa Utekelezaji**: Udhibiti wa usalama wa lazima vs uliopendekezwa kwa faida za mfumo wa usalama wa Microsoft  

### Ubora wa Nyaraka & Ulinganifu wa Viwango  
- **Marejeleo ya Maelezo**: Imesasishwa marejeleo yote kwa MCP Specification 2025-06-18 ya sasa  
- **Mfumo wa Usalama wa Microsoft**: Mwongozo ulioboreshwa wa ushirikiano katika nyaraka zote za usalama  
- **Utekelezaji wa Kivitendo**: Kuongeza mifano ya kina ya msimbo katika .NET, Java, na Python na mifumo ya biashara  
- **Mpangilio wa Rasilimali**: Kuweka makundi kamili ya nyaraka rasmi, viwango vya usalama, na mwongozo wa utekelezaji  
- **Viashirio vya Kuona**: Kuweka alama wazi ya mahitaji yasiyoweza kuepukika vs mbinu zilizopendekezwa  

#### Misingi ya Misingi (01-CoreConcepts/) - Uboreshaji Kamili wa Kisasa  
- **Mabadiliko ya Toleo la Itifaki**: Imesasishwa kwa kurejelea MCP Specification 2025-06-18 na mfumo wa tarehe (muundo wa YYYY-MM-DD)  
- **Uboreshaji wa Usanifu**: Maelezo yaliyoimarishwa ya Wasemaji, Wateja, na Seva ili kuendana na mifumo ya sasa ya MCP  
  - Wasemaji sasa wamefafanuliwa wazi kama programu za AI zinazoratibu muunganisho wa wateja MCP wengi  
  - Wateja wameelezewa kama waunganishaji wa itifaki wanaodumisha mahusiano ya seva kwa moja kwa moja  
  - Seva zimeboreshwa kwa hali za usambazaji wa ndani dhidi ya za mbali  
- **Uundaji Upya wa Vitenzi**: Marekebisho kamili ya vitendo vya seva na wateja  
  - Vitenzi vya Seva: Rasilimali (vyanzo vya data), Maelekezo (templeti), Zana (nyenzo zinazotekelezeka) na maelezo na mifano kamili  
  - Vitenzi vya Mteja: Sampuli (ukamilishaji wa LLM), Kupata (maingizo ya mtumiaji), Kuingiza kumbukumbu (ugunduzi/ufuati)  
  - Imesasishwa kwa mifumo ya sasa ya ugunduzi (`*/list`), urejeshaji (`*/get`), na utekelezaji (`*/call`)  
- **Usanifu wa Itifaki**: Kuanzishwa kwa mfano wa usanifu wa tabaka mbili  
  - Tabaka la Data: Msingi wa JSON-RPC 2.0 na usimamizi wa mzunguko wa maisha na vitenzi  
  - Tabaka la Usafirishaji: STDIO (mitaa) na HTTP inayoelea na SSE (usafirishaji wa mbali)  
- **Mfumo wa Usalama**: Kanuni kamili za usalama ikiwa ni pamoja na idhini wazi ya mtumiaji, ulinzi wa faragha ya data, usalama wa utekelezaji wa zana, na usalama wa tabaka la usafirishaji  
- **Mifumo ya Mawasiliano**: Ujumbe wa itifaki umeboreshwa kuonyesha awamu za kuanzisha, ugunduzi, utekelezaji, na arifa  
- **Mifano ya Msimbo**: Mifano ya lugha nyingi (.NET, Java, Python, JavaScript) imepitishwa upya kuendana na mifumo ya MCP SDK ya sasa  

#### Usalama (02-Security/) - Marekebisho Kamili ya Usalama  
- **Ulinganifu na Viwango**: Ulinganifu wa kamili na mahitaji ya usalama ya MCP Specification 2025-06-18  
- **Mageuzi ya Uthibitishaji**: Kuripoti mageuzi kutoka seva zaOAuth za kawaida hadi kusimamia wakala wa mtoaji wa utambulisho wa nje (Microsoft Entra ID)  
- **Uchambuzi wa Vitisho Maalum vya AI**: Ufunikaji ulioboreshwa wa njia za kisasa za mashambulizi ya AI  
  - Matukio ya kina ya shambulio la sindano ya maelekezo na mifano halisi  
  - Mbinu za sumu ya zana na mifumo ya shambulio la "kutoroka"  
  - Sumukizi ya dirisha la muktadha na mashambulio ya mkanganyiko wa mfano  
- **Suluhisho za Usalama za AI za Microsoft**: Ufunikaji kamili wa mfumo wa usalama wa Microsoft  
  - AI Prompt Shields na utambuzi wa hali ya juu, kuchagua, na mbinu za delimiters  
  - Mifumo ya ushirikiano wa Azure Content Safety  
  - GitHub Advanced Security kwa ulinzi wa mnyororo wa ugavi  
- **Uzuiaji wa Vitisho vya Juu**: Udhibiti wa usalama wa kina kwa  
  - Utekaji wa kikao na muktadha wa mashambulizi ya MCP na mahitaji ya kitambulisho cha kikao cha kriptografia  
  - Shida za msaliti mchanganyiko katika hali za wakala wa MCP na mahitaji ya idhini wazi  
  - Udhaifu wa kupitisha tokeni na udhibiti wa lazima wa uthibitisho  
- **Usalama wa Mnyororo wa Ugavi**: Ufunikaji uliopanuliwa wa mnyororo wa ugavi wa AI ikiwa ni pamoja na mifano ya msingi, huduma za embeddings, watoa muktadha, na API za wahusika wengine  
- **Usalama wa Msingi**: Ushirikiano ulioimarishwa na mifumo ya biashara kabisa ikiwa ni pamoja na usanifu wa kuaminiana sifuri na mfumo wa usalama wa Microsoft  
- **Mpangilio wa Rasilimali**: Kuweka makundi ya viungo kamili vya rasilimali kwa aina (Nyaraka Rasmi, Viwango, Utafiti, Suluhisho za Microsoft, Mwongozo wa Utekelezaji)  

### Maboresho ya Ubora wa Nyaraka  
- **Malengo ya Kujifunza Yaliyopangwa**: Malengo ya kujifunza yaliyoimarishwa kwa matokeo maalum na ya vitendo  
- **Rejeleo za Msalaba**: Kuongeza viungo kati ya mada nyingine zinazohusiana za usalama na misingi  
- **Taarifa za Hali ya Sasa**: Kusanifisha marejeleo yote ya tarehe na viungo vya maelezo kwa viwango vya sasa  
- **Mwongozo wa Utekelezaji**: Kuongeza miongozo maalum ya vitendo ya utekelezaji katika sehemu zote mbili  

## Julai 16, 2025  

### README na Maboresho ya Kuangalia  
- Kupanga upya kabisa urambazaji wa mitaala katika README.md  
- Kubadilisha lebo za `<details>` kwa muundo unaopatikana zaidi wa jedwali  
- Kuunda chaguzi za muundo mbadala katika folda mpya ya "alternative_layouts"  
- Kuongeza mifano ya urambazaji wa kadi, tabbed-style, na accordion-style  
- Kusasisha sehemu ya muundo wa ghala ili kujumuisha faili zote za sasa  
- Kuongeza maelekezo wazi katika sehemu ya "Jinsi ya Kutumia Mitaala Hii"  
- Kuboresha viungo vya maelezo ya MCP kwa kuelekeza kwenye URL sahihi  
- Kuongeza sehemu ya Uhandisi wa Muktadha (5.14) kwenye muundo wa mitaala  

### Maboresho ya Mwongozo wa Kusoma  
- Kupitia upya kabisa mwongozo wa kusoma ili kuendana na muundo wa ghala wa sasa  
- Kuongeza sehemu mpya za Wateja wa MCP na Zana, na Seva za MCP Maarufu  
- Kusasisha Ramani ya Mitaala ya Kuona kwa kusahihisha mada zote  
- Kuongeza maelezo ya Mada za Juu kwa kufunika maeneo maalum yote  
- Kusasisha sehemu ya Mifano ya Kesi kwa kuonyesha mifano halisi  
- Kuongeza rekodi hii kamili ya mabadiliko  

### Michango ya Jamii (06-CommunityContributions/)  
- Kuongeza taarifa za kina kuhusu seva za MCP kwa uzalishaji wa picha  
- Kuongeza sehemu kamili juu ya kutumia Claude katika VSCode  
- Kuongeza maelekezo ya usanidi na matumizi ya mteja wa terminal wa Cline  
- Kusasisha sehemu ya mteja wa MCP ili kujumuisha chaguzi zote maarufu za mteja  
- Kuboresha mifano ya michango kwa sampuli za msimbo sahihi zaidi  

### Mada za Juu (05-AdvancedTopics/)  
- Kupanga folda zote za mada maalum kwa majina yanayofanana  
- Kuongeza nyenzo na mifano ya uhandisi wa muktadha  
- Kuongeza nyaraka za ushirikiano wa wakala wa Foundry  
- Kuboresha nyaraka za ushirikiano wa usalama wa Entra ID  

## Juni 11, 2025  

### Kuanzishwa kwa Awali  
- Kutoza toleo la kwanza la mitaala ya MCP kwa Waanzilishi  
- Kuunda muundo wa msingi kwa sehemu 10 kuu  
- Kutekeleza Ramani ya Mitaala ya Kuona kwa urambazaji  
- Kuongeza miradi ya mfano ya awali katika lugha nyingi za programu  

### Kuanzia (03-GettingStarted/)  
- Kuunda mifano ya utekelezaji wa seva wa kwanza  
- Kuongeza mwongozo wa maendeleo ya mteja  
- Kujumuisha maelekezo ya ushirikiano wa mteja wa LLM  
- Kuongeza nyaraka za ushirikiano wa VS Code  
- Kutekeleza mifano ya seva inayotuma Matukio (Server-Sent Events SSE)  

### Misingi ya Msingi (01-CoreConcepts/)  
- Kuongeza maelezo ya kina ya usanifu wa mteja-seva  
- Kuandika nyaraka juu ya vipengele muhimu vya itifaki  
- Kurekodi mifumo ya ujumbe katika MCP  

## Mei 23, 2025  

### Muundo wa Ghala  
- Kuanzisha ghala na muundo wa folda wa msingi  
- Kuunda faili za README kwa kila sehemu kuu  
- Kuanzisha miundombinu ya tafsiri  
- Kuongeza mali za picha na michoro  

### Nyaraka  
- Kuandika README.md ya awali yenye muhtasari wa mitaala  
- Kuongeza CODE_OF_CONDUCT.md na SECURITY.md  
- Kuanzisha SUPPORT.md na mwongozo wa kupata msaada  
- Kuunda muundo wa mwongozo wa kusoma wa awali  

## Aprili 15, 2025  

### Mipango na Mfumo  
- Mipango ya awali kwa mitaala ya MCP kwa Waanzilishi  
- Kuweka malengo ya kujifunza na hadhira lengwa  
- Kupanga muundo wa sehemu 10 wa mitaala  
- Kuendeleza mfumo wa dhana kwa mifano na masomo ya kesi  
- Kuunda mifano ya awali ya dhana kuu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kanganyo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotoshaji. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya mtaalamu wa kibinadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
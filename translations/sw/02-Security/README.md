# Usalama wa MCP: Ulinzi Kamili kwa Mifumo ya AI

[![MCP Security Best Practices](../../../translated_images/sw/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Bonyeza picha hapo juu kutazama video ya somo hili)_

Usalama ni msingi katika muundo wa mifumo ya AI, ndiyo sababu tunautilia mkazo kama sehemu yetu ya pili. Hii inaendana na kanuni ya Microsoft ya **Salama kwa Muundo** kutoka kwa [Mpango wa Usalama wa Baadaye](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Itifaki ya Muktadha wa Mfano (MCP) inaleta uwezo mpya wenye nguvu kwa programu zinazoendeshwa na AI huku ikileta changamoto za kipekee za usalama zinazozidi hatari za kawaida za programu. Mifumo ya MCP inakabiliwa na wasiwasi wa usalama uliowekwa (uandishi wa msimbo salama, upatikanaji mdogo, usalama wa mnyororo wa usambazaji) pamoja na vitisho vipya vya AI kama vile sindano ya amri, sumu ya zana, kuiba kikao, mashambulizi ya mtumishi aliyekosewa, hatari za kupitisha tokeni, na mabadiliko ya uwezo wa nguvu.

Somo hili linachunguza hatari muhimu zaidi za usalama katika utekelezaji wa MCP—likijumuisha uthibitishaji, idhini, ruhusa nyingi kupita kiasi, sindano isiyo ya moja kwa moja ya amri, usalama wa kikao, matatizo ya mtumishi aliyekosewa, usimamizi wa tokeni, na hatari katika mnyororo wa usambazaji. Utajifunza udhibiti unaoweza kutekelezwa na mbinu bora kupunguza hatari hizi huku ukitumia suluhisho za Microsoft kama Prompt Shields, Azure Content Safety, na GitHub Advanced Security kuimarisha utekelezaji wako wa MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- **Tambua Vitisho Vinavyowezekana kwa MCP**: Tambua hatari za kipekee za usalama katika mifumo ya MCP ikijumuisha sindano ya amri, sumu ya zana, ruhusa nyingi kupita kiasi, kuiba kikao, matatizo ya mtumishi aliyekosewa, hatari za kupitisha tokeni, na hatari katika mnyororo wa usambazaji
- **Tekeleza Udhibiti wa Usalama**: Weka mikakati madhubuti ikijumuisha uthibitishaji madhubuti, upatikanaji wa kiwango cha chini tu, usimamizi salama wa tokeni, udhibiti wa usalama wa kikao, na uhakikishaji wa mnyororo wa usambazaji
- **Tumia Suluhisho za Usalama za Microsoft**: Elewa na tumia Microsoft Prompt Shields, Azure Content Safety, na GitHub Advanced Security kwa ulinzi wa mzigo wa kazi wa MCP
- **Thibitisha Usalama wa Zana**: Tambua umuhimu wa uthibitishaji wa metadata za zana, ufuatiliaji wa mabadiliko ya nguvu, na kujilinda dhidi ya mashambulizi ya sindano ambayo si ya moja kwa moja
- **Unganisha Mbinu Bora**: Changanya kanuni za msingi za usalama (uandishi wa msimbo salama, kuimarisha seva, imani sifuri) na udhibiti wa MCP kwa ulinzi kamili

# Muundo wa Usalama wa MCP & Udhibiti

Utekelezaji wa kisasa wa MCP unahitaji mbinu za usalama zilizo na tabaka ambazo zinashughulikia usalama wa kawaida wa programu na vitisho vya kipekee vya AI. Maelezo ya MCP yanayobadilika kwa kasi yanaendelea kuboresha udhibiti wake wa usalama, kuruhusu muunganiko bora na vya usalama vya biashara na mbinu bora zilizowekwa.

Utafiti kutoka kwa [Ripoti ya Ulinzi Dijitali ya Microsoft](https://aka.ms/mddr) unaonesha kuwa **asilimia 98 ya uvunjifu uliripotiwa ungezuia kwa usafi madhubuti wa usalama**. Mkakati bora wa ulinzi ni mchanganyiko wa mbinu za msingi za usalama na udhibiti wa MCP—vipimo vikuu vya usalama vinabakia kuwa na athari kubwa zaidi kupunguza hatari za usalama kwa ujumla.

## Hali ya Usalama ya Sasa

> **Kumbuka:** Sura hii inachanganya udhibiti wa usalama wa MCP uliowekwa na
> miongozo ya sasa ya idhini ya **MCP Specification 2026-07-28**. Kila mara rejelea
> [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/) ya sasa,
> [ghala la MCP la GitHub](https://github.com/modelcontextprotocol), na
> [nyaraka za mbinu bora za usalama](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> wakati ukitekeleza msimbo unaohitaji usalama zaidi.

> **Sasisho la Idhini:** MCP `2026-07-28` inahitaji wateja kuthibitisha
> kipengele cha `iss` kwenye majibu ya idhini (RFC 9207) na kuunganisha
> sifa zilizosajiliwa na seva ya idhini inayotoa. Usajili wa Mteja wa Muda Hauna Taa;
> utekelezaji mpya unapaswa kutumia Hati za Metadata za Kitambulisho cha Mteja.
> Angalia [Mabadiliko katika MCP: Maelezo ya 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> kwa orodha kamili ya mabadiliko ya idhini.

## 🏔️ Warsha ya Mkutano wa Usalama wa MCP (Sherpa)

Kwa **mafunzo ya vitendo ya usalama**, tunapendekeza sana **Warsha ya Mkutano wa Usalama wa MCP** (Sherpa) - safari kamili ya kuongozwa ya kuhakikisha usalama wa seva za MCP katika Microsoft Azure.

### Muhtasari wa Warsha

[Warsha ya Mkutano wa Usalama wa MCP](https://azure-samples.github.io/sherpa/) inatoa mafunzo ya usalama yanayoweza kutekelezeka kupitia mbinu ya "nyeti → shambulio → tatua → thibitisha" iliyothibitishwa. Utafanya:

- **Jifunze kwa Kuvunja Mambo**: Pata uzoefu wa udhaifu kwa kutumia seva zisizo salama kwa makusudi
- **Tumia Usalama Asilia wa Azure**: Tumia Azure Entra ID, Key Vault, Usimamizi wa API, na AI Content Safety
- **Fuata Ulinzi wa Kina**: Pitia kambi zilizoandaa tabaka kamili za usalama
- **Tekeleza Viwango vya OWASP**: Kila mbinu inaendana na [Mwongozo wa Usalama wa MCP Azure wa OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Pata Msimbo wa Uzalishaji**: Toka na utekelezaji uliothibitishwa na kazi

### Njia ya Safari

| Kambi | Mwelekeo | Hatari za OWASP Zinazofunikwa |
|------|----------|-------------------------------|
| **Kambi ya Msingi** | Misingi ya MCP & udhaifu wa uthibitishaji | MCP01, MCP07 |
| **Kambi 1: Utambulisho** | OAuth 2.1, Utambulisho Unaosimamiwa wa Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Kambi 2: Mlangoni** | Usimamizi wa API, Anuani Binafsi, usimamizi | MCP02, MCP06, MCP07, MCP09 |
| **Kambi 3: Usalama wa Kuingilia/Kutoka** | Sindano ya amri, ulinzi wa taarifa binafsi, usalama wa maudhui | MCP03, MCP05, MCP06, MCP10 |
| **Kambi 4: Ufuatiliaji** | Uchanganuzi wa rekodi, dashibodi, ugunduzi wa vitisho | MCP04, MCP08 |
| **Msingi wa Mkutano** | Jaribio la muunganiko wa Timu Nyekundu / Timu ya Bluu | Zote |

**Anza Sasa**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Hatari Kumi Zaidi za Usalama za OWASP MCP

[Mwongozo wa Usalama wa MCP Azure wa OWASP](https://microsoft.github.io/mcp-azure-security-guide/) unaelezea hatari kumi muhimu zaidi za usalama kwa utekelezaji wa MCP:

| Hatari | Maelezo | Ulinzi wa Azure |
|--------|----------|--------------------|
| **MCP01** | Usimamizi Mbaya wa Tokeni & Kufichuka kwa Siri | Azure Key Vault, Managed Identity |
| **MCP02** | Kuongezeka kwa Ruhusa Kupitia Kupanua Wigo | RBAC, Conditional Access |
| **MCP03** | Sumu ya Zana | Uthibitishaji wa zana, uhakikisho wa uadilifu |
| **MCP04** | Mashambulio kwa Mnyororo wa Usambazaji wa Programu & Mabadiliko ya Tegemezi | GitHub Advanced Security, ukaguzi wa tegemezi |
| **MCP05** | Sindano na Utekelezaji wa Amri | Uthibitishaji wa data, kuweka kizuizi salama |
| **MCP06** | Kupotoshwa kwa Mtiririko wa Nia | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Uthibitisho na Uidhinishaji Usio wa Kutosha | Azure Entra ID, OAuth 2.1 na PKCE |
| **MCP08** | Ukosefu wa Ukaguzi na Telemetri | Azure Monitor, Application Insights |
| **MCP09** | Seva za MCP za Kivuli | Udhibiti wa Kituo cha API, upunguzaji wa mtandao |
| **MCP10** | Muingiliano wa Muktadha & Kutosha Kushiriki | Uainishaji wa data, kuonyeshwa kidogo |

### Mabadiliko ya Uthibitisho wa MCP

Maelezo ya MCP yamebadilika sana katika mbinu yake ya uthibitisho na uidhinishaji:

- **Mbinu ya Awali**: Maelezo ya awali yalihitaji waendelezaji kutekeleza seva za uthibitisho zilizobinafsishwa, ambapo seva za MCP zilifanya kazi kama Seva za Uidhinishaji za OAuth 2.0 zikisimamia uthibitisho wa mtumiaji moja kwa moja
- **Kiwango cha Sasa (`2026-07-28`)**: Seva za MCP zinaweza kuhamishia uthibitisho
  kwa watoa huduma wa utambulisho wa nje kama Microsoft Entra ID. Wateja pia lazima
  wazingatie mahitaji ya sasa ya uthibitishaji wa mtangaza na kufunga vyeti.
- **Usalama wa Tabaka la Usafirishaji**: Msaada ulioboreshwa kwa mifumo ya usafirishaji salama na mifumo sahihi ya uthibitisho kwa miunganisho ya ndani (STDIO) na nje (Streamable HTTP)

## Usalama wa Uthibitisho na Uidhinishaji

### Changamoto za Usalama za Sasa

Utekelezaji wa kisasa wa MCP unakabiliwa na changamoto kadhaa za uthibitisho na uidhinishaji:

### Hatari & Njia za Shambulio

- **Mantiki ya Uidhinishaji Isiyosawazishwa**: Utekelezaji mbaya wa uidhinishaji katika seva za MCP unaweza kufichua data nyeti na kutumika vibaya udhibiti wa ufikiaji
- **Uvunjizi wa Tokeni za OAuth**: Ujanja wa wizi wa tokeni za seva ya MCP ya ndani huruhusu wadukuzi kujifanya seva na kufikia huduma za chini
- **Udhaifu wa Kupitisha Tokeni**: Usimamizi mbaya wa tokeni huunda njia za kuepuka usalama na upungufu wa uwajibikaji
- **Ruhusa Zaidi ya Lazima**: Seva za MCP zilizo na ruhusa za ziada kuvunja kanuni za haki ya chini na kupanua maeneo ya mashambulio

#### Kupitisha Tokeni: Mwitikio Mbaya Mkubwa

**Kupitisha tokeni kwa njia isiyoidhinishwa ni marufuku kabisa** katika maelezo ya sasa ya uidhinishaji wa MCP kutokana na athari kubwa za usalama:

##### Kuepuka Udhibiti wa Usalama
- Seva za MCP na API za chini hutekeleza udhibiti muhimu wa usalama (kudhibiti kasi, uthibitishaji wa maombi, ufuatiliaji wa trafiki) unaotegemea uthibitishaji sahihi wa tokeni
- Matumizi ya tokeni kutoka mteja moja kwa moja kwa API huondoa ulinzi huu muhimu, kuharibu usanifu wa usalama

##### Changamoto za Uwajibikaji na Ukaguzi  
- Seva za MCP haziwezi kutofautisha kati ya wateja wanaotumia tokeni zilizotolewa na mtoaji wa juu, huku ukaguzi ukiyumba
- Magazeti ya seva za rasilimali ya chini yanaonyesha asili za maombi kwa njia isiyo sahihi badala ya via vya kati vya seva za MCP
- Uchunguzi wa tukio na ukaguzi wa kawaida unazidi kuwa mgumu sana

##### Hatari za Kutapeli Data
- Madai ya tokeni zisizothibitishwa huruhusu wahalifu waliopora tokeni kutumia seva za MCP kama wakala wa kutapeli data
- Uvunjaji wa mipaka ya kuaminika huruhusu mifumo isiyoidhinishwa kuingilia njia za usalama zilizokusudiwa

##### Njia za Mashambulio Zaidi ya Huduma Moja
- Tokeni zilizovunjika zinazokubaliwa na huduma nyingi huruhusu kusogea mfululizo kwenye mifumo inayohusiana
- Dhana za kuaminiana kati ya huduma zinaweza kuvunjwa wakati asili ya tokeni haiwezi kuthibitishwa

### Udhibiti wa Usalama & Mikakati ya Kukabili

**Mahitaji Muhimu ya Usalama:**

> **LAZIMA**: Seva za MCP **HAZIRUHUSIWI** kukubali tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP

#### Udhibiti wa Uthibitisho & Uidhinishaji

- **Ukaguzi Mkali wa Uidhinishaji**: Fanya ukaguzi wa kina wa mantiki ya uidhinishaji ya seva za MCP kuhakikisha watumiaji na wateja waliokusudiwa pekee ndio wanaopata rasilimali nyeti
  - **Mwongozo wa Utekelezaji**: [Azure API Management kama Lango la Uthibitisho kwa Seva za MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Uunganishaji wa Utambulisho**: [Kutumia Microsoft Entra ID kwa Uthibitisho wa Seva za MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Usimamizi Salama wa Tokeni**: Tekeleza [mbinu bora za uthibitishaji na maisha ya tokeni za Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Thibitisha madai ya watazamaji wa tokeni yanayolingana na utambulisho wa seva ya MCP
  - Tekeleza mzunguko sahihi wa tokeni na sera za kumaliza muda
  - Zuia mashambulio ya kurudia tokeni na matumizi yasiyoidhinishwa

- **Uhifadhi Salama wa Tokeni**: Hifadhi tokeni kwa usimbaji fiche wakati wote, ikijumuisha wakati wa kuhifadhi na usafirishaji
  - **Mbinu Bora**: [Mwongozo wa Uhifadhi na Usimbaji wa Tokeni Salama](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Utekelezaji wa Udhibiti wa Ufikiaji

- **Kanuni ya Ruhusa ya Chini Zaidi**: Wape seva za MCP ruhusa za chini kabisa zinazohitajika kwa utendakazi uliokusudiwa pekee
  - Vipindi vya ukaguzi wa ruhusa na masasisho ili kuzuia kuongezeka kwa ruhusa zisizohitajika
  - **Nyaraka za Microsoft**: [Usalama wa Ufikiaji wa Chini Zaidi wa Ruhusa](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Udhibiti wa Ufikiaji unaotegemea Nafasi (RBAC)**: Tekeleza mgawo mzuri wa majukumu
  - Weka wigo wa majukumu kwa rasilimali na vitendo maalum
  - Epuka ruhusa pana au zisizohitajika zinazopanua maeneo ya mashambulio

- **Ufuatiliaji wa Rudufu wa Ruhusa**: Tekeleza ukaguzi na ufuatiliaji endelevu wa ufikiaji
  - Fuata mifumo ya matumizi ya ruhusa kwa jambo lisilo la kawaida
  - Fanya matibabu ya haraka ya ruhusa nyingi au zisizotumiwa

## Vitisho vya Usalama vya AI Maalum

### Mashambulio ya Kuingiza Prompt & Udhibiti wa Zana

Utekelezaji wa kisasa wa MCP unakabiliwa na njia za mashambulio za AI zilizobobea ambazo hatua za usalama za kawaida haziwezi kuzitatua kikamilifu:

#### **Kuingiza Prompt kwa Njia Isiyo ya Moja kwa Moja (Kuingiza Prompt Miongoni mwa Fani Mbalimbali)**

**Kuingiza Prompt kwa Njia Isiyo ya Moja kwa Moja** ni moja ya udhaifu mkubwa katika mifumo ya AI yenye MCP. Wadukuzi huingiza maagizo mabaya ndani ya maudhui ya nje—nyaraka, kurasa za wavuti, barua pepe, au vyanzo vya data—ambavyo mifumo ya AI huyaelewa baadaye kama amri halali.

**Senario za Mashambulio:**
- **Kuingiza kwa Nyaraka**: Maagizo mabaya yaliyofichwa katika nyaraka zinazoshughulikiwa yanayosababisha vitendo vya AI visivyotarajiwa
- **Kutumia Maudhui ya Wavuti**: Kurasa za wavuti zilizovamiwa zenye prompt zilizojificha zinazoathiri tabia ya AI wakati wa kusukwa
- **Mashambulio ya Barua Pepe**: Prompti mbaya zilizopo kwenye barua pepe zinazosababisha wasaidizi wa AI kufichua taarifa au kufanya vitendo visivyoidhinishwa
- **Uchafuzi wa Vyanzo vya Data**: Hifadhidata au API zilizoingiliwa zinazotoa maudhui yenye sumu kwa mifumo ya AI

**Athari Halisi**: Mashambulio haya yanaweza kusababisha kupokonywa data, kuvunjwa kwa faragha, uzalishaji wa maudhui hatarishi, na udhibiti wa mwingiliano wa watumiaji. Kwa uchambuzi wa kina, angalia [Kuingiza Prompt katika MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sw/prompt-injection.ed9fbfde297ca877.webp)

#### **Mashambulio ya Utoaji Sumu kwa Zana**

**Utoaji Sumu kwa Zana** unalenga metadata inayofafanua zana za MCP, ukitumia jinsi LLMs zinavyotafsiri maelezo na vigezo vya zana kufanya maamuzi ya utekelezaji.

**Mbinu za Mashambulio:**
- **Ulaghai wa Metadata**: Wadukuzi huingiza maagizo mabaya ndani ya maelezo ya zana, ufafanuzi wa vigezo, au mifano ya matumizi
- **Maagizo Yasiyoonekana**: Prompt zilizofichwa katika metadata ya zana zinazoshughulikiwa na modeli za AI lakini hazionekani kwa watumiaji wa binadamu
- **Mabadiliko ya Zana Kwa Njia ya Mabadiliko Haramu ("Rug Pulls")**: Zana zilizoidhinishwa na watumiaji hubadilishwa baadaye fanya vitendo vya uovu bila uelewa wa mtumiaji
- **Kuingiza Vigezo**: Maudhui mabaya yaliyojengwa ndani ya skimu za vigezo vya zana zinazoonya tabia ya modeli


**Hatari za Seva zinazohudumiwa**: Seva za MCP za mbali zina hatari zilizoongezeka kwani ufafanuzi wa zana unaweza kusasishwa baada ya idhini ya mwanzo ya mtumiaji, ikizalisha matukio ambapo zana zilizokuwepo salama awali zinakuwa hatari. Kwa uchambuzi kamili, angalia [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sw/tool-injection.3b0b4a6b24de6bef.webp)

#### **Njia Nyingine za Kushambulia AI**

- **Uingizaji wa Amri Zaishio Katika Sekta Nyingine (XPIA)**: Mashambulizi yenye ustadi yanayotumia maudhui kutoka maeneo mengi ili kupita kwa udhibiti wa usalama
- **Marekebisho ya Uwezo wa Kitaalamu**: Mabadiliko ya moja kwa moja kwa uwezo wa zana yanayotoroka tathmini za awali za usalama
- **Uchangishaji wa Dirisha la Muktadha**: Mashambulizi yanayochanganya madirisha makubwa ya muktadha kuficha maelekezo hatari
- **Mashambulizi ya Kuchanganya Mfano**: Kutumia mapungufu ya mfano kuunda tabia zisizotarajiwa au zisizo salama


### Athari za Hatari za Usalama wa AI

**Matokeo ya Athari Kuu:**
- **Kupoteza Data**: Upatikanaji usioidhinishwa na wizi wa data nyeti za shirika au za binafsi
- **Uvunjishaji wa Faragha**: Kufichuliwa kwa taarifa za mtu binafsi za utambulisho (PII) na data nyeti za biashara  
- **Udhibiti wa Mfumo**: Mabadiliko yasiyokusudiwa kwa mifumo muhimu na michakato
- **Wizi wa Hati**: Ufisadi wa vidokezo vya uthibitishaji na hati za huduma
- **Msalaba wa Njia**: Matumizi ya mifumo ya AI iliyovamiwa kama nguzo kwa mashambulizi makubwa ya mtandao

### Suluhisho za Usalama za AI za Microsoft

#### **Milinda ya Amri za AI: Ulinzi wa Juu Dhidi ya Mashambulizi ya Uingizaji**

Microsoft **Milinda ya Amri za AI** hutoa ulinzi mpana dhidi ya mashambulizi ya uingizaji wa amri moja kwa moja na isiyo ya moja kwa moja kupitia tabaka mbalimbali za usalama:

##### **Mekaniko za Msingi za Ulinzi:**

1. **Ugunduzi na Kuchuja wa Juu**
   - Algorithi za kujifunza mashine na mbinu za NLP hugundua maelekezo hatari katika maudhui ya nje
   - Uchambuzi wa papo hapo wa nyaraka, kurasa za wavuti, barua pepe, na vyanzo vya data kwa tishio zilizojificha
   - Uelewa wa muktadha wa mifumo ya amri halali dhidi ya hatari

2. **Mbinu za Kuweka Mwangaza**  
   - Hutofautisha maelekezo ya mfumo yaliyoaminika na maingizo ya nje yanayoweza kuwa yamevamiwa
   - Mbinu za uongofu wa maandishi zinazoongeza umuhimu wa mfano huku zikitenganisha maudhui hatari
   - Husaidia mifumo ya AI kuhifadhi mlolongo sahihi wa maelekezo na kupuuza amri zilizowekwa

3. **Mifumo ya Delimita na Alama za Data**
   - Ufafanuzi wazi wa mipaka kati ya ujumbe wa mfumo uliothibitishwa na maandishi ya maingizo ya nje
   - Alama maalum zinabainisha mipaka kati ya vyanzo vya data vilivyoaminika na visivyoaminika
   - Tenganisho wazi linazuia mkanganyiko wa maelekezo na utekelezaji usioidhinishwa wa maamri

4. **Ujasusi wa Tishio Endelevu**
   - Microsoft hufuatilia kwa mara kwa mara mifumo mipya ya mashambulizi na kusasisha kinga
   - Ufuatiliaji wa tishio kwa mbinu mpya za uingizaji na njia za mashambulizi
   - Jedwali la mara kwa mara la usalama kuhakikisha ufanisi dhidi ya tishio zinazoibuka

5. **Uhusiano na Azure Content Safety**
   - Sehemu ya suite kamili ya Azure AI Content Safety
   - Ugunduzi wa ziada wa jaribio za jailbreak, maudhui hatari, na ukiukaji wa sera za usalama
   - Udhibiti wa usalama umeunganishwa katika vipengele vyote vya programu za AI

**Rasilimali za Utekelezaji**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sw/prompt-shield.ff5b95be76e9c78c.webp)


## Tishio la Usalama la MCP la Juu

### Udhaifu wa Kunyakua Kikao

**Udhaifu wa kunyakua kikao** ni njia muhimu ya mashambulizi katika utekelezaji wa MCP wenye hali, ambako wahalifu wasioidhinishwa hupata na kutumia vitambulisho halali vya kikao kuigiza wateja na kufanya vitendo visivyoidhinishwa.

#### **Matukio ya Mashambulizi na Hatari**

- **Uingizaji wa Amri katika Kunyakua Kikao**: Washambuliaji wenye vitambulisho vilivyoibiwa vya kikao huingiza matukio hatari katika seva zinazoshiriki hali ya kikao, yakiwezekana kusababisha vitendo hatari au upatikanaji wa data nyeti
- **Kuigiza Moja kwa Moja**: Vitambulisho vya kikao vilivyoibiwa huruhusu simu za moja kwa moja kwa seva ya MCP bila uthibitishaji, zikitibu washambuliaji kama watumiaji halali
- **Mtiririko Ulioathiriwa wa Kuendelea**: Washambuliaji wanaweza kufuta maombi mapema, kusababisha wateja halali kuendelea na maudhui yanayoweza kuwa hatari

#### **Udhibiti wa Usalama wa Usimamizi wa Kikao**

**Mahitaji Muhimu:**
- **Uthibitishaji wa Uidhinishaji**: Seva za MCP zinazotekeleza uidhinishaji **ZINAHITAJI** kuthibitisha OMBI ZOTE zinazoingia na **HAZITUMII** kikao kwa uthibitishaji
- **Uundaji Salama wa Kikao**: Tumia vitambulisho vya kikao salama kisimoshi, visivyo thabiti ambavyo vinatengenezwa kwa jenereta salama za nambari za nasibu
- **Ufungaji Maalum wa Mtumiaji**: Funga vitambulisho vya kikao na taarifa za mtumiaji kwa kutumia muundo kama `<user_id>:<session_id>` kuzuia matumizi mabaya ya kikao kati ya watumiaji
- **Usimamizi wa Mzunguko wa Kikao**: Tekeleza kumalizika salama, kuzunguka, na kubatilisha ili kupunguza dirisha la udhaifu
- **Usalama wa Usafirishaji**: HTTPS imetakiwa kwa mawasiliano yote kuzuia kukamatwa kwa vitambulisho vya kikao

### Tatizo la Msaidizi Aliyepotea Mwelekeo

**Tatizo la msaidizi aliyepotea mwelekeo** hutokea wakati seva za MCP zinakuwa wawakilishi wa uthibitishaji kati ya wateja na huduma za wahudumu wa tatu, zikitengeneza fursa za kupitisha uidhinishaji kupitia utumiaji wa kitambulisho cha mteja kisichobadilika.

#### **Mbinu za Mashambulizi na Hatari**

- **Kupitisha Kibali kwa Kutumia Vidakuzi**: Uthibitishaji wa mtumiaji wa awali hutoa vidakuzi vya idhini ambavyo washambuliaji hutumia kupitia maombi hatari ya uidhinishaji yenye URI za kuhamisha zilizofanywa kwa ustadi
- **Uziwi wa Msimbo wa Uidhinishaji**: Vidakuzi vya idhini vilivyopo vinaweza kusababisha seva za uidhinishaji kuruka vipeperushi vya idhini, zikielekeza misimbo kwenye vituo vya washambuliaji  
- **Upatikanaji Usioidhinishwa wa API**: Misimbo ya uidhinishaji iliyoporwa huruhusu kubadilishana tokeni na kuigiza watumiaji bila idhini wazi

#### **Mikakati ya Kukabiliana**

**Udhibiti Mhitaji:**
- **Mahitaji ya Idhini Bayana**: Seva za wakala wa MCP zinazotumia vitambulisho vya mteja visivyobadilika **ZINAHITAJI** kupata idhini ya mtumiaji kwa kila mteja aliyejiandikisha kwa nguvu
- **Utekelezaji Salama wa OAuth 2.1**: Fuata mbinu bora za usalama za OAuth ikiwemo PKCE (Proof Key for Code Exchange) kwa maombi yote ya uidhinishaji
- **Uthibitishaji Mkali wa Mteja**: Tekeleza uthibitishaji mkali wa URI za kuhamisha na vitambulisho vya mteja kuzuia matumizi mabaya

### Udhaifu wa Kupitisha Tokeni  

**Kupitisha tokeni** ni muundo usiofaa ambapo seva za MCP zinakubali tokeni za mteja bila uthibitishaji mzuri na kuzitumia kwa API za chini, kukanusha masharti ya uidhinishaji ya MCP.

#### **Madhara ya Usalama**

- **Kupitia Udhibiti**: Matumizi ya tokeni kutoka mteja moja kwa API huruka mipaka muhimu ya ukomo wa matumizi, uthibitishaji, na ufuatiliaji
- **Uharibifu wa Njia ya Uthibitisho**: Tokeni zilizotolewa juu hufanya usawazishaji wa mteja kuwa mgumu, kuharibika uwezo wa kuchunguza matukio
- **Utoaji Data Kupitia Wakala**: Tokeni zisizothibitishwa huruhusu wahalifu kutumia seva kama mawakala kwa upatikanaji usioidhinishwa wa data
- **Uvunjaji wa Mipaka ya Uaminifu**: Huduma za chini zinaweza kukanushwa ikiwa chanzo cha tokeni hakiwezi kuthibitishwa
- **Kuenea kwa Mashambulizi kwa Huduma Nyingi**: Tokeni zilizovamiwa zinazokubaliwa katika huduma nyingi huruhusu mwendo wa usaliti

#### **Udhibiti wa Usalama Unaohitajika**

**Mahitaji Yasiyotoleheshwa:**
- **Uthibitishaji wa Tokeni**: Seva za MCP **HAZITAKUBALI** tokeni ambazo hazijatolewa wazi kwa seva ya MCP
- **Uthibitishaji wa Wasikilizaji**: Hakikisha madai ya wasikilizaji wa tokeni yanalingana na utambulisho wa seva ya MCP
- **Mzunguko Mzuri wa Tokeni**: Tekeleza tokeni za muda mfupi kwa mbinu salama za kuzunguka


## Usalama wa Ugavi wa Vifaa kwa Mifumo ya AI

Usalama wa ugavi umeendelea zaidi ya utegemezi wa programu za jadi na sasa unajumuisha mfumo mzima wa AI. Utekelezaji wa MCP wa kisasa lazima uthibitishe na kufuatilia kwa umakini vipengele vyote vinavyohusiana na AI, kila kimoja kikiwa na mapungufu yanayoweza kuharibu uaminifu wa mfumo.

### Vipengele Vilivyopanuliwa vya Ugavi wa AI

**Utegemezi wa Programu za Jadi:**
- Maktaba na mifumo ya chanzo huria
- Picha za kontena na mifumo ya msingi  
- Zana za maendeleo na mitiririko ya ujenzi
- Vipengele vya miundombinu na huduma

**Vipengele Mahususi vya Ugavi wa AI:**
- **Mifano ya Msingi**: Mifano iliyoandaliwa awali kutoka kwa watoa huduma mbalimbali inayohitaji uthibitishaji wa asili
- **Huduma za Kuweka Alama**: Huduma za nje za urekebishaji na utafutaji wa maana
- **Wahudumu wa Muktadha**: Vyanzo vya data, misingi ya maarifa, na hazina za nyaraka  
- **API za Wahudumu wa Tatu**: Huduma za AI za nje, mitiririko ya ML, na vituo vya usindikaji data
- **Vifaa vya Mfano**: Uzito, usanidi, na tofauti za mfano zilizobinafsishwa
- **Vyanzo vya Takwimu za Mafunzo**: Seti za data zinazotumika kwa mafunzo na kubinafsisha

### Mkakati Kamili wa Usalama wa Ugavi

#### **Uthibitishaji na Uaminifu wa Vipengele**
- **Uthibitishaji wa Asili**: Thibitisha asili, leseni, na uadilifu wa vipengele vyote vya AI kabla ya ujumuishaji
- **Tathmini ya Usalama**: Fanya skani za mapungufu na hakiki za usalama kwa mifano, vyanzo vya data, na huduma za AI
- **Uchambuzi wa Sifa**: Pima rekodi za usalama na desturi za watoa huduma wa AI
- **Uthibitishaji wa Uzingatiaji**: Hakikisha vipengele vyote vinakidhi mahitaji ya usalama na kanuni za shirika

#### **Mitiririko Salama ya Uenezi**  
- **Usalama wa CI/CD otomatiki**: Jumuisha skani za usalama katika mitiririko ya uzalishaji otomatiki
- **Uadilifu wa Vifaa**: Tekeleza uthibitishaji wa kikryptografia kwa vifaa vyote vilivyotumwa (msimbo, mifano, usanidi)
- **Uenezi wa Hatua kwa Hatua**: Tumia mikakati ya uenezi wa pole pole na uthibitishaji wa usalama katika kila hatua
- **Hazina za Vifaa Zinazoaminika**: Tumia tu vitambulisho salama vilivyosajiliwa na vya kuaminika

#### **Ufuatiliaji Endelevu na Majibu**
- **Skani ya Utegemezi**: Ufuatiliaji wa mapungufu wa mara kwa mara kwa utegemezi wa programu na vipengele vya AI
- **Ufuatiliaji wa Mfano**: Tathmini endelevu ya tabia za mfano, mwendo wa utendaji, na matatizo ya usalama
- **Ufuatiliaji wa Afya ya Huduma**: Fuatilia huduma za AI za nje kwa upatikanaji, matukio ya usalama, na mabadiliko ya sera
- **Uhusishaji wa Ujasusi wa Tishio**: Changanya vyanzo vya habari vya tishio vinavyohusiana na hatari za usalama wa AI na ML

#### **Udhibiti wa Upatikanaji na Thamani ya Haki Ndogo**
- **Ruhusa za Ngazi ya Kipengele**: Zuia upatikanaji kwa mifano, data, na huduma kulingana na hitaji la kibiashara
- **Usimamizi wa Akaunti za Huduma**: Tekeleza akaunti za huduma zilizotengwa zenye ruhusa chache zinazohitajika
- **Ugawaji wa Mtandao**: Tenganya vipengele vya AI na punguza upatikanaji wa mtandao kati ya huduma
- **Udhibiti wa Lango la API**: Tumia lango kuu la API kudhibiti na kufuatilia upatikanaji wa huduma za AI za nje

#### **Majibu na Urejeshaji wa Tukio**
- **Tarafa za Majibu ya Kasi**: Taratibu zilizoanzishwa za kurekebisha au kubadilisha vipengele vya AI vilivyoathiriwa
- **Mzunguko wa Hati**: Mifumo ya otomatiki ya kuzungusha siri, funguo za API, na hati za huduma
- **Uwezo wa Kurudisha**: Uwezo wa kurejesha haraka matoleo yaliyokubaliwa ya vipengele vya AI
- **Urejeshaji wa Mavunjiko ya Ugavi**: Taratibu maalum za kukabiliana na uvunjaji wa huduma za AI kutoka chanzo cha juu

### Zana za Usalama za Microsoft na Uunganisho

**GitHub Advanced Security** hutoa ulinzi kamili wa mnyororo wa ugavi ikijumuisha:
- **Skani ya Siri**: Ugunduzi otomatiki wa nywila, funguo za API, na tokeni katika hazina
- **Skani ya Utegemezi**: Tathmini ya udhaifu wa utegemezi wa chanzo huria na maktaba
- **Uchambuzi wa CodeQL**: Uchambuzi wa msimbo wa muda mrefu kwa udhaifu wa usalama na matatizo ya uandishi wa msimbo
- **Uchunguzi wa Mnyororo wa Ugavi**: Uelewa wa afya ya utegemezi na hali ya usalama

**Uunganisho wa Azure DevOps & Azure Repos:**
- Uunganisho wa skani usalama bila mshono kwenye majukwaa ya maendeleo ya Microsoft
- Ukaguzi wa usalama wa moja kwa moja katika Azure Pipelines kwa mizigo ya AI
- Utekelezaji wa sera kwa uenezi salama wa vipengele vya AI

**Mazoezi ya Ndani ya Microsoft:**
Microsoft hufanya mazoezi ya kina ya usalama wa mnyororo wa ugavi katika bidhaa zote. Jifunze kuhusu mbinu zilizothibitishwa katika [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Mazoezi Bora ya Usalama wa Msingi

Utekelezaji wa MCP unakopa na kujenga juu ya hali ya usalama iliyopo katika shirika lako. Kuimarisha mazoezi ya usalama wa msingi kunaboresha sana usalama wa jumla wa mifumo ya AI na utekelezaji wa MCP.

### Misingi ya Usalama ya Msingi

#### **Mazoezi Salama ya Maendeleo**
- **Uzingatiaji wa OWASP**: Linda dhidi ya [OWASP Top 10](https://owasp.org/www-project-top-ten/) hatari za programu za wavuti
- **Ulinzi Maalum wa AI**: Tekeleza udhibiti kwa [OWASP Top 10 kwa LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Usimamizi Salama wa Siri**: Tumia hazina maalum kwa tokeni, funguo za API, na data nyeti za usanidi
- **Usimbaji wa Mwisho-mwisho**: Tekeleza mawasiliano salama kati ya vipengele vya programu na mtiririko wa data
- **Uthibitishaji wa Kuingiza**: Thibitisha kwa kina maingizo yote ya mtumiaji, vigezo vya API, na vyanzo vya data

#### **Uimarishaji wa Miundombinu**
- **Uthibitishaji wa Njia Mbili**: MFA iliyotakiwa kwa akaunti zote za usimamizi na huduma
- **Usimamizi wa Karatasi**: Kampuli za otomatiki na kwa wakati kwa mifumo ya uendeshaji, mifumo, na utegemezi  
- **Uingiliano wa Mtoa Utambulisho**: Usimamizi wa utambulisho wa kati kupitia watoa huduma wa utambulisho shirika (Microsoft Entra ID, Active Directory)
- **Ugawaji wa Mtandao**: Kutenganishwa kwa mantiki kwa vipengele vya MCP kupunguza nafasi za usaliti
- **Kanuni ya Thamani Ndogo**: Ruhusa za chini kabisa zinazohitajika kwa vipengele vyote vya mfumo na akaunti

#### **Ufuatiliaji na Ugunduzi wa Usalama**
- **Kufuatilia Kwa Kina**: Rekodi za kina za shughuli za programu ya AI, ikijumuisha mwingiliano kati ya wateja na seva za MCP
- **Uunganisho wa SIEM**: Msimamizi mkuu wa taarifa za usalama na matukio kwa kugundua hali za kushangaza
- **Uchambuzi wa Tabia**: Ufuatiliaji unaotumia AI kugundua mifumo isiyo ya kawaida katika tabia za mfumo na mtumiaji
- **Ujasusi wa Tishio**: Changanya vyanzo vya habari vya tishio vya nje na viashiria vya kuvamiwa (IOC)
- **Majibu ya Tukio**: Taratibu zilizoeleweka vizuri za kugundua, kujibu, na kurejesha hali baada ya tukio la usalama

#### **Miundo ya Zero Trust**
- **Usiwe na Uaminifu Kabla, Daima Thibitisha**: Thibitisho endelevu la watumiaji, vifaa, na muunganisho wa mtandao
- **Ugawaji Mdogo wa Mtandao**: Udhibiti wa mtandao kwa kina unaotenganisha mzigo na huduma binafsi
- **Usalama wa Kutegemea Utambulisho**: Sera za usalama zenye msingi kwa utambulisho uliothibitishwa badala ya eneo la mtandao
- **Tathmini Endelevu ya Hatari**: Tathmini ya hali ya usalama kwa kuzingatia muktadha wa sasa na tabia
- **Upatikanaji wa Masharti**: Udhibiti wa upatikanaji unaobadilika kulingana na vigezo vya hatari, eneo, na uaminifu wa kifaa

### Mifumo ya Uunganisho wa Shirika

#### **Uunganisho wa Mazingira ya Usalama wa Microsoft**
- **Microsoft Defender for Cloud**: Usimamizi kamili wa hali ya usalama wa wingu
- **Azure Sentinel**: SIEM na uwezo wa SOAR wa asili ya wingu kwa ulinzi wa mizigo ya AI
- **Microsoft Entra ID**: Usimamizi wa utambulisho na upatikanaji wa shirika na sera za upatikanaji wa masharti
- **Azure Key Vault**: Usimamizi wa siri ulioko katikati na msaada wa moduli ya usalama wa vifaa (HSM)
- **Microsoft Purview**: Usimamizi wa data na ulinganifu kwa vyanzo vya data na michakato ya AI

#### **Uzingatiaji wa Sheria na Utawala**
- **Ulinganifu wa Sheria**: Hakikisha utekelezaji wa MCP unakidhi mahitaji maalum ya ulinganifu wa tasnia (GDPR, HIPAA, SOC 2)

- **Uainishaji wa Data**: Kategorizing sahihi na utunzaji wa data nyeti inayoendeshwa na mifumo ya AI
- **Mifuatilio ya Ukaguzi**: Kurekodi kwa kina kwa ajili ya utii wa kanuni na uchunguzi wa uhalifu
- **Dhibiti za Usiri**: Utekelezaji wa kanuni za usiri-kwa-muundo katika usanifu wa mfumo wa AI
- **Usimamizi wa Mabadiliko**: Mchakato rasmi wa mapitio ya usalama ya mabadiliko ya mfumo wa AI

Mazoezi haya ya msingi huunda msingi imara wa usalama ambao huongeza ufanisi wa udhibiti wa usalama maalum wa MCP na hutoa ulinzi wa kina kwa programu zinazotumia AI.

## Muhimu wa Usalama wa Kujifunza

- **Njia ya Usalama ya Tabaka**: Changanya mazoezi ya msingi ya usalama (uginisho salama, cheo cha chini kabisa, uhakiki wa mnyororo wa ugavi, ufuatiliaji endelevu) na udhibiti maalum wa AI kwa ulinzi wa kina

- **Eneo la Vitisho Maalum za AI**: Mifumo ya MCP inakumbana na hatari za kipekee ikiwemo sindano ya amri, sumu ya zana, wizi wa kikao, matatizo ya msaidizi mchanganyiko, udhaifu wa kupitisha tokeni, na ruhusa nyingi zinazohitaji kinga maalum

- **Ubora wa Uthibitishaji na Uidhinishaji**: Tekeleza uthibitishaji imara kwa kutumia watoa huduma wa utambulisho wa nje (Microsoft Entra ID), kamata uhakiki sahihi wa tokeni, na usikubali tokeni ambazo hazijatolewa wazi kwa seva yako ya MCP

- **Kuzuia Mashambulizi ya AI**: Tumia Microsoft Prompt Shields na Azure Content Safety kulinda dhidi ya sindano ya amri isiyo ya moja kwa moja na mashambulizi ya sumu ya zana, huku ukihakiki metadata ya zana na kufuatilia mabadiliko ya nguvu

- **Usalama wa Kikao na Usafirishaji**: Tumia vitambulisho vya kikao visivyo vya kihesabu vinavyohusishwa na utambulisho wa watumiaji, tekeleza usimamizi sahihi wa maisha ya kikao, na usitumie vikao kwa uthibitishaji

- **Mazoezi Bora ya Usalama wa OAuth**: Zuia mashambulizi ya msaidizi mchanganyiko kupitia idhini wazi ya mtumiaji kwa wateja waliojiandikisha kwa nguvu, utekelezaji sahihi wa OAuth 2.1 na PKCE, na uhakiki mkali wa URI ya kurudisha  

- **Kanuni za Usalama wa Tokeni**: Epuka mifumo isiyofaa ya kupitisha tokeni, hakiki madai ya hadhira ya tokeni, tekeleza tokeni zenye muda mfupi za kuzunguka kwa usalama, na dumisha mipaka wazi ya kuamini

- **Usalama wa Kina wa Mnyororo wa Ugavi**: Tendea sehemu zote za ikolojia ya AI (modeli, embeddings, wasambazaji wa muktadha, API za nje) kwa uangalifu sawa wa usalama kama vizuizi vya kawaida vya programu

- **Mabadiliko Endelevu**: Kuwa wa kisasa na sifa za MCP zinazoendelea haraka, changia viwango vya jumuiya ya usalama, na dumisha mitazamo ya usalama inayoweza kubadilika kadri itakavyoendelea

- **Uunganishaji wa Usalama wa Microsoft**: Tumia mazingira kamili ya usalama ya Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) kwa ulinzi bora wa utekelezaji wa MCP

## Rasilimali Kamili

### **Nyaraka Rasmi za Usalama za MCP**
- [MCP Specification (Current: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **Rasilimali za Usalama za OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Orodha kamili ya OWASP MCP Top 10 na mwongozo wa utekelezaji wa Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Hatari rasmi za usalama za OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Mafunzo ya usalama ya vitendo kwa MCP kwenye Azure

### **Viwango vya Usalama & Mazoezi Bora**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Utafiti na Uchambuzi wa Usalama wa AI**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Suluhisho za Usalama za Microsoft**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Miongozo ya Utekelezaji & Mafunzo**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Usalama wa DevOps & Mnyororo wa Ugavi**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Nyaraka Zaidi za Usalama**

Kwa mwongozo kamili wa usalama, rejea nyaraka hizi maalum katika sehemu hii:

- **[Mfano wa Uidhinishaji wa CIMD na DCR](./samples/cimd-dcr-auth/README.md)** - Seva ya rasilimali ya TypeScript MCP `2026-07-28` inayoweza kuendeshwa ikilinganisha Nyaraka za Mapendeleo za ID ya Mteja na kurudisha nyuma kujiandikisha kwa Mteja Mwendawazimu zilizopotoka
- **[Mazoezi Bora ya Usalama ya MCP](./mcp-security-best-practices.md)** - Mazoezi bora kamili ya usalama kwa utekelezaji wa MCP
- **[Utekelezaji wa Azure Content Safety](./azure-content-safety-implementation.md)** - Mifano halisi ya utekelezaji kwa ushirikiano wa Azure Content Safety  
- **[Udhibiti wa Usalama wa MCP](./mcp-security-controls.md)** - Udhibiti wa hivi karibuni wa usalama na mbinu za utekelezaji wa MCP
- **[Mwongozo wa Haraka wa Mazoezi Bora ya MCP](./mcp-best-practices.md)** - Mwongozo wa rejea haraka kwa mazoezi muhimu ya usalama ya MCP
- **[BlueHat 2026: Kulinda mustakabali wa AI: Kulinda MCP kwa mifumo ya ulinzi wa kina](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Mifumo ya ulinzi wa kina kutoka Kituo cha Microsoft cha Majibu ya Usalama (MSRC)

### **Mafunzo ya Usalama ya Vitendo**

- **[Mafunzo ya Kikao cha Usalama cha MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - Warsha kamili ya vitendo kwa kulinda seva za MCP kwenye Azure na kambi za maendeleo kutoka Base Camp hadi Summit
- **[Mwongozo wa Usalama wa OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Usanifu wa rejea na mwongozo wa utekelezaji kwa hatari zote 10 za juu za OWASP MCP

---

## Nini Kinakuja

Ifuatavyo: [Sura ya 3: Kuanzia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
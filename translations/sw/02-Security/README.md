# Usalama wa MCP: Ulinzi Kamili kwa Mifumo ya AI

[![MCP Security Best Practices](../../../translated_images/sw/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Bonyeza picha hapo juu kutazama video ya somo hili)_

Usalama ni msingi wa muundo wa mfumo wa AI, ndiyo maana tunauipa kipaumbele kama sehemu yetu ya pili. Hii inaendana na kanuni ya Microsoft ya **Secure by Design** kutoka kwa [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Itifaki ya Muktadha wa Mfano (MCP) inaleta uwezo mpya wenye nguvu kwa programu zinazoendeshwa na AI huku ikileta changamoto za kipekee za usalama ambazo zinaenda zaidi ya hatari za kawaida za programu. Mifumo ya MCP inakabiliwa na wasiwasi wa usalama uliothibitishwa (kodi salama, ruhusa ndogo kabisa, usalama wa mnyororo wa usambazaji) na vitisho vipya vinavyohusiana na AI ikiwa ni pamoja na sindano ya maelekezo, sumu ya zana, udukuzi wa vikao, mashambulizi ya msaidizi mchanganyiko, udhaifu wa kupitisha tokeni, na mabadiliko ya uwezo wa mabadiliko.

Somo hili linachunguza hatari muhimu zaidi za usalama katika utekelezaji wa MCP—linashughulikia uthibitishaji, idhini, ruhusa nyingi sana, sindano isiyo ya moja kwa moja ya maelekezo, usalama wa kikao, matatizo ya msaidizi mchanganyiko, usimamizi wa tokeni, na udhaifu wa mnyororo wa usambazaji. Utajifunza udhibiti unaoweza kutekelezeka na mbinu bora za kupunguza hatari hizi huku ukitumia suluhisho za Microsoft kama Prompt Shields, Azure Content Safety, na GitHub Advanced Security kuimarisha usambazaji wako wa MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- **Kutambua Vitisho Maalum vya MCP**: Tambua hatari za kipekee za usalama katika mifumo ya MCP ikiwa ni pamoja na sindano ya maelekezo, sumu ya zana, ruhusa nyingi sana, udukuzi wa vikao, matatizo ya msaidizi mchanganyiko, udhaifu wa kupitisha tokeni, na hatari za mnyororo wa usambazaji
- **Kutumia Udhibiti wa Usalama**: Tekeleza mbinu madhubuti ikiwa ni pamoja na uthibitishaji thabiti, upatikanaji wa ruhusa ndogo kabisa, usimamizi salama wa tokeni, udhibiti wa usalama wa kikao, na uhakiki wa mnyororo wa usambazaji
- **Kuitumia Suluhisho za Usalama za Microsoft**: Elewa na tumia Microsoft Prompt Shields, Azure Content Safety, na GitHub Advanced Security kwa ulinzi wa mzigo wa kazi wa MCP
- **Kuthibitisha Usalama wa Zana**: Tambua umuhimu wa uthibitishaji wa metadata ya zana, ufuatiliaji wa mabadiliko ya mabadiliko, na kujilinda dhidi ya mashambulizi ya sindano isiyo ya moja kwa moja ya maelekezo
- **Kujumuisha Mbinu Bora**: Changanya misingi ya usalama iliyothibitishwa (kodi salama, kuimarisha seva, imani sifuri) na udhibiti maalum wa MCP kwa ulinzi kamili

# Miundo na Udhibiti wa Usalama wa MCP

Utekelezaji wa kisasa wa MCP unahitaji mbinu za usalama zenye tabaka nyingi zinazoshughulikia usalama wa kawaida wa programu na vitisho maalum vya AI. Maelezo ya MCP yanayobadilika kwa kasi yanaendelea kuboresha udhibiti wake wa usalama, kuruhusu ushirikiano bora na miundo ya usalama ya taasisi na mbinu bora zilizothibitishwa.

Utafiti kutoka kwa [Ripoti ya Ulinzi wa Kidijitali ya Microsoft](https://aka.ms/mddr) unaonyesha kuwa **asilimia 98 ya uvunjaji uliripotiwa ungezuia kwa usafi wa usalama thabiti**. Mkakati bora wa ulinzi unachanganya mbinu za msingi za usalama na udhibiti maalum wa MCP—mbinu za msingi za usalama zilizo thibitishwa bado ndizo zenye athari kubwa zaidi katika kupunguza hatari za usalama kwa ujumla.

## Hali ya Sasa ya Usalama

> **Kumbuka:** Taarifa hii inaonyesha viwango vya usalama vya MCP hadi **Desemba 18, 2025**. Itifaki ya MCP inaendelea kubadilika kwa kasi, na utekelezaji wa baadaye unaweza kuleta mifumo mipya ya uthibitishaji na udhibiti ulioimarishwa. Kila mara rejelea [Maelezo ya MCP](https://spec.modelcontextprotocol.io/), [hifadhidata ya MCP GitHub](https://github.com/modelcontextprotocol), na [nyaraka za mbinu bora za usalama](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) kwa mwongozo wa hivi karibuni.

### Mageuzi ya Uthibitishaji wa MCP

Maelezo ya MCP yamebadilika sana katika mbinu za uthibitishaji na idhini:

- **Mbinu ya Awali**: Maelezo ya awali yalihitaji waendelezaji kutekeleza seva za uthibitishaji za kawaida, huku seva za MCP zikifanya kazi kama Seva za Idhini za OAuth 2.0 zinazosimamia uthibitishaji wa watumiaji moja kwa moja
- **Kiwango cha Sasa (2025-11-25)**: Maelezo yaliyosasishwa yanaruhusu seva za MCP kuhamisha uthibitishaji kwa watoa huduma wa utambulisho wa nje (kama Microsoft Entra ID), kuboresha hali ya usalama na kupunguza ugumu wa utekelezaji
- **Usalama wa Tabaka la Usafirishaji**: Msaada ulioboreshwa kwa mbinu salama za usafirishaji na mifumo sahihi ya uthibitishaji kwa muunganisho wa ndani (STDIO) na wa mbali (Streamable HTTP)

## Usalama wa Uthibitishaji na Idhini

### Changamoto za Sasa za Usalama

Utekelezaji wa kisasa wa MCP unakabiliwa na changamoto kadhaa za uthibitishaji na idhini:

### Hatari na Njia za Mashambulizi

- **Mantiki ya Idhini Isiyosahihi**: Utekelezaji mbaya wa idhini katika seva za MCP unaweza kufichua data nyeti na kutekeleza udhibiti wa upatikanaji kwa makosa
- **Udukuzi wa Tokeni za OAuth**: Uziizi wa tokeni za seva za MCP za ndani unawawezesha wadukuzi kujifanya seva na kupata huduma za chini
- **Udhaifu wa Kupitisha Tokeni**: Usimamizi mbaya wa tokeni huunda njia za kupita udhibiti wa usalama na mapungufu ya uwajibikaji
- **Ruhusa Nyingi Sana**: Seva za MCP zilizo na ruhusa nyingi sana zinakiuka kanuni ya ruhusa ndogo kabisa na kuongeza maeneo ya mashambulizi

#### Kupitisha Tokeni: Kinyume Kikubwa cha Kanuni

**Kupitisha tokeni kinaruhusiwa kabisa** katika maelezo ya sasa ya idhini ya MCP kutokana na athari kubwa za usalama:

##### Kupita Udhibiti wa Usalama
- Seva za MCP na API za chini hutekeleza udhibiti muhimu wa usalama (kudhibiti kiwango, uthibitishaji wa maombi, ufuatiliaji wa trafiki) unaotegemea uthibitishaji sahihi wa tokeni
- Matumizi ya tokeni moja kwa moja kutoka kwa mteja hadi API hupita ulinzi huu muhimu, na kudhoofisha muundo wa usalama

##### Changamoto za Uwajibikaji na Ukaguzi  
- Seva za MCP haziwezi kutofautisha kati ya wateja wanaotumia tokeni zilizotolewa na huduma za juu, na kuvunja njia za ukaguzi
- Rekodi za seva za rasilimali za chini zinaonyesha vyanzo vya maombi visivyo sahihi badala ya wasuluhishi halisi wa seva za MCP
- Uchunguzi wa matukio na ukaguzi wa ufuataji wa sheria unakuwa mgumu sana

##### Hatari za Utoaji wa Data
- Dhamana zisizothibitishwa za tokeni zinawawezesha wahalifu wenye tokeni zilizoporwa kutumia seva za MCP kama mawakala wa kutoa data
- Kuvunja mipaka ya kuaminiana kunaruhusu mifumo ya upatikanaji isiyoidhinishwa kupita udhibiti wa usalama uliokusudiwa

##### Njia za Mashambulizi ya Huduma Nyingi
- Tokeni zilizovamiwa zinazokubaliwa na huduma nyingi huruhusu harakati za upande kwa upande katika mifumo iliyounganishwa
- Misingi ya kuaminiana kati ya huduma inaweza kuvunjwa wakati vyanzo vya tokeni haviwezi kuthibitishwa

### Udhibiti wa Usalama na Mbinu za Kupunguza

**Mahitaji Muhimu ya Usalama:**

> **LAZIMU**: Seva za MCP **HAZIRUHUSIWI** kukubali tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP

#### Udhibiti wa Uthibitishaji na Idhini

- **Mapitio Makini ya Idhini**: Fanya ukaguzi kamili wa mantiki ya idhini ya seva za MCP kuhakikisha watumiaji na wateja waliokusudiwa tu wanaweza kupata rasilimali nyeti
  - **Mwongozo wa Utekelezaji**: [Azure API Management kama Mlango wa Uthibitishaji kwa Seva za MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Ushirikiano wa Utambulisho**: [Kutumia Microsoft Entra ID kwa Uthibitishaji wa Seva za MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Usimamizi Salama wa Tokeni**: Tekeleza [mbinu bora za uthibitishaji na mzunguko wa tokeni za Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Thibitisha madai ya hadhira ya tokeni yanayolingana na utambulisho wa seva ya MCP
  - Tekeleza sera sahihi za mzunguko na kumalizika kwa tokeni
  - Zuia mashambulizi ya kurudia tokeni na matumizi yasiyoidhinishwa

- **Uhifadhi Salama wa Tokeni**: Hifadhi tokeni kwa usimbaji fiche wakati wa kuhifadhi na kusafirisha
  - **Mbinu Bora**: [Mwongozo wa Uhifadhi Salama wa Tokeni na Usimbaji](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Utekelezaji wa Udhibiti wa Upatikanaji

- **Kanuni ya Ruhusa Ndogo Kabisa**: Toa seva za MCP ruhusa ndogo kabisa zinazohitajika kwa utendaji uliokusudiwa
  - Mapitio na masasisho ya ruhusa mara kwa mara kuzuia kuongezeka kwa ruhusa zisizohitajika
  - **Nyaraka za Microsoft**: [Upatikanaji Salama wa Ruhusa Ndogo Kabisa](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Udhibiti wa Upatikanaji kwa Misingi ya Nafasi (RBAC)**: Tekeleza mgawanyo wa majukumu kwa undani
  - Weka mipaka ya majukumu kwa rasilimali na vitendo maalum
  - Epuka ruhusa pana au zisizohitajika zinazoongeza maeneo ya mashambulizi

- **Ufuatiliaji Endelevu wa Ruhusa**: Tekeleza ukaguzi na ufuatiliaji wa upatikanaji unaoendelea
  - Fuatilia mifumo ya matumizi ya ruhusa kwa mabadiliko yasiyo ya kawaida
  - Rekebisha mara moja ruhusa nyingi au zisizotumika

## Vitisho Maalum vya AI vya Usalama

### Mashambulizi ya Sindano ya Maelekezo na Udanganyifu wa Zana

Utekelezaji wa kisasa wa MCP unakabiliwa na njia za mashambulizi za kipekee za AI ambazo mbinu za kawaida za usalama haziwezi kuzitatua kikamilifu:

#### **Sindano Isiyo ya Moja kwa Moja ya Maelekezo (Sindano ya Maelekezo ya Mikoa Mbalimbali)**

**Sindano Isiyo ya Moja kwa Moja ya Maelekezo** ni moja ya udhaifu mkubwa zaidi katika mifumo ya AI inayotumia MCP. Wadukuzi huingiza maagizo mabaya ndani ya maudhui ya nje—nyaraka, kurasa za wavuti, barua pepe, au vyanzo vya data—ambavyo mifumo ya AI huchakata baadaye kama maagizo halali.

**Mazingira ya Mashambulizi:**
- **Sindano ya Nyaraka**: Maagizo mabaya yaliyofichwa katika nyaraka zinazochakatwa yanayosababisha vitendo visivyotarajiwa vya AI
- **Matumizi Mabaya ya Maudhui ya Wavuti**: Kurasa za wavuti zilizovamiwa zenye maelekezo yaliyowekwa ndani yanayodhibiti tabia ya AI wakati wa kuchambuliwa
- **Mashambulizi ya Barua Pepe**: Maelekezo mabaya katika barua pepe yanayosababisha wasaidizi wa AI kutoa taarifa au kufanya vitendo visivyoidhinishwa
- **Uchafuzi wa Vyanzo vya Data**: Hifadhidata au API zilizovamiwa zinazotoa maudhui yaliyochafuliwa kwa mifumo ya AI

**Athari Halisi**: Mashambulizi haya yanaweza kusababisha utoaji wa data, uvunjaji wa faragha, uzalishaji wa maudhui hatarishi, na udanganyifu wa mwingiliano wa watumiaji. Kwa uchambuzi wa kina, angalia [Sindano ya Maelekezo katika MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/sw/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Mashambulizi ya Sumu ya Zana**

**Sumu ya Zana** inalenga metadata inayofafanua zana za MCP, ikitumia jinsi LLMs zinavyotafsiri maelezo na vigezo vya zana kufanya maamuzi ya utekelezaji.

**Mbinu za Mashambulizi:**
- **Udanganyifu wa Metadata**: Wadukuzi huingiza maagizo mabaya katika maelezo ya zana, ufafanuzi wa vigezo, au mifano ya matumizi
- **Maagizo Yasiyoonekana**: Maelekezo yaliyofichwa katika metadata ya zana yanayosindikwa na mifano ya AI lakini hayaonekani kwa watumiaji wa binadamu
- **Mabadiliko ya Zana ya Muda ("Rug Pulls")**: Zana zilizokubaliwa na watumiaji hubadilishwa baadaye kufanya vitendo vibaya bila ufahamu wa mtumiaji
- **Sindano ya Vigezo**: Maudhui mabaya yaliyowekwa katika miundo ya vigezo vya zana yanayoathiri tabia ya mfano

**Hatari za Seva za Mbali**: Seva za MCP za mbali zina hatari kubwa kwani maelezo ya zana yanaweza kusasishwa baada ya idhini ya awali ya mtumiaji, kuunda mazingira ambapo zana zilizokuwa salama zinakuwa hatari. Kwa uchambuzi wa kina, angalia [Mashambulizi ya Sumu ya Zana (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/sw/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Njia Nyingine za Mashambulizi ya AI**

- **Sindano ya Maelekezo ya Mikoa Mbalimbali (XPIA)**: Mashambulizi ya hali ya juu yanayotumia maudhui kutoka mikoa mingi kupita udhibiti wa usalama
- **Mabadiliko ya Uwezo wa Mabadiliko**: Mabadiliko ya wakati halisi ya uwezo wa zana yanayokwepa tathmini za awali za usalama
- **Sumu ya Dirisha la Muktadha**: Mashambulizi yanayodanganya madirisha makubwa ya muktadha kuficha maagizo mabaya
- **Mashambulizi ya Kuchanganya Mfano**: Kutumia mapungufu ya mfano kuunda tabia zisizotarajiwa au zisizo salama

### Athari za Hatari za Usalama za AI

**Matokeo ya Athari Kubwa:**
- **Utoaji wa Data**: Upatikanaji usioidhinishwa na wizi wa data nyeti za taasisi au binafsi
- **Uvunjaji wa Faragha**: Kufichuliwa kwa taarifa za kibinafsi (PII) na data za biashara za siri  
- **Udanganyifu wa Mfumo**: Mabadiliko yasiyokusudiwa kwa mifumo muhimu na mtiririko wa kazi
- **Uziizi wa Cheti**: Uvunjaji wa tokeni za uthibitishaji na cheti za huduma
- **Harakati za Upande kwa Upande**: Matumizi ya mifumo ya AI iliyovamiwa kama njia za mashambulizi ya mtandao mpana

### Suluhisho za Usalama za AI za Microsoft

#### **AI Prompt Shields: Ulinzi wa Juu Dhidi ya Mashambulizi ya Sindano**

Microsoft **AI Prompt Shields** hutoa ulinzi kamili dhidi ya mashambulizi ya sindano ya maelekezo ya moja kwa moja na isiyo ya moja kwa moja kupitia tabaka nyingi za usalama:

##### **Mbinu za Msingi za Ulinzi:**

1. **Ugunduzi na Kuchuja wa Juu**
   - Algoriti za kujifunza mashine na mbinu za NLP hugundua maagizo mabaya katika maudhui ya nje
   - Uchambuzi wa wakati halisi wa nyaraka, kurasa za wavuti, barua pepe, na vyanzo vya data kwa vitisho vilivyowekwa ndani
   - Uelewa wa muktadha wa mifumo halali dhidi ya mifumo ya maelekezo mabaya

2. **Mbinu za Kuweka Mwanga**  
   - Hutofautisha kati ya maagizo ya mfumo yanayoaminika na maingizo ya nje yanayoweza kuwa yamevamiwa
   - Mbinu za mabadiliko ya maandishi zinazoongeza umuhimu wa mfano huku zikitenganisha maudhui mabaya
   - Husaidia mifumo ya AI kudumisha mpangilio sahihi wa maagizo na kupuuza amri zilizochanganywa

3. **Mifumo ya Kuweka Mipaka na Alama za Data**
   - Ufafanuzi wazi wa mipaka kati ya ujumbe wa mfumo unaoaminika na maandishi ya maingizo ya nje
   - Alama maalum zinazoonyesha mipaka kati ya vyanzo vya data vinavyoaminika na visivyoaminika
   - Tofauti wazi huzuia mkanganyiko wa maagizo na utekelezaji wa amri zisizoidhinishwa

4. **Ufuatiliaji Endelevu wa Ujasusi wa Vitisho**
   - Microsoft inaendelea kufuatilia mifumo mipya ya mashambulizi na kusasisha ulinzi
   - Utafutaji wa vitisho kwa njia ya kuzuia kwa mbinu mpya za sindano na njia za mashambulizi
   - Sasisho za mara kwa mara za mifano ya usalama kudumisha ufanisi dhidi ya vitisho vinavyobadilika

5. **Ushirikiano wa Azure Content Safety**
   - Sehemu ya suite kamili ya Azure AI Content Safety
   - Ugunduzi wa ziada wa jaribio la kuvunja kifungo, maudhui hatarishi, na ukiukaji wa sera za usalama
   - Udhibiti wa usalama uliounganishwa katika vipengele vya programu za AI

**Rasilimali za Utekelezaji**: [Nyaraka za Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/sw/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Vitisho vya Juu vya Usalama wa MCP

### Udhaifu wa Udukuzi wa Vikao

**Udukuzi wa kikao** ni njia muhimu ya mashambulizi katika utekelezaji wa MCP wenye hali ya kuhifadhi ambapo watu wasioidhinishwa wanapata na kutumia vitambulisho halali vya kikao kujifanya wateja na kufanya vitendo visivyoidhinishwa.

#### **Mazingira ya Mashambulizi na Hatari**

- **Sindano ya Maelekezo ya Udukuzi wa Kikao**: Wadukuzi wenye vitambulisho vya vikao vilivyoibwa huingiza matukio mabaya katika seva zinazoshiriki hali ya kikao, ambayo yanaweza kusababisha vitendo hatarishi au kupata data nyeti
- **Ujanja wa Moja kwa Moja**: Vitambulisho vya vikao vilivyoibwa huruhusu simu za moja kwa moja kwa seva za MCP zinazopita uthibitishaji, zikitumia wadukuzi kama watumiaji halali
- **Mtiririko wa Kuendelea Ulioathirika**: Wadukuzi wanaweza kumaliza maombi mapema, na kusababisha wateja halali kuendelea na maudhui yanayoweza kuwa mabaya

#### **Udhibiti wa Usalama kwa Usimamizi wa Vikao**

**Mahitaji Muhimu:**
- **Uthibitishaji wa Idhini**: seva za MCP zinazotekeleza idhini **LAZIMU** kuthibitisha MAOMBI yote yanayoingia na **HAIFAI** kutegemea vikao kwa uthibitishaji
- **Uundaji wa Vikao Salama**: Tumia vitambulisho vya kikao visivyo na utabiri vilivyotengenezwa kwa usalama wa kriptografia kwa kutumia jenereta za nambari za nasibu zilizo salama
- **Ufungaji Maalum kwa Mtumiaji**: Fungia vitambulisho vya kikao kwa taarifa maalum za mtumiaji kwa kutumia muundo kama `<user_id>:<session_id>` ili kuzuia matumizi mabaya ya vikao vya watumiaji wengine
- **Usimamizi wa Mzunguko wa Kikao**: Tekeleza kumalizika kwa muda, mzunguko, na kuharibu vikao ipasavyo ili kupunguza dirisha la udhaifu
- **Usalama wa Usafirishaji**: HTTPS ni lazima kwa mawasiliano yote ili kuzuia wizi wa vitambulisho vya kikao

### Tatizo la Msaidizi Mchanganyiko

**Tatizo la msaidizi mchanganyiko** hutokea wakati seva za MCP zinapotenda kama mawakala wa uthibitishaji kati ya wateja na huduma za wahusika wengine, na kuunda fursa za kupita idhini kupitia matumizi mabaya ya kitambulisho cha mteja kisichobadilika.

#### **Mbinu za Shambulio & Hatari**

- **Kupita Idhini kwa Vidakuzi vya Kukubali**: Uthibitishaji wa mtumiaji wa awali huunda vidakuzi vya kukubali ambavyo washambuliaji hutumia kupitia maombi ya idhini yenye nia mbaya na URI za kuongoza zilizotengenezwa
- **Uziwi wa Msimbo wa Idhini**: Vidakuzi vya kukubali vilivyopo vinaweza kusababisha seva za idhini kuruka skrini za kukubali, na kupeleka misimbo kwa vituo vinavyodhibitiwa na mshambuliaji  
- **Upatikanaji Usioidhinishwa wa API**: Misimbo ya idhini iliyoporwa huruhusu kubadilishana tokeni na kuiga mtumiaji bila idhini wazi

#### **Mikakati ya Kupunguza Hatari**

**Udhibiti wa Lazima:**
- **Mahitaji ya Idhini Wazi**: seva za wakala wa MCP zinazotumia vitambulisho vya mteja visivyobadilika **LAZIMU** kupata idhini ya mtumiaji kwa kila mteja aliyejisajili kwa nguvu
- **Utekelezaji wa Usalama wa OAuth 2.1**: Fuata mbinu bora za usalama za OAuth ikiwemo PKCE (Proof Key for Code Exchange) kwa maombi yote ya idhini
- **Uthibitishaji Mkali wa Mteja**: Tekeleza uthibitishaji mkali wa URI za kuongoza na vitambulisho vya mteja ili kuzuia matumizi mabaya

### Udhaifu wa Kupitisha Tokeni  

**Kupitisha tokeni** ni mfano wa kinyume ambapo seva za MCP zinakubali tokeni za mteja bila uthibitishaji sahihi na kuzipeleka kwa API za chini, kikiuka vipimo vya idhini vya MCP.

#### **Athari za Usalama**

- **Kupita Udhibiti**: Matumizi ya tokeni moja kwa moja kutoka mteja hadi API hupita udhibiti muhimu wa kuzuia kasi, uthibitishaji, na ufuatiliaji
- **Uharibifu wa Rekodi za Ukaguzi**: Tokeni zilizotolewa juu hufanya kutambua mteja kuwa vigumu, na kuvunja uwezo wa uchunguzi wa matukio
- **Utoaji wa Data Kupitia Wakala**: Tokeni zisizothibitishwa huruhusu wahalifu kutumia seva kama mawakala kwa upatikanaji usioidhinishwa wa data
- **Uvunjaji wa Mipaka ya Uaminifu**: Huduma za chini zinaweza kupatwa na uvunjaji wa dhana za uaminifu wakati chanzo cha tokeni hakiwezi kuthibitishwa
- **Upanuzi wa Shambulio kwa Huduma Nyingi**: Tokeni zilizovamiwa zinazokubaliwa katika huduma nyingi huruhusu harakati za upande

#### **Udhibiti wa Usalama Unaohitajika**

**Mahitaji Yasiyokubalika:**
- **Uthibitishaji wa Tokeni**: seva za MCP **HAZIFAI** kukubali tokeni zisizotolewa wazi kwa seva ya MCP
- **Uthibitishaji wa Hadhira**: Daima thibitisha madai ya hadhira ya tokeni yanayolingana na utambulisho wa seva ya MCP
- **Mzunguko Sahihi wa Tokeni**: Tekeleza tokeni za muda mfupi za upatikanaji na mbinu salama za mzunguko

## Usalama wa Mnyororo wa Ugavi kwa Mifumo ya AI

Usalama wa mnyororo wa ugavi umeendelea zaidi ya utegemezi wa kawaida wa programu na sasa unahusisha mfumo mzima wa AI. Utekelezaji wa kisasa wa MCP lazima uthibitishe na kufuatilia kwa ukamilifu vipengele vyote vinavyohusiana na AI, kwani kila kimoja kinaweza kuleta udhaifu unaoweza kuathiri usalama wa mfumo.

### Vipengele Vilivyopanuliwa vya Mnyororo wa Ugavi wa AI

**Utegemezi wa Kawaida wa Programu:**
- Maktaba na mifumo ya chanzo huria
- Picha za kontena na mifumo ya msingi  
- Zana za maendeleo na mistari ya ujenzi
- Vipengele vya miundombinu na huduma

**Vipengele Maalum vya Mnyororo wa Ugavi wa AI:**
- **Mifano ya Msingi**: Mifano iliyofunzwa awali kutoka kwa watoa huduma mbalimbali inayohitaji uthibitisho wa asili
- **Huduma za Uwekaji Alama**: Huduma za nje za kuunda vekta na utafutaji wa maana
- **Watoa Muktadha**: Vyanzo vya data, hifadhidata za maarifa, na maktaba za nyaraka  
- **API za Wahusika Wengine**: Huduma za AI za nje, mistari ya ML, na vituo vya usindikaji data
- **Vifaa vya Mfano**: Uzito, usanidi, na aina zilizobinafsishwa za mifano
- **Vyanzo vya Data za Mafunzo**: Seti za data zinazotumika kwa mafunzo na ubinafsishaji wa mifano

### Mkakati Kamili wa Usalama wa Mnyororo wa Ugavi

#### **Uthibitishaji wa Vipengele & Uaminifu**
- **Uthibitishaji wa Asili**: Thibitisha chanzo, leseni, na uadilifu wa vipengele vyote vya AI kabla ya kuingiza
- **Tathmini ya Usalama**: Fanya skanning za udhaifu na mapitio ya usalama kwa mifano, vyanzo vya data, na huduma za AI
- **Uchambuzi wa Sifa**: Tathmini rekodi za usalama na mbinu za watoa huduma za AI
- **Uthibitishaji wa Uzingatiaji**: Hakikisha vipengele vyote vinakidhi mahitaji ya usalama na kanuni za shirika

#### **Mistari ya Utekelezaji Salama**  
- **Usalama wa CI/CD Otomatiki**: Jumuisha skanning ya usalama katika mistari yote ya utoaji wa otomatiki
- **Uadilifu wa Vifaa**: Tekeleza uthibitishaji wa kriptografia kwa vifaa vyote vilivyotolewa (msimbo, mifano, usanidi)
- **Utoaji wa Hatua kwa Hatua**: Tumia mikakati ya utoaji wa hatua kwa hatua na uthibitishaji wa usalama katika kila hatua
- **Hifadhidata za Vifaa Zinazoaminika**: Toa tu kutoka kwa rejista na hifadhidata za vifaa zilizo thibitishwa na salama

#### **Ufuatiliaji Endelevu & Majibu**
- **Skanning ya Utegemezi**: Ufuatiliaji wa udhaifu unaoendelea kwa utegemezi wote wa programu na vipengele vya AI
- **Ufuatiliaji wa Mfano**: Tathmini endelevu ya tabia ya mfano, mabadiliko ya utendaji, na kasoro za usalama
- **Ufuatiliaji wa Afya ya Huduma**: Fuata huduma za AI za nje kwa upatikanaji, matukio ya usalama, na mabadiliko ya sera
- **Ujumuishaji wa Ujasusi wa Vitisho**: Jumuisha taarifa za vitisho maalum kwa hatari za usalama wa AI na ML

#### **Udhibiti wa Upatikanaji & Haki Ndogo Zaidi**
- **Ruhusa za Kiwango cha Kipengele**: Zuia upatikanaji wa mifano, data, na huduma kulingana na hitaji la biashara
- **Usimamizi wa Akaunti za Huduma**: Tekeleza akaunti za huduma zilizo maalum zenye ruhusa chache zinazohitajika
- **Ugawaji wa Mtandao**: Tengeneza sehemu za AI na punguza upatikanaji wa mtandao kati ya huduma
- **Udhibiti wa Lango la API**: Tumia lango kuu la API kudhibiti na kufuatilia upatikanaji wa huduma za AI za nje

#### **Majibu ya Tukio & Urejeshaji**
- **Tarifisho za Majibu ya Haraka**: Taratibu zilizoanzishwa za kufunga au kubadilisha vipengele vya AI vilivyovamiwa
- **Mzunguko wa Nywila**: Mifumo ya otomatiki ya kuzungusha siri, funguo za API, na nywila za huduma
- **Uwezo wa Kurudisha**: Uwezo wa kurudisha haraka matoleo ya awali yaliyojulikana kuwa salama ya vipengele vya AI
- **Urejeshaji wa Uvunjaji wa Mnyororo wa Ugavi**: Taratibu maalum za kujibu uvunjaji wa huduma za AI za juu

### Zana za Usalama za Microsoft & Ujumuishaji

**GitHub Advanced Security** hutoa ulinzi kamili wa mnyororo wa ugavi ikijumuisha:
- **Skanning ya Siri**: Kugundua otomatiki funguo, funguo za API, na tokeni katika hifadhidata
- **Skanning ya Utegemezi**: Tathmini ya udhaifu kwa utegemezi wa chanzo huria na maktaba
- **Uchambuzi wa CodeQL**: Uchambuzi wa msimbo wa kimantiki kwa udhaifu wa usalama na matatizo ya msimbo
- **Uelewa wa Mnyororo wa Ugavi**: Uwazi wa afya ya utegemezi na hali ya usalama

**Ujumuishaji wa Azure DevOps & Azure Repos:**
- Ujumuishaji wa skanning ya usalama bila mshono katika majukwaa ya maendeleo ya Microsoft
- Ukaguzi wa usalama wa otomatiki katika Azure Pipelines kwa mzigo wa AI
- Utekelezaji wa sera kwa utoaji salama wa vipengele vya AI

**Mazingira ya Ndani ya Microsoft:**
Microsoft inatekeleza mbinu za kina za usalama wa mnyororo wa ugavi katika bidhaa zote. Jifunze kuhusu mbinu zilizothibitishwa katika [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).

## Mbinu Bora za Usalama wa Msingi

Utekelezaji wa MCP unachukua na kujenga juu ya hali yako ya usalama ya shirika iliyopo. Kuimarisha mbinu za msingi za usalama huongeza kwa kiasi kikubwa usalama wa mifumo ya AI na utoaji wa MCP.

### Misingi ya Usalama Muhimu

#### **Mbinu Salama za Maendeleo**
- **Uzingatiaji wa OWASP**: Linda dhidi ya [Udhaifu wa Juu 10 wa OWASP](https://owasp.org/www-project-top-ten/) katika programu za wavuti
- **Ulinzi Maalum wa AI**: Tekeleza udhibiti kwa [Udhibiti wa Juu 10 wa OWASP kwa LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Usimamizi Salama wa Siri**: Tumia hifadhi maalum kwa tokeni, funguo za API, na data nyeti za usanidi
- **Usimbaji wa Mwisho kwa Mwisho**: Tekeleza mawasiliano salama katika vipengele vyote vya programu na mtiririko wa data
- **Uthibitishaji wa Ingizo**: Thibitisha kwa ukali ingizo zote za mtumiaji, vigezo vya API, na vyanzo vya data

#### **Kuimarisha Miundombinu**
- **Uthibitishaji wa Vipengele Vingi**: MFA ni lazima kwa akaunti zote za usimamizi na huduma
- **Usimamizi wa Marekebisho**: Marekebisho ya otomatiki na kwa wakati kwa mifumo ya uendeshaji, mifumo, na utegemezi  
- **Ujumuishaji wa Mtoa Utambulisho**: Usimamizi wa utambulisho wa kati kupitia watoa utambulisho wa shirika (Microsoft Entra ID, Active Directory)
- **Ugawaji wa Mtandao**: Kutenganisha kwa mantiki vipengele vya MCP ili kupunguza harakati za upande
- **Kanuni ya Haki Ndogo Zaidi**: Ruhusa chache zinazohitajika kwa vipengele vyote vya mfumo na akaunti

#### **Ufuatiliaji wa Usalama & Ugunduzi**
- **Kufuatilia kwa Kina**: Rekodi za kina za shughuli za programu za AI, ikijumuisha mwingiliano wa mteja-seva wa MCP
- **Ujumuishaji wa SIEM**: Usimamizi wa taarifa za usalama na matukio kwa ugunduzi wa kasoro
- **Uchambuzi wa Tabia**: Ufuatiliaji unaotumia AI kugundua mifumo isiyo ya kawaida katika mfumo na tabia za mtumiaji
- **Ujasusi wa Vitisho**: Ujumuishaji wa taarifa za vitisho vya nje na viashiria vya uvunjaji (IOCs)
- **Majibu ya Tukio**: Taratibu zilizo wazi za kugundua, kujibu, na kurejesha matukio ya usalama

#### **Msingi wa Zero Trust**
- **Usiamini Kamwe, Thibitisha Daima**: Uthibitishaji endelevu wa watumiaji, vifaa, na muunganisho wa mtandao
- **Ugawaji Mdogo wa Mtandao**: Udhibiti wa mtandao wa kina unaotenganisha mzigo na huduma binafsi
- **Usalama Unaozingatia Utambulisho**: Sera za usalama zinazotegemea utambulisho uliothibitishwa badala ya eneo la mtandao
- **Tathmini Endelevu ya Hatari**: Tathmini ya hali ya usalama kwa muktadha wa sasa na tabia
- **Upatikanaji wa Masharti**: Udhibiti wa upatikanaji unaobadilika kulingana na hatari, eneo, na uaminifu wa kifaa

### Mifumo ya Ujumuishaji wa Shirika

#### **Ujumuishaji wa Mazingira ya Usalama ya Microsoft**
- **Microsoft Defender for Cloud**: Usimamizi kamili wa hali ya usalama wa wingu
- **Azure Sentinel**: SIEM na SOAR asili ya wingu kwa ulinzi wa mzigo wa AI
- **Microsoft Entra ID**: Usimamizi wa utambulisho na upatikanaji wa shirika na sera za upatikanaji wa masharti
- **Azure Key Vault**: Usimamizi wa siri wa kati na msaada wa HSM
- **Microsoft Purview**: Usimamizi wa data na uzingatiaji kwa vyanzo vya data na mtiririko wa AI

#### **Uzingatiaji & Usimamizi**
- **Ulinganifu wa Kanuni**: Hakikisha utekelezaji wa MCP unakidhi mahitaji ya ulinganifu wa sekta (GDPR, HIPAA, SOC 2)
- **Uainishaji wa Data**: Kategorisha na kushughulikia data nyeti inayosindika mifumo ya AI ipasavyo
- **Rekodi za Ukaguzi**: Rekodi kamili kwa ulinganifu wa kanuni na uchunguzi wa forensiki
- **Udhibiti wa Faragha**: Tekeleza kanuni za faragha kwa muundo wa mifumo ya AI
- **Usimamizi wa Mabadiliko**: Taratibu rasmi za mapitio ya usalama kwa mabadiliko ya mifumo ya AI

Mbinu hizi za msingi huunda msingi thabiti wa usalama unaoongeza ufanisi wa udhibiti wa usalama wa MCP na kutoa ulinzi kamili kwa programu zinazoendeshwa na AI.

## Muhimu wa Usalama

- **Mbinu ya Usalama ya Tabaka**: Changanya mbinu za msingi za usalama (kodi salama, haki ndogo, uthibitishaji wa mnyororo wa ugavi, ufuatiliaji endelevu) na udhibiti maalum wa AI kwa ulinzi kamili

- **Mazingira Maalum ya Vitisho vya AI**: Mifumo ya MCP inakabiliwa na hatari za kipekee kama sindano za maelekezo, sumu ya zana, wizi wa vikao, matatizo ya msaidizi mchanganyiko, udhaifu wa kupitisha tokeni, na ruhusa nyingi zinazohitaji mbinu maalum za kupunguza

- **Ubora wa Uthibitishaji & Idhini**: Tekeleza uthibitishaji thabiti kwa kutumia watoa utambulisho wa nje (Microsoft Entra ID), fanya uthibitishaji sahihi wa tokeni, na usikubali tokeni zisizotolewa wazi kwa seva yako ya MCP

- **Kuzuia Shambulio za AI**: Tumia Microsoft Prompt Shields na Azure Content Safety kulinda dhidi ya sindano zisizo za moja kwa moja za maelekezo na sumu ya zana, huku ukithibitisha metadata ya zana na kufuatilia mabadiliko ya nguvu

- **Usalama wa Vikao & Usafirishaji**: Tumia vitambulisho vya kikao visivyo na utabiri vilivyofungamana na utambulisho wa watumiaji, tekeleza usimamizi sahihi wa mzunguko wa kikao, na usitumie vikao kwa uthibitishaji

- **Mbinu Bora za Usalama wa OAuth**: Zuia mashambulio ya msaidizi mchanganyiko kupitia idhini wazi ya mtumiaji kwa wateja waliosajiliwa kwa nguvu, utekelezaji sahihi wa OAuth 2.1 na PKCE, na uthibitishaji mkali wa URI za kuongoza

- **Kanuni za Usalama wa Tokeni**: Epuka mifumo ya kupitisha tokeni isiyofaa, thibitisha madai ya hadhira ya tokeni, tekeleza tokeni za muda mfupi na mzunguko salama, na dumisha mipaka wazi ya uaminifu

- **Usalama Kamili wa Mnyororo wa Ugavi**: Tibu vipengele vyote vya mfumo wa AI (mifano, uwekaji alama, watoa muktadha, API za nje) kwa ukali sawa wa usalama kama utegemezi wa kawaida wa programu

- **Mabadiliko Endelevu**: Endelea kufuatilia vipimo vya MCP vinavyobadilika haraka, changia viwango vya jumuiya za usalama, na dumisha hali za usalama zinazobadilika kadri itakavyohitajika

- **Ujumuishaji wa Usalama wa Microsoft**: Tumia mazingira kamili ya usalama ya Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) kwa ulinzi bora wa utoaji wa MCP

## Rasilimali Kamili

### **Nyaraka Rasmi za Usalama za MCP**
- [MCP Specification (Current: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **Viwango vya Usalama & Mbinu Bora**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Utafiti & Uchambuzi wa Usalama wa AI**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Suluhisho za Usalama za Microsoft**
- [Nyaraka za Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Huduma ya Usalama wa Maudhui ya Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Usalama wa Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Mazingira Bora ya Usimamizi wa Tokeni za Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Usalama wa Juu wa GitHub](https://github.com/security/advanced-security)

### **Miongozo ya Utekelezaji & Mafunzo**
- [Usimamizi wa API wa Azure kama Lango la Uthibitishaji la MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Uthibitishaji wa Microsoft Entra ID na Seva za MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Uhifadhi Salama wa Tokeni na Usimbaji (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Usalama wa DevOps & Mnyororo wa Ugavi**
- [Usalama wa Azure DevOps](https://azure.microsoft.com/products/devops)
- [Usalama wa Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Safari ya Usalama wa Mnyororo wa Ugavi wa Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Nyaraka Zaidi za Usalama**

Kwa mwongozo kamili wa usalama, rejelea nyaraka maalum katika sehemu hii:

- **[MCP Mazoezi Bora ya Usalama 2025](./mcp-security-best-practices-2025.md)** - Mazoezi bora kamili ya usalama kwa utekelezaji wa MCP
- **[Utekelezaji wa Usalama wa Maudhui ya Azure](./azure-content-safety-implementation.md)** - Mifano ya utekelezaji wa vitendo kwa ushirikiano wa Usalama wa Maudhui ya Azure  
- **[Dhibiti za Usalama za MCP 2025](./mcp-security-controls-2025.md)** - Dhibiti na mbinu za hivi karibuni za usalama kwa usambazaji wa MCP
- **[Rejeleo la Haraka la Mazoezi Bora ya MCP](./mcp-best-practices.md)** - Mwongozo wa haraka kwa mazoezi muhimu ya usalama wa MCP

---

## Nini Kifuatacho

Kifuatacho: [Sura ya 3: Kuanzia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Kutotegemea**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
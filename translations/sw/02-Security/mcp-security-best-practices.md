# MCP Mazoezi Bora ya Usalama - Sasisho la Septemba 2026

> **Muhimu:** Hati hii inaakisi
> [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> na rasmi
> [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Mafunzo ya Usalama ya Vitendo

Kwa uzoefu wa utekelezaji wa vitendo, tunapendekeza **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - ziara ya kina ya kuongoza kwa usalama wa seva za MCP katika Azure. Warsha inashughulikia hatari zote za OWASP MCP Top 10 kupitia mbinu ya "dhaifu → matumizi mabaya → kurekebisha → kuthibitisha".

Mazoezi yote katika hati hii yanalingana na **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** kwa mwongozo wa utekelezaji maalum wa Azure.

## Mazoezi Muhimu ya Usalama kwa Utekelezaji wa MCP

Itifaki ya Muktadha wa Mfano inaleta changamoto za kipekee za usalama zinazozidi
usalama wa kawaida wa programu. Mazoezi haya yanashughulikia mahitaji ya msingi
na tishio maalum za MCP ikiwa ni pamoja na sindano ya maagizo, sumu ya zana,
uzii wa hali-ya-mtumiaji, matatizo ya dhamana isiyoeleweka, na mianya ya
kupitisha tokeni.

### **Mahitaji YA IDHIBITIYA ya Usalama**

**Mahitaji Muhimu kutoka MCP Specification:**

> **HAIFAI:** seva za MCP **HAIFAI** kukubali tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP
> 
> **HITAJI:** seva za MCP zinazotekeleza idhini **HITAJI** kuthibitisha maombi yote yanayoingia
>  
> **HAIFAI:** seva za MCP **HAIFAI** kutumia vipindi vya kikao kwa uthibitishaji
>
> **HITAJI:** seva za wakala wa MCP zinazotumia kitambulisho cha mteja wa upande wa tatu kisichobadilika **HITAJI**
> kupata idhini ya kila mteja wa MCP kabla ya kusambaza idhini

---

## 1. **Usalama wa Tokeni & Uthibitishaji**

**Udhibiti wa Uthibitishaji & Idhini:**
   - **Uhakiki Mkali wa Idhini**: Fanya ukaguzi kamili wa mantiki ya idhini ya seva za MCP kuhakikisha watumiaji na wateja waliokusudiwa pekee wanaweza kupata rasilimali
   - **Uunganisho wa Mtoa Utambulisho wa Nje**: Tumia watoa utambulisho walioko kama Microsoft Entra ID badala ya kutekeleza uthibitishaji wa kawaida
   - **Uhakiki wa Hadhira ya Tokeni**: Daima hakiki kwamba tokeni zilitolewa wazi kwa seva yako ya MCP - kamwe usikubali tokeni za juu zaidi
   - **Mzunguko Sahihi wa Tokeni**: Tekeleza mzunguko salama wa tokeni, sera za kumalizika kwa tokeni, na zingatia kuzuia mashambulizi ya kurudia tokeni

**Uhifadhi Salama wa Tokeni:**
   - Tumia Azure Key Vault au hifadhi salama za hati kama hizo kwa siri zote
   - Tekeleza usimbaji kwa tokeni ikiwa wamelala na wakati wa kusafirishwa
   - Rudufu ya hati mara kwa mara na ufuatiliaji wa kufikia isiyoruhusiwa

## 2. **Hali ya Mtumiaji & Usalama wa Usafirishaji**

**Mazoezi Salama ya Hali ya Maombi:**

- **Vikibali Visivyoonekano vya Hali:** Tumia vikibali salama, visivyoeleweka kwa hali ya
   maombi vinavyoenea kwa maombi
- **Ufungaji wa Mtumiaji-Maalum:** Funga vikibali upande wa seva kwa mtumiaji aliyethibitishwa
   na kataa matumizi tena kati ya watumiaji
- **Usimamizi wa Mzunguko wa Maisha:** Maliza na futilia mbali vikibali ili kupunguza dirisha la hatari
   la udhaifu
- **Idhini kwa kila Ombi:** Kamwe usichukulie kikibali cha hali kama uthibitishaji;
   idhinisha kila ombi linalolifikia

**Usalama wa Tabaka la Usafirishaji:**

- Hitaji HTTPS kwa usafirishaji wa HTTP mbali katika uzalishaji
- Tumia upweke wa michakato na hati za mazingira kwa seva za stdio za ndani
- Sanidi TLS ya kisasa na mzunguko sahihi wa vyeti na uhakiki


## 3. **Ulinzi Maalum wa Vitisho vya AI** 🤖

**Ulinzi wa Injection ya Prompt:**
   - **Microsoft Prompt Shields**: Tumia AI Prompt Shields kwa utambuzi wa hali ya juu na kuchuja maelekezo hatari
   - **Usafishaji wa Ingizo**: Thibitisha na safisha ingizo zote ili kuzuia mashambulizi ya injection na matatizo ya confused deputy
   - **Mikabala ya Maudhui**: Tumia mfumo wa delimiter na datamarking kutofautisha maelekezo yanayotegemewa na maudhui ya nje

**Kuzuia Uharibifu wa Vifaa:**
   - **Uthibitishaji wa Metadata ya Vifaa**: Tekeleza ukaguzi wa uadilifu wa maelezo ya vifaa na fuatilia mabadiliko yasiyotarajiwa
   - **Ufuatiliaji wa Vifaa kwa Wakati Halisi**: Fuata mwenendo wa wakati wa utekelezaji na weka onyo kwa mifumo isiyotarajiwa ya utekelezaji
   - **Mchakato wa Idhini**: Hitaji idhini wazi ya mtumiaji kwa mabadiliko ya vifaa na mabadiliko ya uwezo

## 4. **Udhibiti wa Ufikiaji na Ruhusa**

**Kanuni ya Ruhusa za Chini Zaidi Inazohitajika:**
   - Toa ruhusa za chini kabisa kwa seva ya MCP zinazohitajika kwa ajili ya utendaji uliokusudiwa
   - Tekeleza udhibiti wa ufikiaji wa kimsingi wa kazi (RBAC) kwa ruhusa maalum
   - Fanya mapitio ya mara kwa mara ya ruhusa na ufuatiliaji endelevu wa ongezeko la ruhusa

**Udhibiti wa Ruhusa Wakati wa Kutekeleza:**
   - Tumia mipaka ya rasilimali kuzuia mashambulizi ya uchakachuaji rasilimali
   - Tumia kugawanya kwa kontena kwa mazingira ya utekelezaji wa vifaa  
   - Tekeleza ufikiaji wa wakati muafaka kwa kazi za kiutawala

## 5. **Usalama wa Maudhui na Ufuatiliaji**

**Utekelezaji wa Usalama wa Maudhui:**
   - **Ushirikiano wa Azure Content Safety**: Tumia Azure Content Safety kugundua maudhui hatarishi, jaribio la jailbreak, na ukiukaji wa sera
   - **Uchambuzi wa Tabia**: Tekeleza ufuatiliaji wa tabia wakati wa utekelezaji kugundua uvujaji katika seva ya MCP na vifaa
   - **Kumbukumbu Kamili**: Rekodi majaribio yote ya uthibitishaji, mwito wa vifaa, na matukio ya usalama kwa hifadhi salama, isiyoweza kubadilishwa

**Ufuatiliaji Endelevu:**
   - Arifa za wakati halisi kwa mifumo isiyo ya kawaida na jaribio la ufikiaji usioidhinishwa  
   - Ushirikiano na mifumo ya SIEM kwa usimamizi wa kit centralized wa matukio ya usalama
   - Ukaguzi wa mara kwa mara wa usalama na majaribio ya uvunjaji wa usalama wa utekelezaji wa MCP

## 6. **Usalama wa Mnyororo wa Ugavi**

**Uthibitishaji wa Vipengele:**
   - **Uchunguzi wa Mtegemeo**: Tumia skanningi ya otomatiki ya udhaifu kwa vyanzo vyote vya programu na vipengele vya AI
   - **Uthibitishaji wa Asili**: Thibitisha asili, leseni, na uadilifu wa mifano, vyanzo vya data, na huduma za nje
   - **Pakiti Zenye Saini**: Tumia pakiti zilizosainiwa kwa njia ya cryptographic na thibitisha saini kabla ya kutekeleza

**Mtiririko Salama wa Maendeleo:**
   - **Usalama wa Juu wa GitHub**: Tekeleza utambuzi wa siri, uchambuzi wa utegemezi, na uchambuzi wa CodeQL wa hali ya static
   - **Usalama wa CI/CD**: Shirikisha uthibitisho wa usalama katika mitiririko ya otomatiki ya utoaji
   - **Uadilifu wa Vifaa**: Tekeleza uthibitisho wa cryptographic kwa vifaa vilivyotolewa na mipangilio

## 7. **Usalama wa OAuth na Kuzuia Confused Deputy**

**Utekelezaji wa OAuth 2.1:**
   - **Utekelezaji wa PKCE**: Tumia Proof Key for Code Exchange (PKCE) kwa maombi yote ya awamu ya idhini
    - **Usajili wa Mteja**: Pendelea Nyaraka za Metadata ya Kitambulisho cha Mteja au
       usajili wa awali; tumia usajili wa mteja wa Dynamic uliopitwa na wakati kama
       chaguo la kurudi nyuma kwa ulinganifu tu
    - **Ridhaa Wazi**: Proxies za MCP zinazotumia Kitambulisho cha mteja wa tatu za kidume lazima
       zipate ridhaa kwa kila mteja wa MCP kabla ya kuendelea kutoa idhini
   - **Uthibitishaji wa URI wa Kuelekeza Tena**: Tekeleza uthibitishaji wa makali wa URI za mwelekeo tena na watambulishi wa wateja

**Usalama wa Proxy:**
   - Zuia kupita hatua za idhini kwa kutumia udanganyifu wa kitambulisho cha mteja kisichochafuliwa
   - Tekeleza michakato sahihi ya ridhaa kwa upatikanaji wa API za wahusika wengine
   - Fuata wizi wa msimbo wa idhini na ufikiaji usioidhinishwa wa API

## 8. **Majibu ya Tukio & Ufufuo**


**Uwezo wa Kujibu Haraka:**  

   - **Majibu Yaotomatiki**: Tekeleza mifumo ya kiotomatiki kwa mzunguko wa vyeti na kudhibiti vitisho
   - **Tarajali za Kurudisha Hali**: Uwezo wa kurudisha haraka kwenye mipangilio na vipengele vinavyojulikana kuwa salama
   - **Uwezo wa Uchunguzi**: Njia za kina za ukaguzi na kurekodi kwa uchunguzi wa matukio

**Mawasiliano & Uratibu:**
   - Taratibu wazi za kuongeza hadhi kwa matukio ya usalama
   - Uunganisho na timu za majibu ya matukio za shirika
   - Mazoezi ya mara kwa mara ya majaribio ya matukio ya usalama na mazoezi ya meza

## 9. **Uzingatiaji na Udhibiti**

**Uzingatiaji wa Sheria:**
   - Hakikisha utekelezaji wa MCP unakidhi mahitaji maalum ya sekta (GDPR, HIPAA, SOC 2)
   - Tekeleza upangaji wa data na udhibiti wa faragha kwa usindikaji wa data ya AI
   - Dumisha nyaraka kamili kwa ukaguzi wa uzingatiaji

**Usimamizi wa Mabadiliko:**
   - Mchakato rasmi wa mapitio ya usalama kwa mabadiliko yote ya mfumo wa MCP
   - Udhibiti wa toleo na mchakato wa idhini kwa mabadiliko ya mipangilio
   - Tathmini za mara kwa mara za uzingatiaji na uchambuzi wa mapungufu

## 10. **Udhibiti wa Usalama wa Juu**

**Mimilinganyo ya Kuamini Sifuri:**
   - **Kamwe Usiamini, Hakikisha Daima**: Uhakiki endelevu wa watumiaji, vifaa, na muunganisho
   - **Mgawanyiko Mdogo**: Udhibiti wa mtandao wa kina unaotenganisha vipengele vya MCP pekee
   - **Ufikiaji wa Masharti**: Udhibiti wa ufikiaji unaotegemea hatari unaobadilika kulingana na muktadha na tabia ya sasa

**Ulinzi wa Programu Endapo Inakimbia (Runtime):**
   - **Ulinzi wa Programu Endapo Inakimbia kwa Kujilinda (RASP)**: Tumia mbinu za RASP kwa kugundua vitisho kwa wakati halisi
   - **Ufuatiliaji wa Utendaji wa Programu**: Fuatilia mabadiliko ya utendaji yanayoweza kuashiria mashambulizi
   - **Sera za Usalama Zinazobadilika**: Tekeleza sera za usalama zinazobadilika kulingana na mazingira ya sasa ya vitisho

## 11. **Uunganisho wa Mazingira ya Usalama ya Microsoft**

**Usalama Kamili wa Microsoft:**
   - **Microsoft Defender kwa Cloud**: Usimamizi wa hali ya usalama wa makiwa ya MCP
   - **Azure Sentinel**: SIEM na SOAR za asili ya wingu kwa kugundua vitisho vya hali ya juu
   - **Microsoft Purview**: Udhibiti na uzingatiaji wa data kwa mchakato wa AI na vyanzo vya data

**Usimamizi wa Utambulisho na Ufikiaji:**
   - **Microsoft Entra ID**: Usimamizi wa utambulisho wa shirika kwa sera za ufikiaji wa masharti
   - **Usimamizi wa Utambulisho wa Kipekee (PIM)**: Ufikiaji wa wakati kulingana na haja na mchakato wa idhini kwa kazi za usimamizi
   - **Ulinzi wa Utambulisho**: Ufikiaji wa masharti unaotegemea hatari na majibu ya kiotomatiki kwa vitisho

## 12. **Maendeleo Endelevu ya Usalama**

**Kuwa na Habari za Hali ya Juu:**
   - **Ufuatiliaji wa Maelezo**: Mapitio ya mara kwa mara ya masasisho ya maelezo ya MCP na mabadiliko ya mwongozo wa usalama
   - **Ujasusi wa Vitisho**: Uunganisho wa chanzo maalum cha vitisho vya AI na alama za uvamizi
   - **Ushiriki wa Jamii ya Usalama**: Kushiriki kikamilifu katika jumuiya ya usalama ya MCP na programu za kufichua udhaifu

**Usalama Unaobadilika:**
   - **Usalama wa Kujifunza Mashine**: Tumia ugunduzi wa tofauti unaotegemea ML kwa kubaini mifumo mpya ya mashambulizi
   - **Uchanganuzi wa Usalama Unaotabiri**: Tekeleza mifano ya utabiri kwa utambuzi wa vitisho kwa njia ya kuchukua hatua kabla
   - **Uotomatishaji wa Usalama**: Sasisho za sera za usalama kwa njia ya kiotomatiki kulingana na taarifa za vitisho na mabadiliko ya maelezo

---

## **Rasilimali Muhimu za Usalama**

### **Nyaraka Rasmi za MCP**
- [Maelezo ya MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Mbinu Bora za Usalama za MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Maelezo ya Ruhusa za MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Rasilimali za Usalama za OWASP MCP**
- [Mwongozo wa Usalama wa OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Orodha kamili ya OWASP MCP Top 10 na utekelezaji wa Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Hatari rasmi za OWASP MCP
- [Warsha ya Mkutano wa Usalama wa MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Mafunzo ya vitendo ya usalama wa MCP kwenye Azure

### **Suluhisho za Usalama za Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Usalama wa Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Viwango vya Usalama**
- [Mbinu Bora za Usalama za OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 kwa Modeli Kubwa za Lugha](https://genai.owasp.org/)
- [NIST Mfumo wa Usimamizi wa Hatari za AI](https://www.nist.gov/itl/ai-risk-management-framework)

### **Miongozo ya Utekelezaji**
- [Mdirisha wa Uthibitishaji wa Azure API Management MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID na Server za MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Taarifa ya Usalama:** Mbinu za usalama za MCP zinabadilika kwa haraka. Kagua kila mara
> dhidi ya [maelezo ya MCP ya sasa](https://modelcontextprotocol.io/specification/2026-07-28/)
> na [nyaraka rasmi za usalama](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> kabla ya utekelezaji.

## Nini Kinachofuata

- Soma: [Udhibiti wa Usalama wa MCP](./mcp-security-controls.md)
- Rudi kwa: [Muhtasari wa Moduli ya Usalama](./README.md)
- Endelea kwa: [Moduli 3: Kuanzia](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
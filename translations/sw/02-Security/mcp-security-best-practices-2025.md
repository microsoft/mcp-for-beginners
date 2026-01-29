# MCP Mazoezi Bora ya Usalama - Sasisho la Desemba 2025

> **Muhimu**: Hati hii inaonyesha mahitaji ya usalama ya hivi karibuni ya [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) na [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) rasmi. Kila mara rejelea maelezo ya sasa kwa mwongozo wa kisasa zaidi.

## Mazoezi Muhimu ya Usalama kwa Utekelezaji wa MCP

Itifaki ya Muktadha wa Mfano inaleta changamoto za kipekee za usalama ambazo zinaenda zaidi ya usalama wa kawaida wa programu. Mazoezi haya yanashughulikia mahitaji ya msingi ya usalama na vitisho maalum vya MCP ikiwa ni pamoja na sindano ya maelekezo, sumu ya zana, wizi wa vikao, matatizo ya msaidizi mchanganyiko, na udhaifu wa kupitisha tokeni.

### **Mahitaji ya Usalama YA LAZIMU**

**Mahitaji Muhimu kutoka kwa MCP Specification:**

### **Mahitaji ya Usalama YA LAZIMU**

**Mahitaji Muhimu kutoka kwa MCP Specification:**

> **HAIFAI**: Seva za MCP **HAIFAI** kukubali tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP
> 
> **LAZIMU**: Seva za MCP zinazotekeleza idhini **LAZIMU** kuthibitisha MAOMBI yote yanayoingia
>  
> **HAIFAI**: Seva za MCP **HAIFAI** kutumia vikao kwa uthibitishaji
>
> **LAZIMU**: Seva za wakala wa MCP zinazotumia vitambulisho vya mteja vya kudumu **LAZIMU** kupata idhini ya mtumiaji kwa kila mteja aliyejiandikisha kwa nguvu

---

## 1. **Usalama wa Tokeni & Uthibitishaji**

**Udhibiti wa Uthibitishaji & Idhini:**
   - **Ukaguzi Mkali wa Idhini**: Fanya ukaguzi wa kina wa mantiki ya idhini ya seva ya MCP kuhakikisha ni watumiaji na wateja waliokusudiwa tu wanaoweza kupata rasilimali
   - **Uunganisho wa Mtoa Utambulisho wa Nje**: Tumia watoa utambulisho waliothibitishwa kama Microsoft Entra ID badala ya kutekeleza uthibitishaji wa kawaida
   - **Uthibitishaji wa Hadhira ya Tokeni**: Daima thibitisha kuwa tokeni zilitolewa wazi kwa seva yako ya MCP - kamwe usikubali tokeni za juu
   - **Mzunguko Sahihi wa Tokeni**: Tekeleza mzunguko salama wa tokeni, sera za kumalizika, na zuia mashambulizi ya kurudia tokeni

**Uhifadhi Salama wa Tokeni:**
   - Tumia Azure Key Vault au hifadhi salama za siri kwa siri zote
   - Tekeleza usimbaji fiche kwa tokeni wakati wa kuhifadhi na kusafirisha
   - Mzunguko wa mara kwa mara wa siri na ufuatiliaji wa upatikanaji usioidhinishwa

## 2. **Usimamizi wa Vikao & Usalama wa Usafirishaji**

**Mazoezi Salama ya Vikao:**
   - **Vitambulisho vya Vikao Vilivyo Salama Kivificho**: Tumia vitambulisho vya vikao visivyo na utabiri vilivyotengenezwa kwa jenereta salama za nambari za nasibu
   - **Ufungaji wa Mtumiaji Mmoja kwa Moja**: Funga vitambulisho vya vikao kwa utambulisho wa mtumiaji kwa kutumia muundo kama `<user_id>:<session_id>` ili kuzuia matumizi mabaya ya vikao kwa watumiaji wengine
   - **Usimamizi wa Mzunguko wa Vikao**: Tekeleza kumalizika, mzunguko, na kuharibu vikao ipasavyo ili kupunguza madirisha ya udhaifu
   - **Utekelezaji wa HTTPS/TLS**: HTTPS ni lazima kwa mawasiliano yote ili kuzuia wizi wa vitambulisho vya vikao

**Usalama wa Tabaka la Usafirishaji:**
   - Sanidi TLS 1.3 inapowezekana kwa usimamizi sahihi wa vyeti
   - Tekeleza kuweka pini ya vyeti kwa muunganisho muhimu
   - Mzunguko wa mara kwa mara wa vyeti na uhakiki wa uhalali

## 3. **Ulinzi wa Vitisho Maalum vya AI** 🤖

**Ulinzi dhidi ya Sindano ya Maelekezo:**
   - **Microsoft Prompt Shields**: Tumia AI Prompt Shields kwa kugundua na kuchuja maagizo mabaya kwa kiwango cha juu
   - **Usafishaji wa Ingizo**: Thibitisha na safisha ingizo zote ili kuzuia mashambulizi ya sindano na matatizo ya msaidizi mchanganyiko
   - **Mipaka ya Maudhui**: Tumia mfumo wa alama na alama za data kutofautisha maagizo ya kuaminika na maudhui ya nje

**Kuzuia Sumu ya Zana:**
   - **Uthibitishaji wa Metadata ya Zana**: Tekeleza ukaguzi wa uadilifu kwa maelezo ya zana na fuatilia mabadiliko yasiyotarajiwa
   - **Ufuatiliaji wa Zana kwa Muda wa Uendeshaji**: Fuatilia tabia za wakati wa uendeshaji na weka tahadhari kwa mifumo isiyotegemewa ya utekelezaji
   - **Mchakato wa Idhini**: Hitaji idhini wazi ya mtumiaji kwa mabadiliko ya zana na uwezo

## 4. **Udhibiti wa Upatikanaji & Ruhusa**

**Kanuni ya Ruhusa Ndogo Zaidi:**
   - Toa seva za MCP ruhusa za chini kabisa zinazohitajika kwa utendaji uliokusudiwa
   - Tekeleza udhibiti wa upatikanaji kwa misingi ya majukumu (RBAC) na ruhusa za kina
   - Ukaguzi wa mara kwa mara wa ruhusa na ufuatiliaji endelevu wa kuongezeka kwa ruhusa

**Udhibiti wa Ruhusa Wakati wa Uendeshaji:**
   - Weka mipaka ya rasilimali kuzuia mashambulizi ya uchakavu wa rasilimali
   - Tumia upunguzaji wa kontena kwa mazingira ya utekelezaji wa zana  
   - Tekeleza upatikanaji wa wakati muafaka kwa kazi za usimamizi

## 5. **Usalama wa Maudhui & Ufuatiliaji**

**Utekelezaji wa Usalama wa Maudhui:**
   - **Uunganisho wa Azure Content Safety**: Tumia Azure Content Safety kugundua maudhui hatari, jaribio la kuvunja mfumo, na ukiukaji wa sera
   - **Uchambuzi wa Tabia**: Tekeleza ufuatiliaji wa tabia wakati wa uendeshaji kugundua kasoro katika seva ya MCP na utekelezaji wa zana
   - **Kumbukumbu Kamili**: Rekodi majaribio yote ya uthibitishaji, kuitwa kwa zana, na matukio ya usalama kwa uhifadhi salama usioweza kubadilishwa

**Ufuatiliaji Endelevu:**
   - Tahadhari za wakati halisi kwa mifumo ya kutiliwa shaka na majaribio ya upatikanaji usioidhinishwa  
   - Uunganisho na mifumo ya SIEM kwa usimamizi wa matukio ya usalama kwa makao makuu
   - Ukaguzi wa mara kwa mara wa usalama na upimaji wa uvamizi wa utekelezaji wa MCP

## 6. **Usalama wa Mnyororo wa Ugavi**

**Uthibitishaji wa Vipengele:**
   - **Uchunguzi wa Mtegemeo**: Tumia uchunguzi wa kiotomatiki wa udhaifu kwa vyanzo vyote vya programu na vipengele vya AI
   - **Uthibitishaji wa Asili**: Thibitisha asili, leseni, na uadilifu wa mifano, vyanzo vya data, na huduma za nje
   - **Pakiti Zilizotiwa Sahihi**: Tumia pakiti zilizosainiwa kwa kificho na thibitisha sahihi kabla ya usambazaji

**Mtiririko Salama wa Maendeleo:**
   - **Usalama wa Juu wa GitHub**: Tekeleza uchunguzi wa siri, uchambuzi wa utegemezi, na uchambuzi wa CodeQL wa msimbo usiobadilika
   - **Usalama wa CI/CD**: Unganisha uthibitishaji wa usalama katika mitiririko ya usambazaji wa kiotomatiki
   - **Uadilifu wa Vifaa**: Tekeleza uthibitishaji wa kificho kwa vifaa na usanidi uliosambazwa

## 7. **Usalama wa OAuth & Kuzuia Msaidizi Mchanganyiko**

**Utekelezaji wa OAuth 2.1:**
   - **Utekelezaji wa PKCE**: Tumia Proof Key for Code Exchange (PKCE) kwa maombi yote ya idhini
   - **Idhini Wazi**: Pata idhini ya mtumiaji kwa kila mteja aliyejiandikisha kwa nguvu kuzuia mashambulizi ya msaidizi mchanganyiko
   - **Uthibitishaji wa URI ya Kuongoza**: Tekeleza uthibitishaji mkali wa URI za kuongoza na vitambulisho vya mteja

**Usalama wa Wakala:**
   - Zuia kupita idhini kupitia matumizi mabaya ya kitambulisho cha mteja cha kudumu
   - Tekeleza michakato sahihi ya idhini kwa upatikanaji wa API wa wahusika wa tatu
   - Fuatilia wizi wa msimbo wa idhini na upatikanaji usioidhinishwa wa API

## 8. **Majibu ya Tukio & Urejeshaji**

**Uwezo wa Majibu ya Haraka:**
   - **Majibu ya Kiotomatiki**: Tekeleza mifumo ya kiotomatiki kwa mzunguko wa siri na udhibiti wa vitisho
   - **Taratibu za Kurudisha**: Uwezo wa kurudisha haraka usanidi na vipengele vilivyojulikana kuwa salama
   - **Uwezo wa Uchunguzi wa Kiforensiki**: Mifumo ya kina ya ukaguzi na kumbukumbu kwa uchunguzi wa matukio

**Mawasiliano & Uratibu:**
   - Taratibu wazi za kuongezeka kwa kiwango cha matukio ya usalama
   - Uunganisho na timu za majibu ya matukio za shirika
   - Mazoezi ya mara kwa mara ya majaribio ya matukio ya usalama na mazoezi ya meza

## 9. **Uzingatiaji wa Sheria & Usimamizi**

**Uzingatiaji wa Kanuni:**
   - Hakikisha utekelezaji wa MCP unakidhi mahitaji maalum ya sekta (GDPR, HIPAA, SOC 2)
   - Tekeleza upangaji wa data na udhibiti wa faragha kwa usindikaji wa data za AI
   - Dumisha nyaraka kamili kwa ukaguzi wa uzingatiaji

**Usimamizi wa Mabadiliko:**
   - Taratibu rasmi za ukaguzi wa usalama kwa mabadiliko yote ya mfumo wa MCP
   - Udhibiti wa matoleo na michakato ya idhini kwa mabadiliko ya usanidi
   - Tathmini za mara kwa mara za uzingatiaji na uchambuzi wa mapungufu

## 10. **Udhibiti wa Usalama wa Juu**

**Msingi wa Kuamini Sifuri:**
   - **Kamwe Usiamini, Daima Thibitisha**: Thibitisho endelevu wa watumiaji, vifaa, na muunganisho
   - **Ugawaji Mdogo wa Mtandao**: Udhibiti wa mtandao wa kina unaotenganisha vipengele vya MCP binafsi
   - **Upatikanaji wa Masharti**: Udhibiti wa upatikanaji unaotegemea hatari unaobadilika kulingana na muktadha na tabia ya sasa

**Ulinzi wa Programu Wakati wa Uendeshaji:**
   - **Ulinzi wa Programu Wakati wa Uendeshaji (RASP)**: Tumia mbinu za RASP kwa kugundua vitisho kwa wakati halisi
   - **Ufuatiliaji wa Utendaji wa Programu**: Fuatilia kasoro za utendaji zinazoweza kuashiria mashambulizi
   - **Sera za Usalama Zinazobadilika**: Tekeleza sera za usalama zinazobadilika kulingana na mazingira ya vitisho vya sasa

## 11. **Uunganisho wa Mfumo wa Usalama wa Microsoft**

**Usalama Kamili wa Microsoft:**
   - **Microsoft Defender for Cloud**: Usimamizi wa hali ya usalama wa wingu kwa mzigo wa kazi wa MCP
   - **Azure Sentinel**: SIEM na SOAR asili za wingu kwa kugundua vitisho vya hali ya juu
   - **Microsoft Purview**: Usimamizi wa data na uzingatiaji kwa mtiririko wa AI na vyanzo vya data

**Usimamizi wa Utambulisho & Upatikanaji:**
   - **Microsoft Entra ID**: Usimamizi wa utambulisho wa shirika na sera za upatikanaji wa masharti
   - **Usimamizi wa Utambulisho wa Wenye Haki (PIM)**: Upatikanaji wa wakati muafaka na michakato ya idhini kwa kazi za usimamizi
   - **Ulinzi wa Utambulisho**: Upatikanaji wa masharti unaotegemea hatari na majibu ya vitisho ya kiotomatiki

## 12. **Mageuzi Endelevu ya Usalama**

**Kuwa wa Kisasa:**
   - **Ufuatiliaji wa Maelezo**: Mapitio ya mara kwa mara ya sasisho za maelezo ya MCP na mabadiliko ya mwongozo wa usalama
   - **Ujasusi wa Vitisho**: Uunganisho wa vyanzo vya vitisho vya AI na viashiria vya uvamizi
   - **Ushiriki wa Jamii ya Usalama**: Ushiriki hai katika jamii ya usalama ya MCP na programu za kufichua udhaifu

**Usalama Unaobadilika:**
   - **Usalama wa Kujifunza kwa Mashine**: Tumia kugundua kasoro kwa kutumia ML kwa kutambua mifumo mipya ya mashambulizi
   - **Uchanganuzi wa Usalama wa Utabiri**: Tekeleza mifano ya utabiri kwa utambuzi wa vitisho vya mapema
   - **Uendeshaji wa Usalama wa Kiotomatiki**: Sasisho za sera za usalama kwa kiotomatiki kulingana na ujasusi wa vitisho na mabadiliko ya maelezo

---

## **Rasilimali Muhimu za Usalama**

### **Nyaraka Rasmi za MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Suluhisho za Usalama za Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Viwango vya Usalama**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Mwongozo wa Utekelezaji**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Taarifa ya Usalama**: Mazoezi ya usalama ya MCP hubadilika kwa kasi. Kila mara thibitisha dhidi ya [maelezo ya MCP ya sasa](https://spec.modelcontextprotocol.io/) na [nyaraka rasmi za usalama](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) kabla ya utekelezaji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuna wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Mazoezi Bora ya Usalama 2025

Mwongozo huu kamili unaelezea mazoezi muhimu bora ya usalama kwa kutekeleza mifumo ya Model Context Protocol (MCP) kulingana na **MCP Specification 2025-11-25** ya hivi karibuni na viwango vya sasa vya sekta. Mazoezi haya yanashughulikia masuala ya usalama ya jadi pamoja na vitisho maalum vya AI vinavyotokana na utekelezaji wa MCP.

## Mahitaji Muhimu ya Usalama

### Udhibiti wa Usalama wa Lazima (Mahitaji YAWEKE)

1. **Uthibitishaji wa Tokeni**: Seva za MCP **HAZITAKUBALI** tokeni zozote ambazo hazikutolewa wazi kwa seva ya MCP yenyewe  
2. **Uthibitishaji wa Idhini**: Seva za MCP zinazotekeleza idhini **ZITATHIBITISHA** MAOMBI YOTE yanayoingia na **HAZITUMII** vikao kwa uthibitishaji  
3. **Idhini ya Mtumiaji**: Seva za wakala wa MCP zinazotumia vitambulisho vya wateja vya kudumu **ZITAPATA** idhini wazi ya mtumiaji kwa kila mteja aliyejiandikisha kwa nguvu  
4. **Vitambulisho Salama vya Vikao**: Seva za MCP **ZITUMIE** vitambulisho vya vikao visivyo na utabiri vilivyotengenezwa kwa njia salama za nambari za nasibu

## Mazoezi Msingi ya Usalama

### 1. Uthibitishaji na Usafishaji wa Ingizo
- **Uthibitishaji Kamili wa Ingizo**: Thibitisha na safisha ingizo zote ili kuzuia mashambulizi ya sindano, matatizo ya confused deputy, na udhaifu wa sindano za maelekezo  
- **Utekelezaji wa Mipangilio ya Vigezo**: Tekeleza uthibitishaji mkali wa muundo wa JSON kwa vigezo vyote vya zana na ingizo za API  
- **Uchujaji wa Maudhui**: Tumia Microsoft Prompt Shields na Azure Content Safety kuchuja maudhui hatarishi katika maelekezo na majibu  
- **Usafishaji wa Matokeo**: Thibitisha na safisha matokeo yote ya modeli kabla ya kuwasilisha kwa watumiaji au mifumo inayofuata

### 2. Ubora wa Uthibitishaji na Idhini  
- **Watoa Utambulisho wa Nje**: Wekeza uthibitishaji kwa watoa utambulisho walioko (Microsoft Entra ID, watoa huduma wa OAuth 2.1) badala ya kutekeleza uthibitishaji wa kawaida  
- **Ruhusa za Kina**: Tekeleza ruhusa za kina, maalum kwa zana, kwa kufuata kanuni ya udogo wa ruhusa  
- **Usimamizi wa Mzunguko wa Tokeni**: Tumia tokeni za muda mfupi zenye mzunguko salama na uthibitishaji sahihi wa hadhira  
- **Uthibitishaji wa Vipengele Vingi**: Hitaji MFA kwa upatikanaji wote wa kiutawala na shughuli nyeti

### 3. Itifaki Salama za Mawasiliano
- **Usalama wa Tabaka la Usafirishaji**: Tumia HTTPS/TLS 1.3 kwa mawasiliano yote ya MCP na uthibitishaji sahihi wa vyeti  
- **Usimbaji wa Mwisho kwa Mwisho**: Tekeleza tabaka za ziada za usimbaji kwa data nyeti sana wakati wa kusafirishwa na kuhifadhiwa  
- **Usimamizi wa Vyeti**: Dumisha usimamizi sahihi wa mzunguko wa vyeti kwa michakato ya upya kiotomatiki  
- **Utekelezaji wa Toleo la Itifaki**: Tumia toleo la sasa la itifaki ya MCP (2025-11-25) kwa mazungumzo sahihi ya toleo

### 4. Kuzuia Kasi na Ulinzi wa Rasilimali wa Juu
- **Kuzuia Kasi kwa Tabaka Nyingi**: Tekeleza kuzuia kasi kwa watumiaji, vikao, zana, na viwango vya rasilimali ili kuzuia matumizi mabaya  
- **Kuzuia Kasi Inayobadilika**: Tumia kuzuia kasi kwa kutumia mashine kujifunza inayobadilika kulingana na mifumo ya matumizi na viashiria vya vitisho  
- **Usimamizi wa Kiasi cha Rasilimali**: Weka mipaka inayofaa kwa rasilimali za kompyuta, matumizi ya kumbukumbu, na muda wa utekelezaji  
- **Ulinzi wa DDoS**: Tekeleza ulinzi kamili wa DDoS na mifumo ya uchambuzi wa trafiki

### 5. Kumbukumbu na Ufuatiliaji Kamili
- **Kumbukumbu za Ukaguzi Zenye Muundo**: Tekeleza kumbukumbu za kina, zinazoweza kutafutwa kwa shughuli zote za MCP, utekelezaji wa zana, na matukio ya usalama  
- **Ufuatiliaji wa Usalama wa Wakati Halisi**: Tekeleza mifumo ya SIEM yenye utambuzi wa kasoro kwa nguvu za AI kwa mzigo wa MCP  
- **Kumbukumbu Zinazoheshimu Faragha**: Rekodi matukio ya usalama huku ukiheshimu mahitaji na kanuni za faragha ya data  
- **Uunganisho wa Majibu ya Matukio**: Unganisha mifumo ya kumbukumbu na michakato ya majibu ya matukio kiotomatiki

### 6. Mazoezi Bora ya Uhifadhi Salama
- **Moduli za Usalama wa Vifaa**: Tumia uhifadhi wa funguo unaotegemea HSM (Azure Key Vault, AWS CloudHSM) kwa shughuli muhimu za usimbaji  
- **Usimamizi wa Funguo za Usimbaji**: Tekeleza mzunguko sahihi wa funguo, mgawanyiko, na udhibiti wa upatikanaji wa funguo za usimbaji  
- **Usimamizi wa Siri**: Hifadhi funguo zote za API, tokeni, na nyaraka katika mifumo maalum ya usimamizi wa siri  
- **Uainishaji wa Data**: Aina data kulingana na viwango vya unyeti na tumia hatua zinazofaa za ulinzi

### 7. Usimamizi wa Tokeni wa Juu
- **Kuzuia Kupitisha Tokeni**: Zuia wazi mifumo ya kupitisha tokeni inayopitisha udhibiti wa usalama  
- **Uthibitishaji wa Hadhira**: Daima thibitisha madai ya hadhira ya tokeni yanayolingana na utambulisho wa seva ya MCP inayokusudiwa  
- **Idhini Inayotegemea Madai**: Tekeleza idhini ya kina inayotegemea madai ya tokeni na sifa za mtumiaji  
- **Ufungaji wa Tokeni**: Funga tokeni kwa vikao maalum, watumiaji, au vifaa inapofaa

### 8. Usimamizi Salama wa Vikao
- **Vitambulisho vya Vikao vya Usimbaji**: Tengeneza vitambulisho vya vikao kwa kutumia jenereta za nambari za nasibu zilizo salama kisimbaji (sio mfululizo unaoweza kutabirika)  
- **Ufungaji Maalum kwa Mtumiaji**: Funga vitambulisho vya vikao kwa taarifa maalum za mtumiaji kwa kutumia miundo salama kama `<user_id>:<session_id>`  
- **Udhibiti wa Mzunguko wa Vikao**: Tekeleza kumalizika, mzunguko, na mbinu za kuharibu vikao kwa usahihi  
- **Vichwa vya Usalama vya Vikao**: Tumia vichwa vya usalama vya HTTP vinavyofaa kwa ulinzi wa vikao

### 9. Udhibiti wa Usalama Maalum kwa AI
- **Ulinzi wa Sindano za Maelekezo**: Tekeleza Microsoft Prompt Shields zenye spotlighting, delimiters, na mbinu za datamarking  
- **Kuzuia Uchafuzi wa Zana**: Thibitisha metadata ya zana, fuatilia mabadiliko ya nguvu, na thibitisha uadilifu wa zana  
- **Uthibitishaji wa Matokeo ya Modeli**: Chunguza matokeo ya modeli kwa uwezekano wa kuvuja data, maudhui hatarishi, au ukiukaji wa sera za usalama  
- **Ulinzi wa Dirisha la Muktadha**: Tekeleza udhibiti wa kuzuia uchafuzi na mashambulizi ya udanganyifu wa dirisha la muktadha

### 10. Usalama wa Utekelezaji wa Zana
- **Utekelezaji wa Sandboxing**: Endesha utekelezaji wa zana katika mazingira yaliyotengwa na yaliyofungashwa yenye mipaka ya rasilimali  
- **Mgawanyiko wa Haki**: Endesha zana kwa ruhusa ndogo zinazohitajika na akaunti za huduma zilizotengwa  
- **Kutengwa kwa Mtandao**: Tekeleza mgawanyiko wa mtandao kwa mazingira ya utekelezaji wa zana  
- **Ufuatiliaji wa Utekelezaji**: Fuata utekelezaji wa zana kwa tabia zisizo za kawaida, matumizi ya rasilimali, na ukiukaji wa usalama

### 11. Uthibitishaji Endelevu wa Usalama
- **Upimaji wa Usalama Kiotomatiki**: Unganisha upimaji wa usalama katika mistari ya CI/CD kwa zana kama GitHub Advanced Security  
- **Usimamizi wa Udhaifu**: Chunguza mara kwa mara utegemezi wote, ikiwa ni pamoja na modeli za AI na huduma za nje  
- **Upimaji wa Uvunjaji**: Fanya tathmini za usalama mara kwa mara zinazolenga utekelezaji wa MCP  
- **Mapitio ya Msimbo wa Usalama**: Tekeleza mapitio ya lazima ya usalama kwa mabadiliko yote ya msimbo yanayohusiana na MCP

### 12. Usalama wa Mnyororo wa Ugavi kwa AI
- **Uthibitishaji wa Vipengele**: Thibitisha asili, uadilifu, na usalama wa vipengele vyote vya AI (modeli, embeddings, API)  
- **Usimamizi wa Utegemezi**: Dumisha orodha za sasa za programu na utegemezi wa AI zenye ufuatiliaji wa udhaifu  
- **Hifadhi Zinazoaminika**: Tumia vyanzo vilivyothibitishwa na kuaminika kwa modeli zote za AI, maktaba, na zana  
- **Ufuatiliaji wa Mnyororo wa Ugavi**: Fuata kwa karibu kwa mabadiliko katika watoa huduma za AI na hifadhi za modeli

## Mifumo ya Usalama ya Juu

### Miundo ya Zero Trust kwa MCP
- **Usiamini Kamwe, Thibitisha Daima**: Tekeleza uthibitishaji endelevu kwa washiriki wote wa MCP  
- **Mgawanyiko Mdogo**: Tengeneza vipengele vya MCP kwa udhibiti wa mtandao na utambulisho wa kina  
- **Upatikanaji wa Masharti**: Tekeleza udhibiti wa upatikanaji unaotegemea hatari unaobadilika kulingana na muktadha na tabia  
- **Tathmini Endelevu ya Hatari**: Tathmini hali ya usalama kwa nguvu kulingana na viashiria vya vitisho vya sasa

### Utekelezaji wa AI Unaohifadhi Faragha
- **Kupunguza Data**: Onyesha data kidogo tu inayohitajika kwa kila shughuli ya MCP  
- **Faragha ya Tofauti**: Tekeleza mbinu za kuhifadhi faragha kwa usindikaji wa data nyeti  
- **Usimbaji wa Homomorphic**: Tumia mbinu za usimbaji wa hali ya juu kwa hesabu salama kwenye data iliyosimbwa  
- **Mafunzo ya Pamoja**: Tekeleza mbinu za mafunzo ya usambazaji zinazohifadhi eneo na faragha ya data

### Majibu ya Matukio kwa Mifumo ya AI
- **Tarifisho Maalum za Matukio ya AI**: Tengeneza taratibu za majibu ya matukio zinazolenga vitisho vya AI na MCP  
- **Majibu Kiotomatiki**: Tekeleza udhibiti na urejeshaji wa kiotomatiki kwa matukio ya kawaida ya usalama ya AI  
- **Uwezo wa Uchunguzi**: Dumisha maandalizi ya uchunguzi kwa uvunjaji wa mifumo ya AI na uvujaji wa data  
- **Taratibu za Urejeshaji**: Weka taratibu za kurejesha kutokana na uchafuzi wa modeli za AI, mashambulizi ya sindano za maelekezo, na uvunjaji wa huduma

## Rasilimali za Utekelezaji & Viwango

### Nyaraka Rasmi za MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Maelezo ya sasa ya itifaki ya MCP  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Mwongozo rasmi wa usalama  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Mifumo ya uthibitishaji na idhini  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Mahitaji ya usalama wa tabaka la usafirishaji

### Suluhisho za Usalama za Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Ulinzi wa hali ya juu wa sindano za maelekezo  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Uchujaji kamili wa maudhui ya AI  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Usimamizi wa utambulisho na upatikanaji wa biashara  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Usimamizi salama wa siri na nyaraka  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Uchunguzi wa usalama wa mnyororo wa ugavi na msimbo

### Viwango na Mifumo ya Usalama
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Mwongozo wa usalama wa OAuth wa sasa  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Hatari za usalama wa programu za wavuti  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Hatari za usalama maalum kwa AI  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Usimamizi kamili wa hatari za AI  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Mifumo ya usimamizi wa usalama wa taarifa

### Mwongozo wa Utekelezaji & Mafunzo
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Mifumo ya uthibitishaji wa biashara  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Uunganisho wa mtoa utambulisho  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Mazoezi bora ya usimamizi wa tokeni  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Mifumo ya usimbaji wa hali ya juu

### Rasilimali za Usalama za Juu
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Mazoezi ya maendeleo salama  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Upimaji wa usalama maalum kwa AI  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Mbinu za mfano wa vitisho vya AI  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Mbinu za AI zinazohifadhi faragha

### Uzingatiaji na Utawala
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Uzingatiaji wa faragha katika mifumo ya AI  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Utekelezaji wa AI yenye uwajibikaji  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Udhibiti wa usalama kwa watoa huduma za AI  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Mahitaji ya uzingatiaji wa AI katika huduma za afya

### DevSecOps & Uendeshaji Kiotomatiki
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Mistari salama ya maendeleo ya AI  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Uthibitishaji endelevu wa usalama  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Utekelezaji salama wa miundombinu  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Usalama wa kontena za mzigo wa AI

### Ufuatiliaji & Majibu ya Matukio  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Suluhisho kamili za ufuatiliaji  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Taratibu maalum za majibu ya matukio ya AI  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Usimamizi wa taarifa na matukio ya usalama  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Vyanzo vya taarifa za vitisho vya AI

## 🔄 Uboreshaji Endelevu

### Kuwa Mjuzi na Viwango Vinavyobadilika
- **Mabadiliko ya MCP Specification**: Fuata mabadiliko rasmi ya maelezo ya MCP na tahadhari za usalama  
- **Taarifa za Vitisho**: Jiandikishe kwa vyanzo vya taarifa za vitisho vya usalama wa AI na hifadhidata za udhaifu  
- **Ushiriki wa Jamii**: Shiriki katika mijadala ya jamii ya usalama ya MCP na makundi ya kazi  
- **Tathmini za Mara kwa Mara**: Fanya tathmini za hali ya usalama kila robo mwaka na sasisha mazoezi ipasavyo

### Kuchangia Usalama wa MCP
- **Utafiti wa Usalama**: Changia katika utafiti wa usalama wa MCP na programu za kufichua udhaifu  
- **Kushirikiana kwa Mazoezi Bora**: Shiriki utekelezaji wa usalama na masomo yaliyopatikana na jamii
- **Maendeleo ya Kawaida**: Shirikiana katika maendeleo ya vipimo vya MCP na uundaji wa viwango vya usalama  
- **Maendeleo ya Zana**: Tengeneza na shiriki zana na maktaba za usalama kwa mfumo wa MCP  

---

*Hati hii inaonyesha mbinu bora za usalama za MCP kufikia Desemba 18, 2025, kulingana na Vipimo vya MCP 2025-11-25. Mbinu za usalama zinapaswa kukaguliwa na kusasishwa mara kwa mara kadri itakavyobadilika itifaki na mazingira ya vitisho.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Msamaha**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
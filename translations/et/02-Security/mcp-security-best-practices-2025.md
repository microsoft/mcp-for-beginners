# MCP turvalisuse parimad tavad - detsember 2025 uuendus

> **Tähtis**: See dokument kajastab uusimaid [MCP spetsifikatsiooni 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) turvanõudeid ja ametlikke [MCP turvalisuse parimaid tavasid](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Järgige alati kehtivat spetsifikatsiooni, et saada kõige ajakohasemat juhendit.

## MCP rakenduste olulised turvapraktikad

Model Context Protocol toob kaasa unikaalseid turvalisuse väljakutseid, mis ulatuvad traditsioonilisest tarkvaraturvalisusest kaugemale. Need tavad käsitlevad nii põhilisi turvanõudeid kui ka MCP-spetsiifilisi ohte, sealhulgas promptide süstimist, tööriistade mürgitamist, sessiooni kaaperdamist, segaduses esindaja probleeme ja tokeni läbipääsu haavatavusi.

### **KOHUSTUSLIKUD turvanõuded**

**Olulised nõuded MCP spetsifikatsioonist:**

### **KOHUSTUSLIKUD turvanõuded**

**Olulised nõuded MCP spetsifikatsioonist:**

> **EI TOHI**: MCP serverid **EI TOHI** vastu võtta ühtegi tokenit, mis ei ole selgesõnaliselt MCP serverile väljastatud  
>  
> **PEAB**: MCP serverid, mis rakendavad autoriseerimist, **PEAVAD** kontrollima KÕIKI sissetulevaid päringuid  
>  
> **EI TOHI**: MCP serverid **EI TOHI** kasutada sessioone autentimiseks  
>  
> **PEAB**: MCP proxy serverid, mis kasutavad staatilisi kliendi ID-sid, **PEAVAD** saama kasutaja nõusoleku iga dünaamiliselt registreeritud kliendi jaoks

---

## 1. **Tokeni turvalisus ja autentimine**

**Autentimise ja autoriseerimise kontrollid:**  
   - **Range autoriseerimise ülevaatus**: Tehke põhjalikke auditeid MCP serveri autoriseerimisloogikas, et tagada ligipääs ainult kavandatud kasutajatele ja klientidele  
   - **Välise identiteedipakkuja integreerimine**: Kasutage tuntud identiteedipakkujaid nagu Microsoft Entra ID, mitte kohandatud autentimise rakendamist  
   - **Tokeni sihtrühma valideerimine**: Kontrollige alati, et tokenid oleksid selgesõnaliselt teie MCP serverile väljastatud – ärge kunagi aktsepteerige ülemisi tokeneid  
   - **Õige tokeni elutsükkel**: Rakendage turvalist tokeni rotatsiooni, aegumispoliitikaid ja vältige tokeni korduvkasutuse rünnakuid

**Kaitstud tokeni salvestus:**  
   - Kasutage kõigi saladuste jaoks Azure Key Vaulti või sarnaseid turvalisi volituste hoidlaid  
   - Rakendage tokenite krüpteerimist nii puhkeolekus kui ka edastamisel  
   - Regulaarne volituste rotatsioon ja volitamata juurdepääsu jälgimine

## 2. **Sessioonihaldus ja transporditurvalisus**

**Turvalised sessioonipraktikad:**  
   - **Krüptograafiliselt turvalised sessiooni ID-d**: Kasutage turvalisi, mitte-deterministlikke sessiooni ID-sid, mis on genereeritud turvaliste juhuslike arvude generaatoritega  
   - **Kasutajapõhine sidumine**: Siduge sessiooni ID-d kasutaja identiteediga vormingus `<user_id>:<session_id>`, et vältida sessioonide väärkasutust kasutajate vahel  
   - **Sessiooni elutsükli haldus**: Rakendage õiget aegumist, rotatsiooni ja tühistamist, et piirata haavatavuse aken  
   - **HTTPS/TLS nõue**: Kõik suhtlus peab toimuma HTTPS kaudu, et vältida sessiooni ID vargust

**Transpordikihi turvalisus:**  
   - Konfigureerige TLS 1.3 võimalusel koos nõuetekohase sertifikaadi haldusega  
   - Rakendage sertifikaadi kinnitamist (pinning) kriitiliste ühenduste jaoks  
   - Regulaarne sertifikaadi rotatsioon ja kehtivuse kontroll

## 3. **AI-spetsiifiline ohtude kaitse** 🤖

**Promptide süstimise kaitse:**  
   - **Microsoft Prompt Shields**: Kasutage AI Prompt Shields tehnoloogiat pahatahtlike juhiste tuvastamiseks ja filtreerimiseks  
   - **Sisendi puhastamine**: Kontrollige ja puhastage kõik sisendid, et vältida süstimisrünnakuid ja segaduses esindaja probleeme  
   - **Sisu piirid**: Kasutage eraldajaid ja andmemärgistussüsteeme, et eristada usaldusväärseid juhiseid välisest sisust

**Tööriistade mürgitamise ennetamine:**  
   - **Tööriista metaandmete valideerimine**: Rakendage terviklikkuse kontrollid tööriistade definitsioonidele ja jälgige ootamatuid muudatusi  
   - **Dünaamiline tööriistade jälgimine**: Jälgige tööriistade käitumist reaalajas ja seadistage hoiatused ootamatute täitmismustrite korral  
   - **Kinnituse töövood**: Nõudke kasutaja selgesõnalist kinnitust tööriistade muudatuste ja võimekuse muutuste jaoks

## 4. **Ligipääsukontroll ja õigused**

**Vähima privileegi põhimõte:**  
   - Andke MCP serveritele ainult minimaalsed õigused, mis on vajalikud kavandatud funktsionaalsuseks  
   - Rakendage rollipõhist ligipääsukontrolli (RBAC) peenhäälestatud õigustega  
   - Regulaarne õiguste ülevaatus ja pidev jälgimine privileegide eskalatsiooni vältimiseks

**Käivitusaja õiguste kontroll:**  
   - Rakendage ressursipiiranguid, et vältida ressursi ammendamise rünnakuid  
   - Kasutage konteinerite isolatsiooni tööriistade täitmise keskkondades  
   - Rakendage just-in-time ligipääsu haldusfunktsioonide jaoks

## 5. **Sisu turvalisus ja jälgimine**

**Sisu turvalisuse rakendamine:**  
   - **Azure Content Safety integreerimine**: Kasutage Azure Content Safety teenust kahjuliku sisu, jailbreak-katsete ja poliitikavigade tuvastamiseks  
   - **Käitumuslik analüüs**: Rakendage käivitusaegset käitumise jälgimist MCP serveri ja tööriistade täitmise anomaaliate tuvastamiseks  
   - **Põhjalik logimine**: Logige kõik autentimiskatsed, tööriistade kutsed ja turvasündmused turvalisse, muutmatusse salvestusse

**Pidev jälgimine:**  
   - Reaalajas hoiatused kahtlaste mustrite ja volitamata juurdepääsu katsete korral  
   - Integreerimine SIEM süsteemidega tsentraliseeritud turvasündmuste halduseks  
   - Regulaarne turvaaudit ja MCP rakenduste läbipääsu testimine

## 6. **Tarneahela turvalisus**

**Komponentide kontroll:**  
   - **Sõltuvuste skaneerimine**: Kasutage automatiseeritud haavatavuste skaneerimist kõigi tarkvarasõltuvuste ja AI komponentide jaoks  
   - **Päritolu valideerimine**: Kontrollige mudelite, andmeallikate ja väliste teenuste päritolu, litsentsi ja terviklikkust  
   - **Allkirjastatud paketid**: Kasutage krüptograafiliselt allkirjastatud pakette ja kontrollige allkirju enne juurutamist

**Turvaline arendusliin:**  
   - **GitHub Advanced Security**: Rakendage saladuste skaneerimist, sõltuvuste analüüsi ja CodeQL staatilist analüüsi  
   - **CI/CD turvalisus**: Integreerige turvakontrollid kogu automatiseeritud juurutusliini jooksul  
   - **Artefaktide terviklikkus**: Rakendage krüptograafilist kontrolli juurutatud artefaktide ja konfiguratsioonide jaoks

## 7. **OAuth turvalisus ja segaduses esindaja ennetamine**

**OAuth 2.1 rakendamine:**  
   - **PKCE rakendamine**: Kasutage Proof Key for Code Exchange (PKCE) kõigi autoriseerimispäringute jaoks  
   - **Selgesõnaline nõusolek**: Saage kasutaja nõusolek iga dünaamiliselt registreeritud kliendi jaoks, et vältida segaduses esindaja rünnakuid  
   - **Redirect URI valideerimine**: Rakendage ranget redirect URI ja kliendi identifikaatorite valideerimist

**Proxy turvalisus:**  
   - Takistage autoriseerimise möödaviimist staatiliste kliendi ID-de ärakasutamise kaudu  
   - Rakendage nõuetekohased nõusoleku töövood kolmandate osapoolte API ligipääsuks  
   - Jälgige autoriseerimiskoodi vargust ja volitamata API ligipääsu

## 8. **Intsidendile reageerimine ja taastumine**

**Kiired reageerimisvõimalused:**  
   - **Automatiseeritud reageerimine**: Rakendage automatiseeritud süsteeme volituste rotatsiooniks ja ohtude piiramiseks  
   - **Tagasipööramise protseduurid**: Võime kiiresti taastada teada-töötavad konfiguratsioonid ja komponendid  
   - **Forensika võimalused**: Põhjalikud auditeerimisrajad ja logimine intsidentide uurimiseks

**Kommunikatsioon ja koordineerimine:**  
   - Selged eskalatsiooniprotseduurid turvaintsidentide korral  
   - Integreerimine organisatsiooni intsidentidele reageerimise meeskondadega  
   - Regulaarne turvaintsidentide simulatsioon ja lauamängu harjutused

## 9. **Vastavus ja haldus**

**Regulatiivne vastavus:**  
   - Tagage, et MCP rakendused vastavad tööstusharu spetsiifilistele nõuetele (GDPR, HIPAA, SOC 2)  
   - Rakendage andmete klassifitseerimist ja privaatsuskontrolle AI andmetöötluseks  
   - Hoidke põhjalikku dokumentatsiooni vastavusauditiks

**Muudatuste haldus:**  
   - Formaalsed turvaülevaatusprotsessid kõigi MCP süsteemi muudatuste jaoks  
   - Versioonihaldus ja kinnitustöövood konfiguratsioonimuudatuste jaoks  
   - Regulaarne vastavuse hindamine ja lõheanalüüs

## 10. **Täiustatud turvakontrollid**

**Zero Trust arhitektuur:**  
   - **Ärge kunagi usaldage, kontrollige alati**: Kasutajate, seadmete ja ühenduste pidev valideerimine  
   - **Mikrosegmentatsioon**: Peenhäälestatud võrgukontrollid, mis isoleerivad üksikud MCP komponendid  
   - **Tingimuslik ligipääs**: Riskipõhised ligipääsukontrollid, mis kohanduvad jooksva konteksti ja käitumisega

**Käivitusaja rakenduse kaitse:**  
   - **Runtime Application Self-Protection (RASP)**: Rakendage RASP tehnikaid reaalajas ohtude tuvastamiseks  
   - **Rakenduse jõudluse jälgimine**: Jälgige jõudlusanomaaliaid, mis võivad viidata rünnakutele  
   - **Dünaamilised turvapoliitikad**: Rakendage turvapoliitikaid, mis kohanduvad jooksva ohumaastiku põhjal

## 11. **Microsofti turvaökosüsteemi integreerimine**

**Kõikehõlmav Microsofti turvalisus:**  
   - **Microsoft Defender for Cloud**: Pilve turvaseisundi haldus MCP töökoormustele  
   - **Azure Sentinel**: Pilvepõhine SIEM ja SOAR võimekus edasijõudnud ohtude tuvastamiseks  
   - **Microsoft Purview**: Andmehaldus ja vastavus AI töövoogudele ja andmeallikatele

**Identiteedi ja ligipääsu haldus:**  
   - **Microsoft Entra ID**: Ettevõtte identiteedihaldus tingimusliku ligipääsu poliitikatega  
   - **Privileegitud identiteedi haldus (PIM)**: Just-in-time ligipääs ja kinnitustöövood haldusfunktsioonide jaoks  
   - **Identiteedi kaitse**: Riskipõhine tingimuslik ligipääs ja automatiseeritud ohu reageerimine

## 12. **Pidev turvalisuse areng**

**Ajaga kaasas käimine:**  
   - **Spetsifikatsiooni jälgimine**: Regulaarne MCP spetsifikatsiooni uuenduste ja turvajuhiste muutuste ülevaatus  
   - **Ohuintelligentsus**: AI-spetsiifiliste ohuvoogude ja kompromissinäitajate integreerimine  
   - **Turvakogukonna kaasamine**: Aktiivne osalemine MCP turvakogukonnas ja haavatavuste avalikustamise programmides

**Kohanduv turvalisus:**  
   - **Masinõppe turvalisus**: Kasutage ML-põhist anomaaliate tuvastust uute rünnakumustrite identifitseerimiseks  
   - **Etteteadlik turvaanalüütika**: Rakendage ennustavaid mudeleid proaktiivseks ohtude tuvastamiseks  
   - **Turbeautomaatika**: Automatiseeritud turvapoliitikate uuendused ohuintelligentsi ja spetsifikatsiooni muudatuste põhjal

---

## **Olulised turvaressursid**

### **Ametlik MCP dokumentatsioon**  
- [MCP spetsifikatsioon (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

### **Microsofti turvalahendused**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Microsoft Entra ID turvalisus](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Turvastandardid**  
- [OAuth 2.0 turvalisuse parimad tavad (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 suurte keelemudelite jaoks](https://genai.owasp.org/)  
- [NIST AI riskijuhtimise raamistik](https://www.nist.gov/itl/ai-risk-management-framework)  

### **Rakendamisjuhendid**  
- [Azure API Management MCP autentimise värav](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID MCP serveritega](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Turvateade**: MCP turvapraktikad arenevad kiiresti. Kontrollige alati enne rakendamist kehtiva [MCP spetsifikatsiooni](https://spec.modelcontextprotocol.io/) ja [ametliku turvadokumentatsiooni](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) vastu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
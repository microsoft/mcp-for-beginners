# MCP turvalisuse parimad tavad - 2026. aasta septembri värskendus

> **Oluline:** See dokument kajastab
> [MCP spetsifikatsioon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja ametliku
> [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktiline turvakoolitus

Praktilise rakendamiskogemuse saamiseks soovitame **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - põhjalikku juhendatud ekspeditsiooni MCP-serverite turvamiseks Azure'is. Töötuba katab kõiki OWASP MCP Top 10 riske lähenemise kaudu "haavatav → ekspluateerimine → parandamine → valideerimine".

Selles dokumendis olevad tavad vastavad **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** Azure'i-spetsiifiliste juurutamisjuhistega.

## Olulised turvapraktikad MCP-i juurutusteks

Model Context Protocol toob kaasa ainulaadseid turvaväljakutseid, mis ulatuvad
traditsioonilisest tarkvaraturvalisusest kaugemale. Need tavad käsitlevad põhiva
nõudeid ja MCP-spetsiifilisi ohte, sealhulgas promptide süstimist, tööriistade
mürgitamist, oleku-käepideme ülevõtmist, segaduses esindaja probleeme ja tokeni
läbipääsu haavatavusi.

### **KOHUSTUSLIKUD turvanõuded** 

**Olulised nõuded MCP spetsifikatsioonist:**

> **EI TOHI**: MCP serverid **EI TOHI** aktsepteerida mingeid tokeneid, mis ei ole selgesõnaliselt MCP-serverile välja antud
> 
> **PEAB**: MCP-serverid, mis rakendavad autoriseerimist, **PEAVAD** kontrollima KÕIKI sissetulevaid päringuid
>  
> **EI TOHI**: MCP serverid **EI TOHI** kasutada sessioone autentimiseks
>
> **PEAB**: MCP-proxy-serverid, mis kasutavad staatilist kolmanda osapoole kliendi ID-d, **PEAVAD**
> hankima iga MCP-kliendi nõusoleku enne autoriseerimise edastamist

---

## 1. **Token Security & Authentication**

**Autentimise ja autoriseerimise kontrollid:**
   - **Põhjalik autoriseerimise ülevaatus**: Tehke põhjalikke audititusi MCP-serveri autoriseerimisloogika kohta, et tagada, et ainult ettenähtud kasutajad ja kliendid pääsevad ressurssidele ligi
   - **Väline identiteedipakkuja integratsioon**: Kasutage tuntud identiteedipakkujaid nagu Microsoft Entra ID, selle asemel et rakendada kohandatud autentimist
   - **Tokeni sihtrühma valideerimine**: Kontrollige alati, et tokenid on selgesõnaliselt välja antud teie MCP-serverile - ärge kunagi aktsepteerige ülesvoolu tokeneid
   - **Õige tokeni elutsükkel**: Rakendage turvalist tokenite rotatsiooni, aegumise poliitikaid ja vältige tokeni taasesituse rünnakuid

**Protected Token Storage:**
   - Kasutage Azure Key Vaulti või sarnaseid turvalisi volitiste salvestusruume kõigi saladuste jaoks
   - Rakendage tokenite krüpteerimist nii puhkeolekus kui ka edastamise ajal
   - Regulaarne volituste vahetamine ja loata juurdepääsu jälgimine

## 2. **State Handle & Transport Security**

**Secure Application State Practices:**

- **Mitteavalikud olekukäepidemed**: Kasutage turvalisi, mitte-deterministlikke käepidemeid
   rakenduse oleku jaoks, mis ulatub üle päringute
- **Kasutajaspetsiifiline sidumine**: Siduge käepidemed serveripoolsel küljel autentitud
   osapoolega ja keelake kasutajatevaheline taaskasutus
- **Elutsükli haldus**: Aegustage ja tühistage käepidemed, et piirata haavatavuse
   perioode
- **Iga päringu autoriseerimine**: Ärge kunagi käsitlege olekukäepidet autentimisena;
   autoriseerige iga päring, mis seda esitab

**Transport Layer Security:**

- Nõudke tootmiskeskkonnas HTTPS-i kaug-HTTP transpordi jaoks
- Kasutage protsesside isolatsiooni ja keskkonna volitusi kohalike stdio-serverite jaoks
- Konfigureerige kaasaegne TLS koos nõuetekohase sertifikaadi rotatsiooni ja valideerimisega

## 3. **AI-spetsiifiline ohtude kaitse** 🤖

**Prompt-süstimise kaitse:**
   - **Microsoft Prompt Shields**: Paigaldage AI Prompt Shields pahatahtlike juhiste täpsemaks tuvastamiseks ja filtreerimiseks
   - **Sisendite puhastamine**: Kontrollige ja puhastage kõik sisendid, et vältida süstimisrünnakuid ja segaduses esindaja probleeme
   - **Sisu piirid**: Kasutage eraldajaid ja andmemärgistamise süsteeme, et eristada usaldusväärseid juhiseid välisest sisust

**Tööriistade mürgitamise ennetamine:**
   - **Tööriista metaandmete valideerimine**: Rakendage terviklikkuse kontrollid tööriistade määratluste jaoks ja jälgige ootamatuid muutusi
   - **Dünaamiline tööriista jälgimine**: Jälgige käitusajal käitumist ja seadistage teavitused ootamatute täitmismustrite jaoks
   - **Kinnituse töövood**: Nõudke tööriista muudatuste ja võimekuse muutuste puhul selget kasutaja kinnitust

## 4. **Access Control & Permissions**

**Väikseima privileegi põhimõte:**
   - Anda MCP-serveritele ainult minimaalsed õigused, mis on vajalikud kavandatud funktsionaalsuse jaoks
   - Rakendage rollipõhist juurdepääsukontrolli (RBAC) peenhäälestatud õigustega
   - Regulaarne õiguste ülevaatus ja pidev järelevalve privileegide eskalatsiooni eest

**Käitusaja õiguste kontrollid:**
   - Rakendage ressursipiiranguid, et vältida ressursside ammendumise rünnakuid
   - Kasutage konteinerite isolatsiooni tööriistade täitmiskeskkondades  
   - Rakendage just-in-time juurdepääsu administraatorfunktsioonidele

## 5. **Content Safety & Monitoring**

**Sisuohutuse rakendamine:**
   - **Azure Content Safety integratsioon**: Kasutage Azure Content Safety-d kahjuliku sisu, jailbreak-katsete ja poliitikarikkumiste tuvastamiseks
   - **Käitumuslik analüüs**: Rakendage käitusaja käitumise jälgimist, et tuvastada anomaaliaid MCP-serveri ja tööriistade täitmises
   - **Põhjalik logimine**: Logige kõik autentimis katsed, tööriistade käivitused ja turvasündmused turvalisse, muutustekindlasse salvestusse

**Pidev jälgimine:**
   - Reaalajas teavitused kahtlastest mustritest ja loata juurdepääsu katsetest  
   - Integreerimine SIEM-süsteemidega tsentraliseeritud turvasündmuste haldamiseks
   - Regulaarne turvaauditid ja sissetungitestid MCP-juurutuste puhul

## 6. **Supply Chain Security**

**Komponentide verifitseerimine:**
   - **Sõltuvuste skaneerimine**: Kasutage automatiseeritud haavatavuste skaneerimist kõigi tarkvarasõltuvuste ja AI-komponentide jaoks
   - **Päritolu valideerimine**: Kontrollige mudelite, andmeallikate ja väliste teenuste päritolu, litsentsimist ja terviklikkust
   - **Allkirjastatud paketid**: Kasutage krüptograafiliselt allkirjastatud pakette ja kontrollige allkirju enne juurutamist

**Turvaline arenduskanal:**
   - **GitHub Advanced Security**: Rakendage salajaste skaneerimist, sõltuvuste analüüsi ja CodeQL staatilist analüüsi
   - **CI/CD turvalisus**: Integreerige turvakontrollid automaatsete juurutuskanalite igasse etappi
   - **Artefaktide terviklikkus**: Rakendage krüptograafiline verifitseerimine juurutatud artefaktide ja konfiguratsioonide jaoks

## 7. **OAuthi turvalisus ja 'confused deputy' ennetamine**

**OAuth 2.1 rakendamine:**
   - **PKCE rakendamine**: Kasutage Proof Key for Code Exchange (PKCE) kõigi autoriseerimistaotluste puhul
    - **Kliendi registreerimine**: Eelistage Client ID Metadata dokumente või
       eelregistreerimist; kasutage aegunud Dynamic Client Registrationit ainult
       ühilduvusvaruplahendusena
    - **Selge nõusolek**: MCP-proxyd, mis kasutavad staatilist kolmanda osapoole kliendi ID-d, peavad
       hankima iga MCP-kliendi nõusoleku enne autoriseerimise edastamist
   - **Redirect URI valideerimine**: Rakendage ranget redirect URI-de ja kliendi identifikaatorite valideerimist

**Proksi turvalisus:**
   - Takistage autoriseerimise kõrvalepääsu staatilise kliendi ID ärakasutamise kaudu
   - Rakendage sobivaid nõusoleku töövooge kolmanda osapoole API-juurdepääsu jaoks
   - Jälgige autoriseerimiskoodi vargust ja loata API-juurdepääsu

## 8. **Intsidendi reageerimine ja taastumine**

**Kiire reageerimisvõimekus:**
   - **Automatiseeritud reageerimine**: Rakendage automatiseeritud süsteeme volituste vahetamiseks ja ohtude piiramiseks
   - **Tagasipööramise protseduurid**: Võime kiiresti taastada teada-töökorras konfiguratsioonid ja komponendid
   - **Forensilised võimekused**: Põhjalikud auditeerimisrajad ja logid intsidendi uurimiseks

**Kommunikatsioon ja koordineerimine:**
   - Selged eskalatsiooniprotseduurid turvaintsidentide jaoks
   - Integratsioon organisatsiooni intsidentide reageerimismeeskondadega
   - Regulaarsete turvaintsidentide simulatsioonide ja lauaharjutuste läbiviimine

## 9. **Nõuetele vastavus ja juhtimine**

**Regulatiivne vastavus:**
   - Veenduge, et MCP-juurutused vastaksid tööstusharu-spetsiifilistele nõuetele (GDPR, HIPAA, SOC 2)
   - Rakendage andmete klassifitseerimine ja privaatsuse kontrollid AI andmete töötlemiseks
   - Hooldage põhjalikku dokumentatsiooni nõuetele vastavuse auditiks

**Muudatuste haldus:**
   - Formaalsed turvakontrolliprotsessid kõigi MCP-süsteemi muudatuste jaoks
   - Versioonihaldus ja heakskiidu töövood konfiguratsioonimuudatuste jaoks
   - Regulaarne vastavuse hindamine ja lõheanalüüs

## 10. **Täiustatud turvakontrollid**

**Zero Trust arhitektuur:**
   - **Ärge kunagi usalda, kontrolli alati**: Pidev kasutajate, seadmete ja ühenduste valideerimine
   - **Mikrosegmentatsioon**: Peenhäälestatud võrgukontrollid, mis isoleerivad üksikuid MCP-komponente
   - **Tingimuslik juurdepääs**: Riskipõhised juurdepääsukontrollid, mis kohanduvad praeguse konteksti ja käitumise järgi

**Käitusaja rakenduse kaitse:**
   - **Runtime Application Self-Protection (RASP)**: Kasutage RASP-tehnikaid reaalajas ohtude tuvastamiseks
   - **Rakenduse jõudluse jälgimine**: Jälgige jõudlusanomaaliaid, mis võivad viidata rünnakutele
   - **Dünaamilised turvapoliitikad**: Rakendage turvapoliitikaid, mis kohanduvad vastavalt praegusele ohtude maastikule

## 11. **Microsofti turvakosüsteemi integratsioon**

**Põhjalik Microsofti turvalisus:**
   - **Microsoft Defender for Cloud**: Pilve turvaseisundi haldus MCP töökoormustele
   - **Azure Sentinel**: Pilvepõhine SIEM ja SOAR võimekus täiustatud ohtude tuvastamiseks
   - **Microsoft Purview**: Andmehaldus ja vastavus AI töövoogudele ja andmeallikatele

**Identiteedi ja juurdepääsu haldus:**
   - **Microsoft Entra ID**: Ettevõtte identiteedihaldus koos tingimuslike juurdepääsupoliitikatega
   - **Privileged Identity Management (PIM)**: Just-in-time juurdepääs ja heakskiidu töövood administraatorfunktsioonide jaoks
   - **Identity Protection**: Riskipõhine tingimuslik juurdepääs ja automatiseeritud ohtude reageerimine

## 12. **Pidev turvalisuse areng**

**Uuendustega kursis olemine:**
   - **Spetsifikatsiooni jälgimine**: MCP spetsifikatsiooni värskenduste ja turvajuhiste muutuste regulaarne ülevaatus
   - **Ohuteave**: AI-spetsiifiliste ohuandmete ja kompromiteerimise indikaatorite integreerimine
   - **Turvakogukonna kaasamine**: Aktiivne osalemine MCP turvakogukonnas ja haavatavuste avalikustamise programmides

**Adaptiivne turvalisus:**
   - **Masinõppe turvalisus**: Kasutage ML-põhist anomaalia tuvastust uute rünnakumustrite identifitseerimiseks
   - **Prognoositav turvaanalüütika**: Rakendage prognoosivaid mudeleid proaktiivseks ohtude tuvastamiseks
   - **Turvaautomaatika**: Automatiseeritud turvapoliitikate värskendused ohuteabe ja spetsifikatsiooni muutuste alusel

---

## **Kriitilised turvaressursid**

### **Ametlik MCP dokumentatsioon**
- [MCP spetsifikatsioon (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP turvaressursid**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Põhjalik OWASP MCP Top 10 koos Azure'i juurutamise juhendiga
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Ametlikud OWASP MCP turvariskid
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktiline turvakoolitus MCP jaoks Azure'is

### **Microsofti turvalahendused**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Turvastandardid**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Juurutamisjuhendid**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Turvateade:** MCP turvapraktikad arenevad kiiresti. Kontrollige alati
> vastavust praeguse [MCP spetsifikatsiooniga](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja [ametliku turvadokumentatsiooniga](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> enne rakendamist.

## Mis järgmiseks

- Loe: [MCP Security Controls](./mcp-security-controls.md)
- Naase: [Turvamooduli ülevaade](./README.md)
- Jätka: [Moodul 3: Alustamine](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
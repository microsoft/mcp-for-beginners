# MCP turvalisuse parimad tavad – 2026. aasta septembri uuendus

See põhjalik juhend kirjeldab olulisi turvalisuse parimaid tavasid
Model Context Protocol (MCP) süsteemide rakendamiseks, mis põhinevad
**MCP spetsifikatsioonil 2026-07-28** ja kehtivatel tööstusharu standarditel. Need
tavad käsitlevad nii traditsioonilisi turvariske kui ka MCP kasutuselevõtule unikaalseid
tehisintellekti spetsiifilisi ohte.

## Kriitilised turvanõuded

### Kohustuslikud turvakontrollid (MUST nõuded)

1. **Tokeni valideerimine**: MCP serverid **EI TOHI** vastu võtta mingeid tokeneid, mis ei ole otseselt väljastatud sama MCP serveri jaoks
2. **Autoriseerimise kontroll**: MCP serverid, mis rakendavad autoriseerimist, peavad kontrollima KÕIKI saabuvate taotlusi ning **EI TOHI** kasutada autentimiseks sessioone  
3. **Kasutaja nõusolek**: MCP proxy serverid, mis kasutavad staatilisi kolmanda osapoole kliendi IDsid, peavad saama iga MCP kliendi eest explicitse nõusoleku enne autoriseerimisvoo edasi suunamist
4. **Oleku käitleja turvalisus**: MCP serverid **EI TOHI** pidada autentimiseks rakenduse oleku käitlejat iseenesest ning **PEAVAD** autoriseerima iga selle käitlejat kasutava taotluse



## Põhituru praktilised tegevused

### 1. Sisendi valideerimine & puhastus
- **Põhjalik sisendi valideerimine**: Kinnitage ja puhastage kõik sisendid, et vältida süstimisrünnakuid, segadust tekitavaid vahetöötaja probleeme ja promptide süstimist
- **Parameetri skeemi täitmine**: Rakendage ranget JSON skeemi valideerimist kõigi tööriistade parameetrite ja API sisendite jaoks
- **Sisu filtreerimine**: Kasutage Microsoft Prompt Shieldsi ja Azure Content Safety’d, et filtreerida pahatahtlikku sisu promptides ja vastustes
- **Väljundi puhastus**: Kontrollige ja puhastage kõik mudeli väljundid enne kasutajatele või edasiandvate süsteemide esitlust

### 2. Autentimine & autoriseerimine tipptasemel  
- **Väline identiteedi pakkujad**: Usaldage autentimine välistele tunnustatud identiteedipakkujatele (Microsoft Entra ID, OAuth 2.1 pakkujad) asemel et rakendada kohandatud autentimist
- **Kliendi registreerimine**: Eelistage kliendi ID metadokumendid või eelregistreerimist; kasutage aegunud dünaamilist kliendi registreerimist ainult ühilduvuse tagamiseks
- **Peenhäälestatud õigused**: Rakendage detaileeritud, tööriistapõhiseid õigusi järgides vähima privileegi põhimõtet
- **Tokeni elutsükli haldus**: Kasutage lühiajalisi ligipääsutoekeneid koos kindla pööramise ja õige sihtrühma valideerimisega
- **Mitmefaktoriline autentimine**: Nõua MFA-d kogu haldusjuurdepääsu ja tundlike toimingute puhul

### 3. Turvalised kommunikatsiooniprotokollid
- **Transportkihi turvalisus (TLS)**: Kasutage kaugside MCP HTTP suhtlemiseks HTTPS-i koos korrektselt valideeritud sertifikaatidega
	kasutage protsessi isoleerimist ja keskkonna mandaate kohalike stdio serverite jaoks

- **Täielik krüpteerimine**: Rakendage täiendavaid krüpteerimiskihte väga tundlike andmete jaoks, nii edastamisel kui ka salvestamisel
- **Sertifikaadi haldus**: Hoolitsege sertifikaatide elutsükli halduse eest koos automatiseeritud uuendustega
- **Protokolli versiooni nõue**: Kasutage MCP `2026-07-28`, lisage vajalik versioonimetaandmed iga taotluse juurde ning lükake tagasi toetamatud versioonid


### 4. Täiustatud kiirusepiirang ja ressursikaitse
- **Mitmekihiline kiirusepiirang**: Rakendage kiirusepiirangut kasutaja, mandaadi,
  toimingu, tööriista ja ressursi lõikes kuritarvituste vältimiseks
- **Kohanduv kiirusepiirang**: Kasutage masinõppel põhinevat kiirusepiirangut, mis kohandub kasutusmustrite ja ohutunnustega
- **Ressursside kvootide haldus**: Määrake sobivad piirangud arvutusressurssidele, mälu kasutusele ja täitmisaegadele
- **DDoS kaitse**: Paigaldage põhjalikud DDoS kaitse ja liikluse analüüsi süsteemid

### 5. Põhjalik logimine & jälgimine
- **Struktureeritud auditi logimine**: Rakendage detailsed, otsitavad logid kõigi MCP operatsioonide, tööriistade täitmiste ja turvasündmuste jaoks
- **Reaalajas turvajälgimine**: Paigaldage SIEM süsteemid AI-põhise anomaaliate tuvastusega MCP töökoormuste jaoks
- **Privaatsust järgivad logid**: Logige turvasündmusi, austades samas andmekaitse nõudeid ja regulatsioone
- **Intsidendi reageerimise integreerimine**: Siduge logimissüsteemid automatiseeritud intsidentide lahendamise töövoogudega

### 6. Täiustatud turvalised salvestustavad
- **Riistvaralised turvamoodulid**: Kasutage võtmete salvestamiseks HSM-põhist lahendust (Azure Key Vault, AWS CloudHSM) kriitiliste krüptograafiliste toimingute jaoks
- **Krüpteerimisvõtmete haldus**: Rakendage nõuetekohane võtmete pööramine, eraldamine ja juurdepääsukontrollid krüpteerimisvõtmetele
- **Saladuste haldus**: Salvestage kõik API võtmed, tokenid ja mandaadid pühendatud saladuste halduse süsteemidesse
- **Andmete klassifitseerimine**: Klassifitseerige andmeid nende tundlikkuse taseme järgi ja rakendage sobivad kaitsetavad

### 7. Täiustatud tokenite haldus
- **Tokenite läbivuse vältimine**: Rangelt keelata tokenite läbivusmustrid, mis mööduvad turvakontrollidest
- **Publiku valideerimine**: Kontrollige alati, et tokeni sihtgrupi nõuded vastaksid kavandatud MCP serveri identiteedile
- **Nõuete-põhine autoriseerimine**: Rakendage peenhäälestatud autoriseerimist tokeni nõuete ja kasutajate atribuutide alusel
- **Tokenite sidumine**: Kontrollige, et tokenid oleksid suunatud õigele MCP ressursile ning
 siduge rakenduse oleku käitlejad serveripoolsetele autentitud isikutele

### 8. Turvaline rakenduse olek

- **Krüptograafilised oleku käitlejad**: Looge mittejärjepidevad, läbipaistmatu käitlejad
 olekutele, mis hõlmavad mitut taotlust
- **Kasutajapõhine sidumine**: Siduge iga käitleja serveripoolselt autentitud
 isikuga; ärge usaldage kliendi poolt edastatud kasutajatunnust
- **Elutsükli kontrollid**: Aegustage ja tühistage käitlejad ning määratlege, kuidas kutsujad saavad
 tõrgunud olekust taastuda
- **Taotlusepõhine autoriseerimine**: Kontrollige autoriseerimist iga kord, kui käitleja esitatakse;
 käitleja on nimi, mitte mandaadid

### 9. Tehisintellektile spetsiifilised turvakontrollid
- **Prompti süstimise kaitse**: Kasutage Microsoft Prompt Shields’i valgustuse, eraldajate ja andmemärgistustehnikatega
- **Tööriista mürgitamise ennetamine**: Kontrollige tööriista metadatat, jälgige dünaamilisi muudatusi ja valideerige tööriistade terviklikkust
- **Mudeli väljundi valideerimine**: Kontrollige mudeli väljundeid võimaliku andmelekkimise, kahjuliku sisu või turvapoliitika rikkumiste suhtes
- **Kontekstualaku kaitse**: Rakendage kontrollmehhanismid, mis takistavad kontekstualaku mürgitamist ja manipuleerimisrünnakuid

### 10. Tööriistade täitmise turvalisus
- **Täitmismullid**: Käivitage tööriistade täitmine konteineriseeritud, isoleeritud keskkondades koos ressursipiirangutega
- **Privileegide eraldamine**: Käivitage tööriistu miinimumvajaduse privileegide ja eraldiseisvate teenusekontodega
- **Võrgu isoleerimine**: Rakendage võrgu segmentatsiooni tööriistade täitmiskeskkondades
- **Täitmiste jälgimine**: Jälgige tööriista täitmisi anomaaliate, ressursikasutuse ja turvarikkumiste suhtes

### 11. Järjepidev turvalisuse valideerimine
- **Automatiseeritud turvatestimine**: Integreerige turvatestimine CI/CD torudesse tööriistadega nagu GitHub Advanced Security
- **Haavatavuste haldus**: Skaneerige regulaarselt kõiki sõltuvusi, sealhulgas AI mudeleid ja väliseid teenuseid
- **Sissetungimise testimine**: Korraldage regulaarselt turva-auditeid, mis on suunatud otseselt MCP rakendustele
- **Turvakoodi ülevaated**: Rakendage kohustuslikud turvakoodi ülevaated kõigile MCP-ga seotud koodimuudatustele

### 12. Tehisintellekti tarneahela turvalisus
- **Komponentide kontroll**: Kontrollige kõigi AI komponentide (mudelid, manused, APId) päritolu, terviklikkust ja turvalisust
- **Sõltuvuste haldus**: Hoolitsege kõigi tarkvara ja AI sõltuvuste ajakohaste inventuuride ja haavatavuste jälgimise eest
- **Usaldusväärsed hoidlad**: Kasutage kõigi AI mudelite, raamistike ja tööriistade jaoks verifitseeritud ja usaldusväärseid allikaid
- **Tarneahela jälgimine**: Jälgige pidevalt AI teenusepakkujate ja mudeli hoidlate võimalikku kompromiteerimist


## Täiustatud turbemustrid

### Null usaldus MCP jaoks
- **Ära usalda kunagi, kontrolli alati**: Rakenda kõigi MCP osalejate pidev kinnitamine
- **Mikrosegmentimine**: Isoleeri MCP komponendid detailsete võrgustiku- ja identiteedikontrollidega
- **Tingimuslik ligipääs**: Rakenda riskipõhist ligipääsukontrolli, mis kohandub konteksti ja käitumisega
- **Pidev riskihindamine**: Hinda dünaamiliselt turvalisuse seisu praeguste ohuindikaatorite põhjal

### Privaatsust säilitava tehisintellekti rakendamine
- **Andmete minimeerimine**: Avalda iga MCP toimingu jaoks vaid minimaalne vajalik andmekogus
- **Diferentseeritud privaatsus**: Rakenda tundlike andmete töötlemiseks privaatsust säilitavaid meetodeid
- **Homomorfne krüpteerimine**: Kasuta täiustatud krüpteerimistehnikaid krüpteeritud andmete turvaliseks arvutamiseks
- **Federeeritud õppimine**: Rakenda hajutatud õppimise lähenemisi, mis säilitavad andmete lokaalsuse ja privaatsuse

### Juhtumite käsitlemine tehisintellektisüsteemide jaoks
- **AI-spetsiifilised juhtumiprotseduurid**: Töötada välja juhtumite käsitlemise protseduurid, mis on kohandatud AI ja MCP konkreetsete ohtudega
- **Automatiseeritud reageerimine**: Rakendada automatiseeritud piiranguid ja parandusi tavapäraste AI turvajuhtumite korral  
- **Forensika võimekus**: Hoida valmisolekut AI süsteemide kompromiteerimise ja andmerikkumiste forensika jaoks
- **Taastumisprotseduurid**: Määratleda protseduurid AI mudeli mürgitamisest, promptide süstimise rünnakutest ja teenuse kompromiteerimisest taastumiseks

## Rakendamise ressursid & standardid

### 🏔️ Praktikal põhinev turbeõpe
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Kõikehõlmav praktiline töötuba MCP serverite turvamiseks Azure'is
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Viitearhitektuur ja OWASP MCP Top 10 rakendusjuhend

### Ametlik MCP dokumentatsioon
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Kehtiv MCP protokolli spetsifikatsioon
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Ametlik turbejuhend
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP autorisatsioonimustrid
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Transpordi nõuded

### Microsoft Security lahendused
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Täiustatud prompti süstimise kaitse
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kõikehõlmav AI sisu filtreerimine
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Ettevõtte identiteedi ja ligipääsu haldus
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Turvaline saladuste ja volituste haldus
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Tarneahela ja koodi turvakontrollid

### Turbestandardid & raamistikud
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Kehtiv OAuth turbejuhend
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Veebirakenduste turvariskid
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-spetsiifilised turvariskid
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kõikehõlmav tehisintellekti riskide juhtimise raamistik
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Infoturbe juhtimissüsteemid

### Rakendamise juhendid & õpetused
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Ettevõtte autentimismustrid
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Identiteediteenuse pakkuja integratsioon
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Parimad praktikad tokenite haldamiseks
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Täiustatud krüpteerimismustrid

### Täiustatud turberessursid
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Turvalise arenduse praktikad
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-spetsiifiline turbetestimine
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI ohtude modelleerimise metoodika
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Privaatsust säilitavad AI tehnoloogiad

### Vastavus & juhtimine
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Privaatsuse järgimine AI süsteemides
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Vastutustundliku AI rakendamine
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Turvakontrollid AI teenuse pakkujatele
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Tervishoiu AI nõuetele vastavus

### DevSecOps & automatiseerimine
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Turvalised AI arendusliinid
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Pidev turbe valideerimine
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Turvaline infrastruktuuri juurutamine
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI töökoormuste konteinerite turvalisus

### Jälgimine & juhtumite käsitlemine  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Kõikehõlmavad jälgimislahendused
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-spetsiifilised juhtumikäsitluse protseduurid
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Turbeteabe ja sündmuste haldus

- [Ohutuse luure tehisintellekti jaoks](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - tehisintellekti ohulipukad

## 🔄 Jätkuv parandamine

### Jääge kursis muutuvate standarditega
- **MCP spetsifikatsiooni uuendused**: jälgige ametlikke MCP spetsifikatsiooni muudatusi ja turvateateid
- **Ohuteabe teenused**: tellige tehisintellekti turvaohtude vooge ja haavatavuste andmebaase  
- **Kogukonna kaasamine**: osalege MCP turvakogukonna aruteludes ja töörühmades
- **Regulaarne hindamine**: tehke igakuised turvaseisu hinnangud ja värskendage praktikaid vastavalt

### Panustamine MCP turvalisusse
- **Turvauuringud**: panustage MCP turvauuringutesse ja haavatavuste avalikustamise programmidesse
- **Parimate praktikate jagamine**: jagage turvalahendusi ja õppetunde kogukonnaga
- **Standardite arendamine**: osalege MCP spetsifikatsiooni väljatöötamises ja turvastandardite loomises
- **Tööriistade arendamine**: arendage ja jagage turvatööriistu ja -raamatukogusid MCP ökosüsteemis

---

*See dokument kajastab MCP turvalisuse parimaid tavasid seisuga 9. september 2026,
põhinedes MCP spetsifikatsioonil `2026-07-28`. Turvapraktikaid tuleks regulaarselt
üle vaadata vastavalt protokolli ja ohumaastiku arengutele.*

## Mis tuleb järgmisena

- Loe: [MCP Turvalisuse Parimad Praktikad](./mcp-security-best-practices.md)
- Naase: [Turvamooduli Ülevaade](./README.md)
- Jätka: [Moodul 3: Alustamine](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
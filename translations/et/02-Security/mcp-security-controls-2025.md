# MCP turvakontrollid – detsember 2025 uuendus

> **Kehtiv standard**: See dokument kajastab [MCP spetsifikatsiooni 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) turvanõudeid ja ametlikke [MCP turvalisuse parimaid tavasid](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) on oluliselt küpsenud, pakkudes täiustatud turvakontrolle, mis käsitlevad nii traditsioonilist tarkvara turvalisust kui ka AI-spetsiifilisi ohte. See dokument annab põhjalikud turvakontrollid turvaliste MCP rakenduste jaoks seisuga detsember 2025.

## **KOHUSTUSLIKUD turvanõuded**

### **MCP spetsifikatsiooni kriitilised keelud:**

> **KEELATUD**: MCP serverid **EI TOHI** vastu võtta ühtegi tokenit, mis ei ole selgesõnaliselt MCP serverile väljastatud  
>
> **KEELATUD**: MCP serverid **EI TOHI** kasutada sessioone autentimiseks  
>
> **NÕUTUD**: MCP serverid, mis rakendavad autoriseerimist, **PEAVAD** kontrollima KÕIKI sissetulevaid päringuid  
>
> **KOHUSTUSLIK**: MCP proxy serverid, mis kasutavad staatilisi kliendi ID-sid, **PEAVAD** saama kasutaja nõusoleku iga dünaamiliselt registreeritud kliendi jaoks

---

## 1. **Autentimise ja autoriseerimise kontrollid**

### **Välise identiteedipakkuja integreerimine**

**Kehtiv MCP standard (2025-06-18)** lubab MCP serveritel delegeerida autentimine välistele identiteedipakkujatele, mis on oluline turvalisuse täiendus:

### **Välise identiteedipakkuja integreerimine**

**Kehtiv MCP standard (2025-11-25)** lubab MCP serveritel delegeerida autentimine välistele identiteedipakkujatele, mis on oluline turvalisuse täiendus:

**Turvaboonused:**
1. **Eemaldab kohandatud autentimise riskid**: Vähendab haavatavust, vältides kohandatud autentimise rakendusi  
2. **Ettevõtte tasemel turvalisus**: Kasutab tuntud identiteedipakkujaid nagu Microsoft Entra ID koos täiustatud turvafunktsioonidega  
3. **Keskne identiteedihaldus**: Lihtsustab kasutajate elutsükli haldust, juurdepääsukontrolli ja vastavusauditit  
4. **Mitmefaktoriline autentimine**: Pärib MFA võimalused ettevõtte identiteedipakkujatelt  
5. **Tingimuslikud juurdepääsupoliitikad**: Kasutab riskipõhiseid juurdepääsukontrolle ja adaptiivset autentimist

**Rakendamise nõuded:**
- **Tokeni sihtrühma valideerimine**: Kontrolli, et kõik tokenid on selgesõnaliselt MCP serverile väljastatud  
- **Väljastaja kontroll**: Kontrolli, et tokeni väljastaja vastab oodatud identiteedipakkujale  
- **Allkirja valideerimine**: Tokeni terviklikkuse krüptograafiline kontroll  
- **Aegumistähtaja täitmine**: Rangelt järgida tokeni kehtivusaja piiranguid  
- **Ulatus (scope) valideerimine**: Veendu, et tokenid sisaldavad sobivaid õigusi taotletud toiminguteks

### **Autoriseerimise loogika turvalisus**

**Kriitilised kontrollid:**
- **Põhjalikud autoriseerimise auditid**: Regulaarne turvakontroll kõigi autoriseerimisotsuste punktide üle  
- **Veaohutud vaikeseaded**: Keela juurdepääs, kui autoriseerimise loogika ei suuda teha lõplikku otsust  
- **Õiguste piirid**: Selge eristamine erinevate privileegitasemete ja ressursside juurdepääsu vahel  
- **Auditilogimine**: Kõigi autoriseerimisotsuste täielik logimine turvaseire jaoks  
- **Regulaarsed juurdepääsu ülevaated**: Kasutaja õiguste ja privileegide perioodiline valideerimine

## 2. **Tokeni turvalisus ja anti-passthrough kontrollid**

### **Tokeni läbipääsu (passthrough) vältimine**

**Tokeni läbipääs on MCP autoriseerimise spetsifikatsioonis selgesõnaliselt keelatud** kriitiliste turvariskide tõttu:

**Käsitletud turvariskid:**
- **Kontrolli vältimine**: Vältib olulisi turvakontrolle nagu kiirusepiirang, päringu valideerimine ja liikluse jälgimine  
- **Vastutuse kadumine**: Muudab kliendi tuvastamise võimatuks, rikkudes auditeid ja intsidentide uurimist  
- **Proksipõhine andmete väljapääs**: Võimaldab pahatahtlikel osapooltel kasutada servereid volitamata andmetele ligipääsuks  
- **Usalduspiiri rikkumised**: Rikub alluvate teenuste usaldusreeglid tokenite päritolu osas  
- **Lateral liikumine**: Kompromiteeritud tokenid mitmes teenuses võimaldavad laiemat rünnakut

**Rakendamise kontrollid:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Turvalised tokenihalduse mustrid**

**Parimad tavad:**
- **Lühiajalised tokenid**: Minimeeri kokkupuuteaeg sagedase tokenite rotatsiooniga  
- **Just-in-time väljastamine**: Väljastada tokenid ainult konkreetsete toimingute jaoks vajadusel  
- **Turvaline salvestus**: Kasuta riistvaraturbe mooduleid (HSM) või turvalisi võtmehoidlaid  
- **Tokeni sidumine**: Seo tokenid võimalusel konkreetsete klientide, sessioonide või toimingutega  
- **Jälgimine ja häirete tekitamine**: Reaalajas tokeni väärkasutuse või volitamata juurdepääsu mustrite tuvastamine

## 3. **Sessiooni turvakontrollid**

### **Sessiooni kaaperdamise vältimine**

**Käsitletavad rünnakute vektorid:**
- **Sessiooni kaaperdamise prompti süstimine**: Pahatahtlike sündmuste süstimine jagatud sessiooniseisundisse  
- **Sessiooni esindamine**: Volitamata varastatud sessiooni ID-de kasutamine autentimise vältimiseks  
- **Jätkusuutlike voogude rünnakud**: Serveri saadetud sündmuste jätkamise ärakasutamine pahatahtliku sisu süstimiseks

**Kohustuslikud sessioonikontrollid:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Transporditurve:**
- **HTTPS nõue**: Kõik sessioonisuhtlus TLS 1.3 kaudu  
- **Turvalised küpsise atribuudid**: HttpOnly, Secure, SameSite=Strict  
- **Sertifikaadi kinnitamine**: Kriitiliste ühenduste jaoks MITM rünnakute vältimiseks

### **Seisundipõhise vs seisundivaba kaalutlused**

**Seisundipõhiste rakenduste puhul:**
- Jagatud sessiooniseisund vajab täiendavat kaitset süstimisrünnakute vastu  
- Järjekorpõhine sessioonihaldus vajab terviklikkuse kontrolli  
- Mitme serveri instantsi puhul on vajalik turvaline sessiooniseisundi sünkroonimine

**Seisundivabade rakenduste puhul:**
- JWT või sarnane tokenipõhine sessioonihaldus  
- Krüptograafiline sessiooniseisundi terviklikkuse kontroll  
- Vähendatud rünnakupind, kuid nõuab tugevat tokeni valideerimist

## 4. **AI-spetsiifilised turvakontrollid**

### **Prompti süstimise kaitse**

**Microsoft Prompt Shields integratsioon:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Rakendamise kontrollid:**
- **Sisendi puhastamine**: Kõigi kasutajasisendite põhjalik valideerimine ja filtreerimine  
- **Sisu piiri määratlemine**: Selge eristamine süsteemi juhiste ja kasutajasisu vahel  
- **Juhiste hierarhia**: Õiged eelisreeglid vastuoluliste juhiste korral  
- **Väljundi jälgimine**: Potentsiaalselt kahjulike või manipuleeritud väljundite tuvastamine

### **Tööriistade mürgitamise vältimine**

**Tööriistade turvafraamistik:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Dünaamiline tööriistade haldus:**
- **Kinnituse töövood**: Selge kasutaja nõusolek tööriistade muudatusteks  
- **Tagasipööramise võimalused**: Võimalus taastada varasemad tööriistaversioonid  
- **Muudatuste audit**: Tööriistade definitsioonimuudatuste täielik ajalugu  
- **Riskihindamine**: Automaatne tööriistade turvaseisundi hindamine

## 5. **Segaduses esindaja rünnaku vältimine**

### **OAuth proxy turvalisus**

**Rünnakute vältimise kontrollid:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Rakendamise nõuded:**
- **Kasutaja nõusoleku kontroll**: Ära jäta dünaamilise kliendi registreerimisel nõusolekuekraane vahele  
- **Redirect URI valideerimine**: Rangelt valge nimekirja alusel sihtkohtade valideerimine  
- **Autoriseerimiskoodi kaitse**: Lühiajalised koodid, mis kehtivad ainult ühe korra  
- **Kliendi identiteedi kontroll**: Tugev kliendi mandaadi ja metaandmete valideerimine

## 6. **Tööriistade täitmise turvalisus**

### **Sandboxing ja isoleerimine**

**Konteineripõhine isoleerimine:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Protsessi isoleerimine:**
- **Eraldatud protsessikontekstid**: Iga tööriista täitmine isoleeritud protsessiruumis  
- **Protsessidevaheline suhtlus**: Turvalised IPC mehhanismid valideerimisega  
- **Protsessi jälgimine**: Käitumise analüüs ja anomaaliate tuvastamine jooksvalt  
- **Ressursside piiramine**: Rangelt piiratud CPU, mälu ja I/O kasutus

### **Vähima privileegiga rakendamine**

**Õiguste haldus:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Tarneahela turvakontrollid**

### **Sõltuvuste valideerimine**

**Põhjalik komponendi turvalisus:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Jätkuv jälgimine**

**Tarneahela ohu tuvastamine:**
- **Sõltuvuste tervise jälgimine**: Kõigi sõltuvuste pidev hindamine turvariskide osas  
- **Ohuinfo integreerimine**: Reaalajas uuendused tekkivate tarneahela ohtude kohta  
- **Käitumisanalüüs**: Ebatavalise käitumise tuvastamine väliskomponentides  
- **Automaatne reageerimine**: Kompromiteeritud komponentide viivitamatu piiramine

## 8. **Jälgimise ja tuvastamise kontrollid**

### **Turvateabe ja sündmuste haldus (SIEM)**

**Põhjalik logimise strateegia:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Reaalajas ohu tuvastamine**

**Käitumisanalüütika:**
- **Kasutajakäitumise analüüs (UBA)**: Ebatavaliste kasutajate juurdepääsumustrite tuvastamine  
- **Üksuse käitumise analüüs (EBA)**: MCP serveri ja tööriistade käitumise jälgimine  
- **Masinõppe anomaaliate tuvastus**: AI-põhine turvaohtude identifitseerimine  
- **Ohuinfo korrelatsioon**: Täheldatud tegevuste võrdlemine tuntud rünnakumustritega

## 9. **Intsidentidele reageerimine ja taastumine**

### **Automatiseeritud reageerimisvõimekus**

**Viivitamatud reageerimistoimingud:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Forensika võimekus**

**Uurimise tugi:**
- **Auditiraja säilitamine**: Muutmatu logimine krüptograafilise terviklikkusega  
- **Tõendite kogumine**: Automaatne asjakohaste turbeartefaktide kogumine  
- **Ajaskaala rekonstrueerimine**: Üksikasjalik sündmuste jada turvaintsidentide eel  
- **Mõju hindamine**: Kompromissi ulatuse ja andmete lekkimise hindamine

## **Olulised turva- ja arhitektuuripõhimõtted**

### **Sügavuskaitse (Defense in Depth)**
- **Mitmekihiline turvalisus**: Ühteainsat tõrke- või rünnakupunkti ei ole  
- **Redundantne kontroll**: Kriitiliste funktsioonide kattuvad turvameetmed  
- **Veaohutud mehhanismid**: Turvalised vaikeseaded süsteemivigade või rünnakute korral

### **Nullusaldus (Zero Trust) rakendamine**
- **Ära usalda kunagi, kontrolli alati**: Kõigi üksuste ja päringute pidev valideerimine  
- **Vähima privileegi põhimõte**: Kõigi komponentide minimaalsete juurdepääsuõiguste tagamine  
- **Mikrosegmentatsioon**: Täpne võrgustiku ja juurdepääsu kontroll

### **Jätkuv turvalisuse areng**
- **Ohutsooni kohandamine**: Regulaarne uuendamine tekkivate ohtude käsitlemiseks  
- **Turvakontrollide tõhusus**: Kontrollide pidev hindamine ja täiustamine  
- **Spetsifikatsiooni järgimine**: Vastavus MCP turvastandardite arenguga

---

## **Rakendamise ressursid**

### **Ametlik MCP dokumentatsioon**
- [MCP spetsifikatsioon (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autoriseerimise spetsifikatsioon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsofti turvalahendused**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Turvastandardid**
- [OAuth 2.0 turvalisuse parimad tavad (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurte keelemudelite jaoks](https://genai.owasp.org/)
- [NIST küberturvalisuse raamistik](https://www.nist.gov/cyberframework)

---

> **Oluline**: Need turvakontrollid kajastavad kehtivat MCP spetsifikatsiooni (2025-06-18). Kontrolli alati uusimat [ametlikku dokumentatsiooni](https://spec.modelcontextprotocol.io/), kuna standardid arenevad kiiresti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
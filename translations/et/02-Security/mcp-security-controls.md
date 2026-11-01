# MCP turvakontrollid - 2026. aasta septembri värskendus

> **Kehtiv standard:** See dokument kajastab
> [MCP spetsifikatsioon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> ja ametliku
> [MCP turvalisuse parimad tavad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) on oluliselt küpsenud, lisandunud on täiustatud turvakontrollid, mis käsitlevad nii traditsioonilist tarkvaraturvalisust kui ka tehisintellekti-spetsiifilisi ohte. See dokument sisaldab põhjalikke turvakontrolle turvaliste MCP-i rakenduste jaoks, mis on kooskõlas OWASP MCP Top 10 raamistikuga.

## 🏔️ Praktiline turvalisuse koolitus

Praktilise, käelise turvarakenduse kogemuse saamiseks soovitame **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - põhjalikku juhendatud ekspeditsiooni MCP serverite turvamiseks Azure'is, kasutades metoodikat "haavatav → ärakasutamine → parandamine → valideerimine".

Kõik selles dokumendis olevad turvakontrollid on kooskõlas **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, mis pakub viitearhitektuure ja Azure-spetsiifilist juurutusjuhendit OWASP MCP Top 10 riskide jaoks.

## **KOHUSTUSLIKUD turvanõuded**

### **MCP spetsifikatsioonist tulenevad kriitilised keelud:**

> **KEELATUD**: MCP serverid **EI TOHI** vastu võtta ühtegi tokenit, mida ei ole selgesõnaliselt välja antud MCP serverile
>
> **KEELATUD**: MCP serverid **EI TOHI** kasutada sessioone autentimiseks  
>
> **NÕUTUD**: MCP serverid, mis rakendavad autoriseerimist, **PEAVAD** kontrollima KÕIKI sissetulevaid päringuid
>
> **KOHUSTUSLIK**: MCP proxy serverid, mis kasutavad staatilist kolmanda osapoole kliendi ID-d
> **PEAVAD** saama nõusoleku iga MCP kliendi jaoks enne autoriseerimise edastamist

---

## 1. **Autentimise & autoriseerimise kontrollid**

### **Välise identiteedipakkuja integreerimine**

**MCP spetsifikatsioon `2026-07-28`** võimaldab MCP serveritel delegeerida
autentimise välistele identiteedipakkujatele. Autoriseerimine HTTP
edastuste puhul hinnatakse päringu kaupa; kohalikud stdio serverid hangivad volitused
oma keskkonnast.

**Käsitletud OWASP MCP risk**: [MCP07 - Ebapiisav autentimine ja autoriseerimine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Turbe eelised:**
1. **Eemaldab kohandatud autentimise riskid**: Vähendab haavatavuspinna hulka, vältides kohandatud autentimisrakendusi
2. **Ettevõtte klassi turvalisus**: Kasutab tunnustatud identiteedipakkujaid nagu Microsoft Entra ID koos täiustatud turbefunktsioonidega
3. **Keskne identiteedihaldus**: Lihtsustab kasutaja elutsükli haldust, juurdepääsukontrolli ja vastavusauditeid
4. **Mitmefaktoriline autentimine**: Pärib MFA võimalused ettevõtte identiteedipakkujatelt
5. **Tingimuslikud juurdepääsupoliitikad**: Kasu riskipõhistest juurdepääsukontrollidest ja adaptiivsest autentimisest

**Rakendamise nõuded:**
- **Kliendi registreerimine**: Eelista Client ID metaandmete dokumente või
  eelregistreerimist; kasutada aegunud Dynamic Client Registration ainult
  ühilduvuse huvides
- **Token Audience Validation**: Kontrolli, et kõik tokenid oleksid selgelt välja antud MCP-serveri jaoks
- **Issuer Verification**: Kinnita, et tokeni väljastaja vastab oodatud identiteedipakkujale
- **Signature Verification**: Krüptograafiline tokeni terviklikkuse valideerimine
- **Expiration Enforcement**: Tokeni kehtivusaja piirangute range rakendamine
- **Scope Validation**: Veendu, et tokenid sisaldavad vastavaid õigusi taotletud toiminguteks

### **Autoriseerimise loogika turvalisus**

**Kriitilised kontrollid:**
- **Põhjalikud autoriseerimise auditid**: Regulaarne turbeülevaade kõigist autoriseerimisotsuste punktidest
- **Fail-Safe Defaults**: Keelata juurdepääs, kui autoriseerimisloogika ei suuda teha lõplikku otsust
- **Õiguste piirid**: Selge eraldatus erinevate privileegitasemete ja ressurssidele juurdepääsu vahel
- **Audit Logging**: Kõigi autoriseerimisotsuste täielik logimine turvaseire jaoks
- **Regular Access Reviews**: Perioodiline kasutaja õiguste ja privileegimäärangute valideerimine

## 2. **Tokeni turvalisus ja anti-passthrough kontrollid**

**Käsitletud OWASP MCP risk**: [MCP01 - Tokenite haldamise vead ja saladuste lekkimine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Token Passthrough Prevention**

**Tokeni passthrough on MCP-i autoriseerimise spetsifikatsioonis selgelt keelatud** kriitiliste turvariskide tõttu:

**Käsitletavad turvariskid:**
- **Control Circumvention**: Võimaldab mööda minna olulistest turbekontrollidest nagu kiirusepiirang, päringu valideerimine ja liikluse jälgimine
- **Accountability Breakdown**: Muudab kliendi tuvastamise võimatuks, rikub auditeerimisjälgi ja intsidentide uurimist
- **Proxy-Based Exfiltration**: Võimaldab ründajatel kasutada servereid proksidena volitamata andmete juurde pääsemiseks
- **Trust Boundary Violations**: Rikkub alluvate teenuste eeldusi tokeni päritolu kohta
- **Lateral Movement**: Kompromiteeritud tokenid mitme teenuse vahel võimaldavad laiemat rünnakute levikut

**Implementation Controls:**
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

### **Secure Token Management Patterns**

**Best Practices:**
- **Short-Lived Tokens**: Vähenda kokkupuuteaega sagedase tokeni pööramisega
- **Just-in-Time Issuance**: Väljastada tokenid ainult siis, kui need on vajalikud konkreetsete toimingute jaoks
- **Secure Storage**: Kasuta riistvarapõhiseid turbemodule (HSM-id) või turvalisi võtmehoidlaid
- **Token Binding**: Kontrolli tokeni sihtgruppi ja väljastajat kavandatud MCP
  ressursi, kliendi ja toimingu jaoks
- **Monitoring & Alerting**: Tokeni kuritarvituse või volitamata juurdepääsumustrite reaalajas tuvastamine

## 3. **Rakenduse oleku turbekontrollid**

### **Seisundi käepideme ülevõtmise ennetamine**

**Käsitletavad ründevektorid:**
- **Handle Guessing**: Ennustatavad identifikaatorid paljastavad teise kutsuja oleku
- **Cross-user Reuse**: Varastatud käepidet kasutatakse erineva identiteediga
- **Implicit Authorization**: Käepideme omamist tõlgendatakse valesti kui
  juurdepääsu tõendit

**State Handle Controls:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Transport Security:**
- **HTTPS Enforcement**: Nõuda HTTPS-i kaug-HTTP transpordiks
- **Credential Handling**: Saada ja valideeri autoriseerimine kõigi HTTP-päringute juures
- **stdio Isolation**: Kaitsta kohalikke stdio servereid protsessi isolatsiooni ja
  keskkonna tõendite kontrollidega

### **Stateful vs Stateless Considerations**

MCP `2026-07-28` on protokolli tasandil seisunditu. Rakendused võivad siiski
säilitada olekut, tagastades ühe tööriistakõne käepideme ja aktsepteerides
seda tavalise argumendina hilisematel kutsutel.

- Hoia olek sõltumatuna ühestki transpordühendusest.
- Seo seisundi käepidemed serveripoolse autentitud isikuga.
- Kohtle käepidet kui nime, mitte kandjatõendina.
- Määra aegumise ja taastumise käitumine aegunud käepidemete jaoks.

## 4. **Tehisintellektile spetsiifilised turbekontrollid**

**Käsitletavad OWASP MCP riskid**:
- [MCP06 - Eesmärgi voo alistamine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Tööriista mürgitamine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Käskude süstimine ja täitmine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Viipude süstimise kaitse**

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

**Rakenduse kontrollid:**
- **Input Sanitization**: Kõikide kasutajasisestuste põhjalik valideerimine ja filtreerimine
- **Content Boundary Definition**: Selge eraldus süsteemi juhiste ja kasutajasisu vahel
- **Instruction Hierarchy**: Sobivad eelisuse reeglid vastuoluliste juhiste korral
- **Output Monitoring**: Potentsiaalselt kahjulike või manipuleeritud väljundite tuvastamine

### **Tööriistade mürgitamise ennetamine**

**Tööriista turberaamistik:**
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
- **Approval Workflows**: Selge kasutaja nõusolek tööriista muudatuste jaoks
- **Rollback Capabilities**: Võime naasta varasemate tööriista versioonide juurde
- **Change Auditing**: Täielik ajalugu tööriista definitsiooni muudatustest
- **Risk Assessment**: Tööriista turvalisuse automaatne hindamine

## 5. **Segaduses esindaja rünnaku ennetamine**

### **OAuth Proxy Security**

**Ründe ennetamise kontrollid:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
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
- **Kliendi registreerimine**: Eelista eelregistreerimist või Client ID metaandmete
  dokumente; käsitle Dynamic Client Registrationit kui ühilduvuse varuvarianti
- **User Consent Verification**: MCP proksid, mis kasutavad staatilist kolmanda osapoole kliendi
  ID-d, peavad enne autoriseerimise edastamist saama iga kliendi nõusoleku
- **Redirect URI Validation**: Rangelt valgelistel põhinev ümbersuunamiste sihtkohtade valideerimine
- **Authorization Code Protection**: Lühiajalised koodid ühekorralise kasutuse rakendamisega
- **Client Identity Verification**: Tugev kliendi tõendite ja metaandmete valideerimine

## 6. **Tööriistade täitmise turvalisus**

### **Liivakastimine ja isolatsioon**

**Konteineripõhine isolatsioon:**
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

**Protsessi isolatsioon:**
- **Separate Process Contexts**: Iga tööriista täitmine eraldatud protsessi ruumis
- **Inter-Process Communication**: Turvalised IPC-mehhanismid valideerimisega
- **Process Monitoring**: Käitumise analüüs ja anomaaliate tuvastamine reaalaajas
- **Resource Enforcement**: Kõvad piirangud CPU, mälu ja I/O operatsioonidele

### **Least Privilege Implementation**

**Permission Management:**
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

## 7. **Tarneahela turbekontrollid**

**Käsitletud OWASP MCP risk**: [MCP04 - Tarkvara tarneahela rünnakud ja sõltuvuste näpistamine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Dependency Verification**

**Comprehensive Component Security:**
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

### **Continuous Monitoring**

**Supply Chain Threat Detection:**
- **Dependency Health Monitoring**: Kõigi sõltuvuste pidev hindamine turbeprobleemide jaoks
- **Threat Intelligence Integration**: Reaalajas uuendused tekkivate tarneahela ohtude kohta
- **Behavioral Analysis**: Ebahariliku käitumise tuvastamine väliskomponentides
- **Automated Response**: Kompromiteeritud komponentide viivitamatu piiramine

## 8. **Jälgimise ja tuvastamise kontrollid**

**Käsitletud OWASP MCP risk**: [MCP08 - Auditite ja telemeetria puudumine](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Security Information and Event Management (SIEM)**

**Comprehensive Logging Strategy:**
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

### **Real-Time Threat Detection**

**Behavioral Analytics:**
- **User Behavior Analytics (UBA)**: Ebaharilike kasutajate juurdepääsumustrite tuvastamine
- **Entity Behavior Analytics (EBA)**: MCP serveri ja tööriistade käitumise jälgimine
- **Machine Learning Anomaly Detection**: Tehisintellektil põhinev turbeohtude identifitseerimine
- **Threat Intelligence Correlation**: Vaadeldud tegevuste võrdlus tuntud rünnakumustritega

## 9. **Intsidentidele reageerimine ja taastumine**

### **Automaatse reageerimise võimalused**

**Viivitamatud reageerimistegevused:**
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

### **Forensilised võimalused**

**Uurimise tugi:**
- **Audit Trail Preservation**: Muutmatu logimine krüptograafilise terviklikkusega
- **Evidence Collection**: Asjakohaste turbeartefaktide automatiseeritud kogumine
- **Timeline Reconstruction**: Üksikasjalik sündmuste jada, mis viis turvaintsidentideni
- **Impact Assessment**: Hinnang kompromiteerimise ulatusele ja andmete paljastumisele

## **Olulised turbearhitektuuri põhimõtted**

### **Sügavkaitse**
- **Multiple Security Layers**: Turbearhitektuuris ei ole ühteainsat rikepunkti
- **Redundant Controls**: Kattev turbemeetmete ülekatmine kriitiliste funktsioonide jaoks
- **Fail-Safe Mechanisms**: Turvalised vaikeseaded, kui süsteemid puutuvad kokku vigade või rünnakutega

### **Zero Trust rakendamine**
- **Never Trust, Always Verify**: Kõigi üksuste ja päringute pidev valideerimine
- **Principle of Least Privilege**: Minimaalsed juurdepääsuõigused kõigi komponentide jaoks
- **Micro-Segmentation**: Täpne võrgustiku ja juurdepääsu kontroll

### **Pidev turbe areng**
- **Threat Landscape Adaptation**: Regulaarne uuendamine tekkivate ohtude käsitlemiseks
- **Security Control Effectiveness**: Kontinuoossed hindamised ja kontrollide parandamine
- **Specification Compliance**: Vastavus arenevatele MCP turbestandarditele

---

## **Rakendamise ressursid**

### **Ametlik MCP dokumentatsioon**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP turbe ressursid**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Põhjalik OWASP MCP Top 10 koos Azure'i rakendusega
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Ametlikud OWASP MCP turberiskid
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktiline turbeõpe MCP jaoks Azure'is

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Security Standards**
- [OAuth 2.0 turvalisuse parimad tavad (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 suurete keelemudelite jaoks](https://genai.owasp.org/)
- [NIST küberturbe raamistik](https://www.nist.gov/cyberframework)

---

> **Tähtis:** Need turbekontrollid kajastavad MCP spetsifikatsiooni
> `2026-07-28`. Kinnita alati vastavus
> [kehtiva ametliku dokumentatsiooniga](https://modelcontextprotocol.io/specification/2026-07-28/)
> kuna standardid jätkavad arenemist.

## Mis järgmiseks

- Tagasi: [Security Module Overview](./README.md)
- Jätka: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
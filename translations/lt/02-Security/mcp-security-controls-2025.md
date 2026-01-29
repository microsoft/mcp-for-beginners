# MCP Saugumo Kontrolės – 2025 m. gruodžio atnaujinimas

> **Dabartinis standartas**: Šis dokumentas atspindi [MCP specifikaciją 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) saugumo reikalavimus ir oficialias [MCP saugumo gerąsias praktikas](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Modelio konteksto protokolas (MCP) žymiai patobulėjo, įdiegus sustiprintas saugumo kontrolės priemones, apimančias tiek tradicinį programinės įrangos saugumą, tiek dirbtinio intelekto specifines grėsmes. Šis dokumentas pateikia išsamias saugumo kontrolės priemones saugioms MCP įgyvendinimo praktikoms 2025 m. gruodžio mėn.

## **PRIVALOMI saugumo reikalavimai**

### **Kritiniai draudimai pagal MCP specifikaciją:**

> **DRAUDŽIAMA**: MCP serveriai **NETURI** priimti jokių žetonų, kurie nebuvo aiškiai išduoti MCP serveriui  
>
> **DRAUDŽIAMA**: MCP serveriai **NETURI** naudoti sesijų autentifikacijai  
>
> **PRIVALOMA**: MCP serveriai, įgyvendinantys autorizaciją, **PRIVALO** patikrinti VISUS įeinančius užklausimus  
>
> **PRIVALOMA**: MCP proxy serveriai, naudojantys statinius kliento ID, **PRIVALO** gauti vartotojo sutikimą kiekvienam dinamiškai registruotam klientui

---

## 1. **Autentifikacijos ir autorizacijos kontrolės**

### **Išorinio tapatybės teikėjo integracija**

**Dabartinis MCP standartas (2025-06-18)** leidžia MCP serveriams deleguoti autentifikaciją išoriniams tapatybės teikėjams, kas yra reikšmingas saugumo patobulinimas:

### **Išorinio tapatybės teikėjo integracija**

**Dabartinis MCP standartas (2025-11-25)** leidžia MCP serveriams deleguoti autentifikaciją išoriniams tapatybės teikėjams, kas yra reikšmingas saugumo patobulinimas:

**Saugumo privalumai:**
1. **Pašalina individualios autentifikacijos rizikas**: sumažina pažeidžiamumo paviršių vengiant individualių autentifikacijos įgyvendinimų  
2. **Įmonių lygio saugumas**: naudoja patikimus tapatybės teikėjus, tokius kaip Microsoft Entra ID, su pažangiomis saugumo funkcijomis  
3. **Centralizuotas tapatybės valdymas**: supaprastina vartotojų gyvavimo ciklo valdymą, prieigos kontrolę ir atitikties auditą  
4. **Daugiaveiksmė autentifikacija**: paveldi MFA galimybes iš įmonių tapatybės teikėjų  
5. **Sąlyginės prieigos politikos**: naudoja rizika pagrįstą prieigos kontrolę ir adaptuotą autentifikaciją  

**Įgyvendinimo reikalavimai:**
- **Žetonų auditorijos patikra**: patikrinti, ar visi žetonai aiškiai išduoti MCP serveriui  
- **Išdavėjo patikra**: patvirtinti, kad žetono išdavėjas atitinka numatytą tapatybės teikėją  
- **Parašo patikra**: kriptografinis žetono vientisumo patvirtinimas  
- **Galiojimo termino laikymasis**: griežtas žetono galiojimo laiko ribų laikymasis  
- **Srities patikra**: užtikrinti, kad žetonai turi tinkamas teises prašomoms operacijoms  

### **Autorizacijos logikos saugumas**

**Kritinės kontrolės:**
- **Išsamūs autorizacijos auditai**: reguliarios saugumo apžvalgos visiems autorizacijos sprendimų taškams  
- **Saugūs numatytieji nustatymai**: prieiga uždraudžiama, kai autorizacijos logika negali priimti galutinio sprendimo  
- **Leidimų ribos**: aiškus skirtingų privilegijų lygių ir išteklių prieigos atskyrimas  
- **Auditavimo žurnalas**: pilnas visų autorizacijos sprendimų registravimas saugumo stebėsenai  
- **Reguliarūs prieigos peržiūros**: periodinis vartotojų teisių ir privilegijų patikrinimas  

## 2. **Žetonų saugumas ir anti-praėjimo kontrolės**

### **Žetonų praėjimo prevencija**

**Žetonų praėjimas yra aiškiai draudžiamas** MCP autorizacijos specifikacijoje dėl kritinių saugumo rizikų:

**Sprendžiamos saugumo rizikos:**
- **Kontrolės apeinimas**: apeina esmines saugumo kontrolės priemones, tokias kaip užklausų dažnio ribojimas, užklausų patikra ir srauto stebėjimas  
- **Atsakomybės praradimas**: neįmanoma identifikuoti kliento, kas gadina auditų įrašus ir incidentų tyrimą  
- **Proxy pagrindu vykdoma duomenų nutekėjimas**: leidžia kenkėjiškiems veikėjams naudoti serverius kaip proxy neautorizuotam duomenų prieigai  
- **Pasitikėjimo ribų pažeidimai**: pažeidžia žemyninės paslaugos pasitikėjimo žetonų kilme prielaidas  
- **Šoninė judėjimo galimybė**: kompromituoti žetonai keliuose serveriuose leidžia platesnį atakos plitimą  

**Įgyvendinimo kontrolės:**
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

### **Saugios žetonų valdymo praktikos**

**Gerosios praktikos:**
- **Trumpalaikiai žetonai**: sumažina ekspozicijos laiką dažnai keičiant žetonus  
- **Tikslaus laiko išdavimas**: žetonai išduodami tik tada, kai reikalingi konkrečioms operacijoms  
- **Saugus saugojimas**: naudoti aparatinės įrangos saugumo modulius (HSM) arba saugius raktų saugyklas  
- **Žetonų susiejimas**: susieti žetonus su konkrečiais klientais, sesijomis ar operacijomis, jei įmanoma  
- **Stebėjimas ir įspėjimai**: realaus laiko žetonų piktnaudžiavimo ar neautorizuotos prieigos modelių aptikimas  

## 3. **Sesijų saugumo kontrolės**

### **Sesijų užgrobimo prevencija**

**Sprendžiami atakų vektoriai:**
- **Sesijos užgrobimo promptų injekcija**: kenkėjiški įvykiai įterpiami į bendrą sesijos būseną  
- **Sesijos apsimetimas**: neautorizuotas pavogtų sesijos ID naudojimas autentifikacijos apeitimui  
- **Atnaujinamų srautų atakos**: serverio siunčiamų įvykių atnaujinimo išnaudojimas kenkėjiškam turinio įterpimui  

**Privalomos sesijų kontrolės:**
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

**Transporto saugumas:**
- **HTTPS privalomas**: visa sesijų komunikacija per TLS 1.3  
- **Saugūs slapukai**: HttpOnly, Secure, SameSite=Strict atributai  
- **Sertifikatų fiksavimas**: kritinėms jungtims, siekiant išvengti MITM atakų  

### **Valstybės ir bevalstės įgyvendinimo svarstymai**

**Valstybės pagrindu įgyvendinant:**
- Bendrinama sesijos būsena reikalauja papildomos apsaugos nuo injekcijų atakų  
- Eilės pagrindu valdomos sesijos reikalauja vientisumo patikros  
- Keli serverių egzemplioriai reikalauja saugaus sesijos būsenos sinchronizavimo  

**Bevalstės įgyvendinimui:**
- JWT arba panašūs žetonais pagrįsti sesijų valdymo metodai  
- Kriptografinė sesijos būsenos vientisumo patikra  
- Sumažintas atakos paviršius, bet reikalinga tvirta žetonų patikra  

## 4. **Dirbtinio intelekto specifinės saugumo kontrolės**

### **Promptų injekcijos gynyba**

**Microsoft Prompt Shields integracija:**
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

**Įgyvendinimo kontrolės:**
- **Įvesties valymas**: išsami visų vartotojo įvesties patikra ir filtravimas  
- **Turinio ribų apibrėžimas**: aiškus sistemos nurodymų ir vartotojo turinio atskyrimas  
- **Nurodymų hierarchija**: tinkamos pirmenybės taisyklės prieštaringiems nurodymams  
- **Išvesties stebėjimas**: potencialiai žalingos ar manipuliuotos išvesties aptikimas  

### **Įrankių užnuodijimo prevencija**

**Įrankių saugumo sistema:**
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

**Dinaminis įrankių valdymas:**
- **Patvirtinimo procesai**: aiškus vartotojo sutikimas įrankių pakeitimams  
- **Grąžinimo galimybės**: galimybė grįžti prie ankstesnių įrankių versijų  
- **Pakeitimų auditas**: pilna įrankių apibrėžimų pakeitimų istorija  
- **Rizikos vertinimas**: automatizuotas įrankių saugumo būklės vertinimas  

## 5. **Sumaišyto tarpininko atakos prevencija**

### **OAuth proxy saugumas**

**Atakų prevencijos kontrolės:**
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

**Įgyvendinimo reikalavimai:**
- **Vartotojo sutikimo patikra**: niekada nepraleisti sutikimo ekranų dinamiškai klientų registracijai  
- **Redirect URI patikra**: griežta baltųjų sąrašų patikra nukreipimo vietoms  
- **Autorizacijos kodo apsauga**: trumpalaikiai kodai su vienkartiniu naudojimu  
- **Kliento tapatybės patikra**: tvirta kliento kredencialų ir metaduomenų patikra  

## 6. **Įrankių vykdymo saugumas**

### **Smėlio dėžės ir izoliacija**

**Konteinerių pagrindu izoliacija:**
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

**Proceso izoliacija:**
- **Atskiri proceso kontekstai**: kiekvienas įrankio vykdymas izoliuotoje proceso erdvėje  
- **Tarpprocesinė komunikacija**: saugūs IPC mechanizmai su patikra  
- **Proceso stebėjimas**: vykdymo elgsenos analizė ir anomalijų aptikimas  
- **Išteklių apribojimai**: griežtos CPU, atminties ir I/O operacijų ribos  

### **Mažiausių privilegijų įgyvendinimas**

**Leidimų valdymas:**
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

## 7. **Tiekimo grandinės saugumo kontrolės**

### **Priklausomybių patikra**

**Išsamus komponentų saugumas:**
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

### **Nuolatinė stebėsena**

**Tiekimo grandinės grėsmių aptikimas:**
- **Priklausomybių sveikatos stebėsena**: nuolatinė visų priklausomybių saugumo problemų vertinimas  
- **Grėsmių žvalgybos integracija**: realaus laiko atnaujinimai apie kylančias tiekimo grandinės grėsmes  
- **Elgsenos analizė**: neįprastos elgsenos aptikimas išoriniame komponente  
- **Automatizuotas reagavimas**: nedelsiamas kompromituotų komponentų suvaldymas  

## 8. **Stebėjimo ir aptikimo kontrolės**

### **Saugumo informacijos ir įvykių valdymas (SIEM)**

**Išsami žurnalo strategija:**
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

### **Realiojo laiko grėsmių aptikimas**

**Elgsenos analizė:**
- **Vartotojų elgsenos analizė (UBA)**: neįprastų vartotojų prieigos modelių aptikimas  
- **Subjektų elgsenos analizė (EBA)**: MCP serverio ir įrankių elgsenos stebėjimas  
- **Mašininio mokymosi anomalijų aptikimas**: DI pagrįstas saugumo grėsmių identifikavimas  
- **Grėsmių žvalgybos koreliacija**: stebimų veiklų suderinimas su žinomais atakų modeliais  

## 9. **Incidentų valdymas ir atkūrimas**

### **Automatizuotos reagavimo galimybės**

**Nedelsiamo reagavimo veiksmai:**
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

### **Teisėsaugos galimybės**

**Tyrimų palaikymas:**
- **Audito takų išsaugojimas**: nekintamas žurnalo įrašymas su kriptografiniu vientisumu  
- **Įrodymų rinkimas**: automatizuotas susijusių saugumo artefaktų surinkimas  
- **Įvykių laiko juostos atkūrimas**: detali įvykių seka, vedanti prie saugumo incidentų  
- **Poveikio vertinimas**: kompromiso masto ir duomenų atskleidimo įvertinimas  

## **Pagrindiniai saugumo architektūros principai**

### **Gynyba gilumoje**
- **Keli saugumo sluoksniai**: nėra vieno silpno saugumo taško architektūroje  
- **Dubliuotos kontrolės**: persidengiančios saugumo priemonės kritinėms funkcijoms  
- **Saugūs numatytieji nustatymai**: saugūs numatytieji, kai sistemos susiduria su klaidomis ar atakomis  

### **Nulinio pasitikėjimo įgyvendinimas**
- **Niekada nepasitikėti, visada tikrinti**: nuolatinė visų subjektų ir užklausų patikra  
- **Mažiausių privilegijų principas**: minimalios prieigos teisės visiems komponentams  
- **Mikrosegmentacija**: smulkios tinklo ir prieigos kontrolės  

### **Nuolatinė saugumo evoliucija**
- **Grėsmių kraštovaizdžio adaptacija**: reguliariai atnaujinama, siekiant spręsti kylančias grėsmes  
- **Saugumo kontrolės efektyvumas**: nuolatinis kontrolės priemonių vertinimas ir tobulinimas  
- **Specifikacijos atitiktis**: suderinamumas su besikeičiančiais MCP saugumo standartais  

---

## **Įgyvendinimo ištekliai**

### **Oficiali MCP dokumentacija**
- [MCP specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP saugumo gerosios praktikos](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP autorizacijos specifikacija](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft saugumo sprendimai**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Saugumo standartai**
- [OAuth 2.0 saugumo gerosios praktikos (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 dideliems kalbos modeliams](https://genai.owasp.org/)
- [NIST kibernetinio saugumo sistema](https://www.nist.gov/cyberframework)

---

> **Svarbu**: Šios saugumo kontrolės atspindi dabartinę MCP specifikaciją (2025-06-18). Visada tikrinkite naujausią [oficialią dokumentaciją](https://spec.modelcontextprotocol.io/), nes standartai sparčiai keičiasi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
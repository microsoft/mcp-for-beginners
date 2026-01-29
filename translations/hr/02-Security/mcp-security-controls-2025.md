# MCP Sigurnosne Kontrole - Ažuriranje za prosinac 2025.

> **Trenutni standard**: Ovaj dokument odražava sigurnosne zahtjeve [MCP specifikacije 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) i službene [MCP sigurnosne najbolje prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) značajno je sazrio s poboljšanim sigurnosnim kontrolama koje pokrivaju i tradicionalnu softversku sigurnost i prijetnje specifične za AI. Ovaj dokument pruža sveobuhvatne sigurnosne kontrole za sigurne MCP implementacije od prosinca 2025.

## **OBAVEZNI Sigurnosni Zahtjevi**

### **Kritične zabrane iz MCP specifikacije:**

> **ZABRANJENO**: MCP serveri **NE SMIJU** prihvaćati bilo kakve tokene koji nisu izričito izdani za MCP server  
>
> **ZABRANJENO**: MCP serveri **NE SMIJU** koristiti sesije za autentikaciju  
>
> **OBAVEZNO**: MCP serveri koji implementiraju autorizaciju **MORAJU** provjeriti SVE dolazne zahtjeve  
>
> **OBAVEZNO**: MCP proxy serveri koji koriste statične ID-jeve klijenata **MORAJU** dobiti korisnički pristanak za svakog dinamički registriranog klijenta

---

## 1. **Kontrole Autentikacije i Autorizacije**

### **Integracija vanjskog pružatelja identiteta**

**Trenutni MCP standard (2025-06-18)** dopušta MCP serverima delegiranje autentikacije vanjskim pružateljima identiteta, što predstavlja značajno sigurnosno poboljšanje:

### **Integracija vanjskog pružatelja identiteta**

**Trenutni MCP standard (2025-11-25)** dopušta MCP serverima delegiranje autentikacije vanjskim pružateljima identiteta, što predstavlja značajno sigurnosno poboljšanje:

**Sigurnosne prednosti:**
1. **Eliminira rizike prilagođene autentikacije**: Smanjuje površinu ranjivosti izbjegavanjem prilagođenih implementacija autentikacije  
2. **Sigurnost razine poduzeća**: Koristi etablirane pružatelje identiteta poput Microsoft Entra ID s naprednim sigurnosnim značajkama  
3. **Centralizirano upravljanje identitetom**: Pojednostavljuje upravljanje životnim ciklusom korisnika, kontrolu pristupa i reviziju usklađenosti  
4. **Višefaktorska autentikacija**: Nasljeđuje MFA mogućnosti od pružatelja identiteta poduzeća  
5. **Politike uvjetnog pristupa**: Koristi kontrole pristupa temeljene na riziku i adaptivnu autentikaciju  

**Zahtjevi implementacije:**
- **Validacija publike tokena**: Provjeriti da su svi tokeni izričito izdani za MCP server  
- **Provjera izdavatelja**: Validirati da izdavatelj tokena odgovara očekivanom pružatelju identiteta  
- **Provjera potpisa**: Kriptografska validacija integriteta tokena  
- **Primjena isteka**: Strogo provođenje ograničenja trajanja tokena  
- **Validacija opsega**: Osigurati da tokeni sadrže odgovarajuće dozvole za tražene operacije  

### **Sigurnost autorizacijske logike**

**Kritične kontrole:**
- **Sveobuhvatne revizije autorizacije**: Redoviti sigurnosni pregledi svih točaka donošenja autorizacijskih odluka  
- **Sigurnosni zadani odgovori**: Odbij pristup kada autorizacijska logika ne može donijeti konačnu odluku  
- **Granice dozvola**: Jasna razdvojenost između različitih razina privilegija i pristupa resursima  
- **Evidencija revizije**: Potpuno bilježenje svih autorizacijskih odluka za sigurnosni nadzor  
- **Redoviti pregledi pristupa**: Periodična validacija korisničkih dozvola i dodjela privilegija  

## 2. **Sigurnost tokena i kontrole protiv prosljeđivanja**

### **Sprečavanje prosljeđivanja tokena**

**Prosljeđivanje tokena je izričito zabranjeno** u MCP specifikaciji autorizacije zbog kritičnih sigurnosnih rizika:

**Sigurnosni rizici koji se rješavaju:**
- **Zaobilaženje kontrole**: Zaobilazi ključne sigurnosne kontrole poput ograničenja brzine, validacije zahtjeva i nadzora prometa  
- **Raskid odgovornosti**: Onemogućuje identifikaciju klijenta, narušavajući revizijske tragove i istrage incidenata  
- **Izvlačenje podataka preko proxyja**: Omogućuje zlonamjernim akterima korištenje servera kao proxyja za neovlašteni pristup podacima  
- **Kršenje granica povjerenja**: Krši pretpostavke downstream servisa o podrijetlu tokena  
- **Lateralno kretanje**: Kompromitirani tokeni preko više servisa omogućuju širenje napada  

**Kontrole implementacije:**
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

### **Sigurni obrasci upravljanja tokenima**

**Najbolje prakse:**
- **Kratkotrajni tokeni**: Minimizirati izloženost čestim rotacijama tokena  
- **Izdavanje po potrebi**: Izdavati tokene samo kada su potrebni za specifične operacije  
- **Sigurno pohranjivanje**: Koristiti hardverske sigurnosne module (HSM) ili sigurne spremišta ključeva  
- **Povezivanje tokena**: Povezati tokene s određenim klijentima, sesijama ili operacijama gdje je moguće  
- **Nadzor i upozorenja**: Detekcija u stvarnom vremenu zloupotrebe tokena ili neovlaštenih obrazaca pristupa  

## 3. **Kontrole sigurnosti sesija**

### **Sprečavanje otmice sesije**

**Adversarni vektori:**
- **Umetanje prompta za otmicu sesije**: Zlonamjerne radnje umetnute u zajedničko stanje sesije  
- **Impersonacija sesije**: Neovlaštena upotreba ukradenih ID-jeva sesije za zaobilaženje autentikacije  
- **Napadi na nastavak streama**: Iskorištavanje nastavka događaja poslanih sa servera za umetanje zlonamjernog sadržaja  

**Obavezne kontrole sesije:**
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

**Sigurnost prijenosa:**
- **Primjena HTTPS-a**: Sva komunikacija sesije preko TLS 1.3  
- **Sigurni atributi kolačića**: HttpOnly, Secure, SameSite=Strict  
- **Pinning certifikata**: Za kritične veze radi sprječavanja MITM napada  

### **Razmatranja za stanje sesije (stateful) vs bez stanja (stateless)**

**Za implementacije sa stanjem:**
- Dijeljeno stanje sesije zahtijeva dodatnu zaštitu od napada umetanja  
- Upravljanje sesijama temeljeno na redovima zahtijeva provjeru integriteta  
- Više instanci servera zahtijeva sigurnu sinkronizaciju stanja sesije  

**Za implementacije bez stanja:**
- Upravljanje sesijama temeljeno na JWT ili sličnim tokenima  
- Kriptografska provjera integriteta stanja sesije  
- Smanjena površina napada, ali zahtijeva robusnu validaciju tokena  

## 4. **Sigurnosne kontrole specifične za AI**

### **Obrana od umetanja prompta**

**Integracija Microsoft Prompt Shields:**
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

**Kontrole implementacije:**
- **Sanitizacija unosa**: Sveobuhvatna validacija i filtriranje svih korisničkih unosa  
- **Definiranje granica sadržaja**: Jasna razdvojenost između sistemskih uputa i korisničkog sadržaja  
- **Hijerarhija uputa**: Ispravna pravila prioriteta za sukobljene upute  
- **Nadzor izlaza**: Detekcija potencijalno štetnih ili manipuliranih izlaza  

### **Sprečavanje trovanja alata**

**Okvir sigurnosti alata:**
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

**Dinamičko upravljanje alatima:**
- **Radni tokovi odobrenja**: Izričit korisnički pristanak za izmjene alata  
- **Mogućnosti povrata**: Sposobnost vraćanja na prethodne verzije alata  
- **Revizija promjena**: Potpuna povijest izmjena definicija alata  
- **Procjena rizika**: Automatska evaluacija sigurnosnog stanja alata  

## 5. **Sprečavanje napada zbunjenog zamjenika (Confused Deputy)**

### **Sigurnost OAuth proxyja**

**Kontrole za sprječavanje napada:**
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

**Zahtjevi implementacije:**
- **Provjera korisničkog pristanka**: Nikada ne preskakati zaslone pristanka za dinamičku registraciju klijenata  
- **Validacija URI-ja preusmjeravanja**: Stroga validacija odredišta preusmjeravanja na temelju bijele liste  
- **Zaštita autorizacijskog koda**: Kratkotrajni kodovi s provedbom jednokratne upotrebe  
- **Provjera identiteta klijenta**: Robusna validacija vjerodajnica i metapodataka klijenta  

## 6. **Sigurnost izvršavanja alata**

### **Sandboxing i izolacija**

**Izolacija temeljena na kontejnerima:**
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

**Izolacija procesa:**
- **Odvojeni kontekst procesa**: Svako izvršavanje alata u izoliranom prostoru procesa  
- **Međuprocesna komunikacija**: Sigurni IPC mehanizmi s validacijom  
- **Nadzor procesa**: Analiza ponašanja u runtime-u i detekcija anomalija  
- **Primjena ograničenja resursa**: Stroga ograničenja CPU-a, memorije i I/O operacija  

### **Implementacija principa najmanjih privilegija**

**Upravljanje dozvolama:**
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

## 7. **Sigurnosne kontrole lanca opskrbe**

### **Verifikacija ovisnosti**

**Sveobuhvatna sigurnost komponenti:**
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

### **Kontinuirani nadzor**

**Detekcija prijetnji u lancu opskrbe:**
- **Praćenje zdravlja ovisnosti**: Kontinuirana procjena svih ovisnosti zbog sigurnosnih problema  
- **Integracija obavještavanja o prijetnjama**: Ažuriranja u stvarnom vremenu o novim prijetnjama u lancu opskrbe  
- **Analiza ponašanja**: Detekcija neuobičajenog ponašanja u vanjskim komponentama  
- **Automatski odgovor**: Trenutno suzbijanje kompromitiranih komponenti  

## 8. **Kontrole nadzora i detekcije**

### **Sigurnosni informacijsk i sustav za upravljanje događajima (SIEM)**

**Sveobuhvatna strategija bilježenja:**
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

### **Detekcija prijetnji u stvarnom vremenu**

**Analitika ponašanja:**
- **Analitika ponašanja korisnika (UBA)**: Detekcija neuobičajenih obrazaca pristupa korisnika  
- **Analitika ponašanja entiteta (EBA)**: Nadzor ponašanja MCP servera i alata  
- **Detekcija anomalija pomoću strojnog učenja**: AI-pokretano prepoznavanje sigurnosnih prijetnji  
- **Korelacija obavještavanja o prijetnjama**: Usklađivanje opaženih aktivnosti s poznatim obrascima napada  

## 9. **Odgovor na incidente i oporavak**

### **Automatizirane mogućnosti odgovora**

**Neposredne akcije odgovora:**
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

### **Forenzičke mogućnosti**

**Podrška istrazi:**
- **Očuvanje revizijskog traga**: Nemjenjivo bilježenje s kriptografskom integritetom  
- **Prikupljanje dokaza**: Automatsko prikupljanje relevantnih sigurnosnih artefakata  
- **Rekonstrukcija vremenske linije**: Detaljan slijed događaja koji su doveli do sigurnosnih incidenata  
- **Procjena utjecaja**: Evaluacija opsega kompromisa i izloženosti podataka  

## **Ključni principi sigurnosne arhitekture**

### **Obrana u dubinu**
- **Višestruki sigurnosni slojevi**: Nema jedne točke otkaza u sigurnosnoj arhitekturi  
- **Redundantne kontrole**: Preklapajuće sigurnosne mjere za kritične funkcije  
- **Sigurnosni zadani mehanizmi**: Sigurni zadani postavci kada sustavi naiđu na pogreške ili napade  

### **Implementacija Zero Trust**
- **Nikada ne vjeruj, uvijek provjeri**: Kontinuirana validacija svih entiteta i zahtjeva  
- **Princip najmanjih privilegija**: Minimalna prava pristupa za sve komponente  
- **Mikrosegmentacija**: Granularne mrežne i pristupne kontrole  

### **Kontinuirana evolucija sigurnosti**
- **Prilagodba prijetnjama**: Redovita ažuriranja za rješavanje novih prijetnji  
- **Učinkovitost sigurnosnih kontrola**: Stalna evaluacija i poboljšanje kontrola  
- **Usklađenost sa specifikacijom**: Poravnavanje s razvojem MCP sigurnosnih standarda  

---

## **Resursi za implementaciju**

### **Službena MCP dokumentacija**
- [MCP specifikacija (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP sigurnosne najbolje prakse](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP specifikacija autorizacije](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft sigurnosna rješenja**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sigurnosni standardi**
- [OAuth 2.0 sigurnosne najbolje prakse (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 za velike jezične modele](https://genai.owasp.org/)
- [NIST okvir za kibernetičku sigurnost](https://www.nist.gov/cyberframework)

---

> **Važno**: Ove sigurnosne kontrole odražavaju trenutnu MCP specifikaciju (2025-06-18). Uvijek provjerite najnoviju [službenu dokumentaciju](https://spec.modelcontextprotocol.io/) jer se standardi brzo razvijaju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Security Controls - Actualizare Decembrie 2025

> **Standard Curent**: Acest document reflectă cerințele de securitate din [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) și [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) oficiale.

Model Context Protocol (MCP) a evoluat semnificativ cu controale de securitate îmbunătățite care abordează atât securitatea software tradițională, cât și amenințările specifice AI. Acest document oferă controale de securitate cuprinzătoare pentru implementări MCP sigure la data de decembrie 2025.

## **Cerințe Obligatorii de Securitate**

### **Interdicții Critice din Specificația MCP:**

> **INTERZIS**: Serverele MCP **NU TREBUIE** să accepte niciun token care nu a fost emis explicit pentru serverul MCP  
>
> **PROHIBIT**: Serverele MCP **NU TREBUIE** să utilizeze sesiuni pentru autentificare  
>
> **CERUT**: Serverele MCP care implementează autorizarea **TREBUIE** să verifice TOATE cererile primite  
>
> **OBLIGATORIU**: Serverele proxy MCP care folosesc ID-uri statice de client **TREBUIE** să obțină consimțământul utilizatorului pentru fiecare client înregistrat dinamic

---

## 1. **Controale de Autentificare și Autorizare**

### **Integrarea Furnizorului de Identitate Extern**

**Standardul MCP Curent (2025-06-18)** permite serverelor MCP să delege autentificarea către furnizori externi de identitate, reprezentând o îmbunătățire semnificativă a securității:

### **Integrarea Furnizorului de Identitate Extern**

**Standardul MCP Curent (2025-11-25)** permite serverelor MCP să delege autentificarea către furnizori externi de identitate, reprezentând o îmbunătățire semnificativă a securității:

**Beneficii de Securitate:**
1. **Elimină Riscurile Autentificării Personalizate**: Reduce suprafața de vulnerabilitate evitând implementările personalizate de autentificare  
2. **Securitate de Nivel Enterprise**: Folosește furnizori de identitate consacrați precum Microsoft Entra ID cu funcții avansate de securitate  
3. **Management Centralizat al Identității**: Simplifică gestionarea ciclului de viață al utilizatorilor, controlul accesului și auditul conformității  
4. **Autentificare Multi-Factor**: Moștenește capabilitățile MFA de la furnizorii enterprise de identitate  
5. **Politici de Acces Condiționat**: Beneficiază de controale de acces bazate pe risc și autentificare adaptivă

**Cerințe de Implementare:**
- **Validarea Audienței Tokenului**: Verifică că toate tokenurile sunt emise explicit pentru serverul MCP  
- **Verificarea Emitentului**: Validarea că emitentul tokenului corespunde furnizorului de identitate așteptat  
- **Verificarea Semnăturii**: Validare criptografică a integrității tokenului  
- **Aplicarea Expirării**: Aplicarea strictă a limitelor de durată a tokenului  
- **Validarea Domeniului (Scope)**: Asigură că tokenurile conțin permisiunile adecvate pentru operațiile solicitate

### **Securitatea Logicii de Autorizare**

**Controale Critice:**
- **Audituri Complete de Autorizare**: Revizuiri regulate de securitate ale tuturor punctelor de decizie de autorizare  
- **Implicit Deny (Fail-Safe Defaults)**: Refuză accesul când logica de autorizare nu poate lua o decizie definitivă  
- **Limite de Permisiuni**: Separare clară între diferite niveluri de privilegii și acces la resurse  
- **Jurnalizare pentru Audit**: Înregistrare completă a tuturor deciziilor de autorizare pentru monitorizarea securității  
- **Revizuiri Periodice ale Accesului**: Validarea periodică a permisiunilor utilizatorilor și a atribuțiilor de privilegii

## 2. **Securitatea Tokenurilor & Controale Anti-Passthrough**

### **Prevenirea Passthrough-ului Tokenurilor**

**Passthrough-ul tokenurilor este explicit interzis** în Specificația de Autorizare MCP din cauza riscurilor critice de securitate:

**Riscuri de Securitate Abordate:**
- **Ocolirea Controlului**: Evită controalele esențiale de securitate precum limitarea ratei, validarea cererilor și monitorizarea traficului  
- **Lipsa Responsabilității**: Face imposibilă identificarea clientului, corupând traseele de audit și investigațiile incidentelor  
- **Exfiltrare prin Proxy**: Permite actorilor rău intenționați să folosească serverele ca proxy-uri pentru acces neautorizat la date  
- **Încălcări ale Limitelor de Încredere**: Rupe presupunerile serviciilor downstream despre originea tokenurilor  
- **Mișcare Laterală**: Tokenurile compromise pe mai multe servicii permit extinderea atacului

**Controale de Implementare:**
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

### **Modele Sigure de Management al Tokenurilor**

**Cele Mai Bune Practici:**
- **Tokenuri cu Durată Scurtă**: Minimizează fereastra de expunere prin rotație frecventă a tokenurilor  
- **Emitere Just-in-Time**: Emite tokenuri doar când sunt necesare pentru operații specifice  
- **Stocare Securizată**: Folosește module hardware de securitate (HSM) sau seifuri de chei securizate  
- **Legarea Tokenurilor**: Leagă tokenurile de clienți, sesiuni sau operații specifice, acolo unde este posibil  
- **Monitorizare și Alertare**: Detectare în timp real a utilizării abuzive a tokenurilor sau a accesului neautorizat

## 3. **Controale de Securitate pentru Sesiuni**

### **Prevenirea Deturnării Sesiunii**

**Vectori de Atac Abordați:**
- **Injectarea de Prompturi în Deturnarea Sesiunii**: Evenimente malițioase injectate în starea sesiunii partajate  
- **Impersonarea Sesiunii**: Utilizarea neautorizată a ID-urilor de sesiune furate pentru a ocoli autentificarea  
- **Atacuri cu Reluare a Fluxului**: Exploatarea reluării evenimentelor trimise de server pentru injectarea de conținut malițios

**Controale Obligatorii pentru Sesiuni:**
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

**Securitatea Transportului:**
- **Aplicarea HTTPS**: Toată comunicarea sesiunii prin TLS 1.3  
- **Atribute Sigure pentru Cookie-uri**: HttpOnly, Secure, SameSite=Strict  
- **Pinning-ul Certificatului**: Pentru conexiuni critice pentru a preveni atacurile MITM

### **Considerații Stateful vs Stateless**

**Pentru Implementări Stateful:**
- Starea sesiunii partajate necesită protecție suplimentară împotriva atacurilor de injectare  
- Managementul sesiunii bazat pe coadă necesită verificarea integrității  
- Mai multe instanțe de server necesită sincronizare securizată a stării sesiunii

**Pentru Implementări Stateless:**
- Managementul sesiunii bazat pe JWT sau tokenuri similare  
- Verificare criptografică a integrității stării sesiunii  
- Suprafață de atac redusă, dar necesită validare robustă a tokenurilor

## 4. **Controale de Securitate Specifice AI**

### **Apărarea împotriva Injectării de Prompturi**

**Integrarea Microsoft Prompt Shields:**
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

**Controale de Implementare:**
- **Sanitizarea Inputului**: Validare și filtrare cuprinzătoare a tuturor intrărilor utilizatorului  
- **Definirea Limitelor de Conținut**: Separare clară între instrucțiunile sistemului și conținutul utilizatorului  
- **Ierarhia Instrucțiunilor**: Reguli corecte de precedență pentru instrucțiunile conflictuale  
- **Monitorizarea Outputului**: Detectarea outputurilor potențial dăunătoare sau manipulate

### **Prevenirea Otrăvirii Uneltelor**

**Cadrul de Securitate pentru Unelte:**
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

**Management Dinamic al Uneltelor:**
- **Fluxuri de Aprobare**: Consimțământ explicit al utilizatorului pentru modificările uneltelor  
- **Capabilități de Rollback**: Posibilitatea de a reveni la versiuni anterioare ale uneltelor  
- **Auditarea Modificărilor**: Istoric complet al modificărilor definițiilor uneltelor  
- **Evaluarea Riscurilor**: Evaluare automată a posturii de securitate a uneltelor

## 5. **Prevenirea Atacului Confused Deputy**

### **Securitatea Proxy-ului OAuth**

**Controale pentru Prevenirea Atacului:**
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

**Cerințe de Implementare:**
- **Verificarea Consimțământului Utilizatorului**: Nu sări niciodată peste ecranele de consimțământ pentru înregistrarea dinamică a clientului  
- **Validarea Redirect URI**: Validare strictă pe bază de listă albă a destinațiilor de redirecționare  
- **Protecția Codului de Autorizare**: Coduri cu durată scurtă și aplicare de utilizare unică  
- **Verificarea Identității Clientului**: Validare robustă a acreditărilor și metadatelor clientului

## 6. **Securitatea Execuției Uneltelor**

### **Izolare și Sandbox**

**Izolare Bazată pe Containere:**
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

**Izolarea Proceselor:**
- **Contexturi Separate de Proces**: Fiecare execuție a uneltei în spațiu de proces izolat  
- **Comunicare Inter-Proces (IPC)**: Mecanisme IPC securizate cu validare  
- **Monitorizarea Proceselor**: Analiză comportamentală la runtime și detectarea anomaliilor  
- **Aplicarea Resurselor**: Limite stricte pentru CPU, memorie și operațiuni I/O

### **Implementarea Principiului Celor Mai Mici Privilegii**

**Managementul Permisiunilor:**
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

## 7. **Controale de Securitate pentru Lanțul de Aprovizionare**

### **Verificarea Dependențelor**

**Securitate Completă a Componentelor:**
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

### **Monitorizare Continuă**

**Detectarea Amenințărilor în Lanțul de Aprovizionare:**
- **Monitorizarea Sănătății Dependențelor**: Evaluare continuă a tuturor dependențelor pentru probleme de securitate  
- **Integrarea Informațiilor despre Amenințări**: Actualizări în timp real despre amenințările emergente din lanțul de aprovizionare  
- **Analiză Comportamentală**: Detectarea comportamentului neobișnuit în componentele externe  
- **Răspuns Automat**: Contenția imediată a componentelor compromise

## 8. **Controale de Monitorizare și Detectare**

### **Managementul Informațiilor și Evenimentelor de Securitate (SIEM)**

**Strategie Completă de Jurnalizare:**
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

### **Detectarea Amenințărilor în Timp Real**

**Analiză Comportamentală:**
- **Analiza Comportamentului Utilizatorului (UBA)**: Detectarea tiparelor neobișnuite de acces ale utilizatorilor  
- **Analiza Comportamentului Entităților (EBA)**: Monitorizarea comportamentului serverului MCP și al uneltelor  
- **Detectarea Anomaliilor prin Machine Learning**: Identificarea amenințărilor de securitate asistată de AI  
- **Corelarea Informațiilor despre Amenințări**: Potrivirea activităților observate cu tipare cunoscute de atac

## 9. **Răspuns la Incidente și Recuperare**

### **Capabilități de Răspuns Automat**

**Acțiuni Imediate de Răspuns:**
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

### **Capabilități Forensice**

**Suport pentru Investigații:**
- **Păstrarea Traseului de Audit**: Jurnalizare imuabilă cu integritate criptografică  
- **Colectarea Dovezilor**: Colectare automată a artefactelor relevante de securitate  
- **Reconstrucția Cronologiei**: Secvență detaliată a evenimentelor care au condus la incidentele de securitate  
- **Evaluarea Impactului**: Evaluarea amploarei compromiterii și expunerii datelor

## **Principii Cheie ale Arhitecturii de Securitate**

### **Apărare în Profunzime**
- **Straturi Multiple de Securitate**: Fără punct unic de eșec în arhitectura de securitate  
- **Controale Redundante**: Măsuri de securitate suprapuse pentru funcții critice  
- **Mecanisme Fail-Safe**: Setări implicite sigure când sistemele întâmpină erori sau atacuri

### **Implementarea Zero Trust**
- **Niciodată Nu Aveți Încredere, Verificați Întotdeauna**: Validare continuă a tuturor entităților și cererilor  
- **Principiul Celor Mai Mici Privilegii**: Drepturi minime de acces pentru toate componentele  
- **Micro-Segmentare**: Controale granulare de rețea și acces

### **Evoluția Continuă a Securității**
- **Adaptarea la Peisajul Amenințărilor**: Actualizări regulate pentru a aborda amenințările emergente  
- **Eficacitatea Controlului de Securitate**: Evaluare și îmbunătățire continuă a controalelor  
- **Conformitatea cu Specificațiile**: Aliniere cu standardele MCP de securitate în evoluție

---

## **Resurse pentru Implementare**

### **Documentația Oficială MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Soluții de Securitate Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standarde de Securitate**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Important**: Aceste controale de securitate reflectă specificația MCP curentă (2025-06-18). Verificați întotdeauna conform celei mai recente [documentații oficiale](https://spec.modelcontextprotocol.io/) deoarece standardele continuă să evolueze rapid.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
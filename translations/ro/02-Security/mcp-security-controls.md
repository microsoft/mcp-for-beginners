# Controale de Securitate MCP - Actualizare Septembrie 2026

> **Standard curent:** Acest document reflectă
> [Specificația MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> și
> [Cele mai bune practici de securitate MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protocolul Model Context (MCP) a evoluat semnificativ cu controale de securitate îmbunătățite care abordează atât securitatea software tradițională, cât și amenințările specifice AI. Acest document oferă controale de securitate cuprinzătoare pentru implementări sigure MCP, aliniate cu cadrul OWASP MCP Top 10.

## 🏔️ Training Practic de Securitate

Pentru experiență practică în implementarea securității, recomandăm **[Atelierul MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - o expediție ghidată completă pentru securizarea serverelor MCP în Azure folosind metodologia „vulnerabil → exploatat → remediat → validat”.

Toate controalele de securitate din acest document sunt aliniate cu **[Ghidul de Securitate OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)**, care oferă arhitecturi de referință și indicații de implementare specifice Azure pentru riscurile OWASP MCP Top 10.

## **Cerințe Obligatorii de Securitate**

### **Prohibiții Critice din Specificația MCP:**

> **INTERZIS**: Serverele MCP **NU TREBUIE** să accepte niciun token care nu a fost emis explicit pentru serverul MCP
>
> **PROHIBIT**: Serverele MCP **NU TREBUIE** să utilizeze sesiuni pentru autentificare  
>
> **OBLIGATORIU**: Serverele MCP care implementează autorizarea **TREBUIE** să verifice TOATE cererile primite
>
> **MANDATORIU**: Serverele proxy MCP care folosesc un ID client terț static
> **TREBUIE** să obțină consimțământ pentru fiecare client MCP înainte de a transmite autorizarea

---

## 1. **Controale de Autentificare și Autorizare**

### **Integrarea Furnizorilor Externi de Identitate**

**Specificația MCP `2026-07-28`** permite serverelor MCP să delege
autentificarea către furnizori externi de identitate. Autorizarea pentru transporturile HTTP
este evaluată pentru fiecare cerere; serverele locale stdio obțin în schimb acreditările
din mediul lor.

**Risc OWASP MCP Abordat**: [MCP07 - Autentificare și Autorizare Insuficiente](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Beneficii de Securitate:**
1. **Elimină Riscurile Autentificării Personalizate**: Reduce suprafața de vulnerabilitate evitând implementările personalizate de autentificare
2. **Securitate de Nivel Enterprise**: Folosește furnizori de identitate consacrați precum Microsoft Entra ID cu caracteristici avansate de securitate
3. **Management Centralizat al Identității**: Simplifică gestionarea ciclului de viață al utilizatorului, controlul accesului și auditul conformității
4. **Autentificare Multi-Factor (MFA)**: Moștenește capabilitățile MFA de la furnizorii de identitate enterprise
5. **Politici de Acces Condiționat**: Beneficiază de controale de acces bazate pe risc și autentificare adaptivă

**Cerințe de Implementare:**
- **Înregistrarea Clientului**: Preferabil Documente Metadata Client sau
  preînregistrare; utilizați înregistrarea dinamică a clientului învechită doar pentru
  compatibilitate
- **Validarea Publicului Tokenului**: Verificați că toate tokenurile sunt emise explicit pentru serverul MCP
- **Verificarea Emitentului**: Validați că emitentul tokenului corespunde furnizorului de identitate așteptat
- **Verificarea Semnăturii**: Validare criptografică a integrității tokenului
- **Respectarea Expirării**: Aplicarea strictă a limitelor de durată a tokenului
- **Validarea Domeniului (Scope)**: Asigurați-vă că tokenurile conțin permisiunile adecvate pentru operațiile solicitate

### **Securitatea Logicii de Autorizare**


**Controale Critice:**
- **Audituri Comprehensive de Autorizare**: Revizuiri regulate de securitate pentru toate punctele de decizie în autorizare
- **Setări Implicite Fail-Safe**: Respingerea accesului când logica de autorizare nu poate lua o decizie definitivă
- **Frontiere de Permisiuni**: Separare clară între diferite niveluri de privilegii și accesul la resurse
- **Înregistrare Audit**: Înregistrare completă a tuturor deciziilor de autorizare pentru monitorizarea securității
- **Revizuiri Regulate ale Accesului**: Validarea periodică a permisiunilor utilizatorilor și atribuirea privilegiilor

## 2. **Securitatea Tokenurilor & Controale Anti-Passthrough**

**Risc OWASP MCP Abordat**: [MCP01 - Gestionarea Neadecvată a Tokenurilor & Expunerea Secretelor](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Prevenirea Passthrough-ului Tokenurilor**

**Passthrough-ul tokenurilor este explicit interzis** în Specificația MCP de Autorizare din cauza riscurilor critice de securitate:

**Riscuri de Securitate Abordate:**
- **Ocolirea Controlului**: Ocolește controalele esențiale de securitate precum limitarea ratei, validarea cererilor și monitorizarea traficului
- **Pierderea Responsabilității**: Face imposibilă identificarea clientului, corupând jurnalele de audit și investigarea incidentelor
- **Exfiltrare prin Proxy**: Permite actorilor rău intenționați să folosească servere ca proxy pentru acces neautorizat la date
- **Încălcări ale Frontierei de Încredere**: Rupe presupunerile de încredere ale serviciilor downstream privind originea tokenurilor
- **Mișcare Laterală**: Tokenurile compromise în mai multe servicii permit extinderea atacului

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

**Cele mai bune practici:**
- **Tokenuri cu Durată Scurtă de Viață**: Minimizează fereastra de expunere prin rotații frecvente ale tokenurilor
- **Emitere Just-in-Time**: Emite tokenuri doar când sunt necesare pentru operațiuni specifice
- **Stocare Securizată**: Utilizează module hardware de securitate (HSM-uri) sau seifuri de chei securizate
- **Legarea Tokenului**: Validează audiența și emițătorul tokenului pentru MCP-ul destinat
  resursa, clientul și operațiunea
- **Monitorizare & Alertare**: Detectare în timp real a utilizării abuzive a tokenurilor sau modelelor de acces neautorizat

## 3. **Controale de Securitate pentru Starea Aplicației**

### **Prevenirea Deturnării Handle-urilor de Stare**

**Vectori de Atac Abordați:**
- **Ghicirea Handle-urilor**: Identificatorii predictibili expun starea altui apelant
- **Reutilizare între Utilizatori**: Un handle furat este folosit cu o identitate diferită
- **Autorizare Implicită**: Poseziunea unui handle este tratată incorect ca
  dovadă de acces

**Controale pentru Handle-ul Stării:**

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

**Securitate de Transport:**
- **Impunerea HTTPS**: Solicită HTTPS pentru transporturile HTTP la distanță
- **Gestionarea Credentialelor**: Trimite și validează autorizarea la fiecare cerere HTTP
- **Izolarea stdio**: Protejează serverele locale stdio prin izolare de proces și
  controale de credentiale la nivel de mediu

### **Considerații Stateful vs Stateless**

MCP `2026-07-28` este stateless la nivelul protocolului. Aplicațiile pot totuși
menține starea prin returnarea unui handle explicit dintr-un apel de instrument și acceptarea
acestuia ca argument obișnuit la apeluri ulterioare.

- Stocați starea independent de orice conexiune de transport.
- Legați handle-urile de stare la principalul autentificat pe server.
- Tratați un handle ca pe un nume, nu ca pe o acreditare bearer.
- Definiți comportamentul de expirare și recuperare pentru handle-urile învechite.

## 4. **Controale de Securitate Specifice AI**

**Riscuri OWASP MCP Abordate**:

- [MCP06 - Subversiunea fluxului de intenție](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Otrăvirea uneltelor](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Injecția și execuția comenzilor](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Apărarea împotriva injecției în prompt**

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

**Controale de implementare:**
- **Securizarea intrărilor**: Validare și filtrare cuprinzătoare a tuturor intrărilor utilizatorului
- **Definirea limitelor conținutului**: Separare clară între instrucțiunile sistemului și conținutul utilizatorului
- **Ierarhia instrucțiunilor**: Reguli corespunzătoare pentru prioritizarea instrucțiunilor conflictuale
- **Monitorizarea ieșirilor**: Detectarea ieșirilor potențial dăunătoare sau manipulate

### **Prevenirea otrăvirii uneltelor**

**Cadrul de securitate a uneltelor:**
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

**Gestionarea dinamică a uneltelor:**
- **Fluxuri de aprobare**: Consimțământ explicit al utilizatorului pentru modificările uneltelor
- **Capabilități de revenire**: Posibilitatea de a reveni la versiunile anterioare ale uneltelor
- **Auditarea modificărilor**: Istoric complet al modificărilor definițiilor uneltelor
- **Evaluarea riscurilor**: Evaluare automată a poziției de securitate a uneltelor

## 5. **Prevenirea atacului de tip Confused Deputy**

### **Securitatea OAuth Proxy**

**Controale pentru prevenirea atacului:**
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

**Cerinte de implementare:**
- **Înregistrarea clientului**: Se preferă pre-înregistrarea sau documentele metadate Client ID
  Tratați înregistrarea dinamică a clientului ca o soluție de compatibilitate fallback
- **Verificarea consimțământului utilizatorului**: Proxy-urile MCP care folosesc un client terț static
  trebuie să obțină consimțământ per-client înainte de a redirecționa autorizarea
- **Validarea URI de redirecționare**: Validare strictă bazată pe lista albă a destinațiilor de redirecționare
- **Protecția codului de autorizare**: Coduri cu durata scurtă și utilizare unică
- **Verificarea identității clientului**: Validare robustă a acreditărilor și metadatelor clientului

## 6. **Securitatea execuției uneltelor**

### **Sandboxing și izolare**

**Izolare bazată pe containere:**
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

**Izolarea proceselor:**
- **Procese separate**: Fiecare execuție a unei unelte în spațiu de proces izolat
- **Comunicare între procese**: Mecanisme IPC sigure cu validare
- **Monitorizarea proceselor**: Analiză a comportamentului la rulare și detectarea anomaliilor
- **Aplicarea limitelor resurselor**: Limite stricte pentru CPU, memorie și operațiuni I/O

### **Implementarea principiului cel mai mic privilegiu**

**Gestionarea permisiunilor:**
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

## 7. **Controale de securitate pentru lanțul de aprovizionare**

**Risc OWASP MCP abordat**: [MCP04 - Atacuri asupra lanțului de aprovizionare software & manipularea dependențelor](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verificarea dependențelor**

**Securitatea completă a componentelor:**
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

### **Monitorizare continuă**

**Detectarea amenințărilor în lanțul de aprovizionare:**
- **Monitorizarea sănătății dependențelor**: Evaluare continuă a tuturor dependențelor pentru probleme de securitate
- **Integrarea informațiilor despre amenințări**: Actualizări în timp real privind amenințările emergente din lanțul de aprovizionare
- **Analiza comportamentală**: Detectarea comportamentului neobișnuit în componentele externe
- **Răspuns automatizat**: Contenție imediată a componentelor compromise

## 8. **Controale de monitorizare și detectare**

**Risc OWASP MCP abordat**: [MCP08 - Lipsa auditului și telemetriei](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Gestionarea informațiilor și evenimentelor de securitate (SIEM)**

**Strategie cuprinzătoare de logare:**
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

### **Detectarea amenințărilor în timp real**

**Analiza comportamentală:**
- **Analiza comportamentului utilizatorului (UBA)**: Detectarea modelelor neobișnuite de acces ale utilizatorilor
- **Analiza comportamentului entităților (EBA)**: Monitorizarea comportamentului serverului MCP și al uneltelor
- **Detectarea anomaliilor prin machine learning**: Identificarea amenințărilor de securitate susținută de AI
- **Corelarea informațiilor despre amenințări**: Potrivirea activităților observate cu modele cunoscute de atac

## 9. **Răspuns la incidente și recuperare**

### **Capabilități de răspuns automatizat**

**Acțiuni imediate de răspuns:**
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

### **Capabilități de investigație criminalistică**

**Suport pentru investigație:**
- **Păstrarea traseului de audit**: Log-uri imuabile cu integritate criptografică
- **Colectarea dovezilor**: Colectare automată a artefactelor relevante de securitate
- **Reconstrucția cronologiei**: Secvență detaliată a evenimentelor care au dus la incidentele de securitate
- **Evaluarea impactului**: Evaluarea ariei de compromitere și expunerii datelor

## **Principii cheie de arhitectură de securitate**

### **Apărare în profunzime**
- **Straturi multiple de securitate**: Nu există un singur punct de eșec în arhitectura de securitate
- **Controale redundante**: Măsuri suprapuse de securitate pentru funcțiile critice
- **Mecanisme fail-safe**: Configurări implicite sigure când sistemele întâlnesc erori sau atacuri

### **Implementarea Zero Trust**
- **Nu aveți niciodată încredere, verificați întotdeauna**: Validare continuă a tuturor entităților și solicitărilor
- **Principiul celui mai mic privilegiu**: Drepturi de acces minime pentru toate componentele
- **Micro-segmentare**: Controale granulare ale rețelei și accesului

### **Evoluția continuă a securității**
- **Adaptarea la peisajul amenințărilor**: Actualizări regulate pentru a aborda amenințările emergente
- **Eficacitatea controalelor de securitate**: Evaluare continuă și îmbunătățirea controalelor
- **Conformitatea cu specificațiile**: Alinierea cu standardele MCP de securitate în evoluție

---

## **Resurse pentru implementare**

### **Documentația oficială MCP**
- [Specificația MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Cele mai bune practici de securitate MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specificația de autorizare MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Resurse de securitate OWASP MCP**
- [Ghidul de securitate OWASP MCP pentru Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 cu implementare Azure detaliată
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Riscurile oficiale de securitate OWASP MCP
- [Workshop-ul Summit-ului MCP de Securitate (Sherpa)](https://azure-samples.github.io/sherpa/) - Instruire practică în securitate pentru MCP pe Azure

### **Soluții de securitate Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Securitatea conținutului Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standarde de securitate**
- [Cele mai bune practici de securitate OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 pentru Modele Mari de Limbaj](https://genai.owasp.org/)

- [Cadrul de Securitate Cibernetică NIST](https://www.nist.gov/cyberframework)

---

> **Important:** Aceste controale de securitate reflectă Specificația MCP
> `2026-07-28`. Verificați întotdeauna cu
> [documentația oficială curentă](https://modelcontextprotocol.io/specification/2026-07-28/)
> pe măsură ce standardele continuă să evolueze.

## Ce urmează

- Întoarce-te la: [Prezentarea Modulului de Securitate](./README.md)
- Continuă către: [Modulul 3: Începuturi](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Säkerhetskontroller - Uppdatering december 2025

> **Aktuell standard**: Detta dokument speglar [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) säkerhetskrav och officiella [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) har mognat avsevärt med förbättrade säkerhetskontroller som adresserar både traditionell mjukvarusäkerhet och AI-specifika hot. Detta dokument tillhandahåller omfattande säkerhetskontroller för säkra MCP-implementationer från och med december 2025.

## **OBLIGATORISKA säkerhetskrav**

### **Kritiska förbud från MCP-specifikationen:**

> **FÖRBJUDET**: MCP-servrar **FÅR INTE** acceptera några tokens som inte uttryckligen utfärdats för MCP-servern  
>
> **FÖRBJUDET**: MCP-servrar **FÅR INTE** använda sessioner för autentisering  
>
> **KRÄVS**: MCP-servrar som implementerar auktorisering **MÅSTE** verifiera ALLA inkommande förfrågningar  
>
> **OBLIGATORISKT**: MCP-proxyservrar som använder statiska klient-ID:n **MÅSTE** inhämta användarens samtycke för varje dynamiskt registrerad klient

---

## 1. **Autentiserings- och auktoriseringskontroller**

### **Integration med extern identitetsleverantör**

**Aktuell MCP-standard (2025-06-18)** tillåter MCP-servrar att delegera autentisering till externa identitetsleverantörer, vilket utgör en betydande säkerhetsförbättring:

### **Integration med extern identitetsleverantör**

**Aktuell MCP-standard (2025-11-25)** tillåter MCP-servrar att delegera autentisering till externa identitetsleverantörer, vilket utgör en betydande säkerhetsförbättring:

**Säkerhetsfördelar:**
1. **Eliminerar risker med egen autentisering**: Minskar sårbarhetsytan genom att undvika egna autentiseringsimplementationer  
2. **Företagsklassad säkerhet**: Utnyttjar etablerade identitetsleverantörer som Microsoft Entra ID med avancerade säkerhetsfunktioner  
3. **Centraliserad identitetshantering**: Förenklar användarlivscykelhantering, åtkomstkontroll och efterlevnadsrevision  
4. **Multifaktorautentisering**: Ärver MFA-funktioner från företagsidentitetsleverantörer  
5. **Villkorliga åtkomstpolicyer**: Drar nytta av riskbaserade åtkomstkontroller och adaptiv autentisering

**Implementeringskrav:**
- **Validering av tokenmottagare**: Verifiera att alla tokens uttryckligen är utfärdade för MCP-servern  
- **Utfärdarbehörighet**: Validera att tokenutfärdaren matchar förväntad identitetsleverantör  
- **Signaturverifiering**: Kryptografisk validering av tokenintegritet  
- **Utgångsövervakning**: Strikt efterlevnad av tokenlivslängdsgränser  
- **Scope-validering**: Säkerställ att tokens innehåller lämpliga behörigheter för begärda operationer

### **Säkerhet för auktoriseringslogik**

**Kritiska kontroller:**
- **Omfattande auktoriseringsrevisioner**: Regelbundna säkerhetsgranskningar av alla auktoriseringsbeslutspunkter  
- **Fail-safe standardinställningar**: Nekar åtkomst när auktoriseringslogiken inte kan fatta ett definitivt beslut  
- **Behörighetsgränser**: Tydlig separation mellan olika privilegienivåer och resursåtkomst  
- **Revisionsloggning**: Fullständig loggning av alla auktoriseringsbeslut för säkerhetsövervakning  
- **Regelbundna åtkomstgranskningar**: Periodisk validering av användarbehörigheter och privilegietilldelningar

## 2. **Token-säkerhet och anti-passthrough-kontroller**

### **Förebyggande av token-passthrough**

**Token-passthrough är uttryckligen förbjudet** i MCP Authorization Specification på grund av kritiska säkerhetsrisker:

**Säkerhetsrisker som adresseras:**
- **Kontrollomgåelse**: Omgår viktiga säkerhetskontroller som hastighetsbegränsning, förfrågningsvalidering och trafikövervakning  
- **Ansvarsupplösning**: Gör klientidentifiering omöjlig, vilket förstör revisionsspår och incidentutredning  
- **Proxy-baserad exfiltrering**: Möjliggör för illvilliga aktörer att använda servrar som proxys för obehörig dataåtkomst  
- **Brott mot förtroendegränser**: Bryter nedströms tjänsters förtroendeantaganden om tokenursprung  
- **Laterala rörelser**: Komprometterade tokens över flera tjänster möjliggör bredare attacker

**Implementeringskontroller:**
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

### **Säkra mönster för tokenhantering**

**Bästa praxis:**
- **Kortlivade tokens**: Minimera exponeringstid med frekvent tokenrotation  
- **Just-in-time utfärdande**: Utfärda tokens endast när de behövs för specifika operationer  
- **Säker lagring**: Använd hårdvarusäkerhetsmoduler (HSM) eller säkra nyckelvalv  
- **Tokenbindning**: Binda tokens till specifika klienter, sessioner eller operationer där det är möjligt  
- **Övervakning och larm**: Realtidsdetektion av tokenmissbruk eller obehöriga åtkomstmönster

## 3. **Sessionssäkerhetskontroller**

### **Förebyggande av sessionkapning**

**Attackvektorer som adresseras:**
- **Sessionkapnings-promptinjektion**: Illvilliga händelser injiceras i delat sessionsläge  
- **Sessionsimitation**: Obehörig användning av stulna sessions-ID:n för att kringgå autentisering  
- **Återupptagbara strömningsattacker**: Utnyttjande av server-sända händelseåterupptagningar för illvillig innehållsinjektion

**Obligatoriska sessionskontroller:**
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

**Transportssäkerhet:**
- **HTTPS-krav**: All sessionskommunikation över TLS 1.3  
- **Säkra cookie-attribut**: HttpOnly, Secure, SameSite=Strict  
- **Certifikatpinning**: För kritiska anslutningar för att förhindra MITM-attacker

### **Tillståndsbaserade vs tillståndslösa överväganden**

**För tillståndsbaserade implementationer:**
- Delat sessionsläge kräver extra skydd mot injektionsattacker  
- Köbaserad sessionshantering behöver integritetsverifiering  
- Flera serverinstanser kräver säker synkronisering av sessionsläge

**För tillståndslösa implementationer:**
- JWT eller liknande tokenbaserad sessionshantering  
- Kryptografisk verifiering av sessionslägets integritet  
- Minskad attackyta men kräver robust tokenvalidering

## 4. **AI-specifika säkerhetskontroller**

### **Försvar mot promptinjektion**

**Microsoft Prompt Shields-integration:**
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

**Implementeringskontroller:**
- **Inmatningssanering**: Omfattande validering och filtrering av all användarinmatning  
- **Definition av innehållsgränser**: Tydlig separation mellan systeminstruktioner och användarinnehåll  
- **Instruktionshierarki**: Korrekt prioriteringsordning för motstridiga instruktioner  
- **Utdataövervakning**: Detektion av potentiellt skadliga eller manipulerade utdata

### **Förebyggande av verktygsförgiftning**

**Verktygssäkerhetsramverk:**
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

**Dynamisk verktygshantering:**
- **Godkännandeprocesser**: Uttryckligt användarsamtycke för verktygsändringar  
- **Återställningsmöjligheter**: Möjlighet att återgå till tidigare verktygsversioner  
- **Ändringsrevision**: Fullständig historik över verktygsdefinitionsändringar  
- **Riskbedömning**: Automatisk utvärdering av verktygssäkerhetsstatus

## 5. **Förebyggande av Confused Deputy-attacker**

### **OAuth Proxy-säkerhet**

**Kontroller för attackförebyggande:**
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

**Implementeringskrav:**
- **Verifiering av användarsamtycke**: Hoppa aldrig över samtyckesskärmar för dynamisk klientregistrering  
- **Validering av redirect URI**: Strikt vitlistbaserad validering av omdirigeringsdestinationer  
- **Skydd av auktoriseringskod**: Kortlivade koder med engångsanvändning  
- **Verifiering av klientidentitet**: Robust validering av klientuppgifter och metadata

## 6. **Säkerhet vid verktygsexekvering**

### **Sandboxing och isolering**

**Containerbaserad isolering:**
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

**Processisolering:**
- **Separata processkontexter**: Varje verktygsexekvering i isolerat processutrymme  
- **Interprocesskommunikation**: Säkra IPC-mekanismer med validering  
- **Processövervakning**: Analys av körbeteende och detektion av anomalier  
- **Resursbegränsningar**: Hårda gränser för CPU, minne och I/O-operationer

### **Implementering av minsta privilegium**

**Behörighetshantering:**
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

## 7. **Säkerhetskontroller för leveranskedjan**

### **Verifiering av beroenden**

**Omfattande komponentssäkerhet:**
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

### **Kontinuerlig övervakning**

**Hotdetektion i leveranskedjan:**
- **Övervakning av beroendehälsa**: Kontinuerlig bedömning av alla beroenden för säkerhetsproblem  
- **Integration av hotintelligens**: Realtidsuppdateringar om nya hot mot leveranskedjan  
- **Beteendeanalys**: Detektion av ovanligt beteende i externa komponenter  
- **Automatiserad respons**: Omedelbar isolering av komprometterade komponenter

## 8. **Övervaknings- och detektionskontroller**

### **Säkerhetsinformations- och händelsehantering (SIEM)**

**Omfattande loggningsstrategi:**
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

### **Hotdetektion i realtid**

**Beteendeanalys:**
- **User Behavior Analytics (UBA)**: Detektion av ovanliga användaråtkomstmönster  
- **Entity Behavior Analytics (EBA)**: Övervakning av MCP-server och verktygsbeteende  
- **Maskininlärningsbaserad anomalidetektion**: AI-driven identifiering av säkerhetshot  
- **Korrelationsanalys av hotintelligens**: Matchning av observerade aktiviteter mot kända attackmönster

## 9. **Incidenthantering och återställning**

### **Automatiserade responsmöjligheter**

**Omedelbara responsåtgärder:**
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

### **Forensiska möjligheter**

**Stöd för utredning:**
- **Bevarande av revisionsspår**: Oföränderliga loggar med kryptografisk integritet  
- **Insamling av bevis**: Automatisk insamling av relevanta säkerhetsartefakter  
- **Tidslinjerekonstruktion**: Detaljerad sekvens av händelser som ledde till säkerhetsincidenter  
- **Påverkansbedömning**: Utvärdering av kompromissomfattning och dataexponering

## **Viktiga principer för säkerhetsarkitektur**

### **Försvar i djupet**
- **Flera säkerhetslager**: Ingen enskild felpunkt i säkerhetsarkitekturen  
- **Redundanta kontroller**: Överlappande säkerhetsåtgärder för kritiska funktioner  
- **Fail-safe-mekanismer**: Säkra standardinställningar vid systemfel eller attacker

### **Zero Trust-implementering**
- **Lita aldrig, verifiera alltid**: Kontinuerlig validering av alla enheter och förfrågningar  
- **Principen om minsta privilegium**: Minimala åtkomsträttigheter för alla komponenter  
- **Mikrosegmentering**: Granulära nätverks- och åtkomstkontroller

### **Kontinuerlig säkerhetsevolution**
- **Anpassning till hotlandskapet**: Regelbundna uppdateringar för att hantera nya hot  
- **Effektivitet i säkerhetskontroller**: Löpande utvärdering och förbättring av kontroller  
- **Efterlevnad av specifikationer**: Anpassning till utvecklande MCP-säkerhetsstandarder

---

## **Implementeringsresurser**

### **Officiell MCP-dokumentation**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsofts säkerhetslösningar**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Säkerhetsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 för stora språkmodeller](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Viktigt**: Dessa säkerhetskontroller speglar den aktuella MCP-specifikationen (2025-06-18). Verifiera alltid mot den senaste [officiella dokumentationen](https://spec.modelcontextprotocol.io/) eftersom standarder fortsätter att utvecklas snabbt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
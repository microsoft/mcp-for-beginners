# MCP Sikkerhedskontroller - Opdatering december 2025

> **Nuværende standard**: Dette dokument afspejler [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) sikkerhedskrav og officielle [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) er modnet betydeligt med forbedrede sikkerhedskontroller, der adresserer både traditionel softwaresikkerhed og AI-specifikke trusler. Dette dokument giver omfattende sikkerhedskontroller for sikre MCP-implementeringer pr. december 2025.

## **OBLIGATORISKE sikkerhedskrav**

### **Kritiske forbud fra MCP-specifikationen:**

> **FORBUDT**: MCP-servere **MÅ IKKE** acceptere nogen tokens, der ikke eksplicit er udstedt til MCP-serveren  
>
> **FORBUDT**: MCP-servere **MÅ IKKE** bruge sessioner til autentificering  
>
> **KRÆVET**: MCP-servere, der implementerer autorisation, **SKAL** verificere ALLE indgående forespørgsler  
>
> **OBLIGATORISK**: MCP-proxyservere, der bruger statiske klient-ID'er, **SKAL** indhente brugerens samtykke for hver dynamisk registreret klient

---

## 1. **Autentificerings- og autorisationskontroller**

### **Integration af ekstern identitetsudbyder**

**Nuværende MCP-standard (2025-06-18)** tillader MCP-servere at delegere autentificering til eksterne identitetsudbydere, hvilket repræsenterer en betydelig sikkerhedsforbedring:

### **Integration af ekstern identitetsudbyder**

**Nuværende MCP-standard (2025-11-25)** tillader MCP-servere at delegere autentificering til eksterne identitetsudbydere, hvilket repræsenterer en betydelig sikkerhedsforbedring:

**Sikkerhedsfordele:**
1. **Eliminerer risici ved brugerdefineret autentificering**: Reducerer sårbarhedsoverfladen ved at undgå brugerdefinerede autentificeringsimplementeringer  
2. **Enterprise-grade sikkerhed**: Udnytter etablerede identitetsudbydere som Microsoft Entra ID med avancerede sikkerhedsfunktioner  
3. **Centraliseret identitetsstyring**: Forenkler brugerlivscyklusstyring, adgangskontrol og overholdelsesrevision  
4. **Multi-faktor autentificering**: Arver MFA-funktioner fra enterprise identitetsudbydere  
5. **Betingede adgangspolitikker**: Drager fordel af risikobaserede adgangskontroller og adaptiv autentificering

**Implementeringskrav:**
- **Validering af tokenmålgruppe**: Verificer at alle tokens eksplicit er udstedt til MCP-serveren  
- **Udstederverifikation**: Bekræft at tokenudsteder matcher den forventede identitetsudbyder  
- **Signaturverifikation**: Kryptografisk validering af tokenintegritet  
- **Håndhævelse af udløbstid**: Streng håndhævelse af tokenets levetidsgrænser  
- **Scope-validering**: Sikr at tokens indeholder passende tilladelser til de anmodede operationer

### **Sikkerhed for autorisationslogik**

**Kritiske kontroller:**
- **Omfattende autorisationsrevisioner**: Regelmæssige sikkerhedsgennemgange af alle autorisationsbeslutningspunkter  
- **Fail-safe standarder**: Nægt adgang, når autorisationslogikken ikke kan træffe en entydig beslutning  
- **Tilladelsesgrænser**: Klar adskillelse mellem forskellige privilegieniveauer og ressourceadgang  
- **Audit-logning**: Fuldstændig logning af alle autorisationsbeslutninger til sikkerhedsovervågning  
- **Regelmæssige adgangsgennemgange**: Periodisk validering af brugerrettigheder og privilegietildelinger

## 2. **Token-sikkerhed og anti-passthrough-kontroller**

### **Forebyggelse af token-passthrough**

**Token-passthrough er udtrykkeligt forbudt** i MCP Authorization Specification på grund af kritiske sikkerhedsrisici:

**Sikkerhedsrisici der adresseres:**
- **Omgåelse af kontrol**: Omgår væsentlige sikkerhedskontroller som ratebegrænsning, forespørgselsvalidering og trafikovervågning  
- **Ansvarsfraskrivelse**: Gør klientidentifikation umulig, hvilket ødelægger revisionsspor og hændelsesundersøgelser  
- **Proxy-baseret udtræk**: Muliggør ondsindede aktører at bruge servere som proxyer til uautoriseret dataadgang  
- **Brud på tillidsgrænser**: Bryder nedstrøms tjenesters tillidsantagelser om token-oprindelse  
- **Lateral bevægelse**: Kompromitterede tokens på tværs af flere tjenester muliggør bredere angrebsudvidelse

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

### **Sikre tokenhåndteringsmønstre**

**Bedste praksis:**
- **Kortlivede tokens**: Minimer eksponeringsvinduet med hyppig tokenrotation  
- **Just-in-time udstedelse**: Udsted tokens kun når nødvendigt til specifikke operationer  
- **Sikker opbevaring**: Brug hardware-sikkerhedsmoduler (HSM'er) eller sikre nøgleopbevaringssteder  
- **Tokenbinding**: Bind tokens til specifikke klienter, sessioner eller operationer hvor muligt  
- **Overvågning og alarmering**: Realtidsdetektion af tokenmisbrug eller uautoriserede adgangsmønstre

## 3. **Sessionssikkerhedskontroller**

### **Forebyggelse af sessionkapring**

**Angrebsvektorer der adresseres:**
- **Sessionkapring via promptinjektion**: Ondsindede hændelser injiceret i delt sessionstilstand  
- **Sessionudgivelse**: Uautoriseret brug af stjålne session-ID'er til at omgå autentificering  
- **Genoptagelige stream-angreb**: Udnyttelse af server-sent event-genoptagelse til ondsindet indholdsinjektion

**Obligatoriske sessionskontroller:**
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

**Transport-sikkerhed:**
- **HTTPS-håndhævelse**: Al sessionskommunikation over TLS 1.3  
- **Sikre cookieattributter**: HttpOnly, Secure, SameSite=Strict  
- **Certifikatpinning**: For kritiske forbindelser for at forhindre MITM-angreb

### **Stateful vs stateless overvejelser**

**For stateful implementeringer:**
- Delt sessionstilstand kræver yderligere beskyttelse mod injektionsangreb  
- Kø-baseret sessionstyring kræver integritetsverifikation  
- Flere serverinstanser kræver sikker synkronisering af sessionstilstand

**For stateless implementeringer:**
- JWT eller lignende tokenbaseret sessionstyring  
- Kryptografisk verifikation af sessionstilstandens integritet  
- Reduceret angrebsoverflade, men kræver robust tokenvalidering

## 4. **AI-specifikke sikkerhedskontroller**

### **Forsvar mod promptinjektion**

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
- **Inputsanitering**: Omfattende validering og filtrering af alle brugerinput  
- **Indholdsafgrænsning**: Klar adskillelse mellem systeminstruktioner og brugerindhold  
- **Instruktionshierarki**: Korrekte præcedensregler for modstridende instruktioner  
- **Outputovervågning**: Detektion af potentielt skadelige eller manipulerede output

### **Forebyggelse af tool-forgiftning**

**Tool-sikkerhedsramme:**
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

**Dynamisk tool-styring:**
- **Godkendelsesarbejdsgange**: Eksplicit brugersamtykke til tool-ændringer  
- **Rollback-muligheder**: Mulighed for at rulle tilbage til tidligere tool-versioner  
- **Ændringsrevision**: Fuld historik over tool-definitionsændringer  
- **Risikoevaluering**: Automatisk vurdering af tools sikkerhedstilstand

## 5. **Forebyggelse af Confused Deputy-angreb**

### **OAuth Proxy-sikkerhed**

**Angrebsforebyggelseskontroller:**
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
- **Verifikation af brugersamtykke**: Spring aldrig samtykkeskærme over ved dynamisk klientregistrering  
- **Validering af redirect URI**: Streng whitelist-baseret validering af redirect-destinationer  
- **Beskyttelse af autorisationskode**: Kortlivede koder med håndhævelse af enkeltbrug  
- **Verifikation af klientidentitet**: Robust validering af klientlegitimationsoplysninger og metadata

## 6. **Tool-eksekveringssikkerhed**

### **Sandboxing og isolation**

**Containerbaseret isolation:**
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

**Procesisolation:**
- **Separate proceskontekster**: Hver tool-eksekvering i isoleret procesrum  
- **Inter-proces kommunikation**: Sikker IPC-mekanismer med validering  
- **Procesovervågning**: Runtime adfærdsanalyse og anomalidetektion  
- **Ressourcehåndhævelse**: Strenge grænser for CPU, hukommelse og I/O-operationer

### **Implementering af mindst privilegium**

**Tilladelsesstyring:**
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

## 7. **Supply chain-sikkerhedskontroller**

### **Afhængighedsverifikation**

**Omfattende komponent-sikkerhed:**
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

### **Kontinuerlig overvågning**

**Trusselsdetektion i supply chain:**
- **Overvågning af afhængigheders sundhed**: Kontinuerlig vurdering af alle afhængigheder for sikkerhedsproblemer  
- **Integration af trusselsintelligens**: Realtidsopdateringer om nye supply chain-trusler  
- **Adfærdsanalyse**: Detektion af usædvanlig adfærd i eksterne komponenter  
- **Automatisk respons**: Øjeblikkelig inddæmning af kompromitterede komponenter

## 8. **Overvågnings- og detektionskontroller**

### **Security Information and Event Management (SIEM)**

**Omfattende logningsstrategi:**
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

### **Trusselsdetektion i realtid**

**Adfærdsanalyse:**
- **User Behavior Analytics (UBA)**: Detektion af usædvanlige brugeradgangsmønstre  
- **Entity Behavior Analytics (EBA)**: Overvågning af MCP-server og tool-adfærd  
- **Maskinlæringsbaseret anomalidetektion**: AI-drevet identifikation af sikkerhedstrusler  
- **Korrelationsanalyse med trusselsintelligens**: Matchning af observerede aktiviteter med kendte angrebsmønstre

## 9. **Hændelsesrespons og genopretning**

### **Automatiserede responsmuligheder**

**Øjeblikkelige responshandlinger:**
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

### **Rettsmedicinske kapaciteter**

**Undersøgelsesstøtte:**
- **Bevarelse af revisionsspor**: Uforanderlig logning med kryptografisk integritet  
- **Indsamling af beviser**: Automatisk indsamling af relevante sikkerhedsartefakter  
- **Tidslinjerekonstruktion**: Detaljeret sekvens af hændelser, der fører til sikkerhedshændelser  
- **Vurdering af påvirkning**: Evaluering af kompromitteringsomfang og dataeksponering

## **Nøgleprincipper for sikkerhedsarkitektur**

### **Forsvar i dybden**
- **Flere sikkerhedslag**: Intet enkelt fejlpunkt i sikkerhedsarkitekturen  
- **Redundante kontroller**: Overlappende sikkerhedsforanstaltninger for kritiske funktioner  
- **Fail-safe mekanismer**: Sikker standardindstilling ved systemfejl eller angreb

### **Zero Trust-implementering**
- **Aldrig tillid, altid verifikation**: Kontinuerlig validering af alle enheder og forespørgsler  
- **Princippet om mindst privilegium**: Minimale adgangsrettigheder for alle komponenter  
- **Mikrosegmentering**: Granulære netværks- og adgangskontroller

### **Kontinuerlig sikkerhedsudvikling**
- **Tilpasning til trusselslandskabet**: Regelmæssige opdateringer for at adressere nye trusler  
- **Effektivitet af sikkerhedskontroller**: Løbende evaluering og forbedring af kontroller  
- **Overholdelse af specifikationer**: Tilpasning til udviklende MCP-sikkerhedsstandarder

---

## **Implementeringsressourcer**

### **Officiel MCP-dokumentation**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft sikkerhedsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sikkerhedsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Vigtigt**: Disse sikkerhedskontroller afspejler den nuværende MCP-specifikation (2025-06-18). Verificer altid mod den nyeste [officielle dokumentation](https://spec.modelcontextprotocol.io/), da standarder fortsat udvikler sig hurtigt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
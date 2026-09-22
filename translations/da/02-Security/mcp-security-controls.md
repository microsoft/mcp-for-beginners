# MCP Sikkerhedskontroller - Opdatering september 2026

> **Nuværende standard:** Dette dokument afspejler
> [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> og de officielle
> [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) er blevet væsentligt moden med forbedrede sikkerhedskontroller, der adresserer både traditionel software-sikkerhed og AI-specifikke trusler. Dette dokument giver omfattende sikkerhedskontroller for sikre MCP-implementeringer i overensstemmelse med OWASP MCP Top 10-rammeværket.

## 🏔️ Praktisk Sikkerhedstræning

For praktisk erfaring med sikkerhedsimplementering anbefaler vi **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - en omfattende guidet ekspedition til sikring af MCP-servere i Azure ved hjælp af en "sårbar → udnyttelse → rettelse → validering" metode.

Alle sikkerhedskontroller i dette dokument er i overensstemmelse med **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, som tilbyder referencearkitekturer og Azure-specifik implementeringsvejledning for OWASP MCP Top 10 risici.

## **OBLIGATORISKE Sikkerhedskrav**

### **Kritiske Forbud fra MCP Specification:**

> **FORBUDT**: MCP-servere **MÅ IKKE** acceptere tokens, der ikke eksplicit er udstedt til MCP-serveren
>
> **FORBUDT**: MCP-servere **MÅ IKKE** bruge sessioner til autentificering  
>
> **KRÆVET**: MCP-servere med autorisationsimplementering **SKAL** verificere ALLE indgående anmodninger
>
> **OBLIGATORISK**: MCP proxyservere, der bruger en statisk tredjepartsklient-ID,
> **SKAL** indhente samtykke for hver MCP-klient før videresendelse af autorisation

---

## 1. **Autentificerings- & Autorisationskontroller**

### **Integration med Eksterne Identitetsudbydere**

**MCP Specification `2026-07-28`** tillader MCP-servere at delegere
autentificering til eksterne identitetsudbydere. Autorisation for HTTP
transport evalueres pr. anmodning; lokale stdio-servere henter i stedet legitimationsoplysninger
fra deres miljø.

**OWASP MCP Risiko adresseret**: [MCP07 - Utilstrækkelig autentificering & autorisation](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Sikkerhedsmæssige fordele:**
1. **Eliminerer Brugerdefinerede Autentificeringsrisici**: Reducerer sårbarhedsoverflade ved at undgå brugerdefinerede autentificeringsimplementeringer
2. **Enterprise-Niveau Sikkerhed**: Udnytter etablerede identitetsudbydere som Microsoft Entra ID med avancerede sikkerhedsfunktioner
3. **Centraliseret Identitetsstyring**: Forenkler brugerlivscyklus, adgangskontrol og compliance-revisioner
4. **Multi-Faktor Autentificering**: Arver MFA-muligheder fra enterprise identitetsudbydere
5. **Betingede Adgangspolitikker**: Drager fordel af risikobaserede adgangskontroller og adaptiv autentificering

**Implementeringskrav:**
- **Klientregistrering**: Foretræk klient-ID metadata dokumenter eller
  forregistrering; brug kun udfaset dynamisk klientregistrering til
  kompatibilitet
- **Validering af token modtager**: Verificér at alle tokens eksplicit er udstedt til MCP-serveren
- **Verifikation af udsteder**: Bekræft token-udsteder matcher forventet identitetsudbyder
- **Signaturverifikation**: Kryptografisk validering af token-integritet
- **Håndhævelse af udløbstid**: Streng håndhævelse af token levetidsgrænser
- **Scope-validering**: Sørg for at tokens indeholder passende tilladelser til de anmodede operationer

### **Sikkerhedslogik for Autorisation**

**Kritiske kontroller:**
- **Omfattende autorisationsrevisioner**: Regelmæssige sikkerhedsrevisioner af alle autorisationsbeslutningspunkter
- **Fail-Safe standarder**: Nægt adgang hvis autorisationslogikken ikke kan træffe en endelig beslutning
- **Tilladelsesgrænser**: Klar adskillelse mellem forskellige privilegieniveauer og adgang til ressourcer
- **Audit-logging**: Komplet logning af alle autorisationsbeslutninger til sikkerhedsovervågning
- **Regelmæssige adgangsrevisioner**: Periodisk validering af brugertilladelser og privilegie tildelinger

## 2. **Token Sikkerhed & Anti-Passthrough Kontroller**

**OWASP MCP Risiko adresseret**: [MCP01 - Tokenhåndtering & Hemmelighedseksponering](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Forebyggelse af Token Passthrough**

**Token passthrough er eksplicit forbudt** i MCP Autorisationsspecifikationen på grund af kritiske sikkerhedsrisici:

**Sikkerhedsrisici adresseret:**
- **Omgåelse af kontroller**: Undgår væsentlige sikkerhedskontroller som ratebegrænsning, anmodningsvalidering og trafikovervågning
- **Ansvarsbrud**: Gør klientidentifikation umulig, hvilket underminerer revisionsspor og hændelsesundersøgelser
- **Proxy-baseret udtrækning**: Muliggør ondsindede aktører at bruge servere som proxyer til uautoriseret dataadgang
- **Brud på tillidsgrænser**: Bryder nedstrøms tjenestetillid antagelser om token-kilder
- **Lateral bevægelse**: Kompromitterede tokens på tværs af tjenester muliggør bredere angrebsudvidelse

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

### **Sikre Tokenhåndteringsmønstre**

**Bedste praksis:**
- **Kortlivede tokens**: Minimer eksponeringsvinduet med hyppig tokenrotation
- **Just-in-time Udstedelse**: Udsted tokens kun når nødvendigt til specifikke operationer
- **Sikker opbevaring**: Brug hardware sikkerhedsmoduler (HSM) eller sikre nøgledepot
- **Tokenbinding**: Valider token modtager og udsteder for den tilsigtede MCP
  ressource, klient og operation
- **Overvågning & Alarmering**: Realtidsdetektion af token misbrug eller uautoriserede adgangsmønstre

## 3. **Sikkerhedskontroller for Applikationsstatus**

### **Forebyggelse af State Handle Hijacking**

**Angrebsvinkler adresseret:**
- **Handle-gætteri**: Forudsigelige identifikatorer eksponerer en andens tilstand
- **Genbrug på tværs af brugere**: Et stjålet handle bruges med en anden identitet
- **Implicit Autorisation**: Besiddelse af et handle behandles fejlagtigt som
  adgangsbevis

**Kontroller for State Handles:**

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

**Transport Sikkerhed:**
- **HTTPS Håndhævelse**: Kræv HTTPS for fjern HTTP-transporter
- **Håndtering af legitimationsoplysninger**: Send og valider autorisation ved hver HTTP-anmodning
- **stdio Isolation**: Beskyt lokale stdio-servere gennem procesisolation og
  miljø-legitimationskontroller

### **Stateless vs Stateful Overvejelser**

MCP `2026-07-28` er stateless på protokol laget. Applikationer kan stadigvæk
opretholde tilstand ved at returnere et eksplicit handle fra et værktøjskald og acceptere
det som et almindeligt argument i senere kald.

- Gem tilstanden uafhængigt af en enkelt transportforbindelse.
- Bind state handles til den autentificerede principal serverside.
- Behandl et handle som et navn, ikke som en bearer-legitimationsoplysning.
- Definér udløbs- og gendannelsesadfærd for forældede handles.

## 4. **AI-Specifikke Sikkerhedskontroller**

**OWASP MCP Risici adresseret**:
- [MCP06 - Intent Flow Subversion](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Tool Poisoning](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Command Injection & Execution](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Forsvar mod Prompt-injektion**

**Microsoft Prompt Shields Integration:**
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
- **Input-sanitization**: Omfattende validering og filtrering af alle brugerinput
- **Indholdsgrænsedefinition**: Klar adskillelse mellem systeminstruktioner og brugers indhold
- **Instruktionshierarki**: Korrekte præcedensregler for modstridende instruktioner
- **Output-overvågning**: Detektion af potentielt skadelige eller manipulerede outputs

### **Forebyggelse af Tool Poisoning**

**Sikkerhedsramme for værktøjer:**
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

**Dynamisk værktøjsstyring:**
- **Godkendelsesarbejdsgange**: Eksplicit brugeraccept for værktøjsændringer
- **Rollback-muligheder**: Mulighed for at rulle tilbage til tidligere versioner af værktøjer
- **Ændringsrevision**: Komplet historik over ændringer i værktøjsdefinitioner
- **Risikovurdering**: Automatisk evaluering af værktøjssikkerhedsstatus

## 5. **Forebyggelse af Confused Deputy Angreb**

### **OAuth Proxy Sikkerhed**

**Angrebsforebyggelseskontroller:**
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

**Implementeringskrav:**
- **Klientregistrering**: Foretræk forregistrering eller Client ID Metadata
  dokumenter; behandl dynamisk klientregistrering som et kompatibilitets-faldtilbage
- **Brugersamtykke verifikation**: MCP-proxyer, der bruger en statisk tredjepartsklient
  ID må kun videresende autorisation efter indhentet samtykke for hver klient
- **Redirect URI validering**: Streng whitelist-baseret validering af redirect destinationer
- **Beskyttelse af autorisationskode**: Kortlivede koder med single-use håndhævelse
- **Verifikation af klientidentitet**: Robust validering af klientlegitimationsoplysninger og metadata

## 6. **Værktøjsudførelsessikkerhed**

### **Sandboxing & Isolation**

**Container-baseret isolation:**
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
- **Separate proceskontekster**: Hver værktøjsudførelse i isoleret procesrum
- **Inter-proces kommunikation**: Sikker IPC-mekanismer med validering
- **Procesovervågning**: Kørselsadfærdsanalyse og anomalidetektion
- **Ressourcehåndhævelse**: Strenge grænser for CPU, hukommelse og I/O operationer

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

## 7. **Supply Chain Sikkerhedskontroller**

**OWASP MCP Risiko adresseret**: [MCP04 - Software Supply Chain Angreb & Afhængighedsmanipulation](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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

### **Kontinuerlig Overvågning**

**Trusselsdetektion i leverandørkæden:**
- **Overvågning af afhængigheders sundhed**: Kontinuerlig vurdering af alle afhængigheder for sikkerhedsproblemer
- **Integration af trusselsintelligens**: Realtidsopdateringer om nye forsyningskædet trusler
- **Adfærdsanalyse**: Detektion af usædvanlig adfærd i eksterne komponenter
- **Automatisk reaktion**: Øjeblikkelig inddæmning af kompromitterede komponenter

## 8. **Overvågnings- & Detektionskontroller**

**OWASP MCP Risiko adresseret**: [MCP08 - Manglende audit og telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Security Information and Event Management (SIEM)**

**Omfattende logstrategi:**
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
- **Brugeradfærdsanalyse (UBA)**: Detektion af usædvanlige brugeradgangsmønstre
- **Enhedsadfærdsanalyse (EBA)**: Overvågning af MCP-server- og værktøjsadfærd
- **Maskinlærings-anomalidetektion**: AI-drevet identificering af sikkerhedstrusler
- **Trusselsintelligenskoordination**: Sammenligning af observerede aktiviteter med kendte angrebsmønstre

## 9. **Hændelsesrespons & Genopretning**

### **Automatiserede reaktionsevner**

**Øjeblikkelige reaktionshandlinger:**
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

### **Retsmedicinske kapaciteter**

**Undersøgelsesstøtte:**
- **Bevaring af revisionsspor**: Uforanderlig logning med kryptografisk integritet
- **Bevisindsamling**: Automatisk indsamling af relevante sikkerhedsartefakter
- **Tidslinjerekonstruktion**: Detaljeret rækkefølge af hændelser der fører til sikkerhedshændelser
- **Konsekvensvurdering**: Evaluering af kompromisomfang og dataeksponering

## **Nøgleprincipper for sikkerhedsarkitektur**

### **Defense in Depth**
- **Flere sikkerhedslag**: Intet enkelt fejlpunkt i sikkerhedsarkitekturen
- **Redundante kontroller**: Overlappende sikkerhedsforanstaltninger for kritiske funktioner
- **Fail-Safe mekanismer**: Sikre standarder når systemer støder på fejl eller angreb

### **Zero Trust Implementering**
- **Stol aldrig, verificer altid**: Kontinuerlig validering af alle enheder og anmodninger
- **Princip om mindst privilegium**: Minimale adgangsrettigheder for alle komponenter
- **Mikrosegmentering**: Granulære netværks- og adgangskontroller

### **Kontinuerlig sikkerhedsevolution**
- **Tilpasning til trusselslandskabet**: Regelmæssige opdateringer for at håndtere nye trusler
- **Effektivitet af sikkerhedskontroller**: Løbende evaluering og forbedring af kontroller
- **Specifikationssamsvar**: Overensstemmelse med udviklende MCP sikkerhedsstandarder

---

## **Implementeringsressourcer**

### **Officiel MCP Dokumentation**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Sikkerhedsressourcer**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Top 10 med Azure-implementering
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officielle OWASP MCP sikkerhedsrisici
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhedstræning for MCP på Azure

### **Microsoft Sikkerhedsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sikkerhedsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Vigtigt:** Disse sikkerhedskontroller afspejler MCP Specifikation
> `2026-07-28`. Bekræft altid mod
> [den officielle aktuelle dokumentation](https://modelcontextprotocol.io/specification/2026-07-28/)
> da standarder fortsat udvikler sig.

## Hvad er næste skridt

- Vend tilbage til: [Oversigt over Sikkerhedsmodul](./README.md)
- Fortsæt til: [Modul 3: Kom godt i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Sikkerhetskontroller - Oppdatering desember 2025

> **Gjeldende standard**: Dette dokumentet gjenspeiler [MCP Spesifikasjon 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) sikkerhetskrav og offisielle [MCP Sikkerhetsbeste praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Model Context Protocol (MCP) har modnet betydelig med forbedrede sikkerhetskontroller som adresserer både tradisjonell programvaresikkerhet og AI-spesifikke trusler. Dette dokumentet gir omfattende sikkerhetskontroller for sikre MCP-implementeringer per desember 2025.

## **OBLIGATORISKE sikkerhetskrav**

### **Kritiske forbud fra MCP-spesifikasjonen:**

> **FORBUDT**: MCP-servere **MÅ IKKE** akseptere noen tokens som ikke eksplisitt er utstedt for MCP-serveren  
>
> **FORBUDT**: MCP-servere **MÅ IKKE** bruke økter for autentisering  
>
> **PÅKREVD**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler  
>
> **OBLIGATORISK**: MCP-proxyservere som bruker statiske klient-IDer **MÅ** innhente brukerens samtykke for hver dynamisk registrerte klient

---

## 1. **Autentisering & Autorisasjonskontroller**

### **Integrasjon med ekstern identitetsleverandør**

**Gjeldende MCP-standard (2025-06-18)** tillater MCP-servere å delegere autentisering til eksterne identitetsleverandører, noe som representerer en betydelig sikkerhetsforbedring:

### **Integrasjon med ekstern identitetsleverandør**

**Gjeldende MCP-standard (2025-11-25)** tillater MCP-servere å delegere autentisering til eksterne identitetsleverandører, noe som representerer en betydelig sikkerhetsforbedring:

**Sikkerhetsfordeler:**
1. **Eliminerer risiko ved egendefinert autentisering**: Reduserer sårbarhetsoverflaten ved å unngå egendefinerte autentiseringsimplementasjoner  
2. **Sikkerhet på bedriftsnivå**: Utnytter etablerte identitetsleverandører som Microsoft Entra ID med avanserte sikkerhetsfunksjoner  
3. **Sentralisert identitetsadministrasjon**: Forenkler brukerens livssyklusadministrasjon, tilgangskontroll og samsvarsauditering  
4. **Multifaktorautentisering**: Arver MFA-funksjonalitet fra bedriftsidentitetsleverandører  
5. **Betingede tilgangspolicyer**: Drar nytte av risikobaserte tilgangskontroller og adaptiv autentisering

**Implementeringskrav:**
- **Validering av token-målgruppe**: Verifiser at alle tokens er eksplisitt utstedt for MCP-serveren  
- **Utstederverifisering**: Bekreft at token-utsteder samsvarer med forventet identitetsleverandør  
- **Signaturverifisering**: Kryptografisk validering av token-integritet  
- **Utløpshåndhevelse**: Streng håndhevelse av tokenets levetidsgrenser  
- **Omfangsvalidering**: Sørg for at tokens inneholder passende tillatelser for forespurte operasjoner

### **Sikkerhet for autorisasjonslogikk**

**Kritiske kontroller:**
- **Omfattende autorisasjonsrevisjoner**: Regelmessige sikkerhetsgjennomganger av alle autorisasjonsbeslutningspunkter  
- **Feilsikre standarder**: Avvis tilgang når autorisasjonslogikken ikke kan fatte en entydig beslutning  
- **Tillatelsesgrenser**: Klar separasjon mellom ulike privilegienivåer og ressursadgang  
- **Revisjonslogging**: Fullstendig logging av alle autorisasjonsbeslutninger for sikkerhetsovervåking  
- **Regelmessige tilgangsvurderinger**: Periodisk validering av brukerrettigheter og privilegietildelinger

## 2. **Token-sikkerhet & Anti-passthrough-kontroller**

### **Forebygging av token-passthrough**

**Token-passthrough er eksplisitt forbudt** i MCP Autorisasjonsspesifikasjonen på grunn av kritiske sikkerhetsrisikoer:

**Sikkerhetsrisikoer som adresseres:**
- **Omgåelse av kontroll**: Omgår essensielle sikkerhetskontroller som hastighetsbegrensning, forespørselsvalidering og trafikkovervåking  
- **Ansvarsfraskrivelse**: Gjør klientidentifikasjon umulig, noe som ødelegger revisjonsspor og hendelsesundersøkelser  
- **Proxy-basert utvinning**: Gjør det mulig for ondsinnede aktører å bruke servere som proxyer for uautorisert dataadgang  
- **Brudd på tillitsgrenser**: Bryter nedstrøms tjenesters tillitsantakelser om token-opprinnelse  
- **Lateral bevegelse**: Kompromitterte tokens på tvers av flere tjenester muliggjør bredere angrepsutvidelse

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

**Beste praksis:**
- **Kortlivede tokens**: Minimer eksponeringsvindu med hyppig tokenrotasjon  
- **Just-in-time-utstedelse**: Utsted tokens kun når nødvendig for spesifikke operasjoner  
- **Sikker lagring**: Bruk hardware security modules (HSM) eller sikre nøkkellagre  
- **Tokenbinding**: Bind tokens til spesifikke klienter, økter eller operasjoner der det er mulig  
- **Overvåking & varsling**: Sanntidsdeteksjon av tokenmisbruk eller uautorisert tilgangsmønstre

## 3. **Økt-sikkerhetskontroller**

### **Forebygging av øktkapring**

**Angrepsvektorer som adresseres:**
- **Øktkapring via promptinjeksjon**: Ondsinnede hendelser injisert i delt økttilstand  
- **Øktetterligning**: Uautorisert bruk av stjålne økt-IDer for å omgå autentisering  
- **Gjenopptakbare strømangrep**: Utnyttelse av server-sendte hendelsesgjenopptak for ondsinnet innholdsinjeksjon

**Obligatoriske øktkontroller:**
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

**Transport-sikkerhet:**
- **HTTPS-håndhevelse**: All øktkommunikasjon over TLS 1.3  
- **Sikre cookie-attributter**: HttpOnly, Secure, SameSite=Strict  
- **Sertifikatpinning**: For kritiske tilkoblinger for å forhindre MITM-angrep

### **Tilstandsstyrt vs tilstandsløs vurdering**

**For tilstandsstyrte implementeringer:**
- Delt økttilstand krever ekstra beskyttelse mot injeksjonsangrep  
- Købasert øktadministrasjon trenger integritetsverifisering  
- Flere serverinstanser krever sikker synkronisering av økttilstand

**For tilstandsløse implementeringer:**
- JWT eller lignende tokenbasert øktadministrasjon  
- Kryptografisk verifisering av økttilstands integritet  
- Redusert angrepsflate, men krever robust tokenvalidering

## 4. **AI-spesifikke sikkerhetskontroller**

### **Forsvar mot promptinjeksjon**

**Integrasjon med Microsoft Prompt Shields:**
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
- **Inndata-sanitær**: Omfattende validering og filtrering av all brukerinput  
- **Definisjon av innholdsgrenser**: Klar separasjon mellom systeminstruksjoner og brukerinhold  
- **Instruksjonshierarki**: Korrekte prioriteringsregler for motstridende instruksjoner  
- **Utgangsovervåking**: Deteksjon av potensielt skadelig eller manipulert output

### **Forebygging av verktøyforgiftning**

**Sikkerhetsrammeverk for verktøy:**
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

**Dynamisk verktøyadministrasjon:**
- **Godkjenningsarbeidsflyter**: Eksplisitt brukersamtykke for verktøymodifikasjoner  
- **Tilbakerullingsmuligheter**: Evne til å gå tilbake til tidligere verktøyversjoner  
- **Endringsrevisjon**: Fullstendig historikk over endringer i verktøydefinisjoner  
- **Risikovurdering**: Automatisk evaluering av verktøys sikkerhetsstatus

## 5. **Forebygging av Confused Deputy-angrep**

### **OAuth Proxy-sikkerhet**

**Forebyggende kontroller:**
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
- **Verifisering av brukersamtykke**: Aldri hopp over samtykkeskjermer for dynamisk klientregistrering  
- **Validering av redirect URI**: Streng hvitelistebasert validering av omdirigeringsdestinasjoner  
- **Beskyttelse av autorisasjonskode**: Kortlivede koder med håndheving av engangsbruk  
- **Verifisering av klientidentitet**: Robust validering av klientlegitimasjon og metadata

## 6. **Sikkerhet ved verktøykjøring**

### **Sandboxing & isolasjon**

**Containerbasert isolasjon:**
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

**Prosessisolasjon:**
- **Separate prosesskontekster**: Hver verktøykjøring i isolert prosessrom  
- **Inter-prosess kommunikasjon**: Sikker IPC-mekanismer med validering  
- **Prosessovervåking**: Kjøretidsanalyse av oppførsel og anomali-deteksjon  
- **Ressurshåndhevelse**: Strenge grenser for CPU, minne og I/O-operasjoner

### **Implementering av minste privilegium**

**Tillatelsesadministrasjon:**
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

## 7. **Sikkerhetskontroller for forsyningskjeden**

### **Avhengighetsverifisering**

**Omfattende komponent-sikkerhet:**
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

### **Kontinuerlig overvåking**

**Trusseldeteksjon i forsyningskjeden:**
- **Overvåking av avhengigheters helse**: Kontinuerlig vurdering av alle avhengigheter for sikkerhetsproblemer  
- **Integrasjon av trusselintelligens**: Sanntidsoppdateringer om nye trusler i forsyningskjeden  
- **Atferdsanalyse**: Deteksjon av uvanlig oppførsel i eksterne komponenter  
- **Automatisk respons**: Umiddelbar inneslutning av kompromitterte komponenter

## 8. **Overvåking & deteksjonskontroller**

### **Sikkerhetsinformasjon og hendelseshåndtering (SIEM)**

**Omfattende loggestrategi:**
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

### **Sanntids trusseldeteksjon**

**Atferdsanalyse:**
- **Brukeratferdsanalyse (UBA)**: Deteksjon av uvanlige brukeradgangsmønstre  
- **Enhetsatferdsanalyse (EBA)**: Overvåking av MCP-server og verktøyadferd  
- **Maskinlæringsbasert anomali-deteksjon**: AI-drevet identifisering av sikkerhetstrusler  
- **Korrelasjon med trusselintelligens**: Sammenstilling av observerte aktiviteter med kjente angrepsmønstre

## 9. **Hendelseshåndtering & gjenoppretting**

### **Automatiserte responsmuligheter**

**Umiddelbare responshandlinger:**
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

### **Forensiske muligheter**

**Støtte for etterforskning:**
- **Bevaring av revisjonsspor**: Uforanderlig logging med kryptografisk integritet  
- **Innsamling av bevis**: Automatisk innsamling av relevante sikkerhetsartefakter  
- **Tidslinjegjenskapning**: Detaljert sekvens av hendelser som ledet til sikkerhetshendelser  
- **Vurdering av påvirkning**: Evaluering av omfanget av kompromittering og dataeksponering

## **Nøkkelprinsipper for sikkerhetsarkitektur**

### **Forsvar i dybden**
- **Flere sikkerhetslag**: Ingen enkelt feilpunkt i sikkerhetsarkitekturen  
- **Redundante kontroller**: Overlappende sikkerhetstiltak for kritiske funksjoner  
- **Feilsikre mekanismer**: Sikre standarder når systemer møter feil eller angrep

### **Zero Trust-implementering**
- **Aldri stol på, alltid verifiser**: Kontinuerlig validering av alle enheter og forespørsler  
- **Prinsippet om minste privilegium**: Minimale tilgangsrettigheter for alle komponenter  
- **Mikrosegmentering**: Granulære nettverks- og tilgangskontroller

### **Kontinuerlig sikkerhetsevolusjon**
- **Tilpasning til trussellandskapet**: Regelmessige oppdateringer for å adressere nye trusler  
- **Effektivitet av sikkerhetskontroller**: Løpende evaluering og forbedring av kontroller  
- **Samsvar med spesifikasjoner**: Tilpasning til utviklende MCP-sikkerhetsstandarder

---

## **Implementeringsressurser**

### **Offisiell MCP-dokumentasjon**
- [MCP Spesifikasjon (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Sikkerhetsbeste praksis](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Autorisasjonsspesifikasjon](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft sikkerhetsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sikkerhetsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Topp 10 for store språkmodeller](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Viktig**: Disse sikkerhetskontrollene gjenspeiler gjeldende MCP-spesifikasjon (2025-06-18). Verifiser alltid mot den nyeste [offisielle dokumentasjonen](https://spec.modelcontextprotocol.io/) da standarder utvikler seg raskt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
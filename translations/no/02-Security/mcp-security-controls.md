# MCP Sikkerhetskontroller - Oppdatering September 2026

> **Gjeldende standard:** Dette dokumentet reflekterer
> [MCP Spesifikasjon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> og den offisielle
> [MCP Sikkerhetsbeste Praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) har modnet betydelig med forbedrede sikkerhetskontroller som adresserer både tradisjonell programvaresikkerhet og AI-spesifikke trusler. Dette dokumentet gir omfattende sikkerhetskontroller for sikre MCP-implementasjoner som er i samsvar med OWASP MCP Top 10-rammeverket.

## 🏔️ Praktisk Sikkerhetstrening

For praktisk, hands-on erfaring med sikkerhetsimplementering anbefaler vi **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** – en omfattende guidet ekspedisjon for å sikre MCP-servere i Azure ved hjelp av metodikken "sårbar → utnytt → fikse → validere".

Alle sikkerhetskontroller i dette dokumentet er i samsvar med **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, som gir referansearkitektur og Azure-spesifikk implementeringsveiledning for OWASP MCP Top 10-risikoene.

## **OBLIGATORISKE Sikkerhetskrav**

### **Kritiske Forbud i MCP Spesifikasjonen:**

> **FORBUDT**: MCP-servere **MÅ IKKE** godta noen tokens som ikke eksplisitt er utstedt for MCP-serveren
>
> **FORBUDT**: MCP-servere **MÅ IKKE** bruke økter til autentisering  
>
> **PÅKREVD**: MCP-servere som implementerer autorisasjon **MÅ** verifisere ALLE innkommende forespørsler
>
> **OBLIGATORISK**: MCP proxy-servere som bruker en statisk tredjeparts klient-ID
> **MÅ** innhente samtykke for hver MCP-klient før autorisasjon videresendes

---

## 1. **Autentiserings- og Autorisasjonskontroller**

### **Integrasjon med Ekstern Identitetsleverandør**

**MCP Spesifikasjon `2026-07-28`** tillater at MCP-servere delegerer
autentisering til eksterne identitetsleverandører. Autorisasjon for HTTP
transport evalueres per forespørsel; lokale stdio-servere henter
i stedet legitimasjon fra sitt miljø.

**OWASP MCP Risiko Adresse:** [MCP07 - Utilstrekkelig Autentisering & Autorisasjon](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Sikkerhetsfordeler:**
1. **Eliminerer Risiko ved Egendefinert Autentisering**: Reduserer sårbarhetsoverflaten ved å unngå egendefinerte autentiseringsimplementeringer
2. **Sikkerhet på Bedriftsnivå**: Benytter etablerte identitetsleverandører som Microsoft Entra ID med avanserte sikkerhetsfunksjoner
3. **Sentralisert Identitetsadministrasjon**: Forenkler bruker livssyklusadministrasjon, tilgangskontroll og samsvarsevaluering
4. **Flerfaktorautentisering**: Arver MFA-funksjonalitet fra bedriftsidentitetsleverandører
5. **Betingede Tilgangspolicyer**: Drar nytte av risikobaserte tilgangskontroller og adaptiv autentisering

**Implementeringskrav:**
- **Klientregistrering**: Foretrekk Klient ID Metadata-dokumenter eller
  forhåndsregistrering; bruk kun foreldet Dynamisk Klientregistrering for
  kompatibilitet
- **Token Målgruppevalidering**: Verifiser at alle tokens er eksplisitt utstedt for MCP-serveren
- **Utstederverifikasjon**: Valider at token-utsteder samsvarer med forventet identitetsleverandør
- **Signaturverifikasjon**: Kryptografisk validering av token-integritet
- **Utløpshåndhevelse**: Streng håndhevelse av tokenets levetidsbegrensninger
- **Omfangsvalidering**: Sørg for at tokens inneholder passende rettigheter for forespurte operasjoner

### **Autorisasjonslogikk Sikkerhet**

**Kritiske Kontroller:**
- **Omfattende Autorisasjonsrevisjoner**: Regelmessige sikkerhetsgjennomganger av alle autorisasjonsbeslutningspunkter
- **Failsafe-Standarder**: Avslå tilgang når autorisasjonslogikk ikke kan ta en definitiv beslutning
- **Tillatelsesgrenser**: Klar separasjon mellom ulike privilegienivåer og ressursadgang
- **Revisjonslogging**: Fullstendig logging av alle autorisasjonsbeslutninger for sikkerhetsovervåking
- **Regelmessige Tilgangsrevisjoner**: Periodisk validering av brukerrettigheter og privilegietildelinger

## 2. **Tokensikkerhet og Anti-Passthrough-kontroller**

**OWASP MCP Risiko Adresse:** [MCP01 - Tokenfeilbehandling & Eksponering av Hemmeligheter](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Forebygging av Token Passthrough**

**Token passthrough er uttrykkelig forbudt** i MCP Autorisasjon Spesifikasjonen på grunn av kritiske sikkerhetsrisikoer:

**Sikkerhetsrisikoer som adresseres:**
- **Omgåelse av Kontroller**: Omgår essensielle sikkerhetskontroller som ratebegrensning, forespørselsvalidering og trafikkovervåking
- **Ansvarsbrudd**: Gjør klientidentifisering umulig, noe som korrumperer revisjonsspor og hendelsesetterforskning
- **Proxy-basert Utsuging**: Gjør det mulig for ondsinnede aktører å bruke servere som mellomledd for uautorisert dataadgang
- **Brudd på Tillitsgrenser**: Bryter nedstrøms tjenestetillitsantakelser om token-opprinnelse
- **Sideveis Bevegelse**: Kompromitterte tokens på tvers av flere tjenester muliggjør bredere angrep

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

**Beste praksis:**
- **Kortvarige Tokens**: Minimér eksponeringsvinduet med hyppig tokenrotasjon
- **Just-in-Time Utstedelse**: Utsted tokens kun når nødvendig for spesifikke operasjoner
- **Sikker Lagring**: Bruk hardware-sikkerhetsmoduler (HSM) eller sikre nøkkellagre
- **Token Binding**: Verifiser tokenmålgruppe og utsteder for tilsiktet MCP
  ressurs, klient og operasjon
- **Overvåkning & Varsling**: Sanntidsdeteksjon av tokenmisbruk eller uautorisert tilgangsmønster

## 3. **Applikasjonsstat Sikkerhetskontroller**

### **Forebygging av Kapring av Statshåndtak**

**Angrepsvektorer som adresseres:**
- **Gjetting av Håndtak**: Forutsigbare identifikatorer eksponerer en annen brukers tilstand
- **Gjenbruk på tvers av brukere**: Et stjålet håndtak brukes med en annen identitet
- **Implisitt Autorisasjon**: Besittelse av et håndtak blir feilaktig behandlet som
  bevis på tilgang

**Statshåndtak Kontroller:**

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

**Transport Sikkerhet:**
- **HTTPS Håndhevelse**: Krev HTTPS for ekstern HTTP transport
- **Håndtering av Legitimasjon**: Send og verifiser autorisasjon ved hver HTTP-forespørsel
- **Stdio-Isolasjon**: Beskytt lokale stdio-servere gjennom prosessisolasjon og
  miljølegitimationskontroller

### **Tilstandsbasert vs Tilstandsløs Vurdering**

MCP `2026-07-28` er tilstandsløst på protokollaget. Applikasjoner kan likevel
opprettholde tilstand ved å returnere et eksplisitt håndtak fra ett verktøy-kall og akseptere
det som et ordinært argument ved senere kall.

- Lagre tilstand uavhengig av noen enkelt transportforbindelse.
- Bind tilstandshåndtak til den autentiserte prinsippserveren.
- Behandle et håndtak som et navn, ikke som en bærerlegitimasjon.
- Definer utløps- og gjenopprettingsadferd for utdaterte håndtak.

## 4. **AI-Spesifikke Sikkerhetskontroller**

**OWASP MCP Risikoer Adressert:**
- [MCP06 - Undergravelse av Intensjonsflyt](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Verktøyforgiftning](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Kommandoinjeksjon & Utførelse](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Forsvar mot Prompt-injeksjon**

**Microsoft Prompt Shields Integrasjon:**
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
- **Inndata Rensing**: Omfattende validering og filtrering av alle brukerinput
- **Definisjon av Innholdsgrenser**: Klar separasjon mellom systeminstruksjoner og brukerinhold
- **Instruksjonshierarki**: Korrekte prioritetsregler for motstridende instruksjoner
- **Utdataovervåking**: Deteksjon av potensielt skadelig eller manipulert output

### **Forebygging av Verktøyforgiftning**

**Verktøysikkerhetsrammeverk:**
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

**Dynamisk Verktøystyring:**
- **Godkjenningsarbeidsflyter**: Eksplisitt brukersamtykke for verktøymodifikasjoner
- **Mulighet for Tilbakerulling**: Evne til å gå tilbake til tidligere verktøyversjoner
- **Endringsrevisjon**: Fullstendig historikk over endringer i verktøydefinisjoner
- **Risikovurdering**: Automatisert evaluering av verktøysikkerhetsstatus

## 5. **Forebygging av Forvirret Fullmektig Angrep**

### **OAuth Proxy-sikkerhet**

**Forebyggingskontroller:**
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
- **Klientregistrering**: Foretrekk forhåndsregistrering eller Klient ID Metadata-
  dokumenter; behandle Dynamisk Klientregistrering som en kompatibilitets-tilbakefall
- **Brukersamtykke Verifikasjon**: MCP proxier som bruker en statisk tredjeparts klient-
  ID må innhente per-klient samtykke før autorisasjon videresendes
- **Redirect URI Validering**: Streng hvitelistebasert validering av redirect-destinasjoner
- **Beskyttelse av Autorisasjonskode**: Koder med kort levetid og enkeltbruk-kontroll
- **Klientidentitetsverifikasjon**: Robust validering av klientlegitimasjon og metadata

## 6. **Verktøyutførelsessikkerhet**

### **Sandboxing & Isolasjon**

**Container-basert Isolasjon:**
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
- **Separate Prosesskontekster**: Hver verktøyutførelse i isolert prosessrom
- **Mellomprosesskommunikasjon**: Sikre IPC-mekanismer med validering
- **Prosessovervåking**: Analyse av kjøretidsadferd og deteksjon av anomalier
- **Ressurshåndhevelse**: Tøffe begrensninger på CPU, minne og I/O-operasjoner

### **Implementering av Minste Privilegium**

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

## 7. **Sikringskontroller for Leverandørkjeden**

**OWASP MCP Risiko Adresse:** [MCP04 - Angrep på Programvareleverandørkjede & Avhengighetsmanipulering](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Avhengighetsverifikasjon**

**Omfattende Komponentsikkerhet:**
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

### **Kontinuerlig Overvåkning**

**Trusseldeteksjon i Leverandørkjeden:**
- **Avhengighetshelseovervåkning**: Kontinuerlig vurdering av alle avhengigheter for sikkerhetsproblemer
- **Trusselintelligensintegrasjon**: Sanntidsoppdateringer på nye trusler i leverandørkjeden
- **Adferdsanalyse**: Deteksjon av unormal adferd i eksterne komponenter
- **Automatisk Respons**: Øyeblikkelig inneslutning av kompromitterte komponenter

## 8. **Overvåkings- og Deteksjonskontroller**

**OWASP MCP Risiko Adresse:** [MCP08 - Manglende Revisjons- og Telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Sikkerhetsinformasjon og Hendelseshåndtering (SIEM)**

**Omfattende Loggingsstrategi:**
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

### **Sanntids Trusseldeteksjon**

**Adferdsanalyse:**
- **Brukeradferdsanalyse (UBA)**: Deteksjon av uvanlige brukertilgangsmønstre
- **Enhetsadferdsanalyse (EBA)**: Overvåking av MCP-server og verktøyadferd
- **Maskinlæring Anomali-deteksjon**: AI-drevet identifisering av sikkerhetstrusler
- **Sammenstilling av Trusselintelligens**: Matching av observerte aktiviteter mot kjente angrepsmønstre

## 9. **Hendelsesrespons & Gjenoppretting**

### **Automatiserte Responsmuligheter**

**Umiddelbare Responshandlinger:**
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

### **Forensiske Muligheter**

**Støtte til Undersøkelser:**
- **Bevaring av Revisjonsspor**: Uforanderlig logging med kryptografisk integritet
- **Innsamling av Bevis**: Automatisert innsamling av relevante sikkerhetsartefakter
- **Tidslinjegjenskaping**: Detaljert sekvens av hendelser som ledet til sikkerhetshendelser
- **Virkningsevaluering**: Vurdering av omfanget av kompromiss og dataeksponering

## **Nøkkelelementer i Sikkerhetsarkitekturen**

### **Forsvar i Dybdens Prinsipp**
- **Multiple Sikkerhetslag**: Ingen enkelt feilpunkt i sikkerhetsarkitekturen
- **Redundante Kontroller**: Overlappende sikkerhetstiltak for kritiske funksjoner
- **Failsafe-mekanismer**: Sikkre standarder når systemer møter feil eller angrep

### **Implementering av Null Tillit**
- **Aldri Stol, Alltid Verifiser**: Kontinuerlig validering av alle enheter og forespørsler
- **Prinsipp om Minste Privilegium**: Minimale tilgangsrettigheter for alle komponenter
- **Mikrosementering**: Granulære nettverks- og tilgangskontroller

### **Kontinuerlig Sikkerhetsevolusjon**
- **Tilpasning til Trussellandskap**: Regelmessige oppdateringer for å håndtere nye trusler
- **Effektivitet av Sikkerhetskontroller**: Pågående evaluering og forbedring av kontroller
- **Overholdelse av Spesifikasjoner**: Tilpasning til utviklende MCP sikkerhetsstandarder

---

## **Ressurser for Implementering**

### **Offisiell MCP Dokumentasjon**
- [MCP Spesifikasjon (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Sikkerhetsbeste Praksis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisasjon Spesifikasjon](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Sikkerhetsressurser**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattende OWASP MCP Top 10 med Azure implementering
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Offisielle OWASP MCP sikkerhetsrisikoer
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhetstrening for MCP på Azure

### **Microsoft Sikkerhetsløsninger**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sikkerhetsstandarder**
- [OAuth 2.0 Sikkerhetsbeste Praksis (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Store Språkmodeller](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Viktig:** Disse sikkerhetskontrollene gjenspeiler MCP-spesifikasjonen
> `2026-07-28`. Verifiser alltid mot
> [gjeldende offisielle dokumentasjon](https://modelcontextprotocol.io/specification/2026-07-28/)
> da standarder fortsetter å utvikle seg.

## Hva er det neste

- Gå tilbake til: [Security Module Overview](./README.md)
- Fortsett til: [Modul 3: Komme i gang](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
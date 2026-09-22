# MCP Säkerhetskontroller - Uppdatering September 2026

> **Aktuell standard:** Detta dokument speglar
> [MCP-specifikation 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> och den officiella
> [MCP Säkerhetsbästa praxis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) har mognat avsevärt med förbättrade säkerhetskontroller som hanterar både traditionell mjukvarusäkerhet och AI-specifika hot. Detta dokument ger omfattande säkerhetskontroller för säkra MCP-implementationer i linje med OWASP MCP Top 10-ramverket.

## 🏔️ Praktisk säkerhetsutbildning

För praktisk, hands-on erfarenhet av säkerhetsimplementering rekommenderar vi **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - en omfattande guidning för att säkra MCP-servrar i Azure med en metodik "sårbar → utnyttja → fixa → validera".

Alla säkerhetskontroller i detta dokument är i linje med **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, som tillhandahåller referensarkitekturer och Azure-specifik implementeringsvägledning för OWASP MCP Top 10 risker.

## **OBLIGATORISKA säkerhetskrav**

### **Kritiska förbud från MCP-specifikationen:**

> **FÖRBJUDET**: MCP-servrar **FÅR INTE** acceptera några tokens som inte uttryckligen utfärdats för MCP-servern
>
> **FÖRBJUDET**: MCP-servrar **FÅR INTE** använda sessioner för autentisering  
>
> **KRÄVT**: MCP-servrar som implementerar auktorisation **MÅSTE** verifiera ALLA inkommande förfrågningar
>
> **OBLIGATORISKT**: MCP-proxyservrar som använder en statisk tredje parts klient-ID
> **MÅSTE** erhålla samtycke för varje MCP-klient innan vidarebefordran av auktorisation

---

## 1. **Autentisering och auktorisationskontroller**

### **Integration med extern identitetsleverantör**

**MCP-specifikation `2026-07-28`** tillåter att MCP-servrar delegerar
autentisering till externa identitetsleverantörer. Auktorisation för HTTP-
transporter utvärderas per förfrågan; lokala stdio-servrar hämtar istället
referenser från sin miljö.

**OWASP MCP Risk adresserad**: [MCP07 - Otillräcklig autentisering och auktorisation](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Säkerhetsfördelar:**
1. **Eliminerar anpassade autentiseringsrisker**: Minskar sårbarhetsytan genom att undvika anpassade autentiseringsimplementationer
2. **Företagsklass säkerhet**: Utnyttjar etablerade identitetsleverantörer som Microsoft Entra ID med avancerade säkerhetsfunktioner
3. **Centraliserad identitetshantering**: Förenklar användarhantering, åtkomstkontroll och regelefterlevnadsrevision
4. **Multifaktorautentisering**: Ärver MFA-funktionalitet från företagsidentitetsleverantörer
5. **Villkorliga åtkomstpolicyer**: Drar nytta av riskbaserade åtkomstkontroller och adaptiv autentisering

**Implementeringskrav:**
- **Klientregistrering**: Föredra Client ID Metadata-dokument eller
  förregistrering; använd föråldrad dynamisk klientregistrering endast för
  kompatibilitet
- **Verifiering av tokenmottagare**: Verifiera att alla tokens uttryckligen är utfärdade för MCP-servern
- **Utfärdaranteverifiering**: Validera att tokenutfärdare matchar förväntad identitetsleverantör
- **Signaturverifiering**: Kryptografisk validering av tokenintegritet
- **Efterlevnad av utgångstid**: Strikt efterlevnad av tokens giltighetstid
- **Scope-validering**: Säkerställ att tokens innehåller lämpliga behörigheter för begärda operationer

### **Säkerhet för auktorisationslogik**

**Kritiska kontroller:**
- **Omfattande auktorisationsrevisioner**: Regelbundna säkerhetsgranskningar av alla auktorisationsbeslutspunkter
- **Fail-safe standardvärden**: Neka åtkomst när auktorisationslogiken inte kan fatta ett definitivt beslut
- **Behörighetsgränser**: Tydlig separation mellan olika privilegienivåer och resursåtkomst
- **Auditloggning**: Komplett loggning av alla auktorisationsbeslut för säkerhetsövervakning
- **Regelbunden åtkomstgranskning**: Periodisk validering av användarbehörigheter och privilegietilldelningar

## 2. **Tokensäkerhet och anti-passthrough kontroller**

**OWASP MCP Risk adresserad**: [MCP01 - Felhantering av tokens och exponering av hemligheter](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Förebyggande av token-passthrough**

**Token-passthrough är uttryckligen förbjudet** i MCP Auktorisationsspecifikationen på grund av kritiska säkerhetsrisker:

**Säkerhetsrisker som hanteras:**
- **Kontrollomgåelse**: Omgår viktiga säkerhetskontroller som hastighetsbegränsning, förfrågningsvalidering och trafikövervakning
- **Ansvarsutredningsbrott**: Gör det omöjligt att identifiera klienter, vilket förstör revisionsloggar och incidentutredningar
- **Proxybaserad exfiltration**: Gör det möjligt för illasinnade aktörer att använda servrar som proxies för obehörig dataåtkomst
- **Överträdelse av förtroendegränser**: Bryter nedströms tjänsters förtroendeantaganden om tokens ursprung
- **Laterala rörelser**: Komprometterade tokens på flera tjänster möjliggör bredare attackexpansion

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
- **Kortlivade tokens**: Minimera exponeringstid genom frekvent tokenrotation
- **Just-in-time utfärdande**: Utfärda tokens endast när de behövs för specifika operationer
- **Säker lagring**: Använd hårdvarusäkerhetsmoduler (HSM) eller säkra nyckelförråd
- **Tokenbindning**: Validera tokenmottagare och utfärdare för avsedd MCP-
  resurs, klient och operation
- **Övervakning och larm**: Realtidsdetektion av tokenmissbruk eller obehöriga åtkomstmönster

## 3. **Applikationstillståndssäkerhetskontroller**

### **Förebyggande av kapning av tillståndshanterare**

**Angreppsvägar som hanteras:**
- **Gissning av handtag**: Förutsägbara identifierare exponerar en annan användares tillstånd
- **Återanvändning mellan användare**: Ett stulet handtag används med en annan identitet
- **Implicit auktorisation**: Innehav av ett handtag behandlas felaktigt som
  bevis på åtkomst

**Kontroller för tillståndshanterare:**

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

**Transportssäkerhet:**
- **HTTPS-krav**: Kräver HTTPS för fjärr-HTTP-transporter
- **Hantering av referenser**: Skicka och validera auktorisation vid varje HTTP-förfrågan
- **Isolation av stdio**: Skydda lokala stdio-servrar genom procesisolering och
  kontroller av miljö- och referenshantering

### **Stateless kontra stateful överväganden**

MCP `2026-07-28` är stateless på protokollskiktet. Applikationer kan fortfarande
upprätthålla tillstånd genom att returnera ett explicit handtag från ett verktygssamtal och acceptera
det som ett vanligt argument vid senare anrop.

- Spara tillstånd oberoende av någon enskild transportanslutning.
- Binda tillståndshandtag till den autentiserade huvudprincipen serversidan.
- Behandla ett handtag som ett namn, inte som en bärare av referenser.
- Definiera utgångs- och återställningsbeteende för föråldrade handtag.

## 4. **AI-specifika säkerhetskontroller**

**OWASP MCP-risker adresserade**:

- [MCP06 - Subversion av avsiktsflöde](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Verktygsförgiftning](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Kommandoinjektion & Exekvering](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Försvar mot promptinjektion**

**Integration av Microsoft Prompt Shields:**
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
- **Definition av innehållsgräns**: Tydlig separation mellan systeminstruktioner och användarinnehåll
- **Instruktionshierarki**: Korrekt prioriteringsregler för motstridiga instruktioner
- **Övervakning av utdata**: Upptäckt av potentiellt skadliga eller manipulerade utdata

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
- **Godkännande arbetsflöden**: Explicit användarsamtycke för verktygsändringar
- **Återställningsmöjligheter**: Möjlighet att återgå till tidigare verktygsversioner
- **Ändringsrevision**: Fullständig historik över förändringar av verktygsdefinitioner
- **Riskbedömning**: Automatiserad utvärdering av verktygs säkerhetsläge

## 5. **Förebyggande av angrepp som förväxlar ombud**

### **OAuth-proxyssäkerhet**

**Kontroller för att förebygga angrepp:**
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
- **Klientregistrering**: Föredra förregistrering eller Client ID Metadata
  Dokument; behandla dynamisk klientregistrering som en kompatibilitetsreserv
- **Verifiering av användarsamtycke**: MCP-proxyer som använder en statisk tredjepartsklient
  måste inhämta samtycke per klient innan vidarebefordran av auktorisering
- **Validering av Redirect URI**: Strikt vitlistningsbaserad validering av omdirigeringsdestinationer
- **Skydd av auktoriseringskod**: Kortlivade koder med engångsanvändning
- **Verifiering av klientidentitet**: Robusta valideringar av klientuppgifter och metadata

## 6. **Verktygsexekveringssäkerhet**

### **Sandboxing & isolering**

**Isolering baserat på container:**
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
- **Inter-processkommunikation**: Säker IPC med validering
- **Processövervakning**: Analys av körbeteende och anomalidetektion
- **Resurskontroll**: Hårda gränser för CPU, minne och I/O-operationer

### **Tillämpning av minsta privilegium**

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

## 7. **Kontroller för leverantörskedjesäkerhet**

**OWASP MCP-risk adresserad**: [MCP04 - Programvaruleverantörskedjeattacker & manipulation av beroenden](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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

**Hotdetektion i leverantörskedjan:**
- **Övervakning av beroendehälsa**: Kontinuerlig bedömning av alla beroenden för säkerhetsproblem
- **Integrering av hotintelligens**: Uppdateringar i realtid om nya hot i leverantörskedjor
- **Beteendeanalys**: Upptäckt av ovanligt beteende i externa komponenter
- **Automatiserad respons**: Omedelbart ingripande vid komprometterade komponenter

## 8. **Kontroller för övervakning & detektion**

**OWASP MCP-risk adresserad**: [MCP08 - Brist på revision och telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

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
- **Användarbeteendeanalys (UBA)**: Upptäckt av ovanliga användarmönster
- **Entity Behavior Analytics (EBA)**: Övervakning av MCP-server och verktygsbeteende
- **Maskininlärningsbaserad anomalidetektion**: AI-driven identifiering av säkerhetshot
- **Korrelaton med hotintelligens**: Matchning av observerade aktiviteter mot kända angreppsmönster

## 9. **Incidenthantering & återhämtning**

### **Automatiserade responsegenskaper**

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

### **Forensiska egenskaper**

**Stöd vid utredning:**
- **Bevarande av revisionsspår**: Oföränderlig loggning med kryptografisk integritet
- **Insamling av bevis**: Automatiserad insamling av relevanta säkerhetsartefakter
- **Tidslinjekonstruktion**: Detaljerad sekvens av händelser före säkerhetsincidenter
- **Påverkansbedömning**: Utvärdering av kompromissens omfattning och dataexponering

## **Viktiga principer för säkerhetsarkitektur**

### **Försvar i djupet**
- **Flera säkerhetslager**: Ingen ensam svag punkt i säkerhetsarkitekturen
- **Redundanta kontroller**: Överlappande säkerhetsåtgärder för kritiska funktioner
- **Säkra felsäkra mekanismer**: Säkra standardvärden när system möter fel eller angrepp

### **Zero Trust-implementering**
- **Lita aldrig, verifiera alltid**: Kontinuerlig validering av alla enheter och förfrågningar
- **Principen om minsta privilegium**: Minimala åtkomsträttigheter för alla komponenter
- **Mikrosegmentering**: Granulära nätverks- och åtkomstkontroller

### **Kontinuerlig säkerhetsutveckling**
- **Anpassning till hotlandskapet**: Regelbundna uppdateringar för att hantera nya hot
- **Effektivitet i säkerhetskontroller**: Löpande utvärdering och förbättring av kontroller
- **Efterlevnad av specifikationer**: Anpassning till utvecklande MCP-säkerhetsstandarder

---

## **Implementeringsresurser**

### **Officiell MCP-dokumentation**
- [MCP-specifikation (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP säkerhetsbästa praxis](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP auktoriseringsspecifikation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP säkerhetsresurser**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Omfattande OWASP MCP Top 10 med Azure-implementering
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officiella OWASP MCP säkerhetsrisker
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk säkerhetsträning för MCP på Azure

### **Microsoft säkerhetslösningar**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Säkerhetsstandarder**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Topp 10 för Stora Språkmodeller](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Viktigt:** Dessa säkerhetskontroller speglar MCP-specifikationen
> `2026-07-28`. Verifiera alltid mot
> [den aktuella officiella dokumentationen](https://modelcontextprotocol.io/specification/2026-07-28/)
> eftersom standarder fortsätter att utvecklas.

## Vad händer härnäst

- Gå tillbaka till: [Security Module Overview](./README.md)
- Fortsätt till: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
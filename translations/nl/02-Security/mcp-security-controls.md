# MCP Beveiligingscontroles - Update september 2026

> **Huidige standaard:** Dit document weerspiegelt
> [MCP Specificatie 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> en de officiële
> [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Het Model Context Protocol (MCP) is aanzienlijk gevorderd met verbeterde beveiligingscontroles die zowel traditionele softwarebeveiliging als AI-specifieke bedreigingen aanpakken. Dit document biedt uitgebreide beveiligingscontroles voor veilige MCP-implementaties die zijn afgestemd op het OWASP MCP Top 10-framework.

## 🏔️ Praktische Beveiligingstraining

Voor praktische, hands-on ervaring met beveiligingsimplementatie raden wij de **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** aan - een uitgebreide begeleide expeditie voor het beveiligen van MCP-servers in Azure met een "kwetsbaar → exploit → fix → valideer" methodiek.

Alle beveiligingscontroles in dit document zijn in overeenstemming met de **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, die referentiearchitecturen en Azure-specifieke implementatie-instructies biedt voor de OWASP MCP Top 10-risico's.

## **VERPLICHTE Beveiligingseisen**

### **Kritieke Verboden uit MCP Specificatie:**

> **VERBODEN**: MCP-servers **MOGEN GEEN** tokens accepteren die niet expliciet zijn uitgegeven voor de MCP-server
>
> **VERBODEN**: MCP-servers **MOGEN GEEN** sessies gebruiken voor authenticatie  
>
> **VEREIST**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren
>
> **VERPLICHT**: MCP proxy-servers die een statische third-party client-ID gebruiken
> **MOETEN** toestemming verkrijgen voor elke MCP-client voordat autorisatie wordt doorgestuurd

---

## 1. **Authenticatie- & Autorisatiecontroles**

### **Integratie van Externe Identity Provider**

**MCP Specificatie `2026-07-28`** staat MCP-servers toe om
authenticatie te delegeren aan externe identity providers. Autorisatie voor HTTP-
transporten wordt per verzoek geëvalueerd; lokale stdio-servers verkrijgen
in plaats daarvan hun referenties uit hun omgeving.

**Aanpak van OWASP MCP Risico**: [MCP07 - Onvoldoende Authenticatie & Autorisatie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Beveiligingsvoordelen:**
1. **Elimineert Risico's bij Aangepaste Authenticatie**: Vermindert het aanvalsoppervlak door aangepaste authenticatie-implementaties te vermijden
2. **Enterprise-Class Beveiliging**: Maakt gebruik van gevestigde identity providers zoals Microsoft Entra ID met geavanceerde beveiligingsfuncties
3. **Gecentraliseerd Identiteitsbeheer**: Vereenvoudigt levenscyclusbeheer van gebruikers, toegangscontrole en compliance-audits
4. **Multi-Factor Authenticatie**: Erft MFA-mogelijkheden van enterprise identity providers
5. **Conditionele Toegangsbeleid**: Profiteert van risicogebaseerde toegangscontrole en adaptieve authenticatie

**Implementatievereisten:**
- **Clientregistratie**: Geef de voorkeur aan Client ID Metadata Documenten of
  preregistratie; gebruik verouderde Dynamische Clientregistratie alleen voor
  compatibiliteit
- **Validatie van Token Audience**: Verifieer dat alle tokens expliciet zijn uitgegeven voor de MCP-server
- **Issuer Verificatie**: Valideer dat de tokenuitgever overeenkomt met de verwachte identity provider
- **Handtekeningverificatie**: Cryptografische validatie van tokenintegriteit
- **Handhaving van Verlooptijd**: Strikte naleving van tokenlevensduurlimieten
- **Scope Validatie**: Zorg dat tokens de juiste machtigingen bevatten voor de gevraagde operaties

### **Beveiliging van Autorisatielogica**

**Kritieke Controles:**
- **Uitgebreide Autorisatieaudits**: Regelmatige beveiligingsbeoordelingen van alle autorisatiebeslissingen
- **Veilige Standaardinstellingen**: Toegang weigeren wanneer autorisatielogica geen definitieve beslissing kan maken
- **Machtigingsgrenzen**: Duidelijke scheiding tussen verschillende privilege- en resource-toegangsniveaus
- **Auditlogboekregistratie**: Volledige logging van alle autorisatiebeslissingen voor beveiligingsmonitoring
- **Regelmatige Toegangsevaluaties**: Periodieke validatie van gebruikersrechten en privilege-toewijzingen

## 2. **Tokenbeveiliging & Anti-Passthrough Controles**

**Aanpak van OWASP MCP Risico**: [MCP01 - Token verkeerd beheer & Geheimenblootstelling](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Preventie van Token Passthrough**

**Token passthrough is uitdrukkelijk verboden** in de MCP Autorisatiespecificatie vanwege kritieke beveiligingsrisico's:

**Aangepakte beveiligingsrisico's:**
- **Omzeiling van Beheersmaatregelen**: Omzeilt essentiële beveiligingscontroles zoals rate limiting, verzoekvalidatie en verkeersmonitoring
- **Verlies van Verantwoordingsplicht**: Maakt clientidentificatie onmogelijk, wat auditsporen en incidentonderzoek ondermijnt
- **Proxy-gebaseerde Exfiltratie**: Maakt het voor kwaadwillenden mogelijk om servers als proxy te gebruiken voor ongeoorloofde data-toegang
- **Overtreding van Vertrouwensgrenzen**: Doorbreekt aannames over token-bronnen bij downstreamdiensten
- **Laterale Beweging**: Gecompromitteerde tokens over meerdere diensten maken bredere aanvalsexpansie mogelijk

**Implementatiecontroles:**
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

### **Veilige Tokenbeheerpatronen**

**Beste Praktijken:**
- **Kortstondige Tokens**: Minimaliseer blootstellingsperiode door frequente tokenrotatie
- **Just-in-Time Uitgifte**: Geef tokens alleen uit wanneer nodig voor specifieke operaties
- **Veilige Opslag**: Gebruik hardware security modules (HSM's) of beveiligde sleutelkasten
- **Tokenbinding**: Valideer het tokenpubliek en de uitgever voor de bedoelde MCP-
  resource, client en operatie
- **Monitoring & Alerting**: Real-time detectie van tokenmisbruik of ongeautoriseerde toegangs-patronen

## 3. **Beveiligingscontroles voor Applicatiestatus**

### **Voorkomen van Overname van Statushandle**

**Aanvalsvectoren aangepakt:**
- **Raadspel Handle**: Voorspelbare identificatoren onthullen de status van een andere beller
- **Herbruik door Andere Gebruiker**: Een gestolen handle wordt gebruikt met een andere identiteit
- **Impliciete Autorisatie**: Het bezitten van een handle wordt ten onrechte beschouwd als
  bewijs van toegang

**Statushandle-controles:**

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

**Transportbeveiliging:**
- **HTTPS-verplichting**: HTTPS verplicht stellen voor externe HTTP-transporten
- **Referentiebehandeling**: Autorisatie verzenden en valideren bij ieder HTTP-verzoek
- **stdio-isolatie**: Lokale stdio-servers beschermen via procesisolatie en
  referentiecontroles in de omgeving

### **Overwegingen stateless vs stateful**

MCP `2026-07-28` is stateless op protocolniveau. Applicaties kunnen nog steeds
staat bijhouden door een expliciete handle terug te geven vanuit een toolaanroep en
die als gewone argument te accepteren bij latere aanroepen.

- Houd staat onafhankelijk van een enkele transportverbinding.
- Bind statushandles aan de geauthentiseerde principal aan de serverzijde.
- Behandel een handle als een naam, niet als een bearer-referentie.
- Definieer verlopen en herstelgedrag voor verouderde handles.

## 4. **AI-specifieke Beveiligingscontroles**

**OWASP MCP Risico's aangepakt:**
- [MCP06 - Intentiestroom Subversie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Toolvergiftiging](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Command Injection & Executie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Verdediging tegen Promptinjectie**

**Integratie Microsoft Prompt Shields:**
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

**Implementatiecontroles:**
- **Invoersanering**: Uitgebreide validatie en filtering van alle gebruikersinvoer
- **Definitie Inhoudsgrenzen**: Duidelijke scheiding tussen systeeminstructies en gebruikersinhoud
- **Instructiehiërarchie**: Juiste prioriteitsregels bij conflicterende instructies
- **Outputmonitoring**: Detectie van mogelijk schadelijke of gemanipuleerde output

### **Preventie van Toolvergiftiging**

**Toolbeveiligingsraamwerk:**
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

**Dynamisch Toolbeheer:**
- **Goedkeuringsworkflows**: Expliciete gebruikstoestemming voor toolaanpassingen
- **Rollback-mogelijkheden**: Mogelijkheid om terug te keren naar eerdere toolversies
- **Wijzigingsaudit**: Volledige geschiedenis van tooldefinitie-aanpassingen
- **Risicobeoordeling**: Geautomatiseerde evaluatie van de beveiligingsstatus van tools

## 5. **Voorkoming van Confused Deputy-aanvallen**

### **OAuth Proxy Beveiliging**

**Preventiecontroles bij aanvallen:**
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

**Implementatievereisten:**
- **Clientregistratie**: Geef de voorkeur aan preregistratie of Client ID Metadata
  Documenten; behandel Dynamische Clientregistratie als een fallback voor compatibiliteit
- **Verificatie van Gebruikstoestemming**: MCP-proxy's met een statische third-party client-ID
  moeten per client toestemming verkrijgen vóór bevoegdheidoverdracht
- **Validatie Redirect URI**: Strikte whitelist-validatie van redirect-bestemmingen
- **Bescherming van Autorisatiecodes**: Kortdurende codes met single-use afdwinging
- **Verificatie van Clientidentiteit**: Robuuste validatie van clientreferenties en metadata

## 6. **Beveiliging bij Tooluitvoering**

### **Sandboxing & Isolatie**

**Containergebaseerde isolatie:**
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

**Procesisolatie:**
- **Gescheiden Procescontexten**: Elke tooluitvoering in een geïsoleerde procesruimte
- **Inter-procescommunicatie**: Veilige IPC-mechanismen met validatie
- **Procesmonitoring**: Gedragsanalyse tijdens runtime en detectie van anomalieën
- **Handhaving van bronnen**: Strikte limieten op CPU, geheugen en I/O-operaties

### **Implementatie van het Minimum Privilege**

**Beheer van Machtigingen:**
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

## 7. **Beveiligingscontroles voor Supply Chain**

**Aanpak van OWASP MCP Risico**: [MCP04 - Softwareketen Aanvallen & Dependency Manipulatie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verificatie van afhankelijkheden**

**Alomvattende componentbeveiliging:**
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

### **Continu Monitoring**

**Detectie van dreigingen in de supply chain:**
- **Monitoring van afhankelijkheidsgeschiktheid**: Continue beoordeling van alle afhankelijkheden op beveiligingsproblemen
- **Integratie van dreigingsinformatie**: Real-time updates over opkomende threats in de supply chain
- **Gedragsanalyse**: Detectie van ongewoon gedrag in externe componenten
- **Geautomatiseerde respons**: Onmiddellijke isolatie van gecompromitteerde componenten

## 8. **Monitoring- & Detectiecontroles**

**Aanpak van OWASP MCP Risico**: [MCP08 - Gebrek aan Audit en Telemetrie](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Security Information and Event Management (SIEM)**

**Uitgebreide loggingstrategie:**
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

### **Realtime Dreigingsdetectie**

**Gedragsanalyse:**
- **User Behavior Analytics (UBA)**: Detectie van ongewone gebruikerspatronen
- **Entity Behavior Analytics (EBA)**: Monitoring van MCP-server- en toolgedrag
- **Machine Learning Anomaliedetectie**: AI-gestuurde identificatie van beveiligingsdreigingen
- **Correlatie met dreigingsinformatie**: Afstemming van geobserveerde activiteiten op bekende aanvalspatronen

## 9. **Incidentrespons & Herstel**

### **Geautomatiseerde responsmogelijkheden**

**Onmiddellijke reactiestappen:**
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

### **Forensische capaciteiten**

**Ondersteuning bij onderzoek:**
- **Behoud van auditsporen**: Onoverwinnelijke logging met cryptografische integriteit
- **Verzameling van bewijsmateriaal**: Geautomatiseerde verzameling van relevante beveiligingsartefacten
- **Reconstructie van tijdlijn**: Gedetailleerde volgorde van gebeurtenissen die leiden tot beveiligingsincidenten
- **Impactanalyse**: Evaluatie van omvang van compromittering en datablootstelling

## **Belangrijke principes van beveiligingsarchitectuur**

### **Defense in Depth**
- **Meerdere beveiligingslagen**: Geen enkel punt van falen in de beveiligingsarchitectuur
- **Redundante controles**: Overlappende beveiligingsmaatregelen voor kritieke functies
- **Fail-safe mechanismen**: Veilige standaardinstellingen bij fouten of aanvallen

### **Zero Trust Implementatie**
- **Nooit vertrouwen, altijd verifiëren**: Voortdurende validatie van alle entiteiten en verzoeken
- **Principe van minimaal privilege**: Minimale toegangsrechten voor alle componenten
- **Micro-segmentatie**: Gedetailleerde netwerk- en toegangscontroles

### **Continue beveiligingsevolutie**
- **Aanpassing aan dreigingslandschap**: Regelmatige updates om nieuwe dreigingen te adresseren
- **Effectiviteit van beveiligingscontroles**: Doorlopende evaluatie en verbetering van controles
- **Naleving van specificatie**: Afstemming op steeds evoluerende MCP beveiligingsstandaarden

---

## **Implementatieresources**

### **Officiële MCP-documentatie**
- [MCP Specificatie (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Beveiligingsresources**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Uitgebreide OWASP MCP Top 10 met Azure-implementatie
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officiële OWASP MCP beveiligingsrisico's
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on beveiligingstraining voor MCP op Azure

### **Microsoft Beveiligingsoplossingen**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Beveiligingsstandaarden**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 voor Large Language Models](https://genai.owasp.org/)

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Belangrijk:** Deze beveiligingscontroles weerspiegelen MCP Specificatie
> `2026-07-28`. Verifieer altijd aan de hand van de
> [huidige officiële documentatie](https://modelcontextprotocol.io/specification/2026-07-28/)
> aangezien de normen blijven evolueren.

## Wat nu

- Terug naar: [Overzicht van de beveiligingsmodule](./README.md)
- Verder naar: [Module 3: Aan de slag](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
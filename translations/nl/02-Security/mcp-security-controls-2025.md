# MCP Beveiligingscontroles - Update december 2025

> **Huidige standaard**: Dit document weerspiegelt de beveiligingseisen van [MCP Specificatie 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) en de officiële [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Het Model Context Protocol (MCP) is aanzienlijk volwassen geworden met verbeterde beveiligingscontroles die zowel traditionele softwarebeveiliging als AI-specifieke bedreigingen aanpakken. Dit document biedt uitgebreide beveiligingscontroles voor veilige MCP-implementaties per december 2025.

## **VERPLICHTE beveiligingseisen**

### **Kritieke verboden uit MCP-specificatie:**

> **VERBODEN**: MCP-servers **MOGEN GEEN** tokens accepteren die niet expliciet zijn uitgegeven voor de MCP-server  
>
> **VERBODEN**: MCP-servers **MOGEN GEEN** sessies gebruiken voor authenticatie  
>
> **VERPLICHT**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren  
>
> **VERPLICHT**: MCP-proxyservers die statische client-ID's gebruiken **MOETEN** gebruikersconsent verkrijgen voor elke dynamisch geregistreerde client

---

## 1. **Authenticatie- & Autorisatiecontroles**

### **Integratie van externe identiteitsprovider**

**Huidige MCP-standaard (2025-06-18)** staat toe dat MCP-servers authenticatie delegeren aan externe identiteitsproviders, wat een significante beveiligingsverbetering betekent:

### **Integratie van externe identiteitsprovider**

**Huidige MCP-standaard (2025-11-25)** staat toe dat MCP-servers authenticatie delegeren aan externe identiteitsproviders, wat een significante beveiligingsverbetering betekent:

**Beveiligingsvoordelen:**
1. **Elimineert risico's van aangepaste authenticatie**: Vermindert het aanvalsoppervlak door het vermijden van aangepaste authenticatie-implementaties  
2. **Enterprise-grade beveiliging**: Maakt gebruik van gevestigde identiteitsproviders zoals Microsoft Entra ID met geavanceerde beveiligingsfuncties  
3. **Gecentraliseerd identiteitsbeheer**: Vereenvoudigt gebruikerslevenscyclusbeheer, toegangscontrole en compliance-audits  
4. **Multi-factor authenticatie**: Erft MFA-mogelijkheden van enterprise identiteitsproviders  
5. **Voorwaardelijke toegangsbeleid**: Profiteert van risicogebaseerde toegangscontroles en adaptieve authenticatie  

**Implementatievereisten:**
- **Token Audience Validatie**: Verifieer dat alle tokens expliciet zijn uitgegeven voor de MCP-server  
- **Issuer Verificatie**: Valideer dat de token-uitgever overeenkomt met de verwachte identiteitsprovider  
- **Handtekeningverificatie**: Cryptografische validatie van tokenintegriteit  
- **Verloophandhaving**: Strikte handhaving van tokenlevensduur  
- **Scope Validatie**: Zorg dat tokens de juiste machtigingen bevatten voor de gevraagde operaties  

### **Beveiliging van autorisatielogica**

**Kritieke controles:**
- **Uitgebreide autorisatie-audits**: Regelmatige beveiligingsreviews van alle autorisatiebeslissingspunten  
- **Fail-safe defaults**: Toegang weigeren wanneer autorisatielogica geen definitieve beslissing kan nemen  
- **Machtigingsgrenzen**: Duidelijke scheiding tussen verschillende privilege-niveaus en resource-toegang  
- **Auditlogging**: Volledige logging van alle autorisatiebeslissingen voor beveiligingsmonitoring  
- **Regelmatige toegangsreviews**: Periodieke validatie van gebruikersrechten en privilege-toewijzingen  

## 2. **Tokenbeveiliging & Anti-Passthrough Controles**

### **Voorkoming van token-passthrough**

**Token-passthrough is expliciet verboden** in de MCP Autorisatiespecificatie vanwege kritieke beveiligingsrisico's:

**Beveiligingsrisico's aangepakt:**
- **Omzeiling van controles**: Omzeilt essentiële beveiligingscontroles zoals rate limiting, verzoekvalidatie en verkeersmonitoring  
- **Verlies van verantwoordelijkheid**: Maakt clientidentificatie onmogelijk, wat auditsporen en incidentonderzoek corrumpeert  
- **Proxy-gebaseerde exfiltratie**: Staat kwaadwillenden toe servers als proxy te gebruiken voor ongeautoriseerde data toegang  
- **Schending van vertrouwensgrenzen**: Doorbreekt aannames van downstream services over tokenherkomst  
- **Laterale beweging**: Gecompromitteerde tokens over meerdere services maken bredere aanvalsexpansie mogelijk  

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

### **Veilige tokenbeheerpatronen**

**Best practices:**
- **Kortdurende tokens**: Minimaliseer blootstellingsvenster met frequente tokenrotatie  
- **Just-in-time uitgifte**: Geef tokens alleen uit wanneer nodig voor specifieke operaties  
- **Veilige opslag**: Gebruik hardware security modules (HSM's) of beveiligde sleutelkluizen  
- **Tokenbinding**: Bind tokens aan specifieke clients, sessies of operaties waar mogelijk  
- **Monitoring & waarschuwingen**: Real-time detectie van tokenmisbruik of ongeautoriseerde toegangs-patronen  

## 3. **Sessiebeveiligingscontroles**

### **Voorkoming van sessiekaping**

**Aangevallen vectoren aangepakt:**
- **Sessiekaping promptinjectie**: Kwaadaardige gebeurtenissen geïnjecteerd in gedeelde sessiestatus  
- **Sessie-immitatie**: Ongeautoriseerd gebruik van gestolen sessie-ID's om authenticatie te omzeilen  
- **Hervatbare streamaanvallen**: Misbruik van server-sent event hervatting voor kwaadaardige contentinjectie  

**Verplichte sessiecontroles:**
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

**Transportbeveiliging:**
- **HTTPS-handhaving**: Alle sessiecommunicatie via TLS 1.3  
- **Veilige cookie-attributen**: HttpOnly, Secure, SameSite=Strict  
- **Certificaatpinning**: Voor kritieke verbindingen ter voorkoming van MITM-aanvallen  

### **Stateful vs Stateless overwegingen**

**Voor stateful implementaties:**
- Gedeelde sessiestatus vereist extra bescherming tegen injectieaanvallen  
- Wachtrij-gebaseerd sessiebeheer vereist integriteitsverificatie  
- Meerdere serverinstanties vereisen veilige synchronisatie van sessiestatus  

**Voor stateless implementaties:**
- JWT of vergelijkbaar token-gebaseerd sessiebeheer  
- Cryptografische verificatie van sessiestatusintegriteit  
- Verminderd aanvalsoppervlak maar vereist robuuste tokenvalidatie  

## 4. **AI-specifieke beveiligingscontroles**

### **Promptinjectie verdediging**

**Microsoft Prompt Shields integratie:**
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
- **Inputsanitatie**: Uitgebreide validatie en filtering van alle gebruikersinvoer  
- **Definitie van contentgrenzen**: Duidelijke scheiding tussen systeeminstructies en gebruikersinhoud  
- **Instructiehiërarchie**: Juiste prioriteitsregels voor conflicterende instructies  
- **Outputmonitoring**: Detectie van potentieel schadelijke of gemanipuleerde outputs  

### **Voorkoming van toolvergiftiging**

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

**Dynamisch toolbeheer:**
- **Goedkeuringsworkflows**: Expliciete gebruikersconsent voor toolwijzigingen  
- **Rollback-mogelijkheden**: Mogelijkheid om terug te keren naar eerdere toolversies  
- **Wijzigingsauditing**: Volledige geschiedenis van tooldefinitiewijzigingen  
- **Risicobeoordeling**: Geautomatiseerde evaluatie van toolbeveiligingspositie  

## 5. **Voorkoming van Confused Deputy-aanvallen**

### **OAuth Proxy-beveiliging**

**Aanvalsvoorkomende controles:**
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

**Implementatievereisten:**
- **Verificatie van gebruikersconsent**: Nooit consentschermen overslaan bij dynamische clientregistratie  
- **Redirect URI-validatie**: Strikte whitelist-gebaseerde validatie van redirectbestemmingen  
- **Bescherming van autorisatiecodes**: Kortdurende codes met eenmalige gebruiksafdwinging  
- **Clientidentiteitsverificatie**: Robuuste validatie van clientreferenties en metadata  

## 6. **Tooluitvoeringsbeveiliging**

### **Sandboxing & isolatie**

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
- **Gescheiden procescontexten**: Elke tooluitvoering in geïsoleerde procesruimte  
- **Inter-procescommunicatie**: Veilige IPC-mechanismen met validatie  
- **Procesmonitoring**: Runtime gedragsanalyse en anomaliedetectie  
- **Hulpbronnenhandhaving**: Strikte limieten op CPU, geheugen en I/O-operaties  

### **Implementatie van het minste privilege**

**Machtigingsbeheer:**
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

## 7. **Beveiligingscontroles voor de toeleveringsketen**

### **Verificatie van afhankelijkheden**

**Uitgebreide componentbeveiliging:**
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

### **Continue monitoring**

**Detectie van bedreigingen in de toeleveringsketen:**
- **Monitoring van afhankelijkheidsgezondheid**: Continue beoordeling van alle afhankelijkheden op beveiligingsproblemen  
- **Integratie van dreigingsinformatie**: Real-time updates over opkomende bedreigingen in de toeleveringsketen  
- **Gedragsanalyse**: Detectie van ongewoon gedrag in externe componenten  
- **Geautomatiseerde respons**: Onmiddellijke isolatie van gecompromitteerde componenten  

## 8. **Monitoring- & detectiecontroles**

### **Security Information and Event Management (SIEM)**

**Uitgebreide logstrategie:**
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

### **Realtime dreigingsdetectie**

**Gedragsanalyse:**
- **User Behavior Analytics (UBA)**: Detectie van ongebruikelijke gebruikerstoegangspatronen  
- **Entity Behavior Analytics (EBA)**: Monitoring van MCP-server- en toolgedrag  
- **Machine Learning anomaliedetectie**: AI-gestuurde identificatie van beveiligingsbedreigingen  
- **Dreigingsinformatiecorrelatie**: Afstemming van waargenomen activiteiten op bekende aanvalspatronen  

## 9. **Incidentrespons & herstel**

### **Geautomatiseerde responsmogelijkheden**

**Onmiddellijke responsacties:**
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

### **Forensische mogelijkheden**

**Ondersteuning bij onderzoek:**
- **Behoud van audittrail**: Onveranderlijke logging met cryptografische integriteit  
- **Verzameling van bewijsmateriaal**: Geautomatiseerde verzameling van relevante beveiligingsartefacten  
- **Tijdlijnreconstructie**: Gedetailleerde volgorde van gebeurtenissen die tot beveiligingsincidenten leiden  
- **Impactbeoordeling**: Evaluatie van de omvang van compromittering en datalekken  

## **Belangrijke beveiligingsarchitectuurprincipes**

### **Defense in Depth**
- **Meerdere beveiligingslagen**: Geen enkel punt van falen in de beveiligingsarchitectuur  
- **Redundante controles**: Overlappende beveiligingsmaatregelen voor kritieke functies  
- **Fail-safe mechanismen**: Veilige standaardinstellingen bij fouten of aanvallen  

### **Zero Trust-implementatie**
- **Nooit vertrouwen, altijd verifiëren**: Continue validatie van alle entiteiten en verzoeken  
- **Principe van minste privilege**: Minimale toegangsrechten voor alle componenten  
- **Micro-segmentatie**: Gedetailleerde netwerk- en toegangscontroles  

### **Continue beveiligingsevolutie**
- **Aanpassing aan dreigingslandschap**: Regelmatige updates om opkomende bedreigingen aan te pakken  
- **Effectiviteit van beveiligingscontroles**: Voortdurende evaluatie en verbetering van controles  
- **Specificatiecompliance**: Afstemming op evoluerende MCP-beveiligingsstandaarden  

---

## **Implementatieresources**

### **Officiële MCP-documentatie**
- [MCP Specificatie (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft beveiligingsoplossingen**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Beveiligingsstandaarden**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 voor Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Belangrijk**: Deze beveiligingscontroles weerspiegelen de huidige MCP-specificatie (2025-06-18). Verifieer altijd aan de hand van de nieuwste [officiële documentatie](https://spec.modelcontextprotocol.io/) aangezien standaarden snel blijven evolueren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
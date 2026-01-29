# MCP-Sicherheitskontrollen – Update Dezember 2025

> **Aktueller Standard**: Dieses Dokument spiegelt die Sicherheitsanforderungen der [MCP-Spezifikation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) und die offiziellen [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) wider.

Das Model Context Protocol (MCP) hat sich mit erweiterten Sicherheitskontrollen, die sowohl traditionelle Softwaresicherheit als auch KI-spezifische Bedrohungen adressieren, erheblich weiterentwickelt. Dieses Dokument bietet umfassende Sicherheitskontrollen für sichere MCP-Implementierungen ab Dezember 2025.

## **VERPFLICHTENDE Sicherheitsanforderungen**

### **Kritische Verbote aus der MCP-Spezifikation:**

> **VERBOTEN**: MCP-Server **DÜRFEN KEINE** Tokens akzeptieren, die nicht explizit für den MCP-Server ausgestellt wurden  
>
> **VERBOTEN**: MCP-Server **DÜRFEN KEINE** Sitzungen für die Authentifizierung verwenden  
>
> **ERFORDERLICH**: MCP-Server, die Autorisierung implementieren, **MÜSSEN** ALLE eingehenden Anfragen überprüfen  
>
> **VERPFLICHTEND**: MCP-Proxy-Server, die statische Client-IDs verwenden, **MÜSSEN** für jeden dynamisch registrierten Client die Zustimmung des Benutzers einholen

---

## 1. **Authentifizierungs- & Autorisierungskontrollen**

### **Integration externer Identitätsanbieter**

**Aktueller MCP-Standard (2025-06-18)** erlaubt MCP-Servern, die Authentifizierung an externe Identitätsanbieter zu delegieren, was eine bedeutende Sicherheitsverbesserung darstellt:

### **Integration externer Identitätsanbieter**

**Aktueller MCP-Standard (2025-11-25)** erlaubt MCP-Servern, die Authentifizierung an externe Identitätsanbieter zu delegieren, was eine bedeutende Sicherheitsverbesserung darstellt:

**Sicherheitsvorteile:**
1. **Eliminiert Risiken durch eigene Authentifizierung**: Reduziert die Angriffsfläche durch Vermeidung eigener Authentifizierungsimplementierungen  
2. **Enterprise-Grade Sicherheit**: Nutzt etablierte Identitätsanbieter wie Microsoft Entra ID mit fortschrittlichen Sicherheitsfunktionen  
3. **Zentralisiertes Identitätsmanagement**: Vereinfacht Benutzerlebenszyklusverwaltung, Zugriffskontrolle und Compliance-Audits  
4. **Multi-Faktor-Authentifizierung**: Übernimmt MFA-Fähigkeiten der Unternehmens-Identitätsanbieter  
5. **Bedingte Zugriffspolitiken**: Profitiert von risikobasierten Zugriffskontrollen und adaptiver Authentifizierung

**Implementierungsanforderungen:**
- **Token-Audience-Validierung**: Überprüfen, dass alle Tokens explizit für den MCP-Server ausgestellt sind  
- **Issuer-Überprüfung**: Validierung, dass der Token-Aussteller dem erwarteten Identitätsanbieter entspricht  
- **Signaturprüfung**: Kryptografische Validierung der Token-Integrität  
- **Ablaufdurchsetzung**: Strikte Einhaltung der Token-Lebensdauer  
- **Scope-Validierung**: Sicherstellen, dass Tokens die passenden Berechtigungen für angeforderte Operationen enthalten

### **Sicherheit der Autorisierungslogik**

**Kritische Kontrollen:**
- **Umfassende Autorisierungsprüfungen**: Regelmäßige Sicherheitsüberprüfungen aller Autorisierungsentscheidungen  
- **Fail-Safe-Standards**: Zugriff verweigern, wenn die Autorisierungslogik keine eindeutige Entscheidung treffen kann  
- **Berechtigungsgrenzen**: Klare Trennung zwischen verschiedenen Privilegienebenen und Ressourcen-Zugriffen  
- **Audit-Logging**: Vollständige Protokollierung aller Autorisierungsentscheidungen zur Sicherheitsüberwachung  
- **Regelmäßige Zugriffsüberprüfungen**: Periodische Validierung von Benutzerberechtigungen und Privilegienzuweisungen

## 2. **Token-Sicherheit & Anti-Passthrough-Kontrollen**

### **Verhinderung von Token-Passthrough**

**Token-Passthrough ist in der MCP-Autorisierungsspezifikation ausdrücklich verboten** aufgrund kritischer Sicherheitsrisiken:

**Adressierte Sicherheitsrisiken:**
- **Umgehung von Kontrollen**: Umgeht essenzielle Sicherheitskontrollen wie Ratenbegrenzung, Anfragevalidierung und Verkehrsüberwachung  
- **Verlust der Verantwortlichkeit**: Verhindert die Identifikation von Clients, was Audit-Trails und Vorfalluntersuchungen beeinträchtigt  
- **Proxy-basierte Exfiltration**: Ermöglicht Angreifern, Server als Proxies für unautorisierten Datenzugriff zu nutzen  
- **Verletzung von Vertrauensgrenzen**: Bricht Annahmen nachgelagerter Dienste über Token-Herkunft  
- **Laterale Bewegung**: Kompromittierte Tokens über mehrere Dienste ermöglichen breitere Angriffsflächen

**Implementierungskontrollen:**  
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
  
### **Sichere Token-Management-Muster**

**Best Practices:**
- **Kurzlebige Tokens**: Minimierung des Expositionsfensters durch häufige Token-Rotation  
- **Just-in-Time-Ausstellung**: Tokens nur bei Bedarf für spezifische Operationen ausstellen  
- **Sichere Speicherung**: Verwendung von Hardware-Sicherheitsmodulen (HSMs) oder sicheren Schlüsseltresoren  
- **Token-Bindung**: Tokens, wo möglich, an spezifische Clients, Sitzungen oder Operationen binden  
- **Überwachung & Alarmierung**: Echtzeit-Erkennung von Token-Missbrauch oder unautorisierten Zugriffsmustern

## 3. **Sitzungssicherheitskontrollen**

### **Verhinderung von Session Hijacking**

**Adressierte Angriffsvektoren:**
- **Session Hijack Prompt Injection**: Einschleusen bösartiger Ereignisse in geteilten Sitzungszustand  
- **Session-Impersonation**: Unautorisierte Nutzung gestohlener Sitzungs-IDs zur Umgehung der Authentifizierung  
- **Resumable Stream Angriffe**: Ausnutzung der Wiederaufnahme von servergesendeten Ereignissen zur Einschleusung bösartiger Inhalte

**Verpflichtende Sitzungskontrollen:**  
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
  
**Transportsicherheit:**  
- **HTTPS-Durchsetzung**: Alle Sitzungs-Kommunikation über TLS 1.3  
- **Sichere Cookie-Attribute**: HttpOnly, Secure, SameSite=Strict  
- **Zertifikat-Pinning**: Für kritische Verbindungen zur Verhinderung von MITM-Angriffen

### **Stateful vs Stateless Überlegungen**

**Für Stateful-Implementierungen:**  
- Gemeinsamer Sitzungszustand erfordert zusätzlichen Schutz gegen Injection-Angriffe  
- Warteschlangenbasierte Sitzungsverwaltung benötigt Integritätsprüfung  
- Mehrere Serverinstanzen erfordern sichere Synchronisation des Sitzungszustands

**Für Stateless-Implementierungen:**  
- JWT- oder ähnliches tokenbasiertes Sitzungsmanagement  
- Kryptografische Verifikation der Sitzungszustandsintegrität  
- Reduzierte Angriffsfläche, erfordert aber robuste Token-Validierung

## 4. **KI-spezifische Sicherheitskontrollen**

### **Prompt Injection Abwehr**

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
  
**Implementierungskontrollen:**  
- **Eingabesanierung**: Umfassende Validierung und Filterung aller Benutzereingaben  
- **Definition von Inhaltsgrenzen**: Klare Trennung zwischen Systemanweisungen und Benutzerinhalten  
- **Anweisungshierarchie**: Korrekte Prioritätsregeln bei widersprüchlichen Anweisungen  
- **Ausgabeüberwachung**: Erkennung potenziell schädlicher oder manipulierte Ausgaben

### **Verhinderung von Tool Poisoning**

**Tool-Sicherheitsrahmen:**  
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
  
**Dynamisches Tool-Management:**  
- **Genehmigungs-Workflows**: Explizite Benutzerzustimmung für Tool-Änderungen  
- **Rollback-Fähigkeiten**: Möglichkeit zur Rückkehr zu vorherigen Tool-Versionen  
- **Änderungsprotokollierung**: Vollständige Historie der Tool-Definition-Änderungen  
- **Risikobewertung**: Automatisierte Bewertung der Sicherheit des Tools

## 5. **Verhinderung von Confused Deputy Angriffen**

### **OAuth Proxy Sicherheit**

**Angriffsverhinderungskontrollen:**  
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
  
**Implementierungsanforderungen:**  
- **Benutzereinwilligungsprüfung**: Zustimmungsschirme bei dynamischer Client-Registrierung niemals überspringen  
- **Redirect-URI-Validierung**: Strikte Whitelist-basierte Validierung der Weiterleitungsziele  
- **Schutz des Autorisierungscodes**: Kurzlebige Codes mit Einmalverwendung  
- **Client-Identitätsprüfung**: Robuste Validierung von Client-Anmeldeinformationen und Metadaten

## 6. **Tool-Ausführungssicherheit**

### **Sandboxing & Isolation**

**Containerbasierte Isolation:**  
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
  
**Prozessisolation:**  
- **Getrennte Prozesskontexte**: Jede Tool-Ausführung in isoliertem Prozessraum  
- **Interprozesskommunikation**: Sichere IPC-Mechanismen mit Validierung  
- **Prozessüberwachung**: Laufzeitanalyse und Anomalieerkennung  
- **Ressourcenbegrenzung**: Harte Limits für CPU, Speicher und I/O-Operationen

### **Least Privilege Umsetzung**

**Berechtigungsmanagement:**  
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
  
## 7. **Lieferkettensicherheitskontrollen**

### **Abhängigkeitsprüfung**

**Umfassende Komponentensicherheit:**  
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
  
### **Kontinuierliche Überwachung**

**Erkennung von Lieferkettenbedrohungen:**  
- **Überwachung der Abhängigkeitsgesundheit**: Kontinuierliche Bewertung aller Abhängigkeiten auf Sicherheitsprobleme  
- **Integration von Bedrohungsinformationen**: Echtzeit-Updates zu neuen Lieferkettenbedrohungen  
- **Verhaltensanalyse**: Erkennung ungewöhnlichen Verhaltens in externen Komponenten  
- **Automatisierte Reaktion**: Sofortige Eindämmung kompromittierter Komponenten

## 8. **Überwachungs- & Erkennungskontrollen**

### **Security Information and Event Management (SIEM)**

**Umfassende Protokollierungsstrategie:**  
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
  
### **Echtzeit-Bedrohungserkennung**

**Verhaltensanalysen:**  
- **User Behavior Analytics (UBA)**: Erkennung ungewöhnlicher Benutzerzugriffsmuster  
- **Entity Behavior Analytics (EBA)**: Überwachung des Verhaltens von MCP-Servern und Tools  
- **Machine Learning Anomalieerkennung**: KI-gestützte Identifikation von Sicherheitsbedrohungen  
- **Bedrohungsinformationskorrelation**: Abgleich beobachteter Aktivitäten mit bekannten Angriffsmustern

## 9. **Vorfallreaktion & Wiederherstellung**

### **Automatisierte Reaktionsfähigkeiten**

**Sofortige Reaktionsmaßnahmen:**  
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
  
### **Forensische Fähigkeiten**

**Unterstützung bei Untersuchungen:**  
- **Erhalt des Audit-Trails**: Unveränderliche Protokollierung mit kryptografischer Integrität  
- **Beweissammlung**: Automatisierte Erfassung relevanter Sicherheitsartefakte  
- **Zeitlinienrekonstruktion**: Detaillierte Abfolge der Ereignisse vor Sicherheitsvorfällen  
- **Auswirkungsbewertung**: Bewertung des Kompromittierungsumfangs und der Datenexposition

## **Wichtige Sicherheitsarchitekturprinzipien**

### **Verteidigung in der Tiefe**  
- **Mehrere Sicherheitsebenen**: Kein einzelner Ausfallpunkt in der Sicherheitsarchitektur  
- **Redundante Kontrollen**: Überlappende Sicherheitsmaßnahmen für kritische Funktionen  
- **Fail-Safe-Mechanismen**: Sichere Voreinstellungen bei Systemfehlern oder Angriffen

### **Zero Trust Umsetzung**  
- **Nie vertrauen, immer verifizieren**: Kontinuierliche Validierung aller Entitäten und Anfragen  
- **Prinzip der minimalen Rechte**: Minimale Zugriffsrechte für alle Komponenten  
- **Mikrosegmentierung**: Granulare Netzwerk- und Zugriffskontrollen

### **Kontinuierliche Sicherheitsevolution**  
- **Anpassung an Bedrohungslandschaft**: Regelmäßige Updates zur Adressierung neuer Bedrohungen  
- **Wirksamkeit der Sicherheitskontrollen**: Laufende Bewertung und Verbesserung der Kontrollen  
- **Spezifikationskonformität**: Ausrichtung an sich entwickelnden MCP-Sicherheitsstandards

---

## **Implementierungsressourcen**

### **Offizielle MCP-Dokumentation**  
- [MCP-Spezifikation (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft-Sicherheitslösungen**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Sicherheitsstandards**  
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 für Large Language Models](https://genai.owasp.org/)  
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Wichtig**: Diese Sicherheitskontrollen spiegeln die aktuelle MCP-Spezifikation (2025-06-18) wider. Bitte prüfen Sie stets die neueste [offizielle Dokumentation](https://spec.modelcontextprotocol.io/), da sich die Standards schnell weiterentwickeln.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
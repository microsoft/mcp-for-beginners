# MCP Security Controls - Update ng Disyembre 2025

> **Kasalukuyang Pamantayan**: Ang dokumentong ito ay sumasalamin sa [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) mga kinakailangan sa seguridad at opisyal na [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Ang Model Context Protocol (MCP) ay malaki ang pag-unlad na may pinahusay na mga kontrol sa seguridad na tumutugon sa parehong tradisyunal na seguridad ng software at mga banta na partikular sa AI. Ang dokumentong ito ay nagbibigay ng komprehensibong mga kontrol sa seguridad para sa ligtas na mga implementasyon ng MCP mula Disyembre 2025.

## **MANDATORY na Mga Kinakailangan sa Seguridad**

### **Kritikal na Mga Ipinagbabawal mula sa MCP Specification:**

> **IPINAGBABAWAL**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang mga token na hindi tahasang inilabas para sa MCP server  
>
> **IPINAGBABAWAL**: Ang mga MCP server **HINDI DAPAT** gumamit ng mga session para sa pagpapatunay  
>
> **KINAKAILANGAN**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** beripikahin LAHAT ng mga papasok na kahilingan  
>
> **MANDATORY**: Ang mga MCP proxy server na gumagamit ng static client IDs **DAPAT** kumuha ng pahintulot ng user para sa bawat dynamic na nakarehistrong client

---

## 1. **Mga Kontrol sa Pagpapatunay at Awtorisasyon**

### **Integrasyon ng Panlabas na Tagapagbigay ng Pagkakakilanlan**

**Kasalukuyang Pamantayan ng MCP (2025-06-18)** ay nagpapahintulot sa mga MCP server na i-delegate ang pagpapatunay sa mga panlabas na tagapagbigay ng pagkakakilanlan, na kumakatawan sa isang mahalagang pagbuti sa seguridad:

### **Integrasyon ng Panlabas na Tagapagbigay ng Pagkakakilanlan**

**Kasalukuyang Pamantayan ng MCP (2025-11-25)** ay nagpapahintulot sa mga MCP server na i-delegate ang pagpapatunay sa mga panlabas na tagapagbigay ng pagkakakilanlan, na kumakatawan sa isang mahalagang pagbuti sa seguridad:

**Mga Benepisyo sa Seguridad:**
1. **Inaalis ang mga Panganib ng Custom Authentication**: Binabawasan ang surface ng kahinaan sa pamamagitan ng pag-iwas sa mga custom na implementasyon ng pagpapatunay  
2. **Seguridad na Pang-Enterprise**: Ginagamit ang mga kilalang tagapagbigay ng pagkakakilanlan tulad ng Microsoft Entra ID na may mga advanced na tampok sa seguridad  
3. **Sentralisadong Pamamahala ng Pagkakakilanlan**: Pinapasimple ang pamamahala ng lifecycle ng user, kontrol sa access, at pag-audit ng pagsunod  
4. **Multi-Factor Authentication**: Namamana ang mga kakayahan ng MFA mula sa mga enterprise identity provider  
5. **Mga Patakaran sa Kondisyunal na Access**: Nakikinabang mula sa mga risk-based access control at adaptive authentication

**Mga Kinakailangan sa Implementasyon:**
- **Pag-validate ng Token Audience**: Beripikahin na lahat ng token ay tahasang inilabas para sa MCP server  
- **Pag-verify ng Issuer**: Patunayan na ang issuer ng token ay tumutugma sa inaasahang tagapagbigay ng pagkakakilanlan  
- **Pag-verify ng Lagda**: Kryptograpikong beripikasyon ng integridad ng token  
- **Pagpapatupad ng Expiration**: Mahigpit na pagpapatupad ng mga limitasyon sa buhay ng token  
- **Pag-validate ng Saklaw**: Siguraduhing ang mga token ay naglalaman ng angkop na mga pahintulot para sa mga hinihiling na operasyon

### **Seguridad ng Lohika ng Awtorisasyon**

**Kritikal na Mga Kontrol:**
- **Komprehensibong Audit ng Awtorisasyon**: Regular na pagsusuri sa seguridad ng lahat ng punto ng desisyon sa awtorisasyon  
- **Fail-Safe Defaults**: Tanggihan ang access kapag ang lohika ng awtorisasyon ay hindi makagawa ng tiyak na desisyon  
- **Mga Hangganan ng Pahintulot**: Malinaw na paghihiwalay sa pagitan ng iba't ibang antas ng pribilehiyo at access sa mga resource  
- **Audit Logging**: Kumpletong pag-log ng lahat ng desisyon sa awtorisasyon para sa pagmamanman ng seguridad  
- **Regular na Pagsusuri ng Access**: Panahon-panahong beripikasyon ng mga pahintulot ng user at mga asignasyon ng pribilehiyo

## 2. **Seguridad ng Token at Mga Kontrol laban sa Passthrough**

### **Pag-iwas sa Token Passthrough**

**Ang token passthrough ay tahasang ipinagbabawal** sa MCP Authorization Specification dahil sa mga kritikal na panganib sa seguridad:

**Mga Panganib sa Seguridad na Tinugunan:**
- **Pag-iwas sa Kontrol**: Nilalampasan ang mahahalagang kontrol sa seguridad tulad ng rate limiting, pag-validate ng kahilingan, at pagmamanman ng trapiko  
- **Pagkawala ng Pananagutan**: Ginagawang imposible ang pagkilala sa client, na sumisira sa mga audit trail at pagsisiyasat ng insidente  
- **Proxy-Based Exfiltration**: Pinapayagan ang mga malisyosong aktor na gamitin ang mga server bilang proxy para sa hindi awtorisadong pag-access ng data  
- **Paglabag sa Trust Boundary**: Sinisira ang mga palagay ng downstream service tungkol sa pinagmulan ng token  
- **Lateral Movement**: Ang mga kompromisadong token sa maraming serbisyo ay nagpapahintulot ng mas malawak na paglawak ng pag-atake

**Mga Kontrol sa Implementasyon:**
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

### **Mga Pattern sa Secure Token Management**

**Mga Pinakamahusay na Praktis:**
- **Mga Token na Panandalian Lang**: Bawasan ang exposure window sa pamamagitan ng madalas na pag-ikot ng token  
- **Just-in-Time Issuance**: Mag-isyu ng mga token lamang kapag kailangan para sa mga partikular na operasyon  
- **Secure Storage**: Gumamit ng hardware security modules (HSMs) o secure key vaults  
- **Token Binding**: Itali ang mga token sa mga partikular na client, session, o operasyon kung maaari  
- **Monitoring at Alerting**: Real-time na pagtuklas ng maling paggamit ng token o mga pattern ng hindi awtorisadong access

## 3. **Mga Kontrol sa Seguridad ng Session**

### **Pag-iwas sa Session Hijacking**

**Mga Vector ng Atake na Tinugunan:**
- **Session Hijack Prompt Injection**: Malisyosong mga pangyayari na ini-inject sa shared session state  
- **Session Impersonation**: Hindi awtorisadong paggamit ng ninakaw na session ID upang lampasan ang pagpapatunay  
- **Resumable Stream Attacks**: Pagsasamantala sa server-sent event resumption para sa malisyosong pag-inject ng nilalaman

**Mandatory na Mga Kontrol sa Session:**
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

**Seguridad sa Transportasyon:**
- **HTTPS Enforcement**: Lahat ng komunikasyon ng session ay sa TLS 1.3  
- **Secure Cookie Attributes**: HttpOnly, Secure, SameSite=Strict  
- **Certificate Pinning**: Para sa mga kritikal na koneksyon upang maiwasan ang MITM attacks

### **Mga Pagsasaalang-alang sa Stateful vs Stateless**

**Para sa Stateful Implementations:**
- Ang shared session state ay nangangailangan ng karagdagang proteksyon laban sa injection attacks  
- Ang queue-based session management ay nangangailangan ng beripikasyon ng integridad  
- Ang maraming server instances ay nangangailangan ng secure na session state synchronization

**Para sa Stateless Implementations:**
- JWT o katulad na token-based session management  
- Kryptograpikong beripikasyon ng integridad ng session state  
- Nabawasang attack surface ngunit nangangailangan ng matibay na pag-validate ng token

## 4. **Mga Kontrol sa Seguridad na Partikular sa AI**

### **Depensa sa Prompt Injection**

**Integrasyon ng Microsoft Prompt Shields:**
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

**Mga Kontrol sa Implementasyon:**
- **Input Sanitization**: Komprehensibong pag-validate at pagsala ng lahat ng input ng user  
- **Paglilinaw ng Boundary ng Nilalaman**: Malinaw na paghihiwalay sa pagitan ng mga utos ng sistema at nilalaman ng user  
- **Hierarchy ng Instruksyon**: Tamang mga patakaran sa precedence para sa mga nagkakasalungat na utos  
- **Pagmamanman ng Output**: Pagtuklas ng posibleng mapanganib o manipuladong output

### **Pag-iwas sa Tool Poisoning**

**Framework ng Seguridad ng Tool:**
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

**Dynamic Tool Management:**
- **Approval Workflows**: Tahasang pahintulot ng user para sa mga pagbabago sa tool  
- **Rollback Capabilities**: Kakayahang bumalik sa mga naunang bersyon ng tool  
- **Change Auditing**: Kumpletong kasaysayan ng mga pagbabago sa depinisyon ng tool  
- **Risk Assessment**: Automated na pagsusuri ng security posture ng tool

## 5. **Pag-iwas sa Confused Deputy Attack**

### **Seguridad ng OAuth Proxy**

**Mga Kontrol sa Pag-iwas sa Atake:**
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

**Mga Kinakailangan sa Implementasyon:**
- **Pag-verify ng Pahintulot ng User**: Huwag kailanman laktawan ang mga consent screen para sa dynamic client registration  
- **Pag-validate ng Redirect URI**: Mahigpit na whitelist-based na pag-validate ng mga destinasyon ng redirect  
- **Proteksyon ng Authorization Code**: Mga panandaliang code na may single-use enforcement  
- **Pag-verify ng Identidad ng Client**: Matibay na pag-validate ng mga kredensyal at metadata ng client

## 6. **Seguridad sa Pagpapatakbo ng Tool**

### **Sandboxing at Isolation**

**Container-Based Isolation:**
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

**Process Isolation:**
- **Hiwalay na Process Contexts**: Bawat pagpapatakbo ng tool ay nasa hiwalay na process space  
- **Inter-Process Communication**: Secure na mga mekanismo ng IPC na may beripikasyon  
- **Process Monitoring**: Pagsusuri ng runtime behavior at pagtuklas ng anomalya  
- **Resource Enforcement**: Mahigpit na limitasyon sa CPU, memorya, at mga operasyon ng I/O

### **Implementasyon ng Least Privilege**

**Pamamahala ng Pahintulot:**
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

## 7. **Mga Kontrol sa Seguridad ng Supply Chain**

### **Pag-verify ng Dependency**

**Komprehensibong Seguridad ng Komponent:**
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

### **Patuloy na Pagmamanman**

**Pagtuklas ng Banta sa Supply Chain:**
- **Pagmamanman ng Kalusugan ng Dependency**: Patuloy na pagtatasa ng lahat ng dependency para sa mga isyu sa seguridad  
- **Integrasyon ng Threat Intelligence**: Real-time na mga update sa mga umuusbong na banta sa supply chain  
- **Pagsusuri ng Pag-uugali**: Pagtuklas ng hindi pangkaraniwang pag-uugali sa mga panlabas na komponent  
- **Automated na Tugon**: Agarang paglalaman ng mga kompromisadong komponent

## 8. **Mga Kontrol sa Pagmamanman at Pagtuklas**

### **Security Information and Event Management (SIEM)**

**Komprehensibong Estratehiya sa Pag-log:**
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

### **Real-Time na Pagtuklas ng Banta**

**Behavioral Analytics:**
- **User Behavior Analytics (UBA)**: Pagtuklas ng hindi pangkaraniwang pattern ng access ng user  
- **Entity Behavior Analytics (EBA)**: Pagmamanman ng MCP server at pag-uugali ng tool  
- **Machine Learning Anomaly Detection**: AI-powered na pagtukoy ng mga banta sa seguridad  
- **Threat Intelligence Correlation**: Pagtutugma ng mga naobserbahang aktibidad laban sa mga kilalang pattern ng pag-atake

## 9. **Pagtugon sa Insidente at Pagbawi**

### **Automated na Kakayahan sa Pagtugon**

**Agad na Mga Aksyon sa Pagtugon:**
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

### **Mga Kakayahan sa Forensic**

**Suporta sa Pagsisiyasat:**
- **Pagpapanatili ng Audit Trail**: Hindi mababago na pag-log na may kryptograpikong integridad  
- **Pagkolekta ng Ebidensya**: Automated na pagkuha ng mga kaugnay na artifact sa seguridad  
- **Pagbuo ng Timeline**: Detalyadong pagkakasunod-sunod ng mga pangyayari na humantong sa mga insidente sa seguridad  
- **Pagsusuri ng Epekto**: Pagtatasa ng lawak ng kompromiso at paglantad ng data

## **Pangunahing Prinsipyo ng Arkitektura sa Seguridad**

### **Defense in Depth**
- **Maramihang Layer ng Seguridad**: Walang iisang punto ng pagkabigo sa arkitektura ng seguridad  
- **Redundant na Mga Kontrol**: Nag-o-overlap na mga hakbang sa seguridad para sa mga kritikal na function  
- **Fail-Safe Mechanisms**: Ligtas na mga default kapag ang mga sistema ay nakakaranas ng mga error o pag-atake

### **Implementasyon ng Zero Trust**
- **Huwag Magsalig, Laging Mag-verify**: Patuloy na beripikasyon ng lahat ng entidad at kahilingan  
- **Prinsipyo ng Least Privilege**: Pinakamababang karapatan sa access para sa lahat ng komponent  
- **Micro-Segmentation**: Granular na kontrol sa network at access

### **Patuloy na Ebolusyon ng Seguridad**
- **Pag-angkop sa Landscape ng Banta**: Regular na mga update upang tugunan ang mga umuusbong na banta  
- **Epektibidad ng Kontrol sa Seguridad**: Patuloy na pagsusuri at pagpapabuti ng mga kontrol  
- **Pagsunod sa Specification**: Pagsunod sa umuusbong na mga pamantayan sa seguridad ng MCP

---

## **Mga Mapagkukunan sa Implementasyon**

### **Opisyal na Dokumentasyon ng MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Mga Solusyon sa Seguridad ng Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Mga Pamantayan sa Seguridad**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Mahalaga**: Ang mga kontrol sa seguridad na ito ay sumasalamin sa kasalukuyang MCP specification (2025-06-18). Palaging beripikahin laban sa pinakabagong [opisyal na dokumentasyon](https://spec.modelcontextprotocol.io/) dahil ang mga pamantayan ay patuloy na mabilis na umuunlad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
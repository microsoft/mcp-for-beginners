# MCP Security Controls - Update Setyembre 2026

> **Kasalukuyang pamantayan:** Ang dokumentong ito ay sumasalamin sa
> [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> at sa opisyal na
> [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Ang Model Context Protocol (MCP) ay lubos nang umunlad na may pinahusay na mga kontrol sa seguridad na tinatalakay ang parehong tradisyunal na seguridad sa software at mga partikular na banta sa AI. Ang dokumentong ito ay nagbibigay ng komprehensibong mga kontrol sa seguridad para sa ligtas na mga implementasyon ng MCP na naaayon sa OWASP MCP Top 10 na balangkas.

## 🏔️ Praktikal na Pagsasanay sa Seguridad

Para sa praktikal at hands-on na karanasan sa pagpapatupad ng seguridad, inirerekomenda namin ang **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - isang komprehensibong gabay na ekspedisyon sa pag-secure ng MCP servers sa Azure gamit ang metodolohiyang "vulnerable → exploit → fix → validate."

Lahat ng mga kontrol sa seguridad sa dokumentong ito ay nakaayon sa **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, na nagbibigay ng reference architectures at Azure-specific na mga patnubay sa pagpapatupad para sa mga panganib ng OWASP MCP Top 10.

## **MANDATORY Security Requirements**

### **Mahalagang Mga Ipinagbabawal Mula sa MCP Specification:**

> **IPINAGBABAWAL**: Ang mga MCP servers **HINDI DAPAT** tumanggap ng anumang mga token na hindi tahasang inilabas para sa MCP server
>
> **IPINAGBABAWAL**: Ang mga MCP servers **HINDI DAPAT** gumamit ng mga sesyon para sa pagpapatunay
>
> **KINAKAILANGAN**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** tiyakin ang LAHAT ng papasok na mga kahilingan
>
> **MANDATORY**: Ang mga MCP proxy server na gumagamit ng static na third-party client ID
> **DAPAT** kumuha ng pahintulot para sa bawat MCP client bago ipasa ang awtorisasyon

---

## 1. **Mga Kontrol sa Authentication at Authorization**

### **Integrasyon ng External Identity Provider**

**MCP Specification `2026-07-28`** ay nagpapahintulot sa mga MCP server na idelegate ang
authentication sa mga external identity provider. Ang awtorisasyon para sa HTTP
transports ay sinusuri sa bawat kahilingan; ang mga lokal na stdio server ay kumukuha ng kredensyal
mula sa kanilang kapaligiran imbes.

**Natugunang Panganib sa OWASP MCP**: [MCP07 - Insufficient Authentication & Authorization](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Mga Benepisyo sa Seguridad:**
1. **Pinapawi ang mga Panganib sa Custom Authentication**: Pinapaliit ang exposure sa kahinaan sa pamamagitan ng pag-iwas sa mga custom na implementasyon ng authentication
2. **Seguridad na Pang-Enterprise Grade**: Gumagamit ng mga napatunayang identity provider tulad ng Microsoft Entra ID na may mga advanced na tampok sa seguridad
3. **Sentralisadong Pamamahala ng Identidad**: Pinapasimple ang lifecycle ng user management, kontrol sa access, at pagsunod sa pag-audit
4. **Multi-Factor Authentication**: Namamana ang MFA capabilities mula sa enterprise identity providers
5. **Conditional Access Policies**: Nakikinabang mula sa risk-based access controls at adaptive authentication

**Mga Kinakailangan sa Pagpapatupad:**
- **Pagpaparehistro ng Kliyente**: Mas gusto ang Client ID Metadata Documents o
  pre-registration; gamitin lamang ang deprecated Dynamic Client Registration para sa
  compatibility
- **Pagpapatunay ng Token Audience**: Tiyakin na ang lahat ng token ay tahasang inilabas para sa MCP server
- **Pagpapatunay ng Issuer**: Siguraduhing tumutugma ang token issuer sa inaasahang identity provider
- **Pagpapatunay ng Lagda**: Kryptograpikong pagpapatunay ng integridad ng token
- **Pagsunod sa Expiration**: Mahigpit na pagpapatupad ng mga limitasyon sa buhay ng token
- **Pagpapatunay ng Saklaw**: Tiyakin na ang mga token ay naglalaman ng angkop na pahintulot para sa mga hiniling na operasyon

### **Seguridad ng Loob ng Authorization Logic**

**Mahalagang Kontrol:**
- **Komprehensibong Authorization Audits**: Regular na pagsusuri sa seguridad ng lahat ng authorization decision points
- **Fail-Safe Defaults**: Igalang ang pagtanggi ng access kapag hindi makagawa ng tiyak na desisyon ang authorization logic
- **Mga Hangganan ng Pahintulot**: Malinaw na paghihiwalay sa pagitan ng iba't ibang antas ng pribilehiyo at access sa resources
- **Audit Logging**: Kumpletong pag-log ng lahat ng desisyon sa authorization para sa monitoring ng seguridad
- **Regular na Pagsusuri ng Access**: Panahong beripikasyon sa mga user permission at pribilehiyo

## 2. **Token Security at Mga Kontrol laban sa Passthrough**

**Natugunang Panganib sa OWASP MCP**: [MCP01 - Token Mismanagement & Secret Exposure](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Pag-iwas sa Token Passthrough**

**Mahigpit na ipinagbabawal ang token passthrough** sa MCP Authorization Specification dahil sa mga kritikal na panganib sa seguridad:

**Mga Panganib na Nilalayon:**
- **Pag-iwas sa Control**: Nagbypass ng mahahalagang kontrol sa seguridad gaya ng rate limiting, request validation, at traffic monitoring
- **Pagkawala ng Pananagutan**: Nagpapahirap matukoy ang client identity, sumisira sa mga audit trail at pagsisiyasat ng insidente
- **Proxy-Based Exfiltration**: Pinapayagan ang mga malisyosong aktor na gamitin ang mga server bilang proxy para sa hindi awtorisadong pag-access sa datos
- **Paglabag sa Trust Boundary**: Nilalabag ang mga inaasahan ng downstream services ukol sa pinagmulan ng token
- **Lateral Movement**: Ang mga compromised na token sa maraming serbisyo ay nagpapalawak ng saklaw ng atake

**Mga Kontrol sa Pagpapatupad:**
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

### **Mga Pattern ng Ligtas na Pamamahala ng Token**

**Mga Pinakamahusay na Gawi:**
- **Mga Token na Panandalian Lang**: Bawasan ang exposure window sa madalas na pag-ikot ng token
- **Just-in-Time na Pagbibigay**: Magbigay ng mga token lamang kapag kinakailangan para sa partikular na operasyon
- **Ligtas na Imbakan**: Gamitin ang hardware security modules (HSMs) o secure key vaults
- **Token Binding**: Patunayan ang audience at issuer ng token para sa itinakdang MCP
  resource, client, at operasyon
- **Pagmamanman at Pag-alerto**: Real-time na pagtukoy ng maling paggamit ng token o di-awtorisadong mga pattern ng pag-access

## 3. **Mga Kontrol sa Seguridad ng Estado ng Aplikasyon**

### **Pag-iwas sa Hijacking ng State Handle**

**Mga Vector ng Atake na Nilalayon:**
- **Pagtatantiya ng Handle**: Ang makikilalang mga identifier ay nagbubukas sa estado ng ibang tumatawag
- **Cross-user Reuse**: Ang nanakaw na handle ay ginagamit sa ibang identidad
- **Implicit Authorization**: Ang pagkapossesso ng isang handle ay maling tinitingnan bilang
  patunay ng access

**Mga Kontrol sa State Handle:**

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

**Seguridad sa Transportasyon:**
- **HTTPS Enforcement**: Kailangan ang HTTPS para sa remote HTTP transports
- **Paghawak ng Kredensyal**: Ipadala at patunayan ang awtorisasyon sa bawat HTTP request
- **Pag-iisa ng stdio**: Protektahan ang lokal na stdio server sa pamamagitan ng isolation sa proseso at
  mga kontrol sa kredensyal ng kapaligiran

### **Mga Pagsasaalang-alang sa Stateful vs Stateless**

Ang MCP `2026-07-28` ay stateless sa protocol layer. Ang mga aplikasyon ay maaari pa ring
magpanatili ng estado sa pamamagitan ng pagbabalik ng tahasang handle mula sa isang tool call at pagtanggap
nito bilang ordinaryong argumento sa mga susunod na tawag.

- Mag-imbak ng estado nang hiwalay sa anumang transport connection.
- Itali ang mga state handle sa authenticated na principal server-side.
- Ituring ang handle bilang pangalan, hindi bilang isang bearer credential.
- Tukuyin ang expiration at recovery behavior para sa mga stale na handle.

## 4. **Mga Partikular na Kontrol sa Seguridad ng AI**

**Natugunang mga Panganib sa OWASP MCP**:
- [MCP06 - Intent Flow Subversion](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Tool Poisoning](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Command Injection & Execution](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Depensa laban sa Prompt Injection**

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

**Mga Kontrol sa Pagpapatupad:**
- **Input Sanitization**: Komprehensibong pagpapatunay at pagsala sa lahat ng input ng user
- **Paglalarawan ng Content Boundary**: Malinaw na paghihiwalay sa mga utos ng sistema at nilalaman ng user
- **Instruction Hierarchy**: Tamang mga patakaran ng precedence para sa mga magkasalungat na utos
- **Pagmamanman ng Output**: Pagtukoy ng mga posibleng mapanganib o manipuladong output

### **Pag-iwas sa Tool Poisoning**

**Balangkas ng Seguridad ng Tool:**
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

**Dynamic na Pamamahala ng Tool:**
- **Workflow ng Pag-apruba**: Tahasang pahintulot ng user para sa mga pagbabago sa tool
- **Kakayahang Mag-rollback**: Kakayahang bumalik sa mga naunang bersyon ng tool
- **Audit ng mga Pagbabago**: Kumpletong kasaysayan ng mga pagbabagong ginawa sa depinisyon ng tool
- **Pagtatasa sa Panganib**: Automated na ebalwasyon ng postura sa seguridad ng tool

## 5. **Pag-iwas sa Confused Deputy Attack**

### **Seguridad ng OAuth Proxy**

**Mga Kontrol para sa Pag-iwas ng Atake:**
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

**Mga Kinakailangan sa Pagpapatupad:**
- **Pagpaparehistro ng Kliyente**: Mas gusto ang pre-registration o Client ID Metadata
  Documents; ituring ang Dynamic Client Registration bilang fallback sa compatibility
- **Pagpapatunay ng Pahintulot ng User**: Ang mga MCP proxy na gumagamit ng static na third-party client
  ID ay dapat kumuha ng pahintulot ng bawat client bago ipasa ang awtorisasyon
- **Pagpapatunay ng Redirect URI**: Mahigpit na whitelist-based na pagsusuri ng mga destinasyon ng redirect
- **Proteksyon ng Authorization Code**: Mga maikling-buhay na code na may pagpapatupad ng single-use
- **Pagpapatunay ng Identity ng Client**: Matibay na pagpapatunay sa mga kredensyal at metadata ng client

## 6. **Seguridad ng Pagsasagawa ng Tool**

### **Sandboxing at Isolation**

**Isolasyong Batay sa Container:**
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

**Isolation ng Proseso:**
- **Hiwalay na Mga Context ng Proseso**: Bawat pagpapatupad ng tool ay nasa hiwalay na espasyo ng proseso
- **Inter-Process Communication**: Ligtas na mga mekanismo ng IPC na may pagpapatunay
- **Pagmamanman ng Proseso**: Pagsusuri ng pag-uugali sa runtime at pagtukoy ng anomalya
- **Pagpapatupad ng Resource**: Mahigpit na mga limitasyon sa CPU, memorya, at mga operasyon sa I/O

### **Pagpapatupad ng Least Privilege**

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

**Natugunang Panganib sa OWASP MCP**: [MCP04 - Software Supply Chain Attacks & Dependency Tampering](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Pagpapatunay ng Dependency**

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

### **Tuloy-tuloy na Pagmamanman**

**Pagtuklas ng Banta sa Supply Chain:**
- **Pagmamanman sa Kalusugan ng Dependency**: Patuloy na pagtatasa ng lahat ng dependencies para sa mga isyu sa seguridad
- **Integrasyon ng Threat Intelligence**: Real-time na pag-update tungkol sa mga bagong banta sa supply chain
- **Pagsusuri ng Pag-uugali**: Pagtukoy ng hindi pangkaraniwang pag-uugali sa mga panlabas na componente
- **Automated na Tugon**: Agarang pagkontrol ng mga compromised na componente

## 8. **Mga Kontrol sa Pagmamanman at Pagtuklas**

**Natugunang Panganib sa OWASP MCP**: [MCP08 - Lack of Audit and Telemetry](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Seguridad ng Impormasyon at Pamamahala ng Kaganapan (SIEM)**

**Komprehensibong Estratehiya sa Pag-logging:**
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

**Analytics ng Pag-uugali:**
- **User Behavior Analytics (UBA)**: Pagtukoy ng hindi pangkaraniwang pattern ng pag-access ng user
- **Entity Behavior Analytics (EBA)**: Pagmamanman ng pag-uugali ng MCP server at tool
- **Machine Learning Anomaly Detection**: AI-driven na pagkilala ng mga banta sa seguridad
- **Pagsasama ng Threat Intelligence**: Pagtutugma ng mga naobserbahang gawain sa mga kilalang pattern ng pag-atake

## 9. **Pagtugon sa Insidente at Pag-recover**

### **Awtomatikong Kakayahan sa Pagtugon**

**Aksyon sa Agarang Pagtugon:**
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

### **Kakayahan sa Forensic**

**Suporta sa Imbestigasyon:**
- **Pagpapanatili ng Audit Trail**: Hindi mababago na pag-log na may integridad sa cryptographic
- **Pagkolekta ng Ebidensya**: Awtomatikong pagkuha ng mga kaugnay na artifact sa seguridad
- **Pag-uli ng Timeline**: Detalyadong sunud-sunod ng mga pangyayari patungo sa mga insidente ng seguridad
- **Pagsusuri ng Impact**: Pagtatasa sa lawak ng kompromiso at pagkalantad ng datos

## **Pangunahing Mga Prinsipyo ng Arkitektura sa Seguridad**

### **Defense in Depth**
- **Maramihang Patong ng Seguridad**: Walang iisang punto ng pagkabigo sa arkitekturang pangseguridad
- **Redundant na mga Kontrol**: Overlapping na mga hakbang sa seguridad para sa mga kritikal na gawain
- **Fail-Safe Mekanismo**: Ligtas na mga default kapag nakakaranas ng mga error o atake ang mga sistema

### **Pagpapatupad ng Zero Trust**
- **Huwag Magsalalay, Laging Beripikahin**: Patuloy na pagpapatunay ng lahat ng entidad at mga kahilingan
- **Prinsipyo ng Pinakamababang Pribilehiyo**: Minimal na karapatan sa access para sa lahat ng mga komponent
- **Micro-Segmentation**: Granular na kontrol sa network at access

### **Tuloy-tuloy na Pag-evolve ng Seguridad**
- **Pag-angkop sa Tanawin ng Banta**: Regular na pag-update upang tugunan ang mga lumalabas na banta
- **Epektibidad ng Kontrol sa Seguridad**: Patuloy na pagsusuri at pagpapabuti ng mga kontrol
- **Pagsunod sa Specification**: Pagsunod sa mga umuusbong na pamantayan ng MCP seguridad

---

## **Mga Mapagkukunan para sa Pagpapatupad**

### **Opisyal na Dokumentasyon ng MCP**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Mga Mapagkukunan sa Seguridad ng OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Komprehensibong OWASP MCP Top 10 na may implementasyon sa Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Opisyal na mga panganib sa seguridad ng OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on na pagsasanay sa seguridad para sa MCP sa Azure

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

> **Mahalaga:** Ang mga kontrol sa seguridad na ito ay sumasalamin sa MCP Specification
> `2026-07-28`. Palaging i-verify laban sa
> [kasalukuyang opisyal na dokumentasyon](https://modelcontextprotocol.io/specification/2026-07-28/)
> habang patuloy na umuunlad ang mga pamantayan.

## Ano ang Susunod

- Bumalik sa: [Security Module Overview](./README.md)
- Magpatuloy sa: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
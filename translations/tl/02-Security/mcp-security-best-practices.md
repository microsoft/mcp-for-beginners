# MCP Security Best Practices - Setyembre 2026 Update

> **Mahalaga:** Ang dokumentong ito ay sumasalamin sa
> [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> at ang opisyal na
> [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Hands-On Security Training

Para sa praktikal na karanasan sa pagpapatupad, inirerekomenda namin ang **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - isang komprehensibong gabay na ekspedisyon para sa pag-secure ng MCP servers sa Azure. Saklaw ng workshop ang lahat ng OWASP MCP Top 10 risks sa pamamagitan ng metodolohiyang "vulnerable → exploit → fix → validate".

Ang lahat ng mga praktis sa dokumentong ito ay kaayon ng **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** para sa mga gabay na espesipiko sa pagpapatupad sa Azure.

## Mahahalagang Praktis sa Seguridad para sa Mga Implementasyon ng MCP

Ang Model Context Protocol ay nagpapakilala ng natatanging mga hamon sa seguridad na lumalampas
sa tradisyunal na seguridad ng software. Ang mga praktis na ito ay tumutugon sa mga pundamental na
pangangailangan at mga banta na espesipiko sa MCP kabilang ang prompt injection, tool
poisoning, state-handle hijacking, confused deputy problems, at mga kahinaan sa token
passthrough.

### **MANDATORY Security Requirements** 

**Kritikal na mga Kinakailangan mula sa MCP Specification:**

> **HINDI DAPAT**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang token na hindi malinaw na inisyu para sa MCP server
> 
> **DAPAT**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** i-verify ANG LAHAT ng mga papasok na kahilingan
>  
> **HINDI DAPAT**: Ang mga MCP server **HINDI DAPAT** gumamit ng mga session para sa pagpapatunay
>
> **DAPAT**: Ang mga MCP proxy server na gumagamit ng static third-party client ID **DAPAT**
> humingi ng pahintulot para sa bawat MCP client bago ipasa ang awtorisasyon

---

## 1. **Token Security & Authentication**

**Mga Kontrol sa Authentication at Authorization:**
   - **Masusing Pagsusuri ng Authorization**: Isagawa ang komprehensibong audit ng MCP server authorization logic upang matiyak na ang tanging mga nilalayong user at client lamang ang makakakuha ng access sa mga resources
   - **Integrasyon ng External Identity Provider**: Gumamit ng mga kilalang identity provider tulad ng Microsoft Entra ID sa halip na gumawa ng sariling authentication
   - **Token Audience Validation**: Palaging i-validate na ang mga token ay malinaw na inisyu para sa iyong MCP server - huwag tanggapin ang mga token mula sa pataas na daloy
   - **Tamang Token Lifecycle**: Magpatupad ng secure na token rotation, mga patakaran sa expiration, at pigilan ang token replay attacks

**Protektadong Imbakan ng Token:**
   - Gumamit ng Azure Key Vault o katulad na secure credential stores para sa lahat ng mga secret
   - Magpatupad ng encryption para sa mga token habang nakaimbak at habang nasa transmisyon
   - Regular na pag-ikot ng credential at pagmamanman para sa hindi awtorisadong access

## 2. **State Handle & Transport Security**

**Mga Praktis sa Secure Application State:**

- **Opaque State Handles**: Gumamit ng secure, non-deterministic handles para sa
   application state na sumasaklaw sa mga kahilingan
- **User-Specific Binding**: Itali ang mga handle sa server-side sa authenticated
   principal at tanggihan ang paggamit muli sa pagitan ng mga user
- **Lifecycle Management**: I-expire at i-revoke ang mga handle upang limitahan ang bintana ng kahinaan
   windows
- **Per-request Authorization**: Huwag ituring ang state handle bilang authentication;
   i-authorize ang bawat kahilingan na nagpapakita nito

**Transport Layer Security:**

- Kinakailangan ang HTTPS para sa remote HTTP transports sa production
- Gumamit ng process isolation at mga environment credential para sa local stdio servers
- I-configure ang modernong TLS na may tamang certificate rotation at validation

## 3. **Proteksyon Laban sa Mga Espesipikong Banta ng AI** 🤖

**Depensa laban sa Prompt Injection:**
   - **Microsoft Prompt Shields**: Mag-deploy ng AI Prompt Shields para sa advanced na pagtuklas at pagsala ng mga malisyosong instruksyon
   - **Input Sanitization**: I-validate at i-sanitize ang lahat ng input upang maiwasan ang injection attacks at confused deputy problems
   - **Mga Hangganan sa Nilalaman**: Gumamit ng delimiter at datamarking system upang pag-iba'in ang pinagkakatiwalaang instruksyon at panlabas na nilalaman

**Pag-iwas sa Tool Poisoning:**
   - **Validation ng Tool Metadata**: Magpatupad ng mga integrity check para sa mga depinisyon ng tool at mag-monitor para sa di-inaasahang pagbabago
   - **Dynamic Tool Monitoring**: Subaybayan ang runtime behavior at gumawa ng alert system para sa di-inaasahang mga pattern ng pagpapatupad
   - **Approval Workflows**: Kailangan ng malinaw na pahintulot mula sa user para sa mga pagbabago sa tool at kakayahan

## 4. **Kontrol sa Access at mga Pahintulot**

**Prinsipyo ng Pinakamababang Pribilehiyo:**
   - Bigyan ang mga MCP server ng pinakamababang pahintulot na kinakailangan para sa nilalayong functionality
   - Magpatupad ng role-based access control (RBAC) na may maliliit na detalye ng pahintulot
   - Regular na pagsusuri ng pahintulot at tuluy-tuloy na pagmamanman sa pribilehiyo na pag-akyat

**Mga Kontrol sa Pahintulot sa Runtime:**
   - Maglagay ng mga limitasyon sa resource upang maiwasan ang mga resource exhaustion attacks
   - Gumamit ng container isolation para sa mga tool execution environment  
   - Magpatupad ng just-in-time access para sa mga administratibong gawain

## 5. **Kaligtasan ng Nilalaman at Pagmamanman**

**Pagpapatupad ng Kaligtasan ng Nilalaman:**
   - **Integrasyon ng Azure Content Safety**: Gumamit ng Azure Content Safety upang tuklasin ang nakapipinsalang nilalaman, mga pagtatangka ng jailbreak, at paglabag sa patakaran
   - **Behavioral Analysis**: Magpatupad ng runtime behavioral monitoring para matuklasan ang mga anomalya sa pagpapatakbo ng MCP server at tool
   - **Komprehensibong Pag-log**: I-log ang lahat ng pagtatangka sa authentication, pagtawag ng tool, at mga pangyayaring seguridad na may secure at tamper-proof na imbakan

**Tuloy-tuloy na Pagmamanman:**
   - Real-time alerting para sa mga kahina-hinalang pattern at mga pagtatangkang hindi awtorisadong access  
   - Integrasyon sa SIEM systems para sa sentralisadong pamamahala ng mga security event
   - Regular na mga audit sa seguridad at penetration testing ng mga implementasyon ng MCP

## 6. **Seguridad ng Supply Chain**

**Pag-verify ng Komponent:**
   - **Dependency Scanning**: Gumamit ng automated vulnerability scanning para sa lahat ng software dependencies at AI components
   - **Provenance Validation**: Patunayan ang pinagmulan, lisensya, at integridad ng mga modelo, pinagmulan ng datos, at mga panlabas na serbisyo
   - **Signed Packages**: Gumamit ng cryptographically signed packages at i-verify ang mga pirma bago i-deploy

**Secure Development Pipeline:**
   - **GitHub Advanced Security**: Magpatupad ng secret scanning, dependency analysis, at CodeQL static analysis
   - **CI/CD Security**: Isama ang security validation sa buong automated deployment pipelines
   - **Artifact Integrity**: Magpatupad ng cryptographic verification para sa mga deployed artifacts at configuration

## 7. **OAuth Security at Pag-iwas sa Confused Deputy**

**OAuth 2.1 Implementation:**
   - **PKCE Implementation**: Gumamit ng Proof Key for Code Exchange (PKCE) para sa lahat ng authorization requests
    - **Client Registration**: Mas gusto ang Client ID Metadata Documents o
       pre-registration; gamitin lang ang deprecated Dynamic Client Registration bilang
       compatibility fallback
    - **Explicit Consent**: Ang mga MCP proxy na gumagamit ng static third-party client ID ay dapat
       humingi ng pahintulot para sa bawat MCP client bago ipasa ang awtorisasyon
   - **Redirect URI Validation**: Magpatupad ng mahigpit na validation ng mga redirect URI at client identifiers

**Proxy Security:**
   - Pigilan ang pag-bypass ng awtorisasyon sa pamamagitan ng static client ID exploitation
   - Magpatupad ng wastong consent workflows para sa third-party API access
   - Mag-monitor para sa pagnanakaw ng authorization code at hindi awtorisadong API access

## 8. **Pagsagot sa Insidente at Pagbawi**

**Mabilis na Kakayahan sa Pagsagot:**
   - **Automated Response**: Magpatupad ng automated systems para sa pag-ikot ng credential at containment ng banta
   - **Rollback Procedures**: Kakayahang mabilis na bumalik sa mga kilalang tamang configuration at components
   - **Forensic Capabilities**: Detalyadong audit trails at pag-log para sa pagsisiyasat ng insidente

**Komunikasyon at Koordinasyon:**
   - Malinaw na mga proseso ng eskalasyon para sa mga insidente sa seguridad
   - Integrasyon sa mga pangkat ng tugon sa insidente ng organisasyon
   - Regular na mga simulation ng security incident at tabletop na mga pagsasanay

## 9. **Pagsunod at Pamamahala**

**Regulatory Compliance:**
   - Tiyakin na ang mga implementasyon ng MCP ay sumusunod sa mga industry-specific requirements (GDPR, HIPAA, SOC 2)
   - Magpatupad ng data classification at privacy controls para sa AI data processing
   - Panatilihin ang komprehensibong dokumentasyon para sa auditing ng pagsunod

**Change Management:**
   - Pormal na proseso ng pagsusuri sa seguridad para sa lahat ng pagbabago sa sistema ng MCP
   - Version control at approval workflows para sa mga pagbabago sa configuration
   - Regular na pagsusuri sa pagsunod at gap analysis

## 10. **Advanced Security Controls**

**Zero Trust Architecture:**
   - **Huwag Magsalig, Laging I-Verify**: Tuloy-tuloy na pag-verify ng mga user, device, at koneksyon
   - **Micro-segmentation**: Granular na kontrol sa network na naghihiwalay sa bawat bahagi ng MCP
   - **Conditional Access**: Mga kontrol sa access base sa panganib na umaangkop sa kasalukuyang konteksto at pag-uugali

**Runtime Application Protection:**
   - **Runtime Application Self-Protection (RASP)**: Mag-deploy ng mga teknik ng RASP para sa real-time na pagtuklas ng banta
   - **Application Performance Monitoring**: Subaybayan ang mga anomalya sa performance na maaaring magpahiwatig ng pag-atake
   - **Dynamic Security Policies**: Magpatupad ng mga patakaran sa seguridad na umaangkop batay sa kasalukuyang tanawin ng banta

## 11. **Integrasyon sa Microsoft Security Ecosystem**

**Komprehensibong Microsoft Security:**
   - **Microsoft Defender for Cloud**: Pamamahala sa security posture ng cloud para sa mga MCP workload
   - **Azure Sentinel**: Cloud-native SIEM at SOAR na kakayahan para sa advanced na pagtuklas ng banta
   - **Microsoft Purview**: Pamamahala ng datos at pagsunod para sa AI workflows at pinagmulan ng datos

**Pamamahala ng Identity at Access:**
   - **Microsoft Entra ID**: Pamamahala ng enterprise identity na may mga patakaran sa conditional access
   - **Privileged Identity Management (PIM)**: Just-in-time access at approval workflows para sa mga administratibong gawain
   - **Identity Protection**: Risk-based conditional access at automated na pagsagot sa banta

## 12. **Tuloy-tuloy na Ebolusyon ng Seguridad**

**Panatilihing Napapanahon:**
   - **Specification Monitoring**: Regular na pagsuri ng mga update sa MCP specification at mga pagbabago sa security guidance
   - **Threat Intelligence**: Integrasyon ng mga AI-specific threat feeds at indicator ng kompromiso
   - **Pagsali sa Komunidad ng Seguridad**: Aktibong partisipasyon sa MCP security community at mga programa ng paglalantad ng kahinaan

**Adaptive Security:**
   - **Machine Learning Security**: Gumamit ng ML-based anomaly detection para matukoy ang mga bagong pattern ng pag-atake
   - **Predictive Security Analytics**: Magpatupad ng mga predictive model para sa proaktibong pagtukoy ng banta
   - **Security Automation**: Automated na update ng mga security policy base sa threat intelligence at mga pagbabago sa specification

---

## **Mahahalagang Mapagkukunan sa Seguridad**

### **Opisyal na Dokumentasyon ng MCP**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Mga Mapagkukunan ng Seguridad ng OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Komprehensibong OWASP MCP Top 10 na may implementasyon sa Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Opisyal na mga panganib sa seguridad ng OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on na pagsasanay sa seguridad para sa MCP sa Azure

### **Mga Solusyon sa Seguridad ng Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Mga Pamantayan sa Seguridad**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Mga Gabay sa Implementasyon**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Paalala sa Seguridad:** Ang mga praktis sa seguridad ng MCP ay mabilis na umuunlad. Palaging siguraduhin
> laban sa kasalukuyang [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/)
> at [opisyal na dokumentasyon sa seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> bago ang pagpapatupad.

## Ano Ang Susunod

- Basahin: [MCP Security Controls](./mcp-security-controls.md)
- Bumalik sa: [Security Module Overview](./README.md)
- Magpatuloy sa: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Security Best Practices - Update Disyembre 2025

> **Mahalaga**: Ang dokumentong ito ay sumasalamin sa pinakabagong [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) na mga kinakailangan sa seguridad at opisyal na [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Palaging sumangguni sa kasalukuyang espesipikasyon para sa pinaka-napapanahong gabay.

## Mahahalagang Praktis sa Seguridad para sa mga Implementasyon ng MCP

Ang Model Context Protocol ay nagtatakda ng mga natatanging hamon sa seguridad na lampas sa tradisyunal na seguridad ng software. Ang mga praktis na ito ay tumutugon sa parehong pundamental na mga kinakailangan sa seguridad at mga partikular na banta sa MCP kabilang ang prompt injection, tool poisoning, session hijacking, confused deputy problems, at token passthrough vulnerabilities.

### **MANDATORY Security Requirements** 

**Mahalagang Kinakailangan mula sa MCP Specification:**

### **MANDATORY Security Requirements** 

**Mahalagang Kinakailangan mula sa MCP Specification:**

> **HINDI DAPAT**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang token na hindi tahasang inilabas para sa MCP server  
>  
> **DAPAT**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** suriin ang LAHAT ng mga papasok na kahilingan  
>  
> **HINDI DAPAT**: Ang mga MCP server **HINDI DAPAT** gumamit ng mga session para sa pagpapatunay  
>  
> **DAPAT**: Ang mga MCP proxy server na gumagamit ng static client IDs **DAPAT** kumuha ng pahintulot ng gumagamit para sa bawat dinamiko na nakarehistrong kliyente

---

## 1. **Seguridad ng Token at Pagpapatunay**

**Mga Kontrol sa Pagpapatunay at Awtorisasyon:**
   - **Masusing Pagsusuri ng Awtorisasyon**: Magsagawa ng komprehensibong audit sa lohika ng awtorisasyon ng MCP server upang matiyak na tanging mga inaasahang gumagamit at kliyente lamang ang makaka-access sa mga mapagkukunan  
   - **Integrasyon ng Panlabas na Tagapagbigay ng Identidad**: Gumamit ng mga kilalang tagapagbigay ng identidad tulad ng Microsoft Entra ID sa halip na gumawa ng sariling pagpapatunay  
   - **Pagpapatunay ng Audience ng Token**: Palaging tiyakin na ang mga token ay tahasang inilabas para sa iyong MCP server - huwag kailanman tanggapin ang mga token mula sa itaas na antas  
   - **Tamang Siklo ng Buhay ng Token**: Magpatupad ng ligtas na pag-ikot ng token, mga patakaran sa pag-expire, at pigilan ang mga pag-atake ng token replay

**Protektadong Imbakan ng Token:**
   - Gumamit ng Azure Key Vault o katulad na ligtas na imbakan ng mga kredensyal para sa lahat ng lihim  
   - Magpatupad ng encryption para sa mga token habang nakaimbak at habang ipinapadala  
   - Regular na pag-ikot ng kredensyal at pagmamanman para sa hindi awtorisadong pag-access

## 2. **Pamamahala ng Session at Seguridad sa Transportasyon**

**Ligtas na Praktis sa Session:**
   - **Cryptographically Secure Session IDs**: Gumamit ng ligtas, hindi deterministic na mga session ID na nilikha gamit ang secure random number generators  
   - **Pag-uugnay sa Partikular na Gumagamit**: Iugnay ang mga session ID sa mga pagkakakilanlan ng gumagamit gamit ang mga format tulad ng `<user_id>:<session_id>` upang maiwasan ang maling paggamit ng session sa pagitan ng mga gumagamit  
   - **Pamamahala ng Siklo ng Buhay ng Session**: Magpatupad ng tamang pag-expire, pag-ikot, at pag-invalid upang limitahan ang mga bintana ng kahinaan  
   - **Pagsunod sa HTTPS/TLS**: Sapilitang HTTPS para sa lahat ng komunikasyon upang maiwasan ang interception ng session ID

**Seguridad ng Transport Layer:**
   - I-configure ang TLS 1.3 kung maaari kasama ang tamang pamamahala ng sertipiko  
   - Magpatupad ng certificate pinning para sa mga kritikal na koneksyon  
   - Regular na pag-ikot ng sertipiko at beripikasyon ng bisa

## 3. **Proteksyon sa Mga Partikular na Banta ng AI** 🤖

**Depensa sa Prompt Injection:**
   - **Microsoft Prompt Shields**: Mag-deploy ng AI Prompt Shields para sa advanced na pagtuklas at pagsala ng mga malisyosong utos  
   - **Sanitasyon ng Input**: Suriin at linisin ang lahat ng input upang maiwasan ang injection attacks at confused deputy problems  
   - **Mga Hangganan ng Nilalaman**: Gumamit ng mga delimiter at datamarking system upang makilala ang pinagkakatiwalaang mga utos mula sa panlabas na nilalaman

**Pag-iwas sa Tool Poisoning:**
   - **Pagpapatunay ng Metadata ng Tool**: Magpatupad ng mga integrity check para sa mga depinisyon ng tool at subaybayan ang mga hindi inaasahang pagbabago  
   - **Dynamic Tool Monitoring**: Subaybayan ang runtime behavior at mag-set up ng alerto para sa mga hindi inaasahang pattern ng pagpapatupad  
   - **Mga Workflow ng Pag-apruba**: Kailangan ang tahasang pahintulot ng gumagamit para sa mga pagbabago sa tool at mga kakayahan

## 4. **Kontrol sa Access at Mga Pahintulot**

**Prinsipyo ng Pinakamababang Pribilehiyo:**
   - Bigyan ang mga MCP server ng pinakamababang pahintulot na kinakailangan para sa inaasahang functionality  
   - Magpatupad ng role-based access control (RBAC) na may detalyadong mga pahintulot  
   - Regular na pagsusuri ng mga pahintulot at tuloy-tuloy na pagmamanman para sa pag-angat ng pribilehiyo

**Mga Kontrol sa Pahintulot sa Runtime:**
   - Maglagay ng mga limitasyon sa mga mapagkukunan upang maiwasan ang mga pag-atake sa pagkaubos ng mapagkukunan  
   - Gumamit ng container isolation para sa mga kapaligiran ng pagpapatupad ng tool  
   - Magpatupad ng just-in-time access para sa mga administratibong function

## 5. **Kaligtasan ng Nilalaman at Pagmamanman**

**Pagpapatupad ng Kaligtasan ng Nilalaman:**
   - **Integrasyon ng Azure Content Safety**: Gumamit ng Azure Content Safety upang matukoy ang mapanganib na nilalaman, mga pagtatangka ng jailbreak, at mga paglabag sa patakaran  
   - **Pagsusuri ng Pag-uugali**: Magpatupad ng runtime behavioral monitoring upang matukoy ang mga anomalya sa pagpapatakbo ng MCP server at mga tool  
   - **Komprehensibong Pag-log**: I-log ang lahat ng pagtatangka sa pagpapatunay, pagtawag sa tool, at mga kaganapan sa seguridad gamit ang ligtas at hindi madaling baguhin na imbakan

**Tuloy-tuloy na Pagmamanman:**
   - Real-time na alerto para sa mga kahina-hinalang pattern at hindi awtorisadong pagtatangka sa pag-access  
   - Integrasyon sa mga SIEM system para sa sentralisadong pamamahala ng mga kaganapan sa seguridad  
   - Regular na mga audit sa seguridad at penetration testing ng mga implementasyon ng MCP

## 6. **Seguridad ng Supply Chain**

**Pagpapatunay ng mga Komponent:**
   - **Dependency Scanning**: Gumamit ng automated vulnerability scanning para sa lahat ng software dependencies at mga bahagi ng AI  
   - **Pagpapatunay ng Pinagmulan**: Suriin ang pinagmulan, lisensya, at integridad ng mga modelo, pinagkukunan ng data, at mga panlabas na serbisyo  
   - **Mga Nilagdaang Package**: Gumamit ng cryptographically signed packages at beripikahin ang mga lagda bago i-deploy

**Ligtas na Pipeline ng Pag-develop:**
   - **GitHub Advanced Security**: Magpatupad ng secret scanning, dependency analysis, at CodeQL static analysis  
   - **Seguridad sa CI/CD**: Isama ang seguridad sa buong automated deployment pipelines  
   - **Integridad ng Artifact**: Magpatupad ng cryptographic verification para sa mga na-deploy na artifact at mga configuration

## 7. **Seguridad ng OAuth at Pag-iwas sa Confused Deputy**

**Implementasyon ng OAuth 2.1:**
   - **PKCE Implementation**: Gumamit ng Proof Key for Code Exchange (PKCE) para sa lahat ng kahilingan sa awtorisasyon  
   - **Tahasang Pahintulot**: Kumuha ng pahintulot ng gumagamit para sa bawat dinamiko na nakarehistrong kliyente upang maiwasan ang confused deputy attacks  
   - **Pagpapatunay ng Redirect URI**: Magpatupad ng mahigpit na pagpapatunay ng redirect URIs at mga identifier ng kliyente

**Seguridad ng Proxy:**
   - Pigilan ang bypass ng awtorisasyon sa pamamagitan ng static client ID exploitation  
   - Magpatupad ng tamang workflow ng pahintulot para sa access sa third-party API  
   - Subaybayan ang pagnanakaw ng authorization code at hindi awtorisadong access sa API

## 8. **Pagtugon sa Insidente at Pagbawi**

**Mabilis na Kakayahan sa Pagtugon:**
   - **Automated Response**: Magpatupad ng automated systems para sa pag-ikot ng kredensyal at containment ng banta  
   - **Mga Proseso ng Rollback**: Kakayahang mabilis na bumalik sa mga kilalang maayos na configuration at mga komponent  
   - **Kakayahan sa Forensics**: Detalyadong audit trails at pag-log para sa pagsisiyasat ng insidente

**Komunikasyon at Koordinasyon:**
   - Malinaw na mga proseso ng eskalasyon para sa mga insidente sa seguridad  
   - Integrasyon sa mga koponan ng pagtugon sa insidente ng organisasyon  
   - Regular na mga simulation ng insidente sa seguridad at tabletop exercises

## 9. **Pagsunod at Pamamahala**

**Pagsunod sa Regulasyon:**
   - Tiyakin na ang mga implementasyon ng MCP ay sumusunod sa mga partikular na kinakailangan ng industriya (GDPR, HIPAA, SOC 2)  
   - Magpatupad ng klasipikasyon ng data at mga kontrol sa privacy para sa pagproseso ng data ng AI  
   - Panatilihin ang komprehensibong dokumentasyon para sa audit ng pagsunod

**Pamamahala ng Pagbabago:**
   - Pormal na mga proseso ng pagsusuri sa seguridad para sa lahat ng pagbabago sa sistema ng MCP  
   - Kontrol sa bersyon at workflow ng pag-apruba para sa mga pagbabago sa configuration  
   - Regular na mga pagsusuri sa pagsunod at pagsusuri ng mga puwang

## 10. **Mga Advanced na Kontrol sa Seguridad**

**Zero Trust Architecture:**
   - **Huwag Kailanman Magtiwala, Palaging Suriin**: Tuloy-tuloy na beripikasyon ng mga gumagamit, device, at koneksyon  
   - **Micro-segmentation**: Detalyadong kontrol sa network na naghihiwalay sa bawat bahagi ng MCP  
   - **Conditional Access**: Mga kontrol sa access na nakabatay sa panganib na umaangkop sa kasalukuyang konteksto at pag-uugali

**Proteksyon sa Runtime Application:**
   - **Runtime Application Self-Protection (RASP)**: Mag-deploy ng mga teknik ng RASP para sa real-time na pagtuklas ng banta  
   - **Pagsubaybay sa Performance ng Application**: Subaybayan ang mga anomalya sa performance na maaaring magpahiwatig ng pag-atake  
   - **Dynamic Security Policies**: Magpatupad ng mga patakaran sa seguridad na umaangkop batay sa kasalukuyang kalagayan ng banta

## 11. **Integrasyon ng Microsoft Security Ecosystem**

**Komprehensibong Seguridad ng Microsoft:**
   - **Microsoft Defender for Cloud**: Pamamahala ng postura ng seguridad sa cloud para sa mga workload ng MCP  
   - **Azure Sentinel**: Cloud-native SIEM at SOAR na kakayahan para sa advanced na pagtuklas ng banta  
   - **Microsoft Purview**: Pamamahala ng data at pagsunod para sa mga workflow ng AI at mga pinagkukunan ng data

**Pamamahala ng Identidad at Access:**
   - **Microsoft Entra ID**: Pamamahala ng enterprise identity na may mga patakaran sa conditional access  
   - **Privileged Identity Management (PIM)**: Just-in-time access at workflow ng pag-apruba para sa mga administratibong function  
   - **Identity Protection**: Risk-based conditional access at automated na pagtugon sa banta

## 12. **Tuloy-tuloy na Ebolusyon ng Seguridad**

**Panatilihing Napapanahon:**
   - **Pagsubaybay sa Espesipikasyon**: Regular na pagsusuri ng mga update sa MCP specification at mga pagbabago sa gabay sa seguridad  
   - **Threat Intelligence**: Integrasyon ng mga partikular na feed ng banta sa AI at mga indicator ng kompromiso  
   - **Pakikilahok sa Komunidad ng Seguridad**: Aktibong partisipasyon sa MCP security community at mga programa sa paglalantad ng kahinaan

**Adaptive Security:**
   - **Seguridad gamit ang Machine Learning**: Gumamit ng ML-based anomaly detection para matukoy ang mga bagong pattern ng pag-atake  
   - **Predictive Security Analytics**: Magpatupad ng mga predictive model para sa proaktibong pagtukoy ng banta  
   - **Automation sa Seguridad**: Automated na pag-update ng mga patakaran sa seguridad batay sa threat intelligence at mga pagbabago sa espesipikasyon

---

## **Mahalagang Mga Mapagkukunan sa Seguridad**

### **Opisyal na Dokumentasyon ng MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

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

> **Pabatid sa Seguridad**: Ang mga praktis sa seguridad ng MCP ay mabilis na umuunlad. Palaging beripikahin laban sa kasalukuyang [MCP specification](https://spec.modelcontextprotocol.io/) at [opisyal na dokumentasyon sa seguridad](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) bago magpatupad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
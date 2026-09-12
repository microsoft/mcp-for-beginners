# MCP Security Best Practices - Update sa Setyembre 2026

Ang komprehensibong gabay na ito ay naglalahad ng mahahalagang pinakamahusay na kasanayan sa seguridad para sa
pagpapatupad ng Model Context Protocol (MCP) systems batay sa
**MCP Specification 2026-07-28** at kasalukuyang mga pamantayan ng industriya. Ang mga
kasanayang ito ay tumutugon sa parehong tradisyonal na mga isyu sa seguridad at mga banta na tiyak sa AI
na natatangi sa mga deployment ng MCP.

## Mahahalagang Kinakailangan sa Seguridad

### Mga Mandatoryong Kontrol sa Seguridad (MUST Requirements)

1. **Token Validation**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang mga token na hindi tahasang inisyu para sa mismong MCP server
2. **Authorization Verification**: Ang mga MCP server na nagpapatupad ng authorization **DAPAT** suriin ang LAHAT ng papasok na mga kahilingan at **HINDI DAPAT** gumamit ng mga session para sa authentication  
3. **User Consent**: Ang mga MCP proxy server na gumagamit ng static third-party client IDs **DAPAT** kumuha ng tahasang pahintulot para sa bawat MCP client bago ipasa ang authorization flow
4. **State Handle Security**: Ang mga MCP server **HINDI DAPAT** ituring ang pag-aari ng
	application state handle bilang authentication at **DAPAT** bigyang pahintulot ang bawat
	hingi na gumagamit nito

## Pangunahing Mga Kasanayan sa Seguridad

### 1. Pagpapatunay at Sanitasyon ng Input
- **Komprehensibong Pagpapatunay ng Input**: Patunayan at linisin ang lahat ng input upang maiwasan ang injection attacks, confused deputy problems, at prompt injection vulnerabilities
- **Pagpapatupad ng Parameter Schema**: Ipapatupad ang mahigpit na JSON schema validation para sa lahat ng tool parameters at API inputs
- **Pag-filter ng Nilalaman**: Gamitin ang Microsoft Prompt Shields at Azure Content Safety upang i-filter ang mga mapanirang nilalaman sa mga prompt at tugon
- **Sanitasyon ng Output**: Patunayan at linisin ang lahat ng mga output ng modelo bago ipakita sa mga gumagamit o downstream systems

### 2. Kahusayan sa Authentication at Authorization  
- **Mga Panlabas na Tagapagbigay ng Pagkakakilanlan**: I-delegate ang authentication sa mga kilalang identity providers (Microsoft Entra ID, OAuth 2.1 providers) kaysa gumawa ng pasadyang authentication
- **Pagpaparehistro ng Kliyente**: Mas piliin ang Client ID Metadata Documents o pre-registration; gamitin ang deprecated Dynamic Client Registration para lamang sa compatibility
- **Pinong Pinong Mga Pahintulot**: Ipatupad ang mga granular, tool-specific permissions na sumusunod sa prinsipyo ng least privilege
- **Pamamahala ng Lifecycle ng Token**: Gumamit ng mga panandaliang access token na may secure na rotation at wastong pag-verify ng audience
- **Multi-Factor Authentication**: I-require ang MFA para sa lahat ng administratibong access at sensitibong operasyon

### 3. Mga Ligtas na Protocol ng Komunikasyon
- **Transport Layer Security**: Gumamit ng HTTPS na may wastong pagpapatunay ng sertipiko
	para sa remote HTTP MCP communications; gumamit ng process isolation at environment
	credentials para sa lokal na stdio servers
- **End-to-End Encryption**: Ipatupad ang karagdagang mga layer ng encryption para sa lubhang sensitibong data sa transit at nakaimbak
- **Pamamahala ng Sertipiko**: Panatilihin ang nararapat na pamamahala ng lifecycle ng sertipiko gamit ang automated renewal processes
- **Pagpapatupad ng Bersyon ng Protocol**: Gamitin ang MCP `2026-07-28`, isama ang kinakailangang
	version metadata sa bawat kahilingan, at tanggihan ang hindi sinusuportahang mga bersyon

### 4. Advanced Rate Limiting at Proteksyon ng Mga Resource
- **Multi-layer Rate Limiting**: Ipatupad ang rate limiting base sa user, credential,
  operasyon, tool, at resource upang maiwasan ang pang-aabuso
- **Adaptive Rate Limiting**: Gumamit ng machine learning-based rate limiting na umaangkop sa mga pattern ng paggamit at mga tagapagpahiwatig ng banta
- **Pamamahala ng Quota ng Resource**: Magtakda ng nararapat na mga limitasyon para sa mga computational resources, paggamit ng memorya, at oras ng pagpapatupad
- **Proteksyon laban sa DDoS**: Mag-deploy ng komprehensibong DDoS protection at traffic analysis systems

### 5. Komprehensibong Pag-log at Pagsubaybay
- **Structured Audit Logging**: Magpatupad ng detalyado, searchable na mga log para sa lahat ng operasyon ng MCP, pagpapatupad ng tool, at mga insidente sa seguridad
- **Real-time Security Monitoring**: Mag-deploy ng SIEM systems na may AI-powered anomaly detection para sa MCP workloads
- **Privacy-compliant Logging**: I-log ang mga insidente sa seguridad habang iginagalang ang mga kinakailangan sa privacy ng data at mga regulasyon
- **Pagsasama ng Incident Response**: Iugnay ang mga sistema ng pag-log sa mga automated incident response workflows

### 6. Pinahusay na Mga Kasanayan sa Ligtas na Imbakan
- **Hardware Security Modules**: Gamitin ang HSM-backed key storage (Azure Key Vault, AWS CloudHSM) para sa mga kritikal na cryptographic operation
- **Pamamahala ng Encryption Key**: Ipatupad ang wastong key rotation, segregation, at access controls para sa encryption keys
- **Pamamahala ng Mga Lihim**: Itago ang lahat ng API keys, token, at credential sa mga dedikadong secret management systems
- **Pag-uuri ng Data**: Uriin ang data base sa mga antas ng sensibilidad at maglagay ng angkop na mga panukala para sa proteksyon

### 7. Advanced Token Management
- **Pag-iwas sa Token Passthrough**: Tahasang ipagbawal ang mga pattern ng token passthrough na nilalabag ang mga kontrol sa seguridad
- **Verification ng Audience**: Laging patunayan na ang mga audience claims ng token ay tumutugma sa tamang pagkakakilanlan ng MCP server
- **Authorization batay sa Claims**: Ipatupad ang pinong granular na authorization batay sa token claims at mga attribute ng user
- **Token Binding**: Patunayan na ang mga token ay nakatuon sa tamang resource ng MCP at
	mag-bind ng application state handles server-side sa authenticated principal

### 8. Ligtas na Application State

- **Cryptographic State Handles**: Gumawa ng opaque, non-deterministic handles
	para sa state na sumasaklaw sa mga kahilingan
- **Binding na Tiyak sa User**: I-bind ang bawat handle server-side sa authenticated
	principal; huwag pagkatiwalaan ang user ID na ibinigay ng client
- **Mga Kontrol sa Lifecycle**: Palawigin at bawiin ang mga handle, at tukuyin kung paano
	makakabawi ang mga tumatawag mula sa stale state
- **Authorization kada Kahilingan**: Muling suriin ang authorization kapag mayroong
	handle na ipinakita; ang handle ay isang pangalan, hindi kredensyal

### 9. Mga Kontrol sa Seguridad na Tiyak sa AI
- **Depensa laban sa Prompt Injection**: Mag-deploy ng Microsoft Prompt Shields na may spotlighting, delimiters, at datamarking techniques
- **Pag-iwas sa Tool Poisoning**: Patunayan ang metadata ng tool, subaybayan ang mga dynamic na pagbabago, at suriin ang integridad ng tool
- **Pagpapatunay ng Output ng Modelo**: Suriin ang mga output ng modelo para sa posibleng pagtagas ng data, mapanganib na nilalaman, o paglabag sa mga polisiya sa seguridad
- **Proteksyon ng Context Window**: Ipatupad ang mga kontrol upang maiwasan ang context window poisoning at mga atake sa manipulasyon

### 10. Seguridad sa Pagpapatupad ng Tool
- **Execution Sandboxing**: Patakbuhin ang mga tool executions sa containerized, isolated na mga kapaligiran na may mga limitasyon sa resource
- **Paghihiwalay ng Pribilehiyo**: Ipatupad ang mga tool na may pinakamababang kailangan na pribilehiyo at hiwalay na mga service accounts
- **Network Isolation**: Ipatupad ang segmentation ng network para sa mga kapaligiran ng pagpapatupad ng tool
- **Pagsubaybay sa Pagpapatupad**: Subaybayan ang tool execution para sa anomalous na pag-uugali, paggamit ng resource, at paglabag sa seguridad

### 11. Patuloy na Pagpapatunay ng Seguridad
- **Automated Security Testing**: Isama ang pagsusuri ng seguridad sa CI/CD pipelines gamit ang mga tool tulad ng GitHub Advanced Security
- **Pamamahala sa Mga Kahinaan**: Regular na i-scan ang lahat ng dependencies, kasama ang AI models at panlabas na serbisyo
- **Penetration Testing**: Isagawa ang regular na pagsuri sa seguridad na nakatuon sa mga implementasyon ng MCP
- **Mga Review ng Code sa Seguridad**: Ipatupad ang mandatoryong pagsusuri ng seguridad para sa lahat ng MCP-na kaugnay na pagbabago sa code

### 12. Seguridad sa Supply Chain para sa AI
- **Pagpapatotoo ng Komponent**: Patunayan ang pinanggalingan, integridad, at seguridad ng lahat ng mga komponent ng AI (models, embeddings, APIs)
- **Pamamahala ng Dependency**: Panatilihin ang kasalukuyang imbentaryo ng lahat ng software at AI dependencies na may pagsubaybay sa kahinaan
- **Mga Kagalang-galang na Repository**: Gumamit ng beripikado, pinagkakatiwalaang mga pinagmumulan para sa lahat ng AI models, libraries, at tools
- **Pagsubaybay sa Supply Chain**: Patuloy na subaybayan ang mga kompromiso sa mga AI service providers at model repositories

## Mga Advanced na Pattern sa Seguridad

### Zero Trust Architecture para sa MCP
- **Huwag Magsalig, Laging Suriin**: Ipatupad ang patuloy na beripikasyon para sa lahat ng kalahok sa MCP
- **Micro-segmentation**: Ihiwalay ang mga komponent ng MCP gamit ang granular na kontrol sa network at pagkakakilanlan
- **Conditional Access**: Ipatupad ang mga access control na nakabase sa panganib na umaangkop sa konteksto at kilos
- **Patuloy na Pagtatasa ng Panganib**: Dinamikong suriin ang kalagayan sa seguridad batay sa mga kasalukuyang tagapagpahiwatig ng banta

### Pagpapatupad ng AI na Nangangalaga sa Privacy
- **Pag-minimize ng Data**: I-expose lamang ang pinakamababang kailangan na data para sa bawat operasyon ng MCP
- **Differential Privacy**: Ipatupad ang mga teknik na nangangalaga sa privacy para sa pagproseso ng sensitibong data
- **Homomorphic Encryption**: Gumamit ng advanced na encryption technique para sa ligtas na computation sa naka-encrypt na data
- **Pagsasanay na Federated**: Ipatupad ang mga distributed learning approach na nagpapangalaga sa lokalidad at privacy ng data

### Incident Response para sa mga AI System
- **Mga Proseso ng AI-Specific Incident**: Bumuo ng mga procedure sa incident response na nakaangkop sa AI at MCP-specific na mga banta
- **Automated Response**: Ipatupad ang automated containment at remediation para sa mga karaniwang insidente sa seguridad ng AI  
- **Kakayahan sa Forensics**: Panatilihin ang forensic readiness para sa mga kompromiso sa AI system at paglabag sa data
- **Mga Proseso sa Pagbangon**: Magtatag ng mga pamamaraan para makabawi mula sa AI model poisoning, prompt injection attacks, at kompromiso sa serbisyo

## Mga Mapagkukunan at Pamantayan sa Pagpapatupad

### 🏔️ Hands-On Security Training
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Komprehensibong hands-on na workshop para sa pag-secure ng MCP servers sa Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Reference architecture at gabay sa pagpapatupad ng OWASP MCP Top 10

### Opisyal na Dokumentasyon ng MCP
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Kasalukuyang spesipikasyon ng protocol ng MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Opisyal na gabay sa seguridad
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Mga pattern sa HTTP authorization
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Mga kinakailangan sa transportasyon

### Mga Solusyon sa Seguridad ng Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Advanced na proteksyon laban sa prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Komprehensibong pag-filter ng nilalaman ng AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identity at access management
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Ligtas na pamamahala ng mga lihim at credential
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Pagsusuri sa seguridad ng supply chain at code

### Mga Pamantayan at Framework sa Seguridad
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Kasalukuyang gabay sa seguridad ng OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Mga panganib sa seguridad ng web application
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Mga panganib sa seguridad na tiyak sa AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Komprehensibong pamamahala ng panganib sa AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Mga sistema ng pamamahala ng impormasyon sa seguridad

### Mga Gabay sa Pagpapatupad at Tutorial
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Mga pattern sa enterprise authentication
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasyon ng identity provider
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Pinakamahusay na kasanayan sa pamamahala ng token
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Mga advanced na pattern ng encryption

### Mga Advanced na Mapagkukunan sa Seguridad
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Mga kasanayan sa ligtas na pag-develop
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Pagsusuri ng seguridad na tiyak sa AI
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodolohiya sa pagmomodelo ng banta sa AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Mga teknik sa privacy-preserving na AI

### Pagsunod at Pamamahala
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Pagsunod sa privacy sa mga systemang AI
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Responsableng pagpapatupad ng AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Mga kontrol sa seguridad para sa AI service providers
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Mga kinakailangan sa pagsunod para sa healthcare AI

### DevSecOps at Automation
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Ligtas na mga pipeline sa pag-develop ng AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Patuloy na pagpapatunay sa seguridad
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Ligtas na pag-deploy ng imprastruktura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Seguridad sa containerization ng workload ng AI

### Pagsubaybay at Incident Response  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Komprehensibong mga solusyon sa pagsubaybay
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Mga partikular na procedimiento sa insidente para sa AI
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Pamamahala ng impormasyon at mga insidente sa seguridad

- [Threat Intelligence para sa AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Mga pinanggalingan ng AI threat intelligence

## 🔄 Patuloy na Pagpapabuti

### Manatiling Napapanahon sa mga Nagbabagong Pamantayan
- **Mga Update sa Specification ng MCP**: Subaybayan ang mga opisyal na pagbabago sa specification ng MCP at mga security advisories
- **Threat Intelligence**: Mag-subscribe sa mga AI security threat feeds at mga database ng kahinaan  
- **Pakikilahok sa Komunidad**: Lumahok sa mga talakayan at working groups ng MCP security community
- **Regular na Pagsusuri**: Magsagawa ng quarterly security posture assessments at i-update ang mga gawi nang naaayon

### Pag-aambag sa Seguridad ng MCP
- **Pananaliksik sa Seguridad**: Mag-ambag sa pananaliksik ng MCP security at mga programa sa pagdedeklara ng kahinaan
- **Pagbabahagi ng Pinakamahusay na Gawi**: Ibahagi ang mga implementasyon ng seguridad at mga natutunan sa komunidad
- **Pagpapaunlad ng Pamantayan**: Lumahok sa pagpapaunlad ng specification ng MCP at paggawa ng mga security standard
- **Pag-develop ng Mga Kasangkapan**: Bumuo at magbahagi ng mga security tools at mga library para sa MCP ecosystem

---

*Ang dokumentong ito ay sumasalamin sa mga pinakamahusay na gawi sa seguridad ng MCP mula Setyembre 9, 2026,
batay sa MCP Specification `2026-07-28`. Ang mga gawi sa seguridad ay dapat regular na
suriin habang nagbabago ang protocol at tanawin ng mga banta.*

## Ano ang Susunod

- Basahin: [MCP Security Best Practices](./mcp-security-best-practices.md)
- Bumalik sa: [Security Module Overview](./README.md)
- Magpatuloy sa: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
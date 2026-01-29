# MCP Security Best Practices 2025

Ang komprehensibong gabay na ito ay naglalahad ng mahahalagang pinakamahusay na kasanayan sa seguridad para sa pagpapatupad ng Model Context Protocol (MCP) systems batay sa pinakabagong **MCP Specification 2025-11-25** at kasalukuyang mga pamantayan sa industriya. Tinatalakay ng mga kasanayang ito ang parehong tradisyunal na mga alalahanin sa seguridad at mga AI-specific na banta na natatangi sa mga deployment ng MCP.

## Critical Security Requirements

### Mandatory Security Controls (MUST Requirements)

1. **Token Validation**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang mga token na hindi tahasang inilabas para sa mismong MCP server
2. **Authorization Verification**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** beripikahin LAHAT ng mga papasok na kahilingan at **HINDI DAPAT** gumamit ng mga session para sa pagpapatunay  
3. **User Consent**: Ang mga MCP proxy server na gumagamit ng static client IDs **DAPAT** kumuha ng tahasang pahintulot ng gumagamit para sa bawat dynamically registered na kliyente
4. **Secure Session IDs**: Ang mga MCP server **DAPAT** gumamit ng cryptographically secure, non-deterministic na mga session ID na nilikha gamit ang secure random number generators

## Core Security Practices

### 1. Input Validation & Sanitization
- **Komprehensibong Input Validation**: I-validate at i-sanitize ang lahat ng input upang maiwasan ang injection attacks, confused deputy problems, at prompt injection vulnerabilities
- **Parameter Schema Enforcement**: Magpatupad ng mahigpit na JSON schema validation para sa lahat ng tool parameters at API inputs
- **Content Filtering**: Gamitin ang Microsoft Prompt Shields at Azure Content Safety upang salain ang malisyosong nilalaman sa mga prompt at tugon
- **Output Sanitization**: I-validate at i-sanitize ang lahat ng output ng modelo bago ipakita sa mga gumagamit o downstream na mga sistema

### 2. Authentication & Authorization Excellence  
- **External Identity Providers**: I-delegate ang authentication sa mga kilalang identity providers (Microsoft Entra ID, OAuth 2.1 providers) sa halip na magpatupad ng custom authentication
- **Fine-grained Permissions**: Magpatupad ng granular, tool-specific na mga permiso alinsunod sa prinsipyo ng least privilege
- **Token Lifecycle Management**: Gumamit ng short-lived access tokens na may secure rotation at tamang audience validation
- **Multi-Factor Authentication**: Kailanganin ang MFA para sa lahat ng administratibong access at sensitibong operasyon

### 3. Secure Communication Protocols
- **Transport Layer Security**: Gumamit ng HTTPS/TLS 1.3 para sa lahat ng komunikasyon ng MCP na may tamang certificate validation
- **End-to-End Encryption**: Magpatupad ng karagdagang mga layer ng encryption para sa mga sensitibong data habang nasa transit at nakaimbak
- **Certificate Management**: Panatilihin ang tamang pamamahala ng lifecycle ng certificate na may automated renewal processes
- **Protocol Version Enforcement**: Gumamit ng kasalukuyang bersyon ng MCP protocol (2025-11-25) na may tamang version negotiation.

### 4. Advanced Rate Limiting & Resource Protection
- **Multi-layer Rate Limiting**: Magpatupad ng rate limiting sa antas ng user, session, tool, at resource upang maiwasan ang pang-aabuso
- **Adaptive Rate Limiting**: Gumamit ng machine learning-based rate limiting na umaangkop sa mga pattern ng paggamit at mga indikasyon ng banta
- **Resource Quota Management**: Magtakda ng angkop na mga limitasyon para sa computational resources, paggamit ng memorya, at oras ng pagpapatupad
- **DDoS Protection**: Mag-deploy ng komprehensibong DDoS protection at mga sistema ng pagsusuri ng trapiko

### 5. Comprehensive Logging & Monitoring
- **Structured Audit Logging**: Magpatupad ng detalyado, searchable na mga log para sa lahat ng operasyon ng MCP, pagpapatupad ng tool, at mga kaganapan sa seguridad
- **Real-time Security Monitoring**: Mag-deploy ng SIEM systems na may AI-powered anomaly detection para sa mga MCP workload
- **Privacy-compliant Logging**: Mag-log ng mga kaganapan sa seguridad habang iginagalang ang mga kinakailangan at regulasyon sa privacy ng data
- **Incident Response Integration**: Ikonekta ang mga sistema ng pag-log sa automated incident response workflows

### 6. Enhanced Secure Storage Practices
- **Hardware Security Modules**: Gumamit ng HSM-backed key storage (Azure Key Vault, AWS CloudHSM) para sa mga kritikal na cryptographic operations
- **Encryption Key Management**: Magpatupad ng tamang key rotation, segregation, at access controls para sa mga encryption key
- **Secrets Management**: Itago ang lahat ng API keys, token, at kredensyal sa mga dedikadong sistema ng pamamahala ng lihim
- **Data Classification**: Iklasipika ang data batay sa antas ng sensitibidad at magpatupad ng angkop na mga hakbang sa proteksyon

### 7. Advanced Token Management
- **Token Passthrough Prevention**: Tahasang ipagbawal ang mga pattern ng token passthrough na lumalampas sa mga kontrol sa seguridad
- **Audience Validation**: Laging beripikahin na ang mga audience claim ng token ay tumutugma sa nilalayong pagkakakilanlan ng MCP server
- **Claims-based Authorization**: Magpatupad ng fine-grained authorization batay sa mga claim ng token at mga katangian ng gumagamit
- **Token Binding**: Itali ang mga token sa mga partikular na session, gumagamit, o device kung naaangkop

### 8. Secure Session Management
- **Cryptographic Session IDs**: Gumawa ng mga session ID gamit ang cryptographically secure random number generators (hindi predictable na mga sequence)
- **User-specific Binding**: Itali ang mga session ID sa user-specific na impormasyon gamit ang secure na mga format tulad ng `<user_id>:<session_id>`
- **Session Lifecycle Controls**: Magpatupad ng tamang session expiration, rotation, at invalidation na mga mekanismo
- **Session Security Headers**: Gumamit ng angkop na HTTP security headers para sa proteksyon ng session

### 9. AI-Specific Security Controls
- **Prompt Injection Defense**: Mag-deploy ng Microsoft Prompt Shields na may spotlighting, delimiters, at datamarking techniques
- **Tool Poisoning Prevention**: I-validate ang metadata ng tool, subaybayan ang mga dynamic na pagbabago, at beripikahin ang integridad ng tool
- **Model Output Validation**: I-scan ang mga output ng modelo para sa posibleng data leakage, mapanganib na nilalaman, o paglabag sa mga patakaran sa seguridad
- **Context Window Protection**: Magpatupad ng mga kontrol upang maiwasan ang context window poisoning at mga manipulasyon na pag-atake

### 10. Tool Execution Security
- **Execution Sandboxing**: Patakbuhin ang mga pagpapatupad ng tool sa containerized, isolated na mga kapaligiran na may mga limitasyon sa resources
- **Privilege Separation**: Patakbuhin ang mga tool gamit ang pinakamababang kinakailangang mga pribilehiyo at hiwalay na mga service account
- **Network Isolation**: Magpatupad ng network segmentation para sa mga kapaligiran ng pagpapatupad ng tool
- **Execution Monitoring**: Subaybayan ang pagpapatupad ng tool para sa anomalous na pag-uugali, paggamit ng resources, at paglabag sa seguridad

### 11. Continuous Security Validation
- **Automated Security Testing**: Isama ang security testing sa CI/CD pipelines gamit ang mga tool tulad ng GitHub Advanced Security
- **Vulnerability Management**: Regular na i-scan ang lahat ng dependencies, kabilang ang mga AI model at mga external na serbisyo
- **Penetration Testing**: Magsagawa ng regular na mga pagsusuri sa seguridad na partikular na tumutok sa mga implementasyon ng MCP
- **Security Code Reviews**: Magpatupad ng mandatory security reviews para sa lahat ng mga pagbabago sa code na may kaugnayan sa MCP

### 12. Supply Chain Security for AI
- **Component Verification**: Beripikahin ang pinagmulan, integridad, at seguridad ng lahat ng AI components (mga modelo, embeddings, API)
- **Dependency Management**: Panatilihin ang kasalukuyang imbentaryo ng lahat ng software at AI dependencies na may pagsubaybay sa mga kahinaan
- **Trusted Repositories**: Gumamit ng beripikado, pinagkakatiwalaang mga pinagmulan para sa lahat ng AI models, libraries, at tools
- **Supply Chain Monitoring**: Patuloy na subaybayan ang mga kompromiso sa mga AI service provider at mga repository ng modelo

## Advanced Security Patterns

### Zero Trust Architecture for MCP
- **Never Trust, Always Verify**: Magpatupad ng tuloy-tuloy na beripikasyon para sa lahat ng kalahok sa MCP
- **Micro-segmentation**: Ihiwalay ang mga bahagi ng MCP gamit ang granular na mga kontrol sa network at pagkakakilanlan
- **Conditional Access**: Magpatupad ng risk-based access controls na umaangkop sa konteksto at pag-uugali
- **Continuous Risk Assessment**: Dinamikong suriin ang security posture batay sa kasalukuyang mga indikasyon ng banta

### Privacy-Preserving AI Implementation
- **Data Minimization**: I-expose lamang ang pinakamababang kinakailangang data para sa bawat operasyon ng MCP
- **Differential Privacy**: Magpatupad ng mga teknik na nagpoprotekta sa privacy para sa pagproseso ng sensitibong data
- **Homomorphic Encryption**: Gumamit ng advanced na mga teknik ng encryption para sa secure na computation sa naka-encrypt na data
- **Federated Learning**: Magpatupad ng distributed learning approaches na nagpoprotekta sa data locality at privacy

### Incident Response for AI Systems
- **AI-Specific Incident Procedures**: Bumuo ng mga pamamaraan sa pagtugon sa insidente na iniakma sa mga AI at MCP-specific na banta
- **Automated Response**: Magpatupad ng automated containment at remediation para sa mga karaniwang insidente sa seguridad ng AI  
- **Forensic Capabilities**: Panatilihin ang forensic readiness para sa mga kompromiso sa AI system at paglabag sa data
- **Recovery Procedures**: Magtatag ng mga pamamaraan para sa pagbangon mula sa AI model poisoning, prompt injection attacks, at kompromiso sa serbisyo

## Implementation Resources & Standards

### Official MCP Documentation
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Kasalukuyang MCP protocol specification
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Opisyal na gabay sa seguridad
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Mga pattern ng authentication at authorization
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Mga kinakailangan sa transport layer security

### Microsoft Security Solutions
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Advanced na proteksyon laban sa prompt injection
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Komprehensibong AI content filtering
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Enterprise identity at access management
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Secure na pamamahala ng mga lihim at kredensyal
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Supply chain at code security scanning

### Security Standards & Frameworks
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Kasalukuyang gabay sa seguridad ng OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Mga panganib sa seguridad ng web application
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specific na mga panganib sa seguridad
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Komprehensibong pamamahala ng panganib sa AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Mga sistema ng pamamahala ng impormasyon sa seguridad

### Implementation Guides & Tutorials
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Mga pattern ng enterprise authentication
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasyon ng identity provider
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Pinakamahusay na kasanayan sa pamamahala ng token
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Advanced na mga pattern ng encryption

### Advanced Security Resources
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Mga kasanayan sa secure development
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specific na security testing
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodolohiya ng AI threat modeling
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Mga teknik sa privacy-preserving AI

### Compliance & Governance
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Pagsunod sa privacy sa mga AI system
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Responsable na pagpapatupad ng AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Mga kontrol sa seguridad para sa mga AI service provider
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Mga kinakailangan sa pagsunod sa healthcare AI

### DevSecOps & Automation
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Secure na mga pipeline sa pag-develop ng AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Tuloy-tuloy na pag-validate ng seguridad
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Secure na deployment ng imprastruktura
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Seguridad sa containerization ng AI workload

### Monitoring & Incident Response  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Komprehensibong mga solusyon sa monitoring
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specific na mga pamamaraan sa pagtugon sa insidente
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Security information at event management
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Mga pinagmulan ng AI threat intelligence

## 🔄 Continuous Improvement

### Stay Current with Evolving Standards
- **MCP Specification Updates**: Subaybayan ang mga opisyal na pagbabago sa MCP specification at mga advisory sa seguridad
- **Threat Intelligence**: Mag-subscribe sa mga AI security threat feed at mga database ng kahinaan  
- **Community Engagement**: Makilahok sa mga talakayan at working groups ng MCP security community
- **Regular Assessment**: Magsagawa ng quarterly na pagsusuri sa security posture at i-update ang mga kasanayan nang naaayon

### Contributing to MCP Security
- **Security Research**: Mag-ambag sa MCP security research at mga programa sa paglalantad ng kahinaan
- **Best Practice Sharing**: Ibahagi ang mga implementasyon sa seguridad at mga natutunang aral sa komunidad
- **Pamantayang Pag-unlad**: Lumahok sa pagbuo ng MCP specification at paggawa ng pamantayan sa seguridad  
- **Pagbuo ng Kasangkapan**: Bumuo at magbahagi ng mga kasangkapan at aklatan sa seguridad para sa MCP ecosystem  

---

*Ang dokumentong ito ay sumasalamin sa mga pinakamahusay na kasanayan sa seguridad ng MCP hanggang Disyembre 18, 2025, batay sa MCP Specification 2025-11-25. Ang mga kasanayan sa seguridad ay dapat regular na suriin at i-update habang umuunlad ang protocol at ang kalagayan ng mga banta.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
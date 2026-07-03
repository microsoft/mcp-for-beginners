# MCP Security: Complete Protection for AI Systems

[![MCP Security Best Practices](../../../translated_images/pcm/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Click di picture wey dey above to watch video for dis lesson)_

Security na di foundation for AI system design, na why we put am as our second section. Dis one dey follow Microsoft **Secure by Design** principle from di [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Di Model Context Protocol (MCP) dey bring strong new powers to AI-driven apps while e dey still bring unique security wahala wey pass normal software risks. MCP systems dey face both old security wahala dem (secure coding, least privilege, supply chain security) plus new AI-specific threats like prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough weaknesses, and dynamic capability modification.

Dis lesson go show you di most important security wahala for MCP wey include authentication, authorization, too much permissions, indirect prompt injection, session security, confused deputy problems, token management, and supply chain weaknesses. You go learn practical controls and best practices to reduce these risks and use Microsoft tools like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to make your MCP deployment strong.

## Learning Objectives

By the time you finish dis lesson, you go fit:

- **Identify MCP-Specific Threats**: Recognize di special security wahala for MCP systems like prompt injection, tool poisoning, too much permissions, session hijacking, confused deputy problems, token passthrough weaknesses, and supply chain risks
- **Apply Security Controls**: Put correct mitigations for ground like strong authentication, least privilege access, secure token management, session security controls, and supply chain checking
- **Leverage Microsoft Security Solutions**: Understand and deploy Microsoft Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP work
- **Validate Tool Security**: Know why tool metadata validation matter, watch for dynamic changes, and defend against indirect prompt injection attacks
- **Integrate Best Practices**: Join solid security basics (secure coding, server hardening, zero trust) with MCP-specific controls for full protection

# MCP Security Architecture & Controls

Modern MCP implementations need layered security way wey dey handle normal software security and AI-specific threats. Di fast changing MCP specification dey improve security controls as e dey develop, so e fit join enterprise security systems and best practices well well.

Research from [Microsoft Digital Defense Report](https://aka.ms/mddr) show say **98% of reported breaches fit don prevent if people dey do proper security hygiene**. Di best protection stil dey combine correct security practice with MCP-specific controls—basic security measures still dey di top way to reduce risk well.

## Current Security Landscape

> **Note:** Dis info dey reflect MCP security standards for **February 5, 2026**, based on **MCP Specification 2025-11-25**. MCP protocol dey evolve quick quick, and future versions fit bring new authentication methods and better controls. Make sure you dey check di current [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repo](https://github.com/modelcontextprotocol), and [security best practices docs](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) for di latest updates.

> **Looking ahead:** di `2026-07-28` release candidate go tighten authorization more — clients go need confirm di `iss` parameter for authorization responses (RFC 9207), declare OpenID Connect `application_type` when Dynamic Client Registration, and tie registered credentials to authorization server wey issue am. Check [What's Changing in MCP: The 2026-07-28 Release Candidate](../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) for full list of authorization SEPs.

## 🏔️ MCP Security Summit Workshop (Sherpa)

For **hands-on security training**, we strongly recommend di **MCP Security Summit Workshop** (Sherpa) - a full guided security trip to secure MCP servers for Microsoft Azure.

### Workshop Overview

Di [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) dey give practical, actionable security training with a confirmed "vulnerable → exploit → fix → validate" way. You go:

- **Learn by Breaking Things**: See vulnerabilities first hand by attacking purposely insecure servers
- **Use Azure-Native Security**: Use Azure Entra ID, Key Vault, API Management, and AI Content Safety
- **Follow Defence-in-Depth**: Move through camps wey dey build strong security layers
- **Apply OWASP Standards**: Every step dey match [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Get Production Code**: Walk away with strong, tested implementations

### The Expedition Route

| Camp | Focus | OWASP Risks Covered |
|------|-------|---------------------|
| **Base Camp** | MCP basics & authentication vulnerabilities | MCP01, MCP07 |
| **Camp 1: Identity** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Camp 2: Gateway** | API Management, Private Endpoints, governance | MCP02, MCP06, MCP07, MCP09 |
| **Camp 3: I/O Security** | Prompt injection, PII protection, content safety | MCP03, MCP05, MCP06, MCP10 |
| **Camp 4: Monitoring** | Log Analytics, dashboards, threat detection | MCP04, MCP08 |
| **The Summit** | Red Team / Blue Team integration test | All |

**Get Started**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 Security Risks

Di [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) talk about di ten most important security risks for MCP implementations:

| Risk | Description | Azure Mitigation |
|------|-------------|------------------|
| **MCP01** | Token Mismanagement & Secret Exposure | Azure Key Vault, Managed Identity |
| **MCP02** | Privilege Escalation via Scope Creep | RBAC, Conditional Access |
| **MCP03** | Tool Poisoning | Tool validation, integrity verification |
| **MCP04** | Software Supply Chain Attacks & Dependency Tampering | GitHub Advanced Security, dependency scanning |
| **MCP05** | Command Injection & Execution | Input validation, sandboxing |
| **MCP06** | Intent Flow Subversion | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Insufficient Authentication & Authorization | Azure Entra ID, OAuth 2.1 with PKCE |
| **MCP08** | Lack of Audit and Telemetry | Azure Monitor, Application Insights |
| **MCP09** | Shadow MCP Servers | API Center governance, network isolation |
| **MCP10** | Context Injection & Over-Sharing | Data classification, minimal exposure |

### Evolution of MCP Authentication

Di MCP specification don change well well on how e dey do authentication and authorization:

- **Original Way**: Early specs make developers build special authentication servers, and MCP servers waka like OAuth 2.0 Authorization Servers wey manage user authentication direct
- **Current Standard (2025-11-25)**: Updated spec allow MCP servers to pass authentication to outside identity providers (like Microsoft Entra ID), to make security better and reduce how e hard to implement
- **Transport Layer Security**: Improved support for secure transport with correct authentication for local (STDIO) and remote (Streamable HTTP) connections

## Authentication & Authorization Security

### Current Security Challenges

Modern MCP implementations dey face several authentication and authorization wahala:

### Risks & Threat Ways

- **Misconfigured Authorization Logic**: Bad authorization code for MCP servers fit expose sensitive data and wrong apply access control
- **OAuth Token Compromise**: Local MCP server token thief fit make attackers act as servers and enter other services
- **Token Passthrough Weaknesses**: Bad token handling fit create security control bypass and break accountability
- **Excessive Permissions**: MCP servers with too much permission break least privilege rule and open more attack door

#### Token Passthrough: Na Serious Bad Practice

**Token passthrough no dey allowed at all** for current MCP authorization spec because e get serious security problem:

##### Security Control Bypass
- MCP servers and downstream APIs dey do important security controls (rate limiting, request checking, traffic watching) wey depend on token validation
- Client to API direct token use dey skip these important protections, damage di security system

##### Accountability & Audit Wahala  
- MCP servers no fit know if client dey use upstream token, so audit trails go break
- Downstream resource server logs go show wrong request source, no be real MCP server
- Incident investigation and compliance audit go hard pass before

##### Data Theft Risks
- Unchecked token claims fit let bad people wey get stolen tokens use MCP servers as road to carry data comot
- Trust boundary break fit make unauthorized access wey no dey protected by security controls

##### Multiple Service Attack Vectors
- Stolen tokens wey many services accept fit make attackers waka side side for connected systems
- Trust between services fit break if token origin no fit verify

### Security Controls & Mitigations

**Critical Security Requirements:**

> **MANDATORY**: MCP servers **MUST NOT** accept any tokens wey no explicitly issue for MCP server

#### Authentication & Authorization Controls

- **Deep Authorization Review**: Do full audit of MCP server authorization code to make sure only correct users and clients fit enter sensitive resources
  - **Implementation Guide**: [Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identity Integration**: [Using Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Use [Microsoft token validation and lifecycle best practices](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Check token audience claims match MCP server identity
  - Put correct token rotation and expiry rules
  - Stop token replay attack and unauthorized token use

- **Protected Token Storage**: Keep tokens safe with encryption both for storage and for transit
  - **Best Practices**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Access Control Implementation

- **Principle of Least Privilege**: Give MCP servers only minimum permission wey dem need to work
  - Regularly review and update permissions to stop scope creep
  - **Microsoft Documentation**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Apply fine-grain roles assignment
  - Limit roles sharply to specific resources and actions
  - Avoid wide or unnecessary permission wey open attack surface

- **Continuous Permission Monitoring**: Always audit and monitor access
  - Watch permission use for unusual patterns
  - Quickly fix too much or unused privileges

## AI-Specific Security Threats

### Prompt Injection & Tool Manipulation Attacks

Modern MCP implementations dey face sharp AI-specific attack ways wey traditional security no fit handle fully:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

**Indirect Prompt Injection** na one of di most serious weaknesses for MCP AI systems. Attackers go hide bad instructions inside external content—documents, web pages, emails, or data sources—wey di AI system go later treat as real commands.

**Attack Scenarios:**
- **Document-based Injection**: Bad instructions hide in processed documents wey make AI do wrong actions
- **Web Content Exploitation**: Corrupt websites with embedded prompts wey change AI behavior when dem scrape am
- **Email-based Attacks**: Bad prompts for emails wey make AI assistants leak info or do things wey dem no supposed
- **Data Source Contamination**: Corrupted databases or APIs wey give bad content to AI systems

**Real-World Impact**: These attacks fit cause data theft, privacy leak, harmful content creation, and change how users interact. For detailed story, see [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/pcm/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning Attacks**

**Tool Poisoning** dey target metadata wey define MCP tools, exploit how LLMs interpret tool description and parameter to decide how to act.

**Attack Ways:**
- **Metadata Manipulation**: Attackers insert bad instructions inside tool descriptions, parameter definitions, or usage examples
- **Invisible Instructions**: Hidden prompts inside tool metadata wey AI models dey process but humans no dey see
- **Dynamic Tool Modification ("Rug Pulls")**: Tools wey users approve later change to do bad things without user sabi
- **Parameter Injection**: Malicious content inside tool parameter schema wey affect model behavior
**Hosted Server Risks**: Remote MCP servers dey carry higher risks as tool definitions fit update after original user approval, wey fit make tools wey first dey safe turn malicious. For full analysis, check [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/pcm/tool-injection.3b0b4a6b24de6bef.webp)

#### **Additional AI Attack Vectors**

- **Cross-Domain Prompt Injection (XPIA)**: Sophisticated attacks wey use content from different domains to waka pass security controls
- **Dynamic Capability Modification**: Real-time changes to tool capabilities wey fit escape original security checks
- **Context Window Poisoning**: Attacks wey dey change big context windows to hide bad instructions
- **Model Confusion Attacks**: Using model limits to cause unpredictable or unsafe actions


### AI Security Risk Impact

**High-Impact Consequences:**
- **Data Exfiltration**: Unauthorized access and stealing of sensitive enterprise or personal data
- **Privacy Breaches**: Exposure of personally identifiable information (PII) and confidential business data  
- **System Manipulation**: Unplanned changes to important systems and workflows
- **Credential Theft**: Compromise of authentication tokens and service credentials
- **Lateral Movement**: Using compromised AI systems as bridge for wider network attacks

### Microsoft AI Security Solutions

#### **AI Prompt Shields: Advanced Protection Against Injection Attacks**

Microsoft **AI Prompt Shields** dey provide full protection against both direct and indirect prompt injection attacks with plenty security layers:

##### **Core Protection Mechanisms:**

1. **Advanced Detection & Filtering**
   - Machine learning algorithms plus NLP methods dey detect bad instructions inside external content
   - Real-time checking of documents, websites, emails, and data sources for hidden threats
   - Context understanding of correct vs. bad prompt patterns

2. **Spotlighting Techniques**  
   - Separate trusted system instructions from possibly compromised external inputs
   - Text transformation ways wey improve model relevance but still isolate bad content
   - Helps AI systems preserve correct instruction order and ignore injected commands

3. **Delimiter & Datamarking Systems**
   - Clear border between trusted system messages and external input text
   - Special markers dey show boundaries between trusted and untrusted data origins
   - Clear separation stop instruction confusion and unauthorized command running

4. **Continuous Threat Intelligence**
   - Microsoft dey always watch new attack patterns and update defenses
   - Proactive threat hunting for new injection ways and attack things
   - Regular security model patches to keep up with changing threats

5. **Azure Content Safety Integration**
   - Part of full Azure AI Content Safety package
   - Extra detection for jailbreak tries, harmful content, and security rule breakings
   - Unified security controls across AI application parts

**Implementation Resources**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/pcm/prompt-shield.ff5b95be76e9c78c.webp)


## Advanced MCP Security Threats

### Session Hijacking Vulnerabilities

**Session hijacking** na serious attack wey happen for stateful MCP systems where people wey no get right fit get and use correct session IDs to act like users and do unauthorized things.

#### **Attack Scenarios & Risks**

- **Session Hijack Prompt Injection**: Attackers wey get stolen session IDs fit put malicious events inside servers wey share session state, fit trigger bad actions or access sensitive data
- **Direct Impersonation**: Stolen session IDs make attackers fit call MCP servers directly without authentication, as if na real users dem be
- **Compromised Resumable Streams**: Attackers fit stop requests before time, make real clients resume with possible bad content

#### **Security Controls for Session Management**

**Critical Requirements:**
- **Authorization Verification**: MCP servers wey dey implement authorization **MUST** check ALL incoming requests and **MUST NOT** depend on sessions for authentication
- **Secure Session Generation**: Make sure session IDs strong and random with cryptographically secure random number generators
- **User-Specific Binding**: Tie session IDs to user info like `<user_id>:<session_id>` to stop cross-user session misuse
- **Session Lifecycle Management**: Set good expiration, rotation, and invalidation to reduce risk window
- **Transport Security**: Make HTTPS compulsory for all communication to stop session ID interception

### Confused Deputy Problem

**Confused deputy problem** dey happen when MCP servers act as authentication middlemen between clients and third-party services, creating chance for bypassing authorization through static client ID abuse.

#### **Attack Mechanics & Risks**

- **Cookie-based Consent Bypass**: Previous user authentication fit make consent cookies wey attackers fit use through bad authorization requests with designed redirect URIs
- **Authorization Code Theft**: Existing consent cookies fit make authorization servers skip consent screens, redirect codes go attacker-controlled sites  
- **Unauthorized API Access**: Stolen authorization codes fit allow token exchange and user impersonation without permission

#### **Mitigation Strategies**

**Mandatory Controls:**
- **Explicit Consent Requirements**: MCP proxy servers using static client IDs **MUST** get user consent for every dynamically registered client
- **OAuth 2.1 Security Implementation**: Follow current OAuth security rules including PKCE (Proof Key for Code Exchange) for all authorization requests
- **Strict Client Validation**: Strong validation for redirect URIs and client IDs to prevent abuse

### Token Passthrough Vulnerabilities  

**Token passthrough** na clear bad practice wey MCP servers dey accept client tokens without proper check and push am to downstream APIs, breaking MCP authorization rules.

#### **Security Implications**

- **Control Circumvention**: Client-to-API token direct use bypass critical rate limits, validation, and monitoring
- **Audit Trail Corruption**: Tokens from upstream make client identification hard, break investigation ability
- **Proxy-based Data Exfiltration**: Bad actors fit use servers as proxies for unauthorized data with unchecked tokens
- **Trust Boundary Violations**: Downstream services trust assumptions fit break if token origin no clear
- **Multi-service Attack Expansion**: Accepted compromised tokens across services enable lateral attacks

#### **Required Security Controls**

**Non-negotiable Requirements:**
- **Token Validation**: MCP servers **MUST NOT** accept tokens wey no explicitly issued for the MCP server
- **Audience Verification**: Always check token audience claims match MCP server identity
- **Proper Token Lifecycle**: Use short-lived access tokens with secure rotation

## Supply Chain Security for AI Systems

Supply chain security don expand beyond old school software dependencies to cover whole AI system. Today MCP systems must properly verify and monitor all AI parts, as each fit cause vulnerabilities wey fit harm system integrity.

### Expanded AI Supply Chain Components

**Traditional Software Dependencies:**
- Open-source libraries and frameworks
- Container images and base systems  
- Development tools and build pipelines
- Infrastructure components and services

**AI-Specific Supply Chain Elements:**
- **Foundation Models**: Pre-trained models from different providers wey need provenance checks
- **Embedding Services**: External vector and semantic search services
- **Context Providers**: Data sources, knowledge bases, and document repositories  
- **Third-party APIs**: External AI services, ML pipelines, and data processing endpoints
- **Model Artifacts**: Weights, configs, and fine-tuned model versions
- **Training Data Sources**: Datasets used for model training and fine-tuning

### Comprehensive Supply Chain Security Strategy

#### **Component Verification & Trust**
- **Provenance Validation**: Confirm origin, licensing, and integrity of all AI parts before integration
- **Security Assessment**: Scan and review AI models, data sources, and services for vulnerabilities
- **Reputation Analysis**: Check security history and practices of AI service providers
- **Compliance Verification**: Make sure all parts meet company security and regulation rules

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Integrate security scans all through automated deployment pipeline
- **Artifact Integrity**: Use cryptographic checks for all deployed artifacts (code, models, configs)
- **Staged Deployment**: Deploy gradually with security validation at each step
- **Trusted Artifact Repositories**: Deploy only from verified, secure artifact registries and repos

#### **Continuous Monitoring & Response**
- **Dependency Scanning**: Always monitor software and AI component dependencies for vulnerabilities
- **Model Monitoring**: Watch model behavior, performance drift, and security issues continually
- **Service Health Tracking**: Keep eye on external AI services for availability, security, and policy changes
- **Threat Intelligence Integration**: Use threat feeds specific to AI and ML security risks

#### **Access Control & Least Privilege**
- **Component-level Permissions**: Limit access to models, data, and services to what business need
- **Service Account Management**: Use dedicated service accounts with minimum required rights
- **Network Segmentation**: Separate AI parts and restrict network access between services
- **API Gateway Controls**: Use central API gateways to control and watch access to external AI services

#### **Incident Response & Recovery**
- **Rapid Response Procedures**: Ready processes to patch or replace hacked AI components
- **Credential Rotation**: Automated rotation of secrets, API keys, and credentials
- **Rollback Capabilities**: Ability to quickly revert to last good AI component versions
- **Supply Chain Breach Recovery**: Specific steps to handle upstream AI service hacks

### Microsoft Security Tools & Integration

**GitHub Advanced Security** dey provide full supply chain protection including:
- **Secret Scanning**: Automatic detection of keys, tokens, and credentials inside repos
- **Dependency Scanning**: Vulnerability check for open-source dependencies and libraries
- **CodeQL Analysis**: Static code review for security problems and bugs
- **Supply Chain Insights**: See dependency health and security status

**Azure DevOps & Azure Repos Integration:**
- Smooth security scanning for Microsoft dev platforms
- Automatic security checks in Azure Pipelines for AI jobs
- Policy enforcement for safe AI component deployment

**Microsoft Internal Practices:**
Microsoft dey use broad supply chain security practice for all products. Learn how for [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Best Practices

MCP systems build on top of your organisation security foundation. Strong foundation practices go improve overall AI system and MCP security levels.

### Core Security Fundamentals

#### **Secure Development Practices**
- **OWASP Compliance**: Protect against [OWASP Top 10](https://owasp.org/www-project-top-ten/) web app vulnerabilities
- **AI-Specific Protections**: Put controls for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Secure Secrets Management**: Use special vaults for tokens, API keys, and sensitive config data
- **End-to-End Encryption**: Secure communication all through application components and data path
- **Input Validation**: Strong checks on all user inputs, API parameters, and data sources

#### **Infrastructure Hardening**
- **Multi-Factor Authentication**: Mandatory MFA for all admin and service accounts
- **Patch Management**: Automated, timely patching for OSes, frameworks, and dependencies  
- **Identity Provider Integration**: Centralized identity management via enterprise identity providers (Microsoft Entra ID, Active Directory)
- **Network Segmentation**: Logical isolation of MCP parts to reduce lateral movement risk
- **Principle of Least Privilege**: Minimal permissions for all system parts and accounts

#### **Security Monitoring & Detection**
- **Comprehensive Logging**: Detailed logs of AI app activity including MCP client-server actions
- **SIEM Integration**: Centralized security info and event management to spot anomalies
- **Behavioral Analytics**: AI-powered monitoring to detect odd system and user behaviour
- **Threat Intelligence**: Integrate external threat feeds and compromise indicators (IOCs)
- **Incident Response**: Clear steps for security incident detection, response, and recovery

#### **Zero Trust Architecture**
- **Never Trust, Always Verify**: Always check users, devices, and network connections
- **Micro-Segmentation**: Fine network controls that isolate workloads and services
- **Identity-Centric Security**: Security rules based on verified identities, no based on network location
- **Continuous Risk Assessment**: Dynamic security checks based on current context and behavior
- **Conditional Access**: Access controls that adjust according to risk, location, and device trust

### Enterprise Integration Patterns

#### **Microsoft Security Ecosystem Integration**
- **Microsoft Defender for Cloud**: Full cloud security posture management
- **Azure Sentinel**: Cloud-native SIEM and SOAR for AI workload protection
- **Microsoft Entra ID**: Enterprise identity and access management with conditional access policies
- **Azure Key Vault**: Centralized secrets management with hardware security module (HSM)
- **Microsoft Purview**: Data governance and compliance for AI data sources and workflows

#### **Compliance & Governance**
- **Regulatory Alignment**: Make sure MCP implementations follow industry compliance rules (GDPR, HIPAA, SOC 2)
- **Data Classification**: Proper categorization and handling of sensitive data processed by AI systems
- **Audit Trails**: Comprehensive logging for regulatory compliance and forensic investigation
- **Privacy Controls**: Implementation of privacy-by-design principles in AI system architecture
- **Change Management**: Formal processes for security reviews of AI system modifications

Dem foundational practices dey create strong security baseline wey go improve how MCP-specific security controls dey work and dey provide full protection for AI-driven applications.

## Key Security Takeaways

- **Layered Security Approach**: Combine foundational security practices (secure coding, least privilege, supply chain verification, continuous monitoring) with AI-specific controls for comprehensive protection

- **AI-Specific Threat Landscape**: MCP systems dey face unique risks like prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, and too much permissions wey need special mitigations

- **Authentication & Authorization Excellence**: Implement strong authentication using external identity providers (Microsoft Entra ID), enforce correct token validation, and no ever accept tokens wey never explicitly come for your MCP server

- **AI Attack Prevention**: Use Microsoft Prompt Shields and Azure Content Safety to protect against indirect prompt injection and tool poisoning attacks, while you dey validate tool metadata and dey monitor for dynamic changes

- **Session & Transport Security**: Use cryptographically secure, non-deterministic session IDs wey associate with user identities, implement correct session lifecycle management, and no ever use sessions for authentication

- **OAuth Security Best Practices**: Stop confused deputy attacks by getting explicit user consent for dynamically registered clients, proper OAuth 2.1 usage with PKCE, and strict redirect URI validation  

- **Token Security Principles**: Avoid token passthrough bad practices, validate token audience claims, use short-lived tokens with secure rotation, and maintain clear trust boundaries

- **Comprehensive Supply Chain Security**: Treat all AI ecosystem parts (models, embeddings, context providers, external APIs) with the same security strictness as traditional software dependencies

- **Continuous Evolution**: Keep up to date with rapidly changing MCP specifications, contribute to security community standards, and maintain adaptive security levels as the protocol dey mature

- **Microsoft Security Integration**: Use Microsoft full security ecosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for better MCP deployment protection

## Comprehensive Resources

### **Official MCP Security Documentation**
- [MCP Specification (Current: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Security Resources**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Complete OWASP MCP Top 10 with Azure how to implement guide
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Official OWASP MCP security risks
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on security training for MCP on Azure

### **Security Standards & Best Practices**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **AI Security Research & Analysis**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementation Guides & Tutorials**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Supply Chain Security**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Additional Security Documentation**

For full security guidance, check these special documents for this section:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Complete security best practices for MCP implementations
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Practical examples for Azure Content Safety integration  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Latest security controls and methods for MCP deployments
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Quick guide for essential MCP security practices
- **[BlueHat 2026: Securing the future of AI: Securing MCP with defense in depth patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Defense-in-depth patterns from Microsoft Security Response Center (MSRC)

### **Hands-On Security Training**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Full hands-on workshop for securing MCP servers inside Azure with camps from Base Camp to Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Architecture and how to implement guide for all OWASP MCP Top 10 risks

---

## Wetin Next

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
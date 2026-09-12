# MCP Security: Complete Protection for AI Systems

[![MCP Security Best Practices](../../../translated_images/pcm/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Click di image wey dey up to watch video for dis lesson)_

Security na very important tin for AI system design, dat na why we put am as our second section. Dis one dey match with Microsoft own **Secure by Design** principle from di [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Di Model Context Protocol (MCP) dey bring strong new powers come AI-driven applications but e self still dey bring new security wahala wey pass normal software gbege. MCP systems dey face both old security gbege (secure coding, least privilege, supply chain security) plus new AI gbege like prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough vulnerabilities, and dynamic capability modification.

Dis lesson go show di most serious security risks for MCP wey dem implement—covering authentication, authorization, too much permissions, indirect prompt injection, session security, confused deputy problems, token management, and supply chain wahala dem. You go learn how to control dem well with better ways, plus use Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to make your MCP deployment strong.

## Learning Objectives

By di time you finish dis lesson, you go fit:

- **Know MCP-Specific Wahala**: Recognize unique security gbege wey dey MCP systems like prompt injection, tool poisoning, too much permissions, session hijacking, confused deputy problems, token passthrough wahala, and supply chain risks
- **Apply Security Controls**: Use strong mitigations like correct authentication, least privilege access, secure token management, session security controls, and supply chain check
- **Use Microsoft Security Solutions**: Understand and set up Microsoft Prompt Shields, Azure Content Safety, and GitHub Advanced Security for MCP workload protection
- **Check Tool Security**: Know as e important to confirm tool metadata, dey watch for dynamic changes, and protect against indirect prompt injection attacks
- **Join Best Practices Together**: Use established security basics (secure coding, server hardening, zero trust) with MCP-specific controls to give better protection

# MCP Security Architecture & Controls

New MCP implementations need security wey dey layered well for both normal software security and AI-specific wahala dem. Di fast-changing MCP specs dey continue to improve their security controls, so dem fit better add to enterprise security architectures and common best practices.

Research from di [Microsoft Digital Defense Report](https://aka.ms/mddr) show sey **98% of reported breaches for fit stop if dem get strong security hygiene**. Di best protection plan na to join basic security ways with MCP-specific controls—old school security measures still be di best way to reduce security risk well well.

## Current Security Landscape

> **Note:** Dis chapter mix established MCP security rules with di
> current **MCP Specification 2026-07-28** authorization guidance. Always check
> di current [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repository](https://github.com/modelcontextprotocol), and
> [security best practices documentation](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> wen you dey do security-sensitive coding.

> **Authorization update:** MCP `2026-07-28` require clients to check
> di `iss` parameter for authorization responses (RFC 9207) and link registered
> credentials to di issuing authorization server. Dynamic Client Registration
> don stop; new ones suppose use Client ID Metadata Documents.
> See [Wetin Don Change for MCP: The 2026-07-28 Specification](../01-CoreConcepts/mcp-2026-07-28.md)
> for full list of authorization changes.

## 🏔️ MCP Security Summit Workshop (Sherpa)

For **hands-on security training**, we strong recommend di **MCP Security Summit Workshop** (Sherpa) - na full guided journey to secure MCP servers for Microsoft Azure.

### Workshop Overview

Di [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) dey give practical, correct security training using di proven "vulnerable → exploit → fix → validate" way. You go:

- **Learn by Breaking Things**: Experience vulnerabilities by hacking insecure servers
- **Use Azure-Native Security**: Use Azure Entra ID, Key Vault, API Management, and AI Content Safety
- **Follow Defense-in-Depth**: Move through camps to build strong security layers
- **Apply OWASP Standards**: Every technique follow [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Get Production Code**: Take tested and working implementations

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

Di [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) talk di ten most important security risks for MCP implementations:

| Risk | Description | Azure Mitigation |
|------|-------------|------------------|
| **MCP01** | Token Mismanagement & Secret Exposure | Azure Key Vault, Managed Identity |
| **MCP02** | Privilege Escalation via Scope Creep | RBAC, Conditional Access |
| **MCP03** | Tool Poisoning | Tool validation, integrity verification |
| **MCP04** | Software Supply Chain Attacks & Dependency Tampering | GitHub Advanced Security, dependency scanning |
| **MCP05** | Command Injection & Execution | Input validation, sandboxing |
| **MCP06** | Intent Flow Subversion | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Insufficient Authentication & Authorization | Azure Entra ID, OAuth 2.1 with PKCE |
| **MCP08** | No Audit and Telemetry | Azure Monitor, Application Insights |
| **MCP09** | Shadow MCP Servers | API Center governance, network isolation |
| **MCP10** | Context Injection & Over-Sharing | Data classification, minimal exposure |

### How MCP Authentication Don Change

Di MCP specification don change well well about how dem dey do authentication and authorization:

- **Original Way**: Early specs dey make developers to do custom authentication servers, with MCP servers as OAuth 2.0 Authorization Servers wey dey manage user authentication directly
- **Current Standard (`2026-07-28`)**: MCP servers fit pass authentication to external identity providers like Microsoft Entra ID. Clients suppose still apply current issuer-validation and credential-binding rules.
 

- **Transport Layer Security**: Better support for secure transport with correct authentication patterns for both local (STDIO) and remote (Streamable HTTP) connection

## Authentication & Authorization Security

### Security Wahala We Dem Get Now

Modern MCP implementations dey face plenti authentication and authorization gbege:

### Risks & Wahala Dem Fit Cause

- **Authorization Logic Wahala**: Bad authorization logic for MCP servers fit make sensitive data open and wrong access control
- **OAuth Token Compromise**: Local MCP server token thief fit make attacker fake server and enter downstream services
- **Token Passthrough Wahala**: Bad token handling go make security controls bypass and accountability gaps
- **Too Much Permissions**: MCP servers wey get more permission pass wetin dem suppose get dey break least privilege and increase attack area

#### Token Passthrough: Serious Wrong Way

**Token passthrough no allowed** for current MCP authorization because e get serious security problem:

##### How E Dey Break Security Control
- MCP servers and downstream APIs dey use critical security controls (rate limiting, request validation, traffic monitoring) wey need correct token check
- Direct client-to-API token use go pass these protections, spoil security structure

##### Accountability & Audit Wahala  
- MCP servers no fit tell difference between clients using upstream-issued tokens, so audit fit break
- Downstream server logs go show fake request origin no be real MCP servers
- Investigating gbege and compliance auditing go hard well well

##### Data Hacks Risks
- Bad token claims let bad people with stolen token use MCP servers as proxy to take data
- Trust break make unauthorized access ways bypass security controls

##### Multiple-Service Attack Wahala
- Stolen tokens for several services fit allow lateral movement across connected systems
- Trust issues fit show when token sources no fit confirm

### Security Controls & How To Fix Dem

**Important Security Rules:**

> **MANDATORY:** MCP servers **NO GO ACCEPT** any tokens wey dem no explicitly issue for MCP server itself

#### Authentication & Authorization Controls

- **Correct Authorization Review**: Check MCP server authorization logic fully to make sure only correct users and clients fit enter sensitive resources
  - **How To Implement**: [Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identity Join**: [Use Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Use [Microsoft token check and lifecycle best ways](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Check token audience claims match MCP server identity
  - Use correct token rotation and expiration rules
  - Stop token replay attack and unauthorized use

- **Safe Token Storage**: Keep token safe with encryption for storage and during transfer
  - **Best Ways**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Access Control Setup

- **Least Privilege Principle**: Give MCP servers only times minimum permission wey dem need for work
  - Check and update permissions regularly to stop privilege creep
  - **Microsoft Docs**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Use fine-grained role assignment
  - Keep roles tight to specific resources and actions
  - Avoid big or unnecessary permissions wey dey give attackers chance

- **Continuous Permission Monitoring**: Always audit and monitor access
  - Watch how permissions dey used for any strange behavior
  - Quickly fix or remove too much or unused permissions

## AI-Specific Security Wahala Dem

### Prompt Injection & Tool Manipulation Attack Dem

New MCP implement dey face complex AI-specific attack ways wey old security ways no fit fully solve:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

**Indirect Prompt Injection** na one of di worst vulnerability for MCP-enabled AI systems. Attackers dey put bad command inside external content like documents, web pages, emails, or data sources, wey di AI systems later process like correct commands.

**Attack Example Dem:**
- **Document Injection**: Bad command hide for documents wey AI process wey make AI do bad tins
- **Web Content Exploitation**: Bad web pages wey get hidden prompts wey fit control AI when dem scrape am
- **Email Attacks**: Bad prompts inside emails wey fit make AI answer things or do unauthorized tins
- **Data Source Contamination**: Bad database or APIs wey serve dirty content to AI systems

**Real-World Effect**: Dis kind attack fit cause data theft, privacy breach, create bad content, and change user interaction. For full analysis, check [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/pcm/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning Attacks**

**Tool Poisoning** dey target di metadata wey describe MCP tools, dey use how LLMs dey read tool descriptions and parameters to decide how to operate.

**Attack Ways:**
- **Metadata Manipulation**: Attackers dey put bad instructions inside tool descriptions, parameters, or usage examples
- **Invisible Instructions**: Hidden prompts inside tool metadata wey AI models process but humans no see
- **Dynamic Tool Change ("Rug Pulls")**: Tools wey users approve fit later change to do bad things without user sabi
- **Parameter Injection**: Bad content hide inside tool parameter schemas wey fit affect model behavior


**Hosted Server Risks**: Remote MCP servers get big risk as tool definitions fit update after user don approve am first, e fit make safe tools wey dey before, turn to bad ones. For full analysis, check [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/pcm/tool-injection.3b0b4a6b24de6bef.webp)

#### **Additional AI Attack Vectors**

- **Cross-Domain Prompt Injection (XPIA)**: Sharp attacks wey dey use content from different domains to waka pass security controls
- **Dynamic Capability Modification**: Real-time change for tool ability wey fit pass initial security check
- **Context Window Poisoning**: Attacks wey dey change big context windows to hide bad instructions
- **Model Confusion Attacks**: Use model limit to cause wahala or unsafe behavior


### AI Security Risk Impact

**High-Impact Consequences:**
- **Data Exfiltration**: Access and chop sensitive company or personal data without permission
- **Privacy Breaches**: Make personal info (PII) and secret company data show
- **System Manipulation**: Change critical system and workflow damage
- **Credential Theft**: Steal authentication tokens and service credentials
- **Lateral Movement**: Use hacked AI systems as base for bigger network attacks

### Microsoft AI Security Solutions

#### **AI Prompt Shields: Advanced Protection Against Injection Attacks**

Microsoft **AI Prompt Shields** dey give full defense against direct and indirect prompt injection attacks with many security layers:

##### **Core Protection Mechanisms:**

1. **Advanced Detection & Filtering**
   - Machine learning algorithms and NLP ways dey detect bad instructions for external content
   - Real-time check for documents, web pages, emails, and data sources to find hidden threat
   - Understand if prompt na legit or bad pattern 

2. **Spotlighting Techniques**  
   - Fit separate trusted system instructions and possibly hacked external inputs
   - Text change methods wey make model get better relevance but still separate bad content
   - Help AI systems keep proper instruction order and ignore injected commands

3. **Delimiter & Datamarking Systems**
   - Clear boundary between trusted system messages and outside input text
   - Special markers dey show boundaries between trusted and non-trusted data sources
   - Clear separation prevent instruction confusion and stop unauthorised command run

4. **Continuous Threat Intelligence**
   - Microsoft dey always watch new attack style and dey update defense
   - Proactive threat search for new injection methods and attack ways
   - Regular security model update to still dey strong against new threat

5. **Azure Content Safety Integration**
   - Part of full Azure AI Content Safety suite
   - Extra check for jailbreak attempts, bad content, and security rule break
   - One kind security control for AI app components

**Implementation Resources**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/pcm/prompt-shield.ff5b95be76e9c78c.webp)


## Advanced MCP Security Threats

### Session Hijacking Vulnerabilities

**Session hijacking** na critical attack way for stateful MCP systems wey unauthorized people fit grab and use real session IDs to be like client and do bad things.

#### **Attack Scenarios & Risks**

- **Session Hijack Prompt Injection**: Attackers wey get stolen session IDs fit put bad event for servers wey share session, fit cause bad actions or get secret data
- **Direct Impersonation**: Stolen session IDs fit make direct MCP server call without authentication, treat attacker as real user
- **Compromised Resumable Streams**: Attackers fit stop requests quick, make real clients resume with bad content

#### **Security Controls for Session Management**

**Critical Requirements:**
- **Authorization Verification**: MCP servers wey get authorization **MUST** check all incoming requests and **MUST NOT** depend on sessions for authentication
- **Secure Session Generation**: Use cryptographically secure, non-deterministic session IDs wey come from secure random number generators
- **User-Specific Binding**: Bind session IDs to user info with format like `<user_id>:<session_id>` to stop session abuse across users
- **Session Lifecycle Management**: Proper expire, rotate, and cancel session to reduce risk window
- **Transport Security**: Always HTTPS for all communication to stop session ID interception

### Confused Deputy Problem

The **confused deputy problem** happen when MCP servers act as authentication proxy between clients and third-party services, create chance for authorization bypass using fixed client ID abuse.

#### **Attack Mechanics & Risks**

- **Cookie-based Consent Bypass**: Previous user authentication create consent cookies wey attackers fit use through bad authorization requests with fake redirect URIs
- **Authorization Code Theft**: The cookies fit make authorization servers skip consent screen, redirect codes to attacker endpoint  
- **Unauthorized API Access**: Stolen authorization codes allow token exchange and user impersonation without permission

#### **Mitigation Strategies**

**Mandatory Controls:**
- **Explicit Consent Requirements**: MCP proxy servers with static client IDs **MUST** get user consent for each dynamic client registration
- **OAuth 2.1 Security Implementation**: Follow latest OAuth security best practice including PKCE (Proof Key for Code Exchange) for all authorization requests
- **Strict Client Validation**: Strong validation for redirect URIs and client IDs to stop abuse

### Token Passthrough Vulnerabilities  

**Token passthrough** na bad practice where MCP servers accept client tokens without check and send dem to downstream APIs, break MCP authorization rules.

#### **Security Implications**

- **Control Circumvention**: Direct client to API token use skip important rate limiting, validation, and monitoring control
- **Audit Trail Corruption**: Upstream tokens dey hide client identity, make investigation hard
- **Proxy-based Data Exfiltration**: Bad tokens allow attackers use servers as proxy to access data without permission
- **Trust Boundary Violations**: Downstream services no fit trust token origin when token no verify well
- **Multi-service Attack Expansion**: Bad tokens accepted across service to move attack side

#### **Required Security Controls**

**Non-negotiable Requirements:**
- **Token Validation**: MCP servers **MUST NOT** accept tokens wey no explicitly issue for MCP server
- **Audience Verification**: Always validate token audience claim to match MCP server identity
- **Proper Token Lifecycle**: Use short-lived access tokens with secure rotation practice


## Supply Chain Security for AI Systems

Supply chain security don pass old software dependencies to cover full AI ecosystem. Modern MCP must strictly check and monitor all AI parts, because each fit cause system risk.

### Expanded AI Supply Chain Components

**Traditional Software Dependencies:**
- Open-source libraries and frameworks
- Container images and base systems  
- Development tools and build pipelines
- Infrastructure parts and services

**AI-Specific Supply Chain Elements:**
- **Foundation Models**: Pre-trained models from different providers need origin check
- **Embedding Services**: External vectorization and semantic search services
- **Context Providers**: Data sources, knowledge bases, and document repos  
- **Third-party APIs**: External AI services, ML pipelines, and data processing endpoints
- **Model Artifacts**: Weights, settings, and fine-tuned model versions
- **Training Data Sources**: Datasets use for model train and fine-tune

### Comprehensive Supply Chain Security Strategy

#### **Component Verification & Trust**
- **Provenance Validation**: Check origin, licensing, and correctness of all AI parts before use
- **Security Assessment**: Do vulnerability scan and security review for models, data, and AI services
- **Reputation Analysis**: Judge security record and practice of AI service providers
- **Compliance Verification**: Make sure all parts meet company security and law requirement

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Put security scan for all automated deploy pipelines
- **Artifact Integrity**: Use crypto check for all deployed code, models, config
- **Staged Deployment**: Use step by step deploy style with security check each stage
- **Trusted Artifact Repositories**: Deploy only from verified, secure artifact registrar and repo

#### **Continuous Monitoring & Response**
- **Dependency Scanning**: Ongoing vulnerability watch for software and AI parts
- **Model Monitoring**: Constant check of model behavior, performance now and later, and security bugs
- **Service Health Tracking**: Watch external AI services for uptime, security incidents, and policy change
- **Threat Intelligence Integration**: Add threat info feeds special for AI and ML security risk

#### **Access Control & Least Privilege**
- **Component-level Permissions**: Restrict access to models, data, and services based on business need
- **Service Account Management**: Use special service accounts with small needed permissions
- **Network Segmentation**: Separate AI parts and limit network between services
- **API Gateway Controls**: Use one central API gateway to control and watch access to outside AI services

#### **Incident Response & Recovery**
- **Rapid Response Procedures**: Established way to patch or replace hacked AI parts
- **Credential Rotation**: Automatic system to rotate secrets, API keys, and service credentials
- **Rollback Capabilities**: Ability to quickly go back to previous safe AI parts version
- **Supply Chain Breach Recovery**: Special way to handle upstream AI service hack

### Microsoft Security Tools & Integration

**GitHub Advanced Security** get full supply chain protection including:
- **Secret Scanning**: Auto find credentials, API keys, and tokens inside repos
- **Dependency Scanning**: Vulnerability check for open-source dependencies and libraries
- **CodeQL Analysis**: Static code analysis for security holes and coding problems
- **Supply Chain Insights**: See dependency health and security status

**Azure DevOps & Azure Repos Integration:**
- Smooth security scan integration across Microsoft dev platforms
- Auto security check for AI workloads in Azure Pipelines
- Policy push for secure AI part deploy

**Microsoft Internal Practices:**
Microsoft dey do big supply chain security for all products. Learn their way for [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Best Practices

MCP setups inherit and add to your organization's existing security style. Make strong foundation security go well, e go make AI systems and MCP deployments better secure.

### Core Security Fundamentals

#### **Secure Development Practices**
- **OWASP Compliance**: Protect against [OWASP Top 10](https://owasp.org/www-project-top-ten/) web application vulnerabilities
- **AI-Specific Protections**: Put controls for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Secure Secrets Management**: Use special vaults for tokens, API keys, and secret config data
- **End-to-End Encryption**: Use secure communication for all app parts and data flow
- **Input Validation**: Strict check for all user inputs, API params, and data sources

#### **Infrastructure Hardening**
- **Multi-Factor Authentication**: Mandatory MFA for all admin and service accounts
- **Patch Management**: Auto and timely patch for OS, frameworks, and dependencies  
- **Identity Provider Integration**: Centralize identity management through enterprise providers (Microsoft Entra ID, Active Directory)
- **Network Segmentation**: Logical segregation of MCP parts to reduce lateral move chance
- **Principle of Least Privilege**: Give minimum required permission for all system parts and accounts

#### **Security Monitoring & Detection**
- **Comprehensive Logging**: Detailed log of AI app actions, including MCP client-server talks
- **SIEM Integration**: Central security info and event management for unusual activity detection
- **Behavioral Analytics**: AI-powered watch to find strange system and user patterns
- **Threat Intelligence**: Add external threat feeds and indicators of compromise (IOCs)
- **Incident Response**: Clear processes for security incident find, respond, and recover

#### **Zero Trust Architecture**
- **Never Trust, Always Verify**: Always check users, devices, and network connections
- **Micro-Segmentation**: Detailed network control to separate workloads and services
- **Identity-Centric Security**: Security rules based on verified identity not network place
- **Continuous Risk Assessment**: Dynamic security check based on current context and behavior
- **Conditional Access**: Access control wey change based on risk, location, and device trust

### Enterprise Integration Patterns

#### **Microsoft Security Ecosystem Integration**
- **Microsoft Defender for Cloud**: Full cloud security posture management
- **Azure Sentinel**: Cloud-native SIEM and SOAR for AI workload protection
- **Microsoft Entra ID**: Enterprise identity and access management with conditional access rules
- **Azure Key Vault**: Central secret management with hardware security module (HSM) support
- **Microsoft Purview**: Data governance and compliance for AI data and workflows

#### **Compliance & Governance**
- **Regulatory Alignment**: Make sure MCP setups meet industry compliance rules (GDPR, HIPAA, SOC 2)

- **Data Classification**: Proper categorization and handling of sensitive data wey AI systems dey process
- **Audit Trails**: Complete logging for regulatory compliance and forensic investigation
- **Privacy Controls**: Implementation of privacy-by-design principles inside AI system architecture
- **Change Management**: Formal processes for security reviews of AI system modifications

These important practices dey build strong security base wey go improve the effectiveness of MCP-specific security controls and dey give full protection for AI-driven applications.

## Key Security Takeaways

- **Layered Security Approach**: Combine foundational security practices (secure coding, least privilege, supply chain verification, continuous monitoring) with AI-specific controls for full protection

- **AI-Specific Threat Landscape**: MCP systems dey face special risks like prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, and too much permissions wey require special protections

- **Authentication & Authorization Excellence**: Implement strong authentication using external identity providers (Microsoft Entra ID), enforce correct token validation, and no ever accept tokens wey no explicitly issue for your MCP server

- **AI Attack Prevention**: Use Microsoft Prompt Shields and Azure Content Safety to protect against indirect prompt injection and tool poisoning attacks, while validating tool metadata and watching for dynamic changes

- **Session & Transport Security**: Use cryptographically secure, non-deterministic session IDs wey tie to user identities, do proper session lifecycle management, and no ever use sessions for authentication

- **OAuth Security Best Practices**: Stop confused deputy attacks through clear user consent for dynamically registered clients, proper OAuth 2.1 implementation with PKCE, and strict redirect URI validation  

- **Token Security Principles**: Avoid token passthrough anti-patterns, validate token audience claims, do short-lived tokens wey rotate securely, and keep clear trust boundaries

- **Comprehensive Supply Chain Security**: Treat all AI ecosystem components (models, embeddings, context providers, external APIs) with the same security care as traditional software dependencies

- **Continuous Evolution**: Keep up with rapidly changing MCP specifications, contribute to security community standards, and maintain adaptive security posture as the protocol develops

- **Microsoft Security Integration**: Use Microsoft's complete security ecosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for stronger MCP deployment protection

## Complete Resources

### **Official MCP Security Documentation**
- [MCP Specification (Current: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **OWASP MCP Security Resources**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Complete OWASP MCP Top 10 with Azure implementation advice
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

- **[CIMD and DCR Authorization Sample](./samples/cimd-dcr-auth/README.md)** - Runnable TypeScript MCP `2026-07-28` resource server wey compare preferred Client ID Metadata Documents with outdated Dynamic Client Registration fallback
- **[MCP Security Best Practices](./mcp-security-best-practices.md)** - Complete security best practices for MCP implementations
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Practical implementation examples for Azure Content Safety integration  
- **[MCP Security Controls](./mcp-security-controls.md)** - Latest security controls and techniques for MCP deployments
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Quick reference guide for important MCP security practices
- **[BlueHat 2026: Securing the future of AI: Securing MCP with defense in depth patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Defense-in-depth patterns from the Microsoft Security Response Center (MSRC)

### **Hands-On Security Training**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Complete hands-on workshop for securing MCP servers in Azure with step-by-step camps from Base Camp to Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Reference architecture and implementation guidance for all OWASP MCP Top 10 risks

---

## Wetin Follow Next

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
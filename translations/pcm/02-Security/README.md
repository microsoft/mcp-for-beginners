<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c767a35642f753127dc08545c25a290",
  "translation_date": "2025-11-18T19:24:35+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "pcm"
}
-->
# MCP Security: Beta Protection for AI Systems

[![MCP Security Best Practices](../../../translated_images/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.pcm.png)](https://youtu.be/88No8pw706o)

_(Click di image wey dey up to watch di video for dis lesson)_

Security na di main thing for AI system design, na why we dey put am as di second section. E dey follow Microsoft **Secure by Design** principle wey dey from di [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Di Model Context Protocol (MCP) dey bring strong new power to AI-driven apps but e dey also carry new security wahala wey pass di normal software risks. MCP systems dey face di regular security wahala (secure coding, least privilege, supply chain security) plus new AI-specific threats like prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough wahala, and dynamic capability modification.

Dis lesson go show di main security risks wey dey MCP implementations—like authentication, authorization, excessive permissions, indirect prompt injection, session security, confused deputy wahala, token management, and supply chain wahala. You go sabi di controls and best practices wey go help reduce dis risks plus how to use Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to make your MCP deployment strong.

## Wetin You Go Learn

By di end of dis lesson, you go fit:

- **Know MCP-Specific Threats**: Sabi di special security wahala wey dey MCP systems like prompt injection, tool poisoning, excessive permissions, session hijacking, confused deputy wahala, token passthrough wahala, and supply chain risks
- **Use Security Controls**: Fit use di right ways to stop di wahala like strong authentication, least privilege access, secure token management, session security controls, and supply chain verification
- **Use Microsoft Security Solutions**: Understand and use Microsoft Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP workloads
- **Check Tool Security**: Sabi why e dey important to check tool metadata, dey monitor for changes, and stop indirect prompt injection attacks
- **Follow Best Practices**: Mix di regular security basics (secure coding, server hardening, zero trust) with MCP-specific controls for beta protection

# MCP Security Architecture & Controls

Di way we dey do MCP now need layered security wey go cover di regular software security plus di AI-specific wahala. Di MCP specification dey grow well well for security controls, e dey make am easy to join enterprise security architectures and di regular best practices.

Research wey Microsoft do for di [Microsoft Digital Defense Report](https://aka.ms/mddr) show say **98% of di breaches wey dem report fit no happen if people dey follow beta security hygiene**. Di best way to protect na to join di regular security practices with MCP-specific controls—di regular security measures still dey di best way to reduce security wahala.

## Di Security Situation Now

> **Note:** Dis info na MCP security standards as e be for **August 18, 2025**. Di MCP protocol dey change fast, and di future versions fit bring new authentication ways and beta controls. Always check di current [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol), and [security best practices documentation](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) for di latest info.

### How MCP Authentication Don Change

Di MCP specification don change well well for di way e dey do authentication and authorization:

- **Di Old Way**: Di first specifications dey make developers create their own authentication servers, MCP servers dey act as OAuth 2.0 Authorization Servers wey dey manage user authentication directly
- **Di New Standard (2025-06-18)**: Di updated specification dey allow MCP servers to use external identity providers (like Microsoft Entra ID), e dey make security beta and e dey reduce di wahala for implementation
- **Transport Layer Security**: E don beta di support for secure transport ways with correct authentication patterns for both local (STDIO) and remote (Streamable HTTP) connections

## Authentication & Authorization Security

### Di Wahala We Dey Face Now

Di MCP implementations wey we dey do now dey face plenty authentication and authorization wahala:

### Risks & Threats

- **Authorization Logic Wey No Set Well**: If di authorization for MCP servers no dey correct, e fit expose sensitive data and no go apply access controls well
- **OAuth Token Wahala**: If local MCP server token dey thief, attackers fit use am to pretend say dem be di server and access other services
- **Token Passthrough Wahala**: If token no dey handle well, e fit make attackers bypass security controls and create accountability wahala
- **Excessive Permissions**: If MCP servers get too much power, e dey break di least privilege principle and e dey make attack surface big

#### Token Passthrough: Di Big Wahala

**Token passthrough no dey allowed** for di current MCP authorization specification because e get big security wahala:

##### How E Dey Spoil Security Controls
- MCP servers and di APIs wey dey follow dem dey use important security controls (like rate limiting, request validation, traffic monitoring) wey need correct token validation
- If client dey use token directly with API, e dey spoil di security setup

##### Accountability Wahala  
- MCP servers no fit sabi di difference between clients wey dey use token wey dem no issue, e dey spoil audit trails
- Di logs for di resource server go dey show wrong request origins instead of di MCP server wey dey act as intermediary
- E go hard to investigate incidents and do compliance auditing

##### Data Theft Risks
- If token claims no dey validate, attackers wey thief token fit use MCP servers as proxy to thief data
- E dey break di trust boundary and allow unauthorized access

##### Multi-Service Attack Wahala
- If token wey dem thief dey work for many services, attackers fit move from one system to another
- Di trust wey dey between services fit spoil if token origin no dey verify

### Security Controls & How to Stop Di Wahala

**Di Important Security Rules:**

> **MANDATORY**: MCP servers **MUST NOT** accept any token wey dem no issue for di MCP server

#### Authentication & Authorization Controls

- **Check Authorization Well Well**: Make sure say di authorization logic for MCP server dey correct so only di right people and clients fit access sensitive resources
  - **Guide for Implementation**: [Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identity Integration**: [Using Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Manage Token Well**: Use [Microsoft's token validation and lifecycle best practices](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Make sure token audience claims match MCP server identity
  - Use correct token rotation and expiration rules
  - Stop token replay attacks and unauthorized use

- **Keep Token Safe**: Store token well with encryption for both rest and transit
  - **Best Practices**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Access Control Setup

- **Least Privilege Principle**: Give MCP servers only di permissions wey dem need to work
  - Dey check permissions regularly and update am to stop privilege creep
  - **Microsoft Documentation**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Use roles wey dey specific to di resources and actions
  - Make roles tight to di resources wey dem need
  - No give broad permissions wey go make attack surface big

- **Dey Monitor Permissions**: Dey check access and monitor am regularly
  - Look for strange permission usage patterns
  - Quickly fix permissions wey no dey use or wey dey too much

## AI-Specific Security Wahala

### Prompt Injection & Tool Manipulation Attacks

Di MCP implementations wey we dey do now dey face strong AI-specific attack ways wey di regular security measures no fit stop finish:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

**Indirect Prompt Injection** na one of di big wahala for MCP-enabled AI systems. Attackers dey hide bad instructions inside external content—documents, web pages, emails, or data sources—wey AI systems go process as correct commands.

**Attack Scenarios:**
- **Document Injection**: Bad instructions dey hide inside documents wey AI dey process
- **Web Content Wahala**: Web pages wey attackers don spoil dey carry instructions wey go change AI behavior
- **Email Attacks**: Bad prompts dey inside emails wey go make AI assistants leak info or do bad actions
- **Data Source Wahala**: Databases or APIs wey attackers don spoil dey send bad content to AI systems

**Real-World Wahala**: Dis attacks fit make data dey thief, privacy dey spoil, bad content dey generate, and user interactions dey manipulate. For beta analysis, check [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.pcm.png)

#### **Tool Poisoning Attacks**

**Tool Poisoning** dey target di metadata wey dey define MCP tools, e dey use di way LLMs dey understand tool descriptions and parameters to make execution decisions.

**Attack Ways:**
- **Metadata Wahala**: Attackers dey put bad instructions inside tool descriptions, parameter definitions, or usage examples
- **Hidden Instructions**: Bad prompts dey hide inside tool metadata wey AI models go process but humans no go see
- **Dynamic Tool Change ("Rug Pulls")**: Tools wey users don approve go later change to do bad actions without di user sabi
- **Parameter Injection**: Bad content dey hide inside tool parameter schemas wey dey affect model behavior

**Hosted Server Wahala**: Remote MCP servers dey get higher risks because tool definitions fit change after users don approve dem, e dey create wahala wey safe tools fit turn bad. For beta analysis, check [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.pcm.png)

#### **Other AI Attack Ways**

- **Cross-Domain Prompt Injection (XPIA)**: Strong attacks wey dey use content from different domains to pass security controls
- **Dynamic Capability Change**: Real-time changes to tool power wey fit escape di first security checks
- **Context Window Wahala**: Attacks wey dey manipulate big context windows to hide bad instructions
- **Model Confusion Attacks**: Attackers dey use model limitations to create unsafe behaviors

### AI Security Risk Wahala

**Big Wahala We Fit Face:**
- **Data Theft**: Unauthorized access and stealing of sensitive enterprise or personal data
- **Privacy Wahala**: Exposure of personal info (PII) and confidential business data  
- **System Manipulation**: Changes wey no dey plan for important systems and workflows
- **Credential Theft**: Attackers dey thief authentication tokens and service credentials
- **Lateral Movement**: Attackers dey use AI systems wey dem don spoil to attack other systems

### Microsoft AI Security Solutions

#### **AI Prompt Shields: Beta Protection Against Injection Attacks**

Microsoft **AI Prompt Shields** dey give strong defense against both direct and indirect prompt injection attacks with plenty security layers:

##### **Di Main Protection Ways:**

1. **Beta Detection & Filtering**
   - Machine learning algorithms and NLP dey detect bad instructions for external content
   - Real-time check for documents, web pages, emails, and data sources for hidden threats
   - E dey understand di difference between correct and bad prompt patterns

2. **Spotlighting Techniques**  
   - E dey separate trusted system instructions from external inputs wey fit dey bad
   - Text transformation wey dey make model understand beta while e dey isolate bad content
   - E dey help AI systems follow correct instruction hierarchy and ignore bad commands

3. **Delimiter & Datamarking Systems**
   - E dey define clear boundary between trusted system messages and external input text
   - Special markers dey show di difference between trusted and untrusted data sources
   - E dey stop instruction confusion and unauthorized command execution

4. **Continuous Threat Intelligence**
   - Microsoft dey monitor new attack ways and dey update di defenses
   - E dey find new injection techniques and attack ways early
   - Regular security model updates dey keep di defenses strong

5. **Azure Content Safety Integration**
   - E dey part of di full Azure AI Content Safety suite
   - E dey detect jailbreak attempts, bad content, and security policy wahala
   - Unified security controls dey cover all AI app parts

**Resources for Implementation**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.pcm.png)


## Advanced MCP Security Wahala

### Session Hijacking Wahala

**Session hijacking** na big attack way for MCP implementations wey dey use stateful systems, attackers dey get and use correct session IDs to pretend say dem be di client and do bad actions.

#### **Attack Scenarios & Risks**

- **Session Hijack Prompt Injection**: Attackers wey get stolen session IDs dey put bad events inside servers wey dey share session state, e fit trigger bad actions or access sensitive data
- **Direct Impersonation**: Stolen session IDs dey allow attackers to call MCP servers directly without authentication, e go make dem look like correct users
- **Compromised Resumable Streams**: Attackers fit stop requests early, e go make correct clients continue with bad content

#### **Security Controls for Session Management**

**Di Important Rules:**
- **Authorization Verification**: MCP server wey dey do authorization **MUST** check ALL request wey dey come in and **MUST NOT** use session for authentication.
- **Secure Session Generation**: Make sure say you dey use session ID wey dey cryptographically secure, wey no dey predictable, and wey dey generated with secure random number generator.
- **User-Specific Binding**: Tie session ID to user-specific info like `<user_id>:<session_id>` so dat e go stop session abuse between users.
- **Session Lifecycle Management**: Make sure say you dey expire, rotate, and invalidate session well to reduce vulnerability window.
- **Transport Security**: Na compulsory to use HTTPS for all communication so dat session ID no go fit dey intercepted.

### Confused Deputy Problem

Dis **confused deputy problem** dey happen when MCP server dey act like authentication proxy between client and third-party service, wey fit make authorization bypass possible through static client ID exploitation.

#### **Attack Mechanics & Risks**

- **Cookie-based Consent Bypass**: If user don authenticate before, e go create consent cookie wey attacker fit use for bad authorization request wey get fake redirect URI.
- **Authorization Code Theft**: Consent cookie wey don dey before fit make authorization server skip consent screen, redirecting code go endpoint wey attacker dey control.  
- **Unauthorized API Access**: If authorization code dey stolen, e fit allow token exchange and user impersonation without user approval.

#### **Mitigation Strategies**

**Mandatory Controls:**
- **Explicit Consent Requirements**: MCP proxy server wey dey use static client ID **MUST** collect user consent for every client wey dem register dynamically.
- **OAuth 2.1 Security Implementation**: Follow OAuth security best practice like PKCE (Proof Key for Code Exchange) for all authorization request.
- **Strict Client Validation**: Make sure say you dey validate redirect URI and client identifier well so dat exploitation no go happen.

### Token Passthrough Vulnerabilities  

**Token passthrough** na bad practice wey MCP server dey do when dem dey accept client token without proper validation and dey forward am go downstream API, wey dey against MCP authorization rules.

#### **Security Implications**

- **Control Circumvention**: If client dey use token directly for API, e go bypass important control like rate limiting, validation, and monitoring.
- **Audit Trail Corruption**: Token wey dey issued upstream go make client identification hard, wey go scatter investigation process.
- **Proxy-based Data Exfiltration**: If token no dey validated, e go allow bad people use server as proxy to access data wey dem no suppose touch.
- **Trust Boundary Violations**: Downstream service go dey trust token wey dem no suppose trust because dem no fit verify origin.
- **Multi-service Attack Expansion**: If token don compromise, e go dey accepted across different service, wey go allow attacker move around.

#### **Required Security Controls**

**Non-negotiable Requirements:**
- **Token Validation**: MCP server **MUST NOT** accept token wey no dey issued specifically for MCP server.
- **Audience Verification**: Always check say token audience claim match MCP server identity.
- **Proper Token Lifecycle**: Use access token wey no dey last long and dey rotate securely.

## Supply Chain Security for AI Systems

Supply chain security don pass software dependency matter, e don cover AI ecosystem. MCP implementation suppose dey check and monitor all AI-related component well because dem fit bring vulnerability wey go affect system.

### Expanded AI Supply Chain Components

**Traditional Software Dependencies:**
- Open-source library and framework
- Container image and base system  
- Development tool and build pipeline
- Infrastructure component and service

**AI-Specific Supply Chain Elements:**
- **Foundation Models**: Pre-trained model wey dey come from different provider wey need verification.
- **Embedding Services**: External vectorization and semantic search service.
- **Context Providers**: Data source, knowledge base, and document repository.  
- **Third-party APIs**: External AI service, ML pipeline, and data processing endpoint.
- **Model Artifacts**: Weight, configuration, and fine-tuned model variant.
- **Training Data Sources**: Dataset wey dem use for model training and fine-tuning.

### Comprehensive Supply Chain Security Strategy

#### **Component Verification & Trust**
- **Provenance Validation**: Check origin, license, and integrity of all AI component before you use am.
- **Security Assessment**: Scan and review model, data source, and AI service for vulnerability.
- **Reputation Analysis**: Look AI service provider security record and practice.
- **Compliance Verification**: Make sure say all component dey meet organization security and regulatory requirement.

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Add security scanning for automated deployment pipeline.
- **Artifact Integrity**: Use cryptographic verification for all artifact wey you dey deploy (code, model, configuration).
- **Staged Deployment**: Deploy step by step with security validation for each stage.
- **Trusted Artifact Repositories**: Only deploy from verified and secure artifact registry.

#### **Continuous Monitoring & Response**
- **Dependency Scanning**: Dey monitor vulnerability for all software and AI component dependency.
- **Model Monitoring**: Dey check model behavior, performance drift, and security anomaly.
- **Service Health Tracking**: Dey monitor external AI service for availability, security issue, and policy change.
- **Threat Intelligence Integration**: Add threat feed wey dey focus on AI and ML security risk.

#### **Access Control & Least Privilege**
- **Component-level Permissions**: Restrict access to model, data, and service based on wetin dem need.
- **Service Account Management**: Use service account wey get only permission wey dem need.
- **Network Segmentation**: Separate AI component and limit network access between service.
- **API Gateway Controls**: Use centralized API gateway to control and monitor access to external AI service.

#### **Incident Response & Recovery**
- **Rapid Response Procedures**: Get process wey go allow you patch or replace AI component wey don compromise.
- **Credential Rotation**: Use automated system to dey rotate secret, API key, and service credential.
- **Rollback Capabilities**: Fit quickly go back to previous version of AI component wey dey work well.
- **Supply Chain Breach Recovery**: Get process for how you go respond to AI service wey don compromise upstream.

### Microsoft Security Tools & Integration

**GitHub Advanced Security** dey provide supply chain protection like:
- **Secret Scanning**: E dey detect credential, API key, and token for repository automatically.
- **Dependency Scanning**: E dey check open-source dependency and library for vulnerability.
- **CodeQL Analysis**: E dey analyze code for security vulnerability and coding issue.
- **Supply Chain Insights**: E dey give visibility into dependency health and security status.

**Azure DevOps & Azure Repos Integration:**
- E dey integrate security scanning for Microsoft development platform.
- E dey run security check automatically for AI workload in Azure Pipeline.
- E dey enforce policy for secure AI component deployment.

**Microsoft Internal Practices:**
Microsoft dey use strong supply chain security practice for all dem product. You fit learn more for [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Best Practices

MCP implementation dey build on top of your organization security setup. If you strengthen your security foundation, e go make AI system and MCP deployment more secure.

### Core Security Fundamentals

#### **Secure Development Practices**
- **OWASP Compliance**: Protect against [OWASP Top 10](https://owasp.org/www-project-top-ten/) web application vulnerability.
- **AI-Specific Protections**: Add control for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559).
- **Secure Secrets Management**: Use vault for token, API key, and sensitive configuration data.
- **End-to-End Encryption**: Make sure say communication between application component and data flow dey secure.
- **Input Validation**: Dey check user input, API parameter, and data source well.

#### **Infrastructure Hardening**
- **Multi-Factor Authentication**: Make MFA compulsory for all admin and service account.
- **Patch Management**: Dey patch operating system, framework, and dependency on time automatically.  
- **Identity Provider Integration**: Use centralized identity management like Microsoft Entra ID or Active Directory.
- **Network Segmentation**: Separate MCP component logically to stop lateral movement.
- **Principle of Least Privilege**: Give only permission wey system component and account need.

#### **Security Monitoring & Detection**
- **Comprehensive Logging**: Dey log AI application activity well, including MCP client-server interaction.
- **SIEM Integration**: Use centralized security information and event management to detect anomaly.
- **Behavioral Analytics**: Use AI to monitor unusual pattern for system and user behavior.
- **Threat Intelligence**: Add external threat feed and indicator of compromise (IOCs).
- **Incident Response**: Get clear process for how you go detect, respond, and recover from security incident.

#### **Zero Trust Architecture**
- **Never Trust, Always Verify**: Dey verify user, device, and network connection every time.
- **Micro-Segmentation**: Use small network control to separate workload and service.
- **Identity-Centric Security**: Base security policy on verified identity, no be network location.
- **Continuous Risk Assessment**: Dey check security posture based on current context and behavior.
- **Conditional Access**: Dey adjust access control based on risk factor, location, and device trust.

### Enterprise Integration Patterns

#### **Microsoft Security Ecosystem Integration**
- **Microsoft Defender for Cloud**: E dey manage cloud security posture well.
- **Azure Sentinel**: E dey provide cloud-native SIEM and SOAR for AI workload protection.
- **Microsoft Entra ID**: E dey manage enterprise identity and access with conditional access policy.
- **Azure Key Vault**: E dey manage secret centrally with hardware security module (HSM) backing.
- **Microsoft Purview**: E dey handle data governance and compliance for AI data source and workflow.

#### **Compliance & Governance**
- **Regulatory Alignment**: Make sure say MCP implementation dey meet industry compliance requirement (GDPR, HIPAA, SOC 2).
- **Data Classification**: Dey categorize and handle sensitive data wey AI system dey process well.
- **Audit Trails**: Dey log everything well for compliance and investigation.
- **Privacy Controls**: Add privacy-by-design principle for AI system architecture.
- **Change Management**: Dey review AI system modification for security before you go ahead.

Dis foundational practice go give strong security base wey go make MCP-specific security control work better and protect AI application well.

## Key Security Takeaways

- **Layered Security Approach**: Combine foundational security practice (secure coding, least privilege, supply chain verification, continuous monitoring) with AI-specific control to protect well.

- **AI-Specific Threat Landscape**: MCP system dey face unique risk like prompt injection, tool poisoning, session hijacking, confused deputy problem, token passthrough vulnerability, and excessive permission wey need special solution.

- **Authentication & Authorization Excellence**: Use strong authentication with external identity provider (Microsoft Entra ID), enforce token validation well, and no ever accept token wey no dey issued for your MCP server.

- **AI Attack Prevention**: Use Microsoft Prompt Shields and Azure Content Safety to stop indirect prompt injection and tool poisoning attack, dey validate tool metadata, and dey monitor for dynamic change.

- **Session & Transport Security**: Use session ID wey dey cryptographically secure, wey no dey predictable, tie am to user identity, manage session lifecycle well, and no ever use session for authentication.

- **OAuth Security Best Practices**: Stop confused deputy attack by collecting user consent for dynamically registered client, use OAuth 2.1 with PKCE, and validate redirect URI well.  

- **Token Security Principles**: No do token passthrough, validate token audience claim, use short-lived token wey dey rotate securely, and maintain clear trust boundary.

- **Comprehensive Supply Chain Security**: Treat all AI ecosystem component (model, embedding, context provider, external API) with same security level as software dependency.

- **Continuous Evolution**: Dey follow MCP specification wey dey change, contribute to security community standard, and dey adapt security posture as protocol dey mature.

- **Microsoft Security Integration**: Use Microsoft security ecosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) to protect MCP deployment well.

## Comprehensive Resources

### **Official MCP Security Documentation**
- [MCP Specification (Current: 2025-06-18)](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

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

If you wan full security guide, check dis special documents for dis section:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Full security best practices for MCP setup
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Examples wey go show you how to use Azure Content Safety  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - New security controls and techniques for MCP deployment
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Quick guide for MCP security practices wey you need

---

## Wetin Next

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
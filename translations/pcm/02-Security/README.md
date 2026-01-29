# MCP Security: Complete Protection for AI Systems

[![MCP Security Best Practices](../../../translated_images/pcm/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Click di image wey dey above to watch video for dis lesson)_

Security na di foundation for AI system design, na why we put am as our second section. Dis one dey follow Microsoft **Secure by Design** principle from di [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Di Model Context Protocol (MCP) bring strong new powers to AI-driven apps but e still get unique security wahala wey pass normal software risks. MCP systems dey face both normal security palava (secure coding, least privilege, supply chain security) plus new AI-specific gbege like prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough wahala, and dynamic capability modification.

Dis lesson go explore di most important security risks for MCP implementations—cover authentication, authorization, too much permissions, indirect prompt injection, session security, confused deputy problems, token management, and supply chain vulnerabilities. You go learn how to take control and best practices to reduce these risks while you dey use Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to make your MCP deployment strong.

## Learning Objectives

By di time you finish dis lesson, you go fit:

- **Identify MCP-Specific Threats**: Know di unique security risks for MCP systems like prompt injection, tool poisoning, too much permissions, session hijacking, confused deputy problems, token passthrough wahala, and supply chain risks
- **Apply Security Controls**: Use correct mitigations like strong authentication, least privilege access, secure token management, session security controls, and supply chain checking
- **Leverage Microsoft Security Solutions**: Understand and use Microsoft Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP workload
- **Validate Tool Security**: Know why tool metadata validation important, dey watch for dynamic changes, and defend against indirect prompt injection attacks
- **Integrate Best Practices**: Join normal security basics (secure coding, server hardening, zero trust) with MCP-specific controls for full protection

# MCP Security Architecture & Controls

Modern MCP implementations need layered security wey go cover both normal software security and AI-specific threats. Di fast changing MCP specification dey improve its security controls, making am better to join enterprise security architectures and normal best practices.

Research from di [Microsoft Digital Defense Report](https://aka.ms/mddr) show say **98% of reported breaches fit stop if security hygiene strong**. Di best protection strategy na to join basic security practices with MCP-specific controls—di proven baseline security measures still dey most effective to reduce overall security risk.

## Current Security Landscape

> **Note:** Dis info dey reflect MCP security standards as of **December 18, 2025**. Di MCP protocol dey change fast, and future implementations fit bring new authentication patterns and better controls. Always check di current [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol), and [security best practices documentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) for di latest advice.

### Evolution of MCP Authentication

Di MCP specification don change well well for how e dey do authentication and authorization:

- **Original Approach**: Early specs make developers implement custom authentication servers, with MCP servers acting as OAuth 2.0 Authorization Servers wey dey manage user authentication directly
- **Current Standard (2025-11-25)**: Updated spec allow MCP servers to pass authentication to external identity providers (like Microsoft Entra ID), to improve security and reduce implementation wahala
- **Transport Layer Security**: Better support for secure transport with correct authentication patterns for both local (STDIO) and remote (Streamable HTTP) connections

## Authentication & Authorization Security

### Current Security Challenges

Modern MCP implementations dey face some authentication and authorization wahala:

### Risks & Threat Vectors

- **Misconfigured Authorization Logic**: Bad authorization implementation for MCP servers fit expose sensitive data and apply wrong access controls
- **OAuth Token Compromise**: Local MCP server token theft fit make attackers pretend to be servers and access downstream services
- **Token Passthrough Vulnerabilities**: Wrong token handling fit create security control bypass and accountability wahala
- **Excessive Permissions**: MCP servers wey get too much privilege dey break least privilege principles and increase attack surface

#### Token Passthrough: A Critical Anti-Pattern

**Token passthrough no dey allowed at all** for current MCP authorization spec because e get serious security wahala:

##### Security Control Circumvention
- MCP servers and downstream APIs dey do important security controls (rate limiting, request validation, traffic monitoring) wey depend on correct token validation
- Direct client-to-API token use dey bypass these protections, weak the security architecture

##### Accountability & Audit Challenges  
- MCP servers no fit tell difference between clients wey dey use upstream-issued tokens, e break audit trails
- Downstream resource server logs go show wrong request origin instead of real MCP server middlemen
- Incident investigation and compliance auditing go hard well well

##### Data Exfiltration Risks
- Unchecked token claims fit allow bad people with stolen tokens to use MCP servers as proxy to carry data comot
- Trust boundary break fit allow unauthorized access wey bypass security controls

##### Multi-Service Attack Vectors
- Compromised tokens wey multiple services accept fit allow lateral movement across connected systems
- Trust assumptions between services fit break if token origin no fit verify

### Security Controls & Mitigations

**Critical Security Requirements:**

> **MANDATORY**: MCP servers **MUST NOT** accept any tokens wey no explicitly issue for di MCP server

#### Authentication & Authorization Controls

- **Rigorous Authorization Review**: Do full audit of MCP server authorization logic to make sure only correct users and clients fit access sensitive resources
  - **Implementation Guide**: [Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identity Integration**: [Using Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Use [Microsoft's token validation and lifecycle best practices](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Check token audience claims match MCP server identity
  - Use correct token rotation and expiration policies
  - Stop token replay attacks and unauthorized use

- **Protected Token Storage**: Store tokens securely with encryption for both rest and transit
  - **Best Practices**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Access Control Implementation

- **Principle of Least Privilege**: Give MCP servers only minimum permissions wey dem need for correct function
  - Regularly review and update permissions to stop privilege creep
  - **Microsoft Documentation**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Use fine-grained role assignments
  - Scope roles tight to specific resources and actions
  - Avoid broad or unnecessary permissions wey fit increase attack surface

- **Continuous Permission Monitoring**: Do ongoing access audit and monitoring
  - Watch permission usage for strange patterns
  - Quickly fix too much or unused privileges

## AI-Specific Security Threats

### Prompt Injection & Tool Manipulation Attacks

Modern MCP implementations dey face advanced AI-specific attack ways wey normal security measures no fit fully handle:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

**Indirect Prompt Injection** na one of di most serious vulnerabilities for MCP-enabled AI systems. Attackers dey hide bad instructions inside external content—documents, web pages, emails, or data sources—wey AI systems later process as correct commands.

**Attack Scenarios:**
- **Document-based Injection**: Bad instructions hidden inside processed documents wey fit trigger wrong AI actions
- **Web Content Exploitation**: Compromised web pages wey get embedded prompts wey fit control AI behavior when dem scrape am
- **Email-based Attacks**: Bad prompts inside emails wey fit make AI assistants leak info or do unauthorized actions
- **Data Source Contamination**: Compromised databases or APIs wey serve bad content to AI systems

**Real-World Impact**: These attacks fit cause data theft, privacy breach, creation of harmful content, and manipulation of user interactions. For detailed analysis, see [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/pcm/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning Attacks**

**Tool Poisoning** dey target di metadata wey define MCP tools, exploiting how LLMs interpret tool descriptions and parameters to decide how to run dem.

**Attack Mechanisms:**
- **Metadata Manipulation**: Attackers dey put bad instructions inside tool descriptions, parameter definitions, or usage examples
- **Invisible Instructions**: Hidden prompts inside tool metadata wey AI models process but humans no fit see
- **Dynamic Tool Modification ("Rug Pulls")**: Tools wey users approve later get changed to do bad actions without user knowledge
- **Parameter Injection**: Bad content inside tool parameter schemas wey fit affect model behavior

**Hosted Server Risks**: Remote MCP servers get higher risk because tool definitions fit change after user approval, making tools wey once safe become bad. For full analysis, see [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/pcm/tool-injection.3b0b4a6b24de6bef.webp)

#### **Additional AI Attack Vectors**

- **Cross-Domain Prompt Injection (XPIA)**: Advanced attacks wey use content from many domains to bypass security controls
- **Dynamic Capability Modification**: Real-time changes to tool powers wey escape initial security checks
- **Context Window Poisoning**: Attacks wey manipulate big context windows to hide bad instructions
- **Model Confusion Attacks**: Exploit model limits to create unpredictable or unsafe behavior


### AI Security Risk Impact

**High-Impact Consequences:**
- **Data Exfiltration**: Unauthorized access and theft of sensitive enterprise or personal data
- **Privacy Breaches**: Exposure of personally identifiable information (PII) and confidential business data  
- **System Manipulation**: Unintended changes to critical systems and workflows
- **Credential Theft**: Compromise of authentication tokens and service credentials
- **Lateral Movement**: Use of compromised AI systems as stepping stones for bigger network attacks

### Microsoft AI Security Solutions

#### **AI Prompt Shields: Advanced Protection Against Injection Attacks**

Microsoft **AI Prompt Shields** provide full defense against both direct and indirect prompt injection attacks through many security layers:

##### **Core Protection Mechanisms:**

1. **Advanced Detection & Filtering**
   - Machine learning algorithms and NLP techniques detect bad instructions inside external content
   - Real-time check of documents, web pages, emails, and data sources for hidden threats
   - Contextual understanding of real vs. bad prompt patterns

2. **Spotlighting Techniques**  
   - Separate trusted system instructions from possibly bad external inputs
   - Text transformation methods wey improve model relevance while isolating bad content
   - Help AI systems keep correct instruction order and ignore injected commands

3. **Delimiter & Datamarking Systems**
   - Clear boundary between trusted system messages and external input text
   - Special markers to show boundaries between trusted and untrusted data sources
   - Clear separation stop instruction confusion and unauthorized command execution

4. **Continuous Threat Intelligence**
   - Microsoft dey always watch new attack patterns and update defenses
   - Proactive threat hunting for new injection methods and attack ways
   - Regular security model updates to keep effectiveness against changing threats

5. **Azure Content Safety Integration**
   - Part of full Azure AI Content Safety suite
   - Extra detection for jailbreak attempts, harmful content, and security policy breaks
   - Unified security controls across AI app parts

**Implementation Resources**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/pcm/prompt-shield.ff5b95be76e9c78c.webp)


## Advanced MCP Security Threats

### Session Hijacking Vulnerabilities

**Session hijacking** na serious attack way for stateful MCP implementations where unauthorized people fit get and misuse real session IDs to pretend to be clients and do unauthorized actions.

#### **Attack Scenarios & Risks**

- **Session Hijack Prompt Injection**: Attackers wey get stolen session IDs fit inject bad events into servers wey share session state, fit trigger bad actions or access sensitive data
- **Direct Impersonation**: Stolen session IDs fit allow direct MCP server calls wey bypass authentication, treating attackers as real users
- **Compromised Resumable Streams**: Attackers fit stop requests early, making real clients resume with possibly bad content

#### **Security Controls for Session Management**

**Critical Requirements:**
- **Authorization Verification**: MCP servers wey dey do authorization **MUST** check ALL inbound requests and **MUST NOT** rely on sessions for authentication
- **Secure Session Generation**: Use cryptographically secure, non-deterministic session IDs wey dem generate with secure random number generators
- **User-Specific Binding**: Bind session IDs to user-specific information using formats like `<user_id>:<session_id>` to stop cross-user session abuse
- **Session Lifecycle Management**: Make proper expiration, rotation, and invalidation to limit vulnerability windows
- **Transport Security**: HTTPS na mandatory for all communication to stop session ID interception

### Confused Deputy Problem

The **confused deputy problem** dey happen when MCP servers dey act as authentication proxies between clients and third-party services, e dey create chances for authorization bypass through static client ID exploitation.

#### **Attack Mechanics & Risks**

- **Cookie-based Consent Bypass**: Previous user authentication dey create consent cookies wey attackers fit use through malicious authorization requests with crafted redirect URIs
- **Authorization Code Theft**: Existing consent cookies fit make authorization servers skip consent screens, redirecting codes to attacker-controlled endpoints  
- **Unauthorized API Access**: Stolen authorization codes fit allow token exchange and user impersonation without explicit approval

#### **Mitigation Strategies**

**Mandatory Controls:**
- **Explicit Consent Requirements**: MCP proxy servers wey dey use static client IDs **MUST** get user consent for each dynamically registered client
- **OAuth 2.1 Security Implementation**: Follow current OAuth security best practices including PKCE (Proof Key for Code Exchange) for all authorization requests
- **Strict Client Validation**: Make strong validation of redirect URIs and client identifiers to stop exploitation

### Token Passthrough Vulnerabilities  

**Token passthrough** na clear anti-pattern wey MCP servers dey accept client tokens without proper validation and forward dem to downstream APIs, e dey violate MCP authorization specifications.

#### **Security Implications**

- **Control Circumvention**: Direct client-to-API token usage dey bypass important rate limiting, validation, and monitoring controls
- **Audit Trail Corruption**: Tokens wey upstream issue fit make client identification impossible, e go spoil incident investigation capabilities
- **Proxy-based Data Exfiltration**: Unvalidated tokens fit allow bad actors use servers as proxies for unauthorized data access
- **Trust Boundary Violations**: Downstream services trust assumptions fit break when token origins no fit verify
- **Multi-service Attack Expansion**: Compromised tokens wey dem accept for many services fit allow lateral movement

#### **Required Security Controls**

**Non-negotiable Requirements:**
- **Token Validation**: MCP servers **MUST NOT** accept tokens wey no explicitly issue for the MCP server
- **Audience Verification**: Always check token audience claims make sure dem match MCP server identity
- **Proper Token Lifecycle**: Use short-lived access tokens with secure rotation practices


## Supply Chain Security for AI Systems

Supply chain security don grow pass traditional software dependencies to cover the whole AI ecosystem. Modern MCP implementations must seriously verify and monitor all AI-related components, because each one fit bring vulnerability wey fit spoil system integrity.

### Expanded AI Supply Chain Components

**Traditional Software Dependencies:**
- Open-source libraries and frameworks
- Container images and base systems  
- Development tools and build pipelines
- Infrastructure components and services

**AI-Specific Supply Chain Elements:**
- **Foundation Models**: Pre-trained models from different providers wey need provenance verification
- **Embedding Services**: External vectorization and semantic search services
- **Context Providers**: Data sources, knowledge bases, and document repositories  
- **Third-party APIs**: External AI services, ML pipelines, and data processing endpoints
- **Model Artifacts**: Weights, configurations, and fine-tuned model variants
- **Training Data Sources**: Datasets wey dem use for model training and fine-tuning

### Comprehensive Supply Chain Security Strategy

#### **Component Verification & Trust**
- **Provenance Validation**: Check origin, licensing, and integrity of all AI components before integration
- **Security Assessment**: Do vulnerability scans and security reviews for models, data sources, and AI services
- **Reputation Analysis**: Check security track record and practices of AI service providers
- **Compliance Verification**: Make sure all components meet organizational security and regulatory requirements

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Put security scanning for all automated deployment pipelines
- **Artifact Integrity**: Use cryptographic verification for all deployed artifacts (code, models, configurations)
- **Staged Deployment**: Use progressive deployment strategies with security validation for each stage
- **Trusted Artifact Repositories**: Deploy only from verified, secure artifact registries and repositories

#### **Continuous Monitoring & Response**
- **Dependency Scanning**: Ongoing vulnerability monitoring for all software and AI component dependencies
- **Model Monitoring**: Continuous check of model behavior, performance drift, and security anomalies
- **Service Health Tracking**: Monitor external AI services for availability, security incidents, and policy changes
- **Threat Intelligence Integration**: Add threat feeds wey dey specific to AI and ML security risks

#### **Access Control & Least Privilege**
- **Component-level Permissions**: Restrict access to models, data, and services based on business need
- **Service Account Management**: Use dedicated service accounts with minimal required permissions
- **Network Segmentation**: Separate AI components and limit network access between services
- **API Gateway Controls**: Use centralized API gateways to control and monitor access to external AI services

#### **Incident Response & Recovery**
- **Rapid Response Procedures**: Get processes for patching or replacing compromised AI components
- **Credential Rotation**: Automated systems for rotating secrets, API keys, and service credentials
- **Rollback Capabilities**: Fit quickly revert to previous known-good versions of AI components
- **Supply Chain Breach Recovery**: Specific processes for responding to upstream AI service compromises

### Microsoft Security Tools & Integration

**GitHub Advanced Security** dey provide full supply chain protection including:
- **Secret Scanning**: Automated detection of credentials, API keys, and tokens in repositories
- **Dependency Scanning**: Vulnerability assessment for open-source dependencies and libraries
- **CodeQL Analysis**: Static code analysis for security vulnerabilities and coding issues
- **Supply Chain Insights**: Visibility into dependency health and security status

**Azure DevOps & Azure Repos Integration:**
- Smooth security scanning integration across Microsoft development platforms
- Automated security checks in Azure Pipelines for AI workloads
- Policy enforcement for secure AI component deployment

**Microsoft Internal Practices:**
Microsoft dey do plenty supply chain security practices across all products. Learn about proven approaches for [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Best Practices

MCP implementations dey inherit and build on top of your organization's existing security posture. Strong foundational security practices go improve the overall security of AI systems and MCP deployments well well.

### Core Security Fundamentals

#### **Secure Development Practices**
- **OWASP Compliance**: Protect against [OWASP Top 10](https://owasp.org/www-project-top-ten/) web application vulnerabilities
- **AI-Specific Protections**: Put controls for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Secure Secrets Management**: Use dedicated vaults for tokens, API keys, and sensitive configuration data
- **End-to-End Encryption**: Use secure communications across all application components and data flows
- **Input Validation**: Strong validation of all user inputs, API parameters, and data sources

#### **Infrastructure Hardening**
- **Multi-Factor Authentication**: Mandatory MFA for all administrative and service accounts
- **Patch Management**: Automated, timely patching for operating systems, frameworks, and dependencies  
- **Identity Provider Integration**: Centralized identity management through enterprise identity providers (Microsoft Entra ID, Active Directory)
- **Network Segmentation**: Logical isolation of MCP components to limit lateral movement potential
- **Principle of Least Privilege**: Minimal required permissions for all system components and accounts

#### **Security Monitoring & Detection**
- **Comprehensive Logging**: Detailed logging of AI application activities, including MCP client-server interactions
- **SIEM Integration**: Centralized security information and event management for anomaly detection
- **Behavioral Analytics**: AI-powered monitoring to detect unusual patterns in system and user behavior
- **Threat Intelligence**: Integration of external threat feeds and indicators of compromise (IOCs)
- **Incident Response**: Well-defined procedures for security incident detection, response, and recovery

#### **Zero Trust Architecture**
- **Never Trust, Always Verify**: Continuous verification of users, devices, and network connections
- **Micro-Segmentation**: Granular network controls wey isolate individual workloads and services
- **Identity-Centric Security**: Security policies based on verified identities no be network location
- **Continuous Risk Assessment**: Dynamic security posture evaluation based on current context and behavior
- **Conditional Access**: Access controls wey adapt based on risk factors, location, and device trust

### Enterprise Integration Patterns

#### **Microsoft Security Ecosystem Integration**
- **Microsoft Defender for Cloud**: Full cloud security posture management
- **Azure Sentinel**: Cloud-native SIEM and SOAR capabilities for AI workload protection
- **Microsoft Entra ID**: Enterprise identity and access management with conditional access policies
- **Azure Key Vault**: Centralized secrets management with hardware security module (HSM) backing
- **Microsoft Purview**: Data governance and compliance for AI data sources and workflows

#### **Compliance & Governance**
- **Regulatory Alignment**: Make sure MCP implementations meet industry-specific compliance requirements (GDPR, HIPAA, SOC 2)
- **Data Classification**: Proper categorization and handling of sensitive data wey AI systems process
- **Audit Trails**: Full logging for regulatory compliance and forensic investigation
- **Privacy Controls**: Put privacy-by-design principles for AI system architecture
- **Change Management**: Formal processes for security reviews of AI system modifications

These foundational practices go create strong security baseline wey go improve MCP-specific security controls and give full protection for AI-driven applications.

## Key Security Takeaways

- **Layered Security Approach**: Combine foundational security practices (secure coding, least privilege, supply chain verification, continuous monitoring) with AI-specific controls for full protection

- **AI-Specific Threat Landscape**: MCP systems get unique risks like prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, and excessive permissions wey need special mitigations

- **Authentication & Authorization Excellence**: Use strong authentication with external identity providers (Microsoft Entra ID), enforce proper token validation, and no accept tokens wey no explicitly issue for your MCP server

- **AI Attack Prevention**: Use Microsoft Prompt Shields and Azure Content Safety to defend against indirect prompt injection and tool poisoning attacks, plus validate tool metadata and monitor for dynamic changes

- **Session & Transport Security**: Use cryptographically secure, non-deterministic session IDs wey bind to user identities, do proper session lifecycle management, and no use sessions for authentication

- **OAuth Security Best Practices**: Stop confused deputy attacks with explicit user consent for dynamically registered clients, proper OAuth 2.1 implementation with PKCE, and strict redirect URI validation  

- **Token Security Principles**: Avoid token passthrough anti-patterns, validate token audience claims, use short-lived tokens with secure rotation, and keep clear trust boundaries

- **Comprehensive Supply Chain Security**: Treat all AI ecosystem components (models, embeddings, context providers, external APIs) with the same security rigor as traditional software dependencies

- **Continuous Evolution**: Stay up-to-date with fast-changing MCP specifications, contribute to security community standards, and keep adaptive security postures as the protocol mature

- **Microsoft Security Integration**: Use Microsoft's full security ecosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for better MCP deployment protection

## Comprehensive Resources

### **Official MCP Security Documentation**
- [MCP Specification (Current: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
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

For full security guidance, check dis special documents for dis section:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Complete security best practices for MCP implementations
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Practical implementation examples for Azure Content Safety integration  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Latest security controls and techniques for MCP deployments
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Quick reference guide for essential MCP security practices

---

## Wetin Next

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or wrong tins. Di original document wey e dey for im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
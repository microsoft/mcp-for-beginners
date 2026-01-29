# MCP Security: Comprehensive Protection for AI Systems

[![MCP Security Best Practices](../../../translated_images/en/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Click the image above to view video of this lesson)_

Security is fundamental to AI system design, which is why we prioritize it as our second section. This aligns with Microsoft's **Secure by Design** principle from the [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

The Model Context Protocol (MCP) brings powerful new capabilities to AI-driven applications while introducing unique security challenges that extend beyond traditional software risks. MCP systems face both established security concerns (secure coding, least privilege, supply chain security) and new AI-specific threats including prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough vulnerabilities, and dynamic capability modification.

This lesson explores the most critical security risks in MCP implementations—covering authentication, authorization, excessive permissions, indirect prompt injection, session security, confused deputy problems, token management, and supply chain vulnerabilities. You'll learn actionable controls and best practices to mitigate these risks while leveraging Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to strengthen your MCP deployment.

## Learning Objectives

By the end of this lesson, you will be able to:

- **Identify MCP-Specific Threats**: Recognize unique security risks in MCP systems including prompt injection, tool poisoning, excessive permissions, session hijacking, confused deputy problems, token passthrough vulnerabilities, and supply chain risks
- **Apply Security Controls**: Implement effective mitigations including robust authentication, least privilege access, secure token management, session security controls, and supply chain verification
- **Leverage Microsoft Security Solutions**: Understand and deploy Microsoft Prompt Shields, Azure Content Safety, and GitHub Advanced Security for MCP workload protection
- **Validate Tool Security**: Recognize the importance of tool metadata validation, monitoring for dynamic changes, and defending against indirect prompt injection attacks
- **Integrate Best Practices**: Combine established security fundamentals (secure coding, server hardening, zero trust) with MCP-specific controls for comprehensive protection

# MCP Security Architecture & Controls

Modern MCP implementations require layered security approaches that address both traditional software security and AI-specific threats. The rapidly evolving MCP specification continues to mature its security controls, enabling better integration with enterprise security architectures and established best practices.

Research from the [Microsoft Digital Defense Report](https://aka.ms/mddr) demonstrates that **98% of reported breaches would be prevented by robust security hygiene**. The most effective protection strategy combines foundational security practices with MCP-specific controls—proven baseline security measures remain the most impactful in reducing overall security risk.

## Current Security Landscape

> **Note:** This information reflects MCP security standards as of **December 18, 2025**. The MCP protocol continues evolving rapidly, and future implementations may introduce new authentication patterns and enhanced controls. Always refer to the current [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol), and [security best practices documentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) for the latest guidance.

### Evolution of MCP Authentication

The MCP specification has evolved significantly in its approach to authentication and authorization:

- **Original Approach**: Early specifications required developers to implement custom authentication servers, with MCP servers acting as OAuth 2.0 Authorization Servers managing user authentication directly
- **Current Standard (2025-11-25)**: Updated specification allows MCP servers to delegate authentication to external identity providers (such as Microsoft Entra ID), improving security posture and reducing implementation complexity
- **Transport Layer Security**: Enhanced support for secure transport mechanisms with proper authentication patterns for both local (STDIO) and remote (Streamable HTTP) connections

## Authentication & Authorization Security

### Current Security Challenges

Modern MCP implementations face several authentication and authorization challenges:

### Risks & Threat Vectors

- **Misconfigured Authorization Logic**: Flawed authorization implementation in MCP servers can expose sensitive data and incorrectly apply access controls
- **OAuth Token Compromise**: Local MCP server token theft enables attackers to impersonate servers and access downstream services
- **Token Passthrough Vulnerabilities**: Improper token handling creates security control bypasses and accountability gaps
- **Excessive Permissions**: Over-privileged MCP servers violate least privilege principles and expand attack surfaces

#### Token Passthrough: A Critical Anti-Pattern

**Token passthrough is explicitly prohibited** in the current MCP authorization specification due to severe security implications:

##### Security Control Circumvention
- MCP servers and downstream APIs implement critical security controls (rate limiting, request validation, traffic monitoring) that depend on proper token validation
- Direct client-to-API token usage bypasses these essential protections, undermining the security architecture

##### Accountability & Audit Challenges  
- MCP servers cannot distinguish between clients using upstream-issued tokens, breaking audit trails
- Downstream resource server logs show misleading request origins rather than actual MCP server intermediaries
- Incident investigation and compliance auditing become significantly more difficult

##### Data Exfiltration Risks
- Unvalidated token claims enable malicious actors with stolen tokens to use MCP servers as proxies for data exfiltration
- Trust boundary violations allow unauthorized access patterns that bypass intended security controls

##### Multi-Service Attack Vectors
- Compromised tokens accepted by multiple services enable lateral movement across connected systems
- Trust assumptions between services may be violated when token origins cannot be verified

### Security Controls & Mitigations

**Critical Security Requirements:**

> **MANDATORY**: MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server

#### Authentication & Authorization Controls

- **Rigorous Authorization Review**: Conduct comprehensive audits of MCP server authorization logic to ensure only intended users and clients can access sensitive resources
  - **Implementation Guide**: [Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Identity Integration**: [Using Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Implement [Microsoft's token validation and lifecycle best practices](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validate token audience claims match MCP server identity
  - Implement proper token rotation and expiration policies
  - Prevent token replay attacks and unauthorized usage

- **Protected Token Storage**: Secure token storage with encryption both at rest and in transit
  - **Best Practices**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Access Control Implementation

- **Principle of Least Privilege**: Grant MCP servers only minimum permissions required for intended functionality
  - Regular permission reviews and updates to prevent privilege creep
  - **Microsoft Documentation**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Implement fine-grained role assignments
  - Scope roles tightly to specific resources and actions
  - Avoid broad or unnecessary permissions that expand attack surfaces

- **Continuous Permission Monitoring**: Implement ongoing access auditing and monitoring
  - Monitor permission usage patterns for anomalies
  - Promptly remediate excessive or unused privileges

## AI-Specific Security Threats

### Prompt Injection & Tool Manipulation Attacks

Modern MCP implementations face sophisticated AI-specific attack vectors that traditional security measures cannot fully address:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

**Indirect Prompt Injection** represents one of the most critical vulnerabilities in MCP-enabled AI systems. Attackers embed malicious instructions within external content—documents, web pages, emails, or data sources—that AI systems subsequently process as legitimate commands.

**Attack Scenarios:**
- **Document-based Injection**: Malicious instructions hidden in processed documents that trigger unintended AI actions
- **Web Content Exploitation**: Compromised web pages containing embedded prompts that manipulate AI behavior when scraped
- **Email-based Attacks**: Malicious prompts in emails that cause AI assistants to leak information or perform unauthorized actions
- **Data Source Contamination**: Compromised databases or APIs serving tainted content to AI systems

**Real-World Impact**: These attacks can result in data exfiltration, privacy breaches, generation of harmful content, and manipulation of user interactions. For detailed analysis, see [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/en/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning Attacks**

**Tool Poisoning** targets the metadata that defines MCP tools, exploiting how LLMs interpret tool descriptions and parameters to make execution decisions.

**Attack Mechanisms:**
- **Metadata Manipulation**: Attackers inject malicious instructions into tool descriptions, parameter definitions, or usage examples
- **Invisible Instructions**: Hidden prompts in tool metadata that are processed by AI models but invisible to human users
- **Dynamic Tool Modification ("Rug Pulls")**: Tools approved by users are later modified to perform malicious actions without user awareness
- **Parameter Injection**: Malicious content embedded in tool parameter schemas that influence model behavior

**Hosted Server Risks**: Remote MCP servers present elevated risks as tool definitions can be updated after initial user approval, creating scenarios where previously safe tools become malicious. For comprehensive analysis, see [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/en/tool-injection.3b0b4a6b24de6bef.webp)

#### **Additional AI Attack Vectors**

- **Cross-Domain Prompt Injection (XPIA)**: Sophisticated attacks that leverage content from multiple domains to bypass security controls
- **Dynamic Capability Modification**: Real-time changes to tool capabilities that escape initial security assessments
- **Context Window Poisoning**: Attacks that manipulate large context windows to hide malicious instructions
- **Model Confusion Attacks**: Exploiting model limitations to create unpredictable or unsafe behaviors


### AI Security Risk Impact

**High-Impact Consequences:**
- **Data Exfiltration**: Unauthorized access and theft of sensitive enterprise or personal data
- **Privacy Breaches**: Exposure of personally identifiable information (PII) and confidential business data  
- **System Manipulation**: Unintended modifications to critical systems and workflows
- **Credential Theft**: Compromise of authentication tokens and service credentials
- **Lateral Movement**: Use of compromised AI systems as pivots for broader network attacks

### Microsoft AI Security Solutions

#### **AI Prompt Shields: Advanced Protection Against Injection Attacks**

Microsoft **AI Prompt Shields** provide comprehensive defense against both direct and indirect prompt injection attacks through multiple security layers:

##### **Core Protection Mechanisms:**

1. **Advanced Detection & Filtering**
   - Machine learning algorithms and NLP techniques detect malicious instructions in external content
   - Real-time analysis of documents, web pages, emails, and data sources for embedded threats
   - Contextual understanding of legitimate vs. malicious prompt patterns

2. **Spotlighting Techniques**  
   - Distinguishes between trusted system instructions and potentially compromised external inputs
   - Text transformation methods that enhance model relevance while isolating malicious content
   - Helps AI systems maintain proper instruction hierarchy and ignore injected commands

3. **Delimiter & Datamarking Systems**
   - Explicit boundary definition between trusted system messages and external input text
   - Special markers highlight boundaries between trusted and untrusted data sources
   - Clear separation prevents instruction confusion and unauthorized command execution

4. **Continuous Threat Intelligence**
   - Microsoft continuously monitors emerging attack patterns and updates defenses
   - Proactive threat hunting for new injection techniques and attack vectors
   - Regular security model updates to maintain effectiveness against evolving threats

5. **Azure Content Safety Integration**
   - Part of comprehensive Azure AI Content Safety suite
   - Additional detection for jailbreak attempts, harmful content, and security policy violations
   - Unified security controls across AI application components

**Implementation Resources**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/en/prompt-shield.ff5b95be76e9c78c.webp)


## Advanced MCP Security Threats

### Session Hijacking Vulnerabilities

**Session hijacking** represents a critical attack vector in stateful MCP implementations where unauthorized parties obtain and abuse legitimate session identifiers to impersonate clients and perform unauthorized actions.

#### **Attack Scenarios & Risks**

- **Session Hijack Prompt Injection**: Attackers with stolen session IDs inject malicious events into servers sharing session state, potentially triggering harmful actions or accessing sensitive data
- **Direct Impersonation**: Stolen session IDs enable direct MCP server calls that bypass authentication, treating attackers as legitimate users
- **Compromised Resumable Streams**: Attackers can terminate requests prematurely, causing legitimate clients to resume with potentially malicious content

#### **Security Controls for Session Management**

**Critical Requirements:**
- **Authorization Verification**: MCP servers implementing authorization **MUST** verify ALL inbound requests and **MUST NOT** rely on sessions for authentication
- **Secure Session Generation**: Use cryptographically secure, non-deterministic session IDs generated with secure random number generators
- **User-Specific Binding**: Bind session IDs to user-specific information using formats like `<user_id>:<session_id>` to prevent cross-user session abuse
- **Session Lifecycle Management**: Implement proper expiration, rotation, and invalidation to limit vulnerability windows
- **Transport Security**: Mandatory HTTPS for all communication to prevent session ID interception

### Confused Deputy Problem

The **confused deputy problem** occurs when MCP servers act as authentication proxies between clients and third-party services, creating opportunities for authorization bypass through static client ID exploitation.

#### **Attack Mechanics & Risks**

- **Cookie-based Consent Bypass**: Previous user authentication creates consent cookies that attackers exploit through malicious authorization requests with crafted redirect URIs
- **Authorization Code Theft**: Existing consent cookies may cause authorization servers to skip consent screens, redirecting codes to attacker-controlled endpoints  
- **Unauthorized API Access**: Stolen authorization codes enable token exchange and user impersonation without explicit approval

#### **Mitigation Strategies**

**Mandatory Controls:**
- **Explicit Consent Requirements**: MCP proxy servers using static client IDs **MUST** obtain user consent for each dynamically registered client
- **OAuth 2.1 Security Implementation**: Follow current OAuth security best practices including PKCE (Proof Key for Code Exchange) for all authorization requests
- **Strict Client Validation**: Implement rigorous validation of redirect URIs and client identifiers to prevent exploitation

### Token Passthrough Vulnerabilities  

**Token passthrough** represents an explicit anti-pattern where MCP servers accept client tokens without proper validation and forward them to downstream APIs, violating MCP authorization specifications.

#### **Security Implications**

- **Control Circumvention**: Direct client-to-API token usage bypasses critical rate limiting, validation, and monitoring controls
- **Audit Trail Corruption**: Upstream-issued tokens make client identification impossible, breaking incident investigation capabilities
- **Proxy-based Data Exfiltration**: Unvalidated tokens enable malicious actors to use servers as proxies for unauthorized data access
- **Trust Boundary Violations**: Downstream services' trust assumptions may be violated when token origins cannot be verified
- **Multi-service Attack Expansion**: Compromised tokens accepted across multiple services enable lateral movement

#### **Required Security Controls**

**Non-negotiable Requirements:**
- **Token Validation**: MCP servers **MUST NOT** accept tokens not explicitly issued for the MCP server
- **Audience Verification**: Always validate token audience claims match the MCP server's identity
- **Proper Token Lifecycle**: Implement short-lived access tokens with secure rotation practices


## Supply Chain Security for AI Systems

Supply chain security has evolved beyond traditional software dependencies to encompass the entire AI ecosystem. Modern MCP implementations must rigorously verify and monitor all AI-related components, as each introduces potential vulnerabilities that could compromise system integrity.

### Expanded AI Supply Chain Components

**Traditional Software Dependencies:**
- Open-source libraries and frameworks
- Container images and base systems  
- Development tools and build pipelines
- Infrastructure components and services

**AI-Specific Supply Chain Elements:**
- **Foundation Models**: Pre-trained models from various providers requiring provenance verification
- **Embedding Services**: External vectorization and semantic search services
- **Context Providers**: Data sources, knowledge bases, and document repositories  
- **Third-party APIs**: External AI services, ML pipelines, and data processing endpoints
- **Model Artifacts**: Weights, configurations, and fine-tuned model variants
- **Training Data Sources**: Datasets used for model training and fine-tuning

### Comprehensive Supply Chain Security Strategy

#### **Component Verification & Trust**
- **Provenance Validation**: Verify the origin, licensing, and integrity of all AI components before integration
- **Security Assessment**: Conduct vulnerability scans and security reviews for models, data sources, and AI services
- **Reputation Analysis**: Evaluate the security track record and practices of AI service providers
- **Compliance Verification**: Ensure all components meet organizational security and regulatory requirements

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Integrate security scanning throughout automated deployment pipelines
- **Artifact Integrity**: Implement cryptographic verification for all deployed artifacts (code, models, configurations)
- **Staged Deployment**: Use progressive deployment strategies with security validation at each stage
- **Trusted Artifact Repositories**: Deploy only from verified, secure artifact registries and repositories

#### **Continuous Monitoring & Response**
- **Dependency Scanning**: Ongoing vulnerability monitoring for all software and AI component dependencies
- **Model Monitoring**: Continuous assessment of model behavior, performance drift, and security anomalies
- **Service Health Tracking**: Monitor external AI services for availability, security incidents, and policy changes
- **Threat Intelligence Integration**: Incorporate threat feeds specific to AI and ML security risks

#### **Access Control & Least Privilege**
- **Component-level Permissions**: Restrict access to models, data, and services based on business necessity
- **Service Account Management**: Implement dedicated service accounts with minimal required permissions
- **Network Segmentation**: Isolate AI components and limit network access between services
- **API Gateway Controls**: Use centralized API gateways to control and monitor access to external AI services

#### **Incident Response & Recovery**
- **Rapid Response Procedures**: Established processes for patching or replacing compromised AI components
- **Credential Rotation**: Automated systems for rotating secrets, API keys, and service credentials
- **Rollback Capabilities**: Ability to quickly revert to previous known-good versions of AI components
- **Supply Chain Breach Recovery**: Specific procedures for responding to upstream AI service compromises

### Microsoft Security Tools & Integration

**GitHub Advanced Security** provides comprehensive supply chain protection including:
- **Secret Scanning**: Automated detection of credentials, API keys, and tokens in repositories
- **Dependency Scanning**: Vulnerability assessment for open-source dependencies and libraries
- **CodeQL Analysis**: Static code analysis for security vulnerabilities and coding issues
- **Supply Chain Insights**: Visibility into dependency health and security status

**Azure DevOps & Azure Repos Integration:**
- Seamless security scanning integration across Microsoft development platforms
- Automated security checks in Azure Pipelines for AI workloads
- Policy enforcement for secure AI component deployment

**Microsoft Internal Practices:**
Microsoft implements extensive supply chain security practices across all products. Learn about proven approaches in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Foundation Security Best Practices

MCP implementations inherit and build upon your organization's existing security posture. Strengthening foundational security practices significantly enhances the overall security of AI systems and MCP deployments.

### Core Security Fundamentals

#### **Secure Development Practices**
- **OWASP Compliance**: Protect against [OWASP Top 10](https://owasp.org/www-project-top-ten/) web application vulnerabilities
- **AI-Specific Protections**: Implement controls for [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Secure Secrets Management**: Use dedicated vaults for tokens, API keys, and sensitive configuration data
- **End-to-End Encryption**: Implement secure communications across all application components and data flows
- **Input Validation**: Rigorous validation of all user inputs, API parameters, and data sources

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
- **Micro-Segmentation**: Granular network controls that isolate individual workloads and services
- **Identity-Centric Security**: Security policies based on verified identities rather than network location
- **Continuous Risk Assessment**: Dynamic security posture evaluation based on current context and behavior
- **Conditional Access**: Access controls that adapt based on risk factors, location, and device trust

### Enterprise Integration Patterns

#### **Microsoft Security Ecosystem Integration**
- **Microsoft Defender for Cloud**: Comprehensive cloud security posture management
- **Azure Sentinel**: Cloud-native SIEM and SOAR capabilities for AI workload protection
- **Microsoft Entra ID**: Enterprise identity and access management with conditional access policies
- **Azure Key Vault**: Centralized secrets management with hardware security module (HSM) backing
- **Microsoft Purview**: Data governance and compliance for AI data sources and workflows

#### **Compliance & Governance**
- **Regulatory Alignment**: Ensure MCP implementations meet industry-specific compliance requirements (GDPR, HIPAA, SOC 2)
- **Data Classification**: Proper categorization and handling of sensitive data processed by AI systems
- **Audit Trails**: Comprehensive logging for regulatory compliance and forensic investigation
- **Privacy Controls**: Implementation of privacy-by-design principles in AI system architecture
- **Change Management**: Formal processes for security reviews of AI system modifications

These foundational practices create a robust security baseline that enhances the effectiveness of MCP-specific security controls and provides comprehensive protection for AI-driven applications.

## Key Security Takeaways

- **Layered Security Approach**: Combine foundational security practices (secure coding, least privilege, supply chain verification, continuous monitoring) with AI-specific controls for comprehensive protection

- **AI-Specific Threat Landscape**: MCP systems face unique risks including prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, and excessive permissions that require specialized mitigations

- **Authentication & Authorization Excellence**: Implement robust authentication using external identity providers (Microsoft Entra ID), enforce proper token validation, and never accept tokens not explicitly issued for your MCP server

- **AI Attack Prevention**: Deploy Microsoft Prompt Shields and Azure Content Safety to defend against indirect prompt injection and tool poisoning attacks, while validating tool metadata and monitoring for dynamic changes

- **Session & Transport Security**: Use cryptographically secure, non-deterministic session IDs bound to user identities, implement proper session lifecycle management, and never use sessions for authentication

- **OAuth Security Best Practices**: Prevent confused deputy attacks through explicit user consent for dynamically registered clients, proper OAuth 2.1 implementation with PKCE, and strict redirect URI validation  

- **Token Security Principles**: Avoid token passthrough anti-patterns, validate token audience claims, implement short-lived tokens with secure rotation, and maintain clear trust boundaries

- **Comprehensive Supply Chain Security**: Treat all AI ecosystem components (models, embeddings, context providers, external APIs) with the same security rigor as traditional software dependencies

- **Continuous Evolution**: Stay current with rapidly evolving MCP specifications, contribute to security community standards, and maintain adaptive security postures as the protocol matures

- **Microsoft Security Integration**: Leverage Microsoft's comprehensive security ecosystem (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) for enhanced MCP deployment protection

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

For comprehensive security guidance, refer to these specialized documents in this section:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Complete security best practices for MCP implementations
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Practical implementation examples for Azure Content Safety integration  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Latest security controls and techniques for MCP deployments
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Quick reference guide for essential MCP security practices

---

## What's Next

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f00aedb7b1d11b7eaacb0618d8791c65",
  "translation_date": "2025-05-29T23:04:46+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "mo"
}
-->
# Security Best Practices

Adopting the Model Context Protocol (MCP) brings powerful new capabilities to AI-driven applications, but also introduces unique security challenges that go beyond traditional software risks. Alongside established concerns like secure coding, least privilege, and supply chain security, MCP and AI workloads face new threats such as prompt injection, tool poisoning, and dynamic tool modification. If not properly managed, these risks can lead to data leaks, privacy violations, and unintended system behavior.

This lesson covers the most relevant security risks related to MCP—including authentication, authorization, excessive permissions, indirect prompt injection, and supply chain vulnerabilities—and offers practical controls and best practices to address them. You’ll also learn how to use Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to strengthen your MCP deployment. By understanding and applying these controls, you can greatly reduce the chance of a security breach and keep your AI systems reliable and secure.

# Learning Objectives

By the end of this lesson, you will be able to:

- Identify and explain the unique security risks introduced by the Model Context Protocol (MCP), including prompt injection, tool poisoning, excessive permissions, and supply chain vulnerabilities.
- Describe and apply effective mitigating controls for MCP security risks, such as strong authentication, least privilege, secure token management, and supply chain verification.
- Understand and leverage Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP and AI workloads.
- Recognize the importance of validating tool metadata, monitoring for dynamic changes, and defending against indirect prompt injection attacks.
- Integrate established security best practices—such as secure coding, server hardening, and zero trust architecture—into your MCP implementation to minimize the likelihood and impact of security breaches.

# MCP security controls

Any system with access to important resources faces inherent security challenges. These challenges can usually be addressed through proper application of fundamental security controls and concepts. Since MCP is newly defined, its specification is evolving rapidly. As the protocol matures, its security controls will improve, allowing better integration with enterprise security architectures and best practices.

Research published in the [Microsoft Digital Defense Report](https://aka.ms/mddr) shows that 98% of reported breaches could be prevented by robust security hygiene. The best defense against any breach remains getting your baseline security hygiene, secure coding best practices, and supply chain security right—these proven measures still have the greatest impact in reducing risk.

Let’s explore some ways you can start addressing security risks when adopting MCP.

> **Note:** The following information is accurate as of **29th May 2025**. The MCP protocol is continuously evolving, and future implementations may introduce new authentication methods and controls. For the latest updates and guidance, always consult the [MCP Specification](https://spec.modelcontextprotocol.io/), the official [MCP GitHub repository](https://github.com/modelcontextprotocol), and the [security best practice page](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices).

### Problem statement  
The original MCP specification assumed developers would build their own authentication server. This required knowledge of OAuth and related security constraints. MCP servers acted as OAuth 2.0 Authorization Servers, managing user authentication directly rather than delegating it to external services like Microsoft Entra ID. As of **26 April 2025**, an update to the MCP specification allows MCP servers to delegate user authentication to external services.

### Risks
- Misconfigured authorization logic in the MCP server can cause sensitive data exposure and incorrect access controls.
- OAuth token theft on the local MCP server. If stolen, tokens can be used to impersonate the MCP server and access resources and data intended for that OAuth token.

#### Token Passthrough
Token passthrough is explicitly prohibited in the authorization specification because it introduces several security risks, including:

#### Security Control Circumvention
The MCP Server or downstream APIs may enforce security controls like rate limiting, request validation, or traffic monitoring that rely on the token audience or other credential constraints. If clients can obtain and use tokens directly with downstream APIs without the MCP server validating them or ensuring tokens are issued for the correct service, these controls are bypassed.

#### Accountability and Audit Trail Issues
The MCP Server cannot identify or differentiate between MCP Clients when clients use upstream-issued access tokens that are opaque to the MCP Server.  
The downstream Resource Server’s logs may show requests appearing to come from a different source or identity, rather than the MCP server forwarding the tokens.  
Both issues complicate incident investigation, control enforcement, and auditing.  
If the MCP Server passes tokens without validating claims (e.g., roles, privileges, audience) or other metadata, a malicious actor with a stolen token can use the server as a proxy for data exfiltration.

#### Trust Boundary Issues
The downstream Resource Server trusts specific entities, including assumptions about origin or client behavior. Breaking this trust boundary can cause unexpected problems.  
If tokens are accepted by multiple services without proper validation, an attacker compromising one service could use the token to access others.

#### Future Compatibility Risk
Even if an MCP Server starts as a “pure proxy” today, it may need to add security controls later. Proper token audience separation from the start simplifies evolving the security model.

### Mitigating controls

**MCP servers MUST NOT accept any tokens not explicitly issued for the MCP server**

- **Review and Harden Authorization Logic:** Thoroughly audit your MCP server’s authorization implementation to ensure only intended users and clients access sensitive resources. For practical guidance, see [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) and [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/).
- **Enforce Secure Token Practices:** Follow [Microsoft’s best practices for token validation and lifetime](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) to prevent token misuse and reduce risk of replay or theft.
- **Protect Token Storage:** Always store tokens securely and encrypt them at rest and in transit. For tips, see [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2).

# Excessive permissions for MCP servers

### Problem statement  
MCP servers may be granted excessive permissions to the services or resources they access. For example, an MCP server in an AI sales application connecting to an enterprise data store should have access scoped only to sales data, not to all files in the store. Following the principle of least privilege (one of the oldest security principles), no resource should have more permissions than necessary to perform its intended tasks. AI presents an additional challenge here, as its flexibility makes it difficult to define exact required permissions.

### Risks  
- Excessive permissions can allow data exfiltration or modification of data the MCP server shouldn’t access. This may also pose privacy risks if the data includes personally identifiable information (PII).

### Mitigating controls  
- **Apply the Principle of Least Privilege:** Grant the MCP server only the minimum permissions needed to perform its tasks. Regularly review and adjust these permissions to avoid excess. For detailed guidance, see [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access).  
- **Use Role-Based Access Control (RBAC):** Assign roles to the MCP server narrowly scoped to specific resources and actions, avoiding broad or unnecessary permissions.  
- **Monitor and Audit Permissions:** Continuously track permission usage and audit access logs to quickly detect and remediate excessive or unused privileges.

# Indirect prompt injection attacks

### Problem statement

Malicious or compromised MCP servers can pose serious risks by exposing customer data or enabling unintended actions. These risks are particularly relevant in AI and MCP workloads, including:

- **Prompt Injection Attacks:** Attackers embed malicious instructions in prompts or external content, causing the AI to perform unintended actions or leak sensitive data. Learn more: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- **Tool Poisoning:** Attackers manipulate tool metadata (like descriptions or parameters) to influence AI behavior, potentially bypassing security controls or exfiltrating data. Details: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- **Cross-Domain Prompt Injection:** Malicious instructions hidden in documents, web pages, or emails are processed by AI, leading to data leaks or manipulation.  
- **Dynamic Tool Modification (Rug Pulls):** Tool definitions can be changed after user approval, introducing new malicious behaviors without user awareness.

These vulnerabilities emphasize the need for strong validation, monitoring, and security controls when integrating MCP servers and tools. For more, see the linked references above.

![prompt-injection-lg-2048x1034](../../../translated_images/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.mo.png)

**Indirect Prompt Injection** (also called cross-domain prompt injection or XPIA) is a critical vulnerability in generative AI systems, including those using MCP. In this attack, malicious instructions are hidden inside external content—such as documents, web pages, or emails. When the AI processes this content, it may interpret these instructions as legitimate user commands, resulting in unintended actions like data leaks, harmful content generation, or manipulation of user interactions. For detailed explanations and examples, see [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

A particularly dangerous variant is **Tool Poisoning**. Here, attackers inject malicious instructions into MCP tool metadata (like descriptions or parameters). Since large language models (LLMs) rely on this metadata to decide which tools to call, compromised descriptions can trick the model into executing unauthorized tool calls or bypassing security controls. These manipulations are often invisible to users but acted upon by the AI system. This risk is especially high in hosted MCP server environments, where tool definitions can be updated after user approval—a scenario sometimes called a "[rug pull](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)". In such cases, a previously safe tool may later be altered to perform malicious actions, like data exfiltration or system manipulation, without the user’s knowledge. For more details, see [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![tool-injection-lg-2048x1239 (1)](../../../translated_images/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.mo.png)

## Risks  
Unintended AI actions pose various security risks including data exfiltration and privacy breaches.

### Mitigating controls  
### Using prompt shields to protect against Indirect Prompt Injection attacks  
-----------------------------------------------------------------------------

**AI Prompt Shields** are a Microsoft solution designed to defend against both direct and indirect prompt injection attacks. They help by:

1.  **Detection and Filtering:** Using advanced machine learning and natural language processing to detect and filter malicious instructions embedded in external content such as documents, web pages, or emails.
    
2.  **Spotlighting:** This technique helps the AI distinguish valid system instructions from potentially untrustworthy external inputs. By transforming input text to make it more relevant to the model, Spotlighting improves the AI’s ability to identify and ignore malicious instructions.
    
3.  **Delimiters and Datamarking:** Adding delimiters in system messages clearly marks the location of input text, helping the AI separate user inputs from potentially harmful external content. Datamarking extends this by using special markers to highlight trusted versus untrusted data boundaries.
    
4.  **Continuous Monitoring and Updates:** Microsoft continuously monitors and updates Prompt Shields to address emerging threats. This proactive approach keeps defenses effective against the latest attack techniques.
    
5. **Integration with Azure Content Safety:** Prompt Shields are part of the broader Azure AI Content Safety suite, which offers additional tools to detect jailbreak attempts, harmful content, and other security risks in AI applications.

Learn more about AI prompt shields in the [Prompt Shields documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection).

![prompt-shield-lg-2048x1328](../../../translated_images/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.mo.png)

### Supply chain security

Supply chain security remains critical in the AI era, but the scope of what counts as your supply chain has expanded. Beyond traditional code packages, you must now rigorously verify and monitor all AI-related components, including foundation models, embedding services, context providers, and third-party APIs. Each of these can introduce vulnerabilities or risks if not properly managed.

**Key supply chain security practices for AI and MCP:**  
- **Verify all components before integration:** This includes not just open-source libraries but also AI models, data sources, and external APIs. Always check provenance, licensing, and known vulnerabilities.  
- **Maintain secure deployment pipelines:** Use automated CI/CD pipelines with integrated security scanning to catch issues early. Ensure only trusted artifacts are deployed to production.  
- **Continuously monitor and audit:** Implement ongoing monitoring for all dependencies, including models and data services, to detect new vulnerabilities or supply chain attacks.  
- **Apply least privilege and access controls:** Restrict access to models, data, and services to only what is necessary for your MCP server’s operation.  
- **Respond quickly to threats:** Have processes in place to patch or replace compromised components, and rotate secrets or credentials if a breach is detected.

[GitHub Advanced Security](https://github.com/security/advanced-security) offers features like secret scanning, dependency scanning, and CodeQL analysis. These tools integrate with [Azure DevOps](https://azure.microsoft.com/en-us/products/devops) and [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/) to help teams identify and mitigate vulnerabilities across code and AI supply chain components.

Microsoft also implements extensive supply chain security internally across all products. Learn more in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).

# Established security best practices that will uplift your MCP implementation's security posture

Any MCP implementation inherits the existing security posture of your organization’s environment. When considering MCP security as part of your overall AI systems, it’s recommended to enhance your overall security posture. The following established controls are especially relevant:

- Secure coding best practices in your AI application—protect against [the OWASP Top 10](https://owasp.org/www-project-top-ten/), the [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559), use secure vaults for secrets and tokens, implement end-to-end secure communications between all components, etc.  
- Server hardening—use MFA where possible, keep patches up to date, integrate servers with third-party identity providers for access control, etc.  
- Keep devices, infrastructure, and applications patched and up to date.  
- Security monitoring—implement logging and monitoring for AI applications (including MCP clients/servers) and send logs to a central SIEM for anomaly detection.  
- Zero trust architecture—isolate components via network and identity controls to minimize lateral movement if an AI application is compromised.

# Key Takeaways

- Security fundamentals remain crucial: secure coding, least privilege, supply chain verification, and continuous monitoring are essential for MCP and AI workloads.  
- MCP introduces new risks—like prompt injection, tool poisoning, and excessive permissions—that require both traditional and AI-specific controls.  
- Use strong authentication, authorization, and token management, leveraging external identity providers like Microsoft Entra ID where possible.  
- Protect against indirect prompt injection and tool poisoning by validating tool metadata, monitoring for dynamic changes, and using solutions like Microsoft Prompt Shields.  
- Treat all components in your AI supply chain—including models, embeddings, and context providers—with the same rigor as code dependencies.  
- Stay current with evolving MCP specifications and contribute to the community to help shape secure standards.

# Additional Resources

- [Microsoft Digital Defense Report](https://aka.ms/mddr)  
- [MCP Specification](https://spec.modelcontextprotocol.io/)  
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [Rug Pulls in MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)  
- [Prompt Shields Documentation (Microsoft)](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure DevOps](https://azure.microsoft.com/products/devops)
- [Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)
- [Secure Least-Privileged Access (Microsoft)](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Best Practices for Token Validation and Lifetime](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Use Secure Token Storage and Encrypt Tokens (YouTube)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)
- [Azure API Management as Auth Gateway for MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [MCP Security Best Practice](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [Using Microsoft Entra ID to Authenticate with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

### Next 

Next: [Chapter 3: Getting Started](/03-GettingStarted/README.md)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

Could you please clarify what you mean by "mo"? Are you referring to a specific language or dialect? This will help me provide an accurate translation.
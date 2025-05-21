# Security Best Practices

Adopting the Model Context Protocol (MCP) brings powerful new capabilities to AI-driven applications, but also introduces unique security challenges that extend beyond traditional software risks. In addition to established concerns like secure coding, least privilege, and supply chain security, MCP and AI workloads face new threats such as prompt injection, tool poisoning, and dynamic tool modification. These risks can lead to data exfiltration, privacy breaches, and unintended system behaviour if not properly managed.

This lesson explores the most relevant security risks associated with MCP, including authentication, authorisation, excessive permissions, indirect prompt injection, and supply chain vulnerabilities, and provides actionable controls and best practices to mitigate them. You’ll also learn how to leverage Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to strengthen your MCP implementation. By understanding and applying these controls, you can significantly reduce the likelihood of a security breach and ensure your AI systems remain robust and trustworthy.

# Learning Objectives

By the end of this lesson, you will be able to:

- Identify and explain the unique security risks introduced by the Model Context Protocol (MCP), including prompt injection, tool poisoning, excessive permissions, and supply chain vulnerabilities.
- Describe and apply effective mitigating controls for MCP security risks, such as robust authentication, least privilege, secure token management, and supply chain verification.
- Understand and leverage Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP and AI workloads.
- Recognise the importance of validating tool metadata, monitoring for dynamic changes, and defending against indirect prompt injection attacks.
- Integrate established security best practices—such as secure coding, server hardening, and zero trust architecture—into your MCP implementation to reduce the likelihood and impact of security breaches.

# MCP Security Controls

Any system that has access to important resources has implied security challenges. Security challenges can generally be addressed through the correct application of fundamental security controls and concepts. As MCP is newly defined, the specification is changing very rapidly as the protocol evolves. Eventually, the security controls within it will mature, enabling better integration with enterprise and established security architectures and best practices.

Research published in the [Microsoft Digital Defense Report](https://aka.ms/mddr) states that 98% of reported breaches would be prevented by robust security hygiene. The best protection against any kind of breach is to get your baseline security hygiene, secure coding best practices, and supply chain security right—those tried and tested practices that we already know about still make the most impact in reducing security risk.

Let's look at some of the ways you can start to address security risks when adopting MCP.

# MCP Server Authentication (if your MCP implementation was before 26th April 2025)

> **Note:** The following information is correct as of 26th April 2025. The MCP protocol is continually evolving, and future implementations may introduce new authentication patterns and controls. For the latest updates and guidance, always refer to the [MCP Specification](https://spec.modelcontextprotocol.io/) and the official [MCP GitHub repository](https://github.com/modelcontextprotocol).

### Problem Statement 
The original MCP specification assumed that developers would write their own authentication server. This required knowledge of OAuth and related security constraints. MCP servers acted as OAuth 2.0 Authorisation Servers, managing the required user authentication directly rather than delegating it to an external service such as Microsoft Entra ID. As of 26 April 2025, an update to the MCP specification allows for MCP servers to delegate user authentication to an external service.

### Risks
- Misconfigured authorisation logic in the MCP server can lead to sensitive data exposure and incorrectly applied access controls.
- OAuth token theft on the local MCP server. If stolen, the token can then be used to impersonate the MCP server and access resources and data from the service that the OAuth token is for.

### Mitigating Controls
- **Review and Harden Authorization Logic:** Carefully audit your MCP server’s authorization implementation to ensure only intended users and clients can access sensitive resources. For practical guidance, see [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) and [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/).
- **Enforce Secure Token Practices:** Follow [Microsoft’s best practices for token validation and lifetime](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) to prevent misuse of access tokens and reduce the risk of token replay or theft.
- **Protect Token Storage:** Always store tokens securely and use encryption to safeguard them at rest and in transit. For implementation tips, see [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2).

# Excessive Permissions for MCP Servers

### Problem Statement
MCP servers may have been granted excessive permissions to the service/resource they are accessing. For example, an MCP server that is part of an AI sales application connecting to an enterprise data store should have access scoped to the sales data and not be allowed to access all the files in the store. Referencing the principle of least privilege (one of the oldest security principles), no resource should have permissions in excess of what is required for it to execute the tasks it was intended for. AI presents an increased challenge in this space because, to enable it to be flexible, it can be challenging to define the exact permissions required.

### Risks
- Granting excessive permissions can allow for exfiltration or modification of data that the MCP server was not intended to be able to access. This could also be a privacy issue if the data is personally identifiable information (PII).

### Mitigating Controls
- **Apply the Principle of Least Privilege:** Grant the MCP server only the minimum permissions necessary to perform its required tasks. Regularly review and update these permissions to ensure they do not exceed what is needed. For detailed guidance, see [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access).
- **Use Role-Based Access Control (RBAC):** Assign roles to the MCP server that are tightly scoped to specific resources and actions, avoiding broad or unnecessary permissions.
- **Monitor and Audit Permissions:** Continuously monitor permission usage and audit access logs to detect and remediate excessive or unused privileges promptly.

# Indirect Prompt Injection Attacks

### Problem Statement

Malicious or compromised MCP servers can introduce significant risks by exposing customer data or enabling unintended actions. These risks are especially relevant in AI and MCP-based workloads, where:

- **Prompt Injection Attacks:** Attackers embed malicious instructions in prompts or external content, causing the AI system to perform unintended actions or leak sensitive data. Learn more: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- **Tool Poisoning:** Attackers manipulate tool metadata (such as descriptions or parameters) to influence the AI’s behaviour, potentially bypassing security controls or exfiltrating data. Details: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- **Cross-Domain Prompt Injection:** Malicious instructions are embedded in documents, web pages, or emails, which are then processed by the AI, leading to data leakage or manipulation.
- **Dynamic Tool Modification (Rug Pulls):** Tool definitions can be changed after user approval, introducing new malicious behaviours without user awareness.

These vulnerabilities highlight the need for robust validation, monitoring, and security controls when integrating MCP servers and tools into your environment. For a deeper dive, see the linked references above.

![prompt-injection-lg-2048x1034](../images/02-Security/prompt-injection.png)

**Indirect Prompt Injection** (also known as cross-domain prompt injection or XPIA) is a critical vulnerability in generative AI systems, including those using the Model Context Protocol (MCP). In this attack, malicious instructions are hidden within external content, such as documents, web pages, or emails. When the AI system processes this content, it may interpret the embedded instructions as legitimate user commands, resulting in unintended actions like data leakage, generation of harmful content, or manipulation of user interactions. For a detailed explanation and real-world examples, see [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

A particularly dangerous form of this attack is **Tool Poisoning**. Here, attackers inject malicious instructions into the metadata of MCP tools (such as tool descriptions or parameters). Since large language models (LLMs) rely on this metadata to decide which tools to invoke, compromised descriptions can trick the model into executing unauthorised tool calls or bypassing security controls. These manipulations are often invisible to end users but can be interpreted and acted upon by the AI system. This risk is heightened in hosted MCP server environments, where tool definitions can be updated after user approval—a scenario sometimes referred to as a "[rug pull](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)". In such cases, a tool that was previously safe may later be modified to perform malicious actions, such as exfiltrating data or altering system behaviour, without the user's knowledge. For more on this attack vector, see [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![tool-injection-lg-2048x1239 (1)](../images/02-Security/tool-injection.png)

## Risks
Unintended AI actions present a variety of security risks, including data exfiltration and privacy breaches.

### Mitigating Controls

#### Using Prompt Shields to Protect Against Indirect Prompt Injection Attacks

**AI Prompt Shields** are a solution developed by Microsoft to defend against both direct and indirect prompt injection attacks. They help through:

1.  **Detection and Filtering:** Prompt Shields use advanced machine learning algorithms and natural language processing to detect and filter out malicious instructions embedded in external content, such as documents, web pages, or emails.
2.  **Spotlighting:** This technique helps the AI system distinguish between valid system instructions and potentially untrustworthy external inputs. By transforming the input text in a way that makes it more relevant to the model, Spotlighting ensures that the AI can better identify and ignore malicious instructions.
3.  **Delimiters and Datamarking:** Including delimiters in the system message explicitly outlines the location of the input text, helping the AI system recognise and separate user inputs from potentially harmful external content. Datamarking extends this concept by using special markers to highlight the boundaries of trusted and untrusted data.
4.  **Continuous Monitoring and Updates:** Microsoft continuously monitors and updates Prompt Shields to address new and evolving threats. This proactive approach ensures that the defenses remain effective against the latest attack techniques.
5. **Integration with Azure Content Safety:** Prompt Shields are part of the broader Azure AI Content Safety suite, which provides additional tools for detecting jailbreak attempts, harmful content, and other security risks in AI applications.

You can read more about AI Prompt Shields in the [Prompt Shields documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection).

![prompt-shield-lg-2048x1328](../images/02-Security/prompt-shield.png)

### Supply Chain Security

Supply chain security remains fundamental in the AI era, but the scope of what constitutes your supply chain has expanded. In addition to traditional code packages, you must now rigorously verify and monitor all AI-related components, including foundation models, embedding services, context providers, and third-party APIs. Each of these can introduce vulnerabilities or risks if not properly managed.

**Key supply chain security practices for AI and MCP:**
- **Verify all components before integration:** This includes not just open-source libraries, but also AI models, data sources, and external APIs. Always check for provenance, licensing, and known vulnerabilities.
- **Maintain secure deployment pipelines:** Use automated CI/CD pipelines with integrated security scanning to catch issues early. Ensure that only trusted artefacts are deployed to production.
- **Continuously monitor and audit:** Implement ongoing monitoring for all dependencies, including models and data services, to detect new vulnerabilities or supply chain attacks.
- **Apply least privilege and access controls:** Restrict access to models, data, and services to only what is necessary for your MCP server to function.
- **Respond quickly to threats:** Have a process in place for patching or replacing compromised components, and for rotating secrets or credentials if a breach is detected.

[GitHub Advanced Security](https://github.com/security/advanced-security) provides features such as secret scanning, dependency scanning, and CodeQL analysis. These tools integrate with [Azure DevOps](https://azure.microsoft.com/en-us/products/devops) and [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/) to help teams identify and mitigate vulnerabilities across both code and AI supply chain components.

Microsoft also implements extensive internal supply chain security practices for all products. Learn more in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).

# Established Security Best Practices That Will Uplift Your MCP Implementation's Security Posture

Any MCP implementation inherits the existing security posture of your organisation's environment that which it is built. When considering the security of MCP as a component of your overall AI systems, it is recommended that you look at uplifting your overall existing security posture. The following established security controls are especially pertinent:

- Secure coding best practices in your AI application—protect against [the OWASP Top 10](https://owasp.org/www-project-top-ten/), the [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559), use secure vaults for secrets and tokens, implement end-to-end secure communications between all application components, etc.
- Server hardening—use MFA where possible, keep patching up to date, integrate the server with a third-party identity provider for access, etc.
- Keep devices, infrastructure, and applications up to date with patches.
- Security monitoring—implement logging and monitoring of an AI application (including the MCP client/servers) and send those logs to a central SIEM for detection of anomalous activities.
- Zero trust architecture—isolating components via network and identity controls in a logical manner to minimise lateral movement if an AI application were compromised.

# Key Takeaways

- Security fundamentals remain critical: Secure coding, least privilege, supply chain verification, and continuous monitoring are essential for MCP and AI workloads.
- MCP introduces new risks, such as prompt injection, tool poisoning, and excessive permissions, that require both traditional and AI-specific controls.
- Use robust authentication, authorization, and token management practices, leveraging external identity providers like Microsoft Entra ID where possible.
- Protect against indirect prompt injection and tool poisoning by validating tool metadata, monitoring for dynamic changes, and using solutions like Microsoft Prompt Shields.
- Treat all components in your AI supply chain—including models, embeddings, and context providers—with the same rigour as code dependencies.
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
- [Using Microsoft Entra ID to Authenticate with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

### Next

Next: [Chapter 3: Getting Started](/03-GettingStarted/README.md)

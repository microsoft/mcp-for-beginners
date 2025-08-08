# Security Best Practices

[![MCP Security Best Practices](../images/video-thumbnails/03.png)](https://youtu.be/88No8pw706o)

_(Click the image above to view video of this lesson)_

Because security is such an important aspect, we prioritize it as our second section. This is in keeping with the **Secure by design** principle of Microsoft's [Secure Future Initiative](https://www.microsoft.com/en-us/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Adopting the Model Context Protocol (MCP) brings powerful new capabilities to AI-driven applications, but also introduces unique security challenges that extend beyond traditional software risks. In addition to established concerns like secure coding, least privilege, and supply chain security, MCP and AI workloads face new threats such as prompt injection, tool poisoning, dynamic tool modification, session hijacking, confused deputy attacks, and token passthrough vulnerabilities. These risks can lead to data exfiltration, privacy breaches, and unintended system behavior if not properly managed.

This lesson explores the most relevant security risks associated with MCP—including authentication, authorization, excessive permissions, indirect prompt injection, session security, confused deputy problems, token passthrough vulnerabilities, and supply chain vulnerabilities—and provides actionable controls and best practices to mitigate them. You'll also learn how to leverage Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to strengthen your MCP implementation. By understanding and applying these controls, you can significantly reduce the likelihood of a security breach and ensure your AI systems remain robust and trustworthy.

# Learning Objectives

By the end of this lesson, you will be able to:

- Identify and explain the unique security risks introduced by the Model Context Protocol (MCP), including prompt injection, tool poisoning, excessive permissions, session hijacking, confused deputy problems, token passthrough vulnerabilities, and supply chain vulnerabilities.
- Describe and apply effective mitigating controls for MCP security risks, such as robust authentication, least privilege, secure token management, session security controls, and supply chain verification.
- Understand and leverage Microsoft solutions like Prompt Shields, Azure Content Safety, and GitHub Advanced Security to protect MCP and AI workloads.
- Recognize the importance of validating tool metadata, monitoring for dynamic changes, defending against indirect prompt injection attacks, and preventing session hijacking.
- Integrate established security best practices—such as secure coding, server hardening, and zero trust architecture—into your MCP implementation to reduce the likelihood and impact of security breaches.

# MCP security controls

Any system which has access to important resources has implied security challenges. Security challenges can generally be addressed through correct application of fundamental security controls and concepts.  As MCP is only newly defined, the specification is changing very rapidly and as the protocol evolves. Eventually the security controls within it will mature, enabling a better integration with enterprise and established security architectures and best practices.

Research published in the [Microsoft Digital Defense Report](https://aka.ms/mddr) states that 98% of reported breaches would be prevented by robust security hygiene and the best protection against any kind of breach is to get your baseline security hygiene, secure coding best practices and supply chain security right -- those tried and tested practices that we already know about still make the most impact in reducing security risk.

Let's look at some of the ways that you can start to address security risks when adopting MCP.

> **Note:** The following information is correct as of **29th May 2025**. The MCP protocol is continually evolving, and future implementations may introduce new authentication patterns and controls. For the latest updates and guidance, always refer to the [MCP Specification](https://spec.modelcontextprotocol.io/) and the official [MCP GitHub repository](https://github.com/modelcontextprotocol) and [security best practice page](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices).

### Problem statement 
The original MCP specification assumed that developers would write their own authentication server. This required knowledge of OAuth and related security constraints. MCP servers acted as OAuth 2.0 Authorization Servers, managing the required user authentication directly rather than delegating it to an external service such as Microsoft Entra ID. As of **26 April 2025**, an update to the MCP specification allows for MCP servers to delegate user authentication to an external service.

### Risks
- Misconfigured authorization logic in the MCP server can lead to sensitive data exposure and incorrectly applied access controls.
- OAuth token theft on the local MCP server. If stolen, the token can then be used to impersonate the MCP server and access resources and data from the service that the OAuth token is for.

#### Token Passthrough
Token passthrough is explicitly forbidden in the authorization specification as it introduces a number of security risks, that include:

#### Security Control Circumvention
The MCP Server or downstream APIs might implement important security controls like rate limiting, request validation, or traffic monitoring, that depend on the token audience or other credential constraints. If clients can obtain and use tokens directly with the downstream APIs without the MCP server validating them properly or ensuring that the tokens are issued for the right service, they bypass these controls.

#### Accountability and Audit Trail Issues
The MCP Server will be unable to identify or distinguish between MCP Clients when clients are calling with an upstream-issued access token which may be opaque to the MCP Server.
The downstream Resource Server's logs may show requests that appear to come from a different source with a different identity, rather than the MCP server that is actually forwarding the tokens.
Both factors make incident investigation, controls, and auditing more difficult.
If the MCP Server passes tokens without validating their claims (e.g., roles, privileges, or audience) or other metadata, a malicious actor in possession of a stolen token can use the server as a proxy for data exfiltration.

#### Trust Boundary Issues
The downstream Resource Server grants trust to specific entities. This trust might include assumptions about origin or client behavior patterns. Breaking this trust boundary could lead to unexpected issues.
If the token is accepted by multiple services without proper validation, an attacker compromising one service can use the token to access other connected services.

#### Future Compatibility Risk
Even if an MCP Server starts as a "pure proxy" today, it might need to add security controls later. Starting with proper token audience separation makes it easier to evolve the security model.

### Mitigating controls

**MCP servers MUST NOT accept any tokens that were not explicitly issued for the MCP server**

- **Review and Harden Authorization Logic:** Carefully audit your MCP server's authorization implementation to ensure only intended users and clients can access sensitive resources. For practical guidance, see [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) and [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/).
- **Enforce Secure Token Practices:** Follow [Microsoft's best practices for token validation and lifetime](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) to prevent misuse of access tokens and reduce the risk of token replay or theft.
- **Protect Token Storage:** Always store tokens securely and use encryption to safeguard them at rest and in transit. For implementation tips, see [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2).


# Excessive permissions for MCP servers

### Problem statement
MCP servers may have been granted excessive permissions to the service/resource they are accessing. For example, an MCP server that is part of an AI sales application connecting to an enterprise data store should have access scoped to the sales data and not allowed to access all the files in the store. Referencing back to the principle of least privilege (one of the oldest security principles), no resource should have permissions in excess of what is required for it to execute the tasks it was intended for. AI presents an increased challenge in this space because to enable it to be flexible, it can be challenging to define the exact permissions required.

### Risks 
- Granting excessive permissions can allow for exfiltration or amending data that the MCP server was not intended to be able to access. This could also be a privacy issue if the data is personally identifiable information (PII).

### Mitigating controls
- **Apply the Principle of Least Privilege:** Grant the MCP server only the minimum permissions necessary to perform its required tasks. Regularly review and update these permissions to ensure they do not exceed what is needed. For detailed guidance, see [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access).
- **Use Role-Based Access Control (RBAC):** Assign roles to the MCP server that are tightly scoped to specific resources and actions, avoiding broad or unnecessary permissions.
- **Monitor and Audit Permissions:** Continuously monitor permission usage and audit access logs to detect and remediate excessive or unused privileges promptly.

# Indirect prompt injection attacks

### Problem statement

Malicious or compromised MCP servers can introduce significant risks by exposing customer data or enabling unintended actions. These risks are especially relevant in AI and MCP-based workloads, where:

- **Prompt Injection Attacks**: Attackers embed malicious instructions in prompts or external content, causing the AI system to perform unintended actions or leak sensitive data. Learn more: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- **Tool Poisoning**: Attackers manipulate tool metadata (such as descriptions or parameters) to influence the AI's behavior, potentially bypassing security controls or exfiltrating data. Details: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- **Cross-Domain Prompt Injection**: Malicious instructions are embedded in documents, web pages, or emails, which are then processed by the AI, leading to data leakage or manipulation.
- **Dynamic Tool Modification (Rug Pulls)**: Tool definitions can be changed after user approval, introducing new malicious behaviors without user awareness.

These vulnerabilities highlight the need for robust validation, monitoring, and security controls when integrating MCP servers and tools into your environment. For a deeper dive, see the linked references above.

![prompt-injection-lg-2048x1034](../images/02-Security/prompt-injection.png)

**Indirect Prompt Injection** (also known as cross-domain prompt injection or XPIA) is a critical vulnerability in generative AI systems, including those using the Model Context Protocol (MCP). In this attack, malicious instructions are hidden within external content—such as documents, web pages, or emails. When the AI system processes this content, it may interpret the embedded instructions as legitimate user commands, resulting in unintended actions like data leakage, generation of harmful content, or manipulation of user interactions. For a detailed explanation and real-world examples, see [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

A particularly dangerous form of this attack is **Tool Poisoning**. Here, attackers inject malicious instructions into the metadata of MCP tools (such as tool descriptions or parameters). Since large language models (LLMs) rely on this metadata to decide which tools to invoke, compromised descriptions can trick the model into executing unauthorized tool calls or bypassing security controls. These manipulations are often invisible to end users but can be interpreted and acted upon by the AI system. This risk is heightened in hosted MCP server environments, where tool definitions can be updated after user approval—a scenario sometimes referred to as a "[rug pull](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)". In such cases, a tool that was previously safe may later be modified to perform malicious actions, such as exfiltrating data or altering system behavior, without the user's knowledge. For more on this attack vector, see [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).


![tool-injection-lg-2048x1239 (1)](../images/02-Security/tool-injection.png)


## Risks
Unintended AI actions present a variety of security risks that include data exfiltration and privacy breaches.

### Mitigating controls
### Using prompt shields to protect against Indirect Prompt Injection attacks
-----------------------------------------------------------------------------

**AI Prompt Shields** are a solution developed by Microsoft to defend against both direct and indirect prompt injection attacks. They help through:

1.  **Detection and Filtering**: Prompt Shields use advanced machine learning algorithms and natural language processing to detect and filter out malicious instructions embedded in external content, such as documents, web pages, or emails.
    
2.  **Spotlighting**: This technique helps the AI system distinguish between valid system instructions and potentially untrustworthy external inputs. By transforming the input text in a way that makes it more relevant to the model, Spotlighting ensures that the AI can better identify and ignore malicious instructions.
    
3.  **Delimiters and Datamarking**: Including delimiters in the system message explicitly outlines the location of the input text, helping the AI system recognize and separate user inputs from potentially harmful external content. Datamarking extends this concept by using special markers to highlight the boundaries of trusted and untrusted data.
    
4.  **Continuous Monitoring and Updates**: Microsoft continuously monitors and updates Prompt Shields to address new and evolving threats. This proactive approach ensures that the defenses remain effective against the latest attack techniques.
    
5. **Integration with Azure Content Safety:** Prompt Shields are part of the broader Azure AI Content Safety suite, which provides additional tools for detecting jailbreak attempts, harmful content, and other security risks in AI applications.

You can read more about AI prompt shields in the [Prompt Shields documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection).

![prompt-shield-lg-2048x1328](../images/02-Security/prompt-shield.png)


# Confused Deputy Problem

### Problem statement

The confused deputy problem is a security vulnerability that occurs when an MCP server acts as a proxy between MCP clients and third-party APIs. This vulnerability can be exploited when the MCP server uses a static client ID to authenticate with a third-party authorization server that lacks dynamic client registration support.

### Risks

- **Cookie-based consent bypass**: If a user has previously authenticated through the MCP proxy server, a third-party authorization server may set a consent cookie in the user's browser. An attacker can later exploit this by sending the user a malicious link with a crafted authorization request containing a malicious redirect URI.
- **Authorization code theft**: When the user clicks the malicious link, the third-party authorization server may skip the consent screen due to the existing cookie, and the authorization code could be redirected to the attacker's server.
- **Unauthorized API access**: The attacker can exchange the stolen authorization code for access tokens and impersonate the user to access the third-party API without explicit approval.

### Mitigating controls

- **Explicit consent requirements**: MCP proxy servers using static client IDs **MUST** obtain user consent for each dynamically registered client before forwarding to third-party authorization servers.
- **Proper OAuth implementation**: Follow OAuth 2.1 security best practices, including using code challenges (PKCE) for authorization requests to prevent interception attacks.
- **Client validation**: Implement strict validation of redirect URIs and client identifiers to prevent exploitation by malicious actors.


# Token Passthrough Vulnerabilities

### Problem statement

"Token passthrough" is an anti-pattern where an MCP server accepts tokens from an MCP client without validating that the tokens were properly issued to the MCP server itself, and then "passes them through" to downstream APIs. This practice explicitly violates the MCP authorization specification and introduces serious security risks.

### Risks

- **Security Control Circumvention**: Clients could bypass important security controls like rate limiting, request validation, or traffic monitoring if they can use tokens directly with downstream APIs without proper validation.
- **Accountability and Audit Trail Issues**: The MCP server will be unable to identify or distinguish between MCP clients when clients use upstream-issued access tokens, making incident investigation and auditing more difficult.
- **Data Exfiltration**: If tokens are passed without proper claims validation, a malicious actor with a stolen token could use the server as a proxy for data exfiltration.
- **Trust Boundary Violations**: Downstream resource servers may grant trust to specific entities with assumptions about origin or behavior patterns. Breaking this trust boundary could lead to unexpected security issues.
- **Multi-service Token Misuse**: If tokens are accepted by multiple services without proper validation, an attacker compromising one service could use the token to access other connected services.

### Mitigating controls

- **Token validation**: MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server itself.
- **Audience verification**: Always validate that tokens have the correct audience claim that matches the MCP server's identity.
- **Proper token lifecycle management**: Implement short-lived access tokens and proper token rotation practices to reduce the risk of token theft and misuse.


# Session Hijacking

### Problem statement

Session hijacking is an attack vector where a client is provided a session ID by the server, and an unauthorized party obtains and uses that same session ID to impersonate the original client and perform unauthorized actions on their behalf. This is particularly concerning in stateful HTTP servers handling MCP requests.

### Risks

- **Session Hijack Prompt Injection**: An attacker who obtains a session ID could send malicious events to a server that shares session state with the server the client is connected to, potentially triggering harmful actions or accessing sensitive data.
- **Session Hijack Impersonation**: An attacker with a stolen session ID could make calls directly to the MCP server, bypassing authentication and being treated as the legitimate user.
- **Compromised Resumable Streams**: When a server supports redelivery/resumable streams, an attacker could terminate a request prematurely, leading to it being resumed later by the original client with potentially malicious content.

### Mitigating controls

- **Authorization verification**: MCP servers that implement authorization **MUST** verify all inbound requests and **MUST NOT** use sessions for authentication.
- **Secure session IDs**: MCP servers **MUST** use secure, non-deterministic session IDs generated with secure random number generators. Avoid predictable or sequential identifiers.
- **User-specific session binding**: MCP servers **SHOULD** bind session IDs to user-specific information, combining the session ID with information unique to the authorized user (like their internal user ID) using a format like `<user_id>:<session_id>`.
- **Session expiration**: Implement proper session expiration and rotation to limit the window of vulnerability if a session ID is compromised.
- **Transport security**: Always use HTTPS for all communication to prevent session ID interception.


# Supply chain security

Supply chain security remains fundamental in the AI era, but the scope of what constitutes your supply chain has expanded. In addition to traditional code packages, you must now rigorously verify and monitor all AI-related components, including foundation models, embeddings services, context providers, and third-party APIs. Each of these can introduce vulnerabilities or risks if not properly managed.

**Key supply chain security practices for AI and MCP:**
- **Verify all components before integration:** This includes not just open-source libraries, but also AI models, data sources, and external APIs. Always check for provenance, licensing, and known vulnerabilities.
- **Maintain secure deployment pipelines:** Use automated CI/CD pipelines with integrated security scanning to catch issues early. Ensure that only trusted artifacts are deployed to production.
- **Continuously monitor and audit:** Implement ongoing monitoring for all dependencies, including models and data services, to detect new vulnerabilities or supply chain attacks.
- **Apply least privilege and access controls:** Restrict access to models, data, and services to only what is necessary for your MCP server to function.
- **Respond quickly to threats:** Have a process in place for patching or replacing compromised components, and for rotating secrets or credentials if a breach is detected.

[GitHub Advanced Security](https://github.com/security/advanced-security) provides features such as secret scanning, dependency scanning, and CodeQL analysis. These tools integrate with [Azure DevOps](https://azure.microsoft.com/en-us/products/devops) and [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/) to help teams identify and mitigate vulnerabilities across both code and AI supply chain components.

Microsoft also implements extensive supply chain security practices internally for all products. Learn more in [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


# Established security best practices that will uplift your MCP implementation's security posture

Any MCP implementation inherits the existing security posture of your organization's environment that it is built upon, so when considering the security of MCP as a component of your overall AI systems it is recommended that you look at uplifting your overall existing security posture. The following established security controls are especially pertinent:

-   Secure coding best practices in your AI application - protect against [the OWASP Top 10](https://owasp.org/www-project-top-ten/), the [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559), use of secure vaults for secrets and tokens, implementing end-to-end secure communications between all application components, etc.
-   Server hardening -- use MFA where possible, keep patching up to date, integrate the server with a third party identity provider for access, etc.
-   Keep devices, infrastructure and applications up to date with patches
-   Security monitoring -- implementing logging and monitoring of an AI application (including the MCP client/servers) and sending those logs to a central SIEM for detection of anomalous activities
-   Zero trust architecture -- isolating components via network and identity controls in a logical manner to minimize lateral movement if an AI application were compromised.

# Key Takeaways

- Security fundamentals remain critical: Secure coding, least privilege, supply chain verification, and continuous monitoring are essential for MCP and AI workloads.
- MCP introduces new risks—such as prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, and excessive permissions—that require both traditional and AI-specific controls.
- Use robust authentication, authorization, and token management practices, leveraging external identity providers like Microsoft Entra ID where possible.
- Protect against indirect prompt injection and tool poisoning by validating tool metadata, monitoring for dynamic changes, and using solutions like Microsoft Prompt Shields.
- Implement secure session management by using non-deterministic session IDs, binding sessions to user identities, and never using sessions for authentication.
- Prevent confused deputy attacks by requiring explicit user consent for each dynamically registered client and implementing proper OAuth security practices.
- Avoid token passthrough vulnerabilities by ensuring that MCP servers only accept tokens explicitly issued for them and validate token claims appropriately.
- Treat all components in your AI supply chain—including models, embeddings, and context providers—with the same rigor as code dependencies.
- Stay current with evolving MCP specifications and contribute to the community to help shape secure standards.

# Additional Resources

## External Resources
- [Microsoft Digital Defense Report](https://aka.ms/mddr)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/draft/basic/authorization)
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
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

## Additional Security Documents

For more detailed security guidance, please refer to these documents:

- [MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md) - Comprehensive list of security best practices for MCP implementations
- [Azure Content Safety Implementation](./azure-content-safety-implementation.md) - Implementation examples for integrating Azure Content Safety with MCP servers
- [MCP Security Controls 2025](./mcp-security-controls-2025.md) - Latest security controls and techniques for securing MCP deployments
- [MCP Best Practices](./mcp-best-practices.md) - Quick reference guide for MCP security

### Next 

Next: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

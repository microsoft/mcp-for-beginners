# Overview

Introducing any new technology can introduce new security challenges or exacerbate existing security risks. In this lesson, we're going to look at some of the security risks that could be introduced to your environment when using Model Context Protocol (MCP), and what controls you can put in place to mitigate them.

# Learning Objectives

By the end of this lesson, you will:

-   Understand some of the security risks inherent in the MCP specification 
-   Explain some of the mitigating controls that can be implemented to reduce security risks when using MCP
-   Understand why established security best practices are the most effective way to reduce the likelihood of a security breach

# MCP security controls

Any system which has access to important resources has implied security challenges. Security challenges can generally be addressed through correct application of fundamental security controls and concepts.  As MCP is only newly defined, the specification is changing very rapidly and as the protocol evolves. Eventually the security controls within it will mature, enabling a better integration with enterprise and established security architectures and best practices.

Research published in the [Microsoft Digital Defense Report](https://aka.ms/mddr) states that 98% of reported breaches would be prevented by robust security hygiene and the best protection against any kind of breach is to get your baseline security hygiene, secure coding best practices and supply chain security right -- those tried and tested practices that we already know about still make the most impact in reducing security risk.

Let's look at some of the ways that you can start to address security risks when adopting MCP.

# MCP server authentication

### Problem statement 
At the time of writing, the MCP specification assumes that developers will to write their own authentication server. This requires knowledge of OAuth and related security constraints. MCP servers act as OAuth 2.0 Authorization Servers, managing the required user authentication directly rather than delegating it to an external service such as Microsoft Entra ID.

### Risks
- Misconfigured authorization logic in the MCP server can lead to sensitive data exposure and incorrectly applied access controls.
- OAuth token theft on the local MCP server . If stolen, the token can then be used to impersonate the MCP server and access resources and data from the service that the OAuth token is for.

### Mitigating controls
-   Thoroughly review your MCP server authorization logic, here some posts discussing this in more detail - [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) and [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/)
-   Implement [best practices for token validation and lifetime](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
-   [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

*At the time of writing, an RFC has been proposed to change MCP servers from OAuth Providers (OP) to Resource Providers (RP) that use an external identity provider (IdP) as the "golden path". This would enable MCP servers to be integrated with third-party identity providers which provide stronger security controls and abstract the OAuth token storage and management away from the MCP server. You can contribute to and view this RFC [here](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/284).*

# Excessive permissions for MCP servers

### Problem statement
MCP servers may have been granted excessive permissions to the service/resource they are accessing. For example, an MCP server that is part of an AI sales application connecting to an enterprise data store should have access scoped to the sales data and not allowed to access all the files in the store. Referencing back to the principle of least privilege (one of the oldest security principles), no resource should have permissions in excess of what is required for it to execute the tasks it was intended for. AI presents an increased challenge in this space because to enable it to be flexible, it can be challenging to define the exact permissions required.

### Risks 
- Granting excessive permissions can allow for exfiltration or amending data that the MCP server was not intended to be able to access. This could also be a privacy issue if the data is personally identifiable information (PII).

### Mitigating controls
-   Clearly define the permissions that the MCP server has to access the resource/service it connects to. [These permissions should be the minimum required for the MCP server to access the tool or data it is connecting to](https://learn.microsoft.com/en-us/entra/identity-platform/secure-least-privileged-access).

# Indirect prompt injection attacks

### Problem statement
Researchers have shown that the Model Context Protocol (MCP) is vulnerable to a subset of Indirect Prompt Injection attacks known as Tool Poisoning Attacks. Tool poisoning is a scenario where an attacker embeds malicious instructions within the descriptions of MCP tools. These instructions are invisible to users but can be interpreted by the AI model and its underlying systems, leading to unintended actions that could ultimately lead to harmful outcomes.

### Risks
Unintended AI actions present a variety of security risks that include data exfiltration and privacy breaches.

### Mitigating controls
-   Implement AI prompt shields: in Azure AI Foundry, you can follow [these](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-jailbreak?pivots=programming-language-foundry-portal) steps to implement AI prompt shields.
-   Implement robust supply chain security: you can read more about how Microsoft implements supply chain security internally [here](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).

# Established security best practices that will uplift your MCP implementation's security posture

Any MCP implementation inherits the existing security posture of your organization's environment that it is built upon, so when considering the security of MCP as a component of your overall AI systems it is recommended that you look at uplifting your overall existing security posture. The following established security controls are especially pertinent:

-   Secure coding best practices in your AI application - protect against [the OWASP Top 10](https://owasp.org/www-project-top-ten/), the [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559), use of secure vaults for secrets and tokens, implementing end-to-end secure communications between all application components, etc.
-   Server hardening -- use MFA where possible, keep patching up to date, integrate the server with a third party identity provider for access, etc.
-   Keep devices, infrastructure and applications up to date with patches
-   Security monitoring -- implementing logging and monitoring of an AI application (including the MCP client/servers) and sending those logs to a central SIEM for detection of anomalous activities
-   Zero trust architecture -- isolating components via network and identity controls in a logical manner to minimize lateral movement if an AI application were compromised.

# Key Takeaways

- As developers embrace this new approach to integrating their organization's APIs and connectors into LLMs, they need to be aware of security risks and how to implement controls to reduce those risks. 
- There are mitigating security controls that can be put in place to reduce the risks inherent in the current MCP specification.
- As the protocol develops expect that some of the risks will reduce or disappear entirely. 
- We encourage you to contribute to and suggest security related MCP RFCs to make this protocol even better!

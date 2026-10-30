# MCP Security Best Practices - September 2026 Update

> **Important:** Dis dokument dey reflect
> [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> and di official
> [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Hands-On Security Training

For practical implementation experience, we recommend di **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - na comprehensive guided expedition wey teach how to secure MCP servers for Azure. Di workshop dey cover all OWASP MCP Top 10 risks wit one "vulnerable → exploit → fix → validate" methodology.

All practices for dis dokument dey align wit di **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** for Azure-specific implementation guidance.

## Essential Security Practices for MCP Implementations

Di Model Context Protocol bring special security wahala wey pass normal software security. Dem practices for here dey cover di foundational requirements and MCP-specific threats like prompt injection, tool poisoning, state-handle hijacking, confused deputy problems, and token passthrough vulnerabilities.





### **MANDATORY Security Requirements** 

**Critical Requirements from MCP Specification:**

> **MUST NOT**: MCP servers **MUST NOT** accept any tokens wey no bin explicitly issued for di MCP server
> 
> **MUST**: MCP servers wey dey implement authorization **MUST** verify ALL inbound requests
>  
> **MUST NOT**: MCP servers **MUST NOT** use sessions for authentication
>
> **MUST**: MCP proxy servers wey dey use a static third-party client ID **MUST**
> obtain consent for each MCP client before forward authorization

---

## 1. **Token Security & Authentication**

**Authentication & Authorization Controls:**
   - **Rigorous Authorization Review**: Do comprehensive audits of MCP server authorization logic to make sure only di intended users and clients fit access resources
   - **External Identity Provider Integration**: Use established identity providers like Microsoft Entra ID instead of building custom authentication
   - **Token Audience Validation**: Always check say tokens bin explicitly issued for your MCP server - no accept upstream tokens
   - **Proper Token Lifecycle**: Put secure token rotation, expiration policies, and prevent token replay attacks

**Protected Token Storage:**
   - Use Azure Key Vault or similar secure credential stores for all secrets
   - Implement encryption for tokens both at rest and in transit
   - Do regular credential rotation and monitor for unauthorized access

## 2. **State Handle & Transport Security**

**Secure Application State Practices:**

- **Opaque State Handles**: Use secure, non-deterministic handles for
   application state wey span requests
- **User-Specific Binding**: Bind handles server-side to di authenticated
   principal and reject any cross-user reuse
- **Lifecycle Management**: Expire and revoke handles to limit di vulnerability
   window
- **Per-request Authorization**: No ever treat a state handle as authentication;
   authorize every request wey present am

**Transport Layer Security:**

- Require HTTPS for remote HTTP transports for production
- Use process isolation and environment credentials for local stdio servers
- Configure modern TLS wit proper certificate rotation and validation

## 3. **AI-Specific Threat Protection** 🤖

**Prompt Injection Defense:**
   - **Microsoft Prompt Shields**: Deploy AI Prompt Shields for advanced detection and filtering of malicious instructions
   - **Input Sanitization**: Validate and sanitize all inputs to prevent injection attacks and confused deputy problems
   - **Content Boundaries**: Use delimiter and datamarking systems to separate trusted instructions from outside content

**Tool Poisoning Prevention:**
   - **Tool Metadata Validation**: Put integrity checks for tool definitions and watch for unexpected changes
   - **Dynamic Tool Monitoring**: Monitor runtime behavior and set alerts for unexpected execution patterns
   - **Approval Workflows**: Require explicit user approval before tool modifications or capability changes

## 4. **Access Control & Permissions**

**Principle of Least Privilege:**
   - Grant MCP servers only minimum permissions wey dem need for di intended functionality
   - Implement role-based access control (RBAC) wit fine-grained permissions
   - Do regular permission reviews and continuous monitoring for privilege escalation

**Runtime Permission Controls:**
   - Apply resource limits to prevent resource exhaustion attacks
   - Use container isolation for tool execution environments  
   - Implement just-in-time access for administrative functions

## 5. **Content Safety & Monitoring**

**Content Safety Implementation:**
   - **Azure Content Safety Integration**: Use Azure Content Safety to detect harmful content, jailbreak attempts, and policy violations
   - **Behavioral Analysis**: Implement runtime behavioral monitoring to detect anomalies for MCP server and tool execution
   - **Comprehensive Logging**: Log all authentication attempts, tool invocations, and security events with secure, tamper-proof storage

**Continuous Monitoring:**
   - Real-time alerting for suspicious patterns and unauthorized access attempts  
   - Integrate wit SIEM systems for centralized security event management
   - Do regular security audits and penetration testing of MCP implementations

## 6. **Supply Chain Security**

**Component Verification:**
   - **Dependency Scanning**: Use automated vulnerability scanning for all software dependencies and AI components
   - **Provenance Validation**: Verify di origin, licensing, and integrity of models, data sources, and external services
   - **Signed Packages**: Use cryptographically signed packages and verify signatures before deployment

**Secure Development Pipeline:**
   - **GitHub Advanced Security**: Implement secret scanning, dependency analysis, and CodeQL static analysis
   - **CI/CD Security**: Integrate security validation throughout automated deployment pipelines
   - **Artifact Integrity**: Implement cryptographic verification for deployed artifacts and configurations

## 7. **OAuth Security & Confused Deputy Prevention**

**OAuth 2.1 Implementation:**
   - **PKCE Implementation**: Use Proof Key for Code Exchange (PKCE) for all authorization requests
    - **Client Registration**: Prefer Client ID Metadata Documents or
       pre-registration; use deprecated Dynamic Client Registration only as a
       compatibility fallback
    - **Explicit Consent**: MCP proxies wey dey use a static third-party client ID must
       obtain consent for each MCP client before forward authorization
   - **Redirect URI Validation**: Implement strict validation of redirect URIs and client identifiers

**Proxy Security:**
   - Prevent authorization bypass through static client ID exploitation
   - Implement proper consent workflows for third-party API access
   - Monitor for authorization code theft and unauthorized API access

## 8. **Incident Response & Recovery**

**Rapid Response Capabilities:**
   - **Automated Response**: Implement automated systems for credential rotation and threat containment
   - **Rollback Procedures**: Make sure you fit quickly revert to known-good configurations and components
   - **Forensic Capabilities**: Keep detailed audit trails and logging for incident investigation

**Communication & Coordination:**
   - Clear escalation procedures for security incidents
   - Integrate wit organizational incident response teams
   - Do regular security incident simulations and tabletop exercises

## 9. **Compliance & Governance**

**Regulatory Compliance:**
   - Ensure MCP implementations meet industry-specific requirements (GDPR, HIPAA, SOC 2)
   - Implement data classification and privacy controls for AI data processing
   - Maintain comprehensive documentation for compliance auditing

**Change Management:**
   - Formal security review processes for all MCP system modifications
   - Version control and approval workflows for configuration changes
   - Do regular compliance assessments and gap analysis

## 10. **Advanced Security Controls**

**Zero Trust Architecture:**
   - **Never Trust, Always Verify**: Continuous verification of users, devices, and connections
   - **Micro-segmentation**: Granular network controls to isolate individual MCP components
   - **Conditional Access**: Risk-based access controls wey adapt to current context and behavior

**Runtime Application Protection:**
   - **Runtime Application Self-Protection (RASP)**: Deploy RASP techniques for real-time threat detection
   - **Application Performance Monitoring**: Monitor for performance anomalies wey fit indicate attacks
   - **Dynamic Security Policies**: Implement security policies wey fit adapt based on current threat landscape

## 11. **Microsoft Security Ecosystem Integration**

**Comprehensive Microsoft Security:**
   - **Microsoft Defender for Cloud**: Cloud security posture management for MCP workloads
   - **Azure Sentinel**: Cloud-native SIEM and SOAR capabilities for advanced threat detection
   - **Microsoft Purview**: Data governance and compliance for AI workflows and data sources

**Identity & Access Management:**
   - **Microsoft Entra ID**: Enterprise identity management wit conditional access policies
   - **Privileged Identity Management (PIM)**: Just-in-time access and approval workflows for admin functions
   - **Identity Protection**: Risk-based conditional access and automated threat response

## 12. **Continuous Security Evolution**

**Staying Current:**
   - **Specification Monitoring**: Regular review of MCP specification updates and security guidance changes
   - **Threat Intelligence**: Integrate AI-specific threat feeds and indicators of compromise
   - **Security Community Engagement**: Take part for MCP security community and vulnerability disclosure programs

**Adaptive Security:**
   - **Machine Learning Security**: Use ML-based anomaly detection to identify new attack patterns
   - **Predictive Security Analytics**: Implement predictive models for proactive threat identification
   - **Security Automation**: Automate security policy updates based on threat intelligence and specification changes

---

## **Critical Security Resources**

### **Official MCP Documentation**
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Security Resources**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Comprehensive OWASP MCP Top 10 wit Azure implementation
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Official OWASP MCP security risks
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on security training for MCP on Azure

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Security Standards**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementation Guides**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Security notice:** MCP security practices dey change quick-quick. Always verify
> against di current [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/)
> and [official security documentation](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> before you implement.

## What's Next

- Read: [MCP Security Controls](./mcp-security-controls.md)
- Return to: [Security Module Overview](./README.md)
- Continue to: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
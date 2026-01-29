# MCP Security Controls - December 2025 Update

> **Current Standard**: Dis dokument dey reflect [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) security requirements and official [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Di Model Context Protocol (MCP) don mature well well wit beta security controls wey dey address both traditional software security and AI-specific threats. Dis dokument dey provide full security controls for secure MCP implementations as of December 2025.

## **MANDATORY Security Requirements**

### **Critical Prohibitions from MCP Specification:**

> **FORBIDDEN**: MCP servers **MUST NOT** accept any tokens wey dem no explicitly issue for di MCP server
>
> **PROHIBITED**: MCP servers **MUST NOT** use sessions for authentication  
>
> **REQUIRED**: MCP servers wey dey implement authorization **MUST** verify ALL inbound requests
>
> **MANDATORY**: MCP proxy servers wey dey use static client IDs **MUST** get user consent for every dynamically registered client

---

## 1. **Authentication & Authorization Controls**

### **External Identity Provider Integration**

**Current MCP Standard (2025-06-18)** allow MCP servers to delegate authentication to external identity providers, wey be big security improvement:

### **External Identity Provider Integration**

**Current MCP Standard (2025-11-25)** allow MCP servers to delegate authentication to external identity providers, wey be big security improvement:

**Security Benefits:**
1. **Eliminates Custom Authentication Risks**: E reduce vulnerability surface by no dey use custom authentication implementations
2. **Enterprise-Grade Security**: E use established identity providers like Microsoft Entra ID wey get advanced security features
3. **Centralized Identity Management**: E make user lifecycle management, access control, and compliance auditing easy
4. **Multi-Factor Authentication**: E inherit MFA capabilities from enterprise identity providers
5. **Conditional Access Policies**: E benefit from risk-based access controls and adaptive authentication

**Implementation Requirements:**
- **Token Audience Validation**: Verify say all tokens dem explicitly issue for di MCP server
- **Issuer Verification**: Validate say token issuer match di expected identity provider
- **Signature Verification**: Cryptographic validation of token integrity
- **Expiration Enforcement**: Strict enforcement of token lifetime limits
- **Scope Validation**: Make sure tokens get correct permissions for di requested operations

### **Authorization Logic Security**

**Critical Controls:**
- **Comprehensive Authorization Audits**: Regular security reviews of all authorization decision points
- **Fail-Safe Defaults**: Deny access when authorization logic no fit make clear decision
- **Permission Boundaries**: Clear separation between different privilege levels and resource access
- **Audit Logging**: Complete logging of all authorization decisions for security monitoring
- **Regular Access Reviews**: Periodic validation of user permissions and privilege assignments

## 2. **Token Security & Anti-Passthrough Controls**

### **Token Passthrough Prevention**

**Token passthrough na explicitly prohibited** for MCP Authorization Specification because e get critical security risks:

**Security Risks Addressed:**
- **Control Circumvention**: E bypass essential security controls like rate limiting, request validation, and traffic monitoring
- **Accountability Breakdown**: E make client identification impossible, spoil audit trails and incident investigation
- **Proxy-Based Exfiltration**: E allow bad people to use servers as proxies for unauthorized data access
- **Trust Boundary Violations**: E break downstream service trust assumptions about token origins
- **Lateral Movement**: Compromised tokens across many services fit enable bigger attack expansion

**Implementation Controls:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Secure Token Management Patterns**

**Best Practices:**
- **Short-Lived Tokens**: Make exposure window small with frequent token rotation
- **Just-in-Time Issuance**: Issue tokens only when dem need am for specific operations
- **Secure Storage**: Use hardware security modules (HSMs) or secure key vaults
- **Token Binding**: Bind tokens to specific clients, sessions, or operations where e possible
- **Monitoring & Alerting**: Real-time detection of token misuse or unauthorized access patterns

## 3. **Session Security Controls**

### **Session Hijacking Prevention**

**Attack Vectors Addressed:**
- **Session Hijack Prompt Injection**: Bad events wey dem inject inside shared session state
- **Session Impersonation**: Unauthorized use of stolen session IDs to bypass authentication
- **Resumable Stream Attacks**: Exploitation of server-sent event resumption for bad content injection

**Mandatory Session Controls:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Transport Security:**
- **HTTPS Enforcement**: All session communication must dey over TLS 1.3
- **Secure Cookie Attributes**: HttpOnly, Secure, SameSite=Strict
- **Certificate Pinning**: For critical connections to prevent MITM attacks

### **Stateful vs Stateless Considerations**

**For Stateful Implementations:**
- Shared session state need extra protection against injection attacks
- Queue-based session management need integrity verification
- Multiple server instances need secure session state synchronization

**For Stateless Implementations:**
- JWT or similar token-based session management
- Cryptographic verification of session state integrity
- Reduced attack surface but need strong token validation

## 4. **AI-Specific Security Controls**

### **Prompt Injection Defense**

**Microsoft Prompt Shields Integration:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Implementation Controls:**
- **Input Sanitization**: Full validation and filtering of all user inputs
- **Content Boundary Definition**: Clear separation between system instructions and user content
- **Instruction Hierarchy**: Proper precedence rules for conflicting instructions
- **Output Monitoring**: Detection of potentially harmful or manipulated outputs

### **Tool Poisoning Prevention**

**Tool Security Framework:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Dynamic Tool Management:**
- **Approval Workflows**: Explicit user consent for tool modifications
- **Rollback Capabilities**: Ability to revert to previous tool versions
- **Change Auditing**: Complete history of tool definition modifications
- **Risk Assessment**: Automated evaluation of tool security posture

## 5. **Confused Deputy Attack Prevention**

### **OAuth Proxy Security**

**Attack Prevention Controls:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Implementation Requirements:**
- **User Consent Verification**: No skip consent screens for dynamic client registration
- **Redirect URI Validation**: Strict whitelist-based validation of redirect destinations
- **Authorization Code Protection**: Short-lived codes with single-use enforcement
- **Client Identity Verification**: Strong validation of client credentials and metadata

## 6. **Tool Execution Security**

### **Sandboxing & Isolation**

**Container-Based Isolation:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Process Isolation:**
- **Separate Process Contexts**: Each tool execution dey for isolated process space
- **Inter-Process Communication**: Secure IPC mechanisms with validation
- **Process Monitoring**: Runtime behavior analysis and anomaly detection
- **Resource Enforcement**: Hard limits on CPU, memory, and I/O operations

### **Least Privilege Implementation**

**Permission Management:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Supply Chain Security Controls**

### **Dependency Verification**

**Comprehensive Component Security:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Continuous Monitoring**

**Supply Chain Threat Detection:**
- **Dependency Health Monitoring**: Continuous assessment of all dependencies for security issues
- **Threat Intelligence Integration**: Real-time updates on emerging supply chain threats
- **Behavioral Analysis**: Detection of unusual behavior in external components
- **Automated Response**: Immediate containment of compromised components

## 8. **Monitoring & Detection Controls**

### **Security Information and Event Management (SIEM)**

**Comprehensive Logging Strategy:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Real-Time Threat Detection**

**Behavioral Analytics:**
- **User Behavior Analytics (UBA)**: Detection of unusual user access patterns
- **Entity Behavior Analytics (EBA)**: Monitoring of MCP server and tool behavior
- **Machine Learning Anomaly Detection**: AI-powered identification of security threats
- **Threat Intelligence Correlation**: Matching observed activities against known attack patterns

## 9. **Incident Response & Recovery**

### **Automated Response Capabilities**

**Immediate Response Actions:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Forensic Capabilities**

**Investigation Support:**
- **Audit Trail Preservation**: Immutable logging with cryptographic integrity
- **Evidence Collection**: Automated gathering of relevant security artifacts
- **Timeline Reconstruction**: Detailed sequence of events wey lead to security incidents
- **Impact Assessment**: Evaluation of compromise scope and data exposure

## **Key Security Architecture Principles**

### **Defense in Depth**
- **Multiple Security Layers**: No single point of failure for security architecture
- **Redundant Controls**: Overlapping security measures for critical functions
- **Fail-Safe Mechanisms**: Secure defaults when systems get errors or attacks

### **Zero Trust Implementation**
- **Never Trust, Always Verify**: Continuous validation of all entities and requests
- **Principle of Least Privilege**: Minimal access rights for all components
- **Micro-Segmentation**: Granular network and access controls

### **Continuous Security Evolution**
- **Threat Landscape Adaptation**: Regular updates to address new threats
- **Security Control Effectiveness**: Ongoing evaluation and improvement of controls
- **Specification Compliance**: Alignment with evolving MCP security standards

---

## **Implementation Resources**

### **Official MCP Documentation**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Security Standards**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Important**: These security controls dey reflect di current MCP specification (2025-06-18). Always verify against di latest [official documentation](https://spec.modelcontextprotocol.io/) as standards dey continue to evolve fast fast.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) wey translate am. Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or no too correct. The original document wey e dey for im own language na the correct one. If na serious matter, e better make person wey sabi translate am well do am. We no go responsible if person no understand well or if dem use dis translation do mistake.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
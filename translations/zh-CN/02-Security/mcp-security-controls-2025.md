# MCP 安全控制 - 2025 年 12 月更新

> **当前标准**：本文档反映了 [MCP 规范 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) 的安全要求和官方 [MCP 安全最佳实践](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)。

模型上下文协议（MCP）已显著成熟，增强的安全控制涵盖了传统软件安全和 AI 特定威胁。本文档提供了截至 2025 年 12 月的安全 MCP 实施的全面安全控制。

## **强制性安全要求**

### **MCP 规范中的关键禁止事项：**

> **禁止**：MCP 服务器**不得**接受任何未明确为该 MCP 服务器签发的令牌  
>
> **禁止**：MCP 服务器**不得**使用会话进行身份验证  
>
> **要求**：实施授权的 MCP 服务器**必须**验证所有入站请求  
>
> **强制**：使用静态客户端 ID 的 MCP 代理服务器**必须**为每个动态注册的客户端获取用户同意

---

## 1. **身份验证与授权控制**

### **外部身份提供者集成**

**当前 MCP 标准（2025-06-18）**允许 MCP 服务器将身份验证委托给外部身份提供者，代表了显著的安全改进：

### **外部身份提供者集成**

**当前 MCP 标准（2025-11-25）**允许 MCP 服务器将身份验证委托给外部身份提供者，代表了显著的安全改进：

**安全优势：**  
1. **消除自定义身份验证风险**：通过避免自定义身份验证实现减少攻击面  
2. **企业级安全**：利用如 Microsoft Entra ID 等成熟身份提供者的高级安全功能  
3. **集中身份管理**：简化用户生命周期管理、访问控制和合规审计  
4. **多因素认证**：继承企业身份提供者的 MFA 功能  
5. **条件访问策略**：受益于基于风险的访问控制和自适应身份验证

**实施要求：**  
- **令牌受众验证**：验证所有令牌明确为 MCP 服务器签发  
- **签发者验证**：验证令牌签发者与预期身份提供者匹配  
- **签名验证**：对令牌完整性进行加密验证  
- **过期强制**：严格执行令牌生命周期限制  
- **权限范围验证**：确保令牌包含请求操作的适当权限

### **授权逻辑安全**

**关键控制：**  
- **全面授权审计**：定期对所有授权决策点进行安全审查  
- **安全失败默认**：授权逻辑无法做出明确决策时拒绝访问  
- **权限边界**：不同权限级别和资源访问的明确分离  
- **审计日志**：完整记录所有授权决策以便安全监控  
- **定期访问审查**：周期性验证用户权限和特权分配

## 2. **令牌安全与防透传控制**

### **禁止令牌透传**

MCP 授权规范明确禁止令牌透传，因其存在关键安全风险：

**解决的安全风险：**  
- **控制规避**：绕过速率限制、请求验证和流量监控等关键安全控制  
- **责任追踪中断**：无法识别客户端，破坏审计轨迹和事件调查  
- **代理型数据外泄**：恶意行为者利用服务器作为未经授权数据访问的代理  
- **信任边界破坏**：破坏下游服务对令牌来源的信任假设  
- **横向移动**：被攻破的令牌跨多个服务扩展攻击范围

**实施控制：**  
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

### **安全令牌管理模式**

**最佳实践：**  
- **短生命周期令牌**：通过频繁令牌轮换最小化暴露窗口  
- **即时发放**：仅在特定操作需要时发放令牌  
- **安全存储**：使用硬件安全模块（HSM）或安全密钥库  
- **令牌绑定**：尽可能将令牌绑定到特定客户端、会话或操作  
- **监控与告警**：实时检测令牌滥用或未经授权访问模式

## 3. **会话安全控制**

### **防止会话劫持**

**攻击向量：**  
- **会话劫持提示注入**：恶意事件注入共享会话状态  
- **会话冒充**：未经授权使用被盗会话 ID 绕过身份验证  
- **可恢复流攻击**：利用服务器发送事件恢复机制注入恶意内容

**强制会话控制：**  
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

**传输安全：**  
- **强制 HTTPS**：所有会话通信使用 TLS 1.3  
- **安全 Cookie 属性**：HttpOnly、Secure、SameSite=Strict  
- **证书绑定**：关键连接防止中间人攻击

### **有状态与无状态考虑**

**有状态实现：**  
- 共享会话状态需额外防护以防注入攻击  
- 基于队列的会话管理需完整性验证  
- 多服务器实例需安全同步会话状态

**无状态实现：**  
- 使用 JWT 或类似令牌管理会话  
- 会话状态完整性加密验证  
- 攻击面较小，但需强健的令牌验证

## 4. **AI 特定安全控制**

### **提示注入防御**

**Microsoft Prompt Shields 集成：**  
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

**实施控制：**  
- **输入清理**：全面验证和过滤所有用户输入  
- **内容边界定义**：系统指令与用户内容明确分离  
- **指令层级**：冲突指令的优先级规则  
- **输出监控**：检测潜在有害或被操控的输出

### **工具中毒防范**

**工具安全框架：**  
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

**动态工具管理：**  
- **审批工作流**：工具修改需明确用户同意  
- **回滚能力**：支持恢复至先前工具版本  
- **变更审计**：完整记录工具定义修改历史  
- **风险评估**：自动评估工具安全态势

## 5. **混淆代理攻击防范**

### **OAuth 代理安全**

**攻击防范控制：**  
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

**实施要求：**  
- **用户同意验证**：动态客户端注册绝不跳过同意界面  
- **重定向 URI 验证**：严格基于白名单验证重定向目标  
- **授权码保护**：短生命周期且单次使用授权码  
- **客户端身份验证**：强健验证客户端凭据和元数据

## 6. **工具执行安全**

### **沙箱与隔离**

**基于容器的隔离：**  
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

**进程隔离：**  
- **独立进程上下文**：每个工具执行在隔离进程空间  
- **进程间通信**：安全的 IPC 机制并进行验证  
- **进程监控**：运行时行为分析与异常检测  
- **资源限制**：CPU、内存和 I/O 操作的硬限制

### **最小权限实施**

**权限管理：**  
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

## 7. **供应链安全控制**

### **依赖项验证**

**全面组件安全：**  
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

### **持续监控**

**供应链威胁检测：**  
- **依赖健康监控**：持续评估所有依赖的安全问题  
- **威胁情报集成**：实时更新新兴供应链威胁  
- **行为分析**：检测外部组件异常行为  
- **自动响应**：立即遏制被攻破组件

## 8. **监控与检测控制**

### **安全信息与事件管理（SIEM）**

**全面日志策略：**  
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

### **实时威胁检测**

**行为分析：**  
- **用户行为分析（UBA）**：检测异常用户访问模式  
- **实体行为分析（EBA）**：监控 MCP 服务器和工具行为  
- **机器学习异常检测**：AI 驱动的安全威胁识别  
- **威胁情报关联**：将观察到的活动与已知攻击模式匹配

## 9. **事件响应与恢复**

### **自动响应能力**

**即时响应措施：**  
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

### **取证能力**

**调查支持：**  
- **审计轨迹保存**：不可篡改的加密完整日志  
- **证据收集**：自动收集相关安全证据  
- **时间线重建**：详细还原安全事件发生顺序  
- **影响评估**：评估妥协范围和数据暴露

## **关键安全架构原则**

### **纵深防御**  
- **多层安全防护**：安全架构无单点故障  
- **冗余控制**：关键功能重叠安全措施  
- **安全失败机制**：系统遇错或攻击时安全默认

### **零信任实施**  
- **永不信任，始终验证**：持续验证所有实体和请求  
- **最小权限原则**：所有组件最小访问权限  
- **微分段**：细粒度网络和访问控制

### **持续安全演进**  
- **威胁环境适应**：定期更新以应对新兴威胁  
- **安全控制有效性**：持续评估和改进控制措施  
- **规范合规**：与不断演进的 MCP 安全标准保持一致

---

## **实施资源**

### **官方 MCP 文档**  
- [MCP 规范 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP 安全最佳实践](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP 授权规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **微软安全解决方案**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [GitHub 高级安全](https://github.com/security/advanced-security)  
- [Azure 密钥保管库](https://learn.microsoft.com/azure/key-vault/)

### **安全标准**  
- [OAuth 2.0 安全最佳实践 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP 大型语言模型十大风险](https://genai.owasp.org/)  
- [NIST 网络安全框架](https://www.nist.gov/cyberframework)

---

> **重要提示**：这些安全控制反映了当前 MCP 规范（2025-06-18）。标准持续快速演进，请始终核对最新的[官方文档](https://spec.modelcontextprotocol.io/)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
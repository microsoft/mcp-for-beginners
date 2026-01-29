# MCP 安全控制 - 2025 年 12 月更新

> **當前標準**：本文件反映了 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) 的安全要求及官方 [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)。

Model Context Protocol (MCP) 已顯著成熟，增強的安全控制涵蓋傳統軟件安全及 AI 特定威脅。本文檔提供截至 2025 年 12 月的全面 MCP 安全實施控制。

## **強制性安全要求**

### **MCP 規範中的關鍵禁止事項：**

> **禁止**：MCP 伺服器**不得**接受未明確為該 MCP 伺服器簽發的任何令牌  
>
> **禁止**：MCP 伺服器**不得**使用會話進行身份驗證  
>
> **要求**：實施授權的 MCP 伺服器**必須**驗證所有入站請求  
>
> **強制**：使用靜態客戶端 ID 的 MCP 代理伺服器**必須**為每個動態註冊的客戶端獲得用戶同意

---

## 1. **身份驗證與授權控制**

### **外部身份提供者整合**

**當前 MCP 標準 (2025-06-18)** 允許 MCP 伺服器委派身份驗證給外部身份提供者，這是重大安全改進：

### **外部身份提供者整合**

**當前 MCP 標準 (2025-11-25)** 允許 MCP 伺服器委派身份驗證給外部身份提供者，這是重大安全改進：

**安全優勢：**  
1. **消除自訂身份驗證風險**：避免自訂身份驗證實現，減少攻擊面  
2. **企業級安全**：利用 Microsoft Entra ID 等成熟身份提供者的先進安全功能  
3. **集中身份管理**：簡化用戶生命週期管理、存取控制及合規審計  
4. **多因素身份驗證**：繼承企業身份提供者的 MFA 能力  
5. **條件存取政策**：受益於基於風險的存取控制及自適應身份驗證

**實施要求：**  
- **令牌受眾驗證**：驗證所有令牌明確簽發給 MCP 伺服器  
- **簽發者驗證**：驗證令牌簽發者與預期身份提供者匹配  
- **簽名驗證**：對令牌完整性進行加密驗證  
- **過期強制**：嚴格執行令牌有效期限  
- **範圍驗證**：確保令牌包含請求操作所需的適當權限

### **授權邏輯安全**

**關鍵控制：**  
- **全面授權審計**：定期對所有授權決策點進行安全審查  
- **失效安全預設**：授權邏輯無法明確決定時拒絕存取  
- **權限邊界**：明確區分不同特權層級及資源存取  
- **審計日誌**：完整記錄所有授權決策以供安全監控  
- **定期存取審查**：定期驗證用戶權限及特權分配

## 2. **令牌安全與防止令牌直通控制**

### **禁止令牌直通**

MCP 授權規範明確禁止令牌直通，因其帶來嚴重安全風險：

**解決的安全風險：**  
- **控制繞過**：繞過速率限制、請求驗證及流量監控等重要安全控制  
- **責任歸屬失效**：無法識別客戶端，破壞審計追蹤及事件調查  
- **代理基礎資料外洩**：惡意行為者利用伺服器作為未授權資料存取的代理  
- **信任邊界違反**：破壞下游服務對令牌來源的信任假設  
- **橫向移動**：多服務間被盜令牌擴大攻擊範圍

**實施控制：**  
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

**最佳實踐：**  
- **短期令牌**：透過頻繁令牌輪替減少暴露時間  
- **即時發行**：僅在特定操作需要時發行令牌  
- **安全存儲**：使用硬體安全模組 (HSM) 或安全金鑰庫  
- **令牌綁定**：盡可能將令牌綁定至特定客戶端、會話或操作  
- **監控與警報**：實時偵測令牌濫用或未授權存取行為

## 3. **會話安全控制**

### **防止會話劫持**

**攻擊向量：**  
- **會話劫持提示注入**：惡意事件注入共享會話狀態  
- **會話冒充**：未授權使用被盜會話 ID 繞過身份驗證  
- **可恢復串流攻擊**：利用伺服器發送事件恢復注入惡意內容

**強制會話控制：**  
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

**傳輸安全：**  
- **強制 HTTPS**：所有會話通訊使用 TLS 1.3  
- **安全 Cookie 屬性**：HttpOnly、Secure、SameSite=Strict  
- **憑證釘選**：關鍵連線防止中間人攻擊

### **有狀態與無狀態考量**

**有狀態實施：**  
- 共享會話狀態需額外防護以防注入攻擊  
- 基於佇列的會話管理需完整性驗證  
- 多伺服器實例需安全同步會話狀態

**無狀態實施：**  
- 使用 JWT 或類似令牌管理會話  
- 會話狀態完整性加密驗證  
- 攻擊面較小，但需強健令牌驗證

## 4. **AI 特定安全控制**

### **提示注入防禦**

**Microsoft Prompt Shields 整合：**  
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

**實施控制：**  
- **輸入淨化**：全面驗證及過濾所有用戶輸入  
- **內容邊界定義**：系統指令與用戶內容明確分隔  
- **指令層級**：衝突指令的正確優先順序  
- **輸出監控**：偵測潛在有害或被操控的輸出

### **工具中毒防範**

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

**動態工具管理：**  
- **審批工作流程**：工具修改需明確用戶同意  
- **回滾能力**：可回復至先前工具版本  
- **變更審計**：完整記錄工具定義修改歷史  
- **風險評估**：自動評估工具安全狀態

## 5. **混淆代理攻擊防範**

### **OAuth 代理安全**

**攻擊防範控制：**  
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

**實施要求：**  
- **用戶同意驗證**：動態客戶端註冊絕不跳過同意畫面  
- **重定向 URI 驗證**：嚴格白名單驗證重定向目的地  
- **授權碼保護**：短期有效且單次使用授權碼  
- **客戶端身份驗證**：強健驗證客戶端憑證及元資料

## 6. **工具執行安全**

### **沙箱與隔離**

**基於容器的隔離：**  
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

**進程隔離：**  
- **獨立進程上下文**：每個工具執行於隔離進程空間  
- **進程間通訊**：安全 IPC 機制並進行驗證  
- **進程監控**：運行時行為分析及異常偵測  
- **資源限制**：CPU、記憶體及 I/O 操作硬性限制

### **最小權限實施**

**權限管理：**  
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

## 7. **供應鏈安全控制**

### **依賴驗證**

**全面元件安全：**  
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

### **持續監控**

**供應鏈威脅偵測：**  
- **依賴健康監控**：持續評估所有依賴的安全問題  
- **威脅情報整合**：即時更新新興供應鏈威脅  
- **行為分析**：偵測外部元件異常行為  
- **自動響應**：立即遏制受損元件

## 8. **監控與偵測控制**

### **安全資訊與事件管理 (SIEM)**

**全面日誌策略：**  
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

### **即時威脅偵測**

**行為分析：**  
- **用戶行為分析 (UBA)**：偵測異常用戶存取模式  
- **實體行為分析 (EBA)**：監控 MCP 伺服器及工具行為  
- **機器學習異常偵測**：AI 驅動安全威脅識別  
- **威脅情報關聯**：將觀察活動與已知攻擊模式匹配

## 9. **事件響應與復原**

### **自動響應能力**

**即時響應行動：**  
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

### **取證能力**

**調查支援：**  
- **審計軌跡保存**：不可變日誌並具加密完整性  
- **證據收集**：自動收集相關安全資料  
- **時間線重建**：詳細還原安全事件序列  
- **影響評估**：評估妥協範圍及資料暴露

## **關鍵安全架構原則**

### **深度防禦**  
- **多重安全層**：安全架構無單點失效  
- **冗餘控制**：關鍵功能重疊安全措施  
- **失效安全機制**：系統遇錯誤或攻擊時採用安全預設

### **零信任實施**  
- **永不信任，持續驗證**：持續驗證所有實體及請求  
- **最小權限原則**：所有組件僅授予最低存取權限  
- **微分段**：細粒度網路及存取控制

### **持續安全演進**  
- **威脅環境適應**：定期更新以應對新興威脅  
- **安全控制效能**：持續評估及改進控制措施  
- **規範合規**：與不斷演進的 MCP 安全標準保持一致

---

## **實施資源**

### **官方 MCP 文件**  
- [MCP 規範 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft 安全解決方案**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **安全標準**  
- [OAuth 2.0 安全最佳實踐 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP 大型語言模型十大風險](https://genai.owasp.org/)  
- [NIST 網絡安全框架](https://www.nist.gov/cyberframework)

---

> **重要**：這些安全控制反映當前 MCP 規範 (2025-06-18)。標準快速演進，請務必參考最新 [官方文件](https://spec.modelcontextprotocol.io/)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
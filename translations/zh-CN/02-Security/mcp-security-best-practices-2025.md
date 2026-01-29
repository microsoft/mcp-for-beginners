# MCP 安全最佳实践 - 2025 年 12 月更新

> **重要**：本文档反映了最新的 [MCP 规范 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) 安全要求和官方 [MCP 安全最佳实践](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)。请始终参考当前规范以获取最新指导。

## MCP 实现的基本安全实践

模型上下文协议引入了超越传统软件安全的独特安全挑战。这些实践涵盖了基础安全要求和 MCP 特有的威胁，包括提示注入、工具中毒、会话劫持、混淆代理问题和令牌透传漏洞。

### **强制性安全要求**

**来自 MCP 规范的关键要求：**

### **强制性安全要求**

**来自 MCP 规范的关键要求：**

> **不得**：MCP 服务器**不得**接受任何未明确为该 MCP 服务器签发的令牌
> 
> **必须**：实现授权的 MCP 服务器**必须**验证所有入站请求
>  
> **不得**：MCP 服务器**不得**使用会话进行身份验证
>
> **必须**：使用静态客户端 ID 的 MCP 代理服务器**必须**为每个动态注册的客户端获取用户同意

---

## 1. **令牌安全与身份验证**

**身份验证与授权控制：**
   - **严格的授权审查**：对 MCP 服务器授权逻辑进行全面审计，确保只有预期的用户和客户端可以访问资源
   - **外部身份提供者集成**：使用 Microsoft Entra ID 等成熟身份提供者，而非自定义身份验证实现
   - **令牌受众验证**：始终验证令牌是否明确为您的 MCP 服务器签发——绝不接受上游令牌
   - **适当的令牌生命周期管理**：实施安全的令牌轮换、过期策略，防止令牌重放攻击

**受保护的令牌存储：**
   - 对所有机密使用 Azure Key Vault 或类似安全凭据存储
   - 实现令牌静态和传输中的加密
   - 定期轮换凭据并监控未授权访问

## 2. **会话管理与传输安全**

**安全会话实践：**
   - **加密安全的会话 ID**：使用安全随机数生成器生成安全、非确定性的会话 ID
   - **用户特定绑定**：使用 `<user_id>:<session_id>` 等格式将会话 ID 绑定到用户身份，防止跨用户会话滥用
   - **会话生命周期管理**：实施适当的过期、轮换和失效，限制漏洞窗口
   - **HTTPS/TLS 强制执行**：所有通信必须使用 HTTPS，防止会话 ID 被截获

**传输层安全：**
   - 尽可能配置 TLS 1.3 并妥善管理证书
   - 对关键连接实施证书绑定
   - 定期轮换证书并验证有效性

## 3. **AI 特定威胁防护** 🤖

**提示注入防御：**
   - **Microsoft 提示盾**：部署 AI 提示盾以高级检测和过滤恶意指令
   - **输入清理**：验证并清理所有输入，防止注入攻击和混淆代理问题
   - **内容边界**：使用分隔符和数据标记系统区分可信指令和外部内容

**工具中毒预防：**
   - **工具元数据验证**：实施工具定义的完整性检查，监控异常变更
   - **动态工具监控**：监控运行时行为，设置异常执行模式告警
   - **审批工作流**：工具修改和能力变更需用户明确批准

## 4. **访问控制与权限**

**最小权限原则：**
   - 仅授予 MCP 服务器实现预期功能所需的最低权限
   - 实施基于角色的访问控制（RBAC）并细化权限
   - 定期权限审查和持续监控权限提升

**运行时权限控制：**
   - 施加资源限制，防止资源耗尽攻击
   - 使用容器隔离工具执行环境  
   - 实施按需访问的管理功能

## 5. **内容安全与监控**

**内容安全实施：**
   - **Azure 内容安全集成**：使用 Azure 内容安全检测有害内容、越狱尝试和策略违规
   - **行为分析**：实施运行时行为监控，检测 MCP 服务器和工具执行异常
   - **全面日志记录**：记录所有身份验证尝试、工具调用和安全事件，使用安全防篡改存储

**持续监控：**
   - 实时告警可疑模式和未授权访问尝试  
   - 与 SIEM 系统集成，实现安全事件集中管理
   - 定期对 MCP 实现进行安全审计和渗透测试

## 6. **供应链安全**

**组件验证：**
   - **依赖扫描**：对所有软件依赖和 AI 组件使用自动漏洞扫描
   - **来源验证**：验证模型、数据源和外部服务的来源、许可和完整性
   - **签名包**：使用加密签名包，部署前验证签名

**安全开发流水线：**
   - **GitHub 高级安全**：实施机密扫描、依赖分析和 CodeQL 静态分析
   - **CI/CD 安全**：在自动部署流水线中集成安全验证
   - **工件完整性**：对部署工件和配置实施加密验证

## 7. **OAuth 安全与混淆代理防范**

**OAuth 2.1 实现：**
   - **PKCE 实施**：所有授权请求使用代码交换证明（PKCE）
   - **明确同意**：为每个动态注册客户端获取用户同意，防止混淆代理攻击
   - **重定向 URI 验证**：严格验证重定向 URI 和客户端标识符

**代理安全：**
   - 防止通过静态客户端 ID 利用绕过授权
   - 实施第三方 API 访问的适当同意工作流
   - 监控授权码窃取和未授权 API 访问

## 8. **事件响应与恢复**

**快速响应能力：**
   - **自动响应**：实施凭据轮换和威胁遏制的自动化系统
   - **回滚程序**：能够快速恢复到已知良好配置和组件
   - **取证能力**：详细审计轨迹和日志支持事件调查

**沟通与协调：**
   - 明确安全事件升级流程
   - 与组织事件响应团队集成
   - 定期进行安全事件模拟和桌面演练

## 9. **合规与治理**

**法规合规：**
   - 确保 MCP 实现符合行业特定要求（GDPR、HIPAA、SOC 2）
   - 实施 AI 数据处理的数据分类和隐私控制
   - 维护全面的合规审计文档

**变更管理：**
   - 对所有 MCP 系统修改进行正式安全审查
   - 配置变更实施版本控制和审批工作流
   - 定期进行合规评估和差距分析

## 10. **高级安全控制**

**零信任架构：**
   - **永不信任，始终验证**：持续验证用户、设备和连接
   - **微分段**：细粒度网络控制，隔离各个 MCP 组件
   - **条件访问**：基于风险的访问控制，适应当前上下文和行为

**运行时应用保护：**
   - **运行时应用自我保护（RASP）**：部署 RASP 技术实现实时威胁检测
   - **应用性能监控**：监控性能异常，识别潜在攻击
   - **动态安全策略**：根据当前威胁态势调整安全策略

## 11. **微软安全生态系统集成**

**全面微软安全：**
   - **Microsoft Defender for Cloud**：MCP 工作负载的云安全态势管理
   - **Azure Sentinel**：云原生 SIEM 和 SOAR 功能，实现高级威胁检测
   - **Microsoft Purview**：AI 工作流和数据源的数据治理与合规

**身份与访问管理：**
   - **Microsoft Entra ID**：企业身份管理，支持条件访问策略
   - **特权身份管理（PIM）**：按需访问和管理功能审批工作流
   - **身份保护**：基于风险的条件访问和自动威胁响应

## 12. **持续安全演进**

**保持最新：**
   - **规范监控**：定期审查 MCP 规范更新和安全指导变更
   - **威胁情报**：集成 AI 特定威胁情报和妥协指标
   - **安全社区参与**：积极参与 MCP 安全社区和漏洞披露计划

**自适应安全：**
   - **机器学习安全**：使用基于 ML 的异常检测识别新型攻击模式
   - **预测性安全分析**：实施预测模型，主动识别威胁
   - **安全自动化**：基于威胁情报和规范变更自动更新安全策略

---

## **关键安全资源**

### **官方 MCP 文档**
- [MCP 规范 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP 安全最佳实践](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP 授权规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **微软安全解决方案**
- [Microsoft 提示盾](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID 安全](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub 高级安全](https://github.com/security/advanced-security)

### **安全标准**
- [OAuth 2.0 安全最佳实践 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [大型语言模型 OWASP 前十](https://genai.owasp.org/)
- [NIST AI 风险管理框架](https://www.nist.gov/itl/ai-risk-management-framework)

### **实施指南**
- [Azure API 管理 MCP 身份验证网关](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID 与 MCP 服务器](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **安全通知**：MCP 安全实践快速演进。实施前请始终核对当前 [MCP 规范](https://spec.modelcontextprotocol.io/) 和 [官方安全文档](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
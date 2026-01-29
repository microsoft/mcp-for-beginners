# MCP 安全最佳实践 2025

本综合指南概述了基于最新 **MCP 规范 2025-11-25** 及当前行业标准实施模型上下文协议（MCP）系统的关键安全最佳实践。这些实践涵盖了传统安全问题以及 MCP 部署中特有的 AI 相关威胁。

## 关键安全要求

### 强制安全控制（必须要求）

1. **令牌验证**：MCP 服务器**不得**接受任何未明确为该 MCP 服务器颁发的令牌
2. **授权验证**：实现授权的 MCP 服务器**必须**验证所有入站请求，且**不得**使用会话进行身份验证  
3. **用户同意**：使用静态客户端 ID 的 MCP 代理服务器**必须**为每个动态注册的客户端获取明确的用户同意
4. **安全会话 ID**：MCP 服务器**必须**使用通过安全随机数生成器生成的加密安全、非确定性会话 ID

## 核心安全实践

### 1. 输入验证与清理
- **全面输入验证**：验证并清理所有输入，防止注入攻击、混淆代理问题和提示注入漏洞
- **参数模式强制**：对所有工具参数和 API 输入实施严格的 JSON 模式验证
- **内容过滤**：使用 Microsoft Prompt Shields 和 Azure 内容安全过滤提示和响应中的恶意内容
- **输出清理**：在向用户或下游系统展示之前验证并清理所有模型输出

### 2. 身份验证与授权卓越  
- **外部身份提供者**：将身份验证委托给成熟的身份提供者（Microsoft Entra ID、OAuth 2.1 提供者），而非自定义实现
- **细粒度权限**：根据最小权限原则实现细粒度、工具特定的权限
- **令牌生命周期管理**：使用短期访问令牌，配合安全轮换和适当的受众验证
- **多因素认证**：所有管理访问和敏感操作均需 MFA

### 3. 安全通信协议
- **传输层安全**：所有 MCP 通信均使用 HTTPS/TLS 1.3，并进行适当的证书验证
- **端到端加密**：对高度敏感的传输和静态数据实施额外加密层
- **证书管理**：维护适当的证书生命周期管理及自动续期流程
- **协议版本强制**：使用当前 MCP 协议版本（2025-11-25），并进行适当的版本协商

### 4. 高级速率限制与资源保护
- **多层速率限制**：在用户、会话、工具和资源级别实施速率限制，防止滥用
- **自适应速率限制**：使用基于机器学习的速率限制，适应使用模式和威胁指标
- **资源配额管理**：为计算资源、内存使用和执行时间设置适当限制
- **DDoS 保护**：部署全面的 DDoS 保护和流量分析系统

### 5. 全面日志记录与监控
- **结构化审计日志**：为所有 MCP 操作、工具执行和安全事件实施详细且可搜索的日志
- **实时安全监控**：部署带 AI 异常检测的 SIEM 系统监控 MCP 工作负载
- **隐私合规日志**：在尊重数据隐私要求和法规的前提下记录安全事件
- **事件响应集成**：将日志系统连接到自动化事件响应工作流

### 6. 增强安全存储实践
- **硬件安全模块**：使用 HSM 支持的密钥存储（Azure Key Vault、AWS CloudHSM）进行关键加密操作
- **加密密钥管理**：实施适当的密钥轮换、隔离和访问控制
- **机密管理**：将所有 API 密钥、令牌和凭据存储在专用的机密管理系统中
- **数据分类**：根据敏感度对数据进行分类，并应用相应的保护措施

### 7. 高级令牌管理
- **防止令牌透传**：明确禁止绕过安全控制的令牌透传模式
- **受众验证**：始终验证令牌受众声明与目标 MCP 服务器身份匹配
- **基于声明的授权**：基于令牌声明和用户属性实现细粒度授权
- **令牌绑定**：在适当情况下将令牌绑定到特定会话、用户或设备

### 8. 安全会话管理
- **加密会话 ID**：使用加密安全的随机数生成器生成会话 ID（非可预测序列）
- **用户特定绑定**：使用安全格式如 `<user_id>:<session_id>` 将会话 ID 绑定到用户特定信息
- **会话生命周期控制**：实施适当的会话过期、轮换和失效机制
- **会话安全头**：使用适当的 HTTP 安全头保护会话

### 9. AI 特定安全控制
- **提示注入防御**：部署 Microsoft Prompt Shields，结合聚光灯、分隔符和数据标记技术
- **工具中毒预防**：验证工具元数据，监控动态变化，确保工具完整性
- **模型输出验证**：扫描模型输出，防止潜在数据泄露、有害内容或安全策略违规
- **上下文窗口保护**：实施防止上下文窗口中毒和操纵攻击的控制措施

### 10. 工具执行安全
- **执行沙箱**：在容器化、隔离环境中运行工具执行，并设置资源限制
- **权限分离**：以最小必要权限和独立服务账户执行工具
- **网络隔离**：为工具执行环境实施网络分段
- **执行监控**：监控工具执行的异常行为、资源使用和安全违规

### 11. 持续安全验证
- **自动化安全测试**：将安全测试集成到 CI/CD 流水线，使用 GitHub Advanced Security 等工具
- **漏洞管理**：定期扫描所有依赖项，包括 AI 模型和外部服务
- **渗透测试**：定期针对 MCP 实现进行安全评估
- **安全代码审查**：对所有 MCP 相关代码变更实施强制安全审查

### 12. AI 供应链安全
- **组件验证**：验证所有 AI 组件（模型、嵌入、API）的来源、完整性和安全性
- **依赖管理**：维护所有软件和 AI 依赖的最新清单及漏洞跟踪
- **可信仓库**：使用经过验证的可信来源获取所有 AI 模型、库和工具
- **供应链监控**：持续监控 AI 服务提供商和模型仓库的安全状况

## 高级安全模式

### MCP 零信任架构
- **永不信任，始终验证**：对所有 MCP 参与者实施持续验证
- **微分段**：通过细粒度网络和身份控制隔离 MCP 组件
- **条件访问**：实施基于风险的访问控制，适应上下文和行为
- **持续风险评估**：基于当前威胁指标动态评估安全态势

### 隐私保护的 AI 实施
- **数据最小化**：仅暴露每个 MCP 操作所需的最少数据
- **差分隐私**：对敏感数据处理实施隐私保护技术
- **同态加密**：使用先进加密技术实现加密数据的安全计算
- **联邦学习**：实施分布式学习方法，保护数据本地性和隐私

### AI 系统事件响应
- **AI 特定事件流程**：制定针对 AI 和 MCP 特定威胁的事件响应流程
- **自动化响应**：对常见 AI 安全事件实施自动遏制和修复  
- **取证能力**：保持 AI 系统妥协和数据泄露的取证准备
- **恢复流程**：建立 AI 模型中毒、提示注入攻击和服务妥协的恢复流程

## 实施资源与标准

### 官方 MCP 文档
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - 当前 MCP 协议规范
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - 官方安全指导
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - 身份验证和授权模式
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - 传输层安全要求

### Microsoft 安全解决方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 高级提示注入防护
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面 AI 内容过滤
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企业身份和访问管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全机密和凭据管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供应链和代码安全扫描

### 安全标准与框架
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 当前 OAuth 安全指导
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web 应用安全风险
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 特定安全风险
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 全面 AI 风险管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 信息安全管理体系

### 实施指南与教程
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企业身份验证模式
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者集成
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳实践
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高级加密模式

### 高级安全资源
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 安全开发实践
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI 特定安全测试
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 威胁建模方法
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 隐私保护 AI 技术

### 合规与治理
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 系统隐私合规
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 负责任 AI 实施
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 服务提供商安全控制
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 医疗 AI 合规要求

### DevSecOps 与自动化
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全 AI 开发流水线
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 持续安全验证
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全基础设施部署
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 工作负载容器安全

### 监控与事件响应  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 全面监控解决方案
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 特定事件流程
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - 安全信息与事件管理
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威胁情报来源

## 🔄 持续改进

### 跟进不断演进的标准
- **MCP 规范更新**：监控官方 MCP 规范变更和安全公告
- **威胁情报**：订阅 AI 安全威胁源和漏洞数据库  
- **社区参与**：参与 MCP 安全社区讨论和工作组
- **定期评估**：每季度进行安全态势评估并相应更新实践

### 为 MCP 安全贡献力量
- **安全研究**：参与 MCP 安全研究和漏洞披露计划
- **最佳实践分享**：与社区分享安全实施经验和教训
- **标准开发**：参与MCP规范开发和安全标准制定  
- **工具开发**：开发并共享MCP生态系统的安全工具和库  

---

*本文档反映了截至2025年12月18日的MCP安全最佳实践，基于MCP规范2025-11-25。随着协议和威胁环境的发展，应定期审查和更新安全实践。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
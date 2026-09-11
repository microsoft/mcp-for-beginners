# MCP安全最佳实践 - 2026年9月更新

本综合指南概述了基于
**MCP规范 2026-07-28** 及当前行业标准的模型上下文协议（MCP）系统
实施的关键安全最佳实践。这些
实践涵盖了传统安全问题和MCP部署中特有的AI特定威胁。


## 关键安全要求

### 强制安全控制（必须要求）

1. <strong>令牌验证</strong>：MCP服务器 <strong>不得</strong> 接受任何未明确为MCP服务器本身颁发的令牌
2. <strong>授权验证</strong>：实施授权的MCP服务器 <strong>必须</strong> 验证所有入站请求，且 <strong>不得</strong> 使用会话进行身份验证  
3. <strong>用户同意</strong>：使用静态第三方客户端ID的MCP代理服务器 <strong>必须</strong> 在转发授权流程前取得每个MCP客户端的明确同意
4. <strong>状态句柄安全</strong>：MCP服务器 <strong>不得</strong> 将拥有应用状态句柄视为身份验证，且 <strong>必须</strong> 对使用状态句柄的每个请求进行授权



## 核心安全实践

### 1. 输入验证与清理
- <strong>全面输入验证</strong>：验证并清理所有输入，防止注入攻击、混淆代理问题和提示注入漏洞
- <strong>参数架构强制</strong>：对所有工具参数和API输入实施严格的JSON架构验证
- <strong>内容过滤</strong>：使用Microsoft Prompt Shields和Azure内容安全过滤提示和响应中的恶意内容
- <strong>输出清理</strong>：在呈现给用户或下游系统前验证并清理所有模型输出

### 2. 身份验证与授权卓越  
- <strong>外部身份提供者</strong>：将身份验证授权给成熟的身份提供者（Microsoft Entra ID、OAuth 2.1提供者），而非实现自定义身份验证
- <strong>客户端注册</strong>：优先使用客户端ID元数据文档或预注册；仅为兼容使用已弃用的动态客户端注册
- <strong>细粒度权限</strong>：根据最小权限原则实现细粒度、工具特定权限
- <strong>令牌生命周期管理</strong>：使用短期访问令牌，安全轮换并正确验证受众
- <strong>多因素认证</strong>：所有管理访问和敏感操作要求启用MFA

### 3. 安全通信协议
- <strong>传输层安全</strong>：使用带有正确证书验证的HTTPS进行远程HTTP MCP通信；本地stdio服务器使用进程隔离和环境凭据


- <strong>端到端加密</strong>：对高度敏感的传输和静态数据实施额外加密层
- <strong>证书管理</strong>：维持适当的证书生命周期管理，支持自动续订流程
- <strong>协议版本强制</strong>：使用MCP `2026-07-28`，在每个请求中包含必需的版本元数据，拒绝不支持版本


### 4. 高级速率限制与资源保护
- <strong>多层速率限制</strong>：按用户、凭据、
  操作、工具及资源实现速率限制，防止滥用
- <strong>自适应速率限制</strong>：使用基于机器学习的速率限制，适应使用模式和威胁指标
- <strong>资源配额管理</strong>：设置计算资源、内存使用和执行时间的适当限制
- **DDoS防护**：部署全面的DDoS防护与流量分析系统

### 5. 全面日志记录与监控
- <strong>结构化审计日志</strong>：为所有MCP操作、工具执行和安全事件实现详细且可搜索日志
- <strong>实时安全监控</strong>：部署具有AI异常检测的SIEM系统，监控MCP负载
- <strong>隐私合规日志</strong>：在遵守数据隐私要求和法规的前提下记录安全事件
- <strong>事件响应集成</strong>：将日志系统连接到自动化事件响应流程

### 6. 增强安全存储实践
- <strong>硬件安全模块</strong>：对关键加密操作使用基于硬件安全模块的密钥存储（Azure Key Vault，AWS CloudHSM）
- <strong>加密密钥管理</strong>：实施正确的密钥轮换、隔离和访问控制
- <strong>密钥管理</strong>：在专用的密钥管理系统中存储所有API密钥、令牌和凭据
- <strong>数据分类</strong>：根据敏感性级别对数据分类并应用适当保护措施

### 7. 高级令牌管理
- <strong>禁止令牌透传</strong>：明令禁止绕过安全控制的令牌透传模式
- <strong>受众验证</strong>：始终验证令牌中的受众声明是否匹配目标MCP服务器身份
- <strong>基于声明的授权</strong>：基于令牌声明和用户属性实现细粒度授权
- <strong>令牌绑定</strong>：验证令牌针对预期的MCP资源，
	并将应用状态句柄服务器端绑定至已认证主体

### 8. 安全应用状态

- <strong>加密状态句柄</strong>：为跨请求状态生成不透明、非确定性句柄

- <strong>用户绑定</strong>：将每个句柄服务器端绑定至认证主体；不信任客户端提供的用户ID

- <strong>生命周期控制</strong>：过期和吊销句柄，并定义调用方如何从陈旧状态中恢复

- <strong>每请求授权</strong>：每次呈现句柄时重新检查授权；句柄是名称，不是凭据


### 9. AI特定安全控制
- <strong>提示注入防御</strong>：部署微软Prompt Shields，使用聚焦、高亮和数据标记技术
- <strong>工具中毒防护</strong>：验证工具元数据，监控动态变化，校验工具完整性
- <strong>模型输出验证</strong>：扫描模型输出，检测潜在数据泄漏、有害内容或安全策略违规
- <strong>上下文窗口保护</strong>：实施控制，防止上下文窗口被污染和操纵攻击

### 10. 工具执行安全
- <strong>执行沙箱</strong>：在容器化、隔离环境中执行工具，设置资源限制
- <strong>权限分离</strong>：以最低权限执行工具并分隔服务账户
- <strong>网络隔离</strong>：为工具执行环境实现网络分段
- <strong>执行监控</strong>：监测工具执行，发现异常行为、资源使用和安全违规

### 11. 持续安全验证
- <strong>自动化安全测试</strong>：将安全测试集成到CI/CD管道，使用GitHub Advanced Security等工具
- <strong>漏洞管理</strong>：定期扫描所有依赖，包括AI模型和外部服务
- <strong>渗透测试</strong>：定期开展针对MCP实现的安全评估
- <strong>安全代码审查</strong>：对所有MCP相关代码变更实施强制安全审查

### 12. AI供应链安全
- <strong>组件验证</strong>：验证所有AI组件（模型、嵌入、API）的来源、完整性和安全性
- <strong>依赖管理</strong>：维护所有软件和AI依赖的当前清单并跟踪漏洞
- <strong>可信仓库</strong>：使用经过验证、可信的AI模型、库和工具来源
- <strong>供应链监控</strong>：持续监测AI服务提供商和模型仓库的安全性

## 高级安全模式

### MCP的零信任架构
- **永不信任，始终验证**：对所有MCP参与方实施持续验证
- <strong>微分段</strong>：对MCP组件实施细粒度的网络和身份控制隔离
- <strong>条件访问</strong>：实施基于风险的访问控制，适应上下文和行为
- <strong>持续风险评估</strong>：根据当前威胁指标动态评估安全态势

### 隐私保护的AI实现
- <strong>数据最小化</strong>：仅暴露每个MCP操作所需的最小数据
- <strong>差分隐私</strong>：对敏感数据处理实施隐私保护技术
- <strong>同态加密</strong>：使用先进加密技术对加密数据进行安全计算
- <strong>联邦学习</strong>：实施保留数据本地性和隐私的分布式学习方法

### AI系统的事件响应
- **AI特定事件程序**：制定针对AI和MCP特定威胁的事件响应程序
- <strong>自动响应</strong>：对常见AI安全事件实现自动遏制和修复  
- <strong>取证能力</strong>：维护AI系统入侵和数据泄露的取证准备
- <strong>恢复程序</strong>：制定应对AI模型中毒、提示注入攻击和服务受损的恢复流程

## 实施资源与标准

### 🏔️ 实战安全培训
- **[MCP安全峰会研讨会（Sherpa）](https://azure-samples.github.io/sherpa/)** - Azure中保护MCP服务器的综合实战研讨会
- **[OWASP MCP Azure安全指南](https://microsoft.github.io/mcp-azure-security-guide/)** - 参考架构及OWASP MCP Top 10实现指导

### 官方MCP文档
- [MCP规范 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 当前MCP协议规范
- [MCP安全最佳实践](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 官方安全指导
- [MCP授权规范](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP授权模式
- [MCP传输](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - 传输要求

### 微软安全解决方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 高级提示注入保护
- [Azure内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面AI内容过滤
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企业身份及访问管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全的密钥和凭据管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供应链和代码安全扫描

### 安全标准与框架
- [OAuth 2.1安全最佳实践](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 当前OAuth安全指导
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web应用安全风险
- [适用于大型语言模型(LLM)的OWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI特定安全风险
- [NIST AI风险管理框架](https://www.nist.gov/itl/ai-risk-management-framework) - 综合AI风险管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 信息安全管理体系

### 实施指南与教程
- [使用Azure API管理作为MCP认证网关](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企业认证模式
- [Microsoft Entra ID与MCP服务器集成](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者集成
- [安全令牌存储实现](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳实践
- [针对AI的端到端加密](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高级加密模式

### 高级安全资源
- [微软安全开发生命周期](https://www.microsoft.com/sdl) - 安全开发实践
- [AI红队指导](https://learn.microsoft.com/security/ai-red-team/) - AI特定安全测试
- [AI系统威胁模型](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI威胁建模方法
- [AI隐私工程](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 隐私保护的AI技术

### 合规与治理
- [AI的GDPR合规](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI系统中的隐私合规
- [AI治理框架](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 负责任的AI实施
- [AI服务的SOC 2认证](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI服务提供商的安全控制
- [AI的HIPAA合规](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 医疗AI合规要求

### DevSecOps与自动化
- [AI的DevSecOps管道](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全的AI开发管道
- [自动化安全测试](https://learn.microsoft.com/security/engineering/devsecops) - 持续安全验证
- [基础设施即代码安全](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全的基础设施部署
- [AI的容器安全](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI工作负载容器化安全

### 监控与事件响应  
- [Azure监控AI工作负载](https://learn.microsoft.com/azure/azure-monitor/overview) - 全面监控方案
- [AI安全事件响应](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI特定事件响应程序
- [AI系统的SIEM](https://learn.microsoft.com/azure/sentinel/overview) - 安全信息与事件管理

- [AI 威胁情报](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威胁情报来源

## 🔄 持续改进

### 跟进不断发展的标准
- **MCP 规范更新**：监控官方 MCP 规范变更和安全公告
- <strong>威胁情报</strong>：订阅 AI 安全威胁信息源和漏洞数据库  
- <strong>社区参与</strong>：参与 MCP 安全社区讨论和工作组
- <strong>定期评估</strong>：进行季度安全姿态评估并相应更新实践

### 为 MCP 安全做出贡献
- <strong>安全研究</strong>：参与 MCP 安全研究和漏洞披露计划
- <strong>最佳实践分享</strong>：与社区分享安全实施经验和教训
- <strong>标准开发</strong>：参与 MCP 规范制定和安全标准创建
- <strong>工具开发</strong>：为 MCP 生态系统开发并分享安全工具和库

---

*本文件反映了截至 2026 年 9 月 9 日的 MCP 安全最佳实践，
基于 MCP 规范 `2026-07-28`。应随着协议和威胁环境的演变，定期
审查安全实践。*

## 接下来

- 阅读：[MCP 安全最佳实践](./mcp-security-best-practices.md)
- 返回：[安全模块概述](./README.md)
- 继续：[模块3：快速入门](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
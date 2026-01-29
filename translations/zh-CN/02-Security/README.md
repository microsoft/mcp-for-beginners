# MCP 安全性：AI 系统的全面保护

[![MCP Security Best Practices](../../../translated_images/zh-CN/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(点击上方图片观看本课视频)_

安全性是 AI 系统设计的基础，因此我们将其作为第二部分重点介绍。这与微软来自[安全未来计划](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/)的**安全设计原则**相一致。

模型上下文协议（MCP）为 AI 驱动的应用带来了强大的新功能，同时也引入了超越传统软件风险的独特安全挑战。MCP 系统面临既有的安全问题（安全编码、最小权限、供应链安全）以及新的 AI 特有威胁，包括提示注入、工具投毒、会话劫持、混淆代理攻击、令牌透传漏洞和动态能力修改。

本课探讨 MCP 实现中最关键的安全风险——涵盖身份验证、授权、过度权限、间接提示注入、会话安全、混淆代理问题、令牌管理和供应链漏洞。您将学习可操作的控制措施和最佳实践，以减轻这些风险，同时利用微软解决方案如 Prompt Shields、Azure 内容安全和 GitHub 高级安全来强化您的 MCP 部署。

## 学习目标

完成本课后，您将能够：

- **识别 MCP 特有威胁**：识别 MCP 系统中的独特安全风险，包括提示注入、工具投毒、过度权限、会话劫持、混淆代理问题、令牌透传漏洞和供应链风险
- **应用安全控制**：实施有效的缓解措施，包括强身份验证、最小权限访问、安全令牌管理、会话安全控制和供应链验证
- **利用微软安全解决方案**：理解并部署微软 Prompt Shields、Azure 内容安全和 GitHub 高级安全以保护 MCP 工作负载
- **验证工具安全**：认识工具元数据验证的重要性，监控动态变化，并防御间接提示注入攻击
- **整合最佳实践**：结合既有安全基础（安全编码、服务器加固、零信任）与 MCP 特有控制，实现全面保护

# MCP 安全架构与控制

现代 MCP 实现需要分层安全方法，既涵盖传统软件安全，也应对 AI 特有威胁。快速发展的 MCP 规范持续完善其安全控制，促进与企业安全架构和既有最佳实践的更好集成。

来自[微软数字防御报告](https://aka.ms/mddr)的研究表明，**98% 的报告泄露事件可通过健全的安全卫生措施防止**。最有效的保护策略是将基础安全实践与 MCP 特有控制结合——经过验证的基线安全措施仍是降低整体安全风险的最关键因素。

## 当前安全形势

> **注意：** 本信息反映截至**2025 年 12 月 18 日**的 MCP 安全标准。MCP 协议持续快速演进，未来实现可能引入新的身份验证模式和增强控制。请始终参考最新的[MCP 规范](https://spec.modelcontextprotocol.io/)、[MCP GitHub 仓库](https://github.com/modelcontextprotocol)和[安全最佳实践文档](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)获取最新指导。

### MCP 身份验证演进

MCP 规范在身份验证和授权方法上经历了显著演变：

- **最初方法**：早期规范要求开发者实现自定义身份验证服务器，MCP 服务器作为 OAuth 2.0 授权服务器直接管理用户身份验证
- **当前标准（2025-11-25）**：更新规范允许 MCP 服务器将身份验证委托给外部身份提供者（如 Microsoft Entra ID），提升安全态势并降低实现复杂度
- **传输层安全**：增强对本地（STDIO）和远程（可流式 HTTP）连接的安全传输机制支持，采用适当的身份验证模式

## 身份验证与授权安全

### 当前安全挑战

现代 MCP 实现面临多种身份验证和授权挑战：

### 风险与威胁向量

- **授权逻辑配置错误**：MCP 服务器中授权实现缺陷可能暴露敏感数据并错误应用访问控制
- **OAuth 令牌泄露**：本地 MCP 服务器令牌被盗，攻击者可冒充服务器访问下游服务
- **令牌透传漏洞**：不当令牌处理导致安全控制绕过和责任追踪缺失
- **过度权限**：MCP 服务器权限过大，违反最小权限原则，扩大攻击面

#### 令牌透传：关键反模式

**当前 MCP 授权规范明确禁止令牌透传**，因其带来严重安全隐患：

##### 安全控制规避  
- MCP 服务器和下游 API 实施关键安全控制（速率限制、请求验证、流量监控）依赖正确的令牌验证  
- 客户端直接使用 API 令牌绕过这些保护，破坏安全架构

##### 责任与审计难题  
- MCP 服务器无法区分使用上游颁发令牌的客户端，审计链断裂  
- 下游资源服务器日志显示误导性请求来源，非实际 MCP 服务器中介  
- 事件调查和合规审计大幅复杂化

##### 数据外泄风险  
- 未验证的令牌声明使持有被盗令牌的恶意者可利用 MCP 服务器作为数据外泄代理  
- 信任边界被破坏，允许绕过预期安全控制的未授权访问模式

##### 多服务攻击向量  
- 被多个服务接受的被盗令牌支持横向移动攻击  
- 服务间信任假设因无法验证令牌来源而受损

### 安全控制与缓解措施

**关键安全要求：**

> **强制要求**：MCP 服务器**不得接受任何非明确为该 MCP 服务器颁发的令牌**

#### 身份验证与授权控制

- **严格授权审查**：全面审计 MCP 服务器授权逻辑，确保仅允许预期用户和客户端访问敏感资源  
  - **实施指南**：[Azure API 管理作为 MCP 服务器身份验证网关](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
  - **身份集成**：[使用 Microsoft Entra ID 进行 MCP 服务器身份验证](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **安全令牌管理**：实施[微软令牌验证和生命周期最佳实践](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)  
  - 验证令牌受众声明与 MCP 服务器身份匹配  
  - 实施适当的令牌轮换和过期策略  
  - 防止令牌重放攻击和未授权使用

- **受保护的令牌存储**：令牌存储加密，确保存储和传输安全  
  - **最佳实践**：[安全令牌存储和加密指南](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### 访问控制实施

- **最小权限原则**：仅授予 MCP 服务器实现功能所需的最低权限  
  - 定期权限审查和更新，防止权限膨胀  
  - **微软文档**：[安全的最小权限访问](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **基于角色的访问控制（RBAC）**：实施细粒度角色分配  
  - 严格限定角色作用域至特定资源和操作  
  - 避免广泛或不必要权限扩大攻击面

- **持续权限监控**：实施持续访问审计和监控  
  - 监控权限使用模式异常  
  - 及时修正过度或未使用权限

## AI 特有安全威胁

### 提示注入与工具操控攻击

现代 MCP 实现面临复杂的 AI 特有攻击向量，传统安全措施难以完全防范：

#### **间接提示注入（跨域提示注入）**

**间接提示注入**是 MCP 支持的 AI 系统中最关键的漏洞之一。攻击者将恶意指令嵌入外部内容——文档、网页、电子邮件或数据源，AI 系统随后将其处理为合法命令。

**攻击场景：**  
- **基于文档的注入**：恶意指令隐藏在处理的文档中，触发意外 AI 行为  
- **网页内容利用**：被篡改网页包含嵌入提示，爬取时操控 AI 行为  
- **邮件攻击**：邮件中的恶意提示导致 AI 助手泄露信息或执行未授权操作  
- **数据源污染**：被破坏的数据库或 API 向 AI 系统提供受污染内容

**实际影响**：这些攻击可能导致数据外泄、隐私泄露、有害内容生成和用户交互操控。详见[Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)。

![Prompt Injection Attack Diagram](../../../translated_images/zh-CN/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **工具投毒攻击**

**工具投毒**针对定义 MCP 工具的元数据，利用 LLM 解释工具描述和参数以做出执行决策的方式。

**攻击机制：**  
- **元数据操控**：攻击者在工具描述、参数定义或使用示例中注入恶意指令  
- **隐形指令**：工具元数据中隐藏的提示被 AI 模型处理但对人类用户不可见  
- **动态工具修改（“拉地毯”）**：用户批准的工具后续被修改执行恶意操作，用户不知情  
- **参数注入**：恶意内容嵌入工具参数模式，影响模型行为

**托管服务器风险**：远程 MCP 服务器风险更高，工具定义可在用户初次批准后更新，导致原本安全的工具变为恶意。详见[Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)。

![Tool Injection Attack Diagram](../../../translated_images/zh-CN/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **其他 AI 攻击向量**

- **跨域提示注入（XPIA）**：利用多域内容绕过安全控制的复杂攻击  
- **动态能力修改**：实时更改工具能力，逃避初始安全评估  
- **上下文窗口投毒**：操控大上下文窗口隐藏恶意指令  
- **模型混淆攻击**：利用模型局限制造成不可预测或不安全行为

### AI 安全风险影响

**高影响后果：**  
- **数据外泄**：未授权访问和窃取敏感企业或个人数据  
- **隐私泄露**：个人身份信息（PII）和机密业务数据暴露  
- **系统操控**：关键系统和工作流的非预期修改  
- **凭据窃取**：身份验证令牌和服务凭据被攻破  
- **横向移动**：利用被攻破的 AI 系统作为更广泛网络攻击的跳板

### 微软 AI 安全解决方案

#### **AI Prompt Shields：针对注入攻击的高级防护**

微软**AI Prompt Shields**通过多层安全机制，全面防御直接和间接提示注入攻击：

##### **核心保护机制：**

1. **高级检测与过滤**  
   - 机器学习算法和自然语言处理技术检测外部内容中的恶意指令  
   - 实时分析文档、网页、邮件和数据源中的嵌入威胁  
   - 语境理解区分合法与恶意提示模式

2. **聚焦技术**  
   - 区分可信系统指令与潜在受损外部输入  
   - 文本转换方法增强模型相关性，同时隔离恶意内容  
   - 帮助 AI 系统维持正确指令层级，忽略注入命令

3. **分隔符与数据标记系统**  
   - 明确定义可信系统消息与外部输入文本边界  
   - 特殊标记突出可信与不可信数据源边界  
   - 清晰分离防止指令混淆和未授权命令执行

4. **持续威胁情报**  
   - 微软持续监控新兴攻击模式并更新防御  
   - 主动威胁狩猎新注入技术和攻击向量  
   - 定期安全模型更新，保持对不断演变威胁的有效性

5. **Azure 内容安全集成**  
   - 作为全面 Azure AI 内容安全套件的一部分  
   - 额外检测越狱尝试、有害内容和安全策略违规  
   - AI 应用组件间统一安全控制

**实施资源**：[微软 Prompt Shields 文档](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/zh-CN/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## 高级 MCP 安全威胁

### 会话劫持漏洞

**会话劫持**是有状态 MCP 实现中的关键攻击向量，未经授权方获取并滥用合法会话标识符，冒充客户端执行未授权操作。

#### **攻击场景与风险**

- **会话劫持提示注入**：攻击者利用被盗会话 ID 向共享会话状态的服务器注入恶意事件，可能触发有害操作或访问敏感数据  
- **直接冒充**：被盗会话 ID 允许绕过身份验证直接调用 MCP 服务器，将攻击者视为合法用户  
- **可恢复流被破坏**：攻击者可提前终止请求，导致合法客户端恢复时接收潜在恶意内容

#### **会话管理安全控制**

**关键要求：**
- **授权验证**：实现授权的 MCP 服务器**必须**验证所有入站请求，**不得**依赖会话进行身份验证
- **安全会话生成**：使用密码学安全的、非确定性的会话 ID，通过安全随机数生成器生成
- **用户特定绑定**：使用 `<user_id>:<session_id>` 等格式将会话 ID 绑定到用户特定信息，防止跨用户会话滥用
- **会话生命周期管理**：实施适当的过期、轮换和失效机制以限制漏洞窗口
- **传输安全**：所有通信必须使用 HTTPS 以防止会话 ID 被截获

### 混淆代理问题

**混淆代理问题**发生在 MCP 服务器作为客户端与第三方服务之间的身份验证代理时，攻击者通过静态客户端 ID 利用授权绕过的机会。

#### **攻击机制与风险**

- **基于 Cookie 的同意绕过**：先前的用户身份验证创建了同意 Cookie，攻击者通过恶意授权请求和精心构造的重定向 URI 利用这些 Cookie
- **授权码窃取**：现有同意 Cookie 可能导致授权服务器跳过同意页面，将授权码重定向到攻击者控制的端点  
- **未授权 API 访问**：被窃取的授权码允许令牌交换和用户冒充，无需明确批准

#### **缓解策略**

**强制控制：**
- **明确同意要求**：使用静态客户端 ID 的 MCP 代理服务器**必须**为每个动态注册的客户端获取用户同意
- **OAuth 2.1 安全实现**：遵循当前 OAuth 安全最佳实践，包括对所有授权请求使用 PKCE（代码交换证明密钥）
- **严格客户端验证**：严格验证重定向 URI 和客户端标识符以防止利用

### 令牌透传漏洞  

**令牌透传**是一种明显的反模式，指 MCP 服务器接受客户端令牌而不进行适当验证，直接转发给下游 API，违反 MCP 授权规范。

#### **安全影响**

- **控制规避**：客户端直接使用令牌访问 API，绕过关键的速率限制、验证和监控控制
- **审计轨迹破坏**：上游颁发的令牌使客户端身份识别变得不可能，破坏事件调查能力
- **基于代理的数据外泄**：未经验证的令牌使恶意行为者能够利用服务器作为代理进行未授权数据访问
- **信任边界违规**：当无法验证令牌来源时，下游服务的信任假设可能被破坏
- **多服务攻击扩展**：被接受的被破坏令牌可在多个服务间横向移动

#### **必要安全控制**

**不可协商的要求：**
- **令牌验证**：MCP 服务器**不得**接受非明确为 MCP 服务器颁发的令牌
- **受众验证**：始终验证令牌的受众声明与 MCP 服务器身份匹配
- **适当的令牌生命周期**：实施短期访问令牌并采用安全轮换机制


## AI 系统的供应链安全

供应链安全已超越传统软件依赖，涵盖整个 AI 生态系统。现代 MCP 实现必须严格验证和监控所有 AI 相关组件，因为每个组件都可能引入潜在漏洞，危及系统完整性。

### 扩展的 AI 供应链组件

**传统软件依赖：**
- 开源库和框架
- 容器镜像和基础系统  
- 开发工具和构建流水线
- 基础设施组件和服务

**AI 特定供应链元素：**
- **基础模型**：来自不同提供商的预训练模型，需验证来源
- **嵌入服务**：外部向量化和语义搜索服务
- **上下文提供者**：数据源、知识库和文档存储  
- **第三方 API**：外部 AI 服务、机器学习流水线和数据处理端点
- **模型工件**：权重、配置和微调模型变体
- **训练数据源**：用于模型训练和微调的数据集

### 全面供应链安全策略

#### **组件验证与信任**
- **来源验证**：集成前验证所有 AI 组件的来源、许可和完整性
- **安全评估**：对模型、数据源和 AI 服务进行漏洞扫描和安全审查
- **声誉分析**：评估 AI 服务提供商的安全记录和实践
- **合规验证**：确保所有组件符合组织安全和法规要求

#### **安全部署流水线**  
- **自动化 CI/CD 安全**：在自动化部署流水线中集成安全扫描
- **工件完整性**：对所有部署工件（代码、模型、配置）实施密码学验证
- **分阶段部署**：采用渐进式部署策略，在每个阶段进行安全验证
- **可信工件仓库**：仅从已验证的安全工件注册表和仓库部署

#### **持续监控与响应**
- **依赖扫描**：持续监控所有软件和 AI 组件依赖的漏洞
- **模型监控**：持续评估模型行为、性能漂移和安全异常
- **服务健康跟踪**：监控外部 AI 服务的可用性、安全事件和策略变更
- **威胁情报集成**：整合针对 AI 和机器学习安全风险的威胁情报源

#### **访问控制与最小权限**
- **组件级权限**：基于业务需求限制对模型、数据和服务的访问
- **服务账户管理**：实施权限最小化的专用服务账户
- **网络分段**：隔离 AI 组件，限制服务间网络访问
- **API 网关控制**：使用集中式 API 网关控制和监控对外部 AI 服务的访问

#### **事件响应与恢复**
- **快速响应程序**：建立补丁或替换受损 AI 组件的流程
- **凭据轮换**：自动化轮换密钥、API 密钥和服务凭据
- **回滚能力**：快速回退到先前已知良好版本的 AI 组件
- **供应链泄露恢复**：针对上游 AI 服务受损的专门响应程序

### Microsoft 安全工具与集成

**GitHub Advanced Security** 提供全面的供应链保护，包括：
- **秘密扫描**：自动检测仓库中的凭据、API 密钥和令牌
- **依赖扫描**：开源依赖和库的漏洞评估
- **CodeQL 分析**：静态代码分析，发现安全漏洞和编码问题
- **供应链洞察**：依赖健康和安全状态的可视化

**Azure DevOps 与 Azure Repos 集成：**
- 在 Microsoft 开发平台中无缝集成安全扫描
- Azure Pipelines 中针对 AI 工作负载的自动安全检查
- 安全 AI 组件部署的策略执行

**Microsoft 内部实践：**
Microsoft 在所有产品中实施了广泛的供应链安全实践。了解更多请参见 [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)。


## 基础安全最佳实践

MCP 实现继承并构建在组织现有安全态势之上。加强基础安全实践显著提升 AI 系统和 MCP 部署的整体安全性。

### 核心安全基础

#### **安全开发实践**
- **OWASP 合规**：防护 [OWASP Top 10](https://owasp.org/www-project-top-ten/) Web 应用漏洞
- **AI 特定防护**：实施 [OWASP LLM Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559) 控制措施
- **安全秘密管理**：使用专用保险库管理令牌、API 密钥和敏感配置数据
- **端到端加密**：实现所有应用组件和数据流的安全通信
- **输入验证**：严格验证所有用户输入、API 参数和数据源

#### **基础设施加固**
- **多因素认证**：所有管理和服务账户强制 MFA
- **补丁管理**：操作系统、框架和依赖的自动及时补丁
- **身份提供者集成**：通过企业身份提供者（Microsoft Entra ID、Active Directory）实现集中身份管理
- **网络分段**：逻辑隔离 MCP 组件，限制横向移动
- **最小权限原则**：所有系统组件和账户仅授予必要权限

#### **安全监控与检测**
- **全面日志记录**：详细记录 AI 应用活动，包括 MCP 客户端-服务器交互
- **SIEM 集成**：集中安全信息和事件管理，实现异常检测
- **行为分析**：利用 AI 监控系统和用户行为异常模式
- **威胁情报**：整合外部威胁源和妥协指标（IOC）
- **事件响应**：定义完善的安全事件检测、响应和恢复流程

#### **零信任架构**
- **永不信任，始终验证**：持续验证用户、设备和网络连接
- **微分段**：细粒度网络控制，隔离单个工作负载和服务
- **身份中心安全**：基于验证身份而非网络位置的安全策略
- **持续风险评估**：基于当前上下文和行为动态评估安全态势
- **条件访问**：基于风险因素、位置和设备信任的访问控制

### 企业集成模式

#### **Microsoft 安全生态集成**
- **Microsoft Defender for Cloud**：全面云安全态势管理
- **Azure Sentinel**：云原生 SIEM 和 SOAR，保护 AI 工作负载
- **Microsoft Entra ID**：企业身份和访问管理，支持条件访问策略
- **Azure Key Vault**：集中秘密管理，支持硬件安全模块（HSM）
- **Microsoft Purview**：AI 数据源和工作流的数据治理与合规

#### **合规与治理**
- **法规对齐**：确保 MCP 实现符合行业特定合规要求（GDPR、HIPAA、SOC 2）
- **数据分类**：对 AI 系统处理的敏感数据进行适当分类和处理
- **审计轨迹**：满足合规和取证调查的全面日志记录
- **隐私控制**：在 AI 系统架构中实施隐私设计原则
- **变更管理**：对 AI 系统变更进行正式安全审查流程

这些基础实践构建了坚实的安全基线，增强 MCP 特定安全控制的有效性，为 AI 驱动应用提供全面保护。

## 关键安全要点

- **分层安全方法**：结合基础安全实践（安全编码、最小权限、供应链验证、持续监控）与 AI 特定控制，实现全面防护

- **AI 特定威胁环境**：MCP 系统面临独特风险，包括提示注入、工具投毒、会话劫持、混淆代理问题、令牌透传漏洞和过度权限，需专门缓解措施

- **认证与授权卓越**：使用外部身份提供者（Microsoft Entra ID）实现强认证，强制令牌验证，绝不接受非明确颁发给 MCP 服务器的令牌

- **AI 攻击防护**：部署 Microsoft Prompt Shields 和 Azure Content Safety 防御间接提示注入和工具投毒攻击，同时验证工具元数据并监控动态变化

- **会话与传输安全**：使用密码学安全、非确定性且绑定用户身份的会话 ID，实施适当的会话生命周期管理，绝不使用会话进行身份验证

- **OAuth 安全最佳实践**：通过对动态注册客户端的明确用户同意、正确实现 OAuth 2.1（含 PKCE）和严格重定向 URI 验证，防止混淆代理攻击  

- **令牌安全原则**：避免令牌透传反模式，验证令牌受众声明，实施短期令牌和安全轮换，保持清晰信任边界

- **全面供应链安全**：对所有 AI 生态组件（模型、嵌入、上下文提供者、外部 API）施以与传统软件依赖同等的安全严谨性

- **持续演进**：紧跟快速发展的 MCP 规范，参与安全社区标准制定，保持协议成熟过程中的适应性安全态势

- **Microsoft 安全集成**：利用 Microsoft 全面安全生态（Prompt Shields、Azure Content Safety、GitHub Advanced Security、Entra ID）增强 MCP 部署保护

## 综合资源

### **官方 MCP 安全文档**
- [MCP 规范（当前：2025-11-25）](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP 安全最佳实践](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP 授权规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub 仓库](https://github.com/modelcontextprotocol)

### **安全标准与最佳实践**
- [OAuth 2.0 安全最佳实践 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web 应用安全](https://owasp.org/www-project-top-ten/)
- [OWASP LLM Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft 数字防御报告](https://aka.ms/mddr)

### **AI 安全研究与分析**
- [MCP 中的提示注入（Simon Willison）](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [工具投毒攻击（Invariant Labs）](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP 安全研究简报（Wiz Security）](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **微软安全解决方案**
- [Microsoft Prompt Shields 文档](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure 内容安全服务](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID 安全](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure 令牌管理最佳实践](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub 高级安全](https://github.com/security/advanced-security)

### **实施指南与教程**
- [将 Azure API 管理作为 MCP 认证网关](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID 与 MCP 服务器的认证](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [安全令牌存储与加密（视频）](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps 与供应链安全**
- [Azure DevOps 安全](https://azure.microsoft.com/products/devops)
- [Azure Repos 安全](https://azure.microsoft.com/products/devops/repos/)
- [微软供应链安全之旅](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **附加安全文档**

有关全面的安全指导，请参阅本节中的这些专业文档：

- **[MCP 安全最佳实践 2025](./mcp-security-best-practices-2025.md)** - MCP 实施的完整安全最佳实践
- **[Azure 内容安全实施](./azure-content-safety-implementation.md)** - Azure 内容安全集成的实用实施示例  
- **[MCP 安全控制 2025](./mcp-security-controls-2025.md)** - MCP 部署的最新安全控制和技术
- **[MCP 最佳实践快速参考](./mcp-best-practices.md)** - MCP 关键安全实践的快速参考指南

---

## 接下来

下一章：[第3章：入门](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
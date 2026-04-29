# 更新日志：面向初学者的 MCP 课程

本文档记录了面向初学者的模型上下文协议（MCP）课程的所有重要变更。变更按时间逆序记录（最新的变更排在最前）。

## 2026年4月11日

### 新课程、文档修正及依赖项更新

#### 新增课程内容

**模块 05 - 高级主题**
- **课程 5.17：使用 MCP 的对抗式多智能体推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): 新增全面指南，涵盖多智能体系统的对抗辩论模式
  - Mermaid 架构图：两个代理→共享 MCP 服务器→辩论记录→裁判→裁决
  - 用 Python 和 TypeScript 实现的共享 MCP 工具服务器（`web_search` + `run_python`）
  - 对立系统提示（支持 / 反对 / 裁判）明确工具使用要求
  - 用 Python、TypeScript 和 C# 编写的辩论协调器，管理轮次与参数路由
  - MCP `ClientSession` 连接协调器与真实工具调用
  - 用例表（幻觉检测、威胁建模、API 设计评审、事实验证、技术选型）
  - 安全考量：沙箱执行、工具调用验证、速率限制、审计日志
  - 结构化练习，包括三个实用场景（代码审查、架构决策、内容审核）

#### 文档修正

**模块 03 - 入门**
- **05-stdio-server/README.md**：修正不完整的 TypeScript stdio 服务器示例 — 添加缺失的传输实例化 (`new StdioServerTransport()`) 和 `server.connect(transport)` 调用，使其与该节中的 Python 和 .NET 示例一致
- **14-sampling/README.md**：修正拼写错误 — 把 `"Sampling is an davanced features"` 改为 `"Sampling is an advanced feature"`

#### 课程更新

**主 README.md**
- 在课程表中添加条目 5.17（使用 MCP 的对抗式多智能体推理），并提供新课程的直接链接

**05-AdvancedTopics/README.md**
- 在课程序列表中添加课程 5.17 行

**study_guide.md**
- 在高级主题的思维导图和文字描述中添加对抗式多智能体推理主题

#### 代码和安全修正

**模块 05 - 对抗智能体（`mcp-adversarial-agents`）**
- **安全修正 — 命令注入**：用 `execFile` + `promisify` 替换 TypeScript `run_python` 工具中的 `execSync` shell 插值，消除命令注入风险（由 LLM 控制的代码现在作为字面 argv 元素传递，无需 shell 参与）
- **MCP 工具循环连接**：更新 Python 辩论协调器，使用异步的 `AsyncAnthropic` 客户端（替代阻塞的同步 `Anthropic`），每个代理回合直接传递实时的 `ClientSession`，每回合通过 `session.list_tools()` 获取工具定义，并在循环中通过 `session.call_tool()` 调用工具，直到模型输出最终文本响应

#### 依赖更新

- 在多个包（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中将 `hono` 升级至 4.12.12
- 在 TypeScript 包中将 `@hono/node-server` 从 1.19.11 升级至 1.19.13
- 在 Python 包（10-StreamliningAIWorkflows 实验 3 和 4）中将 `cryptography` 从 46.0.5 升级至 46.0.7
- 在 10-StreamliningAIWorkflows inspector 中将 `lodash` 从 4.17.23 升级至 4.18.1

#### 翻译

- 同步 48 种以上语言的最新源改动（i18n 更新）

---

## 2026年2月5日

### 仓库范围的验证与导航改进

#### 新增课程内容

**模块 03 - 入门**
- **12-mcp-hosts/README.md**：新增 MCP 主机设置全面指南
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置示例
  - 所有主要主机的 JSON 配置模板
  - 传输类型比较表（stdio、SSE/HTTP、WebSocket）
  - 常见连接问题排查
  - 主机配置安全最佳实践

- **13-mcp-inspector/README.md**：新增 MCP Inspector 调试指南
  - 安装方法（npx、npm 全局安装、源码安装）
  - 通过 stdio 和 HTTP/SSE 连接服务器
  - 测试工具、资源和提示工作流程
  - VS Code 与 MCP Inspector 集成
  - 常见调试场景及解决方案

**模块 04 - 实践实现**
- **pagination/README.md**：新增分页实现指南
  - Python、TypeScript、Java 中的基于游标分页模式
  - 客户端分页处理
  - 游标设计策略（不透明 vs 结构化）
  - 性能优化建议

**模块 05 - 高级主题**
- **mcp-protocol-features/README.md**：新增协议特性深度解析
  - 进度通知实现
  - 请求取消模式
  - 资源模板 URI 模式
  - 服务器生命周期管理
  - 日志级别控制
  - 带 JSON-RPC 代码的错误处理模式

#### 导航修正（更新 24+ 文件）

**主模块 README 文件**
- 现在链接到首课和下一模块

**02-Security 子文件**
- 所有 5 个补充安全文档新增“下一步”导航：

**09-CaseStudy 文件**
- 所有案例研究文件拥有顺序导航：

**10-StreamliningAI 实验**
- 在模块 10 概览和模块 11 中新增“下一步”部分

#### 代码和内容修正

**SDK 及依赖更新**
- 修复 OpenAI 版本号为空，改为 `^4.95.0`
- SDK 版本从 `^1.8.0` 升级至 `>=1.26.0`
- MCP 版本依赖更新至 `>=1.26.0`

<strong>代码修正</strong>
- 修正无效模型名 `gpt-4o-mini` 为 `gpt-4.1-mini`

<strong>内容修正</strong>
- 修正链接 `READMEmd` 为 `README.md`
- 修正课程标题 `Module 1-3` 为 `Module 0-3`
- 修正大小写敏感路径
- 移除损坏重复的案例研究 5 内容

<strong>初学者指导改进</strong>
- 新增适当的介绍、学习目标和前置条件

#### 课程更新

**主 README.md**
- 在课程表添加条目 3.12（MCP 主机）、3.13（MCP Inspector）、4.1（分页）、5.16（协议特性）

**模块 README**
- 添加课程 12 和 13 至课程列表
- 添加“实践指南”部分，含分页链接
- 添加课程 5.15（自定义传输）和 5.16（协议特性）

**study_guide.md**
- 更新思维导图，包含所有新主题：MCP 主机设置、MCP Inspector、分页策略、协议特性深度解析

## 2026年1月28日

### MCP 规范 2025-11-25 合规性审查

#### 核心概念增强（01-CoreConcepts/）
- **新增客户端原语 - Roots**：添加关于 Roots 客户端原语的全面文档，使服务器能够理解文件系统边界和访问权限
- <strong>工具注释</strong>：新增工具行为注释文档（`readOnlyHint`、`destructiveHint`），以改进工具执行决策
- <strong>采样中的工具调用</strong>：更新采样文档，包含 `tools` 和 `toolChoice` 参数，用于模型主导的采样请求中的工具调用
- **URL 模式触发**：新增基于 URL 的触发文档，支持服务器发起的外部网页交互
- **任务（实验性）**：新增任务特性文档，介绍持久执行包装器和延迟结果检索
- <strong>图标支持</strong>：说明工具、资源、资源模板和提示可包含图标作为额外元数据

#### 文档更新
- **README.md**：新增 MCP 规范 2025-11-25 版本引用及日期版本说明
- **study_guide.md**：更新课程地图，包含任务和工具注释在核心概念部分；更新文档时间戳

#### 规范合规验证
- <strong>协议版本</strong>：验证所有文档引用当前 MCP 规范 2025-11-25
- <strong>架构对齐</strong>：确认两层架构（数据层 + 传输层）文档准确
- <strong>原语文档</strong>：验证服务器原语（资源、提示、工具）和客户端原语（采样、触发、日志、Roots）
- <strong>传输机制</strong>：核实 STDIO 和流式 HTTP 传输文档准确性
- <strong>安全指导</strong>：确认与当前 MCP 安全最佳实践文档一致

#### 关键 MCP 2025-11-25 特性文档
- **OpenID Connect 发现**：通过 OIDC 进行认证服务器发现
- **OAuth 客户端 ID 元数据文档**：推荐的客户端注册机制
- **JSON Schema 2020-12**：MCP 架构定义的默认方言
- **SDK 分级系统**：SDK 功能支持与维护的正式要求
- <strong>治理结构</strong>：MCP 治理中的工作组与利益组的形式化

### 安全文档重大更新（02-Security/）

#### MCP 安全峰会研讨会（Sherpa）集成
- <strong>新增动手培训资源</strong>：在所有安全文档中添加与 [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) 的全面集成
- <strong>远征路线覆盖</strong>：记录从基地营到峰会的完整营地进展
- **OWASP 对齐**：所有安全指导映射到 OWASP MCP Azure 安全指南风险

#### OWASP MCP Top 10 集成
- <strong>新增章节</strong>：主安全 README 加入 OWASP MCP Top 10 安全风险表及 Azure 减缓措施
- <strong>风险驱动文档</strong>：更新 mcp-security-controls-2025.md，针对每个安全领域增加 OWASP MCP 风险引用
- <strong>参考架构</strong>：关联 OWASP MCP Azure 安全指南参考架构与实现模式

#### 更新安全文件
- **README.md**：添加 Sherpa 研讨会概述、远征路线表、OWASP MCP Top 10 风险摘要和动手培训部分
- **mcp-security-controls-2025.md**：更新标题为 2026 年 2 月，增加 OWASP 风险引用（MCP01-MCP08），修正规范版本不一致问题
- **mcp-security-best-practices-2025.md**：新增 Sherpa 和 OWASP 资源部分，更新时间戳更新
- **mcp-best-practices.md**：新增动手培训部分，包含 Sherpa 和 OWASP 链接
- **azure-content-safety-implementation.md**：增加 OWASP MCP06 引用，Sherpa 营地 3 对齐及额外资源部分

#### 新增资源链接
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- 各个 OWASP MCP 风险页面（MCP01-MCP10）

### 课程范围内 MCP 规范 2025-11-25 对齐

#### 模块 03 - 入门
- **SDK 文档**：添加 Go SDK 至官方 SDK 列表；更新所有 SDK 引用以符合 MCP 规范 2025-11-25
- <strong>传输说明</strong>：更新 STDIO 和 HTTP 流传输描述，含具体规范引用

#### 模块 04 - 实践实现
- **SDK 更新**：新增 Go SDK；更新 SDK 列表带规范版本引用
- <strong>授权规范</strong>：更新 MCP 授权规范链接至当前 2025-11-25 版本

#### 模块 05 - 高级主题
- <strong>新特性</strong>：添加关于 MCP 规范 2025-11-25 新特性（任务、工具注释、URL 模式触发、Roots）的说明
- <strong>安全资源</strong>：新增 OWASP MCP Top 10 及 Sherpa 研讨会链接作为附加参考

#### 模块 06 - 社区贡献
- **SDK 列表**：新增 Swift 和 Rust SDK；更新规范链接到 2025-11-25
- <strong>规范引用</strong>：更新 MCP 规范链接至正式规范 URL

#### 模块 07 - 早期采用经验
- <strong>资源更新</strong>：添加 MCP 规范 2025-11-25 链接及 OWASP MCP Top 10 至附加资源

#### 模块 08 - 最佳实践
- <strong>规范版本</strong>：更新 MCP 规范引用为 2025-11-25
- <strong>安全资源</strong>：添加 OWASP MCP Top 10 和 Sherpa 研讨会至附加参考

#### 模块 10 - 简化 AI 工作流程
- <strong>徽章更新</strong>：将 MCP 版本徽章从 SDK 版本（1.9.3）改为规范版本（2025-11-25）
- <strong>资源链接</strong>：更新 MCP 规范链接；增加 OWASP MCP Top 10

#### 模块 11 - MCP 服务器实操实验
- <strong>规范引用</strong>：更新 MCP 规范链接至 2025-11-25 版本
- <strong>安全资源</strong>：新增 OWASP MCP Top 10 至官方资源

## 2025年12月18日
### 安全文档更新 - MCP 规范 2025-11-25

#### MCP 安全最佳实践 (02-Security/mcp-best-practices.md) - 规范版本更新
- <strong>协议版本更新</strong>：更新为最新 MCP 规范 2025-11-25（于 2025 年 11 月 25 日发布）
  - 将所有规范版本引用从 2025-06-18 更新为 2025-11-25
  - 将文档日期引用从 2025 年 8 月 18 日更新为 2025 年 12 月 18 日
  - 验证所有规范 URL 均指向当前文档
- <strong>内容验证</strong>：根据最新标准对安全最佳实践进行全面验证
  - <strong>微软安全解决方案</strong>：验证 Prompt Shields（前称“越狱风险检测”）、Azure 内容安全、Microsoft Entra ID 和 Azure 密钥保管的当前术语和链接
  - **OAuth 2.1 安全**：确认符合最新 OAuth 安全最佳实践
  - **OWASP 标准**：验证 LLMs 相关 OWASP Top 10 参考资料的时效性
  - **Azure 服务**：核实所有微软 Azure 文档链接和最佳实践
- <strong>标准对齐</strong>：确认所有引用的安全标准均为最新
  - NIST 人工智能风险管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳实践
  - Azure 安全与合规框架
- <strong>实施资源</strong>：验证所有实施指南链接和资源
  - Azure API 管理认证模式
  - Microsoft Entra ID 集成指南
  - Azure 密钥保管机密管理
  - DevSecOps 流水线与监控解决方案

### 文档质量保证
- <strong>规范合规</strong>：确保所有强制性 MCP 安全要求（必须/禁止）与最新规范匹配
- <strong>资源时效性</strong>：验证所有指向微软文档、安全标准和实施指南的外部链接
- <strong>最佳实践覆盖</strong>：确认涵盖身份验证、授权、AI 特有威胁、供应链安全和企业模式的全面性

## 2025 年 10 月 6 日

### 入门部分扩展 – 高级服务器用法 & 简单身份验证

#### 高级服务器用法 (03-GettingStarted/10-advanced)
- <strong>新增章节</strong>：新增全面高级 MCP 服务器用法指南，涵盖常规服务器与底层服务器架构
  - **常规 vs 底层服务器**：详细对比及 Python 和 TypeScript 代码示例
  - <strong>基于处理器的设计</strong>：解释基于处理器的工具/资源/提示管理，用于可扩展灵活的服务器实现
  - <strong>实用模式</strong>：实际场景中底层服务器模式对高级功能与架构的优势

#### 简单身份验证 (03-GettingStarted/11-simple-auth)
- <strong>新增章节</strong>：逐步指导 MCP 服务器中简单身份验证的实现
  - <strong>身份验证概念</strong>：清晰解释身份验证与授权及凭证处理
  - <strong>基础身份验证实现</strong>：基于中间件的 Python（Starlette）和 TypeScript（Express）身份认证模式及代码示例
  - <strong>向高级安全进阶</strong>：指导从简单认证过渡至 OAuth 2.1 和 RBAC，并提供高级安全模块参考

这些新增内容为构建更健壮、安全、灵活的 MCP 服务器实现提供了实操性指导，将基础概念与高级生产模式桥接。

## 2025 年 9 月 29 日

### MCP 服务器数据库集成实验室 - 全面实操学习路径

#### 11-MCPServerHandsOnLabs - 新增完整数据库集成课程
- **完整 13 实验学习路径**：新增用于构建生产级 MCP 服务器与 PostgreSQL 数据库集成的综合实操课程
  - <strong>真实案例</strong>：Zava 零售分析用例，展示企业级模式
  - <strong>结构化学习进阶</strong>：
    - **实验 00-03：基础** - 介绍、核心架构、安全与多租户、环境搭建
    - **实验 04-06：构建 MCP 服务器** - 数据库设计与架构、MCP 服务器实现、工具开发
    - **实验 07-09：高级功能** - 语义搜索集成、测试与调试、VS Code 集成
    - **实验 10-12：生产与最佳实践** - 部署策略、监控与可观测性、最佳实践与优化
  - <strong>企业技术</strong>：FastMCP 框架、带 pgvector 的 PostgreSQL、Azure OpenAI 嵌入、Azure 容器应用、应用洞察
  - <strong>高级功能</strong>：行级安全（RLS）、语义搜索、多租户数据访问、向量嵌入、实时监控

#### 术语标准化 - 模块改为实验
- <strong>全面文档更新</strong>：系统更新 11-MCPServerHandsOnLabs 中所有 README 文件，统一使用“实验”术语替代“模块”
  - <strong>章节标题</strong>：将“本模块涵盖内容”更新为“本实验涵盖内容”，覆盖所有 13 个实验
  - <strong>内容描述</strong>：文档中所有“This module provides...”更改为“This lab provides...”
  - <strong>学习目标</strong>：将“本模块结束时...”更改为“本实验结束时...”
  - <strong>导航链接</strong>：将所有“模块 XX:”引用统一转换为“实验 XX:”
  - <strong>完成跟踪</strong>：将“完成本模块后...”更新为“完成本实验后...”
  - <strong>技术引用保留</strong>：保留配置文件中 Python 模块引用（例如 `"module": "mcp_server.main"`）

#### 学习指南增强 (study_guide.md)
- <strong>课程地图可视化</strong>：新增“11.数据库集成实验”部分，直观展示实验结构
- <strong>仓库结构</strong>：从十个主章节更新为十一章节，详述 11-MCPServerHandsOnLabs
- <strong>学习路径指导</strong>：导航说明扩展至涵盖章节 00-11
- <strong>技术覆盖</strong>：补充 FastMCP、PostgreSQL、Azure 服务集成细节
- <strong>学习成果</strong>：强调生产级服务器开发、数据库集成模式与企业安全

#### 主 README 结构增强
- <strong>基于实验的术语</strong>：在 11-MCPServerHandsOnLabs 主要 README.md 中统一使用“实验”结构
- <strong>学习路径组织</strong>：清晰的基础概念到高级实现再到生产部署的渐进路径
- <strong>真实世界聚焦</strong>：强调实战操作及企业级模式与技术

### 文档质量与一致性改进
- <strong>实操学习重心</strong>：整个文档强化基于实验的实用学习方法
- <strong>企业模式重点</strong>：突出生产就绪实现与企业安全考量
- <strong>技术集成</strong>：全面涵盖现代 Azure 服务与 AI 集成模式
- <strong>学习进阶</strong>：明确、结构化的从基础到生产部署的学习路径

## 2025 年 9 月 26 日

### 案例研究增强 - GitHub MCP 注册中心集成

#### 案例研究 (09-CaseStudy/) - 生态系统发展重点
- **README.md**：大幅扩充，新增全面 GitHub MCP 注册中心案例研究
  - **GitHub MCP 注册中心案例**：详细分析 2025 年 9 月 GitHub MCP 注册中心上线
    - <strong>问题分析</strong>：深入探讨 MCP 服务器发现及部署的碎片化挑战
    - <strong>解决方案架构</strong>：GitHub 中心化注册机制及一键式 VS Code 安装
    - <strong>商业影响</strong>：对开发者入门效率及生产力的显著提升
    - <strong>战略价值</strong>：模块化代理部署与跨工具互操作的聚焦
    - <strong>生态系统发展</strong>：定位为代理集成的基础平台
  - <strong>增强案例结构</strong>：更新七个案例研究，格式一致且描述详实
    - Azure AI 旅游代理：多代理协调重点
    - Azure DevOps 集成：工作流程自动化重点
    - 实时文档检索：Python 控制台客户端实现
    - 交互式学习计划生成器：Chainlit 会话式 Web 应用
    - 编辑器内文档：VS Code 与 GitHub Copilot 集成
    - Azure API 管理：企业 API 集成模式
    - GitHub MCP 注册中心：生态发展及社区平台
  - <strong>全面总结</strong>：重写结论段落，突出涵盖多个 MCP 实现维度的七个案例
    - 企业集成、多代理协调、开发者生产力
    - 生态系统发展、教育应用分类
    - 加强对架构模式、实现策略与最佳实践的洞察
    - 强调 MCP 为成熟、生产就绪协议

#### 学习指南更新 (study_guide.md)
- <strong>课程地图可视化</strong>：更新思维导图，新增 GitHub MCP 注册中心于案例研究部分
- <strong>案例描述</strong>：由泛泛描写增强为七个全面案例研究的详细细分
- <strong>仓库结构</strong>：更新第 10 章节，反映全面案例研究覆盖及具体实现细节
- <strong>更变日志集成</strong>：新增 2025 年 9 月 26 日条目，记录 GitHub MCP 注册中心新增和案例研究增强
- <strong>日期更新</strong>：更新页脚时间戳为最新版本（2025 年 9 月 26 日）

### 文档质量改进
- <strong>一致性提升</strong>：统一七个案例实例的格式和结构
- <strong>全面覆盖</strong>：案例涵盖企业、开发者效率及生态系统发展场景
- <strong>战略定位</strong>：强化 MCP 作为代理系统部署基础平台的定位
- <strong>资源整合</strong>：更新额外资源包含 GitHub MCP 注册中心链接

## 2025 年 9 月 15 日

### 高级主题扩展 - 自定义传输与上下文工程

#### MCP 自定义传输 (05-AdvancedTopics/mcp-transport/) - 新高级实现指南
- **README.md**：完整自定义 MCP 传输机制实现指南
  - **Azure 事件网格传输**：全面的无服务器事件驱动传输实现
    - C#、TypeScript 和 Python 示例，集成 Azure Functions
    - 事件驱动架构模式，支持可扩展 MCP 解决方案
    - Webhook 接收器与推送消息处理
  - **Azure 事件中心传输**：高吞吐量流传输实现
    - 用于低延迟场景的实时流处理能力
    - 分区策略与检查点管理
    - 消息批处理与性能优化
  - <strong>企业集成模式</strong>：生产级架构示例
    - 跨多个 Azure Functions 的分布式 MCP 处理
    - 混合传输架构，组合多种传输类型
    - 消息持久性、可靠性及错误处理策略
  - <strong>安全与监控</strong>：Azure 密钥保管集成和可观测性方案
    - 托管身份认证和最小权限访问
    - 应用洞察遥测和性能监测
    - 断路器和容错模式
  - <strong>测试框架</strong>：自定义传输的全面测试策略
    - 使用测试替身和模拟框架的单元测试
    - 基于 Azure 测试容器的集成测试
    - 性能和负载测试考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新兴 AI 学科
- **README.md**：关于上下文工程作为新兴领域的全面探索
  - <strong>核心原则</strong>：完整上下文共享、动作决策感知、上下文窗口管理
  - **MCP 协议对齐**：MCP 设计如何应对上下文工程挑战
    - 上下文窗口限制和渐进加载策略
    - 相关性判定与动态上下文检索
    - 多模态上下文处理与安全考量
  - <strong>实现方法</strong>：单线程与多代理架构
    - 上下文切分与优先排序技术
    - 渐进式上下文加载与压缩策略
    - 分层上下文方法与检索优化
  - <strong>测量框架</strong>：用于上下文有效性评估的新兴指标
    - 输入效率、性能、质量与用户体验考虑
    - 上下文优化的实验方法
    - 失败分析与改进方法

#### 课程导航更新 (README.md)
- <strong>模块结构增强</strong>：更新课程表，新增高级主题
  - 添加上下文工程（5.14）和自定义传输（5.15）
  - 各模块格式和导航链接统一
  - 描述更新以反映当前内容范围

### 目录结构改进
- <strong>命名规范化</strong>：“mcp transport”重命名为“mcp-transport”，与其他高级主题文件夹保持一致
- <strong>内容组织</strong>：所有 05-AdvancedTopics 文件夹均遵循统一命名模式（mcp-[主题]）

### 文档质量提升
- **MCP 规范对齐**：所有新内容均参照现行 MCP 规范 2025-06-18
- <strong>多语言示例</strong>：提供全面 C#、TypeScript 和 Python 代码示例
- <strong>企业焦点</strong>：贯穿生产级模式和 Azure 云集成
- <strong>可视化文档</strong>：使用 Mermaid 图展示架构和流程

## 2025 年 8 月 18 日

### 文档全面更新 - MCP 2025-06-18 标准

#### MCP 安全最佳实践 (02-Security/) - 完整现代化 
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：根据 MCP 规范 2025-06-18 完全重写  
  - <strong>强制性要求</strong>：新增官方规范中的明确 MUST/MUST NOT 要求，带有清晰视觉指示  
  - **12 核心安全实践**：从 15 项列表重构为全面的安全领域  
    - 令牌安全与身份验证，集成外部身份提供者  
    - 会话管理与传输安全，含密码学要求  
    - AI 特定威胁防护，集成 Microsoft 提示盾牌  
    - 访问控制与权限，遵循最小权限原则  
    - 内容安全与监控，集成 Azure 内容安全  
    - 供应链安全，全面组件验证  
    - OAuth 安全与混淆代理防护，实施 PKCE  
    - 事件响应与恢复，自动化能力  
    - 合规与治理，符合监管要求  
    - 高级安全控制，零信任架构  
    - Microsoft 安全生态系统集成，全面解决方案  
    - 持续安全演进，自适应实践  
  - **Microsoft 安全解决方案**：增强 Prompt Shields、Azure 内容安全、Entra ID 和 GitHub 高级安全的集成指导  
  - <strong>实施资源</strong>：按官方 MCP 文档、Microsoft 安全解决方案、安全标准和实施指南分类的综合资源链接  

#### 高级安全控制（02-Security/）- 企业实施  
- **MCP-SECURITY-CONTROLS-2025.md**：企业级安全框架全面改革  
  - **9 个全面安全领域**：从基础控制扩展为详细企业框架  
    - 高级身份验证与授权，集成 Microsoft Entra ID  
    - 令牌安全与防透传控件，全面验证  
    - 会话安全控件，防止劫持  
    - AI 特定安全控件，防止提示注入与工具污染  
    - 混淆代理攻击防护，OAuth 代理安全  
    - 工具执行安全，沙箱与隔离  
    - 供应链安全控件，依赖项验证  
    - 监控与检测控件，SIEM 集成  
    - 事件响应与恢复，自动化能力  
  - <strong>实施示例</strong>：新增详细 YAML 配置块与代码示例  
  - <strong>微软解决方案集成</strong>：全面涵盖 Azure 安全服务、GitHub 高级安全及企业身份管理  

#### 高级主题安全（05-AdvancedTopics/mcp-security/）- 生产就绪实施  
- **README.md**：企业安全实施完全重写  
  - <strong>当前规范对齐</strong>：更新至 MCP 规范 2025-06-18，含强制安全要求  
  - <strong>增强身份验证</strong>：集成 Microsoft Entra ID，包含全面 .NET 与 Java Spring Security 示例  
  - **AI 安全集成**：Microsoft 提示盾牌与 Azure 内容安全实现，含详细 Python 示例  
  - <strong>高级威胁缓解</strong>：详细实现示例涵盖  
    - 混淆代理攻击防护，PKCE 与用户同意验证  
    - 令牌透传防护，包含受众验证与安全令牌管理  
    - 会话劫持防护，密码学绑定及行为分析  
  - <strong>企业安全集成</strong>：Azure 应用洞察监控、威胁检测管道与供应链安全  
  - <strong>实施检查清单</strong>：明确强制与推荐安全控件及 Microsoft 安全生态系统优势  

### 文档质量与标准对齐  
- <strong>规范引用</strong>：更新所有引用至当前 MCP 规范 2025-06-18  
- <strong>微软安全生态系统</strong>：全篇安全文档增强集成指导  
- <strong>实际实施</strong>：新增 .NET、Java 与 Python 详细代码示例，涵盖企业模式  
- <strong>资源组织</strong>：官方文档、安全标准与实施指南的综合分类  
- <strong>视觉指示</strong>：清晰标记强制要求与推荐实践  

#### 核心概念（01-CoreConcepts/）- 完整现代化  
- <strong>协议版本更新</strong>：引用当前 MCP 规范 2025-06-18，采用日期版本格式（YYYY-MM-DD）  
- <strong>架构精炼</strong>：增强 Hosts、Clients 与 Servers 说明，反映当前 MCP 架构模式  
  - Hosts 清晰定义为协调多个 MCP 客户端连接的 AI 应用  
  - Clients 描述为维护一对一服务器关系的协议连接器  
  - Servers 增强本地与远程部署场景描述  
- <strong>原语重构</strong>：服务器与客户端原语完全重写  
  - 服务器原语：资源（数据源）、提示（模板）、工具（可执行功能），附详细说明及示例  
  - 客户端原语：采样（LLM 完成）、引导（用户输入）、日志（调试/监控）  
  - 更新当前发现（`*/list`）、检索（`*/get`）、执行（`*/call`）方法模式  
- <strong>协议架构</strong>：引入双层架构模型  
  - 数据层：基于 JSON-RPC 2.0，含生命周期管理及原语  
  - 传输层：STDIO（本地）及可流 HTTP 含 SSE（远程）传输机制  
- <strong>安全框架</strong>：全面安全原则，含明确用户同意、数据隐私保护、工具执行安全及传输层安全  
- <strong>通信模式</strong>：更新协议消息，展示初始化、发现、执行与通知流程  
- <strong>代码示例</strong>：刷新多语言示例（.NET、Java、Python、JavaScript），反映当前 MCP SDK 模式  

#### 安全（02-Security/）- 全面安全革新  
- <strong>标准对齐</strong>：完全符合 MCP 规范 2025-06-18 安全要求  
- <strong>身份验证演进</strong>：记录从自定义 OAuth 服务器到外部身份提供者委托（Microsoft Entra ID）的演进  
- **AI 特定威胁分析**：增强现代 AI 攻击向量覆盖  
  - 详细提示注入攻击场景及真实案例  
  - 工具污染机制与“地毯式撤销”攻击模式  
  - 上下文窗口污染及模型混淆攻击  
- **微软 AI 安全解决方案**：全面涵盖 Microsoft 安全生态  
  - AI 提示盾牌，含高级检测、聚光灯与分隔符技术  
  - Azure 内容安全集成模式  
  - GitHub 高级安全保护供应链  
- <strong>高级威胁缓解</strong>：详细安全控制涵盖  
  - MCP 特有会话劫持攻击场景及密码学会话 ID 要求  
  - MCP 代理场景混淆代理问题及明确同意要求  
  - 令牌透传漏洞及强制验证控件  
- <strong>供应链安全</strong>：扩大 AI 供应链覆盖，包括基础模型、嵌入服务、上下文提供者及第三方 API  
- <strong>基础设施安全</strong>：强化企业安全模式集成，如零信任架构与 Microsoft 安全生态  
- <strong>资源组织</strong>：按类型分类全面资源链接（官方文档、标准、研究、Microsoft 解决方案、实施指南）  

### 文档质量提升  
- <strong>结构化学习目标</strong>：增强具体、可操作的学习成果  
- <strong>交叉引用</strong>：添加相关安全与核心概念主题链接  
- <strong>信息更新</strong>：更新所有日期引用及规范链接至当前标准  
- <strong>实施指导</strong>：在两个章节中增加具体、可行动的实施指导  

## 2025 年 7 月 16 日

### README 与导航改进  
- 完全重新设计 README.md 中的课程导航  
- 用更易访问的表格格式替换 `<details>` 标签  
- 在新“alternative_layouts”文件夹中创建替代布局选项  
- 添加基于卡片、标签样式及手风琴样式的导航示例  
- 更新仓库结构章节，包含所有最新文件  
- 增强“如何使用本课程”部分，提供明确建议  
- 更新 MCP 规范链接，指向正确 URL  
- 为课程结构添加上下文工程部分（5.14）  

### 学习指南更新  
- 完全修订学习指南，使其与当前仓库结构对齐  
- 新增 MCP 客户端与工具，以及流行 MCP 服务器章节  
- 更新视觉课程图，准确反映所有主题  
- 增强高级主题描述，涵盖所有专业领域  
- 更新案例研究章节，反映真实示例  
- 添加此综合变更日志  

### 社区贡献（06-CommunityContributions/）  
- 添加有关图像生成 MCP 服务器的详细信息  
- 新增 VSCode 中使用 Claude 的全面章节  
- 添加 Cline 终端客户端的设置及使用说明  
- 更新 MCP 客户端章节，包含所有流行客户端选项  
- 强化贡献示例，提供更准确的代码样本  

### 高级主题（05-AdvancedTopics/）  
- 统一命名整理所有专题文件夹  
- 添加上下文工程材料与示例  
- 增加 Foundry 代理集成文档  
- 强化 Entra ID 安全集成文档  

## 2025 年 6 月 11 日

### 初始创建  
- 发布 MCP 入门课程的第一个版本  
- 创建全部 10 个主章节的基础结构  
- 实现视觉课程导航图  
- 添加多语言示例项目  

### 入门（03-GettingStarted/）  
- 创建第一个服务器实现示例  
- 添加客户端开发指导  
- 包含 LLM 客户端集成说明  
- 添加 VS Code 集成文档  
- 实现服务器发送事件（SSE）服务器示例  

### 核心概念（01-CoreConcepts/）  
- 添加客户端-服务器架构详细解释  
- 创建关键协议组件文档  
- 记录 MCP 消息模式  

## 2025 年 5 月 23 日

### 仓库结构  
- 初始化仓库，建立基础文件夹结构  
- 为各主要章节创建 README 文件  
- 设置翻译基础设施  
- 添加图片资源和图示  

### 文档  
- 创建初始 README.md，包含课程概述  
- 添加行为准则（CODE_OF_CONDUCT.md）与安全（SECURITY.md）文档  
- 设置支持说明（SUPPORT.md），提供求助指导  
- 创建初步学习指南结构  

## 2025 年 4 月 15 日

### 规划与框架  
- MCP 入门课程的初步规划  
- 定义学习目标与目标受众  
- 概述课程的 10 部分结构  
- 制定示例与案例研究的概念框架  
- 创建关键概念的初始原型示例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行了翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文档的原始语言版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
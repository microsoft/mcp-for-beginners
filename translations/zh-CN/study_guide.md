# 面向初学者的模型上下文协议 (MCP) 学习指南

本学习指南概述了“面向初学者的模型上下文协议 (MCP)”课程的仓库结构和内容。使用本指南可有效导航仓库，充分利用可用资源。

## 仓库概述

模型上下文协议 (MCP) 是 AI 模型与客户端应用之间交互的标准化框架。最初由 Anthropic 创建，现由更广泛的 MCP 社区通过官方 GitHub 组织维护。本仓库提供全面的课程，包含 C#、Java、JavaScript、Python 和 TypeScript 的实操代码示例，面向 AI 开发者、系统架构师和软件工程师。

## 视觉课程地图

```mermaid
mindmap
  root((初学者 MCP))
    00. 介绍
      ::icon(fa fa-book)
      (协议概述)
      (标准化优势)
      (实际应用案例)
      (AI 集成基础)
    01. 核心概念
      ::icon(fa fa-puzzle-piece)
      (客户端-服务器架构)
      (协议组件)
      (消息模式)
      (传输机制)
      (任务 - 试验性)
      (工具注释)
    02. 安全
      ::icon(fa fa-shield)
      (AI 特有威胁)
      (2025 年最佳实践)
      (Azure 内容安全)
      (认证与授权)
      (微软提示防护)
      (OWASP MCP 前 10)
      (Sherpa 安全研讨会)
    03. 入门指南
      ::icon(fa fa-rocket)
      (首个服务器实现)
      (客户端开发)
      (LLM 客户端集成)
      (VS Code 扩展)
      (SSE 服务器设置)
      (HTTP 流)
      (AI 工具包集成)
      (测试框架)
      (高级服务器使用)
      (简单认证)
      (部署策略)
      (MCP 主机设置)
      (MCP 检查器)
    04. 实践实现
      ::icon(fa fa-code)
      (多语言 SDK)
      (测试与调试)
      (提示模板)
      (示例项目)
      (生产模式)
      (分页策略)
    05. 高级主题
      ::icon(fa fa-graduation-cap)
      (上下文工程)
      (Foundry 代理集成)
      (多模态 AI 工作流)
      (OAuth2 认证)
      (实时搜索)
      (流协议)
      (根上下文)
      (路由策略)
      (采样技术)
      (扩展方案)
      (安全加固)
      (Entra ID 集成)
      (网页搜索 MCP)
      (协议特性深度解析)
      (对抗性多代理推理)
      
    06. 社区
      ::icon(fa fa-users)
      (代码贡献)
      (文档)
      (MCP 客户端生态)
      (MCP 服务器注册表)
      (图像生成工具)
      (GitHub 协作)
    07. 早期采用
      ::icon(fa fa-lightbulb)
      (生产部署)
      (微软 MCP 服务器)
      (Azure MCP 服务)
      (企业案例研究)
      (未来路线图)
    08. 最佳实践
      ::icon(fa fa-check)
      (性能优化)
      (容错能力)
      (系统韧性)
      (监控与可观测性)
    09. 案例研究
      ::icon(fa fa-file-text)
      (Azure API 管理)
      (AI 旅行代理)
      (Azure DevOps 集成)
      (文档 MCP)
      (GitHub MCP 注册表)
      (VS Code 集成)
      (实际应用实现)
    10. 实操研讨会
      ::icon(fa fa-laptop)
      (MCP 服务器基础)
      (高级开发)
      (AI 工具包集成)
      (生产部署)
      (4 实验室结构)
    11. 数据库集成实验室
      ::icon(fa fa-database)
      (PostgreSQL 集成)
      (零售分析用例)
      (行级安全)
      (语义搜索)
      (生产部署)
      (13 实验室结构)
      (实操学习)
```
## 仓库结构

仓库分为十一大部分，每部分聚焦 MCP 的不同方面：

1. **介绍 (00-Introduction/)**
   - 模型上下文协议概述
   - 标准化在 AI 流水线中的重要性
   - 实际用例和优势

2. **核心概念 (01-CoreConcepts/)**
   - 客户端-服务器架构
   - 关键协议组成部分
   - MCP 中的消息模式

3. **安全 (02-Security/)**
   - 基于 MCP 系统的安全威胁
   - 安全实现最佳实践
   - 认证和授权策略
   - <strong>全面的安全文档</strong>：
     - MCP 2025 年安全最佳实践
     - Azure 内容安全实施指南
     - MCP 安全控制及技术
     - MCP 最佳实践速查
   - <strong>关键安全议题</strong>：
     - 提示注入与工具投毒攻击
     - 会话劫持与混淆代表问题
     - 令牌透传漏洞
     - 过度权限与访问控制
     - AI 组件的供应链安全
     - Microsoft 提示防护集成

4. **入门 (03-GettingStarted/)**
   - 环境搭建与配置
   - 创建基础 MCP 服务器与客户端
   - 与现有应用集成
   - 包含内容：
     - 第一个服务器实现
     - 客户端开发
     - 大语言模型客户端整合
     - VS Code 集成
     - 服务器推送事件 (SSE) 服务器
     - 高级服务器使用
     - HTTP 流传输
     - AI 工具包集成
     - 测试策略
     - 部署指导

5. **实践实现 (04-PracticalImplementation/)**
   - 跨语言 SDK 使用
   - 调试、测试与验证技术
   - 可复用提示模板与工作流设计
   - 实例项目与实现示例

6. **高级主题 (05-AdvancedTopics/)**
   - 上下文工程技术
   - Foundry 代理集成
   - 多模态 AI 工作流
   - OAuth2 认证演示
   - 实时搜索功能
   - 实时流处理
   - 根上下文实现
   - 路由策略
   - 采样技术
   - 扩展方法
   - 安全考量
   - Entra ID 安全集成
   - 网络搜索集成
   - 对抗式多代理推理（辩论模式）

7. **社区贡献 (06-CommunityContributions/)**
   - 如何贡献代码和文档
   - 通过 GitHub 合作
   - 社区驱动的增强与反馈
   - 利用多种 MCP 客户端（Claude Desktop、Cline、VSCode）
   - 使用流行 MCP 服务器包括图像生成

8. **早期应用经验 (07-LessonsfromEarlyAdoption/)**
   - 真实案例与成功故事
   - 构建与部署基于 MCP 的解决方案
   - 趋势和未来路线图
   - **Microsoft MCP 服务器指南**：涵盖 10 个生产就绪的 Microsoft MCP 服务器：
     - Microsoft Learn Docs MCP 服务器
     - Azure MCP 服务器（15+ 个专业连接器）
     - GitHub MCP 服务器
     - Azure DevOps MCP 服务器
     - MarkItDown MCP 服务器
     - SQL Server MCP 服务器
     - Playwright MCP 服务器
     - Dev Box MCP 服务器
     - Azure AI Foundry MCP 服务器
     - Microsoft 365 Agents Toolkit MCP 服务器

9. **最佳实践 (08-BestPractices/)**
   - 性能调优与优化
   - 设计容错型 MCP 系统
   - 测试和弹性策略

10. **案例研究 (09-CaseStudy/)**
    - <strong>七个全面案例研究</strong> 展示 MCP 在多样场景中的灵活应用：
    - **Azure AI 旅行代理**：Azure OpenAI 与 AI 搜索的多代理编排
    - **Azure DevOps 集成**：自动化工作流，使用 YouTube 数据更新
    - <strong>实时文档检索</strong>：基于 Python 控制台客户端与 HTTP 流
    - <strong>交互式学习计划生成器</strong>：Chainlit Web 应用与对话 AI
    - <strong>编辑器内文档</strong>：VS Code 集成 GitHub Copilot 工作流
    - **Azure API 管理**：企业 API 集成与 MCP 服务器创建
    - **GitHub MCP 注册中心**：生态系统开发与代理集成平台
    - 涵盖企业集成、开发者效率和生态系统开发的实现示例

11. **实操工作坊 (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - 融合 MCP 与 AI 工具包的全面实操工作坊
    - 构建智能应用，实现 AI 模型与现实工具的桥接
    - 涵盖基础、自定义服务器开发及生产部署策略的实用模块
    - <strong>实验结构</strong>：
      - 实验 1：MCP 服务器基础
      - 实验 2：高级 MCP 服务器开发
      - 实验 3：AI 工具包集成
      - 实验 4：生产部署与扩展
    - 基于实验的学习方法，逐步指导

12. **MCP 服务器数据库集成实验 (11-MCPServerHandsOnLabs/)**
    - **涵盖 13 个实验的完整学习路径**，构建生产就绪的集成 PostgreSQL 的 MCP 服务器
    - <strong>真实零售数据分析实现</strong>，使用 Zava Retail 用例
    - <strong>企业级模式</strong>，包括行级安全 (RLS)、语义搜索和多租户数据访问
    - <strong>完整实验结构</strong>：
      - **实验 00-03：基础知识** - 介绍、架构、安全、环境搭建
      - **实验 04-06：建立 MCP 服务器** - 数据库设计、MCP 服务器实现、工具开发
      - **实验 07-09：高级功能** - 语义搜索、测试调试、VS Code 集成
      - **实验 10-12：生产和最佳实践** - 部署、监控、优化
    - <strong>涵盖技术</strong>：FastMCP 框架、PostgreSQL、Azure OpenAI、Azure 容器应用、应用程序洞察
    - <strong>学习成果</strong>：生产就绪 MCP 服务器、数据库集成模式、AI 驱动分析、企业安全

## 附加资源

仓库还包括支持资源：

- **Images 文件夹**：课程中使用的图表和示意图
- <strong>翻译</strong>：多语言支持，文档自动翻译
- **官方 MCP 资源**：
  - [MCP 文档](https://modelcontextprotocol.io/)
  - [MCP 规范](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub 仓库](https://github.com/modelcontextprotocol)

## 如何使用本仓库

1. <strong>顺序学习</strong>：按章节顺序（00 至 11）获得结构化学习体验。
2. <strong>语言专注</strong>：如关注某编程语言，可浏览对应样例目录中的实现。
3. <strong>实践入门</strong>：从“入门”章节开始，搭建环境并创建首个 MCP 服务器和客户端。
4. <strong>高级探究</strong>：掌握基础后，深入高级主题扩展知识。
5. <strong>社区参与</strong>：通过 GitHub 讨论和 Discord 频道加入 MCP 社区，与专家和同行开发者交流。

## MCP 客户端与工具

课程覆盖多种 MCP 客户端和工具：

1. <strong>官方客户端</strong>：
   - Visual Studio Code
   - Visual Studio Code 中的 MCP
   - Claude Desktop
   - VSCode 中的 Claude
   - Claude API

2. <strong>社区客户端</strong>：
   - Cline（终端版）
   - Cursor（代码编辑器）
   - ChatMCP
   - Windsurf

3. **MCP 管理工具**：
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## 流行的 MCP 服务器

仓库介绍多种 MCP 服务器，包括：

1. **微软官方 MCP 服务器**：
   - Microsoft Learn Docs MCP 服务器
   - Azure MCP 服务器（15+ 专业连接器）
   - GitHub MCP 服务器
   - Azure DevOps MCP 服务器
   - MarkItDown MCP 服务器
   - SQL Server MCP 服务器
   - Playwright MCP 服务器
   - Dev Box MCP 服务器
   - Azure AI Foundry MCP 服务器
   - Microsoft 365 Agents Toolkit MCP 服务器

2. <strong>官方参考服务器</strong>：
   - 文件系统
   - Fetch
   - 内存
   - 顺序思考

3. <strong>图像生成</strong>：
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. <strong>开发工具</strong>：
   - Git MCP
   - 终端控制
   - 代码助手

5. <strong>专业服务器</strong>：
   - Salesforce
   - Microsoft Teams
   - Jira 与 Confluence

## 贡献

本仓库欢迎社区贡献。参见社区贡献章节，了解如何有效为 MCP 生态系统贡献力量。

----

*本学习指南最后更新于 2026 年 2 月 5 日，反映最新的 MCP 规范 2025-11-25，并提供当日仓库概览。仓库内容可能在此日期之后更新。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档是使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译的。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误译负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
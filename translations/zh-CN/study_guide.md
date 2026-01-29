# 初学者的模型上下文协议 (MCP) - 学习指南

本学习指南概述了“初学者的模型上下文协议 (MCP)”课程的仓库结构和内容。使用此指南可以高效浏览仓库并充分利用可用资源。

## 仓库概述

模型上下文协议 (MCP) 是一个标准化框架，用于 AI 模型与客户端应用之间的交互。MCP 最初由 Anthropic 创建，目前由更广泛的 MCP 社区通过官方 GitHub 组织进行维护。本仓库提供了全面的课程内容，包括 C#、Java、JavaScript、Python 和 TypeScript 的代码示例，专为 AI 开发者、系统架构师和软件工程师设计。

## 可视化课程地图

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```


## 仓库结构

仓库分为十一大部分，每部分专注于 MCP 的不同方面：

1. **简介 (00-Introduction/)**
   - 模型上下文协议概述
   - 标准化在 AI 流水线中的重要性
   - 实际应用场景和优势

2. **核心概念 (01-CoreConcepts/)**
   - 客户端-服务器架构
   - 协议的关键组件
   - MCP 中的消息传递模式

3. **安全性 (02-Security/)**
   - MCP 系统中的安全威胁
   - 实现安全性的最佳实践
   - 身份验证和授权策略
   - **全面的安全文档**：
     - MCP 安全最佳实践 2025
     - Azure 内容安全实施指南
     - MCP 安全控制和技术
     - MCP 快速参考最佳实践
   - **关键安全主题**：
     - 提示注入和工具污染攻击
     - 会话劫持和混淆代理问题
     - 令牌传递漏洞
     - 过度权限和访问控制
     - AI 组件的供应链安全
     - Microsoft Prompt Shields 集成

4. **入门 (03-GettingStarted/)**
   - 环境设置和配置
   - 创建基本的 MCP 服务器和客户端
   - 与现有应用集成
   - 包括以下部分：
     - 第一个服务器实现
     - 客户端开发
     - LLM 客户端集成
     - VS Code 集成
     - 服务器发送事件 (SSE) 服务器
     - 高级服务器使用
     - HTTP 流式传输
     - AI 工具包集成
     - 测试策略
     - 部署指南

5. **实践实现 (04-PracticalImplementation/)**
   - 使用不同编程语言的 SDK
   - 调试、测试和验证技术
   - 创建可重用的提示模板和工作流
   - 实现示例的项目样本

6. **高级主题 (05-AdvancedTopics/)**
   - 上下文工程技术
   - Foundry 代理集成
   - 多模态 AI 工作流
   - OAuth2 身份验证演示
   - 实时搜索功能
   - 实时流式传输
   - 根上下文实现
   - 路由策略
   - 采样技术
   - 扩展方法
   - 安全性考虑
   - Entra ID 安全集成
   - Web 搜索集成

7. **社区贡献 (06-CommunityContributions/)**
   - 如何贡献代码和文档
   - 通过 GitHub 协作
   - 社区驱动的增强和反馈
   - 使用各种 MCP 客户端（Claude Desktop、Cline、VSCode）
   - 使用流行的 MCP 服务器，包括图像生成

8. **早期采用的经验教训 (07-LessonsfromEarlyAdoption/)**
   - 实际实施和成功案例
   - 构建和部署基于 MCP 的解决方案
   - 趋势和未来路线图
   - **Microsoft MCP 服务器指南**：涵盖 10 个生产级 Microsoft MCP 服务器的全面指南，包括：
     - Microsoft Learn Docs MCP 服务器
     - Azure MCP 服务器（15+ 专用连接器）
     - GitHub MCP 服务器
     - Azure DevOps MCP 服务器
     - MarkItDown MCP 服务器
     - SQL Server MCP 服务器
     - Playwright MCP 服务器
     - Dev Box MCP 服务器
     - Azure AI Foundry MCP 服务器
     - Microsoft 365 Agents Toolkit MCP 服务器

9. **最佳实践 (08-BestPractices/)**
   - 性能调优和优化
   - 设计容错 MCP 系统
   - 测试和弹性策略

10. **案例研究 (09-CaseStudy/)**
    - **七个全面的案例研究**展示 MCP 在不同场景中的多样性：
    - **Azure AI 旅行代理**：使用 Azure OpenAI 和 AI 搜索进行多代理编排
    - **Azure DevOps 集成**：通过 YouTube 数据更新自动化工作流程
    - **实时文档检索**：带有流式 HTTP 的 Python 控制台客户端
    - **交互式学习计划生成器**：使用 Chainlit Web 应用和对话式 AI
    - **编辑器内文档**：VS Code 集成与 GitHub Copilot 工作流
    - **Azure API 管理**：企业 API 集成与 MCP 服务器创建
    - **GitHub MCP 注册表**：生态系统开发和代理集成平台
    - 实现示例涵盖企业集成、开发者生产力和生态系统开发

11. **动手工作坊 (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - 综合动手工作坊，结合 MCP 和 AI 工具包
    - 构建将 AI 模型与现实工具连接的智能应用
    - 实用模块涵盖基础知识、自定义服务器开发和生产部署策略
    - **实验室结构**：
      - 实验室 1：MCP 服务器基础知识
      - 实验室 2：高级 MCP 服务器开发
      - 实验室 3：AI 工具包集成
      - 实验室 4：生产部署和扩展
    - 基于实验室的学习方法，提供分步指导

12. **MCP 服务器数据库集成实验室 (11-MCPServerHandsOnLabs/)**
    - **全面的 13 个实验室学习路径**，用于构建与 PostgreSQL 集成的生产级 MCP 服务器
    - **基于 Zava 零售的实际零售分析实现**
    - **企业级模式**，包括行级安全 (RLS)、语义搜索和多租户数据访问
    - **完整实验室结构**：
      - **实验室 00-03：基础** - 介绍、架构、安全性、环境设置
      - **实验室 04-06：构建 MCP 服务器** - 数据库设计、MCP 服务器实现、工具开发
      - **实验室 07-09：高级功能** - 语义搜索、测试与调试、VS Code 集成
      - **实验室 10-12：生产与最佳实践** - 部署、监控、优化
    - **涵盖的技术**：FastMCP 框架、PostgreSQL、Azure OpenAI、Azure 容器应用、应用洞察
    - **学习成果**：生产级 MCP 服务器、数据库集成模式、AI 驱动的分析、企业安全

## 附加资源

仓库包括以下支持资源：

- **图片文件夹**：包含课程中使用的图表和插图
- **翻译**：多语言支持，提供文档的自动翻译
- **官方 MCP 资源**：
  - [MCP 文档](https://modelcontextprotocol.io/)
  - [MCP 规范](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub 仓库](https://github.com/modelcontextprotocol)

## 如何使用此仓库

1. **顺序学习**：按章节顺序学习（00 到 11），以获得结构化的学习体验。
2. **特定语言重点**：如果您对某种编程语言感兴趣，请浏览样本目录以查看您偏好的语言实现。
3. **实践实现**：从“入门”部分开始，设置环境并创建您的第一个 MCP 服务器和客户端。
4. **高级探索**：掌握基础知识后，深入高级主题以扩展您的知识。
5. **社区参与**：通过 GitHub 讨论和 Discord 频道加入 MCP 社区，与专家和其他开发者交流。

## MCP 客户端和工具

课程涵盖了各种 MCP 客户端和工具：

1. **官方客户端**：
   - Visual Studio Code
   - MCP 在 Visual Studio Code 中
   - Claude Desktop
   - Claude 在 VSCode 中
   - Claude API

2. **社区客户端**：
   - Cline（基于终端）
   - Cursor（代码编辑器）
   - ChatMCP
   - Windsurf

3. **MCP 管理工具**：
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## 流行的 MCP 服务器

仓库介绍了各种 MCP 服务器，包括：

1. **官方 Microsoft MCP 服务器**：
   - Microsoft Learn Docs MCP 服务器
   - Azure MCP 服务器（15+ 专用连接器）
   - GitHub MCP 服务器
   - Azure DevOps MCP 服务器
   - MarkItDown MCP 服务器
   - SQL Server MCP 服务器
   - Playwright MCP 服务器
   - Dev Box MCP 服务器
   - Azure AI Foundry MCP 服务器
   - Microsoft 365 Agents Toolkit MCP 服务器

2. **官方参考服务器**：
   - 文件系统
   - Fetch
   - 内存
   - 顺序思维

3. **图像生成**：
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **开发工具**：
   - Git MCP
   - 终端控制
   - 代码助手

5. **专用服务器**：
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## 贡献

本仓库欢迎社区贡献。请参阅社区贡献部分，了解如何有效地为 MCP 生态系统做出贡献。

----

*本学习指南更新于 2025 年 10 月 6 日，概述了截至该日期的仓库内容。仓库内容可能在此日期之后更新。*

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。
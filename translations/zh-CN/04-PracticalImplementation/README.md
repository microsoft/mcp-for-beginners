# 实践实现

[![如何使用真实工具和工作流构建、测试及部署 MCP 应用](../../../translated_images/zh-CN/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(点击上方图片观看本课程视频)_

实践实现是 Model Context Protocol (MCP) 的力量得以体现的地方。虽然理解 MCP 背后的理论和架构很重要，但真正的价值是在应用这些概念构建、测试和部署解决方案来解决现实问题时显现的。本章弥合了概念知识与动手开发之间的差距，引导你完成基于 MCP 的应用程序的实现过程。

无论你是在开发智能助手、将 AI 集成到业务工作流中，还是构建用于数据处理的自定义工具，MCP 都提供了一个灵活的基础。它的语言无关设计和针对流行编程语言的官方 SDK，使其易于被各种开发者使用。通过利用这些 SDK，你可以快速制作原型、迭代并扩展跨不同平台和环境的解决方案。

在接下来的章节中，你会找到实际案例、示例代码以及部署策略，展示如何在 C#、Java（Spring）、TypeScript、JavaScript 和 Python 中实现 MCP。你还将学习如何调试和测试 MCP 服务器、管理 API 以及使用 Azure 将解决方案部署到云端。这些动手资源旨在加速你的学习，帮助你自信地构建稳健的、准备好生产的 MCP 应用。

## 概述

本课重点介绍 MCP 在多种编程语言中的实用实现。我们将探讨如何使用 C#、Java（Spring）、TypeScript、JavaScript 和 Python 的 MCP SDK 构建稳健的应用，调试和测试 MCP 服务器，以及创建可复用的资源、提示和工具。

## 学习目标

通过本课，你将能够：

- 使用官方 SDK 在各种编程语言中实现 MCP 解决方案
- 有系统地调试和测试 MCP 服务器
- 创建并使用服务器功能（资源、提示和工具）
- 设计用于复杂任务的有效 MCP 工作流
- 优化 MCP 实现的性能和可靠性

## 官方 SDK 资源

Model Context Protocol 提供多语言官方 SDK（符合 [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **注意：** 依赖于 [Project Reactor](https://projectreactor.io)。详见 [讨论 issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本节提供如何在多个编程语言中实现 MCP 的实用示例。你可以在 `samples` 目录中找到按语言组织的示例代码。

### 可用示例

仓库包含以下语言的[示例实现](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每个示例都展示了该语言及其生态系统中的关键 MCP 概念和实现模式。

### 实用指南

更多实用 MCP 实现指南：

- [分页和大型结果集](./pagination/README.md) - 处理基于游标的分页，用于工具、资源和大型数据集

## 核心服务器功能

MCP 服务器可以实现以下任何组合的功能：

### 资源

资源为用户或 AI 模型提供上下文和数据：

- 文档存储库
- 知识库
- 结构化数据源
- 文件系统

### 提示

提示是为用户设定的模板化消息和工作流：

- 预定义对话模板
- 引导式交互模式
- 专门的对话结构

### 工具

工具是 AI 模型可执行的函数：

- 数据处理工具
- 外部 API 集成
- 计算能力
- 搜索功能

## 示例实现：C# 实现

官方 C# SDK 仓库包含多个示例实现，展示 MCP 的不同方面：

- **基本 MCP 客户端**：展示如何创建 MCP 客户端并调用工具的简单示例
- **基本 MCP 服务器**：基本工具注册的最简服务器实现
- **高级 MCP 服务器**：具备工具注册、认证和错误处理的全功能服务器
- **ASP.NET 集成**：展示如何与 ASP.NET Core 集成的示例
- **工具实现模式**：展示不同复杂度工具实现的多种模式

MCP C# SDK 目前处于预览阶段，API 可能会变更。我们将持续更新本博客以跟进 SDK 发展。

### 关键功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 构建你的 [首个 MCP 服务器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

完整的 C# 实现示例，请访问 [官方 C# SDK 示例仓库](https://github.com/modelcontextprotocol/csharp-sdk)

## 示例实现：Java with Spring 实现

Java with Spring SDK 提供了具备企业级功能的强大 MCP 实现选项。

### 关键功能

- Spring 框架集成
- 强类型安全
- 响应式编程支持
- 全面的错误处理

完整的 Java with Spring 实现示例，请参阅示例目录中的 [Java with Spring 示例](samples/java/containerapp/README.md)。

## 示例实现：JavaScript 实现

JavaScript SDK 提供轻量灵活的 MCP 实现方式。

### 关键功能

- 支持 Node.js 和浏览器
- 基于 Promise 的 API
- 与 Express 等框架轻松集成
- 支持 WebSocket 流式传输

完整的 JavaScript 实现示例，请参阅示例目录中的 [JavaScript 示例](samples/javascript/README.md)。

## 示例实现：Python 实现

Python SDK 提供 Python 风格的 MCP 实现方式，且与出色的机器学习框架集成。

### 关键功能

- 支持 async/await 与 asyncio
- FastAPI 集成``
- 简单的工具注册
- 与流行机器学习库的原生集成

完整的 Python 实现示例，请参阅示例目录中的 [Python 示例](samples/python/README.md)。

## API 管理

Azure API Management 是保护 MCP 服务器的绝佳方案。其思路是在 MCP 服务器前端放置一个 Azure API Management 实例，负责处理你可能需要的功能，如：

- 速率限制
- 令牌管理
- 监控
- 负载均衡
- 安全

### Azure 示例

以下是一个 Azure 示例，即 [创建 MCP 服务器并用 Azure API Management 保护](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

下面图片展示了授权流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

图片中发生了以下流程：

- 使用 Microsoft Entra 进行身份验证和授权。
- Azure API Management 作为网关，使用策略引导和管理流量。
- Azure Monitor 记录所有请求以便后续分析。

#### 授权流程

我们详细看看授权流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授权规范

了解更多关于 [MCP 授权规范](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## 将远程 MCP 服务器部署到 Azure

让我们尝试部署前面提到的示例：

1. 克隆代码库

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 注册 `Microsoft.App` 资源提供程序。

   - 如果你使用 Azure CLI，运行 `az provider register --namespace Microsoft.App --wait`。
   - 如果你使用 Azure PowerShell，运行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。稍等后运行 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 来检查注册是否完成。

1. 运行此 [azd](https://aka.ms/azd) 命令，配置 API 管理服务、函数应用（含代码）和所有其他必需的 Azure 资源

    ```shell
    azd up
    ```

    该命令应在 Azure 上部署所有云资源

### 使用 MCP Inspector 测试服务器

1. 在**新终端窗口**，安装并运行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    你应该看到类似的界面：

    ![Connect to Node inspector](../../../translated_images/zh-CN/connect.141db0b2bd05f096.webp)

1. 按住 CTRL 并点击，加载 MCP Inspector Web 应用（例如 [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）
1. 设置传输类型为 `SSE`
1. 将 URL 设置为在执行 `azd up` 后显示的你的运行中 API 管理 SSE 端点地址，点击 **连接**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **列出工具**。点击某个工具并**运行工具**。

如果所有步骤顺利完成，你现在应该已连接至 MCP 服务器，并成功调用了一个工具。

## 适用于 Azure 的 MCP 服务器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：该系列仓库为使用 Azure Functions（Python、C# .NET 或 Node/TypeScript）构建和部署自定义远程 MCP (Model Context Protocol) 服务器的快速起步模板。

该示例提供完整解决方案，允许开发者：

- 本地构建并运行：在本地机器上开发和调试 MCP 服务器
- 部署到 Azure：通过简单的 azd up 命令轻松部署到云端
- 从客户端连接：支持包括 VS Code Copilot 代理模式和 MCP Inspector 工具在内的多种客户端连接 MCP 服务器

### 关键功能

- 从设计上保障安全：MCP 服务器使用密钥和 HTTPS 进行保护
- 身份认证选项：支持内置身份认证和/或 API 管理的 OAuth
- 网络隔离：支持使用 Azure 虚拟网络（VNET）实现网络隔离
- 无服务器架构：利用 Azure Functions 实现可扩展的事件驱动执行
- 本地开发支持：覆盖全面的本地开发和调试支持
- 简单的部署流程：优化的部署流程到 Azure

仓库包含所有必要的配置文件、源代码和基础设施定义，能够快速开始构建生产就绪的 MCP 服务器实现。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 和 Python 实现的 MCP 示例

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 和 C# .NET 实现的 MCP 示例

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 和 Node/TypeScript 实现的 MCP 示例。

## 关键要点

- MCP SDK 提供了针对不同语言的工具，用于实现稳健的 MCP 解决方案
- 调试和测试过程对可靠的 MCP 应用至关重要
- 可复用的提示模板支持一致的 AI 交互
- 设计良好的工作流可以利用多个工具编排复杂任务
- 实现 MCP 解决方案需考虑安全性、性能和错误处理

## 练习

设计一个实用的 MCP 工作流，解决你领域中的现实问题：

1. 确定 3-4 个对该问题解决有用的工具
2. 创建一个工作流图，展示这些工具如何交互
3. 使用你偏好的语言实现其中一个工具的基础版本
4. 创建一个提示模板，帮助模型有效使用你的工具

## 额外资源

---

## 接下来

下一章：[高级主题](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文档的原语言版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
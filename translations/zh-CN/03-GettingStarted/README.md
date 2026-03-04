## 入门指南  

[![构建您的第一个MCP服务器](../../../translated_images/zh-CN/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(点击上方图片观看本课视频)_

本部分包含多个课程：

- **1 第一个服务器**，在第一个课中，您将学习如何创建第一个服务器并用检查工具检查它，这是测试和调试服务器的宝贵方法，[前往课程](01-first-server/README.md)

- **2 客户端**，本课您将学习如何编写能够连接到服务器的客户端，[前往课程](02-client/README.md)

- **3 带LLM的客户端**，更好的客户端写法是给它添加LLM，这样它能与服务器“协商”要做什么，[前往课程](03-llm-client/README.md)

- **4 在Visual Studio Code中使用GitHub Copilot代理模式的服务器**。这里我们讲如何在Visual Studio Code中运行MCP服务器，[前往课程](04-vscode/README.md)

- **5 stdio传输服务器**，stdio传输是本地MCP服务器到客户端通信的推荐标准，提供安全的基于子进程的通信和内置进程隔离，[前往课程](05-stdio-server/README.md)

- **6 MCP的HTTP流传输（可流式HTTP）**。了解现代HTTP流传输（基于[MCP规范 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http)推荐的远程MCP服务器方式）、进度通知，以及如何使用可流式HTTP实现可扩展的实时MCP服务器和客户端，[前往课程](06-http-streaming/README.md)

- **7 使用VSCode的AI工具包**来使用和测试您的MCP客户端及服务器，[前往课程](07-aitk/README.md)

- **8 测试**。着重讲述如何以不同方式测试服务器和客户端，[前往课程](08-testing/README.md)

- **9 部署**。介绍部署MCP解决方案的多种方式，[前往课程](09-deployment/README.md)

- **10 高级服务器用法**。涵盖高级服务器使用方法，[前往课程](./10-advanced/README.md)

- **11 认证**。介绍如何添加简单认证，从Basic Auth到JWT和RBAC。建议从这章开始，然后查看第5章高级主题，并根据第2章建议进行额外的安全加固，[前往课程](./11-simple-auth/README.md)

- **12 MCP主机**。配置和使用流行的MCP主机客户端，包括Claude Desktop、Cursor、Cline和Windsurf，学习传输类型及排错技巧，[前往课程](./12-mcp-hosts/README.md)

- **13 MCP检查器**。使用MCP检查器交互式调试和测试MCP服务器。学习排错工具、资源及协议消息，[前往课程](./13-mcp-inspector/README.md)

- **14 采样**。创建与MCP客户端协作完成LLM相关任务的MCP服务器，[前往课程](./14-sampling/README.md)

- **15 MCP应用**。构建还能回复UI指令的MCP服务器，[前往课程](./15-mcp-apps/README.md)

模型上下文协议（Model Context Protocol，MCP）是一个开放协议，标准化了应用向LLM提供上下文的方式。可以把MCP想象成AI应用的USB-C接口——它为连接AI模型与各种数据源和工具提供了标准接口。

## 学习目标

完成本课程后，您将能够：

- 设置C#、Java、Python、TypeScript和JavaScript的MCP开发环境
- 构建并部署具备自定义功能（资源、提示和工具）的基础MCP服务器
- 创建连接MCP服务器的主机应用
- 测试和调试MCP实现
- 理解常见的设置挑战及解决方案
- 将MCP实现连接到主流LLM服务

## 设置您的MCP环境

在开始使用MCP之前，准备好开发环境和了解基本工作流程非常重要。本节将指导您完成初始设置步骤，确保您能顺利入门MCP。

### 前置条件

在开始MCP开发之前，请确保您具备：

- **开发环境**：所选语言环境（C#、Java、Python、TypeScript或JavaScript）
- **IDE/编辑器**：Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm或其他现代代码编辑器
- **包管理器**：NuGet、Maven/Gradle、pip或npm/yarn
- **API密钥**：您打算在主机应用中使用的任何AI服务的API密钥


### 官方SDKs

接下来的章节中，您将看到使用Python、TypeScript、Java和.NET构建的解决方案。以下是所有官方支持的SDK。

MCP为多种语言提供了官方SDK（与[2025-11-25 MCP规范](https://spec.modelcontextprotocol.io/specification/2025-11-25/)对齐）：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - 与微软合作维护
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - 与Spring AI合作维护
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方TypeScript实现
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方Python实现（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 官方Kotlin实现
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - 与Loopwork AI合作维护
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 官方Rust实现
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 官方Go实现

## 关键要点

- 利用语言特定SDK搭建MCP开发环境简单便捷
- 构建MCP服务器涉及创建和注册具备明确模式的工具
- MCP客户端连接服务器和模型，实现功能拓展
- 测试和调试对可靠的MCP实现至关重要
- 部署方案涵盖本地开发和云端解决方案

## 练习

我们提供了一组示例，补充本部分各章的练习内容。此外，各章还包含自有的练习和作业

- [Java计算器](./samples/java/calculator/README.md)
- [.Net计算器](../../../03-GettingStarted/samples/csharp)
- [JavaScript计算器](./samples/javascript/README.md)
- [TypeScript计算器](./samples/typescript/README.md)
- [Python计算器](../../../03-GettingStarted/samples/python)

## 额外资源

- [使用模型上下文协议构建Azure上的代理](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [使用Azure容器应用的远程MCP（Node.js/TypeScript/JavaScript）](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP代理](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 下一步

从第一课开始学习：[创建您的第一个MCP服务器](01-first-server/README.md)

完成本模块后，继续学习：[模块4：实践实现](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。请以原始语言的文档作为权威版本。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而产生的任何误解或错误解释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
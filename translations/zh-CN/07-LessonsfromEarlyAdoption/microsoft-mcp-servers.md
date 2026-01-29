# 🚀 10 个正在改变开发者生产力的 Microsoft MCP 服务器

## 🎯 本指南你将学到什么

本实用指南展示了十个正在积极改变开发者与 AI 助手协作方式的 Microsoft MCP 服务器。我们不仅会介绍 MCP 服务器能做什么，更会展示这些服务器如何在微软及其他地方的日常开发工作流中发挥实际作用。

本指南中的每个服务器均基于真实使用情况和开发者反馈精选。你将了解每个服务器的功能、重要性以及如何在自己的项目中最大化利用它们。无论你是 MCP 新手，还是想扩展现有配置，这些服务器都代表了微软生态系统中一些最实用且影响深远的工具。

> **💡 快速入门小贴士**  
>  
> MCP 新手？别担心！本指南专为初学者设计。我们会边讲解边介绍概念，你也可以随时回顾我们的[Introduction to MCP](../00-Introduction/README.md)和[Core Concepts](../01-CoreConcepts/README.md)模块，深入了解背景知识。

## 概览

本综合指南探讨了十个微软 MCP 服务器，这些服务器正在革新开发者与 AI 助手及外部工具的交互方式。从 Azure 资源管理到文档处理，这些服务器展示了 Model Context Protocol 在打造无缝、高效开发工作流中的强大能力。

## 学习目标

完成本指南后，你将能够：  
- 理解 MCP 服务器如何提升开发者生产力  
- 了解微软最具影响力的 MCP 服务器实现  
- 探索每个服务器的实际应用场景  
- 掌握如何在 VS Code 和 Visual Studio 中设置和配置这些服务器  
- 了解更广泛的 MCP 生态系统及未来发展方向  

## 🔧 了解 MCP 服务器：初学者指南

### 什么是 MCP 服务器？

作为 Model Context Protocol（MCP）的初学者，你可能会问：“MCP 服务器到底是什么？为什么我需要关心它？”我们先用一个简单的比喻来说明。

把 MCP 服务器想象成专门的助手，帮助你的 AI 编码伙伴（比如 GitHub Copilot）连接到外部工具和服务。就像你手机上会用不同的应用处理不同任务——一个查天气，一个导航，一个银行业务——MCP 服务器赋予你的 AI 助手与各种开发工具和服务交互的能力。

### MCP 服务器解决了什么问题

在有 MCP 服务器之前，如果你想要：  
- 查看 Azure 资源  
- 创建 GitHub issue  
- 查询数据库  
- 搜索文档  

你必须暂停编码，打开浏览器，访问相应网站，手动完成这些操作。频繁切换上下文会打断你的思路，降低效率。

### MCP 服务器如何改变你的开发体验

有了 MCP 服务器，你可以留在开发环境（VS Code、Visual Studio 等）中，直接让 AI 助手帮你完成这些任务。例如：

**传统流程：**  
1. 停止编码  
2. 打开浏览器  
3. 进入 Azure 门户  
4. 查询存储账户详情  
5. 返回 VS Code  
6. 继续编码  

**现在可以这样做：**  
1. 问 AI：“我的 Azure 存储账户状态如何？”  
2. 根据提供的信息继续编码  

### 初学者的主要好处

#### 1. 🔄 **保持专注状态**  
- 不用在多个应用间切换  
- 专注于正在编写的代码  
- 减少管理不同工具的心理负担  

#### 2. 🤖 **用自然语言替代复杂命令**  
- 不用记忆 SQL 语法，只需描述需要的数据  
- 不用记住 Azure CLI 命令，只需说明目标  
- 让 AI 处理技术细节，你专注逻辑  

#### 3. 🔗 **连接多种工具**  
- 通过组合不同服务创建强大工作流  
- 例如：“获取所有最新 GitHub issue 并创建对应的 Azure DevOps 工作项”  
- 无需编写复杂脚本即可实现自动化  

#### 4. 🌐 **接入不断扩展的生态系统**  
- 利用微软、GitHub 及其他公司的服务器  
- 无缝混合不同厂商的工具  
- 加入跨多种 AI 助手通用的标准化生态  

#### 5. 🛠️ **边做边学**  
- 从预构建服务器开始理解概念  
- 随着熟悉度提升逐步构建自己的服务器  
- 利用现有 SDK 和文档指导学习  

### 初学者的真实案例

假设你是 web 开发新手，正在做第一个项目。MCP 服务器能帮你这样：

**传统做法：**  
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**使用 MCP 服务器：**  
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### 企业标准优势

MCP 正成为行业标准，这意味着：  
- **一致性**：不同工具和公司间体验相似  
- **互操作性**：不同厂商的服务器能协同工作  
- **未来保障**：技能和配置可在不同 AI 助手间迁移  
- **社区支持**：庞大的共享知识和资源生态  

### 入门指南：你将学到什么

本指南将介绍 10 个微软 MCP 服务器，适合各级开发者使用。每个服务器旨在：  
- 解决常见开发难题  
- 减少重复性工作  
- 提升代码质量  
- 增强学习机会  

> **💡 学习小贴士**  
>  
> 如果你完全不了解 MCP，建议先学习我们的[Introduction to MCP](../00-Introduction/README.md)和[Core Concepts](../01-CoreConcepts/README.md)模块。然后再回来看看这些微软工具的实际应用。  
>  
> 想了解 MCP 重要性的更多背景，可以阅读 Maria Naggaga 的文章：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## 在 VS Code 和 Visual Studio 中开始使用 MCP 🚀

如果你使用 Visual Studio Code 或 Visual Studio 2022 搭配 GitHub Copilot，设置这些 MCP 服务器非常简单。

### VS Code 设置

VS Code 的基本流程如下：

1. **启用 Agent 模式**：在 Copilot Chat 窗口切换到 Agent 模式  
2. **配置 MCP 服务器**：将服务器配置添加到 VS Code 的 settings.json 文件中  
3. **启动服务器**：点击你想使用的服务器的“启动”按钮  
4. **选择工具**：选择当前会话要启用的 MCP 服务器  

详细设置说明请参见[VS Code MCP 文档](https://code.visualstudio.com/docs/copilot/copilot-mcp)。

> **💡 专业提示：像专家一样管理 MCP 服务器！**  
>  
> VS Code 扩展视图新增了[管理已安装 MCP 服务器的便捷 UI](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)，你可以快速启动、停止和管理任何已安装的 MCP 服务器，界面清晰简单，快去试试吧！

### Visual Studio 2022 设置

针对 Visual Studio 2022（版本 17.14 及以上）：

1. **启用 Agent 模式**：在 GitHub Copilot Chat 窗口点击“Ask”下拉菜单，选择“Agent”  
2. **创建配置文件**：在解决方案目录下创建 `.mcp.json` 文件（推荐位置：`<SOLUTIONDIR>\.mcp.json`）  
3. **配置服务器**：使用标准 MCP 格式添加服务器配置  
4. **工具审批**：根据提示批准所需工具及相应权限范围  

详细 Visual Studio 设置说明请参见[Visual Studio MCP 文档](https://learn.microsoft.com/visualstudio/ide/mcp-servers)。

每个 MCP 服务器都有自己的配置需求（连接字符串、认证等），但两款 IDE 的设置模式是一致的。

## 从 Microsoft MCP 服务器学到的经验 🛠️

### 1. 📚 Microsoft Learn Docs MCP 服务器

[![在 VS Code 中安装](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![在 VS Code Insiders 中安装](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**功能介绍**：Microsoft Learn Docs MCP 服务器是一个云托管服务，通过 Model Context Protocol 为 AI 助手提供实时访问微软官方文档的能力。它连接到 `https://learn.microsoft.com/api/mcp`，支持对 Microsoft Learn、Azure 文档、Microsoft 365 文档及其他官方微软资源的语义搜索。

**为何有用**：虽然看似“只是文档”，但这个服务器对每个使用微软技术的开发者都至关重要。许多 .NET 开发者对 AI 编码助手的最大抱怨之一是它们无法及时掌握最新的 .NET 和 C# 版本。Microsoft Learn Docs MCP 服务器通过提供最新的文档、API 参考和最佳实践，解决了这一问题。无论你是在使用最新的 Azure SDK，探索 C# 13 新特性，还是实现前沿的 .NET Aspire 模式，这个服务器都确保你的 AI 助手能访问权威且最新的信息，从而生成准确、现代的代码。

**实际应用**：例如，“根据官方 Microsoft Learn 文档，创建 Azure 容器应用的 az cli 命令是什么？”或者“如何在 ASP.NET Core 中使用依赖注入配置 Entity Framework？”又或者“帮我审查这段代码，确保它符合 Microsoft Learn 文档中的性能建议。”该服务器利用先进的语义搜索，覆盖 Microsoft Learn、Azure 文档和 Microsoft 365 文档，返回最多 10 条高质量内容片段，附带文章标题和链接，始终访问最新发布的微软文档。

**特色示例**：该服务器提供了 `microsoft_docs_search` 工具，可针对微软官方技术文档执行语义搜索。配置完成后，你可以提问“如何在 ASP.NET Core 中实现 JWT 认证？”并获得详细的官方回答及来源链接。搜索质量极高，能理解上下文——比如在 Azure 语境下询问“containers”会返回 Azure 容器实例文档，而在 .NET 语境下则返回相关的 C# 集合信息。

这对快速变化或近期更新的库和用例尤其有用。举例来说，最近我在一些编码项目中想利用 .NET Aspire 和 Microsoft.Extensions.AI 的最新特性。通过引入 Microsoft Learn Docs MCP 服务器，我不仅能访问 API 文档，还能获得刚发布的操作指南和示例。
> **💡 专业提示**
> 
> 即使是对工具友好的模型，也需要激励去使用 MCP 工具！可以考虑添加系统提示或[copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot），例如：“你可以访问 `microsoft.docs.mcp` —— 在处理关于 Microsoft 技术（如 C#、Azure、ASP.NET Core 或 Entity Framework）的问题时，使用此工具搜索微软最新的官方文档。”
>
> 想看这个功能的精彩示例，可以查看 Awesome GitHub Copilot 仓库中的[C# .NET Janitor 聊天模式](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)。该模式专门利用 Microsoft Learn Docs MCP 服务器，帮助使用最新的模式和最佳实践来清理和现代化 C# 代码。
### 2. ☁️ Azure MCP 服务器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**功能介绍**：Azure MCP 服务器是一套包含15个以上专用 Azure 服务连接器的综合工具，将整个 Azure 生态系统无缝融入您的 AI 工作流。这不仅仅是一个单一服务器——它是一个强大的集合，涵盖资源管理、数据库连接（PostgreSQL、SQL Server）、基于 KQL 的 Azure Monitor 日志分析、Cosmos DB 集成等多种功能。

**为什么有用**：除了管理 Azure 资源外，该服务器还能显著提升使用 Azure SDK 编写代码的质量。当您以 Agent 模式使用 Azure MCP 时，它不仅帮助您写代码，更帮助您写出符合当前认证模式、错误处理最佳实践并利用最新 SDK 功能的*更优质* Azure 代码。您得到的不是可能可用的通用代码，而是符合 Azure 推荐生产环境模式的代码。

**主要模块包括**：
- **🗄️ 数据库连接器**：通过自然语言直接访问 Azure Database for PostgreSQL 和 SQL Server
- **📊 Azure Monitor**：基于 KQL 的日志分析和运营洞察
- **🌐 资源管理**：完整的 Azure 资源生命周期管理
- **🔐 认证**：DefaultAzureCredential 和托管身份模式
- **📦 存储服务**：Blob 存储、队列存储和表存储操作
- **🚀 容器服务**：Azure 容器应用、容器实例和 AKS 管理
- **以及更多专用连接器**

**实际应用示例**：“列出我的 Azure 存储账户”、“查询我 Log Analytics 工作区过去一小时的错误日志”，或“帮我用 Node.js 构建一个带有正确认证的 Azure 应用”。

**完整演示场景**：这里有一个完整的演示，展示如何将 Azure MCP 与 VS Code 中的 GitHub Copilot for Azure 扩展结合使用。当两者都安装后，输入：

> “创建一个 Python 脚本，使用 DefaultAzureCredential 认证上传文件到 Azure Blob Storage。脚本应连接到名为 'mycompanystorage' 的 Azure 存储账户，上传到名为 'documents' 的容器，创建一个带有当前时间戳的测试文件进行上传，优雅处理错误并提供详细输出，遵循 Azure 认证和错误处理最佳实践，包含注释解释 DefaultAzureCredential 的工作原理，且脚本结构合理，带有函数和文档说明。”

Azure MCP 服务器将生成一个完整的、可用于生产的 Python 脚本，具备以下特点：
- 使用最新的 Azure Blob Storage SDK，采用合适的异步模式
- 实现 DefaultAzureCredential，包含详尽的回退链说明
- 包含健壮的错误处理，针对特定 Azure 异常类型
- 遵循 Azure SDK 的资源管理和连接处理最佳实践
- 提供详细日志和信息丰富的控制台输出
- 脚本结构合理，包含函数、文档和类型提示

令人印象深刻的是，没有 Azure MCP，您可能只能得到通用的 Blob 存储代码，虽然能用但不符合当前 Azure 模式。而有了 Azure MCP，您获得的代码能利用最新认证方法，处理 Azure 特有的错误场景，并遵循微软推荐的生产应用实践。

**特色示例**：我经常忘记 `az` 和 `azd` CLI 的具体命令，通常是先查语法再执行命令。很多时候我直接登录门户点击操作，因为不想承认自己记不住命令。能够直接用自然语言描述需求非常棒，更棒的是还能在 IDE 里完成！

[Azure MCP 仓库](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) 中有丰富的用例列表供您入门。想了解详细的安装指南和高级配置选项，请访问[官方 Azure MCP 文档](https://learn.microsoft.com/azure/developer/azure-mcp-server/)。

### 3. 🐙 GitHub MCP 服务器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**功能介绍**：官方 GitHub MCP 服务器实现了与 GitHub 全生态的无缝集成，支持托管远程访问和本地 Docker 部署。它不仅限于基本的仓库操作，还包括 GitHub Actions 管理、拉取请求工作流、问题跟踪、安全扫描、通知和高级自动化功能。

**为什么有用**：该服务器彻底改变了您与 GitHub 的交互方式，将完整的平台体验直接带入开发环境。无需频繁在 VS Code 和 GitHub.com 之间切换进行项目管理、代码审查和 CI/CD 监控，您可以通过自然语言命令一站式完成所有操作，专注于代码本身。

> **ℹ️ 注意：不同类型的“Agent”**
> 
> 不要将此 GitHub MCP 服务器与 GitHub 的 Coding Agent（可分配问题进行自动编码的 AI 代理）混淆。GitHub MCP 服务器在 VS Code 的 Agent 模式下提供 GitHub API 集成，而 Coding Agent 是一个独立功能，会在被分配到 GitHub 问题时创建拉取请求。

**主要功能包括**：
- **⚙️ GitHub Actions**：完整的 CI/CD 管道管理、工作流监控和工件处理
- **🔀 拉取请求**：创建、审查、合并和管理 PR，支持全面状态跟踪
- **🐛 问题管理**：完整的问题生命周期管理、评论、标签和分配
- **🔒 安全**：代码扫描警报、秘密检测和 Dependabot 集成
- **🔔 通知**：智能通知管理和仓库订阅控制
- **📁 仓库管理**：文件操作、分支管理和仓库管理
- **👥 协作**：用户和组织搜索、团队管理和访问控制

**实际应用示例**：“从我的功能分支创建拉取请求”、“显示本周所有失败的 CI 运行”、“列出我仓库中的未解决安全警报”，或“查找分配给我的所有问题”。

**完整演示场景**：以下是展示 GitHub MCP 服务器功能的强大工作流：

> “我需要为冲刺评审做准备。帮我列出本周我创建的所有拉取请求，检查 CI/CD 管道状态，汇总需要处理的安全警报，并根据带有‘feature’标签的已合并 PR 帮我起草发布说明。”

GitHub MCP 服务器将会：
- 查询您最近的拉取请求及其详细状态
- 分析工作流运行，突出显示失败或性能问题
- 汇总安全扫描结果，优先处理关键警报
- 从已合并的 PR 中提取信息，生成全面的发布说明
- 提供冲刺规划和发布准备的可执行建议

**特色示例**：我非常喜欢用它来处理代码审查工作流。无需在 VS Code、GitHub 通知和拉取请求页面间切换，我只需说“显示所有等待我审查的 PR”，然后“给 PR #123 添加评论，询问认证方法中的错误处理”。服务器负责调用 GitHub API，维护讨论上下文，甚至帮我写出更有建设性的审查评论。

**认证选项**：服务器支持 OAuth（在 VS Code 中无缝体验）和个人访问令牌，且可配置只启用所需的 GitHub 功能模块。您可以选择远程托管服务快速部署，或通过 Docker 本地运行以获得完全控制。

> **💡 专业提示**
> 
> 通过在 MCP 服务器设置中配置 `--toolsets` 参数，仅启用所需的工具集，以减少上下文大小并提升 AI 工具选择效率。例如，针对核心开发工作流，添加 `"--toolsets", "repos,issues,pull_requests,actions"`；如果主要关注 GitHub 监控功能，则使用 `"--toolsets", "notifications, security"`。

### 4. 🔄 Azure DevOps MCP 服务器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**功能介绍**：连接 Azure DevOps 服务，实现全面的项目管理、工作项跟踪、构建管道管理和仓库操作。

**为什么有用**：对于以 Azure DevOps 作为主要 DevOps 平台的团队，这个 MCP 服务器消除了在开发环境和 Azure DevOps 网页界面之间频繁切换的麻烦。您可以直接通过 AI 助手管理工作项、查看构建状态、查询仓库和处理项目管理任务。

**实际应用示例**：“显示当前冲刺中 WebApp 项目的所有活跃工作项”、“为我刚发现的登录问题创建一个缺陷报告”，或“检查构建管道状态并显示最近的失败”。

**特色示例**：您可以轻松通过简单查询查看团队当前冲刺的状态，比如“显示当前冲刺中 WebApp 项目的所有活跃工作项”或“为我刚发现的登录问题创建一个缺陷报告”，无需离开开发环境。

### 5. 📝 MarkItDown MCP 服务器
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**功能介绍**：MarkItDown 是一个全面的文档转换服务器，能够将多种文件格式转换成高质量的 Markdown，专为大语言模型（LLM）处理和文本分析工作流优化。

**为什么有用**：现代文档工作流的必备工具！MarkItDown 支持多种文件格式，同时保留关键的文档结构，如标题、列表、表格和链接。与简单的文本提取工具不同，它注重保持语义意义和格式，这对 AI 处理和人工阅读都非常重要。

**支持的文件格式**：
- **办公文档**：PDF、PowerPoint（PPTX）、Word（DOCX）、Excel（XLSX/XLS）
- **多媒体文件**：图片（含 EXIF 元数据和 OCR）、音频（含 EXIF 元数据和语音转录）
- **网页内容**：HTML、RSS 订阅源、YouTube 链接、维基百科页面
- **数据格式**：CSV、JSON、XML、ZIP 文件（递归处理内容）
- **出版格式**：EPub、Jupyter 笔记本（.ipynb）
- **邮件**：Outlook 邮件（.msg）
- **高级功能**：集成 Azure Document Intelligence 以增强 PDF 处理能力

**高级功能**：MarkItDown 支持基于 LLM 的图像描述（需提供 OpenAI 客户端）、Azure Document Intelligence 增强 PDF 处理、音频转录语音内容，以及插件系统以扩展更多文件格式。

**实际应用**：“将这份 PowerPoint 演示文稿转换为文档站点用的 Markdown”、“从这份 PDF 中提取带有正确标题结构的文本”，或“将这份 Excel 表格转换成易读的表格格式”。

**示例亮点**：引用 [MarkItDown 文档](https://github.com/microsoft/markitdown#why-markdown) 中的话：

> Markdown 非常接近纯文本，标记和格式极少，但仍能表达重要的文档结构。主流大语言模型，如 OpenAI 的 GPT-4o，原生“理解”Markdown，且经常在回答中自发使用 Markdown。这表明它们经过了大量 Markdown 格式文本的训练，理解能力很强。额外好处是，Markdown 规范也非常节省 token。

MarkItDown 非常擅长保留文档结构，这对 AI 工作流至关重要。例如，在转换 PowerPoint 演示文稿时，它保持幻灯片的组织结构和正确的标题，提取表格为 Markdown 表格，包含图片的替代文本，甚至处理演讲者备注。图表被转换为可读的数据表，生成的 Markdown 保持了原始演示的逻辑流程。这使得它非常适合将演示内容输入 AI 系统或从现有幻灯片创建文档。

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**功能介绍**：提供对 SQL Server 数据库（本地、Azure SQL 或 Fabric）的对话式访问

**为什么有用**：类似于 PostgreSQL 服务器，但针对微软 SQL 生态系统。只需简单的连接字符串，即可用自然语言查询数据库——无需频繁切换上下文！

**实际应用**：“查找过去 30 天内未完成的所有订单”会被转换成相应的 SQL 查询并返回格式化结果。

**示例亮点**：设置好数据库连接后，你可以立即开始与数据对话。博客文章中展示了一个简单的问题：“你连接的是哪个数据库？”MCP 服务器通过调用相应的数据库工具，连接到你的 SQL Server 实例，并返回当前数据库连接的详细信息——整个过程无需编写一行 SQL。该服务器支持从模式管理到数据操作的全面数据库操作，全部通过自然语言提示完成。完整的设置说明和 VS Code 及 Claude Desktop 的配置示例，请参见：[Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)。

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**功能介绍**：让 AI 代理能够与网页交互，用于测试和自动化

> **ℹ️ 支持 GitHub Copilot**
> 
> Playwright MCP Server 为 GitHub Copilot 的编码代理提供网页浏览能力！[了解此功能详情](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

**为什么有用**：非常适合基于自然语言描述的自动化测试。AI 可以浏览网站、填写表单，并通过结构化的无障碍快照提取数据——这非常强大！

**实际应用**：“测试登录流程并验证仪表盘是否正确加载”或“生成一个测试，搜索产品并验证结果页面”——全部无需应用源码。

**示例亮点**：我的同事 Debbie O'Brien 最近在 Playwright MCP Server 上做了很多出色的工作！例如，她展示了如何在没有应用源码的情况下生成完整的 Playwright 测试。在她的场景中，她让 Copilot 为一个电影搜索应用创建测试：访问网站，搜索“Garfield”，并验证电影是否出现在结果中。MCP 启动了浏览器会话，利用 DOM 快照探索页面结构，找出正确的选择器，并生成了一个首次运行即通过的完整 TypeScript 测试。

这项技术的强大之处在于它弥合了自然语言指令与可执行测试代码之间的鸿沟。传统方法需要手动编写测试或访问代码库以获取上下文，而 Playwright MCP 允许你测试外部网站、客户端应用，或在无法访问代码的黑盒测试场景中工作。

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**功能介绍**：通过自然语言管理 Microsoft Dev Box 环境

**为什么有用**：极大简化开发环境管理！无需记忆具体命令，即可创建、配置和管理开发环境。

**实际应用**：“搭建一个带有最新 .NET SDK 的新 Dev Box，并为我们的项目配置好”，“查看我所有开发环境的状态”，或“为团队演示创建一个标准化的演示环境”。

**示例亮点**：我非常喜欢用 Dev Box 进行个人开发。让我印象深刻的是 James Montemagno 讲述的 Dev Box 在会议演示中的优势，因为无论会议、酒店还是飞机上的 Wi-Fi 如何，它都能提供超快的以太网连接。事实上，我最近在从布鲁日到安特卫普的公交车上，用手机热点连接笔记本电脑练习会议演示！接下来我计划深入研究团队多开发环境管理和标准化演示环境。客户和同事们也常提到的另一个重要用例是使用 Dev Box 预配置开发环境。在这两种情况下，使用 MCP 来配置和管理 Dev Box，都能通过自然语言交互完成，同时保持在开发环境中。

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**功能介绍**：Azure AI Foundry MCP Server 为开发者提供了全面访问 Azure AI 生态系统的能力，包括模型目录、部署管理、基于 Azure AI Search 的知识索引以及评估工具。这个实验性服务器架起了 AI 开发与 Azure 强大 AI 基础设施之间的桥梁，使构建、部署和评估 AI 应用变得更加便捷。

**为什么有用**：该服务器改变了你使用 Azure AI 服务的方式，将企业级 AI 功能直接融入开发流程。你无需在 Azure 门户、文档和 IDE 之间切换，就能通过自然语言命令发现模型、部署服务、管理知识库并评估 AI 性能。对于构建 RAG（检索增强生成）应用、管理多模型部署或实现全面 AI 评估流程的开发者来说尤为强大。

**主要开发者功能**：
- **🔍 模型发现与部署**：浏览 Azure AI Foundry 的模型目录，获取详细模型信息和代码示例，并将模型部署到 Azure AI 服务
- **📚 知识管理**：创建和管理 Azure AI Search 索引，添加文档，配置索引器，构建复杂的 RAG 系统
- **⚡ AI 代理集成**：连接 Azure AI Agents，查询现有代理，并在生产场景中评估代理性能
- **📊 评估框架**：运行全面的文本和代理评估，生成 Markdown 报告，为 AI 应用实施质量保障
- **🚀 原型工具**：获取基于 GitHub 的原型搭建指南，访问 Azure AI Foundry Labs 的前沿研究模型

**真实开发者使用场景**：“将 Phi-4 模型部署到 Azure AI 服务以支持我的应用”、“为我的文档 RAG 系统创建新的搜索索引”、“根据质量指标评估我的代理响应”，或“为复杂分析任务寻找最佳推理模型”。

**完整演示场景**：以下是一个强大的 AI 开发工作流程：

> “我正在构建一个客户支持代理。帮我从目录中找到一个合适的推理模型，部署到 Azure AI 服务，基于我们的文档创建知识库，搭建评估框架测试响应质量，然后帮我用 GitHub 令牌原型集成进行测试。”

Azure AI Foundry MCP Server 将会：
- 根据你的需求查询模型目录，推荐最优推理模型
- 提供部署命令和你首选 Azure 区域的配额信息
- 为你的文档设置带有合适架构的 Azure AI Search 索引
- 配置带有质量指标和安全检查的评估流程
- 生成带有 GitHub 认证的原型代码，供即时测试
- 提供针对你具体技术栈的全面设置指南

**特色示例**：作为开发者，我一直难以跟上各种 LLM 模型的发展。我知道几个主流模型，但总感觉错过了提升效率和生产力的机会。令牌和配额管理也让我头疼——我总是不确定自己是否为合适的任务选择了正确的模型，或者是否在无效地消耗预算。我最近在和团队讨论 MCP Server 推荐时，从 James Montemagno 那里听说了这个 MCP Server，迫不及待想试用！模型发现功能对我这种想跳出常规、寻找针对特定任务优化模型的人来说特别有吸引力。评估框架能帮我验证是否真的获得了更好的结果，而不仅仅是尝试新东西。

> **ℹ️ 实验状态**
> 
> 该 MCP 服务器处于实验阶段，正在积极开发中。功能和 API 可能会发生变化。非常适合探索 Azure AI 能力和构建原型，但在生产环境中使用时请验证稳定性需求。

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**功能介绍**：为开发者提供构建与 Microsoft 365 及 Microsoft 365 Copilot 集成的 AI 代理和应用所需的关键工具，包括架构验证、示例代码获取和故障排除支持。

**为什么有用**：为 Microsoft 365 和 Copilot 开发涉及复杂的声明式架构和特定开发模式。该 MCP 服务器将关键开发资源直接带入你的编码环境，帮助你验证架构、查找示例代码并解决常见问题，无需频繁查阅文档。

**真实使用场景**：“验证我的声明式代理清单并修复架构错误”、“展示实现 Microsoft Graph API 插件的示例代码”，或“帮我排查 Teams 应用的身份验证问题”。

**特色示例**：我在 Build 大会与朋友 John Miller 聊到 M365 Agents，他推荐了这个 MCP。对于刚接触 M365 Agents 的开发者来说，这非常有帮助，因为它提供了模板、示例代码和脚手架，避免被大量文档淹没。架构验证功能尤其有用，可以避免因清单结构错误而导致的长时间调试。

> **💡 专业提示**
> 
> 建议将此服务器与 Microsoft Learn Docs MCP Server 一起使用，获得全面的 M365 开发支持——一个提供官方文档，另一个提供实用的开发工具和故障排除帮助。

## 接下来是什么？🔮

## 📋 结论

Model Context Protocol (MCP) 正在改变开发者与 AI 助手及外部工具的交互方式。这 10 个微软 MCP 服务器展示了标准化 AI 集成的强大能力，实现了无缝的工作流程，让开发者在保持专注的同时，轻松访问强大的外部功能。

从全面的 Azure 生态系统集成，到专门的 Playwright 浏览器自动化和 MarkItDown 文档处理工具，这些服务器展示了 MCP 如何提升多样化开发场景下的生产力。标准化协议确保这些工具协同工作，打造统一的开发体验。

随着 MCP 生态系统不断发展，积极参与社区、探索新服务器并构建定制解决方案，将是最大化开发效率的关键。MCP 的开放标准特性意味着你可以混合使用不同厂商的工具，打造最适合你需求的工作流程。

## 🔗 额外资源

- [官方 Microsoft MCP 仓库](https://github.com/microsoft/mcp)
- [MCP 社区与文档](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 文档](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 文档](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 文档](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 事件](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days 直播 7 月 29/30 日或点播观看](https://aka.ms/mcpdevdays)

## 🎯 练习

1. **安装与配置**：在你的 VS Code 环境中安装一个 MCP 服务器并测试基本功能。
2. **工作流集成**：设计一个结合至少三个不同 MCP 服务器的开发工作流。
3. **自定义服务器规划**：识别日常开发中可受益于自定义 MCP 服务器的任务，并为其创建规格说明。
4. **性能分析**：比较使用 MCP 服务器与传统方法完成常见开发任务的效率。
5. **安全评估**：评估在开发环境中使用 MCP 服务器的安全影响，并提出最佳实践。

Next:[Best Practices](../08-BestPractices/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
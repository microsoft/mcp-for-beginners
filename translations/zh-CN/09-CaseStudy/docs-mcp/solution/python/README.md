# 使用 Chainlit 和 Microsoft Learn Docs MCP 的学习计划生成器

## 前置条件

- Python 3.8 或更高版本  
- pip（Python 包管理器）  
- 可访问互联网以连接到 Microsoft Learn Docs MCP 服务器  

## 安装

1. 克隆此代码库或下载项目文件。  
2. 安装所需的依赖项：  

   ```bash
   pip install -r requirements.txt
   ```  

## 使用方法

### 场景 1：向 Docs MCP 提交简单查询  
一个命令行客户端，用于连接 Docs MCP 服务器，发送查询并打印结果。  

1. 运行脚本：  
   ```bash
   python scenario1.py
   ```  
2. 在提示符中输入您的文档问题。  

### 场景 2：学习计划生成器（基于 Chainlit 的 Web 应用）  
一个基于 Web 的界面（使用 Chainlit），允许用户为任何技术主题生成个性化的逐周学习计划。  

1. 启动 Chainlit 应用：  
   ```bash
   chainlit run scenario2.py
   ```  
2. 在浏览器中打开终端中提供的本地 URL（例如：http://localhost:8000）。  
3. 在聊天窗口中输入您的学习主题和学习周数（例如，“AI-900 认证，8 周”）。  
4. 应用将返回一个逐周的学习计划，包括相关的 Microsoft Learn 文档链接。  

**所需环境变量：**  

要使用场景 2（带有 Azure OpenAI 的 Chainlit Web 应用），您需要在 `python` 目录下的 `.env` 文件中设置以下环境变量：  

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```  

在运行应用之前，请用您的 Azure OpenAI 资源详细信息填写这些值。  

> [!TIP]  
> 您可以通过 [Azure AI Foundry](https://ai.azure.com/) 轻松部署自己的模型。  

### 场景 3：在 VS Code 中使用 MCP 服务器查看文档  

无需切换浏览器标签即可搜索文档，您可以直接在 VS Code 中引入 Microsoft Learn Docs。这使您能够：  
- 在不离开编码环境的情况下，在 VS Code 中搜索和阅读文档。  
- 引用文档并将链接直接插入到 README 或课程文件中。  
- 将 GitHub Copilot 和 MCP 结合使用，实现无缝的 AI 驱动文档工作流。  

**示例用例：**  
- 在编写课程或项目文档时快速添加参考链接到 README。  
- 使用 Copilot 生成代码，同时使用 MCP 即时查找并引用相关文档。  
- 保持专注于编辑器，提高生产力。  

> [!IMPORTANT]  
> 确保您的工作区中有有效的 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) 配置文件（位置为 `.vscode/mcp.json`）。  

## 为什么场景 2 使用 Chainlit？

Chainlit 是一个现代的开源框架，用于构建对话式 Web 应用。它使创建连接到后端服务（如 Microsoft Learn Docs MCP 服务器）的聊天用户界面变得简单。此项目使用 Chainlit 提供了一种简单、交互式的方式来实时生成个性化学习计划。通过利用 Chainlit，您可以快速构建和部署基于聊天的工具，从而提升生产力和学习效果。  

## 功能概述

此应用允许用户通过简单输入主题和学习时长来创建个性化学习计划。应用会解析您的输入，查询 Microsoft Learn Docs MCP 服务器以获取相关内容，并将结果组织成结构化的逐周计划。每周的推荐内容会显示在聊天窗口中，方便您跟随计划并跟踪进度。集成确保您始终获得最新、最相关的学习资源。  

## 示例查询

在聊天窗口中尝试以下查询，看看应用的响应：  

- `AI-900 认证，8 周`  
- `学习 Azure Functions，4 周`  
- `Azure DevOps，6 周`  
- `Azure 数据工程，10 周`  
- `Microsoft 安全基础，5 周`  
- `Power Platform，7 周`  
- `Azure AI 服务，12 周`  
- `云架构，9 周`  

这些示例展示了应用在不同学习目标和时间范围内的灵活性。  

## 参考资料

- [Chainlit 文档](https://docs.chainlit.io/)  
- [MCP 文档](https://github.com/MicrosoftDocs/mcp)  

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。
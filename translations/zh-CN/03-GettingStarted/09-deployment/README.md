# 部署 MCP 服务器

> [!NOTE]
> 使用 `/sse` 端点的配置示例针对的是传统的 HTTP+SSE 传输。MCP `2026-07-28` 远程服务器使用可流式 HTTP，通常在服务器定义的端点上，比如 `/mcp`。
> 
> 

部署您的 MCP 服务器使其他人能够访问其工具和资源，超越您的本地环境。根据您对可扩展性、可靠性和易管理性的需求，有多种部署策略可供选择。以下内容为本地、容器和云端部署 MCP 服务器提供指导。

## 概览

本课程介绍如何部署您的 MCP 服务器应用。

## 学习目标

完成本课后，您将能够：

- 评估不同的部署方法。
- 部署您的应用。

## 本地开发和部署

如果您的服务器目的是运行在用户机器上供其使用，可以按照以下步骤操作：

1. <strong>下载服务器</strong>。如果服务器不是您编写的，请先下载到您的机器。
1. <strong>启动服务器进程</strong>：运行您的 MCP 服务器应用程序。

对于 SSE（stdio 类型服务器不需要）

1. <strong>配置网络</strong>：确保服务器在预期端口可访问。
1. <strong>连接客户端</strong>：使用类似 `http://localhost:3000` 的本地连接 URL。

## 云端部署

MCP 服务器可以部署到各种云平台：

- <strong>无服务器函数</strong>：将轻量级 MCP 服务器作为无服务器函数进行部署。
- <strong>容器服务</strong>：使用 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服务。
- **Kubernetes**：在 Kubernetes 集群中部署和管理 MCP 服务器，实现高可用性。

### 示例：Azure Container Apps

Azure Container Apps 支持部署 MCP 服务器。目前仍在开发中，现阶段支持 SSE 服务器。

下面是操作步骤：

1. 克隆一个仓库：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 本地运行以测试：

  ```sh
  uv venv
  uv sync

  # Linux/macOS
  export API_KEYS=<AN_API_KEY>
  # Windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若要本地尝试，请在 *.vscode* 目录中创建 *mcp.json* 文件，并添加以下内容：

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  SSE 服务器启动后，您可以点击 JSON 文件中的播放图标，您现在应该能看到 GitHub Copilot 识别了服务器上的工具图标。

1. 部署时，运行以下命令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

这样，您就可以通过这些步骤实现本地部署或部署到 Azure。

## 额外资源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 仓库](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 后续内容

- 下一步: [高级服务器主题](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
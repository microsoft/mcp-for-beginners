# 部署 MCP 服务器

部署您的 MCP 服务器使其他人能够访问其工具和资源，突破本地环境的限制。根据您对可扩展性、可靠性和易管理性的需求，有多种部署策略可供选择。下面您将找到在本地、容器和云端部署 MCP 服务器的指导。

## 概述

本课涵盖如何部署您的 MCP Server 应用。

## 学习目标

完成本课后，您将能够：

- 评估不同的部署方法。
- 部署您的应用。

## 本地开发和部署

如果您的服务器是面向在用户机器上运行的，您可以按照以下步骤操作：

1. **下载服务器**。如果您没有编写该服务器，请先下载到您的机器上。
1. **启动服务器进程**：运行您的 MCP 服务器应用。

对于 SSE（stdio 类型服务器不需要此步骤）

1. **配置网络**：确保服务器可以通过预期端口访问。
1. **连接客户端**：使用如 `http://localhost:3000` 的本地连接 URL。

## 云端部署

MCP 服务器可以部署到各种云平台：

- **无服务器函数**：将轻量级 MCP 服务器作为无服务器函数部署。
- **容器服务**：使用例如 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服务。
- **Kubernetes**：在 Kubernetes 集群中部署和管理 MCP 服务器，实现高可用性。

### 示例：Azure Container Apps

Azure Container Apps 支持 MCP 服务器的部署。该功能仍在开发中，目前支持 SSE 服务器。

操作步骤如下：

1. 克隆一个仓库：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 在本地运行以测试：

  ```sh
  uv venv
  uv sync

  # Linux/macOS
  export API_KEYS=<AN_API_KEY>
  # Windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若要在本地尝试，创建一个位于 *.vscode* 目录中的 *mcp.json* 文件并添加以下内容：

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

  启动 SSE 服务器后，您可以点击 JSON 文件中的播放图标，您现在应该能在 GitHub Copilot 中看到服务器上被拾取的工具，查看工具图标。

1. 要部署，执行以下命令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

就这样，按照这些步骤即可本地部署或部署到 Azure。

## 额外资源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 仓库](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## 后续内容

- 下一步：[高级服务器主题](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始语言版本的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
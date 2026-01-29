# 部署 MCP 服务器

部署你的 MCP 服务器可以让其他人访问其工具和资源，而不仅限于你的本地环境。根据你对可扩展性、可靠性和管理便捷性的需求，有多种部署策略可供选择。下面你将找到关于在本地、容器和云端部署 MCP 服务器的指导。

## 概述

本课将介绍如何部署你的 MCP Server 应用。

## 学习目标

完成本课后，你将能够：

- 评估不同的部署方法。
- 部署你的应用。

## 本地开发与部署

如果你的服务器是为了在用户机器上运行并被使用，可以按照以下步骤操作：

1. **下载服务器**。如果你没有编写服务器代码，先将服务器下载到你的机器上。  
1. **启动服务器进程**：运行你的 MCP 服务器应用。

对于 SSE（stdio 类型服务器不需要此步骤）

1. **配置网络**：确保服务器在预期端口可访问。  
1. **连接客户端**：使用类似 `http://localhost:3000` 的本地连接 URL。

## 云端部署

MCP 服务器可以部署到多种云平台：

- **无服务器函数**：将轻量级 MCP 服务器作为无服务器函数部署。  
- **容器服务**：使用 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服务。  
- **Kubernetes**：在 Kubernetes 集群中部署和管理 MCP 服务器，实现高可用性。

### 示例：Azure Container Apps

Azure Container Apps 支持部署 MCP 服务器。该功能仍在开发中，目前支持 SSE 服务器。

操作步骤如下：

1. 克隆一个仓库：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 在本地运行以测试：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若要本地调试，在 *.vscode* 目录下创建一个 *mcp.json* 文件，并添加以下内容：

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

  SSE 服务器启动后，你可以点击 JSON 文件中的播放图标，此时 GitHub Copilot 应该能识别服务器上的工具，查看工具图标。

1. 部署时，运行以下命令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

就是这样，通过这些步骤你可以在本地部署，也可以部署到 Azure。

## 额外资源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP 仓库](https://github.com/anthonychu/azure-container-apps-mcp-sample)  

## 接下来

- 下一步：[实战演练](../../04-PracticalImplementation/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。
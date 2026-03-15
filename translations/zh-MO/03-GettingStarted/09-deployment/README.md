# 部署 MCP 服務器

部署您的 MCP 服務器可以讓其他人超越本地環境訪問其工具和資源。根據您對可擴展性、可靠性和管理便利性的需求，有多種部署策略可供考慮。以下將提供在本地、容器和雲端部署 MCP 服務器的指引。

## 概述

本課程涵蓋如何部署您的 MCP 服務器應用程式。

## 學習目標

完成本課程後，您將能夠：

- 評估不同的部署方法。
- 部署您的應用程式。

## 本地開發與部署

如果您的服務器是設計運行在用戶機器上供其使用，您可以遵循以下步驟：

1. **下載服務器**。如果您沒有自行撰寫服務器，請先將其下載到您的機器。  
1. **啟動服務器程序**：運行您的 MCP 服務器應用程式  

對於 SSE（不需要用於 stdio 類型的服務器）

1. **配置網絡**：確保服務器在預期的端口可訪問  
1. **連接客戶端**：使用本地連接網址，如 `http://localhost:3000`

## 雲端部署

MCP 服務器可以部署到各種雲端平台：

- **無伺服器函數**：將輕量級 MCP 服務器部署為無伺服器函數  
- **容器服務**：使用 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服務  
- **Kubernetes**：在 Kubernetes 叢集部署及管理 MCP 服務器，以實現高可用性

### 範例：Azure Container Apps

Azure Container Apps 支援部署 MCP 服務器。此功能仍在開發中，目前支援 SSE 服務器。

您可以按照以下步驟進行：

1. 克隆一個代碼庫：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 本地運行以測試：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若要本地測試，請在 *.vscode* 目錄中建立一個 *mcp.json* 文件，並加入以下內容：

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

  SSE 服務器啟動後，您可以點擊 JSON 文件中的播放圖示，您應該會看到 GitHub Copilot 偵測到服務器上的工具，請參閱工具圖示。

1. 若要部署，執行以下指令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

就這樣，通過這些步驟您可以在本地部署，或部署到 Azure。

## 額外資源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 代碼庫](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 下一步

- 下一課： [進階服務器主題](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為最具權威的來源。對於重要資訊，建議採用專業人工翻譯。本公司對因使用本翻譯而引致的任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
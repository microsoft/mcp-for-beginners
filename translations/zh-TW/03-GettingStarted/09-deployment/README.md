# 部署 MCP 伺服器

部署您的 MCP 伺服器可以讓他人超越您的本地環境來存取其工具和資源。根據您對可擴充性、可靠性和管理便利性的需求，有多種部署策略可供考量。以下將引導您如何在本地、容器中及雲端部署 MCP 伺服器。

## 概覽

本課程涵蓋如何部署您的 MCP Server 應用程式。

## 學習目標

完成本課程後，您將能夠：

- 評估不同的部署方法。
- 部署您的應用程式。

## 本地開發與部署

如果您的伺服器是設計供使用者在其機器上運行，您可以依照以下步驟：

1. **下載伺服器**。若您並非自行撰寫伺服器，請先下載到您的機器。
1. **啟動伺服器程序**：執行您的 MCP 伺服器應用程式

針對 SSE（stdio 類型伺服器則不需此步驟）

1. **設定網路**：確保伺服器在預期的埠可被存取
1. **連接客戶端**：使用像 `http://localhost:3000` 的本地連接 URL

## 雲端部署

MCP 伺服器可部署至各種雲端平台：

- **無伺服器函式**：以無伺服器函式方式部署輕量級 MCP 伺服器
- **容器服務**：使用 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服務
- **Kubernetes**：在 Kubernetes 叢集內部署與管理 MCP 伺服器以達高可用性

### 範例：Azure Container Apps

Azure Container Apps 支援部署 MCP 伺服器。目前仍在開發中，且目前支援 SSE 伺服器。

以下是操作步驟：

1. 克隆一個儲存庫：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 在本地執行以測試：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若想在本地試運行，請在 *.vscode* 目錄下建立 *mcp.json* 檔案並加入下列內容：

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

  SSE 伺服器啟動後，您可以在 JSON 檔案中點擊播放圖示，現在應能看到伺服器上的工具被 GitHub Copilot 偵測，請見工具圖示。

1. 部署時，執行以下指令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

就是這樣，您可以依照這些步驟在本地或透過 Azure 進行部署。

## 其他資源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 儲存庫](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## 接下來學習

- 下一課：[進階伺服器主題](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於追求準確性，但請注意自動翻譯可能存在錯誤或不精確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所導致的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
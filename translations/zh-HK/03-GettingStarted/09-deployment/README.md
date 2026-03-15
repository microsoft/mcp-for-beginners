# 部署 MCP 伺服器

部署您的 MCP 伺服器讓其他人能夠在本地環境之外存取其工具和資源。根據您對可擴展性、可靠性和管理便利性的需求，有多種部署策略可供考慮。以下將說明如何在本地、容器及雲端部署 MCP 伺服器。

## 總覽

本課程涵蓋如何部署您的 MCP 伺服器應用程式。

## 學習目標

完成本課程後，您將能夠：

- 評估不同的部署方法。
- 部署您的應用程式。

## 本地開發與部署

如果您的伺服器是打算在使用者機器上執行，供其使用，您可以依照以下步驟：

1. **下載伺服器**。如果您不是自行開發伺服器，請先將它下載到您的電腦上。
1. **啟動伺服器進程**：執行您的 MCP 伺服器應用程式

對 SSE （不適用於 stdio 類型伺服器）

1. **配置網路**：確保伺服器在預期的連接埠可訪問
1. **連接客戶端**：使用本地連接網址如 `http://localhost:3000`

## 雲端部署

MCP 伺服器可部署於多個雲端平台：

- **無伺服器函式**：部署輕量級 MCP 伺服器為無伺服器函式
- **容器服務**：使用 Azure Container Apps、AWS ECS 或 Google Cloud Run 等服務
- **Kubernetes**：在 Kubernetes 叢集部署及管理 MCP 伺服器，實現高可用性

### 範例：Azure Container Apps

Azure Container Apps 支援部署 MCP 伺服器。此功能仍在開發中，目前僅支援 SSE 伺服器。

以下為操作說明：

1. 克隆一個程式碼庫：

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

1. 若欲在本地測試，請在 *.vscode* 目錄下建立 *mcp.json* 檔案，並加入以下內容：

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

  啟動 SSE 伺服器後，您可點擊 JSON 檔案中的播放圖示，GitHub Copilot 即會開始讀取伺服器上的工具，請參見工具圖示。

1. 部署時執行以下指令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

大功告成，即可透過以上步驟在本地或 Azure 端部署。

## 附加資源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 程式庫](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 下一步

- 下一課：[進階伺服器主題](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能存在錯誤或不準確之處。原文文件的原始語言版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。本公司對因使用此翻譯而引起的任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
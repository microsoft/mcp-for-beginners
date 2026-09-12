# 部署 MCP 伺服器

> [!NOTE]
> 使用 `/sse` 端點的配置範例是針對舊版 HTTP+SSE 傳輸方式。MCP `2026-07-28` 遠端伺服器通常使用 Streamable HTTP，端點由伺服器定義，像是 `/mcp`。
> 
> 

部署你的 MCP 伺服器可讓其他人超越你的本地環境存取其工具和資源。根據你的可擴展性、可靠性及管理方便性需求，有幾種部署策略可以考慮。以下為你提供在本地、容器中及雲端部署 MCP 伺服器的指引。

## 概覽

本課程說明如何部署你的 MCP 伺服器應用程式。

## 學習目標

完成本課程後，你將能：

- 評估不同的部署方式。
- 部署你的應用程式。

## 本地開發與部署

若你的伺服器是預計在使用者機器上運行並被消費，請遵循以下步驟：

1. <strong>下載伺服器</strong>。若你不是伺服器的開發者，先將其下載到你的機器。
1. <strong>啟動伺服器程序</strong>：執行你的 MCP 伺服器應用程式。

針對 SSE（stdio 類型伺服器不需要此步驟）

1. <strong>配置網絡</strong>：確保伺服器在預期的埠口可被訪問。
1. <strong>連接客戶端</strong>：使用像 `http://localhost:3000` 的本地連線 URL。

## 雲端部署

MCP 伺服器可以部署至多種雲端平台：

- <strong>無伺服器函數</strong>：以無伺服器函數形式部署輕量級 MCP 伺服器。
- <strong>容器服務</strong>：使用 Azure Container Apps、AWS ECS、或 Google Cloud Run 等服務。
- **Kubernetes**：在 Kubernetes 叢集中部署和管理 MCP 伺服器以實現高可用性。

### 範例：Azure Container Apps

Azure Container Apps 支援部署 MCP 伺服器。目前仍在開發中，現階段支援 SSE 伺服器。

以下是操作步驟：

1. 克隆一個倉庫：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. 在本地運行測試：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. 若要在本地嘗試，於 *.vscode* 目錄下建立 *mcp.json* 檔案，並加入以下內容：

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

  SSE 伺服器啟動後，你可以點選 JSON 檔案的播放圖示，GitHub Copilot 應該會偵測到伺服器上的工具，請參考工具圖示。

1. 部署時，執行以下命令：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

就是這樣，透過這些步驟你可以在本地或 Azure 上部署。

## 附加資源

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 文章](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP 倉庫](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 後續步驟

- 下一課： [進階伺服器主題](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
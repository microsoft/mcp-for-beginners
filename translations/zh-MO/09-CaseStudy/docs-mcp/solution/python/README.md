# 使用 Chainlit 和 Microsoft Learn Docs MCP 的學習計劃生成器

## 先決條件

- Python 3.8 或更高版本
- pip（Python 套件管理工具）
- 可連接 Microsoft Learn Docs MCP 伺服器的網絡訪問

## 安裝

1. 克隆此存儲庫或下載項目文件。
2. 安裝所需的依賴項：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 情境 1：簡單查詢 Docs MCP
一個命令行客戶端，連接到 Docs MCP 伺服器，發送查詢並打印結果。

1. 運行腳本：
   ```bash
   python scenario1.py
   ```
2. 在提示符中輸入您的文檔問題。

### 情境 2：學習計劃生成器（Chainlit 網頁應用）
一個基於網頁的界面（使用 Chainlit），允許用戶生成個性化的逐週學習計劃，適用於任何技術主題。

1. 啟動 Chainlit 應用：
   ```bash
   chainlit run scenario2.py
   ```
2. 在瀏覽器中打開終端提供的本地 URL（例如：http://localhost:8000）。
3. 在聊天窗口中輸入您的學習主題和希望學習的週數（例如："AI-900 認證，8 週"）。
4. 應用將回應一個逐週的學習計劃，包括相關的 Microsoft Learn 文檔鏈接。

**所需環境變數：**

要使用情境 2（使用 Azure OpenAI 的 Chainlit 網頁應用），您必須在 `python` 目錄中的 `.env` 文件中設置以下環境變數：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

在運行應用之前，請用您的 Azure OpenAI 資源詳細信息填寫這些值。

> [!TIP]
> 您可以使用 [Azure AI Foundry](https://ai.azure.com/) 輕鬆部署自己的模型。

### 情境 3：在 VS Code 中使用 MCP 伺服器的內嵌文檔

與其切換瀏覽器標籤來搜索文檔，您可以直接在 VS Code 中引入 Microsoft Learn Docs，使用 MCP 伺服器。這使您能夠：
- 在不離開編碼環境的情況下搜索和閱讀文檔。
- 引用文檔並直接將鏈接插入 README 或課程文件。
- 將 GitHub Copilot 和 MCP 結合使用，實現無縫的 AI 驅動文檔工作流程。

**示例使用場景：**
- 在撰寫課程或項目文檔時快速添加引用鏈接到 README。
- 使用 Copilot 生成代碼，同時使用 MCP 即時查找並引用相關文檔。
- 專注於編輯器，提高工作效率。

> [!IMPORTANT]
> 確保您的工作區中有有效的 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) 配置文件（位置為 `.vscode/mcp.json`）。

## 為什麼選擇 Chainlit 用於情境 2？

Chainlit 是一個現代的開源框架，用於構建對話式網頁應用。它使得創建連接到後端服務（如 Microsoft Learn Docs MCP 伺服器）的聊天界面變得簡單。本項目使用 Chainlit 提供了一種簡單、互動的方式來實時生成個性化學習計劃。通過利用 Chainlit，您可以快速構建和部署基於聊天的工具，提升生產力和學習效果。

## 此應用的功能

此應用允許用戶通過簡單輸入主題和持續時間來創建個性化學習計劃。應用會解析您的輸入，查詢 Microsoft Learn Docs MCP 伺服器以獲取相關內容，並將結果組織成結構化的逐週計劃。每週的推薦內容會顯示在聊天窗口中，方便您跟蹤進度。此集成確保您始終獲得最新、最相關的學習資源。

## 示例查詢

在聊天窗口中嘗試以下查詢，看看應用如何回應：

- `AI-900 認證，8 週`
- `學習 Azure Functions，4 週`
- `Azure DevOps，6 週`
- `Azure 數據工程，10 週`
- `Microsoft 安全基礎知識，5 週`
- `Power Platform，7 週`
- `Azure AI 服務，12 週`
- `雲架構，9 週`

這些示例展示了應用在不同學習目標和時間框架上的靈活性。

## 參考資料

- [Chainlit 文檔](https://docs.chainlit.io/)
- [MCP 文檔](https://github.com/MicrosoftDocs/mcp)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。
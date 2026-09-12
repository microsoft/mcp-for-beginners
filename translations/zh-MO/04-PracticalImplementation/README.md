# 實務實作

[![如何使用實際工具和工作流程構建、測試及部署 MCP 應用](../../../translated_images/zh-MO/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(點擊上圖觀看本課程影片)_

實務實作是讓模型上下文協議（MCP）威力具體呈現的關鍵。儘管理解 MCP 的理論與架構很重要，但真正的價值在於你將這些概念應用於構建、測試和部署解決方案以解決現實世界問題。本章節架起概念知識與實作開發之間的橋樑，引導你完成將基於 MCP 的應用實現的過程。

無論你是在開發智能助理、將 AI 整合進業務工作流程，還是構建用於資料處理的自訂工具，MCP 都能提供靈活的基礎。其語言無關設計及支援多種流行編程語言的官方 SDK，使廣大開發者都能輕鬆入門。利用這些 SDK，你可以快速原型設計、反覆迭代，並在不同平台和環境上擴展你的解決方案。

接下來的章節，你會看到實作範例、示例程式碼與部署策略，展示如何在 C#、Java (Spring)、TypeScript、JavaScript 和 Python 中實現 MCP。你也會學習如何除錯及測試 MCP 伺服器、管理 API，並使用 Azure 將解決方案部署到雲端。這些實作資源設計用以加速你的學習，幫助你自信且穩健地構建可應用於生產環境的 MCP 應用。

## 概覽

本課聚焦於多種程式語言中 MCP 實作的實務層面。我們將探討如何利用 MCP SDK 在 C#、Java (Spring)、TypeScript、JavaScript 和 Python 中構建穩健的應用，除錯和測試 MCP 伺服器，並創建可重用的資源、提示與工具。

## 學習目標

完成本課後，你將能夠：

- 使用各種程式語言的官方 SDK 實作 MCP 解決方案
- 有系統地除錯與測試 MCP 伺服器
- 創建並使用伺服器功能（資源、提示與工具）
- 設計有效的 MCP 工作流程以處理複雜任務
- 優化 MCP 實作以提升效能與可靠性

## 官方 SDK 資源

模型上下文協議為多種語言提供官方 SDK。MCP `2026-07-28` 的 SDK 支援將獨立推出，所以在假設協議相容性前，請先檢查每個 SDK 的發行說明與範例中的套件版本。詳見[官方 SDK 列表](https://modelcontextprotocol.io/docs/sdk):

(上文無需翻譯)
(上文無需翻譯)

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) <strong>注意：</strong>需要依賴[Project Reactor](https://projectreactor.io)。（詳見[討論議題 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本節提供多種程式語言中 MCP 實作的實務範例。你可以在 `samples` 目錄中找到依語言分類的範例程式碼。

### 可用範例

本倉庫包含以下程式語言的[範例實作](../../../04-PracticalImplementation/samples)：


- [C#](./samples/csharp/README.md)
- [Java 搭配 Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例展示該特定語言和生態系中 MCP 的關鍵概念和實作範式。

### 實用指南

其他實用的 MCP 實作指南：

- [分頁與大型結果集](./pagination/README.md) - 處理基於游標的分頁，適用於工具、資源與大型資料集

## 核心伺服器功能

MCP 伺服器可實作這些功能的任意組合：

### 資源

資源提供上下文與資料供使用者或 AI 模型使用：

- 文件庫
- 知識庫
- 結構化資料來源
- 檔案系統

### 提示

提示是為使用者設計的模板化訊息與工作流程：

- 預設對話模板
- 引導式互動模式
- 專門化對話結構

### 工具

工具是讓 AI 模型執行的功能：

- 資料處理工具
- 外部 API 整合
- 運算能力
- 搜尋功能

## 範例實作：C# 實作

官方 C# SDK 倉庫包含多個示範 MCP 不同面向的範例實作：

- **基礎 MCP 客戶端**：簡單範例展示如何建立 MCP 客戶端並呼叫工具
- **基礎 MCP 伺服器**：使用最少工具註冊的伺服器實作
- **進階 MCP 伺服器**：完整功能伺服器，包含工具註冊、身份驗證與錯誤處理
- **ASP.NET 整合**：展示與 ASP.NET Core 整合的範例
- <strong>工具實作模式</strong>：多種工具實作模式，搭配不同複雜度

MCP C# SDK 現在仍處於預覽階段，API 可能會變動。我們會持續隨著 SDK 的發展更新此部落格。

### 主要功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 建立您的[第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

欲獲得完整 C# 實作範例，請訪問[官方 C# SDK 範例倉庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java 搭配 Spring 實作

Java with Spring SDK 提供企業級功能，實現強健的 MCP 實作選項。

### 主要功能

- Spring Framework 整合
- 強型別安全性
- 反應式程式設計支援
- 全面錯誤處理

完整的 Java 搭配 Spring 實作範例，請參見樣本目錄中的 [Java with Spring sample](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且彈性的 MCP 實作方式。

### 主要功能

- 支援 Node.js 與瀏覽器環境
- 基於 Promise 的 API
- 容易整合 Express 與其他框架
- 支援 WebSocket 串流功能

完整的 JavaScript 實作範例，請參見樣本目錄中的 [JavaScript sample](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 提供符合 Python 特色的 MCP 實作方式，並有卓越的機器學習框架整合。

### 主要功能

- 支援 asyncio 的 async/await
- FastAPI 整合
- 簡易工具註冊
- 與流行機器學習庫原生整合

完整的 Python 實作範例，請參見樣本目錄中的 [Python sample](samples/python/README.md)。


## API 管理


Azure API 管理是我們如何保護 MCP 伺服器的一個很好的解決方案。其想法是將 Azure API 管理實例放在您的 MCP 伺服器前面，讓它處理您可能想要的功能，例如：

- 流量限制
- 令牌管理
- 監控
- 負載均衡
- 安全性

### Azure 範例

這裡有一個 Azure 範例，正是這樣做的，即[建立 MCP 伺服器並用 Azure API 管理保護它](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

參見下圖中授權流程的發生方式：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

在前面的圖中，發生了以下事件：

- 使用 Microsoft Entra 進行身份驗證/授權。
- Azure API 管理作為閘道，並使用策略來導向和管理流量。
- Azure 監控記錄所有請求以供進一步分析。

#### 授權流程

讓我們更詳細地看看授權流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

了解更多關於
[MCP 授權規範](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/)。

## 將遠端 MCP 伺服器部署到 Azure

讓我們看看是否能部署前面提及的範例：

1. 複製儲存庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 資源提供者。

   - 如果使用 Azure CLI，執行 `az provider register --namespace Microsoft.App --wait`。
   - 如果使用 Azure PowerShell，執行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。之後等待片刻，執行 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 檢查註冊是否完成。

1. 執行此[azd](https://aka.ms/azd)命令來配置 API 管理服務、帶有程式碼的函數應用以及所有其他所需的 Azure 資源

    ```shell
    azd up
    ```

    此命令應該會部署所有 Azure 上的雲端資源

### 使用 MCP Inspector 測試您的伺服器

1. 在一個<strong>新終端視窗</strong>中，安裝並運行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    您應該會看到類似的介面：

    ![Connect to Node inspector](../../../translated_images/zh-MO/connect.141db0b2bd05f096.webp)

1. CTRL 點擊以從應用程序顯示的 URL (例如 [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)) 載入 MCP Inspector 網頁應用程式
1. 將傳輸類型設定為 `SSE`
1. 將 URL 設為您在執行 `azd up` 後顯示的 API 管理 SSE 端點，然後<strong>連接</strong>：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. <strong>列出工具</strong>。點擊一個工具並<strong>執行工具</strong>。  

如果所有步驟都成功，您現在應該已連接到 MCP 伺服器，並且能夠呼叫一個工具。

## Azure 專用的 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：這組儲存庫是使用 Python、C# .NET 或 Node/TypeScript 的 Azure 函數來構建並部署自訂遠端 MCP（模型上下文協定）伺服器的快速入門範本。

範例提供完整解決方案，允許開發者：

- 本地構建與運行：在本機開發及調試 MCP 伺服器
- 部署到 Azure：使用簡單的 azd up 命令輕鬆部署至雲端
- 從客戶端連接：從多種客戶端連接 MCP 伺服器，包括 VS Code 的 Copilot 代理模式及 MCP Inspector 工具

### 主要功能

- 以安全為設計：MCP 伺服器使用金鑰及 HTTPS 進行保護
- 身份驗證選項：支援使用內建身份驗證及/或 API 管理的 OAuth
- 網路隔離：利用 Azure 虛擬網路（VNET）實現網路隔離
- 無伺服器架構：使用 Azure 函數實現可擴展的事件驅動執行
- 本地開發支持：提供完整的本地開發與調試支持
- 簡單部署：精簡的 Azure 部署流程

儲存庫包含所有必要的配置文件、源代碼及基礎架構定義，使您快速開始實作生產準備的 MCP 伺服器。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Python 的 Azure 函數實作的 MCP 範例

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 C# .NET 的 Azure 函數實作的 MCP 範例

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Node/TypeScript 的 Azure 函數實作的 MCP 範例

## 主要收穫

- MCP SDK 提供專門語言工具來實作穩健的 MCP 解決方案
- 偵錯和測試過程對於 MCP 應用的可靠性至關重要
- 可重用的提示範本能夠確保 AI 互動的一致性
- 設計良好的工作流程可以使用多個工具協調複雜任務
- 實作 MCP 解決方案時需考慮安全性、效能及錯誤處理

## 練習

設計一個實用的 MCP 工作流程，以解決您領域中的真實問題：

1. 識別 3-4 個有助於解決此問題的工具
2. 創建工作流程圖，展示這些工具如何互動
3. 使用您喜歡的語言實作其中一個工具的基本版本
4. 創建一個提示範本，幫助模型有效使用您的工具

## 額外資源

---

## 下一步

下一章節：[進階主題](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
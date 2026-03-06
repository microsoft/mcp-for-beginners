# 實作應用

[![如何使用真實工具和工作流程建構、測試及部署 MCP 應用程式](../../../translated_images/zh-MO/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_（點擊上方圖片觀看本課程視頻）_

實作應用是 Model Context Protocol (MCP) 力量具體展現的地方。雖然了解 MCP 背後的理論與架構很重要，但真正的價值在於將這些概念應用於建構、測試及部署解決實際問題的方案。本章搭起概念知識與實務開發之間的橋樑，帶領您了解如何將基於 MCP 的應用程式付諸實現。

無論您是在開發智能助理、將 AI 整合至業務流程，或是建構用於資料處理的自訂工具，MCP 都提供了一個彈性的基礎。其語言中立設計以及針對多種流行程式語言的官方 SDK，使廣大開發者能夠輕鬆取得。藉由這些 SDK，您可以快速製作原型、迭代並跨不同平台及環境擴展您的方案。

接下來的章節中，您將找到以 C#、Java Spring、TypeScript、JavaScript 與 Python 實作 MCP 的實務範例、示範程式碼及部署策略。您還會學習如何除錯與測試 MCP 伺服器、管理 API，以及使用 Azure 部署解決方案。這些實務資源旨在加速您的學習，並助您自信地建構堅固且可投入生產的 MCP 應用程式。

## 概觀

本課程聚焦於多種程式語言中 MCP 實作的實務面。我們將探討如何使用 C#、Java Spring、TypeScript、JavaScript 及 Python 的 MCP SDK 建構穩健的應用、除錯與測試 MCP 伺服器，以及建立可重用的資源、提示和工具。

## 學習目標

完成本課程後，您將能夠：

- 使用官方 SDK 於多種程式語言中實作 MCP 解決方案
- 系統性地除錯與測試 MCP 伺服器
- 建立並使用伺服器功能（資源、提示和工具）
- 設計複雜任務的有效 MCP 工作流程
- 優化 MCP 實作的效能與可靠性

## 官方 SDK 資源

Model Context Protocol 提供多種語言的官方 SDK（符合 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **註：** 需要依賴 [Project Reactor](https://projectreactor.io)。（詳見 [討論議題 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本節提供跨多種程式語言實作 MCP 的實務範例。您可以於 `samples` 目錄依語言分類找到示範程式碼。

### 提供的範例

本代碼庫包含以下語言的[範例實作](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例皆示範了該語言及生態系中 MCP 的關鍵概念與實作模式。

### 實務指南

更多實際 MCP 實作指南：

- [分頁與大量結果集](./pagination/README.md) – 處理工具、資源與大量資料集的基於游標的分頁

## 核心伺服器功能

MCP 伺服器可以實作以下任意組合的功能：

### 資源

資源提供使用者或 AI 模型可用的上下文與資料：

- 文件庫
- 知識庫
- 結構化資料來源
- 檔案系統

### 提示

提示是用於使用者的模板訊息和工作流程：

- 預先定義的會話模板
- 指導式互動模式
- 專門化對話結構

### 工具

工具是 AI 模型可執行的函式：

- 資料處理工具
- 外部 API 集成
- 計算功能
- 搜尋功能

## 範例實作：C# 實作

官方 C# SDK 倉庫包含多個範例實作，展示 MCP 的不同面向：

- **基礎 MCP 用戶端**：簡單示例展示如何建立 MCP 用戶端及呼叫工具
- **基礎 MCP 伺服器**：具有基本工具註冊的極簡伺服器實作
- **進階 MCP 伺服器**：功能完善的伺服器，包含工具註冊、認證及錯誤處理
- **ASP.NET 整合**：展示與 ASP.NET Core 整合的範例
- **工具實現模式**：多種不同複雜度的工具實作模式

MCP C# SDK 為預覽版，API 可能變動。我們將隨著 SDK 進展持續更新本部落格。

### 主要功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 建構您的[第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

完整 C# 實作範例請參閱 [官方 C# SDK 範例倉庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java Spring 實作

Java Spring SDK 提供企業級特性的 MCP 強大實作選項。

### 主要功能

- Spring 框架整合
- 強型別安全
- 反應式程式支援
- 全面錯誤處理

完整 Java Spring 實作範例請參閱範例目錄中的 [Java Spring 範例](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且彈性的 MCP 實作方式。

### 主要功能

- 支援 Node.js 及瀏覽器
- 基於 Promise 的 API
- 易與 Express 及其他框架整合
- 支援 WebSocket 流式傳輸

完整 JavaScript 實作範例請參閱範例目錄中的 [JavaScript 範例](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 提供符合 Python 慣用法的 MCP 實作，並有優異的機器學習框架整合。

### 主要功能

- 使用 asyncio 的 async/await 支援
- FastAPI 整合
- 簡單的工具註冊
- 與流行機器學習庫的原生整合

完整 Python 實作範例請參閱範例目錄中的 [Python 範例](samples/python/README.md)。

## API 管理

Azure API 管理是保護 MCP 伺服器的良好方案。思路是在 MCP 伺服器前端放置 Azure API 管理實例，讓它處理您可能需要的功能，如：

- 速率限制
- 令牌管理
- 監控
- 負載平衡
- 安全性

### Azure 範例

這是一個示範範例，實現了「建立 MCP 伺服器並使用 Azure API 管理保護」的功能，地址為 [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

以下圖示展示授權流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

如上圖，流程包含：

- 使用 Microsoft Entra 執行身份驗證/授權
- Azure API 管理作為閘道，使用政策引導及管理流量
- Azure Monitor 記錄所有請求以供後續分析

#### 授權流程詳解

更詳細的授權流程如下：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

進一步了解 [MCP 授權規範](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## 部署遠端 MCP 伺服器至 Azure

讓我們來看看如何部署之前提及的範例：

1. 克隆倉庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 資源提供者。

   - 若您使用 Azure CLI，請執行 `az provider register --namespace Microsoft.App --wait`。
   - 若您使用 Azure PowerShell，請執行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。稍後可透過 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 檢查註冊狀態。

1. 執行此 [azd](https://aka.ms/azd) 指令以配置 API 管理服務、Function App（含程式碼）以及其他所有必要 Azure 資源

    ```shell
    azd up
    ```

    此命令將在 Azure 部署所有雲端資源

### 使用 MCP Inspector 測試您的伺服器

1. 在**新終端視窗**安裝並執行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    您應該會看到類似下方介面：

    ![Connect to Node inspector](../../../translated_images/zh-MO/connect.141db0b2bd05f096.webp)

1. Ctrl 點擊 MCP Inspector 網頁應用程式的顯示 URL（例如 [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）
1. 將傳輸類型設為 `SSE`
1. 將 URL 設為您在 `azd up` 後顯示的運行中 API 管理 SSE 端點，然後**連線**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **列出工具**。點選工具並 **執行工具**。

若以上步驟全部完成，您已成功連接至 MCP 伺服器並呼叫了一個工具。

## 適用於 Azure 的 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：這組倉庫提供使用 Azure Functions 與 Python、C# .NET 或 Node/TypeScript 快速啟動建置與部署自訂遠端 MCP（Model Context Protocol）伺服器的範本。

這些範例提供完整解決方案，讓開發者能夠：

- 本地建置及執行：在本地端開發並除錯 MCP 伺服器
- 部署至 Azure：使用簡單的 azd up 指令輕鬆部署到雲端
- 從用戶端連接：可從包括 VS Code Copilot Agent 模式及 MCP Inspector 工具的多種用戶端連結 MCP 伺服器

### 主要特點

- 安全設計：MCP 伺服器採用金鑰與 HTTPS 保護
- 認證選項：支援內建認證與/或 API 管理的 OAuth
- 網路隔離：支援使用 Azure 虛擬網路（VNET）進行網路隔離
- 無伺服器架構：利用 Azure Functions 實現可擴展的事件驅動執行
- 本地開發：完整本地開發及除錯支援
- 簡單部署：精簡的 Azure 部署流程

倉庫包含所有必要的設定檔、原始碼以及基礎設施定義，讓您快速開始生產級 MCP 伺服器實作。

- [Azure 遠端 MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 與 Python 實作 MCP 的範例

- [Azure 遠端 MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 與 C# .NET 實作 MCP 的範例

- [Azure 遠端 MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 與 Node/TypeScript 實作 MCP 的範例

## 重要重點

- MCP SDK 提供語言特定工具以實作強健的 MCP 解決方案
- 除錯與測試流程對於可靠的 MCP 應用至關重要
- 可重用的提示模板確保一致的 AI 互動
- 設計良好的工作流程可協調多項工具完成複雜任務
- 實作 MCP 解決方案需考量安全性、效能及錯誤處理

## 練習

設計一個實務 MCP 工作流程，以解決您領域中的實際問題：

1. 確定 3-4 個對解決此問題有幫助的工具
2. 繪製工作流程圖，展示這些工具如何互動
3. 使用您偏好的語言實作其中一個工具的基本版本
4. 建立幫助模型有效使用您工具的提示模板

## 附加資源

---

## 後續學習

下一章： [進階主題](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
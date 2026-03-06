# 實務實作

[![如何使用真實工具與工作流程來建置、測試及部署 MCP 應用程式](../../../translated_images/zh-TW/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_（點擊上方圖片觀看本課程影片）_

實務實作是讓模型上下文協定（Model Context Protocol，MCP）力量具體展現的階段。理解 MCP 的理論和架構很重要，但當你將這些概念應用於建構、測試及部署解決現實問題的方案時，真正的價值才開始顯現。本章節連結了概念性知識與實務開發，指導你如何讓基於 MCP 的應用程式活躍起來。

無論你是在開發智慧助理、將 AI 整合進商業工作流程，或是建置資料處理的自訂工具，MCP 提供了彈性的基礎。其語言無關的設計以及針對熱門程式語言的官方 SDK，讓廣大開發者都能輕鬆使用。藉由這些 SDK，你可以快速地原型設計、迭代與擴展你的解決方案，跨不同平台和環境進行開發。

接下來的章節中，你會看到實務範例、示範程式碼與部署策略，展現如何在 C#、Java 與 Spring、TypeScript、JavaScript 和 Python 中實作 MCP。你也將學習如何除錯和測試 MCP 伺服器，管理 API，並使用 Azure 部署解決方案。這些實作資源旨在加速你的學習，並幫助你自信地構建穩健且可投入生產的 MCP 應用程式。

## 概覽

本課程聚焦於多語言 MCP 實作的實務面。我們將探討如何使用 C#、Java 與 Spring、TypeScript、JavaScript 以及 Python 的 MCP SDK 來建立健全應用、除錯和測試 MCP 伺服器，以及創建可重用的資源、提示及工具。

## 學習目標

完成本課程後，你將能夠：

- 使用多種程式語言的官方 SDK 實現 MCP 解決方案
- 系統性除錯與測試 MCP 伺服器
- 創建並使用伺服器功能（資源、提示與工具）
- 設計有效的 MCP 工作流程來處理複雜任務
- 優化 MCP 實作以提升效能和可靠度

## 官方 SDK 資源

模型上下文協定提供多種語言的官方 SDK（對應 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java 與 Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **注意：** 需依賴 [Project Reactor](https://projectreactor.io)。（參見 [討論議題 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本節提供多種程式語言中實作 MCP 的實務範例，示範程式碼位於 `samples` 目錄中，按語言分類整理。

### 可用範例

此資源庫包含以下語言的 [示範實作](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java 與 Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例示範該語言及生態系統中關鍵 MCP 概念與實作模式。

### 實務指南

其他實務 MCP 實作指南：

- [分頁與大型結果集](./pagination/README.md) - 處理工具、資源及大型資料集的游標分頁

## 核心伺服器功能

MCP 伺服器可以實作下列任意組合的功能：

### 資源

資源為使用者或 AI 模型提供上下文及資料：

- 文件資料庫
- 知識庫
- 結構化資料源
- 檔案系統

### 提示

提示是用戶的模板化訊息與工作流程：

- 預定義對話模板
- 引導式互動模式
- 專門設計的對話結構

### 工具

工具是 AI 模型可執行的函式：

- 資料處理工具
- 外部 API 整合
- 運算能力
- 搜尋功能

## 範例實作：C# 實作

官方 C# SDK 資源庫包含多個示範實作，展現不同的 MCP 面向：

- **基本 MCP 用戶端**：簡單範例示範如何建立 MCP 用戶端並呼叫工具
- **基本 MCP 伺服器**：最小伺服器實作及基本工具註冊
- **高階 MCP 伺服器**：完整功能伺服器，含工具註冊、認證及錯誤處理
- **ASP.NET 整合**：示範與 ASP.NET Core 整合的範例
- **工具實作模式**：各式工具實作模式，涵蓋不同複雜度

MCP C# SDK 目前為預覽版，API 可能會有變動。我們將持續更新本部落格以跟進 SDK 發展。

### 主要功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 建立你的 [第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

完整的 C# 實作範例，請參見 [官方 C# SDK 範例資源庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java 與 Spring 實作

Java 與 Spring SDK 提供企業級功能的 MCP 堅實實作選項。

### 主要功能

- Spring Framework 整合
- 強型別安全
- 反應式程式設計支援
- 完整的錯誤處理

完整的 Java 與 Spring 實作範例，請參見範例目錄中的 [Java 與 Spring 範例](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且彈性的 MCP 實作方式。

### 主要功能

- 支援 Node.js 與瀏覽器環境
- 基於 Promise 的 API
- 易於整合 Express 及其他框架
- 支援 WebSocket 串流功能

完成的 JavaScript 實作範例，請見範例目錄中的 [JavaScript 範例](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 以 Pythonic 風格實作 MCP，並與主流機器學習框架整合良好。

### 主要功能

- 支援 asyncio 的 async/await
- FastAPI 整合
- 簡單的工具註冊
- 與流行機器學習函式庫的原生整合

完成的 Python 實作範例，請參見範例目錄中的 [Python 範例](samples/python/README.md)。

## API 管理

Azure API Management 是保護 MCP 伺服器的絕佳方案。基本想法是將 Azure API Management 實例置於 MCP 伺服器之前，由它處理常見需求，如：

- 流量限制
- 令牌管理
- 監控
- 負載平衡
- 安全

### Azure 範例

這裡有一個 Azure 範例，正是 [建立 MCP 伺服器並用 Azure API Management 保護之](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

下圖示範授權流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

圖中流程如下：

- 使用 Microsoft Entra 進行認證/授權。
- Azure API Management 作為閘道，透過政策管理與導向流量。
- Azure 監視器記錄所有請求以供後續分析。

#### 授權流程

來更詳細看看授權流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

深入瞭解 [MCP 授權規範](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## 部署遠端 MCP 伺服器到 Azure

讓我們試著部署之前提到的範例：

1. 克隆資料庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 資源提供者。

   - 如果使用 Azure CLI，執行 `az provider register --namespace Microsoft.App --wait`。
   - 如果使用 Azure PowerShell，執行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。之後稍等片刻再執行 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 以確認註冊狀態。

1. 執行此 [azd](https://aka.ms/azd) 指令以建立 API 管理服務、帶程式碼的 Function App 及所有其他必需的 Azure 資源

    ```shell
    azd up
    ```

    此指令將會在 Azure 上部署所有雲端資源

### 使用 MCP Inspector 測試你的伺服器

1. 在 **新終端機視窗**，安裝並執行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    你應該會看到與下圖相似的介面：

    ![Connect to Node inspector](../../../translated_images/zh-TW/connect.141db0b2bd05f096.webp)

1. CTRL 點擊以從應用顯示的 URL 載入 MCP Inspector 網頁應用（例如：[http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）
1. 將傳輸類型設為 `SSE`
1. 將 URL 設成在執行 `azd up` 後顯示的 API 管理 SSE 端點，然後 **Connect**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **列出工具**。點擊其中某個工具並 **執行工具**。

若全部步驟皆成功，你現在將連接至 MCP 伺服器並能呼叫工具。

## 適用於 Azure 的 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：這組資源庫是使用 Azure Functions（Python、C# .NET 或 Node/TypeScript）快速啟動並部署遠端 MCP（模型上下文協定）伺服器的範本。

此範例提供完整解決方案，方便開發者：

- 本地建置與執行：在本機開發並偵錯 MCP 伺服器
- 部署至 Azure：使用簡單 `azd up` 指令快速上雲部署
- 用戶端連線：從多種用戶端連接 MCP 伺服器，包括 VS Code 的 Copilot 代理模式和 MCP Inspector 工具

### 主要功能

- 安全設計：MCP 伺服器使用金鑰與 HTTPS 保障安全
- 身分驗證選項：支援內建認證與/或 API 管理的 OAuth
- 網路隔離：支援 Azure 虛擬網路 (VNET) 隔離
- 無伺服器架構：利用 Azure Functions 實現可擴展的事件驅動執行
- 本地開發：提供完整的本地開發與除錯支援
- 簡易部署：流暢快速的 Azure 部署流程

資源庫包含所有需要的設定檔、原始碼及基礎架構定義，助你快速上手並打造可投入生產的 MCP 伺服器實作。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 與 Python 實作 MCP 範例

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 與 C# .NET 實作 MCP 範例

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 與 Node/TypeScript 實作 MCP 範例。

## 主要重點

- MCP SDK 提供各語言專屬工具來實作健全的 MCP 解決方案
- 除錯與測試程序對可靠的 MCP 應用至關重要
- 可重用提示模板促進 AI 互動一致性
- 精心設計的工作流程能協調複雜任務和多重工具
- 實作 MCP 解決方案需兼顧安全、效能與錯誤處理

## 練習

設計一個實務 MCP 工作流程，解決你領域中的真實問題：

1. 確定 3-4 個適合解決此問題的工具
2. 繪製這些工具互動的工作流程圖
3. 使用你偏好的語言實作其中一個工具的基本版本
4. 創建一個提示模板，幫助模型有效使用你的工具

## 額外資源

---

## 下一步

下一篇： [進階主題](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯服務。因使用本翻譯所引起的任何誤解或誤釋，本公司概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
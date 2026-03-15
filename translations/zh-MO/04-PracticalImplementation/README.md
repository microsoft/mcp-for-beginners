# 實務實作

[![如何使用真實工具與工作流程建構、測試及部署 MCP 應用程式](../../../translated_images/zh-MO/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(點擊上方圖片觀看本課程影片)_

實務實作是模型上下文協議（Model Context Protocol, MCP）威力變得具體的地方。雖然理解 MCP 背後的理論與架構很重要，但真正的價值來自於您將這些概念應用於建構、測試及部署可解決實際問題的解決方案。本章將填補概念知識與實作開發之間的鴻溝，引導您完成將 MCP 應用程式打造出來的流程。

無論您是在開發智慧助理、將 AI 整合進企業工作流程，還是打造用於資料處理的客製化工具，MCP 都提供了彈性的基礎。它的語言無關設計以及針對熱門程式語言提供的官方 SDK，使得廣大開發者都能輕鬆使用。藉由利用這些 SDK，您可以快速原型設計、反覆迭代並跨不同平台與環境擴展您的解決方案。

在以下章節中，您將看到實務範例、範例程式碼與部署策略，示範如何在 C#、Java（Spring）、TypeScript、JavaScript 與 Python 中實作 MCP。您還會學會如何偵錯與測試 MCP 伺服器、管理 API，並使用 Azure 將方案部署至雲端。這些實作資源旨在加速您的學習，使您能夠自信地打造穩健、生產就緒的 MCP 應用程式。

## 概述

本課聚焦於跨多種程式語言的 MCP 實作實務面。我們將探討如何使用 C#、Java（Spring）、TypeScript、JavaScript 以及 Python 版 MCP SDK 來建構穩健的應用程式，偵錯與測試 MCP 伺服器，以及建立可重用的資源、提示與工具。

## 學習目標

完成本課後，您將能夠：

- 使用官方 SDK 在不同程式語言中實作 MCP 解決方案
- 系統性偵錯與測試 MCP 伺服器
- 創建並使用伺服器端功能（資源、提示及工具）
- 設計有效的 MCP 工作流程以完成複雜工作
- 為 MCP 實作優化效能與可靠性

## 官方 SDK 資源

模型上下文協議提供多種語言的官方 SDK（符合 [MCP 規格 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **注意：** 需依賴 [Project Reactor](https://projectreactor.io)。（請參考 [討論議題 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本節提供多種程式語言中 MCP 實作的實務範例。範例程式碼按語言組織在 `samples` 目錄中。

### 可用範例

本儲存庫包含以下語言的[範例實作](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例演示該語言及生態系中 MCP 重要概念和實作模式。

### 實務指南

其他 MCP 實作實務指南：

- [分頁及大型結果集](./pagination/README.md) - 處理工具、資源與大型資料集的游標分頁

## 核心伺服器功能

MCP 伺服器可實作以下任意組合功能：

### 資源

資源提供使用者或 AI 模型使用的上下文與資料：

- 文件庫
- 知識庫
- 結構化資料來源
- 檔案系統

### 提示

提示是用於使用者的範本訊息與工作流程：

- 預定義的對話範本
- 引導式互動模式
- 專門化對話結構

### 工具

工具為 AI 模型可執行的函式：

- 資料處理工具
- 外部 API 整合
- 計算能力
- 搜尋功能

## 範例實作：C# 實作

官方 C# SDK 的儲存庫包含多個示範 MCP 不同面向的範例：

- **基礎 MCP 客戶端**：簡易範例展示如何建立 MCP 客戶端並呼叫工具
- **基礎 MCP 伺服器**：基本工具註冊的最簡伺服器實作
- **進階 MCP 伺服器**：具完整功能的伺服器，包含工具註冊、驗證與錯誤處理
- **ASP.NET 整合**：展示與 ASP.NET Core 整合的範例
- **工具實作用法**：多種具不同複雜度的工具實作文法範例

MCP C# SDK 目前處於預覽階段，API 可能變動。我們會持續更新本部落格以追蹤 SDK 的演進。

### 主要功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 建立您的[第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)。

完整的 C# 實作範例請參閱[官方 C# SDK 範例儲存庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java with Spring 實作

Java with Spring SDK 提供企業級功能的強健 MCP 實作選項。

### 主要功能

- Spring Framework 整合
- 強型別安全
- 支援反應式程式設計
- 全面錯誤處理

完整的 Java with Spring 實作範例，請參閱 samples 目錄下的 [Java with Spring 範例](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且具彈性的 MCP 實作方式。

### 主要功能

- 支援 Node.js 與瀏覽器
- Promise 為基礎的 API
- 容易與 Express 及其他框架整合
- WebSocket 支援串流

完整的 JavaScript 實作範例，請參閱 samples 目錄下的 [JavaScript 範例](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 提供 Python 風格的 MCP 實作方法，並與優秀的機器學習框架整合良好。

### 主要功能

- 支援 asyncio 的 async/await
- FastAPI 整合
- 簡易的工具註冊
- 原生整合熱門機器學習函式庫

完整的 Python 實作範例，請參閱 samples 目錄下的 [Python 範例](samples/python/README.md)。

## API 管理

Azure API 管理是我們如何保護 MCP 伺服器的絕佳解決方案。其概念是將 Azure API 管理實例置於 MCP 伺服器前端，並讓它處理您可能需要的功能，例如：

- 限流
- 令牌管理
- 監控
- 負載平衡
- 安全性

### Azure 範例

以下為一個 Azure 範例，即[建立 MCP 伺服器並以 Azure API 管理保護它](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

下圖展示授權流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

圖中包含以下步驟：

- 使用 Microsoft Entra 進行身份驗證及授權。
- Azure API 管理作為閘道，使用政策指導及管理流量。
- Azure 監控記錄所有請求以供進一步分析。

#### 授權流程

我們更詳細地來看授權流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

了解更多關於 [MCP 授權規範](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## 部署遠端 MCP 伺服器至 Azure

我們來看看是否能部署之前提到的範例：

1. 克隆儲存庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 資源提供者。

   - 若您使用 Azure CLI，執行 `az provider register --namespace Microsoft.App --wait`。
   - 若您使用 Azure PowerShell，執行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。稍待片刻後執行 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 以確認註冊完成。

1. 執行此 [azd](https://aka.ms/azd) 命令來佈建 API 管理服務、包含程式碼的函式應用程式及所有其他需用的 Azure 資源

    ```shell
    azd up
    ```

    此命令會在 Azure 上部署所有雲端資源

### 使用 MCP Inspector 測試您的伺服器

1. 在 **新終端視窗** 中，安裝並執行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    您應該會看到類似的介面：

    ![Connect to Node inspector](../../../translated_images/zh-MO/connect.141db0b2bd05f096.webp)

1. 按住 CTRL 點擊以從程式顯示的網址載入 MCP Inspector 網頁應用程式（例如 [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）
1. 將傳輸類型設為 `SSE`
1. 設定 URL 為您執行中 API 管理 SSE 端點（由 `azd up` 執行結果顯示），並按【連線】：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. 【列出工具】。點選任一工具並【執行工具】。

若上述步驟皆正確，您現在應已連線至 MCP 伺服器，並成功呼叫一個工具。

## 適用於 Azure 的 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：此系列儲存庫為使用 Azure Functions 搭配 Python、C# .NET 或 Node/TypeScript 快速建立及部署自訂遠端 MCP（模型上下文協議）伺服器的範本。

該範例提供完整方案，使開發者能：

- 本地建置與執行：在本機開發及偵錯 MCP 伺服器
- 部署至 Azure：以簡單的 azd up 命令輕鬆將服務部署至雲端
- 從用戶端連線：讓各種用戶端，包括 VS Code 的 Copilot 代理模式及 MCP Inspector 工具，都能連線至 MCP 伺服器

### 主要功能

- 安全性由設計開始：MCP 伺服器使用金鑰及 HTTPS 保護
- 驗證選擇：支援使用內建授權和／或 API 管理的 OAuth
- 網路隔離：透過 Azure 虛擬網路（VNET）實現網路隔離
- 無伺服器架構：利用 Azure Functions 實現可擴展的事件驅動執行
- 本地開發：完整的本地開發與偵錯支援
- 簡易部署：簡化的 Azure 部署流程

儲存庫包含所有必要設定檔、原始碼及基礎建設定義，幫助您快速啟動具生產就緒能力的 MCP 伺服器實作。

- [Azure 遠端 MCP 函式 Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 與 Python 的 MCP 範例實作

- [Azure 遠端 MCP 函式 .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 與 C# .NET 的 MCP 範例實作

- [Azure 遠端 MCP 函式 Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 與 Node/TypeScript 的 MCP 範例實作

## 重要摘要

- MCP SDK 提供語言特定工具以實作健全的 MCP 解決方案
- 偵錯及測試過程對穩定的 MCP 應用至關重要
- 可重用提示範本助力一致性的 AI 互動
- 良好設計的工作流程可協調多工具完成複雜任務
- 實作 MCP 解決方案需兼顧安全性、效能及錯誤處理

## 練習

設計一個實務的 MCP 工作流程，解決您領域中的真實問題：

1. 確認 3-4 個適合用來解決此問題的工具
2. 繪製工作流程圖，展示這些工具如何互動
3. 使用您偏好的程式語言實作其中一個工具的基本版本
4. 建立一個提示範本，協助模型有效運用您的工具

## 額外資源

---

## 下一步

下一章：[進階主題](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。儘管我們致力於確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議聘請專業人工翻譯。本服務對因使用本翻譯而引起的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
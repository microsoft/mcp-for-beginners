# 實務實作

[![如何使用真正的工具與工作流程構建、測試及部署 MCP 應用程式](../../../translated_images/zh-HK/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(點擊上方圖片觀看本課程影片)_

實務實作是使模型語境協議（MCP）威力具體化的關鍵。理解 MCP 的理論與架構固然重要，但真正的價值是在應用這些概念來建置、測試與部署解決方案，以解決真實世界問題時展現出來。本章節銜接概念知識與實作開發，帶領你完成基於 MCP 的應用程式實現流程。

無論你是在開發智慧助理、將 AI 整合進商業工作流程，或建立用於資料處理的自訂工具，MCP 都提供靈活的基礎。它的語言無關設計，以及為常用程式語言提供的官方 SDK，使它對廣大開發者都能輕易使用。透過這些 SDK，你可以快速建立原型、反覆優化，並擴展解決方案，在不同平台與環境間靈活運用。

接下來的章節裡，你將看到實用範例、示範程式碼，還有部署策略，展示如何在 C#、Java (Spring)、TypeScript、JavaScript 和 Python 中實現 MCP。你也會學習如何偵錯與測試 MCP 伺服器、管理 API，以及使用 Azure 將解決方案部署到雲端。這些實作資源旨在加速你的學習，幫助你自信地建立穩健、可投入生產的 MCP 應用程式。

## 概覽

本課程聚焦於跨多種程式語言的 MCP 實務實作面向。我們將探討如何在 C#、Java (Spring)、TypeScript、JavaScript 和 Python 中使用 MCP SDK 建立強健應用程式，並對 MCP 伺服器進行偵錯和測試，創建可重用的資源、提示語與工具。

## 學習目標

完成本課程後，你將能：

- 使用官方 SDK 以不同程式語言實作 MCP 解決方案
- 系統化偵錯及測試 MCP 伺服器
- 建立並使用伺服器功能（資源、提示與工具）
- 為複雜任務設計有效的 MCP 工作流程
- 為效能與可靠性優化 MCP 的實作

## 官方 SDK 資源

模型語境協議提供多種語言的官方 SDK（符合 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java (Spring) SDK](https://github.com/modelcontextprotocol/java-sdk) **注意:** 需依賴 [Project Reactor](https://projectreactor.io)。（詳見 [討論議題 246](https://github.com/orgs/modelcontextprotocol/discussions/246)。）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## 使用 MCP SDK

本節提供跨多種程式語言實作 MCP 的實務範例。你可以在 `samples` 目錄中找到依語言分類的範例程式碼。

### 可用範例

本倉庫包含下列語言的 [範例實作](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java (Spring)](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例都展示該語言生態圈中 MCP 的核心概念與實作模式。

### 實務指南

其他 MCP 實務實作指導：

- [分頁與大量結果集處理](./pagination/README.md) - 用於工具、資源與大型資料集的基於游標分頁處理。

## 核心伺服器功能

MCP 伺服器可實作以下任意組合的功能：

### 資源

資源提供用戶或 AI 模型可導入的上下文與資料：

- 文件庫
- 知識庫
- 結構化資料源
- 檔案系統

### 提示

提示是面向使用者的模板訊息與工作流程：

- 預設會話模板
- 引導互動模式
- 專門化的對話結構

### 工具

工具是 AI 模型可執行的函式：

- 資料處理工具
- 外部 API 整合
- 計算功能
- 搜尋功能

## 範例實作：C# 實作

官方 C# SDK 倉庫包含數個示範不同 MCP 面向的範例實作：

- **基本 MCP 用戶端**：示範如何建立 MCP 用戶端並呼叫工具的簡單範例
- **基本 MCP 伺服器**：具基礎工具註冊的最簡服務器實作
- **進階 MCP 伺服器**：具工具註冊、認證和錯誤處理之完整功能的服務器
- **ASP.NET 整合**：示範如何與 ASP.NET Core 整合的範例
- **工具實作模式**：不同複雜度工具的各種實作模式

C# MCP SDK 正處於預覽階段，API 可能會變動。我們將持續更新此部落格內容。

### 主要功能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- 建立你的 [第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)。

欲取得完整 C# 實作範例，請參閱 [官方 C# SDK 範例倉庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java (Spring) 實作

Java (Spring) SDK 提供企業級強大 MCP 實作功能。

### 主要功能

- Spring Framework 整合
- 強型別安全
- 支援反應式編程
- 完整錯誤處理

完整的 Java (Spring) 實作範例請見 samples 目錄下的 [Java with Spring 範例](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且靈活的 MCP 實作途徑。

### 主要功能

- 支援 Node.js 與瀏覽器
- Promise 風格 API
- 容易與 Express 及其他框架整合
- 支援 WebSocket 流式傳輸

完整的 JavaScript 實作範例請見 samples 目錄下的 [JavaScript 範例](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 以 Pythonic 方式呈現 MCP 實作，並具優秀的機器學習框架整合。

### 主要功能

- 支援 asyncio 的 async/await
- FastAPI 整合
- 簡便的工具註冊
- 原生整合多個熱門機器學習函式庫

完整的 Python 實作範例請見 samples 目錄下的 [Python 範例](samples/python/README.md)。

## API 管理

Azure API 管理是保障 MCP 伺服器安全的良方。其概念是在 MCP 伺服器前端設置一個 Azure API 管理實例，讓其處理你可能需要的功能，包括：

- 流量限制
- 令牌管理
- 監控
- 負載平衡
- 安全性

### Azure 範例

這裡有一個 Azure 範例，做的正是這件事，也就是 [建立 MCP 伺服器並使用 Azure API 管理進行安全防護](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

下圖展示授權流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

在上圖中發生的過程：

- 驗證與授權透過 Microsoft Entra 進行。
- Azure API 管理扮演閘道角色，利用政策導向及管理流量。
- Azure Monitor 記錄所有請求，供後續分析使用。

#### 授權流程詳解

讓我們詳細看看授權流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

瞭解更多關於 [MCP 授權規範](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## 部署遠端 MCP 伺服器到 Azure

現在來看看如何部署先前提到的範例：

1. 複製倉庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 資源提供者。

   - 若使用 Azure CLI，執行 `az provider register --namespace Microsoft.App --wait`。
   - 若使用 Azure PowerShell，執行 `Register-AzResourceProvider -ProviderNamespace Microsoft.App`。完成後稍等，再執行 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 確認註冊狀態。

1. 執行此 [azd](https://aka.ms/azd) 指令來佈署 API 管理服務、函數應用程式（含程式碼）與所有其他必要 Azure 資源

    ```shell
    azd up
    ```

    此指令將在 Azure 上部署所有雲端資源

### 使用 MCP Inspector 測試你的伺服器

1. 在 **新終端機視窗** 內安裝並運行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    你應會看到類似以下介面：

    ![Connect to Node inspector](../../../translated_images/zh-HK/connect.141db0b2bd05f096.webp)

1. Ctrl 點擊來載入 MCP Inspector 網頁應用程式，網址由應用程式顯示（例如 [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）
1. 將傳輸類型設為 `SSE`
1. 將 URL 設為 `azd up` 後顯示的運行中 API 管理 SSE 端點，點選 **連線**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **列出工具清單**。點選一個工具並 **執行工具**。

若以上步驟順利，你應已成功連接 MCP 伺服器並能呼叫工具。

## Azure 的 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：這組倉庫提供快速上手的範本，協助使用 Azure Functions 以 Python、C# .NET 或 Node/TypeScript 建構與部署自訂遠端 MCP（模型語境協議）伺服器。

這些範例提供完整解決方案，讓開發者可以：

- 本地建置與執行：在本機端開發並偵錯 MCP 伺服器
- 部署到 Azure：透過簡單的 azd up 指令迅速上傳雲端
- 從用戶端連線：可從多種用戶端連接 MCP 伺服器，包括 VS Code Copilot 代理模式與 MCP Inspector 工具

### 主要功能

- 以安全設計為先：MCP 伺服器使用金鑰與 HTTPS 保護
- 認證選項：支援使用內建驗證與/或 API 管理的 OAuth
- 網路隔離：支援使用 Azure 虛擬網路（VNET）隔離網路
- 無伺服器架構：利用 Azure 函數以實現可擴展的事件驅動執行
- 本地開發：完整的本地開發與偵錯支持
- 簡易部署：流暢的 Azure 部署流程

倉庫含所有必要的設定檔、原始碼與基礎設施定義，幫助你快速啟動生產等級的 MCP 伺服器實作。

- [Azure 遠端 MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 及 Python 的 MCP 範例實作

- [Azure 遠端 MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 及 C# .NET 的 MCP 範例實作

- [Azure 遠端 MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 及 Node/TypeScript 的 MCP 範例實作

## 重要重點整理

- MCP SDK 提供針對語言的工具來實作健全的 MCP 解決方案
- 偵錯與測試過程是確保 MCP 應用可靠性的關鍵
- 可重用的提示模板確保 AI 互動的一致性
- 良好設計的工作流程可協調多個工具完成複雜任務
- 建置 MCP 解決方案須考量安全性、效能與錯誤處理

## 練習

設計一個符合你領域真實需求的 MCP 工作流程：

1. 挑選 3-4 個有助於解決此問題的工具
2. 繪製工作流程圖，展示這些工具的互動方式
3. 使用你偏好的語言實作其中一個工具的基礎版本
4. 建立能幫助模型有效使用你工具的提示模板

## 額外資源

---

## 下一步

下一章： [進階主題](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
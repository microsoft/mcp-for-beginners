# 🚀 10 個正在改變開發者生產力的 Microsoft MCP 伺服器

## 🎯 你會在本指南學到什麼

本實用指南展示了十個正在積極改變開發者使用 AI 助手工作的 Microsoft MCP 伺服器。我們不僅僅說明 MCP 伺服器<em>可以</em>做什麼，而是展示目前正在真實改變 Microsoft 及其他地方日常開發工作流程的伺服器。

本指南中的每個伺服器都基於真實世界的使用情況和開發者反饋被挑選。你不僅會了解每個伺服器的功能，還會明白它為何重要，以及如何在你的專案中充分利用。無論你是 MCP 新手，還是希望擴展現有設置，這些伺服器代表 Microsoft 生態系統中一些最實用且有影響力的工具。

> **💡 快速入門小貼士**
>
> MCP 新手嗎？別擔心！本指南設計為初學者友好。我們會邊講概念邊進行，而且你隨時可以回顧我們的 [MCP 介紹](../00-Introduction/README.md) 和 [核心概念](../01-CoreConcepts/README.md) 模組以加深背景知識。

## 概覽

本全面指南探討十個 Microsoft MCP 伺服器，它們正在革新開發者與 AI 助理和外部工具互動的方式。從 Azure 資源管理到文件處理，這些伺服器展示了模型上下文協定如何創建無縫且高效的開發流程。

## 學習目標

完成本指南後，你將會：
- 了解 MCP 伺服器如何提升開發者生產力
- 學習 Microsoft 最具影響力的 MCP 伺服器實作
- 探索每個伺服器的實用案例
- 知道如何在 VS Code 和 Visual Studio 中設置和配置這些伺服器
- 探索更廣泛的 MCP 生態系統與未來方向

## 🔧 了解 MCP 伺服器：初學者指南

### 什麼是 MCP 伺服器？

作為模型上下文協定（MCP）的初學者，你可能會好奇：「MCP 伺服器究竟是什麼，為何我應該關注？」我們先用一個簡單的比喻開始。

可以把 MCP 伺服器當作專門助手，幫助你的 AI 程式編寫夥伴（如 GitHub Copilot）連接到外部工具和服務。就像你可能會用手機上不同的應用程式處理不同的任務—一個是天氣、一個是導航、一個是銀行服務—MCP 伺服器賦予你的 AI 助理與不同開發工具和服務互動的能力。

### MCP 伺服器解決的問題

在 MCP 伺服器之前，如果你想要：
- 查看你的 Azure 資源
- 建立 GitHub Issue
- 查詢你的資料庫
- 搜尋文件

你必須停止編碼，打開瀏覽器，前往相關網站並手動執行這些任務。頻繁切換工作上下文會打斷你的工作節奏並降低生產力。

### MCP 伺服器如何改變你的開發體驗

使用 MCP 伺服器，你可以留在開發環境中（VS Code、Visual Studio 等），直接請 AI 助理處理這些任務。例如：

**傳統流程是：**
1. 停止編碼
2. 開啟瀏覽器
3. 前往 Azure 入口網站
4. 查找儲存帳戶細節
5. 回到 VS Code
6. 繼續編碼

**現在你可以這麼做：**
1. 問 AI：「我的 Azure 儲存帳戶狀態如何？」
2. 使用得到的資訊繼續編碼

### 初學者的主要益處

#### 1. 🔄 <strong>保持你的心流狀態</strong>
- 不需再在多個應用程式間切換
- 專注於你正在編寫的程式碼
- 降低管理不同工具的心理負擔

#### 2. 🤖 <strong>使用自然語言代替複雜指令</strong>
- 不需背 SQL 語法，只要描述你需要的數據
- 不用記 Azure CLI 指令，只要說明你想達成的目標
- 讓 AI 處理技術細節，你專注邏輯

#### 3. 🔗 <strong>將多個工具連接起來</strong>
- 透過結合不同服務建立強大工作流程
- 例如：「取得所有近期 GitHub Issue 並建立對應 Azure DevOps 工作項目」
- 建造自動化而不用寫複雜腳本

#### 4. 🌐 <strong>接觸日益成長的生態系統</strong>
- 從 Microsoft、GitHub 及其他公司提供的伺服器中受益
- 無縫混合不同供應商的工具
- 加入一個跨不同 AI 助理都通用的標準化生態系統

#### 5. 🛠️ <strong>實作中學習</strong>
- 從預建伺服器開始理解概念
- 逐步建立自己的伺服器，隨著熟悉度提升
- 使用現有 SDK 和文檔引導學習

### 初學者的真實案例

假設你是網頁開發新手，正在進行你的第一個專案。MCP 伺服器能這樣幫你：

**傳統方式：**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**使用 MCP 伺服器：**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### 企業標準優勢

MCP 正逐漸成為業界標準，代表：
- <strong>一致性</strong>：不同工具和公司間體驗相近
- <strong>互通性</strong>：不同供應商的伺服器能協同工作
- <strong>未來兼容</strong>：技能與設置在不同 AI 助理間可轉移
- <strong>社群力量</strong>：龐大的知識與資源共享生態

### 開始之前：你會學到什麼

本指南將探索 10 個對所有級別開發人員都特別有用的 Microsoft MCP 伺服器。每個伺服器設計目標為：
- 解決常見開發挑戰
- 減少重複工作
- 提升程式碼品質
- 加強學習機會

> **💡 學習小貼士**
>
> 如果你完全是 MCP 新手，建議先學習我們的 [MCP 介紹](../00-Introduction/README.md) 和 [核心概念](../01-CoreConcepts/README.md) 模組。然後再回來這裡看看這些概念如何在真實 Microsoft 工具中實作。
>
> 想了解更多 MCP 重要性，請參考 Maria Naggaga 的文章：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## 在 VS Code 和 Visual Studio 開始使用 MCP 🚀

如果你正在使用 Visual Studio Code 或搭配 GitHub Copilot 的 Visual Studio 2022，設定這些 MCP 伺服器很簡單。

### VS Code 設定

VS Code 的基本流程如下：

1. **啟用代理模式（Agent Mode）**：在 VS Code 中，切換到 Copilot Chat 視窗的代理模式
2. **配置 MCP 伺服器**：將伺服器設定新增至 VS Code 的 settings.json
3. <strong>啟動伺服器</strong>：點擊你想使用的每個伺服器旁的「啟動」按鈕
4. <strong>選擇工具</strong>：選擇本次會話要啟用的 MCP 伺服器

詳細設定說明，請參考 [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)。

> **💡 進階技巧：專業管理 MCP 伺服器！**
>
> VS Code 擴充功能檢視中新增了[方便的 UI 來管理已安裝的 MCP 伺服器](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)！你可以快速啟動、停止和管理任何已安裝的 MCP 伺服器，介面明確簡單。快試試看！

### Visual Studio 2022 設定

對於 Visual Studio 2022（17.14 版本或更新）：

1. <strong>啟用代理模式</strong>：點擊 GitHub Copilot Chat 視窗的「Ask」下拉選單並選擇「代理（Agent）」
2. <strong>建立設定檔</strong>：於專案目錄中建立 `.mcp.json` 檔案（建議位置：`<SOLUTIONDIR>\.mcp.json`）
3. <strong>配置伺服器</strong>：使用標準 MCP 格式新增你的 MCP 伺服器設定
4. <strong>工具授權</strong>：系統提示時，批准你想使用的工具及對應範圍許可權

詳細 Visual Studio 設定指導，請見 [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)。

每個 MCP 伺服器有其特定配置需求（連接字串、驗證等），但兩個 IDE 的設定模式一致。

## 從 Microsoft MCP 伺服器中學到的課程 🛠️

### 1. 📚 Microsoft Learn Docs MCP 伺服器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>功能說明</strong>：Microsoft Learn Docs MCP 伺服器是一個雲端服務，透過模型上下文協定，提供 AI 助理即時存取 Microsoft 官方文件的能力。它連接至 `https://learn.microsoft.com/api/mcp`，可對 Microsoft Learn、Azure 文件、Microsoft 365 文件及其他官方 Microsoft 資源進行語意搜尋。

<strong>為何有用</strong>：雖然這看似「只是文件」，但對任何使用 Microsoft 技術的開發者來說，這伺服器非常關鍵。許多 .NET 開發者對 AI 編碼助手最大的抱怨是它們的資料未及時更新於最新的 .NET 和 C# 發布。Microsoft Learn Docs MCP 伺服器透過提供最新文件、API 參考與最佳實踐的即時存取，解決此問題。無論你是使用最新的 Azure SDK、探索新 C# 13 功能，或實作領先的 Aspire 模式，這伺服器確保你的 AI 助理取得權威且最新資訊，產生準確又現代的程式碼。

<strong>真實應用</strong>：「根據 Microsoft Learn 官方文件，az cli 指令如何建立 Azure container app?」或者「如何在 ASP.NET Core 中用依賴注入配置 Entity Framework?」或是「檢視這段程式碼是否符合 Microsoft Learn 文件中效能建議？」該伺服器透過先進語意搜尋完善覆蓋 Microsoft Learn、Azure 文件與 Microsoft 365 文件，找到最具上下文相關性的資訊，回傳最多 10 段高質量內容，包含文章標題與連結，時刻存取最新文件。

<strong>特色範例</strong>：伺服器公開 `microsoft_docs_search` 工具，可以對 Microsoft 官方技術文件執行語意搜尋。配置後，你可以問「如何在 ASP.NET Core 中實作 JWT 驗證？」並獲得詳細官方回答與來源連結。搜尋品質極佳，因它能理解上下文——在 Azure 的語境下詢問「containers」，搜尋結果為 Azure Container Instances 文件；在 .NET 語境中同詞則返回相關 C# 集合資訊。

這對於快速變化或最近更新的函式庫及用例尤其有用。舉例來說，在某些近期編碼專案中，我想利用 Aspire 和 Microsoft.Extensions.AI 的最新版本功能。加入 Microsoft Learn Docs MCP 伺服器後，我不只取得 API 文件，還得到剛發表的示範及引導。

> **💡 進階技巧**
>
> 即使是友善工具的模型也需要引導使用 MCP 工具！可考慮加入系統提示或[copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) 如：「你有權使用 `microsoft.docs.mcp` —— 當處理 C#、Azure、ASP.NET Core 或 Entity Framework 等 Microsoft 技術相關問題時，使用此工具搜尋 Microsoft 最新官方文件。」
>
> 想看真實範例，請參考 Awesome GitHub Copilot 儲存庫中的 [C# .NET Janitor 聊天模式](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)。此模式特別利用 Microsoft Learn Docs MCP 伺服器，協助清理與現代化 C# 程式碼，採用最新模式與最佳實踐。
### 2. ☁️ Azure MCP 伺服器


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>功能簡介</strong>：Azure MCP Server 是一套包含超過 15 種專業 Azure 服務連接器的完整套件，將整個 Azure 生態系統帶入您的 AI 工作流程。它不僅僅是一台伺服器 — 它是一個強大的集合，包括資源管理、資料庫連接（PostgreSQL、SQL Server）、利用 KQL 的 Azure Monitor 日誌分析、Cosmos DB 整合，以及更多功能。

<strong>有何用處</strong>：除了單純管理 Azure 資源，這個伺服器在使用 Azure SDK 開發時大幅提升代碼品質。當您以 Agent 模式使用 Azure MCP，它不只是幫助您編寫代碼 —— 它為您生成符合目前身份驗證模式、錯誤處理最佳實踐及利用最新 SDK 功能的更佳 Azure 代碼。您不會得到只會運作的通用代碼，而是符合 Azure 生產工作負載推薦模式的代碼。

<strong>主要模組包括</strong>：
- **🗄️ 資料庫連接器**：直接以自然語言存取 Azure Database for PostgreSQL 及 SQL Server
- **📊 Azure Monitor**：基於 KQL 的日誌分析與運營洞察
- **🌐 資源管理**：完整的 Azure 資源生命週期管理
- **🔐 身份驗證**：DefaultAzureCredential 及受管身份識別模式
- **📦 儲存服務**：Blob Storage、Queue Storage 和 Table Storage 操作
- **🚀 容器服務**：Azure Container Apps、Container Instances 和 AKS 管理
- <strong>以及更多專門連接器</strong>

<strong>實際應用範例</strong>：「列出我的 Azure 儲存帳戶」、「查詢我 Log Analytics 工作區過去一小時內的錯誤」、或「協助我用 Node.js 建立帶正確身份驗證的 Azure 應用程式」

<strong>完整示範場景</strong>：這裡展示一個完整流程，演示如何結合 Azure MCP 與 VS Code 中的 GitHub Copilot for Azure 擴充功能。當兩者安裝完成並提示：

> 「建立一個 Python 腳本，使用 DefaultAzureCredential 身份驗證上傳檔案至 Azure Blob Storage。腳本需連接名為 'mycompanystorage' 的 Azure 儲存帳戶，上傳至名為 'documents' 的容器，建立包含當前時間戳的測試檔案供上傳，優雅處理錯誤並提供資訊性輸出，遵循 Azure 身份驗證和錯誤處理最佳實踐，註解解釋 DefaultAzureCredential 的身份驗證工作原理，並以良好結構和適當函數與文件撰寫腳本。」

Azure MCP Server 將產生完整、適合生產環境的 Python 腳本，該腳本：
- 使用最新的 Azure Blob Storage SDK 並符合適當的非同步模式
- 實現 DefaultAzureCredential 並提供完整備援鏈說明
- 包含針對特定 Azure 例外類型的穩健錯誤處理
- 遵循 Azure SDK 關於資源管理與連線管理的最佳實踐
- 提供詳細日誌與具資訊性的主控台輸出
- 建立結構良好的腳本，包含函數、文件說明與型別提示

有趣的是，沒有 Azure MCP，您可能會得到僅能運作但不符合最新 Azure 標準的 Blob Storage 代碼；使用 Azure MCP，您將得到利用最新身份驗證技術、處理 Azure 特定錯誤場景且遵循微軟推薦生產應用程式模式的代碼。

<strong>特色範例</strong>：我經常忘記 `az` 和 `azd` CLI 的特定命令，通常都是兩步：先查語法，再執行命令。我時常直接進 Portal 點擊操作，因為不願承認自己記不住命令。能用自然語言描述需求真的很棒，更棒的是能直接在 IDE 裡面完成！

在 [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) 有一份很棒的用例清單可以協助您入門。想要完整設定指引及進階配置選項，請參考 [官方 Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)。

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

<strong>功能簡介</strong>：官方 GitHub MCP Server 提供與 GitHub 整個生態系統的無縫整合，支援遠端託管存取及本地 Docker 部署選項。這不只是基本的倉庫操作 — 它是一套完整工具組，包括 GitHub Actions 管理、拉取請求工作流、議題追蹤、安全掃描、通知及進階自動化能力。

<strong>有何用處</strong>：這個伺服器改變了您與 GitHub 的互動方式，將完整平台體驗直接帶入您的開發環境。您不必不停切換 VS Code 與 GitHub.com 進行專案管理、程式碼審查和 CI/CD 監控，只需用自然語言指令即可在專注代碼時管理一切。

> **ℹ️ 備註：不同類型的「代理人」**
> 
> 不要將這個 GitHub MCP Server 和 GitHub 的 Coding Agent（指派議題自動執行編碼任務的 AI 代理人）混淆。GitHub MCP Server 在 VS Code 的 Agent 模式中運作，提供 GitHub API 整合；Coding Agent 是另一項功能，指派至 GitHub 議題時會建立拉取請求。

<strong>主要功能包括</strong>：
- **⚙️ GitHub Actions**：完整 CI/CD 管管道管理、工作流監控及工件處理
- **🔀 拉取請求**：建立、審查、合併及全面狀態追蹤的 PR 管理
- **🐛 議題**：完整的議題生命週期管理、留言、標籤與指派
- **🔒 安全**：程式碼掃描警示、密碼檢測及 Dependabot 整合
- **🔔 通知**：智慧通知管理及倉庫訂閱控制
- **📁 倉庫管理**：檔案操作、分支管理及倉庫管理
- **👥 協作**：使用者與組織搜尋、團隊管理及存取控制

<strong>實際應用範例</strong>：「從我的功能分支建立拉取請求」、「列出本週所有失敗的 CI 執行」、「顯示我倉庫的所有開啟安全警報」、或「查找所有指派給我的跨組織議題」

<strong>完整示範場景</strong>：這裡是一個強力流程，展示 GitHub MCP Server 的能力：

> 「我要為我們的 sprint 檢視做準備。請顯示我本週建立的所有拉取請求，檢查我們 CI/CD 管道的狀態，整理我們需處理的安全警示摘要，並根據帶有 'feature' 標籤的合併 PR 協助我撰寫發佈註記。」

GitHub MCP Server 將：
- 查詢您的近期拉取請求並呈現詳細狀態資訊
- 分析工作流執行並標記任何失敗或效能問題
- 編輯安全掃描結果並優先處理關鍵警示
- 從已合併 PR 中提取資訊生成全面發佈註記
- 提供 sprint 規劃與發佈準備的可行後續步驟

<strong>特色範例</strong>：我喜歡用這個來處理程式碼審查工作流。不用跳來跳去於 VS Code、GitHub 通知和拉取請求頁面，只要說「顯示所有等我審查的 PR」，然後「在 PR #123 中留言，詢問身份驗證方法的錯誤處理」，伺服器會處理 GitHub API 呼叫、維持討論上下文，甚至能協助我撰寫更具建設性的審查評論。

<strong>身份驗證選項</strong>：伺服器支援 OAuth（在 VS Code 中無縫）及個人存取令牌，提供可配置工具集，只啟用您所需的 GitHub 功能。您可以選擇以遠端託管服務快速設定，或透過 Docker 本機運行以取得完全控制權。

> **💡 專家提示**
> 
> 透過在 MCP 伺服器設定中配置 `--toolsets` 參數，只啟用您需要的工具集，以減少上下文大小並優化 AI 工具選擇。例如，針對核心開發工作流，可加入 `"--toolsets", "repos,issues,pull_requests,actions"`，如果主要想要 GitHub 監控功能，則使用 `"--toolsets", "notifications, security"`。
### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

<strong>功能簡介</strong>：連線至 Azure DevOps 服務，提供全面的專案管理、工作項目追蹤、建置管線管理及倉庫操作功能。

<strong>有何用處</strong>：對於以 Azure DevOps 作為主要 DevOps 平台的團隊，這個 MCP 伺服器消除了在開發環境與 Azure DevOps 網頁介面間頻繁切換的需求。您可以直接從 AI 助理管理工作項目、查詢建置狀態、查詢倉庫並處理專案管理任務。

<strong>實際應用範例</strong>：「顯示 WebApp 專案本次衝刺中所有活躍工作項目」、「為我剛發現的登入問題建立錯誤回報」、或「檢查我們建置管線狀態並顯示最近任何失敗」

<strong>特色範例</strong>：您可以簡單查詢團隊當前衝刺的狀態，例如「顯示 WebApp 專案本次衝刺所有活躍工作項目」或「為我剛發現的登入問題建立錯誤回報」，而不必離開開發環境。

### 5. 📝 MarkItDown MCP Server


[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

<strong>功能說明</strong>: MarkItDown 是一個綜合文件轉換伺服器，可以將多種檔案格式轉換成高品質 Markdown，並針對大型語言模型（LLM）使用和文本分析工作流程進行優化。

<strong>為何實用</strong>: 現代文件處理工作流程的必備工具！MarkItDown 支援多種檔案格式，同時保留重要的文件結構，如標題、清單、表格及連結。與簡單的文字擷取工具不同，它注重維持語義意義和格式，對於 AI 處理和人類閱讀皆具價值。

<strong>支援的檔案格式</strong>：
- **Office 文件**：PDF、PowerPoint (PPTX)、Word (DOCX)、Excel (XLSX/XLS)
- <strong>媒體檔案</strong>：影像（含 EXIF 元數據與 OCR）、音訊（含 EXIF 元數據與語音轉錄）
- <strong>網頁內容</strong>：HTML、RSS 資訊源、YouTube 連結、維基百科頁面
- <strong>資料格式</strong>：CSV、JSON、XML、ZIP 檔案（遞迴處理內容）
- <strong>出版格式</strong>：EPub、Jupyter 筆記本（.ipynb）
- <strong>電子郵件</strong>：Outlook 郵件（.msg）
- <strong>進階功能</strong>：整合 Azure Document Intelligence，強化 PDF 處理

<strong>進階功能</strong>：MarkItDown 支援透過 OpenAI 客戶端提供的 LLM 驅動影像描述，Azure Document Intelligence 強化 PDF 處理，音訊轉錄語音內容，以及可擴充至更多檔案格式的插件系統。

<strong>實際應用</strong>：將此 PowerPoint 投影片轉為 Markdown 以用於文件站，從此 PDF 擷取文字並保持正確標題結構，或是將此 Excel 試算表轉成可讀的表格格式。

<strong>展示範例</strong>：引用 [MarkItDown 文件](https://github.com/microsoft/markitdown#why-markdown)：

> Markdown 非常接近純文字，標記和格式極少，但提供方式表達重要文件結構。主流大型語言模型，如 OpenAI 的 GPT-4o，本地「使用」Markdown，且常無需提示便將其整合在回應中。這顯示它們已在大量 Markdown 格式文本上訓練並極其熟悉。附帶好處為 Markdown 的標記非常節省標記字元。

MarkItDown 非常善於保留文件結構，對 AI 工作流程尤為重要。舉例而言，轉換 PowerPoint 演示文稿時，它保持投影片組織與正確標題，將表格擷取成 Markdown 表格，包含圖片的替代文字，甚至處理講者備註。圖表轉換為可讀的數據表格，產出的 Markdown 保持原始簡報的邏輯流程，完美用於將簡報內容輸入 AI 系統或從已有投影片創建文件。
### 6. 🗃️ SQL Server MCP 伺服器

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>功能說明</strong>: 提供對 SQL Server 資料庫（本機、Azure SQL 或 Fabric）的對話式存取

<strong>為何實用</strong>: 類似 PostgreSQL 伺服器，但專為 Microsoft SQL 生態系設計。透過簡單連線字串即可開始以自然語言查詢，不必切換上下文！

<strong>實際應用</strong>: 「找出過去 30 天未完成的所有訂單」會轉成適當的 SQL 查詢並回傳格式化結果

<strong>展示範例</strong>：一旦設置好資料庫連線，你就能立即和資料進行對話。部落格文章以簡單問題展示：「你連接的是哪個資料庫？」MCP 伺服器會調用相應的資料庫工具，連接你的 SQL Server 執行個體，並返回有關當前資料庫連線的詳細資訊——全程不需撰寫一行 SQL。伺服器支援從結構管理到資料操作的完整資料庫功能，皆可透過自然語言指令操作。詳細設置說明和 VS Code 與 Claude Desktop 的配置示例，請參閱：[介紹 MSSQL MCP 伺服器（預覽）](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)。


### 7. 🎭 Playwright MCP 伺服器

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

<strong>功能說明</strong>：讓 AI 代理與網頁互動，用於測試與自動化

> **ℹ️ 驅動 GitHub Copilot**
> 
> Playwright MCP 伺服器驅動 GitHub Copilot 的程式編寫代理，使其具備網頁瀏覽功能！[了解此功能詳情](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

<strong>為何實用</strong>：非常適合透過自然語言描述驅動的自動化測試。AI 可以瀏覽網站、填寫表單，並透過可建立結構的無障礙快照擷取資料——這是非常強大的功能！

<strong>實際應用</strong>：「測試登入流程，並驗證儀表板是否正確載入」或「產生測試用例，搜尋產品並驗證結果頁面」——整個過程不需要應用程式原始碼。

<strong>展示範例</strong>：我的同事 Debbie O'Brien 最近在 Playwright MCP 伺服器上做了很棒的工作！例如，她展示如何在沒有應用程式原始碼存取的情況下產生完整的 Playwright 測試。在她的示範中，她要求 Copilot 為一個電影搜尋應用程式創建測試：瀏覽網站，搜尋「Garfield」，並驗證電影是否出現在結果中。MCP 啟動了一個瀏覽器會話，利用 DOM 快照探索頁面結構，找出正確的選擇器，並生成了一個能在首次執行就通過的完整 TypeScript 測試。

此技術強大之處在於，它橋接了自然語言指令與可執行測試程式碼之間的鴻溝。傳統做法需要手動撰寫測試或取得程式碼庫上下文。但使用 Playwright MCP，你可以測試外部網站、用戶端應用程式，或在無法取得程式碼的黑盒測試場景中工作。


### 8. 💻 Dev Box MCP 伺服器

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>功能說明</strong>：透過自然語言管理 Microsoft Dev Box 環境

<strong>為何實用</strong>：大幅簡化開發環境管理！無需記憶具體命令即可建立、配置和管理開發環境。

<strong>實際應用</strong>：「為我們的專案設定新的 Dev Box，安裝最新 .NET SDK」，「查詢我所有開發環境的狀態」，或「為團隊展示建立標準化的示範環境」。

<strong>展示範例</strong>：我非常喜歡用 Dev Box 進行個人開發。啟發我的時刻是 James Montemagno 解釋 Dev Box 如何適合會議展示，因為它無論當下連接的會議、飯店或飛機無線網路多不穩定，都有非常快速的乙太網路連線。事實上，我最近在布魯日搭車到安特衛普時，筆電透過手機熱點連線，還練習了會議展示！接下來，我打算深入研究團隊如何管理多個開發環境及標準化示範環境。而另一個我從客戶和同事聽到的重要用例，是用 Dev Box 做預設開發環境。兩者皆透過 MCP 配置和管理 Dev Box，實現自然語言互動，並能全程待在開發環境內。

### 9. 🤖 Microsoft Foundry MCP 伺服器


[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

<strong>它的功能</strong>：Microsoft Foundry MCP Server 為開發者提供完整存取 Azure 的 AI 生態系統，包括模型目錄、部署管理、利用 Azure AI Search 進行知識索引和評估工具。這個實驗性伺服器橋接了 AI 開發與 Azure 強大 AI 基礎架構之間的鴻溝，使構建、部署和評估 AI 應用程式變得更簡單。

<strong>為什麼它有用</strong>：這個伺服器改變了你使用 Azure AI 服務的方式，將企業級 AI 能力直接引入你的開發工作流程。你不必在 Azure 入口網站、文件和 IDE 之間切換，而是可以通過自然語言指令搜尋模型、部署服務、管理知識庫及評估 AI 表現。對於構建 RAG（檢索增強生成）應用程式、管理多模型部署或實施全面 AI 評估管線的開發者尤其強大。

<strong>主要開發者功能</strong>：
- **🔍 模型發現與部署**：瀏覽 Microsoft Foundry 的模型目錄，獲取詳細的模型資訊與程式碼範例，並將模型部署到 Azure AI 服務
- **📚 知識管理**：建立及管理 Azure AI Search 索引，新增文件，配置索引器，並構建先進的 RAG 系統
- **⚡ AI 代理整合**：連接 Azure AI 代理，查詢現有代理，並在生產場景中評估代理效能
- **📊 評估框架**：執行全面的文本和代理評估，生成 markdown 報告，並為 AI 應用實施品質保證
- **🚀 原型設計工具**：獲得基於 GitHub 的原型設置指引並存取 Microsoft Foundry Labs 的最新研究模型

<strong>實際開發者使用情境</strong>：「將 Phi-4 模型部署到 Azure AI 服務用於我的應用程式」、「為我的文件 RAG 系統創建新的搜尋索引」、「根據品質指標評估我的代理回應」，或「尋找適合複雜分析任務的最佳推理模型」

<strong>完整示範場景</strong>：以下是一個強大的 AI 開發工作流程：

> 「我正在構建一個客戶支持代理。幫我從目錄找到一個好的推理模型，部署到 Azure AI 服務，從我們的文件建立知識庫，設置評估框架以測試回應質量，然後幫我用 GitHub 代幣進行集成原型測試。」

Microsoft Foundry MCP Server 將會：
- 根據你的需求查詢模型目錄，推薦最佳推理模型
- 提供部署命令與所選 Azure 區域的配額資訊
- 設置符合文件需求的 Azure AI Search 索引及其正確架構
- 配置帶有品質指標和安全檢查的評估管線
- 生成含 GitHub 認證的原型程式碼，立即進行測試
- 提供量身定制的全面設置指南，適用於你的技術棧

<strong>特色範例</strong>：身為開發者，我一直難以跟上眾多大型語言模型 (LLM) 的資訊。我只知道幾個主要模型，但感覺錯過了某些提高生產力及效率的機會。而且代幣和配額讓人壓力很大且難以管理——我從不知道自己是否選擇了適合任務的模型，或是在不有效率地燒預算。最近在跟團隊查詢 MCP Server 推薦時，聽 James Montemagno 提到這個 MCP Server，我很期待使用！模型發現功能對像我這種想探索更多非主流模型並尋找為特定任務優化模型的人來說特別出色。評估框架將幫我確保我獲得的結果確實更好，而不只是嘗試新東西而已。

> **ℹ️ 實驗性狀態**
> 
> 此 MCP 伺服器為實驗性且持續開發中，功能和 API 可能會變動。非常適合探索 Azure AI 能力和建立原型，但生產環境務必檢驗穩定性要求。
### 10. 🏢 Microsoft 365 代理工具包 MCP 伺服器

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

<strong>它的功能</strong>：為開發者提供構建與 Microsoft 365 及 Microsoft 365 Copilot 整合的 AI 代理和應用程式的必備工具，包括模式驗證、範例程式碼檢索和疑難排解支援。

<strong>為什麼它有用</strong>：針對 Microsoft 365 和 Copilot 構建涉及複雜的 manifest 結構及特定開發模式。這個 MCP 伺服器將必要的開發資源直接帶入你的編碼環境，幫你驗證結構、尋找範例程式碼以及排除常見問題，無需頻繁查閱文件。

<strong>實際使用情境</strong>：「驗證我的宣告式代理 manifest 並修正任何結構錯誤」、「展示實作 Microsoft Graph API 插件的範例程式碼」，或是「幫我排除 Teams 應用程式的身份驗證問題」

<strong>特色範例</strong>：與 John Miller 在 Build 活動聊天後，我向他詢問 M365 代理相關資訊，他推薦了這個 MCP。對剛接觸 M365 代理的開發者來說相當有幫助，因為它提供模板、範例碼及構架，讓開發者不必陷入繁雜的文件。模式驗證功能對避免 manifest 結構錯誤非常實用，那些錯誤常常會導致數小時的除錯工作。

> **💡 專業小貼士**
> 
> 建議將此伺服器與 Microsoft Learn Docs MCP Server 同時使用以獲得全面的 M365 開發支援——官方文件由一者提供，實用工具及疑難協助由此伺服器提供。


## 接下來呢？🔮

## 📋 結論

模型上下文協議 (MCP) 正在改變開發者與 AI 助理及外部工具互動的方式。這 10 個 Microsoft MCP 伺服器展示了標準化 AI 整合的威力，使開發者能保持專注流程，同時存取強大的外部功能。

從完整的 Azure 生態系統整合，到 Playwright 等專門瀏覽器自動化工具及 MarkItDown 文檔處理工具，這些伺服器展現 MCP 如何提升多元開發場景下的生產力。標準化協議確保這些工具無縫協作，創造一致的開發體驗。

隨著 MCP 生態系統持續演進，積極參與社群、探索新伺服器及建立自訂解決方案將是提升開發效率的關鍵。而 MCP 的開放標準特性則讓你能自由混合不同供應商的工具，打造符合你需求的完美工作流程。

## 🔗 其他資源

- [官方 Microsoft MCP 倉庫](https://github.com/microsoft/mcp)
- [MCP 社群與文件](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 事件](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [超讚的 GitHub Copilot 自訂功能](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP 開發日 活動直播 7 月 29/30 日 或隨選觀看](https://aka.ms/mcpdevdays)

## 🎯 練習

1. <strong>安裝與設定</strong>：在你的 VS Code 環境中設置一個 MCP 伺服器並測試基本功能。
2. <strong>工作流程整合</strong>：設計一個結合至少三個不同 MCP 伺服器的開發工作流程。
3. <strong>自訂伺服器規劃</strong>：找出日常開發中可受惠於自訂 MCP 伺服器的任務，並制定規格。
4. <strong>效能分析</strong>：比較使用 MCP 伺服器與傳統方法執行常見開發任務的效率。
5. <strong>安全性評估</strong>：評估在開發環境中使用 MCP 伺服器的安全性影響，並提出最佳實踐。


下一章節:[最佳實踐](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
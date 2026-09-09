# 🚀 10 個正在改造開發者生產力的 Microsoft MCP 伺服器

## 🎯 本指南將學到的內容

本實用指南展示了十個 Microsoft MCP 伺服器，它們正積極改變開發人員如何使用 AI 助手工作。我們不僅會解釋 MCP 伺服器<em>能做</em>什麼，更會直接展示這些伺服器如何在 Microsoft 以及其他地方的日常開發工作流程中發揮真實作用。

本指南中的每個伺服器都是根據真實使用情況和開發者反饋精選的。你將不只了解每個伺服器的功能，更會懂得它們為何重要，以及如何在自己的專案中充分利用它們。無論你是 MCP 新手還是希望擴充現有設置，這些伺服器代表了 Microsoft 生態系統中一些最實用且具影響力的工具。

> **💡 快速入門提示**
> 
> MCP 新手嗎？別擔心！本指南設計得很適合初學者。我們將隨時解釋相關概念，你也可以隨時回顧我們的[Introduction to MCP](../00-Introduction/README.md)和[Core Concepts](../01-CoreConcepts/README.md)模組來獲得更深入的背景知識。

## 概覽

本綜合指南探討十個正在革命化開發人員與 AI 助手及外部工具互動方式的 Microsoft MCP 伺服器。從 Azure 資源管理到文件處理，這些伺服器展示了 Model Context Protocol 在創造無縫且高效開發工作流程方面的強大威力。

## 學習目標

閱讀結束後，你將能：
- 理解 MCP 伺服器如何提升開發者生產力
- 了解 Microsoft 最具影響力的 MCP 伺服器實作
- 探索每個伺服器的實用運用案例
- 知道如何在 VS Code 和 Visual Studio 中設置與配置這些伺服器
- 探索更廣泛的 MCP 生態系統與未來方向

## 🔧 理解 MCP 伺服器：初學者指南

### 什麼是 MCP 伺服器？

作為 Model Context Protocol (MCP) 的初學者，你可能會想：「MCP 伺服器到底是什麼？我為什麼需要關心？」讓我們先用個簡單比喻來說明。

把 MCP 伺服器想像成專門的助理，幫助你的 AI 程式碼夥伴（如 GitHub Copilot）連接到外部工具和服務。就像你會用手機上的不同應用程式來完成不同任務——一個看天氣、一個導航、一個辦理銀行業務——MCP 伺服器讓你的 AI 助手能與不同開發工具和服務互動。

### MCP 伺服器解決的問題

在有 MCP 伺服器之前，如果你想：
- 查詢你的 Azure 資源
- 建立 GitHub 問題
- 查詢你的資料庫
- 搜尋文件

你必須暫停寫程式，打開瀏覽器，前往相應網站，並手動執行這些任務。這種頻繁切換工作上下文會打斷你的工作流程並降低生產力。

### MCP 伺服器如何改造你的開發體驗

有了 MCP 伺服器，你可以留在你的開發環境（如 VS Code、Visual Studio 等），只需讓你的 AI 助手協助完成這些任務。例如：

**取代傳統工作流程：**
1. 停止寫程式
2. 開啟瀏覽器
3. 進入 Azure 管理入口網站
4. 查詢儲存帳號詳細資料
5. 回到 VS Code
6. 繼續寫程式

**你現在可以這樣做：**
1. 問 AI：「我的 Azure 儲存帳號狀況如何？」
2. 繼續使用提供的資訊寫程式

### 初學者的主要益處

#### 1. 🔄 <strong>保持專注狀態</strong>
- 不必再在多個應用間切換
- 保持對編寫代碼的專注
- 降低管理不同工具的心理負擔

#### 2. 🤖 <strong>使用自然語言而非複雜指令</strong>
- 不需要記憶 SQL 語法，只要描述你需要的數據
- 不必記住 Azure CLI 命令，只需說明你的目的
- 由 AI 處理技術細節，你專注於邏輯推理

#### 3. 🔗 <strong>連結多種工具</strong>
- 組合不同服務，打造強大工作流程
- 例如：「取得最近所有 GitHub 問題並建立相應的 Azure DevOps 工作項目」
- 無需撰寫複雜腳本即可建立自動化

#### 4. 🌐 <strong>存取不斷成長的生態系統</strong>
- 受惠於 Microsoft、GitHub 及其他公司的伺服器
- 無縫混搭不同廠商的工具
- 加入跨不同 AI 助手都有效的標準生態系統

#### 5. 🛠️ <strong>從實作中學習</strong>
- 從預建伺服器開始理解概念
- 隨著熟悉度提升，逐步建立自己的伺服器
- 利用可用的 SDK 和文檔輔助學習

### 初學者的真實示例

假設你是 Web 開發新手，正在進行你的第一個專案。以下展示 MCP 伺服器如何提供幫助：

**傳統方法：**
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

MCP 正成為產業標準，這意味著：
- <strong>一致性</strong>：不同工具和公司間提供相似體驗
- <strong>互操作性</strong>：不同廠商的伺服器能協同運作
- <strong>未來可延續性</strong>：技能和設置可在不同 AI 助手間轉移
- <strong>社群</strong>：擁有龐大且共享的知識和資源生態系統

### 入門指南：你將學到的內容

在本指南中，我們將探討 10 個對各種程度開發者特別有用的 Microsoft MCP 伺服器。每個伺服器皆設計用來：
- 解決常見開發挑戰
- 減少重複性任務
- 改善程式碼品質
- 增強學習機會

> **💡 學習小提示**
> 
> 如果你是 MCP 徹底新手，建議先從我們的[Introduction to MCP](../00-Introduction/README.md)和[Core Concepts](../01-CoreConcepts/README.md)模組開始學習。然後再回來這裡，看 Microsoft 實際工具如何應用這些概念。
>
> 想了解 MCP 重要性的更多背景，請參閱 Maria Naggaga 的文章：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## 在 VS Code 與 Visual Studio 開始使用 MCP 🚀

如果你使用 Visual Studio Code 或 Visual Studio 2022 搭配 GitHub Copilot，設定這些 MCP 伺服器相當簡單。

### VS Code 設定

以下是 VS Code 的基本流程：

1. **啟用 Agent 模式**：在 VS Code 中，於 Copilot Chat 視窗切換至 Agent 模式
2. **配置 MCP 伺服器**：將伺服器配置加入 VS Code 的 settings.json 檔案
3. <strong>啟動伺服器</strong>：為你想使用的每個伺服器點擊「啟動」按鈕
4. <strong>選擇工具</strong>：選擇當前會話要啟用的 MCP 伺服器

詳細設定說明請參見 [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)。

> **💡 專業提示：像專家一樣管理 MCP 伺服器！**
> 
> VS Code 擴充視窗現新增了[方便管理已安裝 MCP 伺服器的新介面](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)！你可以快速啟動、停止並管理任何安裝的 MCP 伺服器，介面清晰簡單，趕快試試看！

### Visual Studio 2022 設定

對於 Visual Studio 2022（版本 17.14 或更新）：

1. **啟用 Agent 模式**：點擊 GitHub Copilot Chat 視窗的「Ask」下拉選單並選擇「Agent」
2. <strong>建立配置文件</strong>：在方案目錄創建 `.mcp.json` 文件（建議位置：`<SOLUTIONDIR>\.mcp.json`）
3. <strong>配置伺服器</strong>：使用標準 MCP 格式加入你的 MCP 伺服器配置
4. <strong>工具授權</strong>：於提示時授權欲使用之工具，設定適當的權限範圍

詳細的 Visual Studio 設定說明請參見 [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)。

每個 MCP 伺服器都有自己的配置需求（連線字串、認證等），但兩個 IDE 中的設定模式是一致的。

## 從 Microsoft MCP 伺服器學到的教訓 🛠️

### 1. 📚 Microsoft Learn Docs MCP 伺服器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>它的功能</strong>：Microsoft Learn Docs MCP 伺服器是一個雲端託管服務，透過 Model Context Protocol 為 AI 助手提供即時訪問官方 Microsoft 文件的能力。它連接至 `https://learn.microsoft.com/api/mcp` ，並啟用跨 Microsoft Learn、Azure 文件、Microsoft 365 文件及其他官方 Microsoft 資源的語意搜尋。

<strong>它的價值</strong>：雖然看似只是「文件」，但本伺服器對於所有使用 Microsoft 技術的開發者來說至關重要。.NET 開發者對 AI 程式碼助手的最大抱怨之一是它們常常沒有更新到最新的 .NET 及 C# 版本。Microsoft Learn Docs MCP 伺服器藉由提供即時訪問最新文件、API 參考與最佳實踐，解決了這個問題。無論你是在使用最新的 Azure SDK、探索新的 C# 13 功能，還是實作最新的 Aspire 模式，本伺服器確保你的 AI 助手能取得權威且最新的資訊，產出精準且現代化的程式碼。

<strong>實務應用</strong>：「根據官方 Microsoft Learn 文件，az cli 有哪些指令可用來建立 Azure container app？」或者「如何在 ASP.NET Core 中使用依賴注入配置 Entity Framework？」又或者「請檢視此程式碼是否符合 Microsoft Learn 文件中的效能建議。」本伺服器透過先進的語意搜尋，全面涵蓋 Microsoft Learn、Azure 文件以及 Microsoft 365 文件，能找出上下文最相關的資訊。回傳多達 10 篇高質量內容片段，附帶文章標題和網址，且永遠存取最新發布的 Microsoft 文件。

<strong>特色示例</strong>：此伺服器公開 `microsoft_docs_search` 工具，執行針對 Microsoft 官方技術文件的語意搜尋。設定後，你可提問「如何在 ASP.NET Core 中實作 JWT 驗證？」並得到詳盡且官方的回覆與來源連結。搜尋質量卓越，因為理解上下文——在 Azure 環境下詢問「container」，會回傳 Azure Container Instances 文件；而同詞於 .NET 環境下，則給出相關 C# 集合資訊。

對於快速變動或近期更新的函式庫和使用案例尤其有用。例如，最近幾個專案中，我想利用 Aspire 與 Microsoft.Extensions.AI 的最新版本功能。透過包含 Microsoft Learn Docs MCP 伺服器，我不僅能利用 API 文件，還獲得剛發布的操作步驟與指導。

> **💡 專業提示**
> 
> 即使是支援工具的模型也需要鼓勵使用 MCP 工具！可考慮加入系統提示或[copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot)，例如：「你可以使用 `microsoft.docs.mcp` 工具——當處理 C#、Azure、ASP.NET Core 或 Entity Framework 等 Microsoft 技術相關問題時，請利用此工具搜尋 Microsoft 最新的官方文件。」
>
> 想看這類範例的運作，請參考 Awesome GitHub Copilot 倉庫中的 [C# .NET Janitor Chat Mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)。此模式特別利用 Microsoft Learn Docs MCP 伺服器協助清理及現代化 C# 程式碼，採用最新模式與最佳實踐。
### 2. ☁️ Azure MCP 伺服器


[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>功能說明</strong>：Azure MCP Server 是一套包含超過 15 種專用 Azure 服務連接器的完整套件，將整個 Azure 生態系統整合到您的 AI 工作流程中。它不僅僅是一台伺服器，更是一組強大工具集合，涵蓋資源管理、資料庫連接（PostgreSQL、SQL Server）、使用 KQL 的 Azure Monitor 日誌分析、Cosmos DB 整合等等。

<strong>用途說明</strong>：除了管理 Azure 資源外，此伺服器還大幅提升使用 Azure SDK 編碼時的程式品質。當您以 Agent 模式使用 Azure MCP，不只是協助您寫程式碼，而是幫您寫出<em>更好</em>的 Azure 程式碼，符合最新的驗證模式、錯誤處理慣例，並利用最新 SDK 功能。您不會只得到可運作的通用程式碼，而是符合 Azure 推薦用於生產工作負載的程式碼。

<strong>主要模組包括</strong>：
- **🗄️ 資料庫連接器**：透過自然語言直接存取 Azure Database for PostgreSQL 和 SQL Server
- **📊 Azure Monitor**：基於 KQL 的日誌分析與營運洞察
- **🌐 資源管理**：完整的 Azure 資源生命週期管理
- **🔐 驗證**：DefaultAzureCredential 與受控識別模式
- **📦 儲存服務**：Blob 儲存體、佇列儲存體和表格儲存體操作
- **🚀 容器服務**：Azure Container Apps、Container Instances 與 AKS 管理
- <strong>以及更多專業連接器</strong>

<strong>實務應用</strong>：例如「列出我的 Azure 儲存帳號」、「查詢過去一小時內 Log Analytics 工作區的錯誤」，或是「幫我用 Node.js 建立使用正確驗證的 Azure 應用程式」

<strong>完整示範案例</strong>：以下是一個完整流程演示，展示將 Azure MCP 與 VS Code 中 GitHub Copilot for Azure 擴充套件結合的力量。當您兩者皆安裝並輸入：

> 「建立一個 Python 腳本，使用 DefaultAzureCredential 驗證上傳檔案至 Azure Blob Storage。腳本應連接我名為 'mycompanystorage' 的 Azure 儲存帳號，將檔案上傳至名為 'documents' 的容器，建立一個含有當前時間戳記的測試檔案，上傳時優雅處理錯誤並提供資訊輸出，遵循 Azure 驗證和錯誤處理最佳實務，包含說明 DefaultAzureCredential 驗證如何運作的註解，且腳本結構完善，具備適當的函式和文件說明。」

Azure MCP Server 將產生一個完整且可投入生產的 Python 腳本，該腳本：
- 使用最新 Azure Blob Storage SDK 並採用正確的非同步模式
- 實作 DefaultAzureCredential，並詳盡說明備援機制
- 包含強健的錯誤處理，涵蓋特定 Azure 例外型別
- 遵循 Azure SDK 資源管理及連線處理最佳實務
- 提供詳細日誌及具有資訊性的命令列輸出
- 產出結構良好、包括函式、文件說明與型別提示的腳本

此外，沒有 Azure MCP，您可能只會取得能運作但不符合當前 Azure 規範的通用 Blob Storage 程式碼。使用 Azure MCP，您會得到運用了最新身份認證方法、處理 Azure 特有錯誤情境，且遵照微軟生產應用建議的程式碼。

<strong>示範實例</strong>：我曾經很難記住 `az`、`azd` CLI 工具的具體指令，往往分兩步：先查語法，再執行命令；我經常直接登入門戶操作，因為不願意承認自己記不得 CLI 語法。能夠只用語言描述需求真的很棒，更讚的是不用離開 IDE 就能做到！

您可在 [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) 找到豐富的使用案例起步指南。若需完整設定教學與進階配置選項，請參考 [官方 Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)。

### 3. 🐙 GitHub MCP Server

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

<strong>功能說明</strong>：官方 GitHub MCP Server 提供與 GitHub 全生態系統的無縫整合，包含託管的遠端存取與本地 Docker 部署選項。這不僅是基本的倉庫操作，它是包含 GitHub Actions 管理、拉取請求工作流程、議題追蹤、安全掃描、通知與先進自動化能力的完整工具組。

<strong>用途說明</strong>：此伺服器改變您與 GitHub 的互動方式，將整個平台體驗直接帶到您的開發環境。您不必頻繁切換 VS Code 和 GitHub.com 來進行專案管理、程式碼審查與 CI/CD 監控，能透過自然語言指令一次完成所有操作，專注於寫程式。

> **ℹ️ 注意：不同類型的「代理人」**
> 
> 不要將此 GitHub MCP Server 與 GitHub 的 Coding Agent（可被指派處理程式碼自動化工作的 AI 代理）混淆。GitHub MCP Server 工作於 VS Code 的 Agent 模式中，提供 GitHub API 整合；而 GitHub Coding Agent 是一項能在指派給 GitHub 議題時自動建立拉取請求的獨立功能。

<strong>主要功能包含</strong>：
- **⚙️ GitHub Actions**：完整 CI/CD 管線管理、工作流程監控與產物處理
- **🔀 拉取請求**：建立、審查、合併與管理 PR，具完整狀態追蹤
- **🐛 議題**：議題全生命周期管理、留言、標籤與指派
- **🔒 安全**：程式碼掃描警報、秘密檢測與 Dependabot 整合
- **🔔 通知**：智慧通知管理與倉庫訂閱控制
- **📁 倉庫管理**：檔案操作、分支管理與倉庫管理
- **👥 協作**：使用者與組織搜尋、團隊管理與存取控制

<strong>實務應用</strong>：例如「從我的功能分支建立拉取請求」、「顯示本週所有失敗的 CI 執行」、「列出我的倉庫中的所有開放安全警報」或「尋找指派給我在所有組織中的議題」

<strong>完整示範案例</strong>：以下是一個展示 GitHub MCP Server 強大功能的工作流程：

> 「我需要準備衝刺回顧，請顯示我本週建立的所有拉取請求，檢查 CI/CD 管線狀態，彙整需要處理的安全警報摘要，並協助我根據標有 'feature' 標籤的已合併 PR 草擬發行說明。」

GitHub MCP Server 將會：
- 查詢您近期的拉取請求與詳細狀態資訊
- 分析工作流程執行並標示任何錯誤或效能問題
- 彙整安全掃描結果並優先處理關鍵警報
- 從已合併 PR 提取資訊生成完整發行說明
- 提供衝刺計劃與發行準備的可行下一步建議

<strong>示範實例</strong>：我很喜歡用它來進行程式碼審查工作流程。不需來回在 VS Code、GitHub 通知與拉取請求頁面切換，我只要說「顯示所有等待我審查的 PR」，接著「在 #123 的 PR 留言詢問驗證方法中的錯誤處理」，伺服器就會處理 GitHub API 呼叫、維持討論上下文，甚至協助我撰寫更有效的審查意見。

<strong>驗證選項</strong>：此伺服器支援 OAuth（在 VS Code 中無縫整合）和個人存取權杖，並可透過設定啟用您所需的 GitHub 功能工具集。您可選擇以遠端託管服務快速部署，或使用 Docker 在本地執行以完全掌控。

> **💡 專家秘訣**
> 
> 透過在 MCP 伺服器設定中配置 `--toolsets` 參數，只啟用必需的工具集以減少上下文大小並提升 AI 工具選擇能力。例如，為核心開發工作流程新增 `"--toolsets", "repos,issues,pull_requests,actions"`，或若您主要想要 GitHub 監控功能，則使用 `"--toolsets", "notifications, security"`。
### 4. 🔄 Azure DevOps MCP Server

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

<strong>功能說明</strong>：連接 Azure DevOps 服務，提供完整的專案管理、工作項目追蹤、建置流程管理及倉庫操作。

<strong>用途說明</strong>：對於以 Azure DevOps 為主要 DevOps 平台的團隊，此 MCP 伺服器消除在開發環境與 Azure DevOps 網頁介面之間不斷切換的麻煩。您能直接透過 AI 助手管理工作項目、檢查建置狀態、查詢倉庫及處理專案管理任務。

<strong>實務應用</strong>：例如「顯示 WebApp 專案本衝刺中所有活動工作項目」、「為剛發現的登入問題建立錯誤報告」，或「檢查建置管線狀態並列出近期失敗」

<strong>示範實例</strong>：您可以輕鬆用「顯示 WebApp 專案本衝刺中所有活動工作項目」或「為剛發現的登入問題建立錯誤報告」等簡單查詢來查看團隊當前衝刺狀態，且不需離開您的開發環境。

### 5. 📝 MarkItDown MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

<strong>它的功能</strong>：MarkItDown 是一個全方位的文件轉換伺服器，能將各種檔案格式轉換成高品質的 Markdown，並針對大型語言模型消費與文本分析工作流程進行最佳化。

<strong>為何有用</strong>：對於現代文件工作流程來說不可或缺！MarkItDown 支援多種檔案格式，並且能保留重要的文件結構，如標題、清單、表格與連結。它並非僅是簡單的文字擷取工具，而是著重於維持語意意義與格式，對 AI 處理和人類可讀性皆具價值。

<strong>支援的檔案格式</strong>：
- **Office 文件**：PDF、PowerPoint (PPTX)、Word (DOCX)、Excel (XLSX/XLS)
- <strong>多媒體檔案</strong>：圖片（包含 EXIF 資料和光學文字辨識）、音訊（包含 EXIF 資料和語音轉錄）
- <strong>網頁內容</strong>：HTML、RSS 源、YouTube 網址、維基百科頁面
- <strong>資料格式</strong>：CSV、JSON、XML、ZIP 檔（遞迴處理內容）
- <strong>出版格式</strong>：EPub、Jupyter 筆記本 (.ipynb)
- <strong>電子郵件</strong>：Outlook 訊息 (.msg)
- <strong>進階</strong>：整合 Azure 文件智慧強化 PDF 處理

<strong>進階功能</strong>：MarkItDown 支援使用大型語言模型強化的圖像描述（需提供 OpenAI 用戶端）、Azure 文件智慧提升 PDF 處理、語音內容轉錄，並擁有可擴充至更多檔案格式的外掛系統。

<strong>實際應用</strong>：「將這個 PowerPoint 簡報轉成文件網站用的 Markdown」、「從這個 PDF 擷取文字並保留正確的標題結構」、或是「將這個 Excel 試算表轉換成可讀的表格格式」

<strong>示範範例</strong>：引用自 [MarkItDown 文件](https://github.com/microsoft/markitdown#why-markdown)：

> Markdown 非常接近純文字，僅有最少的標記或格式，但仍能表示重要的文件結構。主流大型語言模型，如 OpenAI 的 GPT-4o，原生“使用”Markdown，且經常在回應中無需提示地嵌入 Markdown。這顯示它們已受訓於大量 Markdown 格式的文本，且理解得很透徹。附帶好處是，Markdown 約定也相當節省詞元使用。

MarkItDown 非常擅長保留文件結構，這對 AI 工作流程至關重要。例如，在轉換 PowerPoint 簡報時，它保留投影片的組織與正確標題，將表格抽取成 Markdown 表格，加上圖片的替代文字，甚至處理演講者筆記。圖表會轉換成可讀的資料表，而產出的 Markdown 保持原始簡報的邏輯流程。這使它非常適合將簡報內容輸入 AI 系統或用現有投影片製作文檔。
### 6. 🗃️ SQL Server MCP 伺服器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>它的功能</strong>：提供對 SQL Server 資料庫（本機、Azure SQL 或 Fabric）的對話式存取

<strong>為何有用</strong>：類似 PostgreSQL 伺服器，但用於 Microsoft SQL 生態系。只需簡單的連接字串即可連線，並以自然語言開始查詢－不必再頻繁切換上下文！

<strong>實際應用</strong>：「找到過去 30 天尚未完成的所有訂單」會被轉為相應的 SQL 查詢並回傳格式化結果

<strong>示範範例</strong>：完成資料庫連線設定後，即可立即與資料展開對話。該部落格以簡單問題展示： “你連接的是哪個資料庫？” MCP 伺服器透過調用適當的資料庫工具，連接至 SQL Server 執行個體，並回覆當前資料庫連線的細節—完全不需撰寫任何 SQL。伺服器支持從結構管理到資料操作的完整資料庫作業，全部透過自然語言提示即可完成。完整的安裝說明與 VS Code 及 Claude Desktop 的配置範例，請參考：[Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)。


### 7. 🎭 Playwright MCP 伺服器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

<strong>它的功能</strong>：使 AI 代理能與網頁互動，用於測試與自動化

> **ℹ️ 支援 GitHub Copilot**
> 
> Playwright MCP 伺服器是 GitHub Copilot 的 Coding Agent 的驅動引擎，賦予其瀏覽網頁的能力！[瞭解更多此功能](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

<strong>為何有用</strong>：非常適合用自然語言描述驅動的自動化測試。AI 可以瀏覽網站、填寫表單，並透過結構化的可及性快照提取資料－這真的是非常強大的功能！

<strong>實際應用</strong>：「測試登入流程並驗證儀表板是否正確載入」或「產生一個搜尋商品並驗證結果頁面的測試」－全部無需應用程式原始碼

<strong>示範範例</strong>：我的同事 Debbie O'Brien 近期在 Playwright MCP 伺服器上的表現非常出色！例如，她最近示範如何在完全沒有應用程式原始碼的情況下產生完整的 Playwright 測試。在她的案例中，她請 Copilot 為電影搜尋應用建立測試：瀏覽至網站，搜尋 "Garfield"，並驗證電影是否出現在結果中。MCP 啟動瀏覽器工作階段，利用 DOM 快照探索頁面結構，找出正確的選擇器，並產生一個完全運作的 TypeScript 測試，且第一次執行即通過。

這項功能強大的地方在於它彌合了自然語言指示與可執行測試代碼間的鴻溝。傳統方式通常需要手動編寫測試或取得程式碼庫作為背景，但 Playwright MCP 讓你可以測試外部網站、客戶端應用，或在無法存取程式碼的黑盒測試場景下工作。


### 8. 💻 Dev Box MCP 伺服器

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>它的功能</strong>：透過自然語言管理 Microsoft Dev Box 環境

<strong>為何有用</strong>：大幅簡化開發環境管理！建立、配置與管理開發環境，不必記住特定指令。

<strong>實際應用</strong>：「設置新的 Dev Box 並安裝最新版 .NET SDK，配置為我們的專案使用」、「檢查所有開發環境的狀態」或「為團隊發表會建立標準化演示環境」

<strong>示範範例</strong>：我很喜歡使用 Dev Box 作為個人開發環境。令我印象深刻的是，James Montemagno 曾說明 Dev Box 非常適合會議演示，因為它有超高速的網路連接，不論我在何種會議、飯店或是飛機上的 Wi-Fi。事實上，我最近甚至用筆電綁定手機熱點，在公車從布魯日到安特衛普的路上練習會議演示！接下來，我打算深入探討更多團隊管理多個開發環境和標準化演示環境。而且我聽許多客戶和同事說，使用 Dev Box 作為預設配置的開發環境也是一大應用。在這兩種場景下，透過 MCP 以自然語言交互來配置與管理 Dev Box，可以讓你完全待在開發環境中進行操作。

### 9. 🤖 Microsoft Foundry MCP 伺服器


[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

<strong>功能說明</strong>：Microsoft Foundry MCP Server 為開發人員提供全面存取 Azure AI 生態系統的能力，包括模型目錄、部署管理、Azure AI Search 的知識索引與評估工具。這個實驗性伺服器彌合了 AI 開發與 Azure 強大 AI 基礎架構之間的鴻溝，使建構、部署及評估 AI 應用變得更加容易。

<strong>為何有用</strong>：此伺服器改變您與 Azure AI 服務互動的方式，將企業級 AI 功能直接納入開發流程。您不必在 Azure 入口網站、文件和開發環境之間切換，就能透過自然語言指令來探索模型、部署服務、管理知識庫和評估 AI 性能。對於開發 RAG（檢索強化生成）應用、多模型部署管理或實現完整 AI 評估流程的開發者尤其有力。

<strong>主要開發者能力</strong>：
- **🔍 模型探索與部署**：瀏覽 Microsoft Foundry 的模型目錄，取得詳細模型資訊與程式碼範例，並部署模型至 Azure AI 服務
- **📚 知識管理**：建立與管理 Azure AI Search 索引，新增文件、配置索引器，並構建高級 RAG 系統
- **⚡ AI 代理整合**：連接 Azure AI 代理，查詢現有代理，並在生產情境中評估代理執行效能
- **📊 評估框架**：執行全面的文字與代理評估，產生 Markdown 報告，並為 AI 應用實施品質保證
- **🚀 原型設計工具**：提供基於 GitHub 的原型設置指導，並存取 Microsoft Foundry Labs 的前沿研究模型

<strong>實際開發用途</strong>：「將 Phi-4 模型部署至 Azure AI 服務，供我的應用使用」、「為我的文件 RAG 系統建立新的搜索索引」、「根據品質指標評估我的代理回應」，或「為我的複雜分析任務尋找最佳推理模型」

<strong>完整示範場景</strong>：以下是一個強大的 AI 開發工作流程：

> 「我正在建置一個客戶支援代理。幫助我從目錄中尋找優質推理模型，部署到 Azure AI 服務，從我們的文件建立知識庫，設置評估框架以測試回應品質，然後協助我利用 GitHub token 進行整合原型測試。」

Microsoft Foundry MCP Server 將會：
- 根據您的需求查詢模型目錄並推薦最佳推理模型
- 提供在您偏好 Azure 區域的部署指令與配額資訊
- 為您的文件設置符合正確結構的 Azure AI Search 索引
- 配置評估流程，包含品質指標與安全檢查
- 產生帶有 GitHub 認證的原型程式碼，供立即測試使用
- 提供專屬於您技術堆疊的完整設置指南

<strong>特色範例</strong>：作為開發者，我一直很難掌握不同的 LLM 模型。我只知道幾個主流模型，但總覺得錯過了提高生產力與效率的機會。代幣與配額的管理讓我壓力很大且難以掌控──我從未確定自己是否為對的任務選對了模型，或者無效率地燒掉預算。我最近從 James Montemagno 那裡知道了這個 MCP Server，當時我正和團隊成員討論 MCP Server 推薦，現在我很期待開始使用它！模型發現功能對於像我這樣想探索主流之外、尋找針對特定任務優化模型的人尤其令人印象深刻。評估框架則有助於我驗證自己確實獲得更好結果，而非為了嘗試新東西而嘗試。

> **ℹ️ 實驗狀態**
> 
> 此 MCP 伺服器屬於實驗性質並正積極開發中。功能和 API 可能隨時變動。非常適合探索 Azure AI 功能和打造原型，但使用於生產環境時需驗證其穩定性。
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

<strong>功能說明</strong>：為開發者提供構建整合 Microsoft 365 與 Microsoft 365 Copilot 的 AI 代理與應用的必要工具，包括結構驗證、程式碼範例檢索以及除錯協助。

<strong>為何有用</strong>：為 Microsoft 365 與 Copilot 開發涉及複雜的宣告式結構與特定開發模式。此 MCP 伺服器將必要的開發資源直接帶入您的編碼環境，協助您驗證結構、尋找範例程式碼以及除錯常見問題，而不需經常翻閱文件。

<strong>實際使用例子</strong>：「驗證我的宣告式代理結構並修正任何結構錯誤」、「示範 Microsoft Graph API 外掛的實作範例程式碼」，或「協助我排解 Teams 應用程式的身份驗證問題」

<strong>特色範例</strong>：我在 Build 與朋友 John Miller 談及 M365 Agents 後，得到了他的這個 MCP 推薦。對於剛接觸 M365 Agents 的開發者來說，這很棒，因為它提供範本、範例程式碼和腳手架工具，幫助他們從容開始，而不致淹沒在文件裡。結構驗證功能看起來特別實用，能避免因結構錯誤導致數小時的除錯。

> **💡 專家秘訣**
> 
> 建議與 Microsoft Learn Docs MCP Server 配合使用，獲得完整的 M365 開發支援──一方提供官方文件，另一方則提供實務開發工具及除錯協助。


## 下一步？🔮

## 📋 結論

模型上下文協議（MCP）正在改變開發者與 AI 助理及外部工具互動的方式。這 10 個 Microsoft MCP 伺服器展示了標準化 AI 整合的強大能力，使開發者能順暢工作流程，持續保持專注，同時存取強大的外部功能。

從完整的 Azure 生態系統整合，到專門工具如 Playwright 用於瀏覽器自動化及 MarkItDown 用於文件處理，這些伺服器展示了 MCP 如何在各種開發場景中提升生產力。標準化協議確保這些工具能無縫協作，打造一致的開發體驗。

隨著 MCP 生態系統持續演進，積極參與社群、探索新伺服器並打造自訂解決方案，將是提升開發生產力的關鍵。MCP 開放標準的特性意味著您可以混合使用來自不同供應商的工具，創造符合您特定需求的完美工作流程。

## 🔗 其他資源

- [官方 Microsoft MCP 倉庫](https://github.com/microsoft/mcp)
- [MCP 社群與文件](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 活動](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [精彩 GitHub Copilot 自訂化](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days 現場活動 7 月 29/30 日，或隨選觀看](https://aka.ms/mcpdevdays)

## 🎯 練習題

1. <strong>安裝與設定</strong>：在您的 VS Code 環境中設置一個 MCP 伺服器並測試基本功能。
2. <strong>工作流程整合</strong>：設計一個結合至少三個不同 MCP 伺服器的開發工作流程。
3. <strong>自訂伺服器規劃</strong>：找出您日常開發工作中可受益於自訂 MCP 伺服器的任務並撰寫規格說明。
4. <strong>效能分析</strong>：比較使用 MCP 伺服器與傳統方式完成常見開發任務的效率。
5. <strong>安全評估</strong>：評估在您的開發環境中使用 MCP 伺服器的安全影響，並提出最佳實務建議。


下一篇：[最佳實務](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
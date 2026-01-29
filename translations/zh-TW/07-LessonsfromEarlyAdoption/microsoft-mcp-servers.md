# 🚀 10 個正在改變開發者生產力的 Microsoft MCP 伺服器

## 🎯 本指南你將學到什麼

這份實用指南介紹了十個 Microsoft MCP 伺服器，這些伺服器正積極改變開發者與 AI 助手的互動方式。我們不只是說明 MCP 伺服器*能做什麼*，而是展示那些已經在 Microsoft 及其他地方的日常開發流程中帶來實際影響的伺服器。

本指南中的每個伺服器都是根據真實使用情況和開發者反饋精心挑選。你不僅會了解每個伺服器的功能，還會知道它的重要性以及如何在自己的專案中充分利用。無論你是 MCP 新手，還是想擴展現有配置，這些伺服器都代表了 Microsoft 生態系統中最實用且具影響力的工具。

> **💡 快速入門小技巧**  
>  
> MCP 新手別擔心！本指南設計得很友善，我們會邊講解邊帶你了解概念，你也可以隨時回頭參考我們的 [MCP 介紹](../00-Introduction/README.md) 和 [核心概念](../01-CoreConcepts/README.md) 模組，獲得更深入的背景知識。

## 概覽

這份全面指南探討了十個 Microsoft MCP 伺服器，這些伺服器正在革新開發者與 AI 助手及外部工具的互動方式。從 Azure 資源管理到文件處理，這些伺服器展示了 Model Context Protocol 在打造無縫且高效開發流程中的強大威力。

## 學習目標

完成本指南後，你將能夠：
- 了解 MCP 伺服器如何提升開發者生產力
- 認識 Microsoft 最具影響力的 MCP 伺服器實作
- 探索每個伺服器的實際應用案例
- 知道如何在 VS Code 和 Visual Studio 中設定與配置這些伺服器
- 探索更廣泛的 MCP 生態系統及未來發展方向

## 🔧 認識 MCP 伺服器：新手指南

### 什麼是 MCP 伺服器？

作為 Model Context Protocol (MCP) 的新手，你可能會想：「MCP 伺服器到底是什麼？為什麼我需要關心？」讓我們用一個簡單的比喻來說明。

把 MCP 伺服器想像成專門的助理，幫助你的 AI 編碼夥伴（像是 GitHub Copilot）連接到外部工具和服務。就像你手機上會用不同的應用程式處理不同任務——一個看天氣、一個導航、一個銀行理財——MCP 伺服器讓你的 AI 助手能與各種開發工具和服務互動。

### MCP 伺服器解決了什麼問題

在有 MCP 伺服器之前，如果你想要：
- 查看 Azure 資源
- 建立 GitHub issue
- 查詢資料庫
- 搜尋文件

你必須暫停編碼，打開瀏覽器，前往相應網站，手動完成這些操作。這種頻繁切換上下文會打斷你的思路，降低生產力。

### MCP 伺服器如何改變你的開發體驗

有了 MCP 伺服器，你可以留在開發環境（VS Code、Visual Studio 等）中，直接請 AI 助手幫你處理這些任務。例如：

**傳統流程：**  
1. 停止編碼  
2. 打開瀏覽器  
3. 進入 Azure 入口網站  
4. 查詢儲存帳戶細節  
5. 回到 VS Code  
6. 繼續編碼  

**現在你可以這樣做：**  
1. 問 AI：「我的 Azure 儲存帳戶狀態如何？」  
2. 根據回覆繼續編碼  

### 新手的主要好處

#### 1. 🔄 **保持專注狀態**  
- 不用在多個應用程式間切換  
- 專注於正在撰寫的程式碼  
- 降低管理不同工具的心理負擔  

#### 2. 🤖 **用自然語言取代複雜指令**  
- 不用背 SQL 語法，只要描述你需要的資料  
- 不用記 Azure CLI 指令，只要說明你想完成的目標  
- 讓 AI 處理技術細節，你專注邏輯  

#### 3. 🔗 **串接多種工具**  
- 組合不同服務，打造強大工作流程  
- 例如：「取得所有近期 GitHub issue，並建立對應的 Azure DevOps 工作項目」  
- 無需撰寫複雜腳本即可自動化  

#### 4. 🌐 **接觸不斷成長的生態系統**  
- 利用 Microsoft、GitHub 及其他公司打造的伺服器  
- 無縫混合不同廠商的工具  
- 加入跨 AI 助手通用的標準化生態系統  

#### 5. 🛠️ **邊做邊學**  
- 從預建伺服器開始理解概念  
- 慢慢建立自己的伺服器  
- 利用現有 SDK 和文件輔助學習  

### 新手的實際範例

假設你是網頁開發新手，正在做第一個專案。MCP 伺服器能這樣幫你：

**傳統做法：**  
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

MCP 正成為業界標準，這代表：  
- **一致性**：不同工具和公司間體驗相似  
- **互通性**：不同廠商的伺服器能協同工作  
- **未來保障**：技能和設定可跨 AI 助手轉移  
- **社群**：龐大生態系統共享知識與資源  

### 開始學習：你將學到什麼

本指南將介紹 10 個特別適合各種程度開發者使用的 Microsoft MCP 伺服器。每個伺服器都旨在：  
- 解決常見開發挑戰  
- 減少重複性工作  
- 提升程式碼品質  
- 增強學習機會  

> **💡 學習小技巧**  
>  
> 如果你完全不熟 MCP，建議先從我們的 [MCP 介紹](../00-Introduction/README.md) 和 [核心概念](../01-CoreConcepts/README.md) 模組開始，然後再回來看看這些概念如何在 Microsoft 工具中實際運作。  
>  
> 想了解 MCP 重要性的更多背景，可以參考 Maria Naggaga 的文章：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## 在 VS Code 和 Visual Studio 中開始使用 MCP 🚀

如果你使用 Visual Studio Code 或 Visual Studio 2022 搭配 GitHub Copilot，設定這些 MCP 伺服器非常簡單。

### VS Code 設定

VS Code 的基本流程如下：

1. **啟用 Agent 模式**：在 Copilot Chat 視窗切換到 Agent 模式  
2. **配置 MCP 伺服器**：將伺服器設定加入 VS Code 的 settings.json  
3. **啟動伺服器**：點擊你想使用的伺服器旁的「啟動」按鈕  
4. **選擇工具**：挑選本次工作階段要啟用的 MCP 伺服器  

詳細設定說明請參考 [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)。

> **💡 專業提示：像專家一樣管理 MCP 伺服器！**  
>  
> VS Code 擴充功能檢視現在有一個[方便的新介面來管理已安裝的 MCP 伺服器](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)！你可以快速啟動、停止並管理任何 MCP 伺服器，介面清晰簡單，快去試試看！

### Visual Studio 2022 設定

Visual Studio 2022（版本 17.14 或更新）設定步驟：

1. **啟用 Agent 模式**：在 GitHub Copilot Chat 視窗點選「Ask」下拉選單，選擇「Agent」  
2. **建立設定檔**：在解決方案目錄下建立 `.mcp.json` 檔案（建議位置：`<SOLUTIONDIR>\.mcp.json`）  
3. **配置伺服器**：使用標準 MCP 格式加入伺服器設定  
4. **工具授權**：系統提示時，核准你想使用的工具及其權限範圍  

詳細 Visual Studio 設定說明請參考 [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)。

每個 MCP 伺服器都有自己的設定需求（連線字串、認證等），但兩個 IDE 的設定流程大致相同。

## 從 Microsoft MCP 伺服器學到的經驗 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![在 VS Code 安裝](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![在 VS Code Insiders 安裝](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**功能說明**：Microsoft Learn Docs MCP Server 是一個雲端服務，透過 Model Context Protocol 提供 AI 助手即時存取官方 Microsoft 文件。它連接到 `https://learn.microsoft.com/api/mcp`，支援 Microsoft Learn、Azure 文件、Microsoft 365 文件及其他官方資源的語意搜尋。

**為什麼有用**：看似「只是文件」，但這個伺服器對每位使用 Microsoft 技術的開發者都至關重要。許多 .NET 開發者對 AI 編碼助手最大的抱怨是它們無法掌握最新的 .NET 和 C# 版本。Microsoft Learn Docs MCP Server 解決了這個問題，提供即時存取最新的文件、API 參考和最佳實踐。無論你是在使用最新的 Azure SDK、探索 C# 13 新功能，還是實作前沿的 .NET Aspire 模式，這個伺服器都確保你的 AI 助手能取得權威且最新的資訊，生成準確且現代的程式碼。

**實際應用**：例如「根據官方 Microsoft Learn 文件，az cli 指令如何建立 Azure container app？」或「如何在 ASP.NET Core 中使用依賴注入配置 Entity Framework？」又或者「請檢查這段程式碼是否符合 Microsoft Learn 文件中的效能建議。」此伺服器利用先進的語意搜尋，涵蓋 Microsoft Learn、Azure 文件和 Microsoft 365 文件，回傳最多 10 個高品質內容片段，附帶文章標題和 URL，並且始終存取最新發布的 Microsoft 文件。

**特色範例**：此伺服器提供 `microsoft_docs_search` 工具，可對 Microsoft 官方技術文件進行語意搜尋。設定完成後，你可以問「如何在 ASP.NET Core 實作 JWT 認證？」並獲得詳細且官方的回覆，附帶來源連結。搜尋品質優異，能理解上下文——在 Azure 相關問題中提到「containers」會回傳 Azure Container Instances 文件，而在 .NET 相關問題中則會回傳 C# 集合相關資訊。

這對於快速變動或近期更新的函式庫和使用案例特別有用。例如，我最近在一些專案中想利用最新版本的 .NET Aspire 和 Microsoft.Extensions.AI 功能，加入 Microsoft Learn Docs MCP 伺服器後，不僅能取得 API 文件，還能獲得剛發布的教學和指引。
> **💡 專家提示**
> 
> 即使是對工具友善的模型，也需要鼓勵才能使用 MCP 工具！可以考慮加入系統提示或 [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot)，例如：「你可以使用 `microsoft.docs.mcp`，在處理關於 Microsoft 技術（如 C#、Azure、ASP.NET Core 或 Entity Framework）的問題時，利用此工具搜尋 Microsoft 最新的官方文件。」
>
> 想看這個功能的實際範例，可以參考 Awesome GitHub Copilot 倉庫中的 [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)。此模式特別利用 Microsoft Learn Docs MCP 伺服器，幫助清理並現代化 C# 程式碼，採用最新的設計模式和最佳實踐。
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**功能說明**：Azure MCP Server 是一套包含超過15個專門化 Azure 服務連接器的完整工具組，將整個 Azure 生態系統整合進你的 AI 工作流程。這不僅僅是一個單一伺服器，而是一個強大的集合，涵蓋資源管理、資料庫連接（PostgreSQL、SQL Server）、使用 KQL 的 Azure Monitor 日誌分析、Cosmos DB 整合等多種功能。

**為什麼有用**：除了管理 Azure 資源外，這個伺服器在使用 Azure SDK 時能大幅提升程式碼品質。當你以 Agent 模式使用 Azure MCP，它不只是幫你寫程式碼，而是幫你寫出符合現行認證模式、錯誤處理最佳實踐，並善用最新 SDK 功能的 *更優質* Azure 程式碼。你不會只拿到可能可用的通用程式碼，而是符合 Azure 推薦生產環境模式的程式碼。

**主要模組包括**：
- **🗄️ 資料庫連接器**：以自然語言直接存取 Azure Database for PostgreSQL 和 SQL Server
- **📊 Azure Monitor**：基於 KQL 的日誌分析與運營洞察
- **🌐 資源管理**：完整的 Azure 資源生命週期管理
- **🔐 認證**：DefaultAzureCredential 與受管身份模式
- **📦 儲存服務**：Blob Storage、Queue Storage 和 Table Storage 操作
- **🚀 容器服務**：Azure Container Apps、Container Instances 及 AKS 管理
- **以及更多專門化連接器**

**實際應用範例**：「列出我的 Azure 儲存帳戶」、「查詢我 Log Analytics 工作區過去一小時的錯誤」，或「幫我用 Node.js 建立一個具備正確認證的 Azure 應用程式」

**完整示範場景**：以下是一個完整示範，展示如何結合 Azure MCP 與 VS Code 中的 GitHub Copilot for Azure 擴充功能。當你兩者都安裝後，輸入：

> 「建立一個 Python 腳本，使用 DefaultAzureCredential 認證將檔案上傳到 Azure Blob Storage。腳本應連接到名為 'mycompanystorage' 的 Azure 儲存帳戶，並上傳到名為 'documents' 的容器，建立一個帶有當前時間戳的測試檔案進行上傳，優雅地處理錯誤並提供詳細輸出，遵循 Azure 認證與錯誤處理最佳實踐，並包含說明 DefaultAzureCredential 認證運作方式的註解，腳本結構良好，具備適當的函式與文件說明。」

Azure MCP Server 將產生一個完整且可用於生產的 Python 腳本，該腳本：
- 使用最新的 Azure Blob Storage SDK 並採用正確的非同步模式
- 實作 DefaultAzureCredential，並詳細說明完整的備援鏈
- 包含強健的錯誤處理，涵蓋特定的 Azure 例外類型
- 遵循 Azure SDK 在資源管理與連線處理上的最佳實踐
- 提供詳細的日誌記錄與清晰的終端輸出
- 建立結構良好的腳本，包含函式、文件說明與型別提示

這點非常特別，因為沒有 Azure MCP，你可能只會得到一段通用且可用的 blob storage 程式碼，但不符合現行 Azure 模式。使用 Azure MCP，你得到的程式碼會利用最新認證方法，處理 Azure 特有的錯誤情境，並遵循微軟推薦的生產環境實務。

**特色範例**：我常常忘記 `az` 和 `azd` CLI 的特定指令，通常是先查語法再執行命令。很多時候我會直接進入 Azure 入口網站點擊操作，因為不想承認自己記不住 CLI 語法。能夠只用描述方式表達需求真的很棒，更棒的是能在 IDE 裡直接完成！

[Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) 裡有一份很棒的使用案例清單，幫助你快速上手。想要完整的安裝指南與進階設定選項，請參考[官方 Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)。

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**功能說明**：官方 GitHub MCP Server 提供與 GitHub 全生態系統的無縫整合，支援遠端託管存取與本地 Docker 部署選項。這不只是基本的倉庫操作，而是一套完整工具組，涵蓋 GitHub Actions 管理、拉取請求工作流程、議題追蹤、安全掃描、通知與進階自動化功能。

**為什麼有用**：這個伺服器改變你與 GitHub 互動的方式，將完整平台體驗直接帶入開發環境。你不必頻繁在 VS Code 與 GitHub.com 間切換來管理專案、程式碼審查和 CI/CD 監控，而是能透過自然語言指令一手掌控，專注於程式碼。

> **ℹ️ 注意：不同類型的「Agent」**
> 
> 請勿將此 GitHub MCP Server 與 GitHub 的 Coding Agent（可指派議題進行自動化程式碼任務的 AI agent）混淆。GitHub MCP Server 在 VS Code 的 Agent 模式中提供 GitHub API 整合，而 GitHub Coding Agent 是另一項功能，會在被指派議題時建立拉取請求。

**主要功能包括**：
- **⚙️ GitHub Actions**：完整 CI/CD 管線管理、工作流程監控與產物處理
- **🔀 拉取請求**：建立、審查、合併與管理 PR，並提供完整狀態追蹤
- **🐛 議題**：完整議題生命週期管理、留言、標籤與指派
- **🔒 安全**：程式碼掃描警示、秘密偵測與 Dependabot 整合
- **🔔 通知**：智慧通知管理與倉庫訂閱控制
- **📁 倉庫管理**：檔案操作、分支管理與倉庫管理
- **👥 協作**：使用者與組織搜尋、團隊管理與存取控制

**實際應用範例**：「從我的功能分支建立拉取請求」、「顯示本週所有失敗的 CI 執行」、「列出我所有倉庫的開啟安全警示」，或「找出所有指派給我的議題，跨越我的組織」

**完整示範場景**：以下是一個展示 GitHub MCP Server 功能的強大工作流程：

> 「我要準備我們的 sprint 回顧。請顯示我本週建立的所有拉取請求，檢查我們 CI/CD 管線的狀態，彙整需要處理的安全警示摘要，並協助我根據帶有 'feature' 標籤的已合併 PR 草擬發行說明。」

GitHub MCP Server 將會：
- 查詢你近期的拉取請求並提供詳細狀態資訊
- 分析工作流程執行並標示任何失敗或效能問題
- 彙整安全掃描結果並優先處理關鍵警示
- 從已合併 PR 中擷取資訊，生成完整的發行說明
- 提供可行的後續步驟，協助 sprint 規劃與發行準備

**特色範例**：我很喜歡用它來處理程式碼審查流程。不用在 VS Code、GitHub 通知和拉取請求頁面間跳來跳去，我只要說「顯示所有等待我審查的 PR」，接著說「在 PR #123 加一則留言，詢問認證方法的錯誤處理」。伺服器會處理 GitHub API 呼叫，維持討論上下文，甚至幫我撰寫更具建設性的審查評論。

**認證選項**：伺服器支援 OAuth（在 VS Code 中無縫整合）與個人存取權杖，並可透過設定只啟用你需要的 GitHub 功能模組。你可以選擇以遠端託管服務快速部署，或透過 Docker 本地執行以獲得完全控制。

> **💡 專家提示**
> 
> 透過在 MCP 伺服器設定中使用 `--toolsets` 參數，只啟用你需要的工具集，能減少上下文大小並提升 AI 工具選擇效率。例如，針對核心開發工作流程，加入 `"--toolsets", "repos,issues,pull_requests,actions"`；若主要想要 GitHub 監控功能，則使用 `"--toolsets", "notifications, security"`。

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**功能說明**：連接 Azure DevOps 服務，提供完整的專案管理、工作項目追蹤、建置管線管理與倉庫操作功能。

**為什麼有用**：對於以 Azure DevOps 作為主要 DevOps 平台的團隊，這個 MCP 伺服器能消除在開發環境與 Azure DevOps 網頁介面間頻繁切換的困擾。你可以直接從 AI 助手管理工作項目、查看建置狀態、查詢倉庫，並處理專案管理任務。

**實際應用範例**：「顯示 WebApp 專案目前 sprint 中所有活躍的工作項目」、「為我剛發現的登入問題建立錯誤報告」，或「檢查我們建置管線狀態並顯示最近的失敗」

**特色範例**：你可以輕鬆查詢團隊目前 sprint 狀態，只要簡單輸入「顯示 WebApp 專案目前 sprint 中所有活躍的工作項目」或「為我剛發現的登入問題建立錯誤報告」，完全不需離開開發環境。

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**功能說明**：MarkItDown 是一個全面的文件轉換伺服器，能將多種檔案格式轉換成高品質的 Markdown，並針對大型語言模型（LLM）使用及文本分析流程進行優化。

**為什麼有用**：現代文件工作流程的必備工具！MarkItDown 支援多種檔案格式，並保留重要的文件結構，如標題、清單、表格和連結。與簡單的文字擷取工具不同，它著重於維持語意和格式，對 AI 處理和人類閱讀都非常有價值。

**支援的檔案格式**：
- **Office 文件**：PDF、PowerPoint (PPTX)、Word (DOCX)、Excel (XLSX/XLS)
- **多媒體檔案**：圖片（含 EXIF 資料及 OCR）、音訊（含 EXIF 資料及語音轉錄）
- **網頁內容**：HTML、RSS 訂閱源、YouTube 連結、維基百科頁面
- **資料格式**：CSV、JSON、XML、ZIP 檔（遞迴處理內容）
- **出版格式**：EPub、Jupyter 筆記本 (.ipynb)
- **電子郵件**：Outlook 郵件 (.msg)
- **進階功能**：整合 Azure Document Intelligence 以強化 PDF 處理

**進階功能**：MarkItDown 支援利用 LLM 生成圖片描述（需提供 OpenAI 用戶端）、Azure Document Intelligence 強化 PDF 處理、語音內容轉錄，以及可擴充的外掛系統以支援更多檔案格式。

**實際應用**：「將這份 PowerPoint 簡報轉成 Markdown 用於我們的文件網站」、「從這份 PDF 擷取文字並保留正確的標題結構」、或「把這份 Excel 試算表轉成易讀的表格格式」。

**特色範例**：引用 [MarkItDown 文件](https://github.com/microsoft/markitdown#why-markdown)：

> Markdown 非常接近純文字，只有最少的標記或格式，但仍能表達重要的文件結構。主流大型語言模型，如 OpenAI 的 GPT-4o，天生「懂得」Markdown，且經常在回應中自動使用 Markdown。這表示它們已經訓練於大量 Markdown 格式的文本，並且理解它。附帶好處是，Markdown 的慣例也非常節省 token。

MarkItDown 非常擅長保留文件結構，這對 AI 工作流程至關重要。例如，轉換 PowerPoint 簡報時，它會保留投影片的組織結構與正確的標題，將表格轉成 Markdown 表格，包含圖片的替代文字，甚至處理講者備註。圖表會轉成易讀的資料表格，產出的 Markdown 保持原始簡報的邏輯流程。這使得它非常適合將簡報內容輸入 AI 系統或從現有投影片建立文件。

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**功能說明**：提供對 SQL Server 資料庫（本地端、Azure SQL 或 Fabric）的對話式存取。

**為什麼有用**：類似 PostgreSQL 伺服器，但專為 Microsoft SQL 生態系設計。只需簡單的連線字串，即可用自然語言查詢資料庫，免去切換上下文的麻煩！

**實際應用**：「找出過去 30 天內尚未完成的所有訂單」會被轉換成適當的 SQL 查詢並回傳格式化結果。

**特色範例**：設定好資料庫連線後，即可立即開始與資料對話。官方部落格以簡單問題示範：「你連接的是哪個資料庫？」MCP 伺服器會呼叫相應的資料庫工具，連接到 SQL Server 實例，並回傳目前資料庫連線的詳細資訊——全程不需撰寫任何 SQL。此伺服器支援從架構管理到資料操作的完整資料庫作業，全部透過自然語言指令完成。完整設定說明及 VS Code 與 Claude Desktop 範例，請參考：[Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)。

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**功能說明**：讓 AI 代理能與網頁互動，用於測試與自動化。

> **ℹ️ 支援 GitHub Copilot**
> 
> Playwright MCP Server 是 GitHub Copilot 編碼代理的動力來源，賦予它瀏覽網頁的能力！[了解更多此功能](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

**為什麼有用**：非常適合以自然語言描述驅動的自動化測試。AI 可以瀏覽網站、填寫表單，並透過結構化的無障礙快照擷取資料——這功能非常強大！

**實際應用**：「測試登入流程並確認儀表板正確載入」或「產生一個測試，搜尋產品並驗證結果頁面」——全程不需應用程式原始碼。

**特色範例**：我的同事 Debbie O'Brien 最近在 Playwright MCP Server 上做了很棒的工作！例如，她展示了如何在完全不接觸應用程式原始碼的情況下，產生完整的 Playwright 測試。在她的案例中，她請 Copilot 為一個電影搜尋應用程式建立測試：瀏覽網站、搜尋「Garfield」，並驗證電影是否出現在結果中。MCP 啟動瀏覽器會話，利用 DOM 快照探索頁面結構，找出正確的選擇器，並產生一個完全可用的 TypeScript 測試，且第一次執行就通過。

這項技術的強大之處在於它架起了自然語言指令與可執行測試程式碼之間的橋樑。傳統方法需要手動撰寫測試或取得程式碼庫以取得上下文，但 Playwright MCP 讓你能測試外部網站、客戶端應用程式，或在無法取得程式碼的黑盒測試場景中工作。

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**功能說明**：透過自然語言管理 Microsoft Dev Box 環境。

**為什麼有用**：大幅簡化開發環境管理！無需記憶複雜指令，即可建立、設定及管理開發環境。

**實際應用**：「建立一個搭載最新 .NET SDK 的 Dev Box，並為我們的專案進行設定」、「查看我所有開發環境的狀態」，或「為團隊簡報建立標準化的示範環境」。

**特色範例**：我非常喜歡用 Dev Box 進行個人開發。James Montemagno 曾分享 Dev Box 在會議示範上的優勢，因為它不論在會議、飯店或飛機上的 Wi-Fi 狀況如何，都有超快的乙太網路連線。事實上，我最近在從布魯日到安特衛普的巴士上，透過手機熱點連線筆電練習會議示範！接下來我想深入研究團隊多開發環境管理及標準化示範環境。當然，客戶和同事也常提到 Dev Box 用於預先配置的開發環境。在這兩種情況下，使用 MCP 來設定和管理 Dev Box，讓你能用自然語言互動，且全程待在開發環境中。

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**功能說明**：Azure AI Foundry MCP Server 為開發者提供全面存取 Azure AI 生態系的能力，包括模型目錄、部署管理、結合 Azure AI Search 的知識索引，以及評估工具。這個實驗性伺服器架起 AI 開發與 Azure 強大 AI 基礎設施之間的橋樑，讓建立、部署及評估 AI 應用變得更簡單。

**為何有用**：此伺服器改變了您使用 Azure AI 服務的方式，將企業級 AI 功能直接帶入開發流程。您不必在 Azure 入口網站、文件與 IDE 間切換，就能透過自然語言指令探索模型、部署服務、管理知識庫及評估 AI 表現。對於開發 RAG（檢索增強生成）應用、多模型部署管理或實作完整 AI 評估流程的開發者尤其強大。

**主要開發者功能**：
- **🔍 模型探索與部署**：瀏覽 Azure AI Foundry 的模型目錄，取得詳細模型資訊與程式碼範例，並部署模型至 Azure AI 服務
- **📚 知識管理**：建立與管理 Azure AI Search 索引，新增文件、設定索引器，打造複雜的 RAG 系統
- **⚡ AI 代理整合**：連接 Azure AI Agents，查詢現有代理，並在生產環境中評估代理效能
- **📊 評估框架**：執行完整的文字與代理評估，產生 markdown 報告，實施 AI 應用的品質保證
- **🚀 原型工具**：提供基於 GitHub 的原型設置指引，並存取 Azure AI Foundry Labs 的前沿研究模型

**實際開發者使用案例**：「將 Phi-4 模型部署到 Azure AI 服務供我的應用使用」、「為我的文件 RAG 系統建立新的搜尋索引」、「根據品質指標評估我的代理回應」，或「尋找適合我複雜分析任務的最佳推理模型」

**完整示範場景**：以下是一個強大的 AI 開發工作流程：

> 「我正在打造一個客戶支援代理。幫我從目錄中找到一個優秀的推理模型，部署到 Azure AI 服務，從我們的文件建立知識庫，設置評估框架來測試回應品質，然後協助我用 GitHub token 進行整合原型測試。」

Azure AI Foundry MCP Server 將會：
- 根據您的需求查詢模型目錄，推薦最佳推理模型
- 提供部署指令與您偏好 Azure 區域的配額資訊
- 為您的文件設置適當結構的 Azure AI Search 索引
- 配置包含品質指標與安全檢查的評估流程
- 產生帶有 GitHub 認證的原型程式碼，立即進行測試
- 提供針對您技術棧量身打造的完整設置指南

**特色範例**：作為開發者，我一直難以掌握眾多 LLM 模型。雖然知道幾個主要模型，但總覺得錯過了提升生產力與效率的機會。代幣與配額管理也讓人壓力山大，常常不確定是否選對模型或浪費預算。最近在和團隊討論 MCP Server 推薦時，從 James Montemagno 那裡聽說了這個 MCP Server，迫不及待想試用！模型探索功能對像我這種想跳脫常見模型、尋找針對特定任務優化模型的人來說特別吸引。評估框架則能幫助我驗證是否真的獲得更好結果，而不只是嘗試新東西。

> **ℹ️ 實驗性狀態**
> 
> 此 MCP 伺服器仍屬實驗階段，且持續開發中。功能與 API 可能會變動。非常適合探索 Azure AI 能力與建立原型，但用於生產環境前請確認穩定性需求。

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**功能說明**：為開發者提供建構整合 Microsoft 365 與 Microsoft 365 Copilot 的 AI 代理與應用所需的基本工具，包括結構驗證、範例程式碼檢索與故障排除協助。

**為何有用**：針對 Microsoft 365 與 Copilot 的開發涉及複雜的宣告式結構與特定開發模式。此 MCP 伺服器將重要的開發資源直接帶入您的編碼環境，幫助您驗證結構、尋找範例程式碼，並解決常見問題，無需頻繁查閱文件。

**實際使用案例**：「驗證我的宣告式代理清單並修正結構錯誤」、「展示實作 Microsoft Graph API 外掛的範例程式碼」，或「協助我排解 Teams 應用的認證問題」

**特色範例**：我在 Build 大會與朋友 John Miller 聊到 M365 Agents，他推薦了這個 MCP。對於剛接觸 M365 Agents 的開發者來說非常適合，因為它提供範本、範例程式碼與腳手架，讓你不用被文件淹沒就能快速上手。結構驗證功能尤其有用，能避免因清單結構錯誤而浪費數小時除錯。

> **💡 專家小提示**
> 
> 建議搭配 Microsoft Learn Docs MCP Server 一起使用，提供完整的 M365 開發支援——一個提供官方文件，另一個則提供實用的開發工具與故障排除協助。

## 下一步？🔮

## 📋 結論

Model Context Protocol (MCP) 正在改變開發者與 AI 助手及外部工具互動的方式。這 10 個 Microsoft MCP 伺服器展示了標準化 AI 整合的強大力量，讓開發者能在專注開發的同時，無縫存取強大的外部功能。

從完整的 Azure 生態系整合，到專門用於瀏覽器自動化的 Playwright 及文件處理的 MarkItDown，這些伺服器展現 MCP 如何提升多元開發場景的生產力。標準化協議確保這些工具能協同運作，打造一致且流暢的開發體驗。

隨著 MCP 生態系持續演進，積極參與社群、探索新伺服器並打造自訂解決方案，將是提升開發效率的關鍵。MCP 的開放標準特性讓您能混合使用不同廠商的工具，打造最適合您需求的工作流程。

## 🔗 其他資源

- [官方 Microsoft MCP 倉庫](https://github.com/microsoft/mcp)
- [MCP 社群與文件](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 文件](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 文件](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 文件](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 活動](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 7/29-30 或隨選觀看](https://aka.ms/mcpdevdays)

## 🎯 練習題

1. **安裝與設定**：在您的 VS Code 環境中安裝一個 MCP 伺服器並測試基本功能。
2. **工作流程整合**：設計一個結合至少三個不同 MCP 伺服器的開發工作流程。
3. **自訂伺服器規劃**：找出日常開發中可受益於自訂 MCP 伺服器的任務，並撰寫規格。
4. **效能分析**：比較使用 MCP 伺服器與傳統方法執行常見開發任務的效率。
5. **安全評估**：評估在開發環境中使用 MCP 伺服器的安全性影響，並提出最佳實踐建議。

Next:[Best Practices](../08-BestPractices/README.md)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
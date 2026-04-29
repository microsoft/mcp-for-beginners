# 變更記錄：MCP 初學者課程

此文件用於記錄對 Model Context Protocol (MCP) 初學者課程所做的所有重大變更。變更以逆時間順序記錄（最新變更優先）。

## 2026年4月11日

### 新課程、文件修正及依賴更新

#### 新增課程內容

**模組 05 - 進階主題**  
- **課程 5.17：使用 MCP 的對抗式多代理推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`)：全新綜合指南涵蓋多代理系統中對抗式辯論模式  
  - Mermaid 架構圖：兩位代理 → 共享 MCP 伺服器 → 辯論記錄 → 評判 → 裁決  
  - 以 Python 和 TypeScript 實作的共享 MCP 工具伺服器（`web_search` + `run_python`）  
  - 對立系統提示（贊成 / 反對 / 評判）並附帶明確的工具使用要求  
  - 以 Python、TypeScript 和 C# 實作的辯論協調器，管理回合與論點路由  
  - MCP `ClientSession` 對協調器連接至實際工具呼叫  
  - 用例表（幻覺檢測、威脅建模、API 設計審查、事實驗證、技術選型）  
  - 安全性考量：沙盒執行、工具呼叫驗證、速率限制、審計日誌  
  - 結構化練習含三個實務場景（程式碼審查、架構決策、內容審核）

#### 文件修正

**模組 03 - 入門**  
- **05-stdio-server/README.md**：修正未完成的 TypeScript stdio 伺服器範例 — 補充缺少的傳輸實例化(`new StdioServerTransport()`)及 `server.connect(transport)` 呼叫，與同節 Python 與 .NET 範例一致  
- **14-sampling/README.md**：修正錯字 — 將 `"Sampling is an davanced features"` 改為 `"Sampling is an advanced feature"`

#### 課程更新

**主 README.md**  
- 新增條目 5.17（使用 MCP 的對抗式多代理推理）於課程表中，並附直接連結至新課程

**05-AdvancedTopics/README.md**  
- 於課程列表新增第 5.17 課程行

**study_guide.md**  
- 於心智圖及進階主題段落中新增對抗式多代理推理主題

#### 程式碼與安全修正

**模組 05 - 對抗代理 (`mcp-adversarial-agents`)**  
- **安全修正 — 命令注入**：在 TypeScript `run_python` 工具中，替換 `execSync` shell 插值為 `execFile` + `promisify`，消除命令注入風險（LLM 控制的程式碼現以純文字 argv 元素傳遞，完全不通過 shell）  
- **MCP 工具迴圈繫結**：更新 Python 辯論協調器使用非阻塞 `AsyncAnthropic` 用戶端，直接將活躍 `ClientSession` 傳遞至每回合代理，調用 `session.list_tools()` 獲取工具定義，並通過 `session.call_tool()` 循環傳送 `tool_use` 區塊直到模型輸出最終文字回應

#### 依賴更新

- 多個套件（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中將 `hono` 升級至 4.12.12  
- TypeScript 套件中將 `@hono/node-server` 自 1.19.11 升至 1.19.13  
- Python 套件（10-StreamliningAIWorkflows 實驗 3 和 4）中將 `cryptography` 自 46.0.5 升至 46.0.7  
- 於 10-StreamliningAIWorkflows inspector 中將 `lodash` 自 4.17.23 升至 4.18.1

#### 翻譯

- 同步翻譯 48+ 種語言，更新至最新原始碼更動 (i18n 更新)

---

## 2026年2月5日

### 全倉庫驗證與導覽改進

#### 新增課程內容

**模組 03 - 入門**  
- **12-mcp-hosts/README.md**：全新 MCP 主機設定指南  
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置範例  
  - 主要主機 JSON 配置範本  
  - 傳輸類型比較表（stdio、SSE/HTTP、WebSocket）  
  - 常見連線問題排解  
  - 主機配置安全最佳實踐

- **13-mcp-inspector/README.md**：MCP Inspector 除錯指南  
  - 安裝方法（npx、全局 npm、原始碼）  
  - 透過 stdio 與 HTTP/SSE 連接伺服器  
  - 測試工具、資源及提示工作流程  
  - VS Code 與 MCP Inspector 整合  
  - 常見除錯場景與解決方案

**模組 04 - 實務應用**  
- **pagination/README.md**：新分頁實作指南  
  - Python、TypeScript、Java 的游標分頁模式  
  - 用戶端分頁處理  
  - 游標設計策略（不透明 vs 結構化）  
  - 效能優化建議

**模組 05 - 進階主題**  
- **mcp-protocol-features/README.md**：協定功能深度探討  
  - 進度通知實作  
  - 請求取消模式  
  - 具 URI 模板的資源範本  
  - 伺服器生命週期管理  
  - 日誌等級控制  
  - 帶 JSON-RPC 碼的錯誤處理模式

#### 導覽修正（更新 24+ 檔案）

**主模組 README 檔**  
- 現在連結同時指向該模組第一課和下一模組

**02-Security 子檔案**  
- 5 份安全補充文件新增“接下來做什麼”導覽

**09-CaseStudy 檔案**  
- 全部案例研究檔案新增順序導覽

**10-StreamliningAI 實驗室**  
- 對模組 10 總覽及模組 11 新增“接下來做什麼”部分

#### 程式碼與內容修正

**SDK 及依賴更新**  
- 空白的 openai 版本指向 `^4.95.0`  
- 將 SDK 從 `^1.8.0` 更新為 `>=1.26.0`  
- 將 MCP 版本要求更新為 `>=1.26.0`

<strong>程式碼修正</strong>  
- 修正無效模型 `gpt-4o-mini` 為 `gpt-4.1-mini`

<strong>內容修正</strong>  
- 修正壞連結 `READMEmd` 為 `README.md`，修正課程標題 `Module 1-3` 為 `Module 0-3`，修正大小寫路徑  
- 移除損壞重複的案例研究 5 內容

<strong>初學者指引改進</strong>  
- 新增合適的介紹、學習目標和先決條件

#### 課程更新

**主 README.md**  
- 新增條目 3.12（MCP 主機）、3.13（MCP Inspector）、4.1（分頁）、5.16（協定功能）至課程表

**模組 README**  
- 新增第 12 和 13 課至課程列表  
- 新增實務指南部分並加入分頁連結  
- 新增 5.15 課（自訂傳輸）和 5.16 課（協定功能）

**study_guide.md**  
- 更新心智圖涵蓋所有新主題：MCP 主機設定、MCP Inspector、分頁策略、協定功能深度探討

## 2026年1月28日

### MCP 規格 2025-11-25 合規性檢視

#### 核心概念強化 (01-CoreConcepts/)  
- **新客戶端原語 - Roots**：新增詳細文件，說明 Roots 客戶端原語，協助伺服器理解檔案系統界限和存取權限  
- <strong>工具行為註解</strong>：新增工具行為註解文件（`readOnlyHint`、`destructiveHint`），提升工具執行決策  
- <strong>取樣中工具呼叫</strong>：更新取樣文件，包含 `tools` 和 `toolChoice` 參數實現模型驅動工具呼叫  
- **URL 模式引導**：新增文件，說明伺服器啟動外部網路互動的 URL 取樣引導  
- **任務 (實驗性)**：新增章節記錄實驗性 Tasks 功能，用於持久執行包裝及延遲結果檢索  
- <strong>圖示支援</strong>：指出工具、資源、資源範本和提示現在可附加圖示作為額外元資料

#### 文件更新  
- **README.md**：新增 MCP 規格 2025-11-25 版本參考及基於日期的版本控制說明  
- **study_guide.md**：更新課程地圖，將 Tasks 與工具註解列入核心概念部分；更新文件時間戳記

#### 規格合規驗證  
- <strong>協定版本</strong>：核驗所有文件均使用最新 MCP 規格 2025-11-25  
- <strong>架構一致性</strong>：確認雙層架構（資料層 + 傳輸層）文件正確性  
- <strong>原語文件</strong>：驗證伺服器原語（資源、提示、工具）和客戶端原語（取樣、引導、日誌、Roots）文件完整  
- <strong>傳輸機制</strong>：核實 STDIO 與可串流 HTTP 傳輸相關文件正確  
- <strong>安全指引</strong>：確認符合現行 MCP 安全最佳實踐文件

#### MCP 2025-11-25 主要功能紀錄  
- **OpenID Connect 探索**：認證伺服器透過 OIDC 探索  
- **OAuth 用戶端 ID 元資料文檔**：推薦的用戶端註冊機制  
- **JSON Schema 2020-12**：MCP 架構定義的預設方言  
- **SDK 分級系統**：正式化 SDK 功能支援與維護要求  
- <strong>治理架構</strong>：正式化 MCP 工作組與利益群組治理

### 安全文件重大更新 (02-Security/)

#### MCP 安全峰會工作坊 (Sherpa) 整合  
- <strong>全新實作訓練資源</strong>：將 [MCP 安全峰會工作坊（Sherpa）](https://azure-samples.github.io/sherpa/) 全面整合於所有安全文件  
- <strong>探索路線涵蓋</strong>：詳述從大本營至峰頂的完整營地進度  
- **OWASP 對應**：所有安全指南均映射至 OWASP MCP Azure 安全指導風險

#### OWASP MCP 十大安全風險整合  
- <strong>新章節</strong>：在主安全 README 文件中新增 OWASP MCP 十大安全風險表格及 Azure 緩解措施  
- <strong>風險導向文件</strong>：在 mcp-security-controls-2025.md 中加入 OWASP MCP 風險引用，涵蓋各安全領域  
- <strong>參考架構</strong>：連結至 OWASP MCP Azure 安全指導參考架構與實作模式

#### 安全文件更新  
- **README.md**：新增 Sherpa 工作坊概觀、探索路線表、OWASP MCP 十大風險摘要及實作訓練區段  
- **mcp-security-controls-2025.md**：將標頭更新至 2026 年 2 月，增加 OWASP 風險標識（MCP01-MCP08），修正規格版本不一致問題  
- **mcp-security-best-practices-2025.md**：新增 Sherpa 及 OWASP 資源區，更新時間戳記  
- **mcp-best-practices.md**：新增含 Sherpa 和 OWASP 連結的實作訓練區  
- **azure-content-safety-implementation.md**：新增 OWASP MCP06 參考，對應 Sherpa 第三營地及額外資源區

#### 新增資源連結  
- [MCP 安全峰會工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure 安全指導](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP 十大](https://owasp.org/www-project-mcp-top-10/)  
- 個別 OWASP MCP 風險頁面（MCP01-MCP10）

### 全課程 MCP 規格 2025-11-25 對齊

#### 模組 03 - 入門  
- **SDK 文件**：將 Go SDK 加入官方 SDK 列表，並將所有 SDK 參考更新為與 MCP 規格 2025-11-25 對齊  
- <strong>傳輸說明</strong>：更新 STDIO 和 HTTP 流傳輸說明，明確加入規格參考

#### 模組 04 - 實務應用  
- **SDK 更新**：新增 Go SDK，更新 SDK 列表及規格版本參考  
- <strong>授權規格</strong>：更新 MCP 授權規格連結為最新 2025-11-25 版本

#### 模組 05 - 進階主題  
- <strong>新功能</strong>：新增有關 MCP 規格 2025-11-25 新功能註解（Tasks、工具註解、URL 模式引導、Roots）  
- <strong>安全資源</strong>：新增 OWASP MCP 十大與 Sherpa 工作坊連結於附加資源

#### 模組 06 - 社群貢獻  
- **SDK 列表**：新增 Swift 和 Rust SDK，更新規格連結為 2025-11-25  
- <strong>規格參考</strong>：更新 MCP 規格連結為官方規格 URL

#### 模組 07 - 早期採用教訓  
- <strong>資源更新</strong>：新增 MCP 規格 2025-11-25 及 OWASP MCP 十大於附加資源

#### 模組 08 - 最佳實踐  
- <strong>規格版本</strong>：更新 MCP 規格參考至 2025-11-25  
- <strong>安全資源</strong>：新增 OWASP MCP 十大和 Sherpa 工作坊於附加參考

#### 模組 10 - 簡化 AI 工作流程  
- <strong>徽章更新</strong>：將 MCP 版本徽章從 SDK 版本（1.9.3）改為規格版本（2025-11-25）  
- <strong>資源連結</strong>：更新 MCP 規格連結，新增 OWASP MCP 十大

#### 模組 11 - MCP 伺服器實作實驗室  
- <strong>規格參考</strong>：更新 MCP 規格連結至 2025-11-25 版本  
- <strong>安全資源</strong>：新增 OWASP MCP 十大於官方資源

## 2025年12月18日
### 安全文件更新 - MCP 規範 2025-11-25

#### MCP 安全最佳實務 (02-Security/mcp-best-practices.md) - 規範版本更新
- <strong>協議版本更新</strong>：更新以參考最新 MCP 規範 2025-11-25（於 2025 年 11 月 25 日發布）
  - 將所有規範版本參考從 2025-06-18 更新至 2025-11-25
  - 將文件日期參考從 2025 年 8 月 18 日更新至 2025 年 12 月 18 日
  - 驗證所有規範 URL 均指向當前文件
- <strong>內容驗證</strong>：全面驗證安全最佳實務與最新標準的一致性
  - **Microsoft 安全解決方案**：驗證 Prompt Shields（先前稱為 「Jailbreak 風險偵測」）、Azure Content Safety、Microsoft Entra ID 及 Azure Key Vault 的現行術語與連結
  - **OAuth 2.1 安全性**：確認符合最新 OAuth 安全最佳實務
  - **OWASP 標準**：驗證 LLMs 相關的 OWASP Top 10 參考保持最新
  - **Azure 服務**：驗證所有 Microsoft Azure 文件連結與最佳實務
- <strong>標準對齊</strong>：確認所有引用的安全標準為最新版本
  - NIST AI 風險管理架構
  - ISO 27001:2022
  - OAuth 2.1 安全最佳實務
  - Azure 安全與合規架構
- <strong>實作資源</strong>：驗證所有實作指引連結與資源
  - Azure API 管理身分驗證模式
  - Microsoft Entra ID 整合指南
  - Azure Key Vault 秘密管理
  - DevSecOps 管線及監控解決方案

### 文檔品質保證
- <strong>規範遵循</strong>：確保所有強制 MCP 安全要求（MUST/MUST NOT）符合最新規範
- <strong>資源時效性</strong>：驗證所有外部連結至 Microsoft 文檔、安全標準及實作指南
- <strong>最佳實務覆蓋範圍</strong>：確認全面涵蓋身分驗證、授權、AI 特定威脅、供應鏈安全與企業模式

## 2025 年 10 月 6 日

### 入門章節擴充 – 進階伺服器使用與簡易身分驗證

#### 進階伺服器使用 (03-GettingStarted/10-advanced)
- <strong>新增章節</strong>：介紹完整進階 MCP 伺服器使用指南，涵蓋一般與底層伺服器架構
  - <strong>一般伺服器與底層伺服器比較</strong>：提供 Python 和 TypeScript 範例詳細比較兩種方式
  - **基於 Handler 的設計**：說明基於 handler 的工具/資源/Prompt 管理，用於擴展且彈性的伺服器實作
  - <strong>實務範例模式</strong>：介紹底層伺服器模式在進階功能與架構中的應用場景

#### 簡易身分驗證 (03-GettingStarted/11-simple-auth)
- <strong>新增章節</strong>：逐步說明如何於 MCP 伺服器中實作簡易身分驗證
  - <strong>身分驗證概念</strong>：清楚解釋認證與授權，以及憑證處理
  - <strong>基本認證實作</strong>：Python（Starlette）與 TypeScript（Express）中基於中間件的認證模式與程式碼範例
  - <strong>向進階安全的過渡</strong>：指導如何從簡易認證進階到 OAuth 2.1 及 RBAC，並參考進階安全模組

這些新增內容提供實務操作指引，有助建立更穩健、安全且彈性的 MCP 伺服器實作，串接基礎概念與生產環境進階模式。

## 2025 年 9 月 29 日

### MCP 伺服器資料庫整合實作實驗室 - 完整實作學習路徑

#### 11-MCPServerHandsOnLabs - 全面資料庫整合課程
- **完整 13 個實驗室學習路徑**：新增涵蓋 PostgreSQL 資料庫整合的生產就緒 MCP 伺服器實務課程
  - <strong>實務案例</strong>：以 Zava Retail 分析應用展示企業級模式
  - <strong>結構化學習進程</strong>：
    - **實驗室 00-03：基礎** - 介紹、核心架構、安全與多租戶、環境設置
    - **實驗室 04-06：構建 MCP 伺服器** - 資料庫設計與架構、MCP 伺服器實作、工具開發
    - **實驗室 07-09：進階功能** - 語意搜尋整合、測試與除錯、VS Code 整合
    - **實驗室 10-12：生產環境與最佳實務** - 部署策略、監控與可觀測性、最佳實務與優化
  - <strong>企業技術</strong>：FastMCP 框架、帶有 pgvector 的 PostgreSQL、Azure OpenAI 向量嵌入、Azure Container Apps、Application Insights
  - <strong>進階功能</strong>：列級安全性 (RLS)、語意搜尋、多租戶資料存取、向量嵌入、實時監控

#### 術語標準化 - 模組改稱實驗室
- <strong>文檔全面更新</strong>：系統化更新 11-MCPServerHandsOnLabs 內所有 README 檔案採用「實驗室」術語取代「模組」
  - <strong>章節標題</strong>：全部 13 個實驗室將「本模組內容涵蓋」更改為「本實驗室內容涵蓋」
  - <strong>內容描述</strong>：全篇「本模組提供……」更改為「本實驗室提供……」
  - <strong>學習目標</strong>：將「本模組結束時……」更新為「本實驗室結束時……」
  - <strong>導航連結</strong>：所有「Module XX」改為「Lab XX」
  - <strong>完成追蹤</strong>：「完成本模組後……」更新為「完成本實驗室後……」
  - <strong>保留技術參考</strong>：維持 Python 模組引用於設定檔（如 `"module": "mcp_server.main"`）

#### 學習指南強化 (study_guide.md)
- <strong>視覺化課程地圖</strong>：新增「11. 資料庫整合實驗室」章節，完整呈現實驗室架構
- <strong>資料庫結構</strong>：由十個主區段更新為十一個，詳細描述 11-MCPServerHandsOnLabs
- <strong>學習路徑指引</strong>：增強導航指示，涵蓋 00-11 個區段
- <strong>技術覆蓋</strong>：加入 FastMCP、PostgreSQL、Azure 服務整合細節
- <strong>學習成效</strong>：強調生產就緒伺服器開發、資料庫整合模式及企業安全

#### 主要 README 結構優化
- <strong>基於實驗室的術語</strong>：更新 11-MCPServerHandsOnLabs 主要 README.md，保持一致性使用「實驗室」結構
- <strong>學習路徑組織</strong>：清楚從基礎概念到進階實作再到生產部署的學習進程
- <strong>實務聚焦</strong>：強調企業級實作與技術，重視實務動手操作

### 文件品質與一致性改進
- <strong>重視實務學習</strong>：文檔中全程強化以實驗室為核心的動手學習方式
- <strong>企業模式聚焦</strong>：凸顯生產就緒實作與企業安全考量
- <strong>技術整合</strong>：完整涵蓋現代 Azure 服務與 AI 整合模式
- <strong>學習進度清晰</strong>：結構化路徑從初階到生產部署清楚明確

## 2025 年 9 月 26 日

### 案例研究強化 - GitHub MCP Registry 整合

#### 案例研究 (09-CaseStudy/) - 生態系統發展聚焦
- **README.md**：大幅擴充，新增完整 GitHub MCP Registry 案例研究
  - **GitHub MCP Registry 案例研究**：詳細探討 2025 年 9 月發布的 GitHub MCP Registry
    - <strong>問題分析</strong>：深入檢視 MCP 伺服器發現與部署碎片化挑戰
    - <strong>解決方案架構</strong>：GitHub 集中式登錄平台，支援一鍵式 VS Code 安裝
    - <strong>商業影響</strong>：衡量在開發者導入與生產力上的提升
    - <strong>策略價值</strong>：聚焦模組化代理部署與跨工具互操作性
    - <strong>生態系統發展</strong>：作為代理整合基礎平台的定位
  - <strong>完善案例結構</strong>：更新七個案例研究保持一致格式與完整敘述
    - Azure AI 旅遊代理：多代理協同重點
    - Azure DevOps 整合：流程自動化聚焦
    - 即時文件檢索：Python 控制台客戶端實作
    - 互動式學習計劃產生器：Chainlit 會話式網頁應用
    - 編輯器內文件：VS Code 與 GitHub Copilot 整合
    - Azure API 管理：企業 API 整合模式
    - GitHub MCP Registry：生態系統開發與社群平台
  - <strong>全面結論重寫</strong>：強調涵蓋七個案例研究、多樣 MCP 實作維度
    - 企業整合、多代理協同、開發者生產力
    - 生態系統發展、教育應用分類
    - 加強架構模式、實作策略與最佳實務洞見
    - 強調 MCP 為成熟生產協議

#### 學習指南更新 (study_guide.md)
- <strong>視覺化課程地圖</strong>：更新心智圖包含 GitHub MCP Registry 在案例研究章節
- <strong>案例研究描述</strong>：由一般描述提升為七個全面案例研究詳細說明
- <strong>資料庫結構</strong>：更新第 10 單元反映案例研究全貌與細節
- <strong>變更日誌整合</strong>：新增 2025 年 9 月 26 日條目，記錄 GitHub MCP Registry 新增及案例強化
- <strong>日期更新</strong>：更新頁腳時間戳記為最新修訂（2025 年 9 月 26 日）

### 文件品質改進
- <strong>一致性強化</strong>：標準化七個案例研究的格式和結構
- <strong>全面性覆蓋</strong>：案例涵蓋企業、開發生產力及生態系統場景
- <strong>策略定位</strong>：強調 MCP 作為代理系統部署的基礎平台
- <strong>資源整合</strong>：更新額外資源包含 GitHub MCP Registry 連結

## 2025 年 9 月 15 日

### 進階主題擴充 - 客製化傳輸與上下文工程

#### MCP 客製化傳輸 (05-AdvancedTopics/mcp-transport/) - 進階實作完整指南
- **README.md**：完整客製 MCP 傳輸機制實作指導
  - **Azure Event Grid 傳輸**：詳盡無伺服器事件驅動傳輸實作
    - C#、TypeScript 與 Python 範例含 Azure Functions 整合
    - 事件驅動架構模式用於擴展 MCP 解決方案
    - Webhook 接收器及推送式訊息處理
  - **Azure Event Hubs 傳輸**：高吞吐量串流傳輸實作
    - 即時串流能力支援低延遲場景
    - 分區策略與檢查點管理
    - 訊息批次及效能最佳化
  - <strong>企業整合模式</strong>：生產就緒架構範例
    - 跨多個 Azure Functions 的分散式 MCP 處理
    - 多重傳輸類型混合架構
    - 訊息持久化、可靠性與錯誤處理策略
  - <strong>安全與監控</strong>：Azure Key Vault 整合與可觀測性模式
    - 管理身分驗證與最小權限存取
    - Application Insights 遙測及效能監控
    - 斷路器與容錯模式
  - <strong>測試框架</strong>：完整測試策略
    - 使用測試雙替身與模擬框架的單元測試
    - Azure 測試容器的整合測試
    - 效能與負載測試考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新興 AI 領域
- **README.md**：全面探索上下文工程之新興領域
  - <strong>核心原理</strong>：完整上下文共享、行動決策知覺與上下文視窗管理
  - **MCP 協議對應**：MCP 設計如何解決上下文工程挑戰
    - 上下文視窗限制與漸進式載入策略
    - 相關性判斷與動態上下文檢索
    - 多模態上下文處理與安全考量
  - <strong>實作方法</strong>：單線程與多代理架構
    - 上下文分塊與優先管理技巧
    - 漸進式上載與壓縮策略
    - 層次化上下文方法與檢索優化
  - <strong>衡量框架</strong>：新興上下文效能度量指標
    - 輸入效率、效能、品質與使用者體驗考量
    - 上下文優化之實驗性方法
    - 失效分析與改進方法

#### 課程導覽更新 (README.md)
- <strong>強化模組結構</strong>：更新課程表新增進階主題
  - 加入上下文工程 (5.14) 與客製傳輸 (5.15)
  - 模組格式與導航連結一致
  - 更新描述反映目前內容範圍

### 目錄結構改進
- <strong>命名標準化</strong>：「mcp transport」改名為「mcp-transport」，與其他進階主題資料夾一致
- <strong>內容組織</strong>：所有 05-AdvancedTopics 資料夾統一遵循 mcp-[主題] 命名模式

### 文件品質提升
- **MCP 規範對齊**：所有新內容均參考 MCP 規範 2025-06-18
- <strong>多語言範例</strong>：完整 C#、TypeScript 與 Python 範例
- <strong>企業聚焦</strong>：全程生產就緒模式與 Azure 雲端整合
- <strong>視覺文件</strong>：使用 Mermaid 圖表呈現架構與流程

## 2025 年 8 月 18 日

### 文件全面更新 - MCP 2025-06-18 標準

#### MCP 安全最佳實務 (02-Security/) - 完整現代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：完全重寫，符合 MCP 規範 2025-06-18  
  - <strong>強制性要求</strong>：新增官方規範中的明確 MUST/MUST NOT 要求並附加明確視覺指示  
  - **12 核心安全實務**：從 15 項清單重組為全面安全領域  
    - Token 安全與驗證，與外部身份提供者整合  
    - 工作階段管理與傳輸安全，具密碼學要求  
    - AI 專屬威脅防護，整合 Microsoft Prompt Shields  
    - 存取控制與權限，遵循最小權限原則  
    - 內容安全與監控，整合 Azure Content Safety  
    - 供應鏈安全，全面元件驗證  
    - OAuth 安全與混淆代理防護，具 PKCE 實作  
    - 事件响应與復原，自動化能力  
    - 合規性與治理，符合法規要求  
    - 進階安全控制，零信任架構  
    - Microsoft 安全生態系統整合，全面解決方案  
    - 持續安全演進，採用適應性實務  
  - **Microsoft 安全解決方案**：加強 Prompt Shields、Azure Content Safety、Entra ID 與 GitHub Advanced Security 的整合指導  
  - <strong>實作資源</strong>：依官方 MCP 文件、Microsoft 安全解決方案、安全標準與實作指引分類完整資源連結  

#### 進階安全控制 (02-Security/) — 企業實作  
- **MCP-SECURITY-CONTROLS-2025.md**：全面改造為企業級安全框架  
  - **9 個綜合安全領域**：從基本控管擴充為詳細企業框架  
    - 進階驗證與授權，整合 Microsoft Entra ID  
    - Token 安全及防止透傳控管，全方位驗證  
    - 工作階段安全控管，防止劫持  
    - AI 專屬安全控管，防範提示注入和工具中毒  
    - 混淆代理攻擊防護，OAuth 代理安全  
    - 工具執行安全，沙盒與隔離  
    - 供應鏈安全控管，相依性驗證  
    - 監控與偵測控管，整合 SIEM  
    - 事件响应與復原，自動化能力  
  - <strong>實作範例</strong>：新增詳細 YAML 配置區塊與程式碼範例  
  - **Microsoft 解決方案整合**：全面涵蓋 Azure 安全服務、GitHub Advanced Security 與企業身份管理  

#### 進階主題安全 (05-AdvancedTopics/mcp-security/) — 生產環境準備實作  
- **README.md**：為企業安全實作完全改寫  
  - <strong>與現行規範對齊</strong>：更新至 MCP 規範 2025-06-18，包含強制安全要求  
  - <strong>增強驗證</strong>：整合 Microsoft Entra ID，附詳細 .NET 與 Java Spring Security 範例  
  - **AI 安全整合**：實作 Microsoft Prompt Shields 與 Azure Content Safety，並附詳細 Python 範例  
  - <strong>進階威脅緩解</strong>：詳細實作  
    - 混淆代理攻擊防護，含 PKCE 與用戶同意驗證  
    - Token 透傳防護，包含受眾驗證與安全的 token 管理  
    - 工作階段劫持防護，具密碼綁定與行為分析  
  - <strong>企業安全整合</strong>：Azure Application Insights 監控、威脅偵測管線與供應鏈安全  
  - <strong>實作檢查表</strong>：明確區分強制與建議安全控管，並講解 Microsoft 安全生態系統之利益  

### 文件品質與標準對齊  
- <strong>規範參考</strong>：更新所有引用至最新 MCP 規範 2025-06-18  
- **Microsoft 安全生態系統**：強化整合指導於所有安全文件中  
- <strong>實務實作</strong>：新增 .NET、Java 與 Python 的詳細程式碼範例與企業模式  
- <strong>資源組織</strong>：將官方文件、安全標準與實作指引完整分類  
- <strong>視覺指示</strong>：明確標示強制要求與建議實務  

#### 核心概念 (01-CoreConcepts/) — 完整現代化  
- <strong>協定版本更新</strong>：更新為引用現行 MCP 規範 2025-06-18，採用日期格式版本 (YYYY-MM-DD)  
- <strong>架構精鍊</strong>：增強 Hosts、Clients 與 Servers 的描述，反映現行 MCP 架構模式  
  - Hosts 清楚定義為多 MCP 用戶端連線協調的 AI 應用  
  - Clients 描述為維持一對一伺服器關係的協定連接器  
  - Servers 增強本地與遠端部署場景說明  
- <strong>原語重構</strong>：服务器與用戶端原語全面改造  
  - 伺服器原語：Resources（資料來源）、Prompts（模板）、Tools（可執行功能），附詳細解說與範例  
  - 用戶端原語：Sampling（LLM 回覆）、Elicitation（用戶輸入）、Logging（偵錯/監控）  
  - 更新發現(`*/list`)、擷取(`*/get`)與執行(`*/call`)方法模式  
- <strong>協定架構</strong>：導入雙層架構模型  
  - 資料層：基於 JSON-RPC 2.0，含生命週期管理及原語  
  - 傳輸層：STDIO（本地）與可串流 HTTP 含 SSE（遠端）傳輸機制  
- <strong>安全框架</strong>：全方位安全原則，包括明確用戶同意、資料隱私保護、工具執行安全及傳輸層安全  
- <strong>通訊模式</strong>：更新協定訊息顯示初始化、發現、執行與通知流程  
- <strong>程式碼範例</strong>：更新多語言範例 (.NET、Java、Python、JavaScript) 反映現行 MCP SDK 模式  

#### 安全 (02-Security/) — 全面安全改造  
- <strong>標準對齊</strong>：全面符合 MCP 規範 2025-06-18 安全要求  
- <strong>驗證演進</strong>：紀錄自訂 OAuth 伺服器到外部身份提供者委派（Microsoft Entra ID）的演進  
- **AI 專屬威脅分析**：強化現代 AI 攻擊向量覆蓋  
  - 詳細提示注入攻擊情境與實例  
  - 工具中毒機制與「拔地毯」攻擊模式  
  - 上下文窗口中毒與模型混淆攻擊  
- **Microsoft AI 安全解決方案**：全面涵蓋 Microsoft 安全生態系統  
  - AI Prompt Shields 具先進偵測、聚焦與分隔符技術  
  - Azure Content Safety 整合模式  
  - GitHub Advanced Security 提供供應鏈保護  
- <strong>進階威脅緩解</strong>：詳細安全控管  
  - 工作階段劫持，含 MCP 專屬攻擊情境與密碼學會話 ID 要求  
  - MCP 代理混淆代理問題，附明確同意需求  
  - Token 透傳漏洞，具強制驗證控管  
- <strong>供應鏈安全</strong>：擴充 AI 供應鏈涵蓋基礎模型、嵌入服務、上下文提供者及第三方 API  
- <strong>基礎安全</strong>：強化企業安全模式整合，包括零信任架構與 Microsoft 安全生態系統  
- <strong>資源組織</strong>：依類型（官方文件、標準、研究、Microsoft 解決方案、實作指引）分類完整資源連結  

### 文件品質提升  
- <strong>結構化學習目標</strong>：增強學習目標，具體且可執行  
- <strong>跨章節參考</strong>：新增相關安全與核心概念主題間鏈結  
- <strong>資訊更新</strong>：更新所有日期引用與規範鏈結為當前標準  
- <strong>實作指導</strong>：全章節新增具體可行的實作指南  

## 2025年7月16日  

### README 與導覽改進  
- README.md 中課程導覽全面重新設計  
- 用表格取代 `<details>` 標籤，提升可訪問性  
- 新增「alternative_layouts」資料夾中的替代版面選項  
- 添加卡片式、標籤式及手風琴式導覽範例  
- 更新儲存庫結構章節，包含所有最新檔案  
- 強化「如何使用此課程」章節提供明確建議  
- 更新 MCP 規範鏈結指向正確 URL  
- 增設上下文工程（5.14）章節入課程結構  

### 學習指南更新  
- 徹底修訂學習指南，符合目前儲存庫架構  
- 新增 MCP 用戶端與工具，以及熱門 MCP 伺服器章節  
- 更新視覺課程地圖，準確呈現所有主題  
- 強化進階主題描述，涵蓋所有專門領域  
- 更新實例案例章節反映實際範例  
- 添加本完整更新日誌  

### 社群貢獻 (06-CommunityContributions/)  
- 新增詳細 MCP 圖像生產伺服器資訊  
- 新增 VSCode 中使用 Claude 的完整說明  
- 新增 Cline 終端用戶端設定與使用說明  
- 更新 MCP 用戶端章節包含所有熱門選項  
- 強化貢獻範例，提供更準確的程式碼範本  

### 進階主題 (05-AdvancedTopics/)  
- 將所有專門主題資料夾以一致命名整理  
- 新增上下文工程教材與範例  
- 新增 Foundry 代理整合文件  
- 強化 Entra ID 安全整合文件  

## 2025年6月11日  

### 初始建立  
- 發布 MCP for Beginners 課程第一版  
- 建立所有 10 個主要章節的基礎結構  
- 實作視覺課程地圖以供導覽  
- 新增多程式語言範例專案  

### 入門 (03-GettingStarted/)  
- 建立首批伺服器實作範例  
- 提供用戶端開發指導  
- 包含 LLM 用戶端整合說明  
- 新增 VS Code 整合文件  
- 實作 Server-Sent Events (SSE) 伺服器範例  

### 核心概念 (01-CoreConcepts/)  
- 新增用戶端-伺服器架構詳細說明  
- 製作文檔說明主要協定元件  
- 記錄 MCP 中的訊息模式  

## 2025年5月23日  

### 儲存庫結構  
- 初始化儲存庫基本資料夾結構  
- 為主要章節建立 README 文件  
- 設置翻譯基礎架構  
- 添加圖片資產與圖示  

### 文件  
- 建立初版 README.md，介紹課程概覽  
- 添加入 CODE_OF_CONDUCT.md 與 SECURITY.md  
- 設置 SUPPORT.md，提供求助指導  
- 創建初步學習指南結構  

## 2025年4月15日  

### 規劃與架構  
- MCP for Beginners 課程初步規劃  
- 定義學習目標與目標受眾  
- 概述課程十個章節架構  
- 制訂範例與案例研究的概念框架  
- 創建關鍵概念初期範例原型

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯所產生的任何誤解或誤讀，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
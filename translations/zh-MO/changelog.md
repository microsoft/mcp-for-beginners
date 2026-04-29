# 版本記錄：MCP 初學者課程

本文件作為模型上下文協議 (MCP) 初學者課程所有重大變更的記錄。變更以逆時間順序記錄（最新變更優先）。

## 2026 年 4 月 11 日

### 新課程、文檔修正與依賴更新

#### 新增課程內容

**模組 05 - 進階主題**  
- **課程 5.17：使用 MCP 的對抗式多智能體推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`)：全面指南，涵蓋多智能體系統的對抗辯論模式  
  - Mermaid 架構圖：兩個智能體 → 共享 MCP 伺服器 → 辯論文字稿 → 評審 → 判決  
  - 以 Python 及 TypeScript 實現的共享 MCP 工具伺服器（`web_search` + `run_python`）  
  - 對立系統提示（贊成 / 反對 / 評審）明確指定工具使用要求  
  - 以 Python、TypeScript 和 C# 編寫的辯論協調器，管理回合及路由辯論  
  - MCP `ClientSession` 連接協調器到真實工具調用  
  - 使用案例表格（幻覺檢測、威脅建模、API 設計審查、事實驗證、技術選擇）  
  - 安全考量：沙盒執行、工具調用驗證、速率限制、審計日誌  
  - 結構化練習，包含三個實際場景（代碼審查、架構決策、內容審核）

#### 文檔修正

**模組 03 - 入門**  
- **05-stdio-server/README.md**：修正不完整的 TypeScript stdio 伺服器範例 — 補充遺漏的傳輸層實例化（`new StdioServerTransport()`）及 `server.connect(transport)` 呼叫，使之與同節的 Python 和 .NET 範例一致  
- **14-sampling/README.md**：修正錯字 — `"Sampling is an davanced features"` 更正為 `"Sampling is an advanced feature"`

#### 課程更新

**主 README.md**  
- 課程表新增條目 5.17（使用 MCP 的對抗式多智能體推理），並加上該課程的直接連結  

**05-AdvancedTopics/README.md**  
- 課程表新增課程 5.17 行

**study_guide.md**  
- 在進階主題的思維導圖與文字說明中加入對抗式多智能體推理主題

#### 程式碼和安全修正

**模組 05 - 對抗智能體 (`mcp-adversarial-agents`)**  
- **安全修正 — 命令注入**：在 TypeScript 的 `run_python` 工具中，用 `execFile` + `promisify` 取代 `execSync` 與 shell 插值，消除了命令注入風險（LLM 控制的程式碼現在作為字面 argv 元素傳入，沒經過 shell）  
- **MCP 工具迴圈連線**：更新 Python 辯論協調器改用非同步 `AsyncAnthropic` 客戶端（取代阻塞同步 `Anthropic`），直接將活躍的 `ClientSession` 傳給每個智能體回合，每回合透過 `session.list_tools()` 獲取工具定義，並在迴圈中用 `session.call_tool()` 傳送 `tool_use` 區塊，直到模型回應最終文字

#### 依賴更新

- 多個套件 (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows) 中將 `hono` 更新到 4.12.12  
- TypeScript 套件中將 `@hono/node-server` 從 1.19.11 提升至 1.19.13  
- Python 套件 (10-StreamliningAIWorkflows 實驗 3 和 4) 升級 `cryptography` 從 46.0.5 至 46.0.7  
- 10-StreamliningAIWorkflows 監控器中將 `lodash` 從 4.17.23 提升至 4.18.1  

#### 翻譯

- 同步48+種語言的翻譯，更新至最新源碼變更（i18n 更新）

---

## 2026 年 2 月 5 日

### 全倉庫驗證及導航改進

#### 新增課程內容

**模組 03 - 入門**  
- **12-mcp-hosts/README.md**：全新的 MCP 主機設定指南  
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置範例  
  - 所有主流主機的 JSON 配置範本  
  - 傳輸類型比較表（stdio、SSE/HTTP、WebSocket）  
  - 連線故障排除  
  - 主機配置的安全最佳實踐  

- **13-mcp-inspector/README.md**：全新的 MCP Inspector 除錯指南  
  - 安裝方法（npx、npm 全域、從原始碼）  
  - 透過 stdio、HTTP/SSE 連線伺服器  
  - 測試工具、資源及提示工作流程  
  - VS Code 整合 MCP Inspector  
  - 常見除錯場景及解法  

**模組 04 - 實務實作**  
- **pagination/README.md**：全新的分頁實作指南  
  - Python、TypeScript、Java 中的基於游標的分頁模式  
  - 客戶端分頁處理  
  - 游標設計策略（不透明 vs. 結構化）  
  - 性能優化建議  

**模組 05 - 進階主題**  
- **mcp-protocol-features/README.md**：全新的協議功能深度解析  
  - 進度通知實作  
  - 請求取消模式  
  - 帶 URI 模式的資源範本  
  - 伺服器生命週期管理  
  - 日誌等級控制  
  - JSON-RPC 錯誤處理模式  

#### 導航修正（24+ 檔案更新）

**主模組README**  
- 現在同時連結至第一課與下一模組  

**02-Security 子檔案**  
- 所有5份補充安全文件新增「接下來是？」導航  

**09-案例研究檔案**  
- 所有案例研究檔案新增順序導航  

**10-StreamliningAI 實驗室**  
- 在模組10總覽與模組11新增「接下來是？」章節

#### 程式碼與內容修正

**SDK與依賴更新**  
修正空白 openai 版本為 `^4.95.0`  
SDK 從 `^1.8.0` 更新為 `>=1.26.0`  
MCP 版本固定為 `>=1.26.0`

<strong>程式碼修正</strong>  
修正無效模型 `gpt-4o-mini` 為 `gpt-4.1-mini`

<strong>內容修正</strong>  
修正壞掉的連結 `READMEmd` → `README.md`，修正課程標題 `Module 1-3` → `Module 0-3`，修正大小寫敏感路徑  
移除損壞的重複案例研究 5 內容

<strong>初學指導改善</strong>  
新增適當的介紹、學習目標及前提條件

#### 課程更新

**主 README.md**  
- 課程表新增條目 3.12（MCP Hosts）、3.13（MCP Inspector）、4.1（分頁）、5.16（協議功能）  

**模組 README**  
- 課程清單新增 12 與 13  
- 新增實務指南區塊，包含分頁連結  
- 新增課程 5.15（自訂傳輸）與 5.16（協議功能）  

**study_guide.md**  
- 更新思維導圖，新增 MCP Hosts 設定、MCP Inspector、分頁策略、協議功能深度解析

## 2026 年 1 月 28 日

### MCP 規範 2025-11-25 合規審查

#### 核心概念強化（01-CoreConcepts/）  
- **新增客戶端原語 - Roots**：新增 Roots 客戶端原語完整文件，讓伺服器理解檔案系統邊界與存取權限  
- <strong>工具註解</strong>：新增工具行為註解文件（`readOnlyHint`、`destructiveHint`）以優化工具執行決策  
- <strong>採樣中的工具呼叫</strong>：更新採樣文件，包含 `tools` 與 `toolChoice` 參數，支持模型驅動呼叫工具  
- **URL 模式引發**：新增基於 URL 的引發說明，支持伺服器啟動的外部網絡互動  
- **任務 (實驗性)**：新增記錄實驗性任務功能的章節，支持持久執行封裝與延後結果取回  
- <strong>圖示支援</strong>：註明工具、資源、資源範本與提示可包含圖示作為附加元數據

#### 文檔更新  
- **README.md**：新增 MCP 規範 2025-11-25 版本參考與日期版本說明  
- **study_guide.md**：更新課程地圖，納入核心概念部分的任務與工具註解；更新文件時間戳  

#### 規範合規驗證  
- <strong>協議版本</strong>：確認所有文檔引用最新 MCP 規範 2025-11-25  
- <strong>架構對齊</strong>：確認兩層架構（資料層 + 傳輸層）文檔準確性  
- <strong>原語文件</strong>：驗證伺服器原語（資源、提示、工具）與客戶端原語（採樣、引發、日誌、Roots）文件完備  
- <strong>傳輸機制</strong>：確認 STDIO 與可串流 HTTP 傳輸文檔正確  
- <strong>安全指引</strong>：驗證符合當前 MCP 安全最佳實踐文檔

#### 重要 MCP 2025-11-25 功能文件  
- **OpenID Connect 探索**：透過 OIDC 進行認證伺服器發現  
- **OAuth 客戶端 ID 元資料文檔**：建議的客戶端註冊機制  
- **JSON Schema 2020-12**：作為 MCP 架構定義的預設方言  
- **SDK 分級系統**：正式化 SDK 功能支持與維護需求  
- <strong>治理結構</strong>：正式化 MCP 工作組與利益相關組織治理

### 安全文件重大更新（02-Security/）

#### MCP 安全峰會工作坊（Sherpa）整合  
- <strong>新增實務訓練資源</strong>：在所有安全文件中加入與 [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) 的完整整合  
- <strong>探險路線涵蓋</strong>：記錄營地間完整進程，從基地營到峰頂  
- **符合 OWASP**：所有安全指導映射至 OWASP MCP Azure 安全指南的風險

#### OWASP MCP Top 10 整合  
- <strong>新增章節</strong>：在主安全 README 中增加 OWASP MCP Top 10 安全風險表與 Azure 減輕措施  
- <strong>風險為本文件</strong>：在 mcp-security-controls-2025.md 爲每個安全領域添加 OWASP MCP 風險引用  
- <strong>參考架構</strong>：鏈結 OWASP MCP Azure 安全指南參考架構和實作範式

#### 更新安全文件  
- **README.md**：新增 Sherpa 工作坊概述、探險路線表、OWASP MCP Top 10 風險摘要及實務訓練章節  
- **mcp-security-controls-2025.md**：更新標題為 2026 年 2 月，新增 OWASP 風險參考 (MCP01-MCP08)，修正規範版本不一致  
- **mcp-security-best-practices-2025.md**：新增 Sherpa 與 OWASP 資源章節，更新時間戳  
- **mcp-best-practices.md**：新增實務訓練章節，包含 Sherpa 和 OWASP 連結  
- **azure-content-safety-implementation.md**：新增 OWASP MCP06 引用、Sherpa 3 處營地對齊及額外資源章節

#### 新增資源連結  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- 各個 OWASP MCP 風險頁面（MCP01-MCP10）

### 全課程 MCP 規範 2025-11-25 對齊

#### 模組 03 - 入門  
- **SDK 文件**：新增 Go SDK 至官方 SDK 清單；更新所有 SDK 參考以符合 MCP 規範 2025-11-25  
- <strong>傳輸說明</strong>：更新 STDIO 與 HTTP 串流傳輸描述，明確加入規範引用

#### 模組 04 - 實務實作  
- **SDK 更新**：新增 Go SDK；更新 SDK 清單及規範版本引用  
- <strong>授權規範</strong>：更新 MCP 授權規範鏈結至當前 2025-11-25 版本

#### 模組 05 - 進階主題  
- <strong>新功能</strong>：新增關於 MCP 規範 2025-11-25 功能的說明（任務、工具註解、URL 模式引發、Roots）  
- <strong>安全資源</strong>：新增 OWASP MCP Top 10 及 Sherpa 工作坊連結至參考文獻

#### 模組 06 - 社群貢獻  
- **SDK 清單**：新增 Swift 與 Rust SDK；更新規範鏈結至 2025-11-25  
- <strong>規範參考</strong>：更新 MCP 規範連結為直接規範 URL

#### 模組 07 - 早期採用經驗  
- <strong>資源更新</strong>：新增 MCP 規範 2025-11-25 連結及 OWASP MCP Top 10 至額外資源

#### 模組 08 - 最佳實務  
- <strong>規範版本</strong>：更新 MCP 規範參考為 2025-11-25  
- <strong>安全資源</strong>：新增 OWASP MCP Top 10 與 Sherpa 工作坊至參考文獻

#### 模組 10 - 精簡 AI 工作流程  
- <strong>徽章更新</strong>：將 MCP 版本徽章從 SDK 版本（1.9.3）改為規範版本（2025-11-25）  
- <strong>資源連結</strong>：更新 MCP 規範連結，新增 OWASP MCP Top 10

#### 模組 11 - MCP 伺服器實作實驗室  
- <strong>規範參考</strong>：更新 MCP 規範連結至 2025-11-25 版本  
- <strong>安全資源</strong>：新增 OWASP MCP Top 10 至官方資源列表

## 2025 年 12 月 18 日
### 安全文件更新 - MCP 規範 2025-11-25

#### MCP 安全最佳實踐 (02-Security/mcp-best-practices.md) - 規範版本更新
- <strong>協議版本更新</strong>：已更新為參考最新 MCP 規範 2025-11-25（於 2025 年 11 月 25 日發佈）
  - 將所有規範版本參考自 2025-06-18 更新為 2025-11-25
  - 將文件日期參考自 2025 年 8 月 18 日更新為 2025 年 12 月 18 日
  - 驗證所有規範網址指向最新文件
- <strong>內容驗證</strong>：對安全最佳實踐進行全面驗證，確保符合最新標準
  - <strong>微軟安全方案</strong>：驗證 Prompt Shields（前稱「越獄風險檢測」）、Azure Content Safety、Microsoft Entra ID 與 Azure Key Vault 的最新術語與連結
  - **OAuth 2.1 安全**：確認符合最新 OAuth 安全最佳實踐
  - **OWASP 標準**：驗證 LLM 的 OWASP 十大參考資料仍為最新
  - **Azure 服務**：驗證所有 Microsoft Azure 文件連結與最佳實踐
- <strong>標準對齊</strong>：所有參考的安全標準確認為最新
  - NIST 人工智能風險管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳實踐
  - Azure 安全與合規框架
- <strong>實施資源</strong>：驗證所有實施指南連結與資源
  - Azure API 管理認證模式
  - Microsoft Entra ID 整合指南
  - Azure Key Vault 機密管理
  - DevSecOps 流水線與監控方案

### 文件品質保證
- <strong>規範合規性</strong>：確保所有 MCP 強制安全要求（必須/禁止）與最新規範一致
- <strong>資源時效性</strong>：確認所有外部微軟文件、安規標準及實施指南連結有效
- <strong>最佳實踐涵蓋</strong>：確認全面涵蓋認證、授權、AI 特定威脅、供應鏈安全及企業模式

## 2025 年 10 月 6 日

### 初學者指南擴充 – 進階伺服器使用與簡易認證

#### 進階伺服器使用 (03-GettingStarted/10-advanced)
- <strong>新增章節</strong>：引入全面進階 MCP 伺服器使用指南，涵蓋常規與低層伺服器架構。
  - <strong>常規與低層伺服器對比</strong>：Python 與 TypeScript 範例詳述兩種方法。
  - <strong>基於處理程序的設計</strong>：說明基於處理程序的工具/資源/提示管理，以支援可擴展且彈性的伺服器實作。
  - <strong>實務樣式</strong>：展示低層伺服器樣式在進階功能與架構中的應用場景。

#### 簡易認證 (03-GettingStarted/11-simple-auth)
- <strong>新增章節</strong>：逐步指導在 MCP 伺服器中實作簡易認證。
  - <strong>認證概念</strong>：清楚說明認證與授權之間差異，及憑證處理方式。
  - <strong>基本認證實作</strong>：Python (Starlette) 和 TypeScript (Express) 中基於中介軟體的認證範例與程式碼。
  - <strong>進階安全發展</strong>：指引從簡易認證逐步升級至 OAuth 2.1 與基於角色的存取控制，並附加進階安全模組參考。

這些延伸內容提供實務操作指導，協助打造更穩健、安全且彈性的 MCP 伺服器實作，連接基礎概念與進階生產模式。

## 2025 年 9 月 29 日

### MCP 伺服器資料庫整合實驗室 - 全面實務學習路徑

#### 11-MCPServerHandsOnLabs - 新增完整資料庫整合課程
- **完整 13 個實驗室學習路徑**：新增實務課程，涵蓋建置生產級 MCP 伺服器與 PostgreSQL 資料庫整合
  - <strong>實務案例</strong>：Zava Retail 分析案例，展示企業級模式
  - <strong>結構化學習進程</strong>：
    - **實驗室 00-03：基礎** - 介紹、核心架構、安全與多租戶、環境設定
    - **實驗室 04-06：建置 MCP 伺服器** - 資料庫設計與結構、MCP 伺服器實作、工具開發  
    - **實驗室 07-09：進階功能** - 語義搜尋整合、測試與除錯、VS Code 整合
    - **實驗室 10-12：生產與最佳實踐** - 部署策略、監控與可觀察性、最佳實踐與優化
  - <strong>企業技術</strong>：FastMCP 框架、Pgvector PostgreSQL 擴展、Azure OpenAI 嵌入、Azure Container Apps、Application Insights
  - <strong>進階功能</strong>：行級安全 (RLS)、語義搜尋、多租戶資料存取、向量嵌入、即時監控

#### 術語標準化 - 模組至實驗室轉換
- <strong>全面文件更新</strong>：系統性將 11-MCPServerHandsOnLabs 中所有 README 檔案的「模組」術語更新為「實驗室」
  - <strong>章節標題</strong>：將「本模組涵蓋內容」改為「本實驗室涵蓋內容」
  - <strong>內容描述</strong>：將「本模組提供…」改為「本實驗室提供…」
  - <strong>學習目標</strong>：將「本模組結束時…」改為「本實驗室結束時…」
  - <strong>導航連結</strong>：將所有「模組 XX：」引用改為「實驗室 XX：」
  - <strong>完成追蹤</strong>：將「完成本模組後…」改為「完成本實驗室後…」
  - <strong>保留技術引用</strong>：Python 配置檔中的模組參考維持不變（如 `"module": "mcp_server.main"`）

#### 學習指南強化 (study_guide.md)
- <strong>視覺化課程地圖</strong>：新增「11. 資料庫整合實驗室」區塊，詳列實驗室結構
- <strong>代碼庫結構</strong>：由十個主區塊更新為十一個區段，加入 11-MCPServerHandsOnLabs 詳細說明
- <strong>學習路徑指引</strong>：增強導航指示，覆蓋 00-11 區段
- <strong>技術涵蓋</strong>：新增 FastMCP、PostgreSQL、Azure 服務整合細節
- <strong>學習成果</strong>：強調生產級伺服器開發、資料庫整合模式及企業安全

#### 主 README 結構強化
- <strong>以實驗室術語為基礎</strong>：11-MCPServerHandsOnLabs 主 README.md 完整採用「實驗室」結構
- <strong>學習路徑組織</strong>：明確從基礎概念至進階實作再到生產部署的進程
- <strong>實務導向</strong>：強調實務與企業級模式與技術之學習

### 文件品質與一致性改進
- <strong>強調實作學習</strong>：全文強化以實驗室為主的操作導向
- <strong>企業模式聚焦</strong>：突出生產就緒實作與企業安全議題
- <strong>技術整合</strong>：全方位涵蓋現代 Azure 服務與 AI 整合樣式
- <strong>學習進程清晰</strong>：由基礎到生產部署的有序路徑

## 2025 年 9 月 26 日

### 案例研究增強 - GitHub MCP Registry 整合

#### 案例研究 (09-CaseStudy/) - 生態系發展焦點
- **README.md**：大幅擴充，新增完整 GitHub MCP Registry 案例研究
  - **GitHub MCP Registry 案例研究**：詳述 2025 年 9 月 GitHub MCP Registry 發布
    - <strong>問題分析</strong>：深入探討分散 MCP 伺服器發現與部署挑戰
    - <strong>解決架構</strong>：GitHub 集中式註冊表與一鍵 VS Code 安裝方式
    - <strong>商業影響</strong>：顯著提升開發者入門與生產力
    - <strong>策略價值</strong>：聚焦模組化代理部署與跨工具互操作性
    - <strong>生態系發展</strong>：定位為代理系統集成基礎平台
  - <strong>案例研究結構強化</strong>：更新全部七個案例，格式統一並提供詳盡描述
    - Azure AI 旅遊代理：多代理協調強調
    - Azure DevOps 整合：工作流自動化聚焦
    - 即時文件檢索：Python 主控台客戶端實作
    - 互動學習計畫生成器：Chainlit 對話型 Web 應用
    - 編輯器內文件：VS Code 與 GitHub Copilot 整合
    - Azure API 管理：企業 API 整合模式
    - GitHub MCP Registry：生態系發展與社群平台
  - <strong>全面結論改寫</strong>：強調七大案例跨越多 MCP 實作維度
    - 企業整合、多代理協作、開發者效率
    - 生態系發展、教育應用分類
    - 深度解析架構模式、實作策略及最佳實踐
    - 展現 MCP 作為成熟與生產就緒協議

#### 學習指南更新 (study_guide.md)
- <strong>視覺化課程地圖</strong>：更新心智圖，包含 GitHub MCP Registry 於案例研究區塊
- <strong>案例研究描述</strong>：由泛泛描述改為七個詳盡案例拆解
- <strong>代碼庫結構</strong>：更新第 10 區段以反映完整案例研究涵蓋及具體細節
- <strong>更新日誌整合</strong>：添加 2025 年 9 月 26 日條目文檔 GitHub MCP Registry 新增及案例研究強化
- <strong>日期更新</strong>：更新頁腳時間戳為最新修訂（2025 年 9 月 26 日）

### 文件品質改進
- <strong>一致性強化</strong>：標準化所有七例案例格式與結構
- <strong>全面涵蓋</strong>：案例跨企業、開發效率與生態系場景
- <strong>策略定位強化</strong>：凸顯 MCP 作為代理系統部署基礎平台
- <strong>資源整合</strong>：更新附加資源包含 GitHub MCP Registry 連結

## 2025 年 9 月 15 日

### 進階主題擴充 - 自訂傳輸與上下文工程

#### MCP 自訂傳輸 (05-AdvancedTopics/mcp-transport/) - 新增進階實作指南
- **README.md**：完整自訂 MCP 傳輸機制實作指南
  - **Azure Event Grid 傳輸**：全面無伺服器事件驅動傳輸實作
    - C#、TypeScript 與 Python 範例，結合 Azure Functions
    - 可擴展 MCP 解決方案之事件驅動架構模式
    - Webhook 接收者與推送訊息處理
  - **Azure Event Hubs 傳輸**：高吞吐量串流傳輸實作
    - 低延遲場景的即時串流能力
    - 分區策略與檢查點管理
    - 訊息批次與效能優化
  - <strong>企業整合模式</strong>：生產就緒架構範例
    - 分散式 MCP 處理橫跨多 Azure Functions
    - 混合傳輸架構結合多種傳輸類型
    - 訊息持久性、可靠性與錯誤處理策略
  - <strong>安全與監控</strong>：Azure Key Vault 整合與可觀察性模式
    - 管理身分認證與最小權限存取
    - Application Insights 遙測與效能監控
    - 熔斷器與容錯模式
  - <strong>測試框架</strong>：自訂傳輸綜合測試策略
    - 使用測試替身和模擬框架的單元測試
    - 結合 Azure 測試容器的整合測試
    - 效能與負載測試考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新興 AI 領域
- **README.md**：深入探討上下文工程作為新興領域
  - <strong>核心原則</strong>：完整上下文共享、行動決策感知與上下文窗口管理
  - **MCP 協議對應**：MCP 設計如何解決上下文工程挑戰
    - 上下文窗口限制與漸進式載入策略
    - 相關性判定與動態上下文擷取
    - 多模態上下文處理與安全考量
  - <strong>實作方式</strong>：單執行緒與多代理架構
    - 上下文切塊與優先級技術
    - 漸進式上下文載入與壓縮策略
    - 分層上下文方法與擷取優化
  - <strong>衡量框架</strong>：新興的上下文效能評估指標
    - 輸入效率、效能、質量與用戶體驗
    - 上下文優化實驗方法
    - 失敗分析與改進方法學

#### 課程導覽更新 (README.md)
- <strong>強化模組結構</strong>：課程表新增進階主題
  - 加入上下文工程 (5.14) 與自訂傳輸 (5.15)
  - 全模組格式與導航連結保持一致
  - 更新描述反映當前內容範圍

### 目錄結構改善
- <strong>命名標準化</strong>：將「mcp transport」改名為「mcp-transport」，與其他進階主題資料夾保持一致
- <strong>內容組織</strong>：所有 05-AdvancedTopics 資料夾皆遵循 mcp-[主題] 命名規範

### 文件品質提升
- **MCP 規範對齊**：新內容引用最新 MCP 規範 2025-06-18
- <strong>多語言範例</strong>：提供 C#、TypeScript 與 Python 完整程式碼範例
- <strong>企業聚焦</strong>：全程包含生產就緒設計模式與 Azure 雲端整合
- <strong>視覺文件</strong>：使用 Mermaid 圖表呈現架構與流程

## 2025 年 8 月 18 日

### 文件全面更新 - MCP 2025-06-18 標準

#### MCP 安全最佳實踐 (02-Security/) - 全面現代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：根據 MCP 規範 2025-06-18 完全重寫
  - <strong>強制性要求</strong>：新增官方規範中的明確 MUST/MUST NOT 要求，並附清晰視覺標示
  - **12 個核心安全實踐**：由 15 項列表重構為完整安全領域
    - 代幣安全與驗證，整合外部身份識別提供者
    - 會話管理與傳輸安全，含密碼學要求
    - AI 專用威脅防護，整合 Microsoft Prompt Shields
    - 存取控制與權限管理，依據最小權限原則
    - 內容安全與監控，整合 Azure Content Safety
    - 供應鏈安全，涵蓋完整元件驗證
    - OAuth 安全與混淆代理防範，實作 PKCE
    - 事件回應與復原，具備自動化能力
    - 合規與治理，符合法規要求
    - 進階安全控制，採用零信任架構
    - Microsoft 安全生態系統整合，涵蓋全面解決方案
    - 持續安全演進，採用適應性實踐
  - **Microsoft 安全解決方案**：強化 Prompt Shields、Azure Content Safety、Entra ID 及 GitHub Advanced Security 整合指引
  - <strong>實作資源</strong>：依官方 MCP 文件、Microsoft 安全解決方案、安全標準與實作指南分類彙整資源連結

#### 進階安全控制 (02-Security/) — 企業級實作
- **MCP-SECURITY-CONTROLS-2025.md**：全面翻新，導入企業級安全框架
  - **9 大安全領域**：從基本控制擴展至詳細企業框架
    - 進階驗證與授權，整合 Microsoft Entra ID
    - 代幣安全與反直通控制，具全面驗證機制
    - 會話安全控制，防範接管攻擊
    - AI 專用安全控制，防止提示注入與工具中毒
    - 混淆代理攻擊防範，OAuth 代理安全
    - 工具執行安全，沙箱與隔離機制
    - 供應鏈安全控制，依賴性驗證
    - 監控與偵測控制，整合 SIEM
    - 事件回應與復原，自動化能力
  - <strong>實作範例</strong>：新增詳盡 YAML 配置區塊與程式碼示例
  - **Microsoft 解決方案整合**：涵蓋 Azure 安全服務、GitHub Advanced Security 與企業身份管理

#### 進階主題安全 (05-AdvancedTopics/mcp-security/) — 生產環境實作
- **README.md**：企業安全實作全面重寫
  - <strong>符合最新規範</strong>：更新為 MCP 規範 2025-06-18，包括強制安全需求
  - <strong>強化驗證</strong>：整合 Microsoft Entra ID，並提供豐富 .NET 與 Java Spring Security 範例
  - **AI 安全整合**：Microsoft Prompt Shields 與 Azure Content Safety 實作，含詳細 Python 範例
  - <strong>進階威脅緩解</strong>：詳盡實作範例涵蓋
    - 混淆代理攻擊防範，含 PKCE 與使用者同意驗證
    - 代幣直通防護，受眾驗證與安全代幣管理
    - 會話接管防範，密碼學綁定與行為分析
  - <strong>企業安全整合</strong>：Azure Application Insights 監控、威脅偵測管線與供應鏈安全
  - <strong>實作檢查表</strong>：清楚區分強制與建議安全控制，說明 Microsoft 安全生態系優勢

### 文件品質與標準對齊
- <strong>規範參考</strong>：全部參照現行 MCP 規範 2025-06-18
- **Microsoft 安全生態系統**：加強所有安全文件的整合指導
- <strong>實務實作</strong>：新增 .NET、Java 與 Python 詳細程式範例，符合企業模式
- <strong>資源分類</strong>：完整分類官方文件、安全標準與實作指南
- <strong>視覺標示</strong>：明確標示強制要求與建議實務

#### 核心概念 (01-CoreConcepts/) — 完整現代化
- <strong>協定版本更新</strong>：更新為 MCP 規範 2025-06-18，採用日期版本格式（YYYY-MM-DD）
- <strong>架構優化</strong>：增強 Hosts、Clients 及 Servers 說明，反映當前 MCP 架構模式
  - Hosts 明確定義為協調多個 MCP Client 連線的 AI 應用
  - Clients 描述為保持一對一伺服器關係的協定連接器
  - Servers 強化描述本地與遠端部署場景
- <strong>原件重構</strong>：伺服器與客戶端原件全面更新
  - 伺服器原件：資源（資料來源）、提示（模板）、工具（可執行函式），附詳細說明與範例
  - 客戶端原件：採樣（LLM 產出）、引導（使用者輸入）、日誌（偵錯／監控）
  - 更新現行發現（`*/list`）、檢索(`*/get`)及執行(`*/call`)方法模式
- <strong>協定架構</strong>：引入兩層架構模型
  - 資料層：以 JSON-RPC 2.0 為基礎，具生命週期管理與原件
  - 傳輸層：含 STDIO（本地）與支援 SSE 的 Streamable HTTP（遠端）
- <strong>安全框架</strong>：全面安全原則，包括明確使用者同意、資料隱私保護、工具執行安全及傳輸層安全
- <strong>通訊模式</strong>：更新協定訊息顯示初始化、發現、執行與通知流程
- <strong>程式碼範例</strong>：更新多語言範例（.NET、Java、Python、JavaScript），反映現行 MCP SDK 模式

#### 安全 (02-Security/) — 全面安全大翻新  
- <strong>標準對齊</strong>：完全符合 MCP 規範 2025-06-18 安全要求
- <strong>驗證演進</strong>：記錄從自訂 OAuth 伺服器到外部身份提供者委派（Microsoft Entra ID）演變
- **AI 專用威脅分析**：加強現代 AI 攻擊向量涵蓋
  - 詳細提示注入攻擊案例與真實世界範例
  - 工具中毒機制及「地毯式拔除」攻擊模式
  - 上下文視窗中毒與模型混淆攻擊
- **Microsoft AI 安全解決方案**：全面介紹 Microsoft 安全生態系
  - AI Prompt Shields 具高級偵測、聚光燈與分隔符技術
  - Azure Content Safety 整合模式
  - GitHub Advanced Security 供應鏈保護
- <strong>進階威脅緩解</strong>：詳細安全控制涵蓋
  - 會話接管，含 MCP 特定攻擊與密碼會話 ID 要求
  - MCP 代理場景下混淆代理問題及明確同意規定
  - 代幣直通弱點與強制驗證控管
- <strong>供應鏈安全</strong>：擴充 AI 供應鏈涵蓋基礎模型、嵌入服務、上下文提供者與第三方 API
- <strong>基礎安全</strong>：強化企業安全模式整合，包括零信任架構與 Microsoft 安全生態系
- <strong>資源分類</strong>：依類型分類全面資源連結（官方文件、標準、研究、Microsoft 解決方案、實作指南）

### 文件品質改進
- <strong>結構化學習目標</strong>：增強具體且可行的學習成果
- <strong>交叉參考</strong>：新增相關安全與核心概念主題連結
- <strong>資訊更新</strong>：更新所有日期引用及規範連結至最新標準
- <strong>實作指引</strong>：兩大部分中加入具體可行的實作指南

## 2025 年 7 月 16 日

### README 及導覽改進
- 完全重設 README.md 中課程導覽
- 以表格格式取代 `<details>` 標籤，提升無障礙
- 在新「alternative_layouts」資料夾內建立替代排版選項
- 新增卡片式、分頁式與手風琴式導覽範例
- 更新倉庫結構章節，納入所有最新檔案
- 強化「如何使用此課程」段落，提供清楚建議
- MCP 規範連結更新為正確網址
- 新增課程結構中的 Context Engineering 章節（5.14）

### 學習指南更新
- 全面修訂學習指南，使其符合目前倉庫結構
- 新增 MCP 客戶端與工具、熱門 MCP 伺服器新章節
- 更新視覺化課程地圖，準確反映所有主題
- 加強進階主題描述，涵蓋所有專業領域
- 更新案例研究章節，反映實際案例
- 附上此綜合版本更新記錄

### 社群貢獻 (06-CommunityContributions/)
- 新增 MCP 影像生成伺服器詳細資訊
- 新增在 VSCode 中使用 Claude 的完整說明
- 新增 Cline 終端客戶端設定與使用指引
- 更新 MCP 客戶端章節，包含所有熱門選項
- 以更準確程式碼範例強化貢獻示例

### 進階主題 (05-AdvancedTopics/)
- 統一整理所有專業主題資料夾命名
- 新增 Context Engineering 材料與範例
- 新增 Foundry 代理整合文件
- 加強 Entra ID 安全整合說明

## 2025 年 6 月 11 日

### 初版建立
- 發布 MCP 入門課程首版
- 建立全部 10 個主區塊基本架構
- 實作視覺課程地圖便於導航
- 新增多語言初始示範專案

### 入門指南 (03-GettingStarted/)
- 建立首批伺服器實作範例
- 新增客戶端開發指導
- 包含 LLM 客戶端整合說明
- 新增 VS Code 整合文件
- 實作 Server-Sent Events（SSE）伺服器範例

### 核心概念 (01-CoreConcepts/)
- 詳細說明客戶端-伺服器架構
- 撰寫主要協定元件文件
- 文件中記錄 MCP 通訊模式

## 2025 年 5 月 23 日

### 倉庫結構
- 建立基本資料夾結構
- 為主要區塊建立 README 檔
- 設置翻譯架構
- 新增圖像資源與示意圖

### 文件
- 建立初版 README.md，含課程總覽
- 新增行為守則 CODE_OF_CONDUCT.md 及安全文件 SECURITY.md
- 建立 SUPPORT.md，提供求助指引
- 預備學習指南結構

## 2025 年 4 月 15 日

### 規劃與框架
- MCP 入門課程初步規劃
- 定義學習目標與目標受眾
- 擬定 10 區塊課程結構
- 開發範例與案例研究概念框架
- 建立核心概念初版範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。文件的原文版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而引起的任何誤解或誤釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
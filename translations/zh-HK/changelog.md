# 變更紀錄：MCP 初學者課程

此文件用於記錄 Model Context Protocol (MCP) 初學者課程的所有重大更動。變更按照時間倒序記錄（最新變更優先）。

## 2026年4月11日

### 新課程、文件修正及依賴更新

#### 新增課程內容

**第05模組 - 進階主題**
- **課程 5.17：基於 MCP 的對抗性多代理推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`)：涵蓋多代理系統對抗辯論模式的完整指南
  - Mermaid 架構圖：兩個代理 → 共享 MCP 伺服器 → 辯論記錄 → 法官 → 裁決
  - 共用 MCP 工具伺服器（`web_search` + `run_python`）由 Python 和 TypeScript 實作
  - 對立系統提示（支持 / 反對 / 法官），有明確工具使用要求
  - 用 Python、TypeScript 和 C# 實現的辯論協調器，管理回合和參數路由
  - MCP `ClientSession` 對協調器真實工具呼叫的連線
  - 用例表（幻覺識別、威脅建模、API 設計評審、事實核查、技術選型）
  - 安全考量：沙盒執行、工具調用驗證、速率限制、稽核日誌
  - 結構化練習包含三個實務場景（程式碼審查、架構決策、內容審核）

#### 文件修正

**第03模組 - 入門**
- **05-stdio-server/README.md**：修正未完成的 TypeScript stdio 伺服器範例 — 補上缺失的傳輸實例化（`new StdioServerTransport()`）及 `server.connect(transport)` 呼叫，與同節中的 Python 和 .NET 範例保持一致
- **14-sampling/README.md**：修正文法錯誤 — 將 `"Sampling is an davanced features"` 改成 `"Sampling is an advanced feature"`

#### 課程更新

**主 README.md**
- 在課程表中新增條目 5.17（基於 MCP 的對抗性多代理推理）並附上導向新課程的連結

**05-AdvancedTopics/README.md**
- 在課程列表表格新增課程 5.17 行

**study_guide.md**
- 在心智圖及進階主題的文字敘述中新增對抗性多代理推理主題

#### 程式碼與安全修正

**第05模組 - 對抗代理 (`mcp-adversarial-agents`)**
- **安全修正 — 命令注入**：將 TypeScript `run_python` 工具中的 `execSync` shell 插值替換為 `execFile` + `promisify`，消除命令注入風險（LLM 控制的程式碼現在作為字串參數傳遞，無 shell 參與）
- **MCP 工具迴圈連線**：更新 Python 辯論協調器使用非同步 `AsyncAnthropic` 客戶端（取代同步阻塞 `Anthropic`），在每個代理回合直接傳遞有效的 `ClientSession`，透過 `session.list_tools()` 每回合獲取工具定義，並在迴圈中使用 `session.call_tool()` 發送 `tool_use` 區塊直到模型產生最終文字回應

#### 依賴更新

- 將多個套件（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中的 `hono` 升級到 4.12.12
- TypeScript 套件中將 `@hono/node-server` 從 1.19.11 升級至 1.19.13
- Python 套件（10-StreamliningAIWorkflows 實驗室 3 和 4）將 `cryptography` 從 46.0.5 升級到 46.0.7
- 將 10-StreamliningAIWorkflows 檢視工具中的 `lodash` 從 4.17.23 升級到 4.18.1

#### 翻譯

- 同步超過 48 種語言的翻譯，更新至最新原始碼變更（i18n 更新）

---

## 2026年2月5日

### 全倉庫驗證與導覽改進

#### 新增課程內容

**第03模組 - 入門**
- **12-mcp-hosts/README.md**：MCP 主機設置完整指南
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置示例
  - 所有主要主機的 JSON 配置模板
  - 傳輸類型比較表（stdio、SSE/HTTP、WebSocket）
  - 常見連線問題排解
  - 主機安全設定最佳實踐

- **13-mcp-inspector/README.md**：MCP Inspector 除錯指南
  - 安裝方式（npx、npm 全域、原始碼）
  - 透過 stdio 及 HTTP/SSE 連接伺服器
  - 測試工具、資源與提示詞工作流程
  - VS Code 與 MCP Inspector 整合
  - 常見除錯場景與解決方案

**第04模組 - 實作與應用**
- **pagination/README.md**：分頁實作指南
  - Python、TypeScript、Java 的基於游標分頁範式
  - 用戶端分頁處理
  - 游標設計策略（不透明 vs 結構化）
  - 效能優化建議

**第05模組 - 進階主題**
- **mcp-protocol-features/README.md**：協議新特性深度解析
  - 進度通知實作
  - 請求取消模式
  - URI 模式的資源模板
  - 伺服器生命週期管理
  - 日誌等級控制
  - JSON-RPC 錯誤處理模式

#### 導覽修正（24+ 檔案更新）

**主要模組 README**
- 新增連結指向第一節與下一模組

**02-Security 子文件**
- 5 篇安全補充文件均加上「後續內容」導覽：

**09-案例研究**
- 所有案例研究文件均加上順序導覽：

**10-StreamliningAI 實驗室**
新增「後續內容」區塊於模組 10 總覽及模組 11

#### 程式碼與內容修正

**SDK 與依賴更新**
修正空白的 openai 版本號為 `^4.95.0`  
SDK 版本從 `^1.8.0` 更新到 `>=1.26.0`  
mcp 版本標記更新為 `>=1.26.0`

<strong>程式碼修正</strong>
修正無效模型 `gpt-4o-mini` 改為 `gpt-4.1-mini`

<strong>內容修正</strong>
修正壞掉的連結 `READMEmd` → `README.md`，課程標題 `Module 1-3` 改為 `Module 0-3`，修正大小寫錯誤路徑  
移除損毀的重複案例研究 5 內容

<strong>初學者指引提升</strong>
新增合適的介紹、學習目標及先決條件

#### 課程更新

**主 README.md**
- 新增條目 3.12（MCP 主機）、3.13（MCP Inspector）、4.1（分頁）、5.16（協議特性）於課程列表

**模組 README**
- 新增課程 12 和 13 至課程列表  
- 新增實作指南區塊含分頁連結  
- 新增課程 5.15（自訂傳輸）、5.16（協議特性）

**study_guide.md**
- 更新心智圖，新增 MCP 主機設定、MCP Inspector、分頁策略、協議特性深度解析等主題

## 2026年1月28日

### MCP 規範 2025-11-25 相容性檢視

#### 核心概念強化 (01-CoreConcepts/)
- **新增客戶端原語 - Roots**：紀錄完整文檔，Roots 客戶端原語讓伺服器理解檔案系統邊界與存取權限
- <strong>工具註解</strong>：新增工具行為註解文檔（`readOnlyHint`、`destructiveHint`），利於工具執行決策
- **Sampling 中的工具呼叫**：更新 Sampling 文件，新增 `tools` 及 `toolChoice` 參數支持模型驅動的工具呼叫
- **URL 模式誘導**：補充 URL 方式誘導，用於伺服器發起外部網路互動
- **任務（實驗性）**：新增任務功能章節，說明持久化執行封裝及延遲結果檢索
- <strong>圖示支持</strong>：指出工具、資源、資源模板與提示詞均可包含圖示作為額外元資料

#### 文件更新
- **README.md**：新增 MCP 規範 2025-11-25 版本參考及依日期版本控管說明
- **study_guide.md**：更新課程地圖，於核心概念章節加入任務與工具註解，更新文件時間戳記

#### 規範合規驗證
- <strong>協議版本</strong>：確認所有文件參考最新 MCP 規範 2025-11-25
- <strong>架構一致性</strong>：確認雙層架構（資料層 + 傳輸層）文件準確
- <strong>原語文件</strong>：驗證伺服器原語（資源、提示詞、工具）及客戶端原語（Sampling、誘導、日誌、Roots）文件
- <strong>傳輸機制</strong>：確認 STDIO 與可串流 HTTP 傳輸描述正確
- <strong>安全指引</strong>：符合現行 MCP 安全最佳實踐文件

#### 重要 MCP 2025-11-25 新功能紀錄
- **OpenID Connect 探索**：OIDC 認證伺服器探索
- **OAuth 用戶端 ID 元資料文件**：建議的客戶端註冊機制
- **JSON Schema 2020-12**：MCP 預設的 schema 方言
- **SDK 分層系統**：正式化 SDK 功能支援與維護規範
- <strong>治理結構</strong>：正式定義 MCP 的工作組與利益團體

### 安全文件重大更新 (02-Security/)

#### MCP 安全峰會工作坊 (Sherpa) 整合
- <strong>新增實作培訓資源</strong>：於所有安全文檔中整合完整的 [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) 內容
- <strong>遠征路線詳述</strong>：記錄從基地營到峰會完整營地進度
- **與 OWASP 對應**：所有安全指引映射至 OWASP MCP Azure Security Guide 風險清單

#### OWASP MCP Top 10 整合
- <strong>新增章節</strong>：主安全 README 加入 OWASP MCP Top 10 安全風險表及 Azure 減緩建議
- <strong>基於風險的文件</strong>：在 mcp-security-controls-2025.md 中加入 OWASP MCP 風險參考（MCP01-MCP08）
- <strong>參考架構</strong>：連結至 OWASP MCP Azure Security Guide 參考架構與實作範式

#### 安全文件更新
- **README.md**：加入 Sherpa 工作坊簡介、遠征路線表、OWASP MCP Top 10 摘要及實作培訓章節
- **mcp-security-controls-2025.md**：更新標題為 2026年2月，新增 OWASP 風險註記（MCP01-MCP08），修正規範版本不一致問題
- **mcp-security-best-practices-2025.md**：加入 Sherpa 及 OWASP 資源章節，更新時間戳
- **mcp-best-practices.md**：新增帶 Sherpa 和 OWASP 連結的實作培訓章節
- **azure-content-safety-implementation.md**：新增 OWASP MCP06 參考，Sherpa 營地 3 對應，及附加資源章節

#### 新增資源連結
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- 單獨 OWASP MCP 風險頁面（MCP01-MCP10）

### 全課程 MCP 規範 2025-11-25 對齊

#### 第03模組 - 入門
- **SDK 文件**：新增 Go SDK 至官方 SDK 清單；更新所有 SDK 參考以符合 MCP 規範 2025-11-25
- <strong>傳輸說明</strong>：更新 STDIO 與 HTTP 串流傳輸描述加入明確規範引用

#### 第04模組 - 實作與應用
- **SDK 更新**：新增 Go SDK；修訂 SDK 清單包含規範版本參考
- <strong>授權規範</strong>：將 MCP 授權規範連結更新至 2025-11-25 版本

#### 第05模組 - 進階主題
- <strong>新功能</strong>：補充 MCP 規範 2025-11-25 新功能說明（任務、工具註解、URL 模式誘導、Roots）
- <strong>安全資源</strong>：添加 OWASP MCP Top 10 與 Sherpa 工作坊連結於附加參考

#### 第06模組 - 社群貢獻
- **SDK 清單**：新增 Swift 與 Rust SDK；更新 MCP 規範連結至 2025-11-25
- <strong>規範參考</strong>：更新 MCP 規範連結指向官方規範 URL

#### 第07模組 - 早期採用經驗
- <strong>資源更新</strong>：新增 MCP 規範 2025-11-25 連結及 OWASP MCP Top 10 于附加資源中

#### 第08模組 - 最佳實踐
- <strong>規範版本</strong>：更新 MCP 規範參考為 2025-11-25
- <strong>安全資源</strong>：新增 OWASP MCP Top 10 與 Sherpa 工作坊連結於附加資源

#### 第10模組 - AI 工作流程精簡
- <strong>徽章更新</strong>：將 MCP 版本徽章從 SDK 版本（1.9.3）改為規範版本（2025-11-25）
- <strong>資源連結</strong>：更新 MCP 規範連結並新增 OWASP MCP Top 10

#### 第11模組 - MCP 伺服器實作實驗室
- <strong>規範連結</strong>：更新 MCP 規範連結至 2025-11-25 版本
- <strong>安全資源</strong>：新增 OWASP MCP Top 10 至官方資源列表

## 2025年12月18日
### 安全文件更新 - MCP 規範 2025-11-25

#### MCP 安全最佳實踐 (02-Security/mcp-best-practices.md) - 規範版本更新
- <strong>協議版本更新</strong>：更新至最新 MCP 規範 2025-11-25（於 2025 年 11 月 25 日發布）
  - 更新所有規範版本參考從 2025-06-18 至 2025-11-25
  - 更新文件日期參考從 2025 年 8 月 18 日至 2025 年 12 月 18 日
  - 驗證所有規範網址指向最新文件
- <strong>內容驗證</strong>：針對最新標準全面驗證安全最佳實踐
  - <strong>微軟安全解決方案</strong>：確認 Prompt Shields（前稱「越獄風險檢測」）、Azure Content Safety、Microsoft Entra ID 及 Azure Key Vault 的現用術語與連結
  - **OAuth 2.1 安全**：確認與最新 OAuth 安全最佳實踐保持一致
  - **OWASP 標準**：驗證 LLM 相關 OWASP Top 10 參考依然最新
  - **Azure 服務**：確認所有微軟 Azure 文件連結和最佳實踐
- <strong>標準符合性</strong>：所有引用安全標準均確認為最新
  - NIST AI 風險管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳實踐
  - Azure 安全性與合規框架
- <strong>實作資源</strong>：確認所有實作指南連結及資源
  - Azure API 管理身份認證範例
  - Microsoft Entra ID 整合指南
  - Azure Key Vault 秘密管理
  - DevSecOps 流程與監控解決方案

### 文件品質保證
- <strong>規範符合性</strong>：確保所有強制 MCP 安全要求（必須/必不得）與最新版規範一致
- <strong>資源新穎度</strong>：驗證所有外部連結指向微軟文件、安全標準與實作指南
- <strong>最佳實踐涵蓋範圍</strong>：確認涵蓋身份驗證、授權、AI 特定威脅、供應鏈安全及企業模式

## 2025 年 10 月 6 日

### 入門章節擴展 – 進階伺服器使用與簡單認證

#### 進階伺服器使用 (03-GettingStarted/10-advanced)
- <strong>新增章節</strong>：引入全面進階 MCP 伺服器使用指南，涵蓋常規與低階伺服器架構
  - <strong>常規與低階伺服器比較</strong>：詳細比較並提供 Python 與 TypeScript 範例代碼
  - **基於 Handler 的設計**：說明 handler 為核心的工具/資源/提示管理，用於可擴展且靈活的伺服器實作
  - <strong>實務範例</strong>：展示低階伺服器設計模式於進階功能與架構的應用場景

#### 簡單認證 (03-GettingStarted/11-simple-auth)
- <strong>新增章節</strong>：逐步指導 MCP 伺服器中實作簡易身份驗證
  - <strong>認證概念</strong>：明確闡述認證與授權差異及憑證處理
  - <strong>基本認證實作</strong>：中介軟體身份驗證模式於 Python (Starlette) 與 TypeScript (Express) 範例代碼
  - <strong>朝向進階安全發展</strong>：引導從簡單認證進階至 OAuth 2.1 及基於角色的存取控制（RBAC），附帶進階安全模組參考

此新增內容提供實務、操作指引，有助於構建更強大、安全與靈活的 MCP 伺服器實作，串接基礎概念與進階生產模式。

## 2025 年 9 月 29 日

### MCP 伺服器資料庫整合實驗室 - 全面實務學習路徑

#### 11-MCPServerHandsOnLabs - 新增完整資料庫整合課程
- **完整 13 實驗學習路徑**：新增針對生產就緒 MCP 伺服器與 PostgreSQL 資料庫整合的全面實驗課程
  - <strong>真實案例實作</strong>：Zava Retail 零售分析案例展示企業級模式
  - <strong>結構化學習進程</strong>：
    - **實驗 00-03：基礎** — 介紹、核心架構、安全性與多租戶、環境設定
    - **實驗 04-06：建置 MCP 伺服器** — 資料庫設計與結構、MCP 伺服器實作、工具開發
    - **實驗 07-09：高階功能** — 語意搜尋整合、測試與除錯、VS Code 整合
    - **實驗 10-12：生產與最佳實踐** — 部署策略、監控與觀察性、最佳實踐與優化
  - <strong>企業技術</strong>：FastMCP 框架、PostgreSQL 搭配 pgvector、Azure OpenAI Embeddings、Azure Container Apps、Application Insights
  - <strong>高階功能</strong>：行級安全（RLS）、語意搜尋、多租戶資料存取、向量嵌入、實時監控

#### 術語標準化 - 模組改為實驗
- <strong>全面文件更新</strong>：系統性將 11-MCPServerHandsOnLabs 內所有 README 文件中「Module」術語替換為「Lab」
  - <strong>章節標題</strong>：將「What This Module Covers」更新為「What This Lab Covers」遍及 13 個實驗
  - <strong>內容描述</strong>：將「This module provides...」改為「This lab provides...」
  - <strong>學習目標</strong>：將「By the end of this module...」改為「By the end of this lab...」
  - <strong>導航連結</strong>：所有「Module XX:」參考更換為「Lab XX:」
  - <strong>完成追蹤</strong>：將「After completing this module...」改為「After completing this lab...」
  - <strong>技術參考保持</strong>：維持 Python 模組設定引用（例如 `"module": "mcp_server.main"`）

#### 學習指南增強 (study_guide.md)
- <strong>視覺課程地圖</strong>：新增「11. 資料庫整合實驗室」章節並包含完整實驗結構視覺化
- <strong>程式庫結構</strong>：從十個主要章節更新為十一個，詳細說明 11-MCPServerHandsOnLabs
- <strong>學習路徑引導</strong>：強化導航指引涵蓋 00-11 章節
- <strong>技術涵蓋</strong>：新增 FastMCP、PostgreSQL、Azure 服務整合細節
- <strong>學習成效</strong>：強調生產就緒伺服器開發、資料庫整合模式與企業安全

#### 主要 README 結構增強
- <strong>基於實驗的術語</strong>：11-MCPServerHandsOnLabs 主 README.md 一致使用「Lab」結構
- <strong>學習路徑組織</strong>：清晰呈現從基礎到進階實作至生產部署的學習流程
- <strong>現實世界聚焦</strong>：強調實務操作及企業級技術與模式

### 文件品質與一致性改進
- <strong>強化實務學習</strong>：整體文件加強實驗室導向
- <strong>企業模式聚焦</strong>：突出生產就緒實作與企業安全考量
- <strong>技術整合</strong>：全面涵蓋現代 Azure 服務與 AI 整合模式
- <strong>學習進階</strong>：清晰結構化路徑涵蓋基礎至生產部署

## 2025 年 9 月 26 日

### 案例研究強化 - GitHub MCP Registry 整合

#### 案例研究 (09-CaseStudy/) - 生態系發展焦點
- **README.md**：大幅擴充，加入全面 GitHub MCP Registry 案例研究
  - **GitHub MCP Registry 案例研究**：全新深入探討 2025 年 9 月 GitHub MCP Registry 發布
    - <strong>問題解析</strong>：詳述 MCP 伺服器發現及部署分散挑戰
    - <strong>解決架構</strong>：GitHub 集中註冊機制與一鍵 VS Code 安裝方案
    - <strong>商業影響</strong>：明顯提升開發者上手速度與生產力
    - <strong>策略價值</strong>：聚焦模組化代理部署與跨工具互操作性
    - <strong>生態系發展</strong>：定位基礎且核心平台，支持智能代理整合
  - <strong>增強案例研究架構</strong>：所有七個案例研究均更新格式統一，內容詳盡
    - Azure AI 旅遊代理：多代理協同重點
    - Azure DevOps 整合：工作流程自動化焦點
    - 即時文件檢索：Python 控制台用戶端實作
    - 互動式學習計畫產生器：Chainlit 對話式網頁應用
    - 編輯器內文件：VS Code 與 GitHub Copilot 整合
    - Azure API 管理：企業 API 整合模式
    - GitHub MCP Registry：生態系發展與社區平臺
  - <strong>綜合結論</strong>：重寫結論部分，高度強調涵蓋多元 MCP 實作面向的七大案例研究
    - 企業整合、多代理協同、開發者生產力
    - 生態系發展、教育應用分類
    - 加強建築模式、實作策略及最佳實踐洞察
    - 強調 MCP 為成熟、生產就緒協議

#### 學習指南更新 (study_guide.md)
- <strong>視覺課程地圖</strong>：更新心智圖納入 GitHub MCP Registry 案例研究
- <strong>案例研究描述</strong>：由一般描述擴充為七個詳細案例細分說明
- <strong>程式庫結構</strong>：更新第 10 章反映完整案例研究涵蓋與實作細節
- <strong>變更記錄融合</strong>：新增 2025 年 9 月 26 日條目，記錄 GitHub MCP Registry 及案例研究增強
- <strong>日期更新</strong>：更新頁尾時間戳為最新版本（2025 年 9 月 26 日）

### 文件品質改進
- <strong>一致性強化</strong>：七個案例均落實統一格式與結構
- <strong>完整涵蓋範圍</strong>：案例涵蓋企業、開發者生產力、生態系場景
- <strong>策略定位</strong>：突出 MCP 作為智能代理系統部署基石的核心地位
- <strong>資源整合</strong>：更新附加資源，包含 GitHub MCP Registry 連結

## 2025 年 9 月 15 日

### 進階主題擴展 - 自訂傳輸與上下文工程

#### MCP 自訂傳輸 (05-AdvancedTopics/mcp-transport/) - 全新進階實作指南
- **README.md**：完整自訂 MCP 傳輸機制實作指南
  - **Azure Event Grid 傳輸**：全面伺服器無伺服器事件驅動傳輸實作
    - C#、TypeScript 與 Python 範例結合 Azure Functions
    - 事件驅動架構模式，支援可擴展 MCP 解決方案
    - Webhook 接收器與推送訊息處理
  - **Azure Event Hubs 傳輸**：高吞吐量串流傳輸實作
    - 支援低延遲場景的實時串流能力
    - 分區策略與檢查點管理
    - 訊息批次處理與效能優化
  - <strong>企業整合模式</strong>：生產就緒架構範例
    - 多重 Azure Functions 分散 MCP 處理
    - 混合傳輸架構結合多種傳輸類型
    - 訊息持久性、可靠性與錯誤處理策略
  - <strong>安全與監控</strong>：Azure Key Vault 整合與可觀察性模式
    - 管理身份驗證與最小權限訪問
    - Application Insights 遙測與效能監控
    - 斷路器與容錯模式
  - <strong>測試框架</strong>：自訂傳輸完整測試策略
    - 單元測試與假件模擬框架
    - Azure 測試容器整合測試
    - 效能與負載測試措施

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新興 AI 領域
- **README.md**：全面探討上下文工程作為新興領域
  - <strong>核心原則</strong>：完整上下文共享、行動決策感知及上下文視窗管理
  - **MCP 協議對齊**：MCP 設計如何因應上下文工程挑戰
    - 上下文視窗限制與漸進式載入策略
    - 關聯性判定與動態上下文檢索
    - 多模態上下文處理與安全性考量
  - <strong>實作方法</strong>：單線程與多代理架構比較
    - 上下文切片與優先排序技術
    - 漸進式上下文載入與壓縮策略
    - 分層上下文方法與檢索優化
  - <strong>衡量框架</strong>：上下文效果評估的新興指標
    - 輸入效率、效能、品質與用戶體驗考量
    - 上下文優化實驗性方法
    - 失效分析與改善方法論

#### 課程導航更新 (README.md)
- <strong>模組結構增強</strong>：更新課程表含新增進階主題
  - 新增上下文工程 (5.14) 與自訂傳輸 (5.15) 條目
  - 全模組格式與導航連結一致化
  - 更新描述以反映當前內容範圍

### 目錄結構改進
- <strong>命名標準化</strong>：將「mcp transport」重新命名為「mcp-transport」，與其他進階主題資料夾一致
- <strong>內容組織</strong>：所有 05-AdvancedTopics 資料夾統一命名格式（mcp-[主題]）

### 文件品質提升
- **MCP 規範對齊**：所有新內容參考當前 MCP 規範 2025-06-18
- <strong>多語言範例</strong>：C#、TypeScript 與 Python 完整程式碼示例
- <strong>企業聚焦</strong>：生產就緒模式與 Azure 雲端整合貫穿全篇
- <strong>視覺文件</strong>：使用 Mermaid 圖示架構與流程視覺化

## 2025 年 8 月 18 日

### 文件全面更新 - MCP 2025-06-18 標準

#### MCP 安全最佳實踐 (02-Security/) - 全面現代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：完全重寫，符合 MCP 規範 2025-06-18
  - <strong>強制要求</strong>：新增官方規範中的明確 MUST/MUST NOT 要求，並附清晰視覺標示
  - **12 核心安全實踐**：由 15 項列表重組為全面安全領域
    - 代幣安全與身份驗證，整合外部身份提供者
    - 會話管理與傳輸安全，包含密碼學要求
    - AI 專用威脅防護，整合 Microsoft Prompt Shields
    - 訪問控制與權限，遵循最小權限原則
    - 內容安全與監控，整合 Azure Content Safety
    - 供應鏈安全，包含全面組件驗證
    - OAuth 安全與混淆代理防護，實施 PKCE
    - 事件響應與復原，具自動化能力
    - 法規遵循與治理，符合相關法規要求
    - 先進安全控制，採用零信任架構
    - Microsoft 安全生態系統整合，提供全面解決方案
    - 持續安全演進，採用自適應實踐
  - **Microsoft 安全解決方案**：強化 Prompt Shields、Azure Content Safety、Entra ID 與 GitHub Advanced Security 的整合指引
  - <strong>實施資源</strong>：依官方 MCP 文件、Microsoft 安全解決方案、安全標準及實施指南分類的綜合資源連結

#### 先進安全控制 (02-Security/) - 企業實施
- **MCP-SECURITY-CONTROLS-2025.md**：全面改版，採用企業級安全框架
  - **9 大綜合安全領域**：由基本控制擴展為詳細企業框架
    - 先進驗證與授權，整合 Microsoft Entra ID
    - 代幣安全與反偽冒控管，全面驗證
    - 會話安全控管，防範劫持
    - AI 專用安全控管，防範提示注入與工具中毒
    - 混淆代理攻擊防護，OAuth 代理安全
    - 工具執行安全，沙盒與隔離
    - 供應鏈安全控管，依賴項驗證
    - 偵測與監控控管，整合 SIEM
    - 事件響應與復原，自動化能力
  - <strong>實作範例</strong>：新增詳細 YAML 配置區塊與程式碼範例
  - **Microsoft 解決方案整合**：涵蓋 Azure 安全服務、GitHub Advanced Security 及企業身份管理

#### 進階主題安全 (05-AdvancedTopics/mcp-security/) - 量產級實施
- **README.md**：全面重寫企業安全實施指南
  - <strong>當前規範對齊</strong>：更新至 MCP 規範 2025-06-18，附強制安全要求
  - <strong>強化身份驗證</strong>：整合 Microsoft Entra ID，提供完整 .NET 與 Java Spring Security 範例
  - **AI 安全整合**：Microsoft Prompt Shields 與 Azure Content Safety 實作，附詳細 Python 範例
  - <strong>先進威脅緩解</strong>：完整實作範例涵蓋
    - 混淆代理攻擊防護，PKCE 與使用者同意驗證
    - 代幣穿透防護，受眾驗證與安全代幣管理
    - 會話劫持防護，密碼學綁定與行為分析
  - <strong>企業安全整合</strong>：Azure Application Insights 監控、威脅偵測管線與供應鏈安全
  - <strong>實施清單</strong>：明確強制與建議安全控管，以及 Microsoft 安全生態系統優勢

### 文件品質與標準對齊
- <strong>規範引用</strong>：更新所有參考至現行 MCP 規範 2025-06-18
- **Microsoft 安全生態系統**：全文件強化整合指導
- <strong>實務實作</strong>：新增完整 .NET、Java 及 Python 範例，呈現企業化架構
- <strong>資源組織</strong>：官方文件、安全標準與實施指南分類完善
- <strong>視覺標示</strong>：強制要求與建議實踐清晰標記

#### 核心概念 (01-CoreConcepts/) - 全面現代化
- <strong>協議版本更新</strong>：改為參考現行 MCP 規範 2025-06-18，採用日期版次（YYYY-MM-DD 格式）
- <strong>架構細化</strong>：強化對 Hosts、Clients 及 Servers 的描述，符合現行 MCP 架構範式
  - Hosts 明確定義為協調多個 MCP 客戶端連線的 AI 應用
  - Clients 描述為保持一對一伺服器關係的協議連接器
  - Servers 強化本地與遠端部署場景說明
- <strong>原始構造重組</strong>：完整改寫伺服器與客戶端的基元
  - 伺服器基元：資源（資料來源）、提示（模板）、工具（可執行功能），附詳細說明與範例
  - 客戶端基元：抽樣（LLM 完成）、引導（使用者輸入）、紀錄（偵錯/監控）
  - 更新採用現行的發現（`*/list`）、取回（`*/get`）及執行（`*/call`）方法模式
- <strong>協議架構</strong>：引入雙層架構模型
  - 資料層：JSON-RPC 2.0 基礎，含生命週期管理與基元
  - 傳輸層：STDIO（本地）與支持 SSE 的串流 HTTP（遠端）傳輸機制
- <strong>安全框架</strong>：全面安全原則，包含明確使用者同意、資料隱私保護、工具安全執行與傳輸安全
- <strong>通訊模式</strong>：更新協議訊息以展示初始化、發現、執行及通知流程
- <strong>程式碼範例</strong>：刷新多語言範例（.NET、Java、Python、JavaScript），符合現行 MCP SDK 模式

#### 安全 (02-Security/) - 全面安全改造  
- <strong>標準對齊</strong>：完全符合 MCP 規範 2025-06-18 的安全要求
- <strong>認證演進</strong>：記錄從自訂 OAuth 伺服器至外部身份提供者委派（Microsoft Entra ID）的演變
- **AI 專用威脅分析**：強化現代 AI 攻擊向量說明
  - 詳盡的提示注入攻擊場景與實例
  - 工具中毒機制及「地毯式攻擊」模式
  - 上下文視窗中毒與模型混淆攻擊
- **Microsoft AI 安全解決方案**：全面涵蓋 Microsoft 安全生態系統
  - AI Prompt Shields，具先進偵測、聚焦及分隔符技術
  - Azure Content Safety 整合範例
  - GitHub Advanced Security 用於供應鏈保護
- <strong>先進威脅緩解</strong>：詳細安全控管涵蓋
  - 會話劫持，含 MCP 特定攻擊案例與密碼學會話 ID 要求
  - MCP 代理場景中的混淆代理問題，附明確同意要求
  - 代幣穿透弱點，附強制驗證控管
- <strong>供應鏈安全</strong>：擴展 AI 供應鏈涵蓋，包含基礎模型、嵌入服務、上下文供應方及第三方 API
- <strong>基礎安全</strong>：增強與企業安全模式整合，包括零信任架構及 Microsoft 安全生態系統
- <strong>資源組織</strong>：依類型分類全面資源連結（官方文件、標準、研究、Microsoft 解決方案、實施指南）

### 文件品質提升
- <strong>結構化學習目標</strong>：強化具體且可操作的學習目標
- <strong>交叉參照</strong>：新增相關安全與核心概念主題間連結
- <strong>最新資訊</strong>：更新所有日期與規範連結至現行標準
- <strong>實作指導</strong>：兩大章節中加入具體且可操作的實施指南

## 2025 年 7 月 16 日

### README 與導航改進
- 全面重新設計 README.md 中的課程導航
- 將 `<details>` 標籤替換為更易用的表格格式
- 新建 "alternative_layouts" 目錄，提供多種排版選項
- 新增卡片式、分頁式及手風琴式導航範例
- 更新版本庫結構章節，涵蓋所有最新檔案
- 加強「如何使用此課程」說明，明確推薦策略
- 更新 MCP 規範連結指向正確 URL
- 新增課程結構中的 Context Engineering 節（5.14）

### 學習指南更新
- 完全修訂學習指南以符合最新版本庫結構
- 新增 MCP 客戶端與工具章節，以及熱門 MCP 伺服器內容
- 更新視覺課程圖以精確反映所有主題
- 強化進階主題描述，涵蓋所有專業領域
- 更新案例研究章節，反映實際範例
- 增加本次全面變更記錄

### 社群貢獻 (06-CommunityContributions/)
- 新增關於用於圖像生成的 MCP 伺服器詳細資訊
- 新增在 VSCode 使用 Claude 的完整說明
- 新增 Cline 終端客戶端設定及使用指引
- 更新 MCP 客戶端章節，包含所有熱門客戶端選項
- 強化貢獻範例，提供更精確程式碼片段

### 先進主題 (05-AdvancedTopics/)
- 一致命名組織所有專業主題資料夾
- 新增上下文工程相關素材與實例
- 新增 Foundry 代理整合文件
- 強化 Entra ID 安全整合文件

## 2025 年 6 月 11 日

### 初始建立
- 發佈 MCP 初學者課程第一版
- 建立 10 大主題基礎架構
- 實作視覺課程地圖以利導航
- 新增多語言範例專案

### 入門指南 (03-GettingStarted/)
- 創建首批伺服器實作範例
- 新增客戶端開發指導
- 加入 LLM 客戶端整合說明
- 提供 VS Code 整合文檔
- 實作 Server-Sent Events (SSE) 伺服器範例

### 核心概念 (01-CoreConcepts/)
- 詳解客戶端-伺服器架構
- 撰寫主要協議元件文件
- 記錄 MCP 中之訊息模式

## 2025 年 5 月 23 日

### 版本庫結構
- 初始化版本庫，建構基本資料夾結構
- 為各主要章節建立 README 文件
- 搭建翻譯基礎設施
- 新增影像資產與圖表

### 文件
- 創建初版 README.md，概述課程內容
- 新增 CODE_OF_CONDUCT.md 與 SECURITY.md
- 設立 SUPPORT.md，提供求助指引
- 建構初步學習指南結構

## 2025 年 4 月 15 日

### 規劃與架構
- MCP 初學者課程初期規劃
- 定義學習目標與對象
- 梳理課程 10 大章節結構
- 建立範例與案例研究的概念架構
- 創建關鍵概念的初始示範範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言文件應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
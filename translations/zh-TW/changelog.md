# 更新日誌：初學者 MCP 課程

本文件作為對 Model Context Protocol (MCP) 初學者課程所有重大變更的記錄。變更以逆時間順序記錄（最新變更優先）。

## 2026 年 7 月 29 日

### 新模組 08 伴隨課程：可靠性 Sidecars 與安全重試

新增一個對 MCP 工具廠商中立的伴隨課程，適用於產生真實世界
效果，與最終 `2026-07-28` 規範保持一致。

- <strong>新增</strong>：[reliability-sidecar 可靠性 sidecar 伴隨課程]
  採用一個支援工單故事、兩個 Mermaid 圖，以及一個重試決策
  流程來說明穩定操作鍵、原子重複授權、
  協調、證據與 Tasks 擴展邊界。
- <strong>新增</strong>：一個標準程式庫的 Python 和 SQLite 故障注入練習
  使用分開的操作和工單資料庫以演示外部效果提交後
  響應遺失的情況。六個確定性測試涵蓋天真的
  複製、守護啟動重啟恢復、載荷衝突、緩存結果、
  活躍請求，以及同時重複授權。
- <strong>更新</strong>：模組 08 現在連結伴隨課程，確定
  最終 `2026-07-28` 無狀態請求模型，區分 OpenTelemetry
  可觀測性與已棄用的 MCP 紀錄功能，並限制其
  通用重試範例只能用於唯讀操作。
- <strong>可選</strong>：該課程將可攜概念對應到一個標記的社群
  實作，且不將託管服務或網路呼叫納入
  練習範圍內。

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026 年 7 月 2 日

### 新課程：2026-07-28 MCP 規範釋出候選版本

補充即將推出的 `2026-07-28` MCP 規範釋出候選版本（2026 年 5 月 21 日宣布；最終發布預定於 7 月 28 日），內容摘自[官方公告部落格文章](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)。課程基線仍為 **MCP 規範 2025-11-25**，直到新版本釋出，因此此為前瞻指導，而非現有課程的重寫。

- <strong>新增</strong>：[01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — 全面覆蓋無狀態協議核心（移除 `initialize` 握手與 `Mcp-Session-Id`）、新的 `Mcp-Method`/`Mcp-Name` 路由標頭、`ttlMs`/`cacheScope` 快取元資料、_meta 中的 W3C Trace Context、正式 Extensions 框架（MCP 應用及新 Tasks 擴展）、六項授權強化 SEP、Roots/Sampling/Logging 的廢止，及工具架構轉向完全使用 JSON Schema 2020-12。
- <strong>更新</strong>，加入前瞻提示並連結至新課程：
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md)：協議版本說明、Sampling/Roots/Logging/Tasks 節點，以及「接下來做什麼」

  - [02-Security/README.md](./02-Security/README.md)：授權強化提示
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md)：無狀態傳輸提示
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md)：取樣棄用提示
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md)：日誌棄用及任務擴展提示
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md)：無狀態/會話路由提示
  - [README.md](./README.md)：「展望未來」規範部分說明及課程模組表新增 `1.1` 項目
  - [study_guide.md](./study_guide.md)：核心概念總覽中前瞻性重點及附上日期的補充說明
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md)：無狀態請求模型前關於 `mcp-session-id` 傳輸映射的說明
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md)：模組總覽中針對根上下文/取樣棄用及任務擴展的說明
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md)：授權強化提示

## 2026 年 6 月 24 日

### 新課程：在 Copilot 應用中使用 MCP

- [工具部分](./12-tooling/README.md) 新增工具部分。
- [Copilot 應用中的 MCP](./12-tooling/01-copilot-app/README.md)

## 2026 年 6 月 16 日

### MCP 規範對齊與範例驗證

已針對目前 **MCP 規範 2025-11-25** 與最新官方 SDK 驗證課程，修正剩餘過時的規範參考，並確認核心範例仍能建置與執行。

#### 規範版本修正 (2025-06-18 / 2025-03-26 → 2025-11-25)

更新英文內容中仍標示舊版規範為<em>當前/最新</em>標準的部分，並將連結重新指向權威的 `modelcontextprotocol.io` 規範路徑：
- **05-AdvancedTopics/mcp-security/README.md**：更新「當前標準」橫幅、介紹、核心安全原則標題、強制要求標題、Microsoft Entra ID 章節、參考資源連結及結尾安全通知（8 處引用）為 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**：更新額外資源規範連結及「當前標準」橫幅為 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**：以現行 2025-11-25 的安全最佳實踐頁面取代過時的 `2025-03-26` 安全與信任連結

- **03-GettingStarted/14-sampling/README.md**: 更新官方採樣文件連結至 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: 將現在時態的「當前 MCP 規範」參考和附加資源規範連結更新至 2025-11-25（歷史 SSE 棄用說明保持不變以確保準確性）

#### 根據最新 SDK 進行範例驗證

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` 解決了 `@modelcontextprotocol/sdk@1.29.0`；`tsc --noEmit` 通過無類型錯誤 — 現有 `McpServer`/`StdioServerTransport` API 依然有效
- **Python (03-GettingStarted/01-first-server/solution/python)**: 在獨立的 `.venv` 使用 `mcp[cli]`（1.27.2）驗證；`py_compile` 通過，`FastMCP.list_tools()` 正確返回了 `add` 和 `subtract` 工具
- 確認所有樣本 `@modelcontextprotocol/sdk` 版本範圍（`>=1.26.0` / `^1.26.0` / `^1.27.0`）均能順利解析到目前的 `1.29.0`，且無破壞性 API 變更

#### 相依鎖定版本調整（縮小版本差距）

將過時的 SDK 鎖定版本提升，使每個範例跟蹤當前 MCP 發行版，符合整個倉庫慣例：
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: 將 `@modelcontextprotocol/sdk` 從 `^1.8.0` 提升為 `>=1.26.0`，並更新過時的「updated for MCP 2025-06-18」套件描述為「aligned with MCP Specification 2025-11-25」
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** 與 **lab4/code/github_mcp_server/pyproject.toml**: 將準確的鎖定版本 `mcp==1.23.0` 提升為 `mcp>=1.26.0`；重新生成兩個 `uv.lock` 檔案（使用 `uv lock`），鎖定檔解析為當前的 `mcp 1.27.2`，並與清單保持同步

#### 課程差距分析 — 最新規範功能覆蓋

驗證課程已涵蓋 MCP 2025-11-25 中引入/擴展的所有基本功能，無內容缺口：
- **取樣（Sampling）**: 課程 03-GettingStarted/14-sampling 以及 05-AdvancedTopics/mcp-sampling
- **引導（包括 URL 模式）**: 文件在 01-CoreConcepts 和 05-AdvancedTopics/mcp-protocol-features 中說明
- **根（Roots）**: 文件在 00-Introduction、01-CoreConcepts 以及 05-AdvancedTopics/mcp-root-contexts 中說明
- **任務（實驗性、長時間運行操作）**: 文件在 01-CoreConcepts 及 05-AdvancedTopics/mcp-protocol-features 中說明
- <strong>工具註解</strong>（`readOnlyHint` / `destructiveHint`）: 文件在 01-CoreConcepts 及 05-AdvancedTopics/mcp-protocol-features 中說明

### 安全強化與相依漏洞修復

對所有依賴清單與範例原始碼進行全面安全掃描，並修復所有報告的 npm 警告與一項程式碼層級的安全問題。修復後，`npm audit` 在所有掃描目錄中均顯示 **0 漏洞**。

#### npm 依賴漏洞（間接）— 已修復

審核了所有 15 個提交的 `package-lock.json` 檔案。漏洞僅限於 MCP Inspector 開發工具、OpenAI 客戶端和 MCP SDK 所拉入的間接依賴；所有漏洞都已修復且未破壞範例：
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** 與 **lab3/code/weather_mcp/inspector**: 提升了 `@modelcontextprotocol/inspector`（`0.16.6` / `0.14.1` → `0.22.0`），清除了所夾帶的 `ajv`、`brace-expansion`、`diff`、`path-to-regexp` 和 `ws` 的安全警告。新增 npm `overrides` 條目，強制使用已修補的 `shell-quote@1.8.4`，消除了 `concurrently` 所帶來的剩餘嚴重警告；重新生成兩個鎖定檔（現在無任何漏洞）
- **03-GettingStarted/samples/typescript**: `npm audit fix` 將間接依賴 `qs`（中度）更新至已修補版本
- **03-GettingStarted/samples/javascript**: `npm audit fix` 將間接依賴 `hono`（中度）更新至已修補版本
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` 將間接依賴 `form-data`（高風險）更新至已修補版本
- **03-GettingStarted/11-simple-auth/solution/typescript**: 生成了缺失的 `package-lock.json`，確保專案可重現且可安全審核（0 漏洞）

#### 程式碼層級安全修復（OWASP A03: 注入攻擊）

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: 移除 `open_in_vscode` 工具中的 `shell=True`。先前的 `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` 允許資料夾路徑內的 shell 元字元被 `cmd.exe` 解讀（命令注入的風險）。現在改為直接執行解析後的 `Code.exe` 並以資料夾為參數 — 無 shell，功能等同且安全。

#### Python 依賴檢查

- 使用 `pip-audit` 審核所有 Python 需求套件。`05-AdvancedTopics` 與 `03-GettingStarted/samples/python` 報告 <strong>無已知漏洞</strong>（其 `mcp` / `httpx` / `pydantic` / `python-dotenv` 版本範圍均能解析至當前的修補版）
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` 發現間接依賴 **`werkzeug` 3.1.1** 含有三個 `safe_join` Windows 裝置名稱拒絕服務漏洞通知 — `CVE-2025-66221`、`CVE-2026-21860` 和 `CVE-2026-27199`（皆於 3.1.6 修復）。新增明確的安全版本鎖定 `werkzeug>=3.1.6`，以確保解析至修補版；並驗證此限制在 `chainlit` / `mcp` / `semantic-kernel` 堆疊下正常解析

### 產品名稱重新品牌化

更新所有課程內容以反映 Microsoft 的產品重新品牌策略：


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: 更新了 Discord 社群連結

- **AGENTS.md**: 更新 Discord 伺服器參考
- **README.md**: 更新技術生態系統參考
- **study_guide.md**: 更新案例研究參考
- **05-AdvancedTopics/README.md**: 更新第 5.13 單元標題與描述
- **05-AdvancedTopics/mcp-integration/README.md**: 更新章節標題與描述
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: 完整模組標題與內容更新
- **05-AdvancedTopics/mcp-security-entra/README.md**: 更新交叉參考連結
- **07-LessonsfromEarlyAdoption/README.md**: 更新案例研究參考
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: 更新第 9 章標題、徽章與功能
- **08-BestPractices/README.md**: 更新 Discord 社群連結
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: 更新 Discord 頻道參考
- **09-CaseStudy/docs-mcp/solution/python/README.md**: 更新模型部署參考
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: 更新 AI 服務表格
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: 更新資源參考

#### AI 工具組 / AITK → 微軟 Foundry 工具組擴充套件（VS Code）
- **README.md**: 更新主要課程參考
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: 更新模組標題、概述與所有模組標頭
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: 更新標題、學習目標、設定指示與資源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: 更新標題、學習目標、MCP 主機表格與交叉參考
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: 更新標題、徽章、先決條件與資源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: 更新代理建構者參考與回饋連結
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: 更新先決條件與擴充套件參考

---

## 2026 年 4 月 11 日

### 新課程、文件修正及依賴性更新

#### 新增課程內容

**第五單元 - 進階主題**
- **第五課 5.17：使用 MCP 進行對抗式多代理推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`)：新增全面指南，涵蓋多代理系統的對抗辯論模式
  - Mermaid 架構圖：兩個代理 → 共享 MCP 伺服器 → 辯論記錄 → 評審 → 裁決
  - 共享 MCP 工具伺服器 (`web_search` + `run_python`)，用 Python 和 TypeScript 實作
  - 對立系統提示（支持 / 反對 / 評審）附帶明確的工具使用要求
  - 使用 Python、TypeScript 與 C# 的辯論協調器，管理輪次並路由論點
  - MCP `ClientSession` 用於協調器實際工具呼叫連結
  - 使用案例表（幻覺偵測、威脅建模、API 設計審查、事實驗證、技術選擇）
  - 安全考量：沙箱執行、工具呼叫驗證、速率限制、審計日誌
  - 結構化練習包括三個實際場景（程式碼審查、架構決策、內容審核）

#### 文件修正

**第三單元 - 入門**
- **05-stdio-server/README.md**: 修正 TypeScript stdio 伺服器範例不完整 — 新增缺失的傳輸實例化（`new StdioServerTransport()`）及 `server.connect(transport)` 呼叫，使其與同章節的 Python 和 .NET 範例一致
- **14-sampling/README.md**: 修正錯字 — 將 `"Sampling is an davanced features"` 更正為 `"Sampling is an advanced feature"`

#### 課程更新

**主要 README.md**
- 在課程表中新增 5.17 節（使用 MCP 的對抗式多代理推理）並附上新課程直接連結

**05-AdvancedTopics/README.md**
- 在課程表新增第 5.17 課行

**study_guide.md**
- 在心智圖與進階主題說明中新增對抗式多代理推理主題

#### 程式碼與安全修正

**第五單元 - 對抗式代理 (`mcp-adversarial-agents`)**
- **安全修正 — 命令注入**：在 TypeScript `run_python` 工具中，將 `execSync` shell 插值替換為 `execFile` + `promisify` ，消除命令注入風險（LLM 控制的代碼現以字面 argv 元素傳遞，不涉及 shell）
- **MCP 工具循環接線**：更新 Python 辯論協調器使用 `AsyncAnthropic` 客戶端（取代阻塞同步 `Anthropic`），直接於每個代理回合傳遞實時 `ClientSession`，每回合通過 `session.list_tools()` 取得工具定義，並在循環中透過 `session.call_tool()` 發送 `tool_use` 區塊直到模型輸出最終文字回應

#### 依賴性更新

- 將多個套件（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中的 `hono` 升級至 4.12.12
- 將 TypeScript 套件中的 `@hono/node-server` 從 1.19.11 升級至 1.19.13
- 將 Python 套件（10-StreamliningAIWorkflows 的實驗 3 和 4）中的 `cryptography` 從 46.0.5 升級至 46.0.7
- 將 10-StreamliningAIWorkflows 檢查器的 `lodash` 從 4.17.23 升級至 4.18.1

#### 翻譯更新

- 對超過 48 種語言的翻譯與最新原文變更同步 (i18n 更新)

---

## 2026 年 2 月 5 日

### 全倉儲驗證與導航改進

#### 新增課程內容

**第三單元 - 入門**
- **12-mcp-hosts/README.md**: 新增完整 MCP 主機設定指南
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 設定範例
  - 所有主要主機的 JSON 設定範本
  - 傳輸類型比較表（stdio、SSE/HTTP、WebSocket）
  - 常見連線問題排解
  - 主機設定安全最佳實踐

- **13-mcp-inspector/README.md**: 新增 MCP Inspector 偵錯指南
  - 安裝方式（npx、npm 全域、原始碼）
  - 透過 stdio 及 HTTP/SSE 連接伺服器
  - 測試工具、資源與提示工作流程
  - VS Code 與 MCP Inspector 整合
  - 常見偵錯場景與解決方案

**第四單元 - 實作**
- **pagination/README.md**: 新增分頁實作指南
  - 在 Python、TypeScript、Java 中的基於游標分頁模式
  - 用戶端分頁操作
  - 游標設計策略（不透明 vs. 結構化）
  - 效能優化建議

**第五單元 - 進階主題**
- **mcp-protocol-features/README.md**: 新增協議功能深入解析
  - 進度通知實作
  - 請求取消模式
  - 帶 URI 模式的資源範本
  - 伺服器生命週期管理
  - 日誌等級控制
  - 帶 JSON-RPC 錯誤碼的錯誤處理模式

#### 導航修正（超過 24 個文件更新）

**主模組 README**
 現在鏈結第一課與下一模組

**02-Security 子文件**
- 所有 5 個安全補充文件均新增「下一步」導航：

**09-CaseStudy 文件**
- 所有案例研究文件均新增連續導航：

**10-StreamliningAI 實驗室**
在第 10 單元概述與第 11 單元新增「下一步」章節

#### 程式碼與內容修正

**SDK 與依賴更新**
修正空白 openai 版本為 `^4.95.0`
SDK 從 `^1.8.0` 更新到 `>=1.26.0`
MCP 版本標記更新為 `>=1.26.0`

<strong>程式碼修正</strong>
修正無效模型名稱 `gpt-4o-mini` 為 `gpt-4.1-mini`

<strong>內容修正</strong>
修正錯誤連結 `READMEmd` → `README.md`，修正課程標題 `Module 1-3` → `Module 0-3`，修正大小寫敏感路徑
移除破損的重複案例研究第 5 節內容

<strong>初學者指導改進</strong>
新增適當的介紹、學習目標與先決條件，提升初學者體驗

#### 課程更新

**主要 README.md**
- 在課程表中新增 3.12（MCP 主機）、3.13（MCP Inspector）、4.1（分頁）、5.16（協議功能）項目

**模組 README**
新增第 12 與 13 課至課程列表
新增實作指南區塊及分頁連結
新增第 5.15（自訂傳輸）與 5.16（協議功能）課程

**study_guide.md**
- 更新心智圖，包含所有新主題：MCP 主機設定、MCP Inspector、分頁策略、協議功能深入解析

## 2026 年 1 月 28 日

### MCP 規範 2025-11-25 相容性檢視

#### 核心概念增強（01-CoreConcepts/）
- **新增客戶端原語 — Roots**：新增完整文檔說明 Roots 客戶端原語，協助伺服器理解檔案系統邊界及存取權限
- <strong>工具註解</strong>：新增工具行為註解（`readOnlyHint`、`destructiveHint`）文件，以改善工具執行決策
- <strong>取樣中的工具呼叫</strong>：更新取樣文檔，納入 `tools` 與 `toolChoice` 參數，用於取樣請求期間模型驅動的工具調用
- **URL 模式引導**：新增文檔說明基於 URL 的引導，用於伺服器啟動的外部網路互動
- **任務（實驗功能）**：新增章節說明任務功能，提供持久執行包裝器及延遲結果檢索
- <strong>圖示支援</strong>：標示工具、資源、資源範本與提示可包含圖示作為額外元資料

#### 文件更新
- **README.md**：新增 MCP 規範 2025-11-25 版本參考及基於日期的版本控制說明
- **study_guide.md**：更新課程地圖以包含任務與工具註解於核心概念區；更新文件時間戳記

#### 規範相容性驗證
- <strong>協議版本</strong>：確認所有文件均指向最新 MCP 規範 2025-11-25
- <strong>架構對齊</strong>：確認文件準確描述兩層架構（資料層 + 傳輸層）
- <strong>原語文件</strong>：驗證伺服器端原語（資源、提示、工具）與客戶端原語（取樣、引導、日誌、Roots）
- <strong>傳輸機制</strong>：確認 STDIO 與可串流 HTTP 傳輸文件正確
- <strong>安全指引</strong>：確認與現行 MCP 安全最佳實踐文件相符

#### 主要 MCP 2025-11-25 功能文件
- **OpenID Connect 探索**：OIDC 協議的驗證伺服器發現
- **OAuth 用戶端 ID 元資料文件**：推薦的用戶端註冊機制
- **JSON Schema 2020-12**：MCP 架構定義的預設方言
- **SDK 層級制度**：正式化 SDK 功能支援與維護要求
- <strong>治理結構</strong>：正式化 MCP 中的工作小組與利益小組治理

### 安全文件重大更新（02-Security/）

#### MCP 安全高峰會研討會（Sherpa）整合
- <strong>新增實務訓練資源</strong>：於所有安全文件中新增與 [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) 的全面整合
- <strong>探險路線覆蓋</strong>：文件中完整描述從基營到高峰的營地階段進展
- **OWASP 對齊**：所有安全指引映射至 OWASP MCP Azure Security Guide 風險項目

#### OWASP MCP 十大風險整合
- <strong>新增章節</strong>：在主要安全 README 中新增 OWASP MCP 十大安全風險表及 Azure 緩解措施
- <strong>基於風險的文件</strong>：更新 mcp-security-controls-2025.md，加入 OWASP MCP 風險標示（MCP01-MCP08）與各安全領域對應
- <strong>參考架構</strong>：鏈結至 OWASP MCP Azure Security Guide 參考架構及實作範例

#### 更新的安全文件
- **README.md**：新增 Sherpa 研討會概述、探險路線表、OWASP MCP 十大風險摘要及實務訓練章節
- **mcp-security-controls-2025.md**：更新標題至 2026 年 2 月，新增 OWASP 風險參考（MCP01-MCP08），修正規範版本不一致問題
- **mcp-security-best-practices-2025.md**：新增 Sherpa 及 OWASP 資源章節，更新時間戳記
- **mcp-best-practices.md**：新增實務訓練章節並附加 Sherpa 及 OWASP 連結
- **azure-content-safety-implementation.md**：新增 OWASP MCP06 參考，與 Sherpa 第 3 營對齊，並新增額外資源章節

#### 新增資源連結
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure 安全指南](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP 前10大風險](https://owasp.org/www-project-mcp-top-10/)
- 個別 OWASP MCP 風險頁面 (MCP01-MCP10)

### 課程全局 MCP 規範 2025-11-25 對齊

#### 模組 03 - 入門
- **SDK 文件**：新增 Go SDK 至官方 SDK 列表；更新所有 SDK 參考以符合 MCP 規範 2025-11-25
- <strong>傳輸說明澄清</strong>：更新 STDIO 和 HTTP Streaming 傳輸描述，並加入明確規範參考

#### 模組 04 - 實作
- **SDK 更新**：新增 Go SDK；更新 SDK 清單並標示規範版本
- <strong>授權規範</strong>：更新 MCP 授權規範鏈接至目前 2025-11-25 版本

#### 模組 05 - 進階主題
- <strong>新功能</strong>：新增關於 MCP 規範 2025-11-25 新增功能（任務、工具註解、URL 模式引導、Roots）的說明
- <strong>安全資源</strong>：新增 OWASP MCP 前 10 風險與 Sherpa 工作坊連結於補充參考

#### 模組 06 - 社群貢獻
- **SDK 列表**：加入 Swift 和 Rust SDK；更新規範鏈接為 2025-11-25 版本
- <strong>規範參考</strong>：更新 MCP 規範連結至直接規範網址

#### 模組 07 - 早期採用經驗
- <strong>資源更新</strong>：新增 MCP 規範 2025-11-25 連結及 OWASP MCP 前 10 於補充資源

#### 模組 08 - 最佳實踐
- <strong>規範版本</strong>：更新 MCP 規範參考至 2025-11-25
- <strong>安全資源</strong>：新增 OWASP MCP 前 10 及 Sherpa 工作坊於補充參考

#### 模組 10 - 精簡 AI 工作流程
- <strong>徽章更新</strong>：MCP 版本徽章從 SDK 版本（1.9.3）改為規範版本（2025-11-25）
- <strong>資源連結</strong>：更新 MCP 規範連結；新增 OWASP MCP 前 10

#### 模組 11 - MCP 伺服器實驗室
- <strong>規範參考</strong>：更新 MCP 規範鏈接至 2025-11-25 版本
- <strong>安全資源</strong>：新增 OWASP MCP 前 10 至官方資源

## 2025 年 12 月 18 日

### 安全文件更新 - MCP 規範 2025-11-25

#### MCP 安全最佳實踐 (02-Security/mcp-best-practices.md) - 規範版本更新
- <strong>協議版本更新</strong>：更新為引用最新 MCP 規範 2025-11-25（於 2025 年 11 月 25 日發布）
  - 所有規範版本參考從 2025-06-18 更新為 2025-11-25
  - 文件日期參考從 2025 年 8 月 18 日更新至 2025 年 12 月 18 日
  - 驗證所有規範 URL 指向最新文件
- <strong>內容驗證</strong>：全面驗證安全最佳實踐與最新標準一致性
  - **Microsoft 安全解決方案**：確認 Prompt Shields（原稱「越獄風險偵測」）、Azure Content Safety、Microsoft Entra ID 與 Azure Key Vault 的最新術語與連結
  - **OAuth 2.1 安全**：確認符合最新 OAuth 安全最佳實踐
  - **OWASP 標準**：驗證 OWASP LLMs 前 10 參考仍為最新
  - **Azure 服務**：確認所有 Microsoft Azure 文件連結與最佳實踐
- <strong>標準對齊</strong>：所有引用的安全標準皆為最新
  - NIST AI 風險管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳實踐
  - Azure 安全與合規框架
- <strong>實作資源</strong>：驗證所有實作指南連結與資源
  - Azure API 管理認證範例
  - Microsoft Entra ID 整合指南
  - Azure Key Vault 秘密管理
  - DevSecOps 管線與監控解決方案

### 文件品質保證
- <strong>規範符合性</strong>：確保所有強制 MCP 安全需求（MUST/MUST NOT）符合最新規範
- <strong>資源更新性</strong>：驗證所有外部連結至 Microsoft 文件、安全標準與實作指南
- <strong>最佳實踐涵蓋</strong>：確認完整涵蓋認證、授權、AI 專屬威脅、供應鏈安全與企業範例

## 2025 年 10 月 6 日

### 入門章節擴展 – 進階伺服器使用與簡易認證

#### 進階伺服器使用 (03-GettingStarted/10-advanced)
- <strong>新增章節</strong>：介紹全面的進階 MCP 伺服器使用指南，涵蓋常規與低階伺服器架構。
  - **常規 vs. 低階伺服器**：詳細比較並提供 Python 及 TypeScript 兩種方法範例。
  - <strong>基於處理器設計</strong>：說明基於處理器的工具/資源/提示管理，提升伺服器實現的可擴展性與彈性。
  - <strong>實務範型</strong>：實務場景說明，低階伺服器範型對進階功能及架構的助益。

#### 簡易認證 (03-GettingStarted/11-simple-auth)
- <strong>新增章節</strong>：逐步指引 MCP 伺服器實作簡易認證。
  - <strong>認證觀念</strong>：清楚解說認證與授權的差異，以及認證憑證處理。
  - <strong>基礎認證實作</strong>：Python (Starlette) 與 TypeScript (Express) 中基於中介軟體的認證範型與代碼範例。
  - <strong>邁向進階安全</strong>：指導從簡易認證過渡至 OAuth 2.1 和 RBAC，並參考進階安全模組。

這些新增內容為建立更健全、安全、彈性 MCP 伺服器實作提供實務且操作性指引，連結基礎概念與進階生產範型。

## 2025 年 9 月 29 日

### MCP 伺服器資料庫整合實驗室 - 全面動手學習路徑

#### 11-MCPServerHandsOnLabs - 新增完整資料庫整合課程
- **完整 13 個實驗路徑**：新增結合 PostgreSQL 資料庫整合的生產級 MCP 伺服器構建實務課程
  - <strong>真實案例實作</strong>：Zava Retail 分析用例展示企業級範型
  - <strong>結構化學習進程</strong>：
    - **實驗 00-03：基礎** - 介紹、核心架構、安全與多租戶、環境配置
    - **實驗 04-06：構建 MCP 伺服器** - 資料庫設計與模式、MCP 伺服器實作、工具開發  
    - **實驗 07-09：進階功能** - 語意搜尋整合、測試與除錯、VS Code 整合
    - **實驗 10-12：生產與最佳實踐** - 部署策略、監控與觀察、最佳實踐與優化
  - <strong>企業技術</strong>：FastMCP 框架、PostgreSQL 結合 pgvector、Azure OpenAI 嵌入、Azure 容器應用、Application Insights
  - <strong>進階功能</strong>：行級安全性 (RLS)、語意搜尋、多租戶資料存取、向量嵌入、實時監控

#### 術語標準化 - 模組改為實驗室
- <strong>全面文件更新</strong>：系統性更新 11-MCPServerHandsOnLabs 目錄下所有 README 檔案，將術語由「模組」改為「實驗室」
  - <strong>章節標題</strong>：所有 13 個實驗室的「本模組涵蓋內容」更新為「本實驗室涵蓋內容」
  - <strong>內容描述</strong>：將「此模組提供…」改為「此實驗室提供…」
  - <strong>學習目標</strong>：更新「本模組結束時…」至「本實驗室結束時…」
  - <strong>導航連結</strong>：所有交叉參考與導覽中的「模組 XX」改為「實驗室 XX」
  - <strong>完成追蹤</strong>：將「完成此模組後…」更換為「完成此實驗室後…」
  - <strong>保留技術參考</strong>：維持設定檔中的 Python 模組參考（例如 `"module": "mcp_server.main"`）

#### 學習指南強化 (study_guide.md)
- <strong>視覺課程地圖</strong>：新增「11. 資料庫整合實驗室」章節，完整視覺化實驗室結構
- <strong>儲存庫結構</strong>：從十個主章節更新至十一個，並詳述 11-MCPServerHandsOnLabs
- <strong>學習路徑指引</strong>：加強覆蓋 00-11 章節的導覽說明
- <strong>技術涵蓋</strong>：新增 FastMCP、PostgreSQL、Azure服務整合細節
- <strong>學習成果</strong>：強調生產就緒伺服器開發、資料庫整合範型與企業安全

#### 主 README 結構強化
- <strong>以實驗室術語</strong>：更新 11-MCPServerHandsOnLabs 主 README.md，統一使用「實驗室」結構
- <strong>學習路徑組織</strong>：清楚區分從基礎概念、進階實作至生產部署的進程
- <strong>實務導向</strong>：強調以企業級範型與技術為核心的動手學習

### 文件品質與一致性改進
- <strong>動手學習強調</strong>：在整份文件重申實驗室導向的實務學習模式
- <strong>企業範型聚焦</strong>：強調生產就緒實作與企業安全考量
- <strong>技術整合</strong>：全面涵蓋現代 Azure 服務和 AI 整合範型
- <strong>學習進程</strong>：從基礎到生產部署的清晰結構路徑

## 2025 年 9 月 26 日

### 個案研究強化 - GitHub MCP Registry 整合

#### 個案研究 (09-CaseStudy/) - 生態系發展焦點
- **README.md**：大幅擴充，包含完整 GitHub MCP Registry 個案研究
  - **GitHub MCP Registry 個案研究**：全方位檢視 GitHub 於 2025 年 9 月推出的 MCP Registry
    - <strong>問題分析</strong>：詳細檢視分散式 MCP 伺服器發現與部署難題
    - <strong>解決方案架構</strong>：GitHub 的集中式登錄方式及一鍵安裝 VS Code 功能
    - <strong>業務影響</strong>：顯著提升開發者入門與生產力
    - <strong>策略價值</strong>：聚焦模組化代理部署與跨工具互操作性
    - <strong>生態系發展</strong>：定位為代理系統整合的基礎平台
  - <strong>個案研究結構優化</strong>：更新七項個案研究，使格式與描述一致且完整
    - Azure AI 旅行代理：多代理協調重點
    - Azure DevOps 整合：流程自動化焦點
    - 即時文件檢索：Python 控制台用戶端實作
    - 互動式學習計劃生成器：Chainlit 對話式網頁應用
    - 編輯器內文件：VS Code 與 GitHub Copilot 整合
    - Azure API 管理：企業 API 整合範型
    - GitHub MCP Registry：生態系發展與社群平台
  - <strong>綜合結論</strong>：重寫結論，突顯七項個案研究涵蓋多面向 MCP 實作
    - 企業整合、多代理協調、開發者生產力
    - 生態系發展、教育應用分類
    - 強化對架構模式、實作策略及最佳實踐的見解
    - 強調 MCP 為成熟且生產就緒的協定

#### 學習指南更新 (study_guide.md)
- <strong>視覺課程地圖</strong>：更新心智圖，新增 GitHub MCP Registry 至個案研究章節
- <strong>個案研究描述</strong>：由泛泛描述擴充為七個全面個案研究的詳細解析
- <strong>儲存庫結構</strong>：更新第 10 章節反映全面個案研究涵蓋與具體實作細節
- <strong>更新記錄整合</strong>：新增 2025 年 9 月 26 日條目，記錄 GitHub MCP Registry 加入與個案研究強化
- <strong>日期更新</strong>：更新頁腳時間戳為最新改版時間（2025 年 9 月 26 日）

### 文件品質改進
- <strong>一致性強化</strong>：標準化七個個案研究的格式與結構
- <strong>全面涵蓋</strong>：個案研究涵蓋企業、開發者生產力與生態系發展場景
- <strong>策略定位</strong>：強化 MCP 作為代理系統部署基礎平台的焦點
- <strong>資源整合</strong>：更新補充資源，新增 GitHub MCP Registry 連結

## 2025 年 9 月 15 日

### 進階主題擴展 - 自訂傳輸與上下文工程

#### MCP 自訂傳輸 (05-AdvancedTopics/mcp-transport/) - 進階實作指南
- **README.md**：完整 MCP 自訂傳輸機制實作指南
  - **Azure 事件網格傳輸**：全面的無伺服器事件驅動傳輸實作
    - C#、TypeScript 及 Python 範例結合 Azure Functions 整合
    - 可擴展 MCP 解決方案的事件驅動架構範型
    - Webhook 接收器與推送訊息處理
  - **Azure Event Hubs 傳輸**：高吞吐量串流傳輸實作
    - 低延遲場景的即時串流能力
    - 分區策略與檢查點管理
    - 訊息批次與效能優化
  - <strong>企業整合範型</strong>：生產就緒的架構範例
    - 分散式 MCP 處理跨多個 Azure Functions
    - 混合傳輸架構結合多種傳輸類型
    - 訊息持久性、可靠性與錯誤處理策略
  - <strong>安全與監控</strong>：Azure Key Vault 整合與觀察模式
    - 管理身份驗證與最低權限存取
    - Application Insights 遙測與效能監控
    - 斷路器與容錯模式
  - <strong>測試框架</strong>：自訂傳輸的全面測試策略
    - 使用測試替身與模擬框架的單元測試
    - 結合 Azure 測試容器的整合測試
    - 效能與負載測試考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新興 AI 領域
- **README.md**：全面探討上下文工程作為新興領域
  - <strong>核心原理</strong>：完整上下文共用、行動決策意識、上下文視窗管理

  - **MCP 協議對齊**：MCP 設計如何解決上下文工程挑戰
    - 上下文視窗限制與漸進式載入策略
    - 相關性判斷與動態上下文檢索
    - 多模態上下文處理與安全性考量
  - <strong>實作方法</strong>：單線程與多代理架構
    - 上下文分片與優先排序技術
    - 漸進式上下文載入與壓縮策略
    - 分層上下文方法與檢索優化
  - <strong>衡量框架</strong>：新興指標評估上下文效能
    - 輸入效率、效能、品質與用戶體驗考量
    - 上下文優化的實驗方法
    - 故障分析與改進方法論

#### 課程導航更新 (README.md)
- <strong>增強模組結構</strong>：更新課程表以包含新進階主題
  - 新增上下文工程 (5.14) 與自訂傳輸 (5.15)
  - 全模組一致的格式與導航連結
  - 更新描述以反映現有內容範圍

### 目錄結構改進
- <strong>命名標準化</strong>：將 "mcp transport" 重命名為 "mcp-transport" 以符合其他進階主題資料夾命名規則
- <strong>內容組織</strong>：所有 05-AdvancedTopics 資料夾遵循一致命名模式 (mcp-[topic])

### 文件品質提升
- **MCP 規範對齊**：所有新內容參考現行 MCP 規範 2025-06-18
- <strong>多語言範例</strong>：全面性 C#、TypeScript 與 Python 程式碼範例
- <strong>企業聚焦</strong>：生產就緒範例與 Azure 雲端整合遍佈其中
- <strong>視覺化文件</strong>：架構與流程的 Mermaid 圖示

## 2025年8月18日

### 文件全面更新 - MCP 2025-06-18 標準

#### MCP 安全最佳實踐 (02-Security/) - 全面現代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：全面重寫，與 MCP 規範 2025-06-18 對齊
  - <strong>強制性要求</strong>：依官方規範新增明確的 MUST/MUST NOT 要求，並設有清晰視覺指示
  - **12 項核心安全實踐**：從 15 項清單重構為完整安全領域
    - 令牌安全與外部身分提供者整合認證
    - 會話管理與傳輸安全含密碼學要求
    - AI 專屬威脅防護，結合 Microsoft Prompt Shields
    - 存取控制與權限，最小權限原則
    - 內容安全與監控，Azure 內容安全整合
    - 供應鏈安全，全面元件驗證
    - OAuth 安全及「混淆代理」防範，PKCE 實作
    - 事件回應與復原，自動化能力
    - 合規與治理，符合法規要求
    - 進階安全控管，零信任架構
    - Microsoft 安全生態系整合，全面解決方案
    - 持續安全演進，自適應實務
  - <strong>微軟安全解決方案</strong>：強化 Prompt Shields、Azure 內容安全、Entra ID 與 GitHub 高級安全整合指導
  - <strong>實作資源</strong>：依官方 MCP 文件、微軟安全解決方案、安全標準與實作指南分類全面資源連結

#### 進階安全控管 (02-Security/) - 企業實作
- **MCP-SECURITY-CONTROLS-2025.md**：全面改寫，企業級安全框架
  - **9 項全面安全領域**：由基礎控管擴展為詳細企業框架
    - 進階認證與授權，整合 Microsoft Entra ID
    - 令牌安全與反繞過控管，全面驗證
    - 會話安全控管，防止劫持
    - AI 專屬安全控管，防止提示注入與工具中毒
    - 混淆代理攻擊防範，OAuth 代理安全
    - 工具執行安全，沙盒與隔離機制
    - 供應鏈安全控管，依賴驗證
    - 監控與偵測控管，整合 SIEM
    - 事件回應與復原，自動化能力
  - <strong>實作範例</strong>：新增詳細 YAML 配置區塊與程式碼範例
  - <strong>微軟解決方案整合</strong>：全面涵蓋 Azure 安全服務、GitHub 高級安全與企業身份管理

#### 進階主題安全 (05-AdvancedTopics/mcp-security/) - 生產就緒實作
- **README.md**：全面重寫，企業安全實作
  - <strong>規範最新對齊</strong>：更新至 MCP 規範 2025-06-18，包含強制安全要求
  - <strong>增強認證</strong>：Microsoft Entra ID 整合，附全面 .NET 與 Java Spring Security 範例
  - **AI 安全整合**：實作 Microsoft Prompt Shields 與 Azure 內容安全，包含詳細 Python 範例
  - <strong>進階威脅緩解</strong>：全面實作範例涵蓋
    - 混淆代理攻擊防範，PKCE 與用戶同意驗證
    - 令牌繞過防範，受眾驗證與安全令牌管理
    - 會話劫持防範，密碼學綁定與行為分析
  - <strong>企業安全整合</strong>：Azure Application Insights 監控、威脅偵測管線與供應鏈安全
  - <strong>實作檢核清單</strong>：清楚標示強制與建議安全控管，附微軟安全生態系利益

### 文件品質與標準對齊
- <strong>規範參考</strong>：更新所有參考至現行 MCP 規範 2025-06-18
- <strong>微軟安全生態系</strong>：增強所有安全文件中的整合指導
- <strong>實務實作</strong>：新增 .NET、Java 與 Python 詳細程式碼範例及企業模式
- <strong>資源組織</strong>：官方文件、安全標準與實作指南的全面分類
- <strong>視覺指示</strong>：清楚標示強制要求與建議實務


#### 核心概念 (01-CoreConcepts/) - 完全現代化
- <strong>協議版本更新</strong>：更新參考至現行 MCP 規範 2025-06-18，採日期版本編號 (YYYY-MM-DD 格式)
- <strong>架構精煉</strong>：加強 Hosts、Clients 與 Servers 描述，反映現行 MCP 架構模式
  - Hosts 現已明確定義為協調多 MCP 客戶端連線的 AI 應用
  - Clients 描述為保持一對一伺服器關係的協議連接器
  - Servers 增強區分本地與遠端部署情境
- <strong>原始元件重組</strong>：全面改寫伺服器與客戶端原始元件
  - 伺服器原始元件：資源（資料來源）、提示（模板）、工具（可執行功能）並附詳細說明與範例
  - 客戶端原始元件：取樣（LLM 補全）、引導（用戶輸入）、記錄（日誌/監控）
  - 更新現行探索 (`*/list`)、檢索 (`*/get`) 與執行 (`*/call`) 方法模式
- <strong>協議架構</strong>：引入二層架構模型
  - 資料層：基於 JSON-RPC 2.0，包含生命週期管理與原始元件
  - 傳輸層：STDIO（本地）及可串流 HTTP 搭配 SSE（遠端）傳輸機制
- <strong>安全框架</strong>：全面安全原則，含明確用戶同意、資料隱私保護、工具執行安全與傳輸層安全
- <strong>通訊模式</strong>：更新協議訊息，顯示初始化、探索、執行與通知流程
- <strong>程式碼範例</strong>：刷新多語言範例 (.NET、Java、Python、JavaScript) 以反映現行 MCP SDK 模式

#### 安全 (02-Security/) - 全面安全改版  
- <strong>標準對齊</strong>：完全符合 MCP 規範 2025-06-18 的安全要求
- <strong>認證演進</strong>：紀錄從自訂 OAuth 伺服器到外部身分提供者委派（Microsoft Entra ID）的變革
- **AI 專屬威脅分析**：增強現代 AI 攻擊向量覆蓋
  - 詳細提示注入攻擊場景與實例
  - 工具中毒機制與「拉地毯」攻擊模式
  - 上下文視窗中毒與模型混淆攻擊
- **微軟 AI 安全解決方案**：全面涵蓋微軟安全生態系
  - AI Prompt Shields 具先進偵測、聚光燈標示與分隔符技巧
  - Azure 內容安全整合模式
  - GitHub 高級安全供應鏈保護
- <strong>進階威脅緩解</strong>：詳細安全控管涵蓋
  - 會話劫持，含 MCP 專屬攻擊場景與密碼學會話 ID 要求
  - MCP 代理場景混淆代理問題與明確同意要求
  - 令牌繞道漏洞，強制驗證控管
- <strong>供應鏈安全</strong>：擴充 AI 供應鏈涵蓋，包括基礎模型、嵌入服務、上下文提供者及第三方 API
- <strong>基礎安全</strong>：增強企業安全模式整合，包括零信任架構與微軟安全生態系
- <strong>資源組織</strong>：依類別（官方文件、標準、研究、微軟解決方案、實作指南）分類全面資源連結

### 文件品質改進
- <strong>結構化學習目標</strong>：增強具體且可執行的學習成果
- <strong>交叉參考</strong>：新增相關安全與核心概念主題間連結
- <strong>最新資訊</strong>：更新所有日期參考與規範連結到現行標準
- <strong>實作指導</strong>：於兩大部分加入具體且可執行的實作指導方針

## 2025年7月16日

### README 與導航改進
- 完全重新設計 README.md 中課程導航
- 以更易存取的表格格式取代 `<details>` 標籤
- 在新 "alternative_layouts" 資料夾建立替代版型選項
- 新增卡片式、分頁式與手風琴式導航示例
- 更新儲存庫結構章節以涵蓋最新檔案
- 強化「如何使用此課程」章節，提供明確建議
- 更新 MCP 規範連結指向正確 URL
- 新增上下文工程部分 (5.14) 到課程結構

### 學習指南更新
- 完全修訂學習指南以符合現有儲存庫結構
- 新增 MCP 客戶端與工具、熱門 MCP 伺服器新章節
- 更新視覺課程地圖，精確反映所有主題
- 增強進階主題說明，涵蓋所有專業領域
- 更新案例研究章節，反映真實示例
- 新增此綜合變更日志

### 社群貢獻 (06-CommunityContributions/)
- 新增 MCP 影像生成伺服器詳細資訊
- 新增於 VSCode 中使用 Claude 的全面章節
- 新增 Cline 終端客戶端設定與使用說明
- 更新 MCP 客戶端章節，包含所有熱門客戶端選項
- 強化貢獻範例，提供更精確的程式碼範例

### 進階主題 (05-AdvancedTopics/)
- 有系統地組織所有專業主題資料夾，以一致命名
- 新增上下文工程教材與範例
- 新增 Foundry 代理整合文件
- 強化 Entra ID 安全整合文件

## 2025年6月11日

### 初版建立
- 發布 MCP 初學者課程首版
- 建立所有 10 個主要章節基礎結構
- 實作視覺課程地圖以利導航
- 新增多種程式語言的初始示例專案

### 入門 (03-GettingStarted/)
- 建立首批伺服器實作範例
- 新增客戶端開發指導
- 收錄 LLM 客戶端整合指引
- 新增 VS Code 整合文件
- 實作伺服器事件推送 (SSE) 範例

### 核心概念 (01-CoreConcepts/)
- 新增詳細的客戶端-伺服器架構說明
- 建立主要協議組件文件
- 記錄 MCP 中的訊息模式

## 2025年5月23日

### 儲存庫結構
- 初始化儲存庫，建立基礎資料夾結構
- 建立各主要章節的 README 文件
- 設置翻譯基礎結構
- 新增圖片資產與圖表

### 文件
- 建立初始 README.md，包含課程概覽
- 新增 CODE_OF_CONDUCT.md 與 SECURITY.md
- 設立 SUPPORT.md，提供求助指引
- 建立初期學習指南架構

## 2025年4月15日

### 規劃與框架
- MCP 初學者課程的初期規劃
- 制定學習目標與目標受眾
- 概述課程 10 章節結構
- 開發範例與案例研究的概念框架
- 創建關鍵概念的初期原型範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
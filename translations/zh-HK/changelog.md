# 變更紀錄：初學者 MCP 課程

本文件用作記錄對 Model Context Protocol (MCP) 初學者課程所做的所有重大變更。變更依時間逆序記錄（最新變更優先）。

## 2026 年 7 月 29 日

### 新模塊 08 伴隨課程：可靠性側車與安全重試

新增與 MCP 工具相關的中立廠商伴隨課程，涵蓋產生實際效果的工具，
與最終的 `2026-07-28` 規範對齊。

- <strong>新增</strong>：[可靠性側車伴隨課程][reliability-sidecar]
  使用一個支援票證故事、兩個 Mermaid 圖表和一個重試決策
  流程來說明穩定操作鍵、原子重複接收、
  調和、證據，以及 Tasks 擴展邊界。
- <strong>新增</strong>：使用標準庫 Python 和 SQLite 失敗注入練習，
  採用獨立的操作和票證存儲演示外部效果提交後響應丟失的情況。
  六個確定性測試涵蓋天真重複、保護重啟恢復、有效載荷衝突、
  緩存結果、活動主張和並發重複接收。
- <strong>更新</strong>：模塊 08 現在鏈接伴隨課程，明確最終的 `2026-07-28` 無狀態請求模型，
  區分 OpenTelemetry 可觀察性功能與已棄用的 MCP 日誌功能，
  並將其通用重試範例限制於只讀操作。
- <strong>可選</strong>：課程將其可攜概念映射到一個帶標籤的社群實現，
  但不將託管服務或網絡調用納入練習。

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md








  新的 `Mcp-Method`/`Mcp-Name` 路由標頭，`ttlMs`/`cacheScope` 快取元資料，

  六個授權加強 SEP，棄用 Roots/Sampling/Logging，並移至完整的 JSON Schema 2020-12 用於工具架構。
- <strong>更新</strong> 加入前瞻性提示並鏈結新課程：
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md)：協定版本說明，Sampling/Roots/Logging/Tasks 部分，以及「後續展望」
  - [02-Security/README.md](./02-Security/README.md)：授權加強提示
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md)：無狀態傳輸提示
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md)：Sampling 棄用提示
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md)：Logging 棄用及 Tasks 擴展提示
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md)：無狀態/會話路由提示
  - [README.md](./README.md)：規範部分的「前瞻」說明並新增課程模塊表中的 `1.1` 條目
  - [study_guide.md](./study_guide.md)：核心概念總覽下的前瞻子彈點和帶日期附錄說明
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md)：在無狀態請求模型前的 `mcp-session-id` 傳輸映射提示
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md)：模塊概覽中有 Root Contexts/Sampling 棄用與 Tasks 擴展
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md)：授權加強提示

## 2026 年 6 月 24 日

### 新課程：在 Copilot 應用中使用 MCP

- 新增 [工具部分](./12-tooling/README.md)。
- [Copilot 應用中的 MCP](./12-tooling/01-copilot-app/README.md)

## 2026 年 6 月 16 日

### MCP 規範對齊與範例驗證

已驗證課程內容符合現行 **MCP 規範 2025-11-25** 和最新官方 SDK，修正所有陳舊的規範引用，確認核心範例仍能成功構建與執行。

#### 規範版本修正（2025-06-18 / 2025-03-26 → 2025-11-25）

更新了仍聲稱舊版規範為<em>現行/最新</em>標準的英文內容，並重新指向正規的 `modelcontextprotocol.io` 規範路徑：
- **05-AdvancedTopics/mcp-security/README.md**：更新「現行標準」橫幅、介紹、核心安全原則標題、強制要求標題、Microsoft Entra ID 部分、參考與資源連結，以及結尾安全通知（8 個參考資料）至 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**：更新附加資源規範連結和「現行標準」橫幅至 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**：將過時的 `2025-03-26` 安全與信任連結替換為最新的 2025-11-25 安全最佳實踐頁面
- **03-GettingStarted/14-sampling/README.md**：更新官方 Sampling 文件連結為 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: 更新現在式「目前 MCP 規範」參考及附加資源規範連結至 2025-11-25（歷史 SSE 棄用註解保持原樣以維持準確性）

#### 與目前 SDK 驗證範例

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: 使用 `npm install` 解決 `@modelcontextprotocol/sdk@1.29.0`；`tsc --noEmit` 無類型錯誤通過 — 現有的 `McpServer`/`StdioServerTransport` API 仍然有效
- **Python (03-GettingStarted/01-first-server/solution/python)**: 在隔離的 `.venv` 裡用 `mcp[cli]` (1.27.2) 驗證；`py_compile` 通過且 `FastMCP.list_tools()` 正確返回了 `add` 和 `subtract` 工具
- 確認所有範例的 `@modelcontextprotocol/sdk` 版本範圍 (`>=1.26.0` / `^1.26.0` / `^1.27.0`) 全都乾淨解析至目前的 `1.29.0`，無破壞性 API 變更

#### 依賴版本對齊（彌合版本差距）

將過時的 SDK 版本上調，使每個範例都追蹤目前 MCP 版本，符合整個倉庫的慣例：
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: 將 `@modelcontextprotocol/sdk` 從 `^1.8.0` 升級至 `>=1.26.0`，並將過時的「更新以符合 MCP 2025-06-18」套件描述改為「與 MCP 規範 2025-11-25 對齊」
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** 與 **lab4/code/github_mcp_server/pyproject.toml**: 將精確釘版本 `mcp==1.23.0` 調整為 `mcp>=1.26.0`；重新生成兩個 `uv.lock` 檔（使用 `uv lock`），確保鎖檔解析到當前 `mcp 1.27.2`，並與配置文件保持同步

#### 課程差距分析 — 最新規範功能涵蓋

已驗證課程已涵蓋 MCP 2025-11-25 中引入與擴充的所有基礎功能，無遺缺內容：
- <strong>抽樣</strong>: 課程 03-GettingStarted/14-sampling 及 05-AdvancedTopics/mcp-sampling
- **引導（包含 URL 模式）**: 記載於 01-CoreConcepts 與 05-AdvancedTopics/mcp-protocol-features
- **根 Contexts**: 記載於 00-Introduction、01-CoreConcepts 以及 05-AdvancedTopics/mcp-root-contexts
- **任務（實驗性，長時間操作）**: 記載於 01-CoreConcepts 與 05-AdvancedTopics/mcp-protocol-features
- <strong>工具註釋</strong>（`readOnlyHint` / `destructiveHint`）: 記載於 01-CoreConcepts 與 05-AdvancedTopics/mcp-protocol-features

### 安全強化及依賴漏洞修復

執行了全方位的安全檢查，涵蓋所有依賴清單和範例原始碼，並修復了所有報告的 npm 警示和一個程式碼層級問題。修復後，`npm audit` 報告所有審核目錄皆為 **0 漏洞**。

#### npm 依賴漏洞（傳遞性）— 已修復

審核所有 15 個提交的 `package-lock.json` 文件。漏洞限於 MCP Inspector 開發工具、OpenAI 客戶端和 MCP SDK 所拉取的傳遞性依賴；均已修復且不破壞範例：
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** 和 **lab3/code/weather_mcp/inspector**: 將 `@modelcontextprotocol/inspector` （`0.16.6` / `0.14.1` → `0.22.0`）升級，清除了捆綁的 `ajv`、`brace-expansion`、`diff`、`path-to-regexp` 和 `ws` 警示。增加 npm `overrides` 條目，強制使用修補版 `shell-quote@1.8.4`，消除 `concurrently` 的高危警示；重新生成兩個鎖檔（現在無漏洞）
- **03-GettingStarted/samples/typescript**: 使用 `npm audit fix` 更新傳遞性 `qs`（中度）至修補版本
- **03-GettingStarted/samples/javascript**: 使用 `npm audit fix` 更新傳遞性 `hono`（中度）至修補版本
- **03-GettingStarted/03-llm-client/solution/typescript**: 使用 `npm audit fix` 更新傳遞性 `form-data`（高危）至修補版本
- **03-GettingStarted/11-simple-auth/solution/typescript**: 生成缺失的 `package-lock.json`，使專案可重複和可審核（無漏洞）

#### 程式碼層級安全修正（OWASP A03: 注入攻擊）

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: 從 `open_in_vscode` 工具移除 `shell=True`。先前的 `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` 會讓資料夾路徑中 shell 元字元被 `cmd.exe` 解析（命令注入途徑）。現在直接啟動解析後的 `Code.exe` 並以資料夾作為引數 — 不經由 shell — 功能相同且安全

#### Python 依賴檢查

- 使用 `pip-audit` 審核所有 Python 需求集。`05-AdvancedTopics` 與 `03-GettingStarted/samples/python` 報告 <strong>無已知漏洞</strong>（其 `mcp` / `httpx` / `pydantic` / `python-dotenv` 範圍皆解析至當前修補版本）
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` 標示傳遞依賴 **`werkzeug` 3.1.1** 有三個 `safe_join` Windows 裝置名稱拒絕服務漏洞 — `CVE-2025-66221`、`CVE-2026-21860` 和 `CVE-2026-27199`（皆已於 3.1.6 修復）。加上明確安全釘版本 `werkzeug>=3.1.6`，確保解析到修補版本；並驗證該約束與 `chainlit` / `mcp` / `semantic-kernel` 堆疊兼容並正常解析

### 產品名稱重新命名

更新所有課程內容以反映微軟的產品重新命名：


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**：更新 Discord 社群連結

- **AGENTS.md**：更新 Discord 伺服器參考
- **README.md**：更新技術生態系統參考
- **study_guide.md**：更新案例研究參考
- **05-AdvancedTopics/README.md**：更新第 5.13 章標題和描述
- **05-AdvancedTopics/mcp-integration/README.md**：更新章節標題和描述
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**：完整模組標題和內容更新
- **05-AdvancedTopics/mcp-security-entra/README.md**：更新交叉引用連結
- **07-LessonsfromEarlyAdoption/README.md**：更新案例研究參考
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**：更新第 9 章標題、徽章和功能
- **08-BestPractices/README.md**：更新 Discord 社群連結
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**：更新 Discord 頻道參考
- **09-CaseStudy/docs-mcp/solution/python/README.md**：更新模型部署參考
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**：更新 AI 服務表
- **11-MCPServerHandsOnLabs/03-Setup/README.md**：更新資源參考

#### AI 工具包 / AITK → Microsoft Foundry Toolkit 擴展於 VS Code
- **README.md**：更新主要課程參考
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**：更新模組標題、概覽及所有模組標題
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**：更新標題、學習目標、安裝指示和資源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**：更新標題、學習目標、MCP 主機表及交叉參考
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**：更新標題、徽章、先決條件和資源
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**：更新代理生成器參考與反饋連結
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**：更新先決條件和擴展參考

---

## 2026年4月11日

### 新課程、文件修正及依賴更新

#### 新增課程內容

**模組 05 - 進階主題**
- **課程 5.17：使用 MCP 的對抗多代理推理** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`)：對多代理系統中對抗辯論模式的全方位指引
  - Mermaid 架構圖：兩個代理 → 共享 MCP 伺服器 → 辯論記錄 → 評審 → 裁決
  - 使用 Python 與 TypeScript 實作的共享 MCP 工具伺服器 (`web_search` + `run_python`)
  - 對立系統提示（支持 / 反對 / 評審）具明確工具使用要求
  - Python、TypeScript 及 C# 實作的辯論指揮者，管理回合並路由論點
  - MCP `ClientSession` 連接指揮者與實際工具呼叫
  - 使用案例表（幻覺偵測、威脅建模、API 設計審查、事實驗證、技術選擇）
  - 安全考量：沙盒執行、工具呼叫驗證、速率限制、稽核日誌
  - 三個實務場景的結構化練習（程式碼審查、架構決策、內容審核）

#### 文件修正

**模組 03 - 入門**
- **05-stdio-server/README.md**：修正未完成的 TypeScript stdio 伺服器示例 — 新增缺失的傳輸實例化（`new StdioServerTransport()`）及 `server.connect(transport)` 呼叫，以符合同章節 Python 與 .NET 範例
- **14-sampling/README.md**：修正打字錯誤 — 更正 `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### 課程更新

**主 README.md**
- 在課程表中新增 5.17 項（使用 MCP 的對抗多代理推理）並附上新課程直接連結

**05-AdvancedTopics/README.md**
- 在課程表中新增第 5.17 課程行

**study_guide.md**
- 在心智圖和進階主題散文描述中新增對抗多代理推理議題

#### 程式碼與安全修正

**模組 05 - 對抗代理 (`mcp-adversarial-agents`)**
- **安全修正 — 命令注入**：在 TypeScript `run_python` 工具中，將 `execSync` 命令列插值替換為 `execFile` + `promisify`，消除命令注入風險（由 LLM 控制的程式碼現在作為字面 argv 元素傳遞，無 Shell 介入）
- **MCP 工具迴圈連接**：更新 Python 辯論指揮者使用 `AsyncAnthropic` 客戶端（取代阻塞同步 `Anthropic`），每回合直接傳遞活躍的 `ClientSession` 給代理，透過 `session.list_tools()` 獲取工具定義，並使用循環中的 `session.call_tool()` 發送 `tool_use` 區塊，直至模型輸出最終文字回應

#### 依賴更新

- 將多個套件（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）中的 `hono` 升級到 4.12.12 版本
- 將 TypeScript 套件中 `@hono/node-server` 從 1.19.11 升級至 1.19.13
- 將 Python 套件（10-StreamliningAIWorkflows 實驗室 3 和 4）中 `cryptography` 從 46.0.5 升級至 46.0.7
- 將 10-StreamliningAIWorkflows 檢查器中的 `lodash` 從 4.17.23 升級至 4.18.1

#### 翻譯

- 同步更新 48 種以上語言的翻譯以符合最新原始碼變更（i18n 更新）

---

## 2026年2月5日

### 倉庫範圍驗證與導航改進

#### 新增課程內容

**模組 03 - 入門**
- **12-mcp-hosts/README.md**：全新 MCP 主機設置綜合指引
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf 配置示例
  - 所有主要主機的 JSON 配置模板
  - 傳輸類型比較表（stdio、SSE/HTTP、WebSocket）
  - 常見連線問題故障排除
  - 主機配置安全最佳實踐

- **13-mcp-inspector/README.md**：MCP Inspector 除錯指南
  - 安裝方式（npx、npm 全域、原始碼）
  - 透過 stdio 與 HTTP/SSE 連接服務器
  - 測試工具、資源和提示工作流程
  - VS Code 與 MCP Inspector 整合
  - 常見除錯情境和解決方案

**模組 04 - 實務實作**
- **pagination/README.md**：分頁實作指南
  - Python、TypeScript、Java 中的游標分頁範式
  - 客戶端分頁處理
  - 游標設計策略（不透明 vs 結構化）
  - 性能優化建議

**模組 05 - 進階主題**
- **mcp-protocol-features/README.md**：協定特色深入分析
  - 進度通知實作
  - 請求取消模式
  - 帶 URI 範本的資源模板
  - 伺服器生命週期管理
  - 日誌等級控制
  - 以 JSON-RPC 錯誤碼的錯誤處理模式

#### 導航修正（24+ 文件更新）

**主模組 README 文件**
 目前同時連結首課與下一模組

**02-Security 子文件**
- 所有 5 個補充安全文件現有「下一步」導航：

**09-CaseStudy 文件**
- 所有案例研究文件現有連續導航：

**10-StreamliningAI 實驗室**
在模組 10 概覽與模組 11 增加「下一步」區塊

#### 程式碼與內容修正

**SDK 與依賴更新**
修正空白 openai 版本為 `^4.95.0`
將 SDK 從 `^1.8.0` 更新至 `>=1.26.0`
將 MCP 版本鎖定更新至 `>=1.26.0`

<strong>程式碼修正</strong>
修正無效模型 `gpt-4o-mini` 為 `gpt-4.1-mini`

<strong>內容修正</strong>
修正斷裂連結 `READMEmd` → `README.md`，修正課程表標題 `Module 1-3` → `Module 0-3`，修正大小寫敏感路徑
移除損壞重複案例研究 5 內容

<strong>初學者指導改善</strong>
為初學者新增適當介紹、學習目標和先決條件

#### 課程更新

**主 README.md**
- 在課程表新增 3.12 (MCP 主機)、3.13 (MCP Inspector)、4.1 (分頁)、5.16 (協定特色)

**模組 README**
新增第 12 與 13 課於課程清單
新增實踐指南區塊並附上分頁連結
新增課程 5.15（自訂傳輸）與 5.16（協定特色）

**study_guide.md**
- 更新心智圖納入所有新主題：MCP 主機設置、MCP Inspector、分頁策略、協定特色深入解析

## 2026年1月28日

### MCP 2025-11-25 規範合規審查

#### 核心概念強化 (01-CoreConcepts/)
- **新增客戶端原語 - Roots**：新增完整文檔說明 Roots 客戶端原語，使伺服器能理解檔案系統邊界與存取權限
- <strong>工具註解</strong>：新增關於工具行為註解（`readOnlyHint`、`destructiveHint`）的文檔，用於更佳的工具執行決策
- <strong>抽樣中的工具呼叫</strong>：更新抽樣文檔，包含抽樣請求中模型驅動工具調用的 `tools` 與 `toolChoice` 參數
- **URL 模式引導**：新增伺服器發起的外部 Web 互動基於 URL 的引導文檔
- **任務（實驗性）**：新增關於實驗性任務功能的章節，涵蓋耐久執行包裝與延遲結果檢索
- <strong>圖示支援</strong>：註明工具、資源、資源模板與提示現在可以包含作為額外元資料的圖示

#### 文件更新
- **README.md**：新增 MCP 規範 2025-11-25 版本參考與基於日期的版本控制說明
- **study_guide.md**：更新課程地圖，納入核心概念中任務與工具註解；更新文件時間戳

#### 規範合規驗證
- <strong>協定版本</strong>：確認所有文檔皆引用最新 MCP 規範 2025-11-25
- <strong>架構對齊</strong>：確認雙層架構（資料層 + 傳輸層）文檔準確
- <strong>原語文檔</strong>：驗證伺服器原語（資源、提示、工具）及客戶端原語（抽樣、引導、日誌、Roots）
- <strong>傳輸機制</strong>：確認 STDIO 與可串流 HTTP 傳輸文檔準確
- <strong>安全指引</strong>：確認與當前 MCP 安全最佳實踐文檔對齊

#### 主要 MCP 2025-11-25 功能記錄
- **OpenID Connect 探索**：透過 OIDC 進行驗證伺服器探索
- **OAuth 客戶端 ID 元資料文件**：建議的客戶端註冊機制
- **JSON Schema 2020-12**：MCP 架構定義的預設語法
- **SDK 分級系統**：正式要求 SDK 功能支援與維護等級
- <strong>治理結構</strong>：正式確立 MCP 工作組與利益團體治理模式

### 安全文件重大更新 (02-Security/)

#### MCP 安全高峰工作坊 (Sherpa) 整合
- <strong>新實作訓練資源</strong>：在所有安全文件中加入與 [MCP 安全高峰工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/) 的完整整合
- <strong>探險路線覆蓋</strong>：記錄從基地營至山頂的完整營地間進展
- **OWASP 對齊**：所有安全指導皆映射至 OWASP MCP Azure 安全指南風險

#### OWASP MCP 前十名整合
- <strong>新增章節</strong>：在主安全 README 中加入帶有 Azure 防護的 OWASP MCP 前十大安全風險表
- <strong>風險導向文件</strong>：更新 mcp-security-controls-2025.md，針對每個安全領域增加 OWASP MCP 風險參考
- <strong>參考架構</strong>：連結至 OWASP MCP Azure 安全指南參考架構與實作範式

#### 已更新的安全文件
- **README.md**：新增 Sherpa 工作坊概觀、探險路線表、OWASP MCP 前十大風險摘要及實作訓練區塊
- **mcp-security-controls-2025.md**：更新標頭為 2026 年 2 月，增加 OWASP 風險參考（MCP01-MCP08），修正規範版本不一致
- **mcp-security-best-practices-2025.md**：新增 Sherpa 與 OWASP 資源區塊，更新時間戳
- **mcp-best-practices.md**：新增含 Sherpa 與 OWASP 連結的實作訓練區塊
- **azure-content-safety-implementation.md**：新增 OWASP MCP06 參考，Sherpa 營地 3 對齊與額外資源區塊

#### 新增資源連結
- [MCP 安全高峰工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure 安全指南](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- 個別 OWASP MCP 風險頁面 (MCP01-MCP10)

### 課程全局 MCP 規範 2025-11-25 對齊

#### 模組 03 - 入門
- **SDK 文件**: 將 Go SDK 加入官方 SDK 清單；更新所有 SDK 參考以符合 MCP 規範 2025-11-25
- <strong>傳輸說明</strong>: 更新 STDIO 和 HTTP Streaming 傳輸描述，並附以明確規範參考

#### 模組 04 - 實作應用
- **SDK 更新**: 新增 Go SDK；SDK 清單附規範版本參考更新
- <strong>授權規範</strong>: 更新 MCP 授權規範連結至最新 2025-11-25 版本

#### 模組 05 - 進階主題
- <strong>新功能</strong>: 新增關於 MCP 規範 2025-11-25 功能（任務、工具註解、URL 模式激發、Roots）的說明
- <strong>安全資源</strong>: 新增 OWASP MCP Top 10 與 Sherpa 工作坊連結至額外參考

#### 模組 06 - 社群貢獻
- **SDK 清單**: 新增 Swift 和 Rust SDK；更新規範連結至 2025-11-25
- <strong>規範參考</strong>: 更新 MCP 規範連結至直接規範 URL

#### 模組 07 - 早期採用經驗
- <strong>資源更新</strong>: 新增 MCP 規範 2025-11-25 連結與 OWASP MCP Top 10 至額外資源

#### 模組 08 - 最佳實踐
- <strong>規範版本</strong>: 更新 MCP 規範參考至 2025-11-25
- <strong>安全資源</strong>: 新增 OWASP MCP Top 10 與 Sherpa 工作坊至額外參考

#### 模組 10 - 優化 AI 工作流程
- <strong>徽章更新</strong>: 將 MCP 版本徽章由 SDK 版本 (1.9.3) 改為規範版本 (2025-11-25)
- <strong>資源連結</strong>: 更新 MCP 規範連結；新增 OWASP MCP Top 10

#### 模組 11 - MCP 伺服器實作實驗室
- <strong>規範參考</strong>: 更新 MCP 規範連結至 2025-11-25 版本
- <strong>安全資源</strong>: 新增 OWASP MCP Top 10 至官方資源

## 2025年12月18日

### 安全文檔更新 - MCP 規範 2025-11-25

#### MCP 安全最佳實踐 (02-Security/mcp-best-practices.md) - 規範版本更新
- <strong>協議版本更新</strong>: 更新參考至最新 MCP 規範 2025-11-25（發布於2025年11月25日）
  - 將所有規範版本參考從 2025-06-18 更新至 2025-11-25
  - 將文件日期參考從 2025年8月18日更新至 2025年12月18日
  - 確認所有規範 URL 指向當前文檔
- <strong>內容驗證</strong>: 針對最新標準全面驗證安全最佳實踐
  - <strong>微軟安全解決方案</strong>: 驗證 Prompt Shields（前稱「越獄風險檢測」）、Azure 內容安全、Microsoft Entra ID 和 Azure Key Vault 的當前詞彙與連結
  - **OAuth 2.1 安全**: 確認符合最新 OAuth 安全最佳實踐
  - **OWASP 標準**: 驗證 OWASP LLMs Top 10 參考仍然有效
  - **Azure 服務**: 確認所有 Microsoft Azure 文件連結與最佳實踐
- <strong>標準對齊</strong>: 確認所有引用的安全標準皆為最新
  - NIST AI 風險管理框架
  - ISO 27001:2022
  - OAuth 2.1 安全最佳實踐
  - Azure 安全與合規框架
- <strong>實作資源</strong>: 驗證所有實作指南連結與資源
  - Azure API Management 認證模式
  - Microsoft Entra ID 集成指南
  - Azure Key Vault 機密管理
  - DevSecOps 管線與監控解決方案

### 文檔品質保證
- <strong>規範合規</strong>: 確保所有強制 MCP 安全需求（MUST/MUST NOT）與最新規範一致
- <strong>資源時效性</strong>: 驗證所有微軟文件、安全標準與實作指南外部連結
- <strong>最佳實踐覆蓋</strong>: 確認涵蓋完整的身份驗證、授權、AI 特定威脅、供應鏈安全與企業模式

## 2025年10月6日

### 入門章節擴展 — 進階伺服器使用與簡易認證

#### 進階伺服器使用 (03-GettingStarted/10-advanced)
- <strong>新增章節</strong>: 引入完整指南說明進階 MCP 伺服器使用方法，包括一般與低階伺服器架構。
  - **一般 vs 低階伺服器**: 詳細比較及 Python 與 TypeScript 範例代碼。
  - <strong>基於處理器設計</strong>: 說明基於處理器的工具/資源/提示管理，用於可擴展且靈活的伺服器實現。
  - <strong>實用模式</strong>: 真實情境中低階伺服器模式對進階功能與架構的優勢。

#### 簡易認證 (03-GettingStarted/11-simple-auth)
- <strong>新增章節</strong>: 步驟導引說明如何在 MCP 伺服器中實作簡易認證。
  - <strong>認證概念</strong>: 清楚解釋認證與授權差異及憑證處理。
  - <strong>基礎認證實作</strong>: Python (Starlette) 與 TypeScript (Express) 中介軟體認證模式範例代碼。
  - <strong>邁向進階安全</strong>: 指引從簡易認證開始，進階至 OAuth 2.1 與 RBAC，並參考進階安全模組。

這些新增內容提供實用的動手指導，協助建構更穩健、安全且靈活的 MCP 伺服器實作，連結基礎概念與進階生產模式。

## 2025年9月29日

### MCP 伺服器資料庫整合實驗室 — 全面實操學習路徑

#### 11-MCPServerHandsOnLabs - 新增完整資料庫整合課程
- **完整 13 實驗學習路徑**: 新增實用課程，說明如何構建具生產力的 MCP 伺服器並整合 PostgreSQL 資料庫
  - <strong>真實案例實作</strong>: Zava Retail 分析案例展示企業級模式
  - <strong>結構化學習進度</strong>:
    - **實驗 00-03: 基礎** - 介紹、核心架構、安全與多租戶、環境設定
    - **實驗 04-06: 建構 MCP 伺服器** - 資料庫設計與結構、MCP 伺服器實作、工具開發
    - **實驗 07-09: 進階功能** - 語義搜索整合、測試與調試、VS Code 整合
    - **實驗 10-12: 生產與最佳實踐** - 部署策略、監控與可觀察性、最佳實踐與優化
  - <strong>企業技術</strong>: FastMCP 框架、PostgreSQL 與 pgvector、Azure OpenAI 嵌入、Azure Container Apps、Application Insights
  - <strong>進階功能</strong>: 行級安全 (RLS)、語義搜尋、多租戶資料存取、向量嵌入、實時監控

#### 術語標準化 - 模組到實驗室轉換
- <strong>文檔系統性更新</strong>: 系統性地將 11-MCPServerHandsOnLabs 所有 README 文件中的「模組」改為「實驗」
  - <strong>章節標題</strong>: 將所有 13 個實驗的「本模組涵蓋內容」更新為「本實驗涵蓋內容」
  - <strong>內容描述</strong>: 文本中「本模組提供...」改為「本實驗提供...」
  - <strong>學習目標</strong>: 將「完成本模組後...」改為「完成本實驗後...」
  - <strong>導航連結</strong>: 將所有「模組 XX」引用改為「實驗 XX」於交叉參考及導航中
  - <strong>完成追蹤</strong>: 將「完成本模組後...」改為「完成本實驗後...」
  - <strong>保留技術參考</strong>: 在配置文件中保持 Python 模組參考不變（例如 "module": "mcp_server.main"）

#### 學習指南增強 (study_guide.md)
- <strong>視覺課程地圖</strong>: 新增「11. 資料庫整合實驗室」章節，完整展示實驗結構
- <strong>倉庫結構</strong>: 從十個主章節更新為十一個，詳述 11-MCPServerHandsOnLabs
- <strong>學習路徑指導</strong>: 增強導航說明，覆蓋 00-11 課程章節
- <strong>技術涵蓋</strong>: 新增 FastMCP、PostgreSQL、Azure 服務整合細節
- <strong>學習成果</strong>: 強調生產就緒的伺服器開發、資料庫整合模式與企業安全

#### 主 README 結構增強
- <strong>實驗室術語</strong>: 11-MCPServerHandsOnLabs 主要 README.md 全面統一使用「實驗」結構
- <strong>學習路徑組織</strong>: 清楚呈現從基礎概念到進階實作及生產部署的進度
- <strong>實務導向</strong>: 強調實用的動手學習及企業級模式與技術

### 文檔品質與一致性提升
- <strong>動手學習強調</strong>: 整體文檔中強化實驗室實操教學法
- <strong>企業模式聚焦</strong>: 突出台生產就緒實現與企業安全考量
- <strong>技術整合</strong>: 全面覆蓋現代 Azure 服務與 AI 整合模式
- <strong>學習進程</strong>: 清晰結構化路徑，從基礎至生產部署

## 2025年9月26日

### 案例研究增強 — GitHub MCP Registry 整合

#### 案例研究 (09-CaseStudy/) — 生態系發展聚焦
- **README.md**: 大幅擴充，新增詳細 GitHub MCP Registry 案例研究
  - **GitHub MCP Registry 案例研究**: 全面審視 GitHub 在 2025 年 9 月推出的 MCP Registry
    - <strong>問題分析</strong>: 詳細探討 MCP 伺服器分散發現與部署的挑戰
    - <strong>解決架構</strong>: GitHub 集中式註冊中心與一鍵安裝 VS Code 擴充功能
    - <strong>商業影響</strong>: 提升開發者入門與生產效率的量化成果
    - <strong>策略價值</strong>: 聚焦模組化代理部署與跨工具互操作性
    - <strong>生態系發展</strong>: 定位為代理整合基礎平台
  - <strong>強化案例結構</strong>: 更新所有七個案例研究，統一格式與詳細描述
    - Azure AI 旅行代理: 多代理協調聚焦
    - Azure DevOps 整合: 工作流程自動化焦點
    - 即時文件檢索: Python 控制台客戶端實作
    - 互動式學習計劃生成器: Chainlit 對話式網頁應用
    - 編輯器中文件: VS Code 與 GitHub Copilot 整合
    - Azure API 管理: 企業 API 整合模式
    - GitHub MCP Registry: 生態系發展與社群平台
  - <strong>全面結論</strong>: 重寫結論部分，強調七個涵蓋多元 MCP 實作維度的案例研究
    - 企業整合、多代理協調、開發者生產力
    - 生態系發展、教育應用分類
    - 深化架構模式、實作策略與最佳實踐見解
    - 強調 MCP 作為成熟、生產就緒協議

#### 學習指南更新 (study_guide.md)
- <strong>視覺課程地圖</strong>: 更新心智圖，將 GitHub MCP Registry 加入案例研究章節
- <strong>案例描述</strong>: 從一般描述增強至七個詳細全面案例研究細分
- <strong>倉庫結構</strong>: 更新第十章節反映詳細案例研究覆蓋與具體實作細節
- <strong>變更紀錄整合</strong>: 新增 2025年9月26日 條目，記錄 GitHub MCP Registry 新增及案例研究強化
- <strong>日期更新</strong>: 更新頁尾時間戳至最新修訂 (2025年9月26日)

### 文檔品質提升
- <strong>一致性強化</strong>: 統一七個案例研究範例的格式與結構
- <strong>全面覆蓋</strong>: 案例研究涵蓋企業、開發者生產力與生態系發展場景
- <strong>策略定位</strong>: 強化 MCP 作為代理系統部署基礎平台的定位
- <strong>資源整合</strong>: 將 GitHub MCP Registry 連結更新納入額外資源

## 2025年9月15日

### 進階主題擴展 — 自訂傳輸與上下文工程

#### MCP 自訂傳輸 (05-AdvancedTopics/mcp-transport/) - 新進階實作指南
- **README.md**: 完整自訂 MCP 傳輸機制實作指南
  - **Azure Event Grid 傳輸**: 完整無伺服器事件驅動傳輸實作
    - 包含 C#、TypeScript 與 Python 範例及 Azure Functions 整合
    - 針對可擴展 MCP 解決方案的事件驅動架構模式
    - Webhook 接收器與推送訊息處理
  - **Azure Event Hubs 傳輸**: 高吞吐量串流傳輸實作
    - 低延遲場景的即時串流能力
    - 分區策略與檢查點管理
    - 訊息批處理與效能優化
  - <strong>企業整合模式</strong>: 生產就緒架構範例
    - 分布式 MCP 處理跨多個 Azure Functions
    - 混合傳輸架構結合多種傳輸類型
    - 訊息持久性、可靠性與錯誤處理策略
  - <strong>安全與監控</strong>: Azure Key Vault 整合與可觀察性模式
    - 託管身份驗證與最小權限存取
    - Application Insights 遙測與效能監控
    - 斷路器與容錯模式
  - <strong>測試框架</strong>: 自訂傳輸的全面測試策略
    - 使用偽件與模擬框架的單元測試
    - Azure 測試容器的整合測試
    - 效能與負載測試考量

#### 上下文工程 (05-AdvancedTopics/mcp-contextengineering/) - 新興 AI 學科
- **README.md**: 對上下文工程作全面探索，作為一門新興領域
  - <strong>核心原則</strong>: 完整上下文共享、動作決策感知與上下文視窗管理

  - **MCP 協議對齊**：MCP 設計如何解決上下文工程挑戰
    - 上下文視窗限制和漸進式加載策略
    - 相關性判斷和動態上下文檢索
    - 多模態上下文處理和安全性考量
  - <strong>實作方法</strong>：單線程與多代理架構
    - 上下文分塊和優先級技術
    - 漸進式上下文加載與壓縮策略
    - 分層上下文方法與檢索優化
  - <strong>測量框架</strong>：新興指標用於上下文效能評估
    - 輸入效率、效能、品質及用戶體驗考量
    - 上下文優化的實驗方法
    - 失效分析與改進方法

#### 課程導覽更新 (README.md)
- <strong>強化模組結構</strong>：更新課程表以包含新的進階主題
  - 新增上下文工程 (5.14) 及自訂傳輸 (5.15) 條目
  - 各模組間格式和導覽鏈接一致化
  - 更新描述以反映當前內容範圍

### 目錄結構改進
- <strong>命名標準化</strong>：將 "mcp transport" 重命名為 "mcp-transport"，與其他進階主題資料夾一致
- <strong>內容組織</strong>：所有 05-AdvancedTopics 資料夾現遵循統一命名模式 (mcp-[topic])

### 文件質量提升
- **MCP 規範對齊**：所有新內容皆參考 MCP 規範 2025-06-18
- <strong>多語言範例</strong>：提供 C#、TypeScript 及 Python 全面程式碼範例
- <strong>企業導向</strong>：全篇均採用生產級模式並整合 Azure 雲端
- <strong>視覺化文件</strong>：使用 Mermaid 圖示呈現架構與流程

## 2025年8月18日

### 文件全面更新 - MCP 2025-06-18 標準

#### MCP 安全最佳實踐 (02-Security/) - 完整現代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：完整重寫，符合 MCP 規範 2025-06-18
  - <strong>強制性要求</strong>：新增官方規範中明確 MUST/MUST NOT 要求並標示清晰
  - **12 核心安全實踐**：從 15 項列表重組為全面安全領域
    - 令牌安全與身份驗證，集成外部身份提供者
    - 會話管理與傳輸安全，包含密碼學要求
    - AI 專屬威脅防護，集成 Microsoft Prompt Shields
    - 存取控制和權限管理，遵循最小權限原則
    - 內容安全與監控，集成 Azure Content Safety
    - 供應鏈安全，全面元件驗證
    - OAuth 安全與混淆代理攻擊防護，實施 PKCE
    - 事件回應與復原，自動化能力
    - 合規與治理，符合法規要求
    - 進階安全控管，採用零信任架構
    - 微軟安全生態系統整合，全面解決方案
    - 持續安全演進，適應性做法
  - <strong>微軟安全解決方案</strong>：加強 Prompt Shields、Azure Content Safety、Entra ID 與 GitHub 高級安全整合指導
  - <strong>實作資源</strong>：依官方 MCP 文件、微軟安全解決方案、安全標準及實作指南分類全面資源鏈結

#### 進階安全控管 (02-Security/) - 企業等級實作
- **MCP-SECURITY-CONTROLS-2025.md**：全面改版，採用企業級安全框架
  - **9 大全面安全領域**：由基本控管擴充為詳細企業框架
    - 進階身份驗證與授權，整合 Microsoft Entra ID
    - 令牌安全與防止透傳控管，含全面驗證
    - 會話安全控管，防範會話劫持
    - AI 專屬安全控管，防範提示注入和工具污染
    - 混淆代理攻擊防護，OAuth 代理安全
    - 工具執行安全，沙箱隔離
    - 供應鏈安全控管，依賴驗證
    - 監控與偵測控管，整合 SIEM
    - 事件回應與復原，自動化能力
  - <strong>實作範例</strong>：新增詳細 YAML 設定區塊與程式碼範例
  - <strong>微軟解決方案整合</strong>：全面涵蓋 Azure 安全服務、GitHub 高級安全及企業身份管理

#### 進階主題安全 (05-AdvancedTopics/mcp-security/) - 生產準備實作
- **README.md**：企業安全實作完整重寫
  - <strong>當前規範對齊</strong>：更新為 MCP 規範 2025-06-18，包含強制性安全需求
  - <strong>強化認證</strong>：Microsoft Entra ID 整合，提供完善 .NET 與 Java Spring Security 範例
  - **AI 安全整合**：Microsoft Prompt Shields 與 Azure Content Safety 實作，附詳細 Python 範例
  - <strong>進階威脅緩解</strong>：全面實作範例涵蓋
    - 混淆代理攻擊防護，結合 PKCE 與用戶同意驗證
    - 令牌透傳防護，使用受眾驗證與安全令牌管理
    - 會話劫持防止，採用密碼學綁定與行為分析
  - <strong>企業安全整合</strong>：Azure Application Insights 監控、威脅偵測管線與供應鏈安全
  - <strong>實作檢查清單</strong>：明確標示強制與建議安全控管及微軟安全生態系優勢

### 文件質量與標準對齊
- <strong>規範引用</strong>：更新所有引用至 MCP 規範 2025-06-18
- <strong>微軟安全生態系</strong>：全篇均加強整合指導
- <strong>實務實作</strong>：新增 .NET、Java、Python 詳細程式碼範例及企業模式
- <strong>資源組織</strong>：全面分類官方文件、安全標準與實作指引
- <strong>視覺標示</strong>：清晰標記強制需求與建議做法


#### 核心概念 (01-CoreConcepts/) - 全面現代化
- <strong>協議版本更新</strong>：改為使用 MCP 規範 2025-06-18 日期版本 (YYYY-MM-DD 格式)
- <strong>架構精煉</strong>：增強 Hosts、Clients 與 Servers 描述，以符合現行 MCP 架構模式
  - Hosts 明確定義為協調多個 MCP 客戶端連線的 AI 應用
  - Clients 描述為維持與伺服器一對一關係的協議連接器
  - Servers 則增強本地與遠程部署場景說明
- <strong>原始元件重構</strong>：完整改寫伺服器與客戶端原語
  - 伺服器原語：資源（資料來源）、提示（模板）、工具（可執行函式）詳解與範例
  - 客戶端原語：抽樣（LLM 補全）、引導（用戶輸入）、記錄（調試/監控）
  - 更新為目前發現 (`*/list`)、檢索 (`*/get`) 及執行 (`*/call`) 方法模式
- <strong>協議架構</strong>：引入雙層架構模型
  - 資料層：基於 JSON-RPC 2.0，含生命週期管理與原語
  - 傳輸層：STDIO（本地）及可串流 HTTP 含 SSE（遠程）傳輸機制
- <strong>安全框架</strong>：周延安全原則，包括明確用戶同意、資料隱私保護、工具執行安全及傳輸層安全
- <strong>通訊模式</strong>：更新協議訊息，展現初始化、發現、執行與通知流程
- <strong>程式碼範例</strong>：更新多語言範例（.NET、Java、Python、JavaScript）以反映現行 MCP SDK 樣板

#### 安全 (02-Security/) - 全面安全改造
- <strong>標準對齊</strong>：完全符合 MCP 規範 2025-06-18 安全要求
- <strong>身份驗證演進</strong>：紀錄自訂 OAuth 伺服器至外部身份提供者授權 (Microsoft Entra ID) 的演變
- **AI 專屬威脅分析**：加強現代 AI 攻擊向量之覆蓋
  - 詳細的提示注入攻擊場景與實例
  - 工具污染機制及「地毯式抽離」攻擊模式
  - 上下文視窗污染及模型混淆攻擊
- **微軟 AI 安全解決方案**：全面涵蓋微軟安全生態系
  - AI Prompt Shields，含進階偵測、聚光與分隔符技術
  - Azure Content Safety 整合模式
  - GitHub 高級安全，用於供應鏈防護
- <strong>進階威脅緩解</strong>：詳細安全控管涵蓋
  - MCP 專屬會話劫持攻擊場景與密碼學會話 ID 需求
  - MCP 代理場景下混淆代理問題與明確同意要求
  - 令牌透傳漏洞與強制驗證控管
- <strong>供應鏈安全</strong>：擴展 AI 供應鏈覆蓋，含基礎模型、嵌入服務、上下文提供者及第三方 API
- <strong>基礎安全</strong>：加強與企業安全模式整合，包括零信任架構與微軟安全生態系
- <strong>資源組織</strong>：依類型（官方文件、標準、研究、微軟解決方案、實作指南）完整分類資源鏈結

### 文件質量改進
- <strong>結構化學習目標</strong>：強化具體且可執行的學習成果
- <strong>交叉引用</strong>：新增安全與核心概念主題間鏈結
- <strong>當前資訊</strong>：更新所有日期引用與規範鏈結至最新標準
- <strong>實作指導</strong>：於兩大章節提供具體且可執行的實作指南

## 2025年7月16日

### README 及導覽改進
- 完全重新設計 README.md 中的課程導覽
- 以更易用的表格格式取代 `<details>` 標籤
- 在新建的 "alternative_layouts" 資料夾中建立替代佈局選項
- 新增卡片式、分頁樣式及手風琴式導覽範例
- 更新庫結構章節以包含所有最新檔案
- 強化「如何使用本課程」章節，給出清晰建議
- 更新 MCP 規範連結指向正確 URL
- 課程結構中新增上下文工程章節 (5.14)

### 學習指南更新
- 完全修訂學習指南以符合現有庫結構
- 新增 MCP 客戶端與工具及熱門 MCP 伺服器新章節
- 更新視覺課程地圖，精確反映所有主題
- 增強進階主題描述，涵蓋所有專門領域
- 更新案例研究，呈現實際範例
- 新增此全面變更記錄

### 社群貢獻 (06-CommunityContributions/)
- 新增關於影像生成 MCP 伺服器的詳細資訊
- 新增全面的 VSCode 中使用 Claude 的章節
- 新增 Cline 終端客戶端設定與使用說明
- 更新 MCP 客戶端章節，涵括所有熱門客戶端選項
- 強化貢獻範例，提供更精確的程式碼範例

### 進階主題 (05-AdvancedTopics/)
- 統一命名組織所有專門主題資料夾
- 新增上下文工程教材與範例
- 新增 Foundry 代理整合文件
- 強化 Entra ID 安全整合文件

## 2025年6月11日

### 初始建立
- 發布 MCP 入門課程第一版
- 建立所有 10 個主章節的基本結構
- 實作視覺課程地圖以便導覽
- 新增多種程式語言的初始範例專案

### 快速入門 (03-GettingStarted/)
- 建立第一批伺服器實作範例
- 新增客戶端開發指導
- 包含 LLM 客戶端整合指令
- 新增 VS Code 整合文件
- 實作 Server-Sent Events (SSE) 伺服器範例

### 核心概念 (01-CoreConcepts/)
- 新增詳盡的客戶端-伺服器架構說明
- 撰寫關鍵協議元件文件
- 紀錄 MCP 訊息模式

## 2025年5月23日

### 資料庫結構
- 初始化庫，設定基礎資料夾結構
- 為各主要章節建立 README 文件
- 設置翻譯基礎架構
- 新增圖像資產與圖示

### 文件
- 建置初版 README.md 課程總覽
- 新增 CODE_OF_CONDUCT.md 與 SECURITY.md
- 設置 SUPPORT.md 並提供求助指導
- 建立初步學習指南架構

## 2025年4月15日

### 規劃與框架
- MCP 入門課程初期規劃
- 定義學習目標及目標受眾
- 制定 10 章節課程架構大綱
- 發展範例與案例研究的概念框架
- 建立關鍵概念的初期原型範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
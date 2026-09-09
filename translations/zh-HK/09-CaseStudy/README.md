# MCP 實戰：真實案例研究

[![MCP 實戰：真實案例研究](../../../translated_images/zh-HK/10.3262cc80b4de5071.webp)](https://youtu.be/IxshWb2Az5w)

_(點擊上圖觀看本課程影片)_

Model Context Protocol（MCP）正在改變 AI 應用程式與數據、工具及服務互動的方式。本節展示了多個真實案例，示範 MCP 在各類企業場景中的實際應用。

## 概覽

本節展示了具體 MCP 實作範例，突顯企業如何利用此協議解決複雜的商業挑戰。透過這些案例研究，您將深入了解 MCP 在真實場景中的多功能性、擴展性以及實用效益。

## 主要學習目標

透過探索這些案例，您將能：

- 理解 MCP 如何應用於解決特定業務問題
- 學習不同的整合模式與建築方法
- 掌握在企業環境中落實 MCP 的最佳實踐
- 獲得真實實作中遇到的挑戰與解決方案洞見
- 識別在自身專案中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅遊代理人 — 參考實作](./travelagentsample.md)

本案例研究探討微軟的完整參考解決方案，展示如何利用 MCP、Azure OpenAI 及 Azure AI 搜尋來建構多代理人驅動的 AI 旅遊規劃應用。專案亮點包括：

- 透過 MCP 進行多代理人協同編排
- 使用 Azure AI 搜尋實現企業數據整合
- 採用 Azure 服務保障安全且可擴展的架構
- 可擴展的工具與可重用 MCP 元件
- 由 Azure OpenAI 支援的對話式用戶體驗

架構與實作細節為構建以 MCP 作為協調層的複雜多代理人系統提供有價值的洞見。

### 2. [從 YouTube 資料更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

本案例展示 MCP 在自動化工作流程中的實際應用，說明如何利用 MCP 工具：

- 從線上平台（YouTube）擷取數據
- 更新 Azure DevOps 系統中的工作項目
- 創建可重複使用的自動化流程
- 跨異構系統整合數據

此範例示範即使是相對簡單的 MCP 實作，也能通過自動化例行任務及提升系統間數據一致性帶來顯著效率提升。

### 3. [使用 MCP 實現即時文件檢索](./docs-mcp/README.md)

本案例指導您如何將 Python 控制台客戶端連接至 Model Context Protocol（MCP）伺服器，以檢索並記錄即時且具上下文感知的微軟文件。您將學習如何：

- 使用 Python 客戶端及官方 MCP SDK 連接 MCP 伺服器
- 運用串流 HTTP 客戶端達成高效即時數據檢索
- 呼叫伺服器端文件工具並將響應直接記錄至控制台
- 無需離開終端機即可整合最新微軟文件進入工作流程

本章包含實務練習、最小可行程式碼範例及進一步學習資源連結。詳見連結章節的完整步驟與程式碼，體驗 MCP 如何改變文件存取與開發人員生產力於控制台環境中。

### 4. [基於 MCP 的互動式學習計劃生成器 Web 應用](./docs-mcp/README.md)

本案例示範如何運用 Chainlit 與 Model Context Protocol（MCP）開發互動式 Web 應用，為任意主題生成個性化學習計劃。用戶可指定主題（如「AI-900 認證」）及學習時長（例如 8 週），應用將提供逐週內容建議。Chainlit 提供對話式聊天介面，提升互動性及適應性。

- 由 Chainlit 支援的對話式 Web 應用
- 用戶驅動的主題及時長輸入
- 透過 MCP 提供逐週內容推薦
- 聊天介面中的即時自適應回應

此專案展示對話式 AI 與 MCP 如何結合，打造動態且用戶驅動的現代網頁教育工具。

### 5. [在 VS Code 編輯器中使用 MCP 伺服器呈現文件](./docs-mcp/README.md)

本案例展示如何透過 MCP 伺服器，將微軟 Learn 文件直接帶入 VS Code 環境，無需切換瀏覽器分頁！您將看到如何：

- 使用 MCP 面板或命令面板在 VS Code 內即時搜尋與閱讀文件
- 參考文件並直接插入連結到 README 或課程 Markdown 檔案
- 結合 GitHub Copilot 與 MCP 實現無縫 AI 支援文件與程式流程
- 透過即時回饋與微軟準確資料驗證與強化文件
- 將 MCP 整合入 GitHub 工作流程以持續文件驗證

實作內容包含：

- 便捷設定的 `.vscode/mcp.json` 範例配置
- 基於截圖的編輯器內體驗演示
- 關於結合 Copilot 與 MCP 以提升生產力的技巧

此情境適合課程作者、文件撰寫者及開發者，他們希望工作時能專注於編輯器內，使用 MCP 支援的文件、Copilot 及驗證工具。

### 6. [APIM MCP 伺服器建立](./apimsample.md)

本案例提供如何透過 Azure API Management（APIM）建立 MCP 伺服器的逐步指南，涵蓋：

- 在 Azure API Management 中設置 MCP 伺服器
- 將 API 操作公開為 MCP 工具
- 配置速率限制與安全性政策
- 使用 Visual Studio Code 與 GitHub Copilot 測試 MCP 伺服器

此範例說明如何運用 Azure 能力創建強健的 MCP 伺服器，強化 AI 系統與企業 API 的整合。

### 7. [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)

本案例探討 GitHub 於 2025 年 9 月推出的 MCP Registry，解決 AI 生態圈中關於分散 MCP 伺服器發現與部署的核心問題。

#### 概述
**MCP Registry** 解決了散落於各個程式庫和註冊中心的 MCP 伺服器管理難題，過去這造成整合過程緩慢且易出錯。這些伺服器使 AI 代理能與外部系統（如 API、資料庫及文件來源）互動。

#### 問題陳述
建置代理工作流程的開發者面臨多項挑戰：
- 各平台 MCP 伺服器的 <strong>發現性差</strong>
- 散布於論壇與文件中的 <strong>重複設定問題</strong>
- 來自未經驗證且不可信來源的 <strong>安全風險</strong>
- 伺服器品質及相容性 <strong>缺乏標準化</strong>

#### 解決方案架構
GitHub MCP Registry 集中管理受信 MCP 伺服器，具備以下特色：
- 透過 VS Code 一鍵安裝，簡化設定流程
- 以星標、活躍度及社群驗證進行訊號過濾排序
- 與 GitHub Copilot 及其他 MCP 相容工具直接整合
- 採開放貢獻模式，允許社群及企業夥伴參與

#### 商業影響
該註冊中心帶來多項可量化成效：
- 使用 Microsoft Learn MCP Server 等工具，實現更快開發者上手，直接串流官方文件至代理
- 利用如 `github-mcp-server` 專用伺服器提升生產力，實現自然語言 GitHub 自動化（PR 建立、CI 重跑、程式碼掃描）
- 透過精選清單與透明配置標準，建立更強健的生態系信任

#### 策略價值
對專注於代理生命週期管理及可複現工作流程的從業人員而言，MCP Registry 提供：
- 具標準化元件的模組化代理部署能力
- 以註冊中心為基礎的評估管線，確保測試及驗證一致性
- 跨工具互操作性，促進不同 AI 平台的無縫整合

本案例證明 MCP Registry 不僅是目錄，更是可擴展且實務導向的模型整合與代理系統部署基石平台。

### 8. [從代理發佈至社群網絡](./publora-social-publishing.md)

本案例介紹一個 **可寫入的遠端 MCP 伺服器** — 其工具可代表用戶執行不可逆的操作 — 並以社群發佈為示範範例。代理草擬貼文，經人工核准後，伺服器將於多個網絡排程發布。

有趣之處在於發佈所施加的設計限制，且適用於任何寫入伺服器：

- **開放發現，驗證執行** — `tools/list` 無需憑證即可回答，方便註冊中心與客戶端檢視；而每次 `tools/call` 呼叫需憑證，否則回傳帶有 `WWW-Authenticate` 標頭的 `401` 錯誤
- **無需離帶步驟的 OAuth 註冊** — 動態客戶端註冊，`2026-07-28` 規範指向 Client ID Metadata Documents
- <strong>工具註解</strong>（`readOnlyHint`、`destructiveHint`、`idempotentHint`），使客戶端判斷需確認的操作 — 以提示為主，不強制執行，為連接器目錄審核所期待
- <strong>不可捏造識別碼</strong>，使幻覺值明顯失敗而非基於仿真值行動
- <strong>貼文工具所用冪等鍵</strong>，避免代理運行時重試產生重複發布
- <strong>工具架構中描述的無操作目標</strong>，用於審核與 CI，執行整個寫入流程卻不發布任何內容

本章末附有短小檢查表，方便您評估自己構建的伺服器。

## 結語

這八個全面的案例研究展現了 Model Context Protocol 在多元真實場景中驚人的多功能性及實用性。從複雜的多代理旅行規劃系統及企業 API 管理，到流暢的文件工作流程及革新的 GitHub MCP Registry，這些案例展示 MCP 如何以標準化且可擴展的方式連接 AI 系統與必需的工具、數據和服務，帶來卓越價值。

案例範疇涵蓋 MCP 實作的多個層面：
- <strong>企業整合</strong>：Azure API 管理與 Azure DevOps 自動化
- <strong>多代理編排</strong>：協調式 AI 代理的旅遊規劃
- <strong>開發者生產力</strong>：VS Code 整合與即時文件存取
- <strong>生態系發展</strong>：GitHub MCP Registry 作為核心平台
- <strong>教育應用</strong>：互動式學習計劃生成器與對話式介面

透過研究這些實作，您將獲得關鍵洞見：
- 適用不同規模與用例的建築模式
- 平衡功能性與可維護性的實作策略
- 生產部署中的安全及擴展性考量
- MCP 伺服器開發與客戶端整合的最佳實踐
- 以生態思維構建互聯的 AI 驅動解決方案

這些案例共同說明 MCP 不僅是理論框架，而是一個成熟且生產就緒的協議，使解決複雜的商業問題成為可能。無論您是在開發簡單自動化工具或先進多代理系統，此處展示的模式與方法都將成為您 MCP 專案的堅實基礎。

## 其他資源

- [Azure AI 旅遊代理人 GitHub 程式庫](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP 工具](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP 工具](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP 伺服器](https://github.com/MicrosoftDocs/mcp)
- [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)
- [MCP 社群範例](https://github.com/microsoft/mcp)

## 接下來

- 上一節：[模組 8：最佳實踐](../08-BestPractices/README.md)
- 下一節：[模組 10：簡化 AI 工作流程：利用 AI 工具組建構 MCP 伺服器](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
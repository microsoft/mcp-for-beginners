# MCP 實戰：真實案例研究

[![MCP 實戰：真實案例研究](../../../translated_images/zh-TW/10.3262cc80b4de5071.webp)](https://youtu.be/IxshWb2Az5w)

_(點擊上方圖片觀看本課程影片)_

模型上下文協議（Model Context Protocol，MCP）正在改變 AI 應用程序與數據、工具和服務的互動方式。本節展示了多個真實案例，說明 MCP 在各種企業場景中的實際應用。

## 概述

本節展示 MCP 實作的具體範例，突顯各組織如何利用此協議解決複雜的業務挑戰。透過檢視這些案例研究，您將深入了解 MCP 在真實世界情境中的多樣性、可擴展性及實際效益。

## 主要學習目標

透過探索這些案例，您將能：

- 了解 MCP 如何應用於解決特定的商業問題
- 學習不同的整合模式和架構方法
- 辨識在企業環境中實作 MCP 的最佳實務
- 獲取真實實作中遇到的挑戰與解決方案洞見
- 識別在您自身專案中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅遊代理人 — 參考實作](./travelagentsample.md)

本案例研究剖析微軟的全面參考解決方案，演示如何利用 MCP、Azure OpenAI 及 Azure AI Search 建構多代理人協同的 AI 旅遊規劃應用。專案重點包括：

- 透過 MCP 進行多代理人編排
- 與 Azure AI Search 的企業數據整合
- 使用 Azure 服務構築安全且可擴展的架構
- 利用可重用的 MCP 組件實現可擴展工具開發
- 由 Azure OpenAI 支援的對話式使用體驗

架構與實作細節提供了如何以 MCP 作為協調層建構複雜多代理系統的寶貴見解。

### 2. [從 YouTube 資料更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

該案例展示 MCP 在自動化工作流程中的實際應用示例。它說明如何利用 MCP 工具：

- 從線上平台（YouTube）擷取資料
- 更新 Azure DevOps 系統中的工作項目
- 創建可重複使用的自動化工作流程
- 整合不同系統間的數據

此示例說明即使是相對簡單的 MCP 實作，也能透過自動化例行任務和提升系統間數據一致性帶來顯著效率提升。

### 3. [使用 MCP 即時文件檢索](./docs-mcp/README.md)

本案例引導您如何將 Python 終端客戶端連接到 Model Context Protocol（MCP）伺服器以檢索並記錄即時且具上下文感知的微軟文件。您將學會如何：

- 使用 Python 客戶端和官方 MCP SDK 連接 MCP 伺服器
- 使用串流 HTTP 客戶端高效地進行即時資料檢索
- 在伺服器上調用文件工具，並直接將回應記錄到終端
- 不離開終端將最新的微軟文件整合入您的工作流程

本章包含實作練習、精簡代碼範例與深度學習資源連結。詳見連結章節中的完整示範及程式碼，了解 MCP 如何改變基於終端的文檔存取和開發者生產力。

### 4. [使用 MCP 的互動式學習計畫產生器網頁應用](./docs-mcp/README.md)

此案例演示如何使用 Chainlit 與 Model Context Protocol (MCP) 建置互動式網頁應用，為任一主題生成個人化學習計畫。使用者可指定主題（如「AI-900 證照」）及學習時長（例如 8 週），應用會逐週提供推薦內容。Chainlit 提供對話型聊天介面，使體驗更具互動性與適應性。

- 由 Chainlit 支援的對話式網頁應用
- 使用者驅動的主題與時長輸入
- 利用 MCP 提供週別內容推薦
- 聊天介面中即時且適應性的回應

本專案展現對話式 AI 與 MCP 如何結合，創造現代網站環境中動態且用戶驅動的教育工具。

### 5. [VS Code 中利用 MCP 伺服器查看內嵌文件](./docs-mcp/README.md)

本案例示範如何將 Microsoft Learn Docs 直接帶入 VS Code 環境中，無需再切換瀏覽器分頁！您將看到如何：

- 使用 MCP 面板或命令面板，在 VS Code 內立即搜尋並閱讀文件
- 在 README 或課程 Markdown 檔直接參考文件並插入連結
- 搭配 GitHub Copilot 與 MCP，實現無縫的 AI 文件與程式碼工作流程
- 透過即時反饋和微軟來源的精準性驗證與增強您的文件
- 整合 MCP 與 GitHub 工作流程，持續進行文件驗證

實作包括：

- 用於簡易設置的範例 `.vscode/mcp.json` 配置檔
- 內嵌編輯體驗的截圖導覽
- 結合 Copilot 與 MCP 的生產力提升小技巧

此場景非常適合課程作者、文檔撰寫者以及開發者，他們希望在編輯器中專注工作，同時使用文件、Copilot 和驗證工具，全由 MCP 支援。

### 6. [建立 APIM MCP 伺服器](./apimsample.md)

本案例提供 Azure API 管理服務（APIM）建立 MCP 伺服器的分步指導。內容涵蓋：

- 在 Azure API 管理中設定 MCP 伺服器
- 將 API 操作公開為 MCP 工具
- 配置流量限制和安全性策略
- 利用 Visual Studio Code 和 GitHub Copilot 測試 MCP 伺服器

本示例展示如何利用 Azure 能力打造強健的 MCP 伺服器，應用於多種場域，提升 AI 系統與企業 API 的整合效果。

### 7. [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)

本案例探討 GitHub 於 2025 年 9 月推出的 MCP Registry，如何解決 AI 生態系中的一項關鍵挑戰：MCP 伺服器發現與部署分散且繁瑣。

#### 概述
**MCP Registry** 解決了 MCP 伺服器散佈於多個儲存庫與註冊中心的問題，整合速度緩慢且易出錯。這些伺服器允許 AI 代理與外部系統（如 API、資料庫和文件來源）互動。

#### 問題陳述
開發代理工作流程的開發者遇到幾個挑戰：
- **MCP 伺服器發現度低**，分散於不同平台
- <strong>重複設定問題</strong>散布於論壇和文件中
- <strong>安全風險</strong>來自未驗證且不受信任的來源
- <strong>伺服器品質與兼容性缺乏標準化</strong>

#### 解決方案架構
GitHub 的 MCP Registry 集中可信任的 MCP 伺服器，具備關鍵功能：
- VS Code 一鍵安裝集成，簡化設定步驟
- 依據星數、活動及社群驗證過濾排序，降低噪音
- 與 GitHub Copilot 及其他 MCP 相容工具的直接整合
- 採用開放的貢獻模式，社群及企業合作夥伴皆可參與

#### 商業影響
該註冊中心帶來可衡量的改善：
- 使開發者更快上手，例如 Microsoft Learn MCP Server 可直接將官方文件串流至代理
- 透過專門伺服器如 `github-mcp-server` 提升生產力，支援自然語言 GitHub 自動化（PR 建立、CI 重跑、代碼掃描）
- 以策展清單與透明設定標準強化生態系信任

#### 策略價值
對專精代理生命週期管理與可重現工作流程的實務者而言，MCP Registry 提供：
- 採用標準元件的模組化代理部署能力
- 註冊中心支援的評估管線，確保測試與驗證一致性
- 跨工具互操作性，促進不同 AI 平台無障礙整合

本案例證明 MCP Registry 不僅是目錄，而是可擴展、真實模型整合及代理系統部署的基石平台。

### 8. [代理人向社交網路發布內容](./publora-social-publishing.md)

本案例示範一個「具寫入能力的遠端 MCP 伺服器」——其工具代表用戶執行不可逆操作——以社交發布為範例。一名代理人草擬貼文，由人工審核後，伺服器負責排程發佈於各大網絡。

有趣的是發布操作所帶來的設計限制，這些限制適用於任何執行寫入（非讀取）操作的伺服器：

- **公開發現、驗證後執行** — `tools/list` 無需認證即可回應，以供註冊中心和客戶端探索；而所有 `tools/call` 須攜帶令牌，否則回傳帶有 `WWW-Authenticate` 標頭的 `401` 狀態碼
- **OAuth 註冊無需帶外流程** — 目前使用動態客戶端註冊，並以「客戶端 ID 元資料文件」為 2026-07-28 規範指引
- <strong>工具註解</strong>（`readOnlyHint`、`destructiveHint`、`idempotentHint`），用於客戶端決定確認與否——作為提示並非強制，且連接器目錄於審核時已經要求
- <strong>不可杜撰的識別碼</strong>，虛構值會明顯失敗，避免使用看似合理但錯誤的值
- <strong>貼文創建工具須支援冪等鍵</strong>，確保代理執行重試時不會重複發布
- <strong>工具架構中描述的無操作目標</strong>，用於完整測試寫入流程但不實際發布，用於審核和持續整合

本章最後附有適用於您建立的伺服器的簡短核對清單。

## 結語

這八個完整的案例研究展現了模型上下文協議在多元真實場景中的卓越多樣性與實用價值。從複雜的多代理旅遊規劃系統、企業 API 管理，到精簡的文檔工作流程與革新的 GitHub MCP Registry，這些範例證明 MCP 提供標準化且可擴展的方式，將 AI 系統與必需的工具、數據與服務連結，創造出卓越價值。

案例涵蓋 MCP 實作的多個方面：
- <strong>企業整合</strong>：Azure API 管理與 Azure DevOps 自動化
- <strong>多代理人編排</strong>：協調 AI 代理進行旅遊規劃
- <strong>開發者生產力</strong>：VS Code 整合及即時文件存取
- <strong>生態系發展</strong>：GitHub MCP Registry 作為基礎平台
- <strong>教育應用</strong>：互動學習計畫產生器與對話式介面

透過學習這些實作，您將獲得關鍵見解：
- 適用於不同規模與用例的架構模式
- 平衡功能與可維護性的實作策略
- 生產環境部署的安全性與可擴展性考量
- MCP 伺服器開發與客戶端整合的最佳實務
- 建構相互連結的 AI 解決方案的生態系思維

這些範例共同展示 MCP 不僅是理論框架，更是成熟且適用於生產環境的協議，能為複雜業務挑戰提供實際解決方案。無論您構建簡單自動化工具或複雜多代理系統，這裡所示範的模式與方法都為您的 MCP 專案打下堅實基礎。

## 附加資源

- [Azure AI 旅遊代理人 GitHub 儲存庫](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP 工具](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP 工具](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP 伺服器](https://github.com/MicrosoftDocs/mcp)
- [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)
- [MCP 社群範例](https://github.com/microsoft/mcp)

## 接下來是

- 上一篇：[模組 8：最佳實務](../08-BestPractices/README.md)
- 下一篇：[模組 10：優化 AI 工作流程：使用 AI 工具包建置 MCP 伺服器](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
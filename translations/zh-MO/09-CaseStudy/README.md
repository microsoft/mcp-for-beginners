# MCP 實戰：真實案例研究

[![MCP 實戰：真實案例研究](../../../translated_images/zh-MO/10.3262cc80b4de5071.webp)](https://youtu.be/IxshWb2Az5w)

_(點擊上圖觀看本課程影片)_

模型上下文協議（Model Context Protocol，MCP）正在改變 AI 應用程式與資料、工具和服務互動的方式。本節展示了多個真實案例，說明 MCP 在各種企業場景中的實際應用。

## 概覽

本節呈現 MCP 實作的具體範例，強調組織如何利用此協議解決複雜商業挑戰。透過這些案例研究，你將瞭解 MCP 在現實場景中多樣性、可擴展性以及實用效益。

## 主要學習目標

探討這些案例後，你將能夠：

- 理解 MCP 如何應用於解決特定商業問題
- 了解不同的整合模式與架構方法
- 識別企業環境下實施 MCP 的最佳實踐
- 獲得真實實作中遇到的挑戰與解決方案洞見
- 發現將相似模式應用於自身專案的機會

## 特色案例研究

### 1. [Azure AI 旅遊代理 – 參考實作範例](./travelagentsample.md)

此案例研究探討微軟完整的參考解決方案，示範如何利用 MCP、Azure OpenAI 與 Azure AI 搜尋建構一個多代理、AI 驅動的旅遊計劃應用。專案亮點包括：

- 透過 MCP 實現多代理協調
- 與 Azure AI 搜尋的企業資料整合
- 使用 Azure 服務打造安全且可擴展的架構
- 可擴充且可重複使用的 MCP 元件工具
- 由 Azure OpenAI 推動的對話式用戶體驗

架構與實作詳情提供了以 MCP 作為協調層建構複雜多代理系統的寶貴洞察。

### 2. [從 YouTube 資料更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

此案例演示 MCP 在自動化工作流程中的實際應用。展示了如何使用 MCP 工具：

- 從線上平台（YouTube）提取資料
- 更新 Azure DevOps 系統中的工作項目
- 創建可重複使用的自動化工作流
- 整合各異系統之間的資料

此範例說明即使相對簡單的 MCP 實現，也能透過自動化例行任務與改進系統間資料一致性，提供顯著效率提升。

### 3. [使用 MCP 進行即時文件檢索](./docs-mcp/README.md)

此案例指導你如何連接 Python 命令列客戶端與 Model Context Protocol (MCP) 伺服器，檢索並記錄即時、上下文感知的 Microsoft 文件。你將學習如何：

- 使用 Python 客戶端及官方 MCP SDK 連接 MCP 伺服器
- 使用串流 HTTP 客戶端高效即時檢索資料
- 呼叫伺服器上的文件工具並將回應直接記錄於命令列
- 不離開終端機即整合最新 Microsoft 文件入工作流程

本章節包含實作作業、一個最小可用程式碼範例及進階學習資源連結。請參考連結章節的完整步驟和程式碼，了解 MCP 如何在以命令行為主的環境中改變文件訪問及開發者生產力。

### 4. [使用 MCP 建立互動式學習計劃產生器網頁應用](./docs-mcp/README.md)

此案例展示如何使用 Chainlit 與 Model Context Protocol (MCP) 建構一款互動式網頁應用，為任一主題生成個人化學習計劃。使用者可指定主題（如「AI-900 認證」）和學習時長（例如 8 週），應用程式會提供逐週的推薦內容。Chainlit 提供對話式聊天介面，使體驗生動且可適應需求。

- 使用 Chainlit 推動的對話式網頁應用
- 使用者主導輸入主題及時長
- 透過 MCP 提供逐週內容建議
- 聊天介面中即時且可適應的回應

專案說明對話式 AI 與 MCP 如何結合，創造動態且用戶驅動的現代網頁教育工具。

### 5. [在 VS Code 中使用 MCP 伺服器直接查看文件](./docs-mcp/README.md)

本案例示範如何將 Microsoft Learn 文件直接引入 VS Code 環境，使用 MCP 伺服器—毋須切換瀏覽器分頁！你將看到如何：

- 利用 MCP 面板或命令面板即時搜尋並閱讀 VS Code 內文件
- 直接引用文件並將連結插入 README 或課程 Markdown 檔案
- 結合 GitHub Copilot 與 MCP，實現 AI 加持的文件與程式碼工作流
- 透過即時回饋與 Microsoft 資料來源提升文檔的驗證與品質
- 將 MCP 與 GitHub 工作流整合，實現持續文件驗證

實作內容包括：

- 範例 `.vscode/mcp.json` 配置，簡化設定流程
- 內置編輯器體驗的截圖導覽
- 結合 Copilot 與 MCP 的生產力技巧

此方案非常適合課程作者、文件編寫者及開發者，讓他們能在編輯器中專注於文件、Copilot 及驗證工具，這一切都由 MCP 支持。

### 6. [建立 APIM MCP 伺服器](./apimsample.md)

本案例提供逐步指南，說明如何使用 Azure API Management (APIM) 建立 MCP 伺服器。內容包括：

- 在 Azure API Management 設置 MCP 伺服器
- 將 API 操作作為 MCP 工具公開
- 配置流量限制與安全策略
- 使用 Visual Studio Code 與 GitHub Copilot 測試 MCP 伺服器

此範例說明如何利用 Azure 能力打造強大 MCP 伺服器，使其能用於多種應用，提升 AI 系統與企業 API 整合。

### 7. [GitHub MCP 註冊中心 — 加速智能代理整合](https://github.com/mcp)

本案例探討 GitHub MCP 註冊中心於 2025 年 9 月推出，如何解決 AI 生態系中的一大難題：MCP 伺服器的分散發現與部署。

#### 概覽
**MCP 註冊中心** 解決了過去 MCP 伺服器散落在多個倉庫和註冊庫，導致整合緩慢且易出錯的痛點。這些伺服器使得 AI 代理能與外部系統如 API、資料庫和文檔源互動。

#### 問題陳述
構建代理工作流的開發者面臨多項挑戰：
- **MCP 伺服器於不同平台間發現困難**
- <strong>論壇與文檔中零散的重複設定問題</strong>
- <strong>來自未驗證與不信任來源的安全風險</strong>
- <strong>伺服器品質與相容性缺乏標準化</strong>

#### 解決方案架構
GitHub MCP 註冊中心集中管理受信任的 MCP 伺服器，核心特點：
- 透過 VS Code 一鍵安裝整合，簡化設定
- 根據星標、活躍度及社群驗證做降噪排序
- 直接整合 GitHub Copilot 與其他兼容 MCP 的工具
- 採用開放貢獻模式，允許社群與企業夥伴共同貢獻

#### 商業影響
註冊中心帶來明顯改善：
- 透過 Microsoft Learn MCP 伺服器等工具加速開發者上手，文件直接串流至代理
- 透過專業伺服器如 `github-mcp-server` 強化生產力，支援自然語言 GitHub 自動化（PR 建立、CI 重跑、程式碼掃描）
- 透過策劃清單和透明配置標準提升生態系信任

#### 策略價值
對專注代理生命週期管理和可重現工作流程的從業者，MCP 註冊中心提供：
- 具標準化元件的模組化代理部署能力
- 具註冊中心支持的評估管線，實現一致測試與驗證
- 跨工具互通，促進不同 AI 平台間無縫整合

本案例說明 MCP 註冊中心不僅是目錄，更是實現可擴展、真實世界模型整合和代理系統部署的基石平台。

### 8. [代理發布至社交網絡](./publora-social-publishing.md)

本案例示範一個 **可寫遠端 MCP 伺服器**—其工具可代表使用者執行不可逆動作—以社交發布為示例。代理起草貼文，使用者核准，伺服器再於各社交網絡排程發佈。

設計上的挑戰是這種發布對伺服器施加的限制，且此限制適用於所有寫入而非僅讀的伺服器：

- **公開發現，需授權執行** — `tools/list` 無需憑證即可回應，方便註冊表與客戶端檢視；但所有 `tools/call` 需認證，否則回傳帶有 `WWW-Authenticate` 標頭的 `401`
- **無需離線流程的 OAuth 註冊** — 現行為動態客戶端註冊，`2026-07-28` 規範未來將導向客戶端 ID 元資料文件
- <strong>工具標註</strong>（`readOnlyHint`、`destructiveHint`、`idempotentHint`），供客戶端決定確定操作—為提示非強制，且連接器目錄審核現在期望含此屬性
- <strong>無法憑空編造的識別碼</strong>，使幻覺值大聲失敗，避免對貌似合理的值執行
- <strong>貼文創建工具中的冪等鍵</strong>，確保代理執行時重試不會造成重複貼文
- <strong>工具架構中描述的空操作目標</strong>，用以完整測試寫入流程且不發布任何內容，供審核者和 CI 使用

本章節最後提供一份可用於正在建立伺服器的簡短檢查清單。

## 結論

這八個完整的案例研究展示了模型上下文協議在多樣真實世界場景中的卓越彈性與實用應用。從複雜的多代理旅遊規劃系統與企業 API 管理，到簡化文檔工作流程與劃時代的 GitHub MCP 註冊中心，這些範例展現 MCP 如何標準化、可擴展地連結 AI 系統與所需工具、資料和服務，創造卓越價值。

案例涵蓋 MCP 實作的多個面向：
- <strong>企業整合</strong>：Azure API Management 與 Azure DevOps 自動化
- <strong>多代理協調</strong>：協調的 AI 代理旅遊規劃
- <strong>開發者生產力</strong>：VS Code 整合與即時文檔存取
- <strong>生態系發展</strong>：GitHub MCP 註冊中心為基礎平台
- <strong>教育應用</strong>：互動式學習計劃產生器及對話介面

透過研讀這些實作，你將獲得關鍵洞察：
- 不同規模與使用案例的架構模式
- 功能與可維護性平衡的實施策略
- 生產部署的安全與可擴展性考量
- MCP 伺服器開發與客戶端整合的最佳實踐
- 建設相互連結 AI 聯動解決方案的生態系思維

這些範例共同示範 MCP 不僅僅是理論架構，更是成熟、可投入生產的協議，推動解決複雜商業挑戰的實用方案。無論你是打造簡單自動化工具或複雜的多代理系統，這裡呈現的模式與方法都提供了你 MCP 專案的堅實基礎。

## 附加資源

- [Azure AI 旅遊代理 GitHub 倉庫](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP 工具](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP 工具](https://github.com/microsoft/playwright-mcp)
- [Microsoft 文件 MCP 伺服器](https://github.com/MicrosoftDocs/mcp)
- [GitHub MCP 註冊中心 — 加速智能代理整合](https://github.com/mcp)
- [MCP 社群範例](https://github.com/microsoft/mcp)

## 後續安排

- 上一章節：[第 8 模組：最佳實踐](../08-BestPractices/README.md)
- 下一章節：[第 10 模組：簡化 AI 工作流程：使用 AI 工具包建立 MCP 伺服器](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
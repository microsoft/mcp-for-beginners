# MCP 實踐：真實案例研究

[![MCP 實踐：真實案例研究](../../../translated_images/zh-TW/10.3262cc80b4de5071fde8ba74c5c5d6738a0a9f398dcc0423f0210f632e2238b8.png)](https://youtu.be/IxshWb2Az5w)

_（點擊上方圖片觀看本課程的影片）_

模型上下文協議（MCP）正在改變 AI 應用程式與數據、工具和服務互動的方式。本節展示了多個真實案例，說明 MCP 在各種企業場景中的實際應用。

## 概述

本節展示了 MCP 實施的具體例子，突顯了各組織如何利用此協議解決複雜的業務挑戰。透過研究這些案例，您將深入了解 MCP 在真實場景中的多功能性、可擴展性以及實際效益。

## 主要學習目標

透過探索這些案例，您將能夠：

- 理解 MCP 如何應用於解決特定業務問題
- 學習不同的整合模式和架構方法
- 掌握在企業環境中實施 MCP 的最佳實踐
- 獲得在真實實施中遇到的挑戰和解決方案的洞察
- 發掘在自己的項目中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅行代理 – 參考實現](./travelagentsample.md)

此案例研究探討了微軟的全面參考解決方案，展示如何使用 MCP、Azure OpenAI 和 Azure AI Search 建立多代理、AI 驅動的旅行規劃應用程式。該項目展示了：

- 透過 MCP 進行多代理協調
- 與 Azure AI Search 整合企業數據
- 使用 Azure 服務構建安全、可擴展的架構
- 可擴展的工具，包含可重用的 MCP 元件
- 由 Azure OpenAI 驅動的對話式用戶體驗

架構和實施細節提供了構建複雜多代理系統的寶貴見解，MCP 作為協調層發揮了重要作用。

### 2. [從 YouTube 數據更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

此案例研究展示了 MCP 在自動化工作流程中的實際應用。它說明了如何使用 MCP 工具：

- 從線上平台（如 YouTube）提取數據
- 更新 Azure DevOps 系統中的工作項目
- 創建可重複的自動化工作流程
- 整合分散系統中的數據

此例子說明了即使是相對簡單的 MCP 實施，也能透過自動化例行任務和改善系統間數據一致性帶來顯著的效率提升。

### 3. [使用 MCP 實現即時文件檢索](./docs-mcp/README.md)

此案例研究指導您如何連接 Python 控制台客戶端到 MCP 伺服器，以檢索並記錄即時、上下文感知的微軟文件。您將學習：

- 使用 Python 客戶端和官方 MCP SDK 連接 MCP 伺服器
- 使用流式 HTTP 客戶端進行高效的即時數據檢索
- 呼叫伺服器上的文件工具並直接將響應記錄到控制台
- 將最新的微軟文件整合到您的工作流程中，而無需離開終端

本章節包含一個動手作業、最小可行代碼範例，以及深入學習的額外資源連結。查看完整的操作指南和代碼，了解 MCP 如何改變文件訪問和開發者生產力。

### 4. [使用 MCP 建立互動式學習計劃生成器網頁應用](./docs-mcp/README.md)

此案例研究展示如何使用 Chainlit 和 MCP 建立一個互動式網頁應用，生成針對任何主題的個性化學習計劃。用戶可以指定主題（例如 "AI-900 認證"）和學習時長（例如 8 週），應用程式將提供逐週的推薦內容。Chainlit 提供了對話式聊天介面，使體驗更具吸引力和適應性。

- 由 Chainlit 驅動的對話式網頁應用
- 用戶主導的提示輸入主題和時長
- 使用 MCP 提供逐週的內容推薦
- 在聊天介面中即時生成適應性響應

此項目展示了如何將對話式 AI 和 MCP 結合，創建現代網頁環境中的動態、用戶驅動的教育工具。

### 5. [在 VS Code 中使用 MCP 伺服器實現文件檢索](./docs-mcp/README.md)

此案例研究展示如何將 Microsoft Learn 文件直接引入 VS Code 環境中，無需切換瀏覽器標籤！您將看到如何：

- 使用 MCP 面板或命令面板在 VS Code 中即時搜索和閱讀文件
- 參考文件並直接將連結插入 README 或課程 Markdown 文件
- 將 GitHub Copilot 和 MCP 結合，實現無縫的 AI 驅動文件和代碼工作流程
- 使用即時反饋和微軟提供的準確性驗證和增強您的文件
- 將 MCP 與 GitHub 工作流程整合，實現持續文件驗證

實施內容包括：

- 示例 `.vscode/mcp.json` 配置，便於快速設置
- 基於截圖的操作指南，展示編輯器內的使用體驗
- 結合 Copilot 和 MCP 的技巧，最大化生產力

此場景非常適合課程作者、文件撰寫者和開發者，幫助他們在編輯器中專注於文件、Copilot 和驗證工具的工作，所有這些都由 MCP 驅動。

### 6. [使用 Azure API Management 建立 MCP 伺服器](./apimsample.md)

此案例研究提供了逐步指南，教您如何使用 Azure API Management 建立 MCP 伺服器。內容涵蓋：

- 在 Azure API Management 中設置 MCP 伺服器
- 將 API 操作公開為 MCP 工具
- 配置速率限制和安全性策略
- 使用 Visual Studio Code 和 GitHub Copilot 測試 MCP 伺服器

此例子說明如何利用 Azure 的功能建立一個強大的 MCP 伺服器，可用於各種應用，增強 AI 系統與企業 API 的整合。

### 7. [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)

此案例研究探討 GitHub 的 MCP Registry（於 2025 年 9 月推出）如何解決 AI 生態系統中的一個關鍵挑戰：分散的 MCP 伺服器發現和部署。

#### 概述
**MCP Registry** 解決了分散的 MCP 伺服器在不同存儲庫和註冊表中難以發現的問題，這曾導致整合速度慢且容易出錯。這些伺服器使 AI 代理能與外部系統（如 API、數據庫和文件來源）互動。

#### 問題陳述
開發者在構建代理工作流程時面臨多項挑戰：
- **發現性差**：MCP 伺服器分散於不同平台
- **重複設置問題**：分散於論壇和文件中
- **安全風險**：來自未驗證和不可信來源
- **缺乏標準化**：伺服器質量和兼容性不一致

#### 解決方案架構
GitHub 的 MCP Registry 集中管理可信的 MCP 伺服器，具備以下關鍵功能：
- **一鍵安裝**：透過 VS Code 簡化設置
- **信號優於噪音排序**：根據星級、活動和社群驗證進行排序
- **直接整合**：與 GitHub Copilot 和其他 MCP 兼容工具無縫連接
- **開放貢獻模式**：允許社群和企業合作夥伴共同貢獻

#### 業務影響
註冊表帶來了可衡量的改進：
- **更快的上手**：例如使用 Microsoft Learn MCP Server，直接將官方文件流式傳輸到代理
- **提高生產力**：透過專用伺服器（如 `github-mcp-server`），實現自然語言的 GitHub 自動化（PR 創建、CI 重跑、代碼掃描）
- **更強的生態系統信任**：透過精選列表和透明的配置標準

#### 戰略價值
對於專注於代理生命周期管理和可重現工作流程的從業者，MCP Registry 提供：
- **模組化代理部署**：具備標準化元件
- **註冊表支持的評估管道**：實現一致的測試和驗證
- **跨工具互操作性**：在不同 AI 平台間無縫整合

此案例研究展示 MCP Registry 不僅僅是一個目錄，而是一個可擴展的基礎平台，用於真實世界模型整合和代理系統部署。

## 結論

這七個全面的案例研究展示了模型上下文協議在多樣化真實場景中的非凡多功能性和實際應用。從複雜的多代理旅行規劃系統和企業 API 管理，到簡化的文件工作流程和革命性的 GitHub MCP Registry，這些例子展示了 MCP 如何提供標準化、可擴展的方式，將 AI 系統與所需的工具、數據和服務連接起來，從而創造卓越價值。

案例研究涵蓋 MCP 實施的多個維度：
- **企業整合**：Azure API Management 和 Azure DevOps 自動化
- **多代理協調**：透過協作 AI 代理進行旅行規劃
- **開發者生產力**：VS Code 整合和即時文件訪問
- **生態系統發展**：GitHub 的 MCP Registry 作為基礎平台
- **教育應用**：互動式學習計劃生成器和對話式介面

透過研究這些實施，您將獲得關鍵洞察：
- **架構模式**：適用於不同規模和使用案例
- **實施策略**：在功能性和可維護性之間取得平衡
- **安全性和可擴展性**：針對生產部署的考量
- **最佳實踐**：MCP 伺服器開發和客戶端整合
- **生態系統思維**：構建互聯的 AI 驅動解決方案

這些例子共同證明 MCP 不僅僅是一個理論框架，而是一個成熟的、可投入生產的協議，能夠為複雜的業務挑戰提供實際解決方案。無論您是在構建簡單的自動化工具還是複雜的多代理系統，這些案例中展示的模式和方法都為您的 MCP 項目提供了堅實的基礎。

## 附加資源

- [Azure AI 旅行代理 GitHub 存儲庫](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP 工具](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP 工具](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [GitHub MCP Registry — 加速代理整合](https://github.com/mcp)
- [MCP 社群範例](https://github.com/microsoft/mcp)

下一步：實作實驗 [簡化 AI 工作流程：使用 AI 工具包構建 MCP 伺服器](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

---


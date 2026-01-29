# Scenario 3: 在 VS Code 編輯器內使用 MCP 伺服器查看文件

## 概覽

在此情境中，您將學習如何透過 MCP 伺服器，將 Microsoft Learn 文件直接帶入 Visual Studio Code 環境。您不必再頻繁切換瀏覽器分頁搜尋文件，而是能在編輯器內直接存取、搜尋並參考官方文件。這種方式能簡化工作流程，讓您保持專注，並能與 GitHub Copilot 等工具無縫整合。

- 在 VS Code 內搜尋並閱讀文件，無需離開編碼環境。
- 直接在 README 或課程檔案中引用文件並插入連結。
- 結合 GitHub Copilot 與 MCP，打造流暢的 AI 助力文件工作流程。

## 學習目標

完成本章後，您將了解如何在 VS Code 中設定並使用 MCP 伺服器，提升文件與開發工作流程。您將能夠：

- 配置工作區以使用 MCP 伺服器進行文件查詢。
- 在 VS Code 內直接搜尋並插入文件內容。
- 結合 GitHub Copilot 與 MCP 的力量，打造更高效的 AI 輔助工作流程。

這些技能將幫助您保持專注、提升文件品質，並增強作為開發者或技術寫作者的生產力。

## 解決方案

為了實現編輯器內的文件存取，您將依序完成一系列步驟，將 MCP 伺服器與 VS Code 及 GitHub Copilot 整合。此方案非常適合課程作者、文件撰寫者及開發者，讓您在編輯器中專注工作，同時使用文件與 Copilot。

- 在撰寫課程或專案文件時，快速新增 README 的參考連結。
- 使用 Copilot 產生程式碼，並利用 MCP 即時查找及引用相關文件。
- 保持在編輯器內專注，提高工作效率。

### 逐步指南

開始前，請依照以下步驟操作。每個步驟都可以搭配資源資料夾中的截圖，幫助視覺說明流程。

1. **新增 MCP 設定：**  
   在專案根目錄下建立 `.vscode/mcp.json` 檔案，並加入以下設定：  
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```  
   此設定告訴 VS Code 如何連接到 [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp)。

   ![Step 1: Add mcp.json to .vscode folder](../../../../../../translated_images/zh-TW/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.png)
    
2. **開啟 GitHub Copilot Chat 面板：**  
   如果尚未安裝 GitHub Copilot 擴充功能，請前往 VS Code 的擴充功能檢視並安裝。您也可以直接從 [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) 下載。接著，從側邊欄開啟 Copilot Chat 面板。

   ![Step 2: Open Copilot Chat panel](../../../../../../translated_images/zh-TW/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.png)

3. **啟用代理模式並確認工具：**  
   在 Copilot Chat 面板中，啟用代理模式。

   ![Step 3: Enable agent mode and verify tools](../../../../../../translated_images/zh-TW/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.png)

   啟用後，確認 MCP 伺服器已列為可用工具之一。這確保 Copilot 代理能存取文件伺服器，取得相關資訊。

   ![Step 3: Verify MCP server tool](../../../../../../translated_images/zh-TW/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.png)

4. **開始新對話並向代理提問：**  
   在 Copilot Chat 面板開啟新對話，您現在可以向代理提出文件相關問題。代理會使用 MCP 伺服器，直接在編輯器中擷取並顯示相關 Microsoft Learn 文件。

   - *「我正在為主題 X 撰寫學習計畫，計畫為期 8 週，請建議每週應學習的內容。」*

   ![Step 4: Prompt the agent in chat](../../../../../../translated_images/zh-TW/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

5. **即時查詢：**

   > 以下為 Azure AI Foundry Discord [#get-help](https://discord.gg/D6cRhjHWSC) 頻道中的即時查詢範例（[查看原始訊息](https://discord.com/channels/1113626258182504448/1385498306720829572)）：
   
   *「我想了解如何部署多代理解決方案，這些 AI 代理是在 Azure AI Foundry 上開發的。我發現沒有像 Copilot Studio 頻道那樣的直接部署方式。那麼，企業用戶要如何部署，才能互動並完成工作？  
   有許多文章或部落格提到可以使用 Azure Bot 服務作為 MS Teams 與 Azure AI Foundry 代理之間的橋樑。如果我設定一個 Azure Bot，透過 Azure Function 連接到 Azure AI Foundry 的 Orchestrator Agent 來執行協調，這樣可行嗎？還是我需要為多代理解決方案中的每個 AI 代理建立 Azure Function，在 Bot Framework 端進行協調？其他建議也非常歡迎。」*

   ![Step 5: Live queries](../../../../../../translated_images/zh-TW/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.png)

   代理會回應相關文件連結與摘要，您可以直接插入到 Markdown 檔案中，或作為程式碼中的參考。

### 範例查詢

以下是一些您可以嘗試的範例查詢，展示 MCP 伺服器與 Copilot 如何協同工作，提供即時且具上下文的文件與參考，無需離開 VS Code：

- 「示範如何使用 Azure Functions 觸發器。」
- 「插入 Azure Key Vault 官方文件的連結。」
- 「Azure 資源安全的最佳實踐有哪些？」
- 「尋找 Azure AI 服務的快速入門指南。」

這些查詢將展示 MCP 伺服器與 Copilot 如何協同，提供即時且具上下文的文件與參考，讓您無需離開 VS Code。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
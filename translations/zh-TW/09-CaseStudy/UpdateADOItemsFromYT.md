# 案例研究：使用 MCP 從 YouTube 資料更新 Azure DevOps 項目

> **Disclaimer:** 市面上已有工具和報告能自動化將 YouTube 等平台的資料更新至 Azure DevOps 項目。以下情境僅作為示範，說明如何運用 MCP 工具進行自動化與整合。

## 概述

本案例展示如何利用 Model Context Protocol (MCP) 及其工具，自動化將線上平台（如 YouTube）上的資訊更新至 Azure DevOps (ADO) 工作項目。此情境僅為這些工具廣泛應用能力的一個範例，能靈活調整以符合其他類似的自動化需求。

在此範例中，一位 Advocate 使用 ADO 項目追蹤線上會議，每個項目包含 YouTube 影片的 URL。透過 MCP 工具，Advocate 能以可重複且自動化的方式，將最新的影片觀看次數等指標更新至 ADO 項目。此方法同樣適用於其他需要將線上資料整合至 ADO 或其他系統的情境。

## 情境說明

Advocate 負責追蹤線上會議及社群互動的影響力。每場會議皆以 ADO 工作項目記錄於 'DevRel' 專案中，且工作項目包含 YouTube 影片 URL 欄位。為了準確報告會議的觸及範圍，Advocate 需將當前的影片觀看數及資料擷取日期更新至 ADO 項目。

## 使用工具

- [Azure DevOps MCP](https://github.com/microsoft/azure-devops-mcp)：透過 MCP 程式化存取並更新 ADO 工作項目。
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)：自動化瀏覽器操作，擷取網頁（如 YouTube 影片統計資料）上的即時數據。

## 逐步工作流程

1. **識別 ADO 項目**：從 'DevRel' 專案中取得 ADO 工作項目 ID（例如 1234）。
2. **擷取 YouTube URL**：使用 Azure DevOps MCP 工具從該工作項目取得 YouTube 影片 URL。
3. **擷取影片觀看數**：利用 Playwright MCP 工具前往該 YouTube URL，擷取目前的觀看次數。
4. **更新 ADO 項目**：使用 Azure DevOps MCP 工具，將最新觀看數及擷取日期寫入 ADO 工作項目的「Impact and Learnings」區塊。

## 範例提示

```bash
- Work with the ADO Item ID: 1234
- The project is '2025-Awesome'
- Get the YouTube URL for the ADO item
- Use Playwright to get the current views from the YouTube video
- Update the ADO item with the current video views and the updated date of the information
```

## Mermaid 流程圖

```mermaid
flowchart TD
    A[Start: Advocate identifies ADO Item ID] --> B[Get YouTube URL from ADO Item using Azure DevOps MCP]
    B --> C[Extract current video views using Playwright MCP]
    C --> D[Update ADO Item's Impact and Learnings section with view count and date]
    D --> E[End]
```

## 技術實作

- **MCP 編排**：由 MCP 伺服器負責協調 Azure DevOps MCP 與 Playwright MCP 工具的使用。
- **自動化**：流程可手動觸發，或排程定期執行，確保 ADO 項目資料持續更新。
- **擴充性**：同樣模式可延伸至更新其他線上指標（如按讚數、留言數）或其他平台的資料。

## 成果與影響

- **效率提升**：自動擷取與更新影片指標，減少 Advocate 的手動工作量。
- **資料準確**：確保 ADO 項目反映最新的線上資料。
- **可重複使用**：提供可複製的工作流程，適用於其他資料來源或指標的類似情境。

## 參考資料

- [Azure DevOps MCP](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
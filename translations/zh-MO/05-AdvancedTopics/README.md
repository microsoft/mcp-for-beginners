# MCP 高級主題

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/zh-MO/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(點擊上方圖片觀看本課程影片)_

本章涵蓋模型上下文協議（MCP）實作中的一系列高級主題，包括多模態整合、可擴展性、安全最佳實踐與企業整合。這些主題對於構建健壯且可投入生產的 MCP 應用程式，以滿足現代 AI 系統的需求至關重要。

## 概述

本課程探討模型上下文協議實作中的高級概念，專注於多模態整合、可擴展性、安全最佳實踐以及企業整合。這些主題對於打造能夠應對企業環境中複雜需求的生產級 MCP 應用程式至關重要。

## 學習目標

課程結束時，您將能夠：

- 在 MCP 框架中實作多模態能力
- 為高需求場景設計可擴展的 MCP 架構
- 應用符合 MCP 安全原則的安全最佳實踐
- 將 MCP 與企業 AI 系統及框架整合
- 在生產環境中優化效能及可靠性

## 課程與範例專案

| 連結 | 標題 | 說明 |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | 與 Azure 整合 | 學習如何將 MCP 伺服器整合到 Azure 上 |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP 多模態範例 | 音訊、影像與多模態回應的範例 |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 示範 | 簡易 Spring Boot 應用展示 MCP 的 OAuth2，包含授權與資源伺服器。展示安全的令牌發行、受保護端點、Azure Container Apps 部署以及 API 管理整合。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | 根上下文 | 深入了解根上下文及其實作方式 |
| [5.5 Routing](./mcp-routing/README.md) | 路由 | 學習各種類型的路由 |
| [5.6 Sampling](./mcp-sampling/README.md) | 取樣 | 學習如何操作取樣 |
| [5.7 Scaling](./mcp-scaling/README.md) | 擴展 | 了解擴展相關知識 |
| [5.8 Security](./mcp-security/README.md) | 安全性 | 保護您的 MCP 伺服器 |
| [5.9 Web Search sample](./web-search-mcp/README.md) | 網頁搜尋 MCP | Python MCP 伺服器與客戶端整合 SerpAPI 支援即時網頁、新聞、商品搜尋及問答。展示多工具協作、外部 API 整合及強健錯誤處理。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | 串流 | 即時資料串流已成為現今數據驅動世界的必要，企業與應用需要即時資訊以做出及時決策。 |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | 網頁即時搜尋 | MCP 如何透過提供跨 AI 模型、搜尋引擎及應用的標準化上下文管理，改變即時網頁搜尋。 | 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID 認證 | Microsoft Entra ID 提供強大的雲端身份與存取管理方案，確保只有授權的使用者與應用能與您的 MCP 伺服器互動。 |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry 整合 | 學習如何將 Model Context Protocol 伺服器與 Azure AI Foundry 代理整合，啟用強大的工具協作及企業 AI 能力，搭配標準化外部資料來源連接。 |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | 上下文工程 | MCP 伺服器上下文工程技術的未來機會，包括上下文優化、動態上下文管理及 MCP 框架內有效提示工程的策略。 |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | 自訂傳輸 | 學習如何為特殊 MCP 通訊情境實作自訂傳輸機制。 |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | 協定功能深入探討 | 精通進階協定功能，包含進度通知、請求取消、資源範本及錯誤處理模式。 |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 對抗性多代理推理 | 使用兩個立場相反的代理，共享單一 MCP 工具組，透過結構化辯論捕捉幻覺、揭露邊緣案例，並產出更精確校準的結果。 |

> **MCP 規範 2025-11-25 新增**：規範現在實驗性支援 <strong>任務</strong>（具進度追蹤的長時間運作）、<strong>工具註解</strong>（關於工具行為的安全性元資料）、**URL 模式引導**（請求客戶端提供特定 URL 內容）以及強化的 <strong>根</strong>（用於工作區上下文管理）。詳情請參閱 [MCP 規範變更日誌](https://spec.modelcontextprotocol.io/)。

## 額外參考資料

想取得最新的高級 MCP 主題資訊，請參考：
- [MCP 文件](https://modelcontextprotocol.io/)
- [MCP 規範 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub 倉庫](https://github.com/modelcontextprotocol)
- [OWASP MCP 十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - 安全風險及緩解措施
- [MCP 安全峰會工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/) - 實作安全訓練課程

## 主要重點

- 多模態 MCP 實作拓展 AI 能力，超越文本處理
- 可擴展性對企業部署至關重要，可透過水平與垂直擴展解決
- 全面安全措施保護資料並確保正確的存取控制
- 與 Azure OpenAI、Microsoft AI Foundry 等平台的企業整合強化 MCP 功能
- 高級 MCP 實作受益於優化架構與謹慎資源管理

## 練習

為特定應用場景設計企業級 MCP 實作：

1. 確認您的用例所需的多模態需求
2. 概述保護敏感資料所需的安全控管
3. 設計可應對不同負載的可擴展架構
4. 規劃與企業 AI 系統的整合點
5. 記錄潛在效能瓶頸及緩解策略

## 額外資源

- [Azure OpenAI 文件](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry 文件](https://learn.microsoft.com/en-us/ai-services/)

---

## 接下來

開始探索本模組的課程： [5.1 MCP Integration](./mcp-integration/README.md)

完成本模組後，繼續至： [模組 6：社群貢獻](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
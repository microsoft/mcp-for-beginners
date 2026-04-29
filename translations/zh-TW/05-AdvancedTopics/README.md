# MCP 高級主題

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/zh-TW/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(點擊上方圖片觀看本課程影片)_

本章涵蓋模型上下文協議（MCP）實作的多項高級主題，包括多模態整合、可擴展性、安全最佳實務及企業整合。這些主題對建立強健且適合生產環境的 MCP 應用程式至關重要，能符合現代 AI 系統的需求。

## 概述

本課程探討模型上下文協議實作中的高級概念，重點在多模態整合、可擴展性、安全最佳實務及企業整合。這些主題是建構能處理複雜企業需求的生產級 MCP 應用程式的關鍵。

## 學習目標

完成本課程後，您將能夠：

- 在 MCP 框架中實作多模態功能
- 設計適用於高需求場景的可擴展 MCP 架構
- 採用符合 MCP 安全原則的安全最佳實務
- 將 MCP 整合到企業 AI 系統及框架中
- 優化生產環境中的效能與可靠性

## 課程與範例專案

| 連結 | 標題 | 說明 |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | 與 Azure 整合 | 學習如何在 Azure 上整合您的 MCP 伺服器 |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP 多模態範例 | 音訊、影像與多模態回應範例 |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 範例 | 簡易 Spring Boot 應用展示 MCP OAuth2 作為授權與資源伺服器。示範安全令牌發行、受保護端點、Azure Container Apps 部署及 API 管理整合。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | 根上下文 | 進一步了解根上下文及其實作方法 |
| [5.5 Routing](./mcp-routing/README.md) | 路由 | 了解不同類型的路由 |
| [5.6 Sampling](./mcp-sampling/README.md) | 取樣 | 學習如何使用取樣 |
| [5.7 Scaling](./mcp-scaling/README.md) | 擴展 | 關於擴展的內容 |
| [5.8 Security](./mcp-security/README.md) | 安全 | 保護您的 MCP 伺服器安全 |
| [5.9 Web Search sample](./web-search-mcp/README.md) | 網路搜尋 MCP | Python MCP 伺服器與客戶端整合 SerpAPI，實現即時網路、新聞、商品搜尋與問答。示範多工具協同、外部 API 整合與健全錯誤處理。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | 串流 | 即時資料串流已成為當今資料驅動世界的重要需求，企業與應用需即時取得資訊以做出迅速決策。 |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | 網路即時搜尋 | MCP 如何透過標準化的上下文管理方式改變模型、搜尋引擎與應用間的即時網路搜尋。 |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID 認證 | Microsoft Entra ID 提供強大雲端身分與存取管理解決方案，確保僅有被授權的使用者與應用能存取您的 MCP 伺服器。 |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry 整合 | 學習如何將模型上下文協議伺服器與 Azure AI Foundry 代理整合，實現強大工具協同與企業 AI 能力，並標準化外部資料來源連接。 |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | 上下文工程 | MCP 伺服器上下文工程技術的未來機會，包括上下文優化、動態上下文管理與 MCP 框架中有效提示工程策略。 |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | 自訂傳輸 | 學習如何為特殊 MCP 通訊情境實作自訂傳輸機制。 |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | 協議功能 | 精通進階協議功能包括進度通知、請求取消、資源範本與錯誤處理模式。 |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 對抗性多智能體 | 使用立場對立的兩個智能體，共用同一 MCP 工具集，藉由結構化辯論捕捉幻覺、揭露邊緣案例，並產出更精確的輸出。 |

> **MCP 規範 2025-11-25 新增**：規範現包含實驗性支援 <strong>任務</strong>（具有進度追蹤的長時間操作）、<strong>工具註解</strong>（工具行為元資料以增強安全）、**URL 模式引導**（向客戶端請求特定 URL 內容）及強化 <strong>根</strong>（用於工作區上下文管理）。完整細節請參閱 [MCP 規範變更日誌](https://spec.modelcontextprotocol.io/)。

## 附加參考資料

欲取得 MCP 高級主題的最新資訊，請參考：
- [MCP 文件](https://modelcontextprotocol.io/)
- [MCP 規範 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub 倉庫](https://github.com/modelcontextprotocol)
- [OWASP MCP 十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - 安全風險與緩解措施
- [MCP 安全峰會工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/) - 實務安全訓練

## 重點摘要

- 多模態 MCP 實作超越純文字處理，擴展 AI 能力
- 可擴展性對企業部署至關重要，可透過水平與垂直擴展來實現
- 全面安全措施保護資料並確保正確存取控管
- 與 Azure OpenAI 和 Microsoft AI Foundry 等平台的企業整合增強 MCP 功能
- 高級 MCP 實作受益於優化架構與謹慎的資源管理

## 練習

為特定使用案例設計企業級 MCP 實作：

1. 確認使用案例的多模態需求
2. 制定保護敏感資料所需的安全控管
3. 設計能處理不同負載的可擴展架構
4. 規劃與企業 AI 系統的整合點
5. 記錄潛在效能瓶頸與緩解策略

## 額外資源

- [Azure OpenAI 文件](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry 文件](https://learn.microsoft.com/en-us/ai-services/)

---

## 下一步

從本模組的課程開始探索: [5.1 MCP Integration](./mcp-integration/README.md)

完成本模組後，請繼續進入: [模組 6：社群貢獻](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。本公司對於因使用此翻譯而產生的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
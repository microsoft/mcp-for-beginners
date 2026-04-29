# MCP 高級主題

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/zh-HK/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(點擊上圖觀看本課程影片)_

本章涵蓋 Model Context Protocol (MCP) 實作中的一系列高級主題，包括多模態整合、可擴展性、安全最佳實踐及企業整合。這些主題對於構建能滿足現代 AI 系統需求的穩健且生產級 MCP 應用至關重要。

## 概覽

本課程探討 Model Context Protocol 實作中的高級概念，重點是多模態整合、可擴展性、安全最佳實踐及企業整合。這些主題對於構建能處理企業環境中複雜需求的生產級 MCP 應用非常重要。

## 學習目標

完成本課程後，您將能夠：

- 在 MCP 框架中實作多模態功能
- 設計應對高需求場景的可擴展 MCP 架構
- 應用符合 MCP 安全原則的安全最佳實踐
- 將 MCP 與企業 AI 系統及框架整合
- 優化生產環境中的效能及可靠性

## 課程與範例專案

| 連結 | 標題 | 說明 |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | 與 Azure 整合 | 學習如何在 Azure 上整合您的 MCP 伺服器 |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP 多模態範例 | 音訊、影像及多模態回應範例 |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 範例 | 最小化 Spring Boot 應用展示 MCP 的 OAuth2 作為授權及資源伺服器。示範安全令牌頒發、受保護端點、Azure Container Apps 部署及 API 管理整合。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | 根上下文 | 進一步了解根上下文及其實作方法 |
| [5.5 Routing](./mcp-routing/README.md) | 路由 | 學習不同類型的路由 |
| [5.6 Sampling](./mcp-sampling/README.md) | 抽樣 | 學習如何操作抽樣 |
| [5.7 Scaling](./mcp-scaling/README.md) | 擴展 | 了解擴展方法 |
| [5.8 Security](./mcp-security/README.md) | 安全 | 保護您的 MCP 伺服器安全 |
| [5.9 Web Search sample](./web-search-mcp/README.md) | 網絡搜尋 MCP | Python MCP 伺服器及客戶端結合 SerpAPI 用於即時網頁、新聞、產品搜尋及問答。示範多工具協同、外部 API 整合及強健錯誤處理。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | 串流 | 即時資料串流已成為當今數據驅動世界的關鍵，企業和應用需即時存取資訊以做出及時決策。 |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | 網絡即時搜尋 | MCP 如何透過在 AI 模型、搜尋引擎與應用間提供標準化上下文管理方式，轉變即時網絡搜尋。 | 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID 認證 | Microsoft Entra ID 提供強健的雲端身份和存取管理方案，助確保只有授權用戶及應用可與您的 MCP 伺服器互動。 |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry 整合 | 學習如何將 Model Context Protocol 伺服器與 Azure AI Foundry 代理整合，實現強大的工具協調及標準化外部資料源連接企業 AI 能力。 |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | 上下文工程 | MCP 伺服器上下文工程技巧未來機會，包括上下文優化、動態上下文管理，以及 MCP 框架中有效提示工程策略。 |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | 自訂傳輸 | 學習如何為特殊 MCP 通訊場景實作自訂傳輸機制。 |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | 協議特性 | 精通進階協議特性，包括進度通知、請求取消、資源模板及錯誤處理模式。 |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 對抗型代理 | 透過兩個持對立立場且共享單一 MCP 工具集的代理，捕捉幻覺、發現邊緣案例，並透過結構化辯論產出更佳校準輸出。 |

> **MCP 規範 2025-11-25 新增**：規範現已實驗性支援 <strong>任務</strong>（帶進度追蹤的長時間操作）、<strong>工具註釋</strong>（有關工具行為以保障安全的元資料）、**URL 模式引導**（要求客戶端提供特定 URL 內容）及強化的 <strong>根環境</strong>（用於工作區上下文管理）。詳情請參閱 [MCP 規範變更紀錄](https://spec.modelcontextprotocol.io/)。

## 額外參考資料

欲取得最新的 MCP 高階主題資訊，請參閱：
- [MCP 文件](https://modelcontextprotocol.io/)
- [MCP 規範 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub 儲存庫](https://github.com/modelcontextprotocol)
- [OWASP MCP 十大風險](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - 安全風險與緩解措施
- [MCP 安全峰會工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/) - 實務安全訓練

## 主要重點

- 多模態 MCP 實作將 AI 能力延伸至文字處理以外
- 可擴展性對企業部署至關重要，透過水平及垂直擴展來達成
- 全面性的安全措施保障資料與正確存取控制
- 與 Azure OpenAI 及 Microsoft AI Foundry 等平台的企業整合增強 MCP 能力
- 進階 MCP 實作受益於優化架構與謹慎的資源管理

## 練習

為特定用例設計企業級 MCP 實作：

1. 確認您的用例多模態需求
2. 概述保護敏感資料所需的安全控管
3. 設計能處理不同負載的可擴展架構
4. 規劃與企業 AI 系統的整合點
5. 記錄可能的效能瓶頸及緩解策略

## 額外資源

- [Azure OpenAI 文件](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry 文件](https://learn.microsoft.com/en-us/ai-services/)

---

## 下一步

從本模組的課程開始探索：[5.1 MCP 整合](./mcp-integration/README.md)

完成本模組後，繼續至：[模組 6：社群貢獻](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於提供準確翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
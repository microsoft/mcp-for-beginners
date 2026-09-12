# 🚀 MCP 伺服器與 PostgreSQL - 完整學習指南

## 🧠 MCP 數據庫整合學習路線概述

這份完整學習指南教你如何藉由實際的零售分析實作，搭建可用於生產的 **Model Context Protocol (MCP) 伺服器** 並與數據庫整合。你將學習企業級模式，包括 **列級安全 (RLS)**、<strong>語義搜尋</strong>、<strong>Azure AI 整合</strong>和<strong>多租戶數據存取</strong>。

無論你是後端開發工程師、AI 工程師或數據架構師，本指南均提供結構化學習，搭配實務範例和動手練習，帶你探索以下 MCP 伺服器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 資源

- 📘 [MCP 文件](https://modelcontextprotocol.io/) – 詳盡教程與使用指南
- 📜 [MCP 規格 (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – 協定架構與技術參考
- 🧑‍💻 [MCP GitHub 倉庫](https://github.com/modelcontextprotocol) – 開源 SDK、工具與程式範例
- 🌐 [MCP 社群](https://github.com/orgs/modelcontextprotocol/discussions) – 加入討論並參與社群貢獻
- 🔒 [OWASP MCP 十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – 安全最佳實踐與風險緩解


## 🧭 MCP 數據庫整合集學習路線

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 完整學習架構

| 實驗室 | 主題 | 說明 | 連結 |
|--------|-------|-------------|------|
| **實驗室 1-3：基礎篇** | | | |
| 00 | [MCP 數據庫整合簡介](./00-Introduction/README.md) | MCP 與數據庫整合概覽及零售分析案例 | [開始學習](./00-Introduction/README.md) |
| 01 | [核心架構概念](./01-Architecture/README.md) | 了解 MCP 伺服器架構、數據庫層與安全模式 | [學習](./01-Architecture/README.md) |
| 02 | [安全性與多租戶](./02-Security/README.md) | 列級安全、身份驗證與多租戶數據存取 | [學習](./02-Security/README.md) |
| 03 | [環境設置](./03-Setup/README.md) | 設置開發環境、Docker、Azure 資源 | [設定](./03-Setup/README.md) |
| **實驗室 4-6： MCP 伺服器構建** | | | |
| 04 | [數據庫設計與結構](./04-Database/README.md) | PostgreSQL 設置、零售模式設計與範例資料 | [構建](./04-Database/README.md) |
| 05 | [MCP 伺服器實作](./05-MCP-Server/README.md) | 構建具數據庫整合的 FastMCP 伺服器 | [構建](./05-MCP-Server/README.md) |
| 06 | [工具開發](./06-Tools/README.md) | 創建數據庫查詢工具與結構查詢功能 | [構建](./06-Tools/README.md) |
| **實驗室 7-9：進階功能** | | | |
| 07 | [語義搜尋整合](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 與 pgvector 實作向量嵌入 | [進階](./07-Semantic-Search/README.md) |
| 08 | [測試與除錯](./08-Testing/README.md) | 測試策略、除錯工具與驗證方法 | [測試](./08-Testing/README.md) |
| 09 | [VS Code 整合](./09-VS-Code/README.md) | 配置 VS Code MCP 整合與 AI 聊天功能 | [整合](./09-VS-Code/README.md) |
| **實驗室 10-12：生產與最佳實踐** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure 容器應用與擴展考量 | [部署](./10-Deployment/README.md) |
| 11 | [監控與可觀察性](./11-Monitoring/README.md) | Application Insights、記錄、效能監控 | [監控](./11-Monitoring/README.md) |
| 12 | [最佳實踐與優化](./12-Best-Practices/README.md) | 效能優化、安全加固與生產環境技巧 | [優化](./12-Best-Practices/README.md) |

### 💻 你將打造的系統

完成本學習路線後，你將建置一套完整的 **Zava 零售分析 MCP 伺服器**，特色包括：

- <strong>多表零售數據庫</strong> 包含顧客訂單、產品和庫存
- <strong>列級安全</strong> 用於門店基礎數據隔離
- <strong>語義商品搜尋</strong> 使用 Azure OpenAI 嵌入技術
- **VS Code AI 聊天整合** 支援自然語言查詢
- <strong>生產環境部署</strong> 使用 Docker 與 Azure
- <strong>完整監控系統</strong> 搭配 Application Insights

## 🎯 學習先決條件

為了充份利用此學習路線，你應具備：

- <strong>程式設計經驗</strong>：熟悉 Python（優先）或類似語言
- <strong>數據庫知識</strong>：基本 SQL 與關聯式數據庫認識
- **API 概念**：理解 REST API 與 HTTP 概念
- <strong>開發工具</strong>：熟悉命令列、Git 與程式編輯器
- <strong>雲端基礎</strong>：（可選）了解 Azure 或同類雲端平台
- **Docker 認識**：（可選）了解容器化概念

### 必備工具

- **Docker Desktop** - 用於執行 PostgreSQL 與 MCP 伺服器
- **Azure CLI** - 進行雲端資源部署
- **VS Code** - 用於開發與 MCP 整合
- **Git** - 版本控制
- **Python 3.8+** - MCP 伺服器開發

## 📚 學習指南與資源

此學習路線內含完整資源，協助你順利學習：

### 學習指南

每個實驗室包含：
- <strong>清晰學習目標</strong> - 你將達成什麼
- <strong>循序漸進指引</strong> - 詳細實作步驟
- <strong>程式碼範例</strong> - 可運作範例與說明
- <strong>練習題目</strong> - 動手實作機會
- <strong>故障排除指南</strong> - 常見問題及解決方案
- <strong>額外資源</strong> - 延伸閱讀與探究

### 先決條件檢查

每開始實驗前，你會找到：
- <strong>所需知識</strong> - 須預先了解的內容
- <strong>環境設定驗證</strong> - 如何確認環境就緒
- <strong>時間評估</strong> - 預期完成所需時間
- <strong>學習成果</strong> - 完成後你將會掌握

### 推薦學習路線

根據你的經驗程度選擇路線：

#### 🟢 <strong>初學者路線</strong>（新手 MCP）
1. 先完成 [MCP 入門](https://aka.ms/mcp-for-beginners) 0-10 單元
2. 完成 00-03 實驗室加強基礎
3. 跟隨 04-06 實驗室動手構建
4. 嘗試 07-09 實驗室實務應用

#### 🟡 <strong>中階路線</strong>（具部分 MCP 經驗）
1. 回顧 00-01 實驗室中的數據庫專題
2. 聚焦 02-06 實驗室的實作內容
3. 深入學習 07-12 實驗室的進階功能

#### 🔴 <strong>高階路線</strong>（有 MCP 經驗）
1. 瀏覽 00-03 實驗室取得背景知識
2. 專注於 04-09 實驗室的數據庫整合
3. 集中研究 10-12 實驗室的生產部署

## 🛠️ 如何有效利用此學習路線

### 依序學習（推薦）

按順序完成實驗室，建立全面認知：

1. <strong>閱讀概覽</strong> - 理解學習內容
2. <strong>檢查先決條件</strong> - 確認具備必要知識
3. <strong>跟隨步驟指引</strong> - 一邊學一邊實作
4. <strong>完成練習題</strong> - 鞏固所學
5. <strong>回顧重點</strong> - 牢固學習成果

### 針對性學習

若需特定技能：

- <strong>數據庫整合</strong>：聚焦 04-06 實驗室
- <strong>安全實作</strong>：專注於 02、08、12 實驗室
- **AI／語義搜尋**：深入研究 07 實驗室
- <strong>生產部署</strong>：學習 10-12 實驗室

### 動手練習

每個實驗室包含：
- <strong>可用程式碼範例</strong> - 複製、修改及實驗
- <strong>實務場景</strong> - 實際零售分析案例
- <strong>循序漸進複雜度</strong> - 由簡入繁構建
- <strong>驗證步驟</strong> - 確認實作正確

## 🌟 社群與支援

### 獲取幫助

- **Azure AI Discord**：[加入獲取專家支援](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 倉庫與實作範例**：[部署範例與資源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社群**：[加入更廣泛 MCP 討論](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 準備好開始了嗎？

立即展開你的旅程，從 **[實驗室 00：MCP 數據庫整合簡介](./00-Introduction/README.md)** 開始

---

*通過這個全面且實作導向的學習體驗，掌握生產級 MCP 伺服器與數據庫整合的架構建置。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
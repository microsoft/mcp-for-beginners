# 🚀 MCP 伺服器與 PostgreSQL - 完整學習指南

## 🧠 MCP 資料庫整合學習路徑概述

本全面學習指南將教您如何透過實務零售分析案例建置可投入生產的 **Model Context Protocol (MCP) 伺服器** 並與資料庫整合。您將學習企業級架構模式，包括 **列級安全 (Row Level Security, RLS)**、<strong>語意搜尋</strong>、**Azure AI 整合**，以及 <strong>多租戶資料存取</strong>。

無論您是後端開發人員、AI 工程師或資料架構師，本指南提供有結構的學習，並搭配實際範例與動手練習，引導您完成以下 MCP 伺服器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 資源

- 📘 [MCP 文件](https://modelcontextprotocol.io/) – 詳細教學與用戶指南
- 📜 [MCP 規格 (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – 協定架構與技術參考
- 🧑‍💻 [MCP GitHub 倉庫](https://github.com/modelcontextprotocol) – 開源 SDK、工具與程式碼範例
- 🌐 [MCP 社群](https://github.com/orgs/modelcontextprotocol/discussions) – 參與討論並貢獻社群
- 🔒 [OWASP MCP 十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – 安全最佳實務與風險緩解


## 🧭 MCP 資料庫整合學習路徑

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 完整學習架構

| 實驗室 | 主題 | 說明 | 連結 |
|--------|-------|-------------|------|
| **實驗室 1-3：基礎篇** | | | |
| 00 | [MCP 資料庫整合簡介](./00-Introduction/README.md) | MCP 與資料庫整合及零售分析案例概述 | [從此開始](./00-Introduction/README.md) |
| 01 | [核心架構觀念](./01-Architecture/README.md) | 理解 MCP 伺服器架構、資料庫層和安全模式 | [學習](./01-Architecture/README.md) |
| 02 | [安全性與多租戶](./02-Security/README.md) | 列級安全、驗證與多租戶資料存取 | [學習](./02-Security/README.md) |
| 03 | [環境設定](./03-Setup/README.md) | 設定開發環境、Docker 及 Azure 資源 | [設定](./03-Setup/README.md) |
| **實驗室 4-6：建置 MCP 伺服器** | | | |
| 04 | [資料庫設計與結構](./04-Database/README.md) | PostgreSQL 設定、零售資料結構設計與範例資料 | [建置](./04-Database/README.md) |
| 05 | [MCP 伺服器實作](./05-MCP-Server/README.md) | 以資料庫整合構建 FastMCP 伺服器 | [建置](./05-MCP-Server/README.md) |
| 06 | [工具開發](./06-Tools/README.md) | 建置資料庫查詢工具與結構檢視 | [建置](./06-Tools/README.md) |
| **實驗室 7-9：進階功能** | | | |
| 07 | [語意搜尋整合](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 與 pgvector 實作向量嵌入 | [進階](./07-Semantic-Search/README.md) |
| 08 | [測試與除錯](./08-Testing/README.md) | 測試策略、除錯工具與驗證方法 | [測試](./08-Testing/README.md) |
| 09 | [VS Code 整合](./09-VS-Code/README.md) | 設定 VS Code MCP 整合與 AI 聊天使用 | [整合](./09-VS-Code/README.md) |
| **實驗室 10-12：生產與最佳實務** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure Container Apps 與擴充考量 | [部署](./10-Deployment/README.md) |
| 11 | [監控與可觀察性](./11-Monitoring/README.md) | Application Insights、日誌記錄與效能監控 | [監控](./11-Monitoring/README.md) |
| 12 | [最佳實務與優化](./12-Best-Practices/README.md) | 效能優化、安全強化與生產環境建議 | [優化](./12-Best-Practices/README.md) |

### 💻 您將建置的內容

完成本學習路徑後，您將完成一個完整的 **Zava 零售分析 MCP 伺服器**，具備：

- <strong>多表零售資料庫</strong>，包含客戶訂單、產品與庫存
- <strong>基於店舖的列級安全</strong>
- **使用 Azure OpenAI 向量嵌入的語意產品搜尋**
- **VS Code AI 聊天整合**，支援自然語言查詢
- <strong>生產環境部署</strong>，使用 Docker 和 Azure
- <strong>全面監控</strong>，利用 Application Insights

## 🎯 學習先決條件

為了最大化學習成效，您應具備：

- <strong>程式設計經驗</strong>：熟悉 Python(優選)或相似語言
- <strong>資料庫知識</strong>：基本 SQL 和關聯式資料庫概念
- **API 概念**：了解 REST API 和 HTTP 基礎
- <strong>開發工具</strong>：使用命令列、Git 與程式編輯器經驗
- <strong>雲端基礎</strong>：(選擇性) 了解 Azure 或類似雲端平台
- **Docker 熟悉度**：(選擇性) 了解容器化概念

### 必備工具

- **Docker Desktop** - 執行 PostgreSQL 與 MCP 伺服器
- **Azure CLI** - 部署雲端資源
- **VS Code** - 開發與 MCP 整合
- **Git** - 版本控制
- **Python 3.8+** - MCP 伺服器開發

## 📚 學習指南與資源

本學習路徑包含豐富資源，助您有效導航：

### 學習指南

各實驗室包含：
- <strong>明確學習目標</strong> - 您將達成的成果
- <strong>逐步操作指引</strong> - 詳細實作說明
- <strong>程式碼範例</strong> - 可運作範例與解說
- <strong>練習題</strong> - 實作練習機會
- <strong>除錯指南</strong> - 常見問題及解決方案
- <strong>附加資源</strong> - 進階閱讀與探索

### 先決條件檢查

每個實驗室開始前，您可參考：
- <strong>必要知識</strong> - 您應具備的預備能力
- <strong>環境驗證</strong> - 如何確認環境配置準備完成
- <strong>時間預估</strong> - 預計完成時間
- <strong>學習成效</strong> - 完成後您將掌握的內容

### 推薦學習路徑

可依經驗層級選擇適合的路徑：

#### 🟢 <strong>初學者路徑</strong>（MCP 新手）
1. 確認已完成 [MCP 初學者指南](https://aka.ms/mcp-for-beginners) 0-10 節
2. 完成 00-03 實驗室，強化基礎理解
3. 進行 04-06 實驗室動手建置
4. 嘗試 07-09 實驗室，應用實務

#### 🟡 <strong>中階路徑</strong>（具備部分 MCP 經驗）
1. 複習 00-01 實驗室，掌握資料庫專屬概念
2. 專注 02-06 實驗室的實作
3. 深入 07-12 實驗室，探索進階功能

#### 🔴 <strong>進階路徑</strong>（具備 MCP 經驗）
1. 快速瀏覽 00-03 實驗室獲得背景知識
2. 專注 04-09 實驗室完成資料庫整合
3. 集中 10-12 實驗室的生產部署各階段

## 🛠️ 如何有效利用此學習路徑

### 依序學習（推薦）

按順序完成實驗室，獲得完整理解：

1. <strong>閱讀總覽</strong> - 瞭解您將學習內容
2. <strong>檢查先決條件</strong> - 確保具備必要知識
3. <strong>跟著步驟操作</strong> - 一邊學一邊實作
4. <strong>完成練習題</strong> - 強化理解
5. <strong>回顧重點</strong> - 鞏固學習成果

### 針對性學習

若您需要特定技能：

- <strong>資料庫整合</strong>：專注 04-06 實驗室
- <strong>安全性實作</strong>：重點在 02、08、12 實驗室
- **AI / 語意搜尋**：深入 07 實驗室
- <strong>生產部署</strong>：研讀 10-12 實驗室

### 實務練習

各實驗室包含：
- <strong>可運作程式碼範例</strong> - 複製、修改與嘗試
- <strong>實際場景</strong> - 實務零售分析案例
- <strong>漸進難度</strong> - 從簡單到進階建置
- <strong>驗證步驟</strong> - 確認您的實作效果

## 🌟 社群與支援

### 尋求幫助

- **Azure AI Discord**： [加入專家支援](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 倉庫與實作範例**： [部署範例與資源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社群**： [參與更廣泛的 MCP 討論](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 準備開始了嗎？

從 **[實驗室 00：MCP 資料庫整合簡介](./00-Introduction/README.md)** 開始您的旅程

---

*透過這個全面且實務的學習體驗，精通建置可投入生產的 MCP 與資料庫整合伺服器。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
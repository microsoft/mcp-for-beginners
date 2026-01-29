# 🚀 MCP 伺服器與 PostgreSQL - 完整學習指南

## 🧠 MCP 資料庫整合學習路徑概述

這份全面的學習指南教您如何透過實際的零售分析實作，建立可投入生產的 **Model Context Protocol (MCP) 伺服器**，並整合資料庫。您將學習企業級模式，包括 **Row Level Security (RLS)**、**語義搜尋**、**Azure AI 整合** 和 **多租戶資料存取**。

無論您是後端開發者、AI 工程師或資料架構師，這份指南提供結構化的學習內容，包含真實案例和實作練習，並引導您完成 MCP 伺服器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 資源

- 📘 [MCP 文件](https://modelcontextprotocol.io/) – 詳細的教學和使用指南
- 📜 [MCP 規範](https://modelcontextprotocol.io/docs/) – 協議架構和技術參考
- 🧑‍💻 [MCP GitHub 儲存庫](https://github.com/modelcontextprotocol) – 開源 SDK、工具和程式碼範例
- 🌐 [MCP 社群](https://github.com/orgs/modelcontextprotocol/discussions) – 加入討論並為社群做出貢獻

## 🧭 MCP 資料庫整合學習路徑

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 的完整學習結構

| 實驗 | 主題 | 描述 | 連結 |
|--------|-------|-------------|------|
| **實驗 1-3：基礎** | | | |
| 00 | [MCP 資料庫整合簡介](./00-Introduction/README.md) | MCP 與資料庫整合及零售分析案例概述 | [從這裡開始](./00-Introduction/README.md) |
| 01 | [核心架構概念](./01-Architecture/README.md) | 理解 MCP 伺服器架構、資料庫層級和安全模式 | [學習](./01-Architecture/README.md) |
| 02 | [安全性與多租戶](./02-Security/README.md) | Row Level Security、身份驗證和多租戶資料存取 | [學習](./02-Security/README.md) |
| 03 | [環境設置](./03-Setup/README.md) | 設置開發環境、Docker 和 Azure 資源 | [設置](./03-Setup/README.md) |
| **實驗 4-6：建立 MCP 伺服器** | | | |
| 04 | [資料庫設計與結構](./04-Database/README.md) | PostgreSQL 設置、零售結構設計和範例資料 | [建立](./04-Database/README.md) |
| 05 | [MCP 伺服器實作](./05-MCP-Server/README.md) | 建立與資料庫整合的 FastMCP 伺服器 | [建立](./05-MCP-Server/README.md) |
| 06 | [工具開發](./06-Tools/README.md) | 創建資料庫查詢工具和結構檢視工具 | [建立](./06-Tools/README.md) |
| **實驗 7-9：進階功能** | | | |
| 07 | [語義搜尋整合](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 和 pgvector 實作向量嵌入 | [進階](./07-Semantic-Search/README.md) |
| 08 | [測試與除錯](./08-Testing/README.md) | 測試策略、除錯工具和驗證方法 | [測試](./08-Testing/README.md) |
| 09 | [VS Code 整合](./09-VS-Code/README.md) | 配置 VS Code MCP 整合和 AI 聊天使用 | [整合](./09-VS-Code/README.md) |
| **實驗 10-12：生產與最佳實踐** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure Container Apps 和擴展考量 | [部署](./10-Deployment/README.md) |
| 11 | [監控與可觀測性](./11-Monitoring/README.md) | Application Insights、日誌記錄和效能監控 | [監控](./11-Monitoring/README.md) |
| 12 | [最佳實踐與優化](./12-Best-Practices/README.md) | 效能優化、安全加固和生產技巧 | [優化](./12-Best-Practices/README.md) |

### 💻 您將建立的內容

完成此學習路徑後，您將建立一個完整的 **Zava 零售分析 MCP 伺服器**，包含：

- **多表零售資料庫**，包括客戶訂單、產品和庫存
- **Row Level Security**，實現基於商店的資料隔離
- **語義產品搜尋**，使用 Azure OpenAI 嵌入技術
- **VS Code AI 聊天整合**，進行自然語言查詢
- **生產就緒部署**，使用 Docker 和 Azure
- **全面監控**，透過 Application Insights

## 🎯 學習的先決條件

為了充分利用此學習路徑，您應具備以下知識：

- **程式設計經驗**：熟悉 Python（首選）或類似語言
- **資料庫知識**：基本了解 SQL 和關聯式資料庫
- **API 概念**：理解 REST API 和 HTTP 概念
- **開發工具**：熟悉命令列、Git 和程式碼編輯器
- **雲端基礎知識**：（選擇性）基本了解 Azure 或類似雲端平台
- **Docker 熟悉度**：（選擇性）理解容器化概念

### 所需工具

- **Docker Desktop** - 用於執行 PostgreSQL 和 MCP 伺服器
- **Azure CLI** - 用於部署雲端資源
- **VS Code** - 用於開發和 MCP 整合
- **Git** - 用於版本控制
- **Python 3.8+** - 用於 MCP 伺服器開發

## 📚 學習指南與資源

此學習路徑包含全面的資源，幫助您有效學習：

### 學習指南

每個實驗包含：
- **清晰的學習目標** - 您將達成的目標
- **逐步指導** - 詳細的實作指南
- **程式碼範例** - 帶有解釋的工作範例
- **練習** - 實作練習機會
- **故障排除指南** - 常見問題及解決方案
- **額外資源** - 進一步閱讀和探索

### 先決條件檢查

在開始每個實驗之前，您將看到：
- **所需知識** - 您應事先了解的內容
- **設置驗證** - 如何驗證您的環境
- **時間估算** - 預期完成時間
- **學習成果** - 完成後您將掌握的內容

### 推薦學習路徑

根據您的經驗水平選擇學習路徑：

#### 🟢 **初學者路徑**（MCP 新手）
1. 確保您已完成 [MCP 初學者指南](https://aka.ms/mcp-for-beginners) 的 0-10 節
2. 完成實驗 00-03，鞏固基礎知識
3. 跟隨實驗 04-06，進行實作
4. 嘗試實驗 07-09，進行實際應用

#### 🟡 **中級路徑**（有 MCP 經驗）
1. 回顧實驗 00-01，了解資料庫相關概念
2. 專注於實驗 02-06，進行實作
3. 深入研究實驗 07-12，探索進階功能

#### 🔴 **高級路徑**（MCP 熟手）
1. 瀏覽實驗 00-03，了解背景
2. 專注於實驗 04-09，進行資料庫整合
3. 集中於實驗 10-12，進行生產部署

## 🛠️ 如何有效使用此學習路徑

### 順序學習（推薦）

依次完成實驗，全面理解：

1. **閱讀概述** - 了解您將學習的內容
2. **檢查先決條件** - 確保您具備所需知識
3. **遵循逐步指導** - 邊學邊實作
4. **完成練習** - 鞏固您的理解
5. **回顧重點** - 鞏固學習成果

### 目標導向學習

如果您需要特定技能：

- **資料庫整合**：專注於實驗 04-06
- **安全性實作**：集中於實驗 02、08、12
- **AI/語義搜尋**：深入研究實驗 07
- **生產部署**：學習實驗 10-12

### 實作練習

每個實驗包含：
- **工作程式碼範例** - 複製、修改並試驗
- **真實案例** - 實際零售分析應用場景
- **漸進式複雜度** - 從簡單到進階逐步建立
- **驗證步驟** - 確保您的實作有效

## 🌟 社群與支援

### 獲得幫助

- **Azure AI Discord**: [加入以獲得專家支援](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 儲存庫與實作範例**: [部署範例與資源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社群**: [加入更廣泛的 MCP 討論](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 準備開始了嗎？

從 **[實驗 00：MCP 資料庫整合簡介](./00-Introduction/README.md)** 開始您的旅程

---

*透過這份全面且實作導向的學習體驗，掌握建立生產就緒的 MCP 伺服器與資料庫整合的技能。*

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
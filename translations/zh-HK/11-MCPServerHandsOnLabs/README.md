# 🚀 MCP 伺服器與 PostgreSQL - 完整學習指南

## 🧠 MCP 數據庫整合學習路徑概覽

這份全面的學習指南教你如何通過實際的零售分析實現，構建可投入生產的 **Model Context Protocol (MCP) 伺服器**，並整合數據庫。你將學習企業級模式，包括 **行級安全性 (RLS)**、**語義搜索**、**Azure AI 整合** 和 **多租戶數據訪問**。

無論你是後端開發者、AI 工程師還是數據架構師，這份指南提供結構化的學習內容，包含真實案例和動手練習，帶你一步步完成 MCP 伺服器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 資源

- 📘 [MCP 文檔](https://modelcontextprotocol.io/) – 詳細教程和用戶指南
- 📜 [MCP 規範](https://modelcontextprotocol.io/docs/) – 協議架構和技術參考
- 🧑‍💻 [MCP GitHub 資源庫](https://github.com/modelcontextprotocol) – 開源 SDK、工具和代碼示例
- 🌐 [MCP 社群](https://github.com/orgs/modelcontextprotocol/discussions) – 加入討論並為社群做出貢獻

## 🧭 MCP 數據庫整合學習路徑

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 的完整學習結構

| 實驗 | 主題 | 描述 | 連結 |
|--------|-------|-------------|------|
| **實驗 1-3：基礎** | | | |
| 00 | [MCP 數據庫整合介紹](./00-Introduction/README.md) | MCP 與數據庫整合及零售分析案例概述 | [從這裡開始](./00-Introduction/README.md) |
| 01 | [核心架構概念](./01-Architecture/README.md) | 理解 MCP 伺服器架構、數據庫層和安全模式 | [學習](./01-Architecture/README.md) |
| 02 | [安全性與多租戶](./02-Security/README.md) | 行級安全性、身份驗證和多租戶數據訪問 | [學習](./02-Security/README.md) |
| 03 | [環境設置](./03-Setup/README.md) | 設置開發環境、Docker 和 Azure 資源 | [設置](./03-Setup/README.md) |
| **實驗 4-6：構建 MCP 伺服器** | | | |
| 04 | [數據庫設計與架構](./04-Database/README.md) | PostgreSQL 設置、零售架構設計和示例數據 | [構建](./04-Database/README.md) |
| 05 | [MCP 伺服器實現](./05-MCP-Server/README.md) | 構建與數據庫整合的 FastMCP 伺服器 | [構建](./05-MCP-Server/README.md) |
| 06 | [工具開發](./06-Tools/README.md) | 創建數據庫查詢工具和架構檢視工具 | [構建](./06-Tools/README.md) |
| **實驗 7-9：進階功能** | | | |
| 07 | [語義搜索整合](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 和 pgvector 實現向量嵌入 | [進階](./07-Semantic-Search/README.md) |
| 08 | [測試與除錯](./08-Testing/README.md) | 測試策略、除錯工具和驗證方法 | [測試](./08-Testing/README.md) |
| 09 | [VS Code 整合](./09-VS-Code/README.md) | 配置 VS Code MCP 整合及 AI 聊天功能 | [整合](./09-VS-Code/README.md) |
| **實驗 10-12：生產與最佳實踐** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure 容器應用和擴展考量 | [部署](./10-Deployment/README.md) |
| 11 | [監控與可觀測性](./11-Monitoring/README.md) | 應用洞察、日誌記錄和性能監控 | [監控](./11-Monitoring/README.md) |
| 12 | [最佳實踐與優化](./12-Best-Practices/README.md) | 性能優化、安全加固和生產技巧 | [優化](./12-Best-Practices/README.md) |

### 💻 你將構建的內容

完成這條學習路徑後，你將構建一個完整的 **Zava 零售分析 MCP 伺服器**，包括：

- **多表零售數據庫**，包含客戶訂單、產品和庫存
- **行級安全性**，實現基於門店的數據隔離
- **語義產品搜索**，使用 Azure OpenAI 嵌入技術
- **VS Code AI 聊天整合**，支持自然語言查詢
- **生產級部署**，使用 Docker 和 Azure
- **全面監控**，通過應用洞察實現

## 🎯 學習的先決條件

為了充分利用這條學習路徑，你應該具備以下知識：

- **編程經驗**：熟悉 Python（首選）或類似語言
- **數據庫知識**：基本了解 SQL 和關係型數據庫
- **API 概念**：理解 REST API 和 HTTP 概念
- **開發工具**：熟悉命令行、Git 和代碼編輯器
- **雲基礎知識**：（可選）基本了解 Azure 或類似雲平台
- **Docker 基礎**：（可選）理解容器化概念

### 所需工具

- **Docker Desktop** - 用於運行 PostgreSQL 和 MCP 伺服器
- **Azure CLI** - 用於部署雲資源
- **VS Code** - 用於開發和 MCP 整合
- **Git** - 用於版本控制
- **Python 3.8+** - 用於 MCP 伺服器開發

## 📚 學習指南與資源

這條學習路徑包含全面的資源，幫助你有效學習：

### 學習指南

每個實驗包括：
- **清晰的學習目標** - 你將達成的目標
- **逐步指導** - 詳細的實現指南
- **代碼示例** - 帶有解釋的工作示例
- **練習** - 動手練習機會
- **故障排除指南** - 常見問題及解決方案
- **額外資源** - 深入閱讀和探索

### 先決條件檢查

在開始每個實驗之前，你會看到：
- **所需知識** - 你需要事先了解的內容
- **設置驗證** - 如何驗證你的環境
- **時間估算** - 預期完成時間
- **學習成果** - 完成後你將掌握的知識

### 推薦學習路徑

根據你的經驗水平選擇學習路徑：

#### 🟢 **初學者路徑**（MCP 新手）
1. 確保你已完成 [MCP 初學者指南](https://aka.ms/mcp-for-beginners) 的 0-10 節
2. 完成實驗 00-03，鞏固基礎知識
3. 跟隨實驗 04-06，進行動手構建
4. 嘗試實驗 07-09，進行實際應用

#### 🟡 **中級路徑**（有 MCP 經驗）
1. 回顧實驗 00-01，了解數據庫相關概念
2. 重點學習實驗 02-06，進行實現
3. 深入研究實驗 07-12，掌握進階功能

#### 🔴 **高級路徑**（MCP 高手）
1. 瀏覽實驗 00-03，了解背景
2. 重點學習實驗 04-09，進行數據庫整合
3. 專注於實驗 10-12，進行生產部署

## 🛠️ 如何有效使用這條學習路徑

### 順序學習（推薦）

按順序完成實驗，全面理解：

1. **閱讀概述** - 理解你將學到的內容
2. **檢查先決條件** - 確保你具備所需知識
3. **跟隨逐步指導** - 邊學邊實現
4. **完成練習** - 鞏固你的理解
5. **回顧關鍵要點** - 強化學習成果

### 目標導向學習

如果你需要特定技能：

- **數據庫整合**：重點學習實驗 04-06
- **安全性實現**：專注於實驗 02、08、12
- **AI/語義搜索**：深入研究實驗 07
- **生產部署**：學習實驗 10-12

### 動手練習

每個實驗包括：
- **工作代碼示例** - 複製、修改並試驗
- **真實場景** - 實際零售分析案例
- **漸進式複雜度** - 從簡單到高級逐步構建
- **驗證步驟** - 確保你的實現有效

## 🌟 社群與支持

### 獲取幫助

- **Azure AI Discord**: [加入以獲取專家支持](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 資源庫與實現示例**: [部署示例與資源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社群**: [加入更廣泛的 MCP 討論](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 準備開始了嗎？

從 **[實驗 00：MCP 數據庫整合介紹](./00-Introduction/README.md)** 開始你的旅程吧！

---

*通過這份全面的動手學習體驗，掌握構建生產級 MCP 伺服器與數據庫整合的技能。*

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
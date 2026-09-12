# 🚀 MCP 伺服器與 PostgreSQL - 完整學習指南

## 🧠 MCP 數據庫整合學習路徑概覽

本綜合學習指南教你如何透過實務零售分析案例構建生產等級的 **模型上下文協議 (MCP) 伺服器**，並整合數據庫。你將學習企業級模式，包括 **列級安全 (RLS)**、<strong>語義搜尋</strong>、<strong>Azure AI 整合</strong>及<strong>多租戶數據存取</strong>。

無論你是後端開發者、AI 工程師或資料架構師，本指南以結構化學習和實際範例及操作練習，帶領你完成以下 MCP 伺服器 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail。

## 🔗 官方 MCP 資源

- 📘 [MCP 文件](https://modelcontextprotocol.io/) – 詳細教學與使用指南
- 📜 [MCP 規範 (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – 協議架構與技術參考
- 🧑‍💻 [MCP GitHub 倉庫](https://github.com/modelcontextprotocol) – 開源 SDK、工具與程式碼範例
- 🌐 [MCP 社群](https://github.com/orgs/modelcontextprotocol/discussions) – 參與討論並貢獻社群
- 🔒 [OWASP MCP 前十大](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – 安全最佳實踐與風險緩解


## 🧭 MCP 數據庫整合學習路徑

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 完整學習結構

| 實驗室 | 主題 | 描述 | 連結 |
|--------|-------|-------------|------|
| **實驗室 1-3：基礎** | | | |
| 00 | [MCP 與數據庫整合簡介](./00-Introduction/README.md) | MCP 與數據庫整合及零售分析使用案例概覽 | [從這裡開始](./00-Introduction/README.md) |
| 01 | [核心架構概念](./01-Architecture/README.md) | 理解 MCP 伺服器架構、數據庫層與安全模式 | [學習](./01-Architecture/README.md) |
| 02 | [安全性與多租戶](./02-Security/README.md) | 列級安全、驗證與多租戶數據存取 | [學習](./02-Security/README.md) |
| 03 | [環境設置](./03-Setup/README.md) | 建置開發環境、Docker、Azure 資源 | [設置](./03-Setup/README.md) |
| **實驗室 4-6：建構 MCP 伺服器** | | | |
| 04 | [數據庫設計與架構](./04-Database/README.md) | PostgreSQL 設定、零售架構設計與範例資料 | [建構](./04-Database/README.md) |
| 05 | [MCP 伺服器實作](./05-MCP-Server/README.md) | 搭建具數據庫整合的 FastMCP 伺服器 | [建構](./05-MCP-Server/README.md) |
| 06 | [工具開發](./06-Tools/README.md) | 建立數據庫查詢工具及架構探索 | [建構](./06-Tools/README.md) |
| **實驗室 7-9：進階功能** | | | |
| 07 | [語義搜尋整合](./07-Semantic-Search/README.md) | 使用 Azure OpenAI 與 pgvector 實現向量嵌入 | [進階](./07-Semantic-Search/README.md) |
| 08 | [測試與除錯](./08-Testing/README.md) | 測試策略、除錯工具與驗證方法 | [測試](./08-Testing/README.md) |
| 09 | [VS Code 整合](./09-VS-Code/README.md) | 配置 VS Code MCP 整合與 AI 聊天使用 | [整合](./09-VS-Code/README.md) |
| **實驗室 10-12：生產與最佳實踐** | | | |
| 10 | [部署策略](./10-Deployment/README.md) | Docker 部署、Azure Container Apps 和擴展考量 | [部署](./10-Deployment/README.md) |
| 11 | [監控與可觀察性](./11-Monitoring/README.md) | Application Insights、日誌與效能監控 | [監控](./11-Monitoring/README.md) |
| 12 | [最佳實踐與優化](./12-Best-Practices/README.md) | 效能優化、安全強化與生產環境技巧 | [優化](./12-Best-Practices/README.md) |

### 💻 你將建立的內容

完成此學習路徑後，你將擁有一個完整的 **Zava 零售分析 MCP 伺服器**，具備：

- <strong>多表零售數據庫</strong>，涵蓋客戶訂單、產品與庫存
- <strong>列級安全</strong>，實現門店間數據隔離
- <strong>語義產品搜尋</strong>，採用 Azure OpenAI 嵌入技術
- **VS Code AI 聊天整合**，支持自然語言查詢
- <strong>生產就緒的部署</strong>，使用 Docker 與 Azure
- <strong>完善的監控</strong>，結合 Application Insights

## 🎯 學習前置條件

為充分利用此學習路徑，你應具備：

- <strong>程式設計經驗</strong>：熟悉 Python（首選）或類似語言
- <strong>數據庫知識</strong>：基本 SQL 和關聯式數據庫認識
- **API 概念**：理解 REST API 和 HTTP 基本概念
- <strong>開發工具</strong>：具命令列、Git 及程式編輯器經驗
- <strong>雲端基礎</strong>：（選擇性）瞭解 Azure 或類似雲端平台
- **Docker 熟悉度**：（選擇性）理解容器化概念

### 必備工具

- **Docker Desktop** - 執行 PostgreSQL 與 MCP 伺服器
- **Azure CLI** - 雲端資源部署
- **VS Code** - 開發與 MCP 整合
- **Git** - 版本控制
- **Python 3.8+** - MCP 伺服器開發

## 📚 學習指南與資源

本學習路徑包含豐富資源，助你有效掌握：

### 學習指南

每個實驗室包含：
- <strong>明確學習目標</strong> - 你將達成的項目
- <strong>逐步操作指引</strong> - 詳細實作教學
- <strong>程式碼範例</strong> - 可運作範例與說明
- <strong>練習題</strong> - 實作練習機會
- <strong>疑難排解指南</strong> - 常見問題與解決方案
- <strong>額外資源</strong> - 深入閱讀與探索

### 前置條件檢查

每個實驗室開始前，你會看到：
- <strong>所需知識</strong> - 須知背景
- <strong>環境驗證</strong> - 如何確保環境正確
- <strong>時間預估</strong> - 預期完成時間
- <strong>學習成果</strong> - 完成後你會掌握的內容

### 推薦學習路徑

根據經驗選擇合適路徑：

#### 🟢 <strong>初學者路徑</strong>（MCP 新手）
1. 先完成 [MCP 初學者](https://aka.ms/mcp-for-beginners) 的 0-10 課程
2. 完成實驗室 00-03，強化基礎理解
3. 跟隨實驗室 04-06，實際建構
4. 嘗試實驗室 07-09，體驗實務應用

#### 🟡 <strong>中階路徑</strong>（有部分 MCP 經驗）
1. 複習實驗室 00-01，強化數據庫專門知識
2. 聚焦實驗室 02-06，進行實作
3. 深入實驗室 07-12，掌握進階功能

#### 🔴 <strong>進階路徑</strong>（熟悉 MCP）
1. 略讀實驗室 00-03，了解背景脈絡
2. 專注實驗室 04-09，數據庫整合
3. 集中實驗室 10-12，生產部署流程

## 🛠️ 如何有效使用此學習路徑

### 按序學習（推薦）

按照順序完成各實驗室，全面掌握內容：

1. <strong>閱讀概覽</strong> - 理解學習內容
2. <strong>檢查前置條件</strong> - 確認具備所需知識
3. <strong>跟隨操作指引</strong> - 實作過程中學習
4. <strong>完成練習題</strong> - 鞏固理解
5. <strong>回顧重點</strong> - 強化學習成果

### 定向學習

若需特定技能學習：

- <strong>數據庫整合</strong>：聚焦實驗室 04-06
- <strong>安全實作</strong>：專注實驗室 02、08、12
- **AI/語義搜尋**：深入實驗室 07
- <strong>生產部署</strong>：研讀實驗室 10-12

### 實務演練

每個實驗室包含：
- <strong>可運作程式碼範例</strong> - 複製、修改與實驗
- <strong>真實場景模擬</strong> - 實務零售分析案例
- <strong>逐步提升難度</strong> - 從簡單到進階構建
- <strong>驗證步驟</strong> - 確定實作成功

## 🌟 社群與支持

### 尋求協助

- **Azure AI Discord**: [加入獲得專家支援](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 倉庫與實作範例**: [部署範例與資源](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 社群**: [加入 MCP 更大社群討論](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 準備好開始了嗎？

即刻開始你的旅程，從 **[實驗室 00：MCP 與數據庫整合介紹](./00-Introduction/README.md)** 開始

---

*透過此完整且實作豐富的學習體驗，精通構建生產就緒的 MCP 伺服器與數據庫整合。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
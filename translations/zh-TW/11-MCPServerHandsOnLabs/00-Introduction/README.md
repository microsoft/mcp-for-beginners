# MCP 資料庫整合介紹

## 🎯 本實驗涵蓋內容

本介紹實驗提供了建立具備資料庫整合功能的 Model Context Protocol (MCP) 伺服器的全面概述。透過 Zava Retail 分析案例（https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail），您將了解商業案例、技術架構以及實際應用。

## 概述

**Model Context Protocol (MCP)** 使 AI 助手能夠安全地即時存取並與外部資料來源互動。結合資料庫整合後，MCP 為以資料驅動的 AI 應用解鎖了強大的功能。

此學習路徑教您如何建立可投入生產的 MCP 伺服器，透過 PostgreSQL 將 AI 助手連接到零售銷售資料，並實現企業模式，例如行級安全性、語義搜尋以及多租戶資料存取。

## 學習目標

完成本實驗後，您將能夠：

- **定義** Model Context Protocol 及其在資料庫整合中的核心優勢
- **識別** MCP 伺服器架構中與資料庫相關的關鍵組件
- **理解** Zava Retail 案例及其商業需求
- **認識** 安全且可擴展的資料庫存取的企業模式
- **列出** 此學習路徑中使用的工具和技術

## 🧭 挑戰：AI 與真實世界資料的結合

### 傳統 AI 的限制

現代 AI 助手功能強大，但在處理真實世界商業資料時面臨重大限制：

| **挑戰** | **描述** | **商業影響** |
|----------|----------|--------------|
| **靜態知識** | AI 模型僅基於固定資料集訓練，無法存取最新商業資料 | 資訊過時，錯失商機 |
| **資料孤島** | 資料被鎖定在 AI 無法存取的資料庫、API 和系統中 | 分析不完整，工作流程分散 |
| **安全限制** | 直接存取資料庫會引發安全性和合規性問題 | 部署受限，需手動準備資料 |
| **複雜查詢** | 商業用戶需要技術知識才能提取資料洞察 | 使用率降低，流程低效 |

### MCP 解決方案

Model Context Protocol 解決了這些挑戰，提供：

- **即時資料存取**：AI 助手可查詢即時資料庫和 API
- **安全整合**：透過身份驗證和權限控制存取
- **自然語言介面**：商業用戶可用簡單英文提問
- **標準化協議**：適用於不同的 AI 平台和工具

## 🏪 認識 Zava Retail：學習案例研究 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

在整個學習路徑中，我們將為 **Zava Retail** 建立 MCP 伺服器，這是一個虛構的 DIY 零售連鎖店，擁有多個店鋪位置。此真實場景展示了企業級 MCP 實施。

### 商業背景

**Zava Retail** 的運營包括：
- **8 間實體店鋪**，位於華盛頓州（西雅圖、貝爾維尤、塔科馬、斯波坎、埃弗里特、雷德蒙、柯克蘭）
- **1 間線上商店**，提供電子商務銷售
- **多樣化產品目錄**，包括工具、五金、園藝用品和建材
- **多層管理架構**，包括店鋪經理、區域經理和高管

### 商業需求

店鋪經理和高管需要 AI 驅動的分析功能以：

1. **分析銷售表現**，涵蓋不同店鋪和時間段
2. **追蹤庫存水平**，識別補貨需求
3. **了解顧客行為**，分析購買模式
4. **透過語義搜尋** 發掘產品洞察
5. **生成報告**，使用自然語言查詢
6. **維護資料安全**，採用基於角色的存取控制

### 技術需求

MCP 伺服器必須提供：

- **多租戶資料存取**，店鋪經理僅能查看自己店鋪的資料
- **靈活查詢**，支持複雜的 SQL 操作
- **語義搜尋**，用於產品發現和推薦
- **即時資料**，反映當前商業狀態
- **安全身份驗證**，採用行級安全性
- **可擴展架構**，支持多個並發用戶

## 🏗️ MCP 伺服器架構概述

我們的 MCP 伺服器實現了一個針對資料庫整合優化的分層架構：

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### 關鍵組件

#### **1. MCP 伺服器層**
- **FastMCP 框架**：現代 Python MCP 伺服器實現
- **工具註冊**：使用類型安全的聲明式工具定義
- **請求上下文**：用戶身份和會話管理
- **錯誤處理**：穩健的錯誤管理和日誌記錄

#### **2. 資料庫整合層**
- **連接池管理**：高效的 asyncpg 連接管理
- **架構提供者**：動態表架構發現
- **查詢執行器**：基於 RLS 上下文的安全 SQL 執行
- **交易管理**：ACID 合規性和回滾處理

#### **3. 安全層**
- **行級安全性**：PostgreSQL RLS 用於多租戶資料隔離
- **用戶身份**：店鋪經理身份驗證和授權
- **存取控制**：細粒度的權限和審計追蹤
- **輸入驗證**：防止 SQL 注入和查詢驗證

#### **4. AI 增強層**
- **語義搜尋**：使用向量嵌入進行產品發現
- **Azure OpenAI 整合**：生成文本嵌入
- **相似性算法**：pgvector 餘弦相似性搜尋
- **搜尋優化**：索引和性能調整

## 🔧 技術堆疊

### 核心技術

| **組件** | **技術** | **用途** |
|----------|----------|----------|
| **MCP 框架** | FastMCP (Python) | 現代 MCP 伺服器實現 |
| **資料庫** | PostgreSQL 17 + pgvector | 關聯式資料與向量搜尋 |
| **AI 服務** | Azure OpenAI | 文本嵌入和語言模型 |
| **容器化** | Docker + Docker Compose | 開發環境 |
| **雲平台** | Microsoft Azure | 生產部署 |
| **IDE 整合** | VS Code | AI 聊天和開發工作流程 |

### 開發工具

| **工具** | **用途** |
|----------|----------|
| **asyncpg** | 高性能 PostgreSQL 驅動 |
| **Pydantic** | 資料驗證和序列化 |
| **Azure SDK** | 雲服務整合 |
| **pytest** | 測試框架 |
| **Docker** | 容器化和部署 |

### 生產堆疊

| **服務** | **Azure 資源** | **用途** |
|----------|----------------|----------|
| **資料庫** | Azure Database for PostgreSQL | 管理式資料庫服務 |
| **容器** | Azure Container Apps | 無伺服器容器託管 |
| **AI 服務** | Azure AI Foundry | OpenAI 模型和端點 |
| **監控** | Application Insights | 可觀察性和診斷 |
| **安全性** | Azure Key Vault | 機密和配置管理 |

## 🎬 真實世界使用場景

讓我們探索不同用戶如何與 MCP 伺服器互動：

### 場景 1：店鋪經理的績效審查

**用戶**：Sarah，西雅圖店鋪經理  
**目標**：分析上一季度的銷售表現

**自然語言查詢**：
> "顯示我店鋪在 2024 年第四季度收入最高的前 10 項產品"

**發生了什麼**：
1. VS Code AI 聊天將查詢發送到 MCP 伺服器
2. MCP 伺服器識別 Sarah 的店鋪上下文（西雅圖）
3. RLS 策略僅篩選西雅圖店鋪的資料
4. 生成並執行 SQL 查詢
5. 格式化結果並返回到 AI 聊天
6. AI 提供分析和洞察

### 場景 2：使用語義搜尋進行產品發現

**用戶**：Mike，庫存經理  
**目標**：找到類似顧客需求的產品

**自然語言查詢**：
> "我們有哪些產品類似於‘戶外使用的防水電氣接頭’？"

**發生了什麼**：
1. 查詢由語義搜尋工具處理
2. Azure OpenAI 生成嵌入向量
3. pgvector 執行相似性搜尋
4. 相關產品按相關性排序
5. 結果包括產品詳細信息和可用性
6. AI 建議替代品和捆綁銷售機會

### 場景 3：跨店鋪分析

**用戶**：Jennifer，區域經理  
**目標**：比較所有店鋪的表現

**自然語言查詢**：
> "比較過去 6 個月所有店鋪的銷售類別"

**發生了什麼**：
1. 為區域經理存取設置 RLS 上下文
2. 生成複雜的多店鋪查詢
3. 數據在店鋪位置間聚合
4. 結果包括趨勢和比較
5. AI 識別洞察和建議

## 🔒 安全性與多租戶深入探討

我們的實現優先考慮企業級安全性：

### 行級安全性 (RLS)

PostgreSQL RLS 確保資料隔離：

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### 用戶身份管理

每個 MCP 連接包括：
- **店鋪經理 ID**：RLS 上下文的唯一標識符
- **角色分配**：權限和存取級別
- **會話管理**：安全身份驗證令牌
- **審計日誌**：完整的存取歷史記錄

### 資料保護

多層安全性：
- **連接加密**：所有資料庫連接使用 TLS
- **SQL 注入防護**：僅使用參數化查詢
- **輸入驗證**：全面的請求驗證
- **錯誤處理**：錯誤消息中不包含敏感資料

## 🎯 關鍵要點

完成本介紹後，您應該了解：

✅ **MCP 價值主張**：MCP 如何連接 AI 助手與真實世界資料  
✅ **商業背景**：Zava Retail 的需求和挑戰  
✅ **架構概述**：關鍵組件及其交互方式  
✅ **技術堆疊**：整個過程中使用的工具和框架  
✅ **安全模型**：多租戶資料存取和保護  
✅ **使用模式**：真實世界查詢場景和工作流程  

## 🚀 下一步

準備深入了解？繼續學習：

**[實驗 01：核心架構概念](../01-Architecture/README.md)**

了解 MCP 伺服器架構模式、資料庫設計原則以及支持我們零售分析解決方案的詳細技術實現。

## 📚 其他資源

### MCP 文件
- [MCP 規範](https://modelcontextprotocol.io/docs/) - 官方協議文件
- [MCP 初學者指南](https://aka.ms/mcp-for-beginners) - 全面的 MCP 學習指南
- [FastMCP 文件](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 文件

### 資料庫整合
- [PostgreSQL 文件](https://www.postgresql.org/docs/) - 完整的 PostgreSQL 參考
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量擴展文件
- [行級安全性](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服務
- [Azure OpenAI 文件](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服務整合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 管理式資料庫服務
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 無伺服器容器

---

**免責聲明**：這是一個使用虛構零售資料的學習練習。在生產環境中實施類似解決方案時，請始終遵循您組織的資料治理和安全政策。

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用本翻譯而引起的任何誤解或錯誤解讀概不負責。
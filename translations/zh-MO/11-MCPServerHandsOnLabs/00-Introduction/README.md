# MCP 數據庫整合介紹

## 🎯 本實驗涵蓋內容

這個入門實驗提供了建立具有數據庫整合功能的 Model Context Protocol (MCP) 伺服器的全面概述。透過 Zava Retail 分析案例（https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail），您將了解業務案例、技術架構以及實際應用。

## 概述

**Model Context Protocol (MCP)** 使 AI 助手能夠安全地即時訪問並與外部數據源交互。結合數據庫整合，MCP 為數據驅動的 AI 應用解鎖了強大的功能。

此學習路徑教您如何構建生產級 MCP 伺服器，通過 PostgreSQL 將 AI 助手連接到零售銷售數據，並實現企業模式，例如行級安全性、語義搜索和多租戶數據訪問。

## 學習目標

完成本實驗後，您將能夠：

- **定義** Model Context Protocol 及其在數據庫整合中的核心優勢
- **識別** MCP 伺服器架構中與數據庫相關的關鍵組件
- **理解** Zava Retail 案例及其業務需求
- **認識** 安全且可擴展的數據庫訪問的企業模式
- **列出** 此學習路徑中使用的工具和技術

## 🧭 挑戰：AI 與真實世界數據的結合

### 傳統 AI 的局限性

現代 AI 助手功能強大，但在處理真實世界業務數據時面臨重大局限：

| **挑戰** | **描述** | **業務影響** |
|----------|----------|--------------|
| **靜態知識** | AI 模型基於固定數據集訓練，無法訪問最新業務數據 | 過時的洞察，錯失機會 |
| **數據孤島** | 信息被鎖定在 AI 無法訪問的數據庫、API 和系統中 | 分析不完整，工作流程分散 |
| **安全限制** | 直接訪問數據庫會引發安全和合規問題 | 部署受限，需手動準備數據 |
| **複雜查詢** | 業務用戶需要技術知識才能提取數據洞察 | 使用率降低，流程低效 |

### MCP 解決方案

Model Context Protocol 通過以下方式解決這些挑戰：

- **即時數據訪問**：AI 助手可查詢實時數據庫和 API
- **安全整合**：通過身份驗證和權限控制進行受控訪問
- **自然語言界面**：業務用戶可用簡單的英語提問
- **標準化協議**：適用於不同的 AI 平台和工具

## 🏪 認識 Zava Retail：學習案例 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

在整個學習路徑中，我們將為 **Zava Retail** 構建 MCP 伺服器，這是一個虛構的 DIY 零售連鎖店，擁有多個門店位置。此場景展示了企業級 MCP 實施。

### 業務背景

**Zava Retail** 的運營包括：
- **8 家實體店**，位於華盛頓州（西雅圖、貝爾維尤、塔科馬、斯波坎、埃弗里特、雷德蒙、柯克蘭）
- **1 家線上商店**，提供電子商務銷售
- **多樣化產品目錄**，包括工具、五金、園藝用品和建築材料
- **多層管理架構**，包括門店經理、區域經理和高管

### 業務需求

門店經理和高管需要 AI 驅動的分析功能來：

1. **分析銷售表現**，涵蓋各門店和時間段
2. **追蹤庫存水平**，並識別補貨需求
3. **了解客戶行為** 和購買模式
4. **通過語義搜索發現產品洞察**
5. **使用自然語言查詢生成報告**
6. **通過基於角色的訪問控制維護數據安全**

### 技術需求

MCP 伺服器必須提供：

- **多租戶數據訪問**，門店經理僅能查看自己門店的數據
- **靈活查詢**，支持複雜的 SQL 操作
- **語義搜索**，用於產品發現和推薦
- **即時數據**，反映當前業務狀態
- **安全身份驗證**，包括行級安全性
- **可擴展架構**，支持多個並發用戶

## 🏗️ MCP 伺服器架構概述

我們的 MCP 伺服器實現了一個針對數據庫整合優化的分層架構：

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
- **工具註冊**：具有類型安全性的聲明式工具定義
- **請求上下文**：用戶身份和會話管理
- **錯誤處理**：健全的錯誤管理和日誌記錄

#### **2. 數據庫整合層**
- **連接池管理**：高效的 asyncpg 連接管理
- **模式提供者**：動態表模式發現
- **查詢執行器**：基於 RLS 上下文的安全 SQL 執行
- **事務管理**：ACID 合規性和回滾處理

#### **3. 安全層**
- **行級安全性**：PostgreSQL RLS 用於多租戶數據隔離
- **用戶身份**：門店經理身份驗證和授權
- **訪問控制**：細粒度的權限和審計記錄
- **輸入驗證**：防止 SQL 注入和查詢驗證

#### **4. AI 增強層**
- **語義搜索**：基於向量嵌入的產品發現
- **Azure OpenAI 整合**：生成文本嵌入
- **相似性算法**：pgvector 餘弦相似性搜索
- **搜索優化**：索引和性能調整

## 🔧 技術堆疊

### 核心技術

| **組件** | **技術** | **用途** |
|----------|----------|----------|
| **MCP 框架** | FastMCP (Python) | 現代 MCP 伺服器實現 |
| **數據庫** | PostgreSQL 17 + pgvector | 關聯數據與向量搜索 |
| **AI 服務** | Azure OpenAI | 文本嵌入和語言模型 |
| **容器化** | Docker + Docker Compose | 開發環境 |
| **雲平台** | Microsoft Azure | 生產部署 |
| **IDE 整合** | VS Code | AI 聊天和開發工作流 |

### 開發工具

| **工具** | **用途** |
|----------|----------|
| **asyncpg** | 高性能 PostgreSQL 驅動 |
| **Pydantic** | 數據驗證和序列化 |
| **Azure SDK** | 雲服務整合 |
| **pytest** | 測試框架 |
| **Docker** | 容器化和部署 |

### 生產堆疊

| **服務** | **Azure 資源** | **用途** |
|----------|----------------|----------|
| **數據庫** | Azure Database for PostgreSQL | 托管數據庫服務 |
| **容器** | Azure Container Apps | 無伺服器容器託管 |
| **AI 服務** | Azure AI Foundry | OpenAI 模型和端點 |
| **監控** | Application Insights | 可觀察性和診斷 |
| **安全性** | Azure Key Vault | 機密和配置管理 |

## 🎬 真實世界使用場景

讓我們探索不同用戶如何與 MCP 伺服器交互：

### 場景 1：門店經理的業績回顧

**用戶**：Sarah，西雅圖門店經理  
**目標**：分析上一季度的銷售表現

**自然語言查詢**：
> "顯示我門店在 2024 年第四季度收入最高的前 10 種產品"

**發生了什麼**：
1. VS Code AI 聊天將查詢發送到 MCP 伺服器
2. MCP 伺服器識別 Sarah 的門店上下文（西雅圖）
3. RLS 策略僅篩選西雅圖門店的數據
4. 生成並執行 SQL 查詢
5. 格式化結果並返回到 AI 聊天
6. AI 提供分析和洞察

### 場景 2：使用語義搜索進行產品發現

**用戶**：Mike，庫存經理  
**目標**：找到與客戶需求相似的產品

**自然語言查詢**：
> "我們有哪些產品類似於‘戶外使用的防水電氣連接器’？"

**發生了什麼**：
1. 查詢由語義搜索工具處理
2. Azure OpenAI 生成嵌入向量
3. pgvector 執行相似性搜索
4. 相關產品按相關性排序
5. 結果包括產品詳細信息和可用性
6. AI 建議替代品和捆綁銷售機會

### 場景 3：跨門店分析

**用戶**：Jennifer，區域經理  
**目標**：比較所有門店的銷售表現

**自然語言查詢**：
> "比較過去 6 個月所有門店的各類銷售情況"

**發生了什麼**：
1. 為區域經理設置 RLS 上下文
2. 生成複雜的多門店查詢
3. 數據在門店位置間聚合
4. 結果包括趨勢和比較
5. AI 識別洞察並提供建議

## 🔒 安全性和多租戶深度解析

我們的實現優先考慮企業級安全性：

### 行級安全性 (RLS)

PostgreSQL RLS 確保數據隔離：

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
- **門店經理 ID**：RLS 上下文的唯一標識符
- **角色分配**：權限和訪問級別
- **會話管理**：安全身份驗證令牌
- **審計日誌**：完整的訪問歷史記錄

### 數據保護

多層安全性：
- **連接加密**：所有數據庫連接使用 TLS
- **防止 SQL 注入**：僅使用參數化查詢
- **輸入驗證**：全面的請求驗證
- **錯誤處理**：錯誤消息中不包含敏感數據

## 🎯 關鍵要點

完成此介紹後，您應該了解：

✅ **MCP 價值主張**：MCP 如何連接 AI 助手和真實世界數據  
✅ **業務背景**：Zava Retail 的需求和挑戰  
✅ **架構概述**：關鍵組件及其交互方式  
✅ **技術堆疊**：使用的工具和框架  
✅ **安全模型**：多租戶數據訪問和保護  
✅ **使用模式**：真實世界查詢場景和工作流程  

## 🚀 下一步

準備深入學習？繼續：

**[實驗 01：核心架構概念](../01-Architecture/README.md)**

了解 MCP 伺服器架構模式、數據庫設計原則以及支持我們零售分析解決方案的詳細技術實現。

## 📚 附加資源

### MCP 文檔
- [MCP 規範](https://modelcontextprotocol.io/docs/) - 官方協議文檔
- [MCP 初學者指南](https://aka.ms/mcp-for-beginners) - 全面的 MCP 學習指南
- [FastMCP 文檔](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 文檔

### 數據庫整合
- [PostgreSQL 文檔](https://www.postgresql.org/docs/) - 完整的 PostgreSQL 參考
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量擴展文檔
- [行級安全性](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服務
- [Azure OpenAI 文檔](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服務整合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 托管數據庫服務
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 無伺服器容器

---

**免責聲明**：這是一個使用虛構零售數據的學習練習。在生產環境中實施類似解決方案時，請始終遵循您組織的數據治理和安全政策。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。
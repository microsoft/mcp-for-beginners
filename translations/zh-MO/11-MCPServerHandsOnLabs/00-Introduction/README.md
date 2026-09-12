# MCP 數據庫整合介紹

> [!NOTE]
> 本學習路徑中的圖表或程式碼若使用 HTTP/SSE 或初始化
> 選項，反映的是範例 MCP `2025-11-25` 依賴版本。對於新的
> 實作，請使用 `2026-07-28` 無狀態請求及 Streamable HTTP。

## 🎯 本實驗室涵蓋內容

本入門實驗室提供建立具有數據庫整合的模型上下文協議 (MCP) 服務器的完整概述。您將透過 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 中的 Zava Retail 零售分析實例，了解商業案例、技術架構及實際應用。

## 概述

**模型上下文協議 (MCP)** 使 AI 助理能即時安全地存取並與外部資料來源互動。結合數據庫整合時，MCP 釋放強大能力，推動資料驅動的 AI 應用。

本學習路徑教您建立可用於生產環境的 MCP 服務器，將 AI 助理連接至 PostgreSQL 的零售銷售數據，並實作企業級模式，如行級安全、多租戶資料存取和語義搜尋。

## 學習目標

完成本實驗後，您將能夠：

- <strong>定義</strong> 模型上下文協議及其數據庫整合的核心優點
- <strong>識別</strong> MCP 服務器架構中與數據庫關鍵元件
- <strong>理解</strong> Zava Retail 使用案例及其商業需求
- <strong>認識</strong> 企業級安全且可擴展的數據庫存取模式
- <strong>列出</strong> 本學習路徑中使用的工具與技術

## 🧭 挑戰：AI 與實際資料的結合

### 傳統 AI 的限制

現代 AI 助理功能強大，但在處理實際商業資料時面臨重要限制：

| <strong>挑戰</strong> | <strong>說明</strong> | <strong>商業影響</strong> |
|---------------|-----------------|-------------------|
| <strong>靜態知識</strong> | AI 模型基於固定資料集訓練，無法存取即時商業資料 | 洞見過時，錯失良機 |
| <strong>數據孤島</strong> | 資訊鎖定於數據庫、API 及系統，AI 無法觸及 | 分析不完整，流程破碎 |
| <strong>安全限制</strong> | 直接存取數據庫牽涉安全與合規顧慮 | 部署受限，人工作業多 |
| <strong>複雜查詢</strong> | 商業使用者需具備技術知識以取得數據洞見 | 採用率低，效率不彰 |

### MCP 解決方案

模型上下文協議透過以下方式解決這些挑戰：

- <strong>即時數據存取</strong>：AI 助理查詢即時數據庫與 API
- <strong>安全整合</strong>：經過授權與權限控管的受控存取
- <strong>自然語言介面</strong>：商業用戶可用英文直接提問
- <strong>標準化協議</strong>：適用於不同 AI 平台與工具

## 🏪 認識 Zava Retail：我們的學習案例 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

在本學習路徑中，我們將為 **Zava Retail** 建置 MCP 服務器，該零售連鎖店為虛構的 DIY 銷售商，擁有多個門市。此真實情境示範企業級 MCP 實作。

### 商業背景

**Zava Retail** 營運：
- **8 家實體店**，遍佈華盛頓州（Seattle、西雅圖、Bellevue、Tacoma、Spokane、Everett、Redmond、Kirkland）
- **1 家網店**，進行電子商務銷售
- <strong>多元產品目錄</strong>，包括工具、五金、園藝用具和建築材料
- <strong>多層級管理結構</strong>：店經理、區域經理與主管

### 商業需求

店經理與主管需要 AI 驅動的分析，以：

1. <strong>分析各門市及時段銷售表現</strong>
2. <strong>追蹤庫存水平及補貨需求</strong>
3. <strong>理解顧客行為及購買模式</strong>
4. <strong>透過語義搜索發掘產品洞見</strong>
5. <strong>用自然語言查詢生成報告</strong>
6. <strong>以角色基礎存取控制維持數據安全</strong>

### 技術需求

MCP 服務器必須提供：

- <strong>多租戶數據存取</strong>：店經理只能看到自身店鋪資料
- <strong>彈性查詢能力</strong>：支援複雜 SQL 操作
- <strong>語義搜尋</strong>：產品發現及推薦
- <strong>即時資料</strong>：反映最新商業狀況
- <strong>安全身份驗證</strong>：結合行級安全 (RLS)
- <strong>可擴展架構</strong>：支援多並發用戶

## 🏗️ MCP 服務器架構總覽

我們的 MCP 服務器採用分層架構，優化數據庫整合：

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

### 關鍵元件

#### **1. MCP 服務器層**
- **FastMCP 框架**：現代 Python MCP 服務器實作
- <strong>工具註冊</strong>：宣告式工具定義並具型別安全
- <strong>請求上下文</strong>：用戶身份及會話管理
- <strong>錯誤處理</strong>：強韌錯誤管理與日誌紀錄

#### **2. 數據庫整合層**
- <strong>連線池</strong>：高效 asyncpg 連接管理
- <strong>結構提供者</strong>：動態資料表結構發現
- <strong>查詢執行器</strong>：帶 RLS 上下文的安全 SQL 執行
- <strong>交易管理</strong>：ACID 合規與回滾處理

#### **3. 安全層**
- <strong>行級安全</strong>：PostgreSQL RLS 提供多租戶資料隔離
- <strong>用戶身份</strong>：店經理認證與授權
- <strong>存取控制</strong>：細粒度權限與稽核軌跡
- <strong>輸入驗證</strong>：防止 SQL 注入與查詢驗證

#### **4. AI 增強層**
- <strong>語義搜尋</strong>：使用向量嵌入進行產品發現
- **Azure OpenAI 整合**：生成文字嵌入
- <strong>相似度演算法</strong>：使用 pgvector 餘弦相似度搜尋
- <strong>搜尋優化</strong>：索引與效能調校

## 🔧 技術堆疊

### 核心技術

| <strong>元件</strong> | <strong>技術</strong> | <strong>用途</strong> |
|---------------|----------------|-------------|
| **MCP 框架** | FastMCP (Python) | 現代 MCP 服務器實作 |
| <strong>數據庫</strong> | PostgreSQL 17 + pgvector | 關聯資料與向量搜尋 |
| **AI 服務** | Azure OpenAI | 文字嵌入及語言模型 |
| <strong>容器化</strong> | Docker + Docker Compose | 開發環境 |
| <strong>雲端平台</strong> | Microsoft Azure | 生產部署 |
| **IDE 整合** | VS Code | AI 聊天及開發流程 |

### 開發工具

| <strong>工具</strong> | <strong>用途</strong> |
|----------|-------------|
| **asyncpg** | 高效能 PostgreSQL 驅動 |
| **Pydantic** | 資料驗證與序列化 |
| **Azure SDK** | 雲端服務整合 |
| **pytest** | 測試框架 |
| **Docker** | 容器化與部署 |

### 生產堆疊

| <strong>服務</strong> | **Azure 資源** | <strong>用途</strong> |
|-------------|-------------------|-------------|
| <strong>數據庫</strong> | Azure Database for PostgreSQL | 托管式數據庫服務 |
| <strong>容器</strong> | Azure Container Apps | 伺服器無伺服器容器主機 |
| **AI 服務** | Microsoft Foundry | OpenAI 模型與端點 |
| <strong>監控</strong> | Application Insights | 可觀察性與診斷 |
| <strong>安全性</strong> | Azure Key Vault | 秘密及配置管理 |

## 🎬 實際使用情境

讓我們來看不同用戶如何與 MCP 服務器互動：

### 情境一：店經理績效評估

<strong>用戶</strong>：Sarah，西雅圖店經理  
<strong>目標</strong>：分析 2024 年第四季銷售績效

<strong>自然語言查詢</strong>：
> 「顯示我店鋪 2024 年第四季前 10 大營收產品」

<strong>發生的事情</strong>：
1. VS Code AI Chat 將查詢發送至 MCP 服務器
2. MCP 服務器識別 Sarah 的店鋪上下文（西雅圖）
3. RLS 政策篩選僅限西雅圖店鋪資料
4. 產生並執行 SQL 查詢
5. 格式化結果返回給 AI Chat
6. AI 提供分析與洞見

### 情境二：語義搜尋進行產品發掘

<strong>用戶</strong>：Mike，庫存經理  
<strong>目標</strong>：找到與顧客需求相似的產品

<strong>自然語言查詢</strong>：
> 「我們賣哪些類似 ‘戶外用防水電氣接頭’ 的產品？」

<strong>發生的事情</strong>：
1. 查詢經由語義搜尋工具處理
2. Azure OpenAI 生成嵌入向量
3. pgvector 執行相似度搜尋
4. 相關產品依關聯度排名
5. 結果含產品細節及庫存狀況
6. AI 建議替代方案與套裝組合

### 情境三：跨店銷售分析

<strong>用戶</strong>：Jennifer，區域經理  
<strong>目標</strong>：比較所有店鋪的業績表現

<strong>自然語言查詢</strong>：
> 「比較過去 6 個月所有店鋪的類別銷售」

<strong>發生的事情</strong>：
1. 為區域經理設定 RLS 上下文存取
2. 產生複雜的多店鋪查詢
3. 從多店鋪位置彙整資料
4. 結果包含趨勢與比較
5. AI 識別洞見與建議

## 🔒 安全性與多租戶深入探討

我們的實作優先考量企業級安全：

### 行級安全 (RLS)

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

每個 MCP 連線包含：
- **店經理 ID**：RLS 上下文唯一標識
- <strong>角色分配</strong>：權限與存取階層
- <strong>會話管理</strong>：安全驗證令牌
- <strong>稽核紀錄</strong>：完整存取歷史

### 資料保護

多層安全防護：
- <strong>連線加密</strong>：所有數據庫連線皆使用 TLS
- **防 SQL 注入**：僅使用參數化查詢
- <strong>輸入驗證</strong>：全面查詢驗證
- <strong>錯誤處理</strong>：錯誤訊息不含敏感資料

## 🎯 主要收穫

完成本介紹後，您應該能理解：

✅ **MCP 價值主張**：MCP 如何橋接 AI 助理與實際資料  
✅ <strong>商業背景</strong>：Zava Retail 的需求與挑戰  
✅ <strong>架構概述</strong>：關鍵元件及其互動  
✅ <strong>技術堆疊</strong>：貫穿全路徑的工具與框架  
✅ <strong>安全模型</strong>：多租戶資料存取與保護  
✅ <strong>使用模式</strong>：真實查詢情境與工作流程  

## 🚀 接下來的步驟

準備深入探討嗎？請繼續：

**[實驗室 01：核心架構概念](../01-Architecture/README.md)**

了解 MCP 服務器架構模式、數據庫設計原理與支持我們零售分析解決方案的詳細技術實作。

## 📚 附加資源

### MCP 文件
- [MCP 規範](https://modelcontextprotocol.io/docs/) - 官方協議文件
- [MCP 新手入門](https://aka.ms/mcp-for-beginners) - 全面 MCP 學習指南
- [FastMCP 文件](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 文件

### 數據庫整合
- [PostgreSQL 文件](https://www.postgresql.org/docs/) - 完整 PostgreSQL 參考
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量擴展文件
- [行級安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服務
- [Azure OpenAI 文件](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服務整合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 托管數據庫服務
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 無伺服器容器

---

<strong>免責聲明</strong>：本為使用虛構零售資料的學習練習。實作類似解決方案於生產環境時，請務必遵守您組織的數據治理及安全政策。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
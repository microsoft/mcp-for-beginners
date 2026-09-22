# MCP 資料庫整合入門

> [!NOTE]
> 本學習路徑中的圖表或程式碼若使用 HTTP/SSE 或初始化選項，
> 均反映範例中的 MCP `2025-11-25` 依賴版本。對於新的實作，
> 請使用 `2026-07-28` 無狀態請求和可串流 HTTP。

## 🎯 本實驗涵蓋內容

本入門實驗將全面介紹如何建置結合資料庫的模型上下文協定（MCP）伺服器。你將透過 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 中的 Zava Retail 零售分析案例，了解商業背景、技術架構與實務應用。

## 概述

**模型上下文協定（MCP）** 使 AI 助理能即時安全地存取並與外部資料來源互動。結合資料庫整合後，MCP 可大幅強化數據驅動的 AI 應用功能。

本學習路徑教你打造可投入生產的 MCP 伺服器，透過 PostgreSQL 將 AI 助理連接至零售銷售數據，實作企業級模式如列級安全、多語義搜尋與多租戶資料存取。

## 學習目標

完成此實驗後，你將能夠：

- <strong>定義</strong> 模型上下文協定及其資料庫整合的核心優勢
- <strong>識別</strong> 搭配資料庫的 MCP 伺服器架構關鍵組件
- <strong>理解</strong> Zava Retail 用例及其商業需求
- <strong>認識</strong> 企業級安全且可擴展資料庫存取模式
- <strong>列出</strong> 本學習路徑所用的工具與技術

## 🧭 挑戰：AI 遇上現實世界資料

### 傳統 AI 限制

現代 AI 助理雖然威力強大，但在處理真實商業數據時仍面臨重大限制：

| <strong>挑戰</strong> | <strong>說明</strong> | <strong>商業影響</strong> |
|---------------|-----------------|-------------------|
| <strong>靜態知識</strong> | AI 模型訓練於固定資料集，無法存取最新商業數據 | 資訊過時，錯失商機 |
| <strong>資料孤島</strong> | 資料鎖定於資料庫、API 及系統，AI 無法觸及 | 分析不完整，流程支離破碎 |
| <strong>安全限制</strong> | 直接存取資料庫提升安全與合規風險 | 部署受限，須人工準備數據 |
| <strong>複雜查詢</strong> | 商業用戶需技術知識以擷取數據洞察 | 採用率低，效率不彰 |

### MCP 解決方案

模型上下文協定透過以下方式解決這些挑戰：

- <strong>即時資料存取</strong>：AI 助理可查詢即時資料庫及 API
- <strong>安全整合</strong>：透過認證與權限控管提供受控存取
- <strong>自然語言介面</strong>：商業用戶以純英文詢問問題
- <strong>標準化協定</strong>：可跨不同 AI 平台與工具運作

## 🏪 認識 Zava Retail：我們的學習案例 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

整個學習路徑中，我們將為 **Zava Retail** 建置 MCP 伺服器。Zava Retail 是一家擁有多家實體門市的虛構 DIY 零售連鎖店。此真實場景展示企業級 MCP 實作。

### 商業背景

**Zava Retail** 運營：
- **8 家實體門市**，遍布華盛頓州（西雅圖、貝爾維尤、塔科馬、斯波坎、埃弗里特、雷德蒙德、柯克蘭）
- **1 處網路商店**，銷售電子商務商品
- <strong>多元產品目錄</strong>，包含工具、硬體、園藝用品及建材
- <strong>多層管理架構</strong>，具備店經理、區域經理及主管

### 商業需求

店經理和主管需要 AI 驅動的分析功能以：

1. <strong>分析各門市與時間段的銷售績效</strong>
2. **追蹤庫存水位，識別補貨需求**
3. <strong>了解顧客行為與購買模式</strong>
4. <strong>透過語義搜尋挖掘商品洞察</strong>
5. <strong>用自然語言查詢產生報告</strong>
6. <strong>以角色基礎存取控制維護資料安全</strong>

### 技術需求

MCP 伺服器需提供：

- <strong>多租戶資料存取</strong>，店經理只能看見所屬門市資料
- <strong>彈性查詢</strong>，支援複雜 SQL 操作
- <strong>語義搜尋</strong>，用於商品發現及推薦
- <strong>即時資料</strong>，反映即時商業狀態
- <strong>安全認證</strong>，結合列級安全保障
- <strong>可擴展架構</strong>，支持多用戶併發

## 🏗️ MCP 伺服器架構概覽

我們的 MCP 伺服器採層級架構設計，針對資料庫整合進行優化：

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

### 主要組件

#### **1. MCP 伺服器層**
- **FastMCP 框架**：現代 Python MCP 伺服器實作
- <strong>工具註冊</strong>：宣告式工具定義，具備型別安全
- <strong>請求上下文</strong>：使用者身份與會話管理
- <strong>錯誤處理</strong>：健全錯誤管理與記錄

#### **2. 資料庫整合層**
- <strong>連線池管理</strong>：高效 asyncpg 連線管理
- **Schema 提供者**：動態資料表結構發現
- <strong>查詢執行器</strong>：結合 RLS 上下文的安全 SQL 執行
- <strong>交易管理</strong>：ACID 合規與回滾處理

#### **3. 安全層**
- **列級安全（RLS）**：PostgreSQL RLS 實現多租戶資料隔離
- <strong>用戶身份</strong>：店經理認證與授權
- <strong>存取控制</strong>：細粒度權限與審計軌跡
- <strong>輸入驗證</strong>：防止 SQL 注入與查詢驗證

#### **4. AI 增強層**
- <strong>語義搜尋</strong>：使用向量嵌入實現商品發現
- **Azure OpenAI 整合**：文字嵌入產生
- <strong>相似度演算法</strong>：pgvector 餘弦相似度搜尋
- <strong>搜尋優化</strong>：索引與效能調校

## 🔧 技術堆疊

### 核心技術

| <strong>組件</strong> | <strong>技術</strong> | <strong>用途</strong> |
|---------------|----------------|-------------|
| **MCP 框架** | FastMCP (Python) | 現代 MCP 伺服器實作 |
| <strong>資料庫</strong> | PostgreSQL 17 + pgvector | 關聯資料與向量搜尋 |
| **AI 服務** | Azure OpenAI | 文字嵌入與語言模型 |
| <strong>容器化</strong> | Docker + Docker Compose | 開發環境 |
| <strong>雲端平台</strong> | Microsoft Azure | 生產部署 |
| **IDE 整合** | VS Code | AI 聊天與開發流程 |

### 開發工具

| <strong>工具</strong> | <strong>用途</strong> |
|----------|-------------|
| **asyncpg** | 高效 PostgreSQL 驅動 |
| **Pydantic** | 資料驗證與序列化 |
| **Azure SDK** | 雲端服務整合 |
| **pytest** | 測試框架 |
| **Docker** | 容器化與部署 |

### 生產堆疊

| <strong>服務</strong> | **Azure 資源** | <strong>用途</strong> |
|-------------|-------------------|-------------|
| <strong>資料庫</strong> | Azure Database for PostgreSQL | 托管資料庫服務 |
| <strong>容器</strong> | Azure Container Apps | 無伺服器容器托管 |
| **AI 服務** | Microsoft Foundry | OpenAI 模型與終端 |
| <strong>監控</strong> | Application Insights | 可觀察性與診斷 |
| <strong>安全</strong> | Azure Key Vault | 秘密與設定管理 |

## 🎬 真實使用情境

讓我們探索不同用戶如何與 MCP 伺服器互動：

### 情境 1：店經理績效檢視

<strong>用戶</strong>：Sarah，西雅圖店經理  
<strong>目標</strong>：分析上一季銷售績效

<strong>自然語言查詢</strong>：
> 「顯示我門市 2024 年第 4 季的營收前 10 名產品」

<strong>流程</strong>：
1. VS Code AI 聊天將查詢送出至 MCP 伺服器
2. MCP 伺服器辨識 Sarah 的門市上下文（西雅圖）
3. RLS 規則過濾資料，僅限西雅圖門市
4. 產生並執行 SQL 查詢
5. 格式化結果回傳給 AI 聊天
6. AI 提供分析與洞察

### 情境 2：語義搜尋商品發現

<strong>用戶</strong>：Mike，庫存經理  
<strong>目標</strong>：尋找與顧客需求相似產品

<strong>自然語言查詢</strong>：
> 「我們販售哪些與『戶外用防水電氣接頭』相似的產品？」

<strong>流程</strong>：
1. 查詢由語義搜尋工具處理
2. Azure OpenAI 產生嵌入向量
3. pgvector 執行相似度搜尋
4. 相關產品依相關性排序
5. 結果含產品細節及庫存狀態
6. AI 建議替代品及組合銷售機會

### 情境 3：跨店分析

<strong>用戶</strong>：Jennifer，區域經理  
<strong>目標</strong>：比對所有門市績效

<strong>自然語言查詢</strong>：
> 「比較過去 6 個月內所有門市的類別銷售」

<strong>流程</strong>：
1. 設定 RLS 上下文，允許區域經理存取
2. 產生複雜多店查詢
3. 跨門市位置彙整資料
4. 結果包含趨勢與比較
5. AI 辨識洞察與建議

## 🔒 安全與多租戶深入探討

我們的實作強調企業級安全：

### 列級安全（RLS）

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

### 使用者身份管理

每個 MCP 連線包含：
- **店經理 ID**：作為 RLS 上下文的唯一識別碼
- <strong>角色分配</strong>：權限與存取層級
- <strong>會話管理</strong>：安全驗證令牌
- <strong>審計記錄</strong>：完整存取歷史

### 資料保護

多層安全措施：
- <strong>連線加密</strong>：所有資料庫連線皆使用 TLS
- **防止 SQL 注入**：僅使用參數化查詢
- <strong>輸入驗證</strong>：全面請求驗證
- <strong>錯誤處理</strong>：錯誤訊息不含敏感資料

## 🎯 重要結論

完成本入門後，你應理解：

✅ **MCP 價值主張**：MCP 如何連結 AI 助理與真實資料  
✅ <strong>商業背景</strong>：Zava Retail 的需求與挑戰  
✅ <strong>架構概覽</strong>：關鍵組件與互動方式  
✅ <strong>技術堆疊</strong>：所使用的工具與框架  
✅ <strong>安全模型</strong>：多租戶資料存取與保護  
✅ <strong>使用模式</strong>：真實查詢場景與工作流程  

## 🚀 下一步

準備深入了解？繼續學習：

**[實驗 01：核心架構概念](../01-Architecture/README.md)**

了解 MCP 伺服器架構模式、資料庫設計原則，以及支撐我們零售分析解決方案的詳細技術實作。

## 📚 其他資源

### MCP 文件
- [MCP 規範](https://modelcontextprotocol.io/docs/) - 官方協定文件
- [MCP 初學者指南](https://aka.ms/mcp-for-beginners) - 全面 MCP 學習手冊
- [FastMCP 文件](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 說明

### 資料庫整合
- [PostgreSQL 文件](https://www.postgresql.org/docs/) - 完整 PostgreSQL 參考資料
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量擴充文件
- [列級安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服務
- [Azure OpenAI 文件](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服務整合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 托管資料庫服務
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 無伺服器容器

---

<strong>免責聲明</strong>：本為學習練習，使用虛構零售數據。請在生產環境實作類似方案時，務必遵循您的組織資料治理與安全政策。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
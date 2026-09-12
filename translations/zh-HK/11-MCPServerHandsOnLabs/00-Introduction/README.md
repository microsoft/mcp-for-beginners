# MCP 數據庫整合入門

> [!NOTE]
> 本學習路徑中使用 HTTP/SSE 或初始化選項的圖表或程式碼反映了範例中 MCP `2025-11-25` 的相依性。對於新實作，請使用 `2026-07-28` 狀態無狀態請求及可串流 HTTP。
> 


## 🎯 本實驗涵蓋內容

本入門實驗提供了搭建結合數據庫整合的模型上下文協定（MCP）伺服器的全面概述。您將透過 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail 中的 Zava Retail 分析案例，了解業務情境、技術架構以及實際應用。

## 概述

**模型上下文協定 (MCP)** 使 AI 助理能夠安全地存取並即時與外部資料源互動。結合數據庫整合，MCP 為資料驅動的 AI 應用釋放強大能力。

本學習路徑教授如何構建可投入生產使用的 MCP 伺服器，透過 PostgreSQL 將 AI 助理連線到零售銷售數據，實現企業範例如行級安全、語義搜尋及多租戶數據存取。

## 學習目標

完成本實驗後，您將能：

- <strong>定義</strong> 模型上下文協定及其數據庫整合的核心優勢
- <strong>識別</strong> MCP 伺服器與數據庫架構的關鍵元件
- <strong>理解</strong> Zava Retail 使用案例及其業務需求
- <strong>辨識</strong> 企業級安全且可擴充的數據庫存取模式
- <strong>列舉</strong> 本學習路徑中使用的工具與技術

## 🧭 挑戰：AI 與現實數據的結合

### 傳統 AI 的限制

現代 AI 助理功能強大，但在處理真實業務數據時，面臨以下重大限制：

| <strong>挑戰</strong> | <strong>描述</strong> | <strong>業務影響</strong> |
|---------------|-----------------|-------------------|
| <strong>靜態知識</strong> | AI 模型基於固定資料集訓練，無法取用最新業務資料 | 洞見過時、錯失商機 |
| <strong>數據孤島</strong> | 資訊鎖定在數據庫、API 及系統中，AI 無法存取 | 分析不完整、流程零散 |
| <strong>安全限制</strong> | 直接存取資料庫帶來安全與合規疑慮 | 部署受限、須手動準備資料 |
| <strong>複雜查詢</strong> | 業務用戶需具備技術知識方能提取數據見解 | 採用率降低、流程效率差 |

### MCP 解決方案

模型上下文協定透過以下方式解決這些挑戰：

- <strong>即時數據存取</strong>：AI 助理查詢即時資料庫與 API
- <strong>安全整合</strong>：透過身份驗證與權限控管控制存取
- <strong>自然語言介面</strong>：業務用戶以簡單英語提問
- <strong>標準化協定</strong>：兼容不同 AI 平台與工具

## 🏪 認識 Zava Retail：本學習案例 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

在本學習路徑中，我們將為 **Zava Retail** 架設 MCP 伺服器，這是一個擁有多個門市的虛構 DIY 零售連鎖。此真實場景示範了企業級 MCP 實作。

### 業務背景

**Zava Retail** 營運：
- **8 間實體店鋪**，分布於華盛頓州（西雅圖、貝爾維尤、塔克馬、斯波坎、埃弗里特、雷德蒙、科克蘭）
- **1 間線上商店**，進行電子商務銷售
- <strong>豐富產品目錄</strong>，含工具、硬體、園藝用品及建築材料
- <strong>多層管理架構</strong>，有店長、區經理及高階主管

### 業務需求

店長及主管需要 AI 助力的分析功能，以：

1. <strong>分析銷售表現</strong>，跨店鋪及不同時間段
2. <strong>追蹤庫存水平</strong>，辨識補貨需求
3. <strong>了解客戶行為</strong>及購物模式
4. <strong>透過語義搜尋</strong> 探索產品見解
5. <strong>以自然語言查詢產生報告</strong>
6. <strong>透過角色基礎存取控制維護資料安全</strong>

### 技術需求

MCP 伺服器必須具備：

- <strong>多租戶資料存取</strong>，店長只能看見自己店鋪資料
- <strong>彈性查詢</strong>，支援複雜 SQL 操作
- <strong>語義搜尋</strong>，用於產品探索與推薦
- <strong>即時數據</strong>，反映當前業務狀況
- <strong>安全認證</strong>，結合行級安全 (RLS)
- <strong>可擴充架構</strong>，支援多用戶併發

## 🏗️ MCP 伺服器架構概覽

我們的 MCP 伺服器實現分層架構，針對數據庫整合優化：

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

### 主要元件

#### **1. MCP 伺服器層**
- **FastMCP 框架**：現代化 Python MCP 伺服器實作
- <strong>工具註冊</strong>：帶型別安全的宣告式工具定義
- <strong>請求上下文</strong>：用戶身份及會話管理
- <strong>錯誤處理</strong>：健全的錯誤管理與記錄

#### **2. 數據庫整合層**
- <strong>連線池管理</strong>：高效 asyncpg 連接管理
- <strong>結構提供者</strong>：動態表結構偵測
- <strong>查詢執行器</strong>：具 RLS 上下文的安全 SQL 執行
- <strong>交易管理</strong>：ACID 合規與回滾處理

#### **3. 安全層**
- <strong>行級安全</strong>：PostgreSQL RLS 實現多租戶資料隔離
- <strong>用戶身份</strong>：店長身份驗證與授權
- <strong>存取控制</strong>：細粒度權限與審計追蹤
- <strong>輸入驗證</strong>：防範 SQL 注入及查詢驗證

#### **4. AI 強化層**
- <strong>語義搜尋</strong>：用於產品探索的向量嵌入
- **Azure OpenAI 整合**：文字嵌入生成
- <strong>相似度算法</strong>：pgvector 餘弦相似搜尋
- <strong>搜尋優化</strong>：索引與效能調校

## 🔧 技術堆疊

### 核心技術

| <strong>元件</strong> | <strong>技術</strong> | <strong>用途</strong> |
|---------------|----------------|-------------|
| **MCP 框架** | FastMCP (Python) | 現代化 MCP 伺服器實作 |
| <strong>數據庫</strong> | PostgreSQL 17 + pgvector | 關聯資料與向量搜尋 |
| **AI 服務** | Azure OpenAI | 文字嵌入與語言模型 |
| <strong>容器化</strong> | Docker + Docker Compose | 開發環境 |
| <strong>雲平台</strong> | Microsoft Azure | 生產部署 |
| **IDE 整合** | VS Code | AI 聊天與開發工作流程 |

### 開發工具

| <strong>工具</strong> | <strong>用途</strong> |
|----------|-------------|
| **asyncpg** | 高效能 PostgreSQL 驅動 |
| **Pydantic** | 數據驗證與序列化 |
| **Azure SDK** | 雲端服務整合 |
| **pytest** | 測試框架 |
| **Docker** | 容器化與部署 |

### 生產堆疊

| <strong>服務</strong> | **Azure 資源** | <strong>用途</strong> |
|-------------|-------------------|-------------|
| <strong>數據庫</strong> | Azure Database for PostgreSQL | 受管數據庫服務 |
| <strong>容器</strong> | Azure Container Apps | 無伺服器容器主機 |
| **AI 服務** | Microsoft Foundry | OpenAI 模型與端點 |
| <strong>監控</strong> | Application Insights | 可觀察性與診斷 |
| <strong>安全</strong> | Azure Key Vault | 機密與設定管理 |

## 🎬 真實使用情境

讓我們探討不同用戶如何與 MCP 伺服器互動：

### 情境 1：店長績效評估

<strong>用戶</strong>：Sarah，西雅圖店店長  
<strong>目標</strong>：分析上一季銷售績效

<strong>自然語言查詢</strong>：
>「顯示我店鋪 2024 年第 4 季營收排名前 10 名的產品」

<strong>發生過程</strong>：
1. VS Code AI 聊天發送查詢到 MCP 伺服器
2. MCP 伺服器識別 Sarah 的店鋪上下文（西雅圖）
3. RLS 政策過濾出僅屬西雅圖店數據
4. 產生並執行 SQL 查詢
5. 格式化結果回傳 AI 聊天
6. AI 進行分析與洞見提供

### 情境 2：產品探索與語義搜尋

<strong>用戶</strong>：Mike，庫存經理  
<strong>目標</strong>：尋找類似客戶需求的產品

<strong>自然語言查詢</strong>：
>「我們販售哪些產品類似『戶外用防水電氣接頭』？」

<strong>發生過程</strong>：
1. 查詢由語義搜尋工具處理
2. Azure OpenAI 生成向量嵌入
3. pgvector 執行相似度搜尋
4. 根據相關性為相關產品排名
5. 結果含產品詳情及庫存狀態
6. AI 建議替代品及組合銷售方案

### 情境 3：跨店鋪分析

<strong>用戶</strong>：Jennifer，區域經理  
<strong>目標</strong>：比較所有店鋪表現

<strong>自然語言查詢</strong>：
>「比較過去 6 個月所有店鋪的品類銷售情況」

<strong>發生過程</strong>：
1. 依區域經理權限設置 RLS 上下文
2. 產生複雜跨店查詢
3. 匯總不同店鋪數據
4. 結果包含趨勢及比較分析
5. AI 提供洞見與建議

## 🔒 安全性與多租戶深入解析

我們的實作重視企業級安全性：

### 行級安全 (RLS)

PostgreSQL 行級安全確保資料隔離：

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
- **店長 ID**：RLS 上下文之唯一識別碼
- <strong>角色分配</strong>：權限與存取層級
- <strong>會話管理</strong>：安全認證令牌
- <strong>稽核紀錄</strong>：完整存取歷史

### 資料保護

多層安全措施：
- <strong>連線加密</strong>：所有資料庫連接皆使用 TLS
- **防範 SQL 注入**：僅使用參數化查詢
- <strong>輸入驗證</strong>：全面請求檢驗
- <strong>錯誤處理</strong>：錯誤訊息不洩露敏感資料

## 🎯 重要心得

完成本入門後，您應理解：

✅ **MCP 價值主張**：MCP 如何串接 AI 助理與現實數據  
✅ <strong>業務背景</strong>：Zava Retail 的需求及挑戰  
✅ <strong>架構概覽</strong>：關鍵元件與其互動  
✅ <strong>技術堆疊</strong>：學習路徑中使用的工具與框架  
✅ <strong>安全模型</strong>：多租戶資料存取與保護  
✅ <strong>使用模式</strong>：實際查詢情境與工作流程  

## 🚀 下一步

準備深入探究？繼續閱讀：

**[Lab 01: 核心架構概念](../01-Architecture/README.md)**

了解 MCP 伺服器架構範式、數據庫設計原則及支撐我們零售分析解決方案的詳細技術實作。

## 📚 延伸資源

### MCP 文件
- [MCP 規範](https://modelcontextprotocol.io/docs/) - 官方協定文件
- [MCP 新手指南](https://aka.ms/mcp-for-beginners) - 全面 MCP 學習指南
- [FastMCP 文檔](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 文件

### 數據庫整合
- [PostgreSQL 文件](https://www.postgresql.org/docs/) - 完整 PostgreSQL 參考資料
- [pgvector 指南](https://github.com/pgvector/pgvector) - 向量擴充文件
- [行級安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 指南

### Azure 服務
- [Azure OpenAI 文件](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 服務整合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 受管數據庫服務
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 無伺服器容器

---

<strong>免責聲明</strong>：本練習使用虛構零售資料。實作類似解決方案於生產環境時，請務必遵循您組織的資料治理及安全政策。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
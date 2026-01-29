# 課程：建立網頁搜尋 MCP 伺服器

本章示範如何打造一個真實世界的 AI 代理，整合外部 API、處理多樣化資料類型、管理錯誤，並協調多個工具——全部以生產環境可用的格式呈現。你將學到：

- **整合需要驗證的外部 API**
- **處理來自多個端點的多樣資料類型**
- **穩健的錯誤處理與日誌策略**
- **在單一伺服器中協調多工具運作**

結束後，你將擁有實務經驗，掌握進階 AI 與大型語言模型（LLM）應用的設計模式與最佳實踐。

## 介紹

本課程將教你如何建立一個進階的 MCP 伺服器與客戶端，利用 SerpAPI 將 LLM 能力擴展至即時網路資料。這是開發能存取最新網路資訊的動態 AI 代理的重要技能。

## 學習目標

完成本課程後，你將能夠：

- 安全地將外部 API（如 SerpAPI）整合到 MCP 伺服器中
- 實作多種工具，涵蓋網頁、新聞、產品搜尋及問答
- 解析並格式化結構化資料，供 LLM 使用
- 有效處理錯誤與管理 API 請求速率限制
- 建立並測試自動化及互動式 MCP 客戶端

## 網頁搜尋 MCP 伺服器

本節介紹網頁搜尋 MCP 伺服器的架構與功能。你將看到 FastMCP 與 SerpAPI 如何結合，將 LLM 能力擴展至即時網路資料。

### 概覽

此實作包含四個工具，展示 MCP 安全且高效處理多樣外部 API 任務的能力：

- **general_search**：廣泛的網頁搜尋結果
- **news_search**：最新新聞標題
- **product_search**：電子商務產品資料
- **qna**：問答摘要

### 功能
- **程式碼範例**：包含針對 Python 的語言特定程式碼區塊（並可輕鬆擴展至其他語言），使用程式碼切換以提高清晰度

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

在執行客戶端前，了解伺服器的運作很有幫助。[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 檔案實作了 MCP 伺服器，透過整合 SerpAPI，提供網頁、新聞、產品搜尋及問答工具。它負責處理進來的請求、管理 API 呼叫、解析回應，並將結構化結果回傳給客戶端。

你可以查看 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 的完整實作。

以下是伺服器如何定義並註冊工具的簡短範例：

### Python 伺服器

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **外部 API 整合**：示範如何安全處理 API 金鑰與外部請求
- **結構化資料解析**：展示如何將 API 回應轉換為 LLM 友善格式
- **錯誤處理**：具備完善的錯誤處理與適當的日誌紀錄
- **互動式客戶端**：包含自動化測試與互動模式供測試使用
- **上下文管理**：利用 MCP Context 進行日誌與請求追蹤

## 先決條件

開始前，請確保你的環境已正確設定，依照以下步驟安裝所有相依套件並配置 API 金鑰，確保開發與測試順利進行。

- Python 3.8 或以上版本
- SerpAPI API 金鑰（可於 [SerpAPI](https://serpapi.com/) 註冊，提供免費方案）

## 安裝

請依照以下步驟設定你的環境：

1. 使用 uv（推薦）或 pip 安裝相依套件：

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. 在專案根目錄建立 `.env` 檔案，填入你的 SerpAPI 金鑰：

```
SERPAPI_KEY=your_serpapi_key_here
```

## 使用說明

網頁搜尋 MCP 伺服器是核心元件，透過整合 SerpAPI，提供網頁、新聞、產品搜尋及問答工具。它負責處理請求、管理 API 呼叫、解析回應，並回傳結構化結果給客戶端。

你可以查看 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 的完整實作。

### 啟動伺服器

使用以下指令啟動 MCP 伺服器：

```bash
python server.py
```

伺服器將以 stdio 為基礎運行，客戶端可直接連線。

### 客戶端模式

客戶端（`client.py`）支援兩種與 MCP 伺服器互動的模式：

- **一般模式**：執行自動化測試，涵蓋所有工具並驗證回應。適合快速檢查伺服器與工具是否正常運作。
- **互動模式**：啟動選單介面，讓你手動選擇並呼叫工具，輸入自訂查詢，並即時查看結果。適合探索伺服器功能與嘗試不同輸入。

你可以查看 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) 的完整實作。

### 執行客戶端

執行自動化測試（會自動啟動伺服器）：

```bash
python client.py
```

或以互動模式執行：

```bash
python client.py --interactive
```

### 使用不同方式測試

根據需求與工作流程，有多種方式測試與互動伺服器提供的工具。

#### 使用 MCP Python SDK 撰寫自訂測試腳本
你也可以利用 MCP Python SDK 撰寫自己的測試腳本：

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

在此情境中，「測試腳本」指的是你撰寫的自訂 Python 程式，作為 MCP 伺服器的客戶端。它不是正式的單元測試，而是讓你程式化連線伺服器、以自訂參數呼叫任一工具並檢視結果。這種方式適合：

- 原型設計與工具呼叫實驗
- 驗證伺服器對不同輸入的回應
- 自動化重複工具呼叫
- 在 MCP 伺服器上建立自訂工作流程或整合

你可以用測試腳本快速嘗試新查詢、除錯工具行為，甚至作為更進階自動化的起點。以下是使用 MCP Python SDK 建立此類腳本的範例：

## 工具說明

伺服器提供以下工具，供你執行不同類型的搜尋與查詢。每個工具的參數與範例用法如下。

本節詳述各工具及其參數。

### general_search

執行一般網頁搜尋並回傳格式化結果。

**如何呼叫此工具：**

你可以使用 MCP Python SDK 從自己的腳本呼叫 `general_search`，或在 Inspector 或互動式客戶端模式中操作。以下是 SDK 的程式碼範例：

# [Python 範例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

或在互動模式中，從選單選擇 `general_search`，並在提示時輸入查詢。

**參數：**
- `query`（字串）：搜尋查詢字串

**範例請求：**

```json
{
  "query": "latest AI trends"
}
```

### news_search

搜尋與查詢相關的最新新聞文章。

**如何呼叫此工具：**

你可以使用 MCP Python SDK 從自己的腳本呼叫 `news_search`，或在 Inspector 或互動式客戶端模式中操作。以下是 SDK 的程式碼範例：

# [Python 範例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

或在互動模式中，從選單選擇 `news_search`，並在提示時輸入查詢。

**參數：**
- `query`（字串）：搜尋查詢字串

**範例請求：**

```json
{
  "query": "AI policy updates"
}
```

### product_search

搜尋符合查詢的產品。

**如何呼叫此工具：**

你可以使用 MCP Python SDK 從自己的腳本呼叫 `product_search`，或在 Inspector 或互動式客戶端模式中操作。以下是 SDK 的程式碼範例：

# [Python 範例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

或在互動模式中，從選單選擇 `product_search`，並在提示時輸入查詢。

**參數：**
- `query`（字串）：產品搜尋查詢字串

**範例請求：**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

從搜尋引擎取得問題的直接答案。

**如何呼叫此工具：**

你可以使用 MCP Python SDK 從自己的腳本呼叫 `qna`，或在 Inspector 或互動式客戶端模式中操作。以下是 SDK 的程式碼範例：

# [Python 範例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

或在互動模式中，從選單選擇 `qna`，並在提示時輸入問題。

**參數：**
- `question`（字串）：欲尋找答案的問題

**範例請求：**

```json
{
  "question": "what is artificial intelligence"
}
```

## 程式碼細節

本節提供伺服器與客戶端實作的程式碼片段與參考。

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

完整實作請參考 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 與 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)。

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## 本課程的進階概念

開始建置前，這裡介紹本章將會出現的重要進階概念。理解這些有助於你跟上內容，即使你對它們不熟悉：

- **多工具協調**：指在單一 MCP 伺服器中同時運行多種工具（如網頁搜尋、新聞搜尋、產品搜尋與問答）。這讓伺服器能處理多元任務，而非單一功能。
- **API 請求速率限制管理**：許多外部 API（如 SerpAPI）限制一定時間內的請求數量。良好的程式會檢查這些限制並妥善處理，避免應用程式因超限而崩潰。
- **結構化資料解析**：API 回應通常複雜且巢狀。此概念指將回應轉換成乾淨、易用的格式，方便 LLM 或其他程式使用。
- **錯誤復原**：有時會發生問題，例如網路故障或 API 回應異常。錯誤復原讓程式能處理這些狀況，並提供有用回饋，而非直接崩潰。
- **參數驗證**：檢查工具輸入是否正確且安全，包括設定預設值與確保型別正確，有助於避免錯誤與混淆。

本節將協助你診斷並解決使用網頁搜尋 MCP 伺服器時常見的問題。遇到錯誤或異常行為時，先參考此故障排除章節，通常能快速解決問題。

## 故障排除

使用網頁搜尋 MCP 伺服器時，偶爾會遇到問題——這在開發外部 API 與新工具時很常見。本節提供最常見問題的實用解決方案，幫助你快速回到正軌。遇到錯誤時，請先從這裡開始：以下建議針對大多數使用者遇到的問題，通常能在不需額外協助下解決。

### 常見問題

以下列出使用者最常遇到的問題，並附上清楚說明與解決步驟：

1. **.env 檔案缺少 SERPAPI_KEY**
   - 若出現錯誤 `SERPAPI_KEY environment variable not found`，表示應用程式找不到存取 SerpAPI 所需的 API 金鑰。解決方法是在專案根目錄建立 `.env` 檔案（若尚未存在），並加入類似 `SERPAPI_KEY=your_serpapi_key_here` 的一行。請將 `your_serpapi_key_here` 替換成你從 SerpAPI 網站取得的實際金鑰。

2. **找不到模組錯誤**
   - 如 `ModuleNotFoundError: No module named 'httpx'` 表示缺少必要的 Python 套件。通常是因為尚未安裝所有相依套件。請在終端機執行 `pip install -r requirements.txt`，安裝專案所需的所有套件。

3. **連線問題**
   - 若出現 `Error during client execution`，通常表示客戶端無法連接伺服器，或伺服器未正常運行。請確認客戶端與伺服器版本相容，且 `server.py` 存在且在正確目錄中運行。重新啟動伺服器與客戶端也常有幫助。

4. **SerpAPI 錯誤**
   - 若看到 `Search API returned error status: 401`，表示你的 SerpAPI 金鑰缺失、錯誤或已過期。請前往 SerpAPI 控制台確認金鑰，並更新 `.env` 檔案。若金鑰正確但仍出錯，請檢查免費方案配額是否已用盡。

### 除錯模式

預設情況下，應用程式只記錄重要資訊。若想查看更詳細的執行過程（例如診斷棘手問題），可啟用 DEBUG 模式。這會顯示更多關於每個步驟的細節。

**範例：一般輸出**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**範例：DEBUG 輸出**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

注意 DEBUG 模式會額外顯示 HTTP 請求、回應及其他內部細節，對故障排除非常有幫助。
要啟用 DEBUG 模式，請在你的 `client.py` 或 `server.py` 頂部將日誌等級設為 DEBUG：

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## 下一步

- [5.10 實時串流](../mcp-realtimestreaming/README.md)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
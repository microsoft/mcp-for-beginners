# Model Context Protocol (MCP) Python 實作

此倉庫包含 Model Context Protocol (MCP) 的 Python 實作，示範如何建立同時支援 MCP 標準的伺服器與客戶端應用程式。

## 概覽

MCP 實作包含兩個主要部分：

1. **MCP 伺服器 (`server.py`)** - 一個提供以下功能的伺服器：
   - **工具**：可遠端呼叫的函式
   - **資源**：可取得的資料
   - **提示**：用於產生語言模型提示的範本

2. **MCP 客戶端 (`client.py`)** - 連接伺服器並使用其功能的客戶端應用程式

## 功能

此實作展示了多項 MCP 的核心功能：

### 工具
- `completion` - 從 AI 模型產生文字補全（模擬）
- `add` - 簡單的加法計算器，將兩個數字相加

### 資源
- `models://` - 回傳可用 AI 模型的資訊
- `greeting://{name}` - 根據指定名稱回傳個人化問候語

### 提示
- `review_code` - 產生用於程式碼審查的提示範本

## 安裝

使用此 MCP 實作前，請先安裝所需套件：

```powershell
pip install mcp-server mcp-client
```

## 啟動伺服器與客戶端

### 啟動伺服器

在一個終端機視窗中執行伺服器：

```powershell
python server.py
```

也可以使用 MCP CLI 以開發模式啟動伺服器：

```powershell
mcp dev server.py
```

或安裝到 Claude Desktop（若有支援）：

```powershell
mcp install server.py
```

### 執行客戶端

在另一個終端機視窗中執行客戶端：

```powershell
python client.py
```

這會連接到伺服器並展示所有可用功能。

### 客戶端使用說明

客戶端 (`client.py`) 展示了所有 MCP 功能：

```powershell
python client.py
```

這會連接伺服器並測試所有功能，包括工具、資源和提示。輸出將顯示：

1. 計算器工具結果（5 + 7 = 12）
2. 對「What is the meaning of life?」的 completion 工具回應
3. 可用 AI 模型清單
4. 「MCP Explorer」的個人化問候語
5. 程式碼審查提示範本

## 實作細節

伺服器是使用 `FastMCP` API 實作，該 API 提供定義 MCP 服務的高階抽象。以下是定義工具的簡化範例：

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

客戶端使用 MCP 客戶端函式庫連接並呼叫伺服器：

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## 進一步了解

欲了解更多 MCP 資訊，請造訪：https://modelcontextprotocol.io/

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
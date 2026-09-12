# MCP 中的分頁與大型結果集

當您的 MCP 伺服器處理大量資料集時 - 無論是列出成千上萬個檔案、資料庫紀錄或搜尋結果 - 都需要分頁來有效管理記憶體並提供快速回應的使用者體驗。本指南涵蓋如何在 MCP 中實作與使用分頁功能。

## 為什麼分頁很重要

若沒有分頁，大量回應可能導致：

- <strong>記憶體耗盡</strong> - 一次載入數百萬筆紀錄
- <strong>回應時間遲緩</strong> - 使用者需等待所有資料載入完成
- <strong>逾時錯誤</strong> - 請求超過逾時限制
- **AI 性能不佳** - 大型語言模型難以處理龐大上下文

MCP 採用 <strong>基於游標的分頁</strong> 以可靠且一致地瀏覽結果集。

---

## MCP 分頁的運作方式

### 游標概念

<strong>游標</strong> 是一個不透明的字串，用來標記您在結果集中的位置。就像長篇書籍裡的書籤。

```mermaid
sequenceDiagram
    participant Client
    participant Server
    
    Client->>Server: 工具/列表（無游標）
    Server-->>Client: 工具 [1-10]，下一個游標："abc123"
    
    Client->>Server: 工具/列表（游標："abc123"）
    Server-->>Client: 工具 [11-20]，下一個游標："def456"
    
    Client->>Server: 工具/列表（游標："def456"）
    Server-->>Client: 工具 [21-25]，下一個游標：null（結束）
```

### MCP 方法中的分頁

以下這些 MCP 方法支援分頁：

| 方法 | 回傳 | 支援游標 |
|--------|---------|----------------|
| `tools/list` | 工具定義 | ✅ |
| `resources/list` | 資源定義 | ✅ |
| `prompts/list` | 提示定義 | ✅ |
| `resources/templates/list` | 資源範本 | ✅ |

---

## 伺服器實作

### Python (FastMCP)

```python
from mcp.server import Server
from mcp.types import Tool, ListToolsResult
import math

app = Server("paginated-server")

# 模擬大型數據集
ALL_TOOLS = [
    Tool(name=f"tool_{i}", description=f"Tool number {i}", inputSchema={})
    for i in range(100)
]

PAGE_SIZE = 10

@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    """List tools with pagination support."""
    
    # 解碼游標以獲取起始索引
    start_index = 0
    if cursor:
        try:
            start_index = int(cursor)
        except ValueError:
            start_index = 0
    
    # 獲取結果頁面
    end_index = min(start_index + PAGE_SIZE, len(ALL_TOOLS))
    page_tools = ALL_TOOLS[start_index:end_index]
    
    # 計算下一個游標
    next_cursor = None
    if end_index < len(ALL_TOOLS):
        next_cursor = str(end_index)
    
    return ListToolsResult(
        tools=page_tools,
        nextCursor=next_cursor
    )
```

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { ListToolsResultSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server({
  name: "paginated-server",
  version: "1.0.0"
});

// 模擬大型資料集
const ALL_TOOLS = Array.from({ length: 100 }, (_, i) => ({
  name: `tool_${i}`,
  description: `Tool number ${i}`,
  inputSchema: { type: "object", properties: {} }
}));

const PAGE_SIZE = 10;

server.setRequestHandler(ListToolsResultSchema, async (request) => {
  // 解碼游標
  let startIndex = 0;
  if (request.params?.cursor) {
    startIndex = parseInt(request.params.cursor, 10) || 0;
  }
  
  // 獲取結果頁面
  const endIndex = Math.min(startIndex + PAGE_SIZE, ALL_TOOLS.length);
  const pageTools = ALL_TOOLS.slice(startIndex, endIndex);
  
  // 計算下一個游標
  const nextCursor = endIndex < ALL_TOOLS.length ? String(endIndex) : undefined;
  
  return {
    tools: pageTools,
    nextCursor
  };
});
```

### Java (Spring MCP)

```java
@Service
public class PaginatedToolService {
    
    private static final int PAGE_SIZE = 10;
    private final List<Tool> allTools;
    
    public PaginatedToolService() {
        // 初始化大型資料集
        this.allTools = IntStream.range(0, 100)
            .mapToObj(i -> new Tool("tool_" + i, "Tool number " + i, Map.of()))
            .collect(Collectors.toList());
    }
    
    @McpMethod("tools/list")
    public ListToolsResult listTools(@Param("cursor") String cursor) {
        // 解碼游標
        int startIndex = 0;
        if (cursor != null && !cursor.isEmpty()) {
            try {
                startIndex = Integer.parseInt(cursor);
            } catch (NumberFormatException e) {
                startIndex = 0;
            }
        }
        
        // 取得結果頁面
        int endIndex = Math.min(startIndex + PAGE_SIZE, allTools.size());
        List<Tool> pageTools = allTools.subList(startIndex, endIndex);
        
        // 計算下一個游標
        String nextCursor = endIndex < allTools.size() ? String.valueOf(endIndex) : null;
        
        return new ListToolsResult(pageTools, nextCursor);
    }
}
```

---

## 用戶端實作

### Python 用戶端

```python
from mcp import ClientSession

async def get_all_tools(session: ClientSession) -> list:
    """Fetch all tools using pagination."""
    all_tools = []
    cursor = None
    
    while True:
        result = await session.list_tools(cursor=cursor)
        all_tools.extend(result.tools)
        
        if result.nextCursor is None:
            break
        cursor = result.nextCursor
    
    return all_tools

# 使用方法
async with client_session as session:
    tools = await get_all_tools(session)
    print(f"Found {len(tools)} tools")
```

### TypeScript 用戶端

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";

async function getAllTools(client: Client): Promise<Tool[]> {
  const allTools: Tool[] = [];
  let cursor: string | undefined = undefined;
  
  do {
    const result = await client.listTools({ cursor });
    allTools.push(...result.tools);
    cursor = result.nextCursor;
  } while (cursor);
  
  return allTools;
}

// 使用方法
const tools = await getAllTools(client);
console.log(`Found ${tools.length} tools`);
```

### 延遲載入模式

對於非常大型的資料集，按需載入頁面：

```python
class PaginatedToolIterator:
    """Lazily iterate through paginated tools."""
    
    def __init__(self, session: ClientSession):
        self.session = session
        self.cursor = None
        self.buffer = []
        self.exhausted = False
    
    async def __anext__(self):
        # 如果可用，從緩衝區返回
        if self.buffer:
            return self.buffer.pop(0)
        
        # 檢查是否已經讀取所有頁面
        if self.exhausted:
            raise StopAsyncIteration
        
        # 取得下一頁
        result = await self.session.list_tools(cursor=self.cursor)
        self.buffer = list(result.tools)
        self.cursor = result.nextCursor
        
        if self.cursor is None:
            self.exhausted = True
        
        if not self.buffer:
            raise StopAsyncIteration
        
        return self.buffer.pop(0)
    
    def __aiter__(self):
        return self

# 用法 - 對大型數據集的記憶體效率高
async for tool in PaginatedToolIterator(session):
    process_tool(tool)
```

---

## 資源分頁

資源通常需要為目錄或大型資料集實作分頁：

```python
from mcp.server import Server
from mcp.types import Resource, ListResourcesResult
import os

app = Server("file-server")

@app.list_resources()
async def list_resources(cursor: str | None = None) -> ListResourcesResult:
    """List files in directory with pagination."""
    
    directory = "/data/files"
    all_files = sorted(os.listdir(directory))
    
    # 解碼游標（檔案索引）
    start_index = int(cursor) if cursor else 0
    page_size = 20
    end_index = min(start_index + page_size, len(all_files))
    
    # 為此頁面建立資源清單
    resources = []
    for filename in all_files[start_index:end_index]:
        filepath = os.path.join(directory, filename)
        resources.append(Resource(
            uri=f"file://{filepath}",
            name=filename,
            mimeType="application/octet-stream"
        ))
    
    # 計算下一個游標
    next_cursor = str(end_index) if end_index < len(all_files) else None
    
    return ListResourcesResult(
        resources=resources,
        nextCursor=next_cursor
    )
```

---

## 游標設計策略

### 策略 1：基於索引 (簡單)

```python
# 游標只是索引
cursor = "50"  # 從第 50 個項目開始
```

**優點：** 簡單、無狀態
**缺點：** 如果新增或刪除項目，結果可能會變動

### 策略 2：基於 ID (穩定)

```python
# Cursor 是最後看到的 ID
cursor = "item_abc123"  # 從這個項目之後開始
```

**優點：** 即使項目變動也穩定
**缺點：** 需要有序的 ID

### 策略 3：編碼狀態 (複雜)

```python
import base64
import json

def encode_cursor(state: dict) -> str:
    return base64.b64encode(json.dumps(state).encode()).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(base64.b64decode(cursor).decode())

# 游標包含多個狀態欄位
cursor = encode_cursor({
    "offset": 50,
    "filter": "active",
    "sort": "name"
})
```

**優點：** 可編碼複雜狀態
**缺點：** 較複雜，游標字串較大

---

## 最佳實踐

### 1. 選擇適當的頁面大小

```python
# 考慮資料大小
PAGE_SIZE_SMALL_ITEMS = 100   # 簡單的元資料
PAGE_SIZE_MEDIUM_ITEMS = 20   # 更豐富的物件
PAGE_SIZE_LARGE_ITEMS = 5     # 複雜的內容
```

### 2. 優雅處理無效游標

```python
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    try:
        start_index = int(cursor) if cursor else 0
        if start_index < 0 or start_index >= len(ALL_TOOLS):
            start_index = 0  # 重置到開始
    except (ValueError, TypeError):
        start_index = 0  # 無效的游標，重新開始
    # ...
```

### 3. 包含總數量（可選）

```python
return ListToolsResult(
    tools=page_tools,
    nextCursor=next_cursor,
    # 某些實作包含用於使用者介面進度的總數
    _meta={"total": len(ALL_TOOLS)}
)
```

### 4. 測試邊界情況

```python
async def test_pagination():
    # 空結果集
    result = await session.list_tools()
    assert result.tools == []
    assert result.nextCursor is None
    
    # 單頁
    result = await session.list_tools()
    assert len(result.tools) <= PAGE_SIZE
    
    # 無效的游標
    result = await session.list_tools(cursor="invalid")
    assert result.tools  # 應該返回第一頁
```

---

## 常見陷阱

### ❌ 回傳所有結果後再於客戶端分頁

```python
# 不好：將所有東西載入記憶體中
@app.list_tools()
async def list_tools() -> ListToolsResult:
    all_tools = load_all_tools()  # 100萬個工具！
    return ListToolsResult(tools=all_tools)
```

### ✅ 於資料源端分頁

```python
# 良好：只載入需要的部分
@app.list_tools()
async def list_tools(cursor: str | None = None) -> ListToolsResult:
    offset = int(cursor) if cursor else 0
    tools = await db.query_tools(offset=offset, limit=PAGE_SIZE)
    return ListToolsResult(tools=tools, nextCursor=...)
```

---

## 下一步

- [模組 5.14 - 上下文工程](../../05-AdvancedTopics/mcp-contextengineering/README.md)
- [模組 8 - 最佳實踐](../../08-BestPractices/README.md)
- [3.8 - 測試您的 MCP 伺服器](../../03-GettingStarted/08-testing/README.md)

---

## 額外資源

- [MCP 規範 - 分頁](https://modelcontextprotocol.io/specification/2026-07-28/)
- [基於游標的分頁詳解](https://slack.engineering/evolving-api-pagination-at-slack/)
- [Python SDK 分頁測試](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
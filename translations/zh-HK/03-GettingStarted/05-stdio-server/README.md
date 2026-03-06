# MCP 伺服器與 stdio 傳輸

> **⚠️ 重要更新**：根據 MCP 規範 2025-06-18，獨立的 SSE（伺服器推送事件）傳輸已被**棄用**，並被「可串流 HTTP」傳輸取代。目前 MCP 規範定義了兩種主要傳輸機制：
> 1. **stdio** - 標準輸入/輸出（推薦用於本地伺服器）
> 2. **可串流 HTTP** - 適用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新為聚焦於**stdio 傳輸**，這是大多數 MCP 伺服器實作所推薦的做法。

stdio傳輸允許 MCP 伺服器透過標準輸入和輸出串流與用戶端通訊。這是在目前 MCP 規範中最常用且推薦的傳輸機制，提供簡單且高效的方式來構建 MCP 伺服器，能輕鬆整合各種客戶端應用程式。

## 概覽

本課程涵蓋如何使用 stdio 傳輸來建立和使用 MCP 伺服器。

## 學習目標

完成本課程後，你將能夠：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 除錯 MCP 伺服器。
- 在 Visual Studio Code 中使用 MCP 伺服器。
- 理解目前的 MCP 傳輸機制及為何推薦使用 stdio。

## stdio 傳輸 - 運作方式

stdio 傳輸是當前 MCP 規範（2025-06-18）支援的兩種傳輸類型之一。其運作方式如下：

- **簡單通訊**：伺服器從標準輸入 (`stdin`) 讀取 JSON-RPC 訊息，並將訊息發送至標準輸出 (`stdout`)。
- **基於程序**：用戶端將 MCP 伺服器當作子程序啟動。
- **訊息格式**：訊息為獨立的 JSON-RPC 請求、通知或回應，以換行符分隔。
- **日誌紀錄**：伺服器可選擇將 UTF-8 字串寫入標準錯誤輸出 (`stderr`) 作為日誌。

### 主要要求：
- 訊息必須以換行符分隔，且不得包含內嵌換行符
- 伺服器不得於 `stdout` 輸出非有效 MCP 訊息
- 用戶端不得於伺服器的 `stdin` 輸入非有效 MCP 訊息

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

在上述程式碼中：

- 我們從 MCP SDK 載入 `Server` 類別及 `StdioServerTransport`
- 以基本設定和功能建立伺服器實例

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 建立伺服器實例
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

在上述程式碼中，我們：

- 使用 MCP SDK 建立伺服器實例
- 使用裝飾器定義工具
- 使用 stdio_server 上下文管理器處理傳輸

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

與 SSE 主要的不同在於 stdio 伺服器：

- 不需 Web 伺服器設置或 HTTP 端點
- 由用戶端啟動為子程序
- 使用 stdin/stdout 串流通訊
- 實作與除錯較簡單

## 練習：建立 stdio 伺服器

建立伺服器時，我們需記住兩件事：

- 需要使用 Web 伺服器曝光連線及訊息端點。
## 實驗實作：建立簡單 MCP stdio 伺服器

本實作中，我們將使用推薦的 stdio 傳輸建立簡單 MCP 伺服器。該伺服器將曝光可供客戶端呼叫的工具，使用標準 Model Context Protocol。

### 前置需求

- Python 3.8 或更新版本
- MCP Python SDK：`pip install mcp`
- 基本異步程式設計知識

開始建立我們的第一個 MCP stdio 伺服器：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 建立伺服器
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # 使用 stdio 傳輸
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 與已棄用 SSE 方法的主要差異

**Stdio 傳輸（目前標準）：**
- 簡單子程序模式 - 用戶端啟動伺服器為子程序
- 透過 stdin/stdout 傳輸 JSON-RPC 訊息
- 無需設置 HTTP 伺服器
- 更佳效能與安全性
- 除錯與開發更容易

**SSE 傳輸（自 MCP 2025-06-18 起棄用）：**
- 需要 HTTP 伺服器並且有 SSE 端點
- 複雜的 Web 伺服器架構配置
- HTTP 端點的額外安全考量
- 現由可串流 HTTP 替代適用於 Web 場景

### 建立 stdio 傳輸伺服器

為了建立 stdio 伺服器，我們需要：

1. **匯入必要函式庫** - MCP 伺服器元件與 stdio 傳輸
2. **建立伺服器實例** - 定義伺服器及其能力
3. **定義工具** - 加入欲暴露的功能
4. **設定傳輸** - 配置 stdio 通訊
5. **啟動伺服器** - 啟動並處理訊息

一起逐步建構：

### 步驟 1：建立基礎 stdio 伺服器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 建立伺服器
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 步驟 2：加入更多工具

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### 步驟 3：啟動伺服器

將程式碼儲存為 `server.py`，並在命令列執行：

```bash
python server.py
```

伺服器會啟動並等待從 stdin 輸入。它將透過 stdio 傳輸以 JSON-RPC 訊息通訊。

### 步驟 4：使用 Inspector 測試

你可以使用 MCP Inspector 測試你的伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 啟動 Inspector 並指向你的伺服器
3. 測試你建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 除錯你的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是用於除錯與測試 MCP 伺服器的重要工具。以下是如何用它來測試 stdio 伺服器：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **測試伺服器**：Inspector 提供網頁介面，你可以：
   - 查看伺服器功能
   - 使用不同參數測試工具
   - 監控 JSON-RPC 訊息
   - 除錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 除錯 MCP 伺服器：

1. 在 `.vscode/launch.json` 建立執行組態：
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. 在伺服器程式碼中設定斷點
3. 啟動除錯並使用 Inspector 測試

### 常見除錯技巧

- 使用 `stderr` 記錄日誌 - 不要在 `stdout` 輸出非 MCP 訊息
- 確保所有 JSON-RPC 訊息均以換行符分隔
- 先用簡單工具測試，再增加複雜功能
- 使用 Inspector 驗證訊息格式

## 在 VS Code 使用你的 stdio 伺服器

當你完成 MCP stdio 伺服器建置後，可以將其整合進 VS Code，以搭配 Claude 或其他相容 MCP 的客戶端使用。

### 配置

1. **建立 MCP 設定檔**，路徑為 `%APPDATA%\Claude\claude_desktop_config.json` (Windows) 或 `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)：

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **重啟 Claude**：關閉並重新開啟 Claude，載入新伺服器設定。

3. **測試連線**：與 Claude 開始對話，嘗試使用你的伺服器工具：
   - 「你可以用問候工具跟我打招呼嗎？」
   - 「計算 15 與 27 的總和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

這裡有完整的 TypeScript 範例供參考：

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 新增工具
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio 伺服器範例

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 小結

在本更新課程中，你學會如何：

- 使用目前推薦的 **stdio 傳輸** 建立 MCP 伺服器
- 理解 SSE 為何被棄用，取而代之的是 stdio 和可串流 HTTP
- 建立能讓 MCP 用戶端呼叫的工具
- 使用 MCP Inspector 除錯伺服器
- 將 stdio 伺服器整合至 VS Code 與 Claude

與已棄用的 SSE 方法相比，stdio 傳輸提供更簡易、更安全且效能更佳的 MCP 伺服器建置方式。根據 2025-06-18 規範，它是大多數 MCP 伺服器實作所推薦的傳輸機制。

### .NET

1. 不妨先建立一些工具，為此我們將建立一個名為 *Tools.cs* 的檔案，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試你的 stdio 伺服器

現在你已建置完成 stdio 伺服器，讓我們來測試確認其正常運作。

### 前置需求

1. 確認已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 已將伺服器程式碼儲存（例如為 `server.py`）

### 使用 Inspector 進行測試

1. **啟動 Inspector 與伺服器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **開啟網頁介面**：Inspector 將啟動瀏覽器視窗顯示伺服器功能。

3. **測試工具**： 
   - 嘗試 `get_greeting` 工具，使用不同姓名
   - 測試 `calculate_sum` 工具，輸入各種數字
   - 呼叫 `get_server_info` 工具，查看伺服器元資料

4. **監控通訊**：Inspector 顯示用戶端與伺服器間交換的 JSON-RPC 訊息。

### 你會看到什麼

當伺服器正確啟動時，你應該會看到：
- Inspector 中列出的伺服器功能
- 可供測試的工具
- 成功的 JSON-RPC 訊息交換
- 工具回應會顯示在介面中

### 常見問題及解決方法

**伺服器無法啟動：**
- 檢查所有相依套件是否已安裝：`pip install mcp`
- 確認 Python 語法及縮排正確
- 觀察主控台錯誤訊息

**工具未出現：**
- 確保存在 `@server.tool()` 裝飾器
- 確認工具函式在 `main()` 執行前已定義
- 確保伺服器正確設定

**連線問題：**
- 確認伺服器正確使用 stdio 傳輸
- 檢查是否有其他程序干擾
- 驗證 Inspector 指令語法是否正確

## 作業

嘗試擴展你的伺服器，新增更多功能。參考[此頁面](https://api.chucknorris.io/)來增加調用 API 的工具。由你決定伺服器的樣貌。祝你玩得開心 :)

## 解答

[解答](./solution/README.md) 這是一個可能可運作的實作範例。

## 主要重點

本章的主要重點如下：

- stdio 傳輸是本地 MCP 伺服器推薦的通訊機制。
- stdio 傳輸允許 MCP 伺服器與用戶端利用標準輸入輸出流無縫通訊。
- 你可以使用 Inspector 與 Visual Studio Code 直接使用 stdio 伺服器，使除錯與整合更為簡單。

## 範例 

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python) 

## 額外資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 下一步

## 後續步驟

學習了如何使用 stdio 傳輸構建 MCP 伺服器後，你可以探索更進階的主題：

- **下一步**：[MCP 的 HTTP 串流（可串流 HTTP）](../06-http-streaming/README.md) - 了解遠端伺服器支援的另一種傳輸機制
- **進階**：[MCP 安全最佳實踐](../../02-Security/README.md) - 在 MCP 伺服器中實作安全性
- **生產環境**：[部署策略](../09-deployment/README.md) - 如何部署伺服器供正式使用

## 額外資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言的 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 更多社群提供的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件透過 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議聘請專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
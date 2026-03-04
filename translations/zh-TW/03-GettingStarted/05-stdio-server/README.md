# MCP Server 使用 stdio 傳輸

> **⚠️ 重要更新**：從 MCP 規範 2025-06-18 起，獨立的 SSE（Server-Sent Events）傳輸已被 **棄用**，並改由「Streamable HTTP」傳輸取代。目前的 MCP 規範定義了兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（建議用於本地伺服器）
> 2. **Streamable HTTP** - 用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新為聚焦於 **stdio 傳輸**，這是大多數 MCP 伺服器實作的推薦方式。

stdio 傳輸允許 MCP 伺服器透過標準輸入與輸出串流與客戶端進行通訊。這是現行 MCP 規範中最常用且推薦的傳輸機制，提供一種簡單且高效率的方式來建構 MCP 伺服器，且能輕易整合至各種客戶端應用程式。

## 概覽

本課程涵蓋如何使用 stdio 傳輸來建構並使用 MCP 伺服器。

## 學習目標

完成此課程後，你將能夠：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 在 Visual Studio Code 中使用 MCP 伺服器。
- 了解現在 MCP 的傳輸機制及為何推薦 stdio。

## stdio 傳輸 - 運作方式

stdio 傳輸是現行 MCP 規範（2025-06-18）支持的兩種傳輸類型之一。運作方式如下：

- **簡單通訊**：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並將回應透過標準輸出（`stdout`）傳送。
- **基於進程**：客戶端啟動 MCP 伺服器作為子進程。
- **訊息格式**：訊息為獨立的 JSON-RPC 請求、通知或回應，以換行符分隔。
- **日誌記錄**：伺服器可透過標準錯誤（`stderr`）寫入 UTF-8 字串作為日誌。

### 主要要求：
- 訊息必須以換行符分隔，且不得包含內嵌換行符
- 伺服器不得在 `stdout` 輸出非有效的 MCP 訊息
- 客戶端不得向伺服器的 `stdin` 傳送非有效 MCP 訊息

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

在以上代碼中：

- 我們從 MCP SDK 匯入 `Server` 類別與 `StdioServerTransport`
- 建立具備基本配置與能力的伺服器實例

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

在以上程式碼中，我們：

- 使用 MCP SDK 創建伺服器實例
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

與 SSE 的主要差異是 stdio 伺服器：

- 不需設定 Web 伺服器或 HTTP 端點
- 由客戶端以子程序形式啟動
- 透過 stdin/stdout 流通訊
- 實作與偵錯更簡單

## 練習：建立 stdio 伺服器

建立伺服器時，我們需要注意兩件事：

- 需使用 Web 伺服器來暴露連線與訊息的端點。

## 實驗：建立簡單的 MCP stdio 伺服器

本實驗將使用推薦的 stdio 傳輸建立簡單 MCP 伺服器，該伺服器將暴露可由客戶端透過標準 Model Context Protocol 呼叫的工具。

### 先決條件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 基本非同步程式設計概念

讓我們開始建立第一個 MCP stdio 伺服器：

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

**Stdio 傳輸（現行標準）：**
- 簡單的子程序模型 — 由客戶端啟動伺服器為子進程
- 透過 stdin/stdout 使用 JSON-RPC 訊息通訊
- 不須設定 HTTP 伺服器
- 提升效能與安全性
- 偵錯與開發更容易

**SSE 傳輸（MCP 2025-06-18 以後棄用）：**
- 需 HTTP 伺服器與 SSE 端點
- 較複雜的 Web 伺服器架構設定
- HTTP 端點需額外安全考量
- 現改由 Streamable HTTP 取代以支援 Web 場景

### 使用 stdio 傳輸建立伺服器

建立 stdio 伺服器，我們需：

1. **匯入必要函式庫** — 取得 MCP 伺服器組件與 stdio 傳輸
2. **建立伺服器實例** — 定義伺服器及其能力
3. **定義工具** — 新增我們要暴露的功能
4. **設定傳輸** — 配置 stdio 通訊
5. **啟動伺服器** — 啟動伺服器並處理訊息

以下採逐步構建：

### 步驟 1：建立基本的 stdio 伺服器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 設定日誌記錄
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

### 步驟 2：新增更多工具

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

### 步驟 3：執行伺服器

將程式碼另存為 `server.py`，並於命令列執行：

```bash
python server.py
```

伺服器將啟動並等待來自 stdin 的輸入，透過 stdio 傳輸使用 JSON-RPC 訊息交流。

### 步驟 4：使用 Inspector 測試

你可以使用 MCP Inspector 來測試伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 執行 Inspector 並指向你的伺服器
3. 測試你所建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 偵錯你的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是用於偵錯與測試 MCP 伺服器的有用工具。以下是如何搭配你的 stdio 伺服器使用：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **測試伺服器**：Inspector 提供 Web 介面，你可以：
   - 查看伺服器能力
   - 以不同參數測試工具
   - 監控 JSON-RPC 訊息
   - 偵錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 中偵錯你的 MCP 伺服器：

1. 在 `.vscode/launch.json` 建立啟動設定：
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
3. 啟動除錯並搭配 Inspector 測試

### 常見偵錯建議

- 使用 `stderr` 記錄日誌 — 絕勿向 `stdout` 輸出，因其保留給 MCP 訊息
- 確保所有 JSON-RPC 訊息均以換行符分隔
- 先用簡單工具測試，再加入複雜功能
- 使用 Inspector 驗證訊息格式

## 在 VS Code 中使用你的 stdio 伺服器

完成 MCP stdio 伺服器後，你可以將其整合至 VS Code，用於 Claude 或其他支援 MCP 的客戶端。

### 設定方法

1. 在 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）建立 MCP 設定檔：

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

2. **重新啟動 Claude**：關閉再開啟 Claude 以載入新伺服器設定。

3. **測試連線**：開始與 Claude 對話並嘗試使用你的伺服器工具：
   - 「你可以用問候工具跟我打招呼嗎？」
   - 「計算 15 和 27 的和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

以下為完整的 TypeScript 範例供參考：

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

// 添加工具
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

## 總結

在本次更新課程中，你學會了：

- 使用現行 **stdio 傳輸**（推薦方式）構建 MCP 伺服器
- 理解為何 SSE 傳輸被棄用，並以 stdio 與 Streamable HTTP 取代
- 建立可被 MCP 客戶端呼叫的工具
- 使用 MCP Inspector 偵錯伺服器
- 將 stdio 伺服器整合至 VS Code 與 Claude

與已棄用的 SSE 方法相比，stdio 傳輸提供更簡單、更安全且效能更好的 MCP 伺服器建置方式。它是截至 2025-06-18 規範下，大多數 MCP 伺服器實作所建議使用的傳輸方式。

### .NET

1. 先建立一些工具，為此我們建立一個檔案 *Tools.cs*，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試你的 stdio 伺服器

現在你已建立 stdio 伺服器，讓我們測試它以確保功能正常。

### 先決條件

1. 確認你已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 伺服器程式碼已存檔（例如 `server.py`）

### 使用 Inspector 測試

1. **啟動 Inspector 與你的伺服器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打開 Web 介面**：Inspector 將開啟瀏覽器視窗，顯示伺服器能力。

3. **測試工具**：
   - 使用不同名稱測試 `get_greeting` 工具
   - 以各種數字測試 `calculate_sum` 工具
   - 呼叫 `get_server_info` 工具查看伺服器元資料

4. **監控通訊**：Inspector 顯示客戶端與伺服器間的 JSON-RPC 訊息交換。

### 你應該會看到的

當伺服器正常啟動時，你會看到：
- Inspector 中列出的伺服器能力
- 可用於測試的工具
- 成功交換的 JSON-RPC 訊息
- 介面中顯示的工具回應

### 常見問題及解決方案

**伺服器無法啟動：**
- 請檢查所有依賴已安裝：`pip install mcp`
- 確認 Python 語法及縮排正確
- 檢視主控台錯誤訊息

**工具未出現：**
- 確認有 `@server.tool()` 裝飾器
- 工具函式必須在 `main()` 之前定義
- 伺服器配置是否正確

**連線問題：**
- 確保使用 stdio 傳輸
- 確認無其他程序干擾
- 驗證 Inspector 的指令語法正確

## 作業

嘗試擴充你的伺服器能力。參考 [這個頁面](https://api.chucknorris.io/) 增加調用 API 的工具，由你決定伺服器要具備哪些功能。玩得開心 :)

## 解答

[解答](./solution/README.md) 這裡有一份可運作的範例解答。

## 重要重點

本章關鍵要點如下：

- stdio 傳輸是本地 MCP 伺服器推薦的通訊機制。
- stdio 傳輸允許 MCP 伺服器與客戶端無縫利用標準輸入輸出串流通訊。
- 你可使用 Inspector 與 Visual Studio Code 直接使用 stdio 伺服器，使偵錯和整合更簡單。

## 範例程式

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python)

## 其他資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 後續步驟

## 下一步

既然你學會了如何使用 stdio 傳輸建立 MCP 伺服器，可以探索更進階的主題：

- **接下來**：[MCP 的 HTTP Streaming（Streamable HTTP）](../06-http-streaming/README.md) - 了解遠端伺服器採用的另一種傳輸機制
- **進階**：[MCP 安全最佳實踐](../../02-Security/README.md) - 強化 MCP 伺服器的安全性
- **打造生產環境**：[部署策略](../09-deployment/README.md) - 在生產環境部署伺服器

## 補充資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言的 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 更多社群提供的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議委由專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或曲解概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
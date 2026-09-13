# 使用 stdio 傳輸的 MCP 伺服器

> **⚠️ 重要更新**：自 MCP 規範 2025-06-18 起，獨立的 SSE（伺服器傳送事件）傳輸已被<strong>廢止</strong>，並被「可串流 HTTP」傳輸取代。當前 MCP 規範定義了兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（推薦用於本地伺服器）
> 2. **可串流 HTTP** - 用於可能在內部使用 SSE 的遠端伺服器
>
> 本課程已更新為專注於 **stdio 傳輸**，這是大多數 MCP 伺服器實現推薦的方式。

stdio 傳輸允許 MCP 伺服器通過標準輸入和輸出串流與客戶端通訊。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供了一種簡單且高效的方法來構建 MCP 伺服器，能夠輕鬆整合各種客戶端應用程式。

## 概覽

本課程涵蓋如何使用 stdio 傳輸來構建和使用 MCP 伺服器。

## 學習目標

完成本課程後，您將能：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 使用 Visual Studio Code 使用 MCP 伺服器。
- 了解當前 MCP 傳輸機制及為何推薦 stdio。


## stdio 傳輸 - 運作方式

stdio 傳輸是 MCP 規範
`2026-07-28` 中的兩種標準傳輸之一。其運作方式如下：

- <strong>簡單通訊</strong>：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並將訊息送至標準輸出（`stdout`）。
- <strong>基於進程</strong>：客戶端將 MCP 伺服器作為子進程啟動。
- <strong>訊息格式</strong>：訊息為獨立的 JSON-RPC 請求、通知或回應，以換行符號分隔。
- <strong>日誌記錄</strong>：伺服器可將 UTF-8 字串寫入標準錯誤（`stderr`）以作日誌用途。

### 主要要求：
- 訊息必須以換行符分隔，且不可包含內嵌換行符
- 伺服器不可對 `stdout` 寫入非有效 MCP 訊息
- 客戶端不可對伺服器的 `stdin` 寫入非有效 MCP 訊息

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

上述程式碼中：

- 我們從 MCP SDK 匯入 `Server` 類別和 `StdioServerTransport`
- 使用基本配置和功能建立伺服器實例
- 創建 `StdioServerTransport` 實例並將伺服器連接到它，實現透過 stdin/stdout 的通訊

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

上述程式碼中我們：

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

與 SSE 相比，stdio 伺服器的主要差異為：

- 不需要設置網頁伺服器或 HTTP 端點
- 由客戶端啟動為子進程
- 通過 stdin/stdout 串流通訊
- 實作與偵錯更簡單

## 練習：建立 stdio 伺服器

建立伺服器時，我們需記住兩件事：

- 我們需要使用網頁伺服器以公開連接和訊息端點。
## 實驗室：建立簡單 MCP stdio 伺服器


在本實驗中，我們將使用推薦的 stdio 傳輸來建立一個簡單的 MCP 伺服器。該伺服器將公開客戶端可以使用標準 Model Context Protocol 呼叫的工具。

### 先決條件

- Python 3.8 或更新版本
- MCP Python SDK：`pip install mcp`
- 基本的非同步程式設計理解

讓我們從建立第一個 MCP stdio 伺服器開始：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 創建伺服器
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
    # 使用標準輸入輸出傳輸
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 與已棄用的 SSE 方法的主要差異

**Stdio 傳輸（目前標準）：**
- 簡單的子程序模型 — 客戶端作為子程序啟動伺服器
- 使用 JSON-RPC 訊息通過 stdin/stdout 通訊
- 無需設置 HTTP 伺服器
- 更好的效能與安全性
- 更容易的除錯與開發

**SSE 傳輸（自 MCP 2025-06-18 起已棄用）：**
- 需要帶有 SSE 端點的 HTTP 伺服器
- 需要更複雜的網頁伺服器基礎設施設定
- HTTP 端點的額外安全考量
- 現已由 Streamable HTTP 取代，用於基於網路的場景

### 使用 stdio 傳輸建立伺服器

要建立我們的 stdio 伺服器，我們需要：

1. <strong>匯入所需套件</strong> - 需要 MCP 伺服器元件和 stdio 傳輸
2. <strong>建立伺服器實例</strong> - 定義具備功能的伺服器
3. <strong>定義工具</strong> - 新增我們想要公開的功能
4. <strong>設定傳輸</strong> - 配置 stdio 通訊
5. <strong>執行伺服器</strong> - 啟動伺服器並處理訊息

讓我們逐步建立：

### 步驟 1：建立基礎 stdio 伺服器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 創建伺服器
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

將程式碼儲存為 `server.py` 並從命令列執行：

```bash
python server.py
```

伺服器會啟動並等待來自 stdin 的輸入。它使用 JSON-RPC 訊息透過 stdio 傳輸進行通訊。

### 步驟 4：使用 Inspector 測試

你可以使用 MCP Inspector 來測試你的伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 執行 Inspector 並指向你的伺服器
3. 測試你建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 除錯你的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是除錯與測試 MCP 伺服器的寶貴工具。以下是如何使用它與你的 stdio 伺服器：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>測試你的伺服器</strong>：Inspector 提供一個網頁介面，你可以：
   - 查看伺服器功能
   - 測試帶有不同參數的工具
   - 監控 JSON-RPC 訊息
   - 除錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 中除錯你的 MCP 伺服器：

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

2. 在伺服器程式碼中設定中斷點
3. 執行除錯器並搭配 Inspector 測試

### 常見除錯技巧

- 使用 `stderr` 進行記錄 — 千萬不要寫入 `stdout`，因為那是保留給 MCP 訊息用的
- 確保所有 JSON-RPC 訊息以換行字元分隔
- 先以簡單的工具測試，再逐步加入複雜功能

- 使用 Inspector 來驗證訊息格式

## 在 VS Code 中使用你的 stdio 伺服器


當你建立好你的 MCP stdio 伺服器後，你可以將它和 VS Code 整合，用來和 Claude 或其他相容 MCP 的客戶端一起使用。

### 設定

1. **建立一個 MCP 設定檔** 在 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

2. **重新啟動 Claude**：關閉並重新開啟 Claude 以載入新的伺服器設定。

3. <strong>測試連線</strong>：開始和 Claude 對話並試用你的伺服器工具：
   - 「你可以用問候工具向我打招呼嗎？」
   - 「計算 15 與 27 的和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

以下是一個完整的 TypeScript 範例供參考：

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

## 總結

在這次更新的課程中，你學會了如何：

- 使用目前的 **stdio 傳輸** 建立 MCP 伺服器（推薦方式）
- 理解為什麼 SSE 傳輸被棄用，改用 stdio 和 Streamable HTTP
- 創建可被 MCP 客戶端呼叫的工具
- 使用 MCP Inspector 來除錯你的伺服器
- 將你的 stdio 伺服器與 VS Code 及 Claude 整合

stdio 傳輸提供比已棄用的 SSE 方案更簡單、更安全且更高效的 MCP 伺服器建構方式。根據 2025-06-18 規範，它是大部分 MCP 伺服器實作的推薦傳輸方式。


### .NET

1. 我們先來建立一些工具，為此我們會建立一個 *Tools.cs* 檔案，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試你的 stdio 伺服器

現在你已經建立了 stdio 伺服器，讓我們來測試它是否正常運作。

### 先決條件

1. 確認你已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 你的伺服器程式碼應該已儲存（例如 `server.py`）

### 使用 Inspector 進行測試

1. **啟動 Inspector 與你的伺服器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>開啟網頁介面</strong>：Inspector 將打開瀏覽器視窗，顯示你的伺服器功能。

3. <strong>測試各工具</strong>：
   - 嘗試 `get_greeting` 工具搭配不同的名字
   - 使用各種數字測試 `calculate_sum` 工具
   - 呼叫 `get_server_info` 工具查看伺服器資訊

4. <strong>監控通訊</strong>：Inspector 會顯示客戶端與伺服器間交換的 JSON-RPC 訊息。

### 你應該會看到什麼

當你的伺服器正確啟動時，你會看到：
- Inspector 中列出伺服器能力
- 可測試的工具
- 成功的 JSON-RPC 訊息交換
- 介面中顯示的工具回應

### 常見問題與解決方案

**伺服器無法啟動：**
- 檢查是否安裝了所有依賴：`pip install mcp`
- 驗證 Python 語法和縮排
- 留意主控台的錯誤訊息

**工具未出現：**
- 確保有加上 `@server.tool()` 裝飾器
- 確認工具函式定義在 `main()` 之前
- 驗證伺服器是否正確設定

**連線問題：**
- 確認伺服器正確使用 stdio 傳輸
- 確定沒有其他程序干擾
- 驗證 Inspector 命令語法正確

## 作業

嘗試為你的伺服器添加更多功能。參見 [這個頁面](https://api.chucknorris.io/) 以例如新增呼叫 API 的工具。你可自行決定伺服器應該呈現的功能。祝你玩得開心 :)
## 解答

[解答](./solution/README.md) 這裡是一個含有可運作程式碼的可能解決方案。

## 重要摘要

本章的重點摘要如下：

- stdio 傳輸是本地 MCP 伺服器推薦的機制。
- stdio 傳輸利用標準輸入和輸出流實現 MCP 伺服器與客戶端無縫溝通。
- 你可以直接使用 Inspector 和 Visual Studio Code 消費 stdio 伺服器，使除錯與整合變得簡單。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 其他資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下來要做什麼

## 下一步

現在你已學會如何使用 stdio 傳輸建造 MCP 伺服器，可以探索更進階的主題：

- <strong>下一章</strong>：[HTTP 流（Streamable HTTP）上的 MCP](../06-http-streaming/README.md) - 學習另一個支援的遠端伺服器傳輸機制
- <strong>進階</strong>：[MCP 安全最佳實踐](../../02-Security/README.md) - 在你的 MCP 伺服器中實作安全性
- <strong>正式環境</strong>：[部署策略](../09-deployment/README.md) - 部署你的伺服器以供正式使用

## 其他資源

- [MCP 規範 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 最新規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 支援所有語言的 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 更多由社群提供的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
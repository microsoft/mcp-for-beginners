# MCP 伺服器使用 stdio 傳輸

> **⚠️ 重要更新**：根據 MCP 規範 2025-06-18，獨立的 SSE（Server-Sent Events）傳輸已被<strong>淘汰</strong>，取而代之的是「Streamable HTTP」傳輸。目前的 MCP 規範定義了兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（推薦用於本地伺服器）
> 2. **Streamable HTTP** - 適用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新，專注於<strong>stdio 傳輸</strong>，這是大多數 MCP 伺服器實作推薦的方法。

stdio 傳輸允許 MCP 伺服器通過標準輸入和輸出串流與客戶端通信。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供簡單且高效的方式來構建 MCP 伺服器，可以輕鬆整合各種客戶端應用。

## 概述

本課程涵蓋如何使用 stdio 傳輸來建立及使用 MCP 伺服器。

## 學習目標

在本課程結束時，你將能夠：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 使用 Visual Studio Code 使用 MCP 伺服器。
- 理解目前的 MCP 傳輸機制以及為何推薦 stdio。

## stdio 傳輸 - 運作原理

stdio 傳輸是目前 MCP 規範（2025-06-18）支持的兩種傳輸類型之一。其運作方式如下：

- <strong>簡單通信</strong>：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並將訊息發送到標準輸出（`stdout`）。
- <strong>基於程序</strong>：客戶端將 MCP 伺服器作為子程序啟動。
- <strong>訊息格式</strong>：訊息是獨立的 JSON-RPC 請求、通知或回應，以換行符號分隔。
- <strong>日誌</strong>：伺服器可以將 UTF-8 字串寫入標準錯誤（`stderr`）作為日誌。

### 主要要求：
- 訊息必須以換行符號分隔，且不得包含內嵌換行符號
- 伺服器不得向 `stdout` 寫入非有效 MCP 訊息
- 客戶端不得向伺服器的 `stdin` 寫入非有效 MCP 訊息

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

在上述程式碼中：

- 我們從 MCP SDK 匯入 `Server` 類別與 `StdioServerTransport`
- 建立具有基本配置與能力的伺服器實例
- 創建 `StdioServerTransport` 實例並將伺服器連接至該傳輸，啟用透過 stdin/stdout 通信

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

在上述程式碼中我們：

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

與 SSE 的關鍵差異是 stdio 伺服器：

- 不需要設定網頁伺服器或 HTTP 端點
- 由客戶端作為子進程啟動
- 通過 stdin/stdout 串流通信
- 更簡單實作與偵錯

## 練習：建立 stdio 伺服器

建立伺服器時，我們需要記住兩點：

- 需要使用網頁伺服器來暴露連線和訊息端點。

## 實驗：建立簡單的 MCP stdio 伺服器

在本實驗中，我們將使用推薦的 stdio 傳輸建立一個簡單 MCP 伺服器。此伺服器將暴露客戶端可以使用標準 Model Context Protocol 調用的工具。

### 先決條件

- Python 3.8 或更新版本
- MCP Python SDK：`pip install mcp`
- 基本的非同步程式設計理解

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

## 與淘汰 SSE 方法的主要差異

**Stdio 傳輸（當前標準）：**
- 簡單的子程序模型 - 由客戶端啟動伺服器作為子進程
- 通過 stdin/stdout 使用 JSON-RPC 訊息通信
- 不需要設置 HTTP 伺服器
- 更佳的效能與安全性
- 更容易偵錯與開發

**SSE 傳輸（自 MCP 2025-06-18 起淘汰）：**
- 需要含有 SSE 端點的 HTTP 伺服器
- 較為複雜的網頁伺服器基礎架構設置
- 對 HTTP 端點有額外的安全性考量
- 現已被網頁場景下的 Streamable HTTP 取代

### 使用 stdio 傳輸建立伺服器

建立 stdio 伺服器需：

1. <strong>引入所需函式庫</strong> - 需要 MCP 伺服器元件和 stdio 傳輸
2. <strong>建立伺服器實例</strong> - 定義具有能力的伺服器
3. <strong>定義工具</strong> - 加入想暴露的功能
4. <strong>設定傳輸</strong> - 配置 stdio 通信
5. <strong>啟動伺服器</strong> - 啟動並處理訊息

逐步建置如下：

### 第一步：建立基本 stdio 伺服器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 創建服務器
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

### 第二步：新增更多工具

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

### 第三步：啟動伺服器

將程式碼存成 `server.py` 並透過命令列執行：

```bash
python server.py
```

伺服器將啟動並等待從 stdin 輸入。它透過 stdio 傳輸使用 JSON-RPC 訊息通信。

### 第四步：使用 Inspector 測試

你可以使用 MCP Inspector 測試你的伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 運行 Inspector 並設定連至你的伺服器
3. 測試你建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 偵錯你的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是偵錯和測試 MCP 伺服器的重要工具。以下是使用它來偵錯 stdio 伺服器的方法：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>測試伺服器</strong>：Inspector 提供網頁介面，你可以：
   - 檢視伺服器能力
   - 以不同參數測試工具
   - 監控 JSON-RPC 訊息
   - 偵錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 中偵錯 MCP 伺服器：

1. 在 `.vscode/launch.json` 建立啟動配置：
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

2. 在伺服器程式碼中設置斷點
3. 運行偵錯器並使用 Inspector 測試

### 常見偵錯建議

- 使用 `stderr` 作日誌，不要寫入 `stdout`，因為它保留給 MCP 訊息
- 確保所有 JSON-RPC 訊息以換行符號分隔
- 先用簡單工具測試，再加入複雜功能
- 使用 Inspector 驗證訊息格式

## 在 VS Code 中使用你的 stdio 伺服器

建立 MCP stdio 伺服器後，可以整合至 VS Code 與 Claude 或其他相容 MCP 的客戶端：

### 配置

1. 在 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）創建 MCP 配置檔：

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

2. **重新啟動 Claude**：關閉並重新開啟 Claude 以讀取新的伺服器配置。

3. <strong>測試連接</strong>：開始與 Claude 對話並嘗試使用伺服器工具：
   - 「你可以用 greeting 工具跟我打招呼嗎？」
   - 「計算 15 加 27 的總和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

以下是完整 TypeScript 範例供參考：

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

在這個更新的課程中，你學會了：

- 使用目前推薦的 **stdio 傳輸** 建立 MCP 伺服器
- 理解 SSE 傳輸為何被淘汰，改用 stdio 及 Streamable HTTP
- 創建可由 MCP 客戶端調用的工具
- 使用 MCP Inspector 偵錯伺服器
- 將 stdio 伺服器整合進 VS Code 與 Claude

stdio 傳輸提供相較於淘汰的 SSE 更簡單、更安全及高效的 MCP 伺服器建構方式。根據 2025-06-18 規範，它是大多數 MCP 伺服器實作推薦的傳輸。

### .NET

1. 讓我們先建立一些工具，我們會建立一個檔案 *Tools.cs*，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試你的 stdio 伺服器

既然你已建立了 stdio 伺服器，讓我們進行測試確保它能正常運作。

### 先決條件

1. 確認你已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 你的伺服器程式碼已保存（例如保存為 `server.py`）

### 使用 Inspector 測試

1. **啟動 Inspector 與你的伺服器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>開啟網頁介面</strong>：Inspector 將開啟瀏覽器視窗顯示伺服器能力。

3. <strong>測試工具</strong>：
   - 使用不同名稱嘗試 `get_greeting` 工具
   - 測試不同數字的 `calculate_sum` 工具
   - 呼叫 `get_server_info` 工具以查看伺服器元資料

4. <strong>監控通訊</strong>：Inspector 顯示客戶端與伺服器間交換的 JSON-RPC 訊息。

### 你應該看到的內容

當你的伺服器成功啟動時，你會看到：
- Inspector 中顯示伺服器能力列表
- 工具可供測試
- 成功的 JSON-RPC 訊息交換
- 介面中顯示工具回應

### 常見問題與解決方案

**伺服器無法啟動：**
- 確認所有相依套件已安裝：`pip install mcp`
- 檢查 Python 語法與縮排
- 查看終端機中的錯誤訊息

**工具未顯示：**
- 確保有使用 `@server.tool()` 裝飾器
- 確認工具函式在 `main()` 前已定義
- 確認伺服器設定正確

**連線問題：**
- 確保伺服器正確使用 stdio 傳輸
- 檢查沒有其他程序干擾
- 驗證 Inspector 的指令語法

## 作業

嘗試為你的伺服器加入更多功能。可參考[此頁面](https://api.chucknorris.io/)，例如新增調用 API 的工具。由你決定伺服器的功能長什麼樣子。祝你玩得開心 :)

## 解答

[解答](./solution/README.md) 這裡有一個可行且可運作的程式碼範例。

## 重要結論

本章的重點如下：

- stdio 傳輸是本地 MCP 伺服器推薦的機制。
- stdio 傳輸允許 MCP 伺服器與客戶端無縫使用標準輸入輸出串流通信。
- 你可以使用 Inspector 和 Visual Studio Code 直接使用 stdio 伺服器，讓偵錯與整合更加簡單。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 其他資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下來是什麼

## 下一步

學會使用 stdio 傳輸建立 MCP 伺服器後，你可以探究更進階的主題：

- <strong>下一步</strong>：[MCP 的 HTTP 串流 (Streamable HTTP)](../06-http-streaming/README.md) - 瞭解另一種支援用於遠端伺服器的傳輸機制
- <strong>進階</strong>：[MCP 安全性最佳實踐](../../02-Security/README.md) - 在 MCP 伺服器中實作安全措施
- <strong>生產環境</strong>：[部署策略](../09-deployment/README.md) - 將伺服器部署到生產環境

## 其他資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 更多社群的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件以其母語版本為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而導致的任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
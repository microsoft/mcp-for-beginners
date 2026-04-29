# MCP 伺服器與 stdio 傳輸

> **⚠️ 重要更新**：根據 MCP 規範 2025-06-18，獨立 SSE（Server-Sent Events）傳輸已被 <strong>棄用</strong>，並由「可串流 HTTP」傳輸取代。目前 MCP 規範定義兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（建議用於本地伺服器）
> 2. **可串流 HTTP** - 適用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新為專注於 **stdio 傳輸**，這是大多數 MCP 伺服器實現所推薦的方法。

stdio 傳輸允許 MCP 伺服器透過標準輸入和輸出串流與客戶端通訊。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供了一種簡單且高效的方式構建能輕鬆與各種客戶端應用整合的 MCP 伺服器。

## 概覽

本課程涵蓋如何使用 stdio 傳輸建立與使用 MCP 伺服器。

## 學習目標

完成本課程後，您將能夠：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 在 Visual Studio Code 中使用 MCP 伺服器。
- 了解目前 MCP 的傳輸機制以及為何建議使用 stdio。

## stdio 傳輸 - 運作方式

stdio 傳輸是目前 MCP 規範（2025-06-18）支援的兩種傳輸類型之一。其運作方式如下：

- <strong>簡單通訊</strong>：伺服器從標準輸入 (`stdin`) 讀取 JSON-RPC 訊息，並將訊息發送至標準輸出 (`stdout`)。
- <strong>基於程序</strong>：客戶端啟動 MCP 伺服器作為子程序。
- <strong>訊息格式</strong>：訊息為單獨的 JSON-RPC 請求、通知或回應，以換行符分隔。
- <strong>日誌紀錄</strong>：伺服器可選擇寫入 UTF-8 字串到標準錯誤 (`stderr`) 用作日誌。

### 主要要求：
- 訊息必須以換行符分隔，且不得包含內嵌的換行符
- 伺服器不得寫入非有效 MCP 訊息至 `stdout`
- 客戶端不得寫入非有效 MCP 訊息至伺服器的 `stdin`

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

- 我們從 MCP SDK 匯入 `Server` 類別及 `StdioServerTransport`
- 建立具有基本設定與能力的伺服器實例
- 建立 `StdioServerTransport` 實例並將伺服器連接至它，以啟用 stdin/stdout 通訊

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

上述程式碼中，我們：

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

與 SSE 的主要差異在於 stdio 伺服器：

- 不需設定網頁伺服器或 HTTP 端點
- 由客戶端以子程序啟動
- 通過 stdin/stdout 串流通訊
- 實作及偵錯更簡單

## 練習：建立 stdio 伺服器

建立伺服器需留意兩件事：

- 需要使用網頁伺服器以公開連接與訊息端點。
## 實驗室：建立簡單 MCP stdio 伺服器

本實驗室將使用建議的 stdio 傳輸建立簡單 MCP 伺服器。此伺服器將公開可由客戶端使用標準 Model Context 協議呼叫的工具。

### 先決條件

- Python 3.8 或更新版本
- MCP Python SDK：`pip install mcp`
- 具備非同步程式設計基礎

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

**Stdio 傳輸（當前標準）：**
- 簡單的子程序模式 — 客戶端啟動伺服器作為子程序
- 透過 stdin/stdout 使用 JSON-RPC 訊息通訊
- 不需設定 HTTP 伺服器
- 更佳的效能與安全性
- 更易於偵錯與開發

**SSE 傳輸（自 MCP 2025-06-18 起棄用）：**
- 需 HTTP 伺服器及 SSE 端點
- 部署較複雜，需網頁伺服器架構
- HTTP 端點需額外安全考量
- 現已由可串流 HTTP 取代於網頁場景使用

### 使用 stdio 傳輸建立伺服器

建立 stdio 伺服器需：

1. <strong>匯入必要函式庫</strong> — 需要 MCP 伺服器元件及 stdio 傳輸
2. <strong>建立伺服器實例</strong> — 定義具體功能
3. <strong>定義工具</strong> — 添增要公開的功能
4. <strong>設定傳輸</strong> — 配置 stdio 通訊
5. <strong>運行伺服器</strong> — 啟動並處理訊息

讓我們逐步建構：

### 第 1 步：建立基本 stdio 伺服器

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

### 第 2 步：添加更多工具

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

### 第 3 步：執行伺服器

將程式碼存檔為 `server.py`，並從命令列執行：

```bash
python server.py
```

伺服器將啟動並等待來自 stdin 的輸入。它使用 stdio 傳輸透過 JSON-RPC 訊息進行通訊。

### 第 4 步：使用 Inspector 測試

您可以使用 MCP Inspector 測試伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 執行 Inspector 並指向您的伺服器
3. 測試您建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 偵錯您的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是偵錯與測試 MCP 伺服器的重要工具。以下為如何搭配 stdio 伺服器使用：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>測試您的伺服器</strong>：Inspector 提供網頁介面，您可以在此：
   - 查看伺服器功能
   - 以不同參數測試工具
   - 監視 JSON-RPC 訊息
   - 偵錯連線問題

### 使用 VS Code

您也可以直接在 VS Code 中偵錯 MCP 伺服器：

1. 在 `.vscode/launch.json` 中建立啟動設定：
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
3. 執行偵錯器，並搭配 Inspector 測試

### 常見偵錯建議

- 利用 `stderr` 做日誌紀錄 — 千萬不要寫入 `stdout`，因其專用於 MCP 訊息
- 確保所有 JSON-RPC 訊息均以換行符分隔
- 先用簡單工具測試，再加入複雜功能
- 使用 Inspector 驗證訊息格式

## 在 VS Code 中使用您的 stdio 伺服器

建立 MCP stdio 伺服器後，您可以將其整合至 VS Code，以搭配 Claude 或其他 MCP 兼容客戶端使用。

### 配置

1. **在 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）建立 MCP 配置檔**：

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

2. **重啟 Claude**：關閉並重新開啟 Claude 以載入新的伺服器設定。

3. <strong>測試連線</strong>：開始與 Claude 交談並嘗試使用您的伺服器工具：
   - 「你可以用問候工具向我打招呼嗎？」
   - 「計算 15 和 27 的和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

以下為完整的 TypeScript 範例參考：

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

## 小結

本更新課程中，您學習了如何：

- 使用目前推薦的 **stdio 傳輸** 建立 MCP 伺服器
- 理解 SSE 傳輸為何被 stdio 及可串流 HTTP 所取代
- 建立可被 MCP 用戶端呼叫的工具
- 使用 MCP Inspector 偵錯伺服器
- 將 stdio 伺服器與 VS Code 及 Claude 整合

與已棄用的 SSE 方法相較，stdio 傳輸提供更簡單、更安全且效能更佳的 MCP 伺服器建置方式。根據 2025-06-18 規範，stdio 是大多數 MCP 伺服器實作的推薦傳輸方式。

### .NET

1. 讓我們先建立一些工具，為此將建立一個名為 *Tools.cs* 的檔案，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試您的 stdio 伺服器

您建立好 stdio 伺服器後，現在是時候測試確保它能正常運作。

### 先決條件

1. 確認已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 已保存您的伺服器程式碼（例如命名為 `server.py`）

### 使用 Inspector 測試

1. **使用您的伺服器啟動 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>開啟網頁介面</strong>：Inspector 會在瀏覽器中開啟頁面，顯示您的伺服器功能。

3. <strong>測試工具</strong>： 
   - 嘗試使用不同姓名呼叫 `get_greeting` 工具
   - 用各種數字測試 `calculate_sum` 工具
   - 呼叫 `get_server_info` 工具查看伺服器元資料

4. <strong>監視通訊內容</strong>：Inspector 顯示客戶端與伺服器間交換的 JSON-RPC 訊息。

### 您應該看到的結果

當您的伺服器正常啟動時，您會看到：
- Inspector 中列出伺服器功能
- 可供測試的工具
- 成功交換的 JSON-RPC 訊息
- 介面上顯示的工具回應

### 常見問題與解決方案

**伺服器無法啟動：**
- 確認所有依賴已安裝：`pip install mcp`
- 檢查 Python 語法與縮排
- 留意主控台錯誤訊息

**工具未顯示：**
- 確認存在 `@server.tool()` 裝飾器
- 確認工具函式已在 `main()` 前定義
- 確認伺服器已正確設定

**連線問題：**
- 確認伺服器正確使用 stdio 傳輸
- 確認無其他程序干擾
- 檢查 Inspector 指令語法

## 作業

嘗試擴充伺服器功能。參考[這個頁面](https://api.chucknorris.io/)來新增一個可呼叫 API 的工具。由您決定伺服器應該長怎樣。祝您玩得愉快 :)

## 解答

[解答](./solution/README.md) 這裡是一個可工作的程式碼解答範例。

## 重要重點整理

本章的重點如下：

- stdio 傳輸是本地 MCP 伺服器推薦使用的機制。
- stdio 傳輸允許 MCP 伺服器與客戶端透過標準輸入輸出流無縫通訊。
- 你可以直接使用 Inspector 與 Visual Studio Code 進行 stdio 伺服器的調試與整合，簡化開發流程。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python) 

## 額外資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 下一步

## 後續進度

您已學會如何用 stdio 傳輸建立 MCP 伺服器，接著可以探索更進階主題：

- <strong>接下來</strong>：[MCP HTTP 串流 (Streamable HTTP)](../06-http-streaming/README.md) - 學習遠端伺服器使用的另一種傳輸機制
- <strong>進階</strong>：[MCP 安全最佳實務](../../02-Security/README.md) - 在 MCP 伺服器中實施安全措施
- <strong>生產環境</strong>：[部署策略](../09-deployment/README.md) - 將伺服器投入生產使用

## 額外資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範文件
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 來自社群更多伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引致之任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP 伺服器搭配 stdio 傳輸

> **⚠️ 重要更新**：根據 MCP 規範 2025-06-18，獨立的 SSE（Server-Sent Events）傳輸已被 <strong>淘汰</strong>，並由「Streamable HTTP」傳輸取代。當前的 MCP 規範定義了兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（建議用於本地伺服器）
> 2. **Streamable HTTP** - 用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新，重點放在 **stdio 傳輸**，這是大多數 MCP 伺服器實作推薦的方式。

stdio 傳輸允許 MCP 伺服器透過標準輸入輸出串流與客戶端進行通訊。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供一種簡單且高效的方式來建置 MCP 伺服器，能輕鬆整合各種客戶端應用程式。

## 概觀

本課程涵蓋如何使用 stdio 傳輸建立及使用 MCP 伺服器。

## 學習目標

完成本課程後，你將能夠：

- 使用 stdio 傳輸建立 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 在 Visual Studio Code 中使用 MCP 伺服器。
- 理解目前 MCP 傳輸機制以及為何推薦使用 stdio。

## stdio 傳輸 - 運作原理

stdio 傳輸是目前 MCP 規範（2025-06-18）支持的兩種傳輸類型之一。其運作方式如下：

- <strong>簡單通訊</strong>：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並傳送訊息至標準輸出（`stdout`）。
- <strong>基於程序</strong>：客戶端啟動 MCP 伺服器作為子程序。
- <strong>訊息格式</strong>：訊息為獨立的 JSON-RPC 請求、通知或回應，使用換行符分隔。
- <strong>日誌紀錄</strong>：伺服器可寫入 UTF-8 字串至標準錯誤（`stderr`）做日誌用途。

### 主要要求：
- 訊息必須以換行符分隔，且不得包含內嵌換行符
- 伺服器不得寫入非有效 MCP 訊息的內容到 `stdout`
- 客戶端不得寫入非有效 MCP 訊息的內容到伺服器的 `stdin`

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

上述代碼中：

- 我們從 MCP SDK 匯入 `Server` 類別及 `StdioServerTransport`
- 建立一個具備基本配置與能力的伺服器實例
- 建立 `StdioServerTransport` 實例並連結伺服器，使其透過 stdin/stdout 進行通訊

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

上述代碼中：

- 使用 MCP SDK 建立伺服器實例
- 透過裝飾器定義工具
- 使用 stdio_server 上下文管理器管理傳輸

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

- 無需設定網頁伺服器或 HTTP 端點
- 由客戶端作為子程序啟動
- 透過 stdin/stdout 流進行通訊
- 實作及偵錯更簡單

## 練習：創建 stdio 伺服器

創建伺服器時，我們需記住兩點：

- 需要使用網頁伺服器公開用於連線及訊息的端點。

## 實驗室：建立簡單的 MCP stdio 伺服器

在本實驗室，我們將使用推薦的 stdio 傳輸建立一個簡單的 MCP 伺服器。此伺服器將提供客戶端可使用的工具，透過標準的 Model Context Protocol 呼叫。

### 事前準備

- Python 3.8 或以上
- MCP Python SDK：`pip install mcp`
- 基本異步程式設計知識

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

## 與已淘汰的 SSE 方法主要差異

**Stdio 傳輸（現行標準）：**
- 簡單的子程序模型—客戶端啟動伺服器作為子程序
- 使用 stdin/stdout 透過 JSON-RPC 訊息通訊
- 不需設定 HTTP 伺服器
- 效能和安全性更佳
- 更容易進行偵錯與開發

**SSE 傳輸（2025-06-18 起已淘汰）：**
- 需要 HTTP 伺服器及 SSE 端點
- 需複雜的網頁伺服器架構設定
- HTTP 端點額外安全性考量
- 現由 Streamable HTTP 用於網頁場景替代

### 使用 stdio 傳輸建立伺服器

建立 stdio 伺服器的步驟：

1. <strong>引入必要函式庫</strong>—需要 MCP 伺服器元件及 stdio 傳輸
2. <strong>建立伺服器實例</strong>—定義伺服器功能與能力
3. <strong>定義工具</strong>—新增想要公開的功能
4. <strong>設定傳輸</strong>—配置 stdio 通訊
5. <strong>執行伺服器</strong>—啟動伺服器並處理訊息

讓我們一步步構建：

### 步驟 1：建立基本 stdio 伺服器

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

### 步驟 3：啟動伺服器

將代碼儲存為 `server.py`，並在命令列執行：

```bash
python server.py
```

伺服器將啟動並等待 stdin 輸入。它透過 stdio 傳輸使用 JSON-RPC 訊息來通訊。

### 步驟 4：使用 Inspector 測試

你可以用 MCP Inspector 來測試你的伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 執行 Inspector，並連結到你的伺服器
3. 測試你建立的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## 偵錯你的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是用來偵錯及測試 MCP 伺服器的有用工具。以下是使用 stdio 伺服器的步驟：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **執行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>測試你的伺服器</strong>：Inspector 提供網頁介面，可用來：
   - 查看伺服器能力
   - 測試工具及不同參數
   - 監控 JSON-RPC 訊息
   - 偵錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 偵錯 MCP 伺服器：

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

2. 在伺服器程式碼中設置中斷點
3. 啟動偵錯並搭配 Inspector 測試

### 常見偵錯技巧

- 使用 `stderr` 紀錄日誌—切勿寫入 `stdout`，因為該串流保存給 MCP 訊息
- 確保所有 JSON-RPC 訊息均以換行符結尾
- 先以簡單工具測試，再加上複雜功能
- 使用 Inspector 來驗證訊息格式

## 在 VS Code 中使用你的 stdio 伺服器

建立完 MCP stdio 伺服器後，可以整合至 VS Code，並與 Claude 或其他支持 MCP 的客戶端共用。

### 配置

1. **建立 MCP 配置檔**，路徑為 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

2. **重新啟動 Claude**：關閉並重新開啟 Claude 以載入新的伺服器配置。

3. <strong>測試連線</strong>：與 Claude 開始對話，嘗試使用你的伺服器工具：
   - 「可以使用問候工具跟我打招呼嗎？」
   - 「計算 15 和 27 的總和」
   - 「伺服器資訊是什麼？」

### TypeScript stdio 伺服器範例

以下為完整 TypeScript 範例供參考：

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

在這次更新的課程中，你學會了：

- 如何使用現行推薦的 **stdio 傳輸** 建立 MCP 伺服器
- 了解為何 SSE 傳輸被淘汰，而改用 stdio 與 Streamable HTTP
- 建立可供 MCP 客戶端呼叫的工具
- 使用 MCP Inspector 偵錯伺服器
- 將 stdio 伺服器整合到 VS Code 及 Claude

stdio 傳輸提供比淘汰的 SSE 更簡單、更安全且效能更佳的 MCP 伺服器建置方式，是根據 2025-06-18 規範，絕大多數 MCP 伺服器實作的建議傳輸機制。

### .NET

1. 首先建立一些工具，為此我們會建立一個 *Tools.cs* 檔案，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## 練習：測試你的 stdio 伺服器

你已經建立好 stdio 伺服器，現在讓我們測試確保它能正常工作。

### 事前準備

1. 確認已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 伺服器程式碼已儲存（例如 `server.py`）

### 使用 Inspector 進行測試

1. **啟動 Inspector 與你的伺服器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>開啟網頁介面</strong>：Inspector 會開啟瀏覽器視窗，顯示伺服器能力。

3. <strong>測試工具</strong>：
   - 嘗試 `get_greeting` 工具並使用不同名稱
   - 測試 `calculate_sum` 工具與不同數字
   - 呼叫 `get_server_info` 工具查看伺服器元資料

4. <strong>監控通訊</strong>：Inspector 顯示客戶端與伺服器間交換的 JSON-RPC 訊息。

### 你應該會看到的

當伺服器成功啟動，你應該看到：
- Inspector 列出伺服器能力
- 工具供測試使用
- JSON-RPC 訊息成功交換
- 工具回應顯示在介面

### 常見問題及解決方案

**伺服器無法啟動：**
- 檢查所有依賴是否安裝：`pip install mcp`
- 確認 Python 語法及縮排正確
- 查看主控台的錯誤訊息

**工具未顯示：**
- 確認存在 `@server.tool()` 裝飾器
- 確認工具函數定義在 `main()` 前
- 確認伺服器配置正確

**連線問題：**
- 確定伺服器正確使用 stdio 傳輸
- 確認沒有其他程序干擾
- 驗證 Inspector 指令語法

## 作業

嘗試為你的伺服器增添更多功能。參考[這個頁面](https://api.chucknorris.io/)加上一個呼叫 API 的工具。由你決定伺服器的樣貌，玩得開心 :)

## 解答

[解答](./solution/README.md) 這裡有一個可運作的解答範例程式碼。

## 主要重點

本章節的主要重點如下：

- stdio 傳輸是本地 MCP 伺服器的推薦通訊機制。
- stdio 傳輸能利用標準輸入輸出串流，實現 MCP 伺服器與客戶端間無縫通訊。
- 你可以直接用 Inspector 和 Visual Studio Code 來使用 stdio 伺服器，使得偵錯與整合更為簡便。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)

## 額外資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下來學習

## 下一步驟

既然你已學會如何使用 stdio 傳輸建立 MCP 伺服器，可以探索更進階主題：

- <strong>下一步</strong>：[HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - 了解用於遠端伺服器的另一種傳輸機制
- <strong>進階</strong>：[MCP 安全最佳實踐](../../02-Security/README.md) - 在 MCP 伺服器實作安全措施
- <strong>生產環境</strong>：[部署策略](../09-deployment/README.md) - 部署你的伺服器供生產使用

## 額外資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言 SDK 參考
- [社群範例](../../06-CommunityContributions/README.md) - 更多社群貢獻的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而導致的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
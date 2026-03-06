# MCP 伺服器與 stdio 傳輸

> **⚠️ 重要更新**：根據 MCP 規範 2025-06-18，獨立的 SSE（Server-Sent Events）傳輸已被**棄用**，並由「可串流 HTTP (Streamable HTTP)」傳輸取代。當前 MCP 規範定義了兩種主要傳輸機制：
> 1. **stdio** - 標準輸入/輸出（建議用於本地伺服器）
> 2. **可串流 HTTP** - 用於可能在內部使用 SSE 的遠程伺服器
>
> 本課程已更新，重點放在**stdio 傳輸**，這是大多數 MCP 伺服器實現推薦的方式。

Stdio 傳輸允許 MCP 伺服器透過標準輸入與輸出串流與用戶端通訊。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供一種簡單高效的方式構建 MCP 伺服器，可輕鬆整合多種用戶端應用程式。

## 簡介

本課程涵蓋如何使用 stdio 傳輸構建及使用 MCP 伺服器。

## 學習目標

完成本課程後，您將能夠：

- 使用 stdio 傳輸構建 MCP 伺服器。
- 使用 Inspector 除錯 MCP 伺服器。
- 使用 Visual Studio Code 使用 MCP 伺服器。
- 了解當前 MCP 傳輸機制及為何推薦使用 stdio。

## stdio 傳輸 - 運作原理

stdio 傳輸是 MCP 目前規範（2025-06-18）支持的兩種傳輸類型之一。其工作方式如下：

- **簡單通訊**：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並向標準輸出（`stdout`）發送訊息。
- **以行程為基礎**：用戶端啟動 MCP 伺服器作為子行程。
- **訊息格式**：訊息是獨立的 JSON-RPC 請求、通知或回應，以換行符分隔。
- **日誌記錄**：伺服器可寫入 UTF-8 字串到標準錯誤（`stderr`）作為日誌。

### 主要要求：
- 訊息**必須**以換行符劃分，且**不得**含有嵌入換行符
- 伺服器**不得**向 `stdout` 寫入非有效 MCP 訊息
- 用戶端**不得**向伺服器的 `stdin` 寫入非有效 MCP 訊息

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

- 我們從 MCP SDK 匯入 `Server` 類別與 `StdioServerTransport`
- 創建一個具有基本配置和能力的伺服器實例

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

- 使用 MCP SDK 創建伺服器實例
- 利用裝飾器定義工具
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

與 SSE 的關鍵區別在於 stdio 伺服器：

- 不需要網頁伺服器設置或 HTTP 端點
- 由用戶端作為子行程啟動
- 透過 stdin/stdout 串流通訊
- 更簡單實現與除錯

## 練習：建立 stdio 伺服器

建立伺服器時，我們需記得：

- 需使用網頁伺服器公開連線與訊息端點。

## 實驗：建立簡單 MCP stdio 伺服器

本實驗將使用推薦的 stdio 傳輸創建簡單 MCP 伺服器。該伺服器將公開可供用戶端透過標準 Model Context Protocol 呼叫的工具。

### 前置條件

- Python 3.8 或以上版本
- MCP Python SDK：`pip install mcp`
- 對非同步程式設計有基本了解

現在開始建立第一個 MCP stdio 伺服器：

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
- 簡單子行程模型 — 用戶端啟動伺服器作為子行程
- 透過 stdin/stdout 使用 JSON-RPC 訊息通訊
- 不需設置 HTTP 伺服器
- 性能與安全性更佳
- 更方便除錯與開發

**SSE 傳輸（自 MCP 2025-06-18 起棄用）：**
- 需要 HTTP 伺服器並設有 SSE 端點
- 設置更複雜，需網頁伺服器架構
- HTTP 端點有額外安全性考量
- 現由可串流 HTTP 取代，適用網頁場景

### 使用 stdio 傳輸建立伺服器

建立 stdio 伺服器時，我們需要：

1. **匯入所需函式庫** — MCP 伺服器元件與 stdio 傳輸
2. **創建伺服器實例** — 定義伺服器及其能力
3. **定義工具** — 新增要公開的功能
4. **設定傳輸** — 配置 stdio 通訊
5. **啟動伺服器** — 開始伺服器並處理訊息

讓我們一步步來實作：

### 步驟 1：建立基本 stdio 伺服器

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

將程式碼儲存為 `server.py` 並從命令列執行：

```bash
python server.py
```

伺服器將啟動並等待來自 `stdin` 的輸入。它透過 stdio 傳輸使用 JSON-RPC 訊息通訊。

### 步驟 4：使用 Inspector 測試

您可以使用 MCP Inspector 測試伺服器：

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

MCP Inspector 是除錯與測試 MCP 伺服器的重要工具。以下說明如何用它搭配 stdio 伺服器：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **啟動 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **測試你的伺服器**：Inspector 提供網頁介面，可：
   - 檢視伺服器能力
   - 使用不同參數測試工具
   - 監控 JSON-RPC 訊息
   - 除錯連線問題

### 使用 VS Code

你也可以直接在 VS Code 除錯 MCP 伺服器：

1. 在 `.vscode/launch.json` 裡建立啟動設定：
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
3. 啟動除錯器並搭配 Inspector 測試

### 常見除錯技巧

- 使用 `stderr` 作為日誌用途 — 絕不要寫入 `stdout`，因其保留給 MCP 訊息
- 確保所有 JSON-RPC 訊息均以換行符分隔
- 先用簡單工具測試，再加複雜功能
- 使用 Inspector 驗證訊息格式

## 在 VS Code 使用你的 stdio 伺服器

建置好 MCP stdio 伺服器後，你可以將它與 VS Code 整合，並搭配 Claude 或其他 MCP 相容用戶端使用。

### 配置

1. **建立 MCP 配置文件**，路徑為 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

2. **重新啟動 Claude**：關閉並重新打開 Claude 以載入新伺服器配置。

3. **測試連線**：與 Claude 開始新對話並嘗試使用伺服器工具：
   -「你可以用問候工具向我打招呼嗎？」
   -「計算 15 與 27 的總和」
   -「伺服器資訊是什麼？」

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

// 加入工具
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

在本更新課程中，你學會了：

- 使用現行**stdio 傳輸**建構 MCP 伺服器（推薦方法）
- 了解為何 SSE 傳輸被棄用，並改由 stdio 與可串流 HTTP 取代
- 創建 MCP 用戶端可呼叫的工具
- 使用 MCP Inspector 除錯伺服器
- 將 stdio 伺服器整合進 VS Code 與 Claude

與已棄用的 SSE 方法相比，stdio 傳輸提供了更簡單、更安全及效能更佳的 MCP 伺服器建構方式。它是截至 2025-06-18 規範推薦給大多數 MCP 伺服器實現的傳輸機制。

### .NET

1. 先建立一些工具，我們將建立一個檔案 *Tools.cs*，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試你的 stdio 伺服器

既然你已經建置好 stdio 伺服器，現在讓我們測試它以確保運作正常。

### 前置條件

1. 確認已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 伺服器程式碼已儲存（例如 `server.py`）

### 使用 Inspector 測試

1. **與你的伺服器一起啟動 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打開網頁介面**：Inspector 將開啟瀏覽器視窗，顯示你伺服器的能力。

3. **測試工具**：
   - 嘗試使用不同名稱呼叫 `get_greeting` 工具
   - 用多組數字測試 `calculate_sum` 工具
   - 呼叫 `get_server_info` 工具查看伺服器元資料

4. **監控通訊**：Inspector 會顯示用戶端與伺服器間交換的 JSON-RPC 訊息。

### 你應該看到什麼

當伺服器正確啟動，你會看到：
- 伺服器能力列在 Inspector 中
- 工具可供測試
- JSON-RPC 訊息交換成功
- 工具回應在介面顯示

### 常見問題與解決方案

**伺服器無法啟動：**
- 確認所有相依已安裝：`pip install mcp`
- 檢查 Python 語法及縮排
- 留意主控台中的錯誤訊息

**工具未出現：**
- 確保有使用 `@server.tool()` 裝飾器
- 工具函式需於 `main()` 前定義
- 確認伺服器設定正確

**連線問題：**
- 確保伺服器正確使用 stdio 傳輸
- 檢查是否有其他行程干擾
- 驗證 Inspector 指令語法正確

## 作業

嘗試擴充你的伺服器能力。可參考[此頁](https://api.chucknorris.io/)來新增連接 API 的工具。伺服器內容由你決定，祝你玩得開心 :)

## 解答

[解答](./solution/README.md) 這裡提供一個可執行的範例解答。

## 重點整理

本章關鍵重點如下：

- stdio 傳輸是本地 MCP 伺服器推薦的通訊機制。
- stdio 傳輸利用標準輸入輸出串流，讓 MCP 伺服器與用戶端間通訊無縫順暢。
- 你可以直接使用 Inspector 及 Visual Studio Code 使用 stdio 伺服器，讓除錯與整合更簡單。

## 範例 

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python) 

## 額外資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下來

## 下一步

學會使用 stdio 傳輸建立 MCP 伺服器後，你可以探索更進階主題：

- **下一步**：[MCP HTTP 串流 (可串流 HTTP)](../06-http-streaming/README.md) - 了解遠程伺服器使用的其他傳輸機制
- **進階**：[MCP 安全最佳實務](../../02-Security/README.md) - 在你的 MCP 伺服器中實現安全機制
- **生產環境**：[部署策略](../09-deployment/README.md) - 伺服器生產環境部署

## 額外資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言 SDK 參考文件
- [社群範例](../../06-CommunityContributions/README.md) - 更多社群提供的伺服器範例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能存在錯誤或不準確之處。原文的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用此翻譯所引致的任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
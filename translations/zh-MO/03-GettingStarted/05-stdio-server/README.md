# MCP 伺服器與 stdio 傳輸

> **⚠️ 重要更新**：自 MCP 規範 2025-06-18 起，獨立的 SSE（伺服器推送事件）傳輸已被**棄用**，並由「Streamable HTTP」傳輸取代。目前的 MCP 規範定義了兩種主要的傳輸機制：
> 1. **stdio** - 標準輸入/輸出（建議用於本地伺服器）
> 2. **Streamable HTTP** - 適用於可能內部使用 SSE 的遠端伺服器
>
> 本課程已更新為專注於 **stdio 傳輸**，這是大多數 MCP 伺服器實作的推薦方法。

stdio 傳輸允許 MCP 伺服器通過標準輸入和輸出流與客戶端進行通信。這是目前 MCP 規範中最常用且推薦的傳輸機制，提供了一種簡單且高效的方式來構建 MCP 伺服器，並能輕鬆整合到各種客戶端應用中。

## 概述

本課程將介紹如何使用 stdio 傳輸來構建和使用 MCP 伺服器。

## 學習目標

完成本課程後，您將能夠：

- 使用 stdio 傳輸構建 MCP 伺服器。
- 使用 Inspector 偵錯 MCP 伺服器。
- 使用 Visual Studio Code 消費 MCP 伺服器。
- 理解目前的 MCP 傳輸機制以及為何推薦使用 stdio。

## stdio 傳輸 - 運作方式

stdio 傳輸是目前 MCP 規範（2025-06-18）支持的兩種傳輸類型之一。其運作方式如下：

- **簡單通信**：伺服器從標準輸入（`stdin`）讀取 JSON-RPC 訊息，並將訊息發送到標準輸出（`stdout`）。
- **基於進程**：客戶端將 MCP 伺服器作為子進程啟動。
- **訊息格式**：訊息是單獨的 JSON-RPC 請求、通知或回應，以換行符分隔。
- **日誌記錄**：伺服器可以將 UTF-8 字串寫入標準錯誤（`stderr`）作為日誌記錄。

### 關鍵要求：
- 訊息**必須**以換行符分隔，且**不得**包含嵌入的換行符。
- 伺服器**不得**向 `stdout` 寫入任何非 MCP 訊息的內容。
- 客戶端**不得**向伺服器的 `stdin` 寫入任何非 MCP 訊息的內容。

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

- 我們從 MCP SDK 匯入了 `Server` 類別和 `StdioServerTransport`。
- 我們使用基本配置和功能創建了一個伺服器實例。

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

- 使用 MCP SDK 創建了一個伺服器實例。
- 使用裝飾器定義工具。
- 使用 `stdio_server` 上下文管理器處理傳輸。

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

與 SSE 的主要區別在於 stdio 伺服器：

- 不需要設置網頁伺服器或 HTTP 端點。
- 由客戶端作為子進程啟動。
- 通過 stdin/stdout 流進行通信。
- 更易於實作和偵錯。

## 練習：創建一個 stdio 伺服器

要創建我們的伺服器，需要記住以下兩點：

- 我們需要使用網頁伺服器來暴露連接和訊息的端點。

## 實驗：創建一個簡單的 MCP stdio 伺服器

在本實驗中，我們將使用推薦的 stdio 傳輸創建一個簡單的 MCP 伺服器。此伺服器將暴露工具，供客戶端使用標準的 Model Context Protocol 調用。

### 先決條件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 基本的異步編程知識

讓我們開始創建第一個 MCP stdio 伺服器：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 與已棄用的 SSE 方法的主要區別

**Stdio 傳輸（目前標準）：**
- 簡單的子進程模型 - 客戶端將伺服器作為子進程啟動。
- 通過 stdin/stdout 使用 JSON-RPC 訊息進行通信。
- 不需要設置 HTTP 伺服器。
- 性能和安全性更佳。
- 更易於偵錯和開發。

**SSE 傳輸（自 MCP 2025-06-18 起棄用）：**
- 需要具有 SSE 端點的 HTTP 伺服器。
- 需要更複雜的網頁伺服器基礎設施。
- 需要額外考慮 HTTP 端點的安全性。
- 現已被 Streamable HTTP 替代，用於基於網頁的場景。

### 使用 stdio 傳輸創建伺服器

要創建 stdio 伺服器，我們需要：

1. **匯入所需的庫** - 我們需要 MCP 伺服器組件和 stdio 傳輸。
2. **創建伺服器實例** - 定義伺服器及其功能。
3. **定義工具** - 添加我們想要暴露的功能。
4. **設置傳輸** - 配置 stdio 通信。
5. **運行伺服器** - 啟動伺服器並處理訊息。

讓我們逐步構建：

### 第一步：創建一個基本的 stdio 伺服器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### 第二步：添加更多工具

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

### 第三步：運行伺服器

將程式碼保存為 `server.py`，並從命令行運行：

```bash
python server.py
```

伺服器將啟動並等待來自 stdin 的輸入。它通過 stdio 傳輸使用 JSON-RPC 訊息進行通信。

### 第四步：使用 Inspector 測試

您可以使用 MCP Inspector 測試您的伺服器：

1. 安裝 Inspector：`npx @modelcontextprotocol/inspector`
2. 運行 Inspector 並指向您的伺服器。
3. 測試您創建的工具。

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## 偵錯您的 stdio 伺服器

### 使用 MCP Inspector

MCP Inspector 是一個用於偵錯和測試 MCP 伺服器的寶貴工具。以下是如何將其與您的 stdio 伺服器一起使用：

1. **安裝 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **運行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **測試您的伺服器**：Inspector 提供了一個網頁界面，您可以：
   - 查看伺服器功能。
   - 使用不同參數測試工具。
   - 監控 JSON-RPC 訊息。
   - 偵錯連接問題。

### 使用 VS Code

您也可以直接在 VS Code 中偵錯您的 MCP 伺服器：

1. 在 `.vscode/launch.json` 中創建啟動配置：
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

2. 在伺服器程式碼中設置斷點。
3. 運行偵錯器並使用 Inspector 測試。

### 常見偵錯提示

- 使用 `stderr` 記錄日誌 - 切勿向 `stdout` 寫入內容，因為它保留給 MCP 訊息。
- 確保所有 JSON-RPC 訊息都以換行符分隔。
- 先測試簡單工具，再添加複雜功能。
- 使用 Inspector 驗證訊息格式。

## 在 VS Code 中消費您的 stdio 伺服器

構建 MCP stdio 伺服器後，您可以將其整合到 VS Code 中，與 Claude 或其他 MCP 相容的客戶端一起使用。

### 配置

1. **創建 MCP 配置檔案**，位於 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

2. **重新啟動 Claude**：關閉並重新打開 Claude 以加載新的伺服器配置。

3. **測試連接**：與 Claude 開始對話並嘗試使用伺服器的工具：
   - 「你能用問候工具向我問好嗎？」
   - 「計算 15 和 27 的總和。」
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

// Add tools
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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 總結

在本更新課程中，您學習了如何：

- 使用目前的 **stdio 傳輸**（推薦方法）構建 MCP 伺服器。
- 理解為何 SSE 傳輸被棄用，並由 stdio 和 Streamable HTTP 取代。
- 創建可供 MCP 客戶端調用的工具。
- 使用 MCP Inspector 偵錯您的伺服器。
- 將您的 stdio 伺服器整合到 VS Code 和 Claude 中。

與已棄用的 SSE 方法相比，stdio 傳輸提供了一種更簡單、更安全且性能更高的方式來構建 MCP 伺服器。根據 2025-06-18 規範，這是大多數 MCP 伺服器實作的推薦傳輸方式。

### .NET

1. 讓我們先創建一些工具，為此我們將創建一個名為 *Tools.cs* 的檔案，內容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 練習：測試您的 stdio 伺服器

現在您已經構建了 stdio 伺服器，讓我們測試它以確保其正常運作。

### 先決條件

1. 確保您已安裝 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 您的伺服器程式碼應已保存（例如，作為 `server.py`）。

### 使用 Inspector 測試

1. **使用您的伺服器啟動 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打開網頁界面**：Inspector 將打開一個瀏覽器窗口，顯示您的伺服器功能。

3. **測試工具**：
   - 嘗試使用不同的名字測試 `get_greeting` 工具。
   - 使用各種數字測試 `calculate_sum` 工具。
   - 調用 `get_server_info` 工具查看伺服器元數據。

4. **監控通信**：Inspector 顯示客戶端和伺服器之間交換的 JSON-RPC 訊息。

### 您應該看到的結果

當您的伺服器正確啟動時，您應該看到：
- Inspector 中列出的伺服器功能。
- 可供測試的工具。
- 成功的 JSON-RPC 訊息交換。
- 工具回應顯示在界面中。

### 常見問題及解決方案

**伺服器無法啟動：**
- 檢查是否已安裝所有依賴項：`pip install mcp`
- 驗證 Python 語法和縮排。
- 查看控制台中的錯誤訊息。

**工具未顯示：**
- 確保存在 `@server.tool()` 裝飾器。
- 檢查工具函數是否定義在 `main()` 之前。
- 驗證伺服器是否正確配置。

**連接問題：**
- 確保伺服器正確使用 stdio 傳輸。
- 檢查是否有其他進程干擾。
- 驗證 Inspector 命令語法。

## 作業

嘗試為您的伺服器添加更多功能。例如，參考 [這個頁面](https://api.chucknorris.io/) 添加一個調用 API 的工具。您可以自行設計伺服器的外觀和功能。玩得開心 :)

## 解答

[解答](./solution/README.md) 提供了一個可能的解決方案及可運行的程式碼。

## 關鍵要點

本章的關鍵要點如下：

- stdio 傳輸是本地 MCP 伺服器的推薦機制。
- stdio 傳輸允許 MCP 伺服器和客戶端通過標準輸入和輸出流無縫通信。
- 您可以直接使用 Inspector 和 Visual Studio Code 消費 stdio 伺服器，這使得偵錯和整合變得簡單。

## 範例

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python) 

## 其他資源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 下一步

## 下一步行動

現在您已經學會如何使用 stdio 傳輸構建 MCP 伺服器，您可以探索更高級的主題：

- **下一步**：[MCP 的 HTTP 串流（Streamable HTTP）](../06-http-streaming/README.md) - 學習遠端伺服器的另一種支持的傳輸機制。
- **進階**：[MCP 安全最佳實踐](../../02-Security/README.md) - 在您的 MCP 伺服器中實現安全性。
- **生產環境**：[部署策略](../09-deployment/README.md) - 將您的伺服器部署到生產環境。

## 其他資源

- [MCP 規範 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方規範。
- [MCP SDK 文件](https://github.com/modelcontextprotocol/sdk) - 各語言的 SDK 參考。
- [社群範例](../../06-CommunityContributions/README.md) - 更多來自社群的伺服器範例。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
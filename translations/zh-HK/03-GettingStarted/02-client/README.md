# 建立客戶端

客戶端是與 MCP 伺服器直接通訊的自訂應用程式或腳本，用來請求資源、工具和提示。與使用檢查器工具（提供圖形介面與伺服器互動）不同，自行編寫客戶端可實現程式化和自動化的互動，讓開發者能將 MCP 功能整合到自己的工作流程中，自動完成任務，並構建符合特定需求的自訂解決方案。

## 概述

本課程介紹 MCP 生態系統中的客戶端概念。你將學會如何編寫屬於自己的客戶端並連接至 MCP 伺服器。

## 學習目標

完成本課程後，你將能夠：

- 了解客戶端的功能。
- 編寫自己的客戶端。
- 與 MCP 伺服器連接並測試，確保伺服器正常運作。

## 編寫客戶端需要什麼？

要編寫客戶端，需要做到以下幾點：

- **匯入正確的函式庫**。你將使用與之前相同的函式庫，但會用不同的結構。
- **實例化客戶端**。建立客戶端實例並透過選擇的傳輸方式連接。
- **決定要列出哪些資源**。你的 MCP 伺服器上有資源、工具和提示，你需要決定要列出哪些。
- **將客戶端整合到主機應用程式中**。當你了解伺服器功能後，需要將它整合到主機應用程式中，當使用者輸入提示或命令時，即可呼叫對應的伺服器功能。

了解了高階流程後，我們接著看看範例。

### 範例客戶端

來看看這個範例客戶端：

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// 列出提示
const prompts = await client.listPrompts();

// 取得提示
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// 列出資源
const resources = await client.listResources();

// 閱讀資源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 調用工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

在上述程式碼中，我們：

- 匯入函式庫
- 建立使用 stdio 傳輸連接的客戶端實例
- 列出提示、資源及工具並呼叫它們

這就是一個能與 MCP 伺服器溝通的客戶端。

接下來的練習部分，我們會逐段拆解程式碼並說明細節。

## 練習：編寫客戶端

如上所述，我們會花些時間說明程式碼，也歡迎你跟著編寫。

### -1- 匯入函式庫

先匯入需要的函式庫，需要使用客戶端和傳輸協議 stdio 的參考。stdio 是用於本機執行的協議，SSE 是未來章節會提及的另一個傳輸選項。目前先使用 stdio。

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

對於 Java，請在你之前 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 範例的 Java Spring Boot 專案中，於 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾建立新類別 `SDKClient`，並加入以下匯入：

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

你需要在 `Cargo.toml` 中新增以下相依：

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

之後便可在客戶端程式中匯入相關函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接下來進行實例化。

### -2- 實例化客戶端與傳輸

需要建立傳輸和客戶端的實例：

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

上述程式碼：

- 建立了 stdio 傳輸實例，並指定如何找到及啟動伺服器的命令與參數，因為建立客戶端時需要啟動伺服器。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 實例化了客戶端，給定名稱與版本。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 透過先前建立的傳輸連接客戶端。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 建立用於 stdio 連接的服務器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行文件
    args=["run", "server.py"],  # 選用的命令行參數
    env=None,  # 選用的環境變數
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 初始化連接
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

上述程式碼：

- 匯入所需函式庫
- 建立伺服器參數物件，用來啟動伺服器以便客戶端連接
- 定義 `run` 方法，該方法呼叫 `stdio_client`，啟動客戶端會話
- 建立進入點，透過 `asyncio.run` 執行 `run` 方法

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

上述程式碼：

- 匯入需要的函式庫
- 建立 stdio 傳輸並建立 `mcpClient` 客戶端，後者用來列出及呼叫 MCP 伺服器功能

注意在「Arguments」中，你可以指定 *.csproj* 或可執行檔。

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // 您的客戶端邏輯寫在這裡
    }
}
```

上述程式碼：

- 建立 main 方法，設置 SSE 傳輸指向 `http://localhost:8080`，即 MCP 伺服器所在地
- 建立客戶端類別，建構子接受傳輸物件
- 在 `run` 方法中，建立同步 MCP 客戶端並初始化連線
- 使用 SSE（Server-Sent Events）傳輸，適合與 Java Spring Boot MCP 伺服器通訊的 HTTP 方案

#### Rust

此 Rust 範例假設伺服器為同一目錄下名為 "calculator-server" 的鄰近專案，以下程式碼會啟動伺服器並連接。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設服務器是同一目錄下名為 "calculator-server" 的兄弟項目
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: 初始化

    // TODO: 列出工具

    // TODO: 用參數 = {"a": 3, "b": 2} 呼叫加法工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

我們有個可連接的客戶端，但尚未列出功能，接著來做此事：

#### TypeScript

```typescript
// 列出提示
const prompts = await client.listPrompts();

// 列出資源
const resources = await client.listResources();

// 列出工具
const tools = await client.listTools();
```

#### Python

```python
# 列出可用資源
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 列出可用工具
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

這裡列出可用的資源 `list_resources()` 和工具 `list_tools`，並將它們印出。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

範例示範如何列出伺服器上的工具，並印出工具名稱。

#### Java

```java
// 列出並示範工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 你亦可以 ping 伺服器以驗證連線
client.ping();
```

上述程式碼：

- 呼叫 `listTools()` 獲取 MCP 伺服器的所有工具
- 使用 `ping()` 確認與伺服器的連接工作正常
- `ListToolsResult` 物件包含工具的名稱、描述及輸入結構

很好，現在已取得所有功能。接著問題是何時呼叫它們？此客戶端相當簡單，需要在想使用時明確呼叫功能。下一章我們會建立更進階、具備自有大型語言模型（LLM）的客戶端。現在先看看如何呼叫伺服器功能：

#### Rust

主函式中，初始化客戶端後可以啟動伺服器並列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 呼叫功能

呼叫功能時需確保指定正確參數，有時還要指定欲呼叫的功能名稱。

#### TypeScript

```typescript

// 讀取資源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 調用工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// 調用提示
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

程式碼中，我們：

- 讀取一個資源，透過呼叫 `readResource()` 並指定 `uri`。伺服器端可能的程式碼如下：

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    其中 `uri` 的值 `file://example.txt` 對應伺服器端的 `file://{name}`，`example.txt` 被映射到 `name`。

- 呼叫工具，傳入工具名稱 `name` 及參數 `arguments`：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，呼叫 `getPrompt()` 並傳入 `name` 和 `arguments`，伺服器程式碼範例如下：

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    所以客戶端呼叫程式碼會長這樣，對應伺服器定義：

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# 讀取資源
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# 呼叫工具
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

程式中，我們：

- 呼叫名為 `greeting` 的資源，使用 `read_resource`
- 呼叫名為 `add` 的工具，使用 `call_tool`

#### .NET

1. 新增呼叫工具的程式碼：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 印出結果的範例：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// 調用各種計算器工具
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

上述程式碼：

- 透過 `callTool()` 和 `CallToolRequest` 物件呼叫多個計算器工具
- 每次呼叫指定工具名稱及工具所需參數的 `Map`
- 伺服器端工具期待特定的參數名稱（例如數學運算的 "a"、"b"）
- 伺服器回傳結果封裝在 `CallToolResult` 物件中

#### Rust

```rust
// 以參數 {"a": 3, "b": 2} 呼叫 add 工具
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- 執行客戶端

在終端機輸入以下指令執行客戶端：

#### TypeScript

將下列加入 *package.json* 的 "scripts" 區段：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

使用此指令呼叫客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

先確保 MCP 伺服器啟動於 `http://localhost:8080`，然後執行客戶端：

```bash
# 建立你的專案
./mvnw clean compile

# 執行客戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或執行方案資料夾 `03-GettingStarted\02-client\solution\java` 的完整客戶端專案：

```bash
# 導覽至解決方案目錄
cd 03-GettingStarted/02-client/solution/java

# 建置並執行 JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作業

這次作業將應用所學，建立自己的客戶端。

這有一個可用伺服器，你的客戶端需呼叫它，試試能否新增更多功能以讓伺服器更有趣。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 建立一個 MCP 伺服器
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 新增一個加法工具
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 新增一個動態問候資源
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// 開始在標準輸入接收訊息及在標準輸出發送訊息

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# 建立一個 MCP 伺服器
mcp = FastMCP("Demo")


# 新增一個加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 新增一個動態問候資源
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

可參考此專案學習如何 [新增提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另外，也請查看此連結如何呼叫 [提示及資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在 [上一節](../../../../03-GettingStarted/01-first-server) 中，你學會如何用 Rust 建立簡單 MCP 伺服器。你可接著擴充它，或參考此連結查看更多基於 Rust 的 MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

**解答資料夾**包含完整可運作的客戶端實作，示範本教程涵蓋的所有概念。每個解答都包含客戶端與伺服器程式碼，分別在獨立自給專案中組織。

### 📁 解答結構

解答目錄依程式語言分類：

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 每個解答包含內容

每個語言專屬解答提供：

- **完整客戶端實作**，涵蓋課程所有功能
- **運作中專案結構**，含恰當相依和組態
- **建置及執行腳本**，方便設定與執行
- **詳細 README**，包含語言特定指示
- **錯誤處理與結果處理範例**

### 📖 使用解答

1. **進入你偏好的語言資料夾**：

   ```bash
   cd solution/typescript/    # 適用於 TypeScript
   cd solution/java/          # 適用於 Java
   cd solution/python/        # 適用於 Python
   cd solution/dotnet/        # 適用於 .NET
   ```

2. **依 README 指示操作**，包括：
   - 安裝相依
   - 專案建置
   - 執行客戶端

3. **你應該會看到如下範例輸出**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完整文件與逐步教學，請參考：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了所有本教程涵蓋語言的完整、可執行客戶端實作範例。這些範例示範了上述完整功能，可以作參考實作或作為你自己專案的起點。

### 可用的完整範例

| 語言 | 檔案 | 描述 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 傳輸的完整 Java 客戶端，具完善錯誤處理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 傳輸，能自動啟動伺服器的完整 C# 客戶端 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 完整 MCP 協定支援的 TypeScript 客戶端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用 async/await 模式的完整 Python 客戶端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 實現非同步運作的完整 Rust 客戶端 |

各個完整範例包含：
- ✅ **連線建立** 與錯誤處理
- ✅ **伺服器發現**（工具、資源、提示視情況而定）
- ✅ **計算機操作**（加、減、乘、除、幫助）
- ✅ **結果處理** 與格式化輸出
- ✅ **全面錯誤處理**
- ✅ **乾淨、有註解的程式碼**，附逐步說明

### 完整範例入門指南

1. **從上表選擇你偏好的語言**
2. **查看完整範例檔案** 以了解完整實作
3. **依照 [`complete_examples.md`](./complete_examples.md) 指示執行範例**
4. **修改並擴充** 範例以符合你的特定需求

關於執行及自訂這些範例的詳細文件，請參考：**[📖 完整範例文件](./complete_examples.md)**

### 💡 解決方案與完整範例比較

| **解決方案資料夾** | **完整範例** |
|--------------------|-------------|
| 含建置檔案的完整專案結構 | 單檔案實作範例 |
| 具備依賴且可直接執行 | 專注的程式碼範例 |
| 類似生產環境的設定 | 教育參考用 |
| 針對語言的工具鏈 | 跨語言比較 |

兩種方式都很有價值 —— 使用 **解決方案資料夾** 來打造完整專案，使用 **完整範例** 作為學習與參考。

## 重要重點

本章關於用戶端的重點如下：

- 可用於發現並呼叫伺服器上的功能。
- 可以在啟動自己時啟用伺服器（如本章所述），但用戶端也能連線到已在運行的伺服器。
- 是測試伺服器功能的好方法，與前章所述的 Inspector 等替代方案並行使用。

## 額外資源

- [在 MCP 中建立用戶端](https://modelcontextprotocol.io/quickstart/client)

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 接下來

- 下一步：[使用 LLM 建立用戶端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
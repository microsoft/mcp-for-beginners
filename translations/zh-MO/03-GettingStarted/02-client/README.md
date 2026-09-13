# 建立客戶端

客戶端是自訂應用程式或腳本，直接與 MCP 伺服器通訊以請求資源、工具和提示。與使用檢查器工具不同，後者提供與伺服器互動的圖形界面，而編寫自己的客戶端則允許程式化和自動化的互動。這使得開發人員能將 MCP 功能整合到自己的工作流程中，自動化任務，並打造符合特定需求的自訂解決方案。

## 概述

本課介紹 Model Context Protocol (MCP) 生態系中的客戶端概念。您將學習如何撰寫自己的客戶端並連線到 MCP 伺服器。

## 學習目標

在本課結束時，您將能夠：

- 了解客戶端的功能。
- 撰寫您自己的客戶端。
- 連接並測試客戶端與 MCP 伺服器，確保其運作正常。

## 撰寫客戶端需要什麼？

撰寫客戶端時，您需要執行以下步驟：

- <strong>匯入正確的函式庫</strong>。您將會使用與之前相同的函式庫，只是使用不同結構。
- <strong>實例化客戶端</strong>。這會涉及建立客戶端實例並連接到選擇的通訊傳輸方式。
- <strong>決定要列出哪些資源</strong>。您的 MCP 伺服器帶有資源、工具和提示，您需要決定列出其中的哪一項。
- <strong>將客戶端整合到主機應用程式</strong>。一旦了解伺服器能力，您需要將此整合到主機應用程式，讓使用者輸入提示或指令時，能呼叫相應的伺服器功能。

現在我們大致了解接下來要做的事，讓我們看一下範例。

### 範例客戶端

讓我們看看這個範例客戶端：

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

// 呼叫工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

在上面程式碼，我們：

- 匯入函式庫
- 建立客戶端實例並使用 stdio 做為傳輸連接。
- 列出提示、資源和工具並呼叫它們。

就是這樣，一個能與 MCP 伺服器通訊的客戶端誕生了。

下一個練習部分我們將慢慢拆解每段程式碼並解釋其運作原理。

## 練習：撰寫客戶端

如前所述，我們慢慢解說程式碼，如果您願意，歡迎一起實作。

### -1- 匯入函式庫

先匯入我們需要的函式庫，我們需要引用客戶端以及所選通訊協定 stdio。stdio 是設計在本機執行的通訊協定。SSE 是另一個通訊協定，會在未來章節介紹，但目前先以 stdio 進行。

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

對於 Java，您將建立一個連線至前一練習的 MCP 伺服器之客戶端。使用 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 範例中的 Java Spring Boot 專案結構，於 `src/main/java/com/microsoft/mcp/sample/client/` 目錄內建立新的 Java 類別 `SDKClient`，並加入以下匯入：

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

您需在 `Cargo.toml` 文件中加入以下相依性。

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

從此，您就可以在客戶端程式碼中匯入所需函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接著進入實例化部分。

### -2- 實例化客戶端與傳輸

我們需要建立傳輸實例以及客戶端實例：

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

在上方程式中我們：

- 建立 stdio 傳輸實例。注意它如何指定指令及參數以搜尋並啟動伺服器，這是建立客戶端時必須處理的部分。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 透過名稱與版本實例化客戶端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 將客戶端連接至所選用的傳輸。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 建立 stdio 連線的伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 可選的命令列參數
    env=None,  # 可選的環境變數
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 初始化連線
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

在上述程式中我們：

- 匯入必要函式庫
- 實例化伺服器參數物件，用以運行伺服器並讓客戶端連線。
- 定義一個 `run` 方法，呼叫 `stdio_client` 啟動客戶端工作階段。
- 建立一個入口點，將 `run` 方法提供給 `asyncio.run` 執行。

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

在上述程式中，我們：

- 匯入必要函式庫。
- 建立 stdio 傳輸並建立名為 `mcpClient` 的客戶端，後者用於列出與呼叫 MCP 伺服器功能。

注意在 "Arguments" 欄，您可以指定 *.csproj* 檔案或執行檔。

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
        
        // 你嘅客戶端邏輯寫喺呢度
    }
}
```

在上述程式中，我們：

- 建立 main 方法，設定 SSE 傳輸，指向我們在 `http://localhost:8080` 執行的 MCP 伺服器。
- 建立一個客戶端類別，建構子參數為該傳輸。
- 在 `run` 方法中創建同步 MCP 客戶端並初始化連線。
- 使用 SSE（伺服器發送事件）傳輸，適合與 Java Spring Boot MCP 伺服器的 HTTP 通訊。

#### Rust

注意此 Rust 客戶端假設伺服器是同一目錄下名為 "calculator-server" 的兄弟專案。下方程式啟動伺服器並連線。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設伺服器是一個名為 "calculator-server" 的同層級專案，位於同一目錄下
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

    // 待辦事項：初始化

    // 待辦事項：列出工具

    // 待辦事項：使用參數 {"a": 3, "b": 2} 呼叫 add 工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

現在，當程式執行時，我們有一個能連線的客戶端。但它尚未列出功能，接下來來實作這部分：

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

此處我們列出可用資源 `list_resources()` 和工具 `list_tools`，並印出它們。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

以上為如何列出伺服器上的工具範例，並對每個工具印出其名稱。

#### Java

```java
// 列出及示範工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 你亦可以 Ping 伺服器以驗證連接
client.ping();
```

在上述程式我了：

- 呼叫 `listTools()` 取得 MCP 伺服器所有可用工具。
- 使用 `ping()` 驗證與伺服器之連線是否正常。
- `ListToolsResult` 物件包含所有工具資訊，包含名稱、描述與輸入結構。

很好，現在取得所有功能。問題是何時使用它們？此客戶端很簡單，意味須明確呼叫相應功能。下一章我們會建立更進階的客戶端，並能存取它自己的大型語言模型 (LLM)。不過先看看如何呼叫伺服器功能：

#### Rust

在 main 函數中，初始化客戶端後，可初始化伺服器並列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 呼叫功能

要呼叫功能需指定正確的參數，某些情況還需指定呼叫名稱。

#### TypeScript

```typescript

// 閱讀資源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 呼叫工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// 呼叫提示
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

在上述程式中，我們：

- 讀取資源，我們呼叫 `readResource()` 並指定 `uri`。伺服器端大概是這模樣：

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

    我們的 `uri` 值 `file://example.txt` 對應伺服器的 `file://{name}`。`example.txt` 會綁定至 `name`。

- 呼叫工具，透過指定工具 `name` 及其 `arguments` 來呼叫：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，呼叫 `getPrompt()` 並指定 `name` 與 `arguments`。伺服器程式碼如下：

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

    你的客戶端程式碼如上，即與伺服器宣告相符：

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
# 讀取一個資源
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# 調用一個工具
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

在上述程式中，我們：

- 呼叫名為 `greeting` 的資源，使用 `read_resource`。
- 呼叫名為 `add` 的工具，使用 `call_tool`。

#### .NET

1. 我們加了程式碼來呼叫工具：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 用以下程式碼印出結果：

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

在上述程式中，我們：

- 使用 `callTool()` 方法與 `CallToolRequest` 對象多次呼叫計算機工具。
- 每次工具呼叫均指定工具名稱及其所需參數 `Map`。
- 伺服器工具期望特定參數名稱（例如數學運算的 "a", "b"）。
- 結果透過 `CallToolResult` 物件帶回伺服器回應。

#### Rust

```rust
// 呼叫加法工具，參數為 = {"a": 3, "b": 2}
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

要執行客戶端，請在終端機輸入下列指令：

#### TypeScript

將以下條目加入 *package.json* 的 "scripts" 區段：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

使用下方指令呼叫客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

先確定您的 MCP 伺服器正在 `http://localhost:8080` 運行，然後執行客戶端：

```bash
# 建構你的專案
./mvnw clean compile

# 執行客戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，您亦可直接執行方案資料夾 `03-GettingStarted\02-client\solution\java` 中提供的完整客戶端專案：

```bash
# 導航到解決方案目錄
cd 03-GettingStarted/02-client/solution/java

# 建構並執行 JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作業

本作業中，您將利用所學建立一個客戶端，但請創建屬於您自己的客戶端。

這裡有一個伺服器可供您透過客戶端程式碼呼叫，看看您能否幫伺服器加入更多功能來增加趣味。

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

// 開始從標準輸入接收訊息並在標準輸出發送訊息

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

# 建立一個MCP伺服器
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

請參閱此專案學習如何 [新增提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另可參考此連結學習如何呼叫 [提示與資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在 [前一部分](../../../../03-GettingStarted/01-first-server) 您已學會如何使用 Rust 建立簡易 MCP 伺服器。您可繼續擴展該伺服器，或參考這個連結取得更多 Rust MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

<strong>解答資料夾</strong> 包含完整且可直接執行的客戶端實作，示範本教學涵蓋的所有概念。每份解答包含獨立的客戶端與伺服器程式碼專案。

### 📁 解答結構

解答目錄依程式語言組織分類：

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

### 🚀 每套解答包含

各語言解答均提供：

- <strong>完整客戶端實作</strong>，涵蓋教學中所有功能
- <strong>完善專案結構</strong>，具備正確相依與設定
- <strong>建置與執行指令腳本</strong>，易於設定與執行
- **詳細 README**，提供語言特定指導
- <strong>錯誤處理</strong>與結果處理範例

### 📖 使用解答

1. <strong>進入您偏好的語言資料夾</strong>：

   ```bash
   cd solution/typescript/    # 用於 TypeScript
   cd solution/java/          # 用於 Java
   cd solution/python/        # 用於 Python
   cd solution/dotnet/        # 用於 .NET
   ```

2. **遵循每個資料夾內的 README 指示**，說明：
   - 安裝相依套件
   - 建置專案
   - 執行客戶端

3. <strong>您應會看到範例輸出</strong>：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

詳細說明與逐步指引，請參考：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了本教程覆蓋的所有程式語言的完整工作客戶端實作，這些範例展示上述功能，並可用作參考實作或您專案的起點。

### 可用的完整範例

| 語言 | 檔案 | 描述 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 傳輸的完整 Java 客戶端，具備完善的錯誤處理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 傳輸的完整 C# 客戶端，自動啟動伺服器 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 完整支援 MCP 協議的 TypeScript 客戶端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用 async/await 範式的完整 Python 客戶端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 作非同步作業的完整 Rust 客戶端 |

每份完整範例皆包含：

- ✅ <strong>連線建立與錯誤處理</strong>
- ✅ <strong>伺服器發現</strong>（可用工具、資源、提示）
- ✅ <strong>計算機運算功能</strong>（加、減、乘、除、說明）
- ✅ <strong>結果處理與格式化輸出</strong>
- ✅ <strong>完善的錯誤處理</strong>

- ✅ **乾淨、有註解的程式碼** 並附有逐步說明

### 使用完整範例快速上手

1. <strong>從上表選擇你偏好的程式語言</strong>
2. <strong>檢視完整範例檔案</strong>，了解完整實作內容
3. **依照 [`complete_examples.md`](./complete_examples.md) 的指示執行範例**
4. <strong>修改並擴充</strong> 範例以符合你的特定需求

有關執行及自訂這些範例的詳細文件，請參考：**[📖 完整範例文件](./complete_examples.md)**

### 💡 解決方案與完整範例比較

| <strong>解決方案資料夾</strong> | <strong>完整範例</strong> |
|--------------------|--------------------- |
| 完整專案結構，含建置檔案 | 單一檔案實作 |
| 可立即執行且包含相依性 | 專注於程式碼範例 |
| 類生產環境設定 | 教學參考 |
| 依語言特定工具 | 跨語言比較 |

兩種方式各有價值—使用 <strong>解決方案資料夾</strong> 來進行完整專案，使用 <strong>完整範例</strong> 做為學習與參考。

## 主要收穫

本章關於客戶端的主要收穫如下：

- 可用於伺服器功能的發現與呼叫。
- 可在伺服器啟動的同時啟動伺服器（如本章所示）且客戶端也能連接至已執行的伺服器。
- 是測試伺服器功能的好方法，與上一章提到的 Inspector 等其他工具相較。

## 額外資源

- [在 MCP 中建立客戶端](https://modelcontextprotocol.io/quickstart/client)

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.NET 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 接下來

- 下一步：[使用 LLM 建立客戶端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
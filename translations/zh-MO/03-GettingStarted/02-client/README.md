# 建立一個客戶端

客戶端是用來直接與 MCP 伺服器通訊的自訂應用程式或腳本，以請求資源、工具和提示。不同於使用檢查器工具（提供與伺服器互動的圖形介面），自行撰寫客戶端則允許程式化和自動化的互動。這讓開發者能將 MCP 功能整合進自己的工作流程，自動化任務，並建立符合特定需求的自訂解決方案。

## 概覽

本課程介紹 Model Context Protocol (MCP) 生態系統中的客戶端概念。你將學習如何撰寫自己的客戶端並連接到 MCP 伺服器。

## 學習目標

學完本課後，你將能夠：

- 理解客戶端能做什麼。
- 撰寫自己的客戶端。
- 連接並測試客戶端與 MCP 伺服器，以確保伺服器運作正常。

## 撰寫客戶端需要哪些步驟？

要撰寫客戶端，你需要做以下幾點：

- **引入正確的函式庫**。你會使用之前相同的函式庫，只是搭配不同的構造。
- **實例化客戶端**。這會包含建立一個客戶端實例並連接到選定的傳輸方法。
- **決定要列出哪些資源**。你的 MCP 伺服器包含資源、工具和提示，你需要決定要列出哪些。
- **將客戶端整合到主機應用程式**。一旦你瞭解伺服器的功能，就需要把它整合到主機應用程式中，這樣使用者輸入提示或其他指令時，對應的伺服器功能便會被呼叫。

現在我們對整體要做什麼有個了解，接著讓我們看個範例。

### 範例客戶端

來看這個範例客戶端：

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

// 獲取提示
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

在前面的程式碼中，我們：

- 引入函式庫
- 建立客戶端實例並使用 stdio 做為傳輸連接
- 列出提示、資源和工具，並全部呼叫執行

這樣我們就有了一個可以與 MCP 伺服器通訊的客戶端。

接下來的練習部分，我們會仔細解析每段程式碼並說明內容。

## 練習：撰寫客戶端

如上所述，讓我們慢慢解釋程式碼，當然你也可以跟著打程式碼。

### -1- 引入函式庫

先引入需要的函式庫，我們會參考客戶端和我們選擇的傳輸協定 stdio。stdio 是設計執行於本地機器的協定。SSE 是另一個傳輸協定，會在未來章節介紹。現在，先繼續用 stdio。

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

針對 Java，你會建立一個連接先前練習 MCP 伺服器的客戶端。使用 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 中相同的 Java Spring Boot 專案結構，在 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾建立一個名為 `SDKClient` 的新 Java 類別，並加入以下匯入：

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

你需要在 `Cargo.toml` 檔案加入以下依賴：

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

接著，你便能在你的客戶端程式碼中引用所需函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接下來是實例化。

### -2- 實例化客戶端及傳輸

我們需要建立傳輸與客戶端的實例：

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

前面的程式碼中，我們：

- 建立了一個 stdio 傳輸實例。注意它指定了命令與參數，用於尋找與啟動伺服器，這是我們建立客戶端時必須做的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 透過給定名稱和版本來實例化客戶端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 將客戶端連接到所選的傳輸協定。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 為 stdio 連接建立伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 選用命令列參數
    env=None,  # 選用環境變數
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

前面的程式碼中，我們：

- 引入必要的函式庫
- 實例化一個伺服器參數物件，用來執行伺服器並能與客戶端連線
- 定義一個 `run` 方法，該方法呼叫 `stdio_client` 以啟動客戶端會話
- 建立一個入口點，使用 `asyncio.run` 執行 `run` 方法

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

前面的程式碼中，我們：

- 引入必要的函式庫。
- 建立了一個 stdio 傳輸和一個用於列出及呼叫 MCP 伺服器功能的客戶端 `mcpClient`。

注意，"Arguments" 可指定為 *.csproj* 或執行檔。

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
        
        // 你的客戶端邏輯寫喺呢度
    }
}
```

前面的程式碼中，我們：

- 建立了一個主方法，設定 SSE 傳輸，連接到 `http://localhost:8080`，此為 MCP 伺服器運行位置。
- 建立一個以傳輸為建構子參數的客戶端類別。
- 在 `run` 方法中，建立了一個同步 MCP 客戶端並初始化連線。
- 使用 SSE（Server-Sent Events）傳輸，適用於與 Java Spring Boot MCP 伺服器的 HTTP 通訊。

#### Rust

此 Rust 客戶端假設伺服器為同目錄下名為 "calculator-server" 的同級專案，以下程式碼會啟動伺服器並連接。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設伺服器係同一目錄下名為 "calculator-server" 嘅兄弟項目
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

    // 待辦事項：用參數 {"a": 3, "b": 2} 呼叫 add 工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

現在我們有了可連線的客戶端，但尚未實際列出伺服器功能，接著來做這件事：

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

在這裡，我們列出可用的資源 (`list_resources()`) 和工具 (`list_tools`)，並將結果印出。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上面是如何列出伺服器工具的範例。對每個工具，我們印出其名稱。

#### Java

```java
// 列出並演示工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 您亦可使用 ping 指令測試伺服器連線狀況
client.ping();
```

前面的程式碼中，我們：

- 呼叫 `listTools()` 以取得 MCP 伺服器上所有可用工具。
- 使用 `ping()` 確認與伺服器的連線正常。
- `ListToolsResult` 包含所有工具的相關資訊，包括名稱、描述和輸入結構。

很好，現在已擷取所有功能。接著的問題是什麼時候使用？這個客戶端很簡單，必須明確呼叫功能才會使用。下一章將建立擁有自主大型語言模型（LLM）的進階客戶端。先來看看如何呼叫伺服器功能：

#### Rust

在主函式中，初始化客戶端後，可初始化伺服器並列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 呼叫功能

呼叫功能時必須指定正確的參數，有時也需指定功能名稱。

#### TypeScript

```typescript

// 讀取資源
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

前面程式碼我們：

- 讀取資源，透過 `readResource()` 呼叫資源，指定 `uri`。伺服器端可能長這樣：

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

    我們的 `uri` 值為 `file://example.txt`，與伺服器端的 `file://{name}` 匹配，`example.txt` 會映射到 `name`。

- 呼叫工具，指定其 `name` 和 `arguments`，示例如下：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，呼叫 `getPrompt()`，指定 `name` 和 `arguments`。伺服器端程式碼如下：

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

    因此你的客戶端程式碼會像這樣，對應伺服器端宣告：

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

前面程式碼中，我們：

- 使用 `read_resource` 呼叫名為 `greeting` 的資源。
- 使用 `call_tool` 呼叫名為 `add` 的工具。

#### .NET

1. 新增呼叫工具的程式碼：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 印出結果的程式碼如下：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// 呼叫各種計算器工具
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

前面程式碼中，我們：

- 使用 `callTool()` 方法搭配 `CallToolRequest` 物件呼叫多個計算工具。
- 每個工具呼叫指定工具名稱及所需參數的 `Map`。
- 伺服器工具期待指定參數名稱（例如數學運算的 "a", "b"）。
- 結果以 `CallToolResult` 物件回傳，包含來自伺服器的響應。

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

在終端機輸入以下指令執行客戶端：

#### TypeScript

在 *package.json* 的 "scripts" 欄位新增以下指令：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

執行下述指令召喚客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

首先確定你的 MCP 伺服器運行於 `http://localhost:8080`，然後執行客戶端：

```bash
# 建構您的項目
./mvnw clean compile

# 執行用戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，你可以執行解決方案資料夾中完整的客戶端專案 `03-GettingStarted\02-client\solution\java`：

```bash
# 導航到解決方案目錄
cd 03-GettingStarted/02-client/solution/java

# 建構並執行JAR文件
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作業

透過這份作業，你將使用所學來建立自己的客戶端。

這有一個可供使用的伺服器，你需要透過客戶端呼叫它，試著為伺服器新增更多功能，使其更有趣。

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

// 開始在標準輸入接收訊息並在標準輸出發送訊息

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

請參考此專案，了解如何[新增提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另外，查看這個連結以了解如何呼叫[提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在[前一節](../../../../03-GettingStarted/01-first-server)中，你學會了使用 Rust 建立簡單的 MCP 伺服器。你可以繼續在那基礎上開發，或參考這個連結獲得更多基於 Rust 的 MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

**解答資料夾**包含完整可運行的客戶端實作範例，示範本教學涵蓋的所有概念。每個解答包含獨立且完整的客戶端與伺服器程式碼專案。

### 📁 解答結構

解答目錄依程式語言組織：

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

### 🚀 每個解答包含什麼

每種語言對應的解答提供：

- **完整客戶端實作**，涵蓋教學中所有功能
- **可用的專案結構**，含適當依賴與配置
- **編譯與執行腳本**，方便設定與執行
- **詳盡 README**，提供語言特定指引
- **錯誤處理與結果處理範例**

### 📖 如何使用解答

1. **切換至你偏好的語言資料夾**：

   ```bash
   cd solution/typescript/    # 用於 TypeScript
   cd solution/java/          # 用於 Java
   cd solution/python/        # 用於 Python
   cd solution/dotnet/        # 用於 .NET
   ```

2. **依照資料夾中 README 指示進行操作**：
   - 安裝依賴
   - 編譯專案
   - 執行客戶端

3. **你將看到的範例輸出**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完整文件與逐步指引詳見：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了本教學涵蓋所有程式語言的完整且可運行客戶端實作範例。這些範例展示了前述功能的完整實現，可供參考或作為你專案的起點。

### 可用的完整範例

| 語言     | 檔案                       | 說明                                               |
|----------|----------------------------|----------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)           | 使用 SSE 傳輸的完整 Java 客戶端，含完整錯誤處理         |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)           | 使用 stdio 傳輸、含自動啟動伺服器的完整 C# 客戶端           |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 完整 MCP 協議支援的 TypeScript 客戶端               |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)           | 使用 async/await 模式的完整 Python 客戶端               |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)               | 使用 Tokio 實現非同步操作的完整 Rust 客戶端                    |

每個完整範例包含：
- ✅ **連線建立** 及錯誤處理
- ✅ **伺服器探索**（工具、資源、提示，如適用）
- ✅ **計算機操作**（加、減、乘、除、說明）
- ✅ **結果處理** 及格式化輸出
- ✅ **全面錯誤處理**
- ✅ **乾淨、註解詳盡的程式碼**，附逐步說明

### 開始使用完整範例

1. **從上表選擇您偏好的語言**
2. **閱覽完整範例檔案** 以瞭解完整實作
3. **依照 [`complete_examples.md`](./complete_examples.md) 中說明執行範例**
4. **修改及延伸** 範例以符合您的特定使用需求

關於執行與自訂這些範例的詳細文件，請參閱：**[📖 完整範例文件](./complete_examples.md)**

### 💡 解決方案 與 完整範例

| **解決方案資料夾** | **完整範例** |
|--------------------|--------------------- |
| 完整專案結構暨建置檔案 | 單一檔案實作範例 |
| 含依賴，可直接運行 | 專注於程式碼範例 |
| 生產環境類似設定 | 教學參考用途 |
| 語言特定工具鏈 | 跨語言比較 |

兩者皆具價值——完整專案請用 **解決方案資料夾**，學習及參考請用 **完整範例**。

## 重要重點

本章節關於用戶端的重點如下：

- 可用於伺服器功能的探索與調用。
- 可在自身啟動時啟動伺服器（如本章所示），且用戶端亦可連接至已運行的伺服器。
- 是測試伺服器功能的絕佳方式，與前章所述的檢查器等替代方案並行評估。

## 額外資源

- [在 MCP 架構下建立用戶端](https://modelcontextprotocol.io/quickstart/client)

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 下一步

- 下一章： [使用 LLM 創建用戶端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。儘管我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引致的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
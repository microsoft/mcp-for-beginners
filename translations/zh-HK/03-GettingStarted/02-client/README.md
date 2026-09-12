# 建立客戶端

客戶端是自訂應用程式或腳本，可直接與 MCP 伺服器通訊以請求資源、工具及提示。與使用提供圖形介面以與伺服器互動的檢查工具不同，自行撰寫客戶端可進行程式化及自動化互動。這讓開發者能將 MCP 功能整合進自身工作流程，自動化工作並打造專為特定需求量身訂製的解決方案。

## 概覽

本課程介紹 Model Context Protocol (MCP) 生態系統中的客戶端概念。你將學習如何撰寫自己的客戶端，並讓它連接至 MCP 伺服器。

## 學習目標

完成本課程後，你將能夠：

- 理解客戶端能做什麼。
- 撰寫自己的客戶端。
- 連接並測試客戶端與 MCP 伺服器，確保伺服器運作如預期。

## 撰寫客戶端需要做什麼？

撰寫客戶端，你需要完成以下事項：

- <strong>匯入正確的函式庫</strong>。你將使用前面相同的函式庫，但架構會不同。
- <strong>實例化客戶端</strong>。這包含建立一個客戶端實例並連接到選定的傳輸方式。
- <strong>決定要列出哪些資源</strong>。你的 MCP 伺服器有資源、工具和提示，你必須決定列出哪些。
- <strong>將客戶端整合到主機應用程式中</strong>。當你了解伺服器能力後，需要將其整合進主機應用程式，讓使用者輸入提示或其他指令時，呼叫相對應的伺服器功能。

現在我們從高層次理解我們即將執行的操作，接下來看看一個範例。

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

在前述程式碼中，我們：

- 匯入函式庫
- 建立一個客戶端實例並使用 stdio 作為傳輸連線。
- 列出提示、資源與工具，並觸發它們。

就這樣，一個可以與 MCP 伺服器對話的客戶端誕生了。

接下來的練習部分，我們會逐步解析每段程式碼並解釋其內容，請耐心跟進。

## 練習：撰寫客戶端

如上所述，讓我們花些時間解釋程式碼，如果你願意，也可以邊做邊寫。

### -1- 匯入函式庫

先匯入所需函式庫，我們需要參考客戶端與選用的傳輸協定 stdio。stdio 是設計給執行於本地端機器的協定。SSE 是另一種傳輸協定，我們將在未來章節展示，但目前先用 stdio。

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

對於 Java，你將建立一個客戶端來連接前一練習中的 MCP 伺服器。以 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 的 Java Spring Boot 專案結構為例，在 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾中建立一個新類別 `SDKClient`，並加入以下匯入：

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

需要在 `Cargo.toml` 裡加入以下相依套件。

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

接著在客戶端程式中匯入必要函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接著進入實例化階段。

### -2- 實例化客戶端與傳輸

我們要建立傳輸和客戶端實例：

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

在前述程式碼中，我們：

- 建立 stdio 傳輸實例。注意它如何指定 command 和 args 來尋找並啟動伺服器，這是在建立客戶端時需要做的設定。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 以名稱和版本號來實例化客戶端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 將客戶端連接到所選傳輸。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 建立 stdio 連接的服務器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 可選的命令行參數
    env=None,  # 可選的環境變數
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

在前述程式碼中，我們：

- 匯入所需函式庫
- 實例化 server parameters 物件，我們會用它來啟動伺服器以便客戶端能連接。
- 定義 `run` 方法，內部呼叫 `stdio_client` 啟動客戶端會話。
- 建立入口點，將 `run` 方法提供給 `asyncio.run`。

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

在前述程式碼中，我們：

- 匯入需要的函式庫。
- 建立 stdio 傳輸並建立名為 `mcpClient` 的客戶端。 此客戶端會用於列出及呼叫 MCP 伺服器上的功能。

注意，"Arguments" 部分你可以指定 *.csproj* 檔案或執行檔。

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
        
        // 你的客戶端邏輯寫在這裡
    }
}
```

在前述程式碼中，我們：

- 建立 main 方法，設定 SSE 傳輸連接到 `http://localhost:8080`，該處執行 MCP 伺服器。
- 建立一個接收傳輸作為建構子參數的客戶端類別。
- 在 `run` 方法中，使用該傳輸建立同步 MCP 客戶端並初始化連線。
- 使用 SSE (Server-Sent Events) 傳輸，適合與 Java Spring Boot MCP 伺服器基於 HTTP 通訊。

#### Rust

請注意此 Rust 客戶端假設伺服器為同目錄下名為 "calculator-server" 的兄弟專案。以下程式碼會啟動伺服器並連接它。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設伺服器是一個名為 "calculator-server" 的兄弟項目，位於同一目錄中
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

    // 待辦: 初始化

    // 待辦: 列出工具

    // 待辦: 使用參數 = {"a": 3, "b": 2} 呼叫加法工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

至此，我們已有可連接的客戶端（若執行此程式）。不過，它尚未列出伺服器功能，接下來來完成這部分：

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

這裡我們列出可用資源（`list_resources()`）及工具（`list_tools`），並將它們列印出來。

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
// 列出並示範工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 你亦可以 ping 伺服器以驗證連線
client.ping();
```

在前述程式碼中，我們：

- 呼叫 `listTools()` 取得 MCP 伺服器上的所有可用工具。
- 使用 `ping()` 確認到伺服器的連線正常。
- `ListToolsResult` 包含所有工具資訊，包括名稱、描述和輸入結構。

太好了，現已蒐集所有功能。那麼我們何時使用它們呢？這個客戶端相當簡單，必須在想用功能時明確呼叫。在下一章，我們會建立更進階的客戶端，內建自己的大型語言模型 (LLM)。目前讓我們看看如何呼叫伺服器上的功能：

#### Rust

在 main 函式中，初始化客戶端後，可以啟動伺服器並列出部份功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 呼叫功能

要呼叫功能，我們需要確定指定正確的參數，並在某些情況下指定要呼叫的名稱。

#### TypeScript

```typescript

// 讀取一個資源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 調用一個工具
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

在前述程式碼中，我們：

- 讀取資源，透過呼叫 `readResource()` 並指定 `uri`。伺服器端大概是這樣：

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

    我們的 `uri` 值 `file://example.txt` 和伺服器端的 `file://{name}` 配對，`example.txt` 對映至 `name`。

- 呼叫工具，透過指定工具的 `name` 及其 `arguments` 如下：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，呼叫 `getPrompt()` 並帶入 `name` 和 `arguments`。伺服器端程式碼如下：

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

    因此你的客戶端程式碼會長這樣以呼應伺服器端的宣告：

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

在前述程式碼中，我們：

- 使用 `read_resource` 呼叫名為 `greeting` 的資源。
- 使用 `call_tool` 呼叫名為 `add` 的工具。

#### .NET

1. 加入呼叫工具的程式碼：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 列印結果的程式碼如下：

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

在前述程式碼中，我們：

- 使用 `callTool()` 方法與 `CallToolRequest` 物件呼叫多個計算工具。
- 每次呼叫指定工具名稱和該工具所需的參數 Map。
- 伺服器工具預期特定參數名稱（例如數學運算的 "a", "b"）。
- 結果以 `CallToolResult` 物件回傳，包含伺服器回應。

#### Rust

```rust
// 呼叫加法工具，參數為 {"a": 3, "b": 2}
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

在終端機輸入以下指令以執行客戶端：

#### TypeScript

在 *package.json* 的 "scripts" 區塊中加入以下內容：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

執行以下指令呼叫客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

確認 MCP 伺服器在 `http://localhost:8080` 運作中，接著執行客戶端：

```bash
# 構建您的項目
./mvnw clean compile

# 運行客戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，你也可以執行提供於解決方案資料夾 `03-GettingStarted\02-client\solution\java` 的完整客戶端專案：

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

本次作業中，你將使用所學來建立自己的客戶端。

這裡有個伺服器你可以用來呼叫，試著為它新增更多功能，讓伺服器更有趣。

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

// 開始接收 stdin 的訊息並透過 stdout 發送訊息

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

請參考此專案了解如何 [新增提示與資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

同時，參考此連結以了解如何呼叫 [提示與資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在 [前面章節](../../../../03-GettingStarted/01-first-server)，你學會如何用 Rust 建立簡易 MCP 伺服器。你可以在此基礎繼續開發，或者參考此連結查看更多基於 Rust 的 MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

<strong>解答資料夾</strong>包含完整、可直接執行的客戶端實作，展示本教學所涵蓋的各項概念。每套解答均包含客戶端及伺服器程式碼，分別整理成獨立自包含的專案。

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

### 🚀 每套解答包含內容

每個語言專用解答都提供：

- <strong>完整客戶端實作</strong>，涵蓋教學所有功能
- <strong>可運作的專案結構</strong>，含完整相依與設定
- <strong>建置與執行腳本</strong>，方便快速啟動
- **詳盡 README**，含語言專屬指示
- <strong>錯誤處理</strong>和結果處理範例

### 📖 使用解答

1. <strong>前往你偏好的語言資料夾</strong>：

   ```bash
   cd solution/typescript/    # 適用於 TypeScript
   cd solution/java/          # 適用於 Java
   cd solution/python/        # 適用於 Python
   cd solution/dotnet/        # 適用於 .NET
   ```

2. **依該資料夾 README 指示操作**：
   - 安裝相依套件
   - 建置專案
   - 執行客戶端

3. <strong>你應該會看到的範例輸出</strong>：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完整文件及步驟說明請參閱：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了完整可執行的客戶端範例，涵蓋本教學所有程式語言。這些範例展現上述功能，能作為參考實作或個人專案起點。

### 可用完整範例

| 語言 | 檔案 | 說明 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 傳輸的完整 Java 客戶端，含完整錯誤處理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 傳輸並自動啟動伺服器的完整 C# 客戶端 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 支援完整 MCP 協議的 TypeScript 客戶端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用 async/await 的 Python 客戶端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 非同步操作的 Rust 客戶端 |

每個完整範例包含：

- ✅ <strong>連線建立</strong>與錯誤處理
- ✅ <strong>伺服器探索</strong>（工具、資源、提示，視情況而定）
- ✅ <strong>計算工具操作</strong>（加、減、乘、除、說明）
- ✅ <strong>結果處理</strong>與格式化輸出
- ✅ <strong>完善的錯誤處理</strong>

- ✅ <strong>清晰且有說明的代碼</strong>，附有逐步註解

### 透過完整範例開始

1. <strong>從上方表格中選擇您的偏好語言</strong>
2. <strong>檢視完整範例檔案</strong>以了解完整實作
3. **依照[`complete_examples.md`](./complete_examples.md)中的指示執行範例**
4. <strong>修改並擴展</strong>範例以符合您的特定使用需求

有關執行和自訂這些範例的詳細文件，請參考：**[📖 完整範例文件](./complete_examples.md)**

### 💡 解決方案與完整範例

| <strong>解決方案資料夾</strong> | <strong>完整範例</strong> |
|--------------------|--------------------- |
| 包含建置檔案的完整專案架構 | 單一檔案實作 |
| 可立即執行並含依賴 | 專注的程式碼範例 |
| 近似生產環境的設定 | 教學參考 |
| 語言特定工具鏈 | 跨語言比較 |

這兩者方式皆有價值 —— 使用<strong>解決方案資料夾</strong>來取得完整專案，使用<strong>完整範例</strong>做學習及參考。

## 重要重點

本章關於客戶端的重點總結如下：

- 可用於同時發現與調用伺服器上的功能。
- 在自身啟動時也能啟動伺服器（如本章所示），且客戶端亦能連接至正在運行的伺服器。
- 是測試伺服器功能的絕佳方式，與之前章節所述的 Inspector 等替代方案並行使用。

## 額外資源

- [在 MCP 中建置客戶端](https://modelcontextprotocol.io/quickstart/client)

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.NET 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 接下來是

- 下一步：[使用 LLM 建立客戶端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
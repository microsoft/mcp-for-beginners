# 建立客戶端

客戶端是用來與 MCP 伺服器直接通訊，請求資源、工具及提示的自訂應用程式或腳本。與使用提供圖形介面用於操作伺服器的檢查工具不同，撰寫自己的客戶端可以進行程式化和自動化的互動。這使開發者能將 MCP 功能整合到自有工作流程中，自動化任務，並打造符合特定需求的自訂解決方案。

## 概覽

本課程介紹 Model Context Protocol (MCP) 生態系統中「客戶端」的概念。您將學習如何撰寫自己的客戶端並與 MCP 伺服器建立連線。

## 學習目標

透過本課程結束時，您將能夠：

- 了解客戶端的功能。
- 撰寫您自己的客戶端。
- 連線並測試客戶端與 MCP 伺服器確保其正常運作。

## 撰寫客戶端需要做什麼？

撰寫客戶端，您需要完成以下事項：

- <strong>匯入正確的函式庫</strong>。您將使用之前相同的函式庫，但組件將不同。
- <strong>實例化客戶端</strong>。這會包含建立客戶端的實例並連接到所選的傳輸方法。
- <strong>決定要列出哪些資源</strong>。您的 MCP 伺服器附帶資源、工具和提示，您需要決定要列出哪些。
- <strong>將客戶端整合至主機應用程式</strong>。了解伺服器功能後，您需要將客戶端整合進主機應用程式，讓使用者輸入提示或指令時，能呼叫相應的伺服器功能。

了解整體流程後，我們接下來看個範例。

### 範例客戶端

讓我們看看此範例客戶端：

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

在以上程式碼中我們：

- 匯入函式庫
- 建立客戶端實例並使用 stdio 傳輸連線
- 列出所有提示、資源和工具並呼叫它們

就這樣，建立了一個能與 MCP 伺服器溝通的客戶端。

在下一個練習環節，我們將細分每個程式碼片段進行深入說明。

## 練習：撰寫一個客戶端

如前所述，讓我們慢慢說明程式碼，也歡迎跟著練習撰寫。

### -1- 匯入函式庫

匯入所需函式庫，我們會引用客戶端和所選傳輸協定 stdio。stdio 是本地機器運行時使用的協定，未來章節將展示 SSE 作為另一傳輸選項，目前先繼續使用 stdio。

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

Java 範例將建立一個能連接到先前練習 MCP 伺服器的客戶端。以 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 的 Java Spring Boot 專案結構為基礎，在 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾創建新 Java 類別 `SDKClient`，並加入以下匯入：

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

需將以下相依加入 `Cargo.toml` 檔案中。

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

接著您就可以在客戶端程式碼中匯入必要函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接下來繼續實例化部份。

### -2- 實例化客戶端與傳輸

我們需要建立傳輸和客戶端的實例：

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

前述程式碼中我們：

- 建立 stdio 傳輸實例。注意指定了啟動伺服器的指令與引數，這是建立客戶端時必須考慮的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 實例化一個命名並帶版本號的客戶端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 把客戶端連接至所選的傳輸。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 建立用於 stdio 連線的伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 選用的命令列參數
    env=None,  # 選用的環境變數
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

前述程式碼中我們：

- 匯入所需函式庫
- 實例化伺服器參數物件，後續啟動伺服器並以客戶端連接它時會用到
- 定義 `run` 方法，該方法會呼叫 `stdio_client` 啟動客戶端會話
- 創建進入點並以 `asyncio.run` 呼叫 `run`

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

前述程式碼中我們：

- 匯入所需函式庫。
- 建立 stdio 傳輸，並創建客戶端物件 `mcpClient`，此客戶端用於列出及呼叫 MCP 伺服器功能。

注意在 "Arguments" 中，您可以指向 *.csproj* 或可執行檔。

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

前述程式碼中我們：

- 建立 main 方法，設定 SSE 傳輸指向執行於 `http://localhost:8080` 的 MCP 伺服器。
- 創建一個客戶端類別，建構子參數為傳輸物件。
- 在 `run` 方法中，使用傳輸建立同步 MCP 客戶端並初始化連線。
- 使用適合 Java Spring Boot MCP 伺服器的 SSE（伺服器發送事件）傳輸。

#### Rust

注意此 Rust 客戶端假設伺服器是同一個目錄下名為 "calculator-server" 的兄弟專案。下方程式碼會啟動伺服器並連線。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設伺服器是同一目錄下名為 "calculator-server" 的兄弟專案
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

    // 待辦事項：以參數 = {"a": 3, "b": 2} 呼叫新增工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

現在，我們已有能連接的客戶端程式。但它尚未列出伺服器的功能，接下來就做這件事：

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

這裡呼叫 `list_resources()` 列出資源和 `list_tools` 列出工具，並將它們列印出來。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

以上示例展現如何列出伺服器上的工具。對每個工具，我們列印它的名稱。

#### Java

```java
// 列出並示範工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 你也可以對伺服器進行 ping 以驗證連線
client.ping();
```

前述程式碼中我們：

- 呼叫 `listTools()` 從 MCP 伺服器獲取全部可用工具。
- 使用 `ping()` 驗證與伺服器的連線正常。
- `ListToolsResult` 包含所有工具的名稱、描述及輸入模式資訊。

太好了，現在我們獲取了所有功能。那麼何時使用它們呢？此客戶端設計簡單，意味著需要明確呼叫想要的功能。下一章將建立較進階的客戶端，配備自己的大型語言模型 LLM。目前，我們來看看如何呼叫伺服器功能：

#### Rust

在 main 函數中，初始化客戶端後，我們可以初始化伺服器並列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 呼叫功能

呼叫功能時需確保傳入正確引數，有時還要指定功能名稱。

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

在前述程式碼中我們：

- 讀取資源，透過 `readResource()` 並指定 `uri`。伺服器端程式碼看起來可能是這樣：

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

    我們的 `uri` 值 `file://example.txt` 對應伺服器上的 `file://{name}`，即 `example.txt` 映射給 `name`。

- 呼叫工具，透過指定工具 `name` 和 `arguments` 實現：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，通過呼叫 `getPrompt()` 並傳入 `name` 和 `arguments`。伺服器程式碼如下：

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

    因此客戶端程式碼呼叫方式會與伺服器宣告對應：

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

- 以 `read_resource` 呼叫名為 `greeting` 的資源。
- 以 `call_tool` 呼叫名為 `add` 的工具。

#### .NET

1. 先加入呼叫工具的程式碼：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 以下程式碼用於顯示呼叫結果：

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

前述程式碼中，我們：

- 使用 `callTool()` 方法搭配 `CallToolRequest` 物件呼叫多個計算器工具。
- 每次呼叫指定工具名稱及該工具所需的引數 `Map`。
- 伺服器工具期待特定參數名稱（如數學運算的 "a"、"b"）。
- 回傳結果為包含伺服器回應的 `CallToolResult` 物件。

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

在終端機輸入以下指令啟動客戶端：

#### TypeScript

在 *package.json* 的 "scripts" 區塊新增以下條目：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

輸入以下指令呼叫客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

確保 MCP 伺服器已在 `http://localhost:8080` 運行，然後執行客戶端：

```bash
# 建置您的專案
./mvnw clean compile

# 執行客戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，您也可執行位於解決方案資料夾 `03-GettingStarted\02-client\solution\java` 中的完整客戶端專案：

```bash
# 導航到解決方案目錄
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

此作業中，您將運用課程所學撰寫自己的客戶端。

下面提供一個伺服器範例，您必須透過客戶端呼叫，試著增加更多功能使伺服器更有趣。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 建立一個MCP伺服器
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

// 新增一個動態問候語資源
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

// 開始在標準輸入接收訊息並在標準輸出傳送訊息

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

請參考此專案查看如何[新增提示與資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另外，查看此連結了解如何呼叫[提示與資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在[上一節](../../../../03-GettingStarted/01-first-server)您已學會如何用 Rust 建立簡單 MCP 伺服器。您可以繼續擴展它，或參考此連結查看更多基於 Rust 的 MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

<strong>解答資料夾</strong>包含完善且可直接執行的客戶端範例，展示本教程涵蓋的所有概念。每套解答專案皆包含獨立的客戶端與伺服器程式碼，組織完善自包含。

### 📁 解答結構

解答目錄依程式語言區分：

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

每個語言專屬解答提供：

- <strong>完整客戶端實作</strong>，涵蓋教程中所有功能
- <strong>可運行專案結構</strong>，附正確相依與設定
- <strong>建置與執行腳本</strong>，簡化設置及執行程序
- **詳細 README**，說明各語言專屬操作指引
- <strong>錯誤處理與結果示範</strong>

### 📖 使用解答

1. <strong>切換到想用的語言資料夾</strong>：

   ```bash
   cd solution/typescript/    # 適用於 TypeScript
   cd solution/java/          # 適用於 Java
   cd solution/python/        # 適用於 Python
   cd solution/dotnet/        # 適用於 .NET
   ```

2. **依照各資料夾 README 指示**：
   - 安裝相依套件
   - 建置專案
   - 執行客戶端

3. <strong>您應該能在輸出看到如下結果</strong>：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

更完整文件與逐步說明，請見：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了涵蓋本教程所有程式語言的完整且可運作的客戶端實作。這些範例展示了上面說明的功能，可做為參考範本或自行開發的起點。

### 可用的完整範例

| 語言 | 檔案 | 說明 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 傳輸的完整 Java 客戶端，含完整錯誤處理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 傳輸並自動啟動伺服器的完整 C# 客戶端 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 支援完整 MCP 協議的 TypeScript 客戶端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 採用 async/await 模式的完整 Python 客戶端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 執行非同步操作的完整 Rust 客戶端 |

每個完整範例包含：

- ✅ <strong>連線建立</strong>與錯誤處理
- ✅ <strong>伺服器發現</strong>（工具、資源、提示）
- ✅ <strong>計算器操作</strong>（加、減、乘、除、幫助）
- ✅ <strong>結果處理</strong>與格式化輸出
- ✅ <strong>全面的錯誤處理</strong>

- ✅ <strong>乾淨且有註解的程式碼</strong>，附有逐步說明

### 入門完整範例

1. <strong>從上方表格中選擇您偏好的語言</strong>
2. <strong>查看完整範例檔案</strong>，以理解完整實作
3. **依照 [`complete_examples.md`](./complete_examples.md) 中的指示執行範例**
4. <strong>修改並擴充</strong> 範例以符合您的特定需求

有關執行與自訂這些範例的詳細文件，請見：**[📖 完整範例文件](./complete_examples.md)**

### 💡 Solution 與 Complete Examples 的比較

| **Solution 資料夾** | **Complete Examples** |
|--------------------|--------------------- |
| 完整專案結構與建置檔案 | 單檔實作範例 |
| 可執行且有相依性 | 專注於程式碼範例 |
| 類生產環境設定 | 教學參考 |
| 語言特定工具支援 | 跨語言比較 |

兩者均有其價值 —— 使用 **solution 資料夾** 進行完整專案開發，使用 **complete examples** 作為學習與參考。

## 重點摘要

本章關於客戶端的重點如下：

- 既可用於發現，也可用於調用伺服器上的功能。
- 可以在自己啟動時同時啟動伺服器（像本章所示），但也能連線到已運行的伺服器。
- 是測試伺服器能力的絕佳工具，與上章說明的 Inspector 等替代方案並列。

## 額外資源

- [在 MCP 中建立客戶端](https://modelcontextprotocol.io/quickstart/client)

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
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# 創建客戶端

客戶端是自訂應用程序或腳本，直接與 MCP 伺服器通訊以請求資源、工具和提示。與使用提供圖形介面與伺服器互動的檢查工具不同，撰寫自己的客戶端可進行程式化和自動化互動。這使開發人員能將 MCP 功能整合到自己的工作流程中，自動化任務，並構建針對特定需求定制的解決方案。

## 概述

本課程介紹 Model Context Protocol (MCP) 生態系中的客戶端概念。您將學習如何撰寫自己的客戶端並讓它連接到 MCP 伺服器。

## 學習目標

完成本課程後，您將能夠：

- 了解客戶端的功能。
- 撰寫自己的客戶端。
- 與 MCP 伺服器連接並測試，確保伺服器如預期運作。

## 撰寫客戶端需要哪些元素？

撰寫客戶端時，您需要：

- **匯入正確的函式庫**。您將使用與之前相同的函式庫，只是使用不同的結構。
- **實例化客戶端**。這包括建立客戶端實例並將其連接到選擇的通訊方式。
- **決定要列出的資源**。您的 MCP 伺服器有資源、工具和提示，您需要決定列出哪一個。
- **將客戶端整合到主機應用程式**。了解伺服器的能力後，您需要將它整合到主機應用程式中，當使用者輸入提示或其他命令時即會調用對應的伺服器功能。

既然我們已大致了解即將執行的內容，接下來看一個範例。

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

// 列出提示詞
const prompts = await client.listPrompts();

// 取得一個提示詞
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// 列出資源
const resources = await client.listResources();

// 讀取一個資源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 呼叫一個工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

在上面程式碼中，我們：

- 匯入函式庫
- 建立客戶端實例並使用 stdio 作為傳輸方式連接
- 列出提示、資源和工具並呼叫它們

這就是可以與 MCP 伺服器通訊的客戶端。

接下來的練習部分，我們將逐段程式碼詳細說明。

## 練習：撰寫客戶端

如上所述，讓我們花時間解說程式碼，若想依照操作也盡量跟著寫。

### -1- 匯入函式庫

匯入我們需要的函式庫，需引用客戶端與選擇的傳輸協議 stdio。stdio 是設計來在您的本機運行的協議。SSE 是未來章節會展示的另一種傳輸協議，您也可以選擇它。現在先繼續用 stdio。

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

對於 Java，您將創建一個能連接先前練習 MCP 伺服器的客戶端。使用 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 的相同 Java Spring Boot 專案結構，在 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾新增名為 `SDKClient` 的 Java 類別，並加入以下匯入：

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

您需要將以下依賴項新增到您的 `Cargo.toml` 文件中。

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

然後，在客戶端程式碼中匯入必要函式庫。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接著進行實例化。

### -2- 實例化客戶端與傳輸

我們需要建立傳輸實例及客戶端實例：

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

在上述程式碼中，我們：

- 建立 stdio 傳輸實例。注意如何指定啟動伺服器的指令和參數，這是我們創建客戶端時需要做的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 透過給予名稱與版本實例化客戶端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 將客戶端連接至選擇的傳輸。

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
    args=["run", "server.py"],  # 選擇性的命令列參數
    env=None,  # 選擇性的環境變數
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

在上述程式碼中，我們：

- 匯入所需函式庫
- 實例化伺服器參數物件，用於執行伺服器，方便客戶端連接
- 定義 `run` 方法，該方法調用 `stdio_client` 啟動客戶端會話
- 建立入口點，透過 `asyncio.run` 執行 `run` 方法

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

在上述程式碼中，我們：

- 匯入所需函式庫。
- 建立 stdio 傳輸並創建名為 `mcpClient` 的客戶端。後者用於列出並調用 MCP 伺服器上的功能。

註：在 "Arguments" 部分，您可以指向 *.csproj* 或可執行檔。

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

在上述程式碼中，我們：

- 建立一個 main 方法，設置 SSE 傳輸指向 MCP 伺服器正在運行的 `http://localhost:8080`
- 創建一個客戶端類別，以傳輸作為建構子參數
- 在 `run` 方法中，使用該傳輸建立同步 MCP 客戶端並初始化連線
- 使用 SSE（Server-Sent Events）傳輸，適合使用 Java Spring Boot MCP 伺服器的 HTTP 通訊

#### Rust

注意此 Rust 客戶端假設伺服器是命名為 "calculator-server" 的兄弟專案，位於同一資料夾中。以下程式碼將啟動該伺服器並連接。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假設伺服器是一個名為 "calculator-server" 的同級專案，位於相同目錄中
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

    // 待辦事項：使用參數 {"a": 3, "b": 2} 呼叫加法工具

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

現在，我們的客戶端在程式執行時可以連接伺服器，但尚未列出功能，接下來來完成它：

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
# 列出可用的資源
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 列出可用的工具
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

此處列出可用的資源 `list_resources()` 和工具 `list_tools`，並將其輸出。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

以上是如何列出伺服器工具的範例。針對每個工具，顯示其名稱。

#### Java

```java
// 列出並示範工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 你也可以使用 ping 伺服器來驗證連線
client.ping();
```

在上述程式碼中，我們：

- 呼叫 `listTools()` 取得 MCP 伺服器提供的所有工具
- 使用 `ping()` 確認連線正常
- `ListToolsResult` 包含所有工具的資訊，如名稱、描述和輸入架構

很好，現已擷取所有功能。接著要問，何時使用呢？此客戶端很簡單，必須我們明確呼叫功能。下一章我們將建立能存取自身大型語言模型（LLM）的進階客戶端。但現階段，先看如何調用伺服器上的功能：

#### Rust

在 main 函式中，初始化客戶端後，可初始化伺服器並列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 調用功能

呼叫功能時，要確保指定正確的參數，有時還包括欲呼叫的名稱。

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

在上述程式碼中，我們：

- 讀取資源，呼叫 `readResource()` 並指定 `uri`。伺服器端大致如下：

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

    我們的 `uri` 值是 `file://example.txt`，對應伺服器的 `file://{name}`，`example.txt` 將映射給 `name`。

- 呼叫工具，指定 `name` 和 `arguments` 如下：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 取得提示，呼叫 `getPrompt()` 並使用 `name` 和 `arguments`。伺服器程式碼如下：

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

    因此，您的客戶端程式碼如下，以符合伺服器端的宣告：

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

在上述程式碼中，我們：

- 使用 `read_resource` 呼叫名為 `greeting` 的資源
- 使用 `call_tool` 呼叫名為 `add` 的工具

#### .NET

1. 新增呼叫工具的程式碼：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 打印結果的程式碼示例如下：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// 調用各種計算工具
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

在上述程式碼中，我們：

- 使用 `callTool()` 並傳入 `CallToolRequest` 物件呼叫多個計算器工具
- 每個工具呼叫指定工具名稱和所需的參數 `Map`
- 伺服器工具期待特定參數名稱（例如「a」、「b」用於數學運算）
- 結果以 `CallToolResult` 物件形式返回，包含伺服器的回應

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

在終端機輸入以下指令以執行客戶端：

#### TypeScript

在 *package.json* 的 "scripts" 區段加入以下內容：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

使用以下指令執行客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

首先確保 MCP 伺服器在 `http://localhost:8080` 執行，再執行客戶端：

```bash
# 建置你的專案
./mvnw clean compile

# 執行客戶端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或您也可以執行解決方案資料夾中的完整客戶端專案 `03-GettingStarted\02-client\solution\java`：

```bash
# 導航到解決方案目錄
cd 03-GettingStarted/02-client/solution/java

# 編譯並執行JAR檔案
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作業

這次作業將使用所學來建立自己的客戶端。

這裡有個您可以使用的伺服器，需用客戶端程式碼呼叫，看看是否能為伺服器新增更多功能使其更有趣。

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

// 新增動態問候資源
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

請參考此專案了解如何[新增提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另請查看此連結了解如何調用[提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在[前一個章節](../../../../03-GettingStarted/01-first-server)，您學到如何使用 Rust 建立簡易 MCP 伺服器。您可以繼續基於該專案開發，或參考以下連結取得更多 Rust MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

**解答資料夾**包含完整且可直接執行的客戶端實作，示範本教學涵蓋的所有概念。每組解答包含獨立分隔的客戶端與伺服器專案。

### 📁 解答結構

此解答目錄依程式語言分類：

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

### 🚀 每個解答包含的內容

各語言解答包含：

- **完整的客戶端實作**，涵蓋教學全部功能
- **完善的專案結構**，包含正確依賴與設定
- **建置與執行腳本**，方便設定和執行
- **詳細 README**，內含語言特定指導
- **錯誤處理**與結果處理範例

### 📖 使用解答

1. **進入您偏好的語言資料夾**：

   ```bash
   cd solution/typescript/    # 適用於 TypeScript
   cd solution/java/          # 適用於 Java
   cd solution/python/        # 適用於 Python
   cd solution/dotnet/        # 適用於 .NET
   ```

2. **依每個資料夾的 README 指示操作**，包含：
   - 安裝依賴
   - 建置專案
   - 執行客戶端

3. **您將看到的範例輸出**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完整文件與逐步指導，請參閱：**[📖 解答文件](./solution/README.md)**

## 🎯 完整範例

我們提供了本教學所涵蓋所有程式語言的完整且可運行客戶端實作。這些範例展示上面描述的全部功能，您可將其作為參考實作或自己專案的起點。

### 可用的完整範例

| 語言   | 檔案                         | 說明                                        |
|--------|------------------------------|---------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)     | 使用 SSE 傳輸的完整 Java 客戶端，內含完善錯誤處理           |
| **C#**    | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)      | 使用 stdio 傳輸的完整 C# 客戶端，支援自動啟動伺服器           |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 完整的 TypeScript 客戶端，支援全 MCP 協議功能                |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)      | 使用 async/await 模式的完整 Python 客戶端                      |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)          | 使用 Tokio 進行非同步作業的完整 Rust 客戶端                    |

每個完整範例皆包含：
- ✅ **連線建立** 與錯誤處理  
- ✅ **伺服器偵測**（工具、資源、必要時的提示）  
- ✅ **計算機運算**（加、減、乘、除、說明）  
- ✅ **結果處理** 與格式化輸出  
- ✅ **完整錯誤處理**  
- ✅ **乾淨、有註解的程式碼**，逐步說明  

### 使用完整範例快速入門

1. **從上表選擇你偏好的語言**  
2. **查看完整範例檔案**，了解完整實作  
3. **依照 [`complete_examples.md`](./complete_examples.md) 指示執行範例**  
4. **修改並擴充範例**，符合你的特定需求  

關於執行與自訂這些範例的詳細文件，請參閱：**[📖 完整範例文件](./complete_examples.md)**  

### 💡 解決方案與完整範例比較

| **解決方案資料夾** | **完整範例**              |
|--------------------|--------------------------|
| 含建置檔案的完整專案結構 | 單一檔案實作範例           |
| 支援相依性即可執行       | 針對功能的程式碼範例        |
| 近似正式生產環境        | 教育性參考                |
| 語言特定工具鏈          | 跨語言比較                |

兩者皆有價值 —— 使用 **解決方案資料夾** 建立完整專案，使用 **完整範例** 做學習與參考。  

## 重要重點

本章重點關於客戶端如下：

- 可用來偵測與呼叫伺服器功能。  
- 可在啟動自己時同時啟動伺服器（如本章示範），也可以連接已執行的伺服器。  
- 是測試伺服器功能的良好工具，與上一章提及的 Inspector 兩者可互補。  

## 附加資源

- [在 MCP 中建立客戶端](https://modelcontextprotocol.io/quickstart/client)  

## 範例

- [Java 計算機](../samples/java/calculator/README.md)  
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript 計算機](../samples/javascript/README.md)  
- [TypeScript 計算機](../samples/typescript/README.md)  
- [Python 計算機](../../../../03-GettingStarted/samples/python)  
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)  

## 下一步

- 下一步：[使用 LLM 建立客戶端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# 建立客戶端

客戶端是自訂的應用程式或腳本，直接與 MCP 伺服器溝通以請求資源、工具和提示。與使用檢查工具提供的圖形介面不同，撰寫自己的客戶端可以進行程式化和自動化的互動。這使得開發者能將 MCP 的功能整合到自己的工作流程中，自動化任務，並根據特定需求建立量身定制的解決方案。

## 概述

本課程介紹了 Model Context Protocol (MCP) 生態系統中的客戶端概念。您將學習如何撰寫自己的客戶端並將其連接到 MCP 伺服器。

## 學習目標

完成本課程後，您將能夠：

- 理解客戶端的功能。
- 撰寫自己的客戶端。
- 連接並測試客戶端與 MCP 伺服器，確保伺服器正常運作。

## 撰寫客戶端需要做什麼？

撰寫客戶端需要完成以下步驟：

- **匯入正確的函式庫**。您將使用之前相同的函式庫，但使用不同的結構。
- **實例化客戶端**。這包括建立客戶端實例並將其連接到選定的傳輸方法。
- **決定要列出哪些資源**。您的 MCP 伺服器提供資源、工具和提示，您需要決定列出哪一項。
- **將客戶端整合到主應用程式**。一旦了解伺服器的功能，您需要將其整合到主應用程式中，以便使用者輸入提示或其他指令時，能調用相應的伺服器功能。

現在我們已經了解了高層次的概念，接下來讓我們看一個範例。

### 客戶端範例

讓我們看看以下客戶端範例：

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

在上述程式碼中，我們：

- 匯入函式庫。
- 建立客戶端實例並使用 stdio 作為傳輸方式進行連接。
- 列出提示、資源和工具並全部調用。

這樣就完成了一個可以與 MCP 伺服器溝通的客戶端。

接下來的練習部分，我們將逐段解析程式碼並解釋其運作方式。

## 練習：撰寫客戶端

如上所述，我們將逐步解釋程式碼，並且如果您願意，可以跟著一起編寫。

### -1- 匯入函式庫

讓我們匯入所需的函式庫，我們需要引用客戶端和選定的傳輸協議 stdio。stdio 是一種適用於本地機器運行的協議。SSE 是另一種傳輸協議，我們會在未來章節中展示，但目前我們先使用 stdio。

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

對於 Java，您將建立一個客戶端，從之前的練習中連接到 MCP 伺服器。使用 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 中的 Java Spring Boot 專案結構，在 `src/main/java/com/microsoft/mcp/sample/client/` 資料夾中建立一個名為 `SDKClient` 的 Java 類別，並添加以下匯入：

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

您需要在 `Cargo.toml` 文件中添加以下依賴項。

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

然後，您可以在客戶端程式碼中匯入必要的函式庫。

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

### -2- 實例化客戶端和傳輸

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

在上述程式碼中，我們：

- 建立了一個 stdio 傳輸實例。注意它如何指定命令和參數以找到並啟動伺服器，這是我們在建立客戶端時需要做的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 實例化了一個客戶端，並為其指定名稱和版本。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 將客戶端連接到選定的傳輸方式。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

在上述程式碼中，我們：

- 匯入所需的函式庫。
- 實例化伺服器參數物件，因為我們將使用它來啟動伺服器，以便能用客戶端連接。
- 定義了一個 `run` 方法，該方法進一步調用 `stdio_client` 以啟動客戶端會話。
- 建立了一個入口點，提供 `run` 方法給 `asyncio.run`。

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

在上述程式碼中，我們：

- 匯入所需的函式庫。
- 建立了一個 stdio 傳輸並建立了一個客戶端 `mcpClient`。後者將用於列出和調用 MCP 伺服器上的功能。

注意，在 "Arguments" 中，您可以指向 *.csproj* 或可執行文件。

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
        
        // Your client logic goes here
    }
}
```

在上述程式碼中，我們：

- 建立了一個主方法，設置 SSE 傳輸，指向 MCP 伺服器運行的 `http://localhost:8080`。
- 建立了一個客戶端類別，將傳輸作為建構函數參數。
- 在 `run` 方法中，使用傳輸建立了一個同步 MCP 客戶端並初始化連接。
- 使用 SSE (Server-Sent Events) 傳輸，適合與 Java Spring Boot MCP 伺服器進行基於 HTTP 的通信。

#### Rust

此 Rust 客戶端假設伺服器是同一目錄中的兄弟專案 "calculator-server"。以下程式碼將啟動伺服器並連接到它。

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出伺服器功能

現在，我們有一個客戶端可以在程式運行時進行連接。然而，它尚未列出功能，因此接下來讓我們完成這部分：

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

在這裡，我們列出了可用的資源 `list_resources()` 和工具 `list_tools`，並將它們打印出來。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

以上是列出伺服器工具的範例。對於每個工具，我們打印出其名稱。

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

在上述程式碼中，我們：

- 調用 `listTools()` 以獲取 MCP 伺服器上的所有可用工具。
- 使用 `ping()` 驗證與伺服器的連接是否正常。
- `ListToolsResult` 包含所有工具的資訊，包括名稱、描述和輸入結構。

很好，現在我們已捕捉到所有功能。接下來的問題是何時使用它們？這個客戶端相對簡單，簡單的意思是我們需要在需要時顯式調用功能。在下一章中，我們將建立一個更高級的客戶端，該客戶端可以訪問自己的大型語言模型 (LLM)。但目前，讓我們看看如何調用伺服器上的功能：

#### Rust

在主函數中，初始化客戶端後，我們可以初始化伺服器並列出一些功能。

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 調用功能

要調用功能，我們需要確保指定正確的參數，有時還需要指定要調用的名稱。

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

在上述程式碼中，我們：

- 讀取資源，通過調用 `readResource()` 並指定 `uri`。以下是伺服器端的可能程式碼：

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

    我們的 `uri` 值 `file://example.txt` 與伺服器上的 `file://{name}` 匹配。`example.txt` 將映射到 `name`。

- 調用工具，通過指定其 `name` 和 `arguments` 來調用：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 獲取提示，通過 `getPrompt()` 調用 `name` 和 `arguments`。伺服器端程式碼如下：

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

    因此，您的客戶端程式碼如下，以匹配伺服器上聲明的內容：

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

在上述程式碼中，我們：

- 調用了名為 `greeting` 的資源，使用 `read_resource`。
- 調用了名為 `add` 的工具，使用 `call_tool`。

#### .NET

1. 添加一些程式碼以調用工具：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 打印結果，以下是處理結果的程式碼：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

- 使用 `callTool()` 方法和 `CallToolRequest` 物件調用了多個計算器工具。
- 每次工具調用都指定工具名稱和工具所需的參數 `Map`。
- 伺服器工具期望特定的參數名稱（例如 "a" 和 "b" 用於數學運算）。
- 結果以 `CallToolResult` 物件返回，包含伺服器的回應。

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

### -5- 運行客戶端

要運行客戶端，請在終端中輸入以下命令：

#### TypeScript

在 *package.json* 的 "scripts" 部分添加以下條目：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

使用以下命令調用客戶端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

首先，確保您的 MCP 伺服器正在 `http://localhost:8080` 運行。然後運行客戶端：

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，您可以運行解決方案資料夾 `03-GettingStarted\02-client\solution\java` 中提供的完整客戶端專案：

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作業

在此作業中，您將使用所學內容建立自己的客戶端。

以下是一個伺服器，您需要通過客戶端程式碼調用它，試著為伺服器添加更多功能，使其更有趣。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

查看此專案以了解如何 [添加提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

此外，查看此連結以了解如何調用 [提示和資源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在 [上一節](../../../../03-GettingStarted/01-first-server) 中，您學習了如何使用 Rust 建立一個簡單的 MCP 伺服器。您可以繼續基於此進行構建，或者查看此連結以獲取更多基於 Rust 的 MCP 伺服器範例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解決方案

**解決方案資料夾**包含完整、可運行的客戶端實現，展示了本教程涵蓋的所有概念。每個解決方案都包括客戶端和伺服器程式碼，並以獨立的專案形式組織。

### 📁 解決方案結構

解決方案目錄按程式語言組織：

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

### 🚀 每個解決方案包含什麼

每個語言特定的解決方案提供：

- **完整的客戶端實現**，包含本教程中的所有功能。
- **工作專案結構**，具有適當的依賴項和配置。
- **構建和運行腳本**，便於設置和執行。
- **詳細的 README**，提供語言特定的指導。
- **錯誤處理**和結果處理範例。

### 📖 使用解決方案

1. **導航到您偏好的語言資料夾**：

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **按照每個資料夾中的 README 指導**：
   - 安裝依賴項
   - 構建專案
   - 運行客戶端

3. **您應該看到的範例輸出**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

有關完整文檔和逐步指導，請參閱：**[📖 解決方案文檔](./solution/README.md)**

## 🎯 完整範例

我們提供了所有程式語言的完整、可運行的客戶端實現。這些範例展示了上述功能的全部內容，可用作參考實現或您自己專案的起點。

### 可用完整範例

| 語言 | 文件 | 描述 |
|------|------|------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 傳輸的完整 Java 客戶端，包含全面的錯誤處理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 傳輸的完整 C# 客戶端，包含自動伺服器啟動 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 完整的 TypeScript 客戶端，支持完整的 MCP 協議 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用 async/await 模式的完整 Python 客戶端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 進行非同步操作的完整 Rust 客戶端 |
每個完整範例包括：

- ✅ **建立連線**及錯誤處理
- ✅ **伺服器探索**（工具、資源、提示等適用）
- ✅ **計算器操作**（加、減、乘、除、幫助）
- ✅ **結果處理**及格式化輸出
- ✅ **全面的錯誤處理**
- ✅ **乾淨且有註解的程式碼**，附有逐步註解

### 開始使用完整範例

1. **從上表選擇你偏好的語言**
2. **檢視完整範例檔案**以了解完整的實現方式
3. **按照 [`complete_examples.md`](./complete_examples.md) 中的指示執行範例**
4. **根據你的特定需求修改及擴展範例**

如需有關執行及自訂這些範例的詳細文件，請參閱：**[📖 完整範例文件](./complete_examples.md)**

### 💡 解決方案 vs. 完整範例

| **解決方案資料夾** | **完整範例** |
|--------------------|--------------------- |
| 包含建置檔案的完整專案結構 | 單一檔案的實現 |
| 附帶依賴項目即可執行 | 專注於程式碼範例 |
| 接近生產環境的設置 | 教育性參考 |
| 特定語言的工具支持 | 跨語言比較 |

這兩種方法都很有價值——使用 **解決方案資料夾** 來完成專案，使用 **完整範例** 來學習及參考。

## 主要重點

本章的主要重點如下，關於客戶端：

- 可用於探索及調用伺服器上的功能。
- 可在啟動自身的同時啟動伺服器（如本章所述），但客戶端也可以連接到正在運行的伺服器。
- 是測試伺服器功能的好方法，與上一章提到的 Inspector 等替代方案相比。

## 其他資源

- [在 MCP 中建立客戶端](https://modelcontextprotocol.io/quickstart/client)

## 範例

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python)
- [Rust 計算器](../../../../03-GettingStarted/samples/rust)

## 下一步

- 下一步：[使用 LLM 建立客戶端](../03-llm-client/README.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
# 创建客户端

客户端是直接与 MCP 服务器通信以请求资源、工具和提示的自定义应用程序或脚本。与使用检视器工具提供的图形界面不同，编写您自己的客户端可以实现程序化和自动化交互。这使开发人员能够将 MCP 功能集成到自己的工作流中，自动化任务，并构建满足特定需求的定制解决方案。

## 概述

本课程介绍了 Model Context Protocol (MCP) 生态系统中的客户端概念。您将学习如何编写自己的客户端并使其连接到 MCP 服务器。

## 学习目标

通过本课程，您将能够：

- 理解客户端的功能。
- 编写您自己的客户端。
- 连接并测试客户端与 MCP 服务器，确保服务器按预期工作。

## 编写客户端需要什么？

编写客户端时，您需要完成以下步骤：

- <strong>导入正确的库</strong>。您将使用与之前相同的库，只是结构有所不同。
- <strong>实例化客户端</strong>。这包括创建客户端实例并连接到选定的传输方式。
- <strong>决定要列出哪些资源</strong>。您的 MCP 服务器提供了资源、工具和提示，您需要决定列出哪一类。
- <strong>将客户端集成到宿主应用程序</strong>。了解服务器的功能后，您需要将其集成到您的宿主应用程序中，以便用户输入提示或其他命令时调用相应的服务器功能。

现在我们已经从高层了解了将要做的事情，接下来看看示例。

### 示例客户端

让我们来看看这个示例客户端：

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

// 获取提示
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// 列出资源
const resources = await client.listResources();

// 读取资源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 调用工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

在上面的代码中，我们：

- 导入库
- 创建客户端实例并使用 stdio 传输连接它。
- 列出提示、资源和工具并调用它们。

就这样，一个可以与 MCP 服务器通信的客户端完成了。

在接下来的练习部分，我们会慢慢拆解每段代码并解释其功能。

## 练习：编写一个客户端

如上所述，我们将花时间详解代码，如果您愿意，也可以边学边写。

### -1- 导入库

让我们导入所需的库，我们需要引用客户端和传输协议 stdio。stdio 是针对本地运行程序的协议。SSE 是另一个传输协议，后续章节会介绍，但现在我们先继续用 stdio。

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

对于 Java，您将创建一个连接先前练习中 MCP 服务器的客户端。使用 [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) 中的 Java Spring Boot 项目结构，在 `src/main/java/com/microsoft/mcp/sample/client/` 目录下新建一个名为 `SDKClient` 的 Java 类，并添加以下导入：

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

您需要在 `Cargo.toml` 文件中添加以下依赖。

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

接着，您可以在客户端代码中导入所需库。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接下来进入实例化部分。

### -2- 实例化客户端和传输

我们需要创建传输实例和客户端实例：

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

在上述代码中，我们：

- 创建了一个 stdio 传输实例。注意它指定了启动服务器的命令和参数，这是创建客户端时需要做的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 实例化客户端并赋予其名称和版本。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 将客户端连接到所选传输。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 为 stdio 连接创建服务器参数
server_params = StdioServerParameters(
    command="mcp",  # 可执行文件
    args=["run", "server.py"],  # 可选的命令行参数
    env=None,  # 可选的环境变量
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 初始化连接
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

在上述代码中，我们：

- 导入所需库
- 实例化服务器参数对象，用于运行服务器以便客户端连接
- 定义 `run` 方法，调用 `stdio_client` 启动客户端会话
- 创建入口点，使用 `asyncio.run` 调用 `run` 方法

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

在上述代码中，我们：

- 导入所需库。
- 创建 stdio 传输并实例化客户端 `mcpClient`，用于列出和调用 MCP 服务器功能。

注意，“Arguments”中可以指向 *.csproj* 或可执行文件。

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
        
        // 你的客户端逻辑写在这里
    }
}
```

在上述代码中，我们：

- 创建主方法，设置 SSE 传输指向 `http://localhost:8080`，即 MCP 服务器运行地址。
- 创建客户端类，传输参数通过构造函数传入。
- 在 `run` 方法中使用传输创建同步 MCP 客户端并初始化连接。
- 使用 SSE（服务器推送事件）传输，适合 Java Spring Boot MCP 服务器的 HTTP 通信。

#### Rust

注意此 Rust 客户端假定服务器是同目录下名为 "calculator-server" 的兄弟项目。以下代码将启动服务器并连接。

```rust
async fn main() -> Result<(), RmcpError> {
    // 假设服务器是同一目录下名为 "calculator-server" 的兄弟项目
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

    // 待办：初始化

    // 待办：列出工具

    // 待办：调用添加工具，参数为 {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出服务器功能

现在我们有了可连接的客户端程序。但它还没列出功能，接下来实现此功能：

#### TypeScript

```typescript
// 列出提示
const prompts = await client.listPrompts();

// 列出资源
const resources = await client.listResources();

// 列出工具
const tools = await client.listTools();
```

#### Python

```python
# 列出可用资源
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

这里列出了可用的资源，`list_resources()` 和工具，`list_tools` 并打印它们。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上述示例展示了如何列出服务器上的工具，并打印每个工具名称。

#### Java

```java
// 列出并演示工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 您还可以通过ping服务器来验证连接
client.ping();
```

在上述代码中，我们：

- 调用 `listTools()` 获取 MCP 服务器所有可用工具。
- 使用 `ping()` 验证与服务器的连接是否正常。
- `ListToolsResult` 包含所有工具信息，包括名称、描述和输入模式。

很好，我们现在获取了所有功能。问题是何时调用它们？这个客户端比较简单，调用功能需显式调用。下章将创建更高级的客户端，带有自己的大型语言模型 LLM。现在先看看如何调用服务器的功能：

#### Rust

在主函数中，客户端初始化后可以初始化服务器并列出部分功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 调用功能

调用功能时需确保传入正确参数，有时还需指定要调用的名称。

#### TypeScript

```typescript

// 读取资源
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 调用工具
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// 调用提示
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

在上面的代码中，我们：

- 读取资源，通过调用 `readResource()` 并指定 `uri` 参数。服务器端代码大概是：

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

    我们的 `uri` 值 `file://example.txt` 对应服务器的 `file://{name}`。`example.txt` 被映射到 `name`。

- 调用工具，通过指定其 `name` 和 `arguments`：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 获取提示，通过调用 `getPrompt()` 并传入 `name` 和 `arguments`。服务器代码如下：

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

    因此，客户端代码看起来应该像这样，匹配服务器声明：

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
# 读取一个资源
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# 调用一个工具
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

上述代码中，我们：

- 调用了名为 `greeting` 的资源，用 `read_resource`。
- 调用了名为 `add` 的工具，用 `call_tool`。

#### .NET

1. 下面添加调用工具的代码：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 输出结果的代码如下：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// 调用各种计算器工具
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

在上述代码中，我们：

- 使用 `callTool()` 方法调用多个计算器工具，传入 `CallToolRequest` 对象。
- 每次调用指定工具名称和该工具所需参数的 `Map`。
- 服务器工具期望特定参数名（如数学运算的 "a", "b"）。
- 返回值为包含服务器响应的 `CallToolResult` 对象。

#### Rust

```rust
// 调用加法工具，参数为 = {"a": 3, "b": 2}
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

### -5- 运行客户端

要运行客户端，请在终端中输入以下命令：

#### TypeScript

在 *package.json* 的 "scripts" 区块中添加以下条目：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

通过以下命令调用客户端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

请确保 MCP 服务器运行在 `http://localhost:8080`，然后运行客户端：

```bash
# 构建您的项目
./mvnw clean compile

# 运行客户端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

您也可以运行解决方案文件夹中的完整客户端项目 `03-GettingStarted\02-client\solution\java`：

```bash
# 导航到解决方案目录
cd 03-GettingStarted/02-client/solution/java

# 构建并运行 JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 作业

在本作业中，您将运用所学知识创建自己的客户端。

这里有一个可用的服务器，您需要通过客户端代码调用它，尝试为服务器添加更多功能，使其更有趣。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 创建一个MCP服务器
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 添加一个加法工具
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 添加一个动态问候资源
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

// 开始在标准输入接收消息并在标准输出发送消息

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

# 创建一个 MCP 服务器
mcp = FastMCP("Demo")


# 添加一个加法工具
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 添加一个动态问候资源
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

查看此项目，了解如何 [添加提示和资源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

另请查看此链接了解如何调用 [提示和资源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在 [上一节](../../../../03-GettingStarted/01-first-server) 中，您学会了如何用 Rust 创建一个简单的 MCP 服务器。您可以在此基础上继续构建，或查看此链接获取更多基于 Rust 的 MCP 服务器示例：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解决方案

<strong>解决方案文件夹</strong>包含完整且可运行的客户端实现，演示了本教程涉及的所有概念。每个解决方案都包含独立且自包含的客户端和服务器代码项目。

### 📁 解决方案结构

解决方案目录按编程语言组织：

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

### 🚀 每个解决方案包含内容

每种语言的解决方案提供：

- <strong>完整客户端实现</strong>，包含教程中所有功能
- <strong>可用的项目结构</strong>，具备依赖和配置文件
- <strong>构建和运行脚本</strong>，便于设置和执行
- <strong>详细的自述文档</strong>，包含语言特定说明
- <strong>错误处理</strong>和结果处理示例

### 📖 使用解决方案

1. <strong>进入您偏好的语言文件夹</strong>：

   ```bash
   cd solution/typescript/    # 适用于 TypeScript
   cd solution/java/          # 适用于 Java
   cd solution/python/        # 适用于 Python
   cd solution/dotnet/        # 适用于 .NET
   ```

2. **遵循每个文件夹中的README说明**，包括：
   - 安装依赖
   - 构建项目
   - 运行客户端

3. <strong>示例输出</strong>您应看到：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

详细文档和分步指导见：**[📖 解决方案文档](./solution/README.md)**

## 🎯 完整示例

我们提供了覆盖本教程所有编程语言的完整工作客户端示例。这些示例展示了上述完整功能，您可用它们作为参考实现或自己项目的起点。

### 可用的完整示例

| 语言 | 文件 | 描述 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 传输的完整 Java 客户端，含全面错误处理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 传输的完整 C# 客户端，自动启动服务器 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 支持完整 MCP 协议的 TypeScript 客户端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用 async/await 模式的完整 Python 客户端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 实现异步操作的完整 Rust 客户端 |

每个完整示例都包含：

- ✅ <strong>连接建立</strong>和错误处理
- ✅ <strong>服务器发现</strong>（工具、资源、提示，如果适用）
- ✅ <strong>计算器操作</strong>（加、减、乘、除、帮助）
- ✅ <strong>结果处理</strong>和格式化输出
- ✅ <strong>全面的错误处理</strong>

- ✅ **干净、有注释的代码**，带有逐步注释

### 带完整示例的入门指南

1. <strong>从上表中选择您喜欢的语言</strong>
2. <strong>查看完整示例文件</strong> 以了解完整实现
3. **按照 [`complete_examples.md`](./complete_examples.md) 中的说明运行示例**
4. <strong>修改并扩展示例以适应您的具体用例</strong>

有关运行和自定义这些示例的详细文档，请参见：**[📖 完整示例文档](./complete_examples.md)**

### 💡 解决方案与完整示例的区别

| <strong>解决方案文件夹</strong> | <strong>完整示例</strong> |
|--------------------|--------------------- |
| 带有构建文件的完整项目结构 | 单文件实现 |
| 依赖齐全，可直接运行 | 针对性代码示例 |
| 类生产环境设置 | 教育参考 |
| 语言特定工具 | 跨语言对比 |

两种方法都很有价值——使用<strong>解决方案文件夹</strong>用于完整项目，使用<strong>完整示例</strong>用于学习和参考。

## 主要收获

本章关于客户端的主要收获如下：

- 可用于发现和调用服务器上的功能。
- 能在服务器启动时自行启动服务器（如本章所示），同时客户端也可以连接到正在运行的服务器。
- 是测试服务器功能的绝佳方式，类似前一章描述的 Inspector 等替代方案。

## 额外资源

- [在 MCP 中构建客户端](https://modelcontextprotocol.io/quickstart/client)

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.NET 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)
- [Rust 计算器](../../../../03-GettingStarted/samples/rust)

## 接下来

- 下一步：[用 LLM 创建客户端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
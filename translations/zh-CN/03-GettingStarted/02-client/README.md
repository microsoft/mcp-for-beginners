# 创建客户端

客户端是直接与 MCP 服务器通信以请求资源、工具和提示的自定义应用程序或脚本。与使用提供图形界面与服务器交互的检查器工具不同，编写自己的客户端允许进行程序化和自动化的交互。这使开发人员能够将 MCP 功能集成到自己的工作流程中，自动化任务，并构建针对特定需求的定制解决方案。

## 概述

本课程介绍了 Model Context Protocol (MCP) 生态系统中的客户端概念。您将学习如何编写自己的客户端并使其连接到 MCP 服务器。

## 学习目标

通过本课后，您将能够：

- 理解客户端能做什么。
- 编写您自己的客户端。
- 连接并测试客户端与 MCP 服务器以确保服务器按预期工作。

## 编写客户端需要哪些内容？

要编写客户端，您需要执行以下操作：

- **导入正确的库**。您将使用之前相同的库，但构造方式不同。
- **实例化客户端**。这包括创建客户端实例并连接到选定的传输方法。
- **决定列出哪些资源**。您的 MCP 服务器带有资源、工具和提示，您需要决定要列出其中的哪些。
- **将客户端集成到主机应用程序中**。一旦了解了服务器的功能，就需要将其集成到主机应用程序中，这样用户输入提示或其他命令时即可调用相应的服务器功能。

现在我们对即将要做的事情有了一个高级的了解，接下来让我们看一个示例。

### 客户端示例

来看这个客户端示例：

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

// 获取一个提示
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// 列出资源
const resources = await client.listResources();

// 读取一个资源
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

在前面的代码中，我们：

- 导入了库
- 创建了客户端实例并使用 stdio 作为传输连接它。
- 列出了提示、资源和工具，并调用了它们全部。

这就是一个可以与 MCP 服务器通信的客户端。

接下来练习部分，我们将花时间逐块分析代码并解释发生了什么。

## 练习：编写客户端

如上所述，让我们慢慢解释代码，如果愿意也可以边学边写代码。

### -1- 导入库

导入需要的库，我们需要引用客户端和选择的传输协议 stdio。stdio 是针对本地机器运行的协议。SSE 是未来章节展示的另一种传输协议，但目前我们继续使用 stdio。

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

对于 Java，您将创建一个连接到上一练习 MCP 服务器的客户端。沿用[开始使用 MCP 服务器](../../../../03-GettingStarted/01-first-server/solution/java)中的 Java Spring Boot 项目结构，在`src/main/java/com/microsoft/mcp/sample/client/`文件夹中创建一个名为 `SDKClient` 的 Java 类，并添加以下导入：

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

您需要在`Cargo.toml`文件中添加以下依赖项。

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

然后，在客户端代码中导入必要的库。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

接下来进行实例化。

### -2- 实例化客户端和传输

我们需要创建一个传输实例和客户端实例：

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

在前面的代码中我们：

- 创建了一个 stdio 传输实例。注意它如何指定用于查找和启动服务器的命令和参数，因为这正是创建客户端时需要做的。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 通过给客户端指定名称和版本来实例化客户端。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 将客户端连接到选定的传输。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 为stdio连接创建服务器参数
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

在前面的代码中我们：

- 导入了需要的库
- 实例化了服务器参数对象，因为我们将用它运行服务器，这样客户端才能连接。
- 定义了一个方法 `run`，它调用 `stdio_client` 来启动客户端会话。
- 创建了入口点，将 `run` 方法传递给 `asyncio.run`。

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

在前面的代码中我们：

- 导入了需要的库。
- 创建了 stdio 传输并创建了客户端 `mcpClient`。后者将用于列出和调用 MCP 服务器上的功能。

注意，“参数”中，您可以指向 *.csproj* 文件或可执行文件。

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
        
        // 您的客户端逻辑写在这里
    }
}
```

在前面的代码中我们：

- 创建了一个主方法，设置了一个指向 `http://localhost:8080` 的 SSE 传输，MCP 服务器将在此运行。
- 创建了一个客户端类，构造函数接收传输参数。
- 在 `run` 方法中，使用传输创建同步 MCP 客户端并初始化连接。
- 使用 SSE（服务器发送事件）传输，适用于 Java Spring Boot MCP 服务器上的基于 HTTP 的通信。

#### Rust

注意此 Rust 客户端假定服务器是同一目录中名为 "calculator-server" 的兄弟项目。下面代码将启动服务器并连接它。

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

    // 待办事项：初始化

    // 待办事项：列出工具

    // 待办事项：调用添加工具，参数 = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- 列出服务器功能

现在，我们已有可以连接到服务器的客户端。如果程序运行，连接应该有效。然而，目前它没有实际列出服务器功能，下一步我们来实现这个：

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

这里我们列出了可用的资源 `list_resources()` 和工具 `list_tools`，并打印它们。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上面示例展示了如何列出服务器上的工具。对于每个工具，我们打印其名称。

#### Java

```java
// 列出并演示工具
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 您还可以ping服务器以验证连接
client.ping();
```

在前面的代码中我们：

- 调用 `listTools()` 获取 MCP 服务器上所有可用工具。
- 使用 `ping()` 验证与服务器的连接是否正常。
- `ListToolsResult` 包含了所有工具的信息，包括名称、描述和输入模式。

很好，现在我们捕获了所有功能。接下来的问题是，我们什么时候使用这些功能？此客户端相对简单，意思是我们需要明确调用功能。当我们需要它们时显式调用即可。下一章我们将创建一个更高级客户端，拥有自己的大型语言模型（LLM）。现在我们先看看如何调用服务器上的功能：

#### Rust

在主函数中，初始化客户端后，我们可以初始化服务器并列出一些功能。

```rust
// 初始化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 列出工具
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 调用功能

调用功能时，需要确保指定正确的参数，在某些情况下还要指定调用名称。

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

在前面的代码中我们：

- 读取资源，通过调用 `readResource()` 并指定 `uri`。服务器端对应如下：

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

    我们的 `uri` 值 `file://example.txt` 匹配服务器端 `file://{name}`，`example.txt` 将映射为 `name`。

- 调用工具，调用方式是指定其 `name` 和 `arguments`，如下：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 获取提示，调用 `getPrompt()` 并传入 `name` 和 `arguments`。服务器端代码示例如下：

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

    因此客户端代码对应如下，以匹配服务器端的声明：

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
# 读取资源
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# 调用工具
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

在上述代码中，我们：

- 使用 `read_resource` 调用了一个名为 `greeting` 的资源。
- 使用 `call_tool` 调用了一个名为 `add` 的工具。

#### .NET

1. 添加调用工具的代码：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 打印结果的代码示例：

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

在前面的代码中我们：

- 使用 `callTool()` 方法调用了多个计算器工具，传入了 `CallToolRequest` 对象。
- 每个工具调用都指定工具名称和对应参数映射。
- 服务器工具期望特定参数名（如数学运算的 "a", "b"）。
- 结果作为 `CallToolResult` 对象返回，包含服务器响应。

#### Rust

```rust
// 使用参数调用加法工具 = {"a": 3, "b": 2}
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

在终端输入以下命令运行客户端：

#### TypeScript

在 *package.json* 的 "scripts" 部分添加以下内容：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

使用以下命令调用客户端：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

确保 MCP 服务器正在 `http://localhost:8080` 运行。然后运行客户端：

```bash
# 构建你的项目
./mvnw clean compile

# 运行客户端
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

或者，您也可以运行位于解决方案文件夹 `03-GettingStarted\02-client\solution\java` 中的完整客户端项目：

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

本作业中，您将运用所学知识创建自己的客户端。

这是一个您可以使用的服务器，需通过客户端代码调用，看看能否为服务器添加更多功能以使其更有趣。

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

// 添加动态问候资源
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

# 创建一个MCP服务器
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

请参阅此项目，了解如何[添加提示和资源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)。

还可以访问此链接，查看如何调用[提示和资源](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)。

### Rust

在[前一章节](../../../../03-GettingStarted/01-first-server)中，您学习了如何使用 Rust 创建简单 MCP 服务器。您可以继续基于该项目开发，或者参考这个链接，获取更多基于 Rust 的 MCP 服务器示例：[MCP 服务器示例](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解决方案

**解决方案文件夹**包含完整、可直接运行的客户端实现，演示了本教程涵盖的所有概念。每个解决方案包括分别组织的客户端和服务器代码，具有独立工程结构。

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

每个语言特定的解决方案提供：

- **完整客户端实现**，覆盖教程中所有功能
- **工作项目结构**，包含正确的依赖和配置
- **构建和运行脚本**，方便快速搭建和执行
- **详细的 README**，含语言特有的指导
- **错误处理和结果处理示例**

### 📖 使用解决方案

1. **进入您偏好的语言文件夹：**

   ```bash
   cd solution/typescript/    # 用于TypeScript
   cd solution/java/          # 用于Java
   cd solution/python/        # 用于Python
   cd solution/dotnet/        # 用于.NET
   ```

2. **按照每个文件夹中的 README 指南操作：**
   - 安装依赖
   - 构建项目
   - 运行客户端

3. **示例输出应如下所示：**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完整文档及逐步指南，请见：**[📖 解决方案文档](./solution/README.md)**

## 🎯 完整示例

我们提供了涵盖本教程中所有编程语言的完整、可运行客户端实现。这些示例演示了上述全部功能，可作为参考实现或您项目的起点。

### 可用完整示例

| 语言 | 文件 | 描述 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | 使用 SSE 传输的完整 Java 客户端，包含全面的错误处理 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | 使用 stdio 传输且支持自动启动服务器的完整 C# 客户端 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | 支持完整 MCP 协议的 TypeScript 客户端 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | 使用异步/等待模式的完整 Python 客户端 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | 使用 Tokio 进行异步操作的完整 Rust 客户端 |

每个完整示例均包含：
- ✅ **连接建立** 和错误处理
- ✅ **服务器发现**（工具、资源、提示，如适用）
- ✅ **计算器操作**（加、减、乘、除、帮助）
- ✅ **结果处理** 和格式化输出
- ✅ **全面的错误处理**
- ✅ **简洁、文档齐全的代码**，带有逐步注释

### 开始使用完整示例

1. **从上表中选择您偏好的语言**
2. **查看完整示例文件** 以理解完整实现
3. **按照 [`complete_examples.md`](./complete_examples.md) 中的说明运行示例**
4. **修改和扩展** 示例以满足您的特定用例

有关运行和自定义这些示例的详细文档，请参见：**[📖 完整示例文档](./complete_examples.md)**

### 💡 解决方案与完整示例

| **解决方案文件夹** | **完整示例** |
|--------------------|--------------|
| 完整项目结构，含构建文件 | 单文件实现 |
| 可运行，含依赖项 | 重点代码示例 |
| 生产级别设置 | 教学参考 |
| 语言特定工具 | 跨语言比较 |

两种方法都很有价值 —— 使用**解决方案文件夹**来构建完整项目，使用**完整示例**进行学习和参考。

## 关键要点

本章节关于客户端的关键要点如下：

- 可用于发现服务器上的功能并调用它们。
- 可以在客户端启动自己的同时启动服务器（如本章所示），但客户端也可以连接到正在运行的服务器。
- 是测试服务器功能的极好方式，类似于上一章所述的 Inspector 工具。

## 额外资源

- [在 MCP 中构建客户端](https://modelcontextprotocol.io/quickstart/client)

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)
- [Rust 计算器](../../../../03-GettingStarted/samples/rust)

## 接下来

- 下一章：[使用 LLM 创建客户端](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文档的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误读负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
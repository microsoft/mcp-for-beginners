# Tạo một client

Client là các ứng dụng hoặc script tùy chỉnh giao tiếp trực tiếp với MCP Server để yêu cầu tài nguyên, công cụ và gợi ý. Khác với việc sử dụng công cụ inspector, cung cấp giao diện đồ họa để tương tác với server, việc viết client của riêng bạn cho phép tương tác lập trình và tự động hóa. Điều này giúp các nhà phát triển tích hợp khả năng của MCP vào quy trình làm việc của họ, tự động hóa các tác vụ và xây dựng các giải pháp tùy chỉnh phù hợp với nhu cầu cụ thể.

## Tổng quan

Bài học này giới thiệu khái niệm về client trong hệ sinh thái Model Context Protocol (MCP). Bạn sẽ học cách viết client của riêng mình và kết nối nó với MCP Server.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Hiểu được những gì một client có thể làm.
- Viết client của riêng bạn.
- Kết nối và kiểm tra client với MCP Server để đảm bảo server hoạt động như mong đợi.

## Những gì cần làm để viết một client?

Để viết một client, bạn cần thực hiện các bước sau:

- **Nhập đúng thư viện**. Bạn sẽ sử dụng cùng thư viện như trước, chỉ khác các cấu trúc.
- **Khởi tạo một client**. Điều này bao gồm việc tạo một instance của client và kết nối nó với phương thức truyền tải đã chọn.
- **Quyết định tài nguyên nào cần liệt kê**. MCP Server của bạn đi kèm với các tài nguyên, công cụ và gợi ý, bạn cần quyết định cái nào sẽ được liệt kê.
- **Tích hợp client vào ứng dụng host**. Khi bạn đã biết khả năng của server, bạn cần tích hợp nó vào ứng dụng host để khi người dùng nhập một gợi ý hoặc lệnh khác, tính năng tương ứng của server sẽ được kích hoạt.

Bây giờ chúng ta đã hiểu sơ bộ những gì cần làm, hãy xem một ví dụ tiếp theo.

### Một ví dụ về client

Hãy xem ví dụ về client này:

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

Trong đoạn mã trên, chúng ta đã:

- Nhập các thư viện.
- Tạo một instance của client và kết nối nó bằng stdio để truyền tải.
- Liệt kê các gợi ý, tài nguyên và công cụ, sau đó gọi tất cả.

Vậy là bạn đã có một client có thể giao tiếp với MCP Server.

Hãy dành thời gian trong phần bài tập tiếp theo để phân tích từng đoạn mã và giải thích những gì đang diễn ra.

## Bài tập: Viết một client

Như đã nói ở trên, hãy dành thời gian giải thích mã, và nếu muốn, bạn có thể viết mã cùng lúc.

### -1- Nhập các thư viện

Hãy nhập các thư viện cần thiết, chúng ta sẽ cần tham chiếu đến một client và giao thức truyền tải đã chọn, stdio. stdio là một giao thức dành cho các chương trình chạy trên máy cục bộ của bạn. SSE là một giao thức truyền tải khác mà chúng ta sẽ giới thiệu trong các chương sau, nhưng đó là lựa chọn khác của bạn. Hiện tại, hãy tiếp tục với stdio.

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

Đối với Java, bạn sẽ tạo một client kết nối với MCP Server từ bài tập trước. Sử dụng cấu trúc dự án Java Spring Boot tương tự từ [Bắt đầu với MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), tạo một lớp Java mới có tên `SDKClient` trong thư mục `src/main/java/com/microsoft/mcp/sample/client/` và thêm các thư viện sau:

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

Bạn sẽ cần thêm các dependency sau vào tệp `Cargo.toml`.

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

Từ đó, bạn có thể nhập các thư viện cần thiết vào mã client của mình.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Hãy chuyển sang bước khởi tạo.

### -2- Khởi tạo client và giao thức truyền tải

Chúng ta sẽ cần tạo một instance của giao thức truyền tải và của client:

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

Trong đoạn mã trên, chúng ta đã:

- Tạo một instance giao thức truyền tải stdio. Lưu ý cách nó chỉ định lệnh và tham số để tìm và khởi động server, vì đó là điều chúng ta cần làm khi tạo client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Khởi tạo một client bằng cách cung cấp tên và phiên bản.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Kết nối client với giao thức truyền tải đã chọn.

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

Trong đoạn mã trên, chúng ta đã:

- Nhập các thư viện cần thiết.
- Khởi tạo một đối tượng tham số server vì chúng ta sẽ sử dụng nó để chạy server để có thể kết nối với client của mình.
- Định nghĩa một phương thức `run` gọi `stdio_client`, bắt đầu một phiên client.
- Tạo một điểm vào nơi chúng ta cung cấp phương thức `run` cho `asyncio.run`.

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

Trong đoạn mã trên, chúng ta đã:

- Nhập các thư viện cần thiết.
- Tạo một giao thức truyền tải stdio và một client `mcpClient`. Client này sẽ được sử dụng để liệt kê và gọi các tính năng trên MCP Server.

Lưu ý, trong "Arguments", bạn có thể chỉ đến tệp *.csproj* hoặc tệp thực thi.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo một phương thức chính thiết lập giao thức truyền tải SSE trỏ đến `http://localhost:8080`, nơi MCP Server của chúng ta sẽ chạy.
- Tạo một lớp client nhận giao thức truyền tải làm tham số constructor.
- Trong phương thức `run`, chúng ta tạo một client MCP đồng bộ sử dụng giao thức truyền tải và khởi tạo kết nối.
- Sử dụng giao thức truyền tải SSE (Server-Sent Events), phù hợp cho giao tiếp dựa trên HTTP với các MCP Server Java Spring Boot.

#### Rust

Client Rust này giả định server là một dự án anh em có tên "calculator-server" trong cùng thư mục. Mã dưới đây sẽ khởi động server và kết nối với nó.

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

### -3- Liệt kê các tính năng của server

Bây giờ, chúng ta đã có một client có thể kết nối nếu chương trình được chạy. Tuy nhiên, nó chưa thực sự liệt kê các tính năng, vì vậy hãy làm điều đó tiếp theo:

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

Ở đây chúng ta liệt kê các tài nguyên có sẵn, `list_resources()` và công cụ, `list_tools`, sau đó in chúng ra.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Trên đây là một ví dụ về cách chúng ta có thể liệt kê các công cụ trên server. Đối với mỗi công cụ, chúng ta in ra tên của nó.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Trong đoạn mã trên, chúng ta đã:

- Gọi `listTools()` để lấy tất cả các công cụ có sẵn từ MCP Server.
- Sử dụng `ping()` để xác minh rằng kết nối với server đang hoạt động.
- `ListToolsResult` chứa thông tin về tất cả các công cụ bao gồm tên, mô tả và schema đầu vào của chúng.

Tuyệt vời, bây giờ chúng ta đã nắm bắt tất cả các tính năng. Câu hỏi tiếp theo là khi nào chúng ta sử dụng chúng? Client này khá đơn giản, đơn giản ở chỗ chúng ta sẽ cần gọi các tính năng một cách rõ ràng khi muốn sử dụng chúng. Trong chương tiếp theo, chúng ta sẽ tạo một client nâng cao hơn có quyền truy cập vào mô hình ngôn ngữ lớn (LLM) của riêng nó. Hiện tại, hãy xem cách chúng ta có thể gọi các tính năng trên server:

#### Rust

Trong hàm chính, sau khi khởi tạo client, chúng ta có thể khởi tạo server và liệt kê một số tính năng của nó.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Gọi các tính năng

Để gọi các tính năng, chúng ta cần đảm bảo chỉ định đúng tham số và trong một số trường hợp là tên của tính năng cần gọi.

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

Trong đoạn mã trên, chúng ta đã:

- Đọc một tài nguyên, chúng ta gọi tài nguyên bằng cách gọi `readResource()` và chỉ định `uri`. Đây là cách nó có thể trông như thế nào trên server:

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

    Giá trị `uri` của chúng ta `file://example.txt` khớp với `file://{name}` trên server. `example.txt` sẽ được ánh xạ tới `name`.

- Gọi một công cụ, chúng ta gọi nó bằng cách chỉ định `name` và `arguments` như sau:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Lấy gợi ý, để lấy gợi ý, bạn gọi `getPrompt()` với `name` và `arguments`. Mã server trông như sau:

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

    Và mã client của bạn sẽ trông như sau để khớp với những gì được khai báo trên server:

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

Trong đoạn mã trên, chúng ta đã:

- Gọi một tài nguyên có tên `greeting` bằng `read_resource`.
- Gọi một công cụ có tên `add` bằng `call_tool`.

#### .NET

1. Thêm một đoạn mã để gọi công cụ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Để in kết quả, đây là một đoạn mã để xử lý:

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

Trong đoạn mã trên, chúng ta đã:

- Gọi nhiều công cụ tính toán bằng phương thức `callTool()` với các đối tượng `CallToolRequest`.
- Mỗi lần gọi công cụ chỉ định tên công cụ và một `Map` các tham số cần thiết cho công cụ đó.
- Các công cụ server yêu cầu các tên tham số cụ thể (như "a", "b" cho các phép toán).
- Kết quả được trả về dưới dạng các đối tượng `CallToolResult` chứa phản hồi từ server.

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

### -5- Chạy client

Để chạy client, nhập lệnh sau vào terminal:

#### TypeScript

Thêm mục sau vào phần "scripts" trong *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Gọi client với lệnh sau:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Đầu tiên, đảm bảo MCP Server của bạn đang chạy trên `http://localhost:8080`. Sau đó chạy client:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Ngoài ra, bạn có thể chạy dự án client hoàn chỉnh được cung cấp trong thư mục giải pháp `03-GettingStarted\02-client\solution\java`:

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

## Bài tập

Trong bài tập này, bạn sẽ sử dụng những gì đã học để tạo một client của riêng mình.

Dưới đây là một server bạn có thể sử dụng mà bạn cần gọi thông qua mã client của mình, thử thêm nhiều tính năng hơn vào server để làm cho nó thú vị hơn.

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

Xem dự án này để biết cách [thêm gợi ý và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Ngoài ra, kiểm tra liên kết này để biết cách gọi [gợi ý và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Trong [phần trước](../../../../03-GettingStarted/01-first-server), bạn đã học cách tạo một MCP Server đơn giản với Rust. Bạn có thể tiếp tục xây dựng dựa trên đó hoặc kiểm tra liên kết này để biết thêm các ví dụ về MCP Server dựa trên Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Giải pháp

**Thư mục giải pháp** chứa các triển khai client hoàn chỉnh, sẵn sàng chạy, minh họa tất cả các khái niệm được đề cập trong hướng dẫn này. Mỗi giải pháp bao gồm cả mã client và server được tổ chức trong các dự án riêng biệt, độc lập.

### 📁 Cấu trúc giải pháp

Thư mục giải pháp được tổ chức theo ngôn ngữ lập trình:

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

### 🚀 Những gì mỗi giải pháp bao gồm

Mỗi giải pháp theo ngôn ngữ cung cấp:

- **Triển khai client hoàn chỉnh** với tất cả các tính năng từ hướng dẫn.
- **Cấu trúc dự án hoạt động** với các dependency và cấu hình phù hợp.
- **Script build và chạy** để dễ dàng thiết lập và thực thi.
- **README chi tiết** với hướng dẫn cụ thể cho từng ngôn ngữ.
- **Ví dụ xử lý lỗi** và xử lý kết quả.

### 📖 Sử dụng các giải pháp

1. **Đi đến thư mục ngôn ngữ bạn chọn**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Làm theo hướng dẫn trong README** trong mỗi thư mục để:
   - Cài đặt các dependency.
   - Build dự án.
   - Chạy client.

3. **Kết quả ví dụ** bạn sẽ thấy:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Để biết tài liệu đầy đủ và hướng dẫn từng bước, xem: **[📖 Tài liệu giải pháp](./solution/README.md)**

## 🎯 Ví dụ hoàn chỉnh

Chúng tôi đã cung cấp các triển khai client hoàn chỉnh, hoạt động cho tất cả các ngôn ngữ lập trình được đề cập trong hướng dẫn này. Các ví dụ này minh họa đầy đủ chức năng được mô tả ở trên và có thể được sử dụng làm tài liệu tham khảo hoặc điểm bắt đầu cho các dự án của riêng bạn.

### Các ví dụ hoàn chỉnh có sẵn

| Ngôn ngữ | Tệp | Mô tả |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java hoàn chỉnh sử dụng giao thức SSE với xử lý lỗi toàn diện |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# hoàn chỉnh sử dụng giao thức stdio với khởi động server tự động |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript hoàn chỉnh với hỗ trợ đầy đủ giao thức MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python hoàn chỉnh sử dụng các mẫu async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust hoàn chỉnh sử dụng Tokio cho các hoạt động async |
Mỗi ví dụ hoàn chỉnh bao gồm:

- ✅ **Thiết lập kết nối** và xử lý lỗi
- ✅ **Khám phá máy chủ** (công cụ, tài nguyên, gợi ý khi cần)
- ✅ **Các phép toán máy tính** (cộng, trừ, nhân, chia, trợ giúp)
- ✅ **Xử lý kết quả** và định dạng đầu ra
- ✅ **Xử lý lỗi toàn diện**
- ✅ **Mã sạch, có chú thích** với các bước giải thích chi tiết

### Bắt đầu với các ví dụ hoàn chỉnh

1. **Chọn ngôn ngữ bạn muốn** từ bảng trên
2. **Xem xét tệp ví dụ hoàn chỉnh** để hiểu toàn bộ cách triển khai
3. **Chạy ví dụ** theo hướng dẫn trong [`complete_examples.md`](./complete_examples.md)
4. **Tùy chỉnh và mở rộng** ví dụ cho trường hợp sử dụng cụ thể của bạn

Để xem tài liệu chi tiết về cách chạy và tùy chỉnh các ví dụ này, hãy xem: **[📖 Tài liệu Ví dụ Hoàn Chỉnh](./complete_examples.md)**

### 💡 Giải pháp vs. Ví dụ Hoàn Chỉnh

| **Thư mục Giải pháp** | **Ví dụ Hoàn Chỉnh** |
|--------------------|--------------------- |
| Cấu trúc dự án đầy đủ với các tệp build | Triển khai trong một tệp duy nhất |
| Sẵn sàng chạy với các phụ thuộc | Ví dụ mã tập trung |
| Thiết lập giống sản phẩm | Tài liệu tham khảo giáo dục |
| Công cụ dành riêng cho ngôn ngữ | So sánh giữa các ngôn ngữ |

Cả hai cách tiếp cận đều có giá trị - sử dụng **thư mục giải pháp** cho các dự án hoàn chỉnh và **ví dụ hoàn chỉnh** để học tập và tham khảo.

## Những điểm chính cần lưu ý

Những điểm chính cần lưu ý trong chương này về các client:

- Có thể được sử dụng để vừa khám phá vừa gọi các tính năng trên máy chủ.
- Có thể khởi động một máy chủ trong khi tự khởi động (như trong chương này), nhưng các client cũng có thể kết nối với các máy chủ đang chạy.
- Là một cách tuyệt vời để kiểm tra khả năng của máy chủ bên cạnh các lựa chọn thay thế như Inspector đã được mô tả trong chương trước.

## Tài nguyên bổ sung

- [Xây dựng client trong MCP](https://modelcontextprotocol.io/quickstart/client)

## Mẫu

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)
- [Máy tính Rust](../../../../03-GettingStarted/samples/rust)

## Tiếp theo

- Tiếp theo: [Tạo client với LLM](../03-llm-client/README.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
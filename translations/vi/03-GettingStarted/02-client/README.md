# Tạo một client

Client là các ứng dụng hoặc script tùy chỉnh giao tiếp trực tiếp với MCP Server để yêu cầu tài nguyên, công cụ và prompt. Khác với việc sử dụng công cụ inspector, vốn cung cấp giao diện đồ họa để tương tác với server, việc viết client riêng cho phép tương tác theo chương trình và tự động hóa. Điều này giúp các nhà phát triển tích hợp các khả năng của MCP vào quy trình làm việc của riêng họ, tự động hóa các nhiệm vụ và xây dựng giải pháp tùy chỉnh phù hợp với nhu cầu cụ thể.

## Tổng quan

Bài học này giới thiệu khái niệm về client trong hệ sinh thái Model Context Protocol (MCP). Bạn sẽ học cách viết client riêng của mình và kết nối nó với MCP Server.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Hiểu client có thể làm gì.
- Viết client riêng.
- Kết nối và thử nghiệm client với MCP server để đảm bảo server hoạt động như mong đợi.

## Viết client bao gồm những gì?

Để viết client, bạn cần thực hiện các bước sau:

- **Nhập các thư viện đúng**. Bạn sẽ sử dụng cùng thư viện như trước, chỉ khác cấu trúc.
- **Tạo một instance client**. Điều này bao gồm tạo một instance client và kết nối nó với phương thức truyền tải đã chọn.
- **Quyết định tài nguyên cần liệt kê**. MCP server có tài nguyên, công cụ và prompt, bạn cần chọn những cái nào sẽ liệt kê.
- **Tích hợp client vào ứng dụng chủ**. Khi bạn đã biết các năng lực của server, bạn cần tích hợp chức năng này vào ứng dụng chủ sao cho nếu người dùng nhập prompt hay lệnh nào đó, tính năng tương ứng của server sẽ được gọi.

Giờ chúng ta đã hiểu ở cấp độ tổng quát việc mình sắp làm, hãy xem một ví dụ bên dưới.

### Ví dụ về một client

Hãy xem ví dụ client này:

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

// Liệt kê các lời nhắc
const prompts = await client.listPrompts();

// Lấy một lời nhắc
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Liệt kê các tài nguyên
const resources = await client.listResources();

// Đọc một tài nguyên
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Gọi một công cụ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Trong đoạn mã trên, chúng ta:

- Nhập các thư viện
- Tạo instance client và kết nối với phương thức truyền tải stdio.
- Liệt kê prompt, tài nguyên và công cụ rồi gọi tất cả.

Bạn đã có một client có thể giao tiếp với MCP Server.

Hãy dành thời gian ở phần bài tập kế tiếp để phân tích từng đoạn code và giải thích chi tiết.

## Bài tập: Viết client

Như đã nói ở trên, hãy dành thời gian chú giải mã nguồn, và bạn có thể code theo nếu muốn.

### -1- Nhập thư viện

Hãy nhập các thư viện cần thiết, bạn cần tham chiếu client và giao thức truyền tải stdio. stdio là giao thức cho các ứng dụng chạy trên máy cục bộ. SSE là một giao thức truyền tải khác mà chúng tôi sẽ trình bày trong các chương sau, nhưng giờ bạn hãy tiếp tục với stdio.

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

Đối với Java, bạn tạo client kết nối tới MCP server ở bài tập trước. Sử dụng cùng cấu trúc dự án Java Spring Boot từ [Bắt đầu với MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), tạo một lớp Java mới tên `SDKClient` trong thư mục `src/main/java/com/microsoft/mcp/sample/client/` và thêm các import sau:

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

Bạn sẽ cần thêm các dependencies sau vào file `Cargo.toml`.

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

Sau đó, bạn có thể import các thư viện cần thiết vào mã client.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Chúng ta chuyển sang phần khởi tạo.

### -2- Khởi tạo client và transport

Chúng ta sẽ tạo một instance transport và một instance client:

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

Trong đoạn code trên, chúng ta đã:

- Tạo một instance transport stdio. Chú ý nó chỉ định `command` và `args` để tìm và khởi động server, việc này cần thiết khi tạo client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Khởi tạo client với tên và phiên bản.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Kết nối client với transport đã chọn.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Tạo các tham số máy chủ cho kết nối stdio
server_params = StdioServerParameters(
    command="mcp",  # Tệp thực thi
    args=["run", "server.py"],  # Các đối số dòng lệnh tùy chọn
    env=None,  # Các biến môi trường tùy chọn
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Khởi tạo kết nối
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Trong đoạn code trên, chúng ta:

- Nhập các thư viện cần thiết.
- Khởi tạo đối tượng tham số server để chạy server, giúp client kết nối.
- Định nghĩa phương thức `run` gọi `stdio_client` để bắt đầu phiên client.
- Tạo điểm vào, dùng `asyncio.run` chạy `run`.

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

Trong đoạn code trên:

- Nhập các thư viện cần thiết.
- Tạo transport stdio và tạo client `mcpClient`. Đây là đối tượng dùng để liệt kê và gọi các tính năng trên MCP Server.

Lưu ý, trong "Arguments", bạn có thể trỏ tới file *.csproj* hoặc file thực thi.

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
        
        // Logic khách hàng của bạn được đặt ở đây
    }
}
```

Trong đoạn code trên:

- Tạo phương thức main thiết lập transport SSE trỏ tới `http://localhost:8080` – địa chỉ MCP server chạy.
- Tạo lớp client nhận transport qua constructor.
- Trong phương thức `run`, tạo một MCP client đồng bộ dùng transport và khởi tạo kết nối.
- Sử dụng SSE (Server-Sent Events) phù hợp giao tiếp HTTP với MCP server Java Spring Boot.

#### Rust

Lưu ý client Rust này giả định server là một dự án anh em có tên "calculator-server" trong cùng thư mục. Code dưới đây sẽ khởi động server và kết nối tới nó.

```rust
async fn main() -> Result<(), RmcpError> {
    // Giả sử server là một dự án anh em tên là "calculator-server" trong cùng thư mục
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

    // TODO: Khởi tạo

    // TODO: Liệt kê các công cụ

    // TODO: Gọi công cụ add với các đối số = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Liệt kê các tính năng của server

Bây giờ, chúng ta có client có thể kết nối nếu chạy chương trình. Tuy nhiên, nó chưa liệt kê các tính năng, hãy thực hiện bước này:

#### TypeScript

```typescript
// Liệt kê các lời nhắc
const prompts = await client.listPrompts();

// Liệt kê các tài nguyên
const resources = await client.listResources();

// liệt kê các công cụ
const tools = await client.listTools();
```

#### Python

```python
# Liệt kê các tài nguyên có sẵn
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Liệt kê các công cụ có sẵn
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tại đây, chúng ta liệt kê tài nguyên bằng `list_resources()` và công cụ bằng `list_tools()` rồi in ra.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Đây là ví dụ về cách liệt kê các công cụ trên server. Với mỗi công cụ, chúng ta in ra tên.

#### Java

```java
// Liệt kê và trình bày các công cụ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Bạn cũng có thể ping máy chủ để xác minh kết nối
client.ping();
```

Trong đoạn code trên:

- Gọi `listTools()` để lấy tất cả công cụ có trên MCP server.
- Dùng `ping()` để xác thực kết nối tới server.
- `ListToolsResult` chứa thông tin về công cụ, bao gồm tên, mô tả, và cấu trúc đầu vào.

Tuyệt vời, bây giờ chúng ta đã lấy danh sách tính năng. Vậy khi nào sử dụng chúng? Client này khá đơn giản, tức chúng ta cần gọi thủ công khi muốn dùng. Trong chương tiếp theo, chúng ta sẽ tạo client nâng cao có tích hợp mô hình ngôn ngữ lớn (LLM). Còn giờ, xem cách gọi tính năng trên server:

#### Rust

Trong hàm main, sau khi khởi tạo client, ta có thể khởi động server và liệt kê một số tính năng của nó.

```rust
// Khởi tạo
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Liệt kê công cụ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Gọi tính năng

Để gọi tính năng, cần chỉ rõ đối số phù hợp và trong một số trường hợp là tên của tính năng muốn gọi.

#### TypeScript

```typescript

// Đọc một tài nguyên
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Gọi một công cụ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// gọi lời nhắc
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Trong đoạn code trên, chúng ta:

- Đọc một tài nguyên, gọi bằng `readResource()` với `uri`. Đây là cấu trúc trên server:

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

    Giá trị `uri` là `file://example.txt` tương ứng `file://{name}` trên server. `example.txt` sẽ được gán cho `name`.

- Gọi một công cụ, chỉ định `name` và `arguments` như sau:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Lấy prompt, gọi `getPrompt()` với `name` và `arguments`. Mã server trông như sau:

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

    Do đó mã client tương ứng sẽ như sau:

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
# Đọc một tài nguyên
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Gọi một công cụ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Trong đoạn code trên:

- Gọi tài nguyên tên `greeting` qua `read_resource`.
- Gọi công cụ tên `add` qua `call_tool`.

#### .NET

1. Thêm mã gọi một công cụ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Để in kết quả, đây là đoạn xử lý:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Gọi các công cụ máy tính khác nhau
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

Trong đoạn code trên:

- Gọi nhiều công cụ toán học bằng `callTool()` với các đối tượng `CallToolRequest`.
- Mỗi cuộc gọi chỉ định tên công cụ và `Map` các tham số cần thiết.
- Công cụ server kỳ vọng tham số hợp lệ (ví dụ "a", "b").
- Kết quả trả về là các đối tượng `CallToolResult` chứa phản hồi từ server.

#### Rust

```rust
// Gọi công cụ add với các đối số = {"a": 3, "b": 2}
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

Để chạy client, gõ lệnh sau trong terminal:

#### TypeScript

Thêm đoạn cấu hình sau vào phần "scripts" trong *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Gọi client với lệnh:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Đảm bảo MCP server chạy tại `http://localhost:8080`, sau đó chạy client:

```bash
# Xây dựng dự án của bạn
./mvnw clean compile

# Chạy client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Bạn cũng có thể chạy dự án client hoàn chỉnh trong thư mục giải pháp `03-GettingStarted\02-client\solution\java`:

```bash
# Điều hướng đến thư mục giải pháp
cd 03-GettingStarted/02-client/solution/java

# Xây dựng và chạy JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Bài tập

Trong bài tập này, bạn sẽ sử dụng những gì đã học để tạo client của riêng bạn.

Dưới đây là server bạn có thể dùng và cần gọi qua mã client của bạn, xem bạn có thể thêm tính năng mới cho server để làm nó thú vị hơn.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Tạo một máy chủ MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Thêm một công cụ cộng
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Thêm một tài nguyên chào hỏi động
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

// Bắt đầu nhận tin nhắn trên stdin và gửi tin nhắn trên stdout

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

# Tạo một máy chủ MCP
mcp = FastMCP("Demo")


# Thêm một công cụ cộng
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Thêm một tài nguyên lời chào động
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

Xem dự án này để biết cách [thêm prompt và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Ngoài ra, check link này để biết cách gọi [prompt và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Trong [phần trước](../../../../03-GettingStarted/01-first-server), bạn đã học cách tạo MCP server đơn giản bằng Rust. Bạn có thể tiếp tục phát triển hoặc tham khảo thêm các ví dụ MCP server Rust tại đây: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Giải pháp

**Thư mục giải pháp** chứa các triển khai client hoàn chỉnh, sẵn sàng chạy, minh họa tất cả các khái niệm trong tutorial. Mỗi giải pháp gồm có cả client và server, tổ chức thành dự án riêng biệt, độc lập.

### 📁 Cấu trúc thư mục giải pháp

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

### 🚀 Mỗi giải pháp bao gồm

Mỗi giải pháp ngôn ngữ cung cấp:

- **Triển khai client hoàn chỉnh** với tất cả tính năng trong tutorial
- **Cấu trúc dự án hoạt động** với phụ thuộc và cấu hình đầy đủ
- **Script build và chạy** để dễ dàng thiết lập và chạy thử
- **README chi tiết** hướng dẫn theo ngôn ngữ
- **Xử lý lỗi** và ví dụ xử lý kết quả

### 📖 Sử dụng giải pháp

1. **Đi đến thư mục ngôn ngữ bạn chọn**:

   ```bash
   cd solution/typescript/    # Dành cho TypeScript
   cd solution/java/          # Dành cho Java
   cd solution/python/        # Dành cho Python
   cd solution/dotnet/        # Dành cho .NET
   ```

2. **Theo hướng dẫn trong README từng thư mục để:**
   - Cài đặt phụ thuộc
   - Build dự án
   - Chạy client

3. **Ví dụ đầu ra bạn nên thấy:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Tài liệu đầy đủ, hướng dẫn từng bước xem tại: **[📖 Tài liệu giải pháp](./solution/README.md)**

## 🎯 Ví dụ hoàn chỉnh

Chúng tôi cung cấp các ví dụ client hoàn chỉnh hoạt động cho tất cả ngôn ngữ lập trình đã trình bày. Ví dụ minh họa đầy đủ chức năng đã nói trên, giúp bạn tham khảo hoặc dùng làm cơ sở cho dự án riêng.

### Ví dụ hoàn chỉnh có sẵn

| Ngôn ngữ | File | Mô tả |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java hoàn chỉnh dùng transport SSE với xử lý lỗi toàn diện |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# hoàn chỉnh dùng transport stdio với tự động khởi động server |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript hoàn chỉnh hỗ trợ đầy đủ giao thức MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python hoàn chỉnh dùng async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust hoàn chỉnh dùng Tokio cho xử lý bất đồng bộ |

Mỗi ví dụ hoàn chỉnh bao gồm:
- ✅ **Thiết lập kết nối** và xử lý lỗi
- ✅ **Khám phá máy chủ** (công cụ, tài nguyên, lời nhắc khi có thể)
- ✅ **Các phép toán máy tính** (cộng, trừ, nhân, chia, trợ giúp)
- ✅ **Xử lý kết quả** và định dạng đầu ra
- ✅ **Xử lý lỗi toàn diện**
- ✅ **Mã sạch, có chú thích** với các bước giải thích chi tiết

### Bắt đầu với các Ví dụ Hoàn chỉnh

1. **Chọn ngôn ngữ ưa thích của bạn** từ bảng trên
2. **Xem lại tệp ví dụ hoàn chỉnh** để hiểu toàn bộ cách triển khai
3. **Chạy ví dụ** theo hướng dẫn trong [`complete_examples.md`](./complete_examples.md)
4. **Sửa đổi và mở rộng** ví dụ cho trường hợp sử dụng cụ thể của bạn

Để có tài liệu chi tiết về cách chạy và tùy chỉnh các ví dụ này, xem: **[📖 Tài liệu Ví dụ Hoàn chỉnh](./complete_examples.md)**

### 💡 Giải pháp so với Ví dụ Hoàn chỉnh

| **Thư mục Giải pháp** | **Ví dụ Hoàn chỉnh** |
|--------------------|--------------------- |
| Cấu trúc dự án đầy đủ với các tệp xây dựng | Triển khai một tệp đơn |
| Sẵn sàng chạy với các phụ thuộc | Ví dụ mã tập trung |
| Thiết lập gần giống môi trường sản xuất | Tham khảo học tập |
| Công cụ đặc thù ngôn ngữ | So sánh đa ngôn ngữ |

Cả hai cách đều có giá trị - sử dụng **thư mục giải pháp** cho dự án hoàn chỉnh và **ví dụ hoàn chỉnh** để học và tham khảo.

## Những điểm chính cần nhớ

Những điểm chính cho chương này về client như sau:

- Có thể được dùng để khám phá và gọi các tính năng trên máy chủ.
- Có thể khởi động một máy chủ khi client tự khởi động (như trong chương này) nhưng client cũng có thể kết nối tới các máy chủ đang chạy.
- Là cách tuyệt vời để thử khả năng máy chủ bên cạnh các lựa chọn khác như Inspector như đã mô tả trong chương trước.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo tính chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc thiếu sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính xác và đáng tin cậy. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ hiểu lầm hay cách diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
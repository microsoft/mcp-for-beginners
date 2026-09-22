# Tạo một client

Client là các ứng dụng tùy chỉnh hoặc script giao tiếp trực tiếp với một MCP Server để yêu cầu tài nguyên, công cụ và các prompt. Khác với việc sử dụng công cụ inspector, vốn cung cấp giao diện đồ họa để tương tác với server, việc tự viết client cho phép tương tác chương trình hóa và tự động hóa. Điều này giúp các nhà phát triển tích hợp các khả năng của MCP vào quy trình làm việc riêng, tự động hóa công việc và xây dựng các giải pháp tùy chỉnh phù hợp với nhu cầu cụ thể.

## Tổng quan

Bài học này giới thiệu khái niệm các client trong hệ sinh thái Model Context Protocol (MCP). Bạn sẽ học cách viết client của riêng mình và kết nối nó với MCP Server.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Hiểu client có thể làm gì.
- Viết client của riêng bạn.
- Kết nối và kiểm tra client với MCP server để đảm bảo server hoạt động như mong đợi.

## Việc cần làm để viết một client là gì?

Để viết một client, bạn cần làm những bước sau:

- **Nhập khẩu các thư viện phù hợp**. Bạn sẽ dùng cùng một thư viện như trước, chỉ khác về cấu trúc sử dụng.
- **Khởi tạo một client**. Điều này bao gồm tạo một thể hiện client và kết nối nó với phương thức truyền tải được chọn.
- **Quyết định những tài nguyên nào sẽ được liệt kê**. MCP server của bạn có tài nguyên, công cụ và prompt, bạn cần quyết định những gì sẽ liệt kê.
- **Tích hợp client vào ứng dụng chủ**. Khi đã biết khả năng của server, bạn cần tích hợp nó vào ứng dụng chủ sao cho khi người dùng nhập prompt hoặc lệnh khác, tính năng tương ứng trên server được gọi.

Bây giờ chúng ta đã hiểu ở cấp độ tổng quát, hãy xem ví dụ tiếp theo.

### Ví dụ về client

Hãy xem ví dụ client dưới đây:

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

// Liệt kê các câu nhắc
const prompts = await client.listPrompts();

// Lấy một câu nhắc
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

Trong đoạn mã trên chúng ta đã:

- Nhập các thư viện
- Tạo một thể hiện client và kết nối nó sử dụng stdio làm phương thức truyền tải.
- Liệt kê prompts, tài nguyên và công cụ rồi gọi tất cả chúng.

Thế là bạn có một client có thể giao tiếp với MCP Server.

Hãy dành thời gian ở phần bài tập tiếp theo để phân tích từng đoạn mã và giải thích hoạt động.

## Bài tập: Viết một client

Như đã nói ở trên, hãy dành thời gian giải thích mã và nếu muốn bạn có thể code cùng.

### -1- Nhập khẩu các thư viện

Hãy nhập khẩu các thư viện cần thiết, chúng ta cần tham chiếu đến client và giao thức truyền tải đã chọn, stdio. stdio là giao thức dành cho các thứ chạy trên máy cục bộ của bạn. SSE là một giao thức truyền tải khác mà chúng ta sẽ trình bày ở các chương sau, đó là lựa chọn khác của bạn. Hiện tại, hãy tiếp tục với stdio.

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

Với Java, bạn sẽ tạo client kết nối đến MCP server trong bài tập trước đó. Sử dụng cấu trúc dự án Java Spring Boot đã dùng trong [Bắt đầu với MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), tạo một lớp Java mới tên `SDKClient` trong thư mục `src/main/java/com/microsoft/mcp/sample/client/` và thêm các import sau:

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

Bạn cần thêm các dependencies dưới đây vào file `Cargo.toml`.

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

Từ đó, bạn có thể nhập các thư viện cần thiết trong mã client.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Bây giờ tiến tới phần khởi tạo.

### -2- Khởi tạo client và giao thức truyền tải

Chúng ta sẽ tạo một thể hiện của giao thức truyền tải và một thể hiện client:

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

Trong đoạn code trên chúng ta đã:

- Tạo một thể hiện giao thức stdio. Lưu ý cách nó xác định lệnh và tham số để tìm và khởi động server vì đó là việc cần làm khi tạo client.

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

- Kết nối client với giao thức truyền tải đã chọn.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Tạo tham số máy chủ cho kết nối stdio
server_params = StdioServerParameters(
    command="mcp",  # Tập tin thực thi
    args=["run", "server.py"],  # Tham số dòng lệnh tùy chọn
    env=None,  # Biến môi trường tùy chọn
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

Trong đoạn mã trên chúng ta đã:

- Nhập khẩu các thư viện cần thiết
- Khởi tạo một đối tượng tham số server dùng để chạy server sao cho client có thể kết nối.
- Định nghĩa phương thức `run` gọi `stdio_client` để bắt đầu phiên client.
- Tạo một điểm vào nơi cung cấp phương thức `run` cho `asyncio.run`.

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

Trong đoạn mã trên chúng ta đã:

- Nhập các thư viện cần thiết.
- Tạo giao thức stdio và client `mcpClient`. Client này dùng để liệt kê và gọi các tính năng trên MCP Server.

Lưu ý, trong "Arguments", bạn có thể trỏ đến *.csproj* hoặc file thực thi.

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
        
        // Logic khách hàng của bạn đi đây
    }
}
```

Trong đoạn mã trên chúng ta đã:

- Tạo phương thức main thiết lập giao thức SSE trỏ đến `http://localhost:8080` nơi MCP server chạy.
- Tạo lớp client nhận giao thức truyền tải trong constructor.
- Trong phương thức `run`, tạo một client MCP đồng bộ dùng giao thức và khởi tạo kết nối.
- Dùng giao thức SSE (Server-Sent Events) thích hợp cho giao tiếp HTTP với MCP server Java Spring Boot.

#### Rust

Client Rust này giả định server là dự án anh em tên "calculator-server" trong cùng thư mục. Đoạn mã dưới đây sẽ khởi động server và kết nối tới nó.

```rust
async fn main() -> Result<(), RmcpError> {
    // Giả sử máy chủ là một dự án anh chị em có tên "calculator-server" trong cùng thư mục
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

    // TODO: Liệt kê công cụ

    // TODO: Gọi công cụ add với các đối số = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Liệt kê các tính năng của server

Bây giờ chúng ta có client có thể kết nối nếu chạy chương trình. Tuy nhiên nó chưa liệt kê các tính năng nên hãy làm điều đó tiếp theo:

#### TypeScript

```typescript
// Liệt kê lời nhắc
const prompts = await client.listPrompts();

// Liệt kê tài nguyên
const resources = await client.listResources();

// liệt kê công cụ
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

Ở đây chúng ta liệt kê tài nguyên hiện có bằng `list_resources()` và công cụ bằng `list_tools` rồi in ra.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ví dụ trên cho thấy việc liệt kê các công cụ trên server. Với mỗi công cụ ta in ra tên nó.

#### Java

```java
// Liệt kê và trình bày các công cụ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Bạn cũng có thể ping máy chủ để kiểm tra kết nối
client.ping();
```

Trong đoạn mã trên chúng ta đã:

- Gọi `listTools()` để lấy danh sách tất cả công cụ sẵn có từ MCP server.
- Dùng `ping()` để kiểm tra kết nối server có hoạt động.
- `ListToolsResult` chứa thông tin về công cụ bao gồm tên, mô tả và định dạng đầu vào.

Tốt, giờ chúng ta đã lấy được tất cả tính năng. Nhưng câu hỏi là khi nào dùng? Client này khá đơn giản, cần gọi rõ ràng các tính năng khi muốn dùng. Ở chương tiếp theo, ta sẽ tạo client nâng cao có truy cập LLM riêng của nó. Hiện giờ, hãy xem cách gọi các tính năng trên server:

#### Rust

Trong hàm main, sau khi khởi tạo client, ta khởi tạo server và liệt kê vài tính năng.

```rust
// Khởi tạo
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Liệt kê công cụ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Gọi các tính năng

Để gọi tính năng ta cần đảm bảo truyền đúng đối số và trong một số trường hợp tên tính năng cần gọi.

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

// gọi lệnh nhắc
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Trong đoạn mã trên ta đã:

- Đọc một tài nguyên, gọi `readResource()` với `uri`. Đây là cách nó có thể hiển thị trên server:

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

    Giá trị `uri` là `file://example.txt` khớp với `file://{name}` trên server. `example.txt` sẽ được gán cho `name`.

- Gọi công cụ, ta gọi bằng cách chỉ định `name` và `arguments` như sau:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Lấy prompt, gọi `getPrompt()` với `name` và `arguments`. Mã server như sau:

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

    Mã client kết quả sẽ trông như thế này để phù hợp server:

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

Trong đoạn code trên chúng ta đã:

- Gọi tài nguyên có tên `greeting` qua `read_resource`.
- Gọi công cụ `add` qua `call_tool`.

#### .NET

1. Thêm mã gọi công cụ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Để in kết quả, đoạn mã xử lý như sau:

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

Trong đoạn mã trên chúng ta đã:

- Gọi nhiều công cụ máy tính bằng phương thức `callTool()` với các đối tượng `CallToolRequest`.
- Mỗi lần gọi xác định tên công cụ và `Map` các đối số cần thiết.
- Công cụ máy chủ cần tên tham số cụ thể (như "a", "b" cho phép toán).
- Kết quả trả về dưới dạng `CallToolResult` chứa phản hồi từ server.

#### Rust

```rust
// Gọi công cụ thêm với các đối số = {"a": 3, "b": 2}
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

Để chạy client, nhập lệnh sau trong terminal:

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

Đầu tiên, đảm bảo MCP server đang chạy trên `http://localhost:8080`. Sau đó chạy client:

```bash
# Xây dựng dự án của bạn
./mvnw clean compile

# Chạy client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Ngoài ra, bạn có thể chạy dự án client hoàn chỉnh trong thư mục `03-GettingStarted\02-client\solution\java`:

```bash
# Điều hướng đến thư mục giải pháp
cd 03-GettingStarted/02-client/solution/java

# Xây dựng và chạy tệp JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Bài tập

Trong bài tập này, bạn sẽ dùng những gì đã học để tạo client của riêng bạn.

Đây là một server bạn có thể dùng gọi qua mã client, thử xem bạn có thể thêm tính năng cho server để nó thú vị hơn không.

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

// Thêm một tài nguyên lời chào động
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


# Thêm một tài nguyên chào hỏi động
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

Xem dự án này để biết cách [thêm prompts và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Cũng hãy xem liên kết này để biết cách gọi [prompts và tài nguyên](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Trong [phần trước](../../../../03-GettingStarted/01-first-server), bạn đã học cách tạo một MCP server đơn giản bằng Rust. Bạn có thể tiếp tục phát triển dựa trên đó hoặc xem liên kết này để có thêm ví dụ MCP server bằng Rust: [Ví dụ MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Giải pháp

Thư mục **solution** chứa các triển khai client hoàn chỉnh, sẵn sàng chạy minh họa tất cả các khái niệm trong hướng dẫn này. Mỗi giải pháp bao gồm cả mã client và server được tổ chức trong các dự án riêng biệt, tự chứa.

### 📁 Cấu trúc Solution

Thư mục solution được tổ chức theo ngôn ngữ lập trình:

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

Mỗi giải pháp theo ngôn ngữ cung cấp:

- **Triển khai client hoàn chỉnh** với đầy đủ tính năng từ hướng dẫn
- **Cấu trúc dự án hoạt động** với các phụ thuộc và cấu hình đúng
- **Script build và chạy** để dễ thiết lập và thực thi
- **README chi tiết** với hướng dẫn riêng theo ngôn ngữ
- **Ví dụ xử lý lỗi** và xử lý kết quả

### 📖 Sử dụng các giải pháp

1. **Đi tới thư mục ngôn ngữ mà bạn thích**:

   ```bash
   cd solution/typescript/    # Dành cho TypeScript
   cd solution/java/          # Dành cho Java
   cd solution/python/        # Dành cho Python
   cd solution/dotnet/        # Dành cho .NET
   ```

2. **Làm theo hướng dẫn README** trong mỗi thư mục để:
   - Cài đặt các phụ thuộc
   - Xây dựng dự án
   - Chạy client

3. **Kết quả mẫu** bạn sẽ thấy:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Để xem tài liệu đầy đủ và hướng dẫn chi tiết theo từng bước, xem: **[📖 Tài liệu Solution](./solution/README.md)**

## 🎯 Ví dụ hoàn chỉnh

Chúng tôi đã cung cấp các triển khai client hoàn chỉnh và hoạt động cho tất cả ngôn ngữ lập trình trong hướng dẫn này. Những ví dụ này minh họa đầy đủ chức năng như mô tả và có thể dùng làm tham chiếu hoặc điểm bắt đầu cho dự án của bạn.

### Các ví dụ hoàn chỉnh có sẵn

| Ngôn ngữ | Tệp | Mô tả |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java hoàn chỉnh dùng giao thức SSE với xử lý lỗi toàn diện |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# hoàn chỉnh dùng giao thức stdio với khởi động server tự động |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript hoàn chỉnh với hỗ trợ đầy đủ giao thức MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python hoàn chỉnh sử dụng mô hình async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust hoàn chỉnh dùng Tokio cho các hoạt động không đồng bộ |

Mỗi ví dụ hoàn chỉnh bao gồm:

- ✅ **Kết nối và xử lý lỗi**
- ✅ **Khám phá server** (công cụ, tài nguyên, prompt nếu có)
- ✅ **Các phép toán máy tính** (cộng, trừ, nhân, chia, trợ giúp)
- ✅ **Xử lý kết quả** và xuất định dạng
- ✅ **Xử lý lỗi toàn diện**

- ✅ **Mã nguồn sạch, có chú thích** với bình luận từng bước

### Bắt đầu với các Ví dụ Hoàn chỉnh

1. **Chọn ngôn ngữ ưa thích của bạn** từ bảng trên
2. **Xem lại tệp ví dụ hoàn chỉnh** để hiểu toàn bộ cách triển khai
3. **Chạy ví dụ** theo hướng dẫn trong [`complete_examples.md`](./complete_examples.md)
4. **Chỉnh sửa và mở rộng** ví dụ cho trường hợp sử dụng cụ thể của bạn

Để có tài liệu chi tiết về cách chạy và tùy chỉnh các ví dụ này, xem: **[📖 Tài liệu Ví dụ Hoàn chỉnh](./complete_examples.md)**

### 💡 Giải pháp so với Ví dụ Hoàn chỉnh

| **Thư mục Giải pháp** | **Ví dụ Hoàn chỉnh** |
|--------------------|--------------------- |
| Cấu trúc dự án đầy đủ với các tệp xây dựng | Các triển khai trong một tệp đơn |
| Sẵn sàng chạy với các phụ thuộc | Các ví dụ mã tập trung |
| Cài đặt giống môi trường sản xuất | Tham khảo mang tính giáo dục |
| Công cụ riêng cho từng ngôn ngữ | So sánh đa ngôn ngữ |

Cả hai cách tiếp cận đều có giá trị - sử dụng **thư mục giải pháp** cho các dự án đầy đủ và **ví dụ hoàn chỉnh** cho học tập và tham khảo.

## Những điểm chính cần nhớ

Các điểm chính của chương này về các client như sau:

- Có thể được dùng để khám phá và gọi các chức năng trên server.
- Có thể khởi động một server trong khi server tự khởi động (như trong chương này) nhưng client cũng có thể kết nối với các server đang chạy.
- Là cách tuyệt vời để kiểm thử khả năng của server bên cạnh các lựa chọn thay thế như Inspector như đã mô tả trong chương trước.

## Tài nguyên bổ sung

- [Xây dựng client trong MCP](https://modelcontextprotocol.io/quickstart/client)

## Mẫu ví dụ

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .NET](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)
- [Máy tính Rust](../../../../03-GettingStarted/samples/rust)

## Tiếp theo là gì

- Tiếp theo: [Tạo client với LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
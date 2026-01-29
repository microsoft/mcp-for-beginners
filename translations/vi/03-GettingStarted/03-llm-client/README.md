# Tạo một client với LLM

Cho đến nay, bạn đã thấy cách tạo một server và một client. Client đã có thể gọi server một cách rõ ràng để liệt kê các công cụ, tài nguyên và prompt của nó. Tuy nhiên, đây không phải là cách tiếp cận thực tế. Người dùng của bạn sống trong thời đại agentic và mong muốn sử dụng prompt và giao tiếp với một LLM để làm điều đó. Đối với người dùng của bạn, họ không quan tâm bạn có sử dụng MCP hay không để lưu trữ khả năng của bạn nhưng họ mong muốn sử dụng ngôn ngữ tự nhiên để tương tác. Vậy làm thế nào để giải quyết điều này? Giải pháp là thêm một LLM vào client.

## Tổng quan

Trong bài học này, chúng ta tập trung vào việc thêm một LLM vào client của bạn và cho thấy cách điều này mang lại trải nghiệm tốt hơn nhiều cho người dùng của bạn.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có thể:

- Tạo một client với một LLM.
- Tương tác liền mạch với server MCP sử dụng một LLM.
- Cung cấp trải nghiệm người dùng cuối tốt hơn ở phía client.

## Cách tiếp cận

Hãy thử hiểu cách tiếp cận mà chúng ta cần thực hiện. Thêm một LLM nghe có vẻ đơn giản, nhưng liệu chúng ta có thực sự làm điều này?

Đây là cách client sẽ tương tác với server:

1. Thiết lập kết nối với server.

1. Liệt kê các khả năng, prompt, tài nguyên và công cụ, và lưu lại schema của chúng.

1. Thêm một LLM và truyền các khả năng đã lưu và schema của chúng theo định dạng mà LLM hiểu.

1. Xử lý prompt của người dùng bằng cách truyền nó cho LLM cùng với các công cụ được client liệt kê.

Tuyệt vời, bây giờ chúng ta đã hiểu cách làm điều này ở mức cao, hãy thử làm điều đó trong bài tập dưới đây.

## Bài tập: Tạo một client với LLM

Trong bài tập này, chúng ta sẽ học cách thêm một LLM vào client của mình.

### Xác thực sử dụng GitHub Personal Access Token

Tạo một token GitHub là một quá trình đơn giản. Đây là cách bạn có thể làm:

- Vào GitHub Settings – Nhấp vào ảnh hồ sơ của bạn ở góc trên bên phải và chọn Settings.
- Điều hướng đến Developer Settings – Cuộn xuống và nhấp vào Developer Settings.
- Chọn Personal Access Tokens – Nhấp vào Fine-grained tokens rồi chọn Generate new token.
- Cấu hình Token của bạn – Thêm ghi chú để tham khảo, đặt ngày hết hạn, và chọn các phạm vi cần thiết (quyền truy cập). Trong trường hợp này, hãy chắc chắn thêm quyền Models.
- Tạo và sao chép Token – Nhấp Generate token, và đảm bảo sao chép ngay lập tức, vì bạn sẽ không thể xem lại nó.

### -1- Kết nối với server

Hãy tạo client của chúng ta trước:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Nhập zod để xác thực schema

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

Trong đoạn mã trên chúng ta đã:

- Nhập các thư viện cần thiết
- Tạo một lớp với hai thành viên, `client` và `openai` sẽ giúp chúng ta quản lý client và tương tác với LLM tương ứng.
- Cấu hình instance LLM của chúng ta để sử dụng GitHub Models bằng cách đặt `baseUrl` trỏ đến API inference.

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

Trong đoạn mã trên chúng ta đã:

- Nhập các thư viện cần thiết cho MCP
- Tạo một client

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

Trước tiên, bạn cần thêm các phụ thuộc LangChain4j vào file `pom.xml` của bạn. Thêm các phụ thuộc này để kích hoạt tích hợp MCP và hỗ trợ GitHub Models:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Sau đó tạo lớp client Java của bạn:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Cấu hình LLM để sử dụng Mô hình GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Tạo giao thức MCP để kết nối với máy chủ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Tạo khách hàng MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Trong đoạn mã trên chúng ta đã:

- **Thêm các phụ thuộc LangChain4j**: Cần thiết cho tích hợp MCP, client chính thức OpenAI, và hỗ trợ GitHub Models
- **Nhập các thư viện LangChain4j**: Cho tích hợp MCP và chức năng mô hình chat OpenAI
- **Tạo một `ChatLanguageModel`**: Được cấu hình để sử dụng GitHub Models với token GitHub của bạn
- **Thiết lập HTTP transport**: Sử dụng Server-Sent Events (SSE) để kết nối với server MCP
- **Tạo một client MCP**: Sẽ xử lý giao tiếp với server
- **Sử dụng hỗ trợ MCP tích hợp sẵn của LangChain4j**: Giúp đơn giản hóa tích hợp giữa LLM và server MCP

#### Rust

Ví dụ này giả định bạn có một server MCP dựa trên Rust đang chạy. Nếu bạn chưa có, hãy tham khảo lại bài học [01-first-server](../01-first-server/README.md) để tạo server.

Khi bạn đã có server MCP Rust, mở terminal và điều hướng đến cùng thư mục với server. Sau đó chạy lệnh sau để tạo một dự án client LLM mới:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Thêm các phụ thuộc sau vào file `Cargo.toml` của bạn:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Không có thư viện Rust chính thức cho OpenAI, tuy nhiên, crate `async-openai` là một [thư viện được cộng đồng duy trì](https://platform.openai.com/docs/libraries/rust#rust) và thường được sử dụng.

Mở file `src/main.rs` và thay thế nội dung bằng đoạn mã sau:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Tin nhắn ban đầu
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Thiết lập client OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Thiết lập client MCP
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Lấy danh sách công cụ MCP

    // TODO: Đàm thoại LLM với các cuộc gọi công cụ

    Ok(())
}
```

Đoạn mã này thiết lập một ứng dụng Rust cơ bản sẽ kết nối với server MCP và GitHub Models để tương tác với LLM.

> [!IMPORTANT]
> Hãy chắc chắn đặt biến môi trường `OPENAI_API_KEY` với token GitHub của bạn trước khi chạy ứng dụng.

Tuyệt vời, bước tiếp theo, hãy liệt kê các khả năng trên server.

### -2- Liệt kê khả năng của server

Bây giờ chúng ta sẽ kết nối với server và yêu cầu các khả năng của nó:

#### Typescript

Trong cùng lớp, thêm các phương thức sau:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // liệt kê công cụ
    const toolsResult = await this.client.listTools();
}
```

Trong đoạn mã trên chúng ta đã:

- Thêm mã để kết nối với server, `connectToServer`.
- Tạo một phương thức `run` chịu trách nhiệm xử lý luồng ứng dụng của chúng ta. Cho đến nay nó chỉ liệt kê các công cụ nhưng chúng ta sẽ thêm nhiều hơn vào nó sớm.

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
    print("Tool", tool.inputSchema["properties"])
```

Đây là những gì chúng ta đã thêm:

- Liệt kê tài nguyên và công cụ và in ra chúng. Đối với công cụ, chúng ta cũng liệt kê `inputSchema` mà chúng ta sẽ sử dụng sau.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

Trong đoạn mã trên chúng ta đã:

- Liệt kê các công cụ có sẵn trên MCP Server
- Đối với mỗi công cụ, liệt kê tên, mô tả và schema của nó. Phần sau là thứ chúng ta sẽ dùng để gọi công cụ sớm.

#### Java

```java
// Tạo một nhà cung cấp công cụ tự động phát hiện các công cụ MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Nhà cung cấp công cụ MCP tự động xử lý:
// - Liệt kê các công cụ có sẵn từ máy chủ MCP
// - Chuyển đổi các sơ đồ công cụ MCP sang định dạng LangChain4j
// - Quản lý việc thực thi công cụ và phản hồi
```

Trong đoạn mã trên chúng ta đã:

- Tạo một `McpToolProvider` tự động phát hiện và đăng ký tất cả các công cụ từ server MCP
- Bộ cung cấp công cụ xử lý chuyển đổi giữa schema công cụ MCP và định dạng công cụ của LangChain4j bên trong
- Cách tiếp cận này trừu tượng hóa quá trình liệt kê và chuyển đổi công cụ thủ công

#### Rust

Lấy công cụ từ server MCP được thực hiện bằng phương thức `list_tools`. Trong hàm `main` của bạn, sau khi thiết lập client MCP, thêm đoạn mã sau:

```rust
// Lấy danh sách công cụ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Chuyển đổi khả năng server thành công cụ LLM

Bước tiếp theo sau khi liệt kê khả năng server là chuyển đổi chúng thành định dạng mà LLM hiểu. Khi làm được điều đó, chúng ta có thể cung cấp các khả năng này như các công cụ cho LLM.

#### TypeScript

1. Thêm đoạn mã sau để chuyển đổi phản hồi từ MCP Server thành định dạng công cụ mà LLM có thể sử dụng:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Tạo một schema zod dựa trên input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Cụ thể đặt kiểu thành "function"
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    Đoạn mã trên lấy phản hồi từ MCP Server và chuyển đổi nó thành định nghĩa công cụ mà LLM có thể hiểu.

1. Tiếp theo, hãy cập nhật phương thức `run` để liệt kê khả năng server:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    Trong đoạn mã trên, chúng ta đã cập nhật phương thức `run` để duyệt qua kết quả và với mỗi mục gọi `openAiToolAdapter`.

#### Python

1. Trước tiên, hãy tạo hàm chuyển đổi sau

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    Trong hàm `convert_to_llm_tools` ở trên, chúng ta lấy phản hồi công cụ MCP và chuyển đổi nó thành định dạng mà LLM có thể hiểu.

1. Tiếp theo, hãy cập nhật mã client của chúng ta để sử dụng hàm này như sau:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Ở đây, chúng ta thêm một lời gọi đến `convert_to_llm_tool` để chuyển đổi phản hồi công cụ MCP thành thứ mà chúng ta có thể cung cấp cho LLM sau này.

#### .NET

1. Thêm mã để chuyển đổi phản hồi công cụ MCP thành thứ mà LLM có thể hiểu

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

Trong đoạn mã trên chúng ta đã:

- Tạo một hàm `ConvertFrom` nhận tên, mô tả và schema đầu vào.
- Định nghĩa chức năng tạo một FunctionDefinition được truyền vào ChatCompletionsDefinition. Phần sau là thứ mà LLM có thể hiểu.

1. Hãy xem cách cập nhật một số mã hiện có để tận dụng hàm trên:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// Tạo giao diện Bot cho tương tác ngôn ngữ tự nhiên
public interface Bot {
    String chat(String prompt);
}

// Cấu hình dịch vụ AI với các công cụ LLM và MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Trong đoạn mã trên chúng ta đã:

- Định nghĩa một interface `Bot` đơn giản cho tương tác ngôn ngữ tự nhiên
- Sử dụng `AiServices` của LangChain4j để tự động liên kết LLM với bộ cung cấp công cụ MCP
- Framework tự động xử lý chuyển đổi schema công cụ và gọi hàm phía sau
- Cách tiếp cận này loại bỏ việc chuyển đổi công cụ thủ công - LangChain4j xử lý toàn bộ sự phức tạp của việc chuyển đổi công cụ MCP sang định dạng tương thích với LLM

#### Rust

Để chuyển đổi phản hồi công cụ MCP thành định dạng mà LLM có thể hiểu, chúng ta sẽ thêm một hàm trợ giúp định dạng danh sách công cụ. Thêm đoạn mã sau vào file `main.rs` của bạn dưới hàm `main`. Hàm này sẽ được gọi khi gửi yêu cầu đến LLM:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

Tuyệt vời, chúng ta đã sẵn sàng xử lý các yêu cầu của người dùng, vậy hãy làm điều đó tiếp theo.

### -4- Xử lý yêu cầu prompt của người dùng

Trong phần mã này, chúng ta sẽ xử lý các yêu cầu của người dùng.

#### TypeScript

1. Thêm một phương thức sẽ được dùng để gọi LLM của chúng ta:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Gọi công cụ của máy chủ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Làm gì đó với kết quả
        // CẦN LÀM

        }
    }
    ```

    Trong đoạn mã trên chúng ta:

    - Thêm phương thức `callTools`.
    - Phương thức này nhận phản hồi từ LLM và kiểm tra xem công cụ nào đã được gọi, nếu có:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // gọi công cụ
        }
        ```

    - Gọi một công cụ, nếu LLM chỉ ra nó nên được gọi:

        ```typescript
        // 2. Gọi công cụ của máy chủ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Làm gì đó với kết quả
        // CẦN LÀM
        ```

1. Cập nhật phương thức `run` để bao gồm các lời gọi đến LLM và gọi `callTools`:

    ```typescript

    // 1. Tạo các tin nhắn làm đầu vào cho LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Gọi LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Duyệt qua phản hồi của LLM, với mỗi lựa chọn, kiểm tra xem nó có gọi công cụ không
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Tuyệt vời, đây là mã đầy đủ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Nhập zod để xác thực schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // có thể cần thay đổi thành url này trong tương lai: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // Tạo một schema zod dựa trên input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Cụ thể đặt kiểu thành "function"
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. Gọi công cụ của server
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Làm gì đó với kết quả
          // Cần làm
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Duyệt qua phản hồi LLM, với mỗi lựa chọn, kiểm tra xem nó có gọi công cụ không
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. Thêm một số import cần thiết để gọi LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Tiếp theo, thêm hàm sẽ gọi LLM:

    ```python
    # llm

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # Tham số tùy chọn
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    Trong đoạn mã trên chúng ta đã:

    - Truyền các hàm mà chúng ta tìm thấy trên server MCP và đã chuyển đổi cho LLM.
    - Sau đó gọi LLM với các hàm đó.
    - Tiếp theo, kiểm tra kết quả để xem hàm nào nên được gọi, nếu có.
    - Cuối cùng, truyền một mảng các hàm cần gọi.

1. Bước cuối cùng, cập nhật mã chính của chúng ta:

    ```python
    prompt = "Add 2 to 20"

    # hỏi LLM công cụ nào để sử dụng, nếu có
    functions_to_call = call_llm(prompt, functions)

    # gọi các hàm được đề xuất
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Đó là bước cuối cùng, trong đoạn mã trên chúng ta:

    - Gọi một công cụ MCP qua `call_tool` sử dụng hàm mà LLM cho rằng chúng ta nên gọi dựa trên prompt.
    - In kết quả của cuộc gọi công cụ tới MCP Server.

#### .NET

1. Đây là một số mã để thực hiện yêu cầu prompt LLM:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    Trong đoạn mã trên chúng ta đã:

    - Lấy các công cụ từ server MCP, `var tools = await GetMcpTools()`.
    - Định nghĩa prompt người dùng `userMessage`.
    - Tạo một đối tượng options chỉ định model và công cụ.
    - Thực hiện yêu cầu tới LLM.

1. Bước cuối cùng, xem liệu LLM có nghĩ chúng ta nên gọi một hàm không:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    Trong đoạn mã trên chúng ta đã:

    - Lặp qua danh sách các cuộc gọi hàm.
    - Với mỗi cuộc gọi công cụ, phân tích tên và tham số rồi gọi công cụ trên server MCP sử dụng client MCP. Cuối cùng in kết quả.

Đây là mã đầy đủ:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4o-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Thực hiện các yêu cầu ngôn ngữ tự nhiên tự động sử dụng các công cụ MCP
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

Trong đoạn mã trên chúng ta đã:

- Sử dụng prompt ngôn ngữ tự nhiên đơn giản để tương tác với các công cụ server MCP
- Framework LangChain4j tự động xử lý:
  - Chuyển đổi prompt người dùng thành các cuộc gọi công cụ khi cần
  - Gọi các công cụ MCP phù hợp dựa trên quyết định của LLM
  - Quản lý luồng hội thoại giữa LLM và server MCP
- Phương thức `bot.chat()` trả về các phản hồi ngôn ngữ tự nhiên có thể bao gồm kết quả từ việc thực thi công cụ MCP
- Cách tiếp cận này cung cấp trải nghiệm người dùng liền mạch, nơi người dùng không cần biết về triển khai MCP bên dưới

Ví dụ mã hoàn chỉnh:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

Đây là phần mà phần lớn công việc diễn ra. Chúng ta sẽ gọi LLM với prompt người dùng ban đầu, sau đó xử lý phản hồi để xem có công cụ nào cần được gọi không. Nếu có, chúng ta sẽ gọi các công cụ đó và tiếp tục hội thoại với LLM cho đến khi không còn cuộc gọi công cụ nào cần thiết và chúng ta có phản hồi cuối cùng.

Chúng ta sẽ gọi LLM nhiều lần, vì vậy hãy định nghĩa một hàm để xử lý cuộc gọi LLM. Thêm hàm sau vào file `main.rs` của bạn:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Hàm này nhận client LLM, danh sách các tin nhắn (bao gồm prompt người dùng), các công cụ từ server MCP, và gửi yêu cầu đến LLM, trả về phản hồi.
Phản hồi từ LLM sẽ chứa một mảng `choices`. Chúng ta sẽ cần xử lý kết quả để xem có bất kỳ `tool_calls` nào xuất hiện không. Điều này cho chúng ta biết LLM đang yêu cầu một công cụ cụ thể được gọi với các đối số. Thêm đoạn mã sau vào cuối tệp `main.rs` của bạn để định nghĩa một hàm xử lý phản hồi từ LLM:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // In nội dung nếu có sẵn
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Xử lý các cuộc gọi công cụ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Thêm tin nhắn trợ lý

        // Thực thi mỗi cuộc gọi công cụ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Thêm kết quả công cụ vào tin nhắn
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Tiếp tục cuộc trò chuyện với kết quả công cụ
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```

Nếu có `tool_calls`, nó sẽ trích xuất thông tin công cụ, gọi máy chủ MCP với yêu cầu công cụ, và thêm kết quả vào các tin nhắn hội thoại. Sau đó nó tiếp tục cuộc hội thoại với LLM và các tin nhắn được cập nhật với phản hồi của trợ lý và kết quả gọi công cụ.

Để trích xuất thông tin gọi công cụ mà LLM trả về cho các cuộc gọi MCP, chúng ta sẽ thêm một hàm trợ giúp khác để trích xuất mọi thứ cần thiết để thực hiện cuộc gọi. Thêm đoạn mã sau vào cuối tệp `main.rs` của bạn:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```

Với tất cả các phần đã sẵn sàng, bây giờ chúng ta có thể xử lý lời nhắc ban đầu của người dùng và gọi LLM. Cập nhật hàm `main` của bạn để bao gồm đoạn mã sau:

```rust
// Cuộc trò chuyện LLM với các cuộc gọi công cụ
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```

Điều này sẽ truy vấn LLM với lời nhắc ban đầu của người dùng yêu cầu tổng của hai số, và nó sẽ xử lý phản hồi để xử lý động các cuộc gọi công cụ.

Tuyệt vời, bạn đã làm được!

## Bài tập

Lấy mã từ bài tập và xây dựng máy chủ với nhiều công cụ hơn. Sau đó tạo một client với LLM, giống như trong bài tập, và thử nghiệm với các lời nhắc khác nhau để đảm bảo tất cả các công cụ trên máy chủ của bạn được gọi một cách động. Cách xây dựng client này giúp người dùng cuối có trải nghiệm tuyệt vời vì họ có thể sử dụng các lời nhắc thay vì các lệnh client chính xác, và không cần biết đến bất kỳ máy chủ MCP nào đang được gọi.

## Giải pháp

[Giải pháp](/03-GettingStarted/03-llm-client/solution/README.md)

## Những điểm chính cần nhớ

- Thêm LLM vào client của bạn cung cấp một cách tốt hơn để người dùng tương tác với các máy chủ MCP.
- Bạn cần chuyển đổi phản hồi từ máy chủ MCP thành thứ mà LLM có thể hiểu được.

## Mẫu

- [Máy tính Java](../samples/java/calculator/README.md)
- [Máy tính .Net](../../../../03-GettingStarted/samples/csharp)
- [Máy tính JavaScript](../samples/javascript/README.md)
- [Máy tính TypeScript](../samples/typescript/README.md)
- [Máy tính Python](../../../../03-GettingStarted/samples/python)
- [Máy tính Rust](../../../../03-GettingStarted/samples/rust)

## Tài nguyên bổ sung

## Tiếp theo

- Tiếp theo: [Sử dụng máy chủ với Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
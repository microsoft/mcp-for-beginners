# 使用 LLM 创建客户端

到目前为止，您已经了解了如何创建服务器和客户端。客户端能够显式调用服务器以列出其工具、资源和提示。然而，这种方法并不十分实用。您的用户生活在智能代理时代，他们期望使用提示并与 LLM 交流。他们并不关心您是否使用 MCP 来存储功能；他们只期望使用自然语言进行交互。那么我们该如何解决这个问题呢？解决方案是向客户端添加 LLM。

## 概览

本课程重点介绍如何向客户端添加 LLM，并展示这如何为用户提供更好的体验。

## 学习目标

本课结束时，您将能够：

- 创建一个带有 LLM 的客户端。
- 使用 LLM 无缝与 MCP 服务器交互。
- 在客户端提供更好的终端用户体验。

## 方法

让我们尝试理解需要采取的方法。添加 LLM 听起来简单，但我们究竟会如何做？

客户端将如何与服务器交互：

1. 建立与服务器的连接。

1. 列出功能、提示、资源和工具，并保存它们的架构。

1. 添加 LLM，并以 LLM 理解的格式传递保存的功能及其架构。

1. 通过将用户提示和客户端列出的工具一并传递给 LLM 来处理用户提示。

很好，现在我们对大体做法有了了解，让我们在下面的练习中尝试一下。

## 练习：创建带有 LLM 的客户端

在此练习中，我们将学习如何向客户端添加 LLM。

### 使用 GitHub 个人访问令牌进行身份验证

创建 GitHub 令牌是一个简单的过程。操作方法如下：

- 进入 GitHub 设置 – 点击右上角的个人头像，选择“设置”。
- 导航到开发者设置 – 向下滚动并点击“开发者设置”。
- 选择个人访问令牌 – 点击“细粒度令牌”，然后生成新令牌。
- 配置您的令牌 – 添加备注以作参考，设置过期日期，并选择必要的作用域（权限）。此处务必添加 Models 权限。
- 生成并复制令牌 – 点击生成令牌，务必立即复制，因为之后无法再次查看。

### -1- 连接到服务器

让我们先创建客户端：

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 导入 zod 用于模式验证

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

在前述代码中我们已经：

- 导入所需库
- 创建了一个类，包含两个成员，`client` 和 `openai`，分别帮助我们管理客户端和与 LLM 交互。
- 配置了我们的 LLM 实例，使其通过设置 `baseUrl` 指向推理 API 使用 GitHub Models。

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 创建用于 stdio 连接的服务器参数
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

在前述代码中我们已经：

- 导入了 MCP 所需的库
- 创建了客户端

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

首先，您需要将 LangChain4j 依赖项添加到您的 `pom.xml` 文件中。添加这些依赖以启用 MCP 集成和与 OpenAI 兼容的 MiniMax API：

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

设置你的 MiniMax API 密钥，以及可选的端点和模型。
`MINIMAX_MODEL_ID` 支持 `MiniMax-M3` 和 `MiniMax-M2.7`。
如果未设置 `OPENAI_BASE_URL`，则 `MINIMAX_REGION` 支持 `global_en` 和 `cn_zh`。

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

若要按区域选择端点，则省略 `OPENAI_BASE_URL`：

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

然后创建你的 Java 客户端类：

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        // 创建用于连接服务器的 MCP 传输
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // 创建 MCP 客户端
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

在前述代码中我们已经：

- **添加了 LangChain4j 依赖**：用于 MCP 集成和与 OpenAI 兼容的 MiniMax API
- **导入了 LangChain4j 库**：用于 MCP 集成和 OpenAI 聊天模型功能
- **创建一个 `ChatLanguageModel`**：配置为使用 MiniMax，带有你的 MiniMax API 密钥、端点和支持的模型 ID
- **设置 HTTP 传输**：使用服务器推送事件 (SSE) 连接 MCP 服务器
- **创建 MCP 客户端**：用于处理与服务器的通信
- **使用 LangChain4j 内置 MCP 支持**：简化了 LLM 与 MCP 服务器间的集成

#### Rust

此示例假设您已有一个基于 Rust 的 MCP 服务器在运行。如果没有，请参考 [01-first-server](../01-first-server/README.md) 课程创建服务器。

拥有 Rust MCP 服务器后，打开终端并导航到服务器所在的目录。然后运行以下命令创建一个新的 LLM 客户端项目：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

在 `Cargo.toml` 文件中添加以下依赖：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 目前没有官方的 Rust OpenAI 库，但 `async-openai` crate 是一个[社区维护的库](https://platform.openai.com/docs/libraries/rust#rust)，被广泛使用。

打开 `src/main.rs` 文件，并用以下代码替换其内容：

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
    // 初始消息
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // 设置 OpenAI 客户端
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // 设置 MCP 客户端
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

    // 待办事项：获取 MCP 工具列表

    // 待办事项：使用工具调用的大型语言模型对话

    Ok(())
}
```

这段代码设置了一个基本的 Rust 应用程序，能够连接到 MCP 服务器和 GitHub Models 以进行 LLM 交互。

> [!IMPORTANT]
> 请确保在运行应用程序前，将 `OPENAI_API_KEY` 环境变量设置为您的 GitHub 令牌。

很好，下一步让我们列出服务器的功能。

### -2- 列出服务器功能

现在我们将连接到服务器并请求其功能：

#### TypeScript

在同一类中，添加以下方法：

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // 列出工具
    const toolsResult = await this.client.listTools();
}
```

在前述代码中我们已经：

- 添加了连接到服务器的代码，`connectToServer`。
- 创建了一个负责处理应用程序流程的 `run` 方法。目前它仅列出工具，但我们很快会扩展功能。

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
    print("Tool", tool.inputSchema["properties"])
```

我们做了如下添加：

- 列出了资源和工具并打印它们。工具还列出了稍后会用到的 `inputSchema`。

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

在前述代码中我们已经：

- 列出了 MCP 服务器上的可用工具
- 对每个工具列出名称、描述及其架构。后者稍后会被用于调用工具。

#### Java

```java
// 创建一个自动发现MCP工具的工具提供者
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP工具提供者自动处理：
// - 从MCP服务器列出可用工具
// - 将MCP工具模式转换为LangChain4j格式
// - 管理工具执行和响应
```

在前述代码中我们已经：

- 创建 `McpToolProvider`，自动发现并注册 MCP 服务器上的所有工具
- 工具提供者内部处理 MCP 工具架构与 LangChain4j 工具格式的转换
- 这种方法抽象了手动列举和转换工具的过程

#### Rust

从 MCP 服务器检索工具是通过调用 `list_tools` 方法实现的。在你的 `main` 函数中，设置好 MCP 客户端后，添加以下代码：

```rust
// 获取MCP工具列表
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 将服务器功能转换为 LLM 工具

接下来在列出服务器功能之后，将其转换为 LLM 理解的格式。完成后，我们可以将这些功能作为工具提供给 LLM。

#### TypeScript

1. 添加以下代码，将 MCP 服务器的响应转换为 LLM 可使用的工具格式：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 根据 input_schema 创建一个 zod 模式
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 明确设置类型为 "function"
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

    上述代码接收 MCP 服务器的响应，并将其转换为 LLM 理解的工具定义格式。

2. 接下来我们更新 `run` 方法以列出服务器功能：

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

    在前述代码中，我们更新了 `run` 方法，遍历结果并对每个条目调用 `openAiToolAdapter`。

#### Python

1. 首先，创建如下转换函数

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

    在函数 `convert_to_llm_tools` 中，我们将 MCP 工具响应转换成 LLM 能理解的格式。

2. 接下来更新客户端代码以利用该函数：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    这里我们调用 `convert_to_llm_tool` 将 MCP 工具响应转成稍后可供 LLM 使用的格式。

#### .NET

1. 添加代码将 MCP 工具响应转换成 LLM 可理解内容

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

在前述代码中我们已经：

- 创建了 `ConvertFrom` 函数，接收名称、描述和输入架构。
- 定义功能以创建 `FunctionDefinition` 并传递给 `ChatCompletionsDefinition`，后者可被 LLM 理解。

2. 接着我们看看如何更新现有代码以利用上述函数：

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
// 创建一个用于自然语言交互的Bot接口
public interface Bot {
    String chat(String prompt);
}

// 使用LLM和MCP工具配置AI服务
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

在前述代码中我们已经：

- 定义了简单的 `Bot` 接口用于自然语言交互
- 使用 LangChain4j 的 `AiServices` 自动将 LLM 绑定到 MCP 工具提供者
- 框架自动处理工具架构转换和函数调用的后台操作
- 这种方法消除了手动转换工具的需求，LangChain4j 负责编码 MCP 工具到 LLM 兼容格式的复杂性

#### Rust

为将 MCP 工具响应转换为 LLM 可理解的格式，我们添加一个格式化工具列表的辅助函数。在 `main.rs` 文件中，在 `main` 函数下方添加以下代码。这会在向 LLM 发送请求时被调用：

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

很好，我们已准备好处理用户请求，接下来处理这部分。

### -4- 处理用户提示请求

这部分代码中，我们将处理用户请求。

#### TypeScript

1. 添加一个方法，用于调用我们的 LLM：

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. 调用服务器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用结果做一些事情
        // 待办事项

        }
    }
    ```

    在上述代码中我们：

    - 添加了 `callTools` 方法。
    - 该方法接受 LLM 返回，并检查是否有工具被调用。

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 调用工具
        }
        ```

    - 如果 LLM 指示调用工具，则调用该工具：

        ```typescript
        // 2. 调用服务器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用结果做一些事情
        // 待办事项
        ```

2. 更新 `run` 方法，添加调用 LLM 和 `callTools`：

    ```typescript

    // 1. 创建作为LLM输入的消息
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. 调用LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. 遍历LLM响应，对于每个选项，检查是否有工具调用
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

很好，完整代码如下：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 导入 zod 用于模式验证

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 未来可能需要更改为此 URL：https://models.github.ai/inference
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
          // 基于 input_schema 创建一个 zod 模式
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // 明确设置类型为 "function"
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
    
    
          // 2. 调用服务器的工具
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. 对结果进行处理
          // 待办事项
    
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. 遍历 LLM 响应，对于每个选项，检查是否有工具调用
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

1. 添加调用 LLM 所需的导入

    ```python
    # 大语言模型
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. 添加调用 LLM 的函数：

    ```python
    # 大语言模型

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
            # 可选参数
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

    在前述代码中我们：

    - 将从 MCP 服务器获取并转换的函数传递给 LLM。
    - 调用 LLM，传入这些函数。
    - 检查结果，查看是否需要调用函数。
    - 最后传入调用的函数数组。

3. 最后一步，更新主代码：

    ```python
    prompt = "Add 2 to 20"

    # 询问大型语言模型是否需要任何工具
    functions_to_call = call_llm(prompt, functions)

    # 调用建议的函数
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    这就是最后一步，我们在上述代码中：

    - 调用 MCP 工具，通过 `call_tool` 使用 LLM 基于提示认为应调用的函数。
    - 打印对 MCP 服务器的工具调用结果。

#### .NET

1. 展示用于 LLM 提示请求的代码：

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
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    在前述代码中我们：

    - 从 MCP 服务器获取工具，`var tools = await GetMcpTools()`。
    - 定义用户提示 `userMessage`。
    - 构造一个指定模型和工具的选项对象。
    - 发送请求到 LLM。

2. 最后一步，检查 LLM 是否认为需要调用函数：

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

    在前述代码中我们：

    - 遍历函数调用列表。
    - 对每个工具调用，解析名称和参数，使用 MCP 客户端调用 MCP 服务器上的工具。最后打印结果。

完整代码如下：

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

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

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

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
    Model = "gpt-4.1-mini",
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

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // 执行自动使用MCP工具的自然语言请求
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

在前述代码中我们：

- 使用简单的自然语言提示与 MCP 服务器工具交互
- LangChain4j 框架自动处理：
  - 在需要时将用户提示转换为工具调用
  - 根据信息调用适当的 MCP 工具
  - 管理 LLM 与 MCP 服务器之间的对话流程
- `bot.chat()` 方法返回自然语言响应，可能包含 MCP 工具执行结果
- 该方法为用户提供无缝体验，用户无需了解底层 MCP 实现

完整示例代码：

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust

这里是主要工作所在。我们首先用初始用户提示调用 LLM，然后处理响应查看是否需要调用任何工具。如果是，我们将调用那些工具，并继续与 LLM 交互，直到不再需要调用工具并获得最终响应。


我们将多次调用 LLM，所以让我们定义一个函数来处理 LLM 调用。将以下函数添加到你的 `main.rs` 文件中：

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

该函数接收 LLM 客户端、消息列表（包括用户提示）、来自 MCP 服务器的工具，并向 LLM 发送请求，返回响应。

LLM 的响应将包含一个 `choices` 数组。我们需要处理结果以查看是否存在任何 `tool_calls`。这让我们知道 LLM 请求调用特定工具并传递参数。将以下代码添加到你的 `main.rs` 文件底部，以定义一个处理 LLM 响应的函数：

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

    // 如果有内容则打印
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // 处理工具调用
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // 添加助手消息

        // 执行每个工具调用
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // 将工具结果添加到消息中
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // 使用工具结果继续对话
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

如果存在 `tool_calls`，则提取工具信息，使用工具请求调用 MCP 服务器，并将结果添加到对话消息中。然后继续使用 LLM 进行对话，消息内容将更新为助理的响应和工具调用结果。

为了提取 LLM 返回的用于 MCP 调用的工具调用信息，我们将添加另一个辅助函数来提取调用所需的所有内容。将以下代码添加到你的 `main.rs` 文件底部：

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

有了所有这些组件，我们现在可以处理初始用户提示并调用 LLM。更新你的 `main` 函数，包含以下代码：

```rust
// 具有工具调用的语言模型对话
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

这将使用初始用户提示查询 LLM，询问两个数字的和，并处理响应以动态处理工具调用。

太好了，你成功了！

## 任务

利用练习中的代码扩展服务器，添加更多工具。然后参考练习创建一个带 LLM 的客户端，用不同的提示测试它，确保所有服务器工具都能被动态调用。这样构建客户端意味着最终用户将获得极佳的用户体验，因为他们可以使用提示，而不是精确的客户端命令，并且对任何 MCP 服务器的调用毫不知情。

## 解决方案

[解决方案](./solution/README.md)

## 关键要点

- 为你的客户端添加 LLM，提供用户与 MCP 服务器交互的更好方式。
- 需要将 MCP 服务器响应转换为 LLM 可以理解的内容。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)
- [Rust 计算器](../../../../03-GettingStarted/samples/rust)

## 额外资源

## 接下来

- 下一步：[使用 Visual Studio Code 调用服务器](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
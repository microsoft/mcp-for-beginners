# 使用 LLM 创建客户端

到目前为止，您已经了解了如何创建服务器和客户端。客户端能够显式调用服务器以列出其工具、资源和提示。然而，这不是一种非常实用的方法。您的用户生活在智能代理时代，期望使用提示与 LLM 进行交互。他们并不关心您是否使用 MCP 来存储您的功能；他们只期望使用自然语言进行交互。那么，我们如何解决这个问题呢？解决方案是在客户端中添加一个 LLM。

## 概述

本课重点介绍如何添加 LLM 到客户端，并展示这如何为您的用户提供更好的体验。

## 学习目标

通过本课，您将能够：

- 创建带有 LLM 的客户端。
- 使用 LLM 无缝与 MCP 服务器交互。
- 在客户端提供更好的最终用户体验。

## 方法

让我们尝试理解需要采取的方法。添加 LLM 听起来很简单，但我们到底怎么做呢？

客户端将如何与服务器交互：

1. 与服务器建立连接。

1. 列出能力、提示、资源和工具，保存它们的架构。

1. 添加 LLM，并以 LLM 能理解的格式传入保存的能力及其架构。

1. 通过将用户提示和客户端列出的工具一起传入 LLM 来处理用户请求。

很好，现在我们了解了高层如何实现，让我们通过下面的练习进行尝试。

## 练习：使用 LLM 创建客户端

在本练习中，我们将学习如何向客户端添加 LLM。

### 使用 GitHub 个人访问令牌进行身份验证

创建 GitHub 令牌是一个简单的过程。您可以按以下步骤操作：

- 转到 GitHub 设置 – 点击右上角的头像，选择“设置”。
- 导航到开发者设置 – 向下滚动并点击“开发者设置”。
- 选择个人访问令牌 – 点击“细粒度令牌”，然后生成新令牌。
- 配置令牌 – 添加备注、设置到期日期，选择必要的权限（范围）。此处务必添加 Models 权限。
- 生成并复制令牌 – 点击生成令牌并务必立即复制，因为之后无法再次查看。

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

在上述代码中，我们：

- 导入了所需的库
- 创建了一个包含两个成员的类，`client` 和 `openai`，分别帮助管理客户端和与 LLM 交互。
- 配置 LLM 实例使用 GitHub Models，方法是将 `baseUrl` 设置为推理 API 地址。

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 创建用于标准输入输出连接的服务器参数
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

- 导入了 MCP 所需库
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

首先，您需要将 LangChain4j 依赖添加到您的 `pom.xml` 文件中。添加这些依赖以启用 MCP 集成和 GitHub Models 支持：

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

然后创建 Java 客户端类：

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
    
    public static void main(String[] args) throws Exception {        // 配置 LLM 使用 GitHub 模型
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // 创建 MCP 传输以连接服务器
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
}
```

在上述代码中，我们：

- **添加了 LangChain4j 依赖**：用于 MCP 集成、OpenAI 官方客户端和 GitHub Models 支持
- **导入了 LangChain4j 库**：用于 MCP 集成和 OpenAI 聊天模型功能
- **创建了一个 `ChatLanguageModel`**：配置使用 GitHub Models 和您的 GitHub 令牌
- **设置 HTTP 传输**：使用服务器发送事件 (SSE) 连接到 MCP 服务器
- **创建了 MCP 客户端**：用于处理与服务器的通信
- **利用 LangChain4j 内置的 MCP 支持**：简化了 LLM 与 MCP 服务器之间的集成

#### Rust

此示例假设您有一个 Rust 基于 MCP 的服务器在运行。如果没有，可参考[01-first-server](../01-first-server/README.md)课程来创建服务器。

拥有 Rust MCP 服务器后，打开终端并切换到服务器相同目录，然后运行以下命令创建新的 LLM 客户端项目：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

向您的 `Cargo.toml` 文件添加以下依赖：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 目前没有官方的 Rust OpenAI 库，但 `async-openai` crate 是一个[社区维护库](https://platform.openai.com/docs/libraries/rust#rust)，被广泛使用。

打开 `src/main.rs` 文件并用以下代码替换其内容：

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

    // 待办事项：使用工具调用的 LLM 对话

    Ok(())
}
```

该代码设置了一个基本的 Rust 应用，连接 MCP 服务器和 GitHub Models 进行 LLM 交互。

> [!IMPORTANT]
> 运行应用前，请确保设置环境变量 `OPENAI_API_KEY`，其值为您的 GitHub 令牌。

很好，下一步，让我们列出服务器上的能力。

### -2- 列出服务器能力

现在我们将连接服务器并请求其能力：

#### TypeScript

在同一个类中，添加以下方法：

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

在上述代码中，我们：

- 添加了连接服务器的代码，`connectToServer`。
- 创建了一个 `run` 方法，负责处理应用流程。目前它仅列出工具，但我们很快会添加更多。

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

新增功能包括：

- 列出资源和工具并打印。对于工具，我们还列出了 `inputSchema`，稍后会使用。

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

在上述代码中，我们：

- 列出了 MCP 服务器上可用的工具
- 对每个工具，列出名称、描述和其架构。后者稍后用于调用工具。

#### Java

```java
// 创建一个自动发现MCP工具的工具提供者
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP工具提供者自动处理：
// - 列出来自MCP服务器的可用工具
// - 将MCP工具架构转换为LangChain4j格式
// - 管理工具执行和响应
```

在上述代码中，我们：

- 创建了一个 `McpToolProvider`，自动发现并注册 MCP 服务器上的所有工具
- 工具提供者内部处理 MCP 工具架构和 LangChain4j 工具格式的转换
- 该方法抽象化了手动列出和转换工具的过程

#### Rust

通过 `list_tools` 方法从 MCP 服务器获取工具。在 `main` 函数中，设置 MCP 客户端后，添加以下代码：

```rust
// 获取MCP工具列表
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 将服务器能力转换为 LLM 工具

列出服务器能力后，下一步是将它们转换为 LLM 能理解的格式。完成后，我们可以将这些能力作为工具提供给 LLM。

#### TypeScript

1. 添加以下代码，将 MCP 服务器响应转换为 LLM 可用的工具格式：

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

上述代码将 MCP 服务器的响应转换为 LLM 能理解的工具定义格式。

1. 接下来更新 `run` 方法，列出服务器能力：

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

前述代码中，我们更新了 `run` 方法，遍历结果并对每条调用 `openAiToolAdapter`。

#### Python

1. 首先，创建以下转换函数：

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

函数 `convert_to_llm_tools` 接收 MCP 工具响应，并转换为 LLM 能理解的格式。

1. 接着更新客户端代码，使用该函数：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

此处，我们调用 `convert_to_llm_tool` 将 MCP 工具响应转换为后续传入 LLM 的格式。

#### .NET

1. 添加代码将 MCP 工具响应转换为 LLM 可理解格式：

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

在上述代码中，我们：

- 创建了函数 `ConvertFrom`，接受名称、描述和输入架构。
- 定义功能生成 `FunctionDefinition`，传入 `ChatCompletionsDefinition`，后者为 LLM 可识别格式。

1. 接着更新一些现有代码以利用该函数：

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
// 创建一个用于自然语言交互的机器人接口
public interface Bot {
    String chat(String prompt);
}

// 使用LLM和MCP工具配置AI服务
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

在上述代码中，我们：

- 定义了一个简单的 `Bot` 接口用于自然语言交互
- 使用 LangChain4j 的 `AiServices` 自动将 LLM 与 MCP 工具提供者绑定
- 框架自动处理工具架构转换和函数调用
- 该方法免去了手动转换工具的步骤——LangChain4j 负责将 MCP 工具转换为 LLM 兼容格式的所有复杂工作

#### Rust

为了将 MCP 工具响应转换为 LLM 能理解格式，我们添加一个辅助函数格式化工具列表。将以下代码添加到 `main.rs` 中 `main` 函数下面，调用 LLM 时会用到：

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

很好，现在我们已经做好处理用户请求的准备，接下来处理用户提示。

### -4- 处理用户提示请求

此部分代码将处理用户请求。

#### TypeScript

1. 添加一个方法用于调用 LLM：

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

        // 3. 对结果进行处理
        // 待办事项

        }
    }
    ```

上述代码中，我们：

- 新增方法 `callTools`。
- 该方法接收 LLM 响应，检查是否调用了工具：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 调用工具
        }
        ```

- 如果 LLM 指示调用，调用对应工具：

        ```typescript
        // 2. 调用服务器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 对结果做某些操作
        // 待办事项
        ```

1. 更新 `run` 方法，增加对 LLM 的调用和 `callTools` 调用：

    ```typescript

    // 1. 创建作为大型语言模型输入的消息
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. 调用大型语言模型
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. 遍历大型语言模型的响应，对于每个选项，检查是否有工具调用
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

好，完整代码如下：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 导入 zod 进行模式验证

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 将来可能需要更改为此网址：https://models.github.ai/inference
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
          // 根据 input_schema 创建 zod 模式
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // 显式设置类型为“function”
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
    
          // 3. 处理结果
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
    
        // 1. 遍历 LLM 响应，对于每个选项，检查是否有工具调用
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

1. 添加必要的导入以调用 LLM：

    ```python
    # 大型语言模型
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. 再添加调用 LLM 的函数：

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

上述代码中，我们：

- 将转换后 MCP 服务器上的函数传给 LLM。
- 调用 LLM 并传入这些函数。
- 检查结果判断是否需要调用函数。
- 最后传入需要调用的函数数组。

1. 最后，更新主代码：

    ```python
    prompt = "Add 2 to 20"

    # 询问大型语言模型是否需要使用任何工具
    functions_to_call = call_llm(prompt, functions)

    # 调用建议的函数
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

此代码中，我们：

- 通过 `call_tool` 调用 MCP 工具，该函数调用由 LLM 基于提示决定。
- 打印工具调用返回的结果。

#### .NET

1. 展示执行 LLM 提示请求的代码：

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

上述代码中，我们：

- 从 MCP 服务器获取工具，`var tools = await GetMcpTools()`。
- 定义用户提示 `userMessage`。
- 构建包含模型和工具的选项对象。
- 向 LLM 发出请求。

1. 最后，检查 LLM 是否建议调用函数：

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

上述代码中，我们：

- 遍历函数调用列表。
- 对每个工具调用，解析名称和参数，使用 MCP 客户端调用相应工具，最后打印结果。

以下为完整代码：

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

// 5. Print the generic response
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

上述代码中，我们：

- 用简单自然语言提示与 MCP 服务器上的工具交互
- LangChain4j 框架自动处理：
  - 根据需要将用户提示转换为工具调用
  - 根据 LLM 决策调用相应 MCP 工具
  - 管理 LLM 与 MCP 服务器的对话流程
- `bot.chat()` 方法返回自然语言响应，可能包含 MCP 工具执行结果
- 该方法提供无缝用户体验，用户无需了解底层 MCP 实现

完整代码示例：

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

这里是大部分工作的核心。我们将用初始用户提示调用 LLM，然后处理响应检查是否需要调用工具。如果需要，调用相应工具，并继续与 LLM 对话，直到不再需要调用工具，得到最终响应。

我们将多次调用 LLM，因此定义一个函数处理 LLM 调用。将以下函数添加至 `main.rs` 文件：

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

该函数接收 LLM 客户端、消息列表（包括用户提示）、来自 MCP 服务器的工具，发送请求给 LLM 并返回响应。
LLM 的响应将包含一个 `choices` 数组。我们需要处理结果以查看是否存在任何 `tool_calls`。这让我们知道 LLM 正在请求调用带有参数的特定工具。在你的 `main.rs` 文件底部添加以下代码，以定义一个处理 LLM 响应的函数：

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


如果存在 `tool_calls`，它将提取工具信息，使用工具请求调用 MCP 服务器，并将结果添加到会话消息中。然后它继续与 LLM 对话，并用助理的响应和工具调用结果更新消息。

为了提取 LLM 返回的用于 MCP 调用的工具调用信息，我们将添加另一个帮助函数来提取执行调用所需的所有内容。在你的 `main.rs` 文件底部添加以下代码：

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


所有部分就绪后，我们现在可以处理初始用户提示并调用 LLM。更新你的 `main` 函数以包含以下代码：

```rust
// 使用工具调用的LLM对话
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

将练习中的代码扩展，构建一个包含更多工具的服务器。然后创建一个带有 LLM 的客户端，就像练习中一样，使用不同的提示进行测试，确保你的服务器工具都能动态调用。这样构建客户端意味着最终用户将获得很好的用户体验，因为他们能够使用提示，而不是精确的客户端命令，并且不会察觉任何 MCP 服务器被调用。

## 解决方案

[解决方案](./solution/README.md)

## 关键要点

- 向客户端添加 LLM，能为用户提供更好的与 MCP 服务器交互的方式。
- 你需要将 MCP 服务器的响应转换为 LLM 能理解的内容。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)
- [Rust 计算器](../../../../03-GettingStarted/samples/rust)

## 附加资源

## 后续内容

- 后续：[使用 Visual Studio Code 访问服务器](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
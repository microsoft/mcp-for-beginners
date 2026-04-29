# 使用 LLM 建立用戶端

迄今為止，您已經了解如何建立伺服器和用戶端。用戶端能夠明確調用伺服器來列出其工具、資源和提示。然而，這並不是一個非常實用的方法。您的使用者處於代理時代，期望使用提示語並與 LLM 進行交流。他們不關心您是否使用 MCP 來儲存您的功能；他們只是期望使用自然語言來互動。那麼，我們如何解決這個問題？解決方案是向用戶端添加 LLM。

## 概覽

本課程專注於向您的用戶端添加 LLM，並展示這如何為您的使用者提供更好的體驗。

## 學習目標

完成本課程後，您將能夠：

- 建立帶有 LLM 的用戶端。
- 使用 LLM 無縫地與 MCP 伺服器互動。
- 提供更好的用戶端最終使用者體驗。

## 方法

讓我們嘗試了解我們需要採取的方法。添加 LLM 聽起來很簡單，但我們真的會這麼做嗎？

以下是用戶端與伺服器互動的方式：

1. 建立與伺服器的連接。

1. 列出功能、提示、資源和工具，並保存它們的結構。

1. 添加 LLM，並以 LLM 能理解的格式傳遞已保存的功能及其結構。

1. 處理使用者提示，將其與用戶端列出的工具一起傳遞給 LLM。

很好，現在我們了解了高階方式，讓我們嘗試在下面的練習中實作。

## 練習：使用 LLM 建立用戶端

在本練習中，我們將學習如何向用戶端添加 LLM。

### 使用 GitHub 個人存取權杖認證

建立 GitHub 權杖是一個簡單的過程。操作方式如下：

- 前往 GitHub 設定 – 點擊右上角的頭像並選擇「Settings」。
- 進入開發者設定 – 向下滾動並點選「Developer Settings」。
- 選擇個人存取權杖 – 點選「Fine-grained tokens」然後點「Generate new token」。
- 配置您的權杖 – 添加一個備註作為參考，設定過期日期，並選擇必要的範圍（權限）。這裡務必添加 Models 權限。
- 產生並複製權杖 – 點擊「Generate token」，並務必立即複製，因為之後將無法再次看到。

### -1- 連接到伺服器

讓我們先建立用戶端：

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 匯入 zod 用於結構驗證

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

在上述程式碼中我們：

- 導入所需的函式庫
- 建立一個包含兩個成員的類別，`client` 和 `openai`，分別幫助我們管理用戶端並與 LLM 互動。
- 配置 LLM 實例使用 GitHub Models，將 `baseUrl` 設為指向推理 API。

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 為 stdio 連接創建伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 選用的命令列參數
    env=None,  # 選用的環境變數
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

在上述程式碼中我們：

- 導入 MCP 所需的函式庫
- 建立一個用戶端

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

首先，您需要將 LangChain4j 的依賴項新增至您的 `pom.xml` 文件。加入這些依賴以啟用 MCP 集成和 GitHub Models 支援：

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

接著建立您的 Java 用戶端類別：

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
    
    public static void main(String[] args) throws Exception {        // 配置大型語言模型以使用 GitHub 模型
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // 創建 MCP 傳輸以連接伺服器
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // 創建 MCP 用戶端
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

在上述程式碼中我們：

- **新增 LangChain4j 依賴**：MCP 集成、OpenAI 官方用戶端和 GitHub Models 支援所需
- **導入 LangChain4j 函式庫**：用於 MCP 集成及 OpenAI 聊天模型功能
- **建立 `ChatLanguageModel`**：配置以使用 GitHub Models，需提供您的 GitHub 權杖
- **設定 HTTP 傳輸**：使用 Server-Sent Events (SSE) 連接 MCP 伺服器
- **建立 MCP 用戶端**：用於和伺服器通訊
- **使用 LangChain4j 內建的 MCP 支援**：簡化 LLM 與 MCP 伺服器間的整合

#### Rust

本範例假設您已有一個基於 Rust 的 MCP 伺服器在運行。如果沒有，請參考 [01-first-server](../01-first-server/README.md) 課程建立伺服器。

當您擁有 Rust MCP 伺服器後，打開終端機，定位到伺服器目錄，然後執行以下指令建立新的 LLM 用戶端專案：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

將以下依賴新增到您的 `Cargo.toml` 檔案中：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 目前沒有 OpenAI 的官方 Rust 函式庫，但 `async-openai` 欄位是一個由社群維護的函式庫，廣泛使用，詳見 [社群維護庫](https://platform.openai.com/docs/libraries/rust#rust)。

打開 `src/main.rs` 檔案，將內容替換為以下程式碼：

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
    // 初始訊息
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // 設定 OpenAI 用戶端
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // 設定 MCP 用戶端
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

    // 待辦事項：取得 MCP 工具清單

    // 待辦事項：使用工具呼叫進行大型語言模型對話

    Ok(())
}
```

此程式碼設定了一個基本的 Rust 應用程式，將會連接 MCP 伺服器與 GitHub Models 來進行 LLM 互動。

> [!IMPORTANT]
> 執行應用程式前，請務必將 `OPENAI_API_KEY` 環境變數設定為您的 GitHub 權杖。

很好，接下來讓我們列出伺服器的功能。

### -2- 列出伺服器功能

現在我們將連接伺服器並取得其功能：

#### Typescript

在同一個類別中，加入以下方法：

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

在上述程式碼中我們：

- 新增了用於連接伺服器的程式碼 `connectToServer`。
- 建立 `run` 方法，負責處理應用流程。目前它僅列出工具，稍後我們會增加功能。

#### Python

```python
# 列出可用資源
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

我們新增了：

- 列出資源與工具並印出。對於工具，我們也列出了 `inputSchema`，稍後會使用。

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

在上述程式碼中我們：

- 列出 MCP 伺服器上可用的工具
- 對每個工具，列出名稱、描述及其結構。結構是我們稍後用來呼叫工具的重要部分。

#### Java

```java
// 建立一個自動發現 MCP 工具的工具提供者
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP 工具提供者自動處理：
// - 從 MCP 伺服器列出可用的工具
// - 將 MCP 工具架構轉換為 LangChain4j 格式
// - 管理工具執行與回應
```

在上述程式碼中我們：

- 建立一個 `McpToolProvider`，自動發現並註冊 MCP 伺服器的所有工具
- 工具提供者在內部處理 MCP 工具結構與 LangChain4j 工具格式之間的轉換
- 這種方式抽象化了手動列出和轉換工具的過程

#### Rust

從 MCP 伺服器檢索工具透過 `list_tools` 方法完成。在 `main` 函式中設定 MCP 用戶端後，加入以下程式碼：

```rust
// 取得 MCP 工具清單
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 將伺服器功能轉換成 LLM 工具

列出伺服器功能後的下一步是將它們轉換成 LLM 能理解的格式。完成後，我們就可以將這些功能以工具的形式提供給 LLM。

#### TypeScript

1. 新增以下程式碼，將 MCP 伺服器回應轉成 LLM 可以使用的工具格式：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 根據 input_schema 建立 zod 架構
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 明確設定類型為 "function"
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

    上述程式碼將 MCP 伺服器的回應轉換為 LLM 可理解的工具定義格式。

1. 接著更新 `run` 方法來列出伺服器功能：

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

    在先前程式碼中，我們更新了 `run` 方法，針對結果的每一筆資料調用 `openAiToolAdapter`。

#### Python

1. 首先，建立以下轉換函式

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

    在函式 `convert_to_llm_tools` 中，我們將 MCP 工具回應轉換成 LLM 可理解的格式。

1. 接著，更新您的用戶端代碼以利用此函式，如下：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    這裡，我們加入對 `convert_to_llm_tool` 的呼叫，將 MCP 工具回應轉換成稍後能給 LLM 的格式。

#### .NET

1. 新增程式碼將 MCP 工具回應轉換為 LLM 可理解的格式

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

在上述程式碼中我們：

- 建立 `ConvertFrom` 函式接受名稱、描述和輸入結構
- 定義功能以建立 `FunctionDefinition`，並將其傳遞給 `ChatCompletionsDefinition`，後者是 LLM 可理解的形式

1. 接著，我們如何更新現有程式碼以利用上面函式：

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
// 建立用於自然語言互動的機器人介面
public interface Bot {
    String chat(String prompt);
}

// 使用LLM和MCP工具配置AI服務
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

在上述程式碼中我們：

- 定義簡單的 `Bot` 介面，用於自然語言交互
- 使用 LangChain4j 的 `AiServices` 自動將 LLM 與 MCP 工具提供者綁定
- 框架自動處理工具結構轉換和函式呼叫
- 免去手動轉換工具的繁瑣，LangChain4j 處理了 MCP 工具轉換成 LLM 兼容格式的全部複雜性

#### Rust

為了將 MCP 工具回應轉成 LLM 能理解的格式，我們將新增一個輔助函式來格式化工具列表。在您的 `main.rs` 檔案中，於 `main` 函式下方新增以下程式碼。當呼叫 LLM 時會使用此函式：

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

很好，我們已經設定好處理使用者需求，接著來處理。

### -4- 處理使用者提示請求

這部分程式碼將負責處理使用者需求。

#### TypeScript

1. 新增呼叫 LLM 的方法：

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. 呼叫伺服器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用結果進行處理
        // 待辦事項

        }
    }
    ```

    前述程式碼我們：

    - 新增 `callTools` 方法。
    - 該方法接收 LLM 回應，檢查是否有應呼叫的工具：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 呼叫工具
        }
        ```

    - 如果 LLM 指示呼叫工具，則執行：

        ```typescript
        // 2. 呼叫伺服器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用結果做一些事情
        // 待辦事項
        ```

1. 更新 `run` 方法，加入呼叫 LLM 及呼叫 `callTools`：

    ```typescript

    // 1. 創建作為 LLM 輸入的訊息
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. 呼叫 LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. 檢查 LLM 回應中每個選項是否含有工具呼叫
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

很好，我們列出完整程式碼：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 匯入 zod 以進行結構驗證

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 未來可能需要更改為這個網址：https://models.github.ai/inference
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
          // 根據 input_schema 建立 zod 結構
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // 明確設定類型為 "function"
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
    
    
          // 2. 呼叫伺服器的工具
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. 對結果進行處理
          // 待辦事項
    
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
    
        // 1. 遍歷 LLM 回應，對每個選項檢查是否有工具呼叫
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

1. 加入呼叫 LLM 所需的匯入：

    ```python
    # 大型語言模型
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. 接著，新增呼叫 LLM 的函式：

    ```python
    # 大型語言模型

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
            # 選填參數
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

    在上述程式碼中，我們：

    - 傳遞從 MCP 伺服器找到並轉換的函式給 LLM。
    - 呼叫 LLM 並帶入這些函式。
    - 檢查結果判斷是否有應呼叫的函式。
    - 最後傳送一組要呼叫的函式陣列。

1. 最後一步，更新主程式：

    ```python
    prompt = "Add 2 to 20"

    # 詢問大型語言模型是否需要使用任何工具，以及使用哪些工具
    functions_to_call = call_llm(prompt, functions)

    # 呼叫建議的函式
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    以上是最後步驟，在上述程式碼中我們：

    - 使用 `call_tool` 呼叫 MCP 工具，選用 LLM 基於提示建議呼叫的函式。
    - 印出呼叫 MCP 工具的結果。

#### .NET

1. 展示用於 LLM 提示請求的程式碼：

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

    在上述程式碼中我們：

    - 從 MCP 伺服器取得工具，`var tools = await GetMcpTools()`。
    - 定義使用者提示 `userMessage`。
    - 建立指定模型與工具的選項物件。
    - 向 LLM 發出請求。

1. 最後一步，檢查是否需要呼叫函式：

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

    在上述程式碼中我們：

    - 遍歷函式呼叫清單。
    - 解析每個工具呼叫的名稱與參數，並使用 MCP 用戶端呼叫工具，最後印出結果。

完整程式碼如下：

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
    // 執行自動使用 MCP 工具的自然語言請求
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

在上述程式碼中我們：

- 使用簡單的自然語言提示與 MCP 伺服器工具交流
- LangChain4j 框架自動處理：
  - 在需要時將使用者提示轉換為工具呼叫
  - 根據 LLM 決策呼叫適當的 MCP 工具
  - 管理 LLM 與 MCP 伺服器間的對話流程
- `bot.chat()` 方法返回可能包含 MCP 工具執行結果的自然語言回應
- 此方式提供流暢的用戶體驗，使用者無須知道底層 MCP 實作細節

完整程式碼範例：

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

這裡完成大部分工作。我們會對 LLM 發出初始使用者提示，然後依據回應判斷是否需要呼叫工具。如果需要，我們會呼叫工具，並繼續與 LLM 對話直到不需再呼叫工具且得到最終回應。

為多次呼叫 LLM，我們定義一個函式負責處理 LLM 呼叫。請將以下程式碼新增到您的 `main.rs` 檔案：

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

此函式接收 LLM 用戶端、訊息列表（含使用者提示）、MCP 伺服器的工具，發送請求給 LLM 並回傳回應。
LLM 的回應將包含一個 `choices` 陣列。我們需要處理結果以查看是否有任何 `tool_calls`。這讓我們知道 LLM 正在請求調用具有參數的特定工具。將以下程式碼新增到你的 `main.rs` 檔案底部，以定義一個用於處理 LLM 回應的函式：

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

    // 如果有內容則列印
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // 處理工具呼叫
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // 新增助理訊息

        // 執行每個工具呼叫
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // 將工具結果加入訊息
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // 使用工具結果繼續對話
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

如果存在 `tool_calls`，它會擷取工具資訊，使用工具請求呼叫 MCP 伺服器，並將結果新增到對話訊息中。然後它繼續與 LLM 的對話，並用助理的回應和工具呼叫結果更新訊息。

為了擷取 LLM 回傳給 MCP 呼叫的工具呼叫資訊，我們將新增另一個輔助函式來擷取進行呼叫所需的一切。將以下程式碼新增到你的 `main.rs` 檔案底部：

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

完成所有組件後，我們現在可以處理初始使用者提示並呼叫 LLM。更新你的 `main` 函式以包含以下程式碼：

```rust
// 與工具呼叫的大型語言模型對話
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

這將以初始使用者提示查詢 LLM，要求計算兩個數字的總和，並處理回應以動態處理工具呼叫。

太好了，你完成了！

## 作業

從練習中取用程式碼並擴充伺服器，增加更多工具。接著建立一個像練習中那樣帶有 LLM 的用戶端，並使用不同提示測試它，以確保所有伺服器工具都能動態呼叫。用這種方式建立客戶端意味著最終使用者將有絕佳的使用體驗，因為他們能使用提示，而不是精確的客戶端指令，且對任何 MCP 伺服器的呼叫全然不知。

## 解答

[解答](./solution/README.md)

## 重要重點

- 在客戶端加入 LLM 提供使用者更好的方式與 MCP 伺服器互動。
- 你需要將 MCP 伺服器回應轉換為 LLM 可以理解的資料格式。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 額外資源

## 下一步

- 下一步：[使用 Visual Studio Code 消費伺服器](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的原文版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯所產生的任何誤解或誤用負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
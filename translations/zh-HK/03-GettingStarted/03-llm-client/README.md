# 使用 LLM 創建一個客戶端

到目前為止，你已經看到如何創建一個服務器和一個客戶端。客戶端能夠明確調用服務器來列出它的工具、資源和提示。然而，這並不是一個很實用的方法。你的用戶生活在智能代理時代，他們期望使用提示詞並與 LLM 交流。他們不關心你是否使用 MCP 來存儲你的能力；他們只期望以自然語言互動。那麼，我們如何解決這個問題？解決方案是將 LLM 添加到客戶端中。

## 概覽

在本課中，我們將重點放在向你的客戶端添加 LLM，並展示這如何為你的用戶提供更好的體驗。

## 學習目標

完成本課後，你將能夠：

- 創建帶有 LLM 的客戶端。
- 使用 LLM 無縫地與 MCP 服務器互動。
- 在客戶端提供更好的最終用戶體驗。

## 方法

讓我們嘗試理解我們需要採取的方法。添加 LLM 聽起來很簡單，但我們真的會這麼做嗎？

以下是客戶端與服務器的互動方式：

1. 與服務器建立連接。

1. 列出能力、提示詞、資源和工具，並保存其結構。

1. 添加一個 LLM，並以 LLM 理解的格式傳入保存的能力及其結構。

1. 通過將用戶提示詞與客戶端列出的工具一起傳遞給 LLM，處理使用者的提示詞。

很好，現在我們在高層次上理解了如何執行，讓我們在以下練習中嘗試這個方法。

## 練習：使用 LLM 創建客戶端

在本練習中，我們將學習如何向客戶端添加 LLM。

### 使用 GitHub 個人訪問令牌進行身份驗證

創建 GitHub 令牌是一個簡單的過程。以下是操作方法：

- 前往 GitHub 設置 – 點擊右上角的個人頭像並選擇「設定」。
- 進入開發者設定 – 向下滾動並點擊「Developer Settings」。
- 選擇個人訪問令牌 – 點擊「Fine-grained tokens」然後點擊「Generate new token」。
- 配置你的令牌 – 添加備註便於識別，設定過期日期，並選擇必要的範圍（權限）。在此案例中，確保添加了 Models 權限。
- 生成並複製令牌 – 點擊「Generate token」，確保立即複製，因為你之後將無法再次查看。

### -1- 連接至伺服器

讓我們先建立客戶端：

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 導入 zod 作為架構驗證

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

在上述代碼中，我們：

- 導入了所需的庫。
- 創建了一個包含兩個成員的類，`client` 和 `openai` 用於幫助管理客戶端並與 LLM 互動。
- 配置了 LLM 實例，通過設置 `baseUrl` 指向推理 API 以使用 GitHub 模型。

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 為 stdio 連線建立伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行檔
    args=["run", "server.py"],  # 可選的命令行參數
    env=None,  # 可選的環境變數
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 初始化連線
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

在上述代碼中，我們：

- 導入了 MCP 所需的庫。
- 創建了一個客戶端。

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

首先，你需要將 LangChain4j 的依賴添加到你的 `pom.xml` 文件中。添加這些依賴以啟用 MCP 集成和 GitHub 模型支持：

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

然後創建你的 Java 客戶端類：

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

        // 創建 MCP 傳輸以連接服務器
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // 創建 MCP 客戶端
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

在上述代碼中，我們：

- **添加了 LangChain4j 依賴**：這是 MCP 集成、OpenAI 官方客戶端和 GitHub 模型支持所必需的。
- **導入了 LangChain4j 庫**：用於 MCP 集成和 OpenAI 聊天模型功能。
- **創建了一個 `ChatLanguageModel`**：配置為使用帶有你的 GitHub 令牌的 GitHub 模型。
- **設置了 HTTP 傳輸**：使用服務端事件（SSE）連接至 MCP 服務器。
- **創建了一個 MCP 客戶端**：將負責與服務器通信。
- **使用了 LangChain4j 內建的 MCP 支持**：簡化了 LLM 與 MCP 服務器間的集成。

#### Rust

本範例假設你已有基於 Rust 的 MCP 服務器運行。如果沒有，請參考 [01-first-server](../01-first-server/README.md) 課程來創建服務器。

獲得 Rust MCP 服務器後，打開終端並切換至該服務器所在目錄，然後執行以下命令來創建一個新的 LLM 客戶端項目：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

在你的 `Cargo.toml` 文件中添加以下依賴：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 目前沒有官方的 Rust OpenAI 庫，但 `async-openai` Crate 是一個 [社群維護的庫](https://platform.openai.com/docs/libraries/rust#rust)，廣泛使用。

打開 `src/main.rs` 文件，並用以下程式碼替換其內容：

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

    // 設定 OpenAI 客戶端
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // 設定 MCP 客戶端
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

    // 待辦事項：獲取 MCP 工具列表

    // 待辦事項：使用工具調用的大型語言模型對話

    Ok(())
}
```

此代碼設置了一個基本的 Rust 應用，將連接 MCP 服務器和 GitHub 模型以進行 LLM 互動。

> [!IMPORTANT]
> 請確保在運行應用前，將你的 GitHub 令牌設定為環境變數 `OPENAI_API_KEY`。

很好，下一步讓我們列出服務器的能力。

### -2- 列出服務器能力

現在我們將連接至服務器並詢問其能力：

#### TypeScript

在同一類中，添加以下方法：

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

在上述代碼中，我們：

- 添加了用於連接服務器的代碼 `connectToServer`。
- 創建了一個負責處理應用流程的 `run` 方法。目前只列出了工具，但我們稍後會添加更多內容。

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

以下是我們添加的內容：

- 列出資源和工具並打印出來。對於工具，我們還列出 `inputSchema`，稍後會用到。

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

在上述代碼中，我們：

- 列出了 MCP 服務器上的工具。
- 對每個工具列出了名稱、描述和其結構。後者將用於稍後調用工具。

#### Java

```java
// 創建一個自動發現 MCP 工具的工具供應者
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP 工具供應者自動處理：
// - 從 MCP 伺服器列出可用工具
// - 將 MCP 工具結構轉換為 LangChain4j 格式
// - 管理工具執行及回應
```

在上述代碼中，我們：

- 創建了 `McpToolProvider`，自動從 MCP 服務器發現並註冊所有工具。
- 工具提供者內部處理 MCP 工具結構與 LangChain4j 工具格式的轉換。
- 該方法抽象掉了手動的工具列出和轉換過程。

#### Rust

從 MCP 服務器檢索工具是使用 `list_tools` 方法。在你的 `main` 函式中，設置好 MCP 客戶端後，添加以下代碼：

```rust
// 獲取 MCP 工具清單
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 將服務器能力轉換為 LLM 工具

列出服務器能力後的下一步是將它們轉換成 LLM 能夠理解的格式。一旦完成，我們就可以將這些能力作為工具提供給 LLM。

#### TypeScript

1. 添加以下代碼將 MCP 服務器的響應轉換為 LLM 可用的工具格式：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 根據 input_schema 創建一個 zod 結構
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

以上代碼將從 MCP 服務器的響應轉換為 LLM 能理解的工具定義格式。

1. 接著，讓我們更新 `run` 方法以列出服務器能力：

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

在上述代碼中，我們更新了 `run` 方法，遍歷結果並對每個條目呼叫 `openAiToolAdapter`。

#### Python

1. 首先，我們創建以下轉換器函數：

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

在上述函數 `convert_to_llm_tools` 中，我們接收 MCP 工具響應並將其轉換為 LLM 能夠理解的格式。

1. 接著，讓我們更新客戶端代碼來使用此函數，如下所示：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

在這裡，我們增加了調用 `convert_to_llm_tool` 的程式碼，用於將 MCP 工具響應轉換成稍後將輸入至 LLM 的資料。

#### .NET

1. 現在加入用於將 MCP 工具響應轉換為 LLM 可理解格式的代碼：

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

在上述代碼中，我們：

- 創建了一個函數 `ConvertFrom`，接收名稱、描述和輸入結構。
- 定義功能以創建一個 `FunctionDefinition`，該定義會被傳遞到 `ChatCompletionsDefinition`。後者是 LLM 可理解的格式。

1. 接下來，讓我們看看如何更新現有代碼以利用上述函數：

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
// 建立一個用於自然語言互動的機械人界面
public interface Bot {
    String chat(String prompt);
}

// 使用LLM和MCP工具配置人工智能服務
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

在上述代碼中，我們：

- 定義了一個簡單的 `Bot` 介面用於自然語言互動。
- 使用 LangChain4j 的 `AiServices` 自動將 LLM 與 MCP 工具提供者綁定。
- 框架自動處理工具結構轉換和函數調用細節。
- 這種方法消除了手動工具轉換的需要——LangChain4j 處理所有將 MCP 工具轉換為 LLM 相容格式的複雜性。

#### Rust

為了將 MCP 工具響應轉換為 LLM 可理解的格式，我們將添加一個幫助函數來格式化工具列表。在你的 `main.rs` 文件中 `main` 函式下方添加以下代碼。此函數將在向 LLM 發送請求時呼叫：

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

很好，我們已準備好處理使用者請求，接下來讓我們開始著手。

### -4- 處理用戶提示請求

這部分代碼將處理用戶請求。

#### TypeScript

1. 添加一個用於調用 LLM 的方法：

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

        // 3. 使用結果進行某些操作
        // 待辦事項

        }
    }
    ```

在上述代碼中，我們：

- 新增了一個名為 `callTools` 的方法。
- 該方法接受一個 LLM 響應並檢查是否有工具被呼叫（如果有）：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 調用工具
        }
        ```

- 如 LLM 指示，呼叫相應的工具：

        ```typescript
        // 2. 呼叫伺服器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用結果做些事情
        // 待辦事項
        ```

1. 更新 `run` 方法，新增對 LLM 的呼叫及調用 `callTools`：

    ```typescript

    // 1. 建立作為 LLM 輸入的訊息
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. 調用 LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. 遍歷 LLM 的回應，對每個選項檢查是否有工具調用
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

很好，讓我們完整列出代碼：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 導入 zod 作為結構驗證工具

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 將來可能需要更改為此網址：https://models.github.ai/inference
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
    
          // 3. 處理結果
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
    
        // 1. 檢查 LLM 回應，對每個選項，確認是否有工具呼叫
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

1. 新增調用 LLM 所需的導入：

    ```python
    # 大型語言模型
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. 接著，新增調用 LLM 的函數：

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
            # 可選參數
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

在上述代碼中，我們：

- 將從 MCP 服務器找到並轉換的函數（工具），傳遞給 LLM。
- 調用帶有這些函數的 LLM。
- 檢查結果以辨識是否有函數應該被調用。
- 最終，傳遞應調用的函數陣列。

1. 最後，更新主代碼：

    ```python
    prompt = "Add 2 to 20"

    # 問大模型需要使用哪些工具（如果有的話）
    functions_to_call = call_llm(prompt, functions)

    # 呼叫建議的函式
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

以上就是最後步驟。在上述代碼中，我們：

- 通過 `call_tool` 呼叫 MCP 工具，依據 LLM 根據提示決定的函數進行。
- 列印工具調用結果。

#### .NET

1. 示範用於向 LLM 發送提示請求的代碼：

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

在上述代碼中，我們：

- 從 MCP 服務器獲取工具，`var tools = await GetMcpTools()`。
- 定義了用戶提示 `userMessage`。
- 創建了包含模型和工具的選項對象。
- 發起了向 LLM 的請求。

1. 最後一步，檢查 LLM 是否認為應該調用函數：

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

在上述代碼中，我們：

- 遍歷函數調用列表。
- 對每個工具調用，解析名稱和參數，並使用 MCP 客戶端調用 MCP 服務器上的工具。最後列印結果。

完整代碼示例如下：

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

在上述代碼中，我們：

- 使用簡單的自然語言提示詞與 MCP 服務器工具互動。
- LangChain4j 框架自動處理：
  - 必要時將用戶提示轉換為工具調用。
  - 根據 LLM 的決策調用相應的 MCP 工具。
  - 管理 LLM 與 MCP 服務器間的對話流程。
- `bot.chat()` 方法返回包含 MCP 工具執行結果的自然語言回答。
- 這種方式提供了流暢的用戶體驗，用戶無需了解背後的 MCP 實作。

完整程式範例：

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

大部分工作將在此處完成。我們將使用初始用戶提示調用 LLM，然後處理回應，判斷是否需要呼叫任何工具。如果需要，我們將呼叫這些工具，並持續與 LLM 互動，直到不再需要呼叫任何工具並取得最終回應為止。

由於會多次調用 LLM，讓我們定義一個函數來處理對 LLM 的呼叫。將以下函數新增至你的 `main.rs` 文件：

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

此函數接受 LLM 客戶端、一系列訊息（包含用戶提示）、從 MCP 伺服器獲取的工具，發送請求至 LLM，並返回回應。
LLM 的回應會包含一個 `choices` 陣列。我們需要處理結果，查看是否存在任何 `tool_calls`。這讓我們知道 LLM 請求呼叫特定工具並附帶參數。將以下程式碼加入你的 `main.rs` 檔案底部，以定義一個處理 LLM 回應的函式：

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

    // 如有內容則打印
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // 處理工具調用
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // 新增助手訊息

        // 執行每個工具調用
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // 將工具結果新增到訊息中
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

如果存在 `tool_calls`，它會擷取工具資訊，呼叫 MCP 伺服器以執行工具請求，並將結果加入對話訊息中。接著會繼續與 LLM 進行對話，並更新訊息，包含助理的回應和工具呼叫結果。

為了擷取 LLM 回傳給 MCP 呼叫的工具呼叫資訊，我們將新增另一個輔助函式來擷取所有呼叫所需的資料。將以下程式碼加入你的 `main.rs` 檔案底部：

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

當所有部分都到位後，我們現在可以處理初始用戶提示並呼叫 LLM。更新你的 `main` 函式，包含以下程式碼：

```rust
// LLM 與工具調用的對話
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

這會使用初始用戶提示詢問兩數相加的和來查詢 LLM，並依據回應動態處理工具呼叫。

太棒了，你成功了！

## 作業

用練習中的程式碼擴充伺服器，增加更多工具。然後建立一個帶有 LLM 的用戶端，就像練習一樣，並用不同的提示測試，確保伺服器的所有工具都會被動態呼叫。以這種方式建立用戶端，意味著最終用戶將有很棒的使用者體驗，因為他們可以使用提示，而非確切的用戶端命令，且不會察覺有任何 MCP 伺服器正在被呼叫。

## 解答

[Solution](./solution/README.md)

## 主要重點

- 在用戶端加入 LLM，提供使用者更好的方式與 MCP 伺服器互動。
- 需要將 MCP 伺服器的回應轉換成 LLM 可以理解的格式。

## 範例

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 額外資源

## 接下來做什麼

- 下一步：[使用 Visual Studio Code 消費伺服器](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# 使用 LLM 建立一個客戶端

到目前為止，你已經看過如何建立一個伺服器和一個客戶端。客戶端能夠明確地呼叫伺服器，列出其工具、資源和提示。然而，這並不是一個非常實用的方法。你的用戶生活在智能代理時代，期望使用提示並與 LLM 進行交流。他們不在乎你是否使用 MCP 來存儲你的能力；他們只是期望能夠使用自然語言互動。那麼我們如何解決這個問題呢？解決方案是向客戶端添加一個 LLM。

## 概覽

在本課程中，我們將重點放在為客戶端添加 LLM，並展示如何為用戶提供更好的體驗。

## 學習目標

在本課程結束時，你將能夠：

- 使用 LLM 創建客戶端。
- 使用 LLM 無縫地與 MCP 伺服器進行互動。
- 在客戶端提供更好的最終用戶體驗。

## 方法

讓我們來了解我們需要採取的方法。添加 LLM 聽起來很簡單，但我們真的會這麼做嗎？

以下是客戶端與伺服器互動的方式：

1. 建立與伺服器的連線。

1. 列出能力、提示、資源和工具，並保存它們的結構。

1. 添加一個 LLM 並以 LLM 能理解的格式傳遞已保存的能力和結構。

1. 通過將用戶提示和客戶端列出的工具一起傳遞給 LLM，處理用戶提示。

很好，現在我們在高層次上了解了如何執行，讓我們在下面的練習中嘗試一下。

## 練習：建立一個帶有 LLM 的客戶端

在這個練習中，我們將學習如何向客戶端添加 LLM。

### 使用 GitHub 個人存取令牌進行身份驗證

創建 GitHub 令牌的過程很簡單。以下是方法：

- 前往 GitHub 設置 – 點擊右上角的個人頭像，選擇「Settings」。
- 導航到開發者設置 – 向下滾動並點擊「Developer Settings」。
- 選擇個人存取令牌 – 點擊「Fine-grained tokens」，然後生成新令牌。
- 配置你的令牌 – 添加備注、設置過期日期，並選擇所需的範圍（權限）。在這裡，請務必添加「Models」權限。
- 生成並複製令牌 – 點擊「Generate token」，並確保立即複製，因為你將無法再次查看它。

### -1- 連接伺服器

讓我們先建立客戶端：

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 導入 zod 以進行結構驗證

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

在以上程式碼中，我們：

- 匯入了所需的庫
- 建立了一個擁有兩個成員 `client` 與 `openai` 的類，用以分別管理客戶端及與 LLM 互動。
- 配置了 LLM 實例，將 `baseUrl` 設定為指向推理 API 的 GitHub 模型。

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# 為 stdio 連線建立伺服器參數
server_params = StdioServerParameters(
    command="mcp",  # 可執行文件
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

在以上程式碼中，我們：

- 匯入了 MCP 所需的庫
- 建立了一個客戶端

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

首先，你需要將 LangChain4j 的依賴加入 `pom.xml` 文件。添加這些依賴以啟用 MCP 整合及兼容 OpenAI 的 MiniMax API：

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

設定你的 MiniMax API 金鑰，並可選擇設定端點與模型。
`MINIMAX_MODEL_ID` 支持 `MiniMax-M3` 和 `MiniMax-M2.7`。若未設定
`OPENAI_BASE_URL`，`MINIMAX_REGION` 支持 `global_en` 和 `cn_zh`。

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

若想根據區域選擇端點，請移除 `OPENAI_BASE_URL`：

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

接著建立你的 Java 客戶端類別：

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

        // 建立用於連接伺服器的 MCP 傳輸
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // 建立 MCP 用戶端
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

在上述程式碼中，我們：

- **添加了 LangChain4j 依賴**：用於 MCP 整合和兼容 OpenAI 的 MiniMax API
- **匯入了 LangChain4j 庫**：用於 MCP 整合及 OpenAI 聊天模型功能
- **建立了 `ChatLanguageModel`**：配置使用 MiniMax，包括你的 MiniMax API 金鑰、端點及支持的模型 ID
- **設定了 HTTP 傳輸方式**：使用伺服器發送事件（SSE）連接 MCP 伺服器
- **建立了 MCP 客戶端**：負責與伺服器通訊
- **使用 LangChain4j 的內建 MCP 支援**：簡化了 LLM 與 MCP 伺服器之間的整合

#### Rust

此範例假設你有一個基於 Rust 的 MCP 伺服器在執行。如果你還沒有，請參考 [01-first-server](../01-first-server/README.md) 課程來建立伺服器。

當你有了 Rust MCP 伺服器後，打開終端機並切換到伺服器所在資料夾。接著執行以下命令來建立新的 LLM 客戶端專案：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

在你的 `Cargo.toml` 文件中加入以下依賴：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 雖然沒有官方的 Rust OpenAI 函式庫，但 `async-openai` crate 是一個由社群維護的庫，並且被廣泛使用，詳情見[此處](https://platform.openai.com/docs/libraries/rust#rust)。

打開 `src/main.rs` 文件並用以下程式碼替換其內容：

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

此程式碼設定了一個基本的 Rust 應用程式，用以連線至 MCP 伺服器以及 GitHub 模型以進行 LLM 互動。

> [!IMPORTANT]
> 執行應用程式前，請務必將 `OPENAI_API_KEY` 環境變數設為你的 GitHub 令牌。

好了，我們的下一步是列出伺服器上的能力。

### -2- 列出伺服器能力

現在我們將連接伺服器並請求其能力：

#### Typescript

在同一個類中添加以下方法：

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

在上述程式碼中，我們：

- 添加了連接伺服器的程式碼 `connectToServer`。
- 建立了一個 `run` 方法負責處理應用程式流程，目前只列出工具，但我們待會會繼續擴充。

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

以下為新增內容：

- 列出了資源與工具並列印出來。對工具我們也列出 `inputSchema`，稍後會用上。

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

在上述程式碼中，我們：

- 列出了 MCP 伺服器上的工具
- 對每個工具列出了名稱、描述以及其結構。後者是我們稍後呼叫工具時會用到的。

#### Java

```java
// 建立一個自動發現MCP工具的工具提供者
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP工具提供者會自動處理：
// - 從MCP伺服器列出可用工具
// - 將MCP工具架構轉換為LangChain4j格式
// - 管理工具執行及回應
```

在上述程式碼中，我們：

- 建立了一個 `McpToolProvider`，自動尋找並註冊所有 MCP 伺服器上的工具
- 工具提供者內部處理 MCP 工具結構與 LangChain4j 工具格式之間的轉換
- 此方法抽象了手動列出工具和轉換的過程

#### Rust

從 MCP 伺服器取得工具是通過 `list_tools` 方法完成的。在你的 `main` 函數中，設置好 MCP 客戶端後，添加以下程式碼：

```rust
// 獲取 MCP 工具列表
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 將伺服器能力轉換為 LLM 工具

列出伺服器能力後的下一步，是將它們轉換成 LLM 可以理解的格式。完成後，我們可以將這些能力作為工具提供給 LLM。

#### TypeScript

1. 添加以下程式碼來將 MCP 伺服器的回應轉換為 LLM 可用的工具格式：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 根據 input_schema 建立一個 zod schema
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

    以上程式碼將 MCP 伺服器的回應轉換為 LLM 可以理解的工具定義格式。

2. 接著更新 `run` 方法來列出伺服器能力：

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

    在上述程式碼中，我們更新了 `run` 方法來將結果映射並對每個條目調用 `openAiToolAdapter`。

#### Python

1. 首先，我們來建立以下轉換函數：

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

    在上面的函數 `convert_to_llm_tools` 中，我們將 MCP 工具回應轉換為 LLM 可以理解的格式。

2. 接著更新客戶端程式碼，利用此函數：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    這裡我們新增呼叫 `convert_to_llm_tool`，將 MCP 工具回應轉換為稍後可以餵給 LLM 的格式。

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

在上述程式碼中，我們：

- 建立了一個函式 `ConvertFrom`，接收名稱、描述和輸入結構。
- 定義功能以建立 `FunctionDefinition`，並傳入給 `ChatCompletionsDefinition`。後者是 LLM 可以理解的格式。

2. 接著看看如何更新既有程式碼以利用上述函式：

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

// 使用大型語言模型及多模態處理工具配置人工智能服務
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

在上述程式碼中，我們：

- 定義了簡單的 `Bot` 介面以進行自然語言互動
- 使用 LangChain4j 的 `AiServices` 自動將 LLM 與 MCP 工具提供者繫結
- 框架自動處理工具結構轉換與函式呼叫的細節
- 此方法省去了手動轉換工具的工作，LangChain4j 負責將 MCP 工具轉為 LLM 可用格式

#### Rust

為了將 MCP 工具回應轉換為 LLM 能理解的格式，我們將新增一個輔助函數來格式化工具清單。在 `main` 函數下面的 `main.rs` 文件中添加以下程式碼。此函數將在向 LLM 發出請求時被調用：

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

很好，我們已經設定好接收用戶請求的流程，接著來處理它們。

### -4- 處理用戶提示請求

在這部分程式碼中，我們將處理用戶請求。

#### TypeScript

1. 添加一個方法用以呼叫我們的 LLM：

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

        // 3. 使用結果做某些事情
        // 待辦事項

        }
    }
    ```

    在上面的程式碼中，我們：

    - 新增了一個方法 `callTools`。
    - 該方法接收 LLM 回應並檢查被呼叫了哪些工具（如果有的話）：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 呼叫工具
        }
        ```

    - 如果 LLM 指示應該呼叫工具，就調用該工具：

        ```typescript
        // 2. 呼叫服務器的工具
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 使用結果做些事情
        // 待辦事項
        ```

2. 更新 `run` 方法，加入呼叫 LLM 與 `callTools` 的程式碼：

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

    // 3. 檢視 LLM 回應，對每個選項，檢查是否包含工具呼叫
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

很好，以下是完整程式碼列表：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 導入 zod 用於結構驗證

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 未來可能需要改用此網址：https://models.github.ai/inference
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
    
        // 3. 逐一檢查 LLM 回應中每個選項，查看是否有工具呼叫
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

1. 新增一些呼叫 LLM 所需的匯入：

    ```python
    # 大語言模型
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. 接著新增呼叫 LLM 的函式：

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

    在上述程式碼中，我們：

    - 將從 MCP 伺服器找到並轉換的函式傳入 LLM。
    - 然後使用該函式呼叫 LLM。
    - 接著檢查結果以決定是否需呼叫函式。
    - 最後，我們將要呼叫的函式列表傳給 LLM。

3. 最後一步，更新主要程式碼：

    ```python
    prompt = "Add 2 to 20"

    # 問LLM有沒有要用到任何工具
    functions_to_call = call_llm(prompt, functions)

    # 呼叫建議的函數
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    好了，這是最後一步，在上面程式碼中我們：

    - 使用 LLM 考慮的函式透過 `call_tool` 呼叫 MCP 工具。
    - 列印出 MCP 伺服器工具呼叫結果。

#### .NET

1. 展示一段用於 LLM 提示請求的程式碼：

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

    在上述程式碼中，我們：

    - 從 MCP 伺服器取得工具，`var tools = await GetMcpTools()`。
    - 定義了使用者提示 `userMessage`。
    - 建立一個包含模型及工具的設定物件。
    - 向 LLM 發出請求。

2. 最後一步，查看 LLM 是否認為應該呼叫函式：

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

    在上述程式碼中，我們：

    - 迴圈處理函式呼叫列表。
    - 對每個工具呼叫，解析名稱和參數並透過 MCP 客戶端呼叫 MCP 伺服器上的工具，最後列印結果。

以下是完整程式碼：

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

在上述程式碼中，我們：

- 使用簡單的自然語言提示與 MCP 伺服器工具互動
- LangChain4j 框架自動處理：
  - 根據需要將使用者提示轉換成工具呼叫
  - 根據 LLM 決策呼叫適當的 MCP 工具
  - 管理 LLM 與 MCP 伺服器間的對話流程
- `bot.chat()` 方法返回可能包含 MCP 工具執行結果的自然語言回應
- 此方法為用戶提供了無縫體驗，用戶無需知道底層 MCP 的實作

完整程式碼範例：

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

這裡是大部分工作發生的地方。我們將以初始用戶提示呼叫 LLM，然後處理回應以判斷是否需要呼叫任何工具。如果需要，我們將呼叫這些工具，並持續與 LLM 對話，直到不再需要工具呼叫並有最終回應為止。


我們會多次調用 LLM，所以我們來定義一個函數來處理 LLM 調用。將以下函數加入你的 `main.rs` 文件：

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

此函數接受 LLM 客戶端、一系列訊息（包括用戶提示）、來自 MCP 伺服器的工具，並向 LLM 發送請求，返回回應。

LLM 回應會包含一個 `choices` 陣列。我們需要處理結果來檢查是否有 `tool_calls` 存在。這可以讓我們知道 LLM 正請求以參數調用特定工具。將以下程式碼加入 `main.rs` 文件底部，以定義一個處理 LLM 回應的函數：

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
        messages.push(message.clone()); // 新增助理訊息

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

            // 將工具結果加入訊息
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // 以工具結果繼續對話
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

如果存在 `tool_calls`，它會擷取工具資訊，呼叫 MCP 伺服器執行工具請求，並將結果加入對話訊息中。然後繼續與 LLM 對話，並更新訊息內容為助理回應及工具調用結果。

為了擷取 LLM 回傳用於 MCP 呼叫的工具調用資訊，我們會再新增一個輔助函數來擷取進行呼叫所需的所有內容。將以下程式碼加入 `main.rs` 文件底部：

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

將所有部分組合完成後，我們現在可以處理初始使用者提示並調用 LLM 了。更新你的 `main` 函數，包含以下程式碼：

```rust
// 與工具通話的LLM對話
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

這會用初始使用者提示查詢 LLM，要求計算兩個數字的總和，並處理回應以動態執行工具呼叫。

很好，你完成了！

## 作業

將練習中的程式碼擴充伺服器，加入更多工具。然後建立一個有 LLM 的客戶端，就像練習中所做的，並以不同提示測試，確保你的伺服器工具都能被動態調用。這種建立客戶端的方式能提供終端使用者很棒的使用體驗，因為他們能用提示詞，而非精確的客戶端命令，且不會察覺到有任何 MCP 伺服器被調用。

## 解答

[解答](./solution/README.md)

## 重要重點

- 為你的客戶端添加 LLM，能提供用戶更好的 MCP 伺服器互動方式。
- 你需要轉換 MCP 伺服器回應為 LLM 能理解的格式。

## 範例

- [Java 計算器](../samples/java/calculator/README.md)
- [.Net 計算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算器](../samples/javascript/README.md)
- [TypeScript 計算器](../samples/typescript/README.md)
- [Python 計算器](../../../../03-GettingStarted/samples/python)
- [Rust 計算器](../../../../03-GettingStarted/samples/rust)

## 額外資源

## 後續內容

- 下一步：[使用 Visual Studio Code 消費伺服器](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
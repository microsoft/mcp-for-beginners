# Креирање клијента са LLM-ом

> [!NOTE]
> Примери Java клијената повезују се преко застарелог HTTP+SSE транспорта и
> циљају MCP `2025-11-25` SDK API-је. Користите SDK компатибилан са `2026-07-28` и
> Streamable HTTP за нове даљинске клијенте.

До сада сте видели како да креирате сервер и клијента. Клијент је могао експлицитно да позове сервер да листа његове алате, ресурсе и упите. Међутим, ово није баш практичан приступ. Ваша корисници живе у агенцијској ери и очекују да користе упите и комуницирају са LLM-ом уместо тога. Они не брину да ли користите MCP за складиштење ваших капацитета; једноставно очекују да комуницирају користећи природни језик. Како то онда решавамо? Решење је да додамо LLM клијенту.

## Преглед

У овој лекцији фокусирамо се на додавање LLM-а клијенту и показујемо како то пружа много боље корисничко искуство.

## Циљеви учења

На крају ове лекције ћете моћи да:

- Креирате клијента са LLM-ом.
- Беспрекорно комуницирате са MCP сервером користећи LLM.
- Пружите боље корисничко искуство на клијентској страни.

## Приступ

Хајде да покушамо да разумемо приступ који треба да применимо. Додавање LLM-а звучи једноставно, али да ли ћемо то заправо урадити?

Ево како ће клијент комуницирати са сервером:

1. Успостављање везе са сервером.

1. Листати капацитете, упите, ресурсе и алате, и сачувати њихове шеме.

1. Додати LLM и проследити сачуване капацитете и њихове шеме у формату који LLM разуме.

1. Обрадити кориснички упит прослеђивањем LLM-у заједно са алатима које је клијент листао.

Одлично, сада када разумемо како можемо ово урадити на високом нивоу, хајде да покушамо у доњој вежби.

## Вежба: Креирање клијента са LLM-ом

У овој вежби ћемо научити како додати LLM нашем клијенту.

### Конфигуришите Microsoft Foundry

GitHub Models је повучен 30. јула 2026. Креирајте Microsoft Foundry ресурс,
активирајте модел као што је `gpt-5.1`, и подесите ове променљиве окружења:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Користите име распоређивања у позивима API-ја. Оно може бити другачије од имена основног модела. Прегледајте

[распоред повлачења Microsoft Foundry модела](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
пре избора модела.

### -1- Повежите се са сервером

Прво хајде да креирамо нашег клијента:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }
}
```

У претходном коду смо:

- Увезли потребне библиотеке
- Креирали класу са два члана, `client` и `openai`, која ће нам помоћи да управљамо клијентом и комуницирамо са LLM-ом.
- Конфигурисали OpenAI клијента да користи Microsoft Foundry v1 крајњу тачку и API кључ.

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

У претходном коду смо:

- Увезли потребне библиотеке за MCP
- Креирали клијента

#### .NET

```csharp
using ModelContextProtocol.Client;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
var client = new ChatClient(
    deployment,
    new ApiKeyCredential(apiKey),
    new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Прво, потребно је да додате зависности LangChain4j у ваш `pom.xml` фајл. Додајте ове зависности да бисте омогућили интеграцију с MCP-ом и OpenAI компатибилним MiniMax API-јем:

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

Подесите ваш MiniMax API кључ и опционално крајњу тачку и модел.
`MINIMAX_MODEL_ID` подржава `MiniMax-M3` и `MiniMax-M2.7`. Ако
`OPENAI_BASE_URL` није подешен, `MINIMAX_REGION` подржава `global_en` и `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

За избор крајње тачке по региону уместо тога, прескочите `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Затим креирајте вашу Java клијент класу:

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

        // Create MCP transport for connecting to server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Create MCP client
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

У претходном коду смо:

- **Додали LangChain4j зависности**: Потребно за интеграцију MCP-а и OpenAI компатибилног MiniMax API-ја
- **Увезли LangChain4j библиотеке**: За интеграцију MCP-а и OpenAI чат модела
- **Креирали `ChatLanguageModel`**: Конфигурисан за коришћење MiniMax-а са вашим MiniMax API кључем, крајњом тачком и подржаним ID-ом модела
- **Подесили HTTP транспорт**: Користећи Server-Sent Events (SSE) за повезивање са MCP сервером
- **Креирали MCP клијента**: Који ће обрађивати комуникацију са сервером
- **Користили уграђену подршку LangChain4j за MCP**: Која поједностављује интеграцију између LLM-ова и MCP сервера

#### Rust

Овај пример претпоставља да имате настављен MCP сервер заснован на Rust-у. Ако га немате, погледајте назад у лекцију [01-first-server](../01-first-server/README.md) да бисте креирали сервер.

Када имате ваш Rust MCP сервер, отворите терминал и идите у исту фасциклу као и сервер. Затим покрените следећу команду да бисте креирали нови LLM клијент пројекат:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Додајте следеће зависности у ваш `Cargo.toml` фајл:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Не постоји званична Rust библиотека за OpenAI, али `async-openai` crate је [једна библиотека коју одржава заједница](https://platform.openai.com/docs/libraries/rust#rust) и често се користи.

Отворите `src/main.rs` фајл и замените његов садржај следећим кодом:

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
    // Initial message
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Setup Microsoft Foundry client
    let endpoint = std::env::var("AZURE_OPENAI_ENDPOINT")?;
    let api_key = std::env::var("AZURE_OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base(format!("{}/openai/v1", endpoint.trim_end_matches('/')))
            .with_api_key(api_key),
    );

    // Setup MCP client
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

    // TODO: Get MCP tool listing 

    // TODO: LLM conversation with tool calls

    Ok(())
}
```

Овај код подешава Rust апликацију која се повезује са MCP сервером и
Microsoft Foundry моделом за интеракције са LLM-ом.

> [!IMPORTANT]
> Подесите `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, и
> `AZURE_OPENAI_DEPLOYMENT` пре покретања апликације.

Одлично, за следећи корак, хајде да листамо капацитете на серверу.

### -2- Листање капацитета сервера

Сада ћемо се повезати са сервером и затражити његове капацитете:

#### Typescript

У истој класи, додајте следеће методе:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

У претходном коду смо:

- Додали код за повезивање са сервером, `connectToServer`.
- Креирали `run` методу која управља током апликације. Тренутно само листа алате, али ускоро ћемо додати још.

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
    print("Tool", tool.inputSchema["properties"])
```

Ево шта смо додали:

- Листање ресурса и алата и њихово исписивање. За алате такође листамо `inputSchema` који ћемо касније користити.

#### .NET

```csharp
async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

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

У претходном коду смо:

- Листали алате доступне на MCP серверу
- За сваки алат, листали име, опис и његову схему. Ово последње ћемо користити за позивање алата ускоро.

#### Java

```java
// Create a tool provider that automatically discovers MCP tools
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// The MCP tool provider automatically handles:
// - Listing available tools from the MCP server
// - Converting MCP tool schemas to LangChain4j format
// - Managing tool execution and responses
```

У претходном коду смо:

- Креирали `McpToolProvider` који аутоматски открива и региструје све алате са MCP сервера
- Провајдер алата управља конверзијом између MCP алатских шема и LangChain4j алатског формата интерно
- Овај приступ апстрахује ручно листање и конверзију алата

#### Rust

Добијање алата са MCP сервера се врши користећи `list_tools` методу. У вашој `main` функцији, након подешавања MCP клијента, додајте следећи код:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конверзија капацитета сервера у LLM алате

Следећи корак након листања капацитета сервера је да их конвертујемо у формат који LLM разуме. Када то урадимо, можемо ове капацитете пружити као алате нашем LLM-у.

#### TypeScript

1. Додајте следећи код да конвертујете одговор са MCP сервера у формат алата који LLM може користити:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Create a zod schema based on the input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitly set type to "function"
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

    Горњи код узима одговор са MCP сервера и конвертује га у дефиницију алата коју LLM разуме.

2. Хајде да ажурирамо `run` методу следеће да листамо капацитете сервера:

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

    У претходном коду, ажурирали смо `run` методу да мапира кроз резултат и за сваки унос позове `openAiToolAdapter`.

#### Python

1. Прво, хајде да креирамо следећу конверзијску функцију

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

    У функцији `convert_to_llm_tools` узимамо MCP алатски одговор и конвертујемо га у формат који LLM разуме.

2. Следеће, ажурирајмо наш код клијента да искористи ову функцију овако:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Овде додајемо позив `convert_to_llm_tool` да конвертујемо MCP алатски одговор у нешто што можемо касније проследити LLM-у.

#### .NET

1. Додајмо код за конверзију MCP алатског одговора у нешто што LLM разуме

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

У претходном коду смо:

- Креирали функцију `ConvertFrom` која прима име, опис и улазну шему.
- Креирали OpenAI `ChatTool` из MCP алатског JSON шема.

2. Погледајмо како можемо ажурирати постојећи код да искористи ову функцију:

    ```csharp
    async Task<List<ChatTool>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatTool> toolDefinitions = [];

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);
        }

        return toolDefinitions;
    }
    ```
    
У претходном коду смо:

- Ажурирали функцију да конвертује MCP алатски одговор у LLM алат. Истакнућемо додат код:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Улазна шема је део одговора алата, али на "properties" атрибуту, па морамо издвојити. Поред тога, сада позивамо `ConvertFrom` са детаљима алата. Сада када смо обавили тешки део, погледајмо како се саставља позив када обрађујемо кориснички упит.

#### Java

```java
// Create a Bot interface for natural language interaction
public interface Bot {
    String chat(String prompt);
}

// Configure the AI service with LLM and MCP tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У претходном коду смо:

- Дефинисали једноставан `Bot` интерфејс за интеракције на природном језику
- Користили LangChain4j `AiServices` да аутоматски повежемо LLM са MCP провајдером алата
- Фрејмворк аутоматски управља конверзијом схеме алата и позивом функција у позадини
- Овај приступ елиминише ручну конверзију алата – LangChain4j обрађује сву сложеност конверзије MCP алата у LLM-компатибилан формат

#### Rust

Да бисмо конвертовали MCP алатски одговор у формат који LLM разуме, додаћемо помоћну функцију која форматира листу алата. Додајте следећи код у ваш `main.rs` фајл испод функције `main`. Ово ће се позивати приликом захтева ка LLM-у:

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

Одлично, сада смо спремни да обрађујемо корисничке захтеве, па хајде то урадимо следеће.

### -4- Обрада корисничких упита

У овом делу кода ћемо обрађивати корисничке захтеве.

#### TypeScript

1. Додајте методу која ће се користити за позивање нашег LLM-а:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  

        }
    }
    ```

    У претходном коду смо:

    - Додали методу `callTools`.
    - Метода прима LLM одговор и проверава које алате је позвао, ако их је било:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Позива алат ако LLM указује да треба да се позове:

        ```typescript
        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  
        ```

2. Ажурирајте `run` методу да укључује позиве LLM-у и позив `callTools`:

    ```typescript

    // 1. Create messages that's input for the LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Calling the LLM
    let response = this.openai.chat.completions.create({
        model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
        max_completion_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Go through the LLM response,for each choice, check if it has tool calls 
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Одлично, хајде да прикажемо цео код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
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
          // Create a zod schema based on the input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitly set type to "function"
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
    
    
          // 2. Call the server's tool 
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Do something with the result
          // TODO  
    
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
            model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
            max_completion_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Go through the LLM response, for each choice, check if it has tool calls 
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

1. Додајмо неке потребне увозе за позивање LLM-а

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Затим додајмо функцију која ће позивати LLM. Овај пример користи
    активни модел `gpt-5.1`. Погледајте
    [распоред повлачења Microsoft Foundry модела](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    приликом избора модела за вашу апликацију.

    ```python
    # llm

    def call_llm(prompt, functions):
        client = OpenAI(
            base_url=(
                f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/"
            ),
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

        print("CALLING LLM")
        response = client.chat.completions.create(
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
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
            tools=functions,
            max_completion_tokens=1000,
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

У претходном коду смо:

- Проследили функције које смо нашли на MCP серверу и конвертовали LLM-у.
- Затим позвали LLM са тим функцијама.
- Затим прегледали резултат да видимо које функције треба позвати, ако их има.
- На крају проследили низ функција за позив.

3. Последњи корак, ажурирајмо главни код:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

Ето, то је био последњи корак, у горе наведеном коду ми:

- Позивамо MCP алат преко `call_tool` користећи функцију за коју је LLM мислио да треба да се позове на основу нашег упита.
- Штампамо резултат позива алата на MCP сервер.

#### .NET

1. Прикажимо код за извршавање захтева за LLM упит:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new UserChatMessage(userMessage));


    // 2. Define options, including the tools
    var options = new ChatCompletionOptions
    {
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
    var content = response.Content.FirstOrDefault()?.Text;

    ```

У претходном коду смо:

    - Преузете алатке са MCP сервера, `var tools = await GetMcpTools()`.
    - Дефинисана корисничка упит `userMessage`.
    - Конструктован објекат опција који специфицира модел и алатке.
    - Послат захтев ка LLM-у.

2. Још један последњи корак, хајде да видимо да ли LLM мисли да треба да позовемо функцију:

    ```csharp
    // 4. Check if the response contains a function call
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
        var result = await mcpClient.CallToolAsync(
            call.FunctionName,
            dict!,
            cancellationToken: CancellationToken.None
        );

        var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
        if (textBlock != null)
        {
            Console.WriteLine(textBlock.Text);
        }

    }
    ```

    У претходном коду смо:

    - Прошли кроз листу позива функција.
    - За сваки позив алата издвојили име и аргументе и позвали алат на MCP серверу користећи MCP клијент. На крају исписујемо резултате.

Ево кода у целини:

```csharp
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
if (string.IsNullOrWhiteSpace(endpoint) || string.IsNullOrWhiteSpace(apiKey))
{
    Console.WriteLine("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY.");
    return;
}

var client = new ChatClient(
    model: deployment,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });
var chatHistory = new List<ChatMessage>
{
    new SystemChatMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}

async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
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

chatHistory.Add(new UserChatMessage(userMessage));

// 3. Define options, including the tools
var options = new ChatCompletionOptions
{
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
var content = response.Content.FirstOrDefault()?.Text;

// 5. Check if the response contains a function call
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
    var result = await mcpClient.CallToolAsync(
        call.FunctionName,
        dict!,
        cancellationToken: CancellationToken.None
    );

    var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
    if (textBlock != null)
    {
        Console.WriteLine(textBlock.Text);
    }

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Јава

```java
try {
    // Execute natural language requests that automatically use MCP tools
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

У претходном коду смо:

- Користили једноставне природне језичке упите за интеракцију са алатима MCP сервера
- LangChain4j оквир аутоматски управља:
  - Претварањем корисничких упита у позиве алата кад је то потребно
  - Позивањем одговарајућих MCP алата на основу одлуке LLM-а
  - Управљањем током разговора између LLM-а и MCP сервера
- `bot.chat()` метода враћа одговоре у природном језику који могу укључивати резултате извођења MCP алата
- Овај приступ обезбеђује беспрекорно корисничко искуство где корисници не морају да знају о унутрашњој имплементацији MCP-а

Комплетан пример кода:

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

#### Раст

Овде се одвија већина посла. Позваћемо LLM са почетним корисничким упитом, затим обрадити одговор да видимо да ли је потребно позвати неке алате. Уколико је потребно, позваћемо те алате и наставити разговор са LLM-ом док више не буде потребно позива алата и док не добијемо коначни одговор.

Направићемо више позива LLM-у, па хајде да дефинишемо функцију која ће руковати позивима LLM-а. Додајте следећу функцију у ваш `main.rs` фајл:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let model = std::env::var("AZURE_OPENAI_DEPLOYMENT")
        .unwrap_or_else(|_| "gpt-5.1".to_string());
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": model,
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Ова функција прихвата LLM клијента, листу порука (укључујући кориснички упит), алате са MCP сервера, и шаље захтев LLM-у, враћајући одговор.

Одговор LLM-а ће садржати низ `choices`. Потребно је да обрадимо резултат да видимо да ли су присутни било какви `tool_calls`. Ово нам говори да LLM тражи да се позове одређени алат са аргументима. Додајте следећи код на крај вашег `main.rs` фајла да дефинишете функцију која ће руковати одговором LLM-а:

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

    // Print content if available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Handle tool calls
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Add assistant message

        // Execute each tool call
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Add tool result to messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continue conversation with tool results
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

Уколико су `tool_calls` присутни, извлачи информације о алату, позива MCP сервер са захтевом за алат, и додаје резултате у поруке разговора. Онда наставља разговор са LLM-ом, при чему се поруке ажурирају одговором асистента и резултатима позива алата.

Да бисмо извукли информације о позиву алата које LLM враћа за MCP позиве, додајемо још једну помоћну функцију за извлачење свега што је потребно за позив. Додајте следећи код на крај вашег `main.rs` фајла:

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

Са свим деловима на месту, сада можемо да руковамо почетним корисничким упитом и позовемо LLM. Ажурирајте вашу `main` функцију да укључи следећи код:

```rust
// LLM conversation with tool calls
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

Ово ће послати упит LLM-у са почетним корисничким упитом питајући за збир два броја, и обрадиће одговор да динамички рукује позивима алата.

Одлично, успели сте!

## Задатак

Узмите код из вежбе и направите сервер са још неколико алата. Затим направите клијента са LLM-ом, као у вежби, и тестирајте са различитим упитима како бисте били сигурни да сви ваши серверски алати могу да се позову динамички. Овим приступом израде клијента крајњи корисник ће имати одлично корисничко искуство јер може да користи упите, уместо тачних команди клијента, и неће бити свестан било каквог позива MCP сервера.

## Решење

[Решење](./solution/README.md)

## Кључне поуке

- Додавање LLM-а у ваш клијент пружа бољи начин корисничке интеракције са MCP серверима.
- Потребно је да претворите одговор MCP сервера у нешто што LLM може да разуме.

## Примери

- [Јава калкулатор](../samples/java/calculator/README.md)
- [.NET калкулатор](../../../../03-GettingStarted/samples/csharp)
- [ЈаваСкрипт калкулатор](../samples/javascript/README.md)
- [ТајпСкрипт калкулатор](../samples/typescript/README.md)
- [Пајтон калкулатор](../../../../03-GettingStarted/samples/python)
- [Раст калкулатор](../../../../03-GettingStarted/samples/rust)

## Додатни ресурси

## Шта следи

- Следеће: [Коришћење сервера помоћу Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
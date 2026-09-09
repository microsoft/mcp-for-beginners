# Креирање клијента са LLM

До сада сте видели како се креира сервер и клијент. Клијент је могао експлицитно да позове сервер да наброји своје алате, ресурсе и упите. Међутим, ово није веома практичан приступ. Ваши корисници живе у ери агената и очекују да користе упите и комуницирају са LLM-ом уместо тога. Не занима их да ли користите MCP за чување својих могућности; они једноставно очекују да комуницирају коришћењем природног језика. Па како то решити? Решење је да додате LLM клијенту.

## Преглед

У овој лекцији фокусираћемо се на додавање LLM-а клијенту и показати како то пружа много боље корисничко искуство.

## Циљеви учења

До краја ове лекције моћи ћете да:

- Креирате клијента са LLM-ом.
- Беспрекорно комуницирате са MCP сервером користећи LLM.
- Обезбедите боље корисничко искуство на страни клијента.

## Приступ

Покушајмо да разумемо приступ који треба применити. Додавање LLM-а звучи једноставно, али да ли ћемо то заиста урадити?

Ево како ће клијент комуницирати са сервером:

1. Успоставити везу са сервером.

1. Набројати могућности, упите, ресурсе и алате, и сачувати њихову шему.

1. Додати LLM и проследити сачуване могућности и њихову шему у формату који LLM разуме.

1. Обрадити кориснички упит прослеђивањем LLM-у заједно са алатима које клијент има.

Супер, сада када разумемо како то урадити на општем нивоу, покушајмо у следећем вежбању.

## Вежба: Креирање клијента са LLM-ом

У овој вежби ћемо научити како да додамо LLM нашем клијенту.

### Аутентификација коришћењем GitHub Personal Access Token

Креирање GitHub токена је једноставан процес. Ево како можете то урадити:

- Идите у GitHub Settings – Кликните на своју слику профила горе десно и изаберите Settings.
- Идите у Developer Settings – Скролујте доле и кликните на Developer Settings.
- Изаберите Personal Access Tokens – Кликните на Fine-grained tokens и онда Generate new token.
- Конфигуришите свој токен – Додајте белешку за референцу, подесите датум истека и изаберите потребне дозвољене области (permissions). У овом случају обавезно укључите Models дозволу.
- Генеришите и копирајте токен – Кликните Generate token, и уверите се да сте га одмах копирали, јер га поново нећете видети.

### -1- Повежите се са сервером

Прво направимо наш клијент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Увоз zod за валидацију шеме

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

У претходном коду ми смо:

- Импортовали потребне библиотеке
- Креирали класу са два члана, `client` и `openai` који ће нам помоћи да управљамо клијентом и интерактивно радимо са LLM-ом.
- Конфигурисали нашу LLM инстанцу да користи GitHub Models подешавањем `baseUrl` за inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Креирај параметре сервера за стдио везу
server_params = StdioServerParameters(
    command="mcp",  # Извршна датотека
    args=["run", "server.py"],  # Опциони аргументи командне линије
    env=None,  # Опционалне променљиве окружења
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Иницијализуј везу
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

У претходном коду ми смо:

- Импортовали потребне библиотеке за MCP
- Креирали клијента

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

Прво, потребно је да додате LangChain4j зависности у ваш `pom.xml` фајл. Додајте ове зависности како бисте омогућили интеграцију MCP-а и OpenAI-компатибилни MiniMax API:

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

Подесите ваш MiniMax API кључ и, по жељи, endpoint и модел.
`MINIMAX_MODEL_ID` подржава `MiniMax-M3` и `MiniMax-M2.7`. Ако
`OPENAI_BASE_URL` није подешен, `MINIMAX_REGION` подржава `global_en` и `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Да бисте изабрали endpoint по региону, уместо тога изоставите `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Затим креирајте вашу Java клиент класу:

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

        // Креирај MCP транспорт за повезивање са сервером
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Креирај MCP клијента
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

- **Додали LangChain4j зависности**: Потребне за интеграцију MCP-а и OpenAI-компатибилног MiniMax API-ја
- **Импортовали LangChain4j библиотеке**: За интеграцију MCP и OpenAI chat модела
- **Креирали `ChatLanguageModel`**: Конфигурисан да користи MiniMax са вашим MiniMax API кључем, endpoint-ом и подржаним ID моделa
- **Подесили HTTP транспорт**: Коришћењем Server-Sent Events (SSE) за повезивање са MCP сервером
- **Креирали MCP клијента**: Који ће руковати комуникацијом са сервером
- **Користили уграђену LangChain4j подршку за MCP**: Која поједностављује интеграцију између LLM-ова и MCP сервера

#### Rust

Овај пример претпоставља да имате покренут MCP сервер написан у Rust-у. Ако га немате, погледајте назад у лекцију [01-first-server](../01-first-server/README.md) како бисте направили сервер.

Када имате ваш Rust MCP сервер, отворите терминал и идите у исти директоријум као сервер. Затим покрените следећу команду да бисте креирали нови пројекат LLM клијента:

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
> Не постоји званична Rust библиотека за OpenAI, али `async-openai` crate је [библиотека одржавана заједницом](https://platform.openai.com/docs/libraries/rust#rust) која се често користи.

Отворите фајл `src/main.rs` и замените његов садржај следећим кодом:

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
    // Почетна порука
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Подешавање OpenAI клијента
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Подешавање MCP клијента
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

    // ОБАВЕЗНО: Преузми листу алата MCP

    // ОБАВЕЗНО: LLM конверзација са позивима алата

    Ok(())
}
```

Овај код подешава основну Rust апликацију која ће се повезати са MCP сервером и GitHub Models за интеракцију LLM-а.

> [!IMPORTANT]
> Обавезно поставите `OPENAI_API_KEY` као варијаблу окружења са вашим GitHub токеном пре покретања апликације.

Сјајно, за следећи корак хајде да набројимо могућности сервера.

### -2- Набројати могућности сервера

Сада ћемо се повезати са сервером и тражити његове могућности:

#### Typescript

У истој класи додајте следеће методе:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // листање алата
    const toolsResult = await this.client.listTools();
}
```

У претходном коду смо:

- Додали код за повезивање са сервером, `connectToServer`.
- Креирали метод `run` одговоран за руковање током апликације. До сада он само набраја алате, али ћемо ускоро додати више.

#### Python

```python
# Листа доступних ресурса
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Листа доступних алата
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ево шта смо додали:

- Набројали ресурсе и алате и одштампали их. За алате смо такође набројали `inputSchema` који касније користимо.

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

У претходном коду смо:

- Набројали алате доступне на MCP серверу
- За сваки алат набројали назив, опис и његову шему. Ово последње ћемо користити да позивамо алате убрзо.

#### Java

```java
// Креирајте провајдера алата који аутоматски открива MCP алате
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP провајдер алата аутоматски обрађује:
// - Листање доступних алата са MCP сервера
// - Претварање шема MCP алата у LangChain4j формат
// - Управљање извршавањем алата и одговорима
```

У претходном коду смо:

- Креирали `McpToolProvider` који аутоматски открива и региструје све алате са MCP сервера
- Провајдер алата управља претварањем између MCP шема алата и LangChain4j формата алата интерно
- Овај приступ апстрахује ручни процес набрајања и претварања алата

#### Rust

Превлачење алата са MCP сервера се обавља методом `list_tools`. У вашој функцији `main`, након подешавања MCP клијента, додајте следећи код:

```rust
// Добити листу MCP алата
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Претворити могућности сервера у LLM алате

Следећи корак након набрајања могућности сервера је да их претворимо у формат који LLM разуме. Када то урадимо, можемо ове могућности пружити као алате нашем LLM-у.

#### TypeScript

1. Додајте следећи код за претварање одговора са MCP сервера у формат алата који LLM може користити:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Креирај зод шему на основу input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Јасно подеси тип на "функција"
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

    Горњи код узима одговор са MCP сервера и претвара га у дефиницију алата коју LLM може да разуме.

2. Хајде да ажурирамо метод `run` да набраја могућности сервера:

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

    У претходном коду ажурирали смо метод `run` да пролази кроз резултат и за сваки унос позива `openAiToolAdapter`.

#### Python

1. Прво, направимо следећу конвертор функцију

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

    У функцији `convert_to_llm_tools` претварамо MCP одговор алата у формат који LLM може да разуме.

2. Следеће, ажурирајмо наш клијентски код да користи ову функцију овако:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Овде додавамо позив `convert_to_llm_tool` да конвертујемо MCP одговор алата у нешто што касније можемо проследити LLM-у.

#### .NET

1. Хајде да додамо код за претварање одговора MCP алата у нешто што LLM може разумети

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

У претходном коду смо:

- Креирали функцију `ConvertFrom` која узима назив, опис и улазну шему.
- Дефинисали функционалност која креира `FunctionDefinition` који се прослеђује `ChatCompletionsDefinition`. Ово је нешто што LLM разуме.

2. Хајде да видимо како можемо ажурирати постојећи код да искористи ову функцију:

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
// Креирајте интерфејс за Бота за интеракцију природним језиком
public interface Bot {
    String chat(String prompt);
}

// Конфигуришите АИ услугу са ЛЛМ и МЦП алатима
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У претходном коду смо:

- Дефинисали једноставан интерфејс `Bot` за интеракцију на природном језику
- Користили LangChain4j `AiServices` за аутоматско повезивање LLM-а са MCP провајдером алата
- Фрејмворк аутоматски управља конверзијом шема алата и позивима функција у позадини
- Овај приступ елиминише ручну конверзију алата - LangChain4j решава сложеност претварања MCP алата у LLM-компатибилни формат

#### Rust

Да бисмо претворили одговор MCP алата у формат који LLM разуме, додамо помоћну функцију која форматира листу алата. Додајте следећи код у ваш фајл `main.rs` испод функције `main`. Ово ће се звати када шаљемо захтеве LLM-у:

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

Супер, сада смо спремни да обрадимо корисничке захтеве, па хајде то урадимо следеће.

### -4- Обрадити кориснички упит

У овом делу кода ћемо обрадити корисничке упите.

#### TypeScript

1. Додајте метод којим ћемо позивати наш LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Позовите алатку сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Урадите нешто са резултатом
        // ЗАДАЦИ

        }
    }
    ```

    У претходном коду смо:

    - Додали метод `callTools`.
    - Метод прима LLM одговор и проверава који су алати позвани, ако их има:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // позови алат
        }
        ```

    - Позива алат, ако LLM указује да треба да буде позван:

        ```typescript
        // 2. Позвати алатку сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Урадити нешто са резултатом
        // ЗА УРАДИТИ
        ```

2. Ажурирајте метод `run` да укључи позиве LLM-у и позив `callTools`:

    ```typescript

    // 1. Креирајте поруке које су улаз за LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Позивање LLM-а
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Прођите кроз LLM одговор, за сваки избор проверите да ли има позиве алата
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Супер, ево целог кода:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Увези зод за валидацију шеме

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можда ће бити потребно променити на овај УРЛ у будућности: https://models.github.ai/inference
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
          // Направи зод шему на основу input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Јасно подеси тип на "function"
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
    
    
          // 2. Позови алатку сервера
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Уради нешто са резултатом
          // ЗАДАТАК
    
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
    
        // 3. Прођи кроз одговор ЛЛМ, за сваки избор провери да ли има позиве алатке
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

1. Додајмо неке увозе потребне за позив LLM-а

    ```python
    # ллм
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Следеће, додајмо функцију која ће позивати LLM:

    ```python
    # ллм

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
            # Опционални параметри
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

    У претходном коду смо:

    - Проследили функције које смо нашли на MCP серверу и конвертовали их LLM-у.
    - Затим смо позвали LLM са тим функцијама.
    - Затим проверавамо резултат да видимо које функције треба позвати, ако их има.
    - На крају прослеђујемо низ функција за позив.

3. Последњи корак, ажурирајмо главни код:

    ```python
    prompt = "Add 2 to 20"

    # питај LLM које алате да користи, ако их има
    functions_to_call = call_llm(prompt, functions)

    # позови предложене функције
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ето, то је био последњи корак, у овом коду смо:

    - Позвали MCP алат преко `call_tool` користећи функцију коју је LLM одлучио да позове на основу нашег упита.
    - Одштампали резултат позива алата на MCP сервер.

#### .NET

1. Погледајмо неки код који ради LLM упит:

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

    У претходном коду смо:

    - Преузели алате са MCP сервера, `var tools = await GetMcpTools()`.
    - Дефинисали кориснички упит `userMessage`.
    - Конструисали објекат опција који указује на модел и алате.
    - Послали захтев LLM-у.

2. Један последњи корак, видимо да ли LLM мисли да треба позвати неку функцију:

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

    У претходном коду смо:

    - Прошли кроз листу позива функција.
    - За сваки позив алата, извукли назив и аргументе и позвали алат на MCP серверу користећи MCP клијента. Коначно одштампали резултате.

Ево кода у целини:

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
    // Изврши захтеве на природном језику који аутоматски користе MCP алате
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

- Користили једноставне упите на природном језику да комуницирамо са алатима MCP сервера
- LangChain4j фрејмворк аутоматски управља:
  - Претварањем корисничких упита у позиве алата када је то потребно
  - Позивањем одговарајућих MCP алата базираних на LLM одлуци
  - Управљањем током разговора између LLM-а и MCP сервера
- Метод `bot.chat()` враћа одговоре на природном језику који могу укључити резултате извођења MCP алата
- Овај приступ пружа беспрекорно корисничко искуство где корисници не морају да знају о спољашњој MCP имплементацији

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

#### Rust

Овде се дешава највећи део рада. Позваћемо LLM са почетним корисничким упитом, онда обрадити одговор да видимо да ли треба позвати неке алате. Ако да, позваћемо те алате и наставити разговор са LLM-ом док више не буде потреба за позивом алата и добијемо коначни одговор.


Направићемо више позива ка LLM, па хајде да дефинишемо функцију која ће обрадити позив LLM-а. Додајте следећу функцију у ваш `main.rs` фајл:

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

Ова функција узима LLM клијента, листу порука (укључујући кориснички упит), алате са MCP сервера и шаље захтев ка LLM-у, враћајући одговор.

Одговор из LLM-а ће садржати низ `choices`. Потребно је обрадити резултат да бисмо видели да ли постоје неки `tool_calls`. Ово нам говори да LLM тражи да се позове одређени алат са аргументима. Додајте следећи код на дно вашег `main.rs` фајла да дефинишете функцију која ће обрадити одговор LLM-а:

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

    // Испиши садржај ако је доступан
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обради позиве алата
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Додај поруку асистента

        // Изврши сваки позив алата
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Додај резултат алата у поруке
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Настави разговор са резултатима алата
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

Ако су присутни `tool_calls`, она извлачи информације о алату, позива MCP сервер са захтевом за алат и додаје резултате у поруке разговора. Затим наставља разговор са LLM-ом, а поруке се ажурирају са одговором асистента и резултатима позива алата.

Да бисмо извукли информације о позиву алата које LLM враћа за MCP позиве, додаћемо још једну помоћну функцију која ће издвојити све што је потребно за извршење позива. Додајте следећи код на дно вашег `main.rs` фајла:

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

Са свим деловима на месту, сада можемо обрадити почетни кориснички упит и позвати LLM. Ажурирајте вашу `main` функцију да укључи следећи код:

```rust
// LLM разговор са позивима алата
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

Ово ће послати упит LLM-у са почетним корисничким питањем за збир два броја и обрадити одговор да динамички управља позивима алата.

Сјајно, успели сте!

## Задатак

Узмите код из вежбе и проширите сервер додатним алатима. Затим направите клијента са LLM-ом, као у вежби, и тестирајте га са различитим упитима да бисте били сигурни да се сви ваши серверски алати позивају динамички. Овај начин изградње клијента омогућава крајњем кориснику одлично корисничко искуство јер може да користи упите, уместо тачних команди клијента, и да не буде свестан било каквих MCP позива ка серверу.

## Решење

[Решење](./solution/README.md)

## Кључне поуке

- Додавање LLM-а вашем клијенту пружа бољи начин да корисници комуницирају са MCP серверима.
- Потребно је конвертовати одговор MCP сервера у нешто што LLM може да разуме.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.Net калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python)
- [Rust калкулатор](../../../../03-GettingStarted/samples/rust)

## Додатни ресурси

## Шта следи

- Следеће: [Конзумирање сервера користећи Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
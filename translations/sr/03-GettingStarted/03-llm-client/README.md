# Креирање клијента са LLM

До сада сте видели како се креира сервер и клијент. Клијент је могао да позива сервер експлицитно да наброји његове алате, ресурсe и упите. Међутим, ово није баш практичан приступ. Ваши корисници живе у агенцијској ери и очекују да користе упите и комуницирају са LLM-ом уместо тога. Немају ништа против да ли користите MCP за складиштење ваших могућности; они једноставно очекују да комуницирају природним језиком. Па како то да решимо? Решење је да додамо LLM клијенту.

## Преглед

У овој лекцији фокусирамо се на додавање LLM-а вашем клијенту и показујемо како то пружа боље корисничко искуство.

## Циљеви учења

До краја ове лекције, моћи ћете да:

- Креирате клијента са LLM-ом.
- Беспрекорно комуницирате са MCP сервером користећи LLM.
- Пружите боље корисничко искуство са стране клијента.

## Приступ

Покушајмо да разумемо приступ који треба да предузмемо. Додавање LLM-а звучи једноставно, али да ли ћемо то заиста урадити?

Ево како ће клијент комуницирати са сервером:

1. Успоставити везу са сервером.

1. Набројати могућности, упите, ресурсе и алате, и сачувати њихову шему.

1. Додати LLM и проследити сачуване могућности и њихову шему у формату који LLM разуме.

1. Обрадити кориснички упит тако што ћемо га проследити LLM-у заједно са алатима које је клијент набројао.

Супер, сада када разумемо како да то урадимо на високом нивоу, покушајмо у доњем упражњењу.

## Упражњење: Креирање клијента са LLM

У овом упражњењу ћемо научити како да додамо LLM нашем клијенту.

### Аутентификација коришћењем GitHub Personal Access Token

Креирање GitHub токена је једноставан процес. Ево како то можете урадити:

- Идите на GitHub Settings – Кликните на своју профилну слику у горњем десном углу и изаберите Settings.
- Идите на Developer Settings – Скролујте доле и кликните на Developer Settings.
- Изаберите Personal Access Tokens – Кликните на Fine-grained tokens па на Generate new token.
- Конфигуришите свој токен – Додајте напомену за референцу, подесите датум истека, и изаберите неопходне опсеге (права). У овом случају обавезно додајте Models дозволу.
- Генеришите и копирајте токен – Кликните на Generate token и обавезно га копирајте одмах пошто га после нећете видети.

### -1- Повезивање на сервер

Хајде најпре да креирамо наш клијент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Увезите zod за валидацију шеме

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

У претходном коду смо:

- Импортовали потребне библиотеке
- Креирали класу са два члана, `client` и `openai` који ће нам помоћи да управљамо клијентом и комуницирамо са LLM-ом
- Конфигурисали нашу LLM инстанцу да користи GitHub Models тако што смо поставили `baseUrl` да упућује на inference API

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Креирај параметре сервера за stdio везу
server_params = StdioServerParameters(
    command="mcp",  # Извршна датотека
    args=["run", "server.py"],  # Опциони аргументи командне линије
    env=None,  # Опционе променљиве окружења
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

У претходном коду смо:

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

Прво, потребно је да додате LangChain4j зависности у ваш `pom.xml` фајл. Додајте ове зависности за омогућавање MCP интеграције и подршку за GitHub Models:

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

Затим креирајте ваш Java клијент класu:

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
    
    public static void main(String[] args) throws Exception {        // Конфигуришите ЛЛМ да користи GitHub моделе
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Креирајте МЦП транспорт за повезивање са сервером
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Креирајте МЦП клијента
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

У претходном коду смо:

- **Додали LangChain4j зависности**: Потребне за MCP интеграцију, OpenAI званичног клијента и подршку GitHub Models
- **Импортовали LangChain4j библиотеке**: За MCP интеграцију и функционалност OpenAI chat модела
- **Креирали `ChatLanguageModel`**: Конфигурисан да користи GitHub Models са вашим GitHub токеном
- **Подесили HTTP транспорт**: Користећи Server-Sent Events (SSE) за повезивање са MCP сервером
- **Креирали MCP клијента**: Који ће управљати комуникацијом са сервером
- **Користили LangChain4j уграђену MCP подршку**: Која поједностављује интеграцију између LLM и MCP сервера

#### Rust

Овај пример претпоставља да имате Rust базиран MCP сервер који ради. Ако га немате, погледајте [01-first-server](../01-first-server/README.md) лекцију да креирате сервер.

Када имате ваш Rust MCP сервер, отворите терминал и идите у исти директоријум као и сервер. Потом покрените следећу команду да бисте креирали нови LLM клијент пројекат:

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
> Званична Rust библиотека за OpenAI не постоји, али `async-openai` crate је [заједничка одржавана библиотека](https://platform.openai.com/docs/libraries/rust#rust) која се често користи.

Отворите `src/main.rs` фајл и замените његову садржину следећим кодом:

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

    // Подеси OpenAI клијента
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Подеси MCP клијента
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

    // ЗА РАДУ: Добијте листу алата MCP

    // ЗА РАДУ: LLM разговор са позивима алата

    Ok(())
}
```

Овај код поставља основну Rust апликацију која ће се повезивати са MCP сервером и GitHub Models за LLM интеракције.

> [!IMPORTANT]
> Обавезно поставите `OPENAI_API_KEY` променљиву окружења са вашим GitHub токеном пре покретања апликације.

Сјајно, за наш следећи корак, хајде да набројимо могућности на серверу.

### -2- Набројати могућности сервера

Сада ћемо се повезати на сервер и затражити његове могућности:

#### TypeScript

У истој класи додајте следеће методе:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // набрајање алата
    const toolsResult = await this.client.listTools();
}
```

У претходном коду смо:

- Додали код за повезивање са сервером, `connectToServer`.
- Креирали `run` метод одговоран за руковање током апликације. До сада само набраја алате, али ћемо ускоро додати више.

#### Python

```python
# Прикажите доступне ресурсе
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Прикажите доступне алате
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ево шта смо додали:

- Набрајање ресурса и алата и штампање их. За алате смо такође набројали `inputSchema` који касније користимо.

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
- За сваки алат набројали име, опис и његову шему. Ово последње ћемо користити да би ускоро позвали алате.

#### Java

```java
// Креирајте провајдера алата који аутоматски открива MCP алате
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Провајдер MCP алата аутоматски обезбеђује:
// - Листање доступних алата са MCP сервера
// - Претварање шема MCP алата у LangChain4j формат
// - Управљање извршавањем алата и одговорима
```

У претходном коду смо:

- Креирали `McpToolProvider` који аутоматски открива и региструје све алате са MCP сервера
- Провајдер алата управља конверзијом између MCP алат шема и LangChain4j формата алата интерно
- Овај приступ апстрахује ручно набрајање алата и процес конверзије

#### Rust

Пребирање алата са MCP сервера се ради коришћењем `list_tools` метода. У вашој `main` функцији, након постављања MCP клијента, додајте следећи код:

```rust
// Преузмите листу МЦП алата
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертовање могућности сервера у LLM алате

Следећи корак након набрајања могућности сервера је да их конвертујемо у формат који LLM разуме. Када то урадимо, можемо ове могућности пружити као алате нашем LLM-у.

#### TypeScript

1. Додајте следећи код за конверзију одговора са MCP сервера у формат алата који LLM може користити:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Креирајте зод шему на основу улазне схеме
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Јасно поставите тип на "функција"
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

    Горњи код узима одговор са MCP сервера и конвертује га у дефиницију алата коју LLM може да разуме.

1. Хајде да уредимо `run` методу да наброји могућности сервера:

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

    У претходном коду, ажурирали смо `run` метод да прође кроз резултат и за сваки унос позове `openAiToolAdapter`.

#### Python

1. Прво, хајде да направимо следећу конверзијску функцију

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

    У функцији `convert_to_llm_tools` узимамо MCP одговор о алату и конвертујемо га у формат који LLM разуме.

1. Следеће, ажурирајмо наш клијентски код да искористи ову функцију овако:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Овде додајемо позив на `convert_to_llm_tool` да конвертујемо MCP алат у нешто што касније можемо проследити LLM-у.

#### .NET

1. Додајмо код за конвертовање MCP одговора у нешто што LLM разуме

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

- Креирали функцију `ConvertFrom` која узима име, опис и улазну шему.
- Дефинисали функционалност која креира `FunctionDefinition` која се прослеђује `ChatCompletionsDefinition`. Овај последњи део LLM разуме.

1. Хајде да видимо како можемо ажурирати постојећи код да искористи ову функцију:

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
// Креирајте бот интерфејс за интеракцију природним језиком
public interface Bot {
    String chat(String prompt);
}

// Конфигуришите AI сервис са LLM и MCP алатима
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У претходном коду смо:

- Дефинисали једноставан `Bot` интерфејс за комуникацију природним језиком
- Користили LangChain4j `AiServices` да аутоматски повежемо LLM са MCP провајдером алата
- Овај фрејмворк аутоматски обрађује конверзију шеме алата и позив функција иза сцене
- Овај приступ елиминише ручну конверзију алата – LangChain4j управља целокупном сложеношћу претварања MCP алата у LLM-компатибилан формат

#### Rust

Да би конвертовали одговор MCP алата у формат који LLM разуме, додамо помоћну функцију која форматира листу алата. Додајте следећи код у ваш `main.rs` фајл испод `main` функције. Ово ће бити позивано при захтевима LLM-у:

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

Сјајно, сада смо спремни да обрадимо захтеве корисника, па хајде да то урадимо.

### -4- Обрадити кориснички упит

У овом делу кода обрађујемо корисничке захтеве.

#### TypeScript

1. Додајте метод који ћемо користити за позив нашег LLM-а:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Позови алат сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Уради нешто са резултатом
        // ЗА УРАДИТИ

        }
    }
    ```

    У претходном коду смо:

    - Додали методу `callTools`.
    - Метода прегледа LLM одговор и проверава да ли су позвани неки алати:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // позив алата
        }
        ```

    - Позива алат ако LLM указује да треба да се позове:

        ```typescript
        // 2. Позовите алат сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Урадите нешто са резултатом
        // ЗАДАЦИ
        ```

1. Ажурирајте `run` методу да укључи позив на LLM и позив `callTools`:

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

    // 3. Прегледајте одговор LLM-а, за сваки избор проверите да ли има позиве алата
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Сјајно, ево комплетног кода:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортујте зод за валидацију шеме

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можда ће бити потребно променити у овај URL у будућности: https://models.github.ai/inference
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
          // Креирајте зод шему на основу input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Јасно поставите тип као "функција"
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
    
    
          // 2. Позовите алатку сервера
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Урадите нешто са резултатом
          // ЗА УРАДИТИ
    
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
    
        // 1. Прођите кроз LLM одговор, за сваки избор проверите да ли има позиве алатки
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
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Затим, додајмо функцију која ће позвати LLM:

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
            # Опциони параметри
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

    - Проследили наше функције, које смо пронашли на MCP серверу и адаптирали, LLM-у.
    - Затим позвали LLM са тим функцијама.
    - Потом посматрамо резултат да видимо које функције треба позвати, ако уопште.
    - На крају прослеђујемо низ функција за позив.

1. Последњи корак, ажурирајмо наш главни код:

    ```python
    prompt = "Add 2 to 20"

    # питај LLM која алатка треба користити, ако икако треба
    functions_to_call = call_llm(prompt, functions)

    # позови предложене функције
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ето, то је био последњи корак, у коду изнад ми:

    - Позивамо MCP алат преко `call_tool` користећи функцију коју је LLM идентификовао као неопходну на основу нашег упита.
    - Исписујемо резултат позива алата са MCP сервера.

#### .NET

1. Погледајмо код за извршавање LLM упита:

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
    - Конструисали опције са подешеним моделом и алатима.
    - Послали захтев LLM-у.

1. Још један корак, видимо да ли LLM мисли да треба да позовемо функцију:

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

    - Пролазили кроз листу позива функција.
    - За сваки позив алата, издвојили име и аргументе и позвали алат на MCP серверу користећи MCP клијента. На крају исписали резултате.

Ево комплетног кода:

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
    // Изврши захтеве на природном језику који аутоматски користе МЦП алате
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

- Користили једноставне природнојезичке упите за интеракцију са MCP сервер алатима
- LangChain4j фрејмворк аутоматски обрађује:
  - Конверзију корисничких упита у позиве алата кад је потребно
  - Позива одговарајуће MCP алате на основу одлуке LLM-а
  - Управљање током конверзације између LLM-а и MCP сервера
- `bot.chat()` метод враћа одговоре на природном језику који могу укључивати резултате извршавања MCP алата
- Овај приступ пружа беспрекорно корисничко искуство где корисници не морају да знају за унутрашњу MCP имплементацију

Комплетан пример кода:

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

Овде се одвија већина посла. Позваћемо LLM са почетним корисничким упитом, па ћемо обрадити одговор да видимо да ли треба позвати неке алате. Ако треба, позваћемо те алате и наставити конверзацију са LLM-ом док више не буде потребно позивати алате и док не добијемо коначни одговор.

Планирамо више позива LLM-у, па дефинишимо функцију која ће се тим позивима бавити. Додајте следећу функцију у ваш `main.rs` фајл:

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

Ова функција прима LLM клијента, листу порука (укључујући кориснички упит), алате са MCP сервера, и шаље захтев LLM-у враћајући одговор.
Odgovor od LLM će sadržati niz `choices`. Trebaćemo da obradimo rezultat da vidimo da li postoje bilo kakvi `tool_calls`. Ovo нам даје do znanja da LLM zahteva da se određeni alat pozove sa argumentima. Dodajte sledeći kod na kraj vašeg `main.rs` fajla da definišete funkciju za rukovanje LLM odgovorom:

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

    // Штампај садржај ако је доступан
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

Ako postoje `tool_calls`, izdvajaju se informacije o alatu, poziva MCP server sa zahtevom za alat, i rezultati se dodaju u poruke konverzacije. Zatim se konverzacija nastavlja sa LLM, a poruke se ažuriraju sa odgovorom asistenta i rezultatima poziva alata.

Da bismo izdvojili informacije poziva alata koje LLM vraća za MCP pozive, dodaćemo još jednu pomoćnu funkciju koja izdvaja sve što je potrebno za izvršenje poziva. Dodajte sledeći kod na kraj vašeg `main.rs` fajla:

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

Sa svim potrebnim delovima na mestu, sada možemo da obradimo početni korisnički upit i pozovemo LLM. Ažurirajte svoju `main` funkciju da uključite sledeći kod:

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

Ovo će poslati upit LLM-u sa početnim korisničkim promptom tražeći zbir dva broja, i obradiće odgovor da dinamički rukuje pozivima alata.

Odlično, uspeli ste!

## Zadatak

Uzmite kod iz vežbe i proširite server sa još nekoliko alata. Zatim kreirajte klijenta sa LLM-om, kao u vežbi, i testirajte ga sa različitim upitima da biste bili sigurni da se svi alati servera dinamički pozivaju. Ovaj način pravljenja klijenta znači da krajnji korisnik ima sjajno korisničko iskustvo jer može da koristi prirodne upite umesto preciznih komandi klijenta i ne mora biti svestan da se MCP server uopšte poziva.

## Rešenje

[Solution](./solution/README.md)

## Ključne tačke

- Dodavanje LLM-a u vaš klijent pruža bolji način za korisnike da interaguju sa MCP Serverima.
- Potrebno je konvertovati odgovor MCP Servera u nešto što LLM može da razume.

## Primeri

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Dodatni resursi

## Šta sledi

- Sledeće: [Korišćenje servera pomoću Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање**:  
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква непоразумевања или погрешне интерпретације које могу настати коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
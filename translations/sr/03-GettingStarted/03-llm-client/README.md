# Креирање клијента са LLM

До сада сте видели како да креирате сервер и клијента. Клијент је могао да позове сервер експлицитно да наброји његове алате, ресурсе и упите. Међутим, ово није веома практичан приступ. Ваши корисници живе у ери агената и очекују да користе упите и комуницирају са LLM-ом. Немају бригу око тога да ли користите MCP за складиштење својих могућности; они једноставно очекују да интерагују користећи природни језик. Како да решимо овај проблем? Решење је да додамо LLM клијенту.

## Преглед

У овом поглављу фокусирамо се на додавање LLM-а вашем клијенту и показујемо како то пружа много боље искуство за вашег корисника.

## Циљеви учења

До краја овог поглавља, моћи ћете да:

- Креирате клијента са LLM-ом.
- Беспрекорно интерагујете са MCP сервером користећи LLM.
- Пружите боље искуство крајњег корисника на клијентској страни.

## Приступ

Покушајмо да разумемо приступ који треба да применимо. Додавање LLM-а звучи једноставно, али да ли ћемо то заиста и урадити?

Ево како ће клијент интераговати са сервером:

1. Успоставити везу са сервером.

2. Набројати могућности, упите, ресурсе и алате, и сачувати њихову шему.

3. Додати LLM и проследити сачуване могућности и њихову шему у формату који LLM разуме.

4. Обрадити кориснички упит прослеђујући га LLM-у заједно са алатима које је клијент набројао.

Одлично, сада када разумемо како можемо то урадити на високом нивоу, хајде да то испробамо у доњој вежби.

## Вежба: Креирање клијента са LLM

У овој вежби научићемо како да додамо LLM нашем клијенту.

### Аутентикација коришћењем GitHub Personal Access Token

Креирање GitHub токена је једноставан процес. Ево како то можете урадити:

- Идите у GitHub Settings – Кликните на своју слику профила у горњем десном углу и изаберите Settings.
- Навигација до Developer Settings – Скролујте надоле и кликните на Developer Settings.
- Изаберите Personal Access Tokens – Кликните на Fine-grained tokens и затим Generate new token.
- Конфигуришите ваш токен – Додајте белешку за референцу, подесите датум истека и изаберите потребне опсеге (овлашћења). У овом случају обавезно додајте Models овлашћење.
- Генеришите и копирајте токен – Кликните Generate token и обавезно га одмах копирајте јер га касније нећете моћи видети поново.

### -1- Повезивање са сервером

Хајде прво да креирамо наш клијент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Увези зод за валидацију шеме

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

- Увезли потребне библиотеке
- Креирали класу са два члана, `client` и `openai`, која ће нам помоћи да управљамо клијентом и интерагујемо са LLM-ом, респективно.
- Конфигурисали нашу LLM инстанцу да користи GitHub Models тако што смо поставили `baseUrl` да показује на inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Креирајте серверске параметре за стандардну улазно-излазну везу
server_params = StdioServerParameters(
    command="mcp",  # Извршна датотека
    args=["run", "server.py"],  # Опционални аргументи командне линије
    env=None,  # Опционалне променљиве окружења
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Иницијализација везе
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

Прво ћете морати да додате LangChain4j зависности у ваш `pom.xml` фајл. Додајте ове зависности да омогућите MCP интеграцију и подршку за GitHub Models:

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

Затим креирајте ваш Java клиент класу:

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
    
    public static void main(String[] args) throws Exception {        // Конфигуришите LLM да користи GitHub моделе
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Направите MCP транспорт за повезивање са сервером
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Направите MCP клијента
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

У претходном коду смо:

- **Додали LangChain4j зависности**: Потребне за MCP интеграцију, OpenAI званичног клијента и подршку за GitHub Models
- **Увезли LangChain4j библиотеке**: За MCP интеграцију и OpenAI чат модел функционалност
- **Креирали `ChatLanguageModel`**: Конфигурисан да користи GitHub Models са вашим GitHub токеном
- **Поставили HTTP транспорт**: Користећи Server-Sent Events (SSE) за повезивање на MCP сервер
- **Креирали MCP клијента**: Који управља комуникацијом са сервером
- **Користили LangChain4j уграђену MCP подршку**: Која поједностављује интеграцију између LLM-а и MCP сервера

#### Rust

Овај пример претпоставља да имате Rust базиран MCP сервер који ради. Ако га немате, вратите се на [01-first-server](../01-first-server/README.md) лекцију ради креирања сервера.

Када имате ваш Rust MCP сервер, отворите терминал и идите у исти директоријум као и сервер. Затим покрените следећу команду да креирате нови LLM клијент пројекат:

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
> Не постоји званична Rust библиотека за OpenAI, међутим, `async-openai` crate је [задржавана библиотека у заједници](https://platform.openai.com/docs/libraries/rust#rust) која се често користи.

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

    // ЗА УРАДИТИ: Набавити листу алата MCP-а

    // ЗА УРАДИТИ: LLM разговор са позивима алата

    Ok(())
}
```

Овај код поставља основну Rust апликацију која ће се повезати на MCP сервер и GitHub Models ради LLM интеракција.

> [!IMPORTANT]
> Обавезно подесите `OPENAI_API_KEY` околинску променљиву са вашим GitHub токеном пре покретања апликације.

Одлично, за наш следећи корак, хајде да набројимо могућности на серверу.

### -2- Набрајање могућности сервера

Сада ћемо се повезати са сервером и питати за његове могућности:

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
- Креирали `run` метод који је задужен за управљање током наше апликације. До сада само набраја алате али ускоро ћемо додати више.

#### Python

```python
# Наведи доступне ресурсе
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Наведи доступне алате
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ево шта смо додали:

- Набрајање ресурса и алата и исписивање тих података. За алате смо такође набројали `inputSchema` који ћемо касније користити.

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
- За сваки алат набројали име, опис и његову шему. Ово последње ћемо користити да ускоро позовемо алате.

#### Java

```java
// Креирајте провајдера алата који аутоматски открива MCP алате
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP провајдер алата аутоматски управља:
// - Листање доступних алата са MCP сервера
// - Конвертовање шема MCP алата у LangChain4j формат
// - Управљање извршењем алата и одговорима
```

У претходном коду смо:

- Креирали `McpToolProvider` који аутоматски открива и региструје све алате са MCP сервера
- Провајдер алата унутрашње управља конверзијом између MCP алат шема и LangChain4j алат формата
- Овај приступ апстрахује ручно набрајање алата и процес конверзије

#### Rust

Добијање алата са MCP сервера се ради коришћењем `list_tools` методе. У вашој `main` функцији, након подешавања MCP клијента, додајте следећи код:

```rust
// Добити листу МЦП алата
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертовање могућности сервера у LLM алате

Следећи корак након набрајања могућности сервера је конвертовање у формат који LLM разуме. Када то урадимо, можемо ове могућности понудити као алате нашем LLM-у.

#### TypeScript

1. Додајте следећи код за конвертовање одговора са MCP сервера у формат алата који LLM може користити:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Креирајте зод шему на основу улазне шеме
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Јасно подесите тип на "function"
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

    Горњи код преузима одговор са MCP сервера и конвертује га у дефиницију алата коју LLM може разумети.

1. Ажурирајмо `run` метод да набројимо могућности сервера:

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

    У претходном коду смо ажурирали `run` метод тако што смо пролазили кроз резултат и за сваки унос позвали `openAiToolAdapter`.

#### Python

1. Прво, хајде да направимо следећу конверзиону функцију

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

    У функцији `convert_to_llm_tools` претварамо MCP алат у формат који LLM разуме.

1. Сада ажурирајмо наш клијентски код да користи ову функцију овако:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Овде додамо позив `convert_to_llm_tool` да конвертујемо MCP одговор у нешто што касније можемо проследити LLM-у.

#### .NET

1. Додајмо код за конверзију MCP алат одговора у формат који LLM може разумети

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
- Дефинисали функционалност која креира `FunctionDefinition` који се прослеђује `ChatCompletionsDefinition`. Ово последње LLM може разумети.

1. Ајде да видимо како да ажурирамо постојећи код да искористи ову функцију:

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
// Креирајте Бот интерфејс за интеракцију на природном језику
public interface Bot {
    String chat(String prompt);
}

// Конфигуришите AI услугу са LLM и MCP алатима
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У претходном коду смо:

- Дефинисали једноставан `Bot` интерфејс за интеракцију на природном језику
- Користили LangChain4j `AiServices` да аутоматски повежемо LLM са MCP провајдером алата
- Фрејмворк аутоматски управља конверзијом шема алата и позивом функција иза сцене
- Овај приступ елиминише ручну конверзију алата - LangChain4j управља свом комплексношћу конвертовања MCP алата у LLM-компатибилан формат

#### Rust

Да бисмо конвертовали MCP одговор у формат који LLM разуме, додамо помоћну функцију која форматира листу алата. Додајте следећи код у ваш `main.rs` фајл испод `main` функције. Ово ће се позивати када правимо захтеве ка LLM-у:

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

Одлично, сада смо спремни да обрадимо корисничке захтеве, па да пређемо на то.

### -4- Обрада корисничког упита

У овом делу кода ћемо обрадити корисничке захтеве.

#### TypeScript

1. Додајте метод који ће се користити за позив нашег LLM-а:

    ```typescript
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
        // ЗА УРАДИТИ

        }
    }
    ```

    У претходном коду смо:

    - Додали метод `callTools`.
    - Метод узима LLM одговор и проверава који алати су позвани, ако их има:

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
        // 2. Позови серверски алат
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Уради нешто са резултатом
        // ЗА УРАДИТИ
        ```

1. Ажурирајте `run` метод да укључи позиве на LLM и позив `callTools`:

    ```typescript

    // 1. Направите поруке које су унос за LLM
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

    // 3. Прођите кроз одговор LLM-а, за сваки избор, проверите да ли има позиве алата
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Одлично, ево целог кода:

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
            baseURL: "https://models.inference.ai.azure.com", // можда ће бити потребно променити на овај URL у будућности: https://models.github.ai/inference
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
          // Креирај зод шему засновану на input_schema
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
    
    
          // 2. Позови серверски алат
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Уради нешто са резултатом
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Прегледај одговор LLM, за сваки избор провери да ли има позиве алата
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

1. Додајмо увозе потребне за позив LLM-а

    ```python
    # ллм
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Затим, додајмо функцију која позива LLM:

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

    - Проследили функције које смо нашли на MCP серверу и конвертовали LLM-у.
    - Затим смо позвали LLM са тим функцијама.
    - Затим прегледамо резултат да видимо које функције треба позвати, ако их има.
    - На крају, прослеђујемо низ функција које треба позвати.

1. Последњи корак, ажурирајмо наш главни код:

    ```python
    prompt = "Add 2 to 20"

    # питај LLM које алате да користи, ако их има
    functions_to_call = call_llm(prompt, functions)

    # позови предложене функције
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    То је био последњи корак, у горњем коду ми:

    - Позивамо MCP алат преко `call_tool` користећи функцију за коју је LLM мислио да треба да буде позвана на основу нашег упита.
    - Штампамо резултат позива алата са MCP сервера.

#### .NET

1. Прикажимо неки код за слање LLM упита:

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
    - Конструисали опције са моделом и алатима.
    - Послали захтев LLM-у.

1. Још један корак, видимо да ли LLM мисли да треба позвати функцију:

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
    - За сваки позив алата, извукли име и аргументе и позвали алат на MCP серверу користећи MCP клијента. На крају штампали резултате.

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Извршавајте захтеве на природном језику који аутоматски користе MCP алате
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

- Користили једноставне упите на природном језику за интеракцију са MCP алатима на серверу
- LangChain4j фрејмворк аутоматски управља:
  - Конвертовањем корисничких упита у позиве алата када је потребно
  - Позивом одговарајућих MCP алата према одлуци LLM-а
  - Управљањем током разговора између LLM-а и MCP сервера
- Метод `bot.chat()` враћа одговоре на природном језику који могу укључивати резултате извршења MCP алата
- Овај приступ пружа беспрекорно корисничко искуство где корисници не морају да знају о унутрашњој имплементацији MCP-а

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

Овде се већина посла дешава. Позваћемо LLM са почетним корисничким упитом, затим обрадити одговор да видимо да ли је потребно позвати неке алате. Ако јесте, позваћемо те алате и наставити разговор са LLM-ом све док не буде више потреба за позивима алата и док не добијемо коначни одговор.

Планирамо више позива LLM-у, па хајде да дефинишемо функцију која ће управљати позивима LLM-а. Додајте следећу функцију у ваш `main.rs` фајл:

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

Ова функција узима LLM клијента, листу порука (укључујући кориснички упит), алате са MCP сервера, шаље захтев LLM-у и враћа одговор.
Одговор од LLM ће садржати низ `choices`. Потребно је да обрадимо резултат да видимо да ли постоје `tool_calls`. Ово нам говори да LLM захтева позивање одређеног алата са аргументима. Додајте следећи код на дно вашег `main.rs` фајла да бисте дефинисали функцију која ће обрадити LLM одговор:

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
  
Ако постоје `tool_calls`, извлачи информације о алату, позива MCP сервер са захтевом алата и додаје резултате у поруке конверзације. Затим наставља конверзацију са LLM и поруке се ажурирају са одговором асистента и резултатима позива алата.

Да бисмо извукли информације о позиву алата које LLM враћа за MCP позиве, додаћемо још једну помоћну функцију која ће извући све што је потребно за позив. Додајте следећи код на дно вашег `main.rs` фајла:

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
  
Са свим деловима на месту, сада можемо обрадити почетни кориснички упит и позвати LLM. Ажурирајте вашу `main` функцију да укључује следећи код:

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
  
Ово ће упитати LLM са почетним корисничким упитом који тражи збир два броја, и обрадиће одговор да динамички управља позивима алата.

Сјајно, успели сте!

## Задатак

Узмите код из вежбе и изградите сервер са још више алата. Затим направите клијента са LLM-ом, као у вежби, и тестирате га са различитим упитима да бисте били сигурни да се сви ваши серверски алати динамички позивају. Оваквим приступом изградње клијента крајњи корисник има одлично корисничко искуство јер може користити упите уместо тачних команди клијента и без знања о MCP серверу који се позива.

## Решење

[Решење](/03-GettingStarted/03-llm-client/solution/README.md)

## Кључне појединости

- Додавање LLM-а вашем клијенту пружа бољи начин за интеракцију корисника са MCP серверима.
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

- Следеће: [Коришћење сервера у Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразуми или погрешна тумачења настала употребом овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
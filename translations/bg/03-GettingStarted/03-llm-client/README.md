# Създаване на клиент с LLM

> [!NOTE]
> Примерите за Java клиент се свързват чрез наследения HTTP+SSE транспорт и
> насочват MCP `2025-11-25` SDK API-та. Използвайте SDK съвместим с `2026-07-28` и
> Streamable HTTP за нови отдалечени клиенти.

Досега сте видели как да създадете сървър и клиент. Клиентът беше в състояние да извика сървъра изрично, за да изброи неговите инструменти, ресурси и подсказки. Въпреки това, този подход не е много практичен. Вашите потребители живеят в агентичното време и очакват да използват подсказки и да комуникират с LLM. Те не се интересуват дали използвате MCP за съхранение на вашите възможности; те просто очакват да взаимодействат чрез естествен език. Как да решим това? Решението е да добавим LLM към клиента.

## Преглед

В този урок се фокусираме върху добавянето на LLM към вашия клиент и показваме как това осигурява много по-добро изживяване за потребителя.

## Учебни цели

До края на този урок ще можете:

- Да създадете клиент с LLM.
- Безпроблемно да взаимодействате със сървър MCP чрез LLM.
- Да предоставите по-добро потребителско изживяване на клиентската страна.

## Подход

Нека се опитаме да разберем подхода, който трябва да вземем. Добавянето на LLM звучи просто, но ще го направим ли наистина?

Ето как клиентът ще взаимодейства със сървъра:

1. Установяване на връзка със сървъра.

1. Изброяване на възможностите, подсказките, ресурсите и инструментите и записване на тяхната схема.

1. Добавяне на LLM и подаване на запазените възможности и тяхната схема във формат, който LLM разбира.

1. Обработка на потребителска подсказка чрез подаването ѝ към LLM заедно с инструментите, изброени от клиента.

Отлично, сега когато разбираме как можем да направим това на високо ниво, нека опитаме в следващото упражнение.

## Упражнение: Създаване на клиент с LLM

В това упражнение ще научим как да добавим LLM към нашия клиент.

### Оторизация чрез GitHub Personal Access Token

Създаването на GitHub токен е лесен процес. Ето как можете да го направите:

- Отидете в GitHub Settings – Кликнете върху профилната си снимка в горния десен ъгъл и изберете Settings.
- Отидете на Developer Settings – Превъртете надолу и кликнете на Developer Settings.
- Изберете Personal Access Tokens – Кликнете на Fine-grained tokens и след това Generate new token.
- Конфигурирайте своя токен – Добавете бележка за справка, задайте дата на изтичане и изберете необходимите обхвати (права). В този случай не забравяйте да добавите разрешението Models.
- Генерирайте и копирайте токена – Натиснете Generate token и се уверете, че го копирате веднага, защото няма да можете да го видите отново.

### -1- Свържете се със сървъра

Нека първо създадем нашия клиент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортиране на zod за валидиране на схема

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

В горния код ние:

- Импортирахме нужните библиотеки
- Създадохме клас с два член-променливи, `client` и `openai`, които ще ни помагат да управляваме клиент и да взаимодействаме с LLM съответно.
- Конфигурирахме нашия LLM инстанция да използва GitHub Models чрез задаване на `baseUrl` към inference API-то.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Създаване на сървърни параметри за stdio връзка
server_params = StdioServerParameters(
    command="mcp",  # Изпълним файл
    args=["run", "server.py"],  # Незадължителни аргументи от командния ред
    env=None,  # Незадължителни променливи на средата
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Инициализиране на връзката
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

В горния код ние:

- Импортирахме нужните библиотеки за MCP
- Създадохме клиент

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

Първо, трябва да добавите зависимостите на LangChain4j към вашия `pom.xml` файл. Добавете тези зависимости, за да активирате интеграцията с MCP и OpenAI-съвместимото MiniMax API:

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

задайте своя MiniMax API ключ и, евентуално, endpoint и модел.
`MINIMAX_MODEL_ID` поддържа `MiniMax-M3` и `MiniMax-M2.7`. Ако
`OPENAI_BASE_URL` не е зададен, `MINIMAX_REGION` поддържа `global_en` и `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

За да изберете endpoint по регион, пропуснете `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

След това създайте вашия Java клиент клас:

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

        // Създаване на MCP транспорт за връзка със сървър
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Създаване на MCP клиент
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

В горния код ние:

- **Добавихме зависимостите на LangChain4j**: Необходими за интеграция с MCP и OpenAI-съвместимото MiniMax API
- **Импортирахме библиотеките на LangChain4j**: За интеграция с MCP и функционалността на OpenAI чат модел
- **Създадохме `ChatLanguageModel`**: Конфигуриран да използва MiniMax с вашия MiniMax API ключ, endpoint и поддържан модел ID
- **Настроихме HTTP транспорта**: Използвайки Server-Sent Events (SSE) за връзка със сървъра MCP
- **Създадохме MCP клиент**: Който ще обработва комуникацията със сървъра
- **Използвахме вградена поддръжка на MCP в LangChain4j**: Която опростява интеграцията между LLM и MCP сървъри

#### Rust

Този пример предполага, че имате работещ Rust базиран MCP сървър. Ако нямате, върнете се към урока [01-first-server](../01-first-server/README.md), за да създадете сървъра.

След като имате своя Rust MCP сървър, отворете терминал и навигирайте до същата директория като сървъра. След това изпълнете следната команда, за да създадете нов LLM клиент проект:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Добавете следните зависимости в `Cargo.toml` файла си:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Няма официална Rust библиотека за OpenAI, но `async-openai` crate е [общностно поддържана библиотека](https://platform.openai.com/docs/libraries/rust#rust), която често се използва.

Отворете файла `src/main.rs` и заменете съдържанието му със следния код:

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
    // Начално съобщение
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Настройка на OpenAI клиент
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Настройка на MCP клиент
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

    // TODO: Вземете списъка с инструменти на MCP

    // TODO: Разговор с LLM с извиквания на инструменти

    Ok(())
}
```

Този код създава базово Rust приложение, което ще се свърже със сървър MCP и GitHub Models за взаимодействия с LLM.

> [!IMPORTANT]
> Уверете се, че сте зададете променливата на средата `OPENAI_API_KEY` с вашия GitHub токен преди да стартирате приложението.

Отлично, за следващата стъпка нека изброим възможностите на сървъра.

### -2- Изброяване на възможностите на сървъра

Сега ще се свържем със сървъра и ще поискаме неговите възможности:

#### Typescript

В същия клас добавете следните методи:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // изброяване на инструменти
    const toolsResult = await this.client.listTools();
}
```

В горния код ние:

- Добавихме код за свързване към сървъра, `connectToServer`.
- Създадохме метод `run`, отговарящ за управлението на нашия поток на приложение. До момента той само изброява инструментите, но скоро ще добавим още функционалности.

#### Python

```python
# Изброяване на наличните ресурси
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Изброяване на наличните инструменти
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ето какво добавихме:

- Изброяване на ресурси и инструменти и отпечатването им. За инструментите също така изброяваме `inputSchema`, което ще използваме по-късно.

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


В предходния код ние:

- Изброихме инструментите, налични на MCP сървъра
- За всеки инструмент изброихме име, описание и неговата схема. Последното е нещо, което ще използваме скоро, за да извикваме инструментите.

#### Java

```java
// Създайте доставчик на инструменти, който автоматично открива MCP инструменти
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Доставчикът на MCP инструменти автоматично обработва:
// - Изброяване на налични инструменти от MCP сървъра
// - Конвертиране на схеми на MCP инструменти във формат LangChain4j
// - Управление на изпълнението на инструменти и отговори
```

В предходния код ние:

- Създадохме `McpToolProvider`, който автоматично открива и регистрира всички инструменти от MCP сървъра
- Доставчикът на инструменти автоматично управлява преобразуването между схемите на MCP инструментите и формата на инструментите на LangChain4j
- Този подход абстрахира ръчния процес по изброяване и преобразуване на инструментите

#### Rust

Извличането на инструменти от MCP сървъра се извършва чрез метода `list_tools`. Във вашата функция `main`, след настройването на MCP клиента, добавете следния код:

```rust
// Вземете списък с инструменти MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Преобразуване на възможностите на сървъра в LLM инструменти

Следващата стъпка след изброяването на възможностите на сървъра е да ги преобразуваме във формат, който LLM разбира. След това можем да предоставим тези възможности като инструменти на нашия LLM.

#### TypeScript

1. Добавете следния код, за да преобразувате отговора от MCP сървъра във формат за инструмент, който LLM може да използва:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Създайте zod схема въз основа на input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно задайте типа на "функция"
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

    Горният код взема отговор от MCP сървъра и го преобразува във формат на дефиниция на инструмент, който LLM може да разбере.

2. Нека обновим метода `run`, за да изброим възможностите на сървъра:

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

    В предходния код обновихме метода `run`, така че да премине през резултата и за всяка позиция да извика `openAiToolAdapter`.

#### Python

1. Първо, нека създадем следната функция за преобразуване

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

    В горната функция `convert_to_llm_tools` взимаме отговор от MCP инструмент и го преобразуваме във формат, който LLM може да разбере.

2. След това, нека обновим кода на нашия клиент, за да използва тази функция, както следва:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тук добавяме извикване на `convert_to_llm_tool`, за да преобразуваме отговора от MCP инструмент в нещо, което можем по-късно да подадем на LLM.

#### .NET

1. Добавяме код за преобразуване на отговора от MCP инструмент в нещо, което LLM може да разбере

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

В предходния код ние:

- Създадохме функция `ConvertFrom`, която приема име, описание и входната схема.
- Дефинирахме функционалност, която създава FunctionDefinition, която се подава към ChatCompletionsDefinition. Последното е нещо, което LLM може да разбере.

2. Нека видим как можем да обновим съществуващ код, за да използваме тази функция:

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
// Създайте интерфейс на бот за взаимодействие на естествен език
public interface Bot {
    String chat(String prompt);
}

// Конфигурирайте AI услугата с LLM и MCP инструменти
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

В предходния код ние:

- Дефинирахме прост интерфейс `Bot` за взаимодействия с естествен език
- Използвахме LangChain4j `AiServices` за автоматично свързване на LLM с доставчика на MCP инструменти
- Фреймуъркът автоматично управлява преобразуването на схемата на инструмента и извикването на функции зад кулисите
- Този подход премахва ръчното преобразуване на инструменти - LangChain4j управлява цялата сложност при преобразуването на MCP инструменти във формат съвместим с LLM

#### Rust

За да преобразуваме отговора от MCP инструмента във формат, който LLM може да разбере, ще добавим помощна функция, която форматира списъка с инструменти. Добавете следния код във вашия файл `main.rs` под функцията `main`. Това ще се извиква при правене на заявки към LLM:

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

Отлично, вече сме готови да обработваме заявки от потребители, нека се заемем с това.

### -4- Обработка на заявка от потребител

В тази част на кода ще обработваме заявки от потребители.

#### TypeScript

1. Добавете метод, който ще се използва за извикване на нашия LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Обадете се на инструмента на сървъра
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Направете нещо с резултата
        // TODO

        }
    }
    ```

    В предходния код ние:

    - Добавихме метод `callTools`.
    - Методът приема отговор от LLM и проверява дали има извикани инструменти, ако има:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // извикване на инструмент
        }
        ```

    - Извиква инструмент, ако LLM показва, че трябва да бъде извикан:

        ```typescript
        // 2. Извикайте инструмента на сървъра
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Направете нещо с резултата
        // ЗАДАЧА
        ```

2. Обновете метода `run`, за да включите извиквания към LLM и извикване на `callTools`:

    ```typescript

    // 1. Създайте съобщения, които са вход за LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Извикване на LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Прегледайте отговора на LLM, за всеки избор проверете дали има повиквания на инструменти
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Отлично, нека видим пълния код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортирайте zod за валидация на схеми

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // може да се наложи да се смени на този URL в бъдеще: https://models.github.ai/inference
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
          // Създайте zod схема базирана на input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Явно задайте типа на "function"
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
    
    
          // 2. Извикайте инструмента на сървъра
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Направете нещо с резултата
          // ЗАДАЧА
    
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
    
        // 3. Прегледайте отговора от LLM, за всеки избор проверете дали има повиквания на инструменти
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

1. Нека добавим нужните импорти за извикване на LLM

    ```python
    # голям езиков модел
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. След това, нека добавим функцията, която ще извика LLM:

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
            # По избор параметри
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

    В предходния код ние:

    - Предадохме нашите функции, които намерихме на MCP сървъра и преобразувахме, на LLM.
    - След това извикахме LLM с тези функции.
    - После инспектираме резултата, за да видим кои функции трябва да извикаме, ако има такива.
    - Накрая подаваме масив от функции за извикване.

3. Финална стъпка, нека обновим основния код:

    ```python
    prompt = "Add 2 to 20"

    # попитай големия езиков модел какви инструменти да използва, ако има такива
    functions_to_call = call_llm(prompt, functions)

    # извикай предложените функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ето, това беше финалната стъпка, в горния код ние:

    - Извикваме MCP инструмент чрез `call_tool` използвайки функция, която LLM смята, че трябва да извика въз основа на нашия подканващ текст.
    - Печатаме резултата от извикването на инструмента към MCP Сървъра.

#### .NET

1. Нека покажем малко код за правене на заявка към LLM подканващ текст:

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

    В предходния код ние:

    - Изтеглихме инструменти от MCP сървъра, `var tools = await GetMcpTools()`.
    - Дефинирахме потребителски подканващ текст `userMessage`.
    - Създадохме обект с опции, който посочва модел и инструменти.
    - Направихме заявка към LLM.

2. Последна стъпка, нека видим дали LLM смята, че трябва да се извика функция:

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

    В предходния код ние:

    - Обхождаме списък с извиквания на функции.
    - За всяко извикване на инструмент извличаме име и аргументи и извикваме инструмента на MCP сървъра чрез MCP клиента. Накрая печатаме резултатите.

Ето пълния код:

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
    // Изпълнява заявки на естествен език, които автоматично използват MCP инструменти
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

В предходния код ние:

- Използвахме прости подканващи текстове на естествен език за взаимодействие с инструментите на MCP сървъра
- Фреймуъркът LangChain4j автоматично управлява:
  - Преобразуването на подканващите текстове на потребителя към извиквания на инструменти, когато е необходимо
  - Извикването на съответните MCP инструменти според решението на LLM
  - Управлението на потока на разговор между LLM и MCP сървъра
- Методът `bot.chat()` връща отговори на естествен език, които може да включват резултати от изпълнението на MCP инструменти
- Този подход осигурява безпроблемно потребителско изживяване, при което потребителите не е нужно да знаят за вътрешната реализация на MCP

Пълен примерен код:

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


Тук се случва основната част от работата. Ще извикаме LLM с началния потребителски подсказ, след което ще обработим отговора, за да видим дали трябва да се извикат някакви инструменти. Ако е така, ще извикаме тези инструменти и ще продължим разговора с LLM, докато не се наложи повече извиквания на инструменти и имаме окончателен отговор.

Ще правим множество извиквания към LLM, затова нека дефинираме функция, която да се грижи за извикването на LLM. Добавете следната функция във вашия файл `main.rs`:

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

Тази функция приема клиент LLM, списък със съобщения (включително потребителския подсказ), инструменти от MCP сървъра и изпраща заявка към LLM, върщайки отговора.

Отговорът от LLM ще съдържа масив от `choices`. Ще трябва да обработим резултата, за да видим дали има присъстващи `tool_calls`. Това ни показва, че LLM иска да се извика конкретен инструмент с аргументи. Добавете следния код в края на вашия файл `main.rs`, за да дефинирате функция за обработка на отговора от LLM:

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

    // Отпечатайте съдържанието, ако е налично
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обработка на повиквания към инструменти
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Добавяне на съобщение от асистента

        // Изпълнение на всяко повикване към инструмента
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Добавяне на резултата от инструмента към съобщенията
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Продължете разговора с резултатите от инструмента
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

Ако има `tool_calls`, функцията извлича информацията за инструмента, извиква MCP сървъра със заявката за инструмента и добавя резултатите в съобщенията на разговора. След това продължава разговора с LLM, а съобщенията се актуализират с отговора на асистента и резултатите от извикването на инструмента.

За да извлечем информацията за извикванията на инструменти, която LLM връща за MCP извиквания, ще добавим още една помощна функция, която да извлича всичко необходимо за извършване на извикването. Добавете следния код в края на вашия файл `main.rs`:

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

С всичките части на място вече можем да се справим с началния потребителски подсказ и да извикаме LLM. Актуализирайте вашата функция `main`, за да включите следния код:

```rust
// Разговор на LLM с повиквания към инструменти
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

Това ще запита LLM с началния потребителски подсказ, искащ сумата на две числа, и ще обработи отговора, за да управлява динамично извиквания на инструменти.

Страхотно, успяхте!

## Задача

Вземете кода от упражнението и разширете сървъра с още инструменти. След това създайте клиент с LLM, както в упражнението, и го тествайте с различни подскази, за да се уверите, че всички инструменти на сървъра ви се извикват динамично. Този начин на изграждане на клиент осигурява много добро потребителско изживяване, тъй като потребителят може да използва подскази вместо точни команди и няма да забележи дали MCP сървър се извиква.

## Решение

[Решение](./solution/README.md)

## Основни изводи

- Добавянето на LLM към вашия клиент осигурява по-добър начин потребителите да взаимодействат с MCP сървъри.
- Нужно е да конвертирате отговора от MCP сървъра в нещо, което LLM може да разбере.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.Net калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python)
- [Rust калкулатор](../../../../03-GettingStarted/samples/rust)

## Допълнителни ресурси

## Какво следва

- Следва: [Употреба на сървър с Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
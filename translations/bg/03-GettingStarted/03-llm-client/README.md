# Създаване на клиент с LLM

Досега видяхте как да създадете сървър и клиент. Клиентът можеше експлицитно да извиква сървъра, за да изброи неговите инструменти, ресурси и подкани. Въпреки това, това не е много практичен подход. Потребителите ви живеят в агенцията ера и очакват да използват подкани и да комуникират с LLM вместо това. Те не ги интересува дали използвате MCP за съхранение на вашите възможности; те просто очакват да взаимодействат с естествен език. Как да решим това? Решението е да добавите LLM към клиента.

## Преглед

В този урок се фокусираме върху добавянето на LLM към вашия клиент и показваме как това осигурява много по-добро изживяване за потребителя ви.

## Учебни цели

До края на този урок ще можете:

- Да създадете клиент с LLM.
- Безпроблемно да взаимодействате със сървър MCP, използвайки LLM.
- Да осигурите по-добро потребителско изживяване от страна на клиента.

## Подход

Нека се опитаме да разберем подхода, който трябва да предприемем. Добавянето на LLM звучи просто, но наистина ли ще го направим?

Ето как клиентът ще взаимодейства със сървъра:

1. Установяване на връзка със сървъра.

1. Изброяване на възможности, подкани, ресурси и инструменти и запазване на тяхната схема.

1. Добавяне на LLM и подаване на запазените възможности и техните схеми във формат, който LLM разбира.

1. Обработка на потребителската подкана, като я подаваме на LLM заедно с инструментите, изброени от клиента.

Отлично, сега когато разбираме как можем да направим това на общо ниво, нека го изпробваме в следващото упражнение.

## Упражнение: Създаване на клиент с LLM

В това упражнение ще научим как да добавим LLM към нашия клиент.

### Автентикация с помощта на персонален достъп до GitHub токен

Създаването на токен в GitHub е лесен процес. Ето как можете да го направите:

- Отидете в GitHub Настройки – Кликнете върху снимката на профила си в горния десен ъгъл и изберете Настройки.
- Навигирайте до Настройки за разработчици – Превъртете надолу и кликнете върху Настройки за разработчици.
- Изберете Лични токени за достъп – Кликнете върху Токени с фини настройки и след това Генерирайте нов токен.
- Конфигурирайте вашия токен – Добавете бележка за справка, задайте дата на изтичане и изберете необходимите обхвати (разрешения). В този случай се уверете, че сте добавили разрешение Models.
- Генерирайте и копирайте токена – Кликнете върху Генериране на токен и се уверете, че го копирате веднага, тъй като няма да можете да го видите отново.

### -1- Свързване със сървър

Нека първо създадем нашия клиент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортирайте zod за валидиране на схема

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

- Импортирахме необходимите библиотеки
- Създадохме клас с два члена, `client` и `openai`, които ще ни помогнат да управляваме клиент и да взаимодействаме с LLM съответно.
- Конфигурирахме нашия LLM екземпляр да използва GitHub Models, като зададохме `baseUrl`, сочещ към inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Създаване на сървърни параметри за stdio връзка
server_params = StdioServerParameters(
    command="mcp",  # Изпълним файл
    args=["run", "server.py"],  # Незадължителни аргументи на командния ред
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

- Импортирахме необходимите библиотеки за MCP
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

Първо, трябва да добавите зависимостите на LangChain4j във вашия `pom.xml` файл. Добавете тези зависимости, за да активирате интеграцията на MCP и OpenAI-съвместимия MiniMax API:

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

Задайте вашия MiniMax API ключ и, опционално, крайна точка и модел.
`MINIMAX_MODEL_ID` поддържа `MiniMax-M3` и `MiniMax-M2.7`. Ако
`OPENAI_BASE_URL` не е зададен, `MINIMAX_REGION` поддържа `global_en` и `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

За да изберете крайна точка според региона, пропуснете `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

След това създайте вашия Java клиентски клас:

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

        // Създаване на MCP транспорт за свързване със сървър
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

- **Добавихме зависимости LangChain4j**: Необходими за интеграция с MCP и OpenAI-съвместимия MiniMax API
- **Импортирахме библиотеките LangChain4j**: За интеграция с MCP и функционалност на OpenAI чат модел
- **Създадохме `ChatLanguageModel`**: Конфигуриран да използва MiniMax с вашия MiniMax API ключ, крайна точка и поддържан модел ID
- **Настроихме HTTP транспорт**: Използвайки Server-Sent Events (SSE) за свързване със сървъра MCP
- **Създадохме MCP клиент**: Който ще обработва комуникацията със сървъра
- **Използвахме вградената поддръжка на MCP на LangChain4j**: Което опростява интеграцията между LLM и MCP сървъри

#### Rust

Този пример предполага, че имате работещ MCP сървър базиран на Rust. Ако нямате такъв, върнете се към урока [01-first-server](../01-first-server/README.md), за да създадете сървъра.

След като имате вашия Rust MCP сървър, отворете терминал и навигирайте до същата директория като сървъра. След това изпълнете следната команда, за да създадете нов LLM клиентски проект:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Добавете следните зависимости във вашия `Cargo.toml` файл:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Няма официална Rust библиотека за OpenAI, но `async-openai` crate е [библиотека поддържана от общността](https://platform.openai.com/docs/libraries/rust#rust), която се използва често.

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

    // Настройка на OpenAI клиента
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Настройка на MCP клиента
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

    // ЗАДАЧА: Вземи списък с инструменти на MCP

    // ЗАДАЧА: Разговор с LLM с извиквания на инструменти

    Ok(())
}
```

Този код настройва базово Rust приложение, което ще се свързва със сървър MCP и GitHub Models за LLM взаимодействия.

> [!IMPORTANT]
> Уверете се, че сте задали променливата на средата `OPENAI_API_KEY` с вашия GitHub токен, преди да стартирате приложението.

Отлично, за следващата стъпка, нека изброим възможностите на сървъра.

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

- Добавихме код за свързване със сървъра, `connectToServer`.
- Създадохме метод `run`, отговорен за обработка на потока на нашето приложение. Досега той само изброява инструментите, но скоро ще добавим още.

#### Python

```python
# Избройте наличните ресурси
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Избройте наличните инструменти
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ето какво добавихме:

- Изброяване на ресурси и инструменти и извеждането им. За инструментите също изброяваме `inputSchema`, което ще използваме по-късно.

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

В горния код ние:

- Изброихме инструментите на разположение в MCP сървъра
- За всеки инструмент изброихме име, описание и неговата схема. Последното е нещо, което ще използваме скоро при повикване на инструментите.

#### Java

```java
// Създайте доставчик на инструменти, който автоматично открива MCP инструменти
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Доставчикът на MCP инструменти автоматично управлява:
// - Изброяване на наличните инструменти от MCP сървъра
// - Преобразуване на MCP схемите на инструментите в LangChain4j формат
// - Управление на изпълнението на инструменти и отговори
```

В горния код ние:

- Създадохме `McpToolProvider`, който автоматично открива и регистрира всички инструменти от MCP сървъра
- Провайдърът на инструменти обработва конверсията между схемите на MCP инструменти и формата на LangChain4j инструментите вътрешно
- Този подход абстрахира ръчния процес на изброяване и конвертиране на инструменти

#### Rust

Вземането на инструменти от MCP сървъра се прави чрез метода `list_tools`. Във вашата `main` функция, след като настроите клиента MCP, добавете следния код:

```rust
// Вземете списъка с инструменти MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертиране на възможностите на сървъра в инструменти за LLM

Следващата стъпка след изброяването на възможностите на сървъра е да ги конвертираме в формат, който LLM разбира. След като го направим, можем да предоставим тези възможности като инструменти на нашия LLM.

#### TypeScript

1. Добавете следния код за конвертиране на отговора от MCP сървъра в инструментален формат, който LLM може да използва:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Създайте zod схема въз основа на input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно задайте тип на "function"
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

    Горният код взема отговор от MCP сървъра и го конвертира в инструментална дефиниция, която LLM може да разбере.

2. Нека след това актуализираме метода `run` да изброява възможностите на сървъра:

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

    В горния код сме актуализирали метода `run`, за да минава през резултата и за всяка записа да извиква `openAiToolAdapter`.

#### Python

1. Първо, нека създадем следната конверторна функция

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

    В горната функция `convert_to_llm_tools` взимаме отговора на MCP инструмент и го конвертираме в формат, който LLM може да разбере.

2. След това нека актуализираме кода на клиента да използва тази функция по следния начин:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тук добавяме извикване на `convert_to_llm_tool`, за да конвертираме отговора на MCP инструмента в нещо, което можем да подадем на LLM по-късно.

#### .NET

1. Нека добавим код за конвертиране на отговора на MCP инструмента в нещо, което LLM може да разбере

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

В горния код ние:

- Създадохме функция `ConvertFrom`, която приема име, описание и входна схема.
- Дефинирахме функционалност, която създава FunctionDefinition, която се подава на ChatCompletionsDefinition. Последното е нещо, което LLM може да разбере.

2. Нека видим как можем да актуализираме съществуващ код, за да използваме функцията по-горе:

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

// Конфигурирайте AI услугата с инструменти LLM и MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

В горния код ние:

- Дефинирахме прост интерфейс `Bot` за взаимодействие с естествен език
- Използвахме LangChain4j `AiServices`, за да свържем автоматично LLM с MCP доставчика на инструменти
- Фреймуъркът автоматично обработва преобразуването на схемите на инструментите и извикването на функции зад кулисите
- Този подход елиминира ръчното преобразуване на инструменти - LangChain4j обработва цялата сложност по преобразуването на MCP инструментите в формат, съвместим с LLM

#### Rust

За да конвертираме отговора на MCP инструмента в формат, който LLM може да разбере, ще добавим помощна функция, която форматира списъка с инструменти. Добавете следния код във вашия `main.rs` файл под функцията `main`. Това ще се извиква при правене на заявки към LLM:

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

Отлично, вече сме подготвени да обработваме потребителски заявки, така че нека преминем към това.

### -4- Обработка на потребителската подкана

В тази част на кода ще обработим потребителските заявки.

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


        // 2. Извикайте инструмента на сървъра
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

    В горния код ние:

    - Добавихме метод `callTools`.
    - Методът приема отговор от LLM и проверява кои инструменти са били извикани, ако има такива:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // извикай инструмент
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

2. Актуализирайте метода `run`, за да включва извиквания към LLM и извикване на `callTools`:

    ```typescript

    // 1. Създаване на съобщения, които са вход за LLM
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

    // 3. Преглед на отговора от LLM, за всеки избор проверете дали има повиквания на инструменти
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Отлично, нека видим кода изцяло:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортиране на zod за валидиране на схеми

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
          // Създайте zod схема въз основа на input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Явно задаване на тип "function"
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
    
    
          // 2. Извикване на инструмента на сървъра
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
    
        // 3. Прегледайте отговора от LLM, за всеки избор проверете дали има извиквания на инструменти
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

1. Нека добавим някои импорти, необходими за извикване на LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. След това нека добавим функцията, която ще извика LLM:

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
            # Незадължителни параметри
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

    В горния код ние:

    - Подадохме нашите функции, които намерихме на MCP сървъра и конвертирахме, на LLM.
    - След това извикахме LLM със същите функции.
    - После проверяваме резултата, за да видим какви функции трябва да се извикат, ако има такива.
    - Накрая подаваме масив с функции за извикване.

3. Последна стъпка, нека актуализираме основния код:

    ```python
    prompt = "Add 2 to 20"

    # попитайте LLM кои инструменти да използва, ако има такива
    functions_to_call = call_llm(prompt, functions)

    # извикайте предложените функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Това беше последната стъпка, в кода по-горе ние:

    - Извикваме MCP инструмент чрез `call_tool` с функция, която LLM смята, че трябва да бъде извикана въз основа на нашата подкана.
    - Извеждаме резултата от извикването на инструмента на MCP сървъра.

#### .NET

1. Нека покажем примерен код за правене на заявка към LLM с подкана:

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

    В горния код ние:

    - Изтеглихме инструменти от MCP сървъра, `var tools = await GetMcpTools()`.
    - Дефинирахме потребителска подкана `userMessage`.
    - Създадохме обект с опции, указващ модел и инструменти.
    - Направихме заявка към LLM.

2. Една последна стъпка, нека видим дали LLM смята, че трябва да извика функция:

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

    В горния код ние:

    - Обхождаме списък с извиквания на функции.
    - За всяко извикване на инструмент извличаме име и аргументи и извикваме инструмента на MCP сървъра, използвайки MCP клиента. Накрая извеждаме резултатите.

Ето кода изцяло:

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
    // Изпълнява заявки на естествен език, които автоматично използват инструменти MCP
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

В горния код ние:

- Използвахме прости подкани на естествен език за взаимодействие с инструментите на MCP сървъра
- Фреймуъркът LangChain4j автоматично се справя с:
  - Преобразуване на потребителските подкани в извиквания на инструменти, когато е необходимо
  - Извикване на подходящите MCP инструменти според решението на LLM
  - Управление на потока на разговора между LLM и MCP сървъра
- Методът `bot.chat()` връща отговори на естествен език, които може да включват резултати от изпълнения на MCP инструменти
- Този подход осигурява безпроблемно потребителско изживяване, при което потребителите не трябва да знаят за подлежащата MCP реализация

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

Тук се случва по-голямата част от работата. Ще извикаме LLM с началната потребителска подкана, след което ще обработим отговора, за да видим дали трябва да се извика някой инструмент. Ако е така, ще извикаме тези инструменти и ще продължим разговора с LLM докато повече извиквания на инструменти не са необходими и имаме краен отговор.


Ще правим множество повиквания към LLM, затова нека дефинираме функция, която ще обработва повикването към LLM. Добавете следната функция във файла `main.rs`:

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

Тази функция приема LLM клиент, списък с съобщения (включително подканата от потребителя), инструменти от MCP сървъра и изпраща заявка към LLM, връщайки отговора.

Отговорът от LLM ще съдържа масив от `choices`. Ще трябва да обработим резултата, за да проверим дали има някакви `tool_calls`. Това ни показва, че LLM иска да бъде извикан конкретен инструмент с аргументи. Добавете следния код в долната част на `main.rs`, за да дефинирате функция, която обработва отговора от LLM:

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

    // Отпечатване на съдържание, ако е налично
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обработка на повиквания към инструменти
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Добавяне на съобщение от асистента

        // Изпълнение на всяко повикване към инструмент
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Добавяне на резултат от инструмента към съобщенията
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Продължаване на разговора с резултатите от инструмента
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

Ако има `tool_calls`, функцията извлича информацията за инструмента, извиква MCP сървъра с тази заявка и добавя резултатите към съобщенията от разговора. След това продължава разговора с LLM, актуализирайки съобщенията с отговора на асистента и резултатите от извикването на инструмента.

За да извлечем информацията за повиквания на инструменти, която LLM връща за MCP извикванията, ще добавим още една помощна функция, която извлича всичко необходимо за осъществяване на повикването. Добавете следния код в долната част на `main.rs`:

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

С всички тези части на място, сега можем да обработим първоначалната подканата от потребителя и да направим повикване към LLM. Обновете функцията `main`, като добавите следния код:

```rust
// Разговор с LLM с извиквания на инструменти
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

Това ще направи заявка към LLM с началната потребителска подканa, като поиска сумата на две числа и ще обработи отговора, за да управлява динамично повикванията на инструменти.

Отлично, успяхте!

## Задание

Вземете кода от упражнението и разширете сървъра с още инструменти. След това създайте клиент с LLM, както в упражнението, и го тествайте с различни подканващи фрази, за да сте сигурни, че всичките ви сървърни инструменти се извикват динамично. Този начин на изграждане на клиент осигурява страхотно потребителско изживяване, тъй като потребителите могат да използват подканващи фрази, вместо точни команди, и да останат незасегнати от вызовите към MCP сървъра.

## Решение

[Решение](./solution/README.md)

## Основни изводи

- Добавянето на LLM към вашия клиент предоставя по-добър начин за взаимодействие на потребителите с MCP сървъри.
- Необходимо е да конвертирате отговора от MCP сървъра в нещо, което LLM може да разбере.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.Net калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python)
- [Rust калкулатор](../../../../03-GettingStarted/samples/rust)

## Допълнителни ресурси

## Какво следва

- Следващо: [Използване на сървър с Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
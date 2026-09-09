# Создание клиента с LLM

Пока что вы видели, как создать сервер и клиента. Клиент мог явно вызывать сервер, чтобы получить список его инструментов, ресурсов и подсказок. Однако это не очень практичный подход. Ваши пользователи живут в эпоху агентов и ожидают использовать подсказки и общаться с LLM вместо этого. Им без разницы, используете ли вы MCP для хранения своих возможностей; они просто ожидают взаимодействия на естественном языке. И как же это решить? Решение — добавить LLM к клиенту.

## Обзор

В этом уроке мы сосредоточимся на добавлении LLM к вашему клиенту и покажем, как это обеспечивает гораздо лучший опыт для пользователя.

## Цели обучения

К концу этого урока вы сможете:

- Создать клиента с LLM.
- Беспроблемно взаимодействовать с сервером MCP с помощью LLM.
- Обеспечить лучший опыт конечного пользователя на стороне клиента.

## Подход

Давайте попробуем понять подход, который нам нужно использовать. Добавить LLM звучит просто, но действительно ли мы это сделаем?

Вот как клиент будет взаимодействовать с сервером:

1. Установить соединение с сервером.

1. Получить список возможностей, подсказок, ресурсов и инструментов, а затем сохранить их схему.

1. Добавить LLM и передать сохранённые возможности и их схему в формате, который понимает LLM.

1. Обрабатывать пользовательские подсказки, передавая их LLM вместе со списком инструментов, полученным клиентом.

Отлично, теперь, когда мы понимаем, как это можно сделать на высоком уровне, давайте попробуем в упражнении ниже.

## Упражнение: Создание клиента с LLM

В этом упражнении мы научимся добавлять LLM к нашему клиенту.

### Аутентификация с помощью персонального токена доступа GitHub

Создать токен GitHub — это простой процесс. Вот как это сделать:

- Перейдите в настройки GitHub — нажмите на свой аватар в правом верхнем углу и выберите Настройки.
- Перейдите в "Настройки разработчика" — прокрутите вниз и нажмите на "Настройки разработчика".
- Выберите "Персональные токены доступа" — нажмите на "Токены с детальной настройкой" и затем "Создать новый токен".
- Настройте токен — добавьте заметку для справки, установите дату истечения и выберите необходимые разрешения (scopes). В данном случае обязательно добавьте разрешение Models.
- Сгенерируйте и скопируйте токен — нажмите "Создать токен" и обязательно скопируйте его сразу, так как после это будет невозможно.

### -1- Подключение к серверу

Давайте сначала создадим нашего клиента:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортировать zod для проверки схемы

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

В приведённом выше коде мы:

- Импортировали необходимые библиотеки.
- Создали класс с двумя членами, `client` и `openai`, которые помогут нам управлять клиентом и взаимодействовать с LLM соответственно.
- Настроили экземпляр LLM для использования моделей GitHub, установив `baseUrl`, указывающий на API вывода.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Создать параметры сервера для соединения stdio
server_params = StdioServerParameters(
    command="mcp",  # Исполняемый файл
    args=["run", "server.py"],  # Необязательные аргументы командной строки
    env=None,  # Необязательные переменные окружения
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Инициализировать соединение
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

В приведённом выше коде мы:

- Импортировали необходимые библиотеки для MCP.
- Создали клиента.

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

Сначала вам нужно добавить зависимости LangChain4j в файл `pom.xml`. Добавьте эти зависимости для интеграции с MCP и OpenAI-совместимым API MiniMax:

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

Установите свой API-ключ MiniMax и, при необходимости, конечную точку и модель.
`MINIMAX_MODEL_ID` поддерживает `MiniMax-M3` и `MiniMax-M2.7`. Если
`OPENAI_BASE_URL` не установлен, `MINIMAX_REGION` поддерживает `global_en` и `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Чтобы выбрать конечную точку по региону, вместо этого опустите `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Затем создайте класс вашего Java клиента:

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

        // Создать MCP транспорт для подключения к серверу
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Создать MCP клиент
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

В приведённом выше коде мы:

- **Добавили зависимости LangChain4j**: необходимые для интеграции с MCP и OpenAI-совместимым API MiniMax.
- **Импортировали библиотеки LangChain4j**: для интеграции MCP и функциональности чат-модели OpenAI.
- **Создали `ChatLanguageModel`**: настроенный для использования MiniMax с вашим API-ключом MiniMax, конечной точкой и поддерживаемым идентификатором модели.
- **Настроили HTTP-транспорт**: с использованием Server-Sent Events (SSE) для подключения к серверу MCP.
- **Создали клиента MCP**: который будет обрабатывать коммуникацию с сервером.
- **Использовали встроенную поддержку MCP в LangChain4j**: что упрощает интеграцию между LLM и серверами MCP.

#### Rust

Этот пример предполагает, что у вас запущен сервер MCP на Rust. Если его нет, обратитесь к уроку [01-first-server](../01-first-server/README.md) для создания сервера.

Как только у вас будет сервер MCP на Rust, откройте терминал и перейдите в ту же директорию, где находится сервер. Затем выполните следующую команду для создания нового проекта клиента LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Добавьте следующие зависимости в файл `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Официальной библиотеки OpenAI для Rust нет, однако `async-openai` — это [библиотека, поддерживаемая сообществом](https://platform.openai.com/docs/libraries/rust#rust), которая широко используется.

Откройте файл `src/main.rs` и замените его содержимое следующим кодом:

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
    // Начальное сообщение
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Настроить клиента OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Настроить клиента MCP
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

    // TODO: Получить список инструментов MCP

    // TODO: Общение с LLM с вызовами инструментов

    Ok(())
}
```

Этот код настраивает базовое приложение на Rust, которое подключается к серверу MCP и GitHub Models для взаимодействия с LLM.

> [!IMPORTANT]
> Перед запуском приложения обязательно установите переменную окружения `OPENAI_API_KEY` с вашим токеном GitHub.

Отлично, на следующем шаге давайте получим список возможностей сервера.

### -2- Получение возможностей сервера

Теперь мы подключимся к серверу и запросим его возможности:

#### Typescript

В той же классе добавьте следующие методы:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // перечисление инструментов
    const toolsResult = await this.client.listTools();
}
```

В приведённом выше коде мы:

- Добавили код для подключения к серверу, `connectToServer`.
- Создали метод `run`, который отвечает за поток работы нашего приложения. Пока он только перечисляет инструменты, но мы скоро дополним его.

#### Python

```python
# Список доступных ресурсов
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Список доступных инструментов
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Вот что мы добавили:

- Перечисление ресурсов и инструментов с их выводом. Для инструментов мы также выводим `inputSchema`, который будет использоваться позже.

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

В приведённом выше коде мы:

- Перечислили инструменты, доступные на сервере MCP.
- Для каждого инструмента перечислили имя, описание и его схему. Последнее пригодится нам для вызова инструментов вскоре.

#### Java

```java
// Создайте поставщика инструментов, который автоматически обнаруживает инструменты MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Поставщик инструментов MCP автоматически обрабатывает:
// - Список доступных инструментов с сервера MCP
// - Конвертацию схем инструментов MCP в формат LangChain4j
// - Управление выполнением инструментов и ответами
```

В приведённом выше коде мы:

- Создали `McpToolProvider`, который автоматически обнаруживает и регистрирует все инструменты с сервера MCP.
- Провайдер инструментов внутрь обрабатывает преобразование между схемами инструментов MCP и форматом инструментов LangChain4j.
- Такой подход абстрагирует от ручного перечисления инструментов и процесса преобразования.

#### Rust

Получение инструментов с сервера MCP осуществляется методом `list_tools`. В функции `main`, после настройки клиента MCP, добавьте следующий код:

```rust
// Получить список инструментов MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертация возможностей сервера в инструменты для LLM

Следующий шаг после перечисления возможностей сервера — преобразовать их в формат, который понимает LLM. После этого мы можем предоставить эти возможности как инструменты LLM.

#### TypeScript

1. Добавьте следующий код для конвертации ответа с сервера MCP в формат инструмента, который LLM сможет использовать:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Создайте схему zod на основе input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно установите тип в "function"
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

    Приведённый код берет ответ от сервера MCP и преобразует его в формат определения инструмента, который понимает LLM.

2. Далее обновим метод `run`, чтобы перечислять возможности сервера:

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

    В приведённом коде мы обновили метод `run`, чтобы пройтись по результату и для каждой записи вызвать `openAiToolAdapter`.

#### Python

1. Сначала создадим следующую функцию-конвертер:

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

    Функция `convert_to_llm_tools` принимает ответ с MCP и конвертирует его в формат, понятный LLM.

2. Затем обновим наш код клиента, используя эту функцию следующим образом:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Здесь мы вызываем `convert_to_llm_tool`, чтобы преобразовать ответ MCP в формат, который позже подадим LLM.

#### .NET

1. Добавим код для преобразования ответа MCP в формат, который понимает LLM:

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

В приведённом выше коде мы:

- Создали функцию `ConvertFrom`, которая принимает имя, описание и схему входных данных.
- Определили функциональность, которая создает `FunctionDefinition`, передаваемый в `ChatCompletionsDefinition`. Последнее понимает LLM.

2. Давайте обновим существующий код, чтобы использовать эту функцию:

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
// Создать интерфейс бота для взаимодействия на естественном языке
public interface Bot {
    String chat(String prompt);
}

// Настроить AI сервис с использованием инструментов LLM и MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

В приведённом выше коде мы:

- Определили простой интерфейс `Bot` для взаимодействия на естественном языке.
- Использовали `AiServices` LangChain4j для автоматической связки LLM с провайдером инструментов MCP.
- Фреймворк автоматически обрабатывает преобразование схемы инструментов и вызовы функций "за кулисами".
- Такой подход устраняет ручное преобразование инструментов — LangChain4j самостоятельно справляется с преобразованием MCP инструментов в совместимый с LLM формат.

#### Rust

Чтобы преобразовать ответ MCP в формат, который понимает LLM, добавим вспомогательную функцию для форматирования списка инструментов. Добавьте следующий код в файл `main.rs` после функции `main`. Эта функция будет вызываться при запросах к LLM:

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

Отлично, теперь мы готовы обрабатывать запросы пользователей, так что приступим к этому.

### -4- Обработка пользовательских подсказок

В этой части кода мы будем обрабатывать запросы пользователей.

#### TypeScript

1. Добавьте метод, который будет использоваться для вызова нашего LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Вызвать инструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Сделать что-то с результатом
        // TODO

        }
    }
    ```

    В приведённом коде мы:

    - Добавили метод `callTools`.
    - Метод принимает ответ LLM и проверяет, какие инструменты были вызваны, если вообще были:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // вызов инструмента
        }
        ```

    - Вызывает инструмент, если LLM указывает, что его следует вызвать:

        ```typescript
        // 2. Вызов инструмента сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Сделать что-то с результатом
        // TODO
        ```

2. Обновите метод `run`, чтобы включить вызовы LLM и вызов `callTools`:

    ```typescript

    // 1. Создайте сообщения, которые являются вводом для LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Вызов LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Просмотрите ответ LLM, для каждого варианта проверьте, есть ли вызовы инструментов
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Отлично, давайте покажем полный код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортировать zod для проверки схемы

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // возможно, в будущем нужно будет изменить на этот URL: https://models.github.ai/inference
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
          // Создать схему zod на основе input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Явно установить тип "function"
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
    
    
          // 2. Вызвать инструмент сервера
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Сделать что-то с результатом
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
    
        // 3. Пройтись по ответу LLM, для каждого варианта проверить, есть ли вызовы инструментов
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

1. Добавим необходимые импорты для вызова LLM:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Далее добавим функцию, которая будет вызывать LLM:

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
            # Необязательные параметры
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

    В приведённом коде мы:

    - Передали в LLM функции, которые мы нашли на сервере MCP и преобразовали.
    - Затем вызвали LLM с этими функциями.
    - После этого проверяем результат, чтобы понять, какие функции нужно вызвать, если такие есть.
    - Наконец, передали массив функций для вызова.

3. Финальный шаг — обновим основной код:

    ```python
    prompt = "Add 2 to 20"

    # спросить у LLM, какие инструменты использовать, если есть
    functions_to_call = call_llm(prompt, functions)

    # вызвать предложенные функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Вот и финальный шаг, в приведённом коде мы:

    - Вызываем инструмент MCP через `call_tool` используя функцию, которую LLM посчитал нужным вызвать на основании нашего запроса.
    - Выводим результат вызова инструмента на сервер MCP.

#### .NET

1. Покажем пример кода для запроса с подсказкой LLM:

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

    В приведённом коде мы:

    - Получили инструменты с сервера MCP, `var tools = await GetMcpTools()`.
    - Определили пользовательскую подсказку `userMessage`.
    - Сконструировали объект опций, указывающий модель и инструменты.
    - Выполнили запрос к LLM.

2. Последний шаг — посмотрим, считает ли LLM, что нужно вызвать функцию:

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

    В приведённом коде мы:

    - Прошлись циклом по списку вызовов функций.
    - Для каждого вызова инструмента извлекаем имя и аргументы и вызываем инструмент на сервере MCP через MCP клиент. В конце выводим результаты.

Вот полный код:

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
    // Выполняйте запросы на естественном языке, автоматически используя инструменты MCP
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

В приведённом выше коде мы:

- Использовали простые подсказки на естественном языке для взаимодействия с инструментами сервера MCP.
- Фреймворк LangChain4j автоматически обрабатывает:
  - Преобразование пользовательских подсказок в вызовы инструментов при необходимости.
  - Вызовы соответствующих инструментов MCP на основании решения LLM.
  - Управление ходом разговора между LLM и сервером MCP.
- Метод `bot.chat()` возвращает ответы на естественном языке, которые могут включать результаты выполнения инструментов MCP.
- Такой подход обеспечивает бесшовный опыт пользователя, где пользователям не нужно знать о внутренней реализации MCP.

Пример полного кода:

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

Здесь происходит большая часть работы. Мы вызовем LLM с исходной пользовательской подсказкой, затем обработаем ответ, чтобы проверить, нужно ли вызвать какие-либо инструменты. Если да, то вызовем эти инструменты и продолжим разговор с LLM до тех пор, пока не потребуется больше вызовов инструментов и мы не получим окончательный ответ.


Мы будем несколько раз вызывать LLM, поэтому давайте определим функцию, которая будет обрабатывать вызов LLM. Добавьте следующую функцию в ваш файл `main.rs`:

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

Эта функция принимает клиента LLM, список сообщений (включая запрос пользователя), инструменты с сервера MCP и отправляет запрос к LLM, возвращая ответ.

Ответ от LLM будет содержать массив `choices`. Нам нужно обработать результат, чтобы проверить наличие `tool_calls`. Это позволит нам узнать, запрашивает ли LLM вызов конкретного инструмента с аргументами. Добавьте следующий код в конец вашего файла `main.rs` для определения функции обработки ответа LLM:

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

    // Вывести содержимое, если доступно
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обработать вызовы инструментов
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Добавить сообщение помощника

        // Выполнить каждый вызов инструмента
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Добавить результат инструмента в сообщения
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Продолжить разговор с результатами инструмента
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

Если `tool_calls` присутствуют, функция извлекает информацию о инструменте, вызывает сервер MCP с запросом инструмента и добавляет результаты к сообщениям переписки. Затем продолжается диалог с LLM, а сообщения обновляются ответом ассистента и результатами вызова инструмента.

Чтобы извлечь информацию о вызове инструмента, который возвращает LLM для вызовов MCP, мы добавим ещё одну вспомогательную функцию, которая извлечёт всё необходимое для выполнения вызова. Добавьте следующий код в конец вашего файла `main.rs`:

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

Со всеми необходимыми компонентами на месте, теперь мы можем обработать первоначальный запрос пользователя и вызвать LLM. Обновите вашу функцию `main`, включив следующий код:

```rust
// Разговор LLM с вызовами инструментов
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

Это отправит запрос LLM с начальными данными пользователя, прося посчитать сумму двух чисел, и обработает ответ для динамического вызова инструментов.

Отлично, вы справились!

## Задание

Возьмите код из упражнения и расширьте сервер, добавив ещё несколько инструментов. Затем создайте клиента с LLM, как в упражнении, и протестируйте его с различными запросами, чтобы убедиться, что все ваши инструменты сервера вызываются динамически. Такой способ построения клиента обеспечивает отличное взаимодействие для конечного пользователя, поскольку он может использовать запросы, а не точные команды клиента, и не замечать вызовы сервера MCP.

## Решение

[Решение](./solution/README.md)

## Основные выводы

- Добавление LLM в ваш клиент предоставляет лучший способ для пользователей взаимодействовать с серверами MCP.
- Нужно преобразовать ответ сервера MCP в формат, понятный LLM.

## Примеры

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Дополнительные ресурсы

## Что дальше

- Далее: [Использование сервера через Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
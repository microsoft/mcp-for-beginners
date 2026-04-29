# Создание клиента с LLM

До сих пор вы видели, как создать сервер и клиента. Клиент мог явно вызывать сервер для получения списка его инструментов, ресурсов и подсказок. Однако это не очень практичный подход. Ваши пользователи живут в эпоху агентов и ожидают использовать подсказки и общаться с LLM. Их не волнует, используете ли вы MCP для хранения возможностей; они просто хотят взаимодействовать на естественном языке. Итак, как мы решим эту задачу? Решение — добавить LLM к клиенту.

## Обзор

В этом уроке мы сосредоточимся на добавлении LLM к вашему клиенту и покажем, как это обеспечивает намного лучший опыт для пользователя.

## Цели обучения

К концу урока вы сможете:

- Создавать клиента с LLM.
- Бесшовно взаимодействовать с сервером MCP, используя LLM.
- Обеспечивать лучший пользовательский опыт на стороне клиента.

## Подход

Давайте попробуем понять подход, который нам нужно применить. Добавить LLM кажется простой задачей, но действительно ли мы это сделаем?

Вот как клиент будет взаимодействовать с сервером:

1. Установить соединение с сервером.

1. Перечислить возможности, подсказки, ресурсы и инструменты, сохранить их схему.

1. Добавить LLM и передать сохранённые возможности и их схему в формате, понятном LLM.

1. Обрабатывать пользовательскую подсказку, передавая её LLM вместе с инструментами, перечисленными клиентом.

Отлично, теперь, когда мы понимаем, как это можно сделать на высоком уровне, давайте попробуем внизу в упражнении.

## Упражнение: Создание клиента с LLM

В этом упражнении мы научимся добавлять LLM к нашему клиенту.

### Аутентификация с использованием персонального токена доступа GitHub

Создание токена GitHub — простой процесс. Вот как это сделать:

- Перейдите в Настройки GitHub – нажмите на вашу фотографию профиля в правом верхнем углу и выберите Настройки.
- Перейдите в Настройки разработчика – прокрутите вниз и кликните на Настройки разработчика.
- Выберите Персональные токены доступа – нажмите на Токены с тонкой настройкой, затем Создать новый токен.
- Настройте ваш токен – добавьте заметку для справки, установите дату истечения и выберите необходимые области доступа (разрешения). В нашем случае обязательно добавьте разрешение Models.
- Создайте и скопируйте токен – нажмите Создать токен, и обязательно скопируйте его сразу, так как вы больше не увидите его повторно.

### -1- Подключение к серверу

Давайте сначала создадим нашего клиента:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортируйте zod для валидации схемы

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

- Импортировали необходимые библиотеки
- Создали класс с двумя членами, `client` и `openai`, которые помогут нам управлять клиентом и взаимодействовать с LLM соответственно.
- Настроили наш экземпляр LLM использовать GitHub Models, установив `baseUrl` на адрес inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Создать параметры сервера для подключения stdio
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

- Импортировали необходимые библиотеки для MCP
- Создали клиента

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

Сначала необходимо добавить зависимости LangChain4j в ваш файл `pom.xml`. Добавьте эти зависимости для поддержки интеграции MCP и GitHub Models:

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

Затем создайте ваш Java класс клиента:

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
    
    public static void main(String[] args) throws Exception {        // Настроить LLM для использования моделей GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

В приведённом выше коде мы:

- **Добавили зависимости LangChain4j**: необходимые для интеграции MCP, официального клиента OpenAI и поддержки GitHub Models
- **Импортировали библиотеки LangChain4j**: для интеграции MCP и функционала чата OpenAI
- **Создали `ChatLanguageModel`**: настроенный использовать GitHub Models с вашим токеном GitHub
- **Настроили HTTP транспорт**: используя Server-Sent Events (SSE) для подключения к серверу MCP
- **Создали MCP клиент**: который будет управлять связью с сервером
- **Использовали встроенную поддержку MCP LangChain4j**: что упрощает интеграцию между LLM и MCP серверами

#### Rust

Этот пример предполагает, что у вас запущен MCP сервер на Rust. Если нет, обратитесь к уроку [01-first-server](../01-first-server/README.md) для создания сервера.

Как только у вас будет сервер MCP на Rust, откройте терминал и перейдите в ту же директорию, что и сервер. Затем выполните следующую команду для создания нового проекта клиента LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Добавьте следующие зависимости в ваш файл `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Официальной библиотеки Rust для OpenAI нет, однако crate `async-openai` — это [библиотека, поддерживаемая сообществом](https://platform.openai.com/docs/libraries/rust#rust), которая широко используется.

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

    // Настройка клиента OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Настройка клиента MCP
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

    // TODO: Разговор LLM с вызовами инструментов

    Ok(())
}
```

Этот код настраивает базовое приложение на Rust, которое подключается к серверу MCP и GitHub Models для взаимодействия с LLM.

> [!IMPORTANT]
> Обязательно установите переменную окружения `OPENAI_API_KEY` со значением вашего GitHub токена перед запуском приложения.

Отлично, следующий шаг — перечислить возможности сервера.

### -2- Перечисление возможностей сервера

Теперь мы подключимся к серверу и запросим его возможности:

#### TypeScript

В том же классе добавьте следующие методы:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // инструменты для листинга
    const toolsResult = await this.client.listTools();
}
```

В приведённом выше коде мы:

- Добавили код для подключения к серверу, метод `connectToServer`.
- Создали метод `run`, отвечающий за обработку нашего потока приложения. Пока он лишь выводит список инструментов, но мы скоро добавим больше.

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

- Перечисление ресурсов и инструментов и их вывод. Для инструментов также перечисляем `inputSchema`, который будет использоваться позже.

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

- Перечислили инструменты, доступные на MCP сервере
- Для каждого инструмента вывели имя, описание и его схему. Последнее мы будем использовать для вызова инструментов в ближайшее время.

#### Java

```java
// Создать провайдера инструментов, который автоматически обнаруживает инструменты MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Провайдер инструментов MCP автоматически обрабатывает:
// - Перечисление доступных инструментов с сервера MCP
// - Конвертацию схем инструментов MCP в формат LangChain4j
// - Управление выполнением инструментов и ответами
```

В приведённом выше коде мы:

- Создали `McpToolProvider`, который автоматически обнаруживает и регистрирует все инструменты с MCP сервера
- Провайдер инструментов обрабатывает преобразование между схемами MCP инструментов и форматом инструментов LangChain4j внутренне
- Этот подход абстрагирует ручной процесс перечисления и преобразования инструментов

#### Rust

Получение инструментов с MCP сервера выполняется с помощью метода `list_tools`. В функции `main`, после настройки MCP клиента, добавьте следующий код:

```rust
// Получить список инструментов MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертация возможностей сервера в инструменты LLM

Следующий шаг после перечисления возможностей сервера — преобразовать их в формат, понятный LLM. После этого мы можем предоставить эти возможности как инструменты нашему LLM.

#### TypeScript

1. Добавьте следующий код для преобразования ответа от MCP сервера в формат инструментов, который LLM может использовать:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Создайте схему zod на основе input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно задайте тип "function"
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

    Приведённый выше код принимает ответ от MCP сервера и конвертирует его в формат описания инструмента, который понимает LLM.

1. Обновим метод `run`, чтобы перечислить возможности сервера:

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

1. Сначала создадим следующую функцию конвертации

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

    В функции `convert_to_llm_tools` мы принимаем ответ инструмента MCP и преобразуем его в формат, понятный LLM.

1. Затем обновим клиентский код, чтобы использовать эту функцию следующим образом:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Здесь мы добавляем вызов `convert_to_llm_tool`, чтобы конвертировать ответ MCP инструмента в формат, который позже можем передать LLM.

#### .NET

1. Добавим код для преобразования ответа инструмента MCP в формат, который может понять LLM:

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

- Создали функцию `ConvertFrom`, которая принимает имя, описание и схему ввода.
- Определили функциональность, создающую FunctionDefinition, который передается в ChatCompletionsDefinition. Последний — это то, что понимает LLM.

1. Теперь посмотрим, как обновить существующий код, чтобы воспользоваться этой функцией:

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
// Создайте интерфейс бота для взаимодействия на естественном языке
public interface Bot {
    String chat(String prompt);
}

// Настройте AI-сервис с инструментами LLM и MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

В приведённом выше коде мы:

- Определили простой интерфейс `Bot` для взаимодействия на естественном языке
- Использовали `AiServices` LangChain4j для автоматической привязки LLM к провайдеру инструментов MCP
- Фреймворк автоматически обрабатывает преобразование схем инструментов и вызов функций за кулисами
- Этот подход избавляет от ручного конвертирования инструментов — LangChain4j справляется со всей сложностью преобразования MCP инструментов в формат, совместимый с LLM

#### Rust

Чтобы преобразовать ответ MCP инструмента в формат, понятный LLM, добавим вспомогательную функцию, которая форматирует список инструментов. Добавьте следующий код в ваш файл `main.rs` ниже функции `main`. Он будет вызван при запросах к LLM:

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

Отлично, теперь мы готовы обрабатывать запросы пользователей, займёмся этим следующим.

### -4- Обработка пользовательской подсказки

В этой части кода мы будем обрабатывать запросы пользователей.

#### TypeScript

1. Добавьте метод, который будет использоваться для вызова LLM:

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

    В приведённом выше коде мы:

    - Добавили метод `callTools`.
    - Метод принимает ответ LLM и проверяет, какие инструменты были вызваны, если они есть:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // вызвать инструмент
        }
        ```

    - Вызывает инструмент, если LLM указывает, что его нужно вызвать:

        ```typescript
        // 2. Вызвать инструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Сделать что-то с результатом
        // TODO
        ```

1. Обновите метод `run`, чтобы добавить вызовы к LLM и вызов `callTools`:

    ```typescript

    // 1. Создайте сообщения, которые являются входными данными для LLM
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

Отлично, вот полный код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортировать zod для валидации схемы

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // возможно, позже потребуется изменить на этот URL: https://models.github.ai/inference
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
            type: "function" as const, // Явно указать тип "function"
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
    
          // 3. Что-то сделать с результатом
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
    
        // 1. Пройтись по ответу LLM, для каждого варианта проверить, есть ли вызовы инструментов
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

1. Добавим необходимые импорты для вызова LLM

    ```python
    # ллм
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Далее добавим функцию, которая будет вызывать LLM:

    ```python
    # языковая модель

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

    - Передали функции, найденные на MCP сервере и сконвертированные, в LLM.
    - Затем вызвали LLM с этими функциями.
    - Потом проверяем результат, чтобы понять, какие функции нужно вызвать, если они есть.
    - Наконец, передаём массив функций для вызова.

1. Последний шаг — обновим основной код:

    ```python
    prompt = "Add 2 to 20"

    # спросить LLM, какие инструменты использовать, если они есть
    functions_to_call = call_llm(prompt, functions)

    # вызвать предложенные функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Вот и всё, в приведённом выше коде мы:

    - Вызываем инструмент MCP через `call_tool` используя функцию, которую LLM решил вызвать на основе нашей подсказки.
    - Выводим результат вызова инструмента на MCP сервере.

#### .NET

1. Покажем код для выполнения запроса к LLM:

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

    В приведённом выше коде мы:

    - Получили инструменты с MCP сервера, `var tools = await GetMcpTools()`.
    - Определили пользовательскую подсказку `userMessage`.
    - Создали объект опций с указанием модели и инструментов.
    - Выполнили запрос к LLM.

1. Последний шаг — проверим, считает ли LLM, что нужно вызвать функцию:

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

    - Прошлись по списку вызовов функций.
    - Для каждого вызова парсим имя и аргументы и вызываем инструмент на MCP сервере через MCP клиент. В конце выводим результаты.

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Выполнять запросы на естественном языке с автоматическим использованием инструментов MCP
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

В приведённом коде мы:

- Использовали простые подсказки на естественном языке для взаимодействия с инструментами MCP сервера.
- Фреймворк LangChain4j автоматически обрабатывает:
  - Преобразование пользовательских подсказок в вызовы инструментов при необходимости
  - Вызов соответствующих инструментов MCP в зависимости от решения LLM
  - Управление потоком разговора между LLM и MCP сервером
- Метод `bot.chat()` возвращает ответы на естественном языке, которые могут содержать результаты выполнения инструментов MCP
- Такой подход обеспечивает плавный пользовательский опыт, где пользователям не нужно знать о внутренней реализации MCP

Полный пример кода:

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

Здесь происходит основная часть работы. Мы будем вызывать LLM с начальной пользовательской подсказкой, затем обрабатывать ответ, чтобы понять, нужно ли вызывать какие-либо инструменты. Если да, мы вызовем эти инструменты и продолжим разговор с LLM, пока не перестанут требоваться вызовы инструментов и не получим окончательный ответ.

Будет несколько вызовов LLM, поэтому давайте определим функцию, которая будет обрабатывать вызов LLM. Добавьте следующую функцию в ваш файл `main.rs`:

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

Эта функция принимает клиента LLM, список сообщений (включая подсказку пользователя), инструменты с MCP сервера и отправляет запрос к LLM, возвращая ответ.
Ответ от LLM будет содержать массив `choices`. Нам нужно будет обработать результат, чтобы проверить, есть ли `tool_calls`. Это позволяет нам понять, что LLM запрашивает вызов конкретного инструмента с аргументами. Добавьте следующий код в конец вашего файла `main.rs`, чтобы определить функцию для обработки ответа LLM:

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

    // Печатать содержимое, если доступно
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обрабатывать вызовы инструментов
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Добавить сообщение ассистента

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

        // Продолжить разговор с результатами инструментов
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

Если присутствуют `tool_calls`, функция извлекает информацию об инструменте, вызывает сервер MCP с запросом инструмента и добавляет результаты в сообщения беседы. Затем продолжается беседа с LLM, а сообщения обновляются ответом ассистента и результатами вызова инструмента.

Чтобы извлечь информацию о вызове инструмента, которую возвращает LLM для вызовов MCP, мы добавим ещё одну вспомогательную функцию, которая извлечёт всё необходимое для выполнения вызова. Добавьте следующий код в конец вашего файла `main.rs`:

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

Имея все части на месте, мы теперь можем обработать начальный запрос пользователя и вызвать LLM. Обновите вашу функцию `main`, чтобы включить следующий код:

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

Это будет отправлять запрос к LLM с начальным запросом пользователя с просьбой сложить два числа и обработает ответ для динамического управления вызовами инструментов.

Отлично, вы сделали это!

## Задание

Возьмите код из упражнения и расширьте сервер, добавив ещё несколько инструментов. Затем создайте клиент с LLM, как в упражнении, и протестируйте его с разными запросами, чтобы убедиться, что все инструменты сервера вызываются динамически. Такой способ построения клиента обеспечивает отличный пользовательский опыт, так как конечный пользователь может использовать запросы, а не точные команды клиента, и при этом не замечать вызовы MCP сервера.

## Решение

[Решение](./solution/README.md)

## Основные выводы

- Добавление LLM в ваш клиент предоставляет лучший способ взаимодействия пользователей с MCP серверами.
- Вам нужно преобразовать ответ MCP сервера в что-то, что LLM сможет понять.

## Примеры

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Дополнительные ресурсы

## Что дальше

- Далее: [Использование сервера через Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на языке оригинала следует рассматривать как авторитетный источник. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственность за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
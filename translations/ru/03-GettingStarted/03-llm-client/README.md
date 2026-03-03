# Создание клиента с LLM

До сих пор вы увидели, как создать сервер и клиент. Клиент мог явно вызывать сервер, чтобы получить список его инструментов, ресурсов и подсказок. Однако это не очень практичный подход. Ваши пользователи живут в эру агентов и ожидают использовать подсказки и общаться с LLM. Им не важно, используете ли вы MCP для хранения своих возможностей; они просто хотят взаимодействовать на естественном языке. Итак, как решить эту проблему? Решение — добавить LLM в клиент.

## Обзор

В этом уроке мы сосредоточимся на добавлении LLM в ваш клиент и покажем, как это обеспечивает гораздо лучший опыт для пользователя.

## Цели обучения

К концу этого урока вы сможете:

- Создать клиента с LLM.
- Бесшовно взаимодействовать с MCP сервером с помощью LLM.
- Обеспечить лучший опыт конечного пользователя на стороне клиента.

## Подход

Давайте попробуем понять подход, который нам нужно применить. Добавить LLM звучит просто, но действительно ли мы это сделаем?

Вот как клиент будет взаимодействовать с сервером:

1. Установить соединение с сервером.

1. Получить список возможностей, подсказок, ресурсов и инструментов и сохранить их схему.

1. Добавить LLM и передать сохранённые возможности и их схему в формате, который понимает LLM.

1. Обрабатывать пользовательскую подсказку, передавая её в LLM вместе с инструментами, перечисленными клиентом.

Отлично, теперь, когда мы понимаем, как это сделать на высоком уровне, давайте попробуем это на практике в приведённом ниже упражнении.

## Упражнение: Создание клиента с LLM

В этом упражнении мы научимся добавлять LLM в наш клиент.

### Аутентификация с использованием GitHub Personal Access Token

Создать GitHub токен — это простой процесс. Вот как это сделать:

- Перейдите в настройки GitHub – Нажмите на свою фотографию профиля в правом верхнем углу и выберите Settings.
- Перейдите в Developer Settings – Прокрутите вниз и нажмите Developer Settings.
- Выберите Personal Access Tokens – Нажмите Fine-grained tokens, затем Generate new token.
- Настройте ваш токен – Добавьте заметку для справки, установите дату истечения и выберите необходимые области доступа (разрешения). В данном случае обязательно добавьте разрешение Models.
- Сгенерируйте и скопируйте токен – Нажмите Generate token, и обязательно скопируйте его сразу, так как повторно увидеть токен будет невозможно.

### -1- Подключение к серверу

Давайте сначала создадим нашего клиента:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортируйте zod для проверки схемы

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
- Настроили экземпляр LLM для использования GitHub Models, установив `baseUrl`, указывающий на inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Создать параметры сервера для соединения stdio
server_params = StdioServerParameters(
    command="mcp",  # Выполняемый файл
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

Сначала нужно добавить зависимости LangChain4j в ваш `pom.xml`. Добавьте эти зависимости для поддержки интеграции с MCP и работы с GitHub Models:

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

Затем создайте ваш Java-класс клиента:

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

        // Создать транспорт MCP для подключения к серверу
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Создать клиент MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

В приведённом выше коде мы:

- **Добавили зависимости LangChain4j**: необходимые для интеграции MCP, официального клиента OpenAI и поддержки GitHub Models
- **Импортировали библиотеки LangChain4j**: для интеграции MCP и работы с OpenAI чат-моделью
- **Создали `ChatLanguageModel`**: настроенный для использования GitHub Models с вашим GitHub токеном
- **Настроили HTTP транспорт**: с использованием Server-Sent Events (SSE) для подключения к MCP серверу
- **Создали MCP клиента**: который будет обрабатывать общение с сервером
- **Использовали встроенную поддержку MCP в LangChain4j**: что упрощает интеграцию между LLM и MCP серверами

#### Rust

Этот пример предполагает, что у вас запущен MCP сервер на Rust. Если у вас его нет, обратитесь к уроку [01-first-server](../01-first-server/README.md), чтобы создать сервер.

После того, как у вас есть Rust MCP сервер, откройте терминал и перейдите в ту же директорию, что и сервер. Затем выполните следующую команду, чтобы создать новый проект клиента LLM:

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
> Официальной библиотеки OpenAI для Rust не существует, однако crate `async-openai` является [поддерживаемой сообществом библиотекой](https://platform.openai.com/docs/libraries/rust#rust), которая широко используется.

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

    // TODO: Разговор с LLM с вызовами инструментов

    Ok(())
}
```

Этот код настраивает базовое Rust приложение, которое подключится к MCP серверу и GitHub Models для взаимодействия с LLM.

> [!IMPORTANT]
> Перед запуском приложения убедитесь, что установлена переменная окружения `OPENAI_API_KEY` с вашим GitHub токеном.

Отлично, следующим шагом будем получать список возможностей с сервера.

### -2- Получение списка возможностей сервера

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

    // перечисление инструментов
    const toolsResult = await this.client.listTools();
}
```

В приведённом выше коде мы:

- Добавили код для подключения к серверу, `connectToServer`.
- Создали метод `run`, отвечающий за обработку потока приложения. Пока что он просто выводит список инструментов, но вскоре мы добавим туда больше функций.

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

- Получение списка ресурсов и инструментов и их вывод. Для инструментов мы также выводим `inputSchema`, который будем использовать позже.

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

- Получили список инструментов, доступных на MCP сервере
- Для каждого инструмента вывели имя, описание и его схему. Последнюю мы будем использовать для вызова инструментов в ближайшее время.

#### Java

```java
// Создайте поставщика инструментов, который автоматически обнаруживает инструменты MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Поставщик инструментов MCP автоматически обрабатывает:
// - Список доступных инструментов с сервера MCP
// - Преобразование схем инструментов MCP в формат LangChain4j
// - Управление выполнением инструментов и ответами
```

В приведённом выше коде мы:

- Создали `McpToolProvider`, который автоматически находит и регистрирует все инструменты с MCP сервера
- Провайдер инструментов самостоятельно обрабатывает преобразование схем инструментов MCP в формат LangChain4j
- Этот подход избавляет от необходимости вручную перечислять и конвертировать инструменты

#### Rust

Получение инструментов с MCP сервера выполняется с помощью метода `list_tools`. В вашей функции `main`, после настройки MCP клиента, добавьте следующий код:

```rust
// Получить список инструментов MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Преобразование возможностей сервера в инструменты для LLM

Следующий шаг после получения списка возможностей сервера — преобразовать их в формат, понимаемый LLM. После этого мы можем предоставить эти возможности в виде инструментов нашему LLM.

#### TypeScript

1. Добавьте следующий код для преобразования ответа от MCP сервера в формат инструмента, который может использовать LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Создайте схему zod на основе input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно установите тип "function"
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

    В этом коде мы берём ответ от MCP сервера и конвертируем его в формат определения инструмента, который понимает LLM.

1. Обновим метод `run`, чтобы он выводил возможности сервера:

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

    В приведённом коде мы обновили метод `run`, чтобы пройтись по результату и для каждого элемента вызвать `openAiToolAdapter`.

#### Python

1. Сначала создадим функцию-конвертер:

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

    В функции `convert_to_llm_tools` мы берём ответ MCP инструмента и преобразуем его в формат, понятный LLM.

1. Далее обновим код клиента, чтобы использовать эту функцию:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Здесь мы добавляем вызов `convert_to_llm_tool`, чтобы сконвертировать ответ MCP инструмента в формат, который мы можем передать LLM.

#### .NET

1. Добавим код для преобразования ответа MCP инструмента в понятный для LLM формат:

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

В приведённом коде мы:

- Создали функцию `ConvertFrom`, которая принимает имя, описание и схему ввода.
- Определили функционал создания `FunctionDefinition`, который передаётся в `ChatCompletionsDefinition`. Последнее LLM понимает.

1. Обновим существующий код, чтобы воспользоваться этой функцией:

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

// Настройте AI-сервис с помощью инструментов LLM и MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

В приведённом коде мы:

- Определили простой интерфейс `Bot` для взаимодействия на естественном языке
- Использовали `AiServices` LangChain4j для автоматического связывания LLM с провайдером MCP инструментов
- Фреймворк автоматически обрабатывает конвертацию схем инструментов и вызовы функций за кулисами
- Этот подход исключает ручную конвертацию инструментов — LangChain4j берет на себя всю сложность преобразования MCP инструментов в формат, совместимый с LLM

#### Rust

Для преобразования ответа MCP инструмента в формат, понятный LLM, мы добавим вспомогательную функцию, которая форматирует список инструментов. Добавьте следующий код в ваш файл `main.rs` ниже функции `main`. Он будет вызываться при запросах к LLM:

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

Отлично, теперь мы готовы обрабатывать запросы пользователя. Перейдём к следующему шагу.

### -4- Обработка пользовательского запроса

В этой части кода мы будем обрабатывать запросы пользователя.

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


        // 2. Вызовите инструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Что-то сделайте с результатом
        // TODO

        }
    }
    ```

    В приведённом коде мы:

    - Добавили метод `callTools`.
    - Метод принимает ответ LLM и проверяет, какие инструменты были вызваны, если такие есть:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // вызвать инструмент
        }
        ```

    - Вызывает инструмент, если LLM указывает, что инструмент следует вызвать:

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

1. Обновите метод `run`, чтобы включить вызовы LLM и функцию `callTools`:

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

Отлично, давайте выведем весь код целиком:

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
            type: "function" as const, // Явно установить тип как "function"
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

1. Затем добавим функцию, которая будет вызывать LLM:

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
            # Дополнительные параметры
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

    - Передали функции, полученные с MCP сервера и конвертированные, в LLM.
    - Затем вызвали LLM с этими функциями.
    - После этого проверили результат, чтобы понять, какие функции следует вызвать.
    - В конце передали массив функций для вызова.

1. Финальный шаг — обновим основной код:

    ```python
    prompt = "Add 2 to 20"

    # спросить LLM, какие инструменты использовать, если таковые имеются
    functions_to_call = call_llm(prompt, functions)

    # вызвать предложенные функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Вот и всё, на этом этапе мы:

    - Вызываем MCP инструмент через `call_tool` с функцией, которую LLM посчитал нужным вызвать на основе пользовательской подсказки.
    - Выводим результат вызова инструмента на MCP сервере.

#### .NET

1. Покажем код для выполнения LLM-подсказки:

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

    - Получили инструменты с MCP сервера, `var tools = await GetMcpTools()`.
    - Определили пользовательскую подсказку `userMessage`.
    - Создали объект опций с указанием модели и инструментов.
    - Сделали запрос к LLM.

1. Последний шаг — проверить, нужно ли вызвать функцию согласно LLM:

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

    В коде выше мы:

    - Перебираем список вызовов функций.
    - Для каждого вызова инструмента извлекаем имя и аргументы, вызываем инструмент на MCP сервере через MCP клиента. В завершение выводим результаты.

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
    // Выполнять запросы на естественном языке, которые автоматически используют инструменты MCP
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

- Использовали простые подсказки на естественном языке для взаимодействия с инструментами MCP сервера
- Фреймворк LangChain4j автоматически управляет:
  - Преобразованием пользовательских подсказок в вызовы инструментов при необходимости
  - Вызовом подходящих MCP инструментов по решению LLM
  - Управлением потоком диалога между LLM и MCP сервером
- Метод `bot.chat()` возвращает ответы на естественном языке, которые могут содержать результаты выполнения MCP инструментов
- Этот подход обеспечивает плавный пользовательский опыт, где пользователю не нужно знать о внутренней реализации MCP

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

Здесь происходит основная часть работы. Мы вызовем LLM с начальной пользовательской подсказкой, затем обработаем ответ, чтобы понять, нужно ли вызывать какие-либо инструменты. Если да, вызовем эти инструменты и продолжим общение с LLM, пока не потребуется больше вызовов инструментов и не будет получен окончательный ответ.

Мы сделаем несколько вызовов к LLM, поэтому определим функцию для обработки вызова LLM. Добавьте следующую функцию в ваш файл `main.rs`:

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

Эта функция принимает клиента LLM, список сообщений (включая пользовательскую подсказку), инструменты MCP сервера и отправляет запрос LLM, возвращая ответ.
Ответ от LLM будет содержать массив `choices`. Нам нужно обработать результат, чтобы проверить, присутствуют ли какие-либо `tool_calls`. Это позволит нам понять, что LLM запрашивает вызов конкретного инструмента с аргументами. Добавьте следующий код в конец вашего файла `main.rs`, чтобы определить функцию для обработки ответа LLM:

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

Если присутствуют `tool_calls`, функция извлекает информацию о инструменте, вызывает MCP-сервер с запросом инструмента и добавляет результаты в сообщения беседы. Затем продолжается беседа с LLM, и сообщения обновляются ответом ассистента и результатами вызова инструмента.

Чтобы извлечь информацию о вызове инструмента, которую LLM возвращает для вызовов MCP, мы добавим ещё одну вспомогательную функцию, чтобы извлечь всё необходимое для выполнения вызова. Добавьте следующий код в конец вашего файла `main.rs`:

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

Когда все части в сборе, теперь мы можем обработать начальный запрос пользователя и вызвать LLM. Обновите вашу функцию `main`, включив следующий код:

```rust
// Разговор с LLM с вызовами инструментов
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

Этот код отправит запрос LLM с начальным запросом пользователя, спрашивая сумму двух чисел, и обработает ответ для динамической обработки вызовов инструментов.

Отлично, вы справились!

## Задание

Возьмите код из упражнения и разработайте сервер с большим количеством инструментов. Затем создайте клиент с LLM, как в упражнении, и протестируйте его с разными запросами, чтобы убедиться, что все инструменты вашего сервера вызываются динамически. Такой способ построения клиента обеспечивает отличный пользовательский опыт, так как пользователи могут использовать запросы на естественном языке, а не точные команды клиента, и не подозревают о вызовах MCP сервера.

## Решение

[Решение](/03-GettingStarted/03-llm-client/solution/README.md)

## Основные выводы

- Добавление LLM в ваш клиент предоставляет лучший способ взаимодействия пользователей с MCP серверами.
- Необходимо преобразовать ответ MCP сервера в формат, понятный LLM.

## Примеры

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Дополнительные ресурсы

## Что дальше

- Далее: [Использование сервера с помощью Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на языке исходного текста следует считать авторитетным источником. Для важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или искажения смысла, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
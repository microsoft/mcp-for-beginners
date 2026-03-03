# Створення клієнта з LLM

Дотепер ви бачили, як створити сервер і клієнта. Клієнт міг явно звертатися до сервера, щоб перерахувати його інструменти, ресурси та підказки. Однак це не дуже практичний підхід. Ваші користувачі живуть у агентичну еру та очікують використовувати підказки і спілкуватися з LLM. Їм байдуже, чи використовуєте ви MCP для зберігання своїх можливостей; вони просто очікують взаємодії природною мовою. Тож як же ми це вирішуємо? Рішення – додати LLM до клієнта.

## Огляд

У цьому уроці ми зосередимося на додаванні LLM до вашого клієнта і покажемо, як це покращує досвід для вашого користувача.

## Цілі навчання

До кінця цього уроку ви зможете:

- Створити клієнта з LLM.
- Безперешкодно взаємодіяти з MCP сервером за допомогою LLM.
- Забезпечити кращий досвід для кінцевого користувача на стороні клієнта.

## Підхід

Спробуймо зрозуміти, який підхід нам потрібно застосувати. Додавання LLM звучить просто, але чи справді ми так зробимо?

Ось як клієнт взаємодіятиме з сервером:

1. Встановити з’єднання з сервером.

1. Перелік можливостей, підказок, ресурсів та інструментів і збереження їхньої схеми.

1. Додати LLM і передати збережені можливості та їхню схему у форматі, який розуміє LLM.

1. Обробити підказку користувача, передавши її LLM разом з інструментами, перерахованими клієнтом.

Чудово, тепер ми розуміємо, як це зробити на високому рівні, давайте спробуємо це в наступній вправі.

## Вправа: Створення клієнта з LLM

У цій вправі ми навчимося додавати LLM до нашого клієнта.

### Аутентифікація за допомогою персонального токена доступу GitHub

Створення GitHub токена — це простий процес. Ось як це зробити:

- Перейдіть до Налаштувань GitHub – натисніть на фото профілю у верхньому правому куті та виберіть Налаштування.
- Перейдіть до Налаштувань розробника – прокрутіть вниз і натисніть Налаштування розробника.
- Виберіть Особисті токени доступу – натисніть на Токени з гнучкими налаштуваннями, а потім Згенерувати новий токен.
- Налаштуйте свій токен – додайте примітку для посилання, встановіть дату закінчення терміну дії і виберіть необхідні права доступу. У цьому випадку обов’язково додайте дозвіл Models.
- Згенеруйте і скопіюйте токен – натисніть Згенерувати токен і обов’язково скопіюйте його одразу, оскільки пізніше ви не зможете його побачити.

### -1- Підключення до сервера

Спершу створімо наш клієнт:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Імпортуйте zod для перевірки схеми

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

У наведеному вище коді ми:

- Імпортували потрібні бібліотеки
- Створили клас з двома членами, `client` і `openai`, які допоможуть керувати клієнтом і взаємодіяти з LLM відповідно.
- Налаштували інстанс LLM для використання Models GitHub, вказавши `baseUrl` на API для inference.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для підключення stdio
server_params = StdioServerParameters(
    command="mcp",  # Виконуваний файл
    args=["run", "server.py"],  # Необов'язкові аргументи командного рядка
    env=None,  # Необов'язкові змінні середовища
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Ініціалізувати з'єднання
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

У наведеному вище коді ми:

- Імпортували потрібні бібліотеки для MCP
- Створили клієнта

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

Спершу додайте залежності LangChain4j до файлу `pom.xml`. Додайте ці залежності, щоб увімкнути інтеграцію MCP і підтримку GitHub Models:

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

Потім створіть клас клієнта на Java:

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
    
    public static void main(String[] args) throws Exception {        // Налаштуйте LLM для використання моделей GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Створіть транспорт MCP для підключення до сервера
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Створіть клієнта MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

У наведеному вище коді ми:

- **Додали залежності LangChain4j**: необхідні для інтеграції MCP, офіційного клієнта OpenAI і підтримки GitHub Models
- **Імпортували бібліотеки LangChain4j**: для інтеграції MCP і функціоналу чат-моделі OpenAI
- **Створили `ChatLanguageModel`**: налаштований для використання GitHub Models з вашим GitHub токеном
- **Налаштували HTTP-транспорт**: з використанням Server-Sent Events (SSE) для підключення до MCP сервера
- **Створили MCP клієнта**: який опікується комунікацією з сервером
- **Використали вбудовану підтримку MCP у LangChain4j**: що спрощує інтеграцію між LLM і MCP серверами

#### Rust

Цей приклад припускає, що у вас запущений Rust MCP сервер. Якщо ні, зверніться до уроку [01-first-server](../01-first-server/README.md), щоб створити сервер.

Після того, як у вас є Rust MCP сервер, відкрийте термінал і перейдіть у ту ж папку, де знаходиться сервер. Потім виконайте команду, щоб створити новий проект клієнта LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Додайте наступні залежності до файлу `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Офіційної бібліотеки OpenAI для Rust немає, однак crate `async-openai` є [спільнотною бібліотекою](https://platform.openai.com/docs/libraries/rust#rust), яку широко використовують.

Відкрийте файл `src/main.rs` і замініть його вміст на наступний код:

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
    // Початкове повідомлення
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Налаштування клієнта OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Налаштування клієнта MCP
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

    // TODO: Отримати список інструментів MCP

    // TODO: Розмова з LLM з викликами інструментів

    Ok(())
}
```

Цей код створює базовий Rust додаток, який підключається до MCP сервера та GitHub Models для взаємодії з LLM.

> [!IMPORTANT]
> Переконайтеся, що перед запуском додатку встановили змінну середовища `OPENAI_API_KEY` зі своїм GitHub токеном.

Чудово, наступним кроком давайте перелікуємо можливості на сервері.

### -2- Перелік можливостей сервера

Тепер ми підключимося до сервера і запросимо його можливості:

#### Typescript

В тому ж класі додайте наступні методи:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // перерахування інструментів
    const toolsResult = await this.client.listTools();
}
```

У наведеному вище коді ми:

- Додали код для підключення до сервера, `connectToServer`.
- Створили метод `run`, який відповідає за обробку логіки програми. Поки він лише перераховує інструменти, але незабаром ми додамо більше.

#### Python

```python
# Перелік доступних ресурсів
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Перелік доступних інструментів
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ось що ми додали:

- Перелік ресурсів та інструментів та їх вивід. Для інструментів також виводимо `inputSchema`, який буде корисний згодом.

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

У наведеному вище коді ми:

- Перелічили інструменти, доступні на MCP сервері
- Для кожного інструменту вивели ім'я, опис і його схему. Останнє ми використаємо для виклику інструментів згодом.

#### Java

```java
// Створити провайдера інструментів, який автоматично знаходить інструменти MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Провайдер інструментів MCP автоматично обробляє:
// - Перелік доступних інструментів з сервера MCP
// - Конвертацію схем інструментів MCP у формат LangChain4j
// - Керування виконанням інструментів та відповідями
```

У наведеному вище коді ми:

- Створили `McpToolProvider`, який автоматично виявляє і реєструє всі інструменти з MCP сервера
- Провайдер інструментів внутрішньо перетворює MCP схеми інструментів у формат LangChain4j
- Цей підхід приховує ручний процес переліку і перетворення інструментів

#### Rust

Отримання інструментів з MCP сервера відбувається за допомогою методу `list_tools`. У функції `main`, після налаштування MCP клієнта, додайте цей код:

```rust
// Отримати список інструментів MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Перетворення можливостей сервера в інструменти LLM

Наступним кроком після переліку можливостей сервера є конвертація їх у формат, який розуміє LLM. Зробивши це, ми зможемо надати ці можливості як інструменти нашому LLM.

#### TypeScript

1. Додайте наступний код, щоб перетворити відповідь від MCP сервера у формат інструменту, який LLM може використовувати:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Створіть схему zod на основі input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Явно встановіть тип "function"
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

    Наведений код приймає відповідь від MCP сервера і конвертує її у формат визначення інструменту, який розуміє LLM.

1. Оновімо наступним чином метод `run` для переліку можливостей сервера:

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

    У наведеному коді ми оновили метод `run`, щоб пройтися по результату і для кожного елемента викликати `openAiToolAdapter`.

#### Python

1. Спочатку створимо таку функцію конвертора

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

    У функції `convert_to_llm_tools` ми приймаємо відповідь MCP інструменту і перетворюємо її у формат, зрозумілий для LLM.

1. Далі оновімо код клієнта, щоб використовувати цю функцію так:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тут ми додаємо виклик `convert_to_llm_tool`, щоб перетворити відповідь MCP інструменту на те, що можна передати LLM.

#### .NET

1. Додамо код для конвертації відповіді MCP інструменту в те, що зрозуміє LLM

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

У наведеному коді ми:

- Створили функцію `ConvertFrom`, яка приймає ім'я, опис і схему введення.
- Визначили функціонал, що створює `FunctionDefinition`, який передається у `ChatCompletionsDefinition`. Останнє розуміє LLM.

1. Ось як оновити наявний код для використання цієї функції:

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
// Створіть інтерфейс бота для взаємодії природною мовою
public interface Bot {
    String chat(String prompt);
}

// Налаштуйте AI-сервіс з інструментами LLM та MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У наведеному вище коді ми:

- Визначили простий інтерфейс `Bot` для взаємодій природною мовою
- Використали `AiServices` LangChain4j, які автоматично зв’язують LLM з MCP постачальником інструментів
- Фреймворк автоматично обробляє перетворення схем інструментів і виклик функцій поза сценою
- Цей підхід усуває ручне перетворення інструментів — LangChain4j бере на себе всю складність перетворення MCP інструментів у формат, сумісний з LLM

#### Rust

Щоб конвертувати відповідь MCP інструменту у формат, який розуміє LLM, додамо допоміжну функцію, яка форматуватиме перелік інструментів. Додайте цей код у файл `main.rs` нижче функції `main`. Він викликатиметься при запитах до LLM:

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

Чудово, тепер ми готові обробляти запити користувачів, рахуємо наступним.

### -4- Обробка запиту підказки користувача

У цій частині коду ми обробимо запити користувачів.

#### TypeScript

1. Додамо метод, який буде викликати наш LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Викликати інструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Зробити щось з результатом
        // TODO

        }
    }
    ```

    У наведеному коді ми:

    - Додали метод `callTools`.
    - Метод приймає відповідь LLM і перевіряє, які інструменти були викликані, якщо такі є:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // викликати інструмент
        }
        ```

    - Викликає інструмент, якщо LLM вказує, що його треба викликати:

        ```typescript
        // 2. Викликати інструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Зробити щось з результатом
        // TODO
        ```

1. Оновимо метод `run`, додавши виклики LLM і виклик `callTools`:

    ```typescript

    // 1. Створіть повідомлення, які є вхідними для LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Виклик LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Перегляньте відповідь LLM, для кожного варіанту перевірте, чи є виклики інструментів
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Чудово, наведемо код повністю:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Імпортуйте zod для валідації схеми

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можливо, потрібно буде змінити на цю URL-адресу в майбутньому: https://models.github.ai/inference
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
          // Створіть схему zod на основі input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Явно встановіть тип як "function"
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
    
    
          // 2. Виклик інструменту сервера
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Зробіть щось з результатом
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
    
        // 1. Пройдіться відповіддю LLM, для кожного варіанту перевірте, чи є виклики інструментів
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

1. Додамо необхідні імпорти для виклику LLM

    ```python
    # великий мовна модель
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Потім додамо функцію, яка викликатиме LLM:

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
            # Необов’язкові параметри
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

    У наведеному коді ми:

    - Передали функції, виявлені на MCP сервері та конвертовані, до LLM.
    - Викликали LLM з цими функціями.
    - Інспектували результат, щоб дізнатися, які функції потрібно викликати, якщо взагалі.
    - Передали масив функцій для виклику.

1. Останній крок – оновимо основний код:

    ```python
    prompt = "Add 2 to 20"

    # запитати у LLM, які інструменти використовувати, якщо такі є
    functions_to_call = call_llm(prompt, functions)

    # викликати запропоновані функції
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    От і все, у коді вище ми:

    - Виконуємо виклик MCP інструменту через `call_tool`, використовуючи функцію, яку LLM вважав за потрібне викликати на основі нашої підказки.
    - Виводимо результат виклику інструменту на MCP сервер.

#### .NET

1. Покажемо код для запиту LLM підказки:

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

    У наведеному коді ми:

    - Отримали інструменти з MCP сервера, `var tools = await GetMcpTools()`.
    - Визначили підказку користувача `userMessage`.
    - Створили об’єкт параметрів з вказаною моделлю та інструментами.
    - Виконали запит до LLM.

1. Останній крок — подивимось, чи LLM вважає, що нам слід викликати функцію:

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

    У наведеному коді ми:

    - Пройшлися по списку викликів функцій.
    - Для кожного виклику інструменту розібрали ім'я і аргументи і викликали інструмент на MCP сервері за допомогою MCP клієнта. В кінці виводимо результати.

Ось повний код:

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
    // Виконувати запити природною мовою, які автоматично використовують інструменти MCP
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

У наведеному коді ми:

- Використовували прості підказки природною мовою для взаємодії з інструментами MCP сервера
- Фреймворк LangChain4j автоматично виконує:
  - Перетворення користувацьких підказок у виклики інструментів, коли це потрібно
  - Виклик відповідних MCP інструментів на основі рішення LLM
  - Керування потоками розмови між LLM та MCP сервером
- Метод `bot.chat()` повертає відповіді природною мовою, які можуть включати результати виконання інструментів MCP
- Такий підхід забезпечує безшовний користувацький досвід, де користувачам не потрібно знати про внутрішню реалізацію MCP

Приклад повного коду:

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

Саме тут відбувається більшість роботи. Ми викличемо LLM з початковою підказкою користувача, потім обробимо відповідь, щоб перевірити, чи потрібно викликати якісь інструменти. Якщо так, ми виконаємо ці виклики і продовжимо розмову з LLM, поки не буде завершено виклики інструментів і не отримаємо кінцеву відповідь.

Ми збираємося робити декілька викликів LLM, тож визначимо функцію, яка здійснюватиме виклик LLM. Додайте таку функцію у файл `main.rs`:

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

Ця функція приймає клієнта LLM, список повідомлень (включно з підказкою користувача), інструменти MCP сервера і надсилає запит до LLM, повертаючи відповідь.
Відповідь від LLM буде містити масив `choices`. Нам потрібно обробити результат, щоб побачити, чи присутні будь-які `tool_calls`. Це дає нам знати, що LLM запитує, щоб викликати конкретний інструмент із аргументами. Додайте наступний код у нижню частину вашого файлу `main.rs`, щоб визначити функцію для обробки відповіді LLM:

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

    // Друкувати вміст, якщо він доступний
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обробляти виклики інструментів
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Додати повідомлення асистента

        // Виконати кожен виклик інструменту
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Додати результат інструменту до повідомлень
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Продовжити розмову з результатами інструменту
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

Якщо `tool_calls` присутні, функція витягує інформацію про інструмент, викликає сервер MCP із запитом інструменту та додає результати до повідомлень розмови. Потім вона продовжує розмову з LLM, і повідомлення оновлюються відповіддю асистента та результатами виклику інструменту.

Щоб витягти інформацію про виклик інструменту, яку LLM повертає для викликів MCP, ми додамо ще одну допоміжну функцію для витягу всього, що потрібно для виконання виклику. Додайте наступний код у нижню частину вашого файлу `main.rs`:

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

Із усіма складовими на місці, тепер ми можемо обробити початковий запит користувача і викликати LLM. Оновіть вашу функцію `main`, включивши наступний код:

```rust
// Розмова LLM із викликами інструментів
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

Це виконає запит до LLM із початковим запитом користувача, який запитує суму двох чисел, та обробить відповідь для динамічної обробки викликів інструментів.

Чудово, ви зробили це!

## Завдання

Візьміть код із вправи та розширте сервер додатковими інструментами. Потім створіть клієнта з LLM, як у вправі, і протестуйте його з різними запитами, щоб переконатися, що всі ваші серверні інструменти викликаються динамічно. Такий спосіб створення клієнта забезпечує чудовий користувацький досвід, оскільки користувачі можуть використовувати підказки замість точних команд клієнта і не помічають виклики серверу MCP.

## Розв’язок

[Розв’язок](/03-GettingStarted/03-llm-client/solution/README.md)

## Основні висновки

- Додавання LLM до вашого клієнта забезпечує кращий спосіб взаємодії користувачів із серверами MCP.
- Потрібно конвертувати відповідь сервера MCP у щось, що LLM може зрозуміти.

## Приклади

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Додаткові ресурси

## Що далі

- Далі: [Використання сервера у Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми і прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Створення клієнта з LLM

> [!NOTE]
> Приклади клієнта Java підключаються через застарілий транспорт HTTP+SSE і
> націлені на SDK API MCP `2025-11-25`. Для нових віддалених клієнтів використовуйте SDK,
> сумісний з `2026-07-28`, та Streamable HTTP.

До цього моменту ви бачили, як створювати сервер і клієнта. Клієнт міг явно викликати сервер для переліку його інструментів, ресурсів та підказок. Проте це не дуже практичний підхід. Ваші користувачі живуть у агентному столітті і очікують використовувати підказки та спілкуватися з LLM замість цього. Їх не цікавить, чи використовуєте ви MCP для зберігання своїх можливостей; вони просто хочуть взаємодіяти за допомогою природної мови. Тож як це вирішити? Рішення — додати LLM до клієнта.

## Огляд

У цьому уроці ми сконцентруємося на додаванні LLM до вашого клієнта і покажемо, як це забезпечує набагато кращий досвід для користувача.

## Цілі навчання

До кінця цього уроку ви зможете:

- Створити клієнта з LLM.
- Безперешкодно взаємодіяти з сервером MCP за допомогою LLM.
- Забезпечити кращий досвід кінцевого користувача на стороні клієнта.

## Підхід

Давайте спробуємо зрозуміти, який підхід нам потрібно застосувати. Додавання LLM здається простим, але чи справді ми так зробимо?

Ось як клієнт буде взаємодіяти із сервером:

1. Встановити з’єднання з сервером.

1. Перелічити можливості, підказки, ресурси та інструменти, зберегти їх схему.

1. Додати LLM та передати збережені можливості й їх схему в форматі, який розуміє LLM.

1. Обробити підказку користувача, передаючи її LLM разом з інструментами, переліченими клієнтом.

Чудово, тепер, коли ми розуміємо, як це зробити на високому рівні, давайте спробуємо це в наступній вправі.

## Вправа: Створення клієнта з LLM

У цій вправі ми навчимося додавати LLM до нашого клієнта.

### Аутентифікація за допомогою персонального токена доступу GitHub

Створення токена на GitHub — це простий процес. Ось як ви можете це зробити:

- Перейдіть у Налаштування GitHub – Клацніть на своє фото профілю у верхньому правому куті та оберіть Налаштування.
- Перейдіть у Налаштування розробника – Прокрутіть вниз і клацніть Налаштування розробника.
- Виберіть Персональні токени доступу – Клацніть на Детальна настройка токенів, потім Створити новий токен.
- Налаштуйте токен – Додайте нотатку для довідки, встановіть дату закінчення дії та оберіть необхідні права доступу (перміси). У цьому випадку не забудьте додати дозвіл Models.
- Створіть і скопіюйте токен – Клацніть Створити токен, і обов’язково скопіюйте його одразу, оскільки побачити його вдруге не вдасться.

### -1- Підключення до сервера

Спершу створимо наш клієнт:

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

У наведеному коді ми:

- Імпортували потрібні бібліотеки
- Створили клас з двома членами, `client` і `openai`, які допоможуть керувати клієнтом та взаємодіяти з LLM відповідно.
- Налаштували екземпляр LLM для використання GitHub Models, встановивши `baseUrl` на адресу inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для з'єднання stdio
server_params = StdioServerParameters(
    command="mcp",  # Виконуваний файл
    args=["run", "server.py"],  # Необов'язкові аргументи командного рядка
    env=None,  # Необов'язкові змінні оточення
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

У наведеному коді ми:

- Імпортували необхідні бібліотеки для MCP
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

Спершу потрібно додати залежності LangChain4j у ваш файл `pom.xml`. Додайте ці залежності для увімкнення інтеграції MCP та OpenAI-сумісного MiniMax API:

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

Встановіть ваш ключ MiniMax API і, опційно, endpoint і модель.
`MINIMAX_MODEL_ID` підтримує `MiniMax-M3` і `MiniMax-M2.7`. Якщо
`OPENAI_BASE_URL` не встановлено, `MINIMAX_REGION` підтримує `global_en` і `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Щоб вибрати endpoint за регіоном, не вказуючи `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Потім створіть свій Java-клас клієнта:

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

        // Створити MCP транспорт для підключення до сервера
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Створити MCP клієнта
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

У наведеному коді ми:

- **Додали залежності LangChain4j**: необхідні для інтеграції MCP та OpenAI-сумісного MiniMax API
- **Імпортували бібліотеки LangChain4j**: для інтеграції MCP та функціональності OpenAI chat model
- **Створили `ChatLanguageModel`**: налаштований для використання MiniMax з вашим ключем MiniMax API, endpoint і підтримуваним ідентифікатором моделі
- **Налаштували HTTP-транспорт**: з використанням Server-Sent Events (SSE) для підключення до сервера MCP
- **Створили клієнт MCP**: який буде обробляти комунікацію із сервером
- **Використали вбудовану підтримку MCP LangChain4j**: що спрощує інтеграцію між LLM і серверами MCP

#### Rust

Цей приклад передбачає, що у вас запущений MCP сервер на Rust. Якщо ні, зверніться до уроку [01-first-server](../01-first-server/README.md), щоб створити сервер.

Коли у вас є сервер MCP на Rust, відкрийте термінал і перейдіть у ту ж директорію, що й сервер. Потім виконайте наступну команду для створення проекту клієнта LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Додайте такі залежності у ваш файл `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Офіційної бібліотеки Rust для OpenAI немає, однак `async-openai` — це [спільнотна бібліотека](https://platform.openai.com/docs/libraries/rust#rust), яка часто використовується.

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

    // TODO: Розмова LLM з викликами інструментів

    Ok(())
}
```

Цей код налаштовує базовий додаток на Rust, який підключатиметься до сервера MCP і GitHub Models для взаємодії з LLM.

> [!IMPORTANT]
> Обов’язково встановіть змінну середовища `OPENAI_API_KEY` вашим токеном GitHub перед запуском додатка.

Чудово, наступним кроком давайте перелічимо можливості сервера.

### -2- Перелік можливостей сервера

Тепер підключимося до сервера і запросимо його можливості:

#### TypeScript

У тому ж класі додайте наступні методи:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // перелік інструментів
    const toolsResult = await this.client.listTools();
}
```

У наведеному коді ми:

- Додали код для підключення до сервера, `connectToServer`.
- Створили метод `run`, відповідальний за обробку логіки додатку. Наразі він лише перелічує інструменти, але незабаром ми додамо більше.

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

- Перелік ресурсів і інструментів та їх вивід. Для інструментів також перелічуємо `inputSchema`, який використаємо пізніше.

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


У попередньому коді ми:

- Перелічили інструменти, доступні на MCP Server
- Для кожного інструменту перелічили ім'я, опис і його схему. Останнє — це те, що ми скоро використаємо, щоб викликати інструменти.

#### Java

```java
// Створіть провайдера інструментів, який автоматично відкриває інструменти MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Провайдер інструментів MCP автоматично обробляє:
// - Перелік доступних інструментів з сервера MCP
// - Конвертацію схем інструментів MCP у формат LangChain4j
// - Керування виконанням інструментів та відповідями
```

У попередньому коді ми:

- Створили `McpToolProvider`, який автоматично виявляє та реєструє всі інструменти з MCP сервера
- Провайдер інструментів внутрішньо обробляє конвертацію між схемами інструментів MCP і форматом інструментів LangChain4j
- Такий підхід абстрагує процес ручного переліку інструментів і конвертації

#### Rust

Отримання інструментів з MCP сервера здійснюється за допомогою методу `list_tools`. У вашій функції `main`, після налаштування MCP клієнта, додайте наступний код:

```rust
// Отримати список інструментів MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертувати функціональність сервера у інструменти LLM

Наступним кроком після переліку можливостей сервера є конвертація їх у формат, який розуміє LLM. Після цього ми можемо надати ці можливості як інструменти нашому LLM.

#### TypeScript

1. Додайте наступний код, щоб конвертувати відповідь від MCP Server у формат інструменту, який може використовувати LLM:

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

    Вищенаведений код приймає відповідь від MCP Server та конвертує її у формат визначення інструменту, який розуміє LLM.

2. Оновімо метод `run`, щоб перелічити можливості сервера:

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

    У попередньому коді ми оновили метод `run`, щоб обробити результат і для кожного запису викликати `openAiToolAdapter`.

#### Python

1. Спершу створимо таку функцію конвертера

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

    У функції вище `convert_to_llm_tools` ми беремо відповідь з MCP інструменту та конвертуємо її у формат, зрозумілий LLM.

2. Тепер оновимо наш код клієнта, щоб використовувати цю функцію так:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тут ми додаємо виклик `convert_to_llm_tool`, щоб конвертувати відповідь MCP інструменту в те, що ми зможемо передати LLM потім.

#### .NET

1. Додамо код для конвертації відповіді MCP інструменту у щось, зрозуміле для LLM

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

У попередньому коді ми:

- Створили функцію `ConvertFrom`, яка приймає ім'я, опис і схему введення.
- Описали функціонал, який створює FunctionDefinition, що передається до ChatCompletionsDefinition. Останнє — те, що розуміє LLM.

2. Подивимось, як ми можемо оновити деякий існуючий код, щоб використовувати цю функцію:

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

// Налаштуйте AI-сервіс з інструментами LLM і MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У попередньому коді ми:

- Визначили простий інтерфейс `Bot` для взаємодії природною мовою
- Використали LangChain4j's `AiServices` для автоматичного зв’язування LLM з провайдером інструментів MCP
- Фреймворк автоматично обробляє конвертацію схем інструментів і виклики функцій поза сценою
- Такий підхід усуває необхідність ручного конвертування інструментів — LangChain4j впорається з усією складністю перетворення MCP інструментів у сумісний з LLM формат

#### Rust

Щоб конвертувати відповідь MCP інструменту у формат, який розуміє LLM, ми додамо допоміжну функцію, яка форматує перелік інструментів. Додайте наступний код у ваш файл `main.rs` нижче функції `main`. Це буде викликатися під час запитів до LLM:

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

Чудово, ми налаштувалися на обробку будь-яких запитів користувача, тож перейдемо до цього наступним кроком.

### -4- Обробка запитів користувача

У цій частині коду ми будемо обробляти запити користувачів.

#### TypeScript

1. Додайте метод, який буде використовуватись для виклику нашого LLM:

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

    У попередньому коді ми:

    - Додали метод `callTools`.
    - Метод приймає відповідь LLM і перевіряє, які інструменти було викликано, якщо такі є:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // виклик інструмента
        }
        ```

    - Викликає інструмент, якщо LLM показує, що його слід викликати:

        ```typescript
        // 2. Виклик інструменту сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Зробити щось з результатом
        // ПОТРІБНО ЗРОБИТИ
        ```

2. Оновіть метод `run`, щоб включити виклики до LLM і виклики `callTools`:

    ```typescript

    // 1. Створіть повідомлення, що є вхідними даними для LLM
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

Чудово, ось повний код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Імпортувати zod для валідації схеми

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можливо, у майбутньому потрібно буде змінити на цю адресу: https://models.github.ai/inference
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
          // Створити схему zod на основі input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Явно вказати тип як "function"
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
    
    
          // 2. Викликати інструмент сервера
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Виконати деякі дії з результатом
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
    
        // 3. Переглянути відповідь LLM, для кожного варіанту перевірити, чи є виклики інструментів
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

1. Додамо деякі імпорти, необхідні для виклику LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Далі додамо функцію, яка викликатиме LLM:

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
            # Необов'язкові параметри
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

    У попередньому коді ми:

    - Передали наші функції, знайдені на MCP сервері та конвертовані, до LLM.
    - Потім викликали LLM з цими функціями.
    - Перевіряємо результат, щоб дізнатись, які функції слід викликати, якщо такі є.
    - Зрештою, передаємо масив функцій для виклику.

3. Останній крок, оновимо наш основний код:

    ```python
    prompt = "Add 2 to 20"

    # запитай у LLM, які інструменти доступні, якщо такі є
    functions_to_call = call_llm(prompt, functions)

    # виклич запропоновані функції
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ось, це був останній крок, у наведеному коді ми:

    - Викликаємо інструмент MCP через `call_tool` використовуючи функцію, яку LLM вважає за потрібне викликати на основі нашого запиту.
    - Виводимо результат виклику інструменту на MCP Server.

#### .NET

1. Покажемо код для виконання запиту prompt до LLM:

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

    У попередньому коді ми:

    - Отримали інструменти з MCP сервера, `var tools = await GetMcpTools()`.
    - Визначили запит користувача `userMessage`.
    - Конструювали об’єкт опцій, що задає модель і інструменти.
    - Зробили запит до LLM.

2. Останній крок, перевіримо, чи LLM вважає за потрібне викликати функцію:

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

    У попередньому коді ми:

    - Перебрали список викликів функцій.
    - Для кожного виклику інструменту розібрали ім'я та аргументи, і викликали інструмент на MCP сервері, використовуючи MCP клієнт. Нарешті, вивели результати.

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

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Виконуйте запити природною мовою, які автоматично використовують інструменти MCP
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

У попередньому коді ми:

- Використовували прості промпти природною мовою для взаємодії з інструментами MCP сервера
- Фреймворк LangChain4j автоматично обробляє:
  - Конвертацію користувацьких промптів у виклики інструментів за потребою
  - Виклик відповідних інструментів MCP на основі рішень LLM
  - Керування потоком розмови між LLM і MCP сервером
- Метод `bot.chat()` повертає відповіді природною мовою, які можуть містити результати виконання MCP інструментів
- Такий підхід забезпечує безшовний користувацький досвід, коли користувачам не потрібно знати про реалізацію MCP

Повний приклад коду:

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


Тут відбувається більшість роботи. Ми викличемо LLM з початковим запитом користувача, а потім обробимо відповідь, щоб перевірити, чи потрібно викликати якісь інструменти. Якщо так, ми викличемо ці інструменти і продовжимо розмову з LLM, поки не знадобляться більше викликів інструментів і у нас не буде остаточної відповіді.

Ми будемо робити кілька викликів до LLM, тому давайте визначимо функцію, яка буде обробляти виклики LLM. Додайте наступну функцію у ваш файл `main.rs`:

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

Ця функція приймає клієнта LLM, список повідомлень (включаючи запит користувача), інструменти з сервера MCP і надсилає запит до LLM, повертаючи відповідь.

Відповідь від LLM міститиме масив `choices`. Нам потрібно буде обробити результат, щоб перевірити, чи присутні `tool_calls`. Це дає нам зрозуміти, що LLM запитує виклик певного інструменту з аргументами. Додайте наступний код у кінець вашого файлу `main.rs` для визначення функції, яка обробляє відповідь LLM:

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

    // Друкувати вміст, якщо доступно
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обробити виклики інструментів
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

Якщо `tool_calls` присутні, функція витягує інформацію про інструмент, викликає сервер MCP з запитом до інструменту, і додає результати до повідомлень розмови. Потім вона продовжує розмову з LLM, і повідомлення оновлюються з відповіддю асистента та результатами виклику інструменту.

Щоб витягти інформацію про виклик інструменту, яку LLM повертає для викликів MCP, ми додамо ще одну допоміжну функцію для вилучення всього, що потрібно для виклику. Додайте наступний код у кінець вашого `main.rs`:

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

Маємо всі складові, тепер можна обробляти початковий запит користувача і викликати LLM. Оновіть вашу функцію `main`, додавши наступний код:

```rust
// Розмова LLM з викликами інструментів
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

Це виконає запит до LLM з початковим запитом користувача, який просить суму двох чисел, і обробить відповідь, щоб динамічно обробляти виклики інструментів.

Чудово, ви зробили це!

## Завдання

Візьміть код із вправи і розширте сервер, додавши ще кілька інструментів. Потім створіть клієнта з LLM, як у вправі, і протестуйте з різними запитами, щоб переконатися, що всі серверні інструменти динамічно викликаються. Такий спосіб створення клієнта забезпечує чудовий користувацький досвід, оскільки користувачі можуть використовувати запити замість точних команд клієнта і не бачать, що викликається якийсь MCP сервер.

## Рішення

[Рішення](./solution/README.md)

## Основні висновки

- Додавання LLM до вашого клієнта забезпечує кращий спосіб взаємодії користувачів із MCP серверами.
- Потрібно конвертувати відповідь сервера MCP у щось, що розуміє LLM.

## Приклади

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Додаткові ресурси

## Що далі

- Наступне: [Використання сервера за допомогою Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
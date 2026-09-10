# Створення клієнта з LLM

До цього часу ви бачили, як створити сервер і клієнта. Клієнт міг явно викликати сервер, щоб перелічити його інструменти, ресурси та підказки. Однак це не дуже практичний підхід. Ваші користувачі живуть в агентську епоху і очікують використовувати підказки та спілкуватися з LLM замість цього. Їх не цікавить, чи використовуєте ви MCP для збереження своїх можливостей; вони просто очікують взаємодії за допомогою природної мови. Тож як це вирішити? Рішення полягає в додаванні LLM до клієнта.

## Огляд

У цьому уроці ми зосередимося на додаванні LLM до вашого клієнта та покажемо, як це забезпечує набагато кращий досвід для вашого користувача.

## Навчальні цілі

До кінця цього уроку ви зможете:

- Створити клієнта з LLM.
- Безшовно взаємодіяти з MCP сервером за допомогою LLM.
- Забезпечити кращий досвід кінцевого користувача на стороні клієнта.

## Підхід

Давайте спробуємо зрозуміти підхід, який ми повинні взяти. Додавання LLM звучить просто, але чи насправді ми це зробимо?

Ось як клієнт буде взаємодіяти з сервером:

1. Встановити з'єднання з сервером.

1. Перелічити можливості, підказки, ресурси та інструменти та зберегти їх схему.

1. Додати LLM і передати збережені можливості та їх схему в форматі, який розуміє LLM.

1. Обробити підказку користувача, передаючи її LLM разом з інструментами, переліченими клієнтом.

Чудово, тепер ми розуміємо, як це зробити на високому рівні, давайте спробуємо це в наведеному нижче вправі.

## Вправа: створення клієнта з LLM

У цій вправі ми навчимося додавати LLM до нашого клієнта.

### Аутентифікація за допомогою особистого токена доступу GitHub

Створення токена GitHub — це простий процес. Ось як ви можете це зробити:

- Перейдіть до налаштувань GitHub – натисніть на свою фотографію профілю у верхньому правому куті та виберіть Налаштування.
- Перейдіть до налаштувань розробника – прокрутіть вниз і натисніть Налаштування розробника.
- Виберіть Особисті токени доступу – натисніть Fine-grained tokens, а потім Створити новий токен.
- Налаштуйте свій токен – додайте примітку для довідки, встановіть дату закінчення дії та виберіть необхідні області (дозволи). У цьому випадку обов’язково додайте дозвіл Models.
- Згенеруйте та скопіюйте токен – натисніть Згенерувати токен і не забудьте скопіювати його одразу, бо більше ви його не побачите.

### -1- Підключення до сервера

Давайте спочатку створимо наш клієнт:

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
- Створили клас із двома членами, `client` і `openai`, які допоможуть нам керувати клієнтом і взаємодіяти з LLM відповідно.
- Налаштували екземпляр LLM для використання GitHub Models, встановивши `baseUrl` на inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для з'єднання stdio
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

Спочатку потрібно додати залежності LangChain4j у ваш файл `pom.xml`. Додайте ці залежності, щоб увімкнути інтеграцію MCP та OpenAI-сумісний MiniMax API:

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

Встановіть ваш ключ MiniMax API і, за бажанням, кінцеву точку та модель.
`MINIMAX_MODEL_ID` підтримує `MiniMax-M3` і `MiniMax-M2.7`. Якщо
`OPENAI_BASE_URL` не встановлено, `MINIMAX_REGION` підтримує `global_en` і `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Щоб замість цього вибрати кінцеву точку за регіоном, пропустіть `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Тоді створіть ваш Java клієнтський клас:

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

У наведеному вище коді ми:

- **Додали залежності LangChain4j**: Необхідні для інтеграції MCP та OpenAI-сумісного MiniMax API
- **Імпортували бібліотеки LangChain4j**: Для інтеграції MCP та функцій OpenAI чат-моделі
- **Створили `ChatLanguageModel`**: Налаштований для використання MiniMax з вашим ключем MiniMax API, кінцевою точкою і підтримуваним ідентифікатором моделі
- **Налаштували HTTP-транспортування**: Використання Server-Sent Events (SSE) для підключення до MCP сервера
- **Створили MCP клієнта**: Який буде обробляти зв’язок з сервером
- **Використали вбудовану підтримку MCP LangChain4j**: Що спрощує інтеграцію між LLM і MCP серверами

#### Rust

Цей приклад припускає, що у вас працює MCP сервер на Rust. Якщо у вас його немає, зверніться до уроку [01-first-server](../01-first-server/README.md) для створення сервера.

Після того, як у вас є MCP сервер на Rust, відкрийте термінал і перейдіть у той же каталог, що й сервер. Потім виконайте наступну команду, щоб створити новий проект клієнта LLM:

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
> Офіційної бібліотеки Rust для OpenAI немає, проте crate `async-openai` — це [бібліотека, що підтримується спільнотою](https://platform.openai.com/docs/libraries/rust#rust), яку зазвичай використовують.

Відкрийте файл `src/main.rs` і замініть його вміст наступним кодом:

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

    // TODO: Розмова з LLM із викликами інструментів

    Ok(())
}
```

Цей код налаштовує базовий додаток на Rust, який буде підключатися до MCP сервера і GitHub Models для взаємодії з LLM.

> [!IMPORTANT]
> Пам’ятайте встановити змінну оточення `OPENAI_API_KEY` з вашим токеном GitHub перед запуском додатка.

Чудово, наступним кроком давайте перелічимо можливості сервера.

### -2- Перелік можливостей сервера

Тепер ми підключимося до сервера і запросимо його можливості:

#### Typescript

У тому ж класі додайте такі методи:

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

У наведеному вище коді ми:

- Додали код для підключення до сервера, `connectToServer`.
- Створили метод `run`, відповідальний за керування потоком нашого додатка. Поки що він лише перелічує інструменти, але скоро ми додамо більше.

#### Python

```python
# Перелічити доступні ресурси
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Перелічити доступні інструменти
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ось що ми додали:

- Перелік ресурсів і інструментів і їх вивід. Для інструментів ми також перелічуємо `inputSchema`, який використаємо пізніше.

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
- Для кожного інструменту перелічили ім’я, опис і його схему. Останнє ми використаємо для виклику інструментів незабаром.

#### Java

```java
// Створіть провайдера інструментів, який автоматично знаходить інструменти MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Провайдер інструментів MCP автоматично обробляє:
// - Перелік доступних інструментів із сервера MCP
// - Конвертацію схем інструментів MCP у формат LangChain4j
// - Управління виконанням інструментів та відповідями
```

У наведеному вище коді ми:

- Створили `McpToolProvider`, що автоматично виявляє та реєструє всі інструменти з MCP сервера
- Постачальник інструментів внутрішньо обробляє перетворення між схемою MCP інструментів і форматом інструментів LangChain4j
- Такий підхід приховує ручний процес переліку інструментів і їх перетворення

#### Rust

Отримання інструментів з MCP сервера здійснюється методом `list_tools`. У вашій функції `main`, після налаштування MCP клієнта, додайте наступний код:

```rust
// Отримати список інструментів MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Перетворення можливостей сервера в інструменти LLM

Наступним кроком після переліку можливостей сервера є їхнє перетворення у формат, який розуміє LLM. Після цього ми можемо надати ці можливості як інструменти нашому LLM.

#### TypeScript

1. Додайте наступний код для перетворення відповіді MCP сервера у формат інструменту, який може використовувати LLM:

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

    Наведений вище код приймає відповідь від MCP сервера і перетворює її в формат визначення інструменту, який розуміє LLM.

2. Давайте оновимо метод `run`, щоб перелічити можливості сервера:

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

    У наведеному вище коді ми оновили метод `run`, щоб пройтися по результату і для кожного запису викликати `openAiToolAdapter`.

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

    У функції `convert_to_llm_tools` вище ми беремо відповідь MCP інструменту і перетворюємо її у формат, який розуміє LLM.

2. Потім оновимо наш код клієнта, щоб скористатися цією функцією таким чином:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тут ми додаємо виклик `convert_to_llm_tool` для перетворення відповіді MCP інструменту у щось, що ми потім передамо LLM.

#### .NET

1. Додамо код для перетворення відповіді MCP інструменту у щось, що розуміє LLM

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

У наведеному вище коді ми:

- Створили функцію `ConvertFrom`, яка приймає ім'я, опис і схему введення.
- Визначили функціональність, яка створює FunctionDefinition передається ChatCompletionsDefinition. Останнє розуміє LLM.

2. Ось як ми можемо оновити існуючий код, щоб скористатися цією функцією:

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
// Створіть інтерфейс Бота для взаємодії природною мовою
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

- Визначили простий інтерфейс `Bot` для взаємодії природною мовою
- Використали LangChain4j's `AiServices`, щоб автоматично зв'язати LLM з MCP провайдером інструментів
- Фреймворк автоматично обробляє конвертацію схеми інструментів і виклик функцій за лаштунками
- Такий підхід усуває ручне перетворення інструментів — LangChain4j справляється з усією складністю конвертації MCP інструментів у формат, сумісний з LLM

#### Rust

Щоб перетворити відповідь MCP інструменту в формат, який розуміє LLM, ми додамо допоміжну функцію, яка форматує перелік інструментів. Додайте наступний код у файл `main.rs` під функцією `main`. Цей код буде викликатися під час запитів до LLM:

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

Чудово, наразі ми налаштували обробку запитів користувача, тож давайте перейдемо до цього.

### -4- Обробка запиту підказки користувача

У цій частині коду ми оброблятимемо запити користувача.

#### TypeScript

1. Додайте метод, який буде використано для виклику нашого LLM:

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
        // ТРЕБА ЗРОБИТИ

        }
    }
    ```

    У наведеному вище коді ми:

    - Додали метод `callTools`.
    - Метод приймає відповідь від LLM і перевіряє, які інструменти були викликані, якщо такі є:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // виклик інструменту
        }
        ```

    - Викликає інструмент, якщо LLM вказує, що його потрібно викликати:

        ```typescript
        // 2. Викликати інструмент сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Зробити щось з результатом
        // ЗРОБИТИ
        ```

2. Оновіть метод `run`, щоб включити виклики LLM і виклик `callTools`:

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

    // 3. Пройдіться по відповіді LLM, для кожного варіанту перевірте, чи є виклики інструментів
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Чудово, давайте переглянемо весь код повністю:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Імпортуйте zod для перевірки схеми

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можливо, потрібно буде змінити на цю URL в майбутньому: https://models.github.ai/inference
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
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. Викличте інструмент сервера
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
    
        // 3. Проаналізуйте відповідь LLM, для кожного варіанту перевірте, чи є виклики інструментів
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

    У наведеному вище коді ми:

    - Передали наші функції, які ми отримали з MCP сервера і конвертували, LLM.
    - Потім викликали LLM з цими функціями.
    - Потім перевіряємо результат, щоб побачити, які функції потрібно викликати, якщо такі є.
    - Нарешті, передаємо масив функцій для виклику.

3. Останній крок — оновити наш основний код:

    ```python
    prompt = "Add 2 to 20"

    # запитати у LLM, які інструменти доступні, якщо є
    functions_to_call = call_llm(prompt, functions)

    # викликати запропоновані функції
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ось це був останній крок, у наведеному коді ми:

    - Викликаємо інструмент MCP через `call_tool`, використовуючи функцію, яку LLM вирішив викликати на основі нашої підказки.
    - Виводимо результат виклику інструменту на MCP сервер.

#### .NET

1. Давайте покажемо код для запиту підказки LLM:

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
    - Створили об'єкт опцій з вказаною моделлю та інструментами.
    - Виконали запит до LLM.

2. Останній крок, давайте перевіримо, чи вважає LLM, що ми повинні викликати якусь функцію:

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

    - Перебрали список викликів функцій.
    - Для кожного виклику інструменту розбираємо ім'я та аргументи і викликаємо інструмент на MCP сервері, використовуючи MCP клієнт. Нарешті виводимо результати.

Ось код повністю:

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

У наведеному коді ми:

- Використали прості підказки природною мовою для взаємодії з інструментами MCP сервера
- Фреймворк LangChain4j автоматично обробляє:
  - Перетворення користувацьких підказок в виклики інструментів, коли це потрібно
  - Виклик відповідних інструментів MCP на основі рішення LLM
  - Керування потоком діалогу між LLM та MCP сервером
- Метод `bot.chat()` повертає природні відповіді, які можуть містити результати виконання інструментів MCP
- Такий підхід забезпечує безшовний досвід користувача, де користувачам не потрібно знати про внутрішню реалізацію MCP

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

Саме тут відбувається більшість роботи. Ми викликаємо LLM з початковою підказкою користувача, потім обробляємо відповідь, щоб дізнатися, чи потрібно викликати інструменти. Якщо так, ми викликаємо ці інструменти і продовжуємо діалог з LLM, доки не перестане бути потреби у викликах інструментів і ми не отримаємо кінцеву відповідь.


Ми будемо здійснювати кілька викликів до LLM, тому давайте визначимо функцію, яка оброблятиме виклик LLM. Додайте наступну функцію до вашого файлу `main.rs`:

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

Ця функція приймає клієнта LLM, список повідомлень (включно з підказкою користувача), інструменти з MCP сервера і надсилає запит до LLM, повертаючи відповідь.

Відповідь від LLM міститиме масив `choices`. Нам потрібно обробити результат, щоб перевірити, чи є там `tool_calls`. Це дає нам знати, що LLM запитує виклик певного інструменту з аргументами. Додайте наступний код в кінець файлу `main.rs`, щоб визначити функцію для обробки відповіді LLM:

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

    // Надрукувати вміст, якщо він доступний
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Обробити виклики інструментів
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Додати повідомлення помічника

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

Якщо присутні `tool_calls`, функція вилучає інформацію про інструмент, викликає MCP сервер із запитом інструменту і додає результати до повідомлень розмови. Потім вона продовжує розмову з LLM, а повідомлення оновлюються відповіддю асистента та результатами виклику інструменту.

Щоб витягти інформацію про виклик інструменту, яку LLM повертає для викликів MCP, ми додамо ще одну допоміжну функцію, щоб отримати все необхідне для здійснення виклику. Додайте наступний код у кінець файлу `main.rs`:

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

З усіма частинами на місці, тепер ми можемо обробити початкову підказку користувача та викликати LLM. Оновіть вашу функцію `main`, додавши наступний код:

```rust
// Діалог з великими мовними моделями з викликами інструментів
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

Це відправить запит до LLM із початковою підказкою користувача про суму двох чисел і обробить відповідь для динамічного оброблення викликів інструментів.

Чудово, ви це зробили!

## Завдання

Візьміть код з вправи і розширте сервер, додавши кілька інструментів. Потім створіть клієнта з LLM, як у вправі, і протестуйте його з різними підказками, щоб упевнитися, що всі інструменти вашого сервера викликаються динамічно. Такий спосіб створення клієнта означає, що кінцевий користувач матиме чудовий досвід, адже він зможе використовувати підказки замість точних команд клієнта і не буде помічати будь-яких викликів до MCP сервера.

## Розв’язок

[Розв’язок](./solution/README.md)

## Основні висновки

- Додавання LLM до вашого клієнта забезпечує кращий спосіб взаємодії користувачів із MCP серверами.
- Потрібно конвертувати відповідь MCP сервера у формат, зрозумілий LLM.

## Приклади

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Додаткові ресурси

## Що далі

- Далі: [Використання сервера через Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
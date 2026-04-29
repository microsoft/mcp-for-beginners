# Створення клієнта з LLM

До цього моменту ви бачили, як створити сервер і клієнта. Клієнт міг явно викликати сервер, щоб перелічити його інструменти, ресурси та підказки. Однак це не дуже практичний підхід. Ваші користувачі живуть в епоху агентності і очікують використовувати підказки та спілкуватися з LLM натомість. Їм байдуже, чи використовуєте ви MCP для збереження своїх можливостей; вони просто очікують взаємодіяти за допомогою природної мови. То як же це вирішити? Рішення — додати LLM до клієнта.

## Огляд

У цьому уроці ми зосередимось на додаванні LLM до вашого клієнта і покажемо, як це забезпечує набагато кращий досвід для вашого користувача.

## Цілі навчання

До кінця цього уроку ви зможете:

- Створити клієнта з LLM.
- Безшовно взаємодіяти з MCP сервером, використовуючи LLM.
- Забезпечити кращий користувацький досвід на стороні клієнта.

## Підхід

Давайте спробуємо зрозуміти підхід, який нам потрібно взяти. Додавання LLM звучить просто, але чи справді ми так зробимо?

Ось як клієнт буде взаємодіяти з сервером:

1. Встановити з’єднання із сервером.

1. Перелічити можливості, підказки, ресурси та інструменти, і зберегти їх схему.

1. Додати LLM і передати збережені можливості та їх схему у форматі, який розуміє LLM.

1. Обробити підказку користувача, передаючи її разом з інструментами, які перелічив клієнт, до LLM.

Чудово, тепер, коли ми розуміємо, як це можна зробити на високому рівні, давайте спробуємо це на практиці у наведеному нижче завданні.

## Завдання: Створення клієнта з LLM

У цьому завданні ми навчимося додавати LLM до нашого клієнта.

### Аутентифікація за допомогою персонального токена доступу GitHub

Створення токена GitHub — це проста процедура. Ось як це можна зробити:

- Перейдіть у Налаштування GitHub – Натисніть на зображення вашого профілю у правому верхньому куті і виберіть Налаштування.
- Перейдіть до Налаштувань розробника – Прокрутіть вниз і натисніть Налаштування розробника.
- Виберіть Персональні токени доступу – Натисніть на Fine-grained tokens, а потім Створити новий токен.
- Налаштуйте свій токен – Додайте примітку для посилання, встановіть дату закінчення терміну дії, та виберіть необхідні сфери доступу (дозволи). У цьому випадку обов’язково додайте дозвіл Models.
- Згенеруйте і скопіюйте токен – Натисніть Створити токен, і обов’язково скопіюйте його одразу, оскільки ви більше не зможете побачити його повторно.

### -1- Підключення до сервера

Давайте спочатку створимо нашого клієнта:

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

У попередньому коді ми:

- Імпортували необхідні бібліотеки
- Створили клас з двома членами, `client` і `openai`, які допомагатимуть нам керувати клієнтом і взаємодіяти з LLM відповідно.
- Налаштували наш екземпляр LLM на використання моделей GitHub, встановивши `baseUrl` для роботи з inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для підключення stdio
server_params = StdioServerParameters(
    command="mcp",  # Виконуваний файл
    args=["run", "server.py"],  # Необов’язкові аргументи командного рядка
    env=None,  # Необов’язкові змінні середовища
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Ініціалізувати підключення
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

У попередньому коді ми:

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

Спочатку вам потрібно додати залежності LangChain4j у файл `pom.xml`. Додайте ці залежності, щоб увімкнути інтеграцію MCP і підтримку моделей GitHub:

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

Потім створіть клас свого Java клієнта:

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
    
    public static void main(String[] args) throws Exception {        // Налаштувати LLM для використання моделей GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Створити MCP-транспорту для підключення до сервера
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Створити MCP-клієнт
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

У попередньому коді ми:

- **Додали залежності LangChain4j**: необхідні для інтеграції MCP, офіційного клієнта OpenAI та підтримки моделей GitHub
- **Імпортували бібліотеки LangChain4j**: для інтеграції MCP і функціональності моделей чат OpenAI
- **Створили `ChatLanguageModel`**: налаштований для використання моделей GitHub з вашим GitHub токеном
- **Налаштували HTTP транспорт**: використовуючи серверні події (SSE) для підключення до MCP сервера
- **Створили клієнта MCP**: який буде обробляти комунікацію із сервером
- **Використали вбудовану підтримку MCP у LangChain4j**: що спрощує інтеграцію між LLM і MCP серверами

#### Rust

Цей приклад припускає, що у вас працює MCP сервер на Rust. Якщо у вас немає такого, поверніться до уроку [01-first-server](../01-first-server/README.md), щоб створити сервер.

Після того, як у вас буде MCP сервер на Rust, відкрийте термінал і перейдіть у ту саму директорію, що й сервер. Потім виконайте наступну команду, щоб створити новий проект клієнта LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Додайте наступні залежності у ваш файл `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Офіційної бібліотеки Rust для OpenAI немає, однак crate `async-openai` є [спільнотною бібліотекою](https://platform.openai.com/docs/libraries/rust#rust), що часто використовується.

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

    // Зробити: Отримати список інструментів MCP

    // Зробити: Розмова LLM з викликами інструментів

    Ok(())
}
```

Цей код налаштовує базовий додаток Rust, який підключатиметься до MCP сервера і моделей GitHub для взаємодії з LLM.

> [!IMPORTANT]
> Перед запуском додатку переконайтеся, що встановили змінну середовища `OPENAI_API_KEY` зі своїм GitHub токеном.

Чудово, наступним кроком давайте перелічимо можливості сервера.

### -2- Перелік можливостей сервера

Тепер ми підключимося до сервера і запросимо його можливості:

#### Typescript

У тому ж класі додайте наступні методи:

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

У попередньому коді ми:

- Додали код для підключення до сервера, `connectToServer`.
- Створили метод `run`, відповідальний за обробку потоку додатку. Поки він просто перелічує інструменти, але скоро ми додамо більше.

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

- Перелічення ресурсів та інструментів і їх вивід. Для інструментів ми також перелічуємо `inputSchema`, який використаємо пізніше.

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

- Перелічили інструменти, доступні на MCP сервері
- Для кожного інструменту вивели ім'я, опис і його схему. Останню ми використаємо для виклику інструментів згодом.

#### Java

```java
// Створіть постачальника інструментів, який автоматично знаходить інструменти MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Постачальник інструментів MCP автоматично виконує:
// - Перелік доступних інструментів з сервера MCP
// - Конвертацію схем інструментів MCP у формат LangChain4j
// - Управління виконанням інструментів та відповідями
```

У попередньому коді ми:

- Створили `McpToolProvider`, який автоматично виявляє та реєструє всі інструменти з MCP сервера
- Провайдер інструментів обробляє конвертацію між схемами інструментів MCP і форматом інструментів LangChain4j внутрішньо
- Такий підхід приховує ручний процес переліку інструментів і їх конвертації

#### Rust

Отримання інструментів із MCP сервера виконується методом `list_tools`. У вашій функції `main`, після налаштування MCP клієнта, додайте наступний код:

```rust
// Отримати список інструментів MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертація можливостей сервера в інструменти для LLM

Наступним кроком після переліку можливостей сервера є конвертація їх у формат, який розуміє LLM. Після цього ми зможемо надати ці можливості як інструменти нашому LLM.

#### TypeScript

1. Додайте наступний код для конвертації відповіді від MCP сервера у формат інструментів, який LLM може використовувати:

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

1. Оновімо метод `run`, щоб перелічити можливості сервера:

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

    У наведеному коді ми оновили метод `run`, щоб пройтися по результатах і для кожного запису викликати `openAiToolAdapter`.

#### Python

1. Спочатку створимо наступну функцію-конвертер

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

    У функції `convert_to_llm_tools` ми приймаємо відповідь MCP інструменту і конвертуємо її у формат, зрозумілий LLM.

1. Далі оновимо код клієнта, щоб використовувати цю функцію так:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тут ми додаємо виклик `convert_to_llm_tool`, щоб конвертувати відповідь MCP інструменту в те, що ми можемо передати LLM пізніше.

#### .NET

1. Додамо код для конвертації відповіді MCP інструменту у щось, що розуміє LLM

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

- Створили функцію `ConvertFrom`, яка приймає ім'я, опис і схему вводу.
- Визначили функціонал, що створює `FunctionDefinition`, який потім передається у `ChatCompletionsDefinition`. Останнє — це те, що розуміє LLM.

1. Оновимо деякий існуючий код, щоб скористатись цією функцією:

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

// Налаштуйте AI-сервіс із інструментами LLM та MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

У попередньому коді ми:

- Визначили простий інтерфейс `Bot` для взаємодії природною мовою
- Використали `AiServices` LangChain4j для автоматичного зв’язування LLM з провайдером інструментів MCP
- Фреймворк автоматично обробляє конвертацію схем інструментів і виклик функцій за кадром
- Цей підхід виключає ручну конвертацію інструментів — LangChain4j бере на себе всю складність конвертації MCP інструментів у формат, сумісний з LLM

#### Rust

Щоб конвертувати відповідь MCP інструменту у формат, який розуміє LLM, ми додамо допоміжну функцію, яка форматуватиме перелік інструментів. Додайте наступний код у ваш файл `main.rs` під функцією `main`. Ця функція викликатиметься при зверненнях до LLM:

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

Чудово, тепер ми готові обробляти запити користувача, тож перейдемо до цього.

### -4- Обробка запиту користувача

У цій частині коду ми оброблятимемо запити користувачів.

#### TypeScript

1. Додайте метод, який використовуватиметься для виклику нашого LLM:

    ```typescript
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

        // 3. Зробити щось із результатом
        // TODO

        }
    }
    ```

    У попередньому коді ми:

    - Додали метод `callTools`.
    - Метод приймає відповідь LLM і перевіряє, які інструменти було викликано, якщо такі були:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // виклик інструмента
        }
        ```

    - Викликає інструмент, якщо LLM указує, що його слід викликати:

        ```typescript
        // 2. Виклик інструменту сервера
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Зробіть щось з результатом
        // ДОРОБИТИ
        ```

1. Оновіть метод `run`, щоб включити виклики LLM і виклик `callTools`:

    ```typescript

    // 1. Створіть повідомлення, які є вхідними даними для LLM
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

    // 3. Перегляньте відповідь LLM, для кожного вибору перевірте, чи є у нього виклики інструментів
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Чудово, давайте подивимось повний код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Імпортувати zod для перевірки схеми

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // можливо, потрібно буде змінити URL на цей у майбутньому: https://models.github.ai/inference
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
            type: "function" as const, // Явно встановити тип як "function"
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
    
          // 3. Зробити щось з результатом
          // ПОТРІБНО ЗРОБИТИ
    
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
    
        // 1. Перебрати відповідь LLM, для кожного варіанту перевірити, чи є виклики інструментів
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
    # великий мовний модель
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Далі додамо функцію, яка викликатиме LLM:

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

    У попередньому коді ми:

    - Передали наші функції, знайдені на MCP сервері і конвертовані, у LLM.
    - Потім викликали LLM з цими функціями.
    - Потім проінспектували результат, щоб побачити, які функції слід викликати, якщо такі є.
    - Нарешті, передаємо масив функцій для виклику.

1. Останній крок — оновимо основний код:

    ```python
    prompt = "Add 2 to 20"

    # запитайте у LLM, які інструменти використовувати, якщо такі є
    functions_to_call = call_llm(prompt, functions)

    # викликати запропоновані функції
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ось і останній крок, у наведеному коді ми:

    - Викликаємо MCP інструмент через `call_tool`, використовуючи функцію, яку LLM вирішило викликати на основі нашої підказки.
    - Виводимо результат виклику інструменту на MCP сервері.

#### .NET

1. Ось код для виконання запиту до LLM:

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
    - Визначили користувацьку підказку `userMessage`.
    - Створили об'єкт опцій із вказанням моделі і інструментів.
    - Зробили запит до LLM.

1. Останній крок — перевірити, чи треба викликати функцію, як вважає LLM:

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

    - Пройшлися по списку викликів функцій.
    - Для кожного виклику інструменту розібрали ім’я та аргументи, викликали інструмент на MCP сервері використовуючи MCP клієнт. Нарешті вивели результати.

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

- Використали прості підказки природньою мовою для взаємодії з інструментами MCP сервера
- Фреймворк LangChain4j автоматично обробляє:
  - Конвертацію підказок користувача у виклики інструментів за потреби
  - Виклик відповідних MCP інструментів на підставі рішення LLM
  - Керування потоком розмови між LLM і MCP сервером
- Метод `bot.chat()` повертає відповіді природною мовою, що можуть містити результати виконання інструментів MCP
- Цей підхід забезпечує безшовний користувацький досвід, де користувачам не потрібно знати про внутрішню реалізацію MCP

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

Ось де відбувається більшість роботи. Ми викликаємо LLM із початковою підказкою користувача, потім обробляємо відповідь, щоб побачити, чи потрібно викликати якісь інструменти. Якщо так, викликаємо їх і продовжуємо діалог із LLM, поки виклики інструментів не припиняться і ми не отримаємо остаточну відповідь.

Ми робитимемо кілька викликів до LLM, тож давайте визначимо функцію, яка оброблятиме виклик LLM. Додайте цю функцію у ваш файл `main.rs`:

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
Відповідь від LLM міститиме масив `choices`. Нам потрібно обробити результат, щоб перевірити, чи присутні якісь `tool_calls`. Це дає нам знати, що LLM запрошує виклик конкретного інструмента з аргументами. Додайте наступний код у кінець вашого файлу `main.rs`, щоб визначити функцію для обробки відповіді LLM:

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

        // Виконати кожен виклик інструмента
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Додати результат інструмента до повідомлень
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Продовжити розмову з результатами інструментів
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

Якщо `tool_calls` присутні, функція вилучає інформацію про інструмент, викликає MCP сервер з відповідним запитом і додає результати до повідомлень розмови. Потім вона продовжує розмову з LLM, а повідомлення оновлюються відповіддю асистента і результатами виклику інструменту.

Щоб вилучити інформацію про виклик інструмента, яку LLM повертає для викликів MCP, ми додамо ще одну допоміжну функцію для вилучення всього необхідного для виклику. Додайте наступний код у кінець вашого файлу `main.rs`:

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

Маючи всі елементи на місці, тепер ми можемо обробляти початковий запит користувача і викликати LLM. Оновіть свою функцію `main`, додавши наступний код:

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

Це зробить запит до LLM із початковим запитом користувача, який просить суму двох чисел, і обробить відповідь для динамічного керування викликами інструментів.

Чудово, ви це зробили!

## Завдання

Візьміть код із вправи та розширте сервер, додавши ще кілька інструментів. Потім створіть клієнт з LLM, як у вправі, і протестуйте його з різними запитами, щоб переконатися, що всі ваші інструменти сервера викликаються динамічно. Такий спосіб створення клієнта означає, що кінцевий користувач отримає відмінний досвід, оскільки зможе користуватися запитами замість точних команд клієнта і не буде підозрювати про будь-які виклики MCP сервера.

## Розв’язок

[Розв’язок](./solution/README.md)

## Головні висновки

- Додавання LLM до вашого клієнта забезпечує кращий спосіб взаємодії користувачів із MCP серверами.
- Вам потрібно конвертувати відповідь MCP сервера у формат, зрозумілий для LLM.

## Приклади

- [Java калькулятор](../samples/java/calculator/README.md)
- [.Net калькулятор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калькулятор](../samples/javascript/README.md)
- [TypeScript калькулятор](../samples/typescript/README.md)
- [Python калькулятор](../../../../03-GettingStarted/samples/python)
- [Rust калькулятор](../../../../03-GettingStarted/samples/rust)

## Додаткові ресурси

## Що далі

- Далі: [Використання сервера через Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу машинного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні трактування, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
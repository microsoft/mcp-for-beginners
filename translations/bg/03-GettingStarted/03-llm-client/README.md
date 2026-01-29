# Създаване на клиент с LLM

Досега видяхте как да създадете сървър и клиент. Клиентът е можел да извиква сървъра експлицитно, за да изброи неговите инструменти, ресурси и подсказки. Въпреки това, това не е много практичен подход. Вашият потребител живее в ерата на агентите и очаква да използва подсказки и да комуникира с LLM, за да го направи. За вашия потребител няма значение дали използвате MCP или не за съхранение на вашите възможности, но те очакват да използват естествен език за взаимодействие. Как да решим това? Решението е да добавим LLM към клиента.

## Преглед

В този урок се фокусираме върху добавянето на LLM към вашия клиент и показваме как това осигурява много по-добро изживяване за вашия потребител.

## Учебни цели

Към края на този урок ще можете да:

- Създавате клиент с LLM.
- Безпроблемно да взаимодействате със сървър MCP, използвайки LLM.
- Да осигурите по-добро изживяване за крайния потребител от страна на клиента.

## Подход

Нека се опитаме да разберем подхода, който трябва да предприемем. Добавянето на LLM звучи просто, но наистина ли ще го направим?

Ето как клиентът ще взаимодейства със сървъра:

1. Установяване на връзка със сървъра.

1. Изброяване на възможностите, подсказките, ресурсите и инструментите и запазване на тяхната схема.

1. Добавяне на LLM и предаване на запазените възможности и тяхната схема във формат, който LLM разбира.

1. Обработка на потребителска подсказка чрез предаване към LLM заедно с инструментите, изброени от клиента.

Страхотно, сега когато разбираме как можем да го направим на високо ниво, нека опитаме това в следващото упражнение.

## Упражнение: Създаване на клиент с LLM

В това упражнение ще научим как да добавим LLM към нашия клиент.

### Автентикация с помощта на GitHub Personal Access Token

Създаването на GitHub токен е лесен процес. Ето как можете да го направите:

- Отидете в GitHub Settings – Кликнете върху профилната си снимка в горния десен ъгъл и изберете Settings.
- Навигирайте до Developer Settings – Превъртете надолу и кликнете върху Developer Settings.
- Изберете Personal Access Tokens – Кликнете върху Fine-grained tokens и след това Generate new token.
- Конфигурирайте своя токен – Добавете бележка за справка, задайте дата на изтичане и изберете необходимите обхвати (разрешения). В този случай се уверете, че сте добавили разрешението Models.
- Генерирайте и копирайте токена – Кликнете Generate token и се уверете, че го копирате веднага, тъй като няма да можете да го видите отново.

### -1- Свързване със сървъра

Нека първо създадем нашия клиент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортиране на zod за валидация на схема

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

В предходния код ние:

- Импортирахме необходимите библиотеки
- Създадохме клас с два члена, `client` и `openai`, които ще ни помогнат да управляваме клиент и да взаимодействаме с LLM съответно.
- Конфигурирахме нашия LLM инстанс да използва GitHub Models, като зададохме `baseUrl` да сочи към inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Създаване на параметри за сървър за stdio връзка
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

В предходния код ние:

- Импортирахме необходимите библиотеки за MCP
- Създадохме клиент

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

Първо, трябва да добавите зависимостите на LangChain4j във вашия `pom.xml` файл. Добавете тези зависимости, за да активирате интеграция с MCP и поддръжка на GitHub Models:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Конфигурирайте LLM да използва GitHub модели
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Създайте MCP транспорт за свързване към сървъра
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Създайте MCP клиент
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

В предходния код ние:

- **Добавихме зависимости на LangChain4j**: Необходими за интеграция с MCP, официален OpenAI клиент и поддръжка на GitHub Models
- **Импортирахме библиотеките на LangChain4j**: За интеграция с MCP и функционалност на OpenAI чат модел
- **Създадохме `ChatLanguageModel`**: Конфигуриран да използва GitHub Models с вашия GitHub токен
- **Настроихме HTTP транспорт**: Използвайки Server-Sent Events (SSE) за връзка със сървъра MCP
- **Създадохме MCP клиент**: Който ще обработва комуникацията със сървъра
- **Използвахме вградената поддръжка на MCP в LangChain4j**: Което опростява интеграцията между LLM и MCP сървъри

#### Rust

Този пример предполага, че имате работещ Rust базиран MCP сървър. Ако нямате такъв, върнете се към урока [01-first-server](../01-first-server/README.md), за да създадете сървъра.

След като имате вашия Rust MCP сървър, отворете терминал и навигирайте до същата директория като сървъра. След това изпълнете следната команда, за да създадете нов проект за LLM клиент:

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

    // TODO: Вземете списък с инструменти на MCP

    // TODO: Разговор с LLM с повиквания към инструменти

    Ok(())
}
```

Този код настройва базово Rust приложение, което ще се свързва със сървър MCP и GitHub Models за взаимодействия с LLM.

> [!IMPORTANT]
> Уверете се, че сте задали променливата на средата `OPENAI_API_KEY` с вашия GitHub токен преди да стартирате приложението.

Страхотно, за следващата стъпка нека изброим възможностите на сървъра.

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

В предходния код ние:

- Добавихме код за свързване със сървъра, `connectToServer`.
- Създадохме метод `run`, отговорен за управлението на потока на приложението. Досега той само изброява инструментите, но скоро ще добавим още.

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

- Изброяване на ресурси и инструменти и ги отпечатахме. За инструментите също изброяваме `inputSchema`, който използваме по-късно.

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
- За всеки инструмент изброихме име, описание и неговата схема. Последното е нещо, което ще използваме скоро за извикване на инструментите.

#### Java

```java
// Създайте доставчик на инструменти, който автоматично открива MCP инструменти
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Доставчикът на MCP инструменти автоматично обработва:
// - Изброяване на наличните инструменти от MCP сървъра
// - Преобразуване на схеми на MCP инструменти във формат LangChain4j
// - Управление на изпълнението на инструменти и отговорите им
```

В предходния код ние:

- Създадохме `McpToolProvider`, който автоматично открива и регистрира всички инструменти от MCP сървъра
- Провайдърът на инструменти обработва конверсията между MCP инструментални схеми и формата на инструментите на LangChain4j вътрешно
- Този подход абстрахира ръчния процес на изброяване и конверсия на инструменти

#### Rust

Извличането на инструменти от MCP сървъра се извършва чрез метода `list_tools`. Във вашата функция `main`, след настройване на MCP клиента, добавете следния код:

```rust
// Вземете списък с инструменти MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертиране на възможностите на сървъра в инструменти за LLM

Следващата стъпка след изброяване на възможностите на сървъра е да ги конвертираме във формат, който LLM разбира. След като го направим, можем да предоставим тези възможности като инструменти на нашия LLM.

#### TypeScript

1. Добавете следния код, за да конвертирате отговор от MCP сървъра във формат на инструмент, който LLM може да използва:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Създайте zod схема въз основа на input_schema
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

    Горният код приема отговор от MCP сървъра и го конвертира във формат на дефиниция на инструмент, който LLM може да разбере.

1. Нека актуализираме метода `run`, за да изброим възможностите на сървъра:

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

    В предходния код актуализирахме метода `run`, за да премине през резултата и за всяка позиция да извика `openAiToolAdapter`.

#### Python

1. Първо, нека създадем следната функция за конверсия

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

    В горната функция `convert_to_llm_tools` приемаме MCP инструментален отговор и го конвертираме във формат, който LLM може да разбере.

1. След това, нека актуализираме нашия клиентски код, за да използва тази функция по следния начин:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тук добавяме извикване на `convert_to_llm_tool`, за да конвертираме MCP инструменталния отговор в нещо, което можем да подадем на LLM по-късно.

#### .NET

1. Нека добавим код за конвертиране на MCP инструменталния отговор в нещо, което LLM може да разбере

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

- Създадохме функция `ConvertFrom`, която приема име, описание и входна схема.
- Дефинирахме функционалност, която създава FunctionDefinition, който се подава на ChatCompletionsDefinition. Последното е нещо, което LLM може да разбере.

1. Нека видим как можем да актуализираме съществуващ код, за да използваме тази функция:

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
// Създайте интерфейс за бот за взаимодействие на естествен език
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

- Дефинирахме прост интерфейс `Bot` за взаимодействия на естествен език
- Използвахме `AiServices` на LangChain4j, за да свържем автоматично LLM с MCP tool provider
- Фреймуъркът автоматично обработва конверсията на инструменталните схеми и извикването на функции зад кулисите
- Този подход елиминира ръчната конверсия на инструменти – LangChain4j се грижи за цялата сложност при конвертиране на MCP инструменти във формат, съвместим с LLM

#### Rust

За да конвертираме MCP инструменталния отговор във формат, който LLM може да разбере, ще добавим помощна функция, която форматира списъка с инструменти. Добавете следния код във вашия `main.rs` файл под функцията `main`. Тази функция ще се извиква при заявки към LLM:

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

Страхотно, сега сме готови да обработваме потребителски заявки, нека се заемем с това.

### -4- Обработка на потребителска подсказка

В тази част от кода ще обработваме потребителски заявки.

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

    В предходния код ние:

    - Добавихме метод `callTools`.
    - Методът приема отговор от LLM и проверява кои инструменти са били извикани, ако има такива:

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
        // TODO
        ```

1. Актуализирайте метода `run`, за да включва извиквания към LLM и извикване на `callTools`:

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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Прегледайте отговора на LLM, за всеки избор проверете дали има повиквания към инструменти
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Страхотно, нека изброим целия код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортиране на zod за валидация на схемата

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
          // Създаване на zod схема базирана на input_schema
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Прегледайте отговора на LLM, за всеки избор проверете дали има извиквания на инструменти
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

1. След това, нека добавим функцията, която ще извиква LLM:

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

    В предходния код ние:

    - Подадохме нашите функции, които намерихме на MCP сървъра и конвертирахме, към LLM.
    - След това извикахме LLM с тези функции.
    - След това инспектираме резултата, за да видим кои функции трябва да извикаме, ако има такива.
    - Накрая подаваме масив от функции за извикване.

1. Последна стъпка, нека актуализираме основния код:

    ```python
    prompt = "Add 2 to 20"

    # попитайте LLM какви инструменти да използва, ако има такива
    functions_to_call = call_llm(prompt, functions)

    # извикайте предложените функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Това беше последната стъпка, в горния код ние:

    - Извикваме MCP инструмент чрез `call_tool`, използвайки функция, която LLM смята, че трябва да извика на база нашата подсказка.
    - Отпечатваме резултата от извикването на инструмента към MCP сървъра.

#### .NET

1. Нека покажем код за извършване на LLM заявка с подсказка:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    В предходния код ние:

    - Взехме инструментите от MCP сървъра, `var tools = await GetMcpTools()`.
    - Дефинирахме потребителска подсказка `userMessage`.
    - Конструирахме обект с опции, задаващ модел и инструменти.
    - Направихме заявка към LLM.

1. Последна стъпка, нека видим дали LLM смята, че трябва да извика функция:

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

    - Обходихме списък с извиквания на функции.
    - За всяко извикване на инструмент, извличаме име и аргументи и извикваме инструмента на MCP сървъра чрез MCP клиента. Накрая отпечатваме резултатите.

Ето целия код:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Изпълнявайте заявки на естествен език, които автоматично използват MCP инструменти
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

- Използвахме прости подсказки на естествен език за взаимодействие с инструментите на MCP сървъра
- Фреймуъркът LangChain4j автоматично обработва:
  - Конвертиране на потребителски подсказки в извиквания на инструменти, когато е необходимо
  - Извикване на подходящите MCP инструменти на база решението на LLM
  - Управление на потока на разговора между LLM и MCP сървъра
- Методът `bot.chat()` връща отговори на естествен език, които могат да включват резултати от изпълнения на MCP инструменти
- Този подход осигурява безпроблемно потребителско изживяване, при което потребителите не трябва да знаят за подлежащата MCP имплементация

Пълен примерен код:

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

Тук се случва по-голямата част от работата. Ще извикаме LLM с началната потребителска подсказка, след това ще обработим отговора, за да видим дали трябва да се извикат инструменти. Ако да, ще извикаме тези инструменти и ще продължим разговора с LLM, докато не са необходими повече извиквания на инструменти и имаме окончателен отговор.

Ще правим множество извиквания към LLM, затова нека дефинираме функция, която ще обработва извикването на LLM. Добавете следната функция във вашия `main.rs` файл:

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

Тази функция приема LLM клиент, списък от съобщения (включително потребителската подсказка), инструменти от MCP сървъра и изпраща заявка към LLM, връщайки отговора.
Отговорът от LLM ще съдържа масив от `choices`. Трябва да обработим резултата, за да видим дали има налични `tool_calls`. Това ни показва, че LLM иска да бъде извикан конкретен инструмент с аргументи. Добавете следния код в края на файла `main.rs`, за да дефинирате функция за обработка на отговора от LLM:

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

    // Обработете повикванията на инструменти
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Добавете съобщение от асистента

        // Изпълнете всяко повикване на инструмент
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Добавете резултата от инструмента към съобщенията
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

Ако има `tool_calls`, функцията извлича информацията за инструмента, извиква MCP сървъра с искането за инструмента и добавя резултатите към съобщенията в разговора. След това продължава разговора с LLM, като съобщенията се обновяват с отговора на асистента и резултатите от извикването на инструмента.

За да извлечем информация за извикване на инструмент, която LLM връща за MCP извиквания, ще добавим още една помощна функция, която да извлича всичко необходимо за извършване на извикването. Добавете следния код в края на файла `main.rs`:

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

С всички части на място, сега можем да обработим началния потребителски въпрос и да извикаме LLM. Обновете функцията `main`, за да включва следния код:

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

Това ще направи заявка към LLM с началния потребителски въпрос, който иска сумата на две числа, и ще обработи отговора, за да се справи динамично с извиквания на инструменти.

Страхотно, успяхте!

## Задача

Вземете кода от упражнението и разширете сървъра с още инструменти. След това създайте клиент с LLM, както в упражнението, и го тествайте с различни въпроси, за да се уверите, че всички инструменти на сървъра се извикват динамично. Този начин на изграждане на клиент осигурява отличен потребителски опит, тъй като потребителите могат да използват въпроси вместо точни клиентски команди и не осъзнават, че се извиква MCP сървър.

## Решение

[Решение](/03-GettingStarted/03-llm-client/solution/README.md)

## Основни изводи

- Добавянето на LLM към вашия клиент предоставя по-добър начин за взаимодействие на потребителите с MCP сървъри.
- Трябва да конвертирате отговора от MCP сървъра в нещо, което LLM може да разбере.

## Примери

- [Java калкулатор](../samples/java/calculator/README.md)
- [.Net калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python)
- [Rust калкулатор](../../../../03-GettingStarted/samples/rust)

## Допълнителни ресурси

## Какво следва

- Следва: [Използване на сървър с Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
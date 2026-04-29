# Създаване на клиент с LLM

До момента видяхте как да създадете сървър и клиент. Клиентът е можел да извиква сървъра експлицитно, за да изброи неговите инструменти, ресурси и подканвания. Въпреки това, това не е много практичен подход. Вашите потребители живеят в агентичната ера и очакват да използват подканвания и да комуникират с LLM вместо това. Те не се интересуват дали използвате MCP за съхранение на възможностите си; те просто очакват да взаимодействат чрез естествен език. Така как решаваме това? Решението е да добавим LLM към клиента.

## Преглед

В този урок се фокусираме върху добавянето на LLM към клиента и показваме как това осигурява много по-добро преживяване за вашия потребител.

## Учебни цели

Към края на този урок ще можете да:

- Създавате клиент с LLM.
- Безпроблемно да взаимодействате със сървър MCP, използвайки LLM.
- Да предоставите по-добро крайно потребителско изживяване от страна на клиента.

## Подход

Нека се опитаме да разберем подхода, който трябва да поемем. Добавянето на LLM звучи просто, но наистина ли ще го направим?

Ето как клиентът ще взаимодейства със сървъра:

1. Установяване на връзка със сървъра.

1. Изброяване на възможностите, подканванията, ресурсите и инструментите, и запазване на тяхната схема.

1. Добавяне на LLM и подаване на запазените възможности и техните схеми във формат, който LLM разбира.

1. Обработка на потребителска подканваща фраза чрез подаване към LLM заедно с инструментите, изброени от клиента.

Страхотно, сега когато разбираме как можем да го направим на високо ниво, нека пробваме това в упражнението по-долу.

## Упражнение: Създаване на клиент с LLM

В това упражнение ще научим как да добавим LLM към нашия клиент.

### Удостоверяване с помощта на GitHub Personal Access Token

Създаването на GitHub токен е прост процес. Ето как можете да го направите:

- Отидете в GitHub Settings – Кликнете върху профилната си снимка в горния десен ъгъл и изберете Settings.
- Отидете в Developer Settings – Превъртете надолу и кликнете върху Developer Settings.
- Изберете Personal Access Tokens – Кликнете на Fine-grained tokens и след това Generate new token.
- Конфигурирайте вашия токен – Добавете бележка за справка, задайте дата на изтичане и изберете необходимите обхвати (разрешения). В този случай се уверете, че добавяте разрешението Models.
- Генерирайте и копирайте токена – Кликнете Generate token и се уверете, че веднага го копирате, тъй като няма да можете да го видите отново.

### -1- Свързване със сървъра

Нека първо създадем нашия клиент:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортирайте zod за валидация на схемата

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
- Създадохме клас с двама членове, `client` и `openai`, които ще ни помагат да управляваме клиента и да взаимодействаме с LLM съответно.
- Конфигурирахме нашия инстанс на LLM да използва GitHub Models като зададохме `baseUrl` към inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Създаване на параметри за сървър за stdio връзка
server_params = StdioServerParameters(
    command="mcp",  # Изпълним файл
    args=["run", "server.py"],  # По избор аргументи на командния ред
    env=None,  # По избор променливи на средата
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

Първо трябва да добавите зависимостите LangChain4j във вашия `pom.xml` файл. Добавете тези зависимости, за да активирате интеграция с MCP и поддръжка на GitHub Models:

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

- **Добавихме зависимости LangChain4j**: необходими за интеграция с MCP, официалния OpenAI клиент и поддръжка на GitHub Models
- **Импортирахме библиотеките LangChain4j**: за интеграция с MCP и функционалност на OpenAI chat модел
- **Създадохме `ChatLanguageModel`**: конфигуриран да използва GitHub Models с вашия GitHub токен
- **Настроихме HTTP трансфер**: използвайки Server-Sent Events (SSE) за свързване със сървъра MCP
- **Създадохме MCP клиент**: който ще се грижи за комуникацията със сървъра
- **Използвахме вградена поддръжка на MCP на LangChain4j**: което опростява интеграцията между LLM и MCP сървъри

#### Rust

Този пример предполага, че имате Rust базиран MCP сървър. Ако нямате такъв, върнете се към урока [01-first-server](../01-first-server/README.md), за да създадете сървъра.

Когато имате Rust MCP сървър, отворете терминал и се насочете към същата директория като сървъра. След това изпълнете следната команда, за да създадете нов проект за LLM клиент:

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

    // TODO: Разговор на LLM с повиквания на инструменти

    Ok(())
}
```

Този код настройва основно Rust приложение, което ще се свързва със сървър MCP и GitHub Models за взаимодействия с LLM.

> [!IMPORTANT]
> Уверете се, че сте задали променливата на околната среда `OPENAI_API_KEY` с вашия GitHub токен преди да стартирате приложението.

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
- Създадохме метод `run`, който се грижи за работния поток на приложението ни. До момента той само изброява инструментите, но скоро ще добавим още.

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

- Изброихме ресурси и инструменти и ги отпечатахме. За инструментите изброяваме и `inputSchema`, който използваме по-късно.

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

- Изброихме наличните инструменти в MCP сървъра
- За всеки инструмент изброихме име, описание и неговата схема. Последната ще използваме скоро, за да извикаме инструментите.

#### Java

```java
// Създаване на доставчик на инструменти, който автоматично открива MCP инструменти
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Доставчикът на MCP инструменти автоматично обработва:
// - Изброяване на наличните инструменти от MCP сървъра
// - Конвертиране на MCP схеми на инструменти във формат LangChain4j
// - Управление на изпълнението на инструментите и отговорите
```

В предходния код ние:

- Създадохме `McpToolProvider`, който автоматично открива и регистрира всички инструменти от MCP сървъра.
- Провайдърът на инструменти обработва конверсията между MCP инструментални схеми и формата на инструментите на LangChain4j вътрешно.
- Този подход абстрахира ръчния процес на изброяване на инструменти и конвертиране.

#### Rust

Извличането на инструменти от MCP сървъра се прави чрез метода `list_tools`. Във вашата функция `main`, след настройване на MCP клиента, добавете следния код:

```rust
// Вземете списък с инструменти MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Конвертиране на възможностите на сървъра в LLM инструменти

Следващата стъпка след изброяването на възможностите на сървъра е да ги конвертираме във формат, който LLM разбира. След това можем да предоставим тези възможности като инструменти на нашия LLM.

#### TypeScript

1. Добавете следния код за конвертиране на отговор от MCP сървър в инструментален формат, който LLM може да използва:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Създайте zod схема въз основа на input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Изрично задайте тип "function"
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

    Горният код приема отговор от MCP сървъра и го конвертира в дефиниция на инструмент, която LLM може да разбере.

1. След това обновете метода `run`, за да изброява възможностите на сървъра:

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

    В предходния код обновихме метода `run`, който преминава през резултата и за всеки запис извиква `openAiToolAdapter`.

#### Python

1. Първо нека създадем следната функция за конвертиране:

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

    В горната функция `convert_to_llm_tools` приемаме отговор от MCP инструмент и го преобразуваме във формат, който LLM може да разбере.

1. След това обновете клиентския код да използва тази функция така:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Тук добавяме извикване на `convert_to_llm_tool` за конвертиране на MCP инструменталния отговор в нещо, което можем по-късно да подадем на LLM.

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
- Определихме функционалност, която създава FunctionDefinition, който се подава към ChatCompletionsDefinition. Последното е нещо, което LLM разбира.

1. Нека видим как можем да обновим съществуващ код, за да използваме горната функция:

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
- Използвахме LangChain4j `AiServices` за автоматично свързване на LLM с MCP tool provider
- Фреймуъркът автоматично се грижи за конверсията на схемите и извикванията на функциите зад кулисите
- Този подход елиминира ръчната конверсия на инструменти - LangChain4j се справя с цялата сложност на конвертирането на MCP инструменти към формат съвместим с LLM

#### Rust

За да конвертираме MCP инструменталния отговор във формат, който LLM може да разбере, ще добавим помощна функция, която форматира списъка с инструменти. Добавете следния код в `main.rs` под функцията `main`. Това ще се извиква при правене на заявки към LLM:

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

Страхотно, сега сме готови да обработваме заявките на потребителите, нека да го направим следващо.

### -4- Обработка на заявка с подканване от потребител

В тази част от кода ще обработваме заявки от потребителя.

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

    - Извиква инструмент, ако LLM указва, че трябва да бъде извикан:

        ```typescript
        // 2. Извикайте инструмента на сървъра
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Направете нещо с резултата
        // ЗА НАПРАВA
        ```

1. Обновете метода `run`, за да включва извиквания към LLM и да извиква `callTools`:

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

    // 3. Преглед на отговора от LLM, за всяко избиране проверете дали има повиквания към инструменти
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Страхотно, нека изредим целия код:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Импортиране на zod за валидация на схема

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // може да се наложи да се промени на този URL в бъдеще: https://models.github.ai/inference
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
            type: "function" as const, // Ясно задаване на тип "function"
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
    
          // 3. Направи нещо с резултата
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
    
        // 1. Прегледай LLM отговор, за всяка опция, провери дали има извиквания на инструменти
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

1. Нека добавим някои нужни импорти за извикване на LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. След това добавете функцията, която ще извика LLM:

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
            # Опционални параметри
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

    - Подадохме функциите, които намерихме на MCP сървъра и конвертирахме, към LLM.
    - След това извикахме LLM с тези функции.
    - След това проверяваме резултата, за да видим кои функции трябва да извикаме, ако има такива.
    - Накрая подаваме масив от функции за извикване.

1. Последна стъпка, нека обновим основния код:

    ```python
    prompt = "Add 2 to 20"

    # попитай LLM кои инструменти да се използват, ако има такива
    functions_to_call = call_llm(prompt, functions)

    # извикай предложените функции
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Това беше последната стъпка, в горния код ние:

    - Извикваме MCP инструмент чрез `call_tool`, използвайки функцията, която LLM реши, че трябва да извика въз основа на нашата подканваща фраза.
    - Отпечатваме резултата от извикването към MCP сървъра.

#### .NET

1. Нека покажем код за заявка към LLM с подканване:

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

    - Взехме инструментите от MCP сървъра, `var tools = await GetMcpTools()`.
    - Дефинирахме потребителско подканване `userMessage`.
    - Създадохме обект с опции, указващи модел и инструменти.
    - Направихме заявка към LLM.

1. Още една стъпка, нека проверим дали LLM смята, че трябва да извика функция:

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
    - За всяко извикване на инструмент парсираме име и аргументи и извикваме инструмента на MCP сървъра с помощта на MCP клиента. Накрая отпечатваме резултатите.

Ето целия код:

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

- Използвахме прости подканвания на естествен език за взаимодействие с инструментите на MCP сървъра
- Фреймуъркът LangChain4j автоматично се грижи за:
  - Конвертиране на подканванията на потребителя в извиквания на инструменти, когато е необходимо
  - Извикване на подходящите инструменти на MCP въз основа на решението на LLM
  - Управление на потока на разговор между LLM и MCP сървъра
- Методът `bot.chat()` връща естествени езикови отговори, които може да включват резултати от изпълнението на инструменти на MCP
- Този подход предоставя безпроблемно потребителско изживяване, при което потребителите не трябва да знаят за основната имплементация MCP

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

Тук се извършва основната част от работата. Ще извикаме LLM с първоначалната подканваща фраза на потребителя, след което ще обработим отговора, за да видим дали трябва да се извикат инструменти. Ако е така, ще извикаме тези инструменти и ще продължим разговора с LLM, докато не са необходими повече извиквания на инструменти и имаме окончателен отговор.

Ще правим множество извиквания към LLM, затова нека дефинираме функция, която ще обработва извикването към LLM. Добавете следната функция във вашия `main.rs` файл:

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

Тази функция приема LLM клиента, списък с съобщения (включително потребителската подканваща фраза), инструменти от MCP сървъра, и изпраща заявка към LLM, връщайки отговора.
Отговорът от LLM ще съдържа масив от `choices`. Трябва да обработим резултата, за да видим дали са налични `tool_calls`. Това ни уведомява, че LLM иска конкретен инструмент да бъде извикан с аргументи. Добавете следния код в края на вашия файл `main.rs`, за да дефинирате функция за обработка на отговора от LLM:

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

        // Продължете разговора с резултатите от инструментите
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

Ако има `tool_calls`, той извлича информацията за инструмента, извиква MCP сървъра с искането за инструмента и добавя резултатите към съобщенията в разговора. След това продължава разговора с LLM и съобщенията се обновяват с отговора на асистента и резултатите от извикването на инструмента.

За да извлечем информацията за извикване на инструмент, която LLM връща за MCP повиквания, ще добавим още една помощна функция за извличане на всичко необходимо за извикването. Добавете следния код в края на вашия файл `main.rs`:

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

С всички парчета на място, вече можем да обработим първоначалния потребителски въпрос и да извикаме LLM. Обновете функцията `main`, за да включва следния код:

```rust
// Разговор с LLM и повиквания към инструменти
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

Това ще извърши заявка към LLM с първоначалния потребителски въпрос, питайки за сумата на две числа, и ще обработи отговора, за да се справи динамично с извиквания на инструменти.

Чудесно, успяхте!

## Задание

Вземете кода от упражнението и изградете сървъра с още няколко инструмента. След това създайте клиент с LLM, както в упражнението, и го тествайте с различни въпроси, за да се уверите, че всички ваши инструменти на сървъра се извикват динамично. Този начин на изграждане на клиент означава, че крайният потребител ще има страхотно потребителско изживяване, тъй като може да използва въпроси вместо точни клиентски команди и да не забелязва извикването на MCP сървър.

## Решение

[Решение](./solution/README.md)

## Основни изводи

- Добавянето на LLM към вашия клиент предоставя по-добър начин за потребителите да взаимодействат с MCP сървъри.
- Трябва да конвертирате отговора от MCP сървъра в нещо, което LLM може да разбере.

## Примери

- [Java Календар](../samples/java/calculator/README.md)
- [.Net Календар](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Календар](../samples/javascript/README.md)
- [TypeScript Календар](../samples/typescript/README.md)
- [Python Календар](../../../../03-GettingStarted/samples/python)
- [Rust Календар](../../../../03-GettingStarted/samples/rust)

## Допълнителни ресурси

## Какво следва

- Следва: [Използване на сървър с Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческия услуж [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на оригиналния език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
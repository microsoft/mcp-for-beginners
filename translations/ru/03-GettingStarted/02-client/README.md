# Создание клиента

Клиенты — это пользовательские приложения или скрипты, которые напрямую взаимодействуют с сервером MCP для запроса ресурсов, инструментов и подсказок. В отличие от использования инструмента инспектора, который предоставляет графический интерфейс для взаимодействия с сервером, написание собственного клиента позволяет осуществлять программные и автоматизированные взаимодействия. Это дает разработчикам возможность интегрировать возможности MCP в свои рабочие процессы, автоматизировать задачи и создавать индивидуальные решения, адаптированные под конкретные потребности.

## Обзор

В этом уроке рассматривается концепция клиентов в экосистеме протокола Model Context Protocol (MCP). Вы узнаете, как написать собственного клиента и подключить его к серверу MCP.

## Цели обучения

К концу урока вы сможете:

- Понимать, что может делать клиент.
- Написать собственного клиента.
- Подключиться и протестировать клиента с сервером MCP, чтобы убедиться, что он работает как ожидается.

## Что входит в написание клиента?

Чтобы написать клиента, вам нужно сделать следующее:

- **Импортировать правильные библиотеки**. Вы будете использовать ту же библиотеку, что и раньше, только разные конструкции.
- **Создать экземпляр клиента**. Это включает создание экземпляра клиента и подключение его к выбранному способу транспортировки.
- **Решить, какие ресурсы перечислять**. Ваш сервер MCP содержит ресурсы, инструменты и подсказки, вам нужно решить, какие из них перечислять.
- **Интегрировать клиента в хост-приложение**. Как только вы узнаете возможности сервера, нужно интегрировать это в ваше хост-приложение, так чтобы при вводе пользователем подсказки или другой команды вызывалась соответствующая функция сервера.

Теперь, когда мы в общих чертах понимаем, что предстоит сделать, давайте рассмотрим пример.

### Пример клиента

Рассмотрим этот пример клиента:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// Список подсказок
const prompts = await client.listPrompts();

// Получить подсказку
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Список ресурсов
const resources = await client.listResources();

// Прочитать ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Вызвать инструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

В приведённом выше коде мы:

- Импортировали библиотеки
- Создали экземпляр клиента и подключили его, используя stdio в качестве транспорта.
- Перечислили подсказки, ресурсы и инструменты и вызвали их все.

Вот и всё, клиент, который может общаться с сервером MCP.

В следующем упражнении мы подробно разберём каждый фрагмент кода и объясним, что происходит.

## Упражнение: написание клиента

Как уже говорилось, давайте потратим время на объяснение кода, и вы можете писать код вместе с уроком, если хотите.

### -1- Импорт библиотек

Давайте импортируем необходимые библиотеки — нам нужны ссылки на клиента и выбранный транспортный протокол stdio. stdio — это протокол для работы на вашем локальном компьютере. SSE — другой транспортный протокол, который мы покажем в будущих главах, но пока продолжим использовать stdio.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Для Java вы создадите клиента, который подключается к серверу MCP из предыдущего упражнения. Используя ту же структуру проекта Java Spring Boot из [Начало работы с MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), создайте новый класс Java с именем `SDKClient` в папке `src/main/java/com/microsoft/mcp/sample/client/` и добавьте следующие импорты:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

Вам потребуется добавить следующие зависимости в файл `Cargo.toml`.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

Затем вы можете импортировать необходимые библиотеки в код клиента.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Переходим к созданию экземпляров.

### -2- Создание экземпляра клиента и транспорта

Нам нужно создать экземпляр транспорта и клиента:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

В приведённом коде мы:

- Создали экземпляр транспорта stdio. Обратите внимание, как указаны команда и аргументы для запуска сервера — это то, что нам нужно при создании клиента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Создали экземпляр клиента, указав имя и версию.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Подключили клиента к выбранному транспорту.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Создать параметры сервера для соединения через stdio
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

В приведённом коде мы:

- Импортировали необходимые библиотеки
- Создали объект параметров сервера, который будем использовать для запуска сервера и подключения к нему клиента.
- Определили метод `run`, который запускает `stdio_client`, запускающий сессию клиента.
- Создали точку входа, передав метод `run` в `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

В приведённом коде мы:

- Импортировали нужные библиотеки.
- Создали транспорт stdio и клиента `mcpClient`. Этот клиент мы будем использовать для перечисления и вызова функций на сервере MCP.

Обратите внимание, что в "Arguments" можно указать либо *.csproj*, либо исполняемый файл.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // Ваша клиентская логика располагается здесь
    }
}
```

В приведённом коде мы:

- Создали метод main, который настраивает транспорт SSE, указывающий на `http://localhost:8080`, где будет работать наш сервер MCP.
- Создали класс клиента, принимающий транспорт как параметр конструктора.
- В методе `run` создали синхронный MCP-клиент с использованием транспорта и инициализировали соединение.
- Использовали транспорт SSE (Server-Sent Events), подходящий для HTTP-коммуникации с сервером MCP на базе Java Spring Boot.

#### Rust

Обратите внимание, что клиент Rust предполагает, что сервер — это соседний проект с именем "calculator-server" в той же директории. Код ниже запустит сервер и подключится к нему.

```rust
async fn main() -> Result<(), RmcpError> {
    // Предположим, что сервер — это родственный проект с именем "calculator-server" в той же директории
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Инициализация

    // TODO: Список инструментов

    // TODO: Вызвать инструмент add с аргументами = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Перечисление функций сервера

Теперь у нас есть клиент, который может подключаться, если запущена программа. Однако он еще не перечисляет функции сервера, давайте сделаем это:

#### TypeScript

```typescript
// Список подсказок
const prompts = await client.listPrompts();

// Список ресурсов
const resources = await client.listResources();

// список инструментов
const tools = await client.listTools();
```

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
```

Здесь мы перечисляем доступные ресурсы `list_resources()` и инструменты `list_tools` и выводим их.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Пример выше показывает, как можно перечислить инструменты на сервере. Для каждого инструмента выводим его имя.

#### Java

```java
// Перечислите и продемонстрируйте инструменты
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Вы также можете отправить ping на сервер, чтобы проверить соединение
client.ping();
```

В приведенном коде мы:

- Вызвали `listTools()` для получения всех доступных инструментов на сервере MCP.
- Использовали `ping()`, чтобы проверить, что подключение к серверу работает.
- В `ListToolsResult` содержится информация обо всех инструментах, включая имена, описания и схемы входных данных.

Отлично, теперь у нас есть все функции. Но когда их использовать? Этот клиент достаточно простой: нужно явно вызывать функции, когда они нужны. В следующей главе мы создадим более продвинутого клиента с доступом к собственной большой языковой модели, LLM. А пока давайте посмотрим, как вызвать функции на сервере:

#### Rust

В главной функции после инициализации клиента можно инициализировать сервер и перечислить некоторые его функции.

```rust
// Инициализировать
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Список инструментов
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Вызов функций

Чтобы вызвать функции, нужно указать правильные аргументы, а в некоторых случаях и имя вызываемой функции.

#### TypeScript

```typescript

// Читать ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Вызвать инструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// вызвать подсказку
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

В приведённом коде мы:

- Считываем ресурс, вызывая `readResource()` с указанным `uri`. Вот как это, скорее всего, выглядит на сервере:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    Значение `uri` — `file://example.txt`, соответствует `file://{name}` на сервере. `example.txt` будет сопоставлен с `name`.

- Вызываем инструмент, передавая его `name` и `arguments`, например так:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Получаем подсказку, вызывая `getPrompt()` с `name` и `arguments`. Серверный код примерно такой:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    В итоге ваш код клиента будет выглядеть так, чтобы соответствовать серверной декларации:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Читать ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Вызвать инструмент
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

В приведённом коде мы:

- Вызвали ресурс `greeting` с помощью `read_resource`.
- Вызвали инструмент `add` с помощью `call_tool`.

#### .NET

1. Добавим код для вызова инструмента:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Чтобы вывести результат, используем этот код:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Вызов различных калькуляторных инструментов
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

В приведённом коде мы:

- Вызвали несколько инструментов калькулятора с помощью метода `callTool()` и объектов `CallToolRequest`.
- Каждый вызов инструмента указывает имя инструмента и `Map` с необходимыми параметрами.
- Инструменты на сервере ожидают определённые имена параметров (например, "a", "b" для математических операций).
- Результаты возвращаются в объектах `CallToolResult`, содержащих ответ с сервера.

#### Rust

```rust
// Вызов инструмента add с аргументами = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Запуск клиента

Чтобы запустить клиента, введите следующую команду в терминале:

#### TypeScript

Добавьте следующий скрипт в раздел "scripts" вашего *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Запустите клиента с помощью команды:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Сначала убедитесь, что ваш сервер MCP запущен по адресу `http://localhost:8080`. Затем запустите клиента:

```bash
# Соберите ваш проект
./mvnw clean compile

# Запустите клиент
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Или запустите полный проект клиента, предоставленный в папке решения `03-GettingStarted\02-client\solution\java`:

```bash
# Перейти в каталог решения
cd 03-GettingStarted/02-client/solution/java

# Собрать и запустить JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Задание

В этом задании вы используете полученные знания для создания собственного клиента.

Вот сервер, который вы можете использовать и к которому нужно обращаться через клиентский код. Попробуйте добавить больше функций к серверу, чтобы сделать его интереснее.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Создать MCP сервер
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Добавить инструмент для сложения
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавить динамический ресурс приветствия
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Начать получать сообщения с stdin и отправлять сообщения на stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Создать MCP сервер
mcp = FastMCP("Demo")


# Добавить инструмент сложения
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавить динамический ресурс приветствия
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

Посмотрите этот проект, чтобы узнать, как [добавлять подсказки и ресурсы](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Также ознакомьтесь с этим ссылкой, чтобы узнать, как вызывать [подсказки и ресурсы](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предыдущем разделе](../../../../03-GettingStarted/01-first-server) вы узнали, как создать простой MCP сервер на Rust. Вы можете продолжать на этом строить или посмотреть примеры MCP серверов на Rust по этой ссылке: [Примеры MCP серверов](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

**Папка решения** содержит полный, готовый к запуску код клиентов, демонстрирующий все концепции, рассмотренные в этом уроке. Каждое решение включает как клиентский, так и серверный код, организованные в отдельные самостоятельные проекты.

### 📁 Структура решения

Директория решения организована по языкам программирования:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 Что включает каждое решение

Каждый язык представлен следующими элементами:

- **Полной реализацией клиента** со всеми функциями из урока
- **Рабочей структурой проекта** с правильными зависимостями и конфигурацией
- **Скриптами сборки и запуска** для удобной настройки и выполнения
- **Подробной инструкцией README** со специфическими для языка указаниями
- **Обработкой ошибок** и примерами обработки результатов

### 📖 Использование решений

1. **Перейдите в папку нужного языкового решения**:

   ```bash
   cd solution/typescript/    # Для TypeScript
   cd solution/java/          # Для Java
   cd solution/python/        # Для Python
   cd solution/dotnet/        # Для .NET
   ```

2. **Следуйте инструкциям README** в каждой папке для:
   - Установки зависимостей
   - Сборки проекта
   - Запуска клиента

3. **Пример вывода, который вы должны увидеть:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Для полной документации и пошаговых инструкций смотрите: **[📖 Документация решения](./solution/README.md)**

## 🎯 Полные примеры

Мы предоставили полнофункциональные, рабочие реализации клиентов для всех языков программирования, рассмотренных в этом уроке. Эти примеры демонстрируют полную функциональность, описанную выше, и могут использоваться в качестве эталонов или отправных точек для ваших собственных проектов.

### Доступные полные примеры

| Язык  | Файл | Описание |
|-------|-------|----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Полный клиент на Java с SSE транспортом и подробной обработкой ошибок |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Полный клиент на C# с stdio транспортом и автоматическим запуском сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Полный клиент на TypeScript с полной поддержкой протокола MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Полный клиент на Python с использованием async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Полный клиент на Rust с использованием Tokio для асинхронных операций |

Каждый полный пример включает:

- ✅ **Установление соединения** и обработку ошибок
- ✅ **Обнаружение сервера** (инструменты, ресурсы, подсказки, где применимо)
- ✅ **Операции калькулятора** (сложение, вычитание, умножение, деление, помощь)
- ✅ **Обработку результатов** и форматированный вывод
- ✅ **Всестороннюю обработку ошибок**

- ✅ **Чистый, документированный код** с пошаговыми комментариями

### Начало работы с полными примерами

1. **Выберите предпочтительный язык** из таблицы выше
2. **Изучите полный файл примера**, чтобы понять полную реализацию
3. **Запустите пример** согласно инструкциям в [`complete_examples.md`](./complete_examples.md)
4. **Измените и расширьте** пример под ваш конкретный случай использования

Для подробной документации о запуске и настройке этих примеров смотрите: **[📖 Документация по полным примерам](./complete_examples.md)**

### 💡 Решение против полных примеров

| **Папка с решением** | **Полные примеры** |
|--------------------|--------------------- |
| Полная структура проекта с файлами сборки | Однофайловые реализации |
| Готово к запуску с зависимостями | Сфокусированные примеры кода |
| Настройка, приближенная к продакшену | Образовательная справка |
| Инструменты для конкретного языка | Сравнение между языками |

Оба подхода ценны — используйте **папку с решением** для полноценных проектов и **полные примеры** для обучения и справки.

## Основные выводы

Основные выводы этой главы о клиентах следующие:

- Могут использоваться как для обнаружения, так и для вызова функций на сервере.
- Могут запускать сервер, пока он сам стартует (как в этой главе), но клиенты могут подключаться и к уже запущенным серверам.
- Отличный способ протестировать возможности сервера в дополнение к альтернативам, таким как Inspector, как было описано в предыдущей главе.

## Дополнительные ресурсы

- [Создание клиентов в MCP](https://modelcontextprotocol.io/quickstart/client)

## Примеры

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .NET](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Что дальше

- Далее: [Создание клиента с LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
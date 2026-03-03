# Создание клиента

Клиенты — это пользовательские приложения или скрипты, которые взаимодействуют напрямую с MCP Server для запроса ресурсов, инструментов и подсказок. В отличие от использования инструмента инспектора, который предоставляет графический интерфейс для взаимодействия с сервером, написание собственного клиента позволяет осуществлять программное и автоматизированное взаимодействие. Это позволяет разработчикам интегрировать возможности MCP в свои рабочие процессы, автоматизировать задачи и создавать пользовательские решения, адаптированные к конкретным требованиям.

## Обзор

Этот урок вводит понятие клиентов в экосистеме Model Context Protocol (MCP). Вы научитесь писать собственного клиента и подключать его к MCP Server.

## Цели обучения

По окончании урока вы сможете:

- Понимать, что может делать клиент.
- Написать собственного клиента.
- Подключить и протестировать клиента с сервером MCP, чтобы убедиться, что он работает как ожидается.

## Что нужно для написания клиента?

Чтобы написать клиента, необходимо сделать следующее:

- **Импортировать нужные библиотеки**. Вы будете использовать ту же библиотеку, что и раньше, только другие конструкции.
- **Создать экземпляр клиента**. Это будет означать создание экземпляра клиента и подключение его к выбранному методу транспорта.
- **Решить, какие ресурсы отображать**. Ваш MCP сервер содержит ресурсы, инструменты и подсказки, нужно выбрать, какие из них показывать.
- **Интегрировать клиента в хост-приложение**. Как только вы узнаете возможности сервера, нужно интегрировать это в хост-приложение, чтобы при вводе пользователем подсказки или другой команды вызывалась соответствующая функция сервера.

Теперь, когда мы в общих чертах понимаем, что предстоит сделать, давайте посмотрим следующий пример.

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
- Создали экземпляр клиента и подключились к серверу через stdio транспорт.
- Просмотрели списки подсказок, ресурсов и инструментов и вызвали их все.

Вот и всё — клиент, который может общаться с MCP Server.

Давайте подробнее рассмотрим каждый фрагмент кода в следующем упражнении и объясним, что происходит.

## Упражнение: Написание клиента

Как говорилось выше, давайте подробно объясним код, и при желании следуйте за нами в написании.

### -1- Импорт библиотек

Импортируем необходимые библиотеки — нам нужны ссылки на клиента и на выбранный протокол транспорта, stdio. stdio — протокол для программ, которые запускаются на вашей локальной машине. SSE — другой протокол, который мы покажем в будущих главах, это ваша вторая опция. А пока продолжим со stdio.

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

Для Java создайте клиента, который подключается к MCP серверу из предыдущего упражнения. Используя ту же структуру проекта Java Spring Boot из [Начало работы с MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), создайте новый класс Java с именем `SDKClient` в папке `src/main/java/com/microsoft/mcp/sample/client/` и добавьте следующие импорты:

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

В файл `Cargo.toml` необходимо добавить следующие зависимости.

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

Затем можно импортировать нужные библиотеки в коде клиента.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Переходим к созданию экземпляра.

### -2- Создание экземпляра клиента и транспорта

Нужно создать экземпляр транспорта и экземпляр нашего клиента:

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

В предыдущем коде мы:

- Создали экземпляр транспорта stdio. Обратите внимание, как здесь указываются команда и аргументы запуска сервера — это то, что нам нужно для создания клиента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Создали экземпляр клиента с именем и версией.

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

# Создать параметры сервера для stdio соединения
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

В представленном коде мы:

- Импортировали необходимые библиотеки
- Создали объект параметров сервера, который используется для запуска сервера, чтобы клиент мог подключиться к нему.
- Определили метод `run`, который в свою очередь вызывает `stdio_client`, запускающий сессию клиента.
- Создали точку входа, где вызываем `asyncio.run` с методом `run`.

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

В предыдущем коде мы:

- Импортировали необходимые библиотеки.
- Создали транспорт stdio и экземпляр клиента под названием `mcpClient`. Последний используется для получения списка и вызова функций MCP Server.

Обратите внимание, в "Arguments" можно указать либо *.csproj*, либо исполняемый файл.

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
        
        // Ваша клиентская логика идет сюда
    }
}
```

В предыдущем коде мы:

- Создали метод main, который настраивает транспорт SSE, указывающий на `http://localhost:8080`, где будет запущен наш MCP сервер.
- Создали класс клиента, принимающий транспорт в конструкторе.
- В методе `run` создали синхронного MCP клиента с помощью транспорта и инициализировали подключение.
- Использовали транспорт SSE (Server-Sent Events), подходящий для HTTP-связи с MCP серверами на Java Spring Boot.

#### Rust

Обратите внимание, что этот Rust клиент предполагает, что сервер — это соседний проект с именем "calculator-server" в той же директории. Код ниже запускает сервер и подключается к нему.

```rust
async fn main() -> Result<(), RmcpError> {
    // Предположим, что сервер является сестринским проектом с именем "calculator-server" в той же директории
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

    // TODO: Инициализировать

    // TODO: Список инструментов

    // TODO: Вызвать инструмент add с аргументами = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Просмотр возможностей сервера

Теперь у нас есть клиент, который сможет подключиться при запуске программы. Но пока он не отображает список возможностей, давайте сделаем это:

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
# Перечислить доступные ресурсы
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Перечислить доступные инструменты
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Здесь мы выводим доступные ресурсы функцией `list_resources()` и инструменты `list_tools` и печатаем их.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Пример показывает, как получить список инструментов на сервере. Для каждого инструмента затем выводим имя.

#### Java

```java
// Перечислите и продемонстрируйте инструменты
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Вы также можете выполнить ping сервера, чтобы проверить соединение
client.ping();
```

В предыдущем коде мы:

- Вызвали `listTools()` для получения всех доступных инструментов с MCP сервера.
- Использовали `ping()` для проверки связи с сервером.
- `ListToolsResult` содержит информацию о всех инструментах, включая их имена, описания и схемы входных данных.

Отлично, теперь собрали все возможности. Вопрос, когда их использовать? Этот клиент достаточно простой — чтобы использовать возможности, нужно явно вызвать их. В следующей главе мы создадим более продвинутого клиента с доступом к собственной большой языковой модели, LLM. А пока посмотрим, как вызвать функции сервера:

#### Rust

В функции main, после инициализации клиента, можно инициализировать сервер и показать часть его функций.

```rust
// Инициализация
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Список инструментов
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Вызов функций

Для вызова функций нужно указать правильные аргументы и в некоторых случаях имя функции, которую вызываем.

#### TypeScript

```typescript

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

// вызвать подсказку
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

В предыдущем коде мы:

- Считали ресурс, вызвав `readResource()` с указанием `uri`. На сервере это выглядит примерно так:

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

    Значение `uri` - `file://example.txt` соответствует `file://{name}` на сервере. `example.txt` будет сопоставлено с `name`.

- Вызвали инструмент, указав его `name` и `arguments` так:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Получили подсказку, вызвав `getPrompt()` с `name` и `arguments`. Код сервера:

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

    Следовательно, клиентский код выглядит так, чтобы соответствовать серверу:

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
# Прочитать ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Вызвать инструмент
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

В прошлом коде мы:

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

1. Для вывода результата — вот соответствующий код:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Вызов различных инструментов калькулятора
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

В предыдущем коде мы:

- Вызвали несколько калькуляторных инструментов через метод `callTool()` с объектами `CallToolRequest`.
- Каждый вызов указывает имя инструмента и карту аргументов, требуемых этим инструментом.
- Серверные инструменты ожидают определённые имена параметров (например, "a", "b" для математических операций).
- Результаты возвращаются в объектах `CallToolResult`, содержащих ответ сервера.

#### Rust

```rust
// Вызовите инструмент add с аргументами = {"a": 3, "b": 2}
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

Чтобы запустить клиента, выполните следующую команду в терминале:

#### TypeScript

Добавьте следующую запись в раздел "scripts" файла *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Вызовите клиента командой:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Сначала убедитесь, что MCP сервер запущен по адресу `http://localhost:8080`. Затем запустите клиента:

```bash
# Соберите ваш проект
./mvnw clean compile

# Запустите клиент
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Или запустите полный клиентский проект из папки решения `03-GettingStarted\02-client\solution\java`:

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

В этом задании вы примените полученные знания для создания собственного клиента.

Вот сервер, который вы можете использовать, вызывая его через ваш клиентский код. Попробуйте добавить больше функций на сервер, чтобы сделать его интереснее.

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

// Добавить инструмент сложения
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

// Начать получать сообщения через stdin и отправлять сообщения через stdout

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

# Создать сервер MCP
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

Также проверьте эту ссылку, чтобы узнать, как вызывать [подсказки и ресурсы](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предыдущем разделе](../../../../03-GettingStarted/01-first-server) вы научились создавать простой MCP сервер на Rust. Можете продолжить развитие этого проекта или посмотреть дополнительные примеры серверов MCP на Rust по ссылке: [Примеры MCP серверов](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

Папка **solution** содержит полные, готовые к запуску реализации клиентов, которые демонстрируют все концепции из этого руководства. Каждое решение включает и клиентский, и серверный код, организованные в отдельные, автономные проекты.

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

Каждое решение на конкретном языке содержит:

- **Полную реализацию клиента** со всеми функциями из урока
- **Рабочую структуру проекта** с правильными зависимостями и конфигурацией
- **Скрипты сборки и запуска** для простой настройки и запуска
- **Подробный README** с инструкциями по языку
- **Примеры обработки ошибок и результатов**

### 📖 Использование решений

1. **Перейдите в папку с предпочитаемым языком**:

   ```bash
   cd solution/typescript/    # Для TypeScript
   cd solution/java/          # Для Java
   cd solution/python/        # Для Python
   cd solution/dotnet/        # Для .NET
   ```

2. **Следуйте инструкциям в README каждой папки для:**
   - Установки зависимостей
   - Сборки проекта
   - Запуска клиента

3. **Пример выходных данных, который вы должны увидеть:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Для полной документации и пошаговых инструкций смотрите: **[📖 Документация решения](./solution/README.md)**

## 🎯 Полные примеры

Мы предоставили полноценные, работающие реализации клиентов для всех языков программирования, рассмотренных в этом руководстве. Эти примеры демонстрируют полный описанный выше функционал и могут использоваться как отправная точка для ваших проектов или в качестве эталонных реализаций.

### Доступные полные примеры

| Язык   | Файл                         | Описание                                                        |
|--------|------------------------------|-----------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | Полный клиент Java с транспортом SSE и комплексной обработкой ошибок |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | Полный клиент C# с транспортом stdio и автоматическим запуском сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Полный клиент TypeScript с полной поддержкой протокола MCP       |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)       | Полный клиент Python с использованием async/await паттернов      |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | Полный клиент Rust с использованием Tokio для асинхронных операций |

Каждый полный пример включает:
- ✅ **Установление соединения** и обработка ошибок  
- ✅ **Обнаружение сервера** (инструменты, ресурсы, подсказки, где применимо)  
- ✅ **Операции калькулятора** (сложение, вычитание, умножение, деление, помощь)  
- ✅ **Обработка результата** и форматированный вывод  
- ✅ **Полная обработка ошибок**  
- ✅ **Чистый, документированный код** с комментариями пошагово  

### Начало работы с полными примерами  

1. **Выберите предпочтительный язык** из таблицы выше  
2. **Изучите полный пример файла** для понимания полной реализации  
3. **Запустите пример** согласно инструкциям в [`complete_examples.md`](./complete_examples.md)  
4. **Изменяйте и расширяйте** пример под свои конкретные задачи  

Для подробной документации по запуску и настройке этих примеров смотрите: **[📖 Документация по полным примерам](./complete_examples.md)**  

### 💡 Решение vs. Полные примеры  

| **Папка с решением** | **Полные примеры**       |
|---------------------|-------------------------|
| Полная структура проекта с файлами сборки | Реализации в одном файле         |
| Готово к запуску с зависимостями           | Фокус на коде                    |
| Настройка, близкая к продакшену             | Образовательная справка          |
| Инструменты для конкретного языка           | Сравнение между языками          |  

Обе стратегии полезны — используйте **папку с решением** для готовых проектов, а **полные примеры** — для обучения и справки.  

## Основные выводы  

Основные выводы по этой главе по клиентам:  

- Могут использоваться как для обнаружения, так и для вызова функций сервера.  
- Могут запускать сервер при своем старте (как в этой главе), но также могут подключаться к уже запущенным серверам.  
- Отличный способ протестировать возможности сервера наряду с альтернативами, такими как Инспектор, как описано в предыдущей главе.  

## Дополнительные ресурсы  

- [Создание клиентов в MCP](https://modelcontextprotocol.io/quickstart/client)  

## Примеры  

- [Java Калькулятор](../samples/java/calculator/README.md)  
- [.Net Калькулятор](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Калькулятор](../samples/javascript/README.md)  
- [TypeScript Калькулятор](../samples/typescript/README.md)  
- [Python Калькулятор](../../../../03-GettingStarted/samples/python)  
- [Rust Калькулятор](../../../../03-GettingStarted/samples/rust)  

## Что дальше  

- Далее: [Создание клиента с LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для важной информации рекомендуется обращаться к профессиональному переводчику. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
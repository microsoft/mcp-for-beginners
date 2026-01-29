# Создание клиента

Клиенты — это пользовательские приложения или скрипты, которые напрямую взаимодействуют с MCP Server для запроса ресурсов, инструментов и подсказок. В отличие от использования инструмента инспектора, который предоставляет графический интерфейс для взаимодействия с сервером, написание собственного клиента позволяет осуществлять программное и автоматизированное взаимодействие. Это дает разработчикам возможность интегрировать возможности MCP в свои рабочие процессы, автоматизировать задачи и создавать индивидуальные решения, адаптированные к конкретным потребностям.

## Обзор

Этот урок вводит понятие клиентов в экосистеме Model Context Protocol (MCP). Вы узнаете, как написать собственного клиента и подключить его к MCP Server.

## Цели обучения

К концу этого урока вы сможете:

- Понять, что может делать клиент.
- Написать собственного клиента.
- Подключить и протестировать клиента с MCP Server, чтобы убедиться, что сервер работает должным образом.

## Что нужно для написания клиента?

Чтобы написать клиента, вам нужно выполнить следующие шаги:

- **Импортировать нужные библиотеки**. Вы будете использовать ту же библиотеку, что и раньше, но с другими конструкциями.
- **Создать экземпляр клиента**. Это включает создание экземпляра клиента и подключение его к выбранному методу транспорта.
- **Определить, какие ресурсы перечислить**. Ваш MCP Server предоставляет ресурсы, инструменты и подсказки, и вам нужно решить, какие из них перечислить.
- **Интегрировать клиента в хост-приложение**. После того как вы узнаете возможности сервера, вам нужно интегрировать их в ваше хост-приложение, чтобы пользователь мог вводить подсказки или другие команды, а соответствующая функция сервера была вызвана.

Теперь, когда мы понимаем на высоком уровне, что собираемся делать, давайте рассмотрим пример.

### Пример клиента

Давайте посмотрим на пример клиента:

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

В приведенном выше коде мы:

- Импортируем библиотеки.
- Создаем экземпляр клиента и подключаем его, используя stdio для транспорта.
- Перечисляем подсказки, ресурсы и инструменты и вызываем их все.

Вот так выглядит клиент, который может взаимодействовать с MCP Server.

Давайте уделим время следующему разделу упражнений и разберем каждый фрагмент кода, чтобы объяснить, что происходит.

## Упражнение: Написание клиента

Как было сказано выше, давайте уделим время объяснению кода, и, конечно, вы можете писать код вместе с нами, если хотите.

### -1- Импорт библиотек

Давайте импортируем нужные библиотеки. Нам понадобятся ссылки на клиента и на выбранный транспортный протокол, stdio. stdio — это протокол для вещей, предназначенных для работы на вашем локальном компьютере. SSE — это другой транспортный протокол, который мы покажем в будущих главах, но это ваш другой вариант. Пока что давайте продолжим с stdio.

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Для Java вы создадите клиента, который подключается к MCP Server из предыдущего упражнения. Используя ту же структуру проекта Java Spring Boot из [Начало работы с MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), создайте новый Java-класс под названием `SDKClient` в папке `src/main/java/com/microsoft/mcp/sample/client/` и добавьте следующие импорты:

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

Вам нужно будет добавить следующие зависимости в ваш файл `Cargo.toml`.

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

После этого вы можете импортировать необходимые библиотеки в код клиента.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Давайте перейдем к созданию экземпляра.

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

В приведенном выше коде мы:

- Создали экземпляр транспорта stdio. Обратите внимание, как он указывает команду и аргументы для того, чтобы найти и запустить сервер, так как это то, что нам нужно будет сделать при создании клиента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Создали экземпляр клиента, указав его имя и версию.

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

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

В приведенном выше коде мы:

- Импортировали нужные библиотеки.
- Создали объект параметров сервера, так как мы будем использовать его для запуска сервера, чтобы подключиться к нему с помощью клиента.
- Определили метод `run`, который, в свою очередь, вызывает `stdio_client`, чтобы начать сессию клиента.
- Создали точку входа, где мы предоставляем метод `run` для `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

В приведенном выше коде мы:

- Импортировали нужные библиотеки.
- Создали транспорт stdio и клиента `mcpClient`. Последний мы будем использовать для перечисления и вызова функций MCP Server.

Обратите внимание, что в "Arguments" вы можете указать либо *.csproj*, либо исполняемый файл.

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
        
        // Your client logic goes here
    }
}
```

В приведенном выше коде мы:

- Создали основной метод, который настраивает транспорт SSE, указывая на `http://localhost:8080`, где будет работать наш MCP Server.
- Создали класс клиента, который принимает транспорт как параметр конструктора.
- В методе `run` создали синхронного клиента MCP, используя транспорт, и инициализировали соединение.
- Использовали транспорт SSE (Server-Sent Events), который подходит для HTTP-общения с MCP Server на Java Spring Boot.

#### Rust

Этот клиент на Rust предполагает, что сервер является соседним проектом под названием "calculator-server" в той же директории. Код ниже запустит сервер и подключится к нему.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Перечисление функций сервера

Теперь у нас есть клиент, который может подключаться, если программа будет запущена. Однако он не перечисляет свои функции, поэтому давайте сделаем это следующим шагом:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Здесь мы перечисляем доступные ресурсы, `list_resources()` и инструменты, `list_tools`, и выводим их.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Выше приведен пример того, как мы можем перечислить инструменты на сервере. Для каждого инструмента мы затем выводим его имя.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

В приведенном выше коде мы:

- Вызвали `listTools()`, чтобы получить все доступные инструменты от MCP Server.
- Использовали `ping()`, чтобы проверить, работает ли соединение с сервером.
- `ListToolsResult` содержит информацию обо всех инструментах, включая их имена, описания и схемы ввода.

Отлично, теперь мы захватили все функции. Теперь вопрос: когда мы их используем? Этот клиент довольно простой, в том смысле, что нам нужно будет явно вызывать функции, когда мы их хотим. В следующей главе мы создадим более продвинутого клиента, который будет иметь доступ к собственной модели большого языка (LLM). Пока что давайте посмотрим, как мы можем вызвать функции на сервере:

#### Rust

В основной функции, после инициализации клиента, мы можем инициализировать сервер и перечислить некоторые из его функций.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Вызов функций

Чтобы вызвать функции, нам нужно убедиться, что мы указываем правильные аргументы, а в некоторых случаях имя того, что мы пытаемся вызвать.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

В приведенном выше коде мы:

- Читаем ресурс, вызывая `readResource()` с указанием `uri`. Вот как это, скорее всего, выглядит на стороне сервера:

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

    Наше значение `uri` `file://example.txt` соответствует `file://{name}` на сервере. `example.txt` будет сопоставлено с `name`.

- Вызываем инструмент, указывая его `name` и `arguments`, например:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Получаем подсказку, вызывая `getPrompt()` с `name` и `arguments`. Код сервера выглядит следующим образом:

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

    и ваш клиентский код, соответственно, выглядит следующим образом, чтобы соответствовать тому, что объявлено на сервере:

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

В приведенном выше коде мы:

- Вызвали ресурс под названием `greeting`, используя `read_resource`.
- Вызвали инструмент под названием `add`, используя `call_tool`.

#### .NET

1. Добавим код для вызова инструмента:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Чтобы вывести результат, вот код для обработки:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

В приведенном выше коде мы:

- Вызвали несколько инструментов калькулятора, используя метод `callTool()` с объектами `CallToolRequest`.
- Каждый вызов инструмента указывает имя инструмента и `Map` аргументов, необходимых для этого инструмента.
- Инструменты сервера ожидают определенные имена параметров (например, "a", "b" для математических операций).
- Результаты возвращаются как объекты `CallToolResult`, содержащие ответ от сервера.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

Добавьте следующую запись в раздел "scripts" в *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Вызовите клиента с помощью следующей команды:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Сначала убедитесь, что ваш MCP Server работает на `http://localhost:8080`. Затем запустите клиента:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Или вы можете запустить полный проект клиента, предоставленный в папке решения `03-GettingStarted\02-client\solution\java`:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Задание

В этом задании вы будете использовать полученные знания для создания собственного клиента.

Вот сервер, который вы можете использовать и который вам нужно вызвать через ваш клиентский код. Попробуйте добавить больше функций на сервер, чтобы сделать его более интересным.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

Посмотрите этот проект, чтобы узнать, как [добавить подсказки и ресурсы](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Также ознакомьтесь с этой ссылкой, чтобы узнать, как вызывать [подсказки и ресурсы](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предыдущем разделе](../../../../03-GettingStarted/01-first-server) вы узнали, как создать простой MCP Server на Rust. Вы можете продолжить работу над этим или ознакомиться с этой ссылкой для получения дополнительных примеров MCP Server на Rust: [Примеры MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

**Папка решения** содержит полные, готовые к запуску реализации клиента, демонстрирующие все концепции, рассмотренные в этом уроке. Каждое решение включает как клиентский, так и серверный код, организованный в отдельные, автономные проекты.

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

Каждое решение для конкретного языка предоставляет:

- **Полную реализацию клиента** со всеми функциями из урока.
- **Рабочую структуру проекта** с правильными зависимостями и конфигурацией.
- **Скрипты сборки и запуска** для легкой настройки и выполнения.
- **Подробный README** с инструкциями для конкретного языка.
- **Примеры обработки ошибок** и обработки результатов.

### 📖 Использование решений

1. **Перейдите в папку с вашим предпочтительным языком**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Следуйте инструкциям README** в каждой папке для:
   - Установки зависимостей.
   - Сборки проекта.
   - Запуска клиента.

3. **Пример вывода**, который вы должны увидеть:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Для полной документации и пошаговых инструкций смотрите: **[📖 Документация решения](./solution/README.md)**

## 🎯 Полные примеры

Мы предоставили полные, рабочие реализации клиента для всех языков программирования, рассмотренных в этом уроке. Эти примеры демонстрируют полную функциональность, описанную выше, и могут быть использованы как эталонные реализации или отправные точки для ваших собственных проектов.

### Доступные полные примеры

| Язык       | Файл                          | Описание                                                                 |
|------------|-------------------------------|--------------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Полный клиент на Java с использованием транспорта SSE и обработкой ошибок |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Полный клиент на C# с использованием транспорта stdio и автоматическим запуском сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Полный клиент на TypeScript с полной поддержкой MCP протокола            |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Полный клиент на Python с использованием async/await                     |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Полный клиент на Rust с использованием Tokio для асинхронных операций    |
Каждый пример включает:

- ✅ **Установление соединения** и обработку ошибок
- ✅ **Обнаружение сервера** (инструменты, ресурсы, подсказки, где применимо)
- ✅ **Операции калькулятора** (сложение, вычитание, умножение, деление, помощь)
- ✅ **Обработка результатов** и форматированный вывод
- ✅ **Полная обработка ошибок**
- ✅ **Чистый, документированный код** с пошаговыми комментариями

### Начало работы с полными примерами

1. **Выберите предпочитаемый язык** из таблицы выше
2. **Изучите файл с полным примером**, чтобы понять реализацию
3. **Запустите пример**, следуя инструкциям в [`complete_examples.md`](./complete_examples.md)
4. **Модифицируйте и расширяйте** пример для вашего конкретного случая

Для подробной документации о запуске и настройке этих примеров см. **[📖 Документация по полным примерам](./complete_examples.md)**

### 💡 Решение vs. Полные примеры

| **Папка с решением** | **Полные примеры** |
|--------------------|--------------------- |
| Полная структура проекта с файлами сборки | Реализации в одном файле |
| Готово к запуску с зависимостями | Сфокусированные примеры кода |
| Настройка, приближенная к продакшену | Образовательная справка |
| Инструменты, специфичные для языка | Сравнение между языками |

Оба подхода полезны — используйте **папку с решением** для полноценных проектов и **полные примеры** для обучения и справки.

## Основные выводы

Основные выводы этой главы о клиентах:

- Могут использоваться как для обнаружения, так и для вызова функций на сервере.
- Могут запускать сервер одновременно с собственным запуском (как в этой главе), но также могут подключаться к уже работающим серверам.
- Отличный способ протестировать возможности сервера наряду с альтернативами, такими как Инспектор, описанный в предыдущей главе.

## Дополнительные ресурсы

- [Создание клиентов в MCP](https://modelcontextprotocol.io/quickstart/client)

## Примеры

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .Net](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Что дальше

- Далее: [Создание клиента с использованием LLM](../03-llm-client/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.
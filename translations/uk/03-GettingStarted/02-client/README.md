# Створення клієнта

Клієнти — це користувацькі додатки або скрипти, які безпосередньо взаємодіють із сервером MCP для запиту ресурсів, інструментів і підказок. На відміну від використання інструменту інспектора, який надає графічний інтерфейс для взаємодії із сервером, написання власного клієнта дозволяє програмно та автоматизовано спілкуватися. Це дає змогу розробникам інтегрувати можливості MCP у власні робочі процеси, автоматизувати завдання та створювати користувацькі рішення, пристосовані до конкретних потреб.

## Огляд

У цьому уроці ми познайомимося з концепцією клієнтів в екосистемі Model Context Protocol (MCP). Ви навчитеся писати власного клієнта й підключати його до сервера MCP.

## Цілі навчання

До кінця цього уроку ви зможете:

- Зрозуміти, що може робити клієнт.
- Написати власного клієнта.
- Підключити та протестувати клієнта з сервером MCP, щоб переконатися, що все працює належним чином.

## Що потрібно для написання клієнта?

Для написання клієнта потрібно:

- **Імпортувати потрібні бібліотеки**. Ви використовуватимете ту саму бібліотеку, що й раніше, тільки інші конструкції.
- **Створити екземпляр клієнта**. Це включає створення клієнта та підключення його до обраного транспортного протоколу.
- **Визначитися, які ресурси перелічувати**. Ваш сервер MCP має ресурси, інструменти та підказки, потрібно вибрати, які саме показувати.
- **Інтегрувати клієнта в хост-додаток**. Коли ви знаєте можливості сервера, потрібно інтегрувати це у ваш хост-додаток, щоб при введенні користувачем підказки або іншої команди відповідна функція сервера викликалася.

Тепер, коли ми розуміємо загально, що треба зробити, перейдемо до прикладу.

### Приклад клієнта

Розглянемо цей приклад клієнта:

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

// Список підказок
const prompts = await client.listPrompts();

// Отримати підказку
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Список ресурсів
const resources = await client.listResources();

// Прочитати ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Викликати інструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

У наведеному коді ми:

- Імпортували бібліотеки
- Створили екземпляр клієнта та підключили його через stdio для транспорту.
- Перелічили підказки, ресурси та інструменти та викликали їх усі.

Ось і все, клієнт, який може спілкуватися з сервером MCP.

У наступному розділі вправ присвятимо час розбору кожного фрагмента коду й поясненню, що відбувається.

## Вправа: Написання клієнта

Як було сказано вище, приділимо час поясненню коду, і, за бажанням, пишіть код разом із нами.

### -1- Імпорт бібліотек

Імпортуємо потрібні бібліотеки — нам потрібні посилання на клієнта та обраний транспортний протокол stdio. stdio — це протокол для речей, що запускаються на локальній машині. SSE — це інший транспортний протокол, який ми покажемо в наступних розділах, але зараз продовжимо використовувати stdio.

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

Для Java створіть клієнта, який підключається до сервера MCP з попередньої вправи. Використовуючи ту саму структуру проекту Java Spring Boot із [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), створіть новий клас Java під назвою `SDKClient` у папці `src/main/java/com/microsoft/mcp/sample/client/` і додайте такі імпорти:

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

Вам потрібно додати такі залежності у файл `Cargo.toml`.

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

Звідти ви зможете імпортувати потрібні бібліотеки в коді клієнта.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Переходимо до створення екземплярів.

### -2- Створення клієнта та транспорту

Потрібно створити екземпляр транспорту та клієнта:

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

У наведеному коді ми:

- Створили екземпляр транспорту stdio. Зверніть увагу, що він вказує команду та аргументи для запуску сервера, що нам треба робити для створення клієнта.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Створили екземпляр клієнта, вказавши ім'я та версію.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Під'єднали клієнта до обраного транспорту.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для stdio з'єднання
server_params = StdioServerParameters(
    command="mcp",  # Виконуваний файл
    args=["run", "server.py"],  # Опціональні аргументи командного рядка
    env=None,  # Опціональні змінні оточення
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

- Імпортували потрібні бібліотеки
- Створили об'єкт параметрів сервера, щоб запустити сервер і підключитися до нього клієнтом.
- Визначили метод `run`, який викликає `stdio_client` для запуску сесії клієнта.
- Створили точку входу, де виконується `asyncio.run` з методoм `run`.

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

У наведеному коді ми:

- Імпортували потрібні бібліотеки.
- Створили stdio транспорт та клієнта `mcpClient`. Останній ми використовуватимемо для переліку та виклику функцій на сервері MCP.

Зверніть увагу, у "Arguments" можна вказати або *.csproj* файл, або виконуваний файл.

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
        
        // Ваша логіка клієнта розміщується тут
    }
}
```

У наведеному коді ми:

- Створили метод main, який налаштовує транспорт SSE, що вказує на `http://localhost:8080`, де працюватиме сервер MCP.
- Створили клас клієнта, що приймає транспорт у конструкторі.
- У методі `run` створили синхронний клієнт MCP за допомогою транспорту і ініціалізували з’єднання.
- Використали транспорт SSE (Server-Sent Events), який підходить для HTTP-комунікації з MCP сервером Java Spring Boot.

#### Rust

Зверніть увагу, що клієнт Rust припускає, що сервер — це сусідній проект з назвою "calculator-server" у тій же директорії. Код нижче запускає сервер і підключається до нього.

```rust
async fn main() -> Result<(), RmcpError> {
    // Припустимо, сервер - це проект-брат з ім'ям "calculator-server" у тій же директорії
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

    // TODO: Ініціалізувати

    // TODO: Перерахувати інструменти

    // TODO: Викликати додавання інструменту з аргументами = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Перелік функцій сервера

Тепер у нас є клієнт, який може підключитися, якщо програму запустити. Однак він не перелічує функції, отже зробимо це:

#### TypeScript

```typescript
// Список підказок
const prompts = await client.listPrompts();

// Список ресурсів
const resources = await client.listResources();

// список інструментів
const tools = await client.listTools();
```

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
```

Тут ми перелічуємо доступні ресурси викликом `list_resources()` та інструменти — `list_tools` і виводимо їх.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Вище приклад, як перелічувати інструменти на сервері. Для кожного інструмента ми виводимо його ім'я.

#### Java

```java
// Перелік і демонстрація інструментів
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Ви також можете пропінгувати сервер, щоб перевірити підключення
client.ping();
```

У наведеному коді ми:

- Викликали `listTools()` для отримання всіх доступних інструментів з MCP сервера.
- Використали `ping()` для перевірки з'єднання з сервером.
- `ListToolsResult` містить інформацію про всі інструменти, включно з їхніми іменами, описами та схемами вводу.

Чудово, тепер ми отримали всі функції. А тепер питання — коли їх використовувати? Цей клієнт досить простий: функції треба викликати явно, коли вони потрібні. Наступного розділу ми створимо більш просунутого клієнта з власною великою моделлю мови (LLM). А поки що подивимося, як викликати функції сервера:

#### Rust

У головній функції після ініціалізації клієнта можна ініціалізувати сервер і перерахувати деякі його функції.

```rust
// Ініціалізувати
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Перелічити інструменти
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Виклик функцій

Щоб викликати функції, потрібно вказати правильні аргументи і в деяких випадках ім’я того, що ми хочемо викликати.

#### TypeScript

```typescript

// Прочитати ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Викликати інструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// виклик підказки
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

У наведеному коді ми:

- Читаємо ресурс, викликаючи `readResource()`, вказуючи `uri`. Ось як це, ймовірно, виглядає на сервері:

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

    Значення `uri` — `file://example.txt` співпадає з `file://{name}` на сервері. `example.txt` буде співставлено з `name`.

- Викликаємо інструмент, вказуючи його `name` та `arguments` таким чином:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Отримуємо підказку (prompt), викликаючи `getPrompt()` з `name` та `arguments`. Серверний код виглядає так:

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

    Тому код клієнта виглядає так, щоб відповідати серверному опису:

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
# Прочитати ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Викликати інструмент
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

У наведеному коді ми:

- Викликали ресурс із ім'ям `greeting` за допомогою `read_resource`.
- Викликали інструмент `add` за допомогою `call_tool`.

#### .NET

1. Додаємо код для виклику інструмента:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Для виведення результату ось код для обробки:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Виклик різних інструментів калькулятора
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

У наведеному коді ми:

- Викликали кілька інструментів калькулятора за методом `callTool()`, передаючи `CallToolRequest` об’єкти.
- Кожен виклик інструмента вказує ім’я інструмента та `Map` аргументів, які потрібні цьому інструменту.
- Серверні інструменти очікують конкретні імена параметрів (наприклад, "a" і "b" для математичних операцій).
- Результати повертаються як об'єкти `CallToolResult`, що містять відповідь від сервера.

#### Rust

```rust
// Викликати інструмент add з аргументами = {"a": 3, "b": 2}
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

### -5- Запуск клієнта

Щоб запустити клієнта, введіть у терміналі таку команду:

#### TypeScript

Додайте наступний рядок у розділ "scripts" вашого *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Викличте клієнта такою командою:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Спершу переконайтесь, що ваш сервер MCP запущений на `http://localhost:8080`. Потім запустіть клієнта:

```bash
# Зберіть ваш проєкт
./mvnw clean compile

# Запустіть клієнта
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Альтернативно, ви можете запустити повний проект клієнта з папки `03-GettingStarted\02-client\solution\java`:

```bash
# Перейдіть до каталогу рішення
cd 03-GettingStarted/02-client/solution/java

# Зберіть і запустіть JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Завдання

У цьому завданні ви використаєте набуті навички створення клієнта, щоби написати власного клієнта.

Ось сервер, який ви можете використовувати, викликаючи його через ваш код клієнта. Подивіться, чи зможете додати більше функцій, щоб зробити сервер цікавішим.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Створити MCP сервер
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Додати інструмент додавання
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Додати динамічний ресурс вітання
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

// Почати отримувати повідомлення на stdin і надсилати повідомлення на stdout

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

# Створити MCP сервер
mcp = FastMCP("Demo")


# Додати інструмент додавання
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Додати динамічний ресурс привітання
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

Подивіться цей проект, щоб дізнатися, як [додавати підказки та ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Також перевірте це посилання, щоб дізнатися, як викликати [підказки та ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

У [попередньому розділі](../../../../03-GettingStarted/01-first-server) ви навчились створювати простий MCP сервер на Rust. Можете продовжити розбудову цього або подивитися інші приклади MCP серверів на Rust за посиланням: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Розв'язок

Папка **solution** містить повні, готові до запуску реалізації клієнтів, які демонструють усі концепції, розглянуті у цьому посібнику. Кожен розв’язок включає код як клієнта, так і сервера, організований у окремі, автономні проєкти.

### 📁 Структура розв’язку

Каталог розв’язку організований за мовами програмування:

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

### 🚀 Що містить кожен розв’язок

Кожний варіант розв’язку для конкретної мови надає:

- **Повна реалізація клієнта** зі всіма функціями, розглянутими в посібнику
- **Працездатна структура проекту** з належними залежностями та конфігурацією
- **Скрипти складання та запуску** для зручної установки і виконання
- **Докладний README** з інструкціями для конкретної мови
- **Приклади обробки помилок** та обробки результатів

### 📖 Використання розв’язків

1. **Перейдіть у папку бажаної мови програмування**:

   ```bash
   cd solution/typescript/    # Для TypeScript
   cd solution/java/          # Для Java
   cd solution/python/        # Для Python
   cd solution/dotnet/        # Для .NET
   ```

2. **Дотримуйтесь інструкцій у README** кожної папки для:
   - Встановлення залежностей
   - Складання проекту
   - Запуску клієнта

3. **Приклад виводу**, який ви маєте побачити:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Для повної документації та покрокових інструкцій дивіться: **[📖 Документація розв’язку](./solution/README.md)**

## 🎯 Повні приклади

Ми надали повні, працездатні реалізації клієнтів для всіх мов програмування, охоплених у цьому посібнику. Ці приклади демонструють повну функціональність, описану вище, і можуть слугувати як референсні реалізації або початкові точки для ваших власних проектів.

### Доступні повні приклади

| Мова | Файл | Опис |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Повний клієнт Java з транспортом SSE і всебічною обробкою помилок |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Повний клієнт C# з транспортом stdio та автоматичним запуском сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Повний клієнт TypeScript з повною підтримкою протоколу MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Повний клієнт Python з використанням async/await патернів |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Повний клієнт Rust на базі Tokio для асинхронних операцій |

Кожен повний приклад містить:

- ✅ **Встановлення з’єднання** та обробку помилок
- ✅ **Виявлення сервера** (інструменти, ресурси, підказки, де це застосовно)
- ✅ **Операції калькулятора** (додавання, віднімання, множення, ділення, допомога)
- ✅ **Обробку результатів** та форматований вивід
- ✅ **Всебічну обробку помилок**

- ✅ **Чистий, документований код** з покроковими коментарями

### Початок роботи з повними прикладами

1. **Обрати улюблену мову** із наведеної вище таблиці
2. **Переглянути файл з повним прикладом**, щоб зрозуміти повну реалізацію
3. **Запустити приклад** за інструкціями у [`complete_examples.md`](./complete_examples.md)
4. **Змінити та розширити** приклад для вашого конкретного випадку

Для детальної документації щодо запуску та налаштування цих прикладів дивіться: **[📖 Документація повних прикладів](./complete_examples.md)**

### 💡 Рішення проти повних прикладів

| **Папка з рішенням** | **Повні приклади** |
|--------------------|--------------------- |
| Повна структура проєкту з файлами збірки | Реалізації в одному файлі |
| Готові до запуску з залежностями | Сфокусовані приклади коду |
| Схоже на продуктивний налаштування | Освітня довідка |
| Мовно-специфічні інструменти | Порівняння між мовами |

Обидва підходи є цінними — використовуйте **папку з рішенням** для повних проєктів і **повні приклади** для навчання та довідки.

## Ключові висновки

Ключові висновки цієї глави про клієнтів такі:

- Можуть використовуватися як для виявлення, так і для виклику функцій на сервері.
- Може запускати сервер під час власного запуску (як у цій главі), але клієнти також можуть під’єднуватись до вже запущених серверів.
- Це чудовий спосіб перевірити можливості сервера поруч з альтернативами, як Інспектор, про який йшлося у попередній главі.

## Додаткові ресурси

- [Створення клієнтів у MCP](https://modelcontextprotocol.io/quickstart/client)

## Приклади

- [Калькулятор на Java](../samples/java/calculator/README.md)
- [Калькулятор на .NET](../../../../03-GettingStarted/samples/csharp)
- [Калькулятор на JavaScript](../samples/javascript/README.md)
- [Калькулятор на TypeScript](../samples/typescript/README.md)
- [Калькулятор на Python](../../../../03-GettingStarted/samples/python)
- [Калькулятор на Rust](../../../../03-GettingStarted/samples/rust)

## Що далі

- Далі: [Створення клієнта з LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Створення клієнта

Клієнти — це індивідуальні додатки або скрипти, які безпосередньо спілкуються з MCP Server для запиту ресурсів, інструментів та підказок. На відміну від використання інструмента інспектора, який забезпечує графічний інтерфейс для взаємодії з сервером, написання власного клієнта дозволяє програмно та автоматично взаємодіяти. Це дає змогу розробникам інтегрувати можливості MCP у свої робочі процеси, автоматизувати завдання та створювати індивідуальні рішення, адаптовані до конкретних потреб.

## Огляд

Цей урок знайомить із поняттям клієнтів у екосистемі Model Context Protocol (MCP). Ви навчитеся писати власного клієнта та підключати його до MCP Server.

## Навчальні цілі

Наприкінці цього уроку ви зможете:

- Розуміти, що може робити клієнт.
- Написати власного клієнта.
- Підключити та протестувати клієнта із MCP сервером, щоб упевнитися, що сервер працює належним чином.

## Що входить у написання клієнта?

Для написання клієнта вам потрібно:

- **Імпортувати правильні бібліотеки**. Ви використовуватимете ту ж бібліотеку, що і раніше, але з іншими конструкціями.
- **Створити екземпляр клієнта**. Це означає створити екземпляр клієнта та підключити його до обраного транспортного методу.
- **Визначити, які ресурси перелічувати**. Ваш MCP сервер має ресурси, інструменти та підказки, вам потрібно вирішити, які перераховувати.
- **Інтегрувати клієнта з хост-додатком**. Коли ви знаєте можливості сервера, потрібно інтегрувати клієнта у ваш хост-додаток, щоб при введенні користувачем підказки або іншої команди викликалася відповідна функція сервера.

Тепер, коли ми розуміємо в загальних рисах, що плануємо зробити, розглянемо приклад.

### Приклад клієнта

Ознайомимося з прикладом клієнта:

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

У наведеному вище коді ми:

- Імпортували бібліотеки
- Створили екземпляр клієнта і підключили його використовуючи stdio як транспорт.
- Перелічили підказки, ресурси та інструменти і викликали їх усі.

Отже, у вас є клієнт, який може спілкуватися з MCP Server.

Приділимо достатньо часу у наступному розділі вправ, щоб розібрати кожен фрагмент коду і пояснити, що відбувається.

## Вправа: Написання клієнта

Як уже говорилося, давайте детально пояснимо код, та, зрозуміло, ви можете писати код разом з нами.

### -1- Імпортування бібліотек

Імпортуємо потрібні бібліотеки, нам потрібні посилання на клієнта та обраний транспортний протокол stdio. stdio — це протокол для речей, які запускаються на локальній машині. SSE — це інший транспортний протокол, який ми покажемо у майбутніх розділах, це ваш інший варіант. Наразі ж продовжуємо з stdio.

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

Для Java створіть клієнта, який підключатиметься до MCP серверу з попередньої вправи. Використовуючи ту саму структуру проекту Java Spring Boot з [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), створіть новий клас Java з назвою `SDKClient` у папці `src/main/java/com/microsoft/mcp/sample/client/` та додайте наступні імпорти:

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

Вам потрібно буде додати такі залежності у ваш файл `Cargo.toml`.

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

Після цього ви можете імпортувати необхідні бібліотеки у коді клієнта.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Перейдемо до створення екземплярів.

### -2- Створення екземплярів клієнта та транспорту

Нам потрібно створити екземпляр транспорту та екземпляр клієнта:

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

У наведеному вище коді ми:

- Створили екземпляр транспорту stdio. Зверніть увагу, як вказано команду та аргументи для пошуку та запуску сервера, оскільки це те, що нам потрібно робити при створенні клієнта.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Ініціалізували клієнта, вказавши йому ім'я та версію.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Підключили клієнта до обраного транспорту.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Створити параметри сервера для stdio-підключення
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
            # Ініціалізувати підключення
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

У наведеному вище коді ми:

- Імпортували потрібні бібліотеки.
- Ініціалізували об'єкт параметрів сервера, який використаємо для запуску сервера, щоб приєднатися до нього клієнтом.
- Визначили метод `run`, який викликає `stdio_client` для запуску сесії клієнта.
- Створили точку входу, де передали метод `run` в `asyncio.run`.

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

У наведеному вище коді ми:

- Імпортували потрібні бібліотеки.
- Створили транспорт stdio та клієнта `mcpClient`. Останній використовується для переліку та виклику функцій MCP Server.

Зверніть увагу, що в "Arguments" ви можете вказати або *.csproj*, або виконуваний файл.

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

- Створили метод main, який налаштовує транспорт SSE, що підключається до `http://localhost:8080`, де буде працювати MCP сервер.
- Створили клас клієнта, який приймає транспорт у конструктор.
- У методі `run` створили синхронного MCP клієнта за допомогою транспорту і ініціалізували підключення.
- Використали SSE (Server-Sent Events) транспорт, який підходить для HTTP-комунікації з MCP серверами на Java Spring Boot.

#### Rust

Зауважте, що цей Rust клієнт припускає, що сервер — це проект-сусід з назвою "calculator-server" у тій самій директорії. Нижченаведений код запускає сервер та підключається до нього.

```rust
async fn main() -> Result<(), RmcpError> {
    // Припустимо, що сервер є проектом-братом з назвою "calculator-server" у тій же директорії
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

    // TODO: Перелік інструментів

    // TODO: Викликати інструмент додавання з аргументами = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Перелік особливостей сервера

Тепер у нас є клієнт, який може підключитися, якщо запустити програму. Однак він фактично не перераховує особливості сервера, давайте зробимо це:

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
```

Тут ми перераховуємо доступні ресурси (`list_resources()`) та інструменти (`list_tools`) і виводимо їх.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Наверху показано приклад, як можна отримати список інструментів сервера. Для кожного інструмента ми виводимо його ім'я.

#### Java

```java
// Перелік та демонстрація інструментів
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Ви також можете виконати ping сервера для перевірки з'єднання
client.ping();
```

У наведеному коді ми:

- Викликали `listTools()` для отримання всіх доступних інструментів MCP сервера.
- Використали `ping()` для перевірки з'єднання з сервером.
- `ListToolsResult` містить інформацію про всі інструменти, включаючи їхні імена, описи та схеми вхідних даних.

Чудово, тепер ми отримали всі функції. А коли ми їх використовуємо? Цей клієнт досить простий, у тому сенсі, що ми маємо явно викликати функції, коли вони потрібні. У наступній главі ми створимо більш просунутого клієнта, який матиме власну велику мовну модель, LLM. Наразі ж подивимось, як можна викликати функції сервера:

#### Rust

У функції main, після ініціалізації клієнта, можна ініціалізувати сервер і перерахувати деякі його функції.

```rust
// Ініціалізувати
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Перелічити інструменти
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Виклик функцій

Щоб викликати функції, потрібно правильно вказати аргументи і в деяких випадках ім’я того, що ми хочемо викликати.

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

// викликати запит
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

У наведеному коді ми:

- Читаємо ресурс — викликаємо `readResource()`, вказуючи `uri`. Ось як це, ймовірно, виглядає на сервері:

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

    Значення `uri` — `file://example.txt` відповідає `file://{name}` на сервері. `example.txt` буде відображено як `name`.

- Викликаємо інструмент, вказуючи його `name` і `arguments` так:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Отримуємо підказку — викликаємо `getPrompt()` з `name` та `arguments`. Код сервера виглядає так:

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

    Отже, відповідний код клієнта матиме такий вигляд, щоб відповідати серверній декларації:

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

- Викликали ресурс з ім’ям `greeting` через `read_resource`.
- Викликали інструмент з назвою `add` через `call_tool`.

#### .NET

1. Додамо код для виклику інструмента:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. Код для виводу результату:

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

- Викликали кілька калькуляторних інструментів за допомогою методу `callTool()` з об’єктами `CallToolRequest`.
- Кожен виклик інструмента вказує ім’я інструмента та `Map` аргументів, потрібних для цього інструмента.
- Серверні інструменти очікують конкретні імена параметрів (наприклад, "a", "b" для математичних операцій).
- Результати повертаються як об’єкти `CallToolResult`, що містять відповіді від сервера.

#### Rust

```rust
// Викликати інструмент додавання з аргументами = {"a": 3, "b": 2}
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

Додайте до розділу "scripts" у *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Викликайте клієнта такою командою:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Спершу упевніться, що MCP сервер запущено на `http://localhost:8080`. Потім запустіть клієнта:

```bash
# Зберіть ваш проєкт
./mvnw clean compile

# Запустіть клієнт
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Або ж можна запустити повний проект клієнта з папки рішення `03-GettingStarted\02-client\solution\java`:

```bash
# Перейдіть до каталогу рішення
cd 03-GettingStarted/02-client/solution/java

# Збудуйте та запустіть JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Завдання

У цьому завданні ви застосуєте отримані знання, щоб створити свого власного клієнта.

Ось сервер, який ви можете використовувати та викликати через ваш клієнтський код, спробуйте додати більше функцій у сервер, щоб зробити його цікавішим.

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

// Додати динамічний ресурс привітання
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

// Почати отримувати повідомлення через stdin та надсилати повідомлення через stdout

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

Перегляньте цей проект, щоб дізнатися, як можна [додавати підказки та ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Також перевірте це посилання для прикладів виклику [підказок та ресурсів](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

У [попередньому розділі](../../../../03-GettingStarted/01-first-server) ви навчились створювати простий MCP сервер на Rust. Ви можете продовжити розробку на його основі або ознайомитись із цим посиланням для інших прикладів MCP серверів на Rust: [Приклади MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Рішення

**Папка рішення** містить повні, готові до запуску реалізації клієнтів, які демонструють усі концепції, розглянуті у цьому посібнику. Кожне рішення включає код клієнта та сервера, організований у окремих, самостійних проектах.

### 📁 Структура рішення

Директорія рішення організована за мовами програмування:

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

### 🚀 Що містить кожне рішення

Кожне мовне рішення надає:

- **Повну реалізацію клієнта** з усіма функціями з цього посібника
- **Функціональну структуру проекту** з відповідними залежностями та конфігурацією
- **Сценарії збірки та запуску** для легкого налаштування та виконання
- **Детальний README** з мовно-специфічними інструкціями
- **Обробку помилок** та приклади обробки результатів

### 📖 Використання рішень

1. **Перейдіть у папку з бажаною мовою програмування**:

   ```bash
   cd solution/typescript/    # Для TypeScript
   cd solution/java/          # Для Java
   cd solution/python/        # Для Python
   cd solution/dotnet/        # Для .NET
   ```

2. **Дотримуйтесь інструкцій у README кожної папки щодо:**
   - Встановлення залежностей
   - Зборки проекту
   - Запуску клієнта

3. **Приклад виводу, який ви маєте побачити:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Для повної документації та покрокових інструкцій дивіться: **[📖 Документація рішення](./solution/README.md)**

## 🎯 Повні приклади

Ми надали повні, робочі реалізації клієнтів для всіх мов програмування, розглянутих у цьому посібнику. Ці приклади демонструють повну функціональність, описану вище, і можуть використовуватися як референсні реалізації або відправна точка для ваших власних проектів.

### Доступні повні приклади

| Мова     | Файл                              | Опис                                                   |
|----------|----------------------------------|--------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)          | Повний Java клієнт з SSE транспортом та комплексною обробкою помилок |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)          | Повний C# клієнт з stdio транспортом та автоматичним запуском сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Повний TypeScript клієнт з повною підтримкою протоколу MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)          | Повний Python клієнт, що використовує асинхронні патерни async/await |
| **Rust**  | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)              | Повний Rust клієнт з використанням Tokio для асинхронних операцій |

Кожен повний приклад включає:
- ✅ **Встановлення з’єднання** та обробка помилок
- ✅ **Виявлення сервера** (інструменти, ресурси, підказки там, де це застосовно)
- ✅ **Операції калькулятора** (додавання, віднімання, множення, ділення, допомога)
- ✅ **Обробка результатів** та форматований вивід
- ✅ **Всеосяжна обробка помилок**
- ✅ **Чистий, документований код** з покроковими коментарями

### Початок роботи з повними прикладами

1. **Обрати вашу улюблену мову** з таблиці вище
2. **Переглянути файл з повним прикладом**, щоб зрозуміти повну реалізацію
3. **Запустити приклад** за інструкціями у [`complete_examples.md`](./complete_examples.md)
4. **Змінити та розширити** приклад для вашого конкретного випадку використання

Для детальної документації про запуск та налаштування цих прикладів дивіться: **[📖 Документація повних прикладів](./complete_examples.md)**

### 💡 Рішення vs Повні приклади

| **Папка з рішенням** | **Повні приклади** |
|--------------------|--------------------- |
| Повна структура проекту з файлами збірки | Імплементації в одному файлі |
| Готове до запуску з залежностями | Орієнтовані на код приклади |
| Налаштування, подібне до продуктивного середовища | Освітня довідка |
| Інструменти, специфічні для мови | Порівняння між мовами |

Обидва підходи цінні — використовуйте **папку з рішенням** для повних проектів і **повні приклади** для навчання та довідок.

## Основні висновки

Основні висновки цієї глави про клієнтів:

- Можна використовувати як для виявлення, так і для виклику функцій на сервері.
- Можуть запускати сервер, поки він сам запускається (як у цій главі), але клієнти також можуть підключатися до вже запущених серверів.
- Це чудовий спосіб протестувати можливості сервера поряд із альтернативами, як Інспектор, як описано в попередній главі.

## Додаткові ресурси

- [Створення клієнтів у MCP](https://modelcontextprotocol.io/quickstart/client)

## Приклади

- [Java калькулятор](../samples/java/calculator/README.md)
- [.Net калькулятор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калькулятор](../samples/javascript/README.md)
- [TypeScript калькулятор](../samples/typescript/README.md)
- [Python калькулятор](../../../../03-GettingStarted/samples/python)
- [Rust калькулятор](../../../../03-GettingStarted/samples/rust)

## Що далі

- Далі: [Створення клієнта з LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ був перекладений за допомогою автоматичного перекладача [Co-op Translator](https://github.com/Azure/co-op-translator). Незважаючи на наші зусилля забезпечити точність, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ його рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
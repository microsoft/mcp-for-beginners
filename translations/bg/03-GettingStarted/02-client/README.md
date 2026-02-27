# Създаване на клиент

Клиентите са персонализирани приложения или скриптове, които комуникират директно с MCP сървър за заявка на ресурси, инструменти и подкани. За разлика от използването на инспекторния инструмент, който осигурява графичен интерфейс за взаимодействие със сървъра, написването на собствен клиент позволява програмни и автоматизирани взаимодействия. Това дава възможност на разработчиците да интегрират възможностите на MCP в собствените си работни потоци, да автоматизират задачи и да изграждат персонализирани решения, пригодени за специфични нужди.

## Преглед

Този урок въвежда концепцията за клиенти в екосистемата на Model Context Protocol (MCP). Ще научите как да напишете собствен клиент и да го свържете към MCP сървър.

## Учебни цели

До края на този урок ще можете да:

- Разберете какво може да прави един клиент.
- Напишете собствен клиент.
- Свържете и тествате клиента с MCP сървър, за да се уверите, че сървърът работи както се очаква.

## Какво включва написването на клиент?

За да напишете клиент, трябва да направите следното:

- **Импортирайте правилните библиотеки**. Ще използвате същата библиотека като преди, но с различни конструкции.
- **Инициализирайте клиент**. Това ще включва създаване на клиентски екземпляр и свързването му с избрания транспортен метод.
- **Решете кои ресурси да изброите**. Вашият MCP сървър предоставя ресурси, инструменти и подкани, трябва да решите кои от тях да изброите.
- **Интегрирайте клиента в хост приложението**. След като знаете възможностите на сървъра, трябва да интегрирате това във вашето хост приложение, така че ако потребител въведе подкана или друга команда, съответната сървърна функция да бъде извикана.

Сега, когато накратко разбрахме какво предстои, нека разгледаме един пример.

### Примерен клиент

Нека разгледаме този примерен клиент:

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

// Изброяване на подсказки
const prompts = await client.listPrompts();

// Вземи подсказка
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Изброяване на ресурси
const resources = await client.listResources();

// Прочети ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Повикай инструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

В горния код ние:

- Импортираме библиотеките
- Създаваме екземпляр на клиент и го свързваме, използвайки stdio като транспорт.
- Изброяваме подкани, ресурси и инструменти и ги извикваме всички.

Ето го, клиент, който може да комуникира с MCP сървър.

Нека отделим време в следващото упражнение да разгледаме всеки кодов откъс и да обясним какво се случва.

## Упражнение: Написване на клиент

Както казахме по-горе, нека отделим време да обясним кода, и по възможност пишете кода едновременно с нас, ако желаете.

### -1- Импортиране на библиотеките

Нека импортираме нужните библиотеки, ще ни трябват референции към клиент и към избрания транспортен протокол, stdio. stdio е протокол за неща, които са предназначени да се стартират на локалния ви компютър. SSE е друг транспортен протокол, който ще покажем в бъдещи глави, но това е другият ви вариант. Засега продължаваме със stdio.

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

За Java ще създадете клиент, който се свързва към MCP сървъра от предишното упражнение. Използвайки същата структура на проекта Java Spring Boot от [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), създайте нов Java клас на име `SDKClient` в папката `src/main/java/com/microsoft/mcp/sample/client/` и добавете следните импорти:

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

Ще трябва да добавите следните зависимости във файла си `Cargo.toml`.

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

Оттам можете да импортирате необходимите библиотеки в кода на клиента си.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Нека преминем към инициализацията.

### -2- Инициализиране на клиент и транспорт

Трябва да създадем екземпляр на транспорта и този на клиента ни:

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

В горния код:

- Създадохме екземпляр на stdio транспорт. Обърнете внимание, че се посочват команда и аргументи за това как да се намери и стартира сървъра, тъй като това е нещо, което ще трябва да направим когато създаваме клиента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Инициализирахме клиент, като му дадохме име и версия.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Свързахме клиента с избрания транспорт.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Създаване на параметри за сървър за stdio връзка
server_params = StdioServerParameters(
    command="mcp",  # Изпълним файл
    args=["run", "server.py"],  # Опционални аргументи на командния ред
    env=None,  # Опционални променливи на средата
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

В горния код:

- Импортираме нужните библиотеки
- Инициализираме обект с параметри за сървъра, който ще използваме, за да стартираме сървъра и да се свържем с него чрез клиента.
- Дефинирахме метод `run`, който от своя страна извиква `stdio_client`, който стартира клиентска сесия.
- Създадохме входна точка, където подаваме метода `run` на `asyncio.run`.

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

В горния код:

- Импортирахме нужните библиотеки.
- Създадохме stdio транспорт и клиент `mcpClient`. Последният е това, което ще използваме за изброяване и извикване на функции на MCP сървъра.

Забележка: в "Arguments" можете да посочите или *.csproj*, или изпълнимия файл.

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
        
        // Вашата клиентска логика отива тук
    }
}
```

В горния код:

- Създадохме главен метод, който настройва SSE транспорт, сочещ към `http://localhost:8080`, където ще работи нашия MCP сървър.
- Създадохме клиентски клас, който приема транспорта като параметър на конструктора.
- В метода `run` създаваме синхронен MCP клиент с помощта на транспорта и инициализираме връзката.
- Използвахме SSE (Server-Sent Events) транспорт, подходящ за HTTP базирана комуникация с MCP сървъри на Java Spring Boot.

#### Rust

Обърнете внимание, че този Rust клиент предполага, че сървърът е съседен проект с име "calculator-server" в същата директория. Кодът по-долу ще стартира сървъра и ще се свърже с него.

```rust
async fn main() -> Result<(), RmcpError> {
    // Предполага се, че сървърът е свързан проект на име "calculator-server" в същата директория
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

    // TODO: Инициализиране

    // TODO: Изброяване на инструментите

    // TODO: Извикайте добавяне на инструмент с аргументи = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Изброяване на функциите на сървъра

Сега имаме клиент, който може да се свърже, ако програмата бъде стартирана. Въпреки това, той всъщност не изброява функциите си, така че нека направим това сега:

#### TypeScript

```typescript
// Изброяване на подсказки
const prompts = await client.listPrompts();

// Изброяване на ресурси
const resources = await client.listResources();

// изброяване на инструменти
const tools = await client.listTools();
```

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
```

Тук изброяваме наличните ресурси с `list_resources()` и инструменти с `list_tools` и ги отпечатваме.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Горният пример показва как можем да изброим инструментите на сървъра. За всеки инструмент отпечатваме името му.

#### Java

```java
// Избройте и демонстрирайте инструменти
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Можете също да пингнете сървъра, за да проверите връзката
client.ping();
```

В горния код:

- Извикахме `listTools()` за да получим всички налични инструменти от MCP сървъра.
- Използвахме `ping()` за да проверим дали връзката със сървъра работи.
- `ListToolsResult` съдържа информация за всички инструменти, включително техните имена, описания и схеми на входните данни.

Отлично, сега сме събрали всички функции. Следващият въпрос е кога да ги използваме? Този клиент е доста прост; прост в смисъл, че ще трябва експлицитно да извикваме функциите, когато искаме. В следващата глава ще създадем по-усъвършенстван клиент, който има достъп до собствен голям езиков модел, LLM. Засега обаче нека видим как можем да извикаме функциите на сървъра:

#### Rust

В главната функция, след инициализацията на клиента, можем да инициализираме сървъра и да изброим някои от функциите му.

```rust
// Инициализиране
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Изброяване на инструментите
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Извикване на функции

За да извикаме функции, трябва да осигурим правилни аргументи и в някои случаи името на това, което искаме да извикаме.

#### TypeScript

```typescript

// Прочетете ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Извикайте инструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// извикайте подкана
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

В горния код:

- Четем ресурс, като го извикваме с `readResource()`, посочвайки `uri`. Ето как това най-вероятно изглежда на сървърната страна:

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

    Нашата стойност `uri` е `file://example.txt`, което съвпада с `file://{name}` на сървъра. `example.txt` ще бъде картографирано към `name`.

- Извикваме инструмент, като посочваме неговото `name` и `arguments`, така:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Вземаме подкана (промпт), за да я получим, извикваме `getPrompt()` с `name` и `arguments`. Кодът на сървъра изглежда така:

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

    и вашият клиентски код следва да изглежда така, за да съвпада с това, което е декларирано на сървъра:

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
# Прочетете ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Извикайте инструмент
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

В горния код:

- Извикахме ресурс на име `greeting`, използвайки `read_resource`.
- Извикахме инструмент на име `add` чрез `call_tool`.

#### .NET

1. Нека добавим код за извикване на инструмент:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. За да отпечатаме резултата, ето код за обработка:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Извикайте различни калкулаторни инструменти
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

В горния код:

- Извикахме множество калкулаторни инструменти чрез метода `callTool()` с обекти `CallToolRequest`.
- Всеки извикващ инструмент посочва името на инструмента и `Map` с аргументи, необходими от инструмента.
- Инструментите на сървъра очакват конкретни имена на параметри (като "a", "b" за математически операции).
- Резултатите се връщат като обекти `CallToolResult`, съдържащи отговора от сървъра.

#### Rust

```rust
// Извикайте добавящия инструмент с аргументи = {"a": 3, "b": 2}
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

### -5- Стартиране на клиента

За да стартирате клиента, въведете следната команда в терминала:

#### TypeScript

Добавете следния запис в секцията "scripts" в *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Извикайте клиента с следната команда:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Първо се уверете, че MCP сървърът ви работи на `http://localhost:8080`. След това стартирайте клиента:

```bash
# Компилирайте вашия проект
./mvnw clean compile

# Стартирайте клиента
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Алтернативно, можете да стартирате пълния клиентски проект, предоставен в папката с решение `03-GettingStarted\02-client\solution\java`:

```bash
# Навигирайте до директорията на решението
cd 03-GettingStarted/02-client/solution/java

# Компилирайте и стартирайте JAR файла
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Задание

В това задание ще използвате наученото за създаване на клиент, но ще създадете собствен.

Ето един сървър, който можете да използвате и към който трябва да се обаждате чрез вашия клиентски код. Опитайте да добавите повече функции на сървъра, за да го направите по-интересен.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Създайте MCP сървър
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Добавете инструмент за събиране
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Добавете динамичен ресурс за поздрав
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

// Започнете да получавате съобщения от stdin и да изпращате съобщения към stdout

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

# Създайте MCP сървър
mcp = FastMCP("Demo")


# Добавете инструмент за събиране
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Добавете динамичен ресурс за поздравяване
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

Вижте този проект за това как да [добавяте подкани и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Също, проверете тази връзка за това как да извиквате [подкани и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предишния раздел](../../../../03-GettingStarted/01-first-server) научихте как да създадете прост MCP сървър с Rust. Можете да продължите да го развивате или да разгледате тази връзка за още примери на MCP сървъри на Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

**Папката с решението** съдържа пълни, готови за изпълнение клиентски реализации, които демонстрират всички концепции, разгледани в това ръководство. Всяко решение включва както клиентски, така и сървърни кодове, организирани в отделни, самостоятелни проекти.

### 📁 Структура на решението

Директорията с решението е организирана по програмни езици:

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

### 🚀 Какво включва всяко решение

Всяко решение за конкретен език предоставя:

- **Пълна клиентска реализация** с всички функции от урока
- **Работна структура на проекта** с правилни зависимости и конфигурация
- **Скриптове за компилиране и изпълнение** за лесна настройка и стартиране
- **Подробен README** с инструкции специфични за езика
- **Обработка на грешки** и примери за обработка на резултати

### 📖 Използване на решенията

1. **Навигирайте до папката за предпочитания от вас език**:

   ```bash
   cd solution/typescript/    # За TypeScript
   cd solution/java/          # За Java
   cd solution/python/        # За Python
   cd solution/dotnet/        # За .NET
   ```

2. **Следвайте инструкциите в README във всяка папка за**:
   - Инсталиране на зависимости
   - Компилиране на проекта
   - Стартиране на клиента

3. **Примерен изход, който трябва да видите**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

За пълна документация и инструкции стъпка по стъпка, вижте: **[📖 Документация на решението](./solution/README.md)**

## 🎯 Пълни примери

Предоставили сме пълни, работещи клиентски реализации за всички програмни езици, разгледани в този урок. Тези примери демонстрират цялата функционалност описана по-горе и могат да се използват като референтни реализации или отправна точка за ваши собствени проекти.

### Налични пълни примери

| Език    | Файл                               | Описание                                                        |
|---------|------------------------------------|-----------------------------------------------------------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)   | Пълен Java клиент с SSE транспорт и подробна обработка на грешки |
| **C#**      | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)   | Пълен C# клиент с stdio транспорт и автоматично стартиране на сървъра |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Пълен TypeScript клиент с пълна поддръжка на MCP протокола      |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)   | Пълен Python клиент с асинхронни async/await шаблони            |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)       | Пълен Rust клиент с Tokio за асинхронни операции                |

Всяка пълна демонстрация включва:
- ✅ **Установяване на връзка** и обработка на грешки
- ✅ **Откриване на сървър** (инструменти, ресурси, подканяния, когато е приложимо)
- ✅ **Операции с калкулатор** (събиране, изваждане, умножение, деление, помощ)
- ✅ **Обработка на резултатите** и форматиран изход
- ✅ **Всеобхватна обработка на грешки**
- ✅ **Чист, документиран код** със стъпка по стъпка коментари

### Започване с пълни примери

1. **Изберете предпочитания език** от таблицата по-горе  
2. **Прегледайте пълния примерен файл**, за да разберете пълната реализация  
3. **Стартирайте примера** според инструкциите в [`complete_examples.md`](./complete_examples.md)  
4. **Модифицирайте и разширете** примера за вашия конкретен случай  

За подробна документация относно стартирането и персонализирането на тези примери вижте: **[📖 Документация на пълните примери](./complete_examples.md)**

### 💡 Решение срещу пълни примери

| **Папка с решение** | **Пълни примери** |
|--------------------|-------------------|
| Пълна структура на проекта с файлове за компилиране | Имплементации в един файл |
| Готово за работа със зависимости | Фокусирани примери на код |
| Настройка подобна на продукция | Образователна справка |
| Езиково специфични инструменти | Сравнение между езици |

И двата подхода са ценни – използвайте **папката с решение** за пълни проекти и **пълните примери** за учене и справка.

## Основни изводи

Основните изводи за тази глава относно клиентите са:

- Могат да се използват както за откриване, така и за извикване на функции на сървъра.  
- Могат да стартират сървър, докато се стартират сами (както в тази глава), но клиентите могат да се свързват и към вече работещи сървъри.  
- Това е чудесен начин да тествате възможностите на сървъра заедно с алтернативи като Inspector, както беше описано в предишната глава.

## Допълнителни ресурси

- [Създаване на клиенти в MCP](https://modelcontextprotocol.io/quickstart/client)

## Примери

- [Java Калкулатор](../samples/java/calculator/README.md)  
- [.Net Калкулатор](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Калкулатор](../samples/javascript/README.md)  
- [TypeScript Калкулатор](../samples/typescript/README.md)  
- [Python Калкулатор](../../../../03-GettingStarted/samples/python)  
- [Rust Калкулатор](../../../../03-GettingStarted/samples/rust)

## Какво следва

- Следва: [Създаване на клиент с LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, възникнали от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
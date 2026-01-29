# Създаване на клиент

Клиентите са персонализирани приложения или скриптове, които комуникират директно с MCP сървър, за да заявяват ресурси, инструменти и подсказки. За разлика от използването на инструмента за инспекция, който предоставя графичен интерфейс за взаимодействие със сървъра, писането на собствен клиент позволява програматични и автоматизирани взаимодействия. Това дава възможност на разработчиците да интегрират възможностите на MCP в своите работни процеси, да автоматизират задачи и да създават персонализирани решения, съобразени с конкретни нужди.

## Общ преглед

Този урок представя концепцията за клиенти в екосистемата на Model Context Protocol (MCP). Ще научите как да напишете собствен клиент и да го свържете с MCP сървър.

## Цели на обучението

До края на този урок ще можете:

- Да разберете какво може да прави един клиент.
- Да напишете собствен клиент.
- Да свържете и тествате клиента с MCP сървър, за да се уверите, че той работи както се очаква.

## Какво включва писането на клиент?

За да напишете клиент, трябва да направите следното:

- **Импортирайте правилните библиотеки**. Ще използвате същата библиотека като преди, но с различни конструкции.
- **Създайте клиент**. Това включва създаване на инстанция на клиент и свързването му с избрания метод за транспорт.
- **Решете кои ресурси да изброите**. Вашият MCP сървър разполага с ресурси, инструменти и подсказки, трябва да решите кои от тях да изброите.
- **Интегрирайте клиента към хост приложението**. След като разберете възможностите на сървъра, трябва да го интегрирате към хост приложението, така че когато потребителят въведе подсказка или друга команда, съответната функция на сървъра да бъде извикана.

Сега, след като разбираме на високо ниво какво предстои да направим, нека разгледаме пример.

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

В горния код:

- Импортираме библиотеките.
- Създаваме инстанция на клиент и го свързваме чрез stdio за транспорт.
- Изброяваме подсказки, ресурси и инструменти и ги извикваме.

Ето го, клиент, който може да комуникира с MCP сървър.

Нека отделим време в следващата секция с упражнения, за да разгледаме подробно всеки кодов фрагмент и да обясним какво се случва.

## Упражнение: Писане на клиент

Както казахме по-горе, нека отделим време за обяснение на кода, и ако искате, кодирайте заедно с нас.

### -1- Импортиране на библиотеки

Нека импортираме необходимите библиотеки. Ще ни трябват референции към клиент и към избрания транспортен протокол, stdio. stdio е протокол за неща, които трябва да се изпълняват на вашата локална машина. SSE е друг транспортен протокол, който ще покажем в бъдещи глави, но това е вашата друга опция. Засега обаче, нека продължим със stdio.

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

За Java ще създадете клиент, който се свързва с MCP сървъра от предишното упражнение. Използвайки същата структура на проект Java Spring Boot от [Започване с MCP сървър](../../../../03-GettingStarted/01-first-server/solution/java), създайте нов Java клас, наречен `SDKClient` в папката `src/main/java/com/microsoft/mcp/sample/client/` и добавете следните импорти:

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

Ще трябва да добавите следните зависимости към вашия файл `Cargo.toml`.

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

След това можете да импортирате необходимите библиотеки в клиентския код.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Нека преминем към създаването на инстанция.

### -2- Създаване на клиент и транспорт

Ще трябва да създадем инстанция на транспорта и на нашия клиент:

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

- Създадохме инстанция на stdio транспорт. Обърнете внимание как той специфицира команда и аргументи за това как да намери и стартира сървъра, тъй като това е нещо, което ще трябва да направим, докато създаваме клиента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Създадохме клиент, като му дадохме име и версия.

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

В горния код:

- Импортирахме необходимите библиотеки.
- Създадохме обект с параметри на сървъра, тъй като ще го използваме, за да стартираме сървъра, за да можем да се свържем с него чрез нашия клиент.
- Дефинирахме метод `run`, който от своя страна извиква `stdio_client`, за да стартира клиентска сесия.
- Създадохме входна точка, където предоставяме метода `run` на `asyncio.run`.

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

В горния код:

- Импортирахме необходимите библиотеки.
- Създадохме stdio транспорт и клиент `mcpClient`. Последният ще използваме, за да изброим и извикаме функции на MCP сървъра.

Обърнете внимание, че в "Arguments" можете да посочите или *.csproj*, или изпълнимия файл.

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

В горния код:

- Създадохме основен метод, който настройва SSE транспорт, сочещ към `http://localhost:8080`, където ще работи нашият MCP сървър.
- Създадохме клиентски клас, който приема транспорта като параметър на конструктора.
- В метода `run` създаваме синхронен MCP клиент, използвайки транспорта, и инициализираме връзката.
- Използвахме SSE (Server-Sent Events) транспорт, който е подходящ за HTTP-базирана комуникация с Java Spring Boot MCP сървъри.

#### Rust

Този Rust клиент предполага, че сървърът е съседен проект, наречен "calculator-server", в същата директория. Кодът по-долу ще стартира сървъра и ще се свърже с него.

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

### -3- Изброяване на функциите на сървъра

Сега имаме клиент, който може да се свърже, ако програмата бъде стартирана. Въпреки това, той не изброява функциите си, така че нека направим това следващо:

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

Тук изброяваме наличните ресурси, `list_resources()` и инструменти, `list_tools`, и ги отпечатваме.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Горният пример показва как можем да изброим инструментите на сървъра. За всеки инструмент отпечатваме неговото име.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

В горния код:

- Извикахме `listTools()`, за да получим всички налични инструменти от MCP сървъра.
- Използвахме `ping()`, за да проверим дали връзката със сървъра работи.
- `ListToolsResult` съдържа информация за всички инструменти, включително техните имена, описания и схеми за вход.

Чудесно, сега сме уловили всички функции. Въпросът е кога да ги използваме? Този клиент е доста прост, прост в смисъл, че ще трябва изрично да извикваме функциите, когато ги искаме. В следващата глава ще създадем по-усъвършенстван клиент, който има достъп до собствен модел за голям език (LLM). Засега обаче, нека видим как можем да извикаме функциите на сървъра:

#### Rust

В основната функция, след инициализацията на клиента, можем да инициализираме сървъра и да изброим някои от функциите му.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Извикване на функции

За да извикаме функциите, трябва да се уверим, че сме посочили правилните аргументи и в някои случаи името на това, което се опитваме да извикаме.

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

В горния код:

- Четем ресурс, като го извикваме чрез `readResource()`, посочвайки `uri`. Ето как най-вероятно изглежда на сървърната страна:

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

    Нашата стойност `uri` `file://example.txt` съответства на `file://{name}` на сървъра. `example.txt` ще бъде съпоставен с `name`.

- Извикваме инструмент, като го извикваме чрез посочване на неговото `name` и неговите `arguments`, както следва:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Получаваме подсказка, като я извикваме чрез `getPrompt()` с `name` и `arguments`. Кодът на сървъра изглежда така:

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

    и съответно клиентският код изглежда така, за да съответства на това, което е декларирано на сървъра:

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

В горния код:

- Извикахме ресурс, наречен `greeting`, чрез `read_resource`.
- Извикахме инструмент, наречен `add`, чрез `call_tool`.

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

В горния код:

- Извикахме няколко инструмента за калкулатор чрез метода `callTool()` с обекти `CallToolRequest`.
- Всяко извикване на инструмент специфицира името на инструмента и `Map` с аргументи, необходими за този инструмент.
- Инструментите на сървъра очакват специфични имена на параметри (като "a", "b" за математически операции).
- Резултатите се връщат като обекти `CallToolResult`, съдържащи отговора от сървъра.

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

### -5- Стартиране на клиента

За да стартирате клиента, въведете следната команда в терминала:

#### TypeScript

Добавете следния запис към секцията "scripts" в *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Стартирайте клиента със следната команда:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Първо, уверете се, че вашият MCP сървър работи на `http://localhost:8080`. След това стартирайте клиента:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Алтернативно, можете да стартирате пълния клиентски проект, предоставен в папката с решения `03-GettingStarted\02-client\solution\java`:

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

В това задание ще използвате наученото за създаване на клиент, но ще създадете свой собствен клиент.

Ето сървър, който можете да използвате и който трябва да извикате чрез вашия клиентски код. Опитайте се да добавите повече функции към сървъра, за да го направите по-интересен.

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

Вижте този проект, за да разберете как можете [да добавите подсказки и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Също така, проверете този линк за това как да извикате [подсказки и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предишната секция](../../../../03-GettingStarted/01-first-server) научихте как да създадете прост MCP сървър с Rust. Можете да продължите да надграждате върху това или да проверите този линк за повече примери за MCP сървъри, базирани на Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

**Папката с решения** съдържа пълни, готови за изпълнение клиентски реализации, които демонстрират всички концепции, разгледани в този урок. Всяко решение включва както клиентски, така и сървърни кодове, организирани в отделни, самостоятелни проекти.

### 📁 Структура на решенията

Директорията с решения е организирана по програмни езици:

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

Всяко езиково-специфично решение предоставя:

- **Пълна клиентска реализация** с всички функции от урока.
- **Работеща структура на проекта** с правилни зависимости и конфигурация.
- **Скриптове за изграждане и изпълнение** за лесна настройка и стартиране.
- **Подробен README** с инструкции, специфични за езика.
- **Примери за обработка на грешки** и обработка на резултати.

### 📖 Използване на решенията

1. **Навигирайте до предпочитаната от вас езикова папка**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Следвайте инструкциите в README** във всяка папка за:
   - Инсталиране на зависимости.
   - Изграждане на проекта.
   - Стартиране на клиента.

3. **Примерен изход**, който трябва да видите:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

За пълна документация и инструкции стъпка по стъпка, вижте: **[📖 Документация за решенията](./solution/README.md)**

## 🎯 Пълни примери

Предоставили сме пълни, работещи клиентски реализации за всички програмни езици, разгледани в този урок. Тези примери демонстрират пълната функционалност, описана по-горе, и могат да се използват като референтни реализации или начални точки за вашите собствени проекти.

### Налични пълни примери

| Език | Файл | Описание |
|------|------|----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Пълен Java клиент, използващ SSE транспорт с изчерпателна обработка на грешки |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Пълен C# клиент, използващ stdio транспорт с автоматично стартиране на сървъра |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Пълен TypeScript клиент с пълна поддръжка на MCP протокол |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Пълен Python клиент, използващ async/await модели |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Пълен Rust клиент, използващ Tokio за асинхронни операции |
Всеки завършен пример включва:

- ✅ **Установяване на връзка** и обработка на грешки
- ✅ **Откриване на сървър** (инструменти, ресурси, подсказки, където е приложимо)
- ✅ **Операции на калкулатора** (събиране, изваждане, умножение, деление, помощ)
- ✅ **Обработка на резултати** и форматиран изход
- ✅ **Цялостна обработка на грешки**
- ✅ **Чист, документиран код** със стъпка по стъпка коментари

### Започване с пълни примери

1. **Изберете предпочитания от вас език** от таблицата по-горе
2. **Прегледайте файла с пълния пример**, за да разберете цялостната имплементация
3. **Стартирайте примера**, следвайки инструкциите в [`complete_examples.md`](./complete_examples.md)
4. **Модифицирайте и разширете** примера за вашия специфичен случай

За подробна документация относно стартиране и персонализиране на тези примери, вижте: **[📖 Документация за пълни примери](./complete_examples.md)**

### 💡 Решение срещу Пълни Примери

| **Папка с решения** | **Пълни примери** |
|--------------------|--------------------- |
| Пълна структура на проекта с файлове за изграждане | Имплементации в един файл |
| Готово за стартиране с зависимости | Фокусирани кодови примери |
| Настройка, подобна на продукция | Образователен референтен материал |
| Инструменти, специфични за езика | Сравнение между различни езици |

И двата подхода са ценни - използвайте **папката с решения** за завършени проекти и **пълните примери** за обучение и референция.

## Основни изводи

Основните изводи за тази глава относно клиентите са следните:

- Могат да се използват както за откриване, така и за извикване на функции на сървъра.
- Могат да стартират сървър, докато самите те се стартират (както в тази глава), но клиентите могат да се свързват и с вече работещи сървъри.
- Са отличен начин за тестване на възможностите на сървъра, наред с алтернативи като Inspector, описан в предишната глава.

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

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
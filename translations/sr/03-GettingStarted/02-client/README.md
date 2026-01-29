# Прављење клијента

Клијенти су прилагођене апликације или скрипте које директно комуницирају са MCP сервером ради захтевања ресурса, алата и упита. За разлику од коришћења алата за инспекцију, који пружа графички интерфејс за интеракцију са сервером, писање сопственог клијента омогућава програмску и аутоматизовану интеракцију. Ово омогућава програмерима да интегришу могућности MCP-а у сопствене радне токове, аутоматизују задатке и креирају прилагођена решења прилагођена специфичним потребама.

## Преглед

Ова лекција уводи концепт клијената у оквиру екосистема Model Context Protocol (MCP). Научићете како да напишете сопствени клијент и повежете га са MCP сервером.

## Циљеви учења

На крају ове лекције, бићете у могућности да:

- Разумете шта клијент може да ради.
- Напишете сопствени клијент.
- Повежете и тестирате клијента са MCP сервером како бисте осигурали да сервер ради како се очекује.

## Шта је потребно за писање клијента?

Да бисте написали клијента, потребно је да урадите следеће:

- **Увезите одговарајуће библиотеке**. Користићете исту библиотеку као и раније, само различите конструкције.
- **Инстанцирајте клијента**. Ово укључује креирање инстанце клијента и повезивање са изабраним транспортним методом.
- **Одлучите које ресурсе ћете навести**. Ваш MCP сервер долази са ресурсима, алатима и упитима, а ви треба да одлучите које ћете навести.
- **Интегришите клијента у хост апликацију**. Када сазнате могућности сервера, потребно је да га интегришете у вашу хост апликацију тако да, ако корисник унесе упит или неку другу команду, одговарајућа функција сервера буде позвана.

Сада када смо на високом нивоу разумели шта ћемо радити, хајде да погледамо пример.

### Пример клијента

Погледајмо овај пример клијента:

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

У претходном коду смо:

- Увезли библиотеке.
- Креирали инстанцу клијента и повезали је користећи stdio као транспорт.
- Навели упите, ресурсе и алате и све их позвали.

Ето га, клијент који може да комуницира са MCP сервером.

Хајде да у наредном делу вежбе полако разложимо сваки део кода и објаснимо шта се дешава.

## Вежба: Писање клијента

Као што је горе речено, хајде да полако објаснимо код, а ако желите, можете кодирати заједно са нама.

### -1- Увоз библиотека

Хајде да увеземо библиотеке које су нам потребне. Биће нам потребне референце на клијента и на изабрани транспортни протокол, stdio. stdio је протокол за ствари које треба да се извршавају на вашем локалном рачунару. SSE је други транспортни протокол који ћемо показати у будућим поглављима, али то је ваша друга опција. За сада, наставимо са stdio.

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

За Java, креираћете клијента који се повезује са MCP сервером из претходне вежбе. Користећи исту структуру Java Spring Boot пројекта из [Почетак рада са MCP сервером](../../../../03-GettingStarted/01-first-server/solution/java), креирајте нову Java класу под називом `SDKClient` у фасцикли `src/main/java/com/microsoft/mcp/sample/client/` и додајте следеће увозе:

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

Потребно је да додате следеће зависности у ваш `Cargo.toml` фајл.

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

Одатле можете увезти потребне библиотеке у ваш код клијента.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Прелазимо на инстанцирање.

### -2- Инстанцирање клијента и транспорта

Потребно је да креирамо инстанцу транспорта и инстанцу нашег клијента:

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

У претходном коду смо:

- Креирали инстанцу stdio транспорта. Обратите пажњу како се наводе команда и аргументи за проналажење и покретање сервера, јер је то нешто што ћемо морати да урадимо приликом креирања клијента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Инстанцирали клијента дајући му име и верзију.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Повезали клијента са изабраним транспортом.

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

У претходном коду смо:

- Увезли потребне библиотеке.
- Инстанцирали објекат параметара сервера који ћемо користити за покретање сервера како бисмо могли да се повежемо са њим помоћу нашег клијента.
- Дефинисали метод `run` који позива `stdio_client` за покретање сесије клијента.
- Креирали улазну тачку где пружамо метод `run` функцији `asyncio.run`.

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

У претходном коду смо:

- Увезли потребне библиотеке.
- Креирали stdio транспорт и клијента `mcpClient`. Ово друго ћемо користити за навођење и позивање функција на MCP серверу.

Напомена: У "Arguments", можете навести или *.csproj* или извршни фајл.

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

У претходном коду смо:

- Креирали главни метод који подешава SSE транспорт који показује на `http://localhost:8080`, где ће MCP сервер бити покренут.
- Креирали класу клијента која узима транспорт као параметар конструктора.
- У методу `run`, креирали синхрони MCP клијент користећи транспорт и иницијализовали везу.
- Користили SSE (Server-Sent Events) транспорт који је погодан за HTTP-базиране комуникације са Java Spring Boot MCP серверима.

#### Rust

Овај Rust клијент претпоставља да је сервер суседни пројекат под називом "calculator-server" у истом директоријуму. Код испод ће покренути сервер и повезати се са њим.

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

### -3- Навођење функција сервера

Сада имамо клијента који може да се повеже ако се програм покрене. Међутим, он заправо не наводи своје функције, па хајде да то урадимо следеће:

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

Овде наводимо доступне ресурсе, `list_resources()` и алате, `list_tools`, и исписујемо их.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Горе је пример како можемо навести алате на серверу. За сваки алат затим исписујемо његово име.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

У претходном коду смо:

- Позвали `listTools()` да бисмо добили све доступне алате са MCP сервера.
- Користили `ping()` да бисмо проверили да ли веза са сервером функционише.
- `ListToolsResult` садржи информације о свим алатима, укључујући њихова имена, описе и шеме уноса.

Одлично, сада смо ухватили све функције. Сада је питање када их користимо? Па, овај клијент је прилично једноставан, у смислу да ћемо морати експлицитно позвати функције када их желимо. У следећем поглављу, креираћемо напреднијег клијента који има приступ сопственом великом језичком моделу (LLM). За сада, хајде да видимо како можемо позвати функције на серверу:

#### Rust

У главној функцији, након иницијализације клијента, можемо иницијализовати сервер и навести неке од његових функција.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Позивање функција

Да бисмо позвали функције, морамо осигурати да наведемо исправне аргументе и у неким случајевима име онога што покушавамо да позовемо.

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

У претходном коду смо:

- Прочитали ресурс, позвали смо ресурс помоћу `readResource()` наводећи `uri`. Ево како то највероватније изгледа на серверској страни:

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

    Наша вредност `uri` `file://example.txt` одговара `file://{name}` на серверу. `example.txt` ће бити мапиран на `name`.

- Позвали алат, позвали смо га наводећи његово `name` и његове `arguments` овако:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Добијање упита, да бисмо добили упит, позивамо `getPrompt()` са `name` и `arguments`. Код на серверу изгледа овако:

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

    и ваш резултујући код клијента изгледа овако да одговара ономе што је декларисано на серверу:

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

У претходном коду смо:

- Позвали ресурс под називом `greeting` користећи `read_resource`.
- Позвали алат под називом `add` користећи `call_tool`.

#### .NET

1. Додајмо код за позивање алата:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Да бисмо исписали резултат, ево кода који то обрађује:

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

У претходном коду смо:

- Позвали више калкулаторских алата користећи метод `callTool()` са објектима `CallToolRequest`.
- Сваки позив алата наводи име алата и `Map` аргумената потребних за тај алат.
- Серверски алати очекују специфична имена параметара (као што су "a", "b" за математичке операције).
- Резултати се враћају као објекти `CallToolResult` који садрже одговор са сервера.

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

### -5- Покретање клијента

Да бисте покренули клијента, укуцајте следећу команду у терминалу:

#### TypeScript

Додајте следећи унос у одељак "scripts" у *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Позовите клијента следећом командом:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Прво, уверите се да ваш MCP сервер ради на `http://localhost:8080`. Затим покрените клијента:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Алтернативно, можете покренути комплетан пројекат клијента који се налази у фасцикли решења `03-GettingStarted\02-client\solution\java`:

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

## Задатак

У овом задатку, користићете оно што сте научили у креирању клијента, али ћете креирати сопственог клијента.

Ево сервера који можете користити и који треба да позовете преко вашег кода клијента. Покушајте да додате више функција серверу како би био занимљивији.

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

Погледајте овај пројекат да видите како можете [додати упите и ресурсе](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Такође, проверите овај линк за позивање [упита и ресурса](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

У [претходном одељку](../../../../03-GettingStarted/01-first-server), научили сте како да креирате једноставан MCP сервер са Rust-ом. Можете наставити да радите на томе или проверите овај линк за више примера MCP сервера заснованих на Rust-у: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решење

**Фасцикла решења** садржи комплетне, спремне за покретање имплементације клијената које демонстрирају све концепте обрађене у овом туторијалу. Свако решење укључује и код клијента и код сервера организован у одвојене, самосталне пројекте.

### 📁 Структура решења

Директоријум решења је организован по програмским језицима:

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

### 🚀 Шта свако решење укључује

Свако решење специфично за језик пружа:

- **Комплетну имплементацију клијента** са свим функцијама из туторијала.
- **Радну структуру пројекта** са одговарајућим зависностима и конфигурацијом.
- **Скрипте за изградњу и покретање** за лако подешавање и извршавање.
- **Детаљан README** са упутствима специфичним за језик.
- **Примере обраде грешака** и обраде резултата.

### 📖 Коришћење решења

1. **Идите у фасциклу за жељени језик**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Пратите упутства из README фајла** у свакој фасцикли за:
   - Инсталирање зависности.
   - Изградњу пројекта.
   - Покретање клијента.

3. **Пример излаза** који би требало да видите:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

За комплетну документацију и упутства корак по корак, погледајте: **[📖 Документација решења](./solution/README.md)**

## 🎯 Комплетни примери

Обезбедили смо комплетне, функционалне имплементације клијената за све програмске језике обухваћене овим туторијалом. Ови примери демонстрирају пуну функционалност описану изнад и могу се користити као референтне имплементације или почетне тачке за ваше пројекте.

### Доступни комплетни примери

| Језик | Фајл | Опис |
|-------|------|------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Комплетан Java клијент који користи SSE транспорт са свеобухватним руковањем грешкама |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Комплетан C# клијент који користи stdio транспорт са аутоматским покретањем сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Комплетан TypeScript клијент са пуном подршком за MCP протокол |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Комплетан Python клијент који користи async/await обрасце |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Комплетан Rust клијент који користи Tokio за асинхроне операције |
Сваки комплетан пример укључује:

- ✅ **Успостављање везе** и руковање грешкама  
- ✅ **Откривање сервера** (алати, ресурси, упутства где је применљиво)  
- ✅ **Операције калкулатора** (сабирање, одузимање, множење, дељење, помоћ)  
- ✅ **Обрада резултата** и форматиран излаз  
- ✅ **Свеобухватно руковање грешкама**  
- ✅ **Чист, документован код** са коментарима корак по корак  

### Почетак рада са комплетним примерима

1. **Изаберите жељени језик** из табеле изнад  
2. **Прегледајте датотеку са комплетним примером** да бисте разумели целокупну имплементацију  
3. **Покрените пример** пратећи упутства у [`complete_examples.md`](./complete_examples.md)  
4. **Измените и проширите** пример за ваш специфичан случај употребе  

За детаљну документацију о покретању и прилагођавању ових примера, погледајте: **[📖 Документација комплетних примера](./complete_examples.md)**  

### 💡 Решење у односу на комплетне примере

| **Фолдер решења**       | **Комплетни примери**       |  
|-------------------------|----------------------------|  
| Комплетна структура пројекта са фајловима за изградњу | Имплементације у једној датотеци |  
| Спремно за покретање са зависностима | Фокусирани код примери |  
| Подешавање налик продукцији | Едукативни референтни материјал |  
| Алатке специфичне за језик | Поређење између језика |  

Оба приступа су вредна - користите **фолдер решења** за комплетне пројекте и **комплетне примере** за учење и референцу.  

## Кључне поуке  

Кључне поуке из овог поглавља о клијентима су следеће:  

- Могу се користити и за откривање и за позивање функција на серверу.  
- Могу покренути сервер док се сами покрећу (као у овом поглављу), али клијенти се такође могу повезати са већ покренутим серверима.  
- Представљају одличан начин за тестирање могућности сервера поред алтернатива као што је Инспектор, који је описан у претходном поглављу.  

## Додатни ресурси  

- [Изградња клијената у MCP](https://modelcontextprotocol.io/quickstart/client)  

## Примери  

- [Java Калкулатор](../samples/java/calculator/README.md)  
- [.Net Калкулатор](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Калкулатор](../samples/javascript/README.md)  
- [TypeScript Калкулатор](../samples/typescript/README.md)  
- [Python Калкулатор](../../../../03-GettingStarted/samples/python)  
- [Rust Калкулатор](../../../../03-GettingStarted/samples/rust)  

## Шта следи  

- Следеће: [Креирање клијента са LLM](../03-llm-client/README.md)  

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.
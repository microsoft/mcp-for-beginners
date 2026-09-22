# Креирање клијента

Клијенти су прилагођене апликације или скрипте које директно комуницирају са MCP сервером да би захтевале ресурсе, алате и промптове. За разлику од коришћења алата инспектора, који пружа графички интерфејс за интеракцију са сервером, писање властитог клијента омогућава програмску и аутоматизовану интеракцију. Ово омогућава програмерима да интегришу MCP могућности у своје радне токове, аутоматизују задатке и праве прилагођена решења прилагођена специфичним потребама.

## Преглед

Ова лекција уводи концепт клијената у оквиру екосистема Model Context Protocol (MCP). Учите како да напишете властитог клијента и повежете га са MCP сервером.

## Циљеви учења

До краја ове лекције, моћи ћете да:

- Разумете шта клијент може да ради.
- Напишете властитог клијента.
- Повежете и тестирате клијента са MCP сервером како бисте били сигурни да све ради како се очекује.

## Шта је потребно за писање клијента?

Да бисте написали клијента, мораћете да урадите следеће:

- **Увоз одговарајућих библиотека**. Користићете исту библиотеку као раније, само различите конструкције.
- **Инстанцирајте клијента**. Ово укључује креирање инстанце клијента и повезивање на изабрани метод транспорта.
- **Одлучите које ресурсе ћете навести**. Ваш MCP сервер долази са ресурсима, алатима и промптовима, морате одлучити које ћете навести.
- **Интегришите клијента у хост апликацију**. Када знате могућности сервера, потребно је да то интегришете у вашу хост апликацију тако да ако корисник унесе промпт или команду, одговарајућа функција сервера буде позвана.

Сада када разумемо на високом нивоу шта ћемо урадити, погледајмо следећи пример.

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

// Листа упита
const prompts = await client.listPrompts();

// Узми упит
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Листа ресурса
const resources = await client.listResources();

// Прочитај ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Позови алат
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

У претходном коду смо:

- Увезли библиотеке
- Креирали инстанцу клијента и повезали га користећи stdio као транспорт.
- Навели промптове, ресурсе и алате и позвали их све.

Ето га, клијент који може комуницирати са MCP сервером.

У следећој вежби ћемо издвојити сваки део кода и објаснити шта се дешава.

## Вежба: Писање клијента

Као што је горе речено, хајде да полако објаснимо код и слободно кодирајте уз нас ако желите.

### -1- Увоз библиотека

Увезимо библиотеке које су нам потребне, потребни су нам референце за клијента и изабрани транспортни протокол, stdio. Stdio је протокол за ствари које треба да раде на локалној машини. SSE је други транспортни протокол који ћемо показати у будућим поглављима, али за сада настављамо са stdio.

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

За Јаву, креираћете клијента који се повезује на MCP сервер из претходне вежбе. Користећи исти пројект Java Spring Boot структуру из [Почетак са MCP сервером](../../../../03-GettingStarted/01-first-server/solution/java), направите нову кладу `SDKClient` у фасцикли `src/main/java/com/microsoft/mcp/sample/client/` и додатно увезите следеће:

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

Потребно је да додате следеће зависности у ваш датотеку `Cargo.toml`.

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

Након тога, можете увезти потребне библиотеке у вашем коду клијента.

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

Потребно је да направимо инстанце транспорта и нашег клијента:

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

- Креирали инстанцу stdio транспорта. Имајте на уму како наводи команду и аргументе за лоцирање и покретање сервера јер то морамо урадити док правимо клијента.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Инстанцирали клијента тако што смо му дали име и верзију.

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

# Креирај параметре сервера за стандардну улазно-излазну везу
server_params = StdioServerParameters(
    command="mcp",  # Извршна датотека
    args=["run", "server.py"],  # Опциони аргументи командне линије
    env=None,  # Опционе променљиве окружења
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Иницијализуј везу
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

У претходном коду смо:

- Увезли потребне библиотеке
- Инстанцирали објекат параметара за сервер јер ћемо га користити за покретање сервера како бисмо могли да се повежемо са нашим клијентом.
- Дефинисали методу `run` која позива `stdio_client` која покреће сесију клијента.
- Креирали улазну тачку где методу `run` предајемо `asyncio.run`.

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

У претходном коду смо:

- Увезли потребне библиотеке.
- Креирали stdio транспорт и креирали клијента `mcpClient`. Користићемо га за навођење и позивање функција на MCP серверу.

Напомена, у "Arguments" можете указати и на *.csproj* или на извршну датотеку.

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
        
        // Логика вашег клијента иде овде
    }
}
```

У претходном коду смо:

- Направили главну методу која подешава SSE транспорт упућујући на `http://localhost:8080` где ће наш MCP сервер бити покренут.
- Креирали класу клијента која као параметар конструктору узима транспорт.
- У методи `run` креирамо синхрони MCP клијента користећи транспорт и иницијализујемо везу.
- Користили SSE (Server-Sent Events) транспорт који је прикладан за HTTP комуникацију са Java Spring Boot MCP серверима.

#### Rust

Напомена: овај Rust клијент претпоставља да је сервер сестрински пројекат под називом "calculator-server" у истом директоријуму. Код испод ће покренути сервер и повезати се са њим.

```rust
async fn main() -> Result<(), RmcpError> {
    // Претпоставите да је сервер сестрински пројекат под именом "calculator-server" у истом директоријуму
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

    // TODO: Инициализујте

    // TODO: Направите листу алата

    // TODO: Позовите алат add са аргументима = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Навођење функција сервера

Сад имамо клијента који може да се повеже ако се програм покрене. Међутим, он не наводи тренутно његове функције па хајде да то урадимо сада:

#### TypeScript

```typescript
// Списак упита
const prompts = await client.listPrompts();

// Списак ресурса
const resources = await client.listResources();

// списак алата
const tools = await client.listTools();
```

#### Python

```python
# Листа доступних ресурса
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Листа доступних алата
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Овде наводимо расположиве ресурсе, `list_resources()` и алате, `list_tools` и исписујемо их.

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
// Наведи и демонстрирај алате
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Такође можете да пингујете сервер да бисте проверили везу
client.ping();
```

У претходном коду смо:

- Позвали `listTools()` како бисмо добили све расположиве алате са MCP сервера.
- Користили `ping()` да проверимо да ли је веза са сервером успостављена.
- `ListToolsResult` садржи информације о свим алатима укључујући њихова имена, описе и шеме улаза.

Одлично, сада смо добили све функције. Следеће питање: када их користити? Овај клијент је прилично једноставан, у смислу да ћемо морати експлицитно позивати функције кад год их желимо користити. У следећем поглављу направићемо напреднијег клијента који има приступ сопственом великом језичком моделу, LLM-у. За сада, хајде да видимо како можемо позивати функције на серверу:

#### Rust

У главној функцији, након иницијализације клијента, можемо иницијализовати сервер и навести неке од његових функција.

```rust
// Иницијализуј
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Листа алата
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Позивање функција

Да бисмо позвали функције, морамо обезбедити исправне аргументе, а у неким случајевима и име оно што желимо да позовемо.

#### TypeScript

```typescript

// Прочитај ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Позови алат
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// позови упит
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

У претходном коду смо:

- Читали ресурс, позивамо ресурс коришћењем `readResource()` и навођењем `uri`. Ево како то највероватније изгледа са стране сервера:

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

    Вредност нашег `uri` `file://example.txt` се поклапа са `file://{name}` на серверу. `example.txt` ће бити мапиран на `name`.

- Позвали алат тако што смо навели његово `name` и његове `arguments` овако:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Добили промпт, да бисте добили промпт, позовите `getPrompt()` са `name` и `arguments`. Серверски код изгледа овако:

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

    и клијент код који добијате изгледа овако да одговара ономе што је дефинисано на серверу:

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
# Учитај ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Позови алат
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

У претходном коду смо:

- Позвали ресурс под именом `greeting` коришћењем `read_resource`.
- Позвали алат под именом `add` коришћењем `call_tool`.

#### .NET

1. Додајмо код за позивање алата:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. За испис резултата, ево кода за то:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Позови разне калкулатор алате
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

- Позвали више калкулаторских алата коришћењем `callTool()` методе са `CallToolRequest` објектима.
- Сваки позив алата указује на име алата и `Map` аргумената које од алата захтева.
- Серверски алати очекују специфична имена параметара (као "a", "b" код математичких операција).
- Резултати су враћени као `CallToolResult` објекти са одговором сервера.

#### Rust

```rust
// Позивање алата за сабирање са аргументима = {"a": 3, "b": 2}
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

Додајте следећи унос у секцију "scripts" у *package.json*:

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

Прво, уверите се да је ваш MCP сервер покренут на `http://localhost:8080`. Затим покрените клијента:

```bash
# Направите ваш пројекат
./mvnw clean compile

# Покрените клијента
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Или, можете покренути комплетан клијент пројекат који се налази у фасцикли решења `03-GettingStarted\02-client\solution\java`:

```bash
# Идите до директоријума решења
cd 03-GettingStarted/02-client/solution/java

# Изградите и покрените JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Задатак

У овом задатку, користићете оно што сте научили о креирању клијента, али направите свог властитог клијента.

Ево сервера који можете користити и који треба да позовете преко кода вашег клијента, покушајте да додате више функција серверу да би био занимљивији.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Креирај MCP сервер
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Додај алатку за сабирање
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Додај динамички ресурс за поздрав
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

// Почни да примаш поруке на stdin и шаљеш поруке на stdout

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

# Креирај MCP сервер
mcp = FastMCP("Demo")


# Додај алат за сабирање
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Додај динамички ресурс за поздрављање
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

Погледајте овај пројекат да бисте видели како [додати промптове и ресурсе](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Такође, проверите овај линк за то како да позивате [промптове и ресурсе](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

У [претходном одељку](../../../../03-GettingStarted/01-first-server) сте учили како се прави једноставан MCP сервер у Rust-у. Можете наставити да надограђујете то или проверити овај линк за више примера MCP сервера у Rust-у: [Примери MCP сервера](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решење

Фасцикла **решења** садржи комплетне, спремне за покретање имплементације клијената које демонстрирају све концепте обухваћене овим туторијалом. Свако решење садржи и клиентски и серверски код, организован у одвојене, самосталне пројекте.

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

### 🚀 Шта свака имплементација садржи

Свако решење за одређени језик пружа:

- **Комплетну имплементацију клијента** са свим функцијама из туторијала
- **Радну структуру пројекта** са одговарајућим зависностима и конфигурацијом
- **Скрипте за састављање и покретање** ради лакшег подешавања и извршења
- **Детаљан README** са упутствима специфичним за језик
- **Примере руковођења грешкама** и обраде резултата

### 📖 Коришћење решења

1. **Пронађите фасциклу свог омиљеног језика**:

   ```bash
   cd solution/typescript/    # За TypeScript
   cd solution/java/          # За Java
   cd solution/python/        # За Python
   cd solution/dotnet/        # За .NET
   ```

2. **Пратите упутства у README-у** у свакој фасцикли за:
   - Инсталирање зависности
   - Састављање пројекта
   - Покретање клијента

3. **Пример излаза** који би требало да видите:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

За комплетну документацију и корак по корак упутства, видите: **[📖 Документација за решење](./solution/README.md)**

## 🎯 Комплетни примери

Обезбедили смо комплетне, радне имплементације клијената за све програмске језике обухваћене овим туторијалом. Ови примери показују потпуну функционалност описану горе и могу се користити као референтне имплементације или почетне тачке за ваше пројекте.

### Доступни комплетни примери

| Језик | Датотека | Опис |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Комплетан Java клијент користећи SSE транспорт са свеобухватним руковањем грешкама |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Комплетан C# клијент користећи stdio транспорт са аутоматским покретањем сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Комплетан TypeScript клијент са пуном MCP протокол подршком |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Комплетан Python клијент користећи async/await шаблоне |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Комплетан Rust клијент користећи Tokio за асинхроне операције |

Сваком комплетном примеру укључује:

- ✅ **Успостављање везе** и руковање грешкама
- ✅ **Откривање сервера** (алати, ресурси, промптови где је примењиво)
- ✅ **Операције калкулатора** (збир, разлика, множење, дељење, помоћ)
- ✅ **Обрада резултата** и форматисани излаз
- ✅ **Свеобухватно руковање грешкама**

- ✅ **Чист, документиран код** са корак-по-корак коментарима

### Почетак са комплетним примерима

1. **Изаберите жељени језик** из табеле изнад
2. **Прегледајте комплетну датотеку примера** да бисте разумели пуну имплементацију
3. **Покрените пример** пратећи упутства у [`complete_examples.md`](./complete_examples.md)
4. **Измените и проширите** пример за ваш специфичан случај употребе

За детаљну документацију о покретању и прилагођавању ових примера погледајте: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 Решење у односу на комплетне примере

| **Фасцикла решења** | **Комплетни примери** |
|--------------------|--------------------- |
| Комплетна структура пројекта са билд фајловима | Имплементације у једној датотеци |
| Спремно за покретање са зависностима | Фокусирани примери кода |
| Постављање слично производном окружењу | Едукативна референца |
| Алати специфични за језик | Поређење између језика |

Обе методе су вредне - користите **фасциклу решења** за комплетне пројекте и **комплетне примере** за учење и референцу.

## Кључне поруке

Кључне поруке ове главе везане су за клијенте:

- Могу се користити и за откривање и за позивање функција на серверу.
- Могу да покрену сервер док се сервер сам покреће (као у овој глави), али клијенти се могу повезати и на већ покренуте сервере.
- Одличан су начин да се тестирају могућности сервера поред алтернатива као што је Инспектор описан у претходној глави.

## Додатни ресурси

- [Прављење клијената у MCP](https://modelcontextprotocol.io/quickstart/client)

## Узорци

- [Java калкулатор](../samples/java/calculator/README.md)
- [.NET калкулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript калкулатор](../samples/javascript/README.md)
- [TypeScript калкулатор](../samples/typescript/README.md)
- [Python калкулатор](../../../../03-GettingStarted/samples/python)
- [Rust калкулатор](../../../../03-GettingStarted/samples/rust)

## Шта следи

- Следеће: [Прављење клијента са LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
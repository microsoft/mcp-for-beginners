# Креирање клијента

Клијенти су прилагођене апликације или скрипте које директно комуницирају са MCP сервером како би тражили ресурсе, алате и упите. За разлику од коришћења алата инспектора, који пружа графички интерфејс за интеракцију са сервером, писање свог клијента омогућава програмске и аутоматизоване интеракције. Ово омогућава програмерима да интегришу MCP могућности у своје радне токове, аутоматизују задатке и граде прилагођена решења прилагођена специфичним потребама.

## Преглед

Овај час уводи концепт клијената у оквиру Model Context Protocol (MCP) екосистема. Научићете како да напишете свог клијента и повежете га са MCP сервером.

## Циљеви учења

На крају овог часа, бићете у стању да:

- Разумете шта клијент може да ради.
- Напишете свог клијента.
- Повежете и тестирате клијента са MCP сервером како бисте били сигурни да сервер ради како се очекује.

## Шта све улази у писање клијента?

Да бисте написали клијента, потребно је да урадите следеће:

- **Импортујте исправне библиотеке**. Користићете исту библиотеку као и раније, али са различитим конструкцијама.
- **Инстанцирајте клијента**. Ово ће укључивати креирање инстанце клијента и повезивање са изабраним транспортним методом.
- **Одлучите које ресурсе ћете набрајати**. Ваш MCP сервер има ресурсе, алате и упите, потребно је да одлучите које ћете навести.
- **Интегришите клијента у хост апликацију**. Када знате могућности сервера, потребно је да их интегришете у вашу хост апликацију тако да ако корисник унесе упит или команду, одговарајућа функција сервера буде позвана.

Сада када разумемо на високом нивоу шта ћемо урадити, хајде да погледамо пример.

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

- Импортовали библиотеке  
- Креирали инстанцу клијента и повезали је користећи stdio као транспорт.  
- Навели упите, ресурсе и алате и позвали све њих.  

Ето га, клијент који може да комуницира са MCP сервером.

У следећем делу вежбе ћемо пажљиво размотрити сваки део кода и објаснити шта се дешава.

## Вежба: Писање клијента

Као што је раније речено, узећемо време да објаснимо код, и свакако пратите ако желите да кодирајете заједно.

### -1- Импортују се библиотеке

Хајде да увеземо потребне библиотеке, биће нам потребне референце за клијента и изабрани транспортни протокол, stdio. stdio је протокол за ствари које треба да раде локално на вашем рачунару. SSE је други транспортни протокол који ћемо показати у будућим поглављима, али то је ваша друга опција. За сада настављамо са stdio.

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

За Јаву, креираћете клијента који се повезује са MCP сервером из претходне вежбе. Користећи исту структуру пројекта Java Spring Boot из [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), направите нову класу `SDKClient` у фолдеру `src/main/java/com/microsoft/mcp/sample/client/` и додайте следеће увозе:

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

Потребно је да додате следеће зависности у ваш фајл `Cargo.toml`.

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
  
Одатле можете увезти неопходне библиотеке у вашем коду клијента.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```
  
Хајде да пређемо на инстанцирање.

### -2- Инстанцирање клијента и транспорта

Морамо да направимо инстанцу транспорта и инстанцу нашег клијента:

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

- Направили инстанцу stdio транспорта. Обратите пажњу како се дефинишу команда и аргументи за покретање и проналажење сервера јер ћемо то радити док правимо клијента.

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

# Креирајте параметре сервера за stdio везу
server_params = StdioServerParameters(
    command="mcp",  # Извршна датотека
    args=["run", "server.py"],  # Опционални аргументи командне линије
    env=None,  # Опционалне променљиве окружења
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Иницијализујте везу
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```
  
У претходном коду смо:

- Увезли потребне библиотеке  
- Инстанцирали објекат параметара сервера јер ћемо га користити за покретање сервера да бисмо се могли повезати са клијентом.  
- Дефинисали метод `run` који позива `stdio_client` који покреће сесију клијента.  
- Креирали улазну тачку где пружамо `run` методу `asyncio.run`.

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
- Направили stdio транспорт и креирали клијента `mcpClient`. Ово ћемо користити за набрајање и позив функција на MCP серверу.

Напомена: у "Arguments" можете унети или *.csproj* фајл или извршни фајл.

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

- Направили main метод који подешава SSE транспорт усмерен на `http://localhost:8080` где ће радити наш MCP сервер.  
- Креирали класу клијента која као конструктор прима транспорт.  
- У `run` методу правимо синхрони MCP клијент користећи транспорт и иницијализујемо везу.  
- Користили SSE (Server-Sent Events) транспорт који је погодан за HTTP комуникацију са Java Spring Boot MCP серверима.

#### Rust

Имајте у виду да овај Rust клијент претпоставља да је сервер пројекат који се зове "calculator-server" у истом фолдеру као сестрински пројекат. Код испод покреће сервер и повезује се са њим.

```rust
async fn main() -> Result<(), RmcpError> {
    // Претпоставите да је сервер сродни пројекат под називом "calculator-server" у истом директоријуму
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

    // TODO: Иницијализуј

    // TODO: Листа алата

    // TODO: Позови додати алат са аргументима = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```
  
### -3- Набрајање функција сервера

Сада имамо клијента који може да се повеже ако се програм покрене. Међутим, он још не набраја своје функције, па хајде то да урадимо следеће:

#### TypeScript

```typescript
// Листа упита
const prompts = await client.listPrompts();

// Листа ресурса
const resources = await client.listResources();

// листа алата
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
  
Овде набрајамо доступне ресурсе, `list_resources()` и алате, `list_tools` и исписујемо их.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```
  
Горе је пример како можемо набројати алате на серверу. За сваки алат исписујемо његово име.

#### Java

```java
// Наведи и демонстрирај алате
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Такође можеш пинговати сервер да провериш везу
client.ping();
```
  
У претходном коду смо:

- Позвали `listTools()` да добијемо све доступне алате са MCP сервера.  
- Користили `ping()` да проверимо да ли је веза са сервером активна.  
- `ListToolsResult` садржи информације о свим алатима укључујући имена, описе и шеме уноса.

Одлично, сада смо ухватили све функције. Питање је када их користити? Овом клијенту је потребно да експлицитно позивамо функције кад желимо да их користимо. У следећем поглављу направићемо напреднијег клијента који има свој велики језички модел (LLM). За сада, да видимо како да позивамо функције на серверу:

#### Rust

У main функцији, након иницијализације клијента, можемо иницијализовати сервер и набројати неке његове функције.

```rust
// Иницијализуј
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Листа алата
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```
  
### -4- Позив функција

Да бисмо позвали функције потребно је да обезбедимо исправне аргументе, а понекад и име онога што позивамо.

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

- Учитали ресурс, позивамо ресурс позивом `readResource()` са параметром `uri`. Ево како то највероватније изгледа на страни сервера:

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
  
    Вредност `uri` `file://example.txt` одговара `file://{name}` на серверу. `example.txt` ће се мапирати на `name`.

- Позивамо алат, позивамо га тако што прослеђујемо његово `name` и `arguments` овако:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```
  
- Добијамо упит, да бисмо добили упит, позивамо `getPrompt()` са `name` и `arguments`. Код сервера изгледа овако:

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
  
    и ваш код клијента као резултат изгледа овако да би одговарао ономе што је дефинисано на серверу:

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
# Прочитај ресурс
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Позови алат
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```
  
У претходном коду смо:

- Позвали ресурс под именом `greeting` користећи `read_resource`.  
- Позвали алат зван `add` помоћу `call_tool`.

#### .NET

1. Додајмо код за позив алата:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```
  
1. За испис резултата, ево кода који то ради:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```
  
#### Java

```java
// Позовите разне алате калкулатора
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

- Позвали више калкулаторских алата користећи метод `callTool()` са `CallToolRequest` објектима.  
- Сваки позив алата одређује име алата и `Map` аргумената које тај алат тражи.  
- Алатке на серверу очекују специфична имена параметара (нпр. "a", "b" за математичке операције).  
- Резултати се враћају као `CallToolResult` објекти који садрже одговор сервера.

#### Rust

```rust
// Позови додатни алат са аргументима = {"a": 3, "b": 2}
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
  
### -5- Покрени клијента

Да покренете клијента укуцајте следећу команду у терминалу:

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
# Изградите ваш пројекат
./mvnw clean compile

# Покрените клијента
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```
  
Алтернативно, можете покренути комплетан клијент пројекат који се налази у фасцикли решења `03-GettingStarted\02-client\solution\java`:

```bash
# Идите до директоријума решења
cd 03-GettingStarted/02-client/solution/java

# Креирајте и покрените JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```
  
#### Rust

```bash
cargo fmt
cargo run
```
  
## Задатак

У овом задатку користићете оно што сте научили о креирању клијента, али ћете направити свог сопственог клијента.

Ево сервера који можете користити и коме треба да се обратите преко свог кода клијента, погледајте да ли можете додати више функција серверу да га учините занимљивијим.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Направите МЦП сервер
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Додајте алат за сабирање
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Додајте динамички ресурс за поздрав
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

// Почните са примањем порука на stdin и слањем порука на stdout

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
  
Погледајте овај пројекат да бисте видели како можете [додати упите и ресурсе](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Такође, проверите овај линк како да позивате [упите и ресурсе](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

У претходном одељку ([../01-first-server](../../../../03-GettingStarted/01-first-server)), научили сте како да направите једноставан MCP сервер са Rust-ом. Можете наставити да градите на томе или погледати овај линк за више примера MCP сервера у Rust-у: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решење

**Фасцикла са решењем** садржи комплетне имплементације клијента које су спремне за покретање и демонстрирају све концепте обрађене у овом туторијалу. Сва решења укључују и код клијента и сервера организованих у посебне, самосталне пројекте.

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
  
### 🚀 Шта свака решења садрже

Сва решења за одређени језик садрже:

- **Комплетну имплементацију клијента** са свим функцијама из туторијала  
- **Радну структуру пројекта** са исправним зависностима и конфигурацијом  
- **Скрипте за изградњу и покретање** ради лаког подешавања и извршења  
- **Детаљан README** са упутствима специфичним за језик  
- **Пример обраде грешака** и процесирање резултата  

### 📖 Коришћење решења

1. **Идите у фасциклу вашег одабраног језика**:

   ```bash
   cd solution/typescript/    # За TypeScript
   cd solution/java/          # За Јаву
   cd solution/python/        # За Пајтон
   cd solution/dotnet/        # За .NET
   ```
  
2. **Пратите упутства из README-а у свакој фасцикли за:**  
   - Инсталацију зависности  
   - Изградњу пројекта  
   - Покретање клијента  

3. **Пример излаза који бисте требали видети:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```
  
За комплетну документацију и упутства корак по корак, видите: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 Комплетни примери

Обезбедили смо комплетне, радне имплементације клијента за све програмске језике обухваћене овим туторијалом. Ови примери показују целокупну функционалност описану горе и могу се користити као референтне имплементације или почетне тачке за ваше сопствене пројекте.

### Доступни комплетни примери

| Језик | Фајл | Опис |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Комплетан Java клијент користећи SSE транспорт са свеобухватном обрадом грешака |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Комплетан C# клијент користећи stdio транспорт са аутоматским покретањем сервера |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Комплетан TypeScript клијент са пуном подршком MCP протокола |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Комплетан Python клијент користећи async/await образац |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Комплетан Rust клијент користећи Tokio за асинхроне операције |

Сваки комплетан пример укључује:
- ✅ **Успостављање везе** и руковање грешкама
- ✅ **Откривање сервера** (алати, ресурси, упити где је примењиво)
- ✅ **Операције калкулатора** (збир, одузимање, множење, дељење, помоћ)
- ✅ **Обрада резултата** и форматиран излаз
- ✅ **Свеобухватно руковање грешкама**
- ✅ **Чист, документован код** са корак-по-корак коментарима

### Започињање са комплетним примерима

1. **Изаберите жељени језик** из табеле изнад
2. **Прегледајте комплетну пример фајл** да бисте разумели пуну имплементацију
3. **Покрените пример** пратећи упутства у [`complete_examples.md`](./complete_examples.md)
4. **Измените и проширите** пример за ваш конкретан случај коришћења

За детаљну документацију о покретању и прилагођавању ових примера погледајте: **[📖 Документација комплетних примера](./complete_examples.md)**

### 💡 Решење у односу на комплетне примере

| **Фолдeр решења** | **Комплетни примери** |
|-------------------|---------------------- |
| Пуна структура пројекта са build фајловима | Имплементације у једном фајлу |
| Спремно за покретање са зависностима | Фокусирани код примери |
| Постављање налик производњи | Образовна референца |
| Језички специфични алати | Поређење између језика |

Обa приступa су вредна - користите **фолдер решења** за комплетне пројекте и **комплетне примере** за учење и референцу.

## Кључне напомене

Кључне напомене из овог поглавља у вези клијената су следеће:

- Могу се користити и за откривање и за позивање функција на серверу.
- Могу покренути сервер док сами стартују (као у овом поглављу), али клијенти могу да се повежу и на већ покренуте сервере.
- Одличан су начин за тестирање могућности сервера поред алтернатива као што је Inspector, како је описано у претходном поглављу.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одговорности**:  
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Док се трудимо да обезбедимо тачност, молимо имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Извори документ на његовом оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални превод од стране стручних људи. Нисмо одговорни за било какве неспоразуме или погрешна тумачења која могу произићи из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
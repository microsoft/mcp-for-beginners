# Създаване на клиент

Клиентите са персонализирани приложения или скриптове, които комуникират директно с MCP сървър, за да поискат ресурси, инструменти и подсказки. За разлика от използването на инспекторния инструмент, който предоставя графичен интерфейс за взаимодействие със сървъра, писането на собствен клиент позволява програматично и автоматизирано взаимодействие. Това дава възможност на разработчиците да интегрират възможностите на MCP във собствените си работни потоци, да автоматизират задачи и да изграждат персонализирани решения, съобразени с конкретни нужди.

## Преглед

Този урок представя концепцията за клиенти в екосистемата на Model Context Protocol (MCP). Ще научите как да напишете собствен клиент и как да го свържете със сървър MCP.

## Учебни цели

Към края на този урок ще можете:

- Да разберете какво може да направи един клиент.
- Да напишете свой собствен клиент.
- Да свържете и тествате клиента със сървър MCP, за да се уверите, че работи както се очаква.

## Какво е необходимо за писане на клиент?

За да напишете клиент, трябва да направите следното:

- **Импортиране на правилните библиотеки**. Ще използвате същата библиотека както преди, но с различни конструкции.
- **Създаване на клиент**. Това ще включва създаване на клиентски екземпляр и свързването му с избрания метод за трансфер.
- **Решаване кои ресурси да се изброят**. Вашият MCP сървър идва с ресурси, инструменти и подсказки; трябва да решите кои да се изброят.
- **Интегриране на клиента в хост приложение**. След като знаете възможностите на сървъра, трябва да интегрирате това в хост приложението, така че ако потребител въведе подсказка или друга команда, съответната функция на сървъра да се извика.

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

// Изброяване на подканите
const prompts = await client.listPrompts();

// Вземи подканa
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Изброяване на ресурсите
const resources = await client.listResources();

// Прочетете ресурс
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Извикване на инструмент
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

В предходния код ние:

- Импортираме библиотеките
- Създаваме екземпляр на клиент и го свързваме посредством stdio за трансфер.
- Изброяваме подсказки, ресурси и инструменти и ги извикваме всички.

Ето го, клиент, който може да комуникира с MCP сървър.

Нека се спрем по-подробно в следващия раздел с упражнения и разгледаме всяка част от кода и обясним какво се случва.

## Упражнение: Писане на клиент

Както беше казано по-горе, нека обясним кода на спокойствие и по желание можете да кодирате заедно с нас.

### -1- Импортиране на библиотеки

Нека импортираме библиотеките, от които имаме нужда, ще ни трябват препратки към клиент и към избрания протокол за трансфер, stdio. stdio е протокол за неща, които са предназначени да се стартират на локалната ви машина. SSE е друг протокол за трансфер, който ще демонстрираме в бъдещи глави, но това е вашата друга опция. За сега обаче, нека продължим със stdio.

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

За Java, ще създадете клиент, който се свързва със MCP сървъра от предходното упражнение. Използвайки същата структура на проект Java Spring Boot от [Започване с MCP сървър](../../../../03-GettingStarted/01-first-server/solution/java), създайте нов Java клас на име `SDKClient` във папката `src/main/java/com/microsoft/mcp/sample/client/` и добавете следните импорти:

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

Ще трябва да добавите следните зависимости във файла `Cargo.toml`.

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

Оттам можете да импортирате необходимите библиотеки във вашия клиентски код.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Нека преминем към създаване на инстанции.

### -2- Създаване на клиент и транспортни инстанции

Ще трябва да създадем екземпляр на транспорта и на клиента:

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

В предходния код ние:

- Създадохме stdio транспортен екземпляр. Забележете как се задава команда и аргументи за намиране и стартиране на сървъра, тъй като това е нещо, което ще трябва да направим при създаване на клиента.

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

# Създайте параметри на сървъра за stdio връзка
server_params = StdioServerParameters(
    command="mcp",  # Изпълним файл
    args=["run", "server.py"],  # Незадължителни аргументи от командния ред
    env=None,  # Незадължителни променливи на средата
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

В предходния код ние:

- Импортирахме нужните библиотеки
- Създадохме обект със сървърни параметри, който ще използваме, за да стартираме сървъра и да можем да се свържем с него от клиента.
- Определихме метод `run`, който от своя страна вика `stdio_client`, който стартира клиентска сесия.
- Създадохме точка за вход, в която подаваме метода `run` на `asyncio.run`.

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

В предходния код ние:

- Импортирахме нужните библиотеки.
- Създадохме stdio транспорт и клиент на име `mcpClient`. Последният ще използваме за изброяване и извикване на функции на MCP сървъра.

Забележка, в "Arguments" можете да посочите или *.csproj* или изпълнимия файл.

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
        
        // Логиката на вашия клиент отива тук
    }
}
```

В предходния код ние:

- Създадохме главен метод, който настройва SSE транспорт, сочещ към `http://localhost:8080`, където ще работи нашият MCP сървър.
- Създадохме клиентски клас, който приема транспорта като параметър на конструктора.
- В метода `run` създаваме синхронен MCP клиент с транспорта и инициализираме връзката.
- Използвахме SSE (Server-Sent Events) транспорт, който е подходящ за комуникация по HTTP с Java Spring Boot MCP сървъри.

#### Rust

Обърнете внимание, че този Rust клиент предполага, че сървърът е сестрински проект на име "calculator-server" в същата директория. Следният код ще стартира сървъра и ще се свърже с него.

```rust
async fn main() -> Result<(), RmcpError> {
    // Приемете, че сървърът е събратски проект на име "calculator-server" в същата директория
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

    // TODO: Списък с инструменти

    // TODO: Извикайте добавяне на инструмент с аргументи = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Изброяване на функциите на сървъра

Сега имаме клиент, който може да се свърже, ако програмата бъде стартирана. Въпреки това, той всъщност не изброява функциите си, така че нека го направим сега:

#### TypeScript

```typescript
// Списък с подканващи изрази
const prompts = await client.listPrompts();

// Списък с ресурси
const resources = await client.listResources();

// списък с инструменти
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

Тук изброяваме наличните ресурси чрез `list_resources()` и инструменти с `list_tools` и ги отпечатваме.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

По-горе е пример как можем да изброим инструментите на сървъра. За всеки инструмент после печатаме името му.

#### Java

```java
// Избройте и демонстрирайте инструменти
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Можете също да пингнете сървъра, за да проверите връзката
client.ping();
```

В предходния код ние:

- Извикахме `listTools()` за получаване на всички налични инструменти от MCP сървъра.
- Използвахме `ping()` за проверка дали връзката със сървъра работи.
- `ListToolsResult` съдържа информация за всички инструменти, включително техните имена, описания и схеми на вход.

Отлично, сега сме уловили всички функции. Сега въпросът е кога да ги използваме? Този клиент е доста прост, прост в смисъл, че трябва изрично да викаме функциите, когато искаме. В следващата глава ще създадем по-усъвършенстван клиент с достъп до собствен голям езиков модел, LLM. За сега обаче нека видим как да извикаме функциите на сървъра:

#### Rust

В главната функция, след инициализация на клиента, можем да инициализираме сървъра и да изброим някои от функциите му.

```rust
// Инициализиране
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Изброяване на инструментите
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Извикване на функции

За да извикаме функциите, трябва да сме сигурни, че задаваме правилните аргументи и в някои случаи името на това, което искаме да извикаме.

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

// извикайте подсказка
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

В предходния код ние:

- Четем ресурс, като го извикваме чрез `readResource()` задавайки `uri`. Ето как вероятно изглежда на сървърната страна:

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

    Нашата стойност `uri` `file://example.txt` съвпада с `file://{name}` на сървъра. `example.txt` ще се съпостави на `name`.

- Извикваме инструмент, като задаваме неговото `name` и `arguments`, както следва:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Вземаме подсказка, за да вземем подсказка, извикваме `getPrompt()` с `name` и `arguments`. Кодът на сървъра изглежда така:

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

    и вашият клиентски код следователно изглежда така, за да съответства на това, което е декларирано на сървъра:

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

В предходния код ние:

- Извикахме ресурс, наречен `greeting` използвайки `read_resource`.
- Извикахме инструмент, наречен `add` чрез `call_tool`.

#### .NET

1. Да добавим някакъв код за извикване на инструмент:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. За да отпечатаме резултата, ето код за това:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Извикване на различни калкулаторни инструменти
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

В предходния код ние:

- Извикахме няколко инструмента на калкулатора с метода `callTool()` и обекти `CallToolRequest`.
- Всяко повикване задава името на инструмента и `Map` от аргументи, необходими на инструмента.
- Инструментите на сървъра очакват специфични имена на параметри (като "a", "b" за математически операции).
- Резултатите се връщат като обекти `CallToolResult`, съдържащи отговора от сървъра.

#### Rust

```rust
// Извикайте инструмента за събиране с аргументи = {"a": 3, "b": 2}
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

Стартирайте клиента с командата:

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
# Изградете вашия проект
./mvnw clean compile

# Стартирайте клиента
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Алтернативно, можете да стартирате пълния клиентски проект, предоставен във папката с решение `03-GettingStarted\02-client\solution\java`:

```bash
# Навигирайте до директорията на решението
cd 03-GettingStarted/02-client/solution/java

# Изградете и стартирайте JAR файла
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Задача

В тази задача ще използвате наученото, за да създадете собствен клиент.

Ето един сървър, който можете да използвате и който трябва да извиквате чрез клиентския си код, вижте дали можете да добавите повече функции на сървъра, за да стане по-интересен.

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

// Започнете да получавате съобщения на stdin и да изпращате съобщения на stdout

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


# Добавете динамичен ресурс за поздравление
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

Вижте този проект, за да видите как можете да [добавяте подсказки и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Също така, проверете тази връзка за това как да извиквате [подсказки и ресурси](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

В [предходния раздел](../../../../03-GettingStarted/01-first-server) научихте как да създадете прост MCP сървър с Rust. Можете да продължите да надграждате това или да проверите тази връзка за още примери на MCP сървъри на Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Решение

**Папката с решение** съдържа пълни, готови за стартиране клиентски имплементации, които демонстрират всички концепции, разгледани в този урок. Всяко решение включва както клиентски, така и сървърни кодове, организирани в отделни, самостоятелни проекти.

### 📁 Структура на решението

Директорията на решението е организирана по програмни езици:

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

Всяко решение по конкретен език предоставя:

- **Пълна клиентска имплементация** със всички функции от урока
- **Работна структура на проекта** с правилни зависимости и настройки
- **Скриптове за билд и стартиране** за лесна настройка и изпълнение
- **Подробно README** с инструкции, специфични за езика
- **Обработка на грешки** и примери за обработка на резултати

### 📖 Използване на решенията

1. **Навигирайте до папката с предпочитания от вас език**:

   ```bash
   cd solution/typescript/    # За TypeScript
   cd solution/java/          # За Java
   cd solution/python/        # За Python
   cd solution/dotnet/        # За .NET
   ```

2. **Следвайте инструкциите в README файла** във всяка папка за:
   - Инсталиране на зависимости
   - Създаване на проекта
   - Стартиране на клиента

3. **Примерен изход**, който би трябвало да видите:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

За пълна документация и стъпка по стъпка инструкции, вижте: **[📖 Документация на решението](./solution/README.md)**

## 🎯 Пълни примери

Предоставихме пълни, работещи клиентски имплементации за всички езици, обхванати в този урок. Тези примери демонстрират пълната функционалност описана по-горе и могат да се използват като референтни имплементации или отправни точки за вашите собствени проекти.

### Налични пълни примери

| Език | Файл | Описание |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Пълен Java клиент с SSE транспорт и комплексна обработка на грешки |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Пълен C# клиент с stdio транспорт и автоматично стартиране на сървъра |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Пълен TypeScript клиент с пълна поддръжка на MCP протокола |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Пълен Python клиент с async/await шаблони |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Пълен Rust клиент с Tokio за асинхронни операции |

Всяко пълно решение включва:

- ✅ **Установяване на връзка** и обработка на грешки
- ✅ **Откриване на сървъра** (инструменти, ресурси, подсказки където е приложимо)
- ✅ **Операции на калкулатор** (събиране, изваждане, умножение, деление, помощ)
- ✅ **Обработка на резултати** и форматиран изход
- ✅ **Комплексна обработка на грешки**

- ✅ **Чист, документиран код** със стъпка по стъпка коментари

### Първи стъпки с пълни примери

1. **Изберете предпочитания език** от таблицата по-горе
2. **Прегледайте пълния примерен файл** за да разберете цялата реализация
3. **Стартирайте примера** като следвате инструкциите в [`complete_examples.md`](./complete_examples.md)
4. **Модифицирайте и разширете** примера за вашия конкретен случай

За подробна документация относно стартирането и персонализирането на тези примери вижте: **[📖 Документация за пълните примери](./complete_examples.md)**

### 💡 Решение срещу пълни примери

| **Папка с решение** | **Пълни примери** |
|--------------------|--------------------- |
| Пълна структура на проекта с файлове за билд | Имплементации в един файл |
| Готови за стартиране с зависимости | Фокусирани кодови примери |
| Околна среда близка до продукционна | Образователен справочник |
| Инструменти специфични за езика | Сравнение между езици |

И двата подхода са ценни - използвайте **папката с решение** за цели проекти и **пълните примери** за учене и справка.

## Основни изводи

Основните изводи за тази глава относно клиентите са следните:

- Могат да се използват както за откриване, така и за извикване на функции на сървъра.
- Могат да стартират сървър докато той сам стартира (както в тази глава), но клиентите могат да се свързват и към вече работещи сървъри.
- Отличен начин за тестване на възможностите на сървъра в сравнение с алтернативи като Inspector, както беше описано в предишната глава.

## Допълнителни ресурси

- [Създаване на клиенти в MCP](https://modelcontextprotocol.io/quickstart/client)

## Примери

- [Java Калькулатор](../samples/java/calculator/README.md)
- [.NET Калькулатор](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Калькулатор](../samples/javascript/README.md)
- [TypeScript Калькулатор](../samples/typescript/README.md)
- [Python Калькулатор](../../../../03-GettingStarted/samples/python)
- [Rust Калькулатор](../../../../03-GettingStarted/samples/rust)

## Какво следва

- Следващо: [Създаване на клиент с LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
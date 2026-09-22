# Skapa en klient

Klienter är anpassade applikationer eller skript som kommunicerar direkt med en MCP-server för att begära resurser, verktyg och prompts. Till skillnad från att använda inspektörsverktyget som ger ett grafiskt gränssnitt för serverinteraktion, möjliggör det att skriva en egen klient programmatisk och automatiserad interaktion. Detta gör det möjligt för utvecklare att integrera MCP-funktioner i sina egna arbetsflöden, automatisera uppgifter och bygga anpassade lösningar för specifika behov.

## Översikt

Den här lektionen introducerar konceptet klienter inom Model Context Protocol (MCP)-ekosystemet. Du kommer att lära dig hur man skriver en egen klient och får den att ansluta till en MCP-server.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Förstå vad en klient kan göra.
- Skriva din egen klient.
- Ansluta och testa klienten med en MCP-server för att säkerställa att den fungerar som förväntat.

## Vad krävs för att skriva en klient?

För att skriva en klient behöver du göra följande:

- **Importera rätt bibliotek**. Du kommer använda samma bibliotek som tidigare, bara olika konstruktioner.
- **Instansiera en klient**. Detta innebär att skapa en klientinstans och ansluta den till vald transportmetod.
- **Bestäm vilka resurser som ska listas**. Din MCP-server har resurser, verktyg och prompts; du behöver bestämma vilka som ska listas.
- **Integrera klienten i en värdapplikation**. När du vet serverns funktionalitet behöver du integrera detta i värdapplikationen så att om en användare skriver en prompt eller annat kommando anropas motsvarande serverfunktion.

Nu när vi på en övergripande nivå förstår vad vi ska göra, låt oss titta på ett exempel nästa.

### Ett exempel på en klient

Låt oss titta på detta exempel på en klient:

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

// Lista uppmaningar
const prompts = await client.listPrompts();

// Hämta en uppmaning
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Lista resurser
const resources = await client.listResources();

// Läs en resurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Anropa ett verktyg
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

I den föregående koden:

- Importerar vi biblioteken
- Skapar en klientinstans och ansluter till servern via stdio-transport.
- Listar prompts, resurser och verktyg och anropar alla.

Där har du det, en klient som kan kommunicera med en MCP-server.

Låt oss ta god tid på oss i nästa övningsavsnitt och bryta ner varje kodsnutt och förklara vad som händer.

## Övning: Skriva en klient

Som sagt ovan, låt oss ta tid att förklara koden, och koda gärna med om du vill.

### -1- Importera biblioteken

Vi importerar de bibliotek vi behöver, vi behöver referenser till en klient och till vår valda transportprotokoll, stdio. stdio är ett protokoll för saker som ska köras lokalt på din maskin. SSE är ett annat transportprotokoll som vi visar i framtida kapitel, men för nu fortsätter vi med stdio.

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

För Java skapar du en klient som ansluter till MCP-servern från föregående övning. Med samma Java Spring Boot-projektsstruktur från [Komma igång med MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), skapa en ny Java-klass kallad `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` och lägg till följande imports:

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

Du behöver lägga till följande beroenden i din `Cargo.toml`-fil.

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

Därefter kan du importera nödvändiga bibliotek i din klientkod.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Låt oss gå vidare till instansiering.

### -2- Instansiera klient och transport

Vi behöver skapa en instans av transporten och av vår klient:

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

I den föregående koden har vi:

- Skapat en stdio-transportinstans. Notera hur den specificerar kommando och argument för hur man hittar och startar servern, vilket vi kommer behöva när vi skapar klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instansierat en klient genom att ge den namn och version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Anslutit klienten till vald transport.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Skapa serverparametrar för stdio-anslutning
server_params = StdioServerParameters(
    command="mcp",  # Körbar fil
    args=["run", "server.py"],  # Valfria kommandoradsargument
    env=None,  # Valfria miljövariabler
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initiera anslutningen
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

I den föregående koden har vi:

- Importerat nödvändiga bibliotek
- Instansierat ett serverparametrar-objekt som vi använder för att köra servern så vi kan ansluta till den med vår klient.
- Definierat en metod `run` som i sin tur anropar `stdio_client` som startar en klientsession.
- Skapat en ingångspunkt där vi skickar `run`-metoden till `asyncio.run`.

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

I den föregående koden har vi:

- Importerat nödvändiga bibliotek.
- Skapat en stdio-transport och skapat en klient `mcpClient`. Den senare används för att lista och anropa funktioner på MCP-servern.

Observera att i "Arguments" kan du antingen peka på *.csproj* eller till den körbara filen.

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
        
        // Din klientlogik går här
    }
}
```

I den föregående koden har vi:

- Skapat en main-metod som konfigurerar en SSE-transport som pekar på `http://localhost:8080` där vår MCP-server körs.
- Skapat en klientklass som tar transporten som konstruktörsparameter.
- I `run`-metoden skapar vi en synkron MCP-klient med transporten och initierar anslutningen.
- Använt SSE (Server-Sent Events) transport som passar för HTTP-baserad kommunikation med Java Spring Boot MCP-servrar.

#### Rust

Observera att denna Rust-klient förutsätter att servern är ett syskonprojekt kallat "calculator-server" i samma katalog. Koden nedan startar servern och ansluter till den.

```rust
async fn main() -> Result<(), RmcpError> {
    // Anta att servern är ett syskonprojekt som heter "calculator-server" i samma katalog
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

    // TODO: Initialisera

    // TODO: Lista verktyg

    // TODO: Anropa lägg till verktyg med argument = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Lista serverfunktioner

Nu har vi en klient som kan ansluta om programmet körs. Dock listar den inte sina funktioner än, så låt oss göra det:

#### TypeScript

```typescript
// Lista uppmaningar
const prompts = await client.listPrompts();

// Lista resurser
const resources = await client.listResources();

// lista verktyg
const tools = await client.listTools();
```

#### Python

```python
# Lista tillgängliga resurser
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Lista tillgängliga verktyg
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Här listar vi tillgängliga resurser, `list_resources()` och verktyg, `list_tools` och skriver ut dem.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ovan är ett exempel på hur vi kan lista verktygen på servern. För varje verktyg skriver vi sedan ut namnet.

#### Java

```java
// Lista och demonstrera verktyg
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Du kan också pinga servern för att verifiera anslutningen
client.ping();
```

I den föregående koden har vi:

- Anropat `listTools()` för att hämta alla tillgängliga verktyg från MCP-servern.
- Använt `ping()` för att verifiera att anslutningen till servern fungerar.
- `ListToolsResult` innehåller information om alla verktyg inklusive namn, beskrivningar och indata-schema.

Utmärkt, nu har vi fångat alla funktioner. Frågan är när använder vi dem? Denna klient är ganska enkel, i den meningen att vi måste anropa funktionerna explicit när vi vill ha dem. I nästa kapitel skapar vi en mer avancerad klient med tillgång till egen stor språkmodell, LLM. För nu ska vi se hur vi anropar funktionerna på servern:

#### Rust

I main-funktionen, efter att klienten initierats, kan vi initiera servern och lista några av dess funktioner.

```rust
// Initiera
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Lista verktyg
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Anropa funktioner

För att anropa funktionerna behöver vi säkerställa att rätt argument anges och i vissa fall namnet på det vi försöker anropa.

#### TypeScript

```typescript

// Läs en resurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Anropa ett verktyg
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// anropa prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

I den föregående koden:

- Läser vi en resurs, vi anropar resursen med `readResource()` genom att specificera `uri`. Så här ser det troligen ut på serversidan:

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

    Vårt `uri`-värde `file://example.txt` matchar `file://{name}` på servern. `example.txt` mappas till `name`.

- Anropar ett verktyg genom att specificera dess `name` och dess `arguments` så här:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Hämtar prompt, för att få en prompt anropas `getPrompt()` med `name` och `arguments`. Serverkoden ser ut så här:

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

    och resultatet i klientkoden ser därför ut så här för att matcha vad som deklarerats på servern:

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
# Läs en resurs
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Anropa ett verktyg
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

I den föregående koden har vi:

- Anropat en resurs kallad `greeting` med `read_resource`.
- Anropat ett verktyg kallat `add` med `call_tool`.

#### .NET

1. Låt oss lägga till kod för att anropa ett verktyg:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. För att skriva ut resultatet, här är kod som hanterar det:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Anropa olika kalkylatorverktyg
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

I den föregående koden har vi:

- Anropat flera kalkylatorverktyg med `callTool()`-metoden med `CallToolRequest`-objekt.
- Varje verktygsanrop specificerar verktygets namn och en `Map` med argument som krävs av verktyget.
- Serververktygen förväntar sig specifika parameter-namn (som "a", "b" för matematiska operationer).
- Resultaten returneras som `CallToolResult`-objekt som innehåller svar från servern.

#### Rust

```rust
// Anropa verktyg add med argument = {"a": 3, "b": 2}
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

### -5- Kör klienten

För att köra klienten, skriv följande kommando i terminalen:

#### TypeScript

Lägg till följande post i "scripts"-sektionen i *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kör klienten med följande kommando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Först, se till att din MCP-server körs på `http://localhost:8080`. Kör sedan klienten:

```bash
# Bygg ditt projekt
./mvnw clean compile

# Kör klienten
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du köra hela klientprojektet som finns i mappen `03-GettingStarted\02-client\solution\java`:

```bash
# Navigera till lösningskatalogen
cd 03-GettingStarted/02-client/solution/java

# Bygg och kör JAR-filen
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Uppgift

I denna uppgift använder du det du lärt dig om att skapa en klient men skapar din egen klient.

Här är en server du kan använda som du behöver anropa via din klientkod, se om du kan lägga till fler funktioner i servern för att göra den mer intressant.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Skapa en MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Lägg till ett additionsverktyg
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lägg till en dynamisk hälsningsresurs
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

// Börja ta emot meddelanden på stdin och skicka meddelanden på stdout

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

# Skapa en MCP-server
mcp = FastMCP("Demo")


# Lägg till ett additionsverktyg
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lägg till en dynamisk hälsningsresurs
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

Se detta projekt för att se hur du kan [lägga till prompts och resurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Kolla också denna länk för hur du anropar [prompts och resurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [föregående avsnitt](../../../../03-GettingStarted/01-first-server) lärde du dig skapa en enkel MCP-server med Rust. Du kan fortsätta bygga på det eller kolla denna länk för fler Rust-baserade MCP-serverexempel: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lösning

**lösningsmappen** innehåller kompletta, körbara klientimplementeringar som demonstrerar alla koncept som behandlats i denna handledning. Varje lösning innehåller både klient- och serverkod organiserad i separata, självständiga projekt.

### 📁 Lösningsstruktur

Lösningskatalogen är organiserad efter programmeringsspråk:

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

### 🚀 Vad varje lösning inkluderar

Varje språkspecifik lösning innehåller:

- **Fullständig klientimplementering** med alla funktioner från handledningen
- **Fungerande projektstruktur** med ordnade beroenden och konfiguration
- **Bygg- och kör-skript** för enkel setup och körning
- **Detaljerad README** med språk-specifika instruktioner
- **Felhantering** och exempel på resultatbearbetning

### 📖 Använda lösningarna

1. **Navigera till din föredragna språkmapp**:

   ```bash
   cd solution/typescript/    # För TypeScript
   cd solution/java/          # För Java
   cd solution/python/        # För Python
   cd solution/dotnet/        # För .NET
   ```

2. **Följ README-instruktionerna** i varje mapp för:
   - Installera beroenden
   - Bygga projektet
   - Köra klienten

3. **Exempelutdata** som du bör se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

För fullständig dokumentation och steg-för-steg-instruktioner, se: **[📖 Lösningsdokumentation](./solution/README.md)**

## 🎯 Kompletta exempel

Vi har tillhandahållit kompletta, fungerande klientimplementeringar för alla programmeringsspråk som täcks i denna handledning. Dessa exempel demonstrerar full funktionalitet som beskrivits ovan och kan användas som referensimplementationer eller utgångspunkter för dina egna projekt.

### Tillgängliga kompletta exempel

| Språk | Fil | Beskrivning |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Komplett Java-klient som använder SSE-transport med omfattande felhantering |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Komplett C#-klient som använder stdio-transport med automatisk serverstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplett TypeScript-klient med full MCP-protokollsupport |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Komplett Python-klient som använder async/await-mönster |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Komplett Rust-klient som använder Tokio för asynkrona operationer |

Varje komplett exempel innehåller:

- ✅ **Etablering av anslutning** och felhantering
- ✅ **Serverupptäckt** (verktyg, resurser, prompts där tillämpligt)
- ✅ **Kalkylatoroperationer** (addera, subtrahera, multiplicera, dividera, hjälp)
- ✅ **Resultatbearbetning** och formaterad utskrift
- ✅ **Omfattande felhantering**

- ✅ **Ren, dokumenterad kod** med steg-för-steg-kommentarer

### Komma igång med fullständiga exempel

1. **Välj ditt föredragna språk** från tabellen ovan
2. **Granska den fullständiga exempelfilen** för att förstå hela implementeringen
3. **Kör exemplet** enligt instruktionerna i [`complete_examples.md`](./complete_examples.md)
4. **Modifiera och utöka** exemplet för ditt specifika användningsfall

För detaljerad dokumentation om att köra och anpassa dessa exempel, se: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 Lösning vs. fullständiga exempel

| **Lösningsmapp** | **Fullständiga exempel** |
|-----------------|-------------------------|
| Fullständig projektstruktur med byggfiler | Enkel-fil-implementationer |
| Klara att köra med beroenden | Fokuserade kodexempel |
| Produktionsliknande uppsättning | Pedagogisk referens |
| Språkspecifika verktyg | Jämförelse mellan språk |

Båda tillvägagångssätten är värdefulla - använd **lösningsmappen** för kompletta projekt och **fullständiga exempel** för lärande och referens.

## Viktiga punkter att ta med sig

De viktigaste punkterna för detta kapitel om klienter är följande:

- Kan användas både för att upptäcka och anropa funktioner på servern.
- Kan starta en server medan den själv startar (som i detta kapitel) men klienter kan också ansluta till redan körande servrar.
- Är ett utmärkt sätt att testa serverfunktionalitet jämfört med alternativ som Inspector, vilket beskrevs i föregående kapitel.

## Ytterligare resurser

- [Bygga klienter i MCP](https://modelcontextprotocol.io/quickstart/client)

## Exempel

- [Java Kalkylator](../samples/java/calculator/README.md)
- [.NET Kalkylator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkylator](../samples/javascript/README.md)
- [TypeScript Kalkylator](../samples/typescript/README.md)
- [Python Kalkylator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkylator](../../../../03-GettingStarted/samples/rust)

## Vad händer härnäst

- Nästa: [Skapa en klient med en LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
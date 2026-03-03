# Skapa en klient

Klienter är anpassade applikationer eller skript som kommunicerar direkt med en MCP-server för att begära resurser, verktyg och prompts. Till skillnad från att använda inspektörsverktyget, som tillhandahåller ett grafiskt gränssnitt för att interagera med servern, möjliggör att skriva din egen klient programmatisk och automatiserad interaktion. Detta gör det möjligt för utvecklare att integrera MCP-funktioner i sina egna arbetsflöden, automatisera uppgifter och bygga egna lösningar anpassade efter specifika behov.

## Översikt

Den här lektionen introducerar begreppet klienter inom Model Context Protocol (MCP) ekosystemet. Du kommer att lära dig hur du skriver din egen klient och får den att ansluta till en MCP-server.

## Inlärningsmål

I slutet av denna lektion kommer du att kunna:

- Förstå vad en klient kan göra.
- Skriva din egen klient.
- Ansluta och testa klienten med en MCP-server för att säkerställa att den fungerar som förväntat.

## Vad ingår i att skriva en klient?

För att skriva en klient behöver du göra följande:

- **Importera rätt bibliotek**. Du kommer att använda samma bibliotek som tidigare, bara olika konstruktioner.
- **Skapa en klientinstans**. Detta innebär att skapa en klientinstans och koppla den till den valda transportmetoden.
- **Bestämma vilka resurser som ska listas**. Din MCP-server kommer med resurser, verktyg och prompts, du måste besluta vilka som ska listas.
- **Integrera klienten i en värdapplikation**. När du känner till serverns funktioner behöver du integrera detta i din värdapplikation så att om en användare skriver en prompt eller annan kommando anropas motsvarande serverfunktion.

Nu när vi på hög nivå förstår vad vi ska göra, låt oss titta på ett exempel.

### Ett exempel på klient

Låt oss titta på detta exempel på klient:

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
- Skapar en instans av en klient och kopplar den med stdio som transportmetod.
- Listar prompts, resurser och verktyg och anropar dem alla.

Där har du det, en klient som kan kommunicera med en MCP-server.

Låt oss ta det lugnt i nästa övningsavsnitt och bryta ned varje kodsnutt och förklara vad som händer.

## Övning: Skriva en klient

Som sagt ovan, låt oss ta tiden att förklara koden, och koda gärna med om du vill.

### -1- Importera biblioteken

Låt oss importera de bibliotek vi behöver; vi behöver referenser till en klient och vår valda transportprotokoll, stdio. stdio är ett protokoll för saker som körs lokalt på din maskin. SSE är ett annat transportprotokoll som vi visar i framtida kapitel men det är ditt andra alternativ. För nu, låt oss fortsätta med stdio.

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

För Java, skapar du en klient som ansluter till MCP-servern från föregående övning. Använd samma Java Spring Boot projektstruktur från [Kom igång med MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), skapa en ny Java-klass kallad `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` och lägg till följande imports:

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

Därifrån kan du importera de nödvändiga biblioteken i din klientkod.

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

Vi behöver skapa en instans av transporten och en av vår klient:

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

- Skapat en stdio-transportinstans. Notera hur den specificerar kommando och argument för hur servern ska startas—det är något vi behöver göra när vi skapar klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instansierat en klient genom att ge den ett namn och en version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Anslutit klienten till den valda transporten.

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
            # Initialisera anslutningen
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

I den föregående koden har vi:

- Importerat nödvändiga bibliotek
- Instansierat ett serverparametrar-objekt, eftersom vi kommer använda detta för att köra servern så vi kan ansluta till den med vår klient.
- Definierat en metod `run` som i sin tur anropar `stdio_client` som startar en klient-session.
- Skapat en startpunkt där vi ger `run`-metoden till `asyncio.run`.

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
- Skapat en stdio-transport och en klient `mcpClient`. Den sistnämnda är vad vi ska använda för att lista och anropa funktioner på MCP-servern.

Observera att i “Arguments” kan du antingen peka på *.csproj* eller på körbar fil.

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

- Skapat en main-metod som sätter upp en SSE-transport pekande på `http://localhost:8080` där vår MCP-server körs.
- Skapat en klientklass som tar transporten som konstruktorns parameter.
- I `run`-metoden skapar vi en synkron MCP-klient med transporten och initierar anslutningen.
- Använt SSE (Server-Sent Events) transport som är lämplig för HTTP-baserad kommunikation med Java Spring Boot MCP-servrar.

#### Rust

Observera att denna Rust-klient antar att servern är ett syskonprojekt som heter "calculator-server" i samma katalog. Koden nedan startar servern och ansluter till den.

```rust
async fn main() -> Result<(), RmcpError> {
    // Anta att servern är ett syskonprojekt med namnet "calculator-server" i samma katalog
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

### -3- Lista serverns funktioner

Nu har vi en klient som kan ansluta när programmet körs. Dock listar den inte funktionerna, så låt oss göra det nu:

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

Ovan är ett exempel på hur vi kan lista serverns verktyg. För varje verktyg skriver vi sedan ut dess namn.

#### Java

```java
// Lista och demonstrera verktyg
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Du kan också pinga servern för att verifiera anslutning
client.ping();
```

I den föregående koden har vi:

- Anropat `listTools()` för att hämta alla tillgängliga verktyg från MCP-servern.
- Använt `ping()` för att verifiera att anslutningen till servern fungerar.
- `ListToolsResult` innehåller information om alla verktyg inklusive deras namn, beskrivningar och inmatningsscheman.

Bra, nu har vi fångat alla funktioner. Nu är frågan när använder vi dem? Denna klient är ganska enkel, enkel i den meningen att vi måste anropa funktionerna explicit när vi vill ha dem. I nästa kapitel skapar vi en mer avancerad klient som har tillgång till sin egen stora språkmodell, LLM. För nu, låt oss se hur vi kan anropa funktionerna på servern:

#### Rust

I main-funktionen, efter klienten initierats, kan vi initiera servern och lista några av dess funktioner.

```rust
// Initiera
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Lista verktyg
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Anropa funktioner

För att anropa funktionerna måste vi säkerställa att rätt argument specificeras och i vissa fall namnet på det vi försöker anropa.

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

- Läser vi en resurs genom att anropa `readResource()` med `uri`. Såhär ser det troligen ut på serversidan:

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

    Värdet för `uri` `file://example.txt` matchar `file://{name}` på servern. `example.txt` mappas till `name`.

- Anropar ett verktyg genom att specificera dess `name` och dess `arguments` så här:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Hämtar en prompt, för att hämta en prompt anropar du `getPrompt()` med `name` och `arguments`. Serverkoden ser ut så här:

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

    och din klientkod blir därför så här för att matcha vad som deklarerats på servern:

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

- Anropat ett resursverktyg som heter `greeting` med `read_resource`.
- Anropat ett verktyg som heter `add` med `call_tool`.

#### .NET

1. Låt oss lägga till kod för att anropa ett verktyg:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. För att skriva ut resultatet, här är kod för det:

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

- Anropat flera kalkylatorverktyg med metoden `callTool()` med `CallToolRequest`-objekt.
- Varje verktygsanrop specificerar verktygets namn och en `Map` med argument som krävs.
- Serververktygen förväntar sig specifika parameter-namn (som "a", "b" för matematiska operationer).
- Resultaten returneras som `CallToolResult`-objekt med serverns svar.

#### Rust

```rust
// Anropa add-verktyget med argumenten = {"a": 3, "b": 2}
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

Lägg till följande post i din "scripts"-sektion i *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Anropa klienten med följande kommando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Se först till att din MCP-server körs på `http://localhost:8080`. Kör sedan klienten:

```bash
# Bygg ditt projekt
./mvnw clean compile

# Kör klienten
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du köra hela klientprojektet som finns i lösningsmappen `03-GettingStarted\02-client\solution\java`:

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

I denna uppgift använder du vad du lärt dig om att skapa en klient men skapar en egen klient.

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

// Lägg till ett tilläggsverktyg
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


# Lägg till ett tilläggsverktyg
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

Kolla också denna länk för hur man anropar [prompts och resurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [föregående avsnitt](../../../../03-GettingStarted/01-first-server) lärde du dig hur du skapar en enkel MCP-server med Rust. Du kan fortsätta bygga på det eller titta på denna länk för fler Rust-baserade MCP-serverexempel: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lösning

**Lösningsmappen** innehåller kompletta och färdiga klientimplementationer som visar alla koncept som täcks i denna handledning. Varje lösning inkluderar både klient- och serverkod organiserade i separata, självständiga projekt.

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

### 🚀 Vad varje lösning innehåller

Varje språk-specifik lösning erbjuder:

- **Fullständig klientimplementation** med alla funktioner från handledningen
- **Fungerande projektstruktur** med rätt beroenden och konfiguration
- **Bygg- och körskript** för enkel installation och körning
- **Detaljerad README** med språk-specifika instruktioner
- **Exempel på felhantering** och resultathantering

### 📖 Använda lösningarna

1. **Navigera till din föredragna språk-mapp**:

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

3. **Exempel på utdata** du bör se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

För fullständig dokumentation och steg-för-steg-instruktioner, se: **[📖 Lösningsdokumentation](./solution/README.md)**

## 🎯 Kompletta exempel

Vi har tillhandahållit kompletta, fungerande klientimplementationer för alla programmeringsspråk som täcks i denna handledning. Dessa exempel visar den fulla funktionaliteten beskriven ovan och kan användas som referensimplementationer eller startpunkter för dina egna projekt.

### Tillgängliga kompletta exempel

| Språk   | Fil                              | Beskrivning                                                         |
|---------|---------------------------------|--------------------------------------------------------------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | Komplett Java-klient med SSE-transport och omfattande felhantering |
| **C#**      | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | Komplett C#-klient med stdio-transport och automatisk serverstart  |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplett TypeScript-klient med full MCP-protokollsupport           |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)       | Komplett Python-klient med async/await-mönster                     |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | Komplett Rust-klient som använder Tokio för asynkrona operationer  |

Varje komplett exempel inkluderar:
- ✅ **Anslutningsupprättelse** och felhantering
- ✅ **Serverupptäckt** (verktyg, resurser, prompts där tillämpligt)
- ✅ **Kalkylatoroperationer** (lägg till, subtrahera, multiplicera, dividera, hjälp)
- ✅ **Resultatbehandling** och formaterad utdata
- ✅ **Omfattande felhantering**
- ✅ **Ren, dokumenterad kod** med steg-för-steg-kommentarer

### Kom igång med kompletta exempel

1. **Välj ditt föredragna språk** från tabellen ovan
2. **Granska den kompletta exempel-filen** för att förstå hela implementeringen
3. **Kör exemplet** enligt instruktionerna i [`complete_examples.md`](./complete_examples.md)
4. **Modifiera och utöka** exemplet för ditt specifika användningsfall

För detaljerad dokumentation om hur man kör och anpassar dessa exempel, se: **[📖 Komplett exempel-dokumentation](./complete_examples.md)**

### 💡 Lösning vs. kompletta exempel

| **Lösningsmapp** | **Kompletta exempel** |
|------------------|-----------------------|
| Full projektstruktur med byggfiler | Implementeringar i en fil |
| Färdig att köra med beroenden | Fokuserade kodexempel |
| Produktionslik setup | Pedagogisk referens |
| Språkspecifika verktyg | Jämförelse mellan språk |

Båda tillvägagångssätten är värdefulla - använd **lösningsmappen** för kompletta projekt och **kompletta exempel** för lärande och referens.

## Viktiga slutsatser

De viktigaste slutsatserna för detta kapitel vad gäller klienter är följande:

- Kan användas både för att upptäcka och anropa funktioner på servern.
- Kan starta en server samtidigt som den startar sig själv (som i detta kapitel) men klienter kan också ansluta till redan körande servrar.
- Är ett bra sätt att testa serverfunktioner bredvid andra alternativ som Inspector, som beskrevs i föregående kapitel.

## Ytterligare resurser

- [Bygga klienter i MCP](https://modelcontextprotocol.io/quickstart/client)

## Exempel

- [Java-kalkylator](../samples/java/calculator/README.md)
- [.Net-kalkylator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-kalkylator](../samples/javascript/README.md)
- [TypeScript-kalkylator](../samples/typescript/README.md)
- [Python-kalkylator](../../../../03-GettingStarted/samples/python)
- [Rust-kalkylator](../../../../03-GettingStarted/samples/rust)

## Vad händer härnäst

- Nästa: [Skapa en klient med en LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungsspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
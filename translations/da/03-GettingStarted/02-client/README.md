# Oprettelse af en klient

Klienter er skræddersyede applikationer eller scripts, der kommunikerer direkte med en MCP-server for at anmode om ressourcer, værktøjer og prompts. I modsætning til inspektørværktøjet, som giver en grafisk grænseflade til at interagere med serveren, giver det at skrive sin egen klient mulighed for programmatiske og automatiserede interaktioner. Dette gør det muligt for udviklere at integrere MCP-funktioner i deres egne arbejdsgange, automatisere opgaver og bygge skræddersyede løsninger til specifikke behov.

## Oversigt

Denne lektion introducerer konceptet med klienter inden for Model Context Protocol (MCP)-økosystemet. Du vil lære, hvordan du skriver din egen klient og forbinder den til en MCP-server.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Forstå, hvad en klient kan gøre.
- Skrive din egen klient.
- Forbinde og teste klienten med en MCP-server for at sikre, at den fungerer som forventet.

## Hvad kræves for at skrive en klient?

For at skrive en klient skal du gøre følgende:

- **Importere de korrekte biblioteker**. Du vil bruge det samme bibliotek som før, men med forskellige konstruktioner.
- **Oprette en klientinstans**. Dette indebærer at oprette en klientinstans og forbinde den til den valgte transportmetode.
- **Beslutte, hvilke ressourcer der skal listes**. Din MCP-server leverer ressourcer, værktøjer og prompts, og du skal beslutte, hvilke der skal listes.
- **Integrere klienten i en værtapplikation**. Når du kender serverens funktioner, skal du integrere dette i din værtapplikation, så hvis en bruger indtaster en prompt eller en anden kommando, aktiveres den tilsvarende serverfunktion.

Nu hvor vi forstår på et højt niveau, hvad vi skal gøre, lad os se på et eksempel.

### Et eksempel på en klient

Lad os se på dette eksempel på en klient:

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

I den foregående kode:

- Importerer vi bibliotekerne.
- Opretter en instans af en klient og forbinder den ved hjælp af stdio som transport.
- Lister prompts, ressourcer og værktøjer og aktiverer dem alle.

Der har du det, en klient, der kan kommunikere med en MCP-server.

Lad os tage os tid i den næste øvelsessektion og gennemgå hver kodeblok og forklare, hvad der foregår.

## Øvelse: Skrive en klient

Som nævnt ovenfor, lad os tage os tid til at forklare koden, og du er velkommen til at kode med, hvis du vil.

### -1- Importere bibliotekerne

Lad os importere de biblioteker, vi har brug for. Vi skal bruge referencer til en klient og til vores valgte transportprotokol, stdio. stdio er en protokol til ting, der skal køre på din lokale maskine. SSE er en anden transportprotokol, som vi vil vise i fremtidige kapitler, men det er dit andet valg. For nu fortsætter vi dog med stdio.

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

For Java skal du oprette en klient, der forbinder til MCP-serveren fra den tidligere øvelse. Brug den samme Java Spring Boot-projektstruktur fra [Kom godt i gang med MCP-server](../../../../03-GettingStarted/01-first-server/solution/java), opret en ny Java-klasse kaldet `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` og tilføj følgende imports:

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

Du skal tilføje følgende afhængigheder til din `Cargo.toml`-fil.

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

Derfra kan du importere de nødvendige biblioteker i din klientkode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Lad os gå videre til instansiering.

### -2- Instansiering af klient og transport

Vi skal oprette en instans af transporten og en af vores klient:

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

I den foregående kode har vi:

- Oprettet en stdio transportinstans. Bemærk, hvordan den specificerer kommando og argumenter for, hvordan man finder og starter serveren, da det er noget, vi skal gøre, når vi opretter klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instansieret en klient ved at give den et navn og en version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Forbundet klienten til den valgte transport.

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

I den foregående kode har vi:

- Importeret de nødvendige biblioteker.
- Instansieret et serverparameterobjekt, da vi vil bruge dette til at køre serveren, så vi kan forbinde til den med vores klient.
- Defineret en metode `run`, der igen kalder `stdio_client`, som starter en klientsession.
- Oprettet et entry point, hvor vi giver `run`-metoden til `asyncio.run`.

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

I den foregående kode har vi:

- Importeret de nødvendige biblioteker.
- Oprettet en stdio transport og oprettet en klient `mcpClient`. Sidstnævnte er noget, vi vil bruge til at liste og aktivere funktioner på MCP-serveren.

Bemærk, at i "Arguments" kan du enten pege på *.csproj* eller den eksekverbare fil.

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

I den foregående kode har vi:

- Oprettet en main-metode, der opsætter en SSE-transport, der peger på `http://localhost:8080`, hvor vores MCP-server vil køre.
- Oprettet en klientklasse, der tager transporten som en konstruktørparameter.
- I `run`-metoden opretter vi en synkron MCP-klient ved hjælp af transporten og initialiserer forbindelsen.
- Brugte SSE (Server-Sent Events) transport, som er velegnet til HTTP-baseret kommunikation med Java Spring Boot MCP-servere.

#### Rust

Bemærk, at denne Rust-klient antager, at serveren er et søsterprojekt kaldet "calculator-server" i samme mappe. Koden nedenfor starter serveren og forbinder til den.

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

### -3- Liste over serverfunktioner

Nu har vi en klient, der kan forbinde, hvis programmet køres. Den lister dog ikke faktisk sine funktioner, så lad os gøre det næste:

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

Her lister vi de tilgængelige ressourcer, `list_resources()` og værktøjer, `list_tools` og udskriver dem.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ovenfor er et eksempel på, hvordan vi kan liste værktøjerne på serveren. For hvert værktøj udskriver vi derefter dets navn.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

I den foregående kode har vi:

- Kaldt `listTools()` for at få alle tilgængelige værktøjer fra MCP-serveren.
- Brugte `ping()` for at verificere, at forbindelsen til serveren fungerer.
- `ListToolsResult` indeholder information om alle værktøjer, inklusive deres navne, beskrivelser og inputskemaer.

Fremragende, nu har vi fanget alle funktionerne. Spørgsmålet er nu, hvornår vi bruger dem? Denne klient er ret simpel, i den forstand at vi eksplicit skal kalde funktionerne, når vi ønsker dem. I det næste kapitel vil vi oprette en mere avanceret klient, der har adgang til sin egen store sprogmodel, LLM. For nu skal vi dog se, hvordan vi kan aktivere funktionerne på serveren:

#### Rust

I hovedfunktionen, efter at have initialiseret klienten, kan vi initialisere serveren og liste nogle af dens funktioner.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Aktivere funktioner

For at aktivere funktionerne skal vi sikre os, at vi angiver de korrekte argumenter og i nogle tilfælde navnet på det, vi forsøger at aktivere.

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

I den foregående kode:

- Læser vi en ressource ved at kalde `readResource()` og angive `uri`. Her er, hvordan det sandsynligvis ser ud på serversiden:

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

    Vores `uri`-værdi `file://example.txt` matcher `file://{name}` på serveren. `example.txt` vil blive mappet til `name`.

- Kalder et værktøj ved at angive dets `name` og dets `arguments` som følger:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Henter en prompt ved at kalde `getPrompt()` med `name` og `arguments`. Serverkoden ser sådan ud:

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

    Og din resulterende klientkode ser derfor sådan ud for at matche det, der er erklæret på serveren:

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

I den foregående kode har vi:

- Kaldt en ressource kaldet `greeting` ved hjælp af `read_resource`.
- Aktiveret et værktøj kaldet `add` ved hjælp af `call_tool`.

#### .NET

1. Lad os tilføje noget kode for at kalde et værktøj:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. For at udskrive resultatet, her er noget kode til at håndtere det:

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

I den foregående kode har vi:

- Kaldt flere beregningsværktøjer ved hjælp af `callTool()`-metoden med `CallToolRequest`-objekter.
- Hvert værktøjskald specificerer værktøjets navn og et `Map` af argumenter, der kræves af det pågældende værktøj.
- Serverværktøjerne forventer specifikke parameternavne (som "a", "b" til matematiske operationer).
- Resultater returneres som `CallToolResult`-objekter, der indeholder svaret fra serveren.

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

### -5- Kør klienten

For at køre klienten skal du skrive følgende kommando i terminalen:

#### TypeScript

Tilføj følgende post til din "scripts"-sektion i *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kald klienten med følgende kommando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Sørg først for, at din MCP-server kører på `http://localhost:8080`. Kør derefter klienten:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du køre det komplette klientprojekt, der findes i løsningsmappen `03-GettingStarted\02-client\solution\java`:

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

## Opgave

I denne opgave skal du bruge det, du har lært om at oprette en klient, men lave din egen klient.

Her er en server, du kan bruge, som du skal kalde via din klientkode. Se, om du kan tilføje flere funktioner til serveren for at gøre den mere interessant.

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

Se dette projekt for at se, hvordan du kan [tilføje prompts og ressourcer](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tjek også dette link for, hvordan du aktiverer [prompts og ressourcer](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [det foregående afsnit](../../../../03-GettingStarted/01-first-server) lærte du, hvordan du opretter en simpel MCP-server med Rust. Du kan fortsætte med at bygge videre på det eller tjekke dette link for flere Rust-baserede MCP-servereksempler: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Løsning

**Løsningsmappen** indeholder komplette, klar-til-brug klientimplementeringer, der demonstrerer alle de begreber, der er dækket i denne tutorial. Hver løsning inkluderer både klient- og serverkode organiseret i separate, selvstændige projekter.

### 📁 Løsningsstruktur

Løsningsmappen er organiseret efter programmeringssprog:

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

### 🚀 Hvad hver løsning inkluderer

Hver sprog-specifik løsning giver:

- **Komplet klientimplementering** med alle funktioner fra tutorialen.
- **Fungerende projektstruktur** med korrekte afhængigheder og konfiguration.
- **Bygge- og kørescripts** for nem opsætning og udførelse.
- **Detaljeret README** med sprog-specifikke instruktioner.
- **Fejlhåndtering** og eksempler på resultatbehandling.

### 📖 Brug af løsningerne

1. **Naviger til din foretrukne sprogmappe**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Følg README-instruktionerne** i hver mappe for:
   - Installation af afhængigheder.
   - Bygning af projektet.
   - Kørsel af klienten.

3. **Eksempeloutput**, du bør se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For komplet dokumentation og trin-for-trin instruktioner, se: **[📖 Løsningsdokumentation](./solution/README.md)**

## 🎯 Komplette eksempler

Vi har leveret komplette, fungerende klientimplementeringer for alle programmeringssprog, der er dækket i denne tutorial. Disse eksempler demonstrerer den fulde funktionalitet beskrevet ovenfor og kan bruges som referenceimplementeringer eller udgangspunkt for dine egne projekter.

### Tilgængelige komplette eksempler

| Sprog      | Fil                              | Beskrivelse                                                                 |
|------------|----------------------------------|-----------------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Komplet Java-klient, der bruger SSE-transport med omfattende fejlhåndtering |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Komplet C#-klient, der bruger stdio-transport med automatisk serverstart    |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplet TypeScript-klient med fuld MCP-protokolunderstøttelse               |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Komplet Python-klient, der bruger async/await-mønstre                       |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Komplet Rust-klient, der bruger Tokio til asynkrone operationer             |
Hver komplet eksempel inkluderer:

- ✅ **Oprettelse af forbindelse** og fejlhåndtering
- ✅ **Serveropdagelse** (værktøjer, ressourcer, prompts hvor det er relevant)
- ✅ **Lommeregnerfunktioner** (plus, minus, gange, dividere, hjælp)
- ✅ **Resultatbehandling** og formateret output
- ✅ **Omfattende fejlhåndtering**
- ✅ **Ren, dokumenteret kode** med trin-for-trin kommentarer

### Kom godt i gang med komplette eksempler

1. **Vælg dit foretrukne sprog** fra tabellen ovenfor
2. **Gennemgå den komplette eksempelfil** for at forstå den fulde implementering
3. **Kør eksemplet** ved at følge instruktionerne i [`complete_examples.md`](./complete_examples.md)
4. **Tilpas og udvid** eksemplet til din specifikke brugssituation

For detaljeret dokumentation om at køre og tilpasse disse eksempler, se: **[📖 Dokumentation for komplette eksempler](./complete_examples.md)**

### 💡 Løsning vs. Komplette eksempler

| **Løsningsmappe** | **Komplette eksempler** |
|--------------------|-------------------------|
| Fuld projektstruktur med build-filer | Implementeringer i enkeltfiler |
| Klar til at køre med afhængigheder | Fokuserede kodeeksempler |
| Produktionslignende opsætning | Pædagogisk reference |
| Sprog-specifikke værktøjer | Sammenligning på tværs af sprog |

Begge tilgange er værdifulde - brug **løsningsmappen** til komplette projekter og **de komplette eksempler** til læring og reference.

## Vigtige pointer

De vigtigste pointer for dette kapitel om klienter er følgende:

- Kan bruges til både at opdage og anvende funktioner på serveren.
- Kan starte en server, mens den selv starter (som i dette kapitel), men klienter kan også forbinde til allerede kørende servere.
- Er en fantastisk måde at teste serverens kapabiliteter på, som et alternativ til værktøjer som Inspector, der blev beskrevet i det forrige kapitel.

## Yderligere ressourcer

- [Bygning af klienter i MCP](https://modelcontextprotocol.io/quickstart/client)

## Eksempler

- [Java Lommeregner](../samples/java/calculator/README.md)
- [.Net Lommeregner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Lommeregner](../samples/javascript/README.md)
- [TypeScript Lommeregner](../samples/typescript/README.md)
- [Python Lommeregner](../../../../03-GettingStarted/samples/python)
- [Rust Lommeregner](../../../../03-GettingStarted/samples/rust)

## Hvad er det næste

- Næste: [Oprettelse af en klient med en LLM](../03-llm-client/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
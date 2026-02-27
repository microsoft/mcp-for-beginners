# Oprettelse af en klient

Klienter er brugerdefinerede applikationer eller scripts, der kommunikerer direkte med en MCP-server for at anmode om ressourcer, værktøjer og prompts. I modsætning til at bruge inspektørværktøjet, som giver en grafisk grænseflade til at interagere med serveren, gør det at skrive din egen klient det muligt med programmatiske og automatiserede interaktioner. Dette giver udviklere mulighed for at integrere MCP-funktionaliteter i deres egne arbejdsprocesser, automatisere opgaver og bygge brugerdefinerede løsninger skræddersyet til specifikke behov.

## Oversigt

Denne lektion introducerer konceptet klienter inden for Model Context Protocol (MCP) økosystemet. Du lærer at skrive din egen klient og få den til at forbinde til en MCP-server.

## Læringsmål

Ved afslutningen af denne lektion vil du kunne:

- Forstå hvad en klient kan gøre.
- Skrive din egen klient.
- Forbinde og teste klienten med en MCP-server for at sikre, at denne fungerer som forventet.

## Hvad indebærer det at skrive en klient?

For at skrive en klient, skal du gøre følgende:

- **Importere de korrekte biblioteker**. Du vil bruge det samme bibliotek som før, bare forskellige konstruktioner.
- **Instantierer en klient**. Dette vil involvere at oprette en klientinstans og forbinde den til den valgte transportmetode.
- **Beslutte hvilke ressourcer der skal listes**. Din MCP-server kommer med ressourcer, værktøjer og prompts, du skal beslutte, hvilke der skal listes.
- **Integrere klienten til en værtapplikation**. Når du kender serverens kapaciteter, skal du integrere dette i din værtapplikation, så hvis en bruger skriver en prompt eller en anden kommando, bliver den tilsvarende serverfunktion kaldt.

Nu hvor vi på et overordnet niveau forstår, hvad vi skal gøre, lad os se på et eksempel næste.

### Et eksempel på en klient

Lad os kigge på dette eksempel på en klient:

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

// Hent en prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Liste ressourcer
const resources = await client.listResources();

// Læs en ressource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kald et værktøj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

I den foregående kode:

- Importerer vi bibliotekerne
- Opretter en instans af en klient og forbinder den med stdio som transport.
- Lister prompts, ressourcer og værktøjer og kalder dem alle.

Der har du det, en klient, der kan tale med en MCP-server.

Lad os tage os tid i næste øvelsesafsnit og gennemgå hvert kodesnit og forklare, hvad der sker.

## Øvelse: Skrive en klient

Som sagt ovenfor, lad os tage os tid til at forklare koden, og føl dig endelig fri til at kode med, hvis du vil.

### -1- Importere bibliotekerne

Lad os importere de nødvendige biblioteker; vi skal bruge referencer til en klient og til vores valgte transportprotokol, stdio. stdio er en protokol til ting, der er tænkt til at køre på din lokale maskine. SSE er en anden transportprotokol, som vi vil vise i kommende kapitler, men det er din anden mulighed. For nu, lad os fortsætte med stdio.

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

For Java opretter du en klient, der forbinder til MCP-serveren fra den tidligere øvelse. Brug den samme Java Spring Boot projektstruktur fra [Kom godt i gang med MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), opret en ny Java-klasse kaldet `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` og tilføj følgende imports:

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

Du skal tilføje følgende afhængigheder til din `Cargo.toml` fil.

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

Lad os gå videre til instantiering.

### -2- Instantiering af klient og transport

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

- Oprettet en stdio transport instans. Bemærk hvordan den specificerer kommando og argumenter for, hvordan serveren findes og startes, da det er noget, vi skal gøre, når vi opretter klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instantieret en klient ved at give den navn og version.

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

# Opret serverparametre til stdio-forbindelse
server_params = StdioServerParameters(
    command="mcp",  # Kørbar fil
    args=["run", "server.py"],  # Valgfrie kommandolinjeparametre
    env=None,  # Valgfrie miljøvariabler
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiser forbindelsen
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

I den foregående kode har vi:

- Importeret de nødvendige biblioteker
- Instantieret et serverparameterobjekt, da vi vil bruge dette til at køre serveren, så vi kan forbinde til den med vores klient.
- Defineret en metode `run`, der til gengæld kalder `stdio_client`, som starter en klientsession.
- Oprettet et entry point, hvor vi leverer `run` metoden til `asyncio.run`.

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

I den foregående kode har vi:

- Importeret de nødvendige biblioteker.
- Oprettet en stdio transport og oprettet en klient `mcpClient`. Sidstnævnte bruger vi til at liste og kalde funktioner på MCP-serveren.

Bemærk, i "Arguments" kan du enten pege på *.csproj* eller på det eksekverbare program.

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
        
        // Din klientlogik går her
    }
}
```

I den foregående kode har vi:

- Oprettet en main-metode, der sætter en SSE transport op, som peger på `http://localhost:8080`, hvor vores MCP-server kører.
- Oprettet en klientklasse, der tager transporten som konstruktørparameter.
- I `run` metoden opretter vi en synkron MCP klient ved hjælp af transporten og initialiserer forbindelsen.
- Brugte SSE (Server-Sent Events) transport, som passer til HTTP-baseret kommunikation med Java Spring Boot MCP-servere.

#### Rust

Bemærk, at denne Rust-klient antager, at serveren er et søskendeprojekt kaldet "calculator-server" i samme mappe. Koden nedenfor vil starte serveren og forbinde til den.

```rust
async fn main() -> Result<(), RmcpError> {
    // Antag at serveren er et søskendeprojekt kaldet "calculator-server" i samme mappe
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

    // TODO: Initialiser

    // TODO: List værktøjer

    // TODO: Kald tilføj værktøj med argumenter = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Liste serverens funktioner

Nu har vi en klient, der kan forbinde til serveren, hvis programmet køres. Den lister dog ikke dens funktioner, så lad os gøre det næste:

#### TypeScript

```typescript
// Liste over prompt
const prompts = await client.listPrompts();

// Liste over ressourcer
const resources = await client.listResources();

// liste over værktøjer
const tools = await client.listTools();
```

#### Python

```python
# List tilgængelige ressourcer
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List tilgængelige værktøjer
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Her lister vi de tilgængelige ressourcer, `list_resources()` og værktøjer, `list_tools` og printer dem ud.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ovenfor er et eksempel på, hvordan vi kan liste værktøjerne på serveren. For hvert værktøj printer vi så navnet ud.

#### Java

```java
// Liste og demonstrere værktøjer
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Du kan også pinge serveren for at bekræfte forbindelsen
client.ping();
```

I den foregående kode har vi:

- Kaldt `listTools()` for at få alle tilgængelige værktøjer fra MCP-serveren.
- Brugte `ping()` for at verificere, at forbindelsen til serveren fungerer.
- `ListToolsResult` indeholder information om alle værktøjer, inklusive deres navne, beskrivelser og inputskemaer.

Fint, nu har vi fanget alle funktionerne. Nu er spørgsmålet, hvornår bruger vi dem? Denne klient er ret simpel, simpel i den forstand, at vi eksplicit skal kalde funktionerne, når vi ønsker dem. I næste kapitel vil vi oprette en mere avanceret klient, der har adgang til sin egen store sprogmodel, LLM. Men for nu, lad os se, hvordan vi kan kalde funktionerne på serveren:

#### Rust

I main-funktionen, efter initialisering af klienten, kan vi initialisere serveren og liste nogle af dens funktioner.

```rust
// Initialiser
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listeværktøjer
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Kald funktioner

For at kalde funktionerne skal vi sikre, at vi angiver de rigtige argumenter og i nogle tilfælde navnet på det, vi forsøger at kalde.

#### TypeScript

```typescript

// Læs en ressource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kald et værktøj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// kald prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

I den foregående kode:

- Læser vi en ressource ved at kalde `readResource()` og angive `uri`. Her ser det ud, som det sandsynligvis gør på serversiden:

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

    Vores `uri` værdi `file://example.txt` matcher `file://{name}` på serveren. `example.txt` kortlægges til `name`.

- Kalder et værktøj, vi kalder det ved at angive dets `name` og dets `arguments` som følger:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Henter prompt, for at hente en prompt kalder du `getPrompt()` med `name` og `arguments`. Serverkoden ser sådan ud:

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

    og din resulterende klientkode ser derfor sådan ud for at matche det, der er deklareret på serveren:

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
# Læs en ressource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Kald et værktøj
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

I den foregående kode har vi:

- Kaldt en ressource kaldet `greeting` med `read_resource`.
- Invokeret et værktøj kaldet `add` med `call_tool`.

#### .NET

1. Lad os tilføje noget kode til at kalde et værktøj:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. For at printe resultatet, her er noget kode til at håndtere det:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Kald forskellige lommeregnerværktøjer
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

- Kaldt flere kalkulatorværktøjer ved hjælp af `callTool()` metoden med `CallToolRequest` objekter.
- Hver værktøjskald specificerer værktøjets navn og et `Map` af argumenter, som værktøjet kræver.
- Serverværktøjerne forventer specifikke parameternavne (som "a", "b" for matematiske operationer).
- Resultater returneres som `CallToolResult` objekter, der indeholder serverens svar.

#### Rust

```rust
// Kald add værktøj med argumenter = {"a": 3, "b": 2}
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

Tilføj følgende entry til din "scripts" sektion i *package.json*:

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
# Byg dit projekt
./mvnw clean compile

# Kør klienten
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du køre det komplette klientprojekt, som findes i løsningsmappen `03-GettingStarted\02-client\solution\java`:

```bash
# Naviger til løsningsmappen
cd 03-GettingStarted/02-client/solution/java

# Byg og kør JAR'en
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Opgave

I denne opgave vil du bruge det, du har lært, til at oprette en klient, men oprette din egen klient.

Her er en server, du kan bruge, som du skal kalde via din klientkode, se om du kan tilføje flere funktioner til serveren for at gøre den mere interessant.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Opret en MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Tilføj et additionsværktøj
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Tilføj en dynamisk hilsensressource
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

// Begynd at modtage beskeder på stdin og sende beskeder på stdout

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

# Opret en MCP-server
mcp = FastMCP("Demo")


# Tilføj et additionsværktøj
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Tilføj en dynamisk hilsen-ressource
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

Tjek også dette link for, hvordan du kalder [prompts og ressourcer](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [forrige afsnit](../../../../03-GettingStarted/01-first-server) lærte du, hvordan man opretter en simpel MCP-server med Rust. Du kan fortsætte med at bygge videre på det eller tjekke dette link for flere Rust-baserede MCP-server eksempler: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Løsning

**løsningsmappen** indeholder komplette, klar-til-kørsel klientimplementeringer, der demonstrerer alle koncepterne dækket i denne tutorial. Hver løsning inkluderer både klient- og serverkode organiseret i separate, selvstændige projekter.

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

Hver sprog-specifik løsning indeholder:

- **Komplet klientimplementering** med alle funktioner fra tutorialen
- **Fungerende projektstruktur** med korrekte afhængigheder og konfiguration
- **Build- og kørescripts** for nem opsætning og eksekvering
- **Detaljeret README** med sprog-specifikke instruktioner
- **Fejlhåndtering** og eksempler på resultatbehandling

### 📖 Brug af løsningerne

1. **Naviger til din foretrukne sprogmappe**:

   ```bash
   cd solution/typescript/    # Til TypeScript
   cd solution/java/          # Til Java
   cd solution/python/        # Til Python
   cd solution/dotnet/        # Til .NET
   ```

2. **Følg README instruktionerne** i hver mappe for:
   - Installation af afhængigheder
   - Bygning af projektet
   - Kørsel af klienten

3. **Eksempelkørsel**, som du bør se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For komplet dokumentation og trin-for-trin instruktioner, se: **[📖 Løsningsdokumentation](./solution/README.md)**

## 🎯 Komplette eksempler

Vi har leveret komplette, fungerende klientimplementeringer for alle programmeringssprog dækket i denne tutorial. Disse eksempler demonstrerer den fulde funktionalitet beskrevet ovenfor og kan bruges som referenceimplementeringer eller udgangspunkter for dine egne projekter.

### Tilgængelige komplette eksempler

| Sprog | Fil | Beskrivelse |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompleks Java-klient med SSE-transport og omfattende fejlhåndtering |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompleks C#-klient med stdio transport og automatisk serverstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompleks TypeScript-klient med fuld MCP-protokol support |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompleks Python-klient med async/await mønstre |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompleks Rust-klient med Tokio til async operationer |

Hvert komplet eksempel inkluderer:
- ✅ **Oprettelse af forbindelse** og fejlhåndtering  
- ✅ **Serveropdagelse** (værktøjer, ressourcer, prompts hvor relevant)  
- ✅ **Lommeregneroperationer** (plus, minus, gange, divider, hjælp)  
- ✅ **Resultatbehandling** og formateret output  
- ✅ **Omfattende fejlhåndtering**  
- ✅ **Ren, dokumenteret kode** med trin-for-trin kommentarer  

### Kom godt i gang med komplette eksempler

1. **Vælg dit foretrukne sprog** fra tabellen ovenfor  
2. **Gennemgå den komplette eksempel-fil** for at forstå den fulde implementering  
3. **Kør eksemplet** ved at følge instruktionerne i [`complete_examples.md`](./complete_examples.md)  
4. **Tilpas og udvid** eksemplet til dit specifikke brugstilfælde  

For detaljeret dokumentation om kørsel og tilpasning af disse eksempler, se: **[📖 Kompletdokumentation for eksempler](./complete_examples.md)**  

### 💡 Løsning vs. komplette eksempler

| **Løsningsmappe**     | **Komplette eksempler**  |
|----------------------|-------------------------|
| Fuld projektstruktur med build-filer | Enkel-fil implementeringer  |
| Klar til kørsel med afhængigheder | Fokuserede kodeeksempler       |
| Produktionslignende setup  | Læringsreference                |
| Sprog-specifikke værktøjer | Tvær-sproglig sammenligning    |

Begge tilgange er værdifulde - brug **løsningsmappen** til komplette projekter og **komplette eksempler** til læring og reference.

## Vigtige pointer

De vigtigste pointer i dette kapitel om clients er følgende:

- Kan bruges til både at opdage og kalde funktioner på serveren.  
- Kan starte en server, mens den selv starter (som i dette kapitel), men clients kan også forbinde til kørende servere.  
- Er en fremragende måde at teste serverkapaciteter ved siden af alternativer som Inspector, som blev beskrevet i det forrige kapitel.  

## Yderligere ressourcer

- [Byg clients i MCP](https://modelcontextprotocol.io/quickstart/client)  

## Eksempler

- [Java Lommeregner](../samples/java/calculator/README.md)  
- [.Net Lommeregner](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Lommeregner](../samples/javascript/README.md)  
- [TypeScript Lommeregner](../samples/typescript/README.md)  
- [Python Lommeregner](../../../../03-GettingStarted/samples/python)  
- [Rust Lommeregner](../../../../03-GettingStarted/samples/rust)  

## Hvad er det næste

- Næste: [Opret en client med en LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog skal betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
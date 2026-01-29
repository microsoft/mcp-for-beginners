# Opprette en klient

Klienter er tilpassede applikasjoner eller skript som kommuniserer direkte med en MCP-server for å be om ressurser, verktøy og forespørsler. I motsetning til å bruke inspeksjonsverktøyet, som gir et grafisk grensesnitt for å samhandle med serveren, lar det å skrive din egen klient deg automatisere og programmere interaksjoner. Dette gjør det mulig for utviklere å integrere MCP-funksjonalitet i sine egne arbeidsflyter, automatisere oppgaver og bygge skreddersydde løsninger tilpasset spesifikke behov.

## Oversikt

Denne leksjonen introduserer konseptet med klienter innenfor Model Context Protocol (MCP)-økosystemet. Du vil lære hvordan du skriver din egen klient og kobler den til en MCP-server.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Forstå hva en klient kan gjøre.
- Skrive din egen klient.
- Koble til og teste klienten med en MCP-server for å sikre at den fungerer som forventet.

## Hva kreves for å skrive en klient?

For å skrive en klient må du gjøre følgende:

- **Importere de riktige bibliotekene**. Du vil bruke det samme biblioteket som før, men med forskjellige konstruksjoner.
- **Opprette en klientinstans**. Dette innebærer å opprette en klient og koble den til den valgte transportmetoden.
- **Bestemme hvilke ressurser som skal listes**. MCP-serveren din har ressurser, verktøy og forespørsler, og du må bestemme hvilke du vil liste.
- **Integrere klienten i en vertsapplikasjon**. Når du kjenner til serverens funksjoner, må du integrere dette i vertsapplikasjonen slik at når en bruker skriver inn en forespørsel eller kommando, aktiveres den tilsvarende serverfunksjonen.

Nå som vi har en overordnet forståelse av hva vi skal gjøre, la oss se på et eksempel.

### Et eksempel på en klient

La oss se på dette eksempelet på en klient:

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

I koden ovenfor:

- Importerer vi bibliotekene.
- Oppretter en klientinstans og kobler den til ved hjelp av stdio som transport.
- Lister forespørsler, ressurser og verktøy og aktiverer dem alle.

Der har du det, en klient som kan kommunisere med en MCP-server.

La oss bruke tid i neste øvelsesdel på å bryte ned hver kodebit og forklare hva som skjer.

## Øvelse: Skrive en klient

Som nevnt ovenfor, la oss ta oss tid til å forklare koden, og for all del kode sammen hvis du vil.

### -1- Importere bibliotekene

La oss importere bibliotekene vi trenger. Vi trenger referanser til en klient og til vår valgte transportprotokoll, stdio. stdio er en protokoll for ting som skal kjøres på din lokale maskin. SSE er en annen transportprotokoll vi vil vise i fremtidige kapitler, men det er ditt andre alternativ. For nå fortsetter vi med stdio.

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

For Java oppretter du en klient som kobler til MCP-serveren fra forrige øvelse. Ved å bruke den samme Java Spring Boot-prosjektstrukturen fra [Kom i gang med MCP-server](../../../../03-GettingStarted/01-first-server/solution/java), opprett en ny Java-klasse kalt `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` og legg til følgende imports:

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

Du må legge til følgende avhengigheter i `Cargo.toml`-filen.

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

Derfra kan du importere de nødvendige bibliotekene i klientkoden.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

La oss gå videre til instansiering.

### -2- Opprette klient og transport

Vi må opprette en instans av transporten og en av klienten vår:

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

I koden ovenfor har vi:

- Opprettet en stdio-transportinstans. Merk hvordan den spesifiserer kommando og argumenter for hvordan man finner og starter serveren, da dette er noe vi må gjøre når vi oppretter klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Opprettet en klient ved å gi den et navn og en versjon.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Knyttet klienten til den valgte transporten.

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

I koden ovenfor har vi:

- Importert de nødvendige bibliotekene.
- Opprettet et serverparameterobjekt som vi vil bruke til å kjøre serveren slik at vi kan koble til den med klienten vår.
- Definert en metode `run` som igjen kaller `stdio_client` for å starte en klientsesjon.
- Opprettet et inngangspunkt der vi gir `run`-metoden til `asyncio.run`.

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

I koden ovenfor har vi:

- Importert de nødvendige bibliotekene.
- Opprettet en stdio-transport og en klient `mcpClient`. Sistnevnte er noe vi vil bruke til å liste og aktivere funksjoner på MCP-serveren.

Merk at i "Arguments" kan du enten peke til *.csproj*-filen eller til den kjørbare filen.

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

I koden ovenfor har vi:

- Opprettet en hovedmetode som setter opp en SSE-transport som peker til `http://localhost:8080`, der MCP-serveren vår vil kjøre.
- Opprettet en klientklasse som tar transporten som en konstruktørparameter.
- I `run`-metoden oppretter vi en synkron MCP-klient ved hjelp av transporten og initialiserer tilkoblingen.
- Brukt SSE (Server-Sent Events)-transport, som er egnet for HTTP-basert kommunikasjon med Java Spring Boot MCP-servere.

#### Rust

Denne Rust-klienten antar at serveren er et søsterprosjekt kalt "calculator-server" i samme katalog. Koden nedenfor vil starte serveren og koble til den.

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

### -3- Liste serverfunksjonene

Nå har vi en klient som kan koble til hvis programmet kjøres. Men den lister ikke faktisk funksjonene sine, så la oss gjøre det neste:

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

Her lister vi de tilgjengelige ressursene med `list_resources()` og verktøyene med `list_tools` og skriver dem ut.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ovenfor er et eksempel på hvordan vi kan liste verktøyene på serveren. For hvert verktøy skriver vi deretter ut navnet.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

I koden ovenfor har vi:

- Kalt `listTools()` for å hente alle tilgjengelige verktøy fra MCP-serveren.
- Brukt `ping()` for å bekrefte at tilkoblingen til serveren fungerer.
- `ListToolsResult` inneholder informasjon om alle verktøy, inkludert navn, beskrivelser og inndataskjemaer.

Flott, nå har vi fanget opp alle funksjonene. Spørsmålet er når vi skal bruke dem? Vel, denne klienten er ganske enkel, i den forstand at vi eksplisitt må kalle funksjonene når vi ønsker dem. I neste kapittel vil vi lage en mer avansert klient som har tilgang til sin egen store språkmodell (LLM). For nå, la oss se hvordan vi kan aktivere funksjonene på serveren:

#### Rust

I hovedfunksjonen, etter å ha initialisert klienten, kan vi initialisere serveren og liste noen av funksjonene.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Aktivere funksjoner

For å aktivere funksjonene må vi sørge for at vi spesifiserer de riktige argumentene og i noen tilfeller navnet på det vi prøver å aktivere.

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

I koden ovenfor:

- Leser vi en ressurs ved å kalle `readResource()` og spesifisere `uri`. Slik ser det mest sannsynlig ut på serversiden:

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

    Vår `uri`-verdi `file://example.txt` samsvarer med `file://{name}` på serveren. `example.txt` vil bli mappet til `name`.

- Kaller et verktøy ved å spesifisere `name` og `arguments` slik:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Henter en forespørsel ved å kalle `getPrompt()` med `name` og `arguments`. Serverkoden ser slik ut:

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

    Og den resulterende klientkoden ser derfor slik ut for å samsvare med det som er deklarert på serveren:

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

I koden ovenfor har vi:

- Kalt en ressurs kalt `greeting` ved hjelp av `read_resource`.
- Aktivert et verktøy kalt `add` ved hjelp av `call_tool`.

#### .NET

1. La oss legge til litt kode for å kalle et verktøy:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. For å skrive ut resultatet, her er litt kode for å håndtere det:

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

I koden ovenfor har vi:

- Kalt flere kalkulatorverktøy ved hjelp av `callTool()`-metoden med `CallToolRequest`-objekter.
- Hver verktøykall spesifiserer verktøynavnet og et `Map` med argumenter som kreves av det verktøyet.
- Serververktøyene forventer spesifikke parameternavn (som "a", "b" for matematiske operasjoner).
- Resultatene returneres som `CallToolResult`-objekter som inneholder svaret fra serveren.

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

### -5- Kjøre klienten

For å kjøre klienten, skriv følgende kommando i terminalen:

#### TypeScript

Legg til følgende oppføring i "scripts"-delen i *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kjør klienten med følgende kommando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Først, sørg for at MCP-serveren din kjører på `http://localhost:8080`. Kjør deretter klienten:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du kjøre det komplette klientprosjektet som finnes i løsningsmappen `03-GettingStarted\02-client\solution\java`:

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

## Oppgave

I denne oppgaven skal du bruke det du har lært om å lage en klient, men lage en klient på egen hånd.

Her er en server du kan bruke som du må kalle via klientkoden din. Se om du kan legge til flere funksjoner på serveren for å gjøre den mer interessant.

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

Se dette prosjektet for å se hvordan du kan [legge til forespørsler og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Sjekk også denne lenken for hvordan du aktiverer [forespørsler og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [forrige seksjon](../../../../03-GettingStarted/01-first-server) lærte du hvordan du oppretter en enkel MCP-server med Rust. Du kan fortsette å bygge på det eller sjekke denne lenken for flere MCP-servereksempler basert på Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Løsning

**Løsningsmappen** inneholder komplette, kjørbare klientimplementasjoner som demonstrerer alle konseptene som er dekket i denne opplæringen. Hver løsning inkluderer både klient- og serverkode organisert i separate, selvstendige prosjekter.

### 📁 Løsningsstruktur

Løsningsmappen er organisert etter programmeringsspråk:

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

### 🚀 Hva hver løsning inkluderer

Hver språkspesifikke løsning gir:

- **Komplett klientimplementasjon** med alle funksjoner fra opplæringen.
- **Fungerende prosjektstruktur** med riktige avhengigheter og konfigurasjon.
- **Bygge- og kjøreskript** for enkel oppsett og kjøring.
- **Detaljert README** med språkspesifikke instruksjoner.
- **Feilhåndtering** og eksempler på resultatbehandling.

### 📖 Bruke løsningene

1. **Naviger til mappen for ditt foretrukne språk**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Følg README-instruksjonene** i hver mappe for:
   - Installere avhengigheter.
   - Bygge prosjektet.
   - Kjøre klienten.

3. **Eksempelutdata** du bør se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For fullstendig dokumentasjon og trinnvise instruksjoner, se: **[📖 Løsningsdokumentasjon](./solution/README.md)**

## 🎯 Komplette eksempler

Vi har gitt komplette, fungerende klientimplementasjoner for alle programmeringsspråk som er dekket i denne opplæringen. Disse eksemplene demonstrerer full funksjonalitet som beskrevet ovenfor og kan brukes som referanseimplementasjoner eller utgangspunkt for dine egne prosjekter.

### Tilgjengelige komplette eksempler

| Språk       | Fil                              | Beskrivelse |
|-------------|----------------------------------|-------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Komplett Java-klient som bruker SSE-transport med omfattende feilhåndtering |
| **C#**      | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Komplett C#-klient som bruker stdio-transport med automatisk serveroppstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplett TypeScript-klient med full MCP-protokollstøtte |
| **Python**  | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Komplett Python-klient som bruker async/await-mønstre |
| **Rust**    | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Komplett Rust-klient som bruker Tokio for asynkrone operasjoner |
Hver komplette eksempel inkluderer:

- ✅ **Opprettelse av tilkobling** og feilhåndtering
- ✅ **Serveroppdagelse** (verktøy, ressurser, forslag der det er relevant)
- ✅ **Kalkulatoroperasjoner** (addere, subtrahere, multiplisere, dividere, hjelp)
- ✅ **Resultatbehandling** og formatert utdata
- ✅ **Omfattende feilhåndtering**
- ✅ **Ren, dokumentert kode** med steg-for-steg-kommentarer

### Komme i gang med komplette eksempler

1. **Velg ditt foretrukne språk** fra tabellen ovenfor
2. **Gå gjennom den komplette eksempel-filen** for å forstå hele implementasjonen
3. **Kjør eksemplet** ved å følge instruksjonene i [`complete_examples.md`](./complete_examples.md)
4. **Tilpass og utvid** eksemplet for ditt spesifikke brukstilfelle

For detaljert dokumentasjon om hvordan du kjører og tilpasser disse eksemplene, se: **[📖 Dokumentasjon for komplette eksempler](./complete_examples.md)**

### 💡 Løsning vs. Komplette eksempler

| **Løsningsmappe** | **Komplette eksempler** |
|--------------------|-------------------------|
| Full prosjektstruktur med byggefiler | Implementasjoner i én enkelt fil |
| Klar til å kjøre med avhengigheter | Fokuserte kodeeksempler |
| Produksjonslignende oppsett | Pedagogisk referanse |
| Språkspesifikke verktøy | Tverrspråklig sammenligning |

Begge tilnærmingene er verdifulle - bruk **løsningsmappen** for komplette prosjekter og **komplette eksempler** for læring og referanse.

## Viktige punkter

De viktigste punktene for dette kapittelet om klienter er følgende:

- Kan brukes både til å oppdage og bruke funksjoner på serveren.
- Kan starte en server samtidig som den starter seg selv (som i dette kapittelet), men klienter kan også koble seg til allerede kjørende servere.
- Er en flott måte å teste serverens funksjonalitet på, i tillegg til alternativer som Inspektøren som ble beskrevet i forrige kapittel.

## Tilleggsressurser

- [Bygge klienter i MCP](https://modelcontextprotocol.io/quickstart/client)

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Hva kommer neste

- Neste: [Opprette en klient med en LLM](../03-llm-client/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
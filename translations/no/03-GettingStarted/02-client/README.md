# Lage en klient

Klienter er tilpassede applikasjoner eller skript som kommuniserer direkte med en MCP-server for å be om ressurser, verktøy og spørsmål. I motsetning til å bruke inspektørverktøyet, som gir et grafisk grensesnitt for å samhandle med serveren, tillater det å skrive sin egen klient programmatisk og automatisert samhandling. Dette gjør det mulig for utviklere å integrere MCP-funksjoner i sine egne arbeidsflyter, automatisere oppgaver og bygge skreddersydde løsninger tilpasset spesifikke behov.

## Oversikt

Denne leksjonen introduserer konseptet klienter innenfor Model Context Protocol (MCP)-økosystemet. Du vil lære hvordan du skriver din egen klient og får den til å koble til en MCP-server.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Forstå hva en klient kan gjøre.
- Skrive din egen klient.
- Koble til og teste klienten med en MCP-server for å sikre at den fungerer som forventet.

## Hva kreves for å skrive en klient?

For å skrive en klient må du gjøre følgende:

- **Importere riktige biblioteker**. Du vil bruke det samme biblioteket som før, bare med forskjellige konstruksjoner.
- **Opprette en klient-forekomst**. Dette innebærer å lage en klientinstans og koble den til valgt transportmetode.
- **Bestemme hvilke ressurser som skal listes**. Din MCP-server har ressurser, verktøy og spørsmål, du må avgjøre hvilke som skal listes.
- **Integrere klienten med en vertsapplikasjon**. Når du vet hvilke muligheter serveren har, må du integrere dette i din vertsapplikasjon slik at når en bruker skriver et spørsmål eller en annen kommando, blir tilsvarende serverfunksjon aktivert.

Nå som vi forstår overordnet hva vi skal gjøre, la oss se på et eksempel.

### Et eksempel på klient

La oss se på dette eksempel på klient:

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

// List oppgaver
const prompts = await client.listPrompts();

// Hent en oppgave
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List ressurser
const resources = await client.listResources();

// Les en ressurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kall et verktøy
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

I koden over har vi:

- Importert bibliotekene
- Opprettet en instans av en klient og koblet den til ved hjelp av stdio som transport.
- Listet spørsmål, ressurser og verktøy og kalt alle.

Der har du det, en klient som kan kommunisere med en MCP-server.

La oss bruke god tid i neste øvelsesdel for å bryte ned hvert kodesnitt og forklare hva som skjer.

## Øvelse: Skrive en klient

Som nevnt ovenfor, la oss bruke god tid på å forklare koden, og føl gjerne med og kode selv hvis du vil.

### -1- Importere bibliotekene

La oss importere bibliotekene vi trenger, vi vil trenge referanser til en klient og til vår valgte transportprotokoll, stdio. stdio er en protokoll for ting ment å kjøre på din lokale maskin. SSE er en annen transportprotokoll vi vil vise i fremtidige kapitler, men det er ditt andre alternativ. For nå, la oss fortsette med stdio.

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

For Java vil du opprette en klient som kobler til MCP-serveren fra forrige øvelse. Ved å bruke den samme Java Spring Boot-prosjektstrukturen fra [Kom i gang med MCP-server](../../../../03-GettingStarted/01-first-server/solution/java), opprett en ny Java-klasse kalt `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` og legg til følgende imports:

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

Du må legge til følgende avhengigheter i din `Cargo.toml`-fil.

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

Derfra kan du importere nødvendige biblioteker i klientkoden din.

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

### -2- Instansiere klient og transport

Vi må opprette en instans av transporten og en av klienten:

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

I koden over har vi:

- Opprettet en stdio-transportinstans. Legg merke til hvordan den spesifiserer kommando og argumenter for hvordan man finner og starter serveren, noe vi trenger å gjøre mens vi oppretter klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instansiert en klient ved å gi den et navn og versjon.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Knyttet klienten til valgt transport.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Opprett serverparametere for stdio-tilkobling
server_params = StdioServerParameters(
    command="mcp",  # Kjørbar fil
    args=["run", "server.py"],  # Valgfrie kommandolinjeargumenter
    env=None,  # Valgfrie miljøvariabler
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiser tilkoblingen
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

I koden over har vi:

- Importert nødvendige biblioteker
- Instansiert et objekt for serverparametere som vi bruker for å kjøre serveren slik at vi kan koble til den med vår klient.
- Definert en metode `run` som i sin tur kaller `stdio_client` som starter en klientøkt.
- Opprettet et startpunkt der vi gir `run`-metoden til `asyncio.run`.

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

I koden over har vi:

- Importert nødvendige biblioteker.
- Opprettet en stdio-transport og laget en klient `mcpClient`. Sistnevnte er noe vi bruker for å liste og aktivere funksjoner på MCP-serveren.

Merk at i "Arguments" kan du enten peke til *.csproj* eller til den kjørbare filen.

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
        
        // Din klientlogikk går her
    }
}
```

I koden over har vi:

- Opprettet en main-metode som setter opp en SSE-transport som peker til `http://localhost:8080` hvor vår MCP-server vil kjøre.
- Opprettet en klientklasse som tar transporten som konstruktørparameter.
- I `run`-metoden oppretter vi en synkron MCP-klient med transporten og initialiserer forbindelsen.
- Brukt SSE (Server-Sent Events) transport som er passende for HTTP-basert kommunikasjon med Java Spring Boot MCP-servere.

#### Rust

Merk at denne Rust-klienten antar at serveren er et søskenprosjekt kalt "calculator-server" i samme katalog. Koden under vil starte serveren og koble til den.

```rust
async fn main() -> Result<(), RmcpError> {
    // Antar at serveren er et søskenprosjekt kalt "calculator-server" i samme katalog
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

    // TODO: Initialisere

    // TODO: Liste verktøy

    // TODO: Kall legg til verktøy med argumenter = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Liste serverfunksjonene

Nå har vi en klient som kan koble til dersom programmet kjøres. Likevel lister den ikke funksjonene sine, så la oss gjøre det nå:

#### TypeScript

```typescript
// List oppgaver
const prompts = await client.listPrompts();

// List ressurser
const resources = await client.listResources();

// list verktøy
const tools = await client.listTools();
```

#### Python

```python
# List tilgjengelige ressurser
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List tilgjengelige verktøy
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Her lister vi de tilgjengelige ressursene, `list_resources()` og verktøyene, `list_tools` og skriver dem ut.

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
// List opp og demonstrer verktøy
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Du kan også sende ping til serveren for å verifisere tilkoblingen
client.ping();
```

I koden over har vi:

- Kalt `listTools()` for å hente alle tilgjengelige verktøy fra MCP-serveren.
- Brukt `ping()` for å verifisere at forbindelsen til serveren fungerer.
- `ListToolsResult` inneholder informasjon om alle verktøy, inkludert navn, beskrivelser og inndataskjemaer.

Flott, nå har vi fanget alle funksjonene. Spørsmålet er når bruker vi dem? Vel, denne klienten er ganske enkel, enkel i den forstand at vi må eksplisitt kalle funksjonene når vi vil ha dem. I neste kapittel lager vi en mer avansert klient som har tilgang til sin egen store språkmodell, LLM. For nå, la oss se hvordan vi kan aktivere funksjonene på serveren:

#### Rust

I hovedfunksjonen, etter å ha initialisert klienten, kan vi initialisere serveren og liste noen av dens funksjoner.

```rust
// Initialiser
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Liste over verktøy
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Aktivere funksjoner

For å aktivere funksjonene må vi sikre at vi spesifiserer riktige argumenter og i noen tilfeller navnet på det vi prøver å aktivere.

#### TypeScript

```typescript

// Les en ressurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kall et verktøy
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// kall prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

I koden over har vi:

- Lest en ressurs, vi kaller ressursen ved å kalle `readResource()` og spesifisere `uri`. Slik ser det mest sannsynlig ut på serversiden:

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

    Vår `uri` verdi `file://example.txt` matcher `file://{name}` på serveren. `example.txt` vil bli kartlagt til `name`.

- Kalt et verktøy, vi gjør det ved å spesifisere `name` og `arguments` slik:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Hentet spørsmål, for å få et spørsmål kaller du `getPrompt()` med `name` og `arguments`. Serverkoden ser slik ut:

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

    og klientkoden din vil derfor se slik ut for å samsvare med det som er deklarert på serveren:

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
# Les en ressurs
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Kall et verktøy
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

I koden over har vi:

- Kalt en ressurs kalt `greeting` med `read_resource`.
- Aktivert et verktøy kalt `add` med `call_tool`.

#### .NET

1. La oss legge til noe kode for å kalle et verktøy:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. For å skrive ut resultatet, her er kode for det:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Kall ulike kalkulatorverktøy
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

I koden over har vi:

- Kalt flere kalkulatorverktøy med `callTool()` metoden med `CallToolRequest` objekter.
- Hver verktøysanrop spesifiserer verktøyets navn og en `Map` med argumenter som kreves av det verktøyet.
- Serverens verktøy forventer spesifikke parameter-navn (som "a", "b" for matematiske operasjoner).
- Resultater returneres som `CallToolResult` objekter som inneholder responsen fra serveren.

#### Rust

```rust
// Kall legg til-verktøy med argumenter = {"a": 3, "b": 2}
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

Legg til følgende oppføring i "scripts"-seksjonen i *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kall klienten med følgende kommando:

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
# Bygg prosjektet ditt
./mvnw clean compile

# Kjør klienten
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du kjøre det komplette klientprosjektet som finnes i løsningsmappen `03-GettingStarted\02-client\solution\java`:

```bash
# Naviger til løsningsmappen
cd 03-GettingStarted/02-client/solution/java

# Bygg og kjør JAR-filen
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Oppgave

I denne oppgaven skal du bruke det du har lært om å lage en klient, men lage din egen klient.

Her er en server du kan bruke som du må kalle via klientkoden din, se om du kan legge til flere funksjoner i serveren for å gjøre den mer interessant.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Opprett en MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Legg til et tillegg verktøy
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Legg til en dynamisk hilsenressurs
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

// Begynn å motta meldinger på stdin og sende meldinger på stdout

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

# Opprett en MCP-server
mcp = FastMCP("Demo")


# Legg til et tillegg verktøy
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Legg til en dynamisk hilsenressurs
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

Se dette prosjektet for å se hvordan du kan [legge til spørsmål og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Sjekk også denne lenken for hvordan å aktivere [spørsmål og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [forrige seksjon](../../../../03-GettingStarted/01-first-server) lærte du hvordan man oppretter en enkel MCP-server med Rust. Du kan fortsette å bygge videre på det eller sjekke denne lenken for flere Rust-baserte MCP-server eksempler: [MCP Server Eksempler](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Løsning

**Løsningsmappen** inneholder komplette, kjøringsklare klientimplementasjoner som demonstrerer alle konseptene dekket i denne opplæringen. Hver løsning inkluderer både klient- og serverkode organisert i separate, selvstendige prosjekter.

### 📁 Løsningsstruktur

Løsningskatalogen er organisert etter programmeringsspråk:

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

Hver språkspesifikke løsning tilbyr:

- **Fullstendig klientimplementasjon** med alle funksjoner fra opplæringen
- **Fungerende prosjektstruktur** med riktige avhengigheter og konfigurasjon
- **Bygg- og kjør-skript** for enkel oppsett og kjøring
- **Detaljert README** med språkspesifikke instruksjoner
- **Feilhåndtering** og eksempler på resultatbehandling

### 📖 Bruke løsningene

1. **Naviger til din foretrukne språkmappe**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Følg README-instruksjonene** i hver mappe for:
   - Installere avhengigheter
   - Bygge prosjektet
   - Kjøre klienten

3. **Eksempelutdata** du bør se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For full dokumentasjon og trinnvise instruksjoner, se: **[📖 Løsningsdokumentasjon](./solution/README.md)**

## 🎯 Fullstendige eksempler

Vi har levert komplette, fungerende klientimplementasjoner for alle programmeringsspråk dekket i denne opplæringen. Disse eksemplene demonstrerer all funksjonaliteten beskrevet ovenfor og kan brukes som referanseimplementasjoner eller utgangspunkt for dine egne prosjekter.

### Tilgjengelige fullstendige eksempler

| Språk | Fil | Beskrivelse |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Komplett Java-klient som bruker SSE-transport med omfattende feilhåndtering |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Komplett C# klient med stdio-transport med automatisk serveroppstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplett TypeScript-klient med full MCP-protokollstøtte |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Komplett Python-klient som bruker async/await-mønstre |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Komplett Rust-klient som bruker Tokio for asynkrone operasjoner |

Hvert komplett eksempel inkluderer:

- ✅ **Etablering av forbindelser** og feilhåndtering
- ✅ **Serveroppdagelse** (verktøy, ressurser, spørsmål der det er aktuelt)
- ✅ **Kalkulatoroperasjoner** (addere, subtrahere, multiplisere, dele, hjelp)
- ✅ **Resultatbehandling** og formatert utdata
- ✅ **Omfattende feilhåndtering**

- ✅ **Ren, dokumentert kode** med trinnvise kommentarer

### Komme i gang med komplette eksempler

1. **Velg ditt foretrukne språk** fra tabellen ovenfor
2. **Gå gjennom den komplette eksempel-filen** for å forstå hele implementasjonen
3. **Kjør eksemplet** ved å følge instruksjonene i [`complete_examples.md`](./complete_examples.md)
4. **Endre og utvid** eksemplet for ditt spesifikke bruksområde

For detaljert dokumentasjon om kjøring og tilpasning av disse eksemplene, se: **[📖 Komplett eksemplardokumentasjon](./complete_examples.md)**

### 💡 Løsning vs. komplette eksempler

| **Løsningsmappe** | **Komplette eksempler** |
|--------------------|--------------------- |
| Full prosjektstruktur med byggfiler | Implementasjoner i enkeltfiler |
| Klar til å kjøre med avhengigheter | Fokuserte kodeeksempler |
| Produksjonslignende oppsett | Utdanningsreferanse |
| Språkspesifikt verktøy | Tverrspråklig sammenligning |

Begge tilnærmingene er verdifulle – bruk **løsningsmappen** for komplette prosjekter og **komplette eksempler** for læring og referanse.

## Viktige punkter

Nøkkelpunktene for dette kapitlet om klienter er følgende:

- Kan brukes både til å oppdage og påkalle funksjoner på serveren.
- Kan starte en server mens den selv starter (som i dette kapitlet), men klienter kan også koble til kjørende servere.
- Er en flott måte å teste serverkapasiteter på side om side med alternativer som Inspector, slik det ble beskrevet i forrige kapittel.

## Ytterligere ressurser

- [Bygge klienter i MCP](https://modelcontextprotocol.io/quickstart/client)

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.NET Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Hva skjer videre

- Neste: [Opprette en klient med en LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
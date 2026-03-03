# Lage en klient

Klienter er tilpassede applikasjoner eller skript som kommuniserer direkte med en MCP-server for å be om ressurser, verktøy og oppfordringer. I motsetning til å bruke inspektørverktøyet, som gir et grafisk grensesnitt for å samhandle med serveren, gir det å skrive din egen klient mulighet for programmatiske og automatiserte interaksjoner. Dette gjør det mulig for utviklere å integrere MCP-funksjonalitet i sine egne arbeidsflyter, automatisere oppgaver og bygge tilpassede løsninger skreddersydd til spesifikke behov.

## Oversikt

Denne leksjonen introduserer konseptet klienter innenfor Model Context Protocol (MCP)-økosystemet. Du vil lære hvordan du skriver din egen klient og får den til å koble til en MCP-server.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Forstå hva en klient kan gjøre.
- Skrive din egen klient.
- Koble til og teste klienten med en MCP-server for å sikre at den fungerer som forventet.

## Hva innebærer det å skrive en klient?

For å skrive en klient må du gjøre følgende:

- **Importere riktige biblioteker**. Du vil bruke det samme biblioteket som før, bare ulike konstruksjoner.
- **Opprette en klient**. Dette innebærer å lage en klientinstans og koble den til valgt transportmetode.
- **Bestemme hvilke ressurser som skal listes**. MCP-serveren din har ressurser, verktøy og oppfordringer; du må bestemme hvilke som skal listes.
- **Integrere klienten i en vertsapplikasjon**. Når du kjenner til serverens funksjoner, må du integrere dette i vertsapplikasjonen slik at hvis en bruker skriver inn en oppfordring eller annen kommando, blir tilsvarende serverfunksjon kalt.

Nå som vi har en overordnet forståelse av hva vi skal gjøre, la oss se på et eksempel.

### Et eksempel på en klient

La oss se på dette eksempel på en klient:

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

// List opp meldinger
const prompts = await client.listPrompts();

// Hent en melding
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List opp ressurser
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

I koden ovenfor gjør vi:

- Importerer bibliotekene
- Lager en instans av en klient og kobler den til via stdio for transport.
- Lister opp oppfordringer, ressurser og verktøy og kaller dem alle.

Der har du det, en klient som kan kommunisere med en MCP-server.

La oss bruke god tid i neste øvelse til å bryte ned hver kodebit og forklare hva som skjer.

## Øvelse: Skrive en klient

Som nevnt over, la oss gå grundig gjennom koden, og du kan gjerne kode samtidig om du vil.

### -1- Importere bibliotekene

La oss importere de biblioteker vi trenger, vi vil trenge referanser til en klient og til vår valgte transportprotokoll, stdio. stdio er en protokoll for ting som kjøres på din lokale maskin. SSE er en annen transportprotokoll vi vil vise i kommende kapitler, men det er ditt andre valg. For nå, la oss fortsette med stdio.

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

For Java vil du lage en klient som kobler til MCP-serveren fra forrige øvelse. Ved å bruke samme Java Spring Boot-prosjektstruktur fra [Komme i gang med MCP-server](../../../../03-GettingStarted/01-first-server/solution/java), opprett en ny Java-klasse kalt `SDKClient` i mappen `src/main/java/com/microsoft/mcp/sample/client/` og legg til følgende importer:

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

Du må legge til følgende avhengigheter i `Cargo.toml`-filen din.

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

La oss gå videre til opprettelse.

### -2- Oppretting av klient og transport

Vi trenger å opprette en instans av transporten og en av vår klient:

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

- Opprettet en stdio transportinstans. Legg merke til hvordan den spesifiserer kommando og argumenter for hvordan finne og starte serveren, noe vi trenger når vi lager klienten.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instansiert en klient ved å gi den navn og versjon.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Koble klienten til valgt transport.

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

I koden ovenfor har vi:

- Importert nødvendige biblioteker
- Instansiert et serverparametere-objekt som vi bruker for å kjøre serveren slik at vi kan koble til den med vår klient.
- Definert en metode `run` som kaller `stdio_client` som starter en klientøkt.
- Laget et inngangspunkt der vi gir `run` metoden til `asyncio.run`.

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

I koden ovenfor har vi:

- Importert nødvendige biblioteker.
- Opprettet en stdio transport og opprettet en klient `mcpClient`. Sistnevnte vil vi bruke for å liste opp og kalle funksjoner på MCP-serveren.

Merk at i "Arguments" kan du peke til enten *.csproj* eller til den kjørbare filen.

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
        
        // Logikken for klienten din går her
    }
}
```

I koden ovenfor har vi:

- Laget en hovedmetode som setter opp en SSE transport som peker til `http://localhost:8080` der vår MCP-server kjører.
- Opprettet en klientklasse som tar transporten som konstruktørparameter.
- I `run`-metoden lager vi en synkron MCP-klient med transporten og initialiserer forbindelsen.
- Brukt SSE (Server-Sent Events) transport som passer for HTTP-basert kommunikasjon med Java Spring Boot MCP-servere.

#### Rust

Merk at denne Rust-klienten forutsetter at serveren er et søskenprosjekt kalt "calculator-server" i samme katalog. Koden under vil starte serveren og koble til den.

```rust
async fn main() -> Result<(), RmcpError> {
    // Anta at serveren er et søskenprosjekt kalt "calculator-server" i samme katalog
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

    // TODO: List opp verktøy

    // TODO: Kall add-verktøyet med argumenter = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Liste opp serverfunksjonene

Nå har vi en klient som kan koble til om programmet kjøres. Men den lister faktisk ikke opp sine funksjoner, så la oss gjøre det:

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
# List opp tilgjengelige ressurser
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List opp tilgjengelige verktøy
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Her lister vi opp tilgjengelige ressurser, `list_resources()` og verktøy, `list_tools` og skriver dem ut.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ovenfor er et eksempel på hvordan vi kan liste opp verktøy på serveren. For hvert verktøy skriver vi deretter ut navnet.

#### Java

```java
// Liste opp og demonstrere verktøy
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Du kan også pinge serveren for å bekrefte tilkobling
client.ping();
```

I koden ovenfor har vi:

- Kalt `listTools()` for å hente alle tilgjengelige verktøy fra MCP-serveren.
- Brukt `ping()` for å verifisere at forbindelsen til serveren fungerer.
- `ListToolsResult` inneholder informasjon om alle verktøy inkludert navn, beskrivelser og inndataskjemaer.

Flott, nå har vi fanget opp alle funksjonene. Spørsmålet er når bruker vi dem? Denne klienten er ganske enkel, enkel i den forstand at vi må eksplisitt kalle funksjonene når vi vil bruke dem. I neste kapittel skal vi lage en mer avansert klient som har tilgang til sin egen store språkmodell, en LLM. For nå, la oss se hvordan vi kan kalle funksjonene på serveren:

#### Rust

I hovedfunksjonen, etter initialisering av klienten, kan vi initialisere serveren og liste noen av dens funksjoner.

```rust
// Initialiser
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List opp verktøy
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Kalle funksjoner

For å kalle funksjonene må vi sørge for at vi spesifiserer riktige argumenter og i noen tilfeller navnet på hva vi prøver å kalle.

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

I koden ovenfor:

- Leser vi en ressurs, vi kaller ressursen ved å bruke `readResource()` og spesifisere `uri`. Slik ser det sannsynligvis ut på serversiden:

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

- Kaller et verktøy, vi kaller det ved å spesifisere `name` og `arguments` slik:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Henter en oppfordring, for å hente en oppfordring kaller du `getPrompt()` med `name` og `arguments`. Serverkoden ser slik ut:

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

    og klientkoden din ser derfor slik ut for å matche det som er deklarert på serveren:

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

I koden ovenfor har vi:

- Kalt en ressurs kalt `greeting` ved å bruke `read_resource`.
- Kalt et verktøy kalt `add` med `call_tool`.

#### .NET

1. La oss legge til kode for å kalle et verktøy:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. For å skrive ut resultatet, her er noe kode for å håndtere det:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Kall forskjellige kalkulatorverktøy
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

- Kalt flere kalkulatorverktøy med `callTool()` metoden med `CallToolRequest` objekter.
- Hvert verktøykall spesifiserer verktøynavnet og et `Map` av argumenter som trengs av det verktøyet.
- Serververktøyene forventer spesifikke parameter-navn (som "a", "b" for matematiske operasjoner).
- Resultater returneres som `CallToolResult` objekter med svar fra serveren.

#### Rust

```rust
// Kall legg til-verktøyet med argumenter = {"a": 3, "b": 2}
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

Legg til følgende oppføring i din "scripts"-seksjon i *package.json*:

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

Først, sørg for at MCP-serveren kjører på `http://localhost:8080`. Deretter kjør klienten:

```bash
# Bygg prosjektet ditt
./mvnw clean compile

# Kjør klienten
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativt kan du kjøre komplett klientprosjekt som følger med i løsningsmappen `03-GettingStarted\02-client\solution\java`:

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

Her er en server du kan bruke som du må kalle via klientkoden din, prøv å legge til flere funksjoner i serveren for å gjøre den mer interessant.

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

// Legg til en dynamisk hilseneressurs
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


# Legg til en dynamisk hilsen ressurs
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

Se på dette prosjektet for å se hvordan du kan [legge til oppfordringer og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Sjekk også denne linken for hvordan man kan kalle [oppfordringer og ressurser](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

I [forrige seksjon](../../../../03-GettingStarted/01-first-server) lærte du hvordan man lager en enkel MCP-server med Rust. Du kan fortsette å bygge videre på det, eller se denne linken for flere Rust-baserte MCP-servereksempler: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Løsning

**løsningsmappen** inneholder komplette, klare-til-kjøring klientimplementasjoner som demonstrerer alle konsepter dekket i denne opplæringen. Hver løsning inkluderer både klient- og serverkode organisert i separate, selvstendige prosjekter.

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

Hver språkspesifikke løsning tilbyr:

- **Komplett klientimplementasjon** med alle funksjoner fra opplæringen
- **Arbeidende prosjektstruktur** med riktige avhengigheter og konfigurasjon
- **Bygge- og kjøre-skript** for enkel oppsett og kjøring
- **Detaljert README** med språkspesifikke instruksjoner
- **Feilhåndtering** og eksempler på resultatbehandling

### 📖 Bruke løsningene

1. **Naviger til ønsket språkmappe**:

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

3. **Eksempel på output** du bør se:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For fullstendig dokumentasjon og trinnvis veiledning, se: **[📖 Løsningsdokumentasjon](./solution/README.md)**

## 🎯 Fullstendige eksempler

Vi har levert komplette, fungerende klientimplementasjoner for alle programmeringsspråk som dekkes i denne opplæringen. Disse eksemplene viser full funksjonalitet som beskrevet ovenfor og kan brukes som referanseimplementasjoner eller startpunkter for dine egne prosjekter.

### Tilgjengelige fullstendige eksempler

| Språk   | Fil                              | Beskrivelse                                                       |
|---------|---------------------------------|------------------------------------------------------------------|
| **Java**    | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)          | Komplett Java-klient som bruker SSE-transport med omfattende feilhåndtering |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)         | Komplett C#-klient som bruker stdio-transport med automatisk serveroppstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Komplett TypeScript-klient med full MCP-protokollstøtte          |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)         | Komplett Python-klient som bruker async/await mønstre            |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)             | Komplett Rust-klient som bruker Tokio for asynkrone operasjoner  |

Hver komplett eksempel inkluderer:
- ✅ **Etablering av tilkobling** og feilhåndtering  
- ✅ **Serveroppdagelse** (verktøy, ressurser, kommandoer der det er aktuelt)  
- ✅ **Kalkulatoroperasjoner** (legg til, trekk fra, multipliser, del, hjelp)  
- ✅ **Resultatbehandling** og formatert utdata  
- ✅ **Omfattende feilhåndtering**  
- ✅ **Ren, dokumentert kode** med steg-for-steg-kommentarer  

### Komme i gang med komplette eksempler

1. **Velg ditt foretrukne språk** fra tabellen over  
2. **Gå gjennom komplett eksempel-fil** for å forstå full implementering  
3. **Kjør eksempelet** etter instruksjonene i [`complete_examples.md`](./complete_examples.md)  
4. **Modifiser og utvid** eksempelet for ditt spesifikke brukstilfelle  

For detaljert dokumentasjon om kjøring og tilpasning av disse eksemplene, se: **[📖 Komplett eksempeldokumentasjon](./complete_examples.md)**  

### 💡 Løsning vs. komplette eksempler

| **Løsningsmappe** | **Komplette eksempler** |  
|--------------------|--------------------- |  
| Full prosjektstruktur med bygge-filer | Enkel-fil implementeringer |  
| Klar til kjøring med avhengigheter | Fokuserte kodeeksempler |  
| Produksjonslignende oppsett | Pedagogisk referanse |  
| Språkspesifikke verktøy | Kryss-språk sammenligning |  

Begge tilnærminger er verdifulle – bruk **løsningsmappen** for komplette prosjekter og **komplette eksempler** for læring og referanse.  

## Viktige punkter

De viktigste punktene i dette kapitlet om klienter er følgende:  

- Kan brukes både til å oppdage og kalle funksjoner på serveren.  
- Kan starte en server samtidig som den starter selv (slik det er i dette kapittelet), men klienter kan også koble til kjørende servere.  
- Er en utmerket måte å teste ut serverfunksjonalitet ved siden av alternativer som Inspector, slik det ble beskrevet i forrige kapittel.  

## Ytterligere ressurser

- [Bygge klienter i MCP](https://modelcontextprotocol.io/quickstart/client)  

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)  
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Kalkulator](../samples/javascript/README.md)  
- [TypeScript Kalkulator](../samples/typescript/README.md)  
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)  
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)  

## Hva kommer nå

- Neste: [Opprette en klient med en LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets originale språk bør betraktes som den autoritative kilden. For viktig informasjon anbefales profesjonell menneskelig oversettelse. Vi påtar oss ikke ansvar for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Een client maken

Clients zijn aangepaste applicaties of scripts die rechtstreeks communiceren met een MCP-server om resources, tools en prompts op te vragen. In tegenstelling tot het gebruik van de inspector tool, die een grafische interface biedt om met de server te communiceren, stelt het schrijven van je eigen client je in staat om programmatic en geautomatiseerde interacties uit te voeren. Dit stelt ontwikkelaars in staat om MCP-mogelijkheden in hun eigen workflows te integreren, taken te automatiseren en aangepaste oplossingen te bouwen die zijn afgestemd op specifieke behoeften.

## Overzicht

Deze les introduceert het concept van clients binnen het Model Context Protocol (MCP) ecosysteem. Je leert hoe je je eigen client schrijft en deze verbindt met een MCP-server.

## Leerdoelen

Aan het einde van deze les zul je in staat zijn om:

- Begrijpen wat een client kan doen.
- Je eigen client te schrijven.
- Verbinden en testen van de client met een MCP-server om te zorgen dat deze naar behoren werkt.

## Wat komt er kijken bij het schrijven van een client?

Om een client te schrijven, moet je het volgende doen:

- **Importeer de juiste libraries**. Je gebruikt dezelfde library als voorheen, maar andere constructies.
- **Instantieer een client**. Dit houdt in dat je een client-instantie aanmaakt en deze verbindt met de gekozen transportmethode.
- **Bepaal welke resources je wilt weergeven**. Je MCP-server biedt resources, tools en prompts; je moet beslissen welke je wilt weergeven.
- **Integreer de client in een hostapplicatie**. Zodra je weet welke mogelijkheden de server heeft, moet je deze integreren in je hostapplicatie zodat wanneer een gebruiker een prompt of ander commando invoert, de bijbehorende serverfunctie wordt aangeroepen.

Nu we op hoofdlijnen begrijpen wat we gaan doen, bekijken we het volgende voorbeeld.

### Een voorbeeldclient

Laten we eens kijken naar deze voorbeeldclient:

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

// Lijst prompts
const prompts = await client.listPrompts();

// Haal een prompt op
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Lijst bronnen
const resources = await client.listResources();

// Lees een bron
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Roep een tool aan
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

In de bovenstaande code hebben we:

- De libraries geïmporteerd
- Een client instantie gemaakt en verbonden via stdio als transport.
- Prompts, resources en tools opgesomd en ze allemaal aangeroepen.

Daar heb je het, een client die met een MCP-server kan communiceren.

Laten we in de volgende oefensectie de tijd nemen om elk codefragment te ontleden en uit te leggen wat er gebeurt.

## Oefening: Een client schrijven

Zoals hierboven gezegd, nemen we de tijd om de code uit te leggen, en voel je vrij om mee te coderen als je wilt.

### -1- Importeren van libraries

Laten we de benodigde libraries importeren; we hebben verwijzingen nodig naar een client en naar ons gekozen transportprotocol, stdio. Stdio is een protocol voor zaken die lokaal op je machine draaien. SSE is een ander transportprotocol dat we in toekomstige hoofdstukken zullen tonen, maar dat is jouw andere optie. Voor nu gaan we verder met stdio.

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

Voor Java maak je een client die verbinding maakt met de MCP-server uit de vorige oefening. Met dezelfde Java Spring Boot projectstructuur van [Aan de slag met MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), maak je een nieuwe Java-klasse genaamd `SDKClient` aan in de map `src/main/java/com/microsoft/mcp/sample/client/` en voeg je de volgende imports toe:

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

Je moet de volgende dependencies toevoegen aan je `Cargo.toml` bestand.

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

Vanaf daar kun je de benodigde libraries importeren in je clientcode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Laten we verdergaan met het instantieren.

### -2- Client en transport instantieren

We moeten een instantie van het transport creëren en van onze client:

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

In de bovenstaande code hebben we:

- Een stdio transport instantie gemaakt. Let op hoe het command en args specificeert voor het vinden en opstarten van de server, wat we nodig hebben als we de client aanmaken.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Een client geïnstantieerd door deze een naam en versie te geven.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- De client verbonden met het gekozen transport.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Maak serverparameters voor stdio-verbinding
server_params = StdioServerParameters(
    command="mcp",  # Uitvoerbaar bestand
    args=["run", "server.py"],  # Optionele opdrachtregelargumenten
    env=None,  # Optionele omgevingsvariabelen
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiseer de verbinding
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

In de bovenstaande code hebben we:

- De benodigde libraries geïmporteerd
- Een server parameters object geïnstantieerd om de server te kunnen draaien zodat we er met onze client op kunnen verbinden.
- Een methode `run` gedefinieerd die `stdio_client` aanroept, die een clientsessie start.
- Een entry point gemaakt waar we de `run` methode aan `asyncio.run` meegeven.

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

In de bovenstaande code hebben we:

- De benodigde libraries geïmporteerd.
- Een stdio transport gemaakt en een client `mcpClient` gemaakt. Dit gebruiken we om functies op de MCP-server op te sommen en aan te roepen.

Let op, bij "Arguments" kun je wijzen naar de *.csproj* of naar het uitvoerbare bestand.

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
        
        // Je cliëntlogica gaat hier
    }
}
```

In de bovenstaande code hebben we:

- Een main-methode gemaakt die een SSE transport opzet dat wijst naar `http://localhost:8080` waar onze MCP-server zal draaien.
- Een clientklasse gemaakt die het transport als constructorparameter gebruikt.
- In de `run` methode een synchrone MCP client gemaakt met het transport en verbinding geïnitialiseerd.
- Het SSE (Server-Sent Events) transport gebruikt, dat geschikt is voor HTTP-gebaseerde communicatie met Java Spring Boot MCP-servers.

#### Rust

Let op dat deze Rust client ervan uitgaat dat de server een "calculator-server" sibling-project is in dezelfde map. De onderstaande code start de server en maakt verbinding.

```rust
async fn main() -> Result<(), RmcpError> {
    // Ga ervan uit dat de server een zusterproject is genaamd "calculator-server" in dezelfde map
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

    // TODO: Initialiseren

    // TODO: Lijst hulpmiddelen

    // TODO: Roep add tool aan met argumenten = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- De serverfuncties opsommen

Nu hebben we een client die verbinding kan maken als het programma wordt uitgevoerd. Echter, hij somt de functies nog niet op, laten we dat doen:

#### TypeScript

```typescript
// Lijst met prompts
const prompts = await client.listPrompts();

// Lijst met bronnen
const resources = await client.listResources();

// lijst met hulpmiddelen
const tools = await client.listTools();
```

#### Python

```python
# Lijst van beschikbare bronnen
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Lijst van beschikbare gereedschappen
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Hier sommen we beschikbare resources op via `list_resources()` en tools via `list_tools` en printen ze uit.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Bovenstaand is een voorbeeld hoe we tools op de server kunnen opsommen. Voor elke tool printen we zijn naam.

#### Java

```java
// Lijst en demonstreer tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Je kunt de server ook pingen om de verbinding te verifiëren
client.ping();
```

In de bovenstaande code hebben we:

- `listTools()` aangeroepen om alle beschikbare tools van de MCP-server op te halen.
- `ping()` gebruikt om te verificeren dat de verbinding met de server werkt.
- De `ListToolsResult` bevat informatie over alle tools, inclusief namen, beschrijvingen en input-schema's.

Prima, nu we alle functies hebben gehaald, de vraag is wanneer gebruiken we ze? Deze client is vrij eenvoudig, simpel gezegd moeten we de functies expliciet aanroepen wanneer we ze willen gebruiken. In het volgende hoofdstuk maken we een geavanceerdere client met toegang tot een eigen groot taalmodel (LLM). Voor nu, laten we kijken hoe we serverfuncties kunnen aanroepen:

#### Rust

In de main functie, na het initialiseren van de client, kunnen we de server initialiseren en enkele functies opsommen.

```rust
// Initialiseren
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Lijst gereedschappen
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Functies aanroepen

Om functies aan te roepen moeten we zeker zijn van de juiste argumenten en in sommige gevallen de naam van hetgeen we willen aanroepen specificeren.

#### TypeScript

```typescript

// Lees een bron
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Roep een tool aan
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// oproep prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

In de bovenstaande code hebben we:

- Een resource gelezen, we roepen de resource aan met `readResource()` en specificeren `uri`. Dit ziet er serverkant waarschijnlijk zo uit:

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

    Onze `uri` waarde `file://example.txt` komt overeen met `file://{name}` op de server. `example.txt` wordt daarmee toegewezen aan `name`.

- Een tool aangeroepen, dat doen we door `name` en `arguments` te specificeren zo:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Prompt opgevraagd, om een prompt te krijgen roep je `getPrompt()` met `name` en `arguments` aan. De servercode ziet er zo uit:

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

    en de resulterende clientcode ziet er dus zo uit, overeenkomstig met wat er op de server is gedeclareerd:

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
# Lees een bron
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Roep een hulpmiddel aan
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

In de bovenstaande code hebben we:

- Een resource `greeting` aangeroepen via `read_resource`.
- Een tool `add` aangeroepen via `call_tool`.

#### .NET

1. Laten we wat code toevoegen om een tool aan te roepen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Hieronder wat code om het resultaat uit te printen:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Roep verschillende rekenmachinehulpmiddelen aan
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

In de bovenstaande code hebben we:

- Meerdere calculator tools aangeroepen via de `callTool()` methode met `CallToolRequest` objecten.
- Elke tool-aanroep specificeert de toolnaam en een `Map` van argumenten die de tool nodig heeft.
- De server tools verwachten specifieke parameter namen (zoals "a", "b" voor wiskundige bewerkingen).
- Resultaten worden geretourneerd als `CallToolResult` objecten met de respons van de server.

#### Rust

```rust
// Roep add tool aan met argumenten = {"a": 3, "b": 2}
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

### -5- De client uitvoeren

Om de client uit te voeren typ je de volgende opdracht in de terminal:

#### TypeScript

Voeg de volgende entry toe aan de "scripts" sectie in *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Roep de client aan met de volgende opdracht:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Zorg eerst dat je MCP-server draait op `http://localhost:8080`. Voer daarna de client uit:

```bash
# Bouw je project
./mvnw clean compile

# Start de client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Als alternatief kun je het complete clientproject uitvoeren dat is meegeleverd in de oplossingsmap `03-GettingStarted\02-client\solution\java`:

```bash
# Navigeer naar de oplossingsmap
cd 03-GettingStarted/02-client/solution/java

# Bouw en voer de JAR uit
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Opdracht

In deze opdracht gebruik je wat je hebt geleerd bij het maken van een client, maar maak je je eigen client.

Hier is een server die je kunt gebruiken en die je via je clientcode moet aanroepen. Kijk of je meer functies aan de server kunt toevoegen om het interessanter te maken.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Maak een MCP-server aan
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Voeg een opteltool toe
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Voeg een dynamische begroetingsbron toe
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

// Begin met het ontvangen van berichten op stdin en het versturen van berichten op stdout

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

# Maak een MCP-server
mcp = FastMCP("Demo")


# Voeg een optellingstool toe
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Voeg een dynamische begroetingsbron toe
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

Zie dit project om te kijken hoe je [prompts en resources kunt toevoegen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Check ook deze link voor hoe je [prompts en resources kunt aanroepen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

In de [vorige sectie](../../../../03-GettingStarted/01-first-server) heb je geleerd hoe je een eenvoudige MCP-server met Rust maakt. Je kunt daarop verder bouwen of deze link bekijken voor meer Rust-gebaseerde MCP-server voorbeelden: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Oplossing

De **oplossingsmap** bevat complete, kant-en-klare clientimplementaties die alle in deze tutorial besproken concepten demonstreren. Elke oplossing bevat zowel client- als servercode georganiseerd in aparte, zelfstandige projecten.

### 📁 Oplossingsstructuur

De oplossingsdirectory is georganiseerd per programmeertaal:

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

### 🚀 Wat elke oplossing bevat

Elke taalspecifieke oplossing biedt:

- **Complete clientimplementatie** met alle functies uit de tutorial
- **Werkende projectstructuur** met correcte dependencies en configuratie
- **Build- en runscripts** voor eenvoudige setup en uitvoering
- **Gedetailleerde README** met taalspecifieke instructies
- **Foutafhandeling** en voorbeelden van resultaatverwerking

### 📖 Gebruik van de oplossingen

1. **Navigeer naar de map van je voorkeurs-taal**:

   ```bash
   cd solution/typescript/    # Voor TypeScript
   cd solution/java/          # Voor Java
   cd solution/python/        # Voor Python
   cd solution/dotnet/        # Voor .NET
   ```

2. **Volg de instructies in de README** in elke map voor:
   - Dependencies installeren
   - Het project bouwen
   - De client uitvoeren

3. **Voorbeeld output** die je hoort te zien:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Voor volledige documentatie en stapsgewijze instructies, zie: **[📖 Oplossingsdocumentatie](./solution/README.md)**

## 🎯 Complete voorbeelden

We hebben complete, werkende clientimplementaties geleverd voor alle in deze tutorial behandelde programmeertalen. Deze voorbeelden demonstreren de volledige functionaliteit zoals hierboven beschreven en kunnen worden gebruikt als referentieimplementaties of startpunten voor je eigen projecten.

### Beschikbare complete voorbeelden

| Taal   | Bestand                      | Beschrijving                                                   |
|--------|-----------------------------|----------------------------------------------------------------|
| **Java**      | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)           | Complete Java client gebruikmakend van SSE transport met uitgebreide foutafhandeling  |
| **C#**        | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)           | Complete C# client gebruikmakend van stdio transport met automatische serverstart    |
| **TypeScript**| [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts)   | Complete TypeScript client met volledige MCP protocol ondersteuning                   |
| **Python**    | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)           | Complete Python client gebruikmakend van async/await patronen                         |
| **Rust**      | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)               | Complete Rust client gebruikmakend van Tokio voor async operaties                     |

Elk compleet voorbeeld bevat:

- ✅ **Verbindingsopbouw** en foutafhandeling
- ✅ **Server ontdekking** (tools, resources, prompts waar van toepassing)
- ✅ **Calculator-bewerkingen** (optellen, aftrekken, vermenigvuldigen, delen, hulp)
- ✅ **Resultaatverwerking** en geformatteerde output
- ✅ **Uitgebreide foutafhandeling**

- ✅ **Schone, gedocumenteerde code** met stapsgewijze commentaren  

### Aan de slag met complete voorbeelden  

1. **Kies je voorkeurs taal** uit de bovenstaande tabel  
2. **Bekijk het complete voorbeeldbestand** om de volledige implementatie te begrijpen  
3. **Voer het voorbeeld uit** volgens de instructies in [`complete_examples.md`](./complete_examples.md)  
4. **Pas het voorbeeld aan en breid het uit** voor jouw specifieke gebruik  

Voor gedetailleerde documentatie over het uitvoeren en aanpassen van deze voorbeelden, zie: **[📖 Complete Voorbeelden Documentatie](./complete_examples.md)**  

### 💡 Oplossing versus complete voorbeelden  

| **Oplossingsmap** | **Complete Voorbeelden** |
|--------------------|--------------------- |
| Volledige projectstructuur met buildbestanden | Implementaties in één bestand |
| Klaar om te draaien met afhankelijkheden | Gericht op codevoorbeelden |
| Productie-achtige setup | Educatieve referentie |
| Taal-specifieke tooling | Vergelijking tussen talen |

Beide benaderingen zijn waardevol - gebruik de **oplossingsmap** voor complete projecten en de **complete voorbeelden** voor leren en referentie.  

## Belangrijkste leerpunten  

De belangrijkste leerpunten van dit hoofdstuk over clients zijn:  

- Kunnen zowel gebruikt worden om functies op de server te ontdekken als aan te roepen.  
- Kunnen een server starten terwijl ze zelf opstarten (zoals in dit hoofdstuk), maar clients kunnen ook verbinding maken met al draaiende servers.  
- Zijn een geweldige manier om servermogelijkheden te testen naast alternatieven zoals de Inspector, zoals beschreven in het vorige hoofdstuk.  

## Aanvullende bronnen  

- [Clients bouwen in MCP](https://modelcontextprotocol.io/quickstart/client)  

## Voorbeelden  

- [Java Calculator](../samples/java/calculator/README.md)  
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## Wat is de volgende stap  

- Volgende: [Een client maken met een LLM](../03-llm-client/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
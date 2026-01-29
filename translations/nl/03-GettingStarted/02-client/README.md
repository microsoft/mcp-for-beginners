# Een client maken

Clients zijn aangepaste applicaties of scripts die rechtstreeks communiceren met een MCP-server om bronnen, tools en prompts op te vragen. In tegenstelling tot het gebruik van de inspectietool, die een grafische interface biedt voor interactie met de server, stelt het schrijven van je eigen client je in staat om programmatische en geautomatiseerde interacties te hebben. Dit stelt ontwikkelaars in staat om MCP-functionaliteiten te integreren in hun eigen workflows, taken te automatiseren en aangepaste oplossingen te bouwen die zijn afgestemd op specifieke behoeften.

## Overzicht

Deze les introduceert het concept van clients binnen het Model Context Protocol (MCP)-ecosysteem. Je leert hoe je je eigen client schrijft en deze verbindt met een MCP-server.

## Leerdoelen

Aan het einde van deze les kun je:

- Begrijpen wat een client kan doen.
- Je eigen client schrijven.
- De client verbinden met en testen op een MCP-server om ervoor te zorgen dat deze naar verwachting werkt.

## Wat komt er kijken bij het schrijven van een client?

Om een client te schrijven, moet je het volgende doen:

- **De juiste bibliotheken importeren**. Je gebruikt dezelfde bibliotheek als voorheen, maar met andere constructies.
- **Een client instantiëren**. Dit houdt in dat je een clientinstantie maakt en deze verbindt met de gekozen transportmethode.
- **Bepalen welke bronnen je wilt weergeven**. Je MCP-server bevat bronnen, tools en prompts; je moet beslissen welke je wilt weergeven.
- **De client integreren in een hostapplicatie**. Zodra je de mogelijkheden van de server kent, moet je deze integreren in je hostapplicatie, zodat wanneer een gebruiker een prompt of andere opdracht invoert, de bijbehorende serverfunctie wordt aangeroepen.

Nu we op hoog niveau begrijpen wat we gaan doen, laten we eens naar een voorbeeld kijken.

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

In de bovenstaande code hebben we:

- De bibliotheken geïmporteerd.
- Een instantie van een client gemaakt en deze verbonden met stdio als transport.
- Prompts, bronnen en tools weergegeven en ze allemaal aangeroepen.

Daar heb je het, een client die kan communiceren met een MCP-server.

Laten we in de volgende oefeningsectie de tijd nemen om elk codefragment op te splitsen en uit te leggen wat er gebeurt.

## Oefening: Een client schrijven

Zoals hierboven vermeld, laten we de tijd nemen om de code uit te leggen, en programmeer vooral mee als je dat wilt.

### -1- De bibliotheken importeren

Laten we de bibliotheken importeren die we nodig hebben. We hebben referenties nodig naar een client en naar ons gekozen transportprotocol, stdio. Stdio is een protocol voor dingen die bedoeld zijn om lokaal op je machine te draaien. SSE is een ander transportprotocol dat we in toekomstige hoofdstukken zullen laten zien, maar dat is je andere optie. Voor nu gaan we verder met stdio.

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

Voor Java maak je een client die verbinding maakt met de MCP-server uit de vorige oefening. Gebruik dezelfde Java Spring Boot-projectstructuur van [Aan de slag met MCP-server](../../../../03-GettingStarted/01-first-server/solution/java), maak een nieuwe Java-klasse genaamd `SDKClient` in de map `src/main/java/com/microsoft/mcp/sample/client/` en voeg de volgende imports toe:

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

Je moet de volgende afhankelijkheden toevoegen aan je `Cargo.toml`-bestand.

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

Van daaruit kun je de benodigde bibliotheken importeren in je clientcode.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Laten we doorgaan met het instantiëren.

### -2- Client en transport instantiëren

We moeten een instantie maken van het transport en van onze client:

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

- Een stdio-transportinstantie gemaakt. Let op hoe het de opdracht en argumenten specificeert om de server te vinden en op te starten, aangezien we dat moeten doen bij het maken van de client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Een client geïnstantieerd door het een naam en versie te geven.

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

In de bovenstaande code hebben we:

- De benodigde bibliotheken geïmporteerd.
- Een serverparametersobject geïnstantieerd, aangezien we dit zullen gebruiken om de server te draaien zodat we verbinding kunnen maken met onze client.
- Een methode `run` gedefinieerd die op zijn beurt `stdio_client` aanroept, wat een clientsessie start.
- Een ingangspunt gemaakt waar we de `run`-methode aan `asyncio.run` doorgeven.

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

In de bovenstaande code hebben we:

- De benodigde bibliotheken geïmporteerd.
- Een stdio-transport gemaakt en een client `mcpClient` gemaakt. Deze laatste zullen we gebruiken om functies op de MCP-server weer te geven en aan te roepen.

Let op: in "Arguments" kun je verwijzen naar de *.csproj* of naar het uitvoerbare bestand.

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

In de bovenstaande code hebben we:

- Een hoofdprogramma gemaakt dat een SSE-transport instelt dat verwijst naar `http://localhost:8080`, waar onze MCP-server zal draaien.
- Een clientklasse gemaakt die het transport als constructorparameter neemt.
- In de `run`-methode een synchrone MCP-client gemaakt met behulp van het transport en de verbinding geïnitialiseerd.
- SSE (Server-Sent Events) transport gebruikt, wat geschikt is voor HTTP-gebaseerde communicatie met Java Spring Boot MCP-servers.

#### Rust

Merk op dat deze Rust-client ervan uitgaat dat de server een verwant project is genaamd "calculator-server" in dezelfde map. De onderstaande code zal de server starten en ermee verbinden.

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

### -3- De functies van de server weergeven

Nu hebben we een client die verbinding kan maken als het programma wordt uitgevoerd. Het geeft echter nog niet zijn functies weer, dus laten we dat nu doen:

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

Hier geven we de beschikbare bronnen weer met `list_resources()` en tools met `list_tools` en printen ze uit.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Hierboven staat een voorbeeld van hoe we de tools op de server kunnen weergeven. Voor elke tool printen we vervolgens de naam.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

In de bovenstaande code hebben we:

- `listTools()` aangeroepen om alle beschikbare tools van de MCP-server op te halen.
- `ping()` gebruikt om te controleren of de verbinding met de server werkt.
- De `ListToolsResult` bevat informatie over alle tools, inclusief hun namen, beschrijvingen en invoerschema's.

Geweldig, nu hebben we alle functies vastgelegd. De vraag is nu: wanneer gebruiken we ze? Deze client is vrij eenvoudig, in de zin dat we de functies expliciet moeten aanroepen wanneer we ze willen gebruiken. In het volgende hoofdstuk maken we een geavanceerdere client die toegang heeft tot zijn eigen grote taalmodel (LLM). Voor nu laten we zien hoe we de functies op de server kunnen aanroepen:

#### Rust

In de hoofdfunctie, na het initialiseren van de client, kunnen we de server initialiseren en enkele van zijn functies weergeven.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Functies aanroepen

Om de functies aan te roepen, moeten we ervoor zorgen dat we de juiste argumenten specificeren en in sommige gevallen de naam van wat we proberen aan te roepen.

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

In de bovenstaande code hebben we:

- Een bron gelezen door `readResource()` aan te roepen en `uri` te specificeren. Dit is hoe het er waarschijnlijk uitziet aan de serverzijde:

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

    Onze `uri`-waarde `file://example.txt` komt overeen met `file://{name}` op de server. `example.txt` wordt toegewezen aan `name`.

- Een tool aangeroepen door de `name` en de `arguments` te specificeren, zoals:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Een prompt opgehaald door `getPrompt()` aan te roepen met `name` en `arguments`. De servercode ziet er als volgt uit:

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

    En je resulterende clientcode ziet er daarom als volgt uit om overeen te komen met wat op de server is gedeclareerd:

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

In de bovenstaande code hebben we:

- Een bron genaamd `greeting` aangeroepen met `read_resource`.
- Een tool genaamd `add` aangeroepen met `call_tool`.

#### .NET

1. Laten we wat code toevoegen om een tool aan te roepen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Om het resultaat af te drukken, hier is wat code om dat te verwerken:

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

In de bovenstaande code hebben we:

- Meerdere rekenkundige tools aangeroepen met de methode `callTool()` en `CallToolRequest`-objecten.
- Elke toolaanroep specificeert de toolnaam en een `Map` van argumenten die door die tool vereist zijn.
- De servertools verwachten specifieke parameternamen (zoals "a", "b" voor wiskundige bewerkingen).
- Resultaten worden geretourneerd als `CallToolResult`-objecten die de respons van de server bevatten.

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

### -5- De client uitvoeren

Om de client uit te voeren, typ je de volgende opdracht in de terminal:

#### TypeScript

Voeg de volgende invoer toe aan je "scripts"-sectie in *package.json*:

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

Zorg er eerst voor dat je MCP-server draait op `http://localhost:8080`. Voer vervolgens de client uit:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Als alternatief kun je het volledige clientproject uitvoeren dat wordt geleverd in de oplossingsmap `03-GettingStarted\02-client\solution\java`:

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

## Opdracht

In deze opdracht gebruik je wat je hebt geleerd bij het maken van een client, maar maak je een eigen client.

Hier is een server die je kunt gebruiken en die je moet aanroepen via je clientcode. Kijk of je meer functies aan de server kunt toevoegen om het interessanter te maken.

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

Zie dit project om te zien hoe je [prompts en bronnen kunt toevoegen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Bekijk ook deze link voor hoe je [prompts en bronnen kunt aanroepen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

In de [vorige sectie](../../../../03-GettingStarted/01-first-server) heb je geleerd hoe je een eenvoudige MCP-server maakt met Rust. Je kunt hierop voortbouwen of deze link bekijken voor meer Rust-gebaseerde MCP-servervoorbeelden: [MCP Server Voorbeelden](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Oplossing

De **oplossingsmap** bevat complete, kant-en-klare clientimplementaties die alle concepten uit deze tutorial demonstreren. Elke oplossing bevat zowel client- als servercode, georganiseerd in afzonderlijke, zelfstandige projecten.

### 📁 Structuur van de oplossing

De oplossingsmap is georganiseerd per programmeertaal:

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

Elke taal-specifieke oplossing biedt:

- **Volledige clientimplementatie** met alle functies uit de tutorial.
- **Werkende projectstructuur** met de juiste afhankelijkheden en configuratie.
- **Build- en uitvoerscripts** voor eenvoudige installatie en uitvoering.
- **Gedetailleerde README** met taal-specifieke instructies.
- **Voorbeelden van foutafhandeling** en resultaatverwerking.

### 📖 Gebruik van de oplossingen

1. **Navigeer naar de map van je voorkeurstaal**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Volg de README-instructies** in elke map voor:
   - Het installeren van afhankelijkheden.
   - Het bouwen van het project.
   - Het uitvoeren van de client.

3. **Voorbeeldoutput** die je zou moeten zien:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Voor volledige documentatie en stapsgewijze instructies, zie: **[📖 Oplossingsdocumentatie](./solution/README.md)**

## 🎯 Volledige Voorbeelden

We hebben volledige, werkende clientimplementaties geleverd voor alle programmeertalen die in deze tutorial worden behandeld. Deze voorbeelden demonstreren de volledige functionaliteit zoals hierboven beschreven en kunnen worden gebruikt als referentie-implementaties of startpunten voor je eigen projecten.

### Beschikbare Volledige Voorbeelden

| Taal       | Bestand                              | Beschrijving                                                                 |
|------------|--------------------------------------|-----------------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Volledige Java-client met SSE-transport en uitgebreide foutafhandeling     |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Volledige C#-client met stdio-transport en automatische serverstart         |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Volledige TypeScript-client met volledige MCP-protocolondersteuning        |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Volledige Python-client met async/await-patronen                           |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Volledige Rust-client met Tokio voor asynchrone bewerkingen                |
Elke complete voorbeeld bevat:

- ✅ **Verbinding maken** en foutafhandeling
- ✅ **Server ontdekken** (tools, bronnen, prompts waar van toepassing)
- ✅ **Rekenmachine-operaties** (optellen, aftrekken, vermenigvuldigen, delen, hulp)
- ✅ **Resultaatverwerking** en geformatteerde output
- ✅ **Uitgebreide foutafhandeling**
- ✅ **Schone, gedocumenteerde code** met stapsgewijze opmerkingen

### Aan de slag met complete voorbeelden

1. **Kies je voorkeurstaal** uit de tabel hierboven
2. **Bekijk het complete voorbeeldbestand** om de volledige implementatie te begrijpen
3. **Voer het voorbeeld uit** volgens de instructies in [`complete_examples.md`](./complete_examples.md)
4. **Pas het voorbeeld aan en breid het uit** voor jouw specifieke gebruikssituatie

Voor gedetailleerde documentatie over het uitvoeren en aanpassen van deze voorbeelden, zie: **[📖 Complete Voorbeelden Documentatie](./complete_examples.md)**

### 💡 Oplossing vs. Complete Voorbeelden

| **Oplossingsmap** | **Complete Voorbeelden** |
|--------------------|--------------------- |
| Volledige projectstructuur met build-bestanden | Implementaties in één bestand |
| Klaar om te draaien met afhankelijkheden | Gericht op codevoorbeelden |
| Productie-achtige setup | Educatieve referentie |
| Taal-specifieke tooling | Taaloverschrijdende vergelijking |

Beide benaderingen zijn waardevol - gebruik de **oplossingsmap** voor volledige projecten en de **complete voorbeelden** voor leren en referentie.

## Belangrijke inzichten

De belangrijkste inzichten voor dit hoofdstuk over clients zijn:

- Kunnen worden gebruikt om zowel functies op de server te ontdekken als aan te roepen.
- Kunnen een server starten terwijl ze zelf starten (zoals in dit hoofdstuk), maar clients kunnen ook verbinding maken met draaiende servers.
- Zijn een geweldige manier om servermogelijkheden te testen naast alternatieven zoals de Inspector, zoals beschreven in het vorige hoofdstuk.

## Aanvullende bronnen

- [Clients bouwen in MCP](https://modelcontextprotocol.io/quickstart/client)

## Voorbeelden

- [Java Rekenmachine](../samples/java/calculator/README.md)
- [.Net Rekenmachine](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rekenmachine](../samples/javascript/README.md)
- [TypeScript Rekenmachine](../samples/typescript/README.md)
- [Python Rekenmachine](../../../../03-GettingStarted/samples/python)
- [Rust Rekenmachine](../../../../03-GettingStarted/samples/rust)

## Wat komt hierna

- Volgende: [Een client maken met een LLM](../03-llm-client/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
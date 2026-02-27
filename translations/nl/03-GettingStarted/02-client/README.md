# Een client maken

Clients zijn aangepaste applicaties of scripts die rechtstreeks communiceren met een MCP-server om bronnen, tools en prompts op te vragen. In tegenstelling tot het gebruik van het inspectiegereedschap, dat een grafische interface biedt om met de server te communiceren, maakt het schrijven van je eigen client programmatic en geautomatiseerde interacties mogelijk. Hierdoor kunnen ontwikkelaars MCP-functionaliteiten integreren in hun eigen workflows, taken automatiseren en oplossingen op maat bouwen die zijn afgestemd op specifieke behoeften.

## Overzicht

Deze les introduceert het concept van clients binnen het Model Context Protocol (MCP)-ecosysteem. Je leert hoe je je eigen client schrijft en verbinding maakt met een MCP-server.

## Leerdoelen

Aan het einde van deze les kun je:

- Begrijpen wat een client kan doen.
- Je eigen client schrijven.
- Verbinden en de client testen met een MCP-server om er zeker van te zijn dat deze werkt zoals verwacht.

## Wat komt er kijken bij het schrijven van een client?

Om een client te schrijven, moet je het volgende doen:

- **Importeer de juiste bibliotheken**. Je gebruikt dezelfde bibliotheek als eerder, maar met andere constructies.
- **Instantieer een client**. Dit houdt in dat je een clientinstantie maakt en deze verbindt met de gekozen transportmethode.
- **Bepaal welke resources je wilt weergeven**. Je MCP-server heeft resources, tools en prompts, je moet beslissen welke je wilt tonen.
- **Integreer de client in een hostapplicatie**. Zodra je de mogelijkheden van de server kent, moet je deze integreren in je hostapplicatie zodat wanneer een gebruiker een prompt of andere opdracht invoert, de overeenkomstige serverfunctionaliteit wordt aangeroepen.

Nu we op hoofdlijnen begrijpen wat we gaan doen, bekijken we hieronder een voorbeeld.

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

// Lijst met prompts
const prompts = await client.listPrompts();

// Haal een prompt op
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Lijst met bronnen
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

In bovenstaande code:

- Importeren we de bibliotheken
- Maken we een client instance en verbinden deze via stdio als transport.
- Lijsten we prompts, resources en tools en roepen ze allemaal aan.

Dat is het, een client die kan communiceren met een MCP-server.

Laten we de volgende oefensectie de tijd nemen om elk codefragment te ontleden en uit te leggen wat er gebeurt.

## Oefening: Een client schrijven

Zoals gezegd, laten we de tijd nemen om de code uit te leggen. Codeer gerust mee als je dat wilt.

### -1- Importeer de bibliotheken

Laten we de benodigde bibliotheken importeren. We hebben referenties nodig naar een client en ons gekozen transportprotocol, stdio. stdio is een protocol voor zaken die op je lokale machine draaien. SSE is een ander transportprotocol dat we in toekomstige hoofdstukken zullen behandelen, maar dat is je andere optie. Voor nu gaan we verder met stdio.

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

Voor Java maak je een client die verbinding maakt met de MCP-server uit de vorige oefening. Gebruik dezelfde Java Spring Boot projectstructuur van [Aan de slag met MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), maak een nieuwe Java-klasse genaamd `SDKClient` in de map `src/main/java/com/microsoft/mcp/sample/client/` en voeg de volgende imports toe:

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

Vervolgens kun je de benodigde bibliotheken importeren in je clientcode.

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

We moeten een instantie van het transport maken en van onze client:

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

In bovenstaande code hebben we:

- Een stdio transport instantie gemaakt. Let op hoe het commando en args specificeert om de server te vinden en starten omdat dat iets is wat we moeten doen bij het creëren van de client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Een client geïnstantieerd door een naam en versie op te geven.

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
    args=["run", "server.py"],  # Optionele commandoregelargumenten
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

In bovenstaande code hebben we:

- De benodigde bibliotheken geïmporteerd.
- Een serverparameters-object geïnstantieerd omdat we dit gebruiken om de server te draaien zodat we er met onze client op kunnen aansluiten.
- Een methode `run` gedefinieerd die op zijn beurt `stdio_client` aanroept om een client-sessie te starten.
- Een entrypoint gemaakt waar we de `run` methode aan `asyncio.run` doorgeven.

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

In bovenstaande code hebben we:

- De benodigde bibliotheken geïmporteerd.
- Een stdio transport gemaakt en een client `mcpClient` geïnstantieerd. Dit laatste gebruiken we om functies op de MCP-server te lijsten en aan te roepen.

Let op: bij "Arguments" kun je ofwel naar de *.csproj* verwijzen of naar de uitvoerbare applicatie.

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
        
        // Uw clientlogica gaat hier
    }
}
```

In bovenstaande code hebben we:

- Een main-methode gemaakt die een SSE transport instelt dat wijst naar `http://localhost:8080` waar onze MCP-server draait.
- Een clientklasse gemaakt die het transport via de constructor als parameter ontvangt.
- In de `run`-methode maken we een synchrone MCP-client met het transport en initialiseren de verbinding.
- SSE (Server-Sent Events) transport gebruikt wat geschikt is voor HTTP-gebaseerde communicatie met Java Spring Boot MCP-servers.

#### Rust

Let op: deze Rust client gaat ervan uit dat de server een sibling-project is met de naam "calculator-server" in dezelfde directory. De onderstaande code start de server en maakt verbinding ermee.

```rust
async fn main() -> Result<(), RmcpError> {
    // Ga ervan uit dat de server een sibling-project is genaamd "calculator-server" in dezelfde map
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

### -3- Serverfuncties lijst opvragen

We hebben nu een client die verbinding kan maken wanneer het programma wordt uitgevoerd. Echter, deze lijst niet daadwerkelijk de functies, dus laten we dat nu doen:

#### TypeScript

```typescript
// Lijst met prompts
const prompts = await client.listPrompts();

// Lijst met bronnen
const resources = await client.listResources();

// lijst met tools
const tools = await client.listTools();
```

#### Python

```python
# Beschikbare bronnen weergeven
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Beschikbare tools weergeven
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Hier lijst je de beschikbare resources op met `list_resources()` en tools met `list_tools` en print ze uit.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Bovenstaand is een voorbeeld hoe we tools op de server kunnen tonen. Voor elke tool printen we de naam uit.

#### Java

```java
// Lijst en demonstreer hulpmiddelen
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Je kunt ook de server pingen om de verbinding te controleren
client.ping();
```

In bovenstaande code hebben we:

- `listTools()` aangeroepen om alle beschikbare tools van de MCP-server op te halen.
- `ping()` gebruikt om te verifiëren dat de verbinding met de server werkt.
- De `ListToolsResult` bevat informatie over alle tools inclusief namen, omschrijvingen en input schemas.

Prima, we hebben nu alle functies opgehaald. De vraag is nu wanneer we ze gebruiken? Deze client is vrij simpel omdat we de functies expliciet moeten aanroepen wanneer we ze willen gebruiken. In het volgende hoofdstuk maken we een geavanceerdere client die toegang heeft tot een eigen large language model (LLM). Voor nu kijken we hoe we functies op de server aanroepen:

#### Rust

In de main-functie, na het initialiseren van de client, kunnen we de server initialiseren en enkele functies lijst ophalen.

```rust
// Initialiseren
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Hulpmiddelen weergeven
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Functies aanroepen

Om functies aan te roepen moeten we juiste argumenten opgeven en in sommige gevallen de naam van wat we aanroepen.

#### TypeScript

```typescript

// Lees een bron
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Roep een hulpmiddel aan
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// voer prompt uit
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

In bovenstaande code:

- Lezen we een resource, we roepen de resource aan via `readResource()` door `uri` op te geven. Zo ziet het er waarschijnlijk uit aan de serverzijde:

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

    Onze `uri` waarde `file://example.txt` komt overeen met `file://{name}` op de server. `example.txt` wordt toegewezen aan `name`.

- Roepen we een tool aan, dat gaan we doen door zijn `name` en `arguments` op te geven zoals volgt:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Ophalen van een prompt: om een prompt op te halen, roep je `getPrompt()` aan met `name` en `arguments`. De servercode ziet er zo uit:

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

    en jouw resulterende clientcode ziet er daarom zo uit om te matchen met wat op de server is gedefinieerd:

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

In bovenstaande code hebben we:

- Een resource aangeroepen genaamd `greeting` met `read_resource`.
- Een tool aangeroepen `add` met `call_tool`.

#### .NET

1. Laten we code toevoegen om een tool aan te roepen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Om het resultaat uit te printen, hier wat code om dat te behandelen:

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

In bovenstaande code hebben we:

- Meerdere calculator-tools aangeroepen met de methode `callTool()` en `CallToolRequest` objecten.
- Elke toolaanroep bepaalt de toolnaam en een `Map` van argumenten die de tool vereist.
- De servertools verwachten specifieke parameter namen (zoals "a", "b" voor wiskundige bewerkingen).
- Resultaten worden geretourneerd als `CallToolResult` objecten met de serverrespons.

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

Typ in de terminal het volgende commando om de client uit te voeren:

#### TypeScript

Voeg de volgende entry toe aan je "scripts"-sectie in *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Roep de client aan met het volgende commando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Zorg er eerst voor dat je MCP-server draait op `http://localhost:8080`. Run dan de client:

```bash
# Bouw je project
./mvnw clean compile

# Voer de client uit
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Als alternatief kun je het complete clientproject uitvoeren dat in de solution-map `03-GettingStarted\02-client\solution\java` staat:

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

Gebruik bij deze opdracht wat je geleerd hebt over het maken van een client en bouw je eigen client.

Hier is een server die je kunt gebruiken via je clientcode. Kijk of je meer functies kunt toevoegen aan de server om het interessanter te maken.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Maak een MCP-server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Voeg een optellingstool toe
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

// Begin met het ontvangen van berichten op stdin en het verzenden van berichten op stdout

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

Bekijk dit project om te zien hoe je [prompts en resources kunt toevoegen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Check ook deze link over hoe je [prompts en resources aanroept](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

In de [vorige sectie](../../../../03-GettingStarted/01-first-server) heb je geleerd hoe je een eenvoudige MCP-server maakt met Rust. Je kunt daarop doorgaan bouwen of deze link bekijken voor meer MCP-servervoorbeelden gebaseerd op Rust: [MCP Server Voorbeelden](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Oplossing

De **oplossingsmap** bevat complete, direct uitvoerbare clientimplementaties die alle concepten uit deze tutorial demonstreren. Elke oplossing bevat zowel client- als servercode georganiseerd in aparte, zelfstandige projecten.

### 📁 Structuur oplossing

De map met de oplossing is georganiseerd per programmeertaal:

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

Elke taal-specifieke oplossing bevat:

- **Complete clientimplementatie** met alle features uit de tutorial
- **Werkende projectstructuur** met juiste dependencies en configuratie
- **Build- en uitvoerscripts** voor makkelijke setup en uitvoering
- **Uitgebreide README** met taal-specifieke instructies
- **Foutafhandeling** en voorbeeld van resultaatverwerking

### 📖 Het gebruik van de oplossingen

1. **Navigeer naar de map van je voorkeurstaal**:

   ```bash
   cd solution/typescript/    # Voor TypeScript
   cd solution/java/          # Voor Java
   cd solution/python/        # Voor Python
   cd solution/dotnet/        # Voor .NET
   ```

2. **Volg de README-instructies** in elke map voor:
   - Het installeren van dependencies
   - Het bouwen van het project
   - Het uitvoeren van de client

3. **Voorbeelduitvoer** die je zou moeten zien:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Voor volledige documentatie en stapsgewijze instructies, zie: **[📖 Oplossingsdocumentatie](./solution/README.md)**

## 🎯 Complete Voorbeelden

We hebben complete, werkende clientimplementaties verstrekt voor alle in deze tutorial behandelde programmeertalen. Deze voorbeelden demonstreren de volledige hierboven beschreven functionaliteit en kunnen worden gebruikt als referentie of startpunt voor je eigen projecten.

### Beschikbare complete voorbeelden

| Taal | Bestand | Beschrijving |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Complete Java client met SSE transport en uitgebreide foutafhandeling |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Complete C# client met stdio transport en automatische serverstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Complete TypeScript client met volledige MCP protocolondersteuning |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Complete Python client met async/await patronen |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Complete Rust client met Tokio voor asynchrone operaties |

Elke complete voorbeeld bevat:
- ✅ **Verbindingsopbouw** en foutafhandeling  
- ✅ **Serverontdekking** (tools, bronnen, prompts waar van toepassing)  
- ✅ **Rekenmachinebewerkingen** (optellen, aftrekken, vermenigvuldigen, delen, hulp)  
- ✅ **Resultaatverwerking** en geformatteerde uitvoer  
- ✅ **Uitgebreide foutafhandeling**  
- ✅ **Schone, gedocumenteerde code** met stapsgewijze opmerkingen  

### Aan de slag met volledige voorbeelden  

1. **Kies je voorkeursprogramma taal** uit de bovenstaande tabel  
2. **Bekijk het volledige voorbeeldbestand** om de volledige implementatie te begrijpen  
3. **Voer het voorbeeld uit** volgens de instructies in [`complete_examples.md`](./complete_examples.md)  
4. **Pas het voorbeeld aan en breid het uit** voor jouw specifieke use case  

Voor gedetailleerde documentatie over het draaien en aanpassen van deze voorbeelden, zie: **[📖 Complete Examples Documentation](./complete_examples.md)**  

### 💡 Oplossing vs. Volledige voorbeelden  

| **Oplossingsmap**              | **Volledige voorbeelden**  |  
|-------------------------------|----------------------------|  
| Volledige projectstructuur met build-bestanden | Implementaties in één bestand |  
| Klaar om uit te voeren met afhankelijkheden | Gericht op codevoorbeelden |  
| Productie-achtige opzet         | Educatieve referentie       |  
| Taal-specifieke tooling         | Taaloverstijgende vergelijking  |  

Beide benaderingen zijn waardevol – gebruik de **oplossingsmap** voor complete projecten en de **volledige voorbeelden** voor leren en referentie.  

## Belangrijkste punten  

De belangrijkste punten van dit hoofdstuk over clients zijn:  

- Kunnen worden gebruikt om zowel functies op de server te ontdekken als op te roepen.  
- Kunnen een server starten terwijl ze zelf opstarten (zoals in dit hoofdstuk), maar clients kunnen ook verbinding maken met draaiende servers.  
- Zijn een geweldige manier om servermogelijkheden te testen naast alternatieven zoals de Inspector, zoals beschreven in het vorige hoofdstuk.  

## Aanvullende bronnen  

- [Clients bouwen in MCP](https://modelcontextprotocol.io/quickstart/client)  

## Voorbeelden  

- [Java rekenmachine](../samples/java/calculator/README.md)  
- [.Net rekenmachine](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript rekenmachine](../samples/javascript/README.md)  
- [TypeScript rekenmachine](../samples/typescript/README.md)  
- [Python rekenmachine](../../../../03-GettingStarted/samples/python)  
- [Rust rekenmachine](../../../../03-GettingStarted/samples/rust)  

## Wat is de volgende stap  

- Volgende: [Een client maken met een LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
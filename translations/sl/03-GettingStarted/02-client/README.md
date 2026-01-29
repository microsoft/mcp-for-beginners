# Ustvarjanje odjemalca

Odjemalci so prilagojene aplikacije ali skripte, ki neposredno komunicirajo z MCP strežnikom za zahtevanje virov, orodij in pozivov. Za razliko od uporabe orodja za pregledovanje, ki ponuja grafični vmesnik za interakcijo s strežnikom, pisanje lastnega odjemalca omogoča programatične in avtomatizirane interakcije. To razvijalcem omogoča integracijo zmogljivosti MCP v njihove delovne procese, avtomatizacijo nalog in gradnjo prilagojenih rešitev, prilagojenih specifičnim potrebam.

## Pregled

Ta lekcija uvaja koncept odjemalcev v ekosistemu Model Context Protocol (MCP). Naučili se boste, kako napisati svojega odjemalca in ga povezati z MCP strežnikom.

## Cilji učenja

Do konca te lekcije boste sposobni:

- Razumeti, kaj lahko odjemalec naredi.
- Napisati svojega odjemalca.
- Povezati in preizkusiti odjemalca z MCP strežnikom, da zagotovite, da slednji deluje, kot je pričakovano.

## Kaj vključuje pisanje odjemalca?

Za pisanje odjemalca morate storiti naslednje:

- **Uvoziti ustrezne knjižnice**. Uporabili boste isto knjižnico kot prej, le drugačne konstrukte.
- **Ustvariti odjemalca**. To vključuje ustvarjanje primerka odjemalca in povezavo z izbrano transportno metodo.
- **Odločiti se, katere vire našteti**. Vaš MCP strežnik ima vire, orodja in pozive, vi pa morate odločiti, katere želite našteti.
- **Integrirati odjemalca v gostiteljsko aplikacijo**. Ko poznate zmogljivosti strežnika, morate to integrirati v svojo gostiteljsko aplikacijo, tako da se ob vnosu poziva ali drugega ukaza ustrezna funkcija strežnika sproži.

Zdaj, ko na visoki ravni razumemo, kaj bomo storili, si poglejmo primer.

### Primer odjemalca

Poglejmo si primer odjemalca:

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

V zgornji kodi smo:

- Uvozili knjižnice.
- Ustvarili primerek odjemalca in ga povezali z uporabo stdio za transport.
- Našteli pozive, vire in orodja ter jih vse sprožili.

Tukaj imate odjemalca, ki lahko komunicira z MCP strežnikom.

V naslednjem razdelku vaj si vzemimo čas in razčlenimo vsak del kode ter razložimo, kaj se dogaja.

## Vaja: Pisanje odjemalca

Kot rečeno zgoraj, si vzemimo čas za razlago kode, in če želite, lahko kodirate zraven.

### -1- Uvoz knjižnic

Uvozimo knjižnice, ki jih potrebujemo. Potrebovali bomo reference na odjemalca in na izbrani transportni protokol, stdio. stdio je protokol za stvari, ki naj bi se izvajale na vašem lokalnem računalniku. SSE je drug transportni protokol, ki ga bomo pokazali v prihodnjih poglavjih, vendar je to vaša druga možnost. Za zdaj pa nadaljujmo s stdio.

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

Za Java boste ustvarili odjemalca, ki se poveže z MCP strežnikom iz prejšnje vaje. Z uporabo iste strukture projekta Java Spring Boot iz [Začetek z MCP strežnikom](../../../../03-GettingStarted/01-first-server/solution/java) ustvarite nov razred Java z imenom `SDKClient` v mapi `src/main/java/com/microsoft/mcp/sample/client/` in dodajte naslednje uvoze:

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

Dodati boste morali naslednje odvisnosti v datoteko `Cargo.toml`.

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

Od tam lahko uvozite potrebne knjižnice v svojo odjemalsko kodo.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Nadaljujmo z ustvarjanjem primerka.

### -2- Ustvarjanje odjemalca in transporta

Ustvariti moramo primerek transporta in primerek našega odjemalca:

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

V zgornji kodi smo:

- Ustvarili primerek stdio transporta. Opazite, kako določa ukaz in argumente za to, kako najti in zagnati strežnik, saj je to nekaj, kar bomo morali storiti, ko ustvarimo odjemalca.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Ustvarili odjemalca z imenom in različico.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Povezali odjemalca z izbranim transportom.

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

V zgornji kodi smo:

- Uvozili potrebne knjižnice.
- Ustvarili objekt parametrov strežnika, saj ga bomo uporabili za zagon strežnika, da se lahko povežemo z njim z našim odjemalcem.
- Določili metodo `run`, ki nato pokliče `stdio_client`, kar začne sejo odjemalca.
- Ustvarili vstopno točko, kjer metodi `run` podamo `asyncio.run`.

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

V zgornji kodi smo:

- Uvozili potrebne knjižnice.
- Ustvarili stdio transport in odjemalca `mcpClient`. Slednjega bomo uporabili za naštevanje in sprožanje funkcij na MCP strežniku.

Opomba: v "Arguments" lahko pokažete bodisi na *.csproj* bodisi na izvršljivo datoteko.

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

V zgornji kodi smo:

- Ustvarili glavno metodo, ki nastavi SSE transport, ki kaže na `http://localhost:8080`, kjer bo naš MCP strežnik deloval.
- Ustvarili razred odjemalca, ki transport sprejme kot parameter konstruktorja.
- V metodi `run` ustvarili sinhroni MCP odjemalec z uporabo transporta in inicializirali povezavo.
- Uporabili SSE (Server-Sent Events) transport, ki je primeren za komunikacijo na osnovi HTTP z Java Spring Boot MCP strežniki.

#### Rust

Ta Rust odjemalec predvideva, da je strežnik sorodni projekt z imenom "calculator-server" v isti mapi. Spodnja koda bo zagnala strežnik in se povezala z njim.

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

### -3- Naštevanje funkcij strežnika

Zdaj imamo odjemalca, ki se lahko poveže, če se program zažene. Vendar pa dejansko ne našteva svojih funkcij, zato to storimo naslednje:

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

Tukaj naštejemo razpoložljive vire, `list_resources()` in orodja, `list_tools` ter jih izpišemo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Zgornji primer prikazuje, kako lahko naštejemo orodja na strežniku. Za vsako orodje nato izpišemo njegovo ime.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

V zgornji kodi smo:

- Poklicali `listTools()`, da dobimo vsa razpoložljiva orodja iz MCP strežnika.
- Uporabili `ping()`, da preverimo, ali povezava s strežnikom deluje.
- `ListToolsResult` vsebuje informacije o vseh orodjih, vključno z njihovimi imeni, opisi in shemami vhodnih podatkov.

Odlično, zdaj smo zajeli vse funkcije. Zdaj pa se postavlja vprašanje, kdaj jih uporabimo? Ta odjemalec je precej preprost, preprost v smislu, da bomo morali funkcije izrecno poklicati, ko jih želimo. V naslednjem poglavju bomo ustvarili bolj napreden odjemalec, ki bo imel dostop do lastnega velikega jezikovnega modela (LLM). Za zdaj pa poglejmo, kako lahko sprožimo funkcije na strežniku:

#### Rust

V glavni funkciji, po inicializaciji odjemalca, lahko inicializiramo strežnik in naštejemo nekatere njegove funkcije.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Sprožanje funkcij

Za sprožanje funkcij moramo zagotoviti, da določimo pravilne argumente in v nekaterih primerih ime funkcije, ki jo želimo sprožiti.

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

V zgornji kodi smo:

- Prebrali vir, poklicali smo vir z uporabo `readResource()` in določili `uri`. Tukaj je, kako bi to najverjetneje izgledalo na strežniški strani:

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

    Naša vrednost `uri` `file://example.txt` ustreza `file://{name}` na strežniku. `example.txt` bo preslikan na `name`.

- Poklicali orodje, poklicali smo ga z določitvijo njegovega `name` in njegovih `arguments`, kot sledi:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Pridobili poziv, za pridobitev poziva pokličete `getPrompt()` z `name` in `arguments`. Strežniška koda izgleda takole:

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

    in vaša odjemalska koda bo zato izgledala takole, da se ujema s tem, kar je deklarirano na strežniku:

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

V zgornji kodi smo:

- Poklicali vir z imenom `greeting` z uporabo `read_resource`.
- Sprožili orodje z imenom `add` z uporabo `call_tool`.

#### .NET

1. Dodajmo nekaj kode za klic orodja:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Za izpis rezultata, tukaj je nekaj kode za obdelavo tega:

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

V zgornji kodi smo:

- Poklicali več orodij kalkulatorja z uporabo metode `callTool()` z objekti `CallToolRequest`.
- Vsak klic orodja določa ime orodja in `Map` argumentov, ki jih to orodje zahteva.
- Strežniška orodja pričakujejo specifična imena parametrov (kot sta "a", "b" za matematične operacije).
- Rezultati so vrnjeni kot objekti `CallToolResult`, ki vsebujejo odgovor strežnika.

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

### -5- Zagon odjemalca

Za zagon odjemalca vnesite naslednji ukaz v terminal:

#### TypeScript

Dodajte naslednji vnos v razdelek "scripts" v *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Pokličite odjemalca z naslednjim ukazom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najprej se prepričajte, da vaš MCP strežnik deluje na `http://localhost:8080`. Nato zaženite odjemalca:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativno lahko zaženete celoten projekt odjemalca, ki je na voljo v mapi rešitve `03-GettingStarted\02-client\solution\java`:

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

## Naloga

V tej nalogi boste uporabili, kar ste se naučili pri ustvarjanju odjemalca, in ustvarili svojega odjemalca.

Tukaj je strežnik, ki ga lahko uporabite in ga morate poklicati prek svoje odjemalske kode. Poskusite dodati več funkcij strežniku, da bo bolj zanimiv.

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

Oglejte si ta projekt, da vidite, kako lahko [dodate pozive in vire](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Prav tako preverite to povezavo za klic [pozivov in virov](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [prejšnjem razdelku](../../../../03-GettingStarted/01-first-server) ste se naučili, kako ustvariti preprost MCP strežnik z Rust. Lahko nadaljujete z gradnjo na tem ali preverite to povezavo za več primerov MCP strežnikov na osnovi Rust: [Primeri MCP strežnikov](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rešitev

**Mapa rešitev** vsebuje popolne, pripravljene za zagon implementacije odjemalcev, ki prikazujejo vse koncepte, obravnavane v tem priročniku. Vsaka rešitev vključuje tako kodo odjemalca kot strežnika, organizirano v ločene, samostojne projekte.

### 📁 Struktura rešitve

Mapa rešitev je organizirana po programskih jezikih:

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

### 🚀 Kaj vključuje vsaka rešitev

Vsaka jezikovno specifična rešitev ponuja:

- **Popolno implementacijo odjemalca** z vsemi funkcijami iz priročnika.
- **Delujočo strukturo projekta** z ustreznimi odvisnostmi in konfiguracijo.
- **Skripte za gradnjo in zagon** za enostavno nastavitev in izvedbo.
- **Podroben README** z jezikovno specifičnimi navodili.
- **Primeri obdelave napak** in obdelave rezultatov.

### 📖 Uporaba rešitev

1. **Pomaknite se do mape za želeni jezik**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Sledite navodilom v README** v vsaki mapi za:
   - Namestitev odvisnosti.
   - Gradnjo projekta.
   - Zagon odjemalca.

3. **Primer izpisa**, ki ga morate videti:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za popolno dokumentacijo in navodila po korakih si oglejte: **[📖 Dokumentacija rešitve](./solution/README.md)**

## 🎯 Popolni primeri

Ponudili smo popolne, delujoče implementacije odjemalcev za vse programske jezike, obravnavane v tem priročniku. Ti primeri prikazujejo celotno funkcionalnost, opisano zgoraj, in jih lahko uporabite kot referenčne implementacije ali izhodišča za svoje projekte.

### Na voljo popolni primeri

| Jezik | Datoteka | Opis |
|-------|---------|------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Popoln Java odjemalec z uporabo SSE transporta z obsežno obdelavo napak |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Popoln C# odjemalec z uporabo stdio transporta z avtomatskim zagonom strežnika |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Popoln TypeScript odjemalec s polno podporo MCP protokolu |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Popoln Python odjemalec z uporabo vzorcev async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Popoln Rust odjemalec z uporabo Tokio za asinhrone operacije |
Vsak popoln primer vključuje:

- ✅ **Vzpostavitev povezave** in obravnavo napak
- ✅ **Iskanje strežnika** (orodja, viri, pozivi, kjer je primerno)
- ✅ **Operacije kalkulatorja** (seštevanje, odštevanje, množenje, deljenje, pomoč)
- ✅ **Obdelavo rezultatov** in formatiran izpis
- ✅ **Celovito obravnavo napak**
- ✅ **Čisto, dokumentirano kodo** s komentarji po korakih

### Začetek z popolnimi primeri

1. **Izberite želeni jezik** iz zgornje tabele
2. **Preglejte datoteko s popolnim primerom**, da razumete celotno implementacijo
3. **Zaženite primer** po navodilih v [`complete_examples.md`](./complete_examples.md)
4. **Prilagodite in razširite** primer za vaš specifičen primer uporabe

Za podrobno dokumentacijo o zagonu in prilagajanju teh primerov si oglejte: **[📖 Dokumentacija popolnih primerov](./complete_examples.md)**

### 💡 Rešitev vs. Popolni primeri

| **Mapa rešitev** | **Popolni primeri** |
|--------------------|--------------------- |
| Celotna struktura projekta z gradbenimi datotekami | Implementacije v eni datoteki |
| Pripravljeno za zagon z odvisnostmi | Osredotočeni primeri kode |
| Nastavitev podobna produkciji | Izobraževalni referenčni primer |
| Orodja specifična za jezik | Primerjava med jeziki |

Oba pristopa sta dragocena - uporabite **mapo rešitev** za celotne projekte in **popolne primere** za učenje in referenco.

## Ključne ugotovitve

Ključne ugotovitve tega poglavja o klientih so naslednje:

- Lahko se uporabljajo za odkrivanje in izvajanje funkcij na strežniku.
- Lahko zaženejo strežnik med svojim zagonom (kot v tem poglavju), vendar se lahko klienti povežejo tudi z že delujočimi strežniki.
- So odličen način za testiranje zmogljivosti strežnika poleg alternativ, kot je Inspector, ki je bil opisan v prejšnjem poglavju.

## Dodatni viri

- [Gradnja klientov v MCP](https://modelcontextprotocol.io/quickstart/client)

## Primeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Kaj sledi

- Naprej: [Ustvarjanje klienta z LLM](../03-llm-client/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
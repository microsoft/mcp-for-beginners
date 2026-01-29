# Kliendi loomine

Kliendid on kohandatud rakendused või skriptid, mis suhtlevad otse MCP serveriga, et taotleda ressursse, tööriistu ja juhiseid. Erinevalt inspektori tööriista kasutamisest, mis pakub graafilist liidest serveriga suhtlemiseks, võimaldab oma kliendi kirjutamine programmeerimist ja automatiseeritud suhtlust. See võimaldab arendajatel integreerida MCP võimalusi oma töövoogudesse, automatiseerida ülesandeid ja luua kohandatud lahendusi vastavalt konkreetsetele vajadustele.

## Ülevaade

See õppetund tutvustab klientide kontseptsiooni Model Context Protocol (MCP) ökosüsteemis. Õpid, kuidas kirjutada oma klienti ja ühendada see MCP serveriga.

## Õpieesmärgid

Selle õppetunni lõpuks oskad:

- Mõista, mida klient teha saab.
- Kirjutada oma klienti.
- Ühendada ja testida klienti MCP serveriga, et veenduda, et viimane töötab ootuspäraselt.

## Mis on kliendi kirjutamise protsessis oluline?

Kliendi kirjutamiseks tuleb teha järgmist:

- **Impordi õiged teegid**. Kasutad sama teeki nagu varem, kuid erinevaid konstruktsioone.
- **Loo kliendi eksemplar**. See hõlmab kliendi eksemplari loomist ja selle ühendamist valitud transpordimeetodiga.
- **Otsusta, milliseid ressursse loetleda**. Sinu MCP serveril on ressursid, tööriistad ja juhised, pead otsustama, milliseid loetleda.
- **Integreeri klient hostrakendusse**. Kui tead serveri võimalusi, pead selle integreerima oma hostrakendusse, et kasutaja sisestatud juhis või muu käsk käivitaks vastava serveri funktsiooni.

Nüüd, kui oleme üldisel tasemel aru saanud, mida teeme, vaatame järgmisena näidet.

### Näide kliendist

Vaatame seda näidet kliendist:

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

Eelnevas koodis:

- Impordime teegid.
- Loome kliendi eksemplari ja ühendame selle stdio transpordiga.
- Loetleme juhised, ressursid ja tööriistad ning käivitame need kõik.

Seal see on – klient, mis suudab MCP serveriga suhelda.

Võtame järgmises harjutuse osas aega, et iga koodilõik lahti seletada ja selgitada, mis toimub.

## Harjutus: Kliendi kirjutamine

Nagu öeldud, võtame aega koodi selgitamiseks ja soovi korral võid kaasa kodeerida.

### -1- Teekide importimine

Impordime vajalikud teegid, vajame viiteid kliendile ja valitud transpordiprotokollile, stdio. Stdio on protokoll, mis on mõeldud kohalikul masinal töötamiseks. SSE on teine transpordiprotokoll, mida näitame tulevastes peatükkides, kuid see on sinu teine valik. Praegu jätkame stdio-ga.

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

Java puhul loome kliendi, mis ühendub eelmise harjutuse MCP serveriga. Kasutades sama Java Spring Boot projekti struktuuri kui [MCP serveriga alustamine](../../../../03-GettingStarted/01-first-server/solution/java), loo uus Java klass nimega `SDKClient` kaustas `src/main/java/com/microsoft/mcp/sample/client/` ja lisa järgmised impordid:

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

Pead lisama järgmised sõltuvused oma `Cargo.toml` faili.

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

Sealt saad importida vajalikud teegid oma kliendikoodi.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Liigume edasi eksemplari loomise juurde.

### -2- Kliendi ja transpordi eksemplari loomine

Peame looma transpordi ja kliendi eksemplari:

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

Eelnevas koodis oleme:

- Loonud stdio transpordi eksemplari. Pane tähele, kuidas see määrab käsu ja argumendid serveri leidmiseks ja käivitamiseks, kuna see on midagi, mida peame tegema kliendi loomisel.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Loonud kliendi, andes sellele nime ja versiooni.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Ühendanud kliendi valitud transpordiga.

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

Eelnevas koodis oleme:

- Imporditud vajalikud teegid.
- Loonud serveri parameetrite objekti, kuna kasutame seda serveri käivitamiseks, et saaksime sellega oma kliendi kaudu ühendust võtta.
- Määratlenud meetodi `run`, mis omakorda kutsub `stdio_client`, mis käivitab kliendi sessiooni.
- Loonud sisenemispunkti, kus anname `run` meetodi `asyncio.run`-ile.

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

Eelnevas koodis oleme:

- Imporditud vajalikud teegid.
- Loonud stdio transpordi ja kliendi `mcpClient`. Viimane on midagi, mida kasutame MCP serveri funktsioonide loetlemiseks ja käivitamiseks.

Pane tähele, et "Arguments" osas saad viidata kas *.csproj* failile või käivitatavale failile.

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

Eelnevas koodis oleme:

- Loonud peameetodi, mis seadistab SSE transpordi, osutades `http://localhost:8080`, kus meie MCP server töötab.
- Loonud kliendiklassi, mis võtab transpordi konstruktoriparameetrina.
- Meetodis `run` loome sünkroonse MCP kliendi, kasutades transporti ja algatame ühenduse.
- Kasutanud SSE-d (Server-Sent Events) transporti, mis sobib HTTP-põhiseks suhtluseks Java Spring Boot MCP serveritega.

#### Rust

Pane tähele, et see Rusti klient eeldab, et server on sama kataloogi "calculator-server" nimeline projekt. Allolev kood käivitab serveri ja ühendub sellega.

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

### -3- Serveri funktsioonide loetlemine

Nüüd on meil klient, mis saab ühendust luua, kui programm käivitatakse. Kuid see ei loetle tegelikult oma funktsioone, seega teeme seda järgmisena:

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

Siin loetleme saadaval olevad ressursid, `list_resources()` ja tööriistad, `list_tools` ning prindime need välja.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ülaltoodud näide näitab, kuidas saame serveri tööriistu loetleda. Iga tööriista puhul prindime välja selle nime.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Eelnevas koodis oleme:

- Kutsunud `listTools()`, et saada kõik saadaval olevad tööriistad MCP serverist.
- Kasutanud `ping()`, et kontrollida, kas ühendus serveriga töötab.
- `ListToolsResult` sisaldab teavet kõigi tööriistade kohta, sealhulgas nende nimed, kirjeldused ja sisendiskeemid.

Suurepärane, nüüd oleme kõik funktsioonid kaardistanud. Küsimus on, millal me neid kasutame? Noh, see klient on üsna lihtne, lihtne selles mõttes, et peame funktsioone selgesõnaliselt kutsuma, kui neid vajame. Järgmises peatükis loome arenenuma kliendi, millel on juurdepääs oma suurele keelemudelile (LLM). Praegu aga vaatame, kuidas saame serveri funktsioone käivitada:

#### Rust

Põhifunktsioonis, pärast kliendi algatamist, saame serveri algatada ja mõned selle funktsioonid loetleda.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funktsioonide käivitamine

Funktsioonide käivitamiseks peame tagama, et määrame õiged argumendid ja mõnel juhul ka käivitatava funktsiooni nime.

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

Eelnevas koodis oleme:

- Lugemisressurssi, kutsume ressursi, kasutades `readResource()` ja määrates `uri`. Siin on, kuidas see tõenäoliselt serveri poolel välja näeb:

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

    Meie `uri` väärtus `file://example.txt` vastab `file://{name}` serveris. `example.txt` kaardistatakse `name`-le.

- Tööriista kutsumine, kutsume seda, määrates selle `name` ja `arguments` järgmiselt:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Juhise saamine, juhise saamiseks kutsume `getPrompt()` koos `name` ja `arguments`. Serveri kood näeb välja järgmiselt:

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

    ja sinu kliendikood näeb seega välja järgmiselt, et vastata serveris deklareeritule:

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

Eelnevas koodis oleme:

- Kutsunud ressursi nimega `greeting`, kasutades `read_resource`.
- Käivitanud tööriista nimega `add`, kasutades `call_tool`.

#### .NET

1. Lisame koodi tööriista kutsumiseks:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Tulemuse printimiseks on siin kood, mis seda käsitleb:

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

Eelnevas koodis oleme:

- Kutsunud mitmeid kalkulaatori tööriistu, kasutades `callTool()` meetodit koos `CallToolRequest` objektidega.
- Iga tööriista kutse määrab tööriista nime ja vajalike argumentide `Map`-i.
- Serveri tööriistad eeldavad konkreetseid parameetrite nimesid (näiteks "a", "b" matemaatiliste operatsioonide jaoks).
- Tulemused tagastatakse `CallToolResult` objektidena, mis sisaldavad serveri vastust.

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

### -5- Kliendi käivitamine

Kliendi käivitamiseks sisesta terminali järgmine käsk:

#### TypeScript

Lisa järgmine kirje oma *package.json* "scripts" sektsiooni:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kutsu klienti järgmise käsuga:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Esmalt veendu, et sinu MCP server töötab aadressil `http://localhost:8080`. Seejärel käivita klient:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatiivselt saad käivitada täieliku kliendiprojekti, mis on lahenduskaustas `03-GettingStarted\02-client\solution\java`:

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

## Ülesanne

Selles ülesandes kasutad õpitut kliendi loomiseks, kuid lood oma kliendi.

Siin on server, mida saad kasutada ja mida pead oma kliendikoodiga kutsuma. Proovi lisada serverile rohkem funktsioone, et see oleks huvitavam.

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

Vaata seda projekti, et näha, kuidas [lisada juhiseid ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Samuti vaata seda linki, et näha, kuidas kutsuda [juhiseid ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Eelmises osas (../01-first-server) õppisid, kuidas luua lihtsat MCP serverit Rustiga. Saad seda edasi arendada või vaadata seda linki, et näha rohkem Rusti-põhiseid MCP serveri näiteid: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lahendus

**Lahenduskaust** sisaldab täielikke, käivitatavaid kliendi implementatsioone, mis demonstreerivad kõiki selles juhendis käsitletud kontseptsioone. Iga lahendus sisaldab nii kliendi kui serveri koodi, mis on organiseeritud eraldi, iseseisvates projektides.

### 📁 Lahenduse struktuur

Lahenduse kataloog on organiseeritud programmeerimiskeelte järgi:

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

### 🚀 Mida iga lahendus sisaldab

Iga keelespetsiifiline lahendus pakub:

- **Täielikku kliendi implementatsiooni** kõigi juhendis käsitletud funktsioonidega.
- **Töötavat projektistruktuuri** koos õige sõltuvuste ja konfiguratsiooniga.
- **Ehitus- ja käivitusskripte** lihtsaks seadistamiseks ja käivitamiseks.
- **Üksikasjalikku README-d** keelespetsiifiliste juhistega.
- **Vigade käsitlemise** ja tulemuste töötlemise näiteid.

### 📖 Lahenduste kasutamine

1. **Liigu oma eelistatud keele kausta**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Järgi README juhiseid** igas kaustas:
   - Sõltuvuste installimine
   - Projekti ehitamine
   - Kliendi käivitamine

3. **Näidisväljund**, mida peaksid nägema:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Täieliku dokumentatsiooni ja samm-sammult juhiste jaoks vaata: **[📖 Lahenduse dokumentatsioon](./solution/README.md)**

## 🎯 Täielikud näited

Oleme pakkunud täielikke, töötavaid kliendi implementatsioone kõigi selles juhendis käsitletud programmeerimiskeelte jaoks. Need näited demonstreerivad kogu ülaltoodud funktsionaalsust ja neid saab kasutada viiteimplementatsioonidena või lähtepunktidena oma projektide jaoks.

### Saadaval olevad täielikud näited

| Keel | Fail | Kirjeldus |
|------|------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Täielik Java klient, mis kasutab SSE transporti koos põhjaliku vigade käsitlemisega |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Täielik C# klient, mis kasutab stdio transporti koos automaatse serveri käivitamisega |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Täielik TypeScript klient, millel on täielik MCP protokolli tugi |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Täielik Python klient, mis kasutab async/await mustreid |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Täielik Rust klient, mis kasutab Tokio't asünkroonsete operatsioonide jaoks |

Iga täielik näide sisaldab:

- ✅ **Ühenduse loomist** ja vigade käsitlemist
- ✅ **Serveri avastamist** (tööriistad, ressursid, juhised, kus kohaldatav)
- ✅ **Kalkulaatori operatsioone** (liitmine, lahutamine, korrutamine, jagamine, abi)
- ✅ **Tulemuste töötlemine** ja vormindatud väljund
- ✅ **Põhjalik vigade käsitlemine**
- ✅ **Puhas, dokumenteeritud kood** koos samm-sammuliste kommentaaridega

### Alustamine täielike näidetega

1. **Vali oma eelistatud keel** ülaltoodud tabelist
2. **Vaata täielikku näidiste faili**, et mõista kogu rakendust
3. **Käivita näide** järgides juhiseid failis [`complete_examples.md`](./complete_examples.md)
4. **Muuda ja laienda** näidet vastavalt oma konkreetsele kasutusjuhule

Üksikasjaliku dokumentatsiooni saamiseks nende näidiste käivitamise ja kohandamise kohta vaata: **[📖 Täielike näidiste dokumentatsioon](./complete_examples.md)**

### 💡 Lahendus vs. Täielikud näited

| **Lahenduse kaust** | **Täielikud näited** |
|--------------------|--------------------- |
| Täielik projekti struktuur koos ehitusfailidega | Ühe faili rakendused |
| Valmis käivitamiseks koos sõltuvustega | Keskendunud koodinäited |
| Tootmiskeskkonna sarnane seadistus | Hariduslik viide |
| Keelespetsiifilised tööriistad | Erinevate keelte võrdlus |

Mõlemad lähenemised on väärtuslikud - kasuta **lahenduse kausta** täielike projektide jaoks ja **täielikke näiteid** õppimiseks ja viitamiseks.

## Olulised punktid

Selle peatüki olulised punktid klientide kohta on järgmised:

- Saab kasutada nii serveri funktsioonide avastamiseks kui ka nende käivitamiseks.
- Saab käivitada serveri samal ajal, kui see ise käivitub (nagu selles peatükis), kuid kliendid võivad ühenduda ka juba töötavate serveritega.
- On suurepärane viis serveri võimaluste testimiseks, lisaks alternatiividele nagu Inspector, mida kirjeldati eelmises peatükis.

## Lisamaterjalid

- [Klientide loomine MCP-s](https://modelcontextprotocol.io/quickstart/client)

## Näidised

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Mis edasi?

- Järgmine: [Kliendi loomine LLM-iga](../03-llm-client/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
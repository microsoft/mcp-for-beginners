# Kliendi loomine

Kliendid on kohandatud rakendused või skriptid, mis suhtlevad otse MCP serveriga, et taotleda ressursse, tööriistu ja promte. Erinevalt inspektori tööriista kasutamisest, mis pakub graafilist liidest serveriga suhtlemiseks, võimaldab oma kliendi kirjutamine programmeeritud ja automatiseeritud suhtlust. See võimaldab arendajatel integreerida MCP võimekust omaenda töövoogudesse, automatiseerida ülesandeid ning luua spetsiifilistele vajadustele kohandatud lahendusi.

## Ülevaade

See õppetund tutvustab kliente Model Context Protocoli (MCP) ökosüsteemis. Õpid, kuidas kirjutada oma klient ja ühendada see MCP serveriga.

## Õpieesmärgid

Selle õppetunni lõpuks oled võimeline:

- Mõistma, mida klient suudab teha.
- Kirjutama oma kliendi.
- Ühendama ja testima klienti MCP serveriga, et veenduda selle ootuspärases töös.

## Mis on kliendi kirjutamisse kaasatud?

Kliendi kirjutamiseks tuleb teha järgmist:

- **Impordi õiged teegid.** Kasutad sama teeki nagu varem, ainult erinevaid konstruktoreid.
- **Loo kliendi eksemplar.** Selleks pead looma kliendi näite ja ühendama selle valitud transpordimeetodi kaudu.
- **Otsusta, milliseid ressursse kuvada.** Sinu MCP serveris on ressursid, tööriistad ja promtid, pead valima, milliseid näidata.
- **Integreeri klient hostrakendusse.** Kui tead serveri võimeid, integreeri need oma hostrakendusse, nii et kui kasutaja sisestab prompti või teise käsu, kutsutakse vastav serveri funktsioon.

Nüüd, kui meil on ülevaade, mida teha, vaatame allpool näiteid.

### Näite klient

Vaata seda näite klienti:

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

// Küsitluste loend
const prompts = await client.listPrompts();

// Hangi küsimus
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Ressursside loend
const resources = await client.listResources();

// Loe ressurssi
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Käivita tööriist
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Eelnevas koodis me:

- Impordime teegid
- Loome kliendi eksemplari ja ühendame selle stdio transpordi kaudu.
- Kuvame promte, ressursse ja tööriistu ning kutsume kõiki neid.

Siin see on, klient, kes saab MCP serveriga suhelda.

Võtame järgmises harjutuse osas aega ja selgitame iga kooditüki ja selle tööd.

## Harjutus: Kliendi kirjutamine

Nagu ülal mainitud, võtame aja ja selgitame koodi ning vajadusel saa ka ise kaasa kodeerida.

### -1- Teekide importimine

Impordime vajalikud teegid, meil on vaja viiteid kliendile ja valitud transpordiprotokollile, stdio-le. stdio on protokoll arvutis lokaalselt jooksvate protsesside jaoks. SSE on teine transpordivõimalus, mida näitame tulevastes peatükkides, see on alternatiiv. Seniks jätkame stdio-ga.

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

Javas lood MCP serverile ühenduva kliendi eelmise harjutuse põhjal. Kasutades sama Java Spring Boot projekti struktuuri nagu [Sissejuhatus MCP serverisse](../../../../03-GettingStarted/01-first-server/solution/java), loo uus Java klass nimega `SDKClient` kaustas `src/main/java/com/microsoft/mcp/sample/client/` ning lisa järgmised impordid:

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

Pead lisama järgmised sõltuvused failile `Cargo.toml`.

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

Seejärel saad importida vajalikud teegid oma kliendikoodi.

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

### -2- Kliendi ja transpordi loomine

Peame looma transpordi eksemplari ja kliendi eksemplari:

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

- Loonud stdio transpordi eksemplari. Märka, kuidas seal määratletakse käsk ja argumendid, kuidas server leida ja käivitada, seda peabki kliendi loomisel arvestama.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Loonud kliendi, andes talle nime ja versiooni.

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

# Loo serveri parameetrid stdio ühenduseks
server_params = StdioServerParameters(
    command="mcp",  # Käivitatav fail
    args=["run", "server.py"],  # Valikulised käsurea argumendid
    env=None,  # Valikulised keskkonnamuutujad
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Algata ühendus
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Eelnevas koodis oleme:

- Impordinud vajalikud teegid
- Loonud serveri parameetrite objekti, et server käivitada ja sellega kliendiga ühendada.
- Määratlenud meetodi `run`, mis kutsub `stdio_client`-i, alustades kliendi seanssi.
- Loonud sisendi (entry point) kasutades `asyncio.run`.

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

Eelnevas koodis oleme:

- Impordinud vajalikud teegid.
- Loonud stdio transpordi ja kliendi nimega `mcpClient`. Seda klienti kasutame, et kuvada ja kutsuda MCP serveri funktsioone.

Märkus: "Arguments" võib viidata kas *.csproj* failile või käivitatavale failile.

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
        
        // Teie kliendi loogika läheb siia
    }
}
```

Eelnevas koodis oleme:

- Loonud main meetodi, mis seadistab SSE transpordi aadressile `http://localhost:8080`, kus MCP server töötab.
- Loonud kliendi klassi, mis võtab transpordi konstruktoriparameetrina.
- `run` meetodis loome süntroonse MCP kliendi transpordiga ja algatame ühenduse.
- Kasutame SSE (Server-Sent Events) transporti, mis sobib HTTP-põhisteks suhtlusteks Java Spring Boot MCP serveritega.

#### Rust

Pane tähele, see Rust klient eeldab, et server on timmisood "calculator-server" samas kataloogis. Kood allpool käivitab serveri ja ühendub sellega.

```rust
async fn main() -> Result<(), RmcpError> {
    // Eeldage, et server on sama kataloogi õdeprojekt nimega "calculator-server"
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

    // TODO: Algatada

    // TODO: Tööriistade loendamine

    // TODO: Kutsuge tööriist add argumendiga = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Serveri omaduste kuvamine

Nüüd on meil klient, kes saab programmiga ühenduda. Kuid see ei kuva oma funktsioone, teeme selle nüüd:

#### TypeScript

```typescript
// Loetle käsud
const prompts = await client.listPrompts();

// Loetle ressursid
const resources = await client.listResources();

// loetle tööriistad
const tools = await client.listTools();
```

#### Python

```python
# Loetle saadaolevad ressursid
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Loetle saadaolevad tööriistad
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Siin kuvame olemasolevad ressursid `list_resources()` ja tööriistad `list_tools` ning trükime need välja.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ülal on näide, kuidas kuvada serveri tööriistu. Iga tööriista kohta trükime selle nime.

#### Java

```java
// Loetle ja näita tööriistu
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Võid ka serverit pingida, et kontrollida ühendust
client.ping();
```

Eelnevas koodis oleme:

- Kutsunud `listTools()`, et saada kõik saadaval olevad tööriistad MCP serverist.
- Kasutanud `ping()` ühenduse toimimise kontrollimiseks.
- `ListToolsResult` sisaldab kõigi tööriistade infot - nimed, kirjeldused, sisendi skeemid.

Suurepärane, nüüd omame kõiki funktsioone. Aga millal neid kasutada? See klient on lihtne, peame funktsioonid kutsuma käsitsi. Järgmises peatükis teeme keerukama kliendi, kellel on oma suur keelemudel (LLM). Seniks vaatame, kuidas funktsioone serveris kutsuda:

#### Rust

Main-funktsioonis, pärast kliendi initsialiseerimist, käivitame serveri ja kuvame mõned funktsioonid.

```rust
// Algatamine
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Tööriistade loetelu
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funktsioonide kutsumine

Selleks, et funktsioone kutsuda, peab tagama õiged argumendid ja mõnikord ka õige nime.

#### TypeScript

```typescript

// Loe ressurssi
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kutsu tööriista
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// kutsu prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Eelnevas koodis:

- Loe ressurssi, kutsudes `readResource()` ja määrates `uri`. Serveri pool näeb see välja umbes nii:

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

    Meie `uri` väärtus `file://example.txt` vastab serveri tasandil `file://{name}` mustrile. `example.txt` seotakse parameetriga `name`.

- Kutsu tööriista, nimetades tööriista nime ja argumendid nii:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Saada prompt, kutsudes `getPrompt()` koos `name` ja `arguments`. Serveri kood on selline:

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

    Seetõttu näeb sinu kliendi kood välja umbes nii, et sobituks serveris määratuga:

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
# Loe ressurssi
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Kutsu tööriista
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Eelnevas koodis:

- Kutsusime ressurssi nimega `greeting` kasutades `read_resource`.
- Kutsusime tööriista nimega `add` kasutades `call_tool`.

#### .NET

1. Lisame koodi tööriista kutsumiseks:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. Tulemuse väljastamiseks kasutame järgmist koodi:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Kutsu erinevaid kalkulaatori tööriistu
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

Eelnevas koodis:

- Kutsusime mitut kalkulaatori tööriista `callTool()` meetodiga ja `CallToolRequest` objektidega.
- Iga tööriista kutsumise juures määratakse tööriista nimi ja seletav argumentide `Map`.
- Serveri tööriistad ootavad kindlaid parameetrinimesid (nt "a", "b" matemaatika operatsioonides).
- Tulemused tagastatakse `CallToolResult` objektidena, mis sisaldavad serveri vastust.

#### Rust

```rust
// Kutsu lisamise tööriist argumentidega = {"a": 3, "b": 2}
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

Klienti käivitamiseks tipi terminali järgmine käsk:

#### TypeScript

Lisa pouks avaldusse oma *package.json*- faili "scripts" sektsiooni:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Kutsu klient järgmise käsuga:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Veendu, et MCP server töötab aadressil `http://localhost:8080`. Seejärel käivita klient:

```bash
# Koosta oma projekt
./mvnw clean compile

# Käivita klient
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Või muul juhul võid käivitada kogu kliendi lahenduse projekti, mis asub kaustas `03-GettingStarted\02-client\solution\java`:

```bash
# Liigu lahenduse kataloogi
cd 03-GettingStarted/02-client/solution/java

# Koosta ja käivita JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Kodutöö

Selles kodutöös kasutad õpitut ja teed iseenda kliendi.

Siin on server, mida saad kasutada ja kellest oma kliendi kaudu kutsuda. Proovi lisada serverile huvitavamaid funktsioone.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Loo MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Lisa täiendustööriist
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisa dünaamiline tervituse ressurss
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

// Alusta sõnumite vastuvõttu stdin-i kaudu ja sõnumite saatmist stdout-i kaudu

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

# Loo MCP server
mcp = FastMCP("Demo")


# Lisa liitmistööriist
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Lisa dünaamiline tervitusressurss
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

Vaata seda projekti, et näha, kuidas [lisada prompt'e ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Samuti vaata linki, kuidas kutsuda [prompte ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Eelmises jaotises õppisid, kuidas luua lihtne MCP server Rustiga. Võid jätkata selle arendamist või vaadata lisaks Rust'il põhinevaid MCP serverite näiteid siin: [MCP serveri näited](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lahendus

**Lahenduse kaust** sisaldab täielikke, jooksutamiseks valmis kliendi rakendusi, mis demonstreerivad kõiki selles õpetuses käsitletud mõisteid. Iga lahendus sisaldab nii klient- kui serverikoodi, organiseeritud eraldi iseseisvateks projektideks.

### 📁 Lahenduse struktuur

Lahenduse kaust on organiseeritud programmeerimiskeelte kaupa:

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

Iga keelepõhine lahendus sisaldab:

- **Täielikku kliendi rakendust** koos kõigi õpetuses käsitletud funktsioonidega
- **Toimivat projektistruktuuri** koos õige sõltuvuste ja konfigureerimisega
- **Build ja käivituskäske** lihtsaks seadistamiseks ja käivitamiseks
- **Detailset README faili**, milles on keele põhised juhised
- **Vigade käsitlemise** ja tulemuste töötlemise näiteid

### 📖 Lahenduste kasutamine

1. **Mine oma eelistatud keele kausta**:

   ```bash
   cd solution/typescript/    # TypeScripti jaoks
   cd solution/java/          # Java jaoks
   cd solution/python/        # Pythoni jaoks
   cd solution/dotnet/        # .NETi jaoks
   ```

2. **Järgi iga kausta README juhiseid**, kus on:
   - Sõltuvuste paigaldamine
   - Projekti build
   - Kliendi käivitamine

3. **Näide väljundist, mida peaksid nägema**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Kogu dokumentatsiooni ja samm-sammuliste juhiste jaoks vaata: **[📖 Lahenduse dokumentatsioon](./solution/README.md)**

## 🎯 Täielikud näited

Oleme pakkunud täielikke ja töötavaid kliendi rakendusi kõigis selles õpetuses käsitletud keeltes. Need näited demonstreerivad kõiki eespool kirjeldatud funktsionaalsusi ja sobivad nii viitena kui ka lähtepunktiks sinu oma projektidele.

### Saadaval täielikud näited

| Keel     | Fail                        | Kirjeldus                                                        |
|----------|-----------------------------|-----------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)         | Täielik Java klient kasutades SSE transporti, põhjaliku veahaldusega |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)         | Täielik C# klient stdio transpordiga ja automaatse serveri käivitusega |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Täielik TypeScript kliendi protokolli tugi MCP üldfunktsioonidega    |
| **Python**| [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)         | Täielik Python klient, kasutades async/await mustrit                |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)             | Täielik Rust klient, kasutades Tokio asünkroonseid operatsioone      |

Iga täielik näide sisaldab:
- ✅ **Ühenduse loomine** ja veahaldus
- ✅ **Serveri avastamine** (tööriistad, ressursid, juhised, kus rakenduvad)
- ✅ **Kalkulaatori toimingud** (liitmine, lahutamine, korrutamine, jagamine, abi)
- ✅ **Tulemuste töötlemine** ja vormindatud väljund
- ✅ **Põhjalik veahaldus**
- ✅ **Puhas, dokumenteeritud kood** samm-sammuliste kommentaaridega

### Alustamine koos täielike näidetega

1. **Vali oma eelistatud keel** ülaltoodud tabelist
2. **Vaata läbi täieliku näidifaili**, et mõista kogu teostust
3. **Käivita näide** järgides juhiseid failis [`complete_examples.md`](./complete_examples.md)
4. **Muuda ja laienda** näidet oma konkreetse kasutusjuhtumi jaoks

Üksikasjaliku dokumentatsiooni saamiseks näidete käivitamise ja kohandamise kohta vaata: **[📖 Täielike näidete dokumentatsioon](./complete_examples.md)**

### 💡 Lahendus vs Täielikud näited

| **Lahenduse kaust** | **Täielikud näited** |
|--------------------|--------------------- |
| Täielik projekti struktuur koos ehitusfailidega | Ühe faili teostused |
| Käivitamiseks valmis koos sõltuvustega | Keskendunud koodinäited |
| Tootmisele sarnane seadistus | Hariduslik viite materjal |
| Keele-spetsiifilised tööriistad | Keeleid ületav võrdlus |

Mõlemad lähenemised on väärtuslikud - kasuta **lahenduse kausta** täielike projektide jaoks ja **täielikke näiteid** õppe- ja viitamiseks.

## Peamised järeldused

Selle peatüki peamised järeldused klientide kohta on järgmised:

- Klientide abil saab nii avastada kui ka serveri funktsioone kutsuda.
- Klient saab käivitada serveri samal ajal, kui ta ise käivitub (nagu selles peatükis), kuid kliendid võivad ühendada ka juba töötavate serveritega.
- Klient on suurepärane viis serveri võimete testimiseks lisaks alternatiividele nagu Inspector, nagu kirjeldati eelmises peatükis.

## Täiendavad ressursid

- [Kliendi loomine MCP-s](https://modelcontextprotocol.io/quickstart/client)

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Järgmine samm

- Järgmine: [Kliendi loomine LLM-iga](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles tuleks pidada autoriteetseks allikaks. Olulise info puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
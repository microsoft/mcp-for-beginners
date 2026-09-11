# Kliendi loomine

Kliendid on kohandatud rakendused või skriptid, mis suhtlevad otseselt MCP serveriga, et taotleda ressursse, tööriistu ja juhendeid. Erinevalt inspektori tööriista kasutamisest, mis pakub graafilist liidest serveriga suhtlemiseks, võimaldab oma kliendi kirjutamine programmeeritud ja automatiseeritud suhtluse. See võimaldab arendajatel integreerida MCP võimalused oma töövoogudesse, automatiseerida ülesandeid ja luua spetsiaalsetele vajadustele kohandatud lahendusi.

## Ülevaade

See õppetund tutvustab kliente Model Context Protocol (MCP) ökosüsteemis. Õpid, kuidas kirjutada oma klient ja ühendada see MCP serveriga.

## Õpieesmärgid

Selle õppetunni lõpuks saad:

- Mõista, mida klient saab teha.
- Kirjutada oma klient.
- Ühenduda ja testida klienti MCP serveriga, et veenduda selle eelduspärases toimimises.

## Mis kuulub kliendi kirjutamisse?

Kliendi kirjutamiseks pead tegema järgmist:

- **Impordi õigeid teeke**. Kasutad sama teeki nagu varem, ainult erinevaid struktuure.
- **Iniitsialiseeri klient**. See hõlmab kliendi eksemplari loomist ja ühendamist valitud transpordimeetodiga.
- **Otsusta, milliseid ressursse kuvada**. Sinu MCP serveril on ressursid, tööriistad ja juhendid, pead otsustama, milliseid kuvada.
- **Integreeri klient host-rakendusse**. Kui tead serveri võimalusi, tuleb integreerida see host-rakendusse nii, et kui kasutaja sisestab juhendi või muu käsu, kutsutakse vastav serveri funktsioon välja.

Nüüd kui teame ülaltvaates, mida teeme, vaatame järgmisena näidet.

### Näide kliendist

Vaatame seda näite klienti:

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

// Kuva käsud
const prompts = await client.listPrompts();

// Hangi käsk
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Kuvatav ressurssid
const resources = await client.listResources();

// Loe ressurssi
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Kasuta tööriista
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Eelnevas koodis me:

- Importisime teegid
- Lisasime kliendi instantsi ja ühendasime selle stdio transpordiga.
- Loetlesime juhendeid, ressursse ja tööriistu ning kutsusime need kõik välja.

Siin see on, klient, kes saab MCP serveriga suhelda.

Võtame järgmises harjutuses rahulikult ja lahtiseletame iga koodilõigu ning selgitame, mis toimub.

## Harjutus: kliendi kirjutamine

Nagu eespool mainitud, võtame koodi selgitamisel aega, ja võid kindlasti ka kaasa koodi kirjutada.

### -1- Impordi teegid

Importime vajalikke teeke, meil on vaja viiteid kliendile ja valitud transpordiprotokollile, st stdio-le. Stdio on protokoll asjade jaoks, mis jooksevad kohaliku masina peal. SSE on teine transpordiprotokoll, mida me näitame tulevastes peatükkides — see on su teine valik. Praegu jätkame siiski stdio-ga.

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

Java puhul lood kliendi, mis ühendub eelmise harjutuse MCP serveriga. Kasutades sama Java Spring Boot projektistruktuuri nagu [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), loo uus Java klass nimega `SDKClient` kausta `src/main/java/com/microsoft/mcp/sample/client/` ja lisa järgmised importimised:

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

Liigume instantsieerimise juurde.

### -2- Kliendi ja transpordi instantsieerimine

Peame looma transpordi instantsi ja meie kliendi instantsi:

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

Eelnevas koodis me:

- Lood stdio transpordi instantsi. Pane tähele, et see määrab käsu ja argumendid, kuidas serverit leida ja käivitada, sest see tuleb teha kliendi loomisel.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Lood kliendi, andes talle nime ja versiooni.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Ühendatud klient valitud transpordiga.

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

Eelnevas koodis me:

- Impordisime vajalikud teegid
- Lood serveri parameetrite objekti, mida kasutame serveri käivitamiseks, et kliendiga ühendada.
- Määratlesime `run` meetodi, mis kutsub `stdio_client` funktsiooni, mis alustab kliendiseanssi.
- Lood sisenemispunkti, kus anname `run` meetodi `asyncio.run` meetodile.

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

Eelnevas koodis me:

- Impordisime vajalikud teegid.
- Lood stdio transpordi ja kliendi `mcpClient`. Viimast kasutame MCP serveri funktsioonide listimiseks ja kutsumiseks.

Märkus: "Arguments" sees võid määrata kas *.csproj* faili või täidetava faili tee.

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

Eelnevas koodis me:

- Loonud main meetodi, mis seab üles SSE transpordi, mis osutab aadressile `http://localhost:8080`, kus meie MCP server töötab.
- Loonud kliendi klassi, mis võtab transpordi konstruktoriparameetrina.
- `run` meetodis loodame sünkroonse MCP kliendi transpordi abil ja alustame ühendamist.
- Kasutame SSE (Server-Sent Events) transporti, mis sobib HTTP-põhise suhtluse jaoks Java Spring Boot MCP serveritega.

#### Rust

Märkus: see Rust klient eeldab, et server on suguluses olev projekt nimega "calculator-server" samas kaustas. Alljärgnev kood käivitab serveri ja ühendub sellega.

```rust
async fn main() -> Result<(), RmcpError> {
    // Eeldage, et server on samas kataloogis olev õeprojekt nimega "calculator-server"
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

    // TODO: Loetle tööriistad

    // TODO: Kutsu lisamise tööriist argumendidega = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Serveri funktsioonide listimine

Nüüd on meil klient, kes suudab programmiga ühendada. Kuid ta tegelikult ei kirjuta oma funktsioone välja, teeme seda nüüd:

#### TypeScript

```typescript
// Loendi käsud
const prompts = await client.listPrompts();

// Loendi ressursid
const resources = await client.listResources();

// loendi tööriistad
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

Siin loetleme saadaolevad ressursid `list_resources()` ja tööriistad `list_tools` ning prindime need välja.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ülal on näide, kuidas saame serveri tööriistad välja tuua. Iga tööriista kohta prindime selle nime välja.

#### Java

```java
// Loetle ja näita tööriistu
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Saate serverile ka pingida, et ühendust kontrollida
client.ping();
```

Eelnevas koodis me:

- Kutsusime `listTools()` kõigi MCP serveri tööriistade saamiseks.
- Kasutasime `ping()` selle kontrollimiseks, et ühendus serveriga töötab.
- `ListToolsResult` sisaldab infot kõigi tööriistade kohta, sh nende nimed, kirjeldused ja sisendiskeemid.

Suurepärane, nüüd oleme kõik funktsioonid kaardistanud. Nüüd küsimus: millal neid kasutada? See klient on üsna lihtne — see tähendab, et peame funktsioonid selgesõnaliselt välja kutsuma, kui neid vajame. Järgmises peatükis loome arenenuma kliendi, kellel on oma suur keelemudel (LLM). Praegu aga vaatame, kuidas serveri funktsioone kutsuda:

#### Rust

Peameetodis, pärast kliendi initsialiseerimist, saame initsialiseerida serveri ja loetleda mõned selle funktsioonid.

```rust
// Algata
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Loetle tööriistad
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funktsioonide kutsumine

Funktsioonide kutsumiseks peame veenduma, et määrame õiged argumendid ning mõnel juhul ka selle nime, mida tahame kutsuda.

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

// kutsu prompti
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Eelnevas koodis me:

- Lugesime ressurssi, kutsudes `readResource()` ja määrates `uri`. Serveripool näeb siis ilmselt välja nii:

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

    Meie `uri` väärtus `file://example.txt` vastab serveris `file://{name}` mustrile. `example.txt` omistatakse `name`-le.

- Kutsusime tööriista, määrates selle `name` ja `arguments` järgmiselt:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Saime juhendi, kutsudes `getPrompt()` koos `name` ja `arguments`. Serverikood näeb välja nii:

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

    ning vastavalt näeb kliendikood välja nii, et see vastab serveril määratule:

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

# Käivita tööriist
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Eelnevas koodis me:

- Kutsusime ressurssi nimega `greeting` funktsiooniga `read_resource`.
- Kutsusime tööriista nimega `add` funktsiooniga `call_tool`.

#### .NET

1. Lisame koodi tööriista kutsumiseks:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Tulemuse väljastamiseks on siin kood selle haldamiseks:

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

Eelnevas koodis me:

- Kutsusime mitmeid kalkulaatoritööriistu kasutades `callTool()` meetodit `CallToolRequest` objektidega.
- Iga tööriista kutsumine määrab tööriista nime ja selle tööriista poolt nõutavate parameetrite `Map`-i.
- Serveri tööriistad ootavad kindlaid parameetrinimesid (nt "a", "b" matemaatiliste operatsioonide jaoks).
- Vastused tagastatakse `CallToolResult` objektidena, mis sisaldavad serveri vastuseid.

#### Rust

```rust
// Kutsu lisamise tööriist argumendidega = {"a": 3, "b": 2}
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

Kliendi käivitamiseks tippige terminali järgmine käsk:

#### TypeScript

Lisa oma *package.json* "scripts" sektsiooni järgmine kirjeldus:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Käivita klient järgmise käsuga:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Veendu, et MCP server töötab aadressil `http://localhost:8080`. Seejärel aja klient käima:

```bash
# Koosta oma projekt
./mvnw clean compile

# Käivita klient
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Võid ka käivitada kogu kliendiprojekti, mis on olemas lahenduskaustas `03-GettingStarted\02-client\solution\java`:

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

## Ülesanne

Selles ülesandes kasutad õpitut kliendi loomiseks, kuid teed selle ise.

Siin on server, mida saad kutsuda oma kliendikoodiga. Proovi lisada serverile rohkem funktsioone, et see huvitavam oleks.

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

// Lisa liitmistööriist
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Lisa dünaamiline tervitusressurss
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

// Alusta sõnumite vastuvõttu stdin-ist ja sõnumite saatmist stdout-i

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

Vaata seda projekti, et näha, kuidas saad [lisa juhendeid ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Samuti, vaata seda linki, kuidas kutsuda [juhendeid ja ressursse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

[Eelnevas sektsioonis](../../../../03-GettingStarted/01-first-server) õppisid, kuidas luua lihtne MCP server Rustiga. Sa võid sellele edasi ehitada või vaadata lisaks Rust-põhiseid MCP serveri näiteid siin: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lahendus

**lahenduskaust** sisaldab täielikke, valmis töötavaid klienditeostusi, mis demonstreerivad kõiki selle juhendi käsitletud kontseptsioone. Iga lahendus sisaldab nii kliendi- kui serverikoodi, mis on korraldatud eraldi, iseseisvates projektides.

### 📁 Lahenduse struktuur

Lahenduse kataloog on korraldatud programmeerimiskeelte kaupa:

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

- **Täielikku kliendi teostust** kõikide selle juhendi funktsioonidega
- **Töötavat projektistruktuuri** koos sobivate sõltuvuste ja konfiguratsiooniga
- **Vaigistamise ja käivitamise skripte** lihtsaks seadistuseks ja käivitamiseks
- **Üksikasjalikku README-d** koos keelega seotud juhistega
- **Vigade käsitlemise** ja tulemuste töötlemise näited

### 📖 Lahenduste kasutamine

1. **Mine oma valitud keele kausta**:

   ```bash
   cd solution/typescript/    # TypeScripti jaoks
   cd solution/java/          # Java jaoks
   cd solution/python/        # Pythoni jaoks
   cd solution/dotnet/        # .NET jaoks
   ```

2. **Järgi iga kausta README juhiseid**:
   - Sõltuvuste installeerimine
   - Projekti kompileerimine
   - Kliendi käivitamine

3. **Näide väljundist, mida peaksid nägema**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Täieliku dokumentatsiooni ja samm-sammult juhiste jaoks vaata: **[📖 Lahenduse dokumentatsioon](./solution/README.md)**

## 🎯 Täielikud näited

Oleme pakkunud täielikke, töötavaid klienditeostusi kõigis selles juhendis käsitletud programmeerimiskeeltes. Need näited demonstreerivad kogu ülalkirjeldatud funktsionaalsust ja neid saab kasutada viitenäitena või aluspunktidena oma projektide jaoks.

### Saadaval olevad täielikud näited

| Keel | Fail | Kirjeldus |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Täielik Java klient kasutades SSE transporti koos põhjaliku veahaldusega |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Täielik C# klient kasutades stdio transporti koos automaatse serveri käivitusega |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Täielik TypeScript klient, mis toetab täielikult MCP protokolli |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Täielik Python klient kasutades async/await mustreid |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Täielik Rust klient kasutades Tokio asünkroonsete toimingute jaoks |

Iga täisnäide sisaldab:

- ✅ **Ühenduse loomist** ja veahaldust
- ✅ **Serveri avastamist** (tööriistad, ressursid, juhendid, kui need on olemas)
- ✅ **Kalkulaatori operatsioone** (liida, lahuta, korruta, jaga, abi)
- ✅ **Tulemuste töötlemist** ja vormindatud väljundit
- ✅ **Põhjalikku veahaldust**

- ✅ **Puhas, dokumenteeritud kood** samm-sammuliste kommentaaridega  

### Alustamine täielike näidetega  

1. **Vali ülalolevast tabelist eelistatud keel**  
2. **Vaata täielikku näidist faili** mõistmaks kogu teostust  
3. **Käivita näide** järgnedes juhistele failis [`complete_examples.md`](./complete_examples.md)  
4. **Muuda ja laienda** näidet oma konkreetse vajaduse jaoks  

Täpse dokumentatsiooni ja näidete käivitamise ning kohandamise kohta vaata: **[📖 Täielike näidete dokumentatsioon](./complete_examples.md)**  

### 💡 Lahendus vs Täielikud Näited  

| **Lahenduste kaust** | **Täielikud näited** |  
|--------------------|--------------------- |  
| Täis projektistruktuur koos ehituse failidega | Ühekahelised teostused |  
| Valmis käivitamiseks koos sõltuvustega | Keskendunud koodi näited |  
| Tootmisle valguses seadistus | Hariduslik viitamine |  
| Keelespetsiifilised tööriistad | Keelteülene võrdlus |  

Mõlemad lähenemised on väärtuslikud - kasuta **lahenduste kausta** täielike projektide jaoks ja **täielikke näiteid** õppimiseks ning viiteks.  

## Peamised järeldused  

Selle peatüki peamised järeldused klientide kohta on järgmised:  

- Saab kasutada nii serveri funktsioonide avastamiseks kui ka kutseks.  
- Saab serveri käivitada samal ajal kui see ise käivitatakse (nagu selles peatükis), aga kliendid võivad ka juba töötavaga ühendada.  
- On suurepärane viis testida serveri võimalusi alternatiivide kõrval nagu Inspector, nagu eelnevas peatükis kirjeldatud.  

## Täiendavad ressursid  

- [Kliendi loomine MCP-s](https://modelcontextprotocol.io/quickstart/client)  

## Näited  

- [Java kalkulaator](../samples/java/calculator/README.md)  
- [.NET kalkulaator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript kalkulaator](../samples/javascript/README.md)  
- [TypeScript kalkulaator](../samples/typescript/README.md)  
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)  
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)  

## Mis järgmiseks  

- Järgmine: [Klient LLM-iga loomine](../03-llm-client/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
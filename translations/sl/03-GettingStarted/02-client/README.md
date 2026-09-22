# Ustvarjanje klienta

Klienti so prilagojene aplikacije ali skripti, ki neposredno komunicirajo z MCP strežnikom za zahtevanje virov, orodij in pozivov. Za razliko od uporabe orodja za inšpekcijo, ki zagotavlja grafični vmesnik za interakcijo s strežnikom, pisanje lastnega klienta omogoča programatične in avtomatizirane interakcije. To razvijalcem omogoča integracijo zmogljivosti MCP v svoje delovne tokove, avtomatizacijo opravil in gradnjo prilagojenih rešitev, prilagojenih posebnim potrebam.

## Pregled

Ta lekcija uvaja koncept klientov znotraj ekosistema Model Context Protocol (MCP). Naučili se boste, kako napisati svojega klienta in ga povezati z MCP strežnikom.

## Cilji učenja

Do konca te lekcije boste lahko:

- Razumeli, kaj klient lahko počne.
- Napisali svojega klienta.
- Povezali in testirali klienta z MCP strežnikom, da zagotovite, da ta deluje kot pričakovano.

## Kaj je potrebno za pisanje klienta?

Za pisanje klienta boste morali narediti naslednje:

- **Uvoziti pravilne knjižnice**. Uporabili boste isto knjižnico kot prej, le različne konstrukte.
- **Ustvariti klienta**. To bo vključevalo ustvarjanje instance klienta in njegovo povezavo z izbranim načinom prenosa.
- **Odločiti, katere vire boste navedli**. Vaš MCP strežnik vsebuje vire, orodja in pozive; morate se odločiti, katere boste navedli.
- **Integrirati klienta v gostujočo aplikacijo**. Ko boste poznali zmogljivosti strežnika, morate to integrirati v vašo gostujočo aplikacijo, tako da če uporabnik vnese poziv ali ukaz, se sproži ustrezna funkcija strežnika.

Zdaj, ko na splošno razumemo, kaj nas čaka, si poglejmo naslednji primer.

### Primer klienta

Poglejmo si ta primer klienta:

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

// Seznam pozivov
const prompts = await client.listPrompts();

// Pridobi poziv
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Seznam virov
const resources = await client.listResources();

// Preberi vir
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Pokliči orodje
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

V zgornji kodi smo:

- Uvozili knjižnice
- Ustvarili instanco klienta in jo povezali z uporabo stdio za prenos.
- Našteli pozive, vire in orodja ter jih vse uporabili.

Tukaj ga imate, klient, ki lahko komunicira z MCP strežnikom.

Vzemimo si čas v naslednjem razdelku z vajami in razčlenimo vsak del kode ter razložimo, kaj se dogaja.

## vaja: Pisanje klienta

Kot smo že omenili, si vzemimo čas za razlago kode in, če želite, programirajte zraven.

### -1- Uvoz knjižnic

Uvozimo potrebne knjižnice, potrebovali bomo reference do klienta in do izbranega protokola za prenos, stdio. stdio je protokol za stvari, ki tečejo na vašem lokalnem računalniku. SSE je drug protokol za prenos, ki ga bomo pokazali v prihodnjih poglavjih, ampak to je vaša druga možnost. Za zdaj pa nadaljujmo s stdio.

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

Za Javo boste ustvarili klienta, ki se poveže z MCP strežnikom iz prejšnje vaje. Uporabite isto strukturo projekta Java Spring Boot iz [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), ustvarite novo Java razred imenovan `SDKClient` v mapi `src/main/java/com/microsoft/mcp/sample/client/` in dodajte naslednje uvoze:

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

Dodati boste morali naslednje odvisnosti v vašo datoteko `Cargo.toml`.

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

Od tam lahko uvozite potrebne knjižnice v vašo kodo klienta.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Nadaljujmo z instanciranjem.

### -2- Instanciranje klienta in prenosa

Potrebovali bomo ustvariti instanco prenosa in tisto našega klienta:

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

- Ustvarili instanco prenosa stdio. Opazite, kako določa ukaz in argumente za iskanje in zagon strežnika, saj je to nekaj, kar bomo morali narediti ob ustvarjanju klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instancirali klienta z imenom in verzijo.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Povezali klienta z izbranim načinom prenosa.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Ustvari strežniške parametre za povezavo stdio
server_params = StdioServerParameters(
    command="mcp",  # Izvedljiva datoteka
    args=["run", "server.py"],  # Neobvezni ukazni argumenti
    env=None,  # Neobvezne okoljske spremenljivke
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializiraj povezavo
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

V zgornji kodi smo:

- Uvozili potrebne knjižnice
- Instancirali objekt parametrov strežnika, saj ga bomo uporabili za zagon strežnika, da se bomo lahko povezali z njim z našim klientom.
- Definirali metodo `run`, ki nato kliče `stdio_client`, ki zažene klientovo sejo.
- Ustvarili vstopno točko, kjer posredujemo metodo `run` funkciji `asyncio.run`.

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

V zgornji kodi smo:

- Uvozili potrebne knjižnice.
- Ustvarili stdio prenos in ustvarili klienta `mcpClient`. Ta bo uporabljen za navajanje in klic funkcij na MCP strežniku.

Opomba, pod "Arguments" lahko usmerite bodisi na *.csproj* ali na izvršljivo datoteko.

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
        
        // Tukaj gre vaša logika stranke
    }
}
```

V zgornji kodi smo:

- Ustvarili glavno metodo, ki nastavi SSE prenos usmerjen na `http://localhost:8080`, kjer bo tekel naš MCP strežnik.
- Ustvarili razred klienta, ki prejme prenos kot parameter konstruktorja.
- V metodi `run` ustvarimo sinhroni MCP klient z uporabo prenosa in inicializiramo povezavo.
- Uporabili SSE (Server-Sent Events) prenos, ki je primeren za HTTP komunikacijo z MCP strežniki Java Spring Boot.

#### Rust

Ta Rust klient predvideva, da je strežnik sosednji projekt z imenom "calculator-server" v isti mapi. Koda spodaj bo zagnala strežnik in se z njim povezala.

```rust
async fn main() -> Result<(), RmcpError> {
    // Predpostavimo, da je strežnik sestrski projekt z imenom "calculator-server" v istem imeniku
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

    // TODO: Inicializiraj

    // TODO: Naštej orodja

    // TODO: Pokliči orodje add z argumenti = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Naštevanje funkcij strežnika

Imamo klienta, ki se poveže, če bo program zagnan. Vendar ne navaja dejansko njegovih funkcij, zato poglejmo, kako to urediti:

#### TypeScript

```typescript
// Seznam pozivov
const prompts = await client.listPrompts();

// Seznam virov
const resources = await client.listResources();

// seznam orodij
const tools = await client.listTools();
```

#### Python

```python
# Našteti razpoložljive vire
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Našteti razpoložljiva orodja
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tukaj naštetimo razpoložljive vire z `list_resources()` in orodja z `list_tools` ter jih izpišemo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Zgoraj je primer, kako lahko na strežniku navedemo orodja. Za vsako orodje nato izpišemo njegovo ime.

#### Java

```java
// Naštejte in pokažite orodja
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Strežnik lahko tudi pingaš za preverjanje povezave
client.ping();
```

V zgornji kodi smo:

- Poklicali `listTools()`, da dobimo vsa razpoložljiva orodja od MCP strežnika.
- Uporabili `ping()`, da preverimo, če povezava s strežnikom deluje.
- `ListToolsResult` vsebuje informacije o vseh orodjih vključno z njihovimi imeni, opisi in vhodnimi shemami.

Odlično, zdaj smo zajeli vse funkcije. Zdaj pa vprašanje, kdaj jih uporabljamo? No, ta klient je zelo preprost, preprost v smislu, da bomo morali funkcije izrecno poklicati, ko jih želimo. V naslednjem poglavju bomo ustvarili bolj naprednega klienta, ki ima dostop do lastnega velikega jezikovnega modela (LLM). Za zdaj pa poglejmo, kako lahko zahtevamo funkcije strežnika:

#### Rust

V glavni funkciji, po inicializiranju klienta, lahko inicializiramo strežnik in naštejemo nekaj njegovih funkcij.

```rust
// Inicializiraj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Orodja seznami
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Klic funkcij

Za klic funkcij moramo zagotoviti pravilne argumente in v nekaterih primerih ime tistega, kar želimo klicati.

#### TypeScript

```typescript

// Preberi vir
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Pokliči orodje
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// pokliči poziv
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

V prej prikazani kodi smo:

- Prebrali vir, z metodo `readResource()` z določenm `uri`. Tukaj je, kako to najverjetneje izgleda na strežnikovi strani:

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

    Naša vrednost `uri` `file://example.txt` se ujema z `file://{name}` na strežniku. `example.txt` bo preslikan na `name`.

- Poklicali orodje, klicamo ga tako, da navedemo njegovo `name` in njegove `arguments`, kot sledi:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Dobili poziv, za poziv pokličemo `getPrompt()` z `name` in `arguments`. Koda strežnika izgleda takole:

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

    in zato vaš končni klic klienta izgleda takole, da se ujema z deklaracijo strežnika:

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
# Preberite vir
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Pokličite orodje
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

V prej prikazani kodi smo:

- Poklicali vir z imenom `greeting` z uporabo `read_resource`.
- Poklicali orodje `add` z uporabo `call_tool`.

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
// Pokličite različna orodja kalkulatorja
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

- Poklicali več orodij kalkulatorja z metodo `callTool()` z objekti `CallToolRequest`.
- Vsak klic orodja določa ime orodja in `Map` argumentov, ki jih zahteva to orodje.
- Orodja strežnika zahtevajo posebna imena parametrov (npr. "a", "b" za matematične operacije).
- Rezultati so vrnjeni kot objekti `CallToolResult`, ki vsebujejo odziv strežnika.

#### Rust

```rust
// Pokliči orodje za seštevanje z argumenti = {"a": 3, "b": 2}
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

### -5- Zagon klienta

Za zagon klienta vnesite naslednji ukaz v terminal:

#### TypeScript

Dodajte naslednji zapis v svoj razdelek "scripts" v *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Pokličite klienta z naslednjim ukazom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najprej poskrbite, da vaš MCP strežnik teče na `http://localhost:8080`. Nato zaženite klienta:

```bash
# Zgradite svoj projekt
./mvnw clean compile

# Zaženite odjemalca
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Lahko pa zaženete celoten projekt klienta, ki je priložen v rešitveni mapi `03-GettingStarted\02-client\solution\java`:

```bash
# Pomaknite se do imenika rešitve
cd 03-GettingStarted/02-client/solution/java

# Sestavite in zaženite JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Naloga

V tej nalogi boste uporabili, kar ste se naučili o ustvarjanju klienta, ampak napisali boste svojega.

Tukaj imate strežnik, ki ga lahko uporabite in ki ga morate poklicati preko kode vašega klienta. Poskusite dodati več funkcij strežniku, da bo bolj zanimiv.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Ustvari MCP strežnik
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Dodaj orodje za seštevanje
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dinamični pozdravni vir
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

// Začni prejemati sporočila na stdin in pošiljati sporočila na stdout

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

# Ustvari MCP strežnik
mcp = FastMCP("Demo")


# Dodaj orodje za seštevanje
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dodaj dinamičen vir pozdrava
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

Prav tako preverite ta povezavo, da vidite, kako klicati [pozive in vire](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [prejšnjem razdelku](../../../../03-GettingStarted/01-first-server) ste se naučili, kako ustvariti preprost MCP strežnik z Rustom. Nadaljujete lahko na tem ali pa si ogledate to povezavo za več primerov MCP strežnikov v Rustu: [Primeri MCP strežnika](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rešitev

**Mapa rešitve** vsebuje popolne, pripravljene za zagon implementacije klientov, ki prikazujejo vse koncepte, zajete v tem vodiču. Vsaka rešitev vključuje tako kodo klienta kot strežnika, organizirano v ločenih, samostojnih projektih.

### 📁 Struktura rešitve

Mapa rešitve je organizirana po programskih jezikih:

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

Vsaka rešitev za določen jezik nudi:

- **Popolno implementacijo klienta** z vsemi funkcijami iz vodiča
- **Delujočo strukturo projekta** s pravilnimi odvisnostmi in konfiguracijo
- **Skripte za gradnjo in zagon** za enostavno postavitev in izvedbo
- **Podroben README** z navodili specifičnimi za jezik
- **Primeri obdelave napak** in postopkov za rezultate

### 📖 Uporaba rešitev

1. **Pojdite v mapo za svoj priljubljeni programski jezik**:

   ```bash
   cd solution/typescript/    # Za TypeScript
   cd solution/java/          # Za Java
   cd solution/python/        # Za Python
   cd solution/dotnet/        # Za .NET
   ```

2. **Sledite navodilom v README** v vsaki mapi za:
   - Namestitev odvisnosti
   - Gradnjo projekta
   - Zagon klienta

3. **Primer izpisa**, ki ga boste videli:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za popolno dokumentacijo in korak-po-korak navodila glejte: **[📖 Dokumentacija rešitve](./solution/README.md)**

## 🎯 Popolni primeri

Ponudili smo popolne, delujoče implementacije klientov za vse programske jezike, obravnavane v tem vodiču. Ti primeri prikazujejo vso zgoraj opisano funkcionalnost in jih lahko uporabite kot referenco ali začetno točko za vaše projekte.

### Na voljo popolni primeri

| Jezik | Datoteka | Opis |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Popoln Java klient z uporabo SSE prenosa z obsežnim upravljanjem napak |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Popoln C# klient s stdio prenosom in samodejnim zagonom strežnika |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Popoln TypeScript klient s popolno podporo MCP protokola |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Popoln Python klient z vzorci async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Popoln Rust klient z uporabo Tokio za asinhrone operacije |

Vsak popoln primer vključuje:

- ✅ **Vzpostavitev povezave** in upravljanje napak
- ✅ **Odkritje strežnika** (orodja, viri, pozivi, kjer je primerno)
- ✅ **Operacije kalkulatorja** (dodajanje, odštevanje, množenje, deljenje, pomoč)
- ✅ **Obdelava rezultatov** in oblikovan izpis
- ✅ **Obsežno upravljanje napak**

- ✅ **Čista, dokumentirana koda** s komentarji korak za korakom

### Začetek s popolnimi primeri

1. **Izberite želeni programski jezik** iz tabele zgoraj
2. **Preglejte datoteko popolnega primera** za razumevanje celotne implementacije
3. **Zaženite primer** po navodilih v [`complete_examples.md`](./complete_examples.md)
4. **Spremenite in razširite** primer za vaš specifični primer uporabe

Za podrobno dokumentacijo o zagonu in prilagajanju teh primerov glejte: **[📖 Dokumentacija popolnih primerov](./complete_examples.md)**

### 💡 Rešitev proti popolnim primerom

| **Mapa rešitve** | **Popolni primeri** |
|--------------------|--------------------- |
| Celotna struktura projekta z datotekami za gradnjo | Implementacije v eni datoteki |
| Pripravljeno za zagon z odvisnostmi | Osredotočeni primeri kode |
| Nastavitev podobna produkcijski | Izobraževalni referenčni primer |
| Orodja specifična za jezik | Primerjava med jeziki |

Obe pristopi sta dragoceni - uporabite **mapo rešitve** za celostne projekte in **popolne primere** za učenje in referenco.

## Ključne ugotovitve

Ključne ugotovitve za to poglavje glede odjemalcev so naslednje:

- Uporabljajo se lahko tako za odkrivanje kot klicanje funkcionalnosti na strežniku.
- Lahko začnejo strežnik medtem ko se sami zaganjajo (kot v tem poglavju), vendar se lahko odjemalci povežejo tudi z že tečečimi strežniki.
- Odlična način za testiranje zmogljivosti strežnika poleg alternativ, kot je Inspector, kot je bilo opisano v prejšnjem poglavju.

## Dodatni viri

- [Gradnja odjemalcev v MCP](https://modelcontextprotocol.io/quickstart/client)

## Primeri

- [Java kalkulator](../samples/java/calculator/README.md)
- [.NET kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulator](../../../../03-GettingStarted/samples/rust)

## Kaj sledi

- Naslednje: [Ustvarjanje odjemalca z LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
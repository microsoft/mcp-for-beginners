# Ustvarjanje odjemalca

Odjemalci so prilagojene aplikacije ali skripte, ki neposredno komunicirajo z MCP strežnikom za zahtevanje virov, orodij in pozivov. Za razliko od uporabe orodja za pregledovalnik, ki omogoča grafični vmesnik za interakcijo s strežnikom, pisanje lastnega odjemalca omogoča programirane in avtomatizirane interakcije. To razvijalcem omogoča integracijo zmogljivosti MCP v njihove delovne postopke, avtomatizacijo opravil in izdelavo prilagojenih rešitev, prilagojenih specifičnim potrebam.

## Pregled

Ta lekcija uvaja koncept odjemalcev v ekosistemu Model Context Protocol (MCP). Naučili se boste, kako napisati svoj odjemalec in ga povezati s MCP strežnikom.

## Cilji učenja

Na koncu te lekcije boste znali:

- Razumeti, kaj odjemalec lahko počne.
- Napisati svojega odjemalca.
- Povezati se in preizkusiti odjemalca z MCP strežnikom, da zagotovite, da slednji deluje kot pričakovano.

## Kaj spada v pisanje odjemalca?

Za pisanje odjemalca boste morali narediti naslednje:

- **Uvoziti pravilne knjižnice**. Uporabljali boste isto knjižnico kot prej, le različne konstrukte.
- **Ustvariti instanco odjemalca**. To bo vključevalo ustvarjanje instance odjemalca in njegovo povezavo z izbrano metodo prenosa.
- **Odločiti se, katere vire boste našteli**. Vaš MCP strežnik ima vire, orodja in pozive, odločiti se morate, katere boste našteli.
- **Integrirati odjemalca v gostujočo aplikacijo**. Ko poznate zmogljivosti strežnika, jih morate integrirati v vašo gostujočo aplikacijo, tako da bo ob vnosu poziva ali druge ukaze uporabnika priklicana ustrezna funkcionalnost strežnika.

Sedaj, ko razumemo na visoki ravni, kaj bomo naredili, poglejmo naslednji primer.

### Primer odjemalca

Poglejmo si ta primer odjemalca:

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
- Ustvarili instanco odjemalca in ga povezali z uporabo stdio za prenos.
- Našteli pozive, vire in orodja ter jih vse poklicali.

Tako imamo odjemalca, ki lahko komunicira z MCP strežnikom.

V naslednjem delu vaje si bomo vzeli čas in razčlenili vsak del kode ter razložili, kaj se dogaja.

## Vaja: Pisanje odjemalca

Kot smo že rekli, si bomo vzeli čas za razlago kode, in če želite, kodo tudi pišite skupaj z nami.

### -1- Uvoz knjižnic

Uvozimo knjižnice, ki jih potrebujemo, potrebovali bomo reference za odjemalca in za izbrani prenosni protokol, stdio. stdio je protokol za stvari, ki naj bi tekle na vašem lokalnem računalniku. SSE je drugi prenosni protokol, ki ga bomo pokazali v prihodnjih poglavjih, a to je vaša druga možnost. Za zdaj pa nadaljujmo z stdio.

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

Za Java boste ustvarili odjemalca, ki se poveže s MCP strežnikom iz prejšnje vaje. Uporabite isto strukturo projekta Java Spring Boot iz [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), ustvarite novo Java razredno `SDKClient` v mapi `src/main/java/com/microsoft/mcp/sample/client/` in dodajte naslednje uvoze:

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

Nato lahko v kodi vašega odjemalca uvozite potrebne knjižnice.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Pojdimo na ustvarjanje instanc.

### -2- Ustvarjanje instančne objekta odjemalca in prenosa

Ustvariti bomo morali instanco prenosa in instanco našega odjemalca:

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

- Ustvarili instanco prenosa stdio. Opažamo, da določa ukaz in argumente, kako najti in zagnati strežnik, kar bomo potrebovali med ustvarjanjem odjemalca.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Ustvarili instanco odjemalca z imenom in različico.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Povezali odjemalca z izbranim prenosom.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Ustvari parametre strežnika za stdio povezavo
server_params = StdioServerParameters(
    command="mcp",  # Izvedljiva datoteka
    args=["run", "server.py"],  # Neobvezni argumenti ukazne vrstice
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

- Uvozili potrebne knjižnice.
- Ustvarili objekt parametrov strežnika, saj ga bomo uporabili za zagon strežnika, da se bomo lahko povezali z našim odjemalcem.
- Definirali metodo `run`, ki kliče `stdio_client`, ki začne odjemalčevo sejo.
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
- Ustvarili stdio prenos in odjemalca `mcpClient`. To bomo uporabili za naštetje in klic funkcij MCP strežnika.

Opomba: v "Arguments" lahko navedete pot do *.csproj* ali do izvršljive datoteke.

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
        
        // Vaša logika odjemalca gre sem
    }
}
```

V zgornji kodi smo:

- Ustvarili glavno metodo, ki nastavi SSE prenos, ki se povezuje na `http://localhost:8080`, kjer bo tekel naš MCP strežnik.
- Ustvarili razred odjemalca, ki kot parameter konstruktora prejme prenos.
- V metodi `run` ustvarili sinhroni MCP odjemalec z uporabo prenosa in inicializirali povezavo.
- Uporabili SSE (Server-Sent Events) prenos, ki je primeren za HTTP komunikacijo z MCP strežniki Java Spring Boot.

#### Rust

Ta Rust odjemalec predvideva, da je strežnik sosednji projekt z imenom "calculator-server" v isti mapi. Koda spodaj zažene strežnik in se poveže nanj.

```rust
async fn main() -> Result<(), RmcpError> {
    // Predpostavimo, da je strežnik sorodni projekt z imenom "calculator-server" v isti mapi
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

    // TODO: Prikaži orodja

    // TODO: Pokliči dodaj orodje z argumenti = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Naštevanje funkcij strežnika

Sedaj imamo odjemalca, ki se lahko poveže, če bo program zagnan. Vendar ne našteva njegovih funkcij, zato to naredimo naslednje:

#### TypeScript

```typescript
// Našteti pozive
const prompts = await client.listPrompts();

// Našteti vire
const resources = await client.listResources();

// našteti orodja
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

Tukaj navajamo razpoložljive vire z `list_resources()` in orodja z `list_tools` ter jih izpišemo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Zgoraj je primer, kako lahko naštejemo orodja na strežniku. Za vsako orodje nato izpišemo njegovo ime.

#### Java

```java
// Naštej in pokaži orodja
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Povezavo lahko preveriš tudi s »ping« ukazom strežnika
client.ping();
```

V zgornji kodi smo:

- Poklicali `listTools()`, da dobimo vsa razpoložljiva orodja MCP strežnika.
- Uporabili `ping()`, da preverimo, ali povezava s strežnikom deluje.
- `ListToolsResult` vsebuje informacije o vseh orodjih vključno z njihovimi imeni, opisi in shemami vhodnih podatkov.

Odlično, zdaj smo zajeli vse funkcije. Zdaj je vprašanje, kdaj jih uporabiti? Ta odjemalec je precej enostaven, kar pomeni, da jih bomo morali izrecno klicati, ko jih bomo želeli uporabiti. V naslednjem poglavju bomo ustvarili naprednejšega odjemalca, ki bo imel dostop do lastnega velikega jezikovnega modela, LLM. Za zdaj pa si poglejmo, kako lahko prikličemo funkcije na strežniku:

#### Rust

V glavni funkciji, po inicializaciji odjemalca, lahko inicializiramo strežnik in naštejemo nekatere njegove funkcije.

```rust
// Inicializiraj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Navedite orodja
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Klic funkcij

Za klic funkcij moramo zagotoviti pravilne argumente in v nekaterih primerih ime, kar želimo poklicati.

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

V zgornji kodi smo:

- Prebrali vir; pokličemo vir z `readResource()` in določimo `uri`. Tukaj je, kako to verjetno izgleda na strežniški strani:

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

    Naša vrednost `uri` `file://example.txt` ustreza `file://{name}` na strežniku. `example.txt` bo preslikan v `name`.

- Poklicali orodje; to storimo z določanjem njegovega `name` in `arguments` tako:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Pridobili poziv; za poziv kličemo `getPrompt()` z `name` in `arguments`. Strežniška koda izgleda tako:

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

    in zato vaša koda odjemalca izgleda takole, da ustreza tistemu, kar je deklarirano na strežniku:

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
# Preberi vir
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Pokliči orodje
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

V zgornji kodi smo:

- Poklicali vir z imenom `greeting` z uporabo `read_resource`.
- Poklicali orodje z imenom `add` z uporabo `call_tool`.

#### .NET

1. Dodajmo nekaj kode za klic orodja:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Za izpis rezultata pa nekaj kode za obdelavo:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Pokliči različna orodja kalkulatorja
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

- Poklicali več kalkulacijskih orodij z metodo `callTool()` s predmeti `CallToolRequest`.
- Vsak klic orodja določa ime orodja in `Map` argumentov, ki jih orodje zahteva.
- Strežniška orodja pričakujejo specifična imena parametrov (kot "a", "b" za matematične operacije).
- Rezultati so vrnjeni kot objekti `CallToolResult`, ki vsebujejo odziv strežnika.

#### Rust

```rust
// Pokliči orodje add z argumenti = {"a": 3, "b": 2}
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

Za zagon odjemalca v terminal vpišite naslednji ukaz:

#### TypeScript

Dodajte naslednji vnos v vaš odsek "scripts" v *package.json*:

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

Najprej zagotovite, da vaš MCP strežnik teče na `http://localhost:8080`. Nato zaženite odjemalca:

```bash
# Zgradi svoj projekt
./mvnw clean compile

# Zaženi odjemalca
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Lahko pa zaženete celoten projekt odjemalca, ki je na voljo v mapi rešitve `03-GettingStarted\02-client\solution\java`:

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

V tej nalogi boste uporabili naučeno za ustvarjanje svojega odjemalca.

Tukaj je strežnik, ki ga lahko uporabite in ga morate poklicati preko vaše kode odjemalca. Poskusite dodati več funkcionalnosti strežniku, da bo bolj zanimiv.

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

// Dodaj dinamični vir pozdravov
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


# Dodaj dinamični vir pozdrava
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

V [predhodnem poglavju](../../../../03-GettingStarted/01-first-server) ste se naučili, kako ustvariti preprost MCP strežnik z Rustom. Lahko nadaljujete z razvojem tega ali preverite to povezavo za več primerov MCP strežnikov z Rustom: [Primeri MCP strežnikov](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rešitev

**Mapa rešitve** vsebuje popolne, takoj za zagon pripravljene implementacije odjemalcev, ki prikazujejo vse pojme obravnavane v tem tutorialu. Vsaka rešitev vključuje kodo odjemalca in strežnika, organizirano v ločenih, samostojnih projektih.

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

Vsaka jezikovno specifična rešitev ponuja:

- **Popolno implementacijo odjemalca** z vsemi funkcijami iz tutoriala
- **Delujočo strukturo projekta** s pravilnimi odvisnostmi in konfiguracijo
- **Skripte za gradnjo in zagon** za enostavno nastavitev in izvajanje
- **Podroben README** z navodili po jeziku
- **Primere obdelave napak** in rezultatov

### 📖 Uporaba rešitev

1. **Pomaknite se v mapo za želeni programski jezik**:

   ```bash
   cd solution/typescript/    # Za TypeScript
   cd solution/java/          # Za Javo
   cd solution/python/        # Za Python
   cd solution/dotnet/        # Za .NET
   ```

2. **Sledite navodilom v README v vsaki mapi za:**
   - Namestitev odvisnosti
   - Gradnjo projekta
   - Zagon odjemalca

3. **Primer izhoda, ki ga morate videti:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za popolno dokumentacijo in navodila korak za korakom, glejte: **[📖 Dokumentacija rešitve](./solution/README.md)**

## 🎯 Popolni primeri

Pripravili smo popolne, delujoče implementacije odjemalcev za vse programske jezike, obravnavane v tem tutorialu. Ti primeri prikazujejo vso zgoraj opisano funkcionalnost in jih lahko uporabite kot referenčne implementacije ali izhodišča za lastne projekte.

### Na voljo popolni primeri

| Jezik | Datoteka | Opis |
|--------|----------|------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Popoln Java odjemalec s SSE prenosom in obsežnim ravnanjem z napakami |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Popoln C# odjemalec s stdio prenosom in samodejnim zagonom strežnika |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Popoln TypeScript odjemalec s podporo za MCP protokol v celoti |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Popoln Python odjemalec z uporabo async/await vzorcev |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Popoln Rust odjemalec z uporabo Tokio za asinhrone operacije |

Vsak popoln primer vključuje:
- ✅ **Vzpostavitev povezave** in obravnava napak
- ✅ **Odkritje strežnika** (orodja, viri, pozivi kjer je primerno)
- ✅ **Operacije kalkulatorja** (seštevanje, odštevanje, množenje, deljenje, pomoč)
- ✅ **Obdelava rezultatov** in oblikovani izpis
- ✅ **Celovita obravnava napak**
- ✅ **Čista, dokumentirana koda** s korak za korakom komentarji

### Začetek z dokončnimi primeri

1. **Izberite želeni jezik** iz tabele zgoraj
2. **Preglejte datoteko z dokončnim primerom**, da razumete celotno implementacijo
3. **Zaženite primer** sledite navodilom v [`complete_examples.md`](./complete_examples.md)
4. **Prilagodite in razširite** primer za vaš specifičen primer uporabe

Za podrobno dokumentacijo o zagonu in prilagajanju teh primerov si oglejte: **[📖 Dokumentacija dokončnih primerov](./complete_examples.md)**

### 💡 Rešitev proti dokončnim primerom

| **Mapa z rešitvijo** | **Dokončni primeri** |
|---------------------|--------------------- |
| Celotna struktura projekta z datotekami za gradnjo | Izvedbe v eni datoteki |
| Pripravljeno za zagon z odvisnostmi | Osredotočeni primeri kode |
| Okolje podobno proizvodnemu | Izobraževalni referenčni primer |
| Orodja specifična za jezik | Primerjava med jeziki |

Oba pristopa sta dragocena – uporabite **mapo z rešitvijo** za celovite projekte in **dokončne primere** za učenje in referenco.

## Ključne ugotovitve

Ključne ugotovitve za to poglavje o klientih so naslednje:

- Uporabljajo se lahko za odkrivanje in klicanje funkcionalnosti na strežniku.
- Lahko zaženejo strežnik, medtem ko se sami sprožijo (kot v tem poglavju), vendar se lahko klienti povežejo tudi na že delujoče strežnike.
- So odličen način za preizkus zmožnosti strežnika poleg alternativ, kot je Inspector, kot je bilo opisano v prejšnjem poglavju.

## Dodatni viri

- [Gradnja klientov v MCP](https://modelcontextprotocol.io/quickstart/client)

## Vzorci

- [Java kalkulator](../samples/java/calculator/README.md)
- [.Net kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulator](../../../../03-GettingStarted/samples/rust)

## Kaj sledi

- Naslednje: [Ustvarjanje klienta z LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
Ta dokument je bil preveden z uporabo avtomatske prevajalske storitve AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
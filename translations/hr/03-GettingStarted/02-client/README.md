# Kreiranje klijenta

Klijenti su prilagođene aplikacije ili skripte koje komuniciraju izravno s MCP poslužiteljem kako bi zatražili resurse, alate i upite. Za razliku od korištenja alata za inspekciju, koji pruža grafičko sučelje za interakciju s poslužiteljem, pisanje vlastitog klijenta omogućuje programsku i automatiziranu interakciju. Ovo omogućuje programerima integraciju MCP mogućnosti u vlastite radne procese, automatizaciju zadataka i izgradnju prilagođenih rješenja prilagođenih specifičnim potrebama.

## Pregled

Ova lekcija uvodi koncept klijenata unutar ekosustava Model Context Protocol (MCP). Naučit ćete kako napisati vlastiti klijent i povezati ga s MCP poslužiteljem.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Razumjeti što klijent može raditi.
- Napisati vlastiti klijent.
- Povezati i testirati klijenta s MCP poslužiteljem kako biste osigurali da poslužitelj radi kako se očekuje.

## Što je potrebno za pisanje klijenta?

Za pisanje klijenta potrebno je učiniti sljedeće:

- **Uvesti odgovarajuće biblioteke**. Koristit ćete istu biblioteku kao i prije, samo različite konstrukte.
- **Instancirati klijenta**. Ovo uključuje stvaranje instance klijenta i povezivanje s odabranom metodom prijenosa.
- **Odlučiti koje resurse popisati**. Vaš MCP poslužitelj dolazi s resursima, alatima i upitima, a vi trebate odlučiti koje od njih popisati.
- **Integrirati klijenta u glavnu aplikaciju**. Kada saznate mogućnosti poslužitelja, trebate ga integrirati u glavnu aplikaciju tako da, ako korisnik unese upit ili drugu naredbu, odgovarajuća značajka poslužitelja bude pozvana.

Sada kada razumijemo na visokoj razini što ćemo raditi, pogledajmo sljedeći primjer.

### Primjer klijenta

Pogledajmo ovaj primjer klijenta:

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

U prethodnom kodu:

- Uvozimo biblioteke.
- Kreiramo instancu klijenta i povezujemo je koristeći stdio za prijenos.
- Popisujemo upite, resurse i alate te ih sve pozivamo.

Evo ga, klijent koji može komunicirati s MCP poslužiteljem.

U sljedećem odjeljku vježbi uzet ćemo si vremena da razložimo svaki isječak koda i objasnimo što se događa.

## Vježba: Pisanje klijenta

Kao što je već rečeno, uzet ćemo si vremena da objasnimo kod, a vi slobodno kodirajte zajedno s nama ako želite.

### -1- Uvoz biblioteka

Uvezimo biblioteke koje su nam potrebne. Trebat će nam reference na klijenta i na odabrani protokol prijenosa, stdio. stdio je protokol za stvari koje se pokreću na vašem lokalnom računalu. SSE je još jedan protokol prijenosa koji ćemo pokazati u budućim poglavljima, ali to je vaša druga opcija. Za sada, nastavimo sa stdio.

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

Za Javu ćete kreirati klijenta koji se povezuje s MCP poslužiteljem iz prethodne vježbe. Koristeći istu strukturu Java Spring Boot projekta iz [Početak rada s MCP poslužiteljem](../../../../03-GettingStarted/01-first-server/solution/java), kreirajte novu Java klasu pod nazivom `SDKClient` u mapi `src/main/java/com/microsoft/mcp/sample/client/` i dodajte sljedeće uvoze:

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

Trebat ćete dodati sljedeće ovisnosti u svoju `Cargo.toml` datoteku.

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

Nakon toga, možete uvesti potrebne biblioteke u svoj klijentski kod.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Prijeđimo na instanciranje.

### -2- Instanciranje klijenta i prijenosa

Trebat ćemo kreirati instancu prijenosa i našeg klijenta:

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

U prethodnom kodu:

- Kreirali smo instancu stdio prijenosa. Obratite pažnju kako specificira naredbu i argumente za pronalaženje i pokretanje poslužitelja, jer je to nešto što ćemo trebati učiniti dok kreiramo klijenta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instancirali smo klijenta dajući mu ime i verziju.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Povezali klijenta s odabranim prijenosom.

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

U prethodnom kodu:

- Uvezli smo potrebne biblioteke.
- Instancirali objekt parametara poslužitelja jer ćemo ga koristiti za pokretanje poslužitelja kako bismo se mogli povezati s njim putem klijenta.
- Definirali metodu `run` koja poziva `stdio_client` za pokretanje klijentske sesije.
- Kreirali ulaznu točku gdje pružamo metodu `run` funkciji `asyncio.run`.

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

U prethodnom kodu:

- Uvezli smo potrebne biblioteke.
- Kreirali stdio prijenos i klijenta `mcpClient`. Ovo posljednje koristit ćemo za popis i pozivanje značajki na MCP poslužitelju.

Napomena: U "Arguments" možete ukazati na *.csproj* ili na izvršnu datoteku.

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

U prethodnom kodu:

- Kreirali smo glavnu metodu koja postavlja SSE prijenos usmjeren na `http://localhost:8080`, gdje će MCP poslužitelj biti pokrenut.
- Kreirali klasu klijenta koja uzima prijenos kao parametar konstruktora.
- U metodi `run` kreiramo sinkroni MCP klijent koristeći prijenos i inicijaliziramo vezu.
- Koristili SSE (Server-Sent Events) prijenos koji je prikladan za HTTP komunikaciju s Java Spring Boot MCP poslužiteljima.

#### Rust

Ovaj Rust klijent pretpostavlja da je poslužitelj sestrinski projekt nazvan "calculator-server" u istom direktoriju. Kod ispod pokrenut će poslužitelj i povezati se s njim.

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

### -3- Popis značajki poslužitelja

Sada imamo klijenta koji se može povezati ako se program pokrene. Međutim, on zapravo ne popisuje svoje značajke, pa to učinimo sljedeće:

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

Ovdje popisujemo dostupne resurse, `list_resources()` i alate, `list_tools`, te ih ispisujemo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Gore je primjer kako možemo popisati alate na poslužitelju. Za svaki alat zatim ispisujemo njegovo ime.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

U prethodnom kodu:

- Pozvali smo `listTools()` za dobivanje svih dostupnih alata s MCP poslužitelja.
- Koristili `ping()` za provjeru radi li veza s poslužiteljem.
- `ListToolsResult` sadrži informacije o svim alatima, uključujući njihova imena, opise i ulazne sheme.

Odlično, sada smo zabilježili sve značajke. Sada je pitanje kada ih koristiti? Ovaj klijent je prilično jednostavan, u smislu da ćemo morati eksplicitno pozvati značajke kada ih želimo. U sljedećem poglavlju kreirat ćemo napredniji klijent koji ima pristup vlastitom velikom jezičnom modelu (LLM). Za sada, pogledajmo kako možemo pozvati značajke na poslužitelju:

#### Rust

U glavnoj funkciji, nakon inicijalizacije klijenta, možemo inicijalizirati poslužitelj i popisati neke od njegovih značajki.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pozivanje značajki

Za pozivanje značajki trebamo osigurati da specificiramo ispravne argumente i, u nekim slučajevima, ime onoga što pokušavamo pozvati.

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

U prethodnom kodu:

- Čitamo resurs pozivajući `readResource()` i specificirajući `uri`. Evo kako to najvjerojatnije izgleda na strani poslužitelja:

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

    Naša vrijednost `uri` `file://example.txt` odgovara `file://{name}` na poslužitelju. `example.txt` će biti mapiran na `name`.

- Pozivamo alat specificirajući njegovo `name` i `arguments` ovako:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Dobivamo upit pozivajući `getPrompt()` s `name` i `arguments`. Kod poslužitelja izgleda ovako:

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

    i vaš klijentski kod izgleda ovako kako bi odgovarao onome što je deklarirano na poslužitelju:

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

U prethodnom kodu:

- Pozvali smo resurs nazvan `greeting` koristeći `read_resource`.
- Pozvali alat nazvan `add` koristeći `call_tool`.

#### .NET

1. Dodajmo kod za pozivanje alata:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Za ispis rezultata, evo koda koji to omogućuje:

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

U prethodnom kodu:

- Pozvali smo više alata kalkulatora koristeći metodu `callTool()` s objektima `CallToolRequest`.
- Svaki poziv alata specificira ime alata i `Map` argumenata potrebnih za taj alat.
- Alati poslužitelja očekuju specifična imena parametara (poput "a", "b" za matematičke operacije).
- Rezultati se vraćaju kao `CallToolResult` objekti koji sadrže odgovor poslužitelja.

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

### -5- Pokretanje klijenta

Za pokretanje klijenta, unesite sljedeću naredbu u terminal:

#### TypeScript

Dodajte sljedeći unos u odjeljak "scripts" u *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Pokrenite klijenta sljedećom naredbom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Prvo, osigurajte da vaš MCP poslužitelj radi na `http://localhost:8080`. Zatim pokrenite klijenta:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativno, možete pokrenuti cijeli projekt klijenta dostupan u mapi rješenja `03-GettingStarted\02-client\solution\java`:

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

## Zadatak

U ovom zadatku koristit ćete ono što ste naučili o kreiranju klijenta, ali ćete kreirati vlastitog klijenta.

Evo poslužitelja kojeg možete koristiti i kojeg trebate pozvati putem svog klijentskog koda. Pokušajte dodati više značajki poslužitelju kako bi bio zanimljiviji.

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

Pogledajte ovaj projekt kako biste vidjeli kako možete [dodati upite i resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Također, provjerite ovaj link za pozivanje [upita i resursa](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

U [prethodnom odjeljku](../../../../03-GettingStarted/01-first-server) naučili ste kako kreirati jednostavan MCP poslužitelj s Rustom. Možete nastaviti graditi na tome ili provjeriti ovaj link za više primjera MCP poslužitelja temeljenih na Rustu: [Primjeri MCP poslužitelja](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rješenje

**Mapa rješenja** sadrži kompletne, spremne za pokretanje implementacije klijenata koje demonstriraju sve koncepte obrađene u ovom vodiču. Svako rješenje uključuje i klijentski i poslužiteljski kod organiziran u odvojene, samostalne projekte.

### 📁 Struktura rješenja

Direktorij rješenja organiziran je prema programskom jeziku:

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

### 🚀 Što svako rješenje uključuje

Svako rješenje specifično za jezik pruža:

- **Kompletnu implementaciju klijenta** sa svim značajkama iz vodiča.
- **Radnu strukturu projekta** s odgovarajućim ovisnostima i konfiguracijom.
- **Skripte za izgradnju i pokretanje** za jednostavno postavljanje i izvršavanje.
- **Detaljan README** s uputama specifičnim za jezik.
- **Primjere obrade pogrešaka** i rezultata.

### 📖 Korištenje rješenja

1. **Navigirajte do mape za željeni jezik**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Slijedite upute iz README datoteke** u svakoj mapi za:
   - Instalaciju ovisnosti
   - Izgradnju projekta
   - Pokretanje klijenta

3. **Primjer izlaza** koji biste trebali vidjeti:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za potpunu dokumentaciju i upute korak po korak, pogledajte: **[📖 Dokumentacija rješenja](./solution/README.md)**

## 🎯 Kompletni primjeri

Pružili smo kompletne, funkcionalne implementacije klijenata za sve programske jezike obrađene u ovom vodiču. Ovi primjeri demonstriraju punu funkcionalnost opisanu gore i mogu se koristiti kao referentne implementacije ili početne točke za vaše vlastite projekte.

### Dostupni kompletni primjeri

| Jezik      | Datoteka                          | Opis                                                                 |
|------------|-----------------------------------|----------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletan Java klijent koristeći SSE prijenos s opsežnim rukovanjem pogreškama |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletan C# klijent koristeći stdio prijenos s automatskim pokretanjem poslužitelja |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletan TypeScript klijent s punom podrškom za MCP protokol       |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletan Python klijent koristeći async/await obrasce              |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Kompletan Rust klijent koristeći Tokio za asinhrone operacije       |
Svaki potpuni primjer uključuje:

- ✅ **Uspostavljanje veze** i rukovanje pogreškama
- ✅ **Otkrivanje poslužitelja** (alati, resursi, upiti gdje je primjenjivo)
- ✅ **Operacije kalkulatora** (zbrajanje, oduzimanje, množenje, dijeljenje, pomoć)
- ✅ **Obrada rezultata** i formatirani ispis
- ✅ **Sveobuhvatno rukovanje pogreškama**
- ✅ **Čist, dokumentiran kod** s komentarima korak po korak

### Početak rada s potpunim primjerima

1. **Odaberite željeni jezik** iz tablice iznad
2. **Pregledajte datoteku s potpunim primjerom** kako biste razumjeli cijelu implementaciju
3. **Pokrenite primjer** slijedeći upute u [`complete_examples.md`](./complete_examples.md)
4. **Prilagodite i proširite** primjer za svoj specifični slučaj upotrebe

Za detaljnu dokumentaciju o pokretanju i prilagodbi ovih primjera, pogledajte: **[📖 Dokumentacija potpunih primjera](./complete_examples.md)**

### 💡 Rješenje vs. Potpuni primjeri

| **Mapa rješenja** | **Potpuni primjeri** |
|--------------------|--------------------- |
| Cijela struktura projekta s datotekama za izgradnju | Implementacije u jednoj datoteci |
| Spremno za pokretanje s ovisnostima | Fokusirani primjeri koda |
| Postavka nalik produkciji | Edukativna referenca |
| Alati specifični za jezik | Usporedba među jezicima |

Oba pristupa su vrijedna - koristite **mapu rješenja** za potpune projekte, a **pune primjere** za učenje i referencu.

## Ključne točke

Ključne točke ovog poglavlja o klijentima su sljedeće:

- Mogu se koristiti za otkrivanje i pozivanje funkcionalnosti na poslužitelju.
- Mogu pokrenuti poslužitelj dok se sami pokreću (kao u ovom poglavlju), ali klijenti se također mogu povezati s već pokrenutim poslužiteljima.
- Izvrsni su za testiranje mogućnosti poslužitelja uz alternative poput Inspectora, kako je opisano u prethodnom poglavlju.

## Dodatni resursi

- [Izrada klijenata u MCP-u](https://modelcontextprotocol.io/quickstart/client)

## Primjeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Što slijedi

- Sljedeće: [Izrada klijenta s LLM-om](../03-llm-client/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
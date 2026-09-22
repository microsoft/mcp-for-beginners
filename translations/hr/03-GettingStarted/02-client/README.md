# Kreiranje klijenta

Klijenti su prilagođene aplikacije ili skripte koje komuniciraju izravno s MCP Serverom za zahtjev resursa, alata i upita. Za razliku od korištenja alata inspektora koji pruža grafičko sučelje za interakciju sa serverom, pisanje vlastitog klijenta omogućuje programske i automatizirane interakcije. To programerima omogućuje integraciju MCP mogućnosti u vlastite radne tokove, automatizaciju zadataka i izgradnju prilagođenih rješenja usklađenih s posebnim potrebama.

## Pregled

Ova lekcija uvodi koncept klijenata u ekosustavu Model Context Protocol (MCP). Naučit ćete kako napisati vlastiti klijent i povezati ga s MCP Serverom.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Razumjeti što klijent može raditi.
- Napisati vlastitog klijenta.
- Povezati i testirati klijenta s MCP serverom kako biste osigurali da server radi kako se očekuje.

## Što je potrebno za pisanje klijenta?

Za pisanje klijenta potrebno je sljedeće:

- **Uvesti prave biblioteke**. Koristit ćete istu biblioteku kao i prije, samo različite konstrukte.
- **Stvoriti instancu klijenta**. To uključuje stvaranje instance klijenta i njegovo povezivanje s odabranim transportnim načinom.
- **Odlučiti koje resurse navesti**. Vaš MCP server dolazi s resursima, alatima i upitima, potrebno je odlučiti koje ćete navesti.
- **Integrirati klijenta u aplikaciju domaćina**. Kada znate mogućnosti servera, potrebno ih je integrirati u vašu aplikaciju domaćina tako da kad korisnik unese upit ili drugu naredbu pozove odgovarajuću funkciju servera.

Sad kad razumijemo na visokoj razini što ćemo raditi, pogledajmo sljedeći primjer.

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

// Popis upita
const prompts = await client.listPrompts();

// Dohvati upit
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Popis resursa
const resources = await client.listResources();

// Pročitaj resurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Pozovi alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

U prethodnom kodu smo:

- Uvezli biblioteke
- Stvorili instancu klijenta i povezali je koristeći stdio kao transport.
- Naveli upite, resurse i alate te ih pozvali sve.

Eto ga, klijent koji može razgovarati s MCP Serverom.

U sljedećem odjeljku s vježbama ćemo polako razložiti svaki dio koda i objasniti što se događa.

## Vježba: Pisanje klijenta

Kao što je rečeno, uzimat ćemo vremena za objašnjenje koda, a slobodno napišite kôd uz nas ako želite.

### -1- Uvoz biblioteka

Uvezimo biblioteke koje su nam potrebne, trebat će nam reference na klijenta i na izabrani transportni protokol, stdio. stdio je protokol za stvari koje se pokreću na vašem lokalnom računalu. SSE je drugi transportni protokol koji ćemo pokazati u budućim poglavljima, ali to je vaša druga opcija. Za sada, nastavljamo sa stdio.

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

Za Javu, stvorit ćete klijenta koji se povezuje s MCP serverom iz prethodne vježbe. Koristeći istu Java Spring Boot strukturu projekta iz [Uvod u MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), stvorite novu Java klasu pod nazivom `SDKClient` u mapi `src/main/java/com/microsoft/mcp/sample/client/` i dodajte sljedeće importove:

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

Trebat ćete dodati sljedeće ovisnosti u datoteku `Cargo.toml`.

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

Iz toga možete uvesti potrebne biblioteke u kod klijenta.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Idemo na inicijalizaciju.

### -2- Inicijalizacija klijenta i transporta

Morat ćemo stvoriti instancu transporta i klijenta:

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

U prethodnom kodu smo:

- Stvorili instancu stdio transporta. Primijetite kako se specificiraju naredba i argumenti za pronalaženje i pokretanje servera jer to ćemo trebati napraviti dok stvaramo klijenta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Inicijalizirali klijenta dajući mu ime i verziju.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Povezali klijenta s odabranim transportom.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Stvori parametre poslužitelja za stdio vezu
server_params = StdioServerParameters(
    command="mcp",  # Izvršna datoteka
    args=["run", "server.py"],  # Neobavezni argumenti komandne linije
    env=None,  # Neobavezne varijable okoline
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicijaliziraj vezu
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

U prethodnom kodu smo:

- Importirali potrebne biblioteke
- Inicijalizirali objekt parametara servera jer ćemo ga koristiti za pokretanje servera kako bismo se mogli povezati s njim putem klijenta.
- Definirali metodu `run` koja poziva `stdio_client` koja pokreće klijentsku sesiju.
- Stvorili ulaznu točku gdje metodu `run` prosljeđujemo `asyncio.run`.

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

U prethodnom kodu smo:

- Importirali potrebne biblioteke.
- Stvorili stdio transport i klijenta `mcpClient`. Ovaj drugi koristit ćemo za pregled i pozivanje značajki MCP Servera.

Napomena, u "Arguments" možete pokazati ili na *.csproj* ili na izvršnu datoteku.

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
        
        // Vaša klijentska logika ide ovdje
    }
}
```

U prethodnom kodu smo:

- Stvorili glavnu metodu koja postavlja SSE transport usmjeren na `http://localhost:8080` gdje će naš MCP server raditi.
- Stvorili klasu klijenta koja prima transport kao parametar konstruktora.
- U metodi `run` stvaramo sinkroni MCP klijent koristeći transport i inicijaliziramo vezu.
- Koristili SSE (Server-Sent Events) transport koji je prikladan za HTTP komunikaciju s Java Spring Boot MCP serverima.

#### Rust

Napomena: ovaj Rust klijent pretpostavlja da je server projekt sestrinski, pod nazivom "calculator-server" u istoj mapi. Dolje navedeni kod će pokrenuti server i povezati se s njim.

```rust
async fn main() -> Result<(), RmcpError> {
    // Pretpostavite da je poslužitelj sestrinski projekt nazvan "calculator-server" u istom direktoriju
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

    // TODO: Inicijaliziraj

    // TODO: Nabroji alate

    // TODO: Pozovi alat add s argumentima = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Navođenje značajki servera

Sada imamo klijenta koji se može spojiti ako se program pokrene. Međutim, on zapravo ne navodi njegove značajke pa to napravimo sljedeće:

#### TypeScript

```typescript
// Popis upita
const prompts = await client.listPrompts();

// Popis resursa
const resources = await client.listResources();

// popis alata
const tools = await client.listTools();
```

#### Python

```python
# Prikaži dostupne resurse
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Prikaži dostupne alate
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Ovdje navodimo dostupne resurse, `list_resources()` i alate, `list_tools` te ih ispisujemo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Gore je primjer kako možemo navesti alate na serveru. Za svaki alat ispisujemo njegovo ime.

#### Java

```java
// Nabrojite i demonstrirajte alate
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Također možete pingati poslužitelj za provjeru veze
client.ping();
```

U prethodnom kodu smo:

- Pozvali `listTools()` za dobivanje svih dostupnih alata s MCP servera.
- Koristili `ping()` za provjeru radi li veza sa serverom.
- `ListToolsResult` sadrži informacije o svim alatima uključujući njihova imena, opise i ulazne sheme.

Super, sada smo dohvatili sve značajke. Sad pitanje je kada ih koristiti? Ovaj klijent je prilično jednostavan, jednostavan u smislu da ćemo morati izričito pozivati značajke kad ih želimo. U sljedećem poglavlju ćemo napraviti naprednijeg klijenta koji ima pristup vlastitom velikom jezičnom modelu, LLM-u. Za sada, pogledajmo kako pozvati značajke na serveru:

#### Rust

U glavnoj funkciji, nakon inicijalizacije klijenta, možemo inicijalizirati i server te navesti neke od njegovih značajki.

```rust
// Inicijaliziraj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Popis alata
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pozivanje značajki

Da bismo pozvali značajke, moramo osigurati da navedemo ispravne argumente, a u nekim slučajevima i ime onoga što želimo pozvati.

#### TypeScript

```typescript

// Pročitaj resurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Pozovi alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// pozovi prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

U prethodnom kodu smo:

- Pročitali resurs, pozvali smo resurs pozivom `readResource()` uz navođenje `uri`. Evo kako to najvjerojatnije izgleda na strani servera:

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

    Naša vrijednost `uri` `file://example.txt` odgovara `file://{name}` na serveru. `example.txt` će biti mapiran na `name`.

- Pozvali alat, pozivamo ga navodeći njegovo `name` i `arguments` ovako:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Dohvatili upit, za dobivanje upita pozivamo `getPrompt()` s `name` i `arguments`. Kôd servera izgleda ovako:

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

    Vaš rezultirajući klijentski kod izgleda ovako da se podudara s onim što je deklarirano na serveru:

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
# Pročitaj resurs
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Pozovi alat
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

U prethodnom kodu smo:

- Pozvali resurs nazvan `greeting` pomoću `read_resource`.
- Pozvali alat nazvan `add` pomoću `call_tool`.

#### .NET

1. Dodajmo kôd za pozivanje alata:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Za ispis rezultata, evo koda za to:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Pozovite razne alate kalkulatora
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

U prethodnom kodu smo:

- Pozvali više kalkulatorskih alata koristeći `callTool()` metodu s objektima `CallToolRequest`.
- Svaki poziv alata specificira ime alata i `Map` argumenata potrebnih za taj alat.
- Alati na serveru očekuju specifične nazive parametara (poput "a", "b" za matematičke operacije).
- Rezultati se vraćaju kao objekti `CallToolResult` koji sadrže odgovor servera.

#### Rust

```rust
// Pozovi add alat s argumentima = {"a": 3, "b": 2}
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

Za pokretanje klijenta unesite sljedeću naredbu u terminal:

#### TypeScript

Dodajte sljedeći unos u "scripts" sekciju u *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Pokrenite klijenta s ovom naredbom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Prvo osigurajte da vaš MCP server radi na `http://localhost:8080`. Zatim pokrenite klijenta:

```bash
# Izgradite svoj projekt
./mvnw clean compile

# Pokrenite klijenta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativno, možete pokrenuti kompletan klijentski projekt iz mape rješenja `03-GettingStarted\02-client\solution\java`:

```bash
# Idite do direktorija rješenja
cd 03-GettingStarted/02-client/solution/java

# Izgradite i pokrenite JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Zadatak

U ovom zadatku koristiti ćete naučeno o stvaranju klijenta, ali ćete napraviti vlastitog klijenta.

Evo server kojeg možete koristiti, a trebate ga pozvati putem vašeg klijentskog koda. Pokušajte dodati više značajki serveru da ga učinite zanimljivijim.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Kreiraj MCP poslužitelj
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Dodaj alat za zbrajanje
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dinamički resurs pozdrava
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

// Počni primati poruke na stdin i slati poruke na stdout

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

# Kreiraj MCP poslužitelj
mcp = FastMCP("Demo")


# Dodaj alat za zbrajanje
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Dodaj dinamički resurs za pozdrav
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

Pogledajte ovaj projekt da vidite kako možete [dodati upite i resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Također, pogledajte ovaj link kako pozvati [upite i resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

U [prethodnom odjeljku](../../../../03-GettingStarted/01-first-server) naučili ste kako napraviti jednostavan MCP server s Rustom. Možete nastaviti graditi na tome ili pogledati ovaj link za više primjera MCP servera baziranih na Rustu: [MCP Server Primjeri](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rješenje

**Mapa rješenja** sadrži potpune, odmah iskoristive implementacije klijenata koje demonstriraju sve koncepte obrađene u ovom vodiču. Svako rješenje uključuje i klijentski i serverski kod organiziran u zasebne, samostalne projekte.

### 📁 Struktura rješenja

Mapa rješenja organizirana je prema programskom jeziku:

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

- **Potpunu implementaciju klijenta** sa svim značajkama iz vodiča
- **Ispravnu strukturu projekta** s pravim ovisnostima i konfiguracijom
- **Skripte za izgradnju i pokretanje** za jednostavnu konfiguraciju i izvršenje
- **Detaljni README** s uputama specifičnim za jezik
- **Primjere rukovanja pogreškama** i obrade rezultata

### 📖 Korištenje rješenja

1. **Navigirajte do mape vašeg željenog jezika**:

   ```bash
   cd solution/typescript/    # Za TypeScript
   cd solution/java/          # Za Javu
   cd solution/python/        # Za Python
   cd solution/dotnet/        # Za .NET
   ```

2. **Slijedite upute u README u svakoj mapi za**:
   - Instaliranje ovisnosti
   - Izgradnju projekta
   - Pokretanje klijenta

3. **Primjer izlaza** koji biste trebali vidjeti:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za potpunu dokumentaciju i upute korak po korak, pogledajte: **[📖 Dokumentacija rješenja](./solution/README.md)**

## 🎯 Potpuni primjeri

Osigurali smo kompletne, radne implementacije klijenata za sve programske jezike obrađene u ovom vodiču. Ovi primjeri demonstriraju punu funkcionalnost gore opisana i mogu se koristiti kao referentne implementacije ili početne točke za vaše vlastite projekte.

### Dostupni potpuni primjeri

| Jezik | Datoteka | Opis |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Potpuni Java klijent koristeći SSE transport sa sveobuhvatnim rukovanjem greškama |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Potpuni C# klijent koristeći stdio transport s automatskim pokretanjem servera |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Potpuni TypeScript klijent s punom podrškom za MCP protokol |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Potpuni Python klijent koristeći async/await obrasce |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Potpuni Rust klijent koristeći Tokio za async operacije |

Svaki potpuni primjer uključuje:

- ✅ **Uspostavljanje veze** i rukovanje greškama
- ✅ **Otkriće servera** (alati, resursi, upiti gdje je primjenjivo)
- ✅ **Kalkulatorske operacije** (zbrajanje, oduzimanje, množenje, dijeljenje, pomoć)
- ✅ **Obrada rezultata** i formatirani ispis
- ✅ **Sveobuhvatno rukovanje pogreškama**

- ✅ **Čist, dokumentiran kod** s komentarima korak po korak

### Početak s potpunim primjerima

1. **Odaberite svoj preferirani jezik** iz tablice gore
2. **Pregledajte kompletan primjer datoteke** da biste razumjeli punu implementaciju
3. **Pokrenite primjer** prateći upute u [`complete_examples.md`](./complete_examples.md)
4. **Izmijenite i proširite** primjer za vaš specifični slučaj korištenja

Za detaljnu dokumentaciju o pokretanju i prilagodbi ovih primjera, vidite: **[📖 Dokumentacija kompletnih primjera](./complete_examples.md)**

### 💡 Rješenje vs. Kompletni primjeri

| **Mapa rješenja** | **Kompletni primjeri** |
|--------------------|--------------------- |
| Cijela struktura projekta s build datotekama | Implementacije u jednoj datoteci |
| Spremno za pokretanje s ovisnostima | Fokusirani primjeri koda |
| Postavka nalik produkcijskoj | Edukativni referentni materijal |
| Alati specifični za jezik | Usporedba između jezika |

Oba pristupa su vrijedna - koristite **mapu rješenja** za kompletne projekte i **kompletne primjere** za učenje i referencu.

## Ključne napomene

Ključne napomene za ovo poglavlje o klijentima su sljedeće:

- Mogu se koristiti i za otkrivanje i za pozivanje značajki na poslužitelju.
- Mogu pokrenuti poslužitelj dok se sami pokreću (kao u ovom poglavlju), ali klijenti se također mogu spojiti na već pokrenute poslužitelje.
- Sjajan su način za testiranje sposobnosti poslužitelja uz alternative poput Inspektora kao što je opisano u prethodnom poglavlju.

## Dodatni resursi

- [Izgradnja klijenata u MCP-u](https://modelcontextprotocol.io/quickstart/client)

## Primjeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.NET Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Što slijedi

- Sljedeće: [Kreiranje klijenta s LLM-om](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
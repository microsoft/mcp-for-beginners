# Izrada klijenta

Klijenti su prilagođene aplikacije ili skripte koje izravno komuniciraju s MCP poslužiteljem za zahtjev resursa, alata i naznaka. Za razliku od korištenja alata inspektora koji pruža grafičko sučelje za interakciju s poslužiteljem, pisanje vlastitog klijenta omogućuje programske i automatizirane interakcije. To omogućava programerima integraciju MCP sposobnosti u svoje radne tokove, automatizaciju zadataka i izgradnju prilagođenih rješenja prilagođenih specifičnim potrebama.

## Pregled

Ova lekcija uvodi pojam klijenata unutar Model Context Protocol (MCP) ekosustava. Naučit ćete kako napisati vlastiti klijent i povezati ga s MCP poslužiteljem.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Razumjeti što klijent može učiniti.
- Napisati vlastiti klijent.
- Povezati se i testirati klijenta s MCP poslužiteljem kako biste osigurali da zadnji radi kako se očekuje.

## Što ide u pisanje klijenta?

Za pisanje klijenta, trebate učiniti sljedeće:

- **Uvoz ispravnih biblioteka**. Koristit ćete istu biblioteku kao i ranije, samo različite konstrukte.
- **Inicijalizirati klijenta**. To će uključivati kreiranje instance klijenta i povezivanje na odabranu metodu prijenosa.
- **Odlučiti koje resurse navesti**. Vaš MCP poslužitelj dolazi s resursima, alatima i naznakama, morate odlučiti koje ćete navesti.
- **Integrirati klijenta u glavnu aplikaciju**. Kad znate mogućnosti poslužitelja, trebate integrirati klijenta u glavnu aplikaciju tako da, ako korisnik unese naznaku ili drugi naredbeni zahtjev, odgovarajuća funkcija poslužitelja bude pozvana.

Sad kad razumijemo na visokim razinama što ćemo raditi, pogledajmo primjer.

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

// Dobiti upit
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Popis resursa
const resources = await client.listResources();

// Pročitati resurs
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Pozvati alat
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

U prethodnom kodu:

- Uvozimo biblioteke
- Kreiramo instancu klijenta i povezujemo je koristeći stdio kao transport.
- Navodimo naznake, resurse i alate te pozivamo sve.

Eto ga, klijent koji može komunicirati s MCP poslužiteljem.

Uzeti ćemo si vremena u sljedećoj vježbi da razložimo svaki dio koda i objasnimo što se događa.

## Vježba: Pisanje klijenta

Kao što je rečeno, uzet ćemo si vremena za objašnjenje koda, i svakako kodirajte zajedno ako želite.

### -1- Uvoz biblioteka

Uvezimo potrebne biblioteke, trebat će nam reference na klijenta i na odabrani transportni protokol, stdio. stdio je protokol za stvari koje se izvoze na vašem lokalnom računalu. SSE je drugi transportni protokol koji ćemo pokazati u budućim poglavljima, no to je vaša druga opcija. Za sada nastavljamo sa stdio-om.

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

Za Javu, kreirat ćete klijenta koji se povezuje na MCP poslužitelj iz prijašnje vježbe. Koristeći istu strukturu Java Spring Boot projekta iz [Uvod u MCP poslužitelj](../../../../03-GettingStarted/01-first-server/solution/java), stvorite novu Java klasu pod nazivom `SDKClient` u mapi `src/main/java/com/microsoft/mcp/sample/client/` i dodajte sljedeće uvoze:

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

Morat ćete dodati sljedeće ovisnosti u svoj `Cargo.toml` file.

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

Nakon toga možete uvesti potrebne biblioteke u vaš klijentski kod.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Nastavimo s instanciranjem.

### -2- Instanciranje klijenta i transporta

Morat ćemo stvoriti instancu transporta i instancu našeg klijenta:

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

- Kreirali smo instancu stdio transporta. Primijetite kako specificira naredbu i argumente za pronalazak i pokretanje poslužitelja jer je to nešto što ćemo morati napraviti pri kreiranju klijenta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instancirali klijenta dajući mu ime i verziju.

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

# Kreiraj parametre poslužitelja za stdio vezu
server_params = StdioServerParameters(
    command="mcp",  # Izvršna datoteka
    args=["run", "server.py"],  # Opcionalni argumenti naredbenog retka
    env=None,  # Opcionalne varijable okoline
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

- Uvezli potrebne biblioteke
- Instancirali objekt parametara poslužitelja koji ćemo koristiti za pokretanje poslužitelja da se možemo s njim povezati sa svojim klijentom.
- Definirali metodu `run` koja zauzvrat poziva `stdio_client` što pokreće klijentsku sesiju.
- Kreirali ulaznu točku gdje prosljeđujemo metodu `run` funkciji `asyncio.run`.

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

- Uvezli potrebne biblioteke.
- Kreirali stdio transport i instancirali klijenta `mcpClient`. Ovaj zadnji ćemo koristiti za popisivanje i pozivanje značajki na MCP poslužitelju.

Napomena, u "Arguments" možete navesti ili *.csproj* ili izvršnu datoteku.

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

- Kreirali main metodu koja postavlja SSE transport usmjeren na `http://localhost:8080` gdje će naš MCP poslužitelj biti pokrenut.
- Kreirali klasu klijenta koja prima transport kao parametar konstruktora.
- U metodi `run` kreirali sinhroni MCP klijent koristeći transport i inicijalizirali vezu.
- Koristili SSE (Server-Sent Events) transport koji je prikladan za HTTP komunikaciju s Java Spring Boot MCP poslužiteljima.

#### Rust

Ovaj Rust klijent pretpostavlja da je poslužitelj sestrinski projekt nazvan "calculator-server" u istoj direktoriji. Kod ispod pokreće poslužitelja i povezuje se s njim.

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

    // TODO: Pozovi alat za zbrajanje s argumentima = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Popisivanje značajki poslužitelja

Sada imamo klijenta koji se može povezati ako se program pokrene. No, zapravo ne navodi njegove značajke pa to učinimo sljedeće:

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
# Nabroji dostupne resurse
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Nabroji dostupne alate
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Ovdje navodimo dostupne resurse, `list_resources()` i alate, `list_tools` i ispisujemo ih.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Gore je primjer kako možemo navesti alate na poslužitelju. Za svaki alat ispisujemo njegov naziv.

#### Java

```java
// Navedite i pokažite alate
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Također možete poslati ping poslužitelju za provjeru veze
client.ping();
```

U prethodnom kodu smo:

- Pozvali `listTools()` da dobijemo sve dostupne alate s MCP poslužitelja.
- Koristili `ping()` da provjerimo radi li veza s poslužiteljem.
- `ListToolsResult` sadrži informacije o svim alatima uključujući njihova imena, opise i ulazne sheme.

Odlično, sada smo pokupili sve značajke. Sad pitanje je kada ih koristimo? Ovaj klijent je prilično jednostavan, jednostavan u smislu da ćemo morati eksplicitno pozvati značajke kada ih poželimo. U sljedećem poglavlju kreirat ćemo naprednijeg klijenta koji ima pristup svom velikom jezičnom modelu, LLM-u. Za sada, pogledajmo kako možemo pozvati značajke na poslužitelju:

#### Rust

U glavnoj funkciji, nakon inicijalizacije klijenta, možemo inicijalizirati poslužitelja i navesti neke njegove značajke.

```rust
// Inicijaliziraj
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Popis alata
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pozivanje značajki

Za pozivanje značajki moramo osigurati da specificiramo točne argumente i u nekim slučajevima ime onoga što pokušavamo pozvati.

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

// pozovi upit
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

U prethodnom kodu:

- Čitamo resurs, pozivamo resurs s `readResource()` specificirajući `uri`. Evo kako to najvjerojatnije izgleda s poslužiteljske strane:

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

    Naša `uri` vrijednost `file://example.txt` odgovara `file://{name}` na poslužitelju. `example.txt` će biti mapiran na `name`.

- Pozivamo alat, pozivamo ga specificirajući njegovo `name` i njegove `arguments` ovako:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Dohvaćamo naznaku, za naznaku pozivamo `getPrompt()` sa `name` i `arguments`. Kod poslužitelja izgleda ovako:

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

    a vaš klijentski kod stoga izgleda ovako da odgovara onome što je deklarirano na poslužitelju:

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

- Pozvali resurs zvan `greeting` koristeći `read_resource`.
- Pozvali alat zvan `add` koristeći `call_tool`.

#### .NET

1. Dodajmo malo koda za pozivanje alata:

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
// Pozovi razne alate kalkulatora
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

- Pozvali više kalkulatorskih alata koristeći metodu `callTool()` s objektima `CallToolRequest`.
- Svaki poziv alatu specificira ime alata i `Map` argumenata potrebnih za taj alat.
- Poslužiteljski alati očekuju specifična imena parametara (kao "a", "b" za matematičke operacije).
- Rezultati se vraćaju kao `CallToolResult` objekti koji sadrže odgovor od poslužitelja.

#### Rust

```rust
// Pozovi alat za zbrajanje s argumentima = {"a": 3, "b": 2}
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

### -5- Pokreni klijenta

Za pokretanje klijenta upišite sljedeću naredbu u terminal:

#### TypeScript

Dodajte sljedeći unos u svoj "scripts" odjeljak u *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Pozovite klijenta sljedećom naredbom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Prvo se uvjerite da je vaš MCP poslužitelj pokrenut na `http://localhost:8080`. Zatim pokrenite klijenta:

```bash
# Izgradite svoj projekt
./mvnw clean compile

# Pokrenite klijent
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativno, možete pokrenuti kompletan projekt klijenta iz rješenja u mapi `03-GettingStarted\02-client\solution\java`:

```bash
# Navigirajte do direktorija rješenja
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

U ovom zadatku koristit ćete ono što ste naučili o izradi klijenta, ali ćete kreirati vlastiti klijent.

Evo poslužitelja kojeg možete koristiti i kojeg trebate pozvati kroz svoj klijentski kod, pokušajte dodati više značajki poslužitelju kako bi bio zanimljiviji.

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

// Dodaj dodatni alat
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Dodaj dinamički resurs za pozdrav
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

// Započni primanje poruka na stdin i slanje poruka na stdout

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

Pogledajte ovaj projekt da vidite kako možete [dodati naznake i resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Također, provjerite ovaj link za način pozivanja [naznaka i resursa](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

U [prethodnom dijelu](../../../../03-GettingStarted/01-first-server) naučili ste kako kreirati jednostavan MCP poslužitelj u Rustu. Možete graditi dalje na tome ili provjeriti ovaj link za više Rust baziranih MCP primjera poslužitelja: [Primjeri MCP poslužitelja](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Rješenje

**Mapa rješenja** sadrži kompletne, spremne za pokretanje implementacije klijenata koje demonstriraju sve koncepte obrađene u ovom tutorijalu. Svako rješenje uključuje i klijentski i poslužiteljski kod organizirani u odvojene, samostalne projekte.

### 📁 Struktura rješenja

Direktorij rješenja organiziran je po programskim jezicima:

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

Svako rješenje za određeni jezik pruža:

- **Kompletna implementacija klijenta** sa svim značajkama iz tutorijala
- **Funkcionalna struktura projekta** s pravilnim ovisnostima i konfiguracijom
- **Skripte za izgradnju i pokretanje** za lakše postavljanje i izvođenje
- **Detaljan README** s uputama specifičnim za jezik
- **Primjere za upravljanje greškama** i obradu rezultata

### 📖 Korištenje rješenja

1. **Idite u mapu željenog jezika**:

   ```bash
   cd solution/typescript/    # Za TypeScript
   cd solution/java/          # Za Javu
   cd solution/python/        # Za Python
   cd solution/dotnet/        # Za .NET
   ```

2. **Slijedite upute u README-u** u svakoj mapi za:
   - Instalaciju ovisnosti
   - Izgradnju projekta
   - Pokretanje klijenta

3. **Primjer izlaza** koji biste trebali vidjeti:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Za potpunu dokumentaciju i upute korak po korak pogledajte: **[📖 Dokumentacija rješenja](./solution/README.md)**

## 🎯 Kompletni primjeri

Osigurali smo kompletne, funkcionalne implementacije klijenata za sve programske jezike obrađene u ovom tutorijalu. Ovi primjeri demonstriraju svu funkcionalnost navedenu gore i mogu se koristiti kao referentne implementacije ili polazne točke za vlastite projekte.

### Dostupni kompletni primjeri

| Jezik | Datoteka | Opis |
|----------|---------|---------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Potpuni Java klijent koristeći SSE transport s opsežnim upravljanjem greškama |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Potpuni C# klijent koristeći stdio transport s automatskim pokretanjem poslužitelja |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Potpuni TypeScript klijent s potpunom podrškom MCP protokola |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Potpuni Python klijent koristeći async/await obrasce |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Potpuni Rust klijent koristeći Tokio za asinhrone operacije |

Svaki kompletan primjer uključuje:
- ✅ **Uspostava veze** i rukovanje pogreškama
- ✅ **Otkrivanje servera** (alati, resursi, upiti gdje je primjenjivo)
- ✅ **Operacije kalkulatora** (zbrajanje, oduzimanje, množenje, dijeljenje, pomoć)
- ✅ **Obrada rezultata** i formatirani ispis
- ✅ **Sveobuhvatno rukovanje pogreškama**
- ✅ **Čist, dokumentiran kod** sa komentarima korak po korak

### Početak rada s potpunim primjerima

1. **Odaberite željeni jezik** iz gornje tablice
2. **Pregledajte datoteku potpunog primjera** kako biste razumjeli kompletnu implementaciju
3. **Pokrenite primjer** slijedeći upute u [`complete_examples.md`](./complete_examples.md)
4. **Izmijenite i proširite** primjer za svoj specifični slučaj upotrebe

Za detaljnu dokumentaciju o pokretanju i prilagodbi ovih primjera, pogledajte: **[📖 Dokumentacija potpunih primjera](./complete_examples.md)**

### 💡 Rješenje vs. Potpuni Primjeri

| **Mapa Rješenja** | **Potpuni Primjeri** |
|--------------------|--------------------- |
| Puna struktura projekta s build datotekama | Implementacije u jednoj datoteci |
| Spremno za pokretanje s ovisnostima | Fokusirani primjeri koda |
| Postavka slična produkciji | Edukativna referenca |
| Alati specifični za jezik | Usporedba među jezicima |

Oba pristupa su vrijedna – koristite **mapu rješenja** za kompletne projekte, a **potpune primjere** za učenje i referencu.

## Ključne poruke

Ključne poruke ovog poglavlja o klijentima su sljedeće:

- Mogu se koristiti i za otkrivanje i za pozivanje značajki na serveru.
- Mogu pokrenuti server dok se sami pokreću (kao u ovom poglavlju), ali klijenti se također mogu spojiti i na već pokrenute servere.
- Odličan su način za isprobavanje mogućnosti servera uz alternative poput Inspektora, kako je opisano u prethodnom poglavlju.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
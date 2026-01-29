# Vytvorenie klienta

Klienti sú vlastné aplikácie alebo skripty, ktoré priamo komunikujú s MCP Serverom za účelom požiadania o zdroje, nástroje a výzvy. Na rozdiel od použitia inšpekčného nástroja, ktorý poskytuje grafické rozhranie na interakciu so serverom, písanie vlastného klienta umožňuje programovateľné a automatizované interakcie. To umožňuje vývojárom integrovať schopnosti MCP do vlastných pracovných postupov, automatizovať úlohy a vytvárať vlastné riešenia prispôsobené konkrétnym potrebám.

## Prehľad

Táto lekcia predstavuje koncept klientov v rámci ekosystému Model Context Protocol (MCP). Naučíte sa, ako napísať vlastného klienta a pripojiť ho k MCP Serveru.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Pochopiť, čo klient dokáže.
- Napísať vlastného klienta.
- Pripojiť a otestovať klienta s MCP serverom, aby ste sa uistili, že funguje podľa očakávania.

## Čo zahŕňa písanie klienta?

Na napísanie klienta budete musieť vykonať nasledujúce kroky:

- **Importovať správne knižnice**. Budete používať rovnakú knižnicu ako predtým, len s inými konštruktmi.
- **Vytvoriť inštanciu klienta**. To zahŕňa vytvorenie inštancie klienta a pripojenie k zvolenému spôsobu prenosu.
- **Rozhodnúť sa, aké zdroje zoznamovať**. Váš MCP server obsahuje zdroje, nástroje a výzvy, musíte sa rozhodnúť, ktoré z nich zoznamovať.
- **Integrovať klienta do hostiteľskej aplikácie**. Keď poznáte schopnosti servera, musíte to integrovať do vašej hostiteľskej aplikácie tak, aby sa pri zadaní výzvy alebo iného príkazu používateľom spustila príslušná funkcia servera.

Teraz, keď máme vysokú predstavu o tom, čo ideme robiť, pozrime sa na príklad.

### Príklad klienta

Pozrime sa na tento príklad klienta:

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

V predchádzajúcom kóde sme:

- Importovali knižnice.
- Vytvorili inštanciu klienta a pripojili ju pomocou stdio na prenos.
- Zoznamovali výzvy, zdroje a nástroje a všetky ich spustili.

A je to, klient, ktorý dokáže komunikovať s MCP Serverom.

V ďalšej časti cvičenia si rozoberieme každý úryvok kódu a vysvetlíme, čo sa deje.

## Cvičenie: Písanie klienta

Ako bolo uvedené vyššie, venujme čas vysvetleniu kódu a pokojne si kódujte spolu s nami, ak chcete.

### -1- Import knižníc

Importujme knižnice, ktoré potrebujeme. Budeme potrebovať referencie na klienta a na nami zvolený prenosový protokol, stdio. stdio je protokol určený na spustenie na vašom lokálnom počítači. SSE je ďalší prenosový protokol, ktorý ukážeme v budúcich kapitolách, ale zatiaľ pokračujme so stdio.

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

Pre Javu vytvoríte klienta, ktorý sa pripojí k MCP serveru z predchádzajúceho cvičenia. Pomocou rovnakej štruktúry projektu Java Spring Boot z [Začíname s MCP Serverom](../../../../03-GettingStarted/01-first-server/solution/java) vytvorte novú triedu Java s názvom `SDKClient` v priečinku `src/main/java/com/microsoft/mcp/sample/client/` a pridajte nasledujúce importy:

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

Budete musieť pridať nasledujúce závislosti do vášho súboru `Cargo.toml`.

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

Odtiaľ môžete importovať potrebné knižnice do vášho klientského kódu.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Pokračujme inštanciou.

### -2- Inštancia klienta a prenosu

Budeme musieť vytvoriť inštanciu prenosu a inštanciu nášho klienta:

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

V predchádzajúcom kóde sme:

- Vytvorili inštanciu stdio prenosu. Všimnite si, ako špecifikuje príkaz a argumenty na nájdenie a spustenie servera, pretože to budeme potrebovať pri vytváraní klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Vytvorili inštanciu klienta zadaním názvu a verzie.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Pripojili klienta k zvolenému prenosu.

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

V predchádzajúcom kóde sme:

- Importovali potrebné knižnice.
- Vytvorili objekt parametrov servera, ktorý použijeme na spustenie servera, aby sme sa k nemu mohli pripojiť s naším klientom.
- Definovali metódu `run`, ktorá následne volá `stdio_client`, čo spustí klientsku reláciu.
- Vytvorili vstupný bod, kde poskytujeme metódu `run` do `asyncio.run`.

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

V predchádzajúcom kóde sme:

- Importovali potrebné knižnice.
- Vytvorili stdio prenos a klienta `mcpClient`. Ten použijeme na zoznamovanie a spúšťanie funkcií na MCP Serveri.

Poznámka: V "Arguments" môžete buď ukázať na *.csproj* alebo na spustiteľný súbor.

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

V predchádzajúcom kóde sme:

- Vytvorili hlavnú metódu, ktorá nastavuje SSE prenos smerujúci na `http://localhost:8080`, kde bude bežať náš MCP server.
- Vytvorili triedu klienta, ktorá prijíma prenos ako parameter konštruktora.
- V metóde `run` sme vytvorili synchronného MCP klienta pomocou prenosu a inicializovali pripojenie.
- Použili SSE (Server-Sent Events) prenos, ktorý je vhodný pre HTTP-komunikáciu s Java Spring Boot MCP servermi.

#### Rust

Tento Rust klient predpokladá, že server je súrodenecký projekt s názvom "calculator-server" v rovnakom adresári. Kód nižšie spustí server a pripojí sa k nemu.

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

### -3- Zoznamovanie funkcií servera

Teraz máme klienta, ktorý sa dokáže pripojiť, ak sa program spustí. Avšak, ešte nezoznamuje jeho funkcie, takže to urobme teraz:

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

Tu zoznamujeme dostupné zdroje pomocou `list_resources()` a nástroje pomocou `list_tools` a vypisujeme ich.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Vyššie je príklad, ako môžeme zoznamovať nástroje na serveri. Pre každý nástroj potom vypíšeme jeho názov.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

V predchádzajúcom kóde sme:

- Zavolali `listTools()` na získanie všetkých dostupných nástrojov z MCP servera.
- Použili `ping()` na overenie, že pripojenie k serveru funguje.
- `ListToolsResult` obsahuje informácie o všetkých nástrojoch vrátane ich názvov, popisov a vstupných schém.

Skvelé, teraz sme zachytili všetky funkcie. Otázka je, kedy ich použijeme? Tento klient je pomerne jednoduchý, jednoduchý v tom zmysle, že funkcie budeme musieť explicitne volať, keď ich budeme chcieť. V ďalšej kapitole vytvoríme pokročilejšieho klienta, ktorý bude mať prístup k vlastnému veľkému jazykovému modelu (LLM). Zatiaľ však uvidíme, ako môžeme spustiť funkcie na serveri:

#### Rust

V hlavnej funkcii, po inicializácii klienta, môžeme inicializovať server a zoznamovať niektoré jeho funkcie.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Spustenie funkcií

Na spustenie funkcií musíme zabezpečiť, že špecifikujeme správne argumenty a v niektorých prípadoch názov toho, čo sa snažíme spustiť.

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

V predchádzajúcom kóde sme:

- Čítali zdroj, voláme zdroj pomocou `readResource()` so špecifikovaním `uri`. Takto to pravdepodobne vyzerá na strane servera:

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

    Naša hodnota `uri` `file://example.txt` zodpovedá `file://{name}` na serveri. `example.txt` bude mapované na `name`.

- Volali nástroj, voláme ho špecifikovaním jeho `name` a jeho `arguments` takto:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Získali výzvu, na získanie výzvy voláme `getPrompt()` s `name` a `arguments`. Kód servera vyzerá takto:

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

    A váš výsledný klientský kód preto vyzerá takto, aby zodpovedal tomu, čo je deklarované na serveri:

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

V predchádzajúcom kóde sme:

- Zavolali zdroj s názvom `greeting` pomocou `read_resource`.
- Spustili nástroj s názvom `add` pomocou `call_tool`.

#### .NET

1. Pridajme kód na spustenie nástroja:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Na výpis výsledku pridajme kód na jeho spracovanie:

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

V predchádzajúcom kóde sme:

- Zavolali viacero kalkulačných nástrojov pomocou metódy `callTool()` s objektmi `CallToolRequest`.
- Každé volanie nástroja špecifikuje názov nástroja a `Map` argumentov požadovaných týmto nástrojom.
- Nástroje servera očakávajú konkrétne názvy parametrov (napríklad "a", "b" pre matematické operácie).
- Výsledky sú vrátené ako objekty `CallToolResult` obsahujúce odpoveď zo servera.

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

### -5- Spustenie klienta

Na spustenie klienta zadajte nasledujúci príkaz do terminálu:

#### TypeScript

Pridajte nasledujúci záznam do sekcie "scripts" v *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Spustite klienta nasledujúcim príkazom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najprv sa uistite, že váš MCP server beží na `http://localhost:8080`. Potom spustite klienta:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Prípadne môžete spustiť kompletný klientský projekt poskytnutý v riešení priečinka `03-GettingStarted\02-client\solution\java`:

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

## Zadanie

V tomto zadaní použijete to, čo ste sa naučili pri vytváraní klienta, ale vytvoríte vlastného klienta.

Tu je server, ktorý môžete použiť a ktorý musíte volať prostredníctvom vášho klientského kódu. Skúste pridať viac funkcií na server, aby bol zaujímavejší.

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

Pozrite si tento projekt, aby ste videli, ako môžete [pridať výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tiež si pozrite tento odkaz, ako spustiť [výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [predchádzajúcej sekcii](../../../../03-GettingStarted/01-first-server) ste sa naučili, ako vytvoriť jednoduchý MCP server s Rustom. Môžete na tom pokračovať alebo si pozrieť tento odkaz na ďalšie príklady MCP serverov založených na Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Riešenie

**Riešenie priečinka** obsahuje kompletné, pripravené na spustenie implementácie klientov, ktoré demonštrujú všetky koncepty pokryté v tomto tutoriáli. Každé riešenie obsahuje kód klienta aj servera organizovaný v samostatných, samostatných projektoch.

### 📁 Štruktúra riešenia

Priečinok riešenia je organizovaný podľa programovacieho jazyka:

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

### 🚀 Čo obsahuje každé riešenie

Každé jazykovo špecifické riešenie poskytuje:

- **Kompletnú implementáciu klienta** so všetkými funkciami z tutoriálu.
- **Fungujúcu štruktúru projektu** so správnymi závislosťami a konfiguráciou.
- **Skripty na zostavenie a spustenie** pre jednoduché nastavenie a vykonanie.
- **Podrobný README** s jazykovo špecifickými pokynmi.
- **Príklady spracovania chýb** a výsledkov.

### 📖 Použitie riešení

1. **Prejdite do priečinka preferovaného jazyka**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Postupujte podľa pokynov README** v každom priečinku pre:
   - Inštaláciu závislostí.
   - Zostavenie projektu.
   - Spustenie klienta.

3. **Príklad výstupu**, ktorý by ste mali vidieť:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pre kompletnú dokumentáciu a podrobné pokyny si pozrite: **[📖 Dokumentácia riešenia](./solution/README.md)**

## 🎯 Kompletné príklady

Poskytli sme kompletné, funkčné implementácie klientov pre všetky programovacie jazyky pokryté v tomto tutoriáli. Tieto príklady demonštrujú plnú funkcionalitu popísanú vyššie a môžu byť použité ako referenčné implementácie alebo východiskové body pre vaše vlastné projekty.

### Dostupné kompletné príklady

| Jazyk | Súbor | Popis |
|-------|-------|-------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletný Java klient používajúci SSE prenos s komplexným spracovaním chýb |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletný C# klient používajúci stdio prenos s automatickým spustením servera |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletný TypeScript klient s plnou podporou MCP protokolu |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletný Python klient používajúci async/await vzory |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompletný Rust klient používajúci Tokio pre asynchrónne operácie |
Každý kompletný príklad zahŕňa:

- ✅ **Nadviazanie spojenia** a spracovanie chýb
- ✅ **Objavovanie servera** (nástroje, zdroje, výzvy, kde je to vhodné)
- ✅ **Operácie kalkulačky** (sčítanie, odčítanie, násobenie, delenie, pomoc)
- ✅ **Spracovanie výsledkov** a formátovaný výstup
- ✅ **Komplexné spracovanie chýb**
- ✅ **Čistý, zdokumentovaný kód** s komentármi krok za krokom

### Začíname s kompletnými príkladmi

1. **Vyberte si preferovaný jazyk** z tabuľky vyššie
2. **Prezrite si súbor s kompletným príkladom**, aby ste pochopili celú implementáciu
3. **Spustite príklad** podľa pokynov v [`complete_examples.md`](./complete_examples.md)
4. **Upravte a rozšírte** príklad pre váš konkrétny prípad použitia

Podrobné informácie o spustení a prispôsobení týchto príkladov nájdete tu: **[📖 Dokumentácia ku kompletným príkladom](./complete_examples.md)**

### 💡 Riešenie vs. Kompletné príklady

| **Priečinok riešení** | **Kompletné príklady** |
|-----------------------|-----------------------|
| Kompletná štruktúra projektu s build súbormi | Implementácie v jednom súbore |
| Pripravené na spustenie so závislosťami | Zamerané na vzorové kódy |
| Nastavenie podobné produkcii | Vzdelávací referenčný materiál |
| Nástroje špecifické pre jazyk | Porovnanie medzi jazykmi |

Oba prístupy sú hodnotné - použite **priečinok riešení** pre kompletné projekty a **kompletné príklady** na učenie a referenciu.

## Kľúčové poznatky

Kľúčové poznatky z tejto kapitoly o klientoch sú nasledovné:

- Môžu byť použité na objavovanie aj využívanie funkcií na serveri.
- Môžu spustiť server počas svojho spúšťania (ako v tejto kapitole), ale klienti sa môžu pripojiť aj k už bežiacim serverom.
- Sú skvelým spôsobom na testovanie schopností servera popri alternatívach, ako je napríklad Inspector, ktorý bol popísaný v predchádzajúcej kapitole.

## Ďalšie zdroje

- [Budovanie klientov v MCP](https://modelcontextprotocol.io/quickstart/client)

## Príklady

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Čo ďalej

- Ďalej: [Vytváranie klienta s LLM](../03-llm-client/README.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
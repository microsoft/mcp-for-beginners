# Vytvorenie klienta

Klienti sú vlastné aplikácie alebo skripty, ktoré priamo komunikujú so serverom MCP a požadujú zdroje, nástroje a výzvy. Na rozdiel od použitia nástroja inšpektora, ktorý poskytuje grafické rozhranie na interakciu so serverom, písanie vlastného klienta umožňuje programatickú a automatizovanú interakciu. Vývojárom to umožňuje integrovať možnosti MCP do svojich pracovných tokov, automatizovať úlohy a vytvárať vlastné riešenia prispôsobené konkrétnym potrebám.

## Prehľad

Táto lekcia predstavuje koncept klientov v rámci ekosystému Model Context Protocol (MCP). Naučíte sa, ako napísať vlastného klienta a pripojiť ho k serveru MCP.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Pochopiť, čo klient dokáže.
- Napísať vlastného klienta.
- Pripojiť a otestovať klienta so serverom MCP, aby ste sa uistili, že server funguje ako očakávané.

## Čo zahŕňa písanie klienta?

Na napísanie klienta budete musieť urobiť nasledovné:

- **Importovať správne knižnice**. Budete používať tú istú knižnicu ako predtým, len iné konštrukty.
- **Vytvoriť inštanciu klienta**. To znamená vytvoriť inštanciu klienta a pripojiť ju k vybranému spôsobu prenosu.
- **Rozhodnúť, aké zdroje budete zobrazovať**. Váš server MCP obsahuje zdroje, nástroje a výzvy, musíte sa rozhodnúť, ktoré si zobrazíte.
- **Integrovať klienta do hostiteľskej aplikácie**. Keď budete poznať možnosti servera, je potrebné ho integrovať do hostiteľskej aplikácie tak, aby sa pri zadaní výzvy alebo iného príkazu používateľom zavolala príslušná funkcia servera.

Teraz, keď chápeme na vysokej úrovni, čo máme urobiť, pozrime sa na príklad.

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

// Zoznam výziev
const prompts = await client.listPrompts();

// Získať výzvu
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Zoznam zdrojov
const resources = await client.listResources();

// Prečítať zdroj
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Zavolať nástroj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

V predchádzajúcom kóde sme:

- Importovali knižnice
- Vytvorili inštanciu klienta a pripojili ju pomocou stdio ako transportu.
- Vylistovali výzvy, zdroje a nástroje a všetky ich zavolali.

Máte tu teda klienta, ktorý dokáže komunikovať so serverom MCP.

V ďalšej cvičnej časti si podrobne vysvetlíme každý kódový útržok.

## Cvičenie: Písanie klienta

Ako sme už spomínali, venujme čas vysvetľovaniu kódu, a pokojne aj kódujte spolu s nami, ak chcete.

### -1- Importovanie knižníc

Naimportujme knižnice, ktoré potrebujeme, budeme potrebovať referencie na klienta a na náš zvolený prenosový protokol, stdio. stdio je protokol určený na spúšťanie na vašom lokálnom počítači. SSE je ďalší prenášací protokol, ktorý ukážeme v budúcich kapitolách, ale pre teraz pokračujme so stdio.

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

Pre Javu vytvoríte klienta, ktorý sa pripojí k serveru MCP z predchádzajúceho cvičenia. Používajúc tú istú štruktúru projektu Java Spring Boot z [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), vytvorte novú Java triedu nazvanú `SDKClient` v priečinku `src/main/java/com/microsoft/mcp/sample/client/` a pridajte nasledujúce importy:

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

Budete musieť pridať nasledujúce závislosti do svojho súboru `Cargo.toml`.

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

Odtiaľ môžete importovať potrebné knižnice vo svojom klientskej kóde.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Poďme na vytvorenie inštancie.

### -2- Vytvorenie inštancie klienta a transportu

Budeme musieť vytvoriť inštanciu transportu a našej klienta:

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

- Vytvorili sme inštanciu transportu stdio. Všimnite si, že špecifikuje príkaz a argumenty, ako nájsť a spustiť server, čo budeme potrebovať pri tvorbe klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Vytvorili sme inštanciu klienta, ktorému sme dali meno a verziu.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Pripojili sme klienta k vybranému transportu.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvorte parametre servera pre pripojenie stdio
server_params = StdioServerParameters(
    command="mcp",  # Spustiteľný súbor
    args=["run", "server.py"],  # Voliteľné argumenty príkazového riadku
    env=None,  # Voliteľné premenné prostredia
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializujte pripojenie
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

V predchádzajúcom kóde sme:

- Importovali požadované knižnice
- Vytvorili sme objekt parametrov servera, ktorý použijeme na spustenie servera, aby sme sa k nemu mohli pripojiť s klientom.
- Definovali sme metódu `run`, ktorá následne zavolá `stdio_client`, ktorý spustí klientsku reláciu.
- Vytvorili sme vstupný bod, kde metódu `run` odovzdáme `asyncio.run`.

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

V predchádzajúcom kóde sme:

- Importovali požadované knižnice.
- Vytvorili sme transport stdio a klienta `mcpClient`. Tento klient budeme používať na zoznam i vyvolávanie funkcií servera MCP.

Poznámka: v "Arguments" môžete ukázať buď na súbor *.csproj,* alebo na spustiteľný súbor.

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
        
        // Vaša klientská logika ide sem
    }
}
```

V predchádzajúcom kóde sme:

- Vytvorili sme hlavnú metódu, ktorá nastaví SSE transport ukazujúci na `http://localhost:8080`, kde bude bežať náš MCP server.
- Vytvorili sme klientsku triedu, ktorá ako parameter konštruktora berie transport.
- V metóde `run` vytvoríme synchronný MCP klient pomocou transportu a inicializujeme pripojenie.
- Použili sme SSE (Server-Sent Events) transport vhodný pre HTTP komunikáciu s Java Spring Boot MCP servermi.

#### Rust

Tento Rust klient predpokladá, že server je súrodenecký projekt s názvom "calculator-server" v rovnakom adresári. Kód nižšie spustí server a pripojí sa k nemu.

```rust
async fn main() -> Result<(), RmcpError> {
    // Predpokladajme, že server je súrodenecký projekt s názvom "calculator-server" v rovnakom adresári
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

    // TODO: Inicializovať

    // TODO: Zoznam nástrojov

    // TODO: Zavolať add tool s argumentmi = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Zoznam funkcií servera

Teraz máme klienta, ktorý sa dokáže pripojiť, ak sa program spustí. Avšak zatiaľ nevypisuje svoje funkcie, poďme to urobiť teraz:

#### TypeScript

```typescript
// Zoznam výziev
const prompts = await client.listPrompts();

// Zoznam zdrojov
const resources = await client.listResources();

// Zoznam nástrojov
const tools = await client.listTools();
```

#### Python

```python
# Zoznam dostupných zdrojov
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Zoznam dostupných nástrojov
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Tu vylistujeme dostupné zdroje pomocou `list_resources()` a nástroje pomocou `list_tools` a vypíšeme ich.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Vyššie je príklad, ako môžeme vylistovať nástroje na serveri. Pre každý nástroj následne vypíšeme jeho názov.

#### Java

```java
// Zoznam a ukážka nástrojov
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Môžete tiež pingnúť server na overenie pripojenia
client.ping();
```

V predchádzajúcom kóde sme:

- Zavolali sme `listTools()` na získanie všetkých dostupných nástrojov zo servera MCP.
- Použili sme `ping()` na overenie, že pripojenie k serveru funguje.
- `ListToolsResult` obsahuje informácie o všetkých nástrojoch vrátane ich názvov, popisov a vstupných schém.

Skvelé, teraz sme získali všetky funkcie. Otázka je, kedy ich použijeme? Tento klient je jednoduchý v tom, že musíme explicitne zavolať dané funkcie, keď ich chceme. V ďalšej kapitole vytvoríme pokročilejší klient, ktorý bude mať prístup k vlastnému veľkému jazykovému modelu (LLM). Pre teraz však pozrime sa, ako môžeme vyvolávať funkcie na serveri:

#### Rust

V hlavnej funkcii, po inicializácii klienta, môžeme inicializovať server a vypísať niektoré jeho funkcie.

```rust
// Inicializovať
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Zoznam nástrojov
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Vyvolanie funkcií

Na vyvolanie funkcií musíme zabezpečiť správne zadanie argumentov a v niektorých prípadoch aj názvu toho, čo chceme vyvolať.

#### TypeScript

```typescript

// Načítať zdroj
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Zavolať nástroj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// zavolať prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

V predchádzajúcom kóde sme:

- Prečítali zdroj, zavolali sme zdroj pomocou `readResource()` so špecifikovaním `uri`. Tu je, ako to pravdepodobne vyzerá na serverovej strane:

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

- Zavolali nástroj, voláme ho so špecifikáciou jeho `name` a `arguments`, takto:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Získali výzvu, na získanie výzvy zavoláte `getPrompt()` s `name` a `arguments`. Kód servera vyzerá takto:

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

    a výsledný klientsky kód teda vyzerá takto, aby zodpovedal tomu, čo je deklarované na serveri:

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
# Načítať zdroj
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Zavolať nástroj
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

V predchádzajúcom kóde sme:

- Zavolali zdroj nazvaný `greeting` pomocou `read_resource`.
- Vyvolali nástroj `add` použitím `call_tool`.

#### .NET

1. Pridajme kód na volanie nástroja:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Na vytlačenie výsledku je tu kód na jeho spracovanie:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Zavolať rôzne kalkulačné nástroje
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
- Každé volanie nástroja špecifikuje názov nástroja a mapu argumentov požadovaných týmto nástrojom.
- Nástroje servera očakávajú špecifické názvy parametrov (napríklad „a“, „b“ pre matematické operácie).
- Výsledky sú vrátené ako objekty `CallToolResult` obsahujúce odpoveď zo servera.

#### Rust

```rust
// Zavolajte nástroj add s argumentmi = {"a": 3, "b": 2}
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

Na spustenie klienta zadajte v termináli nasledujúci príkaz:

#### TypeScript

Pridajte nasledujúcu položku do sekcie „scripts“ v *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Zavolajte klienta pomocou tohto príkazu:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najskôr sa uistite, že váš MCP server beží na `http://localhost:8080`. Potom spustite klienta:

```bash
# Skompilujte svoj projekt
./mvnw clean compile

# Spustite klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatívne môžete spustiť kompletný klientsky projekt poskytnutý v riešení v priečinku `03-GettingStarted\02-client\solution\java`:

```bash
# Prejdite do adresára riešenia
cd 03-GettingStarted/02-client/solution/java

# Vytvorte a spustite JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Zadanie

V tomto zadaní použijete naučené vedomosti o vytvorení klienta a vytvoríte vlastného klienta.

Tu je server, ktorý môžete použiť a ku ktorému sa musíte pripájať pomocou vášho klientskeho kódu; skúste k serveru pridať viac funkcií, aby bol zaujímavejší.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Vytvorte MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Pridajte nástroj na sčítanie
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Pridajte dynamický pozdravový zdroj
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

// Začnite prijímať správy na stdin a odosielať správy na stdout

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

# Vytvorte MCP server
mcp = FastMCP("Demo")


# Pridajte nástroj na sčítanie
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Pridajte dynamický zdroj pozdravu
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

Pozrite si tento projekt, kde nájdete, ako [pridať výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tiež si pozrite tento odkaz s ukážkami, ako vyvolať [výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [predchádzajúcej časti](../../../../03-GettingStarted/01-first-server) ste sa naučili, ako vytvoriť jednoduchý MCP server pomocou Rustu. Môžete na tom ďalej stavať alebo si pozrieť tento odkaz s ďalšími príkladmi MCP serverov v Rust jazyku: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Riešenie

**Riešenie** obsahuje kompletné implementácie klientov pripravených na spustenie, ktoré demonštrujú všetky koncepty popísané v tomto návode. Každé riešenie obsahuje kód klienta a servera organizovaný v samostatných, samostatne fungujúcich projektoch.

### 📁 Štruktúra riešenia

Priečinok riešenia je organizovaný podľa programovacích jazykov:

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

### 🚀 Čo každé riešenie obsahuje

Každé riešenie pre konkrétny jazyk poskytuje:

- **Kompletnú implementáciu klienta** so všetkými funkciami z tutoriálu
- **Funkčnú štruktúru projektu** so správnymi závislosťami a konfiguráciou
- **Skripty na build a spustenie** pre ľahké nastavenie a používanie
- **Podrobný README** s inštrukciami pre daný jazyk
- **Príklady spracovania chýb** a výsledkov

### 📖 Použitie riešení

1. **Prejdite do priečinka so zvoleným jazykom**:

   ```bash
   cd solution/typescript/    # Pre TypeScript
   cd solution/java/          # Pre Java
   cd solution/python/        # Pre Python
   cd solution/dotnet/        # Pre .NET
   ```

2. **Nasledujte pokyny v README** v každom priečinku na:
   - Inštaláciu závislostí
   - Vytvorenie projektu
   - Spustenie klienta

3. **Príklad výstupu**, ktorý by ste mali vidieť:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Kompletnú dokumentáciu a krok za krokom inštrukcie nájdete v: **[📖 Dokumentácia riešenia](./solution/README.md)**

## 🎯 Kompletné príklady

Poskytli sme kompletné, funkčné implementácie klientov pre všetky programovacie jazyky popísané v tomto návode. Tieto príklady demonštrujú plnú funkcionalitu opísanú vyššie a môžu byť použité ako referenčné implementácie alebo východiská pre vaše vlastné projekty.

### K dispozícii kompletné príklady

| Jazyk | Súbor | Popis |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletný Java klient využívajúci SSE transport s dôkladným spracovaním chýb |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletný C# klient používajúci stdio transport so štartom servera automaticky |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletný TypeScript klient s plnou podporou MCP protokolu |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletný Python klient používajúci async/await vzory |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompletný Rust klient využívajúci Tokio pre asynchrónne operácie |

Každý kompletný príklad obsahuje:

- ✅ **Nadviazanie pripojenia** a spracovanie chýb
- ✅ **Objavenie servera** (nástroje, zdroje, výzvy, kde relevantné)
- ✅ **Kalkulačné operácie** (sčítanie, odčítanie, násobenie, delenie, pomoc)
- ✅ **Spracovanie výsledkov** a formátovaný výstup
- ✅ **Dôkladné spracovanie chýb**

- ✅ **Čistý, dokumentovaný kód** s krok za krokom komentármi

### Začíname s kompletnými príkladmi

1. **Vyberte si preferovaný jazyk** z tabuľky vyššie
2. **Prejdite si kompletný príkladový súbor** aby ste pochopili celú implementáciu
3. **Spustite príklad** podľa inštrukcií v [`complete_examples.md`](./complete_examples.md)
4. **Upravujte a rozširujte** príklad pre vaše konkrétne použitie

Pre podrobnú dokumentáciu o spúšťaní a prispôsobovaní týchto príkladov, pozrite si: **[📖 Dokumentácia kompletných príkladov](./complete_examples.md)**

### 💡 Riešenie vs. kompletné príklady

| **Súbor riešenia** | **Kompletné príklady** |
|--------------------|--------------------- |
| Plná štruktúra projektu so súbormi na zostavenie | Implementácie v jednom súbore |
| Pripravené na spustenie s závislosťami | Zamerané ukážky kódu |
| Prostredie podobné produkčnému | Vzdelávacia referencia |
| Nástroje špecifické pre jazyk | Porovnanie medzi jazykmi |

Obe prístupy sú hodnotné - používajte **súbor riešenia** pre kompletné projekty a **kompletné príklady** na učenie a referenciu.

## Hlavné body

Hlavné body kapitoly o klientoch sú:

- Môžu sa použiť na objavovanie aj vyvolávanie funkcií na serveri.
- Môžu spustiť server počas spúšťania samotného seba (ako v tejto kapitole), ale klienti sa môžu tiež pripojiť k už bežiacim serverom.
- Sú skvelým spôsobom, ako otestovať schopnosti servera vedľa alternatív ako Inspector, ako bolo popísané v predchádzajúcej kapitole.

## Ďalšie zdroje

- [Budovanie klientov v MCP](https://modelcontextprotocol.io/quickstart/client)

## Príklady

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Čo ďalej

- Ďalej: [Vytvorenie klienta s LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
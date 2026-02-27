# Vytváranie klienta

Klienti sú vlastné aplikácie alebo skripty, ktoré priamo komunikujú so serverom MCP, aby požiadali o zdroje, nástroje a podnety. Na rozdiel od použitia nástroja inspektora, ktorý poskytuje grafické rozhranie na interakciu so serverom, vlastný klient umožňuje programovú a automatizovanú interakciu. To umožňuje vývojárom integrovať schopnosti MCP do svojich vlastných pracovných postupov, automatizovať úlohy a vytvárať vlastné riešenia prispôsobené špecifickým potrebám.

## Prehľad

Táto lekcia predstavuje koncept klientov v ekosystéme Model Context Protocol (MCP). Naučíte sa, ako napísať vlastného klienta a pripojiť ho k serveru MCP.

## Ciele učenia sa

Na konci tejto lekcie budete schopní:

- Pochopiť, čo klient dokáže.
- Napísať vlastného klienta.
- Pripojiť sa a otestovať klienta so serverom MCP na overenie jeho správnej funkčnosti.

## Čo je potrebné na napísanie klienta?

Na napísanie klienta budete musieť urobiť nasledovné:

- **Importovať správne knižnice**. Budete používať rovnakú knižnicu ako predtým, len iné konštrukty.
- **Inštancovať klienta**. To bude zahŕňať vytvorenie inštancie klienta a jeho pripojenie k zvolenému spôsobu prenosu.
- **Rozhodnúť, ktoré zdroje zoznamovať**. Váš server MCP prichádza so zdrojmi, nástrojmi a podnetmi, potrebujete sa rozhodnúť, ktoré z nich zoznamujete.
- **Integrovať klienta do hostiteľskej aplikácie**. Keď poznáte schopnosti servera, musíte ho integrovať do svojej hostiteľskej aplikácie tak, aby pri zadaní podnetu alebo iného príkazu používateľom bola vyvolaná príslušná funkcia servera.

Teraz, keď si vo všeobecnosti rozumieme, čo budeme robiť, pozrime sa na príklad.

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
- Vytvorili inštanciu klienta a pripojili ju pomocou stdio ako spôsob prenosu.
- Zoznamovali podnety, zdroje a nástroje a všetky ich vyvolali.

Toto je klient, ktorý dokáže komunikovať so serverom MCP.

V ďalšej cvičnej časti si dáme čas a rozoberieme každý kódový útržok a vysvetlíme, čo sa deje.

## Cvičenie: Písanie klienta

Ako bolo povedané, poďme si detailnejšie vysvetliť kód a kľudne ho aj sami programujte.

### -1- Import knižníc

Importujme knižnice, ktoré potrebujeme – budeme potrebovať odkazy na klienta a na náš vybraný prenosový protokol stdio. stdio je protokol pre veci, ktoré majú bežať na vašom lokálnom počítači. SSE je ďalší prenosový protokol, ktorý ukážeme v budúcich kapitolách, ale toto je vaša ďalšia možnosť. Teraz však pokračujme so stdio.

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

Pre Java vytvoríte klienta, ktorý sa pripojí k serveru MCP z predchádzajúceho cvičenia. Použitím tej istej štruktúry projektu Java Spring Boot z [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) vytvorte novú triedu s názvom `SDKClient` v priečinku `src/main/java/com/microsoft/mcp/sample/client/` a pridajte nasledujúce importy:

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

Budete musieť do svojho súboru `Cargo.toml` pridať nasledujúce závislosti.

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

Odtiaľ môžete importovať potrebné knižnice vo svojom klientskóm kóde.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Poďme pokračovať inštanciáciou.

### -2- Inštancovanie klienta a prenosu

Budeme potrebovať vytvoriť inštanciu prenosu a klienta:

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

- Vytvorili inštanciu prenosu stdio. Všimnite si, ako špecifikuje príkaz a argumenty, ako nájsť a spustiť server, pretože to budeme musieť urobiť počas vytvárania klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Inštancovali klienta, pričom sme mu dali meno a verziu.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Pripojili sme klienta k zvolenému prenosu.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvorte parametre servera pre stdio pripojenie
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

- Importovali potrebné knižnice
- Vytvorili objekt parametrov servera, ktorý použijeme na spustenie servera, aby sme sa mohli pripojiť s naším klientom.
- Definovali metódu `run`, ktorá následne volá `stdio_client`, ktorá spúšťa klientsku reláciu.
- Vytvorili vstupný bod, kde poskytneme metódu `run` funkcii `asyncio.run`.

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

- Importovali potrebné knižnice.
- Vytvorili prenos stdio a vytvorili klienta `mcpClient`. Ten použijeme na zoznamovanie a vyvolávanie funkcií servera MCP.

Poznámka: v "Arguments" môžete ukázať buď na *.csproj* alebo na spustiteľný súbor.

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
        
        // Vaša logika klienta ide sem
    }
}
```

V predchádzajúcom kóde sme:

- Vytvorili hlavnú metódu, ktorá nastaví prenos SSE nasmerovaný na `http://localhost:8080`, kde bude bežať náš server MCP.
- Vytvorili klientskú triedu, ktorá berie prenos ako parameter konštruktora.
- V metóde `run` sme vytvorili synchronný MCP klient pomocou prenosu a inicializovali pripojenie.
- Použili prenos SSE (Server-Sent Events), ktorý je vhodný pre HTTP komunikáciu s Java Spring Boot MCP servermi.

#### Rust

Tento Rust klient predpokladá, že server je súbežný projekt s názvom "calculator-server" v rovnakom adresári. Nasledujúci kód spustí server a pripojí sa k nemu.

```rust
async fn main() -> Result<(), RmcpError> {
    // Predpokladajte, že server je súrodenecký projekt s názvom "calculator-server" v rovnakom adresári
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

    // TODO: Zavolajte nástroj add s argumentmi = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Zoznam funkcií servera

Teraz máme klienta, ktorý sa môže pripojiť, ak sa program spustí. Avšak ešte nezobrazuje jeho funkcie, spravme to teraz:

#### TypeScript

```typescript
// Zoznam výziev
const prompts = await client.listPrompts();

// Zoznam zdrojov
const resources = await client.listResources();

// zoznam nástrojov
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

Tu zoznamujeme dostupné zdroje `list_resources()` a nástroje `list_tools` a vypisujeme ich.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Vyššie je príklad, ako môžeme zoznamovať nástroje na serveri. Pre každý nástroj následne vypíšeme jeho názov.

#### Java

```java
// Zoznam a ukážka nástrojov
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Môžete tiež pingnúť server na overenie pripojenia
client.ping();
```

V predchádzajúcom kóde sme:

- Zavolali `listTools()` na získanie všetkých dostupných nástrojov zo servera MCP.
- Použili sme `ping()` na overenie, že pripojenie k serveru funguje.
- `ListToolsResult` obsahuje informácie o všetkých nástrojoch vrátane ich názvov, popisov a vstupných schém.

Výborne, teraz máme zachytené všetky funkcie. Otázka znie, kedy ich použiť? Tento klient je dosť jednoduchý, v tom zmysle, že musíme explicitne volať funkcie, keď ich chceme. V ďalšej kapitole vytvoríme pokročilejšieho klienta, ktorý bude mať prístup k vlastnému veľkému jazykovému modelu (LLM). Teraz však pozrime, ako vyvolať funkcie na serveri:

#### Rust

V hlavnej funkcii, po inicializácii klienta, môžeme inicializovať server a zoznamovať niektoré jeho funkcie.

```rust
// Inicializovať
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Zoznam nástrojov
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Vyvolanie funkcií

Na vyvolanie funkcií musíme zabezpečiť, že špecifikujeme správne argumenty a v niektorých prípadoch aj názov toho, čo sa snažíme vyvolať.

#### TypeScript

```typescript

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

// zavolať prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

V predchádzajúcom kóde sme:

- Čítali zdroj, zavolali sme zdroj pomocou `readResource()` so špecifikovaním `uri`. Takto to vyzerá na strane servera:

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

- Zavolali nástroj, zavolali sme ho so špecifikovaním jeho `name` a `arguments` takto:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Získali podnet, na získanie podnetu zavoláte `getPrompt()` s `name` a `arguments`. Kód servera vyzerá takto:

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

    Váš výsledný klientskód preto vyzerá takto, aby zodpovedal deklarovanému na serveri:

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

- Zavolali zdroj s názvom `greeting` použitím `read_resource`.
- Vyvolali nástroj `add` použitím `call_tool`.

#### .NET

1. Pridajme kód na vyvolanie nástroja:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. A tu je kód na vypísanie výsledku:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Zavolajte rôzne nástroje kalkulačky
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

- Zavolali viacero kalkulačných nástrojov použitím metódy `callTool()` s objektmi `CallToolRequest`.
- Každé volanie nástroja špecifikuje názov nástroja a `Map` argumentov potrebných týmto nástrojom.
- Nástroje servera očakávajú špecifické názvy parametrov (napríklad "a", "b" pre matematické operácie).
- Výsledky sú vrátené ako objekty `CallToolResult`, ktoré obsahujú odpoveď zo servera.

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

Na spustenie klienta zadajte nasledujúci príkaz do terminálu:

#### TypeScript

Pridajte nasledujúci záznam do sekcie "scripts" vo *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Klienta spustite nasledujúcim príkazom:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Najskôr sa uistite, že váš server MCP beží na `http://localhost:8080`. Potom spustite klienta:

```bash
# Postavte váš projekt
./mvnw clean compile

# Spustite klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatívne môžete spustiť kompletný klientsky projekt, ktorý je k dispozícii v riešení v priečinku `03-GettingStarted\02-client\solution\java`:

```bash
# Prejdite do adresára riešenia
cd 03-GettingStarted/02-client/solution/java

# Skompilujte a spustite JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Zadanie

V tomto zadaní použijete to, čo ste sa naučili o vytváraní klienta, ale vytvoríte si vlastného klienta.

Tu je server, ktorý môžete použiť, na ktorý musíte volať cez svoj klientsky kód, uvidíte, či dokážete pridať viac funkcií na server, aby bol zaujímavejší.

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

// Pridajte dynamický zdroj pozdravov
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

Pozrite si tento projekt, kde uvidíte, ako môžete [pridať podnety a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tiež si pozrite tento odkaz, ako vyvolávať [podnety a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [predchádzajúcej časti](../../../../03-GettingStarted/01-first-server) ste sa naučili, ako vytvoriť jednoduchý server MCP pomocou Rustu. Môžete na tom pokračovať alebo si pozrieť tento odkaz pre viac príkladov serverov MCP založených na Rustu: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Riešenie

**Priečinok riešenia** obsahuje kompletné, pripravené spustiť implementácie klientov, ktoré demonštrujú všetky koncepcie pokryté v tomto tutoriáli. Každé riešenie obsahuje kód klienta aj servera usporiadaný v samostatných, nezávislých projektoch.

### 📁 Štruktúra riešenia

Adresár riešenia je usporiadaný podľa programovacieho jazyka:

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

Každé riešenie pre daný jazyk poskytuje:

- **Kompletnú implementáciu klienta** so všetkými funkciami z tutoriálu
- **Funkčnú štruktúru projektu** so správnymi závislosťami a konfiguráciou
- **Skripty na kompiláciu a spustenie** pre jednoduché nastavenie a prevádzku
- **Podrobný README** s pokynmi špecifickými pre daný jazyk
- **Príklady spracovania chýb a výsledkov**

### 📖 Používanie riešení

1. **Prejdite do priečinka vybraného jazyka**:

   ```bash
   cd solution/typescript/    # Pre TypeScript
   cd solution/java/          # Pre Java
   cd solution/python/        # Pre Python
   cd solution/dotnet/        # Pre .NET
   ```

2. **Postupujte podľa inštrukcií v README** v každom priečinku pre:
   - Inštaláciu závislostí
   - Kompiláciu projektu
   - Spustenie klienta

3. **Ukážkový výstup**, ktorý by ste mali vidieť:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pre kompletnú dokumentáciu a postupné inštrukcie si pozrite: **[📖 Dokumentácia riešenia](./solution/README.md)**

## 🎯 Kompletné príklady

Poskytli sme kompletné, funkčné implementácie klientov pre všetky programovacie jazyky pokryté v tomto tutoriáli. Tieto príklady demonštrujú plnú funkčnosť opísanú vyššie a môžu slúžiť ako referenčné implementácie alebo východiská pre vaše vlastné projekty.

### Dostupné kompletné príklady

| Jazyk    | Súbor                        | Popis                                                  |
|----------|------------------------------|--------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletný Java klient používajúci SSE prenos s komplexným spracovaním chýb |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletný C# klient používajúci stdio prenos so štartom servera automaticky |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletný TypeScript klient s plnou podporou protokolu MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletný Python klient používajúci asynchrónne vzory async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompletný Rust klient používajúci Tokio pre asynchrónne operácie |

Každý kompletný príklad obsahuje:
- ✅ **Nadviazanie spojenia** a spracovanie chýb
- ✅ **Objavovanie servera** (nástroje, zdroje, výzvy tam, kde je to vhodné)
- ✅ **Operácie kalkulačky** (sčítanie, odčítanie, násobenie, delenie, pomoc)
- ✅ **Spracovanie výsledkov** a formátovaný výstup
- ✅ **Komplexné spracovanie chýb**
- ✅ **Čistý, dokumentovaný kód** s komentármi krok za krokom

### Začíname s kompletnými príkladmi

1. **Vyberte preferovaný jazyk** z tabuľky vyššie
2. **Prejdite si kompletný príkladový súbor**, aby ste pochopili celú implementáciu
3. **Spustite príklad** podľa inštrukcií v [`complete_examples.md`](./complete_examples.md)
4. **Upravujte a rozširujte** príklad pre váš konkrétny prípad použitia

Pre podrobnú dokumentáciu o spúšťaní a prispôsobovaní týchto príkladov si pozrite: **[📖 Dokumentácia kompletných príkladov](./complete_examples.md)**

### 💡 Riešenie vs. Kompletné príklady

| **Zložka riešenia** | **Kompletné príklady** |
|---------------------|-----------------------|
| Kompletná štruktúra projektu s build súbormi | Implementácie v jednom súbore |
| Pripravené na spustenie s knižnicami | Zamerané ukážky kódu |
| Nastavenie produkčného typu | Vzdelávacia referencia |
| Nástroje špecifické pre jazyk | Porovnanie medzi jazykmi |

Oba prístupy sú cenné – použite **zložku riešenia** pre kompletné projekty a **kompletné príklady** na učenie a referenciu.

## Hlavné body

Hlavné závery tejto kapitoly o klientoch sú:

- Môžu sa použiť na objavovanie aj volanie funkcií na serveri.
- Môžu spustiť server a zároveň sa samy spúšťajú (ako v tejto kapitole), ale klienti sa môžu pripojiť aj k už bežiacim serverom.
- Sú skvelým spôsobom, ako otestovať schopnosti servera vedľa alternatív ako Inspector, ako bolo opísané v predchádzajúcej kapitole.

## Ďalšie zdroje

- [Tvorba klientov v MCP](https://modelcontextprotocol.io/quickstart/client)

## Ukážky

- [Java kalkulačka](../samples/java/calculator/README.md)
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulačka](../samples/javascript/README.md)
- [TypeScript kalkulačka](../samples/typescript/README.md)
- [Python kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust kalkulačka](../../../../03-GettingStarted/samples/rust)

## Čo bude ďalej

- Ďalej: [Vytvorenie klienta s LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pri kritických informáciách sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
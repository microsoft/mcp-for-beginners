# Vytvoření klienta

Klienti jsou vlastní aplikace nebo skripty, které komunikují přímo s MCP serverem za účelem požádání o zdroje, nástroje a promptů. Na rozdíl od používání nástroje inspektoru, který poskytuje grafické rozhraní pro interakci se serverem, vlastní klient umožňuje programatickou a automatizovanou interakci. To umožňuje vývojářům integrovat schopnosti MCP do svých pracovních postupů, automatizovat úkoly a vytvářet vlastní řešení přizpůsobená specifickým potřebám.

## Přehled

Tato lekce představuje koncept klientů v rámci ekosystému Model Context Protocol (MCP). Naučíte se, jak napsat vlastního klienta a připojit ho k MCP serveru.

## Cíle učení

Na konci této lekce budete schopni:

- Porozumět, co klient dokáže.
- Napsat vlastního klienta.
- Připojit a otestovat klienta s MCP serverem, aby bylo ověřeno, že server funguje podle očekávání.

## Co patří do psaní klienta?

Chcete-li napsat klienta, budete muset učinit následující kroky:

- **Importovat správné knihovny**. Budete používat stejnou knihovnu jako předtím, jen jiné konstrukty.
- **Vytvořit instanci klienta**. To bude zahrnovat vytvoření instance klienta a připojení k zvolenému způsobu transportu.
- **Rozhodnout, které zdroje chcete vypisovat**. Váš MCP server obsahuje zdroje, nástroje a promptů, musíte se rozhodnout, které z nich budete vypisovat.
- **Integrovat klienta do hostitelské aplikace**. Jakmile znáte schopnosti serveru, je třeba klienta integrovat do hostitelské aplikace tak, aby při zadání promptu nebo jiného příkazu uživatelem byla vyvolána odpovídající funkce serveru.

Nyní, když rozumíme na vysoké úrovni, co budeme dělat, podíváme se na následující příklad.

### Příklad klienta

Podívejme se na tento příklad klienta:

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

// Vypsat výzvy
const prompts = await client.listPrompts();

// Získat výzvu
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Vypsat zdroje
const resources = await client.listResources();

// Přečíst zdroj
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Zavolat nástroj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

V předchozím kódu jsme:

- Importovali knihovny
- Vytvořili instanci klienta a připojili ji pomocí stdio jako transportu.
- Vypsali promptů, zdroje a nástroje a všechny je vyvolali.

Máte tedy klienta, který může komunikovat s MCP serverem.

V další cvičné části si vezmeme čas a rozložíme jednotlivé bloky kódu a vysvětlíme, co se děje.

## Cvičení: Psaní klienta

Jak bylo řečeno výše, vezmeme si čas na vysvětlení kódu a rozhodně klidně kódujte zároveň.

### -1- Import knihoven

Importujme knihovny, které potřebujeme, budeme potřebovat reference na klienta a zvolený protokol transportu, stdio. stdio je protokol pro věci, které mají běžet na vašem lokálním počítači. SSE je další transportní protokol, který ukážeme v budoucích kapitolách, ale to je vaše druhá možnost. Prozatím však pokračujeme se stdio.

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

Pro Javu vytvoříte klienta, který se připojuje k MCP serveru z předchozího cvičení. Použijte stejnou strukturu projektu Java Spring Boot z [Zahájení práce s MCP Serverem](../../../../03-GettingStarted/01-first-server/solution/java), vytvořte novou třídu Java nazvanou `SDKClient` ve složce `src/main/java/com/microsoft/mcp/sample/client/` a přidejte následující importy:

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

Musíte přidat následující závislosti do vašeho souboru `Cargo.toml`.

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

Odtud můžete importovat potřebné knihovny ve svém kódu klienta.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Přejděme k vytvoření instance.

### -2- Vytvoření instance klienta a transportu

Budeme muset vytvořit instanci transportu i klienta:

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

V předchozím kódu jsme:

- Vytvořili instanci stdio transportu. Všimněte si, jak specifikuje příkaz a argumenty, jak server najít a spustit, protože to budeme potřebovat pro vytvoření klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Vytvořili instanci klienta s názvem a verzí.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Připojili klienta k vybranému transportu.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvořit parametry serveru pro stdio připojení
server_params = StdioServerParameters(
    command="mcp",  # Spustitelný soubor
    args=["run", "server.py"],  # Nepovinné argumenty příkazové řádky
    env=None,  # Nepovinné proměnné prostředí
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializovat připojení
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

V předchozím kódu jsme:

- Importovali potřebné knihovny
- Vytvořili objekt parametrů serveru, který využijeme k spuštění serveru, abychom se k němu mohli připojit přes klienta.
- Definovali metodu `run`, která volá `stdio_client`, spouštějící klientskou relaci.
- Vytvořili vstupní bod, kde předáváme metodu `run` do `asyncio.run`.

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

V předchozím kódu jsme:

- Importovali potřebné knihovny.
- Vytvořili stdio transport a klienta `mcpClient`. To použijeme pro výpis a vyvolání funkcí na MCP serveru.

Poznámka, v "Arguments" můžete ukázat buď na *.csproj* nebo na spustitelný soubor.

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
        
        // Vaše klientská logika jde sem
    }
}
```

V předchozím kódu jsme:

- Vytvořili hlavní metodu, která nastavuje SSE transport směřující na `http://localhost:8080`, kde bude běžet náš MCP server.
- Vytvořili třídu klienta, která přijímá transport jako konstruktorový parametr.
- V metodě `run` vytváříme synchronní MCP klienta používajícího transport a inicializujeme připojení.
- Použili SSE (Server-Sent Events) transport, který je vhodný pro HTTP komunikaci s MCP servery běžícími na Java Spring Boot.

#### Rust

Poznámka: Tento Rust klient předpokládá, že server je souběžný projekt pojmenovaný "calculator-server" ve stejné složce. Níže uvedený kód spustí server a připojí se k němu.

```rust
async fn main() -> Result<(), RmcpError> {
    // Předpokládejte, že server je sesterský projekt s názvem "calculator-server" ve stejném adresáři
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

    // TODO: Inicializovat

    // TODO: Vypsat nástroje

    // TODO: Zavolejte přidávací nástroj s argumenty = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Výpis funkcí serveru

Nyní máme klienta, který se může připojit, pokud program spustíme. Nicméně nevypisuje jeho funkce, udělejme tedy toto následující:

#### TypeScript

```typescript
// Seznam výzev
const prompts = await client.listPrompts();

// Seznam zdrojů
const resources = await client.listResources();

// seznam nástrojů
const tools = await client.listTools();
```

#### Python

```python
# Vypsat dostupné zdroje
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Vypsat dostupné nástroje
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Zde vypisujeme dostupné zdroje `list_resources()` a nástroje `list_tools` a vytiskneme je.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Výše je příklad, jak můžeme vypsat nástroje na serveru. Pro každý nástroj pak vypíšeme jeho název.

#### Java

```java
// Vyjmenujte a ukažte nástroje
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Můžete také pingnout server pro ověření připojení
client.ping();
```

V předchozím kódu jsme:

- Zavolali `listTools()` pro získání všech dostupných nástrojů z MCP serveru.
- Použili `ping()` pro ověření, že spojení se serverem funguje.
- `ListToolsResult` obsahuje informace o všech nástrojích včetně jejich názvů, popisů a vstupních schémat.

Skvělé, nyní máme zachyceny všechny funkce. Nyní otázka zní, kdy je používáme? Tento klient je poměrně jednoduchý, to znamená, že musíme explicitně vyvolat funkce, když je chceme použít. V další kapitole vytvoříme pokročilejšího klienta, který bude mít přístup ke svému vlastnímu velkému jazykovému modelu (LLM). Prozatím však uvidíme, jak můžeme vyvolat funkce na serveru:

#### Rust

V hlavní funkci, po inicializaci klienta, inicializujeme server a vypíšeme některé jeho funkce.

```rust
// Inicializovat
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Vypsat nástroje
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Vyvolání funkcí

Pro vyvolání funkcí musíme zajistit správné zadání argumentů a v některých případech i názvu toho, co vyvoláváme.

#### TypeScript

```typescript

// Přečíst zdroj
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Zavolat nástroj
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// zavolat prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

V předchozím kódu jsme:

- Přečetli zdroj, voláme zdroj pomocí `readResource()` a zadáváme `uri`. Na serverové straně to vypadá pravděpodobně takto:

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

    Hodnota `uri` `file://example.txt` odpovídá `file://{name}` na serveru. `example.txt` se namapuje na `name`.

- Zavolali nástroj, voláme ho zadáním jeho `name` a `arguments` takto:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Získali prompt, pro získání promptu voláte `getPrompt()` se `name` a `arguments`. Serverový kód je takovýto:

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

    a výsledný klientský kód vypadá takto, aby odpovídal deklaracím na serveru:

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
# Přečíst zdroj
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Zavolat nástroj
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

V předchozím kódu jsme:

- Zavolali zdroj s názvem `greeting` pomocí `read_resource`.
- Vyvolali nástroj s názvem `add` pomocí `call_tool`.

#### .NET

1. Přidejme kód pro zavolání nástroje:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Pro vypsání výsledku, zde je kód jak na to:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Zavolejte různé kalkulační nástroje
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

V předchozím kódu jsme:

- Zavolali několik kalkulačních nástrojů pomocí metody `callTool()` s objekty `CallToolRequest`.
- Každé volání nástroje specifikuje název nástroje a `Map` argumentů vyžadovaných nástrojem.
- Serverové nástroje očekávají specifické názvy parametrů (např. "a", "b" pro matematické operace).
- Výsledky jsou vráceny jako objekty `CallToolResult` obsahující odpovědi ze serveru.

#### Rust

```rust
// Zavolejte nástroj pro sčítání s argumenty = {"a": 3, "b": 2}
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

### -5- Spuštění klienta

Pro spuštění klienta zadejte v terminálu následující příkaz:

#### TypeScript

Přidejte následující položku do sekce "scripts" v souboru *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Spusťte klienta tímto příkazem:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Nejdříve se ujistěte, že váš MCP server běží na `http://localhost:8080`. Pak spusťte klienta:

```bash
# Sestavte svůj projekt
./mvnw clean compile

# Spusťte klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativně můžete spustit kompletní projekt klienta, který je k dispozici v řešení ve složce `03-GettingStarted\02-client\solution\java`:

```bash
# Přejděte do adresáře řešení
cd 03-GettingStarted/02-client/solution/java

# Sestavte a spusťte JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Úkol

V tomto úkolu použijete to, co jste se naučili, k vytvoření klienta podle vlastního návrhu.

Zde je server, který můžete použít a potřebujete jeho volání přes váš klientský kód: zkuste přidat více funkcí do serveru, aby byl zajímavější.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Vytvořit MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Přidat nástroj pro sčítání
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Přidat dynamický zdroj pozdravů
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

// Začít přijímat zprávy na stdin a odesílat zprávy na stdout

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

# Vytvořit MCP server
mcp = FastMCP("Demo")


# Přidat nástroj pro sčítání
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Přidat dynamický zdroj pozdravu
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

Podívejte se na tento projekt, kde se dozvíte, jak [přidat prompty a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Také si prohlédněte tento odkaz, jak vyvolávat [prompty a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [předchozí části](../../../../03-GettingStarted/01-first-server) jste se naučili, jak vytvořit jednoduchý MCP server v Rustu. Můžete na tom stavět nebo si prohlédnout tento odkaz pro více příkladů MCP serverů v Rustu: [Příklady MCP serverů](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Řešení

**Složka řešení** obsahuje kompletní, připravené k běhu implementace klientů, které demonstrují všechny koncepty pokryté v tomto tutoriálu. Každé řešení zahrnuje klientský i serverový kód, který je organizován v samostatných, soběstačných projektech.

### 📁 Struktura řešení

Adresář řešení je organizován podle programovacích jazyků:

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

### 🚀 Co každé řešení obsahuje

Každé jazykově specifické řešení poskytuje:

- **Kompletní implementaci klienta** se všemi funkcemi z tutoriálu
- **Funkční strukturu projektu** s odpovídajícími závislostmi a konfigurací
- **Skripty na kompilaci a spuštění** pro snadné nastavení a spuštění
- **Podrobný README** s instrukcemi specifickými pro daný jazyk
- **Ukázky správného zpracování chyb a výsledků**

### 📖 Použití řešení

1. **Přejděte do složky podle preferovaného jazyka**:

   ```bash
   cd solution/typescript/    # Pro TypeScript
   cd solution/java/          # Pro Java
   cd solution/python/        # Pro Python
   cd solution/dotnet/        # Pro .NET
   ```

2. **Řiďte se instrukcemi v README** v každé složce pro:
   - Instalaci závislostí
   - Sestavení projektu
   - Spuštění klienta

3. **Očekávaný výstup je následující**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pro kompletní dokumentaci a podrobné instrukce viz: **[📖 Dokumentace řešení](./solution/README.md)**

## 🎯 Kompletní příklady

Poskytli jsme kompletní pracovní implementace klientů pro všechny jazyky pokryté v tomto tutoriálu. Tyto příklady demonstrují veškerou výše popsanou funkcionalitu a mohou být použity jako referenční implementace nebo výchozí body pro vaše projekty.

### Dostupné kompletní příklady

| Jazyk   | Soubor                    | Popis                                                                             |
|---------|---------------------------|----------------------------------------------------------------------------------|
| **Java**  | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | Kompletní Java klient s využitím SSE transportu a důkladným ošetřením chyb       |
| **C#**    | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | Kompletní C# klient používající stdio transport s automatickým spuštěním serveru  |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletní TypeScript klient s plnou podporou MCP protokolu                        |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)       | Kompletní Python klient využívající async/await vzory                             |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | Kompletní Rust klient využívající Tokio pro asynchronní operace                   |

Každý kompletní příklad zahrnuje:
- ✅ **Navázání připojení** a zpracování chyb  
- ✅ **Objevování serveru** (nástroje, zdroje, výzvy tam, kde to je vhodné)  
- ✅ **Operace kalkulačky** (sčítání, odčítání, násobení, dělení, pomoc)  
- ✅ **Zpracování výsledků** a formátovaný výstup  
- ✅ **Komplexní zpracování chyb**  
- ✅ **Čistý, dokumentovaný kód** s komentáři krok za krokem  

### Začínáme s kompletními příklady

1. **Vyberte svůj preferovaný jazyk** z tabulky výše  
2. **Projděte si kompletní příkladový soubor** pro pochopení celé implementace  
3. **Spusťte příklad** podle pokynů v [`complete_examples.md`](./complete_examples.md)  
4. **Upravte a rozšiřte** příklad pro svůj konkrétní případ použití  

Pro podrobnou dokumentaci o spuštění a přizpůsobení těchto příkladů viz: **[📖 Dokumentace kompletních příkladů](./complete_examples.md)**

### 💡 Řešení vs. kompletní příklady

| **Složka řešení** | **Kompletní příklady** |
|-------------------|------------------------|
| Celá struktura projektu s build soubory | Implementace v jednom souboru |
| Připravené ke spuštění s závislostmi | Zaměřené na ukázky kódu |
| Produkční nastavení | Vzdělávací reference |
| Jazykově specifické nástroje | Porovnání napříč jazyky |

Obě přístupy jsou cenné – použijte **složku řešení** pro kompletní projekty a **kompletní příklady** pro učení a referenci.

## Klíčové body

Klíčové poznatky pro tuto kapitolu o klientech jsou následující:

- Lze je použít jak k objevení, tak ke spuštění funkcí na serveru.  
- Dokáží spustit server zatímco se sami spouštějí (jako v této kapitole), ale klienti se také mohou připojit k již běžícím serverům.  
- Jsou skvělým způsobem, jak otestovat schopnosti serveru vedle alternativ jako je Inspector, jak bylo popsáno v předchozí kapitole.  

## Další zdroje

- [Budování klientů v MCP](https://modelcontextprotocol.io/quickstart/client)

## Ukázky

- [Java kalkulačka](../samples/java/calculator/README.md)  
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript kalkulačka](../samples/javascript/README.md)  
- [TypeScript kalkulačka](../samples/typescript/README.md)  
- [Python kalkulačka](../../../../03-GettingStarted/samples/python)  
- [Rust kalkulačka](../../../../03-GettingStarted/samples/rust)  

## Co dál

- Dále: [Vytvoření klienta s LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překládací služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
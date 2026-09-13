# Vytvoření klienta

Klienti jsou vlastní aplikace nebo skripty, které komunikují přímo se serverem MCP za účelem žádosti o zdroje, nástroje a výzvy. Na rozdíl od použití inspektoru, který poskytuje grafické rozhraní pro interakci se serverem, psaní vlastního klienta umožňuje programovatelnou a automatizovanou interakci. To umožňuje vývojářům integrovat schopnosti MCP do vlastních pracovních postupů, automatizovat úkoly a vytvářet vlastní řešení přizpůsobená specifickým potřebám.

## Přehled

Tato lekce představuje koncept klientů v ekosystému Model Context Protocol (MCP). Naučíte se, jak napsat vlastní klient a připojit ho k serveru MCP.

## Cíle učení

Na konci této lekce budete schopni:

- Porozumět, co klient může dělat.
- Napsat vlastního klienta.
- Připojit a otestovat klienta se serverem MCP, aby bylo zajištěno, že server funguje podle očekávání.

## Co obnáší psaní klienta?

Pro napsání klienta musíte udělat následující:

- **Importovat správné knihovny**. Budete používat stejnou knihovnu jako dříve, pouze jiné konstrukty.
- **Vytvořit instanci klienta**. To zahrnuje vytvoření instance klienta a připojení k vybranému způsobu přenosu.
- **Rozhodnout, jaké zdroje zobrazit**. Váš server MCP obsahuje zdroje, nástroje a výzvy, musíte se rozhodnout, které chcete zobrazit.
- **Integrovat klienta do hostitelské aplikace**. Jakmile znáte schopnosti serveru, musíte tuto integraci provést do své hostitelské aplikace tak, aby se při zadání výzvy nebo jiného příkazu uživatelem vyvolala příslušná funkce serveru.

Nyní, když jsme si v hrubých rysech vysvětlili, co budeme dělat, podívejme se na příklad.

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

// Seznam výzev
const prompts = await client.listPrompts();

// Získat výzvu
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Seznam zdrojů
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
- Vytvořili instanci klienta a připojili ji pomocí stdio jako způsobu přenosu.
- Vyjmenovali výzvy, zdroje a nástroje a všechny je vyvolali.

Tady to máte, klient, který může komunikovat se serverem MCP.

V další cvičební části si podrobně vysvětlíme jednotlivé části kódu a co se v nich děje.

## Cvičení: Psaní klienta

Jak už bylo řečeno, pojďme si na vysvětlení kódu dát čas a klidně kódujte současně, pokud chcete.

### -1- Import knihoven

Importujme knihovny, které potřebujeme, budeme potřebovat odkazy na klienta a na náš zvolený přenosový protokol stdio. stdio je protokol pro věci určené k běhu na lokálním počítači. SSE je dalším přenosovým protokolem, který ukážeme v budoucích kapitolách, ale prozatím pokračujme se stdio.

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

Pro Javu vytvoříte klienta, který se připojí k serveru MCP z předchozího cvičení. Použijte stejnou strukturu projektu Java Spring Boot z [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), vytvořte novou třídu Java s názvem `SDKClient` ve složce `src/main/java/com/microsoft/mcp/sample/client/` a přidejte následující importy:

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

Musíte přidat následující závislosti do souboru `Cargo.toml`.

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

Odtud můžete importovat potřebné knihovny do kódu klienta.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Přejděme k vytváření instancí.

### -2- Vytvoření instance klienta a přenosu

Budeme potřebovat vytvořit instanci přenosu i instanci klienta:

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

- Vytvořili instanci přenosu stdio. Všimněte si, jak specifikuje příkaz a argumenty, jak najít a spustit server, protože to budeme potřebovat při vytváření klienta.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Vytvořili instanci klienta, přičemž jsme mu dali jméno a verzi.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Připojili klienta k vybranému přenosu.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvořit parametry serveru pro připojení stdio
server_params = StdioServerParameters(
    command="mcp",  # Spustitelný soubor
    args=["run", "server.py"],  # Volitelné argumenty příkazového řádku
    env=None,  # Volitelné proměnné prostředí
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
- Vytvořili objekt parametrů serveru, protože ho použijeme k spuštění serveru, aby se k němu klient mohl připojit.
- Definovali metodu `run`, která zavolá `stdio_client`, jež spustí klientskou relaci.
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
- Vytvořili přenos stdio a klienta `mcpClient`. To použijeme k výpisu a vyvolání funkcí na serveru MCP.

Poznámka: V "Arguments" můžete buď ukázat na *.csproj* nebo na spustitelný soubor.

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

- Vytvořili hlavní metodu, která nastavuje přenos SSE směřující na `http://localhost:8080`, kde bude běžet náš server MCP.
- Vytvořili klientskou třídu, která přijímá přenos jako parametr konstruktoru.
- V metodě `run` jsme vytvořili synchronní MCP klienta s přenosem a inicializovali připojení.
- Použili přenos SSE (Server-Sent Events), který je vhodný pro komunikaci po HTTP s MCP servery v Java Spring Boot.

#### Rust

Tento Rust klient předpokládá, že server je souběžný projekt pojmenovaný "calculator-server" ve stejné složce. Kód níže spustí server a připojí se k němu.

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

    // TODO: Inicializace

    // TODO: Vypsat nástroje

    // TODO: Zavolat nástroj add s argumenty = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Výpis funkcí serveru

Nyní máme klienta, který se může připojit při spuštění programu. Nicméně nevypisuje své funkce, tak to udělejme:

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

Zde vypisujeme dostupné zdroje, `list_resources()` a nástroje, `list_tools`, a tiskneme je.

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
// Vyjmenujte a předveďte nástroje
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Můžete také použít ping na server pro ověření připojení
client.ping();
```

V předchozím kódu jsme:

- Zavolali `listTools()` pro získání všech dostupných nástrojů ze serveru MCP.
- Použili `ping()` pro ověření, že spojení se serverem funguje.
- `ListToolsResult` obsahuje informace o všech nástrojích včetně jejich jmen, popisů a vstupních schémat.

Skvělé, teď jsme zachytili všechny funkce. Kdy je ale použít? Tento klient je poměrně jednoduchý, což znamená, že musíme explicitně volat funkce, když je chceme použít. V další kapitole vytvoříme pokročilejšího klienta, který bude mít přístup k vlastnímu velkému jazykovému modelu, LLM. Prozatím si ale ukážeme, jak vyvolat funkce na serveru:

#### Rust

V hlavní funkci po inicializaci klienta můžeme inicializovat server a vypsat některé jeho funkce.

```rust
// Inicializovat
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Vypsat nástroje
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Vyvolání funkcí

Pro vyvolání funkcí musíme správně specifikovat argumenty a v některých případech i název toho, co chceme vyvolat.

#### TypeScript

```typescript

// Načíst zdroj
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

// zavolat výzvu
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

V předchozím kódu jsme:

- Načetli zdroj, voláme ho funkcí `readResource()` s parametrem `uri`. Takto to asi vypadá na straně serveru:

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

    Hodnota `uri` `file://example.txt` odpovídá `file://{name}` na serveru. `example.txt` bude namapováno na `name`.

- Zavolali nástroj, voláme ho určením jeho `name` a `arguments` takto:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Získali výzvu, pro získání výzvy voláte `getPrompt()` s `name` a `arguments`. Kód serveru vypadá takto:

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

    a výsledný kód klienta tedy vypadá takto, aby odpovídal tomu, co je deklarováno na serveru:

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
# Přečtěte si zdroj
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Zavolejte nástroj
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

V předchozím kódu jsme:

- Zavolali zdroj s názvem `greeting` pomocí `read_resource`.
- Vyvolali nástroj `add` pomocí `call_tool`.

#### .NET

1. Přidáme kód pro zavolání nástroje:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Pro vypsání výsledku přidáme tento kód:

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

- Zavolali více kalkulačních nástrojů pomocí metody `callTool()` s objekty `CallToolRequest`.
- Každé volání nástroje specifikuje jméno nástroje a `Map` argumentů požadovaných nástrojem.
- Nástroje na serveru očekávají konkrétní názvy parametrů (např. "a", "b" pro matematické operace).
- Výsledky jsou vráceny jako objekty `CallToolResult`, které obsahují odpovědi ze serveru.

#### Rust

```rust
// Zavolejte nástroj add s argumenty = {"a": 3, "b": 2}
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

Pro spuštění klienta zadejte do terminálu následující příkaz:

#### TypeScript

Přidejte následující položku do sekce "scripts" v souboru *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Zavolejte klienta tímto příkazem:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Nejprve se ujistěte, že váš server MCP běží na `http://localhost:8080`. Pak spusťte klienta:

```bash
# Sestavte svůj projekt
./mvnw clean compile

# Spusťte klienta
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativně můžete spustit celý projekt klienta dostupný ve složce řešení `03-GettingStarted\02-client\solution\java`:

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

## Zadání

V tomto zadání použijete to, co jste se naučili o vytváření klienta, ale vytvoříte si vlastního klienta.

Zde je server, který můžete použít a který musíte volat přes svůj klientský kód; zkuste přidat do serveru více funkcí, aby byl zajímavější.

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

// Přidat dynamický zdroj pozdravu
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

# Vytvořit server MCP
mcp = FastMCP("Demo")


# Přidat nástroj pro sčítání
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Přidat dynamický uvítací zdroj
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

Podívejte se na tento projekt, abyste zjistili, jak můžete [přidat výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Také si prohlédněte tento odkaz pro informace, jak vyvolávat [výzvy a zdroje](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

V [předchozí sekci](../../../../03-GettingStarted/01-first-server) jste se naučili, jak vytvořit jednoduchý MCP server v Rustu. Můžete na tom stavět dále, nebo se podívat na tento odkaz pro další příklady MCP serverů založených na Rustu: [Příklady MCP serverů](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Řešení

**Složka řešení** obsahuje kompletní, připravené klientské implementace, které demonstrují všechny koncepty porušené v tomto tutoriálu. Každé řešení zahrnuje klientský i serverový kód uspořádaný v samostatných, samostatně fungujících projektech.

### 📁 Struktura řešení

Adresář řešení je uspořádán podle programovacího jazyka:

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
- **Funkční strukturu projektu** s potřebnými závislostmi a konfigurací
- **Skripty pro sestavení a spuštění** pro snadné nastavení a spuštění
- **Podrobný README** s instrukcemi specifickými pro jazyk
- **Ukázky zacházení s chybami** a zpracování výsledků

### 📖 Použití řešení

1. **Přejděte do složky vašeho preferovaného jazyka**:

   ```bash
   cd solution/typescript/    # Pro TypeScript
   cd solution/java/          # Pro Javu
   cd solution/python/        # Pro Python
   cd solution/dotnet/        # Pro .NET
   ```

2. **Postupujte podle návodu v README** v každé složce pro:
   - Instalaci závislostí
   - Sestavení projektu
   - Spuštění klienta

3. **Příklad výstupu** by měl vypadat takto:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pro kompletní dokumentaci a krok za krokem instrukce viz: **[📖 Dokumentace řešení](./solution/README.md)**

## 🎯 Kompletní příklady

Poskytli jsme kompletní, funkční implementace klientů pro všechny programovací jazyky, pokryté v tomto tutoriálu. Tyto příklady demonstrují veškerou výše popsanou funkčnost a mohou být použity jako referenční implementace nebo jako výchozí body pro vaše vlastní projekty.

### Dostupné kompletní příklady

| Jazyk | Soubor | Popis |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kompletní Java klient použitím přenosu SSE s komplexním zacházením s chybami |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kompletní C# klient použitím přenosu stdio se automatickým spuštěním serveru |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kompletní TypeScript klient s plnou podporou protokolu MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kompletní Python klient používající async/await vzory |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kompletní Rust klient používající Tokio pro asynchronní operace |

Každý kompletní příklad obsahuje:

- ✅ **Založení spojení** a zacházení s chybami
- ✅ **Objevování serveru** (nástroje, zdroje, výzvy tam kde jsou)
- ✅ **Operace kalkulačky** (sčítání, odečítání, násobení, dělení, pomoc)
- ✅ **Zpracování výsledků** a formátovaný výstup
- ✅ **Komplexní zacházení s chybami**

- ✅ **Čistý, dokumentovaný kód** s komentáři krok za krokem

### Začínáme s kompletními příklady

1. **Vyberte si preferovaný jazyk** z tabulky výše
2. **Prohlédněte si kompletní ukázkový soubor** pro pochopení celé implementace
3. **Spusťte příklad** podle pokynů v [`complete_examples.md`](./complete_examples.md)
4. **Upravte a rozšiřte** příklad pro vaše konkrétní použití

Pro podrobné dokumentace o spuštění a přizpůsobení těchto příkladů se podívejte na: **[📖 Dokumentace kompletních příkladů](./complete_examples.md)**

### 💡 Řešení vs. kompletní příklady

| **Složka řešení** | **Kompletní příklady** |
|--------------------|--------------------- |
| Plná struktura projektu s konfiguračními soubory | Jednosouborové implementace |
| Připraveno ke spuštění s závislostmi | Zaměřené ukázky kódu |
| Produkčně podobné nastavení | Vzdělávací reference |
| Nástroje specifické pro jazyk | Porovnání mezi jazyky |

Obě metody jsou cenné - použijte **složku řešení** pro kompletní projekty a **kompletní příklady** pro učení a referenci.

## Klíčová zjištění

Klíčová zjištění pro tuto kapitolu ohledně klientů jsou následující:

- Lze je použít jak k objevování, tak k vyvolávání funkcí na serveru.
- Mohou spustit server současně s jeho spuštěním (jako v této kapitole), ale klienti se také mohou připojit k již běžícím serverům.
- Jsou skvělým způsobem, jak otestovat schopnosti serveru vedle alternativ jako je Inspektor, jak bylo popsáno v předchozí kapitole.

## Další zdroje

- [Tvorba klientů v MCP](https://modelcontextprotocol.io/quickstart/client)

## Ukázky

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.NET Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Co dál

- Dále: [Vytvoření klienta s LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
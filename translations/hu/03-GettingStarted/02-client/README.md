# Ügyfél létrehozása

Az ügyfelek olyan egyedi alkalmazások vagy szkriptek, amelyek közvetlenül kommunikálnak egy MCP szerverrel, hogy erőforrásokat, eszközöket és promptokat kérjenek. Ellentétben az ellenőrző eszköz használatával, amely grafikus felületet biztosít a szerverrel való interakcióhoz, saját ügyfél írása lehetővé teszi a programozott és automatizált interakciókat. Ez lehetővé teszi a fejlesztők számára, hogy az MCP képességeit integrálják saját munkafolyamataikba, automatizálják a feladatokat, és egyedi megoldásokat hozzanak létre specifikus igényekre szabva.

## Áttekintés

Ez a lecke bemutatja az ügyfelek fogalmát a Model Context Protocol (MCP) ökoszisztémájában. Megtanulod, hogyan írj saját ügyfelet, és hogyan csatlakoztasd azt egy MCP szerverhez.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni, hogy mit tud egy ügyfél.
- Saját ügyfelet írni.
- Csatlakoztatni és tesztelni az ügyfelet egy MCP szerverrel, hogy megbizonyosodj arról, hogy az megfelelően működik.

## Mi szükséges egy ügyfél írásához?

Egy ügyfél írásához a következőkre lesz szükséged:

- **A megfelelő könyvtárak importálása**. Ugyanazt a könyvtárat fogod használni, mint korábban, csak más konstrukciókat.
- **Egy ügyfél példányosítása**. Ez magában foglalja egy ügyfélpéldány létrehozását és annak csatlakoztatását a választott szállítási módszerhez.
- **Döntés az erőforrások listázásáról**. Az MCP szerver erőforrásokkal, eszközökkel és promptokkal rendelkezik, el kell döntened, melyiket listázod.
- **Az ügyfél integrálása egy gazdaalkalmazásba**. Miután megismerted a szerver képességeit, integrálnod kell azt a gazdaalkalmazásodba, hogy ha egy felhasználó promptot vagy más parancsot ír be, a megfelelő szerverfunkció legyen meghívva.

Most, hogy magas szinten megértettük, mit fogunk csinálni, nézzünk meg egy példát.

### Példa ügyfél

Nézzünk meg egy példát egy ügyfélre:

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

A fenti kódban:

- Importáljuk a könyvtárakat.
- Létrehozunk egy ügyfélpéldányt, és stdio-t használunk a szállításhoz.
- Listázzuk a promptokat, erőforrásokat és eszközöket, majd mindet meghívjuk.

És íme, egy ügyfél, amely képes kommunikálni egy MCP szerverrel.

A következő gyakorlati szakaszban bontsuk le a kódrészleteket, és magyarázzuk el, mi történik.

## Gyakorlat: Ügyfél írása

Ahogy korábban említettük, szánjunk időt a kód magyarázatára, és ha szeretnéd, kódolj velünk.

### -1- Könyvtárak importálása

Importáljuk a szükséges könyvtárakat. Szükségünk lesz egy ügyfélre és a választott szállítási protokollra, stdio-ra. Az stdio egy protokoll, amely helyi gépen futó dolgokhoz készült. Az SSE egy másik szállítási protokoll, amelyet a későbbi fejezetekben mutatunk be, de ez a másik lehetőséged. Egyelőre azonban folytassuk az stdio-val.

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

A Java esetében egy ügyfelet fogsz létrehozni, amely csatlakozik az előző gyakorlatban létrehozott MCP szerverhez. Használva a Java Spring Boot projektstruktúrát a [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) fejezetből, hozz létre egy új Java osztályt `SDKClient` néven a `src/main/java/com/microsoft/mcp/sample/client/` mappában, és add hozzá a következő importokat:

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

A `Cargo.toml` fájlodhoz hozzá kell adnod a következő függőségeket.

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

Ezután importálhatod a szükséges könyvtárakat az ügyfélkódodban.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Folytassuk az ügyfél példányosításával.

### -2- Ügyfél és szállítás példányosítása

Létre kell hoznunk egy szállítási példányt és az ügyfél példányát:

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

A fenti kódban:

- Létrehoztunk egy stdio szállítási példányt. Figyeld meg, hogy megadja a parancsot és az argumentumokat, hogy hogyan találja meg és indítsa el a szervert, mivel ezt kell tennünk az ügyfél létrehozásakor.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Létrehoztunk egy ügyfelet, megadva neki egy nevet és verziót.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Csatlakoztattuk az ügyfelet a választott szállításhoz.

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

A fenti kódban:

- Importáltuk a szükséges könyvtárakat.
- Létrehoztunk egy szerverparaméter-objektumot, amelyet a szerver futtatásához használunk, hogy csatlakozhassunk hozzá az ügyfelünkkel.
- Meghatároztunk egy `run` nevű metódust, amely viszont meghívja az `stdio_client`-et, amely elindít egy ügyfélmunkamenetet.
- Létrehoztunk egy belépési pontot, ahol az `asyncio.run`-nak átadjuk a `run` metódust.

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

A fenti kódban:

- Importáltuk a szükséges könyvtárakat.
- Létrehoztunk egy stdio szállítást, és létrehoztunk egy `mcpClient` nevű ügyfelet. Ez utóbbit fogjuk használni az MCP szerver funkcióinak listázására és meghívására.

Megjegyzés: az "Arguments" mezőben megadhatod a *.csproj* fájlt vagy a futtatható fájlt.

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

A fenti kódban:

- Létrehoztunk egy fő metódust, amely beállít egy SSE szállítást, amely a `http://localhost:8080` címre mutat, ahol az MCP szerverünk futni fog.
- Létrehoztunk egy ügyfélosztályt, amely a szállítást konstruktorparaméterként veszi át.
- A `run` metódusban létrehoztunk egy szinkron MCP ügyfelet a szállítás használatával, és inicializáltuk a kapcsolatot.
- Az SSE (Server-Sent Events) szállítást használtuk, amely alkalmas HTTP-alapú kommunikációra Java Spring Boot MCP szerverekkel.

#### Rust

Ez a Rust ügyfél feltételezi, hogy a szerver egy "calculator-server" nevű testvérprojekt ugyanabban a könyvtárban. Az alábbi kód elindítja a szervert és csatlakozik hozzá.

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

### -3- A szerver funkcióinak listázása

Most van egy ügyfelünk, amely képes csatlakozni, ha a programot futtatjuk. Azonban még nem listázza a funkcióit, ezért tegyük meg ezt:

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

Itt listázzuk az elérhető erőforrásokat a `list_resources()` és az eszközöket a `list_tools` segítségével, majd kiírjuk őket.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

A fenti példa megmutatja, hogyan listázhatjuk a szerver eszközeit. Az egyes eszközök esetében kiírjuk a nevüket.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

A fenti kódban:

- Meghívtuk a `listTools()` metódust, hogy megszerezzük az összes elérhető eszközt az MCP szervertől.
- Használtuk a `ping()` metódust, hogy ellenőrizzük a szerverrel való kapcsolat működését.
- A `ListToolsResult` tartalmazza az összes eszköz nevét, leírását és bemeneti sémáját.

Nagyszerű, most már rögzítettük az összes funkciót. Most az a kérdés, mikor használjuk őket? Nos, ez az ügyfél elég egyszerű, egyszerű abban az értelemben, hogy kifejezetten meg kell hívnunk a funkciókat, amikor szükségünk van rájuk. A következő fejezetben egy fejlettebb ügyfelet fogunk létrehozni, amely hozzáfér saját nagy nyelvi modelljéhez (LLM). Most azonban nézzük meg, hogyan hívhatjuk meg a szerver funkcióit:

#### Rust

A fő függvényben, miután inicializáltuk az ügyfelet, inicializálhatjuk a szervert, és listázhatjuk néhány funkcióját.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkciók meghívása

A funkciók meghívásához biztosítanunk kell, hogy megadjuk a megfelelő argumentumokat, és bizonyos esetekben a meghívni kívánt funkció nevét.

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

A fenti kódban:

- Egy erőforrást olvasunk be, amelyet a `readResource()` metódussal hívunk meg, megadva a `uri`-t. Így nézhet ki a szerver oldalon:

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

    Az `uri` értékünk `file://example.txt` megfelel a szerveren a `file://{name}`-nek. Az `example.txt` a `name`-hez lesz leképezve.

- Egy eszközt hívunk meg, megadva a `name`-t és az `arguments`-t, például így:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Egy promptot kérünk, a `getPrompt()` metódussal, megadva a `name`-t és az `arguments`-t. A szerver kódja így néz ki:

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

    Az ügyfélkódod így fog kinézni, hogy illeszkedjen a szerveren deklaráltakhoz:

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

A fenti kódban:

- Meghívtunk egy `greeting` nevű erőforrást a `read_resource` segítségével.
- Meghívtunk egy `add` nevű eszközt a `call_tool` segítségével.

#### .NET

1. Adjunk hozzá néhány kódot egy eszköz meghívásához:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Az eredmény kiírásához itt van néhány kód:

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

A fenti kódban:

- Több számológép-eszközt hívtunk meg a `callTool()` metódussal, amely `CallToolRequest` objektumokat használ.
- Minden eszközhívás megadja az eszköz nevét és egy `Map`-et az eszköz által igényelt argumentumokkal.
- A szerver eszközei specifikus paraméterneveket várnak (például "a", "b" matematikai műveletekhez).
- Az eredmények `CallToolResult` objektumokként térnek vissza, amelyek tartalmazzák a szerver válaszát.

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

### -5- Az ügyfél futtatása

Az ügyfél futtatásához írd be a következő parancsot a terminálba:

#### TypeScript

Add hozzá a következő bejegyzést a *package.json* "scripts" szekciójához:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Futtasd az ügyfelet a következő paranccsal:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Először győződj meg arról, hogy az MCP szerver fut a `http://localhost:8080` címen. Ezután futtasd az ügyfelet:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatívaként futtathatod a teljes ügyfélprojektet, amely a `03-GettingStarted\02-client\solution\java` megoldás mappában található:

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

## Feladat

Ebben a feladatban az eddig tanultakat felhasználva saját ügyfelet kell létrehoznod.

Itt van egy szerver, amelyet az ügyfélkódoddal kell meghívnod. Próbálj meg további funkciókat hozzáadni a szerverhez, hogy érdekesebbé tedd.

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

Nézd meg ezt a projektet, hogy megtudd, hogyan adhatsz hozzá [promptokat és erőforrásokat](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Ezenkívül nézd meg ezt a linket, hogy megtudd, hogyan hívhatsz meg [promptokat és erőforrásokat](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Az [előző szakaszban](../../../../03-GettingStarted/01-first-server) megtanultad, hogyan hozz létre egy egyszerű MCP szervert Rustban. Folytathatod annak bővítését, vagy nézd meg ezt a linket további Rust-alapú MCP szerver példákért: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Megoldás

A **megoldás mappa** teljes, futtatható ügyfélmegvalósításokat tartalmaz, amelyek bemutatják az oktatóanyagban tárgyalt összes koncepciót. Minden megoldás tartalmazza az ügyfél- és szerverkódot külön, önálló projektekben.

### 📁 Megoldás struktúra

A megoldás könyvtár programozási nyelv szerint van szervezve:

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

### 🚀 Mit tartalmaz minden megoldás?

Minden nyelvspecifikus megoldás biztosítja:

- **Teljes ügyfélmegvalósítás** az oktatóanyag összes funkciójával.
- **Működő projektstruktúra** megfelelő függőségekkel és konfigurációval.
- **Build- és futtatási szkriptek** az egyszerű beállításhoz és futtatáshoz.
- **Részletes README** nyelvspecifikus utasításokkal.
- **Hibakezelési** és eredményfeldolgozási példák.

### 📖 A megoldások használata

1. **Navigálj a preferált nyelv mappájába**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Kövesd a README utasításait** minden mappában:
   - A függőségek telepítéséhez.
   - A projekt buildeléséhez.
   - Az ügyfél futtatásához.

3. **Példa kimenet**, amit látnod kell:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

A teljes dokumentációért és lépésről lépésre szóló utasításokért lásd: **[📖 Megoldás dokumentáció](./solution/README.md)**

## 🎯 Teljes példák

Teljes, működő ügyfélmegvalósításokat biztosítottunk az oktatóanyagban tárgyalt összes programozási nyelvhez. Ezek a példák bemutatják a fent leírt teljes funkcionalitást, és referenciaként vagy saját projektek kiindulópontjaként használhatók.

### Elérhető teljes példák

| Nyelv | Fájl | Leírás |
|-------|------|--------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Teljes Java ügyfél SSE szállítással, átfogó hibakezeléssel |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Teljes C# ügyfél stdio szállítással, automatikus szerverindítással |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Teljes TypeScript ügyfél teljes MCP protokoll támogatással |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Teljes Python
Minden teljes példa tartalmazza:

- ✅ **Kapcsolat létrehozása** és hibakezelés
- ✅ **Szerver felfedezése** (eszközök, források, javaslatok, ahol alkalmazható)
- ✅ **Számológép műveletek** (összeadás, kivonás, szorzás, osztás, súgó)
- ✅ **Eredmény feldolgozása** és formázott kimenet
- ✅ **Átfogó hibakezelés**
- ✅ **Tiszta, dokumentált kód** lépésről lépésre kommentekkel

### Teljes példák használatának kezdő lépései

1. **Válaszd ki a preferált nyelvet** a fenti táblázatból
2. **Tekintsd át a teljes példa fájlt**, hogy megértsd a teljes implementációt
3. **Futtasd a példát** a [`complete_examples.md`](./complete_examples.md) fájlban található utasítások szerint
4. **Módosítsd és bővítsd** a példát a saját igényeid szerint

A példák futtatásáról és testreszabásáról szóló részletes dokumentációt itt találod: **[📖 Teljes példák dokumentációja](./complete_examples.md)**

### 💡 Megoldás vs. Teljes példák

| **Megoldás mappa** | **Teljes példák** |
|--------------------|--------------------- |
| Teljes projektstruktúra build fájlokkal | Egyfájlos implementációk |
| Azonnal futtatható függőségekkel | Kiemelt kódpéldák |
| Produkciós környezethez hasonló beállítás | Oktatási referencia |
| Nyelvspecifikus eszközök | Nyelvek közötti összehasonlítás |

Mindkét megközelítés értékes - használd a **megoldás mappát** teljes projektekhez, és a **teljes példákat** tanuláshoz és referenciaként.

## Fő tanulságok

A fejezet fő tanulságai az ügyfelekről:

- Használhatók szerver funkciók felfedezésére és meghívására.
- Képesek szervert indítani, miközben maguk is elindulnak (mint ebben a fejezetben), de csatlakozhatnak már futó szerverekhez is.
- Kiváló módja a szerver képességeinek tesztelésére, alternatívák mellett, mint például az Inspector, ahogy az előző fejezetben bemutattuk.

## További források

- [Ügyfelek építése MCP-ben](https://modelcontextprotocol.io/quickstart/client)

## Minták

- [Java Számológép](../samples/java/calculator/README.md)
- [.Net Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)
- [Rust Számológép](../../../../03-GettingStarted/samples/rust)

## Mi következik?

- Következő: [Ügyfél létrehozása LLM-mel](../03-llm-client/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
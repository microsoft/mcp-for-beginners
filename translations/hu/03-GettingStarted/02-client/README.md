# Ügyfél létrehozása

Az ügyfelek egyedi alkalmazások vagy szkriptek, amelyek közvetlenül kommunikálnak egy MCP szerverrel erőforrások, eszközök és parancsok kérésére. Ellentétben az inspector eszköz használatával, amely grafikus felületet biztosít a szerverrel való interakcióhoz, a saját ügyfél megírása lehetővé teszi a programozott és automatizált interakciókat. Ez lehetővé teszi a fejlesztők számára, hogy integrálják az MCP képességeit a saját munkafolyamataikba, automatizálják a feladatokat és testreszabott megoldásokat építsenek adott igényekhez.

## Áttekintés

Ez a lecke bemutatja az ügyfelek fogalmát a Model Context Protocol (MCP) ökoszisztémán belül. Megtanulod, hogyan írj saját ügyfelet, és hogyan kapcsolódjon az MCP szerverhez.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni, mit tud egy ügyfél.
- Megírni a saját ügyfeledet.
- Csatlakozni és tesztelni az ügyfelet egy MCP szerverrel, hogy megbizonyosodj arról, hogy működik a szerver a vártak szerint.

## Mi szükséges egy ügyfél megírásához?

Az ügyfél megírásához a következőket kell tenned:

- **A megfelelő könyvtárak importálása**. Ugyanazt a könyvtárat fogod használni, mint korábban, de más konstrukciókban.
- **Egy ügyfél példányosítása**. Ez magában foglalja egy ügyfél példány létrehozását és annak a kiválasztott transzport módszerhez való csatlakoztatását.
- **Döntés arról, hogy mely erőforrásokat listázzuk**. Az MCP szervered erőforrásokkal, eszközökkel és parancsokkal érkezik, döntened kell, melyeket listázod.
- **Az ügyfél integrálása egy host alkalmazásba**. Ha ismered a szerver képességeit, akkor integrálnod kell az ügyfelet a host alkalmazásba úgy, hogy ha a felhasználó promptot vagy más parancsot ír, a megfelelő szerver funkció végrehajtódik.

Most, hogy nagy vonalakban megértettük, mit fogunk tenni, nézzük meg a következő példát.

### Példa ügyfél

Nézzük meg ezt a példa ügyfelet:

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

// Listázza a promptokat
const prompts = await client.listPrompts();

// Egy prompt lekérése
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listázza az erőforrásokat
const resources = await client.listResources();

// Erőforrás olvasása
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Eszköz meghívása
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

A fenti kódban:

- Importáljuk a könyvtárakat
- Létrehozunk egy ügyfél példányt, és stdio-n keresztül kapcsolódunk.
- Listázzuk a promptokat, erőforrásokat és eszközöket, majd mindet meghívjuk.

Így van, egy olyan ügyfél, ami tud kommunikálni egy MCP szerverrel.

Tartsunk most egy kis szünetet a következő gyakorlati szakaszban, és bontsuk le a kódrészleteket, hogy elmagyarázzuk, mi történik.

## Gyakorlat: Ügyfél írása

Ahogy fentebb elhangzott, szánjunk rá időt a kód magyarázatára, és bátran kövesd a kódot, ha szeretnél.

### -1- Könyvtárak importálása

Importáljuk a szükséges könyvtárakat, referenciákra lesz szükségünk az ügyfélhez és a választott transzport protokollhoz, az stdio-hoz. Az stdio egy protokoll olyan dolgokhoz, amik a helyi gépeden futnak. Az SSE egy másik transzport protokoll, amelyet a jövőbeli fejezetekben mutatunk be, de ez az alternatívád. Most viszont folytassuk stdio-val.

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

Java esetében egy olyan ügyfelet hozol létre, amely csatlakozik az előző feladatban lévő MCP szerverhez. Ugyanazt a Java Spring Boot projektstruktúrát használva, mint a [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) cikkben, hozz létre egy új Java osztályt `SDKClient` néven a `src/main/java/com/microsoft/mcp/sample/client/` mappában, és add hozzá a következő importokat:

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

A `Cargo.toml` fájlodhoz a következő függőségeket kell hozzáadnod.

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

Ezután importálhatod a szükséges könyvtárakat az ügyfél kódodban.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Folytassuk az inicializálással.

### -2- Ügyfél és transzport példányosítása

Létre kell hoznunk egy transzport példányt, illetve az ügyfél példányát:

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

A fentebbi kódban:

- Létrehoztunk egy stdio transzport példányt. Figyeld meg, hogy megadjuk a parancsot és argumentumokat a szerver megtalálására és elindítására, mert ezt meg kell tennünk az ügyfél létrehozásakor.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Példányosítottunk egy ügyfelet, megadva neki nevet és verziót.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Csatlakoztattuk az ügyfelet a kiválasztott transzporthoz.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Szerver paraméterek létrehozása stdio kapcsolathoz
server_params = StdioServerParameters(
    command="mcp",  # Futtatható fájl
    args=["run", "server.py"],  # Opcionális parancssori argumentumok
    env=None,  # Opcionális környezeti változók
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Kapcsolat inicializálása
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

A fentebbi kódban:

- Importáltuk a szükséges könyvtárakat
- Létrehoztunk egy szerver paraméter objektumot, mert ezzel fogjuk futtatni a szervert, hogy aztán az ügyfél hozzá tudjon csatlakozni.
- Definiáltunk egy `run` metódust, amely meghívja a `stdio_client`-et, ami elindít egy ügyfél munkamenetet.
- Létrehoztunk egy belépési pontot, ahol az `asyncio.run`-nak átadjuk a `run` metódust.

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

A fenti kódban:

- Importáltuk a szükséges könyvtárakat.
- Létrehoztunk egy stdio transzportot és egy `mcpClient` ügyfelet. Ezt fogjuk használni, hogy listázzuk és meghívjuk az MCP szerver funkcióit.

Megjegyzés: az "Arguments"-nél megadhatod vagy a *.csproj*-t, vagy a futtatható fájlt.

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
        
        // Ide jön az ügyfél logikája
    }
}
```

A fenti kódban:

- Létrehoztunk egy fő metódust, ami beállít egy SSE transzportot, amely a `http://localhost:8080` címet használja, ahol az MCP szerver futni fog.
- Létrehoztunk egy kliens osztályt, amely konstruktor paraméterként fogadja a transzportot.
- A `run` metódusban létrehozunk egy szinkron MCP ügyfelet a transzporttal, és inicializáljuk a kapcsolatot.
- Az SSE transzportot használtuk, amely alkalmas HTTP-alapú kommunikációra Java Spring Boot MCP szerverekkel.

#### Rust

Ez a Rust kliens feltételezi, hogy a szerver egy testvérprojekt "calculator-server" néven ugyanabban a könyvtárban. Az alábbi kód elindítja a szervert és csatlakozik hozzá.

```rust
async fn main() -> Result<(), RmcpError> {
    // Tegyük fel, hogy a szerver egy testvérprojekt, amely a "calculator-server" nevű ugyanabban a könyvtárban van
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

    // TODO: Inicializálás

    // TODO: Eszközök listázása

    // TODO: Hívja meg az add eszközt a következő argumentumokkal = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- A szerver funkcióinak listázása

Most, hogy van egy ügyfelünk, amely csatlakozni képes, futtathatjuk a programot. Azonban ez még nem listázza a funkciókat, tegyük meg hát ezt:

#### TypeScript

```typescript
// Lista parancsokról
const prompts = await client.listPrompts();

// Lista erőforrásokról
const resources = await client.listResources();

// lista eszközökről
const tools = await client.listTools();
```

#### Python

```python
# Elérhető erőforrások listázása
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Elérhető eszközök listázása
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Itt listázzuk az elérhető erőforrásokat `list_resources()` és eszközöket `list_tools`, majd kiírjuk őket.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Az előző példában látható, hogyan listázzuk az eszközöket a szerveren. Minden eszköznél kiírjuk a nevét.

#### Java

```java
// Eszközök listázása és bemutatása
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// A kapcsolat ellenőrzéséhez pingelhetjük a szervert is
client.ping();
```

A fenti kódban:

- Meghívtuk a `listTools()`-t, hogy megkapjuk az összes elérhető eszközt az MCP szerverről.
- Használtuk a `ping()`-et annak ellenőrzésére, hogy működik-e a kapcsolat a szerverrel.
- A `ListToolsResult` tartalmazza az összes eszköz információját, beleértve a neveket, leírásokat és bemeneti sémákat.

Remek, így az összes funkciót lekértük. Most pedig a kérdés, mikor használjuk őket? Ez az ügyfél elég egyszerű, egyszerű abban az értelemben, hogy explicit módon kell meghívnunk a funkciókat, amikor szükség van rájuk. A következő fejezetben egy fejlettebb ügyfelet hozunk létre, amely saját nagynyelvű modellt, LLM-et használ. Egyelőre nézzük meg, hogyan tudjuk meghívni a szerver funkcióit:

#### Rust

A main függvényben az ügyfél inicializálása után inicializálhatjuk a szervert, és listázhatunk néhány funkciót.

```rust
// Inicializálás
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Eszközök listázása
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkciók meghívása

A funkciók meghívásához biztosítani kell, hogy a helyes argumentumokat és adott esetben az elnevezést megadjuk.

#### TypeScript

```typescript

// Erőforrás olvasása
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Eszköz hívása
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// prompt hívása
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

A fentebbi kódban:

- Egy erőforrást olvasunk, úgy hívjuk meg az erőforrást, hogy `readResource()`-t hívunk `uri` megadásával. Így nézhet ki valószínűleg a szerver oldalon:

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

    Az `uri` értékünk `file://example.txt` megfelel a szerveren lévő `file://{name}`-nek. Az `example.txt` át lesz térképezve `name`-re.

- Meghívunk egy eszközt, amihez megadjuk a nevét (`name`) és az argumentumait (`arguments`):

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Promptot kérünk, ehhez a `getPrompt()`-ot hívjuk meg `name` és `arguments` megadásával. A szerver kód így néz ki:

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

    A kliens kód pedig ehhez igazodik:

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
# Olvasson be egy erőforrást
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Hívjon meg egy eszközt
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

A kódban:

- Meghívtuk az `greeting` nevű erőforrást a `read_resource` segítségével.
- Meghívtunk egy `add` nevű eszközt a `call_tool` használatával.

#### .NET

1. Adjunk hozzá kódot egy eszköz meghívására:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. Az eredmény kiíratásához itt egy példa:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Különböző számológép eszközök hívása
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

- Több számológép eszközt hívtunk meg a `callTool()` metódussal, amely `CallToolRequest` objektumokat kapott.
- Minden eszköz meghívás megadja az eszköz nevét és egy `Map`-et az adott eszköz által igényelt argumentumokkal.
- A szerver eszközök specifikus paraméter neveket várnak (például "a", "b" a matematikai műveletekhez).
- Az eredmények `CallToolResult` objektumokként érkeznek vissza, amelyek tartalmazzák a szerver válaszát.

#### Rust

```rust
// Hívd meg az add eszközt a következő argumentumokkal = {"a": 3, "b": 2}
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

### -5- Ügyfél futtatása

Az ügyfél futtatásához gépeld be a következő parancsot a terminálba:

#### TypeScript

Add hozzá a következő bejegyzést a *package.json* "scripts" szekciójához:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

A kliens indítása a következő parancssal:

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
# Építsd meg a projekted
./mvnw clean compile

# Futtasd az ügyfelet
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatívaként futtathatod a teljes ügyfél projektet, amely a `03-GettingStarted\02-client\solution\java` megoldás mappában található:

```bash
# Navigáljon a megoldás könyvtárába
cd 03-GettingStarted/02-client/solution/java

# Fordítsa le és futtassa a JAR fájlt
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Feladat

Ebben a feladatban a tanultakat felhasználva készítesz egy saját ügyfelet.

Íme egy szerver, amelyet használhatsz, és amelyet a kliens kódodon keresztül kell meghívnod. Próbálj meg további funkciókat hozzáadni a szerverhez, hogy érdekesebbé tedd.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Hozzon létre egy MCP szervert
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Adjon hozzá egy összeadási eszközt
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Adjon hozzá egy dinamikus üdvözlő erőforrást
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

// Kezdje el fogadni az üzeneteket a stdin-en és küldeni azokat a stdout-ra

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

# Egy MCP szerver létrehozása
mcp = FastMCP("Demo")


# Egy összeadó eszköz hozzáadása
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Egy dinamikus üdvözlő erőforrás hozzáadása
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

Nézd meg ezt a projektet, hogy lássd, hogyan lehet [promptokat és erőforrásokat hozzáadni](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Ezenkívül nézd meg ezt a linket, hogy hogyan kell [promptokat és erőforrásokat meghívni](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

A [korábbi részben](../../../../03-GettingStarted/01-first-server) megtanultad, hogyan készíts egyszerű MCP szervert Rust-ban. Folytathatod ezt a fejlesztést, vagy megnézheted ezt a linket további Rust-alapú MCP szerver példákért: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Megoldás

A **megoldás mappa** tartalmazza a teljes, futtatható ügyfél megvalósításokat, amelyek demonstrálják a bemutatott koncepciókat ebben az oktatóanyagban. Minden megoldás külön-külön, önálló projektekben tartalmaz kliens és szerver kódot.

### 📁 Megoldás felépítése

A megoldás könyvtára programozási nyelv szerint van rendszerezve:

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

### 🚀 Mit tartalmaz egy-egy megoldás

Minden nyelvspecifikus megoldás a következőket nyújtja:

- **Teljes kliens megvalósítás**, az oktatóanyagban bemutatott összes funkcióval
- **Működő projekt struktúra** a megfelelő függőségekkel és konfigurációval
- **Build és futtató szkriptek** a könnyű telepítéshez és futtatáshoz
- **Részletes README** nyelvspecifikus utasításokkal
- **Hibakezelés és eredmény feldolgozás példái**

### 📖 A megoldások használata

1. **Navigálj a kívánt nyelv könyvtárába**:

   ```bash
   cd solution/typescript/    # TypeScripthez
   cd solution/java/          # Java-hoz
   cd solution/python/        # Pythonhoz
   cd solution/dotnet/        # .NET-hez
   ```

2. **Kövesd a README utasításait** minden könyvtárban a:
   - Függőségek telepítéséhez
   - Projekt buildeléséhez
   - Ügyfél futtatásához

3. **A következő kimenetet kellene látnod**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

A teljes dokumentáció és lépésenkénti útmutatók elérhetők itt: **[📖 Megoldás Dokumentáció](./solution/README.md)**

## 🎯 Teljes példák

Biztosítottunk teljes, működő kliens megvalósításokat minden programozási nyelvhez, amelyek ebben az oktatóanyagban szerepelnek. Ezek a példák bemutatják az összes fent leírt funkció működését, és használhatók referenciaként vagy kiindulópontként a saját projektjeidhez.

### Elérhető teljes példák

| Nyelv | Fájl | Leírás |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Teljes Java kliens SSE transzporttal, átfogó hibakezeléssel |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Teljes C# kliens stdio transzporttal, automatikus szerver indítással |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Teljes TypeScript kliens teljes MCP protokoll támogatással |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Teljes Python kliens async/await mintákkal |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Teljes Rust kliens Tokio async műveletekkel |

Minden teljes példa tartalmazza:
- ✅ **Kapcsolat létrehozása** és hibakezelés
- ✅ **Szerver keresése** (eszközök, források, promptok, ahol alkalmazható)
- ✅ **Számológép műveletek** (összeadás, kivonás, szorzás, osztás, segítség)
- ✅ **Eredmény feldolgozása** és formázott kimenet
- ✅ **Átfogó hibakezelés**
- ✅ **Tiszta, dokumentált kód** lépésenkénti kommentárokkal

### Kezdés teljes példákkal

1. **Válassza ki a kívánt nyelvet** a fenti táblázatból
2. **Tekintse át a teljes példafájlt** a teljes megvalósítás megértéséhez
3. **Futtassa a példát** az utasítások szerint a [`complete_examples.md`](./complete_examples.md) fájlban
4. **Módosítsa és bővítse** a példát a saját használati esetéhez

A példák futtatásával és testreszabásával kapcsolatos részletes dokumentációért lásd: **[📖 Teljes példák dokumentációja](./complete_examples.md)**

### 💡 Megoldás vs. Teljes példák

| **Megoldás mappa** | **Teljes példák** |
|--------------------|--------------------- |
| Teljes projektstruktúra build fájlokkal | Egyfájlos megvalósítások |
| Közvetlenül futtatható függőségekkel | Fókuszált kódpéldák |
| Termeléshez hasonló környezet | Oktatási hivatkozás |
| Nyelvspecifikus eszközök | Többnyelvű összehasonlítás |

Mindkét megközelítés értékes – használja a **megoldás mappát** teljes projektekhez, a **teljes példákat** pedig tanuláshoz és referenciához.

## Fő tanulságok

A fejezet fő tanulságai az ügyfelekről a következők:

- Használhatók a szerver funkcióinak felfedezésére és meghívására egyaránt.
- Elindíthatnak egy szervert önmaguk elindítása közben (ahogy ebben a fejezetben), de az ügyfelek csatlakozhatnak már futó szerverekhez is.
- Kiváló módja a szerver képességeinek tesztelésére az Inspectorhoz hasonló alternatívák mellett, amint azt az előző fejezet leírta.

## További források

- [Ügyfelek építése az MCP-ben](https://modelcontextprotocol.io/quickstart/client)

## Minták

- [Java számológép](../samples/java/calculator/README.md)
- [.Net számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript számológép](../samples/javascript/README.md)
- [TypeScript számológép](../samples/typescript/README.md)
- [Python számológép](../../../../03-GettingStarted/samples/python)
- [Rust számológép](../../../../03-GettingStarted/samples/rust)

## Mi következik

- Következő: [Ügyfél létrehozása LLM-mel](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével került lefordításra. Bár igyekszünk pontosan fordítani, kérjük, vegye figyelembe, hogy az automatikus fordítás hibákat vagy pontatlanságokat tartalmazhat. Az eredeti, anyanyelvi dokumentum tekintendő hiteles forrásnak. Kritikus jelentőségű információk esetén szakmai, emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
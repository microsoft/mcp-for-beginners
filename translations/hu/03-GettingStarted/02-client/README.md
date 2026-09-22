# Egy kliens létrehozása

A kliensek egyedi alkalmazások vagy szkriptek, amelyek közvetlenül kommunikálnak egy MCP szerverrel források, eszközök és promptok lekérése érdekében. Az inspector eszköz használatával ellentétben, amely grafikus felületet biztosít a szerverrel való interakcióhoz, a saját kliens megírása programozott és automatizált interakciókat tesz lehetővé. Ez lehetővé teszi a fejlesztők számára, hogy integrálják az MCP képességeit saját munkafolyamataikba, automatizálják a feladatokat, és egyedi megoldásokat építsenek konkrét igényekre szabva.

## Áttekintés

Ez a lecke bemutatja a kliensek fogalmát a Model Context Protocol (MCP) ökoszisztémában. Megtanulod, hogyan írhatod meg saját klienseidet, és hogyan csatlakoztathatod őket egy MCP szerverhez.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni, hogy mire képes egy kliens.
- Megírni a saját klienst.
- Csatlakoztatni és tesztelni a klienst egy MCP szerverrel, hogy megbizonyosodj róla, hogy az megfelelően működik.

## Mi szükséges egy kliens megírásához?

Egy kliens megírásához a következőkre lesz szükséged:

- **A megfelelő könyvtárak importálása.** Ugyanazt a könyvtárat fogod használni, mint korábban, csak más konstrukciókkal.
- **Kliens példányosítása.** Ez magában foglalja egy kliens példány létrehozását és a kiválasztott átvitelhez való csatlakoztatását.
- **Dönteni arról, hogy milyen erőforrásokat sorolj fel.** Az MCP szervered rendelkezik forrásokkal, eszközökkel és promptokkal, döntened kell, melyiket listázod.
- **Integrálni a klienst egy hoszt alkalmazásba.** Miután ismered a szerver képességeit, integrálnod kell ezt a hoszt alkalmazásodba, hogy ha egy felhasználó promptot vagy más parancsot ír be, a megfelelő szerver funkció meghívásra kerüljön.

Most, hogy nagy vonalakban értjük, mit fogunk csinálni, nézzünk egy példát.

### Egy példa kliens

Nézzük meg ezt a példát:

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

// Listázza a kéréseket
const prompts = await client.listPrompts();

// Kérjen egy promptot
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listázza az erőforrásokat
const resources = await client.listResources();

// Olvasson el egy erőforrást
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Hívjon meg egy eszközt
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

A fenti kódban:

- Importáltuk a könyvtárakat
- Létrehoztunk egy kliens példányt és csatlakoztattuk stdio átvitel használatával.
- Listáztuk a promptokat, forrásokat és eszközöket és mindegyiket meghívtuk.

Így tehát van egy kliensünk, mely képes kommunikálni egy MCP szerverrel.

A következő feladatban szánjunk időt arra, hogy bontsuk le minden kódrészletet és magyarázzuk el, mi történik.

## Gyakorlat: kliens írása

Ahogy fentebb említettük, szánjunk időt a kód magyarázatára, és természetesen kódoljunk együtt, ha szeretnéd.

### -1- Könyvtárak importálása

Importáljuk a szükséges könyvtárakat, szükségünk lesz hivatkozásokra a kliensre és a kiválasztott átvitel protokollra, a stdio-ra. A stdio egy helyi gépen futtatandó dolgokhoz való protokoll. Az SSE egy másik átvitel protokoll, amit a későbbi fejezetekben mutatunk be, az is egy lehetőség. Egyelőre folytassuk a stdio-val.

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

Java esetén olyan klienst kell létrehoznod, amely az előző feladatban lévő MCP szerverhez csatlakozik. A [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) fejezetben használt Java Spring Boot projekt struktúrát használva hozz létre egy új Java osztályt `SDKClient` néven a `src/main/java/com/microsoft/mcp/sample/client/` mappában, és add hozzá a következő importokat:

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

Ezután importálhatod a szükséges könyvtárakat a kliens kódodba.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Térjünk át a példányosításra.

### -2- Kliens és átvitel példányosítása

Létre kell hoznunk az átvitel és a kliens példányát:

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

Az előző kódban:

- Létrehoztunk egy stdio átvitel példányt. Vegyük észre, hogy megadja a command és args paramétereket a szerver megtalálásához és elindításához, mivel ezt meg kell tennünk a kliens létrehozásakor.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Létrehoztunk egy klienst a nevével és verziójával.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Csatlakoztattuk a klienst a kiválasztott átvitelhez.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Szerver paraméterek létrehozása stdio kapcsolathoz
server_params = StdioServerParameters(
    command="mcp",  # Futtatható állomány
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

Az előző kódban:

- Importáltuk a szükséges könyvtárakat.
- Létrehoztunk egy szerver paraméter objektumot, amelyet a szerver futtatásához fogunk használni, hogy a kliens csatlakozni tudjon hozzá.
- Meghatároztunk egy `run` metódust, amely meghívja a `stdio_client`-et, amely elindítja a kliens munkamenetet.
- Létrehoztunk egy belépési pontot, ahol az `asyncio.run`-nak adjuk át a `run` metódust.

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

Az előző kódban:

- Importáltuk a szükséges könyvtárakat.
- Létrehoztunk egy stdio átvitel példányt és egy `mcpClient` nevezetű klienst. Ezt majd a szerver funkcióinak listázására és meghívására használjuk.

Megjegyzés: az "Arguments" mezőben vagy a *.csproj* fájlra, vagy a futtatható állományra mutathatsz.

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
        
        // Ide kerül az ügyfél logikád
    }
}
```

Az előző kódban:

- Létrehoztunk egy fő metódust, amely egy SSE átvitel példányt állít be, amely a `http://localhost:8080` címet célozza meg, ahol a MCP szerver futni fog.
- Létrehoztunk egy kliens osztályt, amely konstruktor paraméterként megkapja az átvitel példányt.
- A `run` metódusban egy szinkron MCP klienst hozunk létre az átvitel használatával és inicializáljuk a kapcsolatot.
- SSE (Server-Sent Events) átvitel protokollt használtunk, amely HTTP-alapú kommunikációhoz alkalmas Java Spring Boot MCP szerverekkel.

#### Rust

Ez a Rust kliens feltételezi, hogy a szerver egy "calculator-server" nevű testvérprojekt ugyanabban a könyvtárban. Az alábbi kód elindítja a szervert és csatlakozik hozzá.

```rust
async fn main() -> Result<(), RmcpError> {
    // Tegyük fel, hogy a szerver egy testvérprojekt, amely "calculator-server" néven található ugyanabban a könyvtárban
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

    // TODO: Hívja meg az add eszközt az argumentumokkal = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- A szerver funkcióinak listázása

Most már van egy kliensünk, amely csatlakozni tud, ha a program fut. Azonban nem listázza a funkcióit, ezért ezt most pótoljuk:

#### TypeScript

```typescript
// Lista a promptokról
const prompts = await client.listPrompts();

// Listázza az erőforrásokat
const resources = await client.listResources();

// Lista az eszközökről
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

Itt listázzuk az elérhető forrásokat, `list_resources()` és az eszközöket, `list_tools`, majd kiírjuk őket.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Fent egy példa arra, hogyan listázhatjuk az eszközöket a szerveren. Minden eszköz nevét ki is írjuk.

#### Java

```java
// Eszközök listázása és bemutatása
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// A kapcsolat ellenőrzéséhez pingelheti is a szervert
client.ping();
```

Az előző kódban:

- Meghívtuk a `listTools()` metódust az összes elérhető eszköz lekéréséhez az MCP szervertől.
- A `ping()` használatával ellenőriztük a szerverhez való kapcsolat működését.
- A `ListToolsResult` tartalmazza az eszközök információit, köztük nevüket, leírásukat és bemeneti sémáikat.

Kiváló, most már megvannak az összes funkció adatai. De mikor használjuk őket? Ez a kliens elég egyszerű, abban az értelemben, hogy explicit módon kell meghívni a funkciókat, amikor szükség van rájuk. A következő fejezetben egy fejlettebb klienst hozunk létre, amely saját nagy nyelvi modellel (LLM) rendelkezik. Egyelőre nézzük meg, hogyan hívhatjuk meg a szerver funkcióit:

#### Rust

A main függvényben, a kliens inicializálása után inicializálhatjuk a szervert és listázhatjuk néhány funkcióját.

```rust
// Inicializálás
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Eszközök listázása
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funkciók meghívása

A funkciók meghívásához meg kell adnunk a megfelelő argumentumokat, és néhány esetben annak a nevét, amit meg akarunk hívni.

#### TypeScript

```typescript

// Erőforrás beolvasása
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

// Parancs hívása
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Az előző kódban:

- Elolvastunk egy forrást, a `readResource()` metódust meghívva, megadva a `uri`-t. Íme, hogyan néz ki ez valószínűleg a szerver oldalon:

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

    Az `uri` értékünk `file://example.txt`, amely illeszkedik a szerveren található `file://{name}`-hez. Így az `example.txt` a `name`-hez lesz társítva.

- Meghívtunk egy eszközt, megadva a nevét (`name`) és a paramétereit (`arguments`) így:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Lekértünk egy promptot a `getPrompt()` meghívásával, megadva a `name`-t és az `arguments`-ot. A szerver kód így néz ki:

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

    Ezért a kliensed kódja, hogy igazodjon a szerveren deklarálthoz, így fog kinézni:

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
# Erőforrás beolvasása
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Eszköz meghívása
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Az előző kódban:

- Meghívtunk egy `greeting` nevű forrást a `read_resource` segítségével.
- Meghívtunk egy `add` nevű eszközt a `call_tool` használatával.

#### .NET

1. Adjunk hozzá kódot egy eszköz meghívásához:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Eredmény kiíratásához a következő kódot használhatjuk:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Különféle számológép eszközök hívása
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

Az előző kódban:

- Többször hívott kalkulátor eszközöket a `callTool()` metódussal, `CallToolRequest` objektumok segítségével.
- Minden eszköz hívás megadja az eszköz nevét és egy argumentumok `Map`-jét, amelyet az eszköz igényel.
- A szerver eszközök specifikus paraméterneveket várnak (például "a", "b" matematikai műveletekhez).
- Az eredmények `CallToolResult` objektumokban érkeznek vissza, amelyek tartalmazzák a szerver válaszát.

#### Rust

```rust
// Hívja az add eszközt az argumentumokkal = {"a": 3, "b": 2}
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

### -5- A kliens futtatása

A kliens futtatásához írd be a következő parancsot a terminálba:

#### TypeScript

Add hozzá a következő bejegyzést a *package.json* "scripts" szekciójához:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Futtasd a klienst a következő paranccsal:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Először győződj meg róla, hogy az MCP szerver fut a `http://localhost:8080` címen. Ezután futtasd a klienst:

```bash
# Építsd meg a projektedet
./mvnw clean compile

# Futtasd az ügyfelet
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternatívaként futtathatod a teljes kliens projektet, amely megtalálható a `03-GettingStarted\02-client\solution\java` megoldás mappában:

```bash
# Navigáljon a megoldás könyvtárába
cd 03-GettingStarted/02-client/solution/java

# Fordítsa le és futtassa a JAR-t
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Feladat

Ebben a feladatban az eddig tanultakat alkalmazva egy saját klienst írsz.

Íme egy szerver, amelyet használhatsz, amelyet a kliensedből kell meghívni, nézd meg, tudsz-e több funkciót hozzáadni a szerverhez, hogy érdekesebb legyen.

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

// Kezdje meg az üzenetek fogadását a stdin-en és az üzenetek küldését a stdout-on

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

# Hozzon létre egy MCP szervert
mcp = FastMCP("Demo")


# Adjon hozzá egy összeadási eszközt
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Adjon hozzá egy dinamikus üdvözlő erőforrást
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

Nézd meg ezt a projektet, hogy megtudd, hogyan adhatsz hozzá [promptokat és forrásokat](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Továbbá, nézd meg ezt a linket, hogy hogyan hívhatsz meg [promptokat és forrásokat](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

A [korábbi szakaszban](../../../../03-GettingStarted/01-first-server) megtanultad, hogyan készíts egyszerű MCP szervert Rust nyelven. Folytathatod ennek fejlesztését, vagy nézd meg ezt a linket további Rust alapú MCP szerver példákért: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Megoldás

A **megoldás mappa** komplett, azonnal futtatható kliens implementációkat tartalmaz, amelyek bemutatják a tutorialban tárgyalt összes koncepciót. Minden megoldás külön kliens és szerver kódot tartalmaz, elkülönített, önálló projektekként.

### 📁 Megoldás struktúrája

A megoldás könyvtár nyelvenként szervezett:

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

### 🚀 Mit tartalmaz minden megoldás

Minden nyelvspecifikus megoldás:

- **Teljes kliens megvalósítás** az összes tutorialban tárgyalt funkcióval
- **Működő projektstruktúra** a megfelelő függőségekkel és konfigurációval
- **Build és futtató skriptek** a könnyű beállításhoz és futtatáshoz
- **Részletes README** nyelvspecifikus útmutatókkal
- **Hibakezelési és eredményfeldolgozási példák**

### 📖 A megoldások használata

1. **Navigálj a választott programozási nyelv mappájába**:

   ```bash
   cd solution/typescript/    # TypeScripthez
   cd solution/java/          # Javához
   cd solution/python/        # Pythonhoz
   cd solution/dotnet/        # .NET-hez
   ```

2. **Kövessd a README utasításait** minden mappában a következőkért:
   - Függőségek telepítése
   - Projekt buildelése
   - A kliens futtatása

3. **Egy példa kimenet**, amit látnod kell:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Teljes dokumentációért és lépésről-lépésre útmutatókért lásd: **[📖 Megoldás dokumentáció](./solution/README.md)**

## 🎯 Komplett példák

Komplett, működő kliens implementációkat biztosítottunk az összes tutorialban tárgyalt programozási nyelvhez. Ezek a példák bemutatják a teljes fent leírt funkcionalitást, és referencia implementációként vagy kiindulópontként használhatók saját projektjeidhez.

### Elérhető komplett példák

| Nyelv | Fájl | Leírás |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Teljes Java kliens SSE átvitel használatával, átfogó hibakezeléssel |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Teljes C# kliens stdio átvitel használatával, automatikus szerverindítással |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Teljes TypeScript kliens az MCP protokoll teljes támogatásával |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Teljes Python kliens async/await mintákkal |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Teljes Rust kliens Tokio aszinkron műveletekhez |

Minden komplett példa tartalmazza:

- ✅ **Kapcsolódás és hibakezelés**
- ✅ **Szerver felfedezés** (eszközök, források, promptok ahol alkalmazható)
- ✅ **Számológép műveletek** (összeadás, kivonás, szorzás, osztás, segédlet)
- ✅ **Eredmény feldolgozás** és formázott kimenet
- ✅ **Átfogó hibakezelés**

- ✅ **Tiszta, dokumentált kód** lépésről lépésre szóló megjegyzésekkel

### Kezdés teljes példákkal

1. **Válaszd ki a preferált nyelvedet** a fenti táblázatból
2. **Nézd át a teljes példafájlt** a teljes megvalósítás megértéséhez
3. **Futtasd a példát** az utasítások szerint a [`complete_examples.md`](./complete_examples.md) fájlban
4. **Módosítsd és bővítsd** a példát a saját felhasználási esethez

A példák futtatásáról és testreszabásáról részletes dokumentáció található: **[📖 Teljes példák dokumentációja](./complete_examples.md)**

### 💡 Megoldás vs. Teljes példák

| **Megoldás mappa** | **Teljes példák** |
|--------------------|--------------------- |
| Teljes projekt struktúra build fájlokkal | Egyfájlos megvalósítások |
| Kész a futtatásra függőségekkel | Fókuszált kódpéldák |
| Produkciószerű beállítás | Oktatási referencia |
| Nyelv specifikus eszközök | Nyelvek közötti összehasonlítás |

Mindkét megközelítés értékes – használjuk a **megoldás mappát** teljes projektekhez, és a **teljes példákat** tanulásra és referenciaként.

## Fő tanulságok

Ennek a fejezetnek a fő tanulságai az ügyfelekről a következők:

- Használhatók a kiszolgáló funkcióinak felfedezésére és meghívására egyaránt.
- Elindíthatnak egy szervert miközben maguk is elindulnak (ahogy ebben a fejezetben), de az ügyfelek csatlakozhatnak már futó szerverekhez is.
- Nagyszerű módja a szerver képességek kipróbálásának más lehetőségek mellett, mint például az Inspector, amint azt az előző fejezet ismertette.

## További források

- [Ügyfelek építése MCP-ben](https://modelcontextprotocol.io/quickstart/client)

## Minták

- [Java Számológép](../samples/java/calculator/README.md)
- [.NET Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)
- [Rust Számológép](../../../../03-GettingStarted/samples/rust)

## Mi következik

- Következő: [Ügyfél létrehozása LLM-mel](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
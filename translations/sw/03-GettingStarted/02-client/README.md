# Kutengeneza mteja

Wateja ni programu maalum au maandishi yanayozungumza moja kwa moja na MCP Server kuomba rasilimali, zana, na maagizo. Tofauti na kutumia zana ya mchunguzi, ambayo hutoa kiolesura cha picha kwa ajili ya kuingiliana na seva, kuandika mteja wako mwenyewe huruhusu mwingiliano wa programu na otomatiki. Hii inawawezesha waendelezaji kuunganisha uwezo wa MCP katika kazi zao wenyewe, kuendesha kazi kwa otomatiki, na kujenga suluhisho maalum zilizobinafsishwa kulingana na mahitaji maalum.

## Muhtasari

Somo hili linaletwa wazo la wateja ndani ya mfumo wa Model Context Protocol (MCP). Utajifunza jinsi ya kuandika mteja wako mwenyewe na kumfanya aungane na MCP Server.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa kile mteja anaweza kufanya.
- Kuandika mteja wako mwenyewe.
- Kuunganisha na kujaribu mteja na seva ya MCP kuhakikisha inafanya kazi kama inavyotarajiwa.

## Nini kinahitajika kuandika mteja?

Ili kuandika mteja, utahitaji kufanya yafuatayo:

- **Leta maktaba sahihi**. Utatumia maktaba ile ile kama kabla, tu miundo tofauti.
- **Tengeneza mfano wa mteja**. Hii itahusisha kuunda mfano wa mteja na kuunganisha kwa njia ya usafirishaji uliyochaguliwa.
- **Amua rasilimali gani kutazama**. Seva yako ya MCP ina rasilimali, zana na maagizo, unahitaji kuamua ipi utaorodhesha.
- **Unganisha mteja na programu mwenyeji**. Mara ukijua uwezo wa seva, unahitaji kuunganisha hili na programu yako mwenyeji ili endapo mtumiaji ataandika agizo au sehemu nyingine ya amri, kipengele kinacholingana cha seva kiitwe.

Sasa tunapoelewa kwa ujumla kile tunachotaka kufanya, tuchukulie mfano ufuatao.

### Mfano wa mteja

Tuchukulie mfano huu wa mteja:

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

// Orodhesha maagizo
const prompts = await client.listPrompts();

// Pata agizo
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Orodhesha rasilimali
const resources = await client.listResources();

// Soma rasilimali
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Piga simu zana
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Katika msimbo ulio hapo juu tumefanya:

- Leta maktaba
- Tengeneza mfano wa mteja na kuunganisha kwa kutumia stdio kama njia ya usafirishaji.
- Orodhesha maagizo, rasilimali na zana na kuyaitisha yote.

Hivyo ndivyo, mteja anaweza kuzungumza na MCP Server.

Tuchukulie kwa makini sehemu ya mazoezi na kueleza kipande cha msimbo kila mara kinachotokea.

## Zoekezaji: Kuandika mteja

Kama ilivyosemwa hapo juu, tuchukue muda kueleza msimbo, na kwa kila njia andika ikiwa unataka.

### -1- Leta maktaba

Tuzilete maktaba tunazohitaji, tutahitaji marejeleo ya mteja na itifaki yetu ya usafirishaji tuliyochagua, stdio. stdio ni itifaki ya vitu vinavyotarajiwa kuendeshwa kwenye mashine yako ya karibu. SSE ni itifaki nyingine ya usafirishaji tutakayoonyesha katika sura zijazo lakini hiyo ni chaguo lako lingine. Kwa sasa, tukae na stdio.

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

Kwa Java, utaunda mteja anayehusiana na MCP server kutoka zoezi la awali. Ukitumia muundo ule ule wa mradi wa Java Spring Boot kutoka [Anza na MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), tengeneza darasa jipya la Java linaloitwa `SDKClient` katika folda `src/main/java/com/microsoft/mcp/sample/client/` na ongeza imports zifuatazo:

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

Utahitaji kuongeza utegemezi ufuatao kwenye faili lako `Cargo.toml`.

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

Kutoka hapo, utaweza kuleta maktaba zinazohitajika katika msimbo wa mteja wako.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Tuchukulie sasa kuanzisha.

### -2- Kuanzisha mteja na usafirishaji

Tutahitaji kuunda mfano wa usafirishaji na wa mteja wetu:

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

Katika msimbo uliotangulia tumefanya:

- Tumeunda mfano wa usafirishaji wa stdio. Angalia jinsi inavyoelezea amri na mijadala ya jinsi ya kupata na kuanzisha seva kwani hii ni kitu tutakachohitaji tufanye tunapoanzisha mteja.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Tumeanzisha mteja kwa kumpa jina na toleo.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Tumeunganisha mteja na usafirishaji ulioteuliwa.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vigezo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezeka
    args=["run", "server.py"],  # Hoja za hiari za mstari wa amri
    env=None,  # Mazingira ya hiari ya kandarasi
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Anzisha muunganisho
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Katika msimbo uliotangulia tumefanya:

- Leta maktaba zinazohitajika
- Tengeneza kitu cha vigezo vya seva kwani tutakitumia kuendesha seva ili kuungana nayo na mteja wetu.
- Fafanua njia `run` ambayo inaita `stdio_client` ambayo huanzisha kikao cha mteja.
- Tengeneza sehemu ya kuingia ambapo tunatoa njia `run` kwa `asyncio.run`.

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

Katika msimbo uliotangulia tumefanya:

- Leta maktaba zinazohitajika.
- Tunga usafirishaji wa stdio na uunde mteja `mcpClient`. Huu ni kitu tutakachotumia kuorodhesha na kuitisha vipengele kwenye MCP Server.

Kumbuka, katika "Arguments", unaweza kumwelekeza kwenye *.csproj* au kwenye program inayotekelezeka.

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
        
        // Mantiki ya mteja wako inaweza kuwekwa hapa
    }
}
```

Katika msimbo uliotangulia tumefanya:

- Tumeunda njia kuu inayoweka usafirishaji SSE unaoelekeza kwenye `http://localhost:8080` ambapo MCP server itakuwa ikiendesha.
- Tumeunda darasa la mteja linalochukua usafirishaji kama kiparameteri cha muunda.
- Katika njia `run`, tumeunda mteja wa MCP wa muunganiko kwa kutumia usafirishaji na kuanzisha muunganisho.
- Tumetumia usafirishaji wa SSE (Server-Sent Events) unaofaa kwa mawasiliano ya HTTP na MCP servers za Java Spring Boot.

#### Rust

Kumbuka mteja huyu wa Rust anadhani seva ni mradi wa ndugu unaoitwa "calculator-server" katika saraka ile ile. Msimbo hapo chini utaanzisha seva na kuungana nayo.

```rust
async fn main() -> Result<(), RmcpError> {
    // Kubali kuwa seva ni mradi wa kaka uitwao "calculator-server" katika saraka moja
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

    // TODO: Anzisha

    // TODO: Orodhesha zana

    // TODO: Piga simu kuongeza zana kwa hoja = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Kurodha vipengele vya seva

Sasa, tuna mteja anaweza kuungana endapo programu itaendeshwa. Hata hivyo, haorodheshi vipengele vyake sasa, tuchukulie hivyo sasa:

#### TypeScript

```typescript
// Orodhesha vichocheo
const prompts = await client.listPrompts();

// Orodhesha rasilimali
const resources = await client.listResources();

// orodha ya zana
const tools = await client.listTools();
```

#### Python

```python
# Orodhesha rasilimali zinazopatikana
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Orodhesha zana zinazopatikana
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Hapa tunataja rasilimali zilizopo, `list_resources()` na zana, `list_tools` na kuziandika.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Hapo juu ni mfano wa jinsi tunavyoweza kuorodhesha zana za seva. Kwa kila zana, tunachapisha jina lake.

#### Java

```java
// Orodhesha na kuonyesha zana
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Pia unaweza kutuma ping kwa seva kuthibitisha muunganisho
client.ping();
```

Katika msimbo uliotangulia tumefanya:

- Imetaja `listTools()` kupata zana zote zinazopatikana kutoka kwa MCP server.
- Imetumia `ping()` kuthibitisha kuwa muunganisho na seva unafanya kazi.
- `ListToolsResult` ina taarifa kuhusu zana zote ikiwemo majina yao, maelezo, na vipimo vya ingizo.

Vizuri, sasa tumehifadhi vipengele vyote. Sasa swali ni lini tunavitumia? Haya, mteja huyu ni rahisi sana, rahisi kwa maana tunahitaji kupiga simu kwa vipengele vilipowekwa. Katika sura inayofuata, tutaunda mteja zaidi wa hali ya juu ambaye ana ufikiaji wa mfano wa lugha mkubwa wake, LLM. Kwa sasa tuone jinsi ya kuaitisha vipengele kwenye seva:

#### Rust

Katika func main, baada ya kuanzisha mteja, tunaweza kuanzisha seva na kuorodhesha baadhi ya vipengele vyake.

```rust
// Anzisha
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Orodhesha zana
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Kuitisha vipengele

Ili kuitisha vipengele tunahitaji kuhakikisha tumeelezea hoja sahihi na kwa baadhi ya kesi jina la kile tunachojaribu kuitisha.

#### TypeScript

```typescript

// Soma rasilimali
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Piga simu kwa chombo
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// piga simu kwa taarifa
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Katika msimbo uliotangulia tumefanya:

- Kusoma rasilimali, tunaita rasilimali kwa kutumia `readResource()` tukielezea `uri`. Hapa huenda ikawa inavyoonekana upande wa seva:

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

    Thamani yetu ya `uri` `file://example.txt` inalingana na `file://{name}` kwenye seva. `example.txt` itahusishwa na `name`.

- Kuitisha zana, tunaiita kwa kuelezea jina lake `name` na `arguments` kama ifuatavyo:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Kupata agizo, ili kupata agizo, unaiga `getPrompt()` na `name` na `arguments`. Msimbo wa seva unaonekana kama ifuatavyo:

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

    na msimbo wa mteja utakavyoonekana utakubaliana na kile kilichotangazwa kwenye seva:

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
# Soma rasilimali
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Piga zana
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Katika msimbo uliotangulia, tumefanya:

- Kuitisha rasilimali inayoitwa `greeting` kwa kutumia `read_resource`.
- Kuitisha zana iitwayo `add` kwa kutumia `call_tool`.

#### .NET

1. Tongeze msimbo wa kuitisha zana:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Ili kuchapisha matokeo, hapa kuna msimbo wa kushughulikia hiyo:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Piga huduma mbalimbali za kalukuleta
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

Katika msimbo uliotangulia tumefanya:

- Kuitisha zana nyingi za calculator kwa kutumia njia `callTool()` na vitu vya `CallToolRequest`.
- Kila simu ya zana inaonyesha jina la zana na ramani ya hoja zinazohitajika na zana hiyo.
- Zana za seva zinahitaji majina maalum ya vigezo (kama "a", "b" kwa operesheni za hisabati).
- Matokeo huletwa kama vitu vya `CallToolResult` vinavyozidiwa na majibu kutoka kwa seva.

#### Rust

```rust
// Piga simu zana ya kuongeza na hoja = {"a": 3, "b": 2}
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

### -5- Endesha mteja

Kuendesha mteja, andika amri ifuatayo kwenye terminal:

#### TypeScript

Ongeza kipengele ifuatavyo kwenye sehemu ya "scripts" katika *package.json* yako:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Ita mteja kwa amri ifuatayo:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Kwanza, hakikisha MCP server yako inakimbia kwenye `http://localhost:8080`. Kisha endesha mteja:

```bash
# Jenga mradi wako
./mvnw clean compile

# Endesha mteja
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Vinginevyo, unaweza kuendesha mradi kamili wa mteja uliopewa katika folda ya suluhisho `03-GettingStarted\02-client\solution\java`:

```bash
# Elekea kwenye saraka ya suluhisho
cd 03-GettingStarted/02-client/solution/java

# Tengeneza na endesha JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Kazi ya Nyumbani

Katika kazi hii ya nyumbani, utatumia kile ulichojifunza katika kutengeneza mteja lakini utatengeneza mteja wako mwenyewe.

Huyu ni seva unayoweza kutumia unayohitaji kuitisha kupitia msimbo wa mteja wako, tazama ikiwa unaweza kuongeza vipengele zaidi kwenye seva kufanya iwe ya kuvutia zaidi.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Tengeneza seva ya MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Ongeza chombo cha ongezeko
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Ongeza rasilimali ya salamu inayobadilika
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

// Anza kupokea ujumbe kwenye stdin na kutuma ujumbe kwenye stdout

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

# Tengeneza seva ya MCP
mcp = FastMCP("Demo")


# Ongeza chombo cha kuongeza
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Ongeza rasilimali ya salamu yenye mabadiliko
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

Tazama mradi huu kuona jinsi ya [kuongeza maagizo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Pia, angalia kiungo hiki kwa jinsi ya kuitisha [maagizo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Katika [sehemu iliyopita](../../../../03-GettingStarted/01-first-server), ulijifunza jinsi ya kutengeneza seva rahisi ya MCP kwa Rust. Unaweza kuendelea kujenga hapo au angalia kiungo hiki kwa mifano zaidi ya seva za MCP zenye msingi wa Rust: [Mfano za MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Suluhisho

**Folda ya suluhisho** ina utekelezaji kamili wa wateja wa programu, tayari kuendeshwa unaoonyesha dhana zote zilizojadiliwa katika mafunzo haya. Kila suluhisho lina msimbo wa mteja na seva umeandaliwa katika miradi ya kujitegemea.

### 📁 Muundo wa Suluhisho

Saraka ya suluhisho imeandaliwa kwa lugha za programu:

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

### 🚀 Kila Suluhisho Linajumuisha Nini

Kila suluhisho la lugha maalum linatoa:

- **Utekelezaji kamili wa mteja** wenye vipengele vyote kutoka mafunzoni
- **Muundo wa mradi unaofanya kazi** na utegemezi sahihi na usanidi
- **Skripti za kujenga na kuendesha** kwa urahisi wa usanidi na utekelezaji
- **README ya kina** yenye maelekezo ya lugha husika
- **Mifano ya usindikaji wa makosa** na matokeo

### 📖 Kutumia Suluhisho

1. **Elekea saraka ya lugha unayopendelea**:

   ```bash
   cd solution/typescript/    # Kwa TypeScript
   cd solution/java/          # Kwa Java
   cd solution/python/        # Kwa Python
   cd solution/dotnet/        # Kwa .NET
   ```

2. **Fuata maelekezo ya README** katika kila saraka kwa:
   - Kusakinisha utegemezi
   - Kujenga mradi
   - Kuendesha mteja

3. **Matokeo mfano** unayopaswa kuona:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Kwa nyaraka kamili na maelekezo ya hatua kwa hatua, tazama: **[📖 Nyaraka za Suluhisho](./solution/README.md)**

## 🎯 Mifano Kamili

Tumetoa utekelezaji kamili, wa kazi kwa wateja wa lugha zote za programu zilizofunikwa katika mafunzo haya. Mifano hii inaonyesha utendakazi kamili ulioelezwa hapo juu na inaweza kutumika kama marejeleo au kuanzia mradi wako.

### Mifano Kamili Inayopatikana

| Lugha | Faili | Maelezo |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Mteja kamili wa Java akitumia usafirishaji wa SSE na usindikaji wa makosa kwa kina |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Mteja kamili wa C# akitumia usafirishaji wa stdio na kuanzisha seva moja kwa moja |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Mteja kamili wa TypeScript mwenye msaada wa itifaki ya MCP kikamilifu |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Mteja kamili wa Python akitumia mifumo ya async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Mteja kamili wa Rust akitumia Tokio kwa operesheni za async |

Kila mfano kamili unajumuisha:

- ✅ **Kuanza muunganisho** na usindikaji wa makosa
- ✅ **Ugonjwa wa seva** (zana, rasilimali, maagizo pale inapowezekana)
- ✅ **Operesheni za calculator** (ongeza, toa, zidisha, gawanya, msaada)
- ✅ **Usindikaji wa matokeo** na maonyesho yaliyopangwa
- ✅ **Usindikaji wa makosa kwa kina**

- ✅ **Kanuni safi, zilizobainishwa** zilizo na maelezo hatua kwa hatua

### Kuanzia na Mifano Kamili

1. **Chagua lugha unayopendelea** kutoka kwenye jedwali hapo juu
2. **Pitia faili la mfano kamili** kuelewa utekelezaji kamili
3. **Endesha mfano** kufuata maelekezo katika [`complete_examples.md`](./complete_examples.md)
4. **Badilisha na ongeza** mfano kwa matumizi yako maalum

Kwa maelezo ya kina kuhusu kuendesha na kubadilisha mifano hii, angalia: **[📖 Nyaraka za Mifano Kamili](./complete_examples.md)**

### 💡 Suluhisho vs. Mifano Kamili

| **Folda ya Suluhisho** | **Mifano Kamili** |
|--------------------|--------------------- |
| Muundo kamili wa mradi na faili za kujenga | Utekelezaji wa faili moja |
| Tayari kuendesha na utegemezi | Mifano ya kanuni iliyo elekezwa |
| Mipangilio kama kwa uzalishaji | Marejeleo ya elimu |
| Vifaa maalum vya lugha | Mlinganisho wa lugha mbalimbali |

Mbinu zote mbili ni kuwa na thamani - tumia **folda ya suluhisho** kwa miradi kamili na **mifano kamili** kwa kujifunza na marejeleo.

## Muhimu Kukumbuka

Muhimu wa sura hii kuhusu wateja ni yafuatayo:

- Inaweza kutumika kugundua na kuitisha sifa kwenye seva.
- Inaweza kuanzisha seva wakati inavyoanzisha yenyewe (kama sura hii) lakini wateja pia wanaweza kuunganisha na seva zinazotumika.
- Ni njia bora ya kujaribu uwezo wa seva kando na mbadala kama Inspector kama ilivyoelezwa kwenye sura iliyopita.

## Rasilimali Zaidi

- [Kujenga wateja katika MCP](https://modelcontextprotocol.io/quickstart/client)

## Mifano

- [Kalkuleta ya Java](../samples/java/calculator/README.md)
- [Kalkuleta ya .NET](../../../../03-GettingStarted/samples/csharp)
- [Kalkuleta ya JavaScript](../samples/javascript/README.md)
- [Kalkuleta ya TypeScript](../samples/typescript/README.md)
- [Kalkuleta ya Python](../../../../03-GettingStarted/samples/python)
- [Kalkuleta ya Rust](../../../../03-GettingStarted/samples/rust)

## Kifuatavyo

- Kifuatavyo: [Kuunda mteja na LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
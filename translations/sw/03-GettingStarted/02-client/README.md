# Kuunda mteja

Wateja ni programu maalum au skiripti ambazo huwasiliana moja kwa moja na MCP Server kuomba rasilimali, zana, na maelekezo. Tofauti na kutumia chombo cha mtaalamu wa ukaguzi, ambacho hutoa kiolesura cha picha kwa kuingiliana na seva, kuandika mteja wako kunaruhusu mwingiliano wa programu kwa njia ya programu na otomatiki. Hii inawawezesha waendelezaji kuingiza uwezo wa MCP katika michakato yao ya kazi, kuendesha kazi kwa otomatiki, na kujenga suluhisho maalum zilizotengenezwa kwa mahitaji maalum.

## Muhtasari

Mafunzo haya yanaanzisha dhana ya wateja ndani ya mfumo wa Model Context Protocol (MCP). Utajifunza jinsi ya kuandika mteja wako mwenyewe na kuufanya uungane na MCP Server.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa kile mteja anaweza kufanya.
- Kuandika mteja wako mwenyewe.
- Kuunganisha na kujaribu mteja na seva ya MCP kuhakikisha kuwa seva inafanya kazi kama inavyotarajiwa.

## Nini kinaingia katika kuandika mteja?

Ili kuandika mteja, utahitaji kufanya mambo yafuatayo:

- **Ingiza maktaba sahihi**. Utatumia maktaba ile ile kama awali, tofauti ni mabadiliko ya miundo.
- **Tengeneza mteja**. Hii itahusisha kuunda mfano wa mteja na kuunganisha kwa njia ya usafirishaji uliyochagua.
- **Amua rasilimali gani zaorodheshe**. Seva yako ya MCP ina rasilimali, zana na maelekezo, unahitaji kuamua ipi yaorodheshwe.
- **Unganisha mteja kwenye programu mwenyeji**. Mara utakapojua uwezo wa seva, unahitaji kuunganisha hii kwenye programu yako mwenyeji ili kama mtumiaji ataandika maelekezo au amri nyingine, kipengele kinacholingana cha seva kitaitwa.

Sasa tukiwa tumeelewa kwa kiwango cha juu kile tutakachofanya, tuchunguze mfano unaofuata.

### Mfano wa mteja

Tazama mfano huu wa mteja:

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

// Orodha ya maelekezo
const prompts = await client.listPrompts();

// Pata maelekezo
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Orodha ya rasilimali
const resources = await client.listResources();

// Soma rasilimali
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Piga chombo
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Katika msimbo uliotangulia tulifanya:

- Kuingiza maktaba
- Kuunda mfano wa mteja na kuungana kwa kutumia stdio kama usafirishaji.
- Kuuorodhesha maelekezo, rasilimali na zana na kuzitumia zote.

Hapo una mteja anayeweza kuzungumza na MCP Server.

Tuchukue muda katika sehemu ya mazoezi ijayo na tufumue kila kipande cha msimbo na kuelezea kinachotokea.

## Mazoezi: Kuandika mteja

Kama ilivyoambia hapo juu, tuchukue muda kuelezea msimbo, na kwa njia yoyote andika msimbo ikiwa unataka.

### -1- Kuingiza maktaba

Tuingize maktaba tunazohitaji, tutahitaji marejeleo kwa mteja na kwa itifaki ya usafirishaji tuliyoichagua, stdio. stdio ni itifaki kwa ajili ya vitu vinavyopaswa kuendeshwa kwenye mashine yako ya ndani. SSE ni itifaki nyingine ya usafirishaji tutakayoonyesha katika sura zijazo lakini hiyo ni chaguo lako lingine. Kwa sasa, tuchukue stdio tu.

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

Kwa Java, utaunda mteja unaounganisha na MCP server kutoka kwa zoezi lililotangulia. Ukitumia muundo ule ule wa mradi wa Java Spring Boot kutoka [Kuanzia na MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), unda darasa jipya la Java lijulike kama `SDKClient` kwenye folda `src/main/java/com/microsoft/mcp/sample/client/` na ongeza maingizo yafuatayo:

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

Utahitaji kuongeza utegemezi ufuatao kwenye faili yako ya `Cargo.toml`.

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

Kutoka hapo, unaweza kuingiza maktaba zinazohitajika kwenye msimbo wa mteja wako.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Tuweke mbele kwa kuunda mfano.

### -2- Kuunda mfano wa mteja na usafirishaji

Tutahitaji kuunda mfano wa usafirishaji na vilevile wa mteja wetu:

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

Katika msimbo uliopita tumefanya:

- Kuunda mfano wa usafirishaji wa stdio. Angalia jinsi inavyoelezea amri na hoja (args) za jinsi ya kupata na kuanzisha seva kwani hili ni jambo tunalotakiwa kufanya tunapoanzisha mteja.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Kuanzisha mteja kwa kumpa jina na toleo.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Kuunganisha mteja kwenye usafirishaji uliyochaguliwa.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vipimo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezeka
    args=["run", "server.py"],  # Hoja za hiari za mstari wa amri
    env=None,  # Mabadiliko ya mazingira ya hiari
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

Katika msimbo uliopita tumefanya:

- Kuingiza maktaba zinazohitajika
- Kuunda kitu cha vigezo vya seva kama tutakavyotumia hili kuendesha seva ili tuweze kuungana nayo kwa mteja wetu.
- Kuweka njia `run` inayoiita `stdio_client` ambayo huanzisha kikao cha mteja.
- Kuunda sehemu ya kuingia ambapo tunapeana njia ya `run` kwa `asyncio.run`.

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

Katika msimbo uliopita tumefanya:

- Kuingiza maktaba zinazohitajika.
- Kuunda usafirishaji wa stdio na kuunda mteja `mcpClient`. Hii ni kitu ambacho tutatumia kuorodhesha na kuitisha vipengele kwenye MCP Server.

Kumbuka, katika "Arguments", unaweza kuonyesha kwa faili *.csproj* au kwenye faili linaloweza kutekelezwa.

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
        
        // Mantiki ya mteja wako inaenda hapa
    }
}
```

Katika msimbo uliopita tumefanya:

- Kuunda njia kuu (main method) ambayo inaweka usafirishaji wa SSE unaonena `http://localhost:8080` ambapo seva yetu ya MCP itakuwa ikifungua.
- Kuunda darasa la mteja linalopokea usafirishaji kama parameter kwenye konstrukta.
- Katika njia ya `run`, tunaunda mteja wa MCP katika njia ya sinkroni tukiitumia usafirishaji na kuanzisha muunganisho.
- Kutumia usafirishaji wa SSE (Server-Sent Events) unaofaa kwa mawasiliano ya HTTP na seva za MCP za Java Spring Boot.

#### Rust

Kumbuka mteja huyu wa Rust unadhani seva ni mradi wa jamaa aliyeitwa "calculator-server" katika saraka ile ile. Msimbo uliopo utaanzisha seva na kuungana nayo.

```rust
async fn main() -> Result<(), RmcpError> {
    // Kubaliana seva ni mradi wa ndugu unaoitwa "calculator-server" katika saraka sawa
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

    // KTK: Anzisha

    // KTK: Orodhesha zana

    // KTK: Piga simu ya kuongeza zana na hoja = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Kuorodhesha vipengele vya seva

Sasa tuna mteja anayeweza kuungana ikiwa programu itaendeshwa. Hata hivyo, haijaorodhesha vipengele vyake, basi hebu tufanye hivyo sasa:

#### TypeScript

```typescript
// Orodha ya maelekezo
const prompts = await client.listPrompts();

// Orodha ya rasilimali
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

Hapa tunaorodhesha rasilimali zilizopo, `list_resources()` na zana, `list_tools` na kuzichapisha.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Huu ni mfano wa jinsi tunavyoweza kuorodhesha zana kwenye seva. Kwa kila zana, tunachapisha jina lake.

#### Java

```java
// Orodhesha na onyesha zana
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Pia unaweza kutuma ping kwa seva kuthibitisha muunganisho
client.ping();
```

Katika msimbo uliopita tumefanya:

- Kuuita `listTools()` kupata zana zote zinazopatikana kutoka MCP server.
- Kutumia `ping()` kutathmini kuwa muunganisho na seva unafanya kazi.
- Matokeo ya `ListToolsResult` yanajumuisha taarifa kuhusu zana zote ikiwa ni pamoja na majina yao, maelezo, na mipangilio ya matumizi.

Nzuri, sasa tumekamata vipengele vyote. Sasa swali ni lini tunavitumia? Huyu mteja ni rahisi sana, rahisi kwa maana kwamba tutahitaji kuitisha vipengele hapo tunapotaka. Katika sura inayofuata, tutaunda mteja aliye na uwezo zaidi mwenye mtindo wake mkubwa wa lugha, LLM. Kwa sasa, tuchukulie jinsi ya kuitisha vipengele kwenye seva:

#### Rust

Katika kazi kuu (main function), baada ya kuanzisha mteja, tunaweza kuanzisha seva na kuorodhesha baadhi ya vipengele vyake.

```rust
// Anzisha
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Orodha ya zana
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Kuitisha vipengele

Ili kuitisha vipengele tunahitaji kuhakikisha tunabainisha hoja sahihi na katika baadhi ya kesi jina la kile tunachojaribu kuitisha.

#### TypeScript

```typescript

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

// piga simu kiagizo
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Katika msimbo uliopita tulifanya:

- Kusoma rasilimali, tunaita rasilimali kwa kuitisha `readResource()` tukibainisha `uri`. Hapa ni jinsi inavyoweza kuonekana upande wa seva:

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

- Kuitisha zana, tunaaita kwa kubainisha `name` na `arguments` kama ifuatavyo:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Kupata maelekezo, ili kupata maelekezo, unaita `getPrompt()` ukiipa `name` na `arguments`. Msimbo wa seva unaonekana kama:

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

    na msimbo wa mteja unaotokana naye unaonekana kama ifuatavyo ili ulingane na kile kilichotangazwa kwenye seva:

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

# Piga simu kwa chombo
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Katika msimbo uliopita, tumefanya:

- Kuita rasilimali iitwayo `greeting` kwa kutumia `read_resource`.
- Kuitisha zana iitwayo `add` kwa kutumia `call_tool`.

#### .NET

1. Tuweke msimbo wa kuita zana:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Ili kuchapisha matokeo, hapa kuna msimbo wa kushughulikia hayo:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Piga zana mbalimbali za kalkuleta
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

Katika msimbo uliopita tumefanya:

- Kuita zana mbalimbali za kihesabu kwa kutumia njia ya `callTool()` na vitu vya `CallToolRequest`.
- Kila wito wa zana unaainisha jina la zana na `Map` ya hoja zinazohitajika na zana hiyo.
- Zana za seva zinatarajia majina maalum ya vigezo (kama "a", "b" kwa hesabu).
- Matokeo yanarudishwa kama vitu vya `CallToolResult` vinavyoshikilia majibu kutoka kwa seva.

#### Rust

```rust
// Piga simu zana ya kuongeza kwa hoja = {"a": 3, "b": 2}
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

Ili kuendesha mteja, andika amri ifuatayo kwenye terminal:

#### TypeScript

Ongeza kipengele hiki kwenye sehemu ya "scripts" katika *package.json*:

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

Kwanza, hakikisha seva yako ya MCP inaendeshwa kwenye `http://localhost:8080`. Kisha endesha mteja:

```bash
# Jenga mradi wako
./mvnw clean compile

# Endesha mteja
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Kama mbadala, unaweza kuendesha mradi kamili wa mteja ulio kwenye folda ya suluhisho `03-GettingStarted\02-client\solution\java`:

```bash
# Elekea kwenye saraka ya suluhisho
cd 03-GettingStarted/02-client/solution/java

# Jenga na endesha JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Kazi ya nyumbani

Katika kazi hii ya nyumbani, utatumia kile ulichojifunza kuunda mteja lakini unda mteja wako mwenyewe.

Huu ni seva unayotumia ambayo unahitaji kuiitisha kupitia msimbo wa mteja wako, angalia kama unaweza kuongeza vipengele zaidi kwa seva kufanya iwe ya kuvutia zaidi.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Unda seva ya MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Ongeza zana ya kuongeza
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

# Unda seva ya MCP
mcp = FastMCP("Demo")


# Ongeza kifaa cha kuongeza
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Ongeza rasilimali ya salamu inayobadilika
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

Tazama mradi huu kuona jinsi unavyoweza [kuongeza maelekezo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Pia, angalia kiungo hiki cha jinsi ya kuitisha [maelekezo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Katika [sehemu iliyotangulia](../../../../03-GettingStarted/01-first-server), ulijifunza jinsi ya kuunda seva rahisi ya MCP kwa Rust. Unaweza kuendelea kujenga hapo au angalia kiungo hiki kwa mifano zaidi ya seva za MCP zilizoandikwa kwa Rust: [Mifano ya MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Suluhisho

**Folda ya suluhisho** ina utekelezaji kamili wa mteja tayari kuendesha unaoonyesha dhana zote zilizojadiliwa katika mafunzo haya. Kila suluhisho linajumuisha msimbo wa mteja na seva uliopangwa katika miradi tofauti, iliyo huru.

### 📁 Muundo wa Suluhisho

Saraka ya suluhisho imepangwa kwa lugha ya programu:

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

### 🚀 Kila Suluhisho Linajumuisha

Kila suluhisho la lugha maalum linatoa:

- **Utekelezaji kamili wa mteja** ukiwa na vipengele vyote kutoka kwa mafunzo
- **Muundo wa mradi unaofanya kazi** una utegemezi sahihi na usanidi
- **Scripts za kujenga na kuendesha** kwa urahisi wa usanidi na utekelezaji
- **README ya kina** yenye maelekezo maalum kwa kila lugha
- **Udhibiti wa makosa** na mifano ya usindikaji matokeo

### 📖 Kutumia Suluhisho

1. **Fikia folda ya lugha unayopendelea**:

   ```bash
   cd solution/typescript/    # Kwa TypeScript
   cd solution/java/          # Kwa Java
   cd solution/python/        # Kwa Python
   cd solution/dotnet/        # Kwa .NET
   ```

2. **Fuata maelekezo ya README kwenye kila folda kwa ajili ya:**
   - Kufunga utegemezi
   - Kujenga mradi
   - Kuendesha mteja

3. **Matokeo ya mfano** unayopaswa kuona:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Kwa hati kamili na maelekezo ya hatua kwa hatua, angalia: **[📖 Hati za Suluhisho](./solution/README.md)**

## 🎯 Mifano Kamili

Tumetoa utekelezaji kamili wa mteja wa lugha zote za programu zilizofunikwa katika mafunzo haya. Mifano hii inaonyesha utendakazi kamili ulioelezwa hapo juu na inaweza kutumika kama marejeleo au kama msingi wa miradi yako mwenyewe.

### Mifano Kamili Inayopatikana

| Lugha | Faili | Maelezo |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Mteja kamili wa Java akitumia usafirishaji wa SSE na udhibiti wa makosa kwa kina |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Mteja kamili wa C# akitumia usafirishaji wa stdio na kuanzisha seva moja kwa moja |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Mteja kamili wa TypeScript ukiunga mkono itifaki kamili ya MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Mteja kamili wa Python akitumia mifumo ya async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Mteja kamili wa Rust akitumia Tokio kwa operesheni za async |

Kila mfano kamili unajumuisha:
- ✅ **Kuanzishwa kwa muunganisho** na kushughulikia makosa  
- ✅ **Ugunduzi wa seva** (zana, rasilimali, miongozo pale inapowezekana)  
- ✅ **Operesheni za kalkuleta** (ongeza, toa, zidisha, gawanya, msaada)  
- ✅ **Usindikaji wa matokeo** na usanifu wa matokeo  
- ✅ **Kushughulikia makosa kwa kina**  
- ✅ **Nambari safi, iliyobainishwa** yenye maelezo ya hatua kwa hatua  

### Kuanzia na Mifano Kamili  

1. **Chagua lugha unayopendelea** kutoka kwenye meza hapo juu  
2. **Kagua faili la mfano kamili** ili kuelewa utekelezaji kamili  
3. **Endesha mfano huo** ukifuata maelekezo katika [`complete_examples.md`](./complete_examples.md)  
4. **Badilisha na ongeza** mfano kwa matumizi yako maalum  

Kwa nyaraka za kina kuhusu jinsi ya kuendesha na kubinafsisha mifano hii, angalia: **[📖 Nyaraka Kamili za Mifano](./complete_examples.md)**  

### 💡 Suluhisho dhidi ya Mifano Kamili  

| **Folda ya Suluhisho** | **Mifano Kamili** |  
|-----------------------|-------------------|  
| Muundo kamili wa mradi na faili za kujenga | Utekelezaji wa faili moja |  
| Tayari kuendeshwa na utegemezi | Mifano ya nambari iliyoelekezwa |  
| Mpangilio kama wa utengenezaji | Marejeleo ya kielimu |  
| Zana maalum za lugha | Mlinganisho wa lugha mbalimbali |  

Mbinu zote mbili ni za thamani - tumia **folda ya suluhisho** kwa miradi kamili na **mifano kamili** kwa kujifunza na marejeleo.  

## Muhimu Kufahamu  

Muhimu kuelewa katika sura hii kuhusu wateja ni yafuatayo:  

- Wanaweza kutumiwa kugundua na kuitisha sehemu kwenye seva.  
- Wanaweza kuanzisha seva wakati wanajiendesha wenyewe (kama katika sura hii) lakini wateja pia wanaweza kuunganishwa na seva zinazoendesha tayari.  
- Ni njia nzuri ya kujaribu uwezo wa seva kando na njia mbadala kama Inspector ilivyotajwa katika sura iliyopita.  

## Rasilimali Zaidi  

- [Ujengeaji wa wateja katika MCP](https://modelcontextprotocol.io/quickstart/client)  

## Sampuli  

- [Java Kalkuleta](../samples/java/calculator/README.md)  
- [.Net Kalkuleta](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Kalkuleta](../samples/javascript/README.md)  
- [TypeScript Kalkuleta](../samples/typescript/README.md)  
- [Python Kalkuleta](../../../../03-GettingStarted/samples/python)  
- [Rust Kalkuleta](../../../../03-GettingStarted/samples/rust)  

## Kitakachofuata  

- Kifuatazo: [Kuunda mteja na LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kweli ya Kusema**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufanikisha usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au kutokukamilika. Hati ya asili kwa lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu sana, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuwajibiki kwa maelewano au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
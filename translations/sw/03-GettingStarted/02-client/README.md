# Kuunda Mteja

Wateja ni programu maalum au maandiko yanayowasiliana moja kwa moja na Seva ya MCP kuomba rasilimali, zana, na maelekezo. Tofauti na kutumia zana ya ukaguzi, ambayo hutoa kiolesura cha picha kwa kuingiliana na seva, kuandika mteja wako mwenyewe kunaruhusu mwingiliano wa kiotomatiki na wa programu. Hii inawawezesha watengenezaji kuunganisha uwezo wa MCP katika mtiririko wao wa kazi, kuendesha kazi, na kujenga suluhisho maalum kulingana na mahitaji maalum.

## Muhtasari

Somo hili linaanzisha dhana ya wateja ndani ya mfumo wa Model Context Protocol (MCP). Utajifunza jinsi ya kuandika mteja wako mwenyewe na kuunganisha na Seva ya MCP.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa kile mteja anaweza kufanya.
- Kuandika mteja wako mwenyewe.
- Kuunganisha na kujaribu mteja na seva ya MCP ili kuhakikisha inafanya kazi kama inavyotarajiwa.

## Nini kinahitajika kuandika mteja?

Kuandika mteja, unahitaji kufanya yafuatayo:

- **Kuagiza maktaba sahihi**. Utatumia maktaba ile ile kama hapo awali, lakini kwa miundo tofauti.
- **Kuunda mteja**. Hii itahusisha kuunda mfano wa mteja na kuunganisha na njia ya usafirishaji iliyochaguliwa.
- **Kuamua rasilimali za kuorodhesha**. Seva yako ya MCP ina rasilimali, zana, na maelekezo, unahitaji kuamua ni ipi ya kuorodhesha.
- **Kuunganisha mteja na programu ya mwenyeji**. Mara tu unapojua uwezo wa seva, unahitaji kuunganisha hii na programu yako ya mwenyeji ili mtumiaji akiandika maelekezo au amri nyingine, kipengele kinachofaa cha seva kinaitwa.

Sasa kwa kuwa tunaelewa kwa kiwango cha juu kile tunachotaka kufanya, hebu tuangalie mfano ufuatao.

### Mfano wa mteja

Hebu tuangalie mfano huu wa mteja:

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

Katika msimbo uliotangulia:

- Tunaagiza maktaba.
- Tunaunda mfano wa mteja na kuunganisha kwa kutumia stdio kama njia ya usafirishaji.
- Tunaorodhesha maelekezo, rasilimali, na zana na kuzitumia zote.

Hapo unayo, mteja anayeweza kuzungumza na Seva ya MCP.

Hebu tuchukue muda katika sehemu ya mazoezi inayofuata na kuvunja kila kipande cha msimbo na kuelezea kinachoendelea.

## Mazoezi: Kuandika mteja

Kama ilivyosemwa hapo juu, hebu tuchukue muda kuelezea msimbo, na kwa vyovyote vile andika msimbo sambamba ikiwa unataka.

### -1- Kuagiza maktaba

Hebu tuagize maktaba tunazohitaji, tutahitaji marejeleo ya mteja na kwa njia yetu ya usafirishaji iliyochaguliwa, stdio. stdio ni itifaki kwa vitu vinavyokusudiwa kuendeshwa kwenye mashine yako ya ndani. SSE ni itifaki nyingine ya usafirishaji tutakayoonyesha katika sura zijazo lakini hiyo ndiyo chaguo lako lingine. Kwa sasa, tuendelee na stdio.

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

Kwa Java, utaunda mteja anayounganisha na seva ya MCP kutoka zoezi la awali. Ukitumia muundo ule ule wa mradi wa Java Spring Boot kutoka [Kuanza na Seva ya MCP](../../../../03-GettingStarted/01-first-server/solution/java), unda darasa jipya la Java linaloitwa `SDKClient` katika folda `src/main/java/com/microsoft/mcp/sample/client/` na ongeza uagizaji ufuatao:

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

Kutoka hapo, unaweza kuagiza maktaba zinazohitajika katika msimbo wako wa mteja.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Tuendelee na kuunda mfano.

### -2- Kuunda mteja na usafirishaji

Tutahitaji kuunda mfano wa usafirishaji na ule wa mteja wetu:

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

Katika msimbo uliotangulia:

- Tumeunda mfano wa usafirishaji wa stdio. Angalia jinsi inavyobainisha amri na hoja za jinsi ya kupata na kuanzisha seva kwani hiyo ni kitu tutahitaji kufanya tunapounda mteja.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Tumeunda mteja kwa kumpa jina na toleo.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Tumeunganisha mteja na njia ya usafirishaji iliyochaguliwa.

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

Katika msimbo uliotangulia:

- Tumeagiza maktaba zinazohitajika.
- Tumeunda kitu cha vigezo vya seva kwani tutatumia hii kuendesha seva ili tuweze kuunganisha nayo kwa mteja wetu.
- Tumeainisha mbinu `run` ambayo kwa upande wake inaita `stdio_client` ambayo huanzisha kikao cha mteja.
- Tumeunda sehemu ya kuingia ambapo tunatoa mbinu ya `run` kwa `asyncio.run`.

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

Katika msimbo uliotangulia:

- Tumeagiza maktaba zinazohitajika.
- Tumeunda usafirishaji wa stdio na kuunda mteja `mcpClient`. Hili ni jambo tutakalotumia kuorodhesha na kutumia vipengele kwenye Seva ya MCP.

Kumbuka, katika "Arguments", unaweza kuelekeza kwenye *.csproj* au kwenye faili inayoweza kutekelezwa.

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

Katika msimbo uliotangulia:

- Tumeunda mbinu kuu inayoseti usafirishaji wa SSE unaoelekeza `http://localhost:8080` ambapo seva yetu ya MCP itakuwa ikiendesha.
- Tumeunda darasa la mteja linalochukua usafirishaji kama parameter ya constructor.
- Katika mbinu ya `run`, tunaunda mteja wa MCP wa usawazishaji kwa kutumia usafirishaji na kuanzisha muunganisho.
- Tumetumia usafirishaji wa SSE (Server-Sent Events) ambao unafaa kwa mawasiliano yanayotegemea HTTP na seva za MCP za Java Spring Boot.

#### Rust

Kumbuka mteja huyu wa Rust unadhani seva ni mradi wa ndugu unaoitwa "calculator-server" katika saraka ile ile. Msimbo hapa chini utaanzisha seva na kuunganisha nayo.

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

### -3- Kuorodhesha vipengele vya seva

Sasa, tuna mteja anayeweza kuunganishwa ikiwa programu itaendeshwa. Hata hivyo, haionyeshi vipengele vyake kwa hivyo hebu tufanye hivyo sasa:

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

Hapa tunaorodhesha rasilimali zinazopatikana, `list_resources()` na zana, `list_tools` na kuzichapisha.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Hapo juu ni mfano wa jinsi tunavyoweza kuorodhesha zana kwenye seva. Kwa kila zana, tunachapisha jina lake.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Katika msimbo uliotangulia:

- Tumetumia `listTools()` kupata zana zote zinazopatikana kutoka seva ya MCP.
- Tumetumia `ping()` kuthibitisha kuwa muunganisho na seva unafanya kazi.
- `ListToolsResult` ina taarifa kuhusu zana zote ikiwa ni pamoja na majina yao, maelezo, na miundo ya pembejeo.

Vizuri, sasa tumeshika vipengele vyote. Sasa swali ni lini tunavitumia? Naam, mteja huyu ni rahisi, rahisi kwa maana kwamba tutahitaji kuita vipengele moja kwa moja tunapovihitaji. Katika sura inayofuata, tutaunda mteja wa hali ya juu zaidi ambaye ana ufikiaji wa mfano wake wa lugha kubwa, LLM. Kwa sasa, hebu tuone jinsi tunavyoweza kutumia vipengele kwenye seva:

#### Rust

Katika kazi kuu, baada ya kuanzisha mteja, tunaweza kuanzisha seva na kuorodhesha baadhi ya vipengele vyake.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Kutumia vipengele

Kutumia vipengele tunahitaji kuhakikisha tunabainisha hoja sahihi na katika baadhi ya matukio jina la kile tunachojaribu kutumia.

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

Katika msimbo uliotangulia:

- Tunasoma rasilimali, tunaita rasilimali kwa kutumia `readResource()` tukibainisha `uri`. Hivi ndivyo inavyoweza kuonekana upande wa seva:

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

    Thamani yetu ya `uri` `file://example.txt` inalingana na `file://{name}` kwenye seva. `example.txt` italinganishwa na `name`.

- Tunaita zana, tunaita kwa kubainisha `name` na `arguments` zake kama ifuatavyo:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Tunapata maelekezo, ili kupata maelekezo, unaita `getPrompt()` na `name` na `arguments`. Msimbo wa seva unaonekana kama ifuatavyo:

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

    na msimbo wako wa mteja unalingana na hivyo ili kuendana na kile kilichotangazwa kwenye seva:

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

Katika msimbo uliotangulia:

- Tumetumia rasilimali inayoitwa `greeting` kwa kutumia `read_resource`.
- Tumetumia zana inayoitwa `add` kwa kutumia `call_tool`.

#### .NET

1. Ongeza msimbo wa kutumia zana:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Ili kuchapisha matokeo, hapa kuna msimbo wa kushughulikia hilo:

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

Katika msimbo uliotangulia:

- Tumetumia zana kadhaa za calculator kwa kutumia mbinu `callTool()` na vitu vya `CallToolRequest`.
- Kila wito wa zana unabainisha jina la zana na `Map` ya hoja zinazohitajika na zana hiyo.
- Zana za seva zinatarajia majina maalum ya vigezo (kama "a", "b" kwa operesheni za hisabati).
- Matokeo yanarudishwa kama vitu vya `CallToolResult` vinavyobeba majibu kutoka kwa seva.

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

### -5- Kuendesha mteja

Kuendesha mteja, andika amri ifuatayo kwenye terminal:

#### TypeScript

Ongeza ingizo lifuatalo kwenye sehemu ya "scripts" katika *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Endesha mteja kwa amri ifuatayo:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Kwanza, hakikisha seva yako ya MCP inaendesha kwenye `http://localhost:8080`. Kisha endesha mteja:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Vinginevyo, unaweza kuendesha mradi kamili wa mteja uliotolewa katika folda ya suluhisho `03-GettingStarted\02-client\solution\java`:

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

## Kazi

Katika kazi hii, utatumia kile ulichojifunza katika kuunda mteja lakini utaunda mteja wako mwenyewe.

Hapa kuna seva unayoweza kutumia ambayo unahitaji kuipigia simu kupitia msimbo wako wa mteja, angalia ikiwa unaweza kuongeza vipengele zaidi kwenye seva ili kuifanya iwe ya kuvutia zaidi.

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

Angalia mradi huu ili kuona jinsi unavyoweza [kuongeza maelekezo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Pia, angalia kiungo hiki kwa jinsi ya kutumia [maelekezo na rasilimali](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Katika [sehemu ya awali](../../../../03-GettingStarted/01-first-server), ulijifunza jinsi ya kuunda seva rahisi ya MCP na Rust. Unaweza kuendelea kujenga juu ya hiyo au angalia kiungo hiki kwa mifano zaidi ya seva za MCP zinazotumia Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Suluhisho

Folda ya **suluhisho** ina utekelezaji kamili wa wateja walio tayari kuendeshwa ambao unaonyesha dhana zote zilizofunikwa katika mafunzo haya. Kila suluhisho linajumuisha msimbo wa mteja na seva ulioandaliwa katika miradi tofauti, inayojitegemea.

### 📁 Muundo wa Suluhisho

Saraka ya suluhisho imepangwa kulingana na lugha ya programu:

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

Kila suluhisho maalum kwa lugha linatoa:

- **Utekelezaji kamili wa mteja** na vipengele vyote kutoka kwenye mafunzo.
- **Muundo wa mradi unaofanya kazi** na utegemezi sahihi na usanidi.
- **Skripti za kujenga na kuendesha** kwa usanidi rahisi na utekelezaji.
- **README ya kina** yenye maelekezo maalum kwa lugha.
- **Mfano wa kushughulikia makosa** na usindikaji wa matokeo.

### 📖 Kutumia Suluhisho

1. **Nenda kwenye folda ya lugha unayopendelea**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Fuata maelekezo ya README** katika kila folda kwa:
   - Kusakinisha utegemezi.
   - Kujenga mradi.
   - Kuendesha mteja.

3. **Mfano wa matokeo** unayopaswa kuona:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Kwa nyaraka kamili na maelekezo ya hatua kwa hatua, angalia: **[📖 Nyaraka za Suluhisho](./solution/README.md)**

## 🎯 Mifano Kamili

Tumetoa utekelezaji kamili wa wateja wanaofanya kazi kwa lugha zote za programu zilizofunikwa katika mafunzo haya. Mifano hii inaonyesha utendaji kamili ulioelezwa hapo juu na inaweza kutumika kama utekelezaji wa marejeleo au sehemu za kuanzia kwa miradi yako mwenyewe.

### Mifano Kamili Inayopatikana

| Lugha | Faili | Maelezo |
|-------|-------|---------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Mteja kamili wa Java akitumia usafirishaji wa SSE na kushughulikia makosa kwa kina |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Mteja kamili wa C# akitumia usafirishaji wa stdio na kuanzisha seva kiotomatiki |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Mteja kamili wa TypeScript na msaada kamili wa itifaki ya MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Mteja kamili wa Python akitumia mifumo ya async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Mteja kamili wa Rust akitumia Tokio kwa operesheni za async |
Kila mfano kamili unajumuisha:

- ✅ **Kuanzisha muunganisho** na kushughulikia makosa
- ✅ **Ugunduzi wa seva** (vifaa, rasilimali, maelekezo inapohitajika)
- ✅ **Operesheni za kikokotoo** (kujumlisha, kutoa, kuzidisha, kugawanya, msaada)
- ✅ **Usindikaji wa matokeo** na matokeo yaliyopangwa vizuri
- ✅ **Ushughulikiaji wa makosa kwa kina**
- ✅ **Nambari safi, iliyo na maelezo** na maoni ya hatua kwa hatua

### Kuanza na Mifano Kamili

1. **Chagua lugha unayopendelea** kutoka kwenye jedwali hapo juu
2. **Pitia faili ya mfano kamili** ili kuelewa utekelezaji mzima
3. **Endesha mfano** ukifuata maelekezo katika [`complete_examples.md`](./complete_examples.md)
4. **Badilisha na panua** mfano kwa matumizi yako maalum

Kwa maelezo ya kina kuhusu jinsi ya kuendesha na kubadilisha mifano hii, angalia: **[📖 Nyaraka za Mifano Kamili](./complete_examples.md)**

### 💡 Suluhisho vs. Mifano Kamili

| **Folda ya Suluhisho** | **Mifano Kamili** |
|--------------------|--------------------- |
| Muundo kamili wa mradi na faili za ujenzi | Utekelezaji wa faili moja |
| Tayari kuendeshwa na utegemezi | Mifano ya nambari iliyolenga |
| Mpangilio wa uzalishaji | Marejeleo ya kielimu |
| Zana maalum za lugha | Ulinganisho wa lugha tofauti |

Njia zote mbili zina thamani - tumia **folda ya suluhisho** kwa miradi kamili na **mifano kamili** kwa kujifunza na marejeleo.

## Mambo Muhimu

Mambo muhimu ya sura hii kuhusu wateja ni yafuatayo:

- Inaweza kutumika kugundua na kutumia vipengele kwenye seva.
- Inaweza kuanzisha seva wakati inajiendesha (kama ilivyoelezwa katika sura hii) lakini wateja wanaweza pia kuungana na seva zinazoendesha.
- Ni njia nzuri ya kujaribu uwezo wa seva kando na mbadala kama Inspector kama ilivyoelezwa katika sura iliyopita.

## Rasilimali za Ziada

- [Kujenga wateja katika MCP](https://modelcontextprotocol.io/quickstart/client)

## Sampuli

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Nini Kinachofuata

- Kinachofuata: [Kuunda mteja na LLM](../03-llm-client/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
# Paglikha ng isang kliyente

Ang mga kliyente ay mga custom na aplikasyon o script na direktang nakikipag-ugnayan sa isang MCP Server upang humiling ng mga resources, tools, at prompts. Hindi tulad ng paggamit ng inspector tool, na nagbibigay ng graphical na interface para makipag-ugnayan sa server, ang pagsulat ng sarili mong kliyente ay nagbibigay-daan sa programmatic at automated na mga interaksiyon. Ito ay nagpapahintulot sa mga developer na isama ang mga kakayahan ng MCP sa kanilang sariling workflows, i-automate ang mga gawain, at bumuo ng mga custom na solusyon na iniakma sa mga partikular na pangangailangan.

## Pangkalahatang-ideya

Ipinapakilala ng araling ito ang konsepto ng mga kliyente sa loob ng ekosistema ng Model Context Protocol (MCP). Matututuhan mo kung paano sumulat ng sarili mong kliyente at kung paano ito kumonekta sa isang MCP Server.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Maunawaan kung ano ang magagawa ng isang kliyente.
- Sumulat ng sarili mong kliyente.
- Kumonekta at subukan ang kliyente sa isang MCP server upang matiyak na ito ay gumagana gaya ng inaasahan.

## Ano ang mga kinakailangan sa pagsulat ng isang kliyente?

Upang sumulat ng isang kliyente, kailangang gawin ang mga sumusunod:

- **Import ang tamang mga library**. Gagamitin mo ang parehong library tulad ng dati, ngunit iba't ibang mga konstrukto.
- **Gumawa ng isang kliyente**. Kabilang dito ang paglikha ng isang instance ng kliyente at pagkonekta nito sa napiling paraan ng transport.
- **Pumili kung anong mga resources ang ililista**. Ang iyong MCP server ay may kasamang mga resources, tools, at prompts, kailangan mong pumili kung alin ang ililista.
- **Isama ang kliyente sa isang host application**. Kapag nasa alam mo na ang mga kakayahan ng server, kailangan mong isama ito sa iyong host application upang kapag ang isang user ay nag-type ng prompt o ibang utos ay ma-trigger ang katugmang tampok ng server.

Ngayon na naiintindihan natin sa mataas na antas kung ano ang gagawin natin, tingnan natin ang isang halimbawa.

### Isang halimbawa ng kliyente

Tingnan natin ang halimbawa ng kliyenteng ito:

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

// Ilan sa mga prompt
const prompts = await client.listPrompts();

// Kunin ang isang prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Ilan sa mga resources
const resources = await client.listResources();

// Basahin ang isang resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Tawagan ang isang tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Sa naunang code ay:

- Inimport ang mga library
- Gumawa ng isang instance ng kliyente at ikinonekta ito gamit ang stdio para sa transport.
- Nilista ang mga prompts, resources, at tools at tinawag silang lahat.

Ayan, isang kliyente na kayang makipag-usap sa isang MCP Server.

Maglalaan tayo ng oras sa susunod na bahagi ng ehersisyo upang himayin ang bawat snippet ng code at ipaliwanag ang nangyayari.

## Ehersisyo: Pagsusulat ng isang kliyente

Tulad ng nabanggit, maglalaan tayo ng oras sa pagpapaliwanag ng code, at malaya mong sundan ito habang nagko-code.

### -1- Pag-import ng mga library

I-import natin ang mga library na kailangan, kakailanganin natin ng mga reference sa isang kliyente at sa napili nating transport protocol, stdio. Ang stdio ay isang protocol para sa mga bagay na tatakbo sa iyong lokal na makina. Ang SSE ay isa pang transport protocol na ipapakita natin sa mga susunod na kabanata bilang ibang opsyon. Sa ngayon, itutuloy muna natin gamit ang stdio.

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

Para sa Java, gagawa ka ng kliyente na kumokonekta sa MCP server mula sa naunang ehersisyo. Gamit ang parehong Java Spring Boot project structure mula sa [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), gumawa ng bagong Java class na tinatawag na `SDKClient` sa folder na `src/main/java/com/microsoft/mcp/sample/client/` at idagdag ang mga sumusunod na imports:

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

Kailangan mong idagdag ang mga sumusunod na dependencies sa iyong `Cargo.toml` file.

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

Mula doon, maaari mong i-import ang mga kinakailangang library sa iyong client code.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Tayo na sa paggawa ng instantiation.

### -2- Paggawa ng instance ng client at transport

Kailangan nating gumawa ng instance ng transport at ng ating kliyente:

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

Sa naunang code ay:

- Gumawa ng stdio transport instance. Mapapansin dito ang pag-specify ng command at args kung paano maghanap at magsimulang patakbuhin ang server na kailangan nating gawin habang ginagawa ang kliyente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Nag-instantiate ng kliyente sa pamamagitan ng pagbibigay ng pangalan at bersyon.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Ikinonekta ang kliyente sa napiling transport.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Lumikha ng mga parameter ng server para sa stdio na koneksyon
server_params = StdioServerParameters(
    command="mcp",  # Natawag na programa
    args=["run", "server.py"],  # Opsyonal na mga argumento ng linya ng utos
    env=None,  # Opsyonal na mga variable ng kapaligiran
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # I-initialize ang koneksyon
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Sa naunang code ay:

- Inimport ang mga kinakailangang library
- Nag-instantiate ng server parameters na gagamitin para patakbuhin ang server para makakonekta tayo dito gamit ang kliyente.
- Nagdeklara ng method na `run` na tumatawag sa `stdio_client` upang magsimula ng session ng kliyente.
- Nilikha ang entry point kung saan ibinibigay natin ang `run` method sa `asyncio.run`.

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

Sa naunang code ay:

- Inimport ang mga kinakailangang library.
- Gumawa ng stdio transport at gumawa ng kliyente na tinawag na `mcpClient`. Ito ang gagamitin natin para maglista at tumawag ng mga feature sa MCP Server.

Tandaan, sa "Arguments", maaari kang tumukoy sa *.csproj* o sa executable.

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
        
        // Dito ilalagay ang iyong lohika ng kliyente
    }
}
```

Sa naunang code ay:

- Gumawa ng main method na nag-set up ng SSE transport na tumuturo sa `http://localhost:8080` kung saan tatakbo ang MCP server.
- Gumawa ng client class na tumatanggap ng transport bilang constructor parameter.
- Sa `run` method, gumawa tayo ng synchronous MCP client gamit ang transport at inisyalisa ang koneksyon.
- Ginamit ang SSE (Server-Sent Events) transport na angkop para sa HTTP-based na komunikasyon sa Java Spring Boot MCP servers.

#### Rust

Tandaan na ang Rust client na ito ay inaasahang ang server ay isang sibling project na pinangalanang "calculator-server" sa parehong direktoryo. Ang code sa ibaba ay sisimulan ang server at kokonekta rito.

```rust
async fn main() -> Result<(), RmcpError> {
    // Ipinalalagay na ang server ay isang kapatid na proyekto na pinangalanang "calculator-server" sa parehong direktoryo
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

    // GAGAWIN: I-initialize

    // GAGAWIN: Ilahad ang mga kagamitan

    // GAGAWIN: Tawagin ang add tool gamit ang mga argumento = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Paglilista ng mga tampok ng server

Ngayon, mayroon na tayong kliyente na maaaring kumonekta kapag pinatakbo ang programa. Ngunit hindi nito aktwal na nililista ang mga tampok nito kaya't gawin natin iyon:

#### TypeScript

```typescript
// Listahan ng mga prompt
const prompts = await client.listPrompts();

// Listahan ng mga pinagkukunan
const resources = await client.listResources();

// listahan ng mga kasangkapan
const tools = await client.listTools();
```

#### Python

```python
# Ilahad ang mga magagamit na mapagkukunan
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Ilahad ang mga magagamit na kasangkapan
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Dito ay nililista natin ang mga available na resources, `list_resources()` at tools, `list_tools` at ipiniprint ang mga ito.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Nasa itaas ang halimbawa kung paano tayo makakapaglista ng mga tools sa server. Para sa bawat tool, pini-print natin ang pangalan nito.

#### Java

```java
// Ilahad at ipakita ang mga kasangkapan
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Maaari mo ring i-ping ang server upang tiyakin ang koneksyon
client.ping();
```

Sa naunang code ay:

- Tinawag ang `listTools()` upang makuha ang lahat ng available na tools mula sa MCP server.
- Ginamit ang `ping()` upang tiyakin na gumagana ang koneksyon sa server.
- Ang `ListToolsResult` ay naglalaman ng impormasyon tungkol sa lahat ng mga tool kabilang ang kanilang mga pangalan, paglalarawan, at input schemas.

Mahusay, ngayon ay nakuha na natin ang lahat ng mga tampok. Ngayon ang tanong ay kailan natin gagamitin ang mga ito? Ang kliyenteng ito ay medyo simple, ibig sabihin kailangan nating tawagin ang mga tampok nang hayagan kapag gusto natin ito. Sa susunod na kabanata, gagawa tayo ng isang mas advance na kliyente na may access sa sarili nitong malaking language model, LLM. Sa ngayon, tingnan muna natin kung paano tawagin ang mga tampok sa server:

#### Rust

Sa main function, pagkatapos i-initialize ang kliyente, maaari nating i-initialize ang server at ilista ang ilan sa mga tampok nito.

```rust
// Simulan
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Ilahad ang mga kasangkapan
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pagtawag sa mga tampok

Upang tawagin ang mga tampok, kailangan nating tiyakin na tama ang mga argumento at sa ilang kaso ang pangalan ng tinatawagan.

#### TypeScript

```typescript

// Basahin ang isang yaman
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Tawagan ang isang kasangkapan
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// tawagan ang prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Sa naunang code ay:

- Nagbasa ng resource, tinawag ang resource gamit ang `readResource()` na naglalaman ng `uri`. Ganito ito kadalas tignan sa server side:

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

    Ang `uri` na value na `file://example.txt` ay tumutugma sa `file://{name}` sa server. Ang `example.txt` ay ipa-map sa `name`.

- Tumawag ng tool, tinawag ito sa pamamagitan ng pagtukoy ng `name` at `arguments` tulad nito:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Kumuha ng prompt, para makuha ang prompt, tinatawag mo ang `getPrompt()` gamit ang `name` at `arguments`. Ganito ang hitsura ng server code:

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

    kaya ang resulta ng iyong client code ay ganito upang tumugma sa declare sa server:

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
# Basahin ang isang mapagkukunan
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Tawagan ang isang kasangkapan
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Sa naunang code ay:

- Tinawag ang resource na `greeting` gamit ang `read_resource`.
- Tinawag ang tool na `add` gamit ang `call_tool`.

#### .NET

1. Magdagdag tayo ng code upang tumawag sa isang tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Para iprint ang resulta, ito ang code para gawin iyon:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Tawagin ang iba't ibang mga tool sa calculator
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

Sa naunang code ay:

- Tinawag ang maraming calculator tool gamit ang `callTool()` method na may `CallToolRequest` objects.
- Bawat tawag sa tool ay nagsasaad ng pangalan ng tool at isang `Map` ng mga argument na kailangan ng tool.
- Ang mga tool sa server ay inaasahan ang mga tiyak na pangalan ng parameter (tulad ng "a", "b" para sa mga mathematical operation).
- Ang resulta ay ibinalik bilang mga `CallToolResult` object na naglalaman ng tugon mula sa server.

#### Rust

```rust
// Tawagan ang add tool na may mga argumento = {"a": 3, "b": 2}
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

### -5- Patakbuhin ang kliyente

Upang patakbuhin ang kliyente, i-type ang sumusunod na command sa terminal:

#### TypeScript

Idagdag ang sumusunod na entry sa seksyong "scripts" sa *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Tawagin ang kliyente gamit ang sumusunod na command:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Siguraduhing ang MCP server ay tumatakbo sa `http://localhost:8080`. Pagkatapos patakbuhin ang kliyente:

```bash
# Itayo ang iyong proyekto
./mvnw clean compile

# Patakbuhin ang kliyente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Bilang alternatibo, maaari mong patakbuhin ang kumpletong proyekto ng kliyente na nasa solusyon folder `03-GettingStarted\02-client\solution\java`:

```bash
# Mag-navigate sa direktoryo ng solusyon
cd 03-GettingStarted/02-client/solution/java

# I-build at patakbuhin ang JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Takdang Aralin

Sa takdang araling ito, gagamitin mo ang mga natutunan mo sa paglikha ng isang kliyente ngunit gagawa ka ng sarili mong kliyente.

Narito ang isang server na maaari mong gamitin na kailangang tawagin sa pamamagitan ng iyong client code, tingnan kung makakapagdagdag ka ng mas maraming feature sa server upang maging mas kawili-wili.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Lumikha ng isang MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Magdagdag ng isang karagdagang tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Magdagdag ng isang dynamic na greeting resource
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

// Simulang tumanggap ng mga mensahe sa stdin at magpadala ng mga mensahe sa stdout

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

# Gumawa ng MCP server
mcp = FastMCP("Demo")


# Magdagdag ng karagdagang tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng dynamic na pagbati na resource
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

Tingnan ang proyekto na ito para makita kung paano ka makakapagdagdag ng [prompts at resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tingnan din ang link na ito para sa kung paano tumawag ng [prompts at resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Sa [nakaraang seksyon](../../../../03-GettingStarted/01-first-server), natutunan mo kung paano gumawa ng isang simpleng MCP server gamit ang Rust. Maaari kang magpatuloy na bumuo dito o tingnan ang link na ito para sa iba pang mga Rust-based MCP server examples: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solusyon

Ang **solution folder** ay naglalaman ng kumpleto, handa nang patakbuhin na mga implementasyon ng kliyente na nagpapakita ng lahat ng mga konseptong tinalakay sa tutorial na ito. Bawat solusyon ay may kliyente at server code na inayos sa magkahiwalay, self-contained na mga proyekto.

### 📁 Estruktura ng Solusyon

Ang direktoryo ng solusyon ay inayos ayon sa programming language:

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

### 🚀 Ano ang Nilalaman ng Bawat Solusyon

Ang bawat solusyon ayon sa wika ay nagbibigay ng:

- **Kumpletong implementasyon ng kliyente** na may lahat ng tampok mula sa tutorial
- **Gumaganang istruktura ng proyekto** na may tamang dependencies at configuration
- **Mga build at run script** para sa madaling setup at pagpapatupad
- **Detalyadong README** na may mga tagubilin ayon sa wika
- **Halimbawa ng paghawak ng error** at pagproseso ng resulta

### 📖 Paggamit ng mga Solusyon

1. **Pumunta sa folder ng nais mong wika**:

   ```bash
   cd solution/typescript/    # Para sa TypeScript
   cd solution/java/          # Para sa Java
   cd solution/python/        # Para sa Python
   cd solution/dotnet/        # Para sa .NET
   ```

2. **Sundin ang mga tagubilin sa README** sa bawat folder para sa:
   - Pag-install ng dependencies
   - Pag-build ng proyekto
   - Pagpapatakbo ng kliyente

3. **Halimbawa ng output** na makikita mo:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para sa kumpletong dokumentasyon at sunud-sunod na mga tagubilin, tingnan: **[📖 Solusyon Dokumentasyon](./solution/README.md)**

## 🎯 Kumpletong Mga Halimbawa

Nagbigay kami ng kumpleto, gumaganang mga implementasyon ng kliyente para sa lahat ng mga programming language na tinalakay sa tutorial na ito. Ipinapakita ng mga halimbawang ito ang buong functionality na inilarawan sa itaas at maaaring gamitin bilang mga reference implementation o panimulang punto para sa iyong sariling mga proyekto.

### Mga Available na Kumpletong Halimbawa

| Wika | File | Paglalarawan |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kumpletong Java kliyente gamit ang SSE transport na may komprehensibong paghawak ng error |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kumpletong C# kliyente gamit ang stdio transport na may awtomatikong pagsisimula ng server |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kumpletong TypeScript kliyente na may buong suporta sa MCP protocol |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kumpletong Python kliyente gamit ang async/await nga pattern |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Kumpletong Rust kliyente gamit ang Tokio para sa async na operasyon |

Bawat kumpletong halimbawa ay nagsasama ng:

- ✅ **Pag-establish ng koneksyon** at paghawak ng error
- ✅ **Pag-diskubre ng server** (tools, resources, prompts kung saan naaangkop)
- ✅ **Mga operasyon ng calculator** (add, subtract, multiply, divide, help)
- ✅ **Pagproseso ng resulta** at naka-format na output
- ✅ **Komprehensibong paghawak ng error**

- ✅ **Malinis, dokumentadong code** na may hakbang-hakbang na mga komento

### Pagsisimula Gamit ang Kumpletong Mga Halimbawa

1. **Piliin ang iyong nais na wika** mula sa talahanayan sa itaas
2. **Suriin ang kumpletong halimbawa ng file** upang maunawaan ang buong implementasyon
3. **Patakbuhin ang halimbawa** sundin ang mga tagubilin sa [`complete_examples.md`](./complete_examples.md)
4. **Baguhin at palawakin** ang halimbawa para sa iyong partikular na gamit

Para sa detalyadong dokumentasyon tungkol sa pagpapatakbo at pag-customize ng mga halimbawang ito, tingnan: **[📖 Kumpletong Dokumentasyon ng Mga Halimbawa](./complete_examples.md)**

### 💡 Solusyon vs. Kumpletong Mga Halimbawa

| **Folder ng Solusyon** | **Kumpletong Mga Halimbawa** |
|--------------------|--------------------- |
| Buong estruktura ng proyekto na may mga build file | Mga implementasyon sa isang file |
| Handang patakbuhin kasama ang mga dependencies | Nakatuon na mga halimbawa ng code |
| Setup na parang production | Pang-edukasyon na sanggunian |
| Tooling na partikular sa wika | Paghahambing ng iba't ibang wika |

Mahalaga ang parehong mga pamamaraan - gamitin ang **folder ng solusyon** para sa kumpletong mga proyekto at ang **kumpletong mga halimbawa** para sa pag-aaral at sanggunian.

## Pangunahing Mga Punto

Ang mga pangunahing punto para sa kabanatang ito tungkol sa mga kliyente ay ang mga sumusunod:

- Maaaring gamitin upang tuklasin at tawagan ang mga tampok sa server.
- Maaaring magsimula ng server habang nagsisimula rin ito mismo (tulad sa kabanatang ito) ngunit maaaring kumonekta ang mga kliyente sa mga tumatakbong server.
- Isang mahusay na paraan upang subukan ang kakayahan ng server kasabay ng mga alternatibo tulad ng Inspector na inilarawan sa nakaraang kabanata.

## Karagdagang Mga Sanggunian

- [Pagbuo ng mga kliyente sa MCP](https://modelcontextprotocol.io/quickstart/client)

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Ano ang Sunod

- Sunod: [Paglikha ng isang kliyente gamit ang LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Paglikha ng Kliyente

Ang mga kliyente ay mga custom na aplikasyon o script na direktang nakikipag-ugnayan sa isang MCP Server upang humiling ng mga resources, tools, at prompts. Hindi tulad ng paggamit ng inspector tool na nagbibigay ng graphical interface para makipag-ugnayan sa server, ang pagsusulat ng sarili mong kliyente ay nagbibigay-daan para sa programmatic at automated na interaksyon. Sa ganitong paraan, maaaring isama ng mga developer ang mga kakayahan ng MCP sa kanilang sariling workflows, mag-automate ng mga gawain, at bumuo ng mga custom na solusyon na akma sa partikular na pangangailangan.

## Pangkalahatang-ideya

Ang araling ito ay nagpapakilala sa konsepto ng mga kliyente sa loob ng Model Context Protocol (MCP) ecosystem. Matututuhan mong magsulat ng sarili mong kliyente at ikonekta ito sa isang MCP Server.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mo ang sumusunod:

- Maunawaan kung ano ang magagawa ng isang kliyente.
- Magsulat ng sarili mong kliyente.
- Ikonekta at subukan ang kliyente sa isang MCP server upang matiyak na gumagana ito nang maayos.

## Ano ang kailangan sa pagsusulat ng kliyente?

Upang makapagsulat ng kliyente, kailangan mong gawin ang mga sumusunod:

- **I-import ang tamang mga library**. Gagamitin mo ang parehong library tulad ng dati, ngunit iba ang mga constructs.
- **Mag-instantiate ng kliyente**. Kasama rito ang paggawa ng instance ng kliyente at ikonekta ito sa napiling transport method.
- **Magdesisyon kung anong mga resources ang ililista**. Ang iyong MCP server ay may kasamang mga resources, tools, at prompts; kailangan mong magdesisyon kung alin ang ililista.
- **Isama ang kliyente sa isang host application**. Kapag nalaman mo na ang mga kakayahan ng server, kailangan mong isama ito sa iyong host application upang kapag nag-type ang user ng prompt o iba pang command, ang kaukulang feature ng server ay ma-invoke.

Ngayon na nauunawaan na natin sa mataas na antas kung ano ang gagawin, tingnan natin ang isang halimbawa.

### Isang Halimbawa ng Kliyente

Tingnan natin ang halimbawa ng kliyente:

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

Sa code na ito:

- I-import ang mga library.
- Gumawa ng instance ng kliyente at ikonekta ito gamit ang stdio bilang transport.
- Ilista ang mga prompts, resources, at tools at i-invoke ang mga ito.

Narito na ang isang kliyente na maaaring makipag-usap sa isang MCP Server.

Pag-usapan natin nang mas detalyado ang bawat bahagi ng code sa susunod na seksyon ng ehersisyo.

## Ehersisyo: Pagsusulat ng Kliyente

Gaya ng nabanggit, pag-usapan natin nang detalyado ang code, at maaari kang sumabay sa pag-code kung nais mo.

### -1- I-import ang mga Library

I-import natin ang mga library na kailangan natin. Kakailanganin natin ng reference sa isang kliyente at sa napiling transport protocol, stdio. Ang stdio ay isang protocol para sa mga bagay na tumatakbo sa iyong lokal na makina. Ang SSE ay isa pang transport protocol na ipapakita natin sa mga susunod na kabanata, ngunit iyon ang isa pang opsyon. Sa ngayon, magpatuloy tayo sa stdio.

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

Para sa Java, gagawa ka ng kliyente na kumokonekta sa MCP server mula sa nakaraang ehersisyo. Gamit ang parehong Java Spring Boot project structure mula sa [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), gumawa ng bagong Java class na tinatawag na `SDKClient` sa `src/main/java/com/microsoft/mcp/sample/client/` folder at idagdag ang mga sumusunod na imports:

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

Kakailanganin mong idagdag ang mga sumusunod na dependencies sa iyong `Cargo.toml` file.

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

Mula rito, maaari mong i-import ang mga kinakailangang library sa iyong client code.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Magpatuloy tayo sa instantiation.

### -2- Pag-instantiate ng Kliyente at Transport

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

Sa code na ito:

- Gumawa ng stdio transport instance. Pansinin kung paano nito tinutukoy ang command at args para mahanap at ma-start ang server dahil ito ang kailangan nating gawin habang ginagawa ang kliyente.

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

- Ikonekta ang kliyente sa napiling transport.

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

Sa code na ito:

- I-import ang mga kinakailangang library.
- Nag-instantiate ng server parameters object na gagamitin natin para patakbuhin ang server upang makakonekta tayo rito gamit ang ating kliyente.
- Nag-defina ng method na `run` na tumatawag sa `stdio_client` na nagsisimula ng client session.
- Gumawa ng entry point kung saan ibinibigay natin ang `run` method sa `asyncio.run`.

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

Sa code na ito:

- I-import ang mga kinakailangang library.
- Gumawa ng stdio transport at gumawa ng kliyente na `mcpClient`. Ang huli ay gagamitin natin upang ilista at i-invoke ang mga feature sa MCP Server.

Tandaan, sa "Arguments", maaari kang magturo sa *.csproj* o sa executable.

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

Sa code na ito:

- Gumawa ng main method na nagse-set up ng SSE transport na tumuturo sa `http://localhost:8080` kung saan tatakbo ang ating MCP server.
- Gumawa ng client class na tumatanggap ng transport bilang constructor parameter.
- Sa `run` method, gumawa ng synchronous MCP client gamit ang transport at ini-initialize ang koneksyon.
- Gumamit ng SSE (Server-Sent Events) transport na angkop para sa HTTP-based na komunikasyon sa Java Spring Boot MCP servers.

#### Rust

Ang Rust client na ito ay inaasahang ang server ay isang sibling project na tinatawag na "calculator-server" sa parehong direktoryo. Ang code sa ibaba ay mag-i-start ng server at kokonekta rito.

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

### -3- Paglilista ng Mga Feature ng Server

Ngayon, mayroon na tayong kliyente na maaaring kumonekta kapag pinatakbo ang programa. Gayunpaman, hindi pa nito nililista ang mga feature nito kaya gawin natin iyon:

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

Dito, inilista natin ang mga available na resources gamit ang `list_resources()` at tools gamit ang `list_tools` at prinint ang mga ito.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Ito ay isang halimbawa kung paano natin maililista ang mga tools sa server. Para sa bawat tool, prinint natin ang pangalan nito.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Sa code na ito:

- Tinawag ang `listTools()` upang makuha ang lahat ng available na tools mula sa MCP server.
- Gumamit ng `ping()` upang tiyakin na gumagana ang koneksyon sa server.
- Ang `ListToolsResult` ay naglalaman ng impormasyon tungkol sa lahat ng tools kabilang ang kanilang mga pangalan, deskripsyon, at input schemas.

Magaling, nakuha na natin ang lahat ng feature. Ngayon ang tanong ay kailan natin gagamitin ang mga ito? Ang kliyenteng ito ay medyo simple, simple sa kahulugan na kailangan nating tahasang tawagin ang mga feature kapag gusto natin ang mga ito. Sa susunod na kabanata, gagawa tayo ng mas advanced na kliyente na may access sa sarili nitong large language model, LLM. Sa ngayon, tingnan natin kung paano natin ma-i-invoke ang mga feature sa server:

#### Rust

Sa main function, pagkatapos i-initialize ang kliyente, maaari nating i-initialize ang server at ilista ang ilan sa mga feature nito.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pag-invoke ng Mga Feature

Upang ma-invoke ang mga feature, kailangan nating tiyakin na tama ang mga argument na ispesipika at sa ilang kaso ang pangalan ng ating sinusubukang i-invoke.

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

Sa code na ito:

- Nagbasa ng resource sa pamamagitan ng pagtawag sa `readResource()` at ispesipikang `uri`. Ganito ang hitsura nito sa server side:

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

    Ang ating `uri` value na `file://example.txt` ay tumutugma sa `file://{name}` sa server. Ang `example.txt` ay ma-ma-map sa `name`.

- Tumawag ng tool sa pamamagitan ng pag-ispesipika ng `name` at `arguments` nito tulad nito:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Kumuha ng prompt sa pamamagitan ng pagtawag sa `getPrompt()` gamit ang `name` at `arguments`. Ganito ang hitsura ng server code:

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

    At ang iyong resulting client code ay ganito upang tumugma sa nakasaad sa server:

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

Sa code na ito:

- Tumawag ng resource na tinatawag na `greeting` gamit ang `read_resource`.
- Nag-invoke ng tool na tinatawag na `add` gamit ang `call_tool`.

#### .NET

1. Magdagdag ng code upang tumawag ng tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Upang i-print ang resulta, narito ang code para sa pag-handle nito:

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

Sa code na ito:

- Tumawag ng maraming calculator tools gamit ang `callTool()` method na may `CallToolRequest` objects.
- Ang bawat tawag sa tool ay nag-ispesipika ng pangalan ng tool at isang `Map` ng mga argument na kinakailangan ng tool na iyon.
- Ang mga tool sa server ay inaasahan ang mga partikular na pangalan ng parameter (tulad ng "a", "b" para sa mga mathematical operations).
- Ang mga resulta ay ibinabalik bilang `CallToolResult` objects na naglalaman ng tugon mula sa server.

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

### -5- Patakbuhin ang Kliyente

Upang patakbuhin ang kliyente, i-type ang sumusunod na command sa terminal:

#### TypeScript

Idagdag ang sumusunod na entry sa iyong "scripts" section sa *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Patakbuhin ang kliyente gamit ang sumusunod na command:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Siguraduhing tumatakbo ang iyong MCP server sa `http://localhost:8080`. Pagkatapos, patakbuhin ang kliyente:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Bilang alternatibo, maaari mong patakbuhin ang kumpletong client project na nasa solution folder na `03-GettingStarted\02-client\solution\java`:

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

## Gawain

Sa gawaing ito, gagamitin mo ang natutunan sa paggawa ng kliyente ngunit gagawa ka ng sarili mong kliyente.

Narito ang isang server na maaari mong gamitin na kailangan mong tawagan gamit ang iyong client code. Subukang magdagdag ng higit pang mga feature sa server upang gawing mas kawili-wili ito.

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

Tingnan ang proyektong ito upang makita kung paano ka makakapagdagdag ng [prompts at resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Tingnan din ang link na ito para sa kung paano mag-invoke ng [prompts at resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Sa [nakaraang seksyon](../../../../03-GettingStarted/01-first-server), natutunan mo kung paano gumawa ng simpleng MCP server gamit ang Rust. Maaari kang magpatuloy na bumuo mula rito o tingnan ang link na ito para sa higit pang mga halimbawa ng Rust-based MCP server: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solusyon

Ang **solution folder** ay naglalaman ng kumpleto, handa nang patakbuhing mga implementasyon ng kliyente na nagpapakita ng lahat ng konseptong tinalakay sa tutorial na ito. Ang bawat solusyon ay may kasamang parehong client at server code na nakaayos sa magkakahiwalay, self-contained na mga proyekto.

### 📁 Istruktura ng Solusyon

Ang solution directory ay nakaayos ayon sa programming language:

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

### 🚀 Ano ang Kasama sa Bawat Solusyon

Ang bawat language-specific na solusyon ay nagbibigay ng:

- **Kumpletong implementasyon ng kliyente** na may lahat ng feature mula sa tutorial
- **Gumaganang project structure** na may tamang dependencies at configuration
- **Build at run scripts** para sa madaling setup at execution
- **Detalyadong README** na may language-specific na mga tagubilin
- **Mga halimbawa ng error handling** at result processing

### 📖 Paggamit ng Mga Solusyon

1. **Pumunta sa iyong preferred na language folder**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Sundin ang README instructions** sa bawat folder para sa:
   - Pag-install ng dependencies
   - Pag-build ng proyekto
   - Pagpapatakbo ng kliyente

3. **Halimbawang output** na dapat mong makita:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para sa kumpletong dokumentasyon at step-by-step na mga tagubilin, tingnan: **[📖 Dokumentasyon ng Solusyon](./solution/README.md)**

## 🎯 Kumpletong Mga Halimbawa

Nagbigay kami ng kumpleto, gumaganang mga implementasyon ng kliyente para sa lahat ng programming languages na tinalakay sa tutorial na ito. Ang mga halimbawang ito ay nagpapakita ng buong functionality na inilarawan sa itaas at maaaring gamitin bilang reference implementations o panimulang punto para sa iyong sariling mga proyekto.

### Available na Kumpletong Mga Halimbawa

| Wika       | File                              | Deskripsyon                                                                 |
|------------|-----------------------------------|-----------------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Kumpletong Java client gamit ang SSE transport na may komprehensibong error handling |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Kumpletong C# client gamit ang stdio transport na may awtomatikong server startup |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kumpletong TypeScript client na may buong suporta sa MCP protocol          |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Kumpletong Python client gamit ang async/await patterns                     |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Kumpletong Rust client gamit ang Tokio para sa async operations            |
### Mga Kumpletong Halimbawa

Bawat kumpletong halimbawa ay naglalaman ng:

- ✅ **Pagbuo ng koneksyon** at paghawak ng error  
- ✅ **Pagdiskubre ng server** (mga tool, resources, prompts kung naaangkop)  
- ✅ **Mga operasyon ng calculator** (add, subtract, multiply, divide, help)  
- ✅ **Pagproseso ng resulta** at maayos na format ng output  
- ✅ **Komprehensibong paghawak ng error**  
- ✅ **Malinis at dokumentadong code** na may mga hakbang-hakbang na komento  

### Pagsisimula sa Mga Kumpletong Halimbawa

1. **Piliin ang iyong gustong wika** mula sa talahanayan sa itaas  
2. **Suriin ang kumpletong file ng halimbawa** upang maunawaan ang buong implementasyon  
3. **Patakbuhin ang halimbawa** ayon sa mga tagubilin sa [`complete_examples.md`](./complete_examples.md)  
4. **I-modify at palawakin** ang halimbawa para sa iyong partikular na gamit  

Para sa detalyadong dokumentasyon tungkol sa pagpapatakbo at pagpapasadya ng mga halimbawang ito, tingnan: **[📖 Dokumentasyon ng Kumpletong Halimbawa](./complete_examples.md)**

### 💡 Solusyon vs. Kumpletong Halimbawa

| **Folder ng Solusyon** | **Kumpletong Halimbawa** |
|-------------------------|--------------------------|
| Buong istruktura ng proyekto na may mga build file | Mga implementasyong nasa iisang file |
| Handa nang patakbuhin kasama ang mga dependency | Nakatuon sa mga halimbawa ng code |
| Setup na parang pang-produksyon | Pang-edukasyong sanggunian |
| Tooling na partikular sa wika | Paghahambing sa iba't ibang wika |

Parehong mahalaga ang dalawang approach - gamitin ang **folder ng solusyon** para sa mga kumpletong proyekto at ang **kumpletong halimbawa** para sa pag-aaral at sanggunian.

## Mahahalagang Punto

Narito ang mga mahahalagang punto para sa kabanatang ito tungkol sa mga kliyente:

- Maaaring gamitin upang parehong magdiskubre at magpatupad ng mga feature sa server.  
- Maaaring magsimula ng server habang sinisimulan ang sarili nito (tulad ng sa kabanatang ito) ngunit maaaring kumonekta rin ang mga kliyente sa mga tumatakbong server.  
- Isang mahusay na paraan upang subukan ang mga kakayahan ng server bukod sa mga alternatibo tulad ng Inspector na tinalakay sa nakaraang kabanata.  

## Karagdagang Mga Mapagkukunan

- [Pagbuo ng mga kliyente sa MCP](https://modelcontextprotocol.io/quickstart/client)

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## Ano'ng Susunod

- Susunod: [Paglikha ng kliyente gamit ang isang LLM](../03-llm-client/README.md)  

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
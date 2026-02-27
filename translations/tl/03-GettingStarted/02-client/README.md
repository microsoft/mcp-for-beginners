# Paglikha ng isang kliyente

Ang mga kliyente ay mga custom na aplikasyon o mga script na direktang nakikipag-ugnayan sa isang MCP Server upang humiling ng mga mapagkukunan, mga kasangkapan, at mga prompt. Hindi tulad ng paggamit ng inspector tool, na nagbibigay ng grapikal na interface para sa pakikipag-ugnayan sa server, ang pagsulat ng sarili mong kliyente ay nagbibigay-daan sa programmatic at awtomatikong mga interaksyon. Pinapayagan nito ang mga developer na isama ang mga kakayahan ng MCP sa kanilang sariling mga workflow, i-automate ang mga gawain, at bumuo ng mga custom na solusyon na angkop sa partikular na pangangailangan.

## Pangkalahatang-ideya

Itinatanghal ng leksyon na ito ang konsepto ng mga kliyente sa loob ng Model Context Protocol (MCP) ecosystem. Matututuhan mo kung paano sumulat ng sarili mong kliyente at ipa-konekta ito sa isang MCP Server.

## Mga Layuning Pantuto

Pagkatapos ng leksyon na ito, magagawa mong:

- Maunawaan kung ano ang magagawa ng isang kliyente.
- Magsulat ng sarili mong kliyente.
- Kumonekta at subukan ang kliyente sa isang MCP server upang matiyak na gumagana ito ayon sa inaasahan.

## Ano ang kailangang gawin sa pagsulat ng isang kliyente?

Upang makasulat ng isang kliyente, kailangan mong gawin ang mga sumusunod:

- **I-import ang tamang mga library**. Gagamitin mo ang parehong library tulad ng dati, ngunit iba lang ang mga konstrukto.
- **Gumawa ng isang kliyente**. Kasama dito ang paglikha ng isang instance ng kliyente at pagkonekta nito sa napiling paraan ng transportasyon.
- **Pumili kung anong mga resources ang ililista**. Ang iyong MCP server ay may mga resources, tools, at prompts, kailangan mong magpasya kung alin ang ililista.
- **Isama ang kliyente sa isang host application**. Kapag alam mo na ang mga kakayahan ng server, kailangan mong isama ito sa iyong host application upang kapag may user na nag-type ng prompt o ibang utos, maipatawag ang kaukulang tampok ng server.

Ngayon na nauunawaan natin sa mataas na antas kung ano ang gagawin natin, tingnan natin ang isang halimbawa.

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

// Ilista ang mga prompt
const prompts = await client.listPrompts();

// Kumuha ng isang prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Ilista ang mga mapagkukunan
const resources = await client.listResources();

// Basahin ang isang mapagkukunan
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
```

Sa naunang code ay:

- Inimport ang mga library
- Nilikha ang isang instance ng kliyente at kinonekta ito gamit ang stdio bilang transport.
- Nilista ang prompts, resources, at tools at pinatakbo ang lahat.

Narito na, isang kliyenteng maaaring makipag-usap sa isang MCP Server.

Maglalaan tayo ng oras sa susunod na seksyon ng pagsasanay upang hatiin ang bawat bahagi ng code at ipaliwanag kung ano ang nangyayari.

## Pagsasanay: Pagsulat ng isang kliyente

Tulad ng nasabi sa itaas, maglaan tayo ng oras sa pagpapaliwanag ng code, at malayang mag-code kasabay kung nais mo.

### -1- Pag-import ng mga library

I-import natin ang mga kinakailangang library, kakailanganin natin ang mga reperensya sa isang kliyente at sa napiling transport protocol, stdio. Ang stdio ay isang protocol para sa mga bagay na tatakbo sa iyong lokal na makina. Ang SSE ay isa pang transport protocol na ipapakita natin sa mga susunod na kabanata ngunit iyon ang isa pang opsyon mo. Sa ngayon, magpatuloy tayo gamit ang stdio.

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

Para sa Java, gagawa ka ng kliyente na nakakonekta sa MCP server mula sa nakaraang pagsasanay. Gamit ang parehong istruktura ng Java Spring Boot project mula sa [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), gumawa ng bagong Java class na tinatawag na `SDKClient` sa folder na `src/main/java/com/microsoft/mcp/sample/client/` at idagdag ang mga sumusunod na import:

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

Kailangan mong idagdag ang mga sumusunod na dependencies sa iyong file na `Cargo.toml`.

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

Mula doon, maaari mong i-import ang mga kinakailangang library sa iyong code ng kliyente.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Tumingin tayo sa pag-iinstansya.

### -2- Pag-iinstansya ng kliyente at transport

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

- Nilikha ang isang stdio transport instance. Tingnan kung paano nito tinutukoy ang command at args para hanapin at paandarin ang server dahil ito ang gagawin natin bilang bahagi ng paggawa ng kliyente.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Ininstansya ang isang kliyente sa pamamagitan ng pagbibigay nito ng pangalan at bersyon.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Kinonekta ang kliyente sa napiling transport.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Lumikha ng mga parametro ng server para sa koneksyon ng stdio
server_params = StdioServerParameters(
    command="mcp",  # Magagamit
    args=["run", "server.py"],  # Opsyonal na mga argumento sa command line
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
- Ininstansya ang isang server parameters object dahil gagamitin natin ito sa pagpapatakbo ng server para makapag-connect ang kliyente natin.
- Tinukoy ang isang method na `run` na siyang tumatawag sa `stdio_client` na nagsisimula ng session ng kliyente.
- Nilikha ang isang entry point kung saan ibinibigay natin ang method na `run` sa `asyncio.run`.

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
- Gumawa ng stdio transport at ng isang kliyenteng `mcpClient`. Ito ang gagamitin natin upang ilista at tawagin ang mga tampok ng MCP Server.

Paalala, sa "Arguments", maaari kang tumukoy sa *.csproj* o sa executable.

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
        
        // Ang lohika ng iyong kliyente ay dito ginagawa
    }
}
```

Sa naunang code ay:

- Nilikha ang main method na nagse-set up ng SSE transport na nakaturo sa `http://localhost:8080` kung saan tatakbo ang ating MCP server.
- Nilikha ang isang client class na tumatanggap ng transport bilang constructor parameter.
- Sa `run` method, gumagawa tayo ng synchronous MCP client gamit ang transport at initialize ang koneksyon.
- Ginamit ang SSE (Server-Sent Events) transport na angkop para sa HTTP-based na komunikasyon sa mga Java Spring Boot MCP servers.

#### Rust

Pansinin na ang Rust client na ito ay nagpapalagay na ang server ay isang katabing proyekto na may pangalang "calculator-server" sa parehong directory. Ang code sa ibaba ay magpapaandar ng server at magkokonekta dito.

```rust
async fn main() -> Result<(), RmcpError> {
    // Ipagpalagay na ang server ay isang kapatid na proyekto na pinangalanang "calculator-server" sa parehong direktoryo
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

    // TODO: I-initialize

    // TODO: Ilahad ang mga kasangkapan

    // TODO: Tawagin ang add tool na may mga argumento = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Paglilista ng mga tampok ng server

Ngayon, mayroon na tayong kliyente na maaaring kumonekta kapag pinatakbo ang programa. Ngunit hindi nito inililista ang mga tampok nito kaya gawin natin iyon ngayon:

#### TypeScript

```typescript
// Ilahad ang mga prompt
const prompts = await client.listPrompts();

// Ilahad ang mga mapagkukunan
const resources = await client.listResources();

// ilahad ang mga kasangkapan
const tools = await client.listTools();
```

#### Python

```python
# Ilista ang mga magagamit na pinagkukunan
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Ilista ang mga magagamit na kagamitan
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Dito inililista natin ang mga available na resources, `list_resources()` at tools, `list_tools` at inilalathala ang mga ito.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Sa itaas ay isang halimbawa kung paano natin maililista ang mga tools sa server. Para sa bawat tool, inilalathala natin ang pangalan nito.

#### Java

```java
// Ilista at ipakita ang mga kasangkapan
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Maaari mo ring i-ping ang server upang tiyakin ang koneksyon
client.ping();
```

Sa naunang code ay:

- Tinawag ang `listTools()` upang makuha lahat ng available na tools mula sa MCP server.
- Ginamit ang `ping()` upang beripikahin na gumagana ang koneksyon sa server.
- Ang `ListToolsResult` ay naglalaman ng impormasyon tungkol sa lahat ng tools kabilang ang kanilang mga pangalan, paglalarawan, at input schemas.

Magaling, ngayon ay nakalista na natin lahat ng tampok. Ngayon, kailan natin ito gagamitin? Ang kliyenteng ito ay simple lang, nangangahulugan na kailangan natin tawagin nang tahasan ang mga tampok kapag gusto natin silang gamitin. Sa susunod na kabanata, gagawa tayo ng mas advanced na kliyente na may access sa sarili nitong malaking language model, LLM. Sa ngayon, tingnan natin kung paano tawagin ang mga tampok sa server:

#### Rust

Sa main function, pagkatapos i-initialize ang kliyente, maaari nating i-initialize ang server at ilista ang ilan sa mga tampok nito.

```rust
// Simulan
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Itala ang mga kasangkapan
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Pagtawag ng mga tampok

Upang tawagin ang mga tampok kailangan nating siguraduhin na tinutukoy natin ang tamang mga argumento at sa ilang kaso ang pangalan ng tinatawag natin.

#### TypeScript

```typescript

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

// tawagan ang prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Sa naunang code ay:

- Binasa ang isang resource, tinawag ang resource sa pamamagitan ng pagtawag sa `readResource()` na may tinukoy na `uri`. Ganito ang hitsura nito sa server side:

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

    Ang ating `uri` na halaga na `file://example.txt` ay tumutugma sa `file://{name}` sa server. Ang `example.txt` ay imap-map sa `name`.

- Tinawag ang isang tool, tinawag ito sa pamamagitan ng pagtukoy ng `name` at mga `arguments` tulad nito:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Kumuha ng prompt, upang makakuha ng prompt, tinawag ang `getPrompt()` na may `name` at `arguments`. Ganito ang hitsura ng server code:

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

    at ang iyong kliyenteng code bilang resulta ay ganito upang tumugma sa deklarasyon sa server:

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
# Basahin ang isang pinagkukunan
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Tawagan ang isang kasangkapan
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Sa naunang code ay:

- Tinawag ang isang resource na tinatawag na `greeting` gamit ang `read_resource`.
- Tinawag ang isang tool na tinatawag na `add` gamit ang `call_tool`.

#### .NET

1. Magdagdag tayo ng code upang tawagan ang isang tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Upang iprint ang resulta, heto ang code para hawakan iyon:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Tawagan ang iba't ibang mga tool ng kalkuladora
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

- Tinawag ang maraming calculator tools gamit ang `callTool()` method na may mga `CallToolRequest` objects.
- Bawat tawag sa tool ay nagtutukoy ng pangalan ng tool at isang `Map` ng mga argumentong kailangan ng tool.
- Inaasahan ng mga tools sa server ang mga tiyak na pangalan ng parameter (tulad ng "a", "b" para sa mga operasyong matematika).
- Ang mga resulta ay ibinabalik bilang mga `CallToolResult` objects na naglalaman ng tugon mula sa server.

#### Rust

```rust
// Tawagin ang add tool na may mga argumento = {"a": 3, "b": 2}
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

Upang patakbuhin ang kliyente, i-type ang sumusunod na utos sa terminal:

#### TypeScript

Idagdag ang sumusunod na entry sa seksyon ng "scripts" sa iyong *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Patakbuhin ang kliyente gamit ang sumusunod na utos:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Siguruhing tumatakbo ang iyong MCP server sa `http://localhost:8080`. Pagkatapos patakbuhin ang kliyente:

```bash
# Ibuo ang iyong proyekto
./mvnw clean compile

# Patakbuhin ang kliyente
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Bilang alternatibo, maaari mong patakbuhin ang kumpletong client project na ibinigay sa solution folder na `03-GettingStarted\02-client\solution\java`:

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

## Takdang-Aralin

Sa takdang-aralin na ito, gagamitin mo ang iyong natutunan sa paggawa ng kliyente ngunit gagawa ka ng sarili mong kliyente.

Narito ang isang server na maaari mong gamitin na kailangang tawagan gamit ang iyong kliyenteng code, tingnan kung maaari kang magdagdag ng mas maraming feature sa server upang maging mas kawili-wili ito.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Gumawa ng isang MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Magdagdag ng isang addition tool
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

// Simulan ang pagtanggap ng mga mensahe sa stdin at pagpapadala ng mga mensahe sa stdout

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

# Lumikha ng isang MCP server
mcp = FastMCP("Demo")


# Magdagdag ng isang karagdagang tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Magdagdag ng isang dynamic na pagbati na mapagkukunan
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

Gayundin, tingnan ang link na ito para sa kung paano tawagin ang [prompts at resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Sa [nakaunang seksyon](../../../../03-GettingStarted/01-first-server), natutunan mo kung paano gumawa ng simpleng MCP server gamit ang Rust. Maaari kang magpatuloy na bumuo doon o tingnan ang link na ito para sa iba pang mga Rust-based na halimbawa ng MCP server: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solusyon

Ang **solution folder** ay naglalaman ng kumpletong, handa nang patakbuhin na mga implementasyon ng kliyente na nagpapakita ng lahat ng mga konseptong natalakay sa tutorial na ito. Bawat solusyon ay naglalaman ng parehong client at server code na nakaayos sa hiwalay at kumpletong mga proyekto.

### 📁 Istruktura ng Solusyon

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

Bawat solusyon na nakatuon sa wika ay nagbibigay ng:

- **Kumpletong implementasyon ng kliyente** na may lahat ng mga tampok mula sa tutorial
- **Gumaganang istruktura ng proyekto** na may tamang mga dependency at configuration
- **Mga script para sa pag-build at pag-run** para sa madaling pag-setup at pagpapatakbo
- **Detalyadong README** na may mga tagubilin para sa partikular na wika
- **Pag-handle ng error** at mga halimbawa ng pagproseso ng resulta

### 📖 Paggamit ng mga Solusyon

1. **Pumunta sa folder ng nais mong programming language**:

   ```bash
   cd solution/typescript/    # Para sa TypeScript
   cd solution/java/          # Para sa Java
   cd solution/python/        # Para sa Python
   cd solution/dotnet/        # Para sa .NET
   ```

2. **Sundin ang mga tagubilin sa README sa bawat folder para sa:**
   - Pag-install ng mga dependency
   - Pagbuo ng proyekto
   - Pagpapatakbo ng kliyente

3. **Halimbawa ng output** na dapat mong makita:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Para sa kumpletong dokumentasyon at mga hakbang-hakbang na tagubilin, tingnan ang: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 Kumpletong Mga Halimbawa

Nagbigay kami ng kumpleto at gumaganang mga implementasyon ng kliyente para sa lahat ng programming languages na natalakay sa tutorial na ito. Ipinapakita ng mga halimbawang ito ang buong functionality na inilarawan sa itaas at maaaring magamit bilang mga reference implementation o panimulang punto para sa iyong sariling mga proyekto.

### Mga Available na Kumpletong Halimbawa

| Wika     | File                          | Paglalarawan                                                    |
|----------|-------------------------------|----------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | Kumpletong Java client gamit ang SSE transport na may komprehensibong pag-handle ng error |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | Kumpletong C# client gamit ang stdio transport na may awtomatikong pagsisimula ng server  |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Kumpletong TypeScript client na may buong suporta sa MCP protocol |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)     | Kumpletong Python client gamit ang async/await na pattern       |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | Kumpletong Rust client gamit ang Tokio para sa asynchronous na operasyon |

Bawat kumpletong halimbawa ay naglalaman ng:
- ✅ **Pagkakatatag ng koneksyon** at paghawak ng error
- ✅ **Pagdiskubre ng server** (mga kasangkapan, mapagkukunan, prompt kung naaangkop)
- ✅ **Mga operasyon ng calculator** (dagdag, bawas, multiplikasyon, hati, tulong)
- ✅ **Pagproseso ng resulta** at pormat na output
- ✅ **Komprehensibong paghawak ng error**
- ✅ **Malinis, dokumentadong code** na may mga komento hakbang-hakbang

### Pagsisimula gamit ang Kumpletong mga Halimbawa

1. **Pumili ng iyong paboritong wika** mula sa talaan sa itaas
2. **Suriin ang kumpletong halimbawa** upang maunawaan ang buong implementasyon
3. **Patakbuhin ang halimbawa** ayon sa mga tagubilin sa [`complete_examples.md`](./complete_examples.md)
4. **Baguhin at palawakin** ang halimbawa para sa iyong partikular na gamit

Para sa detalyadong dokumentasyon tungkol sa pagpapatakbo at pagpapasadya ng mga halimbawang ito, tingnan: **[📖 Kumpletong Dokumentasyon ng mga Halimbawa](./complete_examples.md)**

### 💡 Solusyon kumpara sa Kumpletong mga Halimbawa

| **Folder ng Solusyon** | **Kumpletong Mga Halimbawa** |
|-----------------------|-----------------------------|
| Buong estruktura ng proyekto kasama ang mga build file | Mga single-file na implementasyon |
| Handa nang patakbuhin kasama ang mga dependency | Mga naka-pokus na halimbawa ng code |
| Setup na parang production | Pang-edukasyong sanggunian |
| Tooling na para sa partikular na wika | Paghahambing ng maraming wika |

Parehong mahalaga ang dalawang pamamaraan - gamitin ang **folder ng solusyon** para sa kumpletong mga proyekto at ang **kumpletong mga halimbawa** para sa pag-aaral at sanggunian.

## Pangunahing Mga Natutunan

Ang pangunahing mga natutunan para sa kabanatang ito tungkol sa mga kliyente:

- Maaaring gamitin upang parehong madiskubre at ma-invoke ang mga tampok sa server.
- Maaaring magsimula ng server habang nagsisimula rin ito mismo (gaya sa kabanatang ito) ngunit maaaring kumonekta ang mga kliyente sa mga tumatakbong server.
- Isang mahusay na paraan upang subukan ang mga kakayahan ng server kasabay ng mga alternatibo tulad ng Inspector na inilalarawan sa nakaraang kabanata.

## Karagdagang Mga Mapagkukunan

- [Pagbuo ng mga kliyente sa MCP](https://modelcontextprotocol.io/quickstart/client)

## Mga Sample

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Ano ang Susunod

- Susunod: [Paglikha ng kliyente gamit ang LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't aming pinagsisikapan ang katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring may mga pagkakamali o di-pagsinop. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagmulan ng katotohanan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
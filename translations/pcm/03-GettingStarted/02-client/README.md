# How to make client

Client na custom app or script wey dey talk directly wit MCP Server to ask for resources, tools, and prompts. E different from inspector tool wey dey use graphical interface to interact wit server. If you write your own client, e go allow you do programmatic and automated interactions. Dis one go help developers put MCP features inside dia own workflow, automate tasks, and build custom solution wey fit dia specific needs.

## Overview

Dis lesson go show you wetin client mean for Model Context Protocol (MCP) ecosystem. You go learn how to write your own client and connect am to MCP Server.

## Wetin you go learn

By the time you finish dis lesson, you go sabi:

- Understand wetin client fit do.
- Write your own client.
- Connect and test di client wit MCP server to make sure say e dey work well.

## Wetin you need to write client?

To write client, you go need do di following:

- **Import di correct libraries**. You go use di same library as before, but na different constructs.
- **Create client instance**. You go create client instance and connect am to di transport method wey you choose.
- **Decide wetin resources to list**. Your MCP server get resources, tools, and prompts, you go need decide which one to list.
- **Put di client inside host application**. Once you sabi di server features, you go need put am inside your host application so dat if user type prompt or command, di server feature go respond.

Now we don understand wetin we wan do, make we look example next.

### Example client

Make we check dis example client:

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

For di code wey dey above:

- We import di libraries.
- We create client instance and connect am using stdio for transport.
- We list prompts, resources, and tools, then invoke dem.

You don get client wey fit talk to MCP Server.

Make we take time for di next exercise section to break down each code snippet and explain wetin dey happen.

## Exercise: How to write client

As we don talk before, make we take time explain di code, and if you wan code along, feel free.

### -1- Import di libraries

Make we import di libraries wey we need. We go need reference to client and di transport protocol wey we choose, stdio. Stdio na protocol for things wey dey run for your local machine. SSE na another transport protocol we go show for future chapters, but na your other option. For now, make we continue wit stdio.

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

For Java, you go create client wey go connect to MCP server from di previous exercise. Using di same Java Spring Boot project structure from [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), create new Java class wey dem call `SDKClient` inside `src/main/java/com/microsoft/mcp/sample/client/` folder and add di following imports:

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

You go need add di following dependencies to your `Cargo.toml` file.

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

From there, you fit import di libraries wey you need inside your client code.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Make we move to instantiation.

### -2- How to create client and transport

We go need create transport instance and client instance:

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

For di code wey dey above:

- We create stdio transport instance. Check how e specify command and args to find and start di server, na wetin we go need do as we dey create di client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- We create client by giving am name and version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- We connect di client to di transport wey we choose.

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

For di code wey dey above:

- We import di libraries wey we need.
- We create server parameters object wey we go use to run di server so we fit connect am wit our client.
- We define method `run` wey dey call `stdio_client` wey dey start client session.
- We create entry point wey dey provide `run` method to `asyncio.run`.

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

For di code wey dey above:

- We import di libraries wey we need.
- We create stdio transport and client `mcpClient`. Na di client we go use to list and invoke features for MCP Server.

Note, for "Arguments", you fit point to di *.csproj* or di executable.

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

For di code wey dey above:

- We create main method wey set up SSE transport wey dey point to `http://localhost:8080` where our MCP server go dey run.
- We create client class wey dey take transport as constructor parameter.
- For di `run` method, we create synchronous MCP client using di transport and initialize di connection.
- We use SSE (Server-Sent Events) transport wey dey good for HTTP-based communication wit Java Spring Boot MCP servers.

#### Rust

Dis Rust client dey assume say di server na sibling project wey dem call "calculator-server" for di same directory. Di code below go start di server and connect to am.

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

### -3- How to list server features

Now, we don get client wey fit connect if di program dey run. But e never list di features, so make we do dat next:

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

Here we dey list di available resources, `list_resources()` and tools, `list_tools` and print dem out.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Di code above na example of how we fit list di tools for di server. For each tool, we go print di name.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

For di code wey dey above:

- We call `listTools()` to get all di tools wey dey MCP server.
- We use `ping()` to check say di connection to di server dey work.
- Di `ListToolsResult` get info about all di tools including dia names, descriptions, and input schemas.

Good, now we don capture all di features. Di question na when we go use dem? Dis client dey simple, simple in di sense say we go need call di features directly when we want dem. For di next chapter, we go create more advanced client wey get access to e own large language model, LLM. For now, make we see how we fit invoke di features for di server:

#### Rust

For di main function, after we initialize di client, we fit initialize di server and list some of e features.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- How to invoke features

To invoke di features, we need make sure say we specify di correct arguments and sometimes di name of wetin we dey try invoke.

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

For di code wey dey above:

- We read resource, we dey call di resource by calling `readResource()` wey dey specify `uri`. Na wetin e go look like for di server side:

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

    Our `uri` value `file://example.txt` dey match `file://{name}` for di server. `example.txt` go match `name`.

- We call tool, we dey call am by specifying e `name` and e `arguments` like dis:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- We get prompt, to get prompt, you go call `getPrompt()` wit `name` and `arguments`. Di server code dey look like dis:

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

    and your client code go look like dis to match wetin dey declared for di server:

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

For di code wey dey above:

- We call resource wey dem call `greeting` using `read_resource`.
- We invoke tool wey dem call `add` using `call_tool`.

#### .NET

1. Make we add code to call tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. To print di result, here na code to handle dat:

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

For di code wey dey above:

- We call multiple calculator tools using `callTool()` method wit `CallToolRequest` objects.
- Each tool call dey specify di tool name and `Map` of arguments wey di tool need.
- Di server tools dey expect specific parameter names (like "a", "b" for math operations).
- Results dey return as `CallToolResult` objects wey get di response from di server.

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

### -5- How to run di client

To run di client, type di following command for terminal:

#### TypeScript

Add di following entry to your "scripts" section for *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Call di client wit di following command:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

First, make sure say your MCP server dey run for `http://localhost:8080`. Then run di client:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Or you fit run di complete client project wey dey di solution folder `03-GettingStarted\02-client\solution\java`:

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

## Assignment

For dis assignment, you go use wetin you don learn to create your own client.

Here na server you fit use wey you need call via your client code, try add more features to di server to make am more interesting.

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

Check dis project to see how you fit [add prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Also, check dis link for how to invoke [prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

For di [previous section](../../../../03-GettingStarted/01-first-server), you don learn how to create simple MCP server wit Rust. You fit continue to build on dat or check dis link for more Rust-based MCP server examples: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solution

Di **solution folder** get complete, ready-to-run client implementations wey dey show all di concepts wey dis tutorial cover. Each solution get both client and server code wey dey organized inside separate, self-contained projects.

### 📁 Solution Structure

Di solution directory dey organized by programming language:

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

### 🚀 Wetin Each Solution Get

Each language-specific solution dey provide:

- **Complete client implementation** wit all di features wey dis tutorial cover
- **Working project structure** wit correct dependencies and configuration
- **Build and run scripts** wey dey easy to set up and execute
- **Detailed README** wit language-specific instructions
- **Error handling** and result processing examples

### 📖 How to Use di Solutions

1. **Enter di folder for di language wey you prefer**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Follow di README instructions** for each folder to:
   - Install dependencies
   - Build di project
   - Run di client

3. **Example output** wey you suppose see:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For complete documentation and step-by-step instructions, check: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 Complete Examples

We don provide complete, working client implementations for all di programming languages wey dis tutorial cover. Dis examples dey show di full functionality wey we don talk about and fit serve as reference implementations or starting points for your own projects.

### Available Complete Examples

| Language | File | Description |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Complete Java client wey dey use SSE transport wit better error handling |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Complete C# client wey dey use stdio transport wit automatic server startup |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Complete TypeScript client wit full MCP protocol support |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Complete Python client wey dey use async/await patterns |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Complete Rust client wey dey use Tokio for async operations |

Each complete example get:

- ✅ **Connection setup** and error handling
- ✅ **Server discovery** (tools, resources, prompts where applicable)
- ✅ **Calculator operations** (add, subtract, multiply, divide, help)
- ✅ **Result processing** and formatted output
- ✅ **Comprehensive error handling**
- ✅ **Clean, documented code** wey get step-by-step comments

### How to Start wit Complete Examples

1. **Pick di language wey you like** from di table wey dey up
2. **Check di complete example file** to sabi how di full implementation take work
3. **Run di example** follow di instructions wey dey inside [`complete_examples.md`](./complete_examples.md)
4. **Change and add your own** for di example to fit your own use case

If you wan see full gist about how to run and customize dis examples, check here: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 Solution vs. Complete Examples

| **Solution Folder** | **Complete Examples** |
|--------------------|--------------------- |
| Full project structure wey get build files | Single-file implementations |
| E dey ready to run wit dependencies | E dey focus on code examples |
| E be like production setup | E dey for learning and reference |
| Language-specific tools | Cross-language comparison |

Both methods dey useful - use di **solution folder** for full projects and di **complete examples** for learning and reference.

## Wetin You Go Learn

Di main things wey you go learn for dis chapter about clients na:

- You fit use am to find and use features wey dey for di server.
- E fit start server as e dey start itself (like for dis chapter) but clients fit still connect to servers wey don dey run already.
- E be better way to test server capabilities join other options like di Inspector wey dem talk about for di last chapter.

## Extra Resources

- [How to build clients for MCP](https://modelcontextprotocol.io/quickstart/client)

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Wetin Go Happen Next

- Next: [How to create client wit LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, na beta make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
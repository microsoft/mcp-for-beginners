# Di how to create client

Clients na custom apps or scripts wey dey yarn directly with MCP Server to request resources, tools, and prompts. E no be like how inspector tool dey work wey get graphical interface to dey interact with di server, but wen you write your own client e go allow programmatic and automated ways to yarn with server. This fit help developers to connect MCP features with dia own workflows, make work automatic, and build custom solutions wey fit better for wetin dem need.

## Overview

Dis lesson go show you wetin client mean for Model Context Protocol (MCP) world. You go learn how to write your own client and connect am to MCP Server.

## Wetin you go learn

By di time you finish dis lesson, you go fit:

- Understand wetin client fit do.
- Write your own client.
- Connect am and test di client with MCP server to make sure e dey work well.

## Wetin e mean to write client?

To write client, you go need do dis kain things:

- **Import di correct libraries**. You go dey use di same library as before, but with different way.
- **Make client instance**. You go create client and connect to di transport method wey you choose.
- **Choose wetin resources to list**. Your MCP server get resources, tools and prompts, you get to choose which one to list.
- **Join the client to host app**. Once you sabi wetin server fit do, you go join am to your host app so that wen user type prompt or command the correct server feature go start.

Now we don understand di high level tori, mek we check example next.

### Sample client

Make we look dis sample client:

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

// Make list of prompts
const prompts = await client.listPrompts();

// Collect one prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Make list of resources
const resources = await client.listResources();

// Read one resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Use one tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

For di code wey come before, we:

- Import libraries
- Create client instance and connect am with stdio transport.
- List prompts, resources and tools and call dem all.

Na so e be, one client wey fit talk with MCP Server.

Make we take time for di next exercise to break code small small and explain wetin dey happen.

## Exercise: How to write client

Like we talk before, make we explain code well, also if you want you fit code along.

### -1- Import di libraries

Make we import di libraries we need, we go need reference to client and transport protocol wey be stdio. Stdio na protocol for things wey go run for your local machine. SSE na another transport we go show later for next chapters but na your second option. For now, mek we continue with stdio.

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

For Java, you go create client wey go connect to MCP server from previous exercise. Use di same Java Spring Boot project structure wey dey [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), create new Java class wey dem go call `SDKClient` for `src/main/java/com/microsoft/mcp/sample/client/` folder and put dis imports:

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

You go need add dis dependencies to your `Cargo.toml` file.

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

From there, you fit import libraries wey client code go need.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Make we continue to instantiation.

### -2- How to instantiate client and transport

We go create instance of transport plus client:

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

For dis code we:

- Create stdio transport instance. See how e talk command and args so that e fit find and start server as we dey create client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Create client give am name and version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Connect client to transport we choose.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Make server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Di executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Begin di connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

For di code before:

- Import needed libraries
- Create server parameters object to run server so client fit connect.
- Define `run` method wey call `stdio_client` to start client session.
- Create entry point to pass `run` method to `asyncio.run`.

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

For di code before, we:

- Import libraries
- Create stdio transport, create client `mcpClient` wey we go use list and call server features.

Note, for "Arguments", you fit point to *.csproj* or executable.

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
        
        // Your client logic deya for here
    }
}
```

For di code before, we:

- Create main method to setup SSE transport point to `http://localhost:8080` wey MCP server go dey run.
- Create client class wey take transport as constructor param.
- For `run` method, create synchronous MCP client with transport and start connection.
- Use SSE transport wey fit HTTP comot Java Spring Boot MCP servers.

#### Rust

Note say dis Rust client dey assume server be sibling project called "calculator-server" for same directory. Di code below go start server and connect to am.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume say di server na one padi project we dem name "calculator-server" for di same folder
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

    // TODO: Make e start

    // TODO: Show list of tools

    // TODO: Call add tool wit arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- How to list server features

Now we get client wey fit connect if program run. But e no dey list features yet so make we do dat:

#### TypeScript

```typescript
// Mak list of prompts
const prompts = await client.listPrompts();

// Mak list of resources
const resources = await client.listResources();

// mak list of tools
const tools = await client.listTools();
```

#### Python

```python
# List di resources wey dey available
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List di tools wey dey available
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

For here, we list things wey dey resources, `list_resources()` and tools, `list_tools` and print dem.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Dis one na example how we fit list tools for server. For each tool, we go print im name.

#### Java

```java
// List and show how tool dem dey work
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You fit still ping di server to check say connection dey okay
client.ping();
```

For di code before, we:

- Call `listTools()` to get all tools wey server get.
- Use `ping()` to confirm connection to server dey alright.
- `ListToolsResult` get info on all tools like names, descriptions, and input schemas.

Good, now we don catch all features. But question be when we go use dem? Well, dis client simple, meaning we go need call features direct when we want dem. For next chapter, we go create better client wey get own large language model, LLM. For now, mek we see how to call features for server:

#### Rust

For main function, after client initialization, we fit also start server and list some features.

```rust
// Start am
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Make list of tools dem
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- How to invoke features

To invoke features, we need to give correct arguments and sometimes name of wetin we wan invoke.

#### TypeScript

```typescript

// Read wan resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call one tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// Call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

For di code before, we:

- Read resource, we call am by `readResource()` give `uri`. Na so e go look for server side:

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

    Our `uri` value `file://example.txt` match `file://{name}` for server. `example.txt` go be `name`.

- Call tool, we call am by `name` and `arguments` like this:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Get prompt, to get prompt, you call `getPrompt()` with `name` and `arguments`. Server code be dis:

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

    Your client code go fine well to match wetin server talk:

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
# Read wan resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call wan tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

For code before, we:

- Call resource wey dem call `greeting` with `read_resource`.
- Call tool named `add` with `call_tool`.

#### .NET

1. Add code to call tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. To print result, dis code fit handle am:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call different calculator tool dem
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

For code before, we:

- Call many calculator tools with `callTool()` method and `CallToolRequest` objects.
- Each tool call get tool name and `Map` of arguments wey tool need.
- Server tools expect specific param names (like "a", "b" for math).
- Results return as `CallToolResult` objects with server response.

#### Rust

```rust
// Call add tool wit arguments = {"a": 3, "b": 2}
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

### -5- How to run the client

To run client, type dis command for terminal:

#### TypeScript

Add dis entry to your "scripts" for *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Call client with dis command:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

First make sure your MCP server dey run for `http://localhost:8080`. Then run client:

```bash
# Build your project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Or you fit run complete client project for solution folder `03-GettingStarted\02-client\solution\java`:

```bash
# Comot go the solution folder
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

For dis assignment, you go use wetin you learn to create client but do am your own way.

Here na server wey you fit use wey you need call with your client code, try add more features to di server to make am more beta.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Mak MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add one addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add one dynamic greeting resource
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

// Begin to dey receive messages for stdin and dey send messages for stdout

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

# Make one MCP server
mcp = FastMCP("Demo")


# Add one tool wey dey do addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add one resource wey fit change how e dey greet people
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

Check dis project to see how to [add prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Also check dis link on how to call [prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

For [previous section](../../../../03-GettingStarted/01-first-server), you learn how to create simple MCP server with Rust. You fit build on top or check dis link for more Rust MCP server examples: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solution

Di **solution folder** get full ready-to-run client implementations wey show all tins we cover for dis tutorial. Each solution get both client and server code inside separate projects wey stand alone.

### 📁 Solution Structure

Di solution folder organize by programming language:

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

### 🚀 Wetin each solution get

Each language solution get:

- **Complete client implementation** with all di tutorial features
- **Working project structure** with dependencies and config correct
- **Build and run scripts** for easy setup and run
- **Detailed README** with language instructions
- **Error handling** and result example

### 📖 How to use solutions

1. **Go your language folder**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Follow README instruction** for:
   - Install dependencies
   - Build project
   - Run client

3. **Wetin you go see output**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For full docs and step by step, see: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 Complete Examples

We provide full working client implementations for all language we cover here. Dem examples show full features wey we talk about and fit use as reference or starting project.

### Available Complete Examples

| Language | File | Description |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Complete Java client wey use SSE transport with full error handling |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Complete C# client with stdio transport wey fit start server automatically |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Complete TypeScript client with full MCP protocol support |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Complete Python client wey use async/await pattern |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Complete Rust client using Tokio for async work |

Each example get:

- ✅ **Connection setting and error handling**
- ✅ **Server discoveries** (tools, resources, prompts where dem dey)
- ✅ **Calculator operations** (add, substract, multiply, divide, help)
- ✅ **Result processing** and nice output
- ✅ **Full error handling**

- ✅ **Clean, documented code** wit step-by-step comments

### How to Start wit Complete Examples

1. **Choose di language wey you like** from di table we dey above
2. **Look di complete example file** to sabi di full implementation
3. **Run di example** by di instructions wey dey for [`complete_examples.md`](./complete_examples.md)
4. **Change and add** more tins to di example for your own case

For detailed documentation about how to run and change these examples, see: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 Solution vs. Complete Examples

| **Solution Folder** | **Complete Examples** |
|--------------------|--------------------- |
| Whole project structure wit build files | Single-file implementations |
| Ready to run with dependensies | Focused code examples |
| Production-like setup | Educational reference |
| Language-specific tooling | Cross-language comparison |

Both ways dey important - use di **solution folder** for full projects and di **complete examples** for learning and reference.

## Key Takeaways

Di key takeaways for dis chapter na dis about clients:

- Fit use am both to find and call features for di server.
- Fit start a server while e dey start itself (like for dis chapter) but clients fit also connect to servers wey don already start.
- Na beta way to test server ability side by side wit other options like di Inspector as dem talk about for di previous chapter.

## Additional Resources

- [Building clients in MCP](https://modelcontextprotocol.io/quickstart/client)

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Wetin Next

- Next: [Creating a client with an LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Creating a client

Clients na custom applications or scripts wey dey communicate directly wit MCP Server to request resources, tools, an prompts. E no be like when you dey use inspector tool, wey dey give graphical interface to interact wit di server, when you write your own client e allow programmatic an automated interactions. Dis one fit make developers fit integrate MCP capabilities into their own workflow dem, automate tasks, an build custom solutions wey dem tailor to specific needs.

## Overview

Dis lesson go introduce di concept of clients inside di Model Context Protocol (MCP) ecosystem. You go learn how to write your own client and connect am to MCP Server.

## Learning Objectives

By di time dis lesson finish, you go fit:

- Understand wetin client fit do.
- Write your own client.
- Connect and test di client wit MCP server to make sure di latter dey work as e suppose.

## What goes into writing a client?

To write client, you go need do dis tins:

- **Import di correct libraries**. You go dey use di same library as before, na just different constructs.
- **Instantiate a client**. Dis one go mean say you go create client instance and connect am to di transport method wey you choose.
- **Decide wetin to list among resources**. Your MCP server get resources, tools an prompts, you need decide which one to list.
- **Integrate di client into host application**. When you sure wetin di server fit do, you need connect am to your host application so if user type prompt or command, di correct server feature go activate.

Now as we don understand wetin we wan do from top, make we see example next.

### An example client

Make we look dis example client:

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

// Make you get one prompt
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

// Use one tool to call
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Inside di code wey just pass, we:

- Import di libraries
- Create client instance an connect am wit stdio for transport.
- List prompts, resources and tools an invoke all of dem.

Na so we get am, client wey fit talk to MCP Server.

Make we take time for next exercise to break down each code part an explain wetin dey happen.

## Exercise: Writing a client

Like we talk before, make we take time explain di code, an of course code along if you want.

### -1- Import the libraries

Make we import di libraries wey we need, we go need references to client and stdio transport protocol wey we choose. stdio na protocol for things wey dem suppose run for your local machine. SSE na another transport protocol we go show for future chapters but dat na your other option. For now, make we continue wit stdio.

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

For Java, you go create client wey connect to MCP server from previous exercise. Use di same Java Spring Boot project structure from [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), create new Java class named `SDKClient` inside `src/main/java/com/microsoft/mcp/sample/client/` folder an add dis imports:

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

You need add dis dependencies to your `Cargo.toml` file.

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

After dat, you fit import di necessary libraries inside your client code.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Make we move go instantiation.

### -2- Instantiating client and transport

We go need create instance of di transport an that one of our client:

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

For di code wey just pass:

- We create stdio transport instance. Notice how e specify command and args for how to find an start di server since na wetin we go need do as we create client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instantiate client by giving am name an version.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Connect client to di transport wey we choose.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Make server parameters for stdio konnekshon
server_params = StdioServerParameters(
    command="mcp",  # Di tin wey pipo fit run
    args=["run", "server.py"],  # Command line args wey no sure
    env=None,  # Environment variables wey no sure
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Start di konnekshon
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

For di code wey just pass:

- Import di libraries we need
- Instantiate server parameters object because we go use am run server so our client fit connect to am.
- Define method `run` wey go call `stdio_client` wey go start client session.
- Create entry point where we pass `run` method to `asyncio.run`.

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

For di code wey just pass:

- Import di libraries wey we need.
- Create stdio transport and create client `mcpClient`. We go use am list and invoke features on MCP Server.

Note: inside "Arguments", you fit point am to *.csproj* or executable.

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
        
        // Your client logic dey here
    }
}
```

For di code wey just pass:

- Create main method wey setup SSE transport wey dey point to `http://localhost:8080` wey our MCP server go dey run.
- Create client class wey carry transport inside constructor parameter.
- Inside `run` method, we create synchronous MCP client use di transport an initialize di connection.
- Use SSE (Server-Sent Events) transport wey good for HTTP-based communication wit Java Spring Boot MCP servers.

#### Rust

Note say di Rust client assume di server na sibling project wey dem call "calculator-server" for di same directory. Di code down here go start di server and connect to am.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume say di server na one padi projek wey dem call "calculator-server" for di same folder
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

    // TODO: Begin

    // TODO: Show tools dem

    // TODO: Call add tool wit arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listing the server features

Now, we get client wey fit connect to server if program run. But e no dey list im features yet, so make we do dat next:

#### TypeScript

```typescript
// List di prompts dem
const prompts = await client.listPrompts();

// List di resources dem
const resources = await client.listResources();

// List di tools dem
const tools = await client.listTools();
```

#### Python

```python
# Make list of all di resources wey dey
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Make list of all di tools wey dey available
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Here we list resources, `list_resources()` an tools, `list_tools` an print dem out.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Dis na example how we fit list tools on server. For each tool, we print im name.

#### Java

```java
// List and show how tools dey work
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You fit still ping the server make you confirm say connection dey okay
client.ping();
```

For di code wey just pass:

- Call `listTools()` to get all tools wey server get.
- Use `ping()` to check say connection to server dey work.
- `ListToolsResult` get info about all tools like name, description, and input schemas.

Good, now we don capture all features. Now wetin we go do wit dem? Well, dis client simple, e mean say we go need explicitly call features if we want use dem. For the next chapter, we go create more advanced client wey get access to im own large language model, LLM. For now, make we see how to invoke features on server:

#### Rust

For main function, after we initialize client, we fit initialize server an list some features.

```rust
// Make e ready
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Show tools list
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invoke features

To invoke features, we need make sure we specify correct arguments an sometimes di name of wetin we dey try invoke.

#### TypeScript

```typescript

// Read one resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Use tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// use prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

For di code wey just pass:

- We read resource by calling `readResource()` specify `uri`. Dis na how e likely go be for server:

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

    Our `uri` value `file://example.txt` match `file://{name}` for server side. `example.txt` go map to `name`.

- Call tool by specifying `name` and `arguments` like dis:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Get prompt, to get prompt, you call `getPrompt()` wit `name` an `arguments`. Server code look like dis:

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

    So your client code go look like dis to match wetin server declare:

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
# Read di resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call one tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

For di code wey just pass:

- Call resource called `greeting` using `read_resource`.
- Invoke tool called `add` using `call_tool`.

#### .NET

1. Make we add code to call tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. To print result, here code to handle am:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call different calculator tings
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

For di code wey just pass:

- Call many calculator tools using `callTool()` method wit `CallToolRequest` objects.
- Each tool call specify tool name an `Map` of arguments wey tool need.
- Server tools expect specific parameter names (like "a", "b" for math operations).
- Results come back as `CallToolResult` objects wey get server response.

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

### -5- Run the client

To run di client, type command wey follow for terminal:

#### TypeScript

Add dis entry to your "scripts" section inside *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Call client wit dis command:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

First, make sure your MCP server dey run on `http://localhost:8080`. Then run client:

```bash
# Build your project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Or sinon, you fit run di complete client project wey dey solution folder `03-GettingStarted\02-client\solution\java`:

```bash
# waka go di solution folder
cd 03-GettingStarted/02-client/solution/java

# build and run di JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Assignment

For dis assignment, you go use wetin you learn to create client but make e be your own client.

Here na server wey you fit use, you go call am through your client code, try add more features to server to make am more interesting.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Make one MCP server
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

// Add one dey change greeting resource
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

// Begin to receive messages for stdin and send messages for stdout

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


# Add one tool wey dey add
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add one dynamic greeting resource
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

See dis project to see how you fit [add prompts an resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Also, check dis link for how to invoke [prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

For [previous section](../../../../03-GettingStarted/01-first-server), you learn how to create simple MCP server wit Rust. You fit continue build on top dat or check dis link for more Rust-based MCP server examples: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Solution

Di **solution folder** get complete, ready-to-run client implementations wey dey show all di concepts we cover for dis tutorial. Each solution get both client and server code for organized separate, self-contained projects.

### 📁 Solution Structure

Di solution directory organized by programming language:

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

### 🚀 What Each Solution Includes

Each language-specific solution get:

- **Complete client implementation** wit all features from tutorial
- **Working project structure** wit correct dependencies an config
- **Build and run scripts** for easy setup an run
- **Detailed README** wit language-specific instructions
- **Error handling** an result processing examples

### 📖 Using the Solutions

1. **Enter your preferred language folder**:

   ```bash
   cd solution/typescript/    # Na for TypeScript
   cd solution/java/          # Na for Java
   cd solution/python/        # Na for Python
   cd solution/dotnet/        # Na for .NET
   ```

2. **Follow di README instructions** inside each folder for:
   - Installing dependencies
   - Building di project
   - Running di client

3. **Example output** wey you supposed see:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

For full documentation and step-by-step instructions, see: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 Complete Examples

We provide complete, working client implementations for all programming languages wey dis tutorial cover. Dis examples show di full functionality wey we talk about and you fit use as reference or starting points for your own projects.

### Available Complete Examples

| Language | File | Description |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Complete Java client using SSE transport wit strong error handling |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Complete C# client using stdio transport wit automatic server startup |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Complete TypeScript client wit full MCP protocol support |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Complete Python client using async/await patterns |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Complete Rust client using Tokio for async operations |

Each complete example get:
- ✅ **Connection establishment** an error handling
- ✅ **Server discovery** (tools, resources, prompts wey apply)
- ✅ **Calculator operations** (add, subtract, multiply, divide, help)
- ✅ **Result processing** an formatted output
- ✅ **Comprehensive error handling**
- ✅ **Clean, documented code** wit step-by-step comments

### Getting Started wit Complete Examples

1. **Choose your preferred language** from di table above
2. **Review di complete example file** to understand di full implementation
3. **Run di example** follow di instructions inside [`complete_examples.md`](./complete_examples.md)
4. **Modify an extend** di example for your specific use case

For detailed documentation about how to run an customize these examples, check: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 Solution vs. Complete Examples

| **Solution Folder** | **Complete Examples** |
|--------------------|--------------------- |
| Full project structure wit build files | Single-file implementations |
| Ready-to-run wit dependencies | Focused code examples |
| Production-like setup | Educational reference |
| Language-specific tooling | Cross-language comparison |

Both ways dey important - use di **solution folder** for complete projects an di **complete examples** for learning an reference.

## Key Takeaways

Di key takeaways for dis chapter na the following about clients:

- Dem fit use am both to discover an invoke features on di server.
- Dem fit start server while dem start itself (like for dis chapter) but clients fit also connect to server wey dey already dey run.
- E good way to test server capabilities beside alternatives like di Inspector as e describe for di previous chapter.

## Additional Resources

- [Building clients in MCP](https://modelcontextprotocol.io/quickstart/client)

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## What's Next

- Next: [Creating a client with an LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Warning**:
Dis document na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate am. Even though we try make e correct, abeg sabi say automated translation fit get mistake or no too correct. Di original document for im own language na di correct one wey person suppose trust. If e sure or gbege, make human professional translate am. We no go responsible for any wahala or wrong meaning wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
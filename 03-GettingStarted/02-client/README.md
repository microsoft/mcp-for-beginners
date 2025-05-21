# Creating a Client

Clients are custom applications or scripts that communicate directly with an MCP Server to request resources, tools, and prompts. Unlike using the inspector tool, which provides a graphical interface for interacting with the server, writing your own client allows for programmatic and automated interactions. This enables developers to integrate MCP capabilities into their own workflows, automate tasks, and build custom solutions tailored to specific needs.

## Overview

This lesson introduces the concept of clients within the Model Context Protocol (MCP) ecosystem. You'll learn how to write your own client and have it connect to an MCP Server.
 
## Learning Objectives

By the end of this lesson, you will be able to:

- Understand what a client can do.
- Write your own client.
- Connect and test the client with an MCP server to ensure it works as expected.

## What Goes Into Writing a Client?

To write a client, you'll need to do the following:

- **Import the correct libraries.** You'll be using the same library as before, just different constructs.
- **Instantiate a client.** This will involve creating a client instance and connecting it to the chosen transport method.
- **Decide on what resources to list.** Your MCP server comes with resources, tools, and prompts. You need to decide which ones to list.
- **Integrate the client into a host application.** Once you know the capabilities of the server, you need to integrate this into your host application so that if a user types a prompt or other command, the corresponding server feature is invoked.

Now that we understand at a high level what we're about to do, let's look at an example next.

### An Example Client

Let's have a look at this example client:

<details>
<summary>TypeScript</summary>

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client({
  name: "example-client",
  version: "1.0.0"
});

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

</details>

In the preceding code, we:

- Import the libraries.
- Create an instance of a client and connect it using stdio for transport.
- List prompts, resources, and tools, and invoke them all.

There you have it—a client that can talk to an MCP Server.

Let's take our time in the next exercise section and break down each code snippet and explain what's going on.

## Exercise: Writing a Client

As said above, let's take our time explaining the code, and by all means, code along if you want.

### -1- Import the Libraries

Let's import the libraries we need. We will need references to a client and to our chosen transport protocol, stdio. stdio is a protocol for things meant to run on your local machine. SSE is another transport protocol we will show in future chapters, but that's your other option. For now, though, let's continue with stdio. 

<details>
<summary>TypeScript</summary>

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

</details>

<details>
<summary>Python</summary>

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

</details>

<details>
<summary>.NET</summary>

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
```

</details>

Let's move on to instantiation.

### -2- Instantiating Client and Transport

We will need to create an instance of the transport and that of our client:

<details>
<summary>TypeScript</summary>

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client({
  name: "example-client",
  version: "1.0.0"
});

await client.connect(transport);
```

In the preceding code, we've:

- Created an stdio transport instance. Note how it specifies the command and args for how to find and start up the server, as that's something we will need to do as we create the client.
- Instantiated a client by giving it a name and version.
- Connected the client to the chosen transport.

</details>

<details>
<summary>Python</summary>

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

In the preceding code, we've:

- Imported the needed libraries.
- Instantiated a server parameters object, as we will use this to run the server, so we can connect to it with our client.
- Defined a method `run` that in turn calls `stdio_client`, which starts a client session. 
- Created an entry point where we provide the `run` method to `asyncio.run`.

</details>

<details>
<summary>.NET</summary>

```csharp
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

In the preceding code, we've:

- Imported the needed libraries.
- Created an stdio transport and created a client `mcpClient`. The latter is something we will use to list and invoke features on the MCP Server.

Note: In "Arguments", you can either point to the *.csproj* or to the executable.

</details>

### -3- Listing the Server Features

Now, we have a client that can connect to the server when the program is run. However, it doesn't actually list its features, so let's do that next:

<details>
<summary>TypeScript</summary>

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// List tools
const tools = await client.listTools();
```

</details>

<details>
<summary>Python</summary>

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

Here we list the available resources with `list_resources()` and tools with `list_tools`, and print them out.

</details>

<details>
<summary>.NET</summary>

```csharp
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Above is an example of how we can list the tools on the server. For each tool, we then print out its name.

</details>

Great, now we've captured all the features. Now the question is, when do we use them? Well, this client is pretty simple, in the sense that we will need to explicitly call the features when we want them. In the next chapter, we will create a more advanced client that has access to its own large language model (LLM). For now, though, let's see how we can invoke the features on the server:

### -4- Invoke Features

To invoke the features, we need to ensure we specify the correct arguments and, in some cases, the name of what we're trying to invoke.

<details>
<summary>TypeScript</summary>

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

// Call a prompt
const promptResult = await client.getPrompt({
  name: "review-code",
  arguments: {
    code: "console.log(\"Hello world\")"
  }
});
```

In the preceding code, we:

- Read a resource by calling `readResource()` and specifying `uri`. Here's what it most likely looks like on the server side:

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

    Our `uri` value `file://example.txt` matches `file://{name}` on the server. `example.txt` will be mapped to `name`.

- Call a tool by specifying its `name` and its `arguments` like so:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Get a prompt by calling `getPrompt()` with `name` and `arguments`. The server code looks like so:

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

    And your resulting client code therefore, looks like this to match what's declared on the server:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    });
    ```

</details>

<details>
<summary>Python</summary>

```python
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

In the preceding code, we've:

- Called a resource called `greeting` using `read_resource`.
- Invoked a tool called `add` using `call_tool`.

</details>

<details>
<summary>C#</summary>

1. Let's add some code to call a tool:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken: CancellationToken.None);
  ```

2. To print out the result, here's some code to handle that:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

</details>

### -5- Run the Client

To run the client, type the following command in the terminal:

<details>
<summary>TypeScript</summary>

Add the following entry to your "scripts" section in *package.json*:

```json
"client": "tsx && node build/client.js"
```

```sh
npm run client
```

</details>

<details>
<summary>Python</summary>

Call the client with the following command:

```sh
python client.py
```

</details>

<details>
<summary>.NET</summary>

```sh
dotnet run
```

</details>

## Assignment

In this assignment, you'll use what you've learned in creating a client to create a client of your own.

Here's a server you can use that you need to call via your client code. See if you can add more features to the server to make it more interesting.

<details>
<summary>TypeScript</summary>

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an additional tool
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

</details>

<details>
<summary>Python</summary>

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an additional tool
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

</details>

<details>
<summary>.NET</summary>

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

See this project to see how you can [add prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Also, check this link for how to invoke [prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

</details>

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The key takeaways for this chapter about clients:

- Can be used to both discover and invoke features on the server.
- Can start a server while it starts itself (like in this chapter), but clients can connect to running servers as well.
- They are a great way to test out server capabilities next to alternatives like the Inspector, as described in the previous chapter.

## Additional Resources

- [Building clients in MCP](https://modelcontextprotocol.io/quickstart/client)

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../samples/csharp/)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../samples/python/) 

## What's Next

Next: [Creating a client with an LLM](/03-GettingStarted/03-llm-client/README.md)


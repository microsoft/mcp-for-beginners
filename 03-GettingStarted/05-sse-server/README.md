# SSE Server

SSE (Server-Sent Events) is a standard for server-to-client streaming, allowing servers to push real-time updates to clients over HTTP. This is particularly useful for applications that require live updates, such as chat applications, notifications, or real-time data feeds. Your server can also be used by multiple clients at the same time, as it lives on a server that can be run somewhere in the cloud, for example.

## Overview

This lesson covers how to build and consume SSE servers.

## Learning Objectives

By the end of this lesson, you will be able to:

- Build an SSE server.
- Debug an SSE server using the Inspector.
- Consume an SSE server using Visual Studio Code.

## SSE: How It Works

SSE is one of two supported transport types. You've already seen the first one, stdio, used in previous lessons. The differences are as follows:

- SSE requires you to handle two things: connections and messages.
- Since this is a server that can live anywhere, you need to reflect that in how you work with tools like the Inspector and Visual Studio Code. Instead of specifying how to start the server, you point to the endpoint where it can establish a connection. See the example code below:

<details>
<summary>TypeScript</summary>

```typescript
app.get("/sse", async (_: Request, res: Response) => {
    const transport = new SSEServerTransport('/messages', res);
    transports[transport.sessionId] = transport;
    res.on("close", () => {
        delete transports[transport.sessionId];
    });
    await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
    const sessionId = req.query.sessionId as string;
    const transport = transports[sessionId];
    if (transport) {
        await transport.handlePostMessage(req, res);
    } else {
        res.status(400).send('No transport found for sessionId');
    }
});
```

In the preceding code:

- `/sse` is set up as a route. When a request is made to this route, a new transport instance is created and the server connects using this transport.
- `/messages` is the route that handles incoming messages.

</details>

<details>
<summary>Python</summary>

```python
mcp = FastMCP("My App")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
```

In the preceding code:

- You create an instance of an ASGI server (using Starlette specifically) and mount the default route `/`.
- Behind the scenes, the routes `/sse` and `/messages` are set up to handle connections and messages, respectively. The rest of the app, like adding features such as tools, works the same as with the stdio servers.

</details>

<details>
<summary>.NET</summary>

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer()
    .WithTools<Tools>();

builder.Services.AddHttpClient();

var app = builder.Build();

app.MapMcp();
```

There are two methods that help us go from a web server to a web server supporting SSE:

- `AddMcpServer` adds capabilities.
- `MapMcp` adds routes like `/sse` and `/messages`.

</details>

Now that we know a little more about SSE, let's build an SSE server next.

## Exercise: Creating an SSE Server

To create our server, we need to keep two things in mind:

- We need to use a web server to expose endpoints for connections and messages.
- We build our server as usual with tools, resources, and prompts, just like when using stdio.

### -1- Create a Server Instance

To create our server, we use the same types as with stdio. However, for the transport, we need to choose SSE.

<details>
<summary>TypeScript</summary>

```typescript
import express, { Request, Response } from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";

const server = new McpServer({
  name: "example-server",
  version: "1.0.0"
});

const app = express();

const transports: { [sessionId: string]: SSEServerTransport } = {};
```

In the preceding code:

- We created a server instance.
- Defined an app using the web framework Express.
- Created a `transports` variable to store incoming connections.

</details>

<details>
<summary>Python</summary>

```python
from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")
```

In the preceding code:

- We imported the libraries needed, including Starlette (an ASGI framework).
- Created an MCP server instance `mcp`.

</details>

<details>
<summary>.NET</summary>

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();

builder.Services.AddHttpClient();

var app = builder.Build();

// TODO: add routes 
```

At this point:

- We created a web app.
- Added support for MCP features through `AddMcpServer`.

</details>

Let's add the needed routes next.

### -2- Add Routes

Let's add routes to handle the connection and incoming messages:

<details>
<summary>TypeScript</summary>

```typescript
app.get("/sse", async (_: Request, res: Response) => {
  const transport = new SSEServerTransport('/messages', res);
  transports[transport.sessionId] = transport;
  res.on("close", () => {
    delete transports[transport.sessionId];
  });
  await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
  const sessionId = req.query.sessionId as string;
  const transport = transports[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res);
  } else {
    res.status(400).send('No transport found for sessionId');
  }
});

app.listen(3001);
```

In the preceding code:

- `/sse` instantiates a transport of type SSE and calls `connect` on the MCP server.
- `/messages` handles incoming messages.

</details>

<details>
<summary>Python</summary>

```python
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
```

In the preceding code:

- We created an ASGI app instance using the Starlette framework. We passed `mcp.sse_app()` to its list of routes, which mounts `/sse` and `/messages` on the app instance.

</details>

<details>
<summary>.NET</summary>

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();

builder.Services.AddHttpClient();

var app = builder.Build();

app.MapMcp();
```

We added one line of code at the end: `app.MapMcp()`. This means we now have routes `/sse` and `/messages`.

</details>

Let's add capabilities to the server next.

### -3- Adding Server Capabilities

Now that we've got everything SSE-specific defined, let's add server capabilities like tools, prompts, and resources.

<details>
<summary>TypeScript</summary>

```typescript
server.tool("random-joke", "A joke returned by the Chuck Norris API", {},
  async () => {
    const response = await fetch("https://api.chucknorris.io/jokes/random");
    const data = await response.json();

    return {
      content: [
        {
          type: "text",
          text: data.value
        }
      ]
    };
  }
);
```

This tool, "random-joke", calls the Chuck Norris API and returns a JSON response.

</details>

<details>
<summary>Python</summary>

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

Now your server has one tool.

</details>

Your full code should look like this:

<details>
<summary>TypeScript</summary>

```typescript
// server-sse.ts
import express, { Request, Response } from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "example-server",
  version: "1.0.0"
});

const app = express();

const transports: { [sessionId: string]: SSEServerTransport } = {};

app.get("/sse", async (_: Request, res: Response) => {
  const transport = new SSEServerTransport('/messages', res);
  transports[transport.sessionId] = transport;
  res.on("close", () => {
    delete transports[transport.sessionId];
  });
  await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
  const sessionId = req.query.sessionId as string;
  const transport = transports[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res);
  } else {
    res.status(400).send('No transport found for sessionId');
  }
});

server.tool("random-joke", "A joke returned by the Chuck Norris API", {},
  async () => {
    const response = await fetch("https://api.chucknorris.io/jokes/random");
    const data = await response.json();

    return {
      content: [
        {
          type: "text",
          text: data.value
        }
      ]
    };
  }
);

app.listen(3001);
```

</details>

<details>
<summary>Python</summary>

```python
from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
```

</details>

<details>
<summary>.NET</summary>

1. Let's create some tools first. Create a file *Tools.cs* with the following content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;

  namespace server;

  [McpServerToolType]
  public sealed class Tools
  {
      public Tools() { }

      [McpServerTool, Description("Add two numbers together.")]
      public async Task<string> AddNumbers(
          [Description("The first number")] int a,
          [Description("The second number")] int b)
      {
          return (a + b).ToString();
      }
  }
  ```

2. Now, leverage the `Tools` class:

  ```csharp
  var builder = WebApplication.CreateBuilder(args);
  builder.Services
      .AddMcpServer()
      .WithTools<Tools>();

  builder.Services.AddHttpClient();

  var app = builder.Build();

  app.MapMcp();
  ```

</details>

Great, we have a server using SSE. Let's take it for a spin next.

## Exercise: Debugging an SSE Server with Inspector

Inspector is a great tool that we saw in a previous lesson ([Creating your first server](/03-GettingStarted/01-first-server/README.md)). Let's see if we can use the Inspector here:

### -1- Running the Inspector

To run the Inspector, you first must have an SSE server running:

1. Run the server:

    <details>
    <summary>TypeScript</summary>

    ```sh
    tsx && node ./build/server-sse.ts
    ```

    </details>

    <details>
    <summary>Python</summary>

    ```sh
    uvicorn server:app
    ```

    Note: We use the executable `uvicorn` that's installed when you type `pip install "mcp[cli]"`. Typing `server:app` means we're trying to run a file `server.py` and for it to have a Starlette instance called `app`. 
    </details>

    <details>
    <summary>.NET</summary>

    ```sh
    dotnet run
    ```

    This should start the server. To interface with it, you need a new terminal.

    </details>

2. Run the Inspector

    > **NOTE:** Run this in a separate terminal window from where the server is running. Also, you need to adjust the command below to fit the URL where your server runs.

    ```sh
    npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/list
    ```

    Running the Inspector looks the same in all runtimes. Note that instead of passing a path to your server and a command for starting the server, you pass the URL where the server is running and specify the `/sse` route.

### -2- Trying Out the Tool

Connect to the server by selecting SSE in the dropdown and filling in the URL field where your server is running, for example, http://localhost:4321/sse. Now click the "Connect" button. As before, select to list tools, select a tool, and provide input values. You should see a result like below:

![SSE Server running in inspector](./assets/sse-inspector.png)

Great, you're able to work with the Inspector. Let's see how we can work with Visual Studio Code next.

## Assignment

Try building out your server with more capabilities. See [this page](https://api.chucknorris.io/) to, for example, add a tool that calls an API. You decide what the server should look like. Have fun :)

## Solution

[Solution](./solution/README.md) — Here's a possible solution with working code.

## Key Takeaways

The takeaways from this chapter are the following:

- SSE is the second supported transport next to stdio.
- To support SSE, you need to manage incoming connections and messages using a web framework.
- You can use both Inspector and Visual Studio Code to consume SSE servers, just like stdio servers. Note how it differs a little between stdio and SSE. For SSE, you need to start up the server separately and then run your Inspector tool. For the Inspector tool, there's also a difference in that you need to specify the URL. 

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../samples/csharp/)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../samples/python/) 

## Additional Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## What's Next

Next: [Getting Started with AI Toolkit for VSCode](/03-GettingStarted/06-aitk/README.md)

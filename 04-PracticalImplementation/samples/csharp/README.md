# Sample

The previous example shows how to use a local .NET project with the `stdio` type. And how to run the server locally in a container. This is a good solution in many situations. However, it can be useful to have the server running remotely, like in a cloud environment. This is where the `http` type comes in.

Looking at the solution in the `04-PracticalImplementation` folder, it may look much more complex than the previous one. But in reality, it is not. If you look closely to the project `src/Calculator`, you will see that it is mostly the same code as the previous example. The only difference is that we are using a different library `ModelContextProtocol.AspNetCore` to handle the HTTP requests. And we change the method `IsPrime` to make it private, just to show that you can have private methods in your code. The rest of the code is the same as before.

The other projects are from [Aspire](https://aspire.dev/get-started/what-is-aspire/). Having Aspire in the solution will improve the experience of the developer while developing and testing and help with observability. It is not required to run the server, but it is a good practice to have it in your solution.

## Start the server locally

1. From VS Code (with the C# DevKit extension), navigate down to the `04-PracticalImplementation/samples/csharp` directory.
1. Execute the following command to start the server:

   ```bash
    dotnet watch run --project ./src/AppHost
   ```

1. When a web browser opens the Aspire dashboard, note the `http` URL. It should be something like `http://localhost:5058/`.

   ![Aspire Dashboard](./images/dotnet-aspire-dashboard.png)

## Test Streamable HTTP with the MCP Inspector

If you have Node.js 22.7.5 and higher, you can use the MCP Inspector to test your server.

Start the server and run the following command in a terminal:

```bash
npx @modelcontextprotocol/inspector http://localhost:5058
```

![MCP Inspector](./images/mcp-inspector.png)

- Select the `Streamable HTTP` as the Transport type.
- In the Url field, enter the URL of the server noted earlier, and append `/mcp`. It should be `http` (not `https`) something like `http://localhost:5058/mcp`.
- select the Connect button.

A nice thing about the Inspector is that it provide a nice visibility on what is happening.

- Try listing the available tools
- Try some of them, it should works just like before.

## Test MCP Server with GitHub Copilot Chat in VS Code

To use the Streamable HTTP transport with GitHub Copilot Chat, change the configuration of the `calc-mcp` server created previously to look like this:

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "http://localhost:5058/mcp"
    }
  }
}
```

Do some tests:

- Ask for "3 prime numbers after 6780". Note how Copilot will use the new tools `NextFivePrimeNumbers` and only return the first 3 prime numbers.
- Ask for "7 prime numbers after 111", to see what happens.
- Ask for "John has 24 lollies and wants to distribute them all to his 3 kids. How many lollies does each kid have?", to see what happens.

## Deploy the server to Azure

Let's deploy the server to Azure so more people can use it.

From a terminal, navigate to the folder `04-PracticalImplementation/samples/csharp` and run the following command:

```bash
azd up
```

Once the deployment is over, you should see a message like this:

![Azd deployment success](./images/azd-deployment-success.png)

Grab the URL and use it in the MCP Inspector and in the GitHub Copilot Chat.

```jsonc
// .vscode/mcp.json
{
  "servers": {
    "calc-mcp": {
      "type": "http",
      "url": "https://calc-mcp.gentleriver-3977fbcf.australiaeast.azurecontainerapps.io/mcp"
    }
  }
}
```

## What's next?

We try different transport types and testing tools. We also deploy your MCP server to Azure. But what if our server needs to access to private resources? For example, a database or a private API? In the next chapter, we will see how we can improve the security of our server.

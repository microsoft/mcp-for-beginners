# Running this sample

You need the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) and [Node.js](https://nodejs.org/) (for the MCP Inspector).

## -1- Install the dependencies

```bash
dotnet restore
```

## -2- Run the sample

```bash
dotnet run
```

The server listens on `http://localhost:3001` and serves MCP over Streamable HTTP at `/mcp`.

## -3- Test the sample

Start a separate terminal before you run the below (ensure the server is still running).

With the server running in one terminal, open another terminal and run the following command:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001/mcp
```

This should start a web server with a visual interface allowing you to test the sample.

> Make sure that the **Streamable HTTP** is selected as the transport type, and URL is `http://localhost:3001/mcp`.

Once the server is connected: 

- try listing tools and run `add_numbers`, with args 2 and 4, you should see 6 in the result.

> [!NOTE]
> The C# method is called `AddNumbers`; the MCP C# SDK publishes it in snake_case as `add_numbers`.

### Testing in CLI mode

You can launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001/mcp --method tools/list
```

This will list all the tools available in the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "add_numbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001/mcp --method tools/call --tool-name add_numbers --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ]
}
```

> [!TIP]
> It's usually a lot faster to run the inspector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

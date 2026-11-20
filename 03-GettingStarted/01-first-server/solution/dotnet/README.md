# Running this sample

You need the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0). To test the server you also need [Node.js](https://nodejs.org/) for `npx`.

## -1- Install the dependencies

```bash
dotnet restore
```

## -2- Run the sample

```bash
dotnet run
```

The server uses the stdio transport: it waits for a client on stdin and writes its log messages to stderr. Press `Ctrl+C` to stop it.

## -3- Test the sample

The inspector starts its own copy of the server, so you don't need to keep the one from step 2 running. Run the following command:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

This should start a web server with a visual interface allowing you to test the sample.

Once the server is connected, try listing tools and run `add`, with args 2 and 4, you should see `Sum 6` in the result.

### Testing in CLI mode

You can launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

This will list all the tools available in the server. You should see the following output (the server's log messages on stderr are printed as well):

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
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

> [!NOTE]
> The C# method is called `Add`, but the MCP C# SDK publishes tool names in snake_case, so the tool is called `add`.

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ]
}
```

> [!TIP]
> It's usually a lot faster to run the inspector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

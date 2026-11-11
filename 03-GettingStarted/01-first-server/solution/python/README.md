# Running this sample

You need Python 3.10 or later (the MCP Python SDK 2.x requires it). You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

> On macOS/Linux use `python3` if `python` is not available.

## -1- Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3"
```

## -3- Run the sample

```bash
mcp run server.py
```

The server uses the stdio transport, so it prints nothing and waits for a client on stdin. Press `Ctrl+C` to stop it.

## -4- Test the sample

You don't need to keep the server from step 3 running: `mcp dev` starts its own copy of the server. Run the following command:

```bash
mcp dev server.py --with typer
```

> [!NOTE]
> `mcp dev` starts the server in a fresh `uv` environment that only installs `mcp` without the `[cli]` extra. Without `--with typer` the server exits immediately with `Error: typer is required` and the inspector shows `Failed to connect to "uv"` / `Connection closed`.

This should start a web server with a visual interface allowing you to test the sample.

Once the server is connected: 

- try listing tools and run `add`, with args 2 and 4, you should see 6 in the result.

- go to resources and resource template and call get_greeting, type in a name and you should see a greeting with the name you provided.

### Testing in ClI mode

The inspector you ran is actually a Node.js app and `mcp dev` is a wrapper around it. 

You can launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

This will list all the tools available in the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "structuredContent": {
    "result": 3
  },
  "isError": false
}
```

> [!TIP]
> It's usually a lot faster to run the inspector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

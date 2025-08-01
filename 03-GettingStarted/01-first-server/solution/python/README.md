# Running this sample

You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

```bash
venv\Scripts\activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run the sample


```bash
mcp run server.py
```

## -4- Test the sample

With the server running in one terminal, open another terminal and run the following command:

```bash
mcp dev server.py
```

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
  "isError": false
}
```

> ![!TIP]
> It's usually a lot faster to run the ispector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

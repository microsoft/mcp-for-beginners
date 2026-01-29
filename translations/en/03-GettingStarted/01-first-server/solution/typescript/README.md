# Running this sample

It is recommended to install `uv`, but it's not mandatory. See [instructions](https://docs.astral.sh/uv/#highlights).

## -1- Install the dependencies

```bash
npm install
```

## -3- Run the sample

```bash
npm run build
```

## -4- Test the sample

With the server running in one terminal, open another terminal and execute the following command:

```bash
npm run inspector
```

This will start a web server with a visual interface that allows you to test the sample.

Once the server is connected:

- Try listing tools and run `add` with arguments 2 and 4. You should see 6 as the result.
- Navigate to resources and resource templates, then call "greeting." Enter a name, and you should see a greeting with the name you provided.

### Testing in CLI mode

The inspector you launched is actually a Node.js application, and `mcp dev` is a wrapper around it.

You can start it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

This will list all the tools available on the server. You should see the following output:

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

To invoke a tool, type:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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

> [!TIP]
> Running the inspector in CLI mode is usually much faster than using the browser.
> Learn more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
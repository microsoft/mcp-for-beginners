# Running this sample

You need [Node.js](https://nodejs.org/) 18 or later, which includes `npm` and `npx`.

## -1- Install the dependencies

```bash
npm install
```

## -2- Build the sample

```bash
npm run build
```

This compiles `src/index.ts` into `build/index.js`.

## -3- Run the sample

```bash
npm start
```

The server uses the stdio transport, so it prints nothing and waits for a client on stdin. Press `Ctrl+C` to stop it.

## -4- Test the sample

You don't need to keep the server from step 3 running: the inspector starts its own copy of the server. Run the following command:

```bash
npm run inspector
```

This should start a web server with a visual interface allowing you to test the sample.

Once the server is connected:

- try listing tools and run `add`, with args 2 and 4, you should see 6 in the result.
- go to resources and resource templates and select `greeting`, type in a name and you should see a greeting with the name you provided.
- go to prompts and select `review-code`, type in some code and you should see a prompt asking to review it.

### Testing in CLI mode

The inspector you ran is a Node.js app. You can also launch it in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

This will list all the tools available in the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "execution": {
        "taskSupport": "forbidden"
      }
    }
  ]
}
```

To invoke a tool type:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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

To read the greeting resource type:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method resources/read --uri greeting://Alice
```

You should see the following output:

```text
{
  "contents": [
    {
      "uri": "greeting://Alice",
      "text": "Hello, Alice!"
    }
  ]
}
```

> [!TIP]
> It's usually a lot faster to run the inspector in CLI mode than in the browser.
> Read more about the inspector [here](https://github.com/modelcontextprotocol/inspector).

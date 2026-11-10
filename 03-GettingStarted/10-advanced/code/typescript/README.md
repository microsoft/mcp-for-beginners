# Run sample

## Install dependencies

```sh
npm install
```

## Build it

```sh
npm run build
```

## Run it

```sh
npm start
```

You should see the text (on stderr, because stdout is reserved for the JSON-RPC messages of the stdio transport):

```text
Registering tools...
Starting server...
```

Great, that means it's starting up correctly. Press `Ctrl+C` to stop it.

## Test the server

Test out the capabilities with the following command:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

This should start up the web interface of the inspector tool.

### Test in CLI mode

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

You should see the following output:

```json
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
      }
    },
    {
      "name": "subtract",
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
      }
    }
  ]
}
```

Run a tool:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

You should see a response similar to:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
}
```

Try testing a tool that doesn't exist like "add2" with this command:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

The Inspector CLI checks the tool name against `tools/list` before it calls the server, so you see:

```text
{"error":{"code":"tool_not_found","message":"Tool 'add2' not found on server."}}
```

If a client does send the call, the server's own check in `server.ts` answers with a tool error result: `{"content":[{"type":"text","text":"Tool add2 not found."}],"isError":true}`.

Also try sending in a parameter `c` that should be rejected by the schema like so:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

You should now see an "invalid arguments" tool error, showing that your validation works:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
    }
  ],
  "isError": true
}
```

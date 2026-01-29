# Running this sample

## -1- Install the dependencies

```bash
dotnet restore
```

## -2- Run the sample

```bash
dotnet run
```

## -3- Test the sample

Start a separate terminal before running the commands below (ensure the server is still active).

With the server running in one terminal, open another terminal and execute the following command:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

This will start a web server with a visual interface that allows you to test the sample.

> Ensure that **Streamable HTTP** is selected as the transport type, and the URL is `http://localhost:3001/mcp`.

Once the server is connected:

- Try listing tools and run `add` with arguments 2 and 4. You should see 6 as the result.
- Navigate to resources and resource templates, call "greeting," type in a name, and you should see a greeting with the name you provided.

### Testing in CLI mode

You can directly launch it in CLI mode by running the following command:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

This will list all the tools available on the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
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
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

To invoke a tool, type:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
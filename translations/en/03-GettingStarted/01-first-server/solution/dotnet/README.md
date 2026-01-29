# Running this sample

## -1- Install the dependencies

```bash
dotnet restore
```

## -3- Run the sample

```bash
dotnet run
```

## -4- Test the sample

With the server running in one terminal, open another terminal and run the following command:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

This will start a web server with a visual interface that lets you test the sample.

Once the server is connected:

- Try listing tools and run `add` with arguments 2 and 4. You should see 6 as the result.
- Go to resources and resource template, call "greeting," type in a name, and you should see a greeting with the name you entered.

### Testing in CLI mode

You can also launch it directly in CLI mode by running the following command:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

This will display all the tools available on the server. You should see the following output:

```text
{
  "tools": [
    {
      "name": "Add",
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
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

To use a tool, type:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

You should see the following output:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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
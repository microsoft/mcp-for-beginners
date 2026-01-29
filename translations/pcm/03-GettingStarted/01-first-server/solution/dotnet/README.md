# How to run dis sample

## -1- Install di dependencies

```bash
dotnet restore
```

## -3- Run di sample

```bash
dotnet run
```

## -4- Test di sample

Wit di server dey run for one terminal, open anoda terminal and run dis command:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dis go start one web server wey get visual interface wey go allow you test di sample.

When di server don connect:

- Try list tools and run `add`, wit args 2 and 4, you go see 6 for di result.
- Go resources and resource template, call "greeting", type one name and you go see greeting wit di name wey you provide.

### Testing for CLI mode

You fit launch am directly for CLI mode by running dis command:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Dis go list all di tools wey dey available for di server. You go see dis output:

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

To use one tool, type:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

You go see dis output:

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
> E dey usually fast pass to run di inspector for CLI mode dan for di browser.
> Read more about di inspector [here](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
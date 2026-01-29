# How to run dis sample

## -1- Install di dependencies

```bash
dotnet restore
```

## -2- Run di sample

```bash
dotnet run
```

## -3- Test di sample

Open another terminal before you run di one wey dey below (make sure say di server still dey run).

Wit di server dey run for one terminal, open another terminal and run dis command:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Dis go start one web server wey get visual interface wey go allow you test di sample.

> Make sure say **Streamable HTTP** dey selected as di transport type, and di URL na `http://localhost:3001/mcp`.

When di server don connect: 

- try list tools and run `add`, wit args 2 and 4, you go see 6 for di result.
- go resources and resource template, call "greeting", type one name and you go see greeting wit di name wey you provide.

### Testing for CLI mode

You fit launch am directly for CLI mode by running dis command:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Dis go list all di tools wey dey available for di server. You go see dis output:

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

To use one tool type:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

You go see dis output:

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
> E dey usually faster to run di inspector for CLI mode pass for di browser.
> Read more about di inspector [here](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, e better make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
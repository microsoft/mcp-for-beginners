# How to run dis sample

E good make you install `uv` but e no dey compulsory, check [instructions](https://docs.astral.sh/uv/#highlights)

## -1- Install di dependencies

```bash
npm install
```

## -3- Run di sample

```bash
npm run build
```

## -4- Test di sample

Wen di server dey run for one terminal, open another terminal and run dis command:

```bash
npm run inspector
```

Dis go start one web server wey get visual interface wey go allow you test di sample.

Wen di server don connect:

- Try make you list tools and run `add`, wit args 2 and 4, you go see 6 for di result.
- Go resources and resource template, call "greeting", type one name and you go see greeting wit di name wey you provide.

### Testing for CLI mode

Di inspector wey you run na Node.js app and `mcp dev` na wrapper wey dey around am.

You fit launch am directly for CLI mode by running dis command:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Dis go list all di tools wey dey available for di server. You go see dis output:

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

To invoke one tool, type:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> E dey usually faster to run di inspector for CLI mode dan for browser.
> Read more about di inspector [here](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am correct, abeg no forget say automatik transleshion fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di main source. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
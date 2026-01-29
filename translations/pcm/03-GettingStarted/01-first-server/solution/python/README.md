# How to run dis sample

E good make you install `uv` but e no dey compulsory, check [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create virtual environment

```bash
python -m venv venv
```

## -1- Activate di virtual environment

```bash
venv\Scripts\activate
```

## -2- Install di dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run di sample

```bash
mcp run server.py
```

## -4- Test di sample

Wit di server dey run for one terminal, open another terminal and run dis command:

```bash
mcp dev server.py
```

Dis go start web server wey get visual interface wey go allow you test di sample.

When di server don connect:

- Try list tools and run `add`, wit args 2 and 4, you go see 6 for di result.

- Go resources and resource template, call get_greeting, type name and you go see greeting wit di name wey you provide.

### Testing for CLI mode

Di inspector wey you run na Node.js app and `mcp dev` na wrapper wey dey around am.

You fit launch am directly for CLI mode by running dis command:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
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

To invoke tool type:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> E dey usually faster to run di inspector for CLI mode pass for browser.
> Read more about di inspector [here](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see so na AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) translate am. Even though we dey try make sure say e correct, abeg no forget say machine translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important matter, e go better make you use professional human translation. We no go fit take blame for any misunderstanding or wahala wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# How to run di sample

We dey assume say you don already get server code wey dey work. Abeg find server from one of di earlier chapters.

## Set up mcp.json

Dis na file wey you go use as reference, [mcp.json](../../../../../03-GettingStarted/04-vscode/solution/mcp.json).

Change di server entry as e need to show di full path to your server, including di full command wey you go use run am.

For di example file wey we mention above, di server entry dey look like dis:

<details>
<summary>node.js</summary>
```json
"hello-mcp": {
    "command": "node",
    "args": [
        "build/index.js"
    ]
}
```
</details>

<details>
<summary>.NET</summary>

You fit need enter di GitHub repository root, wey you fit get from di command, `git rev-parse --show-toplevel`.

```jsonc
{
  "inputs": [
    {
      "type": "promptString",
      "id": "repository-root",
      "description": "The absolute path to the repository root"
    }
  ],
  "servers": {
    "calculator-mcp-dotnet": {
      "type": "stdio",
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "${input:repository-root}/03-GettingStarted/02-client/solution/server/server.csproj"
      ]
    }
  }
}
```

</details>

Dis one mean say you go run command like dis: `node build/index.js`.

- Change di server entry to match where your server file dey or wetin you need to start your server, depending on di runtime and server location wey you choose.

## Use di features wey dey inside di server

- Click di `play` icon, after you don add *mcp.json* to *./vscode* folder,

    Check as di tooling icon go change to show say di number of tools wey dey available don increase. Di tooling icon dey right above di chat field for GitHub Copilot.

## Run one tool

- Type one prompt for your chat window wey match di description of your tool. For example, to trigger di tool `add`, type something like "add 3 to 20".

    You go see one tool wey go show above di chat text box wey go tell you to select am to run di tool like dis visual:

    ![VS Code dey show say e wan run one tool](../../../../../translated_images/pcm/vscode-agent.d5a0e0b897331060.webp)

    If you select di tool, e go give you one number result wey go talk say "23" if your prompt be like wetin we mention before.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg no forget say machine translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important matter, e go better make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
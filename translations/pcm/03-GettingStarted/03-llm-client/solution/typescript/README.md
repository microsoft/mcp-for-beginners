# How to run dis sample

Dis sample dey involve say make LLM dey for di client side. Di LLM go need you to either run am for Codespaces or make you set up personal access token for GitHub to make am work.

## -1- Install di dependencies

```bash
npm install
```

## -3- Run di server

```bash
npm run build
```

## -4- Run di client

```sh
npm run client
```

You go see result wey go look like dis:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Running this sample

This sample requires having an LLM on the client side. You need to either run this in Codespaces or set up a personal access token in GitHub for it to work.

## -1- Install the dependencies

```bash
npm install
```

## -3- Run the server

```bash
npm run build
```

## -4- Run the client

```sh
npm run client
```

You should see a result similar to:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
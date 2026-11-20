# Running this sample

This sample has an LLM on the client: it lists the MCP server's tools, passes them to the model, and calls the tool the model picks. You need [Node.js](https://nodejs.org/) 18 or later and a model deployment in Microsoft Foundry (Azure OpenAI).

## -1- Install the dependencies

```bash
npm install
```

## -2- Configure Microsoft Foundry

Deploy an active model such as `gpt-5.1` in Microsoft Foundry, then set:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

On Windows PowerShell use `$env:AZURE_OPENAI_ENDPOINT="..."` instead of `export`. `AZURE_OPENAI_DEPLOYMENT` is the deployment name, which may differ from the model name.

## -3- Build the sample

```bash
npm run build
```

## -4- Run the client

```sh
npm run client
```

The client starts the server (`build/index.js`) itself over stdio and exits when it's done. You should see a result similar to:

```text
MCPClient started on stdin/stdout
Asking server for available tools
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

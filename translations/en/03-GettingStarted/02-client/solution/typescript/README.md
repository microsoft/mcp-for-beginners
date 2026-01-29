# Running this sample

You're recommended to install `uv` but it's not mandatory, see [instructions](https://docs.astral.sh/uv/#highlights)

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
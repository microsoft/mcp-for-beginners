# ਇਸ ਸੈਂਪਲ ਨੂੰ ਚਲਾਉਣਾ

ਇਸ ਸੈਂਪਲ ਵਿੱਚ ਕਲਾਇੰਟ 'ਤੇ ਇੱਕ LLM ਹੋਣਾ ਸ਼ਾਮਲ ਹੈ। LLM ਨੂੰ ਚਾਹੀਦਾ ਹੈ ਕਿ ਤੁਸੀਂ ਇਸਨੂੰ Codespaces ਵਿੱਚ ਚਲਾਓ ਜਾਂ GitHub ਵਿੱਚ ਇੱਕ personal access token ਸੈੱਟ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਕੰਮ ਕਰ ਸਕੇ।

## -1- Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash
npm install
```

## -3- ਸਰਵਰ ਚਲਾਓ

```bash
npm run build
```

## -4- ਕਲਾਇੰਟ ਚਲਾਓ

```sh
npm run client
```

ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
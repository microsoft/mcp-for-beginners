# ਉਦਾਹਰਨ: ਬੁਨਿਆਦੀ ਹੋਸਟ

ਇੱਕ ਸੰਦੇਸ਼ ਅਮਲੀ ਵਿਧੀ ਜਿਸ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ MCP ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਨ ਵਾਲੀ MCP ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈ ਜਾਂਦੀ ਹੈ ਅਤੇ ਟੂਲ UI ਨੂੰ ਸੁਰੱਖਿਅਤ ਸੈਂਡਬਾਕਸ ਵਿੱਚ ਰੇਨਡਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

ਇਹ ਬੁਨਿਆਦੀ ਹੋਸਟ ਸਥਾਨਕ ਵਿਕਾਸ ਦੌਰਾਨ MCP ਐਪਸ ਦੀ ਟੈਸਟਿੰਗ ਲਈ ਵੀ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।

## ਮੁੱਖ ਫਾਈਲਾਂ

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - ਟੂਲ ਚੋਣ, ਪੈਰਾਮੀਟਰ ਇਨਪੁੱਟ, ਅਤੇ iframe ਪ੍ਰਬੰਧਨ ਨਾਲ React UI ਹੋਸਟ  
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - ਸੁਰੱਖਿਆ ਸੱਚਾਈ ਅਤੇ ਦੋਹਾਂ-ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਸੁਨੇਹਾ ਰਿਲੇ ਨਾਲ ਬਾਹਰੀ iframe ਪ੍ਰਾਕਸੀ  
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - ਮੁੱਖ ਤਰਕ: ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ, ਟੂਲ ਕਾਲਿੰਗ, ਅਤੇ AppBridge ਸੈਟਅਪ

## ਸ਼ੁਰੂਆਤ

```bash
npm install
npm run start
# http://localhost:8080 ਖੋਲ੍ਹੋ
```
  
ਮੂਲ ਰੂਪ ਨਾਲ, ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ MCP ਸਰਵਰ `http://localhost:3001/mcp` ਨਾਲ ਜੁੜਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੇਗੀ। ਤੁਸੀਂ ਇਹ ਵਤੀਰਾ `SERVERS` ਐਨਵਾਇਰਨਮੈਂਟ ਵੇਰੀਏਬਲ ਨੂੰ ਸਰਵਰ URLs ਦੀ JSON ਐਰੇ ਦੇ ਨਾਲ ਸੈੱਟ ਕਰਕੇ ਬਦਲ ਸਕਦੇ ਹੋ:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```
  
## ਆਰਕੀਟੈਕਚਰ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਸੁਰੱਖਿਅਤ UI ਅਲਗਾਊ ਲਈ ਦੋਹਰਾ-iframe ਸੈਂਡਬਾਕਸ ਪੈਟਰਨ ਵਰਤਿਆ ਗਿਆ ਹੈ:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```
  
**ਕਿਉਂ ਦੋ iframe?**

- ਬਾਹਰੀ iframe ਵੱਖਰੇ origin (ਪੋਰਟ 8081) 'ਤੇ ਚੱਲਦਾ ਹੈ ਜੋ ਹੋਸਟ ਤੱਕ ਸਿੱਧਾ ਪਹੁੰਚ ਨਹੀਂ ਦੇਂਦਾ  
- ਅੰਦਰੂਨੀ iframe ਨੂੰ `srcdoc` ਰਾਹੀਂ HTML ਮਿਲਦਾ ਹੈ ਅਤੇ ਇਹ ਸੈਂਡਬਾਕਸ ਗੁਣ-ਧਰਮਾਂ ਨਾਲ ਸੀਮਤ ਹੁੰਦਾ ਹੈ  
- ਸੁਨੇਹੇ ਬਾਹਰੀ iframe ਰਾਹੀਂ ਬਹਿੰਦੇ ਹਨ ਜੋ ਉਹਨਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਅਤੇ ਦੋਹਾਂ-ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਰਿਲੇ ਕਰਦਾ ਹੈ  

ਇਹ ਆਰਕੀਟੈਕਚਰ ਇਸ ਗੱਲ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਭਾਵੇਂ ਟੂਲ UI ਕੋਡ ਦੁਰਪ੍ਰਯੋਗੀ ਹੋਵੇ, ਇਹ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਦੇ DOM, ਕੁਕੀਜ਼, ਜਾਂ ਜਾਵਾਸਕ੍ਰਿਪਟ ਸੰਦਰਭ ਤੱਕ ਪਹੁੰਚ ਨਹੀਂ ਕਰ ਸਕਦਾ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਇਤਲਾਹ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪੱਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭੁੱਲ-ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# ਨਮੂਨਾ ਚਲਾਓ

## Dependencies ਇੰਸਟਾਲ ਕਰੋ

```sh
npm install
```

## ਬਣਾਓ

```sh
npm run build
```

## ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ

```sh
npm run generate
```

ਇਹ ਇੱਕ ਟੋਕਨ *.env* ਫਾਇਲ ਵਿੱਚ ਬਣਾਉਂਦਾ ਹੈ। ਕਲਾਇੰਟ ਇਸ ਫਾਇਲ ਤੋਂ ਪੜ੍ਹੇਗਾ।

## ਕੋਡ ਚਲਾਓ

ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ:

```sh
npm start
```

ਕਲਾਇੰਟ ਨੂੰ ਇੱਕ ਵੱਖਰੇ ਟਰਮੀਨਲ ਵਿੱਚ ਚਲਾਓ:

```sh
npm run client
```

ਸਰਵਰ ਦੇ ਟਰਮੀਨਲ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਆਉਟਪੁੱਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
User exists
User has required scopes
Middleware executed
```

ਅਤੇ ਕਲਾਇੰਟ ਦੇ ਟਰਮੀਨਲ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਆਉਟਪੁੱਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### ਚੀਜ਼ਾਂ ਬਦਲਣਾ

ਆਓ ਯਕੀਨੀ ਬਣਾਈਏ ਕਿ ਅਸੀਂ ਸਕੋਪਸ ਨੂੰ ਸਮਝਦੇ ਹਾਂ। *server.ts* ਫਾਇਲ ਨੂੰ ਲੱਭੋ ਅਤੇ ਇਹ ਕੋਡ:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

ਇਹ ਕਹਿੰਦਾ ਹੈ ਕਿ ਪਾਸ ਕੀਤਾ ਟੋਕਨ "User.Read" ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਆਓ ਇਸਨੂੰ "User.Write" ਵਿੱਚ ਬਦਲ ਦਈਏ। ਹੁਣ `npm run build` ਚਲਾਓ ਅਤੇ ਸਰਵਰ ਨੂੰ ਮੁੜ ਸ਼ੁਰੂ ਕਰੋ `npm start`। ਹੁਣ ਤੁਹਾਨੂੰ ਦਿਖਾਈ ਦੇਵੇਗਾ ਕਿ ਅਥਾਰਾਈਜ਼ੇਸ਼ਨ ਫੇਲ ਹੋ ਜਾਂਦਾ ਹੈ ਕਿਉਂਕਿ ਸਾਡੇ ਕੋਲ ਇਹ ਸਕੋਪ ਨਹੀਂ ਹੈ (ਸਾਡੇ ਕੋਲ User.Read ਅਤੇ Admin.Write ਹਨ):

ਹੁਣ ਕਲਾਇੰਟ ਕਹਿੰਦਾ ਹੈ

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ਅਤੇ ਤੁਸੀਂ ਸਰਵਰ ਦੇ ਟਰਮੀਨਲ ਵਿੱਚ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਇਹ ਕਹਿੰਦਾ ਹੈ:

```text
User exists
```

ਅਤੇ ਇਹ ਇਸ ਪਾਇੰਟ ਤੋਂ ਅੱਗੇ ਨਹੀਂ ਜਾਂਦਾ।

ਜਾਂ ਤਾਂ ਇਸ ਸਕੋਪ "User.Write" ਨੂੰ ਸ਼ਾਮਲ ਕਰੋ ਅਤੇ `npm run generate` ਚਲਾਓ ਅਤੇ ਕਲਾਇੰਟ ਨੂੰ ਮੁੜ ਚਲਾਓ ਜਾਂ ਸਰਵਰ ਕੋਡ ਨੂੰ ਵਾਪਸ ਬਦਲੋ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਾਰੂਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਲਿਖਿਆ ਗਇਆ ਰੂਪ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
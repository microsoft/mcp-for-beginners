# ਇਸ ਨਮੂਨੇ ਨੂੰ ਚਲਾਉਣਾ

ਇੱਥੇ ਦਿਖਾਇਆ ਗਿਆ ਹੈ ਕਿ ਕਿਵੇਂ ਕਲਾਸਿਕ HTTP ਸਟ੍ਰੀਮਿੰਗ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ, ਅਤੇ MCP ਸਟ੍ਰੀਮਿੰਗ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਨੂੰ Python ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਲਾਇਆ ਜਾਵੇ।

### ਝਲਕ

- ਤੁਸੀਂ ਇੱਕ MCP ਸਰਵਰ ਸੈਟਅਪ ਕਰੋਗੇ ਜੋ ਆਈਟਮਾਂ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦੇ ਸਮੇਂ ਕਲਾਇੰਟ ਨੂੰ ਪ੍ਰਗਤੀ ਸੂਚਨਾਵਾਂ ਸਟ੍ਰੀਮ ਕਰਦਾ ਹੈ।
- ਕਲਾਇੰਟ ਹਰ ਸੂਚਨਾ ਨੂੰ ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਦਿਖਾਏਗਾ।
- ਇਹ ਗਾਈਡ ਪੂਰਵ ਸ਼ਰਤਾਂ, ਸੈਟਅਪ, ਚਲਾਉਣ ਅਤੇ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਨੂੰ ਕਵਰ ਕਰਦੀ ਹੈ।

### ਪੂਰਵ ਸ਼ਰਤਾਂ

- Python 3.9 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ ਵਰਜਨ
- `mcp` Python ਪੈਕੇਜ (ਇੰਸਟਾਲ ਕਰਨ ਲਈ `pip install mcp` ਵਰਤੋਂ ਕਰੋ)

### ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਸੈਟਅਪ

1. ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ ਜਾਂ ਹੱਲ ਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ।

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਐਕਟੀਵੇਟ ਕਰੋ (ਸੁਝਾਏ ਗਏ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **ਲੋੜੀਂਦੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ਫਾਈਲਾਂ

- **ਸਰਵਰ:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ਕਲਾਇੰਟ:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### ਕਲਾਸਿਕ HTTP ਸਟ੍ਰੀਮਿੰਗ ਸਰਵਰ ਚਲਾਉਣਾ

1. ਹੱਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. ਕਲਾਸਿਕ HTTP ਸਟ੍ਰੀਮਿੰਗ ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ:

   ```pwsh
   python server.py
   ```

3. ਸਰਵਰ ਸ਼ੁਰੂ ਹੋਵੇਗਾ ਅਤੇ ਇਹ ਦਿਖਾਏਗਾ:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ਕਲਾਸਿਕ HTTP ਸਟ੍ਰੀਮਿੰਗ ਕਲਾਇੰਟ ਚਲਾਉਣਾ

1. ਇੱਕ ਨਵਾਂ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ (ਉਹੀ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਅਤੇ ਡਾਇਰੈਕਟਰੀ ਐਕਟੀਵੇਟ ਕਰੋ):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. ਤੁਸੀਂ ਸਟ੍ਰੀਮ ਕੀਤੇ ਗਏ ਸੁਨੇਹੇ ਲਗਾਤਾਰ ਪ੍ਰਿੰਟ ਹੋਣ ਦੇਖੋਗੇ:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP ਸਟ੍ਰੀਮਿੰਗ ਸਰਵਰ ਚਲਾਉਣਾ

1. ਹੱਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP ਸਰਵਰ ਨੂੰ streamable-http ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ:
   ```pwsh
   python server.py mcp
   ```
3. ਸਰਵਰ ਸ਼ੁਰੂ ਹੋਵੇਗਾ ਅਤੇ ਇਹ ਦਿਖਾਏਗਾ:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP ਸਟ੍ਰੀਮਿੰਗ ਕਲਾਇੰਟ ਚਲਾਉਣਾ

1. ਇੱਕ ਨਵਾਂ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ (ਉਹੀ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਅਤੇ ਡਾਇਰੈਕਟਰੀ ਐਕਟੀਵੇਟ ਕਰੋ):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. ਤੁਸੀਂ ਸੂਚਨਾਵਾਂ ਰੀਅਲ-ਟਾਈਮ ਵਿੱਚ ਪ੍ਰਿੰਟ ਹੋਣ ਦੇਖੋਗੇ ਜਦੋਂ ਸਰਵਰ ਹਰ ਆਈਟਮ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### ਮੁੱਖ ਕਾਰਜਨਵਾਈ ਕਦਮ

1. **FastMCP ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਬਣਾਓ।**
2. **ਇੱਕ ਟੂਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ ਜੋ ਸੂਚੀ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ ਅਤੇ `ctx.info()` ਜਾਂ `ctx.log()` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੂਚਨਾਵਾਂ ਭੇਜਦਾ ਹੈ।**
3. **ਸਰਵਰ ਨੂੰ `transport="streamable-http"` ਨਾਲ ਚਲਾਓ।**
4. **ਇੱਕ ਕਲਾਇੰਟ ਲਾਗੂ ਕਰੋ ਜਿਸ ਵਿੱਚ ਸੁਨੇਹਾ ਹੈਂਡਲਰ ਹੋਵੇ ਜੋ ਆਉਣ ਵਾਲੀਆਂ ਸੂਚਨਾਵਾਂ ਦਿਖਾਏ।**

### ਕੋਡ ਵਾਕਥਰੂ

- ਸਰਵਰ async ਫੰਕਸ਼ਨ ਅਤੇ MCP ਸੰਦਰਭ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਪ੍ਰਗਤੀ ਅੱਪਡੇਟ ਭੇਜਣ ਲਈ।
- ਕਲਾਇੰਟ async ਸੁਨੇਹਾ ਹੈਂਡਲਰ ਲਾਗੂ ਕਰਦਾ ਹੈ ਜੋ ਸੂਚਨਾਵਾਂ ਅਤੇ ਅੰਤਮ ਨਤੀਜਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

### ਸੁਝਾਅ ਅਤੇ ਸਮੱਸਿਆ ਹੱਲ

- ਗੈਰ-ਅਵਰੋਧਕ ਕਾਰਜਾਂ ਲਈ `async/await` ਦੀ ਵਰਤੋਂ ਕਰੋ।
- ਦੋਨੋ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਵਿੱਚ ਅਪਵਾਦਾਂ ਨੂੰ ਹਮੇਸ਼ਾ ਹੈਂਡਲ ਕਰੋ ਤਾਕਿ ਮਜ਼ਬੂਤੀ ਬਣੀ ਰਹੇ।
- ਕਈ ਕਲਾਇੰਟਾਂ ਨਾਲ ਟੈਸਟ ਕਰੋ ਤਾਕਿ ਰੀਅਲ-ਟਾਈਮ ਅੱਪਡੇਟ ਦੇਖੇ ਜਾ ਸਕਣ।
- ਜੇ ਤੁਸੀਂ ਗਲਤੀਆਂ ਦਾ ਸਾਹਮਣਾ ਕਰਦੇ ਹੋ, ਤਾਂ ਆਪਣਾ Python ਵਰਜਨ ਚੈੱਕ ਕਰੋ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੀਆਂ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
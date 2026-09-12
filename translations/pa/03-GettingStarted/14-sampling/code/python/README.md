# ਨਮੂਨਾ ਚਲਾਓ

> [!WARNING]
> ਇਹ ਨਮੂਨਾ ਪੁਰਾਣੇ ਸਮਪਲਿੰਗ ਅਤੇ ਇਕ ਲੈਗੇਸੀ HTTP+SSE ਐਂਡਪੁਆਇੰਟ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਇਹ
> MCP `2025-11-25` ਅਨੁਕੂਲਤਾ ਲਈ ਰੱਖਿਆ ਗਿਆ ਹੈ। ਨਵੇਂ ਇੰਪਲਿਮੇਂਟੇਸ਼ਨ ਸਿੱਧਾ ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਨੂੰ ਕਾਲ ਕਰਨ ਅਤੇ ਦੂਰੇ MCP ਟ੍ਰੈਫਿਕ ਲਈ Streamable HTTP ਦੀ ਵਰਤੋਂ ਕਰਨ ਚਾਹੀਦੇ ਹਨ।


## ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ

```sh
python -m venv venv
source ./venv/bin/activate
```

## ਡਿਪੇਂਡੇਨਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ

```sh
pip install "mcp[cli]"
```

## ਸਰਵਰ ਚਲਾਓ

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot ਅਤੇ VS Code ਨਾਲ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ

mcp.json ਵਿੱਚ ਇਹ ਐਂਟਰੀ ਇਸ ਤਰ੍ਹਾਂ ਸ਼ਾਮਲ ਕਰੋ:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਸਰਵਰ 'ਤੇ "start" 'ਤੇ ਕਲਿੱਕ ਕੀਤਾ ਹੈ।

GitHub Copilot ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਪ੍ਰੰਪਟ ਪੇਸਟ ਕਰੋ:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

ਪਹਿਲੀ ਵਾਰੀ ਤੁਹਾਡੇ ਕੋਲ ਪੁੱਛਿਆ ਜਾਵੇਗਾ ਕਿ ਕੀ ਤੁਸੀਂ Sampling ਕਾਰਵਾਈ ਸਵੀਕਾਰ ਕਰਦੇ ਹੋ, ਫਿਰ ਤੁਹਾਨੂੰ ਟੂਲ ਨੂੰ "create_blog" ਚਲਾਉਣ ਲਈ ਸਵੀਕਾਰ ਕਰਨ ਲਈ ਕਿਹਾ ਜਾਵੇਗਾ। ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਪ੍ਰਤੀਕਿਰਿਆ ਦੇਖੋਗੇ:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
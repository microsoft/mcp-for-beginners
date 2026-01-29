# ਨਮੂਨਾ ਚਲਾਓ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਇੱਕ MCP ਸਰਵਰ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ ਮਿਡਲਵੇਅਰ ਸ਼ਾਮਲ ਹੈ ਜੋ ਵੈਧ Authorization ਹੈਡਰ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।

## Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install "mcp[cli]" 
```

## ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ

```bash
python server.py
```

ਦੂਜੇ ਟਰਮੀਨਲ ਵਿੱਚ ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰੋ

```bash
python client.py
```

ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਭੇਜੀ ਜਾ ਰਹੀ credential ਨੂੰ ਮਨਜ਼ੂਰੀ ਮਿਲ ਰਹੀ ਹੈ।

`client.py` ਵਿੱਚ credential ਨੂੰ "secret-token2" ਵਿੱਚ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ, ਫਿਰ ਤੁਹਾਨੂੰ ਜਵਾਬ ਦੇ ਹਿੱਸੇ ਵਜੋਂ ਇਹ ਟੈਕਸਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਸੀਂ ਪ੍ਰਮਾਣਿਤ ਹੋ (ਤੁਹਾਡੇ ਕੋਲ credential ਸੀ), ਪਰ ਇਹ ਅਵੈਧ ਸੀ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
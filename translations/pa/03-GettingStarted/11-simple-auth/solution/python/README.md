# ਨਮੂਨਾ ਚਲਾਓ

## ਵਾਤਾਵਰਣ ਬਣਾਓ

```sh
python -m venv venv
source ./venv/bin/activate
```

## Dependencies ਇੰਸਟਾਲ ਕਰੋ

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ

ਤੁਹਾਨੂੰ ਇੱਕ ਟੋਕਨ ਜਨਰੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਜੋ ਕਲਾਇੰਟ ਸਰਵਰ ਨਾਲ ਗੱਲ ਕਰਨ ਲਈ ਵਰਤੇਗਾ।

ਕਾਲ ਕਰੋ:

```sh
python util.py
```

## ਕੋਡ ਚਲਾਓ

ਕੋਡ ਚਲਾਓ:

```sh
python server.py
```

ਇੱਕ ਵੱਖਰੇ ਟਰਮੀਨਲ ਵਿੱਚ, ਟਾਈਪ ਕਰੋ:

```sh
python client.py
```

ਸਰਵਰ ਟਰਮੀਨਲ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

ਕਲਾਇੰਟ ਵਿੰਡੋ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਟੈਕਸਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਸਭ ਕੁਝ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।

### ਜਾਣਕਾਰੀ ਬਦਲੋ, ਇਸਨੂੰ ਫੇਲ੍ਹ ਹੋਣ ਦੇਖਣ ਲਈ

*server.py* ਵਿੱਚ ਇਹ ਕੋਡ ਲੱਭੋ:

```python
 if not has_scope(has_header, "Admin.Write"):
```

ਇਸਨੂੰ "User.Write" ਕਹਿਣ ਲਈ ਬਦਲੋ। ਤੁਹਾਡੇ ਮੌਜੂਦਾ ਟੋਕਨ ਕੋਲ ਇਹ ਅਨੁਮਤੀ ਪੱਧਰ ਨਹੀਂ ਹੈ, ਇਸ ਲਈ ਜੇ ਤੁਸੀਂ ਸਰਵਰ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਦੇ ਹੋ ਅਤੇ ਕਲਾਇੰਟ ਨੂੰ ਮੁੜ ਚਲਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ ਸਰਵਰ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਗਲਤੀ ਦੇ ਸਮਾਨ ਕੁਝ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

ਤੁਸੀਂ ਜਾਂ ਤਾਂ ਆਪਣੇ ਸਰਵਰ ਕੋਡ ਨੂੰ ਵਾਪਸ ਬਦਲ ਸਕਦੇ ਹੋ ਜਾਂ ਇੱਕ ਨਵਾਂ ਟੋਕਨ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ ਜਿਸ ਵਿੱਚ ਇਹ ਵਾਧੂ ਸਕੋਪ ਸ਼ਾਮਲ ਹੈ, ਇਹ ਤੁਹਾਡੇ ਉੱਤੇ ਹੈ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
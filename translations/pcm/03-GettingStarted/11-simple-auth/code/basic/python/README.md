# Run sample

Dis sample go start one MCP Server wey get middleware wey dey check say Authorization header dey valid.

## Install dependencies

```bash
pip install "mcp[cli]" 
```

## Start server

```bash
python server.py
```

run di client for another terminal

```bash
python client.py
```

You go see result wey go look like dis:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

dis one mean say di credential wey dem send don dey allowed.

Try change di credential for `client.py` to "secret-token2", den you go see dis text as part of di response:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

dis one mean say dem authenticate you (you get credential), but e no valid.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, make you sabi say translation wey machine do fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important information, e go better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
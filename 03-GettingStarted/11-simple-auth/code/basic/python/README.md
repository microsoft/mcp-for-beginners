# Run sample

This sample starts an MCP Server with a middleware that checks for a valid Authorization header.

## Install dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3" "requests>=2.34.2,<3"
```

## Start server

```bash
python server.py
```

start the client in another terminal

```bash
python client.py
```

You should see a result similar to:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structured_content={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} is_error=False result_type='complete'
```

this means the credential being sent through is being allowed.

Try changing the credential in `client.py` to "secret-token2", then you should see this text as part of the response:

```text
2025-09-30 13:27:44 - httpx2 - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

this means you were authenticated (you had a credential), but it was invalid.
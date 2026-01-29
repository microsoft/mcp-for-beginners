# Run sample

## Create environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Generate token

You need to generate a token that the client will use to communicate with the server.

Run:

```sh
python util.py
```

## Run code

Execute the code with:

```sh
python server.py
```

In a separate terminal, type:

```sh
python client.py
```

In the server terminal, you should see something like:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

In the client window, you should see text similar to:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

This indicates everything is working correctly.

### Modify the information to see it fail

Find this code in *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Change it so it says "User.Write". Your current token doesn't have this permission level, so if you restart the server and try to run the client again, you should see an error similar to the following in the server terminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

You can either revert your server code or generate a new token that includes this additional scope—it's up to you.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
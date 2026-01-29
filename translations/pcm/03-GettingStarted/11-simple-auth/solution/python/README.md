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

You go need generate one token wey the client go use take talk to the server.

Call:

```sh
python util.py
```

## Run code

Run the code with:

```sh
python server.py
```

For another terminal, type:

```sh
python client.py
```

For the server terminal, you go see something like:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

For the client window, you go see text wey resemble:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

This one mean say e dey work well.

### Change the info, make e fail

Find this code for *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Change am make e talk "User.Write". The token wey you get now no get that permission level, so if you restart the server and try run the client again, you go see error wey resemble this one for the server terminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

You fit either change back your server code or generate new token wey get this extra scope, na your choice.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, e good make professional human transle-shon dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
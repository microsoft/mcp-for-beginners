# Run sample

## Create environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]" dotenv PyJWT requests
```

## Generate token

You will need to generate a token that the client will use to talk to the server.

Call:

```sh
python util.py
```

## Run code

Run the code with:

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

In the client window, you should text similar to:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

This means it's all working

### Change the info, to see it failing

Locate this code in *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Change it to so it says "User.Write". Your current token doesn't have that permission level, so if you restart the server and try to run the client once more you should see an error similar to the following in the server terminal:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

You can either change back your server code or generate a new token that contains this additional scope, up to you.


# Running this sample

You need Python 3.10 or later (the MCP Python SDK 2.x requires it). You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

> On macOS/Linux use `python3` if `python` is not available.

## -1- Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3"
```

## -3- Run the sample

```bash
python client.py
```

The client starts `server.py` itself over stdio, so you don't need to run the server separately.

You should see an output similar to:

```text
LISTING RESOURCES
LISTING RESOURCE TEMPLATES
Resource template:  greeting://{name}
LISTING TOOLS
Tool:  add
READING RESOURCE
Hello, hello!
CALL TOOL
[TextContent(type='text', text='8', annotations=None, meta=None)]
```

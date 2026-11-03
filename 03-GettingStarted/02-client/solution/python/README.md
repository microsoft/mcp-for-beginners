# Running this sample

You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

```bash
venv\Scripts\activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3"
```

## -3- Run the sample

```bash
python client.py
```

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

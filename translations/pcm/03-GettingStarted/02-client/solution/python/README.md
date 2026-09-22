# How to run dis sample

Dem recommend say you install `uv` but e no be mandatory, check [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Make one virtual environment

```bash
python -m venv venv
```

## -1- Activate di virtual environment

```bash
venv\Scripts\activate
```

## -2- Install di dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run di sample

```bash
python client.py
```

You go see output like dis:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
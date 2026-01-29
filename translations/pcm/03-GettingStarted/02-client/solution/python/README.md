# How to run dis sample

E good make you install `uv` but e no dey compulsory, check [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create virtual environment

```bash
python -m venv venv
```

## -1- Activate di virtual environment

```bash
venv\Scrips\activate
```

## -2- Install di dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run di sample

```bash
python client.py
```

You go see output wey resemble dis one:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) translet am. Even though we dey try make sure say e correct, abeg make you sabi say machine transleshion fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
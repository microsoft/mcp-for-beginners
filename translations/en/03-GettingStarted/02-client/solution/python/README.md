# Running this sample

You're recommended to install `uv` but it's not mandatory, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

```bash
venv\Scrips\activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]"
```

## -3- Run the sample

```bash
python client.py
```

You should see an output similar to:

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

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
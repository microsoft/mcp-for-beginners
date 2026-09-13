# Selle näidise käivitamine

Soovitame paigaldada `uv`, kuid see ei ole kohustuslik, vaata [juhiseid](https://docs.astral.sh/uv/#highlights)

## -0- Loo virtuaalne keskkond

```bash
python -m venv venv
```

## -1- Aktiveeri virtuaalne keskkond

```bash
venv\Scripts\activate
```

## -2- Paigalda sõltuvused

```bash
pip install "mcp[cli]"
```

## -3- Käivita näidis

```bash
python client.py
```

Sa peaksid nägema väljundit, mis näeb välja umbes selline:

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
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
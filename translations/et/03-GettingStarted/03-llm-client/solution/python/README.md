# Selle näidise käivitamine

Soovitatav on paigaldada `uv`, kuid see pole kohustuslik, vaata [juhiseid](https://docs.astral.sh/uv/#highlights)

## -0- Loo virtuaalne keskkond

```bash
python -m venv venv
```

## -1- Aktiveeri virtuaalne keskkond

```bash
venv\Scrips\activate
```

## -2- Paigalda sõltuvused

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- Käivita näidis

```bash
python client.py
```

Peaksid nägema väljundit, mis on sarnane järgmisele:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
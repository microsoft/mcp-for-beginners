# Покретање овог примера

Препоручује се да инсталирате `uv`, али није обавезно, погледајте [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Креирање виртуелног окружења

```bash
python -m venv venv
```

## -1- Активирање виртуелног окружења

```bash
venv\Scrips\activate
```

## -2- Инсталирање зависности

```bash
pip install "mcp[cli]"
```

## -3- Покретање примера


```bash
python client.py
```

Требало би да видите излаз сличан овоме:

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

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
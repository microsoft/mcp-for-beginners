# Покретање овог примера

Препоручује се да инсталирате `uv`, али то није обавезно, погледајте [упутства](https://docs.astral.sh/uv/#highlights)

## -0- Креирајте виртуелно окружење

```bash
python -m venv venv
```

## -1- Активирајте виртуелно окружење

```bash
venv\Scripts\activate
```

## -2- Инсталирајте зависности

```bash
pip install "mcp[cli]"
```

## -3- Покрените пример

```bash
python client.py
```

Требало би да видите излаз сличан овом:

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
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
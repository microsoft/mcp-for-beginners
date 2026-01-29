# Стартиране на този пример

Препоръчително е да инсталирате `uv`, но не е задължително, вижте [инструкциите](https://docs.astral.sh/uv/#highlights)

## -0- Създаване на виртуална среда

```bash
python -m venv venv
```

## -1- Активиране на виртуалната среда

```bash
venv\Scrips\activate
```

## -2- Инсталиране на зависимостите

```bash
pip install "mcp[cli]"
```

## -3- Стартиране на примера

```bash
python client.py
```

Трябва да видите изход, подобен на:

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

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
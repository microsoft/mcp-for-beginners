# Paleisti šį pavyzdį

Rekomenduojama įdiegti `uv`, tačiau tai nėra būtina, žr. [instrukcijas](https://docs.astral.sh/uv/#highlights)

## -0- Sukurkite virtualią aplinką

```bash
python -m venv venv
```

## -1- Aktyvuokite virtualią aplinką

```bash
venv\Scrips\activate
```

## -2- Įdiekite priklausomybes

```bash
pip install "mcp[cli]"
```

## -3- Paleiskite pavyzdį

```bash
python client.py
```

Turėtumėte pamatyti rezultatą, panašų į:

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

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.
# Kuendesha sampuli hii

Unashauriwa kufunga `uv` lakini si lazima, angalia [maelekezo](https://docs.astral.sh/uv/#highlights)

## -0- Unda mazingira ya mtandaoni

```bash
python -m venv venv
```

## -1- Washa mazingira ya mtandaoni

```bash
venv\Scrips\activate
```

## -2- Sakinisha utegemezi

```bash
pip install "mcp[cli]"
```

## -3- Endesha sampuli


```bash
python client.py
```

Unapaswa kuona matokeo yanayofanana na:

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

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
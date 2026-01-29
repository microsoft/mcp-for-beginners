# Esecuzione di questo esempio

Si consiglia di installare `uv` ma non è obbligatorio, vedi [istruzioni](https://docs.astral.sh/uv/#highlights)

## -0- Crea un ambiente virtuale

```bash
python -m venv venv
```

## -1- Attiva l'ambiente virtuale

```bash
venv\Scrips\activate
```

## -2- Installa le dipendenze

```bash
pip install "mcp[cli]"
```

## -3- Esegui l'esempio

```bash
python client.py
```

Dovresti vedere un output simile a:

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
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
# Zagon tega primera

Priporočamo, da namestite `uv`, vendar ni nujno, poglejte [navodila](https://docs.astral.sh/uv/#highlights)

## -0- Ustvarite virtualno okolje

```bash
python -m venv venv
```

## -1- Aktivirajte virtualno okolje

```bash
venv\Scrips\activate
```

## -2- Namestite odvisnosti

```bash
pip install "mcp[cli]"
```

## -3- Zaženite primer


```bash
python client.py
```

Videli bi morali izhod, podoben temu:

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

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
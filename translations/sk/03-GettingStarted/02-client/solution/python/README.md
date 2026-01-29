# Spustenie tohto príkladu

Odporúča sa nainštalovať `uv`, ale nie je to povinné, pozri [návod](https://docs.astral.sh/uv/#highlights)

## -0- Vytvorenie virtuálneho prostredia

```bash
python -m venv venv
```

## -1- Aktivácia virtuálneho prostredia

```bash
venv\Scrips\activate
```

## -2- Inštalácia závislostí

```bash
pip install "mcp[cli]"
```

## -3- Spustenie príkladu

```bash
python client.py
```

Mali by ste vidieť výstup podobný tomuto:

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

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
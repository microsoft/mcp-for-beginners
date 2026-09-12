# Spustenie tohto príkladu

Odporúča sa nainštalovať `uv`, ale nie je to povinné, pozri [návod](https://docs.astral.sh/uv/#highlights)

## -0- Vytvorenie virtuálneho prostredia

```bash
python -m venv venv
```

## -1- Aktivovanie virtuálneho prostredia

```bash
venv\Scripts\activate
```

## -2- Inštalácia závislostí

```bash
pip install "mcp[cli]"
```

## -3- Spustenie príkladu

```bash
python client.py
```

Mali by ste vidieť výstup podobný:

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
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Zagon tega vzorca

Priporočamo, da namestite `uv`, ni pa nujno, glejte [navodila](https://docs.astral.sh/uv/#highlights)

## -0- Ustvarite virtualno okolje

```bash
python -m venv venv
```

## -1- Aktivirajte virtualno okolje

```bash
venv\Scripts\activate
```

## -2- Namestite odvisnosti

```bash
pip install "mcp[cli]"
```

## -3- Zaženite vzorec

```bash
python client.py
```

Videti bi morali izhod, podoben temu:

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
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
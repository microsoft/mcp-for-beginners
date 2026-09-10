# MCP kalkulaatori server (Python)



Lihtne Model Context Protocol (MCP) serveri rakendus Pythonis, mis pakub põhilist kalkulaatori funktsionaalsust.


## Paigaldamine

Paigalda vajalikke sõltuvusi:

```bash
pip install -r requirements.txt
```

Või paigalda MCP Python SDK otse:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Kasutusjuhend

### Serveri käivitamine

Server on loodud MCP klientide (näiteks Claude Desktop) jaoks. Serveri käivitamiseks:

```bash
python mcp_calculator_server.py
```

**Märkus**: Kui käivitad otse terminalis, näed JSON-RPC valideerimisvigu. See on normaalne käitumine – server ootab korralikult vormistatud MCP kliendipäringuid.

### Funktsioonide testimine

Selleks, et testida kalkulaatori funktsioonide õigsust:

```bash
python test_calculator.py
```

## Tõrkeotsing

### Impordivead

Kui saad vea `ModuleNotFoundError: No module named 'mcp'`, paigalda MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC vead otsekäivitamisel

Vead nagu "Invalid JSON: EOF while parsing a value" otsekäivitamisel on ootuspärased. Server vajab MCP kliendi sõnumeid, mitte otse terminali sisendit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
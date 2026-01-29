# MCP Kalkulaatori Server (Python)

Lihtne Model Context Protocol (MCP) serveri teostus Pythonis, mis pakub põhilist kalkulaatori funktsionaalsust.

## Paigaldamine

Paigalda vajalikud sõltuvused:

```bash
pip install -r requirements.txt
```

Või paigalda MCP Python SDK otse:

```bash
pip install mcp>=1.18.0
```

## Kasutamine

### Serveri käivitamine

Server on mõeldud kasutamiseks MCP klientide poolt (näiteks Claude Desktop). Serveri käivitamiseks:

```bash
python mcp_calculator_server.py
```

**Märkus**: Kui käivitate otse terminalis, näete JSON-RPC valideerimisvigu. See on normaalne käitumine - server ootab korrektselt vormindatud MCP kliendisõnumeid.

### Funktsioonide testimine

Et testida, kas kalkulaatori funktsioonid töötavad korrektselt:

```bash
python test_calculator.py
```

## Tõrkeotsing

### Importimise vead

Kui näete `ModuleNotFoundError: No module named 'mcp'`, paigaldage MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC vead otse käivitamisel

Sellised vead nagu "Invalid JSON: EOF while parsing a value" serveri otse käivitamisel on oodatud. Server vajab MCP kliendisõnumeid, mitte otsest terminalisisendit.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
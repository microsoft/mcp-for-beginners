# Käivita näidis

See näidis käivitab MCP serveri koos vahevara, mis kontrollib kehtivat Authorization päist.

## Paigalda sõltuvused

```bash
pip install "mcp[cli]" 
```

## Käivita server

```bash
python server.py
```

käivita klient teises terminalis

```bash
python client.py
```

Sa peaksid nägema tulemust, mis on sarnane:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

see tähendab, et edastatud mandaati lubati.

Proovi muuta mandaati failis `client.py` väärtuseks "secret-token2", siis peaksid vastuses nägema järgmist teksti:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

see tähendab, et sind autentiti (sul oli mandaat), kuid see oli kehtetu.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
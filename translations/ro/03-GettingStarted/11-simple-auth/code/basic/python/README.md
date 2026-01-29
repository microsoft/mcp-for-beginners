# Rulează exemplul

Acest exemplu pornește un MCP Server cu un middleware care verifică existența unui header Authorization valid.

## Instalează dependențele

```bash
pip install "mcp[cli]" 
```

## Pornește serverul

```bash
python server.py
```

pornește clientul într-un alt terminal

```bash
python client.py
```

Ar trebui să vezi un rezultat similar cu:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

asta înseamnă că acreditivul trimis este permis.

Încearcă să schimbi acreditivul în `client.py` la "secret-token2", apoi ar trebui să vezi acest text ca parte a răspunsului:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

asta înseamnă că ai fost autentificat (aveai un acreditiv), dar acesta era invalid.

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
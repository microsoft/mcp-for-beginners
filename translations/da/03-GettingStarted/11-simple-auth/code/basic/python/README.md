# Kør eksempel

Dette eksempel starter en MCP-server med en middleware, der kontrollerer, om der er en gyldig Authorization-header.

## Installer afhængigheder

```bash
pip install "mcp[cli]" 
```

## Start server

```bash
python server.py
```

start klienten i en anden terminal

```bash
python client.py
```

Du bør se et resultat, der ligner:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Dette betyder, at den sendte legitimationsoplysning bliver accepteret.

Prøv at ændre legitimationsoplysningen i `client.py` til "secret-token2", så bør du se denne tekst som en del af svaret:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Dette betyder, at du blev autentificeret (du havde en legitimationsoplysning), men den var ugyldig.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
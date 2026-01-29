# Kjør eksempel

Dette eksempelet starter en MCP-server med en mellomvare som sjekker etter en gyldig Authorization-header.

## Installer avhengigheter

```bash
pip install "mcp[cli]" 
```

## Start server

```bash
python server.py
```

start klienten i et annet terminalvindu

```bash
python client.py
```

Du bør se et resultat som ligner på:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Dette betyr at legitimasjonen som sendes gjennom blir akseptert.

Prøv å endre legitimasjonen i `client.py` til "secret-token2", da bør du se denne teksten som en del av responsen:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Dette betyr at du ble autentisert (du hadde en legitimasjon), men den var ugyldig.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
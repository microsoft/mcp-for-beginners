# Kör exempel

Det här exemplet startar en MCP-server med en middleware som kontrollerar att en giltig Authorization-header finns.

## Installera beroenden

```bash
pip install "mcp[cli]" 
```

## Starta servern

```bash
python server.py
```

Starta klienten i en annan terminal

```bash
python client.py
```

Du bör se ett resultat som liknar:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Detta betyder att den skickade autentiseringen tillåts.

Prova att ändra autentiseringen i `client.py` till "secret-token2", då bör du se denna text som en del av svaret:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Detta betyder att du blev autentiserad (du hade en autentisering), men den var ogiltig.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
# Voorbeeld uitvoeren

Dit voorbeeld start een MCP-server met een middleware die controleert op een geldige Authorization-header.

## Afhankelijkheden installeren

```bash
pip install "mcp[cli]" 
```

## Server starten

```bash
python server.py
```

start de client in een andere terminal

```bash
python client.py
```

Je zou een resultaat moeten zien dat lijkt op:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Dit betekent dat de toegestuurde referentie wordt geaccepteerd.

Probeer de referentie in `client.py` te wijzigen naar "secret-token2", dan zou je deze tekst als onderdeel van de reactie moeten zien:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Dit betekent dat je geauthenticeerd bent (je had een referentie), maar deze was ongeldig.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
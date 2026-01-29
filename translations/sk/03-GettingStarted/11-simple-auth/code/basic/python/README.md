# Spustenie ukážky

Táto ukážka spúšťa MCP Server s middleware, ktorý kontroluje platný Authorization header.

## Inštalácia závislostí

```bash
pip install "mcp[cli]" 
```

## Spustenie servera

```bash
python server.py
```

spustite klienta v inom termináli

```bash
python client.py
```

Mali by ste vidieť výsledok podobný:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

to znamená, že odoslané poverenie je povolené.

Skúste zmeniť poverenie v `client.py` na "secret-token2", potom by ste mali vidieť tento text ako súčasť odpovede:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

to znamená, že ste boli autentifikovaní (mali ste poverenie), ale bolo neplatné.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
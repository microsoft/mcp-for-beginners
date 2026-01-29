# Endesha mfano

Mfano huu unaanzisha MCP Server na middleware inayokagua kama kuna kichwa cha Authorization halali.

## Sakinisha mahitaji

```bash
pip install "mcp[cli]" 
```

## Anzisha seva

```bash
python server.py
```

anzisha mteja kwenye terminal nyingine

```bash
python client.py
```

Unapaswa kuona matokeo yanayofanana na:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

hii inamaanisha kwamba kitambulisho kinachotumwa kinaruhusiwa.

Jaribu kubadilisha kitambulisho katika `client.py` kuwa "secret-token2", kisha unapaswa kuona maandishi haya kama sehemu ya majibu:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

hii inamaanisha ulithibitishwa (ulikuwa na kitambulisho), lakini kilikuwa batili.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya mtafsiri wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
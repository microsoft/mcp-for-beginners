# Példa futtatása

Ez a példa elindít egy MCP szervert egy köztes réteggel, amely ellenőrzi az érvényes Authorization fejlécet.

## Függőségek telepítése

```bash
pip install "mcp[cli]" 
```

## Szerver indítása

```bash
python server.py
```

indítsd el a klienst egy másik terminálban

```bash
python client.py
```

A következőhöz hasonló eredményt kell látnod:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ez azt jelenti, hogy az elküldött hitelesítő adat engedélyezve van.

Próbáld meg megváltoztatni a hitelesítő adatot a `client.py` fájlban "secret-token2"-re, ekkor a válaszban ezt a szöveget kell látnod:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ez azt jelenti, hogy hitelesítve lettél (volt hitelesítő adatod), de az érvénytelen volt.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
# Pokreni primjer

Ovaj primjer pokreće MCP poslužitelj s middlewareom koji provjerava valjanost Authorization zaglavlja.

## Instaliraj ovisnosti

```bash
pip install "mcp[cli]" 
```

## Pokreni poslužitelj

```bash
python server.py
```

pokreni klijent u drugom terminalu

```bash
python client.py
```

Trebali biste vidjeti rezultat sličan:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

to znači da se proslijeđena vjerodajnica prihvaća.

Pokušajte promijeniti vjerodajnicu u `client.py` na "secret-token2", tada biste trebali vidjeti ovaj tekst kao dio odgovora:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

to znači da ste bili autentificirani (imali ste vjerodajnicu), ali ona nije bila valjana.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
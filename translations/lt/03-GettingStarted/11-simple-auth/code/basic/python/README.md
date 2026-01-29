# Paleiskite pavyzdį

Šiame pavyzdyje paleidžiamas MCP serveris su tarpinė programine įranga, kuri tikrina, ar yra galiojanti Authorization antraštė.

## Įdiekite priklausomybes

```bash
pip install "mcp[cli]" 
```

## Paleiskite serverį

```bash
python server.py
```

paleiskite klientą kitame terminale

```bash
python client.py
```

Turėtumėte matyti rezultatą, panašų į:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

tai reiškia, kad siunčiama akreditacija yra leidžiama.

Pabandykite pakeisti akreditaciją faile `client.py` į "secret-token2", tada turėtumėte matyti šį tekstą kaip dalį atsakymo:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

tai reiškia, kad buvote autentifikuotas (turėjote akreditaciją), tačiau ji buvo neteisinga.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
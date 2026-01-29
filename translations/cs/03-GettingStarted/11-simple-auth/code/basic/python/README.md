# Spuštění ukázky

Tato ukázka spouští MCP Server s middlewarem, který kontroluje platný Authorization header.

## Instalace závislostí

```bash
pip install "mcp[cli]" 
```

## Spuštění serveru

```bash
python server.py
```

spusťte klienta v jiném terminálu

```bash
python client.py
```

Měli byste vidět výsledek podobný:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

to znamená, že předávané přihlašovací údaje jsou povoleny.

Zkuste změnit přihlašovací údaje v `client.py` na "secret-token2", poté byste měli vidět tento text jako součást odpovědi:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

to znamená, že jste byli autentizováni (měli jste přihlašovací údaje), ale byly neplatné.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
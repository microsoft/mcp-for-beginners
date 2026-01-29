# Zagon vzorca

Ta vzorec zažene MCP strežnik z vmesno programsko opremo, ki preverja veljavnost glave Authorization.

## Namestitev odvisnosti

```bash
pip install "mcp[cli]" 
```

## Zagon strežnika

```bash
python server.py
```

zaženite odjemalca v drugem terminalu

```bash
python client.py
```

Videti bi morali rezultat, podoben temu:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

to pomeni, da je posredovano poverilo dovoljeno.

Poskusite spremeniti poverilo v `client.py` na "secret-token2", nato bi morali videti ta tekst kot del odgovora:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

to pomeni, da ste bili avtenticirani (imeli ste poverilo), vendar je bilo neveljavno.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
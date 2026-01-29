# Esegui esempio

Questo esempio avvia un MCP Server con un middleware che verifica la presenza di un'intestazione Authorization valida.

## Installa dipendenze

```bash
pip install "mcp[cli]" 
```

## Avvia il server

```bash
python server.py
```

avvia il client in un altro terminale

```bash
python client.py
```

Dovresti vedere un risultato simile a:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

questo significa che la credenziale inviata è stata accettata.

Prova a cambiare la credenziale in `client.py` in "secret-token2", quindi dovresti vedere questo testo come parte della risposta:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

questo significa che sei stato autenticato (avevi una credenziale), ma era invalida.

---

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
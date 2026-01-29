# Esegui esempio

## Crea ambiente

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installa dipendenze

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Genera token

Dovrai generare un token che il client utilizzerà per comunicare con il server.

Esegui:

```sh
python util.py
```

## Esegui codice

Esegui il codice con:

```sh
python server.py
```

In un terminale separato, digita:

```sh
python client.py
```

Nel terminale del server, dovresti vedere qualcosa come:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Nella finestra del client, dovresti vedere un testo simile a:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Questo significa che tutto funziona correttamente.

### Modifica le informazioni per vedere un errore

Trova questo codice in *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Modificalo in modo che dica "User.Write". Il tuo token attuale non ha quel livello di permesso, quindi se riavvii il server e provi a eseguire nuovamente il client, dovresti vedere un errore simile al seguente nel terminale del server:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Puoi scegliere di ripristinare il codice del server o generare un nuovo token che contenga questo ambito aggiuntivo, a tua discrezione.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
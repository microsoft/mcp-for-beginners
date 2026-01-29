# Esecuzione di questo esempio

Ecco come eseguire il classico server e client HTTP streaming, così come il server e client MCP streaming utilizzando Python.

### Panoramica

- Configurerai un server MCP che invia notifiche di avanzamento al client mentre elabora gli elementi.
- Il client mostrerà ogni notifica in tempo reale.
- Questa guida copre prerequisiti, configurazione, esecuzione e risoluzione dei problemi.

### Prerequisiti

- Python 3.9 o versione successiva
- Il pacchetto Python `mcp` (installabile con `pip install mcp`)

### Installazione e Configurazione

1. Clona il repository o scarica i file della soluzione.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Crea e attiva un ambiente virtuale (consigliato):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Installa le dipendenze necessarie:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### File

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Esecuzione del Classico Server HTTP Streaming

1. Vai nella directory della soluzione:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Avvia il classico server HTTP streaming:

   ```pwsh
   python server.py
   ```

3. Il server si avvierà e mostrerà:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Esecuzione del Classico Client HTTP Streaming

1. Apri un nuovo terminale (attiva lo stesso ambiente virtuale e directory):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Dovresti vedere i messaggi trasmessi stampati in sequenza:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Esecuzione del Server MCP Streaming

1. Vai nella directory della soluzione:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Avvia il server MCP con il trasporto streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Il server si avvierà e mostrerà:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Esecuzione del Client MCP Streaming

1. Apri un nuovo terminale (attiva lo stesso ambiente virtuale e directory):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Dovresti vedere le notifiche stampate in tempo reale mentre il server elabora ogni elemento:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Passaggi Chiave per l'Implementazione

1. **Crea il server MCP utilizzando FastMCP.**
2. **Definisci uno strumento che elabora una lista e invia notifiche utilizzando `ctx.info()` o `ctx.log()`.**
3. **Esegui il server con `transport="streamable-http"`.**
4. **Implementa un client con un gestore di messaggi per mostrare le notifiche appena arrivano.**

### Analisi del Codice
- Il server utilizza funzioni asincrone e il contesto MCP per inviare aggiornamenti di avanzamento.
- Il client implementa un gestore di messaggi asincrono per stampare notifiche e il risultato finale.

### Suggerimenti e Risoluzione dei Problemi

- Usa `async/await` per operazioni non bloccanti.
- Gestisci sempre le eccezioni sia nel server che nel client per garantire robustezza.
- Testa con più client per osservare aggiornamenti in tempo reale.
- Se riscontri errori, verifica la versione di Python e assicurati che tutte le dipendenze siano installate.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
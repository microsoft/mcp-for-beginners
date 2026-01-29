# MCP stdio Server - Soluzione Python

> **⚠️ Importante**: Questa soluzione è stata aggiornata per utilizzare il **trasporto stdio** come raccomandato dalla Specifica MCP 2025-06-18. Il trasporto SSE originale è stato deprecato.

## Panoramica

Questa soluzione Python dimostra come costruire un server MCP utilizzando il trasporto stdio attuale. Il trasporto stdio è più semplice, più sicuro e offre prestazioni migliori rispetto all'approccio SSE deprecato.

## Prerequisiti

- Python 3.8 o successivo
- Si consiglia di installare `uv` per la gestione dei pacchetti, vedere [istruzioni](https://docs.astral.sh/uv/#highlights)

## Istruzioni di configurazione

### Passaggio 1: Creare un ambiente virtuale

```bash
python -m venv venv
```

### Passaggio 2: Attivare l'ambiente virtuale

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Passaggio 3: Installare le dipendenze

```bash
pip install mcp
```

## Avvio del Server

Il server stdio funziona in modo diverso rispetto al vecchio server SSE. Invece di avviare un server web, comunica tramite stdin/stdout:

```bash
python server.py
```

**Importante**: Il server sembrerà bloccarsi - è normale! Sta aspettando messaggi JSON-RPC da stdin.

## Test del Server

### Metodo 1: Utilizzo dell'MCP Inspector (Consigliato)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Questo farà:
1. Avviare il server come sottoprocesso
2. Aprire un'interfaccia web per il test
3. Permettere di testare tutti gli strumenti del server in modo interattivo

### Metodo 2: Test diretto con JSON-RPC

Puoi anche testare inviando messaggi JSON-RPC direttamente:

1. Avvia il server: `python server.py`
2. Invia un messaggio JSON-RPC (esempio):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Il server risponderà con gli strumenti disponibili

### Strumenti Disponibili

Il server fornisce questi strumenti:

- **add(a, b)**: Somma due numeri
- **multiply(a, b)**: Moltiplica due numeri  
- **get_greeting(name)**: Genera un saluto personalizzato
- **get_server_info()**: Ottieni informazioni sul server

### Test con Claude Desktop

Per utilizzare questo server con Claude Desktop, aggiungi questa configurazione al tuo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Differenze Chiave rispetto a SSE

**Trasporto stdio (Attuale):**
- ✅ Configurazione più semplice - non serve un server web
- ✅ Maggiore sicurezza - nessun endpoint HTTP
- ✅ Comunicazione basata su sottoprocessi
- ✅ JSON-RPC su stdin/stdout
- ✅ Prestazioni migliori

**Trasporto SSE (Deprecato):**
- ❌ Richiedeva la configurazione di un server HTTP
- ❌ Necessitava di un framework web (Starlette/FastAPI)
- ❌ Gestione di routing e sessioni più complessa
- ❌ Considerazioni aggiuntive sulla sicurezza
- ❌ Ora deprecato nella MCP 2025-06-18

## Suggerimenti per il Debug

- Usa `stderr` per il logging (mai `stdout`)
- Testa con l'Inspector per il debug visivo
- Assicurati che tutti i messaggi JSON siano delimitati da newline
- Controlla che il server si avvii senza errori

Questa soluzione segue la specifica MCP attuale e dimostra le migliori pratiche per l'implementazione del trasporto stdio.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
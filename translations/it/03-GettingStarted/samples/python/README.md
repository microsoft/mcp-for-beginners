# Server MCP Calculator (Python)

Una semplice implementazione del server Model Context Protocol (MCP) in Python che offre funzionalità di calcolatrice di base.

## Installazione

Installa le dipendenze necessarie:

```bash
pip install -r requirements.txt
```

Oppure installa direttamente l'SDK MCP per Python:

```bash
pip install mcp>=1.18.0
```

## Utilizzo

### Avvio del Server

Il server è progettato per essere utilizzato dai client MCP (come Claude Desktop). Per avviare il server:

```bash
python mcp_calculator_server.py
```

**Nota**: Quando eseguito direttamente in un terminale, vedrai errori di validazione JSON-RPC. Questo è un comportamento normale - il server sta aspettando messaggi formattati correttamente dai client MCP.

### Test delle Funzioni

Per verificare che le funzioni della calcolatrice funzionino correttamente:

```bash
python test_calculator.py
```

## Risoluzione dei Problemi

### Errori di Importazione

Se vedi `ModuleNotFoundError: No module named 'mcp'`, installa l'SDK MCP per Python:

```bash
pip install mcp>=1.18.0
```

### Errori JSON-RPC Durante l'Esecuzione Diretta

Errori come "Invalid JSON: EOF while parsing a value" durante l'esecuzione diretta del server sono previsti. Il server necessita di messaggi dai client MCP, non di input diretto dal terminale.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
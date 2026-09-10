# Server Calcolatore MCP (Python)



Una semplice implementazione server del Model Context Protocol (MCP) in Python che fornisce funzionalità basilari di calcolatrice.


## Installazione

Installa le dipendenze necessarie:

```bash
pip install -r requirements.txt
```

Oppure installa direttamente l’SDK MCP per Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Utilizzo

### Avvio del Server

Il server è progettato per essere utilizzato da client MCP (come Claude Desktop). Per avviare il server:

```bash
python mcp_calculator_server.py
```

**Nota**: Eseguendo direttamente in un terminale, vedrai errori di validazione JSON-RPC. Questo è comportamento normale - il server sta aspettando messaggi MCP da client formattati correttamente.

### Test delle Funzioni

Per testare che le funzioni della calcolatrice funzionino correttamente:

```bash
python test_calculator.py
```

## Risoluzione dei Problemi

### Errori di Importazione

Se visualizzi `ModuleNotFoundError: No module named 'mcp'`, installa l’SDK MCP per Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Errori JSON-RPC Quando Eseguito Direttamente

Errori come "Invalid JSON: EOF while parsing a value" quando si esegue direttamente il server sono previsti. Il server necessita di messaggi da client MCP, non di input diretto da terminale.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
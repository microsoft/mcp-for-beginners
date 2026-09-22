# Esegui l'esempio

> [!WARNING]
> Questo esempio utilizza Sampling deprecato e un endpoint HTTP+SSE legacy. È
> mantenuto per la compatibilità con MCP `2025-11-25`. Le nuove implementazioni
> dovrebbero chiamare direttamente un provider LLM e usare HTTP Streamable per il traffico MCP remoto.

## Crea un ambiente virtuale

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installa le dipendenze

```sh
pip install "mcp[cli]"
```

## Avvia il server

```sh
uvicorn server:app --port 8000
```

## Prova il server con GitHub Copilot e VS Code

Aggiungi la voce a mcp.json come segue:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Assicurati di cliccare su "start" per avviare il server.

Nel prompt di GitHub Copilot incolla quanto segue:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

La prima volta ti verrà chiesto se accettare un'azione Sampling, poi ti verrà chiesto di accettare l'esecuzione dello strumento "create_blog". Dovresti vedere una risposta simile a:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Voer de sample uit

> [!WARNING]
> Deze sample gebruikt verouderde Sampling en een legacy HTTP+SSE endpoint. Het wordt
> behouden voor compatibiliteit met MCP `2025-11-25`. Nieuwe implementaties moeten direct
> een LLM-provider aanroepen en Streamable HTTP gebruiken voor remote MCP-verkeer.

## Maak een virtuele omgeving aan

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installeer dependencies

```sh
pip install "mcp[cli]"
```

## Start de server

```sh
uvicorn server:app --port 8000
```

## Test de server met GitHub Copilot en VS Code

Voeg de entry toe aan mcp.json zoals volgt:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Zorg ervoor dat je op "start" klikt op de server.

Plak in GitHub Copilot de volgende prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

De eerste keer wordt je gevraagd of je een Sampling-actie accepteert, daarna word je gevraagd het tool te accepteren om "create_blog" uit te voeren. Je zou een reactie moeten zien zoals:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
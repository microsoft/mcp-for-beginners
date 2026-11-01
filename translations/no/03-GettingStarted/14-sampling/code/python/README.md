# Kjør eksempelet

> [!WARNING]
> Dette eksempelet bruker utdaterte Sampling og en legacy HTTP+SSE-endepunkt. Det er
> beholdt for MCP `2025-11-25` kompatibilitet. Nye implementasjoner bør kalle
> en LLM-leverandør direkte og bruke Streamable HTTP for ekstern MCP-trafikk.

## Opprett virtuelt miljø

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installer avhengigheter

```sh
pip install "mcp[cli]"
```

## Kjør serveren

```sh
uvicorn server:app --port 8000
```

## Test serveren med GitHub Copilot og VS Code

Legg til oppføringen i mcp.json slik:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Sørg for at du klikker på "start" på serveren.

I GitHub Copilot lim inn følgende prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Første gang vil du bli spurt om du vil godta en Sampling-handling, deretter vil du bli spurt om å godta verktøyet for å kjøre "create_blog". Du bør se et svar som ligner på:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
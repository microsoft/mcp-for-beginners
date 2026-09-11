# Kør eksemplet

> [!WARNING]
> Dette eksempel bruger forældet Sampling og en legacy HTTP+SSE-endpoint. Det er
> bevaret for MCP `2025-11-25` kompatibilitet. Nye implementeringer bør kalde
> en LLM-udbyder direkte og bruge Streamable HTTP til fjern-MCP-trafik.

## Opret virtuelt miljø

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installer afhængigheder

```sh
pip install "mcp[cli]"
```

## Kør serveren

```sh
uvicorn server:app --port 8000
```

## Test serveren med GitHub Copilot og VS Code

Tilføj posten til mcp.json som følger:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Sørg for at klikke på "start" på serveren.

Indsæt følgende prompt i GitHub Copilot:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Første gang bliver du spurgt, om du vil acceptere en Sampling-handling, og derefter bliver du bedt om at acceptere værktøjet til at køre "create_blog". Du bør se et svar der ligner:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
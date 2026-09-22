# Kör exemplet

> [!WARNING]
> Det här exemplet använder föråldrad Sampling och en legacy HTTP+SSE-endpoint. Det
> behålls för kompatibilitet med MCP `2025-11-25`. Nya implementationer bör anropa
> en LLM-leverantör direkt och använda Streamable HTTP för fjärr-MCP-trafik.

## Skapa en virtuell miljö

```sh
python -m venv venv
source ./venv/bin/activate
```

## Installera beroenden

```sh
pip install "mcp[cli]"
```

## Kör servern

```sh
uvicorn server:app --port 8000
```

## Testa servern med GitHub Copilot och VS Code

Lägg till posten i mcp.json så här:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Se till att du klickar på "start" på servern.

I GitHub Copilot, klistra in följande prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Första gången kommer du att bli tillfrågad om du vill acceptera en Sampling-action, sedan kommer du bli ombedd att acceptera verktyget för att köra "create_blog". Du bör se ett svar liknande:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
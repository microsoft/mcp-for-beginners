# Paleiskite pavyzdį

> [!WARNING]
> Šis pavyzdys naudoja pasenusią „Sampling“ funkciją ir seną HTTP+SSE galinį tašką. Jis
> išlaikytas MCP `2025-11-25` suderinamumui. Nauji įgyvendinimai turėtų tiesiogiai kviesti
> LLM tiekėją ir naudoti Streamable HTTP nuotoliniam MCP srautui.

## Sukurkite virtualią aplinką

```sh
python -m venv venv
source ./venv/bin/activate
```

## Įdiekite priklausomybes

```sh
pip install "mcp[cli]"
```

## Paleiskite serverį

```sh
uvicorn server:app --port 8000
```

## Išbandykite serverį su GitHub Copilot ir VS Code

Pridėkite įrašą į mcp.json taip:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Įsitikinkite, kad paspaudėte „start“ serveryje.

GitHub Copilot įklijuokite šią komandą:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Pirmą kartą būsite paprašyti patvirtinti Sampling veiksmą, tada turėsite sutikti, kad įrankis vykdytų „create_blog“. Turėtumėte pamatyti panašią atsakymą:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
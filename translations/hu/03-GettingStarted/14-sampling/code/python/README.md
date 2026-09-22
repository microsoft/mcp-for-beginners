# Futtassa a példát

> [!WARNING]
> Ez a példa egy elavult Samplinget és egy régi HTTP+SSE végpontot használ. Ez
> az MCP `2025-11-25` kompatibilitás miatt maradt meg. Az új megvalósításoknak közvetlenül
> egy LLM szolgáltatóhoz kell fordulniuk, és Streamable HTTP-t kell használniuk a távoli MCP forgalomhoz.

## Virtuális környezet létrehozása

```sh
python -m venv venv
source ./venv/bin/activate
```

## Függőségek telepítése

```sh
pip install "mcp[cli]"
```

## A szerver indítása

```sh
uvicorn server:app --port 8000
```

## Tesztelje a szervert a GitHub Copilottal és a VS Code-dal

Adja hozzá a bejegyzést a mcp.json-hez így:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Győződjön meg róla, hogy a szerveren a "start" gombra kattintott.

A GitHub Copilotban illessze be a következő promptot:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Először megkérdezi, hogy elfogadja-e a Sampling műveletet, majd azt, hogy elfogadja-e a "create_blog" eszköz futtatását. Olyan választ kell látnia, mint például:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
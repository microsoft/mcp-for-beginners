# Run di sample

> [!WARNING]
> Dis sample dey use old Sampling and one old HTTP+SSE endpoint. E still dey
> for MCP `2025-11-25` compatibility. New way be say make una call
> LLM provider direct and use Streamable HTTP for remote MCP traffic.

## Create virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]"
```

## Run di server

```sh
uvicorn server:app --port 8000
```

## Test di server wit GitHub Copilot and VS Code

Add di entry for mcp.json like dis:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Make sure say you click "start" for di server.

For GitHub Copilot paste di prompt wey follow:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Di first time dem go ask if you want accept Sampling action, afta dat dem go ask you accept the tool to run "create_blog". You go see response wey be like:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
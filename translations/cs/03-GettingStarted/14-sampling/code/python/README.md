# Spusťte ukázku

> [!WARNING]
> Tato ukázka používá zastaralý Sampling a starší HTTP+SSE endpoint. Je
> zachována pro kompatibilitu MCP `2025-11-25`. Nové implementace by měly volat
> poskytovatele LLM přímo a používat Streamable HTTP pro vzdálený provoz MCP.

## Vytvořte virtuální prostředí

```sh
python -m venv venv
source ./venv/bin/activate
```

## Nainstalujte závislosti

```sh
pip install "mcp[cli]"
```

## Spusťte server

```sh
uvicorn server:app --port 8000
```

## Otestujte server s GitHub Copilot a VS Code

Přidejte položku do mcp.json takto:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Ujistěte se, že na serveru kliknete na "start".

V GitHub Copilot vložte následující prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Poprvé budete dotázáni, zda chcete přijmout akci Sampling, poté budete požádáni o povolení spuštění nástroje "create_blog". Měli byste vidět odpověď podobnou:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
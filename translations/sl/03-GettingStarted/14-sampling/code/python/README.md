# Zaženi primer

> [!WARNING]
> Ta primer uporablja zastarelo vzorčenje in star HTTP+SSE konec. Ohranja se
> za združljivost MCP `2025-11-25`. Nove implementacije naj neposredno kličejo
> ponudnika LLM in uporabljajo pretočni HTTP za oddaljeni promet MCP.

## Ustvari virtualno okolje

```sh
python -m venv venv
source ./venv/bin/activate
```

## Namesti odvisnosti

```sh
pip install "mcp[cli]"
```

## Zaženi strežnik

```sh
uvicorn server:app --port 8000
```

## Preizkusi strežnik z GitHub Copilot in VS Code

Dodaj vnos v mcp.json takole:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Prepričaj se, da si kliknil "start" na strežniku.

V GitHub Copilot prilepi naslednji poziv:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Prvič boš vprašal, ali želiš sprejeti dejanje Sampling, nato boš moral sprejeti orodje za zagon "create_blog". Moral bi videti odgovor, podoben temu:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
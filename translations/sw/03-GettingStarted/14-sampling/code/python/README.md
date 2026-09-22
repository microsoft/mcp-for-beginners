# Endesha sampuli

> [!WARNING]
> Sampuli hii inatumia Sampling iliyotumika zamani na sehemu ya zamani ya HTTP+SSE. Imehifadhiwa kwa ajili ya ulinganifu wa MCP `2025-11-25`. Utekelezaji mpya unapaswa kupiga simu kwa mtoa LLM moja kwa moja na kutumia Streamable HTTP kwa trafiki ya MCP ya mbali.
> retained for MCP `2025-11-25` compatibility. New implementations should call
> an LLM provider directly and use Streamable HTTP for remote MCP traffic.

## Unda mazingira ya virtual

```sh
python -m venv venv
source ./venv/bin/activate
```

## Sakinisha utegemezi

```sh
pip install "mcp[cli]"
```

## Endesha seva

```sh
uvicorn server:app --port 8000
```

## Jaribu seva na GitHub Copilot na VS Code

Ongeza ingizo kwenye mcp.json kama ifuatavyo:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Hakikisha umebonyeza "anza" kwenye seva.

Katika GitHub Copilot weka wito lifuatalo:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Mara ya kwanza utaulizwa kama unakubali kitendo cha Sampling, kisha utaulizwa ukubali chombo kizifanye "create_blog". Unapaswa kuona majibu kama yafuatayo:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
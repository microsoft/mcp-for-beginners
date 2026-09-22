# Patakbuhin ang halimbawa

> [!WARNING]
> Ang halimbawang ito ay gumagamit ng deprecate na Sampling at lumang HTTP+SSE endpoint. Ito ay
> pinananatili para sa katugmang MCP `2025-11-25`. Ang mga bagong implementasyon ay dapat tumawag
> direkta sa tagapagbigay ng LLM at gumamit ng Streamable HTTP para sa remote MCP traffic.

## Gumawa ng virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Mag-install ng mga dependencies

```sh
pip install "mcp[cli]"
```

## Patakbuhin ang server

```sh
uvicorn server:app --port 8000
```

## Subukan ang server gamit ang GitHub Copilot at VS Code

Idagdag ang entry sa mcp.json tulad nito:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Siguraduhing i-click ang "start" sa server.

Sa GitHub Copilot, i-paste ang sumusunod na prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Sa unang pagkakataon, tatanungin ka kung tatanggapin mo ang isang Sampling action, pagkatapos ay tatanungin kang tanggapin ang tool para patakbuhin ang "create_blog". Makikita mo ang tugon na katulad nito:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
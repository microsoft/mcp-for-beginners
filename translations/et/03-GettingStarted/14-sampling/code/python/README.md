# Käivita näidis

> [!WARNING]
> See näidis kasutab aegunud proovi võtmist (Sampling) ja vananenud HTTP+SSE lõpp-punkti. See on
> säilitatud MCP `2025-11-25` ühilduvuse jaoks. Uued rakendused peaksid kutsuma otse LLM pakkujat
> ja kasutama voogedastatavat HTTP-d kaug-MCP liikluseks.

## Loo virtuaalne keskkond

```sh
python -m venv venv
source ./venv/bin/activate
```

## Paigalda sõltuvused

```sh
pip install "mcp[cli]"
```

## Käivita server

```sh
uvicorn server:app --port 8000
```

## Testi serverit GitHub Copiloti ja VS Code'iga

Lisa kirje mcp.json faili selliselt:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Veendu, et oled serveris klikkinud "start".

GitHub Copiloti liidesesse kleebi järgmine prompt:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Esimest korda küsitakse sinult, kas aktsepteerida proovi võtmise tegevust, seejärel kas aktsepteerida tööriista "create_blog" käivitamist. Sa peaksid nägema vastust sarnaselt:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
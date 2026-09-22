# Pokreni primjer

> [!WARNING]
> Ovaj primjer koristi zastarjeli Sampling i naslijeđeni HTTP+SSE endpoint. Zadržan je
> radi kompatibilnosti s MCP `2025-11-25`. Nove implementacije trebaju pozivati
> LLM pružatelja izravno i koristiti Streamable HTTP za udaljeni MCP promet.

## Stvori virtualno okruženje

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instaliraj ovisnosti

```sh
pip install "mcp[cli]"
```

## Pokreni server

```sh
uvicorn server:app --port 8000
```

## Testiraj server s GitHub Copilot i VS Code

Dodaj unos u mcp.json ovako:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Provjeri da si kliknuo "start" na serveru.

U GitHub Copilot zalijepi sljedeći upit:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Prvi put ćeš biti upitan hoćeš li prihvatiti Sampling akciju, zatim ćeš biti upitan da prihvatiš alat za pokretanje "create_blog". Trebao bi vidjeti odgovor sličan:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
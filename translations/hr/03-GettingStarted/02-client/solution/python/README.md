# Pokretanje ovog primjera

Preporučuje se instalacija `uv`, ali nije obavezno, vidi [upute](https://docs.astral.sh/uv/#highlights)

## -0- Kreirajte virtualno okruženje

```bash
python -m venv venv
```

## -1- Aktivirajte virtualno okruženje

```bash
venv\Scripts\activate
```

## -2- Instalirajte ovisnosti

```bash
pip install "mcp[cli]"
```

## -3- Pokrenite primjer

```bash
python client.py
```

Trebali biste vidjeti izlaz sličan:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
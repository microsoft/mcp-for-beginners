# Pokretanje ovog primjera

Preporučuje se instalacija `uv`, ali nije obavezno, vidi [upute](https://docs.astral.sh/uv/#highlights)

## -0- Kreiraj virtualno okruženje

```bash
python -m venv venv
```

## -1- Aktiviraj virtualno okruženje

```bash
venv\Scrips\activate
```

## -2- Instaliraj ovisnosti

```bash
pip install "mcp[cli]"
pip install openai
```

## -3- Konfiguriraj Microsoft Foundry

Postavi aktivni model poput `gpt-5.1` u Microsoft Foundry, zatim postavi:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

`AZURE_OPENAI_DEPLOYMENT` je naziv implementacije, koji se može razlikovati od
imena osnovnog modela. Pregledajte
[raspored ukidanja Microsoft Foundry modela](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
prije odabira modela.

## -4- Pokreni primjer


```bash
python client.py
```

Trebali biste vidjeti izlaz sličan:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
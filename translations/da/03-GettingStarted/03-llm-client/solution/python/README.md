# Kørsel af dette eksempel

Det anbefales at installere `uv`, men det er ikke et krav, se [instruktioner](https://docs.astral.sh/uv/#highlights)

## -0- Opret et virtuelt miljø

```bash
python -m venv venv
```

## -1- Aktiver det virtuelle miljø

```bash
venv\Scrips\activate
```

## -2- Installer afhængighederne

```bash
pip install "mcp[cli]"
pip install openai
```

## -3- Konfigurer Microsoft Foundry

Udrul en aktiv model såsom `gpt-5.1` i Microsoft Foundry, og sæt derefter:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

`AZURE_OPENAI_DEPLOYMENT` er udrulningsnavnet, som kan være forskelligt fra
den underliggende modelnavn. Tjek
[Microsoft Foundry model pensioneringsplan](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
før du vælger en model.

## -4- Kør eksemplet


```bash
python client.py
```

Du bør se en output som ligner:

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
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "24531f2b6b0f7fa3839accf4dc10088a",
  "translation_date": "2025-12-11T12:56:20+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/python/README.md",
  "language_code": "te"
}
-->
# ఈ నమూనాను నడపడం

మీకు `uv` ను ఇన్‌స్టాల్ చేయాలని సిఫార్సు చేయబడింది కానీ ఇది తప్పనిసరి కాదు, [సూచనలు](https://docs.astral.sh/uv/#highlights) చూడండి

## -0- ఒక వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి

```bash
python -m venv venv
```

## -1- వర్చువల్ ఎన్విరాన్‌మెంట్‌ను యాక్టివేట్ చేయండి

```bash
venv\Scrips\activate
```

## -2- డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- నమూనాను నడపండి


```bash
python client.py
```

మీరు ఈ విధమైన అవుట్‌పుట్‌ను చూడగలరు:

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
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
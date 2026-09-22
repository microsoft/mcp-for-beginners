# ఈ నమూనా 실행 చేయడం

మీరు `uv` ని ఇన్‌స్టాల్ చేయాలని సిఫార్సు చేయబడింది, కానీ ఇది తప్పనిసరి కాదు, చూడండి [సూచనలు](https://docs.astral.sh/uv/#highlights)

## -0- ఒక వర్చువల్ పరిసరాన్ని సృష్టించండి

```bash
python -m venv venv
```

## -1- వర్చువల్ పరిసరాన్ని సక్రియ పరచండి

```bash
venv\Scripts\activate
```

## -2- ఆధారాలను ఇన్‌స్టాల్ చేయండి

```bash
pip install "mcp[cli]"
```

## -3- నమూనా 실행 చేయండి

```bash
python client.py
```

మీరు ఈ తరహా అవుట్పుట్ చూడవచ్చు:

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
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
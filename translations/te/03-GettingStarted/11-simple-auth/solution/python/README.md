<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd28e690667b8ad84bb153cb025cfd73",
  "translation_date": "2025-12-11T13:22:06+00:00",
  "source_file": "03-GettingStarted/11-simple-auth/solution/python/README.md",
  "language_code": "te"
}
-->
# నమూనా నడపండి

## వాతావరణం సృష్టించండి

```sh
python -m venv venv
source ./venv/bin/activate
```

## ఆధారాలు ఇన్‌స్టాల్ చేయండి

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## టోకెన్ సృష్టించండి

క్లయింట్ సర్వర్‌తో మాట్లాడటానికి ఉపయోగించే టోకెన్‌ను మీరు సృష్టించాలి.

కాల్ చేయండి:

```sh
python util.py
```

## కోడ్ నడపండి

కోడ్‌ను ఇలా నడపండి:

```sh
python server.py
```

వేరే టెర్మినల్‌లో, టైప్ చేయండి:

```sh
python client.py
```

సర్వర్ టెర్మినల్‌లో, మీరు ఇలాంటిది చూడాలి:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

క్లయింట్ విండోలో, మీరు ఇలాంటి టెక్స్ట్ చూడాలి:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

అర్థం ఇది సక్రమంగా పనిచేస్తోంది

### విఫలమవుతుందో చూడటానికి సమాచారం మార్చండి

*server.py* లో ఈ కోడ్‌ను కనుగొనండి:

```python
 if not has_scope(has_header, "Admin.Write"):
```

దాన్ని "User.Write" అని మార్చండి. మీ ప్రస్తుత టోకెన్‌కు ఆ అనుమతి స్థాయి లేదు, కాబట్టి మీరు సర్వర్‌ను రీస్టార్ట్ చేసి క్లయింట్‌ను మళ్లీ నడిపితే, సర్వర్ టెర్మినల్‌లో క్రింది లాంటి లోపం కనిపిస్తుంది:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

మీరు మీ సర్వర్ కోడ్‌ను తిరిగి మార్చుకోవచ్చు లేదా ఈ అదనపు స్కోప్ ఉన్న కొత్త టోకెన్‌ను సృష్టించవచ్చు, ఇది మీపై ఆధారపడి ఉంటుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
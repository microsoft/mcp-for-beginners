<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f68294760a11dd3fdd175bd7f904a92",
  "translation_date": "2025-12-11T13:20:36+00:00",
  "source_file": "03-GettingStarted/11-simple-auth/code/basic/python/README.md",
  "language_code": "te"
}
-->
# నమూనా నడపండి

ఈ నమూనా ఒక MCP సర్వర్‌ను ప్రారంభిస్తుంది, ఇది చెల్లుబాటు అయ్యే Authorization హెడ్డర్‌ను తనిఖీ చేసే మిడిల్వేర్‌తో ఉంటుంది.

## డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి

```bash
pip install "mcp[cli]" 
```

## సర్వర్‌ను ప్రారంభించండి

```bash
python server.py
```

మరొక టెర్మినల్‌లో క్లయింట్‌ను ప్రారంభించండి

```bash
python client.py
```

మీకు ఈ విధమైన ఫలితం కనిపించాలి:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ఇది పంపబడుతున్న క్రెడెన్షియల్ అనుమతించబడుతోందని అర్థం.

`client.py` లో క్రెడెన్షియల్‌ను "secret-token2" గా మార్చి చూడండి, అప్పుడు మీరు ఈ టెక్స్ట్‌ను ప్రతిస్పందనలో భాగంగా చూడగలరు:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ఇది మీరు ధృవీకరించబడ్డారని (మీకు క్రెడెన్షియల్ ఉంది), కానీ అది చెల్లుబాటు కానిది అని అర్థం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులుండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవడం మంచిది. ఈ అనువాదం వలన కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
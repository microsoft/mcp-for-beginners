# இந்த மாதிரியை இயக்குதல்

நீங்கள் `uv` ஐ நிறுவ பரிந்துரைக்கப்படுகிறீர்கள் ஆனால் இது கட்டாயம் இல்லை, [instructions](https://docs.astral.sh/uv/#highlights) ஐ பார்க்கவும்

## -0- ஒரு பாராமரிப்பு சூழலை உருவாக்கவும்

```bash
python -m venv venv
```

## -1- பாராமரிப்பு சூழலை இயக்கவும்

```bash
venv\Scripts\activate
```

## -2- தேவையான தொகுதிகளை நிறுவவும்

```bash
pip install "mcp[cli]"
```

## -3- மாதிரியை இயக்கவும்

```bash
python client.py
```

நீங்கள் இதுபோன்ற ஒரு வெளியீட்டை காண வேண்டும்:

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
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
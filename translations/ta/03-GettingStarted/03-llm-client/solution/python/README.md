# இந்த உதாரணத்தை இயக்குவது

`uv` நிறுவ பரிந்துரைக்கப்படுகிறது, ஆனால் இது கட்டாயம் அல்ல, [வழிமுறைகளை](https://docs.astral.sh/uv/#highlights) பார்க்கவும்

## -0- ஒரு மெய்நிகர் சூழலை உருவாக்கவும்

```bash
python -m venv venv
```

## -1- மெய்நிகர் சூழலை செயல்படுத்தவும்

```bash
venv\Scrips\activate
```

## -2- தேவையான பொருட்களை நிறுவவும்

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- உதாரணத்தை இயக்கவும்

```bash
python client.py
```

நீங்கள் இதற்கு ஒத்த ஒரு வெளியீட்டை காணலாம்:

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

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.
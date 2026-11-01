# இந்த மாதிரியை இயக்குவது

நீங்கள் `uv` ஐ நிறுவ பரிந்துரைக்கப்படுகிறீர்கள், ஆனால் அது அவசியம் இல்லை, பாருங்கள் [வழிமுறைகள்](https://docs.astral.sh/uv/#highlights)

## -0- ஒரு மெய்நிகர் சூழலை உருவாக்கவும்

```bash
python -m venv venv
```

## -1- மெய்நிகர் சூழலை செயல்படுத்தவும்

```bash
venv\Scrips\activate
```

## -2- தேவையான சார்புகளை நிறுவவும்

```bash
pip install "mcp[cli]"
pip install openai
```

## -3- Microsoft Foundry-ஐ அமைக்கவும்

Microsoft Foundry-இல் `gpt-5.1` போன்ற செயலில் உள்ள மாடலை நிறுவி, பின்னர் அமைக்க:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

`AZURE_OPENAI_DEPLOYMENT` என்பது deployment பெயராகும்; அது அடிப்படை மாடல் பெயரிலிருந்து மாறியிருக்கலாம்.
சரிபார்க்கவும்
[Microsoft Foundry மாடல் ஓய்வு அட்டவணை](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
மாடலைத் தேர்வு செய்வதற்கு முன்னர்.

## -4- உதாரணத்தை இயக்கவும்


```bash
python client.py
```

பின்வருமாறு ஒரு வெளியீட்டை நீங்கள் காணலாம்:

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
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
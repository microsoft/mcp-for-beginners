# இந்த மாதிரியை இயக்குவது

Python பயன்படுத்தி பாரம்பரிய HTTP ஸ்ட்ரீமிங் சர்வர் மற்றும் கிளையண்ட், MCP ஸ்ட்ரீமிங் சர்வர் மற்றும் கிளையண்ட் ஆகியவற்றை எப்படி இயக்குவது என்பதை இங்கே காணலாம்.

### மேலோட்டம்

- நீங்கள் MCP சர்வரை அமைத்து, அது பொருட்களை செயல்படுத்தும் போது முன்னேற்ற அறிவிப்புகளை கிளையண்டுக்கு ஸ்ட்ரீம் செய்யும்.
- கிளையண்ட் ஒவ்வொரு அறிவிப்பையும் நேரடியாக காட்டும்.
- இந்த வழிகாட்டி முன் தேவைகள், அமைப்பு, இயக்கம் மற்றும் பிழை தீர்க்கும் முறைகளை உள்ளடக்கியது.

### முன் தேவைகள்

- Python 3.9 அல்லது அதற்கு மேற்பட்டது
- `mcp` Python தொகுப்பு (இதை `pip install mcp` மூலம் நிறுவவும்)

### நிறுவல் மற்றும் அமைப்பு

1. ரெப்போசிடரி கிளோன் செய்யவும் அல்லது தீர்வு கோப்புகளை பதிவிறக்கவும்.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **ஒரு வर्चுவல் சூழலை உருவாக்கி, செயல்படுத்தவும் (பரிந்துரைக்கப்படுகிறது):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **தேவையான சார்புகளை நிறுவவும்:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### கோப்புகள்

- **சர்வர்:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **கிளையண்ட்:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### பாரம்பரிய HTTP ஸ்ட்ரீமிங் சர்வரை இயக்குவது

1. தீர்வு கோப்பகத்துக்கு செல்லவும்:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. பாரம்பரிய HTTP ஸ்ட்ரீமிங் சர்வரை தொடங்கவும்:

   ```pwsh
   python server.py
   ```

3. சர்வர் தொடங்கும் மற்றும் கீழ்கண்டதை காட்டும்:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### பாரம்பரிய HTTP ஸ்ட்ரீமிங் கிளையண்டை இயக்குவது

1. புதிய டெர்மினலை திறக்கவும் (அதே வर्चுவல் சூழல் மற்றும் கோப்பகத்தை செயல்படுத்தவும்):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. ஸ்ட்ரீம் செய்யப்பட்ட செய்திகளை தொடர்ச்சியாக அச்சிடப்பட்டதை காணலாம்:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP ஸ்ட்ரீமிங் சர்வரை இயக்குவது

1. தீர்வு கோப்பகத்துக்கு செல்லவும்:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP சர்வரை streamable-http போக்குவரத்துடன் தொடங்கவும்:
   ```pwsh
   python server.py mcp
   ```
3. சர்வர் தொடங்கும் மற்றும் கீழ்கண்டதை காட்டும்:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP ஸ்ட்ரீமிங் கிளையண்டை இயக்குவது

1. புதிய டெர்மினலை திறக்கவும் (அதே வर्चுவல் சூழல் மற்றும் கோப்பகத்தை செயல்படுத்தவும்):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. சர்வர் ஒவ்வொரு பொருளையும் செயல்படுத்தும் போது நேரடியாக அறிவிப்புகளை அச்சிடப்பட்டதை காணலாம்:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### முக்கிய செயல்பாட்டு படிகள்

1. **FastMCP பயன்படுத்தி MCP சர்வரை உருவாக்கவும்.**
2. **ஒரு கருவியை வரையறுக்கவும், இது ஒரு பட்டியலை செயல்படுத்தி `ctx.info()` அல்லது `ctx.log()` மூலம் அறிவிப்புகளை அனுப்பும்.**
3. **`transport="streamable-http"` மூலம் சர்வரை இயக்கவும்.**
4. **அறிவிப்புகளை வருகை தரும் போது காட்ட ஒரு செய்தி கையாளுநருடன் கிளையண்டை செயல்படுத்தவும்.**

### குறியீட்டு விளக்கம்
- சர்வர் async செயல்பாடுகளை MCP சூழலை பயன்படுத்தி முன்னேற்றத்தைப் புதுப்பிக்க அனுப்புகிறது.
- கிளையண்ட் async செய்தி கையாளுநரை செயல்படுத்தி அறிவிப்புகளை மற்றும் இறுதி முடிவை அச்சிடுகிறது.

### குறிப்புகள் மற்றும் பிழை தீர்க்கும் முறை

- non-blocking செயல்பாடுகளுக்கு `async/await` பயன்படுத்தவும்.
- சர்வர் மற்றும் கிளையண்டில் பிழைகளை கையாளவும், இது வலுவான செயல்பாட்டை உறுதிசெய்யும்.
- பல கிளையண்ட்களுடன் சோதனை செய்து நேரடி புதுப்பிப்புகளை கவனிக்கவும்.
- பிழைகள் ஏற்பட்டால், உங்கள் Python பதிப்பை சரிபார்க்கவும் மற்றும் அனைத்து சார்புகளும் நிறுவப்பட்டுள்ளதா என்பதை உறுதிசெய்யவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
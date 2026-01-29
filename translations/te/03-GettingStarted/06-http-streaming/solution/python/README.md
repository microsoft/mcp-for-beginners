# ఈ నమూనాను నడపడం

క్లాసిక్ HTTP స్ట్రీమింగ్ సర్వర్ మరియు క్లయింట్, అలాగే MCP స్ట్రీమింగ్ సర్వర్ మరియు క్లయింట్‌ను Python ఉపయోగించి ఎలా నడపాలో ఇక్కడ ఉంది.

### అవలోకనం

- మీరు ఒక MCP సర్వర్‌ను సెటప్ చేస్తారు, ఇది ఐటెమ్స్‌ను ప్రాసెస్ చేస్తూ క్లయింట్‌కు ప్రోగ్రెస్ నోటిఫికేషన్లను స్ట్రీమ్ చేస్తుంది.
- క్లయింట్ ప్రతి నోటిఫికేషన్‌ను రియల్ టైంలో ప్రదర్శిస్తుంది.
- ఈ గైడ్ ప్రీరిక్విజిట్స్, సెటప్, నడపడం, మరియు ట్రబుల్‌షూటింగ్‌ను కవర్ చేస్తుంది.

### ప్రీరిక్విజిట్స్

- Python 3.9 లేదా కొత్త వెర్షన్
- `mcp` Python ప్యాకేజ్ (ఇన్‌స్టాల్ చేయడానికి `pip install mcp`)

### ఇన్‌స్టాలేషన్ & సెటప్

1. రిపోజిటరీని క్లోన్ చేయండి లేదా సొల్యూషన్ ఫైళ్లను డౌన్లోడ్ చేసుకోండి.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి యాక్టివేట్ చేయండి (సిఫార్సు చేయబడింది):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **అవసరమైన డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ఫైళ్లు

- **సర్వర్:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **క్లయింట్:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### క్లాసిక్ HTTP స్ట్రీమింగ్ సర్వర్ నడపడం

1. సొల్యూషన్ డైరెక్టరీకి వెళ్లండి:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. క్లాసిక్ HTTP స్ట్రీమింగ్ సర్వర్‌ను ప్రారంభించండి:

   ```pwsh
   python server.py
   ```

3. సర్వర్ ప్రారంభమై ఈ క్రింది మెసేజ్‌ను ప్రదర్శిస్తుంది:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### క్లాసిక్ HTTP స్ట్రీమింగ్ క్లయింట్ నడపడం

1. కొత్త టెర్మినల్ ఓపెన్ చేయండి (అదే వర్చువల్ ఎన్విరాన్‌మెంట్ మరియు డైరెక్టరీ యాక్టివేట్ చేయండి):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. స్ట్రీమ్ అయిన సందేశాలు వరుసగా ప్రింట్ అవుతాయని మీరు చూడగలరు:

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

### MCP స్ట్రీమింగ్ సర్వర్ నడపడం

1. సొల్యూషన్ డైరెక్టరీకి వెళ్లండి:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. streamable-http ట్రాన్స్‌పోర్ట్‌తో MCP సర్వర్‌ను ప్రారంభించండి:
   ```pwsh
   python server.py mcp
   ```
3. సర్వర్ ప్రారంభమై ఈ క్రింది మెసేజ్‌ను ప్రదర్శిస్తుంది:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP స్ట్రీమింగ్ క్లయింట్ నడపడం

1. కొత్త టెర్మినల్ ఓపెన్ చేయండి (అదే వర్చువల్ ఎన్విరాన్‌మెంట్ మరియు డైరెక్టరీ యాక్టివేట్ చేయండి):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. సర్వర్ ప్రతి ఐటెమ్‌ను ప్రాసెస్ చేస్తూ నోటిఫికేషన్లు రియల్ టైంలో ప్రింట్ అవుతాయని మీరు చూడగలరు:
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

### ముఖ్య అమలు దశలు

1. **FastMCP ఉపయోగించి MCP సర్వర్‌ను సృష్టించండి.**
2. **ఒక టూల్‌ను నిర్వచించండి, ఇది ఒక జాబితాను ప్రాసెస్ చేసి `ctx.info()` లేదా `ctx.log()` ఉపయోగించి నోటిఫికేషన్లు పంపుతుంది.**
3. **`transport="streamable-http"` తో సర్వర్‌ను నడపండి.**
4. **నోటిఫికేషన్లు వచ్చినప్పుడు ప్రదర్శించడానికి మెసేజ్ హ్యాండ్లర్‌తో క్లయింట్‌ను అమలు చేయండి.**

### కోడ్ వాక్‌త్రూ
- సర్వర్ అసింక్ ఫంక్షన్లు మరియు MCP కాంటెక్స్ట్ ఉపయోగించి ప్రోగ్రెస్ అప్‌డేట్లను పంపుతుంది.
- క్లయింట్ అసింక్ మెసేజ్ హ్యాండ్లర్ అమలు చేసి నోటిఫికేషన్లు మరియు తుది ఫలితాన్ని ప్రింట్ చేస్తుంది.

### సూచనలు & ట్రబుల్‌షూటింగ్

- నాన్-బ్లాకింగ్ ఆపరేషన్ల కోసం `async/await` ఉపయోగించండి.
- సర్వర్ మరియు క్లయింట్ రెండింటిలోనూ ఎక్సెప్షన్లను ఎప్పుడూ హ్యాండిల్ చేయండి.
- రియల్ టైం అప్‌డేట్లను గమనించడానికి బహుళ క్లయింట్లతో పరీక్షించండి.
- ఎర్రర్లు వస్తే, మీ Python వెర్షన్‌ను తనిఖీ చేసి అన్ని డిపెండెన్సీలు ఇన్‌స్టాల్ అయ్యాయో లేదో చూసుకోండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
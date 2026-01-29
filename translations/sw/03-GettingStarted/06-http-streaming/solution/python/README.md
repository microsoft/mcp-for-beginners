# Kuendesha Sampuli Hii

Hapa kuna jinsi ya kuendesha seva na mteja wa kawaida wa HTTP streaming, pamoja na seva na mteja wa MCP streaming kwa kutumia Python.

### Muhtasari

- Utaunda seva ya MCP inayotuma arifa za maendeleo kwa mteja wakati inachakata vitu.
- Mteja ataonyesha kila arifa kwa wakati halisi.
- Mwongozo huu unashughulikia mahitaji ya awali, usanidi, uendeshaji, na utatuzi wa matatizo.

### Mahitaji ya Awali

- Python 3.9 au toleo jipya zaidi
- Kifurushi cha Python `mcp` (sakinisha kwa `pip install mcp`)

### Usakinishaji na Usanidi

1. Clone hifadhi au pakua faili za suluhisho.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Unda na uwashe mazingira ya kawaida (inapendekezwa):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Sakinisha utegemezi unaohitajika:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Faili

- **Seva:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Mteja:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Kuendesha Seva ya Kawaida ya HTTP Streaming

1. Nenda kwenye saraka ya suluhisho:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Anzisha seva ya kawaida ya HTTP streaming:

   ```pwsh
   python server.py
   ```

3. Seva itaanza na kuonyesha:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Kuendesha Mteja wa Kawaida wa HTTP Streaming

1. Fungua terminal mpya (washa mazingira sawa ya kawaida na saraka):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Utapaswa kuona ujumbe wa streaming ukichapishwa kwa mpangilio:

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

### Kuendesha Seva ya MCP Streaming

1. Nenda kwenye saraka ya suluhisho:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Anzisha seva ya MCP kwa kutumia usafirishaji wa streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Seva itaanza na kuonyesha:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Kuendesha Mteja wa MCP Streaming

1. Fungua terminal mpya (washa mazingira sawa ya kawaida na saraka):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Utapaswa kuona arifa zikichapishwa kwa wakati halisi wakati seva inachakata kila kipengee:
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

### Hatua Muhimu za Utekelezaji

1. **Unda seva ya MCP kwa kutumia FastMCP.**
2. **Fafanua zana inayochakata orodha na kutuma arifa kwa kutumia `ctx.info()` au `ctx.log()`.**
3. **Endesha seva kwa `transport="streamable-http"`.**
4. **Tekeleza mteja mwenye mshughulikiaji wa ujumbe ili kuonyesha arifa zinapowasili.**

### Muhtasari wa Msimbo
- Seva inatumia kazi za async na muktadha wa MCP kutuma masasisho ya maendeleo.
- Mteja hutekeleza mshughulikiaji wa ujumbe wa async ili kuchapisha arifa na matokeo ya mwisho.

### Vidokezo na Utatuzi wa Matatizo

- Tumia `async/await` kwa operesheni zisizo na vizuizi.
- Daima shughulikia vizuizi katika seva na mteja kwa uimara.
- Jaribu na wateja wengi ili kuona masasisho ya wakati halisi.
- Ukikumbana na makosa, angalia toleo lako la Python na hakikisha utegemezi wote umesakinishwa.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
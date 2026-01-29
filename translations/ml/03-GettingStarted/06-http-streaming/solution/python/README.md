# ഈ സാമ്പിൾ പ്രവർത്തിപ്പിക്കൽ

ക്ലാസിക് HTTP സ്ട്രീമിംഗ് സെർവർ, ക്ലയന്റ്, കൂടാതെ MCP സ്ട്രീമിംഗ് സെർവർ, ക്ലയന്റ് Python ഉപയോഗിച്ച് എങ്ങനെ പ്രവർത്തിപ്പിക്കാമെന്ന് ഇവിടെ കാണിക്കുന്നു.

### അവലോകനം

- നിങ്ങൾ ഒരു MCP സെർവർ സജ്ജീകരിക്കും, ഇത് ഐറ്റങ്ങൾ പ്രോസസ്സ് ചെയ്യുമ്പോൾ ക്ലയന്റിന് പ്രോഗ്രസ് അറിയിപ്പുകൾ സ്ട്രീം ചെയ്യും.
- ക്ലയന്റ് ഓരോ അറിയിപ്പും യഥാർത്ഥ സമയത്ത് പ്രദർശിപ്പിക്കും.
- ഈ ഗൈഡ് മുൻകൂട്ടി ആവശ്യങ്ങൾ, സജ്ജീകരണം, പ്രവർത്തനം, പ്രശ്നപരിഹാരം എന്നിവ ഉൾക്കൊള്ളുന്നു.

### മുൻകൂട്ടി ആവശ്യങ്ങൾ

- Python 3.9 അല്ലെങ്കിൽ പുതിയത്
- `mcp` Python പാക്കേജ് (`pip install mcp` ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യുക)

### ഇൻസ്റ്റലേഷൻ & സജ്ജീകരണം

1. റിപ്പോസിറ്ററി ക്ലോൺ ചെയ്യുക അല്ലെങ്കിൽ സൊല്യൂഷൻ ഫയലുകൾ ഡൗൺലോഡ് ചെയ്യുക.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ച് ആക്ടിവേറ്റ് ചെയ്യുക (ശുപാർശ ചെയ്യുന്നു):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **ആവശ്യമായ ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ഫയലുകൾ

- **സെർവർ:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ക്ലയന്റ്:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### ക്ലാസിക് HTTP സ്ട്രീമിംഗ് സെർവർ പ്രവർത്തിപ്പിക്കൽ

1. സൊല്യൂഷൻ ഡയറക്ടറിയിലേക്ക് പോകുക:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. ക്ലാസിക് HTTP സ്ട്രീമിംഗ് സെർവർ ആരംഭിക്കുക:

   ```pwsh
   python server.py
   ```

3. സെർവർ ആരംഭിച്ച് താഴെ കാണിക്കുന്നതു പ്രദർശിപ്പിക്കും:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ക്ലാസിക് HTTP സ്ട്രീമിംഗ് ക്ലയന്റ് പ്രവർത്തിപ്പിക്കൽ

1. പുതിയ ടെർമിനൽ തുറക്കുക (അതിനകം സജ്ജീകരിച്ച വെർച്വൽ എൻവയോൺമെന്റ്, ഡയറക്ടറി ആക്ടിവേറ്റ് ചെയ്യുക):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. സ്ട്രീമിംഗ് സന്ദേശങ്ങൾ ക്രമമായി പ്രിന്റ് ചെയ്യുന്നത് കാണാം:

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

### MCP സ്ട്രീമിംഗ് സെർവർ പ്രവർത്തിപ്പിക്കൽ

1. സൊല്യൂഷൻ ഡയറക്ടറിയിലേക്ക് പോകുക:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. streamable-http ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ ആരംഭിക്കുക:
   ```pwsh
   python server.py mcp
   ```
3. സെർവർ ആരംഭിച്ച് താഴെ കാണിക്കുന്നതു പ്രദർശിപ്പിക്കും:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP സ്ട്രീമിംഗ് ക്ലയന്റ് പ്രവർത്തിപ്പിക്കൽ

1. പുതിയ ടെർമിനൽ തുറക്കുക (അതിനകം സജ്ജീകരിച്ച വെർച്വൽ എൻവയോൺമെന്റ്, ഡയറക്ടറി ആക്ടിവേറ്റ് ചെയ്യുക):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. സെർവർ ഓരോ ഐറ്റവും പ്രോസസ്സ് ചെയ്യുമ്പോൾ അറിയിപ്പുകൾ യഥാർത്ഥ സമയത്ത് പ്രിന്റ് ചെയ്യുന്നത് കാണാം:
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

### പ്രധാന നടപ്പാക്കൽ ഘട്ടങ്ങൾ

1. **FastMCP ഉപയോഗിച്ച് MCP സെർവർ സൃഷ്ടിക്കുക.**
2. **ഒരു ടൂൾ നിർവചിക്കുക, ഇത് ഒരു ലിസ്റ്റ് പ്രോസസ്സ് ചെയ്ത് `ctx.info()` അല്ലെങ്കിൽ `ctx.log()` ഉപയോഗിച്ച് അറിയിപ്പുകൾ അയയ്ക്കും.**
3. **`transport="streamable-http"` ഉപയോഗിച്ച് സെർവർ പ്രവർത്തിപ്പിക്കുക.**
4. **അറിയിപ്പുകൾ എത്തുമ്പോൾ പ്രദർശിപ്പിക്കാൻ മെസേജ് ഹാൻഡ്ലർ ഉള്ള ക്ലയന്റ് നടപ്പിലാക്കുക.**

### കോഡ് വിശദീകരണം
- സെർവർ അസിങ്ക് ഫംഗ്ഷനുകളും MCP കോൺടെക്സ്റ്റും ഉപയോഗിച്ച് പ്രോഗ്രസ് അപ്‌ഡേറ്റുകൾ അയയ്ക്കുന്നു.
- ക്ലയന്റ് അസിങ്ക് മെസേജ് ഹാൻഡ്ലർ നടപ്പിലാക്കി അറിയിപ്പുകളും അന്തിമ ഫലവും പ്രിന്റ് ചെയ്യുന്നു.

### ടിപ്പുകൾ & പ്രശ്നപരിഹാരം

- ബ്ലോക്ക് ചെയ്യാത്ത പ്രവർത്തനങ്ങൾക്ക് `async/await` ഉപയോഗിക്കുക.
- സെർവർ, ക്ലയന്റ് ഇരുവർക്കും എക്സെപ്ഷനുകൾ കൈകാര്യം ചെയ്യുക.
- യഥാർത്ഥ സമയ അപ്‌ഡേറ്റുകൾ കാണാൻ ബഹുഭൂരിഭാഗം ക്ലയന്റുകളുമായി പരീക്ഷിക്കുക.
- പിശകുകൾ ഉണ്ടെങ്കിൽ Python പതിപ്പ് പരിശോധിച്ച് എല്ലാ ഡിപ്പൻഡൻസികളും ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Pagsasagawa ng Halimbawang Ito

Narito kung paano patakbuhin ang classic HTTP streaming server at client, pati na rin ang MCP streaming server at client gamit ang Python.

### Pangkalahatang-ideya

- Magse-set up ka ng isang MCP server na magpapadala ng mga progress notification sa client habang pinoproseso nito ang mga item.
- Ipapakita ng client ang bawat notification nang real-time.
- Saklaw ng gabay na ito ang mga kinakailangan, setup, pagpapatakbo, at pag-aayos ng mga problema.

### Mga Kinakailangan

- Python 3.9 o mas bago
- Ang `mcp` na Python package (i-install gamit ang `pip install mcp`)

### Pag-install at Setup

1. I-clone ang repository o i-download ang mga solution file.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Gumawa at i-activate ang isang virtual environment (inirerekomenda):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **I-install ang mga kinakailangang dependency:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Mga File

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Pagpapatakbo ng Classic HTTP Streaming Server

1. Pumunta sa solution directory:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Simulan ang classic HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Magsisimula ang server at magpapakita ng:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Pagpapatakbo ng Classic HTTP Streaming Client

1. Magbukas ng bagong terminal (i-activate ang parehong virtual environment at direktoryo):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Makikita mo ang mga streamed na mensahe na ipinapakita nang sunud-sunod:

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

### Pagpapatakbo ng MCP Streaming Server

1. Pumunta sa solution directory:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Simulan ang MCP server gamit ang streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. Magsisimula ang server at magpapakita ng:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Pagpapatakbo ng MCP Streaming Client

1. Magbukas ng bagong terminal (i-activate ang parehong virtual environment at direktoryo):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Makikita mo ang mga notification na ipinapakita nang real-time habang pinoproseso ng server ang bawat item:
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

### Mga Pangunahing Hakbang sa Implementasyon

1. **Gumawa ng MCP server gamit ang FastMCP.**
2. **Mag-define ng tool na nagpoproseso ng listahan at nagpapadala ng mga notification gamit ang `ctx.info()` o `ctx.log()`.**
3. **Patakbuhin ang server gamit ang `transport="streamable-http"`.**
4. **Mag-implement ng client na may message handler para ipakita ang mga notification habang dumarating ang mga ito.**

### Paglalahad ng Code
- Gumagamit ang server ng async functions at MCP context para magpadala ng mga progress update.
- Ang client ay nag-iimplement ng async message handler para mag-print ng mga notification at ang panghuling resulta.

### Mga Tip at Pag-aayos ng Problema

- Gumamit ng `async/await` para sa mga non-blocking na operasyon.
- Laging mag-handle ng exceptions sa parehong server at client para sa mas matibay na sistema.
- Subukan gamit ang maraming client upang makita ang real-time na mga update.
- Kung makakaranas ng mga error, suriin ang iyong Python version at tiyaking naka-install ang lahat ng dependency.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
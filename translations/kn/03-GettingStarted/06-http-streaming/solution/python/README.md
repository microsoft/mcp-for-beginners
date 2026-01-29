# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

ಕ್ಲಾಸಿಕ್ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್, ಹಾಗೆಯೇ MCP ಸ್ಟ್ರೀಮಿಂಗ್ ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್ ಅನ್ನು Python ಬಳಸಿ ಹೇಗೆ ಚಾಲನೆ ಮಾಡುವುದು ಎಂಬುದನ್ನು ಇಲ್ಲಿ ವಿವರಿಸಲಾಗಿದೆ.

### ಅವಲೋಕನ

- ನೀವು ಐಟಂಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವಾಗ ಪ್ರಗತಿ ಸೂಚನೆಗಳನ್ನು ಕ್ಲೈಂಟ್‌ಗೆ ಸ್ಟ್ರೀಮ್ ಮಾಡುವ MCP ಸರ್ವರ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುತ್ತೀರಿ.
- ಕ್ಲೈಂಟ್ ಪ್ರತಿ ಸೂಚನೆಯನ್ನು ನೈಜ ಸಮಯದಲ್ಲಿ ಪ್ರದರ್ಶಿಸುತ್ತದೆ.
- ಈ ಮಾರ್ಗದರ್ಶಿ ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು, ಸೆಟ್ ಅಪ್, ಚಾಲನೆ ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರವನ್ನು ಒಳಗೊಂಡಿದೆ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

- Python 3.9 ಅಥವಾ ಹೊಸದು
- `mcp` Python ಪ್ಯಾಕೇಜ್ (`pip install mcp` ಮೂಲಕ ಸ್ಥಾಪಿಸಿ)

### ಸ್ಥಾಪನೆ ಮತ್ತು ಸೆಟ್ ಅಪ್

1. ರೆಪೊಸಿಟರಿ ಕ್ಲೋನ್ ಮಾಡಿ ಅಥವಾ ಪರಿಹಾರ ಫೈಲ್‌ಗಳನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **ಅವಶ್ಯಕ ಡಿಪೆಂಡೆನ್ಸಿಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ಫೈಲ್‌ಗಳು

- **ಸರ್ವರ್:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ಕ್ಲೈಂಟ್:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### ಕ್ಲಾಸಿಕ್ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ ಸರ್ವರ್ ಚಾಲನೆ

1. ಪರಿಹಾರ ಡೈರೆಕ್ಟರಿಯ ಕಡೆಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. ಕ್ಲಾಸಿಕ್ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ:

   ```pwsh
   python server.py
   ```

3. ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗಿ ಈ ಕೆಳಗಿನಂತೆ ಪ್ರದರ್ಶಿಸುತ್ತದೆ:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ಕ್ಲಾಸಿಕ್ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ ಕ್ಲೈಂಟ್ ಚಾಲನೆ

1. ಹೊಸ ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ (ಅದೇ ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಮತ್ತು ಡೈರೆಕ್ಟರಿಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. ಸ್ಟ್ರೀಮ್ ಮಾಡಿದ ಸಂದೇಶಗಳು ಕ್ರಮವಾಗಿ ಮುದ್ರಿತವಾಗುತ್ತವೆ:

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

### MCP ಸ್ಟ್ರೀಮಿಂಗ್ ಸರ್ವರ್ ಚಾಲನೆ

1. ಪರಿಹಾರ ಡೈರೆಕ್ಟರಿಯ ಕಡೆಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. streamable-http ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್ ಬಳಸಿ MCP ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ:
   ```pwsh
   python server.py mcp
   ```
3. ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗಿ ಈ ಕೆಳಗಿನಂತೆ ಪ್ರದರ್ಶಿಸುತ್ತದೆ:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP ಸ್ಟ್ರೀಮಿಂಗ್ ಕ್ಲೈಂಟ್ ಚಾಲನೆ

1. ಹೊಸ ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ (ಅದೇ ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ಮತ್ತು ಡೈರೆಕ್ಟರಿಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. ಸರ್ವರ್ ಪ್ರತಿ ಐಟಂ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವಂತೆ ನೈಜ ಸಮಯದಲ್ಲಿ ಸೂಚನೆಗಳು ಮುದ್ರಿತವಾಗುತ್ತವೆ:
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

### ಪ್ರಮುಖ ಅನುಷ್ಠಾನ ಹಂತಗಳು

1. **FastMCP ಬಳಸಿ MCP ಸರ್ವರ್ ರಚಿಸಿ.**
2. **ಪಟ್ಟಿಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವ ಮತ್ತು `ctx.info()` ಅಥವಾ `ctx.log()` ಬಳಸಿ ಸೂಚನೆಗಳನ್ನು ಕಳುಹಿಸುವ ಟೂಲ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ.**
3. **`transport="streamable-http"` ಬಳಸಿ ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ.**
4. **ಸೂಚನೆಗಳು ಬಂದಂತೆ ಪ್ರದರ್ಶಿಸಲು ಸಂದೇಶ ಹ್ಯಾಂಡ್ಲರ್ ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.**

### ಕೋಡ್ ವಾಕ್‌ಥ್ರೂ
- ಸರ್ವರ್ ಅಸಿಂಕ್ ಫಂಕ್ಷನ್‌ಗಳು ಮತ್ತು MCP ಕಾಂಟೆಕ್ಸ್ಟ್ ಬಳಸಿ ಪ್ರಗತಿ ನವೀಕರಣಗಳನ್ನು ಕಳುಹಿಸುತ್ತದೆ.
- ಕ್ಲೈಂಟ್ ಅಸಿಂಕ್ ಸಂದೇಶ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ ಸೂಚನೆಗಳು ಮತ್ತು ಅಂತಿಮ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

### ಸಲಹೆಗಳು ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರ

- ನಾನ್-ಬ್ಲಾಕಿಂಗ್ ಕಾರ್ಯಗಳಿಗೆ `async/await` ಬಳಸಿ.
- ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್ ಎರಡರಲ್ಲಿಯೂ ದೋಷಗಳನ್ನು ಸದಾ ನಿರ್ವಹಿಸಿ.
- ನೈಜ ಸಮಯ ನವೀಕರಣಗಳನ್ನು ನೋಡಲು ಬಹು ಕ್ಲೈಂಟ್‌ಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ.
- ದೋಷಗಳು ಎದುರಾದರೆ, ನಿಮ್ಮ Python ಆವೃತ್ತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಎಲ್ಲಾ ಅವಲಂಬನೆಗಳು ಸ್ಥಾಪಿತವಾಗಿವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
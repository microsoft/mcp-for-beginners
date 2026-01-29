# How to run dis sample

Dis na how you go fit run di classic HTTP streaming server and client, plus di MCP streaming server and client wey dey use Python.

### Overview

- You go set up MCP server wey go dey send progress notifications to di client as e dey process items.
- Di client go dey show each notification as e dey happen.
- Dis guide go cover wetin you need, setup, how to run am, and how to solve problems.

### Wetin you need

- Python 3.9 or newer
- Di `mcp` Python package (install am wit `pip install mcp`)

### Installation & Setup

1. Clone di repository or download di solution files.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Create and activate virtual environment (e good make you do am):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Install di things wey you need:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Files

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### How to run di Classic HTTP Streaming Server

1. Enter di solution directory:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Start di classic HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. Di server go start and show dis:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### How to run di Classic HTTP Streaming Client

1. Open new terminal (activate di same virtual environment and directory):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. You go see di streamed messages wey go dey show one by one:

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

### How to run di MCP Streaming Server

1. Enter di solution directory:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Start di MCP server wit di streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. Di server go start and show dis:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### How to run di MCP Streaming Client

1. Open new terminal (activate di same virtual environment and directory):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. You go see notifications wey go dey show as di server dey process each item:
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

### Key Implementation Steps

1. **Create di MCP server wit FastMCP.**
2. **Define tool wey go process list and send notifications wit `ctx.info()` or `ctx.log()`.**
3. **Run di server wit `transport="streamable-http"`.**
4. **Make client wey go get message handler to show notifications as dem dey come.**

### Code Walkthrough
- Di server dey use async functions and MCP context to send progress updates.
- Di client dey use async message handler to show notifications and di final result.

### Tips & How to Solve Problems

- Use `async/await` for operations wey no go block.
- Always handle exceptions for both server and client to make am strong.
- Test am wit plenty clients to see di real-time updates.
- If you see errors, check your Python version and make sure say you don install all di things wey you need.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
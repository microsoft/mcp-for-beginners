# Running this sample

Here's how to run the classic HTTP streaming server and client, as well as the MCP streaming server and client using Python.

### Overview

- You will set up an MCP server that streams progress notifications to the client as it processes items.
- The client will display each notification in real time.
- This guide covers prerequisites, setup, running, and troubleshooting.

### Prerequisites

- Python 3.9 or newer
- The `mcp` Python package (install with `pip install mcp`)

### Installation & Setup

1. Clone the repository or download the solution files.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Create and activate a virtual environment (recommended):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Install required dependencies:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Files

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Client:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Running the Classic HTTP Streaming Server

1. Navigate to the solution directory:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Start the classic HTTP streaming server:

   ```pwsh
   python server.py
   ```

3. The server will start and display:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Running the Classic HTTP Streaming Client

1. Open a new terminal (activate the same virtual environment and directory):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. You should see streamed messages printed sequentially:

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

### Running the MCP Streaming Server

1. Navigate to the solution directory:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Start the MCP server with the streamable-http transport:
   ```pwsh
   python server.py mcp
   ```
3. The server will start and display:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Running the MCP Streaming Client

1. Open a new terminal (activate the same virtual environment and directory):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. You should see notifications printed in real time as the server processes each item:
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

1. **Create the MCP server using FastMCP.**
2. **Define a tool that processes a list and sends notifications using `ctx.info()` or `ctx.log()`.**
3. **Run the server with `transport="streamable-http"`.**
4. **Implement a client with a message handler to display notifications as they arrive.**

### Code Walkthrough
- The server uses async functions and the MCP context to send progress updates.
- The client implements an async message handler to print notifications and the final result.

### Tips & Troubleshooting

- Use `async/await` for non-blocking operations.
- Always handle exceptions in both server and client for robustness.
- Test with multiple clients to observe real-time updates.
- If you encounter errors, check your Python version and ensure all dependencies are installed.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
# 运行此示例

以下是如何使用 Python 运行经典 HTTP 流式服务器和客户端，以及 MCP 流式服务器和客户端的指南。

### 概述

- 您将设置一个 MCP 服务器，该服务器在处理项目时向客户端流式发送进度通知。
- 客户端将实时显示每条通知。
- 本指南涵盖了前提条件、设置、运行和故障排除。

### 前提条件

- Python 3.9 或更高版本
- `mcp` Python 包（通过 `pip install mcp` 安装）

### 安装与设置

1. 克隆仓库或下载解决方案文件。

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **创建并激活虚拟环境（推荐）：**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **安装所需依赖项：**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### 文件

- **服务器文件:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **客户端文件:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### 运行经典 HTTP 流式服务器

1. 进入解决方案目录：

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. 启动经典 HTTP 流式服务器：

   ```pwsh
   python server.py
   ```

3. 服务器将启动并显示：

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### 运行经典 HTTP 流式客户端

1. 打开一个新的终端（激活相同的虚拟环境并进入目录）：

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. 您应该会看到流式消息按顺序打印：

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

### 运行 MCP 流式服务器

1. 进入解决方案目录：
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. 使用 streamable-http 传输启动 MCP 服务器：
   ```pwsh
   python server.py mcp
   ```
3. 服务器将启动并显示：
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### 运行 MCP 流式客户端

1. 打开一个新的终端（激活相同的虚拟环境并进入目录）：
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. 您应该会看到通知随着服务器处理每个项目实时打印：
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

### 关键实现步骤

1. **使用 FastMCP 创建 MCP 服务器。**
2. **定义一个工具来处理列表，并使用 `ctx.info()` 或 `ctx.log()` 发送通知。**
3. **通过 `transport="streamable-http"` 运行服务器。**
4. **实现一个客户端，使用消息处理器显示到达的通知。**

### 代码讲解
- 服务器使用异步函数和 MCP 上下文发送进度更新。
- 客户端实现了一个异步消息处理器，用于打印通知和最终结果。

### 提示与故障排除

- 使用 `async/await` 进行非阻塞操作。
- 在服务器和客户端中始终处理异常以提高健壮性。
- 使用多个客户端进行测试以观察实时更新。
- 如果遇到错误，请检查您的 Python 版本并确保所有依赖项已安装。

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。
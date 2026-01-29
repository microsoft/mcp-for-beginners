# Chạy mẫu này

Dưới đây là cách chạy máy chủ và máy khách HTTP streaming cổ điển, cũng như máy chủ và máy khách MCP streaming sử dụng Python.

### Tổng quan

- Bạn sẽ thiết lập một máy chủ MCP để truyền thông báo tiến trình đến máy khách khi xử lý các mục.
- Máy khách sẽ hiển thị từng thông báo theo thời gian thực.
- Hướng dẫn này bao gồm các yêu cầu, thiết lập, cách chạy và xử lý sự cố.

### Yêu cầu

- Python 3.9 hoặc mới hơn
- Gói Python `mcp` (cài đặt bằng `pip install mcp`)

### Cài đặt & Thiết lập

1. Clone kho lưu trữ hoặc tải xuống các tệp giải pháp.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Tạo và kích hoạt môi trường ảo (khuyến nghị):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Cài đặt các phụ thuộc cần thiết:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Tệp

- **Máy chủ:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Máy khách:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Chạy máy chủ HTTP Streaming cổ điển

1. Điều hướng đến thư mục giải pháp:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Khởi động máy chủ HTTP streaming cổ điển:

   ```pwsh
   python server.py
   ```

3. Máy chủ sẽ khởi động và hiển thị:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Chạy máy khách HTTP Streaming cổ điển

1. Mở một terminal mới (kích hoạt cùng môi trường ảo và thư mục):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Bạn sẽ thấy các thông điệp được truyền tuần tự:

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

### Chạy máy chủ MCP Streaming

1. Điều hướng đến thư mục giải pháp:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Khởi động máy chủ MCP với giao thức streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Máy chủ sẽ khởi động và hiển thị:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Chạy máy khách MCP Streaming

1. Mở một terminal mới (kích hoạt cùng môi trường ảo và thư mục):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Bạn sẽ thấy các thông báo được hiển thị theo thời gian thực khi máy chủ xử lý từng mục:
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

### Các bước triển khai chính

1. **Tạo máy chủ MCP sử dụng FastMCP.**
2. **Định nghĩa một công cụ xử lý danh sách và gửi thông báo bằng `ctx.info()` hoặc `ctx.log()`.**
3. **Chạy máy chủ với `transport="streamable-http"`.**
4. **Triển khai máy khách với trình xử lý thông điệp để hiển thị thông báo khi chúng đến.**

### Giải thích mã
- Máy chủ sử dụng các hàm async và ngữ cảnh MCP để gửi cập nhật tiến trình.
- Máy khách triển khai một trình xử lý thông điệp async để in thông báo và kết quả cuối cùng.

### Mẹo & Xử lý sự cố

- Sử dụng `async/await` cho các hoạt động không chặn.
- Luôn xử lý ngoại lệ trong cả máy chủ và máy khách để đảm bảo độ tin cậy.
- Kiểm tra với nhiều máy khách để quan sát các cập nhật theo thời gian thực.
- Nếu gặp lỗi, kiểm tra phiên bản Python của bạn và đảm bảo tất cả các phụ thuộc đã được cài đặt.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
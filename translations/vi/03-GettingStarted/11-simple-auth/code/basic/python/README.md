# Chạy mẫu

Mẫu này khởi động một MCP Server với middleware kiểm tra tiêu đề Authorization hợp lệ.

## Cài đặt các phụ thuộc

```bash
pip install "mcp[cli]" 
```

## Khởi động server

```bash
python server.py
```

khởi động client trong một terminal khác

```bash
python client.py
```

Bạn sẽ thấy kết quả tương tự như:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Điều này có nghĩa là thông tin xác thực được gửi qua đã được chấp nhận.

Hãy thử thay đổi thông tin xác thực trong `client.py` thành "secret-token2", sau đó bạn sẽ thấy văn bản này là một phần của phản hồi:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Điều này có nghĩa là bạn đã được xác thực (bạn có thông tin xác thực), nhưng nó không hợp lệ.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
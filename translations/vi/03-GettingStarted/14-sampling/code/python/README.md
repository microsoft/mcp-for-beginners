# Chạy ví dụ

> [!WARNING]
> Ví dụ này sử dụng Sampling đã lỗi thời và điểm cuối HTTP+SSE cũ. Nó được
> giữ lại để tương thích với MCP `2025-11-25`. Các triển khai mới nên gọi trực tiếp
> nhà cung cấp LLM và sử dụng HTTP có khả năng streaming cho lưu lượng MCP từ xa.

## Tạo môi trường ảo

```sh
python -m venv venv
source ./venv/bin/activate
```

## Cài đặt các phụ thuộc

```sh
pip install "mcp[cli]"
```

## Chạy máy chủ

```sh
uvicorn server:app --port 8000
```

## Kiểm tra máy chủ với GitHub Copilot và VS Code

Thêm mục nhập vào mcp.json như sau:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Đảm bảo bạn nhấn "start" trên máy chủ.

Trong GitHub Copilot dán đoạn lệnh sau:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Lần đầu tiên bạn sẽ được hỏi có chấp nhận một hành động Sampling hay không, rồi sau đó sẽ được hỏi chấp nhận công cụ để chạy "create_blog". Bạn sẽ thấy phản hồi tương tự:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
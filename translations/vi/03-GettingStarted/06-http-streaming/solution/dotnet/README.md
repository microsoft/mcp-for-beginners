# Chạy mẫu này

## -1- Cài đặt các phụ thuộc

```bash
dotnet restore
```

## -2- Chạy mẫu

```bash
dotnet run
```

## -3- Kiểm tra mẫu

Mở một terminal riêng trước khi chạy lệnh dưới đây (đảm bảo rằng server vẫn đang chạy).

Khi server đang chạy trong một terminal, mở một terminal khác và chạy lệnh sau:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Điều này sẽ khởi động một server web với giao diện trực quan cho phép bạn kiểm tra mẫu.

> Đảm bảo rằng **Streamable HTTP** được chọn làm loại giao thức, và URL là `http://localhost:3001/mcp`.

Khi server đã kết nối:

- thử liệt kê các công cụ và chạy `add`, với tham số 2 và 4, bạn sẽ thấy kết quả là 6.
- vào phần tài nguyên và mẫu tài nguyên, gọi "greeting", nhập một tên và bạn sẽ thấy lời chào với tên bạn đã cung cấp.

### Kiểm tra trong chế độ CLI

Bạn có thể chạy trực tiếp trong chế độ CLI bằng cách chạy lệnh sau:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Điều này sẽ liệt kê tất cả các công cụ có sẵn trong server. Bạn sẽ thấy đầu ra như sau:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Để gọi một công cụ, nhập:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Bạn sẽ thấy đầu ra như sau:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Thông thường chạy trình kiểm tra trong chế độ CLI sẽ nhanh hơn nhiều so với trên trình duyệt.
> Đọc thêm về trình kiểm tra [tại đây](https://github.com/modelcontextprotocol/inspector).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
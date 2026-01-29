# Chạy mẫu này

## -1- Cài đặt các phụ thuộc

```bash
dotnet restore
```

## -3- Chạy mẫu

```bash
dotnet run
```

## -4- Kiểm tra mẫu

Với máy chủ đang chạy trong một terminal, mở một terminal khác và chạy lệnh sau:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Điều này sẽ khởi động một máy chủ web với giao diện trực quan cho phép bạn kiểm tra mẫu.

Khi máy chủ đã kết nối:

- thử liệt kê các công cụ và chạy `add`, với tham số 2 và 4, bạn sẽ thấy kết quả là 6.
- đi đến tài nguyên và mẫu tài nguyên, gọi "greeting", nhập một tên và bạn sẽ thấy lời chào với tên bạn đã cung cấp.

### Kiểm tra ở chế độ CLI

Bạn có thể khởi động trực tiếp ở chế độ CLI bằng cách chạy lệnh sau:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Điều này sẽ liệt kê tất cả các công cụ có sẵn trong máy chủ. Bạn sẽ thấy đầu ra sau:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Bạn sẽ thấy đầu ra sau:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Thông thường chạy trình kiểm tra ở chế độ CLI nhanh hơn nhiều so với trên trình duyệt.
> Đọc thêm về trình kiểm tra [tại đây](https://github.com/modelcontextprotocol/inspector).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
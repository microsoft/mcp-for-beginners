# MCP stdio Server - Giải pháp .NET

> **⚠️ Quan trọng**: Giải pháp này đã được cập nhật để sử dụng **giao thức stdio** theo khuyến nghị của MCP Specification 2025-06-18. Giao thức SSE ban đầu đã bị ngừng sử dụng.

## Tổng quan

Giải pháp .NET này minh họa cách xây dựng một máy chủ MCP sử dụng giao thức stdio hiện tại. Giao thức stdio đơn giản hơn, an toàn hơn và cung cấp hiệu suất tốt hơn so với phương pháp SSE đã bị ngừng sử dụng.

## Yêu cầu

- .NET 9.0 SDK hoặc mới hơn
- Hiểu biết cơ bản về dependency injection trong .NET

## Hướng dẫn thiết lập

### Bước 1: Khôi phục các phụ thuộc

```bash
dotnet restore
```

### Bước 2: Xây dựng dự án

```bash
dotnet build
```

## Chạy máy chủ

Máy chủ stdio hoạt động khác so với máy chủ HTTP trước đây. Thay vì khởi động một máy chủ web, nó giao tiếp thông qua stdin/stdout:

```bash
dotnet run
```

**Quan trọng**: Máy chủ sẽ có vẻ như bị treo - điều này là bình thường! Nó đang chờ các tin nhắn JSON-RPC từ stdin.

## Kiểm tra máy chủ

### Phương pháp 1: Sử dụng MCP Inspector (Khuyến nghị)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Điều này sẽ:
1. Khởi chạy máy chủ của bạn dưới dạng một tiến trình con
2. Mở giao diện web để kiểm tra
3. Cho phép bạn kiểm tra tất cả các công cụ của máy chủ một cách tương tác

### Phương pháp 2: Kiểm tra trực tiếp bằng dòng lệnh

Bạn cũng có thể kiểm tra bằng cách khởi chạy Inspector trực tiếp:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Các công cụ có sẵn

Máy chủ cung cấp các công cụ sau:

- **AddNumbers(a, b)**: Cộng hai số
- **MultiplyNumbers(a, b)**: Nhân hai số  
- **GetGreeting(name)**: Tạo lời chào cá nhân hóa
- **GetServerInfo()**: Lấy thông tin về máy chủ

### Kiểm tra với Claude Desktop

Để sử dụng máy chủ này với Claude Desktop, thêm cấu hình sau vào `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Cấu trúc dự án

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Những điểm khác biệt chính so với HTTP/SSE

**Giao thức stdio (Hiện tại):**
- ✅ Thiết lập đơn giản hơn - không cần máy chủ web
- ✅ Bảo mật tốt hơn - không có các điểm cuối HTTP
- ✅ Sử dụng `Host.CreateApplicationBuilder()` thay vì `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` thay vì `WithHttpTransport()`
- ✅ Ứng dụng console thay vì ứng dụng web
- ✅ Hiệu suất tốt hơn

**Giao thức HTTP/SSE (Đã ngừng sử dụng):**
- ❌ Yêu cầu máy chủ web ASP.NET Core
- ❌ Cần thiết lập định tuyến `app.MapMcp()`
- ❌ Cấu hình và phụ thuộc phức tạp hơn
- ❌ Các vấn đề bảo mật bổ sung
- ❌ Đã bị ngừng sử dụng trong MCP 2025-06-18

## Tính năng phát triển

- **Dependency Injection**: Hỗ trợ DI đầy đủ cho các dịch vụ và ghi log
- **Structured Logging**: Ghi log đúng cách vào stderr sử dụng `ILogger<T>`
- **Tool Attributes**: Định nghĩa công cụ rõ ràng bằng các thuộc tính `[McpServerTool]`
- **Hỗ trợ Async**: Tất cả các công cụ hỗ trợ hoạt động bất đồng bộ
- **Xử lý lỗi**: Xử lý lỗi và ghi log một cách linh hoạt

## Mẹo phát triển

- Sử dụng `ILogger` để ghi log (không bao giờ ghi trực tiếp vào stdout)
- Xây dựng với `dotnet build` trước khi kiểm tra
- Kiểm tra với Inspector để gỡ lỗi trực quan
- Tất cả ghi log tự động được chuyển vào stderr
- Máy chủ xử lý tín hiệu tắt một cách linh hoạt

Giải pháp này tuân theo đặc tả MCP hiện tại và minh họa các thực tiễn tốt nhất để triển khai giao thức stdio sử dụng .NET.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.